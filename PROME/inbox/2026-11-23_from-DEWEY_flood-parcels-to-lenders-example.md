# DEWEY -> PROME: flooded basin homes to recorded lenders, one worked example (Silver Pines Estates, Rockledge, Brevard)

**Written:** 2026-11-23 18:05 ET (`date`), DEWEY (Claude Code, Opus 5.5, spawned by PROME prome-77). **Task:** DEWEY row of Part 3, `PROME/reports/2026-11-23_florida-flood-sweep/FOLLOWUP_2026-11-23.md`. **Report:** `AGENTS/DEWEY/output/2026-11-23_flood-parcels-to-lenders-silver-pines.md` (parcel table, method, recipe).

## The chain

| Link | What the record shows | Label |
|---|---|---|
| River above the home-flooding stage | NWS Melbourne Flood Statement 947 AM EST 11/23: St. Johns near Cocoa 18.6 ft (24-h max 18.7), "approaches the flood of record", steady through late week; gauge 18.59 ft at 21:15Z | CONFIRMED |
| Named place | Same statement: "At 17.2 feet, Water enters homes ... also low lying homes in the Silver Pines subdivision in Rockledge" | CONFIRMED that NWS names it |
| Homes there actually took water | NWS's line is a standing stage threshold; no city, county or news report found naming Silver Pines in this event | PROXY |
| Which homes are low | FEMA map (panel 12009C0428H, effective 2021-01-29): 32 of 185 single-family parcels in zone AE, 59 in shaded X, 94 in X; AE on Matthew Dr, Shepard Dr, Judith Ter | CONFIRMED (map), PROXY (map = flooded) |
| Flood cover | Mapped-zone homes with a federally regulated or insured mortgage must carry it by law; in force or not is in no free record | UNKNOWN per parcel |
| Debt on the parcel | Brevard Clerk index, matched on lot, block and subdivision: 13 of 20 sampled homes carry a recorded mortgage (8 of 10 in AE, 5 of 10 in X); 4 none found; 3 no record matched | CONFIRMED (originator of record) |
| Who holds it today | At least 4 of 13 are FHA (1 read from the document, 3 inferred from HUD subordinate liens) and 1 VA inferred, which usually means Ginnie Mae pools with federal insurance on the credit loss | PROXY |

## Lenders of record (13 mortgaged homes; originator, not necessarily today's holder)

| Type | First lien | Second or other lien |
|---|---|---|
| Non-bank | Rocket Mortgage LLC (FHA, CONFIRMED), Mortgage Research Center LLC dba Veterans United (VA inferred), Bayshore Mortgage Funding LLC, Swift Home Loans Inc, Lower LLC, Countrywide Home Loans (2003, may be paid) | |
| Bank or bank subsidiary | Fifth Third Bank NA (2023), SunTrust Mortgage Inc (2012, now Truist), PrimeLending, a PlainsCapital Company (2016, Florida housing-bond loan) | |
| Credit union | Space Coast Credit Union (2021) | Space Coast Credit Union (2023), Launch Credit Union (2022) |
| Government | | HUD 3 (2021, 2025, 2026-05-06; FHA partial claims INFERRED), Florida Housing Finance Corp 1 |
| MERS as nominee, originator unread | 3 (2014, 2019, 2020) | |
| Private | | Palmetto Surety Corp (a surety's $500,000 collateral mortgage, 2022) |

Foreclosure filings: none since 2015 in the sample (one lis pendens 2014 by Deutsche Bank National Trust Co as trustee; that home was refinanced in 2025). No Seacoast, SouthState or other basin-concentrated listed bank appears.

## What it means, plainly
The debt on these flooded-zone homes sits mostly with non-bank lenders and federally insured loans, not on regional bank balance sheets; the one recurring local balance-sheet lender is Space Coast Credit Union. If borrowers default, the first loss falls on the uninsured owner's equity, then on FHA or VA, with servicers advancing payments in the meantime. One borrower already needed an FHA workout lien in May 2026, before the flood. This does not test Will's hypothesis that banks will hide losses; in this sample there is little bank exposure to hide.

## Where each route stopped
| Site | Time (ET) | Response |
|---|---|---|
| Brevard Property Appraiser (www.bcpao.us, site and API) | 17:22:54; retested 17:30:12 | 403, Cloudflare managed challenge. STOPPED. Same data reached through Brevard County GIS |
| Brevard Clerk AcclaimWeb | 17:30 to 18:03 | Worked after the public-records disclaimer click-through (no CAPTCHA, no account). One connection reset about 17:48, then normal; a document download timed out 18:03:31, document pulls stopped |
| FEMA NFHL, Brevard GIS, NWS | 17:22 to 17:42 | Open, no refusal |

Will's browser would close the gaps: the three MERS mortgages (OR 8636/1234, 7267/284, 8592/50) name their lender on page 1.

## Not reached
Seminole and Volusia (Lake Harney, Whitcomb Drive) were not attempted; one county was enough for the bounded example. Inbox: the PROME WQ-735 client-name switch and TERRY's thesis-grade ask are both deferred to my next ordinary session (each packet asks for that), logged in my board log. WQ-735 reply line: switched 0 scripts this session, no refusals to name.

## COMPLETION — DEWEY — 2026-11-23
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/DEWEY/output/2026-11-23_flood-parcels-to-lenders-silver-pines.md, AGENTS/DEWEY/output/INDEX.tsv, AGENTS/DEWEY/board_log.tsv, AGENTS/DEWEY/scripts/BACKLOG.md, this packet, AGENTS/REGINALD/inbox/2026-11-23_from-DEWEY_flood-parcel-lenders.md, AGENTS/WALTER/inbox/DEWEY/2026-11-23_from-DEWEY_flood-parcels-to-lenders.md
RESULT: One basin example built from records: Silver Pines Estates (Rockledge), named by NWS 11/23 at 18.6 ft; 32 of 185 homes in FEMA zone AE; 13 of 20 sampled homes carry a recorded mortgage (8 of 10 in AE). First-lien originators: 6 non-bank, 3 bank, 1 credit union, 3 MERS unread; at least 4 FHA; no foreclosure filing since 2015; 3 HUD workout-type liens, one 2026-05-06.
GAPS: Flood-entry is a PROXY (NWS stage threshold, no local damage report found); flood cover and today's holder UNKNOWN; 3 MERS originators unread (download timed out 18:03 ET); Seminole and Volusia not attempted; appraiser site refused (Cloudflare challenge 17:22 and 17:30 ET).
WILL_NEEDS: None required. Optional: open three Brevard Official Records documents (OR 8636/1234, 7267/284, 8592/50) in a browser to name their lenders.
FOLLOW-UP: REGINALD reads the lender list (packet sent). TERRY: no investment implication from one subdivision; PROME decides whether to route.
