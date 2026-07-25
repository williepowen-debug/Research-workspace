# First Brands / Point Bonita — WAL Fraud Vector 1
**Last Updated:** 2026-04-05

---

## The Fraud

**First Brands Group** — $9.3B debt auto-parts supplier. DOJ indicted **January 29, 2026**.

### Scheme
- Falsified financials
- Inflated invoices
- **Double-pledged collateral** — same assets pledged to multiple lenders simultaneously
- Former exec told judge the above under oath (Reuters, Feb 25 2026)

### Scale
- $9.3B total debt
- 15 BDCs hold $237M in exposure (ML-REG-078)
- DOJ criminal prosecution active

---

## WAL Exposure Path

```
First Brands (fraud) 
    → Leveraged fund (Jefferies-linked)
        → Jefferies as intermediary
            → WAL as lender to intermediary chain
```

WAL's exposure is **indirect but now quantified** — WAL lent to **LAM TFG I SPV LLC** (owned by Point Bonita master fund, within Jefferies' Leucadia Asset Management platform). Non-recourse to SPV collateral = First Brands receivables.

**WAL-specific dollar exposure:** **$126.4M disputed** (lawsuit filed Mar 6, 2026). $42.1M paid Jan 15 2026, then Jefferies refused further payments. Total original lending unknown but "steadily increasing amounts" since 2021.

### Structural Detail (from deep analysis, Mar 26 2026)

```
WAL (lender, non-recourse)
    → LAM TFG I SPV LLC (borrower, Point Bonita-owned)
        → Point Bonita master fund ($3B trade-finance, ~$715M First Brands = 25%)
            → Leucadia Asset Management (Jefferies platform)
                → First Brands Group (servicer, now bankrupt + DOJ indicted)
```

**Key structural failures:**
1. **UCC filings lapsed Sept 2025** — collateral perfection broken at critical moment
2. **Cash dominion misrepresentation** — First Brands retained control over collections despite contractual transfer to Point Bonita (per investor lawsuit Feb 25)
3. **No parent guarantee obtained** — WAL asked Jefferies + Point Bonita for guarantees during Oct 2025 forbearance, both refused
4. **Forbearance dispute** — WAL alleges Oct 2025 agreement required full repayment by **Mar 31, 2026** (THIS MONDAY). JEF says non-recourse, no obligation.
5. **Jefferies economic stake** — $43M (5.9% of Point Bonita's First Brands position) + ~$2M via Apex lending. Not merely a manager — skin in the game.

### 🔴 CATALYST: Mar 31 2026 — Alleged Forbearance Payment Deadline
The Oct 2025 forbearance agreement allegedly required full repayment by Mar 31, 2026. One $42.1M payment made Jan 15, then cut off. $126.4M remains disputed. This is the same convergence day as Japan FY-end, USDA Planting, Tricolor liquidation.

---

## Jefferies Confirmation

Jefferies Q1 CY2026 (reported Mar 25 2026 after close):
- **$17M in losses** from First Brands + MFS combined
- **$30M pretax loss Q4 CY2025** on First Brands (recognized earlier, Bloomberg Jan 7 2026)
- **$36M telecom writedown** + **24% decline in fixed income revenue** (per @junkbondinvest, Mar 26)
- EPS $0.70 vs consensus $0.91 — **23% miss**, driven by credit losses
- TBVPS $34.24, down **15.7% YoY** — balance sheet erosion
- Oppenheimer cut PT from $97 to $74 ahead of results

**Total JEF First Brands losses:** $30M (Q4) + portion of $17M (Q1) = **~$40-47M** and counting. Plus legal costs from dual lawsuits (WAL + investor class action).

**Significance:** If Jefferies is taking real P&L losses, WAL's exposure through the same chain is also real — not theoretical.

---

## Timeline

| Date | Event | Source |
|------|-------|--------|
| Oct 2025 | Bloomberg reports WAL faces First Brands risk | Bloomberg, ML-REG-088 |
| Jan 29 2026 | DOJ indicts First Brands | DOJ, ML-REG-078 |
| Feb 23 2026 | Blue Owl gates fund — cites First Brands + Tricolor bankruptcies | Bloomberg, ML-REG-070 |
| Feb 25 2026 | Jefferies sued; former exec confirms fraud to judge | Reuters, ML-REG-088 |
| Feb 27 2026 | WAL -10.64% Convergence Day; Jefferies -11% on MFS disclosure | Market data, ML-REG-096 |
| Mar 25 2026 | Jefferies Q1: $17M loss confirmed | Jefferies earnings, ML-REG-116 |
| Mar 6 2026 | WAL sues JEF for $126.4M (breach + fraud) | Reuters [1] |
| Mar 8-9 2026 | JEF disputes: "meritless," loans were non-recourse to SPV | Nasdaq [3] |
| Mar 25 2026 | Jefferies Q1: $17M loss + $36M telecom writedown + -24% FI rev | Bloomberg/JunkBondInvest |
| **Mar 31 2026** | **Alleged forbearance payment deadline — CONVERGENCE DAY** | |
| Jan-Feb 2026 | First Brands auction: Walbro sold for $50M (Overdrive Capital) | Kroll/Bloomberg |
| Mar 27 2026 | Brand portfolio (Fram, Autolite, Trico) sold for $25M (PGI Northstar) | Bloomberg |
| Feb 2026 | Some units moving to Chapter 7 liquidation | Bloomberg/Crain's Cleveland |
| **Apr 21 2026** | **WAL Q1 earnings — exposure must be addressed** | |

---

## Double-Pledging Pattern

First Brands is not isolated. The double-pledging mechanism has now surfaced in three separate fraud rings:
1. **First Brands** — US, auto parts, DOJ indicted
2. **MFS (Market Financial Solutions)** — UK, £2B mortgage fraud, Barclays £600M / Jefferies £100M exposure (ML-REG-096)
3. **Tricolor** — US, subprime auto, $800M fraud

Reuters framed this as **"cockroaches in private credit"** — if you find one, there are more (ML-REG-096). The structural vulnerability is identical: collateral-based lending where physical verification is infrequent and paper records are manipulated.

Unicus Research (ML-REG-114) drew the explicit structural parallel: CRE origination fraud and auto ABS fraud share the same architecture — infrequent physical verification, paper-based records, originate-to-distribute incentives.

---

## Auction Result (Resolved Apr 2026)

**The Mar 31 forbearance deadline passed. Piecemeal liquidation confirmed.**

### Asset Sales
| Asset | Buyer | Price |
|-------|-------|-------|
| Brand portfolio (Fram, Autolite, Trico — 12 brands) | PGI Northstar | $25M |
| Walbro business | Overdrive Capital LLC | $50M |
| Autolite, Brake Parts, Cardone | Winding down / Chapter 7 | — |
| **Total recovered** | | **~$75M** |

### Recovery Math
- Total debt: $9.3B ($6B on-balance-sheet + $2.4B off-balance-sheet SPVs + $800M supply chain)
- Fabricated receivables: $2.3B confirmed by restructuring advisors
- Asset sale recovery: ~$75M / $9.3B = **<1%**
- Debt trading: **30-47 cents** on the dollar (Dec 2025 - Feb 2026 range)
- Morningstar DBRS adverse scenario: total losses potentially **>$1B** across trade credit insurers/reinsurers

### Key Exposures
| Entity | Exposure | Note |
|--------|----------|------|
| Onset Financial | $1.9B | Inventory-backed |
| Jefferies / Point Bonita | $715M | Receivables — JEF took $40-47M in losses already |
| UBS | >$500M | Supply chain financing |
| 15 BDCs | $237M | Marks need to come down |

### WAL V2 Impact
WAL's $126.4M disputed exposure through Point Bonita/Jefferies is **almost certainly unrecoverable** given <1% asset recovery. The Mar 31 forbearance deadline passed — Jefferies still calling the lawsuit "meritless" and asserting non-recourse. This forces WAL to either:
1. Write off the $126.4M (or net of $42.1M already paid = $84.3M remaining) in Q1 2026
2. Continue disputing in court while carrying impaired asset on books

Either way, this is a Q1 earnings catalyst — analysts will ask about it.

---

## BDC Exposure ($237M across 15 funds)

15 BDCs hold $237M in First Brands exposure (ML-REG-078). This creates a secondary transmission channel:
- BDC marks may be overstated (TCPC/BlackRock precedent — ML-REG-103)
- Fund finance desks that lent to these BDCs based on marks take undisclosed losses
- WAL's NDFI book ($4.2T industry, +35% YoY per ML-REG-115) includes warehouse lines to BDCs

---

## Investor Litigation (Feb 25 2026)

Point Bonita investors sued Jefferies + Point Bonita alleging misrepresentation of "cash dominion" over receivables. If First Brands actually controlled payment streams despite contractual transfer, the collateral supporting both fund investors AND WAL's lending was weaker than represented. This is the fraud mechanism — receivables may have been double-pledged, overstated, or uncollectible.

**Full analysis doc:** `WAL-JEF-PointBonita-Analysis-20260326.docx` (16 footnoted sources, entity structure table, complete timeline)

## Canonical Research

- **FORGE:** `FORGE/research/jefferies/THESIS.md` — Jefferies as convergence node
- **FORGE:** `FORGE/research/jefferies/EARNINGS/Q1_CY2026.md` — $17M loss detail
- **KB:** ML-REG-078 (First Brands DOJ), ML-REG-088 (WAL/JEF confirmed), ML-REG-116 (JEF Q1 earnings)
