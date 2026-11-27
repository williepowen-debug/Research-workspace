"""One plain honest-client request to the SPDR GLD issuer archive (D:L1113 backstop, 2026-11-27).
Permitted by PROME's task letter: one request, honest client name (WQ-735), a refusal is the stop. Never re-run."""
import json, urllib.request, datetime, hashlib, sys
URL = "https://api.spdrgoldshares.com/api/v1/historical-archive?exchange=NYSE&lang=en&product=gld"
rec = {"url": URL, "client": "python urllib, User-Agent research-bot/1.0",
       "requested_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
try:
    r = urllib.request.urlopen(urllib.request.Request(URL, headers={"User-Agent": "research-bot/1.0"}), timeout=60)
    body = r.read(); rec.update(status=r.status, bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
    open("GLD_issuer_archive.xlsx", "wb").write(body)
except Exception as e:
    rec["error"] = repr(e)
rec["received_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
json.dump(rec, open("access.json", "w"), indent=2); print(json.dumps(rec, indent=2))
