"""Backtest of spawn_slate's pre-check: replay daily vintages, compare each ACTIVE row's last class with the row's fate at HEAD."""
import argparse, datetime as dt, re, subprocess, sys, collections
sys.path.insert(0, "PROME/tools"); sys.path.insert(0, "scripts")
import spawn_list as sl, spawn_slate as ss
from docket_view import state_kind
head = sl.read_text("PROME/DOCKET.tsv").split("\n")
d0, d1 = dt.date(2026, 9, 19), dt.date(2026, 10, 1)
last, first_seen, days = {}, {}, 0
d = d0
while d <= d1:
    rev = subprocess.run(["git", "rev-list", "-1", f"--before={d} 23:59", "HEAD"], capture_output=True, text=True).stdout.strip()
    a = argparse.Namespace(horizon=0, as_of=d.isoformat(), docket=f"{rev}:PROME/DOCKET.tsv", gates=f"{rev}:PROME/GATES.tsv",
                           roster=f"{rev}:PROME/ROSTER.md", orch_log=f"{rev}:PROME/state/ORCH_LOG.tsv")
    try:
        body = ss.compose(a, "bt")[2]
    except Exception as e:
        print(d, "FAILED", type(e).__name__, e); d += dt.timedelta(days=1); continue
    days += 1
    vint = sl.read_text(a.docket).split("\n")
    n = 0
    for m in re.finditer(r"`(D:L\d+)` → \*\*([A-Z ]+)\*\*", body):
        key, cls = m.group(1), m.group(2)
        ln = int(key[3:])
        last[key] = (cls, d, vint[ln - 1].split("\t")[0]); first_seen.setdefault(key, d); n += 1
    print(d, "ok", "ACTIVE rows:", n, "conservation:", "OK" if "· OK" in body else "FAILED")
    d += dt.timedelta(days=1)
tab = collections.Counter(); ex = collections.defaultdict(list)
for key, (cls, day, date_cell) in sorted(last.items()):
    c = head[int(key[3:]) - 1].split("\t")
    fate = ("TERMINAL" if state_kind(c[3]) != "PENDING" else "RE-DATED" if c[0] != date_cell else "STILL PENDING, same date")
    tab[(cls, fate)] += 1; ex[(cls, fate)].append(f"{key}@{day:%m/%d}")
print(f"\n{days} daily vintages {d0}..{d1}; {len(last)} distinct DOCKET rows seen ACTIVE; class = the LAST class the row showed; fate = its row at HEAD")
for (cls, fate), n in sorted(tab.items()):
    print(f"{cls:17} {fate:25} {n:3}  {' '.join(ex[(cls, fate)][:12])}")
