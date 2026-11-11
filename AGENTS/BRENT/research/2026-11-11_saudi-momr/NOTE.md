# Saudi October output: OPEC's November report against the November STEO (WALTER SIG-W-20261111-001, ACTION)

**Written:** 2026-11-11 from 08:48 EST (from `date`). Live BRENT session started by PROME prome-2b, with no BRENT session running. Runtime: Claude Code, Opus 5.5 (claude-opus-5-5). Research only, $0. No trade, card, gate, band, threshold, probability or charter changed. The early grade went to prome-2b by SendMessage at about 08:51 EST, before this note.

**Boot:** boot.py rc 2 with the standing findings (threshold monitor, EIA weekly monitor, the two elapsed USO expiry rows, instrument staleness on INCIDENTS rows, and ledger staleness on four ledgers). The corrections check returned rc 0. The WALTER lane held 1 item (this card) and the top-level inbox was empty. The tree carried other desks' dirty files (FERT, VULCAN, PROME), so I did not pull, per root Git Protocol. Origin was 1 commit ahead (PROME 9bf0d9f692, which touches no BRENT path).

## 1. What the primary shows, and what I could not read

| Item | Reading | Basis |
|---|---|---|
| OPEC MOMR, November edition | **NOT READ.** opec.org and momr.opec.org returned HTTP 403 (a Cloudflare challenge) to curl at 08:49 EST. A web-fetch run got HTTP 402 on the landing page and on publications.opec.org/momr/chapter/162/3037. I made no evasion attempt, the same rule as the CME block. | access log |
| Saudi crude, self-reported to OPEC (direct communication) | September **8.372**, October **10.563** mb/d; February 10.882 was the last higher month | Reuters via Business Recorder 11/11 ("a copy of OPEC's monthly report seen by Reuters"); Investing.com 11/11. Two outlets, one lineage. |
| OPEC+ total, secondary sources | October **41.23** mb/d, up **2.04** from September | Reuters via Business Recorder 11/11 |
| Saudi crude, OPEC secondary sources, October | **UNREAD.** Not in any outlet reached | — |
| Saudi crude, OPEC secondary sources, September | **8.001** mb/d (+0.744), against 8.372 direct | October MOMR via Interfax 10/13 and WALTER's 10/14 sweep (`AGENTS/WALTER/research/2026-10-14_iran-full-sweep/leg-B-infrastructure.md`); WALTER did not certify it at the primary on 10/16 |
| Saudi crude, Bloomberg survey, October | **9.2** mb/d (+0.97) | Bloomberg via Rigzone 11/7, House of Saud 11/9 (secondary) |
| Saudi crude, EIA STEO, November vintage (COPR_SA) | Feb 10.5 · Aug 6.35 · Sep 8.5 · **Oct 9.3** | **PRIMARY**, EIA API v2, pulled 08:50 EST (`raw/steo_nov_COPR_SA.json`) |
| Saudi unplanned disruption, EIA (PADI_SA) | Feb 0.07 · Sep 2.25 · **Oct 1.33** | **PRIMARY**, same pull |
| Saudi production capacity, EIA (COPC_SA) | Feb 11.6 · **Oct 9.3**, equal to production; spare COPS_SA 0 since March | **PRIMARY** |

## 2. Which Saudi series I use, and why

**I use the independent estimates: EIA's 9.3 (primary) alongside Bloomberg's survey at 9.2. Saudi's self-report of 10.563 is recorded as an upper-side challenge, not adopted.** OPEC's own secondary-source Saudi figure would be my first choice. It is unread, and I do not infer it.

| Reason | Detail |
|---|---|
| OPEC measures compliance on secondary sources | Direct communication is the member's own claim |
| The direct-minus-independent gap is widening | September: direct 8.372 against secondary 8.001, a gap of +0.37. October: direct 10.563 against the survey at 9.2, about +1.36, and against EIA's 9.3, +1.26. |
| Export arithmetic supports 10.563 only at its edge | See section 4. Exports of 5.5 to 7.0 mb/d plus about 3 mb/d of domestic crude use give production of about 8.5 to 10.0. 10.563 needs the top of the export range and no stock draw. |
| Motive (context, not evidence of error) | The November 29 OPEC+ meetings face the 2027 baseline question. A high self-reported month supports a capacity claim. This is a reason to wait for secondary sources. It does not show the figure is false. |

## 3. Is the STEO shut-in figure overtaken?

**No, not on any evidence that is verified at a primary.** EIA's 2.5 mb/d of Middle East crude shut-ins in October already assumes Saudi at **9.3**, which agrees with the independent survey to within 0.1.

What depends on the series choice:

| If Saudi October was | Saudi's piece of EIA's disruption | Middle East shut-ins | Basis |
|---|---|---|---|
| 9.3 (EIA) or 9.2 (survey) | 1.33 mb/d (PADI_SA) | **about 2.5**, as published | EIA |
| 10.563 (self-report) | about 0: 9.3 + 1.33 = 10.63, EIA's undisrupted Saudi level, so the self-report matches it | **about 1.2** (2.5 − 1.33) | own arithmetic on EIA series |

⚠️ How the 2.5 headline breaks down by country is my reconstruction, not EIA's. October PADI values: Saudi 1.33, Kuwait 0.715, Iraq 0.101, which sum to 2.15 before any non-OPEC Gulf barrels. Iran's 2.32 is evidently not inside the 2.5. The country-level series are EIA's.

**Q4 balance:** the STEO's 1.47 mb/d Q4 build rests on supply. The OPEC report adds to supply; it does not reverse the build. OPEC+ secondary sources rose **+2.04** mb/d from September to October. EIA's OPEC+ crude rose +1.23 (COPR_OPECPLUS 31.49 to 32.72) and OPEC crude +1.315 (21.89 to 23.205). ⚠️ The perimeters differ (EIA's OPEC+ level is about 8.5 mb/d below OPEC's 41.23), so this is direction only: if anything, the independent sources see more October supply than the STEO does. OPEC's own balance and call figures are unread.

**Spare capacity (the 11/29 letter):** EIA carries Saudi capacity equal to production (9.3) and zero spare, which gives COPS_OPEC 0.01 from October to March. If the self-report holds, Saudi's effective capacity in October was at least 10.56, and "no spare" understates what Saudi can add. One agency each way; the IEA OMR is still owed as the second agency before the 11/29 grade.

## 4. Production is not exports: what is known about barrels leaving

| Read | October figure | Route | Grade |
|---|---|---|---|
| Kpler, October 1–25 | Ras Tanura about **2.95** mb/d (September 4.16); Yanbu about **2.21** (September 2.54); total about **5.52**, analyst full-month estimate about 5.8 | Ras Tanura exits **through Hormuz**, and the Sohar ship-to-ship relay still needs Hormuz (THESIS war/access line). Yanbu exits through the **Red Sea**, no Hormuz. | Asharq Business via Egypt Oil & Gas, secondary of a vendor |
| Vortexa | total about **6.5** (September 6.6); Red Sea about **2.5** (September 2.4) | both coasts | Gulf News 10/31, secondary (already a combo:gulf-flow-basis member) |
| Vortexa via Javier Blas | over **7** mb/d in the first 22 days | — | Newsquawk headline of a Bloomberg column, secondary; the gap with 6.5 is unexplained |
| TankerTrackers | 6.99; west coast +296%, east −27% against January–February | — | Gulf News 10/31 and Arab Times 10/23, secondary (already members) |
| Sohar relay | about 60M bbl from Ras Tanura sold for September–October ship-to-ship off Sohar | through Hormuz | Reuters via ARY and Saudi Gazette; Aramco has not commented |
| November | **no vendor print found** (two searches 11/11) | — | unmeasured, not a zero |

**Read:** in October Saudi crude left roughly 55–60% through Hormuz (Ras Tanura) and 40–45% through Yanbu on Kpler, a split that shifted toward Hormuz after the September East-West pipeline attacks. The vendors disagree by up to 1.5 mb/d on the total, and nothing reconciles them to one figure. None of this is a strait count. The 11/9 Petroline hit (operations unaffected, SPA) comes after these windows.

## 5. What moves on my own letter

| Item | Moves? | Why |
|---|---|---|
| WALTER boundary #1 (Brent ≥ $120 on 3 settles) | No | Supply news; the front is about $91 (11/10 vendor) |
| BRT-07 (reopening) | No | No reopening |
| BRT-32 (Yanbu loading halt) | No, OPEN 20% | Yanbu loaded about 2.2 mb/d through October 25 (Kpler); no halt stated |
| BRT-33 (M1−M3 under +3.50) | No, OPEN 20% | More supply pushes the curve toward a narrowing; that direction was already registered. Today's window is read after 14:45 ET |
| BRT-34 (distillate under 95,000) | No, 45% | A crude production figure; the products constraint is unchanged |
| BG-02 | No | A loss gate; this is a gain |
| THESIS Phase 2 Path A | Record only, no version change | WQ-331 P4: no registered Path-A grader; the Saudi resolver was abandoned 10/29 (WQ-533 a) |
| STATUS throughput line | Annotated | EIA's 2.5 stays as the agency figure, with the self-report as an upper-side challenge |
| **Paper-physical gap** | **The reading leans further to the paper-surplus side (a logged member, not a score)** | Independent sources now show October supply up by more than the STEO assumed. Dated Brent's newest print is still **$107.03 (11/3)**: FRED DCOILBRENTEU re-pulled 08:52 EST, realtime 11/11, nothing newer. There is still no measured stock build in a print; WPSR 11/12 is the next physical read. |

Logged on combo:gulf-flow-basis and combo:paper-physical-gap (CATALYSTS, 11/11 adds). No new combination theme opened.

## 6. Owed

The OPEC secondary-source Saudi October figure. If it prints 10 or above, the EIA shut-in figure becomes contested, not just challenged, and section 3 is re-graded. Route: any outlet carrying the table, or Will opening the PDF. The IEA OMR is the second agency. The first November vendor export print goes onto combo:gulf-flow-basis.

**Sources:** [Business Recorder / Reuters 11/11](https://www.brecorder.com/news/40448439/saudi-arabia-leads-further-jump-in-opec-oil-output-despite-war) · [Investing.com 11/11](https://www.investing.com/news/commodities-news/saudi-arabia-raises-oil-output-to-highest-level-since-february-93CH-5018855) · [Rigzone 11/7, Bloomberg survey](https://www.rigzone.com/news/survey_shows_opec_output_neared_prewar_levels-07-nov-2026-185030-article) · [Interfax 10/13](https://interfax.com/newsroom/top-stories/119524/.) · [Egypt Oil & Gas, Kpler](https://egyptoil-gas.com/news/saudi-oil-exports-exceed-5-5-mmbbl-d-in-october-despite-attack/) · [Gulf News 10/31](https://gulfnews.com/business/energy/saudi-oil-keeps-flowing-despite-attacks-say-trackers-why-counting-barrels-is-not-easy-1.500730059) · [Newsquawk, Blas](https://www.newsquawk.com/headlines/saudi-crude-exports-reportedly-exceeded-7mln-bpd-in-the-first-22-days-of-october-returning-to-pre-war-levels-and-suggesting-production-has-risen-towards-9-10mln-bpd-bloombergs-javier-blas-reports-citing-vortexa-data) · [ARY, Sohar relay](https://arynews.tv/aramco-to-boost-gulf-exports-to-60-million-barrels-in-sept-and-oct) · EIA API v2 STEO (`raw/`) · FRED DCOILBRENTEU.

## 7. Production up, exports down or flat: PROME prome-2b question, 09:46 EST (NEXUS contradictions C4/C5)

| Question | Answer from this record |
|---|---|
| Months compared | **September against October.** Kpler's October figure is **partial, October 1–25** (5.52 mb/d; the analyst's full-month estimate is about 5.8). The 6.70 for September is the sum of Kpler's two September terminal figures (Ras Tanura 4.16 + Yanbu 2.54). NEXUS added them; this note never printed 6.70. Vortexa is a full-month comparison, 6.6 to about 6.5. |
| Production change | **+0.8 mb/d (EIA COPR_SA 8.5 to 9.3)** is the primary figure to use. "About 1" is Bloomberg's survey (+0.97), and +2.19 is the self-report. Name the series beside the number. |
| The phrasing | "Saudi crude production rose about 0.8 mb/d from September to October on EIA's estimate, while seaborne exports fell on Kpler's partial-month count (about 6.7 to about 5.8) or were about flat on Vortexa (6.6 to 6.5)." Correct as long as both vendors and the partial month are named. HAWK's "recovering, not shrinking" is a production statement, and it agrees with this. The export side does not show the extra barrels reaching the market in October. |
| Where the difference goes (ranked; none measured) | (1) **Measurement**: a partial month, and vendors that disagree by up to 1.5 mb/d (Blas/Vortexa over 7). This alone could close most of the gap. (2) **Domestic refining**: SATORP (460 kb/d) back at 100% "since early October" (TotalEnergies CEO 10/12, INCIDENTS RF-018; CATALYSTS row 10/29) is a real new domestic crude sink in October. (3) **Storage swing, a hypothesis**: September's exports (about 6.6–6.7) against 8.5 of production leave only about 1.8 for domestic use, below normal Saudi refinery runs. That points to a September stock draw that October may have refilled. Unmeasured; JODI Saudi stocks would test it. (4) **The East-West pipeline is not a sink.** Barrels piped to Yanbu are counted when they load there, so they appear in exports, except for crude run at the Yanbu-area refineries. (5) **Seasonal crude burn** falls after summer, so it goes the wrong way to absorb the gap. |
