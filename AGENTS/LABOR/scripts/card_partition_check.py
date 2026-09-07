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

FALSIFIED BEFORE ADOPTION (10 self-tests, `--self-test`): fires on a gap, an overlap, a missing
two-axis cell and a prose/table contradiction; stays quiet on a clean partition, a correctly
written prose set, a date column, and an abbreviated "186-199K" range; returns CANNOT-VERIFY
rather than PASS when there is no table. Four parser defects were found BY the self-test and by
running it against real cards — a sentence splitter that broke on "i.e.", band letters scraped
out of the word "AND", dates read as ranges, and a unit written once on a two-endpoint range —
each of which had made the check silently return PASS or invent findings.

USAGE
  python3 AGENTS/LABOR/scripts/card_partition_check.py <card.md> [<card.md> ...]
  python3 AGENTS/LABOR/scripts/card_partition_check.py --self-test
Run from anywhere; paths are taken as given.
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
    """Return (lo, hi) closed-ish interval from a band cell, or None if not an interval."""
    c = re.sub(r"[*`]", "", cell).strip()
    if not c:
        return None
    # A date is not an interval. "2026-07-04" reads as the range 7-2026 through the hyphen
    # branch below and manufactured 6 phantom OVERLAP/OPEN-END findings on the 8/13 card's
    # week-ending column — noise that trains the reader to ignore real ones.
    if re.search(r"\d{4}-\d{2}-\d{2}|\b\d{1,2}/\d{1,2}(?:/\d{2,4})?\b", c):
        return None
    if re.search(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d", c, re.I):
        return None
    # 'X >= 250,000' / '>= 250,000' / 'X > 250,000'
    m = re.search(r"(?:[≥>]=?|≥)\s*(" + NUM + ")", c)
    m2 = re.search(r"(?:[≤<]=?|≤)\s*(" + NUM + ")", c)
    rng = re.search(r"(" + NUM + r")\s*[" + DASHES + r"]\s*(" + NUM + ")", c)
    if rng:
        g1, g2 = rng.group(1), rng.group(2)
        # "186-199K" means 186K-199K: in an abbreviated range the unit is written once, on the
        # SECOND endpoint, and applies to both. Reading it literally gives lo=186, hi=199,000 —
        # which manufactured 10 phantom OVERLAP findings across the 7/30 and 8/3-8/7 cards.
        suf = lambda t: (re.search(r"[KkMm]$", t.strip()) or [None])[0] if re.search(r"[KkMm]$", t.strip()) else None
        s1, s2 = suf(g1), suf(g2)
        if s2 and not s1:
            g1 = g1.strip() + s2
        elif s1 and not s2:
            g2 = g2.strip() + s1
        lo, hi = _n(g1), _n(g2)
        if lo is not None and hi is not None:
            return (min(lo, hi), max(lo, hi))
    if m and not m2:
        v = _n(m.group(1))
        return (v, INF) if v is not None else None
    if m2 and not m:
        v = _n(m2.group(1))
        return (-INF, v) if v is not None else None
    return None


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
    """Leg (a): find an interval column; report gaps/overlaps. Returns list of findings."""
    out = []
    ncol = max((len(r) for r in rows), default=0)
    best = None
    for ci in range(ncol):
        got = [(r[0], parse_interval(r[ci])) for r in rows if len(r) > ci]
        iv = [(lab, v) for lab, v in got if v]
        if len(iv) >= 3 and (best is None or len(iv) > len(best[1])):
            best = (ci, iv)
    if not best:
        return out
    ci, iv = best
    lab = lambda s: re.sub(r"[*`]", "", s).strip() or "?"
    iv = sorted(iv, key=lambda t: t[1][0])
    colname = hdr[ci] if ci < len(hdr) else f"col{ci}"
    bounds = [b for _, (a, b) in iv for b in (a, b) if abs(b) != INF]
    gran = 1000 if bounds and all(b % 1000 == 0 for b in bounds) else (
           100 if bounds and all(b % 100 == 0 for b in bounds) else 1)
    for (l1, (a1, b1)), (l2, (a2, b2)) in zip(iv, iv[1:]):
        if b1 == INF or a2 == -INF:
            continue
        if a2 > b1:
            # A gap only matters if a value the series can actually PRINT falls in it.
            # Granularity is inferred from the card's own boundaries: a card written in
            # 1,000s ("186-199K") has no printable value between 185,000 and 186,000, so
            # reporting a 999-value gap there is noise. A card written in full units
            # ("200,000-208,999") drops granularity to 1 and 209,000 IS printable.
            hits = [v for v in (b1 + k * gran for k in range(1, 3)) if b1 < v < a2]
            if hits:
                out.append(("GAP", f"{colname}: bands {lab(l1)} and {lab(l2)} leave "
                                   f"{hits[0]:,.0f}"
                                   + (f" - {a2 - gran:,.0f}" if a2 - gran > hits[0] else "")
                                   + f" in NO BAND (granularity {gran:,.0f})"))
        elif a2 < b1:
            out.append(("OVERLAP", f"{colname}: bands {lab(l1)} and {lab(l2)} both claim "
                                   f"{a2:,.0f} - {b1:,.0f}"))
    lo_end, hi_end = iv[0][1][0], iv[-1][1][1]
    if lo_end != -INF:
        out.append(("OPEN-END", f"{colname}: lowest band starts at {lo_end:,.0f} — "
                                f"values below it are unassigned"))
    if hi_end != INF:
        out.append(("OPEN-END", f"{colname}: highest band ends at {hi_end:,.0f} — "
                                f"values above it are unassigned"))
    return out


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
            lo, hi = bands[b]
            v = verdict(lo, hi)
            if v:
                bad.append(f"band {b} [{lo:,.0f}, {hi:,.0f}] is {v} {num:,.0f}")
        # the converse: a band that DOES satisfy the relation but was left out of the set
        omitted = [b for b, (lo, hi) in sorted(bands.items())
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
    for hdr, rows, ln in tables:
        findings += check_coverage(hdr, rows, ln, path)
        findings += check_cross(hdr, rows)
    prose, bands = check_prose(text, tables)
    findings += prose
    name = os.path.basename(path)
    if not bands:
        print(f"  ⚠️  CANNOT-VERIFY  {name}: no band table with >=3 parseable intervals. "
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
