"""Offline checks for the October 19 commit review; no owner writes or network."""
import datetime as dt
import hashlib
import json
import math
from pathlib import Path
import sys
import tarfile
from unittest.mock import patch
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[3]
P = ROOT / "AGENTS/HENRY/research/2026-10-19_repeat-losers"
metrics = json.loads((P / "metrics.json").read_text())
summary = json.loads((P / "summary.json").read_text())
manifest = json.loads((P / "source-manifest.json").read_text())["raw_members"]
with tarfile.open(P / "sources.tar.gz") as archive:
    blobs = {m.name: archive.extractfile(m).read() for m in archive if m.isfile()}
for item in manifest:
    blob = blobs[item["path"]]
    assert len(blob) == item["bytes"]
    assert hashlib.sha256(blob).hexdigest() == item["sha256"]

def prices(symbol):
    chart = json.loads(blobs[f"raw/chart-{symbol}.json"])["chart"]["result"][0]
    assert chart["meta"]["symbol"] == symbol
    return {
        dt.datetime.fromtimestamp(t, ZoneInfo("America/New_York")).date().isoformat(): v
        for t, v in zip(chart["timestamp"], chart["indicators"]["adjclose"][0]["adjclose"])
        if v is not None
    }

symbols = set(metrics) | {m["sector"] for m in metrics.values()} | {"SPY"}
series = {s: prices(s) for s in symbols}
calendar = sorted(d for d in series["SPY"] if d <= summary["endpoint"])
assert calendar[-1] == "2026-10-19"
comparisons = 0
for symbol, saved in metrics.items():
    sector = saved["sector"]
    for length in (5, 20, 60):
        dates = calendar[-length-1:]
        result = saved["windows"][str(length)]
        assert dates[0] == result["start"]
        returns = {
            s: [series[s][b] / series[s][a] - 1 for a, b in zip(dates, dates[1:])]
            for s in (symbol, sector, "SPY")
        }
        total = math.expm1(math.fsum(math.log1p(v) for v in returns[symbol]))
        sector_total = math.expm1(math.fsum(math.log1p(v) for v in returns[sector]))
        assert abs(total * 100 - result["return_pct"]) < 1e-8
        assert abs(((1 + total) / (1 + sector_total) - 1) * 100
                   - result["sector_relative_wealth_pct"]) < 1e-8
        for condition in ("index_up", "sector_up", "both_up"):
            indexes = [
                i for i in range(length)
                if (condition == "sector_up" or returns["SPY"][i] > 0)
                and (condition == "index_up" or returns[sector][i] > 0)
            ]
            assert len(indexes) == result[condition]["eligible"]
            assert sum(returns[symbol][i] < 0 for i in indexes) == result[condition]["losses"]
        comparisons += 1

sys.path.insert(0, str(ROOT / "AGENTS/WALTER/tools"))
from test_x_bookmarks_workflow import Workflow, x, w

def probe(damaged_stage=False):
    case = Workflow()
    case.setUp()
    try:
        if damaged_stage:
            case.make_items(501)
            case.main()
            stage = w.read_json(x._pending_path())
            stage["ids"].remove("499")
            w.atomic_json(x._pending_path(), stage)
            case.mark()
            case.main()
            case.mark()
            case.main()
            result = {
                "consumed_count": len(x.load_seen()["consumed"]),
                "id_499_consumed": "499" in x.load_seen()["consumed"],
                "scan_complete": x.load_seen()["scan_complete"],
                "pending": x.load_pending(),
            }
            assert result == dict(consumed_count=500, id_499_consumed=False,
                                  scan_complete=True, pending=[])
            return result
        case.main()
        review = case.review(read_state="partly_read", ask_user="Need the missing debt table.")
        with patch.object(w, "commit_checkpoint", side_effect=OSError("simulated shutdown")):
            try:
                case.main("--mark", "--review", str(review))
            except OSError:
                pass
        assert x.load_seen()["consumed"] == ["0"]
        case.main()
        receipt = w.read_json(w.path_for(x.SEEN, "receipt"))
        result = dict(consumed=x.load_seen()["consumed"], pending=x.load_pending(),
                      receipt=receipt, original_review_survives=review.exists())
        assert receipt["items"] == 0 and not receipt.get("requests")
        assert result["original_review_survives"] and not result["pending"]
        return result
    finally:
        case.doCleanups()

print(json.dumps({
    "scope": "Saved vendor data arithmetic, not independent price-source verification; offline bookmark fixtures only.",
    "source_members_verified": len(manifest),
    "symbols_checked": len(metrics),
    "symbol_windows_checked": comparisons,
    "existing_L755_reproduced": probe(True),
    "interrupted_mark_receipt_gap": probe(False),
}, indent=2))
