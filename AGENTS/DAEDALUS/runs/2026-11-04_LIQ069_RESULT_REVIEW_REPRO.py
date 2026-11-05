import sys, importlib.util
import numpy as np
from fractions import Fraction as Fr
s = importlib.util.spec_from_file_location("g", "AGENTS/LIQUID/scripts/gate069_legs.py")
g = importlib.util.module_from_spec(s); s.loader.exec_module(g)
a, b = "2026-10-29", "2026-10-30"; hy = {a: 326, b: 331}
def norm(x, dp): return round(float(np.float32(x)), dp)   # candidate line 257 is dp=2
for t, p, c in (("CRWV", "54.235", "46.10"), ("NBIS", "237.355", "201.75")):
    truth = "FIRED" if Fr(c) <= Fr(p) * Fr(85, 100) else "NOT FIRED"
    res = {}
    for dp in (2, 4):
        eq = {x: {a: 50.0, b: 50.0} for x in g.TICK}
        eq[t] = {a: norm(p, dp), b: norm(c, dp)}
        res[dp] = g.grade_l4(hy, eq)["state"]
    print(t, p, "->", c, f"exact {float((Fr(c)/Fr(p)-1)*100):+.5f}%", "truth", truth, "| 2dp", res[2], "| 4dp", res[4])
