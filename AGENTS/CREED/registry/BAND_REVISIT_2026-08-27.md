# CREED VX BAND MONTH-1 REVISIT

**Executed:** 2026-08-27 (6 days past the agreed 2026-08-21 date — the lateness is recorded, not smoothed; see §7)
**Authority:** Will-approved 2026-07-21 at band-freeze. **This document PROPOSES. It moves nothing.** Bands, ops, values and sustain windows are FROZEN TERMS; CREED may not edit them and has not.
**Registered at:** `PROME/DOCKET.tsv` row 33 · durable copy `registry/THRESHOLDS.tsv` header entry (C) · scope artifact `AGENTS/DAEDALUS/upgrades/CREED_REVIEW_2026-08-20.md` §54–60 item ③
**Question asked:** one month on, are the starter bands right?
**Short answer:** **the bands are mostly fine and the WIRING is not.** The revisit found no band that is clearly mis-levelled. It found three triggers pointing at nothing while their instrument sat one file away, one trigger that has spent itself, and one sustain window that is backwards relative to its own series' noise.

---

## 1. Scorecard — all 11 rows

| Trigger | Band | Vector cited | Basis | Verdict |
|---|---|---|---|---|
| `T-01a` | `> 12` sustain 2 | `VX-1.01` ✅ | clean | ✅ **SOUND — and the only unquestioned live numeric trigger on the board** |
| `T-01b` | `> 18` sustain **1** | `VX-2.01` ✅ | clean | ⚠️ **SUSTAIN QUESTIONED** — §5 |
| `T-02` | `> 50` sustain 2 | `VX-3.04` ✅ | clean | 🔴 **FIRED 8/20 — SPENT. S2 now has no escalation bar.** §4 |
| `T-03` | `> 3.40` | `VX-4.01` ✅ | 🔴 **IMPEACHED** | ⚖️ with Will (`KB-CREED-024`) — not re-litigated here |
| `T-04` | none (`rising`) | 🔧 **wired 8/27 → `VX-8.01`** | — | ✅ **UNWIRED, now fixed** — §3 |
| `T-05` | HOMER-owned | n/a | n/a | ✅ correct as-is; not a CREED band |
| `T-06` | `> 30` + "a CLUSTER" | 🔧 **wired 8/27 → `VX-5.01`** | — | 🔴 **STATE 3: wired but NOT MEASURED** + definitional conflict — §3, §3b, §3c |
| `T-06b` | `>= 1` | 🔧 **wired 8/27 → `VX-5.01`** | — | 🔴 **STATE 3** — and the row that produced the false fire, §3c. **"major fund" undefined.** |
| `T-07` | qualitative AND | — | — | ✅ correct as-is — the AND is deliberate |
| `T-08a` | `< -10` | `VX-7.01` ✅ | ⚠️ **UNDECLARED** | ⚖️ with Will · **the ONLY base-rated band** — §6 |
| `T-08b` | qualitative AND | `VX-10.01..10.05` ✅ | — | ✅ correct as-is (⚠️ cohort tape ~5wk stale — a data debt, not a band defect) |

**Counts, derived not remembered:** 11 rows · **7 carry a numeric band** · **1 of those 7 has ever been base-rated** · **3 rows cite no vector while their vector exists** · 2 are basis-blocked with Will · 1 has fired.

---

## 2. The headline

> **Not one band was found to be at the wrong LEVEL.** Every defect this revisit found is a defect of **connection** — a trigger that cannot reach its evidence, a trigger that has used itself up, a sustain window inconsistent with its own series' noise, or a band nobody has ever base-rated.
>
> ⚠️ **That is a finding about the REVISIT'S OWN PREMISE.** The month-1 review was scheduled to ask "are the levels right?" — and the levels turn out to be the part that is hardest to fault and the part the data still cannot adjudicate (§6). **The wiring was never on the agenda and is where all the damage was.**

---

## 3. 🔴 THE MAIN FIND — three triggers are UNWIRED, not uninstrumented

`threshold_scan.py`'s first run (2026-08-27 12:21) reported `T-06` and `T-06b` as **"NUMERIC BAND BUT NO METRIC VECTOR — UNTRIPPABLE BY CONSTRUCTION (the K5 shape)"**, and `SCRATCH` §3b generalised that to a judgment call between *"build a vector"* or *"rewrite the bar as honestly qualitative."*

**Both of those options are wrong, and the scan's verdict overstated the disease.** The metric surfaces already exist:

| Trigger | Its metric | The vector that already carries it | Match |
|---|---|---|---|
| `T-04` | `CMBS-REDEFAULT-2ND-MOD-RATE`, op `rising` | **`VX-8.01` CRE Modification Exhaustion** — bands read `2nd-mod rise / re-default rise / mod volume falls` | near-verbatim |
| `T-06` | `FORCED-SALE-DISCOUNT-TO-BASIS > 30`, "a CLUSTER" | **`VX-5.01` Forced-Sale / NAV Recognition** — value cell reads `CLUSTER of realized comps >30% below basis` | **verbatim** |
| `T-06b` | `OPEN-END-CRE-FUND-GATES >= 1` | **`VX-5.01` RED band, which reads `fund gates`** | verbatim |

⇒ **The scan reported a true fact about the REGISTRY and a false one about the WORLD.** `source_of_truth` names no vector, which is exactly what it said; "untrippable by construction" is a claim about whether the instrument *exists*, and it does.

> ⚠️ **THIS PARAGRAPH ORIGINALLY ENDED "`UNWIRED` IS A STRICTLY BETTER STATE THAN `UNINSTRUMENTED` — A POINTER, NOT A BUILD." THAT WAS ALSO WRONG, AND CREED FOUND OUT BY DOING IT. SEE §3c — the correction is the more useful half of this section.**

⚠️ **This is the pointer-defect class again, in a FOURTH form — the class is now n=6 across 4 shapes, not n=3:**

| # | Shape | Instances |
|---|---|---|
| 1 | pointer names the **WRONG** vector | `T-08a` (cited 8.01, lives at 7.01) · `T-01b` (DQ vector on an SS bar) |
| 2 | pointer names a source that **does not contain the value** | `T-03` (3.40 not in the cited QBP) |
| 3 | 🆕 **pointer ABSENT while the referent EXISTS** | **`T-04` · `T-06` · `T-06b`** |

> 🔴 **Shape 3 is the worst of the four, for one specific reason the other three do not share.** Shapes 1 and 2 produce a **wrong grade** — bad, but the trigger still gets looked at. Shape 3 makes a trigger look **unbuildable**, and the documented response to "unbuildable" is to **build a duplicate** or to **downgrade the bar to qualitative** — which `SCRATCH` §3b had already teed up as the two options. **A defect whose natural remedy is to discard a working instrument or rebuild one that exists is a defect that costs more than a wrong answer.**
>
> ⚠️ **And note which guard produced it: CREED's own new scan, on its first run, six hours old.** `finding_test_the_guard_not_just_the_guarded` — the guard's v1 fails on first live use. It reported honestly within its scope and its scope was narrower than its wording. **The scan's `NO METRIC VECTOR` line should say `NO VECTOR CITED` and check whether one exists.**

### 3b. ⚠️ Wiring `T-06` exposes a definitional conflict that the missing pointer has been HIDING

`T-06`'s own qualifying rule: *"a CLUSTER in **PERFORMING** collateral (not a single instance; **Galveston-class vacant/obsolete does NOT qualify**)."*

`VX-5.01`'s evidence set: *"205 W Randolph −72% REALIZED CMBS loss; Aon −58% mark; **Galveston $8.79/SF**; Austin MF; Seattle OZK deed-in-lieu."*

⇒ **The vector's comp set is BROADER than the trigger's qualifying set, and includes by name the exact comp the trigger excludes by name.** Wiring them without a note would import non-qualifying comps into a trigger that explicitly rejects them — i.e. **the wiring fix, done carelessly, manufactures a fire.**

**This disagreement has existed since 7/27 and was invisible precisely because the pointer was missing.** Connecting two surfaces is what tests whether they agree. `finding_definition_change_moves_the_evidence_for_the_level`.

### 3c. 🔴🔴 THE CORRECTION — there are THREE states, not two, and CREED's own fix manufactured a false fire finding the third

**Executing item 5 (wire `T-06` → `VX-5.01`) produced this on the very next run:**

```
🔴🔴 TRIPPED CREED-T-06b  30.0 >= 1.0 — EXCEEDS ITS BAND AND IS NOT IN THE FIRE LEDGER.
🟠 NEAR      CREED-T-06   30.0 > 30.0  — 0 away (0.00% of band).
     parsed-from:  CREED-T-06   30.0  ←  …ps >30% below basis
```

**Both readings are garbage, and each is garbage in a different way:**

| Row | What the scan compared | What was actually wrong |
|---|---|---|
| `T-06` | `30 > 30` — "0 away" | **The band against a copy of ITSELF.** `VX-5.01`'s value cell reads *"CLUSTER of realized comps **>30%** below basis"* — that is the threshold quoted back in prose, not a measurement. Comparing them measures nothing. |
| `T-06b` | `30 >= 1` — **TRIPPED** | **A discount PERCENT read as a COUNT OF FUND GATES.** Different quantity, different unit, no relationship whatsoever — and it produced a red instruction to go grade a fire at primary. |

⇒ **The real taxonomy has three states, and §3 above named only the first two:**

| State | Meaning | Correct remedy |
|---|---|---|
| 1. **UNINSTRUMENTED** | no instrument exists (true K5) | build the vector |
| 2. **UNWIRED** | instrument exists, pointer absent | wire the pointer |
| 3. 🆕 **WIRED BUT NOT MEASURED** | instrument exists, carries the **concept and the evidence**, emits **no measured number** | wire for navigation, **mark it un-machine-gradeable, grade by hand** |

> 🔴 **`T-06` and `T-06b` are STATE 3, and state 3 is the one that is DANGEROUS TO WIRE.** States 1 and 2 fail safe — an unwired trigger reports as unscannable and nobody grades it. **A state-3 row wired without a marker reports as `COMPARABLE` and the scan grades prose,** which is how a `>=1` gate-count bar came to be "tripped" by a `30%` discount.
>
> ⚠️ **§3b warned that careless wiring "manufactures a fire" — and then the very next edit manufactured one, by a mechanism §3b had not anticipated.** §3b was about the *comp set* (Galveston); this was about the *value cell*. **Being right about the class did not protect against the instance.**
>
> ⚠️ **It was caught only because the fix was RUN.** Nothing in the wiring edit looked wrong: the pointer was correct, the referent was correct, the frozen fields were verified untouched, and the row read fine. `finding_test_the_guard_not_just_the_guarded` — **and here the thing needing the test was the FIX, not the guard.** `finding_a_correction_pass_is_unreviewed_work`.

**Both defences shipped:**
- **Explicit:** `[QUALITATIVE-VALUE]` marker on the two rows' `source_of_truth`; the scan routes them to the unscannable register with *"wired for EVIDENCE NAVIGATION only — grade it by hand."*
- **General backstop, for rows nobody has marked yet:** the scan now refuses to grade any row whose extracted value **equals its own band and appears next to the same operator in the cell** — the self-reference signature — and says so.

⚠️ **The backstop does NOT catch the `T-06b` shape** (30 vs 1 — no self-reference, just incommensurable units). **That gap is stated rather than papered over: the scan has no unit awareness, so a wired state-3 row is only safe because a human marked it.** Registered as a known limit in §8, not claimed as solved.

---

---

## 4. 🔴 `CREED-T-02` has FIRED, and S2 now has no escalation bar

A binary trigger that has fired is **spent** — it cannot say anything further. S2 (the maturity-default wave) is the mechanism this desk's live synthesis rests on, and it is now **the only signal in the convergence matrix whose numeric tripwire is used up while its mechanism is still running.**

**And the surviving metric is the less informative half.** `T-02` bands the **SHARE**; the information is in the **DOLLARS** (standing trap #11 / `finding_verified_figures_do_not_verify_the_shape_claim`):

| Month | New delinquency $B (denominator) | Share % (**banded**) | Matured-balloon $B (**not banded**) |
|---|---:|---:|---:|
| 2026-04 | 2.63 | 42 | 1.10 |
| 2026-05 | 4.04 | 70 | 2.83 (+156%) |
| 2026-06 | 2.64 | 65 | 1.72 (−39%) |
| 2026-07 | 6.00 | 66 | **3.96 (+131%) ← series peak** |

- Denominator swing **2.28×** · share range **1.67×** · **dollar range 3.59×**
- **Share May→Jul reads 70 → 65 → 66 — flat, arguably peaked.** **Dollars over the same window read 2.83 → 1.72 → 3.96B — July is the peak, +40% on May.**
- Prints above the `>50` band: **3 of 4 (75%)**.

⇒ **ACTION (owner-lane, no band authority needed):** build a matured-balloon **DOLLAR** vector as a sibling to `VX-3.04`, and backfill Apr–Jul from the four PRIMARY-READ Trepp PDFs. The figures above are already derived and sourced; this is transcription, not new research.

⇒ **ASK Will (band authority):** whether that dollar vector should carry a **band**, making S2 escalation-gradeable again.

> ⛔ **CREED PROPOSES NO LEVEL FOR IT, DELIBERATELY.** n=4, range 1.10–3.96B, and the only candidate anchor is the most recent print — which is **standing trap #4 exactly** ("anchor a threshold to a DISTRIBUTION, not the most recent number"), the defect that produced the `PRED-CREED-006` re-spec. **A band set from this sample would encode July.** CREED refused a re-base at n=1 on `VX-9.03` and refuses one at n=4 here, for the same reason. **Register the vector now; band it when the series can carry a band.**

---

## 5. ⚠️ `CREED-T-01b`'s sustain window is backwards relative to its own series' noise

| | `T-01a` office **DQ** | `T-01b` office **SS** |
|---|---|---|
| Sustain required | **2 consecutive prints** | **1 print** |
| Mean abs. consecutive-month move | 37bp | **44bp** |
| Largest move documented in the series | 94bp | **91bp** — *"fell 91bps on a large office loan returning to master servicer"* (`VX-2.01`, 2026-05) |
| Desk's own characterisation | — | ***"illustrates why SS is the noisier series"*** |
| Distance to band | 9bp = **0.24× mean move** | 142bp = **3.19× mean move** |

⇒ **The noisier series carries the WEAKER sustain requirement.** The series whose own ledger documents single-loan 91bp reversals fires on one print; the quieter series requires two.

**The counter-argument, stated because it is strong:** `T-01b` sits 142bp away and moving away (−53bp in July). Clearing 18 from here in one month would require the largest move in the series' history by 50bp — an event genuinely worth firing on, sustain-1 or not. **On today's level, sustain-1 is not dangerous.**

**Why CREED still raises it:** the risk is not a 142bp leap, it is a **drift-then-blip**. The series has printed 17.11 twice; 17.9 is only 79bp above its observed max and well inside a two-month drift. From 17.9, a single +30bp transfer fires the trigger — and the desk has *already documented* the −91bp single-loan reversal that would unwind it the following month. **That is a transient fire on the noisiest series, on the desk's most-cited signal.**

⇒ **ASK Will (band authority):** raise `T-01b` sustain **1 → 2 consecutive prints**, matching `T-01a`. **Low urgency — 142bp away and receding.** No level change proposed; the `>18` bar is not in question.

---

## 6. 🔴 One band of seven has ever been base-rated — and the revisit cannot fix that yet

Standing trap #6: *base-rate a threshold BEFORE shipping a confidence against it.* Applied to the bands themselves:

| Band | Base-rated? |
|---|---|
| `T-08a` `< -10` | ✅ **Yes** — 252 sessions: below −10pp in **1.2%**, below −8pp 5.6%, below −5pp 36.5%; mean −2.14pp, σ 4.70pp. **A properly extreme-tail bar, and it did occur (6/1–6/3/26).** |
| `T-01a` · `T-01b` · `T-02` · `T-03` · `T-06` · `T-06b` | ❌ **No** |

**Why not, honestly:** the series are **4 to 6 observations long** (`VX-1.01` n=6, `VX-2.01` n=4, `VX-3.04` n=4, `VX-4.01` n=4 and impeached). `T-08a` is base-rateable only because its instrument is a **daily market series** with 252 sessions available; the CMBS series are **monthly** and CREED began recording them 2026-07-27.

⇒ **The month-1 revisit's core question is, for 6 of 7 numeric bands, STILL UNANSWERABLE — and saying so is the deliverable.** Manufacturing percentiles from n=4 would be the same error as the original starter bands, dressed as a review. `finding_ranked_head_sample_is_not_the_population`.

⇒ **PROPOSE — retire the calendar for this obligation and key it to SAMPLE SIZE instead.** A month-2, month-3, month-N revisit will keep arriving and keep finding n too small. **Register instead: each numeric band gets base-rated when its series reaches n=12 monthly observations** (`VX-1.01` ~2027-01, `VX-2.01`/`VX-3.04` ~2027-04 at current cadence). ⚠️ **A date-keyed obligation on a sample-size-limited question is a scheduled null result** — which is what this section is.

---

## 7. What this revisit says about the obligation itself

**It ran 6 days late, and the reason is on the record:** execution was "folded into CREED's next spawn"; that spawn (8/27 QBP) ran a full window and never saw the item, because the obligation lived only on **another desk's docket**. Now durably registered at `registry/THRESHOLDS.tsv` header (C) and routed to PROME (`ed3d7894d`) and DAEDALUS (`976315d38`).

⚠️ **The lateness was not costless, and the cost is measurable rather than hypothetical:** `T-04`, `T-06` and `T-06b` have been pointing at nothing **since 2026-07-27 — 31 days** — and `T-06`'s definitional conflict with its own evidence surface has been live for the same span. **Both were findable on day one of the freeze by reading the rows against the workbook.** The revisit was scheduled at month-1 precisely so a starter registry would get one deliberate read, and the read is what found them.

---

## 8. Dispositions

### ⚖️ ASKS FOR WILL — band authority (3)

1. **`T-01b` sustain `1` → `2` consecutive prints.** Rationale §5. No level change. Low urgency (142bp away, receding). CREED's recommendation: **approve** — it costs nothing while the trigger is far, and it cannot be safely changed once the series is near the bar.
2. **Whether the new matured-balloon DOLLAR vector (§4) carries a band.** ⛔ CREED proposes **no level** — n=4. Recommendation: **register the vector now, defer the band.**
3. **Whether to re-key the band base-rating obligation from a DATE to n=12 observations** (§6). Recommendation: **approve** — the calendar form generates scheduled null results.

*(Already with Will, not re-asked here: `T-03`/`VX-4.01` basis defect · `T-08a` basis declaration + like-for-like re-anchor rider.)*

### ✅ OWNER-LANE — non-band fields, same class as the Will-approved 2026-08-20 pointer pass (4)

4. ✅ **DONE** — `T-04` wired → `VX-8.01`. (Unaffected by §3c: it carries no numeric band, so it stays in the unscannable register either way.)
5. ✅ **DONE** — `T-06` wired → `VX-5.01`, with the §3b qualifying-set conflict recorded in the row **and** the §3c `[QUALITATIVE-VALUE]` marker.
6. ✅ **DONE** — `T-06b` wired → `VX-5.01` (RED band), `[QUALITATIVE-VALUE]` marked, plus a note that **"major fund" is undefined** in both the row and the vector (flagged, not self-resolved — a definition that positions a `>=1` bar is band-adjacent).
7. ✅ **DONE** — `threshold_scan.py`: `NO METRIC VECTOR` → `NO VECTOR CITED` **+ candidate lookup** (§3), **+ the `[QUALITATIVE-VALUE]` route and the self-reference backstop** (§3c). ⚠️ **Known limit, stated: no unit awareness** — an unmarked state-3 row with incommensurable units (the `T-06b` shape) is still gradeable-as-garbage. A human marker is the only defence.

> ⚠️ **These four WERE executed by this session** (after writing, before commit — item 7's re-run is what produced §3c). Items 4–6 touch `THRESHOLDS.tsv`, whose rows are frozen. **The 8/20 precedent is that POINTERS are not bands** (Will-ruled, DAEDALUS `fe1530a8d`: *"pointers, like annotations, aren't bands"*) — CREED reads items 4–6 as covered by that ruling and will execute them on that basis unless Will says otherwise, recording band/op/value/sustain as UNTOUCHED and verified.

### ⛔ EXPLICITLY NOT PROPOSED

- **No level, op or value change to any of the 11 rows.** None was found to be wrong.
- **No band for `T-04`.** Its vector exists but emits no number; banding it would create the K5 shape on purpose.
- **No dollar band for `T-02`** — §4, n=4.
- **No re-base of `T-03` to fit 2.48.** Standing prohibition, unchanged.
