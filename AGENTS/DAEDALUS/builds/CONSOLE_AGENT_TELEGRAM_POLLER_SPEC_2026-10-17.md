# Console agent — Telegram relay (poller) SPEC

**Written:** 2026-10-17 12:39 ET · DAEDALUS (daedalus-6d, desktop) · **For:** PROME, Will
**Commissioned by:** PROME prome-ab, cross-session message 2026-10-17 ~12:37 ET (prompt-hook clock). **Spec only; no code.** Option (a) in `CONSOLE_AGENT_CHANNEL_OPTIONS_2026-10-17.md`.
**Applies only if** Will picks Telegram at plan § 3.3 (`PROME/plans/2026-10-17_console-memory-agent-PLAN.md`). Nothing here authorizes a build, a bot, a key, or spend.
**Platform source:** bundled `claude-api` skill, Claude Code 2.1.302, `shared/managed-agents-*.md`, read 2026-10-17. Items marked UNVERIFIED were not checked against live docs or the live Console.

---

## 0. Acceptance conditions (written first, WQ-229)

Stated as properties of the relay, not as symptoms. Each condition is graded on a live fixture before the relay counts as IMPLEMENTED. The relay is a Will-facing surface, so an independent reader devises at least one counterexample of their own before it is called VERIFIED.

| # | Property | Category |
|---|---|---|
| AC1 | A brief written to the store's `/log/YYYY-MM-DD.md` reaches Will's Telegram chat **exactly once** per relay host, within one poll interval of the relay seeing it, with the date in the first line. | ordinary |
| AC2 | A message from Will's chat id reaches the agent as a `user.message`, and the agent's final `agent.message` text comes back to the same chat. A run that ends without one sends an explicit "no reply (status: …)" line, never silence. | ordinary |
| AC3 | A message from **any other chat id** is never forwarded to the agent, never answered, and is logged locally (chat id + timestamp, no content). | wrong owner |
| AC4 | When the relay starts after downtime, it delivers every undelivered brief from the last 7 days in date order, each marked **LATE (written HH:MM, delivered HH:MM)**, then sends one line stating the downtime window it observed. A late brief is never passed off as fresh. | missing information |
| AC5 | If the API key, bot token, store id or agent id is absent or rejected, the relay **exits nonzero with the reason named** and does not loop silently. When Telegram itself is reachable, it sends Will one "relay cannot reach Console: <reason>" line. | missing information |
| AC6 | A second relay on another host (both machines up) produces a **loud** result, either Telegram's 409 on the second `getUpdates` or a startup refusal, and never a silent split of inbound messages. A brief sent once by each host is acceptable, and visible. | concurrent |
| AC7 | A Telegram message that arrives while the agent is mid-reply to the previous one is queued and answered in order, never dropped and never sent into a running session as an interleaved turn. | overlap |
| AC8 | No secret (bot token, API key) appears in any file under the repo, in the memory store, in a prompt, or in a log line. Checked by grepping relay logs and the store listing for the token prefixes. | ordinary (security) |
| AC9 | A session that reaches its budget cap (`stop_reason: budget_reached`) yields a "budget cap reached — not answered" message to Will, not a retry loop. | missing information |

N/A justifications: none. All five categories apply to a two-way relay.

---

## 1. Shape

```
 Anthropic cloud                                   Will's machine (one at a time)          Will's phone
 ┌───────────────────────────────┐                ┌──────────────────────────────┐        ┌──────────┐
 │ deployment 06:00 ET → session │── writes ─▶ memory store /log/DATE.md            │        │          │
 │ memory store (persistent)     │◀── memories.list/retrieve ── relay (poller) ──▶ │ Telegram │
 │ interactive sessions          │◀── sessions.create + user.message ──┘   ◀─getUpdates─│   bot    │
 └───────────────────────────────┘                └──────────────────────────────┘        └──────────┘
```

The relay is a **courier only**. It holds no memory of its own beyond a delivery ledger. Everything Will says is filed by the agent into the cloud store.

## 2. Outbound: the morning brief

- **What it reads:** the memory store via the host-side memory API, `memories.list(store_id, path_prefix="/log/", view="basic")`, then `memories.retrieve` for any `/log/YYYY-MM-DD.md` that is not in the delivery ledger. Chosen over deployment runs → session → `/mnt/session/outputs` because (i) the store is the agent's durable record, so it's the one place the brief must exist; (ii) it survives the session; (iii) it works the same for interactive sessions. The deployment-runs list (`GET /v1/deployment_runs?deployment_id=…&has_error=true`) is read **only to report failures**: a failed 06:00 run produces "06:00 run failed: <error.type>" in Telegram instead of an absent brief.
- **Cadence:** every 5 minutes between 05:55 and 08:00 ET, then every 30 minutes. The deployment fires at 06:00 with up to 9 minutes of jitter (`managed-agents-scheduled-deployments.md`), so the brief normally lands 06:05–06:15. Cost is negligible: list calls are API reads, not model tokens.
- **Size:** a Telegram message is capped at 4,096 characters (UNVERIFIED, from memory of the Bot API; confirm). Longer briefs split on paragraph boundaries, numbered "(1/2)". The plan's "one screen" target should normally fit in one message.
- **Delivery ledger:** a local TSV of `date · memory_id · content_sha256 · delivered_at · host`. Not in the repo; it's per-machine (§5). Cross-machine duplicates are accepted (AC6).

## 3. Inbound: Will messages the agent

- **Receive:** Telegram `getUpdates` long-poll (timeout ~50 s) on the NEW bot's token. Process only updates whose `chat.id` equals Will's chat id in the config (AC3).
- **Session strategy:** **one session per day ("today's thread")**. The first message after 04:00 ET creates a session with the memory store attached `read_write` and a per-session budget (plan § 2: $10). Later messages that day go to the same session as new `user.message` events, so "that" and "the thing I just said" keep their referent. If the day's session is terminated, budget-capped (AC9) or errored, the relay creates a fresh one and says so in one line. Memory stores attach only at session create (`managed-agents-memory.md`), which this strategy respects.
- **Reply:** stream the session's events, or list them after `session.status_idle`. Concatenate the `agent.message` text from that turn and send it back. Queue later inbound messages until the session is idle (AC7).
- **Tool approvals:** none expected (narrow `always_allow` tool set, see the channel note's permission finding). If a `requires_action` idle ever arrives, the relay **does not approve on Will's behalf**. It sends "agent is asking to run <tool>; reply YES to allow" and waits. Approval stays a human act.
- **Relayed words are operator intent.** Text the relay puts in `user.message` counts as the operator's intent under `auto` evaluation (`managed-agents-tools.md:131`). The chat-id allowlist is what makes that safe. Under no circumstances may the relay forward text from anyone else.

## 4. Where the secrets live

| Secret | Location | Rule |
|---|---|---|
| Telegram bot token (NEW bot, created by Will via @BotFather) | `~/.config/console-relay/.env`, mode 600 | ⛔ Not under `~/.claude/channels/`, where a Claude Code Telegram channel could pick it up and become a second poller. ⛔ Never reuse a fleet bot token (OPENCLAW_CUTOVER_PLAN §0c: two pollers on one token ≈ half of Will's messages silently lost). |
| Anthropic credential for the org holding the $200 credits | same `.env` as `ANTHROPIC_API_KEY`, or an `ant auth login` profile | Must belong to the workspace where the agent and store live. Ideally a key scoped to that workspace only (UNVERIFIED whether workspace scoping is available on this org). |
| Will's chat id, store id, agent id, environment id | same `.env` | Not secret, but kept together so one file configures a host. |

Nothing goes in the repo, the memory store, the agent's system prompt or any message (AC8). The repo may carry the relay's **code** only after Will approves a build, and a home for it is decided then (not `scripts/`; this is not a fleet check).

## 5. When the box is off (the serial-machine limit)

- The cloud keeps working: the 06:00 run fires and writes `/log/DATE.md`. Nothing is lost cloud-side.
- Outbound waits. On restart the relay delivers the backlog marked LATE (AC4).
- Inbound waits. Telegram holds unread updates for a limited time (UNVERIFIED, believed 24 h). Past that window, messages Will sent while every relay was down are **lost**, and the relay can't know it. The restart line therefore says, plainly: "relay was down from X to Y; messages you sent before <Y − 24h> may not have arrived".
- **Laptop:** install the same relay (code + `.env`) on the laptop. Will's one-machine-at-a-time practice means one relay at a time. The closeout before a machine switch should stop the relay (`systemctl --user stop console-relay`) so the overlap window is zero. This is a Will habit to add to the switch routine; PROME decides where it is written.
- **Process host:** a systemd user unit on WSL, the same pattern as LIQUID's existing `liquid-hy-watch.service`. `Restart=on-failure` with a backoff; it never restarts in a tight loop on AC5 failures.

## 6. Size and cost

- **Code:** one Python file (~200–300 lines) using the official `anthropic` SDK (`client.beta.memory_stores.*`, `client.beta.sessions.*`, `client.beta.deployment_runs.*`) and plain HTTPS to Telegram. A `--selftest` covers AC1–AC9 against fixtures plus one live smoke test.
- **Cloud cost added by the relay itself:** API list/read calls, no model tokens. Interactive sessions cost what the agent costs (plan § 2), bounded by the per-session budget.

## 7. Open items (not DAEDALUS's to decide)

1. Will picks Telegram (§ 3.3) and creates the new bot. PROME owns the ask.
2. Where the relay code lives in the repo, if anywhere: PROME/Will at build approval.
3. Whether the machine-switch closeout gains a "stop the relay" line: PROME.
4. Independent reader for the relay before VERIFIED: PROME commissions it at build time.
