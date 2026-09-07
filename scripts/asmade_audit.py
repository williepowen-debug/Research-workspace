#!/usr/bin/env python3
"""
asmade_audit.py — AS-MADE CONFIDENCE AUDIT for prediction ledgers (harvest H2, Will-ruled 2026-09-07).

WHY: the 2026-03-04 PREDICTIONS.tsv rollout (91c301279) stamped a placeholder Date_Made on rows
that were ALREADY LIVE in each desk's STATUS.md. A calibration audit that verifies "as-made"
against that ledger reads the walked-down value and passes. LABOR found 4 of 12 scored rows
mis-scored this way (Brier 0.299 -> 0.342). This tool runs LABOR's reproducible procedure
fleet-wide: STATUS.md is the REGISTRATION surface; the TSV is downstream of it.

METHOD (per row): first commit in `git log --reverse -S<ID> -- AGENTS/<D>/STATUS.md` whose blob
carries the ID on a line with a percentage cell; read the FIRST percentage on that line as the
earliest-registered confidence. Compare to the ledger's as-made: the `(was X% [...])` value if the
WQ-112 form is present, else the first percentage in the Confidence cell.

VERDICT per row: SAME · MISMATCH (candidate, owner verifies at the blob) · NOT-FOUND (ID never
appears with a % in STATUS history — the row may have been born in the TSV) · NO-CONF (ledger has
no Confidence column / cell).  Exit: 0 clean · 1 >=1 MISMATCH · 2 CANNOT-VERIFY (no ledger, bad
header). Perimeter printed every run (CHECK_STANDARD §9 / §4).

CANDIDATE GENERATOR, NOT A VERDICT — two named limits:
  (1) it reads the first CELL that is only a percentage after the ID (LABOR's rule); a registration
      line that is not a table row falls back to the first % after the ID.
  (2) the ID can POST-DATE the registration: a row born as prose ("U-3 reaches 4.7%") and numbered
      later returns the numbering commit, not the true first sighting. If the ledger Date_Made precedes
      the printed STATUS date, the owner walks by prediction TEXT (LABOR's 9/7 method). The tool prints
      both dates so that case is visible.

Usage:
  python3 scripts/asmade_audit.py LABOR [ZHAO ...]          # live ledger
  python3 scripts/asmade_audit.py LABOR --ledger-rev <sha>  # ledger as of a commit (positive control)
  python3 scripts/asmade_audit.py --all-seeded
"""
import sys, re, subprocess, csv, io, os, argparse

ROOT = subprocess.run(["git","rev-parse","--show-toplevel"],capture_output=True,text=True).stdout.strip()
SEEDED = ["CARL","HANS","HAWK","HENRY","LABOR","LIQUID","MARCO","OTTO","REGINALD","SAM","ZHAO"]
PCT = re.compile(r"(?<![\d.])(\d{1,3})\s?%")
WAS = re.compile(r"\(was\s+(\d{1,3})\s?%")

def git(*a):
    return subprocess.run(["git",*a],cwd=ROOT,capture_output=True,text=True)

def find_ledger(desk):
    cands=[]
    for dp,dn,fn in os.walk(os.path.join(ROOT,"AGENTS",desk)):
        if any(x in dp for x in ("/archive","/sub_agents","/sub-agents","/inbox","/outbox")): continue
        for f in fn:
            if f.upper().startswith("PREDICTIONS") and f.endswith(".tsv"): cands.append(os.path.relpath(os.path.join(dp,f),ROOT))
    pref=[c for c in cands if c.endswith("workbook/PREDICTIONS.tsv")]
    return (pref or sorted(cands) or [None])[0]

def read_ledger(path, rev=None):
    if rev:
        r=git("show",f"{rev}:{path}")
        if r.returncode: return None,f"no blob {rev}:{path}"
        text=r.stdout
    else:
        text=open(os.path.join(ROOT,path),encoding="utf-8").read()
    lines=[l for l in text.split("\n") if l and not l.startswith("#")]
    rows=list(csv.reader(io.StringIO("\n".join(lines)),delimiter="\t",quoting=csv.QUOTE_NONE))
    hdr=rows[0]; idc=next((i for i,h in enumerate(hdr) if h.strip() in ("Pred_ID","ID")),None)
    cc=next((i for i,h in enumerate(hdr) if h.strip().lower().startswith("confidence")),None)
    dm=next((i for i,h in enumerate(hdr) if h.strip()=="Date_Made"),None)
    st=next((i for i,h in enumerate(hdr) if h.strip()=="Status"),None)
    if idc is None: return None,"no ID column"
    return dict(hdr=hdr,rows=rows[1:],idc=idc,cc=cc,dm=dm,st=st),None

def earliest_status(desk, pid):
    r=git("log","--reverse","--format=%H %cs","-S",pid,"--",f"AGENTS/{desk}/STATUS.md")
    for line in r.stdout.split("\n"):
        if not line: continue
        sha,d=line.split(" ")
        blob=git("show",f"{sha}:AGENTS/{desk}/STATUS.md").stdout
        tok=re.compile(r"(?<![A-Z0-9-])"+re.escape(pid)+r"(?![\d.])")   # exact ID token: not VX-LAB-15, not LAB-150, not LAB-15.02
        for l in blob.split("\n"):
            mt=tok.search(l)
            if mt:
                rest=l[mt.end():]
                # LABOR's rule: read a CELL that is only a percentage (bold/arrows tolerated), never a
                # % embedded in the prediction text ("Temp YoY stays <-6%" carries a 6% that is not a confidence).
                cells=[c.strip() for c in rest.split("|")]
                for c in cells:
                    mc=re.match(r"^\**\s*(\d{1,3})\s?%\**", c)
                    if mc: return d, int(mc.group(1)), sha[:9], l.strip()[:140]
                # non-table registration line ("Adding LAB-12 ... at 60% confidence"): first % after the ID
                if "|" not in l:
                    m=PCT.search(rest)
                    if m: return d, int(m.group(1)), sha[:9], l.strip()[:140]
    return None,None,None,None

def audit(desk, rev=None):
    path=find_ledger(desk)
    if not path: print(f"[{desk}] CANNOT-VERIFY: no PREDICTIONS*.tsv found"); return 2
    led,err=read_ledger(path,rev)
    if err: print(f"[{desk}] CANNOT-VERIFY: {err}"); return 2
    n=0; mism=0; nf=0; same=0; noc=0
    print(f"[{desk}] ledger {path}{' @'+rev if rev else ''} · {len(led['rows'])} rows · Confidence col: {'yes' if led['cc'] is not None else 'NO'}")
    for r in led["rows"]:
        if len(r)<=led["idc"]: continue
        pid=r[led["idc"]].strip()
        if not re.match(r"^[A-Z]{2,4}-\d+",pid): continue
        n+=1
        if led["cc"] is None or len(r)<=led["cc"]:
            noc+=1; continue
        cell=r[led["cc"]]
        w=WAS.search(cell); p=PCT.search(cell)
        asmade = int(w.group(1)) if w else (int(p.group(1)) if p else None)
        d,pc,sha,ctx=earliest_status(desk,pid)
        dm=r[led["dm"]] if led["dm"] is not None and len(r)>led["dm"] else "?"
        if asmade is None: noc+=1; continue
        if pc is None: nf+=1; print(f"   NOT-FOUND  {pid:8s} ledger as-made {asmade:3d}% (Date_Made {dm}) — ID never appears with a % in STATUS history"); continue
        if pc==asmade: same+=1
        else:
            mism+=1; print(f"   MISMATCH   {pid:8s} ledger as-made {asmade:3d}% (Date_Made {dm}) vs STATUS earliest {pc:3d}% @{sha} {d} :: {ctx}")
    print(f"   perimeter: {n} rows read · SAME {same} · MISMATCH {mism} · NOT-FOUND {nf} · NO-CONF {noc}")
    return 1 if mism else 0

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("desks",nargs="*"); ap.add_argument("--all-seeded",action="store_true"); ap.add_argument("--ledger-rev")
    a=ap.parse_args(); desks=SEEDED if a.all_seeded else a.desks
    if not desks: ap.error("name desks or --all-seeded")
    rc=0
    for d in desks: rc=max(rc,audit(d,a.ledger_rev))
    print(f"ASMADE-AUDIT {rc}: {'>=1 MISMATCH candidate' if rc==1 else 'CANNOT-VERIFY on >=1 desk' if rc==2 else 'all SAME/NOT-FOUND'} — candidates, owner verifies at the named blob")
    return rc
if __name__=="__main__": sys.exit(main())
