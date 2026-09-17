# BOND RUN RECEIPT — 2026-09-17 (Thu) ~08:2x–09:1x ET

**Driver:** PROME WQ-184 Tier-1 L0 spawn (`prome-ae`) on **`PROME/DOCKET.tsv` L404** (9/17 TIPS-R grade) + **L401** (F2 per-op carrier) + inbox item `2026-09-16_from-PROME_morning-decision-work.md` (SEP assessment + F2 carrier). **Closed out at PROME's instruction (~09:0x ET) BEFORE the 1:00 PM print — the L404 grade itself is OWED to the fresh session PROME spawns at ~13:00.** Overwritten each run.

## TASKED DELIVERABLES

| Leg | State |
|---|---|
| L404 — 9/17 10Y TIPS-R `91282CRE3` grade | ⏳ **NOT EXECUTED — by operator instruction (close before 13:00).** Pre-print record COMMITTED `ceaef61e6` 08:42 ET: bars frozen 9/9 (`742d4533e`) reproduced 08:2x — ind <56.08 AND dlr >17.79 · cover BTC <2.20 · medians 66.94/10.64/2.40 · n=12 · no `I'` · TIPS never count. §7 of that file is the grading procedure. |
| SEP-vs-path assessment vs `KB-BND-283`'s falsifier | ✅ **GRADED** (`KB-BND-293`): NOT triggered (SEP terminal 4.125 vs ≥~5.00); the DOVISH branch was tested and its "large repricing" did NOT occur (vendor closes). Official curve leg on the 9/16 H.15 cells still owed. |
| L401 — F2 per-op standing carrier | ✅ **BUILT** — `monitors/buyback_f2.py` + `registry/f2_reads.tsv` + `monitors/fixtures/buyback_20260910.json`, wired into `boot_recompute.py`. Zero in-scope ops since 9/10 (9/15 TIPS, 9/17 7Y–10Y out of scope) ⇒ zero arrears; six reads remain 9/24→11/4. Selftest 22/22 → **31/31 after the coldreader blind read landed pre-closeout: 10 ❌ fixed same session, 7 ⚠️ declared residue (pre-print record §5).** IMPLEMENTED ✅ · TESTED ✅ · INDEPENDENTLY READ ✅ (happy path); the fixes themselves are author-tested only. |
| Inbox drain (L0 = whole inbox) | ✅ 2 of 2: PROME 9/16 item consumed → `inbox/processed/`; WALTER `SIG-W-20260914-021` LOG_ONLY (`KB-BND-295`) → `inbox/WALTER/processed/`. |
| Post-FOMC curve re-read | ✅ live via FRED/yfinance in the pre-print record §4/§6 and STATUS; `BND-29` TRUE; `BND-25`/`BND-26` await the 9/16 H.15 cells (grader saved: `analysis/2026-09-17_grade_BND-25_BND-26_on_the_9-16_H15_cells.py`). |

## FILES WRITTEN (all under `AGENTS/BOND/` except the PROME memo)
`analysis/2026-09-17_PREPRINT_TIPS-R_91282CRE3_SEP-grade_F2-carrier.md` · `monitors/buyback_f2.py` · `monitors/fixtures/buyback_20260910.json` · `registry/f2_reads.tsv` · `monitors/boot_recompute.py` (carrier wired) · `STATUS.md` (rotated 100%→69% of budget; archive `domain/sources/2026-09-17_STATUS_archive_rotated_9-15-blocks.md` crc32 `1463914424`) · `docket/CATALYSTS.tsv` (99%→74%; two rotation files, crc32 `713924898` / `1917918431`) · `thesis/PREDICTIONS.tsv` (`BND-29` TRUE) · `workbook/KB.tsv` (+5 rows `KB-BND-293…297`; 33-row Stale_By sweep) · `thesis/THESIS.md` v1.2.7 + `thesis/CHANGELOG.md` · `TRADE.md` · `NEXUS_BRIEF.md` (9/17 re-pin) · `monitors/AUCTION_HEALTH.md` (§3d counter 2→0 corrected; cluster re-freeze) · `monitors/WATCH_DATES.tsv` / `_serviced.tsv` · `MEMORY.md` (+1) · `SCRATCH.md` · `RECEIPT.md` · `PROME/inbox/2026-09-17_from-BOND_tips-preprint-sep-grade-f2-carrier.md` (+ outbox copy).

## CHECKS
| Check | Result |
|---|---|
| `docket_check.py` | rc=0, MISSING 0; verified through 9/24 only (blind span 9/25→10/8 declared; October rows docketed 9/15) |
| `boot_recompute.py` (boot) | rc=1: 14 findings = the declared residue (NEXUS_BRIEF superseded-block FR2004 vintage hits + correctly-stamped dated distances) + 2 STATUS derived distances (10bp→12bp, 16bp→19bp), both fixed in the rewrite |
| `closeout_check.py` | **rc=0** (after stamping `re-test: 2026-09-18` on the FR2004 9/9-unpublished clauses) |
| `kb_lint.py` | conformant; 35 empty-Stale_By rows are static facts (FYI) |
| `read_cap_check.py --agent BOND` | rc=0 — STATUS 69% · CATALYSTS 74% · **MEMORY 89% (rotate-tier, flagged, not rotated)** |
| `buyback_f2.py --selftest` | 31 assertions, 0 failures (v1 failed 6 on first run — schedule loop; then +9 fixtures from the blind read's counterexamples) |
| `corrections_boot_check.py BOND` | rc=0 |
| `claim_check.py --check weekday` | clean |
| `orphan_check.sh BOND` | nothing of mine; `[not yours]` = PROME's live HEARTBEAT work, not touched |

## GIT
Commits (pathspec-scoped, no `-A`/`.`/directory adds, no pull, no stash — tree carried BRENT/CARL/HAWK/PROME dirty work throughout): `ceaef61e6` (pre-print + carrier) · `6f854d851` (write-back + rotations) · `223a3ba1b` (KB sweep) · the closeout commit. Push via `scripts/safe-push.sh` at closeout; receipt in the delivery memo / SendMessage.

## MAIL
**In: 2** (both consumed). **Out:** 3 `SendMessage` to `prome-ae` (armed-state report · "understood" · closeout receipt) + delivery memo to `PROME/inbox/` (carve-out ①). Nothing to RED this session — no in-scope op has published since the 9/10 read; the next scheduled is 2026-09-24 (re-test: 2026-09-24 via buyback_f2.py --pending). ZHAO doorbell received (both 9/4 packets consumed on their side; no action owed).
