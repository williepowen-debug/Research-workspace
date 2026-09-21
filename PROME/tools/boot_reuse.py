"""Optional same-context instruction receipts; never a boot or runtime attestation."""
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import tempfile
from zoneinfo import ZoneInfo

try:
    import fcntl
except ImportError:
    fcntl = None

ROOT = Path(__file__).resolve().parents[2]
ELIGIBLE = ('USER.md', 'PROME/BOOT.md')
BASIS = (*ELIGIBLE, 'CLAUDE.md', 'PROME/CLAUDE.md', 'AGENTS.md',
         'PROME/registry/READS.tsv', '.claude/skills/boot/SKILL.md',
         'PROME/.claude/skills/boot/SKILL.md', 'PROME/tools/boot_read.py',
         'PROME/tools/boot_reuse.py')


def today():
    return dt.datetime.now(ZoneInfo('America/New_York')).date().isoformat()


def policy_hashes():
    hashes = {}
    for name in BASIS:
        path = ROOT / name
        if path.resolve() != path:
            raise ValueError('Symlinked policy input; full read required')
        hashes[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return hashes


def valid_digest(value):
    return (isinstance(value, str) and len(value) == 64
            and all(c in '0123456789abcdef' for c in value))


def valid_state(value, scope):
    if not isinstance(value, dict) or set(value) != set(scope) | {
            'date', 'policy_hashes', 'pending_policy_reads', 'reads'}:
        return False
    if type(value.get('version')) is not int:
        return False
    if any(not isinstance(value.get(k), str) or not value[k].strip()
           for k in ('repository', 'context_id')):
        return False
    if any(value.get(k) != v for k, v in scope.items()) or not isinstance(value['reads'], dict):
        return False
    try:
        dt.date.fromisoformat(value['date'])
    except (TypeError, ValueError):
        return False
    hashes, pending = value['policy_hashes'], value['pending_policy_reads']
    if not isinstance(hashes, dict) or set(hashes) != set(BASIS):
        return False
    if not all(valid_digest(digest) for digest in hashes.values()):
        return False
    if (not isinstance(pending, list) or any(not isinstance(p, str) or p not in BASIS for p in pending)
            or len(set(pending)) != len(pending)):
        return False
    for name, row in value['reads'].items():
        if name not in BASIS or not isinstance(row, dict):
            return False
        if set(row) != {'sha256', 'next_offset', 'eof', 'acknowledged'}:
            return False
        digest = row['sha256']
        if not valid_digest(digest):
            return False
        if type(row['eof']) is not bool or type(row['acknowledged']) is not bool:
            return False
        offset = row['next_offset']
        if row['eof']:
            if offset is not None:
                return False
        elif type(offset) is not int or offset <= 0 or row['acknowledged']:
            return False
    return True


def save_state(path, value):
    temporary = None
    try:
        with tempfile.NamedTemporaryFile('w', encoding='utf-8', dir=path.parent,
                                         prefix=path.name + '.', delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(value, stream, sort_keys=True)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def read_with_state(path, page, state_path, context_id, offset=0, expected_sha=None,
                    view='full', reuse=False, acknowledge=False):
    """Read normally unless an explicitly acknowledged, compatible receipt permits reuse.

    Context retention is a CALLER assertion, never proven by this local sidecar.
    Contiguous page receipts prove delivery order only; explicit acknowledgement
    is required after the caller consumes EOF. Locks guard state, not cognition.
    """
    if not isinstance(context_id, str) or not context_id.strip():
        raise ValueError('A retained-context ID is required; otherwise use a full read')
    if (reuse and acknowledge) or ((reuse or acknowledge) and offset):
        raise ValueError('Reuse/acknowledgement require offset 0 and are mutually exclusive')
    source = Path(path).absolute()
    root = ROOT.resolve()

    def full(reason):
        if acknowledge:
            raise ValueError('Cannot acknowledge: ' + reason)
        result = page(path, offset, expected_sha, view)
        result.update(read_kind='FULL', reuse_reason=reason)
        return result

    if source not in [root / p for p in BASIS] or source.resolve() != source or view != 'full':
        return full('not a policy-basis path/full view; always read')
    state_path = Path(state_path).absolute()
    if state_path.resolve().is_relative_to(root) or state_path.resolve() != state_path:
        return full('state must be outside the repository and not symlinked')
    if state_path == source or state_path.suffix != '.json' or fcntl is None:
        return full('unusable state path or unavailable lock support')
    name = source.relative_to(root).as_posix()
    try:
        lock = state_path.with_suffix(state_path.suffix + '.lock').open('a')
    except OSError:
        return full('state unavailable; no receipt recorded')
    with lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            return full('state busy; no receipt recorded')
        try:
            policy, day = policy_hashes(), today()
        except (OSError, ValueError):
            return full('policy basis unavailable; no receipt recorded')
        scope = {'version': 2, 'repository': str(root), 'context_id': context_id}
        missing = False
        try:
            state = json.loads(state_path.read_text())
        except FileNotFoundError:
            state, missing = None, True
        except OSError:
            return full('state unreadable; no receipt recorded')
        except ValueError:
            state = None
        if not valid_state(state, scope):
            new_context = isinstance(state, dict) and valid_state(state, {
                **scope, 'repository': state.get('repository'), 'context_id': state.get('context_id')})
            # Legacy/corrupt receipts cannot identify changed rules. Require
            # the whole basis instead of silently resetting away recovery debt.
            pending = [] if missing or new_context else list(BASIS)
            state = {**scope, 'date': day, 'policy_hashes': policy,
                     'pending_policy_reads': pending, 'reads': {}}
            checkpoint = bool(pending)
        else:
            changed = {p for p in BASIS if state['policy_hashes'][p] != policy[p]}
            state['pending_policy_reads'] = sorted(set(state['pending_policy_reads']) | changed)
            if changed or state['date'] != day:
                state['reads'] = {}
            state.update(date=day, policy_hashes=policy)
            checkpoint = bool(changed)
        pending = state['pending_policy_reads']

        def checkpoint_recovery():
            try:
                save_state(state_path, state)
            except OSError as exc:
                raise ValueError('Policy recovery not saved; abandon reuse for this context and use plain full reads. ' +
                                 'Do not retry old receipts or reset IDs. Required policy reads: ' + ', '.join(BASIS)) from exc

        # Persist observed changes BEFORE a bad digest, page or ACK can raise.
        # Otherwise a subsequent source reversion would erase the observed debt.
        if checkpoint:
            checkpoint_recovery()

        def recovery(result):
            result['pending_policy_reads'] = list(pending)
            if pending:
                result['recovery'] = ('Reuse blocked: fully read each pending path with this state/context, '
                                      'then --ack-read --sha256 its contiguous EOF digest; do not reset state/ID')
            return result

        previous = state['reads'].get(name)
        try:
            result = page(path, offset, expected_sha, view)
        finally:
            # Also run on page errors: a detected change must survive a later
            # reversion. No page/ACK receipt survives a policy race.
            current_policy, current_day = policy_hashes(), today()
            if current_policy != policy or current_day != day:
                changed = {p for p in BASIS if current_policy[p] != policy[p]}
                state['pending_policy_reads'] = sorted(set(pending) | changed)
                state.update(policy_hashes=current_policy, date=current_day, reads={})
                checkpoint_recovery()
                raise ValueError('Source/policy/date changed during read; restart at offset 0')
        digest = result['sha256']
        matching = previous is not None and previous['sha256'] == digest
        if acknowledge:
            if expected_sha is None or not matching or not previous['eof']:
                raise ValueError('Acknowledgement requires contiguous recorded EOF and its digest')
            previous['acknowledged'] = True
            if name in pending:
                pending.remove(name)
            try:
                save_state(state_path, state)
            except OSError as exc:
                raise ValueError('Acknowledgement not saved; full read required') from exc
            return recovery({'path': str(source), 'sha256': digest, 'read_kind': 'ACKNOWLEDGED',
                             'context_id': context_id, 'text': '', 'eof': True, 'next_offset': None})
        if reuse and name in ELIGIBLE and not pending and matching and previous['eof'] and previous['acknowledged']:
            return recovery({'path': str(source), 'sha256': digest, 'read_kind': 'REUSED_IN_CONTEXT',
                    'context_id': context_id, 'text': '', 'eof': True, 'next_offset': None,
                    'limit': 'Retained instructions only; fresh boot checks and live reads still required'})
        contiguous = offset == 0 or (matching and not previous['eof'] and previous['next_offset'] == offset)
        if contiguous:
            state['reads'][name] = {'sha256': digest, 'next_offset': result['next_offset'],
                                    'eof': result['eof'], 'acknowledged': False}
        else:
            state['reads'].pop(name, None)
        try:
            save_state(state_path, state)
            reason = 'page recorded; acknowledge after EOF' if contiguous else 'noncontiguous read; restart to record'
        except OSError:
            reason = 'state unavailable; no receipt recorded'
        result.update(read_kind='FULL', reuse_reason=reason)
        return recovery(result)
