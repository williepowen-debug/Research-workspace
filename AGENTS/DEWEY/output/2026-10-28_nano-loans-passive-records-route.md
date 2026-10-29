# Nano Banc: is there a passive public-record route to which named loans Sunwest took?
**Date:** 2026-10-28 (22:37–22:42 ET) | **Mode:** Cold | **Request:** REGINALD ASK, `inbox/2026-10-28_from-REGINALD_FHA-kill-pointer-and-Nano-records-route.md` (DOCKET L516 context; no external inquiry; no deadline) | **Confidence:** High on what each route can and cannot reach tonight; no new loan-level transfer evidence found.

## Key finding
**No passive route that an automated desk session can complete exists tonight.** Two routes remain open to a person working in a browser, and one named-loan datum is already on file:
1. **Already on file, the Ontario lien.** The FDIC as receiver for Nano Banc filed in *Plaza Continental* (C.D. Cal. Bankr. 8:26-bk-10986, Doc 100, filed 10/2/2026), asserting succession to Nano's creditor status on that loan. That is evidence the Ontario deed of trust stayed with the receiver rather than passing to Sunwest **as of 10/2** [PRIMARY, read by WAL 10/14, `AGENTS/WAL/research/2026-10-14_Ontario-FDIC-docket-followup.md`]. It does not establish ownership after 10/2.
2. **Open to a person:** the San Bernardino and Riverside recorder indexes (document type, date, grantor, grantee). Section 1 gives the exact searches.
3. **Closed tonight:** court-record text search (CourtListener now requires an account token), PACER (paid), Los Angeles County recorder (no online index), and the FDIC P&A agreement (still not posted).

## 1. Routes tested, 2026-10-29 02:34–02:41 UTC
| Route | What it could show | Result tonight |
|---|---|---|
| FDIC failed-bank page | The executed P&A and its schedules | **Not posted.** HTTP 200; only the creditor notice and bid summary are linked; "Last Updated: October 19, 2026" |
| CourtListener / RECAP search API (DEWEY `recap_pull.py`) | FDIC-R or Sunwest filings, Rule 3001(e) transfers of claim and proofs of claim in the borrowers' Chapter 11 cases | **HTTP 401 "Authentication credentials were not provided"**, including the exact docket-scoped query form that worked anonymously on 10/25. CourtListener docket web pages return 403 to scripted requests. The helper's cache holds no Nano-docket searches |
| PACER | Same filings and the claims registers | Paid access: outside DEWEY's authority |
| **San Bernardino County recorder index** (Ontario, Chino) | A recorded **Assignment of Deed of Trust** from Nano Banc or the FDIC to Sunwest | Public index (Tyler Self-Service, arcselfservice.sbcounty.gov); index only, no images. **Gated by Google reCAPTCHA**, so not automated (DEWEY does not defeat human checks). **A person can run it** |
| **Riverside County recorder index** (Moreno Valley) | Same | Public name search with no human check (webselfservice.rivcoacr.org, "Name Search - Web": party name and recording-date range). DEWEY's scripted submissions returned server error 500 four times (three searches plus one retry with corrected dates), most likely a form-state detail. **A person can run it** |
| Los Angeles County recorder (Bellflower) | Same | "Our office does not provide online access to real estate records or indexes" (lavote.gov). **In person or by mail only** |
| California UCC search | UCC-3 assignment of Nano's security interests | Not tested. Relevant only to loans secured by **pledged LLC membership interests** (the $20M Nano Loan, DEWEY 9/27 §4). Real-property deeds of trust are not UCC filings |
| Sunwest Q3 2026 Call Report (FFIEC CDR, due ~10/30) | Loan-category jumps at acquisition | **Category totals only, never named loans.** Useful for REGINALD's size check, not for O1 |

## 2. The manual searches, if anyone runs them
- **San Bernardino** (Ontario 3700 Inland Empire Blvd; Chino 12233 Central Ave) and **Riverside** (Moreno Valley 23750 Alessandro Blvd).
- **Name search, recording dates 9/25/2026 to today**, three runs: grantor "NANO BANC"; grantor "FEDERAL DEPOSIT INSURANCE"; grantee "SUNWEST BANK".
- **Document types to look for:** assignment of deed of trust; substitution of trustee; reconveyance.
- **Match on the instrument number or APN, not the street address** (DEWEY 9/27 §4x).
- **What a blank result means:** absence of an assignment is weak evidence of retention, because assignments of deeds of trust are often recorded late or never.
- **This is a human browser task, not a desk task.**

## Counter-evidence
- The Ontario datum is one loan at one date. The FDIC could have sold or assigned it after 10/2. The bid summary shows Sunwest bought Pools B and C and **not** A and D. Which pool held which named loan is exactly what is unpublished.
- A recorded assignment would be decisive. A missing one would not prove retention.

## Source quality and process report
- **Sources:**
  - Primary: the FDIC page (fetched directly); the San Bernardino ARC and Riverside ACR self-service pages; the LA RR/CC records page; WAL's 10/14 read of Doc 100.
  - Searches: three WebSearch calls (one found deal coverage only, with conflicting loan figures: "$227M loans" vs "$476M assets").
- **Frustrations:**
  - **New wall: CourtListener anonymous search now returns 401.** That breaks `recap_pull.py search` for every desk. Logged to BACKLOG.
  - A free CourtListener account token (`COURTLISTENER_TOKEN`, already supported by the helper) would restore it. Creating an account is Will's call.
- **Not done, by scope:** no FDIC inquiry, no paid access, no human-check bypass, no new collector.
