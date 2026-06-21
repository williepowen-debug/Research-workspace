#!/usr/bin/env python3
"""
TERRY Option Chain Intake Parser.

Reads pasted/exported broker option-chain CSV/TSV and normalizes key fields for
Terry trade cards. It does NOT fetch broker data or recommend execution.

Examples:
  python3 AGENTS/TERRY/scripts/chain_parse.py chain.csv --underlying WAL --expiry 2026-09-18
  pbpaste | python3 AGENTS/TERRY/scripts/chain_parse.py - --underlying TLT --type put
  python3 AGENTS/TERRY/scripts/chain_parse.py --selftest

Accepted header aliases include: strike, bid, ask, last, mark/mid, delta, theta,
iv/implied volatility, volume/vol, open interest/oi, type/callput.
"""
from __future__ import annotations
import argparse, csv, io, re, sys
from pathlib import Path

ALIASES = {
    'strike': {'strike','strk'},
    'bid': {'bid'},
    'ask': {'ask'},
    'last': {'last','lastprice','last price'},
    'mark': {'mark','mid','midpoint','price'},
    'delta': {'delta'},
    'theta': {'theta'},
    'iv': {'iv','impliedvolatility','implied volatility','impl vol','implied vol'},
    'volume': {'volume','vol'},
    'open_interest': {'openinterest','open interest','oi','open int'},
    'type': {'type','callput','call/put','putcall','right'},
    'expiry': {'expiry','expiration','exp','expiration date'},
}


def norm(s):
    return re.sub(r'[^a-z0-9]+',' ', str(s).strip().lower()).strip()

def compact(s):
    return norm(s).replace(' ','')

def parse_num(x):
    if x is None: return None
    s=str(x).strip().replace('$','').replace(',','').replace('%','')
    if s in {'','--','-','nan','N/A','n/a'}: return None
    try: return float(s)
    except ValueError: return None

def detect_dialect(text):
    sample=text[:2048]
    if '\t' in sample and sample.count('\t') >= sample.count(','):
        return csv.excel_tab
    return csv.Sniffer().sniff(sample, delimiters=',\t;|')

def map_headers(headers):
    mapped={}
    for i,h in enumerate(headers):
        c=compact(h)
        n=norm(h)
        for field, aliases in ALIASES.items():
            if c in {compact(a) for a in aliases} or n in aliases:
                mapped[field]=i
    return mapped

def load_rows(path):
    text = sys.stdin.read() if str(path) == '-' else Path(path).read_text(errors='replace')
    dialect=detect_dialect(text)
    reader=csv.reader(io.StringIO(text), dialect)
    rows=[r for r in reader if any(cell.strip() for cell in r)]
    if not rows: raise SystemExit('no rows')
    headers=rows[0]
    idx=map_headers(headers)
    if 'strike' not in idx or ('bid' not in idx and 'ask' not in idx and 'mark' not in idx and 'last' not in idx):
        raise SystemExit(f"missing required headers. Found: {headers}. Need strike and at least one price field (bid/ask/mark/last).")
    out=[]
    for r in rows[1:]:
        def get(field):
            j=idx.get(field)
            return r[j] if j is not None and j < len(r) else ''
        bid=parse_num(get('bid')); ask=parse_num(get('ask')); mark=parse_num(get('mark'))
        if mark is None and bid is not None and ask is not None: mark=(bid+ask)/2
        spread = (ask-bid) if bid is not None and ask is not None else None
        spread_pct = (spread/mark*100) if spread is not None and mark not in (None,0) else None
        out.append({
            'strike': parse_num(get('strike')), 'type': str(get('type')).upper()[:1] or '',
            'expiry': get('expiry'), 'bid': bid, 'ask': ask, 'mark': mark, 'last': parse_num(get('last')),
            'delta': parse_num(get('delta')), 'theta': parse_num(get('theta')), 'iv': parse_num(get('iv')),
            'volume': parse_num(get('volume')), 'open_interest': parse_num(get('open_interest')),
            'spread_pct': spread_pct,
        })
    return [r for r in out if r['strike'] is not None]

def fmt(x, dp=2):
    return 'N/A' if x is None else f"{x:.{dp}f}"

def run(args):
    rows=load_rows(args.file)
    if args.type:
        want=args.type[0].upper()
        rows=[r for r in rows if not r['type'] or r['type']==want]
    if args.min_oi is not None:
        rows=[r for r in rows if (r['open_interest'] or 0) >= args.min_oi]
    rows=sorted(rows, key=lambda r: (r['expiry'] or args.expiry or '', r['strike']))
    print('TERRY option-chain intake')
    print('=========================')
    print('Parser only — no broker access, no execution recommendation.\n')
    print(f"Underlying: {args.underlying or 'N/A'} | Expiry filter/context: {args.expiry or 'from file/unspecified'} | Rows: {len(rows)}")
    print('Strike   T  Bid    Ask    Mark   Sprd%   Delta   Theta   IV      Vol    OI')
    print('-------  -  -----  -----  -----  ------  ------  ------  ------  -----  -----')
    wide=[]; thin=[]
    for r in rows[:args.limit]:
        if r['spread_pct'] is not None and r['spread_pct'] > args.wide_spread_pct: wide.append(r)
        if (r['open_interest'] or 0) < args.thin_oi: thin.append(r)
        print(f"{fmt(r['strike']):>7}  {r['type'] or '?':<1}  {fmt(r['bid']):>5}  {fmt(r['ask']):>5}  {fmt(r['mark']):>5}  {fmt(r['spread_pct']):>6}  {fmt(r['delta']):>6}  {fmt(r['theta']):>6}  {fmt(r['iv']):>6}  {fmt(r['volume'],0):>5}  {fmt(r['open_interest'],0):>5}")
    if len(rows) > args.limit: print(f"... {len(rows)-args.limit} more rows omitted; use --limit")
    print('\nTERRY liquidity flags')
    print(f"- Wide spread rows >{args.wide_spread_pct:.0f}% of mark in displayed set: {len(wide)}")
    print(f"- Thin OI rows <{args.thin_oi:.0f} OI in displayed set: {len(thin)}")
    print('\nTrade-card reminder: use these fields to justify structure; still requires Will approval before execution.')
    return 0

def selftest():
    sample='''Strike,Type,Bid,Ask,Delta,Theta,IV,Volume,Open Interest\n75,P,1.20,1.45,-0.31,-0.02,42.5,14,380\n80,P,2.10,2.45,-0.45,-0.03,44.1,22,125\n'''
    tmp=Path('/tmp/terry_chain_selftest.csv'); tmp.write_text(sample)
    rows=load_rows(tmp)
    assert len(rows)==2 and rows[0]['mark']==1.325 and round(rows[1]['spread_pct'],2)==15.38
    tmp.unlink(missing_ok=True)
    print('chain_parse.py SELFTEST: PASS')
    return 0

def main():
    ap=argparse.ArgumentParser(description='TERRY option-chain intake parser')
    ap.add_argument('file', nargs='?', help='CSV/TSV path or - for stdin')
    ap.add_argument('--underlying')
    ap.add_argument('--expiry')
    ap.add_argument('--type', choices=['call','put','c','p'])
    ap.add_argument('--min-oi', type=float)
    ap.add_argument('--limit', type=int, default=40)
    ap.add_argument('--wide-spread-pct', type=float, default=15.0)
    ap.add_argument('--thin-oi', type=float, default=100.0)
    ap.add_argument('--selftest', action='store_true')
    args=ap.parse_args()
    if args.selftest: return selftest()
    if not args.file: raise SystemExit('file required unless --selftest')
    return run(args)

if __name__ == '__main__':
    raise SystemExit(main())
