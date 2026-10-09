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
- *2026-09-24 ~00:5x ET (PROME round-2 add-on, capped at ONE pull): tried to re-verify the §6 Barclays quotes at a primary. The WAL IR events page (`investors.westernalliancebancorporation.com/News-and-Presentations/events/default.aspx`) returned **HTTP 404**. No IR-posted transcript was reached, and the webcast replay is audio. ⇒ **All four §6 quotes (NPL $567M → ~$500M; charge-offs under Q2; ACL well over 100% vs 95%; "four down, two to go") REMAIN B2, NOT VERIFIED.** Reason: primary unreachable on the single allowed pull. The requirement to verify before grading still stands and falls to the print session. The Q3 release's own numbers grade §6 regardless; the quotes only set the benchmark.*
- *2026-09-24 08:49 ET (Will-directed re-check): **still NOT ANNOUNCED.** WAL IR press feed (`/feed/PressRelease.svc`, primary): latest item is the 9/14 Barclays notice (the Q2 date notice ran 7/7 for a 7/21 print, 14 days ahead). EDGAR submissions JSON: latest filings are the 9/17 Form 4s. ⇒ Nothing to pin; WAL-01/02 `Resolve_By` 11/15 stays. **Next check: ~Fri 10/2 (last year's announcement date), then every business day until it lands.** When it does, the earliest print date by the 14-day pattern is 14 days after the notice.*
- *2026-09-28 ~15:4x ET (WAL session #10, Will-directed audit repair, `research/AUDIT_2026-09-28.md`; **no grading cell changed**):*
  - ***Date re-check:** still NOT ANNOUNCED (EDGAR submissions: latest filings are the 9/17 Form 4s; IR/web search 9/28). Pattern inference: print ~Tue 10/20 or 10/27, call Wed 10/21 or 10/28. Daily check from Fri 10/2 stands.*
  - ***Delivery contract: the PREDICTIONS.tsv leg (PAT-053).** On release night: **WAL-02** → `workbook/PREDICTIONS.tsv` `Status` + `Date_Resolved` + `Outcome` (the ledger's own column names), with the note "(10-Q-confirm pending: 10-Q frame §2 precedence)". The release-night grade stands unless the 10-Q's ratio or fraud attribution differs, which is the one case the 10-Q frame already says governs. **WAL-01** → a PROVISIONAL note only; the row is final at the 10-Q frame §1 cross-check. This names the procedure the two frames already imply; it changes no letter.*
  - ***Rates context to RECORD at the print (non-gating, for the §8 read):** 10Y ~5.24% intraday 9/28 (5.11% on 9/23); the Fed's +25bp on 9/16 (to 3.75-4.00%) is the Sept hike the Q2 NII guide assumed — delivered. At the print, record the named 6/30 and 9/30 10Y closes (the AOCI move runs between them).*
  - ***Non-gating records (log only, uninformative if absent):** (a) the second $60M substandard credit / LOI (KB-WAL-142): closed at ~carrying · closed at a loss · still held · not mentioned. (b) Office CRITICIZED $ and the CLD/lease-up criticized % (Q2 deck slide 24 analogue, KB-WAL-110) plus office maturities remaining/extended — the upstream bucket for WAL-01's classified line.*
  - ***Gaps ACKNOWLEDGED, deliberately NOT filled by annotation (writing them here would create grading rules after registration; routed to Will/PROME as a decision, audit M2):** (1) §5 has no letter for an appraisal disclosed **below** carrying with **no** specific reserve, or disclosed with no value relative to carrying. (2) §8's non-credit falsifier has no pre-set threshold for "sell-off" or "explains better", and no NO-VERDICT band. (3) §6 has no band for an absent NPL/coverage figure on management's basis; and §6 row 3 ("≥4 cumulative") is already satisfied by the 9/16 claim, so it cannot discriminate at Q3 (the informative read is whether credits 5-6 resolve at par or with charge-downs). If no rule is registered before the print, each of these grades UNRESOLVED and is recorded as such — never improvised.*
- *2026-09-28 ~15:5x ET (WQ-325, Will-ruled): the three rule gaps acknowledged in the 9/28 note above are now **REGISTERED as §10 below**, dated, 15 days before the earliest plausible print date (L170: 10/13). None of the three is left to grade UNRESOLVED by default. §1–§9 are unedited.*
- *2026-10-09 ~10:1x ET (WAL session #11): **PRINT DATE PINNED. Results after the market close on Mon 2026-10-19; call Tue 2026-10-20 at 12:00 p.m. ET.** Source: the issuer's own release dated 2026-10-06 (IR PDF `s21.q4cdn.com/328636679/files/doc_news/Western-Alliance-Bancorporation-Announces-Third-Quarter-2026-Earnings-Release-Date-Conference-Call-and-Webcast-2026.pdf`, read 10/9 10:0x ET; WALTER SIG-W-20261007-007 relayed the same). This frame was registered 9/24, **25 days before the print**, so it is not VOID. ⚠️ **Read-order consequence:** Stage 1 is Monday evening (release + deck); Stage 2 is the Tuesday noon call, so PENDING-CALL items sit overnight. The header's 'earliest plausible 10/13' is the L170 window-open date, not the print. `Resolve_By` 11/15 is unchanged (10-Q frame §8, 10/9). **Hotel (WQ-328, non-gating):** the deck's CRE-Investor composition slide (Q1 analogue: slide 22) can show hotel $ / % / LTV at 9/30. Slide 12 does not split hotel out of non-office classified. Hotel credit is a 10-Q datum (10-Q frame §8, 10/9). Log only.*

---

## 10. Rules registered 2026-09-28 under WQ-325 (dated additions; nothing registered in §1–§9 is edited)

**Authority:** Will, 9/28, verbatim: *"WQ-325: register the three missing print-frame rules by 10/09 as dated additions to the frame, each with an explicit no-verdict band. Edit nothing already registered. If a rule cannot be written before 10/13, that leg grades UNRESOLVED and the frame says so now."* All three are written here, so **no leg defaults to UNRESOLVED**. W5 (letter governs the thesis grade, band governs the ledger), W7 (half-open bands, printed precision) and W9 (explicit-only counting) apply. **Consequences are records only: no score, weight or confidence moves inside a grade (R3).**

### 10.1 — §5 addition: letter **B′** (appraisal in, below carrying, UNRESERVED)

Adds one letter to §5's table. It does not change A, A′, B, C or PENDING-10-Q.

| Q3 disclosure (release, deck or call) | Letter | Read |
|---|---|---|
| The appraisal is **disclosed BELOW carrying value** — an as-is or appraised value stated below the loan's recorded balance, or management saying the appraisal came in below / short of the balance — **with $0 charged off and NO specific reserve disclosed** (reserve stated as zero, or not mentioned) | **B′** | **Bear-lean, recognition DEFERRED.** Bear-medium KILL leg (b) is **NOT satisfied** (the appraisal is not benign). WAL-02's ledger is unaffected (no NCO). The reserve question is carried to the 10-Q frame §4. *"Carrying" = $99M unless the filing states a different recorded balance.* *[⤵ read cell superseded by §10.4(b): an UNDISCLOSED reserve is not a zero reserve]* |
| **⛔ NO-VERDICT band:** (a) an appraisal is said to be **received** but **no value or direction relative to carrying** is disclosed; (b) the release, deck and call **conflict** on the appraisal's direction | **NO-VERDICT** | No letter is assigned; KILL leg (b) stays **open**; carried to the 10-Q frame §4. Never graded benign (same rule as PENDING-10-Q). |

**Precedence (fixed now):** any charge-off or specific reserve ⇒ A or A′, never B′. B′ is only the zero-loss, zero-reserve case. The print letter is final for the print; whatever the 10-Q adds is graded in the 10-Q frame, never back-edited here. *[⤵ superseded in part by §10.4(b)]*

### 10.2 — §8 addition: the non-credit falsifier, with thresholds

**Step 1 — was there a sell-off?** The **reaction session** is the first regular session whose close follows the EX-99.1 release (an after-close release ⇒ the next day). **SELL-OFF** ⇔ WAL's close-to-close change **≤ −3.00%** **AND** WAL minus KRE, same session, **≤ −2.00pp**. Named closes (yfinance via `scripts/market.py`), cross-checked against REGINALD's exit log where it has the row. No sell-off ⇒ the falsifier is **NOT TRIGGERED** (recorded, and nothing further is graded).

**Step 2 — only on a SELL-OFF — classify each leg from the release, deck or call:**

| Leg | BREACH if (Q2 benchmark) | Carrier |
|---|---|---|
| **N1 NIM** | Q3 NIM **≤ 3.47%** (≥ 6bp below Q2's 3.53%; the guide was "stable" / "down maybe about a basis point") | EX-99.1 |
| **N2 Deposit cost** | Q3 total cost of deposits **≥ 1.88%** (≥ 10bp above Q2's 1.78% average, which was trending down) | EX-99.1 / deck |
| **N3 TBV/share** (the AOCI + capital-return hit) | Q3 TBV/share **< $63.24** (a QoQ decline) | EX-99.1 |
| **N4 Guidance** | Any 2026 guide line (NII, NIM, fees, deposits, loans, expenses) **lowered** against the Q2 revision (KB-117), or the NII guide withdrawn | Release / deck / call *[⤵ superseded by §10.4(a): direction-specific]* |
| **C Credit** (any one) | §4 **GUIDE BROKEN** · §6 row 1 **MISSED** · §5 letter **A, A′ or B′** · §3 count **≥ 1** | the existing legs' own grades |

| Verdict | Condition |
|---|---|
| **NON-CREDIT CONFIRMED** ("credit-only sufficiency" FAILS) | SELL-OFF **and** ≥ 1 of N1–N4 BREACH **and** no C breach *[⤵ label superseded by §10.4(a): "CONSISTENT WITH A NON-CREDIT EXPLANATION"]* |
| **CREDIT-CONSISTENT** | SELL-OFF **and** ≥ 1 C breach **and** no N breach |
| **⛔ NO-VERDICT** | SELL-OFF with **both** an N breach and a C breach · SELL-OFF with **neither** (unexplained — logged) · **any** of N1–N4 or the C legs **not printed** by the end of Stage 2 (name which) |

**Consequence:** recorded only. A NON-CREDIT CONFIRMED is an input to the next re-weight proposal (a separate dated edit); it moves nothing here. *[⤵ label per §10.4(a)]*

### 10.3 — §6 addition: a figure not printed on management's basis

| Case | Grade | Where it goes |
|---|---|---|
| **Row 1 (NPLs):** no NPL figure printed on the same basis as management's $567M (release, deck or call) | **NOT-PRINTED ⇒ PENDING-10-Q** | 10-Q frame §5, row "Mgmt's $567M NPL basis": graded there **only if** the 10-Q states management's definition. |
| **Row 2 (coverage):** no coverage ratio stated, **or** a ratio stated **without its denominator** | **NOT-PRINTED ⇒ PENDING-10-Q** (none stated) · **NO-VERDICT** (stated, denominator unstated — record the figure) | The §7 pin and the 10-Q frame §5 RETIRE leg are unaffected. |
| **Row 3 (six-credit count):** no count of "the six" stated | **NOT-PRINTED ⇒ UNRESOLVED** (no 10-Q carries this count) | — |
| **⛔ NO-VERDICT band, all rows:** the figure can be rebuilt on management's basis **only by inference** from this desk's lines (e.g. $562M nonaccrual + an assumed adjustment) | **UNRESOLVED** — never inferred | Record this desk's basis alongside (non-gating), as §6 already says. |

**Non-gating record added:** row 3 ("≥ 4 cumulative") was already met by the 9/16 claim, so at Q3 it cannot discriminate. **Log the outcome of credits 5 and 6** — resolved at par · resolved with a charge-down · still open · not mentioned (uninformative).

### 10.4 — Amendments registered 2026-09-28 ~16:3x ET (Will-directed corrections to §10.1 and §10.2 before first use; everything else in §10 stands)

**Authority:** Will, 9/28, verbatim: *"Lower expenses are incorrectly treated as bad guidance. The new rule flags any lowered guidance—including expenses—as adverse. Lower planned expenses can be favorable. WAL needs direction-specific conditions. It should also label the result 'consistent with a non-credit explanation,' unless evidence establishes causation."* · *"An undisclosed reserve is treated as zero. The new B′ grade accepts 'reserve not mentioned,' then calls the loan unreserved and recognition deferred. Those facts are unknown. Keep the below-book appraisal as adverse evidence, but distinguish explicit zero reserve from reserve undisclosed/pending the 10-Q."* The §10.1–§10.3 text is kept verbatim; the marked clauses are superseded by this section.

**(a) §10.2 — N4 is direction-specific, and the verdict label claims co-occurrence, not cause.**

| N4 guide line (vs the Q2 revision, KB-117) | ADVERSE (BREACH) if | Not a breach |
|---|---|---|
| NII growth | **lowered**, or the NII guide **withdrawn** | held or raised |
| NIM | guided **lower** than "stable" / "down about a basis point" | held or raised |
| Non-interest income (fees) | **lowered** below +13-17% | held or raised |
| Deposit growth | **lowered** below +$6B | held or raised |
| Non-interest **expense** | **RAISED** | held or **lowered** (lower planned expense can be favourable — never a breach) |
| Loan growth | — | **any change is LOGGED only**: WAL cut it in Q2 to fund buybacks, so its direction does not map to adverse |

**Verdict label:** SELL-OFF + ≥ 1 N breach + no C breach ⇒ **"CONSISTENT WITH A NON-CREDIT EXPLANATION"**. The frame names **no instrument that can establish that the non-credit leg CAUSED the move** (co-occurrence on one session is not causation), so no stronger label is available at the print; "credit-only sufficiency" is recorded as **NOT ESTABLISHED to have failed**, only as challenged. The CREDIT-CONSISTENT label and the NO-VERDICT band stand as registered. Consequence unchanged: a record only, an input to the next re-weight proposal, and nothing moves here.

**(b) §10.1 — B′ splits by what is actually disclosed about the reserve.** Both variants require the appraisal to be disclosed below carrying with **$0 charged off**, and both keep the below-book appraisal as **adverse evidence**: KILL leg (b) is **not satisfied**, and each counts as a **C (credit) breach** in §10.2.

| Reserve disclosure | Letter | Read |
|---|---|---|
| A specific reserve **explicitly stated as zero** | **B′₀** | Below-book appraisal, **explicitly unreserved: recognition deferred** (the §10.1 read, now limited to this case) |
| Reserve **not mentioned / not disclosed** in release, deck or call | **B′ᵤ** | Below-book appraisal, **reserve UNDISCLOSED — status unknown, PENDING the 10-Q** (10-Q frame §4). ⛔ **Never read as "unreserved" or "recognition deferred"**: those facts are unknown at the print |

**Precedence, restated:** any charge-off, or a **disclosed** specific reserve > $0 ⇒ A or A′ (unchanged); disclosed zero ⇒ B′₀; undisclosed ⇒ B′ᵤ. The §10.1 NO-VERDICT band (no value or direction relative to carrying; conflicting statements) stands.
- *2026-09-28 ~17:1x ET (WAL session #10, Will-directed pre-print pulls; **benchmarks and non-gating records only — no rule, letter or cell changed**; record → `research/2026-09-28_preprint-inputs-rates-consensus-short-interest.md`):*
  - ***Dated consensus (for the "priced vs surprise" read, §0/§8):** Q3 EPS **$2.43** (Nasdaq, 8 est.) / **$2.44** (Yahoo, 13 analysts), taken 9/28 17:13 ET; revenue **$989.0M** (Yahoo, 12); EPS trend −7.2% over 90 days. Charge-off, NPL and NIM consensus **UNAVAILABLE**. EPS basis (GAAP vs adjusted) not stated by either vendor ⇒ record the release's own figures and the basis gap, never infer. **Re-snapshot the day before the print** (KB-213 Stale_By).*
  - ***Rates context for §10.2 (record, does not change N1/N2):** WAL's own Q2 10-Q table (KB-212): NII +5.9% at +100bp / (8.6)% at −200bp (shock, dynamic, 12-month; average deposit beta 53%); EVE (4.4)% at +100 / (10.5)% at +200. Asset-sensitive on NII, EVE falls as rates rise.*
  - ***Short interest into the print (record):** FINRA 9/15 **5,974,409** shares, **5.48% of shares outstanding**, days to cover **6.4** (the series high; 4.30 at the Q2 print) — KB-214. The 9/30 settlement publishes ~10/9.*
  - ***One-line strike map (non-gating; TERRY/Will lane):** the Dec-18 $70P is in the money in Bear-fast ($52-62), Bear-medium ($58-66) and Tail ($35-45) = 25% combined v2.4 weight, and out of the money across Base ($74-82) and Bull ($86-94). Scenarios are thesis-horizon states, not a Dec-18 forecast. The $4.40 GTC is cancelled (Will 9/28).*
