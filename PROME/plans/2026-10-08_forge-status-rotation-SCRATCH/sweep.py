# Consumer sweep: compare the four consumers' outputs between a baseline (captured before install) and now.
import sys, json, pathlib, subprocess, difflib
SP=pathlib.Path(sys.argv[1]); ROOT=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
sys.path.insert(0, str(ROOT/'PROME/tools'))
# 1. positions_from_forge --json
new=subprocess.run(['python3','AGENTS/TERRY/scripts/positions_from_forge.py','--json','--asof','2026-10-08'],cwd=ROOT,capture_output=True,text=True)
(SP/'after_positions.json').write_text(new.stdout)
a=json.loads((SP/'baseline_positions.json').read_text()); b=json.loads(new.stdout)
def strip(d):
    return json.dumps({k:[{kk:vv for kk,vv in r.items() if kk not in ('note','line')} for r in v] if isinstance(v,list) else v for k,v in d.items()}, sort_keys=True)
print('positions_from_forge: rc', new.returncode, '| stderr lines', len(new.stderr.splitlines()))
print('  identical ignoring note/line:', strip(a)==strip(b))
na=[r for v in a.values() if isinstance(v,list) for r in v]; nb=[r for v in b.values() if isinstance(v,list) for r in v]
changed=[(x.get('ticker'),x.get('instrument'),x.get('expiry_iso')) for x,y in zip(na,nb) if x.get('note')!=y.get('note')]
print('  rows whose note changed:', changed)
st=subprocess.run(['python3','AGENTS/TERRY/scripts/positions_from_forge.py','--selftest'],cwd=ROOT,capture_output=True,text=True); print('  selftest:', st.stdout.strip().splitlines()[-1] if st.stdout.strip() else st.stderr[-200:])
# 2. desk_attention.holdings
import desk_attention as da
h=da.holdings(ROOT.resolve()); (SP/'after_holdings.txt').write_text(json.dumps(h,default=str,indent=0,sort_keys=True))
ha=json.loads((SP/'baseline_holdings.txt').read_text()); hb=json.loads((SP/'after_holdings.txt').read_text())
def flat(x): 
    out=[]; 
    def rec(y):
        if isinstance(y,list): [rec(z) for z in y]
        elif isinstance(y,dict): out.append(y)
    rec(x); return out
fa,fb=flat(ha),flat(hb)
print('holdings: rows', len(fa), '->', len(fb), '| identical ignoring note/line:', [ {k:v for k,v in r.items() if k not in ('note','line')} for r in fa]==[ {k:v for k,v in r.items() if k not in ('note','line')} for r in fb])
print('  notes changed:', [(r.get('ticker'),r.get('instrument')) for r,s in zip(fa,fb) if r.get('note')!=s.get('note')])
# 3. will_brief.parse_money
import will_brief as wb
old=subprocess.check_output(['git','show','ef2bc83f1:FORGE/STATUS.md'],cwd=ROOT,text=True); cur=(ROOT/'FORGE/STATUS.md').read_text(encoding='utf-8')
try:
    pm_old=wb.parse_money(old); pm_new=wb.parse_money(cur)
except TypeError:
    pm_old=wb.parse_money(); pm_new=pm_old
print('parse_money old:', pm_old); print('parse_money new:', pm_new); print('  identical:', pm_old==pm_new)
# 4. pending_receipts
pr=subprocess.run(['python3','AGENTS/BRENT/scripts/pending_receipts.py'],cwd=ROOT,capture_output=True,text=True)
base=(SP/'baseline_pending.txt').read_text(); print('pending_receipts identical:', (pr.stdout+pr.stderr)==base, '| rc', pr.returncode)
