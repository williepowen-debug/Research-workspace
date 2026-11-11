"""Opt-in native browser test. Fixtures only; never sends an operator answer."""
import json
from pathlib import Path
import tempfile
from unittest.mock import patch

import app
from pilot_files import Repo
from test_wq639 import CardTests
from test_desk_browser import run_browser

SCRIPT = r'''<script>(async()=>{
for(let i=0;!model&&i<150;i++)await new Promise(r=>setTimeout(r,50));
const checks=[];const check=(name,pass)=>checks.push({name,pass:!!pass});
let c=model.cards.find(c=>c.wq_id==='901');let a=document.querySelector('[data-unit="901.queue"]');
check('Versioned card shows exact question and choices',c.snapshot.kind==='decisions-queue-display/3'&&a.textContent.includes(c.unit.proposal.question)&&c.unit.proposal.choices.every(x=>a.textContent.includes(x.meaning)&&a.textContent.includes(x.consequence)));
check('Locked conditions visible',a.textContent.includes('Only after review.'));
check('Explicit recommended option enabled',recommendedChoice(c)?.id==='A'&&c.can_respond);
check('Matching chat confirmation retained',c.requires_confirmation&&a.textContent.includes('confirm this same answer'));
openReply(c);
check('Review keeps conditions',document.getElementById('reply-terms').textContent.includes('Only after review.'));
$('cancel').click();
check('No answer fabricated',!c.last);
check('Fits viewport',document.documentElement.scrollWidth<=innerWidth);
const out=document.createElement('pre');out.id='test-results';out.hidden=true;out.textContent=JSON.stringify(checks);document.body.append(out);
})();</script>'''
PILOT = r'''<script>(async()=>{
for(let i=0;!model&&i<150;i++)await new Promise(r=>setTimeout(r,50));
view='History';render();const c=model.cards.find(c=>c.wq_id==='558');const a=document.querySelector('[data-unit="558.L884"]');
const checks=[{name:'Real pilot has integrated receipt',pass:c?.receipt?.state==='integrated'},
{name:'No current clarification demand',pass:!!a&&!a.textContent.includes('PROME needs clarification')&&a.textContent.includes('No further answer is needed')},
{name:'No resend or answer button for recorded pilot',pass:!!a&&!a.querySelector('button')},
{name:'Exact saved history remains accessible',pass:a?.textContent.includes('Saved history and receipt')}];
const out=document.createElement('pre');out.id='test-results';out.hidden=true;out.textContent=JSON.stringify(checks);document.body.append(out);
})();</script>'''


def main():
    work=Path(tempfile.mkdtemp(prefix='cato-wq639-browser-',dir='/mnt/c/Users/willi/AppData/Local/Temp'))
    results={}
    for label,width in [('card-desktop',1440),('card-narrow',620)]:
        f=CardTests();f.setUp()
        try:
            f.install()
            with patch('app.accepted',return_value=(True,'')):
                desk=app.Desk(f.repo,Path(f.tmp.name)/'browser',True)
                results[label]=run_browser(desk,SCRIPT,work,label,width)
        finally:f.doCleanups()
    # Real published history, disposable local state, responses disabled.
    desk=app.Desk(Repo(Path('/home/willi/Research-workspace')),work/'real-preview',False)
    results['real-pilot']=run_browser(desk,PILOT,work,'real-pilot',1440)
    result=work/'results.json';result.write_text(json.dumps(results,indent=2))
    print('RESULT_FILE',result)
    return 0 if all(c['pass'] for run in results.values() for c in run['checks']) else 1

if __name__=='__main__':raise SystemExit(main())
