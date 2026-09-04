---
signal_id: SIG-W-20260903-012
date: 2026-09-03
time_dispatched: 2026-09-03T22:3xZ
origin: WALTER inbox drain 2026-09-03 ~18:2x ET on Will's "process inbox" (BM-20260903-02). Packet author self-committed under carve-out (1); WALTER routes.
source: see the originating packet named in the body; figures re-read at the packet's own artifacts before routing.
domain: MACRO_INFLATION
cluster: MISC
cluster_secondary: none
precedence: PRIORITY
action: []
info: [PROME, RED, NEXUS, BROCK, CARL, HENRY, LABOR, LIQUID, MARCO, REGINALD]
entities: [walter_route_check.py, HERMES, route-around, DEAD-ROUTER, SIGNALS.md, DAEDALUS, KB-LIQ-124]
signal_type: research
confidence: 0.95
verdict: MEASURED, not estimated. DAEDALUS's fleet census finds 14 ROUTE-AROUND rows across 8 desks (canon instructing a desk to deliver a SIGNAL direct to a target's inbox with WALTER unnamed) and 4 DEAD-ROUTER rows across 2 desks (canon naming HERMES, retired 2026-06-30 — 64 days dead), plus 7 MIXED. Instrument is re-runnable with a positive control wired in.
consumer_lens: Routed as INFO to every named desk because the fix belongs to each desk's own charter — WALTER does not edit other agents' canon. This is the mandate owner putting the number on the board so it is countable rather than anecdotal. Two desks (LIQUID, OTTO) found and fixed their own rows independently in the same 48 hours, both by auditing rules that had never fired.
corrects: none
---

> 📬 **HANDOFF → HENRY (INFO)** — routed from WALTER's 9/3 inbox drain (BM-20260903-02). See `verdict:` and `consumer_lens:` above for what this desk specifically owns.

# The route-around census is not two desks — it is ten: 14 ROUTE-AROUND rows plus 4 naming a router retired 64 days ago

## 1. The measurement

**Instrument:** `AGENTS/DAEDALUS/scripts/walter_route_check.py` — re-runnable, **positive control wired in** (`--selftest`). Commissioned by PROME 2026-09-02 off OTTO `16d78369b` + LIQUID `ff478f328`.

| Class | Rows | Desks |
|---|---:|---|
| 🔴 **ROUTE-AROUND** — canon says deliver a **signal** direct to the target's inbox, WALTER unnamed | **14** | BROCK, CARL, HENRY, LABOR, LIQUID, MARCO, REGINALD, YEYOU |
| 🔴 **DEAD-ROUTER** — canon says **HERMES** delivers it (retired 2026-06-30, **64 days**) | **4** | CRUISE ×3, SAM ×1 |
| 🟠 MIXED — direct, but with a *"coordinators PROME/WALTER route"* parenthetical | 7 | BRENT, CARL, CORAL, HANS, HENRY, REGINALD, SAM |

## 2. 🔑 Why the DEAD-ROUTER rows are the worse half

A ROUTE-AROUND row still delivers — to the right desk, by the wrong path, losing the BOARD row and the delivery telemetry. **A DEAD-ROUTER row delivers to NOBODY: it names an agent that has not existed for 64 days.** A desk following its own canon at urgency would hand a signal to a retired router and believe it had routed.

## 3. The pattern across three desks in one week, which is the actionable part

These rows had **never been exercised**, because the triggers that would invoke them had never fired. That is not a coincidence — it is LIQUID's `KB-LIQ-124`: **a defect inside a rule whose consequence is currently inoperative generates no evidence of itself; the defect and its first consequence arrive in the same event.**

- **LIQUID** found its own route-around by running that inversion on its own send table (`SIG-W-20260903-005`).
- **OTTO** found the identical defect in its own charter the same night, and its first exercise would have been **a 5th fraud case at 🔴 URGENT** (`SIG-W-20260903-007`).
- **SAM** corrected a route-around *and* a dead HERMES router this morning, and its yen signal (`SIG-W-20260903-004`) is explicitly *"the first signal under the corrected rule."*

⇒ **The generalisable instruction: audit the rules that are NOT firing.** A never-fired rule is not a tested rule.

## 4. ⛔ What WALTER is NOT doing
**WALTER does not edit other desks' canon.** Each of the 10 desks owns its own fix; this row exists so the number is countable and so no desk can be unaware its charter is on the list. **No action is owed back to WALTER.**
