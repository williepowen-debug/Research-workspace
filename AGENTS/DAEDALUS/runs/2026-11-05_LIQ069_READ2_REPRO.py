#!/usr/bin/env python3
"""Read 2 reproduction, Gate 069 L4 line 257 replacement. Run from the repo root: .venv/bin/python -B <this file>
Works only on scratch text of AGENTS/LIQUID/scripts/gate069_legs.py; never writes it. Hold stays in the real file.
Leg 1 proves the selftest passes with the literal old line at the main() call site.
Leg 2 runs main() end to end on hold-removed scratch text, vendor frame in the live form (float64 carrying float32 noise).
Leg 3 re-grades the record with decimals derived without vendor_close, so the oracle can disagree with the read path."""
import contextlib, importlib.util, io, json, os, pathlib, subprocess, sys, tempfile, types
from fractions import Fraction as Fr
import numpy as np, pandas as pd
PATH = pathlib.Path("AGENTS/LIQUID/scripts/gate069_legs.py")
SRC = PATH.read_text()
HOLD = SRC[SRC.index("    # November4 exact-boundary repair"):SRC.index('    sys.path.insert(0, "FORGE/tools/market-data")')]
CALL = "                eq[t] = vendor_closes(px[t])\n"
OLD = "                eq[t] = {d: round(float(v), 2) for d, v in px[t].dropna().items()}\n"
assert SRC.count(CALL) == 1
NOHOLD = SRC.replace(HOLD, "")

print("LEG 1 selftest with the literal old line at the call site")
with tempfile.TemporaryDirectory() as td:
    p = pathlib.Path(td, "m.py"); p.write_text(SRC.replace(CALL, OLD))
    r = subprocess.run([sys.executable, "-B", str(p), "--selftest"], capture_output=True, text=True)
    print("  rc", r.returncode, [l.strip() for l in r.stdout.splitlines() if "SELFTEST" in l])

print("LEG 2 main() end to end, stubbed vendor and FRED")
D = pd.to_datetime(["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-11-02", "2026-11-03"])
ds = [d.strftime("%Y-%m-%d") for d in D]
def frame(name, prior, close):
    cols = {t: [50.0] * 7 for t in ["APLD", "CRWV", "IREN", "NBIS"]}
    cols[name] = [prior] * 6 + [close]
    return {"Close": pd.DataFrame({t: np.array(v, dtype=np.float32).astype(np.float64) for t, v in cols.items()}, index=D)}
def run(code, fr, hy):
    yf = types.ModuleType("yfinance"); yf.download = lambda *a, **k: fr; sys.modules["yfinance"] = yf
    ft = types.ModuleType("fetch")
    ft.fred_fetch = lambda sid, limit=30: ([{"date": d, "value": f"{v / 100:.2f}"} for d, v in zip(ds, hy)]
                                           if sid == "BAMLH0A0HYM2" else [{"date": d, "value": "1.80"} for d in ds])
    sys.modules["fetch"] = ft
    m = types.ModuleType("s"); exec(compile(code, "s.py", "exec"), m.__dict__)
    b = io.StringIO()
    with contextlib.redirect_stdout(b):
        m.main()
    return "NOT FIRED" if "L4 🟢 NOT FIRED" in b.getvalue() else "FIRED" if "L4 🔴 FIRED" in b.getvalue() else "OTHER"
HY5, HY4 = [300] * 6 + [305], [300] * 6 + [304]
cases = [("CRWV 54.235 -> 46.10", "CRWV", 54.235, 46.10, HY5, "NOT FIRED"),
         ("NBIS 237.355 -> 201.75", "NBIS", 237.355, 201.75, HY5, "FIRED"),
         ("APLD 54.30 -> 46.155 tie", "APLD", 54.30, 46.155, HY5, "FIRED"),
         ("APLD 54.30 -> 46.155 tie HY +4", "APLD", 54.30, 46.155, HY4, "NOT FIRED"),
         ("APLD 54.30 -> 46.16", "APLD", 54.30, 46.16, HY5, "NOT FIRED"),
         ("APLD 20.16 -> 17.135 close-side half-cent", "APLD", 20.16, 17.135, HY5, "FIRED")]
for label, code in (("candidate", NOHOLD), ("literal old line", NOHOLD.replace(CALL, OLD))):
    for nm, t, p_, c, hy, want in cases:
        got = run(code, frame(t, p_, c), hy)
        print(f"  {label}: {nm}: want {want}, got {got}{'' if got == want else '  <-- WRONG'}")

print("LEG 3 record re-grade, decimals from the shortest float32 round-trip, integer oracle")
s = importlib.util.spec_from_file_location("g", PATH); g = importlib.util.module_from_spec(s); s.loader.exec_module(g)
E = pathlib.Path("AGENTS/LIQUID/research/2026-11-05_live-catchup")
raw = json.load(open(E / "raw_closes.json"))
hy = {r["date"]: round(float(r["value"]) * 100) for r in json.load(open(E / "BAMLH0A0HYM2.json"))["rows"]}
dec = lambda v: Fr(np.format_float_positional(np.float32(v), unique=True, trim="-"))
cl = {t: {d: v for d, v in raw[t].items() if d <= "2026-11-04"} for t in g.TICK}
print("  closes", sum(map(len, cl.values())), "non-cent", sum((dec(v) * 100).denominator != 1 for t in cl for v in cl[t].values()),
      "vendor_close != independent decimal", sum(Fr(str(g.vendor_close(v))) != dec(v) for t in cl for v in cl[t].values()))
n = dis = 0; fires = []; near = (None, 99)
for d in sorted(hy):
    if d < "2026-09-02" or not g.is_session(d):
        continue
    pv = g.prev_session(d); n += 1
    eq = {t: {k: g.vendor_close(v) for k, v in cl[t].items() if k <= d} for t in g.TICK}
    got = g.grade_l4({d: hy[d], pv: hy[pv]}, eq)["state"]
    hit = any(dec(cl[t][d]) * 100 <= dec(cl[t][pv]) * 85 for t in g.TICK)
    want = "FIRED" if hit and hy[d] - hy[pv] >= 5 else "NOT FIRED"
    dis += got != want
    if want == "FIRED":
        fires.append((d, hy[d] - hy[pv]))
    for t in g.TICK:
        m = float((dec(cl[t][d]) / dec(cl[t][pv]) - 1) * 100)
        if abs(m + 15) < abs(near[1] + 15):
            near = ((t, d), m)
print("  NYSE sessions", n, "disagreements", dis, "fires", fires, "closest name-move to -15", near)
print("  tolerance disclosure: vendor_close(2.040000000001) =", g.vendor_close(2.040000000001), "; vendor_close(2.04004) =", g.vendor_close(2.04004))
