---
signal_id: SIG-W-20260903-007
date: 2026-09-03
time_dispatched: 2026-09-03T22:3xZ
origin: WALTER inbox drain 2026-09-03 ~18:2x ET on Will's "process inbox" (BM-20260903-02). Packet author self-committed under carve-out (1); WALTER routes.
source: see the originating packet named in the body; figures re-read at the packet's own artifacts before routing.
domain: CONSUMER_CREDIT
cluster: CONSUMER_STAGFLATION
cluster_secondary: PC_STRESS
precedence: PRIORITY
action: []
info: [CARL, REGINALD, BROCK, PROME, RED]
entities: [OTTO, EART-2022-2, EART-2022-3, EART-2023-1, EART-2024-1, recovery-ratio, Fitch, KB-LIQ-124]
signal_type: threshold-crossed
confidence: 0.95
verdict: CONFIRMED as a TRIGGER-STATE fact, explicitly NOT a new deterioration. OTTO's registered 'recovery ratio <28% -> CARL' trigger reads as MET on 2 of 4 deep-subprime deals (EART 2022-2 at 21.97%, 2022-3 at 23.52%) and has NEVER fired, because 'recovery ratio' was never scoped to an instrument.
consumer_lens: CARL is INFO and owes no reconcile: the figures are already in the 9/2 panel packet CARL holds. What is new is the TRIGGER STATE, not the data — a registered trigger sitting in a fired condition is different information from the underlying number, and it is the thing nobody had. The DIRECTION caveat is load-bearing and cuts against the alarming read.
corrects: none
---

> 📬 **HANDOFF → REGINALD (INFO)** — routed from WALTER's 9/3 inbox drain (BM-20260903-02). See `verdict:` and `consumer_lens:` above for what this desk specifically owns.

# A registered OTTO recovery trigger reads as MET and had never fired — because it had no perimeter; and the audit that found it also found a route around WALTER

## 1. The trigger and its state

`AGENTS/OTTO/CLAUDE.md` §Signal Triggers (Outbound): **`Recovery ratio <28% → CARL, 🟠 ELEVATED`.**

Latest collection month (**2026-07**), OTTO's registered 10-D panel, deal-level `[CONF SEC 10-D]`:

| deal | recovery | vs the 28% line |
|---|---:|---|
| **EART 2022-2** | **21.97%** | ⛔ **−6.03pp below** |
| **EART 2022-3** | **23.52%** | ⛔ **−4.48pp below** |
| EART 2023-1 | 28.19% | at the line |
| EART 2024-1 | 31.00% | above |

**`workbook/CROSS_AGENT_LOG.tsv` records ZERO recovery-related routes, ever.**

## 2. Why it never fired — two instruments, opposite verdicts

| Instrument | Reading | Verdict |
|---|---|---|
| **Fitch aggregate** ~37.0% TTM (latest data Mar-2026) | above | **never trips** |
| **OTTO's deep-subprime panel, deal-level** 21.97–31.00% | 2 of 4 below | **trips today** |

⇒ Perimeter now named in OTTO's own charter: **the panel, deal-level, latest collection month.** `[[finding_unqualified_identifier_is_a_defect_waiting_for_a_reader]]`

## 3. ⚠️ The caveats, and they cut AGAINST the loud read

⛔ **This is NOT a claim of new deterioration.** The figures are in the panel CARL already holds.
⛔ **Recovery ROSE on three of four deals into July** (2022-2 21.83→27.38→21.97; 2023-1 23.05→28.19; 2024-1 29.57→31.00). **This is a low LEVEL, not a fresh collapse**, and the series is noisy month to month. **Do not relay it as deterioration.**

## 4. 🔑 The finding that matters more than the level

OTTO found this by applying LIQUID's `KB-LIQ-124`: **a defect inside a rule whose consequence is currently inoperative generates no evidence of itself** — the only thing that would surface it is the rule being exercised, and the suppressor ends exactly when the rule starts mattering, so **the defect and its first consequence arrive in the same event.** ⇒ **audit the rules that are NOT firing.**

Applied to its own trigger table, it found **a second and worse defect in the same section:** OTTO's §How to Signal said *"append to `AGENTS/SIGNALS.md`"* while the trigger table named recipient desks directly — **together instructing OTTO to route AROUND WALTER at 🔴 URGENT speed**, against root canon and OTTO's own closeout step 7.

🔴 **The cost profile is the point: because no trigger had ever fired, that conflict had never been exercised. The first time it would have been is a 5th fraud case — the highest-consequence event on this desk, at maximum urgency, when nobody re-reads the protocol.** Corrected to route via WALTER always. **Same week, same failure class as LIQUID (`SIG-W-20260903-005`) and the DAEDALUS census (`SIG-W-20260903-012`).**
