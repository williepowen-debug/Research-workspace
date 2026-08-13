# CCC/HY ESCALATION — **STAND-DOWN**, and the re-arm condition that stops it being a quiet drop

**Date:** 2026-08-13 · **Agent:** REGINALD · **Authority:** Will-ruled in-session 2026-08-13 (slate item #3) — stand-down approved as REGINALD recommended, **conditional on naming a re-arm.**
**Object:** the escalation to LIQUID/BROCK contemplated by `VX-REG-18.04`'s own rule after its 3rd hard-fire. **NOT the tripwire itself.**

> ## ⚠️ WHAT IS AND IS NOT CHANGING
> **The `3.6×` tripwire is UNTOUCHED** — level, sustain (3 consecutive daily closes), reset rule (any close ≤3.6×) and driver-decomp obligation all stand. The row stays **LIVE and at WATCH**, and it is **still in its fire run**.
> **What stands down is the ESCALATION** — the packet to LIQUID/BROCK that the row's own note said to "consider". No threshold moved; a previously *unwritten judgment call* is now a *written, pre-registered* one.

---

## 1. WHY THE ESCALATION IS NOT BEING SENT

**Not because the fire was wrong — because my characterization of it was, and I found that myself after the escalation was already queued.**

| What the 8/12 escalation case rested on | What 8/13 verification found |
|---|---|
| *"3rd hard-fire, 8/7-8/11"* | **Wrong dates.** The run began **7/31** and is unbroken; the 3-consecutive criterion was met **8/04**. I had reported the run's *last* three closes as its *first* three. (NEXUS caught it; verified at FRED.) |
| *"CCC-widening-LED = the escalation case, NOT the benign-beta of fires #1/#2"* | **Baseline-sensitive.** On the 7/16 baseline my rule names: CCC +53bp vs HY +1bp ⇒ CCC-LED, as recorded. **From the run's own pre-start close (7/30): CCC +17bp vs HY −12bp ⇒ ~73% of the ratio's rise inside the run is HY TIGHTENING** — the same benign-beta mechanism as fires #1 (7/13) and #2 (7/22). |

**The claim that distinguished this fire from the two benign ones does not survive its own run-start baseline.** Escalating on it would ask LIQUID and BROCK to act on a mechanism claim I have already qualified in writing.

**What SURVIVES and is not being retracted:** the **level** story. CCC OAS at 1023 [8/11] / 1020 [8/12] is near the top of its two-year range (max 1137, median 880 over 533 sessions), and **+53bp since 7/16 is real widening, not a denominator artifact**. The row stays at watch *because of the level*, not because of the ratio's slope.

**Corroborating context that argues against urgency:** my own 7/30 bank-side attribution (`BANK-ABSENT`, conf ~0.8) is unretracted — every reachable bank-credit instrument was flat-to-up across the HY widening. **HY sits DOWNSTREAM of bank credit in my chain, so a CCC-tail move under a calm HY with no bank-credit leg is not my chain firing.** And HY itself is *tightening* (272 [8/11] → 271 [8/12]), moving toward `GATE-HY-REKILL`'s <260 line, not away from it.

---

## 2. ★ THE RE-ARM CONDITION — pre-registered, base-rated, and satisfiable

**Design requirement, from the defect that caused the stand-down:** the re-arm must be driven by the **numerator**, because HY is the ratio's own denominator. Any condition pairing "ratio high" with "HY wide" asks numerator and denominator to move apart in a way the index rarely delivers — that is the trap that made NEXUS's Branch A fire **0 times in 19 months**, and it is the same trap in my own attribution.

> ### RE-ARM `VX-REG-18.04-ESC` — registered 2026-08-13
> **The LIQUID/BROCK escalation re-arms when, on 2 CONSECUTIVE daily closes, BOTH hold:**
> **(a) `BAMLH0A3HYC` (CCC OAS) ≥ 1050 bp**, and
> **(b) `BAMLH0A0HYM2` (HY OAS) ≥ 272 bp** — i.e. the CCC widening is **not** being manufactured by HY tightening.
>
> **Instrument:** FRED `BAMLH0A3HYC` / `BAMLH0A0HYM2`, daily close, ~1 business-day publication lag. **Unit:** basis points. **Basis:** option-adjusted spread, index level (not the ratio).
> **On re-arm:** the escalation packet goes out carrying **both baselines** (7/16 and run-start) and leading with the **CCC level**, never the ratio's slope.

**Base rate — 533 sessions, 2024-08-01 → 2026-08-12, pulled 2026-08-13:**

| Candidate | Fires (2 consecutive) | Rate |
|---|---:|---:|
| CCC ≥ 1034 (the 7/31 peak) + HY ≥ 272 | 11 / 532 | 2.1% |
| **CCC ≥ 1050 + HY ≥ 272 — ADOPTED** | **8 / 532** | **1.5%** |
| CCC ≥ 1075 + HY ≥ 272 | 5 / 532 | 0.9% |
| CCC ≥ 1100 + HY ≥ 272 | 1 / 532 | 0.2% |
| *(reference — NEXUS's Branch A: ratio ≥3.60 3-of-5 AND HY ≥280 s3)* | *0 / 418* | **0.0%** |

**Why 1050:** it is **+30bp above today's CCC (1020)** and **+16bp above the run's own 7/31 peak (1034)**, so it requires *new* widening rather than re-firing on the state that just stood down; it fires at **1.5%**, which is discriminating but **not jointly unsatisfiable** (the failure mode I killed twice today — the ≥25% MI3 line at 0/56 and Branch A at 0/418); and it sits below the 2-year max of 1137, so the level is **reachable on this index's own history**.

⚠️ **Honest disclosure about leg (b): it is historically NON-BINDING.** Over 533 sessions, *every* session with CCC ≥ 1034 also had HY ≥ 272 — the joint single-session counts are identical to CCC alone (14/14 at 1034, 11/11 at 1050). **So (b) filters nothing in the sample.** It is in the spec to prevent a *future* repeat of the exact defect that caused this stand-down — a CCC-level reading that looks adverse while HY is collapsing underneath it — not because it does work on the record. **Stated rather than left to be discovered**, because a condition that has never bound is one nobody should assume is protecting them.

**How the re-arm could be wrong:** it is a **level** gate, so it will miss a slow grind that widens CCC 40bp over two months without touching 1050 — and my `finding_effect_below_instrument_detection_floor` says a sub-threshold grind is *no evidence*, not weak evidence, on this instrument. If that is the failure that shows up, the successor is a **rate-of-change** spec on CCC, base-rated separately. **Not built today.**

---

## 3. STATE AFTER THIS NOTE

| Object | State |
|---|---|
| `VX-REG-18.04` tripwire (3.6×, 3 consec, reset ≤3.6×) | **UNCHANGED, LIVE.** Run continues — 7/31 → 8/12 is now **9 consecutive sessions** >3.6× (8/12: CCC 1020 / HY 271 = 3.764). |
| Row status | **WATCH** — held on the CCC **level**, not the ratio's slope. |
| Escalation to LIQUID/BROCK | **STOOD DOWN 2026-08-13**, Will-approved. Re-arms only on `VX-REG-18.04-ESC` above. |
| Driver-decomp obligation | **UNCHANGED, and now must report BOTH baselines** (fixed calendar baseline *and* the run's own start) — the single-baseline read is what produced the retracted characterization. |
| NEXUS | Copy sent. Its registered **8/28** falsifier resolves on this ratio; it is entitled to know the escalation stood down and why. |

*— REGINALD, 2026-08-13. All figures FRED `BAMLH0A3HYC` / `BAMLH0A0HYM2`, daily close, pulled 2026-08-13 (series through 8/12).*
