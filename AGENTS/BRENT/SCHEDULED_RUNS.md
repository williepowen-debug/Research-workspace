# BRENT — Cloud Routines Registry (off-repo prompt mirror)

> **✅ October 28 state — L526 BOOT PREAMBLE INSTALLED LIVE (WQ-510 A; Will 2026-10-28 20:46 ET, "510 A approve"; DOCKET L526).** BRENT updated all four live routines with `RemoteTrigger update` at 2026-10-29 03:45:52–03:46:52Z (23:45–23:46 ET October 28). Each returned HTTP 200 with a new `updated_at`. Live prompt = the saved October 4 after-image with the L526 block inserted after paragraph 1; new saved images and sha256 values are in the table below. **Pre-install live read, same session: Monday and Thursday still carried the October 2 text (legacy `pull --rebase --autostash` and bare `Pushed.` receipt), so the October 4 saved correction had never reached the scheduler. It is live now as part of this install.** Wednesday and Friday were not re-read before replacement; their after-state is fully known. Thursday `mcp_connections: []` was ignored by the API again, so six account connectors remain attached and removal is still a Will UI action. Validation run and receipt: [install report](audits/2026-10-28_L526-preamble-install/REPORT.md).

> **September9 operator decision: retain the existing Claude routines.** Saved reports remain usable by BRENT in the actual approved runtime; provider/model names do not establish tools. No scheduler migration or routine-model change selected. The timing/publication repair was installed10/2; the10/4 saved-prompt correction remains unverified on the live scheduler.
> **October14 review:** all four saved prompt SHA256s below reproduce, with no retired local autostash recipe. Current OpenAI Codex callable-tool inventory exposes no routine/RemoteTrigger/browser tool; installed `claude --help` exposes no routine command. Live config/export/update therefore remains UNVERIFIED, not repaired by this document. Historical normal-run targets below are elapsed where dated; October14/15 is the existing holiday pair, not a newly scheduled job. No October12Monday or October14Wednesday output found in the inspected report lane; absence of a saved report does not establish remote-run failure. [Capability/hash receipt](audits/2026-10-14_operational-followups/routine-review.json). Existing exact UI/export handoff below remains the concrete remaining step; no extra run or scheduler migration created.

> ✅ **INSTALLED 2026-10-02 17:28 ET by BRENT (Will: 9/9 operator decision + 10/2 "Install now")** — the 9/9 timing/publication repair ([plan](audits/2026-09-09_maintenance/ROUTINE_UPDATE.md)) with two refreshes: the Sept-10 EIA example replaced by the Columbus Day week (WPSR wk-10/9 publishes Thu 10/15 12:00 ET), and the Friday BRT-26 / rig-line wording replaced by "BRT-26 RESOLVED 9/25, rig line RETIRED". Before-images + after-images: [`audits/2026-10-02_routine-install/`](audits/2026-10-02_routine-install/). Historical install receipts: Mon updated_at 21:27:04Z, next 10/05 13:45Z · Wed 21:27:24Z, next 10/07 15:04Z · Fri cron `15 20 * * 5`, 21:26:44Z, next **10/09 20:15Z** · Thu fallback CREATED `trig_01ALYRXtjDGbfHeubqdvyJdf` 21:27:46Z, next **10/08 18:15Z**.
> **LIVE DEPLOYMENT FOLLOW-UP 2026-10-04 23:02 ET — prompt half RESOLVED 2026-10-28 by the RemoteTrigger install above; Thursday connector half still open.** October 4 finding, kept as history: Rechecked from commit `7a3829487`: no callable Claude routine/RemoteTrigger list-get-update-export tool; `claude` CLI has no routines command and its MCP inventory has no routine server. No live object was readable or changed. Exact four-ID manual handoff, full prompt hashes, connector removal and acceptance criteria: [correction report § live-deployment follow-up](audits/2026-10-04_cato-correction/REPORT.md#live-deployment-follow-up--2026-10-04-2302-et).
> **SAVED-PROMPT CORRECTION 2026-10-04 — LIVE SINCE 2026-10-28 (inside the L526 install).** All four saved after-images contain only the root Git protocol (no legacy `pull --rebase --autostash` / bare-`Pushed.` block). Thursday reports `NO NEW CORE OBSERVATION` but continues through later supporting-file checks. **Remaining Will action:** at `claude.ai/code/routines`, open the Thursday routine (`trig_01ALYRXtjDGbfHeubqdvyJdf`), remove Gmail, Claude_Docs, Google_Drive, Quartr, Claude_Code_Remote and Canva under connectors/integrations, save, reopen and confirm the six connectors are absent. Prompt replacement is no longer needed.
> ⚠️ **NO TIMEZONE FIELD — crons are fixed UTC.** On **Sun 2026-11-01** (EST) re-set all four +1h UTC (`45 14 * * 1`, `0 16 * * 3`, `15 19 * * 4`, `15 21 * * 5`), or Friday drifts to 15:15 ET — BEFORE the COT post. Registered: CATALYSTS 2026-11-01.
> ⚠️ **Connector evidence 2026-10-28 (live read before install and post-write echo):** Thursday still has 6 account connectors (Gmail, Claude_Docs, Google_Drive, Quartr, Claude_Code_Remote, Canva); the other three have none. A second `mcp_connections: []` update on October 28 was ignored by the API, as on October 2. Removal remains the Will UI action above.
> 🧪 **Acceptance is judged only on runs that fired after 2026-10-29 03:46Z;** earlier runs executed the October 2 text. L526 AC1–AC4 are checked by an independent reader on the first two runs after install, alongside the October 2 release-control checks. Validation run and next normal runs: [install report](audits/2026-10-28_L526-preamble-install/REPORT.md).
>
> **September 9 maintenance — ~~READY, NOT INSTALLED~~ INSTALLED 2026-10-02 (see above):** [exact timing/prompt update and acceptance checks](audits/2026-09-09_maintenance/ROUTINE_UPDATE.md). The 10/04 saved-prompt corrections went live 2026-10-28 inside the L526 install.

> **Audit note 2026-09-08 — source timing, not a remote schedule change:** the mirrored Wednesday 11:00 ET run precedes this week’s WPSR release (Thursday September 10 noon ET). Treat any Wednesday output as pre-release; arrange the owner read after publication. The mirrored Friday 14:00 ET run also precedes COT ~15:30 ET, so it cannot by itself capture the new Friday COT print. Server-side settings were not inspected or changed. [Audit A11](audits/2026-09-08_stale-intel/REPORT.md).


**Created:** 2026-08-03 EVE by PROME (Will-authorized — BRENT idle; owner ratifies at next boot, see inbox packet same date).
**Why this file exists:** routine prompt text is stored **server-side at claude.ai/code/routines — invisible to every repo grep** (VULCAN's 8/3 diagnosis: a dead delivery path survived two repo-side flags because the regression lived in off-repo prompt text). This registry is the repo-visible mirror. **Rule: any change to a routine's prompt updates this file in the same pass, and vice versa.** Pattern source: `AGENTS/VULCAN/SCHEDULED_RUNS.md`.

## Live routines (4) — prompts refreshed 2026-08-03 by PROME (Will-approved); release control installed 2026-10-02 by BRENT (Will-approved); L526 boot preamble installed 2026-10-28 by BRENT (WQ-510 A)

| Routine ID | Name | Cron (UTC) | Local (EDT; +1h UTC from 11/1) | Model | Prompt vintage |
|---|---|---|---|---|---|
| `trig_01DHTJWiUSVYXY9vUeto57qr` | BRENT Monday Market Open | `45 13 * * 1` | Mon 9:45 AM ET | claude-sonnet-5 | L526 install 2026-10-28: saved `audits/2026-10-28_L526-preamble-install/after_monday.txt` (sha256 `0867c63866fc7974`); live `updated_at` 2026-10-29T03:45:52Z |
| `trig_014CDR4kjWtc29mYxXspGAHF` | BRENT Wednesday EIA | `0 15 * * 3` | Wed 11:00 AM ET | claude-sonnet-5 | L526 install 2026-10-28: saved `audits/2026-10-28_L526-preamble-install/after_wednesday.txt` (sha256 `93d70c2c5b9b50f0`); live `updated_at` 2026-10-29T03:46:16Z |
| `trig_01ALYRXtjDGbfHeubqdvyJdf` | BRENT Thursday EIA fallback | `15 18 * * 4` | Thu 2:15 PM ET | claude-sonnet-5 | L526 install 2026-10-28: saved `audits/2026-10-28_L526-preamble-install/after_thursday.txt` (sha256 `724c136490a57aac`); live `updated_at` 2026-10-29T03:46:34Z — CREATED 10/02 |
| `trig_01GBVYAq5TwPc6JQ4hbfYYMe` | BRENT Friday Close | `15 20 * * 5` (was `0 18 * * 5`) | Fri 4:15 PM ET | claude-sonnet-5 | L526 install 2026-10-28: saved `audits/2026-10-28_L526-preamble-install/after_friday.txt` (sha256 `ba09a99c3450dd8d`); live `updated_at` 2026-10-29T03:46:52Z |

**2026-08-04 amendment (PROME, executing BRENT's own ratification-packet request §4 — same-pass mirror per this file's rule):** all three prompts extended with the prediction-row fence: *"Never grade, resolve, or re-mark a BRT-xx prediction row (e.g. BRT-26, BRT-29): report the reading and flag it — resolution happens ONLY in a live BRENT session; a routine 'helpfully' resolving one corrupts the calibration record, and calibration damage is not repairable after the fact."* Friday additionally carries the BRT-26 specific: *no weekly Baker Hughes print is a resolution date — every print is a breach-WATCH.* Header stamps bumped in all three prompts; API updates verified HTTP 200 at 19:13Z, `updated_at` confirmed on each. No other prompt text changed.

## Design contract of the 2026-08-03 refresh (what the prompts now do)

1. **No hardcoded thresholds.** The April-vintage prompts carried levels that rotted in place ("rig trough ~553" vs the registered 457 line; "$4 breached April"; Phase-B/Path-B triggers; "M1-M3 Phase-2 at $3"). The refreshed prompts read **STATUS.md banners + TRACKER.md top block at run time** and apply only currently-registered lines. **Files win on drift** — that sentence is in each prompt.
2. **Retired formulations named as retired** (Friday prompt explicitly kills "declining net longs 2+ weeks" and "+50 from trough").
3. **COT = raw `f_disagg.txt` primary** (Socrata lags the 3:30 post — `finding_cftc_cot_raw_file_beats_socrata_lag`).
4. **Git = current root canon**: prompts defer to root `CLAUDE.md` and require the full fresh-fetch receipt `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).` The retired local recovery recipe and bare `Pushed.` receipt do not appear in the corrected saved prompts; PROME flags go to `PROME/inbox/` (`AGENTS/PROME/` is dead).
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
- It carried **`CUSHING −273K → ~19.10M`** — a figure I had **already retracted on 8/3**. Canonical is **18.60M (−0.77M WoW)**, re-verified today at the EIA v2 primary (`W_EPC0_SAX_YCUOK_MBBL` = 18,599 kbbl). The retraction landed in `demand_destruction/data/monday_2026-08-03.md` and **never reached the surface the automated run reads.**
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
