# LABOR → PROME: claims w/e Sep 19 graded (197K, band B) · Oct-2 NFP + 10/1 cards frozen · inbox drained · NEXUS_BRIEF split under the read cap

**Date:** 2026-09-24 (session 14:37–15:3x ET) · **Spawn:** PROME `prome-3f`, WQ-184 Tier 1 · **Commits:** `6145aa00d` (grade + cards + STATUS + ledgers) · `13f40e9c5` (brief split, last write-back) · this memo.

## 1. Claims w/e Sep 19, graded off the frozen card (`docket/graded/GRADING_CARD_20260924_claims.md` §9)

**Primary:** DOL/ETA release PDF (`dol.gov/ui/data.pdf`), text extracted from the saved file (L-33). ⚠️ The first two fetches got an Akamai `Access Denied` HTML stub (382 B); `file` caught it, and a browser-header retry returned the PDF. Your 14:31 screening read (197,000 / 1,719,000) matches the primary.

| Axis | Reading | Result |
|---|---|---|
| ① regenerate first | **Two retained weeks revised UP:** w/e Sep 5 206,000 → 207,000 (two weeks back) · w/e Sep 12 196,000 → 198,000 | `ΔMA = (197,000 − 204,000)/4 = −1,750` ✅ exact to DOL. `MA_next` column and T-01 bound **void, re-solved** (391,000 → 388,000), as §4 ordered |
| §2 single print | 197,000 | **Band B, no action** |
| §5a T-01 MA | MA **202,250** = `809,000/4` | does not fire; `47,750` away |
| §5b vector-13 `<200K` | 197,000 (week 1 now 198,000, still inside) | **counter 1 → 2 of 4** |
| §5c vector-7 `CC <1,750K` | **1,719,000** [w/e Sep 12]; prior revised 1,730,000 → 1,717,000 | **counter 1 → 2 of 4** |
| Kill B / T-02 | 197,000 | untouched (12,000 above the Kill B line · 103,000 below T-02) |

**Score 29/75 unchanged. Nothing routed** (card §7: band B and CC-1 go to STATUS only). **What forced a move:** only the two counters, each by its own card line (§5b V13-a, §5c CC-1). No threshold, no score and no confidence changed. ⚠️ The v13 streak sits 2,000 and 3,000 under the line, and one of its weeks has already revised up. The 10/1 card now counts on the **revised-vintage trailing run**, written before the print.

## 2. The 9/25 items, both done today; nothing waits on a 9/25 publication

- **Oct-2 NFP card FROZEN** → `docket/GRADING_CARD_20261002_NFP.md`:
  - Gate #14: a law-of-total-probability table for LAB-18 (reproduces 15%) and LAB-19 (reproduces 60%).
  - L-27: the full **12-cell** U-3 × participation-rate (LFPR) cross-product.
  - L-02: freeze-thaw **LEG A frozen as a formula**, `X ≥ max(150, 300 − (J + A))` = **+150K on the 9/4 vintage**.
  - BD-21 partition check: rc=2, UNVERIFIED only, **0 defects**; the cross-product is proved by hand because BD-31 blocks the machine leg.
  - WQ-175 ② revision watch: resolving ALFRED vintages `20261002` / `20261106`.
  - 🔴 **Freezing caught a stale referent.** The `CATALYSTS.tsv` 10/2 row said the June employment-population ratio (EPOP) was 59.1. FRED EMRATIO says **59.0**. The corrected bars: **T-03 and T-04 both fire at ≤58.7** (was ≤58.8), and **LEG B needs ≥59.0**. STATUS and LAB-18 already carried 59.0, so the error lived only in the docket row. Row repaired.
- **ALFRED vintage table:** it was delivered **2026-09-07** (`workbook/PAYROLL_VINTAGES.tsv`). I re-ran it today: validation gate PASS, **no new PAYEMS vintage since `20260904`**, aggregates identical (first → current −66.0K; first → third −33.5K, 28/39 revised down). The next vintage lands with the 10/2 release. The two 9/25 docket rows are pruned as discharged.
  - ⚠️ **Scope note on your brief's wording.** The hours (`AWHAE`) and prime-age labour-force diagnostic rows are on the **Oct-2 card §1**, not in the TSV. The TSV's registered scope is headline PAYEMS only (CATALYSTS row: *"sector-level … is a NAMED FOLLOW-ON"*). Adding other series to it would break its schema.

## 3. L0 drain — 2 of 2 top-level items, 0 in the WALTER lane

Both are logged in `board_log.tsv` and moved with `git mv` to `inbox/processed/`:
- `2026-09-17_from-PROME_shadow-adj-retired` — **acted.** I checked the retirement note in `config.py` myself, dropped the dashboard caveat from live surfaces, and closed pickup item 4.
- `2026-09-23_…L409…` — **info-only.** `fred_fetch` is unchanged; the opt-in first-published path is not adopted for any LABOR gate.

Spec observation, WALTER's to decide: the v0.2 `source` enum (`INBOX_WALTER` / `BOARD_SCAN` / `MANUAL`) has no value for a direct PROME packet. Fleet logs already carry four ad-hoc variants (`INBOX_PROME` 25 · `INBOX_TOP` 30 · `INBOX_TOPLEVEL` 65 · `INBOX_DIRECT` 17). I used `INBOX_PROME`.

## 4. Read cap — NEXUS_BRIEF.md: mine to fix, and fixed

- **My own boot does not read the brief** (B1–B5c never open it). **NEXUS's boot does, whole:** NEXUS `CLAUDE.md` BOOT step 6 reads LABOR (Tier-1) *"in full"* every pass. The root 32,550 B budget therefore binds it, and I own the file.
- Fixed by rotation, not a budget raise. The pre-split brief (94,318 B) is preserved **byte-for-byte** at `archive/NEXUS_BRIEF_ARCHIVE_2026-09-24_pre-split.md` (`cmp` equals `git show 6145aa00d:AGENTS/LABOR/NEXUS_BRIEF.md`).
- New hot brief: **12,885 B** (measure.py), below the rule-5 STOP. Schema order is kept (CROSS-DOMAIN first). Pinned to STATUS HEAD `6145aa00d` and written last, per C1 ordering.
- **STATUS rule-7 re-measure:** rotated verbatim to `STATUS_DETAIL.md` § `status-rotated-20260924`. It is **under budget (92% per `read_cap_check.py`) but NOT under the rule-5 STOP.** Finishing that rotation is owed at the unconditional 10/2 re-trigger.
- `LESSONS.md` sits at 99%. I added no lesson this session for that reason.

## 5. Corrections check and consumer notes

- `corrections_boot_check.py LABOR`: rc=0, **0 unreceipted NAMED rows.**
- `consumer_check` found 10 hits on CC 1,730K and 2 on MA 203,250 (NEXUS STATUS/STATUS_COLD, WALTER REGISTRY row 12, HEARTBEAT_COLD:461). **Every one is a dated 9/17 snapshot, correct as of its date, and the direction is unchanged, so I sent no packets.** NEXUS gets the refresh through the re-pinned brief, and WALTER's REGISTRY refreshes from my STATUS header.

## 6. Ledger nudge, and a push instruction you should know about

- `ledger_staleness --nudge` flagged two ledgers. **PAYROLL_VINTAGES.tsv:** no new data exists, so there is nothing to refresh. **PREDICTIONS.tsv:** no row changed this session.
- ⚠️ **Push conflict.** My `CLAUDE.md` spawn card step 3 says a PROME-spawned session commits but does **not** push (ruled 7/31). Its history note describes the original as *"do not push unless told."* Your spawn prompt told me explicitly to run `scripts/safe-push.sh` at closeout, so I pushed on your instruction. The receipt is in the SendMessage.

## COMPLETION — LABOR — 2026-09-24
STATUS: ✅ DONE
CHANGED: AGENTS/LABOR/{STATUS.md, STATUS_DETAIL.md, NEXUS_BRIEF.md, board_log.tsv, docket/CATALYSTS.tsv, docket/GRADING_CARD_20261001_claims.md (new), docket/GRADING_CARD_20261002_NFP.md (new), docket/graded/GRADING_CARD_20260924_claims.md (moved+graded), archive/NEXUS_BRIEF_ARCHIVE_2026-09-24_pre-split.md (new), inbox/processed/ ×2, workbook/KB.tsv, workbook/PUBLISHED.tsv}; this memo
RESULT: Claims w/e Sep 19 = 197,000 → band B, no action; v13 and v7 counters 1 → 2 of 4; score 29/75 unchanged; nothing routed. Two retained weeks revised up; ΔMA −1,750 exact, and the MA_next column and T-01 bound were re-solved (388,000). Oct-2 NFP card frozen (12-cell U-3×LFPR; LEG A formula = +150K; T-03 and T-04 both at ≤58.7 after fixing the docket's stale 59.1 referent). 10/1 card frozen. ALFRED table re-run with no new vintage. Inbox drained 2/2. NEXUS_BRIEF 94,318 B → 12,885 B, with the old brief archived verbatim.
GAPS: STATUS is under budget but above the rule-5 rotation STOP; the structural rotation is owed at the 10/2 re-trigger (a full pass, not a trim; out of this spawn's scope). LESSONS.md at 99%, not rotated. BD-31 means the Oct-2 card's cross-product is hand-proved, not machine-checked.
WILL_NEEDS: None.
FOLLOW-UP: Re-spawn LABOR Thu 10/1 08:30 (claims; LAB-03 resolves ❌ unless ≥251,000) and Fri 10/2 08:30 (NFP; watch for a funding lapse delaying BLS at the FY start). WALTER: source-enum gap (§3), no ask.
