# R1 — ARCHITECTURE / SPINE — REGINALD whole-profile refresh

Reader R1 of 4 · DAEDALUS · started 2026-10-30 16:41:18 EDT (from `date`) · HEAD 9f0975860
Read-only on tracked files. Only write: this report.

## Pre-read state
- `git status --porcelain -- AGENTS/REGINALD/` at 16:41:18 EDT: EMPTY (clean)
- `git log -5 -- AGENTS/REGINALD` : 33f7a2638 (WALTER 15:17) · 005184d69 (DAEDALUS 13:02) · 609860a7a (DAEDALUS 12:40) · 9ebedf3e2 (REGINALD 09:15 NEXUS brief) · 4222ea74d (REGINALD 09:14 L801 decided)

_(sections A–I follow; written incrementally)_

## Working notes (incremental; consolidated into A–I below)
- Charter read whole 1–166 (24,977 B; last commit d3488e641 2026-10-23 DAEDALUS WQ-508). Charter changes since READS ATTESTATION (2026-10-20): f8405c6f2, 137aedf69, f984ce53c (10/22), d3488e641 (10/23).
- STATUS read whole 1–139 (23,487 B; 4222ea74d 10/30 09:14).
- boot.py read whole 1–245; builtins (inbox / channels / predictions) executed in isolation from /tmp/claude-1000/reginald-r1 (no subprocess legs): inbox rc1 (2 general + 2 WALTER NEW), channels rc0 (WAL 0, OZK 0 above latest ACK), predictions rc0 (7 OPEN, all with Resolve_By). Porcelain before/after: empty/empty.
- read_cap_check.py --agent REGINALD (ROOT tool) → RC=1, `over_budget=1 rotation_due=7`; output saved /tmp/claude-1000/reginald-r1/readcap.txt.
- READS: 55 REGINALD rows (lines 453–508 + 559 is WAL's own); ATTESTATION 2026-10-20; NO REGINALD row for `AGENTS/WAL/REGINALD_CHANNEL.md` or `AGENTS/OZK/REGINALD_CHANNEL.md` (only WAL's own row, line 559).

---

## A. File anatomy (bytes measured 16:46 EDT; budget 32,550 B; 75% = 24,412 B; 70% stop = 22,785 B)

| File | Bytes | % budget | Role | Vintage / stamp in content | Boot read? (charter / READS) | State |
|---|---:|---:|---|---|---|---|
| CLAUDE.md | 24,977 | 76.7% | charter | last commit d3488e641 10/23 (DAEDALUS WQ-508) | whole (READS 462) | current text; **ROTATE-TIER** (grew 22,783 → 24,977 B since 10/20; +1,637 B came from the 10/22 D:L793 fixes, f8405c6f2) |
| STATUS.md | 23,487 | 72.2% | thesis-canonical state | Last Updated 2026-10-30T09:14 (4222ea74d) | whole, Boot-1 | current; regrowing (+1,342 B since 10/28 rotation to 22,145 B) |
| LESSONS.md | 13,201 | 40.6% | verified mistakes | entries to 10/23; footer "Last reviewed 2026-08-20" (:81) | whole, Boot-2 | current body, stale footer |
| CALENDAR.md | 23,495 | 72.2% | dates/checks | Last Updated 2026-10-28 22:39 (:3) | whole, Boot-3 | current header; several stale cells (see G) |
| MEMORY.md | 17,576 | 54.0% | handoff | LAST SESSION 2026-10-30 09:05 (:27) | whole, Boot-4 | current; 91 lines vs 100-line style cap; +2,685 B since 10/28 |
| ROADMAP.md | 23,400 | 71.9% | open threads | Updated 2026-10-30T09:14 (:2) | whole, Boot-5 | current header; some rows stale (see G) |
| BANK_RESEARCH_STANDARD.md | 6,368 | 19.6% | research standard | Established 2026-10-13 | whole, conditional 5a | current |
| SCRATCH.md | 5,257 | 16.2% | scratch | last commit 10/14; live section dated 10/07 | optional 6 | stale vs own ~2-week prune rule (10/07 section = 23 days) |
| NEXUS_BRIEF.md | 21,619 | 66.4% | derived brief | As of 10/30 09:15, pin `4222ea74d` (:5) | whole, closeout | current; **pin = STATUS HEAD (verified)** |
| DECK_EVIDENCE.md | 24,091 | 74.0% | March deck source | FROZEN 2026-07-09 banner (:1), corrections 8/10, 10/10 | whole, closeout-or-fire (READS 502) | frozen; 321 B under 75% |
| BANK_EXPOSURE_MATRIX.md | 24,946 | 76.6% | matrix method + scores | v2.0 rebuilt 2026-08-20; wording fix 10/23; refresh due 11/07 (§8) | scoped (READS 490) | current-to-vintage; not cap-bearing (scoped) |
| STATUS_DASHBOARD.md | 33,571 | **103.1%** | cold channel detail | split 9/02; rows mixed Aug–Oct; re-check date "2026-10-02" passed | cold, NOT a boot read | **over budget** (grew 32,546 → 33,571 B on 10/28–10/29 appends); not declared, not cap-bearing |
| STATUS_MATRIX.md | 8,953 | 27.5% | cold matrix narratives | split 9/24, last commit 10/07 | cold | current-to-vintage |
| STATUS_BEAR_LEDGER.md | 4,136 | 12.7% | cold bear ledger | split 9/14; body 8/27–9/14; re-check "2026-10-14" passed | cold | stale body (HY 273, Q2 QBP), honest "not live state" banner |
| MEMORY_REFERENCE.md | 12,924 | 39.7% | cold how-to | split 9/14; last commit 9/24 | cold | current-to-purpose |
| ROADMAP_BACKLOG.md | 7,829 | 24.1% | cold backlog | split 9/02; last commit 10/10; re-check "2026-10-02" passed | cold | fine |
| SUB_AGENTS.md | 2,680 | 8.2% | peer navigation | Updated October 20 | not boot | current |
| thesis/CHANGELOG.md | 20,270 | 62.3% | dated thesis evolution | **newest entry 2026-10-12** (:3) | whole, closeout-or-fire | live but no entry for 10/22 exit-rule retirement or 10/30 L801 (see H) |
| thesis/THESIS.md | 3,166 | 9.7% | retired stub | RETIRED 8/13 | no | frozen stub (correct) |
| thesis/TIMELINE.md | 3,362 | 10.3% | retired stub | RETIRED 8/20 | no | frozen stub (correct) |
| kernel/REG-01, REG-06 companions | 8,297 / 9,857 | — | Gate C structured companions | 2026-08-27 | no | frozen prep; ROADMAP:30 "nothing owed" |
| kernel/staged_increment2/ (4 CMD json + README) | — | — | staged, NOT live commands | 2026-08-27 | no | byte-frozen; `outbox/kernel/submissions/` empty (correct posture) |
| scripts/boot.py | 10,687 | — | boot orchestrator | 137aedf69 2026-10-22 | 7b (conditional) | current |

Whole-boot load (mandatory whole reads only, before task/peer reads): root CLAUDE 24,634 + AGENTS 5,756 + USER 8,458 + COMPLETION_SPEC 18,614 + charter 24,977 + _NETWORK 13,305 + STATUS 23,487 + LESSONS 13,201 + CALENDAR 23,495 + MEMORY 17,576 + ROADMAP 23,400 = **196,903 B** (Verified sum of measured sizes; informational, no fleet rule on the sum).

## B. Boot path

**Charter order (CLAUDE.md:9, :15, :23-49):** explicit read root CLAUDE/AGENTS/USER + COMPLETION_SPEC + Runtime mechanics + charter → 0 sync (pull safety) → 1 STATUS → 2 LESSONS → 3 CALENDAR → 4 MEMORY → 5 ROADMAP → 5a BANK_RESEARCH_STANDARD (conditional) → 6 SCRATCH (optional) → 7 `scripts/market.py` (KRE<60 / WAL<78 / HY>320) + `vx_ladder_check.py` → 7a `ledger_staleness.py REGINALD` and `--trade` → 7b `boot.py` (conditional: print windows / deeper sweeps; skip for quick tape boots) → WALTER intake (inbox/WALTER/*.md not in BOARD_LOG, append row, `git mv` to processed) → 8 general inbox listing (awareness only unless tasked) → 9a WAL/OZK `REGINALD_CHANNEL.md` entries above latest ACK, ACK each with changed/no-change receipt (WQ-484) → 9b peer STATUS when relevant (BROCK/CORAL/OZK/WAL/FLG/GIBBS/CREED) → 9b BOARD diff → 9c corrections_boot_check → 9d explicit-path commits.

**boot.py (read whole 1–245) — what it actually checks:** subprocess legs market.py, thresholds.py, kre_float.py (`--no-state` under `--check-only`), earnings_countdown.py, insider.py + 8k_monitor.py (slow; skippable), vx_ladder_check.py, corrections_boot_check.py REGINALD, ledger_staleness.py REGINALD `--quiet` and `--trade --quiet`; built-in legs inbox lanes (general + WALTER, BOARD_LOG-aware), peer channels (WAL, OZK: entries above latest REGINALD ACK), prediction resolve-by (OPEN rows vs `registry/PREDICTION_RESOLVE_BY.tsv`). Exit: 0 clean / 1 ALERT / 2 FAIL or INCOMPLETE (boot.py:238-240). Frozen DARKPOOL/SHORT_VOL/SI legs removed (boot.py:45-46).

| Check | Result | Receipt |
|---|---|---|
| Does boot scan `inbox/WALTER/`? | **YES** — charter WALTER-intake block (CLAUDE.md:39), spawned-mode card (:15), and boot.py `check_inbox` (boot.py:97-102). 10/22 finding CLOSED. | builtin run 16:41: `📥 WALTER SIG-W-20261030-007 NEW`, `-010 NEW` |
| Does boot scan general inbox? | YES (step 8 listing; boot.py:94-96) | builtin: 2 DAEDALUS packets listed |
| Exit code honest? | YES (0/1/2; broken builtin = FAIL, boot.py:209-210) | code read |
| Builtins run (isolated, read-only) | inbox rc1 (4 open) · channels rc0 (WAL 0, OZK 0 unACKed) · predictions rc0 (7 OPEN: REG-01/03/06/27/28/29/30, all with Resolve_By 2027-01-05…2027-08-09) | /tmp/claude-1000/reginald-r1 run, porcelain empty before/after |
| Not run | subprocess legs (market.py fetches; kre_float writes state without `--check-only`; EDGAR legs network) | by rule |

Boot-path observations (Verified from text): (1) A deep boot runs vx_ladder, ledger_staleness ×2 and corrections twice (charter steps 7/7a/9c AND inside 7b) — redundancy, not defect. (2) `check_predictions` silently drops any row whose column count ≠ header (boot.py:139) — a malformed OPEN row would vanish rather than read INCOMPLETE (Inferred risk; current file parsed 7 OPEN). (3) Charter commands at :34, :47, :85 remain bare root-relative while the launch path is `cd AGENTS/REGINALD && claude` (10/22 #17a, still OPEN). (4) The 10/28 boot report's recorded read order (STATUS → MEMORY → ROADMAP → LESSONS → CALENDAR, `reports/2026-10-28_boot/REPORT.md:7`) differs from the charter's "this order matters" sequence (Verified; impact low).

## C. Current judgment

| Item | Finding | Receipt |
|---|---|---|
| Where it lives | STATUS head block "**Current judgment (10/30; substance unchanged from 10/22)**" | STATUS.md:7 |
| Mirrors | NEXUS_BRIEF Status line (:3) and CROSS-DOMAIN 10/30 block agree; pin `4222ea74d` = STATUS HEAD | NEXUS_BRIEF.md:3-5; `git log -1 -- STATUS.md` → 4222ea74d |
| Currency vs desk HEAD | Desk's own last commits 4222ea74d (09:14) + 9ebedf3e2 (09:15) 10/30; later commits on the path are DAEDALUS packets (609860a7a, 005184d69) and WALTER signals (33f7a2638) → judgment is current to the desk's own HEAD | `git log -5 -- AGENTS/REGINALD` |
| `## BOTTOM LINE` section | **Still undated, still points at the 10/20 catch-up report, still not the last section** (OPEN PROCESS ASKS follows at :132-139). Carries only pointers + standing caveat; the live judgment is at :7. 10/22 #14a OPEN. | STATUS.md:124-130 |
| Lapsed "next" pointers in a 10/30 write | Claims row "Next print Thu 10/29" and funding row "Next H.4.1 Thu 10/29" were already past when STATUS was written 10/30 09:14 (STATUS:11 discloses H.4.1 unread) | STATUS.md:110, :115 |

## D. Thesis and exit rail

| Item | Now | Receipt | V/I |
|---|---|---|---|
| Thesis version | No numeric version by rule: THESIS retired 8/13 (R1), TIMELINE 8/20 (R2); STATUS §THESIS canonical; v2.0 only from a narrowed STATUS | CLAUDE.md:64; thesis/THESIS.md:1-7; STATUS.md:15-20 | V |
| Live claim + refresh trigger | "Severity CONCENTRATED, not tier-wide" (3 elevated, 8 score ≤2 of 14); scores frozen **until the 11/07 re-score** — trigger dated, NOT expired (8 days out) | STATUS.md:18; BANK_EXPOSURE_MATRIX.md §8 ("stale after ~2026-11-10 = neglect") | V |
| Prior-profile "THESIS v1.4 trigger +17d expired" | CLOSED by retirement | thesis/THESIS.md:1 | V |
| EXIT RULES dated? | **YES** — "Kill rail re-derived: 2026-10-22"; cell states "refreshed 2026-10-28" | STATUS.md:87, :89 | V |
| 'CBRE' defined? | **YES and the leg RETIRED**: CBRE = CBRE Group share price (Feb 2026 "transaction canary"); retired 10/22 as anchor-drifted; Claims>300K kept as escalation, not exit | STATUS.md:93 | V |
| CRE anchor still cites REG-24/25? | **NO** — re-keyed to WAL-01/WAL-02 (old text quoted as "was"); read against WAL's 10/19 grades: NCO 30bp (>25bp) → NOT FIRED literally | STATUS.md:94 | V (WAL figures not re-verified at WAL's ledger by me) |
| CMBS-flows anchor | In force but **UNREAD at month-over-month grain** (CREED's Trepp instrument); level 12.16% [Sept, SECONDARY] | STATUS.md:95 | V |
| Recognition-lane anchor | New 3-leg AND: FL frame NO TRANSMISSION + L180 NOT BROADER (11/07) + REG-03 FALSE (FDIC Q4 QBP ~late Feb 2027). Because leg 3 cannot resolve before ~late Feb 2027, **this stand-down REVIEW cannot fire before then**; the "each already has its own base rate in its frame" claim was not checked here | STATUS.md:96 | V (text) / I (consequence; base-rate claim unverified) |
| WAL seam pointer-only (prior DNT #3) | CHANGED: EXIT RULES now carries two WAL figures (30bp, $272.75M) as anchor reads cited to `../WAL/workbook/PREDICTIONS.tsv`. Deliberate and sourced, but it is the one place the "restates ZERO WAL figures" rule no longer holds | STATUS.md:94 vs :30 | V |
| REG-T-07 live reading | **CLOSED**: 12.16% [Sept 2026 Trepp, SECONDARY], 2.84pp below 15; owner CREED, fallback named | STATUS.md:109 | V |
| thesis/CHANGELOG coverage | Newest entry 2026-10-12. No entry for 10/22 exit-leg retirement / anchor re-key, 10/22 channel-table rotation, or 10/30 L801 (coverage-decline leg dropped). Charter :63-64 require an entry on "framing/claim retirement" | thesis/CHANGELOG.md:3; `grep -n 'CBRE\|L801\|2026-10-2' thesis/CHANGELOG.md` → none | V (absence) / I (whether each is "thesis-level") |

## E. Read-cap and size

`python3 scripts/read_cap_check.py --agent REGINALD` (root tool, 16:4x EDT) → **RC=1**; `READ-CAP-RESULT v1 … reads=1893 over_budget=1 over_cap=0 manifest_defects=0 … rotation_due=7 … charter_mode=unspecified charter_bytes=24977`. `PROME/tools/reads_check.py --agent REGINALD` → **RC=1, "⛔ ATTESTATION STALE (dated 2026-10-20)… READS-CAP UNKNOWN … a partial perimeter, never a clean bill."** Porcelain on AGENTS/REGINALD empty before and after both runs (PROME/ had 6 modified + 1 untracked file before and after — not mine, unchanged).

| Surface | Bytes | % | Tier | Owner | Note |
|---|---:|---:|---|---|---|
| BOARD/SIG-W-20260619-008 (class member) | 39,509 | 121% | **over budget → rc1** | WALTER (file); PROME/DAEDALUS (class-row semantics) | Same as 10/22. The 10/22 reading-companion row (READS 489, `AGENTS/WALTER/reading/SIG-W-20260619-008.md` 21,889 B) did NOT clear rc: the `BOARD/SIG-W-*.md whole` class row (READS 488) still measures all 1,863 members. Declaration wider than practice ("selected, new since BOARD_LOG") |
| AGENTS/CREED/STATUS.md | 26,261 | 81% | rotate | CREED | inside REGINALD perimeter as conditional peer read |
| **AGENTS/REGINALD/CLAUDE.md** | 24,977 | 77% | **rotate (REGINALD-owned)** | REGINALD | +2,194 B since 10/20, of which +1,637 B is the 10/22 D:L793 fix commit (f8405c6f2) — i.e. DAEDALUS's own recommendations. MEMORY:55 "charter trim (77%) pending Will" has **no WILL_QUEUE or DOCKET row** (grep → none) |
| root CLAUDE.md | 24,634 | 76% | rotate | PROME/Will | not REGINALD's |
| 4 BOARD members 79–85% | — | — | rotate | WALTER | class-row artefacts |
| DECK_EVIDENCE.md | 24,091 | 74% | band | REGINALD | FROZEN 7/09 yet listed by charter :61 as a derived surface to "refresh or consciously skip" |
| STATUS / CALENDAR / ROADMAP | 23,487 / 23,495 / 23,400 | 72% each | band, **regrowing** | REGINALD | rotated properly on 10/28 to 22,145 / 22,734 / 22,756 B (<70%); regrew +1,342 / +761 / +644 B in 2 days. STATUS re-crosses 75% after +925 B (PAT-055) |
| STATUS_DASHBOARD.md | 33,571 | 103% | over budget, cold | REGINALD | not declared, not cap-bearing; its own "re-check 2026-10-02" passed and it grew 1,025 B on 10/28–29 |
| WAL / OZK REGINALD_CHANNEL.md | 29,071 / 25,427 | 89% / 78% | **undeclared** | WAL / OZK (files); REGINALD (declaration) | charter step 9a reads them EVERY boot (CLAUDE.md:42) but READS has no REGINALD row for either (only WAL's own row, READS:559) |

## F. DO-NOT-TOUCH items (prior profile) re-verified in this cluster

| Item | Still valid? | Receipt |
|---|---|---|
| Held: POSITIONS canonical over matrix column | YES | LESSONS.md:63-65; STATUS matrix carries scores only |
| Held: HY<260 = REVIEW, not auto-exit | YES | STATUS.md:62, :92 |
| Held: THRESHOLDS contract | CHANGED — now **13 columns** (sustain_unit, exit_condition, value_basis etc. added), not "8-col"; NOTES companion intact | `head -2 registry/THRESHOLDS.tsv` NF=13 |
| Held: 4-cluster independence framing | NOT FOUND in live surfaces (grep of STATUS/CLAUDE/MATRIX/CONVERGENCE → none); superseded by "2 channels instrumented, rest owner-held" | STATUS.md:18-20 |
| Held: MI3 methodology as signature | YES (method; old ratios dead) | CLAUDE.md:122-132 |
| Held: recursive drift-grep, never an enumerated list | YES | CLAUDE.md:63 |
| Held: frozen feeds stay frozen | YES, strengthened (boot.py legs removed; READS rows RETIRED) | boot.py:45-46; READS 494-496 |
| Held: boot-9b + BOARD schema | YES | CLAUDE.md:43-45 |
| 1 NOTES.md companion, never folded | YES | CLAUDE.md:163; registry/NOTES.md:10 |
| 2 REG-T-07 vs TREPP, CREED divergence deliberate | YES | registry/NOTES.md:25 |
| 3 WAL seam pointer-only | MOSTLY — exception in EXIT RULES (see D) | STATUS.md:30 vs :94 |
| 4 drift-grep example labelled dead | MOVED — now only in `archive/2026-10-20_organisation-cleanup_CLAUDE.md` (not live) | grep |
| 5 banners name their rewrite triggers | YES, but several named dates have lapsed un-actioned: DASHBOARD/BACKLOG "2026-10-02", BEAR_LEDGER "2026-10-14" | headers |
| 6 7/18 frames + STAGING files | not re-checked (reports/ out of cluster) | — |
| 7 EGBN reserve-read discriminator | per-bank tree archived → `archive/per-bank/EGBN/`; text survives under `research/EGBN/historical/` (grep hit, not read) | find/grep |
| 8 "547% FLAGGED not overwritten" | SUPERSEDED by the v2.0 rebuild, which explains 497/547 as ~2× wrong denominators | BANK_EXPOSURE_MATRIX.md:33 |
| 9 CREED/BELT freeze banners verbatim | YES | `archive/sub-agents/{CREED,BELT}/STATUS.md:1` |
| 11 "NOT a position name" FITB/PNC/RF | MOOT — dirs archived to `archive/per-bank/` (RETIREMENT_2026-10-22.md:13) | find |
| 12 historical WAL refs preserved | YES (CHANGELOG, archive) | — |
| 13 ZION/TODO §0 | archived with ZION (`archive/per-bank/ZION/TODO.md`); prior profile's "architecture question" is ANSWERED by archiving the whole per-bank tree | find |

## G. Reconciliation — prior profile (8/07 body + banners) and 10/22 review items in this cluster

| # | Item | Now | Receipt |
|---|---|---|---|
| 10/22-1a | EXIT RULES undated, 'CBRE' undefined, claims leg always met | **CLOSED** | STATUS.md:87, :93 |
| 10/22-1b | CRE anchor cites REG-24/25 (moved to WAL, invalidated 10/19) | **CLOSED** (re-keyed to WAL-01/02, evaluated NOT FIRED) | STATUS.md:94 |
| 10/22-1c | no kill-rail stamp | **CLOSED** | STATUS.md:87 |
| 10/22-2 | REG-T-07 no live reading; "No extensions" undated | **CLOSED** (12.16% Sept row; channel table rotated) | STATUS.md:109, :20 |
| 10/22-3 | FLEET_MAP REG-06 gap wrong (DAEDALUS) | CHANGED — FLEET_MAP 10/22 row already says REG-06 has the instrument; first scan due Sat 10/31 | FLEET_MAP row; CALENDAR.md:52 |
| 10/22-5 | trade-ideas-loosened not in charter | **CLOSED at charter level** (TRADE §2b not checked here) | CLAUDE.md:52 |
| 10/22-6 | no Resolve_By / no boot due-scan | **CLOSED** via sidecar + boot.py leg (7 OPEN rows dated) | boot.py:131-153; builtin run |
| 10/22-7 | read-cap rc1 BOARD class row; CALENDAR 76% | rc1 **OPEN (unchanged)**; CALENDAR **CLOSED-then-regrowing** (24,068→22,734→23,495 B) | readcap.txt; `git cat-file -s` series |
| 10/22-8 | FLG/GIBBS missing; pair channels not in boot/READS | FLG/GIBBS **CLOSED** (READS 481-482, CLAUDE.md:42); channels in boot **CLOSED**; channels in READS **OPEN** | READS grep |
| 10/22-9 | outbox lifecycle; 3 10/13 packets not in PROME/inbox | **CLOSED** — PROME late-consumed them 10/22 (`PROME/inbox/processed/2026-10-22_PROME_late-consume_REGINALD-2026-10-13-outbox-packets.md`); 19 old packets retired; outbox/README.md states sender-copy rule; 13 top-level remain | ls outbox |
| 10/22-10 | WAL channel zero ACKs | **CLOSED** (3 ACK blocks incl. 10/22 backfill; boot.py channels rc0) | WAL/REGINALD_CHANNEL.md:21,27,33 |
| 10/22-11 | FFIEC JWT expiry 11/05, no Will row checked | CHANGED — queued: WILL_QUEUE row 495.CDR "renew by Thu 11/5" and row 31 / DOCKET 2026-11-01 credential sitting; **renewal itself still pending (6 days)** | PROME/WILL_QUEUE.md:59-60; DOCKET.tsv:219 |
| 10/22-12 | earnings table omits ZION/HBAN/BaaS | MOSTLY CLOSED — ZION, HBAN, CCB added; CASH (printed 10/21, unread) and GDOT absent | CALENDAR.md:27-44 |
| 10/22-13 | boot.py exits 0, runs frozen feeds, lacks legs; options_oi.py unguarded | boot.py **CLOSED**; options_oi.py **OPEN** (0 FROZEN hits, last commit 2026-04-09, no invocation site) | boot.py:13, :45; grep |
| 10/22-14a | BOTTOM LINE undated / points to 10/20 / not last | **OPEN** | STATUS.md:124-139 |
| 10/22-14b | retired eight-channel table with 🔴 statuses | **CLOSED** (rotated BLOCK T34) | STATUS.md:20 |
| 10/22-14c | FHLB cell repeats leg-3 "grades 11/13 from the CFR" | **OPEN** (stated twice in one cell) | STATUS.md:104 |
| 10/22-14d | OPEN PROCESS ASKS deferred to undated "next touch" | **OPEN, and the V1V3-ACCELERATE row's own trigger ("next registry touch") has FIRED unactioned** — registry touched 8× since 10/9 (5344a98c8 … 85e342c8b); DAEDALUS falsification #5 packet re-asks | STATUS.md:137; `git log --since=2026-10-09 -- registry/` |
| 10/22-16 | glued words | **PARTIAL** — charter ≈2 left ("cap100" :65, "exit1" :33); STATUS 3 (:81 "at15%", "encoded10/21", "original20"); CALENDAR ≈14 ("READ10/20", "notice10/7", "call08:00", "due10/30", "filers11/4"…); ROADMAP ≈4; NEXUS_BRIEF "October30"/"October28" headings | grep -noP output |
| 10/22-17a | charter commands not cwd-proof | **OPEN** | CLAUDE.md:34, :47, :85 |
| 10/22-17b/c | `--trade` line; trade-ideas line | **CLOSED** | CLAUDE.md:34, :52 |
| 10/22-18 | root clutter, MTB/ unbannered | **CLOSED** (7 root files → `archive/root_retired_2026-10-22/`; per-bank tree → `archive/per-bank/`) | ls; RETIREMENT_2026-10-22.md:13 |
| 10/22-19 | CALENDAR claims row carries levels | **MOSTLY CLOSED** — now a pointer, but still restates "latest there: 194K [w/e 10/17]", now itself a print behind | CALENDAR.md:12 |
| PR-8/7 | STATUS 248/250 lines | **CLOSED** (139 lines; bytes govern) | wc -l |
| PR-8/7 | three-way STATUS-internal macro contradiction (dashboard vs threshold vs head) | **CLOSED** — dashboard split cold; STATUS carries one dated row per series (:111-114) | STATUS.md:24-26 |
| PR-8/7 | BANK_EXPOSURE_MATRIX:3 asserts refuted MI3 ratios hold; DECK_EVIDENCE:23 OZK 37.6% marquee | **CLOSED** (v2.0 rebuild; DECK line struck + correction) | MATRIX:1-20; DECK_EVIDENCE.md:24-26 |
| PR-8/7 | LESSONS falsifier-canon pointer broken | **CLOSED** — `../WAL/WEAKNESSES.md` and `../WAL/THESIS.md` both exist | ls |
| PR-8/7 | CLAUDE instructs maintenance of departed WAL/ subtree | **CLOSED** (no such line; WAL/OZK = peers, CLAUDE.md:11) | charter read whole |
| PR-8/7 | inbox 15 unprocessed; outbox drawer | **CLOSED** for the August backlog; **now 4 open** (2 DAEDALUS 10/30 packets + 2 WALTER 10/30 signals), all landed after the desk's 09:15 session | builtin run |
| PR-8/7 | per-bank tree unbannered / architecture question | **CLOSED** by archiving the tree 10/22 (Will's word) | archive/per-bank/ |
| PR-8/7 | MI3 screen repair owed | **CLOSED** 8/13 re-run; next run 11/07 (blocked by JWT if not renewed) | CLAUDE.md:122-130; CALENDAR.md:85 |
| PR banner 10/21 | "REG-06 still names no dated search instrument" | **WRONG then, CLOSED** — instrument since 10/10 | CALENDAR.md:52 |
| new | LESSONS footer "Last reviewed 2026-08-20" while body has 10/23 entries | OPEN (header-over-stale-body class) | LESSONS.md:71-81 |
| new | CALENDAR PREDICTION CHECKPOINTS says "REG-01 through REG-27, 21 rows" and WAL-01/02 "OPEN to Q3 10-Q" | OPEN — REG-28/29/30 registered 10/22 (STATUS:81); WAL graded both 10/19 (STATUS:94) | CALENDAR.md:79-81 |
| new | CALENDAR 11/07 and 11/05 rows sit headerless after `## PREDICTION CHECKPOINTS` + `---` (orphan table rows; won't render as a table; 11/05 listed after 11/07) | OPEN | CALENDAR.md:83-86 |
| new | REG-T-02 exit-log count restated in 3 places, 3 different vintages: CALENDAR "through 10/20: 35 rows", ROADMAP "40 rows through 10/27", STATUS "rows through 10/29" (log has 49 non-empty lines) | OPEN (both CALENDAR and ROADMAP say the count lives ONLY in the log) | CALENDAR.md:65; ROADMAP.md:21; STATUS.md:105 |
| new | ROADMAP OPEN QUESTION "Decide at the 10/22 H.4.1" (discount window) past its date; later entries say "decide with Will" with no queue row seen | OPEN | ROADMAP.md:63, :90, :92 |
| new | SCRATCH 10/07 section older than its own ~2-week prune rule; SCRATCH:12 points to retired THESIS | OPEN (low) | SCRATCH.md:12, 10/07 block |

## H. Ranked route list

| Rank | Sev | Finding (specific) | Owner | Ask |
|---|---|---|---|---|
| 1 | 🟠 | **READS perimeter is UNKNOWN, not clean.** `reads_check.py --agent REGINALD` → "⛔ ATTESTATION STALE (dated 2026-10-20)" (COMPLETION_SPEC committed 10/29); the charter itself is boot-defining and changed 4× after the attestation (f8405c6f2, 137aedf69, f984ce53c on 10/22; d3488e641 on 10/23). The every-boot step 9a reads of `AGENTS/WAL/REGINALD_CHANNEL.md` (29,071 B, 89%) and `AGENTS/OZK/REGINALD_CHANNEL.md` (25,427 B, 78%) have **no REGINALD READS row** | REGINALD (re-enumerate + declare channels as `scoped`: entries above latest ACK) → PROME (register) | Re-attest; add the two channel rows with their real mode |
| 2 | 🟠 | **DAEDALUS's FLEET_MAP row (scored 10/22) lists gaps that are now closed**: EXIT RULES undated / 'CBRE' undefined / CRE anchor on REG-24/25 (all closed STATUS:87-96), REG-T-07 no reading (closed :109), no Resolve_By (closed, sidecar + boot leg), boot doesn't scan inbox/WALTER (closed). Its Next_upgrade condition ("after the desk re-derives EXIT RULES with a dated stamp") is MET (stamp 2026-10-22) | DAEDALUS | Re-cut the row at this refresh; adjudicate the L3 dated-falsification leg now; regenerate FLEET_DIRECTORY |
| 3 | 🟠 | **Charter 24,977 B = 77% (rotate-tier, REGINALD-owned)**; rule-5 stop needs −2,193 B. It was 70.0% (22,783 B) on 10/20; +1,637 B came from the 10/22 D:L793 fix commit implementing DAEDALUS's own review. MEMORY:55 carries "charter trim pending Will" but no WILL_QUEUE/DOCKET row exists (grep) — an undated carry | REGINALD (propose a verbatim rotation or hot/cold split — e.g. HIDDEN CRE methodology :122-132, BaaS paragraph :95, FILES :157-166 are reference, not boot procedure); PROME (queue a dated Will row if the trim needs Will's word); DAEDALUS (own share: price byte cost into future charter-adding asks) | Register the decision with a date; execute to <22,785 B |
| 4 | 🟠 | **read-cap RC=1 unchanged since 10/22**: `BOARD/SIG-W-20260619-008` 39,509 B (121%) via the `BOARD/SIG-W-*.md whole` class row (READS 488, 1,863 members). The 10/22 reading-companion row (READS 489) did not clear rc because the class row still measures the original | PROME (registrar) + DAEDALUS (tool: a "selected / new-since-BOARD_LOG" class mode or companion-shadowing) + WALTER (file) | Pick one remedy; the desk cannot clear this rc alone |
| 5 | 🟠 | **FFIEC CDR JWT expires Thu 11/05** — gates the FFIEC short-list re-run (window Sat 10/31–Wed 11/04, MEMORY:45), the 11/07 Call Report run, MI3 Q3, matrix re-score, L180 breadth and the frozen ranking test. Queued (WILL_QUEUE 495.CDR; row 31; DOCKET 2026-11-01 credential sitting), not yet done | Will (renew); PROME (11/01 sitting) | Renew before 11/05; desk dry-runs one pull after |
| 6 | 🟡 | `## BOTTOM LINE` undated, points to the 10/20 report, not the last section (OPEN PROCESS ASKS follows) — the live judgment is the head block (:7) | REGINALD | Date it and point it at :7 / the 10/30 report, or fold it into the head and make it last |
| 7 | 🟡 | Recognition-lane exit anchor is a 3-leg AND whose leg 3 (REG-03, FDIC Q4 QBP) resolves ~late Feb 2027 ⇒ that stand-down REVIEW cannot fire for ~4 months; "each leg already has its own base rate" unverified | REGINALD | Confirm the lag is intended, or say which leg can REVIEW alone |
| 8 | 🟡 | thesis/CHANGELOG has no entry after 10/12 although 10/22 retired an exit leg and re-keyed the CRE anchor, and 10/30 dropped the coverage-decline predictor (charter :63-64: "framing/claim retirement" → CHANGELOG) | REGINALD | Append dated entries or state on the surface why they are not thesis-level |
| 9 | 🟡 | `V1V3-ACCELERATE` rename: STATUS OPEN PROCESS ASK deferred to "next registry touch"; registry touched 8× since 10/9 without it; falsification #5 packet re-asks (THRESHOLDS.tsv:3) | REGINALD (+WALTER, which reads the token) | Execute or date the deferral |
| 10 | 🟡 | Regrowth after the 10/28 rotation: STATUS 72.2% (+1,342 B in 2 days; re-crosses 75% after +925 B), CALENDAR 72.2%, ROADMAP 71.9%, MEMORY +2,685 B. STATUS_DASHBOARD (cold) 103.1% and growing; its re-check date (10/02) lapsed | REGINALD | Byte-neutral write-backs; split/rotate DASHBOARD before its next append |
| 11 | 🟡 | CALENDAR structure/currency: 11/05 and 11/07 rows orphaned without a table header under `## PREDICTION CHECKPOINTS` (:83-86); that section says "REG-01 through REG-27, 21 rows" and WAL-01/02 "OPEN" (:79-81) — both stale; REG-T-02 log count restated at 3 vintages across CALENDAR:65 / ROADMAP:21 / STATUS:105 | REGINALD | Re-home the two rows into §LATER; point, don't count |
| 12 | 🟡 | Glued words remain (root Output Canon): CALENDAR ≈14, STATUS 3 (:81), charter 2 (:33, :65), ROADMAP ≈4, NEXUS headings "October30" | REGINALD | Re-space on next touch; rotate (don't compress) if bytes bind |
| 13 | 🟡 | Charter boot commands at :34, :47, :85 are bare root-relative; launch is `cd AGENTS/REGINALD && claude` | REGINALD | Wrap as `"$(git rev-parse --show-toplevel)/…"` |
| 14 | 🟡 | DECK_EVIDENCE is FROZEN (7/09 banner) yet charter :61 lists it as a derived surface to "refresh or consciously skip" and READS 502 declares it a whole closeout read (74%) | REGINALD → PROME | Drop it from the closeout derived-surface list / re-declare as on-demand |
| 15 | 🟡 | Header-over-body drift: LESSONS footer "Last reviewed 2026-08-20" over 10/23 entries; ROADMAP open question dated "decide at the 10/22 H.4.1" (:63) still open; SCRATCH 10/07 block past its own prune rule and :12 points to retired THESIS | REGINALD | Hygiene at next closeout |
| 16 | 🟡 | `scripts/options_oi.py` appends to FROZEN OPTIONS_OI.tsv with no frozen guard; no invocation site; last commit 2026-04-09 (10/22 #13 residue) | REGINALD | Archive it or add the guard |

## I. Coverage

| Surface | Read | Ranges / method |
|---|---|---|
| AGENTS/REGINALD/CLAUDE.md | whole | 1–166 |
| STATUS.md | whole | 1–139 |
| LESSONS.md | whole | 1–81 |
| CALENDAR.md | whole | 1–88 |
| MEMORY.md | whole | 1–91 |
| ROADMAP.md | whole | 1–94 |
| SUB_AGENTS.md | whole | `cat` (23 lines) |
| scripts/boot.py | whole | 1–245; builtins executed in isolation |
| STATUS_BEAR_LEDGER.md | whole, lines cut at 600 chars | `cut -c1-600` (17 lines) |
| SCRATCH.md | whole, lines cut at 400 chars | `cut -c1-400` |
| NEXUS_BRIEF.md | part | 1–14 + grep pin |
| DECK_EVIDENCE.md | part | first 3,500 B + all `#` headings |
| BANK_EXPOSURE_MATRIX.md | part | first 5,000 B (≈1–44) + headings + 229–243 |
| STATUS_DASHBOARD.md | part | first 1,500 B + size history |
| STATUS_MATRIX.md | part | 1–12 |
| MEMORY_REFERENCE.md / ROADMAP_BACKLOG.md / BANK_RESEARCH_STANDARD.md | part | heads (6–8 lines) |
| thesis/THESIS.md, TIMELINE.md | part | heads (12 / 6 lines) |
| thesis/CHANGELOG.md | part | 1–10 + headings + grep for 10/2x, CBRE, L801 |
| kernel/*.json, staged_increment2/README.md | part | keys + companion_of/purpose; README 1–15 |
| registry/THRESHOLDS.tsv, NOTES.md, REG_T02_EXIT_LOG.tsv | part | header + rows 3, REG-T-07; NOTES grep; log tail + line count |
| inbox/ (2 DAEDALUS packets) | whole | both; WALTER/ 2 signals listed only |
| outbox/ | listing + README head | — |
| WAL / OZK REGINALD_CHANNEL.md | part | headings + ACK grep + first 12 lines |
| PROME/registry/READS.tsv | REGINALD rows | 453–508 (+559) |
| PROME/WILL_QUEUE.md, DOCKET.tsv | grep only | JWT/CDR, charter trim, discount window |
| baselines | whole | prior profile 1–48; 10/22 review 1–113; FLEET_MAP row |
| Commands (read-only) | — | `read_cap_check.py --agent REGINALD` RC=1; `PROME/tools/reads_check.py --agent REGINALD` RC=1; `git log/cat-file` size series; boot.py builtins |

**Not verified / not read:** POSITIONS.md, TRADE.md (beyond 2 header lines — TRADE shows a 10/22 two-clock header and "RECONCILED 2026-10-22" banner, so 10/22 #4 looks closed, left to the trade reader); workbook/*.tsv contents (PREDICTIONS, VX, KB); reports/ (incl. 7/18 frames + STAGING, DNT #6); research/, domain/, archive/ bodies; boot.py subprocess legs (market.py, thresholds.py, kre_float.py, earnings_countdown.py, insider.py, 8k_monitor.py, vx_ladder_check.py) not run; WAL's 10/19 grades (30bp, $272.75M) not re-verified at WAL's ledger; the "each leg has its own base rate" claim (STATUS:96); whether `--check-only` truly writes nothing in every subprocess leg; WALTER signals SIG-W-20261030-007/-010 bodies.

**REGINALD state during the read:** `git status --porcelain -- AGENTS/REGINALD/` empty at 16:41:18 (start), 16:41:53 (around the boot.py builtin run), 16:46:03, and at close (below). No REGINALD commit landed during the read; desk's own HEAD stayed 9ebedf3e2 / 4222ea74d (10/30 09:14–09:15); path HEAD 33f7a2638 (WALTER).

**Close:** 2026-10-30 16:48:58 EDT (from `date`); porcelain on AGENTS/REGINALD/ empty; path HEAD unchanged at 33f7a2638.
