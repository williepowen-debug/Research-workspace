"""Read-only CATO probes; run from the Git root with .venv/bin/python -B.

Uses repository sources and saved HTML, an isolated JS DOM/store stub, and
temporary build outputs. Never connects to the hosted store or writes PROME files.
"""
import ast
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

from bs4 import BeautifulSoup

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT / 'PROME/tools'))
import decision_deck as D

def git(*args):
    return subprocess.check_output(['git', *args], text=True, cwd=ROOT)

page = (ROOT / 'PROME/artifacts/decision_deck.html').read_text()
soup = BeautifulSoup(page, 'html.parser')
baseline_code = git('show', '46c6b938b^:PROME/tools/decision_deck.py')
baseline_page = git('show', '46c6b938b^:PROME/artifacts/decision_deck.html')
old_soup = BeautifulSoup(baseline_page, 'html.parser')
out = {'head': git('rev-parse', 'HEAD').strip(), 'reviewed_change': '46c6b938b', 'basis': {}}
for name in ['PROME/tools/decision_deck.py', 'PROME/artifacts/decision_deck.html',
             'PROME/registry/WQ_EXPLAINERS.tsv', 'PROME/WILL_QUEUE.md',
             'PROME/BOOT.md', 'PROME/tools/tests/ACCEPTANCE_deck_changeB_2026-10-09.md']:
    out['basis'][name] = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
functions = ['parse_options', 'offered_options', 'validate_options', 'render_unit']
def selected(source):
    return {n.name: ast.dump(n) for n in ast.parse(source).body
            if isinstance(n, ast.FunctionDef) and n.name in functions}
assert selected(baseline_code) == selected((ROOT / 'PROME/tools/decision_deck.py').read_text())
out['preserved_functions'] = functions
out['preserved_fragments'] = {}
for selector in ['ul.opts', 'p.src', '.tapbtns']:
    common_ids = {c['id'] for c in old_soup.select('#owed article.card')} & {c['id'] for c in soup.select('#owed article.card')}
    before, after = ([str(x) for c in s.select('#owed article.card') if c['id'] in common_ids
                      for x in c.select(selector)] for s in [old_soup, soup])
    # Pinning changes card order; compare controls by content, preserving duplicates.
    assert sorted(before) == sorted(after), selector
    out['preserved_fragments'][selector] = len(after)
assert D.UI_JS.strip() in page and D.RULING_JS.strip() in page
out['saved_page_scripts_equal_tested_code'] = True
cards = soup.select('#owed article.card')
out['cards'] = len(cards)
out['cards_removed_since_prior_saved_page'] = sorted({c['id'] for c in old_soup.select('#owed article.card')} - {c['id'] for c in cards})
out['pinned'] = [c['data-wq'] for c in cards if c['data-pin'] == '1']
out['expanded_caveat_cards'] = [c['data-wq'] for c in cards if not c.select_one('details.more')]
out['card_source_links'] = [a['href'] for c in cards for a in c.select('a[href]')]
for group in soup.select('#owed .grp'):
    flags = []
    for c in group.find_next_siblings():
        if 'grp' in c.get('class', []): break
        if c.name == 'article': flags.append(c['data-pin'])
    assert flags == sorted(flags, reverse=True)
out['pinned_first_in_each_group'] = True
out['front_examples'] = {}
for n in ['314', '375']:
    c = BeautifulSoup(str(soup.select_one('#wq-' + n)), 'html.parser')
    for hidden in c.select('details'): hidden.decompose()
    out['front_examples'][n] = c.get_text(' ', strip=True)
out['clock_counterexamples'] = {}
for raw in ['2026-10-14 (re-dated 10/9 17:06 ET; no deadline time set)',
            '2026-10-14 09:45–10:30 ET', '2026-10-14 9:45am–10:30 ET']:
    clock = D.clock_of({'by_raw': raw})
    out['clock_counterexamples'][raw] = {'clock': clock, 'pill': D.due_pill('2026-10-14', 5, False, clock=clock)}
with tempfile.TemporaryDirectory(prefix='cato-deck-review-') as td:
    result = D.build(dt.date(2026, 10, 9), Path(td) / 'owed.html',
                     reference_out=Path(td) / 'reference.html',
                     owed_url=D.OWED_ARTIFACT_URL,
                     reference_url='https://claude.ai/artifact/Wt4aYbC8gqQic2aLEtrWGr')
    rebuilt = Path(result['out']).read_text()
    def normalize(text):
        # Only generated build identity/stamp varies; content timestamps are untouched.
        doc = BeautifulSoup(text, 'html.parser')
        ident = doc.body['data-build']
        sha, stamp = ident.split('·', 1)
        return text.replace(ident, 'BUILD').replace(stamp, 'STAMP').replace(sha, 'SHA')
    out['rebuild_matches_saved_except_build_identity'] = normalize(page) == normalize(rebuilt)
    assert out['rebuild_matches_saved_except_build_identity']

JS = r'''
const vm = require('node:vm'), assert = require('node:assert/strict');
const src = JSON.parse(require('node:fs').readFileSync(0,'utf8'));
function el(dataset={}) {
 const cs=new Set(); return {dataset,hidden:false,textContent:'',listeners:{},
 classList:{add(...x){x.forEach(v=>cs.add(v))},remove(...x){x.forEach(v=>cs.delete(v))},contains:x=>cs.has(x),toggle(x,on){on?cs.add(x):cs.delete(x)}},
 setAttribute(){},addEventListener(k,fn){this.listeners[k]=fn},querySelector(){return null},querySelectorAll(){return []}};
}
(async()=>{
 let tested=0;
 for(const chip of src.chips) {
  const cards=src.cards.map(x=>el(x)), chips=src.chips.map(x=>el({chip:x}));
  const values=new Map([['deck.chip.owed',chip]]);
  const DateFixed=class extends Date {constructor(...a){super(...(a.length?a:['2026-10-09T21:45:00Z']))}};
  vm.runInNewContext(src.ui,{Date:DateFixed,document:{body:{dataset:{view:'owed'}},
    querySelector:()=>({querySelectorAll:()=>chips}),querySelectorAll:s=>s==='#owed .card'?cards:[],getElementById:()=>null},
    localStorage:{getItem:k=>values.get(k),setItem:(k,v)=>values.set(k,v)},location:{hash:''},window:{}});
  for(const c of cards) {
   const d=c.dataset, expected=d.pin==='1'||chip==='All'||d.kchip===chip||d.dom.split(' ').includes(chip);
   assert.equal(!c.classList.contains('chiphide'),expected);tested++;
  }
 }
 const state=el(), card=el(); card.id='wq-7';card.querySelector=()=>state;
 const store=el();let snapshot;
 const db={collection(){return {onSnapshot(fn){snapshot=fn},doc(){throw Error('no writes authorized in probe')}}}};
 vm.runInNewContext(src.rulings,{document:{body:{dataset:{build:'probe'}},querySelectorAll:()=>[],
   getElementById:id=>id==='store'?store:id==='wq-7'?card:id==='toast'?el():null},
   window:{claude:{use:()=>Promise.resolve(db)}},setTimeout:()=>0,clearTimeout(){}});
 await new Promise(setImmediate);
 const base={wq:'7',verdict:'APPROVE',ts:'2026-10-09T21:00:00Z',consumed:true,consumed_at:'2026-10-09T21:15:00Z',consumed_by:'probe'};
 const render=extra=>{snapshot({docs:[{data:()=>({...base,...extra})}]});return state.textContent};
 const received=render({}), recorded=render({recorded_as:'WQ-7 APPROVED; owner action pending'});
 assert(received.includes('receipt is not execution'));
 assert(!recorded.includes('receipt is not execution'));
 assert(recorded.includes('③ Recorded in the queue as:'));
 process.stdout.write(JSON.stringify({filter_checks:tested,received,recorded,
   recorded_time_labels:recorded.match(/\d+\/\d+, \d+:\d+ [AP]M ET/g)}));
})().catch(e=>{console.error(e);process.exit(1)});
'''
runtime = subprocess.run(['node', '-e', JS], input=json.dumps({
    'ui': D.UI_JS, 'rulings': D.RULING_JS,
    'chips': [c['data-chip'] for c in soup.select('.chipbtn')],
    'cards': [{key: c['data-' + key] for key in ['pin', 'kchip', 'dom', 'due']} for c in cards],
}), text=True, capture_output=True)
if runtime.returncode:
    raise RuntimeError(runtime.stderr)
out['independent_runtime'] = json.loads(runtime.stdout)
print(json.dumps(out, indent=2, ensure_ascii=False))
