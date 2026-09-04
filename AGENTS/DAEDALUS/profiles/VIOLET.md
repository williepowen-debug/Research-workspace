# Agent Profile — VIOLET

**Built by:** DAEDALUS · **Body vintage: 2026-09-04 (Fri, EVE) — FULL REFRESH** (prior body 7/22, Δ-bannered since PR#4 8/17; this replaces it) · **Comprehension method:** Mode-A 4-reader fan-out on Opus, read-only, no VIOLET script executed beyond `--help`/`--selftest`; reports persisted (PAT-100): `VIOLET_REFRESH_2026-09-04_READER_A.md` (identity/state/handoff) · `_B.md` (thesis/gates/trade) · `_C.md` (quant engine/workbook) · `_D.md` (predictions/KB/research). **Every 🔴/🟠 finding below was re-verified at the artifact by DAEDALUS after the readers reported**; where a reader was wrong the corrected figure is given and the reader's is struck. **Refresh clock: 21 d → 2026-09-25**, or at the first of: the 9/16 letter grade · KB.tsv two-state ruling · the next external review round.
**Occasion:** Will, 2026-09-04 EVE: *"analyze the rest of VIOLET — what else could use some help or attention from us?"* — the day after two external review rounds on this desk (KB-VIO-242/243) and the DESK_HARDENING_PATTERNS extraction.

> Durable understanding — section-tasks read THIS, not the raw (heavy) agent. Re-read the actual file before applying any change (PAT-009). VIOLET is LIVE (`violet-2a`); every disposition is a task packet, never an edit (AUTHORITY, both guards).

---

## 1. Identity and shape

VIX / vol-term-structure desk; the fleet's **modulation layer** (dual channel: Path A credit-led, Path B concentration-unwind; `thesis/VIX_THESIS.md:236-268`). Market class, ROSTER active. **Cadence:** ~1 commit/day over 30 d; 2026-09-04 alone = 8 commits, one crash, two Codex review rounds. **Posture today:** FLAT since `TRY-VIOLET-VIXCS` closed 7/30 (−$111.60); nothing fired; cheap-tail window OPEN 4/4 into CPI 9/11 + FOMC 9/16 (operator surface, no proposal).

**File anatomy (bytes, HEAD `f4950fa8b`):** `CLAUDE.md` 25,322 · `STATUS.md` **32,546** · `SCRATCH.md` 17,997 · `MEMORY.md` 21,457 · `CALENDAR.md` 20,880 · `NEXUS_BRIEF.md` 30,826 · `CANARY_MAP.md` 31,301 · `TRADE.md` 37,386 · `MAINTENANCE.md` 49,179 · `SIGNAL_INTAKE.md` 18,781 · `board_log.tsv` 76,193 (112 rows) · `thesis/VIX_THESIS.md` 58,233 + `CHANGELOG.md` 49,754 · `workbook/` 31 files 2.77 MB (`KB.tsv` **548,743**, 243 rows · `VX_TERM_HISTORY.tsv` 988,592 · `vix_historical.csv` 645,998) · `scripts/` 34 files · `research/` 47 files · `reports/` 3 · `archive/` 20.

**Boot whole-read set (`CLAUDE.md:22-25`):** STATUS 32,546 · SCRATCH 17,997 · MEMORY 21,457 · CALENDAR 20,880 · CATALYSTS 3,930 — each under the 32,550 B budget; STATUS at **99.99 %** (4 B headroom). *(Reader A's "96,810 B = 178 % of cap" is a context-cost sum, not a cap breach — the read cap is per surface. The SCRATCH read WAS invisible to `read_cap_check` until 2026-09-04 EVE: bare `'last '` scope marker matched "from last session"; fixed fleet-wide, 11 desks recovered, commit `3a0924400`.)* `boot.py` then runs 14 stages whose internal reads no byte checker sees (by design, declared in the tool's perimeter line).

## 2. Where the richness lives (read these, in this order, for any section task)

| Dimension | Local form | Read |
|---|---|---|
| Thesis | v4.0 (8/27) — dual channels; "level-signal decay is a CLASS"; 7 numbered predictions + scoring rules `:426-448`; **tail §"Current status" is 2026-06-10, 86 d stale, present-tense** (`:479-511`), footer still v3.5 (`:515`) | `thesis/VIX_THESIS.md` |
| Convergence | 11-vector / 55-pt matrix, **STATUS-only** (not in the thesis; untagged by thesis version) `STATUS.md:95-111`; `scripts/convergence_score.py` sums it mechanically — **in no boot or closeout step** | `STATUS.md` + `scripts/convergence_score.py` |
| Gates / kill tree | STATUS `:83-90` register: RED-FT-10 (ARMED 1-of-4, CBOE basis, chain 9/3·9/4·9/8·9/9) · KB-VIO-123 6-leg tree (0/6 FADE) · GATE-VIO-116 F1 72.41 re-arm · RV1 RETIRED (F2-killed 8/27) · T9 conjunctive falsifier (one leg measured by an instrument STATUS:72 calls UNUSABLE) · **no VIOLET row in `PROME/GATES.tsv`** (letter routed "as a READ, not a gate row", `letter:177`) | `STATUS.md`, RED `FALSIFICATION_TRIGGERS.tsv` |
| Pre-registration | **Exemplary form:** `research/2026-09-16_FOMC_VIXEXPIRY_PREREG_LETTER.md` (5 legs, frozen 9/2, both-sided bands, INCONCLUSIVE + whole-map NULL declared, anchor TYPE per leg, own weaknesses listed); `research/2026-09-04_nfp_vol_reaction_prereg.md` (same-day card, H-5 of DESK_HARDENING) | `research/*PREREG*` |
| Predictions registry | **SPLIT, no `PREDICTIONS.tsv`:** thesis table #1–7 · the letter's 5 legs · `KB.tsv Stale_By` as de-facto resolver for everything else; no Brier/score surface | see §4 |
| Canaries | `CANARY_MAP.md` — 6 CURRENT cells + tier-3 GEX; DARK contract >2× cadence `:57`; standing `^SKEW` at-moment-of-use rule `:48-53` (H-3) | `CANARY_MAP.md` + `scripts/canary_staleness.py` |
| Trade | `TRADE.md` — FLAT; 7/1 tail-hedge framework RETIRED-SUPERSEDED (WQ-177, Will 9/4 11:11) but its `## LIVE DECISION FRAMEWORK` heading, PENDING gates on a 7/02 print, and re-arm block survive (`:108-119`); footer `Last Updated 2026-07-28` (`:261`); **TRADE LOG `:242` still shows the 7/30-closed spread as OPEN** | `TRADE.md` |
| Quant engine | 34 scripts: 14 boot stages (`boot.py:31-66`), 5 blocking + 1 advisory closeout contracts (`closeout_guard.py:67-75`), 12 research/one-shot tools, 3 unowned-in-practice (`test_daily_log.py` · `skew_integrity.py` · `convergence_score.py`) | reader C §1-3 |
| KB | 243 rows, **schema-perfect** (0 ragged, 0 orphan refs, 0 id gaps — best measured on the fleet); +11.7 rows/wk lifetime, +30 rows/wk now; **100/216 live rows (46 %) past `Stale_By`, 93 empty**; no two-state plan | `workbook/KB.tsv` |
| Handoff | SCRATCH (own next boot) · LAST_COMPLETION (PROME) · NEXUS_BRIEF (NEXUS, Amendment-10 ordering — mechanized 9/4 after 31 d as a sentence) | reader A §3 |
| Mail | inbox empty (7/7 drained 9/4); `outbox/` **8 top-level packets, 7 delivered and never moved to `delivered/`, 1 no trace** (`2026-08-27_to-PROME_GATE-VIO-RV1-transcription-verified-clean.md`) — reader A's "3 no trace" was wrong: the LIQUID and TERRY packets sit in those desks' `inbox/processed/` | `outbox/` |

## 3. Boot and closeout mechanics — what is code and what is a sentence

Mechanized (code, blocking at closeout): KB enums (`validate_workbook`) · grading-note citations · CANARY ledger staleness (`--strict`) · write-back ORDERING vintage (`writeback_order_check`, built 9/4) · CALENDAR⇄CATALYSTS twin (`twin_check`, bidirectional v2). Advisory only: thesis bump. **Sentence-only:** promotion scan (step 13) · MAINTENANCE entry (13a) · **the entire root closeout battery 1b–1e** (charter step 14 cites only §Git Protocol) · "run `skew_integrity` at the moment of use" · "run `test_daily_log.py`". **Two caps advertise a mechanism that does not exist:** `MAINTENANCE.md:131` *"enforced at boot by `check_maintenance_cap()`"* — zero hits repo-wide; `README.md:12,17` "boot-enforced" line caps — nothing in `boot.py`.

**Guard integrity (verified at the lines):** `closeout_guard.run()` returns rc 0 `(skipped — not present)` on a missing script → **all five blocking contracts fail OPEN on file absence** (`:81-82`, clean line `:122`). `boot.py` prints `✓ ran cleanly, no alerts` for a stage whose output carries no KEY_MARKER even when rc≠0 (`:147-156`), and `move.py` returns **0** on primary failure unless `--strict`, which `boot.py:42` does not pass → MOVE dark reads ✅ at the line a session reads. `canary_staleness` CANARY_MAP leg: matcher `:193-195` recognises `Current [M/D]` and `[M/D] STATE` only — **1 of 6 live cells** (basis tokens inside the bracket, e.g. `[8/4 SETTLE]`, escape it); `date(today.year, mon, day)` `:207` goes blind across New Year; missing map returns clean `:176-177`; rc 1 only under `--strict`, boot runs `--quiet`.

## 4. Per-leg maturity read (ladder, market class) — **L4 held, Conf H**

| Leg | Verdict | Evidence |
|---|---|---|
| L3 convergence matrix | ⚠️ present, **arithmetic does not reconcile**: header 25/55 (`STATUS.md:97`), prose "FLAT at 26" (`:113`), cells sum 33 (`:101-111`) | reader B §1, verified |
| L3 exit rules | ✅ named per gate; RV1 killed by its own pre-registered F2 (exemplary) | `STATUS.md:86`, KB-VIO-211 |
| L3 predictions resolving | ✅ resolving (6 graded in 30 d, KB-VIO-196…233) — ⚠️ registry split three ways; thesis table row #7 still "Untested" while KB-VIO-220 graded it HIT 9/2; no score surface | reader D §1 |
| L3 dated falsification surface | ✅ letter + NFP card exemplary · 🔴 thesis tail 86 d stale present-tense (invalidation "CLOSE-AND-HOLD above 23", HY 2.75 [6/8], "Iran/oil leg LIVE") | `thesis:479-515` |
| L4 TRADE.md feeding proposals | ⚠️ has fed (7/1 packet → VIXCS via TERRY); today FLAT; **two-state banner FAILS** (no FROZEN, no vintage header, footer 7/28) and the ledger contradicts itself (`:242` OPEN vs `:15` closed) | reader B §3 |
| L4 signals flowing | ✅ NEXUS_BRIEF every session, 454 routing arrows in KB `Vectors`, packets to HENRY/VULCAN/RED/PROME 9/4 | reader D §6 |
| L5 clean closeouts | ⛔ 9/4: two external rounds found defects in a "5/5 green" closeout; 8 cross-surface contradictions survive (C1–C8, reader A §3) | KB-VIO-242/243 |
| L5 current | ⛔ CANARY_MAP six CURRENT cells 31–38 d (cheap-tail cell reads DORMANT 1/4 vs live OPEN 4/4; GEX band sign inverted since) | `CANARY_MAP.md:19-41,106` |

**Conf H** because every cell above was read at the file this evening, by four readers and re-verified by DAEDALUS. The 6/6-handles re-verification the 9/1 row still owed is discharged by this read.

## 5. Findings register 2026-09-04 — what could use help, ranked (owner in the last column)

| # | Finding (exact locator) | Failure it risks | Owner · route |
|---|---|---|---|
| 1 🔴 | **Thesis tail 86 d stale, present-tense** (`thesis/VIX_THESIS.md:479-515`) | the canonical falsification tail names a dead kill (VIX 23) and a retired posture; the 9/16 grader inherits it | VIOLET · packet |
| 2 🔴 | **Convergence matrix does not add up** (`STATUS.md:97/113/101-111` = 25 / 26 / 33) and `convergence_score.py` is wired nowhere | the number other desks quote out of this surface is three numbers | VIOLET · packet (wire the script into `closeout_guard`) |
| 3 🔴 | **CANARY_MAP CURRENT cells 31–38 d stale, two state-inverted; the guard sees 1 of 6** (`CANARY_MAP.md:19-41,106`; `canary_staleness.py:193-195,207,326`; `boot.py:52`) | the fleet's cross-domain early-warning surface is wrong on the day the window is OPEN | VIOLET · packet |
| 4 🔴 | **`MEMORY.md:168` still teaches the CFTC Tue→Fri calendar retracted the same day** (KB-VIO-243; boot whole-read) | the desk re-derives v3 from its own memory within two sessions | VIOLET · packet (one line) |
| 5 🔴 | **Closeout guard fails OPEN on a missing check; boot prints clean over a crashed stage; MOVE rc 0 on primary failure under `--boot`** (`closeout_guard.py:81-82`; `boot.py:147-156`; `move.py:163` + `boot.py:42`) | the guard built to convert detection into action certifies health it never checked | VIOLET · packet |
| 6 🟠 | **STATUS 4 B under budget after three rotations in one day; +9 KB in 24 h** (23,520 → 32,546 B across `756bf3397`→`f4950fa8b`) | the next sentence breaches; same shape as LABOR's WQ-179 escalation | VIOLET (rotate before the next write) · **PROME: second live instance for WQ-179 rec (c) / H-8** |
| 7 🟠 | **VX_DAILY missing 8/28, 8/31, 9/1, 9/3; nothing checks completeness; `CALENDAR.md:107` says `ledger_staleness` does** | the FT-10 chain and 20d avg cannot be reproduced from the desk's own ledger; max-date reads green | VIOLET (backfill + completeness check) · DAEDALUS (`CHECKS.tsv`: ledger_staleness PASS proves vintage, not completeness) |
| 8 🟠 | **Prediction registry split; thesis table row #7 "Untested" vs KB-VIO-220 HIT; no score surface; `VIO-FOMC-0916` legs in neither registry** | hit-rate unreadable; the 7/11 domain-sweep defect (row #6) returned on row #7 in 54 d | VIOLET · packet |
| 9 🟠 | **KB.tsv 46 % of live rows past `Stale_By`, 93 empty; 549 KB, +34.6 KB on 9/4, no two-state plan** | ACTIVE certifies currency nothing checks; the desk's richest artifact in the silent-rot middle | VIOLET (triage + plan) · DAEDALUS (Stale_By check is a fleet-KB pattern → build queue) |
| 10 🟠 | **TRADE.md: two-state banner fails; log row `:242` OPEN vs `:15` closed; retired framework still headed LIVE with PENDING gates on a 7/02 print** | a reader takes a retired framework as armed | VIOLET · packet |
| 11 🟠 | **`skew_integrity.py` covers 1 of 10 mirrors, invoked by nothing; `cheap_tail.py:92` consumes `^SKEW` unchecked on an OPEN operator surface; `implied_corr.py:62-74` degrades CBOE→yfinance with no trace** | H-3 exists as a rule on this desk and is not run where it matters most | VIOLET · packet (call it from `cheap_tail`; stamp the verdict) |
| 12 🟠 | **Three ledgers in the silent-rot middle** (`VX_M1_HISTORY.tsv` 37 d no writer/reader · `VX_TERM_HISTORY.tsv` 32 d no reader · `vix_historical.csv` 147 d un-bannered while both siblings are FROZEN); `MOVE.tsv`/`IMPLIED_CORR.tsv` outside `CANARIES`; **no `workbook/LEDGER_GLOB`** | root two-state rule unmet; closeout 1c-bis nudges on nothing | VIOLET (banners + CANARIES) · **DAEDALUS/PROME: LEDGER_GLOB exists on 7 of 43 desks — a fleet gap, sweep #2 leg** |
| 13 🟠 | **Grade dates 9/16 · 9/18 · 9/23 (letter) and FT-10's 9/9 earliest fire live only in VIOLET/RED files**; DOCKET L125 names the FOMC with `CALENDAR.md` as artifact and no grade dates; letter reached PROME 9/2 as a read | if VIOLET is dark on 9/16 nothing on the coordination layer knows a grade is due | **PROME** · DOCKET rows with the artifact path |
| 14 🟡 | **`outbox/` lifecycle stopped**: 7 of 8 delivered and never moved to `delivered/`, 1 no trace; 9/4 packets bypassed the directory | the directory's only signal is noise; the 7/30 audit is owed again | VIOLET (`git mv` the 7) · PROME (to-PROME consumption is unverifiable from the sender: convention question) |
| 15 🟡 | **8 cross-surface contradictions after the 17:17 close** (convergence 25/26; KB-rows-since-v4 12/29/20; 3 vs 6 sessions; NFP measurement owed-vs-graded; footer 09:0x on a 17:17 commit; short-vol "deepened three running" vs "stopped") | summary blocks not rewritten with the body — the vintage-only guard's declared blind spot, landing on its author | VIOLET · packet; **DAEDALUS: a within-file same-metric-two-values check is buildable** |
| 16 🟡 | **Two phantom caps** (`MAINTENANCE.md:131` `check_maintenance_cap()`; `README.md:12,17` "boot-enforced") | a named non-existent check reads as coverage — the ritual≠mechanism class the desk logged n=6 that day | VIOLET · delete the claim or build the 15 lines |
| 17 🟡 | **12 research files retirement-eligible** (>60 d, unreferenced by any live doc; VIOLET's own transitive rule `README.md:28`; last sweep 7/30) and `reports/2026-07-11_threads-sweep.md` carries open items with zero closure markers | corpus rot; silently-abandoned triage | VIOLET · sweep (moves only, never rewrites) |
| 18 🟡 | **DOCKET L115 (8/5 VIXCS exit-evaluation, TERRY-owned) PENDING 30 d** | a July trade's pre-registered grade never closed on the coordination layer | **PROME/TERRY** |

**Not findings (checked, clean):** inbox lanes · R1 corrections (rc 0, one NO-OP receipt correctly reasoned) · CALENDAR⇄CATALYSTS 1:1 today · no MODELED date carrying a decision · KB schema · walter_route_check leg A clean · every letter leg gradeable from a named source at a named time.

## 6. Do-not-touch quirks

- `research/`, `reports/`, `outbox/delivered/` are immutable record (`MAINTENANCE.md:72`): retirement **moves** are legitimate, content rewrites are not. KB rows are marked SUPERSEDED/CORRECTED in place, never deleted (`CLAUDE.md:47`).
- The FOMC letter is FROZEN (`§4`): a dated addendum, never a rewrite — two of its five declared weaknesses (#2 MOVE gap "unexplained"; #3 gamma "UNMEASURED") went stale 9/4 and want an addendum, not an edit.
- `thesis_bump_check` is advisory by design; do not propose making it block (its own docstring explains why).
- STATUS rotation = byte-verbatim + crc32 into `archive/STATUS_SESSION_LOG_<date>.md`; the desk does this correctly, three times on 9/4.
- The desk's self-diagnosis is unusually sharp (KB-VIO-234/240/242/243 are the fleet's best-written instances of ritual≠mechanism); the recurring shape is **instance fixed, mechanism not** — row #6 → row #7 in 54 d; 8/04 reference-gap fix → same gap in 12 files; three STATUS rotations in a day and 4 B headroom. Route mechanisms, not lists.

## 7. Open questions for the owner (asked in the packet, not answered here)

1. Is the 55-pt scale still 11 × 5, and is cheap-tail (an opportunity vector) meant to ADD to a stress score? The three published totals suggest the scale itself is undeclared.
2. Which registry is meant to be canonical for forward predictions — the thesis table, the KB `Stale_By` column, or a `PREDICTIONS.tsv` the fleet form expects (`FORGE/PREDICTION_DISCIPLINE.md`)?
3. KB.tsv: FROZEN-by-date rotation (rows before v4.0 → cold) or LIVE with a `Last real data refresh:` header — which two-state form?
