#!/usr/bin/env python3
"""A1-A5 of ACCEPTANCE_presence_reader_contract_2026-09-19.md, plus the four neighbour
categories that contract marked TEST (ordinary · overlap · wrong owner · missing information).
Category 5 (concurrent activity) is a justified N/A there and is deliberately absent."""
import datetime as dt
import io
import json
import subprocess
import sys
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "PROME/tools"))
import session_presence as SP          # noqa: E402
import spawn_list as SL                # noqa: E402

FAILED = []


def check(name, cond, detail=""):
    print(("  ✅ " if cond else "  ❌ ") + name + ("" if cond else f"  — {detail}"))
    if not cond:
        FAILED.append(name)


def fresh_snapshot(host):
    return {"observed_at": dt.datetime.now(dt.timezone.utc).isoformat(), "host": host,
            "coverage": "test", "gaps": None, "error": None,
            "processes": [], "claude": [], "codex": {}}


def run(rows, data, host=None, **kw):
    """`host` is the LOCAL host the check runs on — distinct from data["host"], which is what
    the snapshot CLAIMS. Passing the snapshot's own value makes a foreign snapshot look local
    and silently voids the foreign-host condition (caught by this suite on first run)."""
    buf = io.StringIO()
    with redirect_stdout(buf):
        rc = SP.report(rows, data, host=host or HOST, **kw)
    return rc, buf.getvalue()


HOST = "testhost"
ROW8 = SL.Row("D:L1", "2026-09-19", 0, "TERRY", "ACTIVE", "basis", "cadence", "catalyst")

print("A1 ordinary — runs to completion, one line per due row")
rc, out = run([ROW8], fresh_snapshot(HOST))
check("A1 rc 0 on a clean run", rc == 0, f"rc={rc}")
check("A1 emits the due row", "D:L1\t2026-09-19\tTERRY" in out, out[-200:])

print("A2 producer may gain fields — the reader must not positionally unpack")
class Row9(SL.Row.__mro__[1]):  # plain tuple subclass: a hypothetical 9-field future row
    pass
row9 = tuple(ROW8) + ("future_field",)
rc9, out9 = run([row9], fresh_snapshot(HOST))
check("A2 a 9-field plain tuple does not crash the reader", rc9 == 0, f"rc={rc9}")
check("A2 and still resolves the right owner", "\tTERRY\t" in out9, out9[-200:])
check("A2 producer row is self-describing (named access available)",
      ROW8.owner == "TERRY" and ROW8.cadence == "cadence")

print("A3 a crash must NOT render as the evidence-unavailable verdict")
p = subprocess.run([sys.executable, "-c",
    "import sys; sys.path.insert(0, %r); import session_presence as SP;"
    "SP.main = lambda: (_ for _ in ()).throw(ValueError('boom'));"
    "sys.exit(SP.guarded_main())" % str(ROOT / "PROME/tools")],
    capture_output=True, text=True, cwd=ROOT)
check("A3 a reader crash returns rc=2 (did not look), not rc=1", p.returncode == 2, f"rc={p.returncode}")
check("A3 and says so in words", "CHECK DID NOT RUN" in p.stdout, p.stdout[-200:])
check("A3 disclaims the rc=1 reading BY NAME",
      "'ran, evidence unavailable' (rc=1)" in p.stdout, p.stdout[-200:])
check("A3 ALSO disclaims the rc=2 cannot-certify reading (reader ❌1)",
      "cannot certify its scope" in p.stdout, p.stdout[-200:])

print("A4 a real unknown stays unknown — the repair must not manufacture a pass")
stale = fresh_snapshot(HOST)
stale["observed_at"] = "2020-01-01T00:00:00+00:00"
rc4, out4 = run([ROW8], stale)
check("A4 stale snapshot still returns rc=1", rc4 == 1, f"rc={rc4}")
check("A4 with its reason named", "stale" in out4 and "UNKNOWN" in out4, out4[:200])
foreign = fresh_snapshot("someone-elses-box")   # snapshot CLAIMS another box; we run on HOST
rc4b, out4b = run([ROW8], foreign, host=HOST)
check("A4 foreign-host snapshot also rc=1", rc4b == 1, f"rc={rc4b}")
check("A4 foreign-host reason names the host mismatch",
      "another host" in out4b or "stale" in out4b, out4b[:200])

print("OVERLAP (cat 2) — two failure states at once; neither may mask the other")
# the 2026-09-19 real state: a row shape the reader cannot take AND a stale snapshot
rc_o, out_o = run([row9], stale)
check("overlap: stale snapshot reported", "stale" in out_o, out_o[:200])
check("overlap: the extra-field row still rendered, not dropped", "D:L1\t" in out_o, out_o[-200:])
check("overlap: rc reflects the unavailable evidence", rc_o == 1, f"rc={rc_o}")

print("WRONG OWNER (cat 3) — a WILL/? row must not crash or claim desk evidence")
rw = SL.Row("D:L2", "2026-09-19", 0, "WILL", "WILL-OWNED", "b", "c", "cat")
rcw, outw = run([rw], fresh_snapshot(HOST))
check("wrong owner: WILL row does not crash", rcw == 0, f"rc={rcw}")
check("wrong owner: excluded from the desk overview",
      "\nWILL\t{" not in run([rw], fresh_snapshot(HOST), activities={"desks": {}}, identities={})[1])

print("MISSING INFORMATION (cat 4) — fail loud, never silently drop or claim")
rce, oute = run([], fresh_snapshot(HOST))
check("missing info: empty due-row set does not crash", rce == 0, f"rc={rce}")
check("missing info: still prints the header and the completion line",
      "key\tdue\towner" in oute and "Full due-row view complete" in oute)
for absent in ("observed_at", "host"):
    bad = fresh_snapshot(HOST)
    bad.pop(absent)
    rcb, outb = run([ROW8], bad)
    check(f"missing info: absent '{absent}' fails LOUD (rc=1 + reason)",
          rcb == 1 and "UNKNOWN:" in outb, f"rc={rcb}")

print("A5 standing guarantees unchanged")
_, out5 = run([ROW8], fresh_snapshot(HOST))
check("A5 spawn_authorized never true", '"spawn_authorized": true' not in out5.lower())
check("A5 never asserts a desk is absent/offline",
      "offline" not in out5.lower() and '"current_presence": "ABSENT"' not in out5)


print("A6 an IMPORT-TIME failure must reach the same DID-NOT-RUN state (reader ❌2)")
# move a real dependency away in a throwaway copy of the tree's import path
import os, shutil, tempfile
tmp = tempfile.mkdtemp(prefix="a6-")
shutil.copytree(ROOT / "PROME/tools", Path(tmp) / "tools", dirs_exist_ok=True)
os.makedirs(Path(tmp) / "scripts", exist_ok=True)
for f in (ROOT / "scripts").glob("*.py"):          # everything EXCEPT docket_view
    if f.name != "docket_view.py":
        shutil.copy(f, Path(tmp) / "scripts" / f.name)
p6 = subprocess.run([sys.executable, str(Path(tmp) / "tools" / "session_presence.py")],
                    capture_output=True, text=True, cwd=tmp)
check("A6 a missing dependency returns rc=2, not rc=1", p6.returncode == 2,
      f"rc={p6.returncode} out={p6.stdout[-160:]} err={p6.stderr[-160:]}")
check("A6 and prints the marker", "CHECK DID NOT RUN" in p6.stdout, p6.stdout[-200:])
shutil.rmtree(tmp, ignore_errors=True)

print("A7 the GATE must key did-not-run on the MARKER, never on rc==2 (reader ❌1)")
# ⛔ verified at prome_gate itself. The first version of this suite never imported the gate,
# which is exactly how the rc=2 contract break shipped — wrong artifact, clean result.
sys.path.insert(0, str(ROOT / "PROME/tools"))
import prome_gate as PG          # noqa: E402
check("A7 the gate defines a did-not-run MARKER", hasattr(PG, "DID_NOT_RUN"))
src = (ROOT / "PROME/tools/prome_gate.py").read_text(encoding="utf-8")
check("A7 the gate no longer keys the label on rc==2",
      'if p.returncode == 2 else' not in src, "rc-keyed label still present")
check("A7 it keys on the marker instead", "DID_NOT_RUN in body" in src)
check("A7 marker string agrees with what session_presence prints",
      PG.DID_NOT_RUN == "CHECK DID NOT RUN")

print("A7b a COMPLETED cannot-certify rc=2 must NOT be labelled did-not-run")
# spawn_list returns 2 from a run that finished and found UNKNOWN rows (CHECK_STANDARD §9)
cc = subprocess.run([sys.executable, "-c",
    "print('\u26d4 1 row(s) UNKNOWN — unparseable owner cell'); raise SystemExit(2)"],
    capture_output=True, text=True)
check("A7b the cannot-certify fixture exits 2 without the marker",
      cc.returncode == 2 and "CHECK DID NOT RUN" not in cc.stdout)
check("A7b so the gate's label would NOT fire on it",
      PG.DID_NOT_RUN not in cc.stdout,
      "a completed cannot-certify run would be mislabelled did-not-run")

print()
if FAILED:
    print(f"❌ PRESENCE-READER CONTRACT: {len(FAILED)} FAILED — " + " · ".join(FAILED))
    raise SystemExit(1)
print("✅ PRESENCE-READER CONTRACT: all acceptance conditions + 3 neighbour categories PASS")
