#!/usr/bin/env python3
"""
consumer_check.py — who is still carrying a number you have superseded?

WHY THIS EXISTS (HENRY, 2026-07-28)
-----------------------------------
Agents publish numbers that OTHER agents wire into live gates, and nobody
tracks the consumers. VIOLET carried HENRY's 2026-07-23 gamma flip (~7,496)
as the thesis-kill line for a live position for five days. HENRY refreshed
that number twice (7/27 → ~7,479, 7/28 → ~7,491) and never once asked who
was still holding the old one. On the eve of an FOMC, the stale copy read
~1.4% of headroom to the kill when the live figure was ~0.56%.

The check itself is one grep. The failure was that nobody ran it.

Fleet-generic on purpose — every agent publishes numbers others consume.
Same shape as scripts/orphan_check.sh (which began as a HENRY-local tool and
was adopted fleet-wide 2026-07-23).

TWO DESIGN POINTS, both from VIOLET's review of the first draft:

  1. MATCH ON NUMERIC TOKENS, NOT SUBSTRINGS. A naive grep for "7496" hits
     REGINALD/workbook/SHORT_VOL.tsv:396 — that is 174960, an OZK share
     count. We tokenize each line into number-like spans, strip separators,
     and compare whole values. No substring can survive that.

  2. DISTINGUISH "CARRIES IT" FROM "CARRIES IT FLAGGED SUPERSEDED." PROME's
     DOCKET.tsv and SCRATCH.md both held 7,496 — correctly marked stale, with
     the refreshed gap already computed. Scoring those as stale consumers
     overstates the problem in the tool-owner's favour. We look for a
     supersession marker on the hit line or within +/-CONTEXT lines.

DELIBERATE ASYMMETRY: when classification is ambiguous, we report STALE, not
FLAGGED. A false STALE costs a glance. A false FLAGGED costs exactly the
failure this tool exists to prevent.

2026-08-21 PATCH (DAEDALUS, Will-approved; defects routed by HENRY as author —
sources: WAL/REGINALD marker-drop 🔴, LABOR status-column 🟠, VIOLET NUM_RE
csv-fusion 🟠, LIQUID frozen-banner scope):
  1. PROXIMITY, NOT PRESENCE: a supersession marker clears ONLY the matched
     value(s) within MARKER_WINDOW chars of it — per-needle, so a row carrying
     a live stale value PLUS a history clause about an older one no longer
     buries the live hit under the history clause's marker. The 🟢 bucket is
     auditable via --show-handled (each hit prints WHY it was cleared, incl.
     the matched marker token).
  2. FILE-LEVEL DEAD BANNERS: a file whose banner region declares it FROZEN/
     RETIRED/SUPERSEDED/ARCHIVED (ledger_staleness.is_frozen, the fleet's
     hardened v4 recognizer — one recognizer, not two that drift) is historical
     wholesale; its hits bucket 🟢 with that reason instead of demanding
     per-cell annotation noise.
  3. CSV FIELD FUSION KILLED: in .csv files the comma is a field delimiter,
     not a thousands separator — lines are split on ',' BEFORE tokenizing, so
     '2024-11-15,4.43' can never again manufacture '154.43'. Cache-input dirs
     (*_cache/, cache/) are excluded everywhere: inputs cannot carry a claim.
  4. TOOL READS `status`: a PUBLISHED.tsv `status` column with RETIRED/
     RETRACTED on a metric's latest row makes EVERY recorded value of that
     metric a positive stale-target (what LABOR's sentinel-row convention
     simulated by hand; the sentinel still works, this subsumes it).
  5. TRANSITION SHAPE: a strict 'A → B' arrow between two different values is
     the RECORD of a supersession — cleared per-needle regardless of whether B
     equals this invocation's --new (the multi-old mis-pairing hazard). The
     looser 'dated series row' shape is deliberately NOT auto-cleared: without
     equality-to-current it is indistinguishable from a stale value sitting
     beside unrelated figures, and false-HANDLED is the expensive direction.

USAGE  (fleet-adopted 2026-07-28, Will-approved — moved from AGENTS/HENRY/scripts/
        to root scripts/, the orphan_check adoption path; root CLAUDE.md
        session-end step 1c is the standing trigger)
  python3 scripts/consumer_check.py --agent HENRY --label "gamma flip" \
      --old 7496 --old 7479 --new 7491

  # from a ledger (AGENTS/<NAME>/workbook/PUBLISHED.tsv) — checks every
  # superseded value of every metric automatically:
  python3 scripts/consumer_check.py --agent HENRY --from-ledger

Exit 0 always (advisory) unless --strict, which exits 1 if any STALE consumer
is found. Read-only: never writes, never commits, never edits another agent's
files. Surfacing is the whole job; sending the packet is yours.
"""

import argparse
import os
import re
import sys
from pathlib import Path

# One banner recognizer for the whole fleet (v4, TERRY-hardened, synthetic test
# matrix lives with it) — importing beats re-implementing: two recognizers drift.
# Both scripts live in scripts/; sys.path[0] is this script's dir. Fail LOUD if
# absent — a silent "not frozen" fallback would be the PAT-106 class.
from ledger_staleness import is_frozen

# --------------------------------------------------------------- configuration

SEARCH_ROOTS = ["AGENTS", "PROME", "FORGE", "BOARD"]
SEARCH_EXTS = {".md", ".tsv", ".csv", ".txt"}

# Historical by design — a superseded value SHOULD appear here.
EXCLUDE_PARTS = {
    ".git", "processed", "archive", "_archive", "archived",
    "node_modules", ".venv", "retired", "history",
}

# A hit line (or its neighbourhood) carrying one of these is already handled.
SUPERSESSION_MARKERS = [
    "stale", "superseded", "supersede", "retired", "retire",
    "refreshed", "refresh", "retracted", "retract", "obsolete",
    "outdated", "no longer", "do not cite", "don't cite", "do not use",
    "historical", "deprecated", "corrected", "correction", "was ",
    "prior read", "prior:", "old flip", "supersedes",
]

CONTEXT = 2  # lines either side of a hit to scan for a marker

# A marker excuses a matched value only within this many chars of it (2026-08-21,
# WAL/REGINALD marker-drop fix). Genuine adjacency ("7,496 (superseded 7/28)",
# "was 7,496") sits within ~40 chars; the dropped REGINALD hit had its marker in
# a history clause ~200 chars from the live value it wrongly cleared.
MARKER_WINDOW = 60

# number-like span: 1,234.56 / 7496 / 7,496 / 0.02
NUM_RE = re.compile(r"\d[\d,_]*(?:\.\d+)?")

# strict transition arrow: nothing but the arrow (± spaces) between two values
ARROW_RE = re.compile(r"\s*(?:→|⇒|->|=>)\s*$")

# File-level dead banner, PROSE form: line-initial token (only punctuation/
# emphasis/emoji may precede) + an ISO date somewhere on line 1 — the root
# Data-Hygiene canon form is 'FROZEN <date> — ...', PREPENDED. Banner FORM,
# not keyword presence (PAT-059): '# Notes on superseded values' must not match.
DEAD_LINE1_RE = re.compile(r"^[^A-Z0-9]{0,12}(?:FROZEN|RETIRED|SUPERSEDED|ARCHIVED)\b")
ISO_DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


def file_is_dead(path: Path, rowish: bool) -> bool:
    """File-level dead-surface banner (LIQUID 8/20). Row-oriented files use the
    fleet's hardened v4 recognizer (its designed scope — TSV banner regions,
    TERRY test matrix). Prose files get the STRICT line-1 form only: is_frozen's
    6-line banner region misfires on prose whose opening paragraph merely
    MENTIONS a marker word — caught by this patch's own fixture via
    --show-handled before ship, a false-HANDLED (the expensive direction)."""
    if rowish:
        return is_frozen(path)
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            first = ""
            for l in f:
                if l.strip():
                    first = l.upper()
                    break
    except OSError:
        return False
    return bool(DEAD_LINE1_RE.match(first) and ISO_DATE_RE.search(first))


def _excluded(parts) -> bool:
    """EXCLUDE_PARTS membership + cache-input dirs (VIOLET 8/20: fred_cache/ and
    kin are INPUTS — a cached pull cannot 'carry' a stale claim; scanning them
    scales false hits with retained data)."""
    for p in parts:
        q = p.lower()
        if q in EXCLUDE_PARTS or q == "cache" or q.endswith("_cache"):
            return True
    return False


def _dated_record_class(rel: str):
    """Reason string if `rel` is a HISTORY/ARCHIVE-class file, else None.

    Companion to _excluded(), which matches path COMPONENTS only. This matches the FILE
    STEM, which is where the fleet actually puts its cold halves: FLEET_MAP_HISTORY.tsv,
    STATUS_ARCHIVE_2026-08-23.md, EVOLUTION_ARCHIVE_2026-08.md, PREDICTIONS_ARCHIVE.tsv.
    Added 2026-08-23 after LABOR verified that "history" in EXCLUDE_PARTS matches the
    directory `history/` and misses every one of those filenames.
    """
    stem = rel.rsplit("/", 1)[-1].rsplit(".", 1)[0].upper()
    for tag in ("_HISTORY", "_ARCHIVE", "-HISTORY", "-ARCHIVE"):
        if tag in stem or stem.endswith(tag.lstrip("_-")):
            return f"{rel.rsplit('/', 1)[-1]} is a HISTORY/ARCHIVE-class file"
    return None


def iter_num_tokens(line: str, csv_mode: bool = False):
    """(normalized_value, start) for every numeric token on a line.

    csv_mode: the line is split on ',' FIRST — in a .csv the comma is the FIELD
    DELIMITER, not a thousands separator, and NUM_RE's [\\d,_] class otherwise
    reads straight across the boundary: '2024-11-15,4.43' captured '15,4.43',
    normalize() stripped the comma, and VIOLET's --self run was told her own dir
    carried 154.43 — a 10Y yield row, wrong by ~35x (2026-08-20)."""
    if not csv_mode:
        for m in NUM_RE.finditer(line):
            yield normalize(m.group(0)), m.start(), m.end()
        return
    off = 0
    for field in line.split(","):
        for m in NUM_RE.finditer(field):
            yield normalize(m.group(0)), off + m.start(), off + m.end()
        off += len(field) + 1

# ------- unit/specificity gating (2026-08-07, VIOLET c7d3a07b1: 9-of-9 FP) -------
# Bare-string number matching is ~100% false-positive on short figures: `10.13`
# matched OTTO's subprime loss rate, a REGINALD 10-K exhibit number and SAM options
# rows in one scan. Root canon 1c carries an interim "a 🔴 is a CANDIDATE" stopgap
# whose stated retirement trigger is THIS fix. Three mechanisms, in order:
#   1. --unit / --series context: a hit is 🔴 STALE only when the unit token sits
#      within UNIT_WINDOW chars of the matched number, or a series word is on the
#      line. Without that context the hit demotes to 🟠 CANDIDATE.
#   2. Specificity gate: a needle with ≤ MIN_SIG_DIGITS significant digits and no
#      unit/series context can never be 🔴 — always 🟠 (a 2-sig-fig figure is
#      noise-dominated in any large corpus).
#   3. Runtime collision demotion: a context-less needle whose would-be-stale hits
#      span > COLLISION_FILE_CAP distinct files demotes to 🟠 with the measured
#      count — the tool base-rates its own needle instead of trusting it
#      ([[finding_base_rate_the_instrument_before_its_event_table]] at run time).
# 🟠 CANDIDATE prints the hits but never the send-packets instruction: confirm
# same series AND unit, then re-run with --unit/--series for the 🔴 verdict.
UNIT_WINDOW = 8          # chars either side of the matched number
MIN_SIG_DIGITS = 5       # ≤4 sig digits ⇒ never 🔴 without unit/series context
# RAISED 3→5 on 2026-08-28 (PROME asked ≤3; the 5 residual 🔴 after ≤3 were ALL 4-digit
# gamma-flip levels colliding with SAM's ¥100mn MOF_FLOWS table — a bare 4-digit integer
# is a table cell somewhere; only ≥5 digits or a unit/series match certifies a series) (HENRY via PROME, wiring-sweep day): --from-ledger printed
# "🔴 69 stale consumer reference(s). Send each owner a packet" with ZERO real — 64/69 sat
# on bare ≤3-sig-fig values; root canon 1c says "send nothing on a bare 2-sig-fig figure"
# and the tool's imperative was instructing the packet storm canon forbids (~49 spurious
# packets to ~8 desks). A 3-sig-fig bare number is noise-dominated in this corpus too.
# SIGNED NEEDLES (same fix): NUM_RE carries no sign, so a superseded NEGATIVE value
# ("-3.6") fell through to the TEXT-needle branch — "exact by construction", exempt from
# every numeric-noise gate — which is exactly why 49 hits on "-3.6" (Mexican remittances,
# FL home prices, GD -3.6%…) went 🔴 while "7465" and "38.1" were correctly demoted.
SIGN_RE = re.compile(r"^[-−+]\s*")


def numeric_needle(n: str):
    """'-3.6' -> '3.6' (numeric, sign stripped for matching — the haystack tokenizer is
    unsigned); '7,496' -> '7496'; a non-number -> None. A sign is not text."""
    t = SIGN_RE.sub("", str(n).strip())
    return normalize(t) if NUM_RE.fullmatch(t) else None
COLLISION_FILE_CAP = 4   # context-less needle in >4 distinct files ⇒ 🟠


def sig_digits(tok: str) -> int:
    """Significant digits of a numeric token: digits minus leading zeros.
    '10.13'->4  '8.37'->3  '37'->2  '0.5'->1  '207500'->6 (trailing zeros kept:
    they narrow the match space in a corpus grep even if not 'significant')."""
    digits = re.sub(r"\D", "", tok)
    return len(digits.lstrip("0"))


def context_ok(line: str, hit_values: set, units, series, csv_mode=False) -> bool:
    """True if the line carries the declared unit adjacent to a matched number,
    or a declared series word anywhere on the line."""
    low = line.lower()
    if series and any(s.lower() in low for s in series):
        return True
    if units:
        for val, start, end in iter_num_tokens(line, csv_mode):
            if val not in hit_values:
                continue
            hood = (line[max(0, start - UNIT_WINDOW):start]
                    + line[end:end + UNIT_WINDOW]).lower()
            if any(u.lower() in hood for u in units):
                return True
    return False


def normalize(tok: str) -> str:
    """'7,496' -> '7496'; '7496.0' -> '7496'. Used on BOTH needle and haystack."""
    t = tok.replace(",", "").replace("_", "")
    if "." in t:
        t = t.rstrip("0").rstrip(".")
    return t


def line_values(line: str, csv_mode: bool = False):
    """Every whole numeric value on a line, normalized. Substrings cannot match."""
    return {v for v, _s, _e in iter_num_tokens(line, csv_mode)}


def _context(lines, idx, row_oriented=False):
    """Neighbourhood of a hit — but ROW-ORIENTED FILES GET NO NEIGHBOURHOOD.

    ⚠️ Caught by testing this tool against the very case it was built for.
    In a .tsv each line is an INDEPENDENT RECORD. WALTER/REGISTRY.tsv:16 carries
    the superseded flip; the rows above and below are other agents' entries whose
    notes columns happen to contain words like "refresh" and "corrected". With a
    +/-2 window those markers bled across record boundaries and the genuinely
    stale row was scored 🟢 HANDLED — a FALSE NEGATIVE, i.e. precisely the
    expensive direction this tool's asymmetry is supposed to forbid.

    A marker only clears a row if it is IN that row. Same lesson as
    [[finding_reconcile_match_on_key_not_substring]]: match on the record, not
    on text that merely sits near it.
    """
    if row_oriented:
        return [lines[idx]]
    lo = max(0, idx - CONTEXT)
    hi = min(len(lines), idx + CONTEXT + 1)
    return lines[lo:hi]


def is_row_oriented(relpath: str) -> bool:
    return Path(relpath).suffix.lower() in {".tsv", ".csv"}


def is_blob(line: str) -> bool:
    """Embedded base64/data-URI payloads are not prose; their digits are noise.

    ⚠️ Do NOT gate this on LINE LENGTH. The first cut used len>400 and silently
    dropped WALTER/REGISTRY.tsv:16 (591 chars) — a legitimate registry row, and
    the single genuine stale consumer this tool was written to find. Ledger and
    registry rows are routinely that long.

    The real discriminator is an UNBROKEN TOKEN: a base64 payload is one
    enormous run with no whitespace (46,386 chars in the case at hand), while a
    591-char TSV row is a dozen short tab-separated fields. Measure the token,
    not the line.
    """
    if "base64" in line or "data:image" in line:
        return True
    return any(len(tok) > 200 for tok in line.split())


def marker_cleared(lines, idx, hits, row_oriented=False, csv_mode=False) -> dict:
    """PROXIMITY, NOT PRESENCE (2026-08-21 — the WAL/REGINALD marker-drop fix).

    Returns {matched_needle: marker_token} for ONLY those hits sitting within
    MARKER_WINDOW chars of a supersession marker in the joined context. The old
    has_marker() returned one bool for the whole line if ANY marker appeared
    ANYWHERE in the blob — so a row documenting its own history ('73.92 live …
    (prior 68.93 superseded)') had its LIVE stale value silently buried by the
    history clause's marker, and the more diligently a desk recorded what it
    superseded, the likelier its stale carry was dropped. Per-needle verdicts:
    on that row 68.93 clears (marker adjacent) while 73.92 stays reportable."""
    ctx = _context(lines, idx, row_oriented)
    joined = "\n".join(ctx)
    low = joined.lower()
    mpos = []  # (char_pos, marker_token)
    for mk in SUPERSESSION_MARKERS:
        start = 0
        while True:
            p = low.find(mk, start)
            if p < 0:
                break
            mpos.append((p, mk))
            start = p + 1
    if not mpos:
        return {}
    # offset of the hit line inside the joined blob
    off = 0
    if not row_oriented:
        lo = max(0, idx - CONTEXT)
        off = sum(len(l) + 1 for l in lines[lo:idx])
    hit_line = lines[idx]
    cleared = {}
    for v, s, _e in iter_num_tokens(hit_line, csv_mode):
        if v in hits and v not in cleared:
            near = [mk for p, mk in mpos if abs((off + s) - p) <= MARKER_WINDOW]
            if near:
                cleared[v] = near[0]
    for h in hits:  # text needles (mirror-map dead tokens): same proximity rule
        if h in cleared or NUM_RE.fullmatch(str(h).strip()):
            continue
        s = hit_line.lower().find(str(h).lower())
        if s >= 0:
            near = [mk for p, mk in mpos if abs((off + s) - p) <= MARKER_WINDOW]
            if near:
                cleared[h] = near[0]
    return cleared


def arrow_cleared(line, hits, csv_mode=False) -> set:
    """Needles inside a strict 'A → B' transition (B ≠ A): the RECORD of a
    supersession, cleared regardless of whether B equals this invocation's
    --new — which it won't be under the multi-old mis-pairing VIOLET hit
    (2026-08-20). Strict = NOTHING but the arrow between the two values;
    '7496 → page 32' does not clear (false-HANDLED is the expensive side)."""
    toks = list(iter_num_tokens(line, csv_mode))
    cleared = set()
    for i in range(len(toks) - 1):
        v1, _s1, e1 = toks[i]
        v2, s2, _e2 = toks[i + 1]
        if v1 == v2:
            continue
        if ARROW_RE.fullmatch(line[e1:s2]):
            if v1 in hits:
                cleared.add(v1)
            if v2 in hits:
                cleared.add(v2)
    return cleared


def has_current(lines, idx, current, row_oriented=False, csv_mode=False) -> bool:
    """Is the CURRENT value sitting right next to the old one?

    This turned out to be a far better discriminator than keyword markers.
    A line like

        | (iii) line | SPX close > ~7,496 | ⚠️ warn 7,455 · 🔴 falsified 7,491 |

    is a RE-BASE TABLE — the superseded value appears precisely because it is
    being mapped to the new one. Scoring that as a stale consumer buries the
    genuinely stale rows underneath the paperwork of fixing them. (First run of
    this tool returned 19 hits, most of them exactly this shape.)
    """
    if current in (None, "?", ""):
        return False
    want = normalize(str(current))
    return any(want in line_values(l, csv_mode)
               for l in _context(lines, idx, row_oriented))


def surface_of(relpath: str) -> str:
    """Live state vs point-in-time mail. Both matter; only one needs a packet."""
    parts = {p.lower() for p in Path(relpath).parts}
    if parts & {"inbox", "outbox"}:
        return "MAIL"
    return "LIVE"


def iter_files(workspace: Path, own_dir: Path | None, restrict: set | None = None):
    if restrict is not None:
        # --mirror-map mode: scan exactly the enumerated set (self-INCLUSIVE —
        # the 7/28 PORTFOLIO miss was the publisher checking consumers, not itself)
        for path in sorted(restrict):
            if path.is_file():
                yield path
        return
    for root in SEARCH_ROOTS:
        base = workspace / root
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in SEARCH_EXTS:
                continue
            if _excluded(path.parts):
                continue
            if own_dir and own_dir in path.parents:
                continue
            yield path


# --------------------------------------------------------- mirror-map mode (T1-b)

MIRROR_MAP_DOC = "PROME/SYSTEM.md"
MIRROR_MAP_HEADING = "### Canonical → Mirrors map"
PATH_IN_BACKTICKS = re.compile(r"`([^`]+?\.(?:md|tsv|csv|py|txt))`")


def mirror_map_files(workspace: Path) -> set:
    """Parse the Mirror Map TABLE out of PROME/SYSTEM.md at runtime + add PROME's
    own live surfaces. DESIGN CONSTRAINT (Will-approved 2026-07-28, DAEDALUS T1-b
    amendment): this tool must NOT carry its own copy of the mirror list — a list
    inside the script would be one more mirror that rots. The Mirror Map table is
    the single source; if it moves or the heading changes, fail LOUD below rather
    than silently scanning nothing."""
    doc = workspace / MIRROR_MAP_DOC
    text = doc.read_text(errors="ignore")
    if MIRROR_MAP_HEADING not in text:
        raise SystemExit(f"  ✗ mirror-map: heading {MIRROR_MAP_HEADING!r} not found in "
                         f"{MIRROR_MAP_DOC} — the table moved; fix the tool's anchor, "
                         f"do not fall back to a hardcoded list.")
    section = text.split(MIRROR_MAP_HEADING, 1)[1]
    # table ends at the next heading or ruler
    for stop in ("\n## ", "\n---"):
        if stop in section:
            section = section.split(stop, 1)[0]
    files = set()
    for m in PATH_IN_BACKTICKS.finditer(section):
        rel = m.group(1).strip()
        p = (workspace / rel)
        if p.is_file():
            files.add(p)
    # self-inclusive: PROME's own live surfaces + the root docs PROME stewards
    prome = workspace / "PROME"
    for p in prome.rglob("*"):
        if (p.is_file() and p.suffix.lower() in SEARCH_EXTS
                and not _excluded(p.parts)):
            files.add(p)
    for rel in ("CLAUDE.md", "HEARTBEAT.md", "AGENTS.md"):
        p = workspace / rel
        if p.is_file():
            files.add(p)
    if len(files) < 10:
        raise SystemExit("  ✗ mirror-map: parsed <10 files — the table parse is "
                         "broken; fix the anchor rather than trusting a near-empty scan.")
    return files


def scan(workspace: Path, needles, own_dir: Path | None, current=None,
         restrict: set | None = None, units=None, series=None):
    """-> (stale_live, candidate, mail, handled). Classification order matters.

    Needles that are purely numeric use whole-value token matching (the VIOLET
    substring lesson). Non-numeric needles (mirror-map mode: retired path
    pairings, renamed sections, dead tokens like 'FORGE/PORTFOLIO.md') match as
    literal substrings — canon changes are textual at least as often as numeric;
    text needles are exempt from all three numeric-noise gates.

    🟠 CANDIDATE (2026-08-07) = a live-surface hit the tool cannot certify as the
    same series: no unit/series context on the line, a ≤4-sig-digit needle (≤2 until
    2026-08-28; signed needles are numeric, not text), or a
    context-less needle spanning >COLLISION_FILE_CAP files. Printed, never
    packet-instructed."""
    stale, cand, mail, handled = [], [], [], []
    units = units or []
    series = series or []
    num_wanted = {numeric_needle(n) for n in needles if numeric_needle(n) is not None}
    txt_wanted = {str(n) for n in needles if numeric_needle(n) is None}
    weak_nums = {n for n in num_wanted if sig_digits(n) < MIN_SIG_DIGITS}
    have_ctx = bool(units or series)
    for path in iter_files(workspace, own_dir, restrict):
        try:
            text = path.read_text(errors="ignore")
        except OSError:
            continue
        if not (any(n in text.replace(",", "") for n in num_wanted)
                or any(n in text for n in txt_wanted)):
            continue  # cheap prefilter before the per-line pass
        lines = text.split("\n")
        rel = str(path.relative_to(workspace))
        rowish = is_row_oriented(rel)
        csvish = Path(rel).suffix.lower() == ".csv"
        # File-level dead banner (LIQUID 8/20): a FROZEN/RETIRED/SUPERSEDED/
        # ARCHIVED banner declares the WHOLE file historical — every hit inside
        # buckets 🟢, or the proximity fix below pushes desks toward per-cell
        # annotation noise just to silence known-frozen files.
        file_frozen = file_is_dead(path, rowish)
        for i, line in enumerate(lines):
            if is_blob(line):
                continue
            num_hits = num_wanted & line_values(line, csvish)
            txt_hits = {n for n in txt_wanted if n in line}
            hits = num_hits | txt_hits
            if not hits:
                continue
            txt140 = line.strip()[:140]
            if file_frozen:
                handled.append((rel, i + 1, sorted(hits), txt140,
                                "file-level dead-surface banner (FROZEN class)"))
                continue
            # 1. the new value is right here -> this IS the re-base, not a stale copy
            if has_current(lines, i, current, rowish, csvish):
                handled.append((rel, i + 1, sorted(hits), txt140,
                                f"current value {current} adjacent (re-base record)"))
                continue
            # 2. PER-NEEDLE clearing (2026-08-21): a marker or a strict A→B arrow
            #    clears only the value(s) it sits next to — the rest of the line's
            #    hits stay reportable (the WAL/REGINALD marker-drop fix).
            mk = marker_cleared(lines, i, hits, rowish, csvish)
            ar = arrow_cleared(line, hits, csvish) - set(mk)
            if mk:
                handled.append((rel, i + 1, sorted(mk), txt140,
                                "marker '" + "', '".join(sorted(set(mk.values())))
                                + f"' within {MARKER_WINDOW} chars"))
            if ar:
                handled.append((rel, i + 1, sorted(ar), txt140,
                                "inside a strict A → B transition record"))
            hits = hits - set(mk) - ar
            num_hits = num_hits & hits
            txt_hits = txt_hits & hits
            if not hits:
                continue
            rec = (rel, i + 1, sorted(hits), txt140)
            # 3. sent/received mail is point-in-time; correcting it helps nobody
            if surface_of(rel) == "MAIL":
                mail.append(rec)
            # 4. live surface, unqualified — certify the series before crying stale
            elif txt_hits:
                stale.append(rec)          # text needles: exact by construction
            elif have_ctx:
                if context_ok(line, num_hits, units, series, csvish):
                    stale.append(rec)
                else:
                    cand.append(rec + ("no unit/series context on line",))
            elif num_hits <= weak_nums:
                cand.append(rec + (f"needle <{MIN_SIG_DIGITS} sig digits",))
            else:
                stale.append(rec)          # provisional; collision pass below
    # Runtime collision demotion (context-less numeric needles only)
    if not have_ctx and stale:
        files_by_needle = {}
        for rel, _ln, hits, _txt in stale:
            for h in hits:
                if h in num_wanted:
                    files_by_needle.setdefault(h, set()).add(rel)
        noisy = {n for n, fs in files_by_needle.items() if len(fs) > COLLISION_FILE_CAP}
        if noisy:
            kept = []
            for rec in stale:
                rel, ln, hits, txt = rec
                nh = set(hits) & num_wanted
                if nh and nh <= noisy:
                    cand.append(rec + (
                        f"noise-dominated: needle in {len(files_by_needle[sorted(nh)[0]])} files"
                        " — mass propagation or collision; re-run with --unit/--series",))
                else:
                    kept.append(rec)
            stale = kept

    # ── PATH-CLASS DEMOTION (2026-08-23) — a DATED RECORD is not a STALE CLAIM.
    #
    # Measured by LABOR 8/23: a live run returned 5 hits, 1 real. The other four were
    # correctly-dated historical records (a *_HISTORY register row, a dated preprint, a
    # RESOLVED DOCKET row) that are *supposed* to hold the superseded value — that is what
    # makes them records. The tool cannot tell "this claim is stale" from "this is the
    # written history of the claim", and every 🔴 it raises on one costs a real read.
    #
    # ⚠️ TWO THINGS THIS FIX HAD TO GET RIGHT, BOTH FROM LABOR'S VERIFIED CORRECTION OF MY
    # OWN WRONG FIRST GUESS (I had assumed the gap was in the cross-agent code path):
    #  (1) NOT SCOPED TO NUMERIC. The demotion paths that already exist (have_ctx, weak_nums,
    #      collision) are all numeric-only, and `elif txt_hits` appends to stale BEFORE any of
    #      them can be reached, so a TEXT needle ("32/75", "3.4->3.1%") is structurally immune
    #      to every one of them. For text needles this is the ONLY demotion that can ever fire.
    #      ⛔ So this runs as a post-pass over ALL of `stale`, after the numeric collision pass.
    #  (2) MATCH THE FILE STEM, NOT ONLY PATH COMPONENTS. EXCLUDE_PARTS already contains
    #      "history" and `_excluded()` matches components, so `AGENTS/X/history/old.md` is
    #      excluded while `AGENTS/DAEDALUS/FLEET_MAP_HISTORY.tsv` is NOT — LABOR verified both.
    #      The 41 rotated Gaps rows written to that exact file on 2026-08-23 would all have
    #      landed as 🔴 under the old rule.
    #
    # DEMOTE, NEVER SUPPRESS (PAT-118: widening a recognizer turns a visible false-flag into an
    # invisible false-pass). These stay in the output as 🟠 CANDIDATE with the reason printed,
    # so a genuinely stale line living in an archive is still visible to a reader who looks.
    if stale:
        kept = []
        for rec in stale:
            rel = rec[0]
            why = _dated_record_class(rel)
            if why:
                cand.append(rec + (f"{why} — a dated RECORD is expected to hold superseded "
                                   f"values; verify before treating as stale",))
            else:
                kept.append(rec)
        stale = kept
    return stale, cand, mail, handled


def read_ledger(ledger: Path):
    """PUBLISHED.tsv -> {metric: (current_value, [superseded values])}.

    Schema: header-aware — needs columns metric/value/asof by name (positional
    0/1/2 fallback for headerless variants); `suppress_until` honoured if present.
    `asof` is a DATE or ISO TIMESTAMP (2026-07-31 or 2026-07-31T14:05) — ISO
    strings sort correctly as text, and a timestamp sorts after its bare date.

    SAME-DAY SUPERSESSION FIX (2026-08-07 — LABOR 7/31b via HENRY/PROME): the old
    sort was (asof, value), so two rows with one asof tie-broke on the VALUE
    string and the check could resolve 'current' to the EARLIER append — silently
    inverting a same-day supersession. Tie-break is now (asof, file_line_order):
    append order is authoritative within a day. Duplicate (metric, asof) pairs
    get a ⚠️ so the tie-break is visible, never silent."""
    if not ledger.exists():
        return {}
    raw = [l for l in ledger.read_text().strip().split("\n") if l.strip()]
    if not raw:
        return {}
    header = [h.strip().lower() for h in raw[0].split("\t")]
    def col(name, default):
        return header.index(name) if name in header else default
    c_metric, c_value, c_asof = col("metric", 0), col("value", 1), col("asof", 2)
    c_supp = header.index("suppress_until") if "suppress_until" in header else None
    c_status = header.index("status") if "status" in header else None
    today = __import__("datetime").date.today().isoformat()
    by_metric, seen_pairs = {}, set()
    for idx, l in enumerate(raw[1:]):
        r = l.split("\t")
        if len(r) <= max(c_metric, c_value, c_asof):
            continue
        metric, value, asof = r[c_metric], r[c_value], r[c_asof]
        if (metric, asof) in seen_pairs:
            print(f"  ⚠️  duplicate (metric, asof) in {ledger.name}: {metric} @ {asof} — "
                  f"append order used as the tie-break; give the later row a timestamp asof to disambiguate.")
        seen_pairs.add((metric, asof))
        supp = r[c_supp].strip() if (c_supp is not None and len(r) > c_supp) else ""
        status = (r[c_status].strip().upper()
                  if (c_status is not None and len(r) > c_status) else "")
        by_metric.setdefault(metric, []).append((asof, idx, value, supp, status))
    out = {}
    for metric, entries in by_metric.items():
        entries.sort(key=lambda e: (e[0], e[1]))    # (asof, file_line_order)
        current, supp, status = entries[-1][2], entries[-1][3], entries[-1][4]
        if supp and supp > today:
            print(f"  ⏸  {metric}: suppress_until {supp} on the current row — skipped this run.")
            continue
        # TOOL READS `status` (2026-08-21, LABOR defect-2 mechanism decision,
        # Will-approved): RETIRED/RETRACTED on the metric's LATEST row means the
        # publisher holds NO live value — EVERY recorded value becomes a positive
        # stale-target, exactly what LABOR's terminal-sentinel-row convention
        # simulated by hand. The sentinel still works; this subsumes it.
        if status in {"RETIRED", "RETRACTED"}:
            print(f"  ⛔ {metric}: status {status} on the latest row — no live value; "
                  f"every recorded value is a stale-target (carriers get flagged).")
            # numeric values only: carriers carry the FIGURE; a text sentinel
            # (RETIRED-LABOR-HOLDS-NO-COPY) is a convention artifact and flagging
            # docs that quote the convention is alert fatigue, not detection.
            targets = [v for _, _, v, _, _ in entries if NUM_RE.fullmatch(v.strip())]
            seen, keep = set(), []
            for v in reversed(targets):
                if normalize(v) not in seen:
                    seen.add(normalize(v))
                    keep.append(v)
            if len(keep) > 5:
                print(f"  ◦ {metric}: scanning the 5 most recent values; "
                      f"{len(keep) - 5} older value(s) NOT scanned (pass them via --old to include).")
            out[metric] = (status, keep[:5])
            continue
        superseded = [v for _, _, v, _, _ in entries[:-1] if normalize(v) != normalize(current)]
        # de-dup, keep the most recent few — old values stop being cited
        seen, keep = set(), []
        for v in reversed(superseded):
            if normalize(v) not in seen:
                seen.add(normalize(v))
                keep.append(v)
        if len(keep) > 5:
            # Scan-scope cap must announce itself (PROME 8/8 silent-display-cap
            # sweep): a reader told "superseded A, B, C, D, E" believes that is
            # the whole set; the dropped tail was never scanned at all.
            print(f"  ◦ {metric}: scanning the 5 most recent superseded values; "
                  f"{len(keep) - 5} older value(s) NOT scanned (pass them via --old to include).")
        out[metric] = (current, keep[:5])
    return out


def report(label, current, olds, stale, cand, mail, handled, show_handled=False):
    print(f"\n  ── {label} · superseded {', '.join(map(str, olds))} → current {current}")
    if stale:
        print(f"     🔴 STALE ON A LIVE SURFACE — send the owner a packet ({len(stale)})")
        for p, ln, hits, txt in stale:
            print(f"        {p}:{ln}  [{', '.join(hits)}]")
            print(f"           {txt}")
    if cand:
        print(f"     🟠 CANDIDATE — series NOT certified; confirm same series AND unit, "
              f"then re-run with --unit/--series. NO packet on a 🟠. ({len(cand)})")
        for p, ln, hits, txt, why in cand:
            print(f"        {p}:{ln}  [{', '.join(hits)}]  ({why})")
            print(f"           {txt}")
    if mail:
        owners = sorted({p.split('/')[1] for p, *_ in mail if '/' in p})
        print(f"     🟡 in MAIL, point-in-time — usually no action ({len(mail)}"
              f"{': ' + ', '.join(owners) if owners else ''})")
    if handled:
        # The 🟢 bucket is where the marker-drop class hid for 3+ weeks — it must
        # be auditable (HENRY option 1, 2026-08-21). Default stays count-only;
        # --show-handled prints each hit with WHY it was cleared.
        print(f"     🟢 cleared: marker-adjacent / next to new value / frozen file "
              f"({len(handled)})" + ("" if show_handled else "  [--show-handled to audit]"))
        if show_handled:
            for p, ln, hits, txt, why in handled:
                print(f"        {p}:{ln}  [{', '.join(hits)}]  ({why})")
                print(f"           {txt}")
    if not (stale or cand or mail or handled):
        print("     ✓ no consumer carries a superseded value.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--agent", help="your agent name — excludes AGENTS/<NAME>/ from the scan")
    ap.add_argument("--label", default="value", help="what the number is, for the report")
    ap.add_argument("--old", action="append", default=[], help="superseded value (repeatable)")
    ap.add_argument("--new", default="?", help="the current value")
    ap.add_argument("--from-ledger", metavar="PATH", nargs="?", const="AUTO",
                    help="read metrics from a PUBLISHED.tsv instead of --old/--new")
    ap.add_argument("--mirror-map", action="store_true",
                    help="T1-b mirror walk (2026-07-28): scan ONLY the files enumerated "
                         "in PROME/SYSTEM.md's Canonical→Mirrors table (parsed at "
                         "runtime) + PROME's own surfaces, self-INCLUSIVE (no --agent "
                         "exclusion). Non-numeric --old values match as literal text. "
                         "Run on any canon/threshold change with the OLD token.")
    ap.add_argument("--self", dest="self_mode", action="store_true",
                    help="INVERT the scan: check ONLY your own AGENTS/<NAME>/ for figures "
                         "you superseded this session (needs --agent). Same grep, opposite "
                         "scope — the cross-agent mode above cannot see intra-agent "
                         "propagation, which was ~25 of the defects in PROME's 7/31 audit. "
                         "Deliberately NOT age-gated: a freshly-stamped file carrying a "
                         "stale claim is the case a staleness enforcer passes. "
                         "⚠️ NEEDLE QUALITY MATTERS MORE HERE than in cross-agent mode: "
                         "your own dir is dense with line refs, scores and version "
                         "strings, so a 2-digit --old ('37') is noise-dominated — it "
                         "matched 'market-agent.md:37', a '37/75' composite and a "
                         "FLEET_MAP line number on the first live run. Use a distinctive "
                         "figure (3+ significant digits) or a text token.")
    ap.add_argument("--unit", action="append", default=[],
                    help="unit token that must sit adjacent to the matched number "
                         "(repeatable: %%, bp, $, x, ×, contracts …). With --unit/--series, "
                         "context-confirmed hits are 🔴 and the rest 🟠 CANDIDATE.")
    ap.add_argument("--series", action="append", default=[],
                    help="series word that must appear on the hit line (repeatable: "
                         "'CCC', 'OAS', 'gamma' …). Alternative context to --unit.")
    ap.add_argument("--show-handled", action="store_true",
                    help="print every 🟢-cleared hit with WHY it was cleared (matched "
                         "marker token / adjacent current / frozen banner / A→B arrow). "
                         "The 🟢 bucket is where the 2026-08 marker-drop class hid; "
                         "audit it when a value you KNOW is carried comes back clean.")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any STALE consumer found")
    args = ap.parse_args()
    if len(args.old) > 1:
        # Advisory, NEVER a block (PROME scoping 38ad4495d): repeated --old is
        # CORRECT for prior vintages of the SAME figure collapsing to one --new
        # (a re-base chain); the tool cannot distinguish that from the error by
        # count alone. Keep wording in sync with root CLAUDE.md step 1c.
        print("  ℹ️  multiple --old against one --new: correct ONLY if all are prior "
              "vintages of the SAME figure. To check several DIFFERENT metrics, run "
              "separate invocations or --from-ledger (which pairs each metric's own "
              "old→current) — mis-pairing manufactures false 🔴s (VIOLET 8/20, 3-of-3).")
    if args.self_mode and args.mirror_map:
        ap.error("--self and --mirror-map are opposite scopes; run them separately")
    if args.self_mode and not args.agent:
        ap.error("--self needs --agent (it scans AGENTS/<NAME>/ and nothing else)")

    here = Path(__file__).resolve()
    workspace = here.parents[1]                       # scripts/ -> repo root (was parents[3] at AGENTS/<X>/scripts/ pre-adoption; git mv 2026-07-28)
    own_dir = (workspace / "AGENTS" / args.agent) if args.agent else None
    if own_dir and not own_dir.exists():
        print(f"  ⚠️  --agent {args.agent}: {own_dir} not found; scanning everything.")
        own_dir = None

    print(f"\n{'='*66}\n  CONSUMER CHECK  ·  who still carries a number you superseded?\n{'='*66}")
    if own_dir and not args.self_mode:
        # Suppressed in self mode: printing "own dir excluded" directly above
        # "SELF mode: scanning only your own dir" states both halves of a
        # contradiction and lets the reader pick. STRICT_TEXT rule 9.
        print(f"  own dir excluded: AGENTS/{args.agent}/   "
              f"(processed/ + archive/ excluded everywhere — historical by design)")

    jobs = []
    if args.from_ledger:
        # AUTO derives the ledger from --agent now that the script lives at root
        # scripts/ (pre-adoption it lived at AGENTS/<X>/scripts/ and used its own
        # parent dir; that path silently pointed at repo-root/workbook post-move).
        if args.from_ledger == "AUTO":
            if not args.agent:
                ap.error("--from-ledger AUTO needs --agent to locate AGENTS/<NAME>/workbook/PUBLISHED.tsv")
            led = workspace / "AGENTS" / args.agent / "workbook" / "PUBLISHED.tsv"
        else:
            led = Path(args.from_ledger)
        ledger = read_ledger(led)
        if not ledger:
            print(f"  ⚠️  no ledger rows at {led}")
            return 0
        for metric, (current, olds) in ledger.items():
            if olds:
                jobs.append((metric, current, olds))
        if not jobs:
            print("  ✓ ledger has no superseded values to check.")
            return 0
    else:
        if not args.old:
            ap.error("need --old (repeatable) or --from-ledger")
        jobs.append((args.label, args.new, args.old))

    restrict = None
    if args.self_mode:
        # Reuse the existing restrict path — no new walker. Apply the SAME ext and
        # EXCLUDE_PARTS filters the cross-agent walk uses, so processed/ and archive/
        # stay excluded here too (a superseded value SHOULD survive in those).
        # Scope deliberately covers the WHOLE agent dir, not STATUS/THESIS only:
        # MARCO's own follow-up sweep found 3 more carriers past the audit's list,
        # one of them a KB ledger, and its SCRATCH + KB were exactly what a
        # narrative-only sweep missed (PROME addendum, 2026-07-31).
        restrict = {p for p in own_dir.rglob("*")
                    if p.is_file() and p.suffix.lower() in SEARCH_EXTS
                    and not _excluded(p.parts)}
        own_dir = None                      # self-INCLUSIVE: never exclude the caller
        print(f"  SELF mode: {len(restrict)} files under AGENTS/{args.agent}/ "
              f"(processed/ + archive/ still excluded — historical by design). "
              f"Nothing outside your own dir is scanned.")
    if args.mirror_map:
        restrict = mirror_map_files(workspace)
        own_dir = None  # self-INCLUSIVE by definition — never exclude the caller
        print(f"  mirror-map mode: {len(restrict)} files (SYSTEM.md table, parsed at "
              f"runtime, + PROME surfaces + stewarded root docs; self-inclusive)")

    total_stale, total_cand = 0, 0
    for label, current, olds in jobs:
        stale, cand, mail, handled = scan(workspace, olds, own_dir, current, restrict,
                                          units=args.unit, series=args.series)
        report(label, current, olds, stale, cand, mail, handled,
               show_handled=args.show_handled)
        total_stale += len(stale)
        total_cand += len(cand)

    print()
    if total_cand and not total_stale:
        print(f"  🟠 {total_cand} CANDIDATE(s), zero certified-stale. A 🟠 is a prompt to "
              f"LOOK, never a packet: confirm same series AND unit at the hit, then "
              f"re-run with --unit/--series for the 🔴 verdict.")
    if total_stale and args.self_mode:
        # The instruction INVERTS in self mode: you are the owner, so a packet to
        # yourself is not the fix — editing the surface is. Saying "send the owner a
        # packet" here would be advice to do nothing.
        print(f"  🔴 {total_stale} stale reference(s) on YOUR OWN surfaces. You are the "
              f"owner: fix them in place this session — no packet, nobody else to tell. "
              f"Fix by PATTERN, not by the line list above (a line-targeted sweep left a "
              f"hit on the highest-blast-radius surface three times in one night).")
    elif total_stale:
        print(f"  🔴 {total_stale} stale consumer reference(s). Send each owner a packet "
              f"with the refreshed value — do NOT edit their files.")
    elif total_cand:
        pass  # the 🟠 footer above is the verdict — never print "clean" beside it
    elif args.self_mode:
        print(f"  ✓ clean — no surface under AGENTS/{args.agent}/ carries the superseded "
              f"value unqualified. (Scanned the whole dir, not just STATUS/THESIS.)")
    else:
        print("  ✓ clean — every consumer is current or has it flagged superseded.")
    print(f"{'='*66}\n")
    return 1 if (args.strict and total_stale) else 0


if __name__ == "__main__":
    sys.exit(main())
