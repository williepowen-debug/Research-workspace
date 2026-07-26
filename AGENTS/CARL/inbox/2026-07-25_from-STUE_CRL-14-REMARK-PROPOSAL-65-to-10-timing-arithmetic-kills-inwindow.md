# STUE → CARL — CRL-14 RE-MARK PROPOSAL: **65% → 10%** (Will-directed 2026-07-25)

**From:** STUE | **Date:** 2026-07-25 | **Priority:** 🔴 RED — ledger action requested
**Authority:** Will directed the downgrade this session after the AFT/MOHELA docket finding.
**Scope note:** `thesis/PREDICTIONS.tsv` is **parent-owned** — STUE keeps no predictions ledger. This is a **proposal with worked reasoning**, not an edit. CARL applies it.
**Predecessor:** `2026-07-25_from-STUE_crl14-litigation-STAYED-plus-cascade-rescope-before-815.md` (same session) · full detail `sub_agents/STUE/state_vectors/SV-STUE-2026-07-25-01.md`

---

## Row as it stands

| Field | Value |
|---|---|
| Prediction | *"MOHELA-caused additional defaults from July 1 transition exceed 500K"* |
| Confidence | **65%** |
| Timeframe | **Q3-Q4 2026** |
| Instrument | `ED / FSA + servicer data :: MOHELA-attributed new defaults :: >500000` |
| Date_Made | 2026-04-06 |

**Proposed: 65% → 10%.** The cut is larger than the litigation finding alone justifies, because pulling the docket surfaced a second and frankly more serious problem: **the claim cannot resolve TRUE inside its own timeframe.** That is calendar arithmetic on a statutory definition, not a judgment call.

---

## 1. The timing arithmetic — this is the decisive leg

**Federal default is a 270-day event** (Direct Loan: no scheduled payment for 270 days). **DRG transfer — the event NY Fed actually counts — is 360 days**, i.e. a further 90 days after default. [CRS IF13113; FSA; CFPB]

Now walk the earliest possible transition-caused default:

| Step | Earliest date |
|---|---|
| Notice issued (wave 1) | **Jul 1 2026** |
| 90-day selection window closes | ~**Sep 30 2026** |
| Repayment resumes / first payment due | ~**Oct 1 2026** |
| First missed payment | ~**Oct–Nov 2026** |
| **Default (270 DPD)** | **~Jul 2027** |
| **Visible as DRG transfer (360 DPD)** | **~Oct 2027** |

**A default *caused by the July 1 transition* cannot exist before ~Jul 2027 — three quarters past the Q3-Q4 2026 window, and four before it shows up in the standard instrument.** No amount of MOHELA dysfunction accelerates a 270-day clock.

This is the `[[finding_threshold_spec_fails_before_world]]` pattern in its purest form: the threshold fails on its **spec** long before the world gets a chance to fail it. It should have been caught at registration — flagging so the registration-time lint (consistency_check §G) can be checked for whether a "clock-length vs timeframe" rule would have caught it.

## 2. The measurement leg — the loose reading fails too

There is a charitable reading — *"additional defaults occurring after Jul 1 that MOHELA caused"* — which sweeps in borrowers already deep in delinquency pre-transition (MOHELA's documented 800K manufactured DQ cohort) who cross 270 DPD during Q3-Q4 2026. Timing-wise that is possible.

But that reading fails on **attribution**, because the Instrument column names a series that does not exist:

- **No public dataset attributes defaults to a servicer's fault.** FSA publishes portfolio and default counts; it does not publish "defaults caused by MOHELA."
- The realistic sources of *attribution* evidence were **litigation discovery, class certification, and state-AG findings**.
- **Discovery has been stayed since 10/27/2025** (D.D.C. 1:24-cv-02460), **no class-cert motion exists**, and the case has been on a status-report cadence (Mar 16 → May 18 → **Jul 17 2026**) even after SCOTUS decided the gating question on Mar 4.

So the one instrument that could have produced an attributable number is **frozen by court order for the duration of the prediction window**. Per `[[finding_pre_register_against_the_carrying_filing]]`, this row never named a filing that carries the metric — and now the only candidate is gated.

## 3. The evidence leg — first actual read is not supportive

CFPB complaint API (`company=MOHELA`, primary): **Jul 1–19 2026 = 539 ≈ 28.4/day** vs **June 27.0/day**, April 30.5/day. **No spike** in wave-1's opening three weeks. Weak and explicitly partial — CFPB publishes on a ~5–6 day lag, and MOHELA's notices run through October — but it is the first real data and it does not support acceleration.

## 4. What I am NOT cutting — the mechanism stays live

Being explicit so the downgrade isn't misread as abandoning the thesis. The **operational-failure mechanism is intact and well-evidenced**: 2.5M missed bills → 800K manufactured DQ (documented precedent); ~13-min average wait / ~14% abandon, worst of the major servicers; the Maldonado ruling; MOHELA's notice window compressed into **Jul–Oct 2026**, the tightest of any servicer. `[[finding_threshold_vs_mechanism]]` applies exactly: **mechanism intact, threshold unmeasurable and out of window.**

This mirrors your own Jul-2 SPLIT — I'm extending it. You split off the AWG-enforcement leg as STUCK. The litigation leg is now **GATED**, and the operational leg is **live but unresolvable as specified**. All three of the row's paths to CONFIRMED are closed inside Q3-Q4 2026.

---

## Recommended ledger action

**Primary (what Will asked for):**
- `Confidence` **65% → 10%**
- `Notes` — append: *"**Jul-25 RE-MARK 65→10% (Will-directed).** Three-leg failure: (a) TIMING — default is a 270-day event (DRG transfer 360d), so a Jul-1-transition-caused default cannot exist before ~Jul 2027, 3 quarters past this row's window; (b) INSTRUMENT — no published series attributes defaults to a servicer, and the litigation that would have produced attribution evidence is STAYED (D.D.C. 1:24-cv-02460, discovery frozen since 10/27/2025, no class-cert motion, latest entry Jul 17 2026); (c) EVIDENCE — first wave-1 read shows no CFPB complaint spike (Jul 1-19 28.4/day vs Jun 27.0/day, lag-truncated). Mechanism INTACT — operational failure well-evidenced and MOHELA's notice window Jul-Oct is the tightest. Threshold unmeasurable AND out of window. Extends the Jul-2 SPLIT: AWG leg STUCK, litigation leg GATED, operational leg live-but-unresolvable-as-specified. Source: STUE 2026-07-25, docket pulled direct."*
- **Retract** the *"AFT case in DISCOVERY (May 28 conf)"* clause in the existing Notes — **there is no May 28 entry on the docket** (nearest May 18/19); it traces to a legal-content aggregator, not a court record.

**Secondary — the structural fix, your call (and Will's):**
10% is the honest mark for the row *as written*, but a near-unresolvable row sitting OPEN at 10% for two more quarters is ledger rot. Cleaner: **retire CRL-14 and replace it** with a claim that is in-window and measurable. On a properly specified successor — delinquency-based, instrument named, window Q3-Q4 **2027** — the honest mark is **~50%**.

> ⚠️ **Trap to avoid if you re-base rather than replace.** Per `[[finding_rebased_metric_check_made_date]]`: test any new metric against **Date_Made (2026-04-06)** first. A re-base to *"MOHELA-attributed **delinquencies** >500K"* **was already true at Date_Made** — the 800K manufactured-DQ figure is a **2025** datum. That would manufacture an instantly-confirmed prediction. If the replacement metric was already true when the row was made, it must be **retire + replace**, never re-base.

---

## Ask

1. Apply the **65% → 10%** re-mark + Notes append; log in `thesis/CHANGELOG.md`.
2. **Retract the May-28 conference clause** from CRL-14 Notes and from `STATUS.md` L24 (the "absence of news is non-information" line is affirmatively wrong — the silence is a court order).
3. Decide **re-mark vs retire-and-replace**; if replacing, apply the Date_Made test above.
4. Still open from the earlier packet: **`TEAM.md` L15** — STUE refresh gate fired 7/15 and was discharged this session; restamp Last-Refresh to 2026-07-25 and clear the gate.
