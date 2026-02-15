# SAM Research Status Index

**Updated:** 2026-01-25
**Session:** SAM-XII (004)
**Purpose:** Track research thread status to prevent re-investigation

---

## Status Categories

| Status | Meaning |
|--------|---------|
| EXHAUSTED | OSINT exhausted - do not re-investigate without new external lead |
| COMPLETE | Fully documented - monitor for news only |
| ACTIVE | Currently investigating or watching for triggers |
| DORMANT | Paused pending external development |
| GAPS | Known unknowns that could be researched |
| TERMINAL | Requires Bloomberg/terminal access - cannot research via OSINT |

---

## EXHAUSTED THREADS

| Thread | Summary | Date Closed | Unlock Condition |
|--------|---------|-------------|------------------|
| Norinchukin Acute Crisis | FY25 loss absorbed; back to profit; CLO portfolio shrinking | 2026-01-23 | New capital breach signal or CLO sale >¥500B |
| BOJ Jan 23-24 Decision | Held 0.75% (8-1); Takata dissented; absorbed without panic | 2026-01-24 | Next meeting April 2026 |

---

## COMPLETE THREADS

| Thread | Summary | Documentation |
|--------|---------|---------------|
| 20Y JGB Auction Failure | Worst since 1987; triggered fiscal doom loop | ML-JPN-130, FL-JPN-060 |
| Takaichi Fiscal Platform | ¥122.3T budget, 0% food tax, Sanaeconomics | ML-JPN-133 |
| Life Insurer Aggregate Losses | ¥9.83T+ Big 4 combined; ¥27.2T bonds 30%+ underwater | ML-JPN-135, ML-JPN-141 |
| BOJ QT Status | $502B cut; holdings at 48% (8-year low) | ML-JPN-143 |
| Foreign JGB Flows | Flipped to net sellers | ML-JPN-140 |
| RRP Depletion | Near zero; buffer gone | ML-JPN-145 |
| Mar-a-Lago Accord Mechanics | Miran paper: tariffs first, accord second; TD says "non-starter"; full implementation unlikely | ML-JPN-150, ML-JPN-151 |
| NY Fed Rate Check History | 3 US interventions since 1996; 1998 coordination lasted >10 days; success requires policy backup | ML-JPN-153 |
| China Yuan Policy | PBOC managing independently; allowing gradual appreciation; NOT coordinating with US | ML-JPN-152 |

---

## ACTIVE THREADS

| Thread | Focus | Next Action |
|--------|-------|-------------|
| Feb 5 30Y Auction | Pre-election signal | Monitor MOF results |
| Feb 8 Election | LDP seat count (not just win/lose) | Monitor exit polls |
| Feb 19 20Y Auction | Test if Jan 20 failure was pattern | Monitor MOF results |
| Katayama Intervention | Verbal → actual? Credibility test at 158-162 | Monitor USD/JPY |
| Post-BOJ Reaction | Stabilization holding through Jan 27? | Monitor yields daily |
| US-Japan Coordination | Rate check → actual intervention? | Watch for MOF/Treasury action |
| Jan 29 7Y UST Auction | LIQUID primary; SAM monitors Japan signals | Coordinate with LIQUID |
| Campaign Fiscal Escalation | Competing promises Jan 27-Feb 8 | Monitor NHK, candidate speeches |

---

## DORMANT THREADS

| Thread | Waiting For | Last Checked |
|--------|-------------|--------------|
| CLO Nuclear (FLOW-JPN-3.01) | CLO AAA >150bps OR Norinchukin capital breach | 2026-01-24 (125bps, stable) |
| GPIF Mechanical Rebalancing | USD/JPY >160 | 2026-01-25 (154.71 — 5+ handles cushion) |
| SoftBank Amplifier | Arm <80 OR spreads >500bps | Not recently checked |
| China/Taiwan Escalation | Geopolitical trigger | Not recently checked |
| US Recession Trigger | PMI <45, unemployment >5.5% | Not recently checked |

---

## GAPS (Known Unknowns)

### TERMINAL REQUIRED (Cannot fill via OSINT)

| Gap | Why It Matters | Data Source | Priority |
|-----|----------------|-------------|----------|
| **Japan 5Y CDS** | Direct market pricing of fiscal stress | Bloomberg, WorldGovBonds | HIGH |
| **CCY Basis (USD/JPY)** | Forced-selling indicator; our -45bps is stale | Bloomberg, Refinitiv | HIGH |
| **JGB Futures Positioning** | CFTC-equivalent for Japan | Bloomberg, JPX | MEDIUM |
| **OIS Rate Expectations** | Market pricing for April/June BOJ | Bloomberg | MEDIUM |

### RESEARCH NEEDED (Could investigate)

| Gap | Why It Matters | Approach | Priority |
|-----|----------------|----------|----------|
| **Regional Bank Specific Exposure** | "Record losses" confirmed but unquantified | Japanese sources (Nikkei, BOJ FSR) | HIGH |
| **Life Insurer Individual Actions** | Big 4 strategies diverging (HTM vs selling) | Earnings calls, Japanese press | MEDIUM |
| **GPIF Current Positioning** | Hedge ratio, actual UST exposure | GPIF quarterly reports | MEDIUM |
| **Mega-Bank JGB Appetite** | SMFG "preparing to buy" - others? | Japanese bank earnings, press | MEDIUM |
| **Shunto Wage Negotiations** | Spring 2026 - BOJ watches closely | Japanese labor news | LOW |
| **District-Level Election Polling** | National polls may miss seat dynamics | Japanese polling aggregators | LOW |
| **Intervention Follow-Through** | Will rate check be backed by action? | Watch MOF/Treasury statements | HIGH — WATCH |

### RECENTLY COMPLETED (SAM-XII)

| Gap | Finding | Documentation |
|-----|---------|---------------|
| Mar-a-Lago Accord mechanics | Miran paper: tariffs first, accord second; TD: "non-starter" | ML-JPN-150, ML-JPN-151 |
| China yuan response | PBOC managing independently; not coordinating with US | ML-JPN-152 |
| NY Fed rate check precedent | 3 interventions since 1996; 1998 coordination effective | ML-JPN-153 |

### CROSS-DOMAIN COORDINATION NEEDED

| Gap | Coordinating Agent | Signal Type |
|-----|-------------------|-------------|
| US Funding Stress Details | LIQUID | FTD, SOFR spikes, FHLB |
| US Regional Bank CLO Holdings | REGINALD | BDC credit lines, bank stress |
| Global Liquidity Synthesis | MASTER | Cross-domain escalation |

---

## SIGNALS SENT TO OTHER AGENTS

| Date | To | Signal | Status |
|------|-----|--------|--------|
| 2026-01-23 | CARL | Japan life insurer UST repatriation reducing global demand | SENT |
| 2026-01-24 | LIQUID | Treasury FTD at 8-year high; RRP depleted | PENDING |
| 2026-01-25 | LIQUID | Pre-auction ACK; Japan monitoring for Jan 29 7Y; current state update | SENT |
| 2026-01-26 | SHARED_INTEL (ALL) | **ALERT: Bonds Before Currency** — Framework shift; JGB primary vector, FX secondary | SENT |
| 2026-01-26 | LIQUID | Jan 29 7Y auction context; Japan transmission framework; Feb 5 trigger added | SENT |
| 2026-01-26 | HENRY | Japan 1989 parallels ACK; incorporated as amplifier; feedback loop identified | SENT |

---

## THRESHOLDS TO ADD (From Gap Analysis)

| Metric | Current | Yellow | Orange | Red | Source |
|--------|---------|--------|--------|-----|--------|
| Japan 5Y CDS | UNKNOWN | 50bps | 75bps | 100bps | Needs terminal |
| Treasury FTD | $30.5B (Dec) | $40B | $45B | $50B | DTCC |

---

*Check this file before suggesting any research direction.*
*Last updated: 2026-01-25 SAM-XII*
