#!/usr/bin/env python3
"""Read declared PROFILE body vintages and day clocks; never use receipt/git/deadline dates.

rc0: evaluated dated clocks inside window; rc1: overdue; rc2: cannot evaluate at
least one profile (known overdue findings still print). Content triggers remain
agent-judged. DAEDALUS owns failures: verify declared metadata or refresh/banner
under UPGRADE_PROTOCOL step 0. Bias: ambiguous metadata refuses certification.

Production acceptance set (frozen verbatim, with source paths/hashes in manifest):
scripts/tests/fixtures/profile_clock/{FERT,BROCK,OSPREY,BRENT,CORAL,CARL}.md.
FERT is real clean; BROCK is real overdue; OSPREY reproduces receipt false-clear;
BRENT/CORAL reproduce future-checkpoint pollution; CARL metadata follows a Δ heading.
Re-run scripts/tests/test_profile_clock_check.py on each material change.
"""
from __future__ import annotations
import argparse
import datetime as dt
import re
from pathlib import Path

PROFILES = Path(__file__).resolve().parent.parent / 'profiles'
DATE = r'20\d\d-\d\d-\d\d'
AUTHOR = re.compile(r'^(?:Built(?: by)?|Body(?: date| vintage)?|Profile vintage|Date)\s*:', re.I)
VINTAGE = re.compile(
    rf'^(?:Profile vintage|Body(?: date| vintage)?|Date|Built|Original|Prior full refresh|'
    rf'Full refresh|Fully rebuilt|Fully rewritten|Rewritten|Refreshed(?:\s*\([^)]*\))?)'
    rf'\s*:?\s*(?:prior\s+)?(?P<date>{DATE})', re.I)
CLOCK = re.compile(r'(?:Staleness(?:\s+triggers?|\s*/\s*refresh clock)?(?:\s*\([^)]*\))?|Refresh triggers?(?:\s*\([^)]*\))?|Day clock|Refresh clock)\s*:', re.I)
DAYS = re.compile(
    r'(?:>|&gt;|\bover\b|\bpast\b|\bor\b)\s*(\d{1,3})\s*(?:days?\b|d\b)'
    r'|\b(\d{1,3})\s*-day\s+clock\b'
    r'|\b(?:day clock|refresh clock)\s*:\s*(\d{1,3})\s*d(?:ays?)?\b'
    r'|\b(\d{1,3})\s*d(?:ays?)?\s*→', re.I)
FLOOR = re.compile(rf'\b(?:hard\s+)?floor\s*[:=]?\s*({DATE})', re.I)
RELATIVE = re.compile(r'STATUS[^\n]*\bstamp\b[^\n]*\bleads\b', re.I)


def metadata(text: str) -> list[str]:
    """Whole-file anchored metadata declarations, including fields after Δ headings.

    Only author lines or standalone clock/vintage declarations qualify. No line
    cap, no arbitrary date extraction, no dates from quotes or body discussion.
    """
    lines = [re.sub(r'[*`]', '', line).strip() for line in text.splitlines()]
    return [line for line in lines if AUTHOR.match(line) or CLOCK.match(line)
            or re.match(r'Sources read(?:\s*\([^)]*\))?\s*:', line, re.I)]


def vintage_of(text: str) -> tuple[dt.date | None, str]:
    declared, explicit, ambiguous = [], [], False
    for line in metadata(text):
        if not AUTHOR.match(line):
            continue
        for segment in line.split(' · '):
            match = VINTAGE.match(segment)
            if not match:
                continue
            # A named delta/partial refresh updates only its scope. A plain author
            # refresh declaration retains its legacy meaning; receipt banners do not.
            if (re.search(r'\b(?:delta|partial)\b', segment[:match.end()], re.I)
                    or re.match(r'\s*\((?:delta|partial)\b', segment[match.end():], re.I)):
                continue
            date = dt.date.fromisoformat(match['date'])
            declared.append((date, match.group(0)))
            if segment.lower().startswith(('profile vintage:', 'body vintage:')):
                explicit.append((date, match.group(0)))
            # Established Body: old, refreshed new form declares a body refresh.
            # Section-only refreshes need an explicit whole-body vintage to certify.
            if segment.lower().startswith('body:'):
                follow = re.match(rf',\s*refreshed\s*:?[ ]*({DATE})', segment[match.end():], re.I)
                if follow:
                    declared.append((dt.date.fromisoformat(follow[1]), 'Body refreshed '+follow[1]))
                elif re.search(r'§.*refreshed', segment[match.end():], re.I):
                    ambiguous = True
    if explicit:
        if len({d for d, _ in explicit}) != 1:
            raise ValueError('conflicting explicit body vintages')
        return explicit[0]
    if ambiguous:
        raise ValueError('section refresh lacks explicit whole-body vintage')
    if declared:
        return max(declared, key=lambda item: item[0])
    return None, 'no declared body vintage (git/receipt dates are not substitutes)'


def clock_of(text: str) -> tuple[int | None, dt.date | None, bool]:
    # Read only named clock fields, never arbitrary refresh mentions in a report.
    fields = []
    for line in metadata(text):
        match = CLOCK.search(line)
        if match:
            fields.append(line[match.start():])
    hay = '\n'.join(fields)
    days = [int(next(g for g in m.groups() if g is not None)) for m in DAYS.finditer(hay)]
    floors = [dt.date.fromisoformat(m[1]) for m in FLOOR.finditer(hay)]
    if any(day <= 0 for day in days):
        raise ValueError('day clock must be positive')
    if re.search(r'\bfloor\b', hay, re.I) and not floors:
        raise ValueError('unparseable floor declaration')
    if re.search(r'\b(?:day|refresh) clock\b', hay, re.I) and not days and not floors:
        raise ValueError('unparseable day clock declaration')
    return min(days) if days else None, min(floors) if floors else None, bool(RELATIVE.search(hay))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--quiet', action='store_true')
    parser.add_argument('--as-of', type=dt.date.fromisoformat, default=dt.date.today())
    parser.add_argument('--profiles', type=Path, default=PROFILES)
    args = parser.parse_args(argv)
    if not args.profiles.is_dir():
        print(f'PROFILE-CLOCK 2 CANNOT-EVALUATE: {args.profiles} missing'); return 2
    paths, excluded = [], []
    for path in sorted(args.profiles.glob('*.md')):
        # Population contract = profiles/<AGENT>.md (uppercase agent name), including
        # retired profiles; companion reader reports/templates are not agents.
        (paths if re.fullmatch(r'[A-Z]+', path.stem) else excluded).append(path)
    fired, ok, undated, cannot = [], [], [], []
    for path in paths:
        try:
            text = path.read_text(encoding='utf-8')
            vintage, basis = vintage_of(text)
            days, floor, relative = clock_of(text)
            if vintage is None:
                raise ValueError(basis)
            age = (args.as_of - vintage).days
            if age < 0:
                raise ValueError(f'declared body vintage {vintage} is after as-of {args.as_of}')
            info = f'{path.stem}: body {vintage}, age {age}d [{basis}]'
            if relative:
                raise ValueError(f'{info}; STATUS-stamp-relative >{days}d trigger needs owner-stamp comparison; wall-clock age is NOT that trigger')
            if days is None and floor is None:
                undated.append(info); continue
            hit = []
            if days is not None and age > days: hit.append(f'{age}d > {days}d')
            if floor is not None and args.as_of > floor: hit.append(f'floor {floor} passed')
            (fired if hit else ok).append(info + '; ' + (', '.join(hit) if hit else f'inside declared window (days={days}, floor={floor})'))
        except (OSError, UnicodeError, ValueError) as exc:
            cannot.append(f'{path.stem}: {exc}')
    if not paths:
        cannot.append('no profiles/<AGENT>.md found')
    print(f'PROFILE-CLOCK perimeter as-of {args.as_of}: {len(paths)} profile(s) attempted (includes retired); '
          f'{len(fired)+len(ok)} dated clocks evaluated; {len(undated)} NO-DATED-CLOCK; {len(cannot)} CANNOT-EVALUATE')
    print('Excluded non-profile filenames: ' + (', '.join(p.name for p in excluded) or 'none'))
    print('NOT certified: content/event triggers, owner STATUS-relative clocks, or truth of declared refresh work. No git-date fallback.')
    for line in undated: print('NO-DATED-CLOCK (agent-judged): ' + line)
    if fired:
        print(f'PROFILE-CLOCK 1: {len(fired)} PAST own day clock — DAEDALUS: refresh/banner under UPGRADE_PROTOCOL step 0')
        for line in fired: print('  ALERT '+line)
    if not args.quiet:
        for line in ok: print('  OK '+line)
    if cannot:
        print('PROFILE-CLOCK 2 CANNOT-EVALUATE — DAEDALUS: verify metadata or compare named owner stamp before certifying')
        for line in cannot: print('  '+line)
        return 2
    if fired: return 1
    print(f'PROFILE-CLOCK 0: {len(ok)} evaluated dated clocks inside window; content/undated profiles NOT certified')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
