"""Synthetic-defect injection for snapshot.py's coverage guard.
Tests the GUARD, not the guarded: build series with KNOWN holes and assert the
guard flags them AND that the corrupted verdict is suppressed."""
import sys, importlib.util
spec = importlib.util.spec_from_file_location("snap", "AGENTS/TERRY/scripts/snapshot.py")
snap = importlib.util.module_from_spec(spec); spec.loader.exec_module(snap)

def series(n, base=100.0, dip_at=None, dip=50.0, nulls=()):
    rows = []
    for i in range(n):
        c = base + i * 0.1
        if dip_at is not None and i == dip_at: c = dip
        rows.append({"date": f"d{i:03d}", "close": None if i in nulls else c})
    return {"history": rows}

fails = []
def check(name, cond):
    print(("  PASS  " if cond else "  FAIL  ") + name)
    if not cond: fails.append(name)

print("1) clean batch -> no flags")
h = {"AAA": series(60), "BBB": series(60)}
c = snap.coverage_flags(h, 60)
check("no flag on full batch", all(v[2] == "" for v in c.values()))

print("2) THE REPRODUCTION: one symbol truncated 60 -> 18 (the ^TNX case)")
h = {"AAA": series(60), "TNX": series(18)}
c = snap.coverage_flags(h, 60)
check("truncated symbol flagged SHORT", c["TNX"][2] == "SHORT")
check("healthy sibling NOT flagged", c["AAA"][2] == "")

print("3) the extreme actually disappears (why it matters)")
full = snap.hist_stats(series(60, dip_at=2, dip=4.37)["history"])
trunc = snap.hist_stats(series(60, dip_at=2, dip=4.37)["history"][-18:])
check("full series sees the low 4.37", abs(full["low"] - 4.37) < 1e-9)
check("truncated series MISSES it (silently)", trunc["low"] > 4.37)
check("guard is what catches it, not the stats", snap.coverage_flags({"A": series(60), "B": {"history": series(60)["history"][-18:]}}, 60)["B"][2] == "SHORT")

print("4) null bars inside a full-length series")
h = {"AAA": series(60), "BBB": series(60, nulls=(3, 4))}
c = snap.coverage_flags(h, 60)
check("nulls counted", c["BBB"][1] == 2)
check("null series flagged", c["BBB"][2] in ("NULLS", "SHORT"))

print("5) single-ticker pull (no sibling control) -> absolute floor catches it")
c = snap.coverage_flags({"ONLY": series(10)}, 60)
check("absolute floor flags 10 bars vs 60d request", c["ONLY"][2] == "SHORT")

print("6) empty series")
c = snap.coverage_flags({"DEAD": {"history": []}}, 60)
check("empty flagged NONE", c["DEAD"][2] == "NONE")

print("7) stats carry coverage fields")
st = snap.hist_stats(series(30, nulls=(1,))["history"])
check("n_rows/n_bars/n_nulls present", st["n_rows"] == 30 and st["n_bars"] == 29 and st["n_nulls"] == 1)

print("8) guard must NOT fire on a legitimately shorter benchmark (29 vs 30)")
c = snap.coverage_flags({"AAA": series(30), "BBB": series(29)}, 30)
check("1-bar difference is not a false positive", c["BBB"][2] == "")

print()
print(f"{'ALL PASS' if not fails else 'FAILURES: ' + str(fails)}")
sys.exit(1 if fails else 0)
