"""REBUILT stress test of the KRE–KBWB decoupling (data through the 10/30/2026 close).
Reconstructs the analyses of the original session-13 stress test (whose files were not transferable) from its recorded method.
Every headline number is compared with the value recorded from the original run -> out/comparison_with_original.csv.
Run: bash scripts/fetch.sh && python3 scripts/stress_test.py
"""
import os, json, glob
import numpy as np, pandas as pd
from scipy import stats
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); D = f"{ROOT}/data"; OUT = f"{ROOT}/out"
os.makedirs(OUT, exist_ok=True)
END = pd.Timestamp("2026-10-30"); W = 63; HSTART = "2012-02-01"
rng = np.random.default_rng(20261102)
CMP = []  # (item, rebuilt, original)


def cmp(item, rebuilt, original, note=""):
    CMP.append(dict(item=item, rebuilt=rebuilt, original_session13=original, note=note))


# ------------------------------------------------------------------ data
def load(t):
    j = json.load(open(f"{D}/px/{t}.json"))["chart"]["result"][0]
    s = pd.Series(j["indicators"]["adjclose"][0]["adjclose"], index=pd.to_datetime(j["timestamp"], unit="s").normalize())
    return s[~s.index.duplicated(keep="last")]


P = pd.DataFrame({os.path.basename(f)[:-5]: load(os.path.basename(f)[:-5]) for f in glob.glob(f"{D}/px/*.json")}).sort_index().loc[:END]
P = P[P.index >= "2006-06-22"]
R = P.pct_change()
hold = pd.read_excel(f"{D}/kre_holdings.xlsx", header=4); hold = hold[hold.Ticker.notna() & (hold.Ticker != "-")]
MEM = list(hold.Ticker.astype(str)); WTS = hold.set_index("Ticker").Weight.astype(float); WTS = WTS / WTS.sum()
OVL = ["TFC", "MTB", "HBAN", "CFG", "RF", "EWBC", "PNFP", "FHN", "ZION", "WAL"]
MEGA = ["JPM", "BAC", "WFC", "C", "GS", "MS", "USB", "COF", "PNC", "BNY", "NTRS", "STT", "KEY", "FITB"]  # KBWB names not in KRE ("large banks")
ust = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(f"{D}/ust/ust_*.csv"))])
ust["Date"] = pd.to_datetime(ust["Date"], format="%m/%d/%Y"); ust = ust.drop_duplicates("Date").set_index("Date").sort_index()
R["dy10"] = ust["10 Yr"].reindex(P.index).ffill().diff()
R["OVL10"] = R[OVL].mean(axis=1)
R["KBWB14"] = R[MEGA].mean(axis=1)
R["REST"] = R[[m for m in MEM if m not in OVL]].mean(axis=1)
R["BASKET"] = (R[MEM] * WTS.reindex(MEM).values).sum(axis=1, min_count=100) / WTS.reindex(MEM)[R[MEM].notna().iloc[-1].values].sum()
nav = pd.read_excel(f"{D}/kre_navhist.xlsx", header=3)
nav["Date"] = pd.to_datetime(nav["Date"], format="%d-%b-%Y", errors="coerce"); nav = nav.dropna(subset=["Date"]).set_index("Date").sort_index()
R["KRE_NAV"] = pd.to_numeric(nav["NAV"], errors="coerce").reindex(P.index).pct_change()
R = R.iloc[1:]
win = R.loc[:END].iloc[-W:]  # 63 simple returns, 8/4 -> 10/30 (base close 8/3)
assert win.index[0] == pd.Timestamp("2026-08-04"), win.index[0]
P.loc[:, ["KRE", "KBWB", "SPY", "IWM", "KBE", "IAT", "QABA", "RSP"]].to_csv(f"{D}/etf_adjclose.csv", float_format="%.6f")

# ------------------------------------------------------------------ A. replication + gap concentration
A = {b: win.KRE.corr(win[b]) for b in ["KBWB", "SPY", "IWM", "KBE", "IAT", "QABA", "RSP"]}
for b, o in zip(A, [0.7193, 0.2193, 0.5010, 0.9880, 0.8976, 0.9865, 0.5505]):
    cmp(f"63d corr KRE vs {b}", round(A[b], 4), o)
gap = win.KRE - win.KBWB; sq = gap ** 2; share = (sq / sq.sum()).sort_values(ascending=False)
G = pd.DataFrame({"gap_pct": gap * 100, "share_of_sq_gap": sq / sq.sum()}).sort_values("share_of_sq_gap", ascending=False)
G.to_csv(f"{OUT}/A_gap_days.csv", float_format="%.4f")
cmp("top-5 share of squared gap", round(share.iloc[:5].sum(), 3), 0.438); cmp("top-10 share", round(share.iloc[:10].sum(), 3), 0.622)
cmp("largest gap day (share)", f"{share.index[0].date()} ({share.iloc[0]:.3f})", "2026-10-22 (0.158)")
cmp("2nd gap day (share)", f"{share.index[1].date()} ({share.iloc[1]:.3f})", "2026-09-14 (0.132)")
pd.DataFrame({"benchmark": list(A), "corr_63d": list(A.values())}).to_csv(f"{OUT}/A_replication.csv", index=False, float_format="%.4f")

# ------------------------------------------------------------------ B. R² reconciliation
def r2(y, X):
    Xc = np.column_stack([np.ones(len(X)), X]); b = np.linalg.lstsq(Xc, y, rcond=None)[0]; e = y - Xc @ b
    return 1 - e.var() / y.var(), 1 - e.var(ddof=0) / y.var(ddof=1)
rows = []
for b in ["KBWB", "IWM", "SPY"]:
    good, bug = r2(win.KRE.values, win[[b]].values)
    rows.append(dict(spec=f"KRE ~ {b} (63 returns)", r2=good, r2_ddof_mismatch=bug))
for b in ["IWM", "SPY"]:
    good, _ = r2(win.KRE.values, win[[b, "dy10"]].values); rows.append(dict(spec=f"KRE ~ {b} + Δ10y (63 returns)", r2=good))
w64 = R.loc[:END].iloc[-64:]
for b in ["KBWB", "IWM", "SPY"]:
    good, _ = r2(w64.KRE.values, w64[[b]].values); rows.append(dict(spec=f"KRE ~ {b} (64 returns, base 7/31)", r2=good))
RB = pd.DataFrame(rows); RB.to_csv(f"{OUT}/B_r2_reconciliation.csv", index=False, float_format="%.4f")
cmp("univariate R² KBWB / IWM / SPY", " / ".join(f"{x:.3f}" for x in RB.r2[:3]), "0.517 / 0.251 / 0.048")
cmp("ddof-mismatch R² KBWB / IWM / SPY", " / ".join(f"{x:.4f}" for x in RB.r2_ddof_mismatch[:3]), "0.5251 / 0.263 / 0.063")
cmp("KRE~IWM+Δ10y R²", round(RB.r2[3], 4), 0.2824); cmp("KRE~SPY+Δ10y R²", round(RB.r2[4], 3), 0.153)

# ------------------------------------------------------------------ C. trims applied identically to all history
H_all = R.loc[:END]
def trimmed_corr(x, y, k=0, drop_rank=None):
    g = np.abs(x - y); order = np.argsort(-g)
    keep = np.ones(len(x), bool)
    if drop_rank is not None: keep[order[drop_rank]] = False
    elif k: keep[order[:k]] = False
    return np.corrcoef(x[keep], y[keep])[0, 1]
variants = {"none": dict(k=0), "drop largest (10/22)": dict(k=1), "drop 2nd only (9/14)": dict(drop_rank=1), "drop top-2": dict(k=2), "drop top-5": dict(k=5), "drop top-10": dict(k=10)}
pairs = [("KRE", "KBWB"), ("KBE", "KBWB"), ("QABA", "KBWB"), ("IAT", "KBWB"), ("KRE", "SPY"), ("KRE", "IWM"), ("KRE", "IAT"), ("KBWB", "SPY")]
TR = []
for a, b in pairs:
    H = H_all[[a, b]].dropna(); X, Y = H[a].values, H[b].values
    ends = np.arange(W - 1, len(H)); ends = ends[H.index[ends] >= pd.Timestamp(HSTART)]; k_pos = len(H) - 1
    nonover = ends[(k_pos - ends) % W == 0]
    for vn, kw in variants.items():
        series = np.array([trimmed_corr(X[e - W + 1:e + 1], Y[e - W + 1:e + 1], **kw) for e in ends])
        cur = series[-1]; pct = (series <= cur).mean()
        no = series[np.isin(ends, nonover)]; rank = int((no <= cur).sum())
        TR.append(dict(pair=f"{a}–{b}", variant=vn, current=cur, pct_all_windows=pct, n_windows=len(series), rank_nonoverlap=rank, n_nonoverlap=len(no)))
TR = pd.DataFrame(TR); TR.to_csv(f"{OUT}/C_trims.csv", index=False, float_format="%.4f")
kk = TR[TR.pair == "KRE–KBWB"].set_index("variant")
orig = {"none": (0.719, "1.5%", "1/59"), "drop largest (10/22)": (0.753, "1.3%", ""), "drop 2nd only (9/14)": (0.749, "1.7%", ""), "drop top-2": (0.785, "1.6%", ""),
        "drop top-5": (0.821, "1.3%", ""), "drop top-10": (0.854, "1.1%", "2/59")}
for v, (c, p, r) in orig.items():
    cmp(f"trim {v}: corr, pct, rank", f"{kk.loc[v, 'current']:.3f}, {kk.loc[v, 'pct_all_windows']*100:.1f}%, {kk.loc[v, 'rank_nonoverlap']}/{kk.loc[v, 'n_nonoverlap']}", f"{c}, {p}" + (f", {r}" if r else ""))
cmp("windows since 2012-02", int(kk.loc["none", "n_windows"]), 3708)
cmp("KBWB–SPY corr pct", f"{TR[(TR.pair=='KBWB–SPY')&(TR.variant=='none')].pct_all_windows.iloc[0]*100:.0f}%", "14%")
x, y = win.KRE.values, win.KBWB.values; base = np.corrcoef(x, y)[0, 1]
loo = pd.Series([np.corrcoef(np.delete(x, i), np.delete(y, i))[0, 1] - base for i in range(W)], index=win.index).sort_values(ascending=False)
loo.to_frame("corr_change_if_dropped").to_csv(f"{OUT}/C_leave_one_out.csv", float_format="%.4f")
cmp("LOO 10/22, 9/14", f"{loo[pd.Timestamp('2026-10-22')]:+.3f}, {loo[pd.Timestamp('2026-09-14')]:+.3f}", "+0.034, +0.029")
cmp("days that raise corr when dropped", int((loo > 0).sum()), 30)
seq = [trimmed_corr(x, y, k=k) for k in range(11)]
pd.DataFrame({"k_dropped": range(11), "corr": seq}).to_csv(f"{OUT}/C_sequential_trim.csv", index=False, float_format="%.4f")
cmp("sequential trim k=0..5,10", ", ".join(f"{seq[k]:.3f}" for k in (0, 1, 2, 3, 4, 5, 10)), "0.719, .753, .785, .797, .809, .821, .854")

# ------------------------------------------------------------------ D. path / persistence
H2 = R.loc[:END]
roll = {w: H2.KRE.rolling(w).corr(H2.KBWB).dropna().loc[HSTART:] for w in (21, 42, 63, 126)}
PW = []
for w, s in roll.items():
    no = s.iloc[::-1].iloc[::w]
    PW.append(dict(window=w, current=s.iloc[-1], pct=(s <= s.iloc[-1]).mean(), median=s.median(), rank_nonoverlap=int((no <= s.iloc[-1]).sum()), n_nonoverlap=len(no)))
PW = pd.DataFrame(PW); PW.to_csv(f"{OUT}/D_window_lengths.csv", index=False, float_format="%.4f")
c126 = PW[PW.window == 126].iloc[0]
cmp("126d corr, rank among non-overlap", f"{c126.current:.3f}, {int(c126.rank_nonoverlap)}/{int(c126.n_nonoverlap)}", "0.730, 1/29 (lowest)")
r21 = roll[21]; hist21 = r21; p10_21 = hist21.quantile(.1); med21 = hist21.median()  # original convention: all windows since 2012-02 (incl. 2025-26)
p10_21_pre = r21.loc[:"2024-12-31"].quantile(.1)
blk = r21.iloc[::-1].iloc[::21].iloc[::-1]
b25 = blk.loc["2025-05-01":]
BL = pd.DataFrame({"block_end": b25.index.date, "corr21": b25.values, "below_hist_median": b25.values < med21, "below_hist_p10": b25.values < p10_21})
BL["below_pre2025_p10"] = b25.values < p10_21_pre
BL.to_csv(f"{OUT}/D_blocks21_since_2025-05.csv", index=False, float_format="%.4f")
cmp("21d blocks since 5/2025: below median / below p10 / n", f"{BL.below_hist_median.sum()} / {BL.below_hist_p10.sum()} / {len(BL)} (p10={p10_21:.3f})", "16 / 9 / 18 (p10=0.836)")
hb = blk.loc[:"2024-12-31"] < p10_21; max12 = int(hb.rolling(12).sum().max())
cmp("last 12 blocks below p10 vs hist max in any 12", f"{int(BL.below_hist_p10.iloc[-12:].sum())} vs {max12}", "7 vs 3")
jj = blk.loc["2026-06-01":"2026-08-03"]
cmp("Jun–Jul 2026 21d blocks", ", ".join(f"{d.date()}: {v:.3f}" for d, v in jj.items()), "0.677, 0.640")
r63 = roll[63]; p10_63 = r63.quantile(.1)
cmp("63d 10th pct threshold", round(p10_63, 3), 0.863)
below = (r63 < p10_63)
eps = []; start = None; last = None
for d, v in below.items():
    if v:
        if start is None or (r63.index.get_loc(d) - r63.index.get_loc(last)) > W: 
            if start is not None: eps.append((start, last))
            start = d
        last = d
eps.append((start, last))
EP = pd.DataFrame([dict(start=a.date(), end=b.date(), days_below=int(below.loc[a:b].sum()), span=r63.index.get_loc(b) - r63.index.get_loc(a) + 1, min_corr=r63.loc[a:b].min()) for a, b in eps])
EP.to_csv(f"{OUT}/D_episodes_below_p10.csv", index=False, float_format="%.3f")
recent = EP[pd.to_datetime(EP.start) >= "2025-01-01"]
cmp("episodes <p10 since 2025", "; ".join(f"{r.start}→{r.end} ({r.days_below}/{r.span})" for r in recent.itertuples()), "2025-09-09→2026-02-26 (85 days); 2026-06-10→now (96/100)")
pre = r63.loc[:"2024-12-31"]; idx = pre.index
nxt = [r63.iloc[r63.index.get_loc(d) + W] for d in idx[pre < p10_63] if r63.index.get_loc(d) + W < len(r63) and r63.index[r63.index.get_loc(d) + W] <= pd.Timestamp("2024-12-31")]
nxt = np.array(nxt)
cmp("pre-2025: next 63d window back above p10 / median", f"{(nxt >= p10_63).mean()*100:.1f}% / {np.median(nxt):.3f}", "99.5% / 0.911")
cmp("share of 2026 windows < p10", f"{(r63.loc['2026'] < p10_63).mean()*100:.0f}%", "64%")

# ------------------------------------------------------------------ E. mechanics: tracking error and vol
vk = (H2.KRE.rolling(W).std() * np.sqrt(252)).loc[HSTART:]; vb = (H2.KBWB.rolling(W).std() * np.sqrt(252)).loc[HSTART:]; te = ((H2.KRE - H2.KBWB).rolling(W).std() * np.sqrt(252)).loc[HSTART:]
cmp("TE(KRE−KBWB) now, pct, median", f"{te.iloc[-1]*100:.1f}%, {(te.dropna() <= te.iloc[-1]).mean()*100:.0f} pct, {te.median()*100:.1f}%", "12.0%, 82 pct, 8.9%")
cmp("KRE 63d vol pct", f"{vk.iloc[-1]*100:.1f}%, {(vk.dropna() <= vk.iloc[-1]).mean()*100:.0f} pct", "15.6%, 9 pct")
impl = lambda a, b, t: (a ** 2 + b ** 2 - t ** 2) / (2 * a * b)
cmp("implied corr: current vols + median TE", round(impl(vk.iloc[-1], vb.iloc[-1], te.median()), 3), 0.849)
cmp("implied corr: median vols + current TE", round(impl(vk.median(), vb.median(), te.iloc[-1]), 3), 0.859)
df = pd.DataFrame({"c": r63, "lv": np.log(vk)}).dropna()
pre = df.loc[:"2025-12-31"]; lowv = pre[pre.lv <= np.log(vk.iloc[-1]) + 0.1]
no = df.iloc[::-1].iloc[::W].iloc[::-1]; nopre = no.loc[:"2025-12-31"]
fz = np.arctanh(nopre.c)  # Fisher z, so the residual scale is comparable across correlation levels
sl, ic, *_ = stats.linregress(nopre.lv, fz); resid = fz - (ic + sl * nopre.lv)
z = (np.arctanh(df.c.iloc[-1]) - (ic + sl * df.lv.iloc[-1])) / resid.std(ddof=2)
cmp("min pre-2026 corr in windows with KRE vol ≤ current+10% (log)", round(lowv.c.min(), 3), 0.803, "low-vol conditional")
cmp("vol-adjusted residual z (non-overlap regression of Fisher-z corr on log KRE vol, pre-2026)", round(z, 2), -2.2, "exact original spec not recorded; raw-corr scale gives ≈ −6, Fisher-z −2.6 to −2.9")

# ------------------------------------------------------------------ F. partial correlations, rank corr, lower frequency
def pcorr(df_, a, b, ctrl):
    Xc = np.column_stack([np.ones(len(df_))] + [df_[c].values for c in ctrl])
    ea = df_[a].values - Xc @ np.linalg.lstsq(Xc, df_[a].values, rcond=None)[0]
    eb = df_[b].values - Xc @ np.linalg.lstsq(Xc, df_[b].values, rcond=None)[0]
    return np.corrcoef(ea, eb)[0, 1]
H3 = R.loc[:END, ["KRE", "KBWB", "SPY", "dy10"]].dropna()
ends3 = [e for e in range(W, len(H3) + 1) if H3.index[e - 1] >= pd.Timestamp(HSTART)]
F = {}
for nm, ctrl in (("|SPY", ["SPY"]), ("|SPY+Δ10y", ["SPY", "dy10"]), ("|Δ10y", ["dy10"])):
    s = np.array([pcorr(H3.iloc[e - W:e], "KRE", "KBWB", ctrl) for e in ends3]); F[nm] = s
orig_p = {"|SPY": ("0.728", "11"), "|SPY+Δ10y": ("0.719", "12.6"), "|Δ10y": ("0.697", "1.6")}
for nm, s in F.items():
    cmp(f"partial corr KRE,KBWB {nm}: value, pct", f"{s[-1]:.3f}, {(s <= s[-1]).mean()*100:.1f}", f"{orig_p[nm][0]}, {orig_p[nm][1]}")
sp = np.array([stats.spearmanr(H3.KRE.values[e - W:e], H3.KBWB.values[e - W:e])[0] for e in ends3])
sp_pre = sp[:np.searchsorted(H3.index[[e - 1 for e in ends3]], pd.Timestamp("2026-01-01"))]
cmp("Spearman 63d: value, pct, pre-2026 min", f"{sp[-1]:.3f}, {(sp <= sp[-1]).mean()*100:.2f}, {sp_pre.min():.3f}", "0.717, 1.43, 0.718")
bkre = (H3.KRE.rolling(W).cov(H3.SPY) / H3.SPY.rolling(W).var()).loc[HSTART:]; bkbwb = (H3.KBWB.rolling(W).cov(H3.SPY) / H3.SPY.rolling(W).var()).loc[HSTART:]
cmp("SPY beta KRE / KBWB (pct)", f"{bkre.iloc[-1]:.2f} ({(bkre.dropna() <= bkre.iloc[-1]).mean()*100:.1f}) / {bkbwb.iloc[-1]:.2f} ({(bkbwb.dropna() <= bkbwb.iloc[-1]).mean()*100:.0f})", "0.33 (1.3) / 0.83 (10)")
LF = []
lp = np.log(P.loc[:END, ["KRE", "KBWB"]].dropna())
for k in (2, 5):
    rr = lp.diff(k).iloc[k::k]  # non-overlapping k-day returns, anchored at start
    rr = lp.iloc[::-1].iloc[::k].iloc[::-1].diff().dropna()  # anchored at END
    n = W // k
    s = rr.KRE.rolling(n).corr(rr.KBWB).dropna().loc[HSTART:]
    LF.append(dict(horizon_days=k, obs_per_window=n, current=s.iloc[-1], pct=(s <= s.iloc[-1]).mean()))
LF = pd.DataFrame(LF); LF.to_csv(f"{OUT}/F_lower_frequency.csv", index=False, float_format="%.4f")
cmp("2-day / 5-day return corr pct (non-overlapping k-day returns, same 63-session span)", " / ".join(f"{r.current:.3f} ({r.pct*100:.1f} pct)" for r in LF.itertuples()), "≈0.1 pct both", "original definition not recorded; NOT reproduced exactly")
pd.DataFrame({k: v for k, v in F.items()} | {"spearman": sp}, index=H3.index[[e - 1 for e in ends3]]).to_csv(f"{OUT}/F_partial_spearman_rolling.csv", float_format="%.4f")

# ------------------------------------------------------------------ G. within banks; ETF wrapper
H4 = R.loc["2021-01-01":END]
def rc(a, b):
    s = H4[a].rolling(W).corr(H4[b]).dropna(); return s.iloc[-1], (s <= s.iloc[-1]).mean()
for a, b, o in (("KRE", "OVL10", "0.900 (0.2 pct)"), ("OVL10", "REST", "0.845 (1.0 pct)"), ("OVL10", "KBWB14", "0.846 (12 pct)")):
    v, p = rc(a, b); cmp(f"since 2021: {a} vs {b}", f"{v:.3f} ({p*100:.1f} pct)", o)
cmp("KRE vs members basket (10/30 weights)", round(win.KRE.corr(win.BASKET), 3), 0.998)
cmp("KRE NAV-return corr with KBWB", round(win.KRE_NAV.corr(win.KBWB), 3), 0.714, "SSGA NAV file as downloaded 11/02; small difference unexplained")
cmat = win[MEM].dropna(axis=1).corr().values; avgpc = cmat[np.triu_indices_from(cmat, 1)].mean()
cmp("avg pairwise corr among KRE members (63d)", round(avgpc, 3), 0.64, "from study 1")

# ------------------------------------------------------------------ H. block bootstrap CI
bs = []
for _ in range(5000):
    starts = rng.integers(0, W - 5 + 1, size=int(np.ceil(W / 5)))
    ii = np.concatenate([np.arange(s, s + 5) for s in starts])[:W]
    bs.append(np.corrcoef(x[ii], y[ii])[0, 1])
lo, hi = np.percentile(bs, [2.5, 97.5])
cmp("block bootstrap 95% CI (5-day blocks, 5000 draws)", f"[{lo:.2f}, {hi:.2f}]", "[0.61, 0.81]", "original block length not recorded")
bs10 = []
for _ in range(5000):
    starts = rng.integers(0, W - 10 + 1, size=7); ii = np.concatenate([np.arange(s, s + 10) for s in starts])[:W]
    bs10.append(np.corrcoef(x[ii], y[ii])[0, 1])
cmp("block bootstrap 95% CI (10-day blocks)", "[%.2f, %.2f]" % tuple(np.percentile(bs10, [2.5, 97.5])), "[0.61, 0.81]")

# ------------------------------------------------------------------ figure
fig, ax = plt.subplots(2, 1, figsize=(13, 8), sharex=True)
s63 = roll[63]; s126 = roll[126]
ax[0].plot(s63, lw=.8, c="k", label="63d corr KRE–KBWB"); ax[0].plot(s126, lw=.8, c="tab:blue", label="126d")
ax[0].axhline(p10_63, c="r", ls="--", lw=.8, label=f"63d 10th pct ({p10_63:.3f})"); ax[0].legend(fontsize=8, loc="lower left")
ax[0].set_title("Rolling KRE–KBWB correlation of daily returns (since Feb 2012) — rebuilt stress test")
t5 = TR[(TR.pair == "KRE–KBWB")]
pp = pd.Series(F["|SPY"], index=H3.index[[e - 1 for e in ends3]])
ax[1].plot(pp, lw=.8, c="tab:purple", label="63d partial corr | SPY"); ax[1].plot(bkre.dropna(), lw=.8, c="tab:green", label="KRE 63d SPY beta")
ax[1].axhline(0, c="gray", lw=.5); ax[1].legend(fontsize=8, loc="lower left")
plt.tight_layout(); plt.savefig(f"{OUT}/fig_rolling.png", dpi=120)

C = pd.DataFrame(CMP); C.to_csv(f"{OUT}/comparison_with_original.csv", index=False)
pd.set_option("display.width", 250); pd.set_option("display.max_colwidth", 80)
print(C.to_string())
