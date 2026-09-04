#!/usr/bin/env python3
"""
soi_nonaccrual.py — extract non-accrual rows from a BDC Schedule of Investments (10-Q/10-K).

WHY THIS EXISTS
  A naive grep for the non-accrual footnote marker over-counts badly: the marker is
  re-used in the COMPARATIVE prior-period schedule and in EVERY unconsolidated JV
  schedule in the same filing. BROCK's first attempt returned 23 issuers / 69 loans
  against a stated 15 / 25 (2026-08-28, BCRED Q2-2026). The bug was SCOPE, not parsing.

THE FIX (the whole point of this tool)
  Each schedule is terminated by its own footnote-definition block. So the CURRENT-period
  fund schedule = [first SOI header] .. [first footnote block defining the marker for the
  CURRENT period end]. Everything after that is comparative or JV and must be excluded.

VALIDATED 2026-09-03 on BCRED Q2-2026 (acc 0001803498-26-000048):
  25 loans / 15 issuers == the filing's own stated figures, exact.

TWO SUBTLETIES THAT SILENTLY CORRUPT COUNTS — both handled, both learned the hard way:
  1. INDUSTRY-HEADING GLUE. The first issuer in each industry section is preceded by the
     industry heading with no delimiter once HTML is flattened, e.g.
     "Building Products ES Group Holdings III, Ltd." Handled by suffix-collapse: if a
     captured name ends with another captured name, keep the shorter. Names with no
     shorter twin are reported with a PREFIX? flag for human review rather than guessed.
  2. ONE PORTFOLIO COMPANY, SEVERAL BORROWING ENTITIES. BCRED lists
     "CFCo, LLC (Benefytt Technologies, Inc.)" and "Daylight Beta Parent, LLC (Benefytt
     Technologies, Inc.)" as separate rows. The issuer of record is the PARENTHETICAL.
     Counting the LLCs separately gives 16 issuers where the filing says 15. Any tool
     that counts borrowing entities will over-state issuer counts on restructured credits.

USAGE
  python3 soi_nonaccrual.py <flattened_text_file> --marker 17 --period "June 30, 2026"
  (flatten with: strip tags, unescape entities, collapse whitespace)
"""
import re, sys, argparse

COMPANY_SUFFIX = (r"(?:Inc|LLC|L\.L\.C|Corp|Corporation|Ltd|Limited|L\.?P|LP|BV|B\.V|"
                  r"S\.a\.r\.l|GmbH|PLC|Holdings|Group|Company|Co|AB|AS|NV|N\.V|Trust|Partners)")

# Header wording varies by filer and the FIRST match is often a table-of-contents line,
# not the schedule. Both bugs found 2026-09-03 on the first reuse (BCRED -> ARCC):
# ARCC writes "Consolidated SchedulES of Investments" (plural) and its first occurrence
# is a TOC entry ~126k chars before the real schedule. So: match singular OR plural,
# case-insensitively, and take the first header actually FOLLOWED BY SCHEDULE COLUMNS.
COLUMN_WORDS = re.compile(r'(Interest Rate|Maturity|Par Amount|Principal|Fair Value|Acquisition Date)', re.I)

def current_period_segment(t, marker, period):
    """Return (start,end) of the CURRENT-period fund schedule, or None."""
    fn = re.compile(r'\(' + str(marker) + r'\)\s*[^.]{0,140}?' + re.escape(period))
    hdr = re.compile(r'(?:Consolidated\s+)?Schedules?\s+of\s+Investments', re.I)
    first_fn = fn.search(t)
    if not first_fn:
        return None
    for m in hdr.finditer(t):
        if m.start() >= first_fn.start():
            break
        # a TOC line has no schedule column headers right after it
        if len(COLUMN_WORDS.findall(t[m.end():m.end() + 600])) >= 2:
            return (m.start(), first_fn.start())
    return None

def extract(seg, marker):
    grp = re.compile(r'(?:\(\d{1,2}\)\s*){1,12}')
    name_re = re.compile(
        r"([A-Z][A-Za-z0-9&'’\.\-]*(?:[ ,][A-Za-z0-9&'’\.\-/]+){0,8}?"
        r"(?:,?\s*" + COMPANY_SUFFIX + r"\.?)(?:\s*\([^)]{3,60}\))?)\s*$")
    # par/cost/FV: anchor AFTER the maturity date, else the regex silently grabs the
    # NEXT row's columns. Caught 2026-09-03 by a sanity check (FV/par came out at
    # 26,726c). Any value failing 0 < FV <= 1.5*par is reported, never published.
    val = re.compile(r'\d{1,2}/\d{1,2}/\d{4}\s+(?:(?:\$|EUR|GBP|USD)\s*)?([\d,]+)'
                     r'\s+(?:\$\s*)?([\d,]+)\s+(?:\$\s*)?([\d,]+)\s+([\d.]+)\s*%?')
    rows = []
    for m in grp.finditer(seg):
        if not re.search(r'\(' + str(marker) + r'\)', m.group(0)):
            continue
        pre = seg[max(0, m.start() - 240):m.start()]
        cut = 0
        for n in re.finditer(r'\d[\d,\.]*\s*%?|\$|EUR|GBP|USD', pre):
            cut = max(cut, n.end())
        cand = pre[cut:].strip(' ,')
        nm = name_re.search(cand)
        tail = seg[m.end():m.end() + 400]
        v = val.search(tail)
        par = cost = fv = None
        if v:
            f = lambda x: int(x.replace(',', ''))
            par, cost, fv = f(v.group(1)), f(v.group(2)), f(v.group(3))
            if not (par > 0 and 0 <= fv <= par * 1.5):
                par = cost = fv = None          # implausible -> report, never publish
        rows.append({'name': nm.group(1).strip() if nm else None,
                     'raw': cand[-90:], 'marks': m.group(0).strip(),
                     'par': par, 'cost': cost, 'fv': fv,
                     'tail': tail[:130]})
    return rows

def collapse(rows):
    """Suffix-collapse industry glue; resolve parenthetical parent as issuer of record."""
    names = sorted({r['name'] for r in rows if r['name']}, key=len)
    canon = {}
    for n in names:
        base = next((s for s in names if s != n and n.endswith(s) and len(s) < len(n)), n)
        canon[n] = base
    for r in rows:
        if r['name']:
            r['canonical'] = canon[r['name']]
            par = re.search(r'\(([^)]{3,60})\)\s*$', r['canonical'])
            r['issuer_of_record'] = par.group(1).strip() if par else r['canonical']
            r['prefix_suspect'] = (canon[r['name']] == r['name']
                                   and sum(1 for x in names if x.endswith(r['name'])) == 1
                                   and len(r['name'].split()) > 4)
    return rows

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('textfile'); ap.add_argument('--marker', default='17')
    ap.add_argument('--period', required=True)
    ap.add_argument('--expect-loans', type=int); ap.add_argument('--expect-issuers', type=int)
    a = ap.parse_args()
    t = open(a.textfile, encoding='utf-8', errors='replace').read()
    span = current_period_segment(t, a.marker, a.period)
    if not span:
        print("FAIL: could not locate the current-period schedule", file=sys.stderr); sys.exit(2)
    seg = t[span[0]:span[1]]
    rows = collapse(extract(seg, a.marker))
    unparsed = [r for r in rows if not r['name']]
    issuers = sorted({r['issuer_of_record'] for r in rows if r['name']})
    print(f"segment {span[0]}..{span[1]} ({len(seg):,} chars)")
    print(f"LOANS={len(rows)}  ISSUERS={len(issuers)}  unparsed={len(unparsed)}")
    print(f"{'issuer':<40}{'loans':>6}{'par':>12}{'cost':>12}{'FV':>12}{'FV/par':>9}")
    tp = tf = 0
    for i in issuers:
        rs = [r for r in rows if r.get('issuer_of_record') == i]
        pv = [r for r in rs if r['par'] is not None]
        par = sum(r['par'] for r in pv); cost = sum(r['cost'] for r in pv)
        fv = sum(r['fv'] for r in pv); tp += par; tf += fv
        flag = " PREFIX?" if any(r.get('prefix_suspect') for r in rs) else ""
        part = " PARTIAL" if len(pv) != len(rs) else ""
        cents = f"{fv/par*100:>7.1f}c" if par else "      --"
        print(f"{i[:39]:<40}{len(rs):>6}{par:>12,}{cost:>12,}{fv:>12,}{cents}{flag}{part}")
    if tp:
        print(f"{'TOTAL':<40}{len(rows):>6}{tp:>12,}{'':>12}{tf:>12,}{tf/tp*100:>8.1f}c")
    for r in unparsed:
        print(f"   ??? unparsed: ...{r['raw']}")
    ok = True
    if a.expect_loans is not None:
        ok &= len(rows) == a.expect_loans
        print(f"loans {len(rows)} vs stated {a.expect_loans}: {'MATCH' if len(rows)==a.expect_loans else 'MISMATCH'}")
    if a.expect_issuers is not None:
        ok &= len(issuers) == a.expect_issuers
        print(f"issuers {len(issuers)} vs stated {a.expect_issuers}: {'MATCH' if len(issuers)==a.expect_issuers else 'MISMATCH'}")
    if a.expect_loans is not None or a.expect_issuers is not None:
        print("VALIDATION:", "PASS" if ok else "FAIL — do NOT publish the list until reconciled")
        sys.exit(0 if ok else 1)

if __name__ == '__main__':
    main()
