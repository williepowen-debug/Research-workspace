"""usage: python isda_bench.py FRED_JSON_DIR  (FRED_JSON_DIR holds fred_<SERIES>.json = `fetch.py fred <S> --json --periods 220`;
       needs QuantLib (pip install QuantLib, 1.43 used) and AGENTS/LIQUID/scripts/crwv_cds_grade.py on the path)
ISDA Standard Model benchmark of CoreWeave upfront->conventional spread (DOCKET L510).
Engine: QuantLib IsdaCdsEngine (NumericalFix Taylor, AccrualBias HalfDayBias per ISDA std model v1.8.2 conventions),
flat hazard (conventional-spread convention), R=40%, CDS2015 schedule, ACT/360, step-in T+1, cash settle T+3 bd,
accrual rebate on. Discount curve: USD Treasury CMT par yields (FRED H.15) with SOFR O/N at the front, as a proxy for
the ISDA-standard USD SOFR swap curve (official Markit/S&P curve file unreachable 2026-09-28: rfr.ihsmarkit.com HTTP 500).
"""
import json, sys, datetime as dt
import QuantLib as ql
sys.path.insert(0, '/home/willi/Research-workspace/AGENTS/LIQUID/scripts')
import crwv_cds_grade as g
S = sys.argv[1]
def fred(sid):
    d = json.load(open(f"{S}/fred_{sid}.json"))
    return {o['date']: float(o['value']) for o in d['observations']}
F = {k: fred(k) for k in ['SOFR','DGS1MO','DGS3MO','DGS6MO','DGS1','DGS2','DGS3','DGS5','DGS7','DGS10']}
cal = ql.WeekendsOnly()
def curve(today, date_iso, shift=0.0):
    tenors = [('SOFR',ql.Period(1,ql.Days)),('DGS1MO',ql.Period(1,ql.Months)),('DGS3MO',ql.Period(3,ql.Months)),
              ('DGS6MO',ql.Period(6,ql.Months)),('DGS1',ql.Period(1,ql.Years)),('DGS2',ql.Period(2,ql.Years)),
              ('DGS3',ql.Period(3,ql.Years)),('DGS5',ql.Period(5,ql.Years)),('DGS7',ql.Period(7,ql.Years)),('DGS10',ql.Period(10,ql.Years))]
    dates=[today]; rates=[F['SOFR'][date_iso]/100+shift]
    for k,p in tenors:
        dates.append(today+p); rates.append(F[k][date_iso]/100+shift)
    # treat CMT par yields as continuously-compounded zero rates (proxy; bracketed by the +-50bp shift)
    import math
    dc=ql.Actual365Fixed()
    dfs=[1.0]+[math.exp(-r*dc.yearFraction(today,d)) for r,d in zip(rates[1:],dates[1:])]
    c = ql.DiscountCurve(dates, dfs, dc)   # log-linear discount = piecewise flat forward (ISDA interpolation)
    c.enableExtrapolation()
    return ql.YieldTermStructureHandle(c)
def flat_curve(today, r):
    return ql.YieldTermStructureHandle(ql.FlatForward(today, r, ql.Actual365Fixed(), ql.Continuous))
def qd(d): return ql.Date(d.day, d.month, d.year)
def price(trade, mat, h, disc, c=0.05, R=0.4):
    today = qd(trade); ql.Settings.instance().evaluationDate = today
    sched = ql.Schedule(today, qd(mat), ql.Period(ql.Quarterly), cal, ql.Following, ql.Unadjusted, ql.DateGeneration.CDS2015, False)
    cds = ql.CreditDefaultSwap(ql.Protection.Buyer, 1.0, 0.0, c, sched, ql.Following, ql.Actual360(), True, True,
                               today+1, cal.advance(today,3,ql.Days), ql.FaceValueClaim(), ql.Actual360(True), True, today, 3)
    hz = ql.DefaultProbabilityTermStructureHandle(ql.FlatHazardRate(today, ql.QuoteHandle(ql.SimpleQuote(h)), ql.Actual365Fixed()))
    cds.setPricingEngine(ql.IsdaCdsEngine(hz, R, disc, False, ql.IsdaCdsEngine.Taylor, ql.IsdaCdsEngine.HalfDayBias, ql.IsdaCdsEngine.Piecewise))
    return cds
def par_and_upfront(trade, mat, h, disc, c=0.05):
    cds = price(trade, mat, h, disc, c)
    return cds.fairSpread(), cds.fairUpfront(), abs(cds.accrualRebateNPV())
def solve(trade, mat, U_clean, disc, c=0.05):
    lo, hi = 1e-5, 2.0
    for _ in range(100):
        h = (lo+hi)/2
        _, up, _ = par_and_upfront(trade, mat, h, disc, c)
        if up > U_clean: hi = h
        else: lo = h
    par, up, acc = par_and_upfront(trade, mat, h, disc, c)
    # conventional spread = par spread of a flat-hazard curve; re-derive via a helper-free par on same h
    return par, acc
D = dt.date
Q = [("12/17/25 Dec-30 (Dec peak)", D(2025,12,17), D(2030,12,20), 0.1129, '2025-12-17'),
     ("7/06 Jun-31 CORR 750k",      D(2026,7,6),   D(2031,6,20),  0.0369, '2026-07-06'),
     ("7/06 Jun-31 2M",             D(2026,7,6),   D(2031,6,20),  0.0287, '2026-07-06'),
     ("7/07 Jun-31 3M",             D(2026,7,7),   D(2031,6,20),  0.0366, '2026-07-07'),
     ("9/23 Q2 Dec-31 3M",          D(2026,9,23),  D(2031,12,20), 0.1146, '2026-09-23'),
     ("9/23 Q3 Dec-31 3M (low)",    D(2026,9,23),  D(2031,12,20), 0.1072, '2026-09-23'),
     ("9/23 Q4 Dec-31 3M (high)",   D(2026,9,23),  D(2031,12,20), 0.1208, '2026-09-23'),
     ("9/24 Q1 Dec-31 3M",          D(2026,9,24),  D(2031,12,20), 0.1182, '2026-09-24')]
print(f"{'print':28s} {'U_obs':>6s} | {'LIQ clean':>9s} {'LIQ cash':>8s} | {'ISDA clean':>10s} {'ISDA cash':>9s} | gap clean  gap cash | cash: -50bp +50bp | flat4% | acc(pt) ISDA/LIQ")
for name, tr, mat, U, iso in Q:
    today = qd(tr); ql.Settings.instance().evaluationDate = today
    liq_c = g.conv_spread(U, 0.05, tr, mat)*1e4; liq_d = g.conv_spread(U, 0.05, tr, mat, dirty=True)*1e4
    disc = curve(today, iso)
    _, _, acc = par_and_upfront(tr, mat, 0.08, disc)
    af_liq = 0.05*((tr+dt.timedelta(1))-g.imm_prev(tr)).days/360
    ic, _ = solve(tr, mat, U, disc)                 # reported value read as CLEAN upfront
    id_, _ = solve(tr, mat, U+acc, disc)             # reported value read as CASH net of accrued (clean = U + accrued)
    dn, _ = solve(tr, mat, U+acc, curve(today, iso, -0.005))
    up, _ = solve(tr, mat, U+acc, curve(today, iso, +0.005))
    fl, _ = solve(tr, mat, U+acc, flat_curve(today, 0.04))
    print(f"{name:28s} {U*100:6.2f} | {liq_c:9.0f} {liq_d:8.0f} | {ic*1e4:10.1f} {id_*1e4:9.1f} | {ic*1e4-liq_c:+8.1f} {id_*1e4-liq_d:+8.1f} | {dn*1e4-id_*1e4:+6.1f} {up*1e4-id_*1e4:+6.1f} | {fl*1e4:6.1f} | {acc*100:.3f}/{af_liq*100:.3f}")
