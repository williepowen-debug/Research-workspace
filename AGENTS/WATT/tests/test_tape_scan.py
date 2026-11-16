#!/usr/bin/env python3
"""Offline tests for AGENTS/WATT/tape_scan.py against saved DM2 / EIA-930 payloads.

Run from anywhere:  .venv/bin/python3 AGENTS/WATT/tests/test_tape_scan.py
Each case names the acceptance condition it shows
(proposals/2026-11-16_TAPE_SCAN_ACCEPTANCE.md). No network call is made.
"""
import io
import json
import sys
import tempfile
import urllib.error
from contextlib import redirect_stdout
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import tape_scan as ts  # noqa: E402

SRC = HERE / "sources"
UNV = SRC / "2026-10-29" / "dm2-fivemin-1023-1029.json"
VER = SRC / "2026-11-05" / "dm2-fivemin-verified-1023-1027.json"
DEM = SRC / "2026-10-29" / "eia930-pjm-demand-0901-1028-2026.json"
UTC = timezone.utc


def t(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M").replace(tzinfo=ts.EPT).astimezone(UTC)


class Args:
    def __init__(self, unv=UNV, ver=VER, dem=DEM, retention=15.0):
        self.replay_unverified, self.replay_verified = str(unv), (str(ver) if ver else None)
        self.replay_demand, self.retention_days = (str(dem) if dem else None), retention


def run(cutoff, now, **kw):
    fetch_fn, demand_fn = ts.replay_fetchers(Args(**kw), t(now))
    calls = []

    def counted(feed, s, e):
        calls.append(feed)
        return fetch_fn(feed, s, e)
    rc, lines = ts.scan(t(cutoff), t(now), counted, demand_fn)
    return rc, "\n".join(lines), calls


RESULTS = []


def check(name, cond, detail=""):
    RESULTS.append((name, bool(cond)))
    print(f"{'PASS' if cond else 'FAIL'}  {name}" + (f"  [{detail}]" if not cond and detail else ""))


# A1/A2 — the replay the brief asks for
rc, out, calls = run("2026-10-24T00:00", "2026-10-28T23:59")
check("A1/A2 replay 10/24-10/28 finds the 10/27 18:50-19:00 run",
      rc == 1 and "RUN 2026-10-27 18:50 to 19:00 EPT, 3 prints" in out
      and "$2,026.73 / $1,970.77 / $2,297.21" in out, out)
check("A2 demand limb matches the 10/29 grade (97.9 / 99.8 / 100.3, MET both)",
      "10-27T22Z 97.9%" in out and "10-27T23Z 99.8%" in out and "10-28T00Z 100.3%" in out
      and "FIRED-ON-LETTER pre-grade" in out, out)
check("A4 at most 2 DM2 calls", len(calls) <= 2, str(calls))

# A1 ordinary quiet window: one call, rc 0
rc, out, calls = run("2026-10-28T01:00", "2026-10-28T23:59")
check("A1 ordinary quiet day: rc 0, one call, null meaning printed",
      rc == 0 and calls == [ts.UNVERIFIED] and "says nothing" in out, f"rc={rc} calls={calls}")

# A4 gap longer than both feeds hold here
rc, out, calls = run("2026-10-10T00:00", "2026-10-28T23:59")
check("A4 long gap: head span UNKNOWN, rc 2, run still reported",
      rc == 2 and "UNKNOWN span 2026-10-09 23:00" in out and "RUN 2026-10-27 18:50" in out
      and calls == [ts.UNVERIFIED, ts.VERIFIED], f"rc={rc} calls={calls}\n{out}")

# A5 cutoff unreadable: no API call, rc 2
now = t("2026-11-16T14:00")
for label, text in [("missing", "no line here"),
                    ("duplicated", "**Tape cutoff (machine-read):** 2026-11-14T11:00 EPT\n"
                                   "**Tape cutoff (machine-read):** 2026-11-13T11:00 EPT"),
                    ("garbage", "**Tape cutoff (machine-read):** November 14 11:00 EPT"),
                    ("future", "**Tape cutoff (machine-read):** 2026-11-17T11:00 EPT")]:
    try:
        ts.read_cutoff(text, now)
        check(f"A5 cutoff {label} raises", False)
    except ts.CutoffError:
        check(f"A5 cutoff {label} raises", True)
with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
    f.write("STATUS without the line\n")
buf = io.StringIO()
with redirect_stdout(buf):
    rc = ts.main(["--status", f.name])
check("A5 main(): unreadable cutoff => rc 2, 'No API call made'",
      rc == 2 and "No API call made" in buf.getvalue(), buf.getvalue())
Path(f.name).unlink()
cut, raw = ts.read_cutoff("x\n**Tape cutoff (machine-read):** 2026-11-14T11:00 EPT (unverified 5-min)\n", now)
check("A5 well-formed cutoff parses to 16:00Z", cut == datetime(2026, 11, 14, 16, 0, tzinfo=UTC), str(cut))

# A6 refusal / rate limit / truncation
for code in (401, 429):
    def refuse(feed, s, e, code=code):
        raise urllib.error.HTTPError("u", code, "refused", {}, None)
    rc, lines = ts.scan(t("2026-10-27T00:00"), t("2026-10-28T00:00"), refuse, lambda h: [])
    out = "\n".join(lines)
    check(f"A6 HTTP {code} => rc 2 UNKNOWN, never clean",
          rc == 2 and "UNKNOWN span" in out and "0 price-limb runs" not in out, out)
rc, lines = ts.scan(t("2026-10-27T00:00"), t("2026-10-28T00:00"),
                    lambda f, s, e: {"items": [], "totalRows": 288}, lambda h: [])
check("A6 silent truncation (totalRows > rows) => rc 2", rc == 2 and "truncation" in "\n".join(lines))

# A7 fire straddling the cutoff, beginning before the scan start, and still running
rc, out, _ = run("2026-10-27T18:55", "2026-10-27T23:59")
check("A7 run straddling the cutoff is found whole and labelled",
      rc == 1 and "RUN 2026-10-27 18:50 to 19:00" in out and "STRADDLES THE CUTOFF" in out, out)
rc, out, _ = run("2026-10-27T19:55", "2026-10-27T23:59")
check("A7 run already under way at the scan start is labelled",
      "BEGAN AT OR BEFORE SCAN START" in out and "RUN 2026-10-27 18:55 to 19:00" in out, out)
rc, out, _ = run("2026-10-27T12:00", "2026-10-27T19:02")
check("A7 run including the latest print is labelled RUNNING",
      rc == 1 and "RUNNING AT LATEST PRINT" in out, out)

# A8 a missing stamp inside the run
d = json.load(open(UNV))
d["items"] = [r for r in d["items"] if r["datetime_beginning_ept"] != "2026-10-27T18:55:00"]
holed = Path(tempfile.mkstemp(suffix=".json")[1])
holed.write_text(json.dumps(d))
rc, out, calls = run("2026-10-27T12:00", "2026-10-27T23:59", unv=holed)
check("A8 hole beside $1,000 prints is filled from the verified feed (call 2)",
      rc == 1 and calls == [ts.UNVERIFIED, ts.VERIFIED] and "RUN 2026-10-27 18:50 to 19:00" in out
      and "unverified/verified" in out, out)
rc, out, calls = run("2026-10-27T12:00", "2026-10-27T23:59", unv=holed, ver=None)
check("A8 same hole with the verified call failing => edge prints REVIEW + UNKNOWN span, rc 2",
      rc == 2 and "NEIGHBOUR INTERVAL MISSING" in out and "UNKNOWN span 2026-10-27 18:55" in out
      and "ALSO REVIEW" in out, out)
holed.unlink()

# A8 stale tail
rc, out, _ = run("2026-10-29T00:00", "2026-10-29T23:59")
check("A8 tape ending >60 min before now => tail UNKNOWN, rc 2",
      rc == 2 and "UNKNOWN span 2026-10-29 13:30" in out, out)

# demand source failing does not hide the run
rc, out, _ = run("2026-10-27T12:00", "2026-10-27T23:59", dem=None)
check("A2 demand fetch failing => run still REVIEW, demand limb UNKNOWN",
      rc == 1 and "demand limb UNKNOWN" in out and "PRICE LIMB ONLY (demand UNKNOWN)" in out, out)

# A3 levels are imported, not retyped
src = (HERE / "tape_scan.py").read_text()
check("A3 no $1,000 / $500 literal in tape_scan.py logic",
      "1000.0" not in src and "500.0" not in src and "from power_watch import LMP_ORANGE, LMP_RED" in src)

n_fail = sum(1 for _, ok in RESULTS if not ok)
print(f"\n{len(RESULTS) - n_fail} of {len(RESULTS)} checks passed")
sys.exit(1 if n_fail else 0)
