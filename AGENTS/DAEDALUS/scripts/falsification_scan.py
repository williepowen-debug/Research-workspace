#!/usr/bin/env python3
"""Falsification Freshness Sweep — detection layer (sweep #3, playbook sweeps/FALSIFICATION_SWEEP.md).

Answers ONE question per surface: does this falsification surface still describe the LIVE thesis?
Sweep #1 (ledger_staleness) asks "is this ledger two-state clean?" — a file-level question a
hygiene edit can launder. This asks a CONTENT-consistency question and is therefore keyed on
IN-CONTENT stamps only, NEVER mtime or git-time (PAT-039 two instances, PAT-044; and
`finding_mtime_is_corrupted_by_git_sync` — git pull restamps mtime, so mtime fails FALSE-NEGATIVE).

DETECTION ONLY. Emits verdicts; mutates nothing. Dispositions are packet-only per the playbook —
re-scoping kill criteria is DOMAIN judgment, and the dormant-freeze pre-approval does NOT extend
to this sweep, because a wrong "fix" here silently changes what would falsify a live thesis.

Design commitments (PAT-074 — audit a check by what its PASS means):
  * A surface with NO parseable in-content stamp is UNSTAMPED, never CURRENT. "No date found"
    is not evidence of freshness; it is the absence of evidence, and it is reported as its own class.
  * Output states what was searched and what was skipped — counts for every class, always.
  * A dead-state banner (STATE_VOCABULARY class 1) is FROZEN-OK: a deliberately frozen surface is
    correct, not stale. That is the whole point of the two-state rule.

cwd-proof (PAT-031). Usage:
    python3 falsification_scan.py                # table, flags first
    python3 falsification_scan.py --tsv          # machine-readable
    python3 falsification_scan.py --agent BRENT  # single agent
"""
import os, re, sys
from datetime import date, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
AGENTS = REPO / "AGENTS"
DIRECTORY = REPO / "AGENTS" / "DAEDALUS" / "FLEET_DIRECTORY.md"

STALE_DAYS = 21          # playbook threshold 2: stamp >21d older than live STATUS while ACTIVE
HEADER_LINES = 18        # a surface's OWN stamp lives in its header block, not in its event prose

# Falsification-surface classes (playbook §3). Matched on path, relative to the agent dir.
SURFACE_PATTERNS = [
    (re.compile(r"(^|/)(THESIS|THESIS_VALIDATION|EXIT_PROTOCOL|COUNTER_THESIS)\.md$", re.I), "thesis/validation"),
    (re.compile(r"(^|/)KILL[_A-Z0-9]*\.(md|tsv)$", re.I), "kill tree/memo"),
    (re.compile(r"(^|/)(FALSIFICATION|CONVICTION)[_A-Z0-9]*\.(md|tsv)$", re.I), "falsification/conviction"),
    (re.compile(r"(^|/)CHANGELOG\.md$", re.I), "changelog/pivot log"),
]
# Subtrees that are NOT live falsification rails (packets, corpora, drafts, dead trees).
# 2026-08-17 (SAM review, reader sam-ledgers): bare `red` REMOVED — SAM's red/ is a LIVE
# adversarial rail (COUNTER_THESIS.md is even named in SURFACE_PATTERNS above; the exclusion
# silently won over the include, hiding a 48d-stale rail with >=3 dead keys from sweep #3).
# handoff_RED (packet lane) stays excluded.
EXCLUDE = re.compile(r"(^|/)(_archive|archive|archived|sources|raw|processed|delivered|inbox|outbox"
                     r"|research|reports|proposals|handoff_RED|audits|output|outputs|prompts"
                     r"|builds|domain|sweeps|BLUEPRINTS|templates|\.git)(/|$)", re.I)

# ── Two surface KINDS, two correct vintage rules. Conflating them is a defect in both directions.
#
#  STATE surfaces (thesis, validation doc, exit protocol, kill memo) DESCRIBE a current state, so
#  their vintage is the HEADER's own freshness claim. Reading their newest interior date instead
#  launders them fresh off an event date in the criteria (the HENRY case).
#
#  APPEND-ONLY surfaces (changelogs, decision logs, TSV ledgers) ACCRUE, so their vintage is their
#  NEWEST ENTRY. Reading their header instead reports their BIRTH date as their age — which flagged
#  WALTER's filtered/kill_log.tsv at 106d when its last row is dated yesterday (349 rows, live).
#  Found by opening the file rather than trusting the verdict.
APPEND_ONLY = re.compile(r"(CHANGELOG|_LOG|LOG)\.(md|tsv)$|\.tsv$", re.I)
#  ...and an append-only MARKDOWN log is dated by its newest ENTRY HEADING, not by the newest date
#  anywhere in the file. Prose inside an entry cites later events than the entry itself, so a
#  whole-file max() launders a dead log fresh — LIQUID's pivot log stops at "## v2.0 — 2026-05-19"
#  (76d, the 7/11 pilot's unfixed finding) but carries 2026-06-25 in that entry's body. Third
#  defect of one family found in this instrument in one run: "which date belongs to the surface?"
ENTRY_HEADING = re.compile(r"^#{2,4}\s+.*$", re.M)
#  EVENT logs fill ONLY when the world does something. Age measures the WORLD, not the surface, so
#  an old one is not rot — WALTER's FALSIFICATION_FIRED_LOG has 3 rows and no fire since 2026-06-04,
#  which is a fact about triggers not firing. Flagging it would punish a correctly-quiet ledger.
EVENT_LOG = re.compile(r"(FIRED|FIRE)_?LOG", re.I)

# 2026-08-17 (SAM review): banner FORM, not bare word — a live thesis NARRATING a channel
# retirement ("...TAIL IS RETIRED TO LOW.") was classified as a dead doc. A real banner is
# line-anchored (canon: prepend "FROZEN <date> — ...", possibly behind #/>/**/emoji prefixes)
# OR the token is immediately followed by an ISO date ("FROZEN 2026-07-01" mid-line legacy).
DEAD_BANNER = re.compile(
    r"(?:^[\s>#*_\-—⛔🔴🟠⚠️✅\[\('\"]*(?:FROZEN|SUPERSEDED|RETIRED|ARCHIVED(?: SNAPSHOT)?|DEPRECATED)\b"
    r"|\b(?:FROZEN|SUPERSEDED|RETIRED|ARCHIVED(?: SNAPSHOT)?|DEPRECATED)\s+20\d{2}-\d{2}-\d{2})",
    re.M)
ISO = re.compile(r"(20\d{2})-(\d{2})-(\d{2})")
US = re.compile(r"\b(\d{1,2})/(\d{1,2})(?:/(\d{2,4}))?\b")
VERSION = re.compile(r"\bv(\d+)\.(\d+)\b", re.I)
VERSION_FIELD = re.compile(r"\*\*Version:\*\*\s*(\d+)\.(\d+)", re.I)

TODAY = date.today()


def read(p, limit=None):
    try:
        with open(p, encoding="utf-8", errors="ignore") as f:
            return "".join(f.readlines()[:limit]) if limit else f.read()
    except OSError:
        return ""


def dates_in(text, year_hint=None):
    """Every parseable date, ISO first then US M/D (year inferred — the fleet writes '(7/17)')."""
    out = []
    for m in ISO.finditer(text):
        try:
            out.append(date(int(m.group(1)), int(m.group(2)), int(m.group(3))))
        except ValueError:
            pass
    for m in US.finditer(text):
        mo, dy, yr = int(m.group(1)), int(m.group(2)), m.group(3)
        if not (1 <= mo <= 12 and 1 <= dy <= 31):
            continue
        if yr:
            yr = int(yr) + 2000 if int(yr) < 100 else int(yr)
        else:
            yr = year_hint or TODAY.year
        try:
            d = date(yr, mo, dy)
        except ValueError:
            continue
        if d <= TODAY:            # a bare M/D in the future is almost always a next-year artifact
            out.append(d)
    return out


def newest(text, year_hint=None):
    ds = [d for d in dates_in(text, year_hint) if d <= TODAY]
    return max(ds) if ds else None


# A surface's OWN freshness claim is a LABELLED date. Un-labelled dates in a falsification
# header are usually EVENT dates inside the criteria ("June CPI (7/14) core hot") — taking
# max() over them launders a stale surface as fresh. Found live on HENRY's THESIS_VALIDATION:
# self-stamped "as of 2026-06-23" (41d) but graded CURRENT/17d off a 7/14 CPI reference
# sitting in a confirm-criterion. Same class as PAT-044, one layer down.
STAMP_LABEL = re.compile(
    r"(last\s+updated|updated|as\s+of|reframed|rewritten|rewrite|revised|revision|built|created"
    r"|current\s+state|refreshed|refresh|stamp(?:ed)?|version|vintage|run)\b[^\n]{0,40}?"
    r"(20\d{2}-\d{2}-\d{2}|\b\d{1,2}/\d{1,2}(?:/\d{2,4})?\b)", re.I)


def labelled_stamp(text, year_hint=None):
    """Newest date that carries an explicit freshness LABEL. None if the header makes no claim."""
    found = []
    for m in STAMP_LABEL.finditer(text):
        found.extend(dates_in(m.group(2), year_hint))
    found = [d for d in found if d <= TODAY]
    return max(found) if found else None


def live_thesis(agent_dir):
    """(version_tuple, date, path, bannered) for the agent's thesis file, if it has one.

    ⚠️ A thesis file can itself be dead-bannered — REGINALD's `thesis/THESIS.md` leads with
    'STALE-VINTAGE — v1.4 ... The LIVE thesis lives in STATUS.md. Do NOT cite anything below as
    current.' Reading its version as the LIVE version makes every child surface look measured
    against canon when the reference is itself retired. Same class as the surfaces this sweep
    hunts, one level up: the reference must be checked for the defect being detected.
    """
    for cand in ("thesis/THESIS.md", "THESIS.md"):
        p = agent_dir / cand
        if not p.exists():
            continue
        head = read(p, HEADER_LINES)
        m = VERSION_FIELD.search(head) or VERSION.search(head)
        ver = (int(m.group(1)), int(m.group(2))) if m else None
        bannered = bool(DEAD_BANNER.search(head)) or "STALE-VINTAGE" in head.upper()
        if bannered:
            ver = None          # never grade a child against a retired parent version
        return ver, newest(head), p, bannered
    return None, None, None, False


def status_date(agent_dir):
    p = agent_dir / "STATUS.md"
    return newest(read(p, HEADER_LINES)) if p.exists() else None


def groups():
    """ACTIVE / TIER-2 / DORMANT / SPECIAL from the generated FLEET_DIRECTORY (my own artifact)."""
    g, cur = {}, None
    if not DIRECTORY.exists():
        sys.exit(f"falsification_scan: FAIL — {DIRECTORY} missing; run render_directory.py first")
    for line in DIRECTORY.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            head = line[3:]
            for key in ("ACTIVE", "TIER-2", "DORMANT", "SPECIAL"):
                if key in head:
                    cur = key
            continue
        if cur and line.startswith("| ") and not line.startswith("| Agent") and "---" not in line:
            name = line.strip("|").split("|")[0].strip()
            if re.fullmatch(r"[A-Z][A-Z0-9]+", name):
                g[name] = cur
    if not g:
        sys.exit("falsification_scan: FAIL — parsed 0 agents from FLEET_DIRECTORY (format changed?)")
    return g


def surfaces(agent_dir):
    out = []
    for root, dirs, files in os.walk(agent_dir):
        rel_root = os.path.relpath(root, agent_dir).replace(os.sep, "/")
        rel_root = "" if rel_root == "." else rel_root
        if rel_root and EXCLUDE.search(rel_root):
            dirs[:] = []
            continue
        for fn in files:
            rel = f"{rel_root}/{fn}" if rel_root else fn
            for pat, cls in SURFACE_PATTERNS:
                if pat.search(rel):
                    out.append((rel, cls))
                    break
    return sorted(out)


def scan_agent(name, group):
    agent_dir = AGENTS / name
    ver, tdate, tpath, tbannered = live_thesis(agent_dir)
    sdate = status_date(agent_dir)
    # The clock a surface is judged against. If the thesis file is itself dead-bannered its date
    # is NOT a live clock, so STATUS is the only admissible reference.
    live_ref = sdate if (sdate or tbannered) else tdate
    rows = []
    for rel, cls in surfaces(agent_dir):
        p = agent_dir / rel
        if tpath and p == tpath:
            continue                              # the thesis is the reference, not a surface
        head = read(p, HEADER_LINES)
        append_only = bool(APPEND_ONLY.search(rel))
        event_log = bool(EVENT_LOG.search(rel))
        if append_only:
            body = read(p)                    # vintage = NEWEST ENTRY, not the header's birth date
            if rel.lower().endswith(".md"):
                headings = "\n".join(ENTRY_HEADING.findall(body))
                stamp = newest(headings)      # the entries' own dates only
                loose = newest(body)          # body prose — used to detect laundering below
                if stamp is None:
                    stamp, loose = loose, loose
            else:
                stamp, loose = newest(body), newest(body)
        else:
            stamp = labelled_stamp(head)      # the surface's own freshness CLAIM
            loose = newest(head)              # any date at all, incl. event dates in criteria
        inferred = False
        if stamp is None and loose is not None:
            stamp, inferred = loose, True     # no claim made: fall back, and SAY it was inferred
        banner = bool(DEAD_BANNER.search(head))
        m = VERSION.search(head)
        cited = (int(m.group(1)), int(m.group(2))) if m else None
        age = (live_ref - stamp).days if (stamp and live_ref) else None
        # A labelled stamp much older than the newest date present = the laundering signature.
        launder = (not inferred and stamp and loose and (loose - stamp).days > STALE_DAYS)

        if banner:
            verdict, why = "FROZEN-OK", "dead-state banner in header — deliberately frozen, not rot"
        elif event_log:
            verdict, why = "EVENT-LOG", (
                f"fills only when a trigger fires (last entry {stamp or 'none'}) — age measures the "
                "WORLD, not the surface; not a staleness signal. Whether nothing SHOULD have fired "
                "is a domain question for the owner, not this sweep")
        elif stamp is None:
            verdict, why = "UNSTAMPED", f"no parseable date in first {HEADER_LINES} lines — cannot be judged fresh"
        elif group == "DORMANT":
            verdict, why = "DORMANT-SKIP", "dormant agent: surface may lag legitimately (check the dormant book's own clock)"
        elif age is not None and age > STALE_DAYS:
            verdict, why = "STALE-FLAGGED", f"stamp {stamp} is {age}d behind live ref {live_ref} (threshold {STALE_DAYS}d)"
        elif cited and ver and (ver[0] - cited[0]) * 100 + (ver[1] - cited[1]) > 1:
            verdict, why = "STALE-FLAGGED", f"cites v{cited[0]}.{cited[1]} vs live v{ver[0]}.{ver[1]} — >1 revision behind"
        else:
            verdict, why = "CURRENT", f"stamp {stamp}" + (f", {age}d behind ref" if age is not None else "")
        if append_only and verdict in ("CURRENT", "STALE-FLAGGED"):
            why += " — vintage = NEWEST ENTRY (append-only surface)"
        if inferred and verdict in ("CURRENT", "STALE-FLAGGED"):
            why += " — ⚠ stamp INFERRED (no labelled freshness claim in header; may be an event date)"
        if launder:
            why += (f" — ⚠ header also carries {loose}, {(loose - stamp).days}d newer than its own "
                    "stamp: check which one describes the surface")
        rows.append(dict(agent=name, group=group, surface=rel, cls=cls, verdict=verdict,
                         stamp=stamp, live_ref=live_ref, age=age,
                         cited=f"v{cited[0]}.{cited[1]}" if cited else "-",
                         live_ver=(f"v{ver[0]}.{ver[1]}" if ver else
                                   ("thesis-BANNERED" if tbannered else "-")), why=why))
    return rows, (ver, tdate, sdate, tbannered)


ORDER = {"STALE-FLAGGED": 0, "UNSTAMPED": 1, "CURRENT": 2, "FROZEN-OK": 3,
         "EVENT-LOG": 4, "DORMANT-SKIP": 5}


def main():
    g = groups()
    only = None
    if "--agent" in sys.argv:
        try:
            only = sys.argv[sys.argv.index("--agent") + 1].upper()
        except IndexError:
            print("🔴 falsification_scan CANNOT-CERTIFY: --agent given with no name (usage: --agent NAME)")
            return 2
        if only not in g:
            print(f"🔴 falsification_scan CANNOT-CERTIFY: agent {only!r} not in FLEET_DIRECTORY — "
                  f"0 surfaces scanned (a typo here previously produced a clean-looking zero report)")
            return 2
    rows, no_rail, no_thesis, no_clock, bannered_thesis = [], [], [], [], []
    for name, grp in sorted(g.items()):
        if only and name != only:
            continue
        if not (AGENTS / name).is_dir():
            continue
        r, (ver, tdate, sdate, tbannered) = scan_agent(name, grp)
        if not r:
            # Two very different zeros — never collapse them. "Has a thesis but no separate
            # falsification surface" is a FINDING (the rail must live inside STATUS/TRADE, or
            # nowhere); "no thesis-class file at all" is expected for utility/meta agents.
            (no_rail if live_thesis(AGENTS / name)[2] else no_thesis).append(name)
        if tbannered:
            bannered_thesis.append(name)
        if not (sdate or tdate):
            no_clock.append(name)
        rows.extend(r)
    rows.sort(key=lambda r: (ORDER.get(r["verdict"], 9), r["agent"], r["surface"]))

    if "--tsv" in sys.argv:
        print("Agent\tGroup\tSurface\tClass\tVerdict\tStamp\tLiveRef\tAgeDays\tCitedVer\tLiveVer\tWhy")
        for r in rows:
            print(f"{r['agent']}\t{r['group']}\t{r['surface']}\t{r['cls']}\t{r['verdict']}"
                  f"\t{r['stamp'] or '-'}\t{r['live_ref'] or '-'}\t{r['age'] if r['age'] is not None else '-'}"
                  f"\t{r['cited']}\t{r['live_ver']}\t{r['why']}")
        # NOT-looked-at layer in BOTH modes (PAT-074; self-audit F15 — this mode previously
        # dropped it, contradicting the docstring). '#'-prefixed = comment rows, parsers skip.
        print(f"# NO-RAIL ({len(no_rail)}): {', '.join(no_rail) or 'none'} — thesis w/o separate rail, candidate findings")
        print(f"# NO-THESIS ({len(no_thesis)}): {', '.join(no_thesis) or 'none'} — falsification n/a (utility/meta)")
        print(f"# BANNERED-THESIS ({len(bannered_thesis)}): {', '.join(bannered_thesis) or 'none'} — graded on STATUS clock")
        print(f"# NO-CLOCK ({len(no_clock)}): {', '.join(no_clock) or 'none'} — age comparisons unavailable")
    else:
        counts = {}
        for r in rows:
            counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
        scanned = len({r["agent"] for r in rows})
        print(f"# Falsification Freshness Sweep — detection layer · run {TODAY} · in-content stamps only\n")
        print(f"**Searched:** {len(rows)} falsification surfaces across {scanned} agents "
              f"(of {len(g)} in FLEET_DIRECTORY) · threshold {STALE_DAYS}d behind live STATUS/thesis ref\n")
        print("| Verdict | N |")
        print("|---|---:|")
        for k in sorted(counts, key=lambda k: ORDER.get(k, 9)):
            print(f"| {k} | {counts[k]} |")
        print("\n| Agent | Surface | Class | Verdict | Stamp | Ref | Age | Cited/Live | Why |")
        print("|---|---|---|---|---|---|---:|---|---|")
        for r in rows:
            if r["verdict"] in ("CURRENT", "FROZEN-OK", "DORMANT-SKIP", "EVENT-LOG"):
                continue
            print(f"| {r['agent']} | `{r['surface']}` | {r['cls']} | **{r['verdict']}** "
                  f"| {r['stamp'] or '—'} | {r['live_ref'] or '—'} | {r['age'] if r['age'] is not None else '—'} "
                  f"| {r['cited']}/{r['live_ver']} | {r['why']} |")
        # What was NOT looked at — always printed, never inferred from silence (PAT-074).
        print(f"\n**⚠ HAS A THESIS, NO SEPARATE FALSIFICATION SURFACE ({len(no_rail)}):** "
              f"{', '.join(no_rail) if no_rail else 'none'}. **These are candidate findings, not clean rows.** "
              "The agent carries a live thesis but no kill tree / exit protocol / validation doc this pattern "
              "set can find — so its falsification rail is either embedded in STATUS/TRADE prose (unenforceable "
              "by any surface-level check) or absent. Judgment read required per agent.")
        print(f"\n**No thesis-class file — falsification not applicable ({len(no_thesis)}):** "
              f"{', '.join(no_thesis) if no_thesis else 'none'}. Expected for utility/meta agents.")
        if bannered_thesis:
            print(f"\n**Thesis file is itself dead-bannered ({len(bannered_thesis)}):** "
                  f"{', '.join(bannered_thesis)} — STATUS.md is canonical for these, so their child "
                  "surfaces are graded on the STATUS clock and NO live thesis version is asserted. "
                  "A version comparison against a retired parent would read as conformance.")
        if no_clock:
            print(f"\n**No live reference clock:** {', '.join(no_clock)} — no parseable date in STATUS.md "
                  "or thesis header, so age comparisons are unavailable for them.")

    # §9 rc contract (adopted 2026-08-17 self-audit C3 — previously always None/0; exited 0
    # with 3 STALE-FLAGGED live). Findings = stale/unstamped rows or thesis-without-rail.
    flagged = [r for r in rows if r["verdict"] in ("STALE-FLAGGED", "UNSTAMPED")]
    return 1 if (flagged or no_rail) else 0


if __name__ == "__main__":
    sys.exit(main())
