#!/usr/bin/env python3
"""END-TO-END regression test for the WQ-188 2nd pass (Codex, 2026-09-06).

WHY A SECOND TEST FILE, AND WHY IT IS THE POINT OF THIS ONE.
`test_backfill_authority.py` shipped 12 green contracts on 2026-09-06 AM over
code that still had two open holes. It went green because its `run_yf_pass()`
is a HAND TRANSCRIPTION of `backfill_spot`'s write gate — its own docstring says
so — plus a set of source-substring assertions. **A test that re-implements the
gate is testing its re-implementation; the shipped gate is never executed, so no
defect in it can ever fail the suite.**
`[[finding_crosscheck_with_free_parameter_validates_nothing]]` — zero unknowns
or it is not a test.

⚠️ It was worse than merely blind: contract [2] asserted, in words, the exact
behaviour Codex flags as the danger — *"pre-existing SETTLE is left alone"* —
and its first clause `"settle_stamped" not in str(rows)` compares a COUNTER NAME
against the repr of ledger ROWS, where it can never appear. **That clause cannot
fail.** I wrote the contracts from the fix I had just made instead of from the
failure mode, so the suite certified the hole.
`[[finding_test_the_guard_not_just_the_guarded]]`

⇒ THIS FILE RUNS THE ACTUAL PROGRAM. `backfill.main(["--spot-only"])` is called
for real; only the two EXTERNAL sources are stubbed (`requests.get` and the
`yfinance` module) and `DAILY_LOG` is redirected to a temp file. Nothing about
the write gate, the parser, the basis stamp or the exit code is transcribed —
they are executed and the resulting FILE ON DISK is asserted.

THE FOUR CBOE RESPONSES (Codex's acceptance list), plus the fill-path case the
first three do not reach:
  1. HTTP 503                       -> transport failure   (closed by WQ-188 ①)
  2. HTTP 200 carrying HTML         -> parse failure       (OPEN before this fix)
  3. valid CSV, target date absent  -> destination gate    (OPEN before this fix)
  4. valid CSV with the date        -> control, must be inert
  5. valid CSV, date absent, cell BLANK on a non-SETTLE row -> the provisional
     FILL is allowed, and the row must NOT then be stamped SETTLE.
  6. THE SAME FIXTURE RUN TWICE -> the stamp must not appear on the second run
     either (the 2nd-pass guard's per-run memory failed exactly here).
  7. RECOVERY CONTROL -> once CBOE supplies the series, its value replaces the
     provisional one and the row MUST be allowed to settle.

ACCEPTANCE, asserted on the file after each run:
  · no Yahoo value ever lands in a row labelled basis=SETTLE
  · no false-success exit — a run that could not reach the publisher exits 2

Run:  .venv/bin/python3 AGENTS/VIOLET/scripts/test_backfill_endtoend.py
      rc=0 all pass · rc=1 a contract failed
      --falsify  additionally re-runs every case against the PRE-FIX backfill.py
                 from a PINNED revision (never HEAD) and requires the fixed
                 cases to FAIL there, with a negative control.
"""
from __future__ import annotations

import importlib.util
import io
import subprocess
import sys
import tempfile
from contextlib import redirect_stdout
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

FAILS: list[str] = []
PASSES: list[str] = []

HEADER = ["date", "vix", "vix3m", "vix6m", "vvix", "skew", "vix3m_vix_ratio",
          "m1m2_strict_pct", "m1m2_adj_pct", "m1_symbol", "m2_symbol", "regime",
          "source_ts", "basis", "m1m2_settle_date", "vix9d", "vix9d_vix_ratio"]

# The row from Codex's case: a CBOE-verified SETTLE row carrying skew 151.58.
SETTLE_ROW = {
    "date": "2026-09-04", "vix": "14.53", "vix3m": "17.61", "vix6m": "19.89",
    "vvix": "84.42", "skew": "151.58", "vix3m_vix_ratio": "1.212",
    "regime": "COMPLACENCY", "basis": "SETTLE", "vix9d": "11.97",
    "vix9d_vix_ratio": "0.8238",
}

# What the mirror would serve for the same session. skew is Codex's wrong value.
YF = {"vix": 14.53, "vix9d": 11.97, "vix3m": 17.61,
      "vix6m": 19.89, "vvix": 84.42, "skew": 149.00}

TARGET = "2026-09-04"
HTML_BODY = ("<!DOCTYPE html><html><head><title>Error</title></head>"
             "<body><h1>503 Service Unavailable</h1></body></html>")


# When the HEAD (pre-fix) suite runs, its failures are the EVIDENCE, not defects
# of this suite — they must not drive the exit code. A --falsify run that returned
# rc=1 for doing exactly what it was built to do is a guard you learn to ignore
# [[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]].
EXPECT_FAILURES = False


def check(name: str, cond: bool, detail: str = "") -> None:
    if EXPECT_FAILURES:
        # Recorded and printed, but scored by the FALSIFIED: meta-checks instead.
        print(f"  {'✅' if cond else '❌'} {name}" + (f"\n       {detail}" if detail else ""))
        return
    (PASSES if cond else FAILS).append(name)
    print(f"  {'✅' if cond else '❌'} {name}" + (f"\n       {detail}" if detail else ""))


def csv_for(sym: str, include_target: bool) -> str:
    """A real-shaped CBOE daily-prices CSV. Headers verified live 2026-09-06:
    OHLC indices expose DATE,OPEN,HIGH,LOW,CLOSE; VVIX/SKEW expose DATE,<SYM>."""
    val = {"VIX": 14.53, "VIX9D": 11.97, "VIX3M": 17.61,
           "VIX6M": 19.89, "VVIX": 84.42, "SKEW": 151.58}[sym]
    older = "09/03/2026"
    if sym in ("VVIX", "SKEW"):
        head = f"DATE,{sym}\n"
        body = f"{older},{val - 1:.6f}\n"
        if include_target:
            body += f"09/04/2026,{val:.6f}\n"
    else:
        head = "DATE,OPEN,HIGH,LOW,CLOSE\n"
        body = f"{older},{val:.4f},{val:.4f},{val:.4f},{val - 1:.4f}\n"
        if include_target:
            body += f"09/04/2026,{val:.4f},{val:.4f},{val:.4f},{val:.4f}\n"
    return head + body


class Resp:
    def __init__(self, status: int, text: str):
        self.status_code, self.text = status, text


def make_requests_stub(mod, case: str):
    """Stub only the network edge. `case` selects SKEW's response; the other
    five series always answer correctly, so each test isolates ONE variable."""
    def get(url, timeout=None, headers=None):
        sym = url.rsplit("/", 1)[-1].replace("_History.csv", "")
        if sym != "SKEW":
            return Resp(200, csv_for(sym, include_target=True))
        if case == "503":
            return Resp(503, "")
        if case == "html":
            return Resp(200, HTML_BODY)
        if case == "missing_date":
            return Resp(200, csv_for("SKEW", include_target=False))
        return Resp(200, csv_for("SKEW", include_target=True))
    return get


def install_yfinance_stub():
    """Minimal yfinance: Ticker(sym).history() -> DataFrame with a Close column."""
    import pandas as pd
    import types

    rev = {v: k for k, v in {"vix": "^VIX", "vix9d": "^VIX9D", "vix3m": "^VIX3M",
                             "vix6m": "^VIX6M", "vvix": "^VVIX", "skew": "^SKEW"}.items()}

    class Ticker:
        def __init__(self, sym):
            self.key = rev[sym]

        def history(self, period=None, auto_adjust=False):
            idx = pd.to_datetime(["2026-09-03", "2026-09-04"])
            return pd.DataFrame({"Close": [YF[self.key] - 1, YF[self.key]]}, index=idx)

    mod = types.ModuleType("yfinance")
    mod.Ticker = Ticker
    sys.modules["yfinance"] = mod


def write_ledger(path: Path, row: dict) -> None:
    with open(path, "w") as f:
        f.write("\t".join(HEADER) + "\n")
        f.write("\t".join(str(row.get(c, "") or "") for c in HEADER) + "\n")


def read_ledger(path: Path) -> dict[str, dict]:
    import csv
    with open(path) as f:
        return {r["date"]: r for r in csv.DictReader(f, delimiter="\t")}


def run_case(mod, case: str, row: dict) -> tuple[int, dict, str]:
    """Run the REAL main() with the two external sources stubbed."""
    with tempfile.TemporaryDirectory() as td:
        led = Path(td) / "VX_DAILY.tsv"
        write_ledger(led, row)
        old_log, old_get = mod.DAILY_LOG, mod.requests.get
        mod.DAILY_LOG = led
        mod.requests.get = make_requests_stub(mod, case)
        buf = io.StringIO()
        try:
            with redirect_stdout(buf):
                rc = mod.main(["--spot-only"])
        finally:
            mod.DAILY_LOG, mod.requests.get = old_log, old_get
        return rc, read_ledger(led), buf.getvalue()


def assert_case(mod, case: str, label: str, row: dict, *,
                expect_skew: str, expect_rc, tag: str) -> bool:
    rc, led, _ = run_case(mod, case, row)
    got = led[TARGET]
    skew_ok = str(got["skew"]).startswith(expect_skew)
    rc_ok = (rc in expect_rc) if isinstance(expect_rc, (set, tuple, list)) else (rc == expect_rc)
    # THE ACCEPTANCE CRITERION, asserted on the FILE: no mirror value under SETTLE.
    settle_clean = not (str(got.get("basis", "")).strip().upper() == "SETTLE"
                        and abs(float(got["skew"]) - YF["skew"]) < 1e-9)
    ok = skew_ok and rc_ok and settle_clean
    check(f"{tag} {label}", ok,
          f"skew={got['skew']!r} (want {expect_skew}*) · basis={got.get('basis')!r} "
          f"· rc={rc} (want {expect_rc}) · no-Yahoo-under-SETTLE={settle_clean}")
    return ok


def suite(mod, tag: str) -> list[bool]:
    out = []
    print(f"\n[1] CBOE returns HTTP 503 for SKEW — transport failure")
    out.append(assert_case(mod, "503", "verified 151.58 preserved, run exits 2",
                           dict(SETTLE_ROW), expect_skew="151.58", expect_rc=2, tag=tag))

    print(f"\n[2] CBOE returns HTTP 200 whose body is HTML — parse failure")
    out.append(assert_case(mod, "html", "verified 151.58 preserved, run exits 2",
                           dict(SETTLE_ROW), expect_skew="151.58", expect_rc=2, tag=tag))

    print(f"\n[3] CBOE returns a VALID CSV that lacks 2026-09-04 — destination gate")
    out.append(assert_case(mod, "missing_date",
                           "verified 151.58 preserved (no fallback overwrite)",
                           dict(SETTLE_ROW), expect_skew="151.58", expect_rc=0, tag=tag))

    print(f"\n[4] CONTROL — CBOE valid and complete; the pass must be inert")
    out.append(assert_case(mod, "good", "151.58 unchanged, run exits 0",
                           dict(SETTLE_ROW), expect_skew="151.58", expect_rc=0, tag=tag))
    return out


def fill_path_case(mod, tag: str) -> bool:
    """[5] The FILL route the first four cases cannot reach.

    A row that is NOT SETTLE with a BLANK skew cell, where CBOE answers validly
    but publishes no 9/4 skew. yfinance may legitimately fill the blank — and the
    row must NOT then be stamped SETTLE, because it now holds a mirror value.
    The whole-run `not failed` guard cannot see this: nothing failed.
    """
    print(f"\n[5] Provisional FILL into a blank cell must BLOCK the SETTLE stamp")
    row = dict(SETTLE_ROW)
    row["skew"] = ""
    row["basis"] = ""
    rc, led, _ = run_case(mod, "missing_date", row)
    got = led[TARGET]
    filled = abs(float(got["skew"] or 0) - YF["skew"]) < 1e-9
    not_settle = str(got.get("basis", "")).strip().upper() != "SETTLE"
    ok = filled and not_settle and rc == 0
    check(f"{tag} blank filled provisionally, row NOT stamped SETTLE", ok,
          f"skew={got['skew']!r} basis={got.get('basis')!r} rc={rc} "
          f"(filled={filled} not_settle={not_settle})")
    return ok


# ⚠️ AN IMMUTABLE REV, NOT `HEAD`. The 2nd-pass version of this loader read
# `HEAD:...backfill.py`, which was the pre-fix file AT THE MOMENT I RAN IT and
# became the FIXED file the instant I committed. Codex's next run therefore
# compared fixed code against fixed code and reported 6 passed / 3 failed.
# 🔑 A BASELINE THAT MOVES IS NOT A BASELINE. The experiment was sound and its
# committed reproduction mechanism was broken by the very commit that shipped it
# — a test whose correctness depends on WHEN you run it relative to your own
# commit. Pin the revision; `1e8ae5d00` is the 3-route fix, so `^` is pre-fix.
# (Independently confirmed by Codex against `1e8ae5d00^`: cases 2/3/5 fail,
# 1/4 pass — exactly the intended result.)
# ⚠️ THIS BASELINE IS PERMANENT. Do NOT move it forward when backfill.py is
# refactored. It is the HISTORICAL REGRESSION REFERENCE — the last revision that
# still exhibits the three fail-open routes — and the whole value of --falsify is
# the CONTRAST between it and current code. A newer baseline silently erases that
# contrast: the suite would still print green while comparing fixed against
# fixed, which is exactly the failure that broke the first version of this file.
# If a future refactor stops this revision importing, ADAPT THE HARNESS (shim the
# import, pin a vendored copy) — never re-point the baseline.
PREFIX_REV = "1e8ae5d00^"


def two_run_and_recovery(mod, tag: str) -> list[bool]:
    """[6][7] The SECOND RUN, and the recovery that must still be allowed.

    Codex 3rd pass: the 2nd-pass safeguard remembered provisional writes only for
    the current run. On run 2 the provisional cell is on disk, the destination
    gate correctly PRESERVES it, so nothing new is recorded — and the stamp then
    only asked whether CBOE had `vix`. Run 1 left basis blank; run 2 stamped
    SETTLE over the mirror value. A guard whose memory is shorter than the state
    it guards fails on the second run.

    [7] is the negative control that keeps the fix from being merely restrictive:
    once CBOE supplies SKEW, its value must REPLACE the provisional one and the
    row must be allowed to settle. A guard that never lets anything settle would
    pass [6] and be useless.
    """
    out = []
    print(f"\n[6] TWO RUNS, identical responses — the stamp must NOT appear on run 2")
    row = dict(SETTLE_ROW); row["skew"] = ""; row["basis"] = ""
    with tempfile.TemporaryDirectory() as td:
        led = Path(td) / "VX_DAILY.tsv"
        write_ledger(led, row)
        old_log, old_get = mod.DAILY_LOG, mod.requests.get
        mod.DAILY_LOG = led
        mod.requests.get = make_requests_stub(mod, "missing_date")
        seen = []
        try:
            for _ in range(2):
                with redirect_stdout(io.StringIO()):
                    rc = mod.main(["--spot-only"])
                g = read_ledger(led)["2026-09-04"]
                seen.append((str(g["skew"]), str(g.get("basis", "")).strip().upper(), rc))
        finally:
            mod.DAILY_LOG, mod.requests.get = old_log, old_get
    ok = all(b != "SETTLE" for _, b, _ in seen)
    out.append(ok)
    check(f"{tag} provisional 149.00 never acquires SETTLE across two runs", ok,
          f"run1={seen[0]} run2={seen[1]}")

    print(f"\n[7] RECOVERY CONTROL — when CBOE supplies SKEW, it replaces the "
          f"provisional value and the row MAY settle")
    row = dict(SETTLE_ROW); row["skew"] = ""; row["basis"] = ""
    with tempfile.TemporaryDirectory() as td:
        led = Path(td) / "VX_DAILY.tsv"
        write_ledger(led, row)
        old_log, old_get = mod.DAILY_LOG, mod.requests.get
        mod.DAILY_LOG = led
        try:
            mod.requests.get = make_requests_stub(mod, "missing_date")
            with redirect_stdout(io.StringIO()):
                mod.main(["--spot-only"])
            mod.requests.get = make_requests_stub(mod, "good")   # CBOE catches up
            with redirect_stdout(io.StringIO()):
                rc = mod.main(["--spot-only"])
            g = read_ledger(led)["2026-09-04"]
        finally:
            mod.DAILY_LOG, mod.requests.get = old_log, old_get
    replaced = abs(float(g["skew"]) - 151.58) < 1e-9
    settled = str(g.get("basis", "")).strip().upper() == "SETTLE"
    ok2 = replaced and settled and rc == 0
    out.append(ok2)
    check(f"{tag} CBOE's 151.58 replaces the provisional value and the row settles", ok2,
          f"skew={g['skew']!r} basis={g.get('basis')!r} rc={rc} "
          f"(replaced={replaced} settled={settled})")
    return out


def load_head_module():
    """The PRE-FIX backfill.py from a PINNED rev, imported side-by-side."""
    root = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                          capture_output=True, text=True, check=True).stdout.strip()
    src = subprocess.run(["git", "show", f"{PREFIX_REV}:AGENTS/VIOLET/scripts/backfill.py"],
                         capture_output=True, text=True, check=True, cwd=root).stdout
    tmp = Path(tempfile.mkdtemp()) / "backfill_head.py"
    tmp.write_text(src)
    spec = importlib.util.spec_from_file_location("backfill_head", tmp)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    install_yfinance_stub()
    import backfill

    print("=" * 70)
    print("  END-TO-END — the ACTUAL program path, only the network stubbed")
    print("=" * 70)
    suite(backfill, "FIXED:")
    fill_path_case(backfill, "FIXED:")
    two_run_and_recovery(backfill, "FIXED:")

    if "--falsify" in sys.argv:
        print("\n" + "=" * 70)
        print(f"  FALSIFICATION — the same cases against PRE-FIX backfill.py ({PREFIX_REV})")
        print("  A guard whose failure path has never been RUN is an assumption.")
        print("=" * 70)
        head = load_head_module()
        global EXPECT_FAILURES
        EXPECT_FAILURES = True
        got = (suite(head, "PRE-FIX:") + [fill_path_case(head, "PRE-FIX:")]
               + two_run_and_recovery(head, "PRE-FIX:"))
        EXPECT_FAILURES = False
        # Cases 1 and 4 were already closed by WQ-188 ①, so they SHOULD pass at HEAD.
        # Cases 2, 3 and 5 are what this fix adds and MUST fail at HEAD.
        must_fail = {1: got[1], 2: got[2], 4: got[4]}
        for i, passed in must_fail.items():
            check(f"FALSIFIED: case [{i + 1}] FAILS against pre-fix code", not passed,
                  "the test can distinguish fixed from unfixed"
                  if not passed else "⚠️ test is blind — it passes without the fix")
        check("FALSIFIED: case [6] (two-run stamp) FAILS against pre-fix code",
              not got[5], "the 3rd-pass defect is reproduced by the pinned baseline")
        check("FALSIFIED: cases [1] and [4] still pass pre-fix (WQ-188 ① held)",
              got[0] and got[3], "the new suite does not simply fail everything")

    print("\n" + "=" * 70)
    print(f"  {len(PASSES)} passed · {len(FAILS)} FAILED")
    for f in FAILS:
        print(f"  ❌ {f}")
    print("=" * 70)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
