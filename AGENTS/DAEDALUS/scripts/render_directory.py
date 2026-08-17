#!/usr/bin/env python3
"""render_directory.py — generate AGENTS/DAEDALUS/FLEET_DIRECTORY.md.

The fleet's readable at-a-glance map: per agent — what it is, what it does, is it active, what's it
missing. The charter Job #3 deliverable (plan: upgrades/FLEET_DIRECTORY_BUILD_PLAN.md).

Single source of truth per column (PAT-006 — the directory JOINS, never duplicates):
  - existence + domain ("what it does") + status  <-  PROME/ROSTER.md   (PROME owns who-exists)
  - class + maturity level + missing/next          <-  FLEET_MAP.tsv     (DAEDALUS owns gaps)

Reliability (why this can be trusted, not just maintained):
  - FAILS LOUD on structural breakage (ROSTER table format changed / FLEET_MAP schema changed).
  - FAILS LOUD on any unhandled FLEET_MAP-only agent — a new real agent can never silently vanish;
    it must be either SPECIAL-mapped (prose in ROSTER) or explicitly DROPped (retired).
  - REVERSE guard (2026-08-17 self-audit F14): an ACTIVE/TIER-2 ROSTER agent with NO FLEET_MAP row
    renders an explicit "⚠️ UNGRADED" cell (never a blank identical to by-design dormant) and the
    generator exits rc=1 after writing. Live trigger this guards: PAT-047 registration order lands
    the ROSTER row before the FLEET_MAP row. DORMANT blanks remain by design.
  - Regenerated each Production Review (sweeps/PRODUCTION_REVIEW.md) so the artifact can't rot.

cwd-proof: self-locates repo root from __file__ (PAT-031). Writes FLEET_DIRECTORY.md; prints a summary.
"""
from pathlib import Path
from datetime import date
import sys

REPO = Path(__file__).resolve().parents[3]
ROSTER = REPO / "PROME" / "ROSTER.md"
FLEETMAP = REPO / "AGENTS" / "DAEDALUS" / "FLEET_MAP.tsv"
OUT = REPO / "AGENTS" / "DAEDALUS" / "FLEET_DIRECTORY.md"

# ROSTER '## ' headers that carry an Agent|Domain table -> (group label, status glyph).
GROUPS = {
    "ACTIVE":  ("ACTIVE — persistent domain owners", "\U0001F7E2"),
    "TIER-2":  ("TIER-2 — spawned as needed",        "\U0001F7E1"),
    "DORMANT": ("DORMANT — revive only on explicit need", "⚪"),
}
GROUP_ORDER = ["ACTIVE", "TIER-2", "DORMANT"]

# SPECIAL agents live as PROSE in ROSTER (no table row) but ARE in FLEET_MAP. Domain hardcoded
# (small, slow-changing set); class/level/missing still render FROM FLEET_MAP. New SPECIAL agent -> add here.
SPECIAL = {
    "DAEDALUS": "Fleet architect — design / structure / maturity / lifecycle",
    "YEYOU":    "Repo-wide reviewer (manual / branch model)",
    "RAV":      "Deep factual/analytical reviewer + bounded repair (Codex, Will-driven)",
}
SPECIAL_HDR = ("SPECIAL — meta / cross-fleet (on-demand)", "\U0001F535")
DROP = {"HERMES"}  # retired (folder removed); directory lists LIVE agents only.


def die(msg):
    sys.exit(f"render_directory: FAIL — {msg}")


def parse_roster(path):
    if not path.exists():
        die(f"ROSTER not found at {path}")
    agents, cur = {}, None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("## "):
            head = line[3:].strip()
            cur = next((k for k in GROUPS if head.startswith(k)), None)
            continue
        if cur and line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 2:
                continue
            name, domain = cells[0], cells[1]
            if name == "Agent" or not name or set(name) <= set("-: "):
                continue
            if name in agents:
                die(f"duplicate agent {name!r} across ROSTER tables")
            agents[name] = (cur, domain)          # preserves file order
    if not agents:
        die("no agent rows parsed from ROSTER — table format may have changed (STRUCTURAL)")
    return agents


def parse_fleetmap(path):
    if not path.exists():
        die(f"FLEET_MAP not found at {path}")
    rows = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.startswith("#"):
            continue
        cells = raw.split("\t")
        if cells[0].strip() == "Agent":
            continue
        if len(cells) < 8:
            die(f"FLEET_MAP row {cells[0]!r} has {len(cells)} cols (<8) — schema changed (STRUCTURAL)")
        rows[cells[0].strip()] = (cells[1].strip(), cells[2].strip(), cells[7].strip())  # Class, Level, Next
    if not rows:
        die("no data rows parsed from FLEET_MAP")
    return rows


def truncate(s, n=72):
    """First clause of a dense cell, hard-capped (v1 one-liner — Will-approved).
    Cut at the earliest clause boundary that still keeps real substance (>=25 chars);
    else hard-cap with an ellipsis. Recognizes both '->' and unicode '→'."""
    s = " ".join(s.split())
    if len(s) <= n:
        return s
    best = None
    for sep in (" → ", " -> ", " + ", "; ", ". "):
        i = s.find(sep)
        if 25 <= i <= n:
            best = i if best is None else min(best, i)
    return s[:best].strip() if best else s[:n - 1].rstrip() + "…"


def md_cell(s):
    return s.replace("|", "\\|").strip() or "—"


def row(agent, klass, lvl, does, missing):
    return f"| {agent} | {md_cell(klass)} | {md_cell(lvl)} | {md_cell(does)} | {md_cell(missing)} |"


def main():
    roster = parse_roster(ROSTER)
    fleet = parse_fleetmap(FLEETMAP)

    # Reliability guard: every FLEET_MAP agent absent from ROSTER tables MUST be handled.
    fleet_only = set(fleet) - set(roster)
    unhandled = fleet_only - set(SPECIAL) - DROP
    if unhandled:
        die(f"unhandled FLEET_MAP-only agent(s) {sorted(unhandled)} — add to SPECIAL map or DROP set "
            f"(guard against a real agent silently vanishing from the directory)")

    stamp = date.today().isoformat()
    ungraded = []
    L = []
    L.append("# FLEET DIRECTORY — what every agent is, does, and is missing")
    L.append("")
    L.append(f"> **GENERATED — DO NOT EDIT.** Rendered from `PROME/ROSTER.md` (existence · domain · status) "
             f"+ `AGENTS/DAEDALUS/FLEET_MAP.tsv` (class · maturity · missing/next) by "
             f"`AGENTS/DAEDALUS/scripts/render_directory.py`. Edit the **sources**, then regenerate — "
             f"hand-edits are overwritten. Generated {stamp}.")
    L.append("")
    L.append("*One source of truth per column (PAT-006): **what it does** + **status** ← ROSTER (PROME); "
             "**class** + **maturity level** + **missing/next** ← FLEET_MAP (DAEDALUS). \"Missing / next\" is a "
             "truncated one-liner — full gap detail in `FLEET_MAP.tsv` + `upgrades/<AGENT>_CARD.md`. "
             "Dormant agents are un-graded → blank grade cells; an ACTIVE/TIER-2 agent missing its "
             "FLEET_MAP row renders ⚠️ UNGRADED and the generator exits nonzero — a blank there is never "
             "by-design. PROME graded 2026-07-28 (Will-ratified, "
             "judgment-read only — the scripted floor cannot see a root-level agent).*")
    L.append("")

    counts = {}
    for gkey in GROUP_ORDER:
        title, glyph = GROUPS[gkey]
        members = [a for a, (g, _) in roster.items() if g == gkey]
        counts[gkey] = len(members)
        L.append(f"## {glyph} {title}")
        L.append("")
        L.append("| Agent | Class | Lvl | What it does | Missing / next |")
        L.append("|---|---|---|---|---|")
        for a in members:
            _, does = roster[a]
            if a in fleet:
                klass, lvl, nxt = fleet[a]
                L.append(row(a, klass, lvl, does, truncate(nxt)))
            elif gkey == "DORMANT":                # dormant ungraded — blank grade, by design
                L.append(row(a, "—", "—", does, "—"))
            else:                                  # ACTIVE/TIER-2 with no FLEET_MAP row — loud, never blank
                ungraded.append(a)
                L.append(row(a, "⚠️", "⚠️", does, "⚠️ UNGRADED — in ROSTER, no FLEET_MAP row (register it)"))
        L.append("")

    # SPECIAL group (FLEET_MAP-only, prose in ROSTER)
    title, glyph = SPECIAL_HDR
    counts["SPECIAL"] = len(SPECIAL)
    L.append(f"## {glyph} {title}")
    L.append("")
    L.append("| Agent | Class | Lvl | What it does | Missing / next |")
    L.append("|---|---|---|---|---|")
    for a, does in SPECIAL.items():
        if a not in fleet:
            die(f"SPECIAL agent {a!r} not in FLEET_MAP — cannot render its grade")
        klass, lvl, nxt = fleet[a]
        L.append(row(a, klass, lvl, does, truncate(nxt)))
    L.append("")

    L.append("---")
    L.append(f"*{counts['ACTIVE']} active · {counts['TIER-2']} tier-2 · {counts['DORMANT']} dormant · "
             f"{counts['SPECIAL']} special. Dropped (retired): {', '.join(sorted(DROP))}. "
             f"Regenerated each Production Review — `sweeps/PRODUCTION_REVIEW.md`.*")
    L.append("")

    OUT.write_text("\n".join(L), encoding="utf-8")
    total = sum(counts.values())
    print(f"wrote {OUT.relative_to(REPO)}  ({total} agents: {counts}; dropped {sorted(DROP)})")
    if ungraded:
        print(f"⚠️  REVERSE-GUARD: {len(ungraded)} ACTIVE/TIER-2 agent(s) have NO FLEET_MAP row: "
              f"{sorted(ungraded)} — rendered ⚠️ UNGRADED; register them (PAT-047 tail)")
        sys.exit(1)


if __name__ == "__main__":
    main()
