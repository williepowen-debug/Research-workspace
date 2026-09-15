import pathlib,subprocess,sys,csv,io,datetime as dt,json
sys.path.insert(0,str(pathlib.Path('PROME/tools').resolve()))
import decision_deck as D, prome_gate as G, spawn_list as S, wq_ledger as W
sys.path.insert(0,str(pathlib.Path('scripts').resolve()));import docket_view as V
def blob(rev,p):return subprocess.check_output(['git','show',rev+':'+p],text=True)
for rev in ['f222c6e15','303267de8']:
 print('\nREV',rev)
 rows=D.parse_open(blob(rev,'PROME/WILL_QUEUE.md'));r=next(r for r in rows if str(r['n'])=='219')
 print('WQ219 blocked',r['blocked'],'blocker',r['blocker'],'ledger status calculation',W.status_of_open(r))
 for days in [0,7]:print('aged_wait hypothetical darkness',days,G.aged_waits([r],dt.date(2026,9,20),lambda _:days))
 ledger=list(csv.DictReader(io.StringIO(blob(rev,'PROME/registry/WQ_LEDGER.tsv')),delimiter='\t'));print('WQ219 latest ledger state',next(r['status_after'] for r in reversed(ledger) if r['wq']=='219'))
 state=blob(rev,'PROME/DOCKET.tsv').splitlines()[354].split('\t')[3]
 print('L355 token',state[:70],'docket_class',V.state_kind(state),'spawn_class',S.state_kind(state))
 print('SCRATCH generated L355 count',blob(rev,'PROME/SCRATCH.md').split('<!-- DOCKET-VIEW BEGIN -->')[1].split('<!-- DOCKET-VIEW END -->')[0].count('L355'))
 gates=list(csv.DictReader((l for l in blob(rev,'PROME/GATES.tsv').splitlines() if l and not l.startswith('#')),delimiter='\t'));li=next(r for r in gates if r['gate_id']=='GATE-LIQ-069')
 print('LIQ last_checked',li['last_checked'][:480])
 print('STATUS table header',next(l for l in blob(rev,'PROME/STATUS.md').splitlines() if l.startswith('| PROME action')))
 dash=json.loads(blob(rev,'PROME/tools/dashboard_state.json'));print('dashboard stale assertion','BRENT has NOT re-graded' in dash['one'],'new assertion','BRENT RE-GRADED BG-02 on 9/12' in dash['one'])
 print('backlog mention',[(n,l[:180]) for n,l in enumerate(blob(rev,'PROME/SCRATCH.md').splitlines(),1) if '12 packet' in l or '12-packet' in l])
 print('11th packets',len([l for l in subprocess.check_output(['git','ls-tree','--name-only',rev,'PROME/inbox/'],text=True).splitlines() if l.startswith('PROME/inbox/2026-09-11')]))
