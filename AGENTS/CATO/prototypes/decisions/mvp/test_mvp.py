#!/usr/bin/env python3
"""Author checks for the synthetic store and loopback transport."""
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
import hashlib
import http.client
import json
from pathlib import Path
import re
import sqlite3
import tempfile
import threading
import unittest
import uuid

from server import make_server
from store import Store, demo_record, digest


class RehearsalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.record = demo_record()
        self.store = Store(Path(self.temp.name) / "responses.sqlite3", lambda: deepcopy(self.record))
        self.display = self.store.display()

    def request(self, **changes):
        request = {"id": uuid.uuid4().hex, "display_hash": self.display["hash"],
                   "unit_id": "DEMO-900.READER", "action": "choose", "choice_id": "A",
                   "note": "Only one selftest.\nNo schedule. <script>not code</script>",
                   "revisit": "", "supersedes": None}
        request.update(changes)
        return request

    def test_restart_keeps_exact_terms_conditions_and_selected_unit(self):
        request = self.request()
        event = self.store.save(request)
        restarted = Store(self.store.path)
        result = restarted.responses()
        self.assertEqual(result["events"], [event])
        self.assertEqual(event["request"], request)
        self.assertEqual(event["display"], self.display["snapshot"])
        self.assertEqual(event["selected_choice"], self.record["units"][0]["proposal"]["choices"][0])
        self.assertEqual(result["heads"], {"DEMO-900.READER": event["id"]})
        self.assertEqual(result["receipts"], {})
        self.assertTrue(event["synthetic"])

    def test_retry_is_identical_even_if_source_subsequently_changes(self):
        request = self.request()
        original = self.store.save(request)
        self.record["title"] = "Later source change"
        self.assertEqual(self.store.save(request), original)
        with self.assertRaisesRegex(ValueError, "different content"):
            self.store.save(dict(request, note="Different answer"))

    def test_changed_terms_without_revision_increment_reject_stale_display(self):
        self.record["units"][0]["proposal"]["choices"][0]["consequence"] = "Now runs every day"
        with self.assertRaisesRegex(ValueError, "terms changed"):
            self.store.save(self.request())
        self.assertEqual(self.store.responses()["events"], [])

    def test_changed_record_revision_rejects_old_display(self):
        self.record["record_revision"] += 1
        with self.assertRaisesRegex(ValueError, "terms changed"):
            self.store.save(self.request())

    def test_wrong_kind_choice_source_and_missing_snapshot(self):
        cases = [{"unit_id": "DEMO-900.FILE"}, {"choice_id": "X"},
                 {"unit_id": "DEMO-900.RECEIPT"}, {"unit_id": "495.NPORT"},
                 {"display_hash": "0" * 64}, {"action": "defer"}]
        for fields in cases:
            with self.subTest(fields=fields), self.assertRaises(ValueError):
                self.store.save(self.request(**fields))

    def test_live_record_cannot_be_adopted_by_filename_or_mode(self):
        self.record["wq_id"] = "495"
        with self.assertRaisesRegex(ValueError, "fictional"):
            self.store.display()

    def test_source_error_never_returns_empty_inbox(self):
        def failed():
            raise OSError("missing source")
        self.store.loader = failed
        with self.assertRaises(OSError):
            self.store.display()
        with self.assertRaises(OSError):
            self.store.save(self.request())

    def test_deferral_question_and_task_are_not_approvals(self):
        deferred = self.store.save(self.request(action="defer", choice_id=None, revisit="After the next filing"))
        self.assertIsNone(deferred["selected_choice"])
        self.assertEqual(deferred["request"]["revisit"], "After the next filing")
        question = self.store.save(self.request(action="request_changes", choice_id=None,
                                  note="What is excluded?", supersedes=deferred["id"]))
        self.assertIsNone(question["selected_choice"])
        task = self.store.save(self.request(unit_id="DEMO-900.FILE", action="report_done", choice_id=None))
        self.assertIsNone(task["selected_choice"])
        self.assertEqual(self.store.responses()["receipts"], {})

    def test_question_requires_words_and_unknown_fields_fail(self):
        with self.assertRaisesRegex(ValueError, "needs your words"):
            self.store.save(self.request(action="request_changes", choice_id=None, note="  "))
        with self.assertRaisesRegex(ValueError, "contract"):
            self.store.save(self.request(ignored_condition="Important condition"))

    def test_replacement_preserves_original_and_requires_current_head(self):
        first = self.store.save(self.request())
        with self.assertRaisesRegex(ValueError, "Another response exists"):
            self.store.save(self.request(choice_id="B"))
        second = self.store.save(self.request(choice_id="B", supersedes=first["id"]))
        with self.assertRaisesRegex(ValueError, "Another response exists"):
            self.store.save(self.request(supersedes=first["id"]))
        self.assertEqual(self.store.responses()["events"], [first, second])

    def test_two_overlapping_answers_have_one_head_and_no_silent_override(self):
        def save(request):
            try:
                return self.store.save(request)
            except ValueError as error:
                return str(error)
        with ThreadPoolExecutor(2) as pool:
            results = list(pool.map(save, [self.request(), self.request(choice_id="B")]))
        self.assertEqual(sum(isinstance(r, dict) for r in results), 1)
        self.assertEqual(len(self.store.responses()["events"]), 1)

    def test_write_failure_rolls_back_response_and_head(self):
        with self.store.connection() as db:
            db.execute("CREATE TRIGGER fail_head BEFORE INSERT ON heads BEGIN SELECT RAISE(ABORT, 'disk failure simulation'); END")
        with self.assertRaises(sqlite3.IntegrityError):
            self.store.save(self.request())
        self.assertEqual(self.store.responses()["events"], [])
        self.assertEqual(self.store.responses()["heads"], {})

    def test_receipt_is_separate_bound_to_event_and_not_completion(self):
        event = self.store.save(self.request())
        for event_id, event_hash in [(uuid.uuid4().hex, event["sha256"]), (event["id"], "bad")]:
            with self.assertRaisesRegex(ValueError, "does not match"):
                self.store.acknowledge(event_id, event_hash, "received", "synthetic receiver")
        receipt = self.store.acknowledge(event["id"], event["sha256"], "received", "synthetic receiver")
        self.assertEqual(receipt, self.store.acknowledge(event["id"], event["sha256"], "received", "synthetic receiver"))
        self.store.acknowledge(event["id"], event["sha256"], "integrated", "fictional interpretation only")
        state = self.store.responses()
        self.assertEqual(len(state["receipt_history"]), 2)
        self.assertEqual(state["receipts"][event["id"]]["state"], "integrated")
        with self.assertRaises(ValueError):
            self.store.acknowledge(event["id"], event["sha256"], "completed", "not allowed")
        with self.assertRaises(ValueError):
            self.store.acknowledge(event["id"], event["sha256"], "rejected", "conflict")

    def test_export_preserves_event_hash_and_does_not_claim_delivery(self):
        event = self.store.save(self.request())
        transfer = json.loads(json.dumps(self.store.export(event["id"])))
        self.assertEqual(transfer["event"], event)
        self.assertEqual(digest({k: v for k, v in event.items() if k != "sha256"}), event["sha256"])
        self.assertIn("Export only", transfer["delivery"])

    def test_http_loopback_capability_origin_host_and_size(self):
        server = make_server(self.store)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        port = server.server_port
        def call(method, path, body=None, extra=None):
            conn = http.client.HTTPConnection("127.0.0.1", port, timeout=5)
            headers = {"Content-Type": "application/json", **(extra or {})}
            conn.request(method, path, body, headers)
            response = conn.getresponse()
            status, content = response.status, response.read().decode()
            conn.close()
            return status, content
        status, page = call("GET", "/")
        self.assertEqual(status, 200)
        token = json.loads(re.search(r"const capability=(.+);", page)[1])
        request = self.request()
        headers = {"Origin": f"http://127.0.0.1:{port}", "X-Decisions-Session": token}
        self.assertEqual(call("POST", "/api/responses", json.dumps(request))[0], 403)
        self.assertEqual(call("POST", "/api/responses", json.dumps(request), dict(headers, Origin="https://foreign.example"))[0], 403)
        self.assertEqual(call("GET", "/api/display", extra={"Host": "foreign.example"})[0], 403)
        self.assertEqual(call("POST", "/api/responses", json.dumps(request), headers)[0], 200)
        self.assertEqual(call("POST", "/api/responses", json.dumps(request), headers)[0], 200)
        self.assertEqual(call("POST", "/api/responses", "x" * 600001, headers)[0], 413)
        self.assertEqual(len(self.store.responses()["events"]), 1)


if __name__ == "__main__":
    unittest.main()
