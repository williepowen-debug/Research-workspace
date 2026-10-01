"""Isolated CATO review probes. No network or owner-file writes.

Run from the Git root with python3 -B. Observations reproduce current behavior,
not desired behavior. Synthetic cases do not establish a historical missed signal.
"""
import contextlib
import csv
import datetime as dt
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]


def module(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def invoke(mod, argv):
    out = io.StringIO()
    with patch.object(sys, "argv", ["probe", *argv]), contextlib.redirect_stdout(out):
        rc = mod.main()
    return rc, out.getvalue()


def board_cases():
    mod = module("cato_board", "PROME/tools/board_scan.py")
    findings = {}
    with tempfile.TemporaryDirectory() as tmp:
        mod.BOARD = Path(tmp) / "BOARD"
        mod.BOARD.mkdir()
        mod.CURSOR = Path(tmp) / "cursor.txt"
        mod.CURSOR.write_text("SIG-W-20260930-004\n")
        draft = mod.BOARD / "SIG-W-20260930-005-draft.md"
        draft.write_text("# Incomplete, unpublished draft\n")
        rc, out = invoke(mod, ["--advance"])
        findings["unpublished_malformed_draft"] = {
            "rc": rc, "cursor": mod.CURSOR.read_text().strip(), "output": out.strip()
        }
        draft.write_text("---\nsignal_id: SIG-W-20260930-005\naction: [PROME]\ninfo: []\n---\n# Now published with an action\n")
        rc, out = invoke(mod, ["--advance"])
        findings["same_id_completed_with_action"] = {"rc": rc, "output": out.strip()}
        mod.CURSOR.write_text("SIG-W-20260930-004\n")
        rc, out = invoke(mod, ["--advance"])
        findings["valid_action_control"] = {
            "rc": rc, "cursor": mod.CURSOR.read_text().strip(), "output": out.strip()
        }
        # Even filtering to published files needs a policy for late lower IDs.
        draft.unlink()
        high = mod.BOARD / "SIG-W-20260930-006-published.md"
        high.write_text("---\nsignal_id: SIG-W-20260930-006\naction: [BRENT]\ninfo: [PROME]\n---\n# Higher ID published first\n")
        invoke(mod, ["--advance"])
        draft.write_text("---\nsignal_id: SIG-W-20260930-005\naction: [PROME]\n---\n# Lower ID published later\n")
        rc, out = invoke(mod, ["--advance"])
        findings["late_lower_id"] = {"rc": rc, "output": out.strip()}
    assert findings["unpublished_malformed_draft"]["cursor"].endswith("005")
    assert findings["same_id_completed_with_action"]["rc"] == 0
    assert findings["valid_action_control"]["rc"] == 1
    assert findings["valid_action_control"]["cursor"].endswith("004")
    return findings


def trepp_cases():
    mod = module("cato_trepp", "AGENTS/CREED/scripts/trepptalk_sweep.py")
    findings = {}
    post = {"known-article": ("Known article title", dt.date.today(), "https://example.invalid")}
    def mostly_failed(url):
        if url.endswith(mod.PAGES[0]):
            return "one readable listing"
        raise TimeoutError("synthetic")
    with patch.object(mod, "fetch", mostly_failed), patch.object(mod, "parse", return_value=post), patch.object(mod, "seen_in_desk", return_value=["known.md"]):
        rc, out = invoke(mod, [])
        findings["eight_of_nine_pages_fail"] = {"rc": rc, "output": out.strip()}
    with patch.object(mod, "fetch", side_effect=["valid"] + ["template changed"] * 8), patch.object(mod, "parse", side_effect=lambda raw: post if raw == "valid" else {}), patch.object(mod, "seen_in_desk", return_value=["known.md"]):
        rc, out = invoke(mod, [])
        findings["eight_of_nine_pages_parse_empty"] = {"rc": rc, "output": out.strip()}
    many = {f"slug-{n:02d}": (f"Synthetic article {n:02d}", None, f"https://example.invalid/{n}") for n in range(15)}
    with patch.object(mod, "fetch", return_value="listing"), patch.object(mod, "parse", return_value=many), patch.object(mod, "seen_in_desk", return_value=[]):
        rc, out = invoke(mod, ["--all"])
        findings["all_undated_rows"] = {"rc": rc, "rows_shown": out.count("https://example.invalid/"), "rows_available": 15, "output": out.strip()}
    raw = '<article>September 30, 2026 <a href="https://www.trepp.com/trepptalk/newest-post">Newest office article</a></article><article>August 1, 2026 <a href="https://www.trepp.com/trepptalk/older-post">Older office article</a></article>'
    findings["dates_above_titles"] = {slug: str(row[1]) for slug, row in mod.parse(raw).items()}
    assert findings["eight_of_nine_pages_fail"]["rc"] == 0
    assert findings["eight_of_nine_pages_parse_empty"]["rc"] == 0
    assert findings["all_undated_rows"]["rows_shown"] == 12
    return findings


def brent_replay():
    home = ROOT / "AGENTS/BRENT/research/2026-09-30_path-b-successor"
    gas = {dt.date.fromisoformat(d): v for d, v in json.loads((home / "eia_product_supplied_through_2026-09-25.json").read_text())["WGFUPUS2"]}
    with (home / "GASREGW_fred_2026-09-30.csv").open() as f:
        prices = {}
        for row in csv.DictReader(f):
            try:
                prices[dt.date.fromisoformat(row["observation_date"])]=float(row["GASREGW"])
            except ValueError:
                pass
    def price_yoy(w):
        monday = w + dt.timedelta(days=3)
        return 100 * (prices[monday] / prices[monday - dt.timedelta(days=364)] - 1)
    def volume_yoy(w):
        current = sum(gas[w - dt.timedelta(days=7*k)] for k in range(4))
        base = sum(gas[w - dt.timedelta(days=364+7*k)] for k in range(4))
        return 100 * (current / base - 1)
    eligible = [w for w in sorted(gas) if 1993 <= w.year <= 2025 and not dt.date(2020,3,1) <= w <= dt.date(2021,12,31)]
    allowed = set(eligible)
    outcomes = []
    missing = 0
    for w in eligible:
        try:
            if volume_yoy(w) < -0.5 or min(price_yoy(w-dt.timedelta(days=7*k)) for k in range(12)) < 20:
                continue
            future = [w + dt.timedelta(days=7*k) for k in range(1,9)]
            if not all(d in allowed for d in future):
                continue
            lows = 0
            prior = None
            vals = []
            outcome = None
            for date in future:
                y = volume_yoy(date)
                vals.append(y)
                lows += price_yoy(date) < 20
                if lows >= 3:
                    outcome = "NOT_FIRED"
                    break
                if prior is not None and prior <= -1.5 and y <= -1.5:
                    outcome = "MET"
                    break
                prior = y
            if outcome is None:
                outcome = "NOT_MET" if all(y > -1 for y in vals) else "NO_VERDICT"
            outcomes.append((w, outcome))
        except KeyError:
            missing += 1
    from collections import Counter
    counts = Counter(g for _,g in outcomes)
    clusters = []
    prior = None
    for w,g in outcomes:
        if prior is None or (w-prior).days > 63:
            clusters.append([])
        clusters[-1].append(g)
        prior = w
    fired = [[g for g in c if g != "NOT_FIRED"] for c in clusters]
    fired = [c for c in fired if c]
    result = {"windows":len(outcomes), "counts":dict(counts), "clusters":len(clusters), "surviving_clusters":len(fired), "equal_weight_MET_pct":100*sum(c.count("MET")/len(c) for c in fired)/len(fired), "missing_exact_date_candidates":missing}
    assert len(outcomes) == 88 and counts["MET"] == 32 and len(fired) == 6
    return result


if __name__ == "__main__":
    print(json.dumps({"board":board_cases(), "trepp":trepp_cases(), "brent":brent_replay()}, indent=2))
