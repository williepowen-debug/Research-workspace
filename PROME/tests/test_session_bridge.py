"""Behavioral safety checks for the opt-in session bridge; temporary state only."""
import importlib.util
import json
import multiprocessing
import os
from pathlib import Path
import socket
import tempfile
import threading
import time
import unittest
from unittest import mock


SPEC = importlib.util.spec_from_file_location(
    "session_bridge", Path(__file__).resolve().parents[1] / "tools/session_bridge.py")
bridge = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bridge)


def contend_for_slot(path, ready, finished, results):
    """Keep winner alive until both independent transactions have returned."""
    try:
        journal = bridge.Journal(path)
        identity = bridge.process_identity(os.getpid())
        ready.wait(timeout=10)
        try:
            rid = journal.reserve(1, identity)
            results.put(("reserved", rid))
        except bridge.BridgeError as exc:
            results.put(("refused", str(exc)))
        finished.wait(timeout=10)
    except BaseException as exc:
        results.put(("worker_error", repr(exc)))


class RpcTests(unittest.TestCase):
    def setUp(self):
        self.client, self.server = socket.socketpair()
        self.server.settimeout(2)
        self.rpc = bridge.Rpc(self.client, self.client, "fixture")
        self.addCleanup(self.server.close)
        self.addCleanup(self.rpc.close)

    def send(self, *values):
        self.server.sendall(b"".join(json.dumps(v).encode() + b"\n" for v in values))

    def test_split_frame_and_coalesced_next_frame(self):
        self.server.sendall(b'{"method":"partial","params":{"n":')
        def finish():
            time.sleep(0.02)
            self.server.sendall(b'1}}\n{"id":7,"result":"next"}\n')
        writer = threading.Thread(target=finish)
        writer.start()
        try:
            self.assertEqual(self.rpc.receive(1)["params"], {"n": 1})
            self.assertEqual(self.rpc.receive(1), {"id": 7, "result": "next"})
        finally:
            writer.join(2)

    def test_notifications_and_approval_do_not_displace_response(self):
        self.send(
            {"method": "turn/completed", "params": {"threadId": "t", "turn": {"status": "failed"}}},
            {"id": "approval-1", "method": "item/commandExecution/requestApproval", "params": {}},
            {"id": 1, "result": {"ok": True}},
        )
        self.assertEqual(self.rpc.call("thread/read", timeout=1), {"ok": True})
        transcript = b""
        while transcript.count(b"\n") < 2:
            transcript += self.server.recv(4096)
        sent = [json.loads(line) for line in transcript.splitlines()]
        rejection = next(row for row in sent if row["id"] == "approval-1")
        self.assertIn("error", rejection)
        self.assertNotIn("result", rejection)
        self.assertEqual(self.rpc.wait_event("turn/completed", timeout=0.1)["turn"]["status"], "failed")
        event = self.rpc.wait_event("pilot/requestRejected", timeout=0.1)
        self.assertEqual(event["method"], "item/commandExecution/requestApproval")

    def test_event_predicate_preserves_other_thread_notice(self):
        self.send({"method": "done", "params": {"thread": "other"}},
                  {"method": "done", "params": {"thread": "wanted"}})
        result = self.rpc.wait_event("done", lambda p: p["thread"] == "wanted", timeout=1)
        self.assertEqual(result["thread"], "wanted")
        self.assertEqual(self.rpc.wait_event("done", timeout=0.1)["thread"], "other")

    def test_disconnect_after_request_does_not_become_success(self):
        self.server.shutdown(socket.SHUT_WR)
        with self.assertRaisesRegex(bridge.BridgeError, "UNKNOWN"):
            self.rpc.call("write", timeout=0.1)

    def test_timeout_reports_unknown(self):
        with self.assertRaisesRegex(TimeoutError, "UNKNOWN"):
            self.rpc.call("write", timeout=0.02)

    def test_malformed_json_and_non_object_are_rejected(self):
        self.server.sendall(b'{broken}\n[]\n')
        with self.assertRaisesRegex(bridge.BridgeError, "Malformed"):
            self.rpc.receive(0.1)
        with self.assertRaisesRegex(bridge.BridgeError, "not an object"):
            self.rpc.receive(0.1)

    def test_error_and_missing_result_are_not_success(self):
        self.send({"id": 1, "error": {"code": -1, "message": "refused"}}, {"id": 2})
        with self.assertRaisesRegex(bridge.BridgeError, "refused"):
            self.rpc.call("test", timeout=0.1)
        with self.assertRaisesRegex(bridge.BridgeError, "lacks result/error"):
            self.rpc.call("test", timeout=0.1)


class FakeRpc:
    endpoint = "fixture://existing-server"

    def __init__(self, cwd):
        self.target = {"id": "thread-1", "cwd": str(cwd), "canAcceptDirectInput": True,
                       "status": {"type": "idle"}}
        self.calls = []
        self.failure = None
        self.override_response = False
        self.response = None

    def call(self, method, params):
        self.calls.append((method, params))
        if method == "thread/read":
            return {"thread": self.target}
        if self.failure:
            raise self.failure
        if self.override_response:
            return self.response
        if method == "turn/steer":
            return {"turnId": params["expectedTurnId"]}
        return {"queuedSubmission": {"id": "queue-1", "clientUserMessageId": params["clientUserMessageId"]}}

    @property
    def mutations(self):
        return [(method, params) for method, params in self.calls if method != "thread/read"]


class DoorbellTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.artifact = self.root / "task.md"
        self.artifact.write_text("Bounded fixture task.\n")
        self.db = self.root / "journal.sqlite"
        self.journal = bridge.Journal(self.db)
        self.rpc = FakeRpc(self.root)
        self.envelope = {"message_id": "message-1", "task_id": "task-1", "sender": "PROME",
                         "thread_id": "thread-1", "cwd": str(self.root),
                         "artifact": str(self.artifact), "mode": "queue"}

    def test_acceptance_survives_restart_and_duplicate_never_resends(self):
        first = bridge.doorbell(self.rpc, self.journal, self.envelope)
        second = bridge.doorbell(self.rpc, bridge.Journal(self.db), self.envelope)
        self.assertEqual(first["status"], "ACCEPTED")
        self.assertFalse(first["duplicate"])
        self.assertTrue(second["duplicate"])
        self.assertEqual(second["status"], "ACCEPTED")
        self.assertEqual(len(self.rpc.mutations), 1)
        method, params = self.rpc.mutations[0]
        self.assertEqual(method, "thread/queue/add")
        self.assertEqual(params["clientUserMessageId"], "message-1")
        self.assertNotIn("approvalPolicy", params)

    def test_changed_payload_with_same_id_is_refused(self):
        bridge.doorbell(self.rpc, self.journal, self.envelope)
        with self.assertRaisesRegex(bridge.BridgeError, "different payload"):
            bridge.doorbell(self.rpc, bridge.Journal(self.db), dict(self.envelope, task_id="different"))
        self.assertEqual(len(self.rpc.mutations), 1)

    def test_changed_artifact_with_same_id_is_refused(self):
        bridge.doorbell(self.rpc, self.journal, self.envelope)
        self.artifact.write_text("A different task masquerading as the old message.\n")
        with self.assertRaisesRegex(bridge.BridgeError, "different payload"):
            bridge.doorbell(self.rpc, bridge.Journal(self.db), self.envelope)
        self.assertEqual(len(self.rpc.mutations), 1)

    def test_cwd_mismatch_sends_no_input_and_can_be_corrected(self):
        self.rpc.target["cwd"] = str(self.root / "different-desk")
        with self.assertRaisesRegex(bridge.BridgeError, "cwd mismatch"):
            bridge.doorbell(self.rpc, self.journal, self.envelope)
        self.assertEqual(self.rpc.mutations, [])
        self.rpc.target["cwd"] = str(self.root)
        self.assertEqual(bridge.doorbell(self.rpc, self.journal, self.envelope)["status"], "ACCEPTED")

    def test_unknown_outcome_never_automatically_retries_after_restart(self):
        self.rpc.failure = TimeoutError("Reply lost after recipient may have acted")
        with self.assertRaises(TimeoutError):
            bridge.doorbell(self.rpc, self.journal, self.envelope)
        self.rpc.failure = None
        result = bridge.doorbell(self.rpc, bridge.Journal(self.db), self.envelope)
        self.assertEqual(result["status"], "UNKNOWN")
        self.assertTrue(result["duplicate"])
        self.assertEqual(len(self.rpc.mutations), 1)

    def test_uncertain_capability_and_unloaded_recipient_send_no_input(self):
        for capability, state in [(None, "idle"), (False, "active"), (True, "notLoaded"), (True, "systemError")]:
            with self.subTest(capability=capability, state=state):
                self.rpc.target.update(canAcceptDirectInput=capability, status={"type": state})
                with self.assertRaises(bridge.BridgeError):
                    bridge.doorbell(self.rpc, self.journal, self.envelope)
        self.assertEqual(self.rpc.mutations, [])

    def test_steering_requires_and_transmits_turn_precondition(self):
        envelope = dict(self.envelope, mode="steer")
        with self.assertRaisesRegex(bridge.BridgeError, "expected turn ID"):
            bridge.doorbell(self.rpc, self.journal, envelope)
        self.assertEqual(self.rpc.calls, [])
        self.rpc.target["status"] = {"type": "active"}
        result = bridge.doorbell(self.rpc, self.journal, dict(envelope, expected_turn_id="turn-9"))
        self.assertEqual(result["status"], "ACCEPTED")
        self.assertEqual(self.rpc.mutations[0][0], "turn/steer")
        self.assertEqual(self.rpc.mutations[0][1]["expectedTurnId"], "turn-9")

    def test_wrong_or_missing_thread_identity_refuses_input(self):
        for identity in ("another-thread", None):
            with self.subTest(identity=identity):
                self.rpc.target["id"] = identity
                with self.assertRaisesRegex(bridge.BridgeError, "session identity"):
                    bridge.doorbell(self.rpc, self.journal, self.envelope)
                self.assertEqual(self.rpc.mutations, [])
        self.rpc.target["id"] = self.envelope["thread_id"]
        self.assertEqual(bridge.doorbell(self.rpc, self.journal, self.envelope)["status"], "ACCEPTED")

    def test_ephemeral_queue_refused_before_mutation(self):
        self.rpc.target["ephemeral"] = True
        with self.assertRaisesRegex(bridge.BridgeError, "Ephemeral"):
            bridge.doorbell(self.rpc, self.journal, self.envelope)
        self.assertEqual(self.rpc.mutations, [])
        self.rpc.target["ephemeral"] = False
        self.assertEqual(bridge.doorbell(self.rpc, self.journal, self.envelope)["status"], "ACCEPTED")

    def test_malformed_mutation_acknowledgements_persist_unknown_without_retry(self):
        cases = [("queue", None), ("queue", []), ("queue", {}),
                 ("queue", {"queuedSubmission": None}),
                 ("queue", {"queuedSubmission": {"id": "queue-1", "clientUserMessageId": "wrong-message"}}),
                 ("queue", {"queuedSubmission": {"id": "", "clientUserMessageId": "message-5"}}),
                 ("queue", {"queuedSubmission": {"id": 123, "clientUserMessageId": "message-6"}}),
                 ("steer", None), ("steer", {}), ("steer", {"turnId": "wrong-turn"})]
        for index, (mode, acknowledgement) in enumerate(cases):
            with self.subTest(mode=mode, acknowledgement=acknowledgement):
                envelope = dict(self.envelope, message_id=f"message-{index}", mode=mode,
                                expected_turn_id="turn-9")
                self.rpc.override_response = True
                self.rpc.response = acknowledgement
                sent_before = len(self.rpc.mutations)
                with self.assertRaisesRegex(bridge.BridgeError, "UNKNOWN"):
                    bridge.doorbell(self.rpc, self.journal, envelope)
                self.rpc.override_response = False
                result = bridge.doorbell(self.rpc, bridge.Journal(self.db), envelope)
                self.assertEqual(result["status"], "UNKNOWN")
                self.assertTrue(result["duplicate"])
                self.assertEqual(len(self.rpc.mutations), sent_before + 1)


class CapacityTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.db = self.root / "capacity.sqlite"
        self.journal = bridge.Journal(self.db)
        self.identity = {"pid": 101, "start_ticks": "10", "state": "S", "boot_id": "boot", "pid_namespace": "ns"}
        self.other = dict(self.identity, pid=102)

    def test_two_processes_cannot_both_take_last_slot(self):
        context = multiprocessing.get_context("fork")
        ready, finished, results = context.Barrier(3), context.Event(), context.Queue()
        workers = [context.Process(target=contend_for_slot, args=(str(self.db), ready, finished, results)) for _ in range(2)]
        try:
            for worker in workers:
                worker.start()
            ready.wait(timeout=10)
            outcomes = [results.get(timeout=10) for _ in workers]
            self.assertEqual(sorted(row[0] for row in outcomes), ["refused", "reserved"], outcomes)
            self.assertIn("capacity exhausted", next(row[1] for row in outcomes if row[0] == "refused"))
        finally:
            finished.set()
            for worker in workers:
                worker.join(5)
                if worker.is_alive():
                    worker.terminate()
                    worker.join(5)
            results.close()
            results.join_thread()
        self.assertTrue(all(worker.exitcode == 0 for worker in workers))

    def test_dead_holder_reclaims_slot_but_unknown_holder_counts(self):
        rid = self.journal.reserve(1, self.identity, check=lambda _: "LIVE")
        def unknown_old(identity):
            return "UNKNOWN" if identity["pid"] == 101 else "LIVE"
        with self.assertRaisesRegex(bridge.BridgeError, "capacity exhausted"):
            self.journal.reserve(1, self.other, check=unknown_old)
        def dead_old(identity):
            return "DEAD" if identity["pid"] == 101 else "LIVE"
        new_rid = self.journal.reserve(1, self.other, check=dead_old)
        self.assertNotEqual(rid, new_rid)
        self.assertFalse(self.journal.release(rid, self.identity))
        self.assertTrue(self.journal.release(new_rid, self.other))

    def test_unknown_candidate_cannot_claim_slot(self):
        with self.assertRaisesRegex(bridge.BridgeError, "verified live holder"):
            self.journal.reserve(1, self.identity, check=lambda _: "UNKNOWN")

    def test_shared_capacity_policy_rejects_different_client_limits(self):
        rid = self.journal.reserve(2, self.identity, check=lambda _: "LIVE")
        restarted = bridge.Journal(self.db)
        for changed_limit in (1, 3):
            with self.subTest(limit=changed_limit):
                with self.assertRaisesRegex(bridge.BridgeError, "shared policy"):
                    restarted.reserve(changed_limit, self.other, check=lambda _: "LIVE")
        second = restarted.reserve(2, self.other, check=lambda _: "LIVE")
        with self.assertRaisesRegex(bridge.BridgeError, "capacity exhausted"):
            self.journal.reserve(2, dict(self.other, pid=103), check=lambda _: "LIVE")
        self.assertTrue(self.journal.release(rid, self.identity))
        self.assertTrue(restarted.release(second, self.other))
        # Emptying the registry does not allow another client to redefine policy.
        with self.assertRaisesRegex(bridge.BridgeError, "shared policy"):
            bridge.Journal(self.db).reserve(3, self.identity, check=lambda _: "LIVE")

    def test_wrong_generation_cannot_release_current_holder(self):
        rid = self.journal.reserve(1, self.identity, check=lambda _: "LIVE")
        with self.assertRaisesRegex(bridge.BridgeError, "generation mismatch"):
            self.journal.release(rid, dict(self.identity, start_ticks="older"))
        with self.assertRaisesRegex(bridge.BridgeError, "capacity exhausted"):
            self.journal.reserve(1, self.other, check=lambda _: "LIVE")
        self.assertTrue(self.journal.release(rid, self.identity))
        self.assertFalse(self.journal.release(rid, self.identity))

    def test_duplicate_owner_and_inactive_parent_refused(self):
        rid = self.journal.reserve(3, self.identity, owner="BRENT", check=lambda _: "LIVE")
        with self.assertRaisesRegex(bridge.BridgeError, "Owner writer"):
            self.journal.reserve(3, self.other, owner="BRENT", check=lambda _: "LIVE")
        child = self.journal.reserve(3, self.other, parent=rid, check=lambda _: "LIVE")
        self.assertTrue(self.journal.release(child, self.other))
        self.assertTrue(self.journal.release(rid, self.identity))
        with self.assertRaisesRegex(bridge.BridgeError, "Parent reservation"):
            self.journal.reserve(3, self.other, parent=rid, check=lambda _: "LIVE")

    def test_pid_reuse_zombie_and_host_namespace_mismatch(self):
        cases = [(None, "DEAD"), (dict(self.identity, start_ticks="20"), "DEAD"),
                 (dict(self.identity, state="Z"), "DEAD"),
                 (dict(self.identity, boot_id="other-host"), "UNKNOWN"),
                 (dict(self.identity, pid_namespace="different"), "UNKNOWN"),
                 (dict(self.identity, state="R"), "LIVE")]
        for current, expected in cases:
            with self.subTest(current=current), \
                 mock.patch.object(bridge, "local_context", return_value={"boot_id": "boot", "pid_namespace": "ns"}), \
                 mock.patch.object(bridge, "process_identity", return_value=current):
                self.assertEqual(bridge.liveness(self.identity), expected)
        with mock.patch.object(bridge, "local_context", return_value={"boot_id": "boot", "pid_namespace": "ns"}), \
             mock.patch.object(bridge, "process_identity", side_effect=bridge.BridgeError("cannot inspect")):
            self.assertEqual(bridge.liveness(self.identity), "UNKNOWN")

    def test_absent_pid_in_foreign_boot_or_namespace_is_unknown(self):
        contexts = [{"boot_id": "other-boot", "pid_namespace": "ns"},
                    {"boot_id": "boot", "pid_namespace": "other-namespace"}]
        for observer_context in contexts:
            with self.subTest(context=observer_context), \
                 mock.patch.object(bridge, "local_context", return_value=observer_context), \
                 mock.patch.object(bridge, "process_identity", return_value=None):
                self.assertEqual(bridge.liveness(self.identity), "UNKNOWN")
        with mock.patch.object(bridge, "local_context", side_effect=bridge.BridgeError("unavailable")), \
             mock.patch.object(bridge, "process_identity", return_value=None):
            self.assertEqual(bridge.liveness(self.identity), "UNKNOWN")

    def test_existing_process_with_missing_host_metadata_is_unknown_not_dead(self):
        proc = self.root / "proc"
        pid_dir = proc / "101"
        pid_dir.mkdir(parents=True)
        # /proc stat fields 3..22: state then 18 filler fields, then start time.
        tail = ["S"] + ["0"] * 18 + ["12345"]
        (pid_dir / "stat").write_text("101 (name with spaces) " + " ".join(tail))
        with self.assertRaisesRegex(bridge.BridgeError, "UNKNOWN"):
            bridge.process_identity(101, proc_root=proc)


if __name__ == "__main__":
    unittest.main()
