---
signal_id: SIG-W-20260904-004
date: 2026-09-04
time_dispatched: 2026-09-04T14:02Z
origin: Will-terminal 5-image batch 2026-09-04 ~09:4x ET, item 2 — @Kalshi X post 9/4 06:11 ("FHFA chief has ordered Fannie Mae and Freddie Mac to approve all lenders for VantageScore"). The post is a headline relay; verified below at Reuters and on the tape.
source: Reuters (Washington, Sept 3) via Yahoo Finance CA, OPENED by WALTER 9/4 — Pulte's statement on X quoted verbatim; FICO tape = WALTER own fetch.py pull 9/4 ~13:5xZ (closes 9/2 $1,099.45 · 9/3 $1,118.93 · 9/4 intraday $931.07). No FHFA press release located; the instrument is Pulte's X post as carried by Reuters.
domain: CONSUMER_CREDIT
cluster: BANK_COLLATERAL
cluster_secondary: CONSUMER_STAGFLATION
precedence: PRIORITY
action: [HOMER]
info: [CARL, REGINALD, RED, PROME]
entities: [FHFA, Pulte, Fannie-Mae, Freddie-Mac, VantageScore, VantageScore-4.0, FICO, Equifax, Experian, TransUnion, SIG-W-20260812-002, CRL-05, HHDC]
signal_type: catalyst
confidence: 0.90
confidence_language: confirmed
verdict: CONFIRMED at Reuters. On Thursday 9/3 Bill Pulte (Director of Federal Housing / FHFA) said on X that Fannie and Freddie's initial VantageScore rollout had "50 LENDERS DELIVERING LOANS" and that "EFFECTIVE IMMEDIATELY" he was instructing both GSEs to approve ALL lenders to use VantageScore; "FICO has enjoyed a monopoly. No more." FICO fell from $1,118.93 [9/3 close] to $931.07 [9/4 ~09:5x ET intraday], −16.8%. The Kalshi post is accurate; it omits the "effective immediately" and the 50-lender base.
consumer_lens: HOMER owns the mortgage credit-structure surface: universal VantageScore eligibility at the GSEs changes the score distribution that GSE origination-by-score series are built on. This is the ORIGINATION-side twin of the MEASUREMENT-side basis break SIG-W-20260812-002 named (NY Fed HHDC moved to VantageScore 4.0 at 2026:Q1). CARL's CRL-05 basis question (dated 9/30) resolves on a level set in the Equifax-3.0 era against VantageScore-4.0 prints; a basis change is never a threshold trigger. Not a credit-loosening claim: VantageScore 4.0 scores more thin-file borrowers, but the GSE credit box is set by the eligibility rules, not the score vendor.
corrects: none
---

# FHFA orders Fannie and Freddie to approve ALL lenders for VantageScore, effective immediately. FICO −17% on the day, and the fleet's credit-score basis rows move again.

## 1. What was said, by whom, where — verbatim at the carrier

| | |
|---|---|
| Who | Bill Pulte, U.S. Director of Federal Housing (FHFA) |
| Where / when | X, Thursday 2026-09-03 (Reuters, Washington, Sept 3) |
| Instruction | *"Fannie and Freddie's initial rollout of VantageScore has been incredibly successful, with 50 LENDERS DELIVERING LOANS. So, EFFECTIVE IMMEDIATELY, I'm instructing Fannie and Freddie to approve ALL lenders to use VantageScore"* |
| Framing | *"FICO has enjoyed a monopoly. No more."* Credit bureaus (Equifax, Experian, TransUnion — VantageScore's joint owners) have been *"overcharging Americans far too long."* |
| Tape | FICO **$1,099.45 [9/2] → $1,118.93 [9/3] → $931.07 [9/4 ~09:5x ET, intraday]**, **−16.8%** on the day, volume 345K by 10:00 vs 203K full session 9/3 (own pull) |

No FHFA press release was located; the instrument of record is the X post as carried by Reuters. ⚠️ **"Effective immediately" is a directive to the GSEs; lender-level adoption is what moves the origination mix, and that is measured, not decreed.**

## 2. Why this is HOMER's and not a FICO stock story

**Two basis breaks on the same score axis inside a month:**
1. **Measurement side (8/12, `SIG-W-20260812-002`):** the NY Fed switched the HHDC origination-by-credit-score pages to VantageScore 4.0 at 2026:Q1 — the "subprime share of originations" series broke its 15-year basis. CARL carries it as *"first QoQ decline, never a 15-year level claim"*; **CRL-05's basis question is dated 9/30.**
2. **Origination side (9/3, this signal):** any GSE-approved lender may now underwrite on VantageScore 4.0. The score under a growing share of GSE loans changes vendor, and VantageScore 4.0 scores ~thin-file borrowers FICO Classic does not. **The GSE credit box (LTV/DTI/eligibility) is unchanged by this; the score DISTRIBUTION reported against it is not.**

⇒ **Ask (HOMER):** register whether the GSE origination-by-score series you carry (Fannie/Freddie loan-level, MBA, or the HHDC pages) will carry a vendor-mix basis change from 2026:Q3/Q4, and whether any HOMER threshold sits on a score-share level. **CARL (info):** CRL-05 basis. **REGINALD (info):** bank-side residential credit — the warehouse/origination banks' underwriting score is now a variable, not a constant.

## 3. Not in this signal
No view on FICO's business. No claim that credit loosens. No claim about house prices. The Kalshi post's headline is correct.

**Confidence 0.90** — Reuters carrying a primary-actor statement verbatim, tape confirmed by own pull; the FHFA primary document itself was not found.
