import argparse
import tempfile
import unittest
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from msg import MessagingError, allocation_lock, compose, compose_file, receipt_lock, record_receipt  # noqa: E402
from validate import load_agents, validate  # noqa: E402


def compose_args(repo: Path, *, write: bool = False, subject: str = "Grade KOC platform hit") -> argparse.Namespace:
    return argparse.Namespace(
        repo_root=repo,
        sender="PROME",
        recipient="BRENT",
        role="ACTION",
        urgency="NEXT_BOOT",
        subject=subject,
        requested_action="Grade the KOC hit.",
        definition_of_done="Record a grade or sourced NO_CHANGE.",
        due=None,
        receipt_required=False,
        expected_target=["AGENTS/BRENT/STATUS.md"],
        related=[],
        supersedes=None,
        created_at="2026-07-14T14:00:00+00:00",
        body="Test context.",
        body_file=None,
        write=write,
    )


def receipt_args(repo: Path, message: Path, event: str, **overrides) -> argparse.Namespace:
    values = dict(
        repo_root=repo,
        message=message,
        recipient="BRENT",
        obligation_id="MSG-PROME-20260714-001#BRENT-01",
        event=event,
        event_at="2026-07-14T14:10:00+00:00" if event == "ACCEPTED" else "2026-07-14T15:00:00+00:00",
        next_review_at=None,
        target_path=None,
        effect_or_reason="Accepted for review" if event == "ACCEPTED" else None,
        commit=None,
        evidence_tier="ASSERTED" if event == "ACCEPTED" else None,
    )
    values.update(overrides)
    return argparse.Namespace(**values)


class MessagingCliTests(unittest.TestCase):
    def make_repo(self, root: Path, mode: str = "test") -> None:
        (root / "MESSAGING").mkdir(parents=True)
        (root / "MESSAGING/config.yaml").write_text(
            f'schema: direct-messaging-config/v1\nwrite_mode: {mode}\nreason: "fixture"\n', encoding="utf-8"
        )
        (root / "PROME").mkdir()
        (root / "PROME/ROSTER.md").write_text("| Agent | Domain |\n|---|---|\n| PROME | Coordinator |\n| BRENT | Oil |\n| SAM | Japan |\n", encoding="utf-8")
        (root / "AGENTS/BRENT/inbox").mkdir(parents=True)
        (root / "AGENTS/SAM/inbox").mkdir(parents=True)

    def set_cohort(self, root: Path) -> None:
        (root / "MESSAGING/config.yaml").write_text(
            "schema: direct-messaging-config/v1\n"
            "write_mode: cohort\n"
            "allowed_senders: [PROME]\n"
            "allowed_recipients: [BRENT, SAM]\n"
            'reason: "fixture cohort"\n',
            encoding="utf-8",
        )

    def test_preview_has_no_side_effects(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self.make_repo(repo, mode="disabled")
            text, destination = compose(compose_args(repo))
            self.assertIn("MSG-PROME-20260714-001", text)
            self.assertFalse(destination.exists())
            self.assertFalse((repo / "MESSAGING/runtime").exists())

    def test_write_refuses_when_disabled(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self.make_repo(repo, mode="disabled")
            with self.assertRaises(MessagingError):
                compose(compose_args(repo, write=True))

    def test_live_cohort_allows_prome_to_brent(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self.make_repo(repo)
            self.set_cohort(repo)
            _, destination = compose(compose_args(repo, write=True))
            self.assertTrue(destination.exists())

    def test_live_cohort_rejects_non_allowlisted_recipient(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self.make_repo(repo)
            self.set_cohort(repo)
            args = compose_args(repo, write=True)
            args.recipient = "NEXUS"
            (repo / "AGENTS/NEXUS/inbox").mkdir(parents=True)
            (repo / "PROME/ROSTER.md").write_text(
                (repo / "PROME/ROSTER.md").read_text() + "| NEXUS | Synthesis |\n", encoding="utf-8"
            )
            with self.assertRaises(MessagingError):
                compose(args)

    def test_multi_obligation_file_fans_out_with_one_identity(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self.make_repo(repo)
            self.set_cohort(repo)
            spec = repo / "draft.yaml"
            spec.write_text(
                "sender: PROME\n"
                'created_at: "2026-07-14T14:00:00+00:00"\n'
                'subject: "Two-agent activation packet"\n'
                "body: Cohort test.\n"
                "obligations:\n"
                "  - to: BRENT\n"
                "    role: ACTION\n"
                "    urgency: NEXT_BOOT\n"
                "    requested_action: Re-score the matrix.\n"
                "    definition_of_done: Matrix is current.\n"
                "    expected_targets: [AGENTS/BRENT/STATUS.md]\n"
                "  - to: BRENT\n"
                "    role: INFO\n"
                "    urgency: ROUTINE\n"
                "  - to: SAM\n"
                "    role: ACTION\n"
                "    urgency: NEXT_BOOT\n"
                "    requested_action: Re-pencil the buckets.\n"
                "    definition_of_done: Buckets are current.\n"
                "    expected_targets: [AGENTS/SAM/STATUS.md]\n",
                encoding="utf-8",
            )
            text, destinations = compose_file(argparse.Namespace(repo_root=repo, spec=spec, write=True))
            self.assertEqual(len(destinations), 2)
            self.assertTrue(all(path.exists() for path in destinations))
            self.assertEqual(text.count("message_id: MSG-PROME-20260714-001"), 1)
            self.assertIn("#BRENT-02", text)
            self.assertIn("#SAM-01", text)
            report = validate(destinations, load_agents(repo, None))
            self.assertEqual(report.errors, 0, report.findings)
            self.assertEqual(len(report.messages), 1)
            self.assertEqual(len(report.obligations), 3)

    def test_allocator_contention_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self.make_repo(repo)
            with allocation_lock(repo, "PROME", "20260714"):
                with self.assertRaises(MessagingError):
                    compose(compose_args(repo, write=True))

    def test_test_write_allocates_monotonic_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self.make_repo(repo)
            _, first = compose(compose_args(repo, write=True))
            _, second = compose(compose_args(repo, write=True, subject="Reconcile GCC figure"))
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertIn("-001__", first.name)
            self.assertIn("-002__", second.name)

    def test_receipt_lifecycle_end_to_end(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self.make_repo(repo)
            _, message = compose(compose_args(repo, write=True))
            _, receipt, changed = record_receipt(receipt_args(repo, message, "ACCEPTED"))
            self.assertTrue(changed)
            _, _, changed = record_receipt(
                receipt_args(
                    repo,
                    message,
                    "NO_CHANGE",
                    target_path="AGENTS/BRENT/STATUS.md",
                    effect_or_reason="Current grade remains valid after review.",
                    evidence_tier="POINTED",
                )
            )
            self.assertTrue(changed)
            report = validate([message, receipt], load_agents(repo, None))
            self.assertEqual(report.errors, 0, report.findings)

    def test_exact_duplicate_receipt_event_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self.make_repo(repo)
            _, message = compose(compose_args(repo, write=True))
            args = receipt_args(repo, message, "ACCEPTED")
            record_receipt(args)
            _, _, changed = record_receipt(args)
            self.assertFalse(changed)

    def test_receipt_contention_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self.make_repo(repo)
            _, message = compose(compose_args(repo, write=True))
            with receipt_lock(repo, "BRENT", "MSG-PROME-20260714-001"):
                with self.assertRaises(MessagingError):
                    record_receipt(receipt_args(repo, message, "ACCEPTED"))

    def test_wrong_recipient_cannot_write_receipt(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self.make_repo(repo)
            _, message = compose(compose_args(repo, write=True))
            args = receipt_args(repo, message, "ACCEPTED", recipient="SAM")
            with self.assertRaises(MessagingError):
                record_receipt(args)

    def test_receipt_rejects_message_outside_repository(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            repo = Path(tmp)
            self.make_repo(repo)
            text, _ = compose(compose_args(repo))
            message = Path(outside) / "message.md"
            message.write_text(text, encoding="utf-8")
            with self.assertRaises(MessagingError):
                record_receipt(receipt_args(repo, message, "ACCEPTED"))

    def test_blocked_requires_next_review(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self.make_repo(repo)
            _, message = compose(compose_args(repo, write=True))
            with self.assertRaises(MessagingError):
                record_receipt(
                    receipt_args(repo, message, "BLOCKED", effect_or_reason="Waiting for source publication")
                )

    def test_event_after_terminal_is_rejected_without_file_change(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self.make_repo(repo)
            _, message = compose(compose_args(repo, write=True))
            _, receipt, _ = record_receipt(
                receipt_args(
                    repo,
                    message,
                    "NO_CHANGE",
                    target_path="AGENTS/BRENT/STATUS.md",
                    effect_or_reason="No change warranted.",
                    evidence_tier="POINTED",
                )
            )
            before = receipt.read_text()
            with self.assertRaises(MessagingError):
                record_receipt(receipt_args(repo, message, "ACCEPTED", event_at="2026-07-14T16:00:00+00:00"))
            self.assertEqual(before, receipt.read_text())


if __name__ == "__main__":
    unittest.main()
