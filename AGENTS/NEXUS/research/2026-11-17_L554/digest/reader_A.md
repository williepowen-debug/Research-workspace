# Digest reader A: HENRY, VIOLET, LIQUID, BROCK, REGINALD

Reader: read-only digest reader (Claude Code, Opus 5.5), run 2026-11-17. Baseline: NEXUS intake commit 3db8291eff (2026-11-16 21:04 ET). All five briefs were read whole from the working tree. None of the five has uncommitted edits (`git status` is clean on all five briefs; VIOLET has other uncommitted files: STATUS, CALENDAR, MEMORY, SCRATCH, CATALYSTS.tsv and one untracked research tsv).

Sizes (wc -c): HENRY 3,076 B · VIOLET 4,278 B · LIQUID 21,621 B · BROCK 21,179 B · REGINALD 21,350 B. All are under the 32,550 B read budget.

Brief commits since 3db8291eff:
- HENRY c349b210d3 (11/17 16:55 ET)
- VIOLET 47125539ad (11/16 21:27 ET, an intermediate fold after NEXUS's intake), then 032fc01884 (11/17 16:52 ET)
- LIQUID cd6a9a85d1 (11/17 10:55 ET)
- BROCK 931d9fac39 (file sweep, 11/17 afternoon), then 0d61ac9740 (11/17 16:08 ET)
- REGINALD 6ee5497857, then 8dfd0d7a33, then eb48dd2a97 (11/17 13:48 ET)

## Pin check (`python3 scripts/brief_pin_check.py`; overall line "BRIEF-PIN 1 STALE": 31 briefs, OK-PINNED 15, OK-SAME-COMMIT 10, STALE-PIN 3, UNPINNED 3)
- ⚠️ BROCK UNPINNED: "no STATUS hash in the first 40 header lines — A11 not checkable; A10 fallback: brief commit 0d61ac974 is BEFORE STATUS HEAD 39205bb8c". STATUS HEAD 39205bb8ce is BROCK's closeout at 11/17 16:11 ET, 3 minutes after the brief.
- ⚠️ HENRY UNPINNED: "no STATUS hash in the first 40 header lines — A11 not checkable; A10 fallback: brief commit c349b210d is AFTER STATUS HEAD bf68d3258".
- ✅ LIQUID OK-PINNED: pin d9b88f70c3ebafefb2989a9abff3eea34c6c3561 = STATUS HEAD.
- ✅ REGINALD OK-PINNED: pin d8816a1e6c = STATUS HEAD.
- ✅ VIOLET OK-PINNED: pin 079c3d1434 = STATUS HEAD, with this note: "uncommitted edits present — mid-closeout; graded on committed state".

A PASS proves the pin. It does not prove the content.

---

## HENRY

**HEADER:** "Owner fold: 2026-11-17 16:5x ET closeout on PROME's ask (prome-19, WQ-703; Claude Code, Opus 5.5)."
- Sources: equity closes are Cboe delayed and vendor quotes, agreeing to the cent (16:46 to 16:47 ET). The VIX is the Cboe 16:15 settle (stamp 16:15:01, read 16:46 ET). Yields are Treasury par 11/17. Credit is FRED 11/16.
- Pin: no STATUS hash in the header, so UNPINNED. Brief commit c349b210d3 is after STATUS HEAD bf68d3258f (11/17 16:53 ET).

**VIEW:**
- The S&P closed 7,340.53 (−1.03%) [11/17], 4.00 under the desk's own 200-session average of 7,344.53. HEN-60 is RESOLVED-HIT.
- The selling was broad, not led by chips. VIX settle 25.46, front curve inverted. Gamma is NEGATIVE, about 260 points under the flip.
- Nvidia beat its outlook, but its Q4 outlook excludes China data-center compute and the gross-margin guide is 71–72%. 11/18 is the first close that reflects the results.

**MOVED SINCE 3db8291eff:**

S&P, levels and gamma
| Item | Before [11/16] | Now [11/17] |
|---|---|---|
| S&P close | 7,416.59 (−1.92%) | 7,340.53 (−1.03%), "second close under my last published put wall, 7,500 [11/12]" |
| 200-session average | threshold 7,342.33 for the 11/16 close | 7,344.53, "own calc incl. today", margin 4.00 |
| 50-day average | 7,666.42 | 7,654.76 |
| Close from the 10/6 peak of 7,818.93 | −5.15% | −6.12% |
| Yellow 7,200 | (level unchanged) | 140.53 below the close |
| Red | 7,037.04 | 7,037.04 (unchanged) |
| SPX gamma flip | 7,607 / 7,613, NEGATIVE about −$59B / −$78B per 1% | 7,599 / 7,604, NEGATIVE −$64B / −$87B per 1%, about 260 under the flip (Monday's open interest; not published) |
| QQQ gamma flip | 688–690 | 681 / 680, NEGATIVE |

Walls are still withheld. The desk's own note: "the sign and the flip are robust; the dollar sizes are not."

Fire and grade
- **HEN-60 RESOLVED-HIT** (0.50, Brier 0.25). It was graded on the vendor close "as its letter allows before FRED posts; FRED is checked 11/18".
- ⚠️ In the desk's own words: "The average is my own calculation and the margin is 4.00."
- Sent to WALTER as a signal (ACTION PROME, INFO TERRY, VIOLET).

Breadth [11/17]: RSP −1.45%, IWM −1.43%, KRE $70.85 (−1.86%), against NVDA $155.46 (−0.44%), SMH −0.39%, QQQ $656.95 (−0.73%). Prior [11/16]: NVDA $156.14 (−4.12%), SMH −5.11%, QQQ $661.75 (−2.67%), RSP −1.01%, IWM −1.65%, KRE $72.19 (−0.76%).

Cause: "It came on the day of the BIS chip-rule card (SIG-W-20261117-007); the cause is not established."

VIX
- Settle 25.46 [11/17] (+11.1%), over HENRY's 23 yellow line. Prior: 22.91 [11/16], under it.
- VIX9D 26.70 is over VIX3M 24.98: front curve inverted. Prior: VIX3M 23.02, curve flat.

Rates
- 10Y par 5.10% [11/17] (−2bp), "the fourth close over 5.0". Prior: 5.12% [11/16].
- 2Y 4.80% [11/17]. Prior: 4.83%.
- 30Y: no longer stated (prior 5.46% [11/16]).

Credit (now FRED 11/16; was FRED 11/13)
- HY 334bp YELLOW (+11). Prior: 323.
- BB 196 (+10). Prior: 186.
- CCC 1,310 RED (−6). Prior: 1,316.
- The CCC−BB figure of 1,130 is dropped.

Nvidia (new; press release 11/17)
- Revenue $115.8B against its own $108.0B ± 2% outlook; Data Center $107.6B.
- Q4 outlook $130.0B ± 3% "including an extra week, with no China data-center compute"; gross-margin guide 71–72% against 74.9%.
- After hours (vendor, before the call, not closes): NVDA $158.50 (+1.96%), ES +0.22%, NQ +0.37%.

Removed lines
- The 11/13 VIX correction line (19.30, not 19.03; contango 1.063) is gone.
- The WILL_QUEUE row 697 reference is gone. The brief now says "Nothing is needed from Will."

Forecasts
- HEN-61 0.28 and HEN-63 0.70: unchanged.
- New: "The 8 old rows the audit found are graded Fri 11/20."

**CROSS-DOMAIN / CALIBRATION:**
- "VULCAN owns the capex-chain meaning."
- "LIQUID grades the HY rows."
- "VIOLET broadcasts" (the VIX line).
- HEN-63: "the market price is ORACLE's".
- Uncertain: the cause of the 11/17 selloff ("not established"). HEN-60 rests on HENRY's own calculation, a 4.00 margin, and an unposted FRED close.

**FORWARD:**
- 11/18: FRED for 11/17; the first post-results gamma map.
- 11/18 judgment: a close back over about 7,345 makes HEN-60's condition a one-day breach. A close over about 7,600 (+3.5%) turns the regime.
- 11/18 close: CYPHER row 9 (D:L1051).
- 11/19: D:L823.
- 11/20: the 8 old audit rows are graded; calendar rebuild before 11/20.
- 12/9: FOMC (HEN-63 rate hike, 0.70).
- 12/31: HEN-61 record close, 0.28.

**NEXUS-NAMED:** none.

---

## VIOLET

**HEADER:** "As of: 2026-11-17 16:5x ET (from `date`) | STATUS commit: `079c3d1434`".
- History closes run through 11/16 (SETTLE, 0 corrected). The 11/17 row is TICK.
- Pin check: OK-PINNED, with a mid-closeout note (uncommitted STATUS edits, graded on committed state).
- ⚠️ Baseline note: at NEXUS's intake (3db8291eff) the VIOLET brief was still the 11/11 09:5x ET version (STATUS 53d60073a4). The diff below therefore spans 11/11 to 11/17 and includes the intermediate fold 47125539ad (11/16 21:27 ET).

**VIEW:**
- 🔴 On the 11/17 close print (a TICK): VIX 25.46, cash curve INVERTED (VIX3M/VIX 0.9811), VVIX 121.28, all before Nvidia reported.
- The release took about 3% out of the expiring X6, not the premium. Credit is not confirming (HY 334bp [11/16]).
- RISING_VOL on History from 11/16. Convergence 34/50.

**MOVED SINCE 3db8291eff:**

Status and regime
- Status 🟢 LOW_VOL [11/11, VIX 18.19 tick] → 🔴.
- **Regime shift FIRED (KB-VIO-400):** LOW_VOL [11/13, 19.30] → RISING_VOL [11/16 History, 22.91]. In the intermediate 11/16 fold (KB-VIO-399) this was provisional on a tick of 22.91.
- Convergence 33/50 → **34/50**, on 11/16 History (VVIX 3→4, front curve 3→4, credit 4→3).

Fires on the 11/17 print
- **Cash-curve inversion 🔴:** VIX 25.46 > VIX3M 24.98, ratio 0.9811, "First since 11/06". Outbox SIG `outbox/2026-11-17_SIG-VIO_to-LIQUID-HENRY-RED_inversion-vvix120-on-close-print.md`.
- **VVIX 121.28 > 120 🟠** (high 127.85), "First since 11/06". In the 11/16 fold both of these were NOT FIRED.

"VIX +30% in 5 days, credit flat" row
- VIX leg MET: 19.46 [11/10] → 25.46, +30.83%.
- Credit leg PENDING the FRED 11/17 cell, which must be ≤ 355bp (330 [11/10], 334 [11/16]).
- In the 11/16 fold this row was NOT MET (+15.0%).

**Credit-vol WATCH (KB-VIO-328) CLOSED, size condition NOT MET (KB-VIO-401)**
- Size condition 368bp; peak 348 [11/05]; 334 [11/16]. "Path B, not a credit lead."
- "It reopens only if the 11/17 cell is ≥ 368."
- ⚠️ This was closed at the 11/17 close. The 11/16 fold had said it grades at the 11/18 boot on the FRED 11/17 print.

Nvidia window (inference, delayed quotes)
- Into the release: X6 settled 24.7417, 9.05% over Z6; VIX9D/VIX 1.0487.
- After it: X6 24.00 (−3.0%), Z6 22.20, X6 still 8.1% over Z6. NVDA up 2% to 4% after hours (not a close); ES +0.3%.
- 11/16 fold for comparison: VIX9D/VIX 1.0105; X6 about 6.8% over Z6 on the 11/16 settle.

RED bars (History)
| | 11/11 | 11/12 | 11/13 | 11/16 |
|---|---|---|---|---|
| SKEW | 149.09 | 150.16 | 147.14 | 146.33 |
| VIX | 17.49 | 18.70 | 19.30 | 22.91 |

- No 11/17 SKEW bar yet.
- Intermediate fold: "11/11 VIXCLS 17.49 < 18.00, so RED-29's last leg missed"; FT-10 exit 0 of 4.

Other vol readings
| Item | Earlier | Now |
|---|---|---|
| MOVE | 92.43 [11/10] | 101.28 [11/16] |
| OVX/VIX | 2.73 CALM [11/10]; 2.16 [11/16] | 1.94 CALM [11/17] |
| SAM RV10 | 6.99%, p35.2, USDJPY 159.65 [11/11]; 5.79%, p22.4, USDJPY 159.78 [11/16] | 6.14%, p26.0, USDJPY 159.34 [11/17], CALM |

Forecasts
- PRED-08 (VIX ≥ 30 by 11/20, 25%): "4.54 short on the print, 3 sessions left". The 11/16 fold said 7.09 short on the tick.
- PRED-09 (SKEW < 140 by 12/31, 45%): open.
- PRED-07 and VIO-PRED-10: CONFIRMED earlier; no longer listed.

Calibration and routing
- Tick vs History: "the 11/16 tick matched History exactly (0 corrected). The 11/11 morning tick had overstated VVIX by 5.65."
- TERRY packet (WQ-696): `AGENTS/TERRY/inbox/2026-11-17_from-VIOLET_nvda-close-vol-read.md`. Text: "No direction on NVDA"; "two of the 11/16 invalidators hit before the release".
- PROME packet: `PROME/inbox/2026-11-17_from-VIOLET_nvda-close-watch-endpoint.md`.

**CROSS-DOMAIN / CALIBRATION:**
- "Release content is VULCAN's (WALTER SIG-W-20261117-019): a beat, a guide with no China data-center compute, a margin guide of 71 to 72%, and the CEO search and board investigation named."
- "FT-06, FT-10 and RED-29 are yours" (RED).
- MOVE: "Yours" (BOND / HENRY).
- Oil: "Oil is not leading" (BRENT / HAWK).
- Carry-to-vol: CALM (SAM).
- Test after 11/18: "VIX9D/VIX back under 1 means it was an earnings premium. If it holds, the premium is policy and governance (the BIS rule, China's countermeasures, Bessent's clock about 11/26)."
- Calibration notes: "Inversion: marks peaks, not onsets (KB-VIO-034)." "the score is not a probability." The 11/17 values are a TICK.

**FORWARD:**
- 11/18 (wake asked for 11:00 ET): VIX AM SOQ and X6 final settlement; VIX9D/VIX after it; the FRED 11/17 HY cell (the +30% row's credit leg and the WATCH endpoint); History for 11/17.
- 11/20: PRED-08.
- About 11/26: Bessent deadline (card).
- 12/16: L441.
- 12/31: PRED-09.

**NEXUS-NAMED:** none.

---

## LIQUID

**HEADER:** "As of: 2026-11-17T10:55:33-05:00 | STATUS commit: `d9b88f70c3ebafefb2989a9abff3eea34c6c3561`". Pin check: OK-PINNED.
- Source frontier: FRED ICE first-published November 16 row (HY 10:46 ET, tiers 10:50 ET 11/17); OFR repo volumes to November 13; CFTC TFF as-of November 10.
- ⚠️ This is a morning fold. It predates the 11/17 close (VIX 25.46, inversion, HEN-60).

**VIEW:**
- HY 334 [11/16] puts the WQ-444 >320 run at 2 of 3. It is MET on the 11/17 cell if that cell is above 320.0.
- The tier rule BROADENS on the daily clause, led by BB while CCC tightened.
- Financing constraint stays NOT SHOWN (Cable One, CoreWeave). Funding is PARTIALLY INSTRUMENTED / SUPERVISOR-BLIND.

**MOVED SINCE 3db8291eff:**

HY run and re-kill
- **HY 334 [November 16, first-published], +11.** Prior: 323 [11/13].
- WQ-444 >320 run **2 of 3** (323 [11/13], 334). Prior: 1 of 3.
- "MET on the November 17 cell if above 320.0 (FRED about 10:10 to 10:50 ET 11/18)."
- Re-kill 0 of 2, "74 above 260". Prior: 63 above 260.

Tiers [11/16]: BBB 112 (+1), BB 196 (+10), B 357 (+13), CCC 1,310 (−6).
- **Tier rule BROADENS** on the daily clause ("BB +10 meets its +9 p95"), "one print led by the middle of the ladder while CCC tightened". The 15-session clause is not met.
- Prior: CONTINUES [11/13].

Gates
- 069 L1 and L4 NOT FIRED on November 16 ("all four AI names −6% to −10%, none at −15%").
- 072 NOT FIRED (IG 90, basis 244).
- GATE-LIQ-076 NOT MET 1 of 3, review November 20.
- Table row "HY >320 ×3 / re-kill" was updated to run 2 of 3 [November 16, HY 334]. The other table rows (069, 072, 076, 079) are unchanged and still dated November 6 to November 9.

Cable One (new)
- Skipped an about $10M coupon due 11/16 (8-K 16:41 ET, BROCK KB-BRK-503; BROCK owns the credit).
- 0.160% of XCCC, "so about 1 to 2 bp of CCC at most"; "the November 17 cell is the first that can show it".
- About $675M cash and a planned new financing, "so a financing constraint is NOT SHOWN".

Funding and housekeeping (new)
- OFR tri-party, GCF and DVP repo volumes are now reachable: "no contraction to November 13; volume is not capacity; KB-LIQ-162".
- Funding microstructure stays PARTIALLY INSTRUMENTED / SUPERVISOR-BLIND.
- Re-kill regression tests repaired ("fixtures dated on a bond holiday; watcher unchanged, no reading affected").
- CoreWeave: the planned loan of at least $4B against Meta contracts is still a plan only. Like-for-like is its March DDTL 4.0, $8.5B at SOFR + 2.25%, A3: "access, not a wall". This is unchanged in substance from 11/16.

Rotation: the November 13, November 12 and November 10–11 updates were rotated verbatim (crc32 42b13ffa) to `archive/status_snapshots/NEXUS_BRIEF_rotated_2026-11-17.md`.
- These held: the 11/13 reset to 0 of 3 at 320.0 [11/12]; DTCC 11/12 CoreWeave 5Y about 1,065 and Oracle 5Y about 295; the 11/11-dated FRED row question; the 30-year auction cover 2.36.
- They are not new figures, but they are no longer in the hot brief.

**CROSS-DOMAIN / CALIBRATION:**
- Owner pointers in the brief:
  - "BROCK owns the credit" (Cable One).
  - "BROCK owns X1 relative half."
  - "VIOLET governs edge closes."
  - "December Fed-meeting pricing is ORACLE's (WQ-671 A)."
  - On the November 19 H.4.1: "BOND reads custody".
- ⚠️ Desk's own: "The change in the tech premium over time is unmeasured" (IG tech, corrected 11/16, CATO N14-2).
- "A clean sweep means no stress in what is visible, not no stress."
- Not reachable: cross-currency basis, swap spreads, prime-brokerage margin, repo haircuts, Treasury bid-ask.
- Stale text remains in the body (owner residue, not changed this fold):
  - "Existing next tests" still says "Next: the November 13 ICE HY cell (Monday November 16 about 10:10 ET; run counts stand until then)".
  - It also still says "This is the final STATUS fold of the November 14 session".

**FORWARD:**
- 11/18, about 10:10 to 10:50 ET: FRED November 17 HY cell. The >320 run is MET if above 320.0. The same cell is the first that can show Cable One.
- November 19: H.4.1 foreign repo pool and FIMA read (BOND reads custody); ING's data-centre loan bids, "the nearest named test of an AI financing constraint (KB-LIQ-153)".
- November 20: GATE-LIQ-076 review; 076 W1 as-of November 10 (review_by November 20).
- November 30: GENIUS Act read (owed).
- Predictions:
  - LIQ-08 HY ≥400 by December 30, 10%.
  - LIQ-09 HY ≤320 on December 30, 38%.
  - LIQ-10 SOFR99−IORB ≥+30 twice by December 28, 5%.
  - LIQ-11 Standing Repo ≥$25.0B on December 31, 30%.
- December 31: Hertz Class B funding condition.

**NEXUS-NAMED:** none, apart from the rotation path name `archive/status_snapshots/NEXUS_BRIEF_rotated_2026-11-17.md`.

---

## BROCK

**HEADER:** "As of: 2026-11-17 (BROCK, prome-19 due-row wake D:L1139/L1099/L1071, afternoon CABO/CRMT exposure chain for Will, file sweep 14:27 ET, BRK-36 graded TRUE 16:08 ET) | STATUS commit: the 2026-11-17 BROCK commit (`git log -1 -- AGENTS/BROCK/STATUS.md`)".
- Pin: UNPINNED. Brief commit 0d61ac9740 (16:08 ET) is before STATUS HEAD 39205bb8ce (16:11 ET closeout).
- Convergence 58/70, last rescore 9/25, unchanged.
- ⚠️ The header still reads "HY 323 [11/13, FRED, LIQUID's]", while LIQUID's brief has 334 [11/16].
- ⚠️ The footer still reads "Owner fold completed after final STATUS commit 84e7a03c1; NEXUS consumption remains unverified". This is an old line and was not changed this fold.

**VIEW:**
- 🔴 STAGE 2→3: "substance firming; bank transmission unconfirmed; X1 NOT MET, wrapper NOT ARMED."
- 11/17: BRK-36 TRUE (GBDC NAV down), the CRMT thirteenth bridge, and the CABO skipped coupon. "No listed company bears a loss large relative to itself."

**MOVED SINCE 3db8291eff:**

**BRK-36 RESOLVED TRUE (11/17)**
- Golub (GBDC) 9/30 NAV/sh $14.00 vs $14.25 (−1.75%), 8-K 0001476765-26-000083 at 16:04 ET.
- "issuer cites names on or taken to non-accrual"; NII $0.32 vs $0.33 distribution (KB-BRK-513).
- Call Wed 11/18 10:00 ET.

**CRMT THIRTEENTH BRIDGE** (D:L1139)
- Agreed Mon 11/16; 8-K 0001171843-26-007505 accepted 11/17 08:00:32 ET.
- Relief to Wed 11/18, "2 days, the shortest of 13" (KB-BRK-501).

**CABO skipped ~$10M interest due 11/16**
- On ~$503M 4.00% 2030 notes; 30-day grace to ~12/16; NYSE 802.01B notice 11/13 (KB-BRK-503).
- "Its ~$675M cash at 9/30 is borrowed": revolver $1.05B drawn at 9/30, last $200M drawn 10/8, $478.9M MBI put liability.
- "issuer says sources are insufficient for the 2027–28 maturities (KB-BRK-506)".

**Exposure chain (Will's task)**
- CABO's 13 named revolver lenders, 11 listed, largest CFG 0.32% of equity.
- Closed-end funds RA 0.65% and ACP 0.60% of NAV; OBDC 0.044% of NAV via Credit SLF.
- CRMT lenders all private (Silver Point, Beach Point); no live bank line (KB-BRK-507 to 509).

**Fed FSR 11/13** (read at primary): "riskier AI-SPE tranches held by HY funds, life insurers and BDCs; largest banks close to $1T of exposure (KB-BRK-510)".

The 11/16 row (BRK-11 RESOLVED TRUE, ICMB 141.6%; R2 review HELD → 12/07; Monroe Q3 77.7% FINAL) was already present at 3db8291eff and is unchanged.

Removed rows and lines, with no rotation pointer (footer: "historical observations remain dated in catchups/ and Git")
- Removed cross-domain rows:
  - CRMT eleventh bridge (KB-BRK-472, CRMT $0.87, −23.46% 11/10).
  - The 11/09 row (L927; ADS Q3 FINAL 14.75% demand, 33.89% satisfied, $698.3M notes; KBDC non-accruals 3.6% from 2.7%, KB-BRK-467/468).
  - CRMT ninth bridge (KB-BRK-415; Second Amendment $5.0M new money senior to ~$305.6M).
- Removed from the waiting table: the HTGC falsifier row.
- Removed from the catalyst table: the 10/29 HTGC, 10/30 CRMT/CABO, 11/02, 11/04–05, 11/05–18 SHADE L185 and 11/17 GBDC rows. GBDC is now a ✅ row.
- Removed from the view: the "Documentation closeout" bullet.

Re-dated or updated
- Duration pivot ③: "latest 4.96 [FRED 10/22] is below the rung" is replaced by "10Y 5.10 [Treasury 11/12] above it again, no fifth rung".
- CRMT waiting row: now the fourteenth bridge, STD Wed 11/18, read Thu 11/19 ~08:00–09:30 ET, backstop #9 Wed 11/18.
- CABO waiting row: grace ends ~12/16 (INFERRED); NYSE plan ~12/28; hearing Fri 12/4 (press-only).
- Open constraints: "Next FSK 11/05 BMO" is replaced by "FSK Q3 read 11/05 (KB-BRK-420/421)".
- Next decision: R2 review 12/07, with the BCRED Q4 letter ~12/03–12/07 and the Monroe Q4 final ~12/04–12/07 as the live (a) reads. W3 grades 11/30, and "FSK leg not reversed, so ≥3 of 4 is out of reach".
- BRK-26: "needs a formal SEC enforcement filing (SQN does not resolve it, KB-BRK-429)". The earlier text called SQN a CANDIDATE pending RED (KB-BRK-413).
- BRK-25: "needs an arm's-length sub-90¢ print, count 2".

No score moved; still 58/70.

**CROSS-DOMAIN / CALIBRATION:**
- Domain boundaries: "Insurer exposure belongs to SHADE; EU bank/private-credit seam to HANS."
- "HY 323 [11/13, FRED, LIQUID's]".
- "RED/REGINALD own their rung consequences."
- "no investment implication (TERRY told)".
- "OTTO V-row context only".
- Waiting on:
  - Banks / REGINALD: "CFG +52M attribution"; "PC-attributable reserve build can fire as written".
  - SHADE / LIQUID: joint X1 normalization, L185 11/05–18 and L186 before W3 11/30.
- Conviction: "direction HIGH, timing LOW, bank-recognition LOW."
- Uncertain about: the OTF "13% TII vs ~25% NII" denominator; HTGC/GBDC current funding squeeze "not established"; per-name draw amounts UNKNOWN.

**FORWARD:**
- 11/18: GBDC call 10:00 ET; CRMT STD Wed 11/18, backstop #9.
- 11/19 AM: CRMT read (fourteenth bridge, waiver, transaction, acceleration or 1.03).
- 11/24: IREN AGM.
- 11/30: W3 grade (L183); BRK-32 STUCK (L716); Monroe Q4 offer expires.
- ~12/03–12/07: BCRED Q4 letter (offer expires 12/1) and Monroe Q4 final. "A sub-100% at either FIRES R2 (a) at a third vehicle."
- Fri 12/4: CABO hearing (press-only date).
- 12/07: GATE-BRK-R2 review.
- ~12/16: CABO coupon grace ends (INFERRED). "Unpaid = default and cross-default."
- ~12/28: CABO NYSE plan.
- 12/31: BRK-25/26/33/34/35/37; IE Mackenzie draw end.

**NEXUS-NAMED (verbatim):**
- Row recipients "NEXUS / PROME / TERRY" (the 11/17 row, quoted above), "NEXUS / PROME / OTTO", "NEXUS / PROME / LIQUID", "NEXUS / PROME", "NEXUS / VULCAN / LIQUID", "NEXUS / LIQUID / TERRY", "NEXUS / LIQUID".
- Footer: "Owner fold completed after final STATUS commit 84e7a03c1; NEXUS consumption remains unverified."

---

## REGINALD

**HEADER:** "As of: 2026-11-17 13:48 ET, Will-direct session: Q3 bond-loss wording corrected after review (12:29 entry: Q3 full-universe counts on the FFIEC bulk 9/30 file; REG-T-02 token renamed, label only) | STATUS commit: `d8816a1e6c`". Pin check: OK-PINNED.
- ⚠️ The Status line was not updated for HY. It still reads "HY OAS 323bp [11/13] (REG-T-03 already FIRED; REG-T-04 NOT FIRED, peak 348 [11/05], run 0-of-3)". LIQUID's brief has 334 [11/16].

**VIEW:**
- Severity is concentrated on Q3 levels, with the L180 BROADER qualifier. REG-T-06 REVIEW (FHLB $798.4B, concentrated).
- New 11/17: Q3 unrealized securities losses are BROAD across all banks. It is a vulnerability if banks must sell, not a liquidity crisis.
- "The 10-year, not HY, moves regionals."

**MOVED SINCE 3db8291eff (all new 11/17 entries):**

**Bond losses, all banks** (FFIEC bulk 9/30, 4,267 filers; KB ML-REG-307/308)
- Median bank unrealized securities loss 6.8% → 11.5% of equity pretax in Q3.
- Banks at ≥20% after tax 622 → 1,113 (14.5% → 26.1%; same 4,257 banks 613 → 1,113).
- System dollars $324.7B → $485.7B "(+50%, not doubled)".
- "10Y 4.44 → 5.29, the likely main driver, not isolated" (period endpoints not dated in the brief; context is Q3).
- "Broad, not concentrated." "941 of the 1,113 cross on AFS alone." AOCI opt-out 4,205 of 4,245; HTM 61% of dollars.
- "part reversed in Q4 to date". "TERRY: no implication on its own."
- **Correction:** "Corrected 13:48 after Will's reviewer: the 12:29 text said 'a loss only on forced sales', wrong for AFS."

**Friedberg 95-of-4,295:** "UNIDENTIFIED ... none of my four measures gives 95 on 6/30 (A 622–912, B 492–2,214, C 8, D 456); not cited."

**Modifications vs late loans**
- Heading: "Modifications up, late loans down (GIBBS)".
- Body: "261 banks (6.1%) in Q3 vs 378 (8.8%) in Q2; system late loans +4.5%, performing modifications −2.4%."
- ⚠️ Reader cannot reconcile the heading with the body as written. The body shows late loans +4.5% and modifications −2.4%, which reads opposite to the heading. Check at REGINALD's report `reports/2026-11-17_Q3-universe-counts/REPORT.md`.

**FHLB panel:** SEC filers' Q3 and YTD median 0.0% (n 91, 97); concentrated, unchanged. The 11/16 Status line said "SEC-panel median −0.4% YTD", and that line is still in the Status header.

**REG-T-02 token renamed** to `WAL-PRICE-STRESS`, old name kept as an alias; "no level or consequence change".

**Vendor guidance (D:L798) CORRECTS 11/16:** both comment periods (OP-1881, OP-1880) were extended to Wed 12/16 on Fri 11/13. Of 67 Fed and 24 FDIC letters, three banks describe core-provider dependence; none names a vendor or a figure. "AI appears zero times in both proposals." A new WATCH row was added: comment close Wed 12/16, read from Thu 12/17.

**FLG:** CEO Otting bought 47,324 sh at $10.49 on 11/10 (Form 4 acc 0001323101-26-000007); "not a matrix input".

**Settled 11/16:** WAL $73.46, exit 0-of-3 (54 rows); KRE $72.19; FLG $10.40, 28 closes below RED. Claims 200K [w/e 11/07]; NFCI −0.462 [11/06].

The 11/16 evening and 11/16 wake entries were already present at 3db8291eff and are unchanged:
- CRE exposure: 175 of 889 (19.7%) at or above 300%.
- REG-T-06 REVIEW at $798.428B.
- United Fidelity.
- Reserves: 407 of 4,260 (9.6%).

Rotation: the 11/01–11/05 entries were rotated verbatim to `archive/NEXUS_BRIEF_rotation_2026-11-17.md` BLOCK N2, crc32 `3717bcf1`. These include the 11/05 selloff tape, the KRE redemption base rate, the 11/02 to 11/03 tapes, and the VLY/EGBN/HBAN Call Report reads.

"No score, threshold, gate or trade change."

**CROSS-DOMAIN / CALIBRATION:**
- Routing named in the entries:
  - Bond losses: BOND, LIQUID, TERRY, GIBBS.
  - Friedberg: PROME, WALTER.
  - Modifications: GIBBS.
  - FHLB panel: LIQUID, BOND.
  - Vendor guidance: GIBBS, CYPHER, PROME.
  - FLG: FLG, TERRY.
  - CRE exposure: CREED, GIBBS, TERRY, CATO.
  - MHFIN: CREED.
  - Older entries also name EGBN tree "RED owns the tree", "LIQUID owns contagion" (Ueno, now rotated) and "12/9 FOMC priced +25 85.5 ... (ORACLE KB-ORC-133, 11/11)".
- Uncertain about:
  - "(1) whether the bank-equity leg is now running AHEAD of credit (HY half-retraced while KRE/FLG/OZK kept falling)"
  - "(2) whether CFG's +$3.85B Q2 FHLB draw is brokered substitution (INFERENCE) or funding pressure"
  - "(5) whether the latest partial borrowing reversal persists".
- The CRE exposure count carries this caveat: "Exposure, not distress".

**FORWARD:**
- Next decision point text: "FDIC 9/30 population counts (~mid/late Nov, ESTIMATE) and Q3 QBP (~11/25) test the 11/07 BROADER". ⚠️ This was not updated even though the 11/17 midday entry ran full-universe counts on the FFIEC bulk 9/30 file.
- United Fidelity capital plan due Mon 12/14.
- Vendor-guidance comment close Wed 12/16; full file read from Thu 12/17.
- PFBC test at the 12/31 Call Report.
- OZK Boston land $105.9M, Dec-2026 maturity.
- Fresh ranking frozen ~mid-Jan 2027.
- Brief size re-check on 2026-11-20.

**NEXUS-NAMED:** none, apart from the archive file names `archive/NEXUS_BRIEF_rotation_2026-11-17.md`, `archive/NEXUS_BRIEF_rotation_2026-11-06.md` and `archive/2026-10-20_organisation-cleanup_NEXUS_BRIEF.md`.

---

## CROSS-BRIEF

1. **HY OAS: the briefs disagree on vintage.**
   - 334bp [11/16] in HENRY (FRED 11/16), VIOLET ([11/16]) and LIQUID ([November 16, first-published]).
   - BROCK's header and REGINALD's Status line still carry 323 [11/13] in briefs dated 11/17.
   - BB 196 (+10) and CCC 1,310 (−6) agree between HENRY and LIQUID.
2. **The FRED 11/17 HY cell (posts about 10:10 to 10:50 ET 11/18) is graded by three desks against three different lines.**
   - LIQUID: the >320 run is MET if above 320.0.
   - VIOLET: the +30% row's credit leg needs ≤ 355bp; the WATCH reopens only if ≥ 368.
   - LIQUID: the first cell that can show Cable One (1 to 2 bp of CCC at most).
3. **VIX curve on the 11/17 print.** HENRY and VIOLET agree: VIX settle 25.46 and VIX3M 24.98.
   - HENRY frames the inversion with VIX9D 26.70 over VIX3M.
   - VIOLET frames it as VIX over VIX3M, ratio 0.9811.
   - Same data, different leg.
4. **Nvidia after hours (not closes).** These are not contradictory, but they differ in precision.
   - HENRY: NVDA $158.50 (+1.96%), ES +0.22%.
   - VIOLET: "NVDA up 2% to 4%", ES +0.3%.
   - Both say the gross-margin guide is 71–72% and there is no China data-center compute. Both defer the meaning to VULCAN.
5. **Cable One: the two desks read the cash differently.**
   - LIQUID: "about $675M cash and a planned new financing, so a financing constraint is NOT SHOWN".
   - BROCK: "Its ~$675M cash at 9/30 is borrowed ... issuer says sources are insufficient for the 2027–28 maturities", and default if unpaid by ~12/16.
   - Same figure, different emphasis. BROCK owns the credit.
6. **10-year level: disagreement flagged; reader could not resolve it.**
   - REGINALD: "10Y 4.44 → 5.29" (no date, Q3 context).
   - LIQUID: "The 10-year itself is at its highest since July 2007 (5.10% [November 12]; 5.15% par [November 13])".
   - HENRY: 10Y par 5.10% [11/17], "the fourth close over 5.0".
   - BROCK: 10Y 5.10 [Treasury 11/12].
   - If 5.29 was a Q3 10-year level, it conflicts with LIQUID's "highest since July 2007" claim. The basis of 5.29 is not stated in REGINALD's brief. Check the owner reports.
7. **KRE agrees across desks.** $72.19 [11/16] in REGINALD and in HENRY's prior fold. HENRY now has $70.85 [11/17].
8. **HY run counts, by name.**
   - LIQUID: WQ-444 >320 run 2 of 3.
   - REGINALD: REG-T-04 "run 0-of-3, peak 348".
   - These appear to be different instruments with different counts, carried on a stale 323 by REGINALD.
