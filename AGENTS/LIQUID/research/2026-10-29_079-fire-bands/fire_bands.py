#!/usr/bin/env python3
"""GATE-LIQ-079 FIRE-leg band + base-rate census (DOCKET L261, LIQUID 2026-10-29).
PROPOSAL INPUT ONLY: computes nothing the gate grades; bands are Will's word.
Reuses fp_backtest_079.py's FRED pull and its +/-2 business-day calendar rule (weekday business days,
holidays not removed — the historical approximation that script already used).
Run: .venv/bin/python3 AGENTS/LIQUID/research/2026-10-29_079-fire-bands/fire_bands.py
"""
import sys, os, datetime as dt, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))
import fp_backtest_079 as fb

S = {k: fb.fred(k) for k in ["SOFR99", "SOFR1", "IORB", "IOER", "EFFR", "EFFR75", "EFFR99", "RPONTTLD", "DFEDTARU"]}
ceil = {d: v for d, v in S["IOER"].items() if d < "2021-07-29"}
ceil.update(S["IORB"])
days = [d for d in sorted(S["SOFR99"]) if d in ceil]
cal = fb.calendar_dates(sorted({int(d[:4]) for d in days}))
noncal = {d for d in days if dt.date.fromisoformat(d) not in cal}
bp = lambda a, b: round((a - b) * 100)
arm_sp = {d: bp(S["SOFR99"][d], ceil[d]) for d in days}

# ARM (letter): >=+30, non-calendar, >=2 consecutive publication days; a calendar day between breaks
armed, run = set(), []
for d in days:
    if d in noncal and arm_sp[d] >= 30:
        run.append(d)
        if len(run) >= 2:
            armed.add(d)
    else:
        run = []
def episodes(ds, gap=5):
    ds = sorted(ds); out = []
    for d in ds:
        if out and (dt.date.fromisoformat(d) - dt.date.fromisoformat(out[-1][-1])).days <= gap:
            out[-1].append(d)
        else:
            out.append([d])
    return out
arm_eps = episodes(armed)
print(f"history {days[0]} -> {days[-1]}: {len(days)} SOFR days, {len(noncal)} non-calendar")
print(f"ARMED days (letter rule) {len(armed)}; episodes {[(e[0], e[-1], len(e), max(arm_sp[x] for x in e)) for e in arm_eps]}")

# candidate legs
def eff_ceiling(d): return bp(S["EFFR"][d], ceil[d]) if d in S["EFFR"] else None
def eff75(d): return bp(S["EFFR75"][d], ceil[d]) if d in S["EFFR75"] else None
def eff99(d): return bp(S["EFFR99"][d], ceil[d]) if d in S["EFFR99"] else None
def disp(d): return bp(S["SOFR99"][d], S["SOFR1"][d]) if d in S["SOFR1"] else None
def srf(d): return S["RPONTTLD"].get(d)
idx = {d: i for i, d in enumerate(days)}
def chg10(f, d):
    i = idx[d]
    if i < 10: return None
    a, b = f(d), f(days[i - 10])
    return None if a is None or b is None else a - b

cands = [
    ("3a EFFR-IORB >= 0bp (level)", lambda d: eff_ceiling(d) is not None and eff_ceiling(d) >= 0),
    ("3a' EFFR-IORB 10-day change >= +3bp", lambda d: (chg10(eff_ceiling, d) or -99) >= 3),
    ("3a'' EFFR-IORB 10-day change >= +5bp", lambda d: (chg10(eff_ceiling, d) or -99) >= 5),
    ("3b EFFR75-IORB > 0bp", lambda d: eff75(d) is not None and eff75(d) > 0),
    ("3b' EFFR99-IORB >= +10bp", lambda d: eff99(d) is not None and eff99(d) >= 10),
    ("4a SOFR99-SOFR1 >= 20bp", lambda d: disp(d) is not None and disp(d) >= 20),
    ("4a' SOFR99-SOFR1 >= 30bp", lambda d: disp(d) is not None and disp(d) >= 30),
    ("4a'' SOFR99-SOFR1 >= 50bp", lambda d: disp(d) is not None and disp(d) >= 50),
    ("4b repo ops (RPONTTLD) >= $1B", lambda d: (srf(d) or 0) >= 1.0),
    ("4b' repo ops (RPONTTLD) >= $10B", lambda d: (srf(d) or 0) >= 10.0),
]
TP = [d for d in days if "2019-09-16" <= d <= "2019-09-25"]
res = []
print(f"\n{'candidate':42} {'noncal days met':>18} {'ARMED days met':>15} {'ARM eps met':>12}  TP 2019-09-16..25 days met")
for name, f in cands:
    nc = [d for d in noncal if f(d)]
    am = [d for d in armed if f(d)]
    em = sum(1 for e in arm_eps if any(f(x) for x in e))
    tp = [d for d in TP if f(d)]
    recent = [d for d in noncal if d >= "2025-08-14" and f(d)]
    print(f"{name:42} {len(nc):>5}/{len(noncal)} ({100*len(nc)/len(noncal):4.1f}%) {len(am):>5}/{len(armed):<5} {em:>5}/{len(arm_eps):<5}  {len(tp)}/{len(TP)} {tp[:3]}  | since 2025-08-14 noncal: {len(recent)}")
    res.append(dict(name=name, noncal=len(nc), noncal_n=len(noncal), armed=len(am), armed_n=len(armed), eps=em, eps_n=len(arm_eps), tp=len(tp), tp_n=len(TP), recent=len(recent)))
# joint FIRE candidate: ARMED & 3a(level) or 3b ; & 4a' or 4b
def leg3(d): return cands[0][1](d) or cands[3][1](d)
def leg4(d): return cands[6][1](d) or cands[8][1](d)
fire = sorted(d for d in armed if leg3(d) and leg4(d))
print(f"\nJOINT (proposal): ARMED & (3a or 3b) & (4a' or 4b) -> {len(fire)} days, episodes {[(e[0], e[-1], len(e)) for e in episodes(fire)]}")
print("TP daily detail (SOFR99-ceil, EFFR-ceil, EFFR75-ceil, EFFR99-ceil, SOFR99-SOFR1, repo ops $B):")
for d in TP + [x for e in arm_eps for x in e if x not in TP]:
    print(" ", d, "noncal" if d in noncal else "CAL", arm_sp[d], eff_ceiling(d), eff75(d), eff99(d), disp(d), srf(d))
last = days[-12:]
print("latest:", [(d, arm_sp[d], eff_ceiling(d), eff75(d), eff99(d), disp(d), srf(d)) for d in last])
print("DFEDTARU latest:", sorted(S["DFEDTARU"].items())[-3:], "IORB latest:", sorted(S["IORB"].items())[-3:])
json.dump(dict(res=res, armed_eps=[(e[0], e[-1], len(e)) for e in arm_eps], fire=fire, history=[days[0], days[-1]]),
          open(os.path.join(HERE, "fire_bands_result.json"), "w"), indent=1)
