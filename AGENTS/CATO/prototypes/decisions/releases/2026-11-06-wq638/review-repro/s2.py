import sys; sys.path.insert(0,'/tmp/wq638-rev/scripts')
from fxlib import *
# Staleness after the answer, before app-only prepare.
def case(name, mutate, ruling_first=False):
    root=build('s2'+name)
    for m in [k for k in sys.modules if k in('queue_store','owner_receipt','delivery','authorization','notifications','pilot_files','options','store','briefs','history')]: del sys.modules[m]
    sys.path[:]=[x for x in sys.path if 'wq638-rev/fx' not in x]
    qs,ow,dl,au,no,pf=load(root); repo=qs.Repo(root)
    e=answer(root,qs,repo); publish(root,dl,e)
    if ruling_first:
        p,c=ruled(root,e,au); mutate(root)
        push(root,'mutate')
    else:
        mutate(root); push(root,'mutate'); p,c=ruled(root,e,au)
    attempt(name+' inspect/intake',lambda:(lambda x:{'state':x.get('status')})(ow.inspect_event(repo,e)))
    attempt(name+' prepare app-only',lambda:ow.prepare(repo,e,'integrated',{'path':p,'commit':c},None,app_only=True))
def closed(root):
    (root/'PROME/WILL_QUEUE.md').write_text(queue([]) )
def blocked(root):
    r=row(notes='WAITING on Bob'); (root/'PROME/WILL_QUEUE.md').write_text(queue([r]))
def newsrc(root):
    p='PROME/proposals/2026-11-06_wq700b-options.md'; r=row(ptr=p); (root/'PROME/WILL_QUEUE.md').write_text(queue([r])); (root/p).write_text(options(r,CHAT))
def rowtext(root):
    r=row(q='Should X happen, now covering a held position trade?',ptr=None); (root/'PROME/WILL_QUEUE.md').write_text(queue([r]))
def inplace(root):
    r=row(); (root/OPT).write_text(options(r,CHAT))
def recchange(root):
    r=row(); (root/OPT).write_text(options(r,APP,rec='B'))
case('newsource-chat',newsrc)
case('row-reworded',rowtext)
case('row-closed',closed)
case('inplace-chat-after-ruling',inplace,ruling_first=True)
case('inplace-chat-before-ruling',inplace)
case('rec-changed-after-ruling',recchange,ruling_first=True)
case('blocked-after-ruling',blocked,ruling_first=True)
