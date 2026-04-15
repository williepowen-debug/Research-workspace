# FORGE INBOX — Trade Ideas

Potential trades routed by Prome. Review, research, decide.

---

### Silver Squeeze — Low Volume + Short Pressure

**When:** 2026-02-19 (processed 04:04 UTC Feb 20)
**Source:** @WSBGold, @DarioCpx (Twitter)
**Via:** Will (Telegram)
**Veracity:** ⚠️ UNVERIFIED — plausible but needs CME volume data to confirm

**Raw signal:**
- Claim: Silver futures volume at ~50% of 3-month average on Thursday
- SLV volume: 38,902 shown
- Context: Silver crashed from $115+ to ~$78 (Warsh shock aftermath)
- Thesis: "When shorts run out of time, momentum can turn violent"
- COMEX inventories below 100M oz (tight physical)
- Shanghai premium $10 above Western spot (unusual)

**Trade thesis:**
- Thin liquidity + large short positions = short squeeze potential
- If volume claim is true, market is illiquid enough for violent moves
- Could be a contrarian long setup after the Warsh crash

**Before acting:**
- [ ] Verify volume claim via CME Group data or Bloomberg
- [ ] Check COMEX inventory trend
- [ ] Review short interest / COT positioning
- [ ] Size appropriately — unverified signal = small position if any

**Vehicles:** SLV calls, SI futures, silver miners (SIL, SILJ)

---

### VIX Upside — SKEW Divergence Episode #17 Fired Apr 13

**When:** 2026-04-15 (submitted by VIOLET)
**Source:** VIOLET empirical backtest + options positioning snapshot
**Veracity:** ✅ Data verified against 19-year yfinance sample + live CBOE Apr 15 reads
**Supporting files:**
- `AGENTS/VIOLET/research/2026-04-15_skew_divergence_episodes.md` (17-episode backtest)
- `AGENTS/VIOLET/research/2026-04-15_vix_target_distribution.md` (target distribution + vehicle considerations)
- `AGENTS/VIOLET/workbook/VIX_OPTIONS.tsv` (option chain snapshot 2026-04-15)

**Signal summary:**
- SKEW-VIX-VVIX divergence (SKEW rose ≥10pts while VIX fell ≥5pts and VVIX fell ≥15pts over 20d) fired Apr 13 with SKEW peak 156.9
- 1% base rate (17 episodes in 19 years); 15 of 16 completed episodes produced ≥15% VIX rise within 60 days; 9 of 16 produced ≥50%
- SKEW-peak cohort match (>150) median outcome: VIX peak next 60d = 37.2 from current 18.09
- Current VIX 18.09 | VIX3M 20.81 | VVIX 99.56 | SKEW 149.94 (already rolling from 156.9 peak)

**Target distribution (if pattern continues):**
| Horizon | Central | Range | Tail |
|---------|---------|-------|------|
| 30-day peak | VIX ~25 | 22-30 | 38+ |
| 60-day peak, unconditional | VIX ~28 | 24-38 | 50-63 |
| 60-day peak, high-SKEW cohort | VIX ~37 | 34-40 | 62+ |
| 60-day peak, back-to-back cluster (closest structural analog to our Mar-27 → Apr-13 timing) | VIX ~38 | 25-63 | 62+ |

**Cross-check — options market agrees:**
- Apr 29 (FOMC) expiry: C/P OI ratio 9.01; top call strikes 25, 30, 24, 18, 20 → call-wall 25-30
- May 19 expiry: 3.24M call OI; top strikes 35, 25, 70, 45, 28 → heaviest wing at 35 with tail to 45/70

**Trade thesis:**
Long VIX upside with 30-60 day horizon, sized for high-probability central case (22-30) and leaving optionality for 40+ tail (2025-01 analog).

**Candidate vehicles (for Will to spec):**
| Vehicle | Pro | Con |
|---------|-----|-----|
| VIX calls (direct) | Purest exposure, highest gamma | Prices off futures not spot → M1 at 20.8; contango bleed if stalls |
| VIX futures (direct) | Linear exposure, no premium decay | Roll cost in contango; margin-heavy |
| VXX calls | Equity-style, liquid | VXX is M1/M2 blended — contango grinder |
| UVXY calls | 1.5× leverage | Double contango decay, very dirty instrument |
| SPY puts (proxy) | Cleaner instrument, tracks vol via delta | Mixes direction + vol; not pure play |

**Suggested structure (not prescriptive — Will's call):**
- Expiry: **Jun 17 or Jul 15** (captures full 60d window, avoids sub-30d timing risk)
- Strikes: **22-25 for high-probability payoff** (central case 25-28) OR **30-35 for tail exposure** (matches May 19 call-wall)
- Size: **Start 25% of intended size**; add on (a) SKEW re-ramp above 155, (b) another divergence fire within 30d, or (c) term structure flattening (VIX3M/VIX < 1.05)
- Consider a **calendar or ratio spread** rather than outright longs to offset contango bleed

**Invalidation (exit rules):**
- SKEW drops through 140 within 2 weeks AND VIX stays below 20 → pattern resolving peacefully; exit
- Term structure inverts and no spot move materializes within 5 days → thesis v3.1 says that's a peak marker; exit
- HY OAS rips tighter from 290bps → removes credit component of rising-vol regime
- 60-day window closes without peak reaching 22 → pattern failed (6% historical base rate)

**Reinforcement (add rules):**
- Another divergence fire before May 13 → promote to back-to-back cluster modal (38+ tail toward 55)
- SKEW rebounds above 155 while VIX stays below 22 → cohort stays in high-severity band
- VIX3M/VIX drops below 1.05 without spot move → tactical entry signal per thesis

**Known risks / concerns:**
1. **VIX is coincident, not leading** (VIOLET Principle #1) — options decay is real; timing matters
2. **Apr 29 C/P OI 9.01 means calls are already crowded** — entry price may reflect priced-in tail
3. **Episode #15 (2025-05) is the "dud" analog:** similar post-peak structure, only 22.3 next-60d peak. Not every post-peak fire launches
4. **SKEW already rolling (156.9 → 149.94)** — if it keeps dropping, cohort shifts to 140-150 range (central 26-29)
5. **#14 (2025-01) outlier drove the 62+ tail** — excluding it, high-SKEW median drops to ~30

**Decision:** Will reviews → approves size, vehicle, strike, expiry → FORGE executes.

— VIOLET 2026-04-15

---
