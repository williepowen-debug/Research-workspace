# Do-Now Batch + X1 Reconciliation — 2026-06-25
**Author:** Claude Code Prome (Desktop CC origin — OpenClaw/Codex degraded)
**Session:** 2026-06-25, ~11:05 ET boot → ~12:20 ET write-back
**Purpose:** Capture the cross-agent synthesis from the do-now batch so nothing is lost. Domain artifacts live in each agent's own dir (SHAs below); this doc is the Prome-owned cross-agent layer + HENRY's read (which HENRY declined to self-commit).

---

## Session arc
Booted from Desktop Claude Code (Codex/OpenClaw API degraded; Prome is the live surface). Will authorized teammate-mode spawns (no other agents running). Spawned a **report-only** do-now batch: **SAM** (FXY position truth-up), **BROCK** (APO put confirm + PC read), **HENRY** (May PCE ingest). Ran follow-ups **B1** (BROCK credit-recognition discriminator), **S1** (SAM MOF intervention playbook), **X1** (independent shared-antecedent test, both agents). Then a Will-approved sequenced write-back.

## Live tape (≈11:09 ET, markets open)
HY OAS **271 [6/23]** (+6; back ABOVE the <260 kill) · CCC 956 [6/23] · Brent **$74.24** (−8% post Jun-20 Hormuz declaration) · USD/JPY 161.66 / FXY $56.76 (red) · 10Y ~4.39 live (vs 4.50 [6/23]; TLT +1.4% = duration bid) · VIX 18.43 · APO $121.64 (🟢→🟡, from $137.50) · ARES $112.54 · BIZD $12.19 · KRE $74.57 / OZK $51.89 / WAL $81.35 (banks calm/rallied) · Cushing sub-20M (EIA 6/24).

## Regime delta vs the 6/21 HEARTBEAT (which is now stale)
1. **Energy tail DEFLATED, not re-armed.** Jun-20 Hormuz re-closure declaration resolved **non-kinetic**; Brent fell ~8%. HAW-11 kinetic leg expired unfired 6/22. War-premium leg de-rated.
2. **HY widened back ABOVE the <260 kill (271).** The kill-the-bear scare is off; spreads modestly *support* the bear. 6/24 print pending (held-or-reverted confirmation).
3. **Cushing sub-20M → BRENT Boundary #3 FIRED** (EIA 6/24). Energy deflated on tape but coiled (physically tight + near-record spec short).
4. **Bank-vs-PC divergence — but MACRO, not credit** (see X1). Managers cracked, wrappers held, banks rallied.
5. **May PCE firm (core 3.4% YoY) but as-priced** — backward-looking, can't show the June energy washout yet. Real disinflation test = **June CPI (Jul 14)**.

---

## Agent outputs (durable artifacts in own dirs)
- **BROCK `e11daae4`** — `AGENTS/BROCK/domain/sources/MACRO_VS_CREDIT_DISCRIMINATOR_JUN25.md`: B1 5-variable credit-recognition watch-set (verdict: leaning MACRO); APO Dec $95P **LIVE MARK 6/25** (mid ~$3.35, 176 DTE, 22.3% OTM, recovered ~10–12× off the ~$28 6/15 mark — flagged LIVE-MARK / pending-broker, NOT booked P&L; $130 breach re-arms the put, no forced action); X1 PC-side. + SCRATCH/STATUS pointers.
- **SAM `8e6f4350`** — `AGENTS/SAM/MOF_INTERVENTION_PLAYBOOK.md`: S1 escalation ladder (T0–T3 × USD/JPY zone), strike history (Apr 30 @160.70, May 6 @157.89, ~¥11.73T), the speed/disorder trigger, FXY-stub-by-zone, the stop-vs-payoff whipsaw insight; X1 carry-side. + STATUS note (FXY PENDING broker recon).
- **HENRY — NOT self-committed (declined relayed approval; read captured here):** May PCE → **HEN-34 RESOLVED: hawkish-dots VALIDATED, inverse-feedback PENDING (not falsified)**; one-legged stagflation confirmed (rates leg live, energy leg inverted); higher-for-longer beats duration-break (duration caught a bid; 10Y>4.8 path less likely post energy-inversion); front-end roughly fair, asymmetric down (2Y 4.16). Catalysts: NFP Jul 3, CPI Jul 14, month-end 6/30 $165B into negative gamma.

---

## ★ X1 RECONCILIATION (the keeper) — carry-unwind vs PC-compression: ~1 root, don't double-count
SAM and BROCK answered the shared-antecedent test **independently** and converged on the same operational rule (independent convergence → ratify):

- **They look like they disagree** — SAM "correlated-not-identical / independent in base case," BROCK "shared dominant root" — but they're describing **opposite tails of the yen distribution**:
  - *Higher-for-longer grind (today):* PC multiples compress AND yen stays weak (carry on) → for a long-FXY position, PC down + FXY down. **Shared macro root.**
  - *Disorderly risk-off / carry unwind (the tail FXY bets on):* yen strengthens (FXY up), global delever force-sells the same alts (Aug-5-2024 template) → FXY up + PC down. **Shared root again.**
  - *Idiosyncratic PC credit event (the only clean decoupling):* BDC sub-90¢ markdown / div-cut / PIK→default craters wrapper NAVs while yen + JGBs stay calm → PC fires alone.
- **Rule:** PC-compression + the yen move are **co-symptoms of one root in both the grind and the unwind.** They count as **two independent bear confirmations ONLY when PC fires via the credit-substance leg.**
- **The unification:** BROCK's "now it's credit" trigger IS X1's decoupling marker — one line does both jobs:
  > **Wrapper basket (ARCC/FSK/OBDC/BIZD) LEADS the managers down — APO/ARES hold/bounce on a down day while wrappers make new lows — confirmed by HY OAS > 280 sustained.**
- **Reading today:** decisively **MACRO** (managers −11/−13% cumulative, wrappers ~flat, KRE rallied; HY 271 in-band, no >280). Today's alts selloff added ~½ a confirmation, not two. **Discount the PC + carry co-move ~50% until the trigger fires.**

### So-what
1. **NEXUS double-counts** if it treats PC-compression and the carry signal as separate bear confirmations right now — feed it this rule.
2. **One trigger replaces five** (above) — same line answers both the credit-recognition and the independence questions.
3. **Intersects LIQUID directly:** *HY OAS > 280* is LIQUID's half of the trigger → reinforces the LIQUID reactivation case (BROCK on the wrapper rotation, LIQUID on the spread breakout).

---

## Position cards — PENDING broker reconciliation (NOT booked truth)
- **FXY (SAM):** live FXY $56.74 / USD/JPY 161.65, ~−2.7% unrealized. Binding stop = USD/JPY 162.5 (0.85y away); FXY-55.50 leg does NOT cover it (~$0.94 gap). Action hinges on: did the 13→6 trim fill 6/23? Hold-the-stub if filled (MOF tail pays it); trim-now if not. **Owed: Will's broker truth (fill Y/N, price, count, stop implementation).**
- **APO Dec $95P (BROCK):** ~1 contract, live mid ~$3.35, recovered ~10–12×. No forced action. Cost-basis = broker.

## Open items
1. **FXY broker truth** (Will) → relay to warm SAM to finalize.
2. **LIQUID reactivation** (Will-decision) — now well-motivated.
3. **Regime-surface refresh** — HEARTBEAT / TODAY / NEXUS still on the 6/21 "energy re-fat / HY-near-kill-from-below" read; now wrong. Refresh once (Prome-owned).
4. **HENRY domain update** — pending direct Will confirm (or next HENRY session); read preserved here.
5. **Auto-memory finding** (don't-double-count rule, ratified by independent convergence) worth capturing — but MEMORY.md is over its size limit; prune first.

## Warm agents
SAM + BROCK left alive/idle for follow-ups (e.g. B2 late-July Q2 BDC catalyst map). Release at closeout if unused.
