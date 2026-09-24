# WAL Q3 2026 PRINT — Pre-Registered Grading Frame

**Pre-registered:** **Thu 2026-09-24** (WAL session #7, on PROME's L170 dispatch). **Earliest plausible print date: Tue 2026-10-13** (`PROME/DOCKET.tsv` L170). This frame is written **19 days before it**, so it is not VOID under the frame-before-filing principle.
**Print date: NOT ANNOUNCED** as of 2026-09-24 04:10 UTC (WAL IR press and event feeds, primary; `KB-WAL-197`). The prior pattern (Q3-25 announced 2025-10-02 with the call on Wed 2025-10-22; Q1-26 call Wed 2026-04-22; Q2-26 print Tue 2026-07-21 with the call Wed 2026-07-22) is **inference only**. ⛔ **Pin the actual date from the WAL IR release or the EDGAR 8-K when it is announced, never from this paragraph**, and record it in §9 as a dated pre-print annotation.
**Owner:** WAL (grades it). **Governs:** `WAL-01` (25%) and `WAL-02` (50%) in `workbook/PREDICTIONS.tsv`. It also governs the migration N=2 test (`KB-WAL-111`), the "charge-offs have peaked" guide test (`KB-WAL-118`), the $99M disposition, and the grade of management's 9/16 guidance (`KB-WAL-194`).
**Scope:** the **PRINT** only, meaning the earnings release (8-K EX-99.1), the deck (EX-99.2) and the call. The Q3 **10-Q** is a separate frame (L171, earliest plausible 10/24). Every leg below names the instrument that carries its datum, and says what the 10-Q may later add.
**Discipline:** grade verbatim against this file. **Pre-print annotations are permitted in §9, dated. Post-print edits are forbidden: this file is the honesty record.** Rules W1–W13 of `Q2_GRADING_FRAME_2026-07-21.md` Addendum A carry over wherever this file doesn't override them. W2 (ex-fraud fallback), W7 (half-open bands, printed precision) and W9 (explicit-only migration counting) are restated where they bind.

---

## 0. The bet, and what the print can and cannot resolve

Spot **$75.60 [Wed 2026-09-23 close]** sits **0.47% below** the v2.4 EV of $75.96. The bear case is priced, and what's left is a **resolution trade**. The print is the first instrument that can carry any of these:

| Test | Carrying instrument | Resolves at the print? |
|---|---|---|
| WAL-02 ex-fraud NCO >40bps | EX-99.1 NCO line | **YES, final** (Q3 is the row's only window) |
| WAL-01 Office classified >$500M | EX-99.2 "Classified Assets Mix" slide (slide 12 in the Q1 and Q2 decks), **A2-visual** | **YES, provisional.** The row's own cross-check against total classified comes from the 10-Q |
| Migration N=2 | Deck + call, explicit naming only (W9) | YES, or NOT-DISCLOSED |
| "Charge-offs have peaked" guide | EX-99.1 NCO $ and rate vs Q2 | YES |
| $99M disposition | Call (MODAL) · deck · 8-K if one lands first · **10-Q backstop** | Maybe. Absence means PENDING-10-Q, never benign |
| Mgmt 9/16 benchmark (NPL ~$500M, coverage >100%) | EX-99.1 asset-quality table | YES |

---

## 1. WAL-02 — ex-fraud NCO (the ledger grade; the letter governs verbatim)

**The letter (re-spec 2026-08-20, P3, Will-ruled 8/12 row 32b):** *Q3 ex-fraud NCO > 40bps = CONFIRMED; ≤ 40bps = INVALIDATED.* No undefined band remains. Q2 is spent at 37bps (`KB-WAL-158`).

- **Cell:** the company-reported **annualized net charge-offs / average loans** for Q3, at printed precision (W7). If it isn't published, compute quarterly NCO$ × 4 ÷ reported average HFI loans, to 1 decimal place.
- **Ex-fraud (W2):** subtract only charge-offs **explicitly attributed** to LAM, Cantor, or a newly designated fraud item. If nothing is attributed, total NCO **is** the ex-fraud figure. No inferred adjustments.
- **Threshold:** **40.0bps = INVALIDATED** (≤40). 40.1bps and above = CONFIRMED.
- **Missing disclosure:** if the release carries no NCO ratio and no average-loan base, the grade is **PENDING-10-Q** (the 10-Q carries both). This is never an invalidation.
- **Priced-vs-surprise split (carried from Q2 §1/§7, a THESIS read and not a ledger read):** a 40–55bps print driven by a $99M charge-down is **CONFIRMED for the ledger but priced for the thesis**. Only >55bps with the $99M **majority** charged off (>$49.5M cumulative, W6), or >55bps from **new** credits, is a bear surprise.

## 2. WAL-01 — Office classified $ (deck slide; A2-visual)

**The letter (re-spec 2026-08-20, P2):** *Q3-2026 Office classified ≤ $500M on the Q3 deck's "Classified Assets Mix" Office dollar value = INVALIDATED; > $500M = CONFIRMED. CROSS-CHECK: Office $ ≤ the Q3 10-Q total classified balance. NO-VERDICT / INSTRUMENT-ABSENT if the deck omits the property-type breakout or gives percentages with no total that allows a dollar figure.*

- **Cell:** a printed Office $ governs if one is printed. Otherwise **Office % × total classified $** as printed on the same slide or in EX-99.1 (the Q2 derivation: 28% × $1,128M ≈ $316M, `KB-WAL-108`). Record both inputs.
- **Rounding band:** a whole-% share on ~$1.1B carries ±~$5.6M. **The derived midpoint (printed % × printed total) governs, with no rounding in either direction.** If $500M falls inside midpoint ± (0.5 percentage point × total), the grade carries an **AMBIGUOUS-ROUNDING** tag beside it. The tag is disclosed and doesn't change the grade (the 10-Q has no Office line to settle it).
- **Stage-1 ledger grade:** **> $500M = CONFIRMED (provisional)** · **≤ $500M = INVALIDATED (provisional)**. It becomes final when the 10-Q cross-check passes. The cross-check fails only if Office $ > 10-Q total classified, which would VOID the deck read.
- **Label check first (Q2 lesson, KB-108):** confirm the segment is **Office**, not C&I or "Other CRE" (Q2's 38% slice was C&I). A mislabelled slice is NO-VERDICT, not a grade.
- **Thesis read (separate from the ledger):** direction vs Q2's **$316M**, graded on a **plus-realized basis (W4)**: add in-quarter Office/CRE-NOO gross charge-offs back before reading direction. A decline caused by charge-offs is **never** disconfirming. Rising classified in a shrinking Office book points bear. Both falling points bull.
- ⚠️ **The $99M's bucket is unresolved** (three candidate buckets, `KB-WAL-150/151`). A movement of the $99M between slices is **not** a new migration and must not be double-counted in §3.

## 3. Migration N=2 test (`KB-WAL-111`: Q2 = 0 new, pattern stays N=1)

- **Cell:** the count of **NEW** Office/CRE-NOO credits that migrated pass → classified or nonaccrual **in Q3**, **explicitly identified** in the release, deck or call (W9: **delta inference never increments the count**). The **$99M is excluded**, since it's the N=1 instance. Resolutions of management's "six credits" are **exits**, not migrations.

| Count | Grade | Consequence |
|---|---|---|
| **0**, and the topic was **addressed** (deck migration or classified commentary, or an explicit call answer) | **DISCONFIRM, DP2 of 3** | Broadening disconfirmed a second time. The Thesis-RETIRE broadening counter goes 1→2 of 3 |
| **1** | **N=2: THE PATTERN REPLICATES** | V1b-broadening re-score candidate 2/5 → 3/5 (a separate dated edit, never inside the grade) |
| **≥2** | **ESCALATION** (Q2 frame §3 carried) | v2.5 review triggered |
| **Topic not addressed** (no commentary, no Q&A) | **NOT-DISCLOSED, which is NOT 0** | The RETIRE counter does **not** advance. The 10-Q can't name migrations (segment-level nonaccrual only), so the test stays NO-VERDICT for Q3 |

## 4. The "charge-offs have peaked" guide (`KB-WAL-118`, re-affirmed 9/16 in `KB-WAL-194`)

Guide (7/22): charge-off **dollars and rate** "have peaked… gently sloping down Q3/Q4". 9/16: rate **and** dollars "under that of Q2". **Q2 base: $55.0M · 0.37%** (`KB-WAL-157/158`). Graded on **total** NCO (the guide's own basis).

| Q3 total NCO | Grade |
|---|---|
| $ **< $55.0M** AND rate **< 0.37%** | **GUIDE HELD**: disconfirm-lean for V1b-magnitude |
| Neither above Q2, but either **equal at printed precision** | **FLAT**, neither held nor broken |
| $ **> $55.0M** OR rate **> 0.37%** | **GUIDE BROKEN**: confirm-lean for V1b-magnitude. This is a surprise *against management's own dated guidance* |

## 5. The $99M life-science credit (the conviction-governing discriminator)

State at 6/30: nonaccrual, **$0 charged off**, borrower current end-June, appraisal pending (`KB-WAL-112`). ⚠️ **Per Herndon (Q2 call) it is NOT one of the "six credits"**, so management's six-credit NPL path to ~$500M **does not include it**. Management did not mention it on 9/16.

| Q3 disposition | Letter | Read |
|---|---|---|
| Majority charged off (**> $49.5M cumulative**, W6) or sold at a loss of that size | **A** | BEAR: realization. Feeds the §1 >55bps row |
| Partial charge-off or write-down (**$0 < loss ≤ $49.5M**), or an appraisal **disclosed below carrying value** with a specific reserve | **A′** | Bear-lean: the appraisal cut through, magnitude contained |
| Still nonaccrual, no charge-off, no appraisal outcome disclosed | **B** | Status quo. Deferral, not cure. Bear-medium KILL leg (b) stays open |
| Returned to accrual, paid off or refinanced out, sold at or above carrying, or upgraded, **or appraisal disclosed at or above carrying** | **C** | ★ BULL: bear-medium KILL leg (b) satisfied |
| **Not mentioned** in release, deck or call | **PENDING-10-Q** | ⛔ Never graded benign. Silence is the 0-for-1 base rate |

**W5 carried: on a conflict between the letter and a §1 band, the letter governs the thesis grade and the band governs the ledger.**

## 6. Management's 9/16 benchmark (`KB-WAL-194`, B2; graded against their own basis)

| Guided (9/16) | Q3 cell (EX-99.1) | MET if | MISSED if |
|---|---|---|---|
| NPLs "$567M → about $500M" | mgmt's NPL figure on the same basis as their $567M | **≤ $525M** | > $525M |
| ACL "well over 100%" of NPLs (vs 95%) | mgmt's stated coverage | **> 100%** | ≤ 100% |
| "Four down, two to go" | resolved count of the six | **≥ 4 cumulative** | < 4 |

- **Also record, non-gating:** this desk's full-NPL basis (nonaccrual + 90+ accruing + accruing restructured; Q2 $781M, coverage 69.1%, `KB-WAL-156/157`). The 10-Q (L171) carries the restructured line.
- ⚠️ **Basis caveat:** $567M ≠ this desk's Q2 nonaccrual of $562M. The $5M gap is unexplained. Grade on management's number and record the gap; don't reconcile by inference.

## 7. ⚖️ Measurement pin: the Thesis-RETIRE coverage leg (self-ruled here; PROME may escalate)

The RETIRE rule (`STATUS.md` §EXIT RULES, written 2026-07-25) requires "ACL/NPL coverage rebuilt >100%" and names **no denominator**. **Pinned: (funded + unfunded ACL) ÷ total nonaccrual loans**, the basis of the **96%** that THESIS v2.3 quoted as "ACL/NPL coverage 96%" **on the day the rule was written** (`KB-WAL-157`: (487.4 + 52.0) / 562 = 96.0%). That is the letter's own contemporaneous meaning. The **full-NPL figure is reported alongside and does not gate**. Choosing the stricter basis now would move the goalposts in the bear's favour after management guided toward the easier one. ⛔ **This is a measurement pin: zero weights, probabilities or confidences move (rider R3).**

## 8. Non-credit falsifier, read order, guardrails

- **Non-credit falsifier:** if WAL sells off on the print and NIM, deposit cost, AOCI or guidance explains it better than credit, then "credit-only sufficiency" fails. Watch headline NIM (management guided ~−1bp), the ECR deposit remix, and **the AOCI mark: 10Y 5.11% [9/23, ^TNX indicative], highest since 2007**.
- **Read order (Stage 1, release night):** EX-99.1 NCO line and ratio (§1, §4) → asset-quality table: nonaccrual/NPL, ACL, coverage (§6) → EX-99.2 classified-mix slide (§2) → any $99M or office commentary (§5). **Stage 2 (call):** $99M letter (§5) → migration count (§3) → six-credit count (§6) → attribution (§8). **Nothing thesis-level is final between the stages. Unresolved items log PENDING-CALL.**
- **Guardrails:** keep the ledger and the thesis separate, always. A reserve build (B/A′) is not a realized loss (A). **Positions are TERRY/Will's call.** The Dec-18 $70P contains this print, and its guard (`GATE-TERRY-ROLL70-EXIT`) is REGINALD's to grade, not this frame's. OZK's IQHQ outcome (OZK Q3 call) is a **co-timed** sponsor-behaviour read-across only, with severity **not transferable**.
- **Pre-print probabilities (ledger values, NOT re-graded here):** WAL-01 **25%**, WAL-02 **50%**. ⚠️ *Noted, not acted on:* management's dated guidance ("under Q2" = under 37bps) is in tension with a 50% chance of >40bps. Any pre-print re-grade is a **separate dated edit** (R3), recorded in §9 before the print or not at all.

---

## 9. Pre-print annotations (dated; permitted until the print lands)

- *2026-09-24: frame registered. Print date not announced. Re-check the WAL IR feed from ~10/2 and pin the date here.*
