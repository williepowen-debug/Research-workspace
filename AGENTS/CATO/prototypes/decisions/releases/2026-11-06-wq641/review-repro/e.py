from fx2 import *
# malformed isolation and corruption
root,repo,app,(qs,ow,dl,au,no,pf),c=setup('e')
r2=row(q='Other?',n='701',ptr='PROME/proposals/o2.md',rec='Rec'); 
(root/'PROME/proposals/o2.md').write_text(options(r2,APP,n=701))
(root/'PROME/WILL_QUEUE.md').write_text(queue([row(),r2])); push(root,'two'); accept(root,app,c,**OFF)
e=answer(root,qs,repo); e1=e
good=(root/OPT).read_text()
def show(label):
    try:
        st=app.Desk(repo,root/'.state',True).display(); cards={x['wq_id']:x for x in st['cards']}
        print(label,'| errs',len(st['errors']),'src',len(st['source_errors']),'deliver',st['can_deliver'],{k:(v['can_respond'],v.get('can_deliver')) for k,v in cards.items()})
    except Exception as ex: print(label,'| DISPLAY RAISED',type(ex).__name__,str(ex)[:90])
show('clean')
bads={'mode-list':('"mode": "app"','"mode": ["app"]'),'scope-dict':('"scope": "reversible_internal"','"scope": {}'),'reason-int':('"reason": "Internal, reversible."','"reason": 5'),'conf-string':(None,None),'id-dict':('"id": "A"','"id": {}'),'wq-list':('"wq_id": 700','"wq_id": []'),'rec-list':('"recommended_choice_id": "A"','"recommended_choice_id": []'),'choices-str':(None,'c')}
import re
for k,(a,b) in bads.items():
    t=good
    if k=='conf-string': t=re.sub(r'"confirmation": \{.*?\}','"confirmation": "app"',good,flags=re.S)
    elif k=='choices-str': t=re.sub(r'"choices": \[.*?\],\n "recomm','"choices": "x",\n "recomm',good,flags=re.S)
    else: t=good.replace(a,b)
    assert t!=good,k
    (root/OPT).write_text(t); push(root,k); show(k)
    d=app.Desk(repo,root/'.state',True)
    st=d.display()
    attempt(k+' save on bad card',lambda:d.save({'id':uuid.uuid4().hex,'display_hash':'x','unit_id':'700.queue','action':'reply','choice_id':None,'note':'n','revisit':'','supersedes':None}))
    if k=='mode-list': attempt(k+' deliver saved on bad card',lambda:d.operate('/api/deliver',{'id':e['id']}))
(root/OPT).write_text(good); push(root,'restore'); show('restored')
R='AGENTS/CATO/decisions/queue-responses'
(root/R).mkdir(exist_ok=True)
ident='0'*31+'a'
def corrupt(label,body,path=None):
    p=root/(path or f'{R}/{ident}.json'); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(body); sh(root,'add','-f',str(p.relative_to(root))); push(root,label); show(label); p.unlink(); sh(root,'add','-A'); sh(root,'commit','-qm','x'); sh(root,'push','-q','origin','master'); sh(root,'fetch','-q')
corrupt('reply-not-json','{')
corrupt('reply-list','[]')
corrupt('reply-display-null','{"display":null}')
corrupt('reply-wq-int','{"display":{"record":{"wq_id":5}}}')
corrupt('reply-no-record','{"display":{}}')
ev=json.loads(pf.encoded(e)); ev['id']=ident; corrupt('reply-identified-badhash',json.dumps(ev))
corrupt('orphan-receipt','{}',path=f'PROME/decisions/receipts/{ident}/{"1"*32}.json')
corrupt('receipt-corrupt-on-real',('[]'),path=f"PROME/decisions/receipts/{e['id']}/{'1'*32}.json")
