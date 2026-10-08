# OZK — Agent Index
**Start here on cold boot.**

**Last updated:** 2026-09-24 (full pass — snapshot, file map and counts re-based to STATUS; mirror tokens: thesis **v1.5**, KB **240 / 37** — KB tokens re-synced 2026-09-27). Header history → `git log -p -- AGENTS/OZK/INDEX.md`.

**State snapshot** *(numbers live in `STATUS.md` — this is orientation only)*:
- **Thesis v1.5 RESERVOIR — Q2 DIRECTIONALLY CONFIRMED, conviction 🔴🔴 HIGH.** Stress accumulates in the portfolio until recognition; v1.5 = recognition is appraisal-gated and back-loaded. Q2 fired the adverse-selection tell (classified up while RESG shrank). → `THESIS.md`, `CHANGELOG.md`
- **IQHQ RaDD ($555M funded, one credit):** stated maturity 8/26 was **bridged to Fri 10/9** by a Fifth Modification signed 9/30–10/1 (Citi 10/6, single-source; swept and empty on 8/31 for what was public); multi-year extension + recap in negotiation per the 7/22 call; next read = the Q3 call's "~92-day" report-back. **OZK-09 45%**, A30/B45/C8/D17, Option-2 window runs to the Q4'26 print. → `IQHQ_PLAYBOOK.md`, `workbook/PREDICTIONS.tsv`
- **Second pillar = the RESG debt-on-debt book** (Will-ruled 8/23, as SUBJECT): $1.20B → $0.43B in 12 months (6/25 → 6/26), then **$42.4M charge-offs H1-26** (first in 18 qtrs). L181 verdict 9/24: reported decline OBSERVED, runoff INFERRED, reclassification NOT EXCLUDED. → `MI3_2025Q3_ADJUDICATION.md` §6
- **⚠️ Two facts cold spawns get wrong:** (1) **OZK files Form 10-Q with the FDIC (cert #110), not the SEC** — there is no *SEC* 10-Q, and the FDIC 10-Qs (`raw/Q*_10Q.pdf`) are this desk's best primary. (2) **The 37.6% MI3 "worst in screen" figure is dead** (live 9.35%, rank 5th/14) — never cite it.
- **Positions: one line observed** — Fidelity OZK Nov-20 $40P ×4 in the 10/7 capture (acquisition unknown; no card — TERRY). The Aug-21 puts expired worthless 8/21. ⛔ D1/OZK-salvage ruled closed. → `POSITIONS.md`
- **Next dates:** Oct 1 sub-notes reprice (watch `scripts/flng_watch.py`; read Fri 10/2) · ~Sep 30 Q3 date · ~mid/late Oct Q3 earnings + call · ~Nov Q3 Call Report. → `CALENDAR.md`
- **KB.tsv: 244 rows / 37 groups** (10/8).

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
| `Q1_2026_ANALYSIS.md` | Q1'26 earnings synthesis (Apr 21). Q2'26 grade → `workbook/Q2_2026_SCORING_CARD.md` |
| `TODO.md` | Research queue + prioritization |
| `POSITIONS.md` / `TRADE.md` | Option positions (one line observed 10/7: Nov-20 $40P ×4) / trade ideas (separately frozen) |
| `scripts/boot.py` | Boot kit v0.2 — prices, FDIC filings watch, catalysts, standing watch, inbox, staleness |
| `scripts/flng_watch.py` | FDIC filings watch (cert 110) — rc 0 quiet / 1 new / 2 unknown; `--selftest` |
| `workbook/KB.tsv` | Evidence database (244 rows / 37 groups as of 2026-10-08) |
| `workbook/CALL_REPORT_SERIES.tsv` | **FFIEC Call Report series, 18 quarters** (RSSD 107244) — MI3 both bases, past-due decomposition, NCO, CRE NCO, OREO/NPA. LOG-ONLY source (Z6 never re-grades off it). |
| `MI3_2025Q3_ADJUDICATION.md` | **L181 verdict** (2025Q3 MI3 step = debt-on-debt book decline; §6.5 layers OBSERVED / INFERRED / NOT EXCLUDED) |
| `SWEEP_2026-08-28.md` | Will-directed data-integrity sweep (22 findings) |
| `REGINALD_CHANNEL.md` | REGINALD ↔ OZK pair log |
| `CALL_REPORT_2026Q2_LOG.md` | Q2-2026 Call Report working: MI3 baseline contradiction, kill-§1 adjudication, basis-fork check, frame-spec check, proposals P-OZK-1..5. |
| `workbook/KB_INDEX.md` | KB cluster navigator |
| `workbook/PREDICTIONS.tsv` | Pre-registered falsifiable reads OZK-01→09 — Q2 cycle graded (5 resolved, Brier 0.1987); OZK-02/03/04 resolve at the Q4'26 print; **OZK-09 open at 45%** |

### Active deep dives (read on-demand)
| File | When to Read |
|------|-------------|
| `IQHQ_PLAYBOOK.md` | RaDD resolution tree (A/B/C/D), weighted EL ~$129M |
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
| `research/threads/ATRIUM_LIFESCI_ASSET_MAP.md` | Atrium life-sci asset map — OZK↔Affinius co-lending (777 Industrial $95M), Portal 405, Southline (7/6) |
| `research/threads/IQHQ_AUG_WINDOW_CLOSE_SWEEP.md` | Aug-2026 RaDD window close — SWEPT AND EMPTY, per-instrument ledger (8/31) |
| `research/threads/2026-09-24_CATCHUP_SWEEP.md` | 24-day catch-up: filings, insiders, SI, news, AM re-check (9/24) |
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
| `raw/` | Raw OZK PDFs — Mgmt Comments Q4'24–Q4'25 + Q1'26 · **FDIC 10-Qs Q2'25, Q3'25, Q1'26, Q2'26** · Q2'26 8-K bundle · Q1'26 supplement + transcript |
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
| `workbook/KB.tsv` | Evidence database — 244 rows / 37 groups (as of 2026-10-08) |
| `workbook/KB_INDEX.md` | Cluster navigator (all 37 groups indexed; verified 9/24) |
| `workbook/CALL_REPORT_SERIES.tsv` | FFIEC 18-quarter series (see Core) |
| `workbook/Q2_2026_SCORING_CARD.md` | Q2'26 Stage-1/Stage-2 grades |
| `workbook/KB_MIGRATION_LOG.md` | Audit trail (KB migration provenance) |
| `workbook/PREDICTIONS.tsv` | Pre-registered reads OZK-01→09 (see Core) |

---

## Update Rules

| What Changed | Where | Don't Touch |
|---|---|---|
| A number / data point | `workbook/KB.tsv` | THESIS.md (references KB rows by ID) |
| Narrative / framing | `THESIS.md` + append to `CHANGELOG.md` | KB (data doesn't change because framing did) |
| Thesis-level shift | `THESIS.md` + **MUST** append `CHANGELOG.md` w/ version bump | — |
| New research output | `research/threads/` (post-Q1) or `research/C*/D*` (pre-Q1 rebuttals) | Top level — top level is for core pointers + active deep dives |
| Position change | `POSITIONS.md` + STATUS §Positions (TERRY builds, Will approves) | Don't duplicate in multiple places |
| Session ending | `MEMORY.md` — session handoff notes | INDEX.md (let it stabilize) |

**Research-threads rule:** Threads move to `research/threads/` on creation. Insight gets synthesized into THESIS.md (2-3 sentences + pointer). If the thread's core claim is later retracted or superseded, mark it in `CHANGELOG.md` — don't delete the thread file.

---

*This file is the entry point. If you're an agent spawning cold, read this first, then follow the boot sequence.*

**Last INDEX pass: 2026-09-24** (snapshot + file map re-based; added MI3 adjudication, 8/28 sweep, REGINALD channel, Q2 scoring card, flng_watch, 3 threads, 10-Q PDFs). **Last tree-hygiene pass: 2026-07-06 (staleness sweep).** INDEX re-based (Call Report figures, boot.py sequence, PREDICTIONS OZK-01→09, KB 200/28); `THREAD3_ROLL_MATH.md` (dead — May roll passed) + `AUDIT.md` (→ `AUDIT_2026-04-24.md`) + `workbook/KB_INDEX_AUDIT.md` moved → `archive/`; refuted-figure sweep run (INSIDERS/TIMELINE Aug-2028 + 284K, THESIS/SCENARIOS re-based to Call Report, KB-055/138 demoted REFUTED); KB_INDEX 12 missing groups added; fresh FDIC insider pull integrated (INSIDERS/ refreshed, KB-200).

**Prior pass: 2026-04-23 (Phase 1-3 restructure).**
- **Phase 1** — 4 top-level orphans → `archive/` (AUDIT_MAR25, TEMPLE8, INSTITUTIONAL_OWNERSHIP_PLAN, EXTERNAL_PROMPTS). 15 → 11 top-level .md files.
- **Phase 2** — `sources/` prune: 50+ files → 10 primary-source extracts. Raw LLM outputs (30 files) → `raw/llm_outputs/`. Raw OZK PDFs renamed to snake_case in `raw/`. 15 superseded V1-V3 drafts deleted (~2,700 lines). Earnings call transcript → `raw/Q1_2026_earnings_call_transcript.md`.
- **Phase 3** — Subdomain cleanup: `MARKET/` → `archive/MARKET/` (abandoned Mar 24). `GEOGRAPHY/FL_PARADOX/` sub-sub flattened to single `GEOGRAPHY/FL_PARADOX.md`. 5 → 4 subdomains.
- **Storage tier contract:** `sources/` = primary-source extracts (FDIC/FFIEC/10-K). `raw/` = unedited PDFs + transcripts. `raw/llm_outputs/` = LLM research provenance. `historical/` = quarterly Mgmt Comments extracts for trajectory. `archive/` = completed/dead work — never read at boot.

Earlier passes: 2026-04-22 — moved EARNINGS_PREP → archive/, moved Apr 22 threads → research/threads/.*
