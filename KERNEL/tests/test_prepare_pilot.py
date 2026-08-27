from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = ROOT.parent
sys.path.insert(0, str(ROOT / "tools"))

from prepare_pilot import prepare  # noqa: E402


class PreparePilotTests(unittest.TestCase):
    def test_live_repository_is_refused(self):
        with self.assertRaisesRegex(ValueError, "live repository"):
            prepare(REPOSITORY, "1d9400425f7415083a9ffbd10964670bf255abf2", "2026-08-26T12:00:00.000000Z")

    def test_disposable_clone_gets_only_two_canonical_commands_and_ephemeral_manifests(self):
        with tempfile.TemporaryDirectory() as temporary:
            clone = Path(temporary) / "mirror"
            subprocess.run(["git", "clone", "-q", "--no-hardlinks", str(REPOSITORY), str(clone)], check=True)
            # Mirror the PINNED source commit, not the live HEAD: pilot LIVE-2026-0001
            # committed the real submissions at the exact path prepare() exclusive-creates,
            # so a HEAD-state mirror collides forever after the first live sitting (C8 N4).
            subprocess.run(
                ["git", "-C", str(clone), "checkout", "-q", "--detach", "1d9400425f7415083a9ffbd10964670bf255abf2"],
                check=True,
            )
            (clone / ".gate-c-synthetic-mirror.json").write_text(
                json.dumps({"authority": "NON_AUTHORITATIVE", "mode": "SYNTHETIC_MIRROR"}), encoding="utf-8"
            )
            report = prepare(clone, "1d9400425f7415083a9ffbd10964670bf255abf2", "2026-08-26T12:00:00.000000Z")
            self.assertEqual(len(report["submissions"]), 2)
            for relative in report["submissions"]:
                command = json.loads((clone / relative).read_text(encoding="utf-8"))
                self.assertEqual(command["actor_id"], "SAM")
                self.assertEqual(command["native_refs"][0]["source_commit"], "1d9400425f7415083a9ffbd10964670bf255abf2")
            self.assertTrue((clone / ".rw/rehearsal/inventory.json").exists())
            status = subprocess.run(
                ["git", "-C", str(clone), "status", "--porcelain"], check=True, capture_output=True, text=True
            ).stdout
            self.assertIn("AGENTS/SAM/outbox/kernel/", status)
            self.assertNotIn(".rw/", status)


if __name__ == "__main__":
    unittest.main()
