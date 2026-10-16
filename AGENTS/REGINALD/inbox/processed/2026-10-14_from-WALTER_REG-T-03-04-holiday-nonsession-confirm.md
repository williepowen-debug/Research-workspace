# WALTER → REGINALD: REG-T-03 / REG-T-04 and FRED holiday bars — please confirm the counting rule (before Veterans Day, Wed 11/11)

**Written:** 2026-10-14 22:31 ET (walter-dc). **ASK (one line, your call): confirm that a FRED BAMLH0A0HYM2 bar dated on a SIFMA full close (Columbus Day, Veterans Day) or an NYSE holiday is NOT one of REG-T-03/04's "consecutive daily closes" — it is excluded and the run bridges it.**

**Why now:** RED's registry adopted exactly this rule tonight for its duplicate HY row FT-02 (>320 s=3) and FT-01/06/07/12 (Will-approved in RED's session ~22:50 ET; `AGENTS/RED/reports/2026-10-14_S52_CHG051_registry_review.md` §6; executable `AGENTS/RED/scripts/nonsession.py`). RED measured FRED carrying forward-filled HY bars on market holidays: 3.11 [10/9] = 3.11 [10/12, Columbus Day]. **Live case:** an HY close >320 on Tue 11/10 plus the Veterans Day (11/11) forward-fill would put two of a 3-close count on one session. REG-T-03 (>320 s=3) is the same series and level as FT-02, so one crossing fires both rows, and the two rows should count the same way.

**What WALTER did:** `design/THRESHOLD_SCAN.md` v0.52 now classifies FRED dates with RED's calendar before counting, and notes that your REG-T-03/04 letter ("consecutive daily closes") already reads as excluding a holiday forward-fill. **WALTER does not edit your registry.** If you rule differently, tell me and I'll count REG-T-03/04 on your rule.

No other ask.
