"""Bounded repair of census_v3; fixed population and Git pin, no owner writes.

Run from anywhere: python3 -B census_v4.py --out /tmp/cato-census-v4
Probabilities and Brier values use units 0..1. UNKNOWN is not zero.
Outcome classification and due-date interpretation inherit v3's heuristics;
this is an extraction/sensitivity exercise, not validated forecast skill.
"""
import argparse
import collections
import csv
import datetime as dt
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess

PIN = "e70f558f4ad685cec394a9cdc2ef6ee622d6b6e0"
AS_OF = dt.date(2026, 10, 1)
HERE = Path(__file__).resolve().parent
V3 = HERE.parent / "2026-09-30_2251_census-v3-evidence"
UNKNOWN = "UNKNOWN"

# Unchanged v3 population-path, outcome and due-date helpers.
def classify_file(f):
    if '/before/' in f or '/cleanup/' in f or 'thesis-reconciliation' in f: return 'SNAPSHOT'
    if '/archive/' in f or 'ARCHIVE' in f or 'RESOLVED' in f.upper().split('/')[-1] and 'archive' in f.lower(): return 'ROTATION'
    if 'SCOREBOARD' in f or 'MIRROR' in f: return 'DERIVED'
    return 'LIVE'

def desk(f):
    p=f.split('/'); return p[1] if p[2]!='sub_agents' else p[1]+'/'+p[3]

POS=('CONFIRMED','HIT','TRUE','ACHIEVED','RESOLVED-TRUE','RESOLVED YES','RESOLVED CONFIRMED','RESOLVED-CONFIRM','CORRECT','HELD','OBSERVED')

NEG=('FAILED','MISSED','MISS','FALSE','FALSIFIED','RESOLVED-FALSE','RESOLVED-FAILED','FROZEN-FAILED','RESOLVED_MISS','RESOLVED NO','RESOLVED MISSED','KILLED','WRONG','DISCONFIRMED','REFUTED','RESOLVED-MISS','NOT OBSERVED')

OPENW=('OPEN','ACTIVE','TRACKING','STRENGTHENING','WEAKENING','DUE-UNRESOLVED','ARMED','WATCH')

def m(txt,words): return any(re.match(r'^\W*'+re.escape(w)+r'(\b|$)',txt) for w in words)

def classify(status,outcome):
    s=status.strip().upper().replace('✅','').replace('❌','').strip(); o=outcome.strip().upper().lstrip('✅❌⚠️ ⛔[')
    if any(s.startswith(w) or w in s for w in OPENW) and not s.startswith('RESOLVED'): return 'OPEN'
    if m(s,NEG): return 'FAILED'
    if m(s,POS) and 'MISS' not in s.split('/')[0]:
        if '/ MISS' in s or '/MISS' in s: return 'OTHER'
        return 'CONFIRMED'
    if s.startswith('RESOLVED') or s=='RESOLVED':
        if m(o,NEG) or o.startswith('NO ') or o.startswith('NO —'): return 'FAILED'
        if m(o,POS): return 'CONFIRMED'
        return 'OTHER'
    return 'OTHER'

def parse_date(s):
    s=s or ''
    mm=re.search(r'(20\d\d)-(\d\d)-(\d\d)',s)
    if mm:
        try: return dt.date(*map(int,mm.groups()))
        except ValueError: pass
    mm=re.search(r'\b(20\d\d)-(\d\d)\b',s)
    if mm:
        y,mo=map(int,mm.groups()); return dt.date(y+(mo==12),1 if mo==12 else mo+1,1)-dt.timedelta(1)
    mm=re.search(r'\bQ([1-4])\s*(20\d\d)|\b(20\d\d)\s*Q([1-4])',s)
    if mm:
        q=int(mm.group(1) or mm.group(4)); y=int(mm.group(2) or mm.group(3)); return dt.date(y,3*q,[31,30,30,31][q-1])
    mm=re.search(r'\b(end[- ]|by )?(20\d\d)\b',s)
    if mm and 'FY' in s.upper(): return dt.date(int(mm.group(2)),12,31)
    return None

def col(h,*names):
    hl=[x.lower() for x in h]
    for n in names:
        if n.lower() in hl: return hl.index(n.lower())
    return None


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], text=True)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


def probability(cell):
    # Current Confidence may instead be an explicit grading instruction.
    match = re.match(
        r'^[*_]*(\d{1,3}(?:\.\d+)?)\s*(?:%|pct)(?!\w)', cell.strip())
    if not match:
        return None
    p = float(match[1]) / 100
    return p if 0 <= p <= 1 else None


def normalize(text):
    return ' '.join(text.casefold().split())


def ledger(text):
    # Match v3's comment/blank treatment, retaining full cells and shape.
    lines = [s for s in text.splitlines() if s.strip() and not s.startswith('#')]
    data = list(csv.reader(lines, delimiter='\t'))
    if not data:
        return []
    header = [s.strip() for s in data[0]]
    ii = col(header, 'Pred_ID', 'ID')
    if ii is None:
        return []
    rows = []
    for number, fields in enumerate(data[1:], 2):
        if ii >= len(fields) or not fields[ii].strip():
            continue
        rows.append({'id': fields[ii].strip(), 'header': header, 'fields': fields,
                     'record': number, 'valid': len(fields) == len(header) and len(set(header)) == len(header)})
    return rows


def cell(row, *names):
    i = col(row['header'], *names)
    return row['fields'][i] if i is not None and i < len(row['fields']) else ''


def signature(row):
    return normalize(cell(row, 'Prediction', 'claim'))


WINDOW_NAMES = ('Resolve_By', 'Resolve_Date', 'Resolves_On', 'Resolution_Date', 'Timeframe', 'window', 'Deadline')


def specification(row):
    return (signature(row), normalize(cell(row, *WINDOW_NAMES)),
            normalize(cell(row, 'Resolution_Criteria')), normalize(cell(row, 'Invalidation')))


class Objects:
    """Read immutable objects; missing paths are expected only in history deletes."""
    def __init__(self, repo):
        self.process = subprocess.Popen(['git', '-C', str(repo), 'cat-file', '--batch'],
                                        stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def get(self, sha, path):
        self.process.stdin.write(f'{sha}:{path}\n'.encode())
        self.process.stdin.flush()
        line = self.process.stdout.readline().decode().strip()
        if line.endswith(' missing'):
            return None
        oid, kind, size = line.split()
        if kind != 'blob':
            raise ValueError(f'Expected blob for {sha}:{path}, found {kind}')
        data = self.process.stdout.read(int(size))
        if self.process.stdout.read(1) != b'\n':
            raise ValueError('Incomplete cat-file response')
        return oid, data.decode('utf-8')

    def close(self):
        self.process.stdin.close()
        self.process.stdout.close()
        if self.process.wait() != 0:
            raise RuntimeError('git cat-file failed')


def histories(repo, pin, keys, objects):
    # Include paths deleted/moved before the pin. No working tree or other refs.
    paths = set(git(repo, 'log', pin, '--full-history', '--format=', '--name-only',
                    '--no-renames', '--', ':(glob)AGENTS/**/PREDICTIONS*.tsv').splitlines())
    order = {sha: i for i, sha in enumerate(git(repo, 'rev-list', '--reverse', '--topo-order', pin).splitlines())}
    by_key = collections.defaultdict(list)
    provenance = []
    for path in sorted(paths - {''}):
        kind = classify_file(path)
        d = desk(path)
        wanted = {pid for owner, pid in keys if owner == d}
        if not wanted or kind in ('SNAPSHOT', 'DERIVED'):
            provenance.append({'path': path, 'class': kind, 'searched': False})
            continue
        log = git(repo, 'log', pin, '--full-history', '--format=%H %cI', '--', path).splitlines()
        commits = sorted({line.split()[0]: line.split()[1] for line in log}.items(), key=lambda pair: order[pair[0]])
        first = {}
        birth = None
        variants = collections.defaultdict(set)
        for sha, stamp in commits:
            obj = objects.get(sha, path)
            if obj is None:
                continue
            if birth is None:
                birth = sha
            blob, text = obj
            for r in ledger(text):
                pid = r['id']
                if pid not in wanted:
                    continue
                variants[pid].add(signature(r))
                if pid not in first:
                    first[pid] = {'commit': sha, 'commit_time': stamp, 'path': path, 'blob': blob,
                                  'file_birth_commit': birth, 'at_file_birth': sha == birth,
                                  'source': r, 'p': probability(cell(r, 'Confidence', 'conf_tier')),
                                  'duplicate_id_at_first_commit': False}
                elif first[pid]['commit'] == sha:
                    first[pid]['duplicate_id_at_first_commit'] = True
        for pid, candidate in first.items():
            candidate['claim_versions_in_path'] = len(variants[pid])
            by_key[(d, pid)].append(candidate)
        provenance.append({'path': path, 'class': kind, 'searched': True,
                           'file_birth_commit': birth, 'matched_ids': len(first)})
    for candidates in by_key.values():
        # Same-commit copies cannot establish an earlier time. Prefer an
        # established ledger, then LIVE, while still checking disagreement.
        candidates.sort(key=lambda c: (order[c['commit']], c['at_file_birth'],
                                        classify_file(c['path']) != 'LIVE', c['path']))
    return by_key, provenance


def earliest(candidates, current, repo):
    if not candidates:
        return None, ['no_ledger_history']
    first = candidates[0]
    flags = []
    if not first['source']['valid']:
        flags.append('first_row_schema_error')
    if first['duplicate_id_at_first_commit']:
        flags.append('duplicate_id_in_first_source')
    if first['at_file_birth']:
        flags.append('present_at_source_file_birth')
    if not signature(first['source']) or signature(first['source']) != signature(current):
        flags.append('claim_changed_or_missing')
    old_spec, new_spec = specification(first['source']), specification(current)
    if old_spec[1] != new_spec[1]:
        flags.append('window_text_changed_or_missing')
    if old_spec[2:] != new_spec[2:]:
        flags.append('resolution_terms_changed_or_missing')
    made_names = ('Date_Made', 'Made_Date', 'made', 'date_made', 'Date')
    before, after = cell(first['source'], *made_names), cell(current, *made_names)
    if before and after and normalize(before) != normalize(after):
        flags.append('made_date_changed')
    # A topological ordering is not proof of ordering across independent branches.
    for candidate in candidates[1:]:
        if candidate['commit'] == first['commit']:
            if (specification(candidate['source']), candidate['p']) != (specification(first['source']), first['p']):
                flags.append('same_commit_conflicting_sources')
        elif subprocess.run(['git', '-C', str(repo), 'merge-base', '--is-ancestor',
                             first['commit'], candidate['commit']], check=False).returncode != 0:
            flags.append('incomparable_history_branches')
    if classify(cell(first['source'], 'Status'), cell(first['source'], 'Outcome', 'Result', 'resolution', 'Outcome_Notes')) != 'OPEN':
        flags.append('first_seen_not_open')
    return first, sorted(set(flags))


def apply_annotations(source, file_text, annotations):
    result = {'p_recorded_grade': None, 'eligibility': UNKNOWN, 'pending': False, 'evidence': []}
    assigned = {}
    for a in annotations:
        if a['source_sha256'] != digest(file_text):
            raise ValueError('Annotation source hash mismatch')
        value = file_text if a['field'] == '__file__' else cell(source, a['field'])
        if a['quote'] not in value:
            raise ValueError(f"Annotation quote missing: {a['field']} / {a['quote']}")
        for key in ('p_recorded_grade', 'eligibility', 'pending'):
            if key in a:
                if key == 'p_recorded_grade' and not 0 <= a[key] <= 1:
                    raise ValueError('Annotated probability outside 0..1')
                if key in assigned and assigned[key] != a[key]:
                    raise ValueError('Conflicting source annotations for '+key)
                assigned[key] = a[key]
                result[key] = a[key]
        result['evidence'].append(a)
    return result


def category(source, grade, p_current):
    status = cell(source, 'Status')
    outcome = cell(source, 'Outcome', 'Result', 'resolution', 'Outcome_Notes')
    cls = classify(status, outcome)
    if not source['valid']:
        return 'schema_error', None
    if grade['pending'] or re.search(r'NEEDS[_ -]VERIFY|PENDING[_ -]VERIF', status, re.I):
        return 'pending_verification', None
    y = 1 if cls == 'CONFIRMED' else 0 if cls == 'FAILED' else None
    if grade['eligibility'] == 'EXCLUDED':
        return 'explicitly_ineligible', y
    if cls == 'OPEN':
        due = parse_date(cell(source, 'Resolve_By', 'Resolve_Date', 'Resolves_On', 'Resolution_Date', 'Timeframe', 'window', 'Deadline'))
        return 'open_' + ('undated' if due is None else 'overdue' if due < AS_OF else 'not_due'), None
    if y is None:
        return 'non_binary_or_unknown_status', None
    return ('binary_numeric_current' if p_current is not None else 'binary_no_current_probability'), y


def stats(pairs):
    if not pairs:
        return {'n': 0, 'brier': UNKNOWN, 'base_rate': UNKNOWN, 'in_sample_baseline': UNKNOWN, 'skill_descriptive': UNKNOWN}
    base = sum(y for p, y in pairs) / len(pairs)
    bs = sum((p-y)**2 for p, y in pairs) / len(pairs)
    baseline = base*(1-base)
    return {'n': len(pairs), 'brier': bs, 'base_rate': base, 'in_sample_baseline': baseline,
            'skill_descriptive': 1-bs/baseline if baseline else UNKNOWN}


def write_tsv(path, rows):
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows({k: UNKNOWN if v is None else v for k, v in r.items()} for r in rows)


def run(repo, out):
    pin = git(repo, 'rev-parse', PIN).strip()
    manifest = json.loads((V3/'source-manifest.json').read_text())
    for name, record in manifest.items():
        if hashlib.sha256((V3/name).read_bytes()).hexdigest() != record['sha256']:
            raise ValueError('Preserved v3 input hash mismatch: '+name)
    original = list(csv.DictReader(io.StringIO((V3/'rows_v3.tsv').read_text()), delimiter='\t'))
    keys = {(r['desk'], r['pred_id']) for r in original}
    if len(keys) != len(original) or len(keys) != 534:
        raise ValueError('Frozen v3 population changed')
    annotations = json.loads((HERE/'annotations.json').read_text())
    if annotations['pin'] != pin:
        raise ValueError('Annotation pin mismatch')
    by_key = collections.defaultdict(list)
    for a in annotations['rows']:
        key = (a['desk'], a['pred_id'])
        if key not in keys:
            raise ValueError('Annotation outside frozen population')
        by_key[key].append(a)
    objects = Objects(repo)
    try:
        history, paths = histories(repo, pin, keys, objects)
        rows, sources, comparisons = [], [], []
        files = {}
        for old in original:
            path, key = old['file'], (old['desk'], old['pred_id'])
            if desk(path) != key[0]:
                raise ValueError('Wrong desk in population')
            if path not in files:
                obj = objects.get(pin, path)
                if obj is None:
                    raise ValueError('Missing pinned population source: '+path)
                files[path] = (obj[0], obj[1], ledger(obj[1]))
            blob, text, data = files[path]
            matches = [r for r in data if r['id'] == key[1]]
            if len(matches) != 1:
                raise ValueError(f'Expected one pinned source row: {key}, found {len(matches)}')
            source = matches[0]
            if any(a['path'] != path for a in by_key[key]):
                raise ValueError('Annotation path differs from pinned row source')
            grade = apply_annotations(source, text, by_key[key])
            p_current = probability(cell(source, 'Confidence', 'conf_tier')) if source['valid'] else None
            candidates = history.get(key, [])
            first, flags = earliest(candidates, source, repo)
            pf = first['p'] if first else None
            conflict = any(f in flags for f in ('claim_changed_or_missing', 'made_date_changed', 'first_row_schema_error',
                                                'window_text_changed_or_missing', 'resolution_terms_changed_or_missing',
                                                'duplicate_id_in_first_source', 'same_commit_conflicting_sources', 'incomparable_history_branches'))
            reason, y = category(source, grade, p_current)
            available = reason.startswith('binary_')
            pr = grade['p_recorded_grade']
            r = dict(desk=key[0], pred_id=key[1], pin=pin, source_path=path, source_blob=blob,
                     status_raw=cell(source, 'Status'), disposition=reason, outcome=y,
                     eligibility=grade['eligibility'], probability_basis='fraction_0_to_1',
                     p_current=p_current, p_recorded_grade=pr, p_earliest_observed=pf,
                     p_registration=UNKNOWN, registration_state=UNKNOWN,
                     first_commit=first['commit'] if first else UNKNOWN,
                     first_commit_time=first['commit_time'] if first else UNKNOWN,
                     first_path=first['path'] if first else UNKNOWN,
                     first_at_source_file_birth=int(first['at_file_birth']) if first else UNKNOWN,
                     history_flags=';'.join(flags) or 'none', history_identity_usable=int(not conflict and first is not None),
                     brier_current=(p_current-y)**2 if available and p_current is not None else None,
                     brier_recorded=(pr-y)**2 if available and pr is not None else None,
                     brier_earliest=(pf-y)**2 if available and pf is not None and not conflict else None)
            rows.append(r)
            sources.append({'desk':key[0], 'pred_id':key[1], 'pin':pin, 'path':path, 'blob':blob,
                            'source':source, 'grading':grade, 'history_candidates':candidates})
            comparisons.append(dict(desk=key[0], pred_id=key[1], v3_reason=old['exclusion_reason'] or 'scored',
                v4_reason=reason, v3_current=float(old['p_scored']) if old['p_scored'] else None,
                v4_current=p_current, recorded_grade=pr,
                v3_first=float(old['p_first_committed']) if old['p_first_committed'] else None,
                v4_earliest_observed=pf, v3_first_commit=old['first_commit_sha'],
                v4_first_commit=first['commit'] if first else UNKNOWN, history_flags=r['history_flags']))
    finally:
        objects.close()
    summary = []
    views = {'current_cell_sensitivity':'p_current', 'recorded_grading_subset':'p_recorded_grade',
             'earliest_identity_usable_sensitivity':'p_earliest_observed'}
    for owner in ['FLEET'] + sorted({r['desk'] for r in rows}):
        subset = [r for r in rows if owner == 'FLEET' or r['desk'] == owner]
        for view, field in views.items():
            eligible = [r for r in subset if r['disposition'].startswith('binary_') and r[field] is not None
                        and (field != 'p_earliest_observed' or r['history_identity_usable'])]
            summary.append(dict(desk=owner, view=view, **stats([(r[field], r['outcome']) for r in eligible])))
        both = [r for r in subset if r['disposition'].startswith('binary_') and r['p_current'] is not None
                and r['p_earliest_observed'] is not None and r['history_identity_usable']]
        for field in ('p_current', 'p_earliest_observed'):
            summary.append(dict(desk=owner, view='matched_'+field,
                                **stats([(r[field], r['outcome']) for r in both])))
    metadata = {'pin':pin, 'as_of':AS_OF.isoformat(), 'population':len(rows),
        'dispositions':dict(collections.Counter(r['disposition'] for r in rows)),
        'recorded_probability_known':sum(r['p_recorded_grade'] is not None for r in rows),
        'registration_probability_known':0, 'source_manifest_v3':manifest,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'annotations_sha256':hashlib.sha256((HERE/'annotations.json').read_bytes()).hexdigest(),
        'history_paths':paths,
        'limits':['Fixed v3 population, not a new census of every historical forecast.',
                  'Claim, made-date, window and resolution/invalidation text differences are flagged, not semantically adjudicated; benign formatting can also differ.',
                  'Earliest ledger occurrence is not proven registration; STATUS/Markdown histories are not mined.',
                  'Malformed first rows retain the numeric value in the probability slot as a candidate; they are excluded from history scoring.',
                  'Recorded probabilities are manually reviewed source annotations; unreviewed values stay UNKNOWN.',
                  'Unknown eligibility remains explicit; sensitivity views are not verified calibration cohorts.',
                  'Outcome/date classification otherwise retains v3 heuristics; outcomes not externally audited.',
                  'In-sample baselines and mixed desks/horizons cannot establish forecast skill.']}
    out.mkdir(parents=True, exist_ok=True)
    write_tsv(out/'rows_v4.tsv', rows)
    write_tsv(out/'summary_v4.tsv', summary)
    write_tsv(out/'comparison_v3_v4.tsv', comparisons)
    with (out/'sources_v4.jsonl').open('w') as f:
        for s in sources:
            f.write(json.dumps(s, ensure_ascii=False, sort_keys=True)+'\n')
    (out/'provenance_v4.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k:v for k,v in metadata.items() if k not in ('history_paths','source_manifest_v3')}, indent=2))
    print(json.dumps([r for r in summary if r['desk']=='FLEET'], indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--repo', type=Path, default=Path(git(HERE, 'rev-parse', '--show-toplevel').strip()))
    args = parser.parse_args()
    run(args.repo, args.out)
