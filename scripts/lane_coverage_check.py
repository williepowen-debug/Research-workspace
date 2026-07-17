#!/usr/bin/env python3
"""
lane_coverage_check.py — RESEARCH-INTAKE lane coverage doctor (INFO severity).

Predicate (frozen 2026-07-16, WALTER-corrected wording — see
AGENTS/WALTER/inbox/2026-07-16_from-PROME_coverage-sweep-landed.md):
an ACTIVE Tier-1 agent (excluding synthesis-class) whose domain has neither a
GOOGLE_NEWS_QUERIES entry nor a structured-feed mapping has NO AUTONOMOUS LANE
COLLECTION — intake reaches that domain only via Will's channel and the agent's
own session pulls. That is a coverage FACT to surface, not an alarm: the 7/16
coverage sweep's real finding was "Will is the load-bearing intake channel",
and some domains are deliberately un-laned (prediction-market feeds are
parked/future by design). Severity is LOW/INFO by construction.

Sources compared (live, no caching):
  - PROME/ROSTER.md            -> canonical ACTIVE table (agent + domain)
  - <lane>/scripts/newsweep_config.py -> GOOGLE_NEWS_QUERIES agents lists
                                  (ast-parsed, never imported/executed)
  - STRUCTURED_FEEDS below     -> feed->agent map, evidence-cited (the one
                                  hand-maintained surface in this file)

Exit codes: 0 = ran (INFO findings do not fail the check, by design) ·
2 = structural error (roster/lane/config unreadable) — fail loud, never
silently clean. Run from anywhere (repo root resolved internally).

Usage:
  python3 scripts/lane_coverage_check.py            # full coverage table
  python3 scripts/lane_coverage_check.py --quiet    # INFO findings only
  python3 scripts/lane_coverage_check.py --lane-dir /path/to/Research-Intake
"""
import argparse
import ast
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROSTER = os.path.join(REPO, "PROME", "ROSTER.md")
LANE_DEFAULT = os.path.expanduser("~/Research-Intake")

# Synthesis/meta-class actives: their product is coordination, routing, or
# work ON other agents' outputs — there is no external domain for the lane to
# collect. Roster-verified rationale per name:
#   PROME  coordinator/chief of staff        WALTER signal & news routing owner
#   NEXUS  cross-agent synthesis             RED    adversarial red-team
#   TERRY  trade construction (consumes domain agents' evidence)
#   HAWK   cross-war synthesis + dormant book (its acute theaters are
#          OSPREY/FALCON, which hold their own query coverage)
SYNTHESIS_EXCLUDE = {"PROME", "WALTER", "NEXUS", "RED", "TERRY", "HAWK"}

# Structured (non-news) feed -> covered agents. Evidence-cited from the lane's
# own fetcher configs (verified 2026-07-16); update WHEN A FETCHER'S WATCHLIST
# CHANGES, and keep the evidence note current — this map is the only
# hand-maintained input to this check.
STRUCTURED_FEEDS = {
    "fred": {
        # SERIES list in fetch_fred.py: ICSA/CCSA -> LABOR; UMCSENT/PSAVERT/
        # DRCCLACBS/DRCLACBS/PCEPILFE/CPIUFDNS/CPIENGNS/RSXFS/TOTALNS -> CARL;
        # MORTGAGE30US -> HOMER; DGS10/DGS2/T10Y2Y -> BOND; BAMLH0A0HYM2 -> LIQUID
        "agents": {"LABOR", "CARL", "HOMER", "BOND", "LIQUID"},
        "evidence": "fetch_fred.py SERIES (16 series incl. claims, consumer, mortgage, curve, HY OAS)",
    },
    "eia_petroleum": {
        "agents": {"BRENT"},
        "evidence": "fetch_eia_petroleum.py (Cushing/SPR/crude/products; Boundary#3 band)",
    },
    "treasury_auctions": {
        "agents": {"BOND"},
        "evidence": "fetch_treasury_auctions.py (weak-auction alerts)",
    },
    "cftc_cot": {
        # liveness-verified: the lane's CFTC pull reports VIX lev-money net only
        # (VIOLET-ratified band). JPY/oil COT are pulled by SAM/BRENT in-session,
        # NOT by the lane — do not credit them here.
        "agents": {"VIOLET"},
        "evidence": "fetch_cftc_cot.py (VIX lev-money net, band (-75k,0))",
    },
    "edgar_8k": {
        # TARGETS in fetch_edgar_8k.py: WAL/OZK/EGBN/ZION/VLY -> REGINALD;
        # MU + MSFT/GOOGL/AMZN/META (7/16, tripwire-only) -> VULCAN
        "agents": {"REGINALD", "VULCAN"},
        "evidence": "fetch_edgar_8k.py TARGETS (5 banks + MU + 4 hyperscalers)",
    },
}


def die(msg):
    print(f"ERROR: {msg} — fail-loud, not silently clean.", file=sys.stderr)
    sys.exit(2)


def load_active_roster():
    """Parse the ACTIVE table from PROME/ROSTER.md -> {AGENT: domain}."""
    if not os.path.exists(ROSTER):
        die(f"canonical roster missing at {os.path.relpath(ROSTER, REPO)}")
    text = open(ROSTER, encoding="utf-8").read()
    m = re.search(r"^## ACTIVE\b.*?$(.*?)(?=^## )", text, re.M | re.S)
    if not m:
        die("ROSTER.md has no '## ACTIVE' section (structure changed?)")
    agents = {}
    for line in m.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not re.fullmatch(r"[A-Z][A-Z0-9]{2,}", cells[0]):
            continue  # header/separator/footnote rows
        agents[cells[0]] = cells[1]
    if len(agents) < 15:
        die(f"parsed only {len(agents)} ACTIVE agents from ROSTER.md — "
            f"table format likely changed, refusing to report on a partial read")
    return agents


def load_query_coverage(lane_dir):
    """ast-parse GOOGLE_NEWS_QUERIES -> ({AGENT: [labels]}, [config_agent_names])."""
    cfg = os.path.join(lane_dir, "scripts", "newsweep_config.py")
    if not os.path.exists(cfg):
        die(f"lane clone has no scripts/newsweep_config.py at {lane_dir}")
    try:
        tree = ast.parse(open(cfg, encoding="utf-8").read())
    except SyntaxError as e:
        die(f"newsweep_config.py unparseable: {e}")
    queries = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "GOOGLE_NEWS_QUERIES":
                    try:
                        queries = ast.literal_eval(node.value)
                    except ValueError as e:
                        die(f"GOOGLE_NEWS_QUERIES not a pure literal: {e}")
    if not queries:
        die("GOOGLE_NEWS_QUERIES not found (or empty) in newsweep_config.py")
    cov, named = {}, set()
    for q in queries:
        agents = q.get("agents", [])
        named.update(agents)
        if agents == ["ALL"]:
            continue  # market-wide catch-alls are not domain coverage
        for a in agents:
            cov.setdefault(a, []).append(q.get("label", "?"))
    return cov, named


def main():
    ap = argparse.ArgumentParser(description="Lane coverage doctor (INFO severity).")
    ap.add_argument("--lane-dir", default=os.environ.get("RESEARCH_INTAKE_DIR", LANE_DEFAULT),
                    help="path to the RESEARCH-INTAKE clone (default: ~/Research-Intake "
                         "or $RESEARCH_INTAKE_DIR; machine-local inventory: PROME/MACHINE_LOCAL.md)")
    ap.add_argument("--quiet", action="store_true", help="print INFO findings only")
    args = ap.parse_args()

    if not os.path.isdir(args.lane_dir):
        die(f"RESEARCH-INTAKE clone not found at {args.lane_dir} "
            f"(pass --lane-dir or set $RESEARCH_INTAKE_DIR; see PROME/MACHINE_LOCAL.md)")

    active = load_active_roster()
    qcov, named_in_config = load_query_coverage(args.lane_dir)

    feed_cov = {}
    for feed, spec in STRUCTURED_FEEDS.items():
        for a in spec["agents"]:
            feed_cov.setdefault(a, []).append(feed)

    findings, covered = [], []
    for agent, domain in sorted(active.items()):
        if agent in SYNTHESIS_EXCLUDE:
            continue
        via = []
        if agent in qcov:
            via.append(f"queries[{', '.join(sorted(set(qcov[agent])))}]")
        if agent in feed_cov:
            via.append(f"feeds[{', '.join(sorted(feed_cov[agent]))}]")
        if via:
            covered.append((agent, domain, " + ".join(via)))
        else:
            findings.append(
                f"INFO: no autonomous lane collection for {agent} ({domain}) — "
                f"intake reaches this domain via Will's channel + the agent's own pulls only")

    # Drift catch: config names an agent the ACTIVE roster doesn't know.
    for a in sorted(named_in_config - set(active) - {"ALL"}):
        findings.append(
            f"INFO: newsweep_config names {a!r} in an agents list but it is not in the "
            f"ROSTER ACTIVE table — retired/renamed agent or typo; review the query row")

    if not args.quiet:
        print(f"Lane coverage — {len(active)} ACTIVE roster agents, "
              f"{len(SYNTHESIS_EXCLUDE)} synthesis-class excluded "
              f"({', '.join(sorted(SYNTHESIS_EXCLUDE))}), "
              f"{len(covered)} covered, {len(findings)} INFO finding(s).\n")
        for agent, domain, via in covered:
            print(f"  ✅ {agent:<9} {via}")
        print()
    for f in findings:
        print(f"  ◦ {f}")
    if findings and not args.quiet:
        print("\n(INFO severity by design: an un-laned domain is a routing fact, "
              "not a failure — some are deliberate, e.g. prediction-market feeds are parked.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
