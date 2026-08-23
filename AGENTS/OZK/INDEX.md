# OZK — Agent Index
**Start here on cold boot.**

**Last updated:** 2026-08-07 (mirror-token refresh — KB 217→222/33 [+218..222 Q2 Call Report LOG-ONLY findings]; thesis v1.5 UNCHANGED — no version bump, the 8/7 session moved zero weights). Prior: 2026-07-22 (KB 216→217/33; Q2 print cycle fully graded). Prior: 2026-07-20 (thesis v1.3→v1.5, KB 200/28→216/33 synced). Prior full pass: 2026-07-06 (staleness sweep — snapshot re-based to Call Report figures, boot sequence aligned to CLAUDE.md/boot.py).

**State snapshot:**
- **Q1 2026 earnings ✅ RESOLVED Apr 21** — past-due more than doubled QoQ (**$207M → $487.5M / 1.48%** [Call Report basis; supplement showed $465M/1.41% — definitional fork, Call Report is primary]), 3 new substandard credits, 2 new foreclosed assets, **NCO 0.56% — 1bp ABOVE the ≤55bps kill line** (Invalidation §2, watching Q2). → `Q1_2026_ANALYSIS.md`
- **Thesis v1.5** — RESERVOIR: stress accumulates until the IQHQ RaDD **Aug 2026 maturity** forces recognition; v1.5 recognition-timing refinement = appraisal-gated/back-loaded deferral (Q1'26 10-Q primary). Conviction 🔴🔴 HIGH. → `THESIS.md`, `CHANGELOG.md`
- **KB.tsv: 227 rows / 36 groups** (as of 2026-08-23 orch session)
- **⚠️ `THESIS.md` §MEMO ITEM 3 carries a CONTRADICTED-BY-PRIMARY banner (8/7)** — the 37.6% MI3 baseline does not reproduce at 18 quarters; live 9.35%. Read `CALL_REPORT_2026Q2_LOG.md` §3 before citing MI3 anywhere.
- **Positions: ✅ BOOK CLOSED — ZERO open contracts as of 2026-08-22.** Both Aug-21 legs ($45P ×4, $42.5P ×1) **expired worthless at the 8/21 OPEX** under Will's 8/4 RIDE ruling; realized −$1,686.37 / −100%. *(~~STALE / NOT MANAGED — May lines expired unlogged; Aug 21 lines unverified~~ — **retired 2026-08-23**: the May lines are recorded, and the Aug lines are no longer "unverified," they are gone.)* → `POSITIONS.md`, `STATUS.md` §Positions
- **Next hard catalyst: Q3 2026 earnings + call, ~Oct 2026** — management's self-set **"~92 day"** RaDD report-back [7/22 call]. *(~~Q2 earnings Jul 21~~ — **GRADED 7/21-22**, 5 resolved, mean Brier 0.1987, conviction HELD 🔴🔴 on OZK-07★. ~~Then IQHQ RaDD Aug 2026 maturity~~ — the Aug window is all but run out with no earnings print inside it, the quiet-August path v1.5 pre-registered; ⚠️ this does **not** resolve OZK-09, whose frozen Option-2 window runs through the **Q4'26 print**.)* Weighted EL **~$129M** on $555M funded [7/23 reweight — the "$140M" figure is the pre-7/23 vintage]. → `IQHQ_PLAYBOOK.md`, `workbook/PREDICTIONS.tsv`

---

## Data Ownership (no duplication)

*Canonical full ownership table → `CLAUDE.md` §DOC OWNERSHIP. Quick version:*

| Doc | Owns | Don't put here |
|---|---|---|
| `STATUS.md` | Current prices, thresholds, positions, dashboard | Thesis detail (→ THESIS), deep math (→ sub-docs) |
| `THESIS.md` | Structural bear case, channels, synthesis + pointers | Current numbers (→ STATUS), trajectory math (→ sub-docs) |
| `CHANGELOG.md` | Thesis-level deltas w/ old vs new view, version pinning | Data (→ KB) or process notes |
| `Q1_2026_ANALYSIS.md` | Q1 26 earnings print synthesis — actuals, management comments | Forward scenarios (→ IQHQ_PLAYBOOK, SCENARIOS) |
| `IQHQ_PLAYBOOK.md` | RaDD Aug 2026 scenarios (A/B/C/D), weighted EL, sponsor stack | Other credits (→ SEVEN_CREDIT) |
| `SEVEN_CREDIT_DEEP_DIVE.md` | 11 tracked problem credits ($719M), severity math, sponsor IDs | IQHQ (→ IQHQ_PLAYBOOK) |
| `CALENDAR.md` | Forward dates + thresholds, pure table | Narrative |
| `workbook/KB.tsv` | Canonical evidence database (KB-OZK-xxx) | Narrative (→ THESIS) |
| `workbook/PREDICTIONS.tsv` | Pre-registered falsifiable reads (OZK-01→09) | Analysis (→ research/) |

---

## Boot Sequence

**The canonical boot protocol lives in `CLAUDE.md` §SPAWN PROTOCOL** — git pull → `STATUS.md` → `LESSONS.md` → `CALENDAR.md` → `MEMORY.md` → `scripts/boot.py` (live prices + catalyst countdown + standing watch + inbox + staleness in ~10s).

For deeper cold-boot orientation after that:

| Order | File | What You Get |
|-------|------|-------------|
| 1 | `THESIS.md` | Bear case w/ synthesis pointers to sub-docs |
| 2 | `CHANGELOG.md` (top entry) | Latest thesis-level change + what was retracted |
| 3 | `workbook/KB_INDEX.md` | KB cluster navigator |
| — | Deep dive as needed | `Q1_2026_ANALYSIS.md`, `IQHQ_PLAYBOOK.md`, `SEVEN_CREDIT_DEEP_DIVE.md`, `WEAKNESSES.md` |

---

## File Map

### Core (read at boot / primary pointers)
| File | Description |
|------|-------------|
| `INDEX.md` | This file — nav only, no data |
| `STATUS.md` | Live dashboard (≤250 lines) |
| `LESSONS.md` | Verified mistake patterns + prevention rules (boot read) |
| `CALENDAR.md` | Forward dates + thresholds (boot read) |
| `MEMORY.md` | Session handoff + Feedback/Findings (boot read) |
| `THESIS.md` | Master bear case (synthesis + pointers pattern) |
| `CHANGELOG.md` | Thesis audit trail — v1.5 current, v1.0 pinned |
| `MAINTENANCE.md` | Structural-change log (docs/folders/scripts) — read when investigating structure |
| `Q1_2026_ANALYSIS.md` | Most recent earnings synthesis (Apr 21 actuals) |
| `TODO.md` | Research queue + prioritization |
| `POSITIONS.md` / `TRADE.md` | Option positions (⚠️ broker-stale) / trade ideas |
| `scripts/boot.py` | Boot kit v0.1 — prices, catalysts, watch, inbox, staleness |
| `workbook/KB.tsv` | Evidence database (222 rows / 33 groups as of 2026-08-07) |
| `workbook/CALL_REPORT_SERIES.tsv` | **FFIEC Call Report series, 18 quarters** (RSSD 107244) — MI3 both bases, past-due decomposition, NCO, CRE NCO, OREO/NPA. LOG-ONLY source (Z6 never re-grades off it). |
| `CALL_REPORT_2026Q2_LOG.md` | Q2-2026 Call Report working: MI3 baseline contradiction, kill-§1 adjudication, basis-fork check, frame-spec check, proposals P-OZK-1..5. |
| `workbook/KB_INDEX.md` | KB cluster navigator |
| `workbook/PREDICTIONS.tsv` | Pre-registered falsifiable reads OZK-01→09 (05-09 resolve at Q2 Jul 21) |

### Active deep dives (read on-demand)
| File | When to Read |
|------|-------------|
| `IQHQ_PLAYBOOK.md` | Modeling Aug 2026 RaDD maturity scenarios |
| `SEVEN_CREDIT_DEEP_DIVE.md` | Drilling into RESG problem credits (11 tracked, $719M) |
| `WEAKNESSES.md` | Stress-testing the thesis (bull case steelman — C7 = RESG-runoff de-risking) |
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

### Research — post-Q1 threads
| File | Verdict |
|------|---------|
| `research/threads/IQHQ_SECONDARY_EXPOSURE.md` | NO EVIDENCE of second IQHQ credit — Rossow on-record to Bisnow confirms RaDD is sole |
| `research/threads/CIB_MARGIN_COMPRESSION.md` | Vertical-specific (3/6 compressing), net-neutral, NIM drift 4.20% → 4.10-4.15% |
| `research/threads/RESG_MIX_DETERIORATION.md` | Apr 22 linear projection RETRACTED (Apr 23). Real indicators: substandard migration, past-due regime change, NCO tempo. |
| `research/threads/RESG_CONCENTRATION_VERIFICATION.md` | "88%" = phantom (no such disclosed figure). 6-qtr primary trend pinned: unfunded share 79%→60%, commitments −19% from peak, runoff H2'25-accelerating. Feeds the OZK-07 Jul-21 discriminator. (2026-07-04) |

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
| `INSIDERS/` | Insider trading analysis, FDIC EFR pulls (cert #110 — NOT SEC EDGAR), departures tracker |
| `PRIVATE_CREDIT/` | Affinius/NDFI counterparty risk + `COUNTERPARTY_WATCH.md` (Bluerock TI+ node — TI+ NAV mark leads OZK RaDD credit) |

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
| `archive/AUDIT_REPORT.md`, `archive/AUDIT_REPORT_MAR23.md`, `archive/AUDIT_MAR25.md` | Old audits — superseded by CHANGELOG |
| `archive/GAP_CLOSURE_PLAN.md`, `archive/GAP_ANALYSIS_REPORT.md` | Pre-Q1 gap work complete |
| `archive/STRUCTURE_AUDIT.md`, `archive/RESTRUCTURE_REVIEW.md` | KB migration complete |
| `archive/OZK_THESIS_FEB25.md` | Feb 25 thesis snapshot (pre-v1.0 baseline) |
| `archive/EVIDENCE.md` | Legacy evidence doc |
| `archive/TEMPLE8_SHORT_THESIS_MAR2026.md` | External short thesis (not our analysis) — archived Phase 1 |
| `archive/INSTITUTIONAL_OWNERSHIP_PLAN.md` | FDIC EFR + KB-142-146 work integrated — archived Phase 1 |
| `archive/EXTERNAL_PROMPTS.md` | Q1 prompts resolved — archived Phase 1 |
| `archive/MARKET/` | Mar 24 charts + abandoned trade log, superseded by darkpool/short_vol tools — archived Phase 3 |
| `archive/THREAD3_ROLL_MATH.md` | May $42.5P roll math — dead (May 8 deadline + May 15 expiry passed unlogged) — archived 2026-07-06 |
| `archive/AUDIT_2026-04-24.md` | One-off tree audit deliverable (was top-level `AUDIT.md`) — archived 2026-07-06 |
| `archive/KB_INDEX_AUDIT.md` | Point-in-time KB index audit — archived 2026-07-06 (rollup drift it flagged was fixed same day) |

### Workbook
| File | Content |
|------|---------|
| `workbook/KB.tsv` | Evidence database — 222 rows / 33 groups (as of 2026-08-07; 088/091 schema-repaired, 055/138 REFUTED-demoted 7/6) |
| `workbook/KB_INDEX.md` | Cluster navigator (all 33 groups indexed; reconciled 7/18) |
| `workbook/KB_MIGRATION_LOG.md` | Audit trail (KB migration provenance) |
| `workbook/PREDICTIONS.tsv` | Pre-registered falsifiable reads OZK-01→09 (05-09 + 01 resolve at Q2 print Jul 21) |

---

## Update Rules

| What Changed | Where | Don't Touch |
|---|---|---|
| A number / data point | `workbook/KB.tsv` | THESIS.md (references KB rows by ID) |
| Narrative / framing | `THESIS.md` + append to `CHANGELOG.md` | KB (data doesn't change because framing did) |
| Thesis-level shift | `THESIS.md` + **MUST** append `CHANGELOG.md` w/ version bump | — |
| New research output | `research/threads/` (post-Q1) or `research/C*/D*` (pre-Q1 rebuttals) | Top level — top level is for core pointers + active deep dives |
| Position change | `STATUS.md` + update `IQHQ_PLAYBOOK §6` if related to IQHQ | Don't duplicate in multiple places |
| Session ending | `MEMORY.md` — session handoff notes | INDEX.md (let it stabilize) |

**Research-threads rule:** Threads move to `research/threads/` on creation. Insight gets synthesized into THESIS.md (2-3 sentences + pointer). If the thread's core claim is later retracted or superseded, mark it in `CHANGELOG.md` — don't delete the thread file.

---

*This file is the entry point. If you're an agent spawning cold, read this first, then follow the boot sequence.*

**Last tree-hygiene pass: 2026-07-06 (staleness sweep).** INDEX re-based (Call Report figures, boot.py sequence, PREDICTIONS OZK-01→09, KB 200/28); `THREAD3_ROLL_MATH.md` (dead — May roll passed) + `AUDIT.md` (→ `AUDIT_2026-04-24.md`) + `workbook/KB_INDEX_AUDIT.md` moved → `archive/`; refuted-figure sweep run (INSIDERS/TIMELINE Aug-2028 + 284K, THESIS/SCENARIOS re-based to Call Report, KB-055/138 demoted REFUTED); KB_INDEX 12 missing groups added; fresh FDIC insider pull integrated (INSIDERS/ refreshed, KB-200).

**Prior pass: 2026-04-23 (Phase 1-3 restructure).**
- **Phase 1** — 4 top-level orphans → `archive/` (AUDIT_MAR25, TEMPLE8, INSTITUTIONAL_OWNERSHIP_PLAN, EXTERNAL_PROMPTS). 15 → 11 top-level .md files.
- **Phase 2** — `sources/` prune: 50+ files → 10 primary-source extracts. Raw LLM outputs (30 files) → `raw/llm_outputs/`. Raw OZK PDFs renamed to snake_case in `raw/`. 15 superseded V1-V3 drafts deleted (~2,700 lines). Earnings call transcript → `raw/Q1_2026_earnings_call_transcript.md`.
- **Phase 3** — Subdomain cleanup: `MARKET/` → `archive/MARKET/` (abandoned Mar 24). `GEOGRAPHY/FL_PARADOX/` sub-sub flattened to single `GEOGRAPHY/FL_PARADOX.md`. 5 → 4 subdomains.
- **Storage tier contract:** `sources/` = primary-source extracts (FDIC/FFIEC/10-K). `raw/` = unedited PDFs + transcripts. `raw/llm_outputs/` = LLM research provenance. `historical/` = quarterly Mgmt Comments extracts for trajectory. `archive/` = completed/dead work — never read at boot.

Earlier passes: 2026-04-22 — moved EARNINGS_PREP → archive/, moved Apr 22 threads → research/threads/.*
