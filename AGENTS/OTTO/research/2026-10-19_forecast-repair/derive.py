"""Verify the retained s034 evidence and reproduce the strict original-terms score.

Run with Python3; no network and no owner-ledger mutations. Input probabilities
are original registrations, not current cells. Inclusion decisions are documented
in READOUT; arithmetic alone cannot validate those judgments.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import tarfile

B = Path(__file__).resolve().parent
REPO = B.parents[3]
manifest = json.loads((B / 'sources.json').read_text())
checked = []
with tarfile.open(B / 'sources.tar.gz', 'r:gz') as archive:
    for name, item in manifest.items():
        if 'error' in item:
            continue
        if item.get('original_download_path_retained_in_bundle') is False:
            path = item['retained_pdf_excerpt']
            expected = item['retained_pdf_excerpt_sha256']
        else:
            path, expected = item['path'], item['sha256']
        actual = hashlib.sha256(archive.extractfile(path).read()).hexdigest()
        assert actual == expected, (name, path)
        checked.append({'name': name, 'path': path, 'sha256': actual})
for item in json.loads((B / 'history.json').read_text()):
    saved = (B / item['snapshot']).read_bytes()
    actual = subprocess.check_output(
        ['git', 'show', item['commit'] + ':' + item['path']], cwd=REPO)
    assert saved == actual, item['snapshot']
first = (B / 'ee95c5631-PREDICTIONS.md').read_text()
assert '| Q2 2026 | 70%' in first
assert '| H2 2026 | 50%' in first
assert '| Q1-Q2 2026 | 65%' in first
assert '| 27 |' in (B / '3d85bd588-PREDICTIONS.md').read_text()
inputs = [
    ('OTTO-05', .60, 0), ('OTTO-08', .50, 1),
    ('OTTO-26', .40, 0), ('OTTO-27', .50, 1),
    ('OTTO-28', .50, 0), ('OTTO-29', .75, 0),
    ('OTTO-30', .60, 0), ('OTTO-32', .85, 1),
]
scores = [{'id': i, 'as_made': p, 'outcome': y, 'brier': (p-y)**2}
          for i, p, y in inputs]
total = sum(x['brier'] for x in scores)
assert abs(total - 2.215) < 1e-12
result = {'source_hashes_verified': checked, 'historical_snapshots_verified': 4,
          'strict_original_terms': {'rows': scores, 'n': len(scores),
                                   'hits': sum(x['outcome'] for x in scores),
                                   'sum_brier': total, 'mean_brier': total/len(scores)},
          'revised_OTTO_01_sensitivity': {'probability': .75, 'window': 'Q1-Q2',
                                        'n': 9, 'hits': 4,
                                        'mean_brier': (total + .25**2)/9},
          'fsk_actual_Q1': {'gaap_coverage': .42/.48,
                            'adjusted_coverage': .41/.48},
          'gecc_pre_registration': {'first_lien_fv_to_cost': 1688/4774,
                                   'second_lien_fv_to_cost': 898/15807},
          'limits': 'Inclusion judgments require READOUT; other rows not re-audited. '
                    'PointPredictive original PDF not retained in bundle; page13 '
                    'excerpt hash verified. No confidence/threshold fitting.'}
(B / 'verification.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k:v for k,v in result.items() if k not in
                  ['source_hashes_verified', 'strict_original_terms']}))
print('strict score', len(scores), total/len(scores))
