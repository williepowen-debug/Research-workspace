# First Brands / Point Bonita — WAL Fraud Vector 1
**Last Updated:** 2026-03-25

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

WAL's exposure is **indirect** — through the private credit/leveraged lending chain, not direct lending to First Brands. This makes it harder to quantify but confirmed by Bloomberg (Oct 2025): "Western Alliance faces First Brands risk."

**WAL-specific dollar exposure:** [DATA NEEDED] — not disclosed in WAL filings. Must be addressed at Apr 21 earnings.

---

## Jefferies Confirmation

Jefferies Q1 CY2026 (reported Mar 25 2026 after close):
- **$17M in losses** from First Brands + MFS combined
- EPS $0.70 vs consensus $0.91 — **23% miss**, driven by credit losses
- TBVPS $34.24, down **15.7% YoY** — balance sheet erosion
- Oppenheimer cut PT from $97 to $74 ahead of results

The $17M is described as combined First Brands + MFS. Breakdown between the two: [DATA NEEDED — pending transcript analysis Mar 26].

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

## BDC Exposure ($237M across 15 funds)

15 BDCs hold $237M in First Brands exposure (ML-REG-078). This creates a secondary transmission channel:
- BDC marks may be overstated (TCPC/BlackRock precedent — ML-REG-103)
- Fund finance desks that lent to these BDCs based on marks take undisclosed losses
- WAL's NDFI book ($4.2T industry, +35% YoY per ML-REG-115) includes warehouse lines to BDCs

---

## Canonical Research

- **FORGE:** `FORGE/research/jefferies/THESIS.md` — Jefferies as convergence node
- **FORGE:** `FORGE/research/jefferies/EARNINGS/Q1_CY2026.md` — $17M loss detail
- **KB:** ML-REG-078 (First Brands DOJ), ML-REG-088 (WAL/JEF confirmed), ML-REG-116 (JEF Q1 earnings)
