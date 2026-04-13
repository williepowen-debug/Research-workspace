# VIOLET TRADE

VIX-linked positions and trade framework.

---

## ACTIVE POSITIONS

None currently.

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

### Term Structure Inversion Trade

**Thesis:** Term structure inversion (VIX > VIX3M) predicts vol spikes.

**Setup:**
- VIX3M/VIX ratio drops below 1.0
- Credit stress present
- Macro catalyst pending

**Entry:** VIX futures or calls
**Target:** Backwardation resolves, VIX mean reverts
**Stop:** Inversion persists >2 weeks (structural shift)

---

## TRADE LOG

| Date | Instrument | Action | Size | Entry | Exit | P&L | Notes |
|------|------------|--------|------|-------|------|-----|-------|
| — | — | — | — | — | — | — | No trades yet |

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

*Created: 2026-04-12*
