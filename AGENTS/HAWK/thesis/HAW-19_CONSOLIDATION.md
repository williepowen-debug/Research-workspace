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

## 2 · 🔴 THREE DEFECTS THE CONSOLIDATION SURFACED — none patched

### 🔴 D1 · **LEG A IS STRUCTURALLY UNFIREABLE. This is the finding.**

**`A(iii)` requires terminal throughput down ≥200 kbpd for **≥45 consecutive days**. The window is 2026-08-20 → 2026-09-30 = **41 days**.** LEG A requires **(i) AND (ii) AND (iii) AND (iv)** — all four. **45 > 41**, so even an event on the window's first day completes its duration test on **2026-10-04**, four days after the row resolves.

⇒ **LEG A cannot fire, by construction, for any in-window event whatsoever.** `finding_compound_gate_jointly_unsatisfiable` — individually satisfiable limbs, jointly unsatisfiable in the only state that matters.

**How it got there, and it is a new instance of the day's own defect class:** the **≥45d** figure originated in the **deleted γ limb** ("capacity observed offline ≥45 consecutive days"). When A(iii) was created in the redundancy-exhaustion repair, **the duration was carried across from the limb it replaced and never re-checked against the window.** The enumeration-inheritance finding (`KB-HAWK-287`) has a twin: **a repair inherits the PARAMETERS of the limb it replaces, not just the enumeration of the case it was derived from.**

**Consequence for the row as it stands: HAW-19 can only be falsified by LEG B — kinetic denial — which tests a different proposition than the row's central claim.** The row **cannot test its own headline claim**. The 70% was priced on two live legs.

### 🟠 D2 · The NO-VERDICT band's stated rationale references the deleted γ limb

The band reads: *"…grades NO-VERDICT on that leg — (gamma) is unreachable for late-window events by construction (45 days cannot have elapsed)."* **γ is deleted.** The band itself **survives and is correct**, but its reason is now **A(iii)**'s ≥45d, not γ's. **Editorial correction only — the band's trigger, date and effect are unchanged.** *(And per D1 the band is now near-vacuous: every in-window event, not merely late-window ones, fails the duration test.)*

### 🟠 D3 · `A(ii)(b)` has no numbers — "≥N of M" was never parameterized

`finding_prereg_verdict_boundary_must_be_a_number` requires a boundary to be a **number**. **N and M were never specified.** ⇒ **The redundancy-exhaustion sub-limb is ungradeable as registered**, so in practice **A(ii) can only be satisfied by (ii)(a) — the damaged unit being the asset's ONLY loading path.** A candidate event needing (ii)(b) grades **NO-VERDICT on that limb**.

---

## 3 · ⚖️ DECISION PUT TO WILL — not taken here

**D1 is a resolvability defect on the load-bearing leg.** Fleet canon (`finding_resolvability_defect_is_status_not_confidence`) says that is a **Status** matter, **never** a Confidence cut — pricing resolvability into confidence corrupts the record in both directions.

⚠️ **I am not repairing it unilaterally, and the reason is not squeamishness.** I refused two patches today on the ground that amending a live row while evidence arrives is fitting the spec to the evidence. **This would be the fifth structural change to a row registered the same morning**, and the fact that I can construct a good argument for it is exactly when the discipline should bind hardest.

**The disclosure test has been run, and it comes out clean:** **no in-window event's grading changes under either option.** Taman (7/30, re-struck 8/19) and Kharg (7/18→8/12) are both out of window on initiating cause; nothing else is a LEG-A candidate. So a repair would **not** be reaching for a result — but it is still **Will's call, not mine.**

| Option | Effect | Cost |
|---|---|---|
| **(a) Leave as-is** | Row resolves on **LEG B only**. LEG A recorded as structurally unfireable. | The 70% is **mis-priced** — it was set against two live legs. A CONFIRMED would be near-vacuous on the central claim. |
| **(b) Authorize a resolvability repair** | Either shorten A(iii)'s duration, or extend Resolve_By past 10/04, restoring LEG A. | A fifth same-day amendment. Mitigated: disclosure test clean, and it is a **Status**-class repair. |
| **(c) Retire and re-register** | Clean successor with the window and duration mutually consistent from the start. | Loses the calibration continuity; a row re-registered after in-window evidence needs the made-date test run explicitly. |

**My recommendation: (b), scoped as a Status-class resolvability repair with the disclosure test on the record.** (a) leaves a row that cannot test what it claims — which my own falsification surface calls worthless — and (c) pays a real calibration cost to fix an arithmetic slip.

---

## 4 · Standing limits carried forward (recorded 8/20, deliberately unpatched)

- **Gap five — aggregation covers MOORINGS, not TANKAGE.** At a transshipment terminal tankage is the binding constraint (Taman: 10 tanks destroyed, moorings intact). `KB-HAWK-280`.
- **The initiating-cause window boundary.** A window opening mid-campaign systematically excludes the modal event class in a theater under continuous attack. `KB-HAWK-286`.
- **The regime bet.** A regime that holds throughout confirms the row **without ever stressing it**; a clean CONFIRMED is not a stressed test.
- **The remedy inherited an enumeration.** The redundancy-exhaustion clause enumerates loading points because it was derived from CPC's moorings. `KB-HAWK-287`.
