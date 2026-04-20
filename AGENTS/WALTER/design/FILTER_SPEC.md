# WALTER Filter Specification v0.3

WALTER filters BEFORE routing. Every piece of incoming information passes through a **pre-gate System-Critical bypass**, then **Gate 1** (the two hard kill gates: Novelty + Relevance), then **a soft credibility check** that adjusts confidence before reaching Gate 2 (classification + routing). Most raw information should die at Novelty or Relevance.

> **v0.2 note (Apr 11, 2026):** This is the v1 unified filter model, reconciled from v0.1's 3-question form and CHECKLIST v0.3's 3-check form. Both earlier versions were half-right — v0.1 had Credibility but no System-Critical bypass and used the wrong kill logic (fail-all-three); CHECKLIST had System-Critical and the right kill logic but was missing Credibility entirely. **This model is provisional.** Schedule review after 10+ real signals have passed through OR 30 days from Apr 11, whichever comes first. Adjust based on what we observe in practice.

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

## Pre-Gate: System-Critical Bypass

Before any filter runs, check for system-critical conditions. If any trigger fires, **skip all filter gates, route FLASH immediately, even on duplicates.**

**Bypass triggers:**
- A held position is directly named and materially affected (stop-loss breach, material news, liquidity issue)
- Any safety net override trigger: VIX spike >5 intraday, HY OAS +25bps single session, correlation break in held-position pair, bid-ask widening on held positions, 2+ agents flag same theme within 24h
- A pre-registered falsification rule in any agent's STATUS.md is pierced (e.g., RED's "HY OAS <300 sustained 5d → exit HYG" rule)
- Will explicitly flags a signal as FLASH or IMMEDIATE via Telegram

**Why bypass everything:** When the stakes are position-level or system-level, a duplicate reminder is cheaper than a missed trigger. Normal novelty/relevance filtering would incorrectly kill a critical second-hit.

**Empirical note (v0.3 update Apr 20 2026):** zero FLASH signals across the first 51 dispatches (Apr 11–Apr 20). Bypass has never fired in production. Two interpretations: (a) trigger criteria are appropriately strict (FLASH-worthy events genuinely rare), or (b) criteria miss events that should have fired. The Apr 21 catalyst day (WAL/ZION earnings + Iran ceasefire expiry + 8-channel Iran cluster) is the first real test.

**Pre-Apr-21 bypass reaffirmation:**
- WAL or ZION gap-down >5% premarket on Q1 miss → bypass-trigger (held-position material news)
- KRE 1-day drop >3% intraday → bypass-trigger (proxy-position liquidity + sector stress)
- Iran kinetic-interdiction of US naval vessel (distinct from boarding a commercial ship) → bypass-trigger (safety net: correlation break across oil/equity/USD)
- HY OAS single-session +25bps → bypass-trigger (explicit safety net spec)
- VIX +5 intraday → bypass-trigger (explicit safety net spec)
- Will explicit FLASH flag via Telegram → bypass-trigger

If bypass fires Apr 21, route FLASH immediately + Telegram alert + BOARD archive. Do NOT run through Gate 1.

If no bypass triggers fire → proceed to Gate 1.

---

## Gate 1: Hard Kill Gates (Novelty AND Relevance)

Both Novelty AND Relevance are **hard kill gates**. A signal must pass BOTH to survive to the credibility check. Failing either one kills the signal. This is AND logic, not pass-any.

### Gate 1a — NOVELTY: "Do we already know this?"

**Pass (novel — continues to Gate 1b):**
- Data point not yet in any agent's STATUS or recent signals
- New development on a known theme (even if theme is old, the development is new)
- Updated numbers that supersede previous data
- Contradicts something we currently believe
- Same fact from a MORE credible source than we had before (treat as a confidence upgrade on the existing signal, not a duplicate kill)

**Fail (already known — KILL, log to kill_log.tsv):**
- Same data point already routed in the last 48 hours
- Headline restating information already in an agent's STATUS file
- Commentary on data we already processed without genuinely new angle
- Recycled narrative without new facts

### Gate 1b — RELEVANCE: "Does this touch anything we're tracking?"

**Pass (relevant — continues to credibility check):**
- Directly mentions a held position (any ticker in FORGE/STATUS.md)
- Touches an active thesis domain (labor deterioration, credit stress, Japan carry, energy supply, insurance/shadow, private credit, stagflation, etc.)
- Relates to a transmission chain we monitor (LABOR → CARL → REGINALD → repricing)
- Affects a watched metric (HY OAS, CCC OAS, VIX, initial claims, USD/JPY, JGB 10Y, etc.)
- Relevant to an upcoming catalyst in any agent's calendar
- Could create a new risk vector we haven't considered

**Fail (irrelevant — KILL, log to kill_log.tsv):**
- Market sector we have no exposure to and no thesis about
- Company-specific news for companies outside our universe
- Macro data from regions outside our thesis scope (unless it affects global flows)
- Market commentary that's purely technical/chart-based with no fundamental content

**Edge case:** "Could create a new risk vector" is deliberately broad. When uncertain, pass to Gate 1c and let credibility set the confidence — better to let agents reject at low confidence than to kill something that turned out to matter.

---

## Credibility Check: Confidence Modifier (NOT a hard kill)

Credibility does NOT kill signals outright. Instead, it drives the confidence score, and only kills via the minimum confidence floor.

### How credibility maps to confidence

| Credibility tier | Characteristics | Initial confidence band |
|------------------|-----------------|-------------------------|
| **High** | Named + specific + primary source OR official data release (BLS, FRED, SEC, central bank, earnings report) | 0.75–1.0 |
| **Moderate** | Named source OR specific claims, but not both; or secondary reporting of a primary source | 0.50–0.74 |
| **Low** | Anonymous source with specific verifiable claims, OR named source with vague claims | 0.30–0.49 |
| **Floor-fail (KILL)** | Unsourced rumor + vague claims + no specifics, OR unverifiable content with no credible anchor | <0.30 → KILL via confidence floor |

Then apply the confidence adjustment factors (see Confidence Scoring Guide below). If the FINAL confidence after adjustments falls below 0.30, the signal is killed as unreliable (log to kill_log.tsv with `Failed_Gate: credibility-floor`).

### Why this is a confidence modifier, not a hard kill

An unsourced-but-relevant rumor about a held position is still actionable — at low confidence, with flags. Killing it outright loses information. The floor (<0.30) catches the truly unreliable. The middle tiers (0.30–0.74) pass through to Gate 2 with their confidence attached so agents can decide based on their own thresholds.

**Example:** An anonymous X post claiming WAL is about to announce a capital raise — novel (not in any STATUS), relevant (directly names a held position), credibility Low (anonymous + specific). Resulting confidence ~0.35. Under the old v0.1 "fail-all-three" logic this might still route because it passed Novelty and Relevance. Under v0.2 it still routes — but now explicitly at confidence 0.35 with a credibility flag, so RED or REGINALD can weigh it accordingly.

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

### Default posture: BALANCED (Apr 20 2026 onward)

**START LOOSE retired.** Original posture applied Apr 7-20 (2-week calibration window plus extension); retired by Filter v2 Segment A after 51 dispatches through route_log and 18 kill_log entries showed zero obvious false positives and reasonable route calibration.

**Current posture (v0.3):**
- No default bias toward routing or killing. Apply the tuning rules above as primary guide.
- In pre-catalyst windows (≤72h before WAL/ZION/OZK earnings, Fed meetings, CPI/NFP, Iran ceasefire expiry, BOJ decisions), shift temporarily toward LOOSE on the relevant domain — false-negatives cost more than false-positives when a catalyst is imminent.
- During low-information stretches (no catalysts, stable macro, quiet geopolitics), shift toward TIGHT — let the signal density set by throughput trend itself.
- Review monthly from Apr 20 going forward. Filter v3 trigger: 30 days from Apr 20 (~May 20) OR next 50 dispatches, whichever first.

---

## Full Pipeline Summary

```
Raw Information Arrives
        │
        ▼
   ┌─────────────┐
   │  PRE-GATE    │  SYSTEM-CRITICAL check:
   │  BYPASS      │  Held position hit? Safety net trigger?
   │              │  Falsification rule pierced? Will FLASH?
   └───┬──────┬───┘
       │      │
    no │      │ yes → Skip to ROUTE as FLASH
       ▼      │       (bypass all filter gates)
   ┌─────────────┐
   │  GATE 1a     │  NOVELTY: Already known?
   │  NOVELTY     │  Fail → Kill Log
   └───┬─────────┘
       │ pass
       ▼
   ┌─────────────┐
   │  GATE 1b     │  RELEVANCE: Touches our thesis?
   │  RELEVANCE   │  Fail → Kill Log
   └───┬─────────┘
       │ pass
       ▼
   ┌─────────────┐
   │  CREDIBILITY │  Soft check → sets confidence score
   │  SOFT        │  Conf <0.30 after adjust → Kill Log
   └───┬─────────┘
       │ pass (with confidence attached)
       ▼
   ┌─────────────┐
   │  GATE 2      │  CLASSIFY: Urgency axis + Resource axis
   │  CLASSIFY    │
   └───┬─────────┘
       │
       ▼
   ┌─────────────┐
   │  GATE 3      │  ROUTE: Action vs Info recipients
   │  ROUTE       │  Precedence assignment, AIG groups
   └───┬─────────┘  Conflict detection, MINIMIZE check
       │
       ▼
   ┌─────────────┐
   │  DELIVER     │  Write signal to agent inboxes
   │              │  Log to routed/route_log.tsv
   └─────────────┘
```

---

*v0.3 — April 20, 2026 — Filter v2 Segment A. Retired "START LOOSE" default posture (2-week calibration window expired; 51 dispatches + 18 kills reviewed, zero obvious false positives) and replaced with BALANCED posture — tuning rules as primary guide, context-shift toward LOOSE pre-catalyst and TIGHT during low-information stretches. Added empirical note in Pre-Gate Bypass section (zero FLASH in 51 dispatches) + Pre-Apr-21 bypass reaffirmation (6 specific triggers for WAL/ZION earnings + Iran catalyst day). Filter v3 trigger: ~May 20 or next 50 dispatches.*
*v0.2 — April 11, 2026 — Unified filter model v1 (provisional). Added System-Critical pre-gate bypass. Restructured Gate 1 as AND-logic: Novelty AND Relevance both hard kill (was: fail-all-three pass-any-one). Credibility converted from a hard gate to a confidence modifier with a 0.30 floor kill. Schedule review after 10+ signals or 30 days from Apr 11. Reconciles the divergence with SIGNAL_PROCESSING_CHECKLIST which had a different 3-check model.*
*v0.1 — April 7, 2026*
