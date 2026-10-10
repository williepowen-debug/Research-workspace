# Russia diesel deal vs Ukraine's refinery/terminal strikes — net Atlantic Basin diesel supply to April 2027

**Date:** 2026-10-10 | **Mode:** Thesis | **Commission:** REQ-DEWEY-20261010-001 (WALTER packet, Will-approved "Okay lets do A and C", commit 16395614d) | **Status:** PARTIAL (session 1 of 2, stopped at PROME closeout ask 11:47 ET) — legs 1 DONE, 2 PARTIAL, 5 PARTIAL, 3 and 4 NOT STARTED | **Confidence:** High (instrument text, tape timing) / Low (net-supply verdict — not yet reached)

---

## §0 PRE-REGISTRATION (written 2026-10-10 11:38 ET, BEFORE any primary was read)

**Disclosure of what I had seen when writing this:** the commission packet (its six UNVERIFIED claims) and the *filename* of WALTER's BOARD card `SIG-W-20261010-003` (it names "OFAC GL 135 · diesel-only · to 2027-04-07 · Trump tranches sum 4.8 Mt · last 3 Mt conditional · Novak lifting export curbs · Ukraine hits Rostov terminal · TD22 79.6M"). I had NOT read the card body, any OFAC/Treasury page, any Kremlin/Novak text, any wire, or any price. The commit carrying this section is the timestamp of record.

**Definition used throughout.** NET Atlantic Basin diesel supply from the deal = (Russian middle-distillate exports that exist BECAUSE of the deal, over a stated period, in kb/d) − (Russian middle-distillate exports lost to Ukrainian strikes over the SAME period, in kb/d). A cargo that would have gone to Brazil/Turkey/West Africa anyway and now goes to New York is a **destination reshuffle = ~0 net** to the Atlantic Basin (it may still narrow a sanctions discount or a freight leg; that is a price effect, not added supply). Both terms on the same unit, basis and period, or the comparison is not made.

### What would show the deal adds NO (or negligible) net supply
| # | Observation | Where it would be established |
|---|---|---|
| N1 | The instrument is narrow: limited to named entities/cargoes already loaded, a wind-down, a single counterparty, or attached to new designations (sign inversion) | GL text at ofac.treasury.gov |
| N2 | It does NOT authorize US importation, or EO 14066's import ban stands with no separate action — "into the US" is then false | GL text + EO 14066 / any new EO or determination |
| N3 | Russia's own export restriction on diesel/gasoil is unchanged, or eased only for producers who already export | Government decree / Novak statement / named wire |
| N4 | The 4.8 Mt is a total over a long or unstated period, or partly conditional, so the daily rate is small vs Russia's existing ~0.7–0.9 Mb/d diesel exports (my prior, to be refreshed) | Kremlin/Novak/Trump text; Kpler/Vortexa/IEA OMR export series |
| N5 | Strike-driven refinery/terminal outages remove more middle-distillate output over the period than the deal volume | Dated outage tallies (Reuters/Bloomberg calculations), terminal status |
| N6 | No ships: MINERVA ZEN unreal, not Russian-origin, or no follow-on fixtures; freight cost prohibitive | AIS/fixture reporting, named wire |
| N7 | The named-month ULSD crack did not fall on the news beyond crude's move | NYMEX HOX26/HOZ26 vs CLX26/CLZ26 (or Brent) settlements |

### What would show the deal DOES add net supply
| # | Observation |
|---|---|
| Y1 | Broad GL: all Russian-origin diesel, covering designated sellers (Rosneft/Lukoil-class), through 2027-04-07 |
| Y2 | US importation explicitly authorized with EO 14066 addressed |
| Y3 | Russia lifts or eases its diesel export restriction, with a confirmed volume and period |
| Y4 | Strike outages are short (days–weeks) relative to the period and repair rates exceed strike rates |
| Y5 | Ships observed loading/arriving at volumes incremental to baseline exports |
| Y6 | Named-month ULSD crack fell on 10/9 more than crude, with no competing driver that day |

**Confound watch (pre-committed):** if every confound I find points the same way, I will state that as a fact about the search, not as confirmation. **Prior (stated so it can be wrong):** destination reshuffle dominates incremental volume; my weak prior is "small net add, sign set by the strike tempo". This prior is NOT a finding.

---

## Key Finding (PARTIAL — session 1, 2026-10-10 11:48 ET)

The US instrument is real and broad for diesel: OFAC General License 135 (10/9) licenses every Part 587/589-prohibited transaction tied to selling, delivering, offloading or importing Russian-origin diesel, US importation included, to 12:01 a.m. EDT 2027-04-07, with no designations attached. Whether it adds NET supply is NOT yet answered: the volume claim rests on Trump's post alone (Kremlin gave none), and the swing term is Russia's OWN diesel export ban (in force since July, extended to end-October per NBC/BRENT), which Novak says Russia will lift but for which no decree was found by WALTER or the wires as of 10/10. ★ On the market leg: the whole of 10/9's settle-to-settle crack drop predates the news (CME settles HO/CL 14:28–14:30 ET; the post hit the tape at 14:46 ET); the news itself moved the November crack about −$2.2 to −$2.5/bbl after settlement, which will first appear in the Monday 10/12 settlement, mixed with weekend news.

## Leg 1 — The instrument (DONE)

| Item | Finding | Source class |
|---|---|---|
| Number / date | **General License No. 135**, dated October 9, 2026, signed Bradley T. Smith, Director OFAC | [PRIMARY: OFAC PDF `ofac.treasury.gov/media/937216/download?inline`, read 2026-10-10 11:39 ET, sha256 b42bed87…d65b] |
| Scope (a) | "all transactions prohibited by" 31 CFR 587 or 589 "that are related to the sale, delivery, offloading, or importation, including importation into the United States, of diesel fuel of Russian Federation origin are authorized through 12:01 a.m. eastern daylight time, April 7, 2027" | [PRIMARY: same] |
| Exclusion (b) | no debit to US-held accounts of the Central Bank of Russia, National Wealth Fund, or Ministry of Finance | [PRIMARY: same] |
| Attached to designations? | **No.** The 10/9 action "Issuance of Russia-related General License" carries GL 135 only; the 10/8 action amended GL 13S (Directive 4 admin transactions) — unrelated. Fleet sign-inversion guard checked: not triggered | [PRIMARY: `ofac.treasury.gov/recent-actions/20261009_33`, `/20261008`] |
| "Diesel fuel" | undefined in the license — no HTS code; no FAQ published with the action | [PRIMARY: same] |
| Covers sanctioned sellers? | On its face yes: it licenses ALL Part 587 prohibitions related to the diesel trade, and blocking under EO 14024 is a Part 587 prohibition (§587.201(a)) | [PRIMARY: eCFR 31 CFR 587.201] → reading is **INFERRED** (no OFAC FAQ yet) |
| Overrides EO 14066's import ban? | **At the regulation level, yes.** EO 14066 (3/8/2022) bans import of Russian "petroleum fuels, oils, and products of their distillation" and was issued to "expand the scope of the national emergency declared in Executive Order 14024"; §587.201(b) makes every prohibition under further EOs on that emergency a Part 587 prohibition; GL 135 licenses Part 587 prohibitions; EO 14066 §1(b) itself says its bans apply "except to the extent provided by … licenses" | [PRIMARY: Federal Register 87 FR 13625; eCFR §587.201] |
| The 2022 STATUTE | ⚠️ **Open legal question, not settled here.** P.L. 117-109 (Ending Importation of Russian Oil Act, 4/8/2022) §2 bans all HTS chapter-27 products of Russia "in a manner consistent with any implementation actions issued under Executive Order 14066"; §3 lets the President TERMINATE the ban only by a certification (Russian withdrawal accepted by Ukraine, no NATO threat, recognition of Ukraine's self-determination) effective 90 days later absent a joint resolution of disapproval. GL 135 is not a §3 termination; whether a license counts as an "implementation action" consistent with §2 is the question commentators flag. No §3 certification found (channels: OFAC action pages; not searched: Congressional Record) | [PRIMARY: govinfo PLAW-117publ109] → interpretation **UNKNOWN** |
| Treasury framing | Treasury on X: "at President Trump's direction, … OFAC is immediately issuing a temporary general license to allow the supply of Russian diesel to the global market" | [NEWS: NBC 10/9 14:56 EDT, updated 16:33] |
| EU/UK | EU and UK bans on Russian petroleum products remain in force | [NEWS: relayed in search summary; not read at EUR-Lex this session] |

**Pre-registration grading so far:** Y1 (broad GL, sanctioned sellers on its face, to 4/7/2027) ✅ · Y2 (US import authorized at the regulation level) ✅ with the statute ⚠️ open · N1, N2 not met.

## Leg 2 — The volume, in consistent units (PARTIAL)

**What was said.** Trump, Truth Social 10/9/2026 14:46 EDT (status 117412435306815143), verbatim: *"Russia will immediately supply over 300,000 Tons of Diesel Fuel to the American and Global Marketplace, another 500,000 Tons during the month of November, and 1,000,000 Tons immediately thereafter. Additionally, based on the condition of their Diesel Refineries, Russia will then deliver, within a short period of time, 3,000,000 Tons of Diesel Fuel."* [PRIMARY: archived at trumpstruth.org/statuses/42215, captured 10/10 11:10 EDT]. **4.8 Mt is a sum made by relays, not a figure anyone stated; 3 Mt of it is conditional.** "Tons" is not specified as metric (a short-ton reading cuts every figure by 9.3%; metric assumed below, Russia's convention). The Kremlin readout gave no volume: Putin told Trump Russia was "ready to supply oil and petroleum products to the US and global markets" [NEWS: CNN via Yahoo 10/10; NBC 10/9].

**Conversions (factor 7.45 bbl/t, range 7.40–7.50; metric tonnes):**

| Tranche | Mt | M bbl | Period as stated | kb/d |
|---|---|---|---|---|
| T1 "immediately" | >0.3 | 2.24 (2.22–2.25) | unstated | — |
| T2 November | 0.5 | 3.73 | 30 days | **124** (123–125) |
| T3 "immediately thereafter" | 1.0 | 7.45 | unstated; if December only | 240; if Dec–Jan 120 |
| T4 conditional on refinery condition | 3.0 | 22.35 | "within a short period of time" | — |
| Unconditional T1–T3 | 1.8 | 13.41 | if 10/9–12/31 (83 d) | 162 |
| | | | if spread over the license (180 d) | 74.5 |
| All four | 4.8 | 35.76 (35.5–36.0) | spread over the license (180 d) | 199 |

**US side, for scale** [PRIMARY: EIA weekly via `FORGE/tools/market-data/fetch.py eia_fetch`, pulled 10/10]: US distillate imports, 10 weeks to 10/2/2026, mean **126 kb/d** (latest 118); East Coast (PADD 1) imports mean **86 kb/d** (latest 84); US distillate exports mean **1,674 kb/d** (latest 1,764). November's 124 kb/d alone would roughly match total current US distillate imports — but the US is a large net exporter, so US-bound Russian barrels mostly displace other Atlantic Basin flows (the reshuffle term in §0).

**Russia side — NOT YET ESTABLISHED (next session):** Russia's diesel export ban was imposed in July after strikes and extended to end-October [NEWS: NBC 10/9]; BRENT's docket carries the producer ban to 10/31 and the non-producer/gasoline ban to 1/31/2027 per a 7/30 decree [BRENT `docket/CATALYSTS.tsv` rows 15, 23]. CNN says the July ban "cut roughly 800,000 barrels per day" [NEWS: CNN 10/10, **no source named — UNVERIFIED**]. Novak to TASS: Russia will "immediately begin lifting" the ban [NEWS: NBC quoting TASS]; no published decree found as of 10/10 [NEWS: search summary; WALTER SIG-W-20261010-003]. ⚠️ **This is the swing term:** if the ban is lifted, the export capacity it frees could be several times the 124 kb/d November tranche — or nothing, if refineries cannot run. Pre-strike and current Russian diesel export series (Kpler/LSEG/IEA, dated) not yet in hand.

## Leg 5 — Market read on named, matched months (PARTIAL)

Crack = HO×42 − CL, same month (the basis of GATE-TERRY-VLO-HELD-01 leg A, WQ-386). Vendor: Yahoo via yfinance, pulled 10/10 11:41–11:46 ET. ⚠️ Vendor daily "close" agrees with the 14:28–14:30 ET bars (HOX26 traded 4.7361–4.7412 in the window vs a 4.7384 daily close), so it behaves as settlement, but it is **not a CME settlement file**. Vendor metadata exposed no expiry date; contract identity is by symbol only. The 10/9 daily VOLUME field is a duplicate of 10/8 (vendor defect; prices differ).

| Date | HOX26 $/gal | CLX26 | **Nov crack** | HOZ26 | CLZ26 | **Dec crack** | BZZ26 |
|---|---|---|---|---|---|---|---|
| 10/7 | 4.6227 | 88.28 | 105.87 | 4.4766 | 87.55 | 100.47 | 100.20 |
| 10/8 | 4.8829 | 91.49 | **113.59** | 4.7165 | 90.75 | **107.34** | 104.28 |
| 10/9 | 4.7384 (−2.96%) | 91.85 (+0.39%) | **107.16** (−6.43) | 4.5884 (−2.72%) | 91.01 | **101.70** (−5.64) | 104.72 |

**How much of 10/9 was this news? None of the settle-to-settle move.** CME settles HO and CL on Globex VWAP 14:28:00–14:30:00 ET [INSTITUTIONAL: CME settlement-procedure pages (CME client wiki, not the rulebook text — current version not confirmed)]. GL 135 is signed 14:43:59 EDT (per WALTER's read of the PDF properties) and the post is stamped 14:46 EDT. On 1-minute bars the news reached the tape at **14:46 ET** (HOX26 4.7292 → 4.6905 in that minute on 722 lots, after 4–67 lots a minute from 14:36 to 14:45 with price flat; no pre-announcement leak visible). The Nov crack was already 106.97 at 14:44, down from 113.59 at the 10/8 settle — that decline came during the morning and before the news; its driver is not established here.

| Window (10/9, ET) | HOX26 | CLX26 | Nov crack | Δ crack vs 14:45 |
|---|---|---|---|---|
| 14:45 (last pre-news minute) | 4.7292 | 91.56 | 107.07 | — |
| 14:50 (low area) | 4.6471 | 90.59 | 104.59 | **−2.48** |
| 16:00 bar | 4.679 | 91.66 | 104.86 | −2.21 |
| 16:30 bar | 4.6823 | 91.69 | 104.97 | −2.10 |

December crack moved alike (101.51 at 14:40 → 99.25 at 14:45 bar → 99.43 at 16:00; ≈ −$2.1). The "diesel futures fell 4%" in press reports [NEWS: CNN, NBC] matches HOX26 from the 10/8 settle to the post-settlement trade (4.883 → 4.679 = −4.2%), not the settlement (−2.96%). ⚠️ **Consequence for any rule reading settlements:** the news reaction first appears in the **Mon 10/12 settlement**, confounded with weekend events (WALTER SIG-W-20261010-002, Iran/Saudi 10/10). ICE gasoil cracks not obtained (not on this vendor).

## Legs 3 and 4 — NOT STARTED at primaries (next session)

Leg 3 (capacity offline now, terminals, tankers, transit) and leg 4 (2024–2026 outage durations): two research sub-agents were launched at 11:39 ET and **reaped unfinished** at the 11:47 PROME closeout ask; nothing from them is used here. What is in hand is WALTER's card only (SIG-W-20261010-003, BOARD, read 11:39 ET): the 10/9–10 strike hit the loading terminal of the Novoshakhtinsk refinery in Rostov-on-Don — "Yug Rusi", "NZNP Rostov" and "Novoshakhtinsk terminal" are one site (OSINT geolocation; governor did not name it); "51% of refining offline" is Ukraine's Defence Ministry saying 51% "hit" on 10/4, method unstated; independent figures are lower (Kpler via FT ~60% utilisation; IEA July >20% offline). BRENT records Novoshakhtinsk (~100 kb/d) halted 9/25 on the governor's word via Reuters [BRENT board_log 2026-09-28]. MINERVA ZEN: sailing real, cargo UNSUPPORTED (WALTER).

## Counter-Evidence (so far)

- Against "adds supply": no Russian volume or decree; T4 is conditional on refineries Ukraine says it will keep hitting; US-bound cargoes can be a reshuffle of barrels already reaching Brazil/Turkey/Africa; EU/UK bans stand; the statute question could stall US imports.
- Against "adds nothing": the license is broad and unconditional on its face; the market priced ~−$2.2/bbl on the Nov crack within the hour; lifting Russia's own ban could free volumes larger than the stated tranches.

## Process Report (session 1)

**Searches:** OFAC action pages + PDF (pdfminer), eCFR, Federal Register API, govinfo, Truth Social archive, yfinance daily/5m/1m, EIA v2, 6 web searches/fetches. **Frustrations:** congress.gov 403; CNN 451 (read via Yahoo republication); kremlin.ru fetch failed. **Gaps:** Russian export series; Novak decree; capacity-offline tally; outage base rates; CME settlement file; ICE gasoil. **Next session order:** Russia export baseline + ban instrument → capacity offline (dated, basis) → outage base rates → net-supply arithmetic against §0 → Monday 10/12 settlement read.
