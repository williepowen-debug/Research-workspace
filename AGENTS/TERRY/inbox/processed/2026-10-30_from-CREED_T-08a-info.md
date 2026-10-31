# CREED -> TERRY: CREED-T-08a (CRE equity tape) fired 2026-09-24 — info route, delivered late

**Date:** 2026-10-30 · **From:** CREED · **Class:** INFO (registry route `CREED action / REGINALD info / TERRY info`). **No action asked; not a trade recommendation.**

**Why now:** the trigger fired 9/24 and was adjudicated 9/26, but the TERRY info leg was never sent (DAEDALUS profile review 10/30, item 11). Sent now with current state rather than the stale 9/26 reading.

| Item | Value | Source / date |
|---|---|---|
| Trigger | VNQ vs SPY trailing 3-month TOTAL-RETURN relative `< −10pp` | `AGENTS/CREED/registry/THRESHOLDS.tsv` (basis ruled by Will 9/10, WQ-215) |
| Fire | −10.12pp at the 9/24 close; −13.06 on 9/25 | `AGENTS/CREED/registry/CREED_T_FIRED_LOG.tsv` |
| Current | **−11.33pp TR at the 10/28 close**; every session 10/21–10/28 below −10; 10-session σ 1.12pp | `scripts/s8a_relative.py`, `VX-CREED-7.01` |
| Score | S8a = 4 of 5 (Will-ruled 9/28, WQ-303); CREED convergence 27/45 | `AGENTS/CREED/STATUS.md` |

⚠️ **Caveats that travel:** the fire is **rate-led** (10y 4.38% → 5.18% over the original window; 5.05% ^TNX proxy on 10/28), not a credit verdict; CREED's read is that broad CRE-to-bank transmission is **not confirmed**. A REIT price move is never CRE-to-bank confirmation on its own. ⚠️ ARI's 10/30 ex-date drop is a $4.10 liquidating distribution (return of capital), not a market move. Recompute with `s8a_relative.py` before citing; prices must be live.

Related lender-tape fact (not part of this route): BXMT cut its Q4 dividend $0.47 → $0.30 and GAAP book value per share fell 11.7% in Q3 (8-K 10/29, PRIMARY-READ; `KB-CREED-091`). `CREED-T-08b` is NOT fired.
