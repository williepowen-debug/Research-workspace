from fx2 import *
root,repo,app,(qs,ow,dl,au,no,pf),c=setup('d'); accept(root,app,c,**ON)
e=answer(root,qs,repo); publish(root,dl,e); p,cc=ruled(root,e,au); ref={'path':p,'commit':cc}
now=lambda:datetime.now(timezone.utc).isoformat()
base=dict(response_id=e['id'],response_sha256=e['sha256'],canonical_ruling=None,chat_confirmation=None,confirmed_response_sha256=None)
def rc(schema,state,prev,**k):
    x=dict(base,schema_version=schema,id=uuid.uuid4().hex,state=state,at=now(),previous_receipt_id=prev); x.update(k); return x
two=lambda prev:rc('decisions-receipt/2','integrated',prev,canonical_ruling=ref,confirmed_response_sha256=e['sha256'],authorization_basis='app')
def trial(label,items):
    paths=[]
    for x in items:
        q=ow.receipt_path(repo,x); q.parent.mkdir(parents=True,exist_ok=True); q.write_text(pf.encoded(x)+'\n'); paths.append(q)
    push(root,'t'); attempt(label,lambda:[(i['schema_version'][-1],i['state']) for i in pf.read_receipts(repo,e)])
    for q in paths: q.unlink()
    push(root,'t-')
trial('/2 root',[two(None)])
a=rc('decisions-receipt/1','needs_clarification',None); trial('clarif->/2',[a,two(a['id'])])
a=rc('decisions-receipt/1','rejected_stale',None); trial('stale->/2',[a,two(a['id'])])
a=rc('decisions-receipt/1','received',None); trial('received->/2',[a,two(a['id'])])
leg=rc('decisions-receipt/1','integrated',None,canonical_ruling=ref,chat_confirmation=ref,confirmed_response_sha256=e['sha256']); trial('legacy /1 integrated root',[leg])
