"""Save public publisher evidence and retrieval receipts; no grades or sends."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sys
import importlib.util
import re
import urllib.request

OUT = Path(__file__).resolve().parent
URLS = {
    "airasia-group": "https://newsroom.airasia.com/news/airasia-group-financial-results-second-quarter-2026",
    "thai-airasia": "https://newsroom.airasia.com/news/2026/8/14/aav-announces-financial-results-second-quarter-2026",
    "airasia-philippines": "https://newsroom.airasia.com/news/2026/8/8/airasia-philippines-ranks-no-1-among-the-worlds-most-punctual-low-cost-airlines-in-july-2026",
    "air-india": "https://www.airindia.com/in/en/newsroom/press-release/Air-India-rationalises-international-route-network-through-August-2026.html",
}

if "--verify-rigs" in sys.argv:
    spec = importlib.util.spec_from_file_location("brent_instruments", OUT.parents[1] / "scripts/instrument_check.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    query = "https://rigcount.bakerhughes.com/na-rig-count|North America Rig Count Report - New Report"
    ok, stamp, detail = module.probe_bhrigs(query)
    result = {"ok": ok, "observed": stamp.isoformat() if stamp else None, "detail": detail,
              "retrieved_at": datetime.now(timezone.utc).isoformat()}
    (OUT / "rig-live-verification.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(result))
    raise SystemExit(0 if ok else 2)

records = []
def fetch(name, url):
    record = {"name": name, "url": url, "retrieved_at": datetime.now(timezone.utc).isoformat()}
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "*/*"})
        with urllib.request.urlopen(req, timeout=25) as r:
            blob = r.read()
            record.update(status=r.status, content_type=r.headers.get("Content-Type"), disposition=r.headers.get("Content-Disposition"), final_url=r.url, bytes=len(blob))
        suffix = ".xlsx" if blob[:2] == b"PK" else ".pdf" if blob[:4] == b"%PDF" else ".html"
        (OUT / (name + suffix)).write_bytes(blob)
        records.append(record)
        return blob
    except Exception as exc:
        record["error"] = f"{type(exc).__name__}: {exc}"
        records.append(record)
        return b""
for name, url in URLS.items():
    blob = fetch(name, url)
    if name == "bh-listing" and blob:
        anchors = re.findall(r'<a[^>]*href="([^"]*static-files/[^"]*)"[^>]*>(.*?)</a>', blob.decode(errors="replace"), re.S)
        found = [(href, re.sub("<[^>]+>", "", label).strip()) for href, label in anchors if "Report - New Report" in re.sub("<[^>]+>", "", label)]
        if len(found) == 1:
            href = found[0][0]
            fetch("bh-current", urllib.parse.urljoin(url, href))
(OUT / "retrieval-airlines.json").write_text(json.dumps(records, indent=2))
for row in records:
    print(row["name"], row.get("status", row.get("error")), row.get("bytes", ""), row.get("disposition", ""))
