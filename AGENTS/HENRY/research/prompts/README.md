# HENRY Research Prompts

**Created:** 2026-01-26
**Purpose:** External LLM research prompts for deep search
**Usage:** Run each prompt with research-capable LLM, save output to `/research/outputs/`

---

## Folder Structure

```
prompts/
├── README.md                          # This file
├── SESSION_001_PLAN.md               # Completed baseline research
├── cluster_1_novel_structures/        # 0DTE, passive, private credit
├── cluster_2_timing_catalysts/        # Historical triggers, sentiment, breadth
├── cluster_3_counter_thesis/          # Bull case steelman
├── cluster_4_transmission/            # Wealth effect, corporate feedback
└── cluster_5_cross_market/            # Global valuations, credit divergence
```

---

## Priority Execution Order

| Priority | Prompt ID | File | Rationale |
|----------|-----------|------|-----------|
| 1 | RP-HEN-1.1 | cluster_1/0DTE_gamma_dynamics.md | Novel risk, potential catalyst |
| 2 | RP-HEN-2.1 | cluster_2/historical_catalyst_analysis.md | What triggers the break |
| 3 | RP-HEN-2.3 | cluster_2/breadth_deterioration.md | Real-time actionable |
| 4 | RP-HEN-4.1 | cluster_4/wealth_effect_quantification.md | Transmission to real economy |
| 5 | RP-HEN-3.1 | cluster_3/AI_productivity_bull_case.md | Counter-thesis required |
| 6 | RP-HEN-1.3 | cluster_1/private_credit_leverage.md | Hidden leverage risk |
| 7 | RP-HEN-1.2 | cluster_1/passive_investing_dominance.md | Structural mean reversion |

---

## Output Instructions

When research is complete:

1. Save output to `C:/Projects/HENRY/research/outputs/[PROMPT_ID]_output.md`
2. Use naming convention: `RP-HEN-X.X_output.md`
3. Include date and source LLM in output header
4. HENRY will read, analyze, and integrate into workbook

---

## Prompt Design Notes

Each prompt includes:
- **Context block** - Background for the LLM
- **Numbered questions** - Specific research targets
- **Output specification** - What format HENRY needs
- **Source requests** - Where to find data

---

## Prompt Index

### Cluster 1: Novel Market Structures
| ID | Title | Status |
|----|-------|--------|
| RP-HEN-1.1 | 0DTE Options & Gamma Dynamics | Ready |
| RP-HEN-1.2 | Passive Investing Dominance | Ready |
| RP-HEN-1.3 | Private Credit / Shadow Leverage | Ready |

### Cluster 2: Timing & Catalysts
| ID | Title | Status |
|----|-------|--------|
| RP-HEN-2.1 | Historical Catalyst Analysis | Ready |
| RP-HEN-2.2 | Sentiment Extreme Indicators | Ready |
| RP-HEN-2.3 | Breadth Deterioration Patterns | Ready |

### Cluster 3: Counter-Thesis (Bull Case)
| ID | Title | Status |
|----|-------|--------|
| RP-HEN-3.1 | AI Productivity Justification | Ready |
| RP-HEN-3.2 | Structural Bid Thesis | Ready |

### Cluster 4: Transmission Mechanisms
| ID | Title | Status |
|----|-------|--------|
| RP-HEN-4.1 | Wealth Effect Quantification | Ready |
| RP-HEN-4.2 | Corporate Sector Feedback Loops | Ready |

### Cluster 5: Cross-Market Context
| ID | Title | Status |
|----|-------|--------|
| RP-HEN-5.1 | Global Valuation Comparison | Ready |
| RP-HEN-5.2 | Credit Market Divergence | Ready |

---

*HENRY Research Prompt Library v1.0*
