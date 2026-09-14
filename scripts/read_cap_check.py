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

Exit contract (CHECK_STANDARD §9): 0 clean · 1 FINDINGS (≥1 mandated read over budget, OR ≥1
                                     MANIFEST DEFECT) · 2 CANNOT-EVALUATE (no charter / unknown
                                     desk / unreadable)

⛔ rc IS THREE-STATE AND CARRIES A ONE-BIT REASON. Do not infer WHY from rc, and never from the
totals sentence: with an identical "0/37 over BUDGET" summary, rc 0, 1 and 2 are three different
worlds. READ THE LAST LINE instead — `READ-CAP-RESULT v1 …`, stable key=value pairs, the reason
channel this tool emits for its callers (added 2026-09-14, DOCKET L355). `assessed=0` on that line
means NO COUNT ON IT WAS EARNED; a consumer must not read one. Three problem severities exist and
only two of them move rc: P_DEFECT (the declaration is broken) does; P_ADVISORY (a reading this
tool explicitly refuses to adjudicate, e.g. an executable declared cap-bearing) never does, and
bundling it into rc is DOCKET L354's false RED.

⛔ AND AT EVERY CALL SITE: a three-state contract is defeated by `||`, `and`, `if not`, and every
other two-valued idiom in the language. Writing `rc 0/1/2` in a docstring does not make a caller
three-valued — only a call site that names the states is. Test `-eq 0` / `-eq 1` / `-eq 2`.

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
# Sentinel distinguishing UNAVAILABLE manifest evidence from a desk ABSENT from a good manifest.
# They are different states with different verdicts (rc 2 vs the heuristic) and one object cannot
# carry both — CODEX finding 2.
UNAVAILABLE = object()

# ── PROBLEM SEVERITY SPLIT (2026-09-14, DOCKET L354 + L355) ──────────────────────────────────
# `problems` was a FLAT list of strings and `rc = 1 if (n_over_budget or problems)`, so THREE
# heterogeneous classes shared one bucket and one severity. Two opposite-direction failures came
# out of that single collapse:
#   · L354 (false RED): the executable-declared-cap-bearing line is ADVISORY BY ITS OWN TEXT —
#     "Not reclassified here — the declaration is the reader's." A check that explicitly declines
#     to adjudicate drove rc 1, so a legitimate `programmatic` declaration could never be green.
#   · L355 (false GREEN one surface downstream): validate_all's D1 leg received rc 1 plus a
#     `0/37 over BUDGET` summary, could not tell a MANIFEST DEFECT from a SIZE BACKLOG, read the
#     zero counts and returned PASS — dropping the defect.
# ⛔ The forbidden fix is making every rc 1 blocking: that erases the intentional advisory
# treatment of the over-budget desks and converts a size backlog into a boot blocker.
# The fix is to give the reason a CHANNEL. A three-state rc carrying a one-bit reason is the
# defect; `problems` rows are now typed, rc is computed from DEFECTS only, and the counts travel
# to callers on an explicit machine-readable line instead of being re-derived from prose.
P_DEFECT = "DEFECT"        # the DECLARATION is broken — owner fixes the row or the file. Drives rc.
P_ADVISORY = "ADVISORY"    # a reading this tool will not adjudicate. Prints, counts, NEVER drives rc.

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
    THREE return states, and a caller MUST distinguish them (cold read F1, 2026-09-12 — this
    line still described the merged two-state contract after the split, and it is the sentence a
    future caller reads before writing `if cap_bearing is None: fall back`):
      UNAVAILABLE  the manifest exists but cannot be READ -> rc 2, NEVER a heuristic fallback
      None         this desk is simply ABSENT from a well-formed manifest -> use the heuristic
      a dict       the desk is declared; grade it.
    `path`/`root` exist so --selftest can drive FROZEN tempdir fixtures rather than live surfaces
    (a regression test pinned to a live doc certifies nothing past the next edit — PROME 2026-09-09)."""
    rows, err = load_reads(path)
    base_root = root or ROOT
    # ⛔ A1 (CODEX finding 2, 2026-09-12): a MALFORMED manifest and a desk merely ABSENT from a
    # well-formed one returned the SAME absence-shaped tuple, and check_agent read both as
    # "undeclared" and fell back to the charter heuristic — so UNAVAILABLE evidence was reported as
    # ABSENT evidence, and absent evidence has a defined benign path. That is L294's own invariant,
    # violated in the tool I shipped the sweep from, and it broke my own written condition C10.
    # The two states are now distinguishable by the caller: UNAVAILABLE returns the sentinel.
    if rows is None:
        return UNAVAILABLE, None, None, None, err
    mine = [r for r in rows if r.get("reader") == name]
    if not mine:
        return None, None, None, None, f"desk {name} has NO rows in the manifest"
    # A3 (CODEX, 2026-09-12): an ATTESTATION row is only an attestation if it is WELL-FORMED.
    # The mode leg was never checked, so a row with a bogus mode still printed "ATTESTED by the
    # desk itself" and cleared the desk.
    attested = any(r.get("row_kind") == "ATTESTATION" and r.get("declared_by") == name
                   and (r.get("mode") or "").strip() == "manifest-complete" for r in mine)
    cap_bearing, visible, problems = {}, [], []
    for r in mine:
        if (r.get("row_kind") == "ATTESTATION" and r.get("declared_by") == name
                and (r.get("mode") or "").strip() != "manifest-complete"):
            # F3: without this the desk got rc 2 "you must attest" while its attestation row
            # EXISTED and was one cell wrong — sending the owner to file a duplicate instead of
            # fixing a typo. A READ row with a bad mode already gets a precise line; an
            # ATTESTATION row did not.
            problems.append((P_DEFECT,
                f"ATTESTATION row carries mode `{(r.get('mode') or '').strip() or '(blank)'}` — "
                f"an attestation must be `manifest-complete`, so this row does NOT attest and the "
                f"desk reads UNATTESTED. Fix the one cell; do not file a second attestation."))
        if r.get("row_kind") == "ATTESTATION" and r.get("declared_by") != name:
            problems.append((P_DEFECT, f"ATTESTATION signed by `{r.get('declared_by') or '(blank)'}`, not by "
                            f"{name} — INVALID (manifest ⛔ who-may-attest: reading someone else's "
                            f"charter is INFERENCE, not attestation)"))
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
            problems.append((P_DEFECT, f"`{pth}` ({src}) carries mode `{mode}` — not in the manifest's "
                            f"own mode vocabulary"))
            continue
        if not os.path.exists(full):
            # The condition the heuristic STRUCTURALLY cannot produce: a scan finds only what
            # exists, so a manifest pointing at a deleted file reads as silence.
            problems.append((P_DEFECT, f"declared {mode} read `{pth}` ({src}) DOES NOT EXIST on disk"))
            continue
        if mode in CAP_BEARING_MODES and os.path.isfile(full):
            cap_bearing[full] = (mode, src)
        else:
            visible.append((pth, mode + (" · directory" if os.path.isdir(full) else ""), src))
    # ── AN EXECUTABLE DECLARED CAP-BEARING (added 2026-09-12, on the FIRST new desk to declare) ──
    # The manifest's hardest distinction is `programmatic` vs `summary`, and its failure direction
    # MANUFACTURES a breach. BROCK — the first desk to file after the consumer half shipped — declared
    # three INVOKED TOOLS (`ledger_staleness.py`, `dashboard.py`, `corrections_boot_check.py`) as
    # `programmatic`, which is cap-bearing, producing a 🔴 OVER THE CAP on a desk that is fine. The
    # manifest's own rule settles it: "a programmatic read COUNTS if its CONTENTS ENTER SESSION
    # CONTEXT; if the tool only computes a bounded output, register `summary`." BROCK RUNS those
    # tools; it does not read their source.
    # ⚠️ MY FIRST CUT OF THIS CHECK WAS WRONG AND THE REGRESSION RUN CAUGHT IT. I keyed on CROSS-READER
    # disagreement — "this path is cap-bearing here and `summary` for another reader" — and it fired on
    # PROME/STATUS.md, which PROME reads WHOLE and WALTER reads SCOPED. Both correct: READS.tsv ruling 1
    # says in terms that ONE PATH MAY APPEAR UNDER SEVERAL READERS and that this is CORRECT, never a
    # duplicate. Different readers legitimately do different operations on one file, and my check could
    # not tell "same operation, two verdicts" from "two operations". The real signal is narrower and is
    # about the FILE, not the disagreement: nobody reads an EXECUTABLE's SOURCE into context at boot —
    # they run it. Cross-reader agreement is corroborating evidence, printed when present, never the test.
    # ⛔ THE TOOL DOES NOT RECLASSIFY. The declaration belongs to the reader; silently correcting it
    # would defeat the point of a declared perimeter. It reports; the owner fixes.
    others = {}
    for r in rows:
        if r.get("row_kind") == "READ" and r.get("reader") != name:
            others.setdefault((r.get("path") or "").strip(), set()).add((r.get("mode") or "").strip())
    for full, (mode, src) in list(cap_bearing.items()):
        rel = os.path.relpath(full, base_root)
        if not rel.endswith((".py", ".sh")):
            continue
        soft = sorted(m for m in others.get(rel, set()) if m in VISIBLE_MODES)
        corrob = (f" Another reader declares this same path `{'/'.join(soft)}` (NOT cap-bearing)."
                  if soft else "")
        # ⚠️ ADVISORY, NOT A DEFECT (severity split 2026-09-14, DOCKET L354). The sentence this
        # message ENDS with — "Not reclassified here — the declaration is the reader's" — is a
        # refusal to adjudicate, and a refusal to adjudicate cannot be a blocking verdict. Before
        # the split this line drove rc 1, so a desk whose `programmatic` declaration was CORRECT
        # had no reachable green state. It still prints, still counts, still travels on the
        # machine-readable line; it just does not decide.
        problems.append((P_ADVISORY,
            f"`{rel}` ({src}) is an EXECUTABLE declared `{mode}`, which is CAP-BEARING — so its SOURCE "
            f"is being measured against the read budget. A tool you INVOKE emits a bounded output and "
            f"is `summary`; `programmatic` is for a file whose CONTENTS ENTER CONTEXT (the manifest's "
            f"own ruling 3).{corrob} ⛔ Not reclassified here — the declaration is the reader's."))

    note = (f"perimeter: DECLARED in {os.path.relpath(READS_TSV, ROOT)} — {len(cap_bearing)} "
            f"cap-bearing (whole/programmatic) measured, {len(visible)} declared-not-counted "
            f"(scoped/grep/summary), {len(mine)} manifest row(s) for this desk; "
            + ("ATTESTED by the desk itself" if attested else
               "⛔ NOT ATTESTED by this desk — the perimeter is PARTIAL"))
    return cap_bearing, visible, problems, attested, note


# ── GENERATED-FILE DETECTOR (added 2026-09-12, RED's report, and it is a REMEDY-ROUTING question) ──
# PAT-161's remedy — rotate, or collapse pointers into one index — is WRONG for a GENERATED file, and
# wrong in the worst way: rotation is MEANINGLESS (the next generator run restores every byte, because
# a projection has no history to move) and rewording is IMPOSSIBLE (the generator copies its source
# verbatim, so the file's own author cannot reword it). RED: "it tells the owner to rotate, the owner
# complies because the instrument said so, nothing changes — and worse, the instrument then reads as
# having been followed." `finding_record_of_an_action_is_not_the_action`, manufactured by the advice.
# ⚠️ A GENERATED FILE'S SIZE IS NOT A PROPERTY OF ITSELF. It is a function of someone else's writing
# habits on a different surface, so a read-cap flag on a projection is really a flag on its SOURCE and
# routes to the SOURCE's owner. The only remedies are upstream: narrow the projected column set, or
# type the source column so narrative cannot enter it.
# ⛔ RED suggested keying on a line-0 `# GENERATED` banner. MEASURED BEFORE BUILDING, and the cheap
# version is already wrong: `AGENTS/DAEDALUS/FLEET_DIRECTORY.md` is generated and its LINE 1 carries no
# marker (the banner is on line 3), and `BOARD/INDEX.md` hides its in an HTML comment. Keying on line 0
# would MISS them — `finding_scan_keyed_on_naming_reads_local_form_as_absence`, in a detector built to
# answer a report about exactly that class. So: first FIVE lines, and the marker alone is not enough —
# prose says "generated" constantly — it must sit beside an edit prohibition or a regenerate command.
# Measured on the tree at build time: 13 files of 12,994 match, and the handful of false positives are
# packets DESCRIBING a generated file, which are never boot whole-reads. The message is phrased
# conditionally ("announces itself as") so a false positive is self-correcting: the reader can see the
# banner or its absence.
_GEN_MARK = re.compile(r"\bAUTO-?GENERATED\b|\bGENERATED\b", re.I)
_GEN_PROHIB = re.compile(r"do not (?:hand-)?edit|never hand-edit|regenerate\b|rendered from", re.I)


def generated_banner(path):
    """The banner line if this file announces itself GENERATED, else None. Read-only, never raises."""
    for ln in _head_lines(path):
        if _GEN_MARK.search(ln) and _GEN_PROHIB.search(ln):
            return ln.strip()[:150]
    return None


def _head_lines(path, n=5):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return [next(fh, "") for _ in range(n)]
    except OSError:
        return []


# ── WHO THE GENERATED FLAG ROUTES TO (added 2026-09-14, DOCKET L349 condition C7) ─────────────
# The remedy paragraph shipped 2026-09-12 and says the right thing — rotation is meaningless, the
# size is a property of the SOURCE surface, the flag routes to the SOURCE's owner. It never said
# WHO. `finding_imperfect_level_to_the_right_owner_beats_a_perfect_one_to_nobody`: half a
# dispatch's value is the owner re-reading its own file, and "route it upstream" with no upstream
# named is a remedy the reader cannot execute — which is the same shape as the inapplicable remedy
# the row was raised about. A named-but-imperfect target beats a correct-but-addressless one.
# MEASURED BEFORE BUILDING, on the two live generated boot-reads: RED's
# FALSIFICATION_TRIGGERS_SCAN.tsv banner carries `canon=registry/FALSIFICATION_TRIGGERS.tsv` and
# `Regenerate: python3 AGENTS/RED/scripts/gen_trigger_scan.py`; DAEDALUS's FLEET_DIRECTORY.md names
# PROME/ROSTER.md, AGENTS/DAEDALUS/FLEET_MAP.tsv and render_directory.py across lines 1-3. So the
# generator and the sources ARE stated in the banner region — they just were not being read out.
# ⛔ This DERIVES a candidate, it does not adjudicate one. Where the banner names nothing, the
# function says so in those words rather than guessing a desk from the file's own path — a
# generated file's location tells you its READER, which is precisely the wrong owner.
_PATHY = re.compile(r"(?<![\w/.-])((?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_.-]+\.(?:tsv|md|py|sh|json|csv))")


def generated_sources(path, n=5):
    """(source_paths, owner_desks) named in this file's banner region. ([], []) when none are."""
    me = os.path.normpath(os.path.relpath(os.path.abspath(path), ROOT))
    srcs, owners = [], []
    for ln in _head_lines(path, n):
        for hit in _PATHY.findall(ln):
            hit = os.path.normpath(hit)
            if hit == me or os.path.basename(hit) == os.path.basename(me):
                continue                      # the file naming itself is not its own source
            if hit not in srcs:
                srcs.append(hit)
            parts = hit.split(os.sep)
            if len(parts) >= 2 and parts[0] == "AGENTS" and parts[1] not in owners:
                owners.append(parts[1])
            elif len(parts) >= 2 and parts[0] == "PROME" and "PROME" not in owners:
                owners.append("PROME")
    return srcs, owners


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
    if cap_bearing is UNAVAILABLE:
        # A1: the manifest exists but could not be READ. That is UNAVAILABLE evidence, not absent
        # evidence, and it must NOT fall through to the charter heuristic — which would print a
        # clean line built from a different perimeter while the declared one was unreadable.
        # Restores acceptance condition C10 (runs/2026-09-12_R7_STAGE2_READS_CONSUMER.md), which
        # was written, tested at the PARSER, and never enforced at the CALLER.
        if not quiet:
            print(f"READ-CAP 2 CANNOT-EVALUATE [{name}]: {dnote}. The manifest is UNREADABLE, which is "
                  f"NOT the same as this desk being undeclared — so the charter heuristic is NOT used "
                  f"as a fallback here. Fix the manifest, or re-run once the writer finishes.")
        return 2, None
    declared = cap_bearing is not None
    if declared and not attested:
        # The manifest's own ⛔: rows without an attestation are a PARTIAL perimeter, and a check
        # over a partial perimeter must report UNKNOWN. Reporting clean here is the exact defect
        # this file exists to retire. Fail CLOSED, never to the heuristic (which would read clean).
        if not quiet:
            print(f"READ-CAP 2 CANNOT-EVALUATE [{name}]: {dnote}. An unattested desk is UNKNOWN, "
                  f"never clean — the desk itself must attest (packet to PROME/inbox/; no desk may "
                  f"commit inside PROME/, and PROME may not attest on a desk's behalf).")
            for sev, pr in problems or []:
                print(f"  {'⛔' if sev == P_DEFECT else 'ℹ️ ADVISORY:'} {pr}")
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
    # ── rc IS COMPUTED FROM DEFECTS ONLY (severity split 2026-09-14, DOCKET L354) ──
    # Was `1 if (n_over_budget or problems)`. An ADVISORY is a reading this tool refuses to
    # adjudicate; it can never be the reason a desk is not green. DEFECTS and the size backlog
    # both still drive rc 1 — what changed is that they are now SEPARATELY COUNTED and stated, so
    # no consumer has to re-derive which one fired (DOCKET L355 condition C1/C2).
    defects = [m for sev, m in (problems or []) if sev == P_DEFECT]
    advisories = [m for sev, m in (problems or []) if sev == P_ADVISORY]
    rc = 1 if (n_over_budget or defects) else 0
    # GENERATED reads carrying a REMEDY-BEARING tier, counted so the count can travel (L349 / C7).
    # ⚠️ THE TIER SET IS 🔴/🟠/🟡, NOT 🔴/🟠 — found by reading the LIVE instance the row was
    # raised about instead of the row's description of it. The 9/12 generated branch sat inside
    # `if rc:`, so it could only ever fire on an OVER-BUDGET file. But the live case,
    # AGENTS/RED/registry/FALSIFICATION_TRIGGERS_SCAN.tsv (WALTER:6b, `whole`), is 30,691 B = 94%
    # of budget — 🟡, rc 0 — and grade() hands it the word "rotate-tier (≥75% of budget)".
    # ⇒ THE INAPPLICABLE REMEDY WAS ALREADY PRINTING, ONE TIER BELOW WHERE THE FIX WAS BUILT, and
    # at rc 0 where no caveat could reach it. L349 was registered as "fix BEFORE the instrument
    # starts printing at scale"; it had already started. `finding_scan_keyed_on_naming_reads_local_
    # form_as_absence` — the branch was keyed on the two marks someone had named, and the third
    # mark carries the same remedy word. A remedy word, not a severity, is what needs the caveat.
    REMEDY_TIERS = ("🔴", "🟠", "🟡")
    gen_flagged = [(rel, generated_banner(os.path.join(base, rel)))
                   for mark, rel, *_ in rows if mark in REMEDY_TIERS]
    gen_flagged = [(r, bn) for r, bn in gen_flagged if bn]
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
        for sev, pr in problems or []:
            print(f"  {'⛔' if sev == P_DEFECT else 'ℹ️ ADVISORY:'} {pr}")
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
                      f"   ⛔ AND DO NOT TRY TO REWRITE ALREADY-COMPRESSED TEXT UNDER: a tightening pass over "
                      f"settled prose RELIABLY ADDS bytes (measured +242 B and +451 B on two real attempts) "
                      f"because the compression is already gone and all a re-read adds is the disambiguation "
                      f"it notices. Only MOVING text out removes them — rotate, or collapse several verbose "
                      f"pointers into ONE terse index; both are mechanical, a rewrite is not. (RED 2026-09-12: "
                      f"a reword DOES gain on a first draft you wrote an hour ago and have not yet compressed "
                      f"— +584 B there — but it hits a content floor, and rotation is what clears budget.)\n"
                      # BROCK 2026-09-12, and it cost it a cycle: it wrote "SCOPED READ, NEVER WHOLE" —
                      # semantically exact — and this scanner STILL scored the file a WHOLE read, because
                      # ON_DEMAND_MARKERS matches the literal substring "never read" and BROCK wrote "never
                      # whole". A CORRECT PROTOCOL STATEMENT THE INSTRUMENT CANNOT PARSE IS WORTH ZERO.
                      # BROCK explicitly did NOT ask for a looser matcher — fail-closed is right here, and a
                      # fuzzy one would silently exempt real breaches — but the marker vocabulary is invisible
                      # unless you read this source, and 29 of 37 desks have not. So: PRINT IT. Same reasoning
                      # as PAT-161's line — tell the desk the MECHANICAL MOVE, not the principle.
                      f"   ℹ️  IF A FLAGGED FILE IS NOT ACTUALLY READ WHOLE, the fix may be your CHARTER'S\n"
                      f"      WORDING, not the file. This scanner keys on LITERAL phrases; a semantically exact\n"
                      f"      paraphrase does NOT match (BROCK wrote 'never whole' and stayed flagged).\n"
                      f"      Phrases that EXCLUDE a file: {', '.join(repr(k) for k in ON_DEMAND_MARKERS)}.\n"
                      f"      Phrases that mark a PART read: 'header', 'section', 'the top', 'first/last N',\n"
                      f"      'only the', 'just the', 'rows ', 'lines ', 'table', 'summary'.\n"
                      f"      ⛔ The matcher is deliberately LITERAL and fail-closed. Say the exact words — or\n"
                      f"      declare the file in PROME/registry/READS.tsv, which supersedes this heuristic.")
            if defects:
                print(f"⚠️  READ-CAP 1 [{name}]: {len(defects)} manifest defect(s) above. A declared "
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
        # ── GENERATED PROJECTIONS: PRINTED AT EVERY REMEDY TIER, NOT ONLY INSIDE `if rc:` ──
        # Hoisted out of the rc branch 2026-09-14 (DOCKET L349). While it lived under `if rc:` it
        # could not reach a 🟡 rotate-tier row, which is rc 0 — and the live instance the row was
        # raised about is exactly that: 94% of budget, rc 0, handed the word `rotate-tier` with no
        # caveat attached. A caveat that only fires once the file is ALREADY over budget arrives
        # after the owner has acted on the advice it was meant to qualify.
        for rel, banner in gen_flagged:
            print(f"   ⚠️  {rel} ANNOUNCES ITSELF AS GENERATED — every remedy this check names for it, in the\n"
                      f"      table row above (`rotate-tier`) and in any over-budget paragraph, does NOT apply.\n"
                  f"      banner: {banner}\n"
                  f"      Rotation is MEANINGLESS (the next generator run restores every byte; a projection\n"
                  f"      has no history to move) and rewording is IMPOSSIBLE (the generator copies its\n"
                  f"      source verbatim). A generated file's SIZE IS NOT A PROPERTY OF ITSELF — it is a\n"
                  f"      function of writing habits on its SOURCE surface. ⇒ This flag is really a flag on\n"
                  f"      the SOURCE and routes to the SOURCE's owner. The only remedies are upstream:\n"
                  f"      narrow the projected column set, or TYPE the source column so narrative cannot\n"
                  f"      enter it. (RED 2026-09-12, on its own FALSIFICATION_TRIGGERS_SCAN.tsv.)")
            # C7 (2026-09-14): say WHO. "Route it upstream" with no upstream named is itself a
            # remedy the reader cannot execute — the same shape as the inapplicable advice this
            # branch exists to retire. Derived from the banner region, never from the file's own
            # path (that names its READER, which is the wrong owner by construction).
            srcs, owners = generated_sources(os.path.join(base, rel))
            if owners or srcs:
                print(f"      ➜ ROUTE TO: {', '.join(owners) if owners else '(no desk named in the banner)'}"
                      f"   SOURCE(S) the banner names: {', '.join(srcs) if srcs else '(none)'}\n"
                      f"        ⚠️  DERIVED from this file's own banner, not adjudicated — confirm before "
                      f"sending. The reader's desk is NOT the owner of these bytes.")
            else:
                print(f"      ➜ ROUTE TO: ⛔ CANNOT DERIVE — this file's banner names no source path and no\n"
                      f"        generator. Ask its owner who regenerates it; do NOT infer the owner from the\n"
                      f"        file's location, which names the READER, not the source.")

    # W3: `problems` travels with the result. main() previously inferred the REASON for rc from
    # the over-budget counts, which is what produced the mark bug and then repeated it in the
    # label one line later. One instance did mean two; the fix is to stop inferring.
    if advisories and not quiet:
        print(f"ℹ️  READ-CAP ADVISORY [{name}]: {len(advisories)} reading(s) this check will NOT "
              f"adjudicate (above). ⛔ These do NOT affect rc — the declaration is the reader's, and a "
              f"refusal to adjudicate cannot be a blocking verdict (severity split 2026-09-14, L354).")
    return rc, (name, len(rows), n_over_budget, n_over_cap, rows, defects, advisories, gen_flagged)


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
    import tempfile, io, contextlib
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
        chk("C2/C5 a clean manifest yields no DEFECT and no ADVISORY",
            ([sev for sev, _x in pr], len(pr)), ([], 0))
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
        chk("C5 foreign attestation reported", any("INVALID" in x for _s, x in pr), True)
        chk("C5 ...and it is a DEFECT, not an advisory",
            sorted({_s for _s, x in pr if "INVALID" in x}), [P_DEFECT])
        # C6 — CAPABLE: a declared read that does not exist on disk. The heuristic CANNOT produce this.
        m = _fixture(t, [A, "READ\tD\tgone.md\twhole\ts1\tD\t2026-09-12\t-"], {})
        cb, vis, pr, att, _ = declared_reads("D", m, t)
        chk("C6 absent declared path reported", any("DOES NOT EXIST" in x for _s, x in pr), True)
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
        chk("C10 short row => UNAVAILABLE sentinel (not None: None means ABSENT)",
            declared_reads("D", bad, t)[0] is UNAVAILABLE, True)
        open(bad, "w").write("reader\tpath\n")
        chk("C10 bad header => UNAVAILABLE sentinel", declared_reads("D", bad, t)[0] is UNAVAILABLE, True)
        chk("C10 missing manifest file => UNAVAILABLE sentinel",
            declared_reads("D", os.path.join(t, "nope.tsv"), t)[0] is UNAVAILABLE, True)
        # C11/C4 — a desk with NO rows falls through to the heuristic (cap_bearing is None).
        m = _fixture(t, [A], {})
        chk("C4 desk ABSENT from a good manifest => None, which means use the heuristic",
            declared_reads("ZZZ", m, t)[0] is None, True)
        # unknown mode is a manifest defect, not a silent skip
        m = _fixture(t, [A, "READ\tD\tsmall.md\tskim\ts1\tD\t2026-09-12\t-"], {"small.md": 100})
        chk("unknown mode reported",
            any("mode vocabulary" in x for _s, x in declared_reads("D", m, t)[2]), True)
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

        # ── EXECUTABLE-DECLARED-CAP-BEARING (BROCK 2026-09-12) ───────────────────────────────
        # ⚠️ This guard's v1 keyed on CROSS-READER disagreement and false-positived on PROME/STATUS.md
        # (PROME reads it whole, WALTER scoped — both correct under READS.tsv ruling 1). The negative
        # legs below are that regression, frozen: a .md declared `whole` must NEVER flag, however many
        # other readers declare it differently.
        m = _fixture(t, [A,
                         "READ\tD\ttool.py\tprogrammatic\ts1\tD\t2026-09-12\t-",
                         "READ\tD\tdoc.md\twhole\ts2\tD\t2026-09-12\t-",
                         "READ\tE\tdoc.md\tscoped\ts3\tE\t2026-09-12\tanother reader, a PART",
                         "READ\tE\ttool.py\tsummary\ts4\tE\t2026-09-12\tE invokes it"],
                     {"tool.py": 100, "doc.md": 100})
        cb, vis, pr, att, _ = declared_reads("D", m, t)
        exe = [x for sev, x in pr if "EXECUTABLE" in x]
        chk("exe: .py declared programmatic is flagged", len(exe), 1)
        chk("exe: the corroborating cross-reader mode is named", "summary" in exe[0], True)
        chk("exe: a .md whole read is NOT flagged though another reader says scoped",
            any("doc.md" in x for sev, x in pr), False)
        # ── SEVERITY SPLIT (2026-09-14, DOCKET L354) ─ the executable line is ADVISORY, not a
        # DEFECT, and the split is asserted on the TYPE, not on the message text: a message can be
        # reworded, a severity token cannot drift silently. Both directions watched.
        chk("split: the executable reading is typed ADVISORY",
            sorted({sev for sev, x in pr if "EXECUTABLE" in x}), [P_ADVISORY])
        _sr, _sroot = READS_TSV, ROOT
        READS_TSV, ROOT = m, t
        _adv_rc, _adv_res = check_agent("D", quiet=True)
        READS_TSV, ROOT = _sr, _sroot
        chk("split: an ADVISORY-only desk is rc 0 — a legitimate `programmatic` CAN be green",
            _adv_rc, 0)
        chk("split: ...and the advisory is still REPORTED, not deleted (it counts)",
            (len(_adv_res[6]), len(_adv_res[5])), (1, 0))
        m2 = _fixture(t, [A, "READ\tD\tgone.md\twhole\ts1\tD\t2026-09-12\t-"])
        pr2 = declared_reads("D", m2, t)[2]
        chk("split: a missing declared file is typed DEFECT (not advisory)",
            sorted({sev for sev, x in pr2}), [P_DEFECT])
        m2 = _fixture(t, [A, "READ\tD\tdoc.md\tbogusmode\ts1\tD\t2026-09-12\t-"], {"doc.md": 10})
        chk("split: a bad mode is typed DEFECT",
            sorted({sev for sev, x in declared_reads("D", m2, t)[2]}), [P_DEFECT])
        # OVERLAP NEIGHBOUR (the category that would have been missed): a desk carrying BOTH an
        # advisory and a defect must report BOTH, each under its own severity, and be rc 1 for the
        # DEFECT — never rc 1 "because of the advisory" and never advisory-suppressed by the defect.
        m2 = _fixture(t, [A,
                          "READ\tD\ttool.py\tprogrammatic\ts1\tD\t2026-09-12\t-",
                          "READ\tD\tgone.md\twhole\ts2\tD\t2026-09-12\t-"], {"tool.py": 100})
        pr3 = declared_reads("D", m2, t)[2]
        chk("overlap: both severities survive together",
            (sorted({sev for sev, x in pr3}), len(pr3)), ([P_ADVISORY, P_DEFECT], 2))
        m = _fixture(t, [A, "READ\tD\ttool.py\tsummary\ts1\tD\t2026-09-12\t-"], {"tool.py": 100})
        chk("exe: .py declared summary is clean (the correct form)",
            [x for sev, x in declared_reads("D", m, t)[2] if "EXECUTABLE" in x], [])

        # ── GENERATED-FILE REMEDY ROUTING (RED 2026-09-12) ────────────────────────────────────
        # The banner must be found ANYWHERE in the first five lines, not on line 0: this repo's own
        # generated files put it on line 3 (FLEET_DIRECTORY.md) and inside an HTML comment
        # (BOARD/INDEX.md), so a line-0 detector misses them — and the cost of a miss here is
        # printing a remedy that CANNOT work while the instrument reads as having been followed.
        for rel, body, want, why in [
            ("l1.tsv", "# GENERATED VIEW — do not hand-edit. Regenerate: python3 gen.py\nx\n", True,
             "banner line 1"),
            ("l3.md", "# Title\n\n> **GENERATED — DO NOT EDIT.** Rendered from X\n", True,
             "banner line 3 — a line-0 detector MISSES this"),
            ("html.md", "# T\n\n<!-- GENERATED by gen.py — do not hand-edit. -->\n", True,
             "banner in an HTML comment"),
            ("prose.md", "# T\n\nThe report was generated last week from the desk's notes.\n", False,
             "prose says 'generated' — marker alone must NOT match"),
            ("plain.md", "# Ordinary hand-written file\nbody\n", False, "no marker"),
            ("short.md", "", False, "empty file must not raise"),
        ]:
            f = os.path.join(t, rel)
            open(f, "w").write(body)
            chk(f"generated banner: {why}", generated_banner(f) is not None, want)
        chk("generated banner: missing file returns None, never raises",
            generated_banner(os.path.join(t, "nope.md")), None)

        # ── ROUTING TARGET (2026-09-14, DOCKET L349 / C7) — "route it upstream" must name WHO ──
        # Both directions: a banner that names sources yields them; a banner that names none must
        # say CANNOT DERIVE rather than guess from the file's own path (which names its READER).
        _sroot = ROOT
        try:
            ROOT = t
            open(os.path.join(t, "r1.tsv"), "w").write(
                "# GENERATED VIEW — do not hand-edit. Regenerate: python3 AGENTS/ZZ/scripts/gen.py "
                "| canon=AGENTS/ZZ/registry/CANON.tsv\nrow\n")
            srcs, owners = generated_sources(os.path.join(t, "r1.tsv"))
            chk("route: the banner's source paths are read out",
                sorted(srcs), ["AGENTS/ZZ/registry/CANON.tsv", "AGENTS/ZZ/scripts/gen.py"])
            chk("route: the owning desk is derived from the source path", owners, ["ZZ"])
            open(os.path.join(t, "r2.tsv"), "w").write(
                "# GENERATED — do not hand-edit.\nrow\n")
            chk("route: a banner naming nothing derives NOTHING (never guesses)",
                generated_sources(os.path.join(t, "r2.tsv")), ([], []))
            open(os.path.join(t, "r3.tsv"), "w").write(
                "# GENERATED — do not hand-edit. Regenerate: python3 r3_gen.py from r3.tsv\nrow\n")
            # A BARE filename (no directory) is deliberately NOT derived, and this leg pins that
            # choice rather than the convenience: a bare token is relative to an unstated cwd, so it
            # names no desk and cannot answer the only question this function is asked — WHO owns
            # these bytes. The honest output is CANNOT DERIVE, which sends the reader to ask.
            # Loosening the matcher to bare tokens would also start matching ordinary prose.
            chk("route: a BARE filename derives no owner (fail closed, do not guess)",
                generated_sources(os.path.join(t, "r3.tsv")), ([], []))
        finally:
            ROOT = _sroot

        # ── PUBLIC-PATH LEGS (CODEX findings 2 & 3, 2026-09-12) ───────────────────────────────
        # ⛔ THESE EXIST BECAUSE THE HELPER LEGS WERE NOT ENOUGH AND A GREEN SUITE CERTIFIED A
        # FALSE-GREEN TOOL. C10 above asserts `declared_reads(...)[0] is None` on a malformed
        # manifest — TRUE, the parser was always right — while `check_agent` read that same value as
        # "undeclared" and fell back to the charter heuristic, printing a clean line. I tested the
        # COMPONENT UNDER the defect instead of the PATH THROUGH it. Third instance of that shape in
        # one day across three desks (RED's §5 gate; PROME's spawn_list, whose tests drove the writer
        # and the gate but never main()). Every leg below drives a PUBLIC entry point and asserts the
        # rc a CALLER sees — never a helper's return value.
        sav_r2, sav_root2 = READS_TSV, ROOT
        try:
            ROOT = t
            os.makedirs(os.path.join(t, "AGENTS", "ZD"), exist_ok=True)
            open(os.path.join(t, "AGENTS", "ZD", "CLAUDE.md"), "w").write(
                "# ZD\n## SPAWN PROTOCOL\n1. Read `STATUS.md`\n")
            open(os.path.join(t, "AGENTS", "ZD", "STATUS.md"), "w").write("s")
            AZ = "ATTESTATION\tZD\t.\tmanifest-complete\ts\tZD\t2026-09-12\tok"
            # A1 — UNAVAILABLE manifest must be rc 2 AT THE CALLER, never a heuristic fallback.
            bad2 = os.path.join(t, "bad2.tsv"); open(bad2, "w").write("broken\n")
            READS_TSV = bad2
            chk("A1 public: malformed manifest => check_agent rc 2 (C10, at the CALLER)",
                check_agent("ZD", quiet=True)[0], 2)
            open(bad2, "w").write(HDR + "\nREAD\tZD\n")      # short row
            chk("A1 public: short-row manifest => check_agent rc 2",
                check_agent("ZD", quiet=True)[0], 2)
            # and a desk genuinely ABSENT from a WELL-FORMED manifest still gets the heuristic
            READS_TSV = _fixture(t, [AZ, "READ\tZD\tAGENTS/ZD/STATUS.md\twhole\ts\tZD\t2026-09-12\t-"], {})
            os.makedirs(os.path.join(t, "AGENTS", "QQ"), exist_ok=True)
            open(os.path.join(t, "AGENTS", "QQ", "CLAUDE.md"), "w").write(
                "# QQ\n## SPAWN PROTOCOL\n1. Read `STATUS.md`\n")
            open(os.path.join(t, "AGENTS", "QQ", "STATUS.md"), "w").write("s")
            chk("A1 public: desk ABSENT from a GOOD manifest still uses the heuristic (rc 0)",
                check_agent("QQ", quiet=True)[0], 0)
            # A3 — an ATTESTATION with a bad mode is NOT an attestation => rc 2, not a green line.
            READS_TSV = _fixture(t, ["ATTESTATION\tZD\t.\tbogus\ts\tZD\t2026-09-12\tx",
                                     "READ\tZD\tAGENTS/ZD/STATUS.md\twhole\ts\tZD\t2026-09-12\t-"], {})
            chk("A3 public: ATTESTATION with a bogus mode => rc 2 UNATTESTED",
                check_agent("ZD", quiet=True)[0], 2)
            # A2 — --fleet must never read greener than --agent.
            READS_TSV = _fixture(t, [AZ, "READ\tZD\tAGENTS/ZD/gone.md\twhole\ts\tZD\t2026-09-12\t-"], {})
            rc_agent = check_agent("ZD", quiet=True)[0]
            chk("A2: a missing declared file is rc 1 at --agent", rc_agent, 1)
            fd = os.path.join(t, "AGENTS", "DAEDALUS")
            os.makedirs(fd, exist_ok=True)
            open(os.path.join(fd, "FLEET_DIRECTORY.md"), "w").write(
                "## ACTIVE\n| ZD | desk |\n")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc_fleet = main(["x", "--fleet"])
            chk("A2: and --fleet does NOT report it greener", rc_fleet >= rc_agent, True)
            chk("A2: the fleet ROW shows the defect, not a clean tick",
                "MANIFEST DEFECT" in buf.getvalue(), True)
            chk("A2: a MANIFEST-only defect is marked ⛔", "⛔ ZD" in buf.getvalue(), True)
            # …and an OVER-BUDGET desk must KEEP its cap mark, not be overwritten by ⛔.
            open(os.path.join(t, "AGENTS", "ZD", "big.md"), "w").write("x" * (BUDGET_BYTES + 10))
            READS_TSV = _fixture(t, [AZ, "READ\tZD\tAGENTS/ZD/big.md\twhole\ts\tZD\t2026-09-12\t-"], {})
            buf2 = io.StringIO()
            with contextlib.redirect_stdout(buf2):
                main(["x", "--fleet"])
            # ── COLD-READ REPAIR LEGS (F1/F2/F3/W1, 2026-09-12) ───────────────────────────────
            # Every one drives a PUBLIC path and asserts what a CALLER or a DOWNSTREAM PARSER sees.
            # F2: a run that assessed NOTHING must not print a totals line a parser can read as green.
            broke = os.path.join(t, "broke.tsv"); open(broke, "w").write("broken\n")
            READS_TSV = broke
            b3 = io.StringIO()
            with contextlib.redirect_stdout(b3):
                rc_all = main(["x", "--fleet"])
            o3 = b3.getvalue().replace("\n", " ")
            chk("F2: all-CANNOT-EVALUATE fleet run returns rc 2", rc_all, 2)
            chk("F2: and prints NO totals line a parser could read as green",
                re.search(r"over BUDGET:\s*\d+\s*/\s*\d+.*?over the CAP", o3) is None, True)
            chk("F2: and names the MANIFEST, not N desks", "broke.tsv" in o3, True)
            # F3: a malformed ATTESTATION must NAME the cell, not just say "you must attest".
            READS_TSV = _fixture(t, ["ATTESTATION\tZD\t.\tbogus\ts\tZD\t2026-09-12\tx",
                                     "READ\tZD\tAGENTS/ZD/STATUS.md\twhole\ts\tZD\t2026-09-12\t-"], {})
            b4 = io.StringIO()
            with contextlib.redirect_stdout(b4):
                rc4 = check_agent("ZD")
            chk("F3: bogus ATTESTATION mode => rc 2", rc4[0], 2)
            chk("F3: and the offending CELL is named, not just 'you must attest'",
                "must be `manifest-complete`" in b4.getvalue(), True)
            # W1: a desk BOTH over budget AND manifest-defective must show BOTH, not just the cap.
            open(os.path.join(t, "AGENTS", "ZD", "big2.md"), "w").write("x" * (BUDGET_BYTES + 10))
            READS_TSV = _fixture(t, [AZ,
                                     "READ\tZD\tAGENTS/ZD/big2.md\twhole\ts\tZD\t2026-09-12\t-",
                                     "READ\tZD\tAGENTS/ZD/gone2.md\twhole\ts\tZD\t2026-09-12\t-"], {})
            b5 = io.StringIO()
            with contextlib.redirect_stdout(b5):
                main(["x", "--fleet"])
            chk("W1: over-budget AND manifest-defective shows the cap mark AND the defect label",
                "🟠 ZD" in b5.getvalue() and "MANIFEST DEFECT" in b5.getvalue(), True)
            chk("A2: an OVER-BUDGET desk keeps its cap mark (🟠), not ⛔",
                "🟠 ZD" in buf2.getvalue() and "⛔ ZD" not in buf2.getvalue(), True)
        finally:
            READS_TSV, ROOT = sav_r2, sav_root2

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


# ── THE MACHINE-READABLE REASON CHANNEL (2026-09-14, DOCKET L355 conditions C1/C3) ───────────
# WHY THIS EXISTS AND WHY A PROSE SUMMARY IS NOT IT. scripts/validate_all.py's D1 leg ran this
# tool, matched a regex against the TOTALS SENTENCE, and decided PASS/ADVISORY from the two
# numbers it found. That is re-deriving a REASON from a RESULT. With an identical
# "0/37 over BUDGET" summary the child's rc 0, 1 and 2 are three different worlds, and the
# summary is byte-identical in all three — so a MISSING DECLARED FILE (manifest defect, rc 1,
# zero over-budget desks) rendered as PASS. The counts were true; the verdict was invented.
#
# ⛔ THE RULE THIS ENCODES: pass the reason ACROSS the boundary; never re-derive it from prose on
# the far side. A three-state rc carrying a one-bit reason is not a contract, it is a guess with
# an exit code attached.
#
# CONTRACT — one line, last line of output, stable key=value pairs, never localised, never
# reordered by content. `assessed` GATES EVERY OTHER COUNT: assessed=0 means no number on this
# line was earned and a consumer MUST NOT read one (the same discipline as the fleet totals
# suppression added 2026-09-12 — a number is never printed where it cannot be earned, and never
# BELIEVED where it could not be). Keys may be ADDED; existing keys never change meaning.
RESULT_PREFIX = "READ-CAP-RESULT v1"


def _result_line(mode, rc, assessed, **counts):
    parts = [RESULT_PREFIX, f"mode={mode}", f"rc={rc}", f"assessed={assessed}"]
    parts += [f"{k}={v}" for k, v in counts.items()]
    return " ".join(parts)


def main(argv):
    args = argv[1:]
    if "--selftest" in args:
        return selftest()
    require_manifest = "--require-manifest" in args
    if require_manifest:
        args = [a for a in args if a != "--require-manifest"]
    if "--agent" in args:
        name = args[args.index("--agent") + 1]
        rc, res = check_agent(name, require_manifest=require_manifest)
        if res is None:
            # rc 2: nothing was assessed. Every count below is ZERO because it is UNEARNED, not
            # because it is clean, and `assessed=0` is the flag that says so.
            print(_result_line("agent", rc, 0, desk=name, reads=0, over_budget=0, over_cap=0,
                               manifest_defects=0, advisories=0, generated_flagged=0))
        else:
            _, n, nb, nc, _rows, defs, advs, gen = res
            print(_result_line("agent", rc, 1, desk=name, reads=n, over_budget=nb, over_cap=nc,
                               manifest_defects=len(defs), advisories=len(advs),
                               generated_flagged=len(gen)))
        return rc
    if "--fleet" in args:
        desks = fleet_desks()
        if not desks:
            print("READ-CAP 2 CANNOT-EVALUATE: FLEET_DIRECTORY.md unreadable — regenerate it")
            print(_result_line("fleet", 2, 0, desks=0, cannot_evaluate=0, desks_over_budget=0,
                               desks_over_cap=0, desks_with_manifest_defect=0,
                               desks_with_advisory=0, generated_flagged=0))
            return 2
        print(f"READ-CAP FLEET — cap {CAP_BYTES:,} B · budget {BUDGET_BYTES:,} B · {len(desks)} active+tier-2 desks · "
              f"perimeter per desk = heuristic boot-read set (see --agent for each)")
        print(f"  {'desk':10}{'reads':>6}{'>budget':>9}{'>cap':>6}  worst file (% is of BUDGET — the number the verdict grades)")
        tot_b = tot_c = tot_def = tot_adv = tot_gen = 0; bad = []; cant = []
        for d in desks:
            rc, res = check_agent(d, quiet=True)
            if res is None:
                # A2 (CODEX finding 3): rc 2 desks were already collected here, but a desk with an
                # rc 1 MANIFEST DEFECT returned a result whose over-budget COUNTS were zero, and the
                # fleet verdict was computed from those counts alone — so a missing declared file or
                # an invalid mode rendered as a GREEN, ZERO-READ row. A desk we could not assess must
                # never read greener in --fleet than it does in --agent.
                cant.append(d); continue
            name, n, nb, nc, rows, probs, advs, gen = res
            tot_b += (nb > 0); tot_c += (nc > 0)
            tot_def += (len(probs) > 0); tot_adv += (len(advs) > 0); tot_gen += len(gen)
            worst = rows[0] if rows else None
            w = f"{worst[1]} {worst[3]:.0%} of budget" if worst else "—"
            mark = "🔴" if nc else ("🟠" if nb else "✅")
            # ⚠️ ONLY when there is no CAP finding to show. rc is 1 for ANY finding, so an
            # unguarded `if rc` overwrote 🟠/🔴 on every over-BUDGET desk and destroyed the
            # cap/manifest distinction this mark exists to make — a defect I introduced in the
            # CODEX repair and caught by READING THE ROWS, not the rc. My own A2 leg asserted the
            # new label appeared and the rc propagated; it never asserted the MARK of a desk whose
            # rc came from a CAP breach. Testing what I added, not what I broke.
            if probs and not nb:
                mark = "⛔"           # a manifest defect, with no cap finding to display
            print(f"  {mark} {name:8}{n:>6}{nb:>9}{nc:>6}  {w}"
                  + ("   MANIFEST DEFECT — see `--agent " + name + "`" if probs else ""))
            # W1: the label is keyed on `probs` ALONE, not `probs and not nb` — a desk that is
            # BOTH over budget and manifest-defective showed a plain 🟠 and the defect vanished,
            # sending the owner to apply a rotation remedy to a declaration defect.
            if nb or rc: bad.append(name)
        # ❌F2 (cold read, 2026-09-12): this line printed "0/37 · 0/37" for a run that assessed
        # NOTHING. One malformed row in a manifest PROME edits live sends EVERY desk to `cant`,
        # and the totals still read green — while scripts/validate_all.py's D1 leg parses THIS
        # STRING and never inspects the returncode, so a registered fleet check reported PASS.
        # ⛔ The repair for the false-green class introduced a false green one surface downstream.
        # Totals are now stated over what was ACTUALLY ASSESSED, and are SUPPRESSED entirely when
        # nothing was — a number is never printed where it cannot be earned.
        n_assessed = len(desks) - len(cant)
        if n_assessed == 0:
            print(f"\n  ⛔ NO DESK WAS ASSESSED — {len(cant)}/{len(desks)} CANNOT-EVALUATE. No totals are "
                  f"printed, because none can be earned from this run.\n"
                  f"     Most likely cause: {os.path.relpath(READS_TSV, ROOT)} is unreadable or "
                  f"half-written — check THAT ONE FILE first, not {len(desks)} desks. "
                  f"Run `--agent <NAME>` on any one of them for the reason.")
        else:
            print(f"\n  desks with ≥1 boot read over BUDGET: {tot_b}/{n_assessed} · over the CAP: "
                  f"{tot_c}/{n_assessed}" + (f"   (of {n_assessed} ASSESSED, not {len(desks)} — "
                  f"{len(cant)} CANNOT-EVALUATE: {', '.join(cant)})" if cant else ""))
        if tot_adv:
            print(f"  ℹ️  {tot_adv} desk(s) carry an ADVISORY reading this check will not adjudicate "
                  f"(`--agent <NAME>` for the text). ⛔ Advisories do NOT drive rc — a refusal to "
                  f"adjudicate cannot be a blocking verdict (severity split 2026-09-14, DOCKET L354).")
        if tot_gen:
            print(f"  ℹ️  {tot_gen} flagged read(s) are GENERATED projections — those flags route to the "
                  f"SOURCE surface's owner, not to the reader's desk (`--agent <NAME>` names the target).")
        rc_fleet = 2 if cant else (1 if bad else 0)
        print(_result_line("fleet", rc_fleet, n_assessed, desks=len(desks),
                           cannot_evaluate=len(cant), desks_over_budget=tot_b,
                           desks_over_cap=tot_c, desks_with_manifest_defect=tot_def,
                           desks_with_advisory=tot_adv, generated_flagged=tot_gen))
        return rc_fleet
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
