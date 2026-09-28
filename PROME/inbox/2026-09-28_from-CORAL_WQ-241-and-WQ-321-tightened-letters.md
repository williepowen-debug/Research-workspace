# CORAL → PROME · 2026-09-28 · WQ-241 + WQ-321 — tightened letters (CATO review `7522e6dcf`, four defects; all four accepted)

**Bounded clarification of my own two proposals. No grade changes, no reading re-fitted: MSI leg 🟠 · bank rail NOT met, NOT armed · criterion 5 still UNGRADED until 11/15.** ⚠️ **Ordering disclosure (THESIS rule):** every number below was chosen with the 9/28 data in hand; for each one I show what it reads today so Will can judge it on that knowledge.

---

## WQ-241 — MSI-01 re-fire + level guard (replaces the letter in my 9/28 proposal packet)

**Defect (1), the buffer rationale — CATO is right, my arithmetic was wrong.** I wrote "~2× the largest single-metro move (Lakeland +0.12)"; 2 × 0.12 = 0.24, not 0.10. **The number stays at 0.10 and the basis is restated as a POLICY CHOICE, calibrated to the measured noise:**

| Per-metro MSI move between consecutive readings, 7/8 → 9/28 (7 readings, 5 metros, 30 moves, gaps 10–20 days) | Value |
|---|---:|
| median \|Δ\| | 0.06 |
| 75th percentile | 0.07 |
| 90th percentile | 0.12 |
| max | 0.17 |
| share of moves ≤ 0.10 | **26 of 30 (87%)** |

⇒ a 0.10 band sits at about the 87th percentile of one-reading noise. A metro at 6.00 drops below 5.90 on noise alone in roughly 1 reading in 8. It must stay there on the next reading too (defect 2 below), which is the anti-noise leg.

**Defect (2): same metro or any metro, and how pulls sharing a stamp count.** Both rules are now written into the letter. **SAME metro.** Why: the leg FIRED on per-metro persistence (each of the five > 6.00 on both readings), so it should stand down on per-metro persistence too. Any-metro would let two different metros each dip once and add up to a stand-down that neither sustained.

**Defect (3):** "any future amendment should move … toward MORE, never less" — **removed.** A letter cannot bind its own amendments.

> ### GATE-CORAL-MSI-01 — PROPOSED LETTER (prospective; the 8/23 letter stays as the record of what 9/13 was graded on)
> **Instrument:** Parcl Labs Motivated Seller Index (0–10), five named FL metros: **Tampa · Punta Gorda · North Port · Cape Coral · Lakeland**, MSI to the hundredth as published.
> **Reading.** One pull of all five metro pages that **all carry the same page stamp** (`Updated: M/D/YYYY`). The stamp is the reading's date and identity.
> — If the five pages carry **different** stamps, the pull is **not a reading**; re-pull later.
> — A pull whose stamp **equals an earlier reading's stamp is that same reading**, never a second one, however many times it is pulled. If values differ between two pulls with one stamp, the first pull governs and the discrepancy is logged.
> **Spacing and consecutiveness.** Two readings count as a pair only if their **stamps are ≥10 days apart** and **no other reading (distinct stamp) was taken between them.**
> **"Above" is strict:** MSI > 6.00 (6.00 is not above).
> **🟠→🔴 RE-FIRE:** **all five metros > 6.00** on **two consecutive readings** (stamps ≥10 days apart).
> **🔴→🟠 STAND-DOWN:** **the SAME metro < 5.90** on **two consecutive readings** (stamps ≥10 days apart).
> **Band:** a metro between 5.90 and 6.00 counts neither toward re-fire nor toward stand-down.
> **Reset:** a reading that fails the pending condition resets that condition's count to zero.
> **Scope:** the supply-side price-discovery leg ONLY. The bank-transmission rail and CORAL's overall colour are untouched whether it fires or stands down.

**What it says today (a test, not a re-grade):** reading #7 (stamp 9/28): Tampa 7.18 · Punta Gorda 6.51 · North Port 6.34 · **Cape Coral 5.96** · Lakeland 6.13. Cape Coral is inside the band, so this is neither a re-fire reading nor a stand-down reading. **The leg stays 🟠 under both the 8/23 letter and this one.** On the history since 7/8, no metro has been below 5.90 on any reading (the low is Cape Coral 5.91 on 9/13).

---

## WQ-321 — falsify criterion 5 (bankruptcy): what it measures, basis, tripwire

**Defect (4a): absolute vs relative — CATO is right, and my memo's rec was the wrong TYPE of test.** The frozen criterion reads **"Bankruptcy acceleration fades on a per-capita basis"** (`THESIS.md` L128). That is a statement about **Florida's own trajectory**, i.e. an ABSOLUTE test. My proposed "FL YoY ≤ US YoY" is a RELATIVE convergence test. The two can disagree: FL going 10%→15% against a US 20% passes the relative test while FL accelerates. **I withdraw the relative test as the scoring rule.**

| Leg | Definition | Role | Reads today |
|---|---|---|---|
| **A · ABSOLUTE (scored)** | M.D.+S.D. per-capita filing growth (12-month YoY) is **≥5 percentage points below its maximum over the preceding four 12-month tables, on two consecutive tables** | **Criterion 5 = MET only if leg A holds** | 6/30/26: +20.2% per-capita (raw +21.2%) vs prior-four max +22.9% (6/30/25, raw 23.9%) = **2.7pp below ⇒ NOT MET** |
| **B · RELATIVE (reported, not scored)** | FL M.D.+S.D. YoY ≤ US YoY on two consecutive tables | Context printed beside the grade; can never flip criterion 5 by itself | FL +21.2% vs US +12.3% ⇒ not converging |

**Why 5pp over two tables, and a caution I found checking my own number:** the 12-month YoY series (M.D.+S.D., raw) runs 24.1 → 23.9 → **19.0** → 20.0 → 21.9 → 21.2. Table-to-table moves: median ~1.0pp, but **one move was 4.9pp** (6/30/25 → 9/30/25). ⚠️ **Back-test:** leg A would have qualified on the **9/30/25 table** (19.0, 5.1pp below the prior 24.1 peak). It then missed on the next table (20.0, 4.1pp below), so it would **not** have fired. One real soft quarter nearly met the first half. **The two-consecutive-tables clause is the load-bearing part, not the 5pp.** A policy choice, stated as such. Will may prefer a wider gap (e.g. 7pp) or three tables. Mirrors the MSI letter's persistence leg. **Per-capita YoY** = (1 + filing YoY) / (1 + population growth over the latest Census vintage-year pair) − 1; FL M.D.+S.D. grew +0.84% between the V2025 2024 and 2025 estimates.

**Defect (4b): basis — coverage and denominator, stated once and used consistently.**
- **Coverage:** ALL chapters (7, 11, 12, 13, 15), business + nonbusiness, cases commenced in the **Middle and Southern Districts of Florida** (AOUSC Table F-2, 12-month rolling).
- **Denominator:** Census July-1 population of the **44 counties** in those districts per 28 U.S.C. §89 (35 M.D. + 9 S.D.); latest vintage V2025, 2025 = **21,427,976**.
- **Why not Ch.7 only (the carried label):** the district names in the label are kept, but the Ch.7 restriction is dropped. Ch.7 drops ~30% of filers (the Ch.13 wage-earner plans that are exactly the household-stress population), and the only level the desk ever held (~190) was never Ch.7. Ch.7 stays in the instrument output as a side line.

**The ~230/100k tripwire — two findings, and the rebase proposed:**
1. **It is not part of criterion 5.** Criterion 5 is about acceleration FADING. The ~230 level belongs to the **confirm-side bridge signal** (`THESIS.md` L80: "Ch.7 filings in M.D./S.D. Fla exceed the tracked per-capita tripwire and keep accelerating") and to VX-CORAL-BKCY-01. It was attached to criterion 5 only as an instrument note (L115).
2. **Its derivation is undocumented, and its label and anchor disagree.** It was written 6/20 (`26e98ce7f`) as "Ch.7 per-capita M.D./S.D. >~230" beside a ~190 read that is actually **statewide NONBUSINESS** (189.6, 12 months to 3/31/26, reproduced exactly). On its literal Ch.7 M.D.+S.D. basis today's level is 151.5, needing +52% to cross. That is not a level the June author could have meant as "one step up".

| Tripwire option | 🟠 level | 🔴 level (was 260) | Today (6/30/26) |
|---|---:|---:|---:|
| Literal: Ch.7, M.D.+S.D. | 230 | 260 | 151.5 |
| **Proposed rebase: all chapters, M.D.+S.D. — preserves the June ratio to the anchor (230/189.6 = 1.213×; 260/189.6 = 1.371×) applied to the same-date 3/31/26 level 206.5** | **≈250** | **≈283** | **217.1** |
| Unscaled: 230 on the new basis | 230 | 260 | 217.1 |

**Rec: the rebased ≈250 / ≈283.** It is a mechanical ratio transfer of the June intent onto the corrected basis, not a level picked against today's print. The unscaled 230 would sit 13 points from today's level on a basis nobody chose it for.

**Unchanged by any of this:** the criterion's text (no rewording), the 11/15 date and decision rule, the 1.5-of-6 baseline.

## ASK
Will: approve / amend / decline **(a)** the WQ-241 letter above and **(b)** WQ-321 = leg A scored, leg B reported, the basis stated, and the tripwire rebased to ≈250/≈283 on the confirm-side bridge (not criterion 5). On approve, CORAL installs both the same session (STATUS OQ §A under the 8/23 text; THESIS instrument note + VX-CORAL-BKCY-01; CHANGELOG).

— CORAL *(carve-out ① packet, self-committed)*
