from fx2 import *
# enablement matrix
root,repo,app,(qs,ow,dl,au,no,pf),c=setup('b'); accept(root,app,c,**ON)
e=answer(root,qs,repo); publish(root,dl,e); recv(root,ow,repo,e); p,cc=ruled(root,e,au)
ref={'path':p,'commit':cc}
matrix={'absent':{'app_only_enabled':'__absent__','app_only_since':'__absent__'},'false':{'app_only_enabled':False,'app_only_since':'2026-01-01T00:00:00+00:00'},
 'string-true':{'app_only_enabled':'true','app_only_since':'2026-01-01T00:00:00+00:00'},'one':{'app_only_enabled':1,'app_only_since':'2026-01-01T00:00:00+00:00'},
 'no-since':{'app_only_enabled':True},'null-since':{'app_only_enabled':True,'app_only_since':None},'naive':{'app_only_enabled':True,'app_only_since':'2026-01-01T00:00:00'},
 'garbage':{'app_only_enabled':True,'app_only_since':'soon'},'future':{'app_only_enabled':True,'app_only_since':'2099-01-01T00:00:00+00:00'},
 'after-answer':{'app_only_enabled':True,'app_only_since':datetime.now(timezone.utc).isoformat()}}
for k,v in matrix.items():
    accept(root,app,c,**v)
    d=app.Desk(repo,root/'.deskb',True); card=next(x for x in d.display()['cards'] if x['wq_id']=='700')
    print(k,'| enabled',au.app_only_enabled(repo,e),'| inspect chat',ow.inspect_event(repo,e).get('requires_chat_confirmation'),'| desk chat',card['requires_confirmation'],end=' | ')
    attempt('prepare',lambda:ow.prepare(repo,e,'integrated',ref,None,app_only=True))
accept(root,app,c,**ON)
(root/app.ACCEPTANCE).write_text((root/app.ACCEPTANCE).read_text().replace('"app_only_since"','"app_only_since" ')); print('dirty local acceptance enabled:',au.app_only_enabled(repo,e)); sh(root,'checkout','--',app.ACCEPTANCE)
# broken accepted(): hash drift with app_only true
(root/'AGENTS/CATO/prototypes/decisions/mvp/desk.html').write_text((root/'AGENTS/CATO/prototypes/decisions/mvp/desk.html').read_text()+'\n'); push(root,'drift')
print('build drift enabled:',au.app_only_enabled(repo,e))
