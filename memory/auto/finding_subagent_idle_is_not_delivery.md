---
name: finding_subagent_idle_is_not_delivery
description: an idle notification from a spawned reader is NOT its report — subagents cannot SendMessage to "main" (rejected: "You are the main conversation"), some route to a wrong same-named peer, and content can arrive as duplicates or not at all; treat idle-without-content as undelivered and chase BY NAME with an explicit return route
metadata:
  type: finding
---

**In teams/fan-out mode, "the reader finished" and "the coordinator has the report" are different events, and the harness only guarantees the first.** Idle notifications carry no content; the reader's report may exist only in its own transcript.

**Worked case (2026-08-07, DAEDALUS Production Review, 9 readers).** All 9 spawned with *"your final message must be the complete report."* All 9 went idle; **zero reports had arrived** — only idle notifications. On chase, three distinct failure routes surfaced, each self-reported by a reader:

1. **`SendMessage to "main"` is REJECTED** for a spawned subagent (*"You are the main conversation — 'main' addresses you"*) — the instruction "send to main" is unexecutable, and the reader falls back to hoping its turn text relays.
2. **Name-resolution misdelivery:** two readers resolved the coordinator via ListAgents and sent their full reports to `daedalus-1a` — a *different* session that happened to carry the name — then re-sent in parts after a second chase.
3. **Duplicate storms after recovery:** a reader whose first send DID reach the coordinator via a socket route didn't know it, and began re-sending in 3 parts until told to stand down.

All 9 reports were eventually recovered — by **chasing each reader by its spawn name with an explicit instruction to resend, split into parts if long**. This is the second live instance of the class (2026-07-28 PROME-audit readers idled undelivered; that fix — putting the delivery contract in the spawn prompt — was applied here and was NOT sufficient, because the contract named an unexecutable route).

## How to apply

- **Spawn prompts: make the FINAL TURN TEXT the deliverable** (*"your final message IS the report"*) rather than instructing SendMessage-to-main — the turn text is what the harness relays to the coordinator; "main" is not addressable from below.
- **Treat idle-without-content as UNDELIVERED, always.** Chase by the exact spawn name. A summary line on the idle notification saying "[to main] report sent" is a claim about an attempt, not a delivery — `[[finding_record_of_an_action_is_not_the_action]]`.
- **On chase, pre-authorize splitting** ("if it exceeds message limits, split into parts") — full cohort reports can silently exceed single-message delivery.
- **When a report finally arrives by an unexpected route, tell the sender to stand down** — otherwise it keeps re-sending parts and the coordinator pays for every duplicate.
- Coordinator-side mirror of the agent-side rule this repo already carries (deliver-before-idle): the sender's obligation and the receiver's verification are BOTH required; neither alone closes the loop.
