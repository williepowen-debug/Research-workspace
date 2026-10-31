"""Native Chrome checks over captured live data; simulated refresh changes only."""
import copy
import html
import json
import re
import shutil
import subprocess
import tempfile
import threading
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from unittest.mock import patch

import app
import reader

CHECKS = r'''<script>(async()=>{
const checks=[];const assert=(v,m)=>{if(!v)throw Error(m)};
async function check(name,fn){try{await fn();checks.push({name,pass:true})}catch(e){checks.push({name,pass:false,error:String(e)})}}
for(let n=0;!data&&n<200;n++)await new Promise(r=>setTimeout(r,50));
const initialData=JSON.parse(JSON.stringify(data));
await check('Live sources loaded with housekeeping hidden and unclassified visible',()=>{assert(data,'no data');assert(mode==='day'&&selected===data.today,'agenda must start on today');assert(document.querySelectorAll('.week-pick').length===7,'week strip');assert(data.coverage.length===10,'coverage');assert(!active.has('housekeeping')&&active.has('unclassified'),'layers');assert(data.events.some(e=>e.layer==='unclassified'),'missing unclassified inventory')});
week='2026-11-02';selected=week;mode='day';render();
await check('Agenda details stay alongside on desktop and become modal on narrow screens',()=>{assert($('board').className==='agenda','agenda');assert(document.querySelectorAll('#board .day').length===1,'one selected day');const e=data.events.find(e=>e.id==='ism-m');assert(e,'reviewed release');const scroll=window.scrollY;openDetail(e.id);assert($('detail').open&&$('detail-body').textContent.includes('Source records captured'),'evidence');assert($('detail').matches(':modal')===narrow.matches,'responsive detail mode');if(!narrow.matches){assert($('detail').getBoundingClientRect().left>$('board').getBoundingClientRect().left,'right panel');assert(window.scrollY===scroll,'agenda moved')}closeDetail()});
await check('Week strip counts and keyboard-accessible day selection match the agenda',()=>{const button=document.querySelector('[data-day="2026-11-06"]');assert(button.tagName==='BUTTON','day is not keyboard accessible');button.click();assert(selected==='2026-11-06'&&mode==='day','day selection');assert(Number($('agenda-count').textContent.split(' ')[0])===daily(selected).length,'count');assert(document.querySelector('.week-pick[aria-pressed="true"]').dataset.day===selected,'selection');chooseDay('2026-11-02')});
await check('Week Grid remains available and returns to the selected agenda',()=>{$('week-mode').click();assert(document.querySelectorAll('#board .day').length===7,'week grid');document.querySelector('#board [data-day="2026-11-03"]').click();assert(mode==='day'&&selected==='2026-11-03','grid day handoff');chooseDay('2026-11-02')});
await check('Unclassified work is accessible separately without crowding the day agenda',()=>{assert(![...$('board').querySelectorAll('.card')].some(c=>data.events.find(e=>e.id===c.dataset.id).layer==='unclassified'),'unclassified in agenda');const rail=$('inventory-unclassified');assert(!rail.open,'not collapsed by default');assert(rail.querySelectorAll('.card').length===data.events.filter(e=>e.layer==='unclassified'&&filtered(e)).length,'missing unknown records');rail.querySelector('summary').click();assert(rail.open,'inventory toggle');query='unlikely-match-777';render();assert($('inventory-unclassified').open&&$('inventory-unclassified').querySelector('.count').textContent==='0','expanded/filter state');query='';render();$('inventory-unclassified').open=false});
await check('Navigation moves week without claiming complete coverage',()=>{$('next').click();assert(week==='2026-11-09','next');$('prev').click();assert(week==='2026-11-02','previous');assert($('coverage-body').textContent.includes('outside coverage'),'coverage limit')});
await check('Search and owner filtering narrow actual records',()=>{query='unlikely-match-777';render();assert(!$('board').querySelector('.card'),'search');query='';owner=data.events.find(e=>e.date==='2026-11-02'&&e.layer!=='unclassified').owner;render();assert([...$('board').querySelectorAll('.card')].every(c=>data.events.find(e=>e.id===c.dataset.id).owner===owner),'owner');owner='';render()});
await check('Housekeeping toggle exposes reviewed rows',()=>{const before=$('visible-count').textContent;document.querySelector('[data-layer="housekeeping"]').click();assert(active.has('housekeeping'),'toggle');assert($('visible-count').textContent==='Housekeeping included.','count');document.querySelector('[data-layer="housekeeping"]').click();assert(before===$('visible-count').textContent,'restore')});
await check('Timing inventory does not invent dated grid events',()=>{for(const e of data.events.filter(e=>['uncertain','undated','window'].includes(e.lane)))assert(!$('board').querySelector(`[data-id="${CSS.escape(e.id)}"]`),'timing placed in day grid')});
await check('Source text is escaped in cards and details',()=>{let e=data.events[0];let original=e.title;e.title='<img src=x onerror="window.badCalendar=true">';week=monday(e.date||data.today);selected=week;render();openDetail(e.id);assert(!$('detail-title').querySelector('img')&&!window.badCalendar,'HTML executed');$('close').click();e.title=original;week='2026-11-02';selected=week;render()});
await check('Refresh moves an event and updates the selected detail',async()=>{openDetail('ism-m');await refresh();assert(detailId==='ism-m'&&$('detail').open,'selection lost');closeDetail();assert(data.events.some(e=>e.id==='ism-m'&&e.date==='2026-11-03'),'new date');assert(!$('board').querySelector('[data-date="2026-11-02"] [data-id="ism-m"]'),'old date retained')});
await check('Failed refresh keeps last view with explicit warning',async()=>{const old=data.refreshed_at;await refresh();assert(lastFailure&&data.refreshed_at===old,'lost last view');assert($('status').textContent.includes('Refresh failed'),'missing warning')});
await check('Unavailable source and stale source remain visible',async()=>{await refresh();assert($('status').textContent.includes('unavailable')&&$('status').textContent.includes('STALE:'),'missing warnings');assert($('coverage-body').textContent.includes('unavailable'),'missing inventory')});
await check('No research launch or source mutation controls',()=>{assert(![...document.querySelectorAll('button')].some(b=>/^(start|launch|save|deliver)\b/i.test(b.textContent.trim())),'mutation offered')});
await check('Desktop and narrow viewport fit',()=>{assert(document.documentElement.scrollWidth<=innerWidth,'overflow '+document.documentElement.scrollWidth+' / '+innerWidth)});
data=initialData;lastFailure='';week='2026-11-02';selected=week;mode='day';detailId='';render();if(!narrow.matches)openDetail('ism-m');
const out=document.createElement('pre');out.hidden=true;out.id='test-results';out.textContent=JSON.stringify(checks);document.body.append(out);
})();</script>'''


def windows(path):
    return subprocess.check_output(['wslpath', '-w', str(path)], text=True).strip()


def main():
    captured = reader.snapshot()
    work = Path(tempfile.mkdtemp(prefix='cato-calendar-live-', dir='/mnt/c/Users/willi/AppData/Local/Temp'))
    results = []
    for label, size in [('desktop', '1520,1140'), ('narrow', '600,1100')]:
        calls = [0]
        def fixture(*_):
            calls[0] += 1
            data = copy.deepcopy(captured)
            if calls[0] >= 2:
                next(e for e in data['events'] if e['id'] == 'ism-m')['date'] = '2026-11-03'
            if calls[0] >= 3:
                data['coverage'][0].update(status='unavailable', warnings=['Fixture: missing source', 'STALE: fixture evidence deadline passed'])
            return data
        server = app.make_server()
        original = server.RequestHandlerClass
        class Handler(original):
            def do_GET(self):
                if self.path == '/':
                    body = (reader.HERE / 'index.html').read_text().replace('</body>', CHECKS + '</body>')
                    return self.reply(200, body.encode(), 'text/html')
                if self.path == '/api/calendar' and calls[0] == 2:
                    calls[0] += 1
                    return self.reply(503, b'fixture refresh failure', 'text/plain')
                return super().do_GET()
        server.RequestHandlerClass = Handler
        with patch.object(app, 'snapshot', fixture):
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            url = f'http://127.0.0.1:{server.server_port}/'
            probe = subprocess.run(['/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe', '-NoProfile', '-NonInteractive', '-Command', f"$u='{url}health';for($i=0;$i -lt 30;$i++){{try{{Invoke-WebRequest -UseBasicParsing -TimeoutSec 2 $u | Out-Null;exit 0}}catch{{Start-Sleep -Milliseconds 250}}}};exit 1"], capture_output=True, timeout=50)
            if probe.returncode:
                raise RuntimeError('Windows localhost forwarding unavailable')
            screenshot = work / (label + '.png')
            command = ['/mnt/c/Program Files/Google/Chrome/Application/chrome.exe', '--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check', '--disable-background-networking', '--disable-extensions', '--disable-sync', '--hide-scrollbars', '--user-data-dir=' + windows(work / (label + '-profile')), '--window-size=' + size, '--virtual-time-budget=18000', '--screenshot=' + windows(screenshot), '--dump-dom', url]
            run = subprocess.run(command, capture_output=True, timeout=55)
            output = run.stdout.decode(errors='replace')
            match = re.search(r'<pre hidden="" id="test-results">(.*?)</pre>', output, re.S)
            checks = json.loads(html.unescape(match[1])) if match else [{'name': 'Browser completion', 'pass': False, 'error': run.stderr.decode(errors='replace')[-700:]}]
            for path, headers, method in [('/source?path=../../.ssh/config', {}, 'GET'), ('/api/calendar', {'Origin': 'https://example.invalid'}, 'GET'), ('/api/calendar', {}, 'POST')]:
                try:
                    urlopen(Request(url.rstrip('/') + path, headers=headers, method=method), timeout=5)
                    checks.append({'name': 'HTTP read-only boundary ' + path + method, 'pass': False})
                except HTTPError as error:
                    checks.append({'name': 'HTTP read-only boundary ' + path + method, 'pass': error.code in {403, 404, 501}})
            server.shutdown()
            server.server_close()
        (work / (label + '.html')).write_text(output)
        if screenshot.exists():
            shutil.copyfile(screenshot, reader.HERE / (label + '.png'))
        results.append(dict(viewport=label, checks=checks))
        print(label, json.dumps(checks), flush=True)
    (reader.HERE / 'browser-checks.json').write_text(json.dumps({'kind': 'Author checks; captured live inputs, simulated refresh changes/failures; no source writes', 'work': str(work), 'runs': results}, indent=2) + '\n')
    return int(any(not c['pass'] for r in results for c in r['checks']))


if __name__ == '__main__':
    raise SystemExit(main())
