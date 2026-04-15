# OTTO STATUS

**Updated:** 2026-04-14 19:15 ET | **Status:** 🔴🔴 CRITICAL — SUBPRIME STRESS ESCALATING

---

## SIGNAL DASHBOARD

### Subprime Auto / ABS
| Metric | Value | As Of | Status | Source |
|--------|-------|-------|--------|--------|
| Subprime Auto 60+ DQ | **6.9%** | Jan 2026 | 🔴🔴 | Fitch |
| Auto 90+ DQ (NY Fed) | **5.21%** | Q4 2025 | 🔴 | NY Fed |
| Prime ABS Spreads | **+17bps** | Mar 30 | 🔴 | Auto Finance News |
| SoFi 2025-1 CNL | **2.6% TRIGGERED** | Mar 2026 | 🔴 | Eisman Ep 49 |
| Total Auto Debt | **$1.66T** | Q4 2025 | 🔴 | NY Fed |
| **Extension Unwind Risk** | **35/100** | Apr 14 | 🟡 | OTTO Proxy Model |
| **ABS Issuance YTD** | **$1.55B** (2 deals) | Apr 14 | 🟡 | Westlake, Lendbuzz |

### Key Entities
| Entity | Price/Status | As Of | Status | Notes |
|--------|--------------|-------|--------|-------|
| CVNA | **$359** | Apr 13 | 🟡 | Q1 earnings Apr 29, 10-K filed on time, GT did NOT resign |
| Tricolor | **Ch.7 liquidation** | Mar 31 | 🔴🔴 | Execs criminally charged w/ systematic fraud (Apr 3), recovery rates pending, trial Oct 2026 |
| First Brands | **Ch.11 (Ch.7 risk)** | Apr 14 | 🔴🔴 | Auto parts fraud cluster w/ Tricolor, De Luca report due ~Apr 9, $237M BDC exposure |
| SYF NCO | **5.8%** | Feb 2026 | 🔴🔴 | 3x prime, CARL signal confirmed |

### Macro / Transmission
| Metric | Value | As Of | Status |
|--------|-------|-------|--------|
| Gas National | **$4.125** | Apr 13 | 🔴 |
| Diesel | **$5.65** | Apr 13 | 🔴🔴 |
| Brent | **$98.18** | Apr 13 | 🟠 |
| HY OAS | **294bps** | Apr 10 | 🟢 ⚠️ Complacency gap |

---

## AM BRIEF — April 14, 2026

**CVNA Update (Post-Research):**
- Stock at ~$359, recovered from Feb 18 lows (~$290s)
- **10-K filed on time** (Feb 18) — Grant Thornton did NOT resign, no restatements
- Gotham predictions (GT resignation, 10-K delay, restatements) **did NOT materialize**
- Q1 earnings Apr 29 — watch Retail GPU for reconditioning cost pressure
- Ally correlation: **No significant impact** from CVNA volatility
- Multiple class actions filed post-Gotham report

**Key Developments:**
1. CVNA fraud thesis weakened — Gotham's specific predictions failed
2. Reconditioning cost pressure persists (CFO confirmed on Feb call)
3. Litigation risk elevated but no new court orders on Gotham allegations

**Bankruptcy Update (Post-Research):**
- **Tricolor:** Ch.7 liquidation, Mar 31 deadline passed — recovery rates pending. JPM/FITB losses already taken in Q3 2025 ($170M/$170-200M). No new Q1 disclosures.
- **First Brands:** Ch.11 with Ch.7 conversion risk. De Luca examiner report due ~Apr 9 (check Kroll). 15 BDCs with $237M exposure. Jefferies $40M total loss ($10M Q1).
- **Open items:** Tricolor recovery rates, De Luca report publication, BDC Q1 10-K loss disclosures

**Predictions Update:**
- OTTO-26 (PSEC dividend cut): **FALSIFIED** — No cut, dividend maintained at $0.54 annual
- OTTO-27 (FSK coverage <1.0x): **FALSIFIED** — Q4 2025 coverage 108%, dividend maintained

**Cross-Domain Signals:**
- **CARL:** SYF 5.8% NCO confirms consumer credit stress
- **REGINALD:** No CVNA→Ally contagion observed
- **BROCK:** Private credit gating continues (Ares, Apollo, Blue Owl, Blackstone)

---

## WHAT TO WATCH

| When | Event | Priority | Status |
|------|-------|----------|--------|
| Apr 16 | OZK Q1 Earnings | 🔴 | Monitor for 8-K, NDFI commentary |
| Apr 21 | WAL Q1 Earnings | 🔴 | Watch for warehouse exposure updates |
| Apr 29 | CVNA Earnings | 🟠 | Watch Retail GPU, reconditioning costs |
| May 5 | CVNA Shareholder Vote | 🟠 | Split vote outcome |
| Jun 17 | Tricolor Bankruptcy Hearing | 🟡 | 10:00 AM, status update |
| **TBD** | **First Brands De Luca Report** | 🟡 | Prepetition factoring arrangements — fraud scope |

---

## TOOLS / SCRIPTS

| Script | Purpose | Status | Last Run |
|--------|---------|--------|----------|
| abs_issuance_tracker.py | Track ABS issuance, spreads, ratings | ✅ Active | $1.55B YTD (Westlake, Lendbuzz) |
| extension_proxy.py | Proxy signals for extension unwind | ✅ Active | Score: 35/100 🟡 MODERATE |
| ~~bank_earnings_monitor.py~~ | ~~Bank transcripts~~ | ~~DROPPED~~ | REGINALD handles bank monitoring |

**Workbooks:**
- `workbook/KB.tsv` — Knowledge base
- `workbook/VX.tsv` — Vulnerability index
- `workbook/FLOW.tsv` — Signal flow tracking
- `workbook/CROSS_AGENT_LOG.tsv` — Cross-agent communications

---

## ACTIVE THESIS

**Core:** Subprime auto is the consumer credit canary. 2022 vintage + immigration stress + fuel inflation = 32-year high DQ rates. Transmission to bank warehouse lenders (WAL, OZK) via NDFI and counterparty risk.

**Extended (Apr 15):** Auto supply chain finance fraud is a structural vulnerability. First Brands (auto parts distributor) + Tricolor (subprime lender) share identical fraud patterns: receivables financing, collateral misrepresentation, cash control failures. Upstream (parts) and downstream (loans) stress are linked.

**Positions:**
- None currently
- Watch: CVNA puts on fraud thesis confirmation

**Predictions:** See `PREDICTIONS.tsv`

---

## INBOX

| Item | Received | Status | Action |
|------|----------|--------|--------|
| prome_2026-04-03_sweep.md | Apr 3 | ✅ Processed Apr 15 | Tricolor fraud charges, CPS check |
| sweep_2026-04-03_1419.md | Apr 3 | ✅ Processed Apr 15 | Tricolor criminal charges |
| research_2026-04-06_auto_parts_stress.md | Apr 6 | ✅ Processed Apr 15 | Auto parts fraud cluster, First Brands thesis extension |

**Processed:** 9 items (see `inbox/processed/`)

---

## CROSS-AGENT SIGNALS

### To CARL
| Date | Signal | Status |
|------|--------|--------|
| Mar 30 | SYF 5.8% NCO confirmation | ✅ Delivered |

### To REGINALD
| Date | Signal | Status |
|------|--------|--------|
| Mar 9 | MFS/Jefferies/WAL private credit exposure | ✅ Delivered |
| Apr 15 | Tricolor bank losses: JPM $170M, FITB $170-200M (Q3 2025). Jefferies $40M First Brands total loss. | ✅ Delivered |

### From Other Agents
| Date | From | Signal | Status |
|------|------|--------|--------|
| [Awaiting] | — | — | — |

---

*Archive: `archive/`, `workbook/STATUS_archive_20260325.md`*
