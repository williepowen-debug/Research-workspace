# VIOLET TRADE

VIX-linked positions and trade framework.

---

## ACTIVE POSITIONS

### VIX 25C May 19 — SKEW Divergence Episode #17

| Field | Value |
|-------|-------|
| Instrument | VIX May 19 25 Call |
| Direction | Long |
| Entry Date | 2026-04-16 |
| Strike | 25 |
| Expiry | 2026-05-19 (33 DTE at entry) |
| Thesis | SKEW divergence (94% hit rate, 156.9 peak → high-severity cohort). Central case VIX 25-30 within 60d. |
| Target | VIX 25-30 (ITM at 25+). Optimal window May 15-27. |
| Stop / Invalidation | SKEW <140 sustained + VIX <20 through May 7 (peaceful resolution); 60d window expires Jun 15 without VIX ≥22; HY OAS tightens below 2.60. **Note (KB-VIO-041):** "sustained" = key word. One-day break is not invalidation. But our d+3 Δ -17.7 is unprecedented for high-fire episodes. Watch SKEW through Apr 22 for bounce. |
| Reinforcement (add) | Second divergence fire before May 13; CCC OAS >10.0; VIX3M/VIX <1.05; **SKEW rebounds >145 by Apr 22 (FADE_RERAMP confirmation)** |
| Status | **OPEN — monitoring SKEW trajectory** |

---

## TRADE FRAMEWORK

### VIX Instruments

| Instrument | Use Case | Pros | Cons |
|------------|----------|------|------|
| VIX Futures | Direct vol exposure | Clean, liquid | Contango bleed, term structure risk |
| VIX Options | Defined risk, convexity | Asymmetric payoffs | Expiration timing, IV risk |
| UVXY | Short-term vol (1.5x) | Easy access | Severe decay, not for holding |
| SVIX | Short vol exposure | Inverse VIX | Unlimited risk, margin requirements |
| VIX Calls | Vol spike protection | Convexity | Time decay, timing risk |
| VIX Puts | Vol compression bet | Income | Limited upside, tail risk |

### Trade Types

| Type | Setup | Target | Stop |
|------|-------|--------|------|
| Vol spike hedge | VIX < 20, credit stress building | VIX 30+ | VIX 15 (thesis break) |
| **Sweet spot lag** | **VIX 15-26 + HY OAS >100bps** | **VIX +10pts** | **HY OAS reverses, VIX >30** |
| Term structure play | Inversion expected | Contango return | Backwardation persists |
| Credit-vol lag | HY OAS widens, VIX flat | VIX catches up | Credit reverses |
| Regime shift | Low vol → rising vol | VIX 25-30 | VIX back below 18 |

### Position Sizing

**Rule:** VIX trades are hedges, not alpha. Size accordingly.

| Conviction | Max Position | Time Horizon |
|------------|--------------|--------------|
| Low (🟡) | 0.5% account | 1-2 weeks |
| Medium (🟠) | 1% account | 2-4 weeks |
| High (🔴) | 2% account | 1-3 months |
| Critical (🔴🔴) | 3% account | Event-driven |

---

## THESIS TRADES (Pending)

### Credit-Vol Lag Trade (Four-Model Framework)

**Thesis:** When HY OAS widens >100bps from recent low and VIX < 20, VIX will spike >10pts within 2-6 weeks (70% hit rate, 25-30% false positive).

**Setup (All must be true):**
- HY OAS +100bps from recent low (Claude: 300bps from trough for confirmation)
- VIX < 20 at onset (ensures longest lead time)
- Cross-sector widening (not just energy/single sector)
- Yield curve NOT inverted (reduces false positives)
- No active Fed QE backstop

**Entry:** VIX calls 30-60 DTE when checks 1-3 met; 60-90 DTE when all 5 checks met
**Target:** VIX catches up to credit-implied level (regression: HY OAS × 7.6 + 158 = implied VIX)
**Stop:** HY OAS reverses >50bps, VIX spikes >30 (divergence resolved), or yield curve inverts
**Sizing:** 1% account (medium confidence), 2% account (all 5 checks met)

**Historical Performance:**
| Episode | Entry Signal | Outcome | P&L |
|---------|--------------|---------|-----|
| GFC 2007 | HY OAS 241→350bps, VIX 12-15 | VIX 15→31 in 8 weeks | +100%+ |
| 2011 EU | HY OAS 500→600bps, VIX 18-23 | VIX 23→48 in 10 weeks | +100%+ |
| 2015-16 | HY OAS 336→500bps, VIX 12-17 | VIX 17→40 briefly, then revert | Breakeven |
| Q4 2018 | HY OAS 316→416bps, VIX 13-16 | VIX 16→36 in 4 weeks | +100%+ |
| 2022 | HY OAS 310→340bps, VIX 25-38 | Credit never confirmed | Stopped out |

**Key Insight:** Trade works best in credit-originated crises with VIX < 20. Avoid when VIX already elevated or shock is rate-driven.

### SKEW Divergence Trade (NEW — Phase 2 Validated)

**Thesis:** SKEW divergence (SKEW rising while VIX+VVIX fall) identifies fragility with 94% hit rate for ≥15% VIX rise within 60d. Central case VIX 25-30, timing median 39 days.

**Setup (current — FIRED Apr 13):**
- SKEW divergence pattern fired ✅
- SKEW peak 156.9 (high-severity cohort) ✅
- VIX compressed from 31 to 18 (coiled spring) ✅
- Phase 2 analog translation: 5/12 match, 4 partial, 3 diverge

**Proposed structure (submitted to FORGE/INBOX.md Apr 15, awaiting Will):**
- Expiry: Jun 17 or Jul 15 (captures full 60d window)
- Strikes: 22-25 (central case) OR 30-35 (tail exposure)
- Size: Start 25% of intended; add on SKEW re-ramp, second divergence, or term structure flattening
- Consider calendar/ratio spread to offset contango bleed

**Invalidation (exit):**
- SKEW <140 sustained + VIX <20 → peaceful resolution
- Term structure inverts without spot move in 5d → peak marker per v3.1
- HY OAS tightens from 284bps → removes credit component
- 60d window closes without VIX reaching 22 → pattern failed

**Reinforcement (add):**
- Another divergence fire before May 13 → back-to-back cluster (tail 38+)
- SKEW rebounds >155 while VIX <22 → high-severity band holds
- CCC OAS >10.0 → analog alignment improves
- VIX3M/VIX <1.05 → tactical entry signal

### Term Structure Inversion Trade (REVISED v3.1)

**Thesis (REVISED):** Term structure inversion (VIX > VIX3M) **marks vol peaks, not onsets** (KB-VIO-034: 553 events, 2.2% hit rate for >50% spike, mean -5% forward). Use for **exit timing**, not entry.

**Setup:**
- VIX3M/VIX ratio drops below 1.0
- Interpretation: vol likely peaking — consider taking profits on long vol

**NOT an entry signal.** Flattening contango is NOT an entry for VIX calls.

---

## TRADE LOG

| Date | Instrument | Action | Size | Entry | Exit | P&L | Notes |
|------|------------|--------|------|-------|------|-----|-------|
| 2026-04-16 | VIX May 19 25C | BUY | — | — | — | — | SKEW divergence trade. 33 DTE. Central case VIX 25-30. |

---

## HEDGING PROTOCOL

When to add VIX hedges:

| Condition | Hedge Size | Instrument |
|-----------|------------|------------|
| Portfolio +20% from lows | 1% VIX calls | VIX calls 60 DTE |
| Credit spreads widening | 1-2% VIX calls | VIX calls 30-60 DTE |
| VIX < 15 (complacency) | 0.5% VIX calls | VIX calls 90 DTE |
| Geopolitical event live | 2% VIX calls | VIX calls 30 DTE |
| Term structure inversion | 1% VIX futures | Front month |

---

## PENDING TRADES

### ~~VIX Upside — SKEW Divergence Episode #17~~ → EXECUTED

**Submitted:** 2026-04-15 to FORGE/INBOX.md
**Executed:** 2026-04-16 — Will placed VIX May 19 25C
**Loop closed.** Position now tracked in Active Positions above.

---

*Created: 2026-04-12*
*Last Updated: 2026-04-16*
