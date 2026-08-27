# MATRIX_V2 §1/§3c ADOPTED — and the 8/25–27 cluster graded

**Date:** 2026-08-27 (Thu), written ~09:4x–10:xx ET — **BEFORE the 1PM 7Y print.** That timing is the whole point: the adoption is registered against an auction that has not happened yet.
**Author:** BOND. **Ruling being executed:** Will, 2026-08-20, verbatim *"Approved on both - implement per your rec"* (DAEDALUS MATRIX_V2 structure review).

---

## 0. THE OWED ACTION, AND THE HALF OF IT THAT WAS MISSED

The ruling carried **two dated items, neither gating the other**: **adopt §1/§3c at the 8/25–27 pre-registrations**, and **deliver the base-rating by 9/4**.

🔴 **State it plainly: the adoption was owed at *the pre-registrations*, plural, and TWO of the four auctions in the cluster have already printed un-adopted** (8/25 2Y, 8/26 2Y-reopening, 8/26 5Y). The desk was dark 8/24–8/26. **This document adopts the legs for the 7Y only — the last leg of the cluster and the last one where a pre-registration is still possible.**

⚠️ **Do not let "adopted at the cluster" read as "adopted across the cluster."** The three printed auctions are graded below under the **OLD** rule, because that is the rule that was in force when they printed, and the new percentile threshold is **forward-only by its own §3d audit rule** (*"the live percentile threshold is forward-only — it governs new auctions from the snapshot date forward, never retroactively"*). Back-applying it would be picking a threshold after seeing the prints.

**Cost of the miss, MEASURED — the counterfactual was computed, not asserted.** Applying the adopted `I'` bar to each of the three (each against its own trailing-12 strictly-prior window, % of competitive accepted):

| Print | `I'` bar (15th pctile) | indirect | Would `I'` have fired? |
|---|---:|---:|---|
| 8/25 2Y | 55.75 | 66.01 | **NO** (+10.26pp clear) |
| 8/26 2Y-R | 56.12 | 66.56 | **NO** (+10.44pp clear) |
| 8/26 5Y | 59.48 | 61.51 | **NO** (+2.03pp clear) |

**⇒ The two-day slip changed NO verdict.** That is luck, not vindication, and it does not make the slip free: a pre-registration's only value is that it precedes the print, and for two of these it now cannot.

⚠️ **AND THE COUNTERFACTUAL SURFACED SOMETHING THE ADOPTION ITSELF DID NOT PREDICT — the new rule's bite is wildly uneven across tenors.** The `I'` bar sits above the trailing-12 MIN by **+4.84pp at the 2Y** (55.75 vs 50.91), **+0.82pp at the 7Y** (57.24 vs 56.42) and **just +0.24pp at the 5Y** (59.48 vs 59.24). ⇒ **At the 5Y the adopted rule is barely looser than the old min-based bar it was meant to replace**, because that tenor's trailing-12 indirect distribution is bunched hard at its bottom. **"Indirect at the 15th percentile" is one rule with three very different effective strictnesses.** Not a reason to decline the ruling — it is Will-approved and adopted — but it is a **first-order input to the 9/4 base-rating**, which must report hit-rate and separation **per tenor**, never pooled. Logged as owed item #7.

---

## 1. WHAT IS ADOPTED (substance, not section numbers)

⚠️ **The ruling's section labels and the draft's own section numbers are CROSSED, so I am adopting by SUBSTANCE and recording the discrepancy rather than silently picking a reading.** `thesis/THESIS.md` and `SCRATCH.md` render the ruling as *"§1 = drop dealer-as-bearish · §3c = indirect sufficient alone at the 15th per-tenor percentile."* In `proposals/MATRIX_V2_DRAFT_prome-spawned.md` the actual numbering is **§3c = dealer-drop** and **§3d = the indirect percentile rule**; §1 is the executive summary that states both. **The SUBSTANCE is unambiguous in every rendering and it is the substance Will approved.** No interpretive latitude is being taken.

| # | Leg | Adopted form | Status |
|---|---|---|---|
| **A** | **Indirect at the per-tenor 15th percentile, SUFFICIENT ALONE** | `I'` fires 🟠 standalone when `indirect%` < the 15th percentile of the **trailing-12 prior same-tenor same-TIPS** prints | ✅ **ADOPTED, effective for the 8/27 7Y forward** |
| **B** | **Drop dealer as a BEARISH criterion** | Dealer take is no longer a leg of any *escalation* trigger on the auction-health vector. Retained as a **contrarian-bullish note above 18%** per §3c, and retained as a **descriptive** field on every grade | ✅ **ADOPTED, same scope** |
| **C** | BTC confirmatory-only | — | ⏸️ **STILL HELD — not ruled.** Unchanged. |

**Effect of (A), stated so it is not oversold:** the composition-failure test is *conjunctive* (indirect below trailing-12 MIN **AND** dealer above MAX) and has a base rate near zero by construction. The adopted `I'` gives the vector **a fireable single-instrument escalation path for the first time** — at a threshold (15th pctile) that sits **above** the min, so it is strictly easier to fire, and with no dealer leg to veto it.

---

## 2. 🔴 THE ONE THING I AM NOT DOING UNILATERALLY, AND WHY

**Adopting (B) — "drop dealer as bearish" — would, read at its widest, also strip the dealer leg out of the THESIS KILL**, which quotes the same composition-failure phrasing (*"indirect below the tenor's OWN trailing-12 MIN **and** dealer above its OWN trailing-12 MAX"*).

⛔ **I am NOT making that change. It is flagged to Will, not executed.** Three grounds, and the first is the one that matters:

1. 🔴 **DIRECTION DISCLOSED: dropping the dealer leg makes the thesis kill EASIER TO FIRE, and the kill firing is the outcome that CONFIRMS this desk's own standing bear thesis.** A ruling on *escalation-matrix scoring* is not a licence to loosen a **kill criterion on a live position** in the direction that flatters the author. This is precisely the shape this desk has documented repeatedly — and the one time to be strictest is when the change runs my way.
2. **Scope.** The ruling was on MATRIX_V2, which is the **escalation matrix**. The thesis kill is a separate Will-facing spec that happens to reuse the phrasing. Shared wording is not shared scope.
3. **No mid-flight edits.** `TRY-FIRE-004` is live. This desk's own principle — the one it applied *against itself* on the T6 fresh-high OR-leg — governs here.

**→ ASK TO WILL (one question, no action pending):** *does the 8/20 MATRIX_V2 ruling extend to the thesis kill's composition-failure test, or is it scoped to the auction-health escalation matrix only?* **Until answered, the thesis kill stands EXACTLY as written, dealer leg included.**

---

## 3. THE CONVENTION QUESTION — REAL IN PRINCIPLE, NON-BINDING IN FACT

MATRIX_V2 §3d specifies the indirect percentile on a **%-of-OFFERING** convention. Every live bar on this desk — and `grade_auction.py`'s enforced method — is **%-of-COMPETITIVE-ACCEPTED**. Two conventions, one threshold: a silent pick would be exactly the *unnamed-instrument-makes-a-threshold-a-family* defect this desk has now shipped twice.

**So I computed both** (7Y, trailing-12 strictly prior to 2026-08-27, window 2025-08-28 → 2026-07-28, n=12, linear-interpolation percentile):

| Convention | 15th pctile | median | min |
|---|---:|---:|---:|
| indirect **% of competitive accepted** | **57.24** | 60.80 | 56.42 |
| indirect **% of offering** | **57.15** | 60.68 | 56.34 |

**⇒ The two conventions differ by 0.09pp.** Competitive-accepted runs **99.75%–99.90%** of offering across all twelve 7Y auctions in the window, so the denominators are near-identical at this tenor and the choice **cannot change a verdict unless a print lands inside a 0.09pp window.**

**RULING: adopt on %-of-COMPETITIVE-ACCEPTED** — it is what every other bar, every frozen prediction and the grading tool already use, so it keeps one denominator across the desk. **Recorded, not buried: the of-offering figure is 57.15, and if a print ever lands in the 57.15–57.24 band the verdict is reported as CONVENTION-DEPENDENT and graded both ways rather than resolved by preference.**

⚠️ **This is a 7Y result, not a general one.** The comp/offering ratio is a per-auction fact; at a tenor or in a period where noncompetitive take is larger the gap widens. **Re-derive per tenor; never reuse this 0.09pp.**

---

## 4. ★ FROZEN PRE-REGISTRATION — 8/27 7Y `91282CRJ2`, $44B, 1PM ET

**Bars frozen from the primary at 09:4x ET, before the print.** Trailing-12 same-tenor same-TIPS, strictly prior, % of competitive accepted, window 2025-08-28 → 2026-07-28, n=12:

| Metric | median | mean | min | max |
|---|---:|---:|---:|---:|
| BTC | 2.49 | 2.48 | 2.40 | 2.52 |
| indirect % | 60.80 | 63.83 | 56.42 | 78.39 |
| dealer % | 11.82 | 11.57 | 9.34 | 13.14 |

**★ ADOPTED-RULE TRIGGER (new, first live application):**
- **`I'` — indirect < 57.24% ⇒ fires 🟠 STANDALONE.** No dealer leg, no BTC leg, no second condition.
- **Composition failure (unchanged, thesis-kill-facing):** indirect < 56.42% **AND** dealer > 13.14%.
- **Cover marker (unchanged):** BTC < 2.40 with composition intact.
- **Dealer:** descriptive only. **>18% would be logged as a contrarian-BULLISH note**, never as escalation.

**Branch set — with the MANDATORY RESIDUAL branch (v1.1.4(d)), because a branch set with a hole is how `BND-13` landed 0.03pp from an ungradeable print:**

| Branch | Condition | Read |
|---|---|---|
| **A** | indirect < 56.42 AND dealer > 13.14 | **COMPOSITION FAILURE** — demand hole; thesis-kill leg 1 met |
| **B** | indirect < 57.24 (and not A) | 🟠 **`I'` FIRES STANDALONE** — the adopted rule's first live fire. Auction health → 3 |
| **C** | BTC < 2.40, composition intact | **COVER MARKER** — escalates the vector, mechanism NOT failed |
| **D** | none of the above | 🟢 **CLEAN** — benign resolution n+1 |
| **RESIDUAL** | any print not covered by A–D, incl. a results feed that publishes partially, a re-auction, or a cancelled/postponed auction | **UNGRADEABLE, recorded with cause.** Does NOT default to either side. |

**Margins will be stated on EVERY leg (v1.1.4(e)), including the legs that clear by a mile.**

⚠️ **`BND-19`'s 7Y leg and `BND-20` are graded on their OWN frozen bars (indirect ≥ 60.80; BTC ∈ [2.40, 2.52]) and are NOT re-keyed to the adopted rule.** They were registered 8/21 under the old spec and a prediction is not re-specified after registration. **The adopted rule governs the VECTOR; the frozen predictions govern themselves.**

---

## 5. THE THREE PRINTS THAT LANDED WHILE THE DESK WAS DARK — GRADED

All three at the TreasuryDirect primary via `monitors/grade_auction.py`, benchmarked per-tenor, % of competitive accepted, **no tail computed** (unscoreable from primaries, retired 2026-07-28).

### 5a. 8/25 · 2Y new issue `91282CRH6` · $69B · 🟢 CLEAN
`BTC 2.60 · indirect 66.01% · direct 23.09% · dealer 10.90% · HY 4.2040` (competitive accepted $68.107B)
Bars (n=12, 2026-02-24 → 2026-07-29): BTC med 2.72 / min 2.44 · ind med 57.65 / min 50.91 · dlr med 25.48 / max 49.09

| Leg | Margin vs median | Failure-bar margin |
|---|---:|---:|
| BTC 2.60 | −0.12 (mean −0.30) | +0.16 above min |
| **indirect 66.01** | **+8.36** | **+15.10pp above the failure bar** |
| dealer 10.90 | −14.59 | −38.20pp below the bar |

**Read: STRONG, not merely clean.** Indirect +8.36pp over median at the front end.

### 5b. 8/26 · 2Y REOPENING `91282CRD5` · $28B · 🟢 CLEAN — with one genuine oddity
`BTC 3.14 · indirect 66.56% · direct 0.36% · dealer 33.08%` (competitive accepted $27.986B)
Bars (n=12, 2026-02-25 → 2026-08-25): ind med 58.57 / min 50.91 · dlr med 25.48 / max 49.09

| Leg | Margin vs median | Failure-bar margin |
|---|---:|---:|
| BTC 3.14 | +0.42 | +0.70 above min |
| **indirect 66.56** | **+7.99** | **+15.65pp above the failure bar** |
| dealer 33.08 | +7.60 | −16.01pp below the bar |

★ **DIRECT TOOK 0.36% — essentially zero.** Direct bidders vanished and dealers absorbed the residual (33.08% vs a 25.48% median). **This is NOT a composition failure and must not be reported as one** — the failure test is indirect-driven and indirect printed +15.65pp clear of its bar; foreign/custodial demand was *strong*. But a near-total absence of direct bidding is a real compositional fact and it is logged rather than smoothed over.
⚠️ **Interpretation withheld deliberately.** This is a **seasoned reopening** (`securityTerm` "1-Year 11-Month") with its own buyer base, `$28B` against the `$69B` new issue, and **no `highYield` published in the feed**. I do not have a base rate for direct-take on 2Y reopenings and **I am not inventing a threshold at n=1.** → **Registered as an open question, not a signal.**

### 5c. 8/26 · 5Y new issue `91282CRK9` · $70B · 🟢 CLEAN — and the softest of the three
`BTC 2.37 · indirect 61.51% · direct 28.44% · dealer 10.05% · HY 4.3930` (competitive accepted $69.798B)
Bars (n=12, 2025-09-24 → 2026-07-27): BTC med 2.34 / mean 2.37 / min 2.28 · ind med 61.75 / min 59.24 · dlr med 12.31 / max 15.61

| Leg | Margin vs median | Failure-bar margin |
|---|---:|---:|
| **BTC 2.37** | **+0.03** (mean **−0.00** ⚠️ median/mean disagree on sign) | +0.09 above min |
| **indirect 61.51** | **−0.24** | +2.27pp above the failure bar |
| dealer 10.05 | −2.27 | −5.57pp below the bar |

**Read: clean, and the 7/27 cover marker did NOT repeat** — BTC 2.37 against the 2.28 that fired it. But this is the **soft one of the three**: indirect a quarter-point below its own median, and a BTC sitting *exactly on its trailing-12 mean* (−0.00). **Reported as knife-edge, not as strength.**

**⇒ THREE MORE BENIGN RESOLUTIONS. No cover marker, no composition failure at any tenor.** Streak arithmetic, shown so it is auditable: **14 as recorded 8/21, +3 = 17** consecutive benign coupon resolutions since 7/9.

---

## 6. PREDICTION RESOLUTIONS

### ✅ `BND-18` (55%) — **RESOLVED TRUE, margin +0.03**
*5Y on 8/26 prints BTC ≥ 2.34 (its own trailing-12 median).* **Printed 2.37.**

⚠️ **A hit, and an honest one, but state the margin: +0.03 on a metric whose trailing-12 range is 2.28–2.75.** The same print is **−0.00 against the trailing-12 MEAN**, i.e. the tool itself flagged *median/mean disagree on sign*. **Had the bar been the mean instead of the median, this resolves FALSE.** The bar was frozen at the median on 8/21, before the print, and it stands — but a 55% call landing +0.03 inside its bar is **not** evidence the pricing was good.
✅ **Substance that does survive: the 7/27 cover marker was a one-off, which is what the row was built to test.**
★ **Calibration note — this was the first row priced under the 8/21 bucketed finding** (11 mid-band calls → 3 hits ⇒ price mid-band calls *below* instinct). It was marked ~15pp under instinct and it hit. **n=1 proves nothing; recorded so the next mid-band call can be scored against the same discipline.**

### 🔴 `BND-19` (35%) — **RESOLVED FALSE on leg 2**, 7Y leg still recorded per the registration
*Indirect ≥ own trailing-12 median at ALL THREE new-issue nominal tenors.*

| Leg | Bar | Print | Margin | Verdict |
|---|---:|---:|---:|---|
| 2Y `91282CRH6` (8/25) | ≥ 57.65 | **66.01** | **+8.36** | ✅ PASS |
| 5Y `91282CRK9` (8/26) | ≥ 61.75 | **61.51** | **−0.24** | 🔴 **FAIL** |
| 7Y `91282CRJ2` (8/27) | ≥ 60.80 | *1PM today* | — | **RECORDED REGARDLESS** |

**FALSE — the conjunction is already broken.** ⚠️ **The registration explicitly requires all three legs recorded even after the first fails, so the 7Y leg is graded and logged this session and does not become "moot."** The 2Y-reopening was **excluded at registration** so the scope could not drift into a family; that exclusion is honoured — its +7.99pp does **not** count toward this row.

★ **THE FINDING IS THE MARGIN, AND IT RUNS AGAINST MY OWN THESIS.** This was the deliberately hard row — the thesis's *stronger* form — priced 35%, and **it failed by 0.24pp on one leg of three.** Miss it by 0.24pp and the honest report is *"demand was normal-or-better at two of three tenors and a quarter-point short at the third,"* **not** *"the stronger form of the thesis failed."* **A conjunctive test that fails by a rounding-scale margin is evidence the conjunction is too brittle, not evidence the demand story turned.** Logged as a spec observation for the 9/4 base-rating, **not** acted on: the row is FALSE as written and is scored FALSE.

### ⏳ `BND-20` (85%) — 7Y BTC ∈ [2.40, 2.52] — **resolves ~1PM today.** Bars re-verified above; the band is exactly the trailing-12 min/max, which is the fitted-band caveat logged openly at registration.
### ⏳ `BND-15` (70%) — DFII10 no close ≥2.50 through 8/29. **Live 2.32 [8/25] = 18bp away and STILL WIDENING.** Gate path 6 → 9 → 15 → **18bp**. Three gradeable sessions left (8/26, 8/27, 8/28; 8/29 is a Saturday). ⚠️ **Confidence stays FROZEN at 70%** — it was frozen there when it looked like a likely miss, and the rule has to bind now that it looks like a likely hit or it was never a rule.

---

## 7. WHAT THIS SESSION DOES **NOT** CLAIM

- **The adopted rule has not fired anything.** It is registered pre-print and its first live test is at 1PM.
- **No composite move.** Nothing crossed a pre-registered line; three clean prints are the *absence* of a trigger, not a downgrade condition. The registered auction-health downgrade needs **three consecutive** coupon auctions with indirect ≥ median AND dealer ≤ median — the 5Y's **−0.24pp indirect breaks it**, so the counter is **1** (2Y ✅ → 2Y-R excluded-as-reopening? see below → 5Y ✗ resets). **⚠️ SPEC GAP FOUND: the counter's ruling settled whether TIPS count and never settled whether REOPENINGS count.** Same class as the TIPS ambiguity, unsettled for the same reason — nobody asked. **Settled now, while non-binding: reopenings DO count** (they are nominal coupon auctions against nominal per-tenor bars, unlike TIPS which have their own buyer base and window). ⇒ **2Y ✅ → 2Y-R ✅ → 5Y ✗ RESETS ⇒ counter = 0.** 🔴 **Direction disclosed: counting reopenings ADVANCES a downgrade that weakens my own bear thesis, and the 5Y reset it to zero anyway — so the ruling is made in the direction against me and costs nothing today, which is the only honest time to make one.**
- **No thesis-kill change.** See §2. Flagged to Will, not executed.
- **No claim the two-day slip was harmless.** It changed no verdict (§0) and that is luck.

---

## 8. OWED OUT OF THIS DOCUMENT

| # | Item | Date |
|---|---|---|
| 1 | **Will: does the ruling extend to the thesis kill's dealer leg?** (§2) | ASK — no action pending |
| 2 | Grade the 1PM 7Y against the frozen branch set; resolve `BND-20`; record `BND-19` leg 3 | **8/27, today** |
| 3 | MATRIX_V2 **base-rating** — hit-rate + separation for `I'` at the 15th pctile | **by 9/4** (Will-ruled) |
| 4 | Quarterly percentile-snapshot table in `monitors/AUCTION_HEALTH.md` (§3d audit rail) — **due 10/1**, seeded today for the 7Y | 10/01 |
| 5 | Direct-take base rate for 2Y reopenings (§5b) — **no threshold until it exists** | with #3 |
| 6 | Conjunction brittleness (§6, `BND-19` failing by 0.24pp) — spec observation for the base-rating | with #3 |
| 7 | **Base-rating MUST be reported PER TENOR, not pooled** (§0) — the `I'` bar sits +4.84pp / +0.82pp / +0.24pp above the min at 2Y / 7Y / 5Y, so one pooled hit-rate would average three different rules | with #3 |
