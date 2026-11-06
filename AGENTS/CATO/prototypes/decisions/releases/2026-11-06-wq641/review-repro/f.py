from fx2 import *
import subprocess,time,pty,threading
root,repo,app,(qs,ow,dl,au,no,pf),c=setup('f')
def probe(args,tty=True):
    m,s=pty.openpty()
    p=subprocess.Popen(['python3','-c','import time;time.sleep(4)']+args,stdin=s if tty else subprocess.DEVNULL,stdout=subprocess.DEVNULL)
    time.sleep(.2); i=no.process_identity(p.pid); r=no.interactive_parent(i); p.kill(); p.wait(); os.close(m); os.close(s); return r
for label,args,tty in [('plain tty',[],True),('--resume tty',['--resume'],True),('--model tty',['--model','opus','--','do it'],True),('-p tty',['-p','hi'],True),('--print tty',['--print','hi'],True),('--print=x',['--print=x'],True),('-dp',['-dp','hi'],True),('devnull',[],False),('prompt with dash p after --',['--','-p is a word'],True)]:
    print(label,probe(args,tty))
print('missing pid',no.interactive_parent({'pid':999999}),'none',no.interactive_parent(None) if False else '')
state=root/'.st'; st=str(state); N=no.Notifications(state)
tmpl=f"""
import sys,os,json;sys.dont_write_bytecode=True;sys.path.insert(0,{str(root/'AGENTS/CATO/prototypes/decisions/mvp')!r})
import notification_hook as nh,notifications as no
from pathlib import Path
s=sys.argv[1];ev=sys.argv[2];life=float(sys.argv[3]);par=json.loads(sys.argv[4])
print(s,ev,'exit',nh.run({{'cwd':{str(root/'PROME')!r},'session_id':s,'hook_event_name':ev}},Path({str(root)!r}),Path({st!r}),parent=par,poll=.3,lifetime=life,interactive=True),flush=True)
"""
open('/tmp/wq641-rev/w.py','w').write(tmpl)
par=json.dumps(no.process_identity(os.getpid()))
def go(s,ev,life=6): return subprocess.Popen([sys.executable,'/tmp/wq641-rev/w.py',s,ev,str(life),par],text=True)
def row_():
    import sqlite3
    d=sqlite3.connect(state/'notifications.sqlite3'); return d.execute('select session,beat>0,ended from listener').fetchall()
a=go('A','SessionStart',8); time.sleep(1); print('A',N.status()['state'],row_())
p=go('X','PostToolUse',1); p.wait(); print('foreign PostToolUse no steal',row_())
p=go('A','PostToolUse',1); p.wait(); print('same session rearm no dup',row_())
b=go('B','SessionStart',6); time.sleep(.2); print('B claimed',N.status()['state'],row_())
p=go('A','SessionEnd'); p.wait(); print('old end no effect',row_())
time.sleep(1.5); print('after handover',N.status()['state'],row_(),'A exited',a.poll())
p=go('B','SessionEnd'); p.wait(); print('B end',N.status()['state'],row_())
# heartbeat by stale identity
print('stale hb',N.heartbeat('B',no.process_identity(os.getpid())))
b.wait(); 
# clear order: end A then start B immediately
a=go('C','SessionStart',8); time.sleep(.8); p=go('C','SessionEnd'); p.wait(); b=go('D','SessionStart',4); time.sleep(1.2); print('clear-order',N.status()['state'],row_()); a.wait(); b.wait()
print('final',N.status()['state'])
