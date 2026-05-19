# BOND Receipt — 2026-05-19

Live-data pull and reconcile run by BOND first boot.

| File | Action | Why | Workbook rows | STATUS change | Outbox |
|---|---|---|---|---|---|
| inbox/PROME-20260511-bond-refresh-and-architecture.md | INTEGRATE → processed | Task closed by Prome's 5/13 follow-up (TASK_REFRESH_2026-05-12); auction follow-up now done | — | — | — |
| inbox/signal_2026-05-14_30y_5pct_2007_headline.md | LOG_ONLY → processed | Narrative amplification; data already in STATUS; 30Y above 5 now confirmed sustained | — | Incorporated into regime read | — |
| (live data pull) | INTEGRATE | Refresh stale 5/13 dashboard | KB-BND-028..033 (6 rows) | Dashboard, regime, convergence, catalysts, bottom line, trade interface | to-LIQUID (🟠), to-HENRY (🟡) |

## Key Findings

- **10Y broke 4.5 → 4.59** on 5/15 (FRED DGS10). BND-07 5-session trigger Day 1.
- **30Y at 5.12** — sustained above 5 for 4 sessions (5/12–5/15). First such run since 2007.
- **Credit-duration decoupling sharpened:** HY OAS flat at 283, IG OAS *tightened* 4bps to 75. HYG only -0.62.
- **Bills clean** May 14-19 (BTC 2.66–3.20) — long-end move is term-premium, not mechanical demand failure.
- **TLT $83.01** new low; supports duration-short conviction.
- **SOFR-IORB -12bps** (more negative) — no funding-channel confirmation yet.
- **VX upgrades:** VX-BND-05 (long-end) and VX-BND-12 (term premium) moved to red status emoji (score stayed 4 pending 5-session streak / 20Y confirmation).

## Next Catalyst

**May 20 (tomorrow) 20Y Bond auction.** Clean = ride term-premium move (hold TLT puts). Failed (BTC <2.3 / tail >2bps / dealer spike) = escalate BOND to orange and upgrade TLT puts to 4/5 conditional add.

## Open Gaps

- CDX.HY / CDX.IG still not wired into local market-data tool (VX-BND-06 data gap persists).
- HY-only weekly issuance split still missing (SIFMA aggregate sufficient to reject "freeze" but not classify HY access).
