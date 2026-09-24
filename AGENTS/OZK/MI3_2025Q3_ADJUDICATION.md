# OZK — the 2025Q3 MI3 step: adjudication

**Date:** 2026-08-23 · **Owner:** OZK · **Verdict (8/23): UNRESOLVED.** → ⚖️ **SUPERSEDED 2026-09-24 by §6: LEGITIMATE — the named debt-on-debt book's REPORTED balance fell (OBSERVED); the loans did not stay in item 4 (VERIFIED); economic runoff/repayment is the FAVOURED INFERENCE; reclassification out of the book (within NDFI or to C&I) is NOT SUPPORTED BY ENDPOINTS, NOT EXCLUDED** (verdict INFERRED-HIGH; identity VERIFIED at 5/5 quarters; *narrowed 2026-09-24 per CATO RB2 — §6.5*). Read §6 first.
**Task:** `inbox/processed/2026-08-13d_from-REGINALD_TASK-the-2025Q3-mi3-re-designation-legitimate-or-disclosure-narrowing.md` (Will-ruled 8/13, routed by PROME; read-path = `PROME/DOCKET.tsv` "next-OZK-session" row).
**Input artifact:** `AGENTS/REGINALD/reports/2026-08-13_OZK_MI3_adversarial_verification.md` §3, §7.
**Instrument:** OZK's own 18-quarter FFIEC series, `workbook/CALL_REPORT_SERIES.tsv` (ID_RSSD 107244, FFIEC CDR PWS RetrieveFacsimile SDF, pulled 2026-08-07) — **path (c)** of the three the packet named. Paths (a) transcripts and (b) Management Comments remain **UNRUN**.

> ⛔ **ZERO grades, thresholds, probabilities or scenario weights move on this document.** OZK-09 stays 45%; A30/B45/C8/D17 stand; conviction 🔴🔴 unchanged. This is an instrument adjudication, not a thesis input.
>
> ⚠️ **Scope fence, carried verbatim from the packet because it is one keystroke from being misread:** **MI3 is CRE *not secured* by real estate.** **RESG and every secured book are a different object and are untouched by everything below.** *"OZK's hidden-CRE disclosure fell"* ≠ *"OZK's CRE exposure fell."*

---

## 0. The three answers, up front

| # | Claim | Verdict |
|---|---|---|
| **1** | BROCK's **written-down-not-repaid-down** branch — the one REGINALD asked me to test **first** because it is the branch its Call-Report-only decomposition is blind to | **🔴 REFUTED at the primary.** Hard, not a lean. |
| **2** | REGINALD §3: *"item 9 moved only +$98M… what is left is that the loans never moved"* | **🟠 The discriminator is measured on the wrong window.** At the step quarter item 9 fell **−$576.5M**. The loans **did** move. |
| **3** | Legitimate re-designation **vs** disclosure narrowing | **⚪ UNRESOLVED — and now with THREE live branches, not two.** Not settleable from Call Reports. |

---

## 1. The step quarter, decomposed ($K, from OZK's own series)

| Quarter | MI3 `RCON2746` | Δ | item 4 C&I | Δ | item 9 (9a+9b) | Δ | **items 4+9** | **Δ** | Total loans | Δ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025-03-31 | 1,133,405 | — | 2,066,290 | — | 2,539,394 | — | 4,605,684 | — | 31,107,873 | — |
| 2025-06-30 | 1,202,101 | +68,696 | 2,330,142 | +263,852 | 3,177,436 | **+638,042** | 5,507,578 | +901,894 | 33,005,054 | +1,897,181 |
| **2025-09-30** ⭐ | **769,920** | **−432,181** | 2,870,535 | **+540,393** | 2,600,949 | **−576,487** | 5,471,484 | **−36,094** | 32,846,114 | −158,940 |
| 2025-12-31 | 721,546 | −48,374 | 3,431,585 | +561,050 | 2,755,752 | +154,803 | 6,187,337 | +715,853 | 32,317,785 | −528,329 |
| 2026-03-31 | 489,284 | −232,262 | 3,818,846 | +387,261 | 3,071,157 | +315,405 | 6,890,003 | +702,666 | 32,975,210 | +657,425 |
| 2026-06-30 | 430,277 | −59,007 | 4,603,672 | +784,826 | 3,275,845 | +204,688 | 7,879,517 | +989,514 | 32,560,970 | −414,240 |

**Cross-check that authenticates the read:** REGINALD's published item-9 figure reproduces on my series **exactly** — 2025Q2 → 2026Q2 is `3,177,436 → 3,275,845 = +98,409K`, its "**+$98M**". Getting the same number off an independent pull is what establishes that I am reading the *same measurement* it made, before disputing what that measurement covers.

---

## 2. Finding 1 — BROCK's write-down branch is REFUTED

REGINALD: *"if the re-designated balance was **written down** rather than repaid, that is a materially different story… **Please test this one first; it is the cheapest and it is the one I am blind to.**"*

It is cheap, and the answer is clean, because the Call Report carries a charge-off line for **exactly this loan class**:

| Test | Value at the step quarter | Read |
|---|---|---|
| **`RIAD5409`** — charge-offs on CRE-purpose loans **not secured by RE**, i.e. the MI3 class itself, YTD | **$0** at 2025-09-30 — **and still $0** at 2025-12-31 and 2026-03-31 | The dedicated instrument for this exact branch reads **zero** through the step and for two quarters after |
| **Bank-wide NCO**, 2025Q3, all books | **$34,479K** (0.42% ann.) | Even at **100% attribution** — every charge-off the whole bank took that quarter assigned to this one memo line — it is **8.0%** of the $432,181K decline |

**⇒ The $432M did not leave by being written down.** The first nonzero `RIAD5409` in eighteen quarters is **$42,437K at 2026-06-30 — three quarters AFTER the step.** *(That later print is a real and separate finding, already routed to BROCK 8/7 as UNATTRIBUTED; it is not evidence about 2025Q3 and is not used as such here.)*

---

## 3. Finding 2 — the surviving discriminators were run on a window that cannot see the event

REGINALD's §3 refutes four branches and concludes *"the loans never moved — they stayed in item 4 and only the CRE-purpose designation changed."* **Two of those four refutations are measured across 2025Q2 → 2026Q2 — a window that spans the step and nets it against what came after.**

**(a) Item-9 migration.** "+$98M" is the **net** of one −$576M step and **+$675M of regrowth over the following three quarters** (+155, +315, +205). At the step quarter itself **item 9 fell $576,487K** — the only decline anywhere in the window, and 5.9× larger than the net. A discriminator that reports +$98M for a quarter in which the line fell $576M is not weak evidence; it is **blind to the event it was built to test**.

**(b) Repayment.** Refuted on the grounds that *"a repayment story cannot coexist with a flat total book (−$444M) and a +$2,274M C&I line"* — again the YoY window. **At the step quarter those numbers are different:** total loans **−$158.9M**, item 4 **+$540.4M**, item 9 **−$576.5M**. A $432M repayment inside a $576M container decline, alongside $540M of new C&I origination elsewhere, is **arithmetically coherent**. Repayment is **not refuted at the step quarter**.

**⇒ "What is left is that the loans never moved" does not follow.** ⚠️ This is a correction to a *measurement window*, **not** to REGINALD's data — its cells are triple-verified and I reproduce them to the dollar. `[[finding_window_start_at_an_extremum_inverts_the_move]]`, `[[finding_instrument_reports_clean_against_the_wrong_reference]]`.

---

## 4. Finding 3 — the sharper anomaly, which none of the four branches describes

The obvious next inference is **migration**: item 9 −$576M against item 4 +$540M in the same quarter looks like a ~1:1 transfer, and OZK reports its **entire** MI3 balance inside item 9.a (`RCONPV09` ≡ `RCON2746` to the dollar at **6/6 quarters, including both sides of the step** — `CALL_REPORT_2026Q2_LOG.md` §P-OZK-1), so anything landing in item 4 leaves the memo by construction.

**I ran the falsifier on my own inference and it does not survive.** Item 4's quarterly growth across this window is **+264 / +540 / +561 / +387 / +785 ($M)**. The step quarter's **+$540M is squarely mid-run-rate** — item 4 was growing this fast anyway. The "1:1 offset" is a **coincidence of magnitudes against a trend**, not evidence of a transfer, and RC-C carries no loan identifiers that could settle it. `[[finding_crosscheck_with_free_parameter_validates_nothing]]`

**What does survive is an asymmetry inside item 9.a — and it is the real finding here:**

| | item 9.a total | of which MI3 (the memo bucket) | share |
|---|---:|---:|---:|
| **2025Q2 BUILD** | **+639,725** | +68,696 | **10.7%** |
| **2025Q3 UNWIND** | **−576,450** | −432,181 | **75.0%** |

**The money that came in and the money that went out were not in the same sub-bucket.** OZK's Q2-25 NDFI build was **~89% outside** the sub-bucket carrying its entire CRE-purpose memo balance; the Q3-25 unwind was **75% from inside it**. So the step is **not** a round-trip of the prior quarter's spike: 9.a ends Q3-25 roughly where it sat at Q1-25 (+$63M), while **MI3 ends $363,485K BELOW its Q1-25 level.** The memo balance **failed to track its own container in both directions.**

**That asymmetry is what needs explaining, and none of the four tested branches predicts it.**

---

## 5. Disposition

**§1 of the task packet: UNRESOLVED.** Not settleable from Call Reports — the packet's own stated-acceptable answer, and I would rather give it than a lean.

**But the field is WIDER than the packet's framing, not narrower.** The packet presented a two-way fork (legitimate re-designation vs narrowing) resting on the premise that everything else was refuted. With write-down refuted and migration + repayment both un-refuted at the step quarter, **three branches are live**:

| Branch | Status at the step quarter | What would settle it |
|---|---|---|
| **Written down** | 🔴 **REFUTED** — `RIAD5409` $0, bank NCO ≤8% of the move | — |
| **Migrated 9.a → item 4** | ⚪ **LIVE, unprovable from RC-C** — magnitudes fit, but item-4 growth is within its own trend | Loan-level detail RC-C does not carry |
| **Repaid out of 9.a** | ⚪ **LIVE** — REGINALD's refutation used the YoY window; coherent at the step quarter | Management Comments (path b) |
| **Re-designated in place** | ⚪ **LIVE** — the packet's original hypothesis, now one of three rather than the residual | Transcripts (path a) / Management Comments (path b) |

**Governing correction, carried:** REGINALD's own base rate — a step of this kind occurs in **17 of 154** cohort QoQ transitions (**11.0%**, 7 of 14 banks), and OZK's ranks **3rd by absolute dollars behind two WAL steps**. `RCON2746` is a **step-prone line cohort-wide**. **This is an ordinary instance of an instrument property.** It should be chased at the price of an ordinary instance — which is why paths (a) and (b) are recorded as **owed-if-cheap**, not escalated. `[[finding_base_rate_the_instrument_before_its_event_table]]`

**What I carry forward as REGINALD asked, with the wording it specified:** *a bank whose C&I book doubles while its memo-3 disclosure falls 64% is disclosing less about a larger book* — **as a description of the numbers, not as an accusation.**

**Owed next (cheap, deferred to a session with the window):**
1. **Path (b) — Call Report Management Comments for 2025Q3.** The packet calls this the highest-value unrun item and the reason is structural: ~~OZK files no 10-Q~~ ⛔ **FALSE — retracted 2026-08-28: OZK files Form 10-Q with the FDIC (cert 110), not the SEC.** An empty EDGAR CIK is the expected observation. *(This sentence survived the 8/28 retraction sweep in this file — found and struck 2026-09-24 while running exactly the path it had closed; §6 is that path.)*
2. **Path (a) — Q3-2025 call transcript** (Quartr), with Q2-25 before / Q4-25 after. ⚠️ **Absence of comment settles NOTHING** — a −$432M memo move is not something an analyst asks about, so silence is the expected state on both branches.
3. **The §4 asymmetry** is the sharpest question and neither path was designed to answer it. Ask it directly: *what NDFI lending did OZK add in Q2-2025 and retire in Q3-2025, and why was the CRE-purpose designation attached to the second and not the first?*

**Unchanged and still safe to cite** (REGINALD's, re-confirmed against my series): **`37.6%` is dead** — it appears at no quarter on either basis, now on four independent paths. **OZK ranks 5th of 14 on both bases**, and **"most hidden-CRE-concentrated in the cohort" is RETRACTED by its owner.**

---

*Instrument: `workbook/CALL_REPORT_SERIES.tsv` (18 quarters, 2022-03-31 → 2026-06-30). Every figure above is from that file, which was pulled 2026-08-07 under a pre-registered LOG-ONLY scope and has moved no grade then or now. Working for the underlying pull → `CALL_REPORT_2026Q2_LOG.md`.*


---

## 6. ⚖️ VERDICT 2026-09-24 — DOCKET L181 (Will-ruled 8/13; PROME-directed this session)

**LEGITIMATE — OBSERVED: the 2025Q3 MI3 step is a ~$430M decline in the REPORTED balance of OZK's RESG "debt-on-debt" book, reported under an unchanged definition, and the balance was never in item 4 (so no re-designation of loans left in item 4). INFERRED: the decline is economic runoff (repayment) — favoured, not proven. NOT EXCLUDED: that some of the loans that left the book were reclassified to another NDFI type or to C&I — net endpoints cannot rule a transfer out (§6.5).** Token: **INFERRED-HIGH** on the verdict · **VERIFIED** on the identity it rests on · **UNKNOWN** on the loan-level exit mechanism (repaid vs refinanced away vs other).

### 6.1 The instrument that settles it — path (b)'s real form: the FDIC-filed 10-Qs

§5 recorded path (b) as closed because "OZK files no 10-Q." It does. Pulled this session from FDIC FLNG (`/api/instflng/{id}/attachment/1`): **Q2'25 10-Q (FLNG 11782, `raw/Q2_2025_10Q.pdf`) and Q3'25 10-Q (FLNG 11823, `raw/Q3_2025_10Q.pdf`)**, read alongside the local Q1'26 and Q2'26 10-Qs. Each carries management's own figure for the RESG debt-on-debt book (loans to NDFIs "collateralized by an assignment of a promissory note and all related note documents"), reported as Call Report "other" loans:

| Quarter-end | 10-Q debt-on-debt funded balance (mgmt, text) | `RCON2746` MI3 ($K, Call Report) | Match |
|---|---:|---:|---|
| 2024-12-31 | **~$1.06B** [Q2'25 10-Q p.37] | 1,055,957 | ✅ |
| 2025-06-30 | **~$1.20B** [Q2'25 10-Q p.37] | 1,202,101 | ✅ |
| **2025-09-30** ⭐ | **$0.77B** [Q3'25 10-Q p.37] | **769,920** | ✅ |
| 2026-03-31 | **~$0.49B** [Q1'26 10-Q] | 489,284 | ✅ |
| 2026-06-30 | **~$0.43B** [Q2'26 10-Q] | 430,277 | ✅ |

**5 of 5 quarters, both sides of the step, to the 10-Q's rounding.** OZK's MI3 **is** the debt-on-debt book — nothing else is in the line. (KB-OZK-223 had tied it at the two 2026 quarters; this extends it across the event.)

### 6.1b REGINALD's named discriminator, RUN — Memo-10 NDFI sub-buckets (FFIEC CDR RetrieveFacsimile SDF, RSSD 107244, pulled 2026-09-24)

REGINALD's 9/24 packet (`inbox/…_from-REGINALD_L181-mi3-input-delta…`) withdrew its §3(d)/(e) and named `RCONPV05`–`PV08` as the unrun test of whether the step moved *within* 9.a.

| $K | 6/30/2025 | 9/30/2025 | Δ | 10-Q text 9/30/25 |
|---|---:|---:|---:|---|
| PV05 mortgage credit intermediaries | 0 | 0 | 0 | — |
| PV06 business credit intermediaries | 1,161,937 | 1,184,574 | **+22,637** | $1.18B ✅ |
| PV07 private equity funds | 799,272 | 586,636 | **−212,636** | $0.59B ✅ |
| PV08 consumer credit intermediaries | 0 | 45,729 | **+45,729** | $0.05B ✅ |
| **PV09 other NDFI = MI3 = debt-on-debt** | 1,202,101 | 769,920 | **−432,181** | $0.77B ✅ |
| **Σ = J454 item 9.a** | 3,163,310 | 2,586,859 | −576,451 | $2.59B ✅ |
| *Unfunded commitments, "other" NDFI (PV16)* | *518,243* | *422,842* | *−95,401* | — |

**Read:** (1) the four sub-buckets tie to the 10-Q's NDFI breakdown at every cell — the 10-Q and the Call Report are the same classification, reported twice; (2) ~~no within-9.a relabel of the debt-on-debt book~~ **the endpoints give no positive sign of a within-9.a relabel** — the NDFI buckets that grew added only $68M net against a $432M fall — ⚠️ **but that is a NET comparison and cannot exclude one (§6.5: a PV09→PV06 transfer offset by PV06 runoff fits every endpoint exactly);** (3) REGINALD's "$144M residual" is **PE-fund loans −$213M** (subscription/fund-finance runoff, consistent with the Q1'26 Munn pullback from Fund Finance, LESSONS §CIB) net of +$68M elsewhere; (4) the debt-on-debt book's **unfunded commitments fell too (−$95M)** — consistent with loans and their undrawn lines retiring together, ⚠️ but a relabelled facility would carry its commitment out of PV16 the same way, so this does not discriminate either.
⚠️ **Limit, stated:** the NDFI → C&I branch is **not** falsifiable from these cells — a reclassified borrower would leave PV09 the same way a repaid one does. It stays ⚪ unsupported (no positive evidence; would require OZK to have re-coded loans it still calls NDFI loans in its own 10-Q text), not refuted.
**REGINALD's fork (i) — a separate, open question, carried not answered:** MI3 ≡ PV09 at every quarter means **zero** CRE-purpose balance is reported from item 4, ever. Either OZK's C&I book contains no CRE-purpose loans, or OZK populates memo 3 from the debt-on-debt book only. **UNKNOWN** — not L181's question, and no filing seen addresses it.

### 6.2 Why that decides the question

| Branch (from §5) | Status now | Evidence |
|---|---|---|
| **Re-designated in place (loans stayed in item 4, label moved)** — REGINALD §3(e), the packet's hypothesis | 🔴 **REFUTED** | (i) the MI3 balance was never in item 4 — `RCONPV09` ≡ `RCON2746` in item 9.a both sides of the step (§4); (ii) management's own **separately-stated** debt-on-debt balance fell $1.20B → $0.77B in the same quarter. A label change would leave management's book figure flat. |
| **Disclosure narrowing** | ⚪ **NOT SUPPORTED — not excluded** *(was 🔴 REFUTED; narrowed 9/24, CATO RB2)* | No positive evidence of narrowing. An unchanged definition of the book that REMAINS does not identify the loans that LEFT it, so a relabel out of the book is not excluded. What is observed: the debt-on-debt definition text is **unchanged** Q2'25 → Q3'25 → Q1'26 → Q2'26. And at Q3'25 disclosure **widened**: the 10-Q gave the first full NDFI breakdown — **$2.59B total = $1.18B business credit intermediaries + $0.59B PE funds + $0.05B consumer credit intermediaries + $0.77B debt-on-debt** — which ties to Call Report item 9.a (~$2,587M). |
| **Re-designated within NDFI** (d-o-d loans relabelled as another NDFI type) | ⚪ **NOT SUPPORTED BY ENDPOINTS — NOT EXCLUDED** *(was 🔴 REFUTED; narrowed 9/24, CATO RB2)* | ~~That would leave item 9.a flat~~ — **wrong: it would not**, if the receiving bucket ran off at the same time. CATO's counterexample fits every reported cell: move 432,181 PV09→PV06, run PV06 off 409,544 net ⇒ PV06 +22,637, PV09 −432,181, 9.a −576,451. Excluding it needs FLOW evidence (gross originations/payoffs by sub-bucket), which no filing seen carries. |
| **Written down** | 🔴 REFUTED (8/23, unchanged) | `RIAD5409` $0 through the step |
| **Repaid / refinanced away** | 🟢 **MOST CONSISTENT — INFERRED, not verified** | Q3'25 was OZK's **record RESG repayment quarter, $2.44B** (Q3'25 Mgmt Comments, Fig. 12: "the recent increase in debt financing available for projects has also contributed to RESG repayments"). A $0.43B exit from a RESG-originated book inside a $2.44B RESG repayment quarter is ordinary. No filing attributes it loan-by-loan. |
| **Migrated to item 4 (C&I)** | ⚪ **Not supported — not excluded** | Would require reporting NDFI loans outside item 9 against Call Report instructions; item 4's +$540M sits inside its own +$264M…+$785M run-rate (§4). No evidence for it; not provable absent loan-level data. |

### 6.3 What remains true, and what this does NOT say

- **Scope fence (unchanged):** MI3 = CRE-purpose **not secured** by real estate. Nothing here touches RESG secured credit, IQHQ/RaDD, classified balances or OZK-09.
- **Thesis relevance flips from "disclosure" to "book":** the debt-on-debt book (the P-OZK-2 successor pillar, ruled 8/23 as SUBJECT) **shrank 64% in 12 months (6/25 → 6/26) ($1.20B → $0.43B)** and **then** began charging off — `RIAD5409` **$42.4M H1-26, the first nonzero in 18 quarters**, on a $0.43-0.49B residual ⇒ ~9% of the residual in six months. That is the **adverse-selection shape** the RESERVOIR thesis predicts (good credits refinance out, the residue sours) — recorded as a **description**, moving no number.
- REGINALD's *"disclosing less about a larger book"*: the debt-on-debt book **is** disclosed in the 10-Q every quarter, and the C&I growth is **most likely** a different book (item 4, CIB, in-trend) — ⚠️ *but with NDFI→C&I not excluded (§6.5), "most likely" is the claim, not "is".*

### 6.4 What would change this verdict

1. **Any OZK filing, amendment or transcript stating that debt-on-debt loans were reclassified, re-coded or transferred** (to item 4, to secured CRE, or out of the NDFI definition) in 2025Q3 → re-opens re-designation.
2. **A Call Report amendment** restating 2025Q3 RC-C item 9.a or `RCON2746`.
3. **Loan-level evidence** (UCC/recorder, trade press) of specific debt-on-debt credits that stayed on OZK's books after 9/30/25 but outside the book → migration branch revives.
4. **Path (a) — the Q3'25 call transcript — remains UNRUN** (not local; Quartr not connected). Per §5, silence there settles nothing; an explicit statement would.

*Instruments: FDIC FLNG 11782 / 11823 (pulled 2026-09-24, pdfminer text), local Q1'26 + Q2'26 10-Qs, Q3'25 Mgmt Comments, `workbook/CALL_REPORT_SERIES.tsv`. ZERO grades, thresholds, probabilities, weights or conviction moved.*

### 6.5 Narrowing — CATO RB2 (2026-09-24, relayed by PROME, `inbox/processed/2026-09-24_from-PROME_CATO-RB2…`)

**Accepted in full.** §6.1b–6.2 as first written excluded within-NDFI reclassification **categorically** on net endpoint comparisons ("other buckets grew only +$68M"; "9.a would stay flat"). Net endpoints cannot refute a transfer that is offset by runoff. CATO's counterexample (hypothetical, $K) fits every reported cell exactly: transfer 432,181 PV09→PV06, then PV06 net runoff −409,544 ⇒ PV06 +22,637 ✓ · PV09 −432,181 ✓ · PV07 −212,636 ✓ · PV08 +45,729 ✓ · 9.a −576,451 ✓.

| Layer | Claim | Token |
|---|---|---|
| **OBSERVED** | The reported debt-on-debt balance fell $1.20B → $0.77B (10-Q p.37 ≡ `RCON2746`), under unchanged definition text; Q3'25 disclosure added the NDFI breakdown | VERIFIED |
| **OBSERVED** | The MI3 balance sat in item 9.a (PV09), not item 4, on both sides of the step — REGINALD's withdrawn "stayed in item 4" branch is **not** revived | VERIFIED |
| **INFERRED** | The decline is economic runoff / repayment (record $2.44B RESG repayment quarter) | INFERRED — favoured |
| **NOT EXCLUDED** | Some or all of the exits were reclassifications out of the book (to another NDFI type, or to C&I) | not supported by endpoints, not excluded |

**Verdict LEGITIMATE stands** as: the reported book really shrank, and the favoured reading is runoff. It is **not** a finding that no reclassification occurred. What would upgrade "not excluded" to "refuted": gross flow evidence by sub-bucket (originations/payoffs/transfers), or an OZK statement on the Q3'25 composition change. Neither is in any filing read. Correction packets sent to REGINALD and BROCK the same day.
