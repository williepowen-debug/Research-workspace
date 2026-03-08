# Signal Processing Protocol

**Owner:** PROME
**Purpose:** Process raw inbound signals from Will into structured packages for sub-agents.

---

## Role Division

**PROME = sifter + packager.** Extract the fact, identify the domain, state the thesis connection, package for delivery. Stay light — don't load agent context.

**AGENT = domain expert + integrator.** Receives the package, knows their own KB/VX/thresholds, decides how to integrate (new row, update existing, change status, discard).

**PROME does NOT:** Read the agent's KB before routing. Decide which row to update. Make integration decisions for the agent.

---

## When Will Sends a Signal

Will sends raw material via Telegram: screenshots, articles, tweets, data points, charts, observations. Can be messy, partial, or ambiguous. Prome's job:

### Step 1: Extract
- What is the **actual fact or data point**? Strip narrative, opinion, framing.
- If it's a screenshot/image: describe what it shows factually.
- If ambiguous: state what it MIGHT mean, flag the ambiguity.

### Step 2: Assess
- **Source quality:** Who said this? How reliable? (Use Admiralty scale A-F for source, 1-6 for information)
- **Novelty:** Is this new information, or confirmation of something we already track?
- **Urgency:** Does this approach or breach a threshold? Could it change a position?

### Step 3: Route
- **Primary agent:** Who owns this domain? (1-2 agents max)
- **Cross-agent FYI:** Does this connect domains? Flag for NEXUS if so.
- **Thesis connection:** State in 1-2 sentences why this matters to OUR thesis. The agent shouldn't have to guess why they're getting this.

### Step 4: Package
Write to `AGENTS/{AGENT}/mail/inbox/SIG-{YYYY-MM-DD}-{NNN}.md`:

```markdown
# Signal: [one-line description]

**Date:** YYYY-MM-DD
**Source:** [who/where — handle, publication, filing, etc.]
**Source Quality:** [Admiralty digraph, e.g., B2]
**Received via:** [Will/Telegram, HERMES, agent outbox, etc.]

## Raw Fact
[The actual data point or claim. Verbatim quote if possible. No interpretation.]

## Thesis Connection
[Why Prome thinks this matters — 1-2 sentences. Connect to the agent's domain explicitly.]

## Suggested Action
[What the agent might do: update KB row X, check against VX-Y threshold, compare to prediction Z, write analysis, etc. These are SUGGESTIONS — agent decides.]

## Cross-Agent
[If this signal touches other agents' domains, name them and why. Agent can forward via outbox if they agree.]
```

### Step 5: Deliver
- **Urgent (threshold-approaching, position-affecting, thesis-changing):** Spawn agent immediately with signal reference in task.
- **Non-urgent (confirmatory, background, file-for-later):** Leave in inbox for HERMES delivery or next scheduled check-in.
- **Multi-agent:** Write to primary agent's inbox. If NEXUS-relevant, note in signal for NEXUS pickup.

---

## Batch Processing

When Will sends multiple signals at once:
1. Process all signals first (extract + assess for each)
2. Present summary to Will: "Here's what I found — [N] signals across [agents]. [urgent ones] need immediate routing."
3. Will confirms or redirects
4. Package and deliver

---

## What Makes a Good Signal Package

✅ **Agent can act on it cold** — no need to ask Prome for clarification
✅ **Fact is separated from interpretation** — agent adds their own analysis
✅ **Thesis connection is explicit** — agent knows WHY they got this
✅ **Source is traceable** — agent can verify if needed
✅ **Suggested action is concrete** — not "look into this" but "check against VX-LAB-1.04"

---

## Signal Numbering

Format: `SIG-{YYYY-MM-DD}-{NNN}`
- NNN = sequential within the day, starting at 001
- Track in daily notes (memory/YYYY-MM-DD.md)

---

## Anti-Patterns

❌ Forwarding raw screenshots/articles to agents (that's dumping, not processing)
❌ Reading the agent's full KB to decide routing (that's the agent's job)
❌ Routing to every agent "just in case" (pick 1-2 primary)
❌ Interpreting ambiguous data as definitive (flag ambiguity, let agent + Will decide)
❌ Holding signals for batch when they're urgent (route immediately)
