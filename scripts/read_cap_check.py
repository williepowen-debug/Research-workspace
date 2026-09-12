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

PRODUCTION ACCEPTANCE SET (CHECK_STANDARD §3(e), added 2026-09-07 — re-run at every edit of a regex
in this file): DEFECTIVE input = AGENTS/BRENT/CLAUDE.md:26 ("Read `STATUS.md`" → STATUS.md 74,061 B,
must print 🔴 OVER THE CAP); CLEAN input = AGENTS/BRENT/CLAUDE.md:52 ("log every consumed item to
`board_log.tsv`" → a write target, must NOT appear in the table). Both live paths, both watched
2026-09-07 21:2x on the real files.

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
# "log <items> to FILE" is a WRITE whose target sits inside the read-verb window of the same
# sentence ("… decide *consume now* … log every consumed item to `board_log.tsv`") — sixth live
# correction (BRENT 2026-09-07): board_log.tsv (308 KB) was scored a whole read on BRENT's
# CLAUDE.md:52 and shipped in two packets. Bare `log` is NOT a write verb (a noun in "read the
# log"); the lookahead requires a "to" within 40 chars, which is the write form.
WRITE_VERB_RE = re.compile(r"\b(append|write|update|log a row|git mv|regenerate|commit"
                           r"|log\b(?=[^`]{0,40}\bto\b))\b")
OBJECT_WINDOW = 160        # chars between the read verb and the file token it governs
QUALIFIER_TAIL = 80        # chars AFTER the token in which 'on demand'/'cold'/'grep' still qualifies it
# SCOPED READS ARE NOT WHOLE READS (fifth correction, WAL 2026-08-28, one-directional bias): "the
# top `CHANGELOG.md` entry", "`THESIS.md` header + calibration tables", "cross-reference KB.tsv" were
# scored as whole reads — a scoped read can only OVER-count, never under, so the fleet figure was
# inflated and rankings shifted. A scope token in the verb→token window or the qualifier tail
# means a PART is read; the file drops out. READS.tsv will declare scope explicitly.
SCOPE_MARKERS = ("header", "the top", "top entry", "top of", "top block", "head of",
                 "tail of", "section", "block", "table", "tables", "cross-reference", "skim", "spot-check",
                 "consult", "lines ", "rows ", "preamble", "summary", "bottom line", "only the", "just the")
# 'first '/'last ' were BARE tokens until 2026-09-04 and matched "from last session" in VIOLET's
# boot step 2 ("Read `SCRATCH.md` — ephemeral handoff from last session"), scoring an 18 KB WHOLE
# read as SCOPED and dropping it from the perimeter — a false NEGATIVE, the direction this tool
# must not fail in. A scoping qualifier is "first/last N" or "first/last <unit>"; "last session",
# "last week", "first boot" are not. Found on the VIOLET profile refresh (DAEDALUS).
SCOPE_ORDINAL_RE = re.compile(r"\b(?:first|last)\s+(?:\d+|n\b|few\b|entry|entries|row|rows|line|lines|block|blocks|section|sections|item|items|paragraph|paragraphs|page|pages)")
# Sub-headings nested under a boot heading that are protocols, not boot steps (WAL: a KB.tsv
# mention inside "Inbox Processing Protocol" under the boot section was scored as a boot read).
NON_BOOT_SUBHEAD_RE = re.compile(r"\b(inbox|protocol|closeout|mail|output|writing|delivery|escalation)\b", re.I)
ON_DEMAND_MARKERS = ("on demand", "on-demand", "grep", "cold", "by id", "per-agent", "do not read",
                     "never read", "not a boot read", "read per-agent")
STEP_RE = re.compile(r"^\s*(?:[-*]|\d+[a-z]?[.)]|[A-Z]\d[a-z]?[.)])\s")


def desk_home(name):
    """Resolve a desk to its home. SECOND LOCATION added 2026-09-12 (DAEDALUS) on PHAN's report:
    sub-agents live at `AGENTS/<PARENT>/sub_agents/<NAME>/`, so the one-template resolver returned
    CANNOT-EVALUATE for every one of them and the layer read as covered because the fleet sweep is
    clean on the names it CAN resolve — `finding_scan_keyed_on_naming_reads_local_form_as_absence`.
    It cost something real: PHAN's DOSSIER.md (a boot whole-read) hit 41,078 B = 126% of budget and
    no fleet instrument could flag it. PHAN enumerated SEVEN, all under CARL; the sweep for the
    PATTERN finds EIGHT — `AGENTS/MARCO/sub_agents/TOURISM/CLAUDE.md` is the eighth (PAT-136: an
    enumeration is exhaustive only of its author's search). `--fleet` is unchanged and still walks
    ROSTER/FLEET_DIRECTORY only: sub-agents are not fleet desks and must not be graded as such."""
    if name == "PROME":
        return os.path.join(ROOT, "PROME")
    direct = os.path.join(ROOT, "AGENTS", name)
    if os.path.isfile(os.path.join(direct, "CLAUDE.md")) or not os.path.isdir(os.path.join(ROOT, "AGENTS")):
        return direct
    subs = sorted(p for p in
                  (os.path.join(ROOT, "AGENTS", parent, "sub_agents", name)
                   for parent in sorted(os.listdir(os.path.join(ROOT, "AGENTS"))))
                  if os.path.isfile(os.path.join(p, "CLAUDE.md")))
    if len(subs) == 1:
        return subs[0]
    if len(subs) > 1:
        # Ambiguity is a finding, never a silent pick of the first parent.
        desk_home.ambiguous = subs
    return direct


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


def _resolve(home, tok, charter):
    """Resolve a file token: as written relative to home, else by basename anywhere shallow in home."""
    cand = os.path.normpath(os.path.join(home, tok.lstrip("./")))
    if not os.path.isfile(cand):
        cand = None
        for dp, dn, fn in os.walk(home):
            dn[:] = [d for d in dn if d not in ("archive", "_archive", "processed", "inbox", "outbox")]
            if os.path.basename(tok) in fn:
                cand = os.path.join(dp, os.path.basename(tok)); break
    return cand if cand and cand != charter else None


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
    scoped_overcap = {}
    scanned = 0
    skipped_on_demand = 0
    skipped_scoped = 0
    for s, e in spans:
        boot_lvl = len(lines[s]) - len(lines[s].lstrip("#"))
        in_nonboot_sub = False
        for i in range(s, e):
            l = lines[i]
            if HEADING_RE.match(l) or l.startswith("####"):
                lvl = len(l) - len(l.lstrip("#"))
                in_nonboot_sub = lvl > boot_lvl and bool(NON_BOOT_SUBHEAD_RE.search(l))
            if in_nonboot_sub:
                continue
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
                if (any(k in before[rp:] or k in after for k in SCOPE_MARKERS)
                        or SCOPE_ORDINAL_RE.search(before[rp:]) or SCOPE_ORDINAL_RE.search(after)):
                    skipped_scoped += 1
                    # READ_CAP rule 8 (WALTER): a scoped read of an over-cap file is a PARTIAL fix —
                    # the read is honest, the file is not lean. Keep it visible, never counted.
                    sc = _resolve(home, tok, charter)
                    if sc and os.path.getsize(sc) >= CAP_BYTES:
                        scoped_overcap[sc] = f"boot-step line {i+1}"
                    continue
                cand = _resolve(home, tok, charter)
                if cand:
                    found[cand] = f"boot-step line {i+1}"
    status = os.path.join(home, "STATUS.md")
    if os.path.isfile(status):
        found.setdefault(status, "STATUS.md — universal boot read (root canon)")
    note = (f"perimeter: {len(spans)} boot section(s) in CLAUDE.md, {scanned} 'read' line(s) scanned "
            f"({skipped_on_demand} on-demand/grep + {skipped_scoped} SCOPED-read token(s) excluded by marker), {len(found)} whole-read file(s) found; "
            f"boot.py-internal reads and prose outside the boot section NOT seen (heuristic — READS.tsv replaces it)")
    if not spans:
        note = "perimeter: NO boot/spawn section heading found in CLAUDE.md — only STATUS.md assumed; " + note
    boot_reads.scoped_overcap = {k: v for k, v in scoped_overcap.items() if k not in found}
    return found, note


# ── R7-stage-2: the CONSUMER half of the DECLARATION (DOCKET L209, DAEDALUS 2026-09-12) ──────
# `PROME/registry/READS.tsv` is the desk-authored boot-read manifest (born 2026-08-31, PROME).
# Where a desk has ATTESTED its manifest, that declaration REPLACES the charter heuristic above.
# WHY (measured 2026-09-12, not inferred from one desk): the heuristic scans `CLAUDE.md` boot
# sections, and 29 of 37 active+tier-2 desks delegate their boot protocol to a file it never opens
# (`BOOT.md`, `scripts/boot.py`, `MAINTENANCE.md`, `design/BOOT_PROTOCOL.md`). PROME's own verdict
# read "✅ 1 boot-mandated read" against a 29-row declared perimeter — a clean scan against the
# wrong reference (`finding_instrument_reports_clean_against_the_wrong_reference`).
# ⛔ THE MANIFEST'S OWN RULES, ENFORCED HERE — its header owns the text, this file never restates it:
#   · `whole`/`programmatic` are CAP-BEARING. `scoped`/`grep`/`summary` are declared-and-VISIBLE but
#     NEVER counted. Collapsing the two axes re-creates the false breach `mode` exists to prevent.
#   · An ATTESTATION row is valid ONLY where declared_by == reader. PROME cannot attest for a desk.
#   · An UNATTESTED desk is UNKNOWN, never clean.
READS_TSV = os.path.join(ROOT, "PROME", "registry", "READS.tsv")
CAP_BEARING_MODES = ("whole", "programmatic")
VISIBLE_MODES = ("scoped", "grep", "summary")


def load_reads(path=None):
    """(rows, error). Parse failure => an error string, NEVER an empty row list: READS.tsv lives in
    PROME/ and PROME edits it, so a half-written file must surface as rc 2, not as 'no rows'."""
    p = path or READS_TSV
    rel = os.path.relpath(p, ROOT)
    if not os.path.isfile(p):
        return None, f"no manifest at {rel}"
    try:
        lines = [l.rstrip("\n") for l in open(p, encoding="utf-8")
                 if not l.startswith("#") and l.strip()]
    except OSError as e:
        return None, f"{rel} unreadable ({e.__class__.__name__})"
    if not lines:
        return None, f"{rel} has no rows"
    hdr = lines[0].split("\t")
    missing = [c for c in ("row_kind", "reader", "path", "mode", "declared_by") if c not in hdr]
    if missing:
        return None, f"{rel} header missing column(s): {', '.join(missing)}"
    rows = []
    for n, ln in enumerate(lines[1:], 2):
        cells = ln.split("\t")
        if len(cells) < 5:
            return None, (f"{rel} row {n}: {len(cells)} cell(s), header has {len(hdr)} — refusing to "
                          f"grade a partially-written manifest")
        rows.append(dict(zip(hdr, cells)))
    return rows, None


def declared_reads(name, path=None, root=None):
    """(cap_bearing, visible, problems, attested, note) from the manifest.
    cap_bearing is None when the manifest cannot be used for this desk; `note` says why.
    `path`/`root` exist so --selftest can drive FROZEN tempdir fixtures rather than live surfaces
    (a regression test pinned to a live doc certifies nothing past the next edit — PROME 2026-09-09)."""
    rows, err = load_reads(path)
    base_root = root or ROOT
    if rows is None:
        return None, None, None, None, err
    mine = [r for r in rows if r.get("reader") == name]
    if not mine:
        return None, None, None, None, f"desk {name} has NO rows in the manifest"
    attested = any(r.get("row_kind") == "ATTESTATION" and r.get("declared_by") == name for r in mine)
    cap_bearing, visible, problems = {}, [], []
    for r in mine:
        if r.get("row_kind") == "ATTESTATION" and r.get("declared_by") != name:
            problems.append(f"ATTESTATION signed by `{r.get('declared_by') or '(blank)'}`, not by "
                            f"{name} — INVALID (manifest ⛔ who-may-attest: reading someone else's "
                            f"charter is INFERENCE, not attestation)")
    for r in mine:
        if r.get("row_kind") != "READ":
            continue                                    # ATTESTATION / BASIS rows are not reads
        mode = (r.get("mode") or "").strip()
        pth = (r.get("path") or "").strip()
        src = (r.get("source_boot_step") or "READS.tsv").strip()
        if not pth or mode.startswith("RETIRED"):
            continue
        if "*" in pth or "?" in pth:                    # a CLASS row is declared, never one file
            visible.append((pth, mode + " · CLASS row, not a single file", src))
            continue
        full = os.path.join(base_root, pth)
        if mode not in CAP_BEARING_MODES and mode not in VISIBLE_MODES:
            problems.append(f"`{pth}` ({src}) carries mode `{mode}` — not in the manifest's own "
                            f"mode vocabulary")
            continue
        if not os.path.exists(full):
            # The condition the heuristic STRUCTURALLY cannot produce: a scan finds only what
            # exists, so a manifest pointing at a deleted file reads as silence.
            problems.append(f"declared {mode} read `{pth}` ({src}) DOES NOT EXIST on disk")
            continue
        if mode in CAP_BEARING_MODES and os.path.isfile(full):
            cap_bearing[full] = (mode, src)
        else:
            visible.append((pth, mode + (" · directory" if os.path.isdir(full) else ""), src))
    note = (f"perimeter: DECLARED in {os.path.relpath(READS_TSV, ROOT)} — {len(cap_bearing)} "
            f"cap-bearing (whole/programmatic) measured, {len(visible)} declared-not-counted "
            f"(scoped/grep/summary), {len(mine)} manifest row(s) for this desk; "
            + ("ATTESTED by the desk itself" if attested else
               "⛔ NOT ATTESTED by this desk — the perimeter is PARTIAL"))
    return cap_bearing, visible, problems, attested, note


def grade(b):
    """(mark, utilisation-of-BUDGET, why).

    ⚠️ THE PERCENTAGE IS DENOMINATED IN THE BUDGET, NOT THE CAP — changed 2026-09-12 (DAEDALUS)
    on a MEASURED second instance, not an inference. Until today this returned `b / CAP_BYTES`
    while every verdict above is keyed to BUDGET_BYTES, so one row carried two numbers that read
    OPPOSITELY under one word ("cap"):
        BROCK/STATUS.md   41,162 B   displayed " 76% of cap"   =  126.5% of budget   verdict 🟠
        BROCK/LESSONS.md  35,545 B   displayed " 66% of cap"   =  109.2% of budget   verdict 🟠
    BROCK's 2026-09-12 completion note quoted the NUMBER and not the VERDICT — "STATUS.md still
    75% of read-cap … still over budget; hot/cold split deliberately not started" — and deferred
    the split partly on that reading, while the file sat 8,612 B OVER the budget it is graded on.
    A reader taking the percentage understated severity by ~40 points; only the adjacent verdict
    saved them, and only if they read it.
    SAME FAMILY AS THE L258 OPERATOR MISMATCH: the letter names one denominator and the
    instrument carries another. `finding_distance_to_a_threshold_is_a_claim_about_its_basis`.
    ACCEPTANCE CONDITION (PROME's, in the defect's own terms rather than the symptom's):
    a reader who quotes ONLY the percentage reaches the SAME severity conclusion as a reader who
    quotes only the verdict. So: ≥100% now means "over the thing the verdict grades", always.
    The CAP is still reported — but only where it binds, in the 🔴 text, which is the one place
    the cap is the operative limit."""
    util = b / BUDGET_BYTES
    if b >= CAP_BYTES:
        return "🔴", util, f"OVER THE CAP ({b / CAP_BYTES:.0%} of the {CAP_BYTES:,} B cap) — cannot be read whole"
    if b >= BUDGET_BYTES:
        return "🟠", util, "over budget (readable, no headroom)"
    if b >= BUDGET_BYTES * ROTATE_AT:
        return "🟡", util, "rotate-tier (≥75% of budget)"
    return "✅", util, ""


def check_agent(name, quiet=False, require_manifest=False):
    # R7-stage-2 precedence: a desk's own ATTESTED declaration beats a scan of its charter.
    cap_bearing, visible, problems, attested, dnote = declared_reads(name)
    declared = cap_bearing is not None
    if declared and not attested:
        # The manifest's own ⛔: rows without an attestation are a PARTIAL perimeter, and a check
        # over a partial perimeter must report UNKNOWN. Reporting clean here is the exact defect
        # this file exists to retire. Fail CLOSED, never to the heuristic (which would read clean).
        if not quiet:
            print(f"READ-CAP 2 CANNOT-EVALUATE [{name}]: {dnote}. An unattested desk is UNKNOWN, "
                  f"never clean — the desk itself must attest (packet to PROME/inbox/; no desk may "
                  f"commit inside PROME/, and PROME may not attest on a desk's behalf).")
            for pr in problems or []:
                print(f"  ⛔ {pr}")
        return 2, None
    if declared:
        files = {p: f"{mode} · {src}" for p, (mode, src) in cap_bearing.items()}
        note = dnote
        boot_reads.scoped_overcap = {}          # not the heuristic's run; don't carry its state
    else:
        if require_manifest:
            if not quiet:
                print(f"READ-CAP 2 CANNOT-EVALUATE [{name}]: {dnote} (--require-manifest). The "
                      f"charter heuristic is available without this flag, and says so in its verdict.")
            return 2, None
        files, note = boot_reads(name)
        problems, visible = [], []
    if files is None:
        if not quiet:
            print(f"READ-CAP 2 CANNOT-EVALUATE [{name}]: {note}")
        return 2, None
    rows = []
    base = ROOT if declared else desk_home(name)      # declared rows are repo-relative + cross-agent
    for p in sorted(files, key=lambda x: -os.path.getsize(x)):
        b = os.path.getsize(p)
        mark, util, why = grade(b)
        rows.append((mark, os.path.relpath(p, base), b, util, why, files[p]))
    n_over_cap = sum(1 for r in rows if r[0] == "🔴")
    n_over_budget = sum(1 for r in rows if r[0] in ("🔴", "🟠"))
    rc = 1 if (n_over_budget or problems) else 0
    if not quiet:
        print(f"READ-CAP [{name}] — cap {CAP_BYTES:,} B · budget {BUDGET_BYTES:,} B (60%) · ALL % BELOW ARE OF BUDGET (the number every verdict grades; ≥100% = over) · {note}")
        for mark, rel, b, util, why, src in rows:
            print(f"  {mark} {rel:<34}{b:>9,} B  {util:>5.0%} of budget  {why}  ({src})")
        for sp, src in sorted(getattr(boot_reads, "scoped_overcap", {}).items(), key=lambda kv: -os.path.getsize(kv[0])):
            b = os.path.getsize(sp)
            print(f"  ℹ️ {os.path.relpath(sp, desk_home(name)):<34}{b:>9,} B  {b / BUDGET_BYTES:>5.0%} of budget  "
                  f"scoped read on an OVER-CAP file — honest read, not lean (READ_CAP rule 8: partial fix; not counted)  ({src})")
        for pth, mode, src in visible or []:
            # Declared and VISIBLE, never counted: the mode says the rows do not enter context.
            # Printed so nobody later "discovers" one as a breach (manifest header, NOT CAP-BEARING).
            sz = os.path.join(ROOT, pth)
            bs = f"{os.path.getsize(sz):,} B" if os.path.isfile(sz) else "—"
            print(f"  ◦ {pth:<34}{bs:>9}  declared `{mode}` — not cap-bearing, not counted  ({src})")
        for pr in problems or []:
            print(f"  ⛔ {pr}")
        if rc:
            if n_over_budget:
                print(f"⚠️  READ-CAP 1 [{name}]: {n_over_budget} boot-mandated read(s) over budget, "
                      f"{n_over_cap} over the CAP itself. Remedy = two-state rotation (verbatim, crc-stamped, "
                      f"to archive/) or hot/cold split — per surface, owner's choice of HOW. "
                      f"⛔ Never raise the budget: the read cap is not ours to move.\n"
                      # BROCK 2026-09-12, measured from inside its own repair and asked for here by name:
                      # the first instinct is to tighten the prose, and tightening is an EDIT — it notices
                      # what is unclear and adds the missing qualifier. BROCK's two rewrite passes came out
                      # +242 B and +451 B; collapsing verbose pointers into one terse index is what worked.
                      # DAEDALUS reproduced it the same day on its own STATUS. PAT-161.
                      f"   ⛔ AND DO NOT TRY TO REWRITE YOUR WAY UNDER: a careful tightening pass RELIABLY "
                      f"ADDS bytes (measured +242 B and +451 B on two real attempts). Only MOVING text out "
                      f"removes them — rotate, or collapse several verbose pointers into ONE terse index. "
                      f"Both are mechanical; a rewrite is not.")
            if problems:
                print(f"⚠️  READ-CAP 1 [{name}]: {len(problems)} manifest defect(s) above. A declared "
                      f"read that does not resolve is a defect of the DECLARATION, not of the cap — "
                      f"the owner fixes the row (or the file), never this check.")
        elif declared:
            print(f"✅ READ-CAP 0 [{name}]: every CAP-BEARING read in this desk's ATTESTED manifest is "
                  f"under budget ({len(rows)} measured, {len(visible)} declared-not-counted). "
                  f"Perimeter = the desk's own declaration, not a scan.")
        else:
            print(f"✅ READ-CAP 0 [{name}]: every boot-mandated read this check found is under budget "
                  f"({len(rows)} file(s)). ⚠️ PERIMETER IS THE CHARTER HEURISTIC — this desk has no "
                  f"declaration in {os.path.relpath(READS_TSV, ROOT)}, so this is 'clean within what the "
                  f"scan found', NOT a clean bill. 29 of 37 desks delegate boot to a file it cannot see.")
    return rc, (name, len(rows), n_over_budget, n_over_cap, rows)


HDR = "row_kind\treader\tpath\tmode\tsource_boot_step\tdeclared_by\tdeclared_on\tnotes"


def _fixture(tmp, rows, sizes=None):
    """Write a FROZEN manifest + sized files under tmp. Fixtures are frozen here, never pinned to a
    live surface: a regression test asserting a live doc's current strings certifies nothing past the
    next edit (PROME 2026-09-09, applied to validate_all the same day)."""
    for rel, n in (sizes or {}).items():
        f = os.path.join(tmp, rel)
        os.makedirs(os.path.dirname(f), exist_ok=True)
        open(f, "w").write("x" * n)
    man = os.path.join(tmp, "READS.tsv")
    open(man, "w", encoding="utf-8").write("# frozen fixture\n" + HDR + "\n" + "\n".join(rows) + "\n")
    return man


def selftest():
    """CHECK_STANDARD §3: every leg watched on a CAPABLE case (the alert fires) AND a CLEAN case
    (the clean line prints). rc 0 = all legs pass. Closes this file's own gap-register row — leg A9
    of scripts/validate_all.py was NOT REGISTERED because this check had no --selftest."""
    import tempfile
    global READS_TSV, ROOT
    ok, fail = 0, []

    def chk(leg, got, want):
        nonlocal ok
        if got == want:
            ok += 1
        else:
            fail.append(f"{leg}: expected {want!r}, got {got!r}")

    A = "ATTESTATION\tD\t.\tmanifest-complete\ts\tD\t2026-09-12\tattested by the desk"
    with tempfile.TemporaryDirectory() as t:
        # C1/C2 — CLEAN: a whole read under budget passes; an over-cap `summary` row is NOT counted.
        m = _fixture(t, [A,
                         "READ\tD\tsmall.md\twhole\ts1\tD\t2026-09-12\t-",
                         "READ\tD\thuge.tsv\tsummary\ts2\tD\t2026-09-12\tbounded verdict only"],
                     {"small.md": 100, "huge.tsv": CAP_BYTES + 5000})
        cb, vis, pr, att, _ = declared_reads("D", m, t)
        chk("C1 declared perimeter used", len(cb), 1)
        chk("C2 summary not cap-bearing", len(vis), 1)
        chk("C1 attested", att, True)
        chk("C2/C5 no problems on a clean manifest", pr, [])
        # C2 — CAPABLE: the SAME file declared `whole` must now be measured (and is over the cap).
        m = _fixture(t, [A, "READ\tD\thuge.tsv\twhole\ts2\tD\t2026-09-12\t-"],
                     {"huge.tsv": CAP_BYTES + 5000})
        cb, vis, pr, att, _ = declared_reads("D", m, t)
        chk("C2 whole IS cap-bearing", len(cb), 1)
        chk("C2 grade fires over cap", grade(os.path.getsize(list(cb)[0]))[0], "🔴")
        # C3 — CAPABLE: rows but no attestation => UNKNOWN, never clean.
        m = _fixture(t, ["READ\tD\tsmall.md\twhole\ts1\tD\t2026-09-12\t-"], {"small.md": 100})
        chk("C3 unattested", declared_reads("D", m, t)[3], False)
        # C5 — CAPABLE: an attestation signed by someone else is INVALID and does not clear the desk.
        m = _fixture(t, ["ATTESTATION\tD\t.\tmanifest-complete\ts\tPROME(from-charter)\t2026-09-12\tx",
                         "READ\tD\tsmall.md\twhole\ts1\tD\t2026-09-12\t-"], {"small.md": 100})
        cb, vis, pr, att, _ = declared_reads("D", m, t)
        chk("C5 foreign attestation rejected", att, False)
        chk("C5 foreign attestation reported", any("INVALID" in p for p in pr), True)
        # C6 — CAPABLE: a declared read that does not exist on disk. The heuristic CANNOT produce this.
        m = _fixture(t, [A, "READ\tD\tgone.md\twhole\ts1\tD\t2026-09-12\t-"], {})
        cb, vis, pr, att, _ = declared_reads("D", m, t)
        chk("C6 absent declared path reported", any("DOES NOT EXIST" in p for p in pr), True)
        chk("C6 absent path not silently measured", len(cb), 0)
        # C7 — a RETIRED row is skipped, not measured and not a problem.
        m = _fixture(t, [A, "READ\tD\tgone.md\tRETIRED-2026-09-01\ts1\tD\t2026-09-12\tretired"], {})
        cb, vis, pr, att, _ = declared_reads("D", m, t)
        chk("C7 retired skipped", (len(cb), len(vis), pr), (0, 0, []))
        # C9 — a CLASS row is neither dropped nor counted as one file.
        m = _fixture(t, [A, "READ\tD\tAGENTS/*/STATUS.md\tsummary\ts1\tD\t2026-09-12\tclass"], {})
        cb, vis, pr, att, _ = declared_reads("D", m, t)
        chk("C9 class row visible not measured", (len(cb), len(vis), pr), (0, 1, []))
        # C10 — CAPABLE: a half-written manifest is an ERROR, never an empty (clean) row set.
        bad = os.path.join(t, "bad.tsv")
        open(bad, "w").write(HDR + "\nREAD\tD\n")
        chk("C10 short row => error", declared_reads("D", bad, t)[0] is None, True)
        open(bad, "w").write("reader\tpath\n")
        chk("C10 bad header => error", declared_reads("D", bad, t)[0] is None, True)
        chk("C10 missing file => error", declared_reads("D", os.path.join(t, "nope.tsv"), t)[0] is None, True)
        # C11/C4 — a desk with NO rows falls through to the heuristic (cap_bearing is None).
        m = _fixture(t, [A], {})
        chk("C4 undeclared desk => heuristic", declared_reads("ZZZ", m, t)[0] is None, True)
        # unknown mode is a manifest defect, not a silent skip
        m = _fixture(t, [A, "READ\tD\tsmall.md\tskim\ts1\tD\t2026-09-12\t-"], {"small.md": 100})
        chk("unknown mode reported", any("mode vocabulary" in p for p in declared_reads("D", m, t)[2]), True)
        # BASIS rows are not reads
        m = _fixture(t, [A, "BASIS\tD\tsmall.md\tboot-defining\ts1\tD\t2026-09-12\t-"], {"small.md": 100})
        chk("BASIS row is not a read", declared_reads("D", m, t)[:2], ({}, []))

        # ── DISPLAY DENOMINATOR (PROME 2026-09-12, measured second instance at BROCK) ──────────
        # ACCEPTANCE CONDITION: a reader who quotes ONLY the percentage reaches the SAME severity
        # conclusion as a reader who quotes only the verdict. Tested at the BOUNDARY in both
        # directions, because the old defect lived entirely in the gap between budget and cap.
        over_budget_under_cap = (BUDGET_BYTES + CAP_BYTES) // 2      # BROCK's actual region
        mark, util, why = grade(over_budget_under_cap)
        chk("display: over-budget row is flagged", mark, "🟠")
        chk("display: over-budget row READS as over (>=100%)", util >= 1.0, True)
        mark, util, why = grade(BUDGET_BYTES)                        # exactly on the line
        chk("display: exactly at budget is flagged", mark, "🟠")
        chk("display: exactly at budget reads 100%", f"{util:.0%}", "100%")
        mark, util, why = grade(BUDGET_BYTES - 1)                    # one byte under
        chk("display: one byte under budget is NOT flagged", mark in ("✅", "🟡"), True)
        chk("display: one byte under budget reads <100%", util < 1.0, True)
        mark, util, why = grade(CAP_BYTES + 1)                       # over the cap too
        chk("display: over-cap row still 🔴", mark, "🔴")
        chk("display: over-cap 'why' names the CAP explicitly", "of the" in why and "cap" in why, True)
        chk("display: over-cap util is still budget-denominated", util > 1.6, True)

        # END-TO-END rc contract, both directions (the verdict, not just the parser).
        sav_r, sav_root = READS_TSV, ROOT
        try:
            ROOT = t
            READS_TSV = _fixture(t, [A, "READ\tD\tsmall.md\twhole\ts1\tD\t2026-09-12\t-"],
                                 {"small.md": 100})
            chk("E2E clean => rc 0", check_agent("D", quiet=True)[0], 0)
            READS_TSV = _fixture(t, [A, "READ\tD\thuge.tsv\twhole\ts1\tD\t2026-09-12\t-"],
                                 {"huge.tsv": CAP_BYTES + 5000})
            chk("E2E over cap => rc 1", check_agent("D", quiet=True)[0], 1)
            READS_TSV = _fixture(t, [A, "READ\tD\tgone.md\twhole\ts1\tD\t2026-09-12\t-"], {})
            chk("E2E manifest defect => rc 1", check_agent("D", quiet=True)[0], 1)
            READS_TSV = _fixture(t, ["READ\tD\tsmall.md\twhole\ts1\tD\t2026-09-12\t-"],
                                 {"small.md": 100})
            chk("E2E unattested => rc 2 (UNKNOWN, never clean)", check_agent("D", quiet=True)[0], 2)
            READS_TSV = _fixture(t, [A], {})
            chk("E2E --require-manifest on an undeclared desk => rc 2",
                check_agent("ZZZ", quiet=True, require_manifest=True)[0], 2)
        finally:
            READS_TSV, ROOT = sav_r, sav_root

    total = ok + len(fail)
    for f in fail:
        print(f"  ❌ {f}")
    print(f"{'✅' if not fail else '❌'} READ-CAP SELFTEST {ok}/{total} leg(s) pass "
          f"(R7-stage-2 manifest consumer: C1–C11 + rc contract, frozen tempdir fixtures)")
    return 0 if not fail else 1


def main(argv):
    args = argv[1:]
    if "--selftest" in args:
        return selftest()
    require_manifest = "--require-manifest" in args
    if require_manifest:
        args = [a for a in args if a != "--require-manifest"]
    if "--agent" in args:
        name = args[args.index("--agent") + 1]
        rc, _ = check_agent(name, require_manifest=require_manifest)
        return rc
    if "--fleet" in args:
        desks = fleet_desks()
        if not desks:
            print("READ-CAP 2 CANNOT-EVALUATE: FLEET_DIRECTORY.md unreadable — regenerate it")
            return 2
        print(f"READ-CAP FLEET — cap {CAP_BYTES:,} B · budget {BUDGET_BYTES:,} B · {len(desks)} active+tier-2 desks · "
              f"perimeter per desk = heuristic boot-read set (see --agent for each)")
        print(f"  {'desk':10}{'reads':>6}{'>budget':>9}{'>cap':>6}  worst file (% is of BUDGET — the number the verdict grades)")
        tot_b = tot_c = 0; bad = []; cant = []
        for d in desks:
            rc, res = check_agent(d, quiet=True)
            if res is None:
                cant.append(d); continue
            name, n, nb, nc, rows = res
            tot_b += (nb > 0); tot_c += (nc > 0)
            worst = rows[0] if rows else None
            w = f"{worst[1]} {worst[3]:.0%} of budget" if worst else "—"
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
    # UNKNOWN FLAG GUARD (2026-09-03, Codex/PROME: `--all` fell through to this legacy path, was read
    # as a FILENAME, and died "CANNOT-EVALUATE (FileNotFoundError)" — a usage error dressed as an
    # instrument failure, which then became "UNKNOWN until this runs" in a fleet audit). Any `--flag`
    # that is not a mode is a usage error, named, rc 2. Modes: --agent NAME · --fleet · [FILE ...].
    unknown = [a for a in paths if a.startswith("--")]
    if unknown:
        print(f"READ-CAP 2 USAGE: unknown flag(s) {', '.join(unknown)} — modes are `--agent <NAME>` "
              f"[--require-manifest], `--fleet`, `--selftest`, or explicit file paths; there is no "
              f"`--all` (fleet mode is `--fleet`)")
        return 2
    if not paths:
        print(__doc__); return 2
    rc = 0
    for p in paths:
        try:
            b = os.path.getsize(p)
        except OSError as e:
            print(f"READ-CAP 2 CANNOT-EVALUATE: {p} ({e.__class__.__name__})"); return 2
        mark, util, why = grade(b)
        print(f"  {mark} {os.path.relpath(p, ROOT):<50}{b:>9,} B  {util:>5.0%} of budget  {why}")
        rc = max(rc, 1 if mark in ("🔴", "🟠") else 0)
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))
