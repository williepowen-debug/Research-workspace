"""LABOR 2026-10-21 C2 base rates — implements domain/sources/2026-10-21_C2_BASE_RATES_PREREG.md (commit f95654e55) exactly."""
import json, sys, datetime as dt
D = sys.argv[1]
def load(s):
    o = json.load(open(f"{D}/{s}.json"))
    return sorted((dt.date.fromisoformat(x['date']), float(x['value'])) for x in o if x['value'] not in ('.', ''))
EX0, EX1 = dt.date(2020,3,1), dt.date(2021,12,31)
inex = lambda d: EX0 <= d <= EX1
def overlaps(a, b): return not (b < EX0 or a > EX1)
def addm(d, n):
    y, m = divmod(d.month - 1 + n, 12); return dt.date(d.year + y, m + 1, 1)

def weekly_rel(series):
    v = [x[1] for x in series]; d = [x[0] for x in series]
    ma = [None]*len(v)
    for i in range(3, len(v)): ma[i] = sum(v[i-3:i+1])/4
    rel = [None]*len(v)
    for i in range(3+52, len(v)):
        rel[i] = ma[i] / min(ma[i-52:i])
    return d, ma, rel

icsa = load('ICSA'); ccsa = load('CCSA'); usrec = load('USREC')
rec = {d: v for d, v in usrec}; rec_end = usrec[-1][0]
di, mai, reli = weekly_rel(icsa)
irel = {d: r for d, r in zip(di, reli)}
def hclaims_weeks(t_idx):  # ICSA rel>=1.30 in weeks t+1..t+26 (by ICSA index aligned on date)
    return None
idx_i = {d: i for i, d in enumerate(di)}

def eval_weekly(name, d, rel, cond, out):
    n = len(d); fire = [False]*n
    for i in range(n):
        try: fire[i] = cond(rel, i)
        except TypeError: fire[i] = False
    # episodes
    eps = []; quiet = 0
    for i in range(n):
        if fire[i]:
            if quiet >= 13: eps.append(i)
            quiet = 0
        else: quiet += 1
    def outcome_claims(date):
        # ICSA weeks strictly after date, up to 26 weeks
        j = idx_i.get(date)
        if j is None:  # CC dates are a week earlier than ICSA dates; align to first ICSA week > date
            j = next((k for k, x in enumerate(di) if x > date), None)
            if j is None: return None
            j -= 1
        if j + 26 >= len(di): return None
        win = di[j+1]; wend = di[j+26]
        if overlaps(win, wend): return None
        return any((reli[k] or 0) >= 1.30 for k in range(j+1, j+27))
    def outcome_rec(date):
        m0 = dt.date(date.year, date.month, 1)
        if rec.get(m0) == 1: return 'running'
        if addm(m0, 12) > rec_end: return None
        if overlaps(addm(m0,1), addm(m0,12)): return None
        return any(rec.get(addm(m0, k)) == 1 for k in range(1, 13))
    def elig(i): return rel[i] is not None and not inex(d[i])
    res = {}
    for oname, f in (('H-claims', outcome_claims), ('H-rec', outcome_rec)):
        eh = [(d[i], f(d[i])) for i in eps if elig(i)]
        eh = [(x, h) for x, h in eh if h is not None and h != 'running']
        base = [f(d[i]) for i in range(len(d)) if elig(i)]
        base = [h for h in base if h is not None and h != 'running']
        res[oname] = (sum(h for _, h in eh), len(eh), sum(base), len(base), eh)
    cur = [fire[i] for i in range(len(d)) if d[i] >= dt.date(2022,1,1)]
    res['cur'] = (sum(cur), len(cur))
    res['now'] = (d[-1], rel[-1], fire[-1])
    out[name] = res
    return res

out = {}
c110 = lambda r, i: r[i] >= 1.10
c110x2 = lambda r, i: r[i] >= 1.10 and r[i-1] >= 1.10
c115 = lambda r, i: r[i] >= 1.15
for nm, c in (('R13-a', c110), ('R13-b', c110x2), ('R13-c', c115)):
    eval_weekly(nm, di, reli, c, out)
dc, mac, relc = weekly_rel(ccsa)
for nm, c in (('R7-a', c110), ('R7-b', c110x2), ('R7-c', c115)):
    eval_weekly(nm, dc, relc, c, out)

print("== WEEKLY LETTERS ==")
for nm, r in out.items():
    hc = r['H-claims']; hr = r['H-rec']
    pc = hc[0]/hc[1] if hc[1] else float('nan'); bc = hc[2]/hc[3]
    pr = hr[0]/hr[1] if hr[1] else float('nan'); br = hr[2]/hr[3]
    print(f"{nm}: H-claims {hc[0]}/{hc[1]} = {pc:.3f} vs base {hc[2]}/{hc[3]} = {bc:.3f} (lift {pc/bc:.2f}) | H-rec {hr[0]}/{hr[1]} = {pr:.3f} vs base {hr[2]}/{hr[3]} = {br:.3f} | cur-regime fire {r['cur'][0]}/{r['cur'][1]} = {r['cur'][0]/r['cur'][1]:.3f} | now {r['now'][0]} rel {r['now'][1]:.4f} fire {r['now'][2]}")
    print("   episodes:", " ".join(f"{x}{'*' if h else ''}" for x, h in hc[4]))
# current trailing mins
i = len(di)-1; print("ICSA now MA", mai[i], "trailing52 min MA", min(mai[i-52:i]), "-> 1.10x =", 1.10*min(mai[i-52:i]))
i = len(dc)-1; print("CCSA now MA", mac[i], "trailing52 min MA", min(mac[i-52:i]), "-> 1.10x =", 1.10*min(mac[i-52:i]), "1.15x =", 1.15*min(mac[i-52:i]))

# ---- pickup 9
print("== JOLTS OPENINGS ==")
jol = load('JTSJOL'); hil = dict(load('JTSHIL')); tsl = dict(load('JTSTSL'))
md = [x[0] for x in jol]; mv = [x[1] for x in jol]
net = {m: hil[m] - tsl[m] for m in md if m in hil and m in tsl}
jend = md[-1]
def jo(thr):
    chg = [None]*len(md)
    for i in range(3, len(md)): chg[i] = mv[i]/mv[i-3] - 1
    fire = [c is not None and c <= thr for c in chg]
    eps = []; quiet = 3  # start-of-sample: first firing counts as episode if preceded by >=3 nonfiring (chg undefined months count as nonfiring)
    quiet = 0
    for i in range(len(md)):
        if fire[i]:
            if quiet >= 3: eps.append(i)
            quiet = 0
        else: quiet += 1
    def h_net(m):
        if addm(m, 6) > jend or overlaps(addm(m,1), addm(m,6)): return None
        ms = [addm(m, k) for k in range(1, 7)]
        return any(net[ms[k]] <= 0 and net[ms[k+1]] <= 0 for k in range(5))
    def h_cl(m):
        a, b = addm(m,1), addm(m,7)
        if b > di[-1] or overlaps(a, addm(m,6)): return None
        return any((irel.get(x) or 0) >= 1.30 for x in di if a <= x < b)
    elig = lambda i: chg[i] is not None and not inex(md[i])
    for nm, f in (('H-net', h_net), ('H-claims', h_cl)):
        e = [(md[i], f(md[i])) for i in eps if elig(i)]; e = [(x, h) for x, h in e if h is not None]
        b = [f(md[i]) for i in range(len(md)) if elig(i)]; b = [h for h in b if h is not None]
        pe = sum(h for _, h in e)/len(e) if e else float('nan'); pb = sum(b)/len(b)
        print(f"thr {thr}: {nm} {sum(h for _,h in e)}/{len(e)} = {pe:.3f} vs base {sum(b)}/{len(b)} = {pb:.3f} lift {pe/pb:.2f}")
        print("   episodes:", " ".join(f"{x.isoformat()[:7]}{'*' if h else ''}" for x, h in e))
    print(f"   all episode starts (incl. no-outcome): {[md[i].isoformat()[:7] for i in eps if elig(i)]}; latest chg {chg[-1]:.4f} fire {fire[-1]}")
jo(-0.05); jo(-0.075)
