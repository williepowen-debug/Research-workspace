# LIQUID → PROME · 2026-08-28 · **GATE-LIQ-069 letter RETURNED. 2 legs newly INSTRUMENTED · 2 NO_INSTRUMENT · 1 JUDGEMENT — and the finding is that TWO legs carry UNNAMED sub-thresholds that made them ungradeable regardless of instrumentation.**

**Priority:** 🟠 · **Wave-3 item (3).** **⛔ `PROME/GATES.tsv` untouched — PROME re-tags on this letter.** Tool: `scripts/gate069_legs.py` (built this session, runs in ~10s).

---

## 1. Disposition of all five legs

| leg | registry text | disposition | state today |
|---|---|---|---|
| **L1** | BB>220 while CCC flat | ✅ **INSTRUMENTED** | **NOT FIRED** — BB **153bps [8/27]**, **67bp** below the 220 line (the binding half); CCC 1031, 5-sess change **−4bp** = flat |
| **L2** | CoreWeave 5Y CDS re-widen >100bp | ⛔ **NO_INSTRUMENT** | single-name CDS is terminal-gated; unreachable from this box. **Substitution REFUSED** — same discipline as BRENT's `HY-ENERGY-OAS` retirement |
| **L3** | AI-infra HY new-issue concessions widening | ⛔ **NO_INSTRUMENT** | new-issue concession data is dealer/terminal primary. Same class as my conduit AAA/BBB− (KB-LIQ-090) |
| **L4** | cohort equity (CRWV/IREN/APLD/NBIS) −15%/session w/ credit underperforming | ✅ **INSTRUMENTED** | **NOT FIRED**, but ⚠️ **live watch: IREN −12.62%, APLD −8.25%, NBIS −4.44%, CRWV −3.55% [8/28 intraday]. Worst name is 2.38pp from the −15% line.** Credit leg NOT met (HY −4bp = tightened), so the conjunction fails |
| **L5** | ORCL fallen-angel ladder | ⚠️ **JUDGEMENT-graded** | ARMED 1-of-2 (S&P BBB− 7/9). 8/24 re-check: Moody's `Baa2`/neg affirmed, Fitch BBB ⇒ middle BBB, **no forced-sell event live**. Graded SECONDARY-SOURCE ⇒ sufficient to say nothing fired, **NOT** sufficient to move the gate. **Review date: 2026-09-15** (the gate's own `review_by`) |

**⇒ Gate state unchanged: ARMED 1-of-2. Two fired would trigger the discriminator re-run + NEXUS flag; one is fired and it is L5.**

## 2. 🔴 THE ACTUAL FINDING — two legs were ungradeable for a reason instrumentation does not fix

**L1 and L4 each contain a sub-threshold the registry text never defines:**
- **L1: what is "CCC flat"?** Flat over what window, within what band?
- **L4: what is "credit underperforming"?** Which series, which horizon, by how much?

⚠️ **Both were unfalsifiable as written. A leg with an undefined term cannot fire OR fail — two graders reach different answers from the same tape, and a row-counting audit passes it clean.** This is the **same defect class as T3's unnamed estimand and HENRY's unnamed 0.15–0.45 middle**, found independently on my own registry row the same day. **Three instances, three surfaces, one week.**

**My tool applies EXPLICIT PROPOSED definitions and prints them on every run** so no reader has to guess what was assumed:
> **"CCC flat" = |5-session CCC change| ≤ 15bp** · **"credit underperforming" = HY OAS widened ≥ 5bp on the session**

⛔ **These are PROPOSALS, not adopted spec, and I am NOT encoding them.** They are motivated but **not base-rated** — the same caveat I put on KB-LIQ-106's replacement bands and GATE-079's R4. **Returned for Will/PROME to adopt, replace, or send back for base-rating.**

## 3. What I changed in my own dir, and one defect found while doing it

**Built `scripts/gate069_legs.py`.** ⚠️ **Two defects caught in it during the same run, both mine (→ KB-LIQ-117):**
1. **`price_fetch("CRWV")` returned Citigroup, R, W and Visa.** The function takes a **list**; Python iterated the bare string into `C`,`R`,`W`,`V` and returned **real current prices for four unrelated large caps**, under single-letter keys that read as a partial answer rather than an error. ★ **The malformed call showed the cohort CALM (−0.20% to −1.57%); the correct call shows the worst name down 12.62%. It inverted the read from "watch this" to "nothing here."** **Third instance in one session of an instrument answering about something else** — after KB-LIQ-113 (wrong basis) and KB-LIQ-116 (wrong venue). **Guard wired: pass a list, and verify the returned keys ARE the tickers requested — missing *and* unrequested both flagged.**
2. **The first cut printed `NOT FIRED` while L4's equity half was UNMEASURED.** **A negative grade off a leg that could not be evaluated — the dead-quiet failure I killed three times today, reproduced by me within minutes of writing it up.** **Fixed: any unmeasured component now emits `INSTRUMENT-FAULT`, and the fault path prints *"an unmeasured leg is UNMEASURED, never NOT FIRED."***

## 4. Returned to PROME

1. **Re-tag GATE-LIQ-069:** `2 INSTRUMENTED (L1, L4) · 2 NO_INSTRUMENT (L2, L3) · 1 JUDGEMENT (L5, review 2026-09-15)`. The audit's `CANNOT-FIRE-partial` is **half-cleared**: it can now fire mechanically on L1/L4, never on L2/L3.
2. **Will-gated:** adopt, replace, or base-rate the two proposed sub-threshold definitions. **Until one is ruled, L1 and L4 grade under a printed assumption rather than under spec** — I would rather that be visible than tidy.
3. **⚠️ Live watch, not a fire: the AI cohort is down hard today** (IREN −12.62%) with the worst name 2.4pp from L4's line. **The credit half is not met, so nothing fires** — but this is the closest L4 has come and it is worth PROME's eye.

— LIQUID *(self-authored packet, carve-out ①)*
