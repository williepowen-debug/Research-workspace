# LIQUID — GATE-LIQ-076 review, November 19 credit cell, W2 and H.4.1, yen funding legs (2026-11-20)

**Session:** PROME prome-77 task letter 11:22:25 ET, G:GATE-LIQ-076 due-row wake (C6), launched late; laptop, Claude Code / Opus 5.5. Session start 11:22 ET (`date`). All figures below carry their observation date and basis. Raw pulls: `raw/` (NY Fed PD JSON + headers, `transmission_check_asof_1119.txt`, `boot_1122.txt`).

## 0. The whole story

The November 19 high-yield cell is **352 bp, first-published** (my FRED `output_type=4` pull 11:22:56 ET 11/20), the **first close strictly above 350**, the highest since 353 [May 9, 2025]. The widening has moved up the quality ladder: on the three-week clause BB, BBB and IG all now clear their lines (no longer borderline), and on the day B and BB led, not CCC. **Funding has not changed:** SOFR one basis point over the Fed's interest on reserves, the 99th percentile +8, standing repo $3M, reserves up $19B. The dealer data (W2, as-of 11/11) show dealers *less* short long-end IG, which is absorption, not a warehouse pulling back. **Gate 076 grades NOT MET, 1 of 3**, with no consequence possible. Japan: nothing on the H.4.1 of November 18 shows dollars being raised by selling or borrowing against Treasuries.

## 1. GATE-LIQ-076 grade at review (frozen letter: GATES.tsv row + `workbook/DEALER_POSITIONING_NEXUS_WATCH.md` leg-basis table)

Window: 14 calendar days, **November 7 → 20**. Graded 11:25 ET 11/20.

| Leg | Letter | Observation (date, basis) | Grade |
|---|---|---|---|
| **W1** CFTC TFF SOFR-3M (CME full name) lev-fund net | ≤ −2,950,000 contracts, or w/w cover > +300,000 | as-of **Tue 11/10**: −2,696,034 (254,034 short of the level; graded 11/16). As-of **Tue 11/17**: CFTC file publishes about 15:30 ET today, **UNMEASURED at grade** | **NOT MET** on the latest published print |
| **W2** NY Fed PD SBN2024 IG corporate | G10 < −12,000 $mm, or G5L10 < −800 on 2 consecutive as-of Wednesdays | as-of **Wed 11/11** (published Thu 11/19, first read by me 11:23:20 ET 11/20, API `markets.newyorkfed.org/api/pd/get/…json`): **G10 −7,007; G5L10 +937.** As-of 11/04 unrevised (−7,845; +477) | **NOT MET** (G10 4,993 short of the line; G5L10 positive) |
| **W3** MOVE > 85.00 while VIX < 20.00, same session | witness may grade only when both are >1.00 from their lines | Met in window on **11/12** (witness-certified); 11/9, 11/10, 11/13 are EDGE sessions (VIX within 1.00 of 20) that the 11/13 grade counted. **NOT MET 11/16–11/19**: VIX closes 22.91 / 25.46 / 24.56 / **28.44**, MOVE 101.28 / 101.88 / 98.15 / **96.04** (yfinance closes); 11/20 intraday VIX 30.32 at 11:23 ET | **MET in window** (last 11/13 or 11/12) |

**Grade: NOT MET, 1 of 3 (W3).** No write-up is owed and none could be: the October 22 episode has not reset. A W1 meet on the as-of-11/17 print would make the window 2 of 3 (W3 on 11/12 is within 14 days of 11/17) and still owe nothing.

**Reset clock (owner reading of the letter's reset rule, no letter change):** no leg has met on any date since **11/13**. Ten consecutive business days with no leg met: 11/16, 17, 18, 19, 20, 23, 24, 25, 27, 30. **Re-arm completes at the end of November 30** if W1 as-of 11/17 and 11/24, W2 as-of 11/18 and 11/25, and W3 on every session stay unmet. A W1 meet as-of 11/17 would restart the clock from 11/18 (re-arm about December 2). **Recommended next review_by: December 2** (unchanged from my 11/19 recommendation): first date when a new 2-of-3 could carry a consequence, and it catches W1 as-of 11/24 and W2 as-of 11/18 and 11/25.

**What W2 says beyond the grade:** dealers' long-end IG net short has shrunk from −10,307 [10/14] to −7,007 [11/11], and the 5–10 year bucket went from −1,850 [10/21] to +937. Dealers took bonds on, they did not refuse them. All of it predates the November 16–19 widening.

## 2. The November 19 HY cell as first published

FRED ICE family, `output_type=4`, realtime from 10/20, my pull 11:22:56 ET 11/20; first-published equals latest-revised on every series read (11/10 → 11/19).

| Series | 11/19 | d/d | 15-session (base 10/28) | Context |
|---|---|---|---|---|
| HY OAS | **352** | +5 (86.1 pct) | +38 (93.6 pct) | highest since 353 [2025-05-09]; 2026 prior high 348 [11/5] |
| CCC | **1,361** | +8 (84.0 pct) | +54 | **no higher observation in FRED's ICE window (history from 2023-11-21, rolling ~3 years; includes April 2025)** |
| B | 380 | +7 | **+62 (97.8 pct)** | highest since 383 [2025-05-07] |
| BB | 210 | +5 | +26 | 2026 high 222 [3/30]; 069 L1 line 220 is 10 away |
| BBB | 117 | +1 | +10 | — |
| IG | **94** | +1 | +8 | equals the 2026 high 94 [3/16]; GATE-LIQ-072 strict >94 **NOT MET, at the line** |
| HY − IG | **258** | +4 | — | new 2026 high (254 [11/18]) |
| CCC − B | 981 | +1 (57.5 pct) | −8 | the tail did **not** lead on 11/19 |
| B − BB | 170 | +2 | +36 (99.2 pct) | the middle of the ladder is where the move is |

**Counts:**
- **>320 sustained (WQ-444): MET and extending, 5 observations** — 323 [11/13], 334 [11/16], 343 [11/17], 347 [11/18], 352 [11/19]. Extensions are not re-routed.
- **REGINALD >350 ×3 (REG-T-04) witness: 1 of 3** (352 is 2 above). PROME's launch line "0 of 3 after 347" was written Thursday and is superseded. The 11/20 cell publishes about Monday 11/23 morning (KB-LIQ-151); the earliest completion is the **11/23 cell, about the morning of 11/24**. REGINALD grades; its projection row is REG-37 (WALTER correction 020).
- **GATE-HY-REKILL: NOT FIRED, 0 of 2,** 92 above 260.
- **Tier rule (9/25 §1c): BROADENS on the 15-session clause, clearly:** IG +8 ≥ +6, BBB +10 ≥ +7, BB +26 ≥ +19, all three over (11/18 was borderline with BBB alone at its line). Daily clause fails (IG +1, BBB +1 < +2; BB +5 < +9). Fourth BROADENS in a row. Tiers are not issuer-count breadth.
- **GATE-LIQ-069 (not under review; review 11/25):** L1 NOT FIRED (BB 210; CCC 5-session +47 vs 11/12, not flat). L4 NOT FIRED on the 11/19 session: HY +5 meets the credit half; worst cohort close NBIS −9.39% (CRWV −6.10%, IREN −5.45%, APLD −3.25%). **Watch, 11/20 intraday 11:24 ET: APLD −14.99%, IREN −11.94%, NBIS −10.32%, CRWV −9.43% (vendor, not closes).** L4 on 11/20 needs a close at or below −15% AND the 11/20 HY cell +5 or more (≥ 357). 069 is already 2 of 2 FIRED (L2 + L5); a third leg adds no consequence.
- X1: strict >280 ×3 price half MET; X1 **CLOSED / DON'T-SIZE unchanged** (BROCK owns the relative half; my letter changes nothing).

## 3. Funding: has anything changed since my 11/19 read? (for PROME's HEARTBEAT sentence)

**No. "A financing constraint is NOT SHOWN" stands.** Same-date to IORB 3.90, FRED, November 19: SOFR −IORB **+1**, SOFR75 +5, **SOFR99 +8** (079 arm line +30), TGCR −2; standing repo **$0.003B**; RRP $0.41B. H.4.1 Wednesday 11/18: reserves **$2,979.7B (+$19.1B)**, TGA $916.6B (+$2.2B). Dealers absorbed IG through 11/11 (§1). Primary markets were open in the week: Pinnacle Bank $600M 7.2% Tier 2 at par on 11/18 (REGINALD, EDGAR); Anthropic's $81B IPO on 11/19. **Limits that would hide a constraint:** the November 20 sell-off is in no funding print yet (SOFR for 11/20 publishes Monday about 08:00 ET); haircuts, sponsored repo and prime-brokerage margin are unmeasured; the dealer data predate the 11/16–11/19 widening; private and offshore channels are outside what repo shows.

## 4. Yen: H.4.1 of Wednesday November 18 against "how would Japan fund an intervention" (open with SAM and BOND)

FRED, released Thu 11/19 (FRED updated 16:32 ET), against the 11/11 baseline:

| Leg (owner) | 11/11 | 11/18 | Change | Reading |
|---|---|---|---|---|
| FIMA repo, Wednesday (`H41RESPPALGTRFNWW`, LIQUID) | $0 | **$1M** | +$1M | first non-zero since before 10/21; far too small to be funding; cause not established (small-value operations exist; not checked) |
| Foreign official reverse repo pool, Wednesday (`WLRRAFOIAL`, LIQUID) | $336.1B | **$316.7B** | **−$19.4B** | the only leg moving in the "drawing dollars" direction |
| Same pool, week average (`WREPOFOR`, LIQUID) | $336.4B | $324.1B | −$12.2B | same sign on both bases this week |
| Custody marketable Treasuries, Wednesday (`WMTSECL1`, BOND's leg, context only) | $2,524.2B | **$2,544.0B** | **+$19.8B** | rose, the opposite of selling |

**Reading:** nothing here shows Treasuries sold or borrowed against. The pool fell about as much as custody Treasuries rose, which **fits** official accounts moving cash from the Fed into Treasuries (my inference, not established). None of it is attributable to Japan: both pools hold every official account. USD/JPY 159.38 [11/19] and 158.73 [11/20 intraday, vendor]; no intervention is confirmed since the 160.04 touch on 11/12. **The question stays OPEN.** Confirmation sources: the Ministry of Finance's monthly intervention total (about 11/30) and Japan's December reserves release; TIC November in mid-January. SAM owns the yen call; BOND owns custody and the auction side.

## 5. Trade relevance (sent to TERRY in WQ-696 form) and PROJECTION

**Evidence implies:** a repricing of credit risk that is spreading from the tail into BB, BBB and IG, alongside an equity sell-off (S&P 7,175.83 [11/19 close], 7,081 intraday 11/20; VIX 28.44 close, about 30 intraday), with funding untouched. It is a price-of-risk move, not a financing squeeze. **Horizon:** days to about three weeks (into the December 8–9 FOMC and the year-end turn). **Invalidates it:** HY back to 320.0 or below (resets the run); REG-T-04 failing on the 11/20 cell. **Would upgrade it to a funding story:** SOFR99 −IORB at or above +30 on two consecutive non-calendar days (079), standing repo above $50B, a pulled or failed HY deal, dealers' G10 back toward −12,000. **Unknown:** whether AI-infra equity losses reach HY new-issue access (069 L3 has no instrument); haircuts and margin.

**PROJECTION (my judgment, separate from the evidence above; moves no score, gate or trade):**
- 11/20 HY cell above 350: **about 85%** (S&P −1.3%, VIX ≈30, AI-infra −10 to −15% intraday). REG-T-04 completing on the 11/23 cell: **about 55%** (a Monday bounce is the alternative). Unscored; REGINALD's REG-37 is the graded row for that question.
- HY at or above 400 on any first-published observation through 12/30: **about 17%** now, against my registered LIQ-08 at 10% (registration frozen; this is an unscored update).
- HY at or below 320 on the 12/30 cell: **about 25%** now, against my registered contrarian LIQ-09 at 38% (frozen; unscored update).
- Funding arming before the year-end turn stays unlikely (registered LIQ-10 at 5%; no change in my view).
- **Meaningful alternative:** the sell-off is AI-trade profit-taking around the Anthropic listing; equities stabilise and HY drifts back to 330–340 inside two weeks (about 30%). **What changes my mind:** a funding print in §3's upgrade list, or a third consecutive session of B and BB leading with CCC flat (that would be a broad repricing, not tail stress).

## 6. Inbox (whole-inbox drain: 1 top-level, 5 WALTER)

| Item | Disposition |
|---|---|
| ISHM 11/19 Class 8 October final (13,755, −44% y/y; ACT attributes to EPA 2027) | noted: no credit read changes; current widening is not freight-led; base rate stays ISHM's. `inbox/processed/` |
| SIG-W-20261119-005 small items | noted: ECB bank and private-credit probe → KB-LIQ-154; Paraguay $1B loss → KB-LIQ-157; Nvidia pledge (VULCAN: not established) and Anthropic $81B → KB-LIQ-153 |
| SIG-W-20261119-009 CYPHER grades | info-only: Bank SinoPac $1.3M vendor-route transfers, reimbursed; no payment-system or funding consequence |
| SIG-W-20261119-017 midday reversal | noted: HYG −0.05% while S&P −1.61% (vendor 17:14Z); read with correction 020 |
| SIG-W-20261119-018 HY 347 / REG-T-04 | info-only: my own 11/18 grade; superseded by the 11/19 cell (§2) |
| SIG-W-20261119-020 correction | info-only; correction COR-20261119-20 receipted NO-OP (I carried none of the corrected claims) |

Combination rows appended: KB-LIQ-153, -154, -156, -157 (logging moves no score, gate or band).
