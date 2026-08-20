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

LIVE_SURFACES = ["STATUS.md", "TRADE.md", "NEXUS_BRIEF.md", "PROTOCOL.md",
                 "CLAUDE.md", "thesis/THESIS.md", "docket/CATALYSTS.tsv"]

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
    if not re.search(CLAIM, line, re.I) or not re.search(SOURCE, line, re.I):
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


def check_expired() -> int:
    """C. A past date still carrying a pending verb, with no resolution marker."""
    PENDING = r"(pending|owed|awaiting|due|will\s|expects?|to be (pulled|graded|run)|not yet|outstanding)"
    DONE = r"(resolved|fired|graded|closed|done|✅|void|retired|discharged|delivered|complete)"
    n = 0
    for rel in LIVE_SURFACES:
        p = HERE / rel
        for i, l in live_lines(p):
            if guarded(l) or re.search(DONE, l, re.I):
                continue
            for m in re.finditer(r"20\d{2}-\d{2}-\d{2}", l):
                try:
                    d = dt.date.fromisoformat(m.group(0))
                except ValueError:
                    continue
                if not (dt.timedelta(0) < TODAY - d <= dt.timedelta(days=120)):
                    continue
                near = l[max(0, m.start() - 90):m.start() + 90]
                if re.search(PENDING, near, re.I):
                    show("EXPIRED-PENDING", p, i, l,
                         f"date {m.group(0)} is {(TODAY - d).days}d past and the line still "
                         f"reads as pending, with no resolution marker")
                    n += 1
                    break
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
    ("already corrected => guarded",
     "Corrected 8/20: this cell read '6bp away and closing' -- DFII10 backed off to 2.41",
     "dir", None),
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
