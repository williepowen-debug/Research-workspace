#!/usr/bin/env python3
"""Native Windows Chrome: isolated author fixture, then actual read-only history."""
import html
import json
from pathlib import Path
import re
import subprocess
import tempfile
import threading
from unittest.mock import patch

import app
import test_desk
import test_desk_review
import delivery
from pilot_files import Repo
from server import make_server
from store import HERE, reader

CHECKS = r'''<script>
(async()=>{
const results=[];
function assert(v,why){if(!v)throw Error(why);}
async function check(name,fn){try{await fn();results.push({name,pass:true});}catch(e){results.push({name,pass:false,error:e.message});}}
for(let i=0;!model&&i<100;i++)await new Promise(r=>setTimeout(r,50));
await check('Verdict buttons require unambiguous scope; options use explicit choices',()=>{assert(model&&!model.errors.length,'desk errors');assert(model.cards.length===3,'fixture cards');assert(!document.querySelector('[data-unit="901.queue"] [data-verdict="approve"]'),'options row silently approved');const a=document.querySelector('[data-unit="903.queue"]');assert(a.querySelector('[data-verdict="approve"]')&&a.querySelector('[data-verdict="disapprove"]'),'missing scoped verdict controls');});
await check('Verdict changes preserve conditions without carrying old verdicts',async()=>{const c=model.cards.find(c=>c.wq_id==='903');openVerdict(c,true);assert(!$('note').value,'recommendation copied into answer');$('review').click();assert($('reply-status').textContent.includes('specific decision'),'blank scope accepted');$('verdict-scope').value='Send one digest';$('note').value='Only after my review.';remember();$('cancel').click();openVerdict(c,false);$('review').click();assert(pending.note==='I disapprove: Send one digest\n\nConditions: Only after my review.','old verdict or lost conditions');$('back').click();$('cancel').click();openReply(c);assert(verdict===null&&!$('note').value.includes('I disapprove'),'Other response retained verdict');$('cancel').click();openVerdict(c,true);$('note').value='I disapprove of the side task';remember();$('review').click();assert($('reply-status').textContent.includes('both approve and disapprove'),'contradictory response accepted');$('note').value='Only after my review.';remember();$('review').click();assert(pending.note.startsWith('I approve: Send one digest'),'wrong final verdict');assert(!pending.note.includes('Side obligation'),'approved side note');await save(false);assert(model.cards.find(c=>c.wq_id==='903').last.request.note.startsWith('I approve: Send one digest'),'saved scope lost');view='Decisions';render();});
await check('Review shows exact words, and cancel keeps draft',()=>{openReply(model.cards.find(c=>c.wq_id==='901'));assert(!chosen,'choice preselected');$('review').click();assert($('reply-status').textContent.includes('Choose an option'),'unselected choice accepted');document.querySelector('[data-choice="B"]').click();$('note').value='A, only if the condition remains.\nNo new schedule.';$('note').oninput();$('review').click();assert($('review-body').textContent.includes('B · Decline'),'review lost selected option');assert($('review-body').textContent.includes('Do not do this task.'),'review lost meaning');assert($('review-body').textContent.includes('No new schedule.'),'review lost words');assert($('review-body').textContent.includes('Exact caveat'),'review lost terms');$('back').click();assert($('note').value.includes('No new schedule.'),'draft lost');});
await check('Save local survives refresh with no invented receipt',async()=>{$('review').click();await save(false);assert(view==='Follow-through','wrong view');const c=model.cards.find(c=>c.wq_id==='901');assert(c.last.request.note.includes('No new schedule.'),'saved words lost');assert(c.last.selected_choice.id==='B','selected option lost');assert(!c.receipt,'false receipt');assert($('cards').textContent.includes('safely saved'),'save not explained');await load();assert(model.cards.find(c=>c.wq_id==='901').last,'refresh lost answer');});
await check('Explicit Send publishes saved fixture response without inventing receipt',async()=>{const c=model.cards.find(c=>c.wq_id==='901');await deliver(c.last.id);const sent=model.cards.find(c=>c.wq_id==='901');assert(sent.delivery==='delivered','delivery not confirmed');assert(!sent.receipt,'send invented owner acknowledgment');});
await check('Recent rulings preserve answer time, write time and corrections as text',()=>{view='History';render();const a=document.querySelector('[data-ruling]');assert(a.textContent.includes('21:13 ET')&&a.textContent.includes('21:14 ET'),'timestamps lost');assert(a.textContent.includes('Correction: earlier time was write time.'),'correction lost');assert(!a.querySelector('img'),'ruling interpreted as HTML');});
await check('Task deferral keeps its return condition',async()=>{view='Tasks for me';render();openReply(model.cards.find(c=>c.wq_id==='902'));$('action').value='defer';$('action').onchange();$('note').value='Waiting for corrected report';$('revisit').value='After the next filing';remember();$('review').click();await save(false);assert(model.cards.find(c=>c.wq_id==='902').last.request.revisit==='After the next filing','lost return condition');});
await check('Layout fits the viewport',()=>{assert(document.documentElement.scrollWidth<=innerWidth,'horizontal overflow');});
const out=document.createElement('pre');out.id='test-results';out.hidden=true;out.textContent=JSON.stringify(results);document.body.append(out);
})();</script>'''
HISTORY = r'''<script>(async()=>{for(let i=0;!model&&i<100;i++)await new Promise(r=>setTimeout(r,50));view='History';render();const c=model.cards.find(c=>c.wq_id==='558');const checks=[{name:'Real saved A and integrated receipt visible',pass:!!c&&c.receipt?.state==='integrated'&&c.last.selected_choice?.id==='A'},{name:'Owner implementation shown separately',pass:!!c?.completion},{name:'Closed history has no response controls',pass:!document.querySelector('#cards button')},{name:'Real ruling correction keeps both answer and write times',pass:(model.rulings?.records||[]).some(r=>r.text.includes('WQ-561 RULED A')&&r.text.includes('21:13')&&r.text.includes('21:14'))},{name:'Saved time and receipt time are distinct labels',pass:$('cards').textContent.includes('receipt time, not your answer time')},{name:'Layout fits viewport',pass:document.documentElement.scrollWidth<=innerWidth}];const out=document.createElement('pre');out.id='test-results';out.hidden=true;out.textContent=JSON.stringify(checks);document.body.append(out);})();</script>'''

REPAIR_HISTORY = r'''<script>(async()=>{for(let i=0;!model&&i<150;i++)await new Promise(r=>setTimeout(r,50));view='History';render();const c=model.cards.find(c=>c.wq_id==='901');const a=document.querySelector('[data-unit="901.queue"]');const checks=[{name:'Recorded words belong to receipt event A',pass:c?.last.request.note==='Send digests'&&c.receipt.response_id===c.last.id&&a.textContent.includes('Answer recorded by PROME')},{name:'Opposite unsent B remains visible and separately labelled',pass:a.textContent.includes('Do not send digests')&&a.textContent.includes('Other saved answers — not the answer recorded above')&&a.textContent.includes('Delivery: saved')},{name:'Closed question offers no delivery or response controls',pass:!a.querySelector('button')},{name:'Saved answer terms retained separately',pass:a.textContent.includes('Exact terms saved with this answer')}];const out=document.createElement('pre');out.id='test-results';out.hidden=true;out.textContent=JSON.stringify(checks);document.body.append(out);})();</script>'''


def windows(path):
    return subprocess.check_output(["wslpath", "-w", str(path)], text=True).strip()


def run_browser(desk, script, work, label, width):
    server = make_server(desk)
    original = server.RequestHandlerClass.send
    def send(handler, status, value, mime="application/json"):
        if mime == "text/html" and handler.path == "/":
            value = value.replace("</body>", script + "</body>")
        return original(handler, status, value, mime)
    server.RequestHandlerClass.send = send
    thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
    try:
        url = f"http://127.0.0.1:{server.server_port}/"
        probe = subprocess.run([app.POWERSHELL, "-NoProfile", "-Command",
            f"$u='{url}api/display'; for($i=0;$i -lt 30;$i++){{try{{Invoke-WebRequest -UseBasicParsing -TimeoutSec 2 $u | Out-Null;exit 0}}catch{{Start-Sleep -Milliseconds 250}}}};exit 1"],
            capture_output=True, timeout=50)
        if probe.returncode: raise RuntimeError("Windows HTTP probe failed")
        screenshot = work / (label + ".png")
        cmd = ["/mnt/c/Program Files/Google/Chrome/Application/chrome.exe", "--headless=new", "--disable-gpu",
               "--no-first-run", "--no-default-browser-check", "--disable-background-networking", "--disable-extensions",
               "--disable-sync", "--hide-scrollbars", "--user-data-dir=" + windows(work / (label + "-profile")),
               f"--window-size={width},1100", "--virtual-time-budget=15000", "--screenshot=" + windows(screenshot),
               "--dump-dom", url]
        result = subprocess.run(cmd, capture_output=True, timeout=70)
        dom = result.stdout.decode("utf-8")
        (work / (label + ".html")).write_text(dom)
        match = re.search(r'<pre id="test-results" hidden="">(.*?)</pre>', dom, re.S)
        if not match: raise RuntimeError("No browser result: " + str(work))
        checks = json.loads(html.unescape(match[1]))
        print(label, json.dumps(checks), flush=True)
        return {"checks": checks, "screenshot": str(screenshot)}
    finally:
        server.shutdown(); server.server_close(); thread.join(timeout=5)


def main():
    work = Path(tempfile.mkdtemp(prefix="cato-desk-", dir="/mnt/c/Users/willi/AppData/Local/Temp"))
    runs = {}
    for label, width in [("desktop", 1440), ("narrow", 620)]:
        fixture = test_desk.DeskTests(methodName="test_reuses_owner_parser_and_preserves_literal_pipe_and_words")
        fixture.setUp()
        try:
            fixture.text = fixture.text.replace('## RECENTLY DONE', '| 903 | Send a digest? | DECISION | 2026-11-06 | 10/30 | Send one digest. Side obligation stays with another desk. | Preserve conditions |\n\n## RECENTLY DONE')
            fixture.put('PROME/WILL_QUEUE.md', fixture.text)
            fixture.commit(publish=True)
            fixture.install_options()
            fixture.put('PROME/proposals/2026-10-30_wq901-RULED.md', '# Fixture recorded decision\n\nWill said B at 21:13 ET. Recorded at 21:14 ET.\n\nCorrection: earlier time was write time. <img src=x onerror=alert(1)>\n')
            fixture.commit(publish=True)
            with patch("app.accepted", return_value=(True, "")):
                desk = app.Desk(fixture.repo, Path(fixture.tmp.name) / "browser", True)
                runs[label] = run_browser(desk, CHECKS, work, label, width)
        finally:
            fixture.doCleanups()
    fixture = test_desk_review.ReviewTests(methodName="test_recorded_answer_is_receipt_event_and_later_answer_cannot_send")
    fixture.setUp()
    try:
        a = fixture.store.save(fixture.request(note='Send digests'))
        delivery.deliver(fixture.repo, a)
        fixture.store.save(fixture.request(note='Do not send digests', supersedes=a['id']))
        fixture.integrate(a, close=True)
        with patch("app.accepted", return_value=(True, "")):
            desk = app.Desk(fixture.repo, Path(fixture.tmp.name) / 'review-browser', True)
            desk.stores['901'] = fixture.store
            runs['recorded-answer'] = run_browser(desk, REPAIR_HISTORY, work, 'recorded-answer', 1440)
    finally:
        fixture.doCleanups()
    with tempfile.TemporaryDirectory() as tmp:
        desk = app.Desk(Repo(reader.ROOT), Path(tmp), False)
        runs["actual-history"] = run_browser(desk, HISTORY, work, "actual-history", 1440)
    receipt = {"kind": "Decisions author browser evidence; fixture writes only; actual history read-only",
               "runs": runs, "build_hashes": app.build_hashes(), "work_directory": str(work)}
    (HERE / "desk-validation.json").write_text(json.dumps(receipt, indent=2) + "\n")
    if any(not c["pass"] for r in runs.values() for c in r["checks"]):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
