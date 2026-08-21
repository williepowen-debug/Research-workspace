#!/usr/bin/env python3
"""BOND — stale ASSERTION sweep (the half boot_recompute's drift check cannot see).

WHY THIS EXISTS
---------------
`boot_recompute.py` catches stale NUMBERS. The 2026-08-20 core-file sweep found
that the worst finding was not a number at all:

    TRADE.md: "NO REGISTERED PREDICTION COVERS ANY GATE BELOW.
               thesis/PREDICTIONS.tsv IS EMPTY ... nothing has been
               registered since [8/15]."

Two predictions were OPEN. The claim was already false the day it was written.
No numeric check can see it, because there is no number in it.

Per `finding_dated_carry_item_has_no_expiry_check`: **a carried assertion is a
string; reading it never evaluates it.** A number at least looks wrong
eventually. An assertion just sits there being read and believed.

WHAT IT CHECKS (only mechanically decidable shapes -- see LIMITS)
-----------------------------------------------------------------
  A. DIRECTIONAL  -- "closing / widening / moving toward" about a tracked
     series, verified against that series' ACTUAL recent direction.
     Catches: STATUS+TRADE "one gate is closing" while DFII10 moved AWAY.
  B. FILE-STATE   -- "PREDICTIONS.tsv IS EMPTY", "zero open predictions",
     "inbox drained", verified against the actual file.
     Catches: the TRADE.md defect above.
  C. EXPIRED      -- a past date carrying a still-pending verb and no
     resolution marker.
  D. CAPABILITY   -- "unavailable / blocked / not built / standing series"
     with no `re-test:` trigger. Extends closeout step 16 beyond STATUS.

LIMITS -- stated because a checker that implies more coverage than it has is
itself a stale assertion:
  * It cannot judge whether a piece of ANALYSIS is still true. "The regime
    rotated mid-July" is unfalsifiable by grep.
  * It cannot see an assertion phrased in words it does not know.
  * A silent run means "none of THESE shapes fired", never "the file is true".

USAGE
-----
    python3 monitors/assertion_check.py            # live surfaces
    python3 monitors/assertion_check.py --all      # + analysis/ and archives

rc 0 = nothing fired. rc 1 = at least one finding. rc 1 is NOT a pass.
A finding is a prompt to LOOK, never an instruction to find-replace.
"""
from __future__ import annotations

import datetime as dt
import glob
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent          # AGENTS/BOND
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO / "FORGE" / "tools" / "market-data"))

TODAY = dt.date.today()

# SCRATCH and RECEIPT added 2026-08-20 after an audit found the checker had
# missed a killed framing sitting in SCRATCH.md -- boot read #2, the canonical
# "where are we" handoff. A checker that skips the file the next session reads
# FIRST is scoped wrong.
LIVE_SURFACES = ["STATUS.md", "TRADE.md", "NEXUS_BRIEF.md", "PROTOCOL.md",
                 "CLAUDE.md", "thesis/THESIS.md", "docket/CATALYSTS.tsv",
                 "SCRATCH.md", "RECEIPT.md"]

# A line carrying one of these is ALREADY marked as historical/corrected.
# Flagging it again is the noise that trains a desk to ignore the tool.
GUARD = ("supersed", "corrected", "retract", "was \"", "read \"", "until 8/",
         "historical", "re-pin", "prior", "no longer", "outcome:", "resolved",
         "retired", "✅", "killed", "dead", "stale —", "this line", "i published",
         "my first", "wrongly", "false:", "not the action")

# Everything after this sentinel in a file is treated as explicitly superseded.
SENTINEL = "ASSERTION_CHECK: LIVE-REGION-ENDS"

TRACKED = {                       # alias -> (FRED series, gate level)
    "DFII10": ("DFII10", 2.50), "10Y real": ("DFII10", 2.50),
    "DGS30": ("DGS30", 5.00), "DGS10": ("DGS10", 4.50),
}
TOWARD = ("closing", "closing fast", "narrowing", "approaching", "moving toward",
          "toward it", "re-deepen", "redeepen", "closing in")
AWAY = ("moving away", "backed off", "backing off", "widening", "receding",
        "moved away", "further away")


def live_lines(path: Path):
    """Yield (lineno, text) for the file's LIVE region only."""
    try:
        raw = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return
    for i, l in enumerate(raw, 1):
        if SENTINEL in l:
            return
        yield i, l


QUOTES = [('"', '"'), ('\u201c', '\u201d'), ("'", "'"), ('\u2018', '\u2019'),
          ('*"', '"'), ('`', '`')]


def in_quotes(line: str, start: int, end: int) -> bool:
    """True if [start,end) sits inside a quoted span.

    A QUOTED claim is a CITATION, not an assertion. Added 2026-08-20 after the
    combined closeout pass flagged this desk's OWN documentation: the FILES
    table row that quotes "PREDICTIONS.tsv IS EMPTY" as the example defect the
    checker exists to catch. Same family as the comparator rule in the numeric
    check -- the discriminator is grammatical, not a keyword blacklist, so it
    generalises to quoted claims the GUARD list has never seen.
    """
    for op, cl in QUOTES:
        depth, i = 0, 0
        while i < len(line):
            if line.startswith(op, i) and (depth == 0 or op != cl):
                nxt = line.find(cl, i + len(op))
                if nxt == -1:
                    break
                if i + len(op) <= start and end <= nxt:
                    return True
                i = nxt + len(cl)
                continue
            i += 1
    return False

def guarded(line: str) -> bool:
    low = line.lower()
    return any(g in low for g in GUARD)


def show(tag, path, i, line, msg):
    flat = re.sub(r"\s+", " ", line).strip()
    print(f"\n  🔴 {tag} — {path.name}:{i}")
    print(f"     {msg}")
    print(f"     │ {flat[:150]}{'…' if len(flat) > 150 else ''}")


def capability_hit(line: str) -> bool:
    """True if `line` asserts a source cannot be obtained, with no re-test trigger."""
    CLAIM = (r"\b(unavailable|unscoreable|not free\b|no free\b|paywall|paywalled|"
             r"does not publish|not published|no [\w-]+ (published|available)|"
             r"cannot be (pulled|fetched|verified|scored))")
    SOURCE = (r"(fred|treasurydirect|treasury\s|api|endpoint|series|feed|primary|"
              r"markit|s&p|ny fed|mof|ecb|boe|rba|dataset|publish|when-issued|index level)")
    if guarded(line) or line.lstrip().startswith("|"):
        return False
    if not re.search(SOURCE, line, re.I):
        return False
    # Examine EVERY claim match, not just the first: on BND-17's residual branch
    # the first match was "UNSCOREABLE" inside the verdict LABEL "VOID-UNSCOREABLE",
    # which sits BEFORE the governing "if" and so masked the conditional entirely.
    m = None
    for c in re.finditer(CLAIM, line, re.I):
        if re.search(r"void[-\s]*$", line[:c.start()], re.I):
            continue                      # verdict label, not a claim about a source
        m = c
        break
    if m is None:
        return False
    # A CONDITIONAL claim is not an assertion. "resolves VOID-UNSCOREABLE IF
    # TreasuryDirect has not published components within 24h" is a grading RULE,
    # not a claim that anything is unavailable. Added 2026-08-20 after this fired
    # on BND-17's own residual branch. Fourth grammatical discriminator, after
    # comparator (numeric check), quotation (citation) and source-referent.
    if re.search(r"\b(if|unless|in the event|should|were)\b[^.]{0,90}$",
                 line[:m.start()], re.I):
        return False
    return not re.search(r"re-?test\s*:", line, re.I)


def direction_claims(line: str):
    """Yield (alias, claim, word) for each direction word attributed to its NEAREST alias."""
    if guarded(line):
        return
    low = line.lower()
    aliases = [(m.start(), a) for a in TRACKED
               for m in re.finditer(re.escape(a.lower()), low)]
    if not aliases:
        return
    for words, claim in ((TOWARD, "toward"), (AWAY, "away")):
        for w in words:
            for wm in re.finditer(re.escape(w), low):
                pos, alias = min(aliases, key=lambda t: abs(t[0] - wm.start()))
                if abs(pos - wm.start()) <= 120:
                    yield alias, claim, w


def check_directional(series) -> int:
    """A. A direction word about a tracked series, vs its ACTUAL direction.

    TWO DISCRIMINATORS, both learned the hard way on 2026-08-20:

    1. NEAREST alias, not earliest-in-line. A line reading
       "30Y ... DFII10 now 9bp away and CLOSING" is a claim about DFII10;
       attributing it to 30Y because "30Y" appears first is the same
       line-level conflation that made the gate check cry wolf on
       "30Y >5.0 / 10Y >4.6".
    2. MULTI-WINDOW AGREEMENT. The claim does not state its lookback, so a
       single arbitrary window lets the CHECKER pick the verdict -- exactly
       the defect logged as KB-BND-148 the same morning this was written.
       Flag ONLY when the claim contradicts the actual direction over EVERY
       window (1, 3 and 5 published observations). If the windows disagree,
       the claim is unfalsifiable as phrased and this tool says nothing.
    """
    n = 0
    for rel in LIVE_SURFACES:
        p = HERE / rel
        for i, l in live_lines(p):
            if guarded(l):
                continue
            for alias, claim, w in direction_claims(l):
                sid, gate = TRACKED[alias]
                obs = series.get(sid)
                if not obs or len(obs) < 6:
                    continue
                now = obs[-1][1]
                d_now = abs(gate - now)
                verdicts = set()
                for back in (1, 3, 5):
                    prev = obs[-1 - back][1]
                    d_prev = abs(gate - prev)
                    verdicts.add("toward" if d_now < d_prev - 1e-9
                                 else "away" if d_now > d_prev + 1e-9 else "flat")
                if len(verdicts) != 1:
                    continue            # windows disagree => unfalsifiable, stay silent
                actual = verdicts.pop()
                if actual == "flat" or actual == claim:
                    continue
                show("DIRECTION REVERSED", p, i, l,
                             f"claims {sid} moving {claim.upper()} its {gate} gate "
                             f"(\"{w}\"); it moved {actual.upper()} over ALL of the last "
                             f"1/3/5 published obs (now {now} [{obs[-1][0]}], "
                             f"distance {d_now*100:.0f}bp)")
                n += 1
    return n


def check_file_state() -> int:
    """B. Claims about a file's contents, checked against that file."""
    n = 0
    pred = HERE / "thesis" / "PREDICTIONS.tsv"
    open_ids = []
    if pred.exists():
        for row in pred.read_text(encoding="utf-8").splitlines()[1:]:
            f = row.split("\t")
            if len(f) > 6 and f[6].strip() == "OPEN":
                open_ids.append(f[0])
    inbox = [f for f in glob.glob(str(HERE / "inbox" / "*.md"))]
    wlane = [f for f in glob.glob(str(HERE / "inbox" / "WALTER" / "*.md"))]

    CLAIMS = [
        (r"predictions\.tsv[^.]{0,40}\bis empty\b|no registered prediction|"
         r"zero open predictions|nothing has been registered",
         lambda: bool(open_ids),
         lambda: f"PREDICTIONS.tsv has {len(open_ids)} OPEN row(s): {', '.join(open_ids)}"),
        (r"inbox[^.]{0,30}(fully )?drained|inbox[^.]{0,20}\b0 residue|inbox: 0\b",
         lambda: bool(inbox or wlane),
         lambda: f"inbox/ has {len(inbox)} top-level and {len(wlane)} WALTER-lane file(s) unprocessed"),
    ]
    for rel in LIVE_SURFACES:
        p = HERE / rel
        for i, l in live_lines(p):
            if guarded(l):
                continue
            for pat, is_false, detail in CLAIMS:
                m = re.search(pat, l, re.I)
                if not m or not is_false():
                    continue
                if in_quotes(l, m.start(), m.end()):
                    continue          # a CITATION of the claim, not the claim
                show("FILE-STATE CLAIM FALSE", p, i, l, detail())
                n += 1
    return n


# Both date shapes this desk actually writes. The ISO-only version of this
# regex was the checker's largest blind spot: a 2026-08-21 audit measured
# 253 ISO tokens against 1,336 slash tokens across the scanned surfaces, so
# the rule could see 16% of the dates -- and the STATUS catalyst twin, the
# one place past-dated pending items structurally accumulate, is written
# ENTIRELY in slash format and was therefore invisible by construction.
DATE_TOKEN = re.compile(
    r"(?<![\d/])(?:(20\d{2})-(\d{1,2})-(\d{1,2})|(\d{1,2})/(\d{1,2})(?:/(\d{2,4}))?)(?![\d/])")

CLAUSE = 90          # chars either side of the date == "the same clause"

# A date 1-3 days past carrying "not yet published" is NORMAL OPERATIONS on a
# rates desk -- H.15 publishes on a lag and saying so is correct, not stale.
# Without a floor the rule fires on every dashboard vintage caveat and trains
# the desk to skim past it. The target class is work that should have HAPPENED:
# 16d for the 8/05 QRA twin, 29d for the 7/23 ECB action, 36-94d for the
# unverified outbox packets. Ten days clears the release-lag band and keeps
# every real instance the 2026-08-21 audit found.
MIN_AGE = dt.timedelta(days=10)

STRICT = "--strict" in sys.argv    # clause-scoped suppression; see check_expired()


def resolve_date(m):
    """A matched date token -> a real date, or None if it isn't one.

    A bare `m/d` carries no year. Resolve it to the most recent occurrence
    at or before today: this rule only ever asks about the PAST, and reading
    `12/16` in August as *this* December would silently make an expired item
    look like a future one -- failing in the direction that hides work.
    """
    if m.group(1):
        try:
            return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            return None
    mo, da = int(m.group(4)), int(m.group(5))
    if not (1 <= mo <= 12 and 1 <= da <= 31):
        return None                      # a fraction or a ratio, not a date
    if m.group(6):
        y = int(m.group(6))
        y += 2000 if y < 100 else 0
        try:
            return dt.date(y, mo, da)
        except ValueError:
            return None
    for y in (TODAY.year, TODAY.year - 1):
        try:
            d = dt.date(y, mo, da)
        except ValueError:
            continue
        if d <= TODAY:
            return d
    return None


def expired_hits_in(line: str):
    """The EXPIRED predicate for ONE line. Extracted 2026-08-21 so --selftest
    exercises the SAME code path the live run does. A selftest with its own
    copy of the predicate validates the copy nobody runs -- the free-parameter
    cross-check defect, applied to a test harness."""
    # "upcoming" added 2026-08-21: the STATUS audit found a 14-line section
    # titled "★ UPCOMING" describing two auctions that were BOTH past and BOTH
    # already graded, future-tense throughout. This rule could not see it --
    # a forward-looking HEADER is the purest form of the defect the rule hunts
    # and its vocabulary had no word for it.
    PENDING = (r"\b(pending|owed|awaiting|due|"
               r"will (be|resolve|run|fire|land|need|have to)|expects?|"
               r"to be (pulled|graded|run)|not yet|outstanding|"
               r"still (open|owed|unverified)|unverified)\b")
    DONE = (r"(\b(resolved|fired|graded|closed|done|void|retired|discharged|"
            r"delivered|complete)\b|✅)")
    # STRONG vs SOFT pending vocabulary, split 2026-08-21.
    #   SOFT ("not yet published", "due", "owed") carries a 10-day floor: on a
    #   rates desk a 1-day-old release-lag caveat is NORMAL OPERATIONS and
    #   firing on it teaches the desk to skim the output.
    #   STRONG ("upcoming", "forthcoming") bypasses the floor: nothing can be
    #   upcoming about a date already past, at ANY age. The STATUS audit found
    #   a section titled "★ UPCOMING" for two auctions 1-2 days past and BOTH
    #   already graded -- inside the floor, so the soft rule could never see it.
    STRONG = r"\b(upcoming|forthcoming)\b"
    n = 0
    for m in DATE_TOKEN.finditer(line):
        d = resolve_date(m)
        if d is None:
            continue
        age = TODAY - d
        if age > dt.timedelta(days=120) or age <= dt.timedelta(0):
            continue
        near_s = line[max(0, m.start() - CLAUSE):m.start() + CLAUSE]
        if age < MIN_AGE and not re.search(STRONG, near_s, re.I):
            continue
        near = near_s
        if not (re.search(PENDING, near, re.I) or re.search(STRONG, near, re.I)):
            continue
        scope = near if STRICT else line
        if re.search(DONE, scope, re.I) or guarded(scope):
            continue
        # A pending item WITH A PLAN is not what this rule hunts. The target is
        # orphaned work -- a past date with a pending verb and nothing scheduled.
        # An explicit `re-test:` trigger, or a FUTURE date in the same clause,
        # IS the disposition. Added 2026-08-21 after the rule fired on two rows
        # that were correctly dispositioned: a Jackson Hole row carrying
        # "re-test: retry the KC Fed primary before 8/27", and a SCRATCH item
        # reading "8/27 — content-check the 5 unverified outbox packets".
        # Without this it would have fired on both every closeout until 8/27 --
        # a standing false alarm is what teaches a desk to skim the output.
        # `re-test:` is checked on the WHOLE line: it is a disposition for the
        # row, and on a long docket row it sits far from the date it covers.
        if "re-test:" in line.lower():
            continue
        # NO future-date branch. It was tried on 2026-08-21 and REVERTED the
        # same session: a future date in the clause can be a scheduled
        # DISPOSITION ("8/27 - content-check the packets") or simply the
        # EVENT's own date ("Fri 8/28 or Mon 8/31 - MOF monthly. DATE
        # UNVERIFIED"), and suppressing on it killed a REAL defect fixture.
        # `re-test:` is kept because it is unambiguous and is already this
        # desk's documented convention (closeout step 16).
        return [(m.group(0), (TODAY - d).days)]
    return []


def check_expired() -> int:
    """C. A past date still carrying a pending verb, with no resolution marker.

    DEFAULT: GUARD/DONE suppress at WHOLE-LINE scope (high precision).
    --strict: they suppress at CLAUSE scope (higher recall, more noise).

    WHY BOTH, and why the default did NOT change -- this is a finding against
    my own audit. The 2026-08-21 audit claimed 59 past-date+pending instances
    were being hidden by a stray "✅" elsewhere on a long table row, and
    proposed clause-scoping as the fix. Measured across suppression radii:

        radius   ±90   ±150   ±250   ±400   whole-line
        hits      17     13      9      6        4

    Reading the hits rather than the count: most of the 59 are rows whose
    resolution genuinely IS the row's subject -- the DONE token was doing its
    job, and the audit had counted co-occurrence as suppression. The tradeoff
    is also NOT monotone: ±250 drops a REAL defect (TRADE.md:97 carrying
    "DATE UNVERIFIED, verify asked of SAM" 3 days after the date resolved)
    while keeping softer ones. So there is no clean radius to pick.

    A tool that cries wolf is worse than one that misses -- see the GUARD
    comment above, written for exactly this. Default stays quiet; the deep
    pass is opt-in.
    """
    # \b matters: without it `owed` matches inside "showed" and `due` inside
    # "overdue"/"residue". Found 2026-08-21 -- the un-bounded version fired on
    # STATUS.md:139, a correct and current line, purely on "SAM showed".
    # NOT a bare `will`: the operator is NAMED Will, and this desk writes
    # "Will-approved" / "Will-ruled" / "Will's HELD item" constantly. A bare
    # \bwill\b turns every ruling provenance stamp into a pending verb -- 10
    # false positives on first run, 2026-08-21. Require a real future verb.
    # "upcoming" added 2026-08-21: the STATUS audit found a 14-line section
    # titled "★ UPCOMING" describing two auctions that were BOTH past and BOTH
    # already graded, future-tense throughout. This rule could not see it --
    # a forward-looking HEADER is the purest form of the defect the rule hunts
    # and its vocabulary had no word for it.
    PENDING = (r"\b(pending|owed|awaiting|due|"
               r"will (be|resolve|run|fire|land|need|have to)|expects?|"
               r"to be (pulled|graded|run)|not yet|outstanding|"
               r"still (open|owed|unverified)|unverified)\b")
    DONE = (r"(\b(resolved|fired|graded|closed|done|void|retired|discharged|"
            r"delivered|complete)\b|✅)")
    n = 0
    for rel in LIVE_SURFACES:
        p = HERE / rel
        for i, l in live_lines(p):
            for tok, age in expired_hits_in(l):
                show("EXPIRED-PENDING", p, i, l,
                     f"date {tok} is {age}d past and this CLAUSE still reads as "
                     f"pending, with no resolution marker in it")
                n += 1
    return n


def check_capability() -> int:
    """D. An availability/capability claim with no re-test trigger.

    Delegates to `capability_hit()` -- ONE definition of the predicate, shared
    with --selftest. An earlier version kept a second copy of the regex here;
    two copies that can drift apart is the same defect as a cross-check with a
    free parameter, and the selftest would have validated the copy nobody runs.
    """
    n = 0
    surfaces = LIVE_SURFACES + [f"monitors/{Path(f).name}"
                                for f in sorted(glob.glob(str(HERE / "monitors" / "*.md")))]
    for rel in surfaces:
        p = HERE / rel
        for i, l in live_lines(p):
            if capability_hit(l):
                show("CAPABILITY CLAIM, NO RE-TEST", p, i, l,
                     "a claim about what can/cannot be obtained, with no `re-test:` trigger — "
                     "these are self-sealing: nobody re-tests a source the file says is unavailable")
                n += 1
    return n


# ---------------------------------------------------------------------------
# SELFTEST — fixtures are the REAL defects this desk shipped, verbatim.
# A checker that passes because nothing is left is not a verified checker.
# Run: python3 monitors/assertion_check.py --selftest
# ---------------------------------------------------------------------------
FIXTURES = [
    # (label, line, predicate, expected)
    ("REAL 8/20 defect (verbatim TRADE.md, pre-stamp)",
     "auction gates are composition-keyed and TAIL-FREE (no when-issued published by "
     "TreasuryDirect => a tail-keyed gate is unscoreable by construction)",
     "cap", True),
    ("same claim WITHOUT the magic word -- gap found BY --selftest",
     "the tail column is empty: no when-issued published by TreasuryDirect",
     "cap", True),
    ("REAL: CDX paywall, no re-test",
     "- CDX: true index levels are paywalled (S&P/Markit). Use monitors/cdx_proxy.py",
     "cap", True),
    ("guarded once stamped with re-test:",
     "a tail is unscoreable from TreasuryDirect (re-test: 2026-11-01)",
     "cap", False),
    ("substring trap: 'not FREEze'",
     "Primary market in BOOM, not freeze - April HY priced $40B, series intact",
     "cap", False),
    ("prose reusing the word, no source referent",
     "the desk went dark through the biggest rates day of the month",
     "cap", False),
    ("historical table cell",
     "| 2026-05-08/11 | 281bps | n/a (data gap) | could not adjudicate | FRED + missing CDX source |",
     "cap", False),
    ("REAL 8/20 defect: reversed gate direction",
     "TLT puts HOLD. The arm has RE-DEEPENED and one gate is closing. DFII10 2.41, now 9bp from the 2.5 gate and moving toward it",
     "dir", ("DFII10", "toward")),
    ("nearest-alias, NOT earliest-in-line",
     "30Y 5.28 and 10Y 4.71 -- DFII10 now 9bp away and closing",
     "dir", ("DFII10", "toward")),
    ("quoted CITATION of the defect, not the claim (fired on our own docs)",
     'Stale-ASSERTION sweep. Built because the sweep\'s worst finding — '
     '"PREDICTIONS.tsv IS EMPTY" with two OPEN rows — contained no number.',
     "quote", False),
    ("the SAME claim unquoted is still a finding",
     "NO REGISTERED PREDICTION COVERS ANY GATE BELOW. thesis/PREDICTIONS.tsv IS EMPTY.",
     "quote", True),
    ("CONDITIONAL branch is a RULE, not a claim (fired on BND-17's VOID branch)",
     "resolves VOID-UNSCOREABLE if TreasuryDirect has not published competitive-accepted "
     "components for this CUSIP within 24h of the auction",
     "cap", False),
    ("the SAME words unconditionally ARE a claim",
     "TreasuryDirect has not published competitive-accepted components for this CUSIP",
     "cap", True),
    ("already corrected => guarded",
     "Corrected 8/20: this cell read '6bp away and closing' -- DFII10 backed off to 2.41",
     "dir", None),

    # ---- Shape C (EXPIRED) fixtures, all added 2026-08-21 from the boot-doc
    # audit. Every one is a REAL defect or a REAL false positive shipped that
    # day; none is hypothetical.

    # C1. THE BLIND SPOT: slash dates. The ISO-only regex could see 16% of the
    # dates on these surfaces (253 ISO vs 1,336 slash), and the STATUS catalyst
    # twin is written ENTIRELY in slash format -- invisible by construction.
    ("slash date resolves (was invisible: ISO-only regex)",
     ("Wed 8/5", None), "date", "2026-08-05"),
    ("ISO date still resolves", ("2026-08-05", None), "date", "2026-08-05"),
    ("m/d/yy form resolves", ("8/5/26", None), "date", "2026-08-05"),
    # C2. A bare m/d has no year. Resolving 12/16 in August as THIS December
    # would make an expired item look future-dated -- failing in the direction
    # that HIDES work. Must resolve backwards.
    ("bare m/d resolves BACKWARD, never into the future",
     ("12/16", None), "date", "2025-12-16"),
    # C3. Not every slash pair is a date.
    ("13/45 is not a date (ratio/fraction guard)", ("13/45", None), "date", None),
    ("3.76x ratio is not a date", ("ratio 3.76x", None), "date", None),

    # C4. REAL DEFECT, STATUS.md:222 -- the QRA twin read "still UNVERIFIED,
    # do not grade anything off it" for 16 days after the content was
    # established at two primaries. The rule could not see "Wed 8/5".
    ("REAL 8/21 defect: QRA twin pending 16d after content established",
     "| Wed 8/5 | QRA (pattern-inferred - still UNVERIFIED) | do not grade anything off it until it is |",
     "expired", True),
    # C5. REAL DEFECT, TRADE.md:97 -- MOF date carried "DATE UNVERIFIED,
    # verify asked of SAM" three days after the docket resolved it.
    ("REAL 8/21 defect: MOF date unverified 22d past",
     "- Fri 8/28 or Mon 8/31 - MOF monthly. DATE UNVERIFIED, verify asked of SAM. size read on the 7/30-31 op",
     "expired", True),

    # C6. REAL FALSE POSITIVE, STATUS.md:139 -- "SAM showed" matched `owed`
    # because PENDING had no word boundaries. A correct, current line.
    ("REAL 8/21 false positive: 'showed' must not match `owed`",
     "> SAM showed the 7/13 window is DISQUALIFYING, not merely caveated: its JGB signature is a flattener",
     "expired", False),
    # C7. REAL FALSE POSITIVE x10 -- the OPERATOR IS NAMED WILL. A bare
    # \bwill\b turned every ruling-provenance stamp into a pending verb.
    ("REAL 8/21 false positive: 'Will-approved' is a name, not a future verb",
     "- MBS / housing finance (coverage extension, Will-approved 6/27, integrated 7/1): MBS pricing/spreads",
     "expired", False),
    ("REAL 8/21 false positive: \"Will's HELD sub-item\" is a name",
     "| Mon 8/24 | Will's HELD sub-item - US sovereign CDS (8/10 forum DOCKET deferral) | Reconsideration date |",
     "expired", False),
    # C8. A genuine future verb still fires.
    ("a real future verb still fires",
     "the 7/02 FR2004 print is still owed and will be pulled when the lane reopens",
     "expired", True),
    # C9. MIN_AGE: a 1-day-old release-lag caveat is NORMAL OPERATIONS on a
    # rates desk, not a stale pending item. Without the floor this fired on
    # every dashboard vintage note.
    ("REAL 8/21 defect: a section titled UPCOMING for two PAST, GRADED auctions",
     "## UPCOMING -- 8/19 20Y and 8/20 30Y TIPS (dates VERIFIED at the primary 2026-08-18)",
     "expired", True),
    ("release-lag caveat inside MIN_AGE does NOT fire",
     "| 10Y real (DFII10) | 2.35% [8/19] | 8/20 NOT YET PUBLISHED on this series |",
     "expired", False),

]


def selftest() -> int:
    fails = 0
    print("[assertion_check --selftest] fixtures are REAL defects this desk shipped\n")
    for label, line, kind, expected in FIXTURES:
        if kind == "quote":
            pat = (r"predictions\.tsv[^.]{0,40}\bis empty\b|no registered prediction|"
                   r"zero open predictions|nothing has been registered")
            m = re.search(pat, line, re.I)
            got = bool(m) and not guarded(line) and not in_quotes(line, m.start(), m.end())
        elif kind == "cap":
            got = capability_hit(line)
        elif kind == "date":
            # (text, ref_date) -> the date the token resolves to, or None
            txt, ref = line
            m = DATE_TOKEN.search(txt)
            got = resolve_date(m).isoformat() if (m and resolve_date(m)) else None
        elif kind == "expired":
            got = bool(expired_hits_in(line))
        else:
            claims = list(direction_claims(line))
            got = (claims[0][0], claims[0][1]) if claims else None
        ok = (got == expected)
        fails += 0 if ok else 1
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
        if not ok:
            print(f"        expected {expected!r}, got {got!r}")
    print("\n" + "=" * 74)
    print(f"  {'ALL PASS' if not fails else str(fails) + ' FAILURE(S)'} — "
          f"{len(FIXTURES)} fixtures")
    print("  Known GAP, stated so it is not mistaken for coverage: the retracted")
    print("  \"my FRED series starts 2021-08\" would NOT fire — it is a capability")
    print("  claim phrased in words no pattern here knows. Shape D catches the")
    print("  vocabulary it knows, never the class.")
    print("=" * 74)
    return 1 if fails else 0

def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    print(f"[assertion_check] run {dt.datetime.now():%Y-%m-%d %H:%M} local · "
          f"live surfaces only (sentinel: {SENTINEL})")
    series = {}
    try:
        import fetch
        for sid in ("DFII10", "DGS30", "DGS10"):
            raw = fetch.fred_fetch(sid, limit=400)
            series[sid] = sorted((o["date"], float(o["value"])) for o in raw if "error" not in o)
    except Exception as e:                                   # noqa: BLE001
        print(f"  ⚠️  series fetch failed ({e}) — DIRECTIONAL check SKIPPED, "
              f"which is a GAP not a pass", file=sys.stderr)

    total = 0
    total += check_directional(series) if series else 0
    total += check_file_state()
    total += check_expired()
    total += check_capability()

    print("\n" + "=" * 74)
    if total == 0:
        print("  ✅ no stale assertion of a CHECKED SHAPE fired.")
        print("     Not a certificate of truth: analysis claims, and assertions phrased")
        print("     in words this tool does not know, are outside its scope entirely.")
    else:
        print(f"  🔴 {total} finding(s). rc=1 — NOT a pass.")
        print("     Each is a prompt to LOOK, never an instruction to find-replace:")
        print("     a correctly-labelled QUOTE of a corrected error is a legitimate hit.")
    print("=" * 74)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
