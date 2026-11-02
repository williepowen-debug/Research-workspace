"""Study 4 data build: daily returns panel + French factors + ETF factor proxies + rates/credit.
Output: data/panel.csv (returns in decimals; dy10/dbaa in pp)."""
import os, json
import numpy as np, pandas as pd

H = os.path.dirname(os.path.abspath(__file__)); D = f"{H}/data"
TICK = ["KRE", "KBWB", "SPY", "RSP", "IWM", "IWN", "IWO", "QQQ", "XLF", "KBE", "IWD", "IWF", "MTUM", "XLK",
        "XLU", "IYR", "ITB", "XLI", "XLB", "IYT", "KIE"]
px = {}
for t in TICK:
    j = json.load(open(f"{D}/{t}.json"))["chart"]["result"][0]
    s = pd.Series(j["indicators"]["adjclose"][0]["adjclose"], index=pd.to_datetime(j["timestamp"], unit="s").normalize())
    px[t] = s[~s.index.duplicated(keep="last")]
P = pd.DataFrame(px).sort_index().loc[:"2026-10-30"]
R = P.pct_change()


def ff(fn, skip):
    x = pd.read_csv(f"{D}/{fn}", skiprows=skip, index_col=0)
    x = x[x.index.astype(str).str.strip().str.match(r"^\d{8}$")]
    x.index = pd.to_datetime(x.index.astype(str).str.strip(), format="%Y%m%d")
    return x.apply(pd.to_numeric, errors="coerce") / 100


f3 = ff("F-F_Research_Data_Factors_daily.csv", 3); f3.columns = [c.strip() for c in f3.columns]
mom = ff("F-F_Momentum_Factor_daily.csv", 13); mom.columns = ["MOM"]
F = f3.join(mom)
F.columns = ["MKT_ff", "SMB_ff", "HML_ff", "RF_ff", "MOM_ff"]

M3 = pd.read_csv(f"{D}/master_study3.csv", parse_dates=["date"], index_col=0)  # study-3 master: Treasury yields, BAA10Y
X = R.join(F, how="left").join(M3[["y10", "y2", "y3m", "baa10y"]], how="left")
X["dy10"] = X.y10.diff(); X["dy2"] = X.y2.diff(); X["dbaa"] = X.baa10y.diff()
X["RF"] = X.RF_ff.fillna(X.y3m.shift(1) / 100 / 252)
X["MKT_p"] = X.SPY - X.RF
X["SMB_p"] = X.IWM - X.SPY
X["HML_p"] = X.IWD - X.IWF
X["MOM_p"] = X.MTUM - X.SPY
X["CONC"] = X.SPY - X.RSP
X = X.iloc[1:]
X.index.name = "date"
X.to_csv(f"{D}/panel.csv", float_format="%.7f")
print(X.index.min(), X.index.max(), len(X)); print("French last:", F.dropna().index.max())
ov = X.loc["2013-05-01":"2026-09-30"]
for a, b in (("MKT_ff", "MKT_p"), ("SMB_ff", "SMB_p"), ("HML_ff", "HML_p"), ("MOM_ff", "MOM_p")):
    print(a, b, "corr", round(ov[a].corr(ov[b]), 3))
