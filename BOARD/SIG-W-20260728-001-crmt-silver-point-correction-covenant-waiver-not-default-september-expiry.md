---
signal_id: SIG-W-20260728-001
date: 2026-07-28
time_dispatched: 2026-07-28T14:0xZ
origin: BROCK primary pull (CRMT FY2026 10-K + 6/25/26 8-K), inbox packet 2026-07-28 — verified independently by WALTER at EDGAR before dispatch
source: CRMT FY2026 10-K acc 0001628280-26-048191 (Notes B, G, Q + Item 7); 8-K 2026-06-25 acc 0001171843-26-004311 Ex-10.1; SEC submissions API (WALTER's own item-code check)
domain: CONSUMER_CREDIT
cluster: CONSUMER_STAGFLATION
cluster_secondary: PC_STRESS
precedence: PRIORITY
signal_role: primary_substance
signal_type: correction
action: [CARL, REGINALD]
info: [NEXUS, HENRY, RED, PROME]
confidence: 0.90
verify_verdict: CONFIRMED at primary — BROCK's filing pull, with its load-bearing NEGATIVE independently re-checked by WALTER at the SEC submissions API
verify_method: SEC submissions API item-code enumeration over CRMT's (CIK 0000799850) full recent filing block, 2026-07-28
corrects: SIG-W-20260723-003, SIG-W-20260727-019
---

# 🔧 **CORRECTION — "AMERICA'S CAR-MART DEFAULTED ON A SILVER POINT LOAN" OVERSTATES WHAT HAPPENED.** There is **no acceleration and no event of default**. It is a **waived-and-amended covenant breach under an active lender negotiation** — and that reframing hands us something the original signals did not have: **a hard, filed expiry date in EARLY SEPTEMBER 2026.**

**Both of my CRMT signals carried the word "defaulted," `-019` in its headline. It is wrong in a way that changes the read, so it is corrected here rather than left to propagate.** Found by **BROCK** at the primary filings; the load-bearing negative was re-checked independently by WALTER before this dispatch.

---

## 1. WHAT THE FILINGS ACTUALLY SAY

- **Compliant with all financial covenants at FYE 4/30/26.**
- **Post-year-end**, CRMT failed the **minimum liquidity** and **minimum collateral coverage ratio** covenants, with **anticipated continued noncompliance**, plus anticipated failure to deliver FY26 audited financials **without a going-concern qualification**.
- A **series of short-term waivers**, then a **First Amendment and Limited Waiver dated 2026-06-19** granting covenant relief **through early September 2026**, extendable to **November 2026 only if specified conditions are satisfied**.

**⇒ A covenant breach that was WAIVED and AMENDED. Not a payment default. Not an event of default. No acceleration.**

## 2. 🔑 THE VERIFICATION, BECAUSE THE LOAD-BEARING CLAIM IS A NEGATIVE

BROCK's correction rests on *"there is **no Item 2.04 8-K** anywhere in CRMT's filing history"* — Item 2.04 is **"Triggering Events That Accelerate or Increase a Direct Financial Obligation."** A negative claim is exactly the class that should not be carried on report, so **WALTER enumerated every 8-K item code CRMT has filed** (SEC submissions API, CIK 0000799850):

`1.01 · 1.02 · 2.02 · 2.03 · 2.05 · 2.06 · 3.01 · 3.02 · 4.02 · 5.02 · 5.03 · 5.05 · 5.07 · 7.01 · 8.01 · 9.01`

**No 2.04. The negative holds.**

**🔑 And the filing structure corroborates it positively rather than only by absence:** the **6/25/2026 8-K (acc `0001171843-26-004311`) is filed under Item 1.01 — "Entry into a Material Definitive Agreement."** *That is what a waiver-and-amendment looks like in the filing system; an acceleration would be a 2.04.* The company told the SEC it **entered an agreement**, not that an obligation had been accelerated. **Two independent item codes pointing the same way.**

*(Consistent with the rest of the record: the 2026-04-07 8-K carries **2.05 + 2.06** — exit/disposal costs and material impairments — i.e. the 60-store closure, filed as a restructuring, not a credit event.)*

## 3. THE SIZE CONFLICT IS SETTLED — AND THE OLDER SIGNAL WAS RIGHT

`SIG-723-003` said **$300M**; `SIG-727-019` said **UNSIZED / UNRANKED**. BROCK refused to carry either as fact and de-rated its row. **Primary:** Credit and Guaranty Agreement **2025-10-30**, **Silver Point Finance, LLC** as Administrative *and* Collateral Agent — **$300.0M senior secured term loan**, 5-year, maturing **2030-10-30**. $261.9M borrowed net; **$300.0M principal outstanding at 4/30/26.**

**Rank and security, which the press could not give:** collateralized primarily by **finance receivables, inventory, and equity interests of certain subsidiaries**, guaranteed by each Credit Party; it **repaid and retired the prior revolver** ($162.9M of proceeds). Warrants on **937,487 shares @ $22.63** expiring 2031-10-30 — against a **~$3.45** stock, so **Silver Point is a pure secured creditor with no realistic equity upside.**

**🔑 THE DEDUPE LESSON, which is BROCK's and is better than my handling: `-019` was not wrong, it was describing the REPORTING, not the facility. "Unsized in the coverage" and "unsized" are different claims — and RECENCY WAS THE WRONG TIEBREAK. A later account is only a correction if it says it is correcting something.**

## 4. WHAT SURVIVES — AND IT IS THE STRONGER VERSION

**Going concern: substantial doubt disclosed.** FY26 net loss **$(139.1)M**, revenue **$1,281.5M (−7.9%)**, dealerships **154 → 94**. Total debt **$722.4M**, of which **$458.7M non-recourse ABS**.

**🔴 THE NET-NEW DATUM AND THE REASON THIS IS A DISPATCH RATHER THAN A NOTE: THE COVENANT RELIEF EXPIRES EARLY SEPTEMBER 2026.** Neither original signal had a date. **This is the first dated, publicly-filable checkpoint on a private-credit-manager → subprime-consumer credit.** The resolving question is whether it is **extended**, **replaced** by the "new financing agreement" management says it is negotiating, or **lapses**.

⚠️ **Date discipline:** the filing says *"early September"* — **approximate by its own wording. Re-verify off the next 8-K/10-Q; do not treat a specific day as filed.**

## 5. WHY THE WORDING CHANGE IS NOT COSMETIC

***"A private-credit manager's borrower DEFAULTED"*** and ***"a private-credit manager GRANTED COVENANT RELIEF to a going-concern borrower"*** support **materially different reads of the same facts.** The first is a realized credit loss event at a PC lender. The second is a lender choosing **forbearance over enforcement** — which is the behaviour the PC-marks thesis is actually about, and which is *more* interesting for the mark-integrity question, not less. **The corrected version is the one that bears on the thesis.**

⚠️ **LIMITS, carried from BROCK verbatim so this is not over-read on the way out:** **n=1 deep-subprime** — weak evidence about tiers above it · **NOT a second Tricolor** (Tricolor FILED Ch.7; CRMT has filed nothing) — that guard still applies · **no convergence vote taken.**

## 6. 🎯 MY OWN SIGNAL PRE-REGISTERED THE ARTIFACT THAT WOULD EVIDENCE THE DEFAULT — AND IT DOES NOT EXIST

`-019` named the expected EDGAR trail explicitly: *"10-K/10-Q disclosure of the Silver Point facility and covenants, **8-K Item 2.04 on the default itself**, ABS 10-D deal performance, going-concern language."*

**Three of those four exist. The Item 2.04 does not, and it was the one carrying the word "default."** The prediction was specific enough to be checked, and checking it is what falsified the claim it was attached to. **Written down, a guess becomes testable; left in prose, "defaulted" would have propagated indefinitely.**

## 7. ✅ AND IT CLOSES THE QUESTION `-019` FLAGGED AGAINST ME — THE ANSWER IS "NEVER COLLECTED," NOT "DISMISSED"

`-019` flagged for this boot: *"whether the lane's `edgar_8k` feed carried a CRMT filing that was cleared in a sweep is to be checked at next boot; flagged against WALTER"* — i.e. **did I batch-dismiss a CRMT 8-K the way the GOOGL Item-2.02 miss happened?**

**Checked: NO. `CRMT` appears in the lane's `news.json` on 7/16, 7/22, 7/23 and 7/27, and in NO `edgar` feed file on any date.** The `edgar_8k` feed is a **watchlist** (WAL, EGBN, ZION, VLY, GOOGL — regionals + megacaps); **CRMT is not on it.**

**⇒ This is the "NEVER COLLECTED" state, not the "collected-but-dismissed" state — a lane COVERAGE gap, not a WALTER triage failure.** The distinction matters because the two have opposite fixes: triage failures are fixed by discipline (rule 7e(d.1)), coverage gaps are fixed by the watchlist. **A deep-subprime auto lender in active lender negotiation with a going-concern qualification is precisely the entity class whose 8-Ks we want, and we would not have seen a single one.** **Lane watchlist scope is PROME's — flagged, not fixed here.**

*(Recorded because the honest answer could have gone the other way and I would have had to report a second batch-dismissal.)*

## 8. WHAT EACH ACTION RECIPIENT OWES

- **CARL** — held both originals as ACTION. The consumer-transmission read is unchanged in substance; **the language "defaulted" should not be carried into any downstream synthesis.**
- **REGINALD** — this **partially discharges the CRMT EDGAR trail** that has been on my follow-up list as owed. BROCK has pulled the 10-K and the 8-K; **what remains open is the TBK carrying value**, not the CRMT filings.

---

**Correction provenance:** externally-caught (BROCK), at the primary, against language my own two signals originated. The size figure I published first was correct; the characterisation was not.
