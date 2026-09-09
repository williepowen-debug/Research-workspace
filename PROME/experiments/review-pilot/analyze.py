#!/usr/bin/env python3
"""Descriptive census and masked human-review bundle; no inferential statistics."""
import argparse
import csv
import json
from pathlib import Path
import random

from runner import ROOT, write, score_run, parse_answer, valid_usage


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('run_dir', type=Path)
    args = ap.parse_args()
    out = args.run_dir
    tasks = {t['id']: t for t in json.loads((ROOT / 'corpus.json').read_text())['tasks']}
    order = json.loads((out / 'order.json').read_text())
    results = []
    rows = []
    bundle = []
    for index, scheduled in enumerate(order):
        path = out / f'run-{index:03}.json'
        task = tasks[scheduled['task']]
        result = json.loads(path.read_text()) if path.exists() else {
            'task_id': task['id'], 'condition': scheduled['condition'],
            'repetition': scheduled['rep'], 'status': 'NOT_RUN', 'stages': []}
        score = score_run(task, result)
        stages = result['stages']
        measured_usage = [s['usage'] for s in stages if valid_usage(s.get('usage'))]
        usage_complete = (bool(stages) and len(measured_usage) == len(stages)) or result['status'] == 'NOT_RUN'
        def total(k):
            return sum(u.get(k, 0) for u in measured_usage)
        fields = score['final']['fields']
        flags = score['flag_scores']
        row = {'task': task['id'], 'family': task['family'], 'control': task['no_change_control'],
               'condition': scheduled['condition'], 'repetition': scheduled['rep'],
               'status': result['status'], 'turns': len(stages),
               'first_acceptable': score['first']['acceptable'],
               'final_acceptable': score['final']['acceptable'],
               'final_values_correct': sum(f['value'] for f in fields.values()),
               'final_citations_correct': sum(f['citation'] for f in fields.values()),
               'fields': len(fields), 'repaired_fields': len(score['repaired_fields']),
               'introduced_errors': len(score['introduced_errors']),
               'valid_flags': sum(f['valid'] for f in flags),
               'invalid_flags': sum(not f['valid'] for f in flags),
               'valid_acted_on': sum(f['valid'] and f['acted_on'] for f in flags),
               'valid_ignored': sum(f['valid'] and not f['acted_on'] for f in flags),
               'input_tokens': total('inputTokens'), 'cached_input_tokens': total('cachedInputTokens'),
               'output_tokens': total('outputTokens'), 'reasoning_output_tokens': total('reasoningOutputTokens'),
               'total_tokens': total('totalTokens') if usage_complete else None,
               'known_token_lower_bound': total('totalTokens'), 'usage_complete': usage_complete,
               'measured_turns': len(measured_usage),
               'seconds': sum(s.get('seconds', 0) for s in stages),
               'charges_usd': 'UNAVAILABLE', 'human_validation': 'PENDING'}
        rows.append(row)
        result['score'] = score; results.append(result)
        final_text = stages[2].get('text') if len(stages) >= 3 and stages[2].get('text') else stages[0].get('text') if stages else None
        bundle.append({'sequence_private': index, 'task': task['id'],
                       'documents': task['initial_documents'] + task['update_documents'],
                       'question': task['question'], 'fields': task['fields'],
                       'final_answer': parse_answer(final_text), 'human_grade': None})
    with (out / 'outcomes.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
    groups = {}
    for family in ['all'] + sorted({r['family'] for r in rows}):
        groups[family] = {}
        for arm in ('self', 'separate'):
            selected = [r for r in rows if r['condition'] == arm and (family == 'all' or r['family'] == family)]
            groups[family][arm] = {
                'scheduled': len(selected), 'completed': sum(r['status'] == 'COMPLETED' for r in selected),
                **{k: sum(r[k] for r in selected) for k in (
                    'first_acceptable', 'final_acceptable', 'fields', 'final_values_correct',
                    'final_citations_correct', 'repaired_fields', 'introduced_errors', 'valid_flags',
                    'invalid_flags', 'valid_acted_on', 'valid_ignored', 'known_token_lower_bound',
                    'input_tokens', 'cached_input_tokens', 'output_tokens', 'reasoning_output_tokens', 'seconds')},
                'total_tokens': sum(r['total_tokens'] for r in selected) if all(r['usage_complete'] for r in selected) else None,
                'runs_with_complete_usage': sum(r['usage_complete'] for r in selected)}
    paired = []
    for task_id in sorted({r['task'] for r in rows}):
        for rep in sorted({r['repetition'] for r in rows if r['task'] == task_id}):
            pair = {r['condition']: r for r in rows if r['task'] == task_id and r['repetition'] == rep}
            paired.append({'task': task_id, 'rep': rep, 'separate_minus_self': {
                k: pair['separate'][k] - pair['self'][k]
                if pair['separate'][k] is not None and pair['self'][k] is not None else None for k in (
                    'final_acceptable', 'introduced_errors', 'total_tokens', 'seconds')}})
    write(out / 'summary.json', {'groups': groups, 'paired': paired,
                                'human_validation': 'PENDING', 'inference': 'Descriptive feasibility only'})
    rng = random.Random(9172026); rng.shuffle(bundle)
    mapping = []
    for i, item in enumerate(bundle):
        seq = item.pop('sequence_private'); item['output_id'] = f'OUTPUT-{i+1:03}'
        mapping.append({'output_id': item['output_id'], 'sequence': seq, **order[seq]})
    write(out / 'human-review.json', bundle)
    write(out / 'human-review-mapping-private.json', mapping)
    print(json.dumps(groups['all'], indent=2))


if __name__ == '__main__':
    main()
