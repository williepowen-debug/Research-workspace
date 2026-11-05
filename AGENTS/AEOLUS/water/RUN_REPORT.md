# AEOLUS · WATER — worker RUN REPORT

**run_date: 2026-11-05** (worker run: pulls 11:54–12:05 ET; files written 12:04–12:06 ET, per `date`) · spawned by AEOLUS on Will's word, 11:53 ET · **findings are PROPOSAL-ONLY. AEOLUS adjudicates them.**
*Nothing below is scored, fired, resolved or routed. No source was substituted for a failed command. No git operations were run. This report supersedes the 10/29 `RUN_REPORT.md`.*

---

## The answer in brief

**The free record shows severe gauge state and reduced loads to the Upper Rhine through 10/30. It shows nothing about cargo on 11/02–11/05.** No halt, volume figure or plant warning dated since 10/28 was found. That is a gap in the sources, not evidence that cargo is unhurt.

| Class | Finding | Latest date covered | Source label |
|---|---|---|---|
| **Gauge state** | Kaub 18.0–22.3 cm, Duisburg 154.4–169.0 cm, Emmerich 6.9 cm [11/04], Köln 69 cm [11/05] | 11/04, partial 11/05 | PRIMARY |
| **Surcharge** | Contargo Kaub €1,075 / Ruhrort €335 per full 20′ | 11/05 | PRIMARY. Set by the gauge, so not independent evidence |
| **Market price** | Lower Rhine tanker rates unchanged 10/26–30, Basel up, Frankfurt and Karlsruhe eased. No €/t. CBS Q3 not printed | 10/30 | SECONDARY trade |
| **Reduced load** | "by Thursday loads to Upper Rhine destinations were limited, depending on barge size" | 10/29–30 | SECONDARY trade, no tonnage |
| **Demonstrated halt or cargo reduction** | **None dated since 10/28.** Earlier: "most barges stayed near the ARA, or went no further than Duisburg and Cologne" (10/16 post) | 10/21 | SECONDARY, context |
| **Downstream supply** | Swiss diesel stock release to 11/22, mixed cause | 10/23 notice | PRIMARY |

---

```
observations_added:  92 rows to SERIES.tsv, 30 to LOG.tsv
```

SERIES: Maxau, Worms, Mainz, Emmerich stage (28); six-station discharge (42); Lees Ferry (7); Powell storage (8); heating oil, seven states, labelled confounded (7), all 10/29–11/04 except storage from 10/28 and heating oil 11/05. No new CBS rows, because Q3 has not printed. No new Contargo rows, because AEOLUS already holds 11/05 and the page matches them. No `rhine_freight_eur_t` row. USGS tributary flows are in LOG only, because they are not approved instruments. Stamps checked against the wall clock after writing: none is later than the write.

## threshold_state

**Reported, not graded. The worker fires nothing.**

| Line | Value | Margin | State |
|---|---|---|---|
| Kaub ≤40 / Duisburg ≤180, 3 complete days | Kaub 19.104 / 18.010 / 22.260, Duisburg 168.979 / 161.427 / 154.427 (n=96 each), 11/02–04 | Kaub −17.74 to −21.99; Duisburg −11.02 to −25.57 | **1 window.** AEOLUS recorded it as FIRED (KB-237); not re-graded here. 11/01 fails on Duisburg (181.688). 11/05 incomplete at pull (n=72), skipped |
| NNW marker Kaub 25 / Duisburg 153, descriptive | Kaub below on all three days; Duisburg 154.427 on 11/04 | Duisburg +1.427 | **0 windows** |
| Powell vs 3,510 ft | 3,535.89 [11/04] | +25.89 ft | No day at or below the line in this run. ≥3,520 state: not re-tested |
| Mead vs 1,035 ft | 1,039.29 [11/04] | +4.29 ft | No day at or below the line in this run |
| Memphis, Gatún, USDM, Danube, Paraná, Lees Ferry line | Not tasked; AEOLUS read them this morning (KB-241) | | Not re-pulled, except Lees Ferry flow 6,520 cfs [11/04] |
| Yangtze | No read | | Failed, see gaps |

## changes

**Rhine discharge, 10/29 → 11/04 (m³/s):** Kaub 661 → 531 (low 513 on 11/03) · Duisburg 954 → 677 · Emmerich 1,016 → 703 · Mainz 623 → 495 · Worms 502 → 445 · Maxau 410 → 411 (low 372 on 10/30). Lower Rhine is still falling; Worms, Mainz and Maxau have been roughly flat since 11/01. Still above the 10/19 values in SERIES (Kaub 491.5, Duisburg 607).

**Same-date stage, 11/02–04:**

| | 2026 | 2018 | 2022 |
|---|---|---|---|
| Kaub (cm) | 19.1 / 18.0 / 22.3 | 58.9 / 55.6 / 55.3 | 131.1 / 125.9 / 124.2 |
| Duisburg (cm) | 169.0 / 161.4 / 154.4 | 189.9 / 185.1 / 188.1 | 286.9 / 278.1 / 275.4 |

The datum caveat applies across eras. The 2026 lows remain Kaub −4.8 [10/01] and Duisburg 121.4 [9/29], so this is a re-entry, not a new low. **No discharge history exists for this comparison** (long series is stage only, WSV Q characteristic values empty).

**WSV forecast, init 11/05 07:00 CET:** Kaub 22 on 11/06, 16 on 11/07, then estimate 8 → 5 → 6 through 11/09. Duisburg 150–155. Emmerich 1–3. Instantaneous points; the type changes from forecast to estimate on 11/07.

**Contargo, page table 05.11.2026, verbatim:** *"Wir müssen Sie darauf hinweisen, dass für Pegelstände kleiner gleich 30 cm in Emmerich, 180 cm in Duisburg-Ruhrort, 105 cm in Köln und 80 cm in Kaub unsere Transportverpflichtung endet. Dennoch versuchen wir alles uns Mögliche, um Ihre Container zu transportieren."* All four gauges are inside those lines (2 / 153 / 69 / 18). No suspension or service-limit text is on the page. The obligation ended; service did not stop. Separately, Contargo's 10/30 notice gives barge waits of 48 h at Antwerp and 77 h at Rotterdam, with no cause stated.

**CBS 85817NED: 2026-Q3 has NOT printed.** Latest 2026-Q2: dry spot 130.5 (+11.4% y/y), all goods 135.9 (+6.5%), wet bulk 140.6 (+1.1%). Table modified 2026-09-04. The first print of this event is still ahead.

**Heating oil, 11/05 (confounded):** Baden-Württemberg 171.83, Hessen 175.11, Rheinland-Pfalz 174.90, North Rhine-Westphalia 171.75, Bayern 168.11, Hamburg 160.78, Sachsen-Anhalt 173.44 €/100 L. National 169.27.

**Powell, second pulse:**

| cfs, daily | 10/31 | 11/02 | 11/03 | 11/04 | latest, 11/05 ~09:30 MT |
|---|---|---|---|---|---|
| San Juan near Bluff | 4,970 | 24,700 | 29,900 | 23,100 | **30,500** |
| Colorado near Cisco | 3,950 | 13,600 | 15,500 | 11,100 | 6,710 |
| Green at Green River | 3,590 | 4,150 | 4,750 | 6,070 | 5,860 |
| San Rafael + Dirty Devil | 193 | 1,322 | 1,287 | 563 | not pulled |
| **Gauge sum** | 12,703 | 43,772 | 51,437 | 40,833 | |
| USBR inflow, 919/29 | 13,680 | 41,038 | 41,301 | 53,324 | no print |

- **Storm pulse: evidenced.** Releases were flat (Glen Canyon 6,525–6,664, Flaming Gorge 2,181–2,188, Navajo 250–270 cfs) while unregulated gauges rose together 11/01–03: Chinle Creek 0.3 → 1,650, Mancos 108 → 3,440, Animas 2,570 → 13,600, Dolores 660 → 6,050, Price 57 → 938. KJZZ (11/01, secondary) reports heavy rain and flooding across northern Arizona and the Four Corners.
- **Source:** San Juan about 58% of the gauge sum on 11/03, Colorado 30%, Green 9%. Matching USBR's 11/04 inflow to the 11/03 gauge sum assumes a one-day lag, which is my assumption.
- **Navajo held its share:** inflow 52,053 cfs on 11/02 against a release of 250, above the 44,238 October peak on this daily basis.
- **Holding? Mixed.** Cisco has dropped well below its 17,700 maximum. Bluff fell to 20,800 on 11/04 and rebounded to about 31,000 on 11/05, so the San Juan is on a second crest. The cause of the rebound is not established. Green is holding near 6,000.
- **HYPOTHESIS:** the Archuleta rise below Navajo (230 → 2,400 cfs with flat release) comes from below the dam.
- **Since 11/04:** no newer USBR elevation at 12:01 ET. Powell is +3.99 ft and +242,540 af since 10/31; Mead 1,039.29. Inflow of 53,324 is the 5th-highest October–November day since 1963 (n=3,878); 5 of the top 8 are 2026 days. Report only: do not extrapolate the rate.

## proposed_findings

*Proposals. AEOLUS adjudicates.*

1. **The freight record has a gap exactly where the event is.** Every free freight-side source stops at or before 10/30. Insights Global published 11/04 and covers 10/26–30. CBS ends at Q2. Only the Contargo table runs through 11/05, and that table is a gauge lookup. Sources: LOG `insights_global_week_10_26_to_10_30`, `cbs_85817ned_no_q3_print`.
2. **Contargo's surcharge is not independent evidence, and at Kaub it is saturated.** Every level at or below 40 cm prints the same €1,075, so it cannot register further deterioration. Duisburg's row still moves. Source: Contargo schedule, 11/05.
3. **Flat rates in the week to 10/30 are weak evidence of no harm.** The trade report says thin trading left too little to change the published rates, and that both sides were already covered. Those days had Kaub at 41–57 cm. On 10/20–21 rates fell on forecasts of water, ahead of the water. HYPOTHESIS: rates in this market may turn on forecast as much as on the gauge. Sources: Insights Global 11/04 and 10/30 posts.
4. **Reduced load is documented; lost cargo is not.** The nearest thing to cargo evidence in the window is the "limited" Upper Rhine load statement, without tonnage. The strongest statements are older: 10/16 "most barges stayed near the ARA, or went no further than Duisburg and Cologne"; 10/02 MSG's 14 vessels for a 3-vessel load (one operator, one load).
5. **The Swiss diesel release is a real supply response with a mixed cause.** 45,000 m³, 10/23–11/22, just under 4% of compulsory stock. The Confederation names the trigger as pipeline delays from rain in southern France, against low water that has impaired logistics "seit Monaten". Do not count it as a low-water draw alone. Source: bj.admin.ch release of 23 Oct 2026.
6. **Bottrop's Swiss-grade diesel stop for November has no stated cause.** Insights Global reports the announcement and does not tie it to low water. The refinery statement was not found. Watch-item, not a finding.
7. **Hapag-Lloyd's published table ends at Kaub 25.** Kaub at 18–22 cm falls into "individual agreement". SECONDARY: container-news.com 9/28; the carrier's page returned 403.
8. **The rail substitute may be limited.** Secondary, 8/11: the right-bank Rhine line closed to freight to 12/12/2026. Not verified at DB InfraGO. Worth an owner's check before anyone relies on it.
9. **Company silence, as searched since 10/28.** BASF's 10/28 Q3 release has no mention of Niedrigwasser, Rhein or Logistik and raises the outlook, but it covers the quarter to 9/30 and the call was not read. Covestro, thyssenkrupp, Shell Rheinland, Evonik, Lanxess, GKM and Karlsruhe coal: searched, nothing found. **That is a result, not proof of no impact.** Covestro's August force majeure status is unknown.
10. **Powell's second pulse is a storm pulse, San Juan-led.** Evidence above. Its daily peak so far (53,324 cfs) is below the October event's 63,368; volume was not compared. Navajo absorbed its share again.

**Instrument proposals, none created:**
- **`rhine_freight_eur_t`: do not create.** Newest dated €/t found is €150–160 on 8/4 (Reuters via bdnews24). BargeINSIGHTS is paid. No verified free source.
- **WSV computed fairway depth:** ELWIS page, Stand 10/30, offers "rechnerisch verfügbare Fahrrinnentiefen" at selected Rhine gauges, to help adjust loading. It is the closest free primary to loadable depth. Values were not retrievable by static fetch. Worth a probe.
- **Approve vocabulary** for `powell_inflow`, `cisco_q`, `bluff_q`, `green_river_q`, so the attribution can sit in SERIES.
- **Probe `parameter=Q` on the WSV bulk route.** It would settle whether discharge history exists. Not run: outside this brief.
- **SOURCES.md notes to add:** `bj.admin.ch` serves Swiss federal releases to WebFetch while `www.admin.ch` returns 403 to curl; the Hapag-Lloyd page returns 403 to both.

**Next dated reads:** the next Insights Global Rhine post (first to cover 11/02 on) · CBS Q3 (early December is my estimate from the Q2 lag, no CBS date read) · Swiss release end 11/22 · Covestro Q3 and thyssenkrupp year-end reports.

## gaps

- **Yangtze:** the one retry failed: `curl` rc=28, `http 000`, 45.0 s, 0 bytes. Third failure today. No source substituted.
- **No operational evidence for 11/02–11/05.** See finding 1.
- **Named companies:** see finding 9. Search tools miss paywalled and wire copy, so a null here is weak.
- **BASF call not read;** Quartr is excluded by standing rule.
- **Hapag-Lloyd primary:** HTTP 403 to curl and WebFetch. The table is secondary.
- **`www.admin.ch`:** HTTP 403 to curl. The three Swiss releases were read at `bj.admin.ch` through a WebFetch subagent, so the quotes are relayed, not read by me directly.
- **Rijkswaterstaat droogtemonitor:** the page is JavaScript-rendered and returned no text. The 11/03 edition was not read. Lobith not read.
- **ELWIS:** NfB partly read; `Fahrrinneneinschraenkungen` not read; computed fairway depths not retrieved.
- **Search-summary only, page not opened:** Covestro force majeure, thyssenkrupp July actions, the 10/07 Lobbyregister entry. Treat as leads.
- **USBR site 913 as Blue Mesa is from my memory, unconfirmed;** the meta.csv paths tried returned 404 or no match. It is not load-bearing. Navajo 920 and Flaming Gorge 917 match the 10/29 run.
- **Extra USGS gauges** were picked by me beyond the SOURCES.md list; each name came back from the NWIS response.
- **Maxau, Worms, Mainz, Emmerich stage:** SERIES has no rows for 9/29–10/28. Only the tasked 10/29–11/04 was added.
- **Lees Ferry:** NWIS returned no 10/27 or 10/28 daily value.
- **SERIES.tsv line 252 is a blank row,** already there before this run. Left alone.
- **`Last real data refresh: 2026-11-05` stands:** Contargo and fastenergy carry 11/05 data. Gauge means run to 11/04.
