"""Capture the September EIA vintage; reruns refuse to overwrite evidence."""
import concurrent.futures
import datetime as dt
import hashlib
import json
from pathlib import Path
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parent
SOURCES = {
    "sep26_base.xlsx": "https://www.eia.gov/outlooks/steo/archives/sep26_base.xlsx",
    "sep26.pdf": "https://www.eia.gov/outlooks/steo/archives/sep26.pdf",
    "overview.html": "https://www.eia.gov/outlooks/steo/",
    "global-oil.html": "https://www.eia.gov/outlooks/steo/report/global_oil.php",
    "products.html": "https://www.eia.gov/outlooks/steo/report/petro_prod.php",
}

def fetch(item):
    name, url = item
    path = ROOT / name
    if path.exists():
        raise FileExistsError(path)
    request = urllib.request.Request(url, headers={"User-Agent": "BRENT research source archive"})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read()
        record = dict(file=name, requested_url=url, final_url=response.url,
                      status=response.status, content_type=response.headers.get("Content-Type"),
                      retrieved_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
                      bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    if name.endswith(".xlsx"):
        assert data.startswith(b"PK"), "Workbook is not a ZIP container"
    if name.endswith(".pdf"):
        assert data.startswith(b"%PDF"), "Response is not PDF"
    path.write_bytes(data)
    return record

if __name__ == "__main__":
    assert not (ROOT / "source-manifest.json").exists()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(fetch, SOURCES.items()))
    baseline = ROOT.parent / "2026-09-09_squeeze-review/aug26_base.xlsx"
    manifest = dict(repo_head_before=subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        september_issue="2026-09-09", september_forecast_completed="2026-09-03",
        august_issue="2026-08-11", august_forecast_completed="2026-08-06",
        august_baseline=dict(file=str(baseline.relative_to(ROOT.parent)),
            sha256=hashlib.sha256(baseline.read_bytes()).hexdigest()), sources=records)
    (ROOT / "source-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest, indent=2))
