import sys,json,tempfile
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,'/tmp/cato-wq638/AGENTS/CATO/prototypes/decisions/mvp')
from test_wq638 import OptionATests
from test_desk_browser import run_browser
import app
f=OptionATests();f.setUp()
try:
 f.source()
 desk=app.Desk(f.repo,Path(f.tmp.name)/'browser',True)
 script='''<script>(async()=>{const sleep=ms=>new Promise(r=>setTimeout(r,ms));for(let i=0;i<100&&!model;i++)await sleep(100);const out={};try{const c=model.cards.find(c=>c.wq_id==='901');out.eligible=c.requires_confirmation===false;const article=document.querySelector('[data-unit="901.queue"]');const input=article.querySelector('textarea');input.value='Close it, but record the miss.\\nKeep this exact condition.';input.dispatchEvent(new Event('input'));article.querySelector('[data-recommendation="approve"]').click();document.querySelector('#review').click();out.approve=pending.choice_id==='A'&&pending.action==='choose'&&pending.note===input.value;out.noChat=document.querySelector('#review-confirmation').textContent.includes('No chat repeat');document.querySelector('#review-dialog').close();openRecommendation(c,false);document.querySelector('#review').click();out.disapprove=pending.choice_id===null&&pending.action==='reply'&&pending.note.includes('I disapprove: PROME’s recommendation A')&&pending.note.endsWith(input.value);document.querySelector('#review-dialog').close();out.fits=document.documentElement.scrollWidth<=innerWidth;}catch(e){out.error=e.stack;}const pre=document.createElement('pre');pre.id='test-results';pre.hidden=true;pre.textContent=JSON.stringify(out);document.body.append(pre);})();</script>'''
 work=Path('/mnt/c/Users/willi/AppData/Local/Temp/cato-wq638-browser');work.mkdir(exist_ok=True)
 with patch('app.accepted',return_value=(True,'')):
  result=run_browser(desk,script,work,'option-a',1440)
 print(json.dumps(result))
 if not result['checks'] or not all(v is True for v in result['checks'].values()):raise SystemExit(1)
finally:f.doCleanups()
