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

WHAT THIS TOOL CLAIMS — read before trusting a clean result:
  It reports **SCOPED LINT**, and it will tell you its scope on every run. It does NOT certify
  that a card is correct. A clean result means: every band table it could identify had a single
  resolvable axis, every row on that axis parsed, and coverage ran over all of them with no gap,
  overlap or open end — plus any prose sentence naming a band set AND a number agreed with its
  table. Everything else in the card is unexamined.

WHAT IT REPORTS PER TABLE: VERIFIED · DEFECT · UNVERIFIED · NOT-A-BAND-TABLE.
  UNVERIFIED is not a soft pass. A blank cell, an unreadable cell, fewer than two bands, or two
  columns that could each be the axis all make a table UNVERIFIED, and any UNVERIFIED table
  makes the whole run exit 2. Declare the axis to resolve ambiguity, which also removes the
  precision guess:  <!-- partition-axis: column="X" precision=1000 -->

REVIEW HISTORY — the honest version, because two earlier versions of this note overclaimed:
  v1  shipped with 10 self-tests, all passing, described as "falsified before adoption".
      CODEX wrote 5 independent cases; ALL FIVE returned a false PASS (single band certified;
      strict/inclusive boundary values unowned or double-owned; unreadable row ignored;
      decimal axis blind to a missing 4.2).
  v2  fixed those 5 and was described as falsified. CODEX wrote 4 more; ALL FOUR returned a
      false certification — a blank row ignored, an unbounded upper band swallowing later
      bands undetected, a valid table certifying a second incomplete table, and a reference
      column silently standing in for an unreadable axis. **These were SCOPE failures: v2
      emitted a card-level PASS that one good table could earn.**
  v3  per-table dispositions, no card-level certification, INF-aware overlap, blank rows
      counted as unchecked, ambiguous axis reported rather than guessed, optional explicit
      declaration. 19 self-tests + both CODEX repro sets (5 and 4) pass.
  ⛔ **The recurring error was never the parser — it was calling a self-authored suite
  "falsification".** Ten and then fifteen tests I wrote all passed because I wrote them against
  the design I had in mind. State what was tested and what was not; do not use "falsified" as a
  certification. `[[finding_self_attack_defends_the_argument_not_the_apparatus]]`
"""
import sys, re, os, math
from fractions import Fraction

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
    # a single-point band: '= 50.0 exactly', '50.0 exactly', '== 4.2'
    pt = re.search(r"(?:^|\s)={1,2}\s*(" + NUM + r")|(" + NUM + r")\s+exactly\b", c)
    if pt and not re.search(r"[" + DASHES + r"]|\bto\b|[<>≤≥]", c):
        v = _n(pt.group(1) or pt.group(2))
        if v is not None:
            return (v, True, v, True)
    # ranges written with the word 'to': '+150K to +302K'
    rng = re.search(r"(" + NUM + r")\s*(?:[" + DASHES + r"]|\bto\b)\s*(" + NUM + ")", c)
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


def lo_unit(lo, inclusive, gran):
    """Smallest PRINTABLE unit index this band owns, given its lower bound and operator."""
    k = Fraction(str(lo)) / Fraction(str(gran))
    a = math.ceil(k)
    if not inclusive and a == k:
        a += 1                      # strict '>' excludes the boundary itself
    return int(a)


def hi_unit(hi, inclusive, gran):
    """Largest PRINTABLE unit index this band owns. Rounding to NEAREST was the defect:
    at precision 1,000, `<=199,999` rounded to unit 200 and collided with `200,000-…`,
    manufacturing an overlap in a valid partition."""
    k = Fraction(str(hi)) / Fraction(str(gran))
    b = math.floor(k)
    if not inclusive and b == k:
        b -= 1
    return int(b)


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


AXIS_DECL = re.compile(r"<!--\s*partition-axis:\s*(?P<body>[^>]*?)-->", re.I)


def declared_axis(text):
    """Optional explicit declaration, which REMOVES the inference:
       <!-- partition-axis: column="X" precision=1000 bounds=inclusive -->
    Inference is a guess; a declaration is the card telling the checker what it meant."""
    m = AXIS_DECL.search(text or "")
    if not m:
        return {}
    b = m.group("body")
    out = {}
    k = re.search(r"kind\s*=\s*([a-z-]+)", b)
    if k:
        out["kind"] = k.group(1)
    c = re.search(r'column\s*=\s*"([^"]+)"', b)
    p_ = re.search(r"precision\s*=\s*([0-9.]+)", b)
    if c:
        out["column"] = c.group(1).strip()
    if p_:
        out["precision"] = float(p_.group(1))
    return out


def analyze_table(hdr, rows, decl):
    """Disposition for ONE table: (findings, status, scope).

    status: VERIFIED | DEFECT | UNVERIFIED | NOT-A-BAND-TABLE

    ⛔ This function may NOT return VERIFIED unless EVERY row of the chosen axis column
    resolved to an interval and coverage actually ran over them. A table that merely fails
    to complain is UNVERIFIED, never clean — that distinction is the whole point of the v3
    rewrite (CODEX found four cases where v2 certified a card it had not checked).
    """
    out = []
    ncol = max((len(r) for r in rows), default=0)
    if not ncol:
        return out, "NOT-A-BAND-TABLE", ""
    if decl.get("kind") == "trigger-ladder":
        # A TRIGGER LADDER is not a partition: its rows are escalating conditions that may
        # overlap by design (>=24%, >=27%, >=30%). Judging it as a partition reports gaps
        # that are not defects. ⛔ This declaration names the TABLE TYPE ONLY. It asserts
        # NOTHING about whether the trigger logic is right, and this tool cannot check that.
        return out, "NOT-A-BAND-TABLE", "declared kind=trigger-ladder — table TYPE only; trigger logic NOT verified by this tool"
    cand = []
    for ci in range(ncol):
        cells = [(r[0], (r[ci] if len(r) > ci else "")) for r in rows]
        parsed = [(l, parse_interval(c)) for l, c in cells]
        n_ok = sum(1 for _, v in parsed if v)
        # A partition needs >=2 bands, so a column with ONE numeric cell is not an axis --
        # it is a prose/source table that happens to contain a number. Treating it as an
        # axis made every real graded card UNVERIFIED forever (DAEDALUS 2026-09-07).
        # The >=40% fallback keeps a genuine 2-band table whose one row is unreadable
        # visible as UNVERIFIED rather than silently dismissed.
        if n_ok >= 2 or (n_ok and n_ok / max(len(cells), 1) >= 0.4):
            cand.append((ci, cells, parsed, n_ok))
    if not cand:
        return out, "NOT-A-BAND-TABLE", ""

    name_of = lambda ci: (hdr[ci] if ci < len(hdr) else f"col{ci}").strip() or f"col{ci}"
    # An explicit declaration wins outright.
    chosen = None
    if decl.get("column"):
        for ci, cells, parsed, n in cand:
            if name_of(ci).lower() == decl["column"].lower():
                chosen = (ci, cells, parsed, n)
        if chosen is None:
            # A declaration that cannot be honored must FAIL, never fall back. Falling back
            # silently substitutes a different axis for the one the card named and then
            # reports VERIFIED about it.
            out.append(("BAD-DECLARATION",
                        f"declared axis column=\"{decl['column']}\" is not a readable band "
                        f"column in this table (candidates: "
                        + ", ".join(f"'{name_of(c[0])}'" for c in cand) + ")"))
            return out, "UNVERIFIED", ""
    if chosen is None:
        strong = [c for c in cand if c[3] >= 2]
        if len(strong) > 1:
            out.append(("AMBIGUOUS-AXIS",
                        "two or more columns could be the band axis — "
                        + " vs ".join(f"'{name_of(c[0])}' ({c[3]} intervals)" for c in strong)
                        + ". Declare it: <!-- partition-axis: column=\"X\" -->"))
            return out, "UNVERIFIED", ""
        chosen = strong[0] if strong else cand[0]

    ci, cells, parsed, n_ok = chosen
    axis = name_of(ci)
    lab = lambda t: re.sub(r"[*`]", "", t).strip() or "?"

    # EVERY row must resolve. A blank cell is not "nothing to check" — it is an unchecked row.
    bad = [(l, c) for (l, c), (_, v) in zip(cells, parsed) if v is None]
    for l, c in bad:
        why = "a BLANK interval" if not re.sub(r"[*`\s]", "", c) else "an UNREADABLE interval"
        out.append(("UNVERIFIED-ROW", f"axis '{axis}': band {lab(l)} has {why} — "
                                      f"this table is UNVERIFIED, not clean"))
    iv = [(l, v) for (l, _), (_, v) in zip(cells, parsed) if v]
    if bad:
        # ⛔ Coverage over a SUBSET of the bands is not evidence about the partition — the
        # holes left by the rows that did not parse present as GAPs that do not exist.
        # DAEDALUS 2026-09-07: the ISM card's `= 50.0 exactly` row and the NFP card's
        # `+150K to +302K` rows were unreadable, and the checker reported phantom GAPs at
        # 50 and across 0-302,000 on the remaining rows. Report the unreadable rows and
        # STOP; do not emit a coverage verdict the input cannot support.
        out.append(("COVERAGE-NOT-RUN", f"axis '{axis}': {len(bad)} of {len(cells)} rows "
                                        f"unreadable — coverage NOT evaluated (a partial band "
                                        f"set manufactures gaps that are not in the card)"))
        return out, "UNVERIFIED", f"axis '{axis}', coverage not run"
    if len(iv) < 2:
        out.append(("INSUFFICIENT", f"axis '{axis}': only {len(iv)} band(s) parsed — "
                                    f"a partition cannot be established from fewer than two"))
        return out, "UNVERIFIED", axis

    gran = decl.get("precision") or granularity([b for _, (lo, _, hi, _) in iv for b in (lo, hi)])
    spans = []
    for l, (lo, li, hi, hi_i) in iv:
        a = -INF if lo == -INF else lo_unit(lo, li, gran)
        b = INF if hi == INF else hi_unit(hi, hi_i, gran)
        if a != -INF and b != INF and a > b:
            out.append(("EMPTY-BAND", f"axis '{axis}': band {lab(l)} covers nothing"))
            continue
        spans.append((a, b, lab(l)))
    # -INF-starting bands sort first, ordered by their upper edge, so two overlapping lower
    # tails (<=199999 and <=249999) become adjacent and are compared instead of skipped.
    spans.sort(key=lambda t: (0 if t[0] == -INF else 1,
                              0 if t[0] == -INF else t[0],
                              0 if t[1] == INF else t[1]))
    fmt = lambda u: ("-inf" if u == -INF else "inf" if u == INF else f"{u * gran:,.10g}")
    # COVERAGE BY SWEEP, not by adjacent pairs. Adjacency is only correct for a set of
    # disjoint, ordered bands — the very thing being tested. With a NESTED or overlapping
    # band (`<7`, `4-6`, `3-10`) the sorted neighbour is not the relevant one, and the old
    # code reported a phantom GAP and read the wrong band as the highest. Found by the
    # membership test, not by any example: it is a whole family, not a case.
    order = sorted(spans, key=lambda t: ((0 if t[0] == -INF else 1),
                                         (0 if t[0] == -INF else t[0])))
    run_end, run_lab = None, None
    for a, b, l in order:
        if run_end is not None and a <= run_end:
            hi_ov = b if (run_end == INF or (b != INF and b < run_end)) else run_end
            out.append(("OVERLAP", f"axis '{axis}': bands {run_lab} and {l} both claim "
                                   f"{fmt(a)}" + (f" - {fmt(hi_ov)}" if hi_ov != a else "")))
        if run_end is None or b == INF or (run_end != INF and b > run_end):
            run_end, run_lab = b, l
    merged = []
    for a, b, l in order:
        if merged and (merged[-1][1] == INF or a <= merged[-1][1] + 1):
            if merged[-1][1] != INF and (b == INF or b > merged[-1][1]):
                merged[-1][1] = b
        else:
            merged.append([a, b])
    for (a1, b1), (a2, b2) in zip(merged, merged[1:]):
        out.append(("GAP", f"axis '{axis}': {fmt(b1 + 1)}"
                           + (f" - {fmt(a2 - 1)}" if a2 - 1 > b1 + 1 else "")
                           + f" is in NO BAND (precision {gran:,.10g})"))
    if merged:
        if merged[0][0] != -INF:
            out.append(("OPEN-END", f"axis '{axis}': coverage starts at {fmt(merged[0][0])} — "
                                    f"everything below is unassigned"))
        if merged[-1][1] != INF:
            out.append(("OPEN-END", f"axis '{axis}': coverage ends at {fmt(merged[-1][1])} — "
                                    f"everything above is unassigned"))
    scope = f"axis '{axis}', {len(iv)} bands, precision {gran:,.10g}, bounds as written"
    if bad:
        return out, "UNVERIFIED", scope
    return out, ("DEFECT" if out else "VERIFIED"), scope


WILDCARD = {"any", "either", "*", "-", "\u2014", "n/a", "all"}


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
    """Return 0 only when EVERY candidate band table in the card was fully verified.

    ⛔ This function reports SCOPED LINT. It never certifies a card as correct — it reports
    what it checked, what it could not check, and what it found. v2 emitted a card-level
    "PASS ... partition their axis" that a single good table could earn while a second table,
    a blank row, or an unreadable axis went unexamined.
    """
    if not os.path.exists(path):
        print(f"  ⛔ CANNOT-VERIFY: no such file: {path}")
        return 2
    text = open(path, encoding="utf-8").read()
    decl = declared_axis(text)
    tables = list(parse_tables(text))
    name = os.path.basename(path)

    results = []          # (idx, status, scope, findings)
    for i, (hdr, rows, ln) in enumerate(tables, 1):
        f, st, scope = analyze_table(hdr, rows, decl)
        f += check_cross(hdr, rows)
        if f and st == "VERIFIED":
            st = "DEFECT"
        if st != "NOT-A-BAND-TABLE":
            results.append((i, st, scope, f))

    prose, bands = check_prose(text, tables)
    verified = [r for r in results if r[1] == "VERIFIED"]
    unver    = [r for r in results if r[1] == "UNVERIFIED"]
    defect   = [r for r in results if r[1] == "DEFECT"]

    if not results:
        print(f"  ⚠️  UNVERIFIED  {name}: no band table found. Not a pass — check by hand.")
        return 2

    head = (f"  {'❌ DEFECT   ' if defect else '⚠️  UNVERIFIED' if unver else '✅ LINT-CLEAN'}  {name}: "
            f"{len(results)} band table(s) — {len(verified)} verified, "
            f"{len(unver)} unverified, {len(defect)} with defects"
            + (f", {len(prose)} prose finding(s)" if prose else ""))
    print(head)
    for i, st, scope, f in results:
        mark = {"VERIFIED": "✓", "DEFECT": "✗", "UNVERIFIED": "?"}[st]
        print(f"      [{mark}] table {i}: {st}" + (f" — {scope}" if scope else ""))
        for kind, msg in f:
            print(f"          [{kind}] {msg}")
    for kind, msg in prose:
        print(f"      [{kind}] {msg}")
    if defect or unver or prose:
        return 2
    print(f"      scope: {len(verified)} table(s) checked for gaps, overlaps and open ends. "
          f"Prose claims naming a band set + a number were cross-read against the table. "
          f"NOT checked: anything outside those tables.")
    return 0


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
""", 2, "INSUFFICIENT"),
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
""", 2, "UNVERIFIED-ROW"),
    ("CODEX 5/5: decimal axis omits 4.2", """
| Band | X | Action |
|---|---|---|
| A | <=4.1 | hold |
| B | 4.3-4.4 | hold |
| C | >=4.5 | hold |
""", 2, "GAP"),
    # ---- CODEX's second independent round, 2026-09-07 PM: SCOPE failures ---------------
    # v2 passed all 15 of the tests above while failing all four of these. They are scope
    # failures, not parser bugs: v2 emitted a card-level PASS that one good table could earn.
    ("CODEX v2 1/4: a blank interval row is an UNCHECKED row", """
| Band | X | Action |
|---|---|---|
| A | <=199999 | hold |
| B | 200000-249999 | hold |
| C | >=250000 | fire |
| D |  | unknown |
""", 2, "BLANK"),
    ("CODEX v2 2/4: an unbounded upper band swallows every later band", """
| Band | X | Action |
|---|---|---|
| A | <200000 | hold |
| B | >=200000 | arm |
| C | >=250000 | fire |
""", 2, "OVERLAP"),
    ("CODEX v2 3/4: a valid table cannot certify an incomplete second table", """
| Band | X | Action |
|---|---|---|
| A | <=199999 | hold |
| B | 200000-249999 | hold |
| C | >=250000 | fire |

## Second axis
| Band | Y | Action |
|---|---|---|
| D | >=5 | fire |
""", 2, "INSUFFICIENT"),
    ("CODEX v2 4/4: a reference column cannot certify an unreadable axis", """
| Band | X | Reference |
|---|---|---|
| A | <=199999 | <=199999 |
| B | ??? | 200000-249999 |
| C | >=250000 | >=250000 |
""", 2, "AMBIGUOUS-AXIS"),
    # ---- CODEX round 3, 2026-09-07 PM. Kept HERE, in the repo, not in /tmp: a review
    # ---- case that lives in a scratch file is not a regression test.
    ("CODEX v3 1/4: an unhonourable axis declaration must FAIL, not fall back", """<!-- partition-axis: column="MISSING" precision=1 -->
| Band | X | Action |
|---|---|---|
| A | <=199999 | hold |
| B | 200000-249999 | hold |
| C | >=250000 | fire |
""", 2, "BAD-DECLARATION"),
    ("CODEX v3 2/4: overlapping lower tails", """
| Band | X | Action |
|---|---|---|
| A | <=199999 | hold |
| B | <=249999 | arm |
| C | >=250000 | fire |
""", 2, "OVERLAP"),
    ("CODEX v3 3/4: precision 1000 must not invent overlaps on a valid partition", """<!-- partition-axis: column="X" precision=1000 -->
| Band | X | Action |
|---|---|---|
| A | <=199999 | hold |
| B | 200000-249999 | hold |
| C | >=250000 | fire |
""", 0, None),
    ("CODEX v3 4/4: nested band must not produce a phantom gap", """<!-- partition-axis: column="X" precision=1 -->
| Band | X | Action |
|---|---|---|
| A | <7 | hold |
| B | 4-6 | hold |
| C | 3-10 | hold |
""", 2, "OVERLAP"),
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


ACCEPTANCE = [
    ("valid partition must PASS",
     "| Band | X | A |\n|---|---|---|\n| A | <=199999 | h |\n| B | 200000-249999 | h |\n| C | >=250000 | f |\n", 0),
    ("known GAP must FAIL",
     "| Band | X | A |\n|---|---|---|\n| A | <=199999 | h |\n| B | 210000-249999 | h |\n| C | >=250000 | f |\n", 2),
    ("known OVERLAP must FAIL",
     "| Band | X | A |\n|---|---|---|\n| A | <=200000 | h |\n| B | 200000-249999 | h |\n| C | >=250000 | f |\n", 2),
    ("declared trigger ladder must NOT be judged as a partition",
     "<!-- partition-axis: kind=trigger-ladder -->\n| Trigger | LT share | A |\n|---|---|---|\n| T-a | >=24% | watch |\n| T-b | >=27% | restore |\n| T-c | >=30% | fire |\n", 2),
]


def acceptance_test():
    """PRODUCTION ACCEPTANCE SET (DAEDALUS 2026-09-07). The gate for trusting this tool is
    NOT 'one real card passed' — one pass is a sample of size one. It is: a valid partition
    passes, a known gap fails, a known overlap fails, and a declared trigger ladder is not
    judged as a partition at all."""
    import tempfile, io, contextlib
    print("=" * 72); print("  PRODUCTION ACCEPTANCE SET"); print("=" * 72)
    ok = True
    for nm, md, want in ACCEPTANCE:
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(md); t = f.name
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = check_card(t)
        os.unlink(t)
        good = rc == want
        ok &= good
        print(f"  {'PASS' if good else 'FAIL'}  {nm:58} rc={rc} (want {want})")
        if not good:
            print("        " + buf.getvalue().replace("\n", "\n        ").rstrip())
    print("-" * 72)
    print("  " + ("✅ ACCEPTANCE SET PASSES" if ok else "❌ ACCEPTANCE FAILURE — do not rely on this tool"))
    return 0 if ok else 2


def membership_test(trials=4000, seed=20260907):
    """INDEPENDENT MEMBERSHIP CHECK (CODEX's recommendation, 2026-09-07).

    Instead of adding more hand-picked examples — which only ever cover the cases I already
    thought of — enumerate a small declared grid, count how many bands own each value from
    the INTERVAL TEXT ITSELF, and require the checker's verdict to agree with that count:

        some value owned by 0 bands  <=>  the checker must report a GAP or an OPEN-END
        some value owned by 2+ bands <=>  the checker must report an OVERLAP

    Ground truth is computed by enumeration, not by the checker, so this covers whole
    FAMILIES of boundary cases rather than a handful of familiar ones — it is what found the
    adjacent-pair coverage bug that no example test reached.

    ⛔ SCOPE, stated because a strong test is the easiest thing to over-credit:
      COVERS      randomized INTEGER boundaries at PRECISION 1, over <=, <, >=, >, and ranges,
                  for gap / open-end / overlap detection on a single declared axis.
      DOES NOT COVER  decimal parsing · precisions other than 1 · axis DECLARATION handling
                  (honoured, unhonourable, ambiguous) · unit suffixes (186-199K) · date
                  rejection · the two-axis cross-product leg · any prose interpretation.
    Those are covered only by the named self-tests above, which are examples and therefore
    only reach the cases someone thought of. **This test supports the interval-sweep repair;
    it does not validate the checker as a whole.**
    """
    import random, itertools, tempfile, io, contextlib
    rng = random.Random(seed)
    # The oracle grid must extend BEYOND the range band endpoints are drawn from, or it
    # cannot see an unbounded end. A band set covering [0, inf) leaves everything below 0
    # unassigned — the checker says OPEN-END and a 0..10 grid calls that a false positive.
    # The first version of this test had that defect; the mismatch was in the ORACLE, and
    # tuning the checker to it would have deleted a correct finding.
    GRID = list(range(-3, 15))         # endpoints are drawn from 0..10; sentinels either side
    OPS = ["<=", "<", ">=", ">", "range"]
    bad = []
    for t in range(trials):
        nb = rng.randint(2, 4)
        specs = []
        for _ in range(nb):
            op = rng.choice(OPS)
            if op == "range":
                a = rng.randint(0, 9); b = rng.randint(a, 10)
                specs.append((f"{a}-{b}", lambda v, a=a, b=b: a <= v <= b))
            elif op == "<=":
                a = rng.randint(0, 10); specs.append((f"<={a}", lambda v, a=a: v <= a))
            elif op == "<":
                a = rng.randint(0, 10); specs.append((f"<{a}",  lambda v, a=a: v < a))
            elif op == ">=":
                a = rng.randint(0, 10); specs.append((f">={a}", lambda v, a=a: v >= a))
            else:
                a = rng.randint(0, 10); specs.append((f">{a}",  lambda v, a=a: v > a))
        counts = [sum(1 for _, f in specs if f(v)) for v in GRID]
        truth_gap = any(c == 0 for c in counts)
        truth_ovl = any(c >= 2 for c in counts)
        md = ("<!-- partition-axis: column=\"X\" precision=1 -->\n"
              "| Band | X | Action |\n|---|---|---|\n"
              + "".join(f"| {chr(65+i)} | {txt} | hold |\n" for i, (txt, _) in enumerate(specs)))
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as fh:
            fh.write(md); tmp = fh.name
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            check_card(tmp)
        out = buf.getvalue()
        os.unlink(tmp)
        said_gap = ("[GAP]" in out) or ("[OPEN-END]" in out)
        said_ovl = "[OVERLAP]" in out
        if said_gap != truth_gap or said_ovl != truth_ovl:
            bad.append((md, counts, truth_gap, truth_ovl, said_gap, said_ovl))
            if len(bad) >= 3:
                break
    print("=" * 72)
    print(f"  MEMBERSHIP TEST — {trials} random band sets over a 0..10 grid, "
          f"ground truth by enumeration")
    print("=" * 72)
    if not bad:
        print(f"  ✅ checker verdict matched enumerated ownership on all {trials} cases")
        return 0
    for md, counts, tg, to, sg, so in bad:
        print(f"  ❌ MISMATCH  truth(gap={tg}, overlap={to})  checker(gap={sg}, overlap={so})")
        print("     ownership per value 0..10:", counts)
        print("     " + md.replace("\n", "\n     "))
    print(f"  ❌ {len(bad)} mismatch(es) — the checker disagrees with enumerated membership")
    return 2


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
    if "--membership-test" in argv:
        return membership_test()
    if "--acceptance" in argv:
        return acceptance_test()
    if "--self-test" in argv:
        rc = self_test()
        rc = max(rc, membership_test())
        return max(rc, acceptance_test())
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
    print("  " + ("✅ LINT-CLEAN across all cards — every band table identified was checked "
                  "for gaps, overlaps and open ends. This is NOT a certification that the "
                  "cards are correct; see each card's scope line."
                  if worst == 0 else
                  "❌ DEFECT or UNVERIFIED — resolve before freezing the card"))
    return worst


if __name__ == "__main__":
    sys.exit(main(sys.argv))
