# ORCHESTRATION PLAYBOOK
**Created:** 2026-06-26 | **Updated:** 2026-08-10 (+§Mode C — forum canonized as the third mode, Will-approved in-session; template = `FORUM/CHARTER_TEMPLATE.md`) | Prior: 2026-07-09 (+§Standard Fable session — session-design guide, Will-directed; Codex cross-vendor lane; verification tiers; record-vs-reality rule) | **Owner:** Prome | **Companion to:** `PROME/ORCHESTRAL_LAYER_DESIGN.md` (fleet-scan/ranking layer)
**Purpose:** Operating rules for running a multi-agent session. Read when Will says "let's orchestrate" / before spawning >1 agent. Born from the 2026-06-26 debrief: the orchestration layer works, but we were paying live-orchestration prices for fan-out work and absorbing a fragile-concurrency tax.

---

## The core rule: MODE-SPLIT

Every multi-agent task is one of two modes. **Decide the mode BEFORE spawning.** Mixing them is the #1 source of wasted cost and operator-attention tax.

| | **Mode A — Fan-out execution** | **Mode B — Live orchestration** |
|---|---|---|
| **Tool** | `Workflow` (deterministic script) | teams-mode `Agent` (named) + `SendMessage` |
| **Use when** | tasks are independent, templated, no Will-decision between steps, collection/synthesis specifiable up front | cross-agent dependency resolves mid-flight, Will-decisions between rounds, next step depends on what an agent surfaces |
| **Coordinator role** | author script, collect, synthesize | route, decide, relay, iterate |
| **Concurrency** | serialized by the runtime → no git index races | N concurrent committers → index races (mitigate) |
| **6/26 examples** | the 5 arch self-reports, 5 inbox sweeps, 5 Tier-1 applies | gate-cluster ownership pivot, BROCK↔SHADE handoff, the CARL amendment |

**Decision test — use Mode A (fan-out) if ALL are true:**
- [ ] tasks are independent (no agent needs another's mid-flight output)
- [ ] the prompt is templated/near-identical across agents
- [ ] no Will-decision is needed *between* sub-steps
- [ ] you can specify the collection + synthesis up front

**If ANY is false → Mode B (live).** When unsure, default to Mode A for the parallel-identical part and Mode B only for the decision spine.

> **A third mode exists since 2026-08-07: Mode C — forum** (deliberative synthesis in a shared append-only tree). It is NOT a variant of A or B — see §Mode C below for when it applies.

> **6/26 lesson:** ~70% of the agent-work (self-reports, sweeps, applies) was Mode-A work run as Mode B — I babysat 5 live agents, chased idle ones, and ate index races for tasks a Workflow would have serialized and collected cleanly. Mode-split that work and the same output is ~2× cheaper and quieter.

---

## Most sessions are HYBRID

Don't pick one mode for the whole session. The common shape:

1. **Scout inline** (Prome, no agents) — list the work, find the owners, scope the diff.
2. **Fan-out the parallel part** (Mode A / Workflow) — fire N templated tasks, collect to files, synthesize.
3. **Live-orchestrate the decision spine** (Mode B) — route emergent findings, present Will-decisions, handle handoffs/amendments.

6/26 done right would have been: scout → **Workflow** the triage + sweeps + arch-reports + Tier-1 applies → **live** only for the gate-cluster routing, the BROCK/SHADE spin-ups, and the addendum approval.

---

## Mode C — Forum (deliberative synthesis; canonized 2026-08-10, Will-approved)

**Born 2026-08-07, Will-convened.** Neither fan-out (the posts are interdependent) nor live orchestration of PROME's decision spine (the deliberation itself IS the work): N domain agents write into one append-only tree (`FORUM/YYYY-MM-DD_<slug>/`), read each other's posts the moment they land, and converge on a jointly-owned synthesis with dissent on the record. PROME orchestrates phases, verifies load-bearing figures at primaries, and is sole committer.

**Use when** (any one): the question is cross-desk AND the desks' claims or kills may be **correlated** (shared antecedents, same-kill detection) · the bloc must **pre-register before a catalyst cluster** · Will convenes a **system review**. **Not for:** single-owner questions (packet/spawn), routine grading (owner session), calendar ritual. **Will convenes; PROME may propose.**

**Why it earns its cost — evidence from the first 3 sessions (94 posts, full-read assessment 8/10):**
- **Same-day peer replication kills false numbers before they ship:** OSPREY re-extracting HAWK's STEO PDF between draft and FINAL changed the Will-facing headline from "the absorber is gone" to "a dated convexity window" (war-theaters `03_synthesis/03_OSPREY_…`). As a packet, the wrong version reaches Will.
- **Shared-antecedent detection needs the whole post-set on disk at once:** three desks citing one HY series / one ORACLE packet as "independent" confirmation is only computable with simultaneous visibility (fin-conditions FINAL §7 → BOND's C-36 concession, 4 legs → 2 evidence types, same day).
- **Blind Phase 0 manufactures real independence:** LIQUID's judgmental ~1.5 effective signals vs HENRY's measured 1.3, computed blind — the only genuinely independent convergence in that forum.
- **The dissent structure produces author-self-vetoes** — forum 1: three authors vetoed their own proposals; forum 3: the two sharpest catches were against the synthesis author's own draft.
- **Owner records reverse aggregate labels:** the TERRY routing question, nearly settled 2-for-exemption on aggregate data, reversed by the owner's own consumption record in-thread (forum 1 `06_proposals/07`).

**Measured costs (same assessment):** restatement volume (~1.5MB / 94 posts / 4 days; the headline finding restated ≥8×) and **candidate accumulation feeding Will's ruling backlog** — the pruning rule (template rule 8) exists for this. Compression to Will-facing form is PROME's job and does not scale past a few sessions/week.

**Mechanics canon = `FORUM/README.md` + `FORUM/CHARTER_TEMPLATE.md`** (binding: blind Phase 0 · declared cross-read order · one concur/dissent per desk · PROME verification post · in-place FINAL revision · no live levels in charters · pruning rule · dated withdrawal test on the verdict · rulings-record post closes the tree). Concurrency: participant git barred, PROME commits at phase boundaries — zero index races across 3 sessions, incl. against concurrent Will-owned sessions.

---

## Model tiering (Fable-orchestrated fleet — Will-approved 2026-07-08)

When PROME runs on a top-tier model (Fable 5), **judgment concentrates up, volume delegates down.** Domain agents spawn as subagents/workflows with explicit `model:` overrides instead of Will launching separate interactive sessions. This is the old "research on Sonnet, synthesis on Opus" cost doctrine, one tier up.

| Tier | Model | Work |
|---|---|---|
| Orchestrate/decide | PROME on Fable 5 | Synthesis, adversarial verify of load-bearing claims, trigger-adjudication sign-off, regime/HEARTBEAT/DOCKET/canon writes, cross-agent routing, everything Will-facing |
| Domain judgment | `sonnet` (default) | Domain-agent spawns: evidence gathering + first-pass adjudication, written to their own dirs |
| Load-bearing exception | `opus` | Adjudications where a wrong call moves positioning (e.g., a fired trigger's re-arm call) |
| Mechanical | `haiku` | Fetches, grep/inventory sweeps, staleness checks, formatting, workflow readers |

**Quality rails — stricter, not looser, at lower tiers:**
- **Tight task packets:** every spawn states scope, files to read first (own `CLAUDE.md` + `STATUS.md` — subagents don't auto-load them), today's date explicitly, deliverable format, deliver-before-idle. Web tools need ToolSearch loading — say so in the prompt.
- **Structured outputs** (Workflow `schema`) wherever the result is data.
- **Load-bearing findings get a Fable-level primary-source check** before touching canon, firing a trigger, or routing cross-agent — mandatory, not judgment-call.
- **Escalation valve:** contradictions / ungrounded hedging from a lower-tier agent → PROME pulls that specific question up inline; fallback = re-run higher (still cheaper than running everything big).
- **Git:** spawned agents commit only their own `AGENTS/<NAME>/` dirs (or leave commits to PROME's closeout sweep). Never shared/root files.
- **Context economics:** PROME delegates file-dump reading (Explore/agents) and keeps Fable tokens for synthesis — that's where the cost asymmetry pays.

**Not delegated down, ever:** trigger sign-off, X1/regime state changes, routing decisions, Will-approvals, Telegram sends, HEARTBEAT/DOCKET/GATES writes.

---

## The standard Fable session (session-design guide — Will-directed 2026-07-09; evidence: the 7/8 nine-spawn live-event run + the 7/9 five-agent wave)

The target shape for a PROME-on-Fable working session. Everything here is the *how-to-run-it* layer on top of §Mode-split and §Model tiering — cite those, don't restate.

### Lifecycle
1. **Boot + declare** (`PROME/BOOT.md` in full). End the declaration with: regime + live tape, the top catalyst (especially one that already printed while offline — say that FIRST), pending decisions, blockers.
2. **Co-plan with Will.** Will sets direction; PROME proposes the wave as a table (task · agent · model · why-now), marking what's *sequenced* (true dependency only) vs *parallel*. Get ONE launch approval for the whole wave — not per-agent drip.
3. **Launch.** Parallel spawns go in one message. Sequence only on real data dependency (7/9: TERRY waited for BOND because arm-#1 *was* BOND's verdict; VIOLET/LIQUID ran parallel because nothing coupled them).
4. **While agents work: PROME verifies, and otherwise stays quiet** (§discipline 2). Fable time goes to primary-checking verdicts as they land — not to narrating progress or relaying idle pings.
5. **Canon the same hour a verdict verifies** — HEARTBEAT amendment, DOCKET row, GATES.tsv state flip. Never batch canon to closeout; a crash loses it.
6. **Synthesize at milestones, batched.** Lead with the outcome; N agent reports → one synthesis.
7. **Closeout** (`PROME/CLOSEOUT.md` tier): write-back tail, GATES.tsv states current, auto-memory for new *classes* (not instances), safe-push sweeps every agent's local commits.

### Spawn packet template (proven 7/8–7/9 — every field earned its place)
1. Identity line: *"You are X, the <domain> agent in Will's fleet. PROME spawned you."* + **today's date AND time** + repo root.
2. **Boot-read list** — own `CLAUDE.md` + `STATUS.md` + task-specific files/inbox items *by path* (subagents auto-load nothing).
3. Scoped task **with the tape numbers PROME already has** (don't make a Sonnet agent re-fetch what Fable already verified) — and with traps flagged (e.g. 7/9 LIQUID: "do NOT grade the pre-reg early, it's conditioned on Friday's close").
4. Domain rules restated in one line: numbers > narrative · source + date every claim · no trade recommendations · **no files outside `AGENTS/<NAME>/`**.
5. Deliverables, exactly: files in own dir → **pathspec commit recipe from repo root** (incl. the pre-commit `git status -- AGENTS/<NAME>/` check) → do-not-push → **word-capped SendMessage summary (≤150-200 words)**.
6. The deliver-before-idle line, verbatim (§discipline 1).
7. Web tools note when relevant: *"NOT autoloaded — ToolSearch 'select:WebSearch,WebFetch' first."*

### Verification tiers (Fable's core job — where the model premium pays)
| Claim class | Bar |
|---|---|
| Moves canon / gates capital / fires-or-resolves a trigger | **Primary-source verify, mandatory, BEFORE any canon write** (7/9: BOND's auction figures re-pulled from the TreasuryDirect API — exact match — before HEARTBEAT/DOCKET/TERRY moved) |
| Domain judgment with registered re-arm thresholds | Read the reasoning; spot-check only if surprising (7/9: LIQUID's SpaceX-idiosyncratic verdict — sound structure + registered thresholds = no escalation) |
| Mechanical / hygiene / process claims | Trust commit evidence — verify via `git log`/`git status`/`ls`, not re-doing the work (7/9: VIOLET's "no packet-build commit exists" reproduced in one git command) |

### Record-vs-reality rule (born 7/9 — TWO instances in one day)
**Canon never asserts an artifact exists until it's been verified on disk** (`ls` / git history). "Routed" ≠ "built"; intent ≠ artifact. The 7/6 "fire-card PRE-BUILT" was an inbox packet with no card file for 3 days; the KB-VIO-110 packet-build was a fired gate with no execution for 7. Corollaries: registered action-gates → `PROME/GATES.tsv` **the same session they're approved** ([[finding_fired_gate_needs_owner_independent_ledger]]); when a spawn reports "X was never actually created," git-verify, then fix the canon that claimed otherwise.

### Codex cross-vendor lane (validated ×2 on 7/9)
- **A tool with a charter, not a fleet agent** — no ROSTER entry, no inbox, no STATUS. Invoke via the codex plugin (rescue subagent for delegated investigation; review commands for diffs). **Standing contract = `PROME/codex/CHARTER.md`** (harness home, built 7/9 Will-directed): every spawn prompt cites it near the top — *"Read `PROME/codex/CHARTER.md` first and operate under it."* The charter carries the delivery contract (final message = FULL findings, never idle without delivering — the 7/9 chase lesson), mode rules (read-only default; fix-mode path scope = scripts/ + FORGE/tools/ only), output format/severity rubric, and repo orientation.
- **Best use:** silent-failure hunting on harness/infra code, and **pre-arm red-team of decision-rail logic** (fire-cards, gate definitions) — the places same-vendor blind spots cost most; run it the night BEFORE a gate grades, so fixes can still be pre-registered.
- **Economics:** runs on Will's OpenAI subscription → zero Anthropic tokens for the review itself; PROME pays only the verification pass.
- **Same trust bar as any agent:** findings verified against live code before endorsement (7/9: 22 findings across 2 runs — all real, one scenario overstated). PROME applies fixes under pathspec discipline. **Findings archive = `PROME/codex/findings/`** (PROME-written, with dispositions).

### Fable-context economics (the orchestrator's context IS the session's scarce resource)
- Agents deliver **word-capped summaries + file pointers**, never dumps; PROME reads verdicts and verifies claims — it does not read domain files it can delegate.
- Idle notifications are no-ops: never relayed to Will, never responded to beyond housekeeping.
- Division of labor, fixed: **Will** = direction, launch approval, trade decisions, shared-root commit scope, off-repo truth. **PROME** = wave design, packets, verification, canon, synthesis. **Spawns** = everything else.
- If Fable spend looks heavy, the lever is *fewer/larger batched deliveries* — not reverting the architecture.

---

## Operating disciplines (apply in BOTH modes)

### 1. Report-delivery contract (fixes the chase-the-idle-agent defect)
Every agent's **last action before idling = deliver its result.** Never go idle "holding" without delivering. Two acceptable channels:
- **Live (Mode B):** `SendMessage` the report to the coordinator as the final step.
- **Fan-out (Mode A):** write to a known file (`AGENTS/<NAME>/<TASK>_REPORT.md`) + a ≤120-word reply; coordinator batch-collects. *(Workflow's `schema` option enforces this automatically — the agent's return value IS the structured result.)*

Put this line in every spawn prompt: *"Deliver your result (SendMessage + file) as your final action before idling — do not idle without delivering."*

**Closeout extension (2026-08-15, Will-approved off DAEDALUS's war-triad review):** for a RESIDENT domain-desk session (the agent itself spawned and kept warm across re-task rounds), delivery does NOT end the session — **before final release, PROME injects a closeout leg: "run your own closeout protocol now (derived surfaces and briefs re-stamped — NEXUS_BRIEF, SCRATCH, summary regens, staleness stamps), then enumerate any awaiting-Will / dated-clock / unrouted-proposal items in your tree."** Live orchestration at tempo breaks closeout write-backs: all three 8/15 war desks delivered excellent work AND skipped their derived-surface write-backs (a 5-day-stale NEXUS_BRIEF missing that morning's gate fire; a SCRATCH contradicting the desk's own encode), and ~16 Will-gated asks sat in owner trees with no queue row. The enumeration half feeds PROME's registration sweep — owners enumerate, PROME registers; never grep another desk's tree for its decisions.

### 2. Relay discipline — GO QUIET while agents work
Prome surfaces to Will only: **(a)** a decision Will must make, **(b)** a consolidated result, **(c)** a blocker. **Do NOT relay** idle pings, "holding for X", or per-agent acknowledgments. Batch N agent reports into ONE synthesis, not N relays. *(6/26: dozens of "X is idle / holding" turns were pure operator-attention tax.)*

### 3. Right-size the agent count
The synthesis is the coordinator's job. Don't spawn an agent for work you'll redo. Match N to the *actual* parallelism, not to the number of agents that exist.

### 4. Concurrency / git hygiene
- **Mode A (Workflow) serializes** the agent lifecycle → avoids the shared-`.git/index` race entirely. Prefer it for any write-heavy parallel work.
- **Mode B (live, N concurrent committers)** → index races, dangling deletions, foreign pre-staged files. Mitigations: the canonical **pre-commit `git status -- AGENTS/<NAME>/` check** (root CLAUDE.md), staggered commits, or `isolation: worktree` per agent. A non-trivial Mode-B session is **standing evidence for the separate-clones / worktree migration** (deferred decision — SAM's proposal); log it.

### 5. Triage-first for domain work
Spawn domain agents on a **report-before-execute** mandate so Will directs what gets actioned. Worked well 6/26 — keep it.

### 6. Route to the domain OWNER, not the adjacent agent
Cross-domain findings go to the agent that owns the domain, even if another surfaced it. ([[feedback_route_to_domain_agent]], [[feedback_check_domain_owner_before_messaging]]). 6/26's single biggest value-add: routing the gate-cluster to BROCK (owner) instead of CARL (transmission-adjacent) surfaced 3 more gates + the compounding mechanic + the insurer-lender pathway.

### 7. Proxy/coordinator writes carry the owner's vintage (PAT-112 — DAEDALUS PR#4 ask, PROME-adopted 2026-08-17)
When a coordinator-driven session (forum slate, proxy spawn, fan-out) commits content into an owner's tree WITHOUT running that owner's closeout, do one of exactly two things: **(a)** re-cut the owner's BOTTOM LINE / vintage stamp as part of the same write, or **(b)** stamp the commit message `content-only, owner closeout owed` — which the owner's next boot treats as a due item. Never neither. Why: the 8/10 forum slate wrote into VIOLET/HENRY/LIQUID (and resolved BOND's BND-01) with the result that each desk's dated header no longer covered its newest body content, AND the commits re-armed every git-time staleness fallback — the surfaces read fresher than their own synthesis. ([[finding_hygiene_commit_rearms_the_staleness_lie]] is the same mechanism from the other side.)

---

## Anti-patterns (seen 6/26 — don't repeat)
- **Fan-out work run as live teams-mode** → babysitting, idle-chasing, index races. Use a Workflow.
- **Agents idling without delivering** → wasted round-trips pinging "where's your report?"
- **Relaying every idle notification to Will** → attention tax with no decision content.
- **Amendment racing execution** → I sent an amendment after CARL had already executed → reversions. In live mode, confirm an agent is *holding* (not mid-execute) before sending follow-on scope; or fan-out the corrected task fresh.
- **N agents committing concurrently to the shared tree** → residue/duplicates. Serialize (Workflow) or worktree-isolate.

---

## Quick checklist before spawning
0. **Freshness from GROUND TRUTH, never narrative (Will-directed 2026-08-14):** `python3 PROME/tools/agent_freshness.py --agent <NAME>` — **rc=1 ⇒ STOP: drain the listed from-<NAME> packets out of `PROME/inbox/` and inspect any dirty paths BEFORE writing the brief.** SCRATCH's spawn-queue lines and HANDOFF watch lists are closeout snapshots that rot within hours on multi-window days; a brief written against undrained packets tasks work that may already be Will-ratified (8/14 case: HOMER's encode-confirms sat unread while PROME briefed rows 45/46 as pending — the agent was fresh, PROME's model of it was not). The fleet-wide sweep runs at every boot via `prome_gate` (`--gate` mode); own-surface age is a lower bound, not caught-up proof (`[[finding_freshness_audit_vs_caught_up]]`).
1. **Scout done?** Do I know the work-list, the owners, the diff?
2. **Mode?** Run the decision test → Mode A (fan-out/Workflow) for the parallel-identical part, Mode B (live) only for the decision spine.
3. **Delivery contract** in every prompt? (deliver-before-idle)
4. **Will-decisions identified** up front so I can batch them, not drip them?
5. **Concurrency safe?** Write-heavy parallel → Workflow or worktree, not N live committers.
6. **Go-quiet plan:** what's the *next* thing worth interrupting Will for?

---

## Cross-session coordination (harness `SendMessage`/`ListAgents` — first live use 2026-08-16; governance = `MESSAGING/CROSS_SESSION_MESSAGING.md`)

Independently-launched sessions on the same box can now message each other directly — a THIRD coordination mode beside file packets and teams-mode spawns. **The five rules live in the governance addendum (read it before first use); this section is the choreography.**

**The doorbell pattern (the validated shape — FERT registration, 8/16):**
1. Sender commits the CONTENT as a normal packet/artifact and pushes.
2. Sender messages the doorbell: what landed, the commit, what's unblocked, what's asked.
3. Receiver **verifies the claim at artifacts** (pull; check the commit/files; re-read any ruling being invoked) — a relayed precondition is rule-2 material, never acted on bare.
4. Receiver executes within its own standing authorizations, **names the message trigger + the authorization in its commit**, pushes, and messages back only what unblocks the sender.
5. Anything Will-gated in the chain HOLDS for Will's own word or his verbatim word in a verifiable artifact — a relay never clears it (rule 3). **When relaying gated text for an OK, present from the artifact or verify copy == artifact first** (a drifted convenience copy gets an OK on text that isn't the record).

**When to use which channel:** file packet alone = default (durable, cross-machine, auditable). Packet + doorbell message = when a live counterpart session is blocked on your landing (PAT-047-ordered passes, handoffs, precondition fires). Message alone = pure coordination with zero decision content (status ping, "are you touching file X"). **Never message-alone anything a future session or the other machine needs** — the channel is same-box ephemeral. **Never route market signals here** (WALTER's lane, rule 4). **Cloud receiver ⇒ one-directional** — it cannot reply; read its result in its own transcript/artifacts, never wait on the doorbell's return leg.

**Interrupt hygiene (norm, not machinery):** message only when it unblocks, corrects, or was asked for. Messages consume the receiver's context — a focused mid-grade session owes you nothing mid-round; they drain at its next tool round.

**The discovery step (canonical home = `MESSAGING/CROSS_SESSION_MESSAGING.md` §2 rule 6, Will-ruled 8/16 late; this paragraph is the choreography MIRROR — born here `84509c868`, promoted to canon the same night):** the doorbell only fires if somebody looks — **at packet-commit time, when the packet carries an ASK of, or an answer owed to, a specific agent, run `ListAgents` (~free) and doorbell if that agent's session is live.** The night this channel was ratified, PROME and DAEDALUS ran a full two-round ASK/disposition exchange as live concurrent sessions on pure file packets, and Will hand-carried the coordination between the two open windows — the exact operator-as-relay load the channel had removed hours earlier. Both sessions knew the canon; neither checked for a peer. A channel without a discovery habit is a doorbell nobody rings.

## Two-tier orchestrated-desk model (Will-ruled 2026-08-23, "approved"; record `PROME/proposals/2026-08-23_two-tier-orchestration-pilot-RULED.md` — SINGLE HOME for this workflow; DAEDALUS 5-amendment review folded at encode time)

**The model:** PROME orchestrates desk work through two transports. **TIER = TRANSPORT, NOT CLASS** — the tier describes how the session runs, never the desk's roster class, routing, or obligations; desk obligations are invariant under transport (amendment 5a).

| Tier | Transport | Criterion | Will's access |
|---|---|---|---|
| **Own-window** | Will-launched CC session (`cd AGENTS/<NAME> && claude`) | Work **outlives a PROME session** OR **Will's words land mid-flight** (trade construction, rulings) | Direct — sees it, types into it |
| **Named subagent** | PROME-spawned persistent named agent (Agent tool, `name:`); re-ping via `SendMessage` resumes with context intact, no respawn; quiet when idle costs nothing | **Bounded, completable within PROME's session** (grading, drains, encodes, consumption touches) | Via PROME's task tree + the desk's commits/packets |

**Day-scoped lifecycle:** subagents die with PROME's session (nightly closeout minimum, often sooner for context hygiene). **The repo is the memory; the transcript is intra-day convenience.** A fresh PROME session respawns what it needs and loses nothing — PROVIDED every touch delivered to disk. Between-ping drift is structurally small (short lifespans), with ONE exception the template guards: market/repo state at re-ping.

**Spawn/re-ping template (every tasking carries ALL of these — PAT-046: root canon does not reliably bind spawned agents; the prompt carries the rules):**
1. **FIRST ACTION: read `AGENTS/<NAME>/CLAUDE.md` + `STATUS.md` + your own boot files** — a subagent never launches from the desk dir, so nothing auto-loads.
2. **Full owner session, never a read-only receiver** (§3.5.2): integrate into canonical state and COMMIT before filing anything to `processed/`. **Whole-inbox drain — every sender, not just the triggering item** (rule-6b mandate).
3. **Re-anchor before acting: live data AND re-read your own STATUS + inbox** (amendment 2 — a resumed transcript is a snapshot; repo state moves between touches). On closed-market days: latest closes are final-for-period, cite dated, nothing is live.
4. **Every delivery re-stamps the STATUS header it wrote under** (PROME hardening on PAT-112 — header covers newest content even if PROME dies before the final ping). **The LAST touch runs the desk's own FULL closeout per its protocol** (consumer_check · ledger nudge · orphan check · memory-index check · safe-push); the subagent cannot know which touch is last — **PROME says so in the final ping** (amendment 1).
5. **Commit provenance: subjects lead `<DESK> (orch): ...`** (amendment 3 — keeps desk-cadence instruments honest; `git log -- AGENTS/X/` blindness runs both directions). Pathspec commits, own dir + carve-outs ①②③ only.
6. **⛔ ALL Will-gated surfaces are OUT OF SCOPE** — not just trades: threshold registration, band edits, root/shared docs, roster changes. A subagent hears Will only as PROME's relay, and a relayed word never clears a Will-gated surface (rule 3). A gated need RETURNS to PROME → WILL_QUEUE/GATES on Will's own word (amendment 4). $0 moves; report-before-execute on anything trade-shaped.
7. **Deliver-before-idle:** SendMessage the result to PROME AND write it to your own dir, as the final action before going quiet.
8. **Model: orchestrated-desk subagent sessions spawn `opus` — ⛔ NEVER Fable** (Will-ruled in-session 2026-08-23: *"we need to run these sub-agents as lower model. Lets go with OPUS instead"*, tightened same session: *"cannot spend that much on FABLE sub agents"* — this is the orchestrated-desk override of §Model tiering's sonnet default; haiku stays available for purely mechanical errands; PROME on Fable remains the verify layer for load-bearing findings). ⚠️ **The failure mode is OMISSION: a spawn with no `model:` param silently inherits PROME's Fable — always pass the model explicitly; an omitted model is a defect, not a default.** Each touch's model rides ORCH_LOG's notes column. **Fable-run salvage rule: output already paid for is consumed normally** (committed work, verified residue) — the prohibition is on NEW Fable spawns/resumes, not on reading what exists. Record: the 8/23 wave-1 Fable runs were spawned pre-ruling by omission; both were stopped/replaced on Will's word, their committed output consumed, SAM's uncommitted residue verify-then-integrated by its opus successor.

**Ledger:** every touch logs to `PROME/state/ORCH_LOG.tsv` (authoritative record for orchestrated work; feeds the 8/28 doorbell-soak review — one surface grades both mechanisms; standing post-8/28 reader = fleet_triage when it builds, amendment 5b).

**Failure path (amendment 5b — written so the first real failure runs from a rule, not improvisation):** subagent dies mid-task ⇒ respawn from repo state; check the desk dir for uncommitted residue — **residue is IN-FLIGHT work, not orphaned trash** (`[[finding_dirty_path_means_in_flight_not_orphaned]]`): the respawned desk integrates it, nobody sweeps it.

**PROME closeout hook:** before closing, send each live spawned desk the final run-your-closeout ping, then verify idle + last delivery committed (`PROME/CLOSEOUT.md` pre-closeout step).

## Related
- `PROME/ORCHESTRAL_LAYER_DESIGN.md` — fleet-scan / ranking / revival-proxy layer (the *what to work on*; this doc is the *how to run it*).
- Auto-memory: [[finding_fleet_selfreport_convergence]], [[finding_workflow_concurrency_529]], [[feedback_parallel_spawn_independent_agents]], [[feedback_named_spawn_teams_mode]], [[feedback_warm_parked_agent_collision]].

---

## Orchestration-class fleet memories (fleet-memory embeds — migrated 2026-07-31, Phase-2 restructure)
*One-liners embedded from memory/auto/ (files unchanged); index rows now in memory/auto/INDEX_COLD.md.*

- finding_subagent_escalation_mode_discriminator — Propose-only sub-agents (KOYOMI/KURA/METSUKE pattern) should discriminate escalation handling — money/irreversible blocks on Will; low-stakes/reversible structural applies sane default + logs rationale + flags for veto `[[finding_subagent_escalation_mode_discriminator]]`
- feedback_subagent_prompt_discipline — When spawning research sub-agents, 4 rules to keep returns efficient without over-templating `[[feedback_subagent_prompt_discipline]]`
- finding_subagent_memory_split — "Sub-agent specs should split into <NAME>.md (durable mandate/rubric) + <NAME>_MEMORY.md (dated state — RUN LOG, PENDING, STANDING MONITORS, CALIBRATION, NEXT RUN HINTS); without the MEMORY half, fresh spawns can't self-orient and parent agent must re-brief every spawn" `[[finding_subagent_memory_split]]`
- finding_subagent_baseline_audit — "Sub-agent specs whose job is 'maintain a set' (catalysts, KB rows, trade triggers, signal routes) need explicit baseline-scope audit rubrics, not just incremental-update rubrics. Without baseline audits, the agent extends-from-precedent rather than re-baselines-against-source — and the propagation bug is silent because nothing in the agent's job description surfaces it." `[[finding_subagent_baseline_audit]]`
- finding_subagent_naming_identity_over_functional — Multi-agent systems with named sub-agents should prefer identity-naming (unique per parent — KOYOMI/FASTOW) over functional-naming (shared — CATALYST/WORKBOOK) at current scale; runtime coordination cost outweighs one-time setup cost when both compare `[[finding_subagent_naming_identity_over_functional]]`
- feedback_subagent_propagation_gap — "Sub-agent good work doesn't reliably rise to the parent — at parent closeout, scan sub-agent KB/STATUS for unpropagated facts" `[[feedback_subagent_propagation_gap]]`
- finding_subagent_prefire_date_verification — "For sub-agents maintaining date-keeping sets (catalysts, calendars, predictions), add a STANDING MONITOR that re-fetches source-of-truth for cadence-derived rows within N days of fire date; revise if shifted. Two consecutive BRENT/FASTOW runs caught 2-day errors using this pattern." `[[finding_subagent_prefire_date_verification]]`
- feedback_subagent_web_tools_not_autoloaded — "General-purpose research sub-agents may spawn WITHOUT WebSearch/WebFetch loaded, silently returning no data on web-dependent tasks; confirm tooling in the prompt or do the lookup in-session" `[[feedback_subagent_web_tools_not_autoloaded]]`
- finding_subagent_year_verification — "Before citing any web-pulled metric as load-bearing, confirm the YEAR explicitly from the primary source; aggregator articles silently reference prior-year prints" `[[finding_subagent_year_verification]]`
- feedback_parallel_spawn_independent_agents — When spawning multiple sub-agents whose work doesn't depend on each other, always send them as multiple Agent calls in a single message — never sequentially `[[feedback_parallel_spawn_independent_agents]]`
- feedback_named_spawn_teams_mode — "Naming an Agent spawn via the `name` parameter triggers team-mode (mailbox-based, async, requires SendMessage to direct). Wrong tool for one-shot domain analytical work — use named spawns only for iterative coordination tasks." `[[feedback_named_spawn_teams_mode]]`
- finding_fence_orchestration_live_agent — "Directory-fence teams-mode orchestration against a LIVE agent works, but the fence must be announced to the live session AND its commits watched — a broad-pathspec commit from the live side silently sweeps the orchestrator's in-flight edits into the wrong commit." `[[finding_fence_orchestration_live_agent]]`
- finding_teams_mode_domain_agent_spawn — Teams-mode (named-spawn) works for domain agents like BOND; identity reconstitutes from files. But teammateMode=auto fails to trigger split-pane on WSL2 even inside tmux — set explicit teammateMode=tmux in ~/.claude/settings.json. `[[finding_teams_mode_domain_agent_spawn]]`
- finding_draft_only_teams_spawn — "Teams-mode domain-agent spawn pattern where agent is briefed to draft into proposals/ only, no live state file edits; iterative Will + Prome review via SendMessage across multiple turns before recipient adopts" `[[finding_draft_only_teams_spawn]]`
- finding_teams_mode_iterative_tasks — "Teams-mode SendMessage earns over synchronous Agent spawn when the task is iterative + context-leveraging (refinement loops, multi-round proposal/refine, watching-an-event-resolve); for batch propose-only single-turn work, synchronous spawn is equivalent. Default bias should be SendMessage for iterative; reach for it explicitly because the default mental model is synchronous spawn." `[[finding_teams_mode_iterative_tasks]]`
- feedback_warm_parked_agent_collision — "leaving named teams-mode agents \"warm\" across sessions causes next-session same-name collisions + cleanup-sweep kills; release at closeout or use collision-proof aliases" `[[feedback_warm_parked_agent_collision]]`
- feedback_orchestration_mode_split — multi-agent sessions — split fan-out (Workflow) from live orchestration (teams-mode) before spawning; see ORCHESTRATION_PLAYBOOK `[[feedback_orchestration_mode_split]]`
- finding_workflow_concurrency_529 — "concurrent Workflow runs + live sibling agents overload the account API (529); cap parallelism, degrade to inline/sequential" `[[finding_workflow_concurrency_529]]`
- finding_workflow_agent_unprompted_commit — workflow research subagents have Edit+Bash and can commit to canonical files unprompted; scope them RESEARCH-ONLY or route writes to proposals/ `[[finding_workflow_agent_unprompted_commit]]`
- finding_investigation_routing_discriminator — "route signal-investigation by \"do I need the answer THIS session to make a routing call?\" — yes→inline verify, no→assign a dedicated research agent; a paywalled headline is an investigation POINTER not route-or-kill" `[[finding_investigation_routing_discriminator]]`
- finding_workflow_subagent_repo_sandbox — "Workflow subagents are sandboxed to the repo working tree; pass in-repo paths (not ~/.claude or /tmp) and hardcode script values rather than relying on args binding." `[[finding_workflow_subagent_repo_sandbox]]`
- finding_write_behavior_check_before_agent_tool_run — "Before test-running another agent's tool, grep it for write ops — \"boot kit\" and \"tracker\" scripts mutate their agent's data files, and a verification run becomes an ownership violation" `[[finding_write_behavior_check_before_agent_tool_run]]`
- finding_workflow_scratch_crash_recovery — a crashed /deep-research (or any Workflow) session leaves sub-agent outputs recoverable in /tmp task scratch — salvage before re-running `[[finding_workflow_scratch_crash_recovery]]`
- finding_workflow_rate_limit_resume_recovery — "A /deep-research or Workflow killed mid-run by a session rate limit is recoverable without a full re-run — resume the Workflow from cache (needs args re-passed) + re-spawn any plain-Agent leg that died, with a return-partial guardrail" `[[finding_workflow_rate_limit_resume_recovery]]`
- finding_teams_mode_no_split_pane — Teams mode does not appear to support split-pane visibility on WSL2 even with teammateMode=tmux + TMUX env present; Agent View is the feature that provides the second pane `[[finding_teams_mode_no_split_pane]]`
- finding_batch_extraction_fanout_then_route — "For a large image/document batch (dozens+), split OCR/extraction (mechanical, parallelizable, cheap model) from judgment (dedup/filter/route/verify — the owner keeps this). Fan out N sub-agents to TRANSCRIBE chunks in parallel, then the owner routes on the structured extractions. Keeps fidelity where it matters, keeps the owner's context clean, and is a live instance of role-separation (LOOPS.md Rule 2)." `[[finding_batch_extraction_fanout_then_route]]`
- finding_warm_agent_multiround_sweep — Keep named domain-agent spawns resident across a session and re-task them in escalating rounds (hygiene sweep → approved fixes → deep threads → execution) — each later round is cheap and high-yield because the agent has just re-read its whole domain; validated 4/4 agents, 72 items, 2026-07-11. `[[finding_warm_agent_multiround_sweep]]`
- finding_duplicate_the_decision_changing_finding — "For the ONE finding in a study that actually changes what someone DOES, deliberately run it twice with independent agents. Two independent passes converged on every load-bearing point AND each closed the other's blocked source — and the second pass forced a same-night correction to a recommendation already sent. A strong, well-cited, confident single report is exactly the kind that invites being taken at face value." `[[finding_duplicate_the_decision_changing_finding]]`
- finding_warm_agent_proposal_round — After a task wave, a proposal round — each warm agent proposes its ranked top-3 completable ball-movers, operator picks — produced honest, well-calibrated prioritization (agents self-ranked their own pending hygiene below edge work); 9/9 picked tasks delivered. `[[finding_warm_agent_proposal_round]]`
- finding_scheduled_print_spawn_armed_state_report — Agents spawned ahead of a scheduled release (BLS print, AMC earnings) go idle on a poll timer — indistinguishable from a dropped task unless the spawn prompt REQUIRES an armed-state report before first idle; 4/4 nudges on 7/21 found armed-not-dropped, but only the nudge proved it. `[[finding_scheduled_print_spawn_armed_state_report]]`
- finding_spawn_packet_seed_premise_verification — Coordinator-authored spawn-packet context claims (current time, an agent's ledger state, tool/file ownership) are load-bearing citations, not framing — verify each against ground truth before sending; recipient catches are the backstop, not the design. `[[finding_spawn_packet_seed_premise_verification]]`
