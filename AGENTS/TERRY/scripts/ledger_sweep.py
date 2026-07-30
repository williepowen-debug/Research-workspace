#!/usr/bin/env python3
"""
TERRY ledger sweep — catches the two drift classes that bit this desk 5x on 2026-07-30.

WHY THIS EXISTS
---------------
Every correction pass this desk runs updates the NARRATIVE surfaces (STATUS banners,
the card body, POSTMORTEMS, MEMORY) and forgets the LEDGERS (SETUPS.tsv, PAPER_BOOK.tsv,
setups/INDEX.md, TRADE_BOOK.md). That is `finding_ledger_drift_behind_narrative` and
`finding_state_token_sweep_all_surfaces`, and it recurred FIVE times in a single session:

  1. SIGNALS.tsv carried a 5/15 vintage for 7 days while the banner said "decay discharged"
  2. diesel verdict moved to NO AT THIS PRICE on the card; 3 ledgers still said CONDITIONAL
  3. VIXCS corrections (18.71 / 1.0888 / beta 0.28 / n=2) never reached SETUPS.tsv row 8,
     PAPER_BOOK.tsv PB-0003, or the STATUS BOTTOM LINE
  4. TRY-FIRE-001 carried "HY OAS 269, moved AWAY" for 9 days while the gate was crossing
  5. found BY THIS SCRIPT while building it: the diesel card's own HEADER verdict still
     said CONDITIONAL after the ledgers had been swept to NO AT THIS PRICE

Detection was never the gap — INVOCATION was. So this runs at boot and at closeout, and it
EXITS 1 on any finding. It is a guard; a guard that fails quietly is worse than no guard
(`finding_test_the_guard_not_just_the_guarded`), hence --selftest injects synthetic defects
and asserts they are caught.

THE THREE CHECKS
----------------
C. CARD HEADER vs ITS OWN BODY — does a card's body declare a verdict its header never
   learned? Runs FIRST because it is where the drift starts, and check A is structurally
   blind to it: on 7/30 at 12:35 the header AND all three ledgers agreed on CONDITIONAL
   while the body twice declared "VERDICT: NO AT THIS PRICE". Unanimous agreement on a
   stale value is exactly what a consistency check cannot see.

A. STATE AGREEMENT — for each setup_id, does every surface claim the same state?
   Matched on the KEY (setup_id), never a substring (`finding_reconcile_match_on_key_not_substring`
   — bare-numeric matching is what gave consumer_check.py ~123 false positives on "0.28").

B. SUPERSEDED-VALUE DRIFT — values you corrected (`label ~~old~~ -> new`) in recent TERRY
   commits that are still asserted NAKED somewhere else. Derived from the git diff, so it
   needs no register and no discipline. Returns (label, value) PAIRS: matching a bare
   number is the defect itself, since "0.53" is simultaneously a withdrawn beta and a real
   25C leg fill price.

CONVENTIONS THIS ENCODES (they are load-bearing — see --explain)
  * A card's FIRST "**Terry verdict:**" is its CURRENT state. Later in-body verdict lines
    are dated history and are ignored.
  * ~~Struck text~~ is history everywhere. Stripped before any state match.
  * "(was X)" / "(previously X)" parentheticals are history. Stripped.
  * TRADE_BOOK.md is a dated ledger: only the LAST row naming a setup_id is a state claim.
  * States are matched CASE-SENSITIVELY. A lowercase "conditional" is prose, not a claim.
  * Hyphenated compounds are different nouns: GATE-CLOSED is not a CLOSED card.

NEVER silence a finding by widening COMPATIBLE — that is relaxing a guard to make it pass,
the move root rule #6's break test forbids. Either the surfaces disagree (fix them) or the
normalizer is wrong (fix it, and add the case to --selftest).

Usage:
  (cd "$(git rev-parse --show-toplevel)" && python3 AGENTS/TERRY/scripts/ledger_sweep.py)
  ... --since "3 days ago"    # widen check B's commit window (default: 2 days ago)
  ... --selftest              # synthetic bad-input injection + live run
  ... --explain               # print the conventions above and exit
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------- surfaces

TERRY = Path("AGENTS/TERRY")
SETUPS_TSV = TERRY / "SETUPS.tsv"
INDEX_MD = TERRY / "setups" / "INDEX.md"
TRADE_BOOK = TERRY / "TRADE_BOOK.md"
CARD_DIR = TERRY / "setups"

# Surfaces swept by check B. Ledgers first — they are the ones that rot.
DRIFT_SURFACES = [
    TERRY / "SETUPS.tsv",
    TERRY / "PAPER_BOOK.tsv",
    TERRY / "SIGNALS.tsv",
    TERRY / "STATUS.md",
    TERRY / "TRADE_BOOK.md",
    TERRY / "POSTMORTEMS.md",
    TERRY / "MEMORY.md",
    TERRY / "setups" / "INDEX.md",
]

# ---------------------------------------------------------------- state vocab
# ORDER MATTERS: most-terminal / most-specific first, so that a cell reading
# "NO AT THIS PRICE (was CONDITIONAL)" resolves to NO_AT_THIS_PRICE, not CONDITIONAL.
# The (?<!-) guards matter: "GATE-CLOSED/ADJUDICATION-PENDING" describes the GATE, not the
# card, and "0-fired" is a count. A hyphenated compound is a different noun — reading the
# state out of one is the substring error this whole script exists to prevent.
STATES: list[tuple[str, str]] = [
    (r"NO\s+AT\s+THIS\s+PRICE", "NO_AT_THIS_PRICE"),
    (r"(?<!-)\bCLOSED\b", "CLOSED"),
    (r"\bLAPSED\b", "LAPSED"),
    (r"\bRETIRED\b", "RETIRED"),
    (r"\bPARKED\b", "PARKED"),
    (r"\bSHELVED\b", "SHELVED"),
    (r"\bDORMANT\b", "DORMANT"),
    (r"NO[\s-]+FIRE\b", "NO_FIRE"),
    (r"(?<!-)\bFIRED\b", "FIRED"),
    (r"\bARMABLE\b", "ARMABLE"),
    (r"\bARMED\b", "ARMED"),
    (r"NO\s+TRADE\b", "NO_TRADE"),
    (r"\bCONDITIONAL\b", "CONDITIONAL"),
    (r"\bSTAGED\b", "STAGED"),
    (r"\bCLEAN\b", "CLEAN"),
]

# States that legitimately coexist across surfaces: one describes the CARD's verdict,
# the other the POSITION's lifecycle. Pairs here are not reported as disagreement.
COMPATIBLE: set[frozenset[str]] = {
    frozenset({"FIRED", "CLEAN"}),          # fired card keeps its CLEAN construction verdict
    frozenset({"CLOSED", "CLEAN"}),         # ditto once closed
    frozenset({"CLOSED", "FIRED"}),         # fired then closed
    frozenset({"STAGED", "CONDITIONAL"}),   # staged card awaiting a trigger
    frozenset({"STAGED", "NO_TRADE"}),      # template placeholder verdict on a staged card
    frozenset({"STAGED", "NO_FIRE"}),       # trigger met, TERRY declined -> card stays staged
    frozenset({"ARMABLE", "NO_TRADE"}),
    frozenset({"ARMABLE", "CONDITIONAL"}),
    frozenset({"DORMANT", "CONDITIONAL"}),
    frozenset({"RETIRED", "LAPSED"}),
}

# Correction markers: a line carrying one of these is ANNOTATING an old value, not
# asserting it. Check B ignores such lines.
CORRECTION_MARKERS = re.compile(
    r"(~~|->|→|\bCORRECT|\bWITHDRAWN\b|\bWITHDRAW\b|\bSUPERSED|\bRETIRED\b|\bTRUE\b|"
    r"\bWAS\b|\bREFUTED\b|\bSTALE\b|\bRETRACT|\bNARROWED\b|\bPENDING\b|\bERROR\b|\bWRONG\b)",
    re.IGNORECASE,
)

SETUP_ID_RE = re.compile(r"\bTRY-[A-Z0-9]+(?:-[A-Z0-9]+)*\b")


# ---------------------------------------------------------------- helpers

def strip_history(text: str) -> str:
    """Remove text that is, by convention, a dated historical record rather than a claim."""
    text = re.sub(r"~~.*?~~", " ", text, flags=re.DOTALL)          # struck = history
    # "(was X)" / "(moved from X)" / "(upgraded from X)" — the arrow-of-time idioms this
    # desk actually writes. Everything after them names a PRIOR state, never the current one.
    prior = r"was|previously|formerly|moved\s+from|upgraded\s+from|downgraded\s+from|revised\s+from|changed\s+from"
    text = re.sub(rf"\((?:{prior})\b[^)]*\)", " ", text, flags=re.IGNORECASE)
    text = re.sub(rf"\*?\(?(?:{prior})\s+[^*)\n]{{0,60}}", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"\bwas\s+[A-Z][A-Z _/-]{2,}", " ", text)        # "was CONDITIONAL"
    return text


def state_of(cell: str) -> str | None:
    """
    Normalize a prose cell to one state token, or None if it makes no state claim.

    Matched CASE-SENSITIVELY (states are written in CAPS on every surface of this desk).
    Lowercase is prose, not a claim: the VIXCS card reads "CLEAN ON TERRY'S AXIS ... the
    pricing condition that made it conditional is discharged" — that trailing adjective is
    describing history, and reading a state out of it inverts the card's actual verdict.
    """
    clean = strip_history(cell)
    for pattern, token in STATES:
        if re.search(pattern, clean):
            return token
    return None


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""


def md_cells(line: str) -> list[str]:
    parts = line.split("|")
    if len(parts) < 3:
        return []
    return [c.strip() for c in parts[1:-1]]


# ---------------------------------------------------------------- extractors
# Each takes text and returns {setup_id: state_claim_string}. Pure functions on
# strings so --selftest can drive them with synthetic content.

def cards_from_text(name: str, text: str) -> tuple[str | None, str | None]:
    """(setup_id, current verdict cell) from a card file. FIRST verdict line only."""
    m = re.search(r"\*\*Setup ID:\*\*\s*`?([A-Z0-9-]+)`?", text)
    sid = m.group(1) if m else None
    v = re.search(r"\*\*Terry verdict[^*]*:?\*\*\s*:?\s*(.+)", text)
    if not v:
        v = re.search(r"\*\*Terry verdict[^:]*:\s*(.+?)\*\*", text)
    return sid, (v.group(1).strip() if v else None)


def setups_tsv_states(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    lines = [l for l in text.split("\n") if l.strip()]
    if not lines:
        return out
    hdr = lines[0].split("\t")
    try:
        i_id, i_v, i_s = hdr.index("setup_id"), hdr.index("verdict"), hdr.index("status")
    except ValueError:
        return out
    for line in lines[1:]:
        c = line.split("\t")
        if len(c) <= max(i_id, i_v, i_s):
            continue
        out[c[i_id].strip()] = f"{c[i_v]} || {c[i_s]}"
    return out


def index_md_states(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in text.split("\n"):
        cells = md_cells(line)
        if len(cells) < 2:
            continue
        ids = SETUP_ID_RE.findall(cells[0])
        if len(ids) == 1:
            out[ids[0]] = cells[1]
    return out


def trade_book_states(text: str) -> dict[str, str]:
    """LAST row naming an id wins — earlier rows are dated history."""
    out: dict[str, str] = {}
    for line in text.split("\n"):
        cells = md_cells(line)
        if len(cells) < 6:
            continue
        ids = SETUP_ID_RE.findall(cells[1]) if len(cells) > 1 else []
        if len(set(ids)) == 1:
            out[ids[0]] = cells[5]          # Status column
    return out


# ---------------------------------------------------------------- check A

def check_state_agreement(
    card_states: dict[str, dict[str, str]],
) -> list[str]:
    findings: list[str] = []
    for sid in sorted(card_states):
        claims = card_states[sid]
        resolved = {surf: state_of(cell) for surf, cell in claims.items()}
        resolved = {s: v for s, v in resolved.items() if v}
        if len(resolved) < 2:
            continue
        distinct = set(resolved.values())
        if len(distinct) == 1:
            continue
        if distinct in COMPATIBLE or any(
            distinct <= combo for combo in COMPATIBLE
        ):
            continue
        detail = "; ".join(f"{s}={v}" for s, v in sorted(resolved.items()))
        findings.append(
            f"STATE DISAGREEMENT  {sid}\n"
            f"      {detail}\n"
            f"      -> surfaces disagree on this card's CURRENT state. "
            f"Decide which is right, sweep the others."
        )
    return findings


# ---------------------------------------------------------------- check C
# A card's body declares a verdict its own header never learned.
#
# This is where the 2026-07-30 diesel drift ACTUALLY started, and check A cannot see it:
# at that moment the header said CONDITIONAL and all three ledgers said CONDITIONAL, so
# every state field AGREED — while the card body twice declared "VERDICT: NO AT THIS PRICE".
# Unanimous agreement on a stale value is the failure mode a consistency check is blindest
# to, so it needs its own check: compare the card's LAST in-body verdict declaration to its
# header. Catch it here and check A's ledger sweep follows for free.
VERDICT_DECL_RE = re.compile(
    r"(?:\*\*)?VERDICT\s*[:—-][^.\n]{0,140}"
    r"|verdict\s+(?:moves?|moved|UNCHANGED|stays?|holds?)[^.\n]{0,140}",
    re.IGNORECASE,
)


def declared_verdict(text: str) -> tuple[str | None, str | None]:
    """(state, raw) of the LAST in-body verdict declaration, or (None, None)."""
    last: tuple[str | None, str | None] = (None, None)
    for m in VERDICT_DECL_RE.finditer(text):
        raw = m.group(0)
        # "moved CONDITIONAL -> NO AT THIS PRICE": only what follows the LAST arrow is current.
        tail = re.split(r"->|→", raw)[-1]
        st = state_of(tail)
        if st:
            last = (st, raw.strip())
    return last


def check_header_vs_body(cards: dict[str, tuple[str, str, str]]) -> list[str]:
    findings: list[str] = []
    for sid, (fname, header_cell, body) in sorted(cards.items()):
        head_state = state_of(header_cell)
        body_state, raw = declared_verdict(body)
        if not head_state or not body_state or head_state == body_state:
            continue
        if {head_state, body_state} in COMPATIBLE:
            continue
        findings.append(
            f"CARD HEADER LAGS ITS OWN BODY  {sid}  ({fname})\n"
            f"      header says {head_state}: {header_cell[:70]}\n"
            f"      body declares {body_state}: {raw[:90]}\n"
            f"      -> the card is the last surface to learn its own verdict. Update the "
            f"header, then re-run to sweep the ledgers."
        )
    return findings


# ---------------------------------------------------------------- check B

# A CORRECTED VALUE looks like `~~18.71~~ -> 19.11`, not like a struck paragraph.
# Striking a SENTENCE does not supersede every number inside it — the fill prices in
# "~~Will beat me at ($0.70 vs $0.75) and ($0.45 vs $0.40)~~" are still true facts; what
# was withdrawn was the CLAIM about them. Requiring (a) a short strike that is essentially
# just the value and (b) a replacement arrow nearby is what separates the two.
# Without both, this check reproduces consumer_check.py's ~123 bare-numeric false positives.
STRUCK_VALUE_RE = re.compile(r"(.{0,60}?)~~([^~]{1,30}?)~~(.{0,45})", re.DOTALL)
REPLACEMENT_NEARBY = re.compile(r"(->|→|\bTRUE\b|\bCORRECT|\bWITHDRAWN\b|\bSUPERSED)", re.IGNORECASE)
VALUE_RE = re.compile(r"\d+\.\d{2,}|\bn=\d+\b")
LABEL_RE = re.compile(r"([A-Za-z][A-Za-z0-9-]{2,})[^A-Za-z0-9]*$")
MARKER_WINDOW = 140

# Words that label nothing — never accept them as the key for a value.
STOPWORDS = {
    "the", "and", "was", "with", "from", "that", "this", "its", "our", "his", "her",
    "not", "but", "for", "are", "were", "has", "had", "into", "than", "then", "own",
    "corrected", "true", "wrong", "still", "only", "just", "vs", "per", "via", "at",
}


def struck_tokens_from_diff(diff: str) -> set[tuple[str, str]]:
    """
    Values newly CORRECTED by recent commits, i.e. `label ~~old~~ -> new`.

    Returns (label, value) pairs, NOT bare values. Matching a bare number across the desk
    is the defect that gave consumer_check.py ~123 false positives this morning: "0.53" is
    simultaneously a withdrawn beta AND the real 25C leg fill price, and no amount of
    context-window tuning can separate them without the KEY.
    (`finding_reconcile_match_on_key_not_substring`)

    Deliberately narrow on three axes: a SHORT strike (<=30 chars, so it wraps the value
    and not a paragraph), a replacement marker CLOSE BEHIND it, and a usable label in front.
    """
    pairs: set[tuple[str, str]] = set()
    for line in diff.split("\n"):
        if not line.startswith("+") or line.startswith("+++"):
            continue
        for preceding, inner, trailing in STRUCK_VALUE_RE.findall(line):
            if not REPLACEMENT_NEARBY.search(trailing):
                continue
            found = VALUE_RE.findall(inner)
            if not (1 <= len(found) <= 2):
                continue
            m = LABEL_RE.search(re.sub(r"[*_`~#|]", " ", preceding))
            if not m:
                continue
            label = m.group(1).lower()
            if label in STOPWORDS or VALUE_RE.fullmatch(label):
                continue
            for v in found:
                pairs.add((label, v))
    return pairs


def check_superseded_drift(pairs: set[tuple[str, str]], surfaces: dict[str, str]) -> list[str]:
    """Flag a superseded value only where its LABEL also appears — key+value, never value alone."""
    findings: list[str] = []
    for label, tok in sorted(pairs):
        naked: list[str] = []
        for path, text in surfaces.items():
            for n, line in enumerate(text.split("\n"), 1):
                start = 0
                while (i := line.find(tok, start)) != -1:
                    start = i + len(tok)
                    window = line[max(0, i - MARKER_WINDOW): i + len(tok) + MARKER_WINDOW]
                    # Must be THIS quantity (label present) and not already annotated.
                    if label in window.lower() and not CORRECTION_MARKERS.search(window):
                        naked.append(f"{path}:{n}")
                        break
        if naked:
            findings.append(
                f"SUPERSEDED VALUE STILL NAKED  {label} = {tok}\n"
                f"      corrected in a recent commit but still asserted, unannotated, at:\n"
                + "".join(f"        {loc}\n" for loc in naked[:8])
                + f"      -> annotate or correct each, or the ledger outlives the correction."
            )
    return findings


# ---------------------------------------------------------------- gather

def gather_live():
    claims: dict[str, dict[str, str]] = {}
    cards: dict[str, tuple[str, str, str]] = {}

    def add(sid: str, surface: str, cell: str) -> None:
        if sid and cell:
            claims.setdefault(sid, {})[surface] = cell

    for card in sorted(CARD_DIR.glob("*.md")):
        if card.name == "INDEX.md":
            continue
        body = read(card)
        sid, verdict = cards_from_text(card.name, body)
        if sid and verdict:
            add(sid, f"card({card.name})", verdict)
            cards[sid] = (card.name, verdict, body)

    for sid, cell in setups_tsv_states(read(SETUPS_TSV)).items():
        add(sid, "SETUPS.tsv", cell)
    for sid, cell in index_md_states(read(INDEX_MD)).items():
        add(sid, "INDEX.md", cell)
    for sid, cell in trade_book_states(read(TRADE_BOOK)).items():
        add(sid, "TRADE_BOOK.md", cell)

    return claims, cards, {str(p): read(p) for p in DRIFT_SURFACES if p.exists()}


def recent_diff(since: str) -> str:
    try:
        return subprocess.run(
            ["git", "log", f"--since={since}", "-p", "--unified=0", "--", str(TERRY)],
            capture_output=True, text=True, timeout=60, check=False,
        ).stdout
    except Exception:
        return ""


# ---------------------------------------------------------------- selftest

def selftest() -> int:
    """Inject synthetic defects and assert they are CAUGHT. Testing the guard, not the guarded."""
    print("SELFTEST — synthetic injection")
    fails = 0

    def ok(label: str, cond: bool) -> None:
        nonlocal fails
        print(f"  {'PASS' if cond else 'FAIL'}  {label}")
        if not cond:
            fails += 1

    # --- normalizer
    ok("terminal state beats trailing history",
       state_of("NO AT THIS PRICE (was CONDITIONAL 7/26)") == "NO_AT_THIS_PRICE")
    ok("struck text ignored",
       state_of("~~CONDITIONAL~~ now CLOSED") == "CLOSED")
    ok("'was CONDITIONAL' prose ignored",
       state_of("FIRED LIVE, was CONDITIONAL before the arm") == "FIRED")
    ok("★ '(moved from CONDITIONAL)' is prior state, not current",
       state_of("🟢 **CLEAN ON TERRY'S AXIS** *(moved from 🟡 CONDITIONAL — 7/27)*") == "CLEAN")
    ok("★ hyphenated compound is a different noun — GATE-CLOSED is not a CLOSED card",
       state_of("CONDITIONAL || GATE-CLOSED/ADJUDICATION-PENDING") == "CONDITIONAL")
    ok("'0-fired' count is not a FIRED state",
       state_of("STAGED — 0-fired live, $0 at risk") == "STAGED")
    ok("★ lowercase adjective is prose, not a state claim (the VIXCS card's trailing "
       "'made it conditional' must not override its CLEAN verdict)",
       state_of("🟢 **CLEAN ON TERRY'S AXIS** — the pricing condition that made it "
                "conditional is discharged; it was staged and is now filled") == "CLEAN")
    ok("no state claim -> None", state_of("thesis owner BRENT, see packet") is None)

    # --- check A catches the real 7/30 defect
    injected = {"TRY-X": {
        "card(x.md)": "🟡 **CONDITIONAL — not at Monday's price.**",
        "SETUPS.tsv": "NO AT THIS PRICE || unarmed",
        "INDEX.md": "🔴 **NO AT THIS PRICE**",
    }}
    ok("catches card-vs-ledger disagreement (the live 7/30 diesel defect)",
       len(check_state_agreement(injected)) == 1)

    ok("clean state -> silent", check_state_agreement({"TRY-Y": {
        "card(y.md)": "🔴 NO AT THIS PRICE", "SETUPS.tsv": "NO AT THIS PRICE || unarmed"}}) == [])

    ok("compatible pair not flagged", check_state_agreement({"TRY-Z": {
        "card(z.md)": "🟢 CLEAN ON TERRY'S AXIS", "INDEX.md": "🔒 CLOSED — realized -$111.60"}}) == [])

    ok("single surface -> no verdict", check_state_agreement({"TRY-W": {"card(w.md)": "CLEAN"}}) == [])

    # --- check C: the defect check A is structurally blind to
    ok("★ catches a card whose BODY declares a verdict its HEADER never learned — the "
       "exact 7/30 12:35 diesel state, where header AND all 3 ledgers agreed on the stale value",
       len(check_header_vs_body({"TRY-D": (
           "d.md",
           "\U0001f7e1 **CONDITIONAL — and specifically, NOT AT MONDAY'S PRICE.**",
           "... **VERDICT: NO AT THIS PRICE.** The thesis strengthened ...")})) == 1)
    ok("header matching body -> silent", check_header_vs_body({"TRY-E": (
        "e.md", "\U0001f534 **NO AT THIS PRICE**", "**VERDICT: NO AT THIS PRICE** unchanged")}) == [])
    ok("arrow declaration resolves to the RIGHT side",
       declared_verdict("verdict moved \U0001f7e1 CONDITIONAL -> \U0001f7e2 CLEAN today")[0] == "CLEAN")
    ok("card with no body declaration -> silent",
       check_header_vs_body({"TRY-F": ("f.md", "CONDITIONAL", "no declarations here")}) == [])

    # --- check B extraction: must catch real corrections, must NOT catch struck prose
    toks = struck_tokens_from_diff("+| VIX high ~~18.71~~ **-> 19.11** |\n+beta ~~n=2~~ WITHDRAWN\n")
    ok("extracts (label, value) pairs, not bare values", toks == {("high", "18.71"), ("beta", "n=2")})

    ok("★ struck PROSE containing true prices is NOT harvested (the consumer_check.py "
       "false-positive class this check was built to avoid)",
       struck_tokens_from_diff(
           "+~~The one thing I got beaten on: entry ($0.70 vs my $0.75) and exit "
           "($0.45 vs my $0.40 start), both filled.~~ WITHDRAWN IN FULL\n") == set())
    ok("short strike with NO replacement nearby is not a correction",
       struck_tokens_from_diff("+the old level ~~7.496~~ is gone\n") == set())
    ok("stopword is never accepted as a label",
       struck_tokens_from_diff("+it was ~~0.28~~ -> 0.53\n") == set())

    ok("catches naked superseded value where its LABEL is present",
       len(check_superseded_drift({("high", "18.71")},
           {"SETUPS.tsv": "row\tVIX cash-session high 18.71 vs the 23 line"})) == 1)
    ok("★ same number under a DIFFERENT label is NOT flagged — 0.53 is both a withdrawn "
       "beta and a real 25C leg fill price (key+value, never value alone)",
       check_superseded_drift({("beta", "0.53")},
           {"STATUS.md": "long 20C $1.23 / short 25C $0.53, filled at mark"}) == [])
    ok("annotated value is NOT flagged",
       check_superseded_drift({("high", "18.71")}, {"S.tsv": "high ~~18.71~~ -> TRUE 19.11"}) == [])
    ok("value annotated later in a long cell is NOT flagged (window, not segment)",
       check_superseded_drift({("high", "18.71")}, {
           "S.tsv": "session high 18.71 vs the >=23 line, no trigger missed -> CORRECTED to 19.11"}) == [])
    ok("value absent -> silent", check_superseded_drift({("high", "18.71")}, {"S.tsv": "nothing"}) == [])

    # --- extractors on synthetic surface text
    ok("SETUPS.tsv extractor keys on setup_id",
       setups_tsv_states("setup_id\tverdict\tstatus\nTRY-A\tCLEAN\tFIRED\n") == {"TRY-A": "CLEAN || FIRED"})
    ok("INDEX extractor reads id+status",
       index_md_states("| **TRY-A** | 🔴 NO AT THIS PRICE | SCOPE |") == {"TRY-A": "🔴 NO AT THIS PRICE"})
    ok("TRADE_BOOK last row wins",
       trade_book_states(
           "| d | TRY-A x | o | v | w | CONDITIONAL | c |\n"
           "| d | TRY-A y | o | v | w | CLOSED | c |") == {"TRY-A": "CLOSED"})
    ok("card header verdict is the FIRST one",
       cards_from_text("c.md", "**Setup ID:** `TRY-A` ·\n**Terry verdict:** CLEAN\nlater\n"
                               "**Terry verdict (2026-01-01):** CONDITIONAL")[1].startswith("CLEAN"))

    print(f"\n  {'SELFTEST PASS' if not fails else f'SELFTEST FAIL ({fails})'}")
    return 1 if fails else 0


# ---------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(description="TERRY ledger sweep — card/ledger state agreement + superseded-token drift")
    ap.add_argument("--since", default="2 days ago", help="git window for check B (default: '2 days ago')")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--explain", action="store_true")
    args = ap.parse_args()

    if args.explain:
        print(__doc__)
        return 0
    if args.selftest:
        rc = selftest()
        print("\n--- live run ---")
        rc_live = run_live(args.since)
        return rc or rc_live
    return run_live(args.since)


def run_live(since: str) -> int:
    print("TERRY ledger sweep")
    print("==================")
    if not SETUPS_TSV.exists():
        print("  FAIL — run from repo root: (cd \"$(git rev-parse --show-toplevel)\" && python3 AGENTS/TERRY/scripts/ledger_sweep.py)")
        return 1

    claims, cards, surfaces = gather_live()
    a = check_state_agreement(claims)
    c = check_header_vs_body(cards)
    tokens = struck_tokens_from_diff(recent_diff(since))
    b = check_superseded_drift(tokens, surfaces)

    print(f"\nC. CARD HEADER vs ITS OWN BODY — {len(cards)} card(s)")
    if c:
        for f in c:
            print(f"  🔴 {f}")
    else:
        print("  ✓ every card header matches its latest in-body verdict")

    print(f"\nA. STATE AGREEMENT — {len(claims)} setup_ids across "
          f"{len({s for c in claims.values() for s in c})} surfaces")
    if a:
        for f in a:
            print(f"  🔴 {f}")
    else:
        print("  ✓ all surfaces agree")

    print(f"\nB. SUPERSEDED-VALUE DRIFT — {len(tokens)} corrected value(s) since '{since}'"
          + (f": {', '.join(f'{k}={v}' for k, v in sorted(tokens))}" if tokens else ""))
    if b:
        for f in b:
            print(f"  🔴 {f}")
    else:
        print("  ✓ no naked superseded values" if tokens else "  ✓ nothing corrected in window — nothing to sweep")

    total = len(a) + len(b) + len(c)
    print(f"\n{'🔴 ' + str(total) + ' FINDING(S) — sweep before closeout' if total else '✅ CLEAN'}")
    return 1 if total else 0


if __name__ == "__main__":
    raise SystemExit(main())
