#!/usr/bin/env python3
"""Native Windows Chrome / WSL author checks; isolated synthetic stores and profiles."""
from pathlib import Path
import hashlib
import html
import json
import re
import subprocess
import tempfile
import threading

from server import make_server
from store import HERE, Store

CHECKS = r'''<script>
(async()=>{
 const results=[];
 function assert(ok,why){if(!ok)throw Error(why);}
 async function check(name,f){try{await f();results.push({name,pass:true});}catch(e){results.push({name,pass:false,error:e.message});}}
 for(let tries=0;!model&&tries<100;tries++)await new Promise(resolve=>setTimeout(resolve,50));
 await check('Source and all four views load',()=>{assert(model,'model missing');assert(document.querySelectorAll('#nav button').length===5,'view navigation');assert(document.querySelectorAll('article').length===1,'one decision');});
 if(model){
 const unit=model.snapshot.record.units[0];
 await check('Review cancel preserves exact condition and saves nothing',()=>{const d=draft(unit);d.note='<img src=x onerror=alert(1)> Only one selftest.\nNo schedule.';review(unit,d,null);assert(!el('review-body').querySelector('img'),'executable markup');assert(el('review-body').textContent.includes(d.note),'exact note');el('cancel').click();assert(draft(unit).note===d.note,'draft lost');assert(model.responses.events.length===0,'cancel saved');});
 await check('Failed source read stays explicit and retry preserves the draft',async()=>{const originalApi=api;try{api=async()=>{throw Error('Simulated source failure');};await load();assert(!model,'stale data presented');assert(el('status').textContent.includes('Simulated source failure'),'missing failure');assert(document.querySelector('#nav button').textContent==='Retry source read','no recovery');}finally{api=originalApi;}await load();assert(draft(unit).note.includes('<img'),'draft lost');});
 await check('Save binds one unit and appears as locally saved only',async()=>{review(unit,draft(unit),null);await el('save').onclick();assert(model.responses.events.length===1,'one event');assert(model.responses.events[0].request.unit_id===unit.id,'scope');assert(view==='Follow-through','placement');assert(el('main').textContent.includes('No receiver acknowledgment'),'false receipt');});
 await check('Refresh recovers saved answer from backend',async()=>{model=null;await load();assert(model.responses.events.length===1,'saved state missing');assert(model.responses.events[0].request.note.includes('<img'),'words changed');});
 await check('Question cannot save without words and keeps draft',async()=>{const d=draft(unit);d.action='request_changes';d.note='';review(unit,d,latest(unit.id));await el('save').onclick();assert(el('review').open,'failure dismissed draft');assert(el('review-status').textContent.includes('needs your words'),'missing error');assert(model.responses.events.length===1,'blank question saved');el('cancel').click();});
 await check('Deferral preserves return condition and prior answer',async()=>{const d=draft(unit);d.action='defer';d.note='Wait for evidence';d.revisit='After the next filing';review(unit,d,latest(unit.id));await el('save').onclick();assert(model.responses.events.length===2,'prior answer lost');const e=latest(unit.id);assert(e.request.action==='defer'&&e.selected_choice===null,'approval inferred');assert(e.request.revisit==='After the next filing','condition lost');});
 await check('Personal task report does not create approval or receipt',async()=>{view='Tasks for me';render();const task=model.snapshot.record.units[1];assert(document.querySelectorAll('article').length===1,'task missing');review(task,draft(task),null);await el('save').onclick();const e=latest(task.id);assert(e.request.action==='report_done'&&e.selected_choice===null,'task approval');assert(!model.responses.receipts[e.id],'invented receipt');});
 await check('History remains readable without response controls',()=>{view='History';render();assert(document.querySelectorAll('article').length===1,'history missing');assert(!el('main').querySelector('select,textarea'),'history controls');});
 await check('Layout fits viewport with saved conditions',()=>{view='Follow-through';render();assert(document.documentElement.scrollWidth<=innerWidth,'horizontal overflow');});
 }
 const out=document.createElement('pre');out.id='test-results';out.hidden=true;out.textContent=JSON.stringify(results);document.body.append(out);
})();</script>'''


def windows(path):
    return subprocess.check_output(["wslpath", "-w", str(path)], text=True).strip()


def main():
    chrome = Path("/mnt/c/Program Files/Google/Chrome/Application/chrome.exe")
    work = Path(tempfile.mkdtemp(prefix="cato-decisions-mvp-", dir="/mnt/c/Users/willi/AppData/Local/Temp"))
    runs = {}
    for label, width, height in [("desktop", 1440, 1150), ("narrow", 520, 1100)]:
        with tempfile.TemporaryDirectory(prefix="cato-decisions-store-") as data:
            store = Store(Path(data) / "responses.sqlite3")
            server = make_server(store)
            original = server.RequestHandlerClass.send

            def send(handler, status, value, mime="application/json"):
                if mime == "text/html" and handler.path == "/":
                    value = value.replace("</body>", CHECKS + "</body>")
                return original(handler, status, value, mime)

            server.RequestHandlerClass.send = send
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                # WSL's Windows localhost forwarding may appear after bind returns.
                probe = subprocess.run([
                    "/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe", "-NoProfile", "-Command",
                    f"$u='http://127.0.0.1:{server.server_port}/'; for($i=0;$i -lt 20;$i++) {{ try {{ "
                    "Invoke-WebRequest -UseBasicParsing -TimeoutSec 1 $u | Out-Null; exit 0 "
                    "} catch { Start-Sleep -Milliseconds 250 } }; exit 1"
                ], capture_output=True, text=True, timeout=30)
                if probe.returncode:
                    raise RuntimeError(f"Windows cannot reach WSL loopback; evidence {work}")
                screenshot = work / f"{label}.png"
                command = [str(chrome), "--headless=new", "--disable-gpu", "--no-first-run",
                           "--no-default-browser-check", "--disable-background-networking", "--disable-extensions",
                           "--disable-sync", "--hide-scrollbars", "--user-data-dir=" + windows(work / (label + "-profile")),
                           f"--window-size={width},{height}", "--virtual-time-budget=10000",
                           "--screenshot=" + windows(screenshot), "--dump-dom",
                           f"http://127.0.0.1:{server.server_port}/"]
                result = subprocess.run(command, capture_output=True, text=True, timeout=50)
                (work / f"{label}-dom.html").write_text(result.stdout)
                match = re.search(r'<pre id="test-results" hidden="">(.*?)</pre>', result.stdout, re.S)
                if not match:
                    raise RuntimeError("No browser receipt: " + result.stderr[-1200:] + f"; evidence {work}")
                checks = json.loads(html.unescape(match[1]))
                runs[label] = {"returncode": result.returncode, "checks": checks, "screenshot": str(screenshot)}
                print(label, json.dumps(checks), flush=True)
            finally:
                server.shutdown()
                server.server_close()
                thread.join(timeout=5)
    receipt = {"kind": "synthetic MVP author browser checks; not live adoption or laptop acceptance",
               "runs": runs, "work_directory": str(work),
               "hashes": {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
                          for name in ("store.py", "server.py", "index.html", "test_mvp.py", "test_browser.py")}}
    (HERE / "validation.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print("Evidence directory:", work)
    if any(not c["pass"] for run in runs.values() for c in run["checks"]):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
