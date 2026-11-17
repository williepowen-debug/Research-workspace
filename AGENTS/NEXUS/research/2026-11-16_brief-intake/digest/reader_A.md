# Digest reader A — 10 briefs (RED HENRY SAM VIOLET LIQUID BOND CARL BROCK GIBBS REGINALD)

**Written:** 2026-11-16 21:02 EST (from `date`) · read-only digest for the NEXUS 11/16 brief intake · reader model: Opus (Claude Code subagent)
**Method:** every brief read whole at HEAD; baseline = last commit at or before 2026-11-10 11:19 ET; `git diff <baseline>` read per brief. Figures quoted as the briefs state them; nothing computed. A PASS on the pin check proves the pin, not the content.

## Pin check (verbatim, run once from repo root)

```
BRIEF-PIN 0 OK: 10 brief(s) checked against amendment 11 (pin-follows-STATUS-HEAD) — OK-PINNED 6 · OK-SAME-COMMIT 3 · UNPINNED 1. A PASS proves the pin, never the brief's content; UNPINNED briefs are not A11-checked.
  ⚠️ RED       UNPINNED        no STATUS hash in the first 40 header lines — A11 not checkable; A10 fallback: brief commit 506e6e295 is BEFORE STATUS HEAD 6b5016a60
  ✅ HENRY     OK-SAME-COMMIT  brief and STATUS last committed together in 4eddf5e31
  ✅ SAM       OK-PINNED       pin aadac2268f = STATUS HEAD
  ✅ VIOLET    OK-PINNED       pin 53d60073a4 = STATUS HEAD
  ✅ LIQUID    OK-PINNED       pin 999f781573920f6737b0ff89395ef2ec16334a25 = STATUS HEAD
  ✅ BOND      OK-SAME-COMMIT  brief and STATUS last committed together in 78fec255b
  ✅ CARL      OK-PINNED       pin 17fba50e9f = STATUS HEAD
  ✅ BROCK     OK-SAME-COMMIT  brief and STATUS last committed together in fe4a7e9e4
  ✅ GIBBS     OK-PINNED       pin e0d6f6a5cd = STATUS HEAD
  ✅ REGINALD  OK-PINNED       pin efd26b2691 = STATUS HEAD
```

## Last commit times and working-tree state

| Desk | Brief last commit | STATUS last commit | Baseline (≤ 11/10 11:19 ET) | Brief size (B) | Working tree at read (20:58–20:59 ET 11/16) |
|---|---|---|---|---|---|
| RED | 2026-11-12 12:10:40 −0500 | 2026-11-12 15:34:59 −0500 | b47a7f4b7e (11/10 10:14) | 8,842 | brief and STATUS clean. STATUS committed 3 h 24 min after the brief (UNPINNED) |
| HENRY | 2026-11-16 16:35:34 −0500 | 2026-11-16 16:35:34 −0500 | 47d5eae59a (11/10 10:13) | 2,795 | clean |
| SAM | 2026-11-12 20:16:07 −0500 | 2026-11-12 20:16:01 −0500 | d220a30d5b (11/10 10:12) | 7,294 | clean |
| VIOLET | 2026-11-11 09:51:07 −0500 | 2026-11-11 09:50:32 −0500 | fc61614917 (11/10 11:16) | 5,808 | brief and STATUS clean. **Desk live:** workbook TSVs, fred_cache, board_log, corrections_receipts ` M`; 11 WALTER inbox moves staged |
| LIQUID | 2026-11-16 10:16:31 −0500 | 2026-11-16 10:16:20 −0500 | f5f5950111 (11/9 20:21) | **24,195** | brief and STATUS clean; `workbook/GATE079_CALENDAR_EXCLUDED.tsv` ` M` |
| BOND | 2026-11-13 11:43:07 −0500 | 2026-11-13 11:43:07 −0500 | 5a0d8de586 (11/9 19:41) | 2,474 | brief and STATUS clean. **Desk live:** `registry/cusip_vintage.tsv` ` M`, untracked `analysis/2026-11-16_long-end/` |
| CARL | 2026-11-14 11:26:23 −0500 | 2026-11-14 11:25:48 −0500 | 534aa070d1 (11/10 11:17) | 14,591 | **STATUS.md ` M` (desk live tonight).** Uncommitted header: "Updated: 2026-11-16 21:00 ET … Brent spot row corrected to FRED $92.14 11/11 … BEA 11/25 and 12/23 dates confirmed … no score, prediction or threshold moved." I read the committed brief (working tree = HEAD for the brief) |
| BROCK | 2026-11-16 11:28:17 −0500 | 2026-11-16 11:28:17 −0500 | 7794582852 (11/10 11:13) | **23,381** | brief and STATUS clean; untracked `inbox/2026-11-16_from-OTTO_crmt-evening-feed-read-nothing-since-11-13.md` (not read; filename only) |
| GIBBS | 2026-11-16 13:04:07 −0500 | 2026-11-16 13:03:59 −0500 | b21624efd5 (11/8 12:10) | 6,713 | clean |
| REGINALD | 2026-11-16 19:39:01 −0500 | 2026-11-16 19:38:33 −0500 | 7b7af52d51 (11/8 07:11) | **24,825** | clean |

---

## RED

- **HEADER:** "vS63 (2026-11-12 09:5x ET)". No STATUS hash in the header (UNPINNED per the pin check; STATUS HEAD 6b5016a60 postdates brief commit 506e6e295). Thesis version S63 (2026-11-12, discretionary).
- **VIEW:** HOLD 72 · net-bear 67 (from 68). Stag 32 · Managed 26 · Acute 20 · War 15 · Soft 4 · Rescue 3. "The 11/05 stress round-tripped in four sessions"; "The bear holds levels, not momentum"; "The Fed is the bull's new weak spot."
- **MOVED SINCE BASELINE (vS61 11/10 → vS63 11/12):**
  - **FT-06 exit run BROKE at 4 of 5:** VIXCLS 28.18 · 25.64 · 19.92 · 19.46 · 17.49 [11/11] ("FRED first-published 11/12 09:48 ET, equal to Cboe"). **RED-29 (50pct) WRONG, EVENT FALSE.** The mechanical Stag +2 / Managed −2 did not happen.
  - **S63 discretionary re-derivation: Stag 33 → 32, Managed 25 → 26; net-bear 68 → 67.** Inputs: 5y5y 2.15 [11/10], lowest since 4/22; January Brent settle 91.49 [11/10, BRENT] vs ~110 at S57; CHG-028 closed; held at −1 by third straight 0.3 core (3-mo 3.66) and 12/9 pricing +25 85.5 / +50 11.8 (ORACLE 11/11). Managed offset: payrolls +165K, claims 200K [w/e 11/07], card flow into 90+ 6.87%.
  - SoftBank figure refreshed from SAM 11/11: own-basis 22.5% (not 22.7%); ABB-inclusive 23.4–23.9%; RED's S62-b 24.05% "about 0.2pt high."
  - DEWEY 003R (11/11): $10–100B band coverage 115.97% → 116.76% (trigger OFF); $1–10B worsened, United Fidelity 69.1% of its new problem loans.
  - Non-session cells: FRED ICE OAS dated 11/11 (HY 330, CCC 1,330, BB 193) not counted.
  - Scorecard: 14 CORRECT · 11 WRONG · 6 ACTIVE (was 10 WRONG · 7 ACTIVE). Open challenges 8 → 6 (028 and 049 closed; 045 moved to 11/17; 057 to 11/19; 054 to 11/30).
  - Carried: Oct CPI core +0.3, FT-08 HOLDS; household debt re-spec NOT FIRED (23bp of 100bp).
  - VIEW levels: VIXCLS 17.49 [11/11]; HY 334 [11/09]; S&P 7,619.38 [11/11, WALTER]; SKEW 149.09 [11/11]; CCC 1,311 [11/09]; 10Y auction indirect 61.23% [11/10]; NVDA −5.5% [11/10, vendor]; USD/JPY 159.75 [vendor 11/12].
- **CROSS-DOMAIN / CALIBRATION:** Sends PROME the S63 packet. Waiting on FRED/LIQUID for the 11/10 ICE OAS cell, Will on CHG-045 (11/17), NVIDIA 10-Q guarantee line and ING data-center loan auction bids (11/19, CHG-057), FALCON weekly grade (11/18). Diverges: HY retracement does not un-fire FT-02 until <300 ×3; stagflation co-modal with managed decline; a hiking Fed is not a rescue; DEWEY's bank result is not uniform deterioration. **Uncertain about:** whether 12/9 goes 50 and its effect on the AI-funding edge; whether paper oil's fall is de-escalation or deal hope; whether the FRED 11/11 cell is the 11/10 session relabelled (LIQUID's call). Independence: oil decline counted once, on Stag; rates/banks/part of HY one antecedent.
- **FORWARD:** Tue 11/17 CHG-045 (Will only) · Thu 11/19 CHG-057 re-review + ING auction · ~11/25 FT-10 outcome horizon · Thu 11/26 Thanksgiving · Fri 11/27 VX-006 Zweig grade (tree by 11/20) · Mon 11/30 CHG-044, CHG-054 · Wed 12/9 FOMC · Thu 12/10 November CPI (FT-08 exit only on core ≤0.0, RED-28). Next discretionary re-derivation after 12/04 payrolls.
- **NEXUS-NAMED:** none in the brief.
- **FLAGS:** ⚠️ **Stale as of 11/12; desk has not seen the 11/12 HY 320 print, the 11/13 323 print, the 11/16 S&P −1.92% or VIX 22.91.** Its "HY 334, still over FT-02's 320 fire line" and FT-12 "74bp" are on the 11/09 cell. UNPINNED. "09:5x ET" approximated clock in header. Figures dated and sourced throughout.

## HENRY

- **HEADER:** "Owner fold: 2026-11-16 16:3x ET closeout on PROME's ask (prome-6f; Claude Code, Opus 5.5)." Equity closes vendor/Cboe delayed (16:18 ET); VIX Cboe 16:15 settle (read 16:32 ET); Treasury par 11/16; FRED 11/16 posts 11/17. Pin = same commit as STATUS (4eddf5e31).
- **VIEW:** "The Treasury Secretary's 10-day demand to Nvidia's board (WALTER SIG-W-20261116-002) took the S&P to 7,416.59 (−1.92%), its first close under my last published put wall, 7,500 [11/12]." Narrow, chip-led break; gamma NEGATIVE; VIX settle 22.91 under the 23 yellow line.
- **MOVED SINCE BASELINE (11/10 10:1x fold → 11/16 close):**
  - 11/16 closes (vendor/Cboe delayed, 16:18 ET): S&P 7,416.59 (−1.92%); NVDA $156.14 (−4.12%); SMH −5.11%; QQQ $661.75 (−2.67%, second close under 680); RSP −1.01%; IWM −1.65%; KRE $72.19 (−0.76%).
  - Treasury par 11/16: 10Y 5.12% (−3bp), "third straight close over my 5.0 red line"; 2Y 4.83%; 30Y 5.46%.
  - VIX settle 22.91 [Cboe 16:15], high 24.52; the 16:03 ET 23.02 read "was not the settle"; VIX3M 23.02, curve flat.
  - Gamma at 16:19 ET (chain = 11/13 open interest; not published): SPX flip 7,607 / 7,613, NEGATIVE about −$59B / −$78B per 1%; all walls withheld; QQQ flip 688–690 NEGATIVE.
  - Levels (own calc): 200-session threshold 7,342.33 (close 74.26 over); 50-day 7,666.42; red 7,037.04 (−10% from 10/6 peak 7,818.93); close −5.15% from peak. (Baseline: 200-day 7,328.21, 50-day 7,676.13.)
  - Credit (FRED 11/13): HY 323bp YELLOW; BB 186; CCC 1,316 RED; CCC−BB 1,130 (baseline FRED 11/6: HY 342, BB 208, CCC 1,317).
  - **Correction:** "the 11/13 VIX close was 19.30 (FRED VIXCLS), not the 19.03 I published; contango 1.063, not 1.078."
  - Forecasts: HEN-60 0.50 (open), HEN-61 0.28, HEN-63 hike 12/9 0.70 "(market price per ORACLE)". HEN-57, HEN-58, HEN-62 dropped from the list **without the brief stating their resolution** (HENRY STATUS: HEN-57 NOT FIRED 11/10; HEN-58 RESOLVED NONE 11/13; HEN-62 RESOLVED-HIT 11/10 at 2Y par 4.73).
  - WALTER routing: `ac69f2ac4c` → SIG-W-20261116-011 (ACTION PROME); TERRY NO CARD (relayed).
- **CROSS-DOMAIN / CALIBRATION:** LIQUID grades HY rows; ORACLE owns December pricing. Judgment into NVDA 11/17: "dealers amplify either way. Break failed = a close back over 7,500; regime turns = over about 7,610. Further-down signs: HY widening on 11/17's FRED print, QQQ staying under 680 with chips leading." Free-tier: "sign and flip robust, dollar sizes not." One Will decision registered by PROME (WILL_QUEUE row 697).
- **FORWARD:** FRED 11/16 on 11/17; NVDA results Tue 11/17 after the close; CYPHER row 9 at the 11/18 close (D:L1051); D:L823 11/19; calendar rebuild before 11/20; FOMC 12/9.
- **NEXUS-NAMED:** none.
- **FLAGS:** ⚠️ **"HEN-63 hike 12/9, 0.70 (market price per ORACLE)"** reads as a market price but ORACLE's dated read cited by RED/REGINALD is +25 85.5 / +50 11.8 [11/11]; HENRY's STATUS says 0.70 is the desk's own row "not re-marked" and "market price for the meeting is ORACLE's" — the brief's parenthesis conflates the two. Resolutions of HEN-57/58/62 not in brief. "16:3x ET" approximated clock. Otherwise fresh and well dated.

## SAM

- **HEADER:** "As of: 2026-11-13T01:16Z (20:16 ET 11/12), prome-0f wake (WQ-680 C9 continued): USD/JPY 160 row GRADED … STATUS commit `aadac2268f`."
- **VIEW:** "SoftBank is under its own 25% ceiling at today's Arm; December is live again; the 30Y auction was soft. No Japan-led carry unwind." v1.7 retired-to-LOW, no successor frame, no entry.
- **MOVED SINCE BASELINE (11/10 10:12 ET → 11/12 20:16 ET):**
  - **USD/JPY 160 row GRADED 20:1x ET 11/12 (H 160.044 / C 159.873): TOUCH ✅, NO CLOSE above 160 ❌, speed row not fired.** Own vendor high 160.044 at 11:41 ET, then −0.705 yen inside the 11:43 ET minute, yen-wide, two-thirds retraced; no rate check or intervention established; cause unknown. Katayama 11/13 09:47 JST words (REPORTED, transcript not posted).
  - Intervention funding open: reserve securities −$87.8B vs deposits $6.9B after July–August; reserves $1,179.1B [10/31].
  - **Correction 11/11: SoftBank own-basis leverage 22.5% at Arm $181.49 on full revaluation ("22.7% was the lookup convention")**; 22.8% with the settlement; with ABB $5.4B 23.4–23.9% (lookup 23.6–24.0%); 25% at Arm about $156–164. Yen rally raises it ~+0.04 point per yen.
  - 9984.T 11/11: open −7.2%, low ¥3,465, close ¥3,855 −0.44% on 82.7M (1.28×).
  - Q2 detail added: net loss −¥1,115.3B incl. ¥597.2B Silver Bands 7 write-off and ¥321.9B Intel collar loss; Musk turbine claim "a write-off, not a default" (corrected 11/10 17:20 ET).
  - 11/10: Fed December "~99% priced, HENRY `f3279ab9ac`"; USD/JPY 158.845 (11:30 ET, vendor); Totan BOJ December 76 (11/10 15:15 JST).
  - Insurers: MOF October lifers +¥62.3B net buying (first since May), after Sep −¥288.6B; banks −¥833.5B.
  - Calibration unchanged: 35 rows 16 CONFIRMED / 16 FAILED / 1 special / 1 qualified / 1 OPEN [SAM-33, 72%].
- **CROSS-DOMAIN / CALIBRATION:** VULCAN/LIQUID: "the reported 15.9% and the rolled 22.5% are different objects; quote the Arm price with any rolled figure." SAM proposes NO CARD on the 160 row; tradeability TERRY's via PROME. Waiting: CFTC 11/10 window (released 11/13), FRBNY Q3 (~11/13), SoftBank Q2 call transcript, an offshore basis instrument (absent).
- **FORWARD:** Nov-13 FRBNY Q3 FX report (est.), CFTC print, GMO briefing · Nov-16 Japan Q3 GDP · Nov-18 20Y auction (frozen bars), October trade balance · Nov-30 17:00 JST BOJ December purchase dates (SAM-33); MOF month-end intervention total ~11/30 · Dec 17–18 BOJ MPM.
- **NEXUS-NAMED:** "RED and NEXUS inbox packets on the 22.7% → 22.5% full-revaluation correction." · "Schema owner NEXUS (`AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` §4.1)."
- **FLAGS:** ⚠️ **Stale: as-of 11/12 20:16 ET; its 11/13 (CFTC, FRBNY) and 11/16 (Japan Q3 GDP) catalysts have passed unreported.** Internal inconsistency: the 11/10 update says "Totan BOJ December 76 (11/10 15:15 JST)" while the BOJ December section still reads "Totan incremental equivalent 72 (11/9 15:15 JST)" and "USD/JPY 158.6 vendor 11/10" — the older paragraph was not refreshed. "~99% priced" for December (11/10, via HENRY) differs from ORACLE's 11/11 read used elsewhere (see cross-brief).

## VIOLET

- **HEADER:** "As of: 2026-11-11 09:5x ET (from `date`) | STATUS commit: `53d60073a4`." Official Cboe History closes through 11/10; 11/11 row TICK. Thesis v4.1.9.
- **VIEW:** "🟢 11/11 09:32 ET: VIX 18.19, LOW_VOL, curve steeper (VIX3M/VIX 1.0935), credit following vol down (HY 334bp [11/09])." Convergence 33/50 not re-scored. "VX futures front still inverted into the 12/9 FOMC window."
- **MOVED SINCE BASELINE (11/10 11:2x → 11/11 09:5x):**
  - Status 🟡 → 🟢. 11/10 History VIX 19.46 (LOW_VOL by 0.54), SKEW 151.12; 11/10 close print VIX9D/VIX 0.9527, VIX3M/VIX 1.0606, VVIX 96.63, COR1M 12.35. CPI intraday high 21.61 (History; quote 21.43).
  - 11/11 09:32 ET tick: VIX 18.19 (−6.53%), VIX9D/VIX 0.9307, VIX3M/VIX 1.0935, VVIX 96.03, COR1M 11.10 ("Tick, not a close").
  - New: VX M1:M2 adjusted −1.98% (X6 19.9067 > Z6 19.5125, 11/10 settle), "inference … Untested; no flow evidence."
  - VVIX one-month realized vol 204.3% [11/10], highest since 2006 (KB-VIO-397).
  - Credit line changed from "calm vol is not calm credit" to "credit is easing, tails are not": HY 334bp [11/09], CCC 13.11%; MOVE 92.43 [11/10] (was 85.98).
  - OVX 53.10, OVX/VIX 2.73 CALM [11/10] (was 57.37 / 2.88 [11/09]). Carry-to-vol: RV10 6.99%, p35.2, USDJPY 159.65 [11/11 09:47 ET] (was 4.8%, p16.0, 158.73).
  - Veterans Day (D:L342): ICE OAS 11/11 non-session; VIOLET's VX_DAILY writer refuses closure rows (KB-VIO-395). Flags to LIQUID: FRED HY OAS carries prior values forward on NYSE closures, so a run count "can gain a day on 11/26."
  - Forecasts: VIO-PRED-10 CONFIRMED at 55%; PRED-07 CONFIRMED at 72%; PRED-08 (25%), PRED-09 (45%) open.
- **CROSS-DOMAIN / CALIBRATION:** RED-29 legs handed to RED (since graded WRONG by RED 11/12). NVIDIA cards to VULCAN/HENRY; VIOLET reads only transmission into the 11/17 NVDA → 11/18 VIX SOQ window. Path-B (LIQUID/VULCAN): correlation about 83% of the 11/05 variance rise. "The convergence score is not a probability." LOW_VOL rests on 0.08 and 0.54 points. Inverted analogs "Small sample." Credit-flat line "exploratory." Quote API highs are not History highs.
- **FORWARD:** 11/11 close (RED-29 last leg) · November 17 credit-vol WATCH endpoint and NVIDIA after the close · November 18 VIX AM SOQ · PRED-08 11/20 · December 16 L441 · PRED-09 12/31.
- **NEXUS-NAMED:** none.
- **FLAGS:** ⚠️ **Stale: as-of 11/11 09:5x ET, five sessions old; its NEXT DECISION POINT (11/11 close, next-boot History confirm) has passed; VIX 18.19 is a tick.** Desk live tonight with uncommitted workbook and inbox moves; brief not refreshed. "CCC 13.11%" is in percent where other briefs quote bp (1,311) — same figure, different unit.

## LIQUID

- **HEADER:** "As of: 2026-11-16T10:16:26-05:00 | STATUS commit: `999f781573920f6737b0ff89395ef2ec16334a25`." Source frontier: FRED ICE first-published 11/13 row (read 10:09 ET 11/16); CFTC TFF as-of 11/3; MOVE/VIX 11/13.
- **VIEW:** "Credit-price persistence is demonstrated. Generalized dollar-funding restriction is not." The AI "financing-constraint question stays NOT SHOWN": cost is up, mostly from rates, and the debt clears.
- **MOVED SINCE BASELINE (11/9 20:21 → 11/16 10:16), all first-published unless stated:**
  - **HY 334 (−8) [11/09]**; tier rule STALLS (first time this episode); >320 run 8 observations through 11/09.
  - 11/11-dated FRED ICE row (HY 330, IG 90, BBB 112, BB 193, B 347, CCC 1,330) **not counted** (D:L342); 11/10 row unpublished. "Re-dating the row is Will's call."
  - **HY 320.0 [11/12]: >320 run RESET to 0 of 3** (8 observations 10/29–11/09 ended); CCC +3 to 1,314, BB −17, B −11, CCC−BB 1,131; HY effective yield 8.16%. Tier rule STALLS.
  - **HY 323 [11/13]: >320 run restarts 1 of 3** (earliest MET the 11/17 cell); re-kill 0 of 2, 63 above 260; tier rule CONTINUES (B +5, CCC +2, BB +3), one print.
  - **GATE-LIQ-076 review: NOT MET, 1 of 3 (W3)**; W2 as-of 11/4 G10 −7,845, G5L10 +477; review_by now 11/20 (PROME).
  - DTCC 11/12: CoreWeave 5Y about 1,065 (~90 tighter than 11/10), Oracle 5Y about 295 (flat); 069 L2 not fired. Earlier 11/12 read: CoreWeave 4Y ~1,047 (one $3M trade) vs 1,093–1,105 [11/10].
  - IG tech yield (11/14, **corrected 11/16, CATO N14-2**): broad ICE IG yield 5.96% [11/12], +114bp YTD with spread +6 (83 → 89), "about 95% Treasuries"; tech index's own split unmeasured. Oracle +149 to +213 at every maturity on State Street marks [11/12]. 10Y 5.10% [11/12]; 5.15% par [11/13].
  - CoreWeave planned ≥$4B loan against Meta contracts: "a plan only (Bloomberg 11/11; no filing or terms)."
  - SoftBank 5Y CDS 475 after first Tokyo session (one trade, yen, ±10bp) vs 497 [11/9]. Skydance/Paramount 5Y CDS 529 [11/9]; TERRY re-open lines none crossed.
  - Funding: SOFR99−IORB +6bp [11/9], +7 [11/10]; 079 NOT ARMED. 10Y auction indirect 61.23% (lowest of 13); 30Y cover 2.36, indirect 68.11%.
  - Table row "HY >320 ×3": "Renewed run RESET 0 of 3 at 320 [November 12]" (the 11/16 update supersedes to 1 of 3; table not updated).
- **CROSS-DOMAIN / CALIBRATION:** Japan intervention funding OPEN (SAM's correction); H.4.1 11/19 split agreed with BOND (LIQUID: foreign official repo pool + FIMA; BOND: custody). BROCK owns X1 relative half; X1 CLOSED / DON'T-SIZE. December Fed pricing ORACLE's (WQ-671 A). VIOLET governs edge closes. Limits: "A clean sweep means no stress in what is visible, not no stress"; cross-currency basis, swap spreads, PB margin, repo haircuts unreachable; "The change in the tech premium over time is unmeasured."
- **FORWARD:** 11/17 HY cell (>320 run 2 of 3 possible earliest MET); 11/10 cell if FRED posts; 076 W1 as-of 11/10 (review_by 11/20); 11/19 H.4.1 foreign repo/FIMA; **ING data-centre loan bids 11/19, "the nearest named test of an AI financing constraint"**; 11/30 GENIUS Act read; Hertz Class B condition by 12/31. Predictions LIQ-08 HY ≥400 by 12/30 10%; LIQ-09 HY ≤320 on 12/30 38%; LIQ-10 5%; LIQ-11 30%.
- **NEXUS-NAMED:** none.
- **FLAGS:** ⚠️ **Over 22 KB (24,195 B).** Footer contradicts header: "This is the final STATUS fold of the November 14 session" under an 11/16 header. "Next: the November 13 ICE HY cell (Monday November 16 about 10:10 ET; run counts stand until then)" is already done in the 11/16 update. Registered-test table rows for 069/072/076/079 still carry 11/6–11/9 observations.

## BOND

- **HEADER:** "Last refresh: 2026-11-13 11:4x ET addendum closeout (desktop, PROME prome-72 RULING encode, WQ-682 A)". Treasury through 11/12 close; ICE through FRED-dated 11/12; FR2004 as-of 11/4; FHLB CFR 6/30/2026. bond-state: thesis v1.2.13; posture FLAT@2026-10-30. Pin = same commit (78fec255b).
- **VIEW:** pointer brief, no prose view. Refunding ended with "two I′ marker fires (3Y 11/9, 10Y 11/10) and one clean print; no dealer warehousing at any." Matrix 17/35 unchanged; sleeve FLAT, no proposal.
- **MOVED SINCE BASELINE (11/9 19:4x → 11/13 11:4x):**
  - 30Y `912810UY2` 11/12 CLEAN: indirect 68.11 vs I′ 63.89, dealers 11.39, BTC 2.36 (KB-BND-569). Counter 1, auction health 3. "Indirect bids do not identify Japan (KB-BND-571)." (Baseline: 3Y FIRE, BND-33 TRUE, counter 3 → 0.)
  - Rates 11/12 (KB-BND-573): 2Y 4.86, 10Y 5.10, 30Y 5.43 (+13/+12/+8 vs 11/10); real 10Y 2.86, run 44 sessions ≥2.50; 30Y run 90 sessions ≥5.00. (Baseline 11/9: 4.56/4.88/5.26; real 2.66.)
  - Mortgage spread: PMMS 7.11 − 10Y 5.10 [11/12] = 201bp; **VX-BND-17 2 → 1** (baseline 234bp [11/5]).
  - FR2004 long end $150.760B [as-of 11/4], +3.814; VX-BND-04 2.
  - Credit (KB-BND-577): HY 320 [FRED-dated 11/12], CCC 1314, IG 89 (baseline HY 342 [11/6]).
  - **FHLB red leg RULED A by Will 11/13 (WQ-682) and encoded:** "CFR issuer-stated all-borrower collateralization ratio ≤3.0 at a quarter-end OR >$900B system-wide"; latest 3.7 and $810.7B [6/30/2026], not met; VX-BND-18 2.
  - Benchmark demand VX-BND-20 2; Japan funding baselines (H.4.1, 11/11) KB-BND-576.
  - December Fed pricing: now cites ORACLE (WQ-671 A).
- **CROSS-DOMAIN / CALIBRATION:** LIQUID owns tier verdicts; ORACLE owns December pricing. FHLB caveat: "⚠️ n=2 of 30; confirms ~6 weeks late, never warns; blind to one bank; gross before haircuts. Q3 CFR not posted 11/13 10:27 ET." NBIM advice "still a proposal, no second holder."
- **FORWARD:** buyback op 11/17 20–30Y; H.4.1 first read 11/19 (Japan funding baselines; custody leg per LIQUID split); FR2004 predates the 11/16 refunding settlement; OPEN predictions BND-34 to 37 resolve 12/17–12/31 (BND-34 HY 352 open).
- **NEXUS-NAMED:** none (title "BOND → NEXUS").
- **FLAGS:** ⚠️ **FHLB latest is 6/30 ($810.7B, ratio 3.7) while REGINALD's 11/16 brief has the Q3 CFR: $798.428B [9/30] and all-borrower collateral ratio 3.6 [9/30] "to BOND via WALTER."** Not a contradiction, a vintage gap; the BOND red leg (≤3.0 or >$900B) is still not met on REGINALD's figures. Brief is 3.4 days old with the desk live tonight (untracked `analysis/2026-11-16_long-end/`). "11:4x" approximated clock.

## CARL

- **HEADER:** "Status: 🔴 v2.6.6 — concentrated household strain; broad spending collapse remains unestablished." "As of: 2026-11-14 11:25 ET | STATUS commit: `17fba50e9f`."
- **VIEW:** "Concentrated strain persists; broad collapse is still not established." Registered score 53/70 unchanged.
- **MOVED SINCE BASELINE (11/10 11:17 → 11/14 11:25):**
  - New SENDING rows (11/11): airfares two-year +23.27% Oct, +26.36% Sep (FRED); SA m/m +2.68/+1.16/+0.41% Aug–Oct; Citi modified-card 30+ share 18.59 → 19.08% completes the panel vs Capital One 17.2 → 25.2% ("cause UNKNOWN"; KB-619/620).
  - October core +0.296%; Waller's 50bp text verified; a hike lifts card APR (22.36%) about 1.1% relative per 25bp, at most $3.4B a year per 25bp (KB-615).
  - AAA regular under $4.00 (11/10 $3.979, 11/11 $3.943); EIA 11/09 $3.995 → V5 downgrade clock day 2 of 14 (earliest 11/24); CRL-34 leg 1 of 2.
  - **Grade: ES-02 / CRL-28 "GRADED 11/14 DID_NOT_APPEAR: 60-day avg 23.3/day vs frozen 55; CRL-28 50 → 20%, OPEN"**; next read moved to 2027-01-15.
  - Liberty Street 11/10 (KB-614): card flow into 90+ by zip-income quartile, 2026Q3 lowest 10.33 vs highest 4.40 (2.35×; 2.24× pre-pandemic); every quartile below its 2024Q4 peak.
  - 11/11 VIEW line: hike debate "a slow, small cost for indebted households, not a near-term delinquency trigger"; **CRL-36 stays 70%** ("re-mark to 60 offered, PROME declined 11/11").
  - Carried: Q3 HHDC card flow into 90+ 6.87% (CRL-33 MISSED, CRL-30 not fired); kill-rule RE-SPEC NOT FIRED (23bp vs 100bp floor); superseded AS-WRITTEN shadow MET.
- **CROSS-DOMAIN / CALIBRATION:** "Real risk channel is jobs (LABOR)." Kill-rule divergence sits with Will via PROME (CHG-RED-045 11/17); CARL proposes nothing. Capital One jump "issuer-specific on this measure." Airfare = "resilience, not squeeze." REGINALD owns bank read; RED/REGINALD own HY thresholds. Conviction: concentrated strain MEDIUM-HIGH; broad-collapse timing/level LOW. **Uncertain about:** FY2026 ALLY vintage (nine months old); September real spending and saving composition; student-loan cure share.
- **FORWARD:** 11/17 EIA 11/16 regular gasoline (CRL-34 leg 2, <$4.000) · 11/20 10:00 ET Michigan November final (long-run <3.0% is V12's trigger) · 11/23 11:00 ET AFT v. ED conference · 11/24 AAA <$4.00 two weeks (V5 4 → 3) · 11/25 08:30 ET October PCE/income (CRL-32 leg 1) · ~11/30 EART October 10-Ds · 12/04 November payrolls (V16 print 2 of 2) · Dec 8–9 FOMC (V12) · 12/10 Z.1/DFA cohort read · 12/23 final grade.
- **NEXUS-NAMED:** NEXUS appears only as a recipient in SENDING rows, e.g. "PROME / NEXUS / REGINALD / CORAL | 11/11 answers to WALTER SIG-W-20261111-016 and -017", "PROME / RED / NEXUS | 11/11 answer to WALTER SIG-W-20261110-001", "PROME / BRENT / NEXUS | AAA regular under $4.00". No line asks NEXUS for anything.
- **FLAGS:** ⚠️ **STATUS.md has uncommitted edits tonight (desk live; Brent spot row corrected to FRED $92.14 11/11); brief not refreshed.** Glued words: "EIA October19", "Gartner October26". Footer "Closeout (11/11, WQ-249, PROME prome-2b)" under an 11/14 header. VIEW bullet "Corporate credit: 11/05 HY 348bp (318 on 10/27)" is stale against HY 320 [11/12] / 323 [11/13]. Forward table out of date order (11/25 before 11/20).

## BROCK

- **HEADER:** "As of: 2026-11-16 (BROCK, prome-6f due-row wake D:L1139/L1099/L1059/L1071 + GATE-BRK-R2) | STATUS commit: the 2026-11-16 BROCK commit (`git log -1 -- AGENTS/BROCK/STATUS.md`) | Convergence 58/70, last rescore 9/25, unchanged. HY 323 [11/13, FRED, LIQUID's]; X1 NOT MET; ladder row 10 NOT FIRED."
- **VIEW:** "🔴 STAGE 2→3 — substance firming; bank transmission unconfirmed; X1 NOT MET, wrapper NOT ARMED." "Substance is firmer than established transmission."
- **MOVED SINCE BASELINE (11/10 → 11/16), no score moved on any day:**
  - 11/10 L928 letter now "FINAL at the 17:36 ET re-read (KB-BRK-476)"; CRMT $0.87, −23.46% 11/10.
  - 11/11: +100bp adds $0.10 (FSK) to $0.43 (BXSL) a share a year before fees; one 25bp hike does not close OTF's $0.06 quarterly gap (needs ~+196bp); interest cover OBDC 2.0x / OTF 2.1x at 9/30; "+25bp ≈ 1.94x … ESTIMATE"; 10Y 4.98 [Treasury 11/10]; CoreWeave Q3 debt $46.9B, EBITDA/interest ~2.67x.
  - 11/12: Trinity Capital AI-infrastructure equipment loans 13.5% of net assets at par 9/30; GPU financing "no lender withdrawal or repricing shown with a number"; **10Y 5.10 [Treasury 11/12] meets the Duration red rung again; no rescore.**
  - **11/13: CRMT TWELFTH BRIDGE graded (D:L1098)** — 8-K 0001171843-26-007415 accepted 11/13 09:15:15 ET, standstill to Mon 11/16; no new money (KB-BRK-489). **CABO D:L1058 NOT GRADED**: Light Reading 11/13 says hearing adjourned to 12/4, "conflicting with the 10-Q's 11/13 (not reconciled)"; GTCR + MBI moved 11/11 to intervene; CABO $2.80 [11/13 intraday], −46% from 5.16 on 11/5.
  - **11/16: BRK-11 RESOLVED TRUE** — ICMB asset coverage 141.6% at 9/30 (10-Q 0001193125-26-456667); "⚠️ No forecasting credit: ICMB was 149.5% at 12/31/2025, before the 2/23 forecast." **R2 review HELD → 12/07**: Monroe Q3 77.7% FINAL, run 2; BCRED and Monroe each one quarter from a third fire. CRMT STD 11/16: feed empty at 10:12 ET, NOT GRADED.
  - Monroe Q4 tender offer expires 11/30 (verified 11/16, KB-BRK-498).
- **CROSS-DOMAIN / CALIBRATION:** SHADE owns insurers; HANS EU seam; LIQUID HY; REGINALD/GIBBS banks; RED on SQN "whether asset-based lending is 'PC'". Rates: "income tailwind first, credit headwind later." Conviction direction HIGH, timing LOW, bank-recognition LOW. **Uncertain about:** OTF 13% TII vs ~25% NII; HTGC/GBDC funding squeeze not established; per-name draw amounts UNKNOWN.
- **FORWARD:** CRMT thirteenth-bridge read Mon 11/16 PM / Tue AM; backstop #9 Wed 11/18 · CABO intervention ruling week of 11/16, hearing Fri 12/4 (press-only) · 11/17 AMC GBDC annual results (resolves BRK-36) · L185 SHADE reconcile 11/05–18; L186 before W3 11/30 · Monroe offer expires 11/30; final ~12/04–12/07 · BCRED Q4 letter ~12/03 (forward table) / ~12/04 INFERRED (elsewhere), offer expires 12/1 · BRK-32 grade 11/30.
- **NEXUS-NAMED:** "Owner fold completed after final STATUS commit 84e7a03c1; NEXUS consumption remains unverified." NEXUS also a recipient in most SENDING rows (e.g. "NEXUS / PROME / OTTO | 🆕 11/16: no score moved, 58/70.").
- **FLAGS:** ⚠️ **Over 22 KB (23,381 B).** Pin is not a hash ("the 2026-11-16 BROCK commit"). **Glued words, many:** "ARCC95.77/BXSL88.51/FSK84.79/GBDC97.50/HTGC98.11/OBDC98.11%", "prior85.4", "nonUSD", "up to3pp", "June24,2025", "July30,2026", "September22,2026", "February27", "October6", "shareholderJuly22", "derivativeAugust11", "gaps0.01–3.00pp", "October23", "NDFI4→3 on9/3", "covers11/11", "March31", "June30", "Table9", "May30", "facilities477.9M versus408.2M", "~69.6M before", ".25 software names have191.686M", "final10-Qs", "CFG +52M", "WQ524", "KB376–384", "KB385/386". **Internal contradictions:** NEXT DECISION POINT says "R2 FIRED ×2, review HELD 10/31 (next 11/16 proposed)" while the 11/16 row says HELD → 12/07; footer cites "final STATUS commit 84e7a03c1" (not the current STATUS HEAD fe4a7e9e4); BCRED letter ~12/03 vs ~12/04. **Stale rows:** WAITING-FOR HTGC "10/29 AMC"; forward catalysts 10/29, 10/30, 11/04–05 still listed undated-as-done; VIEW "Next FSK 11/05 BMO". Untracked OTTO inbox packet tonight (filename: nothing since 11/13 on CRMT).

## GIBBS

- **HEADER:** "As of: 2026-11-16 13:05 ET | STATUS commit: `e0d6f6a5cd`."
- **VIEW:** "Large banks: Q3 read unchanged (deposit repricing shared, CRE mostly recognition, stress at PNC office and possibly Goldman CRE, Goldman's $368M unattributed)." Funding access open. Cyber: no large-bank consequence.
- **MOVED SINCE BASELINE (11/8 12:10 → 11/16 13:05):**
  - **Desk premise test R0 (11/16): 0 judgments moved at REGINALD or BROCK (KB-GIB-067) → dormancy recommended to Will via PROME.**
  - **Perimeter re-cut 11/16** (quarterly average assets, 12 CFR 252.2): **HBAN about $260–264B, over $250B (Category III, DERIVED)**; USB about $691–694B under $700B; FITB Category III (KB-GIB-065).
  - REGINALD answered the criticized-line question NO 11/11 (32a42bff7d); those tags stay NOT-YET-DETERMINABLE.
  - New VIEW lines: Northern Trust priced $2B senior notes on the 11/05 selloff day (5.300% 2031, 5.700% 2036). Hiking Fed: most of the 16 gain a little, five flat to slightly negative; capital watch level "the 10Y back above its 5.29% 9/30 mark."
- **CROSS-DOMAIN / CALIBRATION:** HBAN hand-off condition with REGINALD (packet 2026-11-16) — "HBAN moves only by a named hand-off in both desks' files." 11/05 fall (GS −6.44%, MS −5.93%, JPM −4.24%, KRE −2.47%, "WALTER vendor reads at 16:05 ET, not closes") "not explained by these fundamentals." Tension: CYPHER's CYB-INC-053 names GIBBS for Citizens (REGINALD's name). **Uncertain about:** GS provision sector; PNC 60–89 day CRE bucket; call-only NII guides at 7 firms; a late PHP2Shell victim.
- **FORWARD:** Will's R0 ruling (no date) · 2026-11-20 CYPHER R1 flip · 2026-11-23 vendor-guidance comment file (D:L798) · 2027-01-13 Q4 print cluster, CONDITIONAL on R0.
- **NEXUS-NAMED:** none.
- **FLAGS:** WAITING-FOR CYPHER row still lists past dates "11/06 · 11/09 · 11/12." No size or glue issues. Note for NEXUS: if Will accepts R0 dormancy, GIBBS leaves the brief census.

## REGINALD

- **HEADER:** "As of: 2026-11-16 19:38 ET, 11/16 third session, Will direct … | STATUS commit: `efd26b2691`."
- **VIEW:** "Severity concentrated on Q3 levels, with a qualifier: the registered breadth test L180 reads BROADER on its letter, weak [11/07]; frozen 8/20 score showed no skill." "The 10-year, not HY, moves regionals." "wide HY alone does not establish bank transmission."
- **MOVED SINCE BASELINE (11/8 07:11 → 11/16 19:38):**
  - **REG-T-06 REVIEW [11/16]:** FHLB advances $798.428B [9/30] on the Q3 CFR, "third official quarter >$700B", −1.5% q/q (Cincinnati −$22.1B, USB); breadth concentrated (PNC, Citi, Wells, Apollo ≥52.1% of YTD growth; SEC-panel median −0.4% YTD); "no escalation"; "REVIEW is not a crisis label." All-borrower collateral ratio 3.6 [9/30] sent to BOND via WALTER. (Baseline: "run 2-of-3 / REVIEW"; now "run 3 of 3".)
  - HY OAS 323bp [11/13] (baseline 348 [11/05]); REG-T-04 NOT FIRED, run 0-of-3.
  - **CRE exposure, all banks (9/30 Call Reports, 4,205 banks, SR 20-8 denominator):** $1–10B median 226% of capital, 175 of 889 (19.7%) at or above 300% (upper bound); broad 305%; $10–100B 217%, 13.7%. **Correction:** "First run mixed denominators (19.9%, 177); corrected." EGBN 245.8% old basis = 242.0% on SR 20-8. "Exposure, not distress."
  - **Reserves, all banks:** nonaccrual up with allowance down at 407 of 4,260 banks (9.6%, 15.7% of loans) in Q3 vs 8.8% in Q2: "a minority shape, not broad."
  - United Fidelity: brokered $1,006.5M; CDs due within a year at most about $363M; capital plan due Mon 12/14; pre-10/30 waiver "probable (INFERRED)"; "No read-across to the 14; no TERRY candidate."
  - Vendor guidance: 96 comments by 10:15 ET 11/16, none quantifies core-vendor dependence.
  - OZK: $956M reserve deposits, $581M paydowns across 711 modifications; Boston land $105.9M (Dec-2026 maturity) no named payer.
  - 11/11: **REG-31 TRUE against my 40%** (PFBC CRE 60–89 $150.2M [9/30]); six-bank reserves nonaccrual up 6 of 6, coverage down 6 of 6 (EGBN 88.48% → 67.20%); rates 2Y 4.46 → 4.73, 10Y 4.84 → 4.98 [11/05 → 11/10, Treasury]; 12/9 priced +25 85.5, +50 or more 11.8, hold 3.5 (ORACLE KB-ORC-133, 11/11); settled 11/10 WAL $76.30, KRE $73.09, FLG $10.51 (24 closes below RED).
  - VX.tsv FROZEN (11/16 third session).
- **CROSS-DOMAIN / CALIBRATION:** FHLB "totals do not name troubled borrowers or prove regional-bank funding stress." CRE exposure "is not evidence for concentrated-not-tier-wide." MHFIN "three times capital" roughly supported (305%) but "equating it with the 300% supervisory screen is the error"; 75% Class A claim UNVERIFIED. LIQUID owns contagion; CREED owns CMBS. **Uncertain about:** (1) "whether the bank-equity leg is now running AHEAD of credit"; (2) CFG Q2 FHLB draw; (3) OZK news magnitude; (4) MI3 cohort rule "decide before 11/07"; (5) whether the partial borrowing reversal persists.
- **FORWARD:** FDIC 9/30 population counts (~mid/late Nov, ESTIMATE; ~11/19 ESTIMATE) · Q3 QBP (~11/25) tests the 11/07 BROADER · United Fidelity capital plan Mon 12/14 · 12/31 Call Report (PFBC test) · fresh ranking frozen ~mid-Jan 2027 · size re-check "on 2026-11-20, whichever first."
- **NEXUS-NAMED:** none (file name only).
- **FLAGS:** ⚠️ **Over 22 KB (24,825 B)** while the rotation footer still says "Re-check size at any append or on 2026-11-20." **Glued words, many:** "November16", "November11", "November7", "November6", "November5", "November3", "November2", "November1–2", "October20", "Oct6", "Oct12", "since7/24 and338 Canada since8/19", "datedOctober20", "stillOctober19", "OPEN15%", "October21/22", "October21", "October27", "October23", "October26", "October30". **Stale lower body:** CALIBRATION "timing-M (resolvers: the 10/16–10/27 prints, then the 11/07 Call Report run)" and uncertainty (4) "decide before 11/07"; "Calibration vintage … credit observations still October19"; NEXT DECISION POINT "Prior text … Next: Eagle October21/22 named-loan outcomes, OZK October21 call"; WATCH table built on October dates. The top status is current; the lower half was not refreshed.

---

## Cross-brief (≤ 10 lines)

1. **HY OAS:** HENRY, LIQUID, BROCK, REGINALD 323 [11/13]; BOND 320 [FRED-dated 11/12]; **RED and VIOLET 334 [11/09] (stale)**; CARL 348 [11/05] in a VIEW bullet (stale). No disagreement on any shared date; RED's FT-02/FT-12 distances are on the 11/09 cell.
2. **CCC:** HENRY 1,316 [11/13]; LIQUID and BOND 1,314 [11/12]; RED 1,311 [11/09]; VIOLET "13.11%" [11/09] (same figure in percent). CCC−BB: HENRY 1,130 [11/13] vs LIQUID 1,131 [11/12]. Different dates, no conflict.
3. **10Y:** BOND, BROCK, LIQUID 5.10 [11/12]; LIQUID 5.15 par [11/13]; HENRY 5.12 par [11/16] (−3bp); REGINALD and BROCK 4.98 [11/10]. 2Y: BOND 4.86 [11/12], REGINALD 4.73 [11/10], HENRY 4.83 [11/16]. Consistent. GIBBS's capital watch level is 5.29 (10Y 9/30 mark); HENRY's red line is 5.0; BROCK's Duration rung 5.00 — three different lines on one instrument.
4. **⚠️ December FOMC pricing disagrees in framing:** RED and REGINALD cite ORACLE +25 85.5 / +50 11.8 (hold 3.5) [11/11]; SAM cites "~99% priced" (HENRY `f3279ab9ac`, 11/10); HENRY's brief prints HEN-63 "0.70 (market price per ORACLE)". BOND and LIQUID defer to ORACLE (WQ-671 A). HENRY's 0.70 is its own forecast row, not a market price; the parenthesis mislabels it.
5. **VIX:** RED 17.49 [11/11 VIXCLS]; VIOLET 19.46 [11/10 History], 18.19 tick [11/11]; HENRY 22.91 [11/16 Cboe settle], 11/13 19.30 (corrected from 19.03). Consistent on shared dates; RED and VIOLET pre-date the 11/16 move back over 20.
6. **USD/JPY:** RED 159.75 [vendor 11/12]; SAM high 160.044 / close 159.873 [11/12]; VIOLET 159.65 [11/11 09:47 ET]. No conflict. **SoftBank leverage:** RED and SAM agree 22.5% own basis, 23.4–23.9% with ABB.
7. **FHLB (vintage gap, not a conflict):** BOND $810.7B and collateral ratio 3.7 [6/30] ("Q3 CFR not posted 11/13 10:27 ET"); REGINALD $798.428B and ratio 3.6 [9/30, Q3 CFR], sent to BOND via WALTER. BOND's brief has not absorbed REGINALD's 9/30 figures.
8. **Household credit:** RED and CARL agree: card flow into 90+ 6.87%, re-spec NOT FIRED at 23bp of 100bp, CHG-045 for Will 11/17. Payrolls +165K agreed (RED, CARL). **Bank breadth:** RED (via DEWEY) and REGINALD agree "not uniform"; REGINALD 407 of 4,260 banks nonaccrual-up/allowance-down; GIBBS's HBAN-over-$250B re-cut awaits REGINALD's named hand-off.
9. **AI financing test 11/19:** RED (CHG-057 re-review, ING auction, NVIDIA 10-Q guarantee line) and LIQUID (ING bids "the nearest named test") name the same date; BROCK "no lender withdrawal or repricing shown with a number"; LIQUID "financing-constraint question stays NOT SHOWN". No brief has graded the Bessent 11/15 allegation except HENRY (tape only).
10. **NVDA 11/17 after the close:** HENRY (break-failed / regime lines 7,500 / ~7,610), VIOLET (11/17 → 11/18 VIX SOQ window; credit-vol WATCH ends 11/17), LIQUID (11/17 HY cell can make >320 run 2 of 3). VIOLET's and RED's briefs predate the 11/16 selloff entirely.

## Flags summary

- **Over ~22 KB:** REGINALD 24,825 B · LIQUID 24,195 B · BROCK 23,381 B.
- **Stale as-of (before the 11/16 selloff):** VIOLET (11/11 09:5x), RED (11/12, UNPINNED), SAM (11/12 20:16), BOND (11/13), CARL (11/14). VIOLET, BOND and CARL desks are live tonight with uncommitted work; CARL's STATUS.md is ` M`.
- **Glued words:** BROCK (heavy), REGINALD (heavy), CARL ("October19", "October26").
- **Self-contradiction / unrefreshed body:** LIQUID footer "November 14 session" under 11/16 header, "Next: November 13 cell" already done; BROCK R2 "next 11/16 proposed" vs HELD → 12/07, footer pin 84e7a03c1; REGINALD calibration/next-decision text keyed to October and 11/07; SAM Totan 72 vs 76 paragraphs; CARL closeout footer 11/11 under 11/14 header.
- **Figure labelling:** HENRY HEN-63 0.70 "(market price per ORACLE)"; HENRY drops HEN-57/58/62 without stating their resolutions; VIOLET VX M1:M2 inversion is an untested inference; SAM's "~99% priced" is a relay via HENRY dated 11/10.
- **Pin:** RED UNPINNED; BROCK's pin is a prose pointer, not a hash (passed as OK-SAME-COMMIT).
