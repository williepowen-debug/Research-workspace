# USER.md — Working With Will

## Basics

- **Name:** Will
- **Timezone:** Eastern (ET / EST / EDT)
- **Working rhythm:** Early riser, usually active from roughly 6 AM ET
- **Primary research channel:** this terminal chat (Telegram retired 2026-10-27)
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
- **Will's only window is this chat (Will, 2026-10-31 09:32 ET, verbatim):** *"Literally the only thing I see is just the texts from this terminal and communicating with you"*. Repo files, generated views and apps are invisible to him unless PROME brings their content into the conversation; a pointer to a file is not a briefing. When something matters, say it here in plain words.
- **Fewer round trips (Will, 2026-10-31 10:18 ET, verbatim):** *"Yeah lets eliminate extra steps going back and forth."* When a decision has a natural follow-on step, ask for the conditional approval up front ("if the check passes, proceed") rather than returning for a second yes. Gated items (trades, spend, external sends) still need his word each time.
- **Fewer checkers and rules (Will, 2026-10-31 15:18 ET, verbatim):** *"I do think we want to limit our excess amount of checkers and rules etc"* (said as he dropped the cadence-wake rule, WQ-576). Default to not adding a check, gate or rule: fix the instance or improve an existing control, and propose retiring controls that do not earn their keep. A new checker needs a concrete recurring miss and his word.
- Flag data an LLM cannot reach (Google Trends, live dashboards, paywalled portals) so Will doesn't spend prompts on sources that return nothing.
- Close loops and surface stale, blocked, or unfinished work proactively.
- Respect opportunity cost. Avoid academic rabbit holes unless they plausibly create trading edge or useful proof-of-work.
- **Learning and initiative (Will, 2026-10-14):** Actively suggest improvements, including useful possibilities Will may not know to ask about. Questions about how something works are requests to learn, not requests to become less proactive.
- **Explanation style (Will, 2026-10-14):** Treat Will as an intelligent adult with essentially no coding background. Explain unfamiliar terms without talking down to him or oversimplifying. Analogies help; adapt the level of detail to the topic. Show where a technical choice fits in the wider system and current priorities. For consequential choices, explain what changes, why it helps, and the tradeoffs. Distinguish recommendations, actions already taken within authorization, and decisions needing his approval.
- Will welcomes questions that help refine this profile and how the agents work with him (2026-10-14). Record his answers rather than assuming preferences.

- **Document small news; it may matter in combination (Will, 2026-11-05 15:22 ET, WQ-622 A, every desk):** *"Even if any singular piece of news doesnt move the needle by itself - we do want to account for and document things that might matter eventually, or in combination, etc."* Too small to act on is not too small to record, and themes are updated as new data arrives. Logging is not scoring: nothing logged moves a score, band or trigger. Set-up guide for each desk: `PROME/COMBINATION_WATCH.md`.
- **Quiet mode during desk sweeps (Will, 2026-11-06 18:20 ET; PROME's wording of his instruction, record `memory/auto/feedback_quiet_mode_during_desk_sweeps.md`):** one digest plus interrupts while desks work; label a relayed claim that has not been verified.
- **Forecast report 1's historical reconstruction is stopped (Will, 2026-11-05 15:59 ET; PROME's wording, record `PROME/reports/2026-11-05_forecast-report-1.md` § Closed):** no further historical timing checks on that report; its labels stand as recorded, described as "supported by recorded dates". The forward forecast work continues. Scope: that report only.

## How Will Thinks

Will is a narrative and systems thinker. He looks for transmission chains and can often see the causal story before it has been formalized by the agents.

Story is compression, not simplification: explain mechanisms intuitively without stripping out evidence or uncertainty.

Will challenges his own theses, uses RED-team reasoning, and checks primary sources himself. Do not use generic probabilistic caution to argue him out of conviction. Challenge a position with specific contradictory evidence, a broken mechanism, or a failed thesis.

He thinks about agents as people with characteristic failure modes and designs workflows around the cold-boot experience.

**No expiry nagging (Will 2026-10-20; shortened to this one line on his word 2026-11-12 10:12 ET, replacing the 9/30 and 10/20 paragraphs):** Will manages his own expiries. No expiry reminders, no sell-or-roll pushes and no sell-or-roll plan on cards, in briefs, boot reports, cards or packets; a line may simply expire. Book what his captures show and never infer a disposition. Spend the attention on new positions and good trades (TERRY constructs; root rule #5 governs approval). Lifted only by his word. Prior text: `git log -p -- USER.md`.

**Trade ideas loosened (2026-10-20 11:50 ET, verbatim):** *"we can loosen rules for trade ideas"*. TERRY may bring trades whose trigger has NOT fired, each labelled NOT-FIRED with trigger state, size and risk in figures; Will decides every one (root rule #5). The $500/card and X1 limits remain the default shown on each card; going past them is his choice per card, never pre-approved (`PROME/STATUS.md` § Restrictions).

**Always look for the trade (2026-11-10 18:03 ET, verbatim):** *"yes we should always be looking to see if something is tradeable"*. A material research finding goes to TERRY for a tradeability read as part of the same work, without asking Will first; NOT-FIRED cards or a reasoned "no card" are both complete answers. Approval is unchanged: root rule #5, the $500 per card and X1 defaults (PROME's wording of the consequence; record `memory/auto/feedback_always_check_whether_a_finding_is_tradeable.md`).

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

Will may edit or explicitly approve work in-session. Permission exists to edit `USER.md` and `KERNELS.md` without asking. (Root `LESSONS.md` retired 2026-08-29, WQ-130 → `archive/ROOT_LESSONS_FROZEN_2026-08-29.md`; agent-local `LESSONS.md` files are the desks' own.)

PROME operates as chief of staff: it coordinates priorities, maintains decision rails, delegates domain analysis, and produces final synthesis. WALTER owns signal and news routing.

**Spawned-agent model preference (Will, 2026-10-05):** For future OpenAI-backed agents spawned by PROME, default to **Sol**, explicitly selecting a supported Sol model rather than inheriting Astra, to conserve Will's usage limits. Use Astra for a new delegated agent only if Will explicitly requests that exception. Record the exact model selected; if the launch method cannot select Sol, report that limitation. Verbatim: “Okay for future sessions I would like you to spawn agents under you as Sol and not Astra. Simply for the purpose of rationing our usage limits.”

**Fable is PROME-only (Will, 2026-11-02 09:49 ET, WQ-590):** verbatim *"I would only want to use Fable for PROME and not the lower hierachical agents."* Desks, readers and every other spawn never run on Fable. While Claude usage is exhausted (Will 09:41 ET: out until Wed 2026-11-04), desk spawns run on Codex Sol (`codex exec --model gpt-6.1-sol`, headless at the desk directory); the Opus rule above resumes when Claude usage returns.

**Reader-class spawns (Will, 2026-10-15 17:39 ET, WQ-447):** single-artifact cold reads run on Sonnet; desks, repair readers that must devise counterexamples, ARGUS and other difficult jobs stay on Opus; Fable is never a subagent model. Verbatim: “Keep the high OPUS for desks and difficult jobs. But for simply readers like many of these I think sonnet would work?”

## Background

Will has a degree in English Literature and a work history selling cars and cable TV advertising. Technical systems and AI orchestration are not his professional background; he is learning as the system develops and wants to remain an active participant in its direction. Self-directed across trading, systems design, and AI orchestration. (Background clarified by Will, 2026-10-14.)
