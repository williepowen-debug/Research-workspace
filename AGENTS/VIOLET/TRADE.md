# VIOLET TRADE

VIX-linked positions and trade framework.

---

## ACTIVE POSITIONS

**None.** Episode-17 (VIX May 19 25C) expired worthless 2026-05-19 — closed out below. *(Closeout recorded 6/9; this file had carried the position as OPEN for 3 weeks after expiry — caught by orchestrator review.)*

---

## CLOSED POSITIONS

### VIX 25C May 19 — SKEW Divergence Episode #17 (CLOSED — expired worthless)

| Field | Value |
|-------|-------|
| Instrument | VIX May 19 25 Call, long, entered 2026-04-16 (33 DTE) |
| Outcome | **Expired worthless 5/19** — VIX 18.06 at expiry vs strike 25 (6.94 pts OTM at 0 DTE) |
| Path | Trade-level invalidated Apr 23-28 (SKEW <140 4-td strict rule HIT); Will HOLD decision 5/3 as tail lottery on May 13 CPI / expiry mechanics; no tail materialized |
| Post-mortem | `research/2026-06-01_episode17_postmortem.md` — primary mechanism: positive-gamma suppression (KB-VIO-055/062) absorbing 5-6 consecutive catalysts |
| Epilogue | The underlying L1 signal class paid forward 17 days after expiry: 6/5 VIX +40% (KB-VIO-067 DIET fire 5/20-5/29 → spike at td-4). Right framework, wrong expiry window — the timing-vs-thesis lesson, and the vehicle lesson (fixed-expiry OTM calls die on timing even when the signal is right) |

---

## TRADE FRAMEWORK

### VIX Instruments

| Instrument | Use Case | Pros | Cons |
|------------|----------|------|------|
| VIX Futures | Direct vol exposure | Clean, liquid | Contango bleed, term structure risk |
| VIX Options | Defined risk, convexity | Asymmetric payoffs | Expiration timing, IV risk |
| Futures calendars (M2 vs M3) | Event-premium relative value | Not naked short-gamma; defined relationship | Both legs move; basis risk |
| UVXY / SVIX | Tactical only | Easy access | Severe decay / unlimited risk — avoid holding |

**Vehicle rule (Episode-17 + fleet TLT lesson):** match the vehicle to the open transmission channel AND the timing uncertainty. Fixed-expiry OTM options need the move inside the window; calendars and futures tolerate timing slip.

### Trade Types

| Type | Setup | Target | Stop |
|------|-------|--------|------|
| Vol spike hedge | VIX < 20, credit stress building | VIX 30+ | VIX 15 (thesis break) |
| **Sweet spot lag** | **VIX 15-26 + HY OAS >100bps** | **VIX +10pts** | **HY OAS reverses, VIX >30** |
| Credit-vol lag | HY OAS widens, VIX flat | VIX catches up | Credit reverses |
| Regime shift | Low vol → rising vol | VIX 25-30 | VIX back below 18 |
| **Event-premium fade** | **Post-event, premium hump located, substance clean** | **Hump deflates to normal contango** | **Credit confirms / vol re-extends** |

### Position Sizing

**Rule:** VIX trades are hedges, not alpha. Size accordingly. Short-premium trades: defined-risk structures ONLY, one tier lower than the equivalent long-vol conviction.

| Conviction | Long-vol max | Short-premium max | Time Horizon |
|------------|--------------|-------------------|--------------|
| Low (🟡) | 0.5% account | — (don't) | 1-2 weeks |
| Medium (🟠) | 1% account | 0.5% account | 2-4 weeks |
| High (🔴) | 2% account | 1% account | 1-3 months |
| Critical (🔴🔴) | 3% account | 1% account | Event-driven |

---

## LIVE DECISION FRAMEWORK — Event-Premium Fade (M2/Jul into FOMC) — NEW 6/9

**The decision that opens post-CPI 6/10.** Framework written BEFORE the print (8:30 ET 6/10) so the entry is pre-registered, not improvised.

**Thesis:** the 6/5 NFP spike left an event-premium hump, located (convexity_read 6/9) at the VIX9D kink (+2.27 over spot) and the M1:M2 contango (+7.50% adj). Both fade legs (rate-shock, AI-unwind) are deflating; credit never confirmed. If CPI passes non-tail, the remaining premium is fade-able into/through FOMC 6/17.

**Structure (priority order):**
1. **Short M2 (Jul) vs long M3 (Aug) futures calendar** — collects the Jul event-hump deflation post-FOMC; M3 leg hedges parallel vol shifts; not naked short-gamma. Relevant carry is the **M2:M3 spread: +4.00%** (VX/N6 20.14 exp 7/22 → VX/Q6 20.95 exp 8/19, CBOE settlement 6/8) — about HALF the M1:M2 +7.5% hump this doc previously implied; re-quote at entry. *(Corrected 6/9 late — orchestrator flag: prior text quoted the Jun/Jul spread for a Jul/Aug structure.)*
2. Alternative (defined risk): Jul VIX call credit spread sized to max-loss = the position's risk budget.
3. **NOT:** naked short VIX futures, short straddles, SVIX holds.

**Entry gate (ALL required, post-print):**
1. CPI non-tail — front collapses (VIX9D/VIX ratio decisively off 1.114 toward ≤1.05; M1 deflates)
2. Credit stays clean — HY <2.85, CCC <9.55 (LIQUID tripwire; FRED T+1 check)
3. AI-unwind leg not re-extending — NVDA/SMH stable-or-up post-print (HENRY read)
4. `convexity_read.py` post-print still locates a rich hump worth selling (M2 premium vs M3 above normal)
5. BOJ 6/16 risk priced: enter ≤50% size before BOJ, or wait until 6/16 post-MPM for full size

**L1-stack tension (state it, don't hide it):** the 5/20-5/29 DIET fire's fwd-60 window runs through **~Aug 12-21** (60 *trading* days from each fire day — the backtest's unit). At the ≥+15% tier it is RESOLVED (6/5 peaked +40%); at the ≥+50% tier (60% episode base rate, L1 canonical table) the window is **still live** — a second leg to VIX ~25+ remains a priced tail. *(Corrected 6/9 late — orchestrator flag: prior "~8/4" was 60 calendar days from the spike: wrong anchor AND wrong unit, would have lifted the size cap ~2 weeks early. The KB-VIO-079 error class, caught in the same session that canonized it.)* This is why size is capped, risk is defined, and the BOJ split-entry exists. Short-premium here fades the *event hump*, not the L1 signal class.

**Adjudication record:** 6/10 AM post-CPI: **GATE FAILS #1** (gate 1: ratio ~1.15 vs ≤1.05; Iran third leg re-armed the front — KB-VIO-081). 6/10 EOD: **GATE FAILS #2** (ratio 1.145 close-basis; M1:M2 +7.98% re-armed; Iran escalation sustained per WALTER/HAWK; credit clean but CCC 9.51 = 4bp from gate-2 flip). NO ENTRY. Framework alive — invalidation not triggered (VIX closed 21.86 < 22.24 overnight peak < 23). Re-adjudicate 6/11+; realistic next entry window is post-6/17 FOMC, and only on Iran stabilization. KB-VIO-086.

**Invalidation / exit (any one):**
- VIX >23 **closed-and-held** (re-graded 6/10, KB-VIO-082: a 23-touch is the MODAL path for this episode's shape — 6/6 historical early-+40% episodes touched ≥+50% ≈ VIX 23.0 on the table-consistent anchor — so a touch is expected, not disqualifying; only sustained closes above 23 mean the premium is re-arming rather than deflating). **Entry-structure corollary: any post-6/17 entry budgets a retest inside the L1 window (~Aug 12-21) per the KB-VIO-087 level ladder — the budget zone is 24-25 (P ~60-70% / ~40-50% from the 6/10 settle), with 23 near-mechanical — or uses the retest as the entry.**
- HY >2.85 or CCC >9.55 (credit confirms = fade→sustain flip) → exit immediately
- BOJ 6/16 hawkish-of-pricing (carry-unwind channel opens, SAM signal) → exit or cut to runner before FOMC
- Target: hump captured (M2:M3 back to normal contango) post-FOMC — take it off 6/18-6/22, don't overstay

**Approval:** structure + size goes to Will before any execution, per standing rule. This framework pre-registers the conditions; it does not pre-authorize the trade.

---

## THESIS TRADES (Standing)

### Credit-Vol Lag Trade (Four-Model Framework)

**Thesis:** When HY OAS widens >100bps from recent low and VIX < 20, VIX will spike >10pts within 2-6 weeks (70% hit rate, 25-30% false positive).

**Setup (All must be true):** HY OAS +100bps from recent low · VIX < 20 at onset · cross-sector widening · yield curve NOT inverted · no active Fed QE backstop
**Entry:** VIX calls 30-60 DTE (checks 1-3) / 60-90 DTE (all 5)
**Target:** VIX catches up to credit-implied level (HY OAS × 7.6 + 158 = implied VIX)
**Stop:** HY OAS reverses >50bps, VIX >30, or curve inverts
**Sizing:** 1% (medium) / 2% (all 5 checks)
**Status:** DORMANT — HY 2.75 (6/8), nowhere near trigger.

### DIET / STRICT Coiled-Spring Trade (L1 population signal)

Owned by `thesis/VIX_THESIS.md` § The DIET Coiled-Spring Trade — setup, tiers, and the **L1 canonical base-rate table (KB-VIO-079)** live there; this file does not duplicate them. Sizing rule of thumb: quote the base rate at the threshold the structure actually needs (≥+15%: 92-94% episode-level; ≥+50%: 56-60%) — far-OTM strikes price off the lower number.
**Status:** 5/20-5/29 DIET fire paid forward 6/5 (+40% at td-4). No new fire since.

### Term Structure Inversion (REVISED v3.1)

Inversion (VIX > VIX3M) **marks vol peaks, not onsets** (KB-VIO-034: 553 events, 2.2% hit rate). Use for **exit timing on long vol**, never entry.

---

## TRADE LOG

| Date | Instrument | Action | Size | Entry | Exit | P&L | Notes |
|------|------------|--------|------|-------|------|-----|-------|
| 2026-04-16 | VIX May 19 25C | BUY | — | — | — | — | SKEW divergence Episode-17. 33 DTE. Central case VIX 25-30. |
| 2026-05-03 | VIX May 19 25C | HOLD | — | — | — | — | Trade-thesis invalidated (4-td rule hit Apr 23-28); HOLD per Will = tail lottery. |
| 2026-05-19 | VIX May 19 25C | **EXPIRED WORTHLESS** | — | — | 0 | −100% of premium | VIX 18.06 vs strike 25. Post-mortem: `research/2026-06-01_episode17_postmortem.md`. *(Log row added 6/9 — was missing.)* |

*P/L figures are placeholders — cost basis per Will, not authoritative from state files.*

---

## HEDGING PROTOCOL

| Condition | Hedge Size | Instrument |
|-----------|------------|------------|
| Portfolio +20% from lows | 1% VIX calls | VIX calls 60 DTE |
| Credit spreads widening | 1-2% VIX calls | VIX calls 30-60 DTE |
| VIX < 15 (complacency) | 0.5% VIX calls | VIX calls 90 DTE |
| Geopolitical event live | 2% VIX calls | VIX calls 30 DTE |
| Term structure inversion | 1% VIX futures | Front month |

---

*Created: 2026-04-12*
*Last Updated: 2026-06-09 PM (orchestrator-review item #2: Episode-17 closed out [expired 5/19, had sat OPEN 3 weeks]; Event-Premium Fade framework added pre-registered ahead of the 6/10 CPI decision; 94% citations re-pointed at the L1 canonical base-rate table [KB-VIO-079]; short-premium sizing column added.)*
