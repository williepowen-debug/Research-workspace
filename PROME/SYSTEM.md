# Prome System Map
**Created:** 2026-05-08 21:28 ET  
**Owner:** Prome  
**Purpose:** Current architecture map for Prome’s operating system — what each file owns, what to trust, and where future Prome should look first.

---

## North Star

Prome’s system exists to turn public-data research into disciplined decisions without losing context, duplicating facts, or making ad hoc calls under pressure.

Core rule:

> Put facts in the owner file. Other files should point to it, not copy it.

---

## Boot Trust Stack

### Always injected in main sessions

| File | Trust | Role |
|---|---|---|
| `AGENTS.md` | High | Agent roster, transmission chains, spawn restrictions. |
| `SOUL.md` | High | Prome identity/tone. |
| `USER.md` | High | Will preferences and operating style. |
| `MEMORY.md` | High for curated long-term facts; check freshness | Long-term discoveries, thesis framework, system architecture notes. |
| `HEARTBEAT.md` | High for current state if recently updated | Cold-boot current-state orientation. |

### Read at boot / when resuming

| File | Current status | Role |
|---|---|---|
| `PROME/BOOT.md` | Useful but partly stale | Boot sequence, doc ownership, protocol reminders. Some agent/spawn details may lag `AGENTS.md`. |
| `PROME/HANDOFF.md` | Fresh as of 2026-05-08 18:12 ET | Clear/new-session handoff. Best narrative of latest work. |
| `PROME/SCRATCH.md` | Stale / lower trust | Ephemeral session handoff. Should be rewritten once system state stabilizes. |
| `PROME/TODAY.md` | Stale | Daily catalysts/checklist. Do not rely without refresh. |
| `PROME/STATUS.md` | Stale | Operational status. Do not rely without refresh. |
| `PROME/TOSCANINI/QUEUE.md` | Stale | Proposal queue. Do not rely without refresh. |

---

## Current Decision-Support Layer

This is the new lightweight decision system.

```text
Event Pre-Build
→ Position Snapshot
→ Action Card
→ Live Event Read
→ Decision Log
→ HEARTBEAT update
```

| File / directory | Owner | Role |
|---|---|---|
| `PROME/DECISION_FLOW.md` | Prome | Architecture/spec for the decision workflow. |
| `PROME/action-cards/` | Prome | Event-specific branch-to-action cards. Temporary/current decision artifacts. |
| `PROME/action-cards/FSK_MAY11_ACTION_CARD.md` | Prome | First concrete action card; maps FSK branches to allowed/forbidden actions. |
| `PROME/TRADE_DECISIONS.md` | Prome | Permanent log of Will’s trade/portfolio decisions and outcomes. |
| `PROME/POSITIONS.md` | Prome | Current position snapshot, sizing, P/L, OCR caveats. |
| `HEARTBEAT.md` | Prome/root | Current-state pointer layer. Should reference action cards, not contain full action logic. |

Design principle:

- Domain files classify events.
- Position files describe exposure.
- Action cards map event branches to allowed actions.
- Decision logs record what Will actually decided.
- HEARTBEAT orients future Prome.

---

## Domain / Research Layer

| Area | Owner | Role |
|---|---|---|
| `AGENTS/<NAME>/STATUS.md` | Domain agent | Agent current state, domain facts, pending work. |
| `AGENTS/<NAME>/domain/` | Domain agent | Durable domain research and frameworks. |
| `AGENTS/<NAME>/domain/sources/*_PREBUILD_*.md` | Domain agent / Prome when preparing catalyst | Event pre-builds with thresholds and read order. |
| `AGENTS/<NAME>/inbox/` | Domain signal routing | Incoming signals, should be triaged/processed. |
| `FORGE/research/` | Prome / domain-dependent | Thesis research outside a single agent. |
| `FORGE/timing/` | Prome / timing thesis | Timing frameworks, changelog-first thesis files. |

Important current example:

- `AGENTS/BROCK/domain/sources/FSK_PREBUILD_MAY11.md` owns the FSK event framework.
- `PROME/action-cards/FSK_MAY11_ACTION_CARD.md` owns the portfolio/action mapping.

---

## Operational / Orchestration Layer

| File / directory | Role | Trust note |
|---|---|---|
| `PROME/TOSCANINI/AUTONOMY.md` | What Prome can do freely vs must propose/ask. | Use before ambiguous autonomy calls. |
| `PROME/TOSCANINI/PROTOCOL.md` | Proposal mechanics. | Read when presenting proposals. |
| `PROME/TOSCANINI/COMPLETION_SPEC.md` | Required sub-agent completion format. | Use for spawns. |
| `PROME/TOSCANINI/HUNTING.md` | Scoring/ranking work items. | Use when triaging many tasks. |
| `PROME/TOSCANINI/SIGNAL_BATCHING.md` | Multi-signal spawn/routing protocol. | Use for signal batches. |
| `PROME/TOSCANINI/QUEUE.md` | Live proposals. | Currently stale. Refresh before trusting. |
| `PROME/TOSCANINI/WILL_QUEUE.md` | Tasks blocked on Will. | Check if relevant. |
| `PROME/TOSCANINI/DECISIONS.md` | Historical non-trade/system decisions. | Separate from `PROME/TRADE_DECISIONS.md`. |

---

## Tools / Data Layer

| Tool / path | Role | Rule |
|---|---|---|
| `FORGE/tools/market-data/dashboard.py` | Live stress dashboard. | Run before citing current market levels. |
| `FORGE/tools/market-data/fetch.py` | Live prices / FRED series. | Use for individual live data pulls. |
| `FORGE/tools/news-sweep/sweep.py` | Thesis-tagged news sweep + routing. | Prome maintains entity index and WATCH_FOR lists. |
| `dashboard/server.py` | Local web/API dashboard on `:8080`. | Use API endpoints if CLI is inconvenient. |
| `FORGE/tools/filing-watch/` | EDGAR filing monitoring. | Useful for Qs/10-Q catalysts and Call Reports. |

Known current caveat:

- `FORGE/STATUS.md` was flagged stale by inbox signal; do not use it as fresh source until refreshed.

---

## Current Freshness / Trust Table

| File | Status | Use? |
|---|---|---|
| `HEARTBEAT.md` | Fresh enough, updated May 8 from dashboard/handoff; needs timestamp refresh later | Yes, current orientation. |
| `PROME/HANDOFF.md` | Fresh May 8 18:12 ET | Yes for latest narrative. |
| `PROME/POSITIONS.md` | Fresh May 8 14:17 ET from screenshots | Yes, but brokerage screen is execution ground truth. |
| `PROME/DECISION_FLOW.md` | Fresh May 8 | Yes. |
| `PROME/action-cards/FSK_MAY11_ACTION_CARD.md` | Fresh May 8 | Yes for FSK workflow. |
| `PROME/TRADE_DECISIONS.md` | Fresh scaffold | Yes, log future decisions here. |
| `PROME/TODAY.md` | Stale Apr 17 | No, refresh before use. |
| `PROME/STATUS.md` | Stale Apr 17 | No, refresh before use. |
| `PROME/SCRATCH.md` | Stale/legacy | Use only as historical hint; rewrite soon. |
| `PROME/TOSCANINI/QUEUE.md` | Stale | No, refresh before presenting proposals. |
| `FORGE/STATUS.md` | Stale per Prome inbox signal | No, refresh before using. |

---

## Current Live Architecture Gaps

1. **Generic action-card template missing**
   - Needed: `PROME/action-cards/TEMPLATE.md`.
   - Purpose: prevent every new card from becoming bespoke.

2. **Regional-bank action card missing**
   - Needed because bank puts are larger live exposure than private-credit residuals.
   - Scope: Call Reports, KRE/WAL/OZK/HBAN/ZION expiry triage, hold/cut/roll framework.

3. **Stale operational docs**
   - `PROME/TODAY.md`, `PROME/STATUS.md`, `PROME/SCRATCH.md`, `PROME/TOSCANINI/QUEUE.md` need refresh or explicit demotion.

4. **FORGE status stale**
   - Inbox signal requested `FORGE/STATUS.md` refresh.
   - This affects `/COP.md` and any dashboard/system status that references FORGE state.

5. **Git sync blocked**
   - `git pull --rebase` previously blocked by unstaged/untracked local changes.
   - Do not commit/stash without Will approval.

---

## Recommended Next Architecture Steps

1. Create `PROME/action-cards/TEMPLATE.md`.
2. Create regional-bank Call Report / expiry-triage action card.
3. Refresh or retire stale `TODAY.md`, `STATUS.md`, `SCRATCH.md`, and `QUEUE.md`.
4. Resolve git working-tree blocker with Will-approved commit/stash strategy.
5. Update `PROME/BOOT.md` so the boot sequence reflects the new decision-support layer.

---

## Safety / Autonomy Reminders

- Internal reads/organization/editing are generally okay when Will asks.
- External sends/posts/public actions require asking first.
- Trade proposals require Will’s explicit approval. Never execute.
- Use `trash` over `rm` for deletion.
- Do not spawn persistent/managed agents: CARL, REGINALD, SAM, RED, BRENT.
- Before citing live prices, run the market-data dashboard or fetch tool.
