import sys,threading,time,io,contextlib,subprocess,os; sys.path.insert(0,'/tmp/wq638-rev/scripts')
from fxlib import *
root=build('s4'); qs,ow,dl,au,no,pf=load(root); repo=qs.Repo(root)
import app, notification_hook as nh
state=root/'.state'; state.mkdir(exist_ok=True)
N=no.Notifications(state)
print('initial',N.status()['state'])
e=answer(root,qs,repo)
attempt('enqueue unpublished',lambda:N.enqueue(repo,e))
publish(root,dl,e); print('enqueue pub',N.enqueue(repo,e)['state'])
# a superseding answer: old notice?
e2=answer(root,qs,repo,action='reply',choice=None,note='changed'); publish(root,dl,e2); N.enqueue(repo,e2)
print('e,e2',e['id'][:6],e2['id'][:6],'pending',[(n['id'][:6],n['queued']) for n in N.pending('S1')])
# Run hook w/ fake parent = this python
me=no.process_identity(os.getpid())
def fire(session,ev='SessionStart',cwd=root/'PROME',**k):
    err=io.StringIO()
    with contextlib.redirect_stderr(err):
        r=nh.run({'cwd':str(cwd),'session_id':session,'hook_event_name':ev},root,state,parent=me,poll=0.2,lifetime=2,**k)
    return r,err.getvalue()
print('wrong cwd',fire('S1',cwd=root))
print('fire S1',fire('S1'))
print('fire S1 again (no new)',fire('S1')[0],N.status()['state'])
print('new session S2 re-alert',fire('S2')[0])
# receipt/integration on e2; desk ack only if app display runs; old notice e never acked
r=ow.write_received(repo,e2); push(root,'recv')
class D(app.Desk): pass
d=app.Desk(repo,state,enable_responses=False); m=d.display(); print('display errors',m['errors'][:2],'notification',m['notification']['state'])
print('after display pending for S3',[(n['id']==e['id'],n['id']==e2['id']) for n in N.pending('S3')])
# 25 pending ordering/starve simulation skipped
# End then parent-live: session end while listener
N.heartbeat('S9',no.process_identity(os.getpid()),starting=True); N.end('S9'); print('after end',N.status())
# /clear: watcher for A holds lock, SessionEnd(A) + SessionStart(B) at once
res={}
def w():
    res['a']=nh.run({'cwd':str(root/'PROME'),'session_id':'A','hook_event_name':'SessionStart'},root,state,parent=me,poll=0.3,lifetime=3)
t=threading.Thread(target=w); 
# new state w/o notices
import tempfile
state2=root/'.state2'; N2=no.Notifications(state2)
def w2():
    res['a']=nh.run({'cwd':str(root/'PROME'),'session_id':'A','hook_event_name':'SessionStart'},root,state2,parent=me,poll=0.3,lifetime=3)
t=threading.Thread(target=w2); t.start(); time.sleep(0.5)
print('A',N2.status()['state'])
print('end A',nh.run({'cwd':str(root/'PROME'),'session_id':'A','hook_event_name':'SessionEnd'},root,state2,parent=me))
print('start B',subprocess.run([sys.executable,'-c',f"""
import sys,os;sys.dont_write_bytecode=True;sys.path.insert(0,{str(root/'AGENTS/CATO/prototypes/decisions/mvp')!r})
import notification_hook as nh,notifications as no
from pathlib import Path
print(nh.run({{'cwd':{str(root/'PROME')!r},'session_id':'B','hook_event_name':'SessionStart'}},Path({str(root)!r}),Path({str(state2)!r}),parent=no.process_identity(os.getppid()),poll=0.3,lifetime=1))
"""],capture_output=True,text=True).stdout.strip())
print('status after /clear-like',N2.status()); t.join(); print('final',N2.status()['state'])

# malformed confirmation takes down the whole desk display?
r=row(n='701',ptr='PROME/proposals/bad-options.md')
bad=options(r,{'mode':['app'],'scope':'reversible_internal','reason':'x'},n=701)
(root/'PROME/proposals/bad-options.md').write_text(bad)
t=(root/'PROME/WILL_QUEUE.md').read_text().replace('\n\n## CLOSED','\n'+r+'\n\n## CLOSED'); (root/'PROME/WILL_QUEUE.md').write_text(t); push(root,'bad')
d=app.Desk(repo,state,enable_responses=False)
attempt('desk display with malformed mode',lambda:len(d.display()['cards']))
