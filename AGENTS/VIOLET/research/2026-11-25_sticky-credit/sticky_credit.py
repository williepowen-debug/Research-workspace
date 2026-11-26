"""Sticky credit after a VIX fade: does it predict a second vol leg?

Question (Will, 2026-11-25 19:58 ET, option 1): VIX gave back most of its
spike (35.89 [11/20] -> 26.36 [11/24]) while credit held near its wide
(HY 376 -> 372; Baa-10Y 1.61 -> 1.61). In past spikes, when VIX faded fast
but credit did not, what did VIX do over the next 10-20 sessions?

Data (saved in data/, pulled 2026-11-25 ~20:00 ET):
  vix.csv           Cboe VIX_History.csv, closes 1990-01-02 .. 11/24/2026
  BAA10Y.csv        FRED Moody's Baa yield minus 10Y Treasury, 1986 .. 2026-11-24
                    (investment-grade-ish proxy: the only free daily credit
                    spread with 1990s history; FRED's ICE HY series is now
                    truncated to 3 years)
  BAMLH0A0HYM2.csv  FRED ICE BofA HY OAS, 2023-11-27 .. 2026-11-24 (cross-check)

Episode rules (fixed before looking at outcomes):
  Peak P: VIX close >= 25, the max close within +/-10 sessions, and
          P >= 1.5 x L where L = min close over the 20 sessions before P.
  Fade day F: first session 1..5 after P where VIX retraced >= 50% of (P - L).
  Credit at F: widening W = max spread over [L_date, F] - spread at L_date;
          retrace r = (max - spread_F) / W.
          STICKY: W >= 5bp and r <= 25%.  FADED: W < 5bp or r >= 50%.
          (between: MIXED, reported but not in the main split)
  Episodes at least 30 sessions apart (first qualifying peak wins).
Outcomes from F (VIX closes): over the next 20 sessions
  RELEG90: any close >= 0.9 x P (a second leg nearly to the old peak)
  NEWHIGH: any close > P
  FULLFADE: any close <= L + 0.25 x (P - L)
  V10, V20: VIX at F+10 / F+20 as a fraction of P.
"""
import csv, sys
from datetime import datetime
from pathlib import Path

D = Path(__file__).parent / "data"


def load_vix():
    out = []
    with open(D / "vix.csv") as f:
        for row in csv.DictReader(f):
            out.append((datetime.strptime(row["DATE"], "%m/%d/%Y").date(), float(row["CLOSE"])))
    return out


def load_fred(name):
    s = {}
    with open(D / f"{name}.csv") as f:
        r = csv.reader(f)
        next(r)
        for d, v in r:
            if v not in ("", "."):
                s[datetime.strptime(d, "%Y-%m-%d").date()] = float(v) * 100  # bp
    return s


def spread_on(s, keys, d):
    # last published value on or before d (forward fill over holidays)
    lo, hi = 0, len(keys) - 1
    if d < keys[0]:
        return None
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if keys[mid] <= d:
            lo = mid
        else:
            hi = mid - 1
    return s[keys[lo]]


def episodes(vix, s, start=None):
    keys = sorted(s)
    dates = [d for d, _ in vix]
    closes = [c for _, c in vix]
    eps, last_peak = [], -999
    for i in range(20, len(vix) - 1):
        P = closes[i]
        if start and dates[i] < start:
            continue
        if P < 25 or i - last_peak < 30:
            continue
        if P < max(closes[max(0, i - 10): i + 11]):
            continue
        Lwin = closes[i - 20: i]
        L = min(Lwin)
        if P < 1.5 * L:
            continue
        li = i - 20 + Lwin.index(L)
        f = None
        for k in range(1, 6):
            if i + k < len(vix) and closes[i + k] <= P - 0.5 * (P - L):
                f = i + k
                break
        last_peak = i
        if f is None:
            continue
        sL = spread_on(s, keys, dates[li])
        span = [spread_on(s, keys, dates[j]) for j in range(li, f + 1)]
        span = [x for x in span if x is not None]
        if sL is None or not span:
            continue
        smax, sF = max(span), spread_on(s, keys, dates[f])
        W = smax - sL
        r = (smax - sF) / W if W > 0 else None
        if W >= 5 and r is not None and r <= 0.25:
            cls = "STICKY"
        elif W < 5 or (r is not None and r >= 0.5):
            cls = "FADED"
        else:
            cls = "MIXED"
        fwd = closes[f + 1: f + 21]
        full = len(fwd) == 20
        eps.append(dict(
            L_date=dates[li], L=L, P_date=dates[i], P=P, F_date=dates[f], VF=closes[f],
            sL=sL, smax=smax, sF=sF, W=W, r=r, cls=cls, full=full,
            releg90=any(c >= 0.9 * P for c in fwd), newhigh=any(c > P for c in fwd),
            fullfade=any(c <= L + 0.25 * (P - L) for c in fwd),
            v10=closes[f + 10] / P if f + 10 < len(closes) else None,
            v20=closes[f + 20] / P if f + 20 < len(closes) else None,
            maxfwd=max(fwd) / P if fwd else None,
        ))
    return eps


def report(title, eps):
    print(f"\n=== {title} ===")
    print(f"{'peak':10} {'L':>6} {'P':>6} {'fade':10} {'VF':>6} {'W bp':>6} {'retr':>5} {'class':7} "
          f"{'max20/P':>7} {'V10/P':>6} {'V20/P':>6} releg90 newhigh fullfade")
    for e in eps:
        rr = f"{e['r']*100:4.0f}%" if e["r"] is not None else "  n/a"
        v10 = f"{e['v10']:.2f}" if e["v10"] else "  -"
        v20 = f"{e['v20']:.2f}" if e["v20"] else "  -"
        mf = f"{e['maxfwd']:.2f}" if e["maxfwd"] else "  -"
        print(f"{e['P_date']!s:10} {e['L']:6.2f} {e['P']:6.2f} {e['F_date']!s:10} {e['VF']:6.2f} "
              f"{e['W']:6.0f} {rr:>5} {e['cls']:7} {mf:>7} {v10:>6} {v20:>6} "
              f"{'Y' if e['releg90'] else '.':>7} {'Y' if e['newhigh'] else '.':>7} "
              f"{'Y' if e['fullfade'] else '.':>8}{'' if e['full'] else '  (partial window)'}")
    for cls in ("STICKY", "MIXED", "FADED"):
        g = [e for e in eps if e["cls"] == cls and e["full"]]
        if not g:
            continue
        n = len(g)
        med = lambda xs: sorted(xs)[len(xs) // 2]
        print(f"  {cls:7} n={n:2}  releg90 {sum(e['releg90'] for e in g)}/{n}  newhigh "
              f"{sum(e['newhigh'] for e in g)}/{n}  fullfade {sum(e['fullfade'] for e in g)}/{n}  "
              f"median V20/P {med([e['v20'] for e in g]):.2f}  median max20/P {med([e['maxfwd'] for e in g]):.2f}")


if __name__ == "__main__":
    vix = load_vix()
    baa = load_fred("BAA10Y")
    hy = load_fred("BAMLH0A0HYM2")
    report("Baa-10Y, 1990 to 11/24/2026", episodes(vix, baa))
    report("ICE HY OAS, 2023-11-27 to 11/24/2026 (cross-check)", episodes(vix, hy, start=datetime(2023, 12, 1).date()))
    # live case, by hand from the same files
    print("\nLive case: L 19.30 [11/12], P 35.89 [11/20], F 26.62 [11/23] (56% retraced).")
    for nm, s in (("Baa-10Y", baa), ("HY OAS", hy)):
        k = sorted(s)
        sl = spread_on(s, k, datetime(2026, 11, 12).date())
        mx = max(v for d, v in s.items() if datetime(2026, 11, 12).date() <= d <= datetime(2026, 11, 24).date())
        s23, s24 = spread_on(s, k, datetime(2026, 11, 23).date()), spread_on(s, k, datetime(2026, 11, 24).date())
        print(f"  {nm}: L {sl:.0f}, max {mx:.0f}, W {mx-sl:.0f}bp, at F(11/23) retrace {(mx-s23)/(mx-sl)*100:.0f}%, "
              f"11/24 retrace {(mx-s24)/(mx-sl)*100:.0f}%")
