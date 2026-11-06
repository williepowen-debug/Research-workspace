import sys,json,os,stat,uuid; sys.path.insert(0,'/tmp/wq641-rev')
from fx1 import *
sys.dont_write_bytecode=True
def setup(name,policy=APP,version=2,**acc):
    root=build(name,policy,version)
    for f in (root/'scripts/githooks').iterdir():
        if f.is_file(): f.write_text('#!/bin/sh\nexit 0\n')
    sh(root,'config','core.hooksPath','scripts/githooks')
    (root/'PROME/decisions/review.md').write_text('fixture review\n'); c=push(root,'review')
    mods=load(root); qs,ow,dl,au,no,pf=mods
    import app
    repo=qs.Repo(root)
    return root,repo,app,mods,c
def accept(root,app,c,**over):
    a={'schema_version':'decisions-app-acceptance/1','queue_responses':True,'matching_chat_confirmation':True,'confirmation_policy':'explicit-reversible-internal/1',
       'build_hashes':app.build_hashes(),'independent_review':{'path':'PROME/decisions/review.md','commit':c}}
    a.update(over)
    for k in [k for k,v in a.items() if v=='__absent__']: del a[k]
    (root/app.ACCEPTANCE).write_text(json.dumps(a)); return push(root,'accept')
ON={'app_only_enabled':True,'app_only_since':'2026-01-01T00:00:00+00:00'}
OFF={'app_only_enabled':False}
def recv(root,ow,repo,e):
    ow.write_received(repo,e); push(root,'recv')
