# Pre-Auction Baseline — 5/21 10Y Reopening (1pm ET)

**Author:** BOND (Claude Code, Prome-spawned)
**Staged:** 2026-05-21 ~12:27pm ET
**Mode:** DRAFT — no edits to live STATUS / AUCTION_HEALTH / TRADE.md. Post-auction respawn (~2pm) integrates the verdict.
**Auction:** 10Y reopening, 9Y 8M, $42B (5th consecutive 10Y reopen to watch; cusip from TreasuryDirect at 1pm).
**Decision driven:** Dual-grade verdict (v1 + v2) → mechanically resolves matrix Q4 (v2 deployment timing) AND tests VIOLET R11 substance-side trigger #6 (10Y > 4.75%).

---

## 1. Live Tape (as of ~12:25pm ET)

| Metric | Value | Δ vs prev close | Source / Time |
|---|---:|---:|---|
| **10Y yield (^TNX)** | **4.599%** | -7bp vs 5/20 close 4.572%... see range below | yfinance intraday 11:05am |
| 10Y intraday range 5/21 | 4.599 – 4.635 | — | yfinance 15m |
| 10Y 5d trajectory | 4.595 → 4.623 → 4.667 → 4.572 → 4.599 (5/15→5/21) | -2.4bp w/w net (peak 4.687 on 5/19) | yfinance daily |
| 30Y yield (^TYX) | 5.123% | +0.7bp vs 5/20 close 5.116% | yfinance 11:05am |
| 5Y yield (^FVX) | 4.271% | +4.6bp vs 5/20 close 4.225% | yfinance |
| **MOVE index** | **81.53** | **-3.79 vs 5/20 (85.32)** | yfinance 5/20 close (5/21 not yet published) |
| **TLT** | **$83.74** | -$0.17 vs 5/20 close $83.91 | yfinance 12:00pm |
| VIX | 17.20 | -0.25 vs 5/20 close 17.44 | yfinance 11:00am |
| **DXY (DX-Y.NYB)** | **99.43** | **+0.32 vs 5/20 (99.11)** | yfinance |
| **USD/JPY** | **159.18** | **+0.14 vs 5/20 (159.04)** — above 159 | yfinance |
| **Brent (BZ=F)** | **$107.01** | **+$1.99 vs 5/20 ($105.02)** | yfinance |
| HYG | $79.69 | -$0.17 vs 5/20 | yfinance |
| JNK | $95.95 | -$0.18 vs 5/20 | yfinance |

**Curve snapshot (rough):**
- 2Y proxy not clean from yfinance (^IRX is 13wk T-bill, current ~3.57); use SHY 5d for 2Y direction (slight bid: $82.15→$82.08).
- 5Y30Y spread ≈ 5.123 - 4.271 = **85bp** (steeper today: 5Y -4.6bp move bull-flattens front; 30Y essentially unchanged)
- 5Y10Y ≈ 4.599 - 4.271 = 33bp
- 10Y30Y ≈ 5.123 - 4.599 = 52bp

**WI indication for 1pm 10Y:** Per WI Sourcing Playbook §5 — pre-1pm WI is structurally unobtainable without terminal. CME 10Y futures (ZN) front-month implied yield is the directional anchor only; current 10Y cash at 4.599-4.617% intraday range implies WI likely in 4.60-4.62% zone. **Treat as directional, not WI tick.** InvestingLive primary post-1pm (1:05pm refresh start), ZH cross-check by 1:45pm.

---

## 2. Pre-bias check — what happened since 5/20 close

**Risk-on flavor in vol, but macro co-pressure re-firing:**
- MOVE -3.79 (rates vol softer) and VIX -0.25 — pre-auction calm consistent with last-night-of-month flow + relief carry-through from 5/20 20Y clean print.
- **DXY +0.32 and USD/JPY 159.18** — JPY back above 159 for first time this week; modest USD strength re-engaging.
- **Brent +$1.99 to $107** — geopolitical/inventory shock-style move (HAWK domain; BOND notes the macro co-pressure has re-engaged after softening 5/19→5/20).
- TLT -$0.17 — modest give-back of yesterday's relief bid; not capitulation.
- 10Y intraday: opened 4.609, peaked 4.635 ~9:35am, drifted to 4.599 by 11:05am — buy-the-rumor-of-clean-print, sell-the-news? Or auction concession not yet in?

**Net pre-bias read (CORRECTED 12:40pm per Will):** The setup is being held into **constructively-shifted sentiment, NOT building concession**. Trajectory:
- 5/19 10Y intraday high 4.687%
- 5/20 rally — TLT closed $83.91 (the relief bid)
- 5/21 12:25pm 10Y 4.60%, TLT $83.74 — *modest give-back* of the rally, but rally is still the dominant move-of-the-week

The Brent +$1.99 / DXY +0.32 / JPY 159 micro-pressures sit on top of a fundamentally constructive bond backdrop (vol soft, TLT held the rally, 10Y well off 5/19's 4.687 peak). This is **NOT a concession-building day**; it is a held-rally day with mild micro-headwinds.

**No Fed-speak or major data surprise flagged in the last 24h that pre-biases the auction directionally.** Brent move is the most notable non-Fed catalyst — feeds inflation-expectations / term-premium concern, but does not overturn the constructive-backdrop frame.

---

### 2a. SENTIMENT-CONTEXT GRADING LENS (apply at 2pm verdict — Will's frame, MANDATORY annotation)

The matrix (v1 and v2) is statistics-based and indifferent to pre-auction sentiment trajectory. Keep the matrix arithmetic clean. **But the verdict-interpretation layer MUST annotate the sentiment context at print.**

| Auction outcome | Backdrop | Bear/bull weight on the same matrix score |
|---|---|---|
| **Weak print** (v1 or v2 fire) | **Held-rally / constructive sentiment** ← TODAY | **STRONGER bear signal.** Real-money is fading the favorable backdrop. Matrix fire is **upweighted** in verdict commentary. |
| Weak print | Building concession (yields rising into print) | Weaker bear signal at same matrix score. Mechanically priced; fire less surprising. |
| Clean print | Held-rally / constructive sentiment | Modest bull signal (consistent with backdrop; not a strong demand-confirmation surprise). |
| Clean print | Building concession | **STRONGER bull signal.** Demand showed up despite concession. (This was the 5/20 20Y setup post-hoc.) |

**Today's row 1 applies.** A v2 fire today on **any** path (BTC<2.30, I'<52.0% of-offering alone, T' tail ≥+2.9bp proxy, or 2-of-3 of {B', I', T'}) carries MORE weight than the same fire on a concession-building day. The verdict should say so explicitly — not as a separate score, but as an annotation alongside the v1/v2 grid.

**Verdict-template addition (for 2pm respawn output, alongside §3c):**
```
Sentiment context at print: HELD-RALLY (5/19 4.687 → 5/20 rally → 5/21 modest give-back; TLT $83.91→$83.74; 10Y 4.687→4.60).
Weight on matrix verdict: [if fire] UPWEIGHTED bear signal — real-money fading constructive backdrop.
                         [if clean] consistent-with-backdrop bull signal — not a strong demand surprise.
```

**Operational consequence for sizing:** under v2 §5 confidence-stepped sizing, an "I' marginal" fire (indirect 50.5-52.0% of-offering) defaults to half-add. If the sentiment context is held-rally (today), BOND should flag in the recap that **the half-add tier may be under-sizing the genuine signal** — and surface to Will for an upsize decision rather than executing the half-add silently. Matrix budget stays bounded at 2 contracts; question is how aggressively to deploy within bound.

**Symmetric note:** a clean print today is also less informative than a clean print into concession. The 5/20 20Y clean print INTO concession was strong evidence; a 5/21 10Y clean print INTO held-rally is consistent-with-backdrop and does NOT materially update the demand-hole base rate further. Posterior stays ~20-25% on the next observable auction; clean-into-rally doesn't drive it lower the way clean-into-concession did.

---

## 3. Dual-Grade Comparison Framework (1pm-ready)

**Auction parameters:**
- 10Y reopening 9Y 8M, $42B (matching 5/12 10Y new-issue size pattern; reopen mechanics not new-issue)
- Auction time: 1:00pm ET
- Results publish: TreasuryDirect ~1:01-1:03pm; WI confirmation via InvestingLive ~1:05-1:20pm; ZH cross-check by 1:45pm

### 3a. v1 Read (CURRENT live matrix)

| Criterion | Threshold | Reading template |
|---|---|---|
| BTC | < 2.30 | ✓ / ✗ |
| Dealer | > 12% | ✓ / ✗ |
| Indirect (of-offering) | < 55% | ✓ / ✗ |
| Tail (absolute) | > 2bps | ✓ / ✗ (informational; tail not in v1 combinator) |
| **2-of-3 fire? (B, D, I)** | — | **YES / NO** |

### 3b. v2 Read (DRAFT proposal, rule (c) locked per MATRIX_V2_DRAFT)

**Operative thresholds for 10Y, trailing-12mo:**
- B' (BTC) < 2.30
- I' (indirect_pct of-offering) **< 52.0%** (10Y trailing-12mo 15th-pctile snapshot, per MATRIX_V2 §3d)
- T' (tail) **≥ +2.9bps** on `tail_vs_cmt_bps` proxy (10Y trailing-12mo 75th-pctile per v2 README §3); prefer ZH-quoted true tail when available

| Criterion | Threshold | Reading template |
|---|---|---|
| B' (BTC < 2.30) | < 2.30 | ✓ / ✗ |
| **I' (indirect of-offering < 52.0%)** | < 52.0% | ✓ / ✗ (compute via headline indirect_bidder_accepted / offering_amount; ZH typically gives competitive%, convert: indirect_competitive% × ~0.86 ≈ of-offering for 10Y reopens, but COMPUTE FROM TREASURYDIRECT once published) |
| T' (tail ≥ 75th pctile-of-10Y-12mo, ~2.9bps proxy / use ZH true tail) | ≥ +2.9bps proxy OR ZH-confirmed strong tail | ✓ / ✗ |
| **I' alone fires?** | — | **YES / NO** (I' alone is single-criterion sufficient under v2) |
| **2-of-3 of {B', I', T'}?** | — | **YES / NO** |

### 3c. Cross-Grade Verdict Template (for 2pm respawn)

```
v1 fires: YES/NO
v2 fires: YES/NO
Q4 branch resolved: deploy-this-week / deploy-this-week / deploy-next-week-Tue-Thu
```

Per MATRIX_V2 §8 Q4 conditional rule:
- v2 fires today → deploy v2 this week (reconcile fast)
- v1 fires but v2 doesn't → deploy v2 this week (v1 false-positive is worst case)
- Neither fires → deploy in next week's quiet window (Tue-Thu)

**TLT-puts action under v2 (per §5 confidence-stepped table):**
| Print | Action |
|---|---|
| No v2 fire | Hold. No add. |
| 2-of-3 fire | Half-add (1 contract Aug 15 $83P) |
| I' alone, marginal (indirect 10-15th pctile, i.e., ~50.5%-52.0% of-offering) | Half-add |
| I' alone, decisive (indirect <10th pctile, ~<50.5% of-offering) | Full add (2 contracts) |
| 3-of-3 fire | Full add (2) + Will-touch ad-hoc prompt for 3rd contract |

### 3d. Dual-display indirect — capture BOTH numbers in recap

Per MATRIX_V2 §3d dual-display rule:
- `indirect_pct_of_offering` = indirect_bidder_accepted / offering_amount (V2 trigger arithmetic)
- `indirect_pct_of_competitive` = indirect / (indirect + direct + dealer) (ZH/recap convention)

Both numbers go in the post-auction commentary. Trigger uses of-offering only.

---

## 4. 5/12 10Y Benchmark Context (prior 10Y print, useful prior)

Per BOND STATUS Latest Auction Read:
- 5/12 10Y new issue $42B: BTC 2.40, high yield 4.468%, indirect 64.0% (competitive convention — ZH/STATUS), direct 24.1%, dealer 12.0%, tail +0.4bp

**Under v2 dataset (per MATRIX_V2 §6 5/12 10Y re-grade):**
- BTC 2.40: NOT B' (>2.30)
- indirect_pct (of-offering) = **51.5%** → I' FIRES (below 52.0% threshold; 18.2nd pctile of 12mo window; 10th pctile of full prior history)
- tail_vs_cmt_bps proxy ~+1bp, ZH true tail +0.4bp: NOT T' (10Y 75th-pctile is +2.9bps proxy)
- **v2 verdict: ORANGE FIRES (I' alone, 0.5pp margin → marginal-I' classification → half-add tier under §5)**
- v1 verdict: yellow / no-fire under live matrix

**Today's 10Y reopening is a 5th-consecutive-10Y-tail-streak setup.** If 5/12 fired v2 with 0.5pp margin on indirect, the 5/21 reopen pricing into roughly the same yield level (4.60% vs 4.468% on 5/12 — 13bp higher absolute yield, structurally MORE concession than 5/12) sets up:
- If indirect mix today ≥ 52.0%-of-offering → v2 does NOT fire on I'. Foreign-demand thesis weak; combine with 5/20 20Y clean → demand-hole narrative further deteriorated.
- If indirect mix today < 52.0% → v2 fires I'. Confirms 5/12 wasn't a one-off; foreign-bid degradation is sequential at the 10Y reopen.
- Edge case: if indirect is exactly in 50.5-52.0% range → marginal-I' → half-add. If <50.5% → decisive → full-add.

**Posterior base-rate from 5/20 respawn:** ~20-25% for Leg 2 firing (down from prior 35-40%). Today's pre-auction tape mildly supports the lower base rate (vol soft, no panic), but Brent re-firing + DXY/JPY mild USD strength prevents pushing the prior lower than ~20%.

---

## 5. R11 Substance-Side Trigger #6 (NEW — per VIOLET Stage 3 matrix)

**Trigger:** 10Y > 4.75%.
**Current:** 10Y 4.599% — **15.1bp from trigger** (boot prompt said 8bp; tape has moved; current gap wider).
**Distance:** 10Y must move +15bp from current intraday level to arm trigger #6. From yesterday's session high (4.687), only 6bp away.

**Auction scenarios for R11 trigger:**
- Hard tail (>+3bp tail, e.g., 4.63%+ high yield): pushes 10Y secondary toward 4.65-4.70% session high; gap to 4.75% closes to ~5-10bp but does NOT arm trigger #6 directly on the print.
- Catastrophic tail (>+5bp + weak indirect): could drive secondary above 4.70%, possibly probing 4.75% intraday over next 24-48h.
- Clean print: 10Y likely settles 4.55-4.62%; gap to 4.75% widens; trigger #6 dormant.

**Key BOND-to-VIOLET note:** Even if 10Y closes 4.75% today (very unlikely absent catastrophic tail), R11 substance trigger #6 ALONE does not confirm Stage 3 — R11 requires 2 of 3 surface-side triggers (VVIX>105, VIX9D>VIX, SKEW>145) same week + 1 of 3 substance triggers same week. With VIX 17.20 and softening, the surface-side gate looks unlikely to fire this week. Substance trigger #6 firing today would arm, not confirm.

---

## 6. Open Holds (per Prome boot prompt)

- No fresh position recommendations without Will.
- DRAFT mode for tape pull — no edits to live STATUS / AUCTION_HEALTH / TRADE.md.
- Post-auction respawn at ~2pm does the live update with dual-grade verdict.
- Commit scope: only AGENTS/BOND/. No `git add -A`.

---

## 7. Ready for Respawn

This document is the pre-auction baseline. Post-auction (~2pm), BOND respawn:
1. Pull TreasuryDirect press release at 1:01pm → capture BTC, high yield, indirect/direct/dealer pcts (both conventions).
2. Pull InvestingLive WI bullet 1:05-1:20pm → compute tail = awarded high - WI.
3. ZH cross-check by 1:45pm.
4. Fill v1 and v2 grids in §3a / §3b.
5. Emit cross-grade verdict line per §3c template.
6. Update STATUS / AUCTION_HEALTH / TRADE.md with verdict.
7. Outbox to PROME with dual-grade result + Q4 branch resolution.

---

*Author: BOND, Claude Code surface, Prome-spawned 2026-05-21 ~12:25pm ET*
