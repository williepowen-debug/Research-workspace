# Console agent — how Will reaches it (channel options)

**Written:** 2026-10-17 12:39 ET · DAEDALUS (daedalus-6d, desktop) · **For:** PROME (plan § 3.3 decision), Will
**Commissioned by:** PROME prome-ab, cross-session message 2026-10-17 ~12:37 ET (prompt-hook clock) ("own now, decision-independent").
**Parent plan:** `PROME/plans/2026-10-17_console-memory-agent-PLAN.md` (PROME's file; this note answers its § 3.3 and § 6 DAEDALUS question).
**Status:** comparison only. Nothing built, nothing applied, $0 spent.
**Platform source:** the `claude-api` skill's bundled Managed Agents docs, Claude Code 2.1.302, read 2026-10-17: `shared/managed-agents-{tools,webhooks,scheduled-deployments,memory,events,environments}.md`. Fleet facts come from `AGENTS/WALTER/design/OPENCLAW_CUTOVER_PLAN.md` §0c and a listing of `~/.claude/channels/` (directory names and key names only; no secret was read).

---

## The short version for Will

The agent itself lives in Anthropic's cloud. It runs at 6 AM whether or not any of your computers is on, and its memory lives there too. The open question is only how its words reach your phone, and how yours reach it.

- **If you want to text it from Telegram, the relay has to run on one of your computers.** Telegram's bot password is part of the web address, and the Console's secure key store only inserts passwords into a message's headers or body (`managed-agents-tools.md:330`). So the cloud agent can't post to Telegram safely by itself. A small program on your desktop has to carry messages both ways.
- ⚠️ **That program only works while the machine it lives on is awake.** You run one machine at a time (desktop ⇄ laptop). On a laptop day, the 6 AM brief is still written in the cloud, but it reaches your phone only when a machine with the relay comes back on. The same goes for your messages to it. You can install the relay on both machines, but only one may run at a time.
- **The cloud-only alternative is a daily page you read** (for example in Notion). It needs no computer of yours, but it's one-way: you read it, you can't text it.

---

## The three options

| | **(a) Desktop poller + Telegram** | **(b) Hosted page (Notion MCP), outbound only** | **(c) Console session viewer only** |
|---|---|---|---|
| **What Will sees on his phone** | A Telegram chat with a bot. The brief arrives as a message around 06:00–06:10 ET. He can reply "remember …" and get a confirmation back. | A dated Notion page each morning, read in the Notion app. No reply path; capture happens elsewhere. | Nothing on the phone in practice. The Console is a desktop web page (session list, transcript, cost); capture means opening a session in a browser. |
| **Desktop ⇄ laptop switch** | ⚠️ **Breaks while the relay's machine is off.** The cloud run still happens and the brief sits in the memory store; delivery waits for a relay to come up. Telegram holds unread bot updates for a limited time (UNVERIFIED, believed 24 h — check the Bot API docs before relying on it). Two relays running at once → Telegram refuses the second poller (409 Conflict). Loud, not silent. | **Nothing breaks.** Fully cloud-side. | **Nothing breaks.** Fully cloud-side. |
| **Build size** | Medium. One NEW Telegram bot (Will, ~5 min on his phone) + one Python poller (~200–300 lines) + a systemd user unit on each machine. Spec: `CONSOLE_AGENT_TELEGRAM_POLLER_SPEC_2026-10-17.md`. | Small. One MCP server entry + one OAuth vault credential (Will authorizes Notion once in the Console). No code on the box. Requires that Will has, or wants, a Notion workspace (UNKNOWN). | Zero. |
| **Failure modes** | Relay down (machine off, crashed, WSL asleep) → late delivery, with no alarm unless the relay announces itself on restart. Token or key misplaced → silent non-delivery. Brief sent twice when both machines' relays ran on the same day (harmless, visible). Inbound from a stranger → must be dropped by a chat-id allowlist. | MCP tool calls default to `always_ask` (`managed-agents-tools.md:68`), and **a scheduled run has no client attached to approve them, so it waits indefinitely** (`managed-agents-scheduled-deployments.md`, Deployment runs). The Notion write tool must be explicitly `always_allow`. OAuth refresh failure → `vault_credential.refresh_failed`; the page silently stops arriving unless someone watches. | No capture from the phone, so the "dump a thought at any hour" use case is not served. Desk-bound. |
| **Collides with fleet?** | ⚠️ **Must NOT reuse an existing bot token.** The fleet runs per-agent bots (`~/.claude/channels/telegram-{walter,brent,brock,carl,labor,liquid,red,reginald,sam}/`). A second poller on any of those tokens splits Will's messages between two readers, so about half silently vanish (OPENCLAW_CUTOVER_PLAN §0c, "proven"). A new dedicated bot is required. | No. | No. |

### Correction to the commissioning wording
PROME's commission names option (a) as "desktop poller + **existing** bot token". That is unsafe for the reason in the last row: every existing token already has a live reader. Option (a) means **a new bot**, created by Will with @BotFather, whose token is used by nothing else.

---

## A finding that applies to every option: scheduled runs can't stop to ask

`managed-agents-scheduled-deployments.md` (Deployment runs): *"No client is attached when a run fires, so answer calls that pause for approval (`auto` with no determination, or `always_ask`, the MCP default) … or the run waits indefinitely."*

PROME's plan § 4 sets `permission_policy: auto`. Under `auto` the server runs a call, denies it, **or pauses when it reaches no determination** (`managed-agents-tools.md:69,103`). A paused 06:00 run produces no brief and no error. **Recommendation for the definition files (held until Will's five answers):** give the scheduled agent a narrow tool set — file read, write, edit, glob and grep on the memory mount; bash and the web tools off — each `always_allow`. A pause becomes impossible by construction rather than unlikely. If the poller (option a) is built, it could also answer pauses, but that couples the morning brief to the box being on, which is what the cloud schedule exists to avoid.

---

## DAEDALUS recommendation

**Start with (a) if Will wants phone capture. That is the plan's stated purpose ("a conversational capture channel that reaches the phone at any hour", § 5).** Accept and name the serial-machine limit: messages wait while the relay's machine is off. Add **(b) later only if** missed mornings turn out to matter in the two-week measurement. **(c) is the smoke-test surface for everyone, not a channel.**

If Will doesn't use Notion and doesn't want a computer-bound relay, the honest answer is (c) plus one remembered habit: open the Console. That doesn't meet the plan's purpose, so it should be chosen knowingly.

**Decision owner:** Will (plan § 3.3), via PROME. This note is an input, not a ruling.
