# OZK — File Tree Audit (First OZK Session)

**Date:** 2026-04-24 | **Auditor:** OZK (fresh spawn, post-spinout) | **Scope:** Full tree — spinout validation, bloat, staleness, gaps

---

## TL;DR

- **Spinout is 95% clean.** Identity chain, cross-refs, git scope all pass. Two residual gaps: Step 15 (plan not archived) and Step 14 (REGINALD trim partial).
- **Context at boot is well-calibrated.** STATUS+LESSONS+CALENDAR+MEMORY = ~235 lines. Not bloated.
- **Main issues are small drifts, not structural.** Three broken refs, two stale snapshots, one Mar-7-vintage doc (TRADE.md) that probably should be retired.
- **Knowledge base is the highest-leverage bloat risk.** KB_INDEX.md is 37 rows behind (159 indexed vs 196 in KB.tsv) and already self-flagged.

---

## 1. Spinout Validation (Step 13)

Ran the 7-point checklist from `AGENTS/REGINALD/OZK_SPINOUT_PLAN.md` §10:

| # | Check | Result |
|---|-------|--------|
| 1 | Identity: "I am OZK" | ✅ |
| 2 | File ownership at root | ✅ all expected files present (CLAUDE, MEMORY, CALENDAR, LESSONS, POSITIONS, TRADE, STATUS, THESIS, etc.) |
| 3 | CLAUDE.md chain loads root + OZK/CLAUDE.md only (no REGINALD interference) | ✅ |
| 4 | Boot sequence runs clean (STATUS / LESSONS / CALENDAR / MEMORY / market.py / inbox) | ✅ |
| 5 | Cross-ref `../REGINALD/STATUS.md` resolves | ✅ |
| 6 | Outbox write test | ⏭️ skipped (didn't want to pollute with a test file) |
| 7 | Git scope clean | ✅ |

### Residual gaps from the 16-step plan

**🔴 Step 15 — NOT DONE.** `OZK_SPINOUT_PLAN.md` is still at `AGENTS/REGINALD/OZK_SPINOUT_PLAN.md`. Plan §6 Step 15 calls for `git mv` to `AGENTS/OZK/archive/OZK_SPINOUT_PLAN.md`. **This creates a broken ref:** `OZK/CLAUDE.md:6` cites `archive/OZK_SPINOUT_PLAN.md` — the file doesn't exist at that path.

**🟠 Step 14 — PARTIAL.** `REGINALD/STATUS.md` "RESEARCH — OZK" section (lines 327-349) is still ~23 lines of deep Q1 26 numbers. Plan §6 Step 14 + D5 calls for reduction to 5-10 line snapshot + pointer to `../OZK/STATUS.md` with a "Refreshed from OZK/STATUS.md YYYY-MM-DD" note. Right now REGINALD and OZK both own the same Q1 26 deep numbers — that's a drift risk.

---

## 2. Bloat Assessment

**Not bloated at the boot surface.** Boot reads total ~235 lines (STATUS 95 + LESSONS 40 + CALENDAR 51 + MEMORY 49). Deep docs (THESIS 188, CHANGELOG 191, IQHQ_PLAYBOOK 279, SEVEN_CREDIT 300, Q1_ANALYSIS 330) are gated behind explicit navigation — correct.

**Potential bloat candidate:**

**🟡 TRADE.md — Mar 7 vintage with bolted-on Apr 24 annotations.** Structural mismatch: sections 1/3/4/5/6 are Mar 7 REGINALD-vintage prose (pre-Q1, pre-Thread 3 roll math, assumes 4-contract position vs actual 11) with `📌 Current state` paragraphs patched on to keep it "correct." SECTION 2 is missing entirely (non-OZK trades filtered out during REGINALD extraction). The "historical conviction record" framing is debatable — POSITIONS.md is the live state, THREAD3_ROLL_MATH.md owns roll execution, IQHQ_PLAYBOOK.md owns strategy rationale. TRADE.md currently has no unique role. **Recommendation:** either shrink to a one-page "current conviction + sizing rules" (kill Mar 7 content) or archive it entirely.

**Not bloat (verified healthy):**
- `archive/` — 14 files / 2,809 lines. All Mar-25/Mar-27 vintage, properly quarantined, README clear.
- `research/` — 16 files / 2,041 lines. Active deep dives + C1-3 rebuttals + D1-6 series + 3 post-Q1 threads. All load-bearing.
- `raw/` — 7 PDFs (~30MB) + transcript + 29 LLM research outputs in `llm_outputs/`. Storage, not read at boot. Fine.
- `sources/`, `historical/` — tight, primary-source extracts with clear README ownership.

---

## 3. Staleness — What's Drifted

| Location | Issue | Severity |
|----------|-------|----------|
| `INDEX.md:10` | "Positions: $42.5P Aug 21 × 1" — actual is ×3 per STATUS.md | 🟠 misleading |
| `STATUS.md:3` | Price $48.23 (Apr 23) — today live is $47.59 (-1.9%) | 🟡 normal session-delta, refresh at next session start |
| `Q1_2026_ANALYSIS.md:1` | Header says "REGINALD ANALYSIS" — should be OZK | 🟡 cosmetic |
| `SCENARIOS.md:4` | Short Interest data "last refresh Mar 25 — needs FINRA pull" | 🟡 self-flagged, not blocking |
| `TRADE.md` | Mar 7 vintage content throughout (see §2) | 🟡 see above |
| `workbook/KB_INDEX.md:3` | "Total rows: 159, Groups: 17" — actual KB.tsv has 196 rows (37 row drift) | 🟠 self-flagged in TODO.md H1 |
| `research/README.md` "Current Files" table | Lists "OZK Thesis Feb25" as being in `research/` — actually in `archive/` | 🟡 cosmetic |
| `INSIDERS/STATUS.md:2` | Updated 2026-04-12 — predates Q1 print. Intentional ("no material Q1 activity" per TODO.md) | 🟢 acknowledged |

---

## 4. Gaps — Broken Refs & Missing Files

| Ref | Where | Status |
|-----|-------|--------|
| `archive/OZK_SPINOUT_PLAN.md` | `CLAUDE.md:6` | ✅ **FIXED 2026-04-24** — executed Step 15 `git mv` from `AGENTS/REGINALD/` to `AGENTS/OZK/archive/`. |
| `workbook/PREDICTIONS.tsv` | `INDEX.md:134`, `TODO.md:110` | ✅ **FIXED 2026-04-24** — created with 4 OZK rows (OZK-01 through OZK-04) extracted from `REGINALD/workbook/PREDICTIONS.tsv` (formerly REG-16, 21, 22, 23). REG-17 stayed in REGINALD (multi-bank screen: WAL/OZK/EGBN). |
| `sources/FORGE_TRADE_STATUS.md` | Referenced in `sources/README.md:15` as expected broker-snapshot content | ✅ **FALSE ALARM** — auditor missed the README ref. Not orphan. |

---

## 5. What Works Well

- **File ownership table in `CLAUDE.md`** is clean and enforced. No doc-duplication ambiguity I can find.
- **Subdomain separation** (LIFE_SCI / GEOGRAPHY / PRIVATE_CREDIT / INSIDERS) is disciplined. Each has its own STATUS + README + deep files.
- **KB-OZK-xxx citation protocol** is threaded through THESIS, CHANGELOG, and SEVEN_CREDIT. Makes claims auditable.
- **CHANGELOG discipline:** v1.3 entry is thorough (what/why/old vs new/position implication). This is the kind of artifact a future session can actually use.
- **TODO.md** is well-maintained — resolved items marked, next priorities ranked, strategic framing at top, decision gate at bottom. Rare to see a TODO file this usable.
- **Subdomain refresh queue** (TODO.md §Hygiene) shows the Apr 23 PM session closed three subdirs cleanly — process is working.
- **LESSONS.md is tight at 40 lines, 7 rules.** Each has evidence + prevention rule. Not a dumping ground.

---

## 6. Recommended Priorities (if you want fixes)

In order of severity + cheapness:

1. ✅ ~~**🔴 Move spinout plan**~~ — DONE 2026-04-24.
2. ✅ ~~**🔴 Resolve PREDICTIONS.tsv**~~ — DONE 2026-04-24 (extracted per Option A).
3. **🟠 Trim REGINALD/STATUS.md OZK section** (10 min, needs Will approval since edits REGINALD): reduce 23 lines → 5-10 line snapshot + pointer. Completes Step 14.
4. **🟠 Update KB_INDEX.md rollups** (30-60 min): 159 → 196 rows. Self-flagged, not blocking but will bite a future session.
5. **🟠 Fix INDEX.md positions snapshot** (1 min): "$42.5P Aug 21 × 1" → "× 3".
6. **🟡 Decide on TRADE.md:** shrink, archive, or keep as-is. I'd vote archive — POSITIONS + THREAD3 + IQHQ_PLAYBOOK cover the live ground.
7. ✅ ~~**🟡 Orphan check:** `sources/FORGE_TRADE_STATUS.md`~~ — false flag; it's documented in sources/README.md.
8. **🟡 Cosmetic:** Q1_2026_ANALYSIS.md header "REGINALD" → "OZK"; research/README.md Feb25 table row fix.

Items 5+8 total ~2 minutes of mechanical cleanup. Items 3+4+6 are judgment calls that benefit from Will's read.

---

## 7. Open Questions for Will

1. **PREDICTIONS.tsv** — does this file exist at `REGINALD/workbook/` or was the OZK scaffolding planned-but-unbuilt? If planned-but-unbuilt, where should the predictions live (separate file vs KB.tsv status rows)?
2. **TRADE.md future** — keep Mar-7 historical content as "conviction record," shrink to live-state-only, or archive? No strong signal from my read of other agents' patterns.
3. **Step 14 authority** — I can't edit REGINALD files from OZK agent (git protocol). Should I flag this to REGINALD on next spawn, or to you directly?

---

*Audit complete. Nothing here is blocking the next session — these are hygiene items, not integrity failures. The spinout largely worked.*
