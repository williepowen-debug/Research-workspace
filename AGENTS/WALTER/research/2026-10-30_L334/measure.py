"""L334 first deliverable: share of WALTER INFO vs ACTION handoff copies later CITED by the recipient desk.
Cited = the signal ID appears in a tracked file under AGENTS/<desk>/ outside its inbox/ (desk's own working files).
Window: rows routed after the d398fb2f5 timestamp sweep (start 2026-09-12) through 2026-10-23 (>=7 days to cite)."""
import csv, re, subprocess, collections, json, sys
ROOT='/home/willi/Research-workspace'
START, END = '2026-09-12', '2026-10-23T23:59:59Z'
rows=[r for r in csv.DictReader(open(f'{ROOT}/AGENTS/WALTER/routed/delivery_log.tsv',encoding='utf-8'),delimiter='\t')]
rows=[r for r in rows if START <= r['timestamp_routed'] <= END and r['role'] in ('INFO','ACTION')]
pat=re.compile(r'SIG-W-2026\d{4}-\d{3}')
cache={}
MODE=sys.argv[1] if len(sys.argv)>1 else 'strict'
EXCL=re.compile(r'(board_log|BOARD_LOG|consum|orphan|moves|disposition|audit|LIAISON|/inbox/|_INDEX|INDEX\.md|scan|ledger|receipt|census|manifest)',re.I)
STRICT=re.compile(r'(/STATUS[^/]*\.md$|/status_archive/|/workbook/KB[^/]*\.tsv$|/KB[^/]*\.tsv$|/thesis/|THESIS[^/]*\.md$)')
def cited(desk):
    if desk in cache: return cache[desk]
    out=subprocess.run(['git','grep','-oE',r'SIG-W-2026[0-9]{4}-[0-9]{3}','--',f'AGENTS/{desk}/'],cwd=ROOT,capture_output=True,text=True).stdout
    ids=set()
    for line in out.splitlines():
        f,_,i=line.rpartition(':')
        if EXCL.search(f): continue
        if MODE=='strict' and not STRICT.search(f): continue
        if MODE=='broad' and not (f.endswith('.md') or re.search(r'KB[^/]*\.tsv$',f)): continue
        ids.add(i)
    cache[desk]=ids; return ids
t=collections.defaultdict(lambda: collections.Counter())
for r in rows:
    d=r['recipient']; c=r['signal_id'] in cited(d)
    t[(d,r['role'])]['n']+=1; t[(d,r['role'])]['cited']+=c
    t[('ALL',r['role'])]['n']+=1; t[('ALL',r['role'])]['cited']+=c
res=[]
for (d,role),c in sorted(t.items()):
    res.append({'desk':d,'role':role,'n':c['n'],'cited':c['cited'],'rate':round(c['cited']/c['n'],3)})
json.dump({'window':[START,END],'rows':len(rows),'results':res},open(f'{ROOT}/AGENTS/WALTER/research/2026-10-30_L334/results_'+MODE+'.json','w'),indent=1)
for x in res:
    if x['desk']=='ALL' or x['n']>=20: print(f"{x['desk']:9} {x['role']:6} n={x['n']:4} cited={x['cited']:4} rate={x['rate']:.0%}")
