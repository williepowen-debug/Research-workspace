"""Reproduce decisive arithmetic from saved primary-source table extracts."""
from decimal import Decimal as D
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
claims = []


def row(source, table, label):
    tables = json.loads((HERE / f"{source}-tables.json").read_text())
    candidates = []
    for raw in tables[table]["rows"]:
        cells = [c.strip() for c in raw.split("|")]
        cells = [c for c in cells if c]
        if cells and cells[0] == label:
            vals = [D(c.replace(",", "")) for c in cells[1:]
                    if re.fullmatch(r"-?\d[\d,]*(?:\.\d+)?", c)]
            candidates.append((raw, vals))
    assert len(candidates) == 1, (source, table, label, len(candidates))
    raw, vals = candidates[0]
    claims.append({"source": source, "table": table, "label": label,
                   "raw_row": raw, "numeric_cells": [str(x) for x in vals]})
    return vals


wal_nib = row("WAL-release", 10, "Non-interest bearing deposits")
wal_dep = row("WAL-release", 10, "Total deposits")
wal_avg = row("WAL-release", 13, "Non-interest-bearing deposits")
wal_ib = row("WAL-release", 13, "Total interest-bearing deposits")
wal_borrow = row("WAL-release", 10, "Borrowings")
f1 = {
    "period_nib_change_pct": (wal_nib[0] / wal_nib[1] - 1) * 100,
    "period_share_q3_pct": wal_nib[0] / wal_dep[0] * 100,
    "period_share_q2_pct": wal_nib[1] / wal_dep[1] * 100,
    "average_nib_change_pct": (wal_avg[0] / wal_avg[1] - 1) * 100,
    "ib_cost_change_bp": (wal_ib[2] - wal_ib[5]) * 100,
    "total_borrowing_change_pct": (wal_borrow[0] / wal_borrow[1] - 1) * 100,
}
f1["period_share_change_pp"] = f1["period_share_q3_pct"] - f1["period_share_q2_pct"]
assert f1["average_nib_change_pct"] > -5
assert f1["period_nib_change_pct"] < -5 and f1["period_share_change_pp"] < -2
assert f1["ib_cost_change_bp"] == 2

start = row("KEY-release", 34, "Balance at beginning of period")[0]
inflow = row("KEY-release", 34, "Loans placed on nonaccrual status")[0]
# Parentheses encode outflows. Retain sign explicitly when decoding these cells.
key_table = json.loads((HERE / "KEY-release-tables.json").read_text())[34]["rows"]
outflows = {}
for label in ["Charge-offs", "Loans sold", "Payments", "Transfers to OREO", "Loans returned to accrual status"]:
    raw = next(x for x in key_table if x.strip(" | ").startswith(label + " |"))
    value = D(re.search(r"\((\d[\d,]*)\)", raw).group(1).replace(",", ""))
    outflows[label] = value
end = row("KEY-release", 34, "Balance at end of period")[0]
assert start + inflow - sum(outflows.values()) == end == 618

mtb_begin = row("MTB-SEC-release", 16, "Allowance for loan losses")[1]
mtb_end = row("MTB-SEC-release", 16, "Allowance for loan losses")[0]
mtb_provision = row("MTB-SEC-release", 16, "Provision for loan losses")[0]
mtb_nco = row("MTB-SEC-release", 16, "Net charge-offs")[0]
assert mtb_begin + mtb_provision - mtb_nco == mtb_end

results = {"WAL_funding": {k: str(v) for k, v in f1.items()},
           "KEY_NPL_bridge": {"begin": str(start), "inflows": str(inflow),
                              "outflows": {k: str(v) for k, v in outflows.items()}, "end": str(end)},
           "MTB_allowance_bridge": [str(x) for x in [mtb_begin, mtb_provision, mtb_nco, mtb_end]],
           "source_rows": claims,
           "checks": "PASS: WAL F1/F2 arithmetic; KEY NPL flow identity; MTB loan allowance identity",
           "limitations": "Same-source extraction/arithmetic checks, not independent economic evidence; no F3/N inference."}
results["source_hashes"] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in HERE.glob("*-tables.json")}
(HERE / "verification.json").write_text(json.dumps(results, indent=2) + "\n")
print(results["checks"])
print(json.dumps(results["WAL_funding"], indent=2))
