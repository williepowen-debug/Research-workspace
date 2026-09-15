"""Offline specification examples only; no production grading or registry writes."""
from datetime import date


def classify(target, *, is_session, completed, valid_archive, published,
             explicit_omission=False):
    # Calendar and completion are established inputs, not inferred from absence.
    if is_session is None:
        return 'UNKNOWN'
    if not is_session:
        return 'NON_SESSION'
    if not completed:
        return 'SESSION_IN_PROGRESS'
    # An authoritative omission notice is not a numerical completing observation.
    if explicit_omission:
        return 'MISSING_SESSION'
    if not valid_archive:
        return 'UNKNOWN'
    # published contains only validated completed-session observations from the
    # declared series. Hash changes, row counts and HTTP 200 are insufficient.
    if target in published:
        return 'PUBLISHED'
    if any(d > target for d in published):
        return 'MISSING_SESSION'
    return 'UNKNOWN'


def main():
    t = date(2026, 9, 16)
    before, after = date(2026, 9, 15), date(2026, 9, 17)
    base = dict(is_session=True, completed=True, valid_archive=True,
                published={before: 151.0})
    cases = [
        ('unchanged latest archive', {}, 'UNKNOWN'),
        ('historical correction changes bytes only',
         {'published': {date(2026, 9, 1): 141.01, before: 151.0}}, 'UNKNOWN'),
        ('same row count but later session proves hole',
         {'published': {before: 151.0, after: 149.0}}, 'MISSING_SESSION'),
        ('valid target tie is an observation, not a fire by itself',
         {'published': {t: 150.0}}, 'PUBLISHED'),
        ('valid sub-threshold target remains available to reset',
         {'published': {t: 149.0}}, 'PUBLISHED'),
        ('HTTP error', {'valid_archive': False}, 'UNKNOWN'),
        ('HTML 200 / invalid schema',
         {'valid_archive': False, 'published': {after: 150}}, 'UNKNOWN'),
        ('session still in progress',
         {'completed': False, 'published': {t: 150}}, 'SESSION_IN_PROGRESS'),
        ('known exchange closure even with stray feed bar',
         {'is_session': False, 'published': {t: 150}}, 'NON_SESSION'),
        ('calendar not established', {'is_session': None}, 'UNKNOWN'),
        ('empty valid historical archive cannot prove coverage',
         {'published': {}}, 'UNKNOWN'),
        ('explicit target-specific publisher omission notice',
         {'explicit_omission': True}, 'MISSING_SESSION'),
        ('later recovery now supplies target',
         {'published': {before: 151, t: 152, after: 153}}, 'PUBLISHED'),
    ]
    for label, changes, expected in cases:
        observed = classify(t, **(base | changes))
        assert observed == expected, (label, observed, expected)
        print('PASS:', label, '=>', observed)
    print(f'{len(cases)} offline specification cases passed. No FT-10 count or grade computed.')


if __name__ == '__main__':
    main()
