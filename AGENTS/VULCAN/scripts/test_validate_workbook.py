#!/usr/bin/env python3
"""Guard falsification for `validate_workbook.py` — offline, and it NEVER touches a real ledger.

WHY THIS FILE EXISTS
--------------------
On 2026-09-06 a CODEX review found that `allowed_values` on any non-`Enum` field was
DOCUMENTATION ONLY. `price_usd` declared `> 0` and accepted -1, 0 and nan; eleven of
thirteen injected defects passed silently. The repair is only worth what its falsification
is worth, so the injections are retained here as a runnable suite instead of living in a
commit message  [[finding_adoption_is_not_validation]].

THE DESIGN DECISION THAT MATTERS
--------------------------------
The first (ad-hoc) harness mutated the REAL ledgers and restored them per case. It had a
defect: it never restored `GPU_SERIES.tsv` between cases, so nine "catches" were actually
measuring a leftover poisoned ledger. A CONTROL case failing is the only reason it surfaced
 [[finding_crosscheck_with_free_parameter_validates_nothing]].

So this suite copies `scripts/`, `workbook/` and `STATUS.md` into a temp tree and runs the
COPIED validator there. The real ledgers are never opened for writing at all — the failure
mode is removed by construction rather than by remembering to clean up. It also means an
interrupted run cannot leave a corrupted append-only ledger behind.

⚠️ EVERY CASE CARRIES ITS OWN CONTROL. A suite of only-negative cases cannot tell
"the guard fired" from "the guard fires on everything".

Run after ANY edit to `validate_workbook.py` or to SCHEMA.tsv's type declarations:
    python3 AGENTS/VULCAN/scripts/test_validate_workbook.py
rc 0 = all cases behaved  ·  rc 1 = at least one case did not
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
AGENT = HERE.parent

# (label, ledger, column, value, must_be_caught)
CASES = [
    # --- GPU_SERIES: the ledger the review was about. Zero rows on disk, so every case
    #     writes a full synthetic row from GOOD below.
    ("gpu tier = BANANA",                    "GPU_SERIES.tsv", "tier",           "BANANA",              True),
    ("gpu tier = on_demand (real)",          "GPU_SERIES.tsv", "tier",           "on_demand",           False),
    ("gpu unit = USD_per_node_month",        "GPU_SERIES.tsv", "unit",           "USD_per_node_month",  True),
    ("gpu gpu_model = BANANA",               "GPU_SERIES.tsv", "gpu_model",      "BANANA",              True),
    ("gpu source_class = BANANA",            "GPU_SERIES.tsv", "source_class",   "BANANA",              True),
    ("gpu instrument = BANANA",              "GPU_SERIES.tsv", "instrument",     "BANANA",              True),
    ("gpu price_basis = BANANA",             "GPU_SERIES.tsv", "price_basis",    "BANANA",              True),
    ("gpu price_basis = term_normalized",    "GPU_SERIES.tsv", "price_basis",    "term_normalized",     False),
    ("gpu price_usd = -1   (declared > 0)",  "GPU_SERIES.tsv", "price_usd",      "-1",                  True),
    ("gpu price_usd = 0    (declared > 0)",  "GPU_SERIES.tsv", "price_usd",      "0",                   True),
    ("gpu price_usd = nan  (parses!)",       "GPU_SERIES.tsv", "price_usd",      "nan",                 True),
    ("gpu price_usd = inf  (parses!)",       "GPU_SERIES.tsv", "price_usd",      "inf",                 True),
    ("gpu price_usd = abc",                  "GPU_SERIES.tsv", "price_usd",      "abc",                 True),
    ("gpu price_usd = 2.53 (real)",          "GPU_SERIES.tsv", "price_usd",      "2.53",                False),
    ("gpu n_observations = 0 (decl >= 1)",   "GPU_SERIES.tsv", "n_observations", "0",                   True),
    ("gpu n_observations = 3.7 (non-int)",   "GPU_SERIES.tsv", "n_observations", "3.7",                 True),
    ("gpu n_observations = 12 (real)",       "GPU_SERIES.tsv", "n_observations", "12",                  False),
    # --- populated ledgers: the defect was never GPU-only.
    ("VX score = 9   (declared 1|2|3|4|5)",  "VX.tsv",         "score",          "9",                   True),
    ("VX score = 3   (real)",                "VX.tsv",         "score",          "3",                   False),
    ("S4 band = BANANA",                     "S4_SERIES.tsv",  "band",           "BANANA",              True),
    ("S4 band = BANANA(paren)",              "S4_SERIES.tsv",  "band",           "BANANA(cum ticked)",  True),
    ("S4 band = no-stress(...)  (real)",     "S4_SERIES.tsv",  "band",           "no-stress(cum 1->2)", False),
    ("S4 band = yellow-decel(...) (real)",   "S4_SERIES.tsv",  "band",           "yellow-decel(x)",     False),
    ("S4 rev_ntd_mn = nan",                  "S4_SERIES.tsv",  "rev_ntd_mn",     "nan",                 True),
    ("EDGAR tick = BANANA",                  "EDGAR_SEEN.tsv", "tick",           "BANANA",              True),
    ("EDGAR tick = NVDA (real)",             "EDGAR_SEEN.tsv", "tick",           "NVDA",                False),
    ("EDGAR channel = S9",                   "EDGAR_SEEN.tsv", "channel",        "S9",                  True),
    ("EDGAR channel = S5/S1 (real)",         "EDGAR_SEEN.tsv", "channel",        "S5/S1",               False),
    ("EDGAR tier = 7  (declared 1|2|3)",     "EDGAR_SEEN.tsv", "tier",           "7",                   True),
    ("LAYER window_days = 44 (1|5|21|63)",   "LAYER_SERIES.tsv", "window_days",  "44",                  True),
    ("LAYER window_days = 63 (real)",        "LAYER_SERIES.tsv", "window_days",  "63",                  False),
]

GOOD_GPU = {
    "asof_utc": "2026-09-11T20:05:00Z", "reading_date": "2026-09-11", "tier": "on_demand",
    "instrument": "rental_index", "vendor": "TestVendor", "gpu_model": "H100_SXM",
    "unit": "USD_per_GPU_hour", "price_usd": "2.53", "n_observations": "12",
    "panel_spec_id": "GPU-PANEL-01", "price_basis": "term_normalized",
    "spread_vs_other_tier_usd": "", "spread_pct": "UNGRADEABLE",
    "source_class": "index_vendor", "source_url": "https://example.test/x",
    "validation": "ok", "notes": "",
}


def build_sandbox(tmp: Path) -> Path:
    """Copy the agent's validator inputs into a temp tree. The copied script resolves
    WB = parents[1]/'workbook' and STATUS at WB.parent, so everything stays inside."""
    (tmp / "scripts").mkdir()
    shutil.copy2(HERE / "validate_workbook.py", tmp / "scripts" / "validate_workbook.py")
    shutil.copytree(AGENT / "workbook", tmp / "workbook")
    shutil.copy2(AGENT / "STATUS.md", tmp / "STATUS.md")
    return tmp / "scripts" / "validate_workbook.py"


def run(script: Path) -> int:
    return subprocess.run([sys.executable, str(script)],
                          capture_output=True, text=True).returncode


def apply_case(tmp: Path, ledger: str, col: str, val: str) -> None:
    """Mutate ONE cell in the sandbox copy. Read/write in BINARY-safe text mode with
    newline='' so a CRLF ledger (EDGAR_SEEN.tsv is the only one) is not silently
    rewritten — a text-mode round-trip rewrote all 5,036 of its append-only rows once."""
    p = tmp / "workbook" / ledger
    with p.open(encoding="utf-8", newline="") as fh:
        raw = fh.read()
    nl = "\r\n" if "\r\n" in raw else "\n"
    lines = raw.replace("\r\n", "\n").rstrip("\n").split("\n")
    hdr = lines[0].split("\t")
    i = hdr.index(col)
    if len(lines) == 1:                       # empty ledger (GPU_SERIES) — synthesize a row
        row = dict(GOOD_GPU)
        row[col] = val
        lines.append("\t".join(row[h] for h in hdr))
    else:
        r = lines[1].split("\t")
        r[i] = val
        lines[1] = "\t".join(r)
    with p.open("w", encoding="utf-8", newline="") as fh:
        fh.write(nl.join(lines) + nl)


def main() -> int:
    print("validate_workbook.py — guard falsification "
          "(sandboxed: real ledgers are never written)\n")
    with tempfile.TemporaryDirectory() as td:
        base = Path(td) / "base"
        base.mkdir()
        script = build_sandbox(base)
        rc0 = run(script)
        print(f"  {'BASELINE — untouched copy must be CLEAN':52} rc={rc0} "
              f"{'✅' if rc0 == 0 else '❌ SANDBOX DIRTY — every result below is void'}")
        if rc0 != 0:
            return 1
        print()
        bad = 0
        for label, ledger, col, val, must_catch in CASES:
            case = Path(td) / "case"
            if case.exists():
                shutil.rmtree(case)
            case.mkdir()
            s = build_sandbox(case)          # FULL clean state per case, by construction
            apply_case(case, ledger, col, val)
            rc = run(s)
            ok = (rc == 2) == must_catch
            bad += not ok
            print(f"  {label:52} rc={rc} {'CATCH' if must_catch else 'PASS ':5} "
                  f"{'✅' if ok else '❌ WRONG'}")
    n_neg = sum(1 for c in CASES if c[4])
    print(f"\n  {len(CASES)} cases — {n_neg} defects injected, "
          f"{len(CASES) - n_neg} real-form controls — WRONG: {bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
