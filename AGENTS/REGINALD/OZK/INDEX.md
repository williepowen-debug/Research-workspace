# OZK — Agent Index
**Start here on cold boot.**

**Last updated:** 2026-04-22 (post-Q1 26 print integration + file-tree cleanup)

**State snapshot:**
- **Q1 2026 earnings ✅ RESOLVED Apr 21** — past-due doubled QoQ ($207M → $465M), 3 new substandard credits, 2 new foreclosed assets, NCO 0.57% in-line. Slow-grind thesis confirmed. → `Q1_2026_ANALYSIS.md`
- **Thesis v1.1 (Apr 22/23)** — Q1 print integrated; mix-shift linear projection retracted; 3 migration-velocity leading indicators survive. → `CHANGELOG.md`
- **KB.tsv: 185 rows / 17 groups** (178-185 added Apr 22-23)
- **Positions:** $42.5P May 15 × 2 (rolling this week), $42.5P Aug 21 × 1, $45P Aug 21 × 4. Roll recommendation → `THREAD3_ROLL_MATH.md`
- **Next hard catalyst:** IQHQ RaDD Aug 2026 maturity — weighted EL $140M on $555M funded. → `IQHQ_PLAYBOOK.md`

---

## Data Ownership (no duplication)

| Doc | Owns | Don't put here |
|---|---|---|
| `STATUS.md` | Current prices, thresholds, positions, Q1 26 dashboard | Thesis detail (→ THESIS), deep math (→ sub-docs) |
| `THESIS.md` | Structural bear case, channels, synthesis + pointers | Current numbers (→ STATUS), trajectory math (→ sub-docs) |
| `CHANGELOG.md` | Thesis-level deltas w/ old vs new view, version pinning | Data (→ KB) or process notes |
| `Q1_2026_ANALYSIS.md` | Q1 26 earnings print synthesis — actuals, management comments | Forward scenarios (→ IQHQ_PLAYBOOK, SCENARIOS) |
| `IQHQ_PLAYBOOK.md` | RaDD Aug 2026 scenarios (A/B/C/D), weighted EL, sponsor stack | Other credits (→ SEVEN_CREDIT) |
| `SEVEN_CREDIT_DEEP_DIVE.md` | 7 problem credits ($719M), severity math, sponsor IDs | IQHQ (→ IQHQ_PLAYBOOK) |
| `THREAD3_ROLL_MATH.md` | Options roll math — May 15 position → Aug/Nov/Jan27 candidates | General position view (→ STATUS) |
| `workbook/KB.tsv` | 185-row canonical evidence database | Narrative (→ THESIS) |

---

## Boot Sequence

| Order | File | Time | What You Get |
|-------|------|------|-------------|
| 1 | `STATUS.md` | 2 min | Live dashboard, positions, catalyst list, Q1 26 summary |
| 2 | `THESIS.md` | 5 min | Bear case w/ synthesis pointers to sub-docs |
| 3 | `CHANGELOG.md` (v1.1 top entry) | 3 min | What changed this week + what was retracted |
| 4 | `workbook/KB_INDEX.md` | 2 min | 17-cluster KB navigator |
| — | Deep dive as needed | — | `Q1_2026_ANALYSIS.md`, `IQHQ_PLAYBOOK.md`, `SEVEN_CREDIT_DEEP_DIVE.md`, `THREAD3_ROLL_MATH.md` |

**Total cold-boot: ~12 min** for the current operational picture.

---

## File Map

### Core (read at boot / primary pointers)
| File | Description |
|------|-------------|
| `INDEX.md` | This file — nav only, no data |
| `STATUS.md` | Live dashboard |
| `THESIS.md` | Master bear case (synthesis + pointers pattern) |
| `CHANGELOG.md` | Thesis audit trail — v1.1 current, v1.0 pinned |
| `Q1_2026_ANALYSIS.md` | Most recent earnings synthesis (Apr 21 actuals) |
| `TODO.md` | Research backlog |
| `workbook/KB.tsv` | 185-row evidence database |
| `workbook/KB_INDEX.md` | KB cluster navigator |

### Active deep dives (read on-demand)
| File | When to Read |
|------|-------------|
| `IQHQ_PLAYBOOK.md` | Modeling Aug 2026 RaDD maturity scenarios |
| `SEVEN_CREDIT_DEEP_DIVE.md` | Drilling into RESG problem credits |
| `THREAD3_ROLL_MATH.md` | Options roll execution — live recommendation |
| `WEAKNESSES.md` | Stress-testing the thesis (bull case steelman) |
| `SCENARIOS.md` | Probability-weighted outcomes (⚠️ may be superseded by IQHQ_PLAYBOOK §3) |

### Research — rebuttals (bull case pressure-test)
| File | Topic |
|------|-------|
| `research/C1_RECLASSIFICATION_REBUTTAL.md` | "Reclassification is normal" |
| `research/C2_RATE_RELIEF_SCENARIO.md` | "Rate cuts save them" |
| `research/C3_CAPITAL_ABSORPTION_ANALYSIS.md` | "Capital absorbs losses" |

### Research — bear case series D
| File | Topic |
|------|-------|
| `research/D1_LTV_EXTRAPOLATION.md` | LTV stress on reappraised loans |
| `research/D2_PLEDGED_LOANS_LIQUIDITY.md` | 74% pledged, depositor subordination |
| `research/D3_SHADOW_CRE_LEVER.md` | Novel adjusted CRE/Tier1 metric |
| `research/D4_PROBLEM_BANK_COMPARISON.md` | OZK vs problem bank thresholds |
| `research/D5_DIVIDEND_SUSTAINABILITY.md` | Dividend cut probability model |
| `research/D6_EXTEND_AND_PRETEND.md` | 590 mods, 98% classification gap, 59% re-default |

### Research — post-Q1 threads (Apr 22-23, thesis v1.1 inputs)
| File | Verdict |
|------|---------|
| `research/threads/IQHQ_SECONDARY_EXPOSURE.md` | NO EVIDENCE of second IQHQ credit — Rossow on-record to Bisnow confirms RaDD is sole |
| `research/threads/CIB_MARGIN_COMPRESSION.md` | Vertical-specific (3/6 compressing), net-neutral, NIM drift 4.20% → 4.10-4.15% |
| `research/threads/RESG_MIX_DETERIORATION.md` | Apr 22 linear projection RETRACTED (Apr 23). Real indicators: substandard migration, past-due regime change, NCO tempo. |

### Research — other
| File | Topic |
|------|-------|
| `research/8K_FORCED_DISCLOSURE_FRAMEWORK.md` | Pre-announcement pattern analysis |
| `research/NDFI_SHADOW_CRE_ANALYSIS.md` | $2.74B shadow CRE deep dive |
| `research/INSIDER_ACTIVITY_COMPILED.md` | Compiled insider transactions |

### Domain subdirs
| Path | Content |
|------|---------|
| `LIFE_SCI/` | Lab market findings — RaDD, Campus at Horton, downtown SD vacancy, SD/Boston/Chicago $3.2B book |
| `GEOGRAPHY/` | CRE exposure by metro (58 MSAs), FL paradox stress-test, regulatory district mismatch |
| `INSIDERS/` | Insider trading analysis, FDIC EFR pulls, departures tracker |
| `MARKET/` | Market data, trade log, microstructure |
| `PRIVATE_CREDIT/` | Affinius/NDFI counterparty risk |

### Raw sources (don't read at boot)
| Path | Content |
|------|---------|
| `sources/` | Primary-source extracts only — 10-K/10-Q sections, FDIC/FFIEC API pulls, QBP data |
| `raw/` | Raw OZK PDFs (Mgmt Comments, Financial Supplement, transcript) — Q4 24 / Q1-Q4 25 / Q1 26 |
| `raw/llm_outputs/` | Raw LLM research outputs (30 files) — provenance archive, distilled into KB.tsv |
| `historical/` | Time-series Mgmt Comments extracts — Q4 24 / Q1-Q4 25 |

### Archive (completed/stale — don't read)
| File | Why |
|------|-----|
| `archive/EARNINGS_PREP_Q1_2026.md` | Pre-Q1 26 earnings prep (474 lines). Q1 resolved Apr 21 — superseded by `Q1_2026_ANALYSIS.md`. |
| `archive/AUDIT_REPORT.md`, `archive/AUDIT_REPORT_MAR23.md` | Old audits — superseded by CHANGELOG |
| `archive/GAP_CLOSURE_PLAN.md`, `archive/GAP_ANALYSIS_REPORT.md` | Pre-Q1 gap work complete |
| `archive/STRUCTURE_AUDIT.md`, `archive/RESTRUCTURE_REVIEW.md` | KB migration complete |
| `archive/OZK_THESIS_FEB25.md` | Feb 25 thesis snapshot (pre-v1.0 baseline) |
| `archive/EVIDENCE.md` | Legacy evidence doc |

### Workbook
| File | Content |
|------|---------|
| `workbook/KB.tsv` | 185-row evidence database (14-column schema) |
| `workbook/KB_INDEX.md` | 17-cluster navigator |
| `workbook/KB_MIGRATION_LOG.md`, `workbook/KB_INDEX_AUDIT.md` | Audit trails |
| `workbook/PREDICTIONS.tsv` | Falsifiable predictions (REG-01 through REG-23) |

---

## Update Rules

| What Changed | Where | Don't Touch |
|---|---|---|
| A number / data point | `workbook/KB.tsv` | THESIS.md (references KB rows by ID) |
| Narrative / framing | `THESIS.md` + append to `CHANGELOG.md` | KB (data doesn't change because framing did) |
| Thesis-level shift | `THESIS.md` + **MUST** append `CHANGELOG.md` w/ version bump | — |
| New research output | `research/threads/` (post-Q1) or `research/C*/D*` (pre-Q1 rebuttals) | Top level — top level is for core pointers + active deep dives |
| Position change | `STATUS.md` + update `IQHQ_PLAYBOOK §6` if related to IQHQ | Don't duplicate in multiple places |
| Session ending | `../MEMORY.md` (parent REGINALD dir) — session handoff notes | INDEX.md (let it stabilize) |

**Research-threads rule:** Threads move to `research/threads/` on creation. Insight gets synthesized into THESIS.md (2-3 sentences + pointer). If the thread's core claim is later retracted or superseded, mark it in `CHANGELOG.md` — don't delete the thread file.

---

*This file is the entry point. If you're an agent spawning cold, read this first, then follow the boot sequence. Last tree-hygiene pass: 2026-04-22 — moved EARNINGS_PREP → archive/, moved Apr 22 threads → research/threads/.*
