# CREED File Index

**Purpose:** separate current CREED operating truth from legacy source archive material.

## Current boot / operating files

**The boot order is canonical in `CLAUDE.md` § Canonical Boot Order and is not restated here** (re-pointed 2026-10-30, DAEDALUS profile-refresh item 9: this file carried its own numbered list, which had drifted from the charter's). In short: SCRATCH → CLAUDE.md → STATUS → this README → COVERAGE → the predictions scan (4b) → `scripts/threshold_scan.py` (4c) → the current rails (step 6) → `workbook/VX.tsv` + staleness check (7) → corrections check (7b). The list itself lives only in the charter.

## Operating ledgers and logs *(added 2026-07-27 — fleet-parity pass against SHADE/BROCK)*

| File | Role |
|---|---|
| `board_log.tsv` | **Every mail item CREED has read, with its reasoned disposition.** Logged at READ time. An unlogged consume is indistinguishable from a never-seen. ⚠️ Pre-2026-07-11 lane history is **prose-sourced, deliberately not retrofitted** — see the `[PRE-LEDGER-BACKFILL]` row. |
| `SCRATCH.md` | Ephemeral session handoff (overwritten each closeout). Created after an unclean shutdown left CREED with no in-flight-work surface. |
| `MAINTENANCE.md` | **Structural** change log — why CREED is organized this way. **Consult-on-structural-work, NOT a per-session ritual.** Analytical pivots go in `thesis/CHANGELOG.md` instead. |
| `COVERAGE.md` | Lane-by-lane coverage map keyed to **data vintage**, with maturity grades and the blind-spot register. Adopted from `CORAL/COVERAGE.md`. |
| ~~`REVIVAL_PLAN.md`~~ | ⛔ **FROZEN 2026-07-27** — closed episode doc, out of the boot order. Live items forked up to `CLAUDE.md` §Guardrails. Do not cite as current. |
| `LAST_COMPLETION.md` | Closeout stamp. ⚠️ **It skipped the 7/20 and 7/27 closeouts and went stale enough to propagate a wrong claim three hops.** If `STATUS.md` is materially newer than this file, **a closeout was skipped — treat its claims as UNKNOWN, not current.** |

## Threshold registry — `registry/` *(added to this index 2026-08-20; it existed since 7/27 and this file never listed it)*

| File | Role |
|---|---|
| `registry/THRESHOLDS.tsv` | **Machine-readable transcription of the FIRE conditions in `thesis/THESIS.md`.** 11 `CREED-T-*` rows. **Bands are FROZEN TERMS (Will, 7/21) — propose, don't edit.** ⚠️ **Only 5 rows are numerically scannable**; the rest are qualitative, compound, or HOMER-owned — **a clean scan of the 5 must never imply the 11 are clear.** ⚠️ **A LONG comment block precedes the header — count rows matching `^CREED-T`, never `tail -n +2` and never a hard-coded offset.** *(This cell asserted "14 comment lines" until 2026-08-27, when the actual count was **25** — a stale number sitting inside the very warning against hard-coding one. The count is deliberately NOT restated here now: it changes whenever an obligation is logged, so any number written here is a future defect. **Derive it, don't cite it.**)* ⚠️ **This file is also the DURABLE HOME for open band-authority obligations** (awaiting-Will items and approved-but-overdue work) — SCRATCH is overwritten each closeout and the PROME docket is another desk's surface. WALTER reads this file. |
| `registry/CREED_T_FIRED_LOG.tsv` | **NEW 2026-08-20 — the SINGLE record of CREED-T fires.** Carries `effective_date` and `detection_lag` as separate columns on purpose: the date a band was satisfied is not the date CREED noticed. ⚠️ **Deliberately the only such ledger** — WALTER asked to build a mirror and CREED declined (a fire recorded in two disagreeing places is worse than one recorded nowhere). |
| `registry/PREREG_2026-10_TREPP_PRINT.md` | **The SEPTEMBER-2026 print pre-registration — FROZEN on its 2026-09-26 commit, before the print.** September **cannot fire `T-01a`** (0 of 2 legs; 12.00 is not > 12) — it can only start leg 1. Tie convention and refusals declared in advance. **GRADED 2026-10-21 below §6: 12.16 = leg 1 of 2; `T-01b` 16.85 not fired; F1 not triggered.** |
| `registry/PREREG_2026-09_TREPP_PRINT.md` | **The August-2026 Trepp-print PRE-REGISTRATION — ⛔ FROZEN above its line 2026-08-27, GRADING RECORD appended below it 2026-09-02.** ⭐ **The strongest instrument this desk has built, and it proved itself on first use:** written a week before the print because `CREED-T-01a` sat 9bp from a `> 12` band, it fixed the grading rule in advance, enumerated the **11.92–12.00** case explicitly, and pre-refused the sentence *"it basically cleared."* **The print landed at exactly `12.00`.** ⚠️ **Append below the line; never edit above it — the whole value of the document is its date.** |

## Scripts — `scripts/`

| File | Role |
|---|---|
| `scripts/creed_selfcheck.py` | **Closeout guard (step 8b), CREED-scoped, ~25ms, exit 0/1.** Fired-trigger cross-surface consistency · asserted counts vs actual · open staleness banners. ⚠️ **A green certifies its SCOPE, not the work** — its scope is stated at `CLAUDE.md` closeout step 8b (checks ①–③). |
| `scripts/s8a_relative.py` | **Run with `.venv/bin/python3`** (plain `python3` lacks yfinance). **NEW 2026-08-20 (PM).** The S8a recompute recipe (`VX-CREED-7.01` / `CREED-T-08a` / `PRED-CREED-007`) — VNQ vs SPY trailing relative on **both bases**, printed alongside the **series, its noise band and the band's base rate**, because a single trailing-3mo point is demonstrably not a usable read. `--end YYYY-MM-DD` re-derives any past reading. ⚠️ **Exists because COVERAGE lane 9 promised a recipe "in this row's source note" that did not exist**, making both committed readings non-reproducible (found by PROME). `FORGE/tools/market-data/fetch.py` cannot produce this figure (`price`/`fred` only). |
| `scripts/threshold_scan.py` | **NEW 2026-08-27 — BOOT STEP 4c**, ~30ms, read-only, exit 0/1. Current vector values vs **all** frozen bands, **at boot**. **This is `CREED-T-02`'s root cause closed** — no boot step read the registry, so a metric of **66** sat against a band of **50** in CREED's own workbook for **~6 weeks** ungraded (K5 falsified dark-cadence as the cause: CREED was awake and holding both numbers). ⚠️ **A green certifies arithmetic on resolvable rows only** — it never prints "all clear", enumerates every unscannable row by name and reason each run, and **`⛔ BLOCKED` is not `✅ CLEAR`**. ⚠️ **`🔴🔴 TRIPPED` = go grade it at primary; it is NOT a fire.** Verified against the real K5 event on both wirings before shipping. |
| `scripts/test_history_validation.py` | **NEW 2026-09-30.** Fixture tests for the n=12 counter's history validator (`threshold_scan.validate_history`, which `creed_selfcheck` also calls): CATO's 13 saved CW5 counterexamples + 9 ordinary cases, each run end to end in a temp copy. Read-only; exit 0 = all pass. **Run it after any edit to either script.** |
| `scripts/trepptalk_sweep.py` | **NEW 2026-09-30 (Will-approved process). MANUAL TOOL, NOT a boot step: Will declined wiring it into boot (and a WALTER hand-off) on 2026-10-01.** Run it when a session is about Trepp. Lists TreppTalk posts in a window, marked NEW/SEEN. Read-only. **Exit 0 only when all 9 listing pages fetched AND parsed usably and nothing is new; 1 = new rows; 2 = coverage incomplete or unknown, NOT a pass.** Repaired 9/30 evening (CATO RC4): v1 returned a quiet 0 on partial coverage. ⚠️ SEEN = the slug appears under `AGENTS/CREED/`, not proof of a read. |
| `scripts/test_trepptalk_sweep.py` | **NEW 2026-09-30.** Saved cases for the sweep: CATO RC4's four counterexamples plus controls (13 cases, no network). Exit 0 = all pass. **Run it after any edit to the sweep.** Falsified on the v1, which fails 9 of 13. |
| ~~`scripts/boot.py`~~ | ⛔ **RETIRED 2026-09-02 — kept for its source trail, NOT run, and must not be cited as a check that ran.** Disposition of DAEDALUS's 8/28 wiring-sweep item 3 (orphaned tool: on disk, never referenced by `CLAUDE.md`) and SCRATCH deferred item 10. **Retired rather than wired because its staleness checks key on `getmtime`**, and root `CLAUDE.md` §Data Hygiene forbids keying a **new** freshness mechanism on mtime — git sync restamps it, so it fails **FALSE-NEGATIVE** (reads FRESH after a pull). **Wiring it would have installed a known-broken freshness check into the boot path, which is worse than the orphan it was.** Every check it performed is already done, correctly keyed, at boot steps 4b / 4c / 7 / 7b. |

## Live metric layer — the workbook (built 2026-07-27)

`AGENTS/CREED/workbook/` — the quantitative spine under the prose rails. **Read `VX.tsv` at boot and run the 14-day staleness check** (recipe in `CLAUDE.md`).

| File | Role |
|---|---|
| `VX.tsv` | ⚠️ **Notes column HOT-TRUNCATED 2026-09-26 — full notes in `notes/VX_NOTES.md` (on demand, grep by vector ID; crc-stamped verbatim move).** **34-vector dashboard** across 10 categories, mapped to the Expected Signals. The heart. *(31 at build; `VX-CREED-3.04` added 2026-08-20 as the K5 root-cause fix; **`VX-CREED-3.05` added 2026-08-27 — the matured-balloon DOLLAR series, Will-approved, deliberately carrying NO BAND**; **`VX-CREED-5.03` added 2026-08-27 — the open-end-fund-gate COUNT that makes `CREED-T-06b` machine-gradeable**.)* |
| `FLOW.tsv` | 8 CRE transmission chains (legacy 6 refreshed + FLOW-07 lender withdrawal, FLOW-08 fast→slow holder migration) |
| `KB.tsv` | **93** Admiralty-scored research rows, seeded fresh (legacy 40KB KB deliberately not imported). Per-row history: the rows themselves (`Date`, `Notes`); the build-out narrative that sat here is at `archive/README_HISTORY_2026-10-30.md` §1. |
| `PREDICTIONS.tsv` | **3** open forecasts + 6 graded (`PRED-CREED-009` TRUE 2026-08-20; `PRED-CREED-003` FALSE 2026-08-27; `PRED-CREED-004` HIT + `007` MISS 2026-09-28 under WQ-304 option B — Kernel records still OPEN; `PRED-CREED-005` HIT 2026-09-29; `PRED-CREED-006` FALSE 2026-09-29) + 2 excluded (`002a` provenance; `010` PARTIAL, not scored, Will 9/29). Long notes → `notes/PREDICTIONS_NOTES.md` (rotation 9/29). CREED-set confidences, each naming its resolving instrument |
| `PREDICTIONS_SCOREBOARD.md` | Calibration surface + resolution protocol. **n=6** as of 2026-09-29 evening (4/6, mean Brier 0.279). *(Read "n=2 as of 2026-08-27" until 9/29 — two resolutions stale.)* ⚠️ **Not a calibration read.** *(At n=2, 8/27: both graded rows were priced on premises that did not hold. That finding is about those two rows, not the n=6 book.)* **Update it in the same session as the ledger row: both writes, or neither counts.** |
| `VX_HISTORY.tsv` | monthly series for the load-bearing vectors — a level is not a trend |
| `SCHEMA.tsv` | 14-column controlled vocabulary governing `KB.tsv` |
| `WORKBOOK_DESIGN.md` | design rationale + build record + the five Will-approved §10 decisions |
| `LEDGER_GLOB` | **NEW 2026-08-20.** Declares which files `scripts/ledger_staleness.py` enforces: **`workbook/*.tsv registry/*.tsv`**. ⚠️ **It exists because `registry/` had been outside ALL staleness enforcement — the exact surface class whose staleness produced K5** (a trigger that sat untrippable for 6 weeks). `THRESHOLDS.tsv` reads `FROZEN` there by design; the rest must read `ok`. |

**Canonical-truth order:** `STATUS.md` > `thesis/THESIS.md` > `research/REFRESH_*.md` > `workbook/`. If the workbook disagrees with STATUS, **STATUS is right and the workbook is stale.** Threshold bands are **frozen terms** (Will, 7/21) — propose, don't edit. Vectors `4.01` (REGINALD) and `1.03`/`6.01` (HOMER) are **shared — reference, don't fork.**

## Current analytical rails

Use these before making current CRE / CMBS claims:

- `AGENTS/CREED/research/REFRESH_2026-07-27.md` — **PRIOR pack, ON DEMAND since 2026-09-30** (not a boot read; CRE lender leg: ARI wind-down + KREF credit recognition; June SS resolved at 17.11%; life-science bifurcation; mall-cadence kill; 7/27 intraday tape)
- `AGENTS/CREED/research/REFRESH_2026-07-04.md` — superseded 7/27; retained as June-Trepp / realized-recognition-cluster source-trail
- `AGENTS/CREED/research/REFRESH_2026-06-21.md` — superseded 7/4; retained as FDIC-Q1 / maturity-wall source-trail
- `AGENTS/CREED/thesis/THESIS.md` — current thesis rails (**current state only since the 2026-09-30 split**)
- `AGENTS/CREED/thesis/THESIS_HISTORY_2026-09-30.md` — ⛔ verbatim pre-split THESIS (crc32 `42275fe2`): the reasoning trail, never current state
- `AGENTS/CREED/thesis/CHANGELOG.md` — thesis change history (boot reads the newest 3 entries only, since 2026-10-30)
- `AGENTS/CREED/research/INBOX_TRIAGE_2026-06-21.md` — stale inbox resolved against current rails (ON DEMAND since 2026-10-30)
- `AGENTS/CREED/research/REIT_EQUITY_TAPE_MODULE_2026-06-21.md` — public REIT equity-market tape module absorbed from dormant REITS
- `AGENTS/CREED/archive/LEGACY_PULL_FORWARD_2026-06-21.md` — durable mechanisms pulled from legacy CREED, with old values marked stale (ON DEMAND since 2026-10-30)

## Other live surfaces *(indexed 2026-10-30, DAEDALUS profile-refresh item 9 — these existed and were missing from this index)*

| Path | Role |
|---|---|
| `CALENDAR.md` | Dated CREED touchpoints and the PROME DOCKET L-rows CREED owns or consumes. Not a boot read; DOCKET is the authority for L-rows |
| `catchups/` + `catchups/INDEX.md` | One dated catch-up per session; INDEX marks the CURRENT one (boot step 6.1) |
| `notes/VX_NOTES.md` · `notes/FLOW_NOTES.md` · `notes/PREDICTIONS_NOTES.md` | Full verbatim notes split out of the hot TSV cells; read on demand, grep by ID. `VX_NOTES.md` also holds the full Trepp source citations (§VX-SOURCES) and the VX header history |
| `thesis/MECHANISMS.md` | The five transmission channels and their watch lists (live reference, moved out of THESIS 2026-10-30) |
| `thesis/THESIS_HISTORY_2026-10-30.md` · `thesis/CHANGELOG_HISTORY_2026-10-22.md` | ⛔ verbatim rotated history, not current |
| `registry/PREREG_2026-11_TREPP_PRINT.md` | **LIVE pre-registration for the OCTOBER 2026 Trepp print** — decides `CREED-T-01a` (leg 2) and `PRED-CREED-001`. Frozen above its line, graded below it |
| `registry/THRESHOLDS_NOTES.md` · `registry/BAND_REVISIT_2026-08-27.md` | Cold half of the threshold registry; the 8/27 band-revisit record |
| `registry/corrections_receipts.tsv` | Receipts for fleet corrections addressed to CREED (boot step 7b writes here) |
| `registry/kernel_staged/` · `registry/kernel_staged_v2/` · `kernel/` · `outbox/kernel/submissions/` | Gate C Kernel material for the three pinned predictions (001/004/007): staged drafts, native companions, and the submitted commands. ⛔ Never edit a pinned PREDICTIONS row without Will. ⚠️ `registry/kernel_staged/README.md` line 4 still says "NOTHING HERE HAS BEEN SUBMITTED"; that is stale — all 12 commands are in `outbox/kernel/submissions/`. The directory is byte-frozen, so the correction lives here (2026-10-30, DAEDALUS item 13) |
| `outbox/` | CREED's dated delivery packets to PROME (historical; current packets go straight to the recipient's `inbox/`) |
| `evals/` | CREED's own eval suite (v2, 4 cases, 4/4 PASS 2026-10-22; CREED owns the rebuild per Will 10/22) |
| `research/data/` | Machine-readable inputs behind research files (FDIC restructured-loan series; the 10/28 case-flag patch) |
| `archive/STATUS_ROTATION_2026-10-30.md` · `archive/COVERAGE_HISTORY_2026-10-30.md` | ⛔ 2026-10-30 read-cap rotations, verbatim, crc32-stamped |

## Case ledger — `cases/` *(NEW 2026-09-29, Will-directed)*

One row per named distressed CRE property/loan (`CASES.tsv`) plus dated events (`CASE_EVENTS.tsv`); rules in `cases/README.md`. **Not a boot read.** ⚠️ **It is a sample of reported cases, not of the market: pattern reads are hypotheses until tested against an aggregate.**

## Commissioned analyses — `analysis/` *(NEW 2026-09-27)*

One dated file per PROME-commissioned read, at the path the commissioning packet names. **`analysis/2026-09-27_nano-banc-collateral-read.md`**: Nano Banc failure, retained-pool composition (INFERRED), REGINALD's severity figure consumed, the FDIC-sale comp rule (DOCKET L515). Distinct from `research/` (CREED's own source packs and trails).

## Legacy / archive surfaces

**`archive/STATUS_ROTATION_2026-09-02.md` — NEW 2026-09-02.** The blocks rotated off `STATUS.md` when it measured **43,755 B = 134% of the 32,550 B read-cap budget**: the 8/27 catch-up section, the 8/27–8/28 header state bullets, the BOTTOM LINE 8/20 prior windows, and a second pass of four stale/duplicated sections plus this file's own duplicate (STATUS §Current File State). **Verbatim, each block crc32-stamped.** ⛔ **Superseded as current state — do not cite.** ⚠️ **The rotation was audited by OBLIGATION, not by bytes** (see `STATUS.md` §Standing Obligations); a byte-clean split can still delete an owed action.


Do **not** treat these as current analytical truth:

- ~~`AGENTS/CREED/inbox/2026-02-24_signals.md`~~ — removed 6/28 (triaged → `research/INBOX_TRIAGE_2026-06-21.md`; content in THESIS). Live inbox is `inbox/WALTER/`.
- `AGENTS/REGINALD/archive/sub-agents/CREED/` — legacy REGINALD sub-agent tree / source archive (moved from `sub-agents/CREED/` by REGINALD 2026-08-13, `a7bae0d06`; path corrected here 2026-10-22)
- ~~`AGENTS/REITS/`~~ — the dormant public-REIT source archive was **deleted 2026-06-30** (`fbf2569af`; recoverable from git history only). The live REIT tape belongs to CREED (`VX-7.01`, `scripts/s8a_relative.py`)

The legacy tree is useful for mechanism libraries, old source trails, and tracker design. It is not a live dashboard.

## Guardrail

No trade recommendations or current market claims from legacy Jan/Feb/March 2026 values unless they are refreshed against current primary/source data.
