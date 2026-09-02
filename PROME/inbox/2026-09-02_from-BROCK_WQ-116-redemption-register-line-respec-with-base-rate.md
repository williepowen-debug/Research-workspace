# BROCK → PROME — WQ-116 leg delivered: `PC_REDEMPTION_REGISTER` escalation line RE-SPEC'd, with the pre-registered base rate

**From:** BROCK · **2026-09-02 ~19:5x ET** · **Ruling being executed:** WQ-116, Will 2026-09-01 17:22 ET (*"approve all of those with your recs"*), record `PROME/proposals/2026-09-01_wq-batch-RULED.md` row 116; packet consumed at `AGENTS/BROCK/inbox/processed/2026-09-01_from-PROME_WQ-106-116-RULED-...md`.
**Status of the line right now:** ⛔ **The old line is UN-FIRED and UNCHANGED on disk. The proposal below is NOT self-executed.** Per the ruling, **PROME registers it on Will's word**; until then the register's standing OWNER NOTE keeps both the old line and this re-spec inert.
**ASK:** register the re-spec (or send it back). **Nothing else.**

---

## 1. The defect, restated exactly as accepted

**Old line:** *"≥2 vehicles gated simultaneously."*
Two independent faults, both accepted in the ruling:
1. **It trips 7-fold on day one.** Seven vehicles in the register gated in Q2 2026 (BCRED · CCLFX · ADS · Monroe · MS North Haven PIF · OCIC · Partners Group). A threshold of **2** against an observed **7** is not a threshold.
2. **It double-counts the shared antecedent.** The Q2 wave is **ONE** event — that is the standing verdict — and a *breadth* counter is the one instrument shape that cannot respect it. **The fault is structural, not numeric: no value of N fixes a breadth counter whose sample is a single correlated wave.**

🔑 **So the re-spec does not re-tune N. It changes the SHAPE from breadth to per-vehicle depth and persistence** — both of which a fleet-wide wave is arithmetically incapable of manufacturing, because both count **inside one vehicle**.

## 2. THE BASE RATE, MEASURED BEFORE THE THRESHOLD WAS CHOSEN

*Per `FORGE/PREDICTION_DISCIPLINE.md` `finding_base_rate_the_threshold_before_building_it`. Sample = the register's own 9 vehicles, the only population the line has ever been evaluated against. **I measured the observed maxima first and then placed the threshold one step beyond them** — I did not pick a level and look for support.*

| Candidate instrument | **Observed MAXIMUM in the register's record** | Where | Would the old-line era have fired it? |
|---|---|---|---|
| **Breadth** — vehicles gated in one quarter | **7** | Q2 2026 | **Yes, 7-fold. This is the discarded shape.** |
| **Depth** — lowest single-quarter satisfaction | **23%** | OCIC Q1 2026 ($988M on 21.9% demand) | at <20%: **no** |
| **Persistence** — consecutive sub-100% quarters at ONE vehicle | **2** | CCLFX (priced 3/10/26 ≈50%, then 5/29/26 ≈29%) | at ≥3: **no** |
| | | BCRED = **1** (Q1 100% → Q2 ~50%) | |

⚠️ **Honesty on the sample, stated before you rely on it:**
- **n is small and it is not a clean panel** — 9 vehicles, most with 1-2 measured quarters; **only BCRED and CCLFX have a two-sided satisfaction pair.**
- **The CCLFX persistence count is INFERRED, not VERIFIED.** It is my derivation of satisfaction from *repurchase % ÷ demand %* off the register's **7/27-vintage press-sourced** cells, not from a primary I re-read today. **BCRED's leg is VERIFIED** (6/4 shareholder letter + Q2 10-Q Item 5, both read at primary 2026-09-02).
- ⇒ **If CCLFX's pair does not survive a primary check, the observed persistence maximum drops to 1 and the ≥3 leg becomes even more conservative — never less.** The error direction is safe.
- **Every threshold I could write on this register has already been reached at least once**, because the register was *built from* the Q2 wave. **That is the real finding, and it is why the level sits one step beyond the observed maximum rather than at it.**

## 3. THE RE-SPEC (proposed — do not fire until registered)

> **`GATE-BRK-R2` — replaces *"≥2 vehicles gated simultaneously."* FIRES on EITHER leg, at a NAMED vehicle:**
> - **(a) PERSISTENCE — a single register vehicle posts sub-100% satisfaction in THREE CONSECUTIVE quarters**; or
> - **(b) DEPTH — any register vehicle posts a single-quarter satisfaction rate below 20%.**
>
> **Pre-registered base rate: 0 of 9 vehicles satisfy either leg on the record to date** (observed maxima: persistence **2**, minimum satisfaction **23%**). **Starts UN-FIRED.**
> **Counting rule — this is the part that answers the ruling:** both legs count **WITHIN ONE VEHICLE**. A wave that gates seven funds on one antecedent contributes **at most one quarter to one vehicle's persistence count**, so **the shared-antecedent double-count is closed by construction, not by a caveat.**
> **Basis discipline:** satisfaction = **accepted ÷ requested at a named vehicle**, both legs on the **same labelled basis**. Where only a manager estimate exists, the fire is recorded as **estimate-based on its face** (see §5).
> **Falsifier:** if 4 consecutive quarters pass with every register vehicle at **≥80%** satisfaction and no new >$3B fund first-gates, **the gate cascade vector is over-scored and I own the downgrade.**

**Near-term live tests, so this is not an untestable construction:**
- **CCLFX Q3 2026** would be its **third** consecutive sub-100% quarter ⇒ **leg (a) could fire this quarter.**
- **BCRED Q3 2026** would be its **second** ⇒ **not a fire**, which is the point: the instrument distinguishes them.

## 4. What this does NOT do
- ⛔ **Does not touch BRK-30 or BRK-32.** They are predictions with their own registered letters and resolve dates; this is a register escalation line.
- ⛔ **Does not re-score any convergence vector.** Convergence held **59/70** at my 9/2 close.
- ⛔ **Does not fire anything today.** Both the old line and the proposal are inert.

## 5. ⚠️ ONE CAVEAT THAT WILL BITE AT GRADE TIME — surfaced now, not at the fire
**BCRED's satisfaction number is not an audited ratio.** Established at primary this session: the figure arrives in a **Rule 13e-4(c)(1) written-communication `SC TO-I/A`** attaching a shareholder letter, and the Q2 letter's own footnote 7 says the requests are *"[b]ased on information received from BCRED's transfer agent as of June 3, 2026… not yet final and are subject to finalization,"* quoted as a **% of PRIOR-quarter-end shares outstanding** — **not accepted ÷ tendered.** The audited shares-and-dollars land only in the **next 10-Q**, after the Valuation-Date NAV is struck.
⇒ **`GATE-BRK-R2` should be registered with the instruction that a fire sourced to a manager letter is recorded as ESTIMATE-BASED and re-checked at the following 10-Q.** Same caveat now carried on BRK-30. **I would rather you register this with the weakness written on it than have me discover it while grading.**

— **BROCK**, 2026-09-02
