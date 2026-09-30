# CREED FLOW NOTES — the full prior text of `workbook/FLOW.tsv` rows (rotation 2026-09-29)

**What this is:** CATO's workbook review (CW1, `AGENTS/CATO/runs/2026-09-29_2310_creed-workbook-review.md`) found the chain map's "Current" cells carrying stale claims inside long correction narratives. On 2026-09-29 rows 01/02/05/06/07/08 were rewritten as concise current states from evidence already on file, and their full prior `Current` + `Key_Insight` cells were moved here VERBATIM (crc32 over col 7 + newline + col 8).
**How to read:** on demand, `grep -n -A3 '^## FLOW-CREED-0x' AGENTS/CREED/notes/FLOW_NOTES.md`. Not a boot read. **These are HISTORY: do not cite a figure from here as current.**

## FLOW-CREED-01 — CRE Doom Loop
*moved verbatim 2026-09-29, crc32 `ee5e92e0` (col 7 + newline + col 8)*

**Current (col 7) as of the rotation:**

*** TRIGGER ID: CREED-T-03 (bank leg) + CREED-T-01a (CMBS leg) -- carried on the row so an ID-keyed guard can see it. *** 🔴 REFRESHED 2026-09-02, AND THIS CELL WAS CARRYING TWO IMPEACHED CLAIMS FOR 13 DAYS. *** WHAT WAS WRONG: *** it read "bank non-owner CRE PDNA 3.40% and STILL IMPROVING (6th qtr)". BOTH halves were impeached by KB-CREED-024 on 2026-08-27 and this row never got the correction: (a) the 3.40% cannot be reproduced from the FDIC QBP it cites -- the >$250B nonfarm-nonresidential cell reads 2.73% for Q1-2026, 67bp apart, and the non-owner-occupied-only series is ABSENT from the QBP in all four retrieval shapes across TWO consecutive editions (n=2, KB-CREED-026); (b) the "6th straight improvement" is FALSE on the declared basis -- Q3-25 3.20 -> Q4-25 3.23 is a RISE. VX-CREED-4.01 carries an explicit DO-NOT-WRITE-A-LONGER-STREAK-HERE warning about this exact sentence, and this row wrote it anyway. *** CURRENT, ON THE DECLARED BASIS (QBP Table V-A, row 'Nonfarm nonresidential' COMBINED, column 'Greater Than $250 Billion', PRIMARY-READ): 2.48% [Q2-2026], the 2nd consecutive QoQ decline on this basis. WQ-92 ruled 2026-09-01; branch (b), a dated declared re-anchor, recorded on VX-4.01. NO BAND MOVED. *** CMBS legs, August 2026 print (pub 2026-09-01, PRIMARY-READ at publisher): office DQ 12.00% (+9bp) -- CREED-T-01a NOT FIRED, '12.00' is not '> 12', 0 of 2 legs. Office SS: NO AUGUST PRINT (report not published; due ~Sept 8-10), so SS stays 16.58% [Jul] and the SS-DQ SPREAD IS UNCOMPUTABLE FOR AUGUST -- do not carry a spread figure this month. *** THE BANK LEG REMAINS COUNTER-DIRECTION and that verdict never depended on the 3.40: CREED-T-03 was graded NOT FIRED on leg (c) reserve coverage (166.8 -> 172.7%, IMPROVED), which is basis-INDEPENDENT. The impeached number was decorative to the verdict and load-bearing to the reader. ***

**Key_Insight (col 8) as of the rotation:**

Vacancy -> value decline -> LTV breach -> modification -> re-default -> recognition -> provisions. STILL SELECTIVE, PRE-CASCADE: the CMBS legs are elevated and the bank leg has not turned. The chain is loaded at the front and blocked at the back.

## FLOW-CREED-02 — Maturity Wall Cascade
*moved verbatim 2026-09-29, crc32 `629f56f2` (col 7 + newline + col 8)*

**Current (col 7) as of the rotation:**

*** TRIGGER ID: CREED-T-02 -- carried on the row so an ID-keyed guard can see it (deferred item 16). *** *** TRIGGER CONDITION MET -- this chain's stated trigger (field 6) is verbatim CREED-T-02 and it FIRED 2026-08-20, effective the JUNE print. SPENT: a fired binary trigger says nothing further. *** Matured-balloon share of newly delinquent balances: Apr 42% / May 70% / Jun 65% <-sustain met / Jul 66%, PRIMARY-READ off four Trepp PDFs. DERIVED matured-balloon dollars Apr $1.10B / May $2.83B / Jun $1.72B / Jul $3.96B -- JULY IS THE DOLLAR PEAK (+40% vs May, +131% vs Jun): the SHARE plateaued, the QUANTITY did not. 🔴 *** AUGUST 2026 ADDS NO POINT TO EITHER SERIES -- UNRETRIEVED, NOT UNPUBLISHED. *** Trepp's free August excerpt names the five largest newly delinquent loans and prints NO DOLLAR AT ALL (July's gave '$2.6B of the $6.0B'); the composition split lives in the subscriber-gated full report, which is not archived for August. Four shapes checked (WALTER's PDF archive / the free excerpt / the gated report / secondary relays, MHN + commercialsearch both Cloudflare-403). Source request packeted to WALTER 2026-09-02. ⛔ NO SHAPE WORD IS WRITTEN IN EITHER DIRECTION: no denominator was published, so trap #11 forbids one. 🔴 *** WHAT AUGUST DOES SAY ABOUT THIS CHAIN, and it is a NEGATIVE that matters: *** Trepp verbatim -- 'Several large loans became delinquent after failing to pay off at maturity, but their impact was offset by cures, including a large Times Square loan that returned to performing status.' The headline fell 1bp to 7.85% while FOUR OF FIVE property types ROSE. THE MATURITY-DEFAULT FLOW DID NOT STOP; IT WAS MATCHED BY ONE TROPHY-ASSET CURE. A net figure concealing two large offsetting gross flows is not a level reading, and the gross flows are exactly what was not printed. Maturity-adjusted DQ stays 9.62% [Trepp Jul] = multi-year high; NOT refreshed for August (same gated channel). $76.6B CMBS hard maturities, 39% in Q4, 36% at debt yield <=8%.

**Key_Insight (col 8) as of the rotation:**

Maturities force refinance at repriced values; failed refi forces appraisals and NAV marks. THE CLEANEST 2026 FORCING FUNCTION — calendar-driven, borrowers cannot defer it. Q4 back-loading is the timing rail. NEW 7/27: lender capital withdrawal (FLOW-07) removes refi capacity on the other side of this wall. *** FIRED 8/20: the forcing function is no longer prospective -- refi failure at maturity is now the MAJORITY of new CMBS delinquency, three prints running. ⚠️ FOUND BY THE CLOSEOUT SELF consumer_check, NOT by the fire adjudication: this row carried CREED-T-02's condition verbatim in its own trigger field while sitting ARMED. THIRD surface holding one condition (registry row + VX vector + this chain) -- the SAME class of defect K5 exposed, caught the same session by a different instrument.

## FLOW-CREED-05 — Extend-and-Pretend Collapse
*moved verbatim 2026-09-29, crc32 `38a0c4d8` (col 7 + newline + col 8)*

**Current (col 7) as of the rotation:**

STILL ABSORBING at the aggregate (June headline decline was lodging cures + mods; servicers unwilling to seize). FAILING at asset level: Aon + Seattle recaps failed; Sangertown refused a 3rd extension on a DSCR hurdle after rolling twice.

**Key_Insight (col 8) as of the rotation:**

1st mod -> expire -> 2nd mod -> exhaust -> forced recognition -> charge-off. *** THE SS-minus-DQ SPREAD (VX 2.03, 5.54pp) IS THE GAUGE: wide = extensions still working; collapsing = either genuine cures or delinquency catching up. *** Sangertown is the cleanest specimen of this chain ENDING ON SCHEDULE for one credit.

## FLOW-CREED-06 — Lease Expiration / Vacancy Ratchet
*moved verbatim 2026-09-29, crc32 `b95a4911` (col 7 + newline + col 8)*

**Current (col 7) as of the rotation:**

US office vacancy ~21.0% [Moody's Q1-26, record] — BUT provider spread is ~2.4pp (CBRE 18.6% same quarter). Life science BIFURCATED: worst markets healing, Boston/SF worsening on NEW SUPPLY not tenant loss.

**Key_Insight (col 8) as of the rotation:**

Leases expire -> tenants downsize -> vacancy ratchets -> rent decline -> NOI -> DSCR breach -> feeds the maturity wall. *** NEW 7/27 CONSTRAINT: the office->residential CONVERSION EXIT, which puts an unexamined floor under obsolete office, is being attacked at the pro-forma level (Seattle: "not worth even looking at"). PHYSICAL constraints travel; FEE constraints are metro-specific — several metros SUBSIDISE conversion. ***

## FLOW-CREED-07 — CRE Lender Capital Withdrawal
*moved verbatim 2026-09-29, crc32 `87fa9ce9` (col 7 + newline + col 8)*

**Current (col 7) as of the rotation:**

1 named exit (ARI: ~$9B book sold to Athene, board resolved to dissolve) + 1 named credit-loss cutter (KREF: -60% dividend, $148.6M 6-mo provision). 8 of 11 cohort dividends HELD.

**Key_Insight (col 8) as of the rotation:**

*** NEW CHAIN 7/27. *** Public CRE lenders conclude the business no longer earns its cost of capital -> return capital / shrink books -> refi capacity contracts -> the maturity wall (FLOW-02) has fewer lenders on the other side. *** CRITICAL: separate lender-ECONOMICS exits (ARI, book cleared at par) from CREDIT-LOSS shrinkage (KREF, risk-5 write-offs). Fusing them produces "CRE lenders are blowing up," which is wrong about both. *** Currently a CHANNEL-COMPOSITION story much more than a funding-closure story.

## FLOW-CREED-08 — Fast-to-Slow Holder Migration
*moved verbatim 2026-09-29, crc32 `ee8f27be` (col 7 + newline + col 8)*

**Current (col 7) as of the rotation:**

~$9B ARI -> Athene at 99.7% (closed 4/24/26, 8-K disclosed, stockholder-voted). Aggregate: life-insurer CM/MF holdings $775B, +$3.3B Q1 [MBA, rel. 6/18].

**Key_Insight (col 8) as of the rotation:**

*** THE THESIS-CRITICAL CHAIN. Recognition speed is a property of the HOLDER, not the wrapper. *** !! DEMOTED TO REAL-BUT-UNESTABLISHED 2026-07-27 EVE, on TWO INDEPENDENT grounds, both surfaced by SHADE and both accepted: (1) ONE QUARTER -- Q4-2025 CMBS/CDO/ABS was +$3.6B POSITIVE and flipped to -$9.6B only in Q1-2026, the SAME quarter the life-insurer line decelerated from +$11.5B to +$3.3B. Both series were positive the quarter before. This is a SAMPLE-SIZE defect with a known remedy (more quarters). (2) LEGAL FORM -- MBA attributes to the NOTE-HOLDER, so the two buckets are "note held by an insurer" vs "note held by a trust", NOT "insurance channel vs securitized channel". AN INSURER BUYING A CMBS BOND PRINTS AS CMBS, so part of the -$9.6B "shedding" may ITSELF be insurer-held and the divergence may be an ARTIFACT OF INSTRUMENT LEGAL FORM rather than migration between holder types. This is an IDENTIFICATION defect with NO remedy from this series. CREED had offered "two consecutive quarters in opposite directions is the confirmation" -- that fixes (1) ONLY. Resolution of (2) needs a source splitting CMBS holdings BY HOLDER TYPE, which MBA does not publish. DO NOT CARRY AS ESTABLISHED MECHANISM. !! CRE credit migrates from publicly-marked quarterly-reporting holders (CMBS, mortgage REITs) to slow-recognition balance sheets (insurers, banks). CONSEQUENCE: headline CMBS/mREIT/SS metrics measure only the FAST channel — every dollar that migrates leaves the measured population WITHOUT being resolved, so aggregate stress metrics understate system risk BY CONSTRUCTION. *** The discriminator is DISCLOSURE QUALITY + PRICE DISCOVERY, not affiliation: ARI->Athene is affiliate-but-observable; the Delaware Life class is affiliate-and-undisclosed. Do not weld them. ***
