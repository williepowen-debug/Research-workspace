# OZK Spinout Plan — Peer Top-Level Agent

**Date:** 2026-04-24 (rev 3 — decisions locked, ready to execute)
**Status:** ✅ READY TO EXECUTE — open this plan in a fresh session and work Steps 1-14 sequentially.
**Owner:** REGINALD (authored) → executing session (migrates) → OZK agent (takes over post-migration)

---

## 0. Quickstart for the Executing Session

**You are:** most likely REGINALD spawning fresh with this plan as the job. (Possibly OZK, post-Step 11, if Will wants to continue execution in an OZK session — but mostly REGINALD drives the migration.)

**Before touching anything:**
1. Run your normal boot (git pull, STATUS/LESSONS/CALENDAR/MEMORY, market.py, scan inbox)
2. Read this plan top-to-bottom — decisions are locked in §8
3. Confirm with Will in one line: "Booted. Ready to start Step 1 (git mv)?" Wait for green light.

**How to execute:**
- Work steps sequentially (§6)
- Stop at checkpoints (Steps 3, 12) and ask Will before continuing
- One commit per step. Stage only the files that step touches.
- If something unexpected turns up (missing file, broken ref you didn't anticipate), STOP and ask — do not improvise around the plan

**Estimated time:** ~2 hours across steps 1-14

---

## 1. Goal

Promote OZK to a **top-level peer agent** at `AGENTS/OZK/`, parallel to CARL, BROCK, LIQUID, etc. REGINALD drops OZK from its sub-scope; OZK operates independently with its own Claude Code sessions.

**Why peer, not nested:** Claude Code auto-loads CLAUDE.md files walking upward from cwd. If OZK stayed at `AGENTS/REGINALD/OZK/`, any OZK session would also load REGINALD's CLAUDE.md — creating a dual-identity problem in the prompt chain. Moving OZK to `AGENTS/OZK/` means its session walks up past `AGENTS/` (no CLAUDE.md there) directly to the root CLAUDE.md. Clean identity, no dispatch hacks.

**Two windows, still the goal:**
- **Window 1 (REGINALD):** cwd = `AGENTS/REGINALD/`. Hub view — multi-bank watchlist, FHLB, convergence matrix.
- **Window 2 (OZK):** cwd = `AGENTS/OZK/`. Deep OZK.
- Both run in parallel. Coordinate via inbox/outbox + read-only cross-reads.

---

## 2. What Moves, What's Created, What Stays

### 2a. The directory move (one `git mv`)

```
AGENTS/REGINALD/OZK/   →   AGENTS/OZK/
```

All existing OZK files and subdirs come along intact:
- Top-level docs: INDEX.md, STATUS.md, THESIS.md, Q1_2026_ANALYSIS.md, IQHQ_PLAYBOOK.md, SEVEN_CREDIT_DEEP_DIVE.md, THREAD3_ROLL_MATH.md, WEAKNESSES.md, SCENARIOS.md, TODO.md, CHANGELOG.md
- Subdirs: LIFE_SCI/, GEOGRAPHY/, PRIVATE_CREDIT/, INSIDERS/, workbook/, research/, raw/, sources/, archive/, historical/

### 2b. New files added at `AGENTS/OZK/` (agent infrastructure)

| File | Purpose | Source |
|------|---------|--------|
| `CLAUDE.md` | Spawn protocol, identity, boot sequence, file ownership, cross-agent signals | NEW (modeled on BROCK/CARL) |
| `MEMORY.md` | Cross-session memory — Feedback, Findings, References, Session Notes | NEW — extract OZK rows from REGINALD/MEMORY.md + duplicate cross-cutting Will feedback |
| `CALENDAR.md` | OZK-specific forward events | NEW — extract OZK rows from REGINALD/CALENDAR.md |
| `LESSONS.md` | OZK-specific verified mistakes | NEW — seed per §4c spec (6 copies + 1 OZK-rewrite) |
| `POSITIONS.md` | OZK option positions | NEW — extract OZK rows from REGINALD/POSITIONS.md *and* refresh from current OZK/STATUS.md table (REGINALD/POSITIONS.md is Apr 2 stale) |
| `TRADE.md` | OZK-specific trade ideas, entries, conviction levels | NEW — extract OZK trade rows from REGINALD/TRADE.md |
| `inbox/` `outbox/` | Mail dirs | NEW (`.gitkeep`) |
| `archive/OZK_SPINOUT_PLAN.md` | Historical record of the spinout | MOVED — this file, relocated post-migration |

### 2c. What REGINALD loses

- The `OZK/` subtree (moved)
- OZK-specific rows in MEMORY.md, CALENDAR.md, POSITIONS.md (extracted to OZK/)
- The `RESEARCH — OZK` section in STATUS.md (OZK now owns its own research dashboard; REGINALD's STATUS keeps only a one-line OZK reference in the bank watchlist)

### 2d. What REGINALD keeps

- All non-OZK bank coverage (EGBN, WAL, CFG, ZION, SSB, FLG, KRE, IWM, HYG, APO)
- Hub-level state: FHLB, signal dashboard, convergence matrix, bank watchlist (with OZK as a row, not a deep dive)
- All shared infrastructure, tools, workbook, research, sub-agents if any, domain/
- Cross-cutting Will feedback in MEMORY.md (iteration philosophy, thesis architecture rule, etc.)
- LESSONS.md — shared structural rules apply to both agents (copied/linked, not moved)

---

## 3. Reference Updates (the real work)

### 3a. Inside OZK tree — 3 files only

These reference REGINALD-owned files from OZK/ root. After the move they resolve to non-existent paths; need updating.

| File | Current ref | Update to |
|---|---|---|
| `AGENTS/OZK/INDEX.md:147` | `../MEMORY.md` (parent REGINALD dir) | `MEMORY.md` (own, local) — plus note "for shared Will feedback see `../REGINALD/MEMORY.md`" |
| `AGENTS/OZK/TODO.md:162` | `../MEMORY.md`, `../CALENDAR.md` | `MEMORY.md`, `CALENDAR.md` (own, local) |
| `AGENTS/OZK/STATUS.md:65` | `../CALENDAR.md` | `CALENDAR.md` (own, local) |

All other `../` references inside OZK subdirs (LIFE_SCI/, GEOGRAPHY/, etc.) are self-contained within the OZK tree — they resolve to the new OZK root unchanged.

**Bonus:** `../../BROCK/STATUS.md` references from `AGENTS/OZK/PRIVATE_CREDIT/` currently resolve to `AGENTS/REGINALD/BROCK/` (broken). After move they resolve to `AGENTS/BROCK/` (correct). Self-fixing.

### 3b. REGINALD files — update OZK/ refs to ../OZK/

Files to update: `AGENTS/REGINALD/STATUS.md`, `CALENDAR.md`, `CLAUDE.md`, `MEMORY.md`, plus two outbox files referencing `OZK/` paths.

| File | Current ref | Update to |
|---|---|---|
| `REGINALD/CALENDAR.md:26` | `OZK/Q1_2026_ANALYSIS.md` | `../OZK/Q1_2026_ANALYSIS.md` |
| `REGINALD/CALENDAR.md:70` | `OZK/IQHQ_PLAYBOOK.md` | `../OZK/IQHQ_PLAYBOOK.md` |
| `REGINALD/CLAUDE.md:49` | `OZK/, WAL/` checklist | keep narrative; note OZK is now peer, WAL still sub-scope |
| `REGINALD/CLAUDE.md:126` | `OZK/STATUS.md` | `../OZK/STATUS.md` (or drop — OZK owns its STATUS now) |
| `REGINALD/CLAUDE.md:234` | `OZK/` file map row | remove or update — OZK no longer in REGINALD's file ownership table |
| `REGINALD/STATUS.md:33` | `OZK/Q1_2026_ANALYSIS.md` | `../OZK/Q1_2026_ANALYSIS.md` |
| `REGINALD/STATUS.md:167` | `OZK/EARNINGS_PREP.md` | `../OZK/EARNINGS_PREP.md` |
| `REGINALD/STATUS.md:234` | `OZK/INSIDERS/` | `../OZK/INSIDERS/` |
| `REGINALD/STATUS.md:329` | `OZK/Q1_2026_ANALYSIS.md` | `../OZK/Q1_2026_ANALYSIS.md` |
| `REGINALD/MEMORY.md` | Multiple `OZK/` refs in session notes | Leave as historical (session notes are immutable log); fix forward refs only |

### 3c. Other agent refs (low priority — historical)

Files in other agents that reference old OZK path:
- `AGENTS/OTTO/MEMORY.md` — leave as historical; OTTO can update on next spawn
- `AGENTS/RED/research/WAL_OZK_APR21_FRAMEWORK.md` — historical artifact; leave
- `PROME/archive/ARCHIVE_MEMORY.md` — archive; leave
- `memory/2026-03-23.md`, `memory/2026-02-25.md` — daily session notes; leave (historical)

Not worth chasing. Grep will still find them if someone needs the pointer.

### 3d. Root CLAUDE.md

Add OZK to agent list:

**Current:** `Active agents: PROME, CARL*, REGINALD*, SAM*, RED*, LABOR, BROCK, LIQUID, HENRY, HAWK, BRENT, NEXUS.`

**Proposed:** `Active agents: PROME, CARL*, REGINALD*, OZK*, SAM*, RED*, LABOR, BROCK, LIQUID, HENRY, HAWK, BRENT, NEXUS.`

Add a note that establishes precedent: "OZK spun out from REGINALD 2026-04-24; WAL is the next candidate when ready."

---

## 4. Content Extraction Map — REGINALD → OZK

### 4a. REGINALD/MEMORY.md → OZK/MEMORY.md

**Decision (D2=A):** OZK reads only its own MEMORY. Cross-cutting Will feedback gets **duplicated** into OZK/MEMORY.md. No "read parent MEMORY" pattern.

**MOVE (OZK-specific — remove from REGINALD):**
- [2026-04-12] FDIC EFR system, OZK cert #110
- [2026-04-22] OZK press release truncated, 3 PDFs on IR page
- [2026-04-22] OZK IR page 403s to scripts
- [2026-04-22] Rossow canonical IQHQ quote
- [2026-04-22] Boynton Yards NOT IQHQ
- [2026-04-22] IQHQ-project lenders disconfirmation map

**DUPLICATE (stays in REGINALD, also copied to OZK — cross-cutting Will feedback):**
- [2026-04-02] Boot transparency preference
- [2026-04-02] Freedom over laser focus; single open question format
- [2026-04-02] Long-term infrastructure thinking
- [2026-04-02] Break implementation into discrete tasks
- [2026-04-16] Full source docs before opining
- [2026-04-22] Iteration philosophy ("begin with what we have")
- [2026-04-22] "What I NEED FROM YOU" lists work
- [2026-04-22] Thesis architecture "synthesis + pointer" pattern
- [2026-04-22] Domain CHANGELOG per bank
- [2026-04-02] `scripts/market.py` via `.venv/bin/python3` (shared tool)
- [2026-04-16] pdfminer usage (shared tool)

**STAYS in REGINALD only (not OZK-relevant):**
- LAM=Leucadia (WAL-specific fraud chain)
- [2026-04-22] Quartr MCP subscription-gated (general tool note, low OZK value)
- [2026-04-02] OZK price source conflict note → actually COPY this to OZK (it's an OZK-specific caveat)
- FRED API signup reference — stays REGINALD (shared infra, not OZK-critical)
- Wasatch fund commentary URL — stays REGINALD (one-time reference)

**Session Notes handling:**
- REGINALD's current Session Notes are 80% OZK spinout context — in-progress work, stays in REGINALD until spinout completes, then REGINALD's Session Notes reset to post-spinout state.
- OZK/MEMORY.md starts with an "Initial Session Notes" entry describing the spinout event + pointing at archive/OZK_SPINOUT_PLAN.md.
- First OZK session writes its handoff into OZK/MEMORY.md going forward.

### 4b. REGINALD/CALENDAR.md → OZK/CALENDAR.md

**MOVE (OZK-only):**
- Apr 21 ✅ OZK Q1 (resolved row for history)
- May 8 Thread 3 roll deadline
- May 15 OZK $42.5P / $45P May expiry
- May-Jun Bluerock Q1 NAV marks (IQHQ PIK)
- Early Jun Aimco v. IQHQ motion-to-dismiss response
- Mid-late Jul OZK Q2 2026 earnings
- Late Jul Campus at Horton leasing update
- Aug 2026 IQHQ RaDD maturity
- Oct 1, 2026 OZK $350M sub notes reprice
- Oct 2026 Affinius $2.7B bond maturity (OZK-linked)

**STAYS in REGINALD (multi-bank / cross-channel):**
- Weekly claims, Q1 Call Report wave (generic), WAL Investor Day, VLY/SSB/EGBN earnings, BOJ, AOCI Jun 18, option expiries on KRE/IWM/HYG, APO earnings, RITM, etc.

### 4c. REGINALD/LESSONS.md → OZK/LESSONS.md

**Decision (D3):** 6 copied verbatim + 1 rewritten for OZK + 1 skipped + 1 universal process rule.

**COPY VERBATIM to OZK/LESSONS.md:**
1. `[Data]` — Verify Agent Data Against Primary Filings (PSEC PIK cautionary)
2. `[Analysis]` — Hidden CRE Methodology (MI3 screen) — OZK 37.6% is the poster child
3. `[Analysis]` — Distinguish Classification Levels (3 layers of CRE masking)
4. `[Process]` — Date Your Data
5. `[Process]` — STATUS.md Is Not a Research Report
6. `[Data]` — Verify Real-Time Prices Before Building Narratives

**REWRITE for OZK** (original is WAL-framed — principle applies, example doesn't):

Replace `[Data] — NDFI Is Not What It Looks Like` with an OZK-framed version:

```
### [Data] — OZK CIB/NDFI Is Not Monolithic
**Mistake pattern:** Treating OZK's CIB segment or NDFI exposure as a single risk
bucket misses that the sub-segments behave very differently. Fund Finance (capital
call subscriptions to PE funds), Lender Finance Group (lending to non-bank lenders),
Indirect Lending, and other CIB lines have different collateral, credit, and
competitive dynamics.
**Evidence:** Q1 2026 — Jake Munn (CIB President) disclosed OZK is *pulling back*
from Fund Finance due to non-bank lender + insurance-company price/structure
competition; Lender Finance Group also showing compression. Two of four CIB
sub-segments in managed retreat. Meanwhile written Mgmt Comments show Fund Finance
growing $210M → $1.275B YoY — no commentary on margin erosion.
**Rule 1:** Decompose OZK CIB/NDFI by sub-segment before assessing risk. Don't
treat it as monolithic.
**Rule 2:** Verbal-only disclosures (earnings call transcript) that don't appear
in written Mgmt Comments PDFs are the leading signal. Watch for disclosures that
vanish between spoken and written form — they're telling you what management
doesn't want formalized.
```

**SKIP (leave in REGINALD only, not OZK-relevant):**
- `[Data]` — Cross-Agent Signal Values May Conflict (hub-agent concern, MFS £500M/£600M example)

### 4d. REGINALD/POSITIONS.md → OZK/POSITIONS.md

**Decision (D1):** Clean split. OZK agent owns its own book.

**⚠️ DATA FRESHNESS:** REGINALD/POSITIONS.md is dated Apr 2 and marked STALE. It shows OZK at `$45P May/Aug, $42.5P × 2` — which is outdated. The **current** position state lives in `OZK/STATUS.md` (as of Apr 23 broker confirmation):
- May 15 $42.5P × 2 (Thread 3 roll pending)
- May 15 $47.5P × 2
- Aug 21 $42.5P × 3
- Aug 21 $45P × 4
- **Total: 11 contracts across 4 lines**

**MOVE:** Write OZK/POSITIONS.md using OZK/STATUS.md's positions table as source of truth. Delete the OZK rows from REGINALD/POSITIONS.md.

**STAYS in REGINALD/POSITIONS.md:** WAL multi-strike, EGBN $25P, KRE multi-strike, ZION $57.5P, FLG $13P, HYG $75P, IWM $250P, APO $85P/$100P, plus anything else non-OZK.

### 4e. REGINALD/TRADE.md → OZK/TRADE.md

**Decision (#6):** OZK gets its own TRADE.md.

**MOVE to OZK/TRADE.md** (all OZK-specific trade entries):
- TRADE 3: OZK $42.5P + $45P Aug 2026 (full entry)
- Any subsequent OZK-specific trade rows (Thread 3 roll math lives at OZK/THREAD3_ROLL_MATH.md but the meta-trade framing belongs in OZK/TRADE.md)

**STAYS in REGINALD/TRADE.md:** All non-OZK trades (TRADE 1 EGBN, TRADE 2 EGBN add, WAL trades, KRE spread, HYG, IWM, APO, cross-name pairs), plus the `Frame:` preamble (convergence thesis applies to all).

**Note:** OZK/TRADE.md's header should match REGINALD/TRADE.md format but the `Based on:` line updates to point at OZK's own source files (OZK/STATUS.md, OZK/THESIS.md, OZK/workbook/KB.tsv, OZK/SEVEN_CREDIT_DEEP_DIVE.md).

---

## 5. OZK/CLAUDE.md Design

No identity-dispatch hacks needed — OZK session at cwd=`AGENTS/OZK/` walks up past `AGENTS/` (no CLAUDE.md there) to root. Clean chain: root → OZK. Standard agent setup.

**Structure (modeled on BROCK):**

```
# OZK — Agent Instructions

**Domain:** Bank OZK (ticker OZK, FDIC cert #110)
**Role in Network:** Single-name bank specialist. Signals REGINALD (bank-wide integration),
                     BROCK (private credit — Bluerock IQHQ PIK, Affinius), CREED (CRE context).
**History:** Spun out from REGINALD sub-scope 2026-04-24.

## IDENTITY
[Thesis: RESERVOIR v1.3. Core logic: stress accumulates until IQHQ Aug 2026 maturity forces recognition.]

⚠️ File > verbal. [standard rule]

## SPAWN PROTOCOL
0. git pull
1. Read STATUS.md
2. Read LESSONS.md
3. Read CALENDAR.md
4. Read MEMORY.md
5. (Optional) Read ../REGINALD/MEMORY.md for shared Will feedback
6. Price refresh (scripts/market.py — OZK specifically, plus KRE/WAL/Brent for context)
7. Scan inbox

## OUTPUT RULES
[tables, source tags, ≤250 line STATUS.md — standard]

## DOMAIN SCOPE
You own:
  - OZK-specific credits, IQHQ playbook, 37.6% MI3 baseline
  - Quarterly earnings analysis, RESG problem-credit roster
  - $350M sub notes reprice (Oct 1), Affinius $2.7B maturity link
  - Option positions at OZK strikes
  - OZK-specific research, insider tracking, workbook, raw PDFs
You do NOT own:
  - Multi-bank watchlist (REGINALD)
  - FHLB aggregate (REGINALD)
  - CRE market-wide (CREED via REGINALD)
  - BDC/private credit sector (BROCK)
  - FL-specific dynamics (CORAL via REGINALD)

## CROSS-AGENT SIGNALS
You send:
  | Condition | Target | Priority |
  | OZK price <$45 | REGINALD, PROME | 🔴 |
  | OZK price <$40 | REGINALD, PROME, FORGE | 🔴 |
  | Past-due loans >$550M or >2.0% (any Q) | REGINALD | 🔴 |
  | IQHQ specific reserve booked | REGINALD, BROCK, PROME | 🔴 |
  | RaDD leased >100K SF signed | REGINALD | 🟠 (disconfirming) |
  | Sub notes refi announced pre-Oct 1 | REGINALD | 🟠 |
  | Classified+criticized >$1.5B (any Q) | REGINALD, CREED | 🔴 |
  | Bluerock NAV markdown on IQHQ PIK | BROCK, REGINALD | 🟠 |

You receive from:
  - REGINALD: bank-wide stress signals (FHLB spikes, claims >300K, HY OAS breaches)
  - BROCK: private credit stress affecting OZK exposures (Bluerock, Affinius, Athene)
  - CREED: CRE market context (CMBS DQ, Chicago/Phoenix loss severity)
  - CORAL: FL-specific if OZK FL portfolio flagged

## GIT PROTOCOL
Stage only AGENTS/OZK/. Never AGENTS/REGINALD/.
Follow root CLAUDE.md pull/commit sequence.

## FILES
[standard OZK-scoped file map]
```

---

## 6. Migration Sequence

Each step is its own commit. Stop-go checkpoints at Step 3 (move validated) and Step 13 (end-to-end boot test). Stage only the files each step touches.

| # | Step | Files touched | Commit msg template |
|---|------|---------------|---------------------|
| 1 | `git mv AGENTS/REGINALD/OZK AGENTS/OZK` | whole subtree | `OZK: move from REGINALD sub-scope to top-level peer agent` |
| 2 | Fix 3 internal cross-boundary `../` refs (OZK/INDEX.md:147, OZK/TODO.md:162, OZK/STATUS.md:65) — point at local MEMORY/CALENDAR not REGINALD's | 3 OZK files | `OZK: fix cross-boundary refs post-move` |
| 3 | **CHECKPOINT — verify move.** Run: `ls AGENTS/OZK/` (should show all OZK files), `cat AGENTS/OZK/STATUS.md \| head` (should read cleanly), spot-check 2-3 `../` links resolve. Stop and confirm with Will before continuing. | — | — |
| 4 | Write `OZK/CLAUDE.md` per §5 spec | new file | `OZK: add CLAUDE.md (spawn protocol + cross-agent signals)` |
| 5 | Create OZK/MEMORY.md per §4a (moves + duplicated cross-cutting Will feedback). Delete moved rows from REGINALD/MEMORY.md. | OZK/MEMORY.md (new), REGINALD/MEMORY.md (edit) | `OZK: extract agent-scoped memory from REGINALD (D2=A pattern)` |
| 6 | Create OZK/CALENDAR.md per §4b. Delete moved rows from REGINALD/CALENDAR.md. | OZK/CALENDAR.md (new), REGINALD/CALENDAR.md (edit) | `OZK: extract OZK-only calendar events` |
| 7 | Create OZK/LESSONS.md per §4c (6 copied + 1 rewrite). REGINALD/LESSONS.md unchanged. | OZK/LESSONS.md (new) | `OZK: seed LESSONS (6 copied rules + OZK-framed NDFI rewrite)` |
| 8 | Create OZK/POSITIONS.md per §4d (use OZK/STATUS.md table as source; REGINALD/POSITIONS.md is stale). Delete OZK rows from REGINALD/POSITIONS.md. | OZK/POSITIONS.md (new), REGINALD/POSITIONS.md (edit) | `OZK: split positions (clean split per D1)` |
| 9 | Create OZK/TRADE.md per §4e. Delete OZK trade rows from REGINALD/TRADE.md. | OZK/TRADE.md (new), REGINALD/TRADE.md (edit) | `OZK: split TRADE (OZK-specific trade entries move)` |
| 10 | Create OZK/inbox/ + OZK/outbox/ (with `.gitkeep`) | 2 empty dirs | `OZK: add inbox/outbox directories` |
| 11 | Update REGINALD's internal `OZK/` refs → `../OZK/` per §3b table (STATUS.md ×4, CALENDAR.md ×2, CLAUDE.md ×3, outbox files) | ~5 REGINALD files | `REGINALD: update OZK refs to peer path` |
| 12 | Update root CLAUDE.md agent list per §3d | `/home/willi/Research-workspace/CLAUDE.md` | `root: register OZK as top-level agent (spun out from REGINALD)` |
| 13 | **CHECKPOINT — boot test.** Per §10 validation. Will opens fresh Claude Code session with cwd=AGENTS/OZK/. Run 7-point checklist. STOP on any failure. | — | — |
| 14 | Refresh REGINALD/STATUS.md OZK section (D5: keep summary, add freshness rule). Reduce to 5-10 line snapshot + pointer to `../OZK/STATUS.md`. Note "refreshed from OZK/STATUS.md YYYY-MM-DD." | REGINALD/STATUS.md | `REGINALD: reduce OZK section to snapshot + pointer (D5 kept, trimmed)` |
| 15 | Move this plan to OZK archive: `git mv AGENTS/REGINALD/OZK_SPINOUT_PLAN.md AGENTS/OZK/archive/OZK_SPINOUT_PLAN.md` | file moved | `OZK: archive spinout plan (migration complete)` |
| 16 | First genuine OZK session — validate end-to-end. Update MEMORY with handoff. | OZK files via OZK session | `OZK: first agent-session close` |

**Estimated total: 2-3 hours across one or two sessions.**

---

## 7. What Will Does vs What I Do

**Will does:**
- Approve the plan (this doc)
- Approve each commit as I go (one-at-a-time rhythm per MEMORY [2026-04-02] preference)
- Run the Step 12 boot test (open new Claude Code session with cwd=AGENTS/OZK/, verify identity)
- Approve any content-extraction judgment calls during §4 (which rows move vs stay)

**I do (REGINALD agent, this session):**
- Execute the `git mv`
- Write all new files (CLAUDE.md, MEMORY.md, CALENDAR.md, LESSONS.md, POSITIONS.md)
- Edit REGINALD files to update cross-refs
- Stop at each checkpoint for Will's green light

**OZK agent does (first session after spinout):**
- Run Step 14 — first OZK boot, close session, prove the infrastructure works end-to-end

---

## 8. Resolved Decisions

| # | Decision | Call | Mechanics |
|---|----------|------|-----------|
| **D1** | POSITIONS split | **A — Clean split** | OZK/POSITIONS.md owns OZK rows. REGINALD/POSITIONS.md drops OZK rows. Step 8 executes. Note: source OZK rows from OZK/STATUS.md (current) not REGINALD/POSITIONS.md (Apr 2 stale). |
| **D2** | Shared MEMORY | **A — OZK reads only own** | Cross-cutting Will feedback is duplicated into OZK/MEMORY.md. OZK does NOT read `../REGINALD/MEMORY.md` at boot. OZK/CLAUDE.md boot sequence is local-only. List of duplicated rows in §4a. |
| **D3** | LESSONS | **Reviewed per entry** | 6 rules copied verbatim, 1 (NDFI) rewritten for OZK, 1 skipped. Full spec + OZK NDFI rewrite content in §4c. |
| **D4** | WAL followup | **Deferred** | WAL is a parallel sub-scope under REGINALD. After OZK stabilizes (~1-2 weeks), repeat this plan for WAL. Not part of current migration. |
| **D5** | REGINALD/STATUS.md OZK section | **Keep, trim, add freshness rule** | Do NOT drop. Reduce to 5-10 line snapshot + pointer to `../OZK/STATUS.md`. Add a dated "Refreshed from OZK/STATUS.md YYYY-MM-DD" note. REGINALD refreshes this summary at boot or session close by reading OZK/STATUS.md — not by maintaining separate numbers. Step 14 executes. |
| **#5** | Where does SPINOUT_PLAN.md end up? | **`AGENTS/OZK/archive/`** | OZK owns its own spinout history. Step 15 executes. |
| **#6** | OZK TRADE.md | **Yes, split** | OZK/TRADE.md gets OZK trade entries; REGINALD/TRADE.md keeps the rest. Step 9 executes. Spec in §4e. |
| **#7** | Timing | **Fresh session executes** | This session prepares the plan, then context clears. Fresh REGINALD session starts from this plan at Step 1. |

---

## 9. Rollback Plan

If Step 12 boot test fails (OZK session can't find its files, cross-refs broken, HERMES misroutes):

- **Soft rollback (undo Steps 10, 11, 13):** OZK lives at `AGENTS/OZK/` with infrastructure intact, REGINALD's refs still point at old `OZK/` path. Broken-but-contained; can fix forward.
- **Hard rollback (`git mv AGENTS/OZK AGENTS/REGINALD/OZK` + revert all commits):** Full undo. Expensive but clean.

**Unlikely to need rollback** because the move is pure rename + additive files. Biggest real risk is a missed cross-ref causing a 404 in some doc link — easy to fix forward once spotted.

---

## 10. Validation (Step 13 boot test)

Will opens new Claude Code session with cwd = `AGENTS/OZK/`. First prompts:

1. **Identity:** "Who are you?" → "I am OZK."
2. **File ownership:** "What's at the root of your directory?" → OZK lists OZK/ files correctly. Includes CLAUDE.md, MEMORY.md, CALENDAR.md, LESSONS.md, POSITIONS.md, TRADE.md, STATUS.md.
3. **CLAUDE.md chain:** "What project instructions did you load?" → should show root CLAUDE.md + OZK/CLAUDE.md only. If REGINALD's CLAUDE.md appears, something's wrong with the move.
4. **Boot sequence:** "Run your boot protocol." → reads STATUS, LESSONS, CALENDAR, MEMORY, market.py (OZK price), inbox. Confirms all reads succeed, no broken links.
5. **Cross-ref test:** OZK reads `../REGINALD/STATUS.md` — works (peer agent reference).
6. **Outbox write:** OZK drafts a test signal to REGINALD. File appears at `AGENTS/OZK/outbox/`.
7. **Git scope:** OZK runs `git status` after a change, stages only `AGENTS/OZK/`.

All 7 pass = spinout successful. Proceed to Steps 14-16 (REGINALD STATUS summary, archive plan, first OZK handoff).

---

## 11. Estimated Effort

- Steps 1-3 (move + ref fix + checkpoint): 15 min
- Steps 4-10 (new files: CLAUDE/MEMORY/CALENDAR/LESSONS/POSITIONS/TRADE/inbox-outbox): 60-75 min
- Steps 11-12 (REGINALD refs + root CLAUDE.md): 20 min
- Step 13 (validation): 10 min (Will-driven)
- Steps 14-16 (REGINALD STATUS summary + archive + first OZK session close): 30 min

**Total: ~2-2.5 hours across one or two sessions.**

---

**End of plan. All decisions resolved. Ready to execute in fresh session.**

**Fresh session entry point:** read §0 Quickstart, then work Step 1 onward. Stop at Steps 3 and 13 checkpoints.
