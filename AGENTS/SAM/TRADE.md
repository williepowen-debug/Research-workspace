# SAM — Trade Ideas

**Last Updated:** 2026-05-27 (v1.5 sync — Position unchanged; Channel 1 demoted to deferred structural backstop 3-of-3 post-Sumitomo; v1.5 single-path = June BOJ Jun 16 dominant)
**Domain:** Japan Macro, Yen, JGBs, Carry Trade, BOJ Policy

*Live prices, probabilities, threshold status, and dashboard live in `STATUS.md`. This doc owns position details + decision card — point to STATUS for live data.*

---

## Active Positions

### 🔴 FXY (Yen ETF) — LONG (Shares + Calls)

**Shares:** 13 (Tranche 1 + Tranche 2 — added +5 at ~$57.66 May 21)
**Calls:** 1 × June 18 2026 $58 call @ $0.40 premium ($40 total cost). Executed May 21 pre-CPI.
**Entry context (Tranche 1):** USD/JPY at 160 handle, pre-intervention, pre-BOJ hike cycle.
**Entry context (Tranche 2):** Post Apr 30 + May 6 MOF interventions (~¥10T combined), v1.4 thesis bump confirming JGB 30Y at 4.0% via J-ICS lifer abandonment. Better entry than original May 12 $58.00 limit.
**Entry context (Call):** Sized as event lottery — 1 contract = max loss $40 (~5% of share notional). ATM at execution. IV ~9.3% (underpriced for BOJ event). Entered pre-CPI rather than post-CPI for IV protection (CPI surprise risk both ways).

**Thesis (v1.5 single-path):** Structural yen appreciation over next 3-6 months driven by BOJ rate hike (Jun 16 at 55-65%) and carry unwind (CFTC short -93,905, 92% of cycle peak). Channel 1 (life insurer repatriation) demoted to deferred structural backstop after 3-of-3 Big 3 mutual ESR window confirmation (Nippon 195% M&A, Meiji 208% manageable, Sumitomo 197% ↑+19pt WITH foreign book growing +¥1.11T). ESR pressure absorbed via capital actions (Resolution Life M&A, Allstate, Dearborn), equity rally, and hedge-cost relief — NOT foreign bond sales. Foreign books in unrealized GAIN at all three. J-ICS domestic-curve mechanism (JGB 30Y) intact but cross-border transmission timing pushed to multi-year. Channel 3 dormant on Brent collapse (-12% to $93.13 on Iran/Hormuz MOU framework hardening). Channel 2 (carry/BOJ) is the dominant remaining near-term catalyst.

---

## 🔴🔴 FXY Entry Decision Card (v1.4 refresh — May 21)

### DECISION: 13 SHARES + 1 JUNE $58 CALL — EXECUTED MAY 21

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Tranche 1** | ✅ +8 → 8 shares | Executed pre-intervention |
| **Tranche 2** | ✅ +5 → 13 shares at ~$57.66 (May 21) | v1.4 authorization; better entry than original $58 limit |
| **June $58 call** | ✅ 1 × Jun-18 $58 @ $0.40 ($40) | Event lottery; ATM at execution; pre-CPI entry |
| **Stop loss (shares)** | FXY ~$55.05 / USD/JPY ~167 | Oil shock full domination + intervention fails (thesis break) |
| **Price target (6-month)** | FXY ~$60–62 / USD/JPY ~148–152 | Post-BOJ hike + carry unwind + oil stabilization |
| **Blended entry (shares)** | ~$57.48 | (8 × $57.36 + 5 × $57.66) / 13 |
| **R:R from blend (shares)** | 1:1.86 — risk $31.50 to target $62 ($58.76 upside) | Plus convex tail via call |
| **Call max loss** | $40 (sunk if FXY <$58 at June 18 expiry) | 5.3% of share notional |
| **Call payoff @ $60 (target lower)** | ~$160 = 4x | Triggers if BOJ hikes + small post-event move |
| **Call payoff @ $62 (target upper)** | ~$360 = 9x | Triggers if BOJ + intervention #3 or partial unwind |

### Tranche 2 Hard-Trigger Status — UPDATED v1.5 (May 27)

| Hard Trigger | Status (May 27) |
|---|---|
| BOJ hike at June meeting | PENDING (Jun 16; SAM-21 ~57%; market 55-65%) — **dominant remaining catalyst** |
| **MOF intervenes at 160** | ✅ **FIRED — twice (~¥10T / $63.5B); #3 zone dormant on Brent collapse + no jawbone since May 12** |
| USDJPY sub-155 for 3+ sessions WITH oil normalizing | NEAR-MISS (May 6 low 155.05, 1 session); oil now $93.13 — Phase 2 condition active, watch for 3-session test |
| ESR <200% (Big 3 mutuals) | ✅ **RESOLVED 3-of-3 BENIGN** (Nippon 195% M&A; Meiji 208% manageable; Sumitomo 197% ↑+19pt with foreign book growing) — Channel 1 deferred |
| **JGB 30Y >4.0% (v1.4)** | ✅ BREACHED May 15 (4.000%); since RETRACED to 3.866% on Brent + dovish CPI; SAM-26 tracking FALSE at ~25% |
| Fed cuts via credit cascade | PENDING — **elevated to secondary path under v1.5** |

### Why this entry (May 21) vs original May 12 plan

- Original May 12 limit at $58.00 sat unfilled while FXY drifted to $57.66
- v1.4 thesis is STRONGER than May 12: JGB 30Y at 4.0% confirms Channel 1 amplifier; lifer long-end abandonment is self-perpetuating; Bessent affirmation promoted to Channel 3 pillar
- Yen weakness May 12-21 (157.61 → 159.19) is rate-differential-driven (not flow-driven, not trade-driven) — exactly the gap a BOJ hike closes
- STRATEGY no-chase rule applies to UPSIDE breaches (chasing a missed entry up); adding at $57.66 is BELOW the original limit = new entry zone, not a chase
- 18 trading days to BOJ June 16

---

## 🔴 FXY Options Layer (NEW — May 21)

### Strategy: Layer convex tail exposure on linear share base

**Why options:** FXY IV is unusually LOW (9-16% across strikes) — market is pricing FXY as quiet through BOJ. That's wrong if: (a) BOJ actually hikes (realized vol 2-3x current IV), (b) intervention #3 fires, (c) Aug 2024-style unwind (realized vol 50%+). Heavy call positioning across the chain (P/C 0.06x; 89% of call OI in $58-65 zone) means institutional money is already there.

### Position A — September $60 calls — ❌ NOT WARRANTED under v1.5 (resolved May 27)

**Authorization withdrawn.** The asymmetry case for Position A was built on multi-channel convergence (Channel 1 + Channel 2 + Channel 3 firing in same window). Post-Sumitomo (3-of-3 Big 3 ESR resolved benign), Channel 1 is demoted and Channel 3 is dormant. Structure has narrowed to single-path. Paying for time at a 55-65% single-catalyst case is not the asymmetry the position was originally sized for.

**Re-activation conditions (any one re-opens the question):**
1. Channel 1 reactivates — JGB 30Y blowout to 4.5%+ OR ESR re-test sub-200% via market stress (not capital action)
2. Channel 3 reactivates — Iran/Hormuz MOU collapses → Brent snapback → USDJPY 160+ retest → intervention #3 zone live
3. Tokyo May CPI rebounds + CFTC breaks new cycle peak (-102K+) + dissent split widens → SAM-21 re-rates to 70%+
4. Fiscal-dominance / BOJ-frozen path (eval Case 02 finding) sharpens into a distinct tradeable thesis — if true, the right vehicle is JPY vol or curve steepeners, not Sep FXY OTM

*See STRATEGY.md "Position A" section for full decision logic. See STATUS.md "FXY Positioning" for the morning v1.5 writeback that produced this resolution.*

### Position B — June $58 calls — ✅ EXECUTED MAY 21 PRE-CPI (1 contract @ $0.40)

| Field | Value |
|---|---|
| Strike / Expiry | $58 / 2026-06-18 (28 DTE at entry) |
| Entry price | $0.40 ($40 total for 1 contract) |
| Size | 1 contract (max loss $40) |
| Open Interest | 13,846 (smart money already here) |
| IV at entry | 9.3% — underpriced for BOJ event |
| Breakeven | $58.40 (+1.3% from $57.66 entry) |
| Payoff at $60 | ~$160 = **4x** |
| Payoff at $62 | ~$360 = **9x** |
| Captures | BOJ Jun 16 event directly + 2 days post |

**Entry timing — pre-CPI vs my post-CPI recommendation:**
- I had suggested waiting until Friday post-CPI for potentially cheaper entry ($0.20-0.25) on expected soft print
- Will executed pre-CPI for IV protection: if CPI surprises HOT (>2.0%), FXY pops, IV expands, and the post-CPI entry would have been at $0.60+ — locked in worse entry
- Trade-off: paid full price for IV protection; sacrificed potential 50% discount if soft CPI plays out
- **Net:** legitimate hedge against the CPI bimodal outcome. Sized small (1 contract = $40) so the timing penalty is bounded.

**What's NOT in the position (originally planned but not executed):**
- Additional June $58 contracts (2-4 more); skipped given small initial sizing
- Position A (Sep $60 calls) — still authorized but not yet executed

### Total options layer sizing

- **Position A (Sep $60):** $340-680 (~5-10% of position notional)
- **Position B (June $58, conditional Friday):** $120-200 (~2-3%)
- **Combined ceiling:** ~$880 (10-12% of total FXY exposure)

### Execution rules

- **Use limit orders only.** FXY options have wide spreads — June $60 has 200% bid-ask spread. Pay at mid or slightly favorable; do NOT market.
- **Stick to $58 and $60 strikes** where OI is real (13K+ at June $58, 21K at Sep $60). $61+ strikes are illiquid noise.
- **No stops on options** — premium is the loss limit. Sized small for that reason.

### What we are NOT doing (and why)

- **No short-dated OTM strikes ($61+ June):** wide spreads, thin OI, premium is mostly noise
- **No LEAPS ($65+ Jan 2027):** FXY rarely sustains above $65 even in carry unwinds
- **No call spreads:** the asymmetric tail (Aug 2024 redux) IS the point; capping upside throws away the best scenario
- **No puts/spread sells:** different bet; not the thesis

### Catalyst Sequence

*Resolved-event narratives live in `thesis/timeline/TIMELINE.md`. Forward-only catalysts in `CALENDAR.md` and "Key Dates" section above. The June 16 BOJ MPM is the dominant remaining near-term catalyst under v1.5 single-path.*

---

## Carry Unwind Probability (v1.5 — May 27)

*Canonical live numbers in STATUS.md. Snapshot here for reference; refresh on every thesis-level reframe.*

| Timeframe | Probability | Key Driver |
|-----------|-------------|------------|
| **7 day** | **12%** | All Big 3 binary catalysts resolved benign; no near-term Channel 1 trigger remaining. CFTC reload + Tokyo CPI are gradients, not binary. |
| **30 day** | **62%** | Channel 1 leg structurally removed; June BOJ + CFTC reload anchor |
| **60 day** | **80%** | Channel 2 (BOJ hike) is near-sole driver under single-path; Aug 2024 unwind speed precedent intact |

---

## The Asymmetric Setup

### Intervention Paradox
MOF intervenes → sells USD/buys yen → accelerates carry unwind → FXY up.
MOF doesn't intervene → yen weakens on oil → forces more repatriation selling of UST → carry unwind anyway → FXY up (delayed).
**Both paths lead to the same destination.** The only question is speed.

### "Bigger Hike" Possibility (low probability under v1.5)
Mar 30 BOJ Summary of Opinions revealed board members debating not just WHEN to hike but HOW MUCH. Apr 28 produced 3 dissents (Takata, Tamura, Nakagawa) for 1.00% — that's where the dissenters wanted to go in April. SAM-24 @85% on 25bp (to 1.00%) rather than 50bp. 50bp would require either acute crisis (insurer ESR <150%) or full Takaichi-Ueda rupture — neither in v1.5 base case. Path-dependence favors 25bp.

### Independent Fed Path (via HANS)
Private credit cascade (APO, ARES — 9 funds gated) → recession signal → Fed forced to cut → USD weakens → USD/JPY sub-145 WITHOUT BOJ doing anything. This is an independent catalyst that doesn't require BOJ action. Below 145 = carry unwind. Below 140 = disorderly.

---

## Risk Factors (Bear Case — v1.5 single-path)

| Risk | Probability | FXY Impact | Mitigation |
|------|-------------|-----------|-----------|
| **BOJ delays past June** — oil + political cover extends to Sep+ | **25%** | -3–5% short term | **Single-path elevation** — under v1.5 there's no parallel Channel 1 catalyst to absorb the disappointment. Time = more CFTC fuel; unwind more violent when fires. Tokyo May CPI + Jun 18-19 trade balance gate this. |
| **Oil shock dominates** — Kharg struck, Brent $120+; yen stays weak | 15% | FXY to ~$51-53 | Stop at $55.05; position sized to absorb. Currently $93.13 — Phase 2 direction. |
| **Intervention fails** — USDJPY breaks 162+ despite #3, Bessent jawboning empty | 12% | FXY to ~$55–56 before recovery | Hold if fundamentals intact; lowered from 15% on Brent collapse defusing #3 zone |
| **Channel 1 reactivates** (new shock — JGB 30Y to 4.5%+, ESR sub-200% via market stress) | 10% | +3-5pp 60d prob upside (offsetting positive — would expand structure back to multi-channel) | Watch JGB long-end, M&A saturation at Big 3 mutuals |
| **Takaichi political collision** — 0.75% stated ceiling; next hike to 1.00% triggers friction. Scenario: BOJ wants to hike but blocked via Katayama pressure or BOJ Law revision threats | medium-term | Limits structural appreciation | Aida "tolerate to 0.75%, pause until 2027." Watch Kantei/Aida commentary. June hike math unchanged; risk is 2027+. |

---

## Watchlist

### 🟠 EWJ (Japan ETF) — PUTS

**Thesis:** Japan is in a binary trap. 75% of mortgages are FLOATING RATE (linked to BOJ policy rate). BOJ hikes to 1.00% → immediate household stress → consumption drag → recession risk. BOJ doesn't hike → JGB crisis deepens → yen collapse → forced UST selling.

**Entry Triggers (updated v1.5):**
- [ ] BOJ hikes to 1.00% (Jun 16 base case per SAM-21 ~57%; market 55-65%) — mortgage transmission begins
- [x] ~~Tankan shows consumer weakness (Apr 1)~~ — Tankan BEAT (mfg 17, non-mfg 36). Not a trigger.
- [x] ~~Q1 2026 GDP contraction~~ — Q1 GDP BEAT +2.1% ann (May 19). Not a trigger.
- [ ] Mortgage DQ data spikes in Japan
- [ ] Japan Q2 2026 GDP shows contraction (Aug print)

**Anti-Triggers:**
- BOJ delays past June (gives households breathing room) — **single-path elevated risk under v1.5 at 25%**
- Real wages sustain positive (Jan was +1.4% — first positive in 13 months)
- Oil shock resolves (Brent $93.13, MOU framework hardening) — easing CPI pressure ✅ currently active

**Status:** ⏳ WATCHING — BOJ hike Jun 16 is the trigger (SAM-21 ~57% / market 55-65%).

---

### 🟡 TLT (Long Treasuries) — PUTS

**Thesis:** Japanese institutional UST selling drives long-end yields higher. TLT falls.

**Evidence now confirmed:**
- Feb TIC: ¥3.42T ($21.8B) net selling — largest since Oct 2024
- Banks led selling (¥3.14T), life insurers ¥618.7B
- Hedged UST return now negative vs JGB by ~0.34% — structural incentive to sell
- FY-end repatriation active through Mar 31

**Status:** ⏳ WATCHING — LIQUID is primary owner of this trade. SAM provides the Japan flow signal.

---

### 🟡 Japan Banks — SHORTS

**Thesis:** BOJ hike to 1.00% → floating mortgage stress (75% of all mortgages) → bank provisions rise.

**Candidates:** MUFG, SMFG, MFG (US-listed ADRs)

**Entry Triggers:**
- [ ] BOJ hikes to 1.00% (Jun 16 base case — SAM-21 ~57%; market 55-65%)
- [ ] Mortgage DQ spikes in Japan data
- [ ] Bank earnings show provisioning increase

**Status:** 💭 IDEA — Needs Japan-specific mortgage data. June hike timeline confirmed by Apr 28 dissent split.

---

## Key Dates (forward-only; full operational calendar in CALENDAR.md)

| Date | Event | Impact |
|------|-------|--------|
| **🟠 Thu-Fri May 28-29** | **Tokyo May CPI** | Leading indicator for June national. Core-core <1.9% → June BOJ pricing breaks lower from 55-65% → v1.5 single-path impairs materially |
| **🟠 Fri May 29** | **CFTC JPY weekly (May 22 data)** | Currently -93,905 (3rd build week, 92% of cycle peak). Watch for break of -102K or sudden cover. |
| **🟠 ongoing** | **Iran/Hormuz MOU framework** | Sign → Phase 2 accelerates (yen-bullish); collapse → Brent snapback → intervention #3 zone reactivates |
| **🟠 Jun 18-19** | **May trade balance — Phase 1 stability lag-test** | Volume-vs-cost decomposition; gates v1.4 trade-inversion finding (see CALENDAR routing) |
| **🔴🔴 Tue Jun 16** | **BOJ MPM — DOMINANT REMAINING CATALYST (SAM-21 ~57%; market 55-65%; SAM-24 25bp @85%)** | FXY +5–8% structural on hike; v1.5 single-path |
| Jun 16 | Sato joins BOJ board | Hawk→dove swap; post-June political risk |
| Jun 16-17 | BOJ interim QT assessment | Pace adjustment; potential super-long-specific op if JGB stress re-engages |

---

## Historical Context

**Aug 5, 2024 Precedent:**
- Yen strengthened 3%
- VIX spiked to 65 (from ~15)
- Nikkei -12% in one day
- Margin calls cascaded globally
- **Timeline: HOURS, not days**

This can happen again. Position sizing must account for gap risk.

---

## Cross-References

- **LIQUID/TRADE.md** — UST impact, funding stress
- **HENRY/TRADE.md** — VIX/vol plays on Japan trigger
- **HANS** — Fed independent path (private credit cascade)
- **BRENT** — Oil-in-yen dynamics, SK refiner crisis
