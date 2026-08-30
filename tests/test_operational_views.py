import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_operational_views.py"
SPEC = importlib.util.spec_from_file_location("operational_views", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


VALID_ROADMAP = MODULE.load("roadmap.json")
VALID_TASKS = MODULE.load("tasks.json")
VALID_SNAPSHOT = MODULE.load("snapshot.json")
VALID_DECISIONS = MODULE.load("decisions.json")


def _copy(data):
    import copy
    return copy.deepcopy(data)


class OperationalViewsTest(unittest.TestCase):
    def test_control_data_validates(self):
        MODULE.validate(
            MODULE.load("roadmap.json"),
            MODULE.load("tasks.json"),
            MODULE.load("snapshot.json"),
            MODULE.load("decisions.json"),
        )

    def test_commit_shorthand_validates(self):
        self.assertTrue(MODULE._commit_sha("d221fafd34d97be35a67b52cf77ef97bf08cbf4a"))
        self.assertTrue(MODULE._commit_sha("0" * 40))
        self.assertFalse(MODULE._commit_sha("None"))
        self.assertFalse(MODULE._commit_sha("short"))
        self.assertFalse(MODULE._commit_sha("zz" + "0" * 38))
        self.assertFalse(MODULE._commit_sha(None))
        self.assertFalse(MODULE._commit_sha(12345))

    def test_every_blocked_task_has_blocker(self):
        snapshot = MODULE.load("snapshot.json")
        tasks = MODULE.load("tasks.json")
        MODULE.validate(MODULE.load("roadmap.json"), tasks, snapshot, MODULE.load("decisions.json"))

    def test_ruleset_fields_have_expected_types(self):
        snapshot = MODULE.load("snapshot.json")
        for rs in snapshot.get("rulesets", []):
            self.assertIsInstance(rs["id"], str)
            self.assertIsInstance(rs["name"], str)
            self.assertIsInstance(rs["status"], str)
            self.assertIsInstance(rs["target"], str)
            self.assertIsInstance(rs["requires_pull_requests"], bool)
            self.assertIsInstance(rs["requires_review_thread_resolution"], bool)
            self.assertIsInstance(rs["requires_strict_verify_status_checks"], bool)
            self.assertIsInstance(rs["blocks_force_pushes"], bool)
            self.assertIsInstance(rs["blocks_deletion"], bool)
            self.assertIsInstance(rs["requires_approvals"], int)
            self.assertIsInstance(rs["bypass_actors"], list)

    def test_committed_views_are_current(self):
        for path, expected in MODULE.render_all().items():
            self.assertTrue(path.exists(), f"missing generated view: {path.name}")
            self.assertEqual(expected, path.read_text(encoding="utf-8"), path.name)

    def test_every_root_view_declares_it_is_generated(self):
        for path in MODULE.render_all():
            first_line = path.read_text(encoding="utf-8").splitlines()[0]
            self.assertEqual(MODULE.GENERATED_NOTICE, first_line)

    def test_null_commit_rejected_before_generated_view_accepted(self):
        snapshot = _copy(VALID_SNAPSHOT)
        snapshot["history"] = [
            {
                "date": "2026-08-29",
                "commit": None,
                "summary": "A reconciliation entry with no commit.",
            }
        ]
        with self.assertRaises(ValueError):
            MODULE.validate(VALID_ROADMAP, VALID_TASKS, snapshot, VALID_DECISIONS)

    def test_malformed_history_sha_rejected(self):
        snapshot = _copy(VALID_SNAPSHOT)
        snapshot["history"] = [
            {
                "date": "2026-08-29",
                "commit": "not-a-valid-sha",
                "summary": "Malformed SHA.",
            }
        ]
        with self.assertRaises(ValueError):
            MODULE.validate(VALID_ROADMAP, VALID_TASKS, snapshot, VALID_DECISIONS)

    def test_blocked_task_without_blocker_rejected(self):
        tasks = _copy(VALID_TASKS)
        for task in tasks["tasks"]:
            if task["id"] == "REL-01-02":
                task["status"] = "blocked"
        snapshot = _copy(VALID_SNAPSHOT)
        snapshot["blockers"] = []
        with self.assertRaises(ValueError):
            MODULE.validate(VALID_ROADMAP, tasks, snapshot, VALID_DECISIONS)

    def test_blocker_without_existing_task_rejected(self):
        snapshot = _copy(VALID_SNAPSHOT)
        snapshot["blockers"] = [
            {
                "id": "GHOST-B01",
                "severity": "high",
                "task_id": "NONEXISTENT-TASK",
                "description": "A blocker that references a task that does not exist.",
            }
        ]
        with self.assertRaises(ValueError):
            MODULE.validate(VALID_ROADMAP, VALID_TASKS, snapshot, VALID_DECISIONS)

    def test_duplicate_decision_ids_rejected(self):
        decisions = _copy(VALID_DECISIONS)
        decisions["decisions"] = [
            {"id": "D1", "status": "accepted", "title": "First", "decision": "X", "source": "x"},
            {"id": "D1", "status": "accepted", "title": "Duplicate", "decision": "Y", "source": "y"},
        ]
        with self.assertRaises(ValueError):
            MODULE.validate(VALID_ROADMAP, VALID_TASKS, VALID_SNAPSHOT, decisions)

    def test_ruleset_requires_approvals_boolean_rejected(self):
        snapshot = _copy(VALID_SNAPSHOT)
        for rs in snapshot.get("rulesets", []):
            rs["requires_approvals"] = True
        with self.assertRaises(ValueError):
            MODULE.validate(VALID_ROADMAP, VALID_TASKS, snapshot, VALID_DECISIONS)

    def test_ruleset_requires_approvals_negative_rejected(self):
        snapshot = _copy(VALID_SNAPSHOT)
        for rs in snapshot.get("rulesets", []):
            rs["requires_approvals"] = -1
        with self.assertRaises(ValueError):
            MODULE.validate(VALID_ROADMAP, VALID_TASKS, snapshot, VALID_DECISIONS)

    def test_ruleset_non_boolean_field_rejected(self):
        snapshot = _copy(VALID_SNAPSHOT)
        for rs in snapshot.get("rulesets", []):
            rs["requires_pull_requests"] = "yes"
        with self.assertRaises(ValueError):
            MODULE.validate(VALID_ROADMAP, VALID_TASKS, snapshot, VALID_DECISIONS)


    def test_overall_framework_count_rendered_from_task_data(self):
        tasks = _copy(VALID_TASKS)
        modified = False
        for task in tasks["tasks"]:
            if task["status"] == "pending":
                task["status"] = "verified"
                task["commit"] = "0" * 40
                task["evidence"] = ["test-only-evidence.md"]
                modified = True
                break
        self.assertTrue(modified, "expected at least one pending task to convert")

        roadmap = _copy(VALID_ROADMAP)
        snapshot = _copy(VALID_SNAPSHOT)
        MODULE.validate(roadmap, tasks, snapshot, VALID_DECISIONS)

        status_text = MODULE.status_view(roadmap, tasks, snapshot)

        self.assertIn("3 / 13 Tasks Verified\n\n## 2. Itemized Verification Checklist", status_text)
        self.assertNotIn("2 / 13 Tasks Verified", status_text)

if __name__ == "__main__":
    unittest.main()
