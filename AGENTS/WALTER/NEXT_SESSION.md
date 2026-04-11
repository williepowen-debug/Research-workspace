# WALTER — Next Session Handoff

**Written:** 2026-04-10 (end of session) | **For:** Next WALTER boot
**Read this AFTER STATUS.md and the spawn protocol.** This is the prioritized work list for what to tackle next.

---

## Immediate carryover from last session

These three items were queued but not executed before the break.

### 1. Delete SIG-W-20260410-002 (the duplicate)
Located at `AGENTS/WALTER/outbox/SIG-W-20260410-002-cpi-march-fed-locked.md`. This signal was a CPI-only HENRY-action variant I drafted in error, thinking the spec required separate signals per data release. On re-read, "one file per action recipient" means dispatch mechanics, not content splitting. SIG-001 is the canonical version. Delete this file using `trash` (per CLAUDE.md rule 11).

### 2. Get Will's approval on SIG-001 then dispatch
SIG-W-20260410-001-cpi-umich-stagflation.md is in the outbox. Will needs to read and explicitly approve the SUBSTANCE before it goes to 5 inboxes. The signal applies the dual-precedence pattern:

| Recipient | to: | Precedence | Inbox path |
|-----------|-----|------------|------------|
| CARL | CARL (ACTION) | IMMEDIATE | AGENTS/CARL/inbox/SIG-WALTER-CARL-20260410-cpi-umich-stagflation.md |
| HENRY | HENRY (INFO) | PRIORITY | AGENTS/HENRY/inbox/SIG-WALTER-HENRY-20260410-cpi-umich-stagflation.md |
| RED | RED (INFO) | PRIORITY | AGENTS/RED/inbox/SIG-WALTER-RED-20260410-cpi-umich-stagflation.md |
| LIQUID | LIQUID (INFO) | PRIORITY | AGENTS/LIQUID/inbox/SIG-WALTER-LIQUID-20260410-cpi-umich-stagflation.md |
| SAM | SAM (INFO) | PRIORITY | AGENTS/SAM/inbox/SIG-WALTER-SAM-20260410-cpi-umich-stagflation.md |

**Naming convention** (matches existing usage in HENRY's inbox): `SIG-WALTER-{RECIPIENT}-{YYYYMMDD}-{slug}.md`

**Important:** Each per-recipient file should have its `to:` field updated and its `precedence` set per the table. Body content stays identical. This is the dual-precedence pattern from FORMAT_SPEC.

**Note on freshness:** By the time next session runs, the CPI+UMich signal is already 1+ days old. Gate 3 (timeliness) might fail or downgrade. Re-run the checklist before dispatching — if the news has been digested by the network already, this signal may need to be downgraded to PRIORITY or even archived without push.

### 3. Open question for Will: routing log
Should I append a single row to a new `WALTER/log/routing_log.tsv` recording the dispatch decision? Format would be: `timestamp \t signal_id \t gates_passed \t recipients \t precedence \t safety_net \t notes`. This starts the routing audit trail even before the full infrastructure exists.

---

## Spec reconciliation backlog (in priority order)

These are gaps surfaced during the v0.3 checklist worked example. The CONFIDENCE divergence was already resolved last session — these are the remaining ones.

### Gap A: Header schema divergence (HIGH priority)
SIGNAL_PROCESSING_CHECKLIST.md shows a header with fields `domain` and `conflict_zone` that aren't in SIGNAL_FORMAT_SPEC.md. SIGNAL_FORMAT_SPEC has `timestamp`, `source`, `origin`, `group`, `signal_type`, `resources`, `safety_net`, `word_count` not shown in the CHECKLIST example.

**Recommendation:** SIGNAL_FORMAT_SPEC is the canonical schema. Update CHECKLIST to reference FORMAT_SPEC's full header rather than showing a partial example. Decide whether `domain` and `conflict_zone` should be ADDED to FORMAT_SPEC (they're useful) or DROPPED from CHECKLIST.

**Why this matters:** Same root cause as the confidence divergence. If specs disagree, signals are inconsistent.

### Gap B: Filter model divergence (HIGH priority)
FILTER_SPEC.md Gate 1 has THREE checks: Novelty, Relevance, Credibility.
SIGNAL_PROCESSING_CHECKLIST.md Phase 1 has THREE different checks: Already known, In thesis chain, System-critical.

These overlap but use different categories. CHECKLIST is missing Credibility entirely. FILTER_SPEC is missing the System-critical FLASH bypass.

**Recommendation:** Pick one canonical model. Probably the FILTER_SPEC model is cleaner (Novelty + Relevance + Credibility map well to AP/IC research). Add the System-critical bypass to FILTER_SPEC as a pre-Gate-1 short-circuit. Update CHECKLIST to match.

### Gap C: Domain enum (MEDIUM priority)
CHECKLIST uses: ENERGY, LABOR, CONSUMER, BANKING, JAPAN, CREDIT, PRIV_CREDIT.
ROUTING_TABLE uses: Employment/Labor, Consumer Credit, Bank Earnings/CRE, Funding/Liquidity, Oil/Energy, Japan/BOJ/Yen, Market Structure/Vol, Insurance/Shadow, etc.

**Recommendation:** Establish a canonical domain enum in FORMAT_SPEC and have all docs reference it. Probably 8-12 enum values that everyone uses.

---

## Infrastructure backlog

### Build missing directories
The specs reference these but they don't exist on disk yet:
- `WALTER/log/routing_log.tsv` — routing audit trail
- `WALTER/filtered/kill_log.tsv` — filtered signals (FILTER_SPEC defines this)
- `WALTER/routed/route_log.tsv` — routed signals (FILTER_SPEC defines this)
- `WALTER/queue/` — for MINIMIZE-deferred signals
- `WALTER/signals/` — the durable archive (the COP architecture's "Layer 2")

Until these exist, I can't actually log decisions, can't run a kill log, can't operate the MINIMIZE protocol, and don't have a signal archive.

**Recommendation:** Build them all in one round. Empty TSV files with headers, empty directories. Then start writing to them.

### Routing table gaps
ROUTING_TABLE.md doesn't have entries for:
- Macro / Inflation Data (CPI, PCE, GDP, NFP) — I had to improvise for SIG-001
- Tariff / Trade Policy (Trump 90-day pause caught me with no row)
- Geopolitical Non-Energy (Iran ceasefire mechanics outside oil)
- Backup recipients per domain (for when primary is overloaded)
- Load awareness (whether routing should consider current agent state)

**Recommendation:** Add the three missing rows. Add a "backup" column to the table. Add a load-check sub-step in the routing decision.

---

## Process refinements (from research synthesis)

These came out of the brainstorming round on April 10. They're real improvements but not blocking. Pick what's highest-leverage.

| # | Change | Rationale | Priority |
|---|--------|-----------|----------|
| 1 | Filter-first: explicitly run gates BEFORE drafting | Already in CHECKLIST v0.3 — needs to be habit | DONE in spec, drift watch |
| 2 | Push vs pull split: only IMMEDIATE+ pushes; PRIORITY/ROUTINE goes to archive only | Reduces alert fatigue per ATC research | HIGH — depends on signal archive existing |
| 3 | Convergence superevents: bundle related signals into one | Already in CHECKLIST — applied successfully on SIG-001 | DONE |
| 4 | Confidence language alongside numerical | DONE in FORMAT_SPEC v0.2 + CHECKLIST v0.3 | DONE |
| 5 | Composition check (bear/bull balance is structural) | Counter-signals must get equal billing | MEDIUM |
| 6 | Routing happens FIRST in session, not last | Decision fatigue research | HIGH — change boot order |
| 7 | Routing log to TSV | Already mentioned in FILTER_SPEC, just needs the file | HIGH |
| 8 | System health check at boot (stale agents, missing data) | Bloomberg MON pattern | MEDIUM |
| 9 | Capability/load check before routing | Emergency dispatch CAD pattern | MEDIUM |
| 10 | Backup recipients with failover | Emergency dispatch PRF pattern | MEDIUM |

---

## Open questions for Will

1. **Routing log location and format.** Single TSV in `WALTER/log/`? One file per day? Per signal? Per recipient?

2. **Push vs pull threshold.** Confirm: only FLASH and IMMEDIATE get pushed to inboxes, PRIORITY and ROUTINE go to the signal archive only and agents pull via their SIGNAL_INTAKE.md watchlist at boot. This is a meaningful behavioral change.

3. **Mailroom agent.** Earlier you mentioned the idea of a separate agent handling intake. Is that still on the table? If yes, it slots in at the FRONT of the WALTER pipeline (before Gate 1) and changes my role from "ingest + filter + route" to "filter + route + curate."

4. **Signal archive directory.** Should `WALTER/signals/` be the archive (matches the spec naming), or do we want the COP architecture's three-layer model where WALTER/signals/ is Layer 2 and `COP.md` at repo root is Layer 1? The COP discussion from Apr 7 was unfinished.

5. **First live dispatch — proceed or skip?** SIG-001 was drafted yesterday for today's dispatch. By next session it may be 1-2+ days old and the news has been digested. Do we still dispatch it as a test of the pipeline? Or do we skip and wait for the next genuinely-fresh signal?

6. **Tier 1 SIGNAL_INTAKE.md rollout.** Only SAM and BRENT have one. The other Tier 1 agents (CARL, REGINALD, LIQUID, HENRY, HAWK, BROCK, RED) still need them before the routing system can use keyword matching at scale. Want me to ping you when more come in, or chase them yourself?

---

## Suggested order for next session

If I had to pick a single thread to pull, here's the order I'd recommend:

1. **Read this file + STATUS.md handoff section** (5 min)
2. **Check git pull state, refresh registry** (standard boot)
3. **Delete SIG-002** (1 min — close the loop from last session)
4. **Decide with Will: dispatch SIG-001 or skip as stale?** (5 min — open question #5)
5. **If dispatching: build minimal log infrastructure first** (`WALTER/log/routing_log.tsv` with headers — 5 min — Gap B above)
6. **Dispatch SIG-001 or write it off; either way log the decision**
7. **Then move to spec reconciliation: pick header schema OR filter model and tackle one** (30-60 min)

That's a session of work, achievable, and unblocks a lot of the remaining backlog.

---

*Living doc — update or supersede as priorities shift. Delete entries as they're completed. If everything here is done, this file can be replaced with a fresh handoff or deleted entirely.*
