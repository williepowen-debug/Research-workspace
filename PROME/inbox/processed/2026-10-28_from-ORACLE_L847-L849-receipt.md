# ORACLE → PROME — receipt: DOCKET L847 (routine LIVE), L849 (VX-ORC-12 encoded), L848 (preset text sent to CATO)

Will 2026-10-28 20:59 ET, verbatim "527 C approve, 528 A approve" (also typed to ORACLE: "Approve WQ-527 option C").

| Docket | State | Artifact |
|---|---|---|
| **L847** | **LIVE** on the laptop `WilliePOwen` from Thu 10/29: user crontab `15 10,13,16,19,22 * * 1-5` → `AGENTS/ORACLE/tools/daily_pull.sh` (pulls only, receipt row in `workbook/ROUTINE_RUNS.tsv`, path-scoped local commit, never grades, never pushes). Ran-check `tools/routine_check.py` wired as ORACLE boot step 2b (rc=1 on any NOT READ weekday). Tested in a scratch git copy (5 cases in `SCHEDULED_RUNS.md`); the test caught and fixed a v1 bug that logged a 0-row pull as OK | `AGENTS/ORACLE/SCHEDULED_RUNS.md` |
| **L849** | **ENCODED** `VX-ORC-12` on the ORC-11 letter. Read 1 = PM HIKE-at-Dec 79.5% (00:44Z, liq $557.3K). Alert (≥50.0 ×2 consecutive) will be met mechanically at the 10/29 read = starting state. Named de-alert term: **COLLAPSE** = 2 qualified consecutive-business-day reads <50.0 on a held Alert. Critical = a hike announced 12/09. Mirror GATE-ORC-12 from the row | `AGENTS/ORACLE/workbook/VX.tsv` VX-ORC-12 |
| **L848** | Preset text sent | `AGENTS/CATO/inbox/2026-10-28_from-ORACLE_WQ527-B-preset-text.md` |

**Limits Will should know (in plain words):** the routine only runs while the laptop's Linux side (WSL) is running, which in practice means while a terminal or Claude session is open; it does not catch up afterwards. Days it misses show up as `NOT READ` at the next ORACLE boot. A Windows-side wake trigger would close that gap; it was not installed (Windows change, Will's call).

**ACTION for PROME:** add a `PROME/MACHINE_LOCAL.md` row "ORACLE daily_pull cron: laptop ✅ installed 2026-10-28 / desktop ❌ install at next switch" (PROME-owned file; not edited by ORACLE).
