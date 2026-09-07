#!/usr/bin/env python3
"""
wiring_census.py — GUARD-WIRING CENSUS: what a desk's threshold script compares, beside what its
STATUS declares (harvest H1, Will-ruled 2026-09-07).

WHY: LABOR's labor_data.py fired RETIRED U-3 bars for 31 days while its docstring said "wired to
KEY THRESHOLDS", and never fetched EMRATIO, the series the live triggers actually key on. A guard
being CORRECT and being WIRED TO ITS DECLARED REFERENCE are independent properties
(finding_guard_correctness_and_wiring_are_independent).

WHAT IT REPORTS, per desk (CENSUS, not verdict — the owner reads the two columns side by side):
  SERIES    upper-case series tokens the script(s) fetch/compare (FRED-style IDs, tickers)
  CONSTANTS numeric literals adjacent to a comparison operator in the script(s), with their line
  STATUS    numbers appearing in the STATUS threshold section(s) (KEY THRESHOLDS / EXIT RULES /
            THRESHOLD headers); if no such section, the whole STATUS is scanned and SAID SO
  FLAGS     CONST-NOT-IN-STATUS: a compared constant whose text appears nowhere in STATUS
            (candidate UNDECLARED or RETIRED bar)
            SERIES-NOT-IN-STATUS: a fetched series ID (or its alias) absent from STATUS
            (candidate: the script watches something STATUS does not declare)
            ⚠️ what this CANNOT see: a constant that STATUS still MENTIONS as retired (LABOR's
            4.7/5.0 case) — presence is not wiring. That leg needs a reader. Stated, not tuned away.
Exit: 0 census printed, no flags · 1 >=1 flag · 2 CANNOT-VERIFY (no script / no STATUS).
PRODUCTION ACCEPTANCE SET (CHECK_STANDARD §3(e)):
  DEFECTIVE real input: AGENTS/LABOR/scripts/labor_data.py + STATUS.md at `f2558c075^` (the 31-day defect) →
      SERIES-IN-STATUS-NOT-FETCHED EMRATIO · SERIES-NOT-IN-STATUS TEMPHELPS · CONST 1900000 — all three real.
  CLEAN real input: NONE YET. The reverse leg over-fires on prose fleet-wide (run 2026-09-07, 28 desks), so this
      tool is a CENSUS and must not name a desk until that leg is scoped to threshold-table rows.

Usage: python3 scripts/wiring_census.py LABOR [WATT ...] | --all
"""
import sys, re, os, subprocess, argparse
ROOT=subprocess.run(["git","rev-parse","--show-toplevel"],capture_output=True,text=True).stdout.strip()
ALIAS={"EMRATIO":["EPOP","employment-population"],"UNRATE":["U-3","unemployment rate"],"CIVPART":["LFPR","participation"],
       "ICSA":["initial claims","claims"],"CCSA":["continuing claims","CC "],"IC4WSA":["4-wk","4-week"],"PAYEMS":["NFP","payroll"],
       "JTSHIL":["hires"],"JTSJOL":["openings"],"TEMPHELPS":["temp"],"DGS10":["10Y","10-year"],"DGS30":["30Y"],"DGS2":["2Y"],
       "BAMLH0A0HYM2":["HY OAS","HY spread"],"VIXCLS":["VIX"],"T10Y2Y":["2s10s","curve"],"DCOILBRENTEU":["Brent"],"DCOILWTICO":["WTI"]}
CMP=re.compile(r"(?:>=|<=|==|!=|>|<)\s*\(?\s*(-?\d[\d_,]*(?:\.\d+)?)")
SER=re.compile(r"[\"']([A-Z][A-Z0-9]{2,14}(?:=F)?)[\"']")
NUMTXT=re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?)(?:\s?[%KkMm])?")
SKIP_SERIES={"ERROR","WARN","INFO","OK","PASS","FAIL","STALE","FRESH","RED","GREEN","TRUE","FALSE","NONE","UTF","ASCII","GET","POST","ALERT","CANNOT","DAILY","WEEKLY"}

def scripts_for(desk):
    out=[]
    for sub in ("scripts","tools",""):
        d=os.path.join(ROOT,"AGENTS",desk,sub)
        if os.path.isdir(d):
            for f in sorted(os.listdir(d)):
                if f.endswith(".py") and not f.startswith("test"):
                    t=open(os.path.join(d,f),encoding="utf-8",errors="replace").read()
                    if re.search(r"threshold|flag|trigger|>=|<=",t,re.I) and re.search(r"fred|fetch|yf\.|yfinance|requests\.get|urlopen",t,re.I):
                        out.append((os.path.relpath(os.path.join(d,f),ROOT),t))
    return out

def status_thresholds(desk):
    p=os.path.join(ROOT,"AGENTS",desk,"STATUS.md")
    if not os.path.exists(p): return None,None
    t=open(p,encoding="utf-8",errors="replace").read()
    secs=[m.start() for m in re.finditer(r"^#{2,3} .*(THRESHOLD|EXIT RULE|TRIGGER|KILL)",t,re.M|re.I)]
    if secs:
        chunks=[]
        for s0 in secs:
            e=re.search(r"^#{2,3} ",t[s0+3:],re.M); chunks.append(t[s0:(s0+3+e.start()) if e else len(t)])
        return "\n".join(chunks),"threshold section(s)"
    return t,"WHOLE STATUS (no threshold-named section found)"

def census(desk):
    scr=scripts_for(desk)
    if not scr: print(f"[{desk}] CANNOT-VERIFY: no threshold/fetch script found under scripts/ or tools/"); return 2
    st,scope=status_thresholds(desk)
    if st is None: print(f"[{desk}] CANNOT-VERIFY: no STATUS.md"); return 2
    stlow=st.lower(); flags=0
    print(f"[{desk}] scripts: {', '.join(p for p,_ in scr)} · STATUS scope: {scope} ({len(st):,} B)")
    for path,t in scr:
        series=set(); consts=[]
        for i,l in enumerate(t.split("\n"),1):
            ls=l.strip()
            if ls.startswith("#") or ls.startswith('"""') or "print(" in ls or ls.startswith("f\"") : continue
            if re.search(r"fred|fetch|series|ticker|download|yf\.|symbol|SERIES\b|_ID",l,re.I):
                series.update(x for x in SER.findall(l) if x not in SKIP_SERIES and len(x)>=4 and not x.isdigit())
            if re.search(r"\b(if|elif|return|and|or|while|flag)\b",l):
                for m in CMP.finditer(l):
                    c=m.group(1).replace("_","").rstrip(",.")
                    if re.fullmatch(r"-?\d+(?:\.\d+)?",c): consts.append((c,i,ls[:80]))
        series=sorted(series)
        print(f"   {path}: SERIES {series if series else '(none literal)'}")
        for s_ in series:
            names=[s_]+ALIAS.get(s_,[])
            if not any(n.lower() in stlow for n in names):
                flags+=1; print(f"      SERIES-NOT-IN-STATUS  {s_}  (aliases tried: {names})")
        seen=set()
        for c,i,l in consts:
            if c in seen or c in ("0","1","2","3"): continue
            seen.add(c)
            variants={c, c.rstrip("0").rstrip(".") if "." in c else c, f"{int(float(c)):,}" if float(c)>=1000 else c}
            if float(c)>=1000: variants.add(f"{int(float(c))//1000}K"); variants.add(f"{float(c)/1000:g}K")
            hit=any(v.lower() in stlow for v in variants)
            print(f"      CONST {c:>12s}  line {i:4d}  {'in STATUS' if hit else 'NOT IN STATUS ⚠️'}  :: {l}")
            if not hit: flags+=1
    # REVERSE LEG — SERIES-IN-STATUS-NOT-FETCHED: STATUS names a gauge (by alias) that NO script fetches.
    # This is LABOR's EMRATIO case: STATUS moved T-03/T-04 onto EPOP on 8/7; the sweep never fetched it.
    fetched=set()
    for _,t in scr:
        for l in t.split("\n"):
            if re.search(r"fred|fetch|series|ticker|download|yf\.|symbol|SERIES\b|_ID",l,re.I): fetched.update(SER.findall(l))
    for sid,names in ALIAS.items():
        if sid in fetched: continue
        hit=[n for n in names if re.search(r"(?<![A-Za-z])"+re.escape(n.lower())+r"(?![A-Za-z])",stlow)]
        if hit and re.search(r"T-\d|trigger|fires?\b|threshold",stlow):
            # only flag when the alias sits on a line that reads like a trigger row
            rows=[l for l in st.split("\n") if any(re.search(r"(?<![A-Za-z])"+re.escape(n.lower())+r"(?![A-Za-z])",l.lower()) for n in hit) and re.search(r"T-\d|fires?\b|trigger|→|->",l)]
            if rows:
                flags+=1; print(f"      SERIES-IN-STATUS-NOT-FETCHED  {sid}  ({hit[0]!r} on {len(rows)} trigger-shaped STATUS line(s); first: {rows[0].strip()[:90]})")
    print(f"   flags: {flags}  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here")
    return 1 if flags else 0

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("desks",nargs="*"); ap.add_argument("--all",action="store_true"); a=ap.parse_args()
    desks=a.desks or (sorted(d for d in os.listdir(os.path.join(ROOT,"AGENTS")) if os.path.isdir(os.path.join(ROOT,"AGENTS",d,"scripts")) or os.path.isdir(os.path.join(ROOT,"AGENTS",d,"tools"))) if a.all else [])
    if not desks: ap.error("name desks or --all")
    rc=0
    for d in desks: rc=max(rc,census(d))
    print(f"WIRING-CENSUS {rc}: {'flags raised (candidates)' if rc==1 else 'CANNOT-VERIFY on >=1 desk' if rc==2 else 'no flags'} — a census; owner reads script vs STATUS side by side")
    return rc
if __name__=="__main__": sys.exit(main())
