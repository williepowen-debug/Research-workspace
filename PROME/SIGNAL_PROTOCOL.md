# Signal Processing Protocol

**Owner:** PROME
**Purpose:** Process raw inbound signals from Will into structured packages for sub-agents.
**Last Updated:** 2026-03-09

---

## Role Division

**PROME = sifter + packager.** Extract the fact, identify the domain, state the thesis connection, pre-stage KB fields, package for delivery. Stay light — don't load agent context.

**AGENT = domain expert + integrator.** Receives the package, knows their own KB/VX/thresholds, decides how to integrate (new row, update existing, change status, discard). Agent assigns final ID, DerivedFrom, and Vectors.

**PROME does NOT:** Read the agent's KB before routing. Decide which row to update. Make integration decisions for the agent.

---

## Signal Package Template

```markdown
# Signal: [one-line description]

**ID:** SIG-YYYY-MM-DD-NNN
**Date Observed:** YYYY-MM-DD
**Date Processed:** YYYY-MM-DD
**Urgency:** 🔴 URGENT / 🟡 STANDARD / 🟢 BACKGROUND

## Source
- **Who:** [handle, outlet, filing body]
- **Type:** [WIRE / INSTITUTIONAL / FILING / MSM / SOCIAL / OSINT / WILL / AGENT]
- **Quality:** [Admiralty digraph — e.g., B2 = Usually Reliable + Probably True]

## Raw Fact
[The actual data point or claim. Verbatim quote if possible. No interpretation.]

## Prome Analysis
- **Thesis Connection:** [1-2 sentences — why this matters to the agent's domain]
- **Confidence:** [HIGH / MEDIUM / LOW / SPECULATIVE]
- **Contradicts:** [none / existing prediction or KB reference if known]

## KB Staging
- **Suggested Group:** [from VOCABULARIES.tsv NETWORK_GROUPS]
- **Suggested Entity:** [canonical entity name]
- **Epistemic:** [EMPIRICAL / ESTIMATE / ASSUMPTION]
- **Stale_By:** [date or condition]

## Suggested Action
[Concrete: update KB row X, check VX-Y threshold, compare to prediction Z, create new KB row]

## Cross-Agent
- **Primary:** [agent name + why]
- **Secondary:** [agent names + why]
- **Suggested Vectors:** [VX IDs if known, otherwise blank for agent to assign]

## Attachments
[none / path to saved media if relevant]
```

---

## Source Type Categories

| Type | Definition | Examples |
|------|-----------|----------|
| **WIRE** | Real-time news wires | Bloomberg, Reuters, AP, AFP |
| **INSTITUTIONAL** | Research firms, multilaterals, rating agencies | Coface, IMF, BIS, Moody's, S&P |
| **FILING** | Official government/regulatory releases | SEC, BLS, DOL, Fed, Treasury |
| **MSM** | Mainstream media with editorial layer | NYT, WSJ, FT, CNN, BBC |
| **SOCIAL** | Twitter/X verified analysts, commentators | @DeItaone, @Rory_Johnston |
| **OSINT** | Open source intelligence (defense/geo) | @BabakTaghvaee1, @cirnosad |
| **WILL** | Will's own observation or analysis | Direct input via Telegram |
| **AGENT** | Another agent's outbox signal | HERMES delivery, agent outbox |

---

## Admiralty Scale Reference

**Source Reliability:**
- A = Completely Reliable
- B = Usually Reliable
- C = Fairly Reliable
- D = Not Usually Reliable
- E = Unreliable
- F = Cannot Be Judged

**Information Credibility:**
- 1 = Confirmed by Other Sources
- 2 = Probably True
- 3 = Possibly True
- 4 = Doubtful
- 5 = Improbable
- 6 = Cannot Be Judged

Combined: e.g., B2 = Usually Reliable source + Probably True information.

---

## Urgency Categories

| Level | Criteria | Action |
|-------|---------|--------|
| 🔴 **URGENT** | Threshold breach, position-affecting, thesis-changing | Spawn agent immediately |
| 🟡 **STANDARD** | Important, new information, but not time-critical | Inbox for HERMES delivery or next check-in |
| 🟢 **BACKGROUND** | Confirmatory, context-building, structural | Inbox, low priority |

---

## Processing Workflow

### When Will Sends Signal(s)

**Step 1: Extract** — What is the actual fact? Strip narrative/opinion. If image: describe factually.

**Step 2: Assess** — Source quality (Admiralty), novelty (new vs confirmation), urgency (threshold impact?).

**Step 3: Route** — Primary agent (1-2 max). Cross-agent FYI. NEXUS if multi-domain convergence.

**Step 4: Stage KB Fields** — Suggest Group, Entity, Epistemic, Stale_By, Conf. Pre-chew so agent can integrate fast.

**Step 5: Package** — Write to `AGENTS/{AGENT}/mail/inbox/SIG-{YYYY-MM-DD}-{NNN}.md`

**Step 6: Deliver** — Urgent = spawn immediately. Standard/Background = inbox for HERMES.

### Batch Processing
1. Process all signals first (extract + assess each)
2. Present summary to Will: "[N] signals, [agents], [urgent ones]"
3. Will confirms or redirects
4. Package and deliver

---

## Delivery

- **File location:** `AGENTS/{AGENT}/mail/inbox/SIG-{YYYY-MM-DD}-{NNN}.md`
- **Processed signals:** Agent moves to `mail/inbox/processed/` after integration
- **Numbering:** SIG-{YYYY-MM-DD}-{NNN}, sequential within the day starting at 001
- **Tracking:** Log signal IDs in daily notes (memory/YYYY-MM-DD.md)

---

## Media / Attachments

- **Don't save raw screenshots** unless they contain data (charts, tables, trade flows). Agents spawn as text-only.
- **Do save** data-rich visuals (charts with numbers, flow diagrams, maps) to `media/signals/` with signal ID prefix.
- **Always describe** visual content in the Raw Fact field — the text IS the signal for the agent.

---

## What Makes a Good Signal Package

✅ Agent can act on it cold — no clarification needed from Prome
✅ Fact separated from interpretation — agent adds their own analysis
✅ Thesis connection explicit — agent knows WHY they got this
✅ KB fields pre-staged — agent can create a row almost immediately
✅ Source traceable — agent can verify if needed
✅ Suggested action concrete — not "look into this" but "check against VX-X threshold"

---

## Anti-Patterns

❌ Forwarding raw screenshots/articles without extraction (dumping)
❌ Reading agent's full KB before routing (agent's job)
❌ Routing to every agent "just in case" (pick 1-2 primary)
❌ Interpreting ambiguous data as definitive (flag ambiguity)
❌ Holding urgent signals for batch (route immediately)
❌ Leaving Source Quality as "unknown" (always assess, even if F6)
