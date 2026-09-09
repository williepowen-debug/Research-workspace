#!/usr/bin/env python3
"""Dated Totan meeting-OIS indications, ingested after visual image review.

SAM reviews each new chart into workbook/boj_ois_reviews/*.json. Boot verifies
the live image hash, dates and arithmetic before writing BOJ_MEETING_OIS.tsv.
A changed image requires a new visual read; no stale fallback or automatic OCR.
--no-write validates live evidence; --history displays explicitly historical data.
Legacy BOJ_OIS.tsv is frozen, never a fallback. No trading alerts.
"""
import argparse
import csv
import hashlib
import json
import math
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

SAM = Path(__file__).resolve().parents[1]
SOURCE_URL = 'https://www.totan.com/archives/15647'
LEDGER = SAM / 'workbook/BOJ_MEETING_OIS.tsv'
REVIEWS = SAM / 'workbook/boj_ois_reviews'
JST = timezone(timedelta(hours=9))
MAX_AGE = timedelta(days=4)
COLUMNS = ['quote_as_of', 'timezone_basis', 'meeting_month', 'term_start', 'term_end',
           'ois_pct', 'difference_pct', 'incremental_25bp_equivalent_pct',
           'cumulative_expected_hikes', 'step_pct', 'quote_kind', 'source_url',
           'image_url', 'image_sha256', 'method', 'valid_until', 'quality', 'pulled_at']


class SourceError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise SourceError(message)


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.text = []

    def handle_data(self, data):
        self.text.append(data)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'img' and 'wp-image-' in attrs.get('class', ''):
            self.images.append(attrs.get('src', ''))


def table_url(html):
    page = Page()
    page.feed(html)
    text = ' '.join(' '.join(page.text).lower().split())
    for marker in ('business day following the meeting', 'increments of 0.25%',
                   'indicative levels', 'only the impact of monetary policy'):
        require(marker in text, f'Source methodology missing: {marker}')
    require(len(page.images) == 2, 'Expected table then cumulative chart; review source layout')
    for url in page.images:
        parsed = urlparse(url)
        require(parsed.scheme == 'https' and parsed.netloc in
                {'www.totan.com', 'www.tokyotanshi.co.jp'} and
                parsed.path.startswith('/wp-content/uploads/') and parsed.path.endswith('.png'),
                'Unexpected source image URL')
    return page.images[0]


def fetch(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 SAM research'})
    with urllib.request.urlopen(request, timeout=25) as response:
        data = response.read(5_000_001)
    require(len(data) <= 5_000_000, 'Source exceeds size limit')
    return data


def finite(value):
    require(isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value), 'Non-finite or non-numeric quote')
    return float(value)


def validate(review, image, url, now):
    require(now.tzinfo is not None, 'Validation clock requires timezone')
    require(image.startswith(b'\x89PNG\r\n\x1a\n'), 'Expected PNG, not error HTML')
    require(review['schema_version'] == 1 and review['source_url'] == SOURCE_URL,
            'Unrecognized review schema/source')
    require(review['image_url'] == url, 'Reviewed URL differs from live table')
    require(hashlib.sha256(image).hexdigest() == review['image_sha256'],
            'Chart changed: visually review new image; no current quote available')
    require(review['review_method'] == 'SAM visual transcription', 'Unrecognized review method')
    require(review['quote_kind'] == 'indicative OTC meeting-to-meeting OIS median',
            'Instrument kind changed')
    require(review['timezone_basis'] == 'JST assumed from Japanese publisher; image has no zone',
            'Timezone assumption must be explicit')
    asof = datetime.fromisoformat(review['quote_as_of'])
    require(asof.tzinfo is not None and asof.utcoffset() == timedelta(hours=9), 'Bad quote timezone')
    require(timedelta(0) <= now - asof <= MAX_AGE, 'Quote future-dated or older than four days')
    until = date.fromisoformat(review['valid_until'])
    require(asof.date() < until and now.astimezone(JST).date() < until,
            'Quote expired at nearest policy decision date')
    require(bool(review['decision_date_source']), 'Nearest decision date needs provenance')
    step = finite(review['step_pct'])
    require(step == 0.25, 'Expected 25bp source assumption')
    rows = review['rows']
    require(2 <= len(rows) <= 12, 'Incomplete or excessive curve')
    require(len(rows) == review['reviewed_row_count'], 'Transcription does not cover reviewed image rows')
    prior_month, prior_end, prior_ois, total = '', None, None, 0.0
    result = []
    for i, row in enumerate(rows):
        month = date.fromisoformat(row['meeting_month'] + '-01')
        start, end = date.fromisoformat(row['term_start']), date.fromisoformat(row['term_end'])
        require(row['meeting_month'] > prior_month and start <= end and
                (prior_end is None or start > prior_end), 'Duplicate/out-of-order meeting or term')
        require(asof.date() < start and month <= start and (start - month).days <= 40
                and (end - start).days <= 100, 'Invalid reference term')
        if i == 0:
            require(until.strftime('%Y-%m') == row['meeting_month'] and until < start,
                    'Expiry must be nearest decision month and precede reference term')
        ois, diff = finite(row['ois_pct']), finite(row['difference_pct'])
        inc, cumulative = finite(row['incremental_25bp_equivalent_pct']), finite(row['cumulative_expected_hikes'])
        require(-2 <= ois <= 10 and -1 <= diff <= 1 and -4 <= cumulative <= 40,
                'Quote outside reviewed operating range')
        if prior_ois is not None:
            require(abs((ois - prior_ois) - diff) <= .000151, 'OIS difference arithmetic failed')
        require(abs(diff / step * 100 - inc) <= .55, 'Incremental equivalent arithmetic failed')
        total += diff / step
        require(abs(total - cumulative) <= .011, 'Cumulative count arithmetic failed')
        result.append(dict(quote_as_of=review['quote_as_of'], timezone_basis=review['timezone_basis'],
                           **row, step_pct=step, quote_kind=review['quote_kind'], source_url=SOURCE_URL,
                           image_url=url, image_sha256=review['image_sha256'],
                           method=review['review_method'], valid_until=review['valid_until'],
                           quality='REVIEWED_INDICATIVE', pulled_at=now.astimezone(timezone.utc).isoformat()))
        require(set(result[-1]) == set(COLUMNS), 'Unexpected or missing curve columns')
        prior_month, prior_end, prior_ois = row['meeting_month'], end, ois
    return result


def read_rows(path):
    if not path.exists():
        return []
    with path.open(newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        require(reader.fieldnames == COLUMNS, 'Stored ledger schema mismatch')
        rows = list(reader)
    require(all(set(r) == set(COLUMNS) and None not in r.values() for r in rows), 'Malformed ledger row')
    return rows


def append_rows(rows, path=LEDGER):
    existing = read_rows(path)
    key = lambda r: (r['quote_as_of'], r['meeting_month'])
    known = {key(r): r for r in existing}
    require(len(known) == len(existing), 'Duplicate stored quote keys')
    new = []
    for row in rows:
        old = known.get(key(row))
        if old is not None:
            require(all(str(old[c]) == str(row[c]) for c in COLUMNS if c != 'pulled_at'),
                    'Same-vintage revision: preserve history and adjudicate; no overwrite')
        else:
            new.append(row)
    if new:
        require(not existing or rows[0]['quote_as_of'] >= max(r['quote_as_of'] for r in existing),
                'Refusing older curve ingestion')
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix('.tmp')
        with tmp.open('w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=COLUMNS, delimiter='\t', lineterminator='\n')
            writer.writeheader()
            writer.writerows(existing + new)
        tmp.replace(path)
    return len(new)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--no-write', action='store_true')
    parser.add_argument('--history', action='store_true')
    args = parser.parse_args(argv)
    try:
        if args.history:
            print('HISTORICAL stored indications, not current verification; legacy BOJ_OIS.tsv frozen.')
            for row in read_rows(LEDGER):
                print(row['quote_as_of'], row['meeting_month'], row['incremental_25bp_equivalent_pct'],
                      row['cumulative_expected_hikes'])
            return 0
        now = datetime.now(timezone.utc)
        url = table_url(fetch(SOURCE_URL).decode('utf-8'))
        image = fetch(url)
        digest = hashlib.sha256(image).hexdigest()
        reviews = [json.loads(p.read_text()) for p in sorted(REVIEWS.glob('*.json'))]
        matches = [r for r in reviews if r.get('image_sha256') == digest and r.get('image_url') == url]
        require(len(matches) == 1, f'Unreviewed/ambiguous chart {url} SHA256 {digest}; visual review required')
        rows = validate(matches[0], image, url, now)
        print(f"Latest Totan OIS — source quote {rows[0]['quote_as_of']}; checked {now.isoformat()}")
        print(f"Latest nearest meeting {rows[0]['meeting_month']}: "
              f"{rows[0]['incremental_25bp_equivalent_pct']:g}% incremental 25bp equivalent; "
              f"OIS {rows[0]['ois_pct']:.4f}%; indicative, not traded.")
        print('INDICATIVE OTC medians; 25bp increments; JST assumed. No last-trade timestamp.')
        print('Meeting | OIS % | incremental 25bp equivalent % | cumulative expected hikes | reference term')
        for r in rows:
            print(f"{r['meeting_month']} | {r['ois_pct']:.4f} | {r['incremental_25bp_equivalent_pct']:g} | "
                  f"{r['cumulative_expected_hikes']:.2f} | {r['term_start']} to {r['term_end']}")
        print('Cumulative counts are NOT cumulative probabilities; incremental equivalents depend on the model.')
        print('⚠️ Changed chart requires visual review; cumulative counts are not probabilities. Legacy source retired.')
        if not args.no_write:
            print(f'BOJ_MEETING_OIS.tsv: {append_rows(rows)} new rows.')
        return 0
    except (SourceError, OSError, ValueError, KeyError, TypeError) as exc:
        print(f'ALERT BOJ OIS UNAVAILABLE — {exc}. No current quote written.', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
