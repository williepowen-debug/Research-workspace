# HAW-19 — SPEC CONSOLIDATION RECORD

**Executed 2026-08-20, Will-directed.** Pre-consolidation text preserved verbatim at git `a719b5f05:AGENTS/HAWK/thesis/PREDICTIONS.tsv`.

## Why this exists

`HAW-19` took **four structural repairs on its first day**, all legitimate (registration defects found before in-window evidence), each appended as an amendment block. The result was a governing spec spread across a prediction cell plus four amendment layers — **a resolver on 2026-09-30 would have had to reconstruct which text governs**, and that ambiguity is what produces post-hoc rubric drift under time pressure.

## The binding constraint on this exercise

⚠️ **The row is OPEN with in-window evidence already in hand.** A consolidation that changed what fires would be exactly the fitting-spec-to-evidence failure this desk refused twice on 8/20 (gap five, tankage-vs-moorings; and the initiating-cause window boundary).

⇒ **This consolidation is STRICTLY SEMANTICS-PRESERVING and the equivalence is proved below, clause by clause. No threshold moved. No leg added or removed. No non-fire changed. No verdict boundary changed. Confidence unchanged at 70%.**

---

## 1 · Equivalence map — every operative clause, before → after

| # | Pre-consolidation clause | Status | Where it lives now |
|---|---|---|---|
| P1 | Cross-war, theater-agnostic, molecule-explicit | **preserved** | Governing spec, header |
| P2 | Window 2026-08-20 → 2026-09-30 | **preserved** | Governing spec §0 |
| P3 | Claim: no irreversible physical loss of crude productive/export capacity, either theater | **preserved** | Governing spec §0 |
| P4 | "The row's claim is DESTROYED CAPACITY and nothing else" | **preserved** | Governing spec §0 |
| P5 | Demoted willingness gloss | **preserved, non-operative** | Notes (marked GLOSS) |
| P6 | HAW-18 successor lineage | **preserved, non-operative** | Notes |
| P7 | Two legs, both theater-agnostic, both requiring destroyed capacity (KB-HAWK-236) | **preserved** | Governing spec §0 |
| A(i) | Named crude field / stabilization-processing facility / crude-export terminal, either theater, CONFIRMED physical damage (primary or Tier-1; a claim ≠ a confirmation) | **preserved verbatim** | §A.1 |
| A(ii) | Damage must AGGREGATE to terminal, not component — either (a) only loading path, or (b) redundancy exhaustion ≥N of M loading points simultaneously out, damage attribution on ≥1, dark-immune evidenced | **preserved verbatim** | §A.2 |
| A(iii) | Terminal throughput down ≥200 kbpd crude for ≥45 days, BOTH Kpler AND Vortexa within 1.5×, corroborated by the (ii) dark-immune observation | **preserved verbatim** | §A.3 |
| A(iv)(α) | FM explicitly attributed to PHYSICAL DAMAGE (not security / insurance / commercial) | **preserved verbatim** | §A.4 |
| A(iv)(β) | Restoration timeline ≥90d from operator, sovereign, or named Tier-1 assessor (Kpler/Vortexa/IIR/WoodMac/S&P) | **preserved verbatim** | §A.4 |
| A(iv)(γ) | *deleted 8/20 — absence-as-evidence on AIS-derived instruments* | **stays deleted** | Notes only |
| B1-B6 | ≥10 cumulative NAMED, DATED disabled-or-boarded hulls in any rolling 14d; corridor set Hormuz/Gulf of Oman/Bab/Red Sea; out-of-corridor excluded; unattributable increments logged not counted; FROZEN; baseline 5 as of 8/17 ⇒ ≥+5 | **preserved verbatim** | §B.1-B.4 |
| B7-B8 | Rise must occur WITHOUT matching alternate-route rise (SUMED/Sidi Kerir, both trackers within 1.5×) — denial not rerouting | **preserved verbatim** | §B.5 |
| R1 | Resolve_By 2026-09-30, anchor IMMOVABLE | **preserved** | Resolution_Criteria |
| R2 | Either leg fired = FAILED; both unfired = CONFIRMED **only on a dated search attempt** (3 named pulls) | **preserved** | Resolution_Criteria |
| R3 | NO-VERDICT band for late-window LEG-A events lacking α/β | **preserved; stale rationale corrected — see D2** | Resolution_Criteria |
| R4 | Six explicit non-fires (refinery · power/grid/desal · LNG/gas/GTL · security-attributed halt · vessel at any scale · claim-only strike) | **preserved verbatim** | Resolution_Criteria |
| R5 | LEG B instrument caveat — "disabled" definitional stability unchecked; if unstable, LEG B = NO-VERDICT | **preserved verbatim** | Resolution_Criteria |

**Nothing added. Nothing dropped. Nothing re-parameterized.**

---

## 2 · 🔴 THREE DEFECTS THE CONSOLIDATION SURFACED — none patched *(as at 2026-08-20; **D1 was repaired 2026-09-10 under WQ-160 and D2 fell out with it — see the §3 banners. D3 remains open and is expressly left unparameterized by WQ-212. The 9/30 GRADE is separately ruled: DEFECTIVE INSTRUMENT, no calibration credit.** The three diagnoses below are preserved verbatim as the 8/20 record.)*

### 🔴 D1 · **LEG A IS STRUCTURALLY UNFIREABLE. This is the finding.** — ✅ **REPAIRED 2026-09-10 under WQ-160 (§3 banner); the diagnosis below is preserved as written on 2026-08-20.**

**`A(iii)` requires terminal throughput down ≥200 kbpd for **≥45 consecutive days**. The window is 2026-08-20 → 2026-09-30 = **42 days inclusive / 41 exclusive**.** LEG A requires **(i) AND (ii) AND (iii) AND (iv)** — all four. **⚠️ FIGURES CORRECTED 2026-08-20 (OSPREY, verifying rather than accepting):** a 45-day run beginning on the window's first day reaches **day 45 on 2026-10-03**, not 10-04 — I had computed `start+45`, which is **day 46**. And the day-count needs its convention named: **42 inclusive, 41 exclusive.** **⇒ THE COUNT-INDEPENDENT STATEMENT, adopted from OSPREY as the one that goes to Will: the LATEST START DATE for a >=45-consecutive-day run that could complete by Resolve_By is 2026-08-17 -- THREE DAYS BEFORE THE WINDOW OPENS. No in-window event can qualify, and that statement needs no arithmetic about completion dates or day-counting conventions.**

⇒ **LEG A cannot fire, by construction, for any in-window event whatsoever.** `finding_compound_gate_jointly_unsatisfiable` — individually satisfiable limbs, jointly unsatisfiable in the only state that matters.

**How it got there, and it is a new instance of the day's own defect class:** the **≥45d** figure originated in the **deleted γ limb** ("capacity observed offline ≥45 consecutive days"). When A(iii) was created in the redundancy-exhaustion repair, **the duration was carried across from the limb it replaced and never re-checked against the window.** The enumeration-inheritance finding (`KB-HAWK-287`) has a twin: **a repair inherits the PARAMETERS of the limb it replaces, not just the enumeration of the case it was derived from.**

**Consequence for the row as it stands: HAW-19 can only be falsified by LEG B — kinetic denial — which tests a different proposition than the row's central claim.** The row **cannot test its own headline claim**. The 70% was priced on two live legs.

### 🟠 D2 · The NO-VERDICT band's stated rationale references the deleted γ limb

The band reads: *"…grades NO-VERDICT on that leg — (gamma) is unreachable for late-window events by construction (45 days cannot have elapsed)."* **γ is deleted.** The band itself **survives and is correct**, but its reason is now **A(iii)**'s ≥45d, not γ's. **Editorial correction only — the band's trigger, date and effect are unchanged.** *(And per D1 the band is now near-vacuous: every in-window event, not merely late-window ones, fails the duration test.)*

### 🟠 D3 · `A(ii)(b)` has no numbers — "≥N of M" was never parameterized

**⚠️ AUTHORSHIP CORRECTED 2026-08-20, at OSPREY's insistence and on its evidence.** I wrote that D1 and D3 were *"on both of us."* OSPREY pulled its own recorded clause text (`KB-OSPREY-048`) and showed **both defects are in what IT authored**: it left N and M as unbound placeholders, and it carried the `≥45d` verbatim from the deleted limb its clause replaced. **Accurate split: OSPREY AUTHORED both clause defects; HAWK ADOPTED them into this row without checking.** Adopting a defective clause is not authoring one — and the row's defect is still mine to own, because the row is mine.

`finding_prereg_verdict_boundary_must_be_a_number` requires a boundary to be a **number**. **N and M were never specified.** ⇒ **The redundancy-exhaustion sub-limb is ungradeable as registered**, so in practice **A(ii) can only be satisfied by (ii)(a) — the damaged unit being the asset's ONLY loading path.** A candidate event needing (ii)(b) grades **NO-VERDICT on that limb**. **⚠️ STILL OPEN AS AT 2026-09-10, AFTER TWO RULINGS PASSED OVER IT** — neither WQ-160 nor WQ-212 reached D3, and WQ-212 leaves it unparameterized by express ruling.

---

## 3 · ⚖️ DECISION PUT TO WILL — **RULED 2026-09-10: option (b). CLOSED.**

> 🔴🔴 **SECOND RULING THE SAME DAY — WQ-212 (Will APPROVE, Decision Deck tap 2026-09-10 20:45Z; PROME packet `inbox/processed/2026-09-10_from-PROME_WQ-208-211-212-RULED-55-scored-batch-2-both-legs-HAW-19-defective-plus-successor.md`). THE REPAIR ABOVE FIXED THE INSTRUMENT; THIS RULING DISPOSES OF THE GRADE.**
> **On 2026-09-30 `HAW-19` resolves as a DEFECTIVE INSTRUMENT and takes NO CALIBRATION CREDIT.** The original letter, `Date_Made`, prediction text, 9/30 deadline and the **70%** are all kept unchanged.
> **⚠️ WQ-160 AND WQ-212 ARE BOTH LIVE AND THEY DO NOT CONFLICT — this is the one thing a future reader will try to reconcile, so it is written out here.** WQ-160 shortened A.3 and restored resolvability **forward from 9/10** (latest qualifying start 9/17). But LEG A was structurally unfireable for the **first 21 of the row's 42 days** (8/20 → 9/10), and **a forward repair cannot retroactively make a window's first half gradeable.** That un-gradeable half is exactly why the 9/30 print earns no calibration credit. A repaired instrument and an uncreditable grade are the correct pair here, not a contradiction.
> **LEG B is unaffected by the defect** and is still adjudicated on its own original letter and its own evidence through 9/30 — **a LEG-A design defect erases no demonstrated LEG-B failure.** The CONFIRMED path also still requires its **dated in-window search attempt** (FALCON + OSPREY ledgers · CENTCOM's own tally · a Kpler-or-Vortexa flow check): the row must not auto-confirm on neglect, and now must not auto-credit either.
> **D3 STAYS UNPARAMETERIZED BY EXPRESS RULING** — WQ-212 did not reach `A.2(b)`'s `≥N of M` either, so A.2 remains satisfiable only by (a). Two rulings have now passed over D3 without closing it; a future repair needs its own ruling and its own disclosure test.
> **A CAPACITY-ONLY SUCCESSOR IS RULED AND OWED:** prospective, separate event/observation windows **2026-10-01 → 2026-12-22**, its own disclosure test written on its own row, **registered before 2026-10-01**, PROME's deadline **2026-09-25** (DOCKET L321). ⚠️ **Those windows are Will's and SUPERSEDE the v2 draft calendar** (10/01→10/31 event, 12/14 observation) in `design/HAW19_MEASUREMENT_DRAFT.md`. ⚠️ **The successor is NOT registered by this banner and is NOT ready on data:** `audits/2026-09-08_HAW-19_data-feasibility.md` returns NOT READY — no licensed tracker access demonstrated, no matched 73-observation fixture (28 baseline + 45 observation days), no complete terminal/path universe, **no measured base rate behind the draft 65%, which stays uncalibrated and unregistered.** If the data cannot be obtained by 9/25, **narrow or redesign the letter — do not register a number because the dates became feasible.**
> **Naming note:** HAWK's packet proposed the label **STUCK**; the ruled word is **DEFECTIVE INSTRUMENT** and that is what is encoded on the row and everywhere downstream. Record: `KB-HAWK-361`.

> ✅ **RULED — WQ-160.** Will approved **option (b)** by Decision Deck tap **2026-09-10 15:21Z (11:21 ET)**, verbatim word **APPROVE**; relayed PROME → HAWK 2026-09-10 11:3x ET (`inbox/processed/2026-09-10_from-PROME_WQ-160-RULED-option-b-Status-class-repair-of-HAW-19-leg-A-with-disclosure.md`).
> **Executed the same day, 2026-09-10:** the **duration branch** — A.3's `>=45 CONSECUTIVE DAYS` → **`>=14 CONSECUTIVE DAYS`**. **`Resolve_By` was NOT extended** (extending it would extend the §0 claim window itself, adding days in which a qualifying event could occur — that raises P(FAILED) and moves scored mass; it would also destroy the registered IMMOVABLE anchor type).
> **Latest start date for a ≥14-day run completing by 2026-09-30 = 2026-09-17** (inclusive convention: 9/17 is day 1, 9/30 is day 14) — **28 days after the window opens, inside it.** LEG A is fireable again.
> **Confidence unchanged at 70%** — required, not merely permitted: the 70% was priced against two live legs, so restoring LEG A returns the row to its priced basis (`finding_resolvability_defect_is_status_not_confidence`).
> **Disclosure test RE-RUN at patch time (2026-09-10) and written into the row cell** — it comes out clean a second time, on three independent legs: ① no pre-registered non-fire is duration-keyed, so shortening the duration cannot resurrect one; ② an enumerated check of every candidate-shaped event across the elapsed window 8/20→9/10 (Novorossiysk 9/8-9 · Kstovo/NORSI 8/26 · Ryazan/Perm/Tatarstan/Saratov 9/6-8 · Sochi 9/3-4 · Jazan 9/7-8 · Ust-Luga 9/1 · Derya at Kharg 9/8 · Kylo/Riesco/the five 9/8 hulls/Hercules Star/New Andros · Mokha 9/10 · Sheskharis · Bukhta Sever 9/5-6) — **every one fails on a limb this patch does not touch**; ③ both owners independently report zero destroyed crude capacity (FALCON 9/10: *zero confirmed crude barrels offline, 195 days*; OSPREY 9/8: *barrels destroyed = zero*). **No grading anywhere in the window is altered.**
> **D2** is repaired as a side effect — the NO-VERDICT band is no longer near-vacuous and does the work it was written for; its trigger, date and effect are unchanged. **D3 stays OPEN and unpatched** — `A.2(b)`'s `≥N of M` is still unparameterized, so A.2 remains satisfiable only by (a). This ruling did not reach it.
> **Governing record:** the `A.3-vs-WINDOW REPAIR RECORD` at the end of §A in the HAW-19 Prediction cell. **The option table below is preserved as the decision record as it stood on 2026-08-20 — it is history, not a live decision.**


**D1 is a resolvability defect on the load-bearing leg.** Fleet canon (`finding_resolvability_defect_is_status_not_confidence`) says that is a **Status** matter, **never** a Confidence cut — pricing resolvability into confidence corrupts the record in both directions.

⚠️ **I am not repairing it unilaterally, and the reason is not squeamishness.** I refused two patches today on the ground that amending a live row while evidence arrives is fitting the spec to the evidence. **This would be the fifth structural change to a row registered the same morning**, and the fact that I can construct a good argument for it is exactly when the discipline should bind hardest.

**The disclosure test has been run, and it comes out clean:** **no in-window event's grading changes under either option.** Taman (7/30, re-struck 8/19) and Kharg (7/18→8/12) are both out of window on initiating cause; nothing else is a LEG-A candidate. So a repair would **not** be reaching for a result — but it is still **Will's call, not mine.**

| Option | Effect | Cost |
|---|---|---|
| **(a) Leave as-is** | Row resolves on **LEG B only**. LEG A recorded as structurally unfireable. | The 70% is **mis-priced** — it was set against two live legs. A CONFIRMED would be near-vacuous on the central claim. |
| **(b) Authorize a resolvability repair** | Either shorten A(iii)'s duration, or extend Resolve_By past 10/04, restoring LEG A. | A fifth same-day amendment. Mitigated: disclosure test clean, and it is a **Status**-class repair. |
| **(c) Retire and re-register** | Clean successor with the window and duration mutually consistent from the start. | Loses the calibration continuity; a row re-registered after in-window evidence needs the made-date test run explicitly. |

**My recommendation: (b), scoped as a Status-class resolvability repair with the disclosure test on the record.** *(→ RULED (b) 2026-09-10; see the banner at the head of this section. Executed via the duration branch.)* (a) leaves a row that cannot test what it claims — which my own falsification surface calls worthless — and (c) pays a real calibration cost to fix an arithmetic slip.

---

## 4 · Standing limits carried forward (recorded 8/20, deliberately unpatched)

- **Gap five — aggregation covers MOORINGS, not TANKAGE.** At a transshipment terminal tankage is the binding constraint (Taman: 10 tanks destroyed, moorings intact). `KB-HAWK-280`.
- **The initiating-cause window boundary.** A window opening mid-campaign systematically excludes the modal event class in a theater under continuous attack. `KB-HAWK-286`.
- **The regime bet.** A regime that holds throughout confirms the row **without ever stressing it**; a clean CONFIRMED is not a stressed test.
- **The remedy inherited an enumeration.** The redundancy-exhaustion clause enumerates loading points because it was derived from CPC's moorings. `KB-HAWK-287`.
