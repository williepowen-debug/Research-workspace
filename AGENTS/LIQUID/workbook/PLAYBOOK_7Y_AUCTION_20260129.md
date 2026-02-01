# PLAYBOOK: Jan 29, 2026 — 7-Year Note Auction

**Event:** 7-Year Treasury Note Auction
**Size:** ~$44 billion
**Time:** 1:00 PM ET (results available shortly after)
**Risk Level:** CRITICAL

---

## CONTEXT

### Why This Auction Matters

1. **Historical Precedent:** The 7Y tenor failed catastrophically in Feb 2021
   - BTC: 2.04x (worst since 2009)
   - Tail: +4.2bps (massive concession)
   - Indirect: 38.06% (foreign buyers fled)
   - Result: 10Y yield spiked 15bps in hours, risk-off cascade

2. **Current Vulnerabilities:**
   - RRP depleted ($1.96B) — no buffer for shock absorption
   - Dealers stuffed (~$200B net long) — limited capacity to absorb weak auction
   - Reserves declining ($2.954T, -$95B WoW) — liquidity tightening

3. **Positive Factors:**
   - Jan 13 10Y auction was strong (BTC 2.554x, stopped through)
   - SOFR-IORB normalized to -1bp (funding stable)
   - Foreign demand robust at recent auctions (69.5% indirect)

---

## METRICS TO WATCH

Results available at ~1:05 PM ET from TreasuryDirect.

| Metric | Definition | Where to Find |
|--------|------------|---------------|
| **Bid-to-Cover (BTC)** | Total bids / Amount offered | TreasuryDirect results |
| **High Yield** | Auction clearing yield | TreasuryDirect results |
| **Tail** | High Yield - When-Issued (1:00 PM) | Calculate from Bloomberg/market data |
| **Indirect Bid %** | Foreign/institutional demand proxy | TreasuryDirect results |
| **Direct Bid %** | Domestic institutional demand | TreasuryDirect results |
| **Dealer Takedown** | Primary dealer absorption | TreasuryDirect results |

### Baseline Expectations (6-Month Averages for 7Y)
- BTC: ~2.50-2.60x
- Indirect: ~65-70%
- Direct: ~18-22%
- Dealers: ~10-15%

---

## SCENARIO 1: GREEN — Strong Auction

### Metrics
| Metric | Value | Signal |
|--------|-------|--------|
| BTC | >2.40x | Strong demand |
| Tail | Stopped through or <1.0bps | Excellent bid |
| Indirect | >65% | Foreign demand intact |
| Dealer | <15% | Minimal forced absorption |

### Interpretation
Market absorbed supply easily. Foreign demand remains robust. No stress transmission.

### Actions
1. **Log to ML.tsv:** "Jan 29 7Y auction strong. System passed stress test."
2. **Update VX.tsv:** Confirm GREEN status for auction vectors
3. **No signals required** to SAM/REGINALD
4. **Monitoring:** Return to normal weekly cadence

### Follow-Up
- Continue standard monitoring
- Focus shifts to Feb 4 QRA announcement
- Check H.4.1 and FR 2004 on Jan 30 as scheduled

---

## SCENARIO 2: YELLOW — Soft but Acceptable

### Metrics
| Metric | Value | Signal |
|--------|-------|--------|
| BTC | 2.20-2.40x | Below average but acceptable |
| Tail | 1.0-2.0bps | Mild concession |
| Indirect | 58-65% | Some foreign hesitation |
| Dealer | 15-22% | Elevated but manageable |

### Interpretation
Demand softer than recent auctions but within historical norms. Not a failure, but a warning sign. Market digested supply with some friction.

### Actions
1. **Log to ML.tsv:** "Jan 29 7Y auction soft. BTC [X], Tail [X]bps, Indirect [X]%. Elevated dealer takedown."
2. **Update VX.tsv:**
   - VX-LIQUID-2.01 (BTC) → YELLOW if <2.30x
   - VX-LIQUID-2.03 (Tail) → YELLOW if >1.5bps
3. **Monitor secondary market:** Watch bid-ask spreads, 7Y yield movement
4. **Prepare contingency:** Draft signal template for SAM/REGINALD (not sent yet)

### Follow-Up
- **Daily monitoring** through Feb 4 QRA
- Watch for pattern: If Feb 10 3Y or Feb 11 10Y also soft → escalate to ORANGE
- Check SOFR for any post-auction pressure

### Signal Template (Prepare, Do Not Send)
```
Priority: ELEVATED (not sent)
Topic: 7Y Auction Soft — Pattern Watch
Content: Jan 29 7Y showed [metrics]. Single datapoint, not crisis.
         Monitoring for pattern across Feb auctions.
```

---

## SCENARIO 3: ORANGE — Weak Auction

### Metrics
| Metric | Value | Signal |
|--------|-------|--------|
| BTC | 2.00-2.20x | Weak demand |
| Tail | 2.0-4.0bps | Significant concession |
| Indirect | 50-58% | Foreign pullback |
| Dealer | 22-30% | Stressed absorption |

### Interpretation
Demand failed to materialize. Dealers forced to absorb significant share. Foreign buyers demanding higher yields. This is a stress signal but not yet a crisis.

### Actions
1. **Log to ML.tsv:** "Jan 29 7Y auction WEAK. BTC [X], Tail [X]bps, Indirect [X]%. Dealer takedown [X]%. ORANGE alert."
2. **Update VX.tsv:**
   - VX-LIQUID-2.01 (BTC) → ORANGE
   - VX-LIQUID-2.03 (Tail) → ORANGE
   - VX-LIQUID-2.02 (Indirect) → YELLOW or ORANGE
3. **Send ELEVATED signal to SAM:**
   ```yaml
   signal:
     from: LIQUID
     to: SAM
     priority: ELEVATED
     topic: "7Y Auction Weak — Foreign Demand Signal"
     content: |
       Jan 29 7Y auction showed stress:
       - BTC: [X] (weak)
       - Indirect: [X]% (foreign pullback)
       - Tail: +[X]bps (concession demanded)

       Possible Japan/foreign rotation beginning.
       SAM should monitor for correlated signals.
   ```
4. **Send ELEVATED signal to REGINALD:**
   ```yaml
   signal:
     from: LIQUID
     to: REGINALD
     priority: ELEVATED
     topic: "Auction Stress — Dealer Capacity Watch"
     content: |
       Jan 29 7Y auction weak. Dealer takedown [X]%.
       With dealers already net long ~$200B, capacity constraint binding.
       Watch for bank funding stress if pattern continues.
   ```
5. **Monitor SOFR:** Check for post-auction spike
6. **Prepare crisis protocol** for potential Feb auction failures

### Follow-Up
- **Hourly SOFR monitoring** for next 24 hours
- Watch secondary market for yield spillover to 10Y, 30Y
- H.4.1 on Jan 30 becomes CRITICAL (SRF usage)
- FR 2004 on Jan 30 becomes CRITICAL (dealer positioning)
- Prepare for potential CRISIS session if Feb auctions also fail

---

## SCENARIO 4: RED — Failed Auction / Crisis

### Metrics
| Metric | Value | Signal |
|--------|-------|--------|
| BTC | <2.00x | Demand failure |
| Tail | >4.0bps | Extreme concession |
| Indirect | <50% | Foreign flight |
| Dealer | >30% | Dealers overwhelmed |

### Interpretation
**This is a Feb 2021-style failure.** Market cannot absorb Treasury supply at current yields. Foreign buyers have retreated. Dealers forced into distressed absorption. Expect:
- Immediate yield spike across curve
- VaR shocks triggering risk-off
- Potential basis trade stress (MMF→HF transmission)
- SOFR pressure within hours

### Actions

#### IMMEDIATE (Within 30 Minutes of Results)

1. **Log to ML.tsv:**
   ```
   CRISIS: Jan 29 7Y auction FAILED. BTC [X], Tail +[X]bps, Indirect [X]%.
   Activating crisis protocol. Hourly monitoring initiated.
   ```

2. **Update VX.tsv:**
   - VX-LIQUID-2.01 (BTC) → **RED**
   - VX-LIQUID-2.03 (Tail) → **RED**
   - VX-LIQUID-2.02 (Indirect) → **RED** or **ORANGE**

3. **Send URGENT signal to SAM:**
   ```yaml
   signal:
     from: LIQUID
     to: SAM
     priority: URGENT
     topic: "7Y AUCTION FAILED — Crisis Protocol"
     content: |
       URGENT: Jan 29 7Y auction failed (Feb 2021 template).
       - BTC: [X] (<2.00x)
       - Tail: +[X]bps (>4bps)
       - Indirect: [X]% (foreign flight)

       Expect Treasury yield spike, risk-off cascade.
       Japan repatriation pressure may accelerate.
       Coordinate on foreign flow monitoring.
   ```

4. **Send URGENT signal to REGINALD:**
   ```yaml
   signal:
     from: LIQUID
     to: REGINALD
     priority: URGENT
     topic: "7Y AUCTION FAILED — Bank Stress Watch"
     content: |
       URGENT: Jan 29 7Y auction failed.
       Dealer takedown [X]% — balance sheets maxed.

       Watch for:
       - SOFR spike → Bank funding cost surge
       - FHLB advance demand
       - CLO AAA spread widening

       BDC→Bank transmission risk elevated.
   ```

5. **Initiate CRISIS Session:**
   - Switch to **hourly monitoring cadence**
   - Monitor SOFR in real-time if possible
   - Watch for Fed communication/intervention signals

#### WITHIN 2 HOURS

6. **Check SOFR:** Any spike >+5bps above IORB = FLOW-LIQUID-1.01 activating
7. **Check basis trade indicators:** Futures/cash spread, sponsored repo volume
8. **Check MMF flows:** Any signs of redemption pressure
9. **Monitor Fed Desk:** Watch for emergency repo operations

#### WITHIN 24 HOURS

10. **H.4.1 check** (if available): SRF usage spike = confirmation
11. **Prepare Feb auction contingency:** Feb 2 20Y, Feb 4 QRA become critical
12. **Document cascade evidence:** Which transmission paths activating

### Follow-Up
- **CRISIS session until stabilization**
- Continuous SOFR/funding market monitoring
- Coordinate with SAM on Japan flow data
- Coordinate with REGINALD on bank stress data
- Watch for Fed policy response (emergency repo, RMP acceleration, communication)

---

## DECISION TREE

```
                    Jan 29 7Y Auction Results (1:00 PM ET)
                                    |
                    ----------------+----------------
                    |               |               |
              BTC >2.40x      BTC 2.20-2.40x   BTC <2.20x
              Tail <1bp       Tail 1-2bps      Tail >2bps
                    |               |               |
                 GREEN           YELLOW            |
                    |               |               |
               Log only        Log + Watch    -----+-----
                                              |         |
                                        BTC 2.00-2.20   BTC <2.00
                                        Tail 2-4bps     Tail >4bps
                                              |              |
                                           ORANGE          RED
                                              |              |
                                        ELEVATED        URGENT
                                        signals         signals
                                              |              |
                                        Daily          CRISIS
                                        monitor        session
```

---

## POST-AUCTION CHECKLIST

### Immediate (Within 1 Hour)
- [ ] Record auction results in ML.tsv
- [ ] Determine scenario (GREEN/YELLOW/ORANGE/RED)
- [ ] Update VX.tsv if status changed
- [ ] Send signals if ORANGE or RED
- [ ] Check SOFR for immediate reaction

### End of Day
- [ ] Document secondary market reaction
- [ ] Check for yield curve spillover
- [ ] Note any Fed communication
- [ ] Update FL.tsv with next priorities

### Next Day (Jan 30)
- [ ] Check H.4.1 for SRF usage
- [ ] Check FR 2004 for dealer positioning
- [ ] Assess if pattern forming vs. isolated event
- [ ] Prepare for Feb 4 QRA

---

## HISTORICAL REFERENCE

### Feb 25, 2021 — 7Y Failure
| Metric | Value | Context |
|--------|-------|---------|
| BTC | 2.04x | Lowest since 2009 |
| Tail | +4.2bps | Massive concession |
| Indirect | 38.06% | Foreign flight |
| High Yield | 1.195% | 23bps above prior |

**Result:** 10Y yield spiked from 1.38% to 1.54% in 24 hours. Risk-off across assets. Fed had to signal patience to calm markets.

### Current Differences from Feb 2021
| Factor | Feb 2021 | Jan 2026 |
|--------|----------|----------|
| RRP Buffer | ~$200B | $1.96B (NONE) |
| Fed Policy | Accommodative | Neutral/tightening |
| Dealer Positioning | Normal | Stuffed (~$200B) |
| Foreign Demand Trend | Weakening | Strong (69.5% recent) |
| Basis Trade Size | ~$500B | $1.85T |

**Key Risk:** If auction fails, transmission will be faster and deeper due to:
1. No RRP buffer
2. Dealers already at capacity
3. Larger basis trade = larger unwind risk

---

## COMMUNICATION TEMPLATES

### SAM Signal (ORANGE)
```
File: C:/Projects/AGENT_COMMS/SAM_INBOX/2026-01-29_LIQUID_7Y_ELEVATED.md

# Signal: LIQUID → SAM
**Date:** 2026-01-29
**Priority:** ELEVATED
**Topic:** 7Y Auction Weak — Foreign Demand Signal

## Summary
Jan 29 7Y auction showed stress. Monitoring for Japan flow correlation.

## Metrics
- BTC: [X]
- Indirect: [X]%
- Tail: +[X]bps

## Request
Monitor for correlated Japan institutional signals.
```

### REGINALD Signal (ORANGE)
```
File: C:/Projects/AGENT_COMMS/REGINALD_INBOX/2026-01-29_LIQUID_7Y_ELEVATED.md

# Signal: LIQUID → REGINALD
**Date:** 2026-01-29
**Priority:** ELEVATED
**Topic:** Auction Stress — Dealer Capacity Watch

## Summary
7Y auction weak. Dealer balance sheet stress possible.

## Metrics
- Dealer Takedown: [X]%
- Net Position: ~$200B (already ORANGE)

## Request
Monitor FHLB advance rate and CLO AAA spreads.
```

### SAM Signal (RED/URGENT)
```
File: C:/Projects/AGENT_COMMS/SAM_INBOX/2026-01-29_LIQUID_7Y_URGENT.md

# Signal: LIQUID → SAM
**Date:** 2026-01-29
**Priority:** URGENT
**Topic:** 7Y AUCTION FAILED — Crisis Protocol

## Summary
CRISIS: 7Y auction failed. Feb 2021 template. Immediate coordination required.

## Metrics
- BTC: [X] (<2.00x)
- Indirect: [X]% (<50%)
- Tail: +[X]bps (>4bps)

## Transmission Risk
- Treasury yield spike underway
- Japan repatriation may accelerate
- Basis trade unwind risk elevated

## Request
Activate Japan flow monitoring. Coordinate on foreign selling signals.
```

---

*Playbook created: 2026-01-25*
*Valid for: Jan 29, 2026 7Y Auction*
*Review after: Auction results*
