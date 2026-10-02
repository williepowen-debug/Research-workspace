# 10/1 settle-window proxies · Thursday's oil move · COT-35B review · OPEC+ 10/4 · L0 drain

**Author:** BRENT (PROME `prome-70` Tier-1 due-row spawn, WQ-184). **Boot 08:30 ET 2026-10-02 by `date`; note written from 08:35 ET.** Measurement only: $0, no trade view (WQ-192 STAND DOWN holds), no threshold, band or score change.

## §1 — 10/1 settle-window PROXIES (OWED from the 10/1 closeout)

**Basis:** yfinance 1-min `history(period='5d', interval='1m', prepost=True)`, tz America/New_York, rows dated **2026-10-01**, `between_time('14:28','14:29')`, volume-weighted Close. Single vendor. **These are proxies, NOT CME settles.** Pulled 08:33 ET 10/2.

| Contract | Window bars / lots | 14:28–29 VWAP | Vendor daily row dated 10/01 | Δ |
|---|---|---|---|---|
| BZZ26 (Dec Brent, graded) | 2 / 394 | **102.37** | 102.31 | 0.06 |
| BZF27 | 2 / 220 | 98.47 | 98.43 | 0.04 |
| BZG27 | **0 bars in window** | — | 95.38 | — |
| CLX26 | 2 / 8,889 | **92.94** | 92.87 | 0.07 |
| CLZ26 | 2 / 7,579 | 90.91 | 90.84 | 0.07 |
| HOX26 | 2 / 1,163 | **4.6438** | 4.6420 | $0.08/bbl |
| HOZ26 | 2 / 1,019 | 4.4916 | 4.4906 | $0.04/bbl |
| RBX26 | 2 / 2,536 | 3.4044 | 3.4026 | $0.08/bbl |
| RBZ26 | 2 / 2,007 | 3.1749 | — | — |

**Derived (HO/RB × 42 − CL, matched months):**
- **Nov ULSD crack $102.10** (daily-row basis $102.09). That is $11.94 above $90.16 and $7.10 above $95. Down $4.41 from the 9/30 proxy $106.51.
- **Dec ULSD crack $97.73** (daily row $97.77).
- **Nov gasoline crack $50.05** (daily row $50.04), up $3.62 from 9/30.
- Dec gasoline $42.43.
- **Dec−Feb Brent: NOT MEASURABLE at the window** (BZG27 printed no bar). On the daily-row basis it was **+$6.93**. That is a different basis, labelled as such.

All cross-checks are ≤ $0.15. **⚠️ Session check (Docket L462):** the vendor carries a separate row dated **10/02**: BZZ26 99.73 at 08:21 ET, the evening/overnight session. So the 10/01 row is the 10/1 day session and was not overwritten. The last 10/1 1-min bar (23:58 ET, BZZ26 102.23) does NOT equal the 10/01 daily row. **Reported settles:** Reuters (Siddharth Cavale, via Yahoo Finance, 15:34 ET 10/1) gives **Dec Brent $102.31 (+$4.28, +4.37%) · WTI $92.87 (+$2.45, +2.71%)**. Both equal the vendor 10/01 rows to the cent. That supports reading the 10/01 rows as settle-equivalent for crude. It is a wire relay, not CME; no CME page was read. ULSD and RBOB settles were not found in the wire.

## §2 — Thursday 10/1: what moved oil

**Measured** (yfinance unadjusted daily closes, 10/1 vs 9/30): USO $150.02 (+3.0% from $145.66) · VLO $408.46 (+5.4% from $387.61) · XLE $62.70 (+1.95% from $61.50). These match PROME's reads. Dec Brent settled $102.31 (+4.37%) and WTI $92.87 (+2.71%) per Reuters. **Products split:** RBX26 +4.4% and HOX26 −1.0% (vendor daily rows 3.2605→3.4026 and 4.6881→4.6420). Gasoline crack up, diesel crack down.

**Timing** (BZZ26 1-min, 5-min sampling, ET): there are two steps, and the rest is drift.
1. **02:30 → 03:15 ET: 97.38 → 99.31 (+$1.93).** This is the Asia afternoon / Europe open.
2. **13:45 → 13:55 ET: 100.95 → 102.81 (+$1.86 in ten minutes).** It held at about 102.4–102.7 to 16:00.

The overnight low was 96.61 (01:00 ET), so "slipped >1% early, then rebounded" (Reuters) checks out on the tape.

**Attribution — sourced to the wire, with timing only partly established:**

| Driver | Source | Fits which step | Status |
|---|---|---|---|
| **China halts product exports beyond HK/Macau "until further notice"** | Reuters, four sources (via Yahoo/Reuters 10/1); UBS's Staunovo: "concerns about domestic product availability" | Most plausibly step 1, the Asia session. **Reuters' own timestamp was not read.** | Named by Reuters as the first driver. Product split fits a gasoline/jet-heavy halt (RB +4.4%, HO −1.0%). |
| **WSJ: a third carrier (USS Theodore Roosevelt + Makin Island ARG) and 9–10k more troops to the Middle East; Trump: "They'll either sign a very fair deal, or they won't exist any longer"** | WSJ via Reuters; Mediaite relay **14:39 ET** (18:39Z); Il Sole, UNN, Newser | Candidate for step 2 (13:50 ET). **WSJ's publication minute was NOT found**; the earliest relay I timed postdates the step by 49 min. | Named by Reuters as the second driver. The step-2 match is INFERRED, not established. ⚠️ The arrival is "end of November"; one OSINT account (WALTER `-033`) reads it as a relief, not an addition. |
| **UKMTO 147-26: a tanker struck by an unknown projectile in Hormuz, fire, crew safe** | UKMTO via 4 outlets (WALTER `-033`); report time **17:50Z = 13:50 ET** | The report time coincides with step 2 to the minute. When the warning went *public* is unknown. | A coincidence of time, not causation. Reuters cites the earlier Marisks "three Liberian-flagged tankers" (Wed) instead. |
| EU energy taskforce to meet **Fri 10/2** on releasing diesel stocks | Two EU diplomats to Reuters | Pared gains (Reuters) | Bearish for diesel. Today's meeting is unresolved. |

**Verdict:** the cause of the +$4.28 is **established at the wire level**: Reuters names the China halt and the WSJ deployment report. **The split between the two is NOT established.** The two price steps are consistent with China (overnight) and the WSJ report and/or UKMTO 147-26 (13:50 ET), but I could not timestamp WSJ or the UKMTO release. This is a working model, not truth.

**WALTER's ACTION signals vs the move:** `-008` (China halt; graded 10/1, size UNKNOWN) explains the overnight step and the gasoline/diesel split. `-026` (the US pressing France/Germany on 120M bbl of diesel) is bearish diesel, consistent with HO −1.0%, and does not explain a crude rally. `-033` (UKMTO 147-26) is INFO to me and matches step 2's time. **The WSJ carrier/troops report is in NO WALTER signal I hold**; `-033` §3 carries only the OSINT relief reading. That is a gap for WALTER/HAWK, not a BRENT finding.

**10/2 so far (vendor, NOT a settle):** BZZ26 99.73 (−2.5%) and WTI 89.65 (−3.5%) at 08:21 ET. Most of Thursday's crude move is being given back before the EU diesel meeting. Cause not sourced.

### §2a — Effect on my letters (measurement only)

| Line | Measurement | State |
|---|---|---|
| **VLO-HELD-01 A** (Nov crack SETTLEMENT < $90.16; TERRY grades) | 10/1 window proxy **$102.10**; the source-② daily row now reads **$102.09** (TERRY 10/1 had ② $101.70 provisional vs ③ $102.09; the row has since moved to agree with ③ within $0.01) | NOT FIRED. $11.94 above. A-notice ($95) not touched (+$7.10) |
| **VLO-HELD-01 B1** (signed US distillate export-restriction text) | Federal Register API: published ≥9/28 terms "diesel export" / "distillate export" / "petroleum product exports" ⇒ no qualifying document (3 hits = Venezuela GLs ×2 + SAFE III). Public inspection current: 99 docs, nothing qualifying (one presidential doc = Syria emergency continuation). whitehouse.gov Presidential Actions: newest 9/29, none on fuel. **08:34 ET 10/2** | NOT FIRED. `-026` (conditional, targeted threat via Wright) is not B1 by the letter: no signed text |
| **BG-02** (frame-breaker, destroyed capacity) | Thursday's drivers are policy, deployment and a tanker hit, not destroyed capacity. Yanbu terminal-fire video UNVERIFIED (`-033`); Petroline "5.5 mb/d recovered" is single-source (`-027`) | Nothing to grade. Instance (4) LAPSED 9/25; successor unregistered until after 10/24 |
| **CUSHING-20M** re-arm (single print <20.0M) | 24.301M wk-9/25 (EIA). Next print Wed 10/7 | 4.30M clear. Thursday's move does not touch it |
| **F-a** (M1−M3 < +$3.50, pinned BZZ26−BZG27) | +$6.93 on 10/1 daily rows (window not measurable) | NOT crossed, widening |
| `FRED-DCOILBRENTEU` / pinned >$120 | BZZ26 102.31 | NOT FIRED. >$100 line fired earlier, no revert |
| **GASREGW** (retail regular) | $4.465 wk-9/28 vs the $4.500 near-line (−0.8%) | **The nearest line.** Thursday's RBOB +4.4% leans toward a crossing; next print ~Mon 10/5 (EIA). Not graded |
| USO 150 call (Will's hand; sell-or-roll by 10/9) | USO closed **$150.02** on 10/1, exactly at the strike; 10/2 crude −3.5% pre-market | Measurement only. No rail is graded by me |

## §3 — GATE-BRENT-COT-35B review (review_by 2026-10-02)

- **Gradable now:** nothing new. The 9/29 vintage posts ~15:30 ET today. `cot_grade.py --expect 2026-09-29` at 08:34 ET: newest in-row 2026-09-22, **NOT FRESH, DO NOT GRADE**. Re-issue watch: the live 9/22 row matches the ledger (121,362 / 1,841,811).
- **Re-reproduced at the CFTC archive, 08:33 ET 10/2** (`fut_disagg_txt_2024/2025/2026.zip`, market by NAME, code 067651):
  - **4.909% = median of 104 weekly OI-shares 2024-08-13 → 2026-08-04 inclusive = 4.9086%.**
  - **Base = median MM shorts 6/16–8/4 (n=8) = 122,904.5.**
  - The archive's 9/22 row equals the ledger.
  - ⚠️ **The gate row's "NOT re-reproduced since 8/13" is stale.** BRENT already reproduced it on 2026-09-18 (REGISTRY COT-FUEL-35B note; STATUS standing row). Today is the second fresh reproduction. PROME should drop the ⚠ from the condition cell.
- **Armed state for the 15:30 print (pre-registered before it exists):**
  - Leg B needs MM shorts ÷ OI ≤ 4.909%. At OI ≈ 1.84M that means shorts ≤ ~90,400, a fall of ~31,000 in one week. **A joint SPENT is practically unreachable this print**, so the live outcomes are NOT-SPENT (shorts ≥118,326) or NO-VERDICT (shorts ≤118,325, i.e. −3,037 or more).
  - As-of Tue 9/29 means Thursday's rally is not in it.
  - Grade on the raw `f_disagg.txt` with a second pull. The ledger appends on rc=0.
- **Who grades:** the BRENT autonomous Friday routine fires ~14:00 ET, BEFORE the post (the structural defect on the row stands). **PROME should re-spawn BRENT at ≥15:35 ET** for the grade, or grade it at the next live BRENT session before Fri 10/9 (do not let two prints stack).
- **Proposed review_by:** keep **2026-10-02 (15:30 ET print)** for this vintage. After the grade, set **2026-10-09** (as-of 10/6).

## §4 — OPEC+ Sunday 10/4 (Docket L297; CATALYSTS letter pre-registered 9/6)

The seven-country group sets **November only**. My letter grades on the Secretariat statement text: (1) a second consecutive hold, the first point at which "pause" is a defensible word; (2) a resumed increment; (3) no decision.
- **Pre-meeting sourcing** (Bloomberg, two delegates, via investingLive / Yahoo / Investing.com): **hold November quotas steady**; "no final decision"; "most continue to produce below their output targets". That is delegate sourcing, never a grade.
- **My pre-registered read:** outcome (1), a hold, is the base case. Even a resumed increment would be mostly paper. Producers below target plus the Gulf export disruption mean deliverability, not quota, binds. The **spare-capacity figure must be re-pulled at a primary before grading** (the 0.02 mb/d EIA STEO is 8/13 vintage; the Oct STEO lands Tue 10/6).
- **What would surprise:** an increment with a deliverability claim attached, or an explicit statement on Gulf export restoration (Saudi/Kuwait/Iraq).
- **Resolution:** at opec.org (root-page entry; press-releases.html 403s) within 2 trading days. A BRENT session on Mon 10/5 should grade it, or PROME should spawn one.

## §5 — L0 drain (7 in the WALTER lane; -008/-019)

| Signal | Class | Disposition |
|---|---|---|
| `-021` RAF Fairford / Iran (UK PM) | INFO | info-only: HAWK's lane, no BRENT line |
| `-023` Russia strikes Kyiv energy grid | INFO | info-only: power grid, not oil; no BRENT line |
| `-026` US presses FR/DE on 120M bbl diesel or a targeted ban; Russia ban to 10/31 | **ACTION** | **acted.** State change recorded: CONDITIONAL + TARGETED threat, still no order. **Not B1** (no signed text; FR/PI/WH clean 08:34 ET 10/2). Russia extension already graded EXTENDED on CATALYSTS 10/1 (successor row 10/31). **Moves no registered line.** The 120M is single-wire, anonymous. The EU taskforce meets Fri 10/2 (Reuters, two EU diplomats): bearish diesel, relevant to VLO-HELD-01 leg A's distance (currently $11.94) |
| `-027` Petroline ~5.5 mb/d (Argus, one source) | INFO | noted: FALCON's grade. Record-only for me (WQ-331 P4: only the successor resolver grades Saudi relief). Not averaged |
| `-031` ECB pricing / NL gas-storage mandate | INFO | info-only |
| `-033` UKMTO 147-26 Hormuz tanker hit; Yanbu video UNVERIFIED | INFO | noted: report time 13:50 ET matches Thursday's step 2 (§2); no capacity line; BG-02 untouched |
| `-034` PBF Paulsboro turnaround | **ACTION** | **acted.** NOT new: PBF's plan, reported by OPIS (2026 plan) and again 7/31 (Q2), puts Paulsboro (165 kb/d) crude-unit work "in late fall … 30 to 35 days". **No start date published** (OPIS; the 7/31 item via iTiger). BRENT keeps no plant-level fall-maintenance base; aggregate utilisation from WPSR (92.5% wk-9/25) is the base, so a planned TA is in it by construction. INCIDENTS is facility-damage only ⇒ not logged |
| `-008` China halt (10/1) | ACTION | **already dispositioned:** `acted` in board_log 2026-10-01 13:28:05, file in `inbox/WALTER/processed/`. Re-used in §2 today |
| `-019` SPR exchange (10/1) | ACTION | **already dispositioned:** `acted` in board_log 2026-10-01 13:28:05, in processed/. CATALYSTS row 10/06 stands |

Sources: [Reuters via Yahoo, 10/1 15:34 ET](https://finance.yahoo.com/energy/articles/oil-dips-recovering-gulf-exports-044504275.html) · [Mediaite via Yahoo 18:39Z](https://www.yahoo.com/news/politics/articles/breaking-trump-sending-10-000-183949253.html) · [Il Sole 24 Ore](https://en.ilsole24ore.com/art/wsj-third-us-aircraft-carrier-in-the-middle-east-a-further-10000-troops-AJt2pJWB) · [investingLive OPEC+](https://investinglive.com/commodities/oil-opec-seen-holding-november-quotas-steady-at-sunday-meeting-delegates-say/) · [Yahoo OPEC+](https://finance.yahoo.com/energy/articles/opec-expected-keep-november-oil-102921735.html) · [OPIS PBF](https://www.opis.com/resources/energy-market-news-from-opis/pbf-energy-says-it-plans-to-conduct-turnaround-work-at-most-of-its-refineries-in-2026/) · [iTiger PBF 7/31](https://www.itiger.com/news/2655438815) · Federal Register API + public inspection + whitehouse.gov (08:34 ET 10/2) · CFTC `fut_disagg_txt_2024–2026.zip` + live `f_disagg.txt` · yfinance.
