import sys; sys.path.insert(0,'/tmp/wq638-rev/scripts')
from fxlib import *
import uuid, time
root=build('s3'); qs,ow,dl,au,no,pf=load(root); repo=qs.Repo(root)
e=answer(root,qs,repo,note='cond one\nline two'); publish(root,dl,e)
# stale with received receipt in place (real sequence)
rc=ow.write_received(repo,e); push(root,'recv'); print('received',rc)
ok=lambda p,c:{'path':p,'commit':c}
for label,over in [('edited readback',{'readback_text':'WQ-700: A — Do A'}),('wrong hash',{'response_sha256':'0'*64}),('naive ts',{'readback_at':'2026-11-06T12:00:00'}),
  ('readback before saved',{'readback_at':'2020-01-01T00:00:00+00:00'}),('future',{'readback_at':'2099-01-01T00:00:00+00:00'}),('conflict false',{'no_chat_conflict':False}),('scope false',{'conditions_within_scope':'true'}),('trade scope',{'scope':'trade'})]:
    p,c=ruled(root,e,au,name=f'PROME/proposals/x{uuid.uuid4().hex[:6]}-RULED.md',**over)
    attempt(label,lambda:ow.prepare(repo,e,'integrated',ok(p,c),None,app_only=True))
# yesterday's readback
from datetime import timedelta
y=(datetime.now(timezone.utc)-timedelta(days=1)).isoformat()
# unpublished ruling
p='PROME/proposals/local-RULED.md'; (root/p).write_text('x'); sh(root,'add','-A'); sh(root,'commit','-qm','local'); c=sh(root,'rev-parse','HEAD').strip()
attempt('unpublished ruling',lambda:ow.prepare(repo,e,'integrated',ok(p,c),None,app_only=True))
sh(root,'reset','-q','--hard','origin/master')
# later published answer
e2=answer(root,qs,repo,action='reply',choice=None,note='changed my mind'); publish(root,dl,e2)
p,c=ruled(root,e,au,name='PROME/proposals/y1-RULED.md')
attempt('superseded app-only',lambda:ow.prepare(repo,e,'integrated',ok(p,c),None,app_only=True))
p2,c2=ruled(root,e2,au,name='PROME/proposals/y2-RULED.md')
attempt('latest app-only',lambda:ow.prepare(repo,e2,'integrated',ok(p2,c2),None,app_only=True))
print('readback reply:',repr(au.readback_text(e2)))
# defer readback
# chat-required card
root2=build('s3b',policy=CHAT)
for m in ['queue_store','owner_receipt','delivery','authorization','notifications','pilot_files','options','store','briefs','history']: sys.modules.pop(m,None)
sys.path[:]=[x for x in sys.path if 'wq638-rev/fx' not in x]
qs,ow,dl,au,no,pf=load(root2); repo=qs.Repo(root2)
e=answer(root2,qs,repo); publish(root2,dl,e)
print('chat card requires:',ow.inspect_event(repo,e).get('requires_chat_confirmation'))
print(dl.packet_text(e)[-330:])
p,c=ruled(root2,e,au)
attempt('chat card app-only',lambda:ow.prepare(repo,e,'integrated',ok(p,c),None,app_only=True))
forged={'schema_version':'decisions-receipt/2','id':uuid.uuid4().hex,'response_id':e['id'],'response_sha256':e['sha256'],'state':'integrated','at':datetime.now(timezone.utc).isoformat(),'previous_receipt_id':None,'canonical_ruling':ok(p,c),'chat_confirmation':None,'confirmed_response_sha256':e['sha256'],'authorization_basis':'app'}
q=ow.receipt_path(repo,forged); q.parent.mkdir(parents=True,exist_ok=True); q.write_text(pf.encoded(forged)+'\n'); push(root2,'forge')
attempt('forged /2 on chat card (replay)',lambda:pf.read_receipts(repo,e))
# Malformed confirmation
for label,bad in [('mode list',{'mode':['app'],'scope':'reversible_internal','reason':'x'}),('scope dict',{'mode':'app','scope':{},'reason':'x'})]:
    try:
        au.validate_policy(bad); print(label,'accepted')
    except Exception as ex: print(label,type(ex).__name__,ex)
