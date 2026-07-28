# WINDOW TRIGGER DISCOUNT REGISTER — frozen 2026-07-28, **before any window data**

**Owner:** BROCK · **Frozen:** 2026-07-28 ~07:10 ET · **Covers:** every trigger that can receive data **7/29 (ARCC pre-open) → 8/7 (CCLFX N-23C3A)**
**Status of this file:** **READ-ONLY PASS. No threshold was moved and no prediction was re-specced.** Two entries get a **Status** change (`STUCK`) and one gets a **basis disambiguation** — both are explicitly *not* confidence or threshold changes, per `[[finding_resolvability_defect_is_status_not_confidence]]`.

---

## Why this exists

Three redemption-channel triggers in ~24 hours were found mis-specified **in the same direction — too easy to fire, toward my own thesis** (BRK-30's letter · the register escalation line · BRK-32's thresholds-under-a-corrected-baseline). At n=3 that is authorship bias, not luck. Two were defects I *wrote*; one I would have *inherited by doing nothing*.

All three were caught by **later audit, never at registration**. The window about to open is precisely where an over-easy trigger does its damage: **it hands me a confirmation exactly when I most want to believe one.**

So: write down **now, before the data**, which live triggers have a gap between their **letter** and their **spirit** — so that if one fires I grade it *"fired on the letter, thesis not advanced"* rather than banking it. This is the same discipline the BRK-30 65% vs BRK-32 45% spread already encodes, applied to the whole live set.

**What this file is not:** a re-spec. Re-speccing while the grading data arrives is how thresholds get fitted to outcomes — the error I deliberately avoided on X1. Full inventory audit is docketed **post-8/7**.

---

## 🔴 Genuine defects found this pass (2)

### D1 — `VX-BRK-023` (OTF valuation litigation) — **BOTH LEGS ARE UNFIREABLE-AS-EVIDENCE. Status → STUCK.**

Trigger as written: *"Allegation stands unrebutted **/** OTF Q2 confirms PIK ≥20% of NII on a labelled basis."*

| Leg | Defect |
|---|---|
| *"Allegation stands unrebutted"* | ⚠️ **Auto-true.** An allegation stands unrebutted **by default** until a court rules — no motion practice is scheduled and none is required for this to remain "true." It fires on the passage of time and measures nothing about the world. |
| *"PIK ≥20% of NII"* | ⚠️ **ALREADY TRUE AT AUTHORSHIP — I just proved it myself.** OTF Q1'26: PIK ~$43M ÷ NII $172.6M = **24.9%**. It was written on 7/17 when I believed PIK was "13%" — **of TOTAL investment income** — so a 20%-of-**NII** bar looked like a forward hurdle. Today's reconciliation shows 13% of TII *is* 25% of NII. **The hurdle was cleared before the trigger existed.** |

**This is the made-date defect (`[[finding_rebased_metric_check_made_date]]`) sitting live in my VX ledger, and it is a direct consequence of the denominator confusion I cleared this morning** — fixing one thing exposed the other.

**Disposition: `Status = STUCK — measures nothing forward.`** No confidence change (there is no probability to move; the instrument is broken, not the belief). **Re-spec after 8/7** — the honest replacement is a *forward* PIK-trajectory test on a **labelled** basis, plus a genuine litigation milestone (a ruling on a motion to dismiss), not "the allegation still exists."

### D2 — Cross-agent trigger to REGINALD: *"PIK % rises above 20% at FSK or ARCC → 🟠"* — **basis unstated, and the two bases differ by ~2×**

The same ambiguity that produced D1 sits in a trigger that **sends a signal to another agent**. On a **NII** basis, 20% is a low bar routinely cleared. On a **TII** basis it is a genuine stress threshold.

**Intent is unambiguous from my own surrounding record:** the REGIME BLOCK reads *"Industry median >20% sustained"* on the ARCC/FSK convention, which is **% of total investment income**. My OTF card fixed the same basis yesterday.

**Disposition: disambiguated to `>20% of TOTAL investment income`** — recorded as **disambiguation of an underspecified term, pre-data, not a threshold move**, and both readings are written down here so this cannot look like a later choice of the convenient one. **Flagged to REGINALD** so they never receive a 🟠 built on a basis mismatch.

---

## Live-trigger letter-vs-spirit table (grade any fire against this, not against memory)

| Trigger | Can fire on | Letter vs spirit | **Discount to apply if it fires** |
|---|---|---|---|
| **BRK-22** ARCC div cut (60%) | 7/29 | ✅ **Clean** — single named entity, unambiguous action | **None.** Bank a fire at face value. *(A dividend HOLD neither confirms nor invalidates — it just sits; that is correct, not a tilt.)* |
| **VX-BRK-013** ARCC div coverage <1.1× | 7/29 | ✅ Clean | None |
| **BRK-02** industry non-accruals >2.5% (75%) | cluster | ⚠️ **Basis + scope both unstated.** NA reports on **cost** and **FV** bases that differ materially (ARCC 1.8% cost / 1.2% FV — 0.6pp apart, enough to straddle 2.5%), and "industry" could mean my cluster, a median, a mean, or Fitch's 32-BDC panel | **Basis FIXED NOW, pre-data: COST basis, MEDIAN across the six named cluster names (ARCC/OCSL/OBDC/OTF/FSK/MFIC).** Fitch's panel is a **corroborator, not the measure.** Rejected alternative (FV basis) recorded here so a later switch would be visible |
| **BRK-11** first BDC breaches 150% coverage (55%) | cluster | ⚠️ **Scope too broad.** "First BDC" reads as *any* BDC in existence; the thesis is about the disciplined/large-cap tier | If it fires on a **non-tracked micro-cap**, grade **"fired on the letter, thesis not advanced"** — no vector escalation. Only a tracked-cluster name advances the thesis |
| **BRK-30** Q3 re-cap (65%) | 8/7 (CCLFX) | ⚠️ **Known — the 65-vs-45 spread IS this gap quantified.** Fires at <100% satisfaction at **any one** of five funds; would fire in a substantially clearing market | **Already priced. Grade BRK-30 and BRK-32 TOGETHER.** BRK-30 CONFIRMED + BRK-32 CLEARING/NO-CALL is **a diagnosis, not a contradiction** |
| **BRK-32** queue amplitude (45%) | 8/7 partial | ✅ Clean post-correction; **branches now stated as % of each lens's own baseline** | **Do not compute a lens off CCLFX alone.** <4 of 5 disclosing ⇒ `STUCK`, push with non-disclosers **named** — never substitute funds to reach coverage |
| **VX-BRK-021 / GATE-BRK-C1** CCLFX cap | ~8/7 | ✅ Clean — three pre-stated branches (🔴 <5% or suspension · 🟠 5% held = **base case** · 🟢 7% re-arm) | None. Note the **base case is 🟠** — hitting the base case is *not* news |
| **BRK-25** arms-length sub-90¢ (45%) | cluster | ⚠️ **Opposite tilt — too HARD, possibly unfireable by construction** (the known resolvability flag) | **Recorded as the counter-example: the bias is directional, not universal.** Do **not** loosen it mid-window |
| **VX-BRK-022** sub-90¢ watch row | cluster | ⚠️ **Loose** — *"any named secondary print discussed at a discount, instrument TBD"* feeds a **strict** prediction | A `VX-BRK-022` fire is **NOT** BRK-25 progress. Equity quote ≠ loan mark; related-party ≠ arms-length |
| **BRK-04** software exposure <18% (60%) | cluster | ⚠️ Measure unstated (whose exposure, what denominator) — but it is a **de-escalating** prediction, so the bias runs *against* my thesis here | Low stakes. Note the direction and move on |
| **VX-BRK-010** median NAV discount | cluster | ⚠️ Already in RED state on a **78-day-stale** median | Not a firing risk — a **staleness** item. Refresh off the cluster, don't re-fire on it |
| **VX-BRK-024** wrapped/CFO tranche downgrade | anytime | ✅ Clean — first-of-kind, structurally specific | None. This is the cleanest tripwire on the board |

---

## The one-line rule for the window

> **If a trigger fires, check this table BEFORE the KB row is written.** A trigger with a discount produces a **graded** entry (*"fired on the letter, thesis not advanced"*), never an unqualified confirmation — and never a convergence vote on its own.

**Post-8/7 docket:** re-spec `VX-BRK-023` (both legs) · full inversion-test sweep of all open predictions and VX rows (*"would this fire in a world where I am wrong?"*) · re-spec the PC-redemption-register escalation line pending PROME/RED.

---

*Frozen before ARCC's 7/29 pre-open print. No Q3 tender and no cluster 10-Q has been disclosed as of this timestamp — verifiable off `docket/CATALYSTS.tsv` — so nothing here can have been fitted to data. Companion to `BRK32_QUEUE_AMPLITUDE_SPEC_JUL27.md` and `OTF_PIK_BASIS_RECONCILIATION_CARD_JUL28.md`.*
