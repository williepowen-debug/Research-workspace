# OWED-39 / DOCKET L396 — Channel-2 kill-letter scope: **ROUTED, NOT SELF-RULED**

**Written:** 2026-09-18 · **Owner:** OSPREY · **State:** ⚑ **OPEN — Will's word required. NOT closed tonight. Row stays dated 2026-09-19.**
**$0. No mark moved. No clock re-anchored. The dashboard still reads the letter as written.**

---

## 0. HOW THIS FILE WAS WRITTEN, BECAUSE THE PROCESS IS THE FINDING

This section is a record of **two corrections I made to myself in one sitting.** Both are kept visible rather than replaced, because the final answer looks like the original one and **arriving at it by luck versus by measurement are different facts.**

**Claim 1 — what I asserted on 9/15, and `PROME/DOCKET.tsv` L396 then recorded:**
> *"⛔ Nothing turns on it today (the C2 clock is independently anchored at 9/9), which is precisely the argument for ruling it now rather than at the sitting where it decides a kill."*

**That was ASSERTED, never COMPUTED.** `finding_distance_to_a_threshold_is_a_claim_about_its_basis`.

**Claim 2 — what I computed first tonight, and it alarmed me:** on the strictest drawing of the qualifier the Channel-2 clock ran to **35/30** with limb 2 also satisfied — i.e. **the amendment would retire a channel I score 5, the same day.**

**⛔ Claim 2 WAS WRONG, AND IT WAS WRONG BECAUSE MY OWN LEDGER HAD A HOLE.** A **2026-09-08 CPC Marine Terminal** event — drone incident, loading suspended at SPM-2/SPM-3 — was **missing from `STRIKES.tsv` despite falling inside the "swept-complete through 2026-09-16" window.** It was found by a subagent checking `GATE-OSPREY-001`, **not by a sweep, and not by me.** Backfilled tonight as `RU-20260908-CPC-SPM`.

> 🔑 **This is OSPREY's FOUNDING CALIBRATION LESSON (HAW-15) recurring exactly as written: *trusting a stale, gappy own-ledger as a baseline without checking its last-swept mark.*** The swept-complete header said 9/16 and was wrong about 9/8. **A completeness trap, not a quiet week.** The whole Tier-1 ledger apparatus exists because of this failure mode, and it still happened.

**Claim 3 — the corrected computation, §1 below: no kill fires under ANY drawing.** The amendment moves the clock from 8/30 to at most **17/30**. Material, but not a kill.

**Net:** the original *"nothing turns on it"* is approximately restored — **but it was never true as knowledge, only as a guess that happened to land.** And it survived only because a hole in my ledger was patched in the same session. **The routing decision is unchanged and the reason is now the correct one: §3.**

---

## 1. THE MEASUREMENT — every drawing of the qualifier, computed at the ledger, 2026-09-18, AFTER the backfill

Channel-2 kill, §1, requires **BOTH** limbs:
- **Limb 1:** no `crude-terminal` / `pipeline` / `oil-port`-class `STRIKES.tsv` row for **30+ days**
- **Limb 2:** seaborne crude holds **≥3.5 M bpd** 4-wk avg, no shut-in signal

| Drawing of limb 1 | Clock anchor | Limb 1 | Limb 2 | **Kill?** |
|---|---|---:|---|---|
| **(0) Letter as written** — any oil-port row, any basin, any commodity, any flag | 9/10 Makhachkala (**Caspian**) | **8/30** | satisfied | no |
| **(1) Geography only** (mirrors Channel 3's 9/8 qualifier) | 9/9 Novorossiysk **fuel-oil** terminal | **9/30** | satisfied | no |
| **(2) Geography + commodity** — exclude products-only terminals | **9/8 CPC** ← *the backfilled row* | **10/30** | satisfied | no |
| **(3) + `crude-terminal` class only** | **9/8 CPC** | **10/30** | satisfied | no |
| **(4) + Russian barrels only** (per `GATE-OSPREY-001`'s own CPC ruling) | 9/1 Ust-Luga (Baltic, ~700 kb/d crude) | **17/30** | satisfied | no |

**⛔ No drawing fires the kill. Maximum elapsed clock is 17/30.** The amendment roughly **doubles** the elapsed clock (8 → up to 17 days) — material to how close the channel sits to its own kill, **not** decisive today.

⚠️ **Limb 2 is satisfied in every row, and thinly:** latest print **3.54 M bpd 4-wk to 9/13 ≥ 3.50 — headroom 0.04, i.e. 1.1%** — on an instrument with **acknowledged missing 8/30 and 9/6 prints.** A future kill resting on that margin would be resting inside its own instrument's gap. `finding_instrument_error_correlated_with_the_trigger_biases_the_gate`.

---

## 2. THE REAL DEFECT IS NOT GEOGRAPHY — **the two limbs measure different universes**

I raised this as a Caspian question. It is a **scope-alignment** question with **four** independent instances, three of them live right now:

| # | Instance | Limb 1 counts it | Limb 2 measures it | Live example |
|---|---|---|---|---|
| 1 | **Caspian basin** | ✅ | ❌ landlocked, not seaborne | Makhachkala **9/10** |
| 2 | **Products terminals** | ✅ (`oil-port`/`oil-terminal`) | ❌ limb 2 is **crude** | Novorossiysk fuel-oil terminal **9/9** |
| 3 | **Pipeline export** | ✅ (`pipeline` is named in the letter) | ❌ not seaborne | Druzhba class |
| 4 | **Kazakh barrels via CPC** | ✅ (`crude-export-terminal` class) | ❌ limb 2 is **Russian** crude | CPC **9/8** ← *newly visible* |

**Limb 1 sweeps a strictly wider universe than limb 2 can see.** An event can reset the clock while being **invisible to the instrument that would confirm the kill.** Two tests that do not share a subject.

⚠️ **Instance 2 is load-bearing today:** the published Channel-2 anchor (9/9) is a **PRODUCTS** terminal sitting in a **CRUDE** channel's kill test.

🔑 **Instance 4 is the one that should embarrass us, and it is why I am not ruling this.** `GATE-OSPREY-001`'s letter **already says** *"CPC = Kazakh barrels, **non-countable in the Russian-terminal series**."* **The fleet already ruled this exact distinction — for the gate — and never propagated it to the kill letter.** The amendment was, in part, already decided; nobody carried it across. `finding_an_amendment_read_for_one_item_leaves_the_others_derived_from_the_original_live`.

---

## 3. WHY THIS STAYS WITH WILL — the corrected reason

**Not** *"it is free, so rule it cheaply"* (claim 1, never verified). **Not** *"it fires a kill tonight"* (claim 2, false).

> **Because the DRAWING IS THE MARK.** §1 shows one "geography qualifier" spans 8/30 → 17/30 depending on where the line is drawn, and each step is a defensible reading of the same sentence. **A desk choosing among them is a desk choosing how close its own 5 sits to its own kill.** PROME named this correctly at the L308 discharge — *"the desk that owns the letter declined to fix a letter it benefits from interpreting"* — and that reasoning is untouched by tonight's arithmetic.

---

## 4. OPTIONS FOR WILL — decidable, cost of each stated

⚠️ **I do not recommend a drawing.** §3 is why.

| Option | Text | Clock today | Cost |
|---|---|---:|---|
| **A** | Align limb 1 to limb 2: counts only rows serving **Black Sea / Baltic / Azov SEABORNE RUSSIAN CRUDE** export | **17/30** | Fully coherent; consistent with the gate's existing CPC ruling. But Caspian, Druzhba, products and CPC events then reset **nothing** — they need a companion watch or their absence reads as quiet |
| **B** | Geography only — mirror Channel 3's 9/8 qualifier exactly | **9/30** | Minimal, precedent-consistent. Leaves instances 2–4 live, so the same defect returns at the next kill evaluation |
| **C** | Widen limb 2 to total crude export incl. pipeline/Caspian | n/a | ⛔ **Unavailable** — no such instrument at 4-wk cadence; export measures are BRENT's |
| **D** | Leave unqualified | **8/30** | Kill becomes reachable by drift from basins, commodities and flags the thesis never covered |

**If A or B is chosen it must ship with a companion watch** for the excluded classes, or real events stop resetting anything and vanish from view.

---

## 5. FOLDED IN — Channel-3 vessel-scope ambiguity (one row, not two)

**Question:** does a 2026-09-12 Ukrainian USV destroying a **Russian USV** count as a *"vessel-strike incident"* under Channel 3, whose subject is **shadow-fleet tankers**?

**Recommendation I WILL make, because it cuts against me** — it SHORTENS my clock, making the channel **harder** to kill: **NO.** An unmanned surface drone is not a shadow-fleet hull; counting it measures a superset of the channel's subject (§2's finding, one channel over).

Clock: **subject reading → 14/21** (from 9/4) · **bare-letter reading → 6/21** (from 9/12). **No kill either way — and here that statement IS computed.**

---

## 6. WHAT I DID / DID NOT DO

✅ Backfilled `RU-20260908-CPC-SPM`; recorded the completeness defect in the ledger header; **did not advance the swept-complete mark.**
✅ Falsified my own two prior claims in writing, in order, at the top.
❌ Did **not** rule, re-anchor, re-score, or move the band. Dashboard reads drawing (0), **8/30**.
❌ Did **not** pick between A/B/D.

## 7. ASK

**Will's word on the drawing (A / B / D), via PROME.** L396 stays dated **2026-09-19**.

⚠️ **Correction owed to `PROME/DOCKET.tsv` L396:** its text carries my *"nothing turns on it today"* rationale. That sentence was **never verified when written**, is **approximately true by luck**, and should not be the reason quoted at the sitting. **Replace it with §3.**
