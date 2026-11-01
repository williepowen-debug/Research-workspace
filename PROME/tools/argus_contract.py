"""Explicit delivery/evidence contract for argus_scope (schema 2).

Inventory attribution is a recorded reviewer/operator judgment, not a filename
heuristic. This module never stages files, fetches, pushes or advances a baseline.
"""
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path, PurePosixPath


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


def attributed_by_commit(sc, baseline, seen, delivered_paths, rules):
    """WQ-485 A (Will 2026-10-22 12:10 ET): a path changed since the baseline that is COMMITTED-ONLY (no pending
    state, working bytes == committed bytes) and outside PROME's OWNED lane is attributed by its own commits and
    needs no observed classification. Still requiring delivered/observed: PENDING paths (any state), OWNED paths,
    and any path with PROME authorship evidence (a `PROME` commit subject in the window or a from-PROME /
    via-PROME / MSG-PROME filename) — evidence only ever REQUIRES a classification, never grants one
    (counterexample read 2026-10-22 ❌1/⚠️3/⚠️4). `rules` are the perimeter rules PINNED at the freeze
    (L796 ❌2 repair, 2026-10-24: the live perimeter file is never consulted at verify time, so a post-freeze
    perimeter edit cannot flip a path's class). No rules ⇒ no exemption (strict behaviour)."""
    if rules is None:
        return {}
    subjects = sc.commit_subjects(baseline)
    out = {}
    for p, s in seen.items():
        if never_advisory(sc, p, rules):
            continue  # perimeter / guarded ignore files are delivered or they block — never attributed by a commit subject (❌1 CE-C1, ❌A)
        if not s['commits'] or s['pending'] or p in delivered_paths:
            continue
        if s['working_sha256'] != s['commit_sha256']:
            continue
        if sc.classify(p, rules)[0] == 'OWNED':
            continue
        entry = {'path': p, 'committed': [c[:9] for c in s['commits']], 'pending': []}
        if sc.authorship_evidence(entry, subjects):
            continue
        out[p] = s['commits']
    return out


def attributable_commits(sc, baseline, seen, delivered_paths, rules):
    """WQ-448 re-scoped (Will 2026-10-29 13:45 ET, verbatim "yes approved please fix"; acceptance
    ACCEPTANCE_closeout_gate_foreign_overlap_2026-10-29.md): the COMMITTED side of a path judged ALONE — every window
    commit touching it carries a non-PROME subject, no PROME filename evidence, lane not OWNED under the PINNED rules,
    not delivered, not never-advisory. Returns {path: commits}. Unlike attributed_by_commit it ignores pending state
    and working bytes: it answers "whose commits are these", not "is the working tree clean". Used for a path that is
    committed by its desk AND still pending (the desk kept typing), which under WQ-517 A read UNCLASSIFIED at the
    --ref forms and, with eleven live desks, never cleared."""
    if rules is None:
        return {}
    subjects = sc.commit_subjects(baseline)
    out = {}
    for p, s in seen.items():
        if not s['commits'] or p in delivered_paths or never_advisory(sc, p, rules):
            continue
        if sc.classify(p, rules)[0] == 'OWNED':
            continue
        entry = {'path': p, 'committed': [c[:9] for c in s['commits']], 'pending': []}
        if sc.authorship_evidence(entry, subjects):
            continue
        out[p] = s['commits']
    return out


def history_attributable(sc, path, shas, delivered_paths, rules):
    """Reader CE01 (Opus, 2026-10-29 13:5x ET) ❌: the history leg must judge "whose commits are these" over
    baseline..TARGET, not baseline..HEAD — at a --snapshot beyond HEAD a PROME commit in HEAD..target would otherwise
    be invisible to attributable_commits(). `shas` are the commits touching `path` in baseline..target (from
    changes()); each subject is read directly. Same predicate otherwise: not delivered, not never-advisory, lane not
    OWNED under the pinned rules, no PROME authorship evidence (subject or filename)."""
    if rules is None or not shas or path in delivered_paths or never_advisory(sc, path, rules):
        return False
    if PurePosixPath(path).name in IGNORE_FILES:   # reader CE18 (second read): every ignore file stays strict at the history leg too (WQ-517 read #1 ❌1)
        return False
    if sc.classify(path, rules)[0] == 'OWNED':
        return False
    uniq = list(dict.fromkeys(shas))
    subjects = {sha[:9]: git(sc, 'log', '-1', '--format=%s', sha) for sha in uniq}
    entry = {'path': path, 'committed': [sha[:9] for sha in uniq], 'pending': []}
    return not sc.authorship_evidence(entry, subjects)


def pin_perimeter(sc):
    """The perimeter AS LOADED at the freeze, recorded in the manifest outside the contract (L796 ❌2 repair,
    acceptance ACCEPTANCE_closeout_gate_perimeter_pin_2026-10-24.md). No readable perimeter ⇒ rules None ⇒ every
    later verify runs strict. The file's byte digest rides with it so a reader can tell which version was pinned."""
    import tempfile
    try:
        raw = (sc.ROOT / sc.PERIMETER_FILE).read_bytes()
        with tempfile.NamedTemporaryFile('wb', suffix='.tsv', delete=False) as tmp:
            tmp.write(raw)
        try:
            rules = sc.load_perimeter(tmp.name)   # parsed from the SAME bytes the digest covers (reader ⚠️D)
        finally:
            Path(tmp.name).unlink(missing_ok=True)
    except (SystemExit, OSError):
        return {'sha256': None, 'rules': None}
    return {'sha256': hashlib.sha256(raw).hexdigest(), 'rules': [list(r) for r in rules]}


IGNORE_FILES = ('.gitignore', '.gitattributes')


def never_advisory(sc, path, rules):
    """Paths whose edit changes what the gate can SEE — the perimeter (the rules) and git ignore/attribute files (the
    porcelain inventory). Such a path is never advisory, never attributed by its commits and never observed-only:
    it is delivered (reviewed) or it blocks (readers 10/24: CE8b, CE-G1 ❌2, ❌A, ❌B). An ignore file is guarded only
    where it can hide a non-EXCLUDED path under the PINNED rules: the root and any directory the rules do not class
    EXCLUDED (reader ⚠️C: a desk's nested ignore file in its own EXCLUDED lane stays advisory). No rules ⇒ guarded."""
    if path == sc.PERIMETER_FILE:
        return True
    pp = PurePosixPath(path)
    if pp.name not in IGNORE_FILES:
        return False
    if rules is None:
        return True
    parent = str(pp.parent)
    probe = '.ignore-probe' if parent == '.' else f'{parent}/.ignore-probe'
    return sc.classify(probe, rules)[0] != 'EXCLUDED'


def pinned_rules(manifest):
    """The pinned rules a verify classifies with — never the live file. Absent key / null rules ⇒ None (strict)."""
    pin = manifest.get('perimeter')
    if not isinstance(pin, dict) or pin.get('rules') is None:
        return None
    return [tuple(r) for r in pin['rules']]


def freeze(sc, plan):
    base, why = sc.load_baseline()
    require(base is not None, f'baseline unusable: {why}')
    require(isinstance(plan, dict), 'plan must be an object')
    explicit = plan.get('delivered', {})
    auto_d = plan.get('auto_delivered') is True
    require(isinstance(explicit, dict) and (bool(explicit) or auto_d),
            'nonempty delivered mapping (or "auto_delivered": true) required')
    baseline, head = resolve(sc, base['sha']), resolve(sc, 'HEAD')
    seen = inventory(sc, baseline, head)
    pin = pin_perimeter(sc)
    pin_rules = pinned_rules({'perimeter': pin})
    moves = mechanical_moves(sc, baseline, seen, set(explicit), pin_rules)   # WQ-583 AC4
    legs = move_legs(moves)
    plan_delivered = dict(explicit)
    exclude = plan.get('exclude', [])
    require(isinstance(exclude, list) and not (set(exclude) & set(explicit)), 'exclude must be a list disjoint from delivered')
    if auto_d:                                                     # WQ-583 AC6
        plan_delivered = {**derive_delivered(sc, baseline, seen, pin_rules, legs | set(explicit) | set(exclude)), **explicit}
    require(plan_delivered, 'nothing to deliver')
    delivered = {}
    for path, provenance in plan_delivered.items():
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
    guarded = sorted(p for p in seen if never_advisory(sc, p, pin_rules) and p not in delivered)
    require(not guarded, 'changed since the baseline and never attributed by commit or observed-only — deliver it '
            '(the perimeter becomes the pin; an ignore file changes what the gate can see): ' + ', '.join(guarded))
    observed = {}
    for path, item in plan.get('observed', {}).items():
        require(not never_advisory(sc, path, pin_rules), f'{path}: never observed-only — deliver it')
        require(path in seen and path not in delivered, f'{path}: invalid observed membership')
        require(path not in {d['path'] for d in deps if d['mode'] == 'current'},
                f'{path}: current evidence cannot be observed-only')
        observed[path] = [observation(sc, path, item, seen[path])]
    required = set(delivered) | {d['path'] for d in deps if d['mode'] == 'current'} | set(observed)
    required |= {d['path'] for d in deps if d['mode'] == 'historical' and
                 d['path'] in seen and seen[d['path']]['working_sha256'] == d['sha256'] and
                 seen[d['path']]['commit_sha256'] == d['sha256']}
    auto = attributed_by_commit(sc, baseline, seen, set(delivered), pin_rules)
    required |= set(auto) | legs
    # Will 2026-10-29 14:05 ET ("we need to fix this freeze thing. This seems costly"; acceptance
    # ACCEPTANCE_freeze_foreign_pending_2026-10-29.md): the freeze applies the SAME foreign test the verify applies. A
    # pending path outside PROME's OWNED lane under the pin, not delivered, not a never-advisory or ignore-named file,
    # with no PROME authorship evidence — including the committed-AND-pending overlap when its commits are all non-PROME
    # — is RECORDED under `foreign_at_freeze` (lane + inventory snapshot) instead of demanding a hand-written observed
    # entry. OWNED, PROME-evidenced, guarded and unpinned cases stay refused below exactly as before.
    foreign = {}
    if pin_rules is not None:
        subjects = sc.commit_subjects(baseline)
        attributable = attributable_commits(sc, baseline, seen, set(delivered), pin_rules)
        for p in sorted(set(seen) - required):
            s = seen[p]
            if not s['pending'] or never_advisory(sc, p, pin_rules) or PurePosixPath(p).name in IGNORE_FILES:
                continue
            lane = sc.classify(p, pin_rules)[0]
            if lane == 'OWNED':
                continue
            if sc.authorship_evidence({'path': p, 'committed': [c[:9] for c in s['commits']], 'pending': []}, subjects):
                continue
            if s['commits'] and p not in attributable:
                continue
            foreign[p] = {'lane': lane, 'snapshot': s}
        required |= set(foreign)
    require(set(seen) <= required, 'unclassified inventory (PENDING, OWNED, PROME-evidenced or differing from its commit): ' + ', '.join(sorted(set(seen) - required)))
    reused = reuse_entries(sc, baseline, delivered, plan.get('reviewed', {}))   # WQ-583 AC5
    contract = {'baseline': baseline, 'anchor': head, 'delivered': delivered, 'evidence': deps,
                'mechanical_moves': moves, 'reused': reused}
    manifest = {'schema': 2, 'verdict': sc.FROZEN, 'baseline': base['sha'], 'head': head,
                'recorded_at': dt.datetime.now(dt.timezone.utc).isoformat(), 'contract': contract,
                'contract_sha256': digest(contract), 'observed': observed, 'inventory': seen,
                'attributed_by_commit': auto, 'perimeter': pin, 'foreign_at_freeze': foreign,
                'paths': {p: d['sha256'] for p, d in delivered.items()}}
    rc, lines = verify(sc, manifest)
    require(rc == 0, '; '.join(lines))
    # WQ-583 AC1: the reviewed bytes as an immutable commit off every branch; PROME's own pending moves ride it.
    cand = {p: d['sha256'] for p, d in delivered.items()}
    for dest, rec in own_pending_moves(sc, moves, seen, pin_rules).items():
        cand[dest], cand[rec['origin']] = rec['sha256'], None
    manifest['candidate'] = {'sha': build_candidate(sc, head, cand, manifest['contract_sha256'][:12]),
                             'ref': CANDIDATE_REF, 'paths': cand}
    candidate_check(sc, manifest, contract)   # the full verify above already ran; this proves the candidate legs
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
    pin = manifest.get('perimeter')
    if pin is not None:
        require(isinstance(pin, dict) and set(pin) == {'sha256', 'rules'} and sha_ok(pin['sha256'], absent=True),
                'malformed perimeter pin')
        require(pin['rules'] is None or (isinstance(pin['rules'], list) and pin['rules'] and all(
            isinstance(r, list) and len(r) == 3 and all(isinstance(x, str) for x in r) and r[1] in sc.CLASSES
            for r in pin['rules'])), 'malformed perimeter pin rules')
    moves = c.get('mechanical_moves', {})
    require(isinstance(moves, dict) and isinstance(c.get('reused', {}), dict), 'malformed moves/reuse')
    for dest, rec in moves.items():
        path_ok(dest); path_ok(rec['origin'])
        require(sha_ok(rec['sha256']) and dest not in c['delivered'] and rec['origin'] not in c['delivered']
                and not _move_excluded(sc, dest) and not _move_excluded(sc, rec['origin']), f'{dest}: malformed move')
    for path, r in c.get('reused', {}).items():
        require(path in c['delivered'] and r.get('sha256') == c['delivered'][path]['sha256'], f'{path}: malformed reuse')
    candidate_check(sc, manifest, c)
    require(isinstance(manifest['observed'], dict), 'observed classifications must be a mapping')
    for path, records in manifest['observed'].items():
        require(not never_advisory(sc, path, pinned_rules(manifest)), f'{path}: never observed-only (reader 10/24 ❌B)')
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
        errors, post_freeze = [], []
        cand = manifest.get('candidate')   # validate() proved its bytes equal the contract (WQ-583 AC2)
        moves = c.get('mechanical_moves', {})
        held_working = move_legs(moves, sc)
        held_target = move_legs(moves, sc, target) if target else held_working
        own_moves = {d: r for d, r in moves.items()
                     if _own(sc, d, pinned_rules(manifest)) and _own(sc, r['origin'], pinned_rules(manifest))}
        held_delivery = move_legs(own_moves, sc, delivery if delivery else None)   # read #3 ⚠️1 (WQ-584): a desk's move never rides a PROME commit
        for path, entry in c['delivered'].items():
            content = sc._committed_content_id(path, target) if target else sc._content_id(path)
            if content == entry['sha256']:
                continue
            if target is None and cand:
                post_freeze.append(f'POST-FREEZE EDIT (not in the reviewed candidate {cand["sha"][:9]}; re-freeze to ship '
                                   f'it with this delivery, or --carry it to the bookkeeping commit): {path}')
            else:
                errors.append(f'CHANGED-SINCE-REVIEW: delivered {path}')
        for dep in c['evidence']:
            if dep['mode'] == 'current':
                content = sc._committed_content_id(dep['path'], target) if target else sc._content_id(dep['path'])
                if content != dep['sha256']:
                    errors.append(f'CHANGED-SINCE-REVIEW: current evidence {dep["path"]}')
        # Always discover full working/history inventory, even for an explicit path list.
        # Historical dependencies pin their named commit, not the live pathname.
        # L796 ❌2 repair (2026-10-24): every classification below uses the rules PINNED at the freeze. The live
        # PROME/state/AUDIT_PERIMETER.tsv is never read here, so a post-freeze edit of it cannot downgrade an OWNED
        # arrival (itself included) to advisory, and cannot flip a committed-only path into commit attribution.
        # A manifest with no pin (frozen before this change) runs strict.
        rules = pinned_rules(manifest)
        auto = attributed_by_commit(sc, c['baseline'], seen, delivered, rules) if 'attributed_by_commit' in manifest else {}
        attributable = attributable_commits(sc, c['baseline'], seen, delivered, rules) if 'attributed_by_commit' in manifest else {}
        # Will 2026-10-22 12:34 ET ("we need to change these rules"): on a WORKING-TREE verify, a PENDING path that is
        # neither OWNED nor PROME-evidenced is another owner's live work — advisory, never blocking. The delivery
        # commit (--ref) is still verified by its actual paths. Acceptance: ACCEPTANCE_closeout_gate_foreign_pending_2026-10-22.md
        # WQ-517 A (2026-10-24) extends the advisory branch to the --ref / --snapshot forms for PENDING-ONLY paths; see the loop.
        advisories = []
        try:
            subjects = sc.commit_subjects(c['baseline'])
        except SystemExit:
            subjects = None
        def foreign_pending(path, state):
            """The lane class when the path is another owner's live pending file, else None. The perimeter and git
            ignore/attribute files are never advisory (CE8b, CE-G1); OWNED and PROME-evidenced paths never are."""
            if rules is None or subjects is None or not state['pending'] or path in delivered or never_advisory(sc, path, rules):
                return None
            lane = sc.classify(path, rules)[0]
            if lane == 'OWNED':
                return None
            entry = {'path': path, 'committed': [x[:9] for x in state['commits']], 'pending': list(state['pending'])}
            return None if sc.authorship_evidence(entry, subjects) else lane
        for path, state in seen.items():
            if path in delivered | current_deps or ((path, state['working_sha256']) in historical_deps
                                                   and (path, state['commit_sha256']) in historical_deps):
                continue
            if path in auto:  # WQ-485 A: committed-only, outside OWNED — attributed by its commits
                continue
            if path in held_working:  # WQ-583 AC4: byte-identical move, still holding
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
                # WQ-517 A (Will 2026-10-24, full registered restrictions): at the --ref / --snapshot forms the
                # advisory branch reaches ONLY a pending-only path — no commit in baseline..HEAD, hence outside the
                # delivery commit and outside baseline-to-target history — that the predicate already calls foreign
                # (not delivered, not never-advisory, not OWNED under the pin, no PROME evidence). Delivered content,
                # dependencies, actual commit paths, history and snapshot paths stay strict below.
                # Acceptance: ACCEPTANCE_closeout_gate_ref_pending_only_2026-10-24.md
                # Read #1 ❌1 (CE-F/F2/F3, 2026-10-24 19:4x ET): a NESTED ignore file is not `never_advisory` when its own
                # folder is EXCLUDED, yet its patterns can hide an OWNED / PROME-evidenced arrival below it from this
                # inventory — so at the --ref / --snapshot forms every ignore file keeps the PRE-REPAIR strict behaviour
                # (UNCLASSIFIED); the working-tree gap for the same file is DOCKET L835, unchanged here.
                # WQ-448 re-scoped (Will 2026-10-29 13:45 ET): at the --ref / --snapshot forms a path that is committed
                # by its desk AND still pending is advisory too, PROVIDED its committed side is attributable on its own
                # (attributable_commits: every window commit non-PROME by subject, no PROME filename evidence, lane not
                # OWNED, not delivered, not never-advisory). Ignore/attribute files keep the strict behaviour (read #1 ❌1).
                # Delivered content, dependencies, actual commit paths and the history leg below stay strict.
                name_ok = PurePosixPath(path).name not in IGNORE_FILES
                over_committed = False
                if target is None:
                    lane = foreign_pending(path, state)
                elif not state['commits'] and name_ok:
                    lane = foreign_pending(path, state)
                elif state['pending'] and name_ok and path in attributable:
                    lane = foreign_pending(path, state)
                    over_committed = lane is not None
                else:
                    lane = None
                if lane and over_committed:
                    shas = ','.join(dict.fromkeys(x[:9] for x in state['commits']))   # a merge lists a path once per parent — print each sha once
                    advisories.append(f'FOREIGN-PENDING-OVER-COMMITTED (advisory, attributed by its own commits {shas}; '
                                      f'owner UNVERIFIED — {lane} lane, no PROME evidence): {path}')
                elif lane:
                    advisories.append(f'FOREIGN-PENDING (advisory, owner UNVERIFIED — {lane} lane, no PROME evidence): {path}')
                else:
                    errors.append(f'UNCLASSIFIED: {path} (new or changed observed version)')
        if paths is not None:
            for path in set(paths) - delivered - sc.RECEIPT_PATHS - held_delivery:
                errors.append(f'UNREVIEWED DELIVERY PATH: {path}')
        if delivery:
            actual = set(git(sc, 'diff-tree', '--root', '-m', '--no-commit-id', '--name-only',
                             '--no-renames', '-r', '-z', delivery).split('\0')) - {''} - sc.RECEIPT_PATHS
            for path in actual - delivered - held_delivery:
                errors.append(f'UNREVIEWED ACTUAL COMMIT PATH: {path}')
            # Verify any history not in the captured local inventory (e.g. a fetched snapshot).
            for path, shas in changes(sc, c['baseline'], target).items():
                if path in sc.RECEIPT_PATHS | delivered | current_deps | held_target:
                    continue
                content = sc._committed_content_id(path, target)
                if (path, content) in historical_deps:
                    continue
                # WQ-485 A (committed-only) · WQ-448 re-scoped 2026-10-29 (committed side of an overlap path), judged over
                # baseline..TARGET so a PROME commit beyond HEAD cannot hide (reader CE01 ❌, 2026-10-29).
                if 'attributed_by_commit' in manifest and history_attributable(sc, path, shas, delivered, rules):
                    # reader CE16/CE17 (second read): leave a trace for every history path skipped by attribution, so a fetched
                    # snapshot's desk commits never vanish from the output silently.
                    advisories.append(f'FOREIGN-HISTORY (advisory, attributed by its own commits {",".join(dict.fromkeys(x[:9] for x in shas))}): {path}')
                    continue
                records = manifest['observed'].get(path, [])
                if not any(r['snapshot']['commit_sha256'] == content for r in records):
                    errors.append(f'UNCLASSIFIED SNAPSHOT PATH: {path}')
        advisories = post_freeze + advisories
        if errors:
            return 1, errors + advisories
        return 0, advisories + [f'contract {digest(c)} unchanged; verdict {manifest.get("verdict")}; '
                   f'candidate {cand["sha"][:9] if cand else "none"}; {len(moves)} mechanical move(s); '
                   f'{len(c.get("reused", {}))} reused review(s); '
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
    rules = pinned_rules(manifest)
    for path, item in additions.items():
        require(not never_advisory(sc, path, rules),
                f'{path}: never observed-only — the perimeter and guarded ignore files are delivered in a re-freeze or they block (reader 10/24 ❌B)')
        require(path in seen and path not in c['delivered']
                and path not in {d['path'] for d in c['evidence'] if d['mode'] == 'current'},
                f'{path}: not unrelated inventory')
        manifest['observed'].setdefault(path, []).append(observation(sc, path, item, seen[path]))
    manifest['inventory'] = seen
    file.write_text(json.dumps(manifest, indent=2) + '\n')
    return manifest


# ---------------------------------------------------------------- WQ-583 code half (Will 2026-10-31 20:26 ET,
# verbatim "can you do this part now"; DOCKET L912; acceptance tests/ACCEPTANCE_wq583_candidate_moves_reuse_2026-10-31.md;
# bounds from CATO 0629fd459): a review candidate held OFF the shared branch, byte-identical moves skipped pair by pair,
# exact-version review reuse, and a delivery list derived from the inventory instead of typed by hand.

CANDIDATE_REF = 'refs/prome/argus-candidate'
NULL_SHA = '0' * 40


def _run(sc, *args, env=None, data=None):
    full = {**os.environ, 'GIT_NO_REPLACE_OBJECTS': '1', **(env or {})}
    return subprocess.run(['git', *args], cwd=sc.ROOT, env=full, input=data,
                          capture_output=True, check=True).stdout.decode('utf-8')


def tree_entry(sc, ref, path):
    """(mode, blob) of `path` in `ref`, or None when absent."""
    out = _run(sc, 'ls-tree', '-z', ref, '--', path)
    for rec in out.split('\0'):
        if rec and '\t' in rec:
            meta, name = rec.split('\t', 1)
            mode, kind, blob = meta.split()
            if name == path and kind == 'blob':
                return mode, blob
    return None


def _move_excluded(sc, path):
    return (path == sc.PERIMETER_FILE or path in sc.RECEIPT_PATHS
            or PurePosixPath(path).name in IGNORE_FILES)


def _own(sc, path, rules):
    """PROME's side of the tree for move purposes: its own directory or an OWNED lane under the pinned rules."""
    return path.startswith('PROME/') or (rules is not None and sc.classify(path, rules)[0] == 'OWNED')


def mechanical_moves(sc, baseline, seen, explicit, rules=None):
    """AC4: {dest: {'origin', 'sha256'}} for byte-identical moves since the baseline — origin absent from the working
    tree and PRESENT AT THE BASELINE, destination absent at the baseline, same basename, destination bytes (working,
    and committed if committed) equal to the origin's BASELINE bytes, exactly one pairing per (basename, bytes), both
    legs on the same side of PROME's tree (_own). Reader 2026-10-31 ❌1: a version the origin gained INSIDE the window
    is new content, never a move. Never: the perimeter, an ignore/attributes file, a receipt path, an explicit delivery."""
    if rules is None:
        return {}   # no pinned lanes ⇒ no move can be judged same-lane ⇒ strict
    try:
        filemode = _run(sc, 'config', '--bool', 'core.fileMode').strip() != 'false'
    except subprocess.CalledProcessError:
        filemode = True
    origins, dests = {}, {}
    for p, s in seen.items():
        if p in explicit or _move_excluded(sc, p):
            continue
        if s['working_sha256'] is None:
            was = sc._committed_content_id(p, baseline)
            if was is not None and s['commit_sha256'] in (None, was):
                origins.setdefault((PurePosixPath(p).name, was, tree_entry(sc, baseline, p)[0]), []).append(p)
        elif sc._committed_content_id(p, baseline) is None and s['commit_sha256'] in (None, s['working_sha256']):
            f = sc.ROOT / p
            if f.is_symlink() or not f.is_file():
                continue
            committed = tree_entry(sc, 'HEAD', p)
            mode = ('100755' if f.stat().st_mode & 0o111 else '100644') if filemode or not committed else committed[0]
            if committed and committed[0] != mode:
                continue   # committed and working modes disagree: not one version
            dests.setdefault((PurePosixPath(p).name, s['working_sha256'], mode), []).append(p)
    out = {}
    for key, ds in dests.items():
        os_ = origins.get(key, [])   # the key carries bytes AND mode (reader #2 ⚠️9: no exec bit rides a move)
        dl = sc.classify(ds[0], rules)[0] if ds else None
        if (len(ds) == 1 and len(os_) == 1 and _own(sc, ds[0], rules) == _own(sc, os_[0], rules)
                and (dl == sc.classify(os_[0], rules)[0] or (dl == 'EXCLUDED' and sc.classify(os_[0], rules)[0] == 'SHARED'))):
            # reader #2 ❌2 + read #3 ⚠️2 (WQ-584): same pinned lane, or SHARED → EXCLUDED (a consumption) — bytes never move from
            # a less-audited lane into a more-audited one (EXCLUDED desk mail → an OWNED live path is new content)
            out[ds[0]] = {'origin': os_[0], 'sha256': key[1]}
    return out


def move_holds(sc, dest, rec, target=None):
    """A recorded move still holds: destination bytes unchanged and origin still absent (working tree, or `target`)."""
    if target:
        return (sc._committed_content_id(dest, target) == rec['sha256']
                and sc._committed_content_id(rec['origin'], target) is None)
    return sc._content_id(dest) == rec['sha256'] and sc._content_id(rec['origin']) is None


def move_legs(moves, sc=None, target=None):
    """Both legs of every recorded move; with `sc`, only moves that still hold (at `target`, else the working tree)."""
    legs = set()
    for dest, rec in moves.items():
        if sc is None or move_holds(sc, dest, rec, target):
            legs |= {dest, rec['origin']}
    return legs


def own_pending_moves(sc, moves, seen, rules=None):
    """PROME's own moves not yet committed (both legs on PROME's side — its directory or an OWNED lane, e.g. FORGE →
    FORGE/_archive; at least one leg pending): they ride the candidate and ship with the delivery. A desk's move of a
    from-PROME packet is mechanical but never PROME's to commit."""
    return {d: r for d, r in moves.items()
            if _own(sc, d, rules) and _own(sc, r['origin'], rules)
            and (seen.get(d, {}).get('pending') or seen.get(r['origin'], {}).get('pending'))}


def derive_delivered(sc, baseline, seen, rules, skip):
    """AC6: OWNED under the pinned rules · touched by a PROME-subject window commit · PENDING in the SHARED lane with
    PROME filename evidence. Provenance is written from the commit subjects."""
    subjects = sc.commit_subjects(baseline)
    out = {}
    for p, s in sorted(seen.items()):
        if p in skip or p in sc.RECEIPT_PATHS:
            continue
        lane = sc.classify(p, rules)[0] if rules is not None else None
        mine = [c[:9] for c in dict.fromkeys(s['commits']) if sc.PROME_SUBJECT_RE.match(subjects.get(c[:9], ''))]
        name = PurePosixPath(p).name
        sender = bool(re.search(r'from-prome(?![a-z0-9])', name, re.I)
                      or re.match(r'^AGENTS/[^/]+/inbox/MSG-PROME-[^/]+\.md$', p))   # never via-PROME (reader ⚠️8)
        if lane != 'OWNED':
            # Reader 2026-10-31 ❌3: outside PROME's lane a PENDING edit may be another desk's — never claim it
            # automatically; PROME names it in `delivered` or classifies it. A PENDING sender-named packet in a SHARED
            # inbox is PROME's own new packet; a committed-only path PROME's commit or name evidences ships unchanged.
            new_packet = (sender and lane == 'SHARED' and not s['commits'] and s['working_sha256'] is not None
                          and s['commit_sha256'] is None and sc._committed_content_id(p, baseline) is None)
            if s['pending'] and not new_packet:   # reader #2 ❌1: an OLD packet's pending change is the desk's
                continue
            if not mine and not sender:
                continue
        bits = [f'{c} {subjects[c][:70]}' for c in mine[:4]] + ([f'+{len(mine) - 4} more PROME commits'] if len(mine) > 4 else [])
        others = len(set(c[:9] for c in s['commits'])) - len(mine)
        if others:
            bits.append(f'{others} non-PROME commit(s)')
        if s['pending']:
            bits.append('pending at freeze')
        reason = 'OWNED lane' if lane == 'OWNED' else 'PROME commit subject' if mine else 'from-PROME filename'
        out[p] = f'auto (WQ-583 AC6, {reason}): ' + '; '.join(bits or ['no commit'])
    return out


def reuse_entries(sc, baseline, delivered, plan_reviewed):
    """AC5: exact-version reuse from the previous REVIEWED manifest on the same baseline, plus plan-declared reviews
    (a commit or sha256 and a receipt), each accepted only for identical bytes. A changed path is never reused."""
    reused = {}
    f = sc.ROOT / sc.REVIEW_FILE
    try:
        prev = json.loads(f.read_text()) if f.exists() else {}
    except (OSError, ValueError):
        prev = {}
    pc = prev.get('contract') if isinstance(prev, dict) else None
    if (isinstance(pc, dict) and prev.get('schema') == 2 and prev.get('verdict') == sc.REVIEWED
            and prev.get('reviewed_contract_sha256') == digest(pc) == prev.get('contract_sha256')
            and pc.get('baseline') == baseline):
        for p, d in delivered.items():
            old = pc.get('delivered', {}).get(p)
            if isinstance(old, dict) and old.get('sha256') == d['sha256']:
                reused[p] = {'source': 'previous-review', 'contract': prev['contract_sha256'], 'sha256': d['sha256']}
    require(isinstance(plan_reviewed, dict), 'reviewed must be a mapping')
    require(not plan_reviewed, 'declared reviews are switched off (read #3 ⚠️3, WQ-584): only an exact-version '
            'reuse from the previous REVIEWED freeze counts')
    for p, item in plan_reviewed.items():
        require(p in delivered, f'{p}: a declared review must name a delivered path')
        require(isinstance(item, dict) and text_ok(item.get('receipt')), f'{p}: declared review needs a receipt')
        rpath = item['receipt'].split('#', 1)[0].strip()
        require(rpath and sc._committed_content_id(rpath, 'HEAD') is not None,
                f'{p}: the declared review receipt must be a committed file (path#anchor): {item["receipt"]!r}')
        require(p in git(sc, 'show', f'HEAD:{rpath}'), f'{p}: the declared review receipt does not name this path')
        require(text_ok(item.get('commit')), f'{p}: a declared review names the reviewed commit (no bare digest)')
        commit = resolve(sc, item['commit'])
        want = sc._committed_content_id(p, commit)
        require(sha_ok(want) and want == delivered[p]['sha256'],
                f'{p}: the declared review is of a different version — not reused (AC5)')
        reused[p] = {'source': 'declared', 'receipt': item['receipt'], 'commit': commit, 'sha256': want}
    return reused


def build_candidate(sc, head, entries, label):
    """AC1: an immutable commit (parent `head`) holding `entries` {path: sha256|None} at their working bytes, built in
    a PRIVATE index — the shared index and every branch are untouched; referenced only by CANDIDATE_REF."""
    import tempfile
    try:
        filemode = _run(sc, 'config', '--bool', 'core.fileMode').strip() != 'false'
    except subprocess.CalledProcessError:
        filemode = True
    lines = []
    for p, want in sorted(entries.items()):
        f = sc.ROOT / p
        if want is None:
            require(not f.exists() and not f.is_symlink(), f'{p}: expected absent at freeze')
            lines.append(f'0 {NULL_SHA}\t{p}')
            continue
        require(f.is_file() and not f.is_symlink(), f'{p}: candidate holds regular files only')
        blob = _run(sc, 'hash-object', '-w', '--path', p, '--', str(f)).strip()
        if filemode:
            mode = '100755' if f.stat().st_mode & 0o111 else '100644'
        else:   # core.fileMode=false: git keeps the recorded mode (reader ⚠️9)
            mode = (tree_entry(sc, head, p) or ('100644',))[0]
        lines.append(f'{mode} {blob}\t{p}')
    with tempfile.TemporaryDirectory() as td:
        env = {'GIT_INDEX_FILE': str(Path(td) / 'index')}
        _run(sc, 'read-tree', head, env=env)
        _run(sc, 'update-index', '--index-info', env=env, data=('\n'.join(lines) + '\n').encode())
        tree = _run(sc, 'write-tree', env=env).strip()
    sha = _run(sc, 'commit-tree', tree, '-p', head, '-m',
               f'PROME ARGUS review candidate (never on a branch) — {label}').strip()
    for p, want in entries.items():
        require(sc._committed_content_id(p, sha) == want,
                f'{p}: candidate bytes differ from the frozen digest (changed during the freeze, or a git filter) — re-run')
    _run(sc, 'update-ref', '-m', 'argus candidate', CANDIDATE_REF, sha)
    return sha


def candidate_check(sc, manifest, c):
    """validate() leg: the recorded candidate still holds the contract's bytes on the contract's anchor."""
    cand = manifest.get('candidate')
    if cand is None:
        return None
    require(isinstance(cand, dict) and isinstance(cand.get('paths'), dict), 'malformed candidate')
    sha = resolve(sc, cand['sha'])
    require(git(sc, 'rev-parse', sha + '^').strip() == c['anchor'], 'candidate parent is not the frozen anchor')
    expected = {p: d['sha256'] for p, d in c['delivered'].items()}
    for dest, rec in c.get('mechanical_moves', {}).items():
        if dest in cand['paths'] or rec['origin'] in cand['paths']:
            expected[dest], expected[rec['origin']] = rec['sha256'], None
    require(cand['paths'] == expected, 'candidate path set differs from the contract')
    for p, want in expected.items():
        require(sc._committed_content_id(p, sha) == want, f'{p}: candidate bytes differ from the contract')
    return sha


def run_commit_hooks(sc, env, msg_file, workdir):
    """Run the configured pre-commit and commit-msg hooks exactly as `git commit` would for this delivery: the
    private index in GIT_INDEX_FILE, HEAD = current master, a scratch copy of the message. Any refusal refuses."""
    hooks_dir = sc.ROOT / _run(sc, 'rev-parse', '--git-path', 'hooks').strip()   # git's own resolution (reader #2 ⚠️3)
    msg_copy = Path(workdir) / 'COMMIT_EDITMSG'
    msg_copy.write_bytes(Path(msg_file).read_bytes())
    for name, args in (('pre-commit', []), ('commit-msg', [str(msg_copy)])):
        hook = hooks_dir / name
        if not (hook.is_file() and os.access(hook, os.X_OK)):
            continue
        r = subprocess.run([str(hook), *args], cwd=sc.ROOT, env={**os.environ, **env}, capture_output=True)
        require(r.returncode == 0, f'{name} hook refused the delivery (rc {r.returncode}): '
                + (r.stderr or r.stdout).decode('utf-8', 'replace').strip()[:400])
    require(Path(msg_copy).read_bytes() == Path(msg_file).read_bytes(),
            'commit-msg hook rewrote the message — commit it the ordinary way')


def deliver(sc, msg_file, carry=()):
    """AC3: put the REVIEWED candidate's bytes on master as ONE commit on top of current HEAD (other desks' commits
    kept), compare-and-swap, then sync the shared index for exactly those paths. Returns (sha, paths)."""
    manifest = json.loads((sc.ROOT / sc.REVIEW_FILE).read_text())
    c = validate(sc, manifest)
    require(manifest.get('verdict') == sc.REVIEWED and manifest.get('reviewed_contract_sha256') == digest(c),
            'the candidate is not REVIEWED for this contract — an end-of-day closeout marks it only after the ARGUS '
            'audit; an intra-day light closeout (audit deferred) commits with commit_check.py instead')
    cand_sha = candidate_check(sc, manifest, c)
    require(cand_sha is not None, 'no review candidate in this manifest (frozen before WQ-583) — use the commit_check path')
    paths = manifest['candidate']['paths']
    require(_run(sc, 'symbolic-ref', '-q', 'HEAD').strip() == 'refs/heads/master', 'HEAD is not on master')
    head = resolve(sc, 'HEAD')
    require(ancestor(sc, c['anchor'], head), 'the frozen anchor is not an ancestor of HEAD')
    moved = [p for p in paths if tree_entry(sc, head, p) != tree_entry(sc, c['anchor'], p)]
    require(not moved, 'changed on master since the freeze — re-freeze: ' + ', '.join(sorted(moved)))
    drift = sorted(p for p, want in paths.items() if sc._content_id(p) != want)
    carry = set(carry)
    require(not (set(drift) - carry), 'post-freeze edits are NOT in the reviewed candidate — re-freeze to ship them '
            'tonight, or name each with --carry to leave it for the bookkeeping commit: ' + ', '.join(sorted(set(drift) - carry)))
    require(not (carry - set(drift)), '--carry names a path with no post-freeze edit: ' + ', '.join(sorted(carry - set(drift))))
    require(not (sc.ROOT / _run(sc, 'rev-parse', '--git-path', 'index.lock').strip()).exists(),
            'the shared index is locked by another git process — retry')   # read #3 ⚠️5
    staged = []
    for p in paths:
        rows = [r for r in _run(sc, 'ls-files', '-s', '-z', '--', p).split('\0') if r]
        mine = [tuple(r.split('\t', 1)[0].split()) for r in rows if r.split('\t', 1)[1] == p]
        ok = {None if tree_entry(sc, head, p) is None else tree_entry(sc, head, p) + ('0',),
              None if tree_entry(sc, cand_sha, p) is None else tree_entry(sc, cand_sha, p) + ('0',)}
        if (mine[0] if len(mine) == 1 else None if not mine else 'conflict') not in ok:
            staged.append(p)
    require(not staged, 'the shared index holds another version of: ' + ', '.join(staged) + ' — stop; never reset it')
    text = Path(msg_file).read_text(encoding='utf-8')
    subject = next((ln for ln in text.split('\n') if ln.strip()), '')
    require(subject and len(subject) <= 100, f'commit subject empty or {len(subject)} > 100 chars (root Git Protocol 4d)')
    import tempfile
    lines = []
    for p in sorted(paths):
        e = tree_entry(sc, cand_sha, p)
        lines.append(f'{e[0]} {e[1]}\t{p}' if e else f'0 {NULL_SHA}\t{p}')
    data = ('\n'.join(lines) + '\n').encode()
    with tempfile.TemporaryDirectory() as td:
        env = {'GIT_INDEX_FILE': str(Path(td) / 'index')}
        _run(sc, 'read-tree', head, env=env)
        _run(sc, 'update-index', '--index-info', env=env, data=data)
        tree = _run(sc, 'write-tree', env=env).strip()
        require(tree != _run(sc, 'rev-parse', head + '^{tree}').strip(), 'nothing to deliver — HEAD already holds the candidate')
        run_commit_hooks(sc, env, msg_file, td)   # reader 2026-10-31 ❌2: the repo's own hooks, on THIS commit's index
        require(_run(sc, 'write-tree', env=env).strip() == tree,
                'a pre-commit hook changed the index — commit it the ordinary way')   # reader #2 ⚠️4
    new = _run(sc, 'commit-tree', tree, '-p', head, '-F', str(Path(msg_file).resolve())).strip()
    _run(sc, 'update-ref', '-m', 'argus deliver-candidate (WQ-583)', 'refs/heads/master', new, head)
    try:
        _run(sc, 'update-index', '--index-info', data=data)
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(f'DELIVERED {new} but the shared index was not synced ({exc.stderr.decode()[:200]}); '
                           f'retry: git update-index --index-info with the {len(lines)} candidate entries') from exc
    return new, sorted(paths)
