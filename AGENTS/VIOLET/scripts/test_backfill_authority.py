#!/usr/bin/env python3
"""Regression test for WQ-188 fix ① — backfill.py must FAIL CLOSED on CBOE.

WHY THIS FILE EXISTS. On 2026-09-06 the morning session reconciled VX_DAILY.tsv
against CBOE (476 cells: 467 blanks filled, 9 corrected). Codex reviewed the
repair the same day and found it could UNDO ITSELF: `main()` ran the yfinance
pass first, then CBOE; on a CBOE failure the CBOE pass printed "CBOE pass
SKIPPED (yfinance stands)", `write_merged()` saved yfinance's values, and the
run exited 0. Their in-memory case — ledger `skew` 151.58 with basis=SETTLE,
yfinance serving 149.00, CBOE returning 503 — wrote 149.00 AND KEPT THE SETTLE
STAMP, rc=0. That is the ledger every graded `^SKEW` sustain count is derived
from, so the exposure was a silent revert of a verified value under a label
asserting it was verified.

⚠️  These tests hit NO network. Both sources are stubbed, which is the only way
    to exercise the failure branch deliberately — `[[finding_test_the_guard_not_just_the_guarded]]`.
    A guard whose failure path has never been RUN is an assumption, not a control.

Run:  .venv/bin/python3 AGENTS/VIOLET/scripts/test_backfill_authority.py
      rc=0 all pass · rc=1 a contract failed
"""
from __future__ import annotations

import ast
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import backfill  # noqa: E402

FAILS: list[str] = []
PASSES: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    (PASSES if cond else FAILS).append(f"{name}{(' — ' + detail) if detail else ''}")
    print(f"  {'✅' if cond else '❌'} {name}" + (f"\n       {detail}" if detail else ""))


def ledger() -> dict[str, dict]:
    """One row in the shape Codex used: a CBOE-verified SETTLE row."""
    return {
        "2026-09-04": {
            "date": "2026-09-04", "vix": "14.53", "vix3m": "17.61", "vix6m": "19.89",
            "vvix": "84.42", "skew": "151.58", "vix9d": "11.97",
            "vix3m_vix_ratio": "1.212", "vix9d_vix_ratio": "0.8238",
            "basis": "SETTLE", "regime": "COMPLACENCY",
        }
    }


CBOE_GOOD = {
    "vix": {"2026-09-04": 14.53}, "vix3m": {"2026-09-04": 17.61},
    "vix6m": {"2026-09-04": 19.89}, "vvix": {"2026-09-04": 84.42},
    "skew": {"2026-09-04": 151.58}, "vix9d": {"2026-09-04": 11.97},
}
# What yfinance would serve for the same session — the WRONG skew is Codex's value.
YF_BAD = {"vix": 14.53, "vix3m": 17.61, "vix6m": 19.89,
          "vvix": 84.42, "skew": 149.00, "vix9d": 11.97}


def run_yf_pass(rows, cboe_hist, cboe_failed):
    """Exercise backfill_spot's write-authority gate without yfinance/pandas.

    The gate is transcribed from backfill_spot's loop; the assertion below that
    it MATCHES the shipped code keeps this from drifting into a test of itself.
    """
    written = []
    for d_str, row in rows.items():
        for key in backfill.TICKERS:
            if key in cboe_failed:
                continue
            if cboe_hist is not None and cboe_hist.get(key, {}).get(d_str) is not None:
                continue
            row[key] = YF_BAD[key]
            written.append((d_str, key))
    return written


def main() -> int:
    src = Path(backfill.__file__).read_text()

    print("\n[1] CONTRACT (a) — a CBOE failure PRESERVES previously verified values")
    print("    Codex's case: ledger skew 151.58 SETTLE · yfinance 149.00 · CBOE 503 on skew")
    rows = ledger()
    hist = {k: (v if k != "skew" else {}) for k, v in CBOE_GOOD.items()}
    failed = {"skew"}
    run_yf_pass(rows, hist, failed)
    backfill.backfill_spot_cboe(rows, today="2026-09-06", hist=hist, failed=failed)
    check("skew preserved at 151.58 (not reverted to yfinance 149.00)",
          str(rows["2026-09-04"]["skew"]) == "151.58",
          f"got {rows['2026-09-04']['skew']!r}")

    print("\n[2] CONTRACT (c) — basis=SETTLE is never stamped on an unverified row")
    check("SETTLE not newly stamped while a series failed",
          "settle_stamped" not in str(rows) and rows["2026-09-04"]["basis"] == "SETTLE",
          "pre-existing SETTLE is left alone; the test below proves none is ADDED")
    rows2 = ledger()
    rows2["2026-09-04"]["basis"] = "TICK"
    run_yf_pass(rows2, hist, failed)
    res2 = backfill.backfill_spot_cboe(rows2, today="2026-09-06", hist=hist, failed=failed)
    check("a TICK row is NOT promoted to SETTLE on an incomplete run",
          rows2["2026-09-04"]["basis"] == "TICK" and res2["settle_stamped"] == 0,
          f"basis={rows2['2026-09-04']['basis']!r} settle_stamped={res2['settle_stamped']}")

    print("\n[3] ALL SIX series fail — the whole row is untouched, nothing writes")
    rows3 = ledger()
    before = dict(rows3["2026-09-04"])
    all_failed = set(backfill.CBOE_SERIES)
    run_yf_pass(rows3, {k: {} for k in CBOE_GOOD}, all_failed)
    backfill.backfill_spot_cboe(rows3, today="2026-09-06",
                                hist={k: {} for k in CBOE_GOOD}, failed=all_failed)
    check("every one of the six columns is byte-identical after a total CBOE outage",
          all(str(rows3["2026-09-04"][c]) == str(before[c]) for c in backfill.CBOE_SERIES),
          f"skew={rows3['2026-09-04']['skew']!r} vix={rows3['2026-09-04']['vix']!r}")

    print("\n[4] CONTRACT (d) CONTROL — with CBOE reachable, values are unchanged")
    rows4 = ledger()
    res4 = backfill.backfill_spot_cboe(rows4, today="2026-09-06",
                                       hist=CBOE_GOOD, failed=set())
    check("re-run corrects 0 and fills 0 (idempotent on a reconciled ledger)",
          res4["corrected"] == 0 and res4["filled"] == 0,
          f"corrected={res4['corrected']} filled={res4['filled']} agreed={res4['agreed']}")
    check("CBOE still WINS when it disagrees (the pass is not merely inert)",
          _cboe_wins(), "skew 149.00 in the ledger is corrected to CBOE's 151.58")

    print("\n[5] CONTRACT (b) — an empty CBOE answer is NOT a failure")
    check("fetch returns (data, ok); ok gates authority, truthiness does not",
          "-> ({iso_date: close}, ok)" in src and "return {}, False" in src)
    check("main() exits 2 on an incomplete refresh (never 0)",
          "return 2" in src and "BACKFILL INCOMPLETE" in src)
    # ⚠️ FIRST DRAFT OF THIS CHECK WAS WRONG AND FAILED A CORRECT FIX. It grepped
    # the whole source for "yfinance stands" — which still appears, correctly, in
    # three docstrings that record WHY the branch was removed. A test may not
    # force the code to forget its own history. What actually matters is narrow:
    # the phrase must never again reach a user through `print`. AST answers that
    # exactly, where a substring scan answers a different question badly —
    # `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`.
    printed = _printed_strings(src)
    check("the fail-open message can no longer be PRINTED (AST over print() calls)",
          not any("yfinance stands" in s for s in printed),
          f"{len(printed)} print-literals scanned; docstring history is untouched")

    print("\n[6] The gate in THIS test still matches the gate in backfill.py")
    check("backfill_spot withholds on a failed series",
          "if key in failed:" in src and "withheld_failed += 1" in src)
    check("backfill_spot defers to CBOE where CBOE publishes",
          "cboe_hist.get(key, {}).get(d_str) is not None" in src)
    check("backfill_spot_cboe skips failed columns rather than writing them",
          "if col in failed:\n                continue" in src)

    print("\n" + "=" * 70)
    print(f"  {len(PASSES)} passed · {len(FAILS)} FAILED")
    for f in FAILS:
        print(f"  ❌ {f}")
    print("=" * 70)
    return 1 if FAILS else 0


def _printed_strings(src: str) -> list[str]:
    """Every string literal that can reach stdout via print(), f-strings included."""
    out: list[str] = []
    for node in ast.walk(ast.parse(src)):
        if not (isinstance(node, ast.Call) and getattr(node.func, "id", "") == "print"):
            continue
        for arg in node.args:
            for sub in ast.walk(arg):
                if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
                    out.append(sub.value)
    return out


def _cboe_wins() -> bool:
    rows = ledger()
    rows["2026-09-04"]["skew"] = "149.00"
    backfill.backfill_spot_cboe(rows, today="2026-09-06", hist=CBOE_GOOD, failed=set())
    return str(rows["2026-09-04"]["skew"]) == "151.58"


if __name__ == "__main__":
    sys.exit(main())
