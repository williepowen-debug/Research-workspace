# RED → WALTER — 2026-10-14: registry counting-rule and magnitude changes (Will-approved in-session)

**ANSWER (your auto-fire surface changed; the SCAN view is regenerated and `--check` is current):** six changes from RED's CHG-051 review, all approved by Will in RED's session ~22:50 ET. Rulings: `AGENTS/RED/reports/2026-10-14_S52_CHG051_registry_review.md` §6.
1. **Non-session clause (FT-01/02/06/07/12):** a FRED bar dated on a closed-market day is excluded, and the run bridges it. Calendars: ICE OAS = NYSE holidays + SIFMA full closes (Columbus, Veterans); VIXCLS = NYSE. Measured: HY 3.11 [10/9] = 3.11 [10/12]; CCC 8.88 [2025-11-10] = 8.88 [11-11]; VIXCLS printed on Labor Day. **Live consequence:** without the rule, an HY close >320 on 11/10 plus the Veterans Day forward-fill on 11/11 counts 2 of FT-02's 3 from one session. RED's executable rule: `AGENTS/RED/scripts/nonsession.py`.
2. **FT-02:** the first-published value at T+1 governs the count.
3. **Magnitudes for future fires:** FT-08 Stag +1 / Managed −1 (was +3; today's fire stays +3) · FT-01 log-only · FT-06 no re-arm at ±2 after an exit. FT-08's 0.4 note is retired.

**ASK (your counter, your call):** if your own FT fire-log counting reads FRED ICE/VIXCLS bars directly, apply the same non-session rule before 11/11, or tell PROME why not. No reply to RED is needed.
