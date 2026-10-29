# SAM STATUS

**Last written: 2026-10-29 ~08:00 ET — Will-directed catch-up boot (nine days offline since October 20) on the eve of the BOJ October 29–30 decision.** Runtime Claude Code, model Opus 5.5 (`claude-opus-5-5`). Each row keeps its own source clock. Boot report `reports/boot-runs/20261029T041901Z_cb8c5694.jsonl`; news sweep `research/outputs/2026-10-29_sweep/NEWS_SWEEP.md`. Pull not needed (0 behind origin); other desks' trees dirty, so no pull was attempted.

**View:** no fresh observed Japan-led carry unwind. The October 22 Asia selloff (Nikkei about −3%) brought a modest haven bid: USD/JPY −0.91% on a 1.66-yen range, below the fast-move bar. On the October 26 Brazil shock the yen *weakened*. Speculators are net **long** yen at the CFTC (+69,878, 10/20), so the visible short-yen pool that unwound in August 2024 is absent; offshore FX-swap funding stays unmeasured. The market has priced October out (Totan 10/29: **2%**) and December in (**82%**). SAM-42 (25% October hike) grades on the statement PDF after the decision. The long end eased: 30Y back under 4.0% (3.941, MOF 10/28). **v1.7 retired-to-LOW, no successor frame, no entry, no prediction re-mark.** Last Will-confirmed FLAT June 29 is a dated desk record, not a fresh broker reconciliation.

**What changed while offline (sweep, REPORTED unless marked):** every sourced pre-meeting story points to a **hold at 1.25%** (Reuters 10/20, four sources: hold "unless the yen resumes its slide"; December possible). The live variable is the Outlook Report's **"underlying inflation has reached 2%" judgment** (Nikkei 10/22 via DLRI; Kyodo 10/21 says the judgment is made in this Outlook Report). That would be a hawkish hold for December/January. Takata is likely to dissent for a hike. The insurers' H2 plans show **no stated Treasury sales**: open foreign bonds are down or flat at every disclosed insurer except Nippon Life (flat to up), and year-end USD/JPY assumptions are 155–162. Katayama (Diet, 10/27): ready for "decisive action"; no rate check or intervention reported.

## LIVE MARKET DATA

| Instrument / release | Level and observation date | Assessment / limit |
|---|---|---|
| USD/JPY, completed London-label sessions | **10/22 156.721 (−0.91%, range 1.660) · 10/23 156.814 · 10/26 157.540 (+0.46%) · 10/27 157.994 · 10/28 157.832** | Own hourly aggregation, as-last-revised. 10/22 is the window's largest range and still under ~2–3 yen in 1–2 sessions. Vendor quote 10/29 04:19Z 157.71 (live bar, not scored). |
| Crosses, vendor 10/29 04:19Z | EURJPY 175.79 / GBPJPY 210.12 / AUDJPY 111.23 | Individual vendor clocks; not a synchronized attribution study. |
| BOJ meeting OIS **10/29 11:15 JST** (Totan, SAM visual review, SHA `ec55624d…`) | **Oct 2% / OIS 1.2313%; Dec 82%; Jan 26%; Mar 56%; Apr 29%; cumulative Apr 1.94 hikes** | Arithmetic chain checked, live hash validated, 5 rows ingested. Incremental 25bp equivalents ≠ probabilities; counts ≠ probabilities. Indicative OTC medians, JST assumed. Decision expiry 10/30. Was Oct 5% / Dec 76% on 10/20. |
| JGB curve, **MOF 10/28** | **2Y 1.915 / 5Y 2.281 / 10Y 2.867 / 20Y 3.685 / 30Y 3.941 / 40Y 3.974%** | Versus MOF 10/19: 10Y −6.8bp, 30Y −8.7bp. 30Y back below 4.0%. Do not difference vendor against MOF. |
| **2Y auction 10/29** | **BTC 4.031×; lowest 1.912 / average 1.905%; tail 0.7bp** | Orderly; front end, no frozen FIRM/SOFT bar at this tenor. MOF eresul20261029. |
| CFTC legacy JPY, **10/20**, rel 10/23 | **Net +69,878 LONG**, Δ +19,671; L 200,186 / S 130,308; OI 379,141 | Outside the deadband, graded on its own print; no forced-liquidation inference. Old short-side gates void. |
| MOF weekly foreign LT debt | **10/11–17 −¥160.5B · 10/18–24 −¥92.6B**; 4W −¥937.7B; 12W −¥2.44T | Both new weeks inside the ¥1.5T one-week bar, **each evaluated** (every-new-week reader repaired 10/29). Designated reporting investors, not insurer/UST-only. Rolling sums are live-CSV values; ledger keeps first prints. |
| MOF September investor-type, updated Oct-8 | Life insurers **−¥288.6B** (Aug −¥137.3B); banks −¥2,485.6B; trusts +¥1,195.3B | Carried from 10/20; sector selling, no named seller, UST specificity or forced-sale cause. October investor-type due ~Nov-10. |
| US–JP differential, **10/28** | **5Y 2.569pp / 10Y 2.183pp**, 0/5 through bars | Float-tie comparison repaired 10/29 (live history unchanged). FOMC 10/28 held 3.75–4.00% with **two hike dissents** keeps the US leg high. |
| Brent, named contracts (vendor) | **Jan BZF27 $110.20** (10/29 04:07Z; +1.42% vs 10/22); Dec BZZ26 $114.16 (expiry week) | Continuous BZ=F rolled 10/29 Dec→Jan: its −2.62% "move" is a contract switch, not a price move. Oil-benchmark repair still owed. |
| Sept trade balance, MOF customs (stage as parsed 10/29) | **−¥556.5B**; crude VOLUME 11,166 thousand kL **+3.1% YoY**, value +51.1%; LNG 4,779 kt −7.3%; ME crude volume **−30.0%** | Value rise is price, not volume; Middle East substitution continues. Implied unit cost ~$101/bbl is a proxy on the Brent basis that needs repair. |
| Sept national CPI, 2025 base (e-Stat) | headline **2.1** / core **2.1** / core-core **2.4** | Core above 2% for the first time in nine months, in line with forecasts. Tokyo Sept core-core 2.9 (+0.5pp vs National, 2nd exception in 6 paired months; not a signal). |
| FXY / VIX | FXY 58.08 (10/28 close) / VIX 16.97 (10/29 vendor) | FXY options: the Nov chain's 29.7% IV comes with a non-physical 42-vol risk reversal = thin chain, **not stress**; Dec reads 16.2%. HENRY owns US vol. |
| Funding / credit, FRED first-published | SOFR **3.95% (10/27)** vs IORB **3.90%** = **+5bp** (was −3bp 10/19); HY OAS **340bp 10/22 peak → 318bp 10/27** | Repo above the reserve rate into month-end; LIQUID owns the read. None measures offshore yen FX swaps. |

## CHANNELS · BOJ · FED

BOJ policy rate **1.25%** (September 18 decision). Ueda (October 6, 16): further hikes intended, pace conditional, no October signal. Bangkok ~10/16 (REPORTED paraphrase): underlying inflation close to 2%; further increases "can no longer" be tolerated. Ueda in the Diet **10/19** (Reuters, REPORTED): anchoring underlying inflation at 2% "becoming more important"; "failing to adjust our policy rate appropriately could push up long-term interest rates". **General, not an October framing**, and Reuters adds that many at the BOJ were wary of an October hike. **Nothing from Ueda, Himino or Uchida from 10/20 to the quiet period**: the BOJ speech index (last entry ko261016a) and press-conference index (last kk261020a, the Bangkok transcript) were checked by SAM at source 10/29, plus a press search. ⚠️ The Diet-record API returned 0 hits even for the reported 10/19 testimony, so that search is uninformative, not evidence of absence. Quiet period inferred from 10/27 (Daiwa glossary, not BOJ rule text). Pre-meeting reporting (REPORTED): Reuters 10/20 (hold "unless the yen renews its slide"), Kyodo 10/21, Nikkei 10/22, Reuters 10/26 "hawkish pause" (hold by majority; 2% nearly reached; overshoot risk stressed); Bloomberg survey 0% October / 83% December. Hold expected; Outlook may lift the FY2027 core forecast slightly on oil (July: FY2026 2.5 / FY2027 2.4); Takata likely dissents for a hike, Tamura uncertain. Market: October 2%, December 82% (Totan 10/29); Bloomberg OIS ~6.2% October odds 10/20–21 (REPORTED, separate basis). Services PPI Sept +3.7% y/y (PRIMARY; +2.9% ex-international transport). Rengo's 2027 demand is "6% centre, ≥5%" (above 2026). Sources → sweep §§1, 7.

**SAM-33 ops audit, October complete (verified at the record 10/29):** October 21 1–3Y ¥330.0B / 5–10Y ¥305.0B / 25Y+ ¥75.0B; October 28 3–5Y ¥290.0B / 5–10Y ¥305.0B / linkers ¥30.0B. All six purchase days match the September 30 quarterly plan (`mpr260930a.pdf`) on **date and size**. Other days: securities lending only; 10/27 dollar operation zero take-up; 10/27 ¥800B pooled-collateral funds supply (floating, 1.25%). **No fixed-rate or unscheduled JGB purchase October 21–29. Falsifier un-fired; OPEN through Dec-31.** November dates due 10/30 17:00 JST (docket row added).

**Channel 1 RETIRED.** Reactivation requires direct net foreign-credit SALES across ≥2 windows at ≥2 of the registered Big-3/Norinchukin set. **H2 FY2026 insurer plans (REPORTED interviews Oct 15–26, PLANS not executed flows):** in Reuters' 10-major roundup (10/27), yen-bond balances fall at 4 (Nippon, Dai-ichi), rise at 3 (Taiyo, Fukoku) and are flat at 3 (Meiji Yasuda, Japan Post Insurance). Super-long buying is mostly low-to-high-coupon **swaps**, not net new money; Meiji Yasuda calls 30Y at 4% attractive. Open foreign bonds are **cut** at Dai-ichi, Meiji Yasuda, Sumitomo, Fukoku and Taiju; flat at Asahi (reversing a planned cut); **flat to up at Nippon Life**. Hedged books are tilting to floating/private credit. **No insurer stated a UST-sale plan.** Year-end USD/JPY 155–162 (Nippon 160), so no repatriation-forcing yen view. Channel 1 reactivation test **not met**. These are the counter-signal's context, not its refutation: September's executed sector dispositions (−¥288.6B) stand. Profiles → `insurers/TRACKER.md`; detail → sweep §5.

**Fiscal:** food-tax/support bill (8→1% from Apr-2027 for two years) in Lower House deliberation since October 20; the ruling bloc aims to enact by session end Dec-12, funding (~¥10T over two years) unspecified, minority in the Upper House. **A bill, not enacted policy.** A second FY2026 supplementary is reported as "small-scale"; no JGB issuance-plan change or rating action found Oct 20–29.

## US TRANSMISSION — working interpretation, October 20 (unchanged)

**Orderly allocation adjustment is consistent with the evidence; the funding link is not established.** Slower reinvestment removes buying support; active sales add pressure; other buyers and US fundamentals set the net. US asset identity, maturity, hedges and yen conversion remain unknown. A separate fast yen/funding shock could force leveraged equity sales, and Treasuries can rally in that stress while credit weakens. Common JGB/UST moves alone do not establish Japan-led transmission. Mechanisms → `thesis/THESIS.md` § US TRANSMISSION.

## INTERVENTION STATUS

Katayama (Diet, 10/27, REPORTED): watching markets "with a high sense of urgency", ready for "decisive action"; yen ~157.7. Mimura: nothing found. No rate check or intervention reported Oct 20–29; Oct 22 coverage explicitly notes no official action. Words do not upgrade the ladder. Completed ranges stayed under the fast-move bar; the largest was 1.66 yen on 10/22, toward yen strength (no intervention motive). Last official total **¥0 Aug-27→Sep-28**. Pending window Sep-29→Oct-28, release **~Oct-30** (cadence estimate). Japanese quarterly ~Nov-9, FRBNY Q3 ~Nov-13 (estimates). Ladder at inherited T2-equivalent. Sources/ladder → `STATUS_REFERENCE.md`, `MOF_INTERVENTION_PLAYBOOK.md`.

## KEY THRESHOLDS

| Condition | Current observation / consequence |
|---|---|
| USD/JPY 160 / <155 / <147 | 10/28 completed close **157.832**: below 160, above 155/147. Investigation levels; no automatic entry. |
| Fast yen move ≥1.5–2%/day or ~2–3 yen in 1–2 sessions | Largest 10/22: −0.91%, 1.66-yen range. No fire. |
| JGB 10Y 2.40 / 30Y 4.0% | 10Y **2.867** above; 30Y **3.941** now below 4.0 (MOF 10/28). SAM-33's activation (August) is historical and stays lifted. |
| JGB 30Y 4.5% | **55.9bp away** (MOF 10/28); disorderly-impairment mechanism contested. |
| One-week foreign LT-debt selling >¥1.5T | 10/11–17 −¥160.5B, 10/18–24 −¥92.6B: both inside. |
| VECTOR-5 | **NONE**; oil benchmark repair owed. |
| Retired CFTC −108K / −140K / −153K | Moot at net +69,878 LONG. |

USD/JPY basis: WQ-162 own hourly bars, completed London-labelled sessions → `STATUS_REFERENCE.md` § USD/JPY MEASUREMENT BASIS.

## CARRY UNWIND PROBABILITY

August 7 **7d~3 / 30d~8 / 60d~13** is a **historical decomposed assessment**, not a current forecast; no fresh probability system declared. Two live stress tests passed without a Japan-led unwind signature: the 10/22 Asia selloff (yen modestly stronger, orderly) and the 10/26 Brazil shock (yen weaker; BRL/JPY −6.5% vs MXN/JPY +1.4% per WALTER's intraday snapshot). Offshore yen basis still missing.

## WHAT TO WATCH

| Date / clock | Next observation |
|---|---|
| **Oct-30 ~noon JST = Oct-29 ~23:00 ET** | BOJ decision + Outlook Report. **SAM-42 grades on `k261030a.pdf`** (announced target; JST); FALSE if ≤1.25% at Oct-31 23:59 JST. |
| Oct-30 08:30 JST = Oct-29 19:30 ET | Tokyo October CPI, 2025 base. |
| Oct-30 17:00 JST | BOJ November purchase dates (SAM-33). |
| ~Oct-30 (estimate) | MOF monthly intervention total, Sep-29→Oct-28. |
| Nov-3 | Japan holiday (Culture Day); Tokyo markets closed. |
| Nov-5 08:50 JST | September MPM minutes; 10Y auction. |
| Nov-9 / Nov-13 (estimates) | MOF quarterly; FRBNY Q3 FX report. |
| Nov-10 | 30Y auction (frozen FIRM/SOFT bars); Summary of Opinions for this MPM; US CPI. |

Full forward feed → `docket/CALENDAR.md` / `docket/CATALYSTS.tsv`. Still owed: oil-benchmark repair, direct offshore basis, matched intraday Sep attribution.

## POSITION — FLAT (last Will confirmation June 29)

No FXY position was opened under the retired convexity-tail episode; $0 was at risk in that frame. No new broker reconciliation, entry, roll or execution. Re-entry requires a separately argued thesis, review and Will approval; trade construction belongs to TERRY.

## PREDICTIONS

**16 CONFIRMED / 15 FAILED / 1 special / 1 qualified / 2 OPEN**, 35 validated rows; canonical `thesis/PREDICTIONS.tsv`. No mark, terms or status changed this session.

- **SAM-33:** 72%, no emergency/unscheduled cap of a GRADUAL super-long rise through Dec-31. October audited complete at the record, falsifier un-fired. A disorderly-spike response and scheduled taper adjustments are excluded.
- **SAM-42:** 25% as made (WQ-336), BOJ target >1.25% by Oct-31 23:59 JST. Neither re-mark trigger fired: (a) no named-official October framing (BOJ speech and press-conference indexes checked at source 10/29; Ueda's reported 10/19 Diet remark is general, not October-specific; Diet record unsearchable at this lag); (b) reviewed Totan 10/29 = **2%**, far below 60%. Registered below the then-market (36%); the market has since moved far below SAM. Grade on the statement PDF only.
- **SAM-28:** RESOLVED QUALIFIED / NO-VERDICT. **SAM-39:** TRUE-IN-LETTER / FALSE-IN-SPIRIT; successor owes a SHAPE leg.
- **SAM-31:** yen-haven re-couples by Sep-18, 35%, 🔴 **RESOLVED FALSE — always cite WITH its qualification**: interpretive owner judgement on same-clock evidence (n=24 risk-off, yen stronger 7 = 29.2%). ① strict single-episode reading = **QUALIFIED** (9/8–9/9 attribution OPEN); ② a window mean cannot exclude a LATE return; ③ 7/13 unresolved. **Matched intraday cross-pair data settles ①–③ and is owed; if obtained the row is re-openable.** → `STATUS_ARCHIVE.md`; [ruling](docket/2026-09-19_CATO-R4-RULING.md).
- RED VX-026: **RESOLVED-CONFIRM-DEAD** effective 2026-08-07 (RED S53 conceded SAM's reading, 10/15). CH-012 open through the Dec-30 MOF close.

Thesis **v1.7** · peer synthesis → `NEXUS_BRIEF.md`.
