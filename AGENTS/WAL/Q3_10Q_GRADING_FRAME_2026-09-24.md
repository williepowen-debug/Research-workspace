# WAL Q3 2026 10-Q — Pre-Registered Grading Frame

**Pre-registered:** **Thu 2026-09-24** (WAL session #7, PROME round 2, DOCKET **L171**). **Earliest plausible filing date: Sat 2026-10-24.** L171 anchors on the Q2 10-Q, filed 7/31 = print + 10 days. This frame is written **30 days before that date**. It is the companion to `Q3_PRINT_GRADING_FRAME_2026-09-24.md` (the "print frame"). Same discipline: grade verbatim, pre-filing annotations dated in §8, **no edits after the filing**.
**Filing date: UNKNOWN. ⛔ Pin it from the EDGAR filing index (CIK 0001212545, form 10-Q, period 2026-09-30) when it appears, never from expectation.** The Q3 print date isn't announced either (`KB-WAL-197`).
**Specs of record:** the **8/20 P2/P3 repairs (`df87ac3f4`, Will-ruled 8/12 row 32b)**. They are built on here, not re-litigated. `WAL-01` 25% · `WAL-02` 50% · `Resolve_By` 2026-11-15, both `workbook/PREDICTIONS.tsv`.
**Structural fact that shapes this frame (`KB-WAL-151`):** no 10-Q publishes classified or criticized loans **by property type**, and none names office migrations. So this filing **cannot** carry WAL-01's primary datum or the migration count. It carries the cross-checks, the attribution, and the legs the print frame marked **PENDING-10-Q**.

---

## 1. WAL-01: the row's own 10-Q CROSS-CHECK leg (makes the print read final or void)

**Letter (P2):** *"CROSS-CHECK: the Office $ must be ≤ the Q3 10-Q total classified-assets balance."*

- **Cell:** the 10-Q **total classified ASSETS** at 9/30/26 = **classified loans (Note: Loans, risk-category table, company total) + repossessed assets (OREO)**. ⚠️ **Basis pin (measurement only, grounded in arithmetic):** the Q2 deck's "classified assets" total of $1,128M equals **Q2 10-Q classified loans $1,002M + OREO $126M** exactly (`KB-WAL-108/151/155`). The deck and 10-Q tie only on that combined basis. Comparing the deck's Office $ against classified loans alone would test the wrong total.
- **PASS** (Office $ from the deck ≤ that total) ⇒ the print frame's **Stage-1 WAL-01 grade becomes FINAL** (CONFIRMED or INVALIDATED as graded).
- **FAIL** (Office $ > the total) ⇒ the deck read is **VOID**, and WAL-01 grades **NO-VERDICT / INSTRUMENT-CONFLICT**. It never defaults to either side.
- **Consistency check, recorded but not gating:** deck total classified vs (10-Q classified loans + OREO). A gap of more than $10M is logged as a basis break for the Q4 frame.
- **Missing disclosure:** risk-category total or OREO balance not stated ⇒ **CROSS-CHECK-UNRUN**. The Stage-1 grade then stands with that tag. An unrunnable check can't void a read; only a conflict can.
- **If the print graded WAL-01 NO-VERDICT (slide absent):** this 10-Q cannot rescue it (no Office line). WAL-01 stays **NO-VERDICT**. ⛔ **Do not substitute Other CRE-NOO classified or nonaccrual as a proxy.**

## 2. WAL-02: resolution point and confirmation (Q3-only, exhaustive: >40bps CONFIRMED · ≤40bps INVALIDATED)

- **Role:** the **print (EX-99.1) grades WAL-02**, and this filing **confirms or corrects** it. If the print frame logged **PENDING-10-Q** (no ratio or base in the release), **this filing grades it**.
- **Cell:** Q3 net charge-offs (ACL roll-forward, the quarter column: charge-offs minus recoveries) ÷ average HFI loans, annualized, **company-reported ratio at printed precision governs** (W7). **40.0bps = INVALIDATED.**
- **Ex-fraud (W2):** subtract only Q3 charge-offs **the filing explicitly attributes** to Cantor, LAM or a newly designated fraud item. The attribution source is the MD&A "Legal Disputes Related to Credit Facilities" paragraphs (§3). None attributed ⇒ total = ex-fraud.
- **Precedence on conflict:** if the 10-Q's ratio or fraud attribution differs from the release **at printed precision**, **the 10-Q governs** as the later, fuller filing. The grade is recomputed and logged as a **CORRECTION of the Stage-1 grade**, never a silent overwrite. It is also the one case where a release-night grade can flip.
- **Missing disclosure:** no NCO ratio and no average-loan base in either the release or the 10-Q ⇒ compute NCO$ × 4 ÷ the average-balance-table HFI loans. If even that isn't possible ⇒ **NO-VERDICT**, and `Resolve_By` 11/15 is **re-pinned with a reason**, never forced.

## 3. Cantor ledger tie-out + the LAM/Jefferies arc (V2, excluded from composite; forward two-way)

Q2 10-Q carried (`KB-WAL-148`): $98.5M to nonaccrual (9/30/25) · $29.6M specific allowance · $26.1M Q1-26 charge-off · **Q2: "No additional charge-offs"** · two UHNW guaranties (limited + full). The **Q2 filing DROPPED** the remaining specific allowance ($3.5M at 3/31), the ~$70M residual carrying value and the senior-lien figures.

| Cell (MD&A "Legal Disputes…" → Cantor Group V) | Confirms tail deterioration | Refutes / benign | Missing means |
|---|---|---|---|
| **Q3 Cantor charge-off** | **> $0** (recorded as fraud: excluded from WAL-02 under W2) | "No additional charge-offs" | Paragraph absent ⇒ **NARROWED DISCLOSURE**, logged. Not benign, not a charge |
| **Recovery recorded** (guaranty, title policy, collateral sale) | none | **any recovery $ > 0** ⇒ two-way leg confirmed | Uninformative |
| **Remaining specific allowance / residual carrying value** | increase, or residual written below ~$70M without a recovery | residual falls **with** a stated recovery | Not stated (the Q2 pattern) ⇒ **UNRESOLVED**, carried. Never inferred |
| **★ The $64M candidate tie:** Q2 MD&A's "purchase of **$64M** of loans with more-than-insignificant deterioration" (PCD) vs `KB-WAL-123`'s senior protective liens of **$64M** | The filing **explicitly** connects the PCD purchase to Cantor or protective liens ⇒ **TIE CONFIRMED**. The Cantor exposure is then larger than the ~$70M residual (liens bought on top) | The filing attributes the PCD purchase to something else ⇒ **TIE REFUTED**, candidate struck | Silence ⇒ **UNTIED, stays a candidate**. Matching magnitudes are never promoted to a tie by inference |

**LAM / Jefferies (NY Supreme Court; complaint amended May 2026, `KB-WAL-152`):** (a) **Jefferies' counterclaim** (the $25M Point Bonita deposit, `KB-135`, press only): disclosed ⇒ **confirmed at primary**; absent ⇒ **uninformative** (non-existence and immateriality look identical; carried from the Q2 read §6). (b) **Recovery to date** figure: stated ⇒ tests Jefferies' "more than half recovered" claim; absent ⇒ unresolved. (c) Any ruling, settlement or accrual ⇒ a material development ⇒ packet to OTTO/BROCK (standing send rule).

## 4. The $99M: bucket question + disposition (print frame §5 letters carried)

**Bucket (unresolved since the Q2 read, `KB-WAL-150`):** three candidates at 6/30. Q2 nonaccrual moves: **Other CRE-NOO +$16M · Other C&I +$44M · Construction & land development +$24M**. The filing's own label is a hybrid ("a life science laboratory/office CRE loan").

- **Cell:** the nonaccrual-by-segment table QoQ (9/30 vs 6/30) + segment charge-offs in the ACL roll-forward + any narrative naming the loan.
- **IDENTIFIED** only if the **narrative names the segment** for the loan. **CANDIDATE** if a segment's nonaccrual or charge-off move matches the disposition amount within **±$10M** but the narrative doesn't name it. Arithmetic alone never identifies (the W9 principle).
- **Still unresolved** ⇒ recorded as UNRESOLVED for a third filing. The Q4 frame then asks management directly (call).

**Disposition — graded here if the print left it PENDING-10-Q, or CONFIRMED here if the print graded it:**

| Letter (print frame §5) | 10-Q evidence |
|---|---|
| **A** majority charged off (>$49.5M cumulative, W6), or sold at that loss | charge-off attributed to the credit, or a sale loss |
| **A′** partial charge-off (≤$49.5M), or an appraisal disclosed below carrying value with a specific reserve | same, smaller |
| **B** still nonaccrual, no charge-off | still named as nonaccrual, or no segment move consistent with exit |
| **C** returned to accrual, paid off, sold at or above carrying, upgraded, or appraisal at or above carrying | named cure or exit, or a segment nonaccrual **fall ≈ $99M with no matching charge-off** *and* narrative support |
| **Nothing anywhere** (release, call, 10-Q) | ⛔ **NO-VERDICT, carried to Q4. Never C.** The Bear-medium KILL leg (b) stays **open** |

- **⚠️ Subsequent-events note:** read it **first**. That's where the original $99M migration reached the tape (Q1 10-Q, `KB-WAL-140`). Any post-9/30 development on this or any other credit counts as dated evidence there.

## 5. The print frame's PENDING-10-Q legs + 10-Q-only disclosures

| Leg | Cell (10-Q) | Threshold / grade | Missing means |
|---|---|---|---|
| **Thesis-RETIRE coverage leg** (basis **pinned in print frame §7**: (funded + unfunded ACL) ÷ total nonaccrual) | ACL on funded HFI + **ACL on unfunded commitments** (10-Q only: the release may omit unfunded) ÷ nonaccrual total | **> 100% ⇒ leg MET** (one of the RETIRE rule's three conditions; retirement also needs broadening N=3 + a benign appraisal) · ≤ 100% ⇒ NOT MET | Unfunded ACL not stated ⇒ **funded-only ratio reported, labelled; the leg is NOT graded MET** on a partial numerator |
| **Full-NPL basis** (print frame §6 secondary) | nonaccrual + 90+ days accruing + **accruing restructured** (`KB-WAL-156`, Q2 $781M) | **Reported, non-gating.** Accruing restructured Q2 $164M (+$33M): **another rise ⇒ the leading channel is still filling** (logged for V1b-magnitude) | Line absent ⇒ logged |
| **Mgmt's $567M NPL basis** (print frame §6) | reconcile mgmt's NPL definition to the 10-Q's lines | Explained ⇒ basis note closed · unexplained ⇒ carried | — |
| **OREO** (`KB-WAL-155`: $126M, 22 properties, "primarily office") | balance, property count, valuation losses | **Count up again ⇒ WAL still taking title to office** (magnitude signature) · count down with zero valuation losses ⇒ benign | — |
| **V3 NDFI table** (Q2: **$15,812M = 25.9% of HFI**, record) | NDFI total $ and share of HFI | **Share > 25.9% ⇒ measurement beats plan ⇒ write P1 re-score proposal (V3 1/5 → up)** · share < 25.9% **and** $ down QoQ ⇒ mgmt's "warehouse won't be as active" plan confirmed; 1/5 holds on primary evidence at last · otherwise ⇒ MIXED | Table absent ⇒ P1 stays open |
| **Buyback** (bull leg, `KB-WAL-119/196`: $150M H2, "a little bit more in Q3 than in Q4") | Part II Item 2 repurchase table, Q3 $ | **≥ $75M ⇒ on track** · $50–75M ⇒ lagging · **< $50M ⇒ behind guide** | Table absent ⇒ share count delta as proxy, labelled |
| **AOCI / AFS mark** (10Y 5.11% [9/23, ^TNX indicative]) | AOCI and unrealized AFS loss at 9/30 vs 6/30 | Recorded. Context for the capital-rules leg, non-gating | — |

## 6. Read order (filing day)

① **Subsequent-events note** (§4) → ② MD&A NPA narrative + nonaccrual-by-segment (§4, §5) → ③ ACL roll-forward: charge-offs, recoveries, funded + unfunded ACL (§2, §5) → ④ "Legal Disputes Related to Credit Facilities": Cantor, LAM (§3) → ⑤ risk-category totals + OREO (§1) → ⑥ NDFI table, repurchases, AOCI (§5).

## 7. Guardrails

- **Scope fence:** this filing carries neither WAL-01's Office line nor migration names. **Never proxy them from segment data.**
- **Ledger ≠ thesis:** WAL-01/02 grades go to `PREDICTIONS.tsv` (**the TSV leg is named here explicitly, PAT-053**). Thesis reads go to STATUS and CHANGELOG as **separate dated edits**, and weights only move in an edit that changes no spec (R3).
- **Absence is not a result.** Every "missing" cell above resolves to UNRESOLVED, NO-VERDICT or NARROWED, never to benign.
- **No trade content.** The Dec-18 $70P and its guard are TERRY/REGINALD/Will's.
- **Pre-filing probabilities (ledger, unchanged):** WAL-01 25% · WAL-02 50%.

---

## 8. Pre-filing annotations (dated; permitted until the filing lands)

- *2026-09-24: registered. Filing date unknown. Watch EDGAR from ~10/24 and pin it here.*
- *2026-09-24: 10/24 is a **Saturday**, and EDGAR doesn't accept filings on weekends, so the effective earliest filing date is **Mon 10/26**. The L171 deadline of 10/24 is kept as the conservative date; this frame is complete either way.*
- *2026-09-24 ~09:xx ET (REGINALD Cat-IV/AOCI packet, KB-WAL-198): **added cell, non-gating: AFS fair-value hedges + effective duration.** Read the AFS securities note and the derivatives/hedging note for (a) the notional of fair-value hedges on AFS and (b) any stated duration or rate-sensitivity figure. It replaces REGINALD's ASSUMED 3-5 duration with a measured one, and hedged AFS makes the Q3 AOCI hit smaller than his range. Absent ⇒ his range stays labelled ASSUMED. Also record holdco total assets at 9/30 (4Q-average input vs $100B).*
- *2026-09-24 ~10:xx ET (FRAUD-corpus review §2, BROCK's collateral-perfection screen KB-WAL-186): **added cell, non-gating: perfection/servicing review.** Does the Q3 10-Q describe any collateral-perfection, servicing or collateral-agent review, finding or loss **beyond Cantor/LAM** (e.g. mortgage warehouse/MSR, Note Finance, agented SPV facilities such as Crestline, KB-WAL-195)? **Present = informative** (log the book and mechanism). **Absent = uninformative** (10-Q legal notes are blanket, KB-WAL-153). Never grade absence as a clean book.*
- *2026-09-27 (WAL session #8, Nano Banc commission; KB-WAL-201/202): **reader note, NON-GATING, no cell changed.** Nano Banc failed 9/25 (FDIC receiver). Per WAL's own verified complaint, Nano holds 4 senior DOTs ($28.04M original face) ahead of WAL on 5 pleaded collateral loans. **If the Q3 10-Q names a SELLER of any senior-lien purchase, or an FDIC/Nano counterparty, LOG it.** It is informative for state (a)/(b)/(c) in `research/2026-09-27_nano-banc-receivership-stupin-recovery.md` §2. ⛔ It does **not** alter §3's $64M-tie rule (explicit connection only), nor W2 (explicit attribution only). Silence = uninformative.*
