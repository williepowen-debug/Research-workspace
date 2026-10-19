"""Bookmark continuation and review receipts. No credential-file reads; fetching uses injected transport callbacks.

Cursor sidecars match the repository's *_token.json ignore rule. A portable
boolean in the seen ledger forces safe recovery when those local files are lost.
All paths derive from the caller's seen path, including isolated test paths.
"""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[3]
DISPOSITIONS = {'DISPATCH', 'FOLD', 'DUP', 'NOTE', 'KILL', 'NO-ACTION'}
READ_STATES = {'fully_read', 'partly_read', 'unread'}
STATE_KEYS = {'schema', 'incomplete', 'next_token', 'baseline', 'full_walk',
              'started_at', 'head_checked_at'}


def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def path_for(seen_path, name):
    return Path(seen_path).parent / ('x_bookmarks_' + name + '.json')


def atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')
    os.replace(temporary, path)


def read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding='utf-8'))
    except (OSError, UnicodeError, ValueError) as exc:
        raise SystemExit(f'REFUSING: cannot read {Path(path).name} ({type(exc).__name__}). No IDs marked.')


def validate_state(value):
    if not isinstance(value, dict) or set(value) != STATE_KEYS or type(value.get('schema')) is not int or value.get('schema') != 1:
        raise SystemExit('REFUSING: invalid bookmark continuation schema. No IDs marked.')
    if (type(value['incomplete']) is not bool or type(value['full_walk']) is not bool
            or not isinstance(value['baseline'], list)
            or any(not isinstance(x, str) for x in value['baseline'])
            or not isinstance(value['started_at'], str)
            or not isinstance(value['head_checked_at'], (str, type(None)))
            or not isinstance(value['next_token'], (str, type(None)))):
        raise SystemExit('REFUSING: invalid bookmark continuation fields. No IDs marked.')
    if not value['incomplete'] and value['next_token'] is not None:
        raise SystemExit('REFUSING: completed continuation still has a cursor. No IDs marked.')
    return value


def begin_scan(seen_path, seen):
    cursor = path_for(seen_path, 'scan_token')
    if cursor.exists():
        state = validate_state(read_json(cursor))
        if state['incomplete']:
            return state
    # Missing/legacy completion guard means unknown older coverage, not caught up.
    complete = seen.get('scan_complete', False)
    return {'schema': 1, 'incomplete': True, 'next_token': None,
            'baseline': list(seen['consumed']) if complete else [],
            'full_walk': not complete, 'started_at': now(), 'head_checked_at': None}


def reject_cursor(seen_path, state):
    restart = dict(state, next_token=None)
    atomic_json(path_for(seen_path, 'scan_token'), validate_state(restart))


class ScanBatch(list):
    def __init__(self, items, checkpoint, scan):
        super().__init__(items)
        self.checkpoint, self.scan = checkpoint, scan


def stage(seen_path, ids, checkpoint=None, scan=None):
    value = {'ids': list(ids), 'staged_at': __import__('time').time(),
             'review_required': True, 'scan': scan or {}}
    if checkpoint is not None:
        destination = path_for(seen_path, 'next_token')
        atomic_json(destination, validate_state(checkpoint))
        value['checkpoint_hash'] = hashlib.sha256(destination.read_bytes()).hexdigest()
    atomic_json(path_for(seen_path, 'pending'), value)
    receipt = {'kind': 'fetched', 'checked_at': now(), 'items': len(ids),
               'scan': value['scan'], 'review_recorded': False}
    atomic_json(path_for(seen_path, 'receipt'), receipt)
    return receipt


def proposed_checkpoint(seen_path, staged):
    digest = staged.get('checkpoint_hash')
    if digest is None:
        return None  # historical stages had no continuation
    destination = path_for(seen_path, 'next_token')
    try:
        actual = hashlib.sha256(destination.read_bytes()).hexdigest()
    except OSError:
        actual = None
    if not isinstance(digest, str) or actual != digest:
        raise SystemExit('REFUSING: staged continuation is missing/changed. Re-scan; no IDs marked.')
    return validate_state(read_json(destination))


def commit_checkpoint(seen_path, checkpoint):
    if checkpoint is not None:
        atomic_json(path_for(seen_path, 'scan_token'), validate_state(checkpoint))


def validate_stage(staged):
    if (not isinstance(staged, dict) or not isinstance(staged.get('ids'), list)
            or any(not isinstance(key, (str, int)) or isinstance(key, bool) for key in staged['ids'])):
        raise SystemExit('REFUSING: staged IDs must be plain IDs. No IDs marked.')
    normalized = [str(key) for key in staged['ids']]
    if len(set(normalized)) != len(normalized):
        raise SystemExit('REFUSING: duplicate staged IDs. Re-scan; no IDs marked.')
    return dict(staged, ids=normalized)


def review_template(seen_path, destination):
    staged = validate_stage(read_json(path_for(seen_path, 'pending')))
    if not isinstance(staged, dict) or not staged.get('ids'):
        raise SystemExit('No staged bookmarks. No scan performed.')
    value = {'schema': 1, 'staged_at': staged['staged_at'], 'items': [
        {'id': key, 'disposition': None, 'read_state': None,
         'follow_up': None, 'ask_user': None} for key in staged['ids']]}
    # Create-only: never overwrite a completed review, seen file or credential file.
    with Path(destination).open('x', encoding='utf-8') as stream:
        stream.write(json.dumps(value, indent=2) + '\n')
    print(f'Review template: {destination}. Fill one disposition/read state per ID; no scan performed.')


def load_review(destination, staged):
    value = read_json(destination)
    if (not isinstance(value, dict) or set(value) != {'schema', 'staged_at', 'items'}
            or value.get('schema') != 1 or value.get('staged_at') != staged['staged_at']
            or not isinstance(value.get('items'), list)):
        raise SystemExit('REFUSING: review does not match this staged scan. No IDs marked.')
    found = set()
    for item in value['items']:
        if not isinstance(item, dict) or set(item) != {'id', 'disposition', 'read_state', 'follow_up', 'ask_user'}:
            raise SystemExit('REFUSING: invalid review fields. No IDs marked.')
        key = item['id']
        if (not isinstance(key, str) or key in found
                or not isinstance(item['disposition'], str) or item['disposition'] not in DISPOSITIONS
                or not isinstance(item['read_state'], str) or item['read_state'] not in READ_STATES):
            raise SystemExit('REFUSING: incomplete/duplicate review item. No IDs marked.')
        found.add(key)
        if item['read_state'] == 'unread' and item['disposition'] == 'KILL':
            raise SystemExit('REFUSING: unread is not rejected; keep the reading gap explicit.')
        for field in ['follow_up', 'ask_user']:
            text = item[field]
            if text is not None and (not isinstance(text, str) or not text.strip() or len(text) > 500):
                raise SystemExit('REFUSING: follow-up/request must be a concise reference or own note.')
        if item['follow_up']:
            path = Path(item['follow_up'].split('#', 1)[0])
            if (path.is_absolute() or '..' in path.parts
                    or not (ROOT / path).resolve().is_relative_to(ROOT)
                    or not (ROOT / path).is_file()):
                raise SystemExit('REFUSING: follow-up artifact must exist inside the repository.')
        if item['ask_user'] and item['read_state'] == 'fully_read':
            raise SystemExit('REFUSING: missing-content request conflicts with fully_read.')
        if (item['disposition'] in {'DISPATCH', 'FOLD'} and item['read_state'] != 'fully_read'
                and not (item['follow_up'] or item['ask_user'])):
            raise SystemExit('REFUSING: material unread/partial content needs a follow-up or explicit request.')
    if found != set(staged['ids']) or len(found) != len(staged['ids']):
        raise SystemExit('REFUSING: review IDs must exactly match the stage. No IDs marked.')
    return value['items']


def mark_receipt(seen_path, staged, review):
    value = {'kind': 'marked', 'checked_at': now(), 'items': len(staged['ids']),
             'scan': staged.get('scan', {}), 'review_recorded': review is not None,
             'read_counts': dict(Counter(x['read_state'] for x in review or [])),
             'dispositions': dict(Counter(x['disposition'] for x in review or [])),
             'follow_ups': [{'id': x['id'], 'ref': x['follow_up']} for x in review or [] if x['follow_up']],
             'requests': [{'id': x['id'], 'request': x['ask_user']} for x in review or [] if x['ask_user']]}
    atomic_json(path_for(seen_path, 'receipt'), value)
    return value


def print_receipt(value):
    print('\nBookmark receipt — ' + value['checked_at'])
    scan = value.get('scan', {})
    if value['kind'] == 'fetched' and value['items']:
        print(f"Fetched {value['items']} item(s); review is not yet recorded.")
    elif value['kind'] == 'marked' and value['review_recorded']:
        print(f"Reviewed/marked {value['items']} item(s); reading labels are WALTER's attestation.")
        counts = value['read_counts']
        print(f"Fully read {counts.get('fully_read', 0)}; partly read {counts.get('partly_read', 0)}; unread {counts.get('unread', 0)}.")
        print('Dispositions: ' + ', '.join(f'{key} {n}' for key, n in sorted(value['dispositions'].items())))
    elif value['kind'] == 'marked':
        print(f"Marked {value['items']} legacy staged item(s); reading/disposition details unrecorded.")
    else:
        print('No new items returned in this traversal segment.')
    if scan.get('incomplete'):
        print('Older coverage INCOMPLETE; continue at a later human-watched scan. Remaining count unknown.')
    elif scan and not scan.get('head_checked_this_run'):
        print('Reached the end of the older traversal; a fresh head scan is still needed. Coverage across remote list changes is unverified.')
    elif scan:
        print('Returned traversal complete through its recorded head check; this is not owner consumption or a remote snapshot guarantee.')
    else:
        print('Traversal coverage unrecorded; do not claim caught up.')
    if scan:
        print('Latest head check: ' + str(scan.get('head_checked_at') or 'not completed'))
        if not scan.get('head_checked_this_run'):
            print('This run resumed older pages; newer bookmarks were not checked this run.')
    for item in value.get('follow_ups', []):
        print(f"Follow-up {item['id']}: {item['ref']}")
    for item in value.get('requests', []):
        print(f"Missing content for {item['id']}: {item['request']}")


def show_receipt(seen_path):
    source = path_for(seen_path, 'receipt')
    if not source.exists():
        print('No bookmark receipt recorded. Queue status unknown; no scan performed.')
        return
    print_receipt(read_json(source))


def fetch_batch(env, seen, *, seen_path, get_page, requests, refresh, rotate,
                parse, select, max_pages, page_size):
    """Bounded fetch with an unchanging pre-traversal seen baseline.

    Transport callbacks are supplied by the reader. No checkpoint advances here;
    the returned proposal is committed only with marking (or a zero-new page).
    """
    state = begin_scan(seen_path, seen)
    baseline = set(state['baseline'])
    token, page = env['X_BOOKMARK_ACCESS_TOKEN'], state['next_token']
    collected, refreshed, head_checked, attempts = [], False, False, 0
    while attempts < max_pages:
        attempts += 1
        try:
            data, users, media, meta = get_page(env['X_USER_ID'], token, page)
        except requests.HTTPError as exc:
            code = exc.response.status_code if exc.response is not None else None
            if code == 401 and not refreshed:
                if not (env.get('X_CLIENT_ID') and env.get('X_BOOKMARK_REFRESH_TOKEN')):
                    raise SystemExit('Access token rejected; re-authorize. No IDs marked.')
                try:
                    token, replacement = refresh(env['X_CLIENT_ID'], env['X_BOOKMARK_REFRESH_TOKEN'],
                                                 env.get('X_CLIENT_SECRET'))
                except Exception:
                    raise SystemExit('Token refresh failed; re-authorize. No IDs marked.')
                updates = {'X_BOOKMARK_ACCESS_TOKEN': token, 'X_BOOKMARK_REFRESH_TOKEN': replacement}
                rotate(updates)
                env.update(updates)
                refreshed = True
                continue
            if code == 400 and page is not None:
                reject_cursor(seen_path, state)
                raise SystemExit('Pagination cursor rejected. Coverage remains INCOMPLETE; next human-watched scan restarts safely. No IDs marked.')
            raise SystemExit(f'Bookmark API error {code}. Coverage not certified; no IDs marked.')
        except Exception as exc:
            raise SystemExit(f'Bookmark fetch failed ({type(exc).__name__}). No IDs marked.')
        if page is None:
            state['head_checked_at'], head_checked = now(), True
        if not isinstance(meta, dict):
            raise SystemExit('Invalid pagination metadata; coverage not certified, no IDs marked.')
        parsed = [parse(item, users, media) for item in data]
        collected.extend(parsed)
        keys = {item['dedup_key'] for item in parsed}
        complete = bool(keys) and not state['full_walk'] and keys <= baseline
        page = meta.get('next_token')
        if page is not None and (not isinstance(page, str) or not page):
            raise SystemExit('Invalid pagination cursor; coverage not certified, no IDs marked.')
        if complete or page is None:
            state.update(incomplete=False, next_token=None, baseline=[])
            break
        state['next_token'] = page
    if state['incomplete']:
        print(f'⚠️ Reached the {max_pages}-attempt bookmark limit (up to {max_pages * page_size} rows). Older coverage remains INCOMPLETE; continuation will be retained after review/mark.')
    # A shifting list may repeat an item on two pages; stage its ID only once.
    unique = {}
    for item in collected:
        unique.setdefault(item['dedup_key'], item)
    items = select(list(unique.values()), seen.get('consumed', []))
    scan = {'checked_at': now(), 'head_checked_at': state['head_checked_at'],
            'head_checked_this_run': head_checked, 'incomplete': state['incomplete'],
            'attempts': attempts}
    return ScanBatch(items, state, scan)
