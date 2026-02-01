# LIQUID Research Status

**Updated:** 2026-01-25

---

## EXHAUSTED RESEARCH

*Before suggesting new research, check if topic is already covered here.*

### Completed Topics

| # | Topic | Completion Date | Key Findings | Output Location |
|---|-------|-----------------|--------------|-----------------|
| 01 | RRP Depletion Mechanics | 2026-01-25 | RRP depleted ($2.5B). Fed started RMP $40B/mo. Central Bank Balance Sheet Trilemma. System Fed-dependent. | research/RESEARCH_RESULTS/ |
| 02 | SOFR Stress Episodes | 2026-01-25 | SRF is porous ceiling (Dec 31 breach +12bps). GSIB constraints binding. Sawtooth pattern is new normal. | research/RESEARCH_RESULTS/ |
| 03 | Treasury Auction Health | 2026-01-25 | Thresholds validated: BTC <2.30x Yellow, <2.10x Orange. Tail is most immediate signal. 7Y most fragile. | research/RESEARCH_RESULTS/ |
| 04 | FTD Settlement Patterns | 2026-01-25 | $42.4B = Yellow. Driven by scarcity + clearing transition. Monitor aged fails ratio. | research/RESEARCH_RESULTS/ |
| 05 | MMF Post-RRP Deployment | 2026-01-25 | $2.5T rotated to T-bills ($3.5T) + repo ($3.0T). MMF→HF basis trade transmission risk ($1.85T). | research/RESEARCH_RESULTS/ |

### Known Data Gaps

| Topic | Gap Description | Alternative |
|-------|-----------------|-------------|
| Intraday SOFR | No OSINT real-time | Use daily NY Fed |
| Dealer positioning | Terminal only | Use FR 2004 weekly (undervalued per research) |
| CCY basis real-time | Terminal only | Use FX forward points |
| Bank reserve levels | Delayed/terminal | Use Fed H.4.1 weekly |
| Real-time HF leverage | SEC Form PF lagged months | Use futures open interest as proxy |
| Bilateral repo opacity | Non-centrally cleared bilateral (NCCBR) opaque | Wait for clearing mandate |
| MMF shareholder concentration | No real-time data | Monitor flows via ICI weekly |

---

## TOPICS COVERED BY PEER AGENTS

*Do NOT duplicate this research — receive via inter-agent signals instead.*

| Topic | Agent | Notes |
|-------|-------|-------|
| Japan repatriation flows | SAM | SAM's primary domain |
| GPIF/Lifer UST holdings | SAM | SAM tracks Japan institutional behavior |
| Japan institutional behavior | SAM | SAM monitors BOJ, lifers, GPIF |
| FHLB advance rates | REGINALD | REGINALD tracks bank funding stress |
| Regional bank deposits | REGINALD | REGINALD's primary domain |
| CLO/BDC transmission | REGINALD | REGINALD tracks credit transmission |
| Bank funding stress | REGINALD | REGINALD monitors via KRE, CRE DQ |

**Protocol:** When these topics are relevant to LIQUID thesis, check peer agent inboxes or request signal via AGENT_COMMS.

---

## ACTIVE RESEARCH PROMPTS

*All initial research prompts COMPLETE. See `research/RESEARCH_INDEX.md` for original prompts.*

| # | Topic | Vector | Priority | Status |
|---|-------|--------|----------|--------|
| 01 | RRP Depletion Mechanics | VX-LIQUID-1.02 | HIGH | **COMPLETE** |
| 02 | SOFR Stress Episodes | VX-LIQUID-1.01 | HIGH | **COMPLETE** |
| 03 | Treasury Auction Health | VX-LIQUID-2.01/2.02 | MEDIUM | **COMPLETE** |
| 04 | FTD Settlement Patterns | VX-LIQUID-1.03 | MEDIUM | **COMPLETE** |
| 05 | MMF Deployment Post-RRP | VX-LIQUID-1.02 | HIGH | **COMPLETE** |

---

## RESEARCH QUEUE (Future)

| Priority | Topic | Expected Source | Status | Notes |
|----------|-------|-----------------|--------|-------|
| MEDIUM | Central clearing transition impact | FICC/DTCC | FUTURE | Monitor as June 2027 mandate approaches |
| LOW | Fed SRF usage history | NY Fed | FUTURE | Build historical dataset |
| LOW | TGA dynamics | Treasury | FUTURE | Supply-side research |
| LOW | Dealer balance sheet constraints | Public filings | FUTURE | Complex, may be terminal-only |
| LOW | GSIB surcharge mechanics | Fed/BIS | FUTURE | Understand "cliff effect" better |

---

## KEY RESEARCH FINDINGS SUMMARY

### Thesis Validation
- **Funding Market Fragility thesis CONFIRMED**
- Confidence upgraded: Pattern 90% | Timing 70% | Magnitude 85%

### Critical Discoveries

1. **SRF is a Porous Ceiling**
   - Dec 31, 2025: SOFR 3.87% vs SRF 3.75% (+12bps breach)
   - GSIB constraints prevent arbitrage even at profitable spreads
   - Non-dealers cannot access SRF directly

2. **Central Bank Balance Sheet Trilemma**
   - Fed can only achieve 2 of 3: small balance sheet, low volatility, limited intervention
   - Fed chose #2 & #3, abandoning #1
   - RMP ($40B/mo) = de facto balance sheet expansion

3. **MMF → Hedge Fund Transmission**
   - $2.5T RRP rotated to: ~$3.5T T-bills + ~$3.0T private repo
   - MMFs directly fund $1.85T basis trade via FICC Sponsored Repo
   - Cascade risk: MMF stress → repo pullback → forced HF unwind → Treasury selling

4. **Dealer Capacity is Binding Constraint**
   - FR 2004 Net Positioning >$200B = critical indicator
   - SLR prevents dealers from intermediating even at profitable spreads

### New Vectors Added
- VX-LIQUID-1.04: SRF Usage
- VX-LIQUID-1.05: Dealer Net Position
- VX-LIQUID-1.06: Sponsored Repo Volume
- VX-LIQUID-2.03: Auction Tail
- VX-LIQUID-5.01: MMF WAM
- VX-LIQUID-5.02: Basis Trade Exposure

### New Flows Added
- FLOW-LIQUID-2.02: Basis Trade Unwind Cascade
- FLOW-LIQUID-3.01: SRF Ceiling Breach
- FLOW-LIQUID-3.02: Auction Failure Cascade
- FLOW-LIQUID-4.01: TGA Drain Cascade

---

*LIQUID Research Status v2.0 | Updated with completed research, new vectors, thesis validation*
