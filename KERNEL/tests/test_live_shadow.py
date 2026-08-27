from __future__ import annotations

import copy
import hashlib
import json
import shutil
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from core import canonical_bytes  # noqa: E402
from live_grant import LiveShadowGrant, require_live_grant  # noqa: E402
from live_shadow import (  # noqa: E402
    LiveRefusal,
    authorize_live_activation,
    load_activation_document,
    main,
    prepare_live_inputs,
)
from locking import FixtureAcceptanceLock  # noqa: E402
from test_native import SyntheticGitRepository, ref, tsv_line  # noqa: E402
from test_permissions import command, submission_path  # noqa: E402
from writer import FixtureResultStore  # noqa: E402


WIDE_START = "2000-01-01T00:00:00.000000Z"
WIDE_END = "2100-01-01T00:00:00.000000Z"
INJECTED_NOW = "2026-08-26T12:00:00.000000Z"
QUESTION_EVENT = "EVT-018f22e2-7d00-7000-8000-0000000e0001"
FORECAST_EVENT = "EVT-018f22e2-7d00-7000-8000-0000000e0002"
FIXTURE_PERMISSIONS = ROOT / "tests" / "fixtures" / "permissions"


def git(repo_path: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo_path), *args], check=True, capture_output=True, text=True
    ).stdout.strip()


class LivePlayingRepository:
    """A synthetic repository playing the live root for live-mode fixtures."""

    def __init__(self, testcase: unittest.TestCase):
        self.repo = SyntheticGitRepository(testcase)
        self.path = self.repo.path
        policies = self.path / "policies"
        policies.mkdir()
        shutil.copyfile(FIXTURE_PERMISSIONS / "actors.json", policies / "actors.json")
        shutil.copyfile(FIXTURE_PERMISSIONS / "capability-grants.json", policies / "capability-grants.json")
        shutil.copyfile(ROOT / "policies" / "custody-policy.json", policies / "custody-policy.json")

        self.question = command("RegisterQuestion")
        companion = json.loads(self.repo.blob("native/companion.json"))
        selected = canonical_bytes(companion["questions"]["FIX-Q-001"])
        self.question["native_refs"] = [ref(
            self.repo.commit, "native/companion.json", "JSON_POINTER", "/questions/FIX-Q-001", selected
        )]
        self.forecast = command("SubmitForecast")
        forecast_row = tsv_line(self.repo.blob("native/predictions.tsv"), b"FIX-F-001")
        self.forecast["native_refs"] = [ref(
            self.repo.commit, "native/predictions.tsv", "TSV_RECORD_ID", "record_id=FIX-F-001", forecast_row
        )]

        self.paths: dict[str, str] = {}
        for candidate in (self.question, self.forecast):
            relative = submission_path(candidate)
            destination = self.path / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(canonical_bytes(candidate) + b"\n")
            self.paths[candidate["command_id"]] = relative
        git(self.path, "add", "AGENTS")
        git(self.path, "commit", "-q", "-m", "live-playing submissions")
        self.submission_commit = git(self.path, "rev-parse", "HEAD")

    def file_sha(self, relative: str) -> str:
        return hashlib.sha256((self.path / relative).read_bytes()).hexdigest()

    def activation(self, *, window=(WIDE_START, WIDE_END), **overrides) -> dict:
        document = {
            "schema_version": "kernel.live-activation.1",
            "policy_version": "kernel.policy.1",
            "activation_id": "LIVE-TEST-0001",
            "authorized_by": "WILL",
            "authorization_ref": "KERNEL/GATE_C_C7_ACTIVATION_PACKET.md",
            "mode": "LIVE_SHADOW_PILOT",
            "repository_root": str(self.path),
            "repository": "williepowen-debug/Research-workspace",
            "source_commit": self.repo.commit,
            "window_start": window[0],
            "window_end": window[1],
            "revoked_at": None,
            "writer_id": "PROME",
            "commands": [
                {
                    "command_id": self.question["command_id"],
                    "path": self.paths[self.question["command_id"]],
                    "sha256": self.file_sha(self.paths[self.question["command_id"]]),
                },
                {
                    "command_id": self.forecast["command_id"],
                    "path": self.paths[self.forecast["command_id"]],
                    "sha256": self.file_sha(self.paths[self.forecast["command_id"]]),
                },
            ],
            "actors_path": "policies/actors.json",
            "actors_sha256": self.file_sha("policies/actors.json"),
            "capabilities_path": "policies/capability-grants.json",
            "capabilities_sha256": self.file_sha("policies/capability-grants.json"),
            "custody_policy_path": "policies/custody-policy.json",
            "custody_policy_sha256": self.file_sha("policies/custody-policy.json"),
            "event_ids": {
                self.question["command_id"]: QUESTION_EVENT,
                self.forecast["command_id"]: FORECAST_EVENT,
            },
        }
        document.update(overrides)
        return document

    def write_activation(self, document: dict, testcase: unittest.TestCase) -> Path:
        import tempfile

        temporary = tempfile.TemporaryDirectory()
        testcase.addCleanup(temporary.cleanup)
        path = Path(temporary.name) / "activation.json"
        path.write_text(json.dumps(document), encoding="utf-8")
        return path

    def event_files(self) -> list[Path]:
        return sorted((self.path / "KERNEL").glob("shadow/events/**/*.json"))

    def receipt_files(self) -> list[Path]:
        return sorted((self.path / "KERNEL").glob("audit/commands/**/*.json"))

    def view_files(self) -> list[Path]:
        return sorted((self.path / "KERNEL" / "views").glob("*"))


class LiveActivationDocumentTests(unittest.TestCase):
    def setUp(self):
        self.live = LivePlayingRepository(self)

    def grant(self, document=None, now: str = INJECTED_NOW):
        return authorize_live_activation(
            document if document is not None else self.live.activation(),
            live_repository_root=self.live.path,
            now=now,
        )

    def test_valid_document_authorizes_and_mints_a_grant(self):
        grant, activation, findings = self.grant()
        self.assertEqual(findings, [])
        self.assertIsNotNone(activation)
        self.assertIsNotNone(grant)
        self.assertEqual(grant.repository_root, self.live.path.resolve())
        self.assertEqual(grant.kernel_root, self.live.path.resolve() / "KERNEL")
        self.assertEqual(grant.writer_id, "PROME")

    def test_document_shape_and_content_failures_refuse(self):
        base = self.live.activation()
        broken: list[tuple[str, dict]] = []
        missing = copy.deepcopy(base)
        del missing["window_end"]
        broken.append(("missing field", missing))
        extra = copy.deepcopy(base)
        extra["unregistered"] = True
        broken.append(("extra field", extra))
        broken.append(("bad authorized_by", base | {"authorized_by": "PROME"}))
        broken.append(("bad mode", base | {"mode": "LIVE"}))
        broken.append(("bad repository identity", base | {"repository": "someone-else/repo"}))
        broken.append(("relative repository_root", base | {"repository_root": "Research-workspace"}))
        broken.append(("short source_commit", base | {"source_commit": self.live.repo.commit[:12]}))
        broken.append(("inverted window", base | {"window_start": WIDE_END, "window_end": WIDE_START}))
        broken.append(("non-canonical timestamp", base | {"window_start": "2026-08-26T12:00:00Z"}))
        broken.append(("empty writer", base | {"writer_id": " "}))
        dup = copy.deepcopy(base)
        dup["commands"][1] = dict(dup["commands"][0])
        broken.append(("duplicate command", dup))
        badpath = copy.deepcopy(base)
        badpath["commands"][0]["path"] = "KERNEL/shadow/events/x.json"
        broken.append(("non-allowlisted path", badpath))
        pathmismatch = copy.deepcopy(base)
        pathmismatch["commands"][0]["path"] = pathmismatch["commands"][1]["path"]
        broken.append(("path/command_id mismatch", pathmismatch))
        badsha = copy.deepcopy(base)
        badsha["commands"][0]["sha256"] = "ZZ" * 32
        broken.append(("bad sha", badsha))
        badevents = copy.deepcopy(base)
        badevents["event_ids"] = {self.live.question["command_id"]: QUESTION_EVENT}
        broken.append(("event_ids key mismatch", badevents))
        for label, document in broken:
            with self.subTest(label=label):
                activation, findings = load_activation_document(document)
                self.assertIsNone(activation)
                self.assertEqual({finding.code for finding in findings}, {"LIVE_ACTIVATION_INVALID"})

    def test_window_not_started_closed_and_revoked_refuse(self):
        cases = [
            ("not started", self.live.activation(window=("2027-01-01T00:00:00.000000Z", "2027-01-02T00:00:00.000000Z"))),
            ("closed", self.live.activation(window=("2026-01-01T00:00:00.000000Z", "2026-01-02T00:00:00.000000Z"))),
            ("revoked", self.live.activation(
                window=("2026-08-26T00:00:00.000000Z", "2026-08-27T00:00:00.000000Z"),
                revoked_at="2026-08-26T06:00:00.000000Z",
            )),
        ]
        for label, document in cases:
            with self.subTest(label=label):
                grant, _activation, findings = self.grant(document)
                self.assertIsNone(grant)
                self.assertEqual({finding.code for finding in findings}, {"LIVE_WINDOW_REFUSED"})

    def test_repository_root_binding_mismatch_refuses(self):
        import tempfile

        with tempfile.TemporaryDirectory() as other:
            grant, _activation, findings = authorize_live_activation(
                self.live.activation(),
                live_repository_root=other,
                now=INJECTED_NOW,
            )
        self.assertIsNone(grant)
        self.assertEqual({finding.code for finding in findings}, {"LIVE_BINDING_MISMATCH"})


class LiveGrantBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.live = LivePlayingRepository(self)
        grant, _activation, findings = authorize_live_activation(
            self.live.activation(), live_repository_root=self.live.path, now=INJECTED_NOW,
        )
        self.assertEqual(findings, [])
        assert grant is not None
        self.grant = grant

    def test_grant_cannot_be_minted_directly(self):
        with self.assertRaisesRegex(ValueError, "minted only"):
            LiveShadowGrant(
                object(),
                repository_root=self.live.path,
                activation_id="X",
                writer_id="PROME",
                recorded_at=INJECTED_NOW,
            )
        with self.assertRaisesRegex(ValueError, "minted LiveShadowGrant"):
            require_live_grant(object())

    def test_store_with_grant_requires_exactly_the_granted_kernel_root(self):
        store = FixtureResultStore(self.grant.kernel_root, live_grant=self.grant)
        self.assertEqual(store.root, self.grant.kernel_root)
        with self.assertRaisesRegex(ValueError, "exactly the granted KERNEL root"):
            FixtureResultStore(self.live.path, live_grant=self.grant)
        with self.assertRaisesRegex(ValueError, "mutually exclusive"):
            FixtureResultStore(
                self.grant.kernel_root,
                live_grant=self.grant,
                forbidden_repository_root=self.live.path,
            )

    def test_lock_with_grant_requires_exactly_the_granted_repository_root(self):
        lock = FixtureAcceptanceLock(self.live.path, live_grant=self.grant)
        with lock:
            self.assertTrue(lock.held)
        with self.assertRaisesRegex(ValueError, "exactly the granted repository root"):
            FixtureAcceptanceLock(self.live.path / "KERNEL", live_grant=self.grant)

    def test_defaults_without_grant_still_refuse_repository_roots(self):
        with self.assertRaisesRegex(ValueError, "cannot target the live repository tree"):
            FixtureResultStore(self.live.path / "KERNEL", forbidden_repository_root=self.live.path)
        with self.assertRaisesRegex(ValueError, "cannot target the live repository tree"):
            FixtureAcceptanceLock(self.live.path, forbidden_repository_root=self.live.path)


class LiveWindowEnforcementTests(unittest.TestCase):
    """Adversarial review 2026-08-27, findings 1 and 2 (RED).

    Finding 1: read-only modes mint with ``require_window=False``; the grant
    must record that choice and every durable write must refuse a grant minted
    without window enforcement — read-onlyness must not rest on the call path.
    Finding 2: the writer_id-must-equal-custody-primary guard had no direct
    test in either direction.
    """

    CLOSED_WINDOW = ("2026-01-01T00:00:00.000000Z", "2026-01-02T00:00:00.000000Z")

    def setUp(self):
        self.live = LivePlayingRepository(self)

    def test_require_window_true_refuses_a_closed_window(self):
        grant, _activation, findings = authorize_live_activation(
            self.live.activation(window=self.CLOSED_WINDOW),
            live_repository_root=self.live.path,
            now=INJECTED_NOW,
            require_window=True,
        )
        self.assertIsNone(grant)
        self.assertEqual({finding.code for finding in findings}, {"LIVE_WINDOW_REFUSED"})

    def test_window_checked_grant_records_enforcement(self):
        grant, _activation, findings = authorize_live_activation(
            self.live.activation(),
            live_repository_root=self.live.path,
            now=INJECTED_NOW,
            require_window=True,
        )
        self.assertEqual(findings, [])
        assert grant is not None
        self.assertTrue(grant.window_enforced)

    def test_unenforced_window_mints_a_grant_the_store_refuses_to_publish_under(self):
        grant, _activation, findings = authorize_live_activation(
            self.live.activation(window=self.CLOSED_WINDOW),
            live_repository_root=self.live.path,
            now=INJECTED_NOW,
            require_window=False,
        )
        self.assertEqual(findings, [])
        assert grant is not None
        self.assertFalse(grant.window_enforced)
        store = FixtureResultStore(grant.kernel_root, live_grant=grant)
        with self.assertRaisesRegex(ValueError, "without window enforcement"):
            store.publish({})
        self.assertEqual(self.live.event_files(), [])
        self.assertEqual(self.live.receipt_files(), [])

    def test_unenforced_grant_refuses_durable_view_writes(self):
        from live_shadow import render_live_views
        from render import write_views

        grant, _activation, findings = authorize_live_activation(
            self.live.activation(window=self.CLOSED_WINDOW),
            live_repository_root=self.live.path,
            now=INJECTED_NOW,
            require_window=False,
        )
        self.assertEqual(findings, [])
        assert grant is not None
        store = FixtureResultStore(grant.kernel_root, live_grant=grant)
        with self.assertRaisesRegex(ValueError, "without window enforcement"):
            render_live_views(store, grant, [], render_as_of=INJECTED_NOW, check=False)
        with self.assertRaisesRegex(ValueError, "without window enforcement"):
            write_views(
                {"CALIBRATION.tsv": "", "EXCEPTIONS.md": "", "OPEN_QUESTIONS.md": "", "RESOLUTION_QUEUE.md": ""},
                grant.views_root,
                check=False,
                live_grant=grant,
            )
        self.assertEqual(self.live.view_files(), [])
        # check=True is the read/compare mode and must stay reachable for the
        # read-only CLI path: it may report findings but must not refuse.
        _views, check_findings = render_live_views(
            store, grant, [], render_as_of=INJECTED_NOW, check=True
        )
        self.assertTrue(all(f.code in {"VIEW_MISSING", "VIEW_DRIFT"} for f in check_findings))
        self.assertEqual(self.live.view_files(), [])

    def test_writer_id_must_equal_custody_primary_refuses(self):
        document = self.live.activation(writer_id="RED")
        path = self.live.write_activation(document, self)
        with self.assertRaises(LiveRefusal) as context:
            prepare_live_inputs(
                activation_path=path,
                live_repository_root=self.live.path,
                submission_commit=self.live.submission_commit,
                custody_activation_path=None,
                now=INJECTED_NOW,
                require_window=True,
                load_submissions=True,
            )
        self.assertEqual(
            {finding.code for finding in context.exception.findings},
            {"LIVE_BINDING_MISMATCH"},
        )
        self.assertIn("custody policy primary writer", str(context.exception))
        self.assertEqual(self.live.event_files(), [])
        self.assertEqual(self.live.receipt_files(), [])


class LiveShadowCliTests(unittest.TestCase):
    def setUp(self):
        self.live = LivePlayingRepository(self)

    def cli(self, *mode: str, document: dict | None = None, extra: tuple[str, ...] = ()) -> int:
        activation = self.live.write_activation(
            document if document is not None else self.live.activation(), self
        )
        argv = [
            "--activation", str(activation),
            "--live-repository-root", str(self.live.path),
            "--submission-commit", self.live.submission_commit,
            *extra,
            *mode,
        ]
        return main(argv)

    def test_preflight_is_read_only_and_passes(self):
        self.assertEqual(self.cli("--preflight"), 0)
        self.assertEqual(self.live.event_files(), [])
        self.assertEqual(self.live.receipt_files(), [])
        self.assertEqual(self.live.view_files(), [])

    def test_window_refusal_via_cli_writes_nothing(self):
        closed = self.live.activation(window=("2026-01-01T00:00:00.000000Z", "2026-01-02T00:00:00.000000Z"))
        self.assertEqual(self.cli("--apply", document=closed), 1)
        self.assertEqual(self.live.event_files(), [])
        self.assertEqual(self.live.receipt_files(), [])

    def test_pinned_policy_hash_mismatch_refuses_before_write(self):
        drifted = self.live.activation(actors_sha256="0" * 64)
        self.assertEqual(self.cli("--apply", document=drifted), 1)
        self.assertEqual(self.live.event_files(), [])

    def test_submission_pin_mismatches_refuse_before_write(self):
        base = self.live.activation()
        wrong_hash = copy.deepcopy(base)
        wrong_hash["commands"][0]["sha256"] = "0" * 64
        absent = copy.deepcopy(base)
        absent["commands"][0]["path"] = (
            "AGENTS/SAM/outbox/kernel/submissions/CMD-018f22e2-7d00-7000-8000-0000000000ff.json"
        )
        absent["commands"][0]["command_id"] = "CMD-018f22e2-7d00-7000-8000-0000000000ff"
        absent["event_ids"] = {
            "CMD-018f22e2-7d00-7000-8000-0000000000ff": QUESTION_EVENT,
            self.live.forecast["command_id"]: FORECAST_EVENT,
        }
        for label, document in (("wrong hash", wrong_hash), ("absent submission", absent)):
            with self.subTest(label=label):
                self.assertEqual(self.cli("--apply", document=document), 1)
                self.assertEqual(self.live.event_files(), [])

    def test_apply_writes_exact_results_and_views_and_is_idempotent(self):
        self.assertEqual(self.cli("--apply"), 0)
        events = self.live.event_files()
        self.assertEqual(
            [path.name for path in events],
            sorted([f"{QUESTION_EVENT}.json", f"{FORECAST_EVENT}.json"]),
        )
        for path in events:
            document = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(document["authority_mode"], "SHADOW")
            self.assertEqual(document["writer_id"], "PROME")
            self.assertEqual(document["actor_id"], "SAM")
            relative = path.relative_to(self.live.path).as_posix()
            self.assertRegex(relative, r"^KERNEL/shadow/events/\d{4}/\d{2}/EVT-")
        self.assertEqual(self.live.receipt_files(), [])
        views = self.live.view_files()
        self.assertEqual(
            [path.name for path in views],
            ["CALIBRATION.tsv", "EXCEPTIONS.md", "OPEN_QUESTIONS.md", "RESOLUTION_QUEUE.md"],
        )
        for path in views:
            self.assertIn("SHADOW", path.read_text(encoding="utf-8"))

        self.assertEqual(self.cli("--apply"), 0)
        self.assertEqual(self.live.event_files(), events)

    def test_apply_refuses_under_active_substitute_custody_then_recovers(self):
        import tempfile

        custody = {
            "schema_version": "kernel.custody.1",
            "policy_version": "kernel.policy.1",
            "activation_id": "CUSTODY-LIVE-TEST",
            "authorized_by": "WILL",
            "substitute_writer_id": "RED",
            "window_start": WIDE_START,
            "window_end": WIDE_END,
            "command_ids": [self.live.question["command_id"], self.live.forecast["command_id"]],
            "revoked_at": None,
        }
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        custody_path = Path(temporary.name) / "custody-activation.json"
        custody_path.write_text(json.dumps(custody), encoding="utf-8")
        self.assertEqual(
            self.cli("--apply", extra=("--custody-activation", str(custody_path))), 1
        )
        self.assertEqual(self.live.event_files(), [])
        self.assertEqual(self.live.receipt_files(), [])
        self.assertEqual(self.cli("--apply"), 0)
        self.assertEqual(len(self.live.event_files()), 2)

    def test_check_views_passes_then_detects_drift(self):
        self.assertEqual(self.cli("--apply"), 0)
        self.assertEqual(self.cli("--check-views"), 0)
        target = self.live.path / "KERNEL" / "views" / "OPEN_QUESTIONS.md"
        target.write_text(target.read_text(encoding="utf-8") + "hand edit\n", encoding="utf-8")
        self.assertEqual(self.cli("--check-views"), 1)

    def test_audit_additions_passes_then_blocks_modification(self):
        self.assertEqual(self.cli("--apply"), 0)
        git(self.live.path, "add", "KERNEL")
        git(self.live.path, "commit", "-q", "-m", "pilot results")
        head = git(self.live.path, "rev-parse", "HEAD")
        self.assertEqual(
            self.cli("--audit-additions", extra=("--base", self.live.submission_commit, "--head", head)),
            0,
        )
        event = self.live.event_files()[0]
        event.write_text(event.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        git(self.live.path, "add", str(event.relative_to(self.live.path)))
        git(self.live.path, "commit", "-q", "-m", "tamper")
        tampered = git(self.live.path, "rev-parse", "HEAD")
        self.assertEqual(
            self.cli("--audit-additions", extra=("--base", self.live.submission_commit, "--head", tampered)),
            1,
        )


if __name__ == "__main__":
    unittest.main()
