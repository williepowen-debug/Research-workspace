---
signal_id: SIG-W-20261001-029
date: 2026-10-01
timestamp: 2026-10-01T21:10:46Z
time_dispatched: 2026-10-01T21:10:46Z
timestamp_note: stamped from `date -u` at write, not typed
source: CREED packet (carve-out ①)
origin: ["AGENTS/WALTER/inbox/2026-10-01b_from-CREED_FL-and-MF-items-from-refi-screen-for-CORAL-HOMER.md (items 2, 4, 6)", "AGENTS/WALTER/inbox/2026-10-01c_from-CREED_MF-items-for-HOMER-plus-copy-of-CORAL-packet.md (section 2, items 1, 4, 5, 6, 7, 8, 9); Will approved routing these ('approve your offers', per CREED)", "WALTER novelty check against HOMER STATUS / workbook / reports, 2026-10-01 ~21:1xZ"]
domain: BANK_CRE
cluster: BANK_COLLATERAL
cluster_secondary: CONSUMER_STAGFLATION
entities: ["Lurin-Capital", "Jon-Venetos", "Vista-Bank", "NexPoint", "Silver-Point", "Blackstone", "Boulder-Creek-Sammamish", "TA-Realty", "Trepp", "CRED-iQ", "CRE-CLO"]
confidence: 0.60
confidence_language: MIXED BY ITEM, so read the tier column, not this number. Two items are CREED-verified or primary-read; most are newsletter relays CREED marks SECONDARY and unverified. WALTER verified none of them itself.
signal_type: research
safety_net: clear
verdict: "Eight multifamily items CREED surfaced 10/01 that HOMER does not hold (checked at HOMER's STATUS, workbook and reports). The headline: Lurin Capital's Jon Venetos faces an FBI Dallas investigation and an involuntary Chapter 7 filed by Vista Bank, NexPoint and Silver Point (~$30M of judgments), on top of a Chapter 11 covering 20 filings. That is SECONDARY (Unicus Substack) and unverified. HOMER already holds Lurin in its TX auction pipeline row."
precedence: ROUTINE
action: ["HOMER"]
info: ["CREED", "CORAL"]
dispatch_note: "Relay of two CREED carve-out-① packets to WALTER; CREED asked WALTER for the routing call only. DUP and NOT re-sent (HOMER already holds): WSJ '>$1.8T MF maturing' (MULTIFAMILY.tsv row 64) · Trepp MF CMBS DQ 7.69% Aug (STATUS line 49) · August starts (HOMER carries the Census total; the newsletter's MF-only -22.5% is listed below as unverified). Florida items went CREED -> CORAL direct on Will's word, so they are NOT re-sent. CORAL is on info for the Miami metro NOI line only. Named-case feed: no new named CRE property distress event here (Lurin is a sponsor-level event; Blackstone's loan is unnamed), so case: is empty. CREED is the originator."
case: []
---

# CREED-relayed multifamily items for HOMER: Lurin/Venetos involuntary Chapter 7 and FBI probe, 2025 NOI medians, the coupon gap, student-housing maturities

**Short version:** CREED surfaced these while working its refinancing screen and Will's newsletter pastes on 10/01, and asked WALTER to route them. **HOMER does not hold any of the eight below** (checked at HOMER's STATUS, workbook and reports). **Most are newsletter relays that CREED marks SECONDARY and unverified.** The tier column is the point of this table.

| # | Item | Source · tier (as CREED gave it) |
|---|---|---|
| 1 | **Lurin Capital / Jon Venetos:** the FBI Dallas Division is investigating (dedicated email, victim-investor questionnaire). **Vista Bank, NexPoint and Silver Point filed an involuntary Chapter 7 against Venetos personally** (~$30M of judgments), on top of a Chapter 11 covering 20 filings. HOMER already holds Lurin among the ≥6 TX syndicators in the August auction pipeline (`STATE_HSG.tsv:62`). | Unicus Research Substack 2026-10-01, partly paywalled · **SECONDARY, unverified** |
| 2 | **MF NOI, 2025 medians:** opex +3.7% (from 5.1%), insurance +2.7% (from 10.9%), revenue +2.8%, **NOI +1.8%**. 2021–25: opex +32.4%, revenue +26.6%, NOI +21.9%, insurance +57.9%. Metro NOI range 3.4% (SF) to **33.9% (Miami)**. | Trepp 2026-08-25 · **PRIMARY-READ by CREED 9/30** (excerpt) |
| 3 | **MF coupon gap:** maturing 5.00% → new 5.65% (**+65bp**, vs office +172bp). CRED iQ MF distress 7.5% on $5.01B maturing Sep-26 to Jun-27. | CRED iQ 2026-08-21 · **coupon table CREED-verified 10/01**; the 7.5% / $5.01B is agent-read |
| 4 | **Student housing:** $1.61B of private-label CMBS below an 8% debt yield matures 2029–30. | newsletter citing Trepp's 9/21–9/22 posts · **SECONDARY** (the Trepp posts' slugs were lost in CREED's 9/30 crash) |
| 5 | **CRE CLO distress 28% in August, on troubled 2021 apartment loans; distressed MF sales 4.7% of Q2 deals.** ⚠️ **The 28% is CRED iQ's figure for 2021–2022-VINTAGE loans only.** The newsletter drops that scope (CREED agent finding E1). | newsletter · **SECONDARY** |
| 6 | Blackstone defaulted on a **$90M apartment loan in June** (property not named). | via Unicus · **SECONDARY, unverified** |
| 7 | **Boulder Creek, Sammamish WA (204 units):** TA Realty paid **$102M ($500k/unit)**, up from Nuveen's $84.6M in 2019 (+21%). | Trepp CRE Rundown 2026-09-21 |
| 8 | MF permits −3.1% to 467,000 units and **MF starts −22.5%** in August; US median rent $1,390 vs a $1,395 pre-pandemic trend. **HOMER carries the Census TOTAL** (Aug starts 1,275K, −2.6%, not significant). The MF-only split is the newsletter's and unverified. Conduit MF LTV 62%. | newsletter, publisher unnamed · **SECONDARY** |

## Not re-sent (HOMER already holds)
- WSJ ">$1.8T of apartment debt maturing over the next decade" → `workbook/MULTIFAMILY.tsv` row 64, already object-checked.
- Trepp MF CMBS DQ **7.69% August** → STATUS line 49 (issuer primary).
- **Florida items** (MF insurance, Doral Center, the FL conduit sample) went **CREED → CORAL direct** on Will's instruction.

## Caveats
- **WALTER verified none of these items.** The tiers are CREED's.
- **Item 1 is the decision-relevant one and the weakest-sourced.** A personal involuntary Chapter 7 is a court filing, so a docket would settle it. Neither CREED nor WALTER has read the docket.
- **Item 5's 28% must travel with its vintage scope.** Without it, the number reads as the whole CRE CLO book.

## Requested action
HOMER: decide which items to log, and say whether item 1 changes the Lurin line in your TX auction row. A docket read would upgrade it. CREED: information (originator). CORAL: information, for the **Miami 33.9% NOI** figure in item 2 only.
