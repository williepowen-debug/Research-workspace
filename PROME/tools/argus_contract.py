"""Explicit delivery/evidence contract for argus_scope (schema 2).

Inventory attribution is a recorded reviewer/operator judgment, not a filename
heuristic. This module never stages files, fetches, pushes or advances a baseline.
"""
import datetime as dt
import hashlib
import json
import re
import subprocess
from pathlib import PurePosixPath


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                     ensure_ascii=True).encode()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def path_ok(path):
    require(isinstance(path, str) and path and not path.startswith('-')
            and str(PurePosixPath(path)) == path and not PurePosixPath(path).is_absolute()
            and '..' not in PurePosixPath(path).parts and '.git' not in PurePosixPath(path).parts,
            f'invalid repository path: {path!r}')


def text_ok(value):
    return isinstance(value, str) and bool(value.strip())


def sha_ok(value, absent=False):
    return (absent and value is None) or isinstance(value, str) and bool(re.fullmatch('[0-9a-f]{64}', value))


def git(sc, *args):
    return sc._xgit(*args).stdout.decode('utf-8')


def resolve(sc, ref):
    return git(sc, 'rev-parse', '--verify', '--end-of-options', ref + '^{commit}').strip()


def ancestor(sc, older, newer):
    return sc._xgit('merge-base', '--is-ancestor', older, newer, check=False).returncode == 0


def changes(sc, baseline, head):
    result = {}
    for sha in git(sc, 'rev-list', '--reverse', f'{baseline}..{head}').splitlines():
        for path in git(sc, 'diff-tree', '--root', '-m', '--no-commit-id', '--name-only',
                        '--no-renames', '-r', '-z', sha).split('\0'):
            if path:
                result.setdefault(path, []).append(sha)
    return result


def inventory(sc, baseline, head):
    committed = changes(sc, baseline, head)
    pending = {}
    for state, path in sc.porcelain_entries():
        pending.setdefault(path, []).append(state)
    return {p: {'commits': committed.get(p, []), 'pending': pending.get(p, []),
                'working_sha256': sc._content_id(p), 'commit_sha256': sc._committed_content_id(p, head)}
            for p in sorted(set(committed) | set(pending)) if p not in sc.RECEIPT_PATHS}


def evidence(sc, item):
    require(isinstance(item, dict), 'evidence must be an object')
    path_ok(item.get('path'))
    require(text_ok(item.get('commit')), 'evidence requires a persisted commit')
    sha = resolve(sc, item['commit'])
    content = sc._committed_content_id(item['path'], sha)
    require(content is not None, f'evidence unavailable: {sha}:{item["path"]}')
    return {'path': item['path'], 'commit': sha, 'sha256': content}


def observation(sc, path, item, snapshot):
    path_ok(path)
    require(isinstance(item, dict) and text_ok(item.get('owner'))
            and item['owner'].upper() != 'PROME' and text_ok(item.get('reason')),
            f'{path}: observed-only requires a different named owner and non-reliance reason')
    basis = evidence(sc, item.get('basis'))
    require(text_ok(item.get('quote')), f'{path}: attributable evidence quote required')
    body = git(sc, 'show', f'{basis["commit"]}:{basis["path"]}')
    require(item['quote'] in body, f'{path}: attribution quote absent from evidence')
    require(item.get('not_relied_on') is True, f'{path}: non-reliance must be explicit')
    require(isinstance(snapshot, dict) and set(snapshot) == {
        'commits', 'pending', 'working_sha256', 'commit_sha256'}, f'{path}: incomplete observed snapshot')
    require(isinstance(snapshot['commits'], list) and all(
        isinstance(s, str) and re.fullmatch('[0-9a-f]{40}', s) for s in snapshot['commits'])
        and isinstance(snapshot['pending'], list) and all(isinstance(s, str) for s in snapshot['pending'])
        and sha_ok(snapshot['working_sha256'], absent=True)
        and sha_ok(snapshot['commit_sha256'], absent=True), f'{path}: malformed observed snapshot')
    return {'owner': item['owner'], 'reason': item['reason'], 'basis': basis,
            'quote': item['quote'], 'not_relied_on': True, 'snapshot': snapshot,
            'recorded_at': dt.datetime.now(dt.timezone.utc).isoformat()}


def freeze(sc, plan):
    base, why = sc.load_baseline()
    require(base is not None, f'baseline unusable: {why}')
    require(isinstance(plan, dict) and isinstance(plan.get('delivered'), dict)
            and bool(plan['delivered']), 'nonempty delivered mapping required')
    baseline, head = resolve(sc, base['sha']), resolve(sc, 'HEAD')
    seen = inventory(sc, baseline, head)
    delivered = {}
    for path, provenance in plan['delivered'].items():
        path_ok(path)
        require(path not in sc.RECEIPT_PATHS and text_ok(provenance), f'{path}: provenance required')
        require(path in seen, f'{path}: not a change since baseline')
        delivered[path] = {'sha256': sc._content_id(path), 'provenance': provenance,
                           'versions': {s: sc._committed_content_id(path, s) for s in seen[path]['commits']}}
    deps = []
    for item in plan.get('evidence', []):
        dep = evidence(sc, item)
        require(item.get('mode') in ('historical', 'current'), 'evidence mode must be historical/current')
        claims = item.get('claims')
        require(isinstance(claims, dict) and claims and set(claims) <= set(delivered)
                and all(text_ok(c) for c in claims.values()), 'evidence must name delivered claims')
        deps.append({**dep, 'mode': item['mode'], 'claims': claims})
    observed = {}
    for path, item in plan.get('observed', {}).items():
        require(path in seen and path not in delivered, f'{path}: invalid observed membership')
        require(path not in {d['path'] for d in deps if d['mode'] == 'current'},
                f'{path}: current evidence cannot be observed-only')
        observed[path] = [observation(sc, path, item, seen[path])]
    required = set(delivered) | {d['path'] for d in deps if d['mode'] == 'current'} | set(observed)
    required |= {d['path'] for d in deps if d['mode'] == 'historical' and
                 d['path'] in seen and seen[d['path']]['working_sha256'] == d['sha256'] and
                 seen[d['path']]['commit_sha256'] == d['sha256']}
    require(set(seen) <= required, 'unclassified inventory: ' + ', '.join(sorted(set(seen) - required)))
    contract = {'baseline': baseline, 'anchor': head, 'delivered': delivered, 'evidence': deps}
    manifest = {'schema': 2, 'verdict': sc.FROZEN, 'baseline': base['sha'], 'head': head,
                'recorded_at': dt.datetime.now(dt.timezone.utc).isoformat(), 'contract': contract,
                'contract_sha256': digest(contract), 'observed': observed, 'inventory': seen,
                'paths': {p: d['sha256'] for p, d in delivered.items()}}
    rc, lines = verify(sc, manifest)
    require(rc == 0, '; '.join(lines))
    (sc.ROOT / sc.REVIEW_FILE).write_text(json.dumps(manifest, indent=2) + '\n')
    return manifest


def validate(sc, manifest):
    require(manifest.get('schema') == 2, 'unsupported contract schema')
    c = manifest['contract']
    require(digest(c) == manifest['contract_sha256'], 'contract changed: re-freeze and review changed portion')
    if manifest.get('verdict') == sc.REVIEWED:
        require(manifest.get('reviewed_contract_sha256') == digest(c), 'review verdict belongs to another contract')
    base, why = sc.load_baseline()
    require(base is not None, f'baseline unusable: {why}')
    require(resolve(sc, base['sha']) == c['baseline'], 'contract belongs to a different baseline')
    require(ancestor(sc, c['baseline'], c['anchor']), 'anchor does not descend from baseline')
    require(isinstance(c['delivered'], dict) and c['delivered'], 'empty delivered contract')
    require(isinstance(c['evidence'], list), 'evidence must be a list')
    for path, entry in c['delivered'].items():
        path_ok(path)
        require(path not in sc.RECEIPT_PATHS and sha_ok(entry['sha256'], absent=True)
                and text_ok(entry['provenance']), f'{path}: malformed delivery')
        for sha, content in entry['versions'].items():
            require(ancestor(sc, sha, c['anchor']) and ancestor(sc, c['baseline'], sha)
                    and sc._committed_content_id(path, sha) == content, f'{path}: earlier version unavailable')
    require(manifest['paths'] == {p: d['sha256'] for p, d in c['delivered'].items()}, 'paths mirror differs from contract')
    for dep in c['evidence']:
        require(evidence(sc, dep) == {k: dep[k] for k in ('path', 'commit', 'sha256')}, 'evidence version changed')
        require(dep['mode'] in ('current', 'historical') and isinstance(dep['claims'], dict)
                and dep['claims'] and set(dep['claims']) <= set(c['delivered'])
                and all(text_ok(v) for v in dep['claims'].values()), 'invalid dependency claims')
    require(isinstance(manifest['observed'], dict), 'observed classifications must be a mapping')
    for path, records in manifest['observed'].items():
        require(path not in c['delivered'] and path not in {
            d['path'] for d in c['evidence'] if d['mode'] == 'current'}, f'{path}: conflicting observed role')
        require(isinstance(records, list) and records, f'{path}: observed versions must be a nonempty list')
        for entry in records:
            checked = observation(sc, path, entry, entry['snapshot'])
            require(checked['basis'] == entry['basis'], f'{path}: attribution basis changed')
    return c


def verify(sc, manifest, paths=None, ref=None, snapshot=None):
    try:
        c = validate(sc, manifest)
        require(paths is None or bool(paths), 'empty explicit path list')
        require(snapshot is None or ref is not None, 'snapshot requires a named delivery commit')
        delivery = resolve(sc, ref) if ref else None
        target = resolve(sc, snapshot) if snapshot else delivery
        head = resolve(sc, 'HEAD')  # capture once; never re-resolve the named delivery
        require(ancestor(sc, c['anchor'], target or head), 'delivery predates frozen anchor')
        if snapshot:
            require(ancestor(sc, delivery, target), 'delivery is absent from requested snapshot')
        seen = inventory(sc, c['baseline'], head)
        delivered = set(c['delivered'])
        current_deps = {d['path'] for d in c['evidence'] if d['mode'] == 'current'}
        historical_deps = {(d['path'], d['sha256']) for d in c['evidence'] if d['mode'] == 'historical'}
        errors = []
        for path, entry in c['delivered'].items():
            content = sc._committed_content_id(path, target) if target else sc._content_id(path)
            if content != entry['sha256']:
                errors.append(f'CHANGED-SINCE-REVIEW: delivered {path}')
        for dep in c['evidence']:
            if dep['mode'] == 'current':
                content = sc._committed_content_id(dep['path'], target) if target else sc._content_id(dep['path'])
                if content != dep['sha256']:
                    errors.append(f'CHANGED-SINCE-REVIEW: current evidence {dep["path"]}')
        # Always discover full working/history inventory, even for an explicit path list.
        # Historical dependencies pin their named commit, not the live pathname.
        for path, state in seen.items():
            if path in delivered | current_deps or ((path, state['working_sha256']) in historical_deps
                                                   and (path, state['commit_sha256']) in historical_deps):
                continue
            records = manifest['observed'].get(path, [])
            matched = False
            for entry in records:
                if entry.get('snapshot') != state:
                    continue
                # Recheck attributed basis, including exact captured version. No blanket exemption.
                checked = observation(sc, path, entry, state)
                require(checked['basis'] == entry['basis'], f'{path}: attribution basis changed')
                matched = True
            if not matched:
                errors.append(f'UNCLASSIFIED: {path} (new or changed observed version)')
        if paths is not None:
            for path in set(paths) - delivered - sc.RECEIPT_PATHS:
                errors.append(f'UNREVIEWED DELIVERY PATH: {path}')
        if delivery:
            actual = set(git(sc, 'diff-tree', '--root', '-m', '--no-commit-id', '--name-only',
                             '--no-renames', '-r', '-z', delivery).split('\0')) - {''} - sc.RECEIPT_PATHS
            for path in actual - delivered:
                errors.append(f'UNREVIEWED ACTUAL COMMIT PATH: {path}')
            # Verify any history not in the captured local inventory (e.g. a fetched snapshot).
            for path in changes(sc, c['baseline'], target):
                if path in sc.RECEIPT_PATHS | delivered | current_deps:
                    continue
                content = sc._committed_content_id(path, target)
                if (path, content) in historical_deps:
                    continue
                records = manifest['observed'].get(path, [])
                if not any(r['snapshot']['commit_sha256'] == content for r in records):
                    errors.append(f'UNCLASSIFIED SNAPSHOT PATH: {path}')
        if errors:
            return 1, errors
        return 0, [f'contract {digest(c)} unchanged; verdict {manifest.get("verdict")}; '
                   f'delivery {delivery or "working tree"}; snapshot {target or "working tree"}; '
                   f'{len(seen)} inventory paths retained, unrelated content not certified']
    except (ValueError, KeyError, TypeError, AttributeError, OSError, subprocess.CalledProcessError) as exc:
        return 2, [f'CANNOT-EVALUATE: {exc}']


def observe(sc, additions, ref=None):
    file = sc.ROOT / sc.REVIEW_FILE
    manifest = json.loads(file.read_text())
    c = validate(sc, manifest)
    target = resolve(sc, ref or 'HEAD')
    require(ancestor(sc, c['anchor'], target), 'observed snapshot predates contract anchor')
    seen = inventory(sc, c['baseline'], target)
    for path, item in additions.items():
        require(path in seen and path not in c['delivered']
                and path not in {d['path'] for d in c['evidence'] if d['mode'] == 'current'},
                f'{path}: not unrelated inventory')
        manifest['observed'].setdefault(path, []).append(observation(sc, path, item, seen[path]))
    manifest['inventory'] = seen
    file.write_text(json.dumps(manifest, indent=2) + '\n')
    return manifest
