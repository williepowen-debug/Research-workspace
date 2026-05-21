# Escalation Matrix v2 — DRAFT for Will/Prome review

## PROVENANCE

- **Author:** BOND, respawned 2026-05-20 PM ET at Prome's request.
- **Status:** DRAFT proposal. Live `monitors/AUCTION_HEALTH.md` and `STATUS.md` UNCHANGED. No commit. No push.
- **Inputs:**
  - `AGENTS/BOND/analysis/ESCALATION_MATRIX_BACKTEST_prome-spawned.md` (323 coupon auctions, 2023-01 → 2026-05, TLT 5d outcomes)
  - `AGENTS/BOND/analysis/CROSS_TENOR_BASE_RATES_prome-spawned.md` (444 same-week auction pairs)
  - `AGENTS/BOND/data/AUCTION_HISTORY_README_prome-spawned.md` (v2 schema with `tail_vs_cmt_bps`, dual indirect convention)
- **Review path:** Will + Prome read this file → approve / amend / reject → BOND executes implementation plan in §9 on next live session.

---

## 1. Verdict-first executive summary

The current v1 matrix (BTC<2.30, tail>2bps, dealer>12%, indirect<55%, fire on 2-of-3 of {B,D,I}) is **anti-signal at backtest**: fires under-perform base rate by 16.5pp on hit rate (19.2% vs 35.7%) and have a *positive* median 5d TLT return (+0.17% vs −0.19% base). The dealer>12% criterion is the principal corruptor — it is at-median and **wrong-signed at higher cuts** (dealer>20% median TLT 5d = +1.45%, contrarian-bullish).

**Headline proposal:**
- **Keep BTC<2.30** as confirmatory only (low-N, directionally correct).
- **Reformulate tail** to percentile terms (≥75th-pctile per-tenor) rather than absolute >2bps.
- **Drop dealer>12% as a bearish trigger**; retain dealer >18% as a *contrarian-bullish* note (NOT for TLT-put escalation).
- **Indirect rule LOCKED to per-tenor percentile (rule (c))**: `indirect_pct` (of-offering) < 15th-pctile of trailing-12mo prior prints in same tenor. The single best signal in backtest (indirect<50% v1: N=18, hit 50%, median −1.07%), normalized per-tenor so long-end outliers (e.g., 5/12 10Y at 51.5%) aren't missed by a flat threshold.
- Combinator: **2-of-3 of {B', I', T'}**, with **I' alone sufficient** to fire orange. Quarterly snapshot table in `monitors/AUCTION_HEALTH.md` is the audit rail for the moving percentile threshold.

**TLT-puts impact:** orange triggers become rarer but materially more selective; we replace the current ~once-every-12-auctions noisy fire with a ~once-every-25-auctions high-conviction fire. Conditional-add logic gets a confidence-stepped overlay (§6).

*(199 words)*

---

## 2. v1 vs v2 side-by-side

| Criterion | v1 (current) | v2 (proposed) | Evidence |
|---|---|---|---|
| BTC | < 2.30 | < 2.30 (confirmatory only; cannot fire alone) | Backtest: N=9 fires, hit 22.2%, median −0.67%. Directionally right, low N. |
| Tail | > 2bps absolute | ≥ 75th-pctile per-tenor on `tail_vs_cmt_bps` (proxy) | Per-tenor 75th-pctile values diverge widely (30Y: +1.6bps; 2Y: +4.4bps). Absolute 2bps fires almost always on 2Y/3Y, almost never on 30Y. Percentile normalizes. |
| Dealer | > 12% | DROP as bearish; retain dealer >18% as **contrarian-bullish note** (not a TLT-put trigger) | Backtest: dealer>12% hit 32.9% (= base rate); dealer>15% median +0.39%; dealer>20% median +1.45%. Wrong-signed at every threshold above noise. |
| Indirect | < 55% (denominator: of offering_amt) | **`indirect_pct` (of-offering) < 15th-pctile of trailing-12mo prior prints in same tenor** | Backtest's best single signal was indirect<50% (of-offering, v1 convention): N=18, hit 50%, median −1.07%. Per-tenor percentile (rule (c)) normalizes across tenor baselines and catches 5/12-style outliers that any flat threshold misses. Dual indirect numbers still **displayed** in commentary (recap-matching is a separate concern from trigger arithmetic). |
| Combinator | 2-of-3 of {B, D, I} (tail not in combinator) | 2-of-3 of {B', I', T'}; **I' alone is sufficient** (i.e., indirect <15th-pctile-of-tenor-12mo fires orange standalone) | Drops the wrong-signed driver; promotes the best single signal. |

---

## 3. Per-criterion reasoning

### 3a. BTC < 2.30 — KEEP as confirmatory

Backtest result is directionally correct but low-N: N=9, hit 22.2%, median 5d −0.67%. v2 dataset confirms BTC<2.30 is a left-tail event (the 5/13 30Y at BTC 2.30 was the 11th percentile of all 30Y prints since 2023). The signal is real but doesn't beat base rate cleanly on its own.

**Decision:** Keep as a confirmatory leg, not a standalone trigger. BTC<2.30 alone should not fire orange; it must coincide with at least one of {I' (per-tenor 15th-pctile of-offering), T'≥75th-pctile-per-tenor-tail}.

### 3b. Tail > 2bps — REFORMULATE to per-tenor percentile

v1 was not testable in backtest (no tail column). v2 dataset now has `tail_vs_cmt_bps` proxy. The per-tenor distribution (v2 README §3):

| tenor | 75th pctile tail | absolute 2bps maps to ~ |
|---|---|---|
| 2Y | +4.4bps | 30th pctile (very common) |
| 3Y | +3.9bps | 40th pctile |
| 5Y | +2.4bps | 70th pctile |
| 7Y | +2.2bps | 70th pctile |
| 10Y | +2.9bps | 70th pctile |
| 20Y | +2.0bps | 75th pctile |
| 30Y | +1.6bps | 80th pctile |

An absolute >2bps threshold fires very differently across tenors. **Reformulate as ≥75th-pctile per-tenor** so a 30Y tail of +1.7bps is correctly flagged as elevated while a 2Y tail of +2.1bps is correctly NOT flagged (it's below-median for the tenor).

**Caveat:** `tail_vs_cmt_bps` is a CMT-proxy, not true WI tail; v2 README warns of 1–5bp noise per-auction. The percentile-rank framing partially absorbs that noise (it's mean-zero across the time series) but single-auction calls remain noisy. **Confidence: medium.** When BOND reads ZH-quoted true tails (e.g., the +1bp 20Y 5/20), prefer those over the proxy; the proxy is the systematic distribution layer, not the realtime classifier.

### 3c. Dealer > 12% — DROP as bearish, retain >18% as contrarian-bullish note

The clearest backtest finding. Quoting the data:

| threshold | N | hit rate | median 5d TLT | read |
|---|---|---|---|---|
| dealer >12% | 143 | 32.9% | −0.05% | At base rate — noise |
| dealer >15% | 61 | 31.1% | +0.39% | Wrong-signed |
| dealer >18% | 23 | 26.1% | +0.79% | Contrarian-bullish |
| dealer >20% | 11 | 18.2% | +1.45% | Strongly contrarian-bullish |

**Market-structure read (BOND interpretation):** the backtest finding is internally coherent. Dealers absorb supply at the **end** of a sell-off — they backstop at peak yield. So high dealer take is a *late-cycle exhaustion* signal in the duration sell-off, not a *propagation* signal. Selling pressure that produces dealer-take spikes has already largely cleared by the time the spike is visible.

**Decision:**
- **Drop dealer>12% from the bearish escalation matrix entirely.**
- **Retain dealer >18% as a contrarian-bullish observation in commentary.** Do NOT use it for TLT-put add logic; consider it for TLT-put TRIM logic in future revisions (out of scope here).
- Leave the dealer column in monitors/AUCTION_HEALTH.md table for reference; just remove its role in the orange-trigger logic.

**Domain-expert dissent flag:** the backtest spans 2023-2026, which includes a regime where the SLR exemption and dealer balance-sheet capacity were less constrained than they may become if 30Y >5 persists. If we enter a regime where dealers *cannot* absorb (balance sheet caps hit), high dealer take could re-invert from contrarian-bullish back to forced-backstop bearish. The current proposal removes dealer from the trigger but BOND should re-test annually or upon SLR/balance-sheet regime change.

### 3d. Indirect weak — LOCK to per-tenor percentile, of-offering convention

**Decision (Will + Prome confirmed 2026-05-20):** I' fires if `indirect_pct` (of-offering) **< 15th-pctile of trailing-12mo prior prints in the same tenor**.

Backtest baseline: indirect<50% (v1 convention, of-offering) was the **single best signal**: N=18, hit 50%, median 5d TLT −1.07%, FPR 16.7%. This meaningfully beats base rate.

#### Why per-tenor percentile (rule (c)) over any flat threshold

Three paths were honestly considered:
- (a) Flat threshold only (either denominator). Simple, but **systematically blind to long-end indirect outliers**: a flat <50%-of-offering misses 5/12 10Y (51.5%); a flat <60%-of-competitive misses it too (it printed ~74% competitive). The 5/12 miss is not a rare false negative — it's a structural blind spot in exactly the tenors that matter most for the TLT-puts thesis (10Y/20Y/30Y).
- (b) Compound: flat + percentile rail (OR-logic). Catches 5/12, but two rules to apply in real time. Operationally the flat threshold becomes habit, the percentile leg becomes footnote, and within a quarter you've regressed to (a) by behavior.
- (c) Pure per-tenor percentile. One coherent question: *was indirect demand weak for this tenor relative to its own recent history?* No false simplicity. Threshold automatically self-calibrates to per-tenor baselines (10Y indirect runs structurally higher than 2Y indirect, so a flat number on either tenor is a hidden assumption that they share a distribution — they don't).

**The framing that decided it:** "simpler = better" is normally right, but a flat threshold across 7 tenors with different baselines is *false simplicity*. (c) is one rule that asks one coherent question. (a) is one rule that asks the wrong question for 5 of 7 tenors. (c) wins on signal-coherence, not just signal-strength.

#### Convention choice — of-offering, NOT of-competitive

The rule is on `indirect_pct` (of-offering). Reasoning:
1. The backtest signal was native to of-offering — it caught 5/12-style outliers because of-offering captures noncompetitive + SOMA absorption shifts (the actual foreign-demand-into-supply story).
2. of-competitive is the ZH/dealer-recap convention and remains useful for **display** (see §3d.dual-display below), but it ranks auctions *differently* — the 5/20 20Y prints 12th-pctile of-offering vs 45th-pctile of-competitive. The of-offering rank is the bidder-demand-into-supply truth; of-competitive is the dialect.

#### Dual-display convention (preserved)

Trigger arithmetic uses of-offering. **Display commentary uses BOTH numbers**, side-by-side, in every BOND auction recap. Recap-matching against ZH/dealer notes is a separate concern from trigger logic and they can coexist. The 5/20 dialect collision was a *display* failure, not a *trigger* failure — fix display by always quoting both, keep trigger on of-offering.

#### Quarterly snapshot mechanism (audit rail)

The percentile threshold moves as new auctions print and old ones roll out of the trailing 12mo window. Without a snapshot, future audits ("why did 5/12 fire but not a similar print in Sep 2026?") become opaque — the threshold has silently drifted.

**Mechanism:** every quarter (Jan 1, Apr 1, Jul 1, Oct 1), BOND refreshes a footer table in `monitors/AUCTION_HEALTH.md` capturing the current per-tenor 15th-pctile-of-trailing-12mo for `indirect_pct` (of-offering). The snapshot is **dated and frozen** — when auditing a fire that occurred in (say) Q3-2026, the audit references the **Q3-2026 snapshot**, not the live current values.

**Footer table format (to be embedded in `monitors/AUCTION_HEALTH.md`):**

```
## Percentile Snapshot Table — Indirect (of-offering), Trailing-12mo 15th pctile

| Tenor | Q3-2026 (effective 2026-07-01) | Q2-2026 (effective 2026-04-01) | Q1-2026 | Q4-2025 |
|---|---|---|---|---|
| 2Y  | XX.X% | XX.X% | XX.X% | XX.X% |
| 3Y  | XX.X% | XX.X% | XX.X% | XX.X% |
| 5Y  | XX.X% | XX.X% | XX.X% | XX.X% |
| 7Y  | XX.X% | XX.X% | XX.X% | XX.X% |
| 10Y | XX.X% | XX.X% | XX.X% | XX.X% |
| 20Y | XX.X% | XX.X% | XX.X% | XX.X% |
| 30Y | XX.X% | XX.X% | XX.X% | XX.X% |

Audit rule: when re-checking a past auction's fire/no-fire status, use the snapshot in force on the auction date. The live percentile threshold is **forward-only** — it governs new auctions from the snapshot date forward, never retroactively.
```

**Snapshot refresh:** BOND runs the refresh script (`refresh_auction_history_prome-spawned.py` or its successor) on the first business day of each quarter, computes 15th-pctile-of-trailing-12mo per tenor, appends to the table, and commits. Manual sanity-check by BOND: any large quarter-over-quarter shift (>3pp on any tenor) is flagged in the commit message with a one-line explanation (regime shift, sample-rotation effect, etc.).

**Initial seed (today, for reference):** per the v2 dataset prior to 2026-05-20, trailing-12mo 15th-pctile-of-offering:
- 10Y ≈ 52.0% (N=11)
- 20Y ≈ 53.4% (N=12)
- 30Y ≈ 52.5% (N=11)
- 2Y/3Y/5Y/7Y to be populated on first quarterly refresh.

These are the operative thresholds for the §6 re-grade below.

---

## 4. Combinator logic

**v1:** fire orange if ≥2 of {B, D, I} true (tail not in combinator). Dealer was 1-of-3 weight despite being wrong-signed → fires polluted by noise.

**v2 LOCKED:** Fire orange if **EITHER**:
- **I' alone:** `indirect_pct` (of-offering) **< 15th-pctile of trailing-12mo prior prints in same tenor** (single-criterion sufficient — this is the best signal, normalized per-tenor)
- **2-of-3:** {B' (BTC<2.30), I' (indirect <15th-pctile-of-tenor-12mo), T' (tail ≥ 75th-pctile-of-tenor on `tail_vs_cmt_bps`)}

Per-tenor percentile thresholds for I' and T' are read from the **quarterly snapshot table** in `monitors/AUCTION_HEALTH.md` (see §3d). The snapshot in force on the auction date is the audit reference, not the live current table.

**Why I' is single-criterion-sufficient:** the backtest hit rate of 50% at indirect<50% (v1 convention) is already a 16pp uplift over base. Requiring confirmation from BTC or tail would reduce false positives further but would also miss real signals (e.g., 5/12 10Y had indirect at the 10th pctile of all prior 10Y prints, ~18th pctile of trailing-12mo — that alone should have been a hard orange print regardless of BTC).

**Why 2-of-3 of {B', I', T'} rather than I'+1:** if I' is the strongest signal, we want it to be either a standalone fire OR confirmed by one of the other two. Requiring BOTH B' and T' (without I') is permissible because in that scenario you have a low-cover, high-tail print — that's a price+quantity stress combination that historically does precede sell-offs (e.g., 5/13 30Y had BTC 11th pctile + tail 75th pctile; indirect was OK).

**Expected fire frequency:** rough estimate from the v1 backtest distribution:
- I'<50% alone (v1): 18 fires / 323 auctions ≈ 1 per ~18 auctions
- {B', T'} without I': probably ~3-5 additional fires per 3 years
- Combined v2 fire rate: ~20-25 fires per 3 years, vs v1's 26 fires per 3 years

Same approximate frequency, materially better calibration. The "lose noise, keep signal" objective.

---

## 5. TLT-puts conditional-add logic update

### Current logic (v1)
"5/20 20Y orange triggers → hold → 4/5 conditional-add" — binary, single-step.

### Proposed v2 logic (confidence-stepped)

| Auction print | Conditional-add action |
|---|---|
| **No v2 fire** (I' ≥ 15th-pctile-of-tenor AND fewer than 2-of-3 of {B',I',T'}) | Hold. No add. (Current 5/20 state.) |
| **2-of-3 fire** (any 2 of {B'<2.30, I'<15th-pctile-of-tenor, T'≥75th-pctile-of-tenor}) | **Half-add** (1 contract of the 2-contract layer) |
| **I' alone, marginal** (indirect 10th-15th pctile-of-tenor-12mo) | **Half-add** |
| **I' alone, decisive** (indirect <10th pctile-of-tenor-12mo) | **Full add** (2 contracts) |
| **3-of-3 fire** | **Full add (2 contracts) + Will-touch ad-hoc prompt for review of additional capital deployment, decided case-by-case.** The matrix itself does NOT pre-authorize a 3rd contract; the 3-of-3 fire surfaces the rare extreme signal to Will rather than answering it. |

**Why confidence-stepping:** the v1 binary logic put a 5/12 10Y (indirect 7th-10th pctile, real outlier) and a noise-fire (e.g., dealer-only at 12%) in the same bucket. Confidence-stepping lets size respond to signal strength. **Budget is bounded at 2 contracts (Aug 15 $83P × 2)**; spending 1 vs 2 contracts on a marginal vs decisive signal is the right granularity. Anything beyond 2 contracts is out-of-matrix and requires explicit Will sign-off via the ad-hoc prompt path.

**Tomorrow's (5/21) 10Y application:** the cross-tenor base-rate sub-agent re-estimated P(Leg2 weak | Leg1 strong) at 11.7%. If 5/21 10Y prints I' decisively weak (<10th pctile-of-10Y-12mo) given 5/20 was strong-Leg-1, that's a 1-in-12 outlier and warrants the full add. If it prints a marginal 2-of-3 (e.g., BTC<2.30 + tail≥75th-pctile, indirect OK), that's a half-add. If clean, no action.

---

## 6. What the v2 matrix (rule (c) locked) would have said about recent auctions

**Operative thresholds (trailing-12mo prior to each auction date, computed against v2 dataset 2026-05-20):**
- 10Y 15th-pctile-of-offering: **52.0%** (N=11 prior 10Y in 12mo before 5/12)
- 20Y 15th-pctile-of-offering: **53.4%** (N=12 prior 20Y in 12mo before 5/20)
- 30Y 15th-pctile-of-offering: **52.5%** (N=11 prior 30Y in 12mo before 5/13)

### 5/12/2026 10Y

| Metric | Value | v2(c) reading |
|---|---|---|
| BTC | 2.40 | NOT B' (>2.30) |
| `indirect_pct` (of-offering) | **51.5%** | **I' FIRES** — below 15th-pctile-12mo threshold of 52.0% (18.2nd pctile of 12mo window; 10th pctile of full prior history) |
| `indirect_pct_of_competitive` | 64.0% | Display only; not used for trigger |
| `tail_vs_cmt_bps` (proxy) | ~+1bp (BOND records true tail +0.4bp from ZH) | NOT T' (10Y 75th-pctile is +2.9bps) |

**v2(c) verdict:** **ORANGE FIRES** (I' alone, single-criterion sufficient). 5/12 10Y is now correctly flagged.

**Domain-expert verdict: feels right** — this was the cleanest foreign-bid degradation signal in the recent set. (c) catches it; (a) and (b)-as-flat would have missed it.

**Tightness flag:** 51.5% vs 52.0% threshold is a 0.5pp margin. The fire is genuine but it's a *close* fire. In future near-boundary prints, BOND should note the margin in the recap so confidence-stepped sizing (§5) can be tuned (this is exactly an "I' marginal" case → half-add per §5 logic).

### 5/13/2026 30Y

| Metric | Value | v2(c) reading |
|---|---|---|
| BTC | 2.30 | **B' fires** (at threshold; 11th pctile of all prior 30Y) |
| `indirect_pct` (of-offering) | 53.7% | NOT I' (27.3rd pctile of 12mo window; 15th-pctile threshold is 52.5%) |
| `indirect_pct_of_competitive` | 66.6% | Display only |
| `tail_vs_cmt_bps` (proxy) | +1.6 | **T' fires** (75th pctile for 30Y) |

**v2(c) verdict:** **ORANGE FIRES** (B' + T', 2-of-3 satisfied via B' and T'; I' did NOT fire). Same fire as previous draft, different combinator path. 5/13 30Y was a price/quantity stress print, not an indirect-demand print — matrix correctly identifies it via the tail+cover path.

**Domain-expert verdict: feels right.** This was the genuine tail event in the recent set.

### 5/20/2026 20Y

| Metric | Value | v2(c) reading |
|---|---|---|
| BTC | 2.55 | NOT B' |
| `indirect_pct` (of-offering) | **58.3%** | NOT I' (25.0th pctile of 12mo window; 15th-pctile threshold is 53.4%) |
| `indirect_pct_of_competitive` | 67.7% | Display only |
| `tail_vs_cmt_bps` (proxy) | -6.8 (CMT noise) / ZH-reported ~0bp true tail | NOT T' |

**v2(c) verdict:** Would NOT fire. Matches the BOND domain read of "clean, soft-but-functional, no orange."

**Important reconciliation note:** the v2 README §3 quoted the 5/20 20Y indirect-of-offering as **12th-pctile vs all-prior-20Y (N=40, since 2023)**. Under rule (c), we restrict to **trailing-12mo (N=12)**, which raises the relevant percentile to **25th**. This is a real divergence between the full-history rank and the 12mo rank — driven by the 2023-2024 20Y prints running lower on indirect than the 2025-2026 cohort. The 12mo restriction is the correct frame for "is this print weak relative to the *current regime's* trend" — but it does mean some prints that look weak vs all-history are NOT weak vs recent. **Flag for Will/Prome: the 12mo window is the right normalization for regime-coherent fire logic, but BOND should annotate prints where 12mo vs all-history ranks decouple by >15pp — that decoupling is itself a regime-shift signal.**

**Domain-expert verdict: no-fire is the correct call.** The 20Y was clean vs the current regime, even if it looks soft vs the 2023 cohort.

### Cross-check summary (under rule (c))

| Auction | v1 verdict | v2(c) verdict | Domain feel | Reconciled? |
|---|---|---|---|---|
| 5/12 10Y | Yellow (no fire) | **Orange (I' alone, 12mo 18th-pctile)** | Real foreign-bid degradation | **YES — rule (c) catches it** |
| 5/13 30Y | Yellow (no fire — BTC at boundary, dealer 11.7%) | **Orange (B'+T')** | Real demand-weakness print | YES |
| 5/20 20Y | Yellow (no fire) | Yellow (no fire) | Clean vs current regime | YES |

**Headline: rule (c) catches the 5/12 10Y outlier that any flat threshold would miss, correctly fires the 5/13 30Y via the tail+cover path, and correctly does NOT fire the 5/20 20Y.** All three recent prints reconcile.

**New finding surfaced by the lock:** the full-history vs 12mo percentile decoupling on 5/20 20Y (12th vs 25th) is itself information — when ranks decouple by >15pp, that's a regime-shift annotation worth noting in commentary. BOND will add this as a display convention.

---

## 7. Caveats & honest uncertainty

1. **Backtest regime is 2023-2026 — non-stationary.** The dealer wrong-signing may flip in a balance-sheet-constrained regime. Re-test annually.
2. **`tail_vs_cmt_bps` is a proxy** with 1-5bp single-auction noise. Use ZH-quoted true tails when available; treat the proxy as the systematic distribution layer.
3. **Rule (c) is rank-stable, threshold-mobile.** The 15th-pctile threshold value moves as the trailing-12mo window rolls. The quarterly snapshot mechanism (§3d) is the explicit audit rail for this. Single-auction tightness flags (e.g., 5/12 10Y at 51.5% vs 52.0% threshold = 0.5pp margin) should be noted in commentary so confidence-stepped sizing can react.
4. **Small-N percentile noise.** Trailing 12mo gives N=11-12 per long-end tenor (one print per month). The 15th-pctile of N=11 is a stable rank, but single-observation rotations can move the threshold by ~1-2pp at quarter boundaries. Acceptable trade-off for regime-coherence.
5. **5-session horizon in backtest is arbitrary.** Some auction stress takes 10+ sessions; not tested.
6. **TLT-puts hit-rate calibration assumes the backtest's TLT relationship holds.** If we enter a regime where TLT decouples from auction signals (e.g., reflexive Fed cuts on bad prints), the hit rates degrade.
7. **Full-history vs 12mo rank decoupling** (surfaced in §6 5/20 20Y re-grade): when these decouple by >15pp, it's a regime-shift signal worth annotating. Not a calibration error — a feature.

---

## 8. Open questions for Will and Prome

1. ~~**Indirect threshold: flat <60% vs per-tenor percentile <15th?**~~ **RESOLVED 2026-05-20** — Will + Prome confirmed rule (c): `indirect_pct` (of-offering) **< 15th-pctile of trailing-12mo prior prints in same tenor**. Dual-display convention preserved (both of-offering and of-competitive shown in commentary; trigger uses of-offering only). Quarterly snapshot mechanism in `monitors/AUCTION_HEALTH.md` is the audit rail. See §3d for full reasoning and §6 re-grade verification (5/12 10Y now fires, 5/20 20Y correctly does not).

2. **Dealer-as-contrarian-bullish for TRIM logic?** Out of scope here, but the backtest finding (dealer >18% = +0.79% median 5d) is a separate research thread. Worth a follow-up sub-agent to backtest TLT-puts TRIM triggers on high-dealer prints?

3. ~~**Confidence-stepped TLT-add (§5) — granularity OK?**~~ **RESOLVED 2026-05-21** — Will + Prome confirmed middle path: matrix budget remains bounded at **2 contracts (Aug 15 $83P × 2)**. Half-add (1) / Full-add (2) tiers stay in the matrix. **3-of-3 fires do NOT pre-authorize a 3rd contract**; they trigger a Will-touch ad-hoc prompt where BOND surfaces the rare extreme signal and Will decides case-by-case whether to deploy additional capital from broader budget. Rationale: the marginal half-add tier just demonstrated value (5/12 10Y at 0.5pp margin); the aggressive tier is for a tail event we haven't seen and pre-committing capital to it is uncertain EV; the Will-approval gate persists regardless, so the ad-hoc path is strictly more flexible than baking the tier into the matrix.

4. ~~**Live deployment timing.**~~ **DEFERRED-with-rule 2026-05-21** — Will + Prome rejected the "wait until June 10-12" option (three weeks of operating on a known-broken matrix buys nothing). Today's 1pm ET 10Y print is the mechanical decision point. Pre-committed conditional rule, no second decision needed:
   - **v2 fires today** (10Y `indirect_pct` of-offering < 52% per snapshot threshold, OR 2-of-3 of {B', I', T'}) → **deploy v2 this week**. Broken framework + correctly-firing v2 should be reconciled fast.
   - **v1 fires but v2 does NOT** → **also deploy v2 this week**. Each v1 operation cycle on a known-broken rule is risk; false-positive on v1 is the worst-case for staying on v1.
   - **Neither fires** → **deploy in the quiet window of next week (Tue–Thu)**. Calendar choice.

5. **Backtest re-run with v2 dataset and v2 indirect convention?** Would need a fresh Prome-spawned sub-agent. **OPEN** — Will + Prome pairing this with the deployment-timing branch resolution.

---

## 9. Implementation plan (IF approved)

This is a checklist for BOND to execute on next live session after Will/Prome approval. Nothing here is done.

### Phase 0 — Next-respawn boot brief: today's 10Y dual-framework cross-grade (Q4 mechanical-resolution requirement)

**On BOND's next respawn (today, post-1pm-ET 10Y print), the outbox signal MUST include explicit v1+v2 cross-grading** so the §8 Q4 conditional rule resolves mechanically. Format:

**v1 read (current live matrix):**
- BTC < 2.30: ✓ / ✗
- dealer > 12%: ✓ / ✗
- indirect (of-offering) < 55%: ✓ / ✗
- **2-of-3 fire? YES / NO**

**v2 read (proposed matrix, rule (c) locked):**
- BTC < 2.30 (B'): ✓ / ✗
- indirect_pct (of-offering) < 52.0% (10Y trailing-12mo 15th-pctile snapshot threshold; I'): ✓ / ✗
- tail_vs_cmt_bps ≥ 75th-pctile-of-10Y-trailing-12mo (T', proxy ~+2.9bps per v2 README); confirm against ZH-quoted true tail when available: ✓ / ✗
- **I' alone fires? YES / NO** | **2-of-3 fire? YES / NO**

**Cross-grade summary line:** "v1 fires: YES/NO. v2 fires: YES/NO. Q4 branch resolved: deploy-this-week / deploy-this-week / deploy-next-week-Tue-Thu."

Also display `indirect_pct_of_competitive` (ZH convention) alongside `indirect_pct` (of-offering) per the dual-display rule (§3d). Note the trigger arithmetic uses of-offering only; the of-competitive figure is recap-matching display.

### Phase 1 — monitors/AUCTION_HEALTH.md

- [ ] Update §1 Classification Rules table:
  - 🟠 row criteria becomes: "I' (indirect_pct of-offering < 15th-pctile-of-tenor-trailing-12mo) alone, OR 2-of-3 of {BTC<2.30, I' as above, T' (tail_vs_cmt_bps ≥ 75th-pctile-of-tenor-trailing-12mo)}"
  - Remove dealer>12% from 🟠 trigger; add a note that dealer>18% is contrarian-bullish (informational, not a fire)
- [ ] **Add the quarterly Percentile Snapshot Table** (§3d format) as a footer in `monitors/AUCTION_HEALTH.md`; seed with current per-tenor 15th-pctile-of-offering values from the v2 dataset (10Y 52.0%, 20Y 53.4%, 30Y 52.5%; 2Y/3Y/5Y/7Y to be populated)
- [ ] Update Rolling Table to add `indirect_pctile_12mo` and `tail_pctile_12mo` columns (display only; trigger logic reads from snapshot table)
- [ ] Add a "Matrix v2 — calibration source" footer pointing to this proposal file and the backtest doc
- [ ] Document the dual-display convention (both of-offering and of-competitive indirect quoted in every auction recap) and the >15pp full-history-vs-12mo decoupling annotation rule

### Phase 2 — STATUS.md

- [ ] Update "TLT puts posture" language in Regime Read and Trade Interface sections to reflect confidence-stepped add logic, **explicitly bounded at 2 contracts (Aug 15 $83P × 2)**. Matrix recommends up to 2; any 3rd contract requires Will sign-off via the 3-of-3 ad-hoc prompt path.
- [ ] Update Convergence Matrix "Treasury auction health" upgrade-trigger language to match v2 criteria
- [ ] Update Immediate Catalysts table for any pending auctions (e.g., 5/21 10Y) with v2 add-trigger language, including the 3-of-3 → Will-touch surfacing path

### Phase 3 — TRADE.md

- [ ] Update TLT-puts entry with confidence-stepped add table (§5 above)
- [ ] Add reference link to this proposal + backtest

### Phase 4 — KB.tsv

- [ ] Log one VX.tsv entry: "Escalation matrix v1 → v2 swap, 2026-MM-DD, drop dealer-as-bearish, tighten indirect"
- [ ] Log one KB.tsv entry: backtest summary statistics (hit rate, base rate, sample size)

### Phase 5 — Cross-agent notification

- [ ] outbox/ to LIQUID, ZHAO, PROME: "BOND matrix v2 live; orange triggers now selectively rarer and signal-stronger; expect ~20% fewer escalation pings"
- [ ] Update PROTOCOL.md if it references v1 criteria (need to check)

### Phase 6 — Re-grade backlog + quarterly snapshot ops

- [ ] Re-grade the last 6 months of auctions in WATCH_20Y_10Y_MAY20-21.md and equivalent under v2(c) to seed the "expected fires per quarter" baseline
- [ ] **Establish quarterly snapshot refresh routine:** add to BOND's session-start checklist (or as a calendar reminder) — on the first business day of each quarter, refresh the auction history dataset, recompute trailing-12mo 15th-pctile per tenor for indirect (of-offering) and 75th-pctile for tail, append to the snapshot table with quarter-date, commit with explanation if any tenor moved >3pp QoQ
- [ ] **First snapshot population** (post-approval): populate 2Y/3Y/5Y/7Y trailing-12mo 15th-pctile-of-offering values (not computed in this draft because no recent prints in scope; populate from v2 dataset on approval)

**Estimated effort:** 1-2 hours single session for Phases 1-4; Phase 5-6 ~1 more session. Quarterly snapshot refresh thereafter: ~15min per quarter.

---

*Updated 2026-05-20 PM ET: §8 Q1 RESOLVED — indirect rule locked to (c) per-tenor percentile of-offering. §3d, §4, §5, §6 re-graded under the locked rule. Quarterly snapshot mechanism added (§3d) as audit rail.*
*Updated 2026-05-21: §8 Q3 RESOLVED — TLT-puts matrix budget bounded at 2 contracts; 3-of-3 fires trigger Will-touch ad-hoc prompt rather than pre-authorizing a 3rd contract. §5 table updated; §9 Phase 2 reflects bounded-budget language.*
*Updated 2026-05-21 PM ET: §8 Q4 DEFERRED-with-rule — deployment timing keyed to today's 1pm ET 10Y print via three-branch conditional. §9 Phase 0 added: mandatory v1+v2 dual-framework cross-grade in BOND's next-respawn outbox signal so Q4 resolves mechanically. Q5 OPEN, paired with Q4 branch resolution.*
