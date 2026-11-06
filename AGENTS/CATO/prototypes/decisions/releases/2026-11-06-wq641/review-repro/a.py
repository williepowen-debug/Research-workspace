from fx2 import *
def closed(root): (root/'PROME/WILL_QUEUE.md').write_text(queue([]))
def blocked(root): (root/'PROME/WILL_QUEUE.md').write_text(queue([row(notes='WAITING on Bob')]))
def newsrc(root):
    p='PROME/proposals/2026-11-06_wq700b-options.md'; r=row(ptr=p); (root/'PROME/WILL_QUEUE.md').write_text(queue([r])); (root/p).write_text(options(r,CHAT))
def reword(root): (root/'PROME/WILL_QUEUE.md').write_text(queue([row(q='Should X happen, now covering a held position trade?',ptr=None)]))
def inplace(root): (root/OPT).write_text(options(row(),CHAT))
def rec(root): (root/OPT).write_text(options(row(),APP,rec='B'))
def brief(root): (root/OPT).write_text((root/OPT).read_text()+'\nappended prose changing terms\n')
def none(root): (root/'PROME/inbox/x.md').write_text('unrelated\n')
def deskchange(root): pass
CASES={'control':(none,0),'newsource-chat':(newsrc,0),'row-reworded':(reword,0),'row-closed':(closed,0),'inplace-chat-postruling':(inplace,1),'inplace-chat-preruling':(inplace,0),'rec-postruling':(rec,1),'blocked-postruling':(blocked,1),'prose-postruling':(brief,1)}
n=sys.argv[1]; m,first=CASES[n]
root,repo,app,(qs,ow,dl,au,no,pf),c=setup('a'+n); accept(root,app,c,**ON)
e=answer(root,qs,repo); publish(root,dl,e); recv(root,ow,repo,e)
assert au.app_only_enabled(repo,e) and not au.requires_chat(repo,e['display'],e)
if first:
    p,cc=ruled(root,e,au); m(root); push(root,'mut')
else:
    m(root); push(root,'mut'); p,cc=ruled(root,e,au)
attempt(n,lambda:ow.prepare(repo,e,'integrated',{'path':p,'commit':cc},None,app_only=True))
