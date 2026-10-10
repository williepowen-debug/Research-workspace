# BRENT — Saturday 2026-10-10: Russian diesel license, Isaias restart, freight (session `brent-1010`)

**Written 2026-10-10 11:42 EDT (`date`).** Claude Code, Opus 5.5 (`claude-opus-5-5`), spawned by PROME `prome-1e` on Will's word given in WALTER's window at 11:30 ET ("Okay lets do A and C"; relayed by walter-66). Tier: read / grade / record. **No trade, threshold, gate cell or score moved.** Verbatim primary text: [`primary_extracts.md`](primary_extracts.md). Tape evidence: [`tape_pull.py`](tape_pull.py) → [`tape_evidence.json`](tape_evidence.json) + [`bars_1009_extract.csv`](bars_1009_extract.csv) (yfinance 1-min, single vendor, pulled 11:36 ET).

## 1. US sanctions relief on Russian diesel

### Facts at the primary
| Item | Value | Basis |
|---|---|---|
| Instrument | **OFAC Russia-related General License No. 135**, "Authorizing Transactions Related to the Sale, Delivery, Offloading, and Importation of Diesel Fuel of Russian Federation Origin" | [CONF OFAC Recent Action 20261009_33 + GL PDF, sha256 `b42bed87…`] |
| Date / signer | Dated **October 9, 2026**; Bradley T. Smith, Director OFAC | [CONF GL text] |
| Scope | All transactions prohibited by **31 CFR 587** (RuHSR) or **589** that are related to the **sale, delivery, offloading or importation, including importation into the United States**, of Russian-origin diesel fuel | [CONF GL (a)] |
| Expiry | **12:01 a.m. EDT, April 7, 2027** | [CONF GL (a)] |
| Exclusion | No debits to US-held accounts of the Central Bank of Russia, the National Wealth Fund or the Ministry of Finance | [CONF GL (b)] |
| Release time | **PDF digital signature 14:43:59 ET 10/9** (Bradley T. Smith; CreationDate 14:43:38). Trump's post followed at **14:46 ET** and Treasury's X post at **14:49:02 ET**. | [CONF PDF signature dictionary, read by BRENT; Trump's time per WALTER `SIG-W-20261010-003` (archived copy); Treasury's time decoded from the status ID] |
| Tonnage | **0.3 Mt "immediately" + 0.5 Mt in November + 1.0 Mt "immediately thereafter" + 3.0 Mt "based on the condition of their Diesel Refineries"**. **4.8 Mt is a relay's SUM, not a stated figure.** | **SPEAKER: President Trump, Truth Social, 14:46 ET 10/9** (verbatim per WALTER `-003`, archived copy; BRENT read a BeInCrypto/Yahoo relay with the same tranches). No Russian or OFAC document carries a tonnage. |
| Russian side | Kremlin readout (via Xinhua): "readiness to supply oil and petroleum products", no volumes. **Novak (TASS 10/9): Russia "immediately begins lifting restrictions on diesel exports ahead of the schedule". No decree found.** | Relayed by WALTER `-003`; BRENT's own search did not reach TASS. YURI owns the Russian export instrument. |

- **[EST] 4.8 Mt ≈ 35.8M bbl** at 7.45 bbl/t; the unconditional 1.8 Mt ≈ 13.4M bbl. The November tranche (0.5 Mt) ≈ 3.7M bbl ≈ **0.12 mb/d** over 30 days; the 0.3 Mt ≈ 2.2M bbl, one-off. (WALTER's arithmetic matches.) **DEWEY is commissioned on the net-supply question** (`REQ-DEWEY-20261010-001`, due 10/14).
- **What the license does not do** (from its text; OFAC FAQs not read): it does not touch Russia's own diesel export ban (extended to 10/31; a partial lift is being *weighed*, Energy Intelligence headline via WALTER `-014`). It does not repair Russian refineries (Volgograd full halt since 10/2; Ukraine claims a fourth refinery hit this week; OSPREY's ledger). It does not change EU/UK measures. Whether it overrides the 2022 statutory US import ban is contested in commentary; BRENT does not adjudicate it.
- **Before carrying the 4.8 Mt anywhere, say who said it.** It is the President's number, and 3.0 Mt of it is conditional.

### The diesel tape on its proper basis (Fri 10/9)
| Observation | Nov `HOX26×42−CLX26` | Dec `HOZ26×42−CLZ26` | Basis |
|---|---:|---:|---|
| ③ settle-window VWAP 14:28–14:30 ET | **$107.15941** | **$101.68866** | [EST single vendor, typical-price VWAP, 3/3 bars per leg; reproduces `332d877ca` exactly] |
| ② vendor daily row (16:59 bar) | $107.1628 | $101.7028 | [vendor; INFERRED = relayed settlements; ⚠️ volume duplicates 10/8's (HOX26 57,259), the defect TERRY rejected ② for on 10/7] |
| Last real trade 16:58 ET (post-news) | **$104.90** | **$99.46** | [EST vendor last trade; NOT a settlement and NOT a gate observation] |
| Post-settle VWAP 15:00–17:00 ET | $104.73 | $99.20 | [EST] |

- **The "HOX26 −2.96%" print** is vendor 4.7384 vs vendor prior 4.8829 (10/8). Both values sit within $0.001/gal of their 14:28–14:30 window VWAPs. The vendor also wrote 4.7384 into the 16:59 bar as a jump from the 16:58 trade of 4.6800, so both are [INFERRED] relayed **settlements**. ⇒ **The −2.96% is settle-to-settle, and it was set BEFORE the diesel news.** It is the retracement of the 10/8 distillate jump (the 10/9 note's China/Isaias read), not the deal's reaction. Settle-to-settle crack change: −$6.42, matching the 10/9 note.
- **The deal's reaction came after the settlement window.** The license was signed at 14:43:59 ET and Trump posted at 14:46 ET. HOX26 broke on the **14:46 ET bar** (4.7292 → 4.6905 on 721 lots), and CLX26 went 91.56 → 91.18 on 1,541 lots. Crude round-tripped (CLX26 low 90.59 at 14:50, 91.66 by 16:58; BZZ26 103.35 → 104.39). Heating oil recovered only ~40% (low 4.6442, 4.6800 at 16:58). ⇒ **The hit was distillate-specific: about −$2.26 on the Nov crack and −$2.23 on Dec, in post-settle trade [EST].** It enters the first settlement only on **Mon 10/12** (CME energy settles normally on Columbus Day: INFERRED from a search summary of CME's notice; the notice itself returned 403).
- **§2R evening-bar rule.** Friday has no evening session (Globex is shut Fri 17:00 → Sun 18:00 ET), so the 10/9 row read today is Friday's. **From Sun 18:00 ET the vendor's "today" bar is Monday 10/12's session.** Never read a Sunday-evening print as Friday's close or as a Monday settle.
- **Dated Brent (EIA RBRTE)** is unchanged at its last print, 125.44 (10/6). It is a physical basis and is not compared with any futures cell here.

### What it does to `GATE-TERRY-VLO-HELD-01` (ESTIMATE; TERRY grades; Will executes; no gate cell moves on this note)
- **Leg A (Nov basis, through the 10/14 settlement).** Friday's observation predates the news: ③ $107.16 is **$17.00 above $90.16** and $12.16 above the $95 notice line. Post-news trade, $104.90 [EST, not an observation], is **$14.74 above $90.16** and $9.90 above $95. Three Nov settlements remain (10/12, 10/13, 10/14). A Nov fire needs a further ~$14.7 compression in three sessions.
- **Dec basis (governs 10/15–11/19).** Post-news trade, $99.46 [EST], is **$9.30 above $90.16 and $4.46 above the $95 A-notice line**. The notice is the near line, and a notice is a notice only.
- **Leg B1 is not engaged.** GL 135 is US sanctions relief on Russian-origin diesel. It is not a US action that "bans, caps or licenses US distillate/diesel exports". B2 (Valero curbs exports on the record) is not engaged either.
- **Thesis-owner read (BRENT).** The license removes a US-sanctions barrier for buyers, shippers and insurers in the Russian diesel trade. The barrels are bounded by Russia's own ban and its damaged refineries, and the President himself conditioned 3.0 of the 4.8 Mt on the refineries. The first-day market priced ~$2.2/bbl of distillate-specific compression. **Direction: adverse at the margin for the distillate-tightness leg the held VLO share rests on. Not by itself a thesis break.** The next facts that size it: a Russian government decree lifting or relaxing the export ban (YURI); the first loaded cargo under GL 135 (tracking); and Mon 10/12's settlement.

## 2. Isaias restart (DOCKET L633, window 10/10–12)
| Item | State | Basis |
|---|---|---|
| MMA/BSEE 10/10 shut-in | **NOT-YET-PUBLISHED at 11:41 ET.** The RSS newest is `…isaias3` (10/9); `…isaias4` returns 404 (a guessed slug, not evidence of absence). On the 10/8 and 10/9 pattern the page appears ~12:40–13:00 ET, *if* MMA issues a Saturday release. | [CONF BSEE RSS 11:41 ET] |
| Last figure | **1,458,814 b/d = 71.51%** oil, 58.84% gas, 129 of 371 platforms [as of 11:00 CDT 10/9] | [CONF MMA `isaias3`, BRENT `6c0db64fe`; AEOLUS matched it at the primary] |
| Landfall | Near **Destin FL ~8:30 PM CDT 10/9, Cat 2, 105 mph**; ~120 mi E of Pascagoula, ~90 mi E of Mobile Bay | [CONF NHC TCU via AEOLUS packet] |
| Chevron offshore | 4 operated platforms kept producing; **5 shut in; crew remobilisation "will continue through Sunday"** | [CONF Chevron newsroom 10/9] |
| Chevron Pascagoula refinery | **No operator statement on refinery operations since Thursday's "remains operational".** Relays (ZeroHedge, Futunn 10/10) say it was "spared". | Relay only. Operator status is a GAP. |
| Port of Mobile | Its own page still shows **ZULU / CLOSED**, last updated **10/9 08:31 CDT**; no post-storm update | [CONF alports.com 11:39 ET]. A stale-at-source status, not a verified current state. |
| Pascagoula port / LOOP | Not found | GAP |

- **CATALYSTS 10/10 fork, PARTIAL grade (row stays open to 10/12).** Scenario (2)'s preconditions occurred: rapid intensification to Cat 3 and an eastern-core track. Its **refinery leg is NOT observed**: no shutdown was reported, and the crack COMPRESSED on 10/9 rather than widening. Its **offshore-damage leg is UNKNOWN** until the first post-landfall MMA figure or operator damage reports. Chevron's restart language points to scenario (1). The record is: track ran east of refining, refinery leg not observed, offshore leg ungraded.
- WPSR wk-10/9 [EST] ≈ 3.3–3.6M bbl lost (10/9 note), unchanged. It prints Thu 10/15 12:00 ET.

## 3. Tanker freight
| Series | Value | Prior | Basis |
|---|---|---|---|
| **TD3C AG→China (Gibson)** | **WS1,319 / $1,478,500/day [Oct 8]** | WS1,145 / $1,277,000 [Oct 1]; last month $903,500 | [CONF Gibson table, re-fetched by BRENT 10/10, independent of WALTER's capture]. Round voyage, Gibson convention. |
| TD3C FFA Q4 (Gibson) | WS1,258 / $1,397,750 | — | Paper, **$80,750/day under spot** |
| TD3C / TD34 (Baltic) wk41 | **NOT OBTAINED** (bot challenge again 10/10) | TD3C WS1,145 / $1,221,893 [10/2] | Missing, not flat. ⛔ Never mix with Gibson. |
| **TD22 USG→China VLCC (Baltic)** | **$79,611,111 (+$24.8M w/w)** [Baltic round-up 10/9] | — | Relay: The Edge Malaysia, via WALTER `-003`. Not read at the Baltic. This is the only wk41 Baltic figure on file. |
| **USG→China VLCC, November loading** | **$80M "this week" for 2M bbl = $40/bbl** (vs $8.60 pre-war Feb); Cosmo Oil **$81M provisional**, Nov 19–21 loading | $44.8M (~24 days earlier, Baltic-based relay, not verified) | [Shipbroker SSY data on LSEG, via wire syndication, Baird Maritime 10/9 10:22Z]. A **Bloomberg** figure exists for **10/7: $77M vs a 2025 average of $9.2M** (WALTER `-003`, search snippet). A Bloomberg 10/9 figure is SEARCH-NOT-FOUND. The **$76–77M** in the Baird piece were SK Energy's and Trafigura's *failed* bids, not fixtures. ⛔ **Three bases (SSY/LSEG · Baltic TD22 · Bloomberg): never average.** |

- **Placement.** BRENT has **no registered freight-rate line**. `VLCC > WS200` was retired 7/31 (F4); boundary #5 (Worldscale) is NO INSTRUMENT; WAR-RISK-HALVES is retired. TANKER-LIVENESS (STNG/FRO/DHT equity composite) is the only live tanker instrument, and it is ungraded on a weekend. These figures are context only.
- **Transmission (assessment).** $40/bbl USG→Asia freight is a WTI-netback depressant: US crude has to discount to clear to Asia, and the traders say Asian buyers are switching to Murban (premium >$11 to Dubai). That pushes toward a **wider Brent–WTI**. Dec Brent–WTI on vendor daily rows was **$13.71 [10/9; 104.72 − 91.01, INFERRED settles]**; WALTER's +13.63 used last trades. Same direction, different basis. This fits the 10/9 structural-cost note. `THESIS-WTI-BRENT` (>$5) has been above its line all along; no change.

## 4. Inbox and handback
- **7 files consumed** (2 top-level, 5 WALTER; `SIG-W-20261010-003` landed at 11:38 ET mid-session and was folded into §1/§3) = **7 `board_log.tsv` rows = 7 `git mv` to `processed/`.**
- **L659 handback: CLOSED on 10/9.** ① COT #9 graded JOINT NOT-SPENT (`f50d59625`); ② MMA 10/9 71.51% (`6c0db64fe`); ③ settle-window crack $107.16 / $101.69 (`332d877ca`); memo `1762b8e91`, consumed by PROME. The DOCKET L659 state cell is PROME's.
- COT #10 (as-of 10/13) prints Fri 10/16 ~15:30 ET.
- **Boot rc=2, three FINDINGS, all carried:** weekend quotes ungraded (market closed); TANKER-LIVENESS weekend plus stale stamp; and Pending-Receipts: the USO Oct-9 $150C expiry has elapsed. USO closed $148.20 [vendor 10/9], below the strike, and **its disposition (sold or expired) is on no repo surface.** Will's and TERRY's to record; BRENT does not infer a fill.
