#!/usr/bin/env python3
"""
DAEDALUS maturity scanner — objective L0-L2 floor + structural signals for L3-L5.

Read-only. Computes the deterministic, rerunnable layer of the fleet maturity map
(SPEC.md §5). It does NOT make quality judgments — it reports presence/shape/recency
signals; DAEDALUS (the agent) judges the L3-L5 ceiling from these.

Usage:
    python3 AGENTS/DAEDALUS/scripts/maturity_scan.py            # markdown table to stdout
    python3 AGENTS/DAEDALUS/scripts/maturity_scan.py --tsv      # tsv (FLEET_MAP signal rows)

Staleness is measured in commits-behind-HEAD-date (robust to wall-clock skew), not
against the system clock.
"""
import os, re, subprocess, sys

REPO = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                      capture_output=True, text=True).stdout.strip()
AGENTS = os.path.join(REPO, "AGENTS")

# Class map from PROME/ROSTER.md (active+tier2+dormant). Default = Market.
# DAEDALUS references ROSTER for active/dormant; class here is design-class only.
CLASS = {
    "PROME": "Meta", "DAEDALUS": "Meta",
    "WALTER": "Utility", "NEXUS": "Utility", "TERRY": "Utility", "ORACLE": "Utility",
    "RED": "Utility", "YEYOU": "Utility", "DEWEY": "Utility", "HERMES": "Utility",
    # everything else market-domain
}
# Dirs that are not live agents (archives, sources, scaffolds).
SKIP = {"ATHENA", "BARON", "CRUISE", "FERT", "REITS", "TRADES", "SENTRY", "OZK", "ZHAO"}

def sh(args):
    return subprocess.run(args, capture_output=True, text=True, cwd=REPO).stdout

def head_commit_epoch():
    return int(sh(["git", "log", "-1", "--format=%ct"]).strip() or 0)

HEAD_EPOCH = head_commit_epoch()

def agent_dirs():
    out = []
    for name in sorted(os.listdir(AGENTS)):
        p = os.path.join(AGENTS, name)
        if not os.path.isdir(p) or name.startswith("_") or name == "templates":
            continue
        if not (os.path.exists(os.path.join(p, "CLAUDE.md")) or
                os.path.exists(os.path.join(p, "STATUS.md"))):
            continue
        out.append(name)
    return out

def read(path):
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            return f.read()
    except FileNotFoundError:
        return None

def tsv_rows(path):
    txt = read(path)
    if not txt:
        return 0
    return max(0, len([l for l in txt.splitlines() if l.strip() and not l.startswith("#")]) - 1)

def days_behind_head(name):
    ts = sh(["git", "log", "-1", "--format=%ct", "--", f"AGENTS/{name}"]).strip()
    if not ts:
        return None
    return round((HEAD_EPOCH - int(ts)) / 86400, 1)

def commits_30d(name):
    # commits to this agent's path within ~30 days of HEAD date
    since = HEAD_EPOCH - 30 * 86400
    log = sh(["git", "log", f"--since={since}", "--format=%h", "--", f"AGENTS/{name}"])
    return len([l for l in log.splitlines() if l.strip()])

def scan(name):
    d = os.path.join(AGENTS, name)
    cls = CLASS.get(name, "Market")
    claude = read(os.path.join(d, "CLAUDE.md"))
    status = read(os.path.join(d, "STATUS.md"))
    s = status or ""
    wb = os.path.join(d, "workbook")
    sig = {
        "agent": name, "class": cls,
        "has_claude": claude is not None,
        "has_status": status is not None,
        "status_lines": len(s.splitlines()) if status else 0,
        "bottom_line": bool(re.search(r"BOTTOM LINE", s, re.I)),
        "convergence": bool(re.search(r"convergence matrix", s, re.I)),
        "exit_rules": bool(re.search(r"\b(exit|falsif)", s, re.I)),
        "session_counts": bool(re.search(r"\b\d+\+?\s*sessions?\b", s, re.I)),
        "has_workbook": os.path.isdir(wb),
        "tsv_records": sum(tsv_rows(os.path.join(d, f)) for f in os.listdir(d)
                           if f.endswith(".tsv")) if os.path.isdir(d) else 0,
        "kb_rows": tsv_rows(os.path.join(wb, "KB.tsv")),
        "pred_rows": tsv_rows(os.path.join(wb, "PREDICTIONS.tsv")),
        "pred_resolved": len(re.findall(r"\b(CONFIRMED|FAILED|PARTIALLY|EXPIRED)\b",
                                        read(os.path.join(wb, "PREDICTIONS.tsv")) or "")),
        "has_trade": os.path.exists(os.path.join(d, "TRADE.md")),
        "days_behind": days_behind_head(name),
        "commits_30d": commits_30d(name),
    }
    sig["floor"] = floor_level(sig)
    sig["gaps"] = conformance_gaps(sig)
    sig["proposed"] = proposed_level(sig)
    return sig

def floor_level(s):
    """Objective L0-L2 — class-independent STRUCTURAL PRESENCE (not conformance).
    Missing-a-required-section is a gap, NOT a demotion to skeleton (PAT-007)."""
    if not s["has_claude"]:
        return "—"
    if not s["has_status"] or s["status_lines"] < 15:
        return "L0"  # skeleton: no real live state
    # market record = workbook/KB; meta/utility record = any populated top-level .tsv (class-aware, PAT-008)
    has_record = s["kb_rows"] > 0 or s["has_workbook"] or s["tsv_records"] > 0
    if has_record:
        return "L2"
    return "L1"

def conformance_gaps(s):
    """Required-section / discipline gaps — debt flags, independent of level."""
    g = []
    if s["has_status"] and not s["bottom_line"]:
        g.append("no BOTTOM LINE")
    if s["status_lines"] > 260:
        g.append(f"STATUS {s['status_lines']}ln >cap")
    if s["class"] == "Market":
        if not s["convergence"]:
            g.append("no conv-matrix")
        if not s["exit_rules"]:
            g.append("no exit-rules")
        elif not s["session_counts"]:
            g.append("exit-rules lack session counts")
        if s["pred_rows"] > 0 and s["pred_resolved"] == 0:
            g.append("predictions unresolved")
    return "; ".join(g) or "—"

def proposed_level(s):
    """Mechanical hint toward L3-L5 from structural markers. DAEDALUS finalizes by judgment."""
    base = s["floor"]
    if base not in ("L2",):
        return base
    fresh = (s["commits_30d"] or 0) >= 8
    if s["class"] == "Market":
        l3 = s["convergence"] and s["exit_rules"] and s["pred_resolved"] > 0
        l4 = l3 and s["has_trade"] and fresh
        return "L4?" if l4 else ("L3?" if l3 else "L2")
    # Utility / Meta: role discipline proxied by freshness + bottom line + record
    if s["class"] in ("Utility", "Meta"):
        l3 = s["bottom_line"] and fresh
        l4 = l3 and (s["commits_30d"] or 0) >= 15
        return "L4?" if l4 else ("L3?" if l3 else "L2")
    return base

def main():
    rows = [scan(n) for n in agent_dirs() if n not in SKIP]
    rows.sort(key=lambda r: (r["class"], -(r["commits_30d"] or 0)))
    if "--tsv" in sys.argv:
        print("Agent\tClass\tFloor\tProposed\tStatusLines\tKB\tPredResolved\tTrade\tDaysBehind\tCommits30d")
        for r in rows:
            print(f"{r['agent']}\t{r['class']}\t{r['floor']}\t{r['proposed']}\t{r['status_lines']}"
                  f"\t{r['kb_rows']}\t{r['pred_resolved']}\t{'Y' if r['has_trade'] else '-'}"
                  f"\t{r['days_behind']}\t{r['commits_30d']}")
        return
    print(f"# Fleet maturity scan (objective layer) — {len(rows)} agents · HEAD-relative staleness\n")
    print("| Agent | Class | Floor | →L3-5? | 30d | Conformance gaps |")
    print("|---|---|---|---|---:|---|")
    for r in rows:
        print(f"| {r['agent']} | {r['class']} | {r['floor']} | {r['proposed']} "
              f"| {r['commits_30d']} | {r['gaps']} |")
    print("\n_Floor = objective structural presence (L0 skeleton · L1 live STATUS · L2 +structured record). "
          "→L3-5? = mechanical hint; DAEDALUS finalizes by reading. Gaps = conformance debt, independent of level._")

if __name__ == "__main__":
    main()
