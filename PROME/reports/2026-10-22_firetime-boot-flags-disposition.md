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
