# Intake lane — bounded comparison (CATO recommendation, run 2026-10-01 ~13:40–13:55 ET)

Requested by Will (relaying CATO `runs/2026-10-01_1400_walter-intake-direction.md`, commit 2a9930fd8 — verified on origin/master).
Effort: ~15 min of tool work, one session. No lane, collector or WALTER tool files changed.

## Finding 1 — the reviewed batch is a DEGRADED batch, reported healthy

| Date | Google News items | RSS items (FT/BBC/EIA) | liveness `newsweep.status` |
|---|---|---|---|
| 2026-09-02 … 09-29 (typical) | 88–221 | 23–38 | ok |
| **2026-09-17** | **0** | 32 | ok |
| **2026-09-30** | **0** | 35 | ok (`errors: []`) |

- Cause in code: `Research-Intake/scripts/fetch_newsweep.py` ~L112–117 wraps each Google News request in `try/except Exception: pass`; the job returns `status: ok` whatever the leg yielded.
- Live control 2026-10-01 ~13:50 ET from this machine: the `diesel-export-policy` query → HTTP 200, 100 items. Query format is not broken; the failure was runner-side on 9/17 and 9/30. **Cause UNKNOWN** (rate-limit/block is a guess, not established).
- ⇒ CATO's "34 of 35 NEW" is true of the file, but the 35 are RSS-only; the 45 targeted searches contributed nothing that day.
- WALTER's own boot health check (`intake_scan.py`) reported the lane OK on 10/01 — it reads the same status.

## Finding 2 — correction to WALTER's 10/01 brief to Will

WALTER said desks without WATCH_FOR lists can have stories "collected and never put in front of me". Too strong: `intake_scan.py` also surfaces NEW_ALERT, NEW_WATCH and DEVELOPMENT (known-entity) classes. Correct statement: those desks have incomplete TARGETED coverage; plain `NEW` items stay unsurfaced. (CATO's correction; verified at intake_scan.py L206–242.)

## Finding 3 — 9/30 RSS items that deserved triage (candidates, not demonstrated misses)

Grepped BOARD 9/20–10/01; owner desks not checked.

| Item (9/30) | Likely owner | On BOARD? |
|---|---|---|
| FT: "Strong indications" Iran involved in RAF Fairford incident (Burnham) | FALCON / HAWK | no |
| FT: Russia makes extreme threats against NATO countries over Kaliningrad | YURI / HAWK | no |
| BBC: Russia's largest attack on Ukraine energy infrastructure since spring | OSPREY | no |
| BBC: UK household energy bills, biggest rise in four years | HANS | no |
| BBC: last UK/US troops leave Iraq | FALCON | no (anchor carries the pullout) |
| FT: US oil industry says diesel prices won't normalize for a year | BRENT | covered (`-0929-014`, `-1001-015`) |

## Finding 4 — screenshot-originated stories traced (Will batches 10/01)

11 dispatched stories (`-007`…`-009`, `-012`…`-020`) searched in lane batches 9/28–9/30 + `news_seen.json`: **0 of 11 present** (the hurricane hits were unrelated stories). Most broke 9/30–10/01, so the dead 9/30 Google leg and the not-yet-landed 10/01 run explain most of the gap. **Failure point = NOT COLLECTED**, not filtered or waiting for review. One clean batch is needed before separating "never searched for" from "collector down".

## Implication for CATO's choice

Collection RELIABILITY comes before both of CATO's options (discovery review vs faster cadence): on 2 of the last 25 batches the targeted searches silently returned nothing. Re-run this comparison on the next batch with a live Google leg.

## Fixes (owners)

1. WALTER (own tool): `intake_scan.py` health → flag a news batch whose Google-labelled item count is 0 (or far below its trailing median) as DEGRADED, never OK.
2. Lane/collector (PROME-landed, Research-Intake): `fetch_newsweep.py` should count failed queries and report `status: degraded` + per-leg counts in liveness, never `ok` on a total leg failure.
