# Prompt 10 Distilled: Trading Desk Information Flow — What We Keep

**Source discipline:** Institutional trading operations (risk dashboards, Bloomberg Terminal, sell-side research distribution, squawk boxes, crisis protocols)
**Core question answered:** How do professional trading operations manage information overload — prioritize, display, compress, escalate, and shift modes between normal and crisis?

---

## The Big Idea: Single Pane of Glass + Management by Exception

Trading desks solved our exact problem: too much data, too many sources, decisions needed now. Their answer is two principles working together:

1. **Single Pane of Glass (SPoG):** One unified view showing everything that matters. Not 15 screens — one. The COP is our SPoG.

2. **Management by Exception:** Don't review everything. Only surface deviations from expected tolerances. If a metric is within bounds, it's invisible. If it breaches, it screams.

Our translation: The COP doesn't list every metric every agent tracks. It shows what CROSSED A THRESHOLD or CHANGED. "No change" domains get one line. Breaches get prominence.

---

## Five Patterns to Implement

### 1. The Inverted Pyramid Dashboard (Risk Desk Pattern)

Risk dashboards organize information in three layers — same principle as our COP:

| Layer | Risk Dashboard | COP.md |
|-------|---------------|--------|
| **Top: Status** | "Are we within our limits?" Aggregate VaR vs. capital buffers | Header: Network Status 🔴🔴🔴 + one-line editorial assessment |
| **Middle: Trends** | How risk evolved over the session, comparison to norms | Domains: what changed, convergence events, delta markers |
| **Bottom: Detail** | Granular position-level data, counterparty exposures | Footer: pointers to FORGE, signals/, agent STATUS files |

**The Golden Triangle:** Eye-tracking shows users scan top-left first (F-pattern). The most critical information goes there. Our COP already does this — FLASH/IMMEDIATE is at the top, exposure summary at the bottom.

**Semantic coloring is strict:** Red = breach/negative. Green = compliance. Neutral = categorical. No decorative colors. Our status indicators (🔴🟠🟡🟢) follow this principle.

### 2. The ADViCE Compression Framework (Morning Call Pattern)

Trading floor morning calls compress complex research into actionable briefings using ADViCE:

| Principle | Morning Call | COP Entry |
|-----------|-------------|-----------|
| **Conclusion-oriented** | Stock name + recommendation in first 2 sentences | Domain + status + key fact in first line |
| **Differentiated** | How this differs from consensus | What CHANGED — the delta, not the baseline |
| **Validated** | Supported by independent research | Source agent + confidence language |
| **Easy to consume** | Jargon minimized, insights quantified | Numbers not adjectives. "$141" not "very high" |

This is a checklist for writing COP entries. Each domain entry should pass all four checks.

### 3. The Escalation Matrix (Pre-Approved Action Paths)

Trading desks pre-define escalation paths so that when a threshold is hit, the response is automatic — no deliberation needed:

| Level | Trading Desk | Our System |
|-------|-------------|------------|
| **L1 Operational** | Routine troubleshooting, minor issues | ROUTINE signals — COP entry, no action needed |
| **L2 Tactical** | Resource reallocation, budget adjustments | PRIORITY signals — agent processes at next boot |
| **L3 Strategic** | Major scope pivots, client churn risk | IMMEDIATE — primary agent + Will notified |
| **L4 Executive** | C-suite for existential risks | FLASH — all relevant agents + Will + Prome immediately |

**The key insight:** The escalation matrix "kills decision paralysis by giving teams pre-approved paths for action." When HY OAS crosses 320, WALTER doesn't need to think about what to do — the response is pre-defined in the routing table. This is why we built the safety net triggers.

### 4. Regime-Based Mode Switching (Market Regime Pattern)

Trading desks formally classify market regimes and adjust behavior for each:

| Regime | Trading Desk Response | Our Equivalent |
|--------|----------------------|---------------|
| Bull Quiet | Normal sizing, standard stops | Mode: NORMAL — full COP, all signals flowing |
| Bear Volatile (VIX > 25) | Sizes reduced >50%, capital preservation | Mode: MINIMIZE — PRIORITY+ only, routine deferred |
| Crisis | War Room: 20-min huddles, concentrated authority, binary decisions | Mode: FLASH ONLY — COP shows only critical items |

**The 20-Minute Huddle pattern:** "Present, challenge, decide, document." Every conversation ends binary: act, defer, or cancel. This is how Will should interact with the COP during crisis — scan it, decide, move.

**The 13-week cash flow model as "nerve center":** In a cash crisis, desks reconcile to yesterday's bank ledger cent-for-cent. Translation: during our crisis mode, FORGE positions must be live and accurate, not 13-day-old stale data.

### 5. Two-Channel Alerts (Bloomberg Pattern)

Bloomberg separates alerts into two categories:

| Channel | Bloomberg | Our System |
|---------|----------|------------|
| **ALRT (Market)** | Custom conditions: price moves, news keywords, economic events | Signal-level alerts: threshold crossings, catalyst triggers |
| **MON (Enterprise)** | Health of data feeds, connectivity, system status | System-level awareness: which agents are stale, what data is missing |

**Our gap:** We have the ALRT equivalent (signals about market events) but not the MON equivalent (system health monitoring). The [stale] flag on COP domains is a start, but a more systematic "system health" check would catch: which agents haven't updated in >48h? Is FORGE data current? Are any STATUS files contradicting each other?

---

## The Conflicting Signals Problem (Bayesian Pattern)

Portfolio managers use Bayesian updating to handle conflicting analyst opinions. The key question: **how likely is this signal under competing hypotheses?**

When CARL says consumer stress is cracking and RED says credit is holding, WALTER shouldn't pick one — WALTER should present both with diagnostic weight:
- How likely is HY OAS tightening if the bear thesis is correct? (Possible — credit lags)
- How likely is HY OAS tightening if the bull case is correct? (Very likely — stress contained)

The COP already handles this by having both domain entries AND the counter-signals section. But the Bayesian framing adds rigor: counter-signals that are MORE likely under the bull hypothesis should get MORE weight, not less.

---

## Failure Modes That Will Bite Us

### 1. Metric Soup
Too many visuals competing for attention → analysis paralysis. Managers spend 20 minutes cross-referencing charts instead of deciding.
**Our risk:** COP grows beyond 60 lines, every domain has 3 sentences, convergence section has 5 items.
**Fix:** Hard line limit. Cut ruthlessly. If it doesn't pass ADViCE (conclusion-oriented, differentiated, validated, easy to consume), it doesn't make the COP.

### 2. Lack of Context
Dashboard showing "Sales: $50,000" without comparison forces the user to ask "Is that good?"
**Our risk:** COP entry says "HY OAS 316" — is that high? Low? Moving which direction?
**Fix:** Every number on the COP needs context: direction, threshold, comparison. "HY OAS 316, tightening from 342. Threshold: 320." Now Will knows: it was higher, it's coming down, and it's 4bps from the trigger.

### 3. Liquidity Evaporation (Flash Crash Pattern)
In the 2010 flash crash, both humans and algorithms stopped trading simultaneously — liquidity vanished. Information flow was fine; it was the RESPONSE to information that failed.
**Our risk:** During a crisis, all agents fire signals simultaneously and WALTER can't process them all. Or all agents go silent because they're overwhelmed.
**Fix:** MINIMIZE mode. During crisis, WALTER processes FLASH only, defers everything else. And the "minimum signal rate" check from ATC (Prompt 3) — if an agent goes silent for >48h during an active crisis, flag it.

---

## What We Don't Need From Trading Desk Research

- BlueMatrix/Tier1 CRM integration details — no sell-side distribution
- MiFID II compliance and regulatory reporting — no regulatory obligations
- FIX/SWIFT connectivity monitoring — no trading infrastructure
- Greeks (Delta, Gamma, Vega) calculation — not running options models
- Plotly/Streamlit/Redis technical stack — we use markdown files
- Hand signals and pit trading protocols — no physical trading floor
- Bayesian update formula and mathematical notation — we need the principle, not the math
- SOX/GDPR compliance frameworks — no regulatory audit requirements
- Bloomberg Terminal feature-switch deployment methodology — not building software

---

*Distilled from PROMPT10_TRADING_DESK_MASTER.md | April 7, 2026*
