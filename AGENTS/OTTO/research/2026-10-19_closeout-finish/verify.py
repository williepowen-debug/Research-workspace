"""One-off closeout receipt, not a new monitor or a research/source validator.

Checks explicit event identities/date classes, unresolved prediction states/current
confidence and the named conviction claims. Semantic judgments for each event are
recorded in event_review.json after reading both complete tables.
"""
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

B = Path(__file__).resolve().parent
D = B.parents[1]
REPO = D.parents[1]
status = (D/'STATUS.md').read_text()
thesis = (D/'thesis/THESIS.md').read_text()
calendar = list(csv.DictReader((D/'docket/CATALYSTS.tsv').open(), delimiter='\t'))
timeline = status.split('## CRITICAL TIMELINE', 1)[1].split('\n---', 1)[0]
mirror = []
for line in timeline.splitlines():
    if re.match(r'\| ~?\d{4}-\d{2}-\d{2}', line):
        cells = [x.strip() for x in line.strip('|').split('|')]
        mirror.append(cells)
reviews = json.loads((B/'event_review.json').read_text())
assert len(calendar) == len(mirror) == len(reviews) == 32
assert {r['canonical_row'] for r in reviews} == set(range(1,33))
assert {r['status_row'] for r in reviews} == set(range(1,33))
event_results = []
for review in reviews:
    c = calendar[review['canonical_row']-1]
    m = mirror[review['status_row']-1]
    assert review['canonical_anchor'] in c['event'], review['identity']
    assert review['mirror_anchor'] in m[1], review['identity']
    assert c['date'] == re.search(r'\d{4}-\d{2}-\d{2}',m[0])[0]
    assert c['date_class'] in m[2], review['identity']
    assert m[0].startswith('~') == (c['date_class']=='modeled')
    event_results.append({**review, 'date': c['date'],
                          'date_class': c['date_class'], 'result':'PASS'})
preds = list(csv.DictReader((D/'thesis/PREDICTIONS.tsv').open(),delimiter='\t'))
section = status.split('## PREDICTIONS (formal',1)[1].split('### Signal Triggers',1)[0]
pm = {}
for line in section.splitlines():
    match = re.match(r'\| (?:\*\*)?(OTTO-\d+)',line)
    if match: pm[match[1]] = line
unresolved = {r['ID']:r for r in preds if r['Status'] not in ['CONFIRMED','FALSIFIED']}
assert set(pm) == set(unresolved)
claim_reviews = json.loads((B/'prediction_claim_review.json').read_text())
assert set(claim_reviews) == set(unresolved)
prediction_results = []
for key,r in unresolved.items():
    assert r['Status'] in pm[key],key
    current = re.match(r'\d+%',r['Confidence'])[0]
    assert current in pm[key],(key,current)
    prediction_results.append({'id':key,'status':r['Status'],
                               'current_confidence':current,'resolve_date':r['Resolve_Date'],
                               'manual_claim_review':claim_reviews[key], 'result':'PASS'})
conv = thesis.split('**Conviction (decomposed):**',1)[1].split('**Current state',1)[0]
sm = status.split('## THESIS',1)[1].split('\n---',1)[0]
checks = {
    'pattern_HIGH': ('Pattern / direction: HIGH' in conv and 'HIGH conviction' in sm),
    'recovery_HIGH': ('Fraud-recovery magnitude (idiosyncratic): HIGH' in conv and
                      'fraud-recovery magnitude' in sm and 'HIGH conviction' in sm),
    'Tricolor_mechanism_HIGH': ('AT TRICOLOR: HIGH' in conv and 'at Tricolor: HIGH' in sm),
    'general_skip_LOW': ('GENERAL deep-subprime phenomenon: MEDIUM → LOW' in conv and
                        'general deep-subprime: LOW' in sm),
    'funding_DISCONFIRMED': ('Systemic-funding-transmission magnitude: LOW / DISCONFIRMED' in conv and
                           'systemic-transmission legs are DISCONFIRMED' in sm and 'funding (Jul 4' in sm),
    'bank_DISCONFIRMED': ('Bank-contagion-transmission magnitude: LOW / DISCONFIRMED' in conv and
                         'bank contagion (Aug 14' in sm),
    'Carvana_LOWER_carved_out': ('Carvana sub-thesis: LOWER' in conv and 'LOWER conviction' in sm and
                                'Not in the confirmed-case count' in sm),
    'SDT_original_three_total': ('next two quarterly runs' in conv and
                                'next TWO quarterly REFUTEs =3consecutive total' in sm),
}
assert all(checks.values()),checks
operational_calendar = '\n'.join(r[k] for r in calendar for k in ['event','what_to_check','threshold_signal'])
for stale in ['Feb-18 pattern','The finance line is the whole GPU story',
              'EART 2026-4 absent =','As the 10-15 row.',
              'falsified on substance-after-resolve']:
    assert stale not in operational_calendar,stale
# Preserve event dates, classifications, priority, recipients and the forecast ledger.
prior = subprocess.check_output(['git','show','990753244:AGENTS/OTTO/docket/CATALYSTS.tsv'],cwd=REPO,text=True)
old = list(csv.DictReader(prior.splitlines(),delimiter='\t'))
for a,c in zip(old,calendar):
    for k in ['date','date_class','priority','who_cares']:assert a[k]==c[k],(k,a['event'])
pred_before = subprocess.check_output(['git','show','990753244:AGENTS/OTTO/thesis/PREDICTIONS.tsv'],cwd=REPO)
assert pred_before == (D/'thesis/PREDICTIONS.tsv').read_bytes()
assert (D/'STATUS.md').stat().st_size < 32550*.70
sources = ['CLAUDE.md','STATUS.md','thesis/THESIS.md','thesis/PREDICTIONS.tsv',
           'docket/CATALYSTS.tsv','MEMORY.md','LAST_COMPLETION.md','LESSONS.md']
result = {'checked_at_utc':datetime.now(timezone.utc).isoformat(),
          'events':event_results,'predictions':prediction_results,'conviction_checks':checks,
          'operational_stale_guidance_checks':'PASS','prediction_ledger_byte_identical_to_s034':True,
          'source_sha256':{p:hashlib.sha256((D/p).read_bytes()).hexdigest() for p in sources},
          'manual_review':'Event identity AND date/class/meaning reviewed; full claim text and '
                          'omitted qualifiers judged against canonical record. No new source retrieval, '
                          'full-thesis causal audit or independent cold read is implied.',
          'lesson_promotion':'Completed in LESSON_PROMOTION.md; no new class/file/index change.',
          'exceptions':['Push withheld by Will instruction',
                        'Recipient consumption/native fleet transport and CATO OR1 closure unverified',
                        'Scheduled research and fullv1.6 remain separate; see RECEIPT.md']}
(B/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS:32 dated/classified event identities,8 prediction states/current confidences, '
      '8 conviction/rule checks; no event-date or forecast-ledger change.')
