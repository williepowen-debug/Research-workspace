# OZK — Agent Index
**Start here on cold boot.**

**Last session (Mar 25):** KB at **160 rows** across 17 groups. SHORT_INTEREST added as group 17 (KB-OZK-160). FL Paradox complete. Peer comp integrated. D6 Extend-and-Pretend synthesis written. KB_INDEX.md navigator created. Orphan folders (INSIDERS/, MARKET/, PRIVATE_CREDIT/) indexed.

---

## Key Numbers (Q4 2025)

| Metric | Value | Signal |
|--------|-------|--------|
| CRE / Tier 1 Capital | **358%** (guideline: 300%) | 🔴 Highest-tier concentration |
| Adjusted CRE / Tier 1 (w/ shadow) | **405-420%** | 🔴 Novel metric — includes MI3 + NDFI |
| ACL / Total Loans | **1.16%** ($632M) | 🔴 Below peer median ~1.23%, below peer avg ~1.75% |
| ACL / Noncurrent Coverage | **~184%** | 🔴 BELOW peer median 231% — less reserved per $ of problem loans |
| FY2025 NCO Rate (annualized) | **1.18%** FY / **1.18%** Q4 ann | 🔴 5.4x peer median (0.22%). ACL ratio breached. |
| Noncurrent Ratio | **1.06%** ($341M) | 🔴 1.7x peer median (0.61%) |
| Memo Item 3 / C&I | **37.6%** ($1.289B) | 🔴 Hidden CRE in C&I — worst in peer set |
| NDFI (Shadow CRE) | **$2.74B** | Debt-on-debt, counterparty risk |
| Construction on Interest Reserves | **89.7%** ($7.0B of $7.8B) | Clock ticking — reserves deplete |
| Loans Pledged | **74%** ($23.9B) | 🔴 Worst in SVB/FRC comp set |
| Uninsured Deposits | **$11.9B** vs ~$10B unpledged | Depositor subordination risk |
| Short Interest | **~14-15%** (UNDATED — needs refresh) | Crowded |

## Positions

| Strike | Expiry | Contracts | Thesis |
|--------|--------|-----------|--------|
| $42.5P | May 15 | 2 | Wave 1: Apr earnings catalyst |
| $42.5P | Aug 21 | 1 | Waves 2-3: NY pipeline + IQHQ |
| $45P | Aug 21 | **4** | Waves 2-3: NY pipeline + IQHQ (added 2 @ $4.05 Mar 24) |

**Earnings: April 16, 2026** — 23 days

## Data Update Rules

| What Changed | Where to Update | Don't Touch |
|---|---|---|
| **A number/data point** | KB.tsv only | THESIS.md (references KB rows — narrative stays stable) |
| **Narrative/framing** | THESIS.md | KB.tsv (data doesn't change because framing did) |
| **New evidence arrives** | Add KB.tsv row → check off STATUS.md Research Agenda | EVIDENCE.md (legacy, frozen) |
| **Task completed** | STATUS.md Research Agenda checklist | GAP_ANALYSIS Part 7 (frozen snapshot) |
| **Session ending** | Update "Last Session" below + STATUS.md "What's Changed" | — |

## Boot Sequence

| Order | File | Time | What You Get |
|-------|------|------|-------------|
| 1 | `STATUS.md` | 2 min | Dashboard, positions, catalyst calendar, research agenda |
| 2 | `THESIS.md` | 5 min | Full bear case, three waves, bull rebuttals, MI3 discovery |
| 3 | `SCENARIOS.md` | 3 min | Bull/base/bear with probabilities and triggers |
| 4 | `workbook/KB.tsv` | 3 min | **160-row** canonical evidence database |
| — | `workbook/KB_INDEX.md` | 2 min | Group navigator: **17 clusters** → folders → thesis layers |

**Total cold-boot: ~15 min.** Covers 90%+ of what an agent needs.

## File Map

### Core (read at boot)
| File | Description |
|------|-------------|
| `INDEX.md` | This file — start here |
| `STATUS.md` | Live dashboard, positions, catalyst calendar |
| `THESIS.md` | Full thesis with three-wave framework |
| `SCENARIOS.md` | Probability-weighted outcomes (**⚠️ price inputs stale — refresh before earnings**) |
| `workbook/KB.tsv` | Canonical evidence store (**160 rows**, 13 columns) |
| `workbook/KB_INDEX.md` | **KB group navigator** — 17 clusters mapped to folders, thesis layers, and earnings prep |

### Deep Dives (read on-demand)
| File | When to Read |
|------|-------------|
| `EARNINGS_PREP.md` | Prepping for Apr 16 specifically |
| `TEMPLE8_SHORT_THESIS_MAR2026.md` | External short thesis (Temple 8) for comparison |
| `WEAKNESSES.md` | Stress-testing — what breaks the thesis |
| `EXTERNAL_PROMPTS.md` | Research prompts for Will to run externally (9 done, 7 remaining) |

### Research (specific analyses)
| File | Topic |
|------|-------|
| `research/C1_RECLASSIFICATION_REBUTTAL.md` | Bull rebuttal: "reclassification is normal" |
| `research/C2_RATE_RELIEF_SCENARIO.md` | Bull rebuttal: "rate cuts save them" |
| `research/C3_CAPITAL_ABSORPTION_ANALYSIS.md` | Bull rebuttal: "capital absorbs losses" |
| `research/D1_LTV_EXTRAPOLATION.md` | LTV stress on reappraised loans |
| `research/D2_PLEDGED_LOANS_LIQUIDITY.md` | 74% pledged, depositor subordination |
| `research/D3_SHADOW_CRE_LEVER.md` | Novel adjusted CRE/Tier1 metric |
| `research/D4_PROBLEM_BANK_COMPARISON.md` | OZK vs problem bank thresholds |
| `research/D5_DIVIDEND_SUSTAINABILITY.md` | Dividend cut probability model |
| `research/D6_EXTEND_AND_PRETEND.md` | **590 mods, 98% classification gap, 59% re-default — thesis Layer 2** |
| `research/NDFI_SHADOW_CRE_ANALYSIS.md` | $2.74B shadow CRE deep dive |
| `research/INSIDER_ACTIVITY_COMPILED.md` | All insider transactions compiled |
| `research/8K_FORCED_DISCLOSURE_FRAMEWORK.md` | Pre-announcement pattern analysis |
| `INSIDERS/` | Insider trading analysis (deep dive) |
| `MARKET/` | Market data, snapshots, trade log |
| `PRIVATE_CREDIT/` | Affinius/NDFI counterparty risk analysis |

### Life Sciences (asset type — cross-geography)
| File | Content |
|------|---------|
| `LIFE_SCI/FINDINGS.md` | **RaDD 3.3% leased, IQHQ distress cascade, downtown SD >90% vacant, AI demand shrink** |
| `LIFE_SCI/STATUS.md` | Monitoring items: leasing, IQHQ liquidity, loan maturity, Campus at Horton |
| `LIFE_SCI/README.md` | Scope ($3.2B across SD/Boston/Chicago), key numbers, navigation |

### Geography (CRE exposure by metro)
| File | Content |
|------|---------|
| `GEOGRAPHY/EXPOSURE_MAP.md` | 58 MSAs, $2.9B distressed cluster, FL paradox |
| `GEOGRAPHY/REGULATORY_DISTRICTS.md` | FDIC district mismatch, PDNA/NCO gaps |
| `GEOGRAPHY/FL_PARADOX/FINDINGS.md` | 4-model FL stress-test — confirmed fortress with Biscayne 21 exception |
| `GEOGRAPHY/STATUS.md` | Geographic investigation tracker |

### Sources (raw data — don't read at boot)
| File | Content |
|------|---------|
| `sources/10K_Q4_2025_EXTRACT.md` | 10-K data extraction |
| `sources/FDIC_*.md` | FDIC API and QBP data |
| `sources/FFIEC_*.csv` | Call report raw data |
| `sources/IQHQ_RADD_RESEARCH.md` | IQHQ project research |
| `sources/*_NDFI_DEEP_RESEARCH.*` | Multi-LLM NDFI research |
| `sources/INSIDER_SCAN_OZK.md` | Raw insider scan |

### Archive (completed work — don't read)
| File | Why Archived |
|------|-------------|
| `archive/RESTRUCTURE_REVIEW.md` | KB migration complete |
| `archive/GAP_CLOSURE_PLAN.md` | All 7 fixes executed |
| `archive/AUDIT_REPORT.md` | Superseded by GAP_ANALYSIS_REPORT |
| `archive/AUDIT_REPORT_MAR23.md` | Superseded by GAP_ANALYSIS_REPORT |
| `archive/STRUCTURE_AUDIT.md` | Recommendations captured here |

### Workbook
| File | Content |
|------|---------|
| `workbook/KB.tsv` | **160-row** evidence database (13-column standard schema) |
| `workbook/KB_INDEX.md` | Group navigator — 17 clusters mapped to folders + thesis layers |
| `workbook/KB_MIGRATION_LOG.md` | Migration audit trail |

---

*This file is the entry point. If you're an agent spawning cold, read this first, then follow the boot sequence.*
