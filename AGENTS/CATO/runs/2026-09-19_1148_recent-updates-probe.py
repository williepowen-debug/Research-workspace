#!/usr/bin/env python3
"""Pinned, offline review counterexamples. PASS reproduces behavior, not a repair."""
import contextlib
import datetime as dt
import io
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import types
from unittest.mock import patch

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
REV = "1b148338809bedc4de7a0e1f1c78c34273964ae1"
SOURCE = sys.argv[1] if len(sys.argv) > 1 else REV
print("SOURCE", SOURCE)

def module(path):
    m = types.ModuleType("cato_probe_" + Path(path).stem)
    m.__file__ = str(ROOT / path)
    src = ((ROOT / path).read_bytes() if SOURCE == "WORKTREE" else
           subprocess.check_output(["git", "show", SOURCE + ":" + path], cwd=ROOT))
    print("MODULE", path, "sha256", hashlib.sha256(src).hexdigest())
    exec(compile(src, m.__file__, "exec"), m.__dict__)
    return m

f = module("AGENTS/HANS/scripts/fetch_eu.py")
f._agsi_key = lambda: "offline-fixture-not-a-key"
values = {2021:71.26, 2022:85.67, 2023:93.87, 2024:93.38, 2025:81.09}

def norm_case(label, omit=(), wrong_date=False, nan=False):
    def fake_open(req, timeout):
        day = req.full_url.split("date=")[1]
        year = int(day[:4])
        rows = [] if year in omit else [{"full": "NaN" if nan else values[year],
            "gasDayStart": "2020-01-01" if wrong_date else day, "code":"EU"}]
        return io.StringIO(json.dumps({"data":rows}))
    with patch.object(f.urllib.request, "urlopen", fake_open):
        result = f.agsi_norm("2026-09-17")
        with patch.object(f, "ecb", lambda *a: []), patch.object(f, "agsi_eu", lambda: (("2026-09-17",69.06,"0"),None)):
            rendered = io.StringIO()
            with contextlib.redirect_stdout(rendered):
                state = f.main()
    print("RENDER", [line.strip() for line in rendered.getvalue().splitlines()
                      if "GAP TO" in line or "NO GAP REPORTED" in line])
    print("STORAGE", [o for o in state["observations"] if o[0] == "HANS-T-08"],
          "breach", "HANS-T-08" in state["breached"],
          "failure", any("AGSI" in err for err in state["failures"]))
    mean, median, n, meta = result
    gap = None if mean is None else 69.06 - mean
    band = "UNKNOWN" if gap is None else "RED" if gap <= -25 else "ORANGE" if gap <= -15 else "GREEN"
    print(label, "years=", n, "mean=", mean, "gap=", gap, "band=", band)
    return result

healthy = norm_case("complete_five_year_control")
partial = norm_case("missing_2023", omit=(2023,))
assert healthy[2] == 5 and 69.06 - healthy[0] <= -15
assert partial[2] == 4 and 69.06 - partial[0] > -15
assert norm_case("missing_two_years_control", omit=(2023,2024))[0] is None
assert norm_case("wrong_dates_all_five", wrong_date=True)[2] == 5
assert math.isnan(norm_case("nonfinite_all_five", nan=True)[0])

c = module("AGENTS/HANS/scripts/closeout_check.py")
for bad_rc in (1, 2, -15):
    def fake_run(cmd, cwd):
        is_advisory = any(x.endswith(("consumer_check.py", "ledger_staleness.py")) for x in cmd)
        return (bad_rc, "simulated process failure") if is_advisory else (0, "control passed")
    c.run = fake_run
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        rc = c.main()
    lines = [s.strip() for s in out.getvalue().splitlines()
             if "MECHANICAL:" in s or "EXIT 0" in s]
    print("closeout_three_process_errors", bad_rc, "runner_rc=", rc, lines)
    assert rc == 0

assert dt.date(2026,7,31).strftime("%A") == "Friday"
assert dt.date(2026,8,3).strftime("%A") == "Monday"
print("SAM chronology: July 31 Friday -> August 3 Monday, next weekday/session, not second session")
print("net/gross counterexample: assets=1000, NBFI funding=150, NBFI loans=100;")
print("net NBFI debtor=50, 20% loan impairment=20 loss; net borrowing does not remove gross credit risk")
print("PASS: historical behaviors reproduced; no owner file or live network touched")
