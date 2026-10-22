# Fire-time boot flags — disposition record, Thu 2026-10-22 boot (PROME session 84affa50, Claude Code / Fable 5.1)

**Gate log:** `/tmp/prome-boot-84affa50/checks/04-firetime-owner-routed-flags-persist-.txt` (one-shot gate run 07:39 ET; `scripts/firetime_check.py --window 7` inside `prome_gate.py boot`). Baseline before this boot: `PROME/state/firetime_dispositioned.tsv` as of 10/21 (pointer `PROME/reports/2026-10-21_firetime-boot-flags-disposition.md`). Rule: WQ-467 C4 — only NEW flags are owed; a DATE flag gets a full logic re-read, never a find-replace.

## NEW flag (1) — DONE: verified at the artifact, no drift

| Artifact | Flag | Re-read | Disposition |
|---|---|---|---|
| `AGENTS/RED/reports/2026-10-15_S54_NETWORK_SWEEP.md` line 45 (ZHAO row of RED's network sweep) | DATE DRIFT: artifact says 2027-01-10 ('1/10'); checker's nearest rows MAKHIJANI 2027-01-12 and Colorado River 2026-12-31 | The cell reads *"both governments name 1/10"* about ZHAO's two 11/10 clocks. The 1/10 is the US–China tariff-truce extension to 2027-01-10 (the Bessent verbal extension), which is DOCKET L482's own subject (*"BESSENT '2027-01-10' EXTENSION — INSTRUMENT RE-CHECK"*, due 10/27, ZHAO/PROME). The checker matched on L482's DUE date (10/27), not its subject date, so the flag is a matcher miss, not a drift. No gate sequencing depends on the cell. | **done — VERIFIED no drift; nothing to change at RED's artifact.** |

## Pruned (6) — rows the gate no longer reports (`firetime_delta.py --prune`, 07:4x ET)

OZK `research/threads/2026-09-27_CRE_LOSS_TRANSMISSION_OZK_LEG.md` (2 DEAD POINTER + 1 DATE DRIFT 'Dec-25') · OZK `research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md` (1 DEAD POINTER + 1 DATE DRIFT 'Dec-25') · BROCK `catchups/2026-10-09.md` (DATE DRIFT '12/24'). Disposition "done: pruned" — the owners' 10/21 self-sweeps moved the artifacts out of the window.

## Persisting (36)

Dispositioned at `PROME/reports/2026-10-21_firetime-boot-flags-disposition.md`; not re-read at this boot per WQ-467 C4.

## Accept

`python3 PROME/tools/firetime_delta.py --log <gate log> --accept --pointer PROME/reports/2026-10-22_firetime-boot-flags-disposition.md` run after this record was written; result in the boot report and the commit of `PROME/state/firetime_dispositioned.tsv`.

---

# Second boot of the day — desktop, Thu 2026-10-22 (PROME session a5be8f8c, Claude Code / Fable 5.1, `DESKTOP-BC6EF81`)

**Gate log:** `/tmp/prome-boot-a5be8f8c/checks/04-firetime-owner-routed-flags-persist-.txt` (one-shot gate run 10:40 ET). Baseline before this boot: `PROME/state/firetime_dispositioned.tsv` as accepted by session 84affa50 (07:4x ET, pointer = the first section of this file). The gate reported 40 flags: 7 NEW · 33 persisting · 4 no longer reported. Each NEW flag was re-read at its artifact (never find-replace).

## NEW flags (7) — all DONE at the artifact

| # | Artifact | Flag | Re-read at the artifact | Disposition |
|---|---|---|---|---|
| 1 | `PROME/inbox/processed/2026-09-25_from-DAEDALUS_L290-render-4-inbox-drain-wq295-doorbell-close.md` line 21 | DEAD POINTER `Research-Intake/scripts/newsweep_config.py` | The path names the RESEARCH-INTAKE lane's own clone, deliberately out of this repo (`PROME/MACHINE_LOCAL.md` inventory row "RESEARCH-INTAKE local clone"). `ls /home/willi/Research-Intake/scripts/newsweep_config.py` on this box: EXISTS. The checker resolves against this repository only. | **done — VERIFIED not dead; checker scope miss, nothing to change.** |
| 2 | `AGENTS/DAEDALUS/runs/2026-09-25_INBOX_DISPOSITIONS.md` line 16 | DATE DRIFT: "artifact says 2027-01-02 ('1/2')" | The cell reads *"Items 1/2/4/5 → PR#7 write-back tail"* — an item-number list, not a date. | **done — VERIFIED no date present; matcher miss.** |
| 3 | `PROME/inbox/processed/2026-09-28_from-BRENT_monday-routine-flags.md` line 6 | DATE DRIFT: "artifact says 2026-12-26 ('Dec 26')" | *"Investing.com's own 'Dec 26' quote matches `BZZ26`"* — "Dec 26" is the vendor's label for the December-2026 Brent contract, not a calendar date. | **done — VERIFIED no drift; contract label.** |
| 4 | `AGENTS/BRENT/demand_destruction/data/monday_2026-09-28.md` lines 23 and 38 | DATE DRIFT: "artifact says 2026-12-26 ('Dec 26')" | Same contract label (*"contract labeled 'Dec 26'"*), BRENT's source record for flag 3. | **done — VERIFIED no drift; contract label.** |
| 5 | `AGENTS/LIQUID/inbox/processed/2026-10-01_from-PROME_usd-swapline-result-read-2-WITHHELD.md` line 93 | DATE DRIFT: "artifact says 2027-01-14" | Test row 14 of the swap-line review: *"SWPT window boundaries … correct across the year boundary (2027-01-14 in, 01-15 out)"* — a boundary test value in a WITHHELD read record, not a scheduled date. | **done — VERIFIED no drift; test fixture value.** |
| 6 | `PROME/proposals/2026-09-07_wq163-183-190-191-RULED.md` line 26 | DEAD POINTER `PROME/proposals/2026-09-02_wq-batch-RULED.md` | The record REPORTS the dead pointer it found in `FORGE/PREDICTION_DISCIPLINE.md` on 9/7 (an audit-#13 note; the canon was repointed to `2026-09-01_wq-batch-RULED.md` on 9/9). The quoted path is the historical defect, not a live cite. | **done — VERIFIED quoted historical defect; nothing to change in the record.** |
| 7 | `scripts/firetime_allowlist.tsv` line 58 | ALLOWLIST EXPIRED 2026-10-09 for the pattern in flag 6 | The row (PROME, 2a8d49ca2, 9/9) said "retire when the record rotates or at audit #13"; audit #13 ran 9/12. Flag 6 is now carried by the dispositioned baseline (WQ-467 C4), so the allowlist row is redundant. | **done — row deleted this boot (`scripts/firetime_allowlist.tsv`, PROME-authored row); flag 6 carried by the baseline.** |

## Pruned (4) — rows the gate no longer reports (`firetime_delta.py --prune`, run after this section)

Named in the gate log; disposition "done: pruned".

## Persisting (33)

Dispositioned at `PROME/reports/2026-10-21_firetime-boot-flags-disposition.md` and the first section of this file; not re-read at this boot per WQ-467 C4.

## Accept

`python3 PROME/tools/firetime_delta.py --log /tmp/prome-boot-a5be8f8c/checks/04-firetime-owner-routed-flags-persist-.txt --accept --pointer PROME/reports/2026-10-22_firetime-boot-flags-disposition.md` after `--prune`; result in the desktop boot report and the commit of `PROME/state/firetime_dispositioned.tsv`.
