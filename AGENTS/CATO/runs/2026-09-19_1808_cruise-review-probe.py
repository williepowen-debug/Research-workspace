"""Pinned arithmetic and read-only intake census; not a market-data certification."""
import ast
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[3]
REV = '1e3f596abc8840a987e2e3f73901f8d61b722a60'
def read(path):
    return subprocess.check_output(['git', 'show', REV + ':' + path], cwd=ROOT, text=True)

print('Reviewed revision:', REV)
for name in ('STATUS.md', 'TRADE.md', 'WATCHLIST_CCL_PREANNOUNCE.md',
             'domain/CRUISE_TERM_SET.md', 'workbook/KB.tsv', 'workbook/VX.tsv'):
    value = read('AGENTS/CRUISE/' + name)
    print(hashlib.sha256(value.encode()).hexdigest(), name)

base_c, base_r = 23.48, 265.55
c = [22.75, 22.56, 22.11, 22.35, 22.17, 21.84]
# Recover RCL cents from CRUISE's own reported 9/3-base percentages.
reported_r = [-3.8448, -6.1194, -4.3796, -5.9537, -7.4336]
r = [260.14] + [round(base_r * (1 + x / 100), 2) for x in reported_r]
print('RCL cents reconstructed from owner percentages:', r)
daily_wins = cumulative_wins = 0
for i in range(1, 6):
    cd, rd = 100 * (c[i] / c[i-1] - 1), 100 * (r[i] / r[i-1] - 1)
    excess = 100 * (r[i] / base_r - c[i] / base_c)
    daily_wins += cd > rd
    cumulative_wins += excess < 0
    print(f'9/{13+i}: CCL daily={cd:.4f}% RCL daily={rd:.4f}% cumulative excess DD={excess:.4f}pp')
print('CCL daily wins:', daily_wins, 'negative cumulative readings:', cumulative_wins)
threshold = 33.45 * .65
print('CCL threshold:', threshold, 'distance dollars:', 21.84-threshold,
      'distance / threshold pct:', 100 * (21.84/threshold-1))
print('Weekly pct:', {k: round(100*(b/a-1), 4) for k,a,b in
      [('CCL',22.75,21.84),('RCL',260.14,245.81),('NCLH',14.82,14.12)]})
print('2025 deposits sequential pct:', round(100*(7.1/8.5-1), 4))

lane = Path('/home/willi/Research-Intake')
total = hits = 0
for day in ('11', '14', '15', '16', '17'):
    path = lane / f'data/2026-09-{day}/news.json'
    raw = path.read_bytes()
    items = json.loads(raw)['items']
    matched = [x for x in items if 'CRUISE' in x.get('agents', []) or x.get('label') == 'cruise-operators']
    total += len(items)
    hits += len(matched)
    print(path, hashlib.sha256(raw).hexdigest(), 'items=',len(items), 'CRUISE=',len(matched))
    for x in matched:
        print(' ', x['title'])
print('Five stored runs:', total, 'items;', hits, 'CRUISE-labeled items')
cfg = lane / 'scripts/newsweep_config.py'
tree = ast.parse(cfg.read_text())
for node in tree.body:
    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'WATCH_FOR' for t in node.targets):
        print('WATCH_FOR contains CRUISE:', 'CRUISE' in ast.literal_eval(node.value))
print('Sep 18 stored news.json exists:', (lane/'data/2026-09-18/news.json').exists())
