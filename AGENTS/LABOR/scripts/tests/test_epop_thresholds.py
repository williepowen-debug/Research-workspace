#!/usr/bin/env python3
"""
LABOR threshold regression tests — labor_data.py assess().

Run:  .venv/bin/python3 AGENTS/LABOR/scripts/tests/test_epop_thresholds.py
Exit: 0 all pass, 1 any fail.

WHY THIS FILE EXISTS
--------------------
2026-09-07, in one session, the same branch was broken twice and the second
break was introduced BY THE FIX FOR THE FIRST:

  (1) The retired U-3 level bars (>=4.7 / >=5.0, retired 2026-08-07 by BD-15)
      were still firing into the rc=2 path, while EMRATIO -- the LIVE trigger
      gauge since that date -- was not fetched at all.

  (2) The repair compared float differences to exact boundaries. Binary float
      makes that VALUE-DEPENDENT:
          59.1 - 59.4 = -0.29999999999999716  -> <= -0.3 FALSE  (T-03 missed)
          58.9 - 59.2 = -0.30000000000000426  -> <= -0.3 TRUE   (T-03 fires)
      Both display as "-0.3". Eight hand-written guard tests PASSED because the
      chosen fixture landed on the lucky side of the boundary.

The lesson this file encodes: ON A DECIMAL-PUBLISHED SERIES, ONE BOUNDARY
FIXTURE IS A SAMPLE, NOT A PROOF. So the boundary cases below are not a
hand-picked pair -- they are SWEPT across the whole plausible EPOP range.
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import labor_data as L

FAILED = []


def obs(vals):
    return [(f"2026-{max(1, 8 - i):02d}-01", v) for i, v in enumerate(vals)]


def check(name, got, want):
    if got != want:
        FAILED.append(f"{name}: got {got!r}, want {want!r}")
        print(f"  [FAIL] {name}  got={got!r} want={want!r}")
    else:
        print(f"  [pass] {name}")


def epop(now, m3, m6):
    """Build an 8-obs EPOP series with controlled 3-mo and 6-mo referents."""
    v = [now, now, now, m3, m3, m3, m6, m6]
    return L.assess("EMRATIO", "epop", obs(v))


print("\n=== D1 · retired U-3 bars must fire NOTHING (BD-15, 2026-08-07) ===")
for u in (5.0, 4.7, 4.3, 4.1):
    check(f"UNRATE {u}", L.assess("UNRATE", "rate", obs([u, u]))[1], "")

print("\n=== D2 · EPOP exact-boundary sweep — THE REGRESSION THAT SHIPPED ===")
# Sweep the whole boundary class instead of sampling one pair. For every plausible
# current level, a referent exactly 0.3 higher MUST fire T-03, and exactly 0.2
# higher must NOT. Under float subtraction ~half of these fail.
t03_missed, t02_falsefired = [], []
# ⚠️ 2026-09-07: this loop read `range(85, 105)` with `now = i / 10`, i.e. it swept
# 8.5-10.4 while its own comment claimed 58.5-60.4. It passed, and the failure demo
# I published off it printed "missed at EPOP = [8.8, 8.9, 9.3, ...]" -- levels
# impossible for an employment-population ratio -- which I quoted without noticing.
# The measurement was real; the DOMAIN was wrong.
# finding_instrument_reports_clean_against_the_wrong_reference. Caught by CODEX.
for i in range(585, 605):                     # EPOP 58.5 .. 60.4 (tenths, integer)
    now = i / 10
    d, f = epop(now, round(now + 0.3, 1), round(now + 0.3, 1))
    if f != "🟠":
        t03_missed.append((now, f))
    d, f = epop(now, round(now + 0.2, 1), round(now + 0.2, 1))
    if f != "🟢":
        t02_falsefired.append((now, f))
check(f"exactly -0.3 fires T-03 across {20} levels", t03_missed, [])
check(f"exactly -0.2 does NOT fire across {20} levels", t02_falsefired, [])

print("\n=== D2 · CODEX's two reported failing fixtures ===")
check("59.1 / 3m 59.4 / 6m 59.3  -> T-03", epop(59.1, 59.4, 59.3)[1], "🟠")
check("59.1 / 3m 59.4 / 6m 59.6  -> T-04", epop(59.1, 59.4, 59.6)[1], "🔴")

print("\n=== D2 · displayed evidence must agree with the verdict ===")
for now, m3, m6 in [(59.1, 59.4, 59.3), (58.9, 59.2, 59.2), (59.1, 59.4, 59.6)]:
    d, f = epop(now, m3, m6)
    shown_fires = "3m -0.3" in d or "3m -0.4" in d or "3m -0.5" in d
    check(f"disp {d!r} consistent with {f}", shown_fires and f in ("🟠", "🔴"), True)

print("\n=== D2 · conjunction must not relax, T-04 needs BOTH legs ===")
check("6m -0.6 but 3m -0.1 -> no fire", epop(59.1, 59.2, 59.7)[1], "🟢")
check("6m -0.5 exactly + 3m -0.3 exactly -> T-04", epop(59.1, 59.4, 59.6)[1], "🔴")
check("6m -0.4 + 3m -0.3 -> T-03 only", epop(59.1, 59.4, 59.5)[1], "🟠")

print("\n=== D2b · short history is CANNOT-VERIFY, never a green 'no decline' ===")
check("4 obs only", L.assess("EMRATIO", "epop", obs([59.1, 58.9, 59.0, 59.2]))[1], "⚠️")

print("\n=== D3 · live Aug-2026 values reproduce STATUS exactly ===")
d, f = L.assess("EMRATIO", "epop", obs([59.1, 58.9, 59.0, 59.2, 59.1, 59.2, 59.3, 59.4]))
check("live EPOP no fire", f, "🟢")
check("live EPOP disp reproduces STATUS -0.1 / -0.2", ("3m -0.1" in d and "6m -0.2" in d), True)

print("\n=== BD-28(a) · a SINGLE print must not fire a SUSTAINED trigger ===")
# Basis proven from STATUS's own arithmetic, not from its wording:
#   250,000 - 207,250 = 42,750  == "42,750 below T-01 ON MA BASIS"  -> T-01 = MA
#   300,000 - 206,000 = 94,000  == "94K below T-02"                 -> T-02 = single
def claims(sid, v):
    return L.assess(sid, "claims", [("2026-09-05", float(v)), ("2026-08-29", 206000.0)])[1]

# the defect: one band set applied to both series
check("ICSA 260K -> ARM only, NOT a fire", claims("ICSA", 260_000), "🟠")
check("ICSA 300K -> still ARM ('>300K' fires at 301K)", claims("ICSA", 300_000), "🟠")
check("ICSA 301K -> T-02 FIRE", claims("ICSA", 301_000), "🔴")
check("ICSA 250K -> accelerating, not arm", claims("ICSA", 250_000), "🟠")
check("ICSA 229K -> drift", claims("ICSA", 229_000), "🟢")
check("ICSA live 206K -> drift", claims("ICSA", 206_000), "🟢")

check("IC4WSA 251K -> T-01 fires on the MA", claims("IC4WSA", 251_000), "🔴")
check("IC4WSA 250K -> NOT T-01 ('>250K' is strict)", claims("IC4WSA", 250_000), "🟠")
check("IC4WSA 260K -> T-01", claims("IC4WSA", 260_000), "🔴")
check("IC4WSA live 207,250 -> drift", claims("IC4WSA", 207_250), "🟢")

# the conflation itself: at 260K the two series must DISAGREE
check("260K: single ARMs but MA FIRES - bases differ",
      (claims("ICSA", 260_000), claims("IC4WSA", 260_000)), ("🟠", "🔴"))

print("\n=== D4 · null latest value is CANNOT-VERIFY, not a pass ===")
check("newest obs None", L.assess("ICSA", "claims",
      [("2026-09-05", None), ("2026-08-29", 206000.0)])[1], "⚠️")

print("\n=== D5 · epop kind formats as a rate, not a level (CODEX #4) ===")
check("fmt_value epop 59.4", L.fmt_value("epop", 59.4), "59.4%")

print()
if FAILED:
    print(f"{len(FAILED)} FAILED:")
    for f in FAILED:
        print("  -", f)
    sys.exit(1)
print("ALL PASS")
sys.exit(0)
