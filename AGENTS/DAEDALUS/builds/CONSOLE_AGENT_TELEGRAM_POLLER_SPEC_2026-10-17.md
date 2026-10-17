# Console agent — Telegram relay SPEC (v2: primary channel)

**v2 written:** 2026-10-17 12:47 ET · DAEDALUS (daedalus-6d, desktop) · **For:** PROME, Will
**v1:** 2026-10-17 12:39 ET, commit 17ea8f905 (option (a) of three). **v2 is a re-scope, not a correction pass.** Will's brief (plan § 3b, 12:42 ET) made Telegram the PRIMARY channel. PROME's 12:43 ET message asked for four additions: voice notes, a capture latency target, a one-line confirmation, and the serial-machine limit designed around rather than only disclosed.
**Spec only; no code.** Nothing here authorizes a build, a bot, a key, or spend.
**Platform source:** bundled `claude-api` skill, Claude Code 2.1.302, `shared/managed-agents-*.md`, read 2026-10-17. UNVERIFIED = not checked against live docs, the live Console, or the laptop.
**Agent drafts this relay serves:** `builds/console_agent_2026-10-17/` (agent `keeper`, store `will-memory`, relay store `keeper-relay-state`).

---

## 0. Acceptance conditions (written first, WQ-229)

Properties of the relay, not symptoms. Each is graded on a live fixture before IMPLEMENTED. The relay is Will-facing, so an independent reader devises at least one counterexample of their own before VERIFIED.

| # | Property | Category |
|---|---|---|
| AC1 | **A capture is saved before any model runs.** Within **3 s** (text) or **transcription time + 3 s** (voice) of Telegram delivering it, the capture exists in the store at `inbox/YYYY-MM-DD/HHMM-<update_id>.md` with Will's exact words, and Will sees a `✓ saved HH:MM` reply. If the agent is slow, down or out of budget, the capture is still saved. | ordinary |
| AC2 | The `✓ saved` reply is **edited in place** to the agent's one-line filing (`✓ saved 14:02 → kitchen-reno`) when the agent finishes. It is never a second notification. If the agent produces no line within 120 s, the reply becomes `✓ saved 14:02 · filing pending` and the morning run files it. | ordinary |
| AC3 | A message from **any other chat id** is never saved, never forwarded, never answered. It is logged locally as chat id + timestamp, no content. | wrong owner |
| AC4 | A voice note is transcribed **on the relay host**. The saved capture carries `source: voice`, the duration, the transcript, and the Telegram `file_id`, so the audio can be re-fetched while Telegram keeps it. A failed transcription saves `source: voice · TRANSCRIPTION FAILED` plus the file_id, and says so in the reply. It is never silently dropped. | missing information |
| AC5 | Each morning brief reaches Will **exactly once across all relay hosts**. The delivery ledger is shared (§ 5), not per machine. A brief delivered late is marked `LATE (written HH:MM, delivered HH:MM)`. | concurrent |
| AC6 | **At most one relay polls Telegram at any moment**, arbitrated by a lease in the shared relay store (§ 5). A second relay that starts while the lease is fresh stays STANDBY and says so in its own log. A relay that loses the lease stops polling within one heartbeat. Two pollers is a failure, never a split. | concurrent |
| AC7 | A message that arrives while the agent is still filing the previous one is **saved immediately (AC1)** and handed to the agent in order after the current turn. It is never dropped and never interleaved. | overlap |
| AC8 | No secret (bot token, API key) appears in the repo, either memory store, any prompt or message, or any log line. Checked by grepping logs and both store listings for the token prefixes. | ordinary (security) |
| AC9 | Missing or rejected credentials or ids → the relay **exits nonzero naming the reason** and never loops silently. Budget cap reached (`stop_reason: budget_reached`) → the reply line reads `✓ saved · agent at budget cap, filed tomorrow`. | missing information |
| AC10 | When a relay takes the lease after a gap, it sends **one** line: `relay was off X–Y; anything you sent before <Y − 24h> may not have arrived` (see § 5 on Telegram retention), then delivers any backlog. | missing information |

N/A justifications: none. All five categories apply.

---

## 1. Shape: two-stage capture

```
 Will's phone ──text/voice──▶ Telegram ◀──getUpdates── RELAY (whichever machine holds the lease)
                                                          │ 1. (voice) transcribe locally
                                                          │ 2. memories.create inbox/… ──────────▶ ┌ cloud store will-memory ┐
                                                          │ 3. reply "✓ saved HH:MM"                │                          │
                                                          │ 4. user.message "new capture: <path>" ─▶ today's keeper session    │
                                                          │ 5. edit reply → "✓ saved HH:MM → slug"  │ (files into threads/)    │
                                                          │                                         └──────────────────────────┘
 06:00 ET deployment (cloud, no machine needed) ──writes log/DATE.md──▶ store ──read by relay──▶ Telegram brief
```

**Why two stages.** Will's brief says the thought lives for seconds. The model is the slow and failable part: a session starting up, Opus thinking, a budget cap. Stage 1 is plain code and makes the thought safe before any model runs. Stage 2 is the agent's judgment, so it can be slow without losing anything.

## 2. Capture latency targets

| Path | Target (Telegram delivery → `✓ saved`) | Basis |
|---|---|---|
| Text | **≤ 3 s** p95 | long-poll delivery is near-instant; one `memories.create` call; one Telegram send. UNVERIFIED until measured. |
| Voice, ≤ 60 s note | **≤ 10 s** p95 on the desktop | download + local transcription (§ 3) + the text path. Desktop: 20 cores, RTX 3070 visible in WSL (checked 2026-10-17). Laptop: UNVERIFIED, likely slower on CPU only. |
| Filing line (stage 2) | **≤ 60 s** typical, 120 s ceiling (AC2) | the session is already warm if Will messaged earlier that day; a cold session start is slower. UNVERIFIED. |

The relay logs each capture's three timings so the targets are measured from week one, not asserted.

## 3. Voice notes

- **Where it runs:** on the relay host, never in the cloud agent. To DAEDALUS's knowledge Managed Agents takes no audio input; the bundled docs have no audio path (UNVERIFIED against live docs). Local also means Will's spoken thoughts go to no third party.
- **Engine:** `faster-whisper` (open-source Whisper) in the relay's own Python environment. Use the `small` or `medium` model on the desktop GPU, and `small` on CPU for the laptop. Not installed today (checked: not in `.venv`, no system `ffmpeg`; faster-whisper decodes audio through PyAV without system ffmpeg, UNVERIFIED). Install is a build step requiring Will's approval.
- **Cost:** $0 per note; a one-time model download of a few hundred MB per machine (UNVERIFIED size).
- **Rejected alternative:** a cloud speech API, such as OpenAI's Whisper API at about $0.006/min (UNVERIFIED price). It would send every spoken thought to another provider, which is an external send needing Will's word. Hold it as a fallback only if local accuracy disappoints.
- **Accuracy guard:** the agent sees `source: voice` and is told by its prompt never to rewrite captures. A misheard word stays visible in the saved capture, and Will can correct the thread.

## 4. Session strategy and confirmation

- **One session per day.** The first capture after 04:00 ET creates a session with `will-memory` attached `read_write` and a $10 budget (plan § 2). Later captures that day are new `user.message` events in it. If that session is terminated, errored or budget-capped, the relay starts a fresh one and says so in the reply line.
- **The agent's reply is one line** (its prompt requires this). The relay edits the `✓ saved` message to append it (Telegram `editMessageText`), so Will gets **one notification per capture**, not two.
- **Questions and commands** (`what was…`, `kill <slug>`, `push <slug>`) still go through stage 1: saved as captures, so the record is complete. The agent's answer comes back as a normal reply, since it may be longer than one line.
- **Tool approvals:** none expected (narrow `always_allow` tool set). If a `requires_action` ever arrives, the relay asks Will `agent wants to run <tool> — reply YES` and never approves on his behalf.
- **Relayed words are operator intent** (`managed-agents-tools.md:131`). That is why AC3's chat-id allowlist is absolute.

## 5. Designing around the serial-machine limit

**Fact (unchanged from v1):** the relay must run on one of Will's machines. A Telegram bot token travels in the URL path, which the Console's vault never substitutes (`managed-agents-tools.md:330`).

**The design: the relay runs on whichever machine is on, and the machines share state through the cloud, not through git.**

| Piece | Where it lives | Shared between desktop and laptop? |
|---|---|---|
| Captures, threads, briefs | cloud store `will-memory` | **Yes**, it is the cloud |
| **Lease** (`lease.md`: host · heartbeat time) | cloud store `keeper-relay-state`, updated with `memories.update` + `precondition: content_sha256` (optimistic concurrency, `managed-agents-memory.md`) | **Yes.** This is what stops two pollers |
| **Delivery ledger** (`delivered/YYYY-MM-DD.md` per brief) | cloud store `keeper-relay-state` | **Yes.** This is what makes AC5 "exactly once" |
| Bot token, API key, ids | `~/.config/console-relay/.env` (mode 600) on **each** machine | **No.** Installed by Will on each machine |
| Whisper model | each machine's relay environment | **No.** Downloaded per machine |
| Relay logs and timings | each machine, local | **No.** Each machine sees its own |

**Lease rules.** Heartbeat every 2 minutes. A lease older than 6 minutes is free to take. On taking the lease, a relay checks the store for captures and briefs it hasn't handled. A relay whose heartbeat write fails on the precondition has lost the lease and stops polling (AC6). The lease lives in a store the agent never mounts, so ~720 small versions a day never reach the agent's context. (Versions accumulate for the life of the memory. Rotate to a new lease file monthly if the version list grows unwieldy; UNVERIFIED whether that matters.)

**What this buys.** Will can switch machines without remembering anything. Close the desktop lid, open the laptop, and the laptop's relay takes over within ~6 minutes. No duplicate briefs, no split messages, no "stop the relay" step at closeout.

**What it can't buy, stated plainly for Will.**
- ⚠️ **When both machines are off, nothing reaches the phone and nothing from the phone is saved.** The 06:00 brief is still written in the cloud and arrives LATE when a machine comes on.
- ⚠️ **Messages sent while both machines are off wait in Telegram for a limited time.** Believed to be 24 hours (UNVERIFIED; check the Bot API docs). After that they are gone and no relay can know it. AC10's line tells Will the gap.
- **The only fix for "both off" is a machine that is always on.** That would be a small always-on server (a few dollars a month, external). The fleet deliberately shut down its cloud server in the OpenClaw cutover, so this is Will's call and a later phase, not part of this build.

## 6. Where the secrets live

| Secret | Location | Rule |
|---|---|---|
| Telegram bot token (NEW bot, created by Will via @BotFather) | `~/.config/console-relay/.env`, mode 600, on each machine | ⛔ Not under `~/.claude/channels/`, where a Claude Code Telegram channel could pick it up and become a second poller. ⛔ Never a fleet bot token: every fleet bot already has a reader (OPENCLAW_CUTOVER_PLAN §0c). |
| Anthropic credential for the org holding the credits | same `.env` (`ANTHROPIC_API_KEY`) or an `ant auth login` profile | Must belong to the workspace where `keeper` lives. Workspace-scoped key availability is UNVERIFIED. |
| Will's chat id, store ids, agent id, environment id | same `.env` | Not secret; one file configures a machine. |

Nothing secret goes in the repo, either store, any prompt or any message (AC8). The relay's code lands in the repo only after Will approves a build, and its home is decided then (not root `scripts/`; this is not a fleet check).

## 7. Size and cost

- **Code:** one Python file, ~350–450 lines with the lease and voice (up from v1's 200–300), using the official `anthropic` SDK (`beta.memory_stores.*`, `beta.sessions.*`, `beta.deployment_runs.*`), plain HTTPS to Telegram, and `faster-whisper`. A `--selftest` covers AC1–AC10 on fixtures; one live smoke test per machine.
- **Process:** a systemd user unit on each machine (the pattern of LIQUID's `liquid-hy-watch.service`), `Restart=on-failure` with backoff, never a tight loop on AC9 failures.
- **Cloud cost added by the relay:** API reads and small memory writes only, no model tokens. Agent cost is the agent's (plan § 2): $2 per 06:00 run, $10 per day's interactive session.

## 8. Open items (not DAEDALUS's to decide)

1. Will creates the new bot (two minutes in @BotFather) and gives the relay his chat id. PROME owns the ask.
2. The voice engine install (faster-whisper + model download) on each machine: part of build approval.
3. The relay's code home in the repo, if any: PROME/Will at build approval.
4. The independent reader before VERIFIED: PROME commissions it at build time.
5. An always-on host for the "both machines off" gap: Will, later, only if the two-week measurement says missed captures matter.
