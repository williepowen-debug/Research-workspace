# BRENT — Cloud Routines Registry (off-repo prompt mirror)

**Created:** 2026-08-03 EVE by PROME (Will-authorized — BRENT idle; owner ratifies at next boot, see inbox packet same date).
**Why this file exists:** routine prompt text is stored **server-side at claude.ai/code/routines — invisible to every repo grep** (VULCAN's 8/3 diagnosis: a dead delivery path survived two repo-side flags because the regression lived in off-repo prompt text). This registry is the repo-visible mirror. **Rule: any change to a routine's prompt updates this file in the same pass, and vice versa.** Pattern source: `AGENTS/VULCAN/SCHEDULED_RUNS.md`.

## Live routines (3) — prompts refreshed 2026-08-03 by PROME (Will-approved)

| Routine ID | Name | Cron (UTC) | Local | Model | Prompt vintage |
|---|---|---|---|---|---|
| `trig_01DHTJWiUSVYXY9vUeto57qr` | BRENT Monday Market Open | `45 13 * * 1` | Mon 9:45 AM ET | claude-sonnet-5 | 2026-08-03 |
| `trig_014CDR4kjWtc29mYxXspGAHF` | BRENT Wednesday EIA | `0 15 * * 3` | Wed 11:00 AM ET | claude-sonnet-5 | 2026-08-03 |
| `trig_01GBVYAq5TwPc6JQ4hbfYYMe` | BRENT Friday Close | `0 18 * * 5` | Fri 2:00 PM ET | claude-sonnet-5 | 2026-08-03 |

## Design contract of the 2026-08-03 refresh (what the prompts now do)

1. **No hardcoded thresholds.** The April-vintage prompts carried levels that rotted in place ("rig trough ~553" vs the registered 457 line; "$4 breached April"; Phase-B/Path-B triggers; "M1-M3 Phase-2 at $3"). The refreshed prompts read **STATUS.md banners + TRACKER.md top block at run time** and apply only currently-registered lines. **Files win on drift** — that sentence is in each prompt.
2. **Retired formulations named as retired** (Friday prompt explicitly kills "declining net longs 2+ weeks" and "+50 from trough").
3. **COT = raw `f_disagg.txt` primary** (Socrata lags the 3:30 post — `finding_cftc_cot_raw_file_beats_socrata_lag`).
4. **Git = current canon**: pathspec-only, `safe-push.sh`, non-ff → `pull --rebase --autostash` + re-push, verify the literal `Pushed.` line; PROME flags go to `PROME/inbox/` (`AGENTS/PROME/` named as DEAD in each prompt).
5. **Routines record and flag, never decide** — deploy/gate actions stay with live sessions and Will.
6. Model bumped claude-sonnet-4-6 → claude-sonnet-5; WebFetch added to all three.

## Mechanics

- **Update path:** PROME session → `RemoteTrigger {action:"update", trigger_id, body.job_config}` (full `ccr` object required — partial job_config replaces whole object). Deletion is web-UI-only (claude.ai/code/routines).
- **Outputs land:** `demand_destruction/data/{monday,eia,friday}_YYYY-MM-DD.md` + TRACKER.md WEEKLY DATA LOG row, committed by the routine itself (its pushes are a known source of routine non-ff for concurrent sessions — see root Git Protocol step 3).
- **Standing audit:** quarterly routine-prompt audit row on `PROME/DOCKET.tsv` (first: 2026-11-03) — checks every live routine's prompt against this registry and current canon.

## History

- **2026-04-06:** all three created (April thesis generation).
- **2026-08-03:** PROME fleet routine audit (VULCAN's off-repo-regression class): prompts refreshed per the design contract above; this registry born. VULCAN's 3 one-shot routines confirmed fired+disabled (dead, not deleted).
