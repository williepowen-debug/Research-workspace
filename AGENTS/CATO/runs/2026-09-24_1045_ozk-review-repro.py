"""Pinned, offline CATO checks of OZK's September 24 changes; no owner writes."""
import contextlib
import csv
import io
import json
from pathlib import Path
import subprocess
import sys
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
REV = "e9593591146942a4226dc6bc30fd52f50793a6ca"
BEFORE = "24860a684^"


def source(path, rev=REV):
    return subprocess.check_output(["git", "show", f"{rev}:{path}"], cwd=ROOT, text=True)


def table(path, rev=REV):
    return list(csv.DictReader(
        (line for line in source(path, rev).splitlines() if not line.startswith("#")),
        delimiter="\t"))


watch = {"__name__": "cato_pinned_review"}
exec(compile(source("AGENTS/OZK/scripts/flng_watch.py"), "pinned_flng_watch.py", "exec"), watch)
baseline = watch["BASELINE_ID"]
base = [{"instFlngId": n} for n in range(baseline - 181, baseline + 1)]
cases = [
    ("full_baseline", base, 0),
    ("new_filing", base + [{"instFlngId": baseline + 1}], 1),
    ("empty_list", [], 2),
    ("empty_object", {}, 2),
    ("missing_id", base + [{}], 2),
    ("boolean_id", base + [{"instFlngId": True}], 2),
    ("truncated_with_baseline", base[-20:], 2),
    ("older_window", [{"instFlngId": n} for n in range(10000, 10182)], 2),
]
results = []
for name, rows, expected in cases:
    rc, msg, _ = watch["evaluate"](rows, baseline)
    assert rc == expected, (name, rc, expected)
    results.append({"case": name, "rc": rc, "message": msg})
with patch.object(sys, "argv", ["flng_watch.py"]), patch.object(
    watch["urllib"].request, "urlopen", side_effect=TimeoutError("isolated fixture")
), contextlib.redirect_stdout(io.StringIO()) as captured:
    rc = watch["main"]()
assert rc == 2
results.append({"case": "network_timeout", "rc": rc, "message": captured.getvalue().strip()})

# Advisory, not a claim this malformed response occurred at the FDIC.
duplicate = watch["evaluate"]([{"instFlngId": baseline}] * 182, baseline)
assert duplicate[0] == 0

pred_path = "AGENTS/OZK/workbook/PREDICTIONS.tsv"
old = {r["Pred_ID"]: r for r in table(pred_path, BEFORE)}
new = {r["Pred_ID"]: r for r in table(pred_path)}
assert old.keys() == new.keys()
changed_cells = {key: [col for col in old[key] if old[key][col] != new[key][col]]
                 for key in old if old[key] != new[key]}
assert changed_cells == {"OZK-02": ["Timeframe"], "OZK-03": ["Timeframe"],
                         "OZK-04": ["Timeframe"], "OZK-09": ["Invalidation"]}

# Hypothetical flow witness: ALL departing 30-89 balances cure/pay off;
# different formerly current loans supply the nonaccrual inflow.
series = {r["Quarter_End"]: r for r in table("AGENTS/OZK/workbook/CALL_REPORT_SERIES.tsv")}
q1, q2 = series["2026-03-31"], series["2026-06-30"]
value = lambda row, field: int(row[field])
past_due = "PastDue_30_89_RCON1406_K"
nonaccrual = "Nonaccrual_RCON1403_K"
oreo = "OREO_RCON2150_K"
cures = value(q1, past_due) - value(q2, past_due)
transfer = value(q2, oreo) - value(q1, oreo)
chargeoffs_assumed = value(q2, "NCO_qtr_K")
other_inflow = value(q2, nonaccrual) - value(q1, nonaccrual) + transfer + chargeoffs_assumed
assert value(q1, past_due) - cures == value(q2, past_due)
assert value(q1, nonaccrual) + other_inflow - transfer - chargeoffs_assumed == value(q2, nonaccrual)
assert value(q1, oreo) + transfer == value(q2, oreo)

print(json.dumps({
    "revision": REV, "before": BEFORE, "watcher_checks": results,
    "watcher_duplicate_advisory": {"rc": duplicate[0], "message": duplicate[1]},
    "prediction_changed_cells": changed_cells,
    "OZK03_surviving_invalidation": new["OZK-03"]["Invalidation"],
    "hypothetical_flow_counterexample_K": {
        "30_89_cures_or_payoffs": cures, "30_89_to_nonaccrual": 0,
        "other_current_to_nonaccrual": other_inflow,
        "nonaccrual_to_oreo": transfer,
        "assumed_nonaccrual_chargeoffs": chargeoffs_assumed,
        "all_three_endpoints_reproduce": True,
        "limit": "Hypothetical, not observed loan flows; net charge-offs treated as gross with zero recoveries for this witness."
    },
    "four_boot_files_bytes": {name: len(source(f"AGENTS/OZK/{name}").encode())
                              for name in ["STATUS.md", "MEMORY.md", "LESSONS.md", "CALENDAR.md"]},
}, indent=2))
