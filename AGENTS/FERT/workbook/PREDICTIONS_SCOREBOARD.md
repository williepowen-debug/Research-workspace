# FERT — Predictions scoreboard

**LIVE — created 2026-10-28** (Will-approved; peer-comparison gap 3; model = LABOR `workbook/PREDICTIONS_SCOREBOARD.md`). **Last real data refresh: 2026-10-28** (FERT-13 registered OPEN).
**Source of truth:** `workbook/PREDICTIONS.tsv` (the ledger; every grading basis and post-mortem lives on its row). This file **aggregates and indexes**; it never restates a row's letter.
**When to touch it:** before writing a new prediction (run §C), and when a prediction resolves (add it to §A, recompute §B).

---

## §A — Record by charter era

The March-2026 desk and the re-chartered desk (Will-ruled 2026-08-16) are **different instruments**: March rows were written with no stated probability and were graded retroactively at the first live session (2026-08-17). They are kept apart so the March record neither flatters nor drags the live calibration.

### March-2026 charter (graded history — no probabilities, no Brier)

| ID | Claim (short) | Status | Lesson the row carries |
|---|---|---|---|
| FERT-01 | Phase 1: price shock | HIT | — |
| FERT-02 | Phase 2: inventory drawdown | VOID (unfalsifiable) | Never register a phase without a named instrument |
| FERT-03 | Phase 3: allocation crisis | HIT (partial — offshore only) | Scope the geography in the claim text |
| FERT-04 | Phase 4: planting disruption | MISS | An affordability shock is not a physical allocation failure |
| FERT-05 | Phase 5: food-CPI spike, Q3–Q4 2026 | **MISS (so far — window open to 2026-12-31)** ⚠️ | Re-opening needs a FRESH input shock |
| FERT-06 | Urea NOLA > $800 = RED | VOID (broken as instrument) | Benchmark + unit + source + revision policy, or do not register |
| FERT-07 | CF +$2.7B EBITDA tailwind | HIT (direction) / MISS (magnitude) | Derive sensitivity from disclosed figures or state none |
| FERT-08 | Qatar 77 mtpa offline = fertilizer capacity destroyed | MISS | Delete unevidenced mechanism inferences |
| FERT-09 | China export halt permanent | MISS | Never score a policy variable as a frozen constant |
| FERT-10 | India panic purchasing | HIT | The model row: mechanism + geography + trigger all named |

Tally (first status token): **4 HIT · 4 MISS · 2 VOID** of 10. FERT-07 counted as HIT on its first token; it is half a miss.

⚠️ **FERT-05 is provisional and invisible to the boot scan.** Its Status is MISS, not OPEN, so `boot.py` never flags it, yet its Resolve_By (2026-12-31) has not passed. Final grade needs the December CPI food-at-home print (BLS, mid-January 2027). Owner action: grade it finally at the first session after that print. Found 2026-10-28 building this file.

### Re-chartered desk (live calibration)

| ID | Registered | Confidence (as made) | Resolve_By | Status | Outcome = 1 if the stated claim came true | Brier |
|---|---|---|---|---|---|---|
| FERT-11 | 2026-09-05 | 72% | 2026-10-09 | HIT (2026-10-07) | 1 | 0.078 |
| FERT-12 | 2026-09-05 | 78% | 2026-12-02 | MISS (2026-10-14) | 0 | 0.608 |
| FERT-13 | 2026-10-28 | 55% | 2026-12-31 | **OPEN** | — | — |

## §B — Calibration read

- **n = 2 resolved. Mean Brier 0.343** (a constant 50% forecast scores 0.250). Two rows cannot separate skill from luck; this line exists so the number is computed the same way when n grows.
- **Pattern, one instance:** FERT-12 under-called momentum. It registered 78% that retail MAP would *not* exceed $975, on a base rate drawn from four flat August prints; the Sep–Oct run broke it on print 6. FERT-13's base rate uses all 11 weekly steps and rejects the burst-only window as overfit, which is the correction in both directions.
- **Re-mark convention:** the latest dated pre-resolution mark governs scoring, and the original reports separately (`FORGE/PREDICTION_DISCIPLINE.md` § Grading). No FERT row has been re-marked.

## §C — Pre-write checklist (run before any new FERT-XX row)

1. **Instrument named:** series, benchmark, unit, vintage (FERT-02, FERT-06).
2. **Geography in the claim text** (FERT-03).
3. **No frozen policy constant:** a policy variable is re-read, never assumed (FERT-09).
4. **No unevidenced mechanism:** an inference without a primary is an open question, not a premise (FERT-08).
5. **No undisclosed sensitivity:** derive it from filings or state none (FERT-07).
6. **Base rate first, on the claim's own instrument;** say which window was rejected and why (FERT-12, FERT-13).
7. **Grading basis, six elements (WQ-162),** including the negative-resolution guard when a MISS resolves on an absence (FERT-11/12/13 form).
8. **Anchor type named** (calendar / chosen / event) and **If_Falsified_Action** stated as a consequence, not a feeling.
