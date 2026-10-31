"""Real Git/SQLite fixtures for the daily desk. Never submits a live response."""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import uuid

import app
import delivery
from pilot_files import Repo, encoded, read_receipts
from queue_store import QueueStore, REPLIES, open_rows, validate_reply
from store import reader


class DeskTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="cato-desk-test-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "repo"; self.root.mkdir()
        self.git("init", "-q", "-b", "master")
        self.git("config", "user.name", "Fixture author")
        self.git("config", "user.email", "fixture@example.invalid")
        self.text = "## OPEN\n\n| # | Item | Type | Needed by | Since | PROME rec | Notes |\n|---|---|---|---|---|---|---|\n| 901 | A: one task; B: no task. Literal \\| pipe. | DECISION | 2026-11-06 | 10/30 | A with a condition | Exact caveat |\n| 902 | Upload the report | HANDS | 2026-11-06 | 10/30 | When available | Do not upload credentials |\n\n## RECENTLY DONE\n"
        self.put("PROME/WILL_QUEUE.md", self.text)
        self.put("PROME/DOCKET.tsv", "fixture\n")
        self.put("PROME/GATES.tsv", "fixture\n")
        self.put("scripts/claim_check.py", "raise SystemExit(0)\n")
        self.put("scripts/orphan_check.sh", "exit 0\n")
        self.put("scripts/install-git-hooks.sh", "exit 0\n")
        self.put("scripts/safe-push.sh", (reader.ROOT / "scripts/safe-push.sh").read_text())
        self.commit()
        self.remote = Path(self.tmp.name) / "remote.git"
        subprocess.run(["git", "init", "-q", "--bare", str(self.remote)], check=True)
        self.git("remote", "add", "origin", str(self.remote))
        self.git("push", "-qu", "origin", "master")
        self.repo = Repo(self.root)
        self.store = QueueStore(Path(self.tmp.name) / "store.sqlite3", self.repo, "901", True)
        self.display = self.store.display()

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, text=True, stderr=subprocess.PIPE)

    def put(self, path, text):
        p = self.root / path; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text)
        return p

    def commit(self, publish=False):
        self.git("add", "--all"); self.git("commit", "-qm", "Fixture")
        if publish:
            self.git("push", "-q", "origin", "master")

    def request(self, **changes):
        r = {"id": uuid.uuid4().hex, "display_hash": self.display["hash"], "unit_id": "901.queue",
             "action": "reply", "choice_id": None, "note": "A, only if the report includes the caveat.\nNo schedule.",
             "revisit": "", "supersedes": None}
        r.update(changes); return r

    def test_reuses_owner_parser_and_preserves_literal_pipe_and_words(self):
        rows = open_rows(self.text)
        self.assertEqual(set(rows), {"901", "902"})
        self.assertIn("\\|", rows["901"]["row"])
        event = self.store.save(self.request())
        validate_reply(self.repo, event, "901")
        self.assertIsNone(event["selected_choice"])
        self.assertEqual(event["request"]["note"], "A, only if the report includes the caveat.\nNo schedule.")
        self.assertEqual(event["display"]["queue_row"], rows["901"]["row"])

    def test_duplicate_or_shifted_rows_are_not_silently_dropped(self):
        for text in [self.text.replace("## RECENTLY DONE", self.text.splitlines()[4]+"\n## RECENTLY DONE"),
                     self.text.replace("Exact caveat", "Extra | column")]:
            with self.assertRaises(ValueError): open_rows(text)

    def test_empty_open_is_supported_only_with_valid_table(self):
        empty = "\n".join(l for l in self.text.splitlines() if not l.startswith(("| 901", "| 902")))
        self.assertEqual(open_rows(empty), {})
        with self.assertRaises(ValueError): open_rows("## OPEN\nmissing table")

    def test_changed_or_unpublished_terms_block_stale_save(self):
        self.put("PROME/WILL_QUEUE.md", self.text.replace("Exact caveat", "New condition"))
        with self.assertRaisesRegex(ValueError, "not yet published"): self.store.save(self.request())
        self.commit()
        with self.assertRaisesRegex(ValueError, "not yet published"): self.store.save(self.request())
        self.git("push", "-q", "origin", "master")
        with self.assertRaisesRegex(ValueError, "Terms changed"): self.store.save(self.request())

    def test_read_only_and_blank_response_cannot_export(self):
        self.store.enabled = False
        with self.assertRaisesRegex(ValueError, "acceptance"): self.store.save(self.request())
        self.store.enabled = True
        with self.assertRaisesRegex(ValueError, "needs your words"): self.store.save(self.request(note=""))
        self.assertFalse((self.root / REPLIES).exists())

    def test_task_report_is_not_a_ruling_and_deferral_preserves_condition(self):
        task = QueueStore(Path(self.tmp.name) / "task.sqlite3", self.repo, "902", True)
        d = task.display()
        e = task.save(self.request(display_hash=d["hash"], unit_id="902.queue", action="report_done", note="Uploaded report"))
        self.assertIsNone(e["selected_choice"])
        self.assertIsNone(task.display()["receipt"])
        r = self.request(display_hash=d["hash"], unit_id="902.queue", action="defer", note="Need replacement report",
                         revisit="When corrected filing arrives", supersedes=e["id"])
        self.assertEqual(task.save(r)["request"]["revisit"], r["revisit"])

    def test_publication_preserves_other_staged_work_and_retry_is_idempotent(self):
        e = self.store.save(self.request())
        self.put("foreign.txt", "Another owner's work")
        self.git("add", "foreign.txt")
        result = delivery.deliver(self.repo, e)
        self.assertEqual(delivery.delivery_state(self.repo, e), "delivered")
        self.assertEqual(self.git("diff", "--cached", "--name-only").strip(), "foreign.txt")
        self.assertEqual(self.git("show", "--format=", "--name-only", result["commit"]).splitlines(),
                         sorted([delivery.event_path(e), result["packet"]]))
        before = self.git("rev-parse", "HEAD")
        delivery.deliver(self.repo, e)
        self.assertEqual(self.git("rev-parse", "HEAD"), before)

    def test_clone_restores_exact_reply_and_closed_queue_keeps_history(self):
        e = self.store.save(self.request()); delivery.deliver(self.repo, e)
        clone = Path(self.tmp.name) / "clone"
        subprocess.run(["git", "clone", "-q", "-b", "master", str(self.remote), str(clone)], check=True)
        restored = QueueStore(Path(self.tmp.name) / "clone.sqlite3", Repo(clone), "901")
        self.assertEqual(restored.display()["events"], [e])
        self.put("PROME/WILL_QUEUE.md", "\n".join(l for l in self.text.splitlines() if not l.startswith("| 901")))
        self.commit(publish=True)
        d = self.store.display()
        self.assertEqual(d["last"], e)
        self.assertFalse(d["can_respond"])
        self.assertTrue(d["errors"])

    def test_export_failure_keeps_saved_answer_and_retry_does_not_duplicate(self):
        r = self.request()
        with patch("queue_store.immutable_export", side_effect=OSError("fixture disk failure")):
            with self.assertRaisesRegex(ValueError, "Saved locally"): self.store.save(r)
        self.assertEqual(len(self.store.responses()["events"]), 1)
        self.assertEqual(self.store.save(r)["id"], r["id"])
        self.assertEqual(len(self.store.responses()["events"]), 1)

    def test_sync_preserves_dirty_owner_work_when_origin_moves(self):
        other = Path(self.tmp.name) / "other"
        subprocess.run(["git", "clone", "-q", "-b", "master", str(self.remote), str(other)], check=True)
        for key, value in [("user.name", "Fixture"), ("user.email", "fixture@example.invalid")]:
            subprocess.run(["git", "config", key, value], cwd=other, check=True)
        (other / "remote.txt").write_text("remote")
        for args in [["add", "remote.txt"], ["commit", "-qm", "Remote fixture"], ["push", "-q"]]:
            subprocess.run(["git", *args], cwd=other, check=True)
        self.put("PROME/WILL_QUEUE.md", self.text + "Owner work\n")
        before = self.git("rev-parse", "HEAD")
        result = delivery.sync(self.repo)
        self.assertIn("must be reconciled", result["message"])
        self.assertEqual(self.git("rev-parse", "HEAD"), before)
        self.assertTrue((self.root / "PROME/WILL_QUEUE.md").read_text().endswith("Owner work\n"))

    def test_real_desk_shows_closed_pilot_and_current_queue_without_new_answers(self):
        desk = app.Desk(Repo(reader.ROOT), Path(self.tmp.name) / "actual-read", False)
        d = desk.display()
        pilot = next(c for c in d["cards"] if c["wq_id"] == "558")
        self.assertFalse(pilot["errors"])
        self.assertEqual(pilot["group"], "History")
        self.assertEqual(pilot["receipt"]["state"], "integrated")
        self.assertTrue(pilot["completion"])
        self.assertTrue(all(not c["can_respond"] for c in d["cards"]))

    def test_owner_receipt_needs_published_ruling_and_stays_distinct_from_completion(self):
        import owner_receipt
        e = self.store.save(self.request()); delivery.deliver(self.repo, e)
        self.assertEqual(owner_receipt.load_event(self.repo, e["id"]), e)
        with self.assertRaisesRegex(ValueError, "requires published"):
            owner_receipt.prepare(self.repo, e, "integrated")
        self.put("PROME/proposals/fixture-RULED.md", "Fictional owner ruling plus matching confirmation")
        self.commit()
        ref = {"path": "PROME/proposals/fixture-RULED.md", "commit": self.git("rev-parse", "HEAD").strip()}
        with self.assertRaises(subprocess.CalledProcessError):
            owner_receipt.prepare(self.repo, e, "integrated", ref, ref)
        self.git("push", "-q", "origin", "master")
        receipt = owner_receipt.prepare(self.repo, e, "integrated", ref, ref)
        self.put(f"PROME/decisions/receipts/{e['id']}/{receipt['id']}.json", encoded(receipt) + "\n")
        self.put("PROME/WILL_QUEUE.md", "\n".join(l for l in self.text.splitlines() if not l.startswith("| 901")))
        self.commit(publish=True)
        self.assertEqual(read_receipts(self.repo, e), [receipt])
        display = self.store.display()
        self.assertEqual(display["group"], "History")
        self.assertFalse(display["can_respond"])
        self.assertNotIn("completion", display)
        with self.assertRaisesRegex(ValueError, "already terminal"):
            owner_receipt.prepare(self.repo, e, "received")

    def test_transport_refuses_wrong_branch_before_writing(self):
        e = self.store.save(self.request())
        self.git("switch", "-qc", "fixture-other")
        with self.assertRaisesRegex(ValueError, "master checkout"):
            delivery.deliver(self.repo, e)
        self.assertFalse((self.root / "PROME/inbox").exists())

    def test_acceptance_requires_published_review_and_exact_build(self):
        self.assertFalse(app.accepted(self.repo)[0])
        self.put("PROME/reports/fixture-review.md", "Fixture independent acceptance; not real approval")
        self.commit(publish=True)
        record = {"schema_version": "decisions-app-acceptance/1", "queue_responses": True,
                  "matching_chat_confirmation": True, "build_hashes": app.build_hashes(),
                  "independent_review": {"path": "PROME/reports/fixture-review.md", "commit": self.git("rev-parse", "HEAD").strip()}}
        self.put(app.ACCEPTANCE, json.dumps(record)); self.commit()
        self.assertFalse(app.accepted(self.repo)[0])
        self.git("push", "-q", "origin", "master")
        self.assertTrue(app.accepted(self.repo)[0])
        with patch("app.build_hashes", return_value={"changed": "build"}):
            self.assertFalse(app.accepted(self.repo)[0])
        self.put(app.ACCEPTANCE, json.dumps([])); self.commit(publish=True)
        self.assertFalse(app.accepted(self.repo)[0])


if __name__ == "__main__":
    unittest.main()
