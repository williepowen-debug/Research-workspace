"""D:L334 / WQ-556 C two-week remeasurement of lever (a): discretionary INFO-copy trims to HENRY, LIQUID, REGINALD, SAM.
BEFORE = 2026-10-16T00:00Z .. 2026-10-30T00:00Z (14 days), AFTER = 2026-10-30T00:00Z .. 2026-11-13T00:00Z (14 days; lever in force from the 10/30 dispatch).
Measures per target desk: INFO / ACTION delivery rows, signals dispatched (route_log), INFO copies per 100 signals,
late adds (a later delivery row for the same signal and desk = a copy WALTER had to send after the first dispatch),
and strict/broad citation (same definition as research/2026-10-30_L334/measure.py) on the first 7 days of each window.
Run from repo root: python3 AGENTS/WALTER/research/2026-11-13_L334-remeasure/remeasure.py"""
import csv, re, subprocess, collections, json
ROOT = '/home/willi/Research-workspace'
W = {'BEFORE': ('2026-10-16T00:00:00Z', '2026-10-30T00:00:00Z'), 'AFTER': ('2026-10-30T00:00:00Z', '2026-11-13T00:00:00Z')}
CITE = {'BEFORE': ('2026-10-16T00:00:00Z', '2026-10-23T00:00:00Z'), 'AFTER': ('2026-10-30T00:00:00Z', '2026-11-06T00:00:00Z')}
DESKS = ['HENRY', 'LIQUID', 'REGINALD', 'SAM']
dl = list(csv.DictReader(open(f'{ROOT}/AGENTS/WALTER/routed/delivery_log.tsv', encoding='utf-8'), delimiter='\t'))
rl = [l.rstrip('\n').split('\t') for l in open(f'{ROOT}/AGENTS/WALTER/routed/route_log.tsv', encoding='utf-8')]
rl = [f for f in rl if len(f) > 1 and f[1].startswith('SIG-W-')]
EXCL = re.compile(r'(board_log|BOARD_LOG|consum|orphan|moves|disposition|audit|LIAISON|/inbox/|_INDEX|INDEX\.md|scan|ledger|receipt|census|manifest)', re.I)
STRICT = re.compile(r'(/STATUS[^/]*\.md$|/status_archive/|/workbook/KB[^/]*\.tsv$|/KB[^/]*\.tsv$|/thesis/|THESIS[^/]*\.md$)')
def cited(desk, mode):
    out = subprocess.run(['git', 'grep', '-oE', r'SIG-W-2026[0-9]{4}-[0-9]{3}', '--', f'AGENTS/{desk}/'], cwd=ROOT, capture_output=True, text=True).stdout
    ids = set()
    for line in out.splitlines():
        f, _, i = line.rpartition(':')
        if EXCL.search(f): continue
        if mode == 'strict' and not STRICT.search(f): continue
        if mode == 'broad' and not (f.endswith('.md') or re.search(r'KB[^/]*\.tsv$', f)): continue
        ids.add(i)
    return ids
C = {(d, m): cited(d, m) for d in DESKS for m in ('strict', 'broad')}
first = {}
for r in dl:
    k = (r['signal_id'], r['recipient'])
    if k not in first or r['timestamp_routed'] < first[k]: first[k] = r['timestamp_routed']
out = {}
for w, (a, b) in W.items():
    sigs = {f[1] for f in rl if a <= f[0] < b}
    rows = [r for r in dl if a <= r['timestamp_routed'] < b]
    res = {'signals': len(sigs)}
    for d in DESKS:
        info = [r for r in rows if r['recipient'] == d and r['role'] == 'INFO']
        act = [r for r in rows if r['recipient'] == d and r['role'] == 'ACTION']
        isig = {r['signal_id'] for r in info}
        late = sum(1 for r in rows if r['recipient'] == d and r['timestamp_routed'] > first[(r['signal_id'], d)])
        ca, cb = CITE[w]
        cw = {r['signal_id'] for r in info if ca <= r['timestamp_routed'] < cb}
        res[d] = {'info_rows': len(info), 'action_rows': len(act), 'info_per_100_signals': round(100 * len(isig) / max(1, len(sigs)), 1),
                  'late_adds': late, 'cite_window_info': len(cw),
                  'cited_strict': len(cw & C[(d, 'strict')]), 'cited_broad': len(cw & C[(d, 'broad')])}
    out[w] = res
json.dump({'windows': W, 'cite_windows': CITE, 'results': out}, open(f'{ROOT}/AGENTS/WALTER/research/2026-11-13_L334-remeasure/results.json', 'w'), indent=1)
for w in out:
    print(w, 'signals', out[w]['signals'])
    for d in DESKS: print(' ', d, out[w][d])
