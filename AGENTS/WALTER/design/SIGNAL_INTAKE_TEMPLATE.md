# Signal Intake Spec — Template

**Instructions for agents:** Copy this template to your agent directory as `SIGNAL_INTAKE.md`. Fill in every section with your domain-specific needs. This file tells the routing system exactly what information you need, how urgently, and what to ignore. You own this file — update it when your thesis evolves, thresholds shift, or new vectors emerge.

**Where it lives:** `AGENTS/<YOUR_NAME>/SIGNAL_INTAKE.md`

**Who reads it:** The signal routing agent reads all intake specs at boot to build routing rules. Your spec is your subscription — if it's stale or missing, signals may be mis-routed or delayed.

**Who maintains it:** You do. Review when:
- Your thesis version changes
- A major threshold is breached (update the level)
- A new vector enters your domain
- You keep getting signals you don't need (add to exclusions)
- You missed a signal you should have received (add to intake)

---

## How to fill this out

### 1. Header

```
# <AGENT_NAME> — Signal Intake Spec

**Owner:** <AGENT_NAME> | **Consumer:** Routing agent | **Last Updated:** <date>
**Domain:** <1-line description of your domain>
```

### 2. Priority Levels

Use these three levels. Map every signal category to exactly one.

| Priority | Meaning | Expected Delivery |
|----------|---------|-------------------|
| 🔴 IMMEDIATE | Thesis-level, time-sensitive. Could change a position or probability estimate. | As soon as detected |
| 🟠 SAME DAY | Important context. Informs your analysis but doesn't require instant action. | Within the trading day |
| 🟡 WEEKLY BATCH | Background. Useful for tracking trends but low urgency. | Batched and delivered weekly |

### 3. Signal Categories by Priority

For each priority level, list the **specific** categories of information you need. Be concrete — not "economic data" but "Japan CPI (national and Tokyo core)." Group related items under descriptive subheadings.

Example structure:

```
## 🔴 IMMEDIATE

### <Subheading — e.g., Policy Decisions>
- <Specific signal type>
- <Specific signal type>

### <Subheading — e.g., Market Thresholds>
- <Specific signal type with level>

## 🟠 SAME DAY

### <Subheading>
- <Specific signal type>

### Cross-Agent Signals
- <AGENT_NAME>: <what signals from that agent you want forwarded>

## 🟡 WEEKLY BATCH

- <Signal type>
- <Signal type>
```

**Tips:**
- If you're unsure about priority, ask: "Would I change a position or probability within 4 hours of receiving this?" If yes → 🔴. If no but same day → 🟠. Otherwise → 🟡.
- Cross-agent signals go under 🟠 SAME DAY unless they involve a threshold breach, in which case 🔴.

### 4. Keyword Patterns

List terms the routing system can use for automated pattern matching. Three tiers:

```
## KEYWORD PATTERNS

**High confidence (almost always relevant to you):**
<term>, <term>, <term>, ...

**Medium confidence (relevant in context):**
<term>, <term>, <term>, ...

**Low confidence (only if domain-specific):**
<term>, <term>, <term>, ...
```

**Tips:**
- High confidence = if this word appears, it's probably for you. Names of key people, institutions, instruments in your domain.
- Medium confidence = relevant if the surrounding context connects to your domain. Industry terms, secondary players.
- Low confidence = common words that only matter when combined with your domain. E.g., "oil price" is low-confidence for a Japan agent — only relevant if Japan-specific.

### 5. Exclusions — What NOT to Send

Just as important as what you want. List categories that seem like they might be in your domain but aren't, or that belong to another agent.

```
## WHAT NOT TO SEND

- <Category> (→ <correct agent if known>)
- <Category>
- <Category>
```

### 6. Active Thresholds

The specific numerical levels you're watching **right now**. This is the most perishable section — update it whenever a level is breached or your focus shifts.

```
## ACTIVE THRESHOLDS

| Metric | Level | Direction | Why It Matters |
|--------|-------|-----------|----------------|
| <metric> | <number> | Above/Below/At | <1-line reason> |
```

**Tips:**
- "Direction" means: does the signal fire when the metric goes ABOVE, BELOW, or reaches this level?
- "Why It Matters" helps the routing agent understand urgency. "MOF intervention trigger" is better than "important level."
- Remove thresholds that are no longer active. A stale threshold wastes routing attention.

---

## Checklist Before Submitting

- [ ] Header has your name, domain, and date
- [ ] Every signal category is assigned exactly one priority level
- [ ] Keyword patterns cover your core domain terms
- [ ] Exclusions list prevents obvious mis-routes
- [ ] Active thresholds have current levels (not stale)
- [ ] Cross-agent signals section lists what you want forwarded from other agents
- [ ] You've reviewed SAM's SIGNAL_INTAKE.md as a reference example

---

*Template v0.1 — April 9, 2026. Maintained by WALTER.*
