# The 1984–88 Tanker War as a base rate for the 2026 Gulf tanker campaign

**Date:** 2026-10-22 | **Mode:** Thesis | **Confidence:** attack counts 1981–87 Medium · 1988 counts Low · loss and casualty ratios Medium · claims vs confirmation Medium (Iraq only) · insurance Low–Medium · exports and prices High · transit counts none found · escort effect Medium · 2026 carry-over Medium (qualitative) | **Request:** REQ-DEWEY-20261022-006 (WALTER) | **Recipients:** FALCON (action); BRENT, HAWK, SAM, RED, PROME (info)

## Key Finding

From 1981 to the end of 1987 the Tanker War logged **451 attacks on merchant ships (Iraq 283, Iran 168)**. That figure is not the whole war. About **1 attack in 41 sank a ship outright** and about **1 in 10 ended in a sinking or total loss**. Over the whole war, **23% of tankers attacked (55 of 239) were sunk or written off**. Crew deaths ran at about **0.33 per attack** (1984–87), and Iraq's communiqués claimed about **1.7–1.8× the hits that were independently counted** in 1987.

Insurers priced war risk by destination: Iran's Kharg Island terminal peaked at 7.5% of hull value, while Arab-side ports stayed at 0.375–0.75%. Gulf exports and oil prices moved far more with Saudi output policy than with attacks. US escorts made escorted ships almost immune (1 hit in 252 transits), yet total Iranian attacks roughly doubled, falling instead on unescorted ships. The sea campaign ended only when the land war ended in 1988.

The structural patterns carry over to 2026. The numerical rates do not: the 23% loss share, the ~65% claim-confirmation ratio, the 1-in-252 escort rate and the premium levels.

## Intake check

| Test | Result |
|---|---|
| Kill condition: an existing 1980–88 base-rate **table** in FALCON, BRENT or HAWK | **Not met.** I grepped FALCON, BRENT and HAWK on 2026-10-22. "Tanker war" appears only in passing mentions and in incident rows from 2026. None of them holds a count, ratio or insurance table for 1980–88. |
| Closest existing artifact | `AGENTS/BRENT/archive/research_20260321_corpus/HORMUZ_HISTORICAL_PRECEDENTS.md` (archived March 2026). It is a narrative with no count table. This report supplies that table and corrects specific claims in the file (see *Corrections*). The corrections are statements about the cited precedent only. They are not a judgement on any BRENT thesis. |
| 2026 inputs | Read only from FALCON's repo files as of 2026-10-22: `AGENTS/FALCON/domain/vessel-incidents/VESSELS.tsv` (81 data rows, data clock 2026-10-22 00:25Z), `AGENTS/FALCON/STATUS.md` (2026-10-21), and `AGENTS/FALCON/workbook/KB.tsv` and `WARRISK.tsv`. No fresh 2026 news was collected. |

## Evidence

### 1. Attacks, losses and claims

The counts all come from commercial tallies built on Lloyd's data, made while the war was still running. The best known is Ronald O'Rourke's series (*USNI Proceedings*, May 1988). It was **written before the 1988 attacks happened**. The Navy's own history makes the same point: its 283 / 168 totals are "by the end of 1987" ([NHHC H-Gram 018](https://www.history.navy.mil/content/history/nhhc/about-us/leadership/director/directors-corner/h-grams/h-gram-018/h-018-1.html), [PRIMARY]; read via summary, not directly). Every source agrees on the shape: 47–111 attacks a year in 1984–86, and a peak in 1987 of roughly 163–179. They disagree on the levels for 1984 and 1987, so Table 1a shows each source in its own column.

**Table 1a — Attacks per year by attacker. Each column is a separate source; columns are never averaged.**

| Year | O'Rourke 1988 (Iraq / Iran / total) | McCartan, *AFJ* Nov 1987 (Lloyd's + Exxon) | *Economist* 25 Apr 1987 + Lloyd's MIS | US Navy data, Iran only | Cordesman text | Sick working paper (Iraq = **communiqué claims**; Iran = gunboat attacks) |
|---|---|---|---|---|---|---|
| 1981 | 5 / 0 / 5 | — | — | — | — | — |
| 1982 | 22 / 0 / 22 | — | — | — | — | — |
| 1983 | 16 / 0 / 16 | — | — | — | — | — |
| 1984 | 53 / 18 / 71 | 53 / 18 / 71 | **36** / 18 / 54 | 17 | — | — |
| 1985 | 33 / 14 / 47 | 33 / 14 / 47 | 33 / 14 / 47 | 14 | — | — |
| 1986 | 66 / 45 / 111 | 66 / 45 / 111 (printed total "110") | 66 / **41** / 107 | 41 | ch. IX: 107 total; Iraq 65 | — |
| 1987 | 88 / 91 / 179 | to 12 Oct: 62 / 62 / 124 | Jan–Jun: 29 / 29 / 58 | 89 | ch. IX: Iraq 83 / Iran 80; ch. X: Iraq 87 / Iran 92 (and 88 elsewhere in ch. X) | Iraq **153 claimed** / Iran 93 |
| **Total through 1987** | **283 / 168 / 451** | 1984 to 12 Oct 1987: 214 / 139 / 353 | — | — | since 1984: Iraq 215 / Iran 180 | — |
| 1988 (to 20 Aug ceasefire) | not covered | not covered | not covered | **39** | by ~21 Jun 1988: Iran had hit 31 tankers, Iraq 20 | 1 Jan – 7 Aug: Iraq **74 claimed** / Iran 48 |
| Rolling year 23 Jul 1987 – 22 Jul 1988 | — | — | — | — | Center for Defense Information (CDI) data: Iraq 82 / Iran **105** / total 187 | — |

Sources: Cordesman & Wagner, *Lessons of Modern War Vol. II*, ch. IX Figs. 9.1 and 9.8, ch. X Fig. 10.1 (Sick), ch. XIV Fig. 14.3 and §14.4 ([ch. IX](https://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/media/csis/pubs/9005lessonsiraniraqii-chap09.pdf), [ch. X](https://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/media/csis/pubs/9005lessonsiraniraqii-chap10.pdf), [ch. XIV](https://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/media/csis/pubs/9005lessonsiraniraqii-chap14.pdf)) [ACADEMIC, reproducing INSTITUTIONAL tallies]. Cordesman's own warning is that "data sources are not consistent."

Three problems with the sources affect how the table should be read:
- Fig. 14.3 prints the "by Iran / by Iraq" headers swapped for 1984–86. I read it with the columns swapped back, because that is the only reading consistent with every other source.
- The [Atlantic Council](https://www.atlanticcouncil.org/in-depth-research-reports/report/what-attacks-on-shipping-mean-for-the-global-maritime-order/) also cites O'Rourke, but swaps 1982 and 1983 (16 and 22) and gives Iran 16 attacks in 1984. These are transcription differences, not independent data.
- I did not read O'Rourke's original table. USNI returned HTTP 403, so his per-year values come from Cordesman's reproduction.

**Whole-war totals.** No source I reached gives a confirmed full-year count for 1988 by attacker. Adding a 1988 increment of about 70–110 attacks to the 451 gives roughly **520–560 attacks for the whole war**. **That range is DEWEY arithmetic, not a sourced figure.** Its inputs are the 31 + 20 tanker hits by about late June, the 39 Iranian attacks in the Navy data, the 74 Iraqi claims, and the rolling-year count of 187.

Other totals in circulation measure different things and are kept separate here:
- **546 commercial vessels damaged and ~430 civilian sailors killed**, given as a Lloyd's estimate ([Wikipedia "Iran–Iraq War"](https://en.wikipedia.org/wiki/Iran%E2%80%93Iraq_War), [UNVERIFIED] relay).
- **190 ships from 31 nations attacked by Iran, with at least 63 sailors killed** ([Crist 2009, WINEP Policy Focus 95, p. 1](https://www.washingtoninstitute.org/sites/default/files/pdf/PolicyFocus95.pdf), [ACADEMIC]).
- **"411 ships attacked."** I could not trace this to any source (see *Corrections*). [UNVERIFIED]

**Table 1b — Weapon by attacker, 1984 to 12 Oct 1987** (McCartan via Cordesman Fig. 9.8 / 14.3 Pt 2) [INSTITUTIONAL]

| Attacker / year | Air-launched missiles | Bombs or rockets | Helicopter missiles | Ship-launched missiles | Small-boat gunfire, RPGs, grenades | Mines | Other or unknown | Total |
|---|---|---|---|---|---|---|---|---|
| Iraq 1984 | 35 | – | – | – | – | 2 | 16 | 53 |
| Iraq 1985 | 32 | 1 | – | – | – | – | – | 33 |
| Iraq 1986 | 52 | 5 | 1 | – | – | – | 8 | 66 |
| Iraq 1987 (to 12 Oct) | 57 | 3 | – | – | – | – | 2 | 62 |
| Iran 1984 | 18 | – | – | – | – | – | – | 18 |
| Iran 1985 | 10 | – | 3 | – | – | – | 1 | 14 |
| Iran 1986 | 9 | – | 26 | 4 | 1 | – | 5 | 45 |
| Iran 1987 (to 12 Oct) | – | – | 1 | 14 | **34** | **8** | 5 | 62 |

How to read Table 1b:
- Iraq used **air-launched missiles (mostly Exocets) in 176 of 214 attacks**, or 82%.
- Iran moved from aircraft (1984–85) to helicopters (1986) to Revolutionary Guard (IRGC) small boats and mines (1987).
- Iran's air-missile figures are printed in parentheses in the source, and the column alignment for Iran is uncertain in the PDF extraction.
- Mines were **10 of 353** attacks in this window.

**Table 1c — Losses and casualties. Each source is listed separately; none are combined.**

| Source | Scope | Sunk | Total loss / write-off | Damaged | Crew killed |
|---|---|---|---|---|---|
| O'Rourke via [Atlantic Council](https://www.atlanticcouncil.org/in-depth-research-reports/report/what-attacks-on-shipping-mean-for-the-global-maritime-order/) [INSTITUTIONAL] | 1981–87 | **11** | "**three dozen**" | 340 ships (some hit more than once) | ">320 killed, injured or missing" |
| McCartan / Lloyd's / Exxon / CDI, Cordesman Fig. 14.3 Pt 3; NHHC repeats it [INSTITUTIONAL] | 1984–87 | — | — | 340 ships | **116** killed (34 / 7 / 34 / 41 by year); 167 wounded; 37+ missing; **216 of 340 ships had no reported casualties**; 47 had no casualty data |
| Cordesman ch. IX text [ACADEMIC] | 1981–86 | — | about **17** insured total losses from attacks. Of 110 paid total losses, "all but 17" were ships trapped in the Shatt al-Arab | — | **226** deaths |
| Cordesman ch. IX text [ACADEMIC] | 1984 – end-1987 | Iraq "destroyed **49**, heavily damaged **9**"; Iran "destroyed or heavily damaged" **16** | — | — | — |
| Navias & Hooton (1996), p. 183, via [Strauss Center](https://www.strausscenter.org/strait-of-hormuz-tanker-war/) [ACADEMIC via INSTITUTIONAL] | whole war | — | **55 of 239 tankers attacked** were sunk or declared constructive total losses (CTL); bulk carriers 39%, freighters 34% | tankers = 61% of ships attacked | — |
| Navias, [*History Today*](https://www.historytoday.com/history-matters/first-tanker-war) [ACADEMIC author, popular venue] | whole war | — | — | "hundreds" | "**over 400**" seamen |
| Lloyd's Register *Casualty Returns* (via Wayback) [PRIMARY] | by the **year the loss was posted** | — | ships "claimed by" the conflict: 1984 ≈14 · 1985 11 · 1986 19 · 1987 8 · 1988 5 (≈57) | — | — |

Lloyd's Register posts a total loss in the year the write-off is decided. Its 1988 list, for example, includes ships attacked in 1984–87. It also files some attack losses under "fire/explosion". **Annual counts by posting year therefore undercount losses caused by attacks.**

**Table 1d — Ratios. The arithmetic is DEWEY's; the inputs are cited in Tables 1a–1c.**

| Ratio | Value | Basis |
|---|---|---|
| Attacks per outright sinking | **≈41** (451 / 11) | O'Rourke, 1981–87 |
| Sunk or total loss, as a share of attacks | **≈10%** (451 / ~47) | O'Rourke, 1981–87; "three dozen" is approximate |
| Tankers sunk or written off | **23%** (55 / 239), i.e. 1 in 4.3 | Navias & Hooton, whole war, per ship attacked |
| Iraqi attacks that "destroyed" a ship / "destroyed or heavily damaged" one | 23% / **27%** (49 and 58 of 215) | Cordesman, 1984–87 |
| Iranian attacks that "destroyed or heavily damaged" a ship | **9%** (16 / 180) | Cordesman, 1984–87 |
| Crew killed per attack | **≈0.33** (116 / 353) | McCartan, 1984–87. Annual *Economist* basis: 0.91 (1984), 0.34 (1985), 0.82 (1986), 0.17 (H1 1987) |
| Ships attacked with no reported casualties | **64%** (216 / 340) | McCartan, 1984–87 |
| Tankers as a share of ships attacked | **76%** (259 / 340, 1984–87) vs **61%** (whole war) | McCartan vs Navias & Hooton |
| Size effect, Exocet strikes in 1984 | **0 of 17** tankers over 50,000 t sunk (11 significant damage, 6 slight) vs **7 of 33** smaller ships sunk (21%), with 19 heavily damaged | Pengelly, *IDR* 3/1987, via Cordesman ch. XIV [INSTITUTIONAL] |
| Traffic denominator, early 1987 | 168–196 tankers a month moved through the Gulf; Kuwait received 70–80 a month | Cordesman ch. IX |

Ship-kill rates range from about 10% to 23–27%. They depend on the denominator (attacks vs ships attacked), the scope (1981–87 vs the whole war), the ship type (tankers vs all ships) and the attacker (Iraq's Exocets vs Iran's boats and light missiles).

Large tankers that were lost were usually not sunk. They burned after engine-room hits (HAWAII 1986, FAIRSHIP L. 1985) or were storage and shuttle hulls caught in concentrated air raids at Kharg and Larak (BARCELONA 1988; SEAWISE GIANT damaged at Larak) (Lloyd's Register *Casualty Returns*, [PRIMARY]). Navias & Hooton add that Iran's Maverick and AS-12 missiles caused "little physical damage to ships", but that hits on accommodation blocks killed crew ([Strauss](https://www.strausscenter.org/strait-of-hormuz-tanker-war/)).

**Table 1e — Belligerent claims vs confirmed hits** (Cordesman chs. IX, X; Iraqi communiqués via Gary Sick) [ACADEMIC; the underlying claims are PRIMARY]

| Window | Claimed (Iraq) | Confirmed | Ratio | Note |
|---|---|---|---|---|
| Full year 1987 | 153 | 88 (O'Rourke) / 87 (ch. X) / 83 (ch. IX) | **1.74× / 1.76× / 1.84×** | The claims include offshore oil terminals, so the ratio somewhat overstates over-claiming against ships |
| Full year 1987, footnote reading | 153 | "99 confirmed hits" | 1.55× (≈65% confirmed) | Sick's footnote is ambiguous. It may mean 99 of 153 claims were verified, or it may be Iraq's own "confirmed" figure |
| 21 Oct – 4 Nov 1987 | 3 Iranian tankers claimed hit on 28 Oct | 0 successful attacks | phantom claims | One "supertanker hit" was probably a decoy hulk |
| 2nd week of Nov 1987 | 11 | ≤3 | **≥3.7×** | |
| 9–15 Nov 1987 | 15 | 3 | **5×** | |
| 8–20 Nov 1987 | 21 | 4 | **5.25×** | |
| 1 Jan – 8 Mar 1988 | 23 | 9 (confirmed by shipping companies) | **2.6×** | After 8 Mar, "most of its strikes were confirmed" |
| 1 Jan – 7 Aug 1988 | 74 | no full-year confirmed count | — | Iraq ~20 tanker hits by ~late June |
| Iran, any period | **no quantified Iranian claims series found** | — | — | Sick's Iran column (93 in 1987) counts gunboat attacks, not claims |

Cordesman attributes the over-claiming partly to propaganda and partly to genuine misidentification: Iraq had no adequate maritime patrol aircraft, attacked at night, and Iran used decoys and radar reflectors.

### 2. War-risk insurance

**Table 2 — Additional hull war-risk premium, % of hull value per voyage unless stated**

| Date | Destination | Level or change | Source |
|---|---|---|---|
| Sep 1980 | Cargo bound for Iran or Iraq | cargo premiums **+300%** | Navias & Hooton via [Strauss](https://www.strausscenter.org/strait-of-hormuz-insurance-market/) [INSTITUTIONAL] |
| Early 1984 | Kharg | doubled | same |
| **May 1984** | **Kharg** | **7.5%** (peak) | same. This figure has a **single source lineage**. 2026 retrospectives such as [tankerbrief.com](https://tankerbrief.com/deep-dives/insurance-weapon) repeat it [UNVERIFIED] |
| 1984 | Iranian loading ports | premiums up, creating "a price differential for tankers loading within Gulf ports" | [UNCTAD RMT 1984 ¶30](https://unctad.org/system/files/official-document/rmt1984_en.pdf) [PRIMARY] |
| Jan 1985 / May 1985 | Gulf hull rates | halved / doubled again | Strauss [INSTITUTIONAL] |
| Dec 1986 | Shuttle tanker on a six-month charter | war premiums reach "60 percent of the value of a vessel" (cumulative over six months) | Lloyd's List via [CSM, 4 Dec 1986](https://csmonitor.com/1986/1204/aship.html) [NEWS] |
| 3 Feb 1987 | Kuwait-bound | doubled, to **0.375%** | [MEES, 9 Feb 1987](https://archives.mees.com/issues/1267/articles/44207) [INSTITUTIONAL] |
| Early Sep 1987 | Gulf | **+50%** after 20 ships were hit 27 Aug – 3 Sep | Cordesman ch. IX [ACADEMIC] |
| Feb 1988 | Lloyd's Gulf rate | **0.75% → 0.45%** | Cordesman ch. IX [ACADEMIC] |
| After Aug 1988 | Commercial shipping | "approaching pre-war levels" | Cordesman ch. X [ACADEMIC] |

War cover was **repriced, never withdrawn**. None of the sources reached reports a market-wide withdrawal. That is an absence of evidence, not a documented fact.

The market priced the belligerent's terminal rather than "the Gulf". Kharg's 7.5% in 1984 and the Arab-side 0.375–0.75% in 1987–88 are roughly 10–20× apart. That multiple is my inference from figures in different years; I found no single-date side-by-side table.

**Iran carried most of the cost of keeping its buyers:**
- It offered "compensatory price discounts" in May 1984 and "further major oil discounts" after the Sirri raid in August 1986 (Cordesman chs. VII, VIII). The size of the discount per barrel was not found.
- Its shuttle charters cost about **$60M a year plus $20,000 per tanker per day** in 1986 (ch. VIII).
- It insured hulls itself, but "for only 15 percent of their value" ([CSM](https://csmonitor.com/1986/1204/aship.html)).

Claims over the whole war totalled about **$2B, half of it on the Lloyd's market** (Strauss). By mid-1987 the figure was $1.5B, most of it for the ships trapped in the Shatt al-Arab. **I found no dated record of Lloyd's or Joint War Committee listed areas for 1984–88.**

### 3. Traffic, exports and price

**Table 3a — Crude exports, kb/d** ([EIA international bulk data](https://www.eia.gov/opendata/bulk/INTL.zip), series `INTL.57-4-<ISO>-TBPD.A`, downloaded 2026-10-22) [PRIMARY]

| Year | Iran | Iraq | Saudi | Kuwait | UAE | Qatar | Gulf-6 | Gulf-6 share of world |
|---|---|---|---|---|---|---|---|---|
| 1983 | 1,811 | 686 | 4,045 | 544 | 1,057 | 273 | 8,416 | 37.6% |
| 1984 | 1,512 | 844 | 3,458 | 658 | 979 | 340 | 7,791 | 34.6% |
| 1985 | 1,545 | 1,059 | 2,243 | 476 | 910 | 279 | 6,512 | 30.8% |
| 1986 | 1,454 | 1,344 | 3,549 | 756 | 1,050 | 304 | 8,457 | 35.9% |
| 1987 | 1,710 | 1,717 | 2,595 | 607 | 1,162 | 234 | 8,025 | 34.8% |
| 1988 | 1,762 | 2,095 | 3,283 | 698 | 1,245 | 258 | 9,341 | 37.6% |

Caveats on Table 3a:
- These are country exports, **not seaborne flows through Hormuz**.
- Iraq's exports went by pipeline through Turkey, and through Saudi Arabia from September 1985.
- Kuwait's series looks low next to its production.
- An alternative Iranian export series (Wharton/PFC/Roberts via Cordesman ch. VII) gives 1.36 (1984), 1.8 (1985) and 1.5 (1986) mb/d. It conflicts with EIA in level, but both series agree on direction.

**Table 3b — Escalation dips in the attacked exporter (EIA monthly crude production, kb/d) [PRIMARY], with narrative [ACADEMIC]**

| Window | Iran | Arab-side | Reading |
|---|---|---|---|
| Apr → May → Jun 1984 | 2,300 → **1,800** → 2,300 (−22%) | Saudi and Kuwait flat | Exports fell "up to fifty percent for a few days", then "quickly recovered" (ch. VII) |
| Jul → Aug 1984 | 2,500 → 1,800 | Saudi decline is the OPEC-cut trend | A one-month dip |
| Jul → Sep/Oct 1986 | 2,220 → **1,625** (−27%), back to 2,166 by Dec | Saudi and Kuwait drops are the OPEC cut | Exports ~1.6 → 1.1 mb/d, with daily lows near 0.8 mb/d, after the Sirri and Kharg raids (ch. VIII) |
| Aug → Sep 1987 | 2,558 → **1,989** (−22%), back to 2,273 in Oct | Kuwait flat | A one-month dip |

Monthly figures from the 1980s are coarse, so treat them as order-of-magnitude.

The largest swing among Gulf exporters was **policy, not war**. Saudi exports fell 35% in 1985 and rose 58% in 1986. Iraq, shut out of the Gulf, tripled its exports by pipeline (**686 → 2,095 kb/d, 1983 → 1988**; [Cordesman ch. VI](https://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/media/csis/pubs/9005lessonsiraniraqii-chap06.pdf), [ch. VII](https://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/media/csis/pubs/9005lessonsiraniraqii-chap07.pdf)). Kuwait's exports rose from about 970 to about 1,200 kb/d during the escort winter of 1987–88 (ch. IX). **I found no measured series of tanker transits or port calls** for Hormuz in 1983–88.

**Table 3c — Prices** (monthly: [World Bank Pink Sheet](https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/related/CMO-Historical-Data-Monthly.xlsx); daily: [FRED DCOILBRENTEU](https://fred.stlouisfed.org/series/DCOILBRENTEU), whose first observation is 1987-05-20) [PRIMARY]

| Event | Brent, $/bbl | Move |
|---|---|---|
| May 1984 escalation (Kharg; tankers hit 13–16 May) | monthly: 30.13 (Apr) → 29.90 (May) → 27.91 (Jul) | flat to down. Cordesman: "little movement even in the usually sensitive spot market" (glut, full stocks) |
| Saudi output ramp, Dec 1985 → Jul 1986 | **25.85 → 9.45** (Dubai 26.30 → 7.85) | **−63%**. Attributed to Saudi Arabia abandoning restraint ([Hamilton, NBER WP 16790, p. 17](https://www.nber.org/system/files/working_papers/w16790/w16790.pdf) [ACADEMIC]) |
| Bridgeton mine, 24 Jul 1987 | 20.15 → 19.58 | **−2.8%** on the day; range 19.25–20.95 over the following three weeks |
| Worst attack week, 27 Aug – 3 Sep 1987 | Sep average 18.31 | kept falling |
| Praying Mantis, 18 Apr 1988 | 8 Apr 15.55 · 14 Apr 16.65 · 15 Apr 16.85 · **18 Apr 17.45** · 2 May 15.95 | **+3.6%** on the day (vs 15 Apr); +4.8% from 14 Apr; +12.2% from 8 Apr; −8.6% by 2 May |
| Iran's letter accepting UN Resolution 598, 17 Jul 1988 | 15 Jul 14.25 → 18 Jul 15.00 → 22 Jul 15.83 | **+5.3%** in the first session, +11% in a week: an *up* move on peace |
| Ceasefire announced 8 Aug, effective 20 Aug 1988 | 15.48 → 15.03 | no unwind of a war premium visible |
| Post-war low | **11.20 on 5 Oct 1988** | lowest daily close, May 1987 – Dec 1988 |

**War-risk freight did not dominate either.** Very large crude carrier (VLCC) rates from the Gulf to West Europe ran at Worldscale (WS) 32 (Jan 1988) → 65 (Dec 1988), rising *after* the ceasefire ([UNCTAD RMT 1988 ¶57](https://unctad.org/system/files/official-document/rmt1988_en.pdf)). Christian Science Monitor, citing the trade press: "the market is so glutted that the war is only of marginal help."

### 4. Escorts (Earnest Will, July 1987 – 1988) and how the campaign ended

**Table 4a — Attack rates before and during the escort phase** (CDI and US Navy data via Cordesman ch. XIV; Sick series via ch. X) [ACADEMIC]

| Window | Iraq per month | Iran per month | Basis |
|---|---|---|---|
| 1984 / 1985 / 1986 | 4.4 / 2.8 / 5.5 | 1.5 / 1.2 / 3.8 | O'Rourke annual ÷ 12 |
| 22 Jul 1986 – Jul 1987 (year before reflagging) | 5.2 (63/yr) | 4.5 (**54/yr**) | CDI |
| 23 Jul 1987 – 22 Jul 1988 (first escort year) | 6.8 (82/yr) | 8.8 (**105/yr**) | CDI: "Iranian strikes nearly doubled" |
| 1 Jan – 15 Jul 1987 (before escorts) | 6.3 (claims) | **5.7** | Sick |
| 1 Aug 1987 – 15 Apr 1988 | — | **9.8** | Sick |
| ↳ Sep–Dec 1987 peak | 28.0 (claims) | 12.8 | Sick |
| 16 Apr – 15 Jul 1988 (after Praying Mantis) | 8.0 (claims) | **6.0** | Sick |
| Escorted ships | **1 hit in 252 escorted or accompanied transits** (*Bridgeton*, a mine, 24 Jul 1987, on the first convoy). The 252 were 177 reflagged-tanker transits, 57 Military Sealift Command, 14 other US-flag and 4 foreign-flag | — | US Navy data, Cordesman ch. XIV |
| Iranian attacks on Saudi-bound shipping, cumulative | — | 7 (Aug 1987) → 16 → 22 → 26 → **38 (Dec 1987)** | Cordesman ch. IX |

Escort coverage was thin:
- In August 1987 "six out of every seven tankers moved on its own".
- Only one of the eleven reflagged hulls carried crude.
- Only 18 one-way convoys had run by the end of November 1987, against a goal of 10 a month.

Iran "avoided Western escorted ships". In 1987, **73 of its 80 attacks hit Kuwait- or Saudi-linked traffic**, and 72% fell between the UAE and Abu Musa (Cordesman chs. IX, X). US intelligence had predicted this order of Iranian responses: first more attacks on unescorted ships, then mining, then terrorism, and only after that attacks on escorts and warships ([Crist 2009, p. 3](https://www.washingtoninstitute.org/sites/default/files/pdf/PolicyFocus95.pdf)).

**Iraq's surge in the escort year was not caused by the escorts.** It followed Iraq's own pause on Gulf strikes (20 Jul – 29 Aug 1987, with zero claims in August) and the collapse of the Resolution 598 diplomacy.

**Mining.** After the *Iran Ajr* was captured on 21 Sep 1987, Iran laid no more mines for about six months (Crist).

**After Praying Mantis**, Iranian gunboat attacks fell from 9.8 to 6.0 a month. Iran also lost al-Faw (17–18 Apr 1988), Majnoon and the central front over the same weeks, so the fall **cannot be attributed to naval pressure alone**.

**Table 4b — What ended it**

| Factor | Evidence | Source |
|---|---|---|
| Collapse on land, Apr–Jul 1988 | Iraq retook al-Faw in ~48 hours, with chemical weapons; Iran was driven back to the border by June | Cordesman ch. X; Crist 2009 [ACADEMIC] |
| Economic exhaustion | oil revenue **$20B (1982) → $5B (1988)**; Iran "nearly bankrupt" | Razoux via [Wikipedia](https://en.wikipedia.org/wiki/Iran%E2%80%93Iraq_War) [UNVERIFIED]; Cordesman ch. X |
| Fear of chemical weapons and of renewed missile attacks on cities | named alongside Iraq's victories and the threat of Western naval power | Cordesman ch. X |
| Naval pressure, as a contributing factor | Praying Mantis and the Vincennes shoot-down (3 Jul 1988, 290 killed). Rafsanjani, 19 Apr 1988: "Time is not on our side anymore" | Crist 2009; Cordesman chs. X, XIV |
| Formal end | Iran's letter of 17 Jul 1988; ceasefire effective **20 Aug 1988, 03:00 GMT**; Iran did not challenge shipping afterwards | [UN UNIIMOG](https://peacekeeping.un.org/en/mission/past/uniimogbackgr.html) [PRIMARY]; Cordesman ch. X |

Cordesman concludes that Iran learned it "could never succeed in forcing a partial cease-fire that ended the war at sea without accept[ing] a cease-fire on the land." **The sea campaign ended because the land war ended.** No source credits the escorts or Praying Mantis with ending it on their own.

### 5. What carries over to 2026

The 2026 figures below come from FALCON's ledger and STATUS as of 2026-10-22 and 2026-10-21. FALCON's header calls its backfill before 12 July "KNOWN-THIN", so **all ledger counts are lower bounds**. The ledger has **no field for escorted vs unescorted ships**.

Of the 81 rows:
- 11 are US-caused;
- 10 are claims only, duplicates, unresolved or disputed;
- 60 are non-US event rows, of which 48 involve tankers or gas carriers.

The "≥10 attacks in the week to 10/17" figure is **relayed: FALCON STATUS says no UKMTO text was located**. The ledger itself holds 14 non-US hull rows dated 11–17 Oct, but I have not removed possible duplicates.

**Table 5 — Carry-over**

| 1984–88 pattern | 1980s value | 2026 analogue (FALCON, as-of) | Carries? |
|---|---|---|---|
| Belligerents over-claim | Iraq ~1.7–1.8× for the year; 3.7–5× in bursts | 5 CLAIM_ONLY rows plus unlogged IRGC claims (31 Jul, 6 Sep, 17 and 20 Oct). Joint Maritime Information Center (JMIC): "no substantiation" | **YES (pattern)** |
| Stand-off weapons rarely sink large tankers | 1984 Exocets: 0 of 17 tankers over 50,000 t sunk | 0 tankers sunk by non-US fire across 48 non-US tanker and gas-carrier rows | **YES** |
| Few deaths per attack | ≈0.33 killed per attack; 64% of ships had no casualties | IMO: 24 seafarer deaths / 119 incidents, as at 21 Oct (relayed via FALCON STATUS; IMO's definition of "incident" not checked) | **YES (direction only)** |
| Attacks cluster at the attacker's chokepoints | over one-third of Iran's attacks within 50 nm of its platforms; 72% between the UAE and Abu Musa | 46 HORMUZ + 11 GULF_OF_OMAN of 81 rows | **YES** |
| Escorting some ships pushes attacks onto the rest | Iran 54 → 105/yr; Saudi-bound 7 → 38 | not testable: no escort field in the ledger | **Plausibly YES** |
| The sea campaign ends with the wider war | ceasefire 20 Aug 1988; no attacks on shipping afterwards | no dated framework; Iran–Oman corridor coordinates agreed 7 Oct | **Plausibly YES** (FALCON and HAWK own this call) |
| 23% of tankers sunk or written off | Navias & Hooton, whole war | 0 sinkings of 48. "Written off" is not tracked the same way. Confirmed non-US total losses: a dhow and the container ship GFS PRIDE; CAPE DAO is contested | **UNSAFE.** Different measure, different weapons, and a numerator of 0–2 |
| ~65% of claims confirmed | 99 / 153 (1987) | claims now come from IRGC media and Telegram, with neutral reporting (UKMTO, JMIC, AIS) alongside. FALCON's `attacker_axis` column (DEWEY tally of `AGENTS/FALCON/domain/vessel-incidents/VESSELS.tsv`, 81 rows, 2026-10-22) has 44 rows coded exactly UNATTRIBUTED and 8 more with an annotated UNATTRIBUTED/UNKNOWN value. That makes **52 of 81 incidents with no established attacker**: hits that nobody has claimed | **UNSAFE** |
| 1 escorted ship hit in 252 transits | Bridgeton only | the US is now a belligerent (strikes on Iran, a blockade); shore-launched missiles and drones can reach convoys; the IRGC names escorts as targets | **UNSAFE** |
| War-risk premium levels | Arab side 0.375–0.75%; Kharg only, 7.5% peak (1984) | Hormuz **6–10% of hull** (FT brokers ~6 Oct, second-hand) and 7.5–10% (Marsh/Platts, 22 Jul). Source: FALCON STATUS and WARRISK, all 5 rows EXPIRED, no quote after 11 Oct | **UNSAFE.** The 1980s rate was set per destination; the 2026 quote is priced across the whole chokepoint; the premium basis is not confirmed |
| Iran's restraint toward US-flag ships | Iran kept attacks deniable to avoid war with the US (Crist p. 13) | that threshold has already been crossed | **UNSAFE** |
| Iran needs the strait open for its own exports | Iran's Gulf exports were 40% higher in 1987 than 1986 (Cordesman) | Iran's exports are under US blockade; Kharg loadings halted 18 Jul – 12 Aug | **UNSAFE.** The brake is weakened (inference, not a sourced claim) |

## Corrections to circulating figures

| Claim | Where it circulates | What the sources show |
|---|---|---|
| "451 attacks (Iraq 283, Iran 168)" as the whole-war total (1981 – Aug 1988) | [Wikipedia "Tanker war"](https://en.wikipedia.org/wiki/Tanker_war) and secondary sources | It covers **1981 to end-1987 only**: O'Rourke's article dates from May 1988, and NHHC says "by the end of 1987". No confirmed full-year count for 1988 was found. |
| "411 ships were attacked … 239 (roughly 61%) were petroleum tankers" | BRENT archive file, line 9 | **Untraced.** 239 / 411 = 58%, not 61%. Navias & Hooton's 239 at 61% implies ~390 ships (DEWEY arithmetic). [UNVERIFIED] |
| "initial drop of approximately 25%" in commercial shipping "in 1984" | BRENT archive file, line 9 | The source is Blair & Lieberthal (*Foreign Affairs*, 2007), via Strauss. Their sentence says "Initially …", names no year and cites no data. The "1984" was added. No measured transit series exists in the sources reached. |
| Praying Mantis "temporarily spiked prices by 10.7%" | BRENT archive file, line 16 | On FRED Brent: **+3.6% on the day**, +4.8% from 14 to 18 Apr, and +12.2% from 8 to 18 Apr (mostly before the 14 Apr mining). 10.7% does not reproduce on any of these windows. |
| Earnest Will "effectively nullified the asymmetric threats" / "deterred widespread, systematic attacks" | BRENT archive file, lines 16 and 74 | Escorted ships were nearly immune (1 hit in 252 transits), but **Iranian attacks overall rose from 54 to 105 a year** and moved onto unescorted ships. |
| Ceasefire "enacted on August 8, 1988" | BRENT archive file, line 16 | Announced 8 Aug; **took effect 20 Aug 1988** (UN). |
| Iran accepted Resolution 598 on 20 Jul 1988 | Wikipedia | Iran's letter is dated **17 Jul**. 20 Jul is the date of Khomeini's "poisoned chalice" speech. |
| A Gulf-wide war-risk peak of 7.5% | 2026 retrospectives | The 7.5% applied to **Kharg** in May 1984 and has a single source lineage. Arab-side rates were 0.375–0.75%. |

## Counter-Evidence

- **Escort effect.** Cordesman argues that Iran "would have made even greater increases" without the US presence, and the IRGC Navy was growing regardless. These data cannot separate the "escorts provoked more attacks" reading from the "escorts capped a larger rise" reading. Cordesman's interview-based ch. XIV also says the US presence had "a major impact in forcing Iran to accept a ceasefire". That cuts against a purely land-war explanation.
- **The "2% of ships" figure.** Using Cordesman's early-1987 denominator (168–196 tankers a month), the 125 tanker attacks in 1987 (McCartan) would be about **5–6% of tanker movements**. This is DEWEY arithmetic on mismatched bases. The "2%" figure probably uses a broader all-ship denominator, and the question is unresolved.
- **Spread of the loss rate.** The 10% (O'Rourke), 23% (Navias & Hooton, tankers) and 27% (Cordesman, Iraqi attacks) figures differ by 2–3×. Any single "attacks per loss" figure depends on its basis. One unsourced hypothesis: in the 1980s glut, low hull values made it easier to declare a damaged ship an economic write-off, which would inflate the share of ships written off. [UNSOURCED]
- **Why prices barely moved.** The weak price response came during a glut with full stocks and large Saudi spare capacity (Cordesman ch. VII; Hamilton). It is not evidence that tanker attacks are price-neutral in general.
- **"2026 is categorically different."** Several 1980s features recur: a small-boat RPG attack (LOYALTY, 16 Oct 2026), mine *threats*, Kuwait- and Saudi-linked hulls among the targets (AL DASMA is the third Kuwaiti hull since 28 Sep), and stand-off weapons failing to sink large tankers.

## Unknowns

- No confirmed count of attacks by attacker for the whole of 1988. The whole-war 520–560 range is arithmetic.
- O'Rourke's original table and the appendix tables in Navias & Hooton (1996) were not read. Neither was El-Shazly (1998).
- No split of sunk vs written off vs damaged by attacker and year for 1981–88. No whole-war crew-death figure on one consistent basis: estimates run 116 (1984–87) and 226 (1981–86) up to about 430 and "over 400".
- No series of Iranian claims. Sick's "99 confirmed hits" footnote is ambiguous.
- No transit or port-call series for Hormuz or Gulf ports in 1983–88.
- No Lloyd's or Joint War Committee listed-area dates for 1984–88. The premium basis (per voyage or annual) is not confirmed. No baseline rate for Kharg before the escalation.
- The size of Iran's oil discount per barrel. The timing of OPEC decisions around the August 1986 and July 1988 price moves.
- 2026: IMO's definition of "incident"; escorted transit counts; any hits on escorted ships.

## Source Quality Assessment

The spine of this report is Cordesman & Wagner (CSIS, 1990), read in full. It compiles contemporaneous Lloyd's, Exxon, CDI and US Navy data with Gary Sick's communiqué series. It is reliable on direction and order of magnitude, but it is internally inconsistent: it gives Iran's 1987 attacks as 80, 88, 89, 91, 92 or 93 depending on the chapter and figure, and one figure has its column headers swapped.

Navias & Hooton, the source of the 23% tanker loss share and all the insurance levels, reached this report only through the Strauss Center, so those figures carry **one secondary lineage**.

The prices and exports are primary and reproducible: EIA, the World Bank, FRED and UNCTAD.

The Lloyd's Register *Casualty Returns* are primary but are OCR'd scans from Wayback, and they count by posting year.

The Wikipedia relays (546 vessels, ~430 killed, $20B → $5B oil revenue) are tagged [UNVERIFIED].

The 2026 side relies on FALCON's ledger, which is by its own account a lower bound.

## References

All accessed 2026-10-22.

- Cordesman & Wagner, *The Lessons of Modern War Vol. II: The Iran-Iraq War* (CSIS/Westview, 1990), chapters [V](https://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/media/csis/pubs/9005lessonsiraniraqii-chap05.pdf), [VI](https://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/media/csis/pubs/9005lessonsiraniraqii-chap06.pdf), [VII](https://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/media/csis/pubs/9005lessonsiraniraqii-chap07.pdf), [VIII](https://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/media/csis/pubs/9005lessonsiraniraqii-chap08.pdf), [IX](https://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/media/csis/pubs/9005lessonsiraniraqii-chap09.pdf), [X](https://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/media/csis/pubs/9005lessonsiraniraqii-chap10.pdf), [XIV](https://csis-website-prod.s3.amazonaws.com/s3fs-public/legacy_files/files/media/csis/pubs/9005lessonsiraniraqii-chap14.pdf). These chapters reproduce O'Rourke (*Proceedings*, May 1988, pp. 31–32), McCartan (*AFJ*, Nov 1987), the *Economist* (25 Apr 1987), Pengelly (*IDR* 3/1987) and Sick's working paper.
- Crist, *Gulf of Conflict*, WINEP Policy Focus 95 (2009): https://www.washingtoninstitute.org/sites/default/files/pdf/PolicyFocus95.pdf
- Strauss Center, "Tanker War": https://www.strausscenter.org/strait-of-hormuz-tanker-war/ · "Insurance market": https://www.strausscenter.org/strait-of-hormuz-insurance-market/
- NHHC H-Gram 018 (summary only; not read directly): https://www.history.navy.mil/content/history/nhhc/about-us/leadership/director/directors-corner/h-grams/h-gram-018/h-018-1.html
- Atlantic Council: https://www.atlanticcouncil.org/in-depth-research-reports/report/what-attacks-on-shipping-mean-for-the-global-maritime-order/
- Navias, *History Today*: https://www.historytoday.com/history-matters/first-tanker-war
- Lloyd's List, 14 Jun 2019: https://www.lloydslist.com/LL1127899/Tanker-attacks-Establish-the-facts-and-clarify-the-responsibilities-in-Hormuz · 11 Mar 2026: https://www.lloydslist.com/LL1156586/Gulf-war-risk-premiums-topping-double-digit-millions-of-dollars-per-trip
- Lloyd's Register *Casualty Returns* 1981–88: `lloyds-production.s3.amazonaws.com/_file/general/<YYYY>-casualty-returns.pdf`, retrieved via `web.archive.org/web/2020id_/<url>`
- Christian Science Monitor, 4 Dec 1986: https://csmonitor.com/1986/1204/aship.html
- MEES, 9 Feb 1987: https://archives.mees.com/issues/1267/articles/44207
- INTERTANKO history 1984–87: https://intertanko.com/history-1984-1987
- UNCTAD *Review of Maritime Transport* 1984–88: https://unctad.org/system/files/official-document/rmt1984_en.pdf (same pattern for rmt1985 to rmt1988)
- EIA international bulk data: https://www.eia.gov/opendata/bulk/INTL.zip
- World Bank Pink Sheet (monthly): https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/related/CMO-Historical-Data-Monthly.xlsx
- FRED: https://fred.stlouisfed.org/series/DCOILBRENTEU · https://fred.stlouisfed.org/series/WTISPLC
- Hamilton, "Historical Oil Shocks", NBER WP 16790: https://www.nber.org/system/files/working_papers/w16790/w16790.pdf
- UN UNIIMOG background: https://peacekeeping.un.org/en/mission/past/uniimogbackgr.html
- IMO on AIS: https://www.imo.org/en/OurWork/Safety/Pages/AIS.aspx
- Wikipedia (relays only, [UNVERIFIED]): https://en.wikipedia.org/wiki/Tanker_war · https://en.wikipedia.org/wiki/Iran%E2%80%93Iraq_War · https://en.wikipedia.org/wiki/Operation_Earnest_Will
- Fleet artifacts: `AGENTS/FALCON/domain/vessel-incidents/VESSELS.tsv`; `AGENTS/FALCON/STATUS.md`; `AGENTS/FALCON/workbook/KB.tsv` (KB-FALCON-020, 128, 142, 311); `AGENTS/FALCON/workbook/WARRISK.tsv`; `AGENTS/BRENT/archive/research_20260321_corpus/HORMUZ_HISTORICAL_PRECEDENTS.md`

**Reproduction recipe:**
- Daily Brent: `python3 AGENTS/DEWEY/scripts/fred_pull.py DCOILBRENTEU --start 1987-05-01 --csv`.
- Monthly WTI: `fred_pull.py WTISPLC --start 1983-01-01 --csv`.
- Exports and production: EIA `INTL.zip`, series `INTL.57-4-{IRN,IRQ,SAU,KWT,ARE,QAT,WORL}-TBPD.A` and `INTL.57-1-*-TBPD.{A,M}`.
- Cordesman chapters: the CSIS PDFs above, run through `pdftotext -layout`.
- UNCTAD PDFs: these need a browser User-Agent.

## Process Report

- **DEWEY verification and provenance:**
  - DEWEY ran the kill-condition grep itself (FALCON, BRENT, HAWK). BRENT's archived narrative was found and has no count table.
  - DEWEY re-tallied FALCON's `attacker_axis` column (81 rows): 44 exact UNATTRIBUTED plus 8 annotated variants. The carry-over table was corrected from 44 to 52 of 81.
  - Three Opus legs ran in data-return mode. A report-writer sub-agent drafted this report; DEWEY reviewed it before filing.
- **Searches run:** The **session-wide WebSearch cap was exhausted early**: the insurance leg got 4 searches and the escort leg got none. The three legs therefore worked from direct fetches of known sources.
  - **Read in full:** the Cordesman & Wagner CSIS chapters (V–X, XIV), Crist 2009 (WINEP), EIA bulk data, the World Bank Pink Sheet, FRED, UNCTAD RMT 1984–88, and Lloyd's Register *Casualty Returns* (via Wayback).
  - **Not read directly:** O'Rourke (USNI returned 403), Navias & Hooton, Palmer (1992), Crist's *Twilight War* (2012), the USNI originals and NHHC (404 to scripted requests). Their figures arrive through Cordesman, Strauss or Wikipedia relays.
- **Data gaps:**
  - a confirmed count of 1988 attacks by attacker;
  - losses by attacker and year;
  - an Iranian claims series;
  - a Hormuz transit or port-call series;
  - Lloyd's or Joint War Committee listed-area dates and the premium basis;
  - Iran's per-barrel discount;
  - OPEC decision timing;
  - 2026 escort data.
- **Source frustrations:**
  - USNI 403; NHHC 404 to scripts;
  - Lloyd's Register S3 objects return "AllAccessDisabled", so Wayback was needed, and the OCR is noisy;
  - UNCTAD returns 403 to a bare curl;
  - MEES is paywalled after the lead;
  - FRED Brent starts 1987-05-20, so 1984–86 is monthly only;
  - Cordesman's figures are internally inconsistent, and one has its headers swapped.
- **Confidence in findings:**
  - Medium on the counts and ratios for 1981–87: several Lloyd's-based tallies agree within about 10% on most years.
  - Low on 1988.
  - Medium on the Iraqi claims ratio, which rests on one series and an ambiguous footnote.
  - Low–Medium on insurance, which has a single secondary lineage.
  - High on exports and prices, which are primary and reproducible.
  - Medium on the escort effect: two independent series agree on direction.
  - The carry-over judgements are qualitative.
- **If I had more time/tools:**
  - Get Navias & Hooton (1996) and O'Rourke (1988) in full.
  - Parse the 1984–86 Lloyd's Register Part 3 lists of "Ships reported damaged and/or delayed in the region of the Iran-Iraq war" into an annual primary table of damaged ships.
  - Pull MEES for Iran's discounts and the OPEC timeline.
  - Find a Lloyd's Maritime Information Services transit series.
- **Suggestions:**
  - Add a Lloyd's Register *Casualty Returns* Wayback helper to `scripts/`, with OCR clean-up.
  - Log USNI and NHHC scripted-access blocks, and the UNCTAD User-Agent requirement, in `scripts/BACKLOG.md`.
  - An escorted/unescorted field in FALCON's ledger would let the 1987 displacement pattern and the US-intelligence response ranking be tested against 2026. This is a suggestion only, not an action item.
