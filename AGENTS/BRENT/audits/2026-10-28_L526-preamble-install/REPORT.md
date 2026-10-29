# L526 routine boot preamble — live install receipt (WQ-510 A)

**Authority:** Will, 2026-10-28 20:46 ET, verbatim "510 A approve", relayed at the artifact by PROME (`inbox/processed/2026-10-28_from-PROME_WQ510-RULED-A-install-routine-preamble.md`). Scope: install the 10/23 draft (`setups/2026-10-23_L526_routine-boot-preamble-DRAFT.md`, 02156ded7) into all four saved prompts, plus `scripts/routine-requirements.txt`, with the draft's two stated departures. Then validate one live run and report to PROME citing L526. PROME's packet also put trying RemoteTrigger for the October 4 live-prompt reconciliation within BRENT's scope. Nothing else: no money, external send or authority change.

**Installed by:** BRENT live session, 2026-10-28 23:45–23:46 ET, via the `RemoteTrigger` tool. This is the first BRENT session where that tool was exposed; the October 4 and October 14 reviews found none.

## 1. What the live routines held before the install (read in this session)

| Routine | Live prompt before | Evidence |
|---|---|---|
| Monday `trig_01DHTJWiUSVYXY9vUeto57qr` | **October 2 text.** Contains the legacy GIT block (`git pull --rebase --autostash` … "Confirm the literal 'Pushed.' line") that the October 4 correction removed | `get`, `updated_at` 2026-10-02T21:27:04Z; last run 10/26 SUCCEEDED |
| Thursday `trig_01ALYRXtjDGbfHeubqdvyJdf` | **October 2 text** (same legacy block; the old "report NO NEW OBSERVATION and stop" opening). **Six account connectors attached** (Gmail, Claude_Docs, Google_Drive, Quartr, Claude_Code_Remote, Canva) | `get`, `updated_at` 2026-10-02T21:27:53Z; last run 10/22 SUCCEEDED |
| Wednesday, Friday | Not re-read before replacement. Their replacement text is fully known (below) | — |

**Finding:** the October 4 saved-prompt correction never reached the scheduler. From October 4 to October 28 the routines ran the October 2 prompts, including the retired autostash recovery and the bare `Pushed.` receipt. Saved run outputs from that period were produced under that text.

## 2. What was installed

Each new prompt is the saved October 4 after-image (`../2026-10-02_routine-install/after_<day>.txt`, sha256 prefixes 0ef41c90ae9d270e / 7661136cc643482b / 0ff0bf2627d1e8ef / 68e0cd26f0f8952c, re-verified this session) with the draft's fenced block inserted as a new paragraph after paragraph 1. `<date>` was filled as 2026-10-28; nothing else differs from the draft (asserted by script before writing). Saved images are in this folder; the routine receives the file text without its final newline, the convention of the October 2 install.

| Routine | New saved image | sha256 (file) | Bytes | `updated_at` after | Next run |
|---|---|---|---|---|---|
| Monday | `after_monday.txt` | `0867c63866fc7974…` | 4,959 | 2026-10-29T03:45:52Z | 2026-11-02T13:45Z |
| Wednesday | `after_wednesday.txt` | `93d70c2c5b9b50f0…` | 5,780 | 2026-10-29T03:46:16Z | 2026-11-04T15:08Z |
| Thursday | `after_thursday.txt` | `724c136490a57aac…` | 6,122 | 2026-10-29T03:46:34Z | 2026-10-29T18:15Z |
| Friday | `after_friday.txt` | `ba09a99c3450dd8d…` | 5,804 | 2026-10-29T03:46:52Z | 2026-10-30T20:15Z |

Each update sent the full `job_config.ccr` object (environment `env_01QX7qsmYcEN2QccrAXCgLeX`, tools Bash/Read/Write/Edit/Glob/Grep/WebSearch/WebFetch, model claude-sonnet-5, repo source unchanged). Each returned HTTP 200, and the echoed `derived_state.prompt` showed the preamble and no legacy GIT block.

**Verification limit:** the echoed prompts were compared by reading, not by hash; the tool returns the text to this session only, not to a file. A byte-level check is possible at the next export.

**Thursday connectors:** `mcp_connections: []` in the update was ignored by the API, as on October 2; all six remain attached. **Will UI action remains:** claude.ai/code/routines → Thursday EIA fallback → remove the six connectors → save → reopen and confirm.

**Requirements file:** `scripts/routine-requirements.txt` header changed from DRAFT to INSTALLED; pins unchanged.

**Not changed:** crons. The November 1 DST re-set (+1h UTC on all four) is still owed on its registered date (CATALYSTS 2026-11-01; SCHEDULED_RUNS banner). RemoteTrigger can now do it from a BRENT session.

## 3. Validation run

**Observed 2026-10-29T03:57–04:03Z (≈00:00 ET), ~17 min after the Thursday `updated_at` above.** This was the Thursday EIA-fallback routine firing off its registered cron slot (next scheduled fire per `SCHEDULED_RUNS.md` is 2026-10-29T18:15Z) — timing is consistent with this being the install's own validation fire, but the run itself did not confirm *why* it fired (routines report, they don't adjudicate their own trigger). Full output: `AGENTS/BRENT/demand_destruction/data/thursday_2026-10-29.md`.

Container state hit by this run: **not shallow, HEAD detached, `.venv/` absent, master 262 commits behind origin** (clean fast-forward, no divergence).

| AC | Exercised this run? | Result |
|---|---|---|
| AC1 (shallow+detached boots to `master == origin/master`, no human step) | **Partially** — container was detached but not shallow | MET on the detached-HEAD half: `git checkout master` → `git merge --ff-only origin/master` ran clean, 262 commits fast-forwarded, ended at `origin/master` HEAD, no human step. Shallow-clone half still unobserved on a BRENT run. |
| AC2 (diverged master stops at step 3, prints counts, writes nothing) | No — no divergence existed | Not exercised |
| AC3 (missing `.venv/` rebuilt, or name the missing file) | **Yes** | MET — venv was genuinely absent; `python3 -m venv .venv && .venv/bin/pip install -r AGENTS/BRENT/scripts/routine-requirements.txt` completed clean, all six pinned packages installed without error |
| AC4 (clean full clone prints `unshallowed=n detached=n ff=0 venv=present`, quiet path watched) | No — container was not in the clean/quiet state | Not exercised |

First-line receipt format (`PREAMBLE: unshallowed=<y/n> detached=<y/n> ff=<n> venv=<state>`) was produced correctly on both the output file and this routine's final report, per step 5.

**Remaining for the independent reader:** AC2 and AC4, plus AC1's shallow-container case, are still unobserved on any BRENT routine run as of this entry.

## 4. Live-session confirmation of the validation run (BRENT, 2026-10-29 00:0x ET)

- **Why it fired off-schedule:** BRENT's live session fired it deliberately with `RemoteTrigger run` on `trig_01ALYRXtjDGbfHeubqdvyJdf` at 2026-10-29T03:55:57Z (run session `cse_01CW5vraYvBnujbrVP5FPhX1`), as the single validation run PROME asked for. The Thursday fallback was chosen because it is idempotent when the week is already recorded. The routine was right to flag the timing and leave the cause undecided.
- **Receipt checked at the artifact, not from the routine's prose:** line 1 of `demand_destruction/data/thursday_2026-10-29.md` (commit `8049f255d`) reads `PREAMBLE: unshallowed=n detached=y ff=262 venv=rebuilt`. The run log shows each preamble step in order: shallow test, `git fetch origin`, `git checkout master`, `git merge --ff-only origin/master`, the venv test, and `pip install -r AGENTS/BRENT/scripts/routine-requirements.txt`.
- **Acceptance so far:** AC3 met; AC1 met on its detached half only; AC2 and AC4 unobserved. Judgment on all four is for the independent reader; the next normal run is the scheduled Thursday fire, 2026-10-29T18:15Z.
- **Follow-up outside WQ-510's scope, not done:** the routine found a key-free EIA retail workbook needing `xlrd`, which is not pinned. The live-session BRT-31 evaluator also uses `xlrd`. Adding a pin changes the approved requirements file, so it is a proposal for PROME/Will, not a fix made here.
- **State gap:** the run read origin before this session's STATUS/TRACKER push, so its output carries GASREGW at the October 19 value. The live session recorded October 26 ($4.269) in TRACKER line 4.
