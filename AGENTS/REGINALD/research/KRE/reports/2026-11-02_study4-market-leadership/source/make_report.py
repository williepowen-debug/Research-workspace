"""Build REPORT.md tables for study 4 from out/*.csv"""
import os, re
import numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)); OUT = f"{H}/out"


def f(x, d=2, pct=False, sign=False):
    if pd.isna(x): return "—"
    if pct: return f"{x*100:.0f}"
    return f"{x:+.{d}f}" if sign else f"{x:.{d}f}"


def t_sens():
    Q1 = pd.read_csv(f"{OUT}/q1_benchmarks.csv")
    L = ["| Benchmark | KRE corr now | median (pre-2025) | pct | KRE beta now | median | pct | KBWB beta now | median | pct |", "|---|---|---|---|---|---|---|---|---|---|"]
    for b in ["SPY", "RSP", "IWM", "IWN", "QQQ", "XLF", "KBE"]:
        kc = Q1[(Q1.asset == "KRE") & (Q1.bench == b) & (Q1.metric == "corr")].iloc[0]
        kb = Q1[(Q1.asset == "KRE") & (Q1.bench == b) & (Q1.metric == "beta")].iloc[0]
        bb = Q1[(Q1.asset == "KBWB") & (Q1.bench == b) & (Q1.metric == "beta")].iloc[0]
        L.append(f"| {b} | {f(kc.current)} | {f(kc.median_pre2025)} | {f(kc.pct_pre2025, pct=True)} | {f(kb.current)} | {f(kb.median_pre2025)} | {f(kb.pct_pre2025, pct=True)} | {f(bb.current)} | {f(bb.median_pre2025)} | {f(bb.pct_pre2025, pct=True)} |")
    return "\n".join(L)


def t_factor():
    E = pd.read_csv(f"{OUT}/q3_exposures.csv")
    lab = {"MKT_s": "Market (Mkt−RF)", "SMB_s": "Size (SMB)", "HML_s": "Value (HML)", "MOM_s": "Momentum", "dy10": "Δ10y (per 1pp)"}
    L = ["| 5-factor loading (M3) | 21d now | 21d median · pct | 63d now | 63d median · pct | 63d to 9/30, pure French · pct | 126d now | 126d median · pct |", "|---|---|---|---|---|---|---|---|"]
    for k, nm in lab.items():
        c = []
        for w in (21, 63, 126):
            r = E[(E.window == w) & (E.model == "M3 +Δ10y") & (E.factor == k) & (E.end == "to 10/30 (spliced)")].iloc[0]
            c.append((r.current, r.hist_median, r.pct))
        p = E[(E.window == 63) & (E.model == "M3 +Δ10y") & (E.factor == k) & (E.end == "to 9/30 (pure French)")].iloc[0]
        L.append(f"| {nm} | {f(c[0][0])} | {f(c[0][1])} · {f(c[0][2], pct=True)} | **{f(c[1][0])}** | {f(c[1][1])} · {f(c[1][2], pct=True)} | {f(p.current)} · {f(p.pct, pct=True)} | {f(c[2][0])} | {f(c[2][1])} · {f(c[2][2], pct=True)} |")
    U = pd.read_csv(f"{OUT}/q3_unexplained.csv")
    for w in (21, 63, 126):
        pass
    r = {w: U[(U.window == w) & (U.model == "M3 +Δ10y") & (U.end == "to 10/30 (spliced)")].iloc[0] for w in (21, 63, 126)}
    p = U[(U.window == 63) & (U.model == "M3 +Δ10y") & (U.end == "to 9/30 (pure French)")].iloc[0]
    L.append(f"| R² | {f(r[21].r2)} | {f(r[21].r2_hist_median)} · {f(r[21].r2_pct, pct=True)} | **{f(r[63].r2)}** | {f(r[63].r2_hist_median)} · {f(r[63].r2_pct, pct=True)} | {f(p.r2)} · {f(p.r2_pct, pct=True)} | {f(r[126].r2)} | {f(r[126].r2_hist_median)} · {f(r[126].r2_pct, pct=True)} |")
    L.append(f"| Residual vol (ann.) | {f(r[21].resid_vol*100,1)}% | {f(r[21].resid_vol_hist_median*100,1)}% · {f(r[21].resid_vol_pct, pct=True)} | **{f(r[63].resid_vol*100,1)}%** | {f(r[63].resid_vol_hist_median*100,1)}% · {f(r[63].resid_vol_pct, pct=True)} | {f(p.resid_vol*100,1)}% · {f(p.resid_vol_pct, pct=True)} | {f(r[126].resid_vol*100,1)}% | {f(r[126].resid_vol_hist_median*100,1)}% · {f(r[126].resid_vol_pct, pct=True)} |")
    L.append(f"| Residual corr KRE–KBWB | {f(r[21].resid_corr_KRE_KBWB)} | {f(r[21].resid_corr_hist_median)} · {f(r[21].resid_corr_pct, pct=True)} | **{f(r[63].resid_corr_KRE_KBWB)}** | {f(r[63].resid_corr_hist_median)} · {f(r[63].resid_corr_pct, pct=True)} | {f(p.resid_corr_KRE_KBWB)} · {f(p.resid_corr_pct, pct=True)} | {f(r[126].resid_corr_KRE_KBWB)} | {f(r[126].resid_corr_hist_median)} · {f(r[126].resid_corr_pct, pct=True)} |")
    return "\n".join(L)


def t_models():
    U = pd.read_csv(f"{OUT}/q3_unexplained.csv"); U = U[U.end == "to 10/30 (spliced)"]
    L = ["| Model | R² 21d (pct) | R² 63d (pct) | R² 126d (pct) | 63d hist median R² | 63d resid corr KRE–KBWB (pct) |", "|---|---|---|---|---|---|"]
    for m in ["M0 SPY", "M1 MKT", "E1 RSP", "E2 RSP+CONC", "M2 FF3+MOM", "M3 +Δ10y", "M4 +CONC+ΔBaa"]:
        r = {w: U[(U.window == w) & (U.model == m)].iloc[0] for w in (21, 63, 126)}
        L.append(f"| {m} | {f(r[21].r2)} ({f(r[21].r2_pct, pct=True)}) | {f(r[63].r2)} ({f(r[63].r2_pct, pct=True)}) | {f(r[126].r2)} ({f(r[126].r2_pct, pct=True)}) | {f(r[63].r2_hist_median)} | {f(r[63].resid_corr_KRE_KBWB)} ({f(r[63].resid_corr_pct, pct=True)}) |")
    return "\n".join(L)


def t_lead():
    Ld = pd.read_csv(f"{OUT}/q1_leadership.csv")
    keep = ["corr SPY-RSP", "share of SPY var from CONC", "corr RSP-QQQ", "corr SPY-QQQ", "beta RSP~SPY", "beta IWN~SPY", "beta IWN~RSP", "corr HML_p-SPY", "vol CONC (ann.)"]
    L = ["| Market-structure metric (63d) | Now | pre-2025 median | pct | 2025 median | 2026 H1 median |", "|---|---|---|---|---|---|"]
    for k in keep:
        r = Ld[Ld.metric == k].iloc[0]
        L.append(f"| {k.replace('share of SPY var from CONC', 'share of SPY variance not explained by RSP').replace('HML_p', 'value (IWD−IWF)').replace('CONC', 'SPY−RSP')} | {f(r.current)} | {f(r.median_pre2025)} | {f(r.pct_pre2025, pct=True)} | {f(r.median_2025)} | {f(r.median_2026H1)} |")
    return "\n".join(L)


def t_sectors():
    Q2 = pd.read_csv(f"{OUT}/q2_sectors.csv"); SO = pd.read_csv(f"{OUT}/q3b_sectors_m2.csv").set_index("asset")
    BD = pd.read_csv(f"{OUT}/q3b_beta_decomp.csv"); BD = BD[BD.period == "now 63d to 10/30 (spliced)"].set_index("asset")
    L = ["| ETF (role) | SPY beta now · pct | % days below p10: 2025 / 2026 | RSP beta now · pct | Δ SPY beta vs 2012–24: total = structure + own loadings | 5-factor R² pct | resid vol pct | OOS R² hist → Jul–Oct 2026 |", "|---|---|---|---|---|---|---|---|"]
    role = {"KRE": "regional banks", "KBWB": "large banks", "XLF": "financials", "KIE": "insurance", "IWN": "small value", "XLI": "industrials", "XLB": "materials",
            "IYT": "transports", "ITB": "homebuilders", "IYR": "REITs", "XLU": "utilities"}
    for t in role:
        s = Q2[(Q2.etf == t) & (Q2.market == "SPY")].iloc[0]; r = Q2[(Q2.etf == t) & (Q2.market == "RSP")].iloc[0]
        b = BD.loc[t]; so = SO.loc[t]
        L.append(f"| **{t}** ({role[t]}) | {f(s.beta_now)} · {f(s.beta_pct_pre2025, pct=True)} | {f(s.share_days_below_p10_2025, pct=True)}% / {f(s.share_days_below_p10_2026, pct=True)}% | {f(r.beta_now)} · {f(r.beta_pct_pre2025, pct=True)} | {f(b.dBeta_total, sign=True)} = {f(b.dBeta_from_structure, sign=True)} {f(b.dBeta_from_loadings, sign=True)} | {f(so.r2_pct, pct=True)} | {f(so.resid_vol_pct, pct=True)} | {f(so.oos_hist)} → {f(so.oos_2026JulOct)} |")
    return "\n".join(L)


def t_corr():
    C = pd.read_csv(f"{OUT}/q3b_corr_decomp.csv")
    L = ["| Period | KRE–KBWB corr | from common factors | from residuals | residual corr | KRE factor vol | KRE resid vol | KBWB factor vol | KBWB resid vol |", "|---|---|---|---|---|---|---|---|---|"]
    for r in C.itertuples():
        L.append(f"| {r.period} | {f(r.corr)} | {f(r.from_common_factors)} | {f(r.from_residuals)} | {f(r.resid_corr)} | {f(r.KRE_factor_vol*100,1)}% | {f(r.KRE_resid_vol*100,1)}% | {f(r.KBWB_factor_vol*100,1)}% | {f(r.KBWB_resid_vol*100,1)}% |")
    return "\n".join(L)


def t_vm():
    V = pd.read_csv(f"{OUT}/q3_volmatched.csv")
    L = ["| Metric (63d) | Now | pct vs all 2012–24 | pct vs volatility-matched windows | vol-matched median |", "|---|---|---|---|---|"]
    for r in V.itertuples():
        L.append(f"| {r.metric} | {f(r.current)} | {f(r.pct_all_pre2025, pct=True)} | **{f(r.pct_volmatched, pct=True)}** | {f(r.median_volmatched)} |")
    return "\n".join(L)


def t_oos():
    O = pd.read_csv(f"{OUT}/q3_oos.csv")
    per = ["2013-11→2019-12", "2020–2022", "2023–2024", "2025", "2026 Jan–Jun", "2026 Jul–Oct"]
    L = ["| Asset | Model | " + " | ".join(per) + " |", "|---|---|" + "---|" * len(per)]
    for a in ("KRE", "KBWB"):
        for m in ["M0 SPY", "E1 RSP", "E2 RSP+CONC", "M2 FF3+MOM", "M3 +Δ10y", "M4 +CONC+ΔBaa"]:
            r = O[(O.asset == a) & (O.model == m)].set_index("period")
            L.append(f"| {a} | {m} | " + " | ".join(f(r.loc[p, 'oos_r2_pooled']) for p in per) + " |")
    n = O[(O.asset == "KRE") & (O.model == "M0 SPY")].set_index("period").blocks
    L.append("| blocks | | " + " | ".join(str(int(n[p])) for p in per) + " |")
    return "\n".join(L)


def t_beta_terms():
    D = pd.read_csv(f"{OUT}/q4b_rolling_beta_terms.csv", parse_dates=["date"], index_col=0)
    ref = D.loc["2012-03-01":"2024-12-31"].median()
    rows = [("2012–2024 median", ref)]
    for lab, a, b in (("2025 H1", "2025-01", "2025-06"), ("2025 H2", "2025-07", "2025-12"), ("2026 H1", "2026-01", "2026-06"), ("Jul–Sep 2026", "2026-07", "2026-09")):
        rows.append((lab + " (median)", D.loc[a:b].median()))
    rows.append(("window ending 10/30/2026", D.iloc[-1]))
    L = ["| Period | KRE SPY beta | = market term | + value term | + size term | + momentum term | + Δ10y term | + residual | KRE market loading | value factor's beta on SPY | size factor's beta on SPY | KBWB SPY beta | KBWB market term |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for lab, r in rows:
        L.append(f"| {lab} | **{f(r.KRE_uni)}** | {f(r.KRE_term_MKT_s)} | {f(r.KRE_term_HML_s, sign=True)} | {f(r.KRE_term_SMB_s, sign=True)} | {f(r.KRE_term_MOM_s, sign=True)} | {f(r.KRE_term_dy10, sign=True)} | {f(r.KRE_resid_term, sign=True)} | {f(r.KRE_load_MKT_s)} | {f(r.fbeta_HML_s, sign=True)} | {f(r.fbeta_SMB_s, sign=True)} | {f(r.KBWB_uni)} | {f(r.KBWB_term_MKT_s)} |")
    return "\n".join(L)


def t_onsets():
    O = pd.read_csv(f"{OUT}/q4_onsets.csv")
    O2 = pd.read_csv(f"{OUT}/onsets.csv")
    want = [("corr_SPY_RSP", "below p10", O), ("HMLp_beta_on_SPY", "below p10", O), ("HMLff_beta_on_MKTff", "below p10", O), ("corr_QQQ_RSP", "below p10", O),
            ("resid_corr_KRE_KBWB_M3", "below p10", O), ("KRE_corr_KBWB", "below p10", O), ("KRE_M3_dy10", "below p10", O),
            ("KRE_corr_RSP", None, O2), ("KRE_beta_SPY", "below p10", O), ("KRE_corr_IWN", "below p10", O), ("KRE_M3_R2", "below p10", O),
            ("KBWB_beta_SPY", "below p10", O), ("IWN_beta_SPY", "below p10", O), ("XLU_beta_SPY", None, O2), ("KRE_corr_XLI", None, O2), ("KRE_beta_RSP", "below p10", O),
            ("XLI_beta_SPY", "below p10", O)]
    L = ["| Series (63d) | 2025: first 10-day run below pre-2025 p10 · % days below | 2026: first run · % days below |", "|---|---|---|"]
    for s, side, src in want:
        cells = []
        for yr in (2025, 2026):
            if side:
                r = src[(src.series == s) & (src.year.astype(str) == str(yr)) & (src.side == side)]
                col = "first_onset_10d"
            else:
                r = src[(src.series == s) & (src.year.astype(str) == str(yr))]; col = "first_onset"
            if r.empty: cells.append("— · 0%"); continue
            r = r.iloc[0]; cells.append(f"{r[col] if isinstance(r[col], str) else '—'} · {r.share_days*100 if 'share_days' in r else r.share_days_below*100:.0f}%" if False else f"{r[col] if isinstance(r[col], str) else '—'} · {(r['share_days'] if 'share_days' in r.index else r['share_days_below'])*100:.0f}%")
        L.append(f"| {s} | {cells[0]} | {cells[1]} |")
    return "\n".join(L)


def t_rate():
    R = pd.read_csv(f"{OUT}/q3c_rate_beta_value.csv")
    L = ["| Series | Δ10y beta (63d, controlling SPY) now | pct vs 2012–24 | 2012–24 median | 2026 median |", "|---|---|---|---|---|"]
    for r in R.itertuples():
        L.append(f"| {r.series.replace('HML_p', 'Value factor (IWD−IWF)')} | {f(r.rate_beta_now, 3, sign=True)} | {f(r.pct_pre2025, pct=True)} | {f(r.median_pre2025, 3, sign=True)} | {f(r.median_2026, 3, sign=True)} |")
    return "\n".join(L)


if __name__ == "__main__":
    fills = {k: v() for k, v in dict(T_SENS=t_sens, T_FACTOR=t_factor, T_MODELS=t_models, T_LEAD=t_lead, T_SECT=t_sectors, T_CORR=t_corr, T_VM=t_vm,
                                       T_OOS=t_oos, T_TERMS=t_beta_terms, T_ONSETS=t_onsets, T_RATE=t_rate).items()}
    tpl = open(f"{H}/REPORT_template.md").read()
    for k, v in fills.items(): tpl = tpl.replace("{{" + k + "}}", v)
    open(f"{H}/REPORT.md", "w").write(tpl); print("unfilled:", re.findall(r"\{\{\w+\}\}", tpl))
