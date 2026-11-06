# SAM STATUS

**Last written: 2026-11-06 15:48 ET (Fri; Sat 11/7 JST) — PROME C9 on SoftBank's reduced OpenAI check beside card 003, plus Will's funding-stack question (WQ-643); inbox drained.** Runtime Claude Code, model Opus 5.5 (`claude-opus-5-5`). Each row keeps its own source clock. Reads → `research/outputs/2026-11-06_softbank/` (funding stack governs on leverage). Prior write 2026-10-31 (BOJ read). Pull not needed: 0 behind origin at fetch; other desks' trees dirty.

**View:** no fresh observed Japan-led carry unwind, **tested again 11/6 and unchanged.** Tokyo fell 5.96% (Nikkei) and the yen **weakened** through the session (USD/JPY 157.48 → 158.14 in cash hours, 0.75-yen range), so it was a rate repricing, not an unwind: BOJ December pricing dropped to **52%** (Totan 11/6 15:15 JST; 82% on 10/29, pre-decision; model-dependent equivalents, not probabilities) while Fed December hike odds rose to about 77–79% after payrolls (card 017). The risk has moved from a December hike to a December skip and a weaker yen near 160. Speculators were net long yen going in (CFTC 11/3 **+102,321**, a window that ended before the selloff), so the short-yen pool of August 2024 was absent; offshore FX-swap funding stays unmeasured. **v1.7 retired-to-LOW, no successor frame, no entry, no re-mark.** Last Will-confirmed FLAT June 29 is a dated desk record, not a fresh broker reconciliation.

**SoftBank (filing-based, `SOFTBANK_FUNDING_STACK.md`):** the reduced check means nothing for Japan by itself: ¥48B–143B, on a $64.6B stake completed 10/1. **The $40B bridge is gone**: repaid 9/15, undrawn $10B cancelled 9/30; the nearest large maturity is now the Arm margin loan, about $25B, 9/2027 (relay). **Leverage: the quoted 13% is 6/30 only. SAM estimate about 22% on SoftBank's definition, about 24% counting the $10B OpenAI loan SoftBank Group guarantees, against its own 25% ceiling, reached at Arm about $128 and $160.** That loan (8/2028; filing) carries a fair-value trigger on OpenAI. Unusual: the guarantee, the trigger, about 83% of Arm pledged (May, relay), and SoftBank as OpenAI's investor and, through SB Energy, its landlord (Milam, PORTS-Pike 8.0 GW; NVIDIA guarantees up to $105B of that rent, not SoftBank). **No SoftBank–Oracle credit tie found: a shared counterparty in OpenAI, not one loan chain.** No bank or household break found; per-bank exposure undisclosed. Results **Tue 11/10 15:30 JST**: the headline LTV will be at 9/30, Arm $289.66, before the October tranche, about 14–17%, some 7 points kinder than today.


**BOJ October 29–30, PRIMARY (k261030a.pdf, gor2610a.pdf, retrieved 10/31 14:38Z):** hold 1.25%, 8–1; Takata: "underlying CPI inflation having reached the price stability target", proposed ~1.5%. ETF sales pace raised ~¥330B → **~¥860B/yr book (~¥2.46T market)** from January 2027, unanimous. **JGB purchase plan unchanged** (mpr261030c: every per-auction size equals the Sep-30 plan; November dates added). Outlook medians: core CPI FY26 2.5 (–) / **FY27 2.6 (+0.2)** / FY28 2.0; core-core 2.4 / 2.7 / 2.3; GDP 0.7 / 0.7 / 0.8. No date language for the next hike. Ueda's press conference and post-decision OIS NOT read. Pre-meeting sweep (10/29) context → `research/outputs/2026-10-29_sweep/NEWS_SWEEP.md`.

## LIVE MARKET DATA

| Instrument / release | Level and observation date | Assessment / limit |
|---|---|---|
| USD/JPY, completed London-label sessions | 10/30 157.519 · 11/2 157.918 · 11/3 158.462 · 11/4 158.373 (range 1.290) · **11/5 157.492 (−0.56%, range 1.254; H 158.503 / L 157.249)**. **11/6 live ~158.5, +0.64%, range so far 1.241, NOT a completed session, not scored** | Own hourly aggregation, read 11/6 ~20:20Z. Tokyo cash hours 11/6 (00:00–06:30Z): 157.48 → 158.14, range 0.753. ⚠️ `fetch.py` daily is unreliable for sessions (vendor daily bar offset). |
| Crosses, vendor 11/6 ~20:15Z | EURJPY 176.55 / GBPJPY 211.62 / AUDJPY 108.85 | AUD/JPY −1.6% on 11/5 and −0.3% live, mostly AUD weakness (AUD/USD −1.1%, −0.9%). Individual vendor clocks; not a synchronized attribution study. |
| BOJ meeting OIS **11/6 15:15 JST** (Totan, SAM visual review, SHA `802f8a6c…`) | **Dec 52% / OIS 1.3575%; Jan 27%; Mar 40%; Apr 19%; Jun 29%; cumulative Apr 1.38 (10/29: 1.94), Jun 1.67 hikes** | Arithmetic chain checked, live hash validated, 5 rows ingested. Incremental 25bp equivalents ≠ probabilities; counts ≠ probabilities. Indicative OTC medians, JST assumed. Was Dec 82% on 10/29, pre-decision; ⚠️ no reviewed chart between, so not all one day. Reuters 11/6 prints 42% hike, a separate basis. Valid to the 12/18 decision, four-day age limit applies. |
| JGB curve, **MOF 11/5** | **2Y 1.860 / 5Y 2.210 / 10Y 2.806 / 20Y 3.640 / 30Y 3.915 / 40Y 3.929%** | MOF 11/6 not yet published. Vendor 11/6, a separate on-the-run basis, never differenced against MOF: Reuters 2Y 1.72 (−13.5bp), 5Y 2.025 (−16.5), 10Y 2.61 (−14.5, lowest since 6/26), 20Y 3.51 (−8.5), 30Y 3.805 (−4). Fisco close 10Y 2.629, Kyodo 2.635. Front-led; long end held by oil. |
| **10Y auction 11/5** | **BTC 3.213×; lowest 2.800 / average 2.768%; tail 3.2bp**; 2Y 10/29 BTC 4.031×, tail 0.7bp | MOF. Script label orderly; no frozen FIRM/SOFT bar at this tenor, and I draw no grade. Next frozen-bar test 30Y 11/10. |
| CFTC legacy JPY, **11/3**, rel 11/6 | **Net +102,321 LONG**, Δ +730; L 227,198 / S 124,877; OI 380,641 | Inside the ±12,160 deadband. ⚠️ Window ends 11/3, BEFORE the 11/5–6 selloff: this is positioning going in, not the reaction; the 11/10 print, released 11/13, is next. No forced-liquidation inference. Ledger max +120,359 (9/15). Old short-side gates void. |
| MOF weekly foreign LT debt | 10/11–17 −¥160.5B · 10/18–24 −¥92.6B · **10/25–31 +¥1.312T net BUYING** | All inside the ¥1.5T one-week selling bar, each evaluated. Designated reporting investors, not insurer/UST-only. Pre-dates the selloff. Rolling sums are live-CSV values; ledger keeps first prints. |
| MOF September investor-type, updated Oct-8 | Life insurers **−¥288.6B** (Aug −¥137.3B); banks −¥2,485.6B; trusts +¥1,195.3B | Carried from 10/20; sector selling, no named seller, UST specificity or forced-sale cause. October investor-type due ~Nov-10. |
| US–JP differential, **11/5** | **5Y 2.380pp / 10Y 2.034pp** | Boot ledger, pre-selloff. 11/6 widens on both legs (JGB down, UST up after payrolls); not computed across bases. FOMC 10/28 held 3.75–4.00% with two hike dissents; December hike odds ~77–79% (card 017, press reads). |
| Brent (vendor) | BZ=F **$98.46** (11/6 20:04Z, not a settle); Jan $98.29 11/5 settle per BRENT [EST], card 065 | ⚠️ Roll guard failed closed at boot: no percentage across the window. Oil-benchmark repair still owed. BRENT owns marks. |
| Sept trade balance, MOF customs (stage as parsed 10/29) | **−¥556.5B**; crude VOLUME 11,166 thousand kL **+3.1% YoY**, value +51.1%; LNG 4,779 kt −7.3%; ME crude volume **−30.0%** | Value rise is price, not volume; Middle East substitution continues. Implied unit cost ~$101/bbl is a proxy on the Brent basis that needs repair. |
| CPI, 2025 base (e-Stat) | Sept National **2.1 / 2.1 / 2.4** · **Tokyo Oct 2.8 / 2.6 / 2.6** (headline / core / core-core, boot ingest 11/6, not yet analysed) | Sept core above 2% for the first time in nine months. Next National 11/20. |
| FXY / VIX | FXY 57.80 (11/6 vendor, live) / VIX 24.46 (11/6 vendor, live; 16.61 on 11/4, 28.18 on 11/5) | FXY options skipped at boot (`--quick`). HENRY owns US vol. |
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
| USD/JPY 160 / <155 / <147 | 11/5 completed **157.492**; live ~158.5, 1.5 yen below 160. Investigation levels; no automatic entry. |
| Fast yen move ≥1.5–2%/day or ~2–3 yen in 1–2 sessions | 11/5 −0.56%, 1.254 yen; 11/6 live +0.64%, 1.241 so far; two-session span 1.40 yen. No fire on a −5.96% Tokyo day. |
| JGB 10Y 2.40 / 30Y 4.0% | 10Y **2.806** above; 30Y **3.915** below 4.0 (MOF 11/5). SAM-33's activation (August) is historical and stays lifted. |
| JGB 30Y 4.5% | **58.5bp away** (MOF 11/5); disorderly-impairment mechanism contested. |
| One-week foreign LT-debt selling >¥1.5T | 10/25–31 **+¥1.312T** buying: inside. |
| VECTOR-5 | **NONE**; oil benchmark repair owed. |
| Retired CFTC −108K / −140K / −153K | Moot at net +102,321 LONG (11/3). |

USD/JPY basis: WQ-162 own hourly bars, completed London-labelled sessions → `STATUS_REFERENCE.md` § USD/JPY MEASUREMENT BASIS.

## CARRY UNWIND PROBABILITY

August 7 **7d~3 / 30d~8 / 60d~13** is a **historical decomposed assessment**, not a current forecast; no fresh probability system declared. Two live stress tests passed without a Japan-led unwind signature: the 10/22 Asia selloff (yen modestly stronger, orderly) and the 10/26 Brazil shock (yen weaker; BRL/JPY −6.5% vs MXN/JPY +1.4% per WALTER's intraday snapshot). Offshore yen basis still missing.

## WHAT TO WATCH

| Date / clock | Next observation |
|---|---|
| Carried, NOT read | Ueda 10/30 press conference; Outlook full text (11/2); September minutes (11/5); Tokyo Oct CPI analysis. |
| Nov-9 (est.) / Nov-9 | MOF quarterly; SoftBank Corp results. |
| **Nov-10** | **SoftBank Group results 15:30 JST**, briefing 16:30: read list → funding stack §6. Summary of Opinions (written before the selloff, so hawkish against new pricing, not a reaction); 30Y auction (frozen bars); US CPI. |
| Nov-13 | FRBNY Q3 (est.); GMO Internet results briefing (compensation cost, CYPHER). |
| Nov-16 | Japan Q3 GDP. |
| Nov-30 17:00 JST | BOJ December purchase dates (SAM-33). |
| Dec-17–18 | BOJ MPM. |

Full forward feed → `docket/CALENDAR.md` / `docket/CATALYSTS.tsv`. Still owed: oil-benchmark repair, direct offshore basis, matched intraday Sep attribution.

## POSITION — FLAT (last Will confirmation June 29)

No FXY position was opened under the retired convexity-tail episode; $0 was at risk in that frame. No new broker reconciliation, entry, roll or execution. Re-entry requires a separately argued thesis, review and Will approval; trade construction belongs to TERRY.

## PREDICTIONS

**16 CONFIRMED / 16 FAILED / 1 special / 1 qualified / 1 OPEN [SAM-33]**, 35 validated rows; canonical `thesis/PREDICTIONS.tsv`. No change 11/6: no prediction moved, no mark or terms changed. SAM-33 November ops not audited this session.

- **SAM-33:** 72%, no emergency/unscheduled cap of a GRADUAL super-long rise through Dec-31. October audited complete at the record, falsifier un-fired. A disorderly-spike response and scheduled taper adjustments are excluded.
- **SAM-42:** 🔴 **RESOLVED FALSE → FAILED** (graded after 2026-10-31 23:59 JST): BOJ statement `k261030a.pdf` (Oct 30, 12:02 JST) set the target at **around 1.25%**, 8–1; the only MPM in the window. As-made **25%** P(hike): SAM's lean against October was right; Brier **0.0625** (frozen Totan 9/29 reference 36% would score 0.1296). Neither re-mark trigger ever fired. The decisive information (market to 2% by 10/29) arrived after registration — the score credits the as-made call, nothing more. → `research/outputs/2026-10-31_boj/BOJ_1030_READ.md`.
- **SAM-28:** RESOLVED QUALIFIED / NO-VERDICT. **SAM-39:** TRUE-IN-LETTER / FALSE-IN-SPIRIT; successor owes a SHAPE leg.
- **SAM-31:** yen-haven re-couples by Sep-18, 35%, 🔴 **RESOLVED FALSE — always cite WITH its qualification**: interpretive owner judgement on same-clock evidence (n=24 risk-off, yen stronger 7 = 29.2%). ① strict single-episode reading = **QUALIFIED** (9/8–9/9 attribution OPEN); ② a window mean cannot exclude a LATE return; ③ 7/13 unresolved. **Matched intraday cross-pair data settles ①–③ and is owed; if obtained the row is re-openable.** → `STATUS_ARCHIVE.md`; [ruling](docket/2026-09-19_CATO-R4-RULING.md).
- RED VX-026: **RESOLVED-CONFIRM-DEAD** effective 2026-08-07 (RED S53 conceded SAM's reading, 10/15). CH-012 open through the Dec-30 MOF close.

Thesis **v1.7** · peer synthesis → `NEXUS_BRIEF.md`.
