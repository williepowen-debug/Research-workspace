import sys, json, csv, datetime as dt, collections, subprocess, re
sys.path.insert(0,'PROME/tools')
import orch_closeout as oc
LEDGER=sys.argv[1]; APPLY=len(sys.argv)>2 and sys.argv[2]=='--apply'
day=dt.date.today()
rows=[]
for line in open(LEDGER,encoding='utf-8').read().splitlines():
    if not line.strip() or line.startswith('#'): continue
    f=next(csv.reader([line],delimiter='\t',quoting=csv.QUOTE_NONE))
    if f[0]=='date' or len(f)!=13: continue
    rows.append(f)
res=json.loads(subprocess.run(['python3','PROME/tools/orch_closeout.py','--ledger',LEDGER,'--json'],capture_output=True,text=True).stdout)
state={r['key']:r for r in res['rows']}
groups=collections.defaultdict(list)
for f in rows:
    k=oc.touch_key(f)
    if k not in state: continue
    m=f[8].find(oc.MARKER)
    if m<0: continue
    try: data=json.loads(f[8][m+len(oc.MARKER):])
    except Exception: continue
    if 'resolves' in data or not data.get('session_id') or data.get('owner')!='PROME': continue
    groups[(f[1],data['session_id'])].append((f,k,data))
import os
EX={tuple(x) for x in json.load(open(os.path.dirname(os.path.abspath(__file__))+'/exclude.json'))}
plan=[]
for (desk,sid),items in sorted(groups.items(), key=lambda x:x[1][0][0][0]):
    recs=[(f,k,d) for f,k,d in items if f[6].startswith('CLOSED OUT')]
    targets=[(f,k,d) for f,k,d in items if state[k]['state'] in ('ASKED_WORKING','UNKNOWN')]
    if not recs or not targets or (desk,sid) in EX: continue
    rf=recs[-1][0]
    receipt=re.sub(r'\s+',' ',rf[6])[:300]
    plan.append((desk,sid,[k for f,k,d in targets],[f"{f[0]} {f[3]} ({state[k]['state']})" for f,k,d in targets],f"{rf[0]} {rf[3]}",receipt))
print('sessions with a real receipt:',len(plan),'targets:',sum(len(p[2]) for p in plan))
by=collections.Counter(p[3][0][:7] for p in plan); print(by)
no=[(desk,sid,[f"{f[0]} {f[3]}" for f,k,d in items]) for (desk,sid),items in groups.items() if not any(f[6].startswith('CLOSED OUT') for f,k,d in items) and any(state[k]['state']=='ASKED_WORKING' for f,k,d in items)]
print('sessions still working with NO receipt row:',len(no)); 
for n in no[-12:]: print('  ',n)
if APPLY:
    for desk,sid,keys,desc,src,receipt in plan:
        T=dt.datetime.now().astimezone().isoformat(timespec='seconds')
        block=json.dumps({"owner":"PROME","session_id":sid,"touch_at":T,"observed_at":T,"state":"ASKED_RECEIPT","ask":"closeout ask as recorded on the original rows","receipt":f"ORCH_LOG row {src}: {receipt}","resolves":keys})
        out=subprocess.run(['python3','scripts/orch_log.py','--ledger',LEDGER,'append','--date',day.isoformat(),'--desk',desk,'--tier','1','--touch','9-RECEIPT-RECONCILE','--trigger',f"Receipt reconciliation (Will 2026-11-23 12:17 ET, WQ-733): the receipt already on record at the {src} row, bound to its launch row; no new ask, no new evidence",'--drained','0','--delivered',f"RECONCILED {len(keys)} row(s) of session {sid}: "+'; '.join(desc),'--zero_capital','OK','--notes',"PROME prome-77. A record repair, not a touch of the desk. closeout_v1="+block],capture_output=True,text=True)
        if out.returncode: print('FAIL',desk,sid,out.stdout[-200:],out.stderr[-200:]); break
        import time; time.sleep(1.1)
    print('applied')
