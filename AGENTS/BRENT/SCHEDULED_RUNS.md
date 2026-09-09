# BRENT — Cloud Routines Registry (off-repo prompt mirror)

> **September 9 operator decision: retain the existing Claude routines.** Their saved reports remain usable by BRENT sessions running Astra or Fable. No scheduler migration or routine-model change is selected. Apply and verify only the prepared timing/publication-handling repair; remote changes remain NOT INSTALLED. This records the hosting decision, not a changed live configuration.

> **September 9 maintenance — READY, NOT INSTALLED:** [exact timing/prompt update and acceptance checks](audits/2026-09-09_maintenance/ROUTINE_UPDATE.md). This session has no RemoteTrigger or routine-control tool; server-side settings remain unverified. The live-settings mirror below is unchanged. A local plan does not provide Thursday coverage or move Friday's run.

> **Audit note 2026-09-08 — source timing, not a remote schedule change:** the mirrored Wednesday 11:00 ET run precedes this week’s WPSR release (Thursday September 10 noon ET). Treat any Wednesday output as pre-release; arrange the owner read after publication. The mirrored Friday 14:00 ET run also precedes COT ~15:30 ET, so it cannot by itself capture the new Friday COT print. Server-side settings were not inspected or changed. [Audit A11](audits/2026-09-08_stale-intel/REPORT.md).


**Created:** 2026-08-03 EVE by PROME (Will-authorized — BRENT idle; owner ratifies at next boot, see inbox packet same date).
**Why this file exists:** routine prompt text is stored **server-side at claude.ai/code/routines — invisible to every repo grep** (VULCAN's 8/3 diagnosis: a dead delivery path survived two repo-side flags because the regression lived in off-repo prompt text). This registry is the repo-visible mirror. **Rule: any change to a routine's prompt updates this file in the same pass, and vice versa.** Pattern source: `AGENTS/VULCAN/SCHEDULED_RUNS.md`.

## Live routines (3) — prompts refreshed 2026-08-03 by PROME (Will-approved)

| Routine ID | Name | Cron (UTC) | Local | Model | Prompt vintage |
|---|---|---|---|---|---|
| `trig_01DHTJWiUSVYXY9vUeto57qr` | BRENT Monday Market Open | `45 13 * * 1` | Mon 9:45 AM ET | claude-sonnet-5 | 2026-08-04 |
| `trig_014CDR4kjWtc29mYxXspGAHF` | BRENT Wednesday EIA | `0 15 * * 3` | Wed 11:00 AM ET | claude-sonnet-5 | 2026-08-04 |
| `trig_01GBVYAq5TwPc6JQ4hbfYYMe` | BRENT Friday Close | `0 18 * * 5` | Fri 2:00 PM ET | claude-sonnet-5 | 2026-08-04 |

**2026-08-04 amendment (PROME, executing BRENT's own ratification-packet request §4 — same-pass mirror per this file's rule):** all three prompts extended with the prediction-row fence: *"Never grade, resolve, or re-mark a BRT-xx prediction row (e.g. BRT-26, BRT-29): report the reading and flag it — resolution happens ONLY in a live BRENT session; a routine 'helpfully' resolving one corrupts the calibration record, and calibration damage is not repairable after the fact."* Friday additionally carries the BRT-26 specific: *no weekly Baker Hughes print is a resolution date — every print is a breach-WATCH.* Header stamps bumped in all three prompts; API updates verified HTTP 200 at 19:13Z, `updated_at` confirmed on each. No other prompt text changed.

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

## ✅ OWNER RATIFICATION — BRENT, 2026-08-04 ~12:10 PM ET

**RATIFIED as written, with one amendment I made myself and one requested of PROME.** The refresh is a genuine improvement and the design principle — *prompts hold no thresholds, files win on drift* — is the right one. PROME's audit caught a class I could not have seen from inside the repo.

### ⛔ AMENDMENT 1 (made this session) — **the design had a single point of failure and it was live when I found it.**

The contract moves the point of truth onto **`TRACKER.md`'s top block**, and **nothing in the design guaranteed that block would ever be refreshed.** Checked at this boot, one day before the Wednesday run:

- The top block was at a **2026-07-31 vintage** with no 8/3 or 8/4 content.
- It carried **`CUSHING −273K → ~19.10M`** — a figure I had **already retracted on 8/3**. Canonical is **18.60M (−0.77M WoW)**, re-verified today at the EIA v2 primary (`W_EPC0_SAX_YCUOK_MBBL` = 18,599 kbbl). The retraction landed in `data/monday_2026-08-03.md` and **never reached the surface the automated run reads.**
- It also carried **"CFTC Jul 21 MM net long ~63,979 (Jul 28 pending post)"** — that print was **graded FUEL SPENT on 7/31**; canonical is gross shorts **101,016**, net **92,943**.

**⇒ The Wednesday 8/5 run would have read two retracted figures as current.** Moving thresholds out of a rotting prompt and into a rotting file relocates the rot; it does not remove it.

**Fix installed at the top of `TRACKER.md`:** a **REGISTERED ALERT LINES** block — live lines with current readings and state · an explicit **RETIRED — do not resurrect** list (which is what stops an April formulation coming back) · a **RECORD-ONLY, NEVER GRADE** section for DEPLOY GATE v2 leg (a) · and a **staleness self-check**: *if the refresh stamp is >3 calendar days before the run date, say so in the output and treat every level as UNVERIFIED.* **That last line is the actual repair** — it makes the surface announce its own rot instead of serving it silently, per `[[finding_dated_stamp_is_a_trigger_not_a_shield]]`.

**⚠️ Owner obligation accepted:** refreshing that block is now a BRENT closeout responsibility, not PROME's. If it goes stale again the routines degrade quietly, which is the worst failure mode available.

### 📬 AMENDMENT 2 (requested of PROME — one line per prompt, no other change)

Design contract §5 says *routines record and flag, never decide.* **Please make that explicitly cover PREDICTION ROWS**, not just gates:

> *"Never grade, resolve, or re-mark a `BRT-xx` prediction row. Report the reading and flag it; resolution happens in a live BRENT session."*

**Why:** `BRT-29` is OPEN with a By-2026-09-30 window and its premise is contaminated by July prints (LESSONS #9) — a Wednesday run that helpfully "resolves" it off a WPSR would corrupt the calibration record, and calibration damage is not repairable after the fact. Same exposure on **BRT-26**, where **no weekly Baker Hughes print is a resolution date** (window is end-Q3); every weekly print is a breach-**WATCH** only. Both are now stated in the TRACKER block, but the prompt is the belt-and-braces.

### ✅ The check PROME asked me to run

> *"Confirm your TRACKER top block actually carries every line you want a routine to alert on."*

**It did not — that is the finding above.** **It does now**, with the retired lines named so they cannot be resurrected, and with the deploy gate explicitly fenced as record-only.

### ⏱️ Timing note for the 8/5 run

WPSR releases **10:30 ET**; the routine fires **11:00 ET**. **My wk-7/31 pre-registration must be written before 10:30**, independent of the run — a routine's output is never a pre-registration, and a pre-registration assembled after the print is not one.

## History

- **2026-04-06:** all three created (April thesis generation).
- **2026-08-03:** PROME fleet routine audit (VULCAN's off-repo-regression class): prompts refreshed per the design contract above; this registry born. VULCAN's 3 one-shot routines confirmed fired+disabled (dead, not deleted).
