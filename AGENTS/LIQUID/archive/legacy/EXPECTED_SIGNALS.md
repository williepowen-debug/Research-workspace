# LIQUID Expected Signals

**Purpose:** Pre-document expected signal types so they are recognized when they occur.

**Updated:** 2026-01-25 (v2.0 - Added new vectors from research)

---

## Funding Stress Signals

### SOFR Spike

**What it looks like:**
- SOFR-IORB spread >+5bps (Yellow), >+15bps (Orange), >+25bps (Red)
- Typically occurs at quarter-end, month-end, or during flow shocks
- **NEW:** Can breach SRF rate during GSIB-constrained periods (Dec 31 2025: +12bps above SRF)

**Causes:**
- RRP depletion removing buffer (CONFIRMED - now at $2.5B)
- Large Treasury settlement or TGA rebuild
- Foreign selling (Japan repatriation)
- Dealer balance sheet constraints (SLR)
- GSIB Method 2 scoring at quarter/year-end

**Response:**
- Alert SAM and REGINALD
- Monitor SRF usage (H.4.1 weekly)
- Check dealer net positions (FR 2004)
- Expect "sawtooth" pattern at quarter-ends

---

### SRF Usage Spike (NEW)

**What it looks like:**
- SRF usage >$25B sustained (Yellow), >$50B sustained (Orange), >$75B (Red)
- Usage outside quarter-end windows is more concerning than quarter-end spikes

**Causes:**
- Private repo market liquidity exhausted
- Dealers constrained by SLR/GSIB
- Non-dealers forced to pay penalty rates

**Response:**
- Confirm whether quarter-end (expected) or mid-month (concerning)
- Monitor SOFR-SRF spread (if SOFR > SRF rate = ceiling breach)
- Check dealer inventories

**Historical Reference:**
- Dec 31, 2025: Record $74.6B usage, SOFR breached SRF by +12bps

---

### RRP Surge/Collapse

**What it looks like:**
- RRP balance moves significantly ($50B+ daily change)
- Currently at floor (~$2.5B) so surge more likely than collapse

**Causes:**
- MMF cash deployment changes
- T-bill supply dynamics
- Quarter-end window dressing

**Response:**
- Update VX-LIQUID-1.02
- If rising: buffer rebuilding (positive)
- If falling further: immaterial (already at zero)

---

### Treasury Auction Stress

**What it looks like:**
- BTC <2.30x (Yellow), <2.10x (Orange), <2.00x (Red)
- **Tail >1.5bps (Yellow), >3.0bps (Orange), >5.0bps (Red)** — Most immediate signal
- Indirect bid <60% (Yellow), <55% (Orange), <40% (Red)
- Dealer takedown >25% for long-end auctions

**Causes:**
- Foreign buyer withdrawal (Japan, China)
- Dealer capacity constraints
- Supply/demand imbalance
- Repo funding stress

**Response:**
- Alert SAM (foreign demand signal)
- Document in ML
- Watch subsequent auctions for pattern
- **7Y tenor historically most fragile** (Feb 2021 failure: BTC 2.04x, Tail +4.2bps)

**Historical Reference:**
- Feb 2021 7Y failure: BTC 2.04x, Tail +4.2bps, Indirect 38%
- Jan 2026 10Y: BTC 2.55x, Indirect 69.5%, stopped through (healthy)

---

### Auction Tail Stress (NEW)

**What it looks like:**
- Tail = Auction High Yield - When-Issued Yield at 1:00 PM
- Positive tail = weak demand (dealers demanded concession)
- Negative tail (stop-through) = strong demand

**Thresholds:**
- >1.5bps: Yellow — Indigestion
- >3.0bps: Orange — Significant stress
- >5.0bps: Red — Market dysfunction (Feb 2021 had +4.2bps)

**Response:**
- Immediate post-auction volatility likely if tail >2bps
- Watch secondary market bid-ask spreads
- Monitor dealer positions

---

### FHLB Stress

**What it looks like:**
- Advance rate >75% (Yellow), >85% (Orange), "Delivery" issues (Red)
- FHLB debt issuance surge
- Regional bank funding headlines

**Causes:**
- Bank deposit outflows
- Regional bank funding needs
- Credit stress transmission (BDC→Bank path per REGINALD)

**Response:**
- Alert REGINALD immediately
- Monitor for systemic implications
- Check CLO AAA spreads (trigger at >150bps)

---

### Sponsored Repo Contraction (NEW)

**What it looks like:**
- FICC Sponsored Repo volume decline (plateau at Yellow, -$100B/week at Orange)
- Indicates dealer capacity hit or hedge fund deleveraging

**Causes:**
- Netting constraints saturated
- Dealers reducing intermediation
- Hedge funds reducing leverage

**Response:**
- Cross-reference with SOFR stress
- Check basis trade indicators
- Monitor for forced Treasury selling

---

### MMF WAM Shortening (NEW)

**What it looks like:**
- Weighted Average Maturity declining rapidly
- <30 days (Yellow), <20 days (Orange), <15 days (Red)

**Causes:**
- MMF managers hoarding liquidity
- Anticipation of redemptions or volatility
- Defensive positioning

**Response:**
- Leading indicator of stress
- If combined with SOFR spike = basis trade unwind risk
- Monitor MMF flow data (ICI weekly)

---

### Basis Trade Unwind Signals (NEW)

**What it looks like:**
- Sponsored repo volume declining
- MMF WAM shortening
- SOFR spiking
- Treasury cash/futures basis collapsing
- Large Treasury selling volume

**The Cascade:**
```
MMF stress → Stop rolling repo → HF loses funding →
Forced basis unwind → Treasury selling → Price crash
```

**Response:**
- This is a HOURS-speed cascade
- Alert SAM and REGINALD immediately
- Monitor for Fed intervention signals

---

## Cross-Border Signals

### CCY Basis Widening

**What it looks like:**
- USD/JPY basis >-60bps (Yellow), >-75bps (Orange), >-100bps (Red)
- Indicates USD funding stress for Japanese institutions

**Causes:**
- Japan repatriation pressure
- FX hedging cost spike
- Dollar shortage

**Response:**
- Coordinate with SAM on Japan dynamics
- Watch for forced UST selling

---

### FTD Spike

**What it looks like:**
- FTD >$50B (Orange), >$60B (Red)
- Concentrated in specific maturities (on-the-run issues)
- Rising aged fails ratio (>30 days)

**Causes:**
- Settlement infrastructure stress
- Short selling pressure / basis trade
- Delivery squeeze
- Central clearing transition friction

**Response:**
- Document in ML
- Check if broad-based (systemic) or specific CUSIP (technical)
- Monitor aged fails ratio for deterioration

---

## Credit Transmission Signals (NEW)

### CLO AAA Spread Widening

**What it looks like:**
- CLO AAA >130bps (Yellow), >150bps (Orange), >175bps (Red)
- Currently 115bps (35bps cushion to trigger)

**Causes:**
- Credit cycle deterioration
- Risk-off sentiment
- Recession indicators

**Transmission (per REGINALD):**
```
CLO spreads widen → BDC portfolios mark down →
BDCs draw bank credit ($142B) → Regional bank liquidity drain →
FHLB advance surge → FHLB stress
```

**Response:**
- This is REGINALD's primary domain
- LIQUID monitors as FHLB transmission trigger
- If >150bps, escalate FHLB monitoring to ORANGE

---

## Transmission Signals (From Coordinating Agents)

### From SAM

| Signal | Meaning | LIQUID Response |
|--------|---------|-----------------|
| JGB 30Y >4.00% | Bond crisis acute | Prepare for repatriation flow |
| USD/JPY >160 | GPIF trigger | Watch UST selling pressure |
| BOJ emergency | Policy intervention | Heighten monitoring |
| Japan repatriation imminent | $60-100B flow | CRISIS session, hourly SOFR watch |

### From REGINALD

| Signal | Meaning | LIQUID Response |
|--------|---------|-----------------|
| KRE -15% | Regional bank stress | Watch FHLB advance rate |
| CLO AAA >150bps | Credit transmission trigger | Escalate FHLB to ORANGE |
| BDC NAV <-20% | BDC stress acute | Monitor bank credit draws |
| Deposit flight | Bank run signals | Prepare for FHLB stress |

---

## Counter-Signals (Stabilization)

| Signal | Meaning | Implication |
|--------|---------|-------------|
| RRP rising from floor | MMF cash returning | Buffer rebuilding |
| SOFR-IORB narrowing | Funding easing | Stress abating |
| Strong auction BTC | Demand healthy | Foreign bid intact |
| Fed SRF usage declining | Backstop less needed | Private market healing |
| Fed accelerates RMP | Policy response | More liquidity incoming |
| Sponsored repo volume rising | Intermediation healthy | Transmission channel open |
| MMF WAM extending | Confidence returning | Less defensive positioning |

---

## Seasonal/Calendar Signals (Expected Volatility)

| Date | Event | Expected Impact |
|------|-------|-----------------|
| Month-end | Window dressing | SOFR +5-10bps, elevated but normal |
| Quarter-end | GSIB constraints | SOFR +10-20bps, SRF usage spike |
| Year-end | GSIB Method 2 | SOFR can breach SRF, expect $50B+ SRF |
| Tax dates (Apr 15, Jun 15, Sep 15) | TGA drain | Reserve pressure, SOFR stress |
| Large auction settlements | Dealer funding need | Temporary SOFR pressure |

---

*LIQUID Expected Signals v2.0 | Updated with research findings and new vectors*
