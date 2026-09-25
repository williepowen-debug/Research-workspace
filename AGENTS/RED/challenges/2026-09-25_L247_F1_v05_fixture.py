"""RED S47 — logic fixture of L247 spec v0.5 §4 (i)(ii)(v)(vi)(vii)(viii) AS WRITTEN,
over the ACCEPTED event files (no replay engine; reads payloads directly). Not a build."""
import json, glob, hashlib
from decimal import Decimal as D
Q, F = {}, {}
for f in glob.glob('KERNEL/shadow/events/*/*/*.json'):
    d = json.load(open(f)); p = d['payload']
    if d['event_type'] == 'QuestionRegistered': Q[p['question_id']] = p
    if d['event_type'] in ('ForecastSubmitted', 'ForecastAmended'):
        F[(p['forecast_id'], p['forecast_version'])] = (d['event_id'], p)
LABELS = sorted({'YES', 'NO', 'AMBIGUOUS'})
def canon(e):
    obj = {k: e[k] for k in ('probability_vector', 'source_masses', 'normalization')}
    obj['outcome_map'] = sorted(e['outcome_map'], key=lambda r: r['branch'])
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()).hexdigest()
def check(e):
    # (i) event is the submission event of forecast_id at forecast_version  [AS WRITTEN: no question binding]
    k = (e['forecast_id'], e['forecast_version'])
    if k not in F or F[k][0] != e['forecast_event_id']: return 'VECTOR_EVENT_UNKNOWN'
    # (ii) vector[YES] == THAT version's scalar
    if D(e['probability_vector']['YES']) != D(str(F[k][1]['probability'])): return 'VECTOR_CONTRADICTS_EVENT'
    pv = {l: D(v) for l, v in e['probability_vector'].items()}
    if sum(pv.values()) != 1: return 'SIGMA'
    # (v)
    om = e['outcome_map']
    if len({r['branch'] for r in om}) != len(om): return 'VECTOR_MAP_MISMATCH'
    for l in pv:
        if sum((D(r['mass']) for r in om if r['outcome'] == l), D(0)) != pv[l]: return 'VECTOR_MAP_MISMATCH'
    if set(e['source_masses']) != {r['branch'] for r in om}: return 'VECTOR_MAP_MISMATCH'
    if e['normalization']['method'] == 'NONE' and any(D(e['source_masses'][r['branch']]) != D(r['mass']) for r in om): return 'VECTOR_MAP_MISMATCH'
    # (vi) pin -> form -> alpha/beta, against the ENTRY's question rule
    rule = Q[e['question_id']]['resolution_rule']
    if e['resolution_rule_sha256'] != hashlib.sha256(rule.encode()).hexdigest(): return 'VECTOR_RULE_PIN_STALE'
    if not any(f'({r["branch"]}) -> {l}' in rule for r in om for l in LABELS): return 'VECTOR_RULE_FORM_ABSENT'
    for r in sorted(om, key=lambda r: r['branch']):
        if f'({r["branch"]}) -> {r["outcome"]}' not in rule: return f'VECTOR_RULE_MISMATCH alpha {r}'
        for l in LABELS:
            if l != r['outcome'] and f'({r["branch"]}) -> {l}' in rule: return f'VECTOR_RULE_MISMATCH beta {r}'
    # (vii)
    if set(e['outcome_vocabulary']) - {r['outcome'] for r in om}: return 'VECTOR_LABEL_UNMAPPED'
    # (viii)
    if e['ruled_bytes_sha256'] != canon(e): return 'VECTOR_RULED_BYTES_MISMATCH'
    return 'PASS'
def brier(pv, realized='YES'):
    return format((D('0.5') * sum((D(v) - (1 if l == realized else 0)) ** 2 for l, v in pv.items())).normalize(), 'f')
QM = 'Q-019306a1-4c00-7000-8000-00000000006a'
RULE_SHA = hashlib.sha256(Q[QM]['resolution_rule'].encode()).hexdigest()
def entry(fid, fev, masses, labels=('YES', 'NO', 'AMBIGUOUS', 'AMBIGUOUS'), branches='abcd'):
    om = [{'branch': b, 'outcome': o, 'mass': m} for b, o, m in zip(branches, labels, masses)]
    pv = {l: str(sum((D(r['mass']) for r in om if r['outcome'] == l), D(0))) for l in ('YES', 'NO', 'AMBIGUOUS')}
    e = {'question_id': QM, 'forecast_id': fid, 'forecast_version': 1, 'forecast_event_id': fev,
         'outcome_vocabulary': ['YES', 'NO', 'AMBIGUOUS'], 'probability_vector': pv,
         'source_masses': {b: m for b, m in zip(branches, masses)},
         'normalization': {'method': 'NONE', 'source_sum': str(sum(D(m) for m in masses))},
         'outcome_map': om, 'resolution_rule_sha256': RULE_SHA}
    e['ruled_bytes_sha256'] = canon(e); return e
MID = ('F-019306a1-4c00-7000-8000-00000000006a', 'EVT-019306a1-4c00-7000-8000-00000000006b')
cases = {
 'POSITIVE CONTROL (ruled MIDAS-06)': entry(*MID, ['0.45', '0.20', '0.15', '0.20']),
 'RED Exhibit A (b)<->(c) label trade [v0.2 hole]': entry(*MID, ['0.45', '0.20', '0.15', '0.20'], ('YES', 'AMBIGUOUS', 'NO', 'AMBIGUOUS')),
 'Honest-limit fixture .45/.55/0/0': entry(*MID, ['0.45', '0.55', '0.00', '0.00']),
 'Honest-limit min .45/.275/.275/0': entry(*MID, ['0.45', '0.275', '0.275', '0.00']),
 'EXHIBIT C: foreign forecast F-...a1 (scalar 0.9)': entry('F-019306b4-1a00-7000-8000-0000000000a1', 'EVT-019306b4-1a00-7000-8000-0000000000a2', ['0.9', '0.1', '0.0', '0.0']),
 'EXHIBIT C2: foreign forecast F-...a6 (scalar 0.1)': entry('F-019306b4-1a00-7000-8000-0000000000a6', 'EVT-019306b4-1a00-7000-8000-0000000000a7', ['0.1', '0.0', '0.45', '0.45']),
 'EXHIBIT D: crafted branch keys (non-letter)': entry(*MID, ['0.45', '0.55'], ('YES', 'AMBIGUOUS'), branches=['a', 'b) -> NO, (c']),
}
for name, e in cases.items():
    v = check(e); print(f'{name:52s} -> {v:30s} brier(realized YES)={brier(e["probability_vector"]) if v=="PASS" else "-"}')
# alpha terminator: every PAIR_FORM occurrence in the accepted rule with its next char
import re
rule = Q[QM]['resolution_rule']
print('PAIR_FORM occurrences + next char:', [(m.group(0), rule[m.end():m.end()+1]) for m in re.finditer(r'\([a-z]\) -> (YES|NO|AMBIGUOUS)', rule)])
# Sigma basis: context-rounded vs exact
x = D('0.2000000000000000000000000000001'); print('context Σ==1 with a 31-digit mass:', D('0.45') + x + D('0.35') == 1, '| exact:', (D('0.45') + x + D('0.35')).as_tuple() if False else __import__('fractions').Fraction(D('0.45')) + __import__('fractions').Fraction(x) + __import__('fractions').Fraction(D('0.35')) == 1)
d2 = entry(*MID, ['0.45', '0.00', '0.55'], ('YES', 'NO', 'AMBIGUOUS'), branches=['a', 'b', 'b) -> NO, (c'])
print('EXHIBIT D2: crafted non-letter branch key "b) -> NO, (c" -> AMBIGUOUS .55:', check(d2), brier(d2['probability_vector']))
print('   literal formed:', '(b) -> NO, (c) -> AMBIGUOUS' in rule)
