#!/usr/bin/env python3
"""Named housekeeping checks, not a financial grader or a whole-desk certificate."""
from pathlib import Path
from collections import Counter
import argparse,csv,hashlib,json,re,datetime

def fingerprint(kind,item,anchor):
    # Lines may move; the finding's source, type, token and source-line anchor persist.
    token=str(item[3]).split(' (actual ')[0]
    key=[kind,item[0],str(item[2]),token,re.sub(r'\s+',' ',anchor).strip()[:200]]
    return hashlib.sha256(json.dumps(key,ensure_ascii=False).encode()).hexdigest()

def findings(root,drift,revived):
    result=[]
    for kind,items in [('value',drift),('retired',revived)]:
        for item in items:
            anchor=(Path(root)/item[0]).read_text().splitlines()[item[1]-1]
            result.append({'identity':fingerprint(kind,item,anchor),'kind':kind,
                           'path':item[0],'line':item[1],'token':str(item[3]),'anchor':anchor[:200]})
    return result

def compare_history(current,baseline):
    now=Counter(x['identity'] for x in current);old=Counter(x['identity'] for x in baseline)
    return now-old,old-now

def current_fields(root):
    root=Path(root);issues=[]
    def read(path):
        p=root/path
        if not p.is_file():issues.append(('missing-field-source',path));return ''
        return p.read_text()
    raw=read('workbook/KB.tsv');lines=[l for l in raw.splitlines() if l and not l.startswith('#')]
    if not lines:return issues+[('KB-schema','no rows/header')]
    rows=list(csv.DictReader(lines,delimiter='\t'))
    if any(None in r or any(v is None for v in r.values()) for r in rows):
        return issues+[('KB-schema','malformed row')]
    if len({r['ID'] for r in rows})!=len(rows):issues.append(('KB-ID','duplicate ID'))
    if any(not r['Stale_By'] for r in rows if r['Status']=='ACTIVE'):issues.append(('KB-expiry','active row missing expiry date'))
    index=read('INDEX.md');m=re.search(r'KB\s+(\d+)\s+rows\s*/\s*(\d+)\s+(?:groups|Group)',index)
    if not m or (int(m[1]),int(m[2]))!=(len(rows),len({r['Group'] for r in rows})):
        issues.append(('INDEX-KB-count','header does not match KB'))
    nav=read('workbook/KB_INDEX.md');seen=set()
    for line in nav.splitlines():
        cells=[x.strip() for x in line.split('|')]
        if len(cells)==5 and cells[2].isdigit():
            group=cells[1];seen.add(group);gr=[r for r in rows if r['Group']==group]
            expected={r['ID'].removeprefix('KB-WAL-') for r in gr}
            if int(cells[2])!=len(gr) or set(cells[3].split(', '))!=expected:
                issues.append(('KB-group',group+' count/IDs disagree'))
    if seen!={r['Group'] for r in rows}:issues.append(('KB-group','missing/extra group'))
    if any(r['Status']=='ACTIVE' and 'date NOT ANNOUNCED' in r['Fact'] for r in rows) and any(r['ID']=='KB-WAL-217' and r['Status']=='ACTIVE' for r in rows):
        issues.append(('obsolete-earnings-date','active unannounced row beside announced successor'))
    positions=read('POSITIONS.md').split('## History',1)[0]
    leg_count=sum(bool(re.match(r'\| \*\*\$\d+P\*\* \|',line)) for line in positions.splitlines())
    if re.search(r'Acquisition date\s*(?:/[^.]{0,80})?\s*[:=]\s*UNKNOWN',positions,re.I):
        issues.append(('position-acquisition','current acquisition date still UNKNOWN beside accepted activity'))
    charter=read('CLAUDE.md')
    m=re.search(r'Live book\s*=\s*(one|two|\d+)\b',charter,re.I)
    if m:
        count={'one':1,'two':2}.get(m[1].lower(),int(m[1]) if m[1].isdigit() else 0)
        if count!=leg_count:issues.append(('position-mirror','charter leg count differs from positions'))
    if 'auto-loads when launched from this dir' in index:issues.append(('runtime-loading','index assumes CLAUDE auto-load'))
    return issues

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--strict',action='store_true');a=ap.parse_args()
    import importlib.util
    spec=importlib.util.spec_from_file_location('wal_legacy_drift',a.root/'scripts/derived_drift_check.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    canon,drift,revived=module.collect(str(a.root))
    issues=current_fields(a.root)
    baseline_path=a.root/'workbook/DRIFT_HISTORY_2026-10-14.json'
    if not baseline_path.exists():issues.append(('history-baseline','reviewed identity baseline missing'));new={};cleared={}
    else:
        baseline=json.loads(baseline_path.read_text());new,cleared=compare_history(findings(a.root,drift,revived),baseline['reviewed_findings'])
        if datetime.date.today().isoformat()>baseline['review_by']:issues.append(('history-review','review date passed'))
    print(f"Named current-field issues: {len(issues)}; new historical-pattern identities: {sum(new.values())}; cleared reviewed identities: {sum(cleared.values())}.")
    for issue in issues:print('CHECK',*issue)
    for identity in new:print('NEW',identity)
    print('Scope: selected claims, KB/navigation, acquisition/date/position mirrors only; not every statement, market fact or trade rule.')
    return 1 if a.strict and (issues or new or canon is None) else 0

if __name__=='__main__':raise SystemExit(main())
