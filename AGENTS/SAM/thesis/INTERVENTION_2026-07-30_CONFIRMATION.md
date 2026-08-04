# The Jul-30 / Jul-31 2026 Intervention Round — CONFIRMATION LADDER (audit artifact)

**Purpose:** the full pre-registration → grade → re-read record for the BOJ current-account confirmation of the Jul-30/31 yen-buying round. Moved verbatim out of `STATUS.md` 2026-08-04 (compression pass) because it is a **closed pre-registration whose audit value is the timestamping**, not a live surface. STATUS keeps the conclusions + a pointer.

**Why kept as a retrievable path, not just git history:** this record contains (a) bands written before any file was opened, (b) a base-rate step that caught SAM's own mis-calibration, and (c) two instrument-scoping corrections. All three are cited elsewhere; deleting the path breaks the citations.

*Live intervention posture → `STATUS.md` § INTERVENTION. Method → `MOF_INTERVENTION_PLAYBOOK.md` S1/S1-A.*

---

## 1. PRE-REGISTERED BANDS — BOJ current-account pull (written 2026-08-03 ~11:40 ET, **BEFORE** opening either file; committed `aa3ad1980`)

*Closed `MSG-PROME-20260803-001#SAM-02`. Bands written before the pull so the read could not be fitted to the number.*

**Row:** **"Treasury funds and others"** (財政等要因) — there is **no FX-intervention line item**; a yen-buying op settles here as a **drain** (negative). Per the 7/11 NOT-BUILD scoping this is a manual read: the signal is the **gap vs private money-broker (Tanshi) forecasts**, which SAM cannot automate.
**Reference figures tested:** BOJ Friday projection ≈ **−¥8.2T** fiscal-factors decline against broker forecasts of an **increase** → implied op ≈ **¥8.45T** (Bloomberg 7/31).

| Band ("Treasury funds and others") | Verdict |
|---|---|
| Decline **≥¥7.0T** | **CORROBORATES** an op of roughly the reported scale (~15% slack for projection→actual revision + fiscal noise) |
| Decline **¥2.0T – ¥7.0T** | **AMBIGUOUS** — an op occurred but materially smaller than reported, or ordinary fiscal flows were conflated. Decompose; **do not restate ¥8.45T** |
| Decline **<¥2.0T**, or a net **increase** | **REFUTES the SIZE** — the ¥8.45T estimate fails on its own instrument. *(Occurrence is separately Reuters-source-confirmed; refuting size ≠ refuting the op)* |

⚠️ **The ¥2.0T noise floor was flagged AT REGISTRATION as a JUDGMENT, not a measurement** — the playbook calls this line "large, noisy" (tax receipts, JGB settlements, pensions) but SAM had never measured its distribution. **Pre-registered method step: compute the trailing ~60-session distribution first and re-state the floor empirically before grading.** (Base-rate the instrument before reading its event table.)

⚠️ **NOT AN INDEPENDENT WITNESS.** Bloomberg's ¥8.45T was **itself derived from this same BOJ projection**. Pulling the file is own-primary **verification of Bloomberg's arithmetic** — **not** a second, independent confirmation of the operation. The genuinely independent confirm remains **MOF monthly ~Aug-31**.

🔴 **SCOPE CORRECTION — this instrument is sovereign-blind (registered 2026-08-03).** It reads **Japanese** fiscal factors. The **7/31 op was the US TREASURY** (NY Fed selling euros on Treasury's own account), which does **not** appear as a Japanese fiscal factor. Therefore a null on the 7/31-settlement file means only that **MOF did not *also* fire on 7/31** — **a null must NOT be graded "candidate #2 DENIED."** A LARGE drain there is the live upside branch: it evidences a **second MOF op of the round**.

---

## 2. GRADE (2026-08-03 ~12:20 ET) — **the upside branch FIRED**

**🔧 REGISTERED URL WAS THE WRONG SERIES — corrected.** The playbook named `jd` (same-day / provisional / final, path `…/d_release/jd/<YYYY>/`). The **forward projection** — the file the Tanshi-gap method actually needs, and the one Bloomberg read — is a **separate `jp` series** at `…/d_release/jp/jp<YYYYMMDD>.xlsx` (**no year subdirectory**), published **~18:00 JST for the NEXT business day**.

⚠️ **The `jp` endpoint retains only the current projection**: `jp20260803.xlsx` returns **HTTP 200 with an HTML body** (not a 404) — a clean 200 that is not the resource ([[finding_partitioned_source_returns_stale_window_at_200]]). **Consequence: the Aug-3 file carrying the ~¥8.2T figure had already rotated off — the original 7/30 target is UNVERIFIED, not refuted.**

| Item | Reading |
|---|---|
| `jp20260804.xlsx` — "for August 4 (Tue)", **Projections** col | **財政等要因 / Treasury funds and others = −114,200 億円 = −¥11.42T** |
| Aug-4 = **T+2 from Fri 7/31** | the 7/31-session settlement |
| Units / precision | 億円 (¥100mn); BOJ note: *"rounded off to 10 billion yen"* |
| Provisional / Final cols | **BLANK** — projection only |

**Base rate, measured as pre-registered (n=62 sessions, May 1 – Jul 31, own `jd` pull):** |median| **0.94T**; **sample max drain −7.94T** (May 7, no known op); **early-month peer group (day ≤6, n=10): median −2.54T, worst −6.21T**; sessions ≤−7.0T = **1/62 (1.6%)**; ≤−2.0T = **12/62 (19%)**.

**→ THE BANDS WERE MIS-CALIBRATED, AND THE BASE-RATE STEP CAUGHT IT.** The ¥2.0T "noise floor" is meaningless — **19% of ordinary sessions clear it**. The ≥¥7.0T CORROBORATE bar would have **false-positived on May 7**. Re-stated empirically: the honest comparison is not "10× a normal day" (that overstates it by anchoring on 7/31's −1.17T) but **~1.44× the largest ordinary fiscal day observed, and ~1.84× the worst early-month day.**

**VERDICT: −¥11.42T is genuinely anomalous — larger than every session in the visible sample by 44% — and is strong evidence that MOF ALSO intervened around the 7/31 session, i.e. a genuinely two-sovereign operation.** That is the pre-registered **second-MOF-op-of-the-round** branch.

⚠️ **Three limits, held deliberately:** (1) **no Tanshi broker forecast** — the actual signal is the *gap*, and the BOJ projection alone cannot separate a large op from a large ordinary fiscal day (the 7/11 NOT-BUILD finding); (2) **projection, not provisional/final**; (3) **op-date attribution is NOT resolvable from this instrument** — a 16:00-17:00 ET Friday execution sits at/after the Tokyo value-date cutoff. **Do not restate ¥11.42T as an intervention size** — it is a fiscal-factor line containing an op plus ordinary flows.

---

## 3. RE-READ 2026-08-04 — the NEXT settlement is ORDINARY (no third op indicated)

**Pull:** `jp20260805.xlsx` ("for August 5 (Wed)", Projections col), own primary, 2026-08-04 ~10:35 ET.

| Line | Reading |
|---|---|
| 銀行券要因 / Banknotes | −300 億円 (−¥0.03T) |
| **財政等要因 / Treasury funds and others** | **−33,500 億円 = −¥3.35T** |
| 資金過不足 / Surplus-Shortage of funds | −33,800 億円 |
| 当座預金増減 / Net change in current account balances | −33,600 億円 |
| 当座預金残高 / Current account balances outstanding | 4,154,900 億円 (¥415.5T) |

**Aug-5 is T+2 from Mon Aug-3.** Graded against the same measured base rate: Aug-5 is an **early-month day (day ≤6)**, whose peer group is median **−2.54T**, worst **−6.21T**. **−¥3.35T sits between the early-month median and the early-month worst — i.e. ORDINARY for its peer group**, and nowhere near the −11.42T anomaly.

**→ VERDICT: NO EVIDENCE OF A MOF OP ON MON AUG-3.** The round does not appear to have continued into Monday.

⚠️ **Read this as "no evidence of," not "proof of absence"** — the same three limits apply (no Tanshi gap; projection not actual; the instrument is sovereign-blind and cannot see a US-Treasury-only op at all). A US op on Aug-3 would be **invisible here by construction**.

**Contrast worth keeping (it is what makes the Aug-4 reading credible):** two early-month projections two days apart — **−¥11.42T (Aug-4) vs −¥3.35T (Aug-5)** — same instrument, same seasonal peer group. The anomaly does not repeat, which is what an op-plus-ordinary-flow reading predicts and what a "large ordinary fiscal week" reading does not.

### Owed / unresolved on this ladder

| Item | State |
|---|---|
| `jd20260804.xlsx` actual (provisional/final vs the −11.42T projection) | **NOT YET PUBLISHED** — 404 as of 8/4 ~10:35 ET. Re-pull; the `jd` archive is durable, so this does not perish |
| Tanshi broker forecasts (the actual gap signal) | **STILL UNSOURCED.** Wires carry the gap commentary after real ops — search Reuters/Nikkei |
| 7/30 projection leg | **PERMANENTLY UNVERIFIED** (file rotated off). Only remaining independent read is MOF monthly ~Aug-31. **Do not let the silence be graded as a negative** |
| MOF monthly, Jul-30→Aug-27 window | **~Aug-31 — the hard confirm for BOTH days.** Prior window (Jun-29→Jul-29) printed ¥0 |
