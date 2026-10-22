# OZK self-sweep — 2026-10-22 (REPORT-ONLY; nothing fixed)

**Asked by:** Will, direct session, 11:21 ET (`date`). **Scope:** `AGENTS/OZK/` only. **Builds on:** `reports/2026-10-21_self-sweep.md` (36 items). Part A re-checks those at the artifact; Part B lists new findings.
**Instruments run:** `scripts/boot.py` · `corrections_boot_check.py OZK` (rc 0) · `read_cap_check.py --agent OZK` (rc 0, STATUS 69% of budget) · `PROME/tools/inbox_census.py OZK` (0 packets) · `orphan_check.sh OZK` (nothing of ours) · file-by-last-commit listing · targeted greps of STATUS/TODO/CALENDAR/PREDICTIONS/charter · `FORGE/STATUS.md` · `PROME/WILL_QUEUE.md` · `PROME/DOCKET.tsv` · `gh repo view`.
**Git:** origin and local in sync (0 ahead / 0 behind at 11:21 ET); no pull needed. Dirty tree = DAEDALUS `GATE_LOG.tsv` + WALTER caches, not ours.
**Tokens:** VERIFIED = checked at the artifact this session · INFERRED = reasoned, not checked. **Severity:** 🔴 position- or gate-facing · 🟠 decision-facing · 🟡 hygiene.

## Part B — NEW findings (not in the 10/21 report)

| # | Item | file:line | Class | Sev | Fix · effort | Basis |
|---|---|---|---|---|---|---|
| N1 | **Position record stale against FORGE and the WQ-428 ruling.** STATUS shows the Nov-20 $40P ×4 at the 10/7 capture ($0.65 / $260) and never mentions that Will **approved SELL ×4 on 10/14** (WQ-428; window 10/15 – 10/20 15:30 ET). FORGE (ANVIL reconcile 10/22 11:01 ET): **4 still held, mark $0.05, value $20, −$302.65 / −93.8% on $322.65 basis; no sell order visible** (FORGE D-82, "approved sells not evidenced"). Whether it was ordered and not filled is UNKNOWN | `STATUS.md` §Positions, Bottom Line · `POSITIONS.md` header (10/8) | STALE | 🔴 | Re-state the position from FORGE 10/22 + the WQ-428 ruling and its unexecuted state; evidence only, TERRY owns the card and Will the order · 10 min | VERIFIED (FORGE:94,133; WILL_QUEUE:119) |
| N2 | **STATUS Problem Credits is still the Q2 (6/30) roster**, and charter + `SEVEN_CREDIT_DEEP_DIVE.md` banner point to `Q2_2026_10Q_READ.md` §2 as "current". Q3 moves (Boston 10 Prospect → OREO $132.0M after $37.3M c/o; The Jack → pass; Wauwatosa paid off; new Boston land $105.9M SM → substandard; C&C $1,282M → $995M) live only in the Stage-1 thread | `STATUS.md` §Problem Credits · `CLAUDE.md:18` · `SEVEN_CREDIT_DEEP_DIVE.md:3` | STALE | 🟠 | Write a Q3 roster table from the Q3 Management Comments now (FLNG 12022), finish SM detail at the 10-Q · 30 min | VERIFIED |
| N3 | **STATUS headline print table is still "Q2 2026 Snapshot"**; no Q3 snapshot table (the Signal Dashboard is Q3, so the two sections disagree in vintage) | `STATUS.md` §Q2 Snapshot | STALE | 🟡 | Rotate Q2 snapshot + Q2 Call Report tables to `archive/`, add a Q3 snapshot · 20 min (also frees read-cap room) | VERIFIED |
| N4 | **Stale Signal Dashboard cells:** insider buying "zero 7/6→9/27" (10/22 EFR pull extends it: nothing filed after 8/14) · KRE cross-feed $68.89 at 10/7 · RaDD leasing "none found through 9/27" · price $48.87 vs live $48.98 at boot | `STATUS.md` Signal Dashboard | STALE | 🟡 | Refresh at closeout · 5 min | VERIFIED |
| N5 | **STATUS Open Items overtaken:** #2 still names "next resolver L520" (L520 done → now the ~11/5 10-Q); #4 Bluerock refresh is DONE but still listed; #6 NEA 10/20 ARD passed, outcome unknown; #1 Horton 10/14 checkpoint passed | `STATUS.md` §Open Items | STALE | 🟡 | Rewrite to live items only · 10 min | VERIFIED |
| N6 | **Headers not bumped on 10/22 content edits:** TODO says "Last updated 2026-10-12 … Q3 results not graded" · SCENARIOS 07-06 · WEAKNESSES 09-27 · LIFE_SCI/STATUS 07-06 · THESIS "Last factual refresh 2026-10-12" · INDEX 10/12 with a patched parenthetical. A stale header over a fresh body misleads a cold reader | headers of each | STALE | 🟡 | Bump each to 10/22 with a one-line reason · 10 min | VERIFIED |
| N7 | **`research/README.md` (master research index) last touched 9/27** — none of the ~20 October threads are indexed | `research/README.md` | INCOMPLETE | 🟡 | Add the October threads · 15 min | VERIFIED |
| N8 | **MEMORY says "the repo is public"; `gh repo view` reports PRIVATE today.** Will's 10/21 ruling (option A: no full transcripts in tree) may rest on that fact | `MEMORY.md` Findings (Transcripts row) | CONFLICT | 🟡 | Ask Will which is true (was it flipped?); correct MEMORY, keep the ruling unless Will changes it · 2 min | VERIFIED (gh output) |
| N9 | **`sources/2026-10-12_*` = ~21 MB of fetched third-party material** (incl. a Cushman & Wakefield office report PDF, BPRE reports, IIPR agreement HTML); one **0-byte** file (`sources/2026-10-12_DURABILITY/MIDDLESEX_SOUTH_PORTAL.txt`); one **exact duplicate** (`sources/2026-10-12_GAP_PASS/AIMCO_SUBMISSIONS.html` ≡ `.txt`). `raw/` is 64 MB | `sources/2026-10-12_*` · `raw/` | HYGIENE | 🟡 | Trash the empty file and the duplicate; decide (Will) whether copyrighted third-party PDFs belong in tree, same logic as the transcript ruling · 10 min | VERIFIED |
| N10 | **Retirement candidates (>60 days):** April-24 pre-Q1 research (`research/C1–C3`, `D1–D6`, `NDFI_SHADOW_CRE_ANALYSIS.md`, `threads/CIB_MARGIN_COMPRESSION.md`, `threads/RESG_MIX_DETERIORATION.md`) and Q4-2025 `sources/` extracts. Eligible only if no live doc actually travels them — not checked per file. `SWEEP_2026-08-28.md` at root turns 60 days on 10/27 | `research/`, `sources/` | HYGIENE | 🟡 | Per-file reference check, then `git mv` to `archive/` · 30 min | VERIFIED (dates) / INFERRED (eligibility) |
| N11 | **PREDICTIONS OZK-09 notes carry no Q3 entry** (Stage-1 "no reserve named", Stage-2 "pass credit", resolver moved to the 10-Q). Extends 10/21 #21 | `workbook/PREDICTIONS.tsv` OZK-09 row | INCOMPLETE | 🟡 | Append a dated Q3 note, no status change · 5 min | VERIFIED |

## Part A — the 10/21 report's 36 items, re-checked

**Closed since 10/21 (13):** #1 Stage-2 call read done (`research/threads/2026-10-22_Q3_CALL_STAGE2_READ.md`) · #3 re-grade proposed as P-OZK-7, registered **WQ-483** (now Will's) · #4 PROME routed the Q3 grade to TERRY (`AGENTS/TERRY/inbox/2026-10-21_from-PROME_OZK-Q3-stage1-grade.md`) · #5 boot.py watches now Q3 · #6 REGINALD `CALENDAR.md:63` now 6.14% · #7 own CALENDAR now 6.14% · #9 Quartr superseded (needs a Pro subscription; TradingKey used) · #10 EFR pulled 10/22, nothing after 8/14 · #13 DOCKET rows now exist (re-grade 10/31, 10-Q 11/5) · #17 CALENDAR pruned to a RESOLVED section · #18 STATUS 69% of budget · #19 short interest at 9/30 settlement · #22 KB-260–263 added (263 rows, INDEX/KB_INDEX agree).

**Partly closed (3):** #15 TODO body updated, header still 10/12 (→ N6) · #16 STATUS catalyst table pruned, Open Items still stale (→ N5) · #23 POSITIONS fixed; **`TRADE.md:7` still points to `THREAD3_ROLL_MATH.md`** (now `archive/`).

**Still open (19):**

| # | Item | Sev | Due |
|---|---|---|---|
| 2 | OZK-09 recognition leg — RaDD reserve amount or bound | 🔴 | ~11/5 10-Q; window ends at the Q4 print ~Jan 16–20 2027 |
| 8 | **FFIEC CDR login token expires 11/5** — blocks the Q3 Call Report pull (the debt-on-debt pillar's only instrument) | 🟠 **Will action** | by Thu 11/5 |
| 11 | OZK-02 Q3 input (problem-category commitment share) not collected | 🟠 | before Q4 print |
| 12 | OZK-04 roster basis ambiguous (Q3 diagnostic 2.31% on substandard + OREO vs the Q1 $719M roster) | 🟠 | before Q4 print |
| 14 | Sub-notes call-notice window opens **Mon 11/2** (flng_watch + one press search) | 🟠 | 11/2 → 12/22 |
| 26 | Thesis legs with no live feed: IQHQ/Bluerock lane query (PROME owed since 10/1), RaDD leasing, debt-on-debt (rides #8) | 🟠 | — |
| 20 | `CALL_REPORT_SERIES.tsv` 76 days behind (expected until the Q3 pull) | 🟡 | ~Nov 1–10 |
| 21 | PREDICTIONS header "Last real data refresh 2026-07-23" | 🟡 | with N11 |
| 24 | Two bare REGINALD paths in the 9/27 threads | 🟡 | — |
| 25 | Context-only bare names across CALENDAR/TODO/IQHQ_PLAYBOOK/INDEX/STATUS | 🟡 | — |
| 27 | Subdomain STATUS files (GEOGRAPHY 7/6, INSIDERS 7/6, PRIVATE_CREDIT 8/28 headers) pre-Q2; the debt-on-debt pillar's evidence home is PRIVATE_CREDIT | 🟡 | after the 10-Q |
| 28 | Severity comp refresh (KB-OZK-177) — Boston now gives a fresh point (80% of Sept as-is) | 🟡 | — |
| 29 | Access gaps: SD County recorder, FSX docket, Middlesex registry (browser-only) | 🟡 | only if needed |
| 30 | G3: two boot.py items owed to DAEDALUS, delivery unverified | 🟡 | — |
| 31 | G4: `PREDICTIONS_ARCHIVE` seed | 🟡 | — |
| 32 | T1: boot.py INBOX blind to `inbox/WALTER/` (`scripts/boot.py:289` globs `inbox/*.md` only) | 🟡 | — |
| 33 | 11 outbox packets (7/20 → 10/12) never moved to `outbox/delivered/` | 🟡 | — |
| 36 | Charter still calls the sub-notes reprice a future 2026 catalyst (`CLAUDE.md:19`) and carries Q2 roster figures (`:18`) | 🟡 | — |
| 23r | `TRADE.md:7` dead pointer (remainder of #23) | 🟡 | — |

**Clean:** corrections register (0 named rows unreceipted) · read-cap (all four boot reads under budget) · no prediction past its resolve date · inbox empty (both lanes) · no orphaned OZK packets · REGINALD channel fully ACKed.

## What is waiting on Will

1. **WQ-483 / P-OZK-7** — conviction 🔴🔴 HIGH → 🟡 LOW (desk recommendation). DOCKET check-by 10/31.
2. **FFIEC CDR login renewal by Thu 11/5** (#8).
3. **N1 is a fact for Will and TERRY, not a recommendation from this desk:** the sell he approved 10/14 is not evidenced in the broker view at 10/22 11:01 ET.
4. **N8/N9:** is the repo public or private, and should third-party PDFs stay in tree?

---

## Part C — outcomes (Will 11:25 ET: "go ahead and fix the housekeeping items"; worked 11:25–11:4x ET)

**Also landed mid-pass:** WQ-483 ruled (Will 11:24 ET via PROME) → **P-OZK-7 encoded as THESIS v1.7, conviction 🟡 LOW**, commit **67a1634a1**; ruling packet filed to `inbox/processed/`.

| # | Outcome |
|---|---|
| N1 | **FIXED** — STATUS §Positions, Bottom Line, INDEX and `POSITIONS.md` header restated from FORGE 10/22 + WQ-428 (sell approved, not evidenced, order status UNKNOWN). Evidence only; no management |
| N2/N3 | **FIXED** — STATUS carries a Q3 snapshot + Q3 roster from MC Fig 22–23 pp.23–25 (FLNG 12022); Q2 tables moved verbatim → `archive/STATUS_HISTORY_2026-10-22.md`; charter + `SEVEN_CREDIT_DEEP_DIVE.md` now point to STATUS for the current roster. SM still un-itemized → 10-Q |
| N4 | **FIXED** — price $48.96 (11:26 ET), insider row →10/22, KRE $71.79 (11:26 ET), RaDD leasing row notes Q3 silence |
| N5 | **FIXED** — Open Items rewritten to live items; Bluerock refresh removed as done |
| N6 | **FIXED** — headers bumped with what actually changed (TODO, SCENARIOS, WEAKNESSES, LIFE_SCI/STATUS, THESIS, INDEX). WEAKNESSES header now says Q3 + v1.7 are **not yet folded in** (owed, MEMORY NEXT 5) |
| N7 | **FIXED** — 13 October rows added to `research/README.md` |
| N8 | **PARTLY** — MEMORY now records the gh PRIVATE reading beside the ruling; the ruling stands. **Will's answer still needed** |
| N9 | **NO CHANGE — reasoned:** the 0-byte file and the .txt duplicate are both named in their pass's `MANIFEST.json` (fetch provenance). Trashing them breaks the manifest. Copyright question → Will |
| N10 | **PARTLY** — repo-wide reference check run on 20 April-era files: most are still travelled by live OZK docs or by other desks (REGINALD FHLB copy manifest, CREED `CASE_EVENTS.tsv`, REGINALD RP-REG-7, WAL audit), so they stay. Retired: `research/D5_DIVIDEND_SUSTAINABILITY.md` and `sources/FFIEC_CALL_REPORT_Q4_2025_RAW.csv` → `archive/` (pointers updated in KB_INDEX, research README, sources README). `SWEEP_2026-08-28.md` not yet 60 days |
| N11 + #21 | **FIXED** — OZK-09 notes carry a dated Q3 entry; "Last reviewed" → 10/22. "Last real data refresh" left at 7/23 (no confidence or weight moved) |
| #3 | **DONE** — v1.7 (above) |
| #23r | **FIXED** — `TRADE.md:7` → `archive/THREAD3_ROLL_MATH.md` |
| #24 | **FIXED** — both REGINALD paths repo-root-qualified (targets verified to exist) |
| #25 | **FIXED** — bare names qualified in TODO, CALENDAR (×3), IQHQ_PLAYBOOK, INDEX. INDEX archive-table rows already carried `archive/` |
| #30 G3 | **CLOSED — already delivered:** DAEDALUS `runs/2026-08-28_WIRING_SWEEP/RUN_RECORD.md:58` records both items |
| #32 T1 | **FIXED** — `scripts/boot.py` INBOX scans sender lanes; tested with a temporary `inbox/WALTER/` file (listed), then removed (empty) |
| #33 | **FIXED** — 11 packets → `outbox/delivered/` with `outbox/delivered/2026-10-22_DELIVERY_LOG.md`; 10 have receipt evidence in `PROME/`, the 7/20 one does **not** (moved as stale, logged) |
| #36 | **FIXED** — charter core-thesis, roster and catalyst lines rewritten as pointers carrying no version or figures (they had gone stale three times) |
| Not done (not housekeeping) | #11 / #12 OZK-02/04 inputs · #27 subdomain STATUS refresh · #28 severity comps · #31 G4 archive seed · #26 lanes · #29 access gaps · #20 (waits for the Q3 Call Report) · #2 / #8 / #14 dated |

**Checks after the pass:** read-cap rc 0 (STATUS 58% of budget) · claim-check weekday clean on CALENDAR + STATUS.
