# REGINALD Research Prompts

**Created:** 2026-03-05
**Purpose:** Research prompt infrastructure indexed by cluster
**Usage:** Run prompts with research-capable LLM, save output to `research/outputs/`

---

## Folder Structure

```
prompts/
├── README.md                        # This file
├── cluster_1_florida/               # RP-FL series (CORAL territory)
├── cluster_2_geographic/            # RP-REG-3.x series
├── cluster_3_systemic/              # RP-REG-4.x series
├── cluster_4_forensic/              # RQ-REG-A series (fraud/forensic)
└── cluster_5_transmission/          # RQ-REG-B/C series (LP liquidity, FHLB)
```

---

## Completed Research Index

All research below is ✅ Complete. Outputs live in `research/outputs/`. Do NOT re-run without new data.

### Cluster 1: Florida (CORAL Territory) — `cluster_1_florida/`
| ID | Title | Status | Key Finding |
|----|-------|--------|-------------|
| RP-FL-1.1 | Florida Condo Receivership | ✅ Complete | 1,438 blacklisted buildings |
| RP-FL-1.2 | FL Private Insurer Health | ✅ Complete | Carrier stress mapping |
| RP-FL-1.3 | VLY Florida Exposure | ✅ Complete | FL 27% of loans, $3.3B Miami CRE |
| RP-FL-1.4 | Florida Bridge Loan Market | ✅ Complete | Refinancing gap analysis |
| RP-FL-1.5 | Florida Developer Acquisitions | ✅ Complete | Distressed deal flow |
| RP-FL-2.1 | Private Insurer Health (v2) | ✅ Complete | Updated carrier analysis |

### Cluster 2: Geographic & Municipal — `cluster_2_geographic/`
| ID | Title | Status | Key Finding |
|----|-------|--------|-------------|
| RP-REG-3.1 | Regional Bank Geographic Footprints | ✅ Complete | No KRE constituent has material TX border exposure |
| RP-REG-3.2 | Municipal Securities Exposure | ✅ Complete | ZION $5.78B total muni; WAL $1.36B UNRATED |
| RP-REG-3.3 | DC Corridor Bank Analysis | ✅ Complete | EGBN 100% DC, already in crisis |
| RP-REG-3.4 | Texas Border Municipal Analysis | ✅ Complete | Barclays void; CFR/TCBI filling gap |
| RP-REG-3.5 | Florida Insurance-Banking Nexus | ✅ Complete | Citizens $678B "Sword of Damocles" |

### Cluster 3: Systemic Channels — `cluster_3_systemic/`
| ID | Title | Status | Key Finding |
|----|-------|--------|-------------|
| RP-REG-4.1 | Stablecoin Deposit Flight | ✅ Complete | $500B outflow projected by 2028 |
| RP-REG-4.2 | Florida HOA/Condo Crisis | ✅ Complete | Post-Surfside SB 4-D → $10K-$224K assessments |
| RP-REG-4.3 | FL Institutional Capital | ✅ Complete | Private capital flows to distressed FL assets |

### Cluster 4: Forensic / Fraud — `cluster_4_forensic/`
| ID | Title | Status | Key Finding |
|----|-------|--------|-------------|
| RQ-REG-A01 | WAL/ZION Fraud Comparison | ✅ Complete | Both -13% post-Tricolor |
| RQ-REG-A02 | Stupin Syndicate Mapping | ✅ Complete | Sector exposure mapping |
| RQ-REG-A02B | Forensic Insurance Auditor | ✅ Complete | Deep forensic analysis |
| RQ-REG-A03 | Fraud Contagion Signals | ✅ Complete | Sector transmission paths |

### Cluster 5: Transmission Mechanisms — `cluster_5_transmission/`
| ID | Title | Status | Key Finding |
|----|-------|--------|-------------|
| RQ-REG-B01 | LP Liquidity / CFG Transmission | ✅ Complete | Fund finance $10-11B exposure |
| RQ-REG-C01 | FHLB Haircut Policy | ✅ Complete | Haircut mechanics during stress |

---

## Future Prompt Priorities (DATA GAPS)

| Priority | Cluster | Topic | Notes |
|----------|---------|-------|-------|
| 🟡 Medium | cluster_2_geographic | Burke & Herbert (BHRB) deep dive | DC corridor, >50% AFS in munis |
| 🟡 Medium | cluster_2_geographic | Nevada gaming/tourism stress | RENO sub-agent territory |
| 🟡 Medium | cluster_4_forensic | Texas border bank forensics | IBOC is only public play |
| 🟢 Low | cluster_3_systemic | 2013 sequester precedent analysis | Historical comparison |
| 🔴 High | cluster_3_systemic | Q1 bank earnings preview | Apr 2026 catalyst |
| 🟠 Medium | cluster_2_geographic | Phoenix CRE repricing | If Chicago pattern spreads |

---

## Prompt Design Notes

Each prompt should include:
- **Context block** — Background for the LLM (relevant VX/FLOW data)
- **Numbered questions** — Specific research targets
- **Output specification** — What format REGINALD needs (TSV-ready, narrative, or both)
- **Source requests** — EDGAR, FRED, county records, etc.

---

*REGINALD Research Prompt Library v1.0 — 2026-03-05*
