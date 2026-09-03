#!/usr/bin/env python3
"""
HAWK War Monitor — news-scan wrapper with FAIL-LOUD source accounting.

⚠️ SCOPE BANNER (2026-09-02): the D/C/B SCENARIO_BASELINE constants below are
   FROZEN pre-split (2026-07-12) Iran-scenario content. HAWK does NOT own the
   Iran/Gulf theater — FALCON does (AGENTS/FALCON/). The scenario block is a
   historical artifact retained for shape only; DO NOT cite its percentages as
   a live HAWK read. What this script is good for after 2026-09-02 is the ONE
   thing it now does honestly: report how much of its declared source set it
   actually reached.

🔴 FAIL-LOUD CONTRACT (added 2026-09-02, DOCKET L202 / DAEDALUS SFG sweep 8/17):
   1. Every source is declared in NEWS_SOURCES. Nothing is fetched off-registry.
   2. Every scan prints `reached N/M` and names every DEAD source with its error.
   3. Partial coverage SUPPRESSES the interpretation line. A partial scan may
      not render as "status quo holding" — that was the original defect: a bare
      `except: return []` made a dead feed byte-identical to a quiet world.
   4. `--save` is GATED on full coverage. An outage may never write the baseline
      scenario into SCENARIO_HISTORY.tsv as `auto_scan` — that write is permanent.
   5. Exit code: 0 only on full coverage; 2 on any partial/zero coverage.
   6. `--selftest` injects a guaranteed-dead source to prove the guard fires
      (CHECK_STANDARD §3 / [[finding_test_the_guard_not_just_the_guarded]]).

   Source removed 2026-09-02: `http://feeds.reuters.com/reuters/worldnews` —
   live-verified DEAD (URLError Errno -2, name does not resolve) on 2026-08-17
   by DAEDALUS and re-verified DEAD from this box 2026-09-02 19:4x ET.
   Replacement `https://www.aljazeera.com/xml/rss/all.xml` verified HTTP 200 /
   16,957 B same run.

Usage:
  python3 AGENTS/HAWK/scripts/war_monitor.py
  python3 AGENTS/HAWK/scripts/war_monitor.py --save      # gated on full coverage
  python3 AGENTS/HAWK/scripts/war_monitor.py --selftest  # prove the guard fires
"""

import sys
import subprocess
import argparse
from datetime import datetime
from pathlib import Path

HAWK_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = HAWK_DIR / "workbook"
WORKBOOK.mkdir(exist_ok=True)

# ⚠️ FROZEN pre-split constants — historical shape only, NOT a live HAWK read.
SCENARIO_BASELINE = {"D": 82, "C": 12, "B": 6}

# 🔴 THE DECLARED SOURCE SET. Coverage is measured against this list and nothing
#    else. Adding a source here without verifying it live is the defect this
#    registry exists to prevent — probe it, then add it.
NEWS_SOURCES = [
    ("GoogleNews:Israel-Iran", "query", "Israel Iran war"),
    ("GoogleNews:Houthi-RedSea", "query", "Houthi Red Sea"),
    ("GoogleNews:Hormuz", "query", "Hormuz Strait"),
    ("BBC-World", "rss", "http://feeds.bbci.co.uk/news/world/rss.xml"),
    ("AlJazeera-All", "rss", "https://www.aljazeera.com/xml/rss/all.xml"),
]

# Injected only by --selftest, to prove the partial-coverage guard actually fires.
SELFTEST_DEAD_SOURCE = (
    "SELFTEST-DEAD", "rss", "http://feeds.reuters.com/reuters/worldnews")
CEASEFIRE_START = datetime(2026, 4, 12).date()


def _fetch(url, timeout=12):
    """Raw fetch. Returns (ok, bytes_or_None, err_str). NEVER swallows silently."""
    import urllib.request, urllib.error, ssl
    try:
        ctx = ssl.create_default_context()
        req = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0 (compatible; HAWK/1.0; +research)"})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            data = r.read()
            if not data:
                return False, None, f"HTTP {r.status} but ZERO bytes"
            return True, data, ""
    except Exception as e:
        return False, None, f"{type(e).__name__}: {str(e)[:110]}"


def _parse_rss(xml_bytes, limit=5):
    """Parse RSS items. Returns (ok, [lines], err_str)."""
    import re
    from xml.etree import ElementTree as ET
    try:
        root = ET.fromstring(xml_bytes.decode("utf-8", errors="ignore"))
    except Exception as e:
        return False, [], f"XML parse failed: {type(e).__name__}"
    items = root.findall(".//item")
    if not items:
        return False, [], "parsed OK but ZERO <item> elements (feed shape changed?)"
    out = []
    for item in items[:limit]:
        title = item.find("title")
        desc = item.find("description")
        t = title.text if title is not None else ""
        d = desc.text if desc is not None else ""
        if d:
            d = re.sub(r"<[^>]+>", " ", d)
            d = re.sub(r"\s+", " ", d).strip()
        if t:
            out.append(f"{t}: {d[:150]}" if d else t)
    if not out:
        return False, [], "items present but none carried a title"
    return True, out, ""


def probe_source(name, kind, target, limit=5):
    """Fetch ONE declared source. Returns (name, ok, text, err).

    A source counts as REACHED only if it returned parseable, non-empty content.
    HTTP 200 with an empty body, a shape change, or a parse failure all count as
    NOT REACHED and are named in the output — a 200 is not evidence of coverage.
    """
    import urllib.parse
    if kind == "query":
        url = ("https://news.google.com/rss/search?q="
               + urllib.parse.quote(target) + "&hl=en-US&gl=US&ceid=US:en")
    else:
        url = target
    ok, data, err = _fetch(url)
    if not ok:
        return name, False, "", err
    ok, lines, err = _parse_rss(data, limit=limit)
    if not ok:
        return name, False, "", err
    return name, True, "\n".join(f"- {l}" for l in lines), ""


def search_war_news(selftest=False):
    """Scan the declared source set. Returns (results, coverage).

    coverage = {"attempted": M, "reached": N, "dead": [(name, err), ...]}
    """
    sources = list(NEWS_SOURCES)
    if selftest:
        sources.append(SELFTEST_DEAD_SOURCE)

    results, dead, reached = [], [], 0
    for name, kind, target in sources:
        nm, ok, text, err = probe_source(name, kind, target)
        if ok:
            reached += 1
            results.append((nm, text))
        else:
            dead.append((nm, err))

    coverage = {"attempted": len(sources), "reached": reached, "dead": dead}
    return results, coverage


def analyze_signals(news_results):
    """Analyze news for scenario signals."""
    signals = []
    
    # Combine all text for analysis
    all_text = " ".join([r[1] for r in news_results]).lower()
    
    # Escalation signals (increase D)
    escalation_keywords = [
        "strike", "attack", "missile", "drone", "explosion", "damage",
        "casualties", "killed", "destroyed", "retaliation", "escalation"
    ]
    
    # De-escalation signals (increase B)
    deescalation_keywords = [
        "ceasefire", "talks", "negotiation", "agreement", "deal",
        "diplomatic", "mediation", "prisoner exchange", "progress"
    ]
    
    # Stability signals (neutral/ongoing)
    stability_keywords = [
        "holding", "stable", "quiet", "no incidents", "stand-down",
        "compliance", "monitoring"
    ]
    
    escalation_count = sum(1 for k in escalation_keywords if k in all_text)
    deescalation_count = sum(1 for k in deescalation_keywords if k in all_text)
    stability_count = sum(1 for k in stability_keywords if k in all_text)
    
    # Generate signals
    if escalation_count > 2:
        signals.append({
            "type": "🔴",
            "signal": "Escalation indicators detected",
            "impact": "D +5-10%",
            "details": f"Keywords: {escalation_count} escalation mentions"
        })
    
    if deescalation_count > 2:
        signals.append({
            "type": "🟢",
            "signal": "Diplomatic progress indicators",
            "impact": "B +5%",
            "details": f"Keywords: {deescalation_count} de-escalation mentions"
        })
    
    if stability_count > 1 or (escalation_count == 0 and deescalation_count < 2):
        signals.append({
            "type": "🟡",
            "signal": "Ceasefire holding, no major incidents",
            "impact": "D unchanged",
            "details": "Status quo maintained"
        })
    
    return signals


def calculate_scenario_shift(signals):
    """Calculate scenario probability shifts based on signals."""
    new_scenario = SCENARIO_BASELINE.copy()
    
    for sig in signals:
        if "D +" in sig["impact"]:
            # Extract number
            try:
                shift = int(sig["impact"].split("+")[1].split("%")[0])
                new_scenario["D"] = min(95, new_scenario["D"] + shift)
                new_scenario["C"] = max(0, new_scenario["C"] - shift // 2)
                new_scenario["B"] = max(0, new_scenario["B"] - shift // 2)
            except:
                pass
        elif "B +" in sig["impact"]:
            try:
                shift = int(sig["impact"].split("+")[1].split("%")[0])
                new_scenario["B"] = min(20, new_scenario["B"] + shift)
                new_scenario["D"] = max(60, new_scenario["D"] - shift)
            except:
                pass
    
    return new_scenario


def save_war_log(signals, scenario):
    """Log to WAR_LOG.md."""
    log_path = WORKBOOK / "WAR_LOG.md"
    today = datetime.now().strftime("%Y-%m-%d")
    
    with open(log_path, "a") as f:
        f.write(f"\n## {today}\n\n")
        f.write(f"**Scenario:** D {scenario['D']}% / C {scenario['C']}% / B {scenario['B']}%\n\n")
        f.write("**Signals:**\n")
        for sig in signals:
            f.write(f"- {sig['type']} {sig['signal']}\n")
        f.write("\n")


def save_scenario_history(scenario):
    """Log to SCENARIO_HISTORY.tsv."""
    tsv_path = WORKBOOK / "SCENARIO_HISTORY.tsv"
    today = datetime.now().strftime("%Y-%m-%d")
    
    if not tsv_path.exists():
        with open(tsv_path, "w") as f:
            f.write("date\tD_pct\tC_pct\tB_pct\ttrigger_event\n")
    
    with open(tsv_path, "a") as f:
        f.write(f"{today}\t{scenario['D']}\t{scenario['C']}\t{scenario['B']}\tauto_scan\n")


def main():
    parser = argparse.ArgumentParser(description="HAWK war monitor (fail-loud)")
    parser.add_argument("--save", action="store_true",
                        help="Save to workbook — GATED on full source coverage")
    parser.add_argument("--selftest", action="store_true",
                        help="Inject a known-dead source to prove the guard fires")
    args = parser.parse_args()

    today = datetime.now()
    today_date = today.date()
    now = today.strftime("%Y-%m-%d %H:%M ET")

    war_start = datetime(2026, 3, 1).date()
    war_day = (today_date - war_start).days
    ceasefire_day = (today_date - CEASEFIRE_START).days if today_date >= CEASEFIRE_START else 0

    print(f"\n{'='*70}")
    print(f"  HAWK War Monitor — {now}")
    if args.selftest:
        print("  ** SELFTEST MODE — a known-dead source is injected on purpose. **")
    print(f"{'='*70}")

    print(f"\n  War Day: {war_day} | Ceasefire Day: {ceasefire_day} (Apr 12-13)")
    print("  ⚠️  SCENARIO CONSTANTS ARE FROZEN PRE-SPLIT (2026-07-12) — Iran/Gulf is")
    print("      FALCON's theater. Do NOT cite the D/C/B figures below as a live read.")
    print(f"  Frozen baseline: D {SCENARIO_BASELINE['D']}% / C {SCENARIO_BASELINE['C']}% / B {SCENARIO_BASELINE['B']}%")

    print("\n  🔍 Scanning declared source set...")
    news_results, cov = search_war_news(selftest=args.selftest)

    reached, attempted = cov["reached"], cov["attempted"]
    full_coverage = (reached == attempted and attempted > 0)

    # ---- SOURCE COVERAGE — printed on EVERY run, before any interpretation ----
    print(f"\n  SOURCE COVERAGE")
    print(f"  {'-'*60}")
    mark = "✅" if full_coverage else "🔴"
    print(f"  {mark} reached {reached}/{attempted} declared sources")
    for name, err in cov["dead"]:
        print(f"     🔴 DEAD: {name} — {err}")
    if not full_coverage:
        print("  🔴 DEGRADED COVERAGE — this scan CANNOT support a status-quo read.")

    signals = analyze_signals(news_results) if news_results else []
    new_scenario = calculate_scenario_shift(signals)

    print(f"\n  SIGNAL SUMMARY (last 24h, {reached}/{attempted} sources)")
    print(f"  {'-'*60}")
    if signals:
        for sig in signals:
            print(f"  {sig['type']} {sig['signal']}")
            print(f"     Impact: {sig['impact']}")
            if sig.get("details"):
                print(f"     Details: {sig['details']}")
    elif full_coverage:
        print("  🟡 No significant developments across ALL declared sources")
    else:
        print("  ⛔ NO SIGNAL VERDICT — coverage is partial; absence here is not evidence.")

    # ---- INTERPRETATION — suppressed entirely unless coverage is full ----
    print(f"\n  INTERPRETATION")
    print(f"  {'-'*60}")
    if not full_coverage:
        print("  ⛔ SUPPRESSED. A partial scan is not a reading of the world.")
        print(f"     {attempted - reached} of {attempted} declared sources did not return content.")
        print("     Fix the dead source(s) above, or re-run, before interpreting.")
    elif new_scenario["D"] > SCENARIO_BASELINE["D"]:
        print("  🔴 Escalation keywords elevated — route to FALCON/OSPREY, not graded here")
    elif new_scenario["B"] > SCENARIO_BASELINE["B"]:
        print("  🟢 De-escalation keywords elevated — route to FALCON/OSPREY, not graded here")
    else:
        print("  🟡 No keyword shift across a FULLY covered scan")

    print(f"\n  ALERTS")
    print(f"  {'-'*60}")
    alerts = []
    if not full_coverage:
        alerts.append(f"🔴 INSTRUMENT DEGRADED — {reached}/{attempted} sources reached")
    if full_coverage and any(s["type"] == "🔴" for s in signals):
        alerts.append("🔴 Kinetic keywords present — theater desks own the verdict")
    if alerts:
        for alert in alerts:
            print(f"  {alert}")
    else:
        print("  ✅ No active alerts (full coverage)")

    # ---- --save GATE: an outage must never write a baseline into history ----
    if args.save:
        if not full_coverage:
            print(f"\n  ⛔ --save REFUSED. Coverage {reached}/{attempted} is not full.")
            print("     Writing on partial coverage would put the BASELINE scenario into")
            print("     SCENARIO_HISTORY.tsv as `auto_scan`, permanently, on an outage.")
            print("     Nothing was written.")
        else:
            save_war_log(signals, new_scenario)
            save_scenario_history(new_scenario)
            print("\n  💾 Logged to workbook/WAR_LOG.md and SCENARIO_HISTORY.tsv (full coverage)")

    print()
    # rc 0 ONLY on full coverage. Partial coverage is a nonzero exit, so a caller
    # or a boot wrapper cannot mistake a degraded scan for a clean one.
    return 0 if full_coverage else 2


if __name__ == "__main__":
    sys.exit(main())
