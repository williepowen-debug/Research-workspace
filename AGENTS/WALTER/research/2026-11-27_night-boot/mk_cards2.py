import json
RO = "WALTER night boot 2026-11-27, step 7h X bookmarks (Will-launched boot; 2 new IDs fetched 2026-11-28T03:39:41Z)"
P = "PROME/reports/2026-11-11_united-fidelity-follow-up/SYNTHESIS.md"
c20 = dict(
 id="SIG-W-20261127-020",
 slug="BANK-FAILURE-United-Fidelity-Bank-fsb-Evansville-IN-closed-Fri-Nov-27-by-OCC-FDIC-receiver-First-Citizens-assumes-deposits-buys-assets-5.9B-assets-5.4B-deposits-DIF-cost-1.83B-22-branches-incl-Florida",
 safety_net="clear", event_window="open", route_origin=RO,
 origin=["@MacroEdgeRes X post 2026-11-28T01:26:38Z (Will bookmark)", "FDIC press release 2026-11-27 'First-Citizens Bank & Trust Company, Raleigh, North Carolina Assumes ...', fdic.gov, read 2026-11-28T03:40:20Z", "FDIC Failed Bank List row, read 2026-11-28T03:40Z"],
 signal_type="catalyst",
 title="BANK FAILURE: United Fidelity Bank, fsb, Evansville, Indiana (FDIC cert 29566) was closed Fri Nov 27 by the OCC, with the FDIC as receiver; First-Citizens Bank & Trust (Raleigh) assumes substantially all deposits and buys substantially all assets. $5.9B total assets and $5.4B deposits at 9/30; FDIC estimates the Deposit Insurance Fund cost at $1.83B (about 31% of assets); 22 branches in Indiana, Illinois, FLORIDA, Colorado and the US Virgin Islands reopen as First Citizens. This is the bank the fleet has tracked since Nov 11 (DOCKET L1126)",
 body="""# United Fidelity Bank, fsb failed, Fri Nov 27 (FDIC primary read)

| Item | Detail | Source |
|---|---|---|
| Closure | Closed 'today' (Nov 27) by the **OCC**; **FDIC appointed receiver** | FDIC press release 11/27 (read) |
| Resolution | **First-Citizens Bank & Trust Company**, Raleigh NC, assumes substantially all deposits and purchases substantially all assets; depositors keep all funds and coverage | same |
| Size | **$5.9B total assets, $5.4B total deposits** as of 9/30/2026 | same |
| Cost | **Estimated DIF cost $1.83B** (about 31% of total assets, WALTER's division) | same |
| Footprint | **22 branches in Indiana, Illinois, Florida, Colorado and the US Virgin Islands**; reopen as First Citizens Saturday (Saturday branches) or Monday | same |
| List | FDIC Failed Bank List: United Fidelity Bank, fsb, Evansville, Indiana, cert 29566, acquirer First-Citizens Bank & Trust Company, closing date November 27, 2026 | fdic.gov failed bank list (read) |

## What the fleet already holds (not re-verified tonight)

| Record | Content | Owner |
|---|---|---|
| SIG-W-20261111-027 (DEWEY 003R) | United Fidelity was **69.1%** of the $1 to 10B band's new problem loans in Q3; total capital **7.26%** after a **$246.9M Q3 loss** | REGINALD, GIBBS |
| """ + P + """ | OCC order 2023-031 active; Fed written agreement 24-014 with the three parents active; **$2.14B multifamily on nonaccrual**; equity $652.5M to $389.7M (6/30 to 9/30); outside investors hold the **parent's notes and preferred** (report D); CDs advertised at 4.20% to 4.45% APY [11/6] | PROME (synthesis), REGINALD |
| CREED, HOMER, NEXUS, FLG STATUS | United Fidelity about **90% of the industry's Q3 multifamily past-due rise** (FDIC QBP 11/24); bank multifamily charge-offs ex United Fidelity +21% to $784M | HOMER, CREED |
| CORAL KB ML-CORAL-166 | about **$598M of 2021 to 2025 Florida multifamily originations** (HMDA), all retained; Florida impairment UNKNOWN | CORAL |

- **So what:** a $5.9B bank failing with a 31% loss estimate is large for a single small-bank failure, and the loss sits on the Deposit Insurance Fund, not depositors. The fleet's read so far was that this bank's problem is concentrated (one bank, related sponsors), not a breadth signal; the failure confirms the bank-level stress but does not by itself establish spread. The Florida multifamily loans now pass to First Citizens or stay with the FDIC receiver; the press release does not say which loans First Citizens declined, if any.
- **Open, for owners:** whether the parent's notes and preferred are impaired (report D holders); any loss-share agreement (none stated in the release); First Citizens' own statement (not read); how Monday trades in regional banks (KRE, held-position names are TERRY's to judge).
- **Not read:** OCC's own release; First Citizens' release; the bookmark account's text beyond the FDIC wording it copies.""",
 source="fdic.gov/news/press-releases/2026/first-citizens-bank-trust-company-raleigh-north-carolina-assumes (read 2026-11-28T03:40:20Z); fdic.gov/bank-failures/failed-bank-list and /united-fidelity-bank-fsb (read); x.com/MacroEdgeRes/status/2126487902616187341; " + P + "; BOARD SIG-W-20261111-027",
 action=["REGINALD","HOMER","CORAL"], info=["BROCK","LIQUID","CREED","GIBBS","FLG","OZK","NEXUS","DEWEY","RED","PROME"],
 precedence="IMMEDIATE", confidence=0.95,
 confidence_language="confirmed: FDIC press release and failed-bank list read directly",
 cluster="BANK_COLLATERAL", domain="BANK_CRE",
 entities=["United Fidelity Bank","Evansville","OCC","FDIC","First-Citizens Bank & Trust","Deposit Insurance Fund","DOCKET L1126","multifamily nonaccrual","Florida"],
 dispatch_note="IMMEDIATE: a named US bank failure, read at the FDIC; the fleet's own tracked case (DOCKET L1126). REGINALD action (BANK_CRE owner), HOMER action (the bank is about 90% of the Q3 multifamily past-due rise), CORAL action (Florida branches and $598M Florida multifamily). TERRY by BOARD and a direct message for tradeability. RED, PROME by BOARD diff.",
 route_summary="United Fidelity Bank failed 11/27: $5.9B assets, DIF cost $1.83B, First Citizens assumes")

c21 = dict(
 id="SIG-W-20261127-021",
 slug="Will-bookmark-Goldman-chart-Nasdaq-100-futures-net-non-commercial-positioning-6-week-change-about-minus-17pct-of-OI-lowest-in-the-chart-since-mid-2023-CFTC-via-Kobeissi",
 safety_net="clear", event_window="closed", route_origin=RO,
 origin=["@KobeissiLetter X post 2026-11-27T21:52:44Z (Will bookmark), chart image opened (Goldman Sachs GIR Exhibit 5, source CFTC)"],
 signal_type="context",
 title="Will bookmark: Goldman chart (CFTC data, via Kobeissi): Nasdaq 100 CME futures net non-commercial positioning, 6-week change as % of open interest, fell to about -17%, the lowest on a chart starting mid-2023 (prior low about -15%, spring 2024), from a +31% peak about October; Kobeissi adds that NDX and SMH options positioning is the most bearish since April 2026. The 'largest since the 2022 bear market' claim is outside the chart's window",
 body="""# Nasdaq 100 futures positioning (Goldman chart, CFTC data)

| Claim | Read | Verdict |
|---|---|---|
| 6-week change in net non-commercial NDX futures positioning about -17% of OI | chart opened: dashed line near -17%, last point Nov 2026 | REPORTED (Goldman chart; CFTC data not pulled by WALTER) |
| 'largest 6-week reduction since the 2022 bear market' | chart starts about August 2023; the low inside it is about -15% (spring 2024) | Within the chart: lowest since mid-2023. **The 2022 comparison is not shown** |
| prior +32% 6-week increase ending September | chart peak about +31%, around Sep to Oct 2026 | consistent with the chart |
| NDX and SMH options positioning most bearish since April 2026 | text only | UNVERIFIED (no chart) |

- **Vintage:** CFTC COT for the week of Nov 24 is normally delayed by the Thanksgiving holiday; the chart's last point date is not printed. Research-Intake holds a cftc_cot.json for 11/27, not read here.
- **So what:** positioning has swung from crowded long to short-leaning in six weeks; context for HENRY's index-mechanics read and VIOLET's vol read, not a registered trigger.""",
 source="x.com/KobeissiLetter/status/2126434072331534650 and pbs.twimg.com/media/HYDd4M2XIAAprFg.jpg (opened 2026-11-28)",
 action=["HENRY"], info=["VIOLET","VULCAN","RED","PROME"],
 precedence="ROUTINE", confidence=0.6,
 confidence_language="reports: a Goldman chart relayed by an aggregator; CFTC not pulled",
 cluster="POSITIONING_VALUATION", domain="MARKET_VOL",
 entities=["Nasdaq 100","CFTC","Goldman Sachs","SMH","non-commercial positioning"],
 dispatch_note="ROUTINE context; HENRY action (index mechanics and positioning), VIOLET info (vol), VULCAN info (semis). RED, PROME by BOARD diff.",
 route_summary="Bookmark: NDX futures positioning 6-week change about -17% of OI (Goldman, CFTC)")
json.dump([c20], open("cards-020.json","w"), indent=1, ensure_ascii=False)
json.dump([c21], open("cards-021.json","w"), indent=1, ensure_ascii=False)
print("ok")
