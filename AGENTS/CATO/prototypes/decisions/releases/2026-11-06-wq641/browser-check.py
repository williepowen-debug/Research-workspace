import sys,json
from pathlib import Path
sys.path.insert(0,'/tmp/cato-wq638/AGENTS/CATO/prototypes/decisions/mvp')
from test_wq638 import OptionATests
from test_desk_browser import run_browser
import app
f=OptionATests();f.setUp()
try:
 f.source();f.enable_app()
 acceptance=json.loads(f.repo.read(app.ACCEPTANCE));acceptance['app_only_enabled']=False
 f.put(app.ACCEPTANCE,json.dumps(acceptance));f.commit(publish=True)
 desk=app.Desk(f.repo,Path(f.tmp.name)/'browser',True)
 script='''<script>(async()=>{const sleep=ms=>new Promise(r=>setTimeout(r,ms));for(let i=0;i<100&&!model;i++)await sleep(100);const out={};try{const c=model.cards.find(c=>c.wq_id==='901');out.fallback=c.requires_confirmation===true;const a=document.querySelector('[data-unit="901.queue"]'),input=a.querySelector('textarea');input.value='Close it, but record the miss.\\nKeep this condition.';input.dispatchEvent(new Event('input'));a.querySelector('[data-recommendation="approve"]').click();$('review').click();out.approve=pending.choice_id==='A'&&pending.note===input.value;out.chatNotice=$('review-confirmation').textContent.includes('Chat confirmation required');$('review-dialog').close();openRecommendation(c,false);$('review').click();out.disapprove=pending.choice_id===null&&pending.note.endsWith(input.value);$('review-dialog').close();const original=api;let reply={...model,notification:{state:'offline',message:'Fixture offline'}};api=async(path,args)=>path==='/api/display'?reply:path==='/api/sync'?{message:'Fixture synced'}:original(path,args);$('global-status').textContent='Keep delivery message';await load(false);out.background=$('connection-status').textContent==='Fixture offline'&&$('global-status').textContent==='Keep delivery message';reply={...reply,notification:{state:'listening',message:'Fixture connected'}};await refreshConnection();out.focusedStatus=$('connection-status').textContent==='Fixture connected';reply={...reply,limit:'Fixture disabled',errors:['Fixture error'],notification:{state:'unknown',message:'Fixture unknown'}};await load();out.errorStatus=$('connection-status').textContent==='Fixture unknown';$('sync').click();await sleep(100);out.syncStatus=$('connection-status').textContent==='Fixture unknown';api=async()=>{throw Error('Fixture API failure')};await load(false);out.failedStatus=$('connection-status').textContent.includes('unknown');out.fits=document.documentElement.scrollWidth<=innerWidth;}catch(e){out.error=e.stack;}const p=document.createElement('pre');p.id='test-results';p.hidden=true;p.textContent=JSON.stringify(out);document.body.append(p);})();</script>'''
 work=Path('/mnt/c/Users/willi/AppData/Local/Temp/cato-wq641-browser');work.mkdir(exist_ok=True)
 r=run_browser(desk,script,work,'fallback-status',1440)
 print(json.dumps(r));assert all(v is True for v in r['checks'].values())
finally:f.doCleanups()
