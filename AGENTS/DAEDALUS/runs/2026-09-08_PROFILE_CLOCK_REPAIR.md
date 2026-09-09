# Profile-clock repair — September 8, 2026

Completed on Will's approval of `2026-09-08_NEXT_STEPS.md`: “approved go ahead and begin.” The implementation repairs the instrument; it does not claim the underlying profiles were refreshed.

## Result and production acceptance

| Population/result | Before | After, as of September 8 |
|---|---|---|
| Files treated as profiles | 45, including seven reader reports | 38 actual named profiles, including retired YEYOU; reports/template explicitly excluded |
| Dated clocks evaluated | 24, including two report-body false matches | 29: 23 inside their declared calendar window, six overdue |
| Overdue | BROCK only, 48d based on partial Δ | BOND 71>45; BROCK 72>45; CARL 60>45; LIQUID 32>30; SAM 60>45; SHADE 72>45 |
| Cannot evaluate | none | HENRY, HOMER, OSPREY: STATUS-stamp-relative predicates, not elapsed-time clocks |
| No dated clock | 21, including missed declared clocks | Six named content/event-only profiles; never certified |
| Exit | 1 | 2, retaining all six ALERT lines; same result propagated through sweeps_due |

Evidence: `2026-09-08_PROFILE_CLOCK_BEFORE.json` preserves the old live stdout, git boundary and interpreted dates; `2026-09-08_PROFILE_CLOCK_AFTER.json` preserves every source hash and interpretation plus actual test/checker/boot-consumer stdout and exit codes. Six verbatim production profiles are frozen under `scripts/tests/fixtures/profile_clock/`, with source paths and SHA256 manifest. `python3 -B AGENTS/DAEDALUS/scripts/tests/test_profile_clock_check.py`: **12/12 PASS**. Real FERT exercises rc0, BROCK rc1, OSPREY rc2; synthetic cases additionally cover missing/malformed data, future declared vintages, strict boundaries, partial scope, mixed quiet output, encoding failure and visible exclusions.

The publisher is DAEDALUS's own profile metadata, not an external calendar. Read and verified at the source: FERT built 9/5 despite a 9/8 receipt and 9/26 deadline; OSPREY built 8/7 despite a receipt explicitly disclaiming refresh; BRENT full refresh 9/7 despite a 10/22 checkpoint; CORAL refreshed 9/5 despite a 10/5 checkpoint; CARL's author metadata follows Δ headings. These real declarations establish the premise of the repair. No network dependency or assumed market-release schedule.

## Contract and limits

`Profile vintage: YYYY-MM-DD` is the explicit whole-body declaration. Existing labeled build/body/refresh metadata remains supported. Partial Δs, receipt banners, future checkpoints, source dates and git commits do not reset the body clock. The parser reads anchored metadata across the file so a preceding Δ section cannot hide it; clock extraction reads named staleness/clock fields, not arbitrary prose mentions. Existing `45 d →`, `30-day clock`, `Day clock: 21d` and `or 21d` forms now work. Invalid or ambiguous metadata returns rc2; known other alerts remain visible. An unknown format is not certified as a day clock; NO-DATED-CLOCK remains an explicit coverage limitation.

Only OTTO received a metadata clarification, to its existing September 5 date: §§1–3/6–8 refreshed and §§4–5 expressly reverified. This is supported by the existing header and section labels, not a new September 8 review. No other profile body dates or thresholds changed. Template and UPGRADE_PROTOCOL use the same contract, paired with EVOLUTION in the same change.

**STATUS-relative predicates are intentionally unimplemented:** the old checker converted them into wall time. The new one names the needed owner-stamp comparison and refuses certification. OSPREY consequently cannot silently clear after a receipt. A content-trigger/full-refresh read remains due; receipt processing and script implementation by the owner are separate facts. The six overdue bodies already carry warning/Δ dispositions; their full review remains due at the September 15 profile sitting, with work-volume triggers considered sooner. No blanket threshold change or mass refresh was performed to make the check green.

Consumer verified: `sweeps_due.py` invokes `--quiet`, prints child stdout and propagates rc2; live run retained all six alerts and the three limitations. No other code caller of `vintage_of`/`clock_of` found in DAEDALUS scripts. CHECKS contract re-cut with its complete prior row conserved in CHECKS_HISTORY.

## Own sustain finding

The old “profile clock zero, layer closed” claim was not reliable evidence. The PROME sweep also ran September 8, one day after the registry's 21-day interval (two days after the informal September 6 plan). DAEDALUS's pre-existing L5 sustain row explicitly requires both serviced profile debt and sweeps on cadence. Neither instrument repair nor a late completed sweep proves those conditions held. The same per-leg discipline used on PROME therefore puts DAEDALUS at **L4 / confidence M** pending a clean sustain interval; the historical Will-approved September 1 promotion remains preserved in FLEET_MAP_HISTORY. This is a current assessment of standing conditions, not a rewrite of the ruling.

L3 core rubric/check operation: PASS (this repair, tests, registered sweep and file-backed grades). L3 map currency: PASS for rows touched now; wider fleet remains September 15 work. L4 executed/consumed outputs: PASS at bounded scope (September 8 receipt verification and retained prior build/consumption evidence). L4 lessons accruing: PASS (existing PAT-105/PAT-069 applied; no duplicate pattern minted). L5 cadence: FAIL at this sitting. L5 profile-health certification: FAIL for the reviewed interval; mechanism fixed, body debt still open. No other desk is regraded by the clock alone.
