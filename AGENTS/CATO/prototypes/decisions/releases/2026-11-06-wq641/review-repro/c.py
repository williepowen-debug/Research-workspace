from fx2 import *
# Fallback end to end on app-eligible card
root,repo,app,(qs,ow,dl,au,no,pf),c=setup('c'); accept(root,app,c,**OFF)
print('accepted',app.accepted(repo))
d=app.Desk(repo,root/'.state',True); st=d.display(); card=next(x for x in st['cards'] if x['wq_id']=='700')
print('errors',st['errors'],st['source_errors'],'can_deliver',st['can_deliver'],'can_respond',card['can_respond'],'requires',card['requires_confirmation'],'notif',st['notification'])
print('rec option',card['unit']['proposal']['recommendation']['option_id'])
e=answer(root,qs,repo); publish(root,dl,e)
print('packet says:',[s for s in dl.packet_text(e).split('. ') if 'App-only' in s or 'chat' in s])
print('inspect',{k:v for k,v in ow.inspect_event(repo,e).items() if k in('status','requires_chat_confirmation')})
(pp,cc)=ruled(root,e,au); ref={'path':pp,'commit':cc}
attempt('chat prep before received',lambda:ow.prepare(repo,e,'integrated',ref,ref))
ow.write_received(repo,e)
attempt('chat prep received unpublished',lambda:ow.prepare(repo,e,'integrated',ref,ref))
push(root,'recv')
attempt('app-only fallback',lambda:ow.prepare(repo,e,'integrated',ref,None,app_only=True))
attempt('no confirmation',lambda:ow.prepare(repo,e,'integrated',ref,None))
r=attempt('chat prep',lambda:ow.prepare(repo,e,'integrated',ref,ref))
# forged /2 under fallback (valid proof, hand written)
f=dict(r); f.update(schema_version='decisions-receipt/2',id=uuid.uuid4().hex,chat_confirmation=None,authorization_basis='app')
q=ow.receipt_path(repo,f); q.write_text(pf.encoded(f)+'\n'); push(root,'forge2')
attempt('hand /2 replay under fallback',lambda:[x['schema_version'] for x in pf.read_receipts(repo,e)])
st=app.Desk(repo,root/'.state',True).display(); card=next(x for x in st['cards'] if x['wq_id']=='700'); print('desk after hand /2',card['receipt'] and card['receipt']['state'],card['group'],st['errors'])
sh(root,'rm','-qf',str(q.relative_to(root))); push(root,'unforge')
w=r; q=ow.receipt_path(repo,w); q.write_text(pf.encoded(w)+'\n'); push(root,'rcpt')
attempt('chat /1 replay',lambda:[(x['schema_version'],x['state']) for x in pf.read_receipts(repo,e)])
st=app.Desk(repo,root/'.state',True).display(); card=next(x for x in st['cards'] if x['wq_id']=='700'); print('desk',card['receipt']['state'],card['group'])
# receipt chains
root2,repo2,app2,*_=[root,repo,app]
