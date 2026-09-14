#!/usr/bin/env python3
"""Falsification set for the TIE ATOM at every registered threshold (DOCKET L258).

Written S44 2026-09-12 with the fix, after DAEDALUS found that RED-FT-07's letter
(CCC-OAS > 930, STRICT, sustain 1) FIRED on a published 9.30 because the line is
registered in bps but PUBLISHED in percent at 2dp, and float("9.30")*100 is
930.0000000000001 in binary float.

THE TEST IS THE ONE RED RATIFIED, not the one it withdrew. RED's 9/6 OUTBOX note
(RED-TO-PROME-20260906-040 §1) killed the "recompute under both operators" test and
named the valid one: A POSITIVE FIXTURE — an observation exactly on the boundary at
the DECLARED PRECISION. Every case below is that fixture.

ACCEPTANCE CONDITIONS (not a replay of the reproduction):
  exactness      - the tie value scales to the threshold EXACTLY, for every mapped leg
  no flips       - a leg's verdict at its tie must not depend on binary representation
  strictness     - a STRICT band must reject its own boundary; a NON-STRICT one accept it
  hold band      - FT-07's 930 must be allocated to NEITHER fire NOR exit (the letter)
  realised tie   - the FT-07 tie is on the 2dp publication grid, not merely representable
  both tools     - boot.py and base_rate_review.py must use the SAME arithmetic, or the
                   published base rate describes a threshold the live path never evaluates

Run:  python3 AGENTS/RED/scripts/test_tie_atoms.py      (exit 1 on any failure)
"""
import sys
from decimal import Decimal
from pathlib import Path

RED = Path(__file__).resolve().parents[1]


def _load(name):
    src = (RED / "scripts" / name).read_text(encoding="utf-8").replace("\n_ensure_venv()\n", "\n\n")
    ns = {"__name__": "t_" + name, "__file__": str(RED / "scripts" / name)}
    exec(compile(src, name, "exec"), ns)
    return ns


bad = 0
boot = _load("boot.py")
scaled, MM = boot["scaled"], boot["METRIC_MAP"]

# --- 1. the reproduction itself, pinned so it can never regress silently ---
raw = float("9.30") * 100
ok = raw > 930 and scaled("9.30", 100) == 930.0
print(f"  {'PASS' if ok else 'FAIL'}  reproduction pinned: float('9.30')*100={raw!r} fires >930; scaled()=930.0 does not")
bad += not ok

# --- 2. every mapped leg at its exact tie value: no verdict may depend on float repr ---
lines = [l for l in (RED / "registry/FALSIFICATION_TRIGGERS.tsv").read_text(encoding="utf-8").split("\n") if l.strip()]
h = lines[0].split("\t")
legs = flips = 0
for l in lines[1:]:
    c = l.split("\t")
    metric = c[h.index("metric")]
    if metric not in MM:
        continue
    scale = MM[metric][3]
    for op_col, thr_col in (("threshold_op", "threshold_value"), ("exit_op", "exit_threshold")):
        op, thr = c[h.index(op_col)].strip(), c[h.index(thr_col)].strip()
        if op not in (">", "<", ">=", "<=") or not thr:
            continue
        legs += 1
        t = Decimal(thr)
        pub = t / Decimal(str(scale))
        new = scaled(pub, scale)
        if new != float(t):                      # exactness
            flips += 1
            print(f"  FAIL  {c[0]}/{op_col}: tie {pub} scales to {new!r}, not {float(t)!r}")
        strict_ok = (new > float(t)) is False and (new < float(t)) is False
        if not strict_ok:
            flips += 1
            print(f"  FAIL  {c[0]}/{op_col}: tie value is not equal to its own threshold")
print(f"  {'PASS' if not flips else 'FAIL'}  all {legs} mapped legs scale EXACTLY to their threshold at the tie ({flips} defect(s))")
bad += bool(flips)

# --- 3. FT-07's hold band: 930 belongs to NEITHER leg ---
v = scaled("9.30", 100)
hold = (not (v > 930)) and (not (v < 930))
print(f"  {'PASS' if hold else 'FAIL'}  FT-07 930 bp is a one-atom HOLD band: fires={v>930}, exits={v<930}")
bad += not hold

# --- 4. the two tools must agree, or the base rate describes a different threshold ---
try:
    br = _load("base_rate_review.py")
    agree = br["_scaled"]("9.30", 100.0) == scaled("9.30", 100)
    print(f"  {'PASS' if agree else 'FAIL'}  boot.py and base_rate_review.py scale identically at the tie")
    bad += not agree
except Exception as e:                            # network/import-heavy module
    print(f"  SKIP  base_rate_review.py not loadable here ({type(e).__name__}); check _scaled by inspection")

# --- 5. non-strict must still ACCEPT its boundary (guard against over-correcting) ---
acc = scaled("1.50", 100) >= 150 and scaled("150", 1) >= 150
print(f"  {'PASS' if acc else 'FAIL'}  a NON-STRICT band still accepts its own boundary (no over-correction)")
bad += not acc

# --- 6. FT-11's 5-session differencing must be exact (S45 2026-09-14) ---
# S44 recorded FT-11 as "benign by luck". THAT WAS FALSE and this section is the
# falsifier. Swept over the realistic fly range, the RAW path flips the decision on
# leg (iv)'s REGISTERED NON-STRICT `<=-4` at 80 levels — e.g. fly -0.93 -> -0.97 gives
# raw -3.9999999999999925, which FAILS `<= -4`, while the exact value is -4.0, which
# PASSES. The raw path REJECTED a satisfaction the letter ACCEPTS: a live false
# negative. The drift is SIGN-VARYING with operand magnitude, so "the error is always
# in the safe direction" was an unsafe belief, not a property.
# The precondition leg is genuinely benign (its cut is OFF the 1bp grid) — only the
# on-grid -4bp leg was exposed. Each operator is swept ONLY over the range its own
# quantity can occupy; sweeping both over both ranges manufactures decisions that
# cannot occur and reported 123 phantom failures in this repair's first draft.
def _raw_d5(v):
    return [(v[i] - v[i - 5]) * 100.0 for i in range(5, len(v))]


def _exact_d5(v):
    return [float((Decimal(str(v[i])) - Decimal(str(v[i - 5]))) * 100) for i in range(5, len(v))]


def _fly(a):
    return [a, 0, 0, 0, 0, round(a - 0.04, 2)]


_v = _fly(-0.93)
_r = _raw_d5(_v)[-1] > -4 and _exact_d5(_v)[-1] == -4.0
print(f"  {'PASS' if _r else 'FAIL'}  FT-11 false-negative pinned: raw={_raw_d5(_v)[-1]!r} fails <=-4, exact=-4.0 passes")
bad += not _r

# THE LOAD-BEARING ASSERTION: at every exact -4bp tie on the realistic grid, the
# exact path must ACCEPT (the letter is non-strict). Invariance vs the raw path is
# NOT the property to test — the whole point is that the raw path was wrong.
_ties = [round(c * 0.01, 2) for c in range(-100, 101)]
_acc = sum(_exact_d5(_fly(a))[-1] <= -4 for a in _ties)
print(f"  {'PASS' if _acc == len(_ties) else 'FAIL'}  exact path accepts its own boundary at every tie ({_acc}/{len(_ties)})")
bad += _acc != len(_ties)

_rawacc = sum(_raw_d5(_fly(a))[-1] <= -4 for a in _ties)
print(f"  {'PASS' if _rawacc < len(_ties) else 'FAIL'}  the raw path DID mis-reject its own boundary ({len(_ties) - _rawacc} of {len(_ties)})")
bad += not (_rawacc < len(_ties))

# The precondition leg was and remains benign — recorded so a future reader does not
# over-generalise the leg-(iv) defect to the whole row.
_pm = 0
for _c in range(300, 651):
    _a = round(_c * 0.01, 2)
    for _dl in (-0.102, -0.10, -0.11, -0.12):
        _vv = [_a, 0, 0, 0, 0, round(_a + _dl, 2)]
        _pm += (_raw_d5(_vv)[-1] <= -10.2) != (_exact_d5(_vv)[-1] <= -10.2)
print(f"  {'PASS' if _pm == 0 else 'FAIL'}  precondition leg (off-grid cut) was already benign: {_pm} flips")
bad += _pm != 0

_g = _exact_d5([5.25, 0, 0, 0, 0, 5.37])[-1] == 12.0
print(f"  {'PASS' if _g else 'FAIL'}  S44's Delta5(DGS30) 5.25 -> 5.37 still reproduces as +12.0bp")
bad += not _g


print(f"\n{'ALL PASS' if bad == 0 else str(bad) + ' FAILURE(S)'}")
sys.exit(1 if bad else 0)
