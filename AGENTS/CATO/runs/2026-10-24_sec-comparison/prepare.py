#!/usr/bin/env python3
"""Isolated duration-metric comparison; no writes or owner integration.

Use --help for inputs. A filing cutoff limits which filings may be selected;
it does not reconstruct the historical state of SEC's API.
"""
import argparse
from datetime import date, datetime, timezone
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import re
import sys


def iso_day(value):
    return date.fromisoformat(value)


def build(raw, *, cik, concept, unit, prior, current, as_of, retrieved_at):
    data = json.loads(raw)
    if str(data.get('cik')).lstrip('0') != cik.lstrip('0'):
        raise ValueError('Response issuer does not match requested CIK')
    if data.get('taxonomy') != 'us-gaap' or data.get('tag') != concept:
        raise ValueError('Response taxonomy/concept does not match request')
    stamp = datetime.fromisoformat(retrieved_at.replace('Z', '+00:00'))
    if stamp.tzinfo is None:
        raise ValueError('Retrieval timestamp must include timezone')
    cutoff = iso_day(as_of)
    if cutoff > stamp.date():
        raise ValueError('Filing cutoff cannot be later than retrieval date')
    durations = [(iso_day(b) - iso_day(a)).days + 1 for a, b in (prior, current)]
    if min(durations) <= 0 or abs(durations[0] - durations[1]) > 7:
        raise ValueError('Periods have invalid or mismatched durations; comparison withheld')
    if iso_day(prior[1]) >= iso_day(current[0]):
        raise ValueError('Prior and current periods must be ordered and nonoverlapping')
    url = f'https://data.sec.gov/api/xbrl/companyconcept/CIK{int(cik):010d}/us-gaap/{concept}.json'

    def select(period):
        matches = [v for v in data.get('units', {}).get(unit, [])
                   if (v.get('start'), v.get('end')) == tuple(period)]
        if not matches:
            raise ValueError(f'Missing period {period} in unit {unit}; no proxy substituted')
        for v in matches:
            if not v.get('filed'):
                raise ValueError('Matching record lacks filing date')
            iso_day(v['filed'])
        eligible = [v for v in matches if iso_day(v['filed']) <= cutoff]
        if not eligible:
            raise ValueError(f'No filing on or before cutoff for {period}')
        newest = max(v['filed'] for v in eligible)
        latest = [v for v in eligible if v['filed'] == newest]
        identities = set()
        for v in latest:
            if not re.fullmatch(r'\d{10}-\d{2}-\d{6}', v.get('accn', '')) or not v.get('form'):
                raise ValueError('Selected record lacks valid filing identity/form')
            if isinstance(v.get('val'), bool) or not isinstance(v.get('val'), (int, float)) or not math.isfinite(v['val']):
                raise ValueError('Selected record lacks a finite numeric value')
            identities.add((v['accn'], v['val'], v['form']))
        if len(identities) != 1:
            raise ValueError('Ambiguous latest filing/value; explicit source selection needed')
        v = latest[0]
        return {**{k: v.get(k) for k in ('start', 'end', 'val', 'accn', 'form', 'filed', 'fy', 'fp', 'frame')},
                'unit': unit, 'kind': 'reported',
                'filing_url': f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{v['accn'].replace('-', '')}/{v['accn']}-index.html"}

    old, new = select(prior), select(current)
    delta = new['val'] - old['val']
    pct = delta / old['val'] * 100 if old['val'] > 0 else None
    return {'entity': data.get('entityName'), 'cik': cik, 'concept': concept, 'unit': unit,
            'source_url': url, 'retrieved_at': retrieved_at,
            'response_sha256': hashlib.sha256(raw).hexdigest(), 'filing_cutoff': as_of,
            'selection': 'Exact periods/unit; latest filed on or before cutoff; conflicting latest records rejected',
            'prior': old, 'current': new,
            'calculation': {'kind': 'derived', 'difference': delta, 'unit': unit,
                            'formula': 'current.val - prior.val', 'percent_change': pct,
                            'percent_formula': '(current.val - prior.val) / prior.val * 100; omitted when prior <= 0'},
            'limits': ['Filing cutoff is not a historical API snapshot.',
                       'Same concept/unit and similar duration do not establish accounting comparability.',
                       'Standard entity-level US-GAAP facts only; custom tags and segment facts need document work.',
                       'Filing links identify sources; the source statements have not been independently reconciled.']}


def markdown(packet):
    p, c, calc = packet['prior'], packet['current'], packet['calculation']
    lines = [f"# {packet['entity']} — {packet['concept']}", '',
             '| Record | Reporting period | Reported value | Filed | Source |',
             '|---|---|---:|---|---|']
    for label, r in (('Prior', p), ('Current', c)):
        lines.append(f"| {label} | {r['start']} to {r['end']} | {r['val']:,} {r['unit']} | {r['filed']} | [{r['accn']}]({r['filing_url']}) |")
    pct = 'not calculated (prior value is nonpositive)' if calc['percent_change'] is None else f"{calc['percent_change']:+.2f}%"
    lines += ['', f"Calculated change: **{calc['difference']:+,} {calc['unit']}**; {pct}.",
              'Formula: current reported value − prior reported value.', '',
              f"Filing cutoff: {packet['filing_cutoff']}. Retrieved: {packet['retrieved_at']}.",
              f"[SEC data response]({packet['source_url']}); SHA-256 `{packet['response_sha256']}`.", '',
              *[f'- {limit}' for limit in packet['limits']], '']
    return '\n'.join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cik', required=True)
    ap.add_argument('--concept', required=True, help='Standard us-gaap concept')
    ap.add_argument('--unit', required=True)
    ap.add_argument('--prior', nargs=2, required=True, metavar=('START', 'END'))
    ap.add_argument('--current', nargs=2, required=True, metavar=('START', 'END'))
    ap.add_argument('--as-of', required=True, help='Filing-date cutoff, YYYY-MM-DD')
    ap.add_argument('--snapshot', type=Path, help='Saved raw SEC companyconcept JSON; otherwise fetch once')
    ap.add_argument('--retrieved-at', help='Required with snapshot: actual retrieval timestamp including timezone')
    ap.add_argument('--format', choices=('json', 'markdown'), default='json')
    args = ap.parse_args()
    try:
        if not re.fullmatch(r'\d{1,10}', args.cik) or int(args.cik) <= 0:
            raise ValueError('CIK must be 1–10 digits and positive')
        if not re.fullmatch(r'[A-Za-z][A-Za-z0-9]*', args.concept):
            raise ValueError('Invalid US-GAAP concept name')
        if args.snapshot:
            if not args.retrieved_at:
                raise ValueError('--snapshot requires --retrieved-at; file modification time is not provenance')
            raw, retrieved = args.snapshot.read_bytes(), args.retrieved_at
        else:
            if args.retrieved_at:
                raise ValueError('--retrieved-at is only for saved snapshots')
            root = next(p for p in Path(__file__).resolve().parents if (p / 'PROME/ROSTER.md').is_file())
            path = root / 'AGENTS/DEWEY/scripts/edgar_doc.py'
            spec = importlib.util.spec_from_file_location('edgar_transport', path)
            edgar = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(edgar)
            try:
                raw = edgar._get(edgar.CONCEPT.format(cik=f'{int(args.cik):010d}', concept=args.concept), edgar.HJSON)
            except edgar.EdgarError as exc:
                raise ValueError(str(exc)) from exc
            retrieved = datetime.now(timezone.utc).isoformat()
        packet = build(raw, cik=args.cik, concept=args.concept, unit=args.unit,
                       prior=args.prior, current=args.current, as_of=args.as_of, retrieved_at=retrieved)
        print(markdown(packet) if args.format == 'markdown' else json.dumps(packet, indent=2))
        return 0
    except (ValueError, TypeError, KeyError, OSError) as exc:
        print(f'Comparison unavailable: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
