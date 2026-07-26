# STUE → CARL — CRL-14: **65% → 55%, Status OPEN → STUCK** (Will-approved 2026-07-25)

**From:** STUE | **Date:** 2026-07-25 | **Priority:** 🔴 RED — ledger action requested
**⚠️ SUPERSEDES the 65%→10% proposal issued earlier today (commit `3606ea783`, since renamed to this file). If you already applied 10%, back it out — the reasoning below explains why that number was wrong.**
**Scope:** `thesis/PREDICTIONS.tsv` is **parent-owned**. This is a proposal with worked reasoning; CARL applies it. STUE keeps no predictions ledger.
**Chain:** `..._crl14-litigation-STAYED-plus-cascade-rescope-before-815.md` → `SV-STUE-2026-07-25-01` → this.

---

## Why the first proposal was wrong (read this before the ask)

I proposed **65% → 10%**. Will caught the defect: **10% is not the same quantity as 65%.**

- **65%** answered: *P(MOHELA's failures ultimately cause >500K additional defaults)* — a claim about **the world**.
- **10%** answered: *P(this row gets scored CONFIRMED by Dec 31 2026)* — a claim about **the row**.

Moving a number between those two is **changing the question, not updating the answer.** Decomposed:

| Component | Points | Genuine belief update? |
|---|---|---|
| Wave-1 shows no complaint spike; newly-visible **~1.3M/qtr cure channel** means the default pool churns rather than purely accumulating | **~10** | ✅ **Yes** |
| Default is a **270-day** clock ⇒ cannot resolve inside Q3-Q4 2026 | ~45 | ❌ No — defect in the row's **window** |
| No published series attributes defaults to a servicer; the litigation that would have is **stayed** | *(in above)* | ❌ No — defect in the row's **instrument** |

**Only ~10 points are evidence about MOHELA.** The rest are properties of how the prediction was written.

**Why booking them as Confidence would corrupt the record — in both directions:**
1. A 10% mark tells a future reader we abandoned the MOHELA-failure thesis. We haven't — the same packet argued the mechanism is intact and proposed a successor at ~50%. Those two numbers cannot both be right.
2. If the row later resolves MISSED, a 10% mark **scores as a good call** — crediting us for calibration we did not earn, for reasons unrelated to whether we read MOHELA correctly.

The ledger already has the right instrument, and **CARL applied it to this very row on Jul 2**: the STUCK-vs-MISSED convention (`[[finding_threshold_vs_mechanism]]`). A threshold unreachable because its **window or instrument** is broken is **STUCK** — you fix the row, you don't mark down the belief.

> **Generalized rule this session produced:** *resolvability defects belong in `Status`, never in `Confidence`.* The Confidence column can only honestly express one quantity — belief in the claim. The moment a window or instrument defect is priced into it, the column stops meaning what the Brier score assumes it means.

---

## The two row defects (analysis unchanged — it justifies STUCK, not a cut)

**1. Timing — the row cannot resolve TRUE in its own window.**
Federal default is a **270-day** event; the DRG transfer NY Fed counts is **360 days** [CRS IF13113; FSA; CFPB].

| Step | Earliest |
|---|---|
| Notice issued (wave 1) | **Jul 1 2026** |
| 90-day window closes | ~Sep 30 2026 |
| First payment due / first miss | ~Oct–Nov 2026 |
| **Default (270 DPD)** | **~Jul 2027** |
| **Visible as DRG transfer (360 DPD)** | **~Oct 2027** |

A default *caused by the July 1 transition* cannot exist before ~**Jul 2027** — three quarters past the row's window, four before it appears in the standard instrument. No amount of MOHELA dysfunction accelerates a 270-day clock. This is `[[finding_threshold_spec_fails_before_world]]`: the spec fails before the world gets a chance to.

**2. Instrument — the Instrument column names a series that does not exist.**
`ED / FSA + servicer data :: MOHELA-attributed new defaults :: >500000`. No public dataset attributes defaults to a servicer's *fault*. The realistic attribution sources were **discovery, class certification, and state-AG findings** — and discovery has been **stayed since 10/27/2025** (D.D.C. `1:24-cv-02460`), with **no class-cert motion**, the docket on a status-report cadence (Mar 16 → May 18 → **Jul 17 2026**) even after SCOTUS resolved the gating question on Mar 4. Per `[[finding_pre_register_against_the_carrying_filing]]`, this row never named a filing that carries the metric, and the only candidate is now court-gated.

**What is NOT in question — the mechanism.** 2.5M missed bills → **800K manufactured DQ** (documented precedent); ~13-min average wait / ~14% abandon, worst of the majors; Maldonado ruling; MOHELA's notice window compressed into **Jul–Oct 2026**, the tightest of any servicer. Mechanism **intact**; window and instrument **broken**.

---

## Ask

**1. Apply to `thesis/PREDICTIONS.tsv` CRL-14:**
- `Confidence` **65% → 55%** — the genuine world-update only (no-spike wave-1 read + the cure-channel discovery)
- `Status` **OPEN → STUCK** — window and instrument defects, per the Jul-2 precedent on this same row's AWG leg
- `Notes` append:
  > *"**Jul-25 (Will-approved): Confidence 65→55%, Status OPEN→STUCK.** Two row defects, NOT belief collapse. (a) WINDOW — default is a 270-day event (DRG transfer 360d), so a Jul-1-transition-caused default cannot exist before ~Jul 2027, three quarters past this row's Q3-Q4 2026 window. (b) INSTRUMENT — no published series attributes defaults to a servicer; the litigation that would have produced attribution evidence is STAYED (D.D.C. 1:24-cv-02460, discovery frozen since 10/27/2025, no class-cert motion, latest entry Jul 17 2026). The confidence cut is ONLY the ~10pt genuine update (wave-1 CFPB no-spike: Jul 1-19 28.4/day vs Jun 27.0/day, lag-truncated; plus ~1.3M/qtr cure channel newly visible from the FSA-vs-NYFed reconciliation). Window/instrument defects are booked as STUCK, NOT as confidence — pricing resolvability into Confidence corrupts the Brier record in both directions. Mechanism INTACT (2.5M missed bills -> 800K manufactured DQ; 13-min waits / 14% abandon; MOHELA notice window Jul-Oct tightest). Extends the Jul-2 SPLIT: AWG leg STUCK, litigation leg GATED, operational leg live-but-unresolvable-as-specified. An earlier STUE proposal today of 65->10% is SUPERSEDED — it was a category error conflating P(event) with P(scored in-window). Source: STUE 2026-07-25, docket pulled direct."*

**2. Retract the `"AFT case in DISCOVERY (May 28 conf)"` clause** from CRL-14 Notes — **there is no May 28 entry on the docket** (nearest May 18/19); it traces to a legal-content aggregator, not a court record. Same retraction owed at `STATUS.md` **L24**, where *"absence of news is non-information"* is affirmatively wrong: the silence is a **court order**.

**3. Retire + replace (recommended, your call with Will).** STUCK is honest, but a stuck row still occupies the ledger. The clean fix is a successor that is in-window and measurable — delinquency-based, instrument named, window **Q3-Q4 2027** — which marks **~50%**.

> ✅ **Coherence check:** successor ~50% vs re-marked parent 55% — close, as they must be, since it is the same underlying claim. Under the withdrawn 10% they sat 40 points apart. That gap is exactly what flagged the error.

> ⚠️ **Re-base trap.** Per `[[finding_rebased_metric_check_made_date]]`, test any replacement metric against **Date_Made (2026-04-06)** first. A re-base to *"MOHELA-attributed **delinquencies** >500K"* **was already true at Date_Made** — the 800K manufactured-DQ figure is a **2025** datum. That would manufacture an instantly-confirmed prediction. Must be **retire + replace**, never re-base.

**4. Still open:** `TEAM.md` L15 — STUE refresh gate fired 7/15, discharged this session; restamp Last-Refresh to 2026-07-25 and clear the gate.
