#!/usr/bin/env python3
"""Isolated Git/SQLite checks. No real pilot events, rulings or owner writes."""
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import uuid

import pilot_files as pilot
from store import HERE, Store, demo_record, digest, encoded, reader


class PilotFileTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="cato-pilot-fixture-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        self.git("init", "-q", "-b", "master")
        self.git("config", "user.name", "Fictional fixture author")
        self.git("config", "user.email", "fixture@example.invalid")
        self.put("PROME/proposals/fixture-evidence.md", "Fictional test evidence; not a real ruling.\n")
        self.commit()
        evidence_commit = self.git("rev-parse", "HEAD").strip()
        self.record = demo_record()
        self.record.update(schema_version="wq-record/0.1-pilot", mode="supervised-pilot", wq_id="900")
        self.record["units"] = [self.record["units"][0]]
        self.record["units"][0]["id"] = "900.READER"
        self.record["units"][0]["proposal"]["submission_block_reason"] = None
        self.record["sources"][0].update(path="PROME/proposals/fixture-evidence.md", commit=evidence_commit)
        self.source_path = "PROME/proposals/fixture-pilot.md"
        self.write_source()
        self.put("PROME/WILL_QUEUE.md", "| 900 | Fictional fixture | RULE | No schedule; one selftest |\n")
        self.commit()
        self.repo = pilot.Repo(self.root)
        self.store = self.new_store("first.sqlite3", enabled=True)
        self.display = self.store.display()

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, text=True, stderr=subprocess.PIPE)

    def put(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)
        return target

    def commit(self):
        # Only the temporary fixture repository is ever staged here.
        self.git("add", "--all")
        self.git("commit", "-qm", "Isolated fixture state")

    def write_source(self):
        self.put(self.source_path, "# Fictional pilot fixture\n\n```wq-record\n" + json.dumps(self.record) + "\n```\n")

    def new_store(self, name, enabled=False, repo=None):
        return pilot.PilotStore(Path(self.temp.name) / name, repo or self.repo, self.source_path,
                                "900", "900.READER", enable_submissions=enabled)

    def request(self, **changes):
        request = {"id": uuid.uuid4().hex, "display_hash": self.display["hash"], "unit_id": "900.READER",
                   "action": "choose", "choice_id": "A", "note": "Only one test.\nNo schedule. Exact ‘words’ <text>.",
                   "revisit": "", "supersedes": None}
        request.update(changes)
        return request

    def event(self):
        return self.store.save(self.request())

    def receipt(self, event, state="received", previous=None):
        return {"schema_version": "decisions-receipt/1", "id": uuid.uuid4().hex,
                "response_id": event["id"], "response_sha256": event["sha256"], "state": state,
                "at": "2026-10-30T20:00:00+00:00", "previous_receipt_id": previous,
                "canonical_ruling": None, "chat_confirmation": None, "confirmed_response_sha256": None}

    def write_receipt(self, receipt):
        return self.put(f"{pilot.RECEIPTS}/{receipt['response_id']}/{receipt['id']}.json", encoded(receipt) + "\n")

    def test_default_is_read_only_and_creates_no_response_directory(self):
        store = self.new_store("disabled.sqlite3")
        display = store.display()
        with self.assertRaisesRegex(ValueError, "disabled"):
            store.save(self.request(display_hash=display["hash"]))
        self.assertFalse((self.root / pilot.RESPONSES).exists())
        self.assertEqual(display["groups"]["Decisions"][0]["unit"]["proposal"]["caveats"], self.record["units"][0]["proposal"]["caveats"])

    def test_real_producer_mapping_preserves_all_fields_and_references(self):
        record = json.loads(reader.source_text(reader.COPY_REV, reader.COPY_DIR + "/WQ-495.json"))
        record.update(schema_version="wq-record/0.1-pilot", mode="supervised-pilot")
        before = deepcopy(record)
        pilot.validate_record(pilot.Repo(reader.ROOT), record)
        self.assertEqual(record, before)
        self.assertEqual(len(record["units"]), 3)
        self.assertIn("NO schedule", encoded(record))

    def test_ambiguous_json_fences_wrong_mode_and_unsafe_paths_fail(self):
        with self.assertRaisesRegex(ValueError, "Duplicate JSON"):
            pilot.strict_json('{"a":1,"a":2}')
        text = (self.root / self.source_path).read_text()
        with self.assertRaisesRegex(ValueError, "exactly one"):
            pilot.record_block(text + text)
        self.record["mode"] = "design-copy"
        self.write_source()
        self.commit()
        with self.assertRaises(Exception):
            self.store.display()
        for path in ("../outside", "/absolute", "PROME/proposals/../file", "PROME\\other"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                self.repo.path(path)

    def test_dirty_source_and_direct_queue_edits_block_answers(self):
        original = (self.root / self.source_path).read_text()
        self.put(self.source_path, original + "\nUncommitted new condition.\n")
        with self.assertRaisesRegex(ValueError, "Uncommitted"):
            self.store.save(self.request())
        self.put(self.source_path, original)
        self.put("PROME/WILL_QUEUE.md", "| 900 | Changed directly by Will | RULE |\n")
        with self.assertRaisesRegex(ValueError, "Direct queue edit"):
            self.store.save(self.request())
        self.assertEqual(self.store.responses()["events"], [])

    def test_committed_crlf_source_preserves_original_bytes(self):
        path = self.root / self.source_path
        content = path.read_bytes().replace(b"\n", b"\r\n")
        path.write_bytes(content)
        self.commit()
        display = self.store.display()
        self.assertEqual(display["snapshot"]["source_text"].encode("utf-8"), content)
        event = self.store.save(self.request(display_hash=display["hash"]))
        pilot.validate_event(self.repo, event, "900", "900.READER")

    def test_unrelated_commit_does_not_stale_terms_but_changed_terms_do(self):
        self.put("unrelated.txt", "Unrelated fixture commit")
        self.commit()
        pilot.assert_current(self.repo, self.display["snapshot"])
        self.record["units"][0]["proposal"]["choices"][0]["consequence"] = "Changed without a revision increment"
        self.write_source()
        self.commit()
        with self.assertRaisesRegex(ValueError, "terms changed"):
            self.store.save(self.request())

    def test_committed_queue_change_and_settled_state_invalidate_old_display(self):
        self.put("PROME/WILL_QUEUE.md", "| 900 | Settled elsewhere | RULE |\n")
        self.commit()
        with self.assertRaisesRegex(ValueError, "queue row changed"):
            self.store.save(self.request())

    def test_save_export_retry_and_delivery_labels_are_distinct(self):
        request = self.request()
        event = self.store.save(request)
        self.assertFalse(event["synthetic"])
        self.assertEqual(self.store.save(request), event)
        self.assertEqual(event["request"]["note"], request["note"])
        self.assertIn("not committed", pilot.delivery_status(self.repo, event))
        self.commit()
        self.assertIn("remote delivery unverified", pilot.delivery_status(self.repo, event))
        self.git("update-ref", "refs/remotes/origin/master", "HEAD")
        self.assertIn("fresh delivery and acknowledgment not established", pilot.delivery_status(self.repo, event))
        self.assertEqual(pilot.read_receipts(self.repo, event), [])

    def test_export_failure_preserves_local_answer_and_retry_recovers(self):
        request = self.request()
        with patch("pilot_files.os.link", side_effect=OSError("injected export failure")):
            with self.assertRaisesRegex(ValueError, "Saved locally; export pending"):
                self.store.save(request)
        event = self.store.responses()["events"][0]
        self.assertEqual(event, self.store.save(request))
        self.assertEqual(len(self.store.responses()["events"]), 1)

    def test_tampered_and_symlink_exports_are_not_overwritten(self):
        event = self.event()
        path = self.root / pilot.RESPONSES / (event["id"] + ".json")
        path.write_text("altered")
        with self.assertRaisesRegex(ValueError, "different bytes"):
            pilot.export_event(self.repo, event, "900", "900.READER")
        self.assertEqual(path.read_text(), "altered")
        path.rename(path.with_suffix(".preserved"))
        path.symlink_to(Path(self.temp.name) / "outside.json")
        with self.assertRaisesRegex(ValueError, "Symlink"):
            pilot.export_event(self.repo, event, "900", "900.READER")

    def test_git_clone_restore_keeps_full_event_and_previous_reply(self):
        first = self.event()
        second = self.store.save(self.request(action="defer", choice_id=None, revisit="After evidence", supersedes=first["id"]))
        self.commit()
        clone = Path(self.temp.name) / "other-machine"
        subprocess.run(["git", "clone", "-q", "--no-hardlinks", str(self.root), str(clone)], check=True)
        other = self.new_store("other.sqlite3", repo=pilot.Repo(clone))
        state = other.display()["responses"]
        self.assertEqual(state["events"], [first, second])
        self.assertEqual(state["heads"], {"900.READER": second["id"]})
        self.assertEqual(pilot.import_responses(other.repo, other, "900", "900.READER"), 0)
        self.assertEqual(state["receipts"], {})

    def test_import_rejects_fork_without_partially_restoring(self):
        first = self.event()
        fork = deepcopy(first)
        fork["id"] = fork["request"]["id"] = uuid.uuid4().hex
        fork["sha256"] = digest({k: v for k, v in fork.items() if k != "sha256"})
        pilot.export_event(self.repo, fork, "900", "900.READER")
        self.commit()
        other = self.new_store("fork.sqlite3")
        with self.assertRaisesRegex(ValueError, "Conflicting branches"):
            pilot.import_responses(self.repo, other, "900", "900.READER")
        self.assertEqual(other.responses()["events"], [])

    def test_missing_predecessor_and_altered_option_are_rejected(self):
        event = self.event()
        changed = deepcopy(event)
        changed["selected_choice"]["consequence"] = "Permission widened"
        changed["sha256"] = digest({k: v for k, v in changed.items() if k != "sha256"})
        with self.assertRaisesRegex(ValueError, "shown meaning"):
            pilot.validate_event(self.repo, changed, "900", "900.READER")
        missing = deepcopy(event)
        missing["request"]["supersedes"] = uuid.uuid4().hex
        with self.assertRaisesRegex(ValueError, "Missing predecessor"):
            pilot.chain([missing], "id", lambda e: e["request"]["supersedes"])

    def test_rehearsal_events_and_databases_cannot_be_used_for_pilot(self):
        event = self.event()
        with self.assertRaisesRegex(ValueError, "another response mode"):
            Store(self.store.path)
        other = Store(Path(self.temp.name) / "demo.sqlite3")
        with self.assertRaisesRegex(ValueError, "rehearsal database"):
            pilot.import_responses(self.repo, other, "900", "900.READER")
        event["synthetic"] = True
        with self.assertRaisesRegex(ValueError, "Not a supervised"):
            pilot.validate_event(self.repo, event, "900", "900.READER")
        with self.assertRaisesRegex(ValueError, "Only PROME"):
            self.store.acknowledge(event["id"], event["sha256"], "received", "made up")

    def test_wrong_pilot_and_wrong_filename_cannot_import(self):
        event = self.event()
        with self.assertRaisesRegex(ValueError, "another pilot"):
            pilot.validate_event(self.repo, event, "901", "901.READER")
        old = self.root / pilot.RESPONSES / (event["id"] + ".json")
        old.rename(old.with_name(uuid.uuid4().hex + ".json"))
        self.commit()
        with self.assertRaisesRegex(ValueError, "filename/ID"):
            self.new_store("wrong-name.sqlite3").display()

    def test_two_simultaneous_answers_cannot_silently_override(self):
        def save(request):
            try:
                return self.store.save(request)
            except ValueError as error:
                return str(error)
        with ThreadPoolExecutor(2) as pool:
            results = list(pool.map(save, [self.request(), self.request(choice_id="B")]))
        self.assertEqual(sum(isinstance(r, dict) for r in results), 1)
        self.assertEqual(len(self.store.responses()["events"]), 1)

    def test_received_is_separate_and_integration_requires_chat_and_ruling(self):
        event = self.event()
        received = self.receipt(event)
        self.write_receipt(received)
        self.commit()
        self.assertEqual(pilot.read_receipts(self.repo, event), [received])
        integrated = self.receipt(event, "integrated", received["id"])
        self.write_receipt(integrated)
        self.commit()
        with self.assertRaisesRegex(ValueError, "chat-confirmation"):
            pilot.read_receipts(self.repo, event)
        self.put("PROME/proposals/fixture-RULED.md", "Fictional owner interpretation; no real authority.\n")
        self.put("PROME/proposals/fixture-confirmation.md", "Fictional matching chat confirmation.\n")
        self.commit()
        commit = self.git("rev-parse", "HEAD").strip()
        integrated.update(canonical_ruling={"path": "PROME/proposals/fixture-RULED.md", "commit": commit},
                          chat_confirmation={"path": "PROME/proposals/fixture-confirmation.md", "commit": commit},
                          confirmed_response_sha256=event["sha256"])
        self.write_receipt(integrated)
        self.commit()
        self.assertEqual(pilot.read_receipts(self.repo, event), [received, integrated])
        display = self.store.display()
        self.assertEqual(display["responses"]["receipts"][event["id"]]["state"], "integrated")
        self.assertNotIn("completed", encoded(display["responses"]["receipts"]))
        with self.assertRaisesRegex(ValueError, "already integrated"):
            self.store.save(self.request(supersedes=event["id"]))
        self.assertEqual(self.store.save(event["request"]), event)

    def test_receipt_mismatch_dirty_work_and_unknown_state_fail_visibly(self):
        event = self.event()
        receipt = self.receipt(event)
        receipt["response_sha256"] = "0" * 64
        path = self.write_receipt(receipt)
        self.commit()
        with self.assertRaisesRegex(ValueError, "another response/hash"):
            pilot.read_receipts(self.repo, event)
        receipt["response_sha256"] = event["sha256"]
        self.write_receipt(receipt)
        with self.assertRaisesRegex(ValueError, "Uncommitted"):
            pilot.read_receipts(self.repo, event)
        receipt["state"] = "completed"
        self.write_receipt(receipt)
        self.commit()
        with self.assertRaisesRegex(ValueError, "no completed-work"):
            pilot.read_receipts(self.repo, event)

    def test_forked_receipts_and_wrong_evidence_owner_are_rejected(self):
        event = self.event()
        one, two = self.receipt(event), self.receipt(event)
        self.write_receipt(one)
        self.write_receipt(two)
        self.commit()
        with self.assertRaisesRegex(ValueError, "Conflicting branches"):
            pilot.read_receipts(self.repo, event)
        with self.assertRaisesRegex(ValueError, "Wrong owner"):
            self.repo.read("AGENTS/CATO/claims.md", prefix="PROME/proposals")


if __name__ == "__main__":
    unittest.main()
