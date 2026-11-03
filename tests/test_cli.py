import sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from agentsync.cli import main

class T(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp(); self.r = Path(self.d)
    def run_(self, *a): return main(["--root", self.d, *a])
    def test_flow(self):
        self.assertEqual(self.run_("init"), 0)
        self.assertEqual(self.run_("sync", "--check"), 1)
        self.assertEqual(self.run_("sync"), 0)
        self.assertEqual(self.run_("sync", "--check"), 0)
        self.assertTrue((self.r / "GEMINI.md").exists())
        self.assertTrue((self.r / ".claude/skills/example/SKILL.md").exists())
        (self.r / "AGENTS.md").write_text("# changed\n")
        self.assertEqual(self.run_("sync", "--check"), 1)
        self.run_("sync"); self.assertEqual(self.run_("sync", "--check"), 0)
    def test_never_overwrites_foreign(self):
        (self.r / "CLAUDE.md").write_text("my hand-written rules")
        (self.r / "AGENTS.md").write_text("x")
        self.run_("sync")
        self.assertEqual((self.r / "CLAUDE.md").read_text(), "my hand-written rules")
    def test_adopt(self):
        (self.r / "CLAUDE.md").write_text("# my rules\n")
        self.run_("init"); self.assertEqual((self.r / "AGENTS.md").read_text(), "# my rules\n")
        self.run_("sync", "--force"); self.assertIn("agentsync:generated", (self.r / "CLAUDE.md").read_text())
    def test_doctor_secret(self):
        self.run_("init"); (self.r / "AGENTS.md").write_text("key sk-" + "a" * 30)
        self.assertEqual(self.run_("doctor"), 1)

if __name__ == "__main__": unittest.main()
