#!/usr/bin/env python3
"""Amendment 3 three-scenario model for Brevard County and Palm Bay (CORAL, 2026-11-17).

Static parcel model: the 2026 final NAL roll (FL DOR, Brevard 15, ASMNT_YR 2026) with the
amendment's 2028 homestead exemption ($250,000 on non-school assessed value) and the 2027
step ($150,000) applied to today's values. Millage = 2025 rates (Brevard TACD 2025; DOR
Table 1 FY2025-26), the same vintage the Revenue Estimating Conference used. The 5% cap on
non-homestead assessment growth is a growth effect and is zero on a static roll.

Inputs (not in the repo; fetched 2026-11-17 from floridarevenue.com PTO data portal):
  NAL15F202602.csv  (Tax Roll Data Files/NAL/2026F/Brevard 15 Final NAL 2026.zip)
Usage: python3 this.py /path/to/NAL15F202602.csv
"""
import sys
import numpy as np
import pandas as pd

NAL = sys.argv[1]
PB_TACS = {"54U0", "34U0"}           # Palm Bay columns in 2025 Brevard TACD (millage 7.6993)
PB_OPER = 6.7000                     # Palm Bay operating millage FY2025-26 (DOR Table 1)
PB_TOTAL = 7.6993                    # Palm Bay city incl. voted debt (TACD 2025)
CO_GF = 2.8643                       # Brevard County general fund FY2025-26 (DOR Table 1)
PB_NONSCHOOL_ALL = 2.8643 + 0.3242 + 0.134 + 0.3 + 0.0458 + 0.0275 + 0.027 + 0.1555 + 0.1793 + 7.6993
VACANT_UC = {"000", "010", "040", "070", "080", "090", "0000", "0010", "0040", "0070"}
CAP = 10.0                           # constitutional operating cap, Art. VII s.9(b)

cols = ["DOR_UC", "AV_NSD", "TV_NSD", "TAX_AUTH_CD", "EXMPT_01", "EXMPT_02"]
df = pd.read_csv(NAL, usecols=cols, dtype={"TAX_AUTH_CD": str, "DOR_UC": str}, low_memory=False)
for c in ["AV_NSD", "TV_NSD", "EXMPT_01", "EXMPT_02"]:
    df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)
df["hs"] = df.EXMPT_01 > 0
other_ex = (df.AV_NSD - df.TV_NSD - df.EXMPT_01 - df.EXMPT_02).clip(lower=0)
for X in (150_000, 250_000):
    df[f"tv{X}"] = np.where(df.hs, (df.AV_NSD - other_ex - X).clip(lower=0), df.TV_NSD)
df["vacant"] = df.DOR_UC.fillna("").str.zfill(3).isin(VACANT_UC)
df["exempt_nonhs"] = (~df.hs) & (df.TV_NSD == 0)   # government, church etc.


def run(d, name, mill, fee_basis):
    tv0, tv1 = d.TV_NSD.sum(), d.tv250000.sum()
    levy0 = tv0 * mill / 1000
    gap = (tv0 - tv1) * mill / 1000
    h, n = d[d.hs], d[~d.hs]
    out = {"name": name, "parcels": len(d), "homesteads": len(h), "base0_B": tv0 / 1e9, "base1_B": tv1 / 1e9,
           "levy0_M": levy0 / 1e6, "gap_M": gap / 1e6, "gap_share": gap / levy0,
           "gap150_M": (tv0 - d.tv150000.sum()) * mill / 1000 / 1e6}
    sav = (h.TV_NSD - h.tv250000) * mill / 1000
    out["hs_saving_median"] = sav.median()
    # Scenario A: flat per-parcel assessment fills the gap
    payers = d[~d.exempt_nonhs & (~d.vacant if fee_basis == "improved" else True)]
    fee = gap / len(payers)
    out.update(A_fee=fee, A_payers=len(payers), A_hs_share=payers.hs.mean(),
               A_hs_worse=(sav < fee).mean(), A_hs_net_median=(sav - fee).median())
    # Scenario B: no new fees; millage raised to hold revenue, capped
    m_need = levy0 / tv1 * 1000
    m_set = min(m_need, CAP)
    out.update(B_mill_need=m_need, B_mill_set=m_set, B_cut_M=max(0, levy0 - tv1 * m_set / 1000) / 1e6,
               B_nonhs_share=n.tv250000.sum() / tv1,
               B_nonhs_median_rise=(n[n.TV_NSD > 0].TV_NSD.median() * (m_set - mill) / 1000),
               B_hs_net_median=(sav - h.tv250000 * (m_set - mill) / 1000).median())
    return out


pb = df[df.TAX_AUTH_CD.isin(PB_TACS)]
res = [run(pb, "Palm Bay (city operating)", PB_OPER, "improved"),
       run(pb, "Palm Bay (city operating, fee on all parcels)", PB_OPER, "all"),
       run(df, "Brevard County general fund (countywide)", CO_GF, "improved")]
h = pb[pb.hs]
allsav = (h.TV_NSD - h.tv250000) * PB_NONSCHOOL_ALL / 1000
print(f"Palm Bay homestead, all non-school levies ({PB_NONSCHOOL_ALL:.4f} mills): median saving ${allsav.median():,.0f}, "
      f"p25 ${allsav.quantile(.25):,.0f}, p75 ${allsav.quantile(.75):,.0f}; homesteads {len(h):,}; "
      f"fully exempt from non-school tax at $250k {(h.tv250000 == 0).mean():.1%}; vacant parcels {pb.vacant.mean():.1%}")
for r in res:
    print("\n".join(f"  {k}: {v:,.4f}" if isinstance(v, float) else f"  {k}: {v}" for k, v in r.items()))
    print()
