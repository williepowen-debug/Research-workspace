"""SP6: two same-minute builds can misidentify the page recorded as hosted.

Uses the owner's throwaway fixture and production functions; no live build,
hosted record, publication, gate, commit or push. Refuses changed source bytes.
Run from the Git root with python3 -B. --source/--fixture can select saved copies
of the exact reviewed files. This is one counterexample, not a full review.
"""
import argparse
import datetime
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
from unittest.mock import patch

SOURCE_SHA = "ba1ea586cbc2f2c7e0b6b0b728f5d04e7ebc239e76afc69f9b33815cd9ffc596"
FIXTURE_SHA = "354471f4d7be17205989da1ddbc59cb1e4e094748a4cc9ca6374f663e334b7fb"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", type=Path, default=Path("PROME/tools/decision_deck.py"))
    ap.add_argument("--fixture", type=Path, default=Path("PROME/tools/tests/test_deck_owed_digest_L738.py"))
    args = ap.parse_args()
    if digest(args.source) != SOURCE_SHA or digest(args.fixture) != FIXTURE_SHA:
        ap.error("reviewed bytes changed; select the pinned source/fixture, do not infer this old result")
    spec = importlib.util.spec_from_file_location("decision_deck", args.source.resolve())
    deck = importlib.util.module_from_spec(spec)
    sys.modules["decision_deck"] = deck
    spec.loader.exec_module(deck)
    spec = importlib.util.spec_from_file_location("cato_l738_fixture", args.fixture.resolve())
    fixture = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fixture)
    real_datetime = datetime.datetime

    class FrozenDateTime(real_datetime):
        @classmethod
        def now(cls, tz=None):
            value = cls(2026, 10, 16, 4, 30, 10, tzinfo=datetime.timezone.utc)
            return value.astimezone(tz) if tz else value.replace(tzinfo=None)

    case = fixture.OwedDigest("test_a4b_record_copies_the_build_receipt_not_the_queue")
    try:
        case.setUp()
        with patch.object(deck.dt, "datetime", FrozenDateTime):
            a = case.hosted_build()
            fps_a = case.current()
            page_a = case.root / "published-A.html"
            page_a.write_bytes(case.out.read_bytes())
            case.write_queue(fixture.ROW_A.replace("note a", "note B NOT HOSTED")
                             + fixture.ROW_B + fixture.ROW_C)
            b = case.hosted_build()
            fps_b = case.current()
            rc, _ = deck.record_hosted_owed("v-A", deck.page_build_id(page_a))
            hosted = json.loads(deck._owed_hosted_path().read_text())
            verdict = deck.republish_verdict(fps_b, extras=deck.current_extras())
            result = {
                "source_sha256": SOURCE_SHA, "fixture_sha256": FIXTURE_SHA,
                "different_content": fps_a != fps_b,
                "same_build_id": a["build_id"] == b["build_id"],
                "record_rc": rc,
                "hosted_equals_A": hosted["fingerprints"] == fps_a,
                "hosted_equals_unpublished_B": hosted["fingerprints"] == fps_b,
                "current_B_verdict": verdict,
                "real_publish": False,
            }
            assert digest(args.source) == SOURCE_SHA and digest(args.fixture) == FIXTURE_SHA
            assert result["different_content"] and result["same_build_id"]
            assert rc == 0 and not result["hosted_equals_A"]
            assert result["hosted_equals_unpublished_B"] and verdict[0] == "NO-OP"
            print(json.dumps(result, indent=2))
    finally:
        case.doCleanups()


if __name__ == "__main__":
    main()
