# PHAN -> CARL: Fed SHED reads BNPL late payment 26% and flat; our RED band rests on one house reading 47% and rising

**Date:** 2026-10-28 (PM news pass, Will-directed) · **From:** PHAN (dossier) · **To:** CARL
**ACTION:** rule which survey house carries the BNPL late-rate band in STATUS row 25, or carry both with basis labels.
**Narrative:** `AGENTS/CARL/sub_agents/PHAN/PASSES.md` § "2026-10-28 PM pass". PHAN proposes, CARL disposes. Nothing resolved or re-marked here.

## 1. The miss

The Fed's **SHED 2025** (*Report on the Economic Well-Being of U.S. Households in 2025*, published **2026-05-13**; survey fielded October 2025, ~13,000 adults) has a BNPL section. A grep of PHAN/, CARL `STATUS.md` and `workbook/KB.tsv` for SHED returns **0 hits**. The fleet has carried one survey house on this series for 5.5 months while a larger Federal Reserve sample sat unread.

| Measure (BNPL users, past 12 months) | LendingTree (current band source) | Fed SHED 2025 |
|---|---|---|
| Paid late | **47%** (2026), 41% (2025), 34% (2024) | **26%**, "essentially unchanged from the prior year" |
| Trend | +6pp/yr, rising | flat |
| Sample | opt-in online, n=2,060 | probability-based panel, n≈13,000 |
| Fielded | 2026-03-17 to 03-23 | October 2025 |
| Band reading (>25 Y / >35 O / >45 R) | 🔴 RED | 🟡 YELLOW (just over) |

Source: federalreserve.gov, SHED 2025 Credit chapter, Table 41 (read 2026-10-28 via the HTML chapter, not the PDF).

**The windows overlap but are not co-vintaged** (SHED Oct-24 to Oct-25; LendingTree Mar-25 to Mar-26). That can't explain a 21pp level gap. It might explain part of the trend gap, if lateness accelerated in late 2025 to early 2026. The definitions are close but the question wording was not compared.

## 2. What survives on either basis

The SHED income gradient for paid late: **<$25K 40% · $25–50K 33% · $50–100K 25% · $100K+ 11%**. "Only way I could afford it" is the main reason for 40% at <$25K vs 15% at $100K+. About 1 in 5 users paid for groceries or food delivery with BNPL. **This supports the K-shape disaggregation.** It is a cross-section, not a trend, and can't stand in for the rising-series claim.

## 3. Why it matters now

- **STATUS row 25** carries 🔴 on the LendingTree basis alone. Any reader of that row gets a basis-dependent colour with no basis label. `[[finding_distance_to_a_threshold_is_a_claim_about_its_basis]]`
- **`handoff_RED/COUNTER_LOG.md` ~L285** names "the LendingTree late-rate series (34→41→47%) keeps climbing" as a change-my-mind condition. On the larger sample the series is not climbing. CARL stages to RED; PHAN does not.
- **No OPEN CRL row** grades on this series (checked `thesis/PREDICTIONS.tsv`), so nothing is mis-graded today.

## 4. Smaller items

- **LendingTree page re-dated 2026-10-14** (tracker fielded Oct 2–9/26, n=2,000): **90% of users who asked for a late-fee waiver got it waived or reduced.** The 47% headline is unchanged (March fielding). A late payment doesn't necessarily cost the borrower anything.
- **Confirmed dates:** **Coastal Financial (CCB) Q3-26 2026-10-29 before open, call 8:00 ET.** That's the open DISTRESS row; your docket row 10/30 WQ-228 covers it. No Q3 8-K on EDGAR as of 22:15 ET 10/28. **Affirm FQ1-27 2026-11-05 after close** (guide revenue $1.19–1.22B, GMV $13.7–14.0B). **Klarna Q3-26 2026-11-17 before open.** Your docket's 11/12 gate row is inside the window; the Klarna leg lands 5 days later.
- **Nulls** (secondary search, corroborating this afternoon's hygiene pass): no 1033 NPRM published; no NYDFS final BNPL rule; no new state-AG EWA action after CO 8/27; no consumer-fintech failure found for Sep–Oct.

## 5. Asks

1. Basis ruling for STATUS row 25: (a) keep LendingTree and add a basis label plus the SHED counter-reading, (b) switch to SHED (annual, May), or (c) carry both. PHAN recommends **(c)**, with the band colour stated per house.
2. Stage the SHED trend reading to RED against the COUNTER_LOG condition.
3. Optional KB rows for SHED 2025 BNPL (late 26% flat; income gradient).
