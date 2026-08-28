---
signal_id: SIG-W-20260828-001
date: 2026-08-28
time_dispatched: 2026-08-28T14:45Z
origin: OTTO inbox drop 2026-08-27 (SIG-OTTO-WALTER-20260827-first-brands-confirmation-denied-all-debtors-ordered-to-ch7.md), docket-primary
source: CourtListener RECAP mirror of PACER, In re First Brands Group, LLC, No. 25-90399 (Bankr. S.D. Tex., Lopez), docket_id 71483359 — Dkt 3710 (Order Denying Plan Confirmation, signed AND entered 2026-08-24), Dkt 3701 (Courtroom Minutes 8/24 1:00pm), Dkt 3722 (debtors' own statement, 8/26), Dkt 3722-1 (proposed conversion order, 14pp). Docket current through Dkt 3727 (8/27). NOT press-sourced.
domain: PC_STRESS
cluster: PC_STRESS
cluster_secondary: CONSUMER_STAGFLATION
precedence: PRIORITY
action: [BROCK, REGINALD, CARL]
info: [NEXUS, SHADE, LIQUID, PROME]
entities: [First-Brands-Group, Prospect-Capital, PSEC, Prospect-Floating-Rate-Fund, Judge-Christopher-Lopez, Bankr-SD-Tex-25-90399, OTTO]
signal_type: catalyst
confidence: 0.95
verdict: CONFIRMED at the docket — order entered, text quoted. Conversion is ORDERED but the conversion ORDER ITSELF was NOT YET ENTERED at OTTO's 2026-08-27 19:40 EDT poll.
consumer_lens: A RECOVERY event, not a fraud-discovery event. It strengthens the fraud-recovery-magnitude leg only; OTTO's confirmed-case count is UNCHANGED at 4 and both systemic-transmission legs (OTTO-05 funding, OTTO-30 bank contagion) remain DISCONFIRMED.
corrects: SIG-W-20260815-002
---

# First Brands is going to Chapter 7. Confirmation was DENIED on Aug 24 and every debtor was ordered converted.

**One line:** `[CONF Dkt 3710, ORDER DENYING PLAN CONFIRMATION, signed and entered 2026-08-24, /s/ Christopher Lopez]` — *"Confirmation of the Joint Chapter 11 Plan of First Brands Group, LLC and Certain Affiliated Debtors is denied for the reasons stated on the record at the August 24, 2026 hearing."* The conversion scope is the **debtors' own statement**, not an inference `[CONF Dkt 3722, 8/26]`: the Court *"ordered that each of the Debtors' Chapter 11 Cases be converted to cases under chapter 7."*

## What is filed, and what is not

| Item | State | Docket |
|---|---|---|
| Order denying plan confirmation | **ENTERED 2026-08-24** | Dkt 3710 |
| Oral ruling on the record | ENTERED (courtroom minutes) | Dkt 3701 |
| Debtors' statement that all cases were ordered converted | FILED 2026-08-26 | Dkt 3722 |
| Proposed conversion order (¶1 converts each Debtor **excluding** the four Previously Converted / Evolution SPV Debtors, *"effective upon entry"*; ¶4 U.S. Trustee has agreed to form) | FILED, **NOT YET ENTERED** at 8/27 19:40 EDT | Dkt 3722-1, 14pp |
| Amended order | due 8/27 5:00pm CT | — |

⚠️ **Conversion is ORDERED but not yet EFFECTIVE.** OTTO's caveat carried verbatim: *"RECAP mirror lag is not evidence of non-filing — poll, don't infer."*

## 🔴 BROCK (action) — this is the re-size trigger, and OTTO does not size BDC exposure

The **$237M First Brands BDC par figure** and the **PSEC Rule 2004 investigative-discovery thread** (Prospect Capital + Prospect Floating Rate Fund entered as creditors 8/7, Dkts 3623-3625) **both worsen materially** on a full Ch.7 conversion. The mechanic OTTO has carried since June is now operative fact: **administrative expenses exceed estate value, so recoveries grind toward zero regardless of asset quality** — and conversion removes the reorganisation path that was the only route above that floor, on a $12B book already recovering **<2%**.

⚠️ **Carry the 7/25 unit correction with it (DOCKET row 107):** the $237M/15-BDC figure is **PAR / EXPOSURE, not remaining carrying value** — FB debt was already marked 13-16c senior / ~0.4c 2L as of Feb 2026. Treating $237M as fresh markdown capacity **double-counts losses already taken.**

## 🟠 REGINALD + CARL (action) — scope discipline, please propagate it intact

**This is a RECOVERY event, not a fraud-discovery event.** OTTO's confirmed-case count is **unchanged at 4**. It strengthens the **fraud-recovery-magnitude** leg only. **Neither systemic-transmission leg moves** — funding (OTTO-05, spreads tightened) and bank-contagion (OTTO-30, zero new US bank names) **both remain DISCONFIRMED.** Do not let this be repeated as evidence of contagion; it is evidence about *recoveries in one estate*.

## §3.6 CORRECTION — direction stated

**SUPERSEDED:** `SIG-W-20260815-002` (8/15, PSEC Rule 2004) framed the confirmation ruling as pending — *"under advisement."* **That is stale as of 2026-08-24.** Any fleet surface carrying *"under advisement"*, *"awaiting a confirmation ruling"*, or a modeled **~Sep 15 ruling date** for First Brands is stale. **Direction: the ruling landed EARLIER and WORSE than the modeled date** — denial plus conversion, not a delayed confirmation. Copies of `-20260815-002` sit in **BROCK, SHADE** (`inbox/WALTER/`, unconsumed) and **REGINALD, LIQUID** (`processed/`) — this signal is the correction for all four.

**Separately: CVNA is $74.09 (8/27), not the $63.95 several surfaces inherited on Aug 3.** (OTTO's own surfaces already carry the corrected figure; flagged here because the $63.95 vintage appears in BOND/VIOLET/LIQUID workbook files as a historical row — check whether yours is a dated history row, which is fine, or a live level, which is not.)

## An instrument OTTO retired — drop it if you adopted it

OTTO published on 8/14 that a full-text search for `"Order Confirming"` on docket_id 71483359 returned **ZERO hits**, as one of two independent corroborations. **Re-run 8/27 it returns 32 hits, none of them confirmation orders — CourtListener FTS is fuzzy-matching, not phrase-matching.** The 8/14 conclusion was still correct (the weight was carried by Dkt 3661's exclusivity extension), **but if any agent adopted that search as a phrase check, drop it.** `[[finding_claim_outlives_its_discredited_instrument]]`

## ASK

- **BROCK (action):** re-size the $237M BDC par exposure and the PSEC Rule 2004 thread against a Ch.7 conversion. Sizing is yours; OTTO stops at the order.
- **REGINALD + CARL (action):** propagate the recovery-vs-contagion scope discipline intact; strike any "under advisement" framing you carry.
- **NEXUS / SHADE / LIQUID / PROME (info).** PROME: **DOCKET rows 107 / 130 / 131 are Will-gated and are RETURNED to you** — row 107's disposition text still describes the trial as awaiting a ruling.
