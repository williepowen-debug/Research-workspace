#!/usr/bin/env python3
"""Reproduce comparison of extracted primary-source pairs; does not re-fetch sources.

Input was extracted from web-tool primary page line windows, merged by source
line number. English OIC ranges: 0785 [108,786), 0786 [65,673).
Finance multiline rows end at their final |15, |25 or |50 field.
The JSON retains each source line number, item and rate, and source URLs.
This verifies extraction-output equality, not source authenticity, exemptions,
remission, valuation, registration or tax collection.
"""
import json
from collections import Counter
from pathlib import Path

path = Path(__file__).with_name("2026-09-08_orch-hawk-schedule-census.json")
data = json.loads(path.read_text())
finance, legal = data["finance"], data["legal"]
for name, rows in [("finance", finance), ("legal", legal)]:
    counts = Counter(row["code"] for row in rows)
    assert all(n == 1 for n in counts.values()), (name, "duplicate code")
    assert all(row["rate"] in (15, 25, 50) for row in rows), (name, "invalid rate")
f = {row["code"]: row["rate"] for row in finance}
l = {row["code"]: row["rate"] for row in legal}
assert f == l, {"finance_only": sorted(f.keys()-l.keys()),
                "legal_only": sorted(l.keys()-f.keys()),
                "rate_mismatch": [k for k in f.keys() & l.keys() if f[k] != l[k]]}
print(json.dumps({"commodity_items":len(f),
                  "rates":dict(sorted(Counter(f.values()).items())),
                  "missing_each_direction":0, "rate_mismatches":0,
                  "scope":"commodity item/rate equality only"}))

