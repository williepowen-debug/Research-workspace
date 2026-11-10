# NEXUS digest — reader B (10 briefs)

Written 2026-11-10 11:14 EST (from `date`). Read-only; every brief read whole via `cat`. Baseline for "MOVED SINCE" = NEXUS last pass 2026-11-04 ~15:37 ET. Figures are quoted as the briefs state them; no arithmetic of mine. `[?]` = I am unsure of the date or vintage.

## Pin check (`python3 scripts/brief_pin_check.py ... --quiet`, rc=0; per-desk lines from a re-run without `--quiet`)

`BRIEF-PIN 0 OK: 10 brief(s) — OK-PINNED 5 · OK-SAME-COMMIT 4 · UNPINNED 1.` A PASS proves the pin, not the content.

| Desk | Verdict | Brief size / last commit |
|---|---|---|
| BRENT | ⚠️ UNPINNED: "no STATUS hash in the first 40 header lines — A11 not checkable; A10 fallback: brief commit 8cf784d32 is AFTER STATUS HEAD 41fba0cc9" | 26,045 B ⚠️ over-long / 2026-11-10 10:12 |
| VULCAN | ✅ OK-PINNED 14b33c9675 | 13,407 B / 11-10 10:12 |
| ZHAO | ✅ OK-SAME-COMMIT 05d6d6e72 | 14,587 B / 11-09 19:38 |
| CORAL | ✅ OK-SAME-COMMIT d673dd41d | 14,490 B / 11-09 13:00 |
| OSPREY | ✅ OK-PINNED e4bc891bb9 | 12,863 B / 11-09 12:12 |
| FALCON | ✅ OK-PINNED 9c7c5f946e | 14,931 B / 11-09 10:55 |
| ORACLE | ✅ OK-SAME-COMMIT 8cbeac5ec | 5,954 B / 11-09 10:51 (figures 11/06–11/08 only) |
| CYPHER | ✅ OK-PINNED 063fde11b0… | 12,257 B / 11-08 12:07 |
| MIDAS | ✅ OK-SAME-COMMIT f9c4a3028 | 18,214 B ⚠️ long, not in schema shape / 11-08 12:06 |
| WATT | ✅ OK-PINNED c153b55a6 | 12,356 B / 11-05 18:39 ⚠️ oldest brief here |

---

## BRENT

- **HEADER:** As of "November 10 boot-only closeout (2026-11-10 10:12 EST, laptop→desktop switch) — SCOPED-PARTIAL: NOTHING re-verified; no content changed; every row keeps its stated vintage." The latest content vintage is the 11/9 reopen at 14:49 EST. No STATUS hash in the header, hence UNPINNED. Thesis v5.13.
- **⚠️ STALE / LONG:** 26 KB. The As-of chain alone is a run-on paragraph. The 11/10 stamp re-verified nothing, so it is not fresh content. The SCOPE paragraph is the 10/29 vintage.
- **VIEW:** Energy WAIT is retained. The 11/4 fall "needs no physical change to explain it, and none is measured". Crack compression counts against scarcity and the distillate draw counts for it. The desk still separates persistent product scarcity from recovering crude.
- **MOVED SINCE 11/4:**
  - **11/4 marks** (PROME memo; it may be at or after the pass `[?]`): BZF27 $94.62, CLZ26 $88.12, M1−M3 +$4.50 window proxy, Dated Brent $107.03 on 11/3. EIA week 10/30: crude −0.865M, distillate −3.565M to 99.259M, Cushing 27.250M, utilization 94.5%. January 3:2:1 $35.71–$39.09, count 0. Kpler Hormuz crude 7.3 mb/d in the week to 10/28 (relayed) against a 13.5 baseline. Fade <$78 NOT MET at $94.62.
  - **Status line:** US distillate stocks 99.259M (week 10/30), "lowest since 5/2/2003, about 23.8 days of cover [CONF EIA; cover own arithmetic]". December crack "about $91 vendor window". Front over fourth 28.75¢.
  - **11/5:** BZF27 $98.29, CLZ26 $90.52 [EST wire]. Same-minute M1−M3 +$6.10 to +$6.33. Boundary #8 $37.15, count 0. Card 058 **BG-02 NOT MET**. Yanbu flow NOT MEASURABLE, "about 2.5 mb/d exposed on October Vortexa [secondary]". Card 056 signature NOT MET. New forecasts on 11/5: **BRT-32** Yanbu loading halt 20%, **BRT-33** F-a crossing by 11/27 20%, **BRT-34** distillate under 95M 45%, **BRT-35** retail under $4 70%.
  - **11/5 trade:** "original VLO share sold November 5 at $366.665, −$45.33; HELD-01 discharged."
  - **11/6 window:** BZF27 98.35, CLZ26 90.8551, January 3:2:1 $37.19, December crack $91.12 [EST vendor, not settles]. M1−M3 NOT MEASURABLE; same-minute +$5.04. BRT-33 valid 0 of 1. Diesel read **PRICED**: 39 weeks against the 5-yr, exports −79.1M, production +77.8M, demand −3.5M. Card 018: no lost barrel established.
  - **11/6 close:** BZF27 $98.32, CLZ26 $90.83 [EST wire]. Same-contract week: BZF27 −13.3%, CLZ26 −12.8%. January 3:2:1 $37.18. Month-matched WTI−Brent −$8.75. Unverified: Bloomberg via Rigzone says Saudi and UAE shipments are back to prewar levels. After the close, Qeshm "not established as a US strike (card 047)".
  - **11/8 pre-reopen:** BZH27 $93.30; daily-row M1−M3 +$5.02, not a window observation. Aramco December Asia OSP −$2 [EST OilPrice]. Closest line MKT-BZ-F-ABOVE-100 is $1.68 away. Boundary #1 (≥$120 ×3 settles) is 22% away.
  - **11/9 reopen:** "DOWN band hit". BZF27 broke under $95, low 92.80 [EST vendor]. "BRENT's 11/8 small-gap-up model was wrong on direction." Window proxies 14:28–14:30 ET: BZF27 92.5074, BZH27 88.7035, M1−M3 +3.8039 ("first valid BRT-33 session, not under; valid 1 of 2; F-a not crossed, $0.30 above"), CLZ26 86.8774, January 3:2:1 $38.05, boundary #8 count 0, WTI−Brent −$6.80. MKT-CL-F-ABOVE-100 UN-FIRED from the 11/2 settle $96.46. Riyadh office damage was worse than "minor" but out of class; D 85 not fired. "11/9 settles not read at 14:49."
  - **COT #13:** NOT-SPENT, 7th, 125,654 / 6.5831%, as-of 11/3 [CONF raw CFTC].
  - **Fires:** none. Every row says "No line fired, no probability moved."
- **CROSS-DOMAIN / CALIBRATION:** The crowd prices "about 76 for another US land strike within 14 days while its oil legs stay flat (ORACLE)". FALCON holds D 85. Gulf volume and perimeter are unresolved, and the Kpler 24.6 relay is not adopted. Uncertain about incremental delivered diesel, strike offsets, source freshness and access (CME IP-blocked), and LIQUID energy-credit amplification ("No new independent energy HY measurement").
- **FORWARD:**
  - November STEO Tue 11/10, set against the bank surplus call.
  - WPSR Thu 11/12: BRT-31 week five and the first BRT-34 print.
  - Combination themes review 11/12.
  - COT #14 Fri 11/13.
  - BRT-33 window every session through 11/27 (valid 1 of 2, needs 8).
  - BRT-35 first GASREGW print 11/9. No figure is given.
  - OPEC+ January decision 11/29.
- **NEXUS-NAMED:** "**Disposition stated November 5 for NEXUS C35: UNRESOLVED.** No later grade or permanent disposition exists at BRENT; date UNKNOWN" … "C35 stays UNGRADEABLE on this input. Low AIS counts are not normalization. Frozen branches only on target match."

## VULCAN

- **HEADER:** As of 2026-11-10T10:12:57-05:00. STATUS commit 14b33c9675. "Closeout 11/10 … 11/10 TSMC and CoreWeave not yet graded, desktop pickup. No letter fired."
- **VIEW:** Composite **15/25** unchanged (S1 3 / S2 2 / S3 3 / S4 3 / S5 4). Financing (S5) is the only fired channel. The market is "repricing who gets paid and at what cost of money". Big buyers fell 1.5–4% and suppliers and developers fell 9–22%, "but no buyer has cut and the desk's letters did not fire". Nvidia's 11/9 fall is "a single-name governance story".
- **MOVED SINCE 11/4:**
  - **11/5 close** (vendor last 16:47 ET): SPY −4.41%, QQQ −6.49%, RSP −2.89%, SMH −11.21%. Payers AAPL −1.53% to META −3.96%, ORCL −6.93%. Suppliers and developers −9.3% to −22.3%. "S1 cannot see a supplier-led break." Cause not established. "about 60% of SMH's fall from its 10/5 peak predates the vote" `[?` "the vote" is not defined in the brief`]`.
  - **Slot 9 (holdings 11/5):** Mag-7 33.4972%, breadth +4.08pp, YELLOW. Memory core 1mo −43.61%. Lambda and Crusoe announced H100 list-price rises.
  - **11/6 close** (vendor bars): SPY +0.31%, RSP −0.38%, QQQ +1.40%, SMH +3.62%, MU +5.12%, MSFT −0.99%, ORCL 116.10 +0.82%, CRWV +6.28%, IREN +20.02%. Against the 11/4 close: SMH −7.99%, MU −13.23%, IREN −0.32%, CRWV −4.17%. Breadth +3.27pp [11/6].
  - **11/9 intraday 11:16 ET** (not closes): NVDA −6.02%, QQQ +3.07%, SMH +4.32%, AMD +12.14%, AVGO +9.00%. Nvidia opened its own investigation 11/8. No key-person row. No 8-K.
  - **Spreads:** Oracle +145 to +175bp vs February; Meta +57 to +88bp vs April. Both cleared inside talk, so the "S5 flex letter is NOT met". The week's supply was about $60B plus EUR 15B.
  - **Closing papers:** Meta $15.0B closed 11/5, €9.0B settles about 11/12. Alphabet €6.0B closed 11/5. Meta over-allotment about $1.869B. Meta long-term debt $80.9B [9/30] to about $106B ("my sum, not filed").
  - **Backlog and capex:** three-name backlog additions $188.3B to $73.2B. Four-name September capex $207.3B. "No YoY cut anywhere."
  - **Oracle prepayment path:** Oracle prepayments $11.4B, 49% of Q1 operating cash flow, payer unnamed. OpenAI's share of Oracle backlog 45–54% is relay-grade.
  - **China clocks:** all 11/10 US–China clocks re-suspended on paper (BIS 91 FR 70789 published 11/9; MOFCOM-GAC 公告2026年第58号; USTR to 1/9).
  - **Ruling:** WQ-608 RULED A. VULCAN-188..191 registered.
  - **Other:** CME GPU futures review runs to 2027-01-08. Card 002 claims were not promoted.
- **CROSS-DOMAIN / CALIBRATION:** 21 registered, 12 resolved, nine OPEN, none due. Base rates are not computable for VULCAN-189 and only partly counted for -190 and -191. To WATT: the Texas moratorium "is a promise, nothing enacted"; TrendForce Lighthouse 2027 650 to 310 MW "is a forecast"; S3 NOT FIRED. To ZHAO: Marvell and Lumentum are signed, not closed. Oracle, Microsoft and SoftBank "are not one loop on what is read" (Microsoft wind-down: "one Bloomberg chain, size and scope unknown").
- **FORWARD:**
  - **11/10:** CoreWeave Q3 (call 5 PM ET) and TSMC October 6-K. VULCAN-191 and -188 grade by 11/16. TSMC is TRUE at NT$570,630mn or more. CoreWeave is TRUE if the FY2026 capex midpoint falls below $36.5B.
  - **11/12:** Nebius Q3.
  - **11/13:** slot 10.
  - **11/15:** VULCAN-13/-15 and the EXIT_PROTOCOL backstop.
  - **11/16:** FERC EL26-67 responses.
  - **11/17:** NVIDIA Q3 FY27.
  - **~11/19:** NVDA 10-Q, which carries the L322 T-tests.
  - **11/20:** NEXTDC AGM.
  - **12/7:** Jupiter hearing.
  - **12/10:** ERCOT Batch Zero.
  - **~12/15:** ORCL 10-Q, "the decisive test of the prepayment path".
  - **12/16:** Micron (inferred).
  - **2027-01-10:** BIS and MOFCOM stays end.
- **NEXUS-NAMED:** none.

## ZHAO

- **HEADER:** As of "2026-11-09 19:38 ET (by `date`) — closeout for the laptop switch, no content change since 15:23". STATUS commit: "NONE (folded in the same commit as STATUS)".
- **VIEW:** 🟠 **29/60 ELEVATED** (11/06 close, +1 on Vector 5). Every 11/10 clock was re-suspended on paper on 11/9. China is "weak at home, booming abroad". The PBOC is holding the yuan back and accumulating dollars. The P3 verdict stands: "the absence of a forcing function IS the finding".
- **MOVED SINCE 11/4:**
  - **11/06:** V5 4→5. October NBS: mfg 49.3, composite 49.7, imports 47.0, construction new orders 40.0 (headline construction held at 48.0). BIS stayed the Affiliates Rule until 2027-01-10 (public inspection 11/05, publishes 11/09). NPCSC closed with no fiscal figure.
  - **Correction:** "11/02's 'newest is 第52号' read a MOFCOM page frozen at 10/26."
  - **11/06 grades:** ZHA-21 NO at 12%, Brier 0.0144. ZHA-24 closed VOID 11/06, replaced by ZHA-26 (PBOC overnight cut from 1.25% by 12/31, **12%**). ZHA-22..25 registered at 60 / 68 / 12 / 18%. ZHA-20 re-marked to 85% on 11/06.
  - **11/9 clocks:** MOFCOM+GAC 公告2026年第58号 continues the suspension from 11/11 to 2027-01-10, "scope identical to 公告70" (KB-246). BIS stay in the 11/9 FR to 1/10 (KB-242). USTR ships fees through 1/9 23:59 ET (KB-248). Hanwha countermeasures and China's port fees to ~1/10 (KB-247, 249).
  - **11/9 15:23 refresh:** SAFE October reserves $3,405.2B (+$4.9B, valuation). Gold 78.30 Moz (+0.83 Moz ≈ 25.8 t, "largest 2026 add"). "11/09 live FX/HK values" were refreshed, but **no value is stated in the brief**. No score moved.
  - **Rates and fixing:** PBOC main rate overnight at 1.25% since 11/02. CGB 10Y 1.59% (11/06). Fix +0.68% weaker than market (20-fix mean, 11/06). China–US 10Y gap ~327bp.
- **CROSS-DOMAIN / CALIBRATION:** Uncertain about:
  1. whether the 1/9–1/11/2027 cluster gets a third extension or a deal;
  2. the cause of the August residuals;
  3. whether HK carry pressure forces the HKMA in;
  4. leg F's hit rate in a regime change.

  The RED BENIGN-DRIFT counter-frame is "Strengthened again". On the WALTER/WATT side, "WATT T1 re-dates to 1/10, does not open 11/11". The question to VULCAN about 0.1% materials-content resolution is still open. The question to LIQUID is re-pointed: is the absorbing bid now OFFICIAL? An unpriced binary: a BIS Entity-List package naming CXMT/YMTC/SMIC subsidiaries (re-check scheduled 11/9; no result stated). The copper −41% decomposition is still un-run.
- **FORWARD:**
  - **11/10 and 11/11:** ZHA-19 (65%) and ZHA-20 (85%) lookups. "YES branches appear satisfied."
  - **11/10:** GACC October trade (exports consensus +33.5%), CPI/PPI, credit.
  - **Wed 11/18:** **September TIC** ("China Q3 net ≤ −$50B ⇒ LIQUID+PROME"). The August residuals may be revised.
  - **11/27:** MOFCOM 公告2024年第46号 clause 2 ends (content UNVERIFIED).
  - **11/30:** November PMI (ZHA-23).
- **NEXUS-NAMED (verbatim):**
  - "**★ 11/06 — FOR NEXUS: the two-clock story is now one clock, and the domestic read weakened.**"
  - "**★ 10/29 — FOR NEXUS: the PBOC's currency posture has fully reversed, and the desk's gauges could not see it until today.**"
  - "**🟠 10/9 — FOR NEXUS: a pre-registered tripwire fired and I applied it AGAINST my own read.**"

## CORAL

- **HEADER:** As of "2026-11-09 13:0x ET (Mon, coral-ae, Will's direct ask: flooding + Amendment 3) | STATUS commit: pending this closeout (prior `2a6252b7d8`)". The pin check shows the brief and STATUS were committed together.
- **VIEW:** 🟠 The split holds: "household/condo stress confirmed; bank-loss transmission NOT confirmed". The bank rail is NOT met and NOT armed. The supply-side MSI leg has been 🟠 since 9/13. "the stress is localized, not statewide".
- **MOVED SINCE 11/4:**
  - **Amendment 3:** passed, unofficial Yes 61.98%, certified 11/17. Local revenue −$4.95B FY27-28, −$8.78B FY28-29, −$11.86B recurring. Amendment 1 failed at 40.9%. On 11/09, an S&P survey of 90 issuers found an average revenue loss of −14% by end-2028 (range −2.3% to −48%). There is no rating action, and the first bills land Nov 2027.
  - **⛔ DR-4955 correction:** household aid is flagged in all 8 requested counties (OpenFEMA 11/06). "IA 0/8" is withdrawn.
  - **Seven FL 10-Qs:** zero association-loan disclosure. BKU CRE 60-89 $21.3M vs $0. **BKU MIXED, aggregate NO TRANSMISSION, FINAL (REGINALD 11/06).** Avidia association loans $491.9M, quality not split.
  - **MSI #12** (11/05): 4-of-5, Cape Coral 5.85.
  - **MSI #13** (data 11/08): Tampa 7.23, Punta Gorda 6.19, North Port 6.22, Cape Coral **5.84** (series low), Lakeland 6.30. 4-of-5, re-fire fails.
  - **Floods 11/01–03:** Brevard / Indian River / St. Lucie. Malabar 24 in/24 h, 2 deaths, ~2,000 registrations. AccuWeather "$3–5B total economic, not insured". No federal declaration or state request (OpenFEMA 11/09). St. Johns at Cocoa 16.98 ft vs 17.0 major. EO 26-228 covers 14 counties.
  - **OIR Isaias claims:** 68,071 / $735.5M at 11/06. Citizens 216,432 at 10/30.
- **CROSS-DOMAIN / CALIBRATION:**
  - Conviction: mechanism-HIGH, bank-transmission-LOW, timing-MEDIUM.
  - Muni effect of Amendment 3 is "UNREAD" (REGINALD).
  - The flood channel is NFIP or uninsured (AEOLUS, CARL).
  - To CARL: FL bankruptcy 225.9/100k, +21.3% YoY to 9/30, 1.256× US.
- **⚠️ Internal stale items:** NEXT DECISION POINT still says "criterion 6 resolves 11/4" and "When: late Oct → 11/15". The 11/09 table says "Criterion 6 graded 11/15, not early".
- **FORWARD:**
  - **11/15:** falsify grade.
  - **11/16:** FL Realtors October (GSE financed units).
  - **11/17:** Amendment 3 certified.
  - **By 11/19:** MSI #14.
  - **~mid-Nov:** Avidia 10-Q and Citizens 10/31 month-end.
  - **11/20:** proposed L784 re-date.
  - **12/11:** NFIP authorization.
- **NEXUS-NAMED (verbatim):**
  - "| NEXUS | Geography read: statewide firming vs SW/Central-FL MSI still above 6.00 in four of five metros, edging down — the stress is localized, not statewide | 🟠 | Synthesis should not treat FL as uniformly improving or uniformly breaking |"
  - 10/29 row: "NEXUS — check your own demand premise" (about MARCO's MIA Sep −1.82% YoY, mechanism CONFOUNDED).

## OSPREY

- **HEADER:** As of "2026-11-09 (Mon) 12:11 ET (from `date`; osprey-1109, closeout on PROME WQ-249 ask) | STATUS commit: e4bc891bb9".
- **VIEW:** Scores are **5 / 5 / 3** unchanged, in an elevated active Russia/Ukraine energy campaign. Refinery strikes resumed after the 10/16–10/29 lull. The "~30% band still stale, not moved". The figures are capacity, not barrels.
- **MOVED SINCE 11/4:**
  - **Strikes:** YANOS 11/3 (Bloomberg 11/6: "all crude processing halted, one person familiar, ~300 kb/d design"), Ryazan 11/5, Afipsky 11/6. "Six plants since 10/30, at least 1.3 M bpd of capacity plus one Ufa plant (Bloomberg)."
  - **Band:** late October runs about 5 M bpd, October about 4.3 (Kpler 10/28). On the same proxy that is 19–22% / 6–9% against the ~30% band. Not moved; re-derivation owed (OWED-52).
  - **Exports:** Bloomberg 4-wk 3.65 to 11/1, weekly 3.97, relay B3.
  - **C3 limb-2 letter** adopted 11/6 (WQ-637 A). Earliest first kill 11/27; HAWK grades.
  - **11/6 statements:** Zelensky said the operation "continues" and that Russia "has rejected the de-escalation measures".
  - **11/9:** Kirishi KINEF struck and is the newest C1 anchor. "C1 leg A restarts 0/14, earliest 11/23 (PROME re-dated DOCKET L914 to 11/23)." Saratov 11/7 is C3-only.
  - **Combination watch** (logged, not scored): Rosneft gasoline limits in six regions; "two of three US-bound diesel cargoes diverted"; Ust-Luga turret tender; Baltic convoy escort.
  - **Clocks 11/9:** C1 0/30 · C2 22/30 (earliest 11/17) · C3 34/21, limb-2 window 3/21.
  - **New book:** OSP-08…11 OPEN, registered 11/6.
- **CROSS-DOMAIN / CALIBRATION:** "products impairment direction high; incremental lost-volume level low". The brief asks BRENT for the cause of the Primorsk ~3-day pause. The C1 5→4 test is UNREACHABLE without an independent capacity-offline aggregate (none since 9/8). Maritime coverage is news-only; Palaemon 2–9 Nov is unpublished. Russian diesel exports to the US are "a demand-side sign of product recovery".
- **⚠️ Internal stale items:** NEXT DECISION POINT says "**11/20** C1 leg A, OSP-08 grade", but the 11/9 block re-dates C1 leg A to the earliest 11/23. The VIEW section is labelled 2026-10-29.
- **FORWARD:**
  - **11/10–11:** Abu Dhabi talks ("whether the brake on refinery strikes returns"). The energy/maritime ceasefire item rests on an unread outlet.
  - **~11/14:** Kirishi +5d re-read.
  - **11/17:** earliest C2 re-kill (Bloomberg ≥3.9 twice ⇒ C2 5→4; <3.5 blocks the kill).
  - **11/18:** OSP-07 grade (60%) and GATE-OSPREY-001 review.
  - **11/23:** C1 leg A.
  - **11/24–27:** C3 canvass.
  - **11/27:** earliest C3 kill.
  - **By 12/6:** §5 re-read.
- **NEXUS-NAMED:** none addressed to NEXUS.

## FALCON

- **HEADER:** As of "2026-11-09 10:55 ET | STATUS commit: `9c7c5f946e` | Evidence cutoff about 15:50Z 11/09". Unreachable: centcom.mil, UKMTO, Dawn (403). CENTCOM X and the direct Reuters/AP/AFP/Bloomberg feeds were not read.
- **VIEW:** 🔴 **B 1 / C 14 / D 85 HELD** (11/04 weekly review; no letter met through ~15:50Z 11/09). "The live variable is the Qatar track". Only "A signed, dated text confirmed by both sides" moves the letters. The production rung waits on an Abqaiq-class hit. "held means no letter fired, not that D 85 was re-earned."
- **MOVED SINCE 11/4:**
  - **Grades:** FAL-06 CONFIRMED at 70% (no route fired to 23:59 ET 11/5; route (c) never graded). FAL-08..12 OPEN to 12/31: FAL-08 75%, FAL-09 40%, FAL-10 12%, FAL-11 20%, FAL-12 10%. FAL-09 count 0 of 5 (window opened 11/7 00:00 ET).
  - **Hull events:** VELOS SAPPHIRE, 11/4 23:20Z (one seafarer killed). UKMTO 197-26, 11/5 22:00Z. UKMTO 199-26, tanker on fire 8 nm NW of Khasab 19:20Z 11/7. UAE rescued 22 from a burning cargo ship 11/8. Losses 7 ("census 7").
  - **US actions:** HUDA disabled by US aircraft 11/7 (blockade enforcement, excluded from FAL-09). Task Force Iron Gate 11/7: "Not a strike, a campaign or a new order".
  - **Qeshm:** 11/6 "US strike, attribution high, not explicit" (Trump: "We do minor strikes…"). Qeshm/Bandar Abbas blasts 11/8: "NOT ESTABLISHED as US".
  - **Riyadh Aramco office tower 11/8:** "STRUCK, minor damage". "D 85 to 92 NOT FIRED: an office is not production-class." Eastern Province missile intercepted.
  - **IRGC 11/8 claim:** three tankers ablaze, CLAIM-ONLY. Own FIRMS at-sea heat at 26.10N 55.90E, 08:41–10:21Z 11/8. IMO 131 / 25 as at 9 Nov.
  - **Diplomacy:** the Qatar PM met Trump 11/9 on unconfirmed terms ($8B released, blockade lifted, Hormuz reopens on day two, all from unnamed sources). "Ladder item 5 and FAL-10 NOT MET". Rubio 11/8: demands "outrageous and ridiculous".
  - **Iraq:** the US Treasury asked Iraq to shut all but two Iran crossings (Reuters 11/7); four of five are still open.
  - **Transits:** UKMTO weekly via MEE, seven days to 11/4: 11 attacks, three sank. "Hormuz 325 transits vs 277, about 65% below pre-conflict, AIS-seen 71. JMIC 111: about 31 US-assisted a day".
  - **Saudi October flows:** Vortexa 6.5, TankerTrackers 6.99, Kpler 5.4 mb/d. No November print.
  - **GATE-FALCON-001:** LIVE, leg 2 NOT MET (lowest 82.9% vs ≤65%, latest 89 vs 68). Next review 11/11.
- **CROSS-DOMAIN / CALIBRATION:**
  - 3C / 3F / 1P / 0V / 5 OPEN. "Convergence 43/50, saturated composite."
  - "Flow reading is BRENT's." "BRENT owns the price read."
  - "Polymarket legs resolved NO is ORACLE's and not an event grade."
  - "⛔ 46 a day is not comparable with 88 a day or PortWatch 2 to 6".
  - "Tankers delay reporting, so silence is not refutation."
- **FORWARD:**
  - **11/11:** weekly scenario, GATE-FALCON-001 review and combination themes review.
  - **12/31:** FAL-08..12 resolve.
  - Open waits: the Qatar meeting outcome (after cutoff); the third sinking's name; RITI status; Sinokor detentions.
- **NEXUS-NAMED:** none.

## ORACLE

- **HEADER:** As of "2026-11-08T16:58Z pull (Sun, WQ-646 A read 2, context only) for the Iran and oil lines; every other line is the 2026-11-06T22:15Z log". Re-stamped 2026-11-09 10:5x ET: "tooling-only session, NO pull, every figure below unchanged. The Mon 11/09 gate read is the routine's 10:15 ET pull (166f9c649e), logged and not yet graded." ⚠️ The brief carries no 11/09 or 11/10 figures. Git shows an ORACLE routine commit "daily pulls 2026-11-10", which is not reflected in the brief (not read).
- **VIEW:** 🔴 "THE CROWD PRICES ANOTHER US STRIKE ON IRAN AS LIKELY, NOT A SUPPLY SHOCK (11/08 16:58Z)." VX-ORC-07 state unchanged (Critical under WQ-439 A).
- **MOVED SINCE 11/4:** all figures; see answer (e). Resolution 11/07: the effective-ceasefire legs resolved NO. New 2-week-pause market created 11/08. December hike, oil gate, AI/recession, jobs, bank-failure and venue-risk lines are all from the 11/06–11/08 vintage.
- **CROSS-DOMAIN / CALIBRATION:** tensions as written.
  1. 🟠 Against LIQUID/HENRY/BOND: Fed repricing, cause open ("Odds fell 14 to 17 points on 11/05 with stocks and rebounded 14 on 11/06, part before the print").
  2. 🔴 Against BRENT/HAWK/FALCON: "strike resolved, oil flat".
  3. 🟠 Against BOND/TERRY: 10Y resolution basis (Treasury par vs DGS10, unconfirmed since 9/17).
  4. 🟠 Against RED: recession definitions.
- **FORWARD:**
  - **11/09:** Hormuz weekly rolls.
  - **Wed 11/11:** October CPI market end (PM modal 86.0, $3.3K liquidity ⚠️).
  - **2026-11-17T01:00Z:** Nov $110 active-month switch (INFERRED).
  - **11/30:** Hormuz normal; Kalshi Brent month-end (`>$97.99` 48.0, 11/07).
  - **12/04:** November jobs.
  - **12/09:** FOMC.
  - **12/15:** Kalshi gap-fill re-check.
- **NEXUS-NAMED:** none.

## CYPHER

- **HEADER:** As of "2026-11-08 12:07 EST (Arkéa provider and shared-reach check, pulled forward from 11/09 on PROME prome-bf's spawn; no score, band, gate or state moved) | STATUS commit: `063fde11b035bdc825c30f5ec9760ffa580c1b96`".
- **VIEW:** 🟠 One wave trigger has FIRED (CISA KEV 10/26). Compromises are vendor-verified, no victim named, so the R1 flip is not met. Off the wave the bank-vendor channel is live (Finzly, Abrigo, Arkéa), and Arkéa is "a new class, stolen bank money rather than stolen data".
- **MOVED SINCE 11/4:**
  - **Arkéa (CYB-INC-059, 11/04):** "about EUR 100M provisional", provider unnamed. LIQUID 11/06: no effect on its surfaces. HANS 11/06: a one-bank earnings event. The 11/08 re-check found the provider still unnamed, no second institution and no CERT-FR alert.
  - **Bank-vendor watch:** count limb MET 11/05 (Finzly, Abrigo).
  - **Capcom:** corrected to CONFIRMED 11/06 (11.77M records).
  - **Composite:** 24/40 raw, 15/40 shared-root-adjusted (VX-01 2→3, VX-08 3→4). Rows 1 and 3–9 NOT-FIRED at 11/05.
  - **SonicWall SSLVPN** CVE-2026-19868 in CISA KEV 11/06, no victim named.
  - **Shinkin outage:** 128 Japanese credit co-ops for ~5.5 h, "operators think not cyber, no fire".
- **CROSS-DOMAIN / CALIBRATION:** Uncertain about Arkéa's provider and client base, named PHP2Shell victims, whether Finzly's leaked keys were live, and whether Abrigo lost data. "L on any systemic reading". Consequence judgments belong to REGINALD, LIQUID, GIBBS and HANS.
- **FORWARD:**
  - **11/12 (weekly):** wave clock, Abrigo, ConnectWise.
  - **11/13:** GMO briefing and Kiteworks.
  - **11/15:** TruStage.
  - **11/16:** Arkéa weekly look.
  - **11/18:** Row 9 PANW persistence ("PANW at or below $289.24 AND 10.0 points behind HACK on 2 consecutive closes; HENRY grades").
  - **11/20:** R1 flip test.
- **NEXUS-NAMED (verbatim rows):**
  - "| NEXUS / PROME / SAM | 11/06: Capcom corrected to CONFIRMED (11.77M records, no financial channel; the desk's 10/23 read was wrong). Kiteworks: no named route at +16 days, weak evidence. GMO cost not calculable, next 11/13. Shinkin outage: 128 Japanese credit co-ops about 5.5 hours, operators think not cyber, no fire | P3 | Consequence stays with SAM |"
  - "| NEXUS / PROME | Composite 24/40 raw, 15/40 shared-root-adjusted (VX-01 corrected 2->3 on the letter, VX-08 3->4 on the attribution; neither is new bank damage). Rows 1, 3-9 NOT-FIRED at 11/05 | P3 | Wave state for synthesis. Unit 42 verified Dream's compromises; R1 flip still needs a named organisation |"

## MIDAS

- **HEADER:** The top block is dated "November 8 — WQ-451 L3-SAFE SUPPORTS (current read for peers)". There is no as-of line or pin in the header (the pin check shows OK-SAME-COMMIT f9c4a3028).
- **⚠️ SHAPE / STALE:** 18 KB of dated paragraphs with no VIEW / CALIBRATION / NEXT DECISION / FORWARD sections in schema form. The closing price block ("Gold: GCZ26 … [Oct 26 provisional MIRROR daily]") and "Current reading basis" are **October 26 vintage** and still read as current.
- **VIEW** (inferred from the 11/6 and 11/8 blocks): the official gold bid did not pause. Gold traded as a risk asset ("not a stress hedge" finding stands). Metals composite 13/20 on the ruled floor, "not new evidence".
- **MOVED SINCE 11/4:**
  - **11/6:** WQ-451 L1 NOT TESTED ("needed the S&P back at 7,757.17 and got 7,743.98"). GLD trust ended 1,040.51 t. "10/30 is not a LIQUIDATION day on the frozen letter."
  - **11/05:** "S&P −4.36%, GLD +0.81%, about what a 4 bp real-yield fall implied". L2 count 2 of 10, GLD up on 1.
  - **Composite:** 8 → 13/20, scored from the 11/2 close under WQ-352/368.
  - **TERRY lines:** one-month downside line crossed 10/30 and 11/03; "GLD since back at $375.49" `[?` date not stated, after 11/03`]`.
  - **Copper:** LME copper yellow since 11/02, 318,675 t, +36.5% vs median. HGZ26 −2.47% on 11/05.
  - **WGC:** Q3 central banks 321.2 t, of which 120 t reported.
  - **New forecasts:** MIDAS-18..22.
  - **11/8:** PBoC gold 78.30 Moz October vs 77.47 Moz September, **+25.82 t**, "largest monthly addition of 2026 and the fifth straight month above +10 t". SAFE valuation implies about −6.3% on the price of its gold over October.
  - **COT** as-of 11/03: gold net/OI 44.98%, seventh straight weekly fall. Palladium net short −40.11%. No score change, composite 13/20.
- **CROSS-DOMAIN / CALIBRATION:** "TIC sign (L821, ZHAO/SAM own the level) about 11/18 and WGC October (L822) early December still to grade." On the LME build: "the LME build is still not located". Silver and palladium are "one shared root".
- **FORWARD:** TIC sign ~11/18 (L821). WGC October early December (L822). No other dated forward section.
- **NEXUS-NAMED:** none.

## WATT

- **HEADER:** As of: "verified 5-min tape October 23–November 4 (window n=2,028 of 2,028); unverified 5-min to 18:15 EPT November 5; EIA-930 demand to 22Z November 5; … P3 as read October 20. **STATUS commit c153b55a6.**" ⚠️ This is 5 days old, the oldest brief in this set. "Weekly coverage ≤ November 12."
- **VIEW:** P1/P2/P3/P4 = **3**/5/4/2, **composite 14/20** (was 16/20). "P1 de-escalated 5→3 November 5, D:L866 MET". "Historical auction shortfalls remain real. Prospective shortage magnitude is less certain".
- **MOVED SINCE 11/4:**
  - **P1 5→3 on 11/5.** The 11/1 run, "verified $1,273.52/$2,015.32/$2,015.32 at 92.6–91.1% of trailing peak met price only, no posting, cause unknown".
  - **PJM daily max, Oct 28–Nov 3:** $305.75 / $95.72 / $248.16 / $193.76 / $2,015.32 / $419.33 / $393.84.
  - **2029/30 BRA:** window December 9–15, results December 22, cap $337.83, Reliability Requirement 158,712 MW [KB196].
  - **New forecasts:** WATT-14 (clear at cap) 88%, WATT-15 (shortfall above 6,831 MW) 45%, WATT-16 (RED fires Nov 6–Dec 15) 55%, WATT-17 registered.
  - **PJM outlook:** 182,426 MW vs about 147,500 MW forecast peak.
- **CROSS-DOMAIN / CALIBRATION:**
  - "IMM tracks 4,016.9 MW cancelled OR delayed data-center projects as of September 21; about 42% of 9,481 MW forecast growth", flagged as "Demand-realization counterevidence, not 42% of all load".
  - Unknowns: amended RBP docket and order date; cause of the November 1 run; active queue total; hedge shares; NG=F roll.
- **⚠️ Stale forward row:** "November 10–11 Beijing | Battery T1 boundary". ZHAO (11/9) says "WATT T1 re-dates to 1/10, does not open 11/11".
- **FORWARD:**
  - **11/8:** IRAS compliance.
  - **11/16 and 12/16:** EL26-67 responses and answers.
  - **12/2:** WATT-13.
  - **12/9–15 and 12/22:** BRA window and results.
  - **12/10 and 12/17:** ERCOT Batch Zero and PUCT.
  - **12/18:** WATT-16.
  - **12/24 and 2/22/2027:** EO 14421 clocks.
  - **12/31:** WATT-14/15/17.
- **NEXUS-NAMED (verbatim, rows addressed to NEXUS):**
  - "| HENRY / AEOLUS / PROME / NEXUS | **P1 5→3 November 5 (D:L866 MET):** no real EEA-class posting, no 202(c), no RED re-fire October 28–November 3 on a complete verified tape [KB191/193] | ⚠️ Not an all-clear: November 1 00:25–00:35 verified $1,273.52/$2,015.32/$2,015.32 at 92.6–91.1% of trailing peak met price only, no posting, cause unknown [KB192]. November 3 EEA-labelled postings are PJM's winter drill |"
  - The October 29 P1 3→5 row (HENRY / AEOLUS / PROME / NEXUS), the "Year over year the tail got worse" row (HENRY / AEOLUS / NEXUS / VULCAN) and the BRA-timing history row (PROME / NEXUS / WALTER) are all pre-11/4.
  - The packets line records "NEXUS a862a30c4" (October 29).

---

## CROSS-BRIEF (≤10 lines)

1. **PBoC gold:** ZHAO (11/9) "78.30 Moz (+0.83 Moz ≈ 25.8 t, largest 2026 add)" and MIDAS (11/8) "78.30 Moz October vs 77.47 Moz September, +25.82 t" agree. ZHAO's SENDING row to MIDAS still carries the older September "+0.74 Moz ≈ 23 t".
2. **11/10 China clocks:** ZHAO (11/9) and VULCAN (11/10) agree that all are re-suspended to ~2027-01-10 (BIS FR 11/9; 公告2026年第58号; USTR 1/9 23:59 ET). WATT's 11/5 brief still lists a "November 10–11 Beijing" battery T1 boundary, superseded per ZHAO.
3. **Brent/WTI:** BRENT gives BZF27 $98.32 and CLZ26 $90.83 [11/6 wire EST] and a 11/9 window proxy of 92.5074 / 86.8774. ORACLE gives Kalshi Brent 47.0 / 52.0 and WTI $110 Nov 17.0 [11/08 16:58Z]. FALCON cites "Brent −8.7% 11/4 (BRENT's number)". No conflict, but ORACLE's oil legs predate BRENT's 11/9 "DOWN band hit".
4. **Qeshm 11/6:** FALCON calls it "US strike, attribution high, not explicit". BRENT's 11/6-close row says "not established as a US strike (card 047)". ORACLE says the resolution path ran through Trump's "minor strikes". These are different vintages and wordings, and NEXUS should cite FALCON.
5. **Riyadh Aramco office 11/8:** FALCON, BRENT (11/8, 11/9) and ORACLE (via BRENT) all have it below the production rung, with D 85 not fired.
6. **Gulf flow:** FALCON has UKMTO 325 transits/wk, ~65% below pre-conflict, and Saudi October at Vortexa 6.5 / TankerTrackers 6.99 / Kpler 5.4 mb/d. BRENT has Kpler Hormuz crude 7.3 vs 13.5 baseline (week to 10/28) and Yanbu "about 2.5 mb/d exposed". Different perimeters; both desks say so.
7. **11/5 equity drop:** VULCAN has SPY −4.41% (vendor last, 16:47 ET). MIDAS has "S&P −4.36%". ORACLE has Fed odds "fell 14 to 17 points on 11/05 with stocks". This is a small index-vs-ETF basis gap. **All three say the cause is not established, and none ties it to the others.** That is a hinted shared-root thread: one cross-asset day (stocks down, hike odds down, GLD +0.81%, real yield ~−4 bp), unnamed.
8. **Hinted, unnamed:** OSPREY logs "two of three US-bound diesel cargoes diverted" (11/9, not scored). BRENT's live distillate rail sits at 99.259M, 23.8 days of cover, with BRT-34 <95M at 45%. BRENT's diesel read does not cite the diversion, and OSPREY routes it to no one.
9. **Hinted, unnamed:** VULCAN shows Oracle +145–175bp and suppliers −9% to −22% on 11/5. ORACLE has PM "AI bubble burst" at 7.5 and "S&P best asset 87.0" (11/06 log). Neither brief juxtaposes crowd calm against AI financing-cost repricing.
10. **Russian diesel ban to 2027-01-31:** BRENT and OSPREY agree.

## ANSWERS

**(a) AI funding / capex after 11/4.**
- **CoreWeave Q3 11/10:** not in the briefs as a result. VULCAN (11/10): "not yet graded". VULCAN-191 is TRUE if the "FY2026 capex midpoint falls below $36.5B". CRWV +6.28% on 11/6 and −4.17% vs the 11/4 close (vendor bars).
- **SoftBank results 11/10:** not in the briefs. VULCAN only says Oracle and SoftBank "share OpenAI; no credit tie found".
- **Oracle CDS:** not in the briefs. VULCAN has Oracle bond own-comparable spreads "+145 to +175bp vs February", filing-primary, cleared inside talk, so "S5 flex letter is NOT met". ORCL −6.93% on 11/5 and 116.10 +0.82% on 11/6. Oracle prepayments $11.4B = 49% of Q1 OCF, payer unnamed. The decisive test is the ORCL 10-Q ~12/15.
- **Microsoft/OpenAI:** VULCAN: "Microsoft's wind-down sits beside it, one Bloomberg chain, size and scope unknown". "OpenAI's share of Oracle backlog 45-54% is relay-grade; filings name neither."
- **Data-center cancellations in MW:**
  - WATT: "IMM tracks 4,016.9 MW cancelled OR delayed data-center projects as of September 21; about 42% of 9,481 MW forecast growth" (pre-11/4 vintage, carried in the 11/5 brief).
  - VULCAN: "TrendForce Lighthouse 2027 650 to 310 MW is a forecast". The Texas moratorium is "a promise, nothing enacted". S3 NOT FIRED.
- **Financing refused / capex cut:** none in the briefs.
  - VULCAN: "No YoY cut anywhere" (four-name September capex $207.3B, mixed definitions).
  - VULCAN: "no buyer has cut".
  - Meta $15.0B and Alphabet €6.0B closed 11/5. Week supply ~$60B + EUR 15B, AI share not identified.
- **Other:** Nvidia 11/9 −6.02% intraday is a governance story, with "no capex guide changed". ORACLE: PM AI bubble burst "8.25 → 15.9 → 7.5 (liq $129.6K)" [11/06 log].

**(b) Energy.**
- **Lost barrels measured:** none.
  - BRENT: "Tanker card 018: no lost barrel established, flow NOT MEASURABLE, BG-02 NOT MET"; "No verified Saudi loss"; "Yanbu no November print".
  - FALCON: "No stated crude loss, FAL-08 untouched".
  - OSPREY: Russian refinery figures are "CAPACITY, not barrels" (six plants since 10/30, "at least 1.3 M bpd of capacity", Bloomberg; Kirishi 11/9). The ~30% band is stale.
- **Hormuz transits:**
  - FALCON (relay via MEE, UKMTO 403), seven days to 11/4: "Hormuz 325 transits vs 277, about 65% below pre-conflict, AIS-seen 71. JMIC 111: about 31 US-assisted a day".
  - BRENT: "Kpler Hormuz crude 7.3 mb/d week to 10/28, relayed, against 13.5 baseline"; flow UNRESOLVED.
- **Cracks (BRENT):**
  - December crack $91.12 [11/6 window, EST vendor]; "about $91".
  - January 3:2:1 $37.15 (11/5), $37.19 (11/6 window), $37.18 (11/6 close), $38.05 (11/9 window). Boundary #8 count 0.
  - 11/2 crack fallback $89.2472 (TERRY's exit stands; "a CME settle at or above $90.16 would reverse it").
- **Owner fires:** none.
  - BRENT: every row says "No line fired". The 11/9 "DOWN band hit" is a band, not a line, and the 11/8 model "was wrong on direction". MKT-CL-F-ABOVE-100 UN-FIRED.
  - FALCON: D 85 NOT FIRED on Riyadh. FAL-06 CONFIRMED (through 11/5). GATE-FALCON-001 leg 2 NOT MET.
  - OSPREY: no mark moved; C1 leg A reset to 0 by Kirishi.

**(c) China export-control clocks due 11/10, USD/HKD and TIC.**
- **Clocks:** all re-suspended on paper 11/9 (ZHAO; VULCAN agrees):
  - MOFCOM+GAC 公告2026年第58号 to 2027-01-10, "scope identical to 公告70";
  - BIS Affiliates stay to 1/10 (91 FR 70789 per VULCAN);
  - USTR ship fees through 1/9 23:59 ET;
  - Hanwha countermeasures and China port fees to ~1/10.
- **ZHAO forecasts:** ZHA-19 65% and ZHA-20 85% "both look like hits, graded 11/10 and 11/11 as lookups". ⚠️ "2026年第58号 ≠ 2025年第58号".
- **USD/HKD:** no post-11/4 value is stated. The latest stated reading is 10/29: "USD/HKD 7.846 vs the 7.85 convertibility line; HIBOR-SOFR −122.5bp … Aggregate Balance HK$53,999M". The brief says "11/09 live FX/HK values" were refreshed but gives no figure.
- **TIC:** no new reading. September TIC is due Wed 11/18. Carried figures: 6-month China net −$71.5B, China $590.7B, Q3 China+Korea −$21.6B through August. Also SAFE October reserves $3,405.2B (+$4.9B, valuation) [11/9].

**(d) Equity volatility / credit after 11/6.**
- **VIX / gamma:** not in the briefs after 11/6. The only VIX figure is MIDAS "VIX +2.22" on 10/30.
- **HY/IG index spreads:** not in the briefs. BRENT says "No new independent energy HY measurement" from LIQUID.
- **Nearest items:**
  - VULCAN Oracle +145–175bp / Meta +57–88bp own-comparable new-issue spreads (date in the 11/5 week `[?]`).
  - VULCAN 11/6 closes: SPY +0.31%, QQQ +1.40%, SMH +3.62%.
  - VULCAN 11/9 intraday: QQQ +3.07%, SMH +4.32%, NVDA −6.02%.
  - ORACLE "S&P best asset 87.0" and PM recession 4.5 (11/06 log).

**(e) ORACLE prediction-market reads (quoted exactly):**
- **Freshness:** figures are from the 2026-11-08T16:58Z pull (Iran/oil) and the 2026-11-06T22:15Z log (others). There is no pull since; the 11/09 gate read is "logged and not yet graded".
- **New 2-week-pause market** (created 02:48Z 11/08): "by 11/8 23.5 (book 24/25), i.e. about 76 that a qualifying US strike lands on Iran's land within 14 days; 11/15 36.0 · 11/22 48.5 · 11/30 62.5 · 12/31 80.0." ⚠️ "A market about 14 hours old at the read, with $400 to $5K within 2¢ of the bid. Its rule differs from the old event, so never difference the two."
- **Oil and conflict legs (11/08):** "WTI $110 Nov 17.0 (17.0 at read 1), invade 10.5 (10.5), war 2.0, Hormuz normal 12/31 8.5, Kalshi Brent 47.0 / 52.0 on thin books."
- **11/07 resolution:** "Through 11/08 · 11/15 · 11/30 · 12/31 all NO … volume $1.33M · $941.3K · $303.8K · $263.2K. Through 11/05 and 11/06 open at 99.2/99.4 and 97.6/98.0." At 13:43Z 11/07: "WTI $110 Nov 17.0 (19.5), invade 10.5, war 2.2, Hormuz normal 12/31 9.5; thin Kalshi Brent rungs rose 44.0 → 48.0 and 47.0 → 56.0."
- **December hike:** "PM 76.5 (22:15Z, liq $359.7K) · Kalshi 78.0 (OI 92.4K) · futures about 76–80 (Yahoo last, EFFR 3.88 [11/05]). 11/06 read 77.5."
- **Oil gate:** "VX-ORC-04 no active Alert. Reads 52.5 · 52.5 · 64.0 · 36.5 · 30.5 · 25.5 · 16.0 · 19.0 … Spread +71.5 read, +71.0 context."
- **AI / recession:** "PM AI bubble burst 8.25 → 15.9 → 7.5 (liq $129.6K). PM recession 4.5; Kalshi GDP-rule 4.0 (1¢ book). S&P best asset 87.0."
- **Jobs:** "October U3 printed 4.1; Kalshi crowd mode was 4.2. November rungs first logged: `>4.1` 48.0 (⚠mid 47.0) · `>4.2` 13.0 (⚠mid 6.5)."
- **Bank failure:** "any-bank by 12/31 **70.5** on a **$2.2K-liq** book: not a crowd view, not routed."
- **Forward table:** "October CPI market end | PM modal at 86.0 ($3.3K liq ⚠️)"; "Hormuz normal · Kalshi Brent month-end | PM 3.2 · `>$97.99` 48.0 (11/07)".
- ⚠️ ORACLE's own brief gives Hormuz normal 12/31 as 8.5 (11/08) and 9.5 (11/07). The forward row's "PM 3.2" is labelled for 11/30, a different leg `[?]`.
