# Routine release coverage — ready for activation, NOT INSTALLED

September 9 approved maintenance, audit A5. Extends the existing three routines; supersedes their fixed-UTC timing only once installed and verified. No additional monitoring program or trading authority. The current session exposes no RemoteTrigger/routine-control capability; actual remote configuration has not been read or changed. SCHEDULED_RUNS.md remains the last recorded configuration.

## Requested schedule

Use timezone **America/New_York**, preserving local times across daylight-saving changes. Cron strings below are local-time intentions, not confirmed API field names.

| Existing trigger | Desired local execution | Change |
|---|---|---|
| `trig_01DHTJWiUSVYXY9vUeto57qr` Monday | Monday 09:45 (`45 9 * * 1`) | Same local time, timezone-aware |
| `trig_014CDR4kjWtc29mYxXspGAHF` EIA | Wednesday 11:00 (`0 11 * * 3`) plus Thursday 14:15 fallback (`15 14 * * 4`) | Preserve normal early read; cover holiday/later-file publication |
| `trig_01GBVYAq5TwPc6JQ4hbfYYMe` Friday | Friday 16:15 (`15 16 * * 5`) | After usual COT publication and equity close |

If the scheduler accepts only one trigger per routine, add the Thursday trigger with the same EIA job configuration; name it EIA publication fallback, not a separate research mandate. If native timezone scheduling is unavailable, do not silently label fixed UTC as ET: document the required seasonal transition and next run times before activation. Date and publication validation below remain mandatory, including exceptional delays beyond Thursday or Friday. This proposal does not promise automatic coverage of arbitrary publisher delays.

## Exact prompt addition (all three)

> RELEASE AND OBSERVATION CONTROL — September 9 maintenance. Read the current BRENT CLAUDE, STATUS, SCHEDULED_RUNS and TRACKER registered-alert block. Files win on drift. Capture retrieval time, publisher release date and each series' observation date separately. A publication notice is not a numerical report. Before comparing or flagging a new print, verify that its observation period is the intended period and has not already been recorded in the existing data log/output. On a retry with the same observation, report NO NEW OBSERVATION and do not duplicate the observation or treat it as a new crossing. If the publisher has not released the intended period, retain prior values under their original dates, report PENDING PUBLICATION with the publisher's next stated time, and name the next owner read; no missing-data-to-clear inference. Check every required metric, report missing fields and mixed observation weeks explicitly, and do not fill a missing component from another period. Quotes require timestamps and source basis; vendor quotes are not settlements. No hardcoded trading thresholds. Record and flag only; never grade, resolve or re-mark BRT predictions, decide a gate, infer a fill, or authorize capital action. Follow current root Git Protocol and verify the full fresh-fetch push receipt, not a bare Pushed line.

## EIA-specific addition

> Wednesday is the primary release read. The Thursday fallback checks whether the required WPSR observation and later supporting files are now published; it is not permission to count another weekly observation. On September 10, 2026 require week ending September 4, with the publisher's noon/14:00 ET batches. Read the publisher's holiday schedule for each later run rather than reusing this example. Use scripts/eia_weekly.py; rc=2 means inspect missing/stale/mixed inputs, not an all-clear. Record any newly available supporting file without duplicating an already recorded core weekly print. Do not substitute retail survey dates for WPSR dates. Preserve the registered SPR two-print windows; one print cannot finish them.

## Friday-specific addition

> Verify Baker Hughes' intended report date and the CFTC raw f_disagg.txt as-of date separately. Use scripts/cot_grade.py --expect with that week's intended Tuesday observation date, verified against the publisher schedule; exit 3 means WAIT. Socrata lag does not establish a missing raw release. A 16:15 run does not prove publication, and an after-close quote does not prove an official settlement. Record the readings and flag existing registered lines; weekly rig prints are breach watches, not final BRT-26 resolutions. Tanker diagnostic window is closed after 16:00 ET; this routine cannot retroactively grade the once-at/after-14:00 owner gate.

## Installation and acceptance

1. Read each trigger's actual complete configuration and preserve a redacted before-image. Compare the current prompt with this mirror; reconcile any intervening owner changes first.
2. Apply the timing and additions above, preserving current model, repository, permissions and other job fields. The recorded RemoteTrigger update mechanism requires the **full `body.job_config.ccr` object**: never send a partial replacement assembled from this note. Verify the actual current API schema before mutating.
3. Re-fetch each changed trigger. Record ID, updated_at, effective timezone, cron(s), full prompt hash and next local/UTC run. Keep sensitive fields out of committed evidence. Update SCHEDULED_RUNS.md's live table/prompt mirror in the same pass. This pending banner changes only after those receipts exist.
4. Verify next EIA fallback September 10 at 14:15 ET and Friday September 11 at 16:15 ET. Exercise missing release, repeated observation, partial fields and intended new observation in a non-publishing preview if supported; otherwise verify on the first run and explicitly retain that acceptance item as pending. No dry-run output may be represented as an actual released observation or live-run receipt.
5. Source gaps beyond the next scheduled read remain named owner tasks. Do not implement self-rescheduling loops, external messages or additional recurring jobs beyond this bounded fallback.

Until installation, SCRATCH's explicit September 10/11 owner reads provide the work queue; this file provides no unattended execution guarantee.
