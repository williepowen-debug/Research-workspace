# LIQUID STATUS
**Last Updated:** 2026-02-02 | **Status:** 🟠 ELEVATED — Buffer Exhausted, System Fed-Dependent

---

## THESIS

**The plumbing is fragile. The buffer is gone. The Fed is the only thing holding it together.**

US Treasury/repo funding markets have transitioned to a structurally vulnerable state:
- **RRP depleted** — $10.4B remaining vs $2.5T peak. Buffer = ZERO.
- **SRF ceiling is porous** — Dec 31: SOFR traded 12bps ABOVE the Fed's backstop rate
- **Dealers stuffed** — ~$200B net long Treasuries, SLR prevents expansion
- **Basis trade armed** — $1.85T hedge fund positions funded by money market repos

The system now operates in a **Fed-dependent regime**. Any shock that exceeds real-time Fed intervention capacity triggers cascade.

**Confidence:** Pattern 90% | Timing 70% | Magnitude 85%

---

## SIGNAL DASHBOARD

| Vector | Value | Status | Threshold |
|--------|-------|--------|-----------|
| RRP Balance | $10.4B | 🔴 RED | <$5B critical |
| SOFR-IORB Spread | +3bps | 🟢 GREEN | >+5bps yellow |
| SRF Usage (peak) | $74.6B | 🟠 ORANGE | >$50B sustained |
| Dealer Net Position | ~$200B | 🟠 ORANGE | >$200B clogged |
| Basis Trade Exposure | $1.85T | 🟡 YELLOW | >$2.0T orange |
| Treasury FTD | $42.4B | 🟡 YELLOW | >$50B orange |
| Auction BTC (5Y/7Y) | 2.34-2.45x | 🟡 YELLOW | <2.30x orange |
| Auction BTC (2Y/10Y) | 2.55-3.16x | 🟢 GREEN | Healthy |
| CLO AAA Spread | 115bps | 🟢 GREEN | >150bps trigger |

**Composite Assessment:** Structural vulnerability HIGH, active stress LOW

---

## THE RRP STORY

**What happened:**
- RRP peaked at $2.5T (Dec 2022) — excess liquidity parked at Fed
- Drained steadily as MMFs rotated to T-bills and private repo
- Hit effective floor (~$2B) by Jan 2025
- Fed responded with Reserve Management Purchases ($40B/mo T-bills)

**Why it matters:**
- RRP was the system's **shock absorber**
- When funding stress hit, cash could flow OUT of RRP into markets
- With RRP at zero, there's no buffer — stress transmits directly to rates

**Current state:**
- $10.4B as of Feb 2 (8 counterparties)
- Technically above $5B RED threshold but functionally zero
- Any TGA rebuild or auction settlement now drains reserves 1:1

---

## TRANSMISSION MECHANISMS

### 1. Basis Trade Unwind (ARMED)
```
MMF stress
    ↓
Stop rolling FICC Sponsored Repo ($2.48T)
    ↓
Hedge funds can't fund basis trade ($1.85T)
    ↓
Forced Treasury selling
    ↓
Yield spike → VaR shocks → Cascade
```
**Status:** ARMED — Requires MMF redemption trigger
**Precedent:** March 2020 (but we had $500B+ RRP buffer then)

### 2. SRF Ceiling Breach (CONFIRMED)
```
Quarter-end or stress event
    ↓
Collateral demand spikes
    ↓
GSIB dealers won't expand (SLR constraints)
    ↓
Non-dealers can't access SRF directly
    ↓
SOFR trades ABOVE SRF rate
```
**Status:** CONFIRMED — Dec 31, 2025: +12bps breach
**Implication:** SRF is NOT a hard ceiling. SOFR can spike through it.

### 3. Japan Repatriation (LATENT)
```
BOJ policy shift OR USD/JPY >160
    ↓
Japanese institutions repatriate ($60-100B)
    ↓
Treasury selling into market with zero RRP buffer
    ↓
Yield spike without cushion
```
**Status:** LATENT — USD/JPY at ~158, watching BOJ
**Cross-link:** SAM monitors Japan dynamics

### 4. TGA Drain (LATENT)
```
Tax season (April) OR debt ceiling resolution
    ↓
Treasury rebuilds TGA
    ↓
Drains reserves 1:1 (no RRP offset)
    ↓
Reserves approach "ample" floor (~$3T)
    ↓
Funding stress
```
**Status:** LATENT — April 2026 key risk window
**Current reserves:** $2.95T (down $377B YoY)

---

## DEALER CAPACITY CONSTRAINT

**The undervalued indicator:** FR 2004 Net Positioning

- Dealers net long ~$200B Treasuries
- SLR (Supplementary Leverage Ratio) prevents balance sheet expansion
- Even at profitable spreads, dealers WON'T intermediate
- When dealers "stuffed" = zero elasticity for shocks

**Implication:** Market depth is an illusion. Liquidity can vanish instantly.

---

## WARSH NOMINATION

Kevin Warsh nominated as Fed Chair (Jan 30). Key for LIQUID:

**Warsh's history:**
- Balance sheet HAWK — "bloated balance sheet subsidizes Wall Street"
- Criticized low rates enabling deficits
- Prefers "let markets clear" over intervention

**LIQUID implications:**

| Variable | Powell | Warsh (if confirmed) |
|----------|--------|----------------------|
| SRF activation bar | Low | Higher |
| QE threshold | Moderate | Much higher |
| Crisis response speed | Fast | Slower |
| Balance sheet expansion | Willing | Reluctant |

**Key insight:** Fed **CAPACITY** unchanged ($500B SRF, swap lines). Fed **WILLINGNESS** potentially degraded.

**Timeline:**
- May 2026: Powell term expires
- TBD: Warsh confirmation hearings
- Uncertainty elevated until resolved

---

## CROSS-AGENT CONNECTIONS

| Agent | Connection | Signal Exchange |
|-------|------------|-----------------|
| **SAM** | Japan repatriation flows | USD/JPY, GPIF/Lifer positioning, JGB 30Y |
| **REGINALD** | Bank funding stress | FHLB advances, CLO spreads, BDC transmission |
| **HENRY** | Market structure | VaR shocks, Treasury cascade → equity |

**REGINALD linkage:** BDC→FHLB transmission pathway identified. Trigger: CLO AAA >150bps (currently 115bps, 35bps cushion).

---

## FLOWS STATUS

| Flow | Speed | Status | Trigger |
|------|-------|--------|---------|
| RRP Depletion Cascade | Hours-Days | **ARMED** | Any flow shock |
| Basis Trade Unwind | Hours | **ARMED** | MMF redemptions |
| SRF Ceiling Breach | Hours | **CONFIRMED** | Quarter-end + demand |
| Japan Repatriation | Days | LATENT | USD/JPY >160, BOJ |
| TGA Drain | Days | LATENT | April tax season |
| Auction Failure | Hours | LATENT | BTC <2.0x, Tail >3bps |

---

## PREDICTIONS (Falsifiable)

| # | Prediction | Timeframe | Confidence |
|---|------------|-----------|------------|
| 1 | SOFR-IORB spread stays <+10bps absent shock | Q1 2026 | 80% |
| 2 | SRF usage >$50B at March quarter-end | Mar 31, 2026 | 70% |
| 3 | RRP stays <$50B through H1 2026 | H1 2026 | 85% |
| 4 | No auction failure (BTC >2.0x) in Q1 | Q1 2026 | 75% |
| 5 | Warsh confirmation delayed or blocked | H1 2026 | 55% |
| 6 | Reserve balances drop below $2.8T | Q2 2026 | 60% |

---

## DANGER WINDOWS

**Q1 2026 (Current):**
- Feb: Refunding announcement, auction calendar heavy
- Mar 31: Quarter-end — SRF breach risk

**Q2 2026:**
- April: Tax season — TGA rebuild drains reserves
- May: Powell term ends — Fed leadership transition
- Warsh confirmation hearings (if scheduled)

**Structural (Ongoing):**
- Any Japan repatriation wave (SAM monitors)
- Any MMF redemption event (basis trade trigger)
- Any geopolitical shock requiring safe-haven flows

---

## WHAT TO WATCH

**Daily:**
- SOFR rate and spread to IORB
- RRP operation results
- SRF usage (if any)

**Weekly:**
- Treasury auction results (especially 7Y tenor)
- Dealer positioning (FR 2004)
- Reserve balances (H.4.1)

**Event-driven:**
- Fed communications on balance sheet
- Warsh confirmation news
- Japan BOJ policy signals
- Quarter-end funding stress

---

## KEY DOCS
- ML-LIQ-004 through 007: Core research validating thesis
- ML-LIQ-018: 7Y Auction Playbook
- ML-LIQ-022-024: Warsh integration
- FLOW-LIQUID-1.01: RRP Depletion Cascade
- Research: "The Vanishing Buffer" (RRP depletion analysis)

---

## BOTTOM LINE

The funding market is a bomb with the safety removed. The fuse isn't lit — Fed intervention (RMP, SRF) is holding things together. But:

1. **Buffer = zero** — No shock absorption capacity
2. **Dealers clogged** — No market-making elasticity  
3. **$1.85T basis trade** — Transmission mechanism armed
4. **Warsh nomination** — Fed willingness to intervene may decline

System is stable **until it isn't**. When stress hits, it will transmit faster than historical precedent because the RRP cushion that existed in 2020-2023 is gone.

*Next update trigger: Quarter-end (Mar 31) or SOFR-IORB >+10bps*
