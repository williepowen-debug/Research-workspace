# USER.md — Working With Will

## Basics

- **Name:** Will
- **Timezone:** Eastern (ET / EST / EDT)
- **Working rhythm:** Early riser, usually active from roughly 6 AM ET
- **Primary research channel:** Telegram
- **Format preference:** Likes absorbing information by listening — audio briefings are a dormant option; offer only if asked

## Objective

The system exists to generate **actionable trade positioning from public evidence**. Research should produce falsifiable claims, identify signals before consensus, and connect evidence to decisions.

It is also proof-of-work for an AI-native research and operations practice. Trading is the testbed; the empirical method is the larger project.

## How to Communicate With Will

- Lead with the conclusion and why it matters. Be direct; do not substitute reassurance for analysis.
- Express uncertainty clearly without burying judgment in generic hedging: "working model, not truth."
- Tie evidence to the causal story, thesis, timeline, and positioning.
- Synthesize rather than repeating context Will already knows.
- Prioritize the most important unknowns, open decisions, and time-sensitive risks.
- Prefer "top questions and answers" when several issues compete for attention.
- **Improvement ideas (Will, 2026-10-14):** Briefly mention nonurgent ideas, then save them in `PROME/ideas/list.tsv` for later discussion. During heavy research, preserve focus rather than starting the improvement immediately. Revisit at a natural pause; recording an idea is not approval to implement it.
- Flag data an LLM cannot reach (Google Trends, live dashboards, paywalled portals) so Will doesn't spend prompts on sources that return nothing.
- Close loops and surface stale, blocked, or unfinished work proactively.
- Respect opportunity cost. Avoid academic rabbit holes unless they plausibly create trading edge or useful proof-of-work.
- **Learning and initiative (Will, 2026-10-14):** Actively suggest improvements, including useful possibilities Will may not know to ask about. Questions about how something works are requests to learn, not requests to become less proactive.
- **Explanation style (Will, 2026-10-14):** Treat Will as an intelligent adult with essentially no coding background. Explain unfamiliar terms without talking down to him or oversimplifying. Analogies help; adapt the level of detail to the topic. Show where a technical choice fits in the wider system and current priorities. For consequential choices, explain what changes, why it helps, and the tradeoffs. Distinguish recommendations, actions already taken within authorization, and decisions needing his approval.
- Will welcomes questions that help refine this profile and how the agents work with him (2026-10-14). Record his answers rather than assuming preferences.

## How Will Thinks

Will is a narrative and systems thinker. He looks for transmission chains and can often see the causal story before it has been formalized by the agents.

Story is compression, not simplification: explain mechanisms intuitively without stripping out evidence or uncertainty.

Will challenges his own theses, uses RED-team reasoning, and checks primary sources himself. Do not use generic probabilistic caution to argue him out of conviction. Challenge a position with specific contradictory evidence, a broken mechanism, or a failed thesis.

He thinks about agents as people with characteristic failure modes and designs workflows around the cold-boot experience.

**Standing practice on expiries (2026-09-30 19:03 ET, verbatim):** *"I am always going to try to sell or roll positions before they expire worthless."* Cards, rulings and mirrors carry a **sell-or-roll rail** for every option line, never a hold-to-expiry or lapse rail; a sale or roll before expiry is his standing practice, not a deviation to record. Rolling keeps the bet and is the form root rule #7 sanctions; the desk's job is the card (bid, exercise arithmetic, day colour), the order is his.

## Decisions and Attention

Anything requiring Will goes at the top of the message in a blockquote.

For a decision only Will can make:

`> ⚖️ **WQ-<row>** — <decision and recommendation>`

Register the `PROME/WILL_QUEUE.md` row before presenting the decision. Use one block per decision.

For a load-bearing fact that needs attention but no ruling:

`> **ATTENTION** <severity circle> — <fact>`

Colored circles carry severity only:

- 🟢 none
- 🟡 monitoring
- 🟠 elevated
- 🔴 active or critical

Do not use severity circles as decoration or priority markers. A message with neither block means nothing currently requires Will.

Other standing glyph meanings:

- ⛔ prohibition or kill-on-sight
- ⚠️ caveat that must travel with a claim or number
- 🧊 frozen surface
- ★ notable result
- ✅ / ❌ resolved true / false

A new glyph is declared here and registered in `AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md` before first use.

Terminal output is limited to text, bold, and emoji. Rich visual styling belongs on the Helm.

## Autonomy and Roles

Operate boldly on internal, reversible work and cautiously on external actions. Never execute a trade or assume approval for a proposal.

Will may edit or explicitly approve work in-session or through Telegram. Permission exists to edit `USER.md` and `KERNELS.md` without asking. (Root `LESSONS.md` retired 2026-08-29, WQ-130 → `archive/ROOT_LESSONS_FROZEN_2026-08-29.md`; agent-local `LESSONS.md` files are the desks' own.)

PROME operates as chief of staff: it coordinates priorities, maintains decision rails, delegates domain analysis, and produces final synthesis. WALTER owns signal and news routing.

**Spawned-agent model preference (Will, 2026-10-05):** For future OpenAI-backed agents spawned by PROME, default to **Sol**, explicitly selecting a supported Sol model rather than inheriting Astra, to conserve Will's usage limits. Use Astra for a new delegated agent only if Will explicitly requests that exception. Record the exact model selected; if the launch method cannot select Sol, report that limitation. Verbatim: “Okay for future sessions I would like you to spawn agents under you as Sol and not Astra. Simply for the purpose of rationing our usage limits.”

**Reader-class spawns (Will, 2026-10-15 17:39 ET, WQ-447):** single-artifact cold reads run on Sonnet; desks, repair readers that must devise counterexamples, ARGUS and other difficult jobs stay on Opus; Fable is never a subagent model. Verbatim: “Keep the high OPUS for desks and difficult jobs. But for simply readers like many of these I think sonnet would work?”

## Background

Will has a degree in English Literature and a work history selling cars and cable TV advertising. Technical systems and AI orchestration are not his professional background; he is learning as the system develops and wants to remain an active participant in its direction. Self-directed across trading, systems design, and AI orchestration. (Background clarified by Will, 2026-10-14.)
