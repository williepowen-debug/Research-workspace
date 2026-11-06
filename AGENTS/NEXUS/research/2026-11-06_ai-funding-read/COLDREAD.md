# Cold read ledger: READ.md (5,995 B), companions RECORD.md, GRADES.json. Read-only.
| # | Claim (READ.md line) | Grade | Reason |
|---|---|---|---|
| 1 | L5 "Microsoft let an old Oracle contract lapse" (stated as fact) | caution | RECORD L31: "Bloomberg 11/6 via Investing.com and Reuters; body unread by any desk"; "Reported". Next clause says "reportedly" |
| 2 | L5 "the reports cannot explain the jump" (all reports) | caution | RECORD L37: ING sale, BoE questions, bond table "Dated 11/5 ... Same day; causal share unknown". READ L21 excludes only MSFT/OpenAI/ECB |
| 3 | L5/L21 sequence: HY widened 11/5, reports dated 11/6 | caution | Date logic holds for those three. RECORD L32 stamps Reuters "18:46 11/6" yet pulls were 15:27-15:31 ET on 11/6; timezone unstated. Cell is 11/5 close, report times not given |
| 4 | Omitted same-day 11/5 candidates | caution | IREN -16.95% on 11/5 (RECORD L69) and ING/BoE 11/5 are not named in READ's sequence test |
| 5 | L11 HY 348, BB 213 (+14), 2026 high | ok | RECORD L35, L51; GRADES Guards 348; "prior 346, March 30" |
| 6 | L11 Oracle 5Y CDS 305 [11/5, DTCC] | ok | RECORD L51: 292 then 305 |
| 7 | L12 $730.0M / $282.3M / 99.15 [9/30] | ok | RECORD L53. "99.15 of commitment" unit slightly terse |
| 8 | L12 "other 40% of the loans" | caution | 40% appears in RECORD L53 without derivation (730M vs ~1.2B loans) |
| 9 | L13 "All $20B of its pledged public raise through FY30 closed by 11/4" | error-candidate/caution | RECORD L55 names TWO $20B items: a pledge cap FY27-FY30 "on top of" a $20B ATM raise; "both $10B halves closed 11/4". READ conflates; if the cap is exhausted the "levers left" framing changes |
| 10 | L13 "$116 offer", "10-Q about 12/15" | caution | Neither figure/date is in RECORD; unverifiable |
| 11 | L14 ING about $500M of 12 loans; ECB 11/18; ING bids 11/19 | caution | Not in RECORD (cites cards 004/031 only) |
| 12 | L14 "no desk has a figure" | caution | RECORD L57: scope = grep of this repo's STATUS/briefs + 5 workbooks, "not public filings". READ headline L5 and L14 drop that scope; RECORD L77 says it is "scoped in Route 4" but READ never carries it. Adjacent figures exist (HANS EUR4bn/EUR62.5bn private credit, GIBBS, SLOOS, BROCK fund finance) |
| 13 | L15 SAM 21.5% (20-24%) vs 25% ceiling, not 13% | ok | RECORD L40, L59. Estimate flagged |
| 14 | L15/L31 leverage basis | caution | RECORD L59: 11/10 headline "as of 9/30, SAM cases 13.7-16.5%" vs 21.5% now: gap unexplained on READ |
| 15 | L16 Goldman -6.36%, MS -5.94% [11/5] | caution | Not in RECORD; RECORD L61 gives only 11/6 GS +0.06%, MS -0.01% |
| 16 | L15 megabanks fell [11/6] | caution | RECORD L59 MUFG -6.52% etc. dated [11/6] but time/close unstated while vendor reads were intraday 15:31 |
| 17 | L17 Athene 15% | ok | RECORD L63; omits 35% reimbursement and "base unknown" is stated |
| 18 | L22 "hinge is tenant credit, not AI demand" | caution | Inference stated as fact. RECORD L53: Microsoft's change at Childress, Mackenzie loan in BC, link "through the parent guarantee only"; 9.0% facility is the non-Microsoft-backed one |
| 19 | L22 IREN 5.96% vs 9.0-9.51% | caution | Only 9.0% appears in RECORD; 5.96, 9.51 unsourced. "(unlike facilities)" opaque |
| 20 | L22 "No source names either in the review" | caution | "either" and "the review" undefined |
| 21 | L23 Oracle levers lean on labs/chip sellers | ok | Labelled "my inference" |
| 22 | L24 OCIC paid redemptions in notes; Blue Owl on IREN, Nscale, CoreWeave | caution | Not in RECORD (CoreWeave line absent) |
| 23 | L25 OpenAI at $1.25T cuts SoftBank leverage ~2.7 pts | caution | Not in RECORD; RECORD L39 gives +0.07 to +0.20 for a different item |
| 24 | L27 against-list: IREN customer prepays 90%; "Oracle and Meta cleared, inside talk per relay" | caution | 90% not in RECORD; "cleared" undefined; relay-sourced. Omits IREN +18.69% rebound (RECORD L72) |
| 25 | L31 too-worried list | caution | Not stated whether any one or all. "HY under 320" tests magnitude not the "real route" claim; CoreWeave "holds guide" is baseline; "ING routine reason" ING gave none; "OpenAI near $20B" undefined; SoftBank pro forma unobservable by 11/20 (11/10 headline is 9/30); one sub-320 print vs six-print run unspecified |
| 26 | L33 too-calm list | caution | "any one" of eight; "CCC flat", "named lab compute deferral" undefined; "another agency" implies one at floor, unstated. Mostly can fail (named lender refuses, 368 by 11/17, tail +30 twice, PRED-38) |
| 27 | L35 "No probability" vs L45 "60 and 48 held" | caution | Two numbers printed as scores; RECORD L23 says labelled holds, no live falsifier. READ says "EARNED" undefined |
| 28 | L39 scores VULCAN 15/25, BROCK 58/70, HANS T-14 | caution | Not in RECORD; Gate 069 only in RECORD L69 |
| 29 | L45 M-01/M-05 closed neither branch | ok | GRADES: M-01 max 348 <350, claims max run 0; M-05 max 7413 <7516. RECORD L15 adds "under the letter's common construction" (letter ambiguity unmentioned in READ); HY ended 2bp below UP edge |
| 30 | L45 M-04b step 1 of 2 | ok | GRADES cell 11/5 2818 flag 1. READ omits RECORD L17: 11/6 FRED cell >=22.45 fires UP, M-04 30->34; vendor VIX 24.13 intraday |
| 31 | L43 "Unread by every desk" | caution | Same repo-grep scope as #12 |
| 32 | GRADES L13 cell numbers | caution | GRADES note: numbering "in this pull; the frozen grid and FRED govern"; RECORD "grade at actual cell 15" unverified |
