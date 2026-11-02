"""KRE prospective evaluation: frozen resolver (draft for operator review; NOT scheduled).
Usage
  Validation on the reference window, using a local frozen CSV (no network):
      python resolver.py --validate --prices prices_adj.csv --ust-dir <dir with ust_YYYY.csv>
  Resolution (operator only, on or after 2027-02-03, after approval):
      python resolver.py --resolve
Definitions follow PREREGISTRATION.md section 2. Do not edit thresholds.
"""
import argparse, glob, io, json, hashlib, sys, time
import numpy as np, pandas as pd
TICKERS = ["KRE", "KBWB", "SPY", "IWM"]
BASE_CLOSE = "2026-10-30"
N = 63
# NYSE full closures inside the evaluation window (NYSE Group calendar). Early closes 11/27 and 12/24 ARE sessions.
NYSE_HOLIDAYS = ["2026-11-26", "2026-12-25", "2027-01-01", "2027-01-18", "2027-02-15"]
TH = dict(corr=0.863, vol=0.20, beta=0.80, brate_lo=-0.03, brate_hi=0.03)
NEAR = dict(corr=0.005, vol=0.002, beta=0.02, brate=0.005)  # flag only; does not change resolution
def expected_sessions(start="2026-11-02", n=N):
    d = pd.bdate_range(start, "2027-06-30")
    d = d[~d.isin(pd.to_datetime(NYSE_HOLIDAYS))]
    return d[:n]
def yahoo(t):
    import requests
    u = (f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?period1=1761609600"
         f"&period2={int(time.time()) + 86400}&interval=1d&events=div,splits")
    j = requests.get(u, headers={"User-Agent": "Mozilla/5.0"}, timeout=30).json()["chart"]["result"][0]
    ts = pd.to_datetime(j["timestamp"], unit="s").normalize()
    return pd.Series(j["indicators"]["adjclose"][0]["adjclose"], index=ts, name=t)
def treasury_10y(years):
    import requests
    out = []
    for y in years:
        u = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/"
             f"{y}/all?type=daily_treasury_yield_curve&field_tdr_date_value={y}&page&_format=csv")
        x = pd.read_csv(io.StringIO(requests.get(u, headers={"User-Agent": "Mozilla/5.0"}, timeout=30).text))
        x["Date"] = pd.to_datetime(x["Date"]); out.append(x.set_index("Date")["10 Yr"].astype(float))
    s = pd.concat(out).sort_index(); return s[~s.index.duplicated()]
def stats(px, y10, sessions, base):
    """px: adjusted closes (index=dates) incl. base date; sessions: the N evaluation dates."""
    idx = pd.DatetimeIndex([pd.Timestamp(base)]).append(sessions)
    p = px.reindex(idx)
    missing = {t: [str(d.date()) for d in sessions if pd.isna(p.loc[d, t])] for t in px.columns}
    p = p.ffill()          # a missing close -> next available return spans both days (spec 2.6)
    r = p.pct_change().iloc[1:]
    for t, m in missing.items():   # make the spanned day's return zero on the missing day itself
        for d in m: r.loc[pd.Timestamp(d), t] = np.nan
    y = y10.reindex(idx).ffill()   # bond holidays (e.g. Veterans Day) carry the prior yield
    dy = y.diff().iloc[1:]
    df = pd.concat([r, dy.rename("dy")], axis=1).dropna()
    k, b, s = df.KRE, df.KBWB, df.SPY
    corr = float(np.corrcoef(k, b)[0, 1])
    vol = float(k.std(ddof=1) * np.sqrt(252))
    beta = float(np.cov(k, s, ddof=1)[0, 1] / s.var(ddof=1))
    X = np.column_stack([np.ones(len(df)), s, df.dy])
    brate = float(np.linalg.lstsq(X, k, rcond=None)[0][2])
    cum = lambda t: float((1 + r[t].fillna(0)).prod() - 1)
    out = dict(n_returns_used=int(len(df)), missing=missing, corr=corr, vol=vol, beta=beta, brate=brate,
               KRE_ret=cum("KRE"), KBWB_ret=cum("KBWB"), IWM_ret=cum("IWM") if "IWM" in r else None)
    out["KRE_minus_KBWB"] = out["KRE_ret"] - out["KBWB_ret"]
    if out["IWM_ret"] is not None: out["KRE_minus_IWM"] = out["KRE_ret"] - out["IWM_ret"]
    out["C1"] = "persist" if corr <= TH["corr"] else ("calm_norm" if vol < TH["vol"] else "stress_norm")
    out["C2"] = "YES" if beta >= TH["beta"] else "NO"
    out["C3"] = "neg" if brate < TH["brate_lo"] else ("pos" if brate > TH["brate_hi"] else "zero")
    out["near_threshold"] = {
        "corr": abs(corr - TH["corr"]) < NEAR["corr"], "vol": abs(vol - TH["vol"]) < NEAR["vol"],
        "beta": abs(beta - TH["beta"]) < NEAR["beta"],
        "brate": min(abs(brate - TH["brate_lo"]), abs(brate - TH["brate_hi"])) < NEAR["brate"]}
    nmiss = max(len(v) for v in missing.values())
    out["status"] = "VOID_DATA" if nmiss > 3 else "RESOLVED"
    return out
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--validate", action="store_true"); ap.add_argument("--resolve", action="store_true")
    ap.add_argument("--prices"); ap.add_argument("--ust-dir")
    a = ap.parse_args()
    if a.validate:   # reference window 8/4-10/30/2026 from frozen local files; expected 0.7193/0.1561/0.3275/-0.062
        px = pd.read_csv(a.prices, index_col=0, parse_dates=True)[TICKERS].loc[:"2026-10-30"]
        px = px[px.SPY.notna()]
        u = [pd.read_csv(f) for f in sorted(glob.glob(a.ust_dir + "/ust_*.csv"))]
        for x in u: x["Date"] = pd.to_datetime(x["Date"])
        y10 = pd.concat([x.set_index("Date")["10 Yr"] for x in u]).astype(float).sort_index()
        y10 = y10[~y10.index.duplicated()]
        sess = px.loc["2026-08-04":"2026-10-30"].index
        print(json.dumps(stats(px, y10, sess, "2026-08-03"), indent=1)); return
    if a.resolve:
        sess = expected_sessions()
        if pd.Timestamp.today().normalize() <= sess[-1]:
            sys.exit(f"Not resolvable before session 63 ({sess[-1].date()}) has closed.")
        px = pd.concat([yahoo(t) for t in TICKERS], axis=1)
        traded = px.index[(px.index > BASE_CLOSE)]
        # unscheduled closures: the window is the first 63 ACTUAL sessions (spec 2.1)
        actual = traded[:N]
        if not actual.equals(sess): print("NOTE: actual sessions differ from scheduled calendar; using actual.")
        y10 = treasury_10y([2026, 2027])
        res = stats(px, y10, actual, BASE_CLOSE)
        res["window"] = [str(actual[0].date()), str(actual[-1].date())]
        res["data_sha256"] = hashlib.sha256(px.to_csv().encode()).hexdigest()
        res["retrieved_utc"] = pd.Timestamp.utcnow().isoformat()
        print(json.dumps(res, indent=1))
if __name__ == "__main__":
    main()
