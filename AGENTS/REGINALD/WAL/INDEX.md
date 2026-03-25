# WAL — Agent Index
**Start here on cold boot.**

**Last session (Mar 25 late):** KB.tsv seeded — **61 rows across 10 groups**. KB_INDEX.md written with vector mapping, thesis layers, staleness tracking. Architecture complete.

---

## Key Numbers (Q4 2025)

| Metric | Value | Signal |
|--------|-------|--------|
| CRE / Tier 1 Capital | **474%** (guideline: 300%) | 🔴 |
| True CRE Exposure | ~59% of loans (labeled ~35%) | 🔴 |
| Memo Item 3 / C&I | **24.2%** (GROWING) | 🔴 |
| SSFA Capital Savings | $1.1B on $17.2B | 🔴 |
| NCO Rate (SF District) | **1.13%** (highest nationally) | 🔴 |
| Insider Buying | **Zero** | 🔴 |

## Positions

| Strike | Expiry | Contracts | Thesis Alignment |
|--------|--------|-----------|-----------------|
| $85P | Jun 18 | 1 | Deep ITM |
| $77.5P | Sep 18 | 1 | Core |
| $70P | Sep 18 | 1 | Needs decline |
| $65P | Jun 18 | 1 | Aggressive |

**Earnings: ~April 21, 2026**

## Data Update Rules

| What Changed | Where to Update | Don't Touch |
|---|---|---|
| **A number/data point** | KB.tsv only | THESIS.md |
| **Narrative/framing** | THESIS.md | KB.tsv |
| **New evidence arrives** | Add KB.tsv row → check off STATUS.md Research Agenda | |
| **Task completed** | STATUS.md Research Agenda checklist | |
| **Session ending** | Update "Last Session" above + STATUS.md "What's Changed" | |

## Boot Sequence

| Order | File | Time | What You Get |
|-------|------|------|-------------|
| 1 | `STATUS.md` | 1 min | Dashboard, positions, catalysts, research agenda |
| 2 | `THESIS.md` | 4 min | Full thesis — three vectors, geographic evidence, insider, bull rebuttals |
| 3 | `SCENARIOS.md` | 1 min | Bull/base/bear with triggers |
| 4 | `workbook/KB.tsv` | 3 min | **61-row** canonical evidence database |
| — | `workbook/KB_INDEX.md` | 2 min | **10 groups** → vectors → thesis layers → staleness |

## File Map

### Core (read at boot)
| File | Description |
|------|-------------|
| `INDEX.md` | This file — start here |
| `STATUS.md` | Live dashboard, positions, catalyst calendar |
| `THESIS.md` | Full thesis with three-vector framework |
| `SCENARIOS.md` | Probability-weighted outcomes (DRAFT) |
| `workbook/KB.tsv` | Canonical evidence store (**61 rows**, 13 columns) |
| `workbook/KB_INDEX.md` | **KB group navigator** — 10 groups mapped to vectors, thesis layers, staleness |

### Deep Dives (read on-demand)
| File | When to Read |
|------|-------------|
| `EARNINGS_PREP.md` | **Apr 21 prep — A- quality** (tripwires, decision matrix, mgmt defense, 11 KB gaps flagged) |
| `WEAKNESSES.md` | Stress-testing — what breaks the thesis |
| `EXTERNAL_PROMPTS.md` | Research prompts for Will to run externally (5 pending) |
| `TECHNICALS.md` | Chart levels and technical analysis |

### Research (vector-organized)
| Folder | Topic |
|--------|-------|
| `research/HIDDEN_CRE/` | Vector 1: MI3 reclassification, true CRE exposure |
| `research/JEFFERIES/` | Vector 2: Double-pledging, intermediary chain |
| `research/SSFA/` | Vector 3: Capital arbitrage, $17.2B exposures |
| `research/RQ-REG-A01_WAL_ZION_FRAUD_COMPARISON.md` | WAL vs ZION fraud provision analysis |

### Sources & Archive
| Folder | Contents |
|--------|----------|
| `sources/` | Raw inputs (FDIC, FFIEC, insider scans, Jefferies signal) |
| `archive/` | Superseded files |
| `PRIOR_RESEARCH_EXTRACTS.md` | Older LLM research (Feb 2026) — verified selectively |
| `FORGE_STATUS.md` | Original FORGE trade status + SSFA deep dive |
