# WALTER Filter Specification v0.1

WALTER filters BEFORE routing. Every piece of incoming information passes through Gate 1 (filter) before reaching Gate 2 (classification + routing). Most raw information should die at Gate 1.

---

## Boot Context: What WALTER Loads

Before WALTER can filter, it needs to know what matters right now. At session start, load:

| Source | What To Extract | Purpose |
|--------|----------------|---------|
| `AGENTS/*/STATUS.md` (first 30-50 lines each) | Active thesis, current concerns, confidence levels | Know what each agent is tracking |
| `FORGE/STATUS.md` | Open positions: tickers, direction, stops, expiries | Know what we're exposed to |
| `AGENTS/RED/CALENDAR.md` | Upcoming catalysts with dates | Know what events are imminent |
| `AGENTS/WALTER/design/ROUTING_TABLE.md` | Watched domains and metrics | Know default routing |
| `AGENTS/WALTER/filtered/` (last 48h) | Recently filtered signals | Avoid duplicate processing |
| `AGENTS/WALTER/routed/` (last 48h) | Recently routed signals | Detect duplicates |

This gives WALTER a working model of "what matters right now" without needing to understand the full thesis depth.

---

## Gate 1: The Three Filter Questions

Every incoming piece of information gets three questions. A signal must **fail ALL three** to be filtered out. Passing any one is enough to survive to Gate 2.

### Question 1: NOVELTY — "Do we already know this?"

**Pass (novel):**
- Data point not yet in any agent's STATUS or recent signals
- New development on a known theme (even if theme is old, the development is new)
- Updated numbers that supersede previous data
- Contradicts something we currently believe

**Fail (already known):**
- Same data point routed in the last 48 hours
- Headline restating information already in an agent's STATUS
- Commentary on data we already processed (unless it adds a genuinely new angle)
- Recycled narrative without new facts

**Edge case:** If the same fact arrives from a MORE credible source, let it through as a confidence upgrade on the existing signal — don't treat it as duplicate.

### Question 2: RELEVANCE — "Does this touch anything we're tracking?"

**Pass (relevant):**
- Directly mentions a held position (KRE, WAL, OZK, or any ticker in FORGE/STATUS.md)
- Touches an active thesis domain (labor deterioration, credit stress, Japan carry, energy supply, insurance/shadow)
- Relates to a transmission chain we monitor (LABOR → CARL → REGINALD → repricing)
- Affects a watched metric (HY OAS, CCC OAS, VIX, initial claims, etc.)
- Relevant to an upcoming catalyst in CALENDAR.md
- Could create a new risk vector we haven't considered

**Fail (irrelevant):**
- Market sector we have no exposure to and no thesis about
- Company-specific news for companies outside our universe
- Macro data from regions outside our thesis scope (unless it affects global flows)
- Market commentary that's purely technical/chart-based with no fundamental content

**Edge case:** "Could create a new risk vector" is deliberately broad. When uncertain, pass it through with low confidence. Better to let CARL or RED evaluate and reject than for WALTER to filter something that turns out to matter.

### Question 3: CREDIBILITY — "Is this real and specific enough to act on?"

**Pass (credible):**
- Named, identifiable source (news outlet, data provider, SEC filing, named analyst)
- Contains specific claims: numbers, dates, names, measurable assertions
- Primary source or first-hand reporting
- Official data release (FRED, BLS, Fed, earnings report)

**Fail (not credible):**
- Unsourced rumor or anonymous speculation without specifics
- Pure opinion with no supporting data
- Social media noise without verifiable claims
- Clickbait/engagement-farming framing with no substance
- "Some analysts say" without naming who or citing what

**Edge case:** A credible source making a vague claim still passes — the source credibility carries it. An incredible source making a specific, verifiable claim also passes — the specificity can be checked.

---

## Confidence Scoring Guide

When a signal passes Gate 1, WALTER assigns a confidence score (0.0–1.0) before routing.

| Score Range | Meaning | Typical Characteristics |
|-------------|---------|------------------------|
| **0.8–1.0** | High confidence | Official data, primary source, directly measurable, specific and verifiable |
| **0.6–0.8** | Solid | Named credible source, specific claims, consistent with other signals |
| **0.4–0.6** | Moderate | Credible source but interpretive, or specific but from less established source |
| **0.3–0.4** | Low — passes filter but flagged | Single source, unconfirmed, or relevance is indirect. Flag uncertainty to recipient. |
| **<0.3** | Below threshold — filtered out | Unless one of the three gate questions produced a strong pass |

**Adjustment factors:**
- +0.1 if corroborated by second independent source
- +0.1 if consistent with existing agent thesis
- -0.1 if contradicts established data (could be real, but needs higher bar)
- -0.1 if source has history of unreliable reporting
- +0.2 if official government/central bank data release

These are guidelines, not formulas. WALTER uses judgment informed by these factors.

---

## The Kill Log

Filtered signals go to `AGENTS/WALTER/filtered/kill_log.tsv`:

| Column | Description |
|--------|-------------|
| `Date` | ISO8601 timestamp |
| `Origin` | Where the information came from |
| `Summary` | One-line description of what was filtered |
| `Failed_Gate` | Which filter question(s) failed: `novelty` / `relevance` / `credibility` / `all` |
| `Confidence` | Estimated confidence at time of filtering |
| `Notes` | Optional — why this was a close call, if it was |

**Format:**
```
Date	Origin	Summary	Failed_Gate	Confidence	Notes
2026-04-07T14:30:00Z	Reuters	Oil prices steady amid quiet trading	relevance+novelty	0.15	No position, no thesis impact
2026-04-07T15:00:00Z	Twitter/@unknown	"Big bank about to fail"	credibility	0.05	No source, no specifics
```

**Purpose:** Audit trail for tuning. Review weekly: did we filter anything that turned out to matter? If yes, adjust criteria.

---

## Routed Signal Log

Signals that pass Gate 1 and get routed are logged to `AGENTS/WALTER/routed/route_log.tsv`:

| Column | Description |
|--------|-------------|
| `Date` | Timestamp |
| `Signal_ID` | SIG-W-YYYYMMDD-NNN |
| `Origin` | Source |
| `Summary` | One-liner |
| `Precedence` | FLASH/IMMEDIATE/PRIORITY/ROUTINE |
| `To` | Action recipient |
| `Info` | Info recipients |
| `Confidence` | Score assigned |

**Purpose:** Track what was routed, detect if signal volume is trending up (tighten filters) or down (check if pipeline is working).

---

## Tuning Rules

### When to TIGHTEN the filter (let less through):
- Agents report inbox overload or unread signals piling up
- Route log shows >15 signals/day sustained (for our scale)
- Kill log audits show filtered signals rarely mattered
- Alert fatigue indicators: agents stop acknowledging IMMEDIATE signals

### When to LOOSEN the filter (let more through):
- Kill log audit reveals filtered signals that later proved important
- Route log shows <3 signals/day sustained (pipeline may be too tight)
- Major regime change (new positions, new thesis, new risks) — expand relevance scope
- Pre-catalyst windows — lower threshold in days before major events

### Default posture: START LOOSE
For the first 2 weeks of operation, bias toward routing. It's easier to tighten a filter that's letting too much through than to recover from one that killed a critical signal. Calibrate from experience.

---

## Full Pipeline Summary

```
Raw Information Arrives
        │
   ┌────▼────┐
   │  GATE 1  │  FILTER: Novel? Relevant? Credible?
   │  FILTER  │  All three fail → Kill Log
   └────┬────┘
        │ passes
   ┌────▼────┐
   │  GATE 2  │  CLASSIFY: Urgency axis + Resource axis
   │ CLASSIFY │  Safety net override check
   └────┬────┘
        │
   ┌────▼────┐
   │  GATE 3  │  ROUTE: Action vs Info recipients
   │  ROUTE   │  Precedence assignment, AIG groups
   └────┬────┘  Conflict detection, MINIMIZE check
        │
   ┌────▼────┐
   │ DELIVER  │  Write standardized signal to agent inboxes
   │          │  Log to route_log.tsv
   └─────────┘
```

---

*v0.1 — April 7, 2026*
