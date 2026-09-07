#!/usr/bin/env python3
"""
card_partition_check.py — PRE-FREEZE BAND-EXHAUSTION CHECK for grading cards.

Discharges BD-21 (interval coverage) + BD-30 (prose-vs-table agreement) as ONE check,
per DAEDALUS parity ACTION 6 (2026-09-07).

WHAT IT TESTS — three legs, all on branches that did NOT occur:
  (a) COVERAGE   the union of a card's band intervals covers its axis with no GAP and no OVERLAP
  (a2) CROSS     a two-axis band table enumerates the full cross-product of its axis values
  (b) PROSE      every prose sentence naming a band set agrees with the table it describes

WHY LEG (b) EXISTS (BD-30, verified case): GRADING_CARD_20260813_claims.md says the MA declines
"for any print below 209,000 — i.e. in bands C, D, E and F", but Band C is 210,000-229,999, which
is ABOVE 209,000 — and the Band C row itself says "FIRST MA RISE". The card's prose contradicts
its own table, and the card's self-audit ("no enumeration defects") tested only the branch that
occurred, which is the L-27 partition failure wearing a self-audit.

EXIT CODES (repo convention): 0 = PASS · 2 = DEFECT FOUND or CANNOT-VERIFY.
A parse failure is CANNOT-VERIFY, never a PASS (fail closed).

KNOWN LIMITS — stated, not tuned away (loosening a noisy guard inverts its failure direction):
  * It reports on ANY column of >=3 parseable intervals, including derived/reference columns
    that are not band axes. Residual OPEN-END/OVERLAP noise on those is expected and visible;
    it does not hide a real finding. Read the column name in the message before acting.
  * CANNOT-VERIFY is common and correct for prose-shaped cards (FOMC language cards, the ISM
    and NFP cards) whose branches are not written as numeric intervals. It means "check by
    hand", NOT "clean" — 4 of 9 graded cards return it today.
  * Leg (b) only fires on a sentence carrying BOTH a band set and a comparator+number. A prose
    claim phrased without a number is out of reach and always will be.
  * Granularity is inferred from the card's own boundaries. A card that mixes "199K" and
    "208,999" in one column drops to granularity 1 and may report sub-1,000 gaps.

FALSIFICATION HISTORY — read this before trusting a PASS:
  v1 (2026-09-07 AM) shipped with 10 self-tests, all passing, and was recorded as "falsified
  before adoption". CODEX then wrote 5 independent cases and **ALL FIVE returned a false PASS**:
  a single band certified as a partition; strict bounds (`<200000` / `200001-...`) leaving
  200,000 unowned; inclusive bounds (`<=200000` / `200000-...`) double-assigning it; an
  unreadable band row silently ignored; and a decimal axis whose missing 4.2 was invisible
  because granularity only ever inferred 1/100/1000.
  ⛔ **The lesson is about the SUITE, not the parser: ten tests I wrote all passed because I
  wrote them against the design I had in mind.** `[[finding_self_attack_defends_the_argument_
  not_the_apparatus]]` — a self-authored test set defends the argument, not the apparatus.
  v2 carries boundary inclusivity, integer-unit arithmetic at the inferred granularity
  (including decimals), an UNPARSEABLE finding, and a PASS that is only reachable when
  coverage actually RAN. All 15 tests pass — CODEX's 5 are permanent members of the suite.
"""
import sys, re, os

INF = float("inf")
DASHES = "–—−-"          # en, em, minus, hyphen
NUM = r"[+-]?[\d,]+(?:\.\d+)?[KkMm]?"


def _n(tok):
    """'250,000'->250000.0  '209.0K'->209000.0  '-6'-> -6.0 ; None if not numeric."""
    if tok is None:
        return None
    t = tok.strip().replace(",", "").replace("−", "-")
    m = re.fullmatch(r"([+-]?\d+(?:\.\d+)?)([KkMm]?)", t)
    if not m:
        return None
    v = float(m.group(1))
    return v * {"": 1, "k": 1e3, "K": 1e3, "m": 1e6, "M": 1e6}[m.group(2)]


def parse_interval(cell):
    """Return (lo, lo_inc, hi, hi_inc) or None.

    Boundary INCLUSIVITY is carried, not discarded. Dropping it was the defect that let
    `<200,000` + `200,001-249,999` certify as a partition (200,000 owned by nobody) and
    `<=200,000` + `200,000-250,000` certify as disjoint (200,000 owned twice).
    """
    c = re.sub(r"[*`]", "", cell).strip()
    if not c:
        return None
    if re.search(r"\d{4}-\d{2}-\d{2}|\b\d{1,2}/\d{1,2}(?:/\d{2,4})?\b", c):
        return None
    if re.search(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d", c, re.I):
        return None
    rng = re.search(r"(" + NUM + r")\s*[" + DASHES + r"]\s*(" + NUM + ")", c)
    if rng:
        g1, g2 = rng.group(1), rng.group(2)
        sfx = lambda t: (t.strip()[-1] if re.search(r"[KkMm]$", t.strip()) else None)
        s1, s2 = sfx(g1), sfx(g2)
        if s2 and not s1:
            g1 = g1.strip() + s2
        elif s1 and not s2:
            g2 = g2.strip() + s1
        lo, hi = _n(g1), _n(g2)
        if lo is not None and hi is not None:
            return (min(lo, hi), True, max(lo, hi), True)
    ge = re.search(r"(≥|>=)\s*(" + NUM + ")", c)
    gt = re.search(r">(?!=)\s*(" + NUM + ")", c)
    le = re.search(r"(≤|<=)\s*(" + NUM + ")", c)
    lt = re.search(r"<(?!=)\s*(" + NUM + ")", c)
    if (ge or gt) and not (le or lt):
        v = _n((ge.group(2) if ge else gt.group(1)))
        return (v, bool(ge), INF, False) if v is not None else None
    if (le or lt) and not (ge or gt):
        v = _n((le.group(2) if le else lt.group(1)))
        return (-INF, False, v, bool(le)) if v is not None else None
    return None


def granularity(bounds):
    """Smallest value the axis can PRINT, inferred from the card's own boundaries.

    Decimal axes were previously unreachable: granularity was 1/100/1000 only, so a
    `<=4.1` / `4.3-4.4` table had no integer strictly between 4.1 and 4.3 and the missing
    4.2 went unreported.
    """
    fin = [b for b in bounds if abs(b) != INF]
    if not fin:
        return 1.0
    dp = 0
    for b in fin:
        t = f"{b!r}"
        if "." in t:
            frac = t.split(".")[1].rstrip("0")
            dp = max(dp, len(frac))
    if dp:
        return 10.0 ** (-dp)
    if all(b % 1000 == 0 for b in fin):
        return 1000.0
    if all(b % 100 == 0 for b in fin):
        return 100.0
    return 1.0


def parse_tables(text):
    """Yield (header:list[str], rows:list[list[str]], start_line:int) for each markdown table."""
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|") and i + 1 < len(lines) and re.match(
                r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            hdr = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            rows, j = [], i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                rows.append([c.strip() for c in lines[j].strip().strip("|").split("|")])
                j += 1
            yield hdr, rows, i + 1
            i = j
        else:
            i += 1


def band_label(cell):
    c = re.sub(r"[*`\s]", "", cell)
    m = re.fullmatch(r"([A-H]|\d{1,2})", c)
    return m.group(1) if m else None


def check_coverage(hdr, rows, lineno, card):
    """Leg (a): coverage. Returns (findings, coverage_ran).

    Works in INTEGER units of the axis granularity, so boundary arithmetic is exact -- a
    float axis is what produced this repo's own 12-of-20 missed-boundary bug (L-29 #4).
    """
    out, ran = [], False
    ncol = max((len(r) for r in rows), default=0)
    best = None
    # Pick the BAND AXIS by parse FRACTION, not raw count. A prose column ("Card said: ...")
    # can contain two parseable numbers and would otherwise win on count alone, dragging its
    # narrative rows in as UNPARSEABLE and burying the real findings under noise.
    best_score = 0.0
    for ci in range(ncol):
        iv = [(r[0], parse_interval(r[ci])) for r in rows if len(r) > ci]
        if not iv:
            continue
        ok = [(l, v) for l, v in iv if v]
        frac = len(ok) / len(iv)
        if len(ok) >= 2 and frac >= 0.6 and (frac, len(ok)) > (best_score, len(best[1]) if best else 0):
            unp = [l for l, v in iv if v is None and re.sub(r"[*`\s]", "", r_cell(rows, l, ci))]
            best, best_score = (ci, ok, unp), frac
    if not best:
        return out, ran
    ci, iv, unparsed = best
    lab = lambda t: re.sub(r"[*`]", "", t).strip() or "?"
    colname = hdr[ci] if ci < len(hdr) else f"col{ci}"

    # A row in a band table whose interval cannot be read is UNVERIFIED, never ignored.
    for l in unparsed:
        out.append(("UNPARSEABLE", f"{colname}: band {lab(l)} has an unreadable interval — "
                                   f"coverage for this card is UNVERIFIED, not clean"))
    gran = granularity([b for _, (lo, _, hi, _) in iv for b in (lo, hi)])
    U = lambda v: v if abs(v) == INF else int(round(v / gran))
    # closed integer span [a,b] each band actually owns
    spans = []
    for l, (lo, li, hi, hi_i) in iv:
        a = -INF if lo == -INF else (U(lo) if li else U(lo) + 1)
        b = INF if hi == INF else (U(hi) if hi_i else U(hi) - 1)
        if a != -INF and b != INF and a > b:
            out.append(("EMPTY-BAND", f"{colname}: band {lab(l)} covers nothing"))
            continue
        spans.append((a, b, lab(l)))
    spans.sort(key=lambda t: (t[0] == -INF and -1 or 0, t[0] if t[0] != -INF else 0))
    fmt = lambda u: f"{u * gran:,.10g}"
    for (a1, b1, l1), (a2, b2, l2) in zip(spans, spans[1:]):
        if b1 == INF or a2 == -INF:
            continue
        if a2 > b1 + 1:
            out.append(("GAP", f"{colname}: bands {l1} and {l2} leave "
                               f"{fmt(b1 + 1)}" + (f" - {fmt(a2 - 1)}" if a2 - 1 > b1 + 1 else "")
                               + f" in NO BAND (granularity {gran:,.10g})"))
        elif a2 <= b1:
            out.append(("OVERLAP", f"{colname}: bands {l1} and {l2} both claim "
                                   f"{fmt(a2)}" + (f" - {fmt(b1)}" if b1 > a2 else "")))
    if spans:
        if spans[0][0] != -INF:
            out.append(("OPEN-END", f"{colname}: lowest band starts at {fmt(spans[0][0])} — "
                                    f"everything below it is unassigned"))
        if spans[-1][1] != INF:
            out.append(("OPEN-END", f"{colname}: highest band ends at {fmt(spans[-1][1])} — "
                                    f"everything above it is unassigned"))
        ran = True
    return out, ran


def r_cell(rows, label, ci):
    for r in rows:
        if r and r[0] == label and len(r) > ci:
            return r[ci]
    return ""


WILDCARD = {"any", "either", "*", "-", "—", "n/a", "all"}


def _norm(x):
    return re.sub(r"[*`]", "", x).strip().lower()


def check_cross(hdr, rows):
    """Leg (a2): a genuine two-axis band table must enumerate the full cross-product.

    DISCRIMINATOR (this is the whole difficulty): a one-axis band table — `| Band | X | ... |`
    — also has two small-domain columns, so a naive "two categorical columns" test fires on
    every card and is therefore not a test at all (it produced 2 false MISSING-CELL findings
    per table on first build). A REAL cross tabulation repeats its axis values: each axis has
    at least one value appearing in >=2 rows, because rows ARE the combinations. A band table
    never repeats a band label. That single condition separates them with no free parameter.
    """
    out = []
    ncol = min((len(r) for r in rows), default=0)
    if ncol < 3 or len(rows) < 3:
        return out
    cats = []
    for ci in range(min(ncol, 3)):
        vals = [_norm(r[ci]) for r in rows]
        uniq = {v for v in vals if v}
        if not (2 <= len(uniq) <= 5) or any(len(v) > 20 for v in uniq):
            continue
        if max(vals.count(v) for v in uniq) < 2:      # no repeat => not a cross axis
            continue
        if all(band_label(v) for v in uniq):          # a band-label column, not an axis
            continue
        cats.append((ci, uniq, vals))
    if len(cats) < 2:
        return out
    (c1, u1, v1), (c2, u2, v2) = cats[0], cats[1]
    real1 = sorted(u1 - WILDCARD)
    real2 = sorted(u2 - WILDCARD)
    if not real1 or not real2:
        return out
    # A wildcard on one axis covers every value of the other axis for that row.
    seen = set()
    for a, b in zip(v1, v2):
        A = real1 if a in WILDCARD else [a]
        B = real2 if b in WILDCARD else [b]
        for x in A:
            for y in B:
                seen.add((x, y))
    missing = [(a, b) for a in real1 for b in real2 if (a, b) not in seen]
    if missing and len(missing) < len(real1) * len(real2):
        out.append(("MISSING-CELL",
                    f"{hdr[c1]} x {hdr[c2]}: {len(missing)} of "
                    f"{len(real1) * len(real2)} cells absent -> "
                    + "; ".join(f"({a} x {b})" for a, b in missing[:6])))
    return out


SET_RE = re.compile(r"bands?\s+((?:[A-H])(?:\s*(?:,|/|、|and|&|\s)\s*[A-H])+)", re.I)
REL_RE = re.compile(r"(below|above|under|over|at or below|at or above|less than|greater than)"
                    r"\s*(" + NUM + ")", re.I)


def check_prose(text, tables):
    """Leg (b): a sentence naming a band set + a comparator must agree with the table."""
    out = []
    bands = {}
    for hdr, rows, _ in tables:
        ncol = max((len(r) for r in rows), default=0)
        for ci in range(ncol):
            for r in rows:
                if len(r) <= ci:
                    continue
                lb = band_label(r[0])
                iv = parse_interval(r[ci])
                if lb and iv and lb not in bands:
                    bands[lb] = iv
    if not bands:
        return out, bands
    # Split on LINES, not sentences: markdown card prose is one statement per line, and a
    # sentence splitter breaks on "i.e." — which is exactly the construction the real 8/13
    # defect used ("below 209,000 - i.e. in bands C, D, E and F"), severing the comparator
    # from the band set so the check silently found nothing. (Caught by the self-test.)
    for sent in text.split("\n"):
        ms, mr = SET_RE.search(sent), REL_RE.search(sent)
        if not (ms and mr):
            continue
        # \b-anchored: a bare [A-H] scan pulls "A" and "D" out of the connector word "AND",
        # which manufactures a false WRONG-SIDE finding on a correctly-written sentence.
        named = re.findall(r"\b([A-H])\b", ms.group(1).upper())
        rel, num = mr.group(1).lower(), _n(mr.group(2))
        if num is None:
            continue
        lower = rel in ("below", "under", "less than", "at or below")
        # A band [lo,hi] is fully "below N" iff hi < N; fully "above N" iff lo > N.
        # Anything else is either the wrong side entirely, or only a partial overlap.
        def verdict(lo, hi):
            if lower:
                if lo >= num:  return "WRONG SIDE — entirely at/above"
                if hi >= num:  return "only PARTLY below"
            else:
                if hi <= num:  return "WRONG SIDE — entirely at/below"
                if lo <= num:  return "only PARTLY above"
            return None
        bad = []
        for b in named:
            if b not in bands:
                bad.append(f"band {b}: no such band in any table"); continue
            lo, _li, hi, _hi = bands[b]
            v = verdict(lo, hi)
            if v:
                bad.append(f"band {b} [{lo:,.0f}, {hi:,.0f}] is {v} {num:,.0f}")
        # the converse: a band that DOES satisfy the relation but was left out of the set
        omitted = [b for b, (lo, _a, hi, _b) in sorted(bands.items())
                   if b not in named and verdict(lo, hi) is None]
        if bad:
            out.append(("PROSE", f"\"{sent.strip()[:100]}...\"\n          names bands "
                                 f"{', '.join(named)} as {rel} {num:,.0f} — but "
                                 + "; ".join(bad)))
        if omitted and not bad:
            out.append(("PROSE-OMITS", f"\"{sent.strip()[:100]}...\"\n          names bands "
                                       f"{', '.join(named)} as {rel} {num:,.0f} but omits "
                                       f"{', '.join(omitted)}, which also satisfy it"))
    return out, bands


def check_card(path):
    if not os.path.exists(path):
        print(f"  ⛔ CANNOT-VERIFY: no such file: {path}")
        return 2
    text = open(path, encoding="utf-8").read()
    tables = list(parse_tables(text))
    findings = []
    coverage_ran = False
    for hdr, rows, ln in tables:
        f, ran = check_coverage(hdr, rows, ln, path)
        findings += f
        coverage_ran |= ran
        findings += check_cross(hdr, rows)
    prose, bands = check_prose(text, tables)
    findings += prose
    name = os.path.basename(path)
    if not bands or not coverage_ran:
        # PASS must mean coverage was CHECKED, not merely that nothing complained. A single
        # band populated `bands` and returned PASS while coverage never ran at all.
        why = ("no band table with >=2 parseable intervals" if not bands
               else "only one band parsed — a partition cannot be established from one interval")
        print(f"  ⚠️  CANNOT-VERIFY  {name}: {why}. "
              f"Not a pass — check by hand or fix the card's table.")
        return 2
    if not findings:
        print(f"  ✅ PASS  {name}: {len(bands)} bands partition their axis "
              f"(no gap, no overlap, prose agrees)")
        return 0
    print(f"  ❌ DEFECT  {name}: {len(findings)} finding(s) across {len(bands)} bands")
    for kind, msg in findings:
        print(f"      [{kind}] {msg}")
    return 2


SELF_TESTS = [
    # (name, markdown, expect_rc, expect_kind_substring)
    ("gap is caught", """
| Band | X | Assignment |
|---|---|---|
| A | X >= 250,000 | fire |
| B | 230,000 - 249,999 | arm |
| C | 210,000 - 229,999 | hold |
| D | 200,000 - 208,999 | hold |
| E | X <= 199,999 | drop |
""", 2, "GAP"),
    ("clean partition passes", """
| Band | X | Assignment |
|---|---|---|
| A | X >= 250,000 | fire |
| B | 230,000 - 249,999 | arm |
| C | 210,000 - 229,999 | hold |
| D | 200,000 - 209,999 | hold |
| E | X <= 199,999 | drop |
""", 0, None),
    ("overlap is caught", """
| Band | X | Assignment |
|---|---|---|
| A | X >= 250,000 | fire |
| B | 230,000 - 255,000 | arm |
| C | X <= 229,999 | hold |
""", 2, "OVERLAP"),
    ("no table = CANNOT-VERIFY, not pass", "# a card with prose only\nNothing to parse.\n", 2, None),
    ("a DATE column is not an interval column", """
| w/e | Claims | Note |
|---|---|---|
| 2026-07-04 | 199,000 | prior |
| 2026-07-11 | 198,000 | prior |
| 2026-07-18 | 189,000 | prior |
| 2026-07-25 | 209,000 | rolls off |

| Band | X | Assignment |
|---|---|---|
| A | X >= 250,000 | fire |
| B | 200,000 - 249,999 | hold |
| C | X <= 199,999 | drop |
""", 0, None),
    ("two-axis table missing a cell is caught", """
| U-3 | LFPR | assignment |
|---|---|---|
| >= 4.3 | flat or up | genuine slack |
| >= 4.3 | down | no-signal |
| <= 4.1 | down | denominator effect |
| >= 5.0 | any | LAB-12 resolves |

| Band | X | Assignment |
|---|---|---|
| A | X >= 250,000 | fire |
| B | 200,000 - 249,999 | hold |
| C | X <= 199,999 | drop |
""", 2, "MISSING-CELL"),
    ("abbreviated K range does not invent an overlap", """
| Band | X | Assignment |
|---|---|---|
| A | <=185K | drop |
| B | 186-199K | hold |
| C | 200-229K | hold |
| D | >=230K | fire |
""", 0, None),
    ("a real gap at full-unit granularity still fires", """
| Band | X | Assignment |
|---|---|---|
| A | X >= 210,000 | fire |
| B | 200,000 - 208,999 | hold |
| C | X <= 199,999 | drop |
""", 2, "GAP"),
    # ---- the five cases from CODEX's independent review, 2026-09-07 ----------------
    # My own ten self-tests all passed while ALL FIVE of these returned PASS. They are
    # permanent: an adversarial set written by someone else is the only part of this suite
    # that was not designed around the implementation it tests.
    ("CODEX 1/5: a single band cannot establish a partition", """
| Band | X | Action |
|---|---|---|
| A | >=250000 | hold |
""", 2, "CANNOT-VERIFY"),
    ("CODEX 2/5: strict bounds leave 200000 and 250000 unowned", """
| Band | X | Action |
|---|---|---|
| A | <200000 | hold |
| B | 200001-249999 | hold |
| C | >250000 | hold |
""", 2, "GAP"),
    ("CODEX 3/5: inclusive bounds double-assign 200000 and 250000", """
| Band | X | Action |
|---|---|---|
| A | <=200000 | hold |
| B | 200000-250000 | hold |
| C | >=250000 | hold |
""", 2, "OVERLAP"),
    ("CODEX 4/5: an unreadable band row is UNVERIFIED, not ignored", """
| Band | X | Action |
|---|---|---|
| A | <=199999 | hold |
| B | 200000-229999 | hold |
| C | ??? | hold |
| D | >=230000 | hold |
""", 2, "UNPARSEABLE"),
    ("CODEX 5/5: decimal axis omits 4.2", """
| Band | X | Action |
|---|---|---|
| A | <=4.1 | hold |
| B | 4.3-4.4 | hold |
| C | >=4.5 | hold |
""", 2, "GAP"),
    ("prose contradicting the table is caught", """
| Band | X | Assignment |
|---|---|---|
| A | X >= 250,000 | fire |
| B | 230,000 - 249,999 | arm |
| C | 209,000 - 229,999 | FIRST MA RISE |
| D | 200,000 - 208,999 | falls |
| E | X <= 199,999 | falls |

The MA will decline for any print below 209,000 - i.e. in bands C, D and E - purely from roll-off.
""", 2, "PROSE"),
    ("correct prose set is NOT flagged", """
| Band | X | Assignment |
|---|---|---|
| A | X >= 250,000 | fire |
| B | 230,000 - 249,999 | arm |
| C | 209,000 - 229,999 | rise |
| D | 200,000 - 208,999 | falls |
| E | X <= 199,999 | falls |

The MA declines for any print below 209,000 - i.e. in bands D and E - purely from roll-off.
""", 0, None),
]


def self_test():
    import tempfile
    print("=" * 72)
    print("  card_partition_check.py — SELF-TEST (falsify the guard before trusting it)")
    print("=" * 72)
    ok = True
    for nm, md, want_rc, want_kind in SELF_TESTS:
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(md); tmp = f.name
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = check_card(tmp)
        out = buf.getvalue()
        good = (rc == want_rc) and (want_kind is None or want_kind in out)
        ok &= good
        print(f"  {'PASS' if good else 'FAIL'}  {nm:42} rc={rc} (want {want_rc})")
        if not good:
            print("        " + out.replace("\n", "\n        ").rstrip())
        os.unlink(tmp)
    print("-" * 72)
    print("  " + ("✅ ALL SELF-TESTS PASS" if ok else "❌ SELF-TEST FAILURE — do not trust this check"))
    return 0 if ok else 2


def main(argv):
    if "--self-test" in argv:
        return self_test()
    args = [a for a in argv[1:] if not a.startswith("-")]
    if not args:
        print(__doc__.strip()); return 2
    print("=" * 72)
    print(f"  CARD PARTITION CHECK (BD-21 + BD-30) — {len(args)} card(s)")
    print("  legs: (a) interval coverage · (a2) two-axis cross-product · (b) prose-vs-table")
    print("  every leg runs on branches that did NOT occur")
    print("=" * 72)
    worst = 0
    for p in args:
        worst = max(worst, check_card(p))
    print("-" * 72)
    print("  " + ("✅ ALL CARDS PASS" if worst == 0 else
                  "❌ DEFECT or CANNOT-VERIFY — fix before freezing the card"))
    return worst


if __name__ == "__main__":
    sys.exit(main(sys.argv))
