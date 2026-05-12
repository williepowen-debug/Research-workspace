# REGINALD SCRATCH

*Loose notes, intra-day workspace, observations that don't fit anywhere else yet.*

**Purpose:** Capture stuff during the work — half-thoughts, things noticed in passing, quotes worth remembering, format gotchas, draft language.

**What this is NOT:**
- Not a task list (use MEMORY NEXT SESSION)
- Not curated memory (use MEMORY)
- Not a thesis (use THESIS / sub-bank THESIS files)
- Not a research backlog (use ROADMAP — Investigations Backlog section)
- Not a session-bridge (MEMORY Session Notes does that)

**Maintenance discipline:**
- Date each entry / section
- Promote to KB / ROADMAP / STATUS / MEMORY when it grows up; delete when it's done
- Prune aggressively — if a note is older than ~2 weeks and hasn't earned a promotion, delete it

---

## 2026-05-01 PM — Wave 1 chunks 3-6 + Q1 CR sweep [PRUNED 2026-05-11; durable bits already in MEMORY/LESSONS]

**WAL Q1 transcript line-numbers (kept — useful for future quoting):**
- L22: opening — "decisive actions taken on two previously disclosed fraud-related credits"
- L28: LAM — "fully charged off the remaining $126.4 million balance of the loan to a fund of Leucadia Asset Management" + "we will not provide further commentary"
- L34: Cantor — "$29.6 million specific reserve... validated by current as-is appraisal values" + "$26 million" charged + recovery sources (UHNW springing guarantees, mortgage fraud policy)
- L106: leading-vs-lagging — "criticized assets were largely stable... special mention loans increased $78 million quarter-over-quarter, the change was not thematic"
- L154: revised guide — "core net charge-off guidance of 25-35 basis points... at or slightly above the midpoint of this range"

**Open backlog item:**
- "Juris banking" line — mentioned multiple times in WAL transcript as the "real surprise driver." Need KB row capturing what Juris banking actually IS. Research add: what business / counterparty / how does it monetize? (Investor Day May 12 may surface.)

---

## 2026-05-08 PM — May 8 Friday session [PRUNED 2026-05-11; durable bits in MEMORY findings]

Detail in MEMORY.md LAST SESSION (May 8 PM) one-line recap + commit history `d5d08d56` / `486aea0b` / `325dc8de` / `0d876199`.

---

---

## 2026-05-11 PM — Investor Day prep + tape break to $76.95 + Q&A curation overreach caught

**Single-deliverable session: `WAL/INVESTOR_DAY_PREP_2026-05-12.md`.**

**What worked:**
- Reading V2.1 THESIS + V21_RESPONSE_TO_RED_CHG_025 + SIG-W-20260511-023 in parallel before drafting → grounded in current frame, didn't re-derive
- Table-driven structure (5 listening buckets × 4 attributes; decision tree × 8 outcome states; position implications matrix) — kept the file scannable on the day
- Pre-registered decision tree per RED §12.4 — when the event lands tomorrow, day-of read is mechanical, not reactive
- Tape-on-the-day ≠ signal rule explicit at the top of logistics — guards against intraday whipsaw reactions

**What got caught:**
- Layered "Q&A pool is curated by IR" interpretation on top of "in-person attendance by invitation only" — that was a stretch the announcement text didn't actually support
- Will pushed back; honest correction made (invitation-only is capacity-management, not question-filtering; hostile analysts get invited by default)
- Per MEMORY [Evaluate Evidence Standalone] feedback — fired AGAIN. Pattern: I have clean operational text and want to extract an implication; the implication often outruns the evidence. **30-second self-check: what does the text actually say?** Before reaching for what it implies.

**WALTER SIG-W-20260511-023 (WAL Q1 fraud-vs-structural decomposition) integration:**
- Adj NCO 0.39% / classified -9bp QoQ / NPL flat → CONFIRMS V2.1 leading-vs-lagging divergence from lagging-cleaning side
- Doesn't change thesis weight; sharpens Bucket E listening post (NCO guide-raise vs guide-hold tension)
- Mgmt language "past peak stress in office CRE; NPL decline expected H2" sets up the U1 modal trigger

**13-signal BOARD inflow on 5/11 — observation, not action:**
- vs ~1-2/day baseline = 6-10x volume jump
- Could be one-off (Q1 reporting wave + WALTER weekend cohort scan) or new baseline
- Calibration cycle 1 (May 25) will tell whether sustained
- Notable: ~6 of 13 are MI3/NDFI-adjacent — Call Report rules + bank-level NDFI concentration data dropping ahead of FFIEC PDD bulk May 14-16

**Things I noticed but didn't dig into:**
- SIG-W-20260511-030 (cohort counter-evidence: 5 names improving) directly challenges 12/12 fade pattern in REGINALD STATUS — if confirmed it's a STATUS-level revision, not just a row update. Deferred.
- SIG-W-20260511-029 (NDFI 5-cat schema + May 15 CDR Q1 bulk release) is the SCHEMA for how MI3-print landing will look — should read before MI3 print so reading framework is set up.
- SIG-W-20260511-014 (NDFI $1T threshold new Call Report rules MI3-adjacent) may change MI3 disclosure mechanics going forward. Strategic; not urgent.

**One-liners cached:**

```bash
# Investor Day live webcast (Tue May 12 8:30 AM ET):
# https://investors.westernalliancebancorporation.com → Events & Presentations

# Q&A transcript pattern reference for V2.1 mgmt-discount calibration:
grep -E "Vecchione|Idnani|Bruckner|fraud-related|past peak|behind us|long duration" \
  WAL/sources/q1_2026/WAL\ Earnings\ Call.md
```

**Convention question for next session:**
- After Investor Day, write findings to `WAL/INVESTOR_DAY_FINDINGS_2026-05-12.md` (paralleling Q1_2026_ANALYSIS.md format)? Or fold into a v2.1.x THESIS revision directly? Default: separate findings file first; rollup to THESIS only if V2.1 → V2.2 trigger fires.

---

## 2026-05-10/11 PM — Sunday-into-Monday: WALTER LIAISON converged + WAL V2.0 → V2.1 ship

**Architectural ships (high density session):**

```
LIAISON Turns 1-5 close-converged in <13 hr UTC (RED-pace match):
  Turn 1 (REGINALD)  23:11 UTC  empirical-honest "ZERO action" claim
  Turn 2 (WALTER)    23:30 UTC  empirical reframe: 16 ACTION not zero
  Turn 3 (REGINALD)  01:53 UTC  3 files instantiated
  Turn 4 (WALTER)    04:35 UTC  4 deliverables + REG-T-01 sustain=1 LOCK
  Turn 5 (REGINALD)  11:42 UTC  joint-proposal §1+§3
```

**Files mental-map for next-boot context:**

```
LIAISON ships:
  AGENTS/REGINALD/handoff_WALTER/{README.md, LIAISON.md}
  AGENTS/REGINALD/registry/THRESHOLDS.tsv (8 rows REG-T-01..08)
  AGENTS/REGINALD/board/BOARD_LOG.tsv (11-col, 32-row backfill stub)
  AGENTS/REGINALD/CLAUDE.md (Boot Step 9b added)
  AGENTS/REGINALD/design/JOINT_PROPOSAL_2026-05-11_reginald_sections.md

WAL V2.1 ships:
  AGENTS/REGINALD/WAL/THESIS.md (v2.1)
  AGENTS/REGINALD/WAL/SCENARIOS.md (v2.1, Bear-fast/slow split, Jun-conditional EV)
  AGENTS/REGINALD/WAL/CHANGELOG.md (v2.1 entry)
  AGENTS/REGINALD/WAL/V21_RESPONSE_TO_RED_CHG_025.md (formal response)
  AGENTS/REGINALD/WAL/STATUS.md (header v2.1)
  AGENTS/REGINALD/LESSONS.md (2 new methodology entries)
```

**Patterns / one-liners cached (durable bits promoted to MEMORY findings + LESSONS):**

```bash
# Quick BOARD-routing-to-REGINALD audit (mirror what WALTER ran in Turn 2):
grep -lE 'REGINALD' BOARD/SIG-W-*.md | wc -l   # total touched
grep -lE '^to:.*REGINALD' BOARD/SIG-W-*.md | wc -l   # ACTION recipients
grep -lE '^info:.*REGINALD' BOARD/SIG-W-*.md | wc -l   # info recipients

# Quick falsifier-status check before any thesis-level reframing:
grep -E "Falsifier|falsifier|invalidate|Pre-registered" WAL/WEAKNESSES.md
# THEN check whether each has fired post-print before publishing reframe
```

**Two external-grep-catches in 24 hours:**
- WALTER Turn 2: caught "zero action" framing without grep — corrected to 16 of 51
- RED CHG-RED-025: caught V1-demotion-before-tested + Jun-conditional EV math
- Pattern lesson: 30-second self-verification pass catches both before publishing
- Promoted to LESSONS.md as 2 [Methodology] entries

**Things I noticed but didn't dig into:**
- MI3 baseline data (15.5 → 24.2 trajectory) is from prior screen per LESSONS.md "Verify Agent Data Against Primary Filings" — V2.1 restores V1 weight pending MI3 print but I haven't independently re-verified the historical baseline. If 15.5 baseline was wrong, V1's case is weaker than both V2.0 and V2.1 imply. Honest hole in V2.1 not flagged in response memo.
- WAL Investor Day pre-write read-across needs to be done tonight (Mon May 11 evening) — flagged as #1 NEXT SESSION priority but didn't do this session.
- BOARD_LOG.tsv 16 missed-action signal full disposition pass deferred — first real maintenance-discipline test.
- WALTER's bank_transmission enum 8-val (cre/hidden_cre/ndfi/private_credit/mfs_fraud/cmbs_maturity/fed_layoffs/stagflation_trap) lands when FORMAT_SPEC v0.9 batched ship happens — at that point BOARD_LOG.tsv `Channels_Touched` column needs uppercase→snake_case migration (currently uses `CRE,HC,NDFI,PC,MFS,CMBS,FED-LAYOFFS,STAGFLATION`).

**Convention question for next session:**
- Boot Step 9b BOARD scan first execution test. If it works clean, great — that validates the LIAISON architectural ship. If it produces noise/friction, refine in next LIAISON cycle (calibration cycle 1 trigger May 25).

**One open externality I should track:**
- WALTER had uncommitted changes (MEMORY/REGISTRY/SESSION_LOG/STATUS) when I tried pull-then-push — push went through but pull blocked. Next session may need to wait on WALTER's commit before pulling. Check `git status` carefully at boot per pull protocol.

---

## TEMPLATE FOR FUTURE DAYS

```
## YYYY-MM-DD <morning/PM> — <one-line context>

**<Section header>:**
- bullet
- bullet

**Things I noticed but didn't dig into:**
- ...

**One-liners cached:**
```bash
# ...
```

**Convention question / open-thread for next session:**
- ...
```

---

*Companion: `ROADMAP.md` (persistent state across sessions) | `MEMORY.md` (curated cross-session memory) | `STATUS.md` (live dashboard)*
