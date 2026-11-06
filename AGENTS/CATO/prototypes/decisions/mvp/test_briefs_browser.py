import sys,tempfile,json
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parent))
import app
from test_briefs import BriefTests
from test_desk_browser import run_browser
SCRIPT=r'''<script>(async()=>{
for(let i=0;!model&&i<150;i++)await new Promise(r=>setTimeout(r,50));
const checks=[];function check(name,f){try{if(!f())throw Error('assertion failed');checks.push({name,pass:true});}catch(e){checks.push({name,pass:false,error:e.message});}}
const c=model.cards.find(c=>c.wq_id==='901');const a=document.querySelector('[data-unit="901.queue"]');
check('Full short question shown without truncation',()=>a.querySelector('h2').textContent===c.brief.question);
check('Every important condition visible outside collapsed material',()=>c.brief.conditions.every(x=>[...a.querySelectorAll('.conditions li')].some(n=>n.textContent===x&&!n.closest('details'))));
check('Explanation appears once',()=>a.textContent.split(c.brief.what_changes).length===2);
check('Evidence collapsed and exact original available',()=>!a.querySelector('details').open&&a.textContent.includes(c.snapshot.queue_row));
check('Choices preserve meaning and consequence',()=>c.unit.proposal.choices.every(x=>a.textContent.includes(x.meaning)&&a.textContent.includes(x.consequence)));
check('No closed examples resurrected',()=>!model.cards.some(c=>['599','635'].includes(c.wq_id)));
check('Fits viewport',()=>document.documentElement.scrollWidth<=innerWidth);
openReply(c);check('Response review carries conditions',()=>c.brief.conditions.every(x=>$('reply-terms').textContent.includes(x)));
$('cancel').click();
c.brief.recommendation.status='NONE_YET';render();check('No recommendation is labelled accurately',()=>document.querySelector('[data-unit="901.queue"]').textContent.includes('No recommendation yet'));
c.brief=null;c.brief_notice='The short explanation is out of date. Read the full queue wording below before responding.';render();
check('Expired brief exposes full original context',()=>document.querySelector('[data-unit="901.queue"] details').open&&document.querySelector('[data-unit="901.queue"]').textContent.includes('Exact caveat'));
await load();
const out=document.createElement('pre');out.id='test-results';out.hidden=true;out.textContent=JSON.stringify(checks);document.body.append(out);
})();</script>'''
work=Path(tempfile.mkdtemp(prefix='cato-briefs-',dir='/mnt/c/Users/willi/AppData/Local/Temp'))
results={}
for label,width in [('brief-desktop',1440),('brief-narrow',620)]:
 fixture=BriefTests();fixture.setUp()
 try:
  with patch('app.accepted',return_value=(True,'')):
   desk=app.Desk(fixture.repo,Path(fixture.tmp.name)/'browser',True)
   results[label]=run_browser(desk,SCRIPT,work,label,width)
 finally:fixture.doCleanups()
Path('/tmp/cato-decisions-brief-browser-results.json').write_text(json.dumps(results,indent=2))
print('RESULT_FILE /tmp/cato-decisions-brief-browser-results.json')
raise SystemExit(0 if all(c['pass'] for run in results.values() for c in run['checks']) else 1)
