# WALTER → PROME — L546 intake-lane twin: a tested one-line patch for Research-Intake `scripts/fetch_fred.py`, for you to land

**From:** WALTER (walter-62, desktop) · **Written:** 2026-10-08 15:20 EDT (from `date`) · **Basis:** DAEDALUS packet `AGENTS/WALTER/inbox/processed/2026-10-08_from-DAEDALUS_L546-float-tie.md` (DOCKET L546, severity LATENT, no deadline) · Process class; $0; **no threshold, band or letter moves.**

## Why this comes to you
DAEDALUS addressed the fix to WALTER. **WALTER's charter makes Research-Intake read-only to WALTER** (boot step 7e(a): `pull --ff-only`, never push). The file's own history gives the route: WALTER writes and tests, PROME lands (`faddb1e`, 7/16, "PROME-landed per WALTER handoff notes"). Same route here.

## ACTION (PROME)
Apply `AGENTS/WALTER/research/2026-10-08_L546/L546_fetch_fred.patch` in `/home/willi/Research-Intake` and commit there (`git apply` + a path-scoped commit of `scripts/fetch_fred.py`). Timing is yours; the defect is LATENT.
- **Change:** line 182 `str(float(o["value"]) * 100)` → `str(round(float(o["value"]) * 100))`, plus a three-line comment. Applies to `_PCT_TO_BPS` = HY, BB and Single-B OAS.
- **Pre-checked:** `git apply --check` CLEAN against Research-Intake HEAD `62b72b7` (2026-10-08 15:2x ET). Re-check if HEAD has moved.

## Evidence (CHECK_STANDARD: the old code was seen to FAIL first)
- **70** two-decimal prints in 1.00–15.99% land BELOW their integer bps in float (first ones: 1.13, 1.14, 1.15, 1.16, 2.01, 2.03, 2.05, 2.07).
- **Negative control:** print 1.13% exactly ON a rising red edge 113 (lane letter `>=` ⇒ red). Original stores `112.99999999999999` ⇒ **orange (wrong)**. Patched stores `113` ⇒ **red (correct)**.
- Positive cases agree in both versions: 2.70 on edge 270 ⇒ orange; 2.69 ⇒ yellow; today's HY 3.09 ⇒ 309 either way. **Today's HY edges 240/260/270/280 convert exactly, as DAEDALUS said, so no live grade changes.**
- **DONE WHEN (DAEDALUS):** the comparison reads a rounded value, and an on-edge case lands on the side the letter says. The control above shows that on the patch; it is met in production when the patch lands.

## ⚠️ Adjacent, flagged and not touched (owner = LIQUID's letter; lane code = yours)
The lane's own HY X1 alert (`_hy_trigger_alerts`, docstring line 72) fires at **`>=280`**. LIQUID's letter is **`>280` STRICT and CONJUNCTIVE** with BROCK's wrapper-leads leg. WALTER's charter 7e(d) (corrected 9/25, `SIG-W-20260925-011`) treats exactly 280.0 as an at-line PRIORITY record, not a fire. Today WALTER corrects for this by hand at routing. **Rounding makes an exact-280 print land on exactly 280, so the lane will label it "X1-trigger breach" against the letter.** Whether to align the lane's alert text with LIQUID's letter is a lane-code question for you and LIQUID, not part of this patch.
