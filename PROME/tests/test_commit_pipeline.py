"""Real temporary repositories exercise failure ordering and literal path isolation."""
import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

SCRIPT = Path(__file__).resolve().parents[1] / "tools/commit_check.py"


class CommitPipelineTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        (self.root / "owned.txt").write_text("old")
        (self.root / "foreign.txt").write_text("old")
        self.git("add", "--", "owned.txt", "foreign.txt")
        self.git("commit", "-qm", "fixture base")
        self.before = self.git("rev-parse", "HEAD").stdout
        (self.root / "owned.txt").write_text("new")
        (self.root / "foreign.txt").write_text("foreign staged work")
        self.git("add", "--", "foreign.txt")
        (self.root / "msg.txt").write_text("PROME: fixture scoped change\n")
        (self.root / "scripts").mkdir()
        (self.root / "scripts/safe-push.sh").write_text("#!/bin/sh\nprintf pushed > push-marker\n")

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.root, capture_output=True, text=True, check=True)

    def pipeline(self, *paths, strict=False):
        return subprocess.run([sys.executable, str(SCRIPT), "commit", "--stage", "--push",
            *(["--strict-message"] if strict else []), "-F", "msg.txt", "--", *(paths or ("owned.txt",))],
            cwd=self.root, capture_output=True, text=True)

    def test_success_leaves_foreign_staging_and_commits_only_literal_wildcard_file(self):
        (self.root / "literal*.txt").write_text("ours")
        (self.root / "literal-neighbor.txt").write_text("not ours")
        result = self.pipeline("owned.txt", "literal*.txt")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        paths = set(self.git("show", "--format=", "--name-only", "HEAD").stdout.splitlines())
        self.assertEqual(paths, {"owned.txt", "literal*.txt"})
        self.assertEqual(self.git("diff", "--cached", "--name-only").stdout.strip(), "foreign.txt")
        self.assertTrue((self.root / "push-marker").exists())

    def test_git_mv_rename_commits_in_one_batch_naming_both_paths(self):
        # PROME 2026-09-10: `git add` on a git-mv source path aborted the batch ("did not match any files").
        self.git("mv", "owned.txt", "renamed.txt")
        result = self.pipeline("owned.txt", "renamed.txt")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("already staged as deleted/renamed", result.stdout)
        status = self.git("show", "--format=", "--name-status", "--no-renames", "HEAD").stdout.split()
        self.assertEqual(status, ["D", "owned.txt", "A", "renamed.txt"])
        self.assertEqual(self.git("diff", "--cached", "--name-only").stdout.strip(), "foreign.txt")

    def test_unstaged_deletion_of_tracked_file_is_staged_and_committed(self):
        (self.root / "owned.txt").unlink()
        result = self.pipeline("owned.txt")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        status = self.git("show", "--format=", "--name-status", "--no-renames", "HEAD").stdout.split()
        self.assertEqual(status, ["D", "owned.txt"])

    def test_stage_failure_stops_commit_and_push(self):
        (self.root / ".git/index.lock").write_text("fixture lock")
        result = self.pipeline()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("git add failed", result.stdout)
        self.assertEqual(self.git("rev-parse", "HEAD").stdout, self.before)
        self.assertFalse((self.root / "push-marker").exists())

    def test_commit_failure_stops_push_and_preserves_index(self):
        hook = self.root / ".git/hooks/pre-commit"
        hook.write_text("#!/bin/sh\nexit 1\n")
        hook.chmod(0o755)
        result = self.pipeline()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.git("rev-parse", "HEAD").stdout, self.before)
        self.assertFalse((self.root / "push-marker").exists())
        self.assertIn("foreign.txt", self.git("diff", "--cached", "--name-only").stdout)

    def test_verification_failure_stops_push_after_commit(self):
        (self.root / "msg.txt").write_text("PROME: fixture scoped change\n\nClaims `foreign.txt` edited.\n")
        result = self.pipeline(strict=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertNotEqual(self.git("rev-parse", "HEAD").stdout, self.before)
        self.assertFalse((self.root / "push-marker").exists())

    def test_directory_and_symlink_refused_before_staging(self):
        (self.root / "alias.txt").symlink_to("owned.txt")
        for path in (".", "alias.txt"):
            with self.subTest(path=path):
                result = self.pipeline(path)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(self.git("rev-parse", "HEAD").stdout, self.before)
                self.assertFalse((self.root / "push-marker").exists())

    def test_status_failure_prevents_mutations(self):
        old_cwd = Path.cwd()
        try:
            os.chdir(self.root)
            spec = importlib.util.spec_from_file_location("commit_fixture", SCRIPT)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            with mock.patch.object(module.subprocess, "run", return_value=subprocess.CompletedProcess([], 1, b"", b"failed")) as run:
                self.assertEqual(module.do_commit("msg.txt", ["owned.txt"], False, [], stage=True), 2)
                self.assertEqual(run.call_count, 1)
                self.assertIn("status", run.call_args.args[0])
        finally:
            os.chdir(old_cwd)


if __name__ == "__main__":
    unittest.main()
