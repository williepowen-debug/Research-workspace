# FIRE CARD — Monolines (COF / SYF / ALLY) — consumer-credit print, single-name puts (post-print)
**Setup ID:** TRY-FIRE-003 · **Trigger class:** PRINT (consumer-credit, un-maskable-unsecured leg)
**Thesis owner:** CARL (consumer-credit cohort — owns SYF/ALLY/COF) + REGINALD Q2 grid (monoline LEAD block, "prints first, un-maskable unsecured") + grading instrument. NEXUS regime = backdrop. · **Card pre-built:** 2026-06-27 · **Fired:** ____
**Status:** PROPOSE-ONLY — Will [Approve] required (rule #5). The earliest Q2 tell; precedes the regional cards (TRY-FIRE-002).

══════════════════════════════════════════════════════════════
ZONE 1 — PRE-LOCKED (do NOT re-derive at fire)
══════════════════════════════════════════════════════════════
- **Catalyst window:** monoline Q2 prints **~Jul 18–23, 2026** [VERIFY each issuer's confirmed date ~2wk ahead — SYF/COF late-July, ALLY mid-late-July]. This is the LEADING edge — it prints before the regionals (TRY-FIRE-002).
- **Trigger condition (exact) — must grade as UN-MASKED deterioration, NOT headline NCO.**
  CARL documents active **composition-masking**: SYF cut its FY26 NCO guide to <5.5% via book-shrinkage/survivor-pool (Home&Auto −3.7%, active accts −0.7%, ACL +36bps); ALLY 5 straight "improvement" quarters on S-tier mix-down; COF "ALLY-pattern confirmed." So a clean/improving headline NCO is the EXPECTED masked outcome — it is NOT the signal. Grade the un-mask tells (**need ≥2**, or 1 tell synchronized across ≥2 names):
  1. **ACL/reserve BUILD on a FLAT-or-SHRINKING receivables book** — the clean discriminator. On a shrinking monoline book a reserve build is unambiguous deterioration, NOT growth-beta (the regional ALLY beta-trap doesn't apply when the book is contracting).
  2. **Delinquency FORMATION accelerating** — early-stage roll / 30+ DQ / NPF rising QoQ ex-seasonal (the leading edge masking can't hide; NCO lags it ~2 quarters).
  3. **NCO guidance RAISED** — esp. SYF (it CUT to <5.5% in Q1; a re-raise = reversal) — or realized NCO rises *despite* book-shrinkage.
  4. **Survivor-pool exhaustion** — active accounts / receivables fall further + payment-rate drops = the masking lever running out.
- **One-line setup:** the first un-masked consumer-credit print confirms the K-shape deterioration the headline hides — buy the named monoline's downside before the multiple re-rates to the cohort reality.
- **Structure:** **single-name puts** on the firing name, **post-print duration** PAST the print AND toward the vintage loss-window (CARL: FY25 vintage lands 2H-26 / Q1-27) → **Sep / Oct / Jan-27** puts, **~8–12% OTM**. Consider a **put SPREAD** if post-print IV stays rich (cut theta).
- **Name selection (decide at fire by which un-masks cleanest + has the liquid chain):**
  - **SYF** — purest card-subprime monoline; cleanest un-mask read (Q1 already 🔴-cohort, CRL-12 77→55%).
  - **COF** — dual-axis (card NCO 5.1% "clean" + auto subprime-mix +21%, $230M ACL build); **most liquid options**.
  - **ALLY** — the **beta-trap name** (collective/growth build, S-tier mix-down); only if it clearly un-masks past its mask — apply the `grade_print.py` ALLY guard.
- **Why this expression:** un-maskable consumer-credit substance = single-name put, NOT XLF/KRE ETF (dilutes the idiosyncratic tell). Post-print = capture the recognition-lag re-rate, not a binary earnings gap.
- **Alternatives rejected:** pre-print entry = gambling the binary (modal outcome is a MASKED clean headline → would gap UP; violates rule #6 + "no premium into a move"). ETF = dilutes. Naked long calls — n/a (short thesis).
- **Max-loss budget:** $500 per card (Will 2026-06-26).
- **Invalidation (thesis/price/time):** print grades CLEAN un-masked (NCO down AND delinquency formation stable/down AND ACL flat/release on a stable book) → no transmission → NO trade. OR the stock already gapped to fair value on the print (no under-reaction left) → NO chase.
- **Kill line:** guidance affirmed improving + DQ formation stable + survivor-pool dynamics intact → consumer leg defers → no entry / exit.
- **Confirm line:** ≥2 un-mask tells on one name, OR the same tell synchronized across ≥2 monolines (synchronized = stronger) → enter / hold / consider the regional card (TRY-FIRE-002) as the follow-on.

══════════════════════════════════════════════════════════════
ZONE 2 — LIVE MARKS (fill ONLY this at fire — rule #4)
══════════════════════════════════════════════════════════════
- **Timestamp (ET):** ____
- **Trigger-level confirm:** `grade_print.py <COF|SYF|ALLY> --provision _ --nco _ --book-direction <shrinking|flat|growing> [--nco-guide raised] [--dq-formation rising] [--build-type specific|collective]` → **PATH(m)** verdict = ____ · un-mask tells ___/4 · then `grade_print.py --tally` → path (m) FIRES? (≥2 names, or 1 strong-single ≥2 tells). *(Monoline path-(m) tally is built into the grader as of 2026-06-27 — book-on-shrinking build / guide-raise / DQ-formation are the un-mask discriminators; headline NCO does NOT count.)*
- **Spot:** <NAME> $____ as-of ____ · `fetch.py price <NAME> --json` · print-reaction so far: ___% (under-reacted? Y/N)
- **Green/red day check (rule #6):** <NAME> today ___% → puts on green ✓ / breaking & why: ____
- **Chain marks:** `chain_fetch.py <NAME> <EXPIRY> --type put --no-cache`
  | Strike | Mark | Spread% | IV% (post-print crush?) | OI | Moneyness% |
  |---|---|---|---|---|---|
  | | | | | | |
- **Liquidity OK?** [spread/OI per chain flags — Y/N] · SYF/ALLY chains thinner than COF — check.
- **Broker position truth:** monolines NOT in the current FORGE book (verify) — net-new, no overlap expected. `[POSITION_STATE_UNKNOWN]` until confirmed.
- **Sizing:** `risk_calc.py --premium <mark> --max-loss 500` → ____ contracts

══════════════════════════════════════════════════════════════
ZONE 3 — TRIGGER CONFIRM + DECISION
══════════════════════════════════════════════════════════════
- [ ] Grade = UN-MASKED deterioration (≥2 tells / synchronized) — NOT headline-NCO, NOT growth-beta
- [ ] Name selected on cleanest un-mask + liquid chain · [ ] Under-reaction exists (not chasing a completed gap)
- [ ] Live marks < 15 min · [ ] Green/red OK · [ ] Liquidity OK · [ ] Max loss ≤ $500 · [ ] Position truth confirmed

**Terry verdict:** CLEAN / CONDITIONAL / NO TRADE
**Decision:**  [ ] APPROVE   [ ] REJECT   [ ] REWORK: ____

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**

---
*Grader: monoline un-mask tally is BUILT — `grade_config.json` path **m** (members SYF/COF/ALLY, need 2 or 1 strong-single) + `grade_print.py --book-direction/--nco-guide/--dq-formation` (selftest PASS, 2026-06-27). COF/SYF/ALLY now score as signal, not just regional-gate.*
