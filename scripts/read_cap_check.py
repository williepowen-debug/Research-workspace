#!/usr/bin/env python3
"""read_cap_check.py — can this desk's BOOT-MANDATED reads be read WHOLE? (fleet tool, P1)

RULE (Will-approved 2026-08-28, verbatim "P1 approved go ahead" — wiring-sweep proposal P1,
record AGENTS/DAEDALUS/runs/2026-08-28_WIRING_SWEEP/RUN_RECORD.md §9; canon
AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md): any surface a desk's boot protocol tells a session
to READ WHOLE stays under the BYTE BUDGET = 60% of the harness single-read cap. The budget
binds ABOVE any owner-set number. Owners choose HOW (two-state rotation, hot/cold split),
never WHETHER. Per-surface, never a joint cap.

WHY (measured 2026-08-28): 18 of 39 desks' STATUS.md exceeded the cap itself; 5 of 5 audited
boots mandated a read the tool cannot perform; every LINE cap passed clean (a 161-line file at
905 B/line is 146 KB). Past the cap a Read returns a PARTIAL file — the protocol stays written
and execution silently degrades to fragments (PAT-111). The MEMORY.md auto-load cap (25,600 B,
harness_caps.env) is a DIFFERENT constant and does not bind these surfaces.

CONSTANTS — this file is their single owner (AGENTS/DAEDALUS/scripts/read_cap_check.py imports
them; never restate them elsewhere):
  READ_CAP_TOKENS 25,000  OBSERVED from a live truncation message (2026-08-23), confirmed by
                          INDEX_COLD.md truncating silently at 58,825 B (2026-08-23).
  BYTES_PER_TOKEN 2.17    MEASURED on fleet markdown (emoji/unicode/bold-dense). Content-
                          dependent — the weakest leg; a naive 4 B/tok UNDER-counts ~1.8x, the
                          dangerous direction. Re-measure on any new truncation.
  => cap 54,250 B · budget 32,550 B (60%) · rotation trigger 75% of budget · target <70%.

WHAT A PASS PROVES (PAT-074 / PAT-129): rc 0 = every file THIS CHECK FOUND in the desk's boot
protocol is under budget. The perimeter is a HEURISTIC and is printed: a `.md`/`.tsv` token on
a boot-step line containing "read" (any case) inside the charter's SPAWN/BOOT section, plus
STATUS.md always (root Critical Rule: STATUS is canonical truth, every desk reads it). NOT seen:
reads performed inside boot.py, files named only in prose outside the boot section, and
whole-file reads a session decides on its own. R7 stage-2 READS.tsv (~9/14) replaces the
heuristic with a declaration; until then a clean line says "of the files this heuristic found".

Exit contract (CHECK_STANDARD §9): 0 clean · 1 FINDINGS (≥1 mandated read over budget)
                                   · 2 CANNOT-EVALUATE (no charter / unknown desk / unreadable)

Usage (cwd-proof):
    python3 "$(git rev-parse --show-toplevel)/scripts/read_cap_check.py" --agent <NAME>
    python3 "$(git rev-parse --show-toplevel)/scripts/read_cap_check.py" --fleet
    python3 "$(git rev-parse --show-toplevel)/scripts/read_cap_check.py" FILE [FILE ...]
"""
import os
import re
import sys

READ_CAP_TOKENS = 25_000
BYTES_PER_TOKEN = 2.17
TARGET_UTILISATION = 0.60
ROTATE_AT = 0.75          # of BUDGET — start rotating here (DAEDALUS byte-tier convention)
ROTATE_TO = 0.70          # of BUDGET — stop rotating here

CAP_BYTES = int(READ_CAP_TOKENS * BYTES_PER_TOKEN)
BUDGET_BYTES = int(READ_CAP_TOKENS * TARGET_UTILISATION * BYTES_PER_TOKEN)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))

SECTION_RE = re.compile(r"^#{1,4}\s.*\b(SPAWN|BOOT|WHEN SPAWNED|SESSION START|START OF SESSION)\b", re.I)
HEADING_RE = re.compile(r"^#{1,3}\s")
FILE_TOKEN_RE = re.compile(r"`([^`\s]+?\.(?:md|tsv))`")
# "read" as a NOUN is not a verb: "the READ CAP", "a read window", "boot read" — fourth live
# correction, on DAEDALUS's own charter ("Measure against the READ CAP … `FLEET_MAP.tsv` then sat
# at 121%" was parsed as read → object). A heuristic's own author's file is the best test fixture.
READ_VERB_RE = re.compile(r"\bre-?read\b(?!\s*-?\s*(?:cap|window|set|tool|instrument))"
                          r"|\bread\b(?!\s*-?\s*(?:cap|window|set|tool|instrument))"
                          r"|\bscan\b|\bconsume\b")
WRITE_VERB_RE = re.compile(r"\b(append|write|update|log a row|git mv|regenerate|commit)\b")
OBJECT_WINDOW = 160        # chars between the read verb and the file token it governs
QUALIFIER_TAIL = 80        # chars AFTER the token in which 'on demand'/'cold'/'grep' still qualifies it
ON_DEMAND_MARKERS = ("on demand", "on-demand", "grep", "cold", "by id", "per-agent", "do not read",
                     "never read", "not a boot read", "read per-agent")
STEP_RE = re.compile(r"^\s*(?:[-*]|\d+[a-z]?[.)]|[A-Z]\d[a-z]?[.)])\s")


def desk_home(name):
    return os.path.join(ROOT, "PROME") if name == "PROME" else os.path.join(ROOT, "AGENTS", name)


def fleet_desks():
    """Active + tier-2 from the generated FLEET_DIRECTORY.md (same source as corrections_boot_check)."""
    fd = os.path.join(ROOT, "AGENTS", "DAEDALUS", "FLEET_DIRECTORY.md")
    desks, section = [], None
    try:
        for ln in open(fd, encoding="utf-8"):
            if ln.startswith("## "):
                section = ln
            m = re.match(r"^\| ([A-Z]+) \|", ln)
            if m and section and ("ACTIVE" in section or "TIER-2" in section) and m.group(1) != "Agent":
                desks.append(m.group(1))
    except OSError:
        return None
    return desks


def boot_reads(name):
    """(files, perimeter_note) — the boot-mandated whole-read set found in the charter."""
    home = desk_home(name)
    charter = os.path.join(home, "CLAUDE.md")
    if not os.path.isfile(charter):
        return None, f"no charter at {os.path.relpath(charter, ROOT)}"
    lines = open(charter, encoding="utf-8", errors="replace").read().split("\n")
    # locate the boot/spawn section(s): from a matching heading to the next heading of <= its level
    starts = [i for i, l in enumerate(lines) if SECTION_RE.match(l)]
    spans = []
    for s in starts:
        lvl = len(lines[s]) - len(lines[s].lstrip("#"))
        e = next((j for j in range(s + 1, len(lines)) if HEADING_RE.match(lines[j])
                  and (len(lines[j]) - len(lines[j].lstrip("#"))) <= lvl), len(lines))
        spans.append((s, e))
    found = {}
    scanned = 0
    skipped_on_demand = 0
    for s, e in spans:
        for i in range(s, e):
            l = lines[i]
            low = l.lower()
            reads = [m.start() for m in READ_VERB_RE.finditer(low)]
            if not reads:
                continue
            scanned += 1
            for m in FILE_TOKEN_RE.finditer(l):
                tok = m.group(1)
                if tok.startswith(("http", "$")):
                    continue
                # The token must be the OBJECT of a read verb: a `read` within OBJECT_WINDOW chars
                # BEFORE it, with no write verb in between. Second live run: a write-back step
                # ("update STATUS.md; log to PATTERNS.tsv … readable directory") captured five files
                # because "read" was a SUBSTRING of "readable" and the verb-object link was never tested.
                before = low[:m.start()]
                rp = max((r for r in reads if r < m.start()), default=None)
                if rp is None or m.start() - rp > OBJECT_WINDOW:
                    continue
                if WRITE_VERB_RE.search(before[rp:]):
                    continue
                # An ON-DEMAND / grep marker between the read verb and the token means this token is
                # not a whole read ("read FLEET_MAP.tsv per-agent on demand: grep …"). Judged per
                # TOKEN, not per line — a line-level skip (third live run) dropped FLEET_DIRECTORY.md
                # because the SAME line also said "grep" about a different file. The list is a
                # heuristic; it is printed in the perimeter note so a reader can judge it.
                after = low[m.end():m.end() + QUALIFIER_TAIL]
                if any(k in before[rp:] or k in after for k in ON_DEMAND_MARKERS):
                    skipped_on_demand += 1
                    continue
                # resolve: as written relative to home; else basename anywhere shallow in home
                cand = os.path.normpath(os.path.join(home, tok.lstrip("./")))
                if not os.path.isfile(cand):
                    cand = None
                    for dp, dn, fn in os.walk(home):
                        dn[:] = [d for d in dn if d not in ("archive", "_archive", "processed", "inbox", "outbox")]
                        if os.path.basename(tok) in fn:
                            cand = os.path.join(dp, os.path.basename(tok)); break
                if cand and cand != charter:
                    found[cand] = f"boot-step line {i+1}"
    status = os.path.join(home, "STATUS.md")
    if os.path.isfile(status):
        found.setdefault(status, "STATUS.md — universal boot read (root canon)")
    note = (f"perimeter: {len(spans)} boot section(s) in CLAUDE.md, {scanned} 'read' line(s) scanned "
            f"({skipped_on_demand} on-demand/grep token(s) excluded by marker), {len(found)} whole-read file(s) found; "
            f"boot.py-internal reads and prose outside the boot section NOT seen (heuristic — READS.tsv replaces it)")
    if not spans:
        note = "perimeter: NO boot/spawn section heading found in CLAUDE.md — only STATUS.md assumed; " + note
    return found, note


def grade(b):
    util = b / CAP_BYTES
    if b >= CAP_BYTES:
        return "🔴", util, "OVER THE CAP — cannot be read whole"
    if b >= BUDGET_BYTES:
        return "🟠", util, "over budget (readable, no headroom)"
    if b >= BUDGET_BYTES * ROTATE_AT:
        return "🟡", util, "rotate-tier (≥75% of budget)"
    return "✅", util, ""


def check_agent(name, quiet=False):
    files, note = boot_reads(name)
    if files is None:
        if not quiet:
            print(f"READ-CAP 2 CANNOT-EVALUATE [{name}]: {note}")
        return 2, None
    rows = []
    for p in sorted(files, key=lambda x: -os.path.getsize(x)):
        b = os.path.getsize(p)
        mark, util, why = grade(b)
        rows.append((mark, os.path.relpath(p, desk_home(name)), b, util, why, files[p]))
    n_over_cap = sum(1 for r in rows if r[0] == "🔴")
    n_over_budget = sum(1 for r in rows if r[0] in ("🔴", "🟠"))
    rc = 1 if n_over_budget else 0
    if not quiet:
        print(f"READ-CAP [{name}] — cap {CAP_BYTES:,} B · budget {BUDGET_BYTES:,} B (60%) · {note}")
        for mark, rel, b, util, why, src in rows:
            print(f"  {mark} {rel:<34}{b:>9,} B  {util:>5.0%} of cap  {why}  ({src})")
        if rc:
            print(f"⚠️  READ-CAP 1 [{name}]: {n_over_budget} boot-mandated read(s) over budget, "
                  f"{n_over_cap} over the CAP itself. Remedy = two-state rotation (verbatim, crc-stamped, "
                  f"to archive/) or hot/cold split — per surface, owner's choice of HOW. "
                  f"⛔ Never raise the budget: the read cap is not ours to move.")
        else:
            print(f"✅ READ-CAP 0 [{name}]: every boot-mandated read this check found is under budget "
                  f"({len(rows)} file(s)).")
    return rc, (name, len(rows), n_over_budget, n_over_cap, rows)


def main(argv):
    args = argv[1:]
    if "--agent" in args:
        name = args[args.index("--agent") + 1]
        rc, _ = check_agent(name)
        return rc
    if "--fleet" in args:
        desks = fleet_desks()
        if not desks:
            print("READ-CAP 2 CANNOT-EVALUATE: FLEET_DIRECTORY.md unreadable — regenerate it")
            return 2
        print(f"READ-CAP FLEET — cap {CAP_BYTES:,} B · budget {BUDGET_BYTES:,} B · {len(desks)} active+tier-2 desks · "
              f"perimeter per desk = heuristic boot-read set (see --agent for each)")
        print(f"  {'desk':10}{'reads':>6}{'>budget':>9}{'>cap':>6}  worst file")
        tot_b = tot_c = 0; bad = []; cant = []
        for d in desks:
            rc, res = check_agent(d, quiet=True)
            if res is None:
                cant.append(d); continue
            name, n, nb, nc, rows = res
            tot_b += (nb > 0); tot_c += (nc > 0)
            worst = rows[0] if rows else None
            w = f"{worst[1]} {worst[3]:.0%}" if worst else "—"
            mark = "🔴" if nc else ("🟠" if nb else "✅")
            print(f"  {mark} {name:8}{n:>6}{nb:>9}{nc:>6}  {w}")
            if nb: bad.append(name)
        print(f"\n  desks with ≥1 boot read over BUDGET: {tot_b}/{len(desks)} · over the CAP: {tot_c}/{len(desks)}"
              + (f" · CANNOT-EVALUATE: {', '.join(cant)}" if cant else ""))
        if cant:
            return 2
        return 1 if bad else 0
    # explicit files (legacy form)
    paths = args
    if not paths:
        print(__doc__); return 2
    rc = 0
    for p in paths:
        try:
            b = os.path.getsize(p)
        except OSError as e:
            print(f"READ-CAP 2 CANNOT-EVALUATE: {p} ({e.__class__.__name__})"); return 2
        mark, util, why = grade(b)
        print(f"  {mark} {os.path.relpath(p, ROOT):<50}{b:>9,} B  {util:>5.0%} of cap  {why}")
        rc = max(rc, 1 if mark in ("🔴", "🟠") else 0)
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))
