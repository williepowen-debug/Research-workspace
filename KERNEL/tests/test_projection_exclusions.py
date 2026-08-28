"""Registered projection exclusions (kernel.renderer.2, 2026-08-28).

Why this file exists: the MIDAS-06 scoring fence (Will, 8/28: the forecast row
renders UNSCORED — OUTCOME VOCABULARY MISMATCH *regardless of outcome*) had been
written into the docket, the prep file and the reviewer packet — and the
renderer still scored a FINAL YES or NO on the stated probability, excluding
only AMBIGUOUS (Codex cross-vendor follow-up, confirmed at render.py). A ruling
that names a render behaviour is not implemented until the code path carries
it. These tests are the discriminating cases: FINAL YES, FINAL NO, FINAL
AMBIGUOUS and NOT_FINAL all render unscored with the registered reason; an
unlisted question is untouched; a malformed registry fails closed; the registry
joins the source-input digest; and the LIVE registry file names MIDAS-06's
accepted question_id (the wiring proof, not just the mechanism).
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from core import validate_event  # noqa: E402
from render import (  # noqa: E402
    DEFAULT_EXCLUSIONS_RELPATH,
    EXCLUSION_REASONS,
    RENDERER_VERSION,
    load_projection_exclusions,
    render_views,
    validate_projection_exclusions,
)
from test_lifecycle import (  # noqa: E402
    FORECAST_ID,
    QUESTION_ID,
    close_command,
    forecast_command,
    propose_command,
    question_command,
    typed_id,
    verify_command,
)
from writer import FixtureResultStore, FixtureResultWriter  # noqa: E402


AS_OF = "2026-09-19T00:00:00.000000Z"
REASON = "OUTCOME_VOCABULARY_MISMATCH"


def registry(question_id: str = QUESTION_ID, reason: str = REASON) -> dict:
    return {
        "schema_version": "kernel.projection-exclusions.1",
        "policy_version": "kernel.policy.1",
        "registry_id": "projection-exclusions",
        "exclusions": [
            {
                "question_id": question_id,
                "exclusion_reason": reason,
                "ruled_by": "WILL",
                "ruled_at": "2026-08-28",
                "ruling_record": "PROME/proposals/2026-08-28_codex-high-value-audit-RULED.md",
            }
        ],
    }


def calibration_row(views: dict[str, str], forecast_id: str = FORECAST_ID) -> list[str]:
    for line in views["CALIBRATION.tsv"].splitlines():
        if line.startswith("Q-") and forecast_id in line:
            return line.split("\t")
    raise AssertionError("forecast row missing from CALIBRATION.tsv")


def metadata(views: dict[str, str], key: str) -> str:
    for line in views["CALIBRATION.tsv"].splitlines():
        if line.startswith(f"# {key}: "):
            return line[len(f"# {key}: "):]
    raise AssertionError(f"metadata {key} missing")


class ProjectionExclusionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.store = FixtureResultStore(Path(self.temporary.name) / "KERNEL")
        self.writer = FixtureResultWriter(self.store, writer_id="PROME")

    def tearDown(self):
        self.temporary.cleanup()

    def accept(self, command: dict, event_number: int) -> dict:
        outcome = self.writer.accept(command, event_id=typed_id("EVT", event_number),
                                     recorded_at=command["submitted_at"])
        self.assertEqual(outcome.state, "WRITTEN", outcome.finding)
        self.assertTrue(validate_event(outcome.document).valid)
        return outcome.document

    def not_final(self) -> list[dict]:
        self.accept(question_command(), 601)
        self.accept(forecast_command(), 602)
        return self.store.accepted_events()

    def final(self, outcome: str) -> list[dict]:
        self.not_final()
        self.accept(close_command(), 604)
        propose = propose_command()
        propose["payload"]["outcome_value"] = outcome
        self.accept(propose, 605)
        verify = verify_command()
        verify["payload"]["verified_outcome_value"] = outcome
        self.accept(verify, 606)
        return self.store.accepted_events()

    # --- the discriminating cases -------------------------------------------------
    def test_without_registry_final_yes_and_no_are_scored(self):
        for outcome, expected in (("YES", "0.1225"), ("NO", "0.4225")):
            with self.subTest(outcome=outcome):
                self.setUp()
                row = calibration_row(render_views(self.final(outcome), render_as_of=AS_OF))
                self.assertEqual(row[4], outcome)
                self.assertEqual(row[5], expected)          # (0.65 − target)² on the fixture forecast
                self.assertEqual(row[6], "")
                self.tearDown()

    def test_registered_exclusion_unscores_in_every_state(self):
        cases = {"YES": self.final, "NO": self.final, "AMBIGUOUS": self.final}
        for outcome, build in cases.items():
            with self.subTest(outcome=outcome):
                self.setUp()
                views = render_views(build(outcome), render_as_of=AS_OF, projection_exclusions=registry())
                row = calibration_row(views)
                self.assertEqual(row[4], outcome)
                self.assertEqual(row[5], "", "a registered exclusion must never carry a score")
                self.assertEqual(row[6], REASON)
                self.tearDown()
        self.setUp()
        row = calibration_row(render_views(self.not_final(), render_as_of=AS_OF, projection_exclusions=registry()))
        self.assertEqual(row[4], "")
        self.assertEqual(row[5], "")
        self.assertEqual(row[6], REASON, "the exclusion is visible before finality, not only at scoring time")

    def test_unlisted_question_is_untouched_by_the_registry(self):
        other = registry(question_id=typed_id("Q", 999))
        events = self.final("YES")
        with_registry = calibration_row(render_views(events, render_as_of=AS_OF, projection_exclusions=other))
        without = calibration_row(render_views(events, render_as_of=AS_OF))
        self.assertEqual(with_registry, without)
        self.assertEqual(with_registry[5], "0.1225")

    def test_malformed_registry_fails_closed(self):
        bad_reason = registry(reason="NOT_A_REGISTERED_REASON")
        missing = registry()
        del missing["exclusions"][0]["ruling_record"]
        duplicate = registry()
        duplicate["exclusions"].append(copy.deepcopy(duplicate["exclusions"][0]))
        wrong_schema = registry()
        wrong_schema["schema_version"] = "kernel.projection-exclusions.0"
        wrong_id = registry()
        wrong_id["registry_id"] = "something-else"
        events = self.final("YES")
        for label, document in (("reason", bad_reason), ("missing", missing), ("duplicate", duplicate),
                                ("schema", wrong_schema), ("registry_id", wrong_id), ("shape", ["not", "an", "object"])):
            with self.subTest(label=label):
                with self.assertRaises(ValueError):
                    validate_projection_exclusions(document)
                with self.assertRaises(ValueError):
                    render_views(events, render_as_of=AS_OF, projection_exclusions=document)

    def test_registry_joins_the_source_input_digest_and_renderer_version_moved(self):
        events = self.final("YES")
        plain = render_views(events, render_as_of=AS_OF)
        fenced = render_views(events, render_as_of=AS_OF, projection_exclusions=registry())
        self.assertEqual(int(metadata(fenced, "source_input_count")), int(metadata(plain, "source_input_count")) + 1)
        self.assertNotEqual(metadata(fenced, "source_input_set_sha256"), metadata(plain, "source_input_set_sha256"))
        self.assertEqual(metadata(fenced, "renderer_version"), RENDERER_VERSION)
        self.assertEqual(RENDERER_VERSION, "kernel.renderer.2")
        # deterministic under input order, with the registry present
        again = render_views(list(reversed(events)), render_as_of=AS_OF, projection_exclusions=registry())
        self.assertEqual(fenced, again)

    def test_reason_set_is_the_one_enumerated_reason(self):
        self.assertEqual(set(EXCLUSION_REASONS), {REASON})

    # --- wiring proof: the LIVE registry names MIDAS-06's accepted question --------
    def test_live_registry_file_validates_and_names_midas06(self):
        path = REPO / DEFAULT_EXCLUSIONS_RELPATH
        self.assertTrue(path.exists(), f"live registry missing at {path}")
        registry_doc = load_projection_exclusions(path)
        self.assertIsNotNone(registry_doc)
        entries = validate_projection_exclusions(registry_doc)
        staged = REPO / "AGENTS/MIDAS/kernel/staged_submissions/CMD-019306a1-4c00-7000-8000-00000000006a.json"
        self.assertTrue(staged.exists(), "MIDAS-06 RegisterQuestion staging copy missing")
        question_id = json.loads(staged.read_text(encoding="utf-8"))["payload"]["question_id"]
        self.assertIn(question_id, entries)
        self.assertEqual(entries[question_id]["exclusion_reason"], REASON)
        self.assertEqual(entries[question_id]["ruled_by"], "WILL")

    def test_absent_registry_file_means_no_exclusions_not_an_error(self):
        self.assertIsNone(load_projection_exclusions(Path(self.temporary.name) / "nope.json"))


if __name__ == "__main__":
    unittest.main()
