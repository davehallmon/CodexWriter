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
        )

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
