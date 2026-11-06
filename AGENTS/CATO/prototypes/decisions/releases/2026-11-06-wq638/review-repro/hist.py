import sys,json
root=sys.argv[1]; sys.dont_write_bytecode=True
sys.path.insert(0,root+'/AGENTS/CATO/prototypes/decisions/mvp')
import owner_receipt as o, pilot_files as p
from store import reader
repo=p.Repo(reader.ROOT)
r=o.intake(repo)
print(json.dumps([{k:i.get(k) for k in('id','status','reason')} for i in r['items']],sort_keys=True))
