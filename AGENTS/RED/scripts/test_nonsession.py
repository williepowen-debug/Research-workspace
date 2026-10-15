"""Tests for nonsession.py (S52 P1, Will-approved 2026-10-14). Run: python3 AGENTS/RED/scripts/test_nonsession.py"""
from datetime import date
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from nonsession import is_nonsession, drop_nonsessions, bond_extra_closures, us_market_holidays

fails = 0
def check(name, got, want):
    global fails
    ok = got == want
    fails += (not ok)
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else f"  got={got!r} want={want!r}"))

# the measured cases that motivated the rule
check("Columbus 2026-10-12 is a BOND non-session", is_nonsession("BAMLH0A0HYM2", date(2026, 10, 12)), True)
check("Columbus 2026-10-12 is NOT an NYSE non-session (VIXCLS real)", is_nonsession("VIXCLS", date(2026, 10, 12)), False)
check("Labor Day 2026-09-07 is a non-session for ICE", is_nonsession("BAMLH0A3HYC", date(2026, 9, 7)), True)
check("Labor Day 2026-09-07 is a non-session for VIXCLS", is_nonsession("VIXCLS", "2026-09-07"), True)
check("Veterans Day 2025-11-11 (Tue) bond non-session", is_nonsession("BAMLH0A3HYC", date(2025, 11, 11)), True)
check("Veterans Day 2026-11-11 (Wed) bond non-session", is_nonsession("BAMLH0A0HYM2", date(2026, 11, 11)), True)
check("Veterans Day 2029-11-11 (Sun) observed Mon 11-12", date(2029, 11, 12) in bond_extra_closures(2029), True)
check("ordinary Tue 2026-10-13 is a session", is_nonsession("BAMLH0A0HYM2", date(2026, 10, 13)), False)
check("weekend is a non-session", is_nonsession("VIXCLS", date(2026, 10, 10)), True)
check("undeclared series never filtered", is_nonsession("T5YIFR", date(2026, 10, 12)), False)
check("Thanksgiving 2026-11-26 in NYSE calendar", date(2026, 11, 26) in us_market_holidays(2026), True)
# the counter behaviour: a forward-filled holiday bar must not become a second observation
obs = [{"date": "2026-11-12", "value": "3.25"}, {"date": "2026-11-11", "value": "3.22"},
       {"date": "2026-11-10", "value": "3.22"}, {"date": "2026-11-09", "value": "3.10"}]
kept = [o["date"] for o in drop_nonsessions("BAMLH0A0HYM2", obs)]
check("11/11 forward-fill dropped; 11/12 then 11/10 adjacent", kept, ["2026-11-12", "2026-11-10", "2026-11-09"])
check("undeclared series list unchanged", len(drop_nonsessions("DGS30", obs)), 4)
print(f"\n{'ALL PASS' if not fails else str(fails) + ' FAIL'}")
sys.exit(1 if fails else 0)
