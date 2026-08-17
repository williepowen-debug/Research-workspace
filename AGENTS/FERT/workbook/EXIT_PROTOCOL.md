# FERT — Falsification / Exit Protocol

**Kill rail re-derived: 2026-08-17** (first live session under the 2026-08-16 re-charter)
**Next mandatory re-derivation: 2026-11-15** — or immediately on any channel state change below.

> This file carries the DURABLE RULES. It deliberately carries **no live values** — the live read lives in `STATUS.md` with `[src M/D]` (anti-drift split, blueprint §3). If you are reading a price here, the file is malformed.

---

## 0. Standing definitions (so the rules below are gradeable)

| Term | Binding definition |
|---|---|
| **"Sustained"** | Never used without an explicit count of **prints or sessions on a named instrument**. A bare "sustained" in any FERT rule is a defect — fix it, don't interpret it. |
| **"Print"** | One published observation of the named instrument at its own cadence (Pink Sheet = monthly edition; DTN = weekly article; BLS = monthly release). A *bid* is never a print for an *award* instrument. |
| **Missing print** | If the named instrument publishes **no value** for a period (the BLS food-at-home series has a blank at 2025-10), the consecutive-count **pauses — it does not carry across the gap and does not reset**. Gaps are logged, then the count resumes. Stated because a silent blank otherwise makes two non-adjacent months look adjacent. |
| **Channel-kill vs thesis-kill** | Killing one channel never kills the others. Every kill below names **which channel dies** and **where the work migrates**. |

---

## 1. Channel status and per-channel kill rails

### Channel A — Nitrogen supply shock → price → CF
**STATUS: DEAD as of 2026-08-17. Killed, graded, and recorded — not quietly dropped.**

- **What killed it:** China's end-May quota resumption, a *policy* release, not demand destruction. Pink Sheet urea round-tripped −53% Apr→Jul; RCF tender bids cleared ~22% below the level that would reopen the channel.
- **What did NOT kill it:** Hormuz reopening (still shut), Qatar repair (still 3–5 yr), or demand (India still buying 1.7 Mt).
- **Migration path:** analytic weight moves to **Channel B (phosphate)** and to **CF single-name fundamentals**, which survive the nitrogen round-trip on their own evidence (1H26 adj EBITDA +55% y/y).
- **Re-open condition (bidirectional, testable at T1/T5):** an **awarded** India tender CFR print above the G2 level, **or** two consecutive weekly NOLA barge prints above the G1 level. Bids do not count. A single week does not count.

### Channel B — Phosphate tight leg
**STATUS: LIVE. This is the channel that carries FERT's current relevance.**

- **Thesis:** cost-push at the raw-material root (phosphate rock breaking a multi-year plateau + sulfur contract escalation + US producer curtailment), partially offset by the Morocco AD/CVD suspension, transmitting to DTN retail DAP/MAP.
- **CHANNEL KILL — fires from the LIVE state, requires BOTH legs:**
  1. Pink Sheet **phosphate rock** prints at or below its pre-break plateau level for **2 consecutive monthly editions** (the root reverses), **AND**
  2. DTN retail **MAP** prints below the ORANGE band floor in `VX.tsv` for **2 consecutive weekly articles** (the retail end reverses).
  Both legs required because either alone is a basis move, not a regime reversal (`finding_derived_metric_across_vintages_biases_toward_stale_leg`).
- **If killed:** FERT has no live price channel. That is a legitimate outcome — say so, drop to trigger-only dormancy, and **register the standing thresholds with an assigned grader before going quiet** (see §3).

### Channel C — Fertilizer → food-CPI transmission
**STATUS: OPEN INSTRUMENTED QUESTION. Explicitly NOT a carried prediction.**

- The March *timing* claim is graded **MISS** (`PREDICTIONS.tsv` FERT-05). The *mechanism* is **not** refuted — it is un-instrumented (`finding_market_ignoring_is_not_market_refuting`).
- **QUESTION-CLOSE (declare the channel shut):** BLS food-at-home m/m stays below the G4 threshold through the November-2026 print (T3/T6) **AND** no USDA ERS edition revises 2027 food-at-home upward *citing input costs*.
- **QUESTION-REOPEN:** requires a **fresh input shock**, never a re-read of the 2026 one. Concretely: a G1/G2 breach that persists past its stated print count. Re-reading the April spike is not evidence.

---

## 2. Bidirectional flip test (the single read that moves me, in BOTH directions)

Stated as one instrument so it cannot be satisfied by narrative:

| Direction | The single read | Why this one |
|---|---|---|
| **Bullish flip** (fertilizer re-tightens; transmission becomes live again) | **China's 2026 export quota revised DOWN, or the guidance floor reimposed at a level above prevailing international FOB** — read at MOFCOM/NDRC relay or CF commentary | It is the only variable that has *demonstrably* moved global urea 50% in either direction this year. Everything else (Hormuz, Qatar, India demand) was already true while price collapsed. |
| **Bearish flip** (domain goes quiet; FERT should stand down) | **Phosphate rock returns to its plateau AND retail MAP rolls over** (Channel B kill, both legs) — with nitrogen already dead | With A dead and B killed, no priced channel remains; C alone does not justify a live desk at weekly-to-monthly cadence. |

**Both are testable at a named next trigger date** (T10 monthly re-read; T4/T5 weekly; Pink Sheet monthly).

---

## 3. Dormancy is a REGISTRATION EVENT

If FERT stands down again, **every live threshold either moves to `PROME/GATES.tsv` with a named grader, or is retired in place with a dated banner.** No threshold is ever left standing in a dark directory.

This rule exists because it already failed once: the March `urea NOLA >$800` line fired in April, sat ~8 weeks ungraded in a dormant agent's directory, and un-fired — while WALTER relayed escalation twice into an unread inbox (`finding_fired_gate_needs_owner_independent_ledger`). **A local register nobody boots to read is not a wake owner.**

---

## 4. Anti-patterns this rail is written against (all three are FERT's own, graded)

1. **No threshold already breached at write time.** The March >$800 line was breached on the series actually being tracked at the moment it was registered as a forward trigger.
2. **No gate without benchmark + unit + source.** "$800 urea" named a benchmark it did not track, on a unit it never stated.
3. **No mechanism inference promoted to a confirmed pathway.** "LNG damage → fertilizer capacity destroyed" was recorded as `Confirmed=Yes` in FLOW.tsv on zero primaries. It is now graded REFUTED-as-written and retained as history.
