#!/usr/bin/env python3
"""Generate STATUS.md's two mirror tables FROM canon, between GEN markers.

WHY (2026-10-15, S54; spec research/2026-10-15_CLOSEOUT_CHECK_BUILD_SPEC.md item 2).
Until S53 the STATUS open-challenge table and the prediction tally were typed by
hand as CLAIMS about workbook/CHALLENGES.tsv and workbook/PREDICTIONS.tsv. At the
S53 boot the table showed 11 open rows against 6 in canon and the tally said 1
ACTIVE against 2. Checking a hand-written mirror finds the rows someone named;
generating it fixes the class (finding_hand_fixing_named_rows_is_not_fixing_the_class).

BLOCKS (markers are HTML comments, invisible when rendered):
  <!-- GEN:challenges -->  … table of every non-RESOLVED CHALLENGES.tsv row …  <!-- /GEN:challenges -->
  <!-- GEN:tally -->       … one tally line off PREDICTIONS.tsv …                <!-- /GEN:tally -->
Prose outside the markers (live notes, headlines) is RED's and is never touched.

USAGE
  status_mirrors.py --write    regenerate both blocks in place (the only writing path)
  status_mirrors.py --check    rc 0 if both blocks equal a fresh generation (ignoring the
                               stamp line) · rc 1 drift · rc 2 markers missing / canon unreadable
A bare call, --help or an unknown flag refuses (argparse) and writes nothing.
closeout_check.py (a)/(b) reads the generated output, so the two agree by construction;
the check still runs because a hand edit inside the markers is the failure this guards.

Never parse RED's TSVs with the csv module — split on tab.
"""
import argparse
import datetime as dt
import re
import sys
from pathlib import Path

RED = Path(__file__).resolve().parents[1]
STATUS = RED / 'STATUS.md'
CHG = RED / 'workbook' / 'CHALLENGES.tsv'
PRED = RED / 'workbook' / 'PREDICTIONS.tsv'
STAMP_PREFIX = '*Generated '


def tsv(path):
    lines = [l for l in path.read_text(encoding='utf-8').replace('\r\n', '\n').split('\n')
             if l.strip() and not l.startswith('#')]
    hdr = lines[0].split('\t')
    rows = []
    for l in lines[1:]:
        c = l.split('\t')
        rows.append({hdr[i]: (c[i] if i < len(c) else '') for i in range(len(hdr))})
    return rows


def cell(s, n):
    # display only: RED's TSV cells carry literal quotes (never csv-parsed); a cell that was
    # once csv-quoted shows as "…""…""…" — unquote for the rendered table, canon untouched
    s = s.replace('|', '/').replace('\n', ' ').replace('""', '"').strip().strip('"').strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + '…'


def gen_challenges(today):
    rows = tsv(CHG)
    open_rows = [r for r in rows if not r['Status'].startswith('RESOLVED')]
    out = ['| ID | Target | Grade | Status | Re-review | Key finding (canon, truncated) |',
           '|---|---|---|---|---|---|']
    for r in open_rows:
        d = re.match(r'(\d{4})-(\d{2})-(\d{2})', r['Resolved_Date'].strip())
        rr = '%d/%d' % (int(d.group(2)), int(d.group(3))) if d else '⚠️ none'
        out.append('| **%s** | %s | %s | %s | %s | %s |' % (
            r['CHG_ID'], cell(r['Target'], 44), r['Grade'].strip(), r['Status'].strip(), rr,
            cell(r['Key_Finding'], 120)))
    out.append('')
    out.append('%sfrom canon %s by `scripts/status_mirrors.py`: %d rows, %d open, %d RESOLVED*. '
               'Do not hand-edit between the markers; `boot.py` §④ lists the open set live.*'
               % (STAMP_PREFIX, today, len(rows), len(open_rows), len(rows) - len(open_rows)))
    return '\n'.join(out)


def gen_tally(today):
    rows = tsv(PRED)
    c = w = 0
    active, unk = [], []
    for r in rows:
        st = r['Status'].strip()
        if st == 'ACTIVE':
            active.append('%s %s' % (r['Pred_ID'], cell(r['Timeframe'], 24)))
        elif st == 'RESOLVED':
            m = re.search(r'\b(CORRECT|WRONG)\b', r['Outcome'])
            if not m:
                unk.append(r['Pred_ID'])
            elif m.group(1) == 'CORRECT':
                c += 1
            else:
                w += 1
        else:
            unk.append(r['Pred_ID'])
    line = ('**TALLY %s (generated off canon TSV, %d rows): %d CORRECT / %d WRONG / %d ACTIVE (%s).**'
            % (today, len(rows), c, w, len(active), '; '.join(active) or 'none'))
    if unk:
        line += ' ⚠️ UNCLASSIFIED (no CORRECT/WRONG token): %s' % ', '.join(unk)
    return line


def blocks(text):
    out = {}
    for name in ('challenges', 'tally'):
        pat = re.compile(r'(<!-- GEN:%s -->\n)(.*?)(\n<!-- /GEN:%s -->)' % (name, name), re.S)
        m = pat.search(text)
        if not m:
            return None
        out[name] = (m, pat)
    return out


def strip_stamp(block):
    return '\n'.join(l for l in block.split('\n') if not l.startswith(STAMP_PREFIX)).strip()


def main():
    ap = argparse.ArgumentParser(description='Generate STATUS.md mirror blocks from canon.')
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--write', action='store_true')
    g.add_argument('--check', action='store_true')
    a = ap.parse_args()
    if not (STATUS.exists() and CHG.exists() and PRED.exists()):
        print('STATUS-MIRRORS 2 CANNOT RUN: STATUS.md / CHALLENGES.tsv / PREDICTIONS.tsv missing')
        return 2
    text = STATUS.read_text(encoding='utf-8')
    found = blocks(text)
    if found is None:
        print('STATUS-MIRRORS 2 CANNOT RUN: GEN markers missing in STATUS.md (need GEN:challenges and GEN:tally pairs)')
        return 2
    today = dt.date.today().isoformat()
    fresh = {'challenges': gen_challenges(today), 'tally': gen_tally(today)}
    drift = [n for n, (m, _) in found.items() if strip_stamp(m.group(2)) != strip_stamp(fresh[n])]
    if a.check:
        if drift:
            print('STATUS-MIRRORS 1 DRIFT: %s block(s) differ from a fresh generation — run --write, never hand-edit' % ', '.join(drift))
            return 1
        print('STATUS-MIRRORS 0 OK: both blocks equal a fresh generation off canon')
        return 0
    new = text
    for n, (m, pat) in found.items():
        new = pat.sub(lambda mm, n=n: mm.group(1) + fresh[n] + mm.group(3), new, count=1)
    if new != text:
        STATUS.write_bytes(new.encode('utf-8'))
    print('STATUS-MIRRORS wrote %s (%s)' % (', '.join(fresh), 'changed: ' + ', '.join(drift) if drift else 'content unchanged, stamp refreshed'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
