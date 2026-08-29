import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "generate_operational_views.py"
SPEC = importlib.util.spec_from_file_location("operational_views", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


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


if __name__ == "__main__":
    unittest.main()
