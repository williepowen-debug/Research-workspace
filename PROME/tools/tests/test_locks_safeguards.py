#!/usr/bin/env python3
"""Behavioral tests use snapshots in disposable repositories, never live refs/config."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[3]
FILES = (
    "scripts/githooks/commit-msg", "scripts/githooks/pre-commit", "scripts/githooks/pre-push",
    "PROME/tools/docket_row_cap.py", "scripts/harness_caps.env",
    "scripts/install-git-hooks.sh", "scripts/install-claude-hooks.py",
    "scripts/session_banner.sh", "scripts/safe-push.sh", "scripts/claim_check.py",
    "scripts/pipeline_rc_guard.py", "PROME/tools/hooks/pipeline_rc_block.py",
    "PROME/tools/hooks/commit_subject_guard.py", ".claude/settings.json",
)


class Safeguards(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="locks-test-")
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.repo = self.base / "repo"
        self.repo.mkdir()
        for relative in FILES:
            target = self.repo / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(SOURCE / relative, target)
        (self.repo / "PROME/ROSTER.md").write_text("fixture fingerprint\n")
        self.git("init", "-q", "-b", "master")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "commit.gpgsign", "false")
        self.git("commit", "-q", "--allow-empty", "-m", "Fixture baseline")

    def run_command(self, *args, cwd=None, env=None, input=None):
        return subprocess.run(args, cwd=cwd or self.repo, env=env, input=input,
                              capture_output=True, text=True)

    def git(self, *args, check=True, env=None):
        result = self.run_command("git", *args, env=env)
        if check:
            self.assertEqual(result.returncode, 0, result.stderr)
        return result

    def install(self):
        return self.run_command("bash", "scripts/install-git-hooks.sh")

    def test_subject_boundaries_and_paragraphs(self):
        self.assertEqual(self.install().returncode, 0)
        for message, expected in [("x" * 100, 0), ("x" * 101, 1),
                                  ("x" * 60 + "\n" + "y" * 60, 1),
                                  ("x" * 40 + "\n" + "y" * 40, 0),
                                  ("\n\nShort\n\n" + "x" * 200, 0),
                                  ("x" * 50 + "\n  " + "y" * 48, 1)]:
            with self.subTest(message=message):
                result = self.git("commit", "--allow-empty", "-m", message, check=False)
                self.assertEqual(result.returncode, expected, result.stderr)

    def test_file_comment_and_unicode(self):
        self.assertEqual(self.install().returncode, 0)
        for message, expected in [("#" + "x" * 101, 1), ("e\u0301" * 60, 0),
                                  ("é" * 60, 0), ("é" * 101, 1)]:
            with self.subTest(message=message):
                msg = self.base / "message"
                msg.write_text(message, encoding="utf-8")
                result = self.git("commit", "--allow-empty", "--cleanup=verbatim", "-F", str(msg),
                                  check=False, env=dict(os.environ, LC_ALL="C"))
                self.assertEqual(result.returncode, expected, result.stderr)

    def test_message_read_and_cleanup_errors_fail_closed(self):
        hook = str(self.repo / "scripts/githooks/commit-msg")
        self.assertNotEqual(self.run_command(hook, str(self.base / "missing")).returncode, 0)
        invalid = self.base / "invalid"
        invalid.write_bytes(b"\xff")
        self.assertNotEqual(self.run_command(hook, str(invalid)).returncode, 0)
        shim = self.base / "bin"
        shim.mkdir()
        bad_git = shim / "git"
        bad_git.write_text("#!/bin/sh\nexit 128\n")
        bad_git.chmod(0o755)
        msg = self.base / "message"
        msg.write_text("Short")
        env = dict(os.environ, PATH=str(shim) + ":" + os.environ["PATH"])
        self.assertNotEqual(self.run_command(hook, str(msg), env=env).returncode, 0)

    def test_installer_idempotent_and_custom_path_preserved(self):
        self.assertEqual(self.install().returncode, 0)
        self.assertEqual(self.install().returncode, 0)
        self.git("config", "core.hooksPath", "other-hooks")
        self.assertNotEqual(self.install().returncode, 0)
        self.assertEqual(self.git("config", "--get", "core.hooksPath").stdout.strip(), "other-hooks")

    def test_default_prepare_commit_hook_preserved(self):
        hook = self.repo / ".git/hooks/prepare-commit-msg"
        hook.write_text("#!/bin/sh\nexit 0\n")
        hook.chmod(0o755)
        self.assertNotEqual(self.install().returncode, 0)
        self.assertEqual(self.git("config", "--get", "core.hooksPath", check=False).returncode, 1)
        self.assertTrue(hook.is_file())

    def test_config_lock_and_missing_hook_not_installed(self):
        lock = self.repo / ".git/config.lock"
        lock.write_text("another writer")
        self.assertNotEqual(self.install().returncode, 0)
        lock.unlink()
        (self.repo / "scripts/githooks/pre-push").chmod(0o644)
        self.assertNotEqual(self.install().returncode, 0)

    def test_push_fast_forward_rollback_delete_unknown(self):
        origin = self.base / "origin.git"
        self.assertEqual(self.run_command("git", "init", "--bare", "-q", str(origin)).returncode, 0)
        self.git("remote", "add", "origin", str(origin))
        self.assertEqual(self.install().returncode, 0)
        self.git("push", "origin", "HEAD:master")
        old = self.git("rev-parse", "HEAD").stdout.strip()
        self.git("commit", "--allow-empty", "-m", "Next fixture")
        self.git("push", "origin", "HEAD:master")
        self.assertNotEqual(self.git("push", "--force", "origin", old + ":master", check=False).returncode, 0)
        self.assertNotEqual(self.git("push", "--force-with-lease", "origin", old + ":master", check=False).returncode, 0)
        self.assertNotEqual(self.git("push", "origin", ":master", check=False).returncode, 0)
        head = self.git("rev-parse", "HEAD").stdout.strip()
        result = self.run_command(str(self.repo / "scripts/githooks/pre-push"),
                                  input="refs/heads/master " + head + " refs/heads/master " + "f" * 40 + "\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("UNKNOWN", result.stderr)
        # Explicit client bypass still works; only server policy closes this path.
        self.git("push", "--no-verify", "--force", "origin", old + ":master")

    def test_safe_push_from_subdirectory(self):
        origin = self.base / "origin.git"
        self.assertEqual(self.run_command("git", "init", "--bare", "-q", str(origin)).returncode, 0)
        self.git("remote", "add", "origin", str(origin))
        self.git("push", "origin", "HEAD:master")
        self.git("commit", "--allow-empty", "-m", "Next fixture")
        result = self.run_command("bash", "../scripts/safe-push.sh", "--dry-run", cwd=self.repo / "PROME")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("[--dry-run]", result.stdout)

    def test_shallow_failure_withholds_graph_counts(self):
        shim = self.base / "bin"
        shim.mkdir()
        real_git = shutil.which("git")
        script = shim / "git"
        script.write_text('#!/bin/bash\nif [ "$*" = "rev-parse --is-shallow-repository" ]; then echo true; exit 0; fi\n'
                          'if [ "$1" = fetch ]; then if [ "$2" = --unshallow ]; then exit 1; fi; exit 0; fi\n'
                          'if [ "$1" = rev-list ]; then echo "0 0"; exit 0; fi\n'
                          'exec ' + real_git + ' "$@"\n')
        script.chmod(0o755)
        result = self.run_command("bash", "scripts/session_banner.sh", env=dict(os.environ, PATH=str(shim) + ":" + os.environ["PATH"]))
        self.assertEqual(result.returncode, 0)
        self.assertIn("UNSHALLOW FAILED", result.stdout)
        self.assertIn("ancestry UNVERIFIED", result.stdout)
        self.assertNotIn("repo 0/0", result.stdout)

    def test_advisory_has_context_without_permission_decision(self):
        result = self.run_command(sys.executable, "PROME/tools/hooks/pipeline_rc_block.py",
                                  input=json.dumps({"tool_name": "Bash", "tool_input": {
                                      "command": 'python3 scripts/validate_all.py | tail -1; echo "RC=$?"'}}))
        self.assertEqual(result.returncode, 0)
        output = json.loads(result.stdout)["hookSpecificOutput"]
        self.assertEqual(output["hookEventName"], "PreToolUse")
        self.assertTrue(output["additionalContext"])
        self.assertNotIn("permissionDecision", output)
        self.assertEqual(self.run_command(sys.executable, "PROME/tools/hooks/pipeline_rc_block.py", "--selftest").returncode, 0)

    def test_claim_selftest(self):
        self.assertEqual(self.run_command(sys.executable, "scripts/claim_check.py", "--selftest").returncode, 0)

    def test_settings_merge_preserves_other_keys_and_is_idempotent(self):
        target = self.base / "settings.json"
        original = {"permissions": {"deny": ["Bash(rm *)"]}, "model": "keep", "hooks": {
            "Stop": [{"hooks": [{"type": "command", "command": "other-hook"}]}]}}
        target.write_text(json.dumps(original))
        argv = (sys.executable, "scripts/install-claude-hooks.py", "--settings-file", str(target))
        self.assertEqual(self.run_command(*argv).returncode, 0)
        merged = json.loads(target.read_text())
        self.assertEqual(merged["permissions"], original["permissions"])
        self.assertEqual(merged["hooks"]["Stop"], original["hooks"]["Stop"])
        before = target.read_bytes()
        self.assertEqual(self.run_command(*argv).returncode, 0)
        self.assertEqual(target.read_bytes(), before)
        backups = list(self.base.glob("settings.json.fleet-backup-*"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(json.loads(backups[0].read_text()), original)

    def test_existing_fleet_command_metadata_repaired(self):
        source = json.loads((self.repo / ".claude/settings.json").read_text())
        desired = source["hooks"]["SessionStart"][0]["hooks"][0]
        original = dict(desired, timeout=1, **{"async": True})
        target = self.base / "settings.json"
        target.write_text(json.dumps({"hooks": {"SessionStart": [{"hooks": [original]}]}}))
        result = self.run_command(sys.executable, "scripts/install-claude-hooks.py", "--settings-file", str(target))
        self.assertEqual(result.returncode, 0, result.stderr)
        installed = json.loads(target.read_text())["hooks"]["SessionStart"][0]["hooks"][0]
        self.assertEqual(installed, desired)
        self.assertNotIn("async", installed)

    def test_dispatch_wrong_repo_and_legacy_fallback(self):
        settings = json.loads((self.repo / ".claude/settings.json").read_text())
        unrelated = self.base / "unrelated"
        unrelated.mkdir()
        self.assertEqual(self.run_command("git", "init", "-q", cwd=unrelated).returncode, 0)
        for groups in settings["hooks"].values():
            for group in groups:
                for hook in group["hooks"]:
                    result = self.run_command("bash", "-c", hook["command"], cwd=unrelated, input="{}")
                    self.assertEqual(result.returncode, 0)
                    self.assertEqual(result.stdout, "")
        fallback = settings["hooks"]["PreToolUse"][0]["hooks"][1]["command"]
        packet = json.dumps({"tool_name": "Bash", "tool_input": {"command": "git commit -m '" + "x" * 101 + "'"}})
        self.git("config", "core.hooksPath", "custom")
        self.assertEqual(self.run_command("bash", "-c", fallback, input=packet).returncode, 2)
        self.git("config", "--unset", "core.hooksPath")
        self.assertEqual(self.install().returncode, 0)
        self.assertEqual(self.run_command("bash", "-c", fallback, input=packet).returncode, 0)


if __name__ == "__main__":
    unittest.main()
