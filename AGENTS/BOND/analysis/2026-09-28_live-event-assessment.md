# BOND — Live-event assessment, 2026-09-28 (global long-end sell-off, 4th session)

**Written:** 2026-09-28 ~12:0x ET, BOND, Will-directed ("finish this live-event read with one short assessment using the evidence already collected"). **Inputs:** evidence already collected this session (`KB-BND-340/341`) **plus one new pull, disclosed:** ICE BofA **single-B** OAS (`BAMLH0A2HYB`) and BBB (`BAMLC0A4CBBB`), because the question asks for B and it had not been pulled. All spreads come from FRED as fetched 9/28 ~11:5x ET (span 2023-09-29 → 2026-09-25, n=785). Official curve = U.S. Treasury par/real CSV (the H.15 source). Today's (9/28) rates are **vendor intraday, not official**, and nominal only.

---

## 1. What is driving the rise in yields

**Observed decomposition, 10Y, 9/22 → 9/25 (official):**

| Leg | 9/22 | 9/25 | Change | Source |
|---|---:|---:|---:|---|
| 10Y nominal | 4.96 | 5.17 | **+21bp** | Treasury par curve |
| 10Y real (DFII10) | 2.63 | 2.83 | **+20bp** | FRED 9/22 · Treasury real curve 9/25 |
| 10Y inflation compensation (T10YIE) | 2.33 | 2.34 | **+1bp** | FRED |
| 5y5y forward inflation (T5YIFR) | 2.34 | 2.34 | **0** | FRED |
| 2Y nominal (expected-policy proxy) | 4.71 | 4.81 | **+10bp** (peak 4.87 [9/24], +16) | Treasury |
| 1y1y (2×2Y−1Y par approx) | 4.99 | ≈5.12 | **+13bp** (peak 5.23 [9/24], +24) | BOND computation |
| 30Y nominal | 5.29 | 5.49 | **+20bp** | Treasury |

**By day:**

| Day | 10Y | Real | Infl. comp. | 2Y | Reading |
|---|---:|---:|---:|---:|---|
| 9/23 (hot PMI) | +15 | +13 | +2 | +14 | policy path **and** real, whole curve |
| 9/24 | +7 | +9 | −2 | +2 | real, long-end |
| 9/25 | −1 | −2 | +1 | **−6** | **long end up (30Y +2) while front rallied** |
| 9/28 intraday (vendor) | +5 | n/a | n/a | n/a | 5Y +5.6 · 10Y +5.0 · 30Y +4.7 — parallel; no decomposition until the official cells |

**Assessment:**
- **Observed: the rise is a real-yield rise.** Twenty of the 10Y's 21bp came through real yields. Inflation compensation was flat, and so was long-run expected inflation (5y5y). **The widely reported driver, oil reviving inflation fears (TE 9/28, secondary), does not show up in breakevens through 9/25.** If oil matters, it is working through expected Fed policy, not long-run inflation pricing.
- **Observed: expected policy rates rose, then stopped.** 2Y +16 and 1y1y +24 into 9/24 (1y1y at a 2023-forward high). Then Friday gave back part of it (2Y −6), and October-hike odds eased from ~70% (TE 9/24) to ~65% (TE 9/28), both secondary. **So the move through 9/24 was substantially policy-path; the move since has not been.**
- **Inference, not measured: term premium.** The 9/25 shape (front rallies, long end rises, inflation compensation flat) and the 2s30s steepening (58 → 68bp) are *what a rising term premium would look like*. **No model reading covers 9/24–9/28.** The last BOND/HENRY evidence cuts both ways. Under ACM, 9/15→9/23 was path, not premium (TP −6.4bp while 10Y +11; `KB-BND-325`). But 9/22→9/23 alone was TP +7.0 of +15 (`KB-BND-332`), and ACM and KW disagree by 6.9bp on their only shared window. **Label any "term premium is driving it" claim for 9/24 onward as INFERENCE.** FORUM-7 P2 (KW, HENRY's lead) is the pre-registered test.
- **Global:** today's 10Y moves are Anglo-sphere-led (UK +5.9, Canada +6.2, Australia +4.8, US +5 vendor), with core euro and Japan +1–4bp (TE intraday, secondary). **Whether the US is importing or exporting the move is not established** (see §4).

## 2. How far credit stress has spread

| Tier | 9/22 | 9/25 | 3-session Δ | Share of 782 3-session windows with a change at least this large (bp · %) | Level percentile (span) |
|---|---:|---:|---:|---|---:|
| **CCC** | 1075 | **1128** | **+53bp (+4.9%)** | 17 (2.2%) · 27 (3.5%) | **100th** (2026 high; span max 1137 [2025-04-07]) |
| **B** | 271 | **300** | **+29bp (+10.7%)** | 24 (3.1%) · **15 (1.9%)** | 44th |
| **BB** | 156 | **176** | **+20bp (+12.8%)** | 26 (3.3%) · **14 (1.8%)** | 39th |
| HY index | 268 | 293 | +25bp (+9.3%) | 23 (2.9%) · 17 (2.2%) | 43rd |
| **IG** | 77 | **81** | **+4bp (+5.2%)** | 56 (7.2%) · 31 (4.0%) | 39th |
| BBB | 95 | 99 | +4bp (+4.2%) | 68 (8.7%) · 41 (5.2%) | 23rd |

15-session changes (LIQUID's Q2/Q4 letters use this window): CCC +74 · **B +23** · **BB +21** · BBB 0 · IG 0 [9/25]. B was +2 on 9/23, +10 on 9/24 and +23 on 9/25. CCC/BB ratio **6.89 → 6.41** (the tail's lead compressed). 20-session real-yield beta, through 9/24 (BOND's D7 leg): CCC +0.71 (84th pct) · **B +0.14 (72nd; median −0.16)** · BB −0.04 · IG −0.01.

**Assessment:**
- **"Weakest borrowers only" no longer describes the last three sessions.** Proportionally, **BB and single-B widened fastest** (≈ top 2% of 3-session windows), faster than CCC. **B's 15-session change crossed its +9bp p75 on 9/24 (+10) and reached +23 on 9/25.** By LIQUID's registered definition, that is the day the "isolated-CCC" condition stopped holding. B's 20-session sensitivity to real yields rose from +0.03 (BOND's 9/25 D7 read) to +0.14; it is still modest.
- **But it has spread through high yield, not beyond it, and only in speed, not in level.** Investment grade and BBB are +4bp, with 15-session changes of 0. Outside CCC, levels are ordinary (~40th percentile of a 3-year span that is itself a tight-spread era).
- **Formal grades are LIQUID's** (L477 Q4 lead; D1–D5 theirs, D6–D8 BOND-supplied). **BOND grades nothing here.** The facts above went to LIQUID for their letters (`AGENTS/LIQUID/inbox/2026-09-28_from-BOND_credit-tier-facts-for-Q4-grade.md`). On LIQUID's letter, the decisive **D1 (B 15-session ≥ +28bp on 3 consecutive obs with CCC widening) is NOT met** (+23, zero qualifying obs). Its companion legs: BB ≥ +19 met on 9/25; BBB ≥ +7 and IG ≥ +6 not met.
- **Next observations that would change this judgment:**
  - **(i)** B's 15-session change reaching ≥ +28 on the 9/28–9/30 cells. Three in a row would be LIQUID's D1, with the verdict around 10/1.
  - **(ii)** IG/BBB joining: IG 15-session ≥ +6 or BBB ≥ +7 (LIQUID's D1 companion legs). That would mean the move has left high yield.
  - **(iii)** The HY index closing >300 on the 9/28 cell (~9/29). That is BOND's matrix row-4 letter (with velocity).
  - **(iv)** The **10/1 FR2004 below-IG dealer inventory** (D6): whether dealers are warehousing HY paper.
  - **What would reverse it:** B falling back below +9 on the 15-session window while CCC keeps widening. That returns to (A).

## 3. What changes for the thesis

| | Status | Evidence |
|---|---|---|
| **Real-rate / higher-for-longer regime** | **SUPPORTED, strengthened** | 10Y rise ≈ all real (+20 of +21); DFII10 ≥2.50 for 11 consecutive FRED closes (WQ-246 sustain count MET); 30Y three straight fresh 2026 highs (5.49); policy path repriced to a 2023-forward high (1y1y 5.23 [9/24]) |
| **Auction demand hole (the mechanism the kill tests)** | **UNCONFIRMED, not strengthened** | The 9/23 5Y strict-test failure still has no mechanism leg: funding calm (SOFR−IORB 0bp [9/25]; LIQUID found NONE); dealer leg unreadable until 10/1. "Expensive, not broken" remains the better-supported description of auctions |
| **Credit "tail-only" dispersion (9/14 read, `KB-BND-277`)** | **WEAKENED** | CCC 1100 fired (`BND-27` FALSE), and B/BB now widen faster proportionally; still no IG participation |
| **This desk's forecasting on the stress side** | **WEAKENED** | Two consecutive misses, `BND-26` (70%) and `BND-27` (65%), **both under-called the move this desk's own thesis predicts**. Calibration, not direction |

**Why the score stays 14/35:** each matrix row moves only on its pre-registered letter, and none fired.
- **Row 1 (long end, 4):** ⇒5 needs a composition failure at a long-end auction (next: 10/7 10Y-R, 10/8 30Y-R) or the paired kill's mechanism leg. Fresh highs are not the letter.
- **Row 2 (auctions, 3):** ⇒4 needs a composition failure with the funding/FR2004 leg confirmed.
- **Row 3 (dealers, 2):** needs two consecutive FR2004 builds with weak composition, or SOFR−IORB positive. It is 0bp.
- **Row 4 (HY function, 2):** needs HY >300 with velocity. Velocity is present; the level is 7bp short (293). `VX-BND-11` moved 3→4 beneath the row, but that does not move the row.
- Raising a score on judgment while the letters are unmet is exactly what pre-registration exists to prevent.

**Thesis evidence ≠ trade authorization.** Both TLT add-gates read through on their letters (DFII10 sustain MET; OLD-conjunctive re-arm 9/23). **Neither is an add:**
- **Will's rulings stand unchanged:** TLT Sep-30 77P ×20 **hold to expiry**, **NO-ADD** (7/16), **WQ-280 add declined** (9/24), root rule #5.
- A stronger regime read is evidence for the thesis. It is not a card.
- **The 10/1 dealer test arrives AFTER the 9/30 option expiry.** It cannot inform the expiring position. Any consequence of a MET is a **recommendation for a future card**, through TERRY's card and Will's [Approve].

## 4. Separately — genuinely new research need (not started, not in this read)

- **Cross-market attribution of the 9/22→9/28 move:** is the US long end importing the sell-off (gilts / ACGBs / JGBs), exporting it, or moving on a shared driver? Today's pattern (Anglo-sphere +5–7, core euro/Japan +1–4) cannot say which, and it bears directly on the inference in §1. This crosses BOND (UST), HANS (EU/UK) and SAM (JGB/FX), so **owner and scope are PROME's call**; BOND has not started it.
- *(Not new, still open: HY primary-market / refi-wall data remains a fleet gap (L477 Q4 D8); the term-premium measurement for 9/24 onward is already FORUM-7 P2, HENRY's lead.)*
