import sys; sys.path.insert(0,'/tmp/wq638-rev/scripts')
from fxlib import *
root=build('s1'); qs,ow,dl,au,no,pf=load(root); repo=qs.Repo(root)
# happy
e=answer(root,qs,repo); publish(root,dl,e)
print('intake',{k:v for k,v in ow.inspect_event(repo,e).items() if k in('status','requires_chat_confirmation','readback_text')})
p,c=ruled(root,e,au)
r=attempt('happy app-only',lambda:ow.prepare(repo,e,'integrated',{'path':p,'commit':c},None,app_only=True))
attempt('app-only with confirmation',lambda:ow.prepare(repo,e,'integrated',{'path':p,'commit':c},{'path':p,'commit':c},app_only=True))
attempt('no flag no confirmation',lambda:ow.prepare(repo,e,'integrated',{'path':p,'commit':c},None))
# write receipt and replay
pth=ow.receipt_path(repo,r); pth.parent.mkdir(parents=True,exist_ok=True); pth.write_text(pf.encoded(r)+'\n'); push(root,'receipt')
print('replay',[x['state'] for x in pf.read_receipts(repo,e)],[x['state'] for x in pf.read_receipts(repo,e,commit='origin/master')])
# tamper variants on fresh answers
