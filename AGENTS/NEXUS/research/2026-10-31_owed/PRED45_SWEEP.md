# PRED-45 evidence sweep — arms-length loan-level transfer at or below 90.0 cents

**Stamp:** 2026-10-31 12:25 EDT (from `date`). Read-only helper for NEXUS. **The letter has not been graded or changed.** Status of the evidence: **no qualifying instance found; the 10-Q note coverage is thin (see §3).**

Raw EDGAR output (search JSON, filing-status JSON) is saved at `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-NEXUS/ed7f75f2-0945-4652-801c-f5d603f7fbbf/scratchpad/pred45/raw/`.

## 1. Candidate transfers

| Filer | Borrower / loan | Price in cents (how computed) | Arms-length? | Document (accession · URL · date · section) | Qualifies |
|---|---|---|---|---|---|
| BlackRock TCP Capital (TCPC) | **Portfolio** of about $523M across 78 companies, moved into a continuation vehicle; 95% of the vehicle's equity sold | Cannot be computed against par. The release says: "base purchase price for the investments sold was 95% of the gross fair value as of December 31, 2025". That is a percentage of fair value, not of par, and it covers a pool, not a single loan. Gross proceeds were "approximately $152 million" (equity of a vehicle, so leverage is implied), and NAV was expected to fall "approximately 10.4%, or $0.68 per share" | Yes for the buyer side: "funds and accounts sponsored by Pantheon", with a fairness opinion from Lincoln International. But TCPC kept 5% of the vehicle and a direct stake in "substantially all" of the names | 0001193125-26-336845 · https://www.sec.gov/Archives/edgar/data/1370755/000119312526336845/tcpc-ex99_2.htm · 8-K Ex 99.2, 2026-08-06 · "Recent Developments" and "Portfolio Sale Highlights" | **NO.** It is a portfolio sale, not a loan-level sale, and it is priced against fair value, not par. ⚠️ **Watch:** TCPC's Q3 10-Q is not filed yet. Its realized-loss note may disclose this sale loan by loan. Re-test then. Check the deal date against the letter's registration date. |
| Ares Capital (ARCC) | About $1.2B of loans "sold to IHAM or certain vehicles managed by IHAM", inside about $2.5B of Q3 exits | No price disclosed. ARCC reports net realized losses of "$(52)" million in the operating-results table and "(50)" in the statement of operations; the tool flagged that these two figures differ | **No.** IHAM (Ivy Hill) is ARCC's own asset-management portfolio company. A sale to a vehicle the filer controls is not arms-length | 0001628280-26-067382 · https://www.sec.gov/Archives/edgar/data/1287750/000162828026067382/arccq3-2026exhibit991.htm · 8-K Ex 99.1, 2026-10-27 · Portfolio and Investment Activity | **NO.** The sale is to an affiliate and has no price. "3% [of exits] were on non-accrual" also has no price. |
| Hercules (HTGC) | Table rows "Proceeds from sale of debt investments (24.0)" and "Assets Sale - Participants (15.4)", in $M | None. No loan is named and no par basis is given. Q3 "($2.0) million of realized losses on debt investments" | Unknown. "Participants" may be the adviser's affiliated funds; not verified | 0001280784-26-000055 · https://www.sec.gov/Archives/edgar/data/1280784/000128078426000055/htgcq32026release.htm · 8-K Ex 99.1, 2026-10-29 · portfolio table and realized-gains paragraph | **INSUFFICIENT.** The 10-Q note was not read (§3). |
| OFS Capital (OFS) | Net realized loss "$7.8 million" in Q3; some loans "were restructured for new debt and equity investments" | None | — | 0001487918-26-000090 · https://www.sec.gov/Archives/edgar/data/1487918/000148791826000090/ofs-ex99_1.htm · 8-K Ex 99.1, 2026-10-29 · Results of Operations and Portfolio Activity | **NO** on the release: a restructuring is not a transfer, and the "SBIC I LP" sale of LP interests to a third party (10/5) is equity, not a loan. **INSUFFICIENT** on the 10-Q note, which was not read. |
| Saratoga (SAR), fiscal quarter ended 8/31 | Release: "Pepper Palace and the CLO F-Note have been sold post quarter-end"; "Exigo … fully exited at $8.0 million … -6.1% IRR" | None vs par. No cost or par figure is given for Pepper Palace or the F-Note | Not stated | 0001213900-26-107199 · https://www.sec.gov/Archives/edgar/data/1377936/000121390026107199/ea030779301ex99-1.htm · 8-K Ex 99.1, 2026-10-06 · Highlights | **INSUFFICIENT.** The 10-Q (0001213900-26-107187) co-locates "First Brands" with "sold", "realized loss", "written off" and "proceeds" in EDGAR full-text search, but those terms only appear in the same document. I could not reach the note text (§3). **Highest-priority re-read.** |
| Main Street (MAIN) | Preliminary Q3: "a decrease in cost basis due to a realized loss resulted in a net decrease of $19.4 million" (LMM); "$1.8 million" (private loan) | None. No companies are named | — | 0001396440-26-000106 · https://www.sec.gov/Archives/edgar/data/1396440/000139644026000106/main-q32026xprexerxexx991.htm · 8-K Ex 99.1, 2026-10-15 | **INSUFFICIENT.** These are preliminary figures; the full release and 10-Q are still to come. |
| AB Private Credit Investors | Assets "contributed and/or sold" into the ABPCI Private Funding V CLO | No price is disclosed | **No.** The depositor and issuer are wholly owned subsidiaries of the fund | 0001193125-26-427754 · https://www.sec.gov/Archives/edgar/data/1634452/000119312526427754/d134708d8k.htm · 8-K Items 1.01/2.03, 2026-10-21 (8-K/A 10/29) | **NO.** This is an affiliated financing transfer. |
| Onex Direct Lending BDC | "88% of the Company's loan portfolio based on fair value was priced above 85 cents on the dollar"; "completed four exits" | A mark distribution, not a transfer | — | 0001193125-26-426712 · https://www.sec.gov/Archives/edgar/data/1860424/000119312526426712/d107297d8k.htm · 8-K Items 7.01/8.01, 2026-10-20 | **NO.** This is a mark, so the "MARK at any level ⇒ no" counterexample applies. |
| First Brands (court) | OTTO STATUS docket: 11/02 status conference on the "McHenry wind-down sale (Dkt3933) + SPV inventory sale" | — | — | `AGENTS/OTTO/STATUS.md` docket row (desk record, not a court document I fetched) | **NO on the description**: these are operating-asset and inventory sales, not loan transfers. Not read at the court record. |

**Steele Creek:** the 8-K Ex 99.2 of 2026-08-25 (0001213900-26-093450) is a pro forma SOI. Its three First Brands first-lien rows are marks, so it shows no transfer. The 8-K of 2026-10-30 (0001213900-26-114092) is a "$6.2020 per share" dividend (Item 8.01) and contains no sale text.

**BROCK prior work** (`AGENTS/BROCK/research/2026-10-31_R2-review/REVIEW.md` §4, BRK-25): 10/31 full-text searches returned SEARCH-NOT-FOUND, plus the instrument finding that "par" collides with equity par-value boilerplate. The grep of the 10-28/10-29/10-25 reads found no loan sale. BROCK, SHADE and OTTO STATUS have no discounted loan sale. KB-BRK-180/198 record the earlier pattern: GP-led secondaries (CCLFX about $1B) produce **no** arms-length loan-level print.

## 2. Coverage

**Q3-2026 10-Q filed** (from data.sec.gov submissions, read 10/31): **ARCC** (10/27, 0001628280-26-067383), **HTGC** (10/29, 0001280784-26-000054), **OFS** (10/30, 0001487918-26-000091). For all three, only the earnings release was read; the 10-Q note text was not (§3). Saratoga's quarter ending 8/31 was filed 10/06.

**Q3 10-Q not yet filed as of 10/31** (submissions JSON shows no 10-Q with report date 2026-09-30): OBDC, FSK, BXSL, GBDC, MAIN, PSEC, TSLX, OCSL, MFIC, PFLT, PNNT, SLRC, CGBD, NMFC, GSBD, TCPC, BBDC, TPVG, CCAP, FDUS, GAIN, CSWC, TRIN, BCSF, KBDC, MSDL, PSBD, NCDL, CION; non-traded BCRED, ADS, HLEND, OCIC, ASIF, GCRED, OTF, NHPIF, Oaktree Strategic Credit; and Steele Creek. **That is roughly 90% of the BDC book, due about 11/02–11/16, inside the 11/20 window.** OBDE did not resolve to a CIK.

**Full-text searches** (EFTS, 10-Q/8-K, 10/01–10/31 unless noted) returned no BDC hit:
- "sold our investment": 0
- "sold our position": 0
- "sold its position": 0
- "assignment of the loan": 1 (LOPE)
- "sold at a price of": 11 (SPAC and biotech hits)
- "realized loss on the sale": 4 (Kinsale, BXMT, CBU, CNC)
- "sale of the loan": 13 (banks, REITs, credit-agreement exhibits)
- "loan sale": 88 (bank releases)
- "cents on the dollar" "loan" (7/01–10/31): 4 (Onex ×2, PBI, NVVE)
- "business development company" "loan sale" (7/01–): 49. The top hits are Q2 10-Qs, financing exhibits and the AB PCI CLO.
- "First Brands" "sale order": 0

## 3. Limitations (read before relying on a MISS)

1. **www.sec.gov blocked curl for this whole session.** At 12:05 ET it returned "Request Rate Threshold Exceeded", then HTTP 403 "Undeclared Automated Tool" through at least 12:24 ET, with the mandated User-Agent. I did not change the User-Agent. EFTS and data.sec.gov worked.
2. **Documents were read through WebFetch.** That tool extracts with a model; the quotes above are its verbatim returns, not byte-checked by me. On 10-Q HTML it stops at about 75–100k characters, mostly inline-XBRL header and the start of the SOI, **so no 10-Q realized-gain/loss note or MD&A exits paragraph was read (ARCC, HTGC, OFS, SAR, GECC).** These are the sections where a loan-level sale would be disclosed.
3. Full-text search matches at document level only; it has no proximity operator or snippets. A "First Brands" + "sold" hit does not mean First Brands was sold.
4. I did not read court dockets (First Brands, Tricolor, others) for loan-claim transfers (Rule 3001(e)), which would be the court-side route.
5. Out of class and not assessed: mortgage-REIT loan sales (BXMT "realized loss on the sale", TRTX "sale of the loan"). These are CRE loans, and whether CRE debt counts as "private credit" is NEXUS's call.

**Next pass:** re-fetch the Saratoga 10-Q (0001213900-26-107187) notes for First Brands. Then cover the 11/02–11/16 10-Q wave, starting with TCPC (Pantheon sale detail), FSK, OBDC, BCRED, GSBD, PSEC and NMFC. Run it from a session whose curl access to www.sec.gov works.
