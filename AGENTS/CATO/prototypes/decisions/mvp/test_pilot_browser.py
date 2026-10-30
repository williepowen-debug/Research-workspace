#!/usr/bin/env python3
"""Candidate pilot UI against temporary repos only; native Windows Chrome / WSL."""
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess
import tempfile
import threading

from server import make_server
from store import HERE
from test_browser import windows
from test_pilot_files import PilotFileTests

CHECKS = r'''<script>
(async()=>{
 const results=[];
 function assert(ok,why){if(!ok)throw Error(why);}
 async function check(name,f){try{await f();results.push({name,pass:true});}catch(e){results.push({name,pass:false,error:e.message});}}
 for(let tries=0;!model&&tries<100;tries++)await new Promise(resolve=>setTimeout(resolve,50));
 await check('Pilot model labels supervised confirmation and four views',()=>{assert(model&&isPilot(),'pilot missing');assert(el('mode-intro').textContent.includes('matching confirmation'),'condition missing');assert(document.querySelectorAll('#nav button').length===5,'views missing');});
 if(model){
 const unit=model.snapshot.record.units[0];
 if('__PHASE__'==='write'){
  await check('Exact conditions survive review and cancel without a save',()=>{const d=draft(unit);d.note='One test only.\nNo schedule. <img src=x> stays text.';review(unit,d,null);assert(el('review-body').textContent.includes(d.note),'words changed');assert(!el('review-body').querySelector('img'),'executable text');el('cancel').click();assert(model.responses.events.length===0,'cancel saved');});
  await check('Save exports the complete response without a delivery claim',async()=>{review(unit,draft(unit),null);await el('save').onclick();assert(model.responses.events.length===1,'save missing');const event=model.responses.events[0];assert(event.kind==='decisions-response/1'&&!event.synthetic,'wrong dialect');assert(model.responses.delivery[event.id].includes('not committed'),'false delivery');assert(el('main').textContent.includes('No receiver acknowledgment'),'false receipt');});
  await check('Deferral keeps both answers and exact return condition',async()=>{const d=draft(unit);d.action='defer';d.revisit='After the new evidence';review(unit,d,latest(unit.id));await el('save').onclick();assert(model.responses.events.length===2,'history lost');const event=latest(unit.id);assert(event.selected_choice===null&&event.request.revisit==='After the new evidence','deferral changed');});
  await check('Backend refresh restores saved answers and does not create receipt',async()=>{model=null;await load();assert(model.responses.events.length===2,'saved history lost');assert(Object.keys(model.responses.receipts).length===0,'receipt invented');});
 }else if('__PHASE__'==='receipt'){
  await check('Committed owner receipt is distinct from work completion',()=>{view='Follow-through';render();assert(el('main').textContent.includes('PROME recorded the ruling and matching chat confirmation'),'owner receipt missing');assert(el('main').textContent.includes('not completed implementation'),'completion overclaim');});
  await check('Integrated answer has no response controls',()=>{assert(!el('main').querySelector('select,textarea'),'settled question still answerable');});
  await check('Canonical evidence and prior exact answer remain inspectable',()=>{const event=latest(unit.id),receipt=model.responses.receipts[event.id];assert(receipt.canonical_ruling.path.endsWith('-RULED.md'),'canonical ruling lost');assert(receipt.confirmed_response_sha256===event.sha256,'confirmation mismatch');assert(el('main').textContent.includes(event.request.note),'answer lost');});
 }else{
  await check('Default preview refuses submissions and shows the reason',()=>{assert(!model.submissions_enabled,'unexpected enablement');assert(!el('main').querySelector('select,textarea'),'preview controls present');assert(el('main').textContent.includes('independent review'),'gate missing');});
 }
 await check('Pilot layout fits the viewport',()=>{assert(document.documentElement.scrollWidth<=innerWidth,'horizontal overflow');});
 }
 const out=document.createElement('pre');out.id='test-results';out.hidden=true;out.textContent=JSON.stringify(results);document.body.append(out);
})();</script>'''


def main():
    work = Path(tempfile.mkdtemp(prefix="cato-pilot-browser-", dir="/mnt/c/Users/willi/AppData/Local/Temp"))
    runs = {}
    for phase, width, height in [("write", 1440, 1150), ("write", 520, 1100),
                                 ("receipt", 1440, 1150), ("receipt", 520, 1100), ("locked", 1440, 1150)]:
        label = f"{phase}-{width}"
        fixture = PilotFileTests(methodName="test_default_is_read_only_and_creates_no_response_directory")
        fixture.setUp()
        server = None
        try:
            if phase == "receipt":
                event = fixture.event()
                fixture.put("PROME/proposals/fixture-RULED.md", "Fictional ruling only.\n")
                fixture.put("PROME/proposals/fixture-chat.md", "Fictional matching confirmation only.\n")
                fixture.commit()
                commit = fixture.git("rev-parse", "HEAD").strip()
                receipt = fixture.receipt(event, "integrated")
                receipt.update(canonical_ruling={"path": "PROME/proposals/fixture-RULED.md", "commit": commit},
                               chat_confirmation={"path": "PROME/proposals/fixture-chat.md", "commit": commit},
                               confirmed_response_sha256=event["sha256"])
                fixture.write_receipt(receipt)
                fixture.commit()
            if phase == "locked":
                fixture.store.enable_submissions = False
            server = make_server(fixture.store)
            original = server.RequestHandlerClass.send

            def send(handler, status, value, mime="application/json"):
                if mime == "text/html" and handler.path == "/":
                    value = value.replace("</body>", CHECKS.replace("__PHASE__", phase) + "</body>")
                return original(handler, status, value, mime)

            server.RequestHandlerClass.send = send
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            probe = subprocess.run([
                "/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe", "-NoProfile", "-Command",
                f"$u='http://127.0.0.1:{server.server_port}/'; for($i=0;$i -lt 20;$i++) {{ try {{ "
                "Invoke-WebRequest -UseBasicParsing -TimeoutSec 1 $u | Out-Null; exit 0 "
                "} catch { Start-Sleep -Milliseconds 250 } }; exit 1"
            ], capture_output=True, text=True, timeout=30)
            if probe.returncode:
                raise RuntimeError(f"Windows loopback not ready; evidence {work}")
            screenshot = work / (label + ".png")
            command = ["/mnt/c/Program Files/Google/Chrome/Application/chrome.exe", "--headless=new", "--disable-gpu",
                       "--no-first-run", "--no-default-browser-check", "--disable-background-networking", "--disable-extensions",
                       "--disable-sync", "--hide-scrollbars", "--user-data-dir=" + windows(work / (label + "-profile")),
                       f"--window-size={width},{height}", "--virtual-time-budget=10000", "--screenshot=" + windows(screenshot),
                       "--dump-dom", f"http://127.0.0.1:{server.server_port}/"]
            result = subprocess.run(command, capture_output=True, text=True, timeout=50)
            (work / (label + "-dom.html")).write_text(result.stdout)
            match = re.search(r'<pre id="test-results" hidden="">(.*?)</pre>', result.stdout, re.S)
            if not match:
                raise RuntimeError(f"No browser results; evidence {work}: " + result.stderr[-600:])
            checks = json.loads(html.unescape(match[1]))
            runs[label] = {"checks": checks, "returncode": result.returncode, "screenshot": str(screenshot)}
            print(label, json.dumps(checks), flush=True)
        finally:
            if server:
                server.shutdown()
                server.server_close()
                thread.join(timeout=5)
            fixture.doCleanups()
    receipt = {"kind": "candidate pilot author checks on temporary repositories; no live activation or laptop proof",
               "runs": runs, "work_directory": str(work),
               "hashes": {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
                          for name in ("store.py", "server.py", "index.html", "pilot_files.py", "test_pilot_files.py", "test_pilot_browser.py")}}
    (HERE / "pilot-validation.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print("Evidence directory:", work)
    if any(not check["pass"] for run in runs.values() for check in run["checks"]):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
