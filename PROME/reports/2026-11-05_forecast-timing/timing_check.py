#!/usr/bin/env python3
"""One-off timing check for forecast report 1 (Will 2026-11-05 15:48 ET). Not a monitor. Read-only on ledgers.
For each scored row: when did the probability used first enter Git, and what is the earliest date the outcome could be known?"""
import csv, datetime as dt, json, os, re, subprocess, sys, zoneinfo
sys.path.insert(0, 'PROME/tools')
import forecast_report as f
ET = zoneinfo.ZoneInfo('America/New_York')
MON = {m: i + 1 for i, m in enumerate('jan feb mar apr may jun jul aug sep oct nov dec'.split())}
TODAY = dt.date(2026, 11, 5)

def run(*a):
    return subprocess.run(a, capture_output=True, text=True, errors='replace').stdout

def dates_in(s, made):
    out = set()
    for y, m, d in re.findall(r'(20\d\d)-(\d\d)-(\d\d)', s):
        try: out.add(dt.date(int(y), int(m), int(d)))
        except ValueError: pass
    t = re.sub(r'20\d\d-\d\d-\d\d', ' ', s)
    for m, d, y in re.findall(r'(?<![\d/.$-])(\d{1,2})/(\d{1,2})(?:/(\d{2,4}))?(?![\d/%])', t):
        yy = int(y) + (2000 if y and len(y) == 2 else 0) if y else 2026
        try: out.add(dt.date(yy, int(m), int(d)))
        except ValueError: pass
    for mo, d in re.findall(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+(\d{1,2})\b(?!\s*(?:bp|%|pct))', t):
        try: out.add(dt.date(2026, MON[mo.lower()], int(d)))
        except ValueError: pass
    return {x for x in out if (made is None or x >= made) and x <= TODAY}

def parse_iso(s):
    m = re.search(r'(20\d\d)-(\d\d)-(\d\d)', s or '')
    try: return dt.date(*map(int, m.groups())) if m else None
    except ValueError: return None

def history(path):
    """{row id: [(ct, p, sha)]} across every version of the ledger, following renames."""
    log = run('git', 'log', '--follow', '--reverse', '--format=@%H %ct', '--name-only', '--', path).splitlines()
    vers, cur = [], None
    for l in log:
        if l.startswith('@'):
            sha, ct = l[1:].split(); cur = [sha, int(ct), None]; vers.append(cur)
        elif l.strip() and cur:
            cur[2] = l.strip()
    h = {}
    for sha, ct, name in vers:
        blob = run('git', 'show', f'{sha}:{name or path}')
        L = [l for l in blob.splitlines() if l.strip() and not l.startswith('#')]
        if not L: continue
        hdr = [x.strip() for x in L[0].split('\t')]
        ic = f.col(hdr, 'Confidence', 'conf_tier', 'conf', 'prob'); ip = f.col(hdr, 'Prediction', 'prediction')
        for l in L[1:]:
            c = l.split('\t')
            g = lambda i: c[i].strip() if i is not None and i < len(c) else ''
            p = f.prob(g(ic), g(ip))
            if c[0].strip():
                h.setdefault(c[0].strip(), []).append((ct, p, sha))
    return h, (vers[0][1] if vers else None)

def status_first(desk, rid, p):
    """Earliest STATUS.md commit whose line naming the row carries the same percentage (asmade_audit's surface)."""
    path = f'AGENTS/{desk}/STATUS.md'
    for line in run('git', 'log', '--reverse', '--format=%H %ct', f'-S{rid}', '--', path).splitlines()[:6]:
        sha, ct = line.split()
        for l in run('git', 'show', f'{sha}:{path}').splitlines():
            if re.search(r'\b' + re.escape(rid) + r'\b', l):
                tail = l[l.index(rid):]
                m = f.PCT.search(tail)
                if m and abs(float(m.group(1)) / 100 - p) < .0015:
                    return int(ct), sha
    return None

def desk_first(desk, rid, p):
    """Earliest commit anywhere under the desk's directory with a line naming the row and the same percentage."""
    root = f'AGENTS/{desk}'
    for line in run('git', 'log', '--reverse', '--format=%H %ct', f'-S{rid}', '--', root).splitlines()[:8]:
        sha, ct = line.split()
        for l in run('git', 'grep', '-h', '-F', rid, sha, '--', root).splitlines():
            for m in f.PCT.finditer(l):
                if abs(float(m.group(1)) / 100 - p) < .0015:
                    return int(ct), sha
    return None

rows, _ = f.read_all(f.load_bucket())
sc = [r for r in rows if r['bucket'] in ('HIT', 'MISS') and r['p'] is not None]
paths = {r[0].split('/')[1]: [] for r in f.registry()}
for p, _, _ in f.registry():
    paths[p.split('/')[1]].append(p)
out = []
cache = {}
for r in sc:
    best = None
    revised = False
    for path in paths[r['desk']]:
        if path not in cache:
            cache[path] = history(path)
        h, _ = cache[path]
        H = h.get(r['id'])
        if H:
            vals = [x[1] for x in H if x[1] is not None]
            revised = revised or len({round(v, 4) for v in vals}) > 1
            ok = [x for x in H if x[1] is not None and abs(x[1] - r['p']) < .0015]
            if ok and (best is None or ok[0][0] < best[0]):
                best = (ok[0][0], ok[0][2], path)
    # the full Outcome and resolved cells, read from the current ledger row
    made = parse_iso(r['made'])
    res = None
    for path in paths[r['desk']]:
        hdr, rr = f.norm_rows(path)
        for c in rr:
            if c and c[0].strip() == r['id']:
                i = f.col(hdr, 'Date_Resolved', 'Resolution_Date', 'resolved')
                if i is not None and i < len(c): res = parse_iso(c[i])
    ds = dates_in(r['outcome'], made)
    if res: ds.add(res)
    K = min(ds) if ds else None
    src = 'ledger'
    t0 = dt.datetime.fromtimestamp(best[0], ET).date() if best else None
    if K is None or t0 is None or t0 >= K:
        s = status_first(r['desk'], r['id'], r['p']) or desk_first(r['desk'], r['id'], r['p'])
        if s:
            t1 = dt.datetime.fromtimestamp(s[0], ET).date()
            if t0 is None or t1 < t0:
                t0, src = t1, 'desk-history'
    if t0 is None: cls = 'NO-GIT-RECORD'
    elif K is None: cls = 'NO-OUTCOME-DATE'
    elif t0 < K: cls = 'VERIFIED-BEFORE'
    elif t0 == K: cls = 'SAME-DAY'
    else: cls = 'AFTER'
    out.append({'desk': r['desk'], 'id': r['id'], 'p': r['p'], 'bucket': r['bucket'], 'basis': r['basis'], 'first_value_date': str(t0), 'surface': src,
                'earliest_outcome_date': str(K), 'made': r['made'][:10], 'revised_in_git': revised, 'was_mark': r['first'] is not None, 'class': cls, 'conf': r['conf'][:60]})
json.dump(out, open('PROME/reports/2026-11-05_forecast-timing/rows.json', 'w', encoding='utf8'), ensure_ascii=False, indent=0)
print(len(out))
