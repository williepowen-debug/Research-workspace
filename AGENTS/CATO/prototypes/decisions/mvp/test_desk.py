"""Real Git/SQLite fixtures for the daily desk. Never submits a live response."""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import uuid
import hashlib

import app
import delivery
from pilot_files import Repo, encoded, read_receipts
from queue_store import QueueStore, REPLIES, open_rows, validate_reply
from store import reader
import history


class DeskTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="cato-desk-test-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "repo"; self.root.mkdir()
        self.git("init", "-q", "-b", "master")
        self.git("config", "user.name", "Fixture author")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "core.hooksPath", "scripts/githooks")
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

    def install_options(self):
        path = "PROME/proposals/fixture-options.md"
        self.text = self.text.replace("Exact caveat |", "Exact caveat <!-- decisions-options: " + path + " --> |")
        row = open_rows(self.text)["901"]["row"]
        self.options = {"schema_version": "decisions-options/1", "wq_id": "901",
                        "queue_row_sha256": hashlib.sha256(row.encode()).hexdigest(),
                        "choices": [{"id": "A", "label": "Do the task", "meaning": "Only this task, with the caveat.",
                                     "consequence": "One task; no new schedule."},
                                    {"id": "B", "label": "Decline", "meaning": "Do not do this task.",
                                     "consequence": "No change."}]}
        self.put("PROME/WILL_QUEUE.md", self.text)
        self.put(path, "```decisions-options\n" + json.dumps(self.options) + "\n```\n")
        self.commit(publish=True)
        self.display = self.store.display()
        return path

    def test_explicit_options_preserve_meaning_and_conditions_across_delivery_restore(self):
        self.install_options()
        e = self.store.save(self.request(action="choose", choice_id="A", note="Only after my review."))
        self.assertEqual(e["selected_choice"], self.options["choices"][0])
        self.assertEqual(e["request"]["note"], "Only after my review.")
        delivery.deliver(self.repo, e)
        restored = QueueStore(Path(self.tmp.name) / "restore-options.sqlite3", self.repo, "901")
        self.assertEqual(restored.display()["last"], e)
        forged = json.loads(json.dumps(e)); forged["selected_choice"]["meaning"] = "Extra authority"
        from store import digest
        forged["sha256"] = digest({k: v for k, v in forged.items() if k != "sha256"})
        with self.assertRaisesRegex(ValueError, "shown meaning"):
            validate_reply(self.repo, forged, "901")

    def test_options_changed_source_blocks_stale_answer(self):
        path = self.install_options()
        self.options["choices"][0]["meaning"] = "Changed terms"
        self.put(path, "```decisions-options\n" + json.dumps(self.options) + "\n```\n")
        with self.assertRaisesRegex(ValueError, "Uncommitted"):
            self.store.save(self.request(action="choose", choice_id="A"))
        self.commit(publish=True)
        with self.assertRaisesRegex(ValueError, "Terms changed"):
            self.store.save(self.request(action="choose", choice_id="A"))

    def test_bad_options_never_fall_back_to_unbound_buttons(self):
        path = self.install_options()
        good = json.loads(json.dumps(self.options))
        for change in [{"wq_id": "902"}, {"queue_row_sha256": "0" * 64},
                       {"choices": [good["choices"][0], good["choices"][0]]}]:
            bad = {**good, **change}
            self.put(path, "```decisions-options\n" + json.dumps(bad) + "\n```\n")
            self.commit(publish=True)
            with self.assertRaises(ValueError):
                self.store.display()
        self.put(path, "```decisions-options\n" + json.dumps(good) + "\n```\n")
        self.put("PROME/WILL_QUEUE.md", self.text.replace("| DECISION |", "| mixed |"))
        self.commit(publish=True)
        with self.assertRaisesRegex(ValueError, "one DECISION row"):
            self.store.display()

    def test_no_prose_inference_and_unselected_choice_not_saved(self):
        with self.assertRaises(ValueError):
            self.store.save(self.request(action="choose", choice_id="A"))
        self.install_options()
        with self.assertRaises(ValueError):
            self.store.save(self.request(action="choose", choice_id=None))
        with self.assertRaises(ValueError):
            self.store.save(self.request(action="defer", choice_id="A"))
        self.assertFalse(self.store.responses()["events"])

    def test_missing_or_ambiguous_option_sources_refuse_new_answers(self):
        path = self.install_options()
        good = self.repo.path(path).read_text()
        for bad in ["No block", good + good, "> ```decisions-options\n" + json.dumps(self.options) + "\n> ```"]:
            self.put(path, bad); self.commit(publish=True)
            with self.assertRaises(ValueError): self.store.display()
        self.git("rm", "--", path); self.commit(publish=True)
        with self.assertRaisesRegex(ValueError, "missing"):
            self.store.display()

    def test_history_preserves_full_owner_text_and_uses_published_revision(self):
        text = '# WQ-901 — RULED\n\nWill said "A only if reviewed" at 21:13 ET.\n\nRecorded at 21:14 ET.\n\nCorrection: earlier time was write time.\n'
        path = "PROME/proposals/2026-10-30_wq901-RULED.md"
        self.put(path, text); self.commit(publish=True)
        self.put(path, text + "Unpublished owner work\n")
        h = history.recent(self.repo)
        self.assertFalse(h["errors"])
        self.assertEqual(h["records"][0]["text"], text)
        self.assertFalse(h["records"][0]["current"])
        self.assertIn("not a complete ledger", h["scope"])

    def test_failed_push_leaves_exact_commit_and_retry_does_not_duplicate(self):
        e = self.store.save(self.request())
        run = subprocess.run
        def fail_push(args, **kwargs):
            if args == ["bash", "scripts/safe-push.sh"]:
                return subprocess.CompletedProcess(args, 2, "Cannot confirm", "")
            return run(args, **kwargs)
        with patch("delivery.subprocess.run", side_effect=fail_push):
            with self.assertRaisesRegex(ValueError, "publication not confirmed"):
                delivery.deliver(self.repo, e)
        before = self.git("rev-parse", "HEAD")
        self.assertEqual(delivery.delivery_state(self.repo, e), "committed")
        delivery.deliver(self.repo, e)
        self.assertEqual(before, self.git("rev-parse", "HEAD"))
        self.assertEqual(delivery.delivery_state(self.repo, e), "delivered")

    def test_changed_export_during_checks_stops_before_commit(self):
        e = self.store.save(self.request()); before = self.git("rev-parse", "HEAD")
        run = subprocess.run
        def change_export(args, **kwargs):
            result = run(args, **kwargs)
            if args == ["bash", "scripts/orphan_check.sh", "CATO"]:
                self.put(delivery.event_path(e), "Changed by another writer")
            return result
        with patch("delivery.subprocess.run", side_effect=change_export):
            with self.assertRaisesRegex(ValueError, "changed during Send"):
                delivery.deliver(self.repo, e)
        self.assertEqual(before, self.git("rev-parse", "HEAD"))

    def test_concurrent_transport_refuses_without_packet_mutation(self):
        e = self.store.save(self.request())
        with delivery.locked(self.repo):
            with self.assertRaisesRegex(ValueError, "Another Decisions window"):
                delivery.deliver(self.repo, e)
        self.assertFalse((self.root / "PROME/inbox").exists())

    def test_delivery_non_fast_forward_never_rebases_or_forces(self):
        other = Path(self.tmp.name) / "other-push"
        subprocess.run(["git", "clone", "-q", "-b", "master", str(self.remote), str(other)], check=True)
        for key, value in [("user.name", "Fixture"), ("user.email", "fixture@example.invalid")]:
            subprocess.run(["git", "config", key, value], cwd=other, check=True)
        (other / "owner.txt").write_text("Owner's remote work")
        for args in [["add", "owner.txt"], ["commit", "-qm", "Remote owner"], ["push", "-q"]]:
            subprocess.run(["git", *args], cwd=other, check=True)
        remote_head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=other, text=True)
        e = self.store.save(self.request())
        with self.assertRaisesRegex(ValueError, "publication not confirmed"):
            delivery.deliver(self.repo, e)
        self.assertEqual(self.git("rev-parse", "origin/master"), remote_head)
        self.assertFalse((self.root / "owner.txt").exists())
        self.assertEqual(delivery.delivery_state(self.repo, e), "committed")

    def test_desk_refuses_delivery_of_superseded_reply(self):
        desk = app.Desk(self.repo, Path(self.tmp.name) / "superseded", True)
        with patch("app.accepted", return_value=(True, "")):
            card = next(c for c in desk.display()["cards"] if c["wq_id"] == "901")
            first = desk.save(self.request(display_hash=card["hash"]))
            desk.save(self.request(display_hash=card["hash"], supersedes=first["id"], note="B instead"))
            with self.assertRaisesRegex(ValueError, "latest saved"):
                desk.operate("/api/deliver", {"id": first["id"]})

    def test_changed_loaded_build_and_revoked_acceptance_stop_send(self):
        desk = app.Desk(self.repo, Path(self.tmp.name) / "revoked", True)
        with patch("app.accepted", return_value=(True, "")):
            self.assertTrue(desk.permissions()[0])
            with patch("app.build_hashes", return_value={"changed": "file"}):
                self.assertFalse(desk.permissions()[0])
        e = self.store.save(self.request())
        with self.assertRaisesRegex(ValueError, "acceptance revoked"):
            delivery.deliver(self.repo, e, guard=lambda: (_ for _ in ()).throw(ValueError("acceptance revoked")))
        self.assertFalse((self.root / "PROME/inbox").exists())

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

    def test_viewed_then_closed_unanswered_row_does_not_block_the_desk(self):
        desk = app.Desk(self.repo, Path(self.tmp.name) / "visited", True)
        with patch("app.accepted", return_value=(True, "")):
            self.assertEqual(len(desk.display()["cards"]), 2)
            self.put("PROME/WILL_QUEUE.md", "\n".join(l for l in self.text.splitlines() if not l.startswith("| 901")))
            self.commit(publish=True)
            state = desk.display()
            self.assertEqual(state["errors"], [])
            self.assertEqual([c["wq_id"] for c in state["cards"]], ["902"])
            self.assertTrue(state["cards"][0]["can_respond"])

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
