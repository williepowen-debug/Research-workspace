import hashlib, json, os, shutil, subprocess, sys, uuid
from datetime import datetime, timezone
from pathlib import Path
SRC = Path('/tmp/cato-wq638')
OPT = 'PROME/proposals/2026-11-06_wq700-options.md'
def sh(root,*a,check=True):
    return subprocess.run(['git',*a],cwd=root,text=True,capture_output=True,check=check).stdout
def row(q='Should X happen?', ptr=OPT, rec='Recommend A.', notes='notes', n='700'):
    p = f' <!-- decisions-options: {ptr} -->' if ptr else ''
    return f'| {n} | **{q}**{p} | DECISION | 2026-11-20 | 11/06 | {rec} | {notes} |'
def queue(rows):
    return '# Q\n\n## OPEN\n\n| # | Item | Type | Needed by | Since | PROME rec | Notes |\n|---|---|---|---|---|---|---|\n'+'\n'.join(rows)+'\n\n## CLOSED\n'
def options(r, policy, version=2, rec='A', n=700):
    d={'schema_version':f'decisions-options/{version}','wq_id':n,'queue_row_sha256':hashlib.sha256(r.encode()).hexdigest(),
       'choices':[{'id':'A','label':'Do A','meaning':'A means','consequence':'A leads'},{'id':'B','label':'Do B','meaning':'B means','consequence':'B leads'}]}
    if version==2:
        d['recommended_choice_id']=rec; d['confirmation']=policy
    return '# options\n\n```decisions-options\n'+json.dumps(d,ensure_ascii=False,indent=1)+'\n```\n'
APP={'mode':'app','scope':'reversible_internal','reason':'Internal, reversible.'}
CHAT={'mode':'chat','scope':'trade','reason':'A trade.'}
def build(name, policy=APP, version=2):
    root=Path('/tmp/wq638-rev/fx')/name
    shutil.rmtree(root,ignore_errors=True); shutil.rmtree(str(root)+'.git',ignore_errors=True)
    root.mkdir(parents=True)
    for sub in ('AGENTS/CATO/prototypes/decisions/mvp','AGENTS/CATO/prototypes/decisions/comparison'):
        shutil.copytree(SRC/sub,root/sub,ignore=shutil.ignore_patterns('__pycache__','local-state','*.png'))
    (root/'scripts').mkdir()
    for n in ('safe-push.sh','install-git-hooks.sh','claim_check.py','orphan_check.sh','account_guard.py'): shutil.copy(SRC/'scripts'/n,root/'scripts/')
    shutil.copytree(SRC/'scripts/githooks',root/'scripts/githooks'); (root/'AGENTS/CATO/decisions').mkdir(parents=True,exist_ok=True); shutil.copy(SRC/'AGENTS/CATO/decisions/.gitignore',root/'AGENTS/CATO/decisions/')
    (root/'PROME/tools').mkdir(parents=True); shutil.copy(SRC/'PROME/tools/willq_view.py',root/'PROME/tools/')
    (root/'PROME/proposals').mkdir(); (root/'PROME/inbox').mkdir(); (root/'PROME/decisions').mkdir()
    (root/'PROME/inbox/.keep').write_text(''); (root/'PROME/decisions/.keep').write_text('')
    r=row(); (root/'PROME/WILL_QUEUE.md').write_text(queue([r]))
    (root/OPT).write_text(options(r,policy,version))
    sh(root,'init','-q','-b','master'); sh(root,'config','user.email','fx@example.invalid'); sh(root,'config','user.name','fx')
    bare=str(root)+'.git'; subprocess.run(['git','init','-q','--bare','-b','master',bare],check=True)
    sh(root,'remote','add','origin',bare); sh(root,'add','-A'); sh(root,'commit','-qm','base'); sh(root,'push','-q','origin','master'); sh(root,'fetch','-q','origin')
    return root
def load(root):
    m=str(root/'AGENTS/CATO/prototypes/decisions/mvp'); sys.path.insert(0,m)
    sys.dont_write_bytecode=True
    import queue_store, owner_receipt, delivery, authorization, notifications, pilot_files
    return queue_store, owner_receipt, delivery, authorization, notifications, pilot_files
def push(root,msg='c'):
    sh(root,'add','-A'); sh(root,'commit','-qm',msg); sh(root,'push','-q','origin','master'); sh(root,'fetch','-q','origin')
    return sh(root,'rev-parse','HEAD').strip()
def answer(root,qs,repo,action='choose',choice='A',note='cond one',revisit='',wq='700',sup=None):
    state=root/'.state'; state.mkdir(exist_ok=True)
    st=qs.QueueStore(state/f'queue-{wq}.sqlite3',repo,wq,True)
    d=st.display()
    ev=st.save({'id':uuid.uuid4().hex,'display_hash':d['hash'],'unit_id':wq+'.queue','action':action,'choice_id':choice if action=='choose' else None,'note':note,'revisit':revisit,'supersedes':(d['last'] or {}).get('id') if sup is None else sup})
    return ev
def publish(root,dl,ev):
    from pilot_files import encoded
    p=root/dl.event_path(ev); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(encoded(ev)+'\n')
    (root/f"PROME/inbox/decisions-{ev['id']}-from-CATO.md").write_text(dl.packet_text(ev))
    sh(root,'add','-f',dl.event_path(ev))
    return push(root,'publish')
def ruled(root,ev,auth,name=None,**over):
    now=datetime.now(timezone.utc).isoformat()
    proof={'schema_version':'decisions-app-authorization/1','response_id':ev['id'],'response_sha256':ev['sha256'],'scope':'reversible_internal',
           'conditions_within_scope':True,'no_chat_conflict':True,'readback_at':now,'readback_text':auth.readback_text(ev)}
    proof.update(over)
    path=name or f"PROME/proposals/2026-11-06_wq700-{ev['id'][:6]}-RULED.md"
    (root/path).write_text('# WQ-700 ruled\n\nRuling text.\n\n```decisions-app-authorization\n'+json.dumps(proof,ensure_ascii=False)+'\n```\n')
    return path,push(root,'ruling')
def attempt(label,fn):
    try:
        r=fn(); print(f'[{label}] ACCEPTED ->', (json.dumps({k:r.get(k) for k in ("schema_version","state","authorization_basis")}) if isinstance(r,dict) else r))
        return r
    except Exception as e:
        print(f'[{label}] REFUSED {type(e).__name__}: {str(e)[:150]}')
