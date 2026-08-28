# Load-bearing figure manifest for AGENTS/HENRY/STATUS.md — built 2026-08-28 BEFORE the prose rotation.
# A figure is LOAD-BEARING if another desk's gate, my own kill/threshold, or a graded prediction consumes it.
CARD_ONLY = [("0.7787","THREEFYTP10 7/17"),("0.8682","THREEFYTP10 8/21")]  # canonical home = the grade card
FIGURES = [
 # --- 260 ladder / triad (rung-4 reading, WQ 106) ---
 ("263","HY OAS current [FRED 8/27]"),("260","the HY leg's line"),("3bp","distance to the line"),
 ("0 OF 5","my rung-4 count"),("n=120","thesis-life obs"),("787","full-series obs"),
 ("259","the single sub-260 print"),("2025-01-22","its date"),("263 [6/17]","thesis-life min tie"),
 ("14.51","VIXCLS 8/27, leg-2 satisfying close"),("14.25","VIX 8/14 nearest close"),
 ("SIXTH","VIX leg satisfied-session count"),
 # --- vol / gamma ---
 ("14.21","VIX live"),("11.26","VIX9D"),("17.40","VIX3M"),("86.02","VVIX"),("144.05","SKEW"),
 ("7,718","gamma flip"),("+39","spot above flip"),("+$20.4B","Net GEX"),("2,959","contracts"),
 # --- credit ---
 ("1,031","CCC OAS"),("153","BB OAS"),("878","CCC-BB gap"),("+85","CCC 3mo"),("−9","BB 3mo"),
 # --- HEN-42 graded cells ---
 ("+34bp","2s10s registration low 7/23"),("+47bp","2s10s latest published 8/26"),
 ("21 of 21","leg-1 failure count"),("+43","2s10s min 8/4"),("+53","2s10s max 8/17"),
 ("+52","30s10s 8/26"),("+46","30s10s 7/23"),
 ("4.19","DGS2 pinned 8/17-8/20"),("−4bp","7/29 front end"),("+11bp","7/29 long end"),
 ("8bp","long-end real led 7/23-8/26"),
 ("+8.95bp","TP post-registration"),("+7.01bp","TP inside registration window"),("44%","TP share in-window"),
 ("+2.49bp","BOND's TP leg"),("83%","BOND's TP share"),("+4.25bp","TP over the blind window"),
 ("658","pre-registered session distribution"),("14bp","largest 1-session 2s10s move"),
 ("p99","distribution tail"),("13bp","flattening needed to rescue CONFIRM"),
 # --- post-freeze policy-path datum ---
 ("0.48","Kalshi Sept-hike LIVE-INTRADAY"),("+17pp","Kalshi move"),
 ("+5.7bp","5Y live"),("+2.8bp","10Y live"),("−0.6bp","30Y live"),("−6.3bp","5s30s live"),
 # --- market levels ---
 ("7,767.24","SPX"),("4.67","10Y"),("83.33","TLT"),("74.29","KRE"),("159.91","USD/JPY"),
 ("87.84","Brent 8/26 corrected"),("94.39","Brent 8/21"),("−6.94%","Brent 3-session"),
 # --- standing thresholds (static but consumed) ---
 (">320","HY yellow"),(">400","HY orange"),(">500","HY red"),("<$60","KRE"),("<47","ISM"),
 (">5.0","10Y term-premium"),(">23","vol-control"),(">30","VIX risk-off"),
 # --- dated catalysts ---
 ("8/29","HEN-42 flip"),("8/31","pending cells publish"),("9/9","sb0607 buybacks"),("9/11","Aug CPI"),
 # --- verdicts / pointers ---
 ("DENY","HEN-42 verdict"),("HEN-42","the prediction"),("H-2","same-kill counting rule"),
 ("H-1","simultaneity rule"),("GATE-HY-REKILL","LIQUID's rung"),("FT-12","RED's rung"),
 ("2026-08-28_HEN-42_GRADE_CARD_FROZEN","card pointer"),
]
if __name__=="__main__":
    import sys
    from pathlib import Path
    s=Path(sys.argv[1]).read_text()
    miss=[(t,w) for t,w in FIGURES if t not in s]
    print(f"FIGURE MANIFEST: {len(FIGURES)-len(miss)}/{len(FIGURES)} present in {sys.argv[1]}")
    for t,w in miss: print(f"   MISSING: {t!r}  ({w})")
    sys.exit(1 if miss else 0)
