# SAM STATUS

**Last written: 2026-10-31 ~11:0x ET (Sat; 2026-11-01 ~00:0x JST) — PROME spawn, Will-approved read of the BOJ October 29–30 decision; SAM-42 graded; inbox drained (1 top-level + 7 WALTER).** Runtime Claude Code, model Opus 5.5 (`claude-opus-5-5`). Each row keeps its own source clock. Primary read and receipts → `research/outputs/2026-10-31_boj/BOJ_1030_READ.md`. Prior write 2026-10-29 ~08:00 ET (catch-up boot). Pull not attempted (other desks' trees dirty; 0 behind origin at fetch).

**View:** no fresh observed Japan-led carry unwind — **unchanged by the BOJ.** The Bank **held at 1.25% on 8–1** (Takata dissented for 1.5%) and its Outlook now says underlying inflation **"is at a level that is generally consistent with" 2%** (July: "approaching"), with price risks skewed up and the rate-hike sentence kept: a **hawkish hold** that keeps December live. The yen barely moved: USD/JPY 10/30 completed session **157.519 (−0.19%, 0.94-yen range)**, far below the fast-move bar. Speculators were already net **long** yen and added: CFTC **+101,591 (10/27, pre-decision)**, so the short-yen pool that unwound in August 2024 is still absent; offshore FX-swap funding stays unmeasured. **SAM-42 RESOLVED FALSE (FAILED), as-made 25%, Brier 0.0625.** Long end: 30Y 3.941 (MOF 10/28, not refreshed). **v1.7 retired-to-LOW, no successor frame, no entry, no re-mark.** Last Will-confirmed FLAT June 29 is a dated desk record, not a fresh broker reconciliation.

**BOJ October 29–30, PRIMARY (k261030a.pdf, gor2610a.pdf, retrieved 10/31 14:38Z):** hold 1.25%, 8–1; Takata: "underlying CPI inflation having reached the price stability target", proposed ~1.5%. ETF sales pace raised ~¥330B → **~¥860B/yr book (~¥2.46T market)** from January 2027, unanimous. **JGB purchase plan unchanged** (mpr261030c: every per-auction size equals the Sep-30 plan; November dates added). Outlook medians: core CPI FY26 2.5 (–) / **FY27 2.6 (+0.2)** / FY28 2.0; core-core 2.4 / 2.7 / 2.3; GDP 0.7 / 0.7 / 0.8. No date language for the next hike. Ueda's press conference and post-decision OIS NOT read. Pre-meeting sweep (10/29) context → `research/outputs/2026-10-29_sweep/NEWS_SWEEP.md`.

## LIVE MARKET DATA

| Instrument / release | Level and observation date | Assessment / limit |
|---|---|---|
| USD/JPY, completed London-label sessions | 10/22 156.721 (−0.91%, range 1.660) · 10/26 157.540 · 10/27 157.994 · 10/28 157.832 · **10/29 157.818 (−0.01%, 0.548) · 10/30 157.519 (−0.19%, range 0.941; H 157.898 / L 156.957)** | Own hourly aggregation, as-last-revised, read 10/31 14:4xZ; 10/30 has 21 bars (week close). Decision hour 03:00Z: 157.570 → close 157.413 (low 157.110). ⚠️ `fetch.py` daily 10/30 "157.80" is the session OPEN, not the close (vendor daily FX bar lags one session). |
| Crosses, vendor 10/29 04:19Z | EURJPY 175.79 / GBPJPY 210.12 / AUDJPY 111.23 | Individual vendor clocks; not a synchronized attribution study. |
| BOJ meeting OIS **10/29 11:15 JST** (Totan, SAM visual review, SHA `ec55624d…`) | **Oct 2% / OIS 1.2313%; Dec 82%; Jan 26%; Mar 56%; Apr 29%; cumulative Apr 1.94 hikes** | Arithmetic chain checked, live hash validated, 5 rows ingested. Incremental 25bp equivalents ≠ probabilities; counts ≠ probabilities. Indicative OTC medians, JST assumed. Decision expiry 10/30 — **SPENT; pre-decision, not re-read after the hold.** Was Oct 5% / Dec 76% on 10/20. |
| JGB curve, **MOF 10/28** | **2Y 1.915 / 5Y 2.281 / 10Y 2.867 / 20Y 3.685 / 30Y 3.941 / 40Y 3.974%** | Versus MOF 10/19: 10Y −6.8bp, 30Y −8.7bp. 30Y back below 4.0%. Do not difference vendor against MOF. |
| **2Y auction 10/29** | **BTC 4.031×; lowest 1.912 / average 1.905%; tail 0.7bp** | Orderly; front end, no frozen FIRM/SOFT bar at this tenor. MOF eresul20261029. |
| CFTC legacy JPY, **10/27**, rel 10/30 | **Net +101,591 LONG**, Δ +31,713; L 225,516 / S 123,925; OI 374,026 | Window ends BEFORE the BOJ decision. Outside the deadband, graded on its own print; no forced-liquidation inference. Ledger max +120,359 (9/15). Old short-side gates void. |
| MOF weekly foreign LT debt | **10/11–17 −¥160.5B · 10/18–24 −¥92.6B**; 4W −¥937.7B; 12W −¥2.44T | Both new weeks inside the ¥1.5T one-week bar, **each evaluated** (every-new-week reader repaired 10/29). Designated reporting investors, not insurer/UST-only. Rolling sums are live-CSV values; ledger keeps first prints. |
| MOF September investor-type, updated Oct-8 | Life insurers **−¥288.6B** (Aug −¥137.3B); banks −¥2,485.6B; trusts +¥1,195.3B | Carried from 10/20; sector selling, no named seller, UST specificity or forced-sale cause. October investor-type due ~Nov-10. |
| US–JP differential, **10/28** | **5Y 2.569pp / 10Y 2.183pp**, 0/5 through bars | Float-tie comparison repaired 10/29 (live history unchanged). FOMC 10/28 held 3.75–4.00% with **two hike dissents** keeps the US leg high. |
| Brent, named contracts (vendor) | **Jan BZF27 $110.20** (10/29 04:07Z; +1.42% vs 10/22); Dec BZZ26 $114.16 (expiry week) | Continuous BZ=F rolled 10/29 Dec→Jan: its −2.62% "move" is a contract switch, not a price move. Oil-benchmark repair still owed. |
| Sept trade balance, MOF customs (stage as parsed 10/29) | **−¥556.5B**; crude VOLUME 11,166 thousand kL **+3.1% YoY**, value +51.1%; LNG 4,779 kt −7.3%; ME crude volume **−30.0%** | Value rise is price, not volume; Middle East substitution continues. Implied unit cost ~$101/bbl is a proxy on the Brent basis that needs repair. |
| Sept national CPI, 2025 base (e-Stat) | headline **2.1** / core **2.1** / core-core **2.4** | Core above 2% for the first time in nine months, in line with forecasts. Tokyo Sept core-core 2.9 (+0.5pp vs National, 2nd exception in 6 paired months; not a signal). |
| FXY / VIX | FXY 58.08 (10/28 close) / VIX 16.97 (10/29 vendor) | FXY options: the Nov chain's 29.7% IV comes with a non-physical 42-vol risk reversal = thin chain, **not stress**; Dec reads 16.2%. HENRY owns US vol. |
| Funding / credit, FRED first-published | SOFR **3.95% (10/27)** vs IORB **3.90%** = **+5bp** (was −3bp 10/19); HY OAS **340bp 10/22 peak → 318bp 10/27** | Repo above the reserve rate into month-end; LIQUID owns the read. None measures offshore yen FX swaps. |

## CHANNELS · BOJ · FED

BOJ policy rate **1.25%** (September 18 decision; **held October 30, 8–1**). Ueda (October 6, 16): further hikes intended, pace conditional, no October signal. Bangkok ~10/16 (REPORTED paraphrase): underlying inflation close to 2%; further increases "can no longer" be tolerated. Ueda in the Diet **10/19** (Reuters, REPORTED): anchoring underlying inflation at 2% "becoming more important"; "failing to adjust our policy rate appropriately could push up long-term interest rates". **General, not an October framing**, and Reuters adds that many at the BOJ were wary of an October hike. **Nothing from Ueda, Himino or Uchida from 10/20 to the quiet period**: the BOJ speech index (last entry ko261016a) and press-conference index (last kk261020a, the Bangkok transcript) were checked by SAM at source 10/29, plus a press search. ⚠️ The Diet-record API returned 0 hits even for the reported 10/19 testimony, so that search is uninformative, not evidence of absence. Quiet period inferred from 10/27 (Daiwa glossary, not BOJ rule text). Pre-meeting reporting (REPORTED): Reuters 10/20 (hold "unless the yen renews its slide"), Kyodo 10/21, Nikkei 10/22, Reuters 10/26 "hawkish pause" (hold by majority; 2% nearly reached; overshoot risk stressed); Bloomberg survey 0% October / 83% December. Hold expected; Outlook may lift the FY2027 core forecast slightly on oil (July: FY2026 2.5 / FY2027 2.4); Takata likely dissents for a hike, Tamura uncertain. Market: October 2%, December 82% (Totan 10/29); Bloomberg OIS ~6.2% October odds 10/20–21 (REPORTED, separate basis). Services PPI Sept +3.7% y/y (PRIMARY; +2.9% ex-international transport). Rengo's 2027 demand is "6% centre, ≥5%" (above 2026). Sources → sweep §§1, 7.

**SAM-33 ops audit, October complete (verified at the record 10/29):** October 21 1–3Y ¥330.0B / 5–10Y ¥305.0B / 25Y+ ¥75.0B; October 28 3–5Y ¥290.0B / 5–10Y ¥305.0B / linkers ¥30.0B. All six purchase days match the September 30 quarterly plan (`mpr260930a.pdf`) on **date and size**. Other days: securities lending only; 10/27 dollar operation zero take-up; 10/27 ¥800B pooled-collateral funds supply (floating, 1.25%). **No fixed-rate or unscheduled JGB purchase October 21–29. Falsifier un-fired; OPEN through Dec-31.** **November dates READ (mpr261030c, 10/31):** ≤1Y 11/4 · 1–3Y 11/4, 11/11 · 3–5Y 11/19, 11/26 · 5–10Y 11/11, 11/19 · 10–25Y 11/11, 11/26 · 25Y+ 11/4, 11/19 · linkers 11/26; sizes identical to the Sep-30 plan. December dates due Nov-30 17:00 JST.

**Channel 1 RETIRED.** Reactivation requires direct net foreign-credit SALES across ≥2 windows at ≥2 of the registered Big-3/Norinchukin set. **H2 FY2026 insurer plans (REPORTED interviews Oct 15–26, PLANS not executed flows):** in Reuters' 10-major roundup (10/27), yen-bond balances fall at 4 (Nippon, Dai-ichi), rise at 3 (Taiyo, Fukoku) and are flat at 3 (Meiji Yasuda, Japan Post Insurance). Super-long buying is mostly low-to-high-coupon **swaps**, not net new money; Meiji Yasuda calls 30Y at 4% attractive. Open foreign bonds are **cut** at Dai-ichi, Meiji Yasuda, Sumitomo, Fukoku and Taiju; flat at Asahi (reversing a planned cut); **flat to up at Nippon Life**. Hedged books are tilting to floating/private credit. **No insurer stated a UST-sale plan.** Year-end USD/JPY 155–162 (Nippon 160), so no repatriation-forcing yen view. Channel 1 reactivation test **not met**. These are the counter-signal's context, not its refutation: September's executed sector dispositions (−¥288.6B) stand. Profiles → `insurers/TRACKER.md`; detail → sweep §5.

**Fiscal:** food-tax/support bill (8→1% from Apr-2027 for two years) in Lower House deliberation since October 20; the ruling bloc aims to enact by session end Dec-12, funding (~¥10T over two years) unspecified, minority in the Upper House. **A bill, not enacted policy.** A second FY2026 supplementary is reported as "small-scale"; no JGB issuance-plan change or rating action found Oct 20–29.

## US TRANSMISSION — working interpretation, October 20 (unchanged)

**Orderly allocation adjustment is consistent with the evidence; the funding link is not established.** Slower reinvestment removes buying support; active sales add pressure; other buyers and US fundamentals set the net. US asset identity, maturity, hedges and yen conversion remain unknown. A separate fast yen/funding shock could force leveraged equity sales, and Treasuries can rally in that stress while credit weakens. Common JGB/UST moves alone do not establish Japan-led transmission. Mechanisms → `thesis/THESIS.md` § US TRANSMISSION.

## INTERVENTION STATUS

Katayama (Diet, 10/27, REPORTED): watching markets "with a high sense of urgency", ready for "decisive action"; yen ~157.7. Mimura: nothing found. No rate check or intervention reported Oct 20–29; Oct 22 coverage explicitly notes no official action. Words do not upgrade the ladder. Completed ranges stayed under the fast-move bar; the largest was 1.66 yen on 10/22, toward yen strength (no intervention motive). Official totals **¥0 Aug-27→Sep-28** and **¥0 Sep-29→Oct-28** (MOF `20261030e.html`, read at source 10/31). Japanese quarterly ~Nov-9, FRBNY Q3 ~Nov-13 (estimates). Ladder at inherited T2-equivalent. Sources/ladder → `STATUS_REFERENCE.md`, `MOF_INTERVENTION_PLAYBOOK.md`.

## KEY THRESHOLDS

| Condition | Current observation / consequence |
|---|---|
| USD/JPY 160 / <155 / <147 | 10/30 completed close **157.519**: below 160, above 155/147. Investigation levels; no automatic entry. |
| Fast yen move ≥1.5–2%/day or ~2–3 yen in 1–2 sessions | Largest 10/22: −0.91%, 1.66-yen range; BOJ day 10/30 −0.19%, 0.94 yen. No fire. |
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
| Nov-2 14:00 JST | Outlook Report full text (boxes behind the 'at 2%' judgment). |
| Carried, NOT read 10/31 | Tokyo October CPI (10/30); Ueda 10/30 press conference; post-decision Totan OIS. |
| Nov-3 | Japan holiday (Culture Day); Tokyo markets closed. |
| Nov-5 08:50 JST | September MPM minutes; 10Y auction. |
| Nov-9 / Nov-13 (estimates) | MOF quarterly; FRBNY Q3 FX report. |
| Nov-10 | 30Y auction (frozen FIRM/SOFT bars); Summary of Opinions for this MPM; US CPI. |
| Nov-30 17:00 JST | BOJ December purchase dates (SAM-33). |

Full forward feed → `docket/CALENDAR.md` / `docket/CATALYSTS.tsv`. Still owed: oil-benchmark repair, direct offshore basis, matched intraday Sep attribution.

## POSITION — FLAT (last Will confirmation June 29)

No FXY position was opened under the retired convexity-tail episode; $0 was at risk in that frame. No new broker reconciliation, entry, roll or execution. Re-entry requires a separately argued thesis, review and Will approval; trade construction belongs to TERRY.

## PREDICTIONS

**16 CONFIRMED / 16 FAILED / 1 special / 1 qualified / 1 OPEN [SAM-33]**, 35 validated rows; canonical `thesis/PREDICTIONS.tsv`. Only change this session: SAM-42 resolved (status, outcome, notes); no mark or terms changed.

- **SAM-33:** 72%, no emergency/unscheduled cap of a GRADUAL super-long rise through Dec-31. October audited complete at the record, falsifier un-fired. A disorderly-spike response and scheduled taper adjustments are excluded.
- **SAM-42:** 🔴 **RESOLVED FALSE → FAILED** (graded after 2026-10-31 23:59 JST): BOJ statement `k261030a.pdf` (Oct 30, 12:02 JST) set the target at **around 1.25%**, 8–1; the only MPM in the window. As-made **25%** P(hike): SAM's lean against October was right; Brier **0.0625** (frozen Totan 9/29 reference 36% would score 0.1296). Neither re-mark trigger ever fired. The decisive information (market to 2% by 10/29) arrived after registration — the score credits the as-made call, nothing more. → `research/outputs/2026-10-31_boj/BOJ_1030_READ.md`.
- **SAM-28:** RESOLVED QUALIFIED / NO-VERDICT. **SAM-39:** TRUE-IN-LETTER / FALSE-IN-SPIRIT; successor owes a SHAPE leg.
- **SAM-31:** yen-haven re-couples by Sep-18, 35%, 🔴 **RESOLVED FALSE — always cite WITH its qualification**: interpretive owner judgement on same-clock evidence (n=24 risk-off, yen stronger 7 = 29.2%). ① strict single-episode reading = **QUALIFIED** (9/8–9/9 attribution OPEN); ② a window mean cannot exclude a LATE return; ③ 7/13 unresolved. **Matched intraday cross-pair data settles ①–③ and is owed; if obtained the row is re-openable.** → `STATUS_ARCHIVE.md`; [ruling](docket/2026-09-19_CATO-R4-RULING.md).
- RED VX-026: **RESOLVED-CONFIRM-DEAD** effective 2026-08-07 (RED S53 conceded SAM's reading, 10/15). CH-012 open through the Dec-30 MOF close.

Thesis **v1.7** · peer synthesis → `NEXUS_BRIEF.md`.
