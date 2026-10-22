"""L546 float-tie test for s8a_relative (DAEDALUS packet 2026-10-08). Run: python3 test_s8a_float_tie.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s8a_relative as m


class _Col:
    def __init__(self, v): self.iloc = v


class _Idx(list):
    pass


class _Day:
    def __init__(self, d): self._d = d
    def date(self): return self._d


class _Frame:
    def __init__(self, cols, n):
        self._c = {k: _Col(v) for k, v in cols.items()}
        self.index = _Idx(_Day(f"d{i}") for i in range(n))
    def __getitem__(self, k): return self._c[k]
    def __len__(self): return len(self.index)


def _rel(t0, t1, b0, b1):
    f = _Frame({"T": [t0, t1], "B": [b0, b1]}, 2)
    return m._rel_series(f, "T", "B", 1)[0][1]


def main():
    fails = 0
    # 1. exact-on-edge: target -10% vs flat base. Raw float (90/100-1)*100 = -9.999999999999998.
    r = _rel(100.0, 90.0, 100.0, 100.0)
    ok = (r == -10.0) and m._state(r) != "RED/FIRED"   # band letter is STRICT '< -10': -10.00 is not a fire
    print(("PASS" if ok else "FAIL"), "edge -10.00 -> not fired:", r, m._state(r)); fails += not ok
    # 2. a difference that floats to just under the edge (-10.000000000000002 class) must round back onto it.
    r = _rel(100.0, 95.0, 100.0, 105.0)   # -5 - 5 = -10 exactly in letter
    ok = (r == -10.0) and m._state(r) != "RED/FIRED"
    print(("PASS" if ok else "FAIL"), "difference edge -10.00 -> not fired:", r, m._state(r)); fails += not ok
    # 3. ordinary: one bp past the edge fires.
    r = _rel(100.0, 89.99, 100.0, 100.0)
    ok = (r == -10.01) and m._state(r) == "RED/FIRED"
    print(("PASS" if ok else "FAIL"), "-10.01 -> fired:", r, m._state(r)); fails += not ok
    # 4. other edges keep their letter (-8 ORANGE edge, strict).
    r = _rel(100.0, 92.0, 100.0, 100.0)
    ok = (r == -8.0) and m._state(r) == "YELLOW"
    print(("PASS" if ok else "FAIL"), "edge -8.00 -> YELLOW (strict):", r, m._state(r)); fails += not ok
    print("FAILS:", fails)
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
