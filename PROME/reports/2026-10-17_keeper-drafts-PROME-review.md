# PROME review of DAEDALUS's "keeper" drafts
**Written:** 2026-10-17 13:01 ET (prome-ab, desktop) · **Reviewed at the artifacts:** `AGENTS/DAEDALUS/builds/console_agent_2026-10-17/` at 528d63b1f (README, agent.md, environment.yaml, two memory_store yamls, deployment-morning.yaml) · `builds/CONSOLE_AGENT_TELEGRAM_POLLER_SPEC_2026-10-17.md` v2 · `builds/CONSOLE_AGENT_CHANNEL_OPTIONS_2026-10-17.md`. · **For:** Will (before creating anything), DEWEY (research in flight; "TERRY" in the first write was Will's typo, corrected 13:25 ET), CATO, DAEDALUS. · **Status:** one reader's opinion, not an independent verification; no file of DAEDALUS's was edited.

## Verdict
The agent is ready to create and smoke-test. The relay is a larger build than the agent and should be split into phases. Two design choices need Will's word before the schedule exists: the brief's time, and whether an always-on box is in scope.

## What is strong (keep)
1. **Two-stage capture** (relay spec § 1, AC1): plain code saves the thought to the cloud store before any model runs, with a "saved" reply within seconds. This is the one decision that matches Will's brief ("I often lose them"). Everything else can be slow; this cannot.
2. **The prompt carries Will's words and marks inference.** `profile.md`: his lines win, agent lines labelled said-with-date or INFERRED-with-evidence. "Never invent a memory, a date or a quote." Secrets withheld and said so. One line per capture, no advice, speaks first only at the brief.
3. **No-stall by construction:** every enabled tool `always_allow`, zero network hosts, web off; bash justified (clock + `mv`) and contained. Scheduled run cannot pause.
4. **Acceptance conditions before code** (AC1–AC10, all five WQ-229 categories, no N/A) and UNVERIFIED marked where it is.
5. **Smoke test and a manual brief run before any schedule** (README step 5), $2 and $10 caps.

## Findings, ranked
| # | Finding | Why it matters | Proposed change | Owner |
|---|---|---|---|---|
| F1 | **06:00 ET collides with Will's capture window.** USER.md: Will is active from roughly 6 AM. The deployment fires 06:00–06:09 (jitter) and mounts `will-memory` read-write; a capture at 06:03 opens the day's interactive session on the SAME store. Both agents may edit the same `threads/<slug>.md` (last write wins; the store offers no lock). | A lost thread update on his most active morning, silently. | Fire at **05:15 ET**; relay holds stage-2 filing (not stage-1 saving) while a morning run is active; brief finished before he wakes. | Will (time) · DAEDALUS (spec) |
| F2 | **The relay is the real build and it is bundled.** v2 = ~400 lines + lease protocol + delivery ledger + local Whisper on GPU in WSL (CUDA/cuDNN friction UNVERIFIED) + edit-in-place replies + systemd on two machines. The agent is 80 lines. | Weeks of infrastructure before one thought is captured from the phone. | Phase the relay: **R1** text only, one machine, no lease, no voice (≈150 lines, AC1–AC3, AC7–AC9) → **R2** voice → **R3** lease and second machine. Each phase measured. | DAEDALUS · PROME commissions |
| F3 | **"Runs without a machine" buys less than it sounds.** The 06:00 run writes the brief in the cloud, but Will reads it only when a relay machine is on, and captures only reach the store the same way. On a both-off morning: nothing. | The always-on-host question is the fork for the whole channel, not a "later" item. | Decide now: (a) accept the gap and measure it; (b) a tiny always-on box (Pi or ~$5/mo VPS) running ONLY the relay — different from the retired fleet VPS in scope and blast radius. | Will |
| F4 | **Bare-word commands can misfire.** `kill`, `park`, `push` as plain words; a capture beginning "kill the idea of…" or "push back on…" is ambiguous. | A thought mis-filed as a command, or a command filed as a thought. | Slash prefix: `/kill <slug>`, `/park`, `/push`, plus `/threads` (list live) and `/profile <line>` (writes a said-line, so Will edits his profile from the phone, not the Console). | DAEDALUS (prompt + spec) |
| F5 | **Desk-tagged captures go nowhere.** Market/research thoughts are filed under `desk` and not analyzed (good boundary), but nothing routes them onward. | Will's best trading thoughts captured at 11 PM stay in a store PROME never reads. | Brief lists the day's `desk` captures in one line; Will forwards what he wants, or a later PROME read of that tag only (read-only, PROME's ask). | PROME (ask) · Will |
| F6 | **Rewriting `picture.md` daily discards the agent's prior picture.** Versions preserve bytes, but the agent never reads them. | Pattern-matching over weeks needs memory of its own earlier reads. | Keep a dated `picture/YYYY-WW.md` weekly snapshot, or a "what changed since last week" section. Small. | DAEDALUS |
| F7 | **Budget math:** worst day = $2 + $10 = $12 ⇒ $200 lasts ~16 days worst case, 3–6 months typical. | Set expectations. | Keep caps; review spend at the two-week measure. | PROME |
| F8 | **No independent read of the system prompt yet.** It is the one artifact that shapes how the agent treats Will. | WQ-229 says a Will-facing surface gets an independent reader with a counterexample. | One Sonnet cold read (WQ-447 A) before the schedule, not before the smoke test. | PROME commissions on Will's word |

## Not findings (checked, fine)
Captures as one file each (relay writes, agent appends a `filed:` line) · the second store for relay state, never mounted to the agent · the inbox/threads/parked/profile/picture/log layout · `effort: medium` (API default; raise if briefs read thin) · the 14-day resurfacing rule and the monthly parked list · seeding `profile.md` with Will's brief verbatim before the first session.

## Decisions for Will (not for the desks)
1. Brief time: 05:15 ET (rec) or keep 06:00.
2. Always-on box in scope now, or accept the gap and measure.
3. The two rules (profile his to edit; decay with a two-word kill) — still unconfirmed.
4. Name.
