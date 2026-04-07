# COP.md — Template & Design Rationale

**Purpose:** This document defines the structure of COP.md before building it with real data.
**Design goal:** Will reads it in 30 seconds and knows where we are. Agents read it at boot and know what's happening outside their domain.

---

## Design Principles Applied

1. **One screenful** — ~40-50 lines max. If it scrolls twice, it's too long.
2. **Domain-organized, not chronological** — readers jump to what they care about.
3. **Hierarchy first** — FLASH at top, routine at bottom, always.
4. **Same format every time** — readers spend zero effort on the container.
5. **Convergence is surfaced** — grouped events, not separate entries.
6. **Deltas marked** — △ prefix on changed entries since last update.
7. **Staleness flagged** — domains with source data >48h old marked [stale].
8. **Network mode visible** — header shows NORMAL or MINIMIZE level.

---

## Section-by-Section Plan

### SECTION 1: Header (4 lines)
```
# COP — Common Operating Picture
**Updated:** 2026-04-07 16:30 UTC | **WALTER** | Mode: NORMAL
**Network Status:** 🔴🔴 CRITICAL — [one-sentence editorial assessment]
```

Purpose: Timestamp + network mode + one-line editorial assessment.

**Mode indicator** (from Military Messaging MINIMIZE protocol):
- `Mode: NORMAL` — all signals flowing, full COP
- `Mode: MINIMIZE` — high-load regime, only PRIORITY+ signals processing, COP may omit routine domains
- `Mode: FLASH ONLY` — crisis, only FLASH items on COP, everything else deferred

The editorial assessment is WALTER's highest-value judgment call. Examples:
- "Oil-consumer-credit transmission chain firing simultaneously. Earnings in 14 days."
- "Quiet. No threshold crossings since Apr 3. Counter-signals strengthening."

This line tells Will whether to read carefully or skim.

---

### SECTION 2: FLASH / IMMEDIATE (0-5 lines, only when active)
```
## ⚡ IMMEDIATE
- BRENT: Kharg Island struck — 90% Iran exports at risk. Trump deadline 8PM tonight. [Apr 7]
- CARL+BRENT: Gas $4.12 breakpoint FIRED + oil surge = consumer squeeze accelerating. [Apr 7]
```

Rules:
- Only items requiring action or awareness RIGHT NOW
- Disappears entirely when nothing is urgent (section omitted, not left empty)
- Max 5 items. If more than 5 things are FLASH, we're in MINIMIZE mode and the COP says so.
- Each item: DOMAIN: fact, quantified. [date]

---

### SECTION 3: Convergence Events (0-3 items)
```
## Convergence
- **Oil→Consumer→Credit chain** [3 channels]: BRENT oil surge ($141 physical) → CARL gas $4.12 breakpoint → LIQUID HY OAS monitoring. Chain is firing but credit lag not yet confirmed. [Apr 7]
- **Earnings convergence** [4 names]: WAL/OZK/ZION/EGBN all report Apr 20-22. REGINALD 8-channel thesis at test point. [Apr 6]
```

Rules:
- WALTER's single most valuable output — signals from different domains pointing at the same cause
- Must trace CAUSAL mechanism, not just topical overlap
- Includes how many channels are involved and whether the chain is confirmed or pending
- Disappears when no convergence detected

---

### SECTION 4: Domain Status (the main body, ~15-25 lines)
```
## Domains

△ **ENERGY** 🔴🔴🔴
Dated Brent $141 physical, futures $110. Kharg struck. 9-11M bpd disrupted. SPR failed. Trump deadline tonight. [Apr 7]

**LABOR** 🔴
JOLTS inverted 0.91, deepening. NFP +178K masks LFPR collapse (61.9%). UI exhaustion $650M/mo, peak $930M July. [Apr 6]

△ **CONSUMER** 🔴🔴
Gas $4.12 breakpoint fired. CC 90+ DQ 12.70% (92% GFC). Student loan 7.7M default. GDPNow 1.3%. [Apr 7]

**BANKING** 🔴🔴🔴
8-channel convergence on regionals. Leveraged loans -34% YoY. BCRED gate exceeded. Earnings Apr 20-22. [Apr 6]

**JAPAN** 🔴🔴 [stale — last SAM update Apr 2]
USD/JPY 159.81 intervention threshold. JGB 10Y 2.40% breached. Carry unwind 7d: 80%. [Apr 2]

**CREDIT** 🟠
HY OAS 316, tightening. STRONGEST COUNTER-SIGNAL. Credit not confirming stress. Watch for re-breach of 320. [Apr 7]

**PRIVATE CREDIT** 🔴🔴
Stage 2→3 gating. Blue Owl, Ares, Apollo, Blackstone all affected. $4.6B+ trapped. [Apr 6]

**ADVERSARIAL** (RED)
77% confidence. Buffer depletion framework. HY OAS tightening is strongest bull case. Thesis window Jul-Oct. [Apr 5]
```

Rules:
- Organized by DOMAIN (not by agent) — because a domain can span multiple agents
- Each domain: status indicator, 1-3 sentences, key numbers, date of last update
- **△ prefix** on any domain that changed since last COP update — Will's eye goes straight to these
- **[stale]** flag on any domain whose source data is >48h old — prevents false confidence in outdated info
- If nothing changed since last COP update, just the indicator and "No change."
- Domains with higher status indicators sort higher (but after FLASH and Convergence)
- RED/adversarial gets its own line — always visible, always honest

---

### SECTION 5: Counter-Signals (2-4 lines)
```
## Counter-Signals
- HY OAS 316 tightening — credit markets NOT confirming stress [Apr 7]
- NFP +178K — employment channel still holding [Apr 4]
- Staffing canaries (RHI/KFRC) showing sequential improvement [Apr 3]
```

Rules:
- What's NOT going our way. Intellectual honesty.
- Keeps RED's function visible on the COP
- Short list — just the active counter-signals, not every possible bull case

---

### SECTION 6: Catalysts (3-5 lines)
```
## Upcoming Catalysts
- **TODAY Apr 7:** Trump Iran deadline 8PM ET
- **Apr 10:** CPI March
- **Apr 16-22:** Regional bank earnings (ZION 20, WAL/OZK 21, EGBN 22)
- **May 1:** BOJ meeting (hike probability ~35-40%)
- **May 6:** JOLTS March release
```

Rules:
- Next 30 days only
- Date, event, one-line significance
- Sorted chronologically
- Max 8 items — if more, prioritize by thesis relevance

---

### SECTION 7: Positions Exposure (3-5 lines)
```
## Exposure
KRE ~$4.9K (9.4%) | WAL ~$4.4K (8.5%) | OZK ~$2.1K (4%) | TLT ~$1.5K (3%) | APO ~$1.7K (3.3%) | IWM ~$1.3K | Other puts ~$2.3K
Longs: AAPL $20.3K (39%) | CF $1.2K | FXY $231 | TBT $491
Cash: $10.5K (20%)
```

Rules:
- Not detailed positions — that's FORGE
- Just enough to see: where are we exposed, how concentrated, how much cash
- Will should be able to glance and know "we're 80% deployed, heavy in regional bank puts"

---

### SECTION 8: Footer (2 lines)
```
---
*COP maintained by WALTER. Detail: AGENTS/WALTER/signals/ | Positions: FORGE/STATUS.md | Agent STATUS files: AGENTS/<NAME>/STATUS.md*
```

Tells readers where to go for more detail. Pointers, not content.

---

## What's NOT on the COP

- Historical context (how we got here) — that's STATUS files
- Detailed position P&L — that's FORGE
- Research in progress — that's agent workbooks
- Full signal content — that's signals/ archive
- Agent-to-agent coordination — that's inboxes/outboxes
- Methodology or thesis justification — that's thesis docs

---

## Update Protocol

1. WALTER boots → reads all agent STATUS files + FORGE
2. Compares current state to last COP
3. Identifies: threshold crossings, convergence, deltas, new catalysts
4. Rewrites COP.md (full rewrite, not append — it's a snapshot, not a log)
5. If anything is FLASH: Telegram ping to Will

COP.md is OVERWRITTEN each update, not appended. It's the current picture, not a history. History lives in git and the signal archive.

---

## Size Budget

| Section | Target Lines |
|---------|-------------|
| Header | 4 |
| FLASH/IMMEDIATE | 0-5 |
| Convergence | 0-6 |
| Domains | 15-25 |
| Counter-Signals | 2-4 |
| Catalysts | 3-8 |
| Exposure | 3-5 |
| Footer | 2 |
| **TOTAL** | **29-59** |

Target: 40 lines on a normal day. Under 30 on a quiet day. Never over 60.

## Markers Reference

| Marker | Meaning | Source |
|--------|---------|--------|
| △ | Changed since last COP update | Cognitive load research (Prompt 8) |
| [stale] | Source data >48h old, may be outdated | ATC cognitive load (Prompt 3) |
| Mode: NORMAL/MINIMIZE/FLASH ONLY | Network operating mode | Military MINIMIZE protocol (Prompt 2) |

---

*Design document — April 7, 2026*
