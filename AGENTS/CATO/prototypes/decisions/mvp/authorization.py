"""Explicit owner policy and attested app-only integration. No semantic inference."""
from datetime import datetime
from zoneinfo import ZoneInfo

APP_SCOPE = 'reversible_internal'
SCOPES = {APP_SCOPE, 'trade', 'spending', 'external_send', 'held_position',
          'security', 'destructive', 'other'}


def validate_policy(policy):
    if not isinstance(policy, dict) or set(policy) != {'mode', 'scope', 'reason'}:
        raise ValueError('Confirmation policy requires mode, scope and reason')
    if (not isinstance(policy['mode'], str) or not isinstance(policy['scope'], str)
            or policy['mode'] not in {'app', 'chat'} or policy['scope'] not in SCOPES):
        raise ValueError('Unknown confirmation policy; chat confirmation required')
    if not isinstance(policy['reason'], str) or not policy['reason'].strip() or len(policy['reason']) > 3000:
        raise ValueError('Confirmation policy requires a bounded owner explanation')
    if policy['mode'] == 'app' and policy['scope'] != APP_SCOPE:
        raise ValueError('Only reversible internal work can use app-only confirmation')
    return policy


def policy_for(snapshot):
    source = snapshot.get('options_source') or {}
    policy = source.get('confirmation')
    if policy is None:
        return {'mode': 'chat', 'scope': 'other', 'reason': 'No explicit app-only classification.'}
    return validate_policy(policy)


def needs_chat(snapshot):
    return policy_for(snapshot)['mode'] != 'app'


def readback_text(event):
    r = event['request']
    choice = event.get('selected_choice')
    answer = choice['id'] + ' — ' + choice['label'] if choice else r['action'].replace('_', ' ')
    value = 'WQ-' + event['display']['record']['wq_id'] + ': ' + answer
    if r['note']:
        value += '\n' + r['note']
    if r['revisit']:
        value += '\nReturn: ' + r['revisit']
    return value


def validate_app_integration(repo, event, ruling, at):
    # Imported lazily: pilot_files also reads legacy and new receipt dialects.
    from pilot_files import fields, record_block, timestamp
    if event['kind'] != 'decisions-queue-response/1' or needs_chat(event['display']):
        raise ValueError('This answer requires matching chat confirmation')
    if event['request']['action'] not in {'choose', 'reply', 'defer', 'request_changes'}:
        raise ValueError('This response type is not eligible for app-only integration')
    source = event['display']['options_source']
    if repo.read(source['path'], ruling['commit'], prefix='PROME/proposals') != source['text']:
        raise ValueError('Policy or terms changed before ruling; obtain a fresh answer')
    raw = repo.read(ruling['path'], ruling['commit'], prefix='PROME/proposals')
    proof = record_block(raw, 'decisions-app-authorization')
    fields(proof, {'schema_version', 'response_id', 'response_sha256', 'scope',
                   'conditions_within_scope', 'no_chat_conflict', 'readback_at', 'readback_text'}, 'App authorization')
    if (proof['schema_version'] != 'decisions-app-authorization/1'
            or proof['response_id'] != event['id'] or proof['response_sha256'] != event['sha256']
            or proof['scope'] != APP_SCOPE or proof['conditions_within_scope'] is not True
            or proof['no_chat_conflict'] is not True):
        raise ValueError('Owner scope/conflict attestation is missing or names another answer')
    readback, receipt_at = timestamp(proof['readback_at']), timestamp(at)
    if readback < timestamp(event['saved_at']) or readback > receipt_at:
        raise ValueError('Readback chronology is invalid')
    zone = ZoneInfo('America/New_York')
    if readback.astimezone(zone).date() != receipt_at.astimezone(zone).date():
        raise ValueError('PROME must read the ruling back on the same day')
    if proof['readback_text'] != readback_text(event):
        raise ValueError('Readback must preserve the exact answer and conditions')


def app_only_enabled(repo, event=None):
    """Deployment opt-in; source eligibility alone cannot remove chat confirmation."""
    import subprocess
    from pilot_files import strict_json
    from app import accepted, ACCEPTANCE
    try:
        if not accepted(repo)[0]:
            return False
        raw = repo.read(ACCEPTANCE, 'origin/master', prefix='PROME/decisions')
        if repo.read(ACCEPTANCE, clean=True, prefix='PROME/decisions') != raw:
            return False
        record = strict_json(raw)
        if record.get('app_only_enabled') is not True:
            return False
        from pilot_files import timestamp
        from datetime import timezone
        since = timestamp(record.get('app_only_since'))
        if since > datetime.now(timezone.utc):
            return False
        return event is None or timestamp(event['saved_at']) >= since
    except (ValueError, TypeError, AttributeError, OSError, subprocess.CalledProcessError):
        return False


def requires_chat(repo, snapshot, event=None):
    return needs_chat(snapshot) or not app_only_enabled(repo, event)
