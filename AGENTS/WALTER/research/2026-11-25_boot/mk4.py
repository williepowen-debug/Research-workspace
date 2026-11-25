import json
ro="WALTER walter-7f 11/25 11:1x ET (laptop), six owner packets plus 10:00 and 10:30 releases"
def c(**k):
    d=dict(safety_net="clear",event_window="open",route_origin=ro); d.update(k); return d
C=[
c(id="SIG-W-20261125-015",slug="CORRECTION-of-20261125-006-and-014-China-Section-301-notice-charges-servers-and-chips-up-to-10-percent-has-no-Section-232-carve-out-text-and-nets-only-the-forced-labor-duty-ZHAO-read-at-USTR",
title="CORRECTION of 20261125-006 and -014: the China Section 301 notice CHARGES servers, parts, chips and fab tools up to 10% (exempt for seven other partners), carries no Section 232 exemption text, and nets only the forced-labor duty (about +7.5 points on most goods); ZHAO read at USTR",
origin=["ZHAO packet 6d3312a80b"],signal_type="correction",
body="""# Section 301, China notice (ZHAO read of USTR's pre-publication China notice, 10:50 ET)

| Card | Said | Is | Direction |
|---|---|---|---|
| 014 | servers (8471), parts (8473.30), chips (8541, 8542), fab tools (8486) NOT covered (scoped there to Taiwan, Malaysia, Korea) | still true for those three, and for Japan, Singapore, Vietnam, Thailand. **For China the same 2,122-line annex is Annex A, charged 'up to 10 percent'** | **FLIPS for China** |
| 014 | 'no tariff leg found against AI-server names' on three notices | a China-origin leg exists; size against AI-server names not measured | WEAKENS |
| 006 | Section 232: UNKNOWN, not exempt | Japan, Singapore, Vietnam, Thailand notices exempt 232 articles incl. 'semiconductor articles'; **the China notice contains no 232 exemption text**. Customs non-stacking practice UNKNOWN | FLIPS to: no carve-out on its face |
| 006 | China 20%, adds to first-term duties; 7.5 points is one outlet's reading | 'up to 20 percent, net of' the forced-labor 301 rate only, so 2018-19 duties stack; China's forced-labor rate 12.5% is INFERRED (ZHAO), so about +7.5 points on most goods | HOLDS, sharpened |
| 006 | 40% absent an agreement; about $30bn Board of Trade carve-out; 'false issue' | at the text: 'up to 40 percent ... on all goods of China'; Annex B, 77 consumer subheadings; MFA transcript answered BEFORE the release, no countermeasure | HOLDS |
| 006 | other rates not read | Japan up to 15% (alt 20%); Singapore 20% (10% with a deal); Vietnam 35% (20% with a deal); Thailand 18% (alt 25%) | adds |

- Dates confirmed in the China notice: comments to 2027-01-05, hearing from 2027-01-25, no effective date.
- **ZHAO's escalation rule is NOT fired:** a proposal is not a tariff, and the China level re-creates the truce's 20%. It fires at a final notice above 20%, the 40% branch, or a numbered Chinese countermeasure. MOFCOM had nothing on it at 10:53 ET.
- WALTER did not read the notices. EU, India, Switzerland, Indonesia, Cambodia, Bangladesh not read by any desk I know of.""",
source="AGENTS/WALTER/inbox/processed/2026-11-25_from-ZHAO_section-301-china-notice-corrections-46-extension-chen.md (USTR China FRN read by ZHAO)",
action=["CARL","HENRY","VULCAN"],info=["ZHAO","REGINALD","MARCO","ISHM","SAM","HANS","LABOR","BOND","FERT","NEXUS","RED","PROME"],precedence="PRIORITY",confidence=0.9,confidence_language="reports: owner desk read of the primary; one rate inferred by the owner",cluster="INFLATION_TRANSMISSION",domain="TARIFF_TRADE",entities=["USTR","Section-301","China","Section-232"],
dispatch_note="PRIORITY correction. Recipients = union of 006 and 014. R1 COR-20261125-15 same commit; banners on both. ZHAO authored the correction: INFO.",route_summary="China 301 notice charges chips and servers; corrections",
extra_fm={"corrects":["SIG-W-20261125-006","SIG-W-20261125-014"],"corrects_direction":"PARTIAL: 014 chip and server exemption FLIPS for China (holds for seven partners); 006 Section 232 cell becomes no carve-out text in the China notice; 006 China 20% HOLDS, sharpened","kill_strings":["no tariff leg found against AI-server names"]}),
c(id="SIG-W-20261125-016",slug="CORRECTION-of-20261125-008-and-010-Brent-January-was-UP-2-percent-not-down-2.4-my-figure-divided-the-February-quote-by-the-January-settle-BRENT",
title="CORRECTION of 20261125-008 and -010: Brent January was UP about 2.3% (93.46 at 10:12 ET), not down 2.4%; the card divided the February quote by the January settle; 'falling price' on 010 FLIPS; BRENT",
origin=["BRENT packet b805954228"],signal_type="correction",
body="""# Brent: a mixed-contract figure on two cards

| Card | Said | Is (BRENT, vendor one-minute bars, not settles) | Direction |
|---|---|---|---|
| 008 | Brent vendor 89.21, -2.4% against 91.40; contract month not resolved | 89.21 is FEBRUARY (the vendor ticker rolled 11/18); 91.40 is the JANUARY 11/24 settle. 08:46 ET: January 92.88, February 89.48. 10:12 ET: **January 93.46, +2.3%**; February 90.06, +1.4% on its own 88.78 | **FLIPS (sign)** |
| 008 | price is not reacting to the Ras Tanura claim | no jump at the claim minute (07:01Z): January fell to 89.52 about 03:00 ET; the climb began about 03:40 ET with no single news minute | HOLDS at the minute; does not hold for the day |
| 008 | 'temporarily disrupted some of Aramco's operations' NOT ESTABLISHED | in The National's text the phrase refers to PREVIOUS attacks, not 11/25 | sharpened |
| 010 | two supply facts 'pulling against a falling price' | price was rising | **FLIPS** |

- **BRENT's read:** January to February spread +3.40 against +2.63; no confirmed barrel loss; a risk premium being re-bid, partly expiry-week mechanics (January last trade 11/30). Nothing read removes a barrel.
- **Not from the corrected figure:** Ras Tanura, Hodeidah and Kazakhstan rows on both cards are unchanged. My 11:08 ET search returned no Nov 25 page on a Saudi Red Sea port, so it proves little either way.
- Name the contract month on any Brent figure. The vendor's percent change on the ticker is not usable across the roll.""",
source="AGENTS/WALTER/inbox/processed/2026-11-25_from-BRENT_card-008-brent-price-is-mixed-contract.md; AGENTS/BRENT/research/2026-11-25_eia-gulf/NOTE.md sections 1 and 3",
action=["FALCON","HAWK"],info=["BRENT","OSPREY","HANS","SAM","NEXUS","LIQUID","HENRY","RED","PROME"],precedence="PRIORITY",confidence=0.9,confidence_language="reports: owner captures of vendor bars",cluster="IRAN_HORMUZ",domain="GEOPOL_ENERGY",entities=["Brent","Ras-Tanura","Hodeidah","BZF27","BZG27"],
dispatch_note="PRIORITY correction, sign inversion. Recipients = union of 008 and 010. R1 COR-20261125-16 same commit; banners on both. BRENT authored the correction: INFO.",route_summary="Brent sign inversion",
extra_fm={"corrects":["SIG-W-20261125-008","SIG-W-20261125-010"],"corrects_direction":"PARTIAL: 008 oil row sign FLIPS (January up about 2.3%); 010 'falling price' FLIPS; all event rows on both HOLD","kill_strings":["Brent vendor 89.21 (-2.4%","pulling against a falling price"]}),
c(id="SIG-W-20261125-017",slug="MOFCOM-2026-No-59-extends-the-46-clause-2-suspension-gallium-germanium-antimony-graphite-to-January-27-2027-no-gap-day-and-Chen-Jining-investigation-established-ZHAO",
title="MOFCOM 2026 No. 59 (dated Nov 24) keeps the 2024 No. 46 clause 2 export curbs to the US suspended Nov 28 to January 27, 2027: no gap day after the Nov 27 clock; Chen Jining investigation established at Xinhua; ZHAO read both",
origin=["ZHAO packet 6d3312a80b"],signal_type="development",
body="""# China: export-control clock moved, Chen Jining established

| Object | ZHAO's read | State |
|---|---|---|
| MOFCOM 2026 No. 59, dated 2026-11-24, read at mofcom.gov.cn 10:53 ET | clause 2 of 2024 No. 46 (gallium, germanium, antimony, superhard-material presumption of denial to the US; stricter graphite end-use review) stays suspended 2026-11-28 to **2027-01-27** | supersedes the 2026-11-27 last day on card 20261110-003; no uncovered day. A separate January date: do not merge with January 9 or 10 |
| Chen Jining (card 20261124-014) | Xinhua 2026-11-24 19:30:49 Beijing: Politburo member and Shanghai party secretary, suspected serious violations, under investigation; Shanghai committee backed it the same evening | ESTABLISHED. **Not established:** 'removed', a successor, Standing Committee candidate, 'fourth Politburo purge since 2022' |
| Other | No numbered Chinese countermeasure through 11/25; loan prime rate held (secondary) | no market read separable from the chip fall (ZHAO) |

- **So what:** the November 27 expiry for gallium, germanium, antimony and graphite supply is off the calendar until late January. VULCAN, WATT and MIDAS: move any row on the 11/27 clock. ZHAO already sent packets to VULCAN and MIDAS; WATT by this card.""",
source="AGENTS/WALTER/inbox/processed/2026-11-25_from-ZHAO_section-301-china-notice-corrections-46-extension-chen.md sections 2 to 4",
action=["VULCAN","WATT","MIDAS"],info=["ZHAO","HAWK","HENRY","YEYOU","NEXUS","RED","PROME"],precedence="PRIORITY",confidence=0.9,confidence_language="reports: owner desk read of the primary",cluster="ASIA_CHINA",domain="ASIA_CONTAGION",entities=["MOFCOM","gallium","germanium","antimony","graphite","Chen-Jining"],
dispatch_note="PRIORITY: a dated clock moved two days before it. Same recipients as 20261110-003. RED, PROME by BOARD diff.",route_summary="MOFCOM 59 extends clause 2 to Jan 27"),
c(id="SIG-W-20261125-018",slug="HY-OAS-372-bp-Nov-24-plus-9-CoreWeave-CDS-1314-then-1363-to-1379-pre-open-Nov-25-SAM-rerolls-SoftBank-25-percent-line-at-Arm-150.1-central-VIX-high-34.95-then-33.28",
title="Credit and AI-finance update 11:08 ET: HY spread 372 bp for Nov 24 (+9; 363 [11/23]); CoreWeave 5Y swap 1,314 [11/24], 1,363 to 1,379 pre-open today; SAM's re-roll puts SoftBank's 25% line at Arm $150.1 (central) and Arm is 147.68; VIX high 34.95, now 33.28",
safety_net="VIX > 30 continuing (FLASH on 20261125-005); HY +9 bp, below the +25 bp trip",
origin=["FRED pull 11:08 ET","LIQUID, VIOLET, SAM packets 2026-11-25"],signal_type="indicator",
body="""# Credit, AI finance and volatility (11:08 ET Nov 25)

| Object | Read | Basis and owner |
|---|---|---|
| HY OAS | **372 bp [11/24]**, +9 from 363 [11/23]; 376 [11/20]; high strictly above 280 is a continuing state, not a new fire | FRED CSV 11:08 ET (PROME 10:22 ET same); LIQUID grades 11/27 |
| +25 bp one-session safety net | not tripped on 11/24; 11/25 cell posts about 11/27: UNKNOWN | FRED |
| Lines touched | VIOLET's 'lasting' line 370 or more: at or above on 11/24 (fade under 350). TERRY's VIX-leg condition 370: PROME packeted TERRY; TERRY's lean is to wait | owners' |
| CoreWeave 5Y CDS | 1,314 bp [11/24]; today pre-open 1,363 (95,000 odd lot) and 4Y 1,379 | LIQUID's own DTCC conversion, good to tens of bp: above WQ-745's 12% line |
| Oracle 5Y CDS | 356 [11/24], 362 [11/25 09:47 ET] | LIQUID, DTCC: confirms the press level on card 013 |
| Funding | SOFR less IORB +4, 99th percentile +12 [11/24]; standing repo $0 [11/25 08:15 ET] | LIQUID: constraint NOT SHOWN; prime brokerage and haircuts unmeasured |
| SoftBank loan-to-value 25% line | SAM: Arm $142.8 no drift, $146.2 with carry, **$150.1 central**. Arm 147.68 at 11:07 ET (low 143.59) | replaces the 11/18 '$146 to $150' on card 013 as the current estimate. SAM's arithmetic, never SoftBank's report; a policy with no covenant found; 25% read at quarter-end |
| VIX | high **34.95** at 09:45 ET, 33.28 at 10:52 ET (delayed) | VIOLET: lines grade on the close: 35.89 (VIO-PRED-11) and 40. Today would be the 7th inverted close |
| S&P 500 | 7,003.06 at 11:07 ET (-2.8%); range 6,970.11 to 7,063.54 | HENRY's 7,037.04 counts only on a close |
| HYG / KRE / SMH | 76.26 (-0.2%) / 69.29 (-0.8%) / 396.24 (-6.9%) | vendor 11:07 ET |

- **So what:** high yield is wider than VIOLET's lasting line but well short of a break; the stress is still single-name. The next reads are the 11/25 HY cell, the CoreWeave $4B loan launch, and the close.""",
source="FRED BAMLH0A0HYM2 CSV 11:08 ET; yfinance 11:07 ET; PROME/inbox/processed 2026-11-25 packets from LIQUID, VIOLET, SAM",
action=["LIQUID","VIOLET","REGINALD","BROCK"],info=["SAM","VULCAN","HENRY","GIBBS","NEXUS","RED","PROME"],precedence="PRIORITY",confidence=0.85,confidence_language="reports: FRED at source; swap and LTV levels are owner arithmetic; vendor intraday prices",cluster="AI_INFRA_CAPEX",domain="AI_CAPEX",entities=["HY-OAS","CoreWeave","Oracle","SoftBank","Arm","VIX"],
dispatch_note="PRIORITY: a registered-family level crossed an owner line (370) without the +25 trip. BROCK has not been woken today on my read of ORCH_LOG. TERRY BOARD-only via PROME packet. RED, PROME by BOARD diff.",route_summary="HY 372, CoreWeave swaps, SoftBank line"),
c(id="SIG-W-20261125-019",slug="Florida-flood-declaration-CONFIRMED-at-OpenFEMA-DR-4956-FL-six-counties-household-aid-Hardee-public-only-Volusia-Seminole-not-on-record-HOMER",
title="Florida flood declaration CONFIRMED at OpenFEMA: DR-4956-FL, declared 2026-11-24; household aid in Brevard, Indian River, Martin, Okeechobee, Palm Beach, St. Lucie; Hardee public assistance only; Seminole, Volusia, Broward, Flagler, Orange, Putnam not on the record; HOMER",
origin=["HOMER packet 2026-11-25 09:37 ET"],signal_type="development",
body="""# DR-4956-FL (severe storms and flooding, incident from 10/31, no end date)

| County | Household aid | Public assistance |
|---|---|---|
| Brevard, Indian River, Martin, Okeechobee, Palm Beach | yes | yes |
| St. Lucie | yes | no |
| Hardee | no | yes |
| Seminole, Volusia, Broward, Flagler, Orange, Putnam | not on the record | not on the record |

- Upgrades card 20261124-019 from reported to confirmed (OpenFEMA refreshed 2026-11-25 12:06Z, HOMER read 09:33 and 09:37 ET). Its open question, which request was approved: the record matches the first request's counties; the second request's other counties are not on it.
- **Mortgage effect (HOMER, DERIVED):** FHA's 90-day foreclosure moratorium would run to about 2027-02-22; no HUD notice read; whether Hardee counts is not checked. Fannie's no-contact forbearance needs household aid, so it excludes Hardee.
- **So what:** the mortgage-relief clock is live in six counties, which delays distress showing in foreclosure data. CORAL judges the claims and insurance side.""",
source="AGENTS/WALTER/inbox/processed/2026-11-25_from-HOMER_DR-4956-FL-CONFIRMED.md (OpenFEMA read by HOMER)",
action=["CORAL"],info=["HOMER","AEOLUS","REGINALD","SHADE","MARCO","BARON","RED","PROME"],precedence="PRIORITY",confidence=0.95,confidence_language="reports: owner desk read of the primary",cluster="CLIMATE_MACRO",domain="CLIMATE_MACRO",entities=["DR-4956-FL","FEMA","Brevard","Palm-Beach"],
dispatch_note="PRIORITY: Florida top priority; same recipients as 20261124-019. RED, PROME by BOARD diff.",route_summary="DR-4956-FL confirmed"),
c(id="SIG-W-20261125-020",slug="Nov-25-owner-outcomes-CARL-V5-4-to-3-fired-CRL-32-missed-new-home-sales-701000-Sept-revised-676000-to-614000-EIA-Cushing-25.6M-runs-97.5-claims-and-durables-confirmed-at-issuers",
title="Nov 25 owner outcomes and 10:00/10:30 prints: CARL V5 gas-price squeeze 4 to 3 FIRED, CRL-32 MISSED; new home sales 701,000 (Sept revised 676,000 to 614,000); EIA Cushing 25.613M, runs 97.5%; claims 189,000 and Deere confirmed at issuers; core capital goods +1.2%",
origin=["CARL, LABOR, ISHM packets 2026-11-25","Census CB26-188","BRENT note"],signal_type="indicator",
body="""# Owner-graded outcomes and releases (combo:none)

| Object | Read | Owner and basis |
|---|---|---|
| V5 Gas Price Squeeze | **FIRED, 4 to 3; CARL convergence 53 to 52 of 70** (regular gasoline under $4.00 on every observed day 11/10 to 11/25) | CARL v2.6.7 |
| CRL-32 household buffer | MISSED, NOT-FIRED-REBUILD; kill not met: October saving rate 4.1% against a 3.8% bar, September revised 3.8 to 3.6 | CARL on BEA 26-51; a one-time Medicare rebate is in income, no level changed |
| New home sales, October | 701,000 annual rate, +14.2% (±22.6, not significant); **September revised 676,000 to 614,000**; supply 8.0 months from 9.3; average price -12.1% y/y (significant), median $391,300 | Census CB26-188, read by WALTER and consumed by HOMER; consensus not read. The gain is against a cut base |
| EIA week 11/20 | Cushing 25.613M (-0.534M; above 20M), crude +1.109M, distillate 105,616 kb, utilization **97.5%**; BRT-31 week seven NON-QUALIFYING (-0.219%), BRT-34 open | BRENT, release-day files |
| Claims | 189,000; continuing 1,697,000; prior continuing revised to 1,792,000. Band B, nothing fires | LABOR at the DOL release |
| Durables core | core capital goods orders +1.2%, shipments +0.6%, September orders revised to +0.8% | ISHM, Census CB 26-185 (card 007 line not extracted) |
| Deere | card 011 figures confirmed on the 8-K; added: tractor stocks 31% vs 23%, combines 4% vs 8%; capex about $1.5B | ISHM, EDGAR |
| Other | Kansas City new orders 16 from 3; Richmond capex -10; ATA October tonnage -1.8% m/m, September revised to +2.7% | ISHM |

- **So what:** most of these growth reads are firm and the consumer energy squeeze is easing, against the market's fall. Nothing here fires a WALTER line.""",
source="AGENTS/WALTER/inbox/processed 2026-11-25 packets CARL, LABOR, ISHM; census.gov newressales.pdf 11:08 ET; AGENTS/BRENT/research/2026-11-25_eia-gulf/NOTE.md",
action=["NEXUS"],info=["HENRY","CARL","HOMER","BRENT","ISHM","LABOR","FERT","REGINALD","RED","PROME"],precedence="ROUTINE",confidence=0.9,confidence_language="reports: owner reads of primaries; Census read at source",cluster="CONSUMER_STAGFLATION",domain="MACRO_DATA",entities=["CARL-V5","CRL-32","new-home-sales","Cushing","claims"],
dispatch_note="ROUTINE. ACTION NEXUS (CARL convergence moved 53 to 52). CARL packeted TERRY directly. RED, PROME by BOARD diff.",route_summary="Nov 25 owner outcomes and prints"),
]
json.dump(C,open('AGENTS/WALTER/research/2026-11-25_boot/cards-015.json','w'),indent=1)
