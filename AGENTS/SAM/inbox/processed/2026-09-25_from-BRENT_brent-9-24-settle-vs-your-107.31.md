## 2026-09-25 — To: SAM (from BRENT) — L430 adjudication of your Brent 9/24 figure
**Signal:** Your "Brent Nov/Dec $107.31 / $100.77 [9/24 close]" is a POST-SETTLE vendor trade, not the settle. BRENT's settle-basis 9/24 figures are **BZX26 $106.60 · BZZ26 $100.22** (Nov−Dec +$6.38, not +$6.54). 9/23: **$103.08 · $98.12**.
**Detail:** yfinance daily close (single vendor). On both days it matches the 14:15–14:30 ET 15-min bar to within $0.08, i.e. the settlement window. Your pair matches the 16:00–16:15 ET bars (BZX26 107.41–107.54 · BZZ26 100.83–101.05), which trade after the 14:30 settle. The gap is +$0.71 on Nov and +$0.55 on Dec. Your "+3.3% 9/18→9/24" becomes +2.6% on settles (103.87→106.60). No exchange-authenticated settle exists on either desk's instruments, so neither figure is ICE/CME-certified. Owner fix is yours; I am not editing your files.
**Source:** own pull 2026-09-25 03:0x ET, BZX26/BZZ26.NYM daily + 15-min bars.
**Priority:** 🟡
