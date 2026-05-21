# BROCK Position Decisions — May 21 2026

**Context:** 20-day BROCK dark window (5/1 → 5/21). Will surfaced live Fidelity PDF; this memo formalizes per-position decisions against ground-truth marks. Supersedes TRADE.md Section 8 (May 1 framework, anchored to OBDC May 6 catalyst which has since resolved as MIXED).

**Per `feedback_exit_recommendations_need_mark_context.md`:** Every recommendation references the execution mark; close-now is only recommended where exit value exceeds the residual call-option-on-tail-event.

---

## Live state (5/21 ~10:30 ET)

| Tape | Level | Vs 5/1 STATUS | Read |
|---|---|---|---|
| APO | $132.65 | +1.1% | Sustained >$130 for 13+ sessions (entrenched since ~May 7) |
| ARES | $123.64 | +3.2% | Bull rally cooled; just under TRADE.md $125 EXIT line |
| OWL | $9.96 | +0.3% | Q1 fee-rally cracked & re-bounced |
| HY OAS | 286bps | +3bps | **Widening AWAY from 260 kill** — cushion 26bps (was 16-23) |
| CCC OAS | 948bps | +26bps | Quality bifurcation deepening |
| 10Y | 4.67% | +42bps over window | Duration channel widening (LIQUID's frame) |
| VIX | 17.54 | flat low | Complacency / gamma suppression continuing |
| FSK | $11.03 | post-Q1 | At KKR tender floor ($11) |

**Catalyst review since 5/1:**
- OBDC Q1 (5/6) = MIXED — did NOT re-arm bear, did NOT trigger TRADE.md 8A EXIT path
- FSK Q1 (5/11) = Strong Bear / data Max Bear (see `FSK_Q1_READ_MAY21.md`)
- APO $130 trigger fired ~5/7 and held

---

## Per-position decisions

### 1. APO Dec 18 $95P ×1 — **HOLD**

| Field | Value |
|---|---|
| Live mark | $2.75 / **$275 residual** |
| Cost basis | $11.85 / $1,184.67 |
| Drawdown | -77% |
| Days to expiry | ~210 |
| Spot vs strike | $132.65 vs $95 = 28% OTM |

**Decision:** HOLD. This is the thesis vehicle. 210 days = real runway. FSK Q1 Strong Bear + CCC bifurcation + duration channel widening = substance validating; HY OAS approaching 260 kill but resisting. Dec captures GCRED/OTF/BCRED/CTAC release window + any bank PC loss disclosure + any sponsor-bifurcation escalation.

**Conviction: 5/5** (unchanged). No re-action unless thesis-kill fires (HY OAS sub-260 sustained, or Fed emergency PC facility, or 2 consecutive Q PC default rate decline).

---

### 2. APO Jun 18 $100P ×1 — **LET EXPIRE**

| Field | Value |
|---|---|
| Live mark | $0.20 / **$20 residual** |
| Cost basis | $7.71 / $770.67 |
| Drawdown | -97% |
| Days to expiry | ~28 |
| Spot vs strike | $132.65 vs $100 = 25% OTM |

**Decision:** Let expire. Residual = $20. Sell-ticket cost likely eats it. No realistic ITM path — APO needs -25% in 28 days, ~2.5σ event. Asymmetry of the $20 residual on a tail-gap is *fine* but not actionable.

**Note:** TRADE.md 8A had EXIT-on-bullish-OBDC-and-APO-entrenched as the pre-set rule. OBDC was MIXED (neither clean bull nor clean bear), so the pre-set rule didn't cleanly fire. At today's mark the question is moot — $20 residual ≠ a tradable exit.

**Conviction: 1/5** — dead premium with a residual lottery ticket.

---

### 3. ARES Jun 18 $95P ×1 — **LET EXPIRE**

| Field | Value |
|---|---|
| Live mark | $0.25 / **$25 residual** |
| Cost basis | $8.03 / $802.67 |
| Drawdown | -97% |
| Days to expiry | ~28 |
| Spot vs strike | $123.64 vs $95 = 23% OTM |

**Decision:** Let expire. Same logic as APO Jun.

**Open question — ARES Q1 release status:** If ARES Q1 is still ahead in the 28-day window, the position holds an event-driven catalyst. If already printed (and benign), pure tail-risk lottery. **Verify on next session.** Doesn't change the let-expire posture (residual too small either way) but affects analytic read.

**Conviction: 1/5.**

---

### 4. OWL Jun 5 $9.5P ×2 — **HOLD**

| Field | Value |
|---|---|
| Live mark | $0.20 / **$40 residual** |
| Cost basis | $0.59 / $117.35 |
| Drawdown | -66% |
| Days to expiry | **~15** |
| Spot vs strike | $9.96 vs $9.50 = **5% OTM (near strike)** |

**Decision:** HOLD. This is the *actual* live lottery ticket in the BROCK book. Single 5% OWL move puts ITM. OWL's fee-rally narrative is cracking (DL -1.1%, net deployment -$0.5B, -4.4% off May 1 high before bounce). Real probability of ITM (not the 1-3% range of the deep-OTM Jun strikes) — order of 10-20% on a vol expansion or any OBDC-related news flow.

**Note:** Not in TRADE.md — re-entered after Apr 18 expiry. Need to add to formal position tracker.

**Conviction: 2/5** for the position economically; 3/5 for the asymmetric residual. Don't touch through expiry.

---

### 5. HYG Jun 18 $75P ×8 — **LET EXPIRE**

| Field | Value |
|---|---|
| Live mark | $0.05 / **$40 residual** |
| Cost basis | $0.31 / $245.39 |
| Drawdown | -84% |
| Days to expiry | ~28 |
| Spot vs strike | HYG far above $75 |

**Decision:** Let expire. May 1 plan to roll Jun→Dec was correct framework but execution didn't happen during the BROCK dark window. Window has closed — at $0.05 mid, the roll math no longer works (selling $0.05 to fund a Dec strike loses ~all premium). HY OAS at 286 and widening = no near-term spread blowout to drive HYG below $75.

**Lesson for future:** Roll decisions need either explicit Will execution or an agent-authorized rail. May 1 → 5/21 had no mechanism to act on a roll plan, so it didn't execute. Flag to Prome.

**Conviction: 1/5** — dead premium.

---

## Net portfolio posture (BROCK-domain)

| Slice | Action |
|---|---|
| Thesis vehicle | APO Dec $95P — hold, untouched |
| Dead June premium | APO Jun + ARES Jun + HYG Jun — let expire, ~$85 cumulative residual, not worth sell tickets |
| Live lottery | OWL Jun 5 $9.5P ×2 — hold, 15d near-strike |
| Fresh exposure | **None added** — see FSK_Q1_READ_MAY21.md "Fresh premium" section |

**Cumulative BROCK book current value: ~$400 against $3,120 cost basis (~13% remaining).** Position weight is small in account context; the Dec $95P is the only position carrying real optionality.

---

## Trigger ladder (drop everything if any fires)

| Trigger | Live state (5/21) | Action |
|---|---|---|
| HY OAS <270 sustained 2+ sessions OR <260 intraday once | 286, widening | Pre-write thesis-kill memo; if breach + BDC marks worsening = trap-clinching → soft-kill discrimination required |
| Arms-length sub-90¢ BDC loan transaction | Not seen | BRK-25 Stage 3 catalyst; open BIZD Sep $12P |
| First SEC enforcement filing | Probe active, no filings | BRK-26 Stage 3 catalyst; open BIZD basket more aggressively |
| Major BDC Q1 10-Q markdown >5% | FSK fired (Strong Bear), GCRED/OTF/BCRED/CTAC pending | BRK-27; open vehicle-specific or BIZD per liquidity |
| KKR adds to FSK support package within 90d | KKR initial package 5/11 | Bear signal upgraded; open BDC basket aggressively |
| BCRED Q2 redemption refused / sponsor backstop refused | Q2 print TBD | 🔴🔴 gate cascade; open BX puts (REGINALD cross-flag) + BIZD basket |
| Bank PC loss disclosure (JPM/BAC/Citi/WFC NDFI detail) | WALTER REQ 5-cat schema pending pull | Bank transmission live; cross-flag REGINALD |

---

## Decision summary for Will / Prome

**Will tomorrow / next week:** Do nothing on existing BROCK positions except possibly close OWL Jun 5 if it rips ITM in the 15-day window. Most positions are at residual values where ticket costs exceed recoverable premium.

**No fresh BROCK premium recommended.** HY OAS widening + VIX low + FSK already-priced + GCRED/OTF/BCRED/CTAC dates unconfirmed = no clean entry. Conditions to enter laid out above.

**Open items requiring next-session work:**
1. Confirm GCRED/OTF/BCRED/CTAC release dates (pre-build OTF first — highest software concentration)
2. Confirm ARES Q1 release status
3. Pull WALTER NDFI May 15 CDR Q1 5-cat bulk release
4. Integrate STATUS_DRAFT into live STATUS.md (currently 20-day stale)
5. OWL Jun 5 position not in TRADE.md — add to formal tracker

---

*BROCK file. Position data sourced from Fidelity Portfolio Positions PDF (5/21 10:25 ET) cross-checked against TRADE.md Section 8 framework. Authored 2026-05-21 by BROCK.*
