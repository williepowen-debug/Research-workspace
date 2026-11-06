
import sys,os,json;sys.dont_write_bytecode=True;sys.path.insert(0,'/tmp/wq641-rev/fx/f/AGENTS/CATO/prototypes/decisions/mvp')
import notification_hook as nh,notifications as no
from pathlib import Path
s=sys.argv[1];ev=sys.argv[2];life=float(sys.argv[3]);par=json.loads(sys.argv[4])
print(s,ev,'exit',nh.run({'cwd':'/tmp/wq641-rev/fx/f/PROME','session_id':s,'hook_event_name':ev},Path('/tmp/wq641-rev/fx/f'),Path('/tmp/wq641-rev/fx/f/.st'),parent=par,poll=.3,lifetime=life,interactive=True),flush=True)
