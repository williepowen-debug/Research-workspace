# TERRY — VIX-down session read, packet drain, owner grades (2026-11-27, D:L1278)

**Written:** 2026-11-27 from 12:33 EST (from `date`), TERRY, Claude Code, Claude Opus 5.5, laptop. Launch letter: PROME D:L1278 (12:32 ET). NYSE half session, closes 13:00 ET. **NO ORDER. $0. No new card. No card term, rule, size or X1 changed.**

## 1. VIX leg — NO BUILD, NO CARD (a changed lean, reasons below)

**Live read, vendor (yfinance via `chain_fetch.py --no-cache --legs 30,40`, 12:33–12:34 EST, not a close):**

| Item | Value | Basis |
|---|---|---|
| VIX spot | 24.91 | vendor 12:33; Cboe History close 11/25 = 28.29 (VIOLET) ⇒ about −12% from the last real close. `snapshot.py`'s −7.13% is against the 11/26 holiday bar; not used |
| Dec-16 30C | 1.10 / 1.15, OI 210,626 | vendor 12:33 |
| Dec-16 40C | 0.53 / 0.58, OI 135,520 | vendor 12:33 |
| 30/40C spread | **mid $0.57, outer $0.62** | legs gate: both two-sided, exit 0 |
| Same spread before | outer $0.89 [11/24 after hours] · $1.40 [11/25 morning] · $1.03 [11/25 13:21] | my 11/24 and 11/25 notes |
| December VIX future (put-call parity at the 24 and 24.5 strikes) | about **23.3** | 24C 2.15 / 24P 2.83; 24.5C 2.00 / 24.5P 3.15 (mids). Settled 25.0258 [11/25] (VIOLET). Futures quote itself not readable here |
| HY OAS | 372 bp [11/24]; 11/25 cell **UNPOSTED** | FRED CSV 12:34 EST (last rows 352 [11/19], 376 [11/20], 363 [11/23], 372 [11/24]) |
| Tape | SPY 727.09 +1.45%, RSP 218.13 +1.11%, HYG 76.60 +0.10% | vendor 12:34; equity GREEN day |

**Terms if it were built** (reference only, not a card): Dec-16 30/40C ×5 at the outer $0.62 = $310 + $6.50 fees = **$316.50 max loss**; max value (10 − 0.62) × 500 = $4,690; breakeven **about 30.62 on the 12/16 settlement** (special opening quotation), **+31% above the ~23.3 December future**.

**Root rule #6 (calls on red days):** today is green, and the direct measurement says the spread is **30% cheaper than the 11/24 reference** ($0.62 vs $0.89). Under `RISK_RULES.md` § Breaking root rule #6 that is a legitimate break on cost. Cost is not the problem.

**Why not, anyway:**
1. **Construction rule #15 binds.** My 11/25 condition ("wait for a VIX-down session") was a gate that opens on vol decay. It opened today, and by rule #15 it carries **zero** thesis information. I wrote that gate; I am flagging it as a decay-keyed gate rather than letting it feel like confirmation.
2. **Every thesis read since 11/25 points the other way.** VIX 28.29 → ~24.9; the December future 25.03 [11/25 settle] → ~23.3 (parity); VIOLET's fade view 75% → **78%** (VIX close ≤ 25.00 by 12/10; a 0-of-4 near-match base); HYG flat, RSP up, the only credit read a single 372 cell [11/24] with 11/25 still unposted. The spread is cheaper because the thing it pays on got less likely.
3. **No evidence the market misprices it.** $0.57 mid on a $10 width implies a payout weight of about 6%; I have no read that the 12/16 settlement > 30.6 is more likely than that. Unscored view: about 8%, inside the noise.
4. **It is not additive.** It pays on the same credit-second-leg branch as the approved HYG ×5 (fill UNKNOWN, window to 12/4): one view, not two.
5. **Mechanics.** 22 minutes of a half session; no approval and order fit, and my 11/25 note already said no build on 11/27.

**What would make it a card (to Will, root rule #5), window to 12/04:** a credit tell, not a vol-decay tell: a first-published HY cell ≥ 376 (the 11/20 high) with CCC leading, or HENRY's broadening tells (HY > 376 on an RSP-down day, KRE < $65, HYG < ~$75.50; KRE 70.32, HYG 76.60 at 12:35); **and** the spread at or under its 11/24 reference outer $0.89 on that day. **Will's choice, not mine to rule:** if the HYG ×5 hedge is NOT filled, this spread ($316.50) is a near-equal-cost alternative expression of the same branch; it is a substitute, not an add.

VIOLET's 2' (VIX above 25 each close 11/27 to 12/10): a close at or under 25.00 today fails it on day one. Vendor 24.91 at 12:33 is not a close; VIOLET grades at Cboe History.

## 2. Packets — tradeability reads

| # | Packet | TERRY answer | Reason | Changes on |
|---|---|---|---|---|
| 1 | BRENT 11/26 22:46, Jazan refinery hit | **NO CARD** | Energy arm RETIRED (Will 8/7), WQ-192 stand-down, BG-02 NOT MET. BRENT's own read: product-side, plant probably already out since 7/27, Brent−WTI did not widen; "would not build on it alone". Today: vendor BZ=F 90.06 −4.81% (contract UNKNOWN, construction rule #22: not gradeable), CLF27 82.72 −1.15%, HOF27 3.6713 −0.84% (vendor ~10 min behind, 12:37) | A hit at Yanbu, Rabigh or Jeddah's terminal or an Aramco force majeure (BRENT BRT-32 ~25% to 12/31), **and** Will reopening the energy arm |
| 2 | FALCON 11/26, Jazan refinery | **NO CARD** (joint with 1) | No FALCON gate or rung fires; marks B 1 / C 14 / D 85; crude tail stays a Yanbu hit (3% / 10%) | Same as 1 |
| 3 | OSPREY 11/27, Russian runs 2.6–2.7 M bpd | **NO CARD** | Mechanism favours distillate cracks, not crude; the figure is a single-date relay of a paywalled estimate (B3); OSPREY's tanker channel killed today; the desk's last crack card (TRY-BRENT-REFINER/VLO) graded MIXED, crack under the $90.16 dead line since 11/2; a crack expression is BRENT's to price on named contracts (construction rule #22) | The EA/Kpler November monthly print confirming runs < 3.5 M bpd **and** BRENT pricing a named-contract diesel crack back above $95 with a direction; a mutual energy moratorium kills it (OSPREY ~15%) |
| 4 | BROCK 11/26, apartment-loss holders (copy) | **NO CARD** | The listed carriers have already fallen: ABR $1.21 −4.37% (vendor 12:35), −63.9% 10/06 → 11/25 per BROCK; a put on a $1.21 stock after a 64% fall is a chase with no liquid strike structure; FBRT flat says lender-specific, not a class trade | Arbor's 12/31 non-performing balance and loss-sharing allowance rising in the Feb–Mar 10-K, with a named-bank or BDC first loss (would open a class trade) |
| 5 | VIOLET 11/27 10:04, 2' armed on History | **NO CARD either side** | Confirmation only; folded into §1. Fade (short vol) is priced: the December future already sits under spot | VIOLET's lasting tells (close ≥ 31 with HY ≥ 370; VIX6M > 30) for the long side |
| 6 | WAL 11/26, postmortem thesis grades | **Recorded** (`POSTMORTEMS.md`, owner-grade table) | TRY-WAL-ROLL70 WRONG for its window; WAL Sep-18 70P + 67.5P WRONG for its window | — |
| 7 | PROME 11/26, WQ-735 recipe | **Applied** | `GATE-TERRY-007_GRADING_PROCEDURE.md` line 25 now uses `research-bot/1.0`; tested 12:37 EST, FRED DGS10 returned real rows (4.91 [11/24]). Instrument, count rule and caveats untouched | — |
| — | Launch item 5 (tariff proposals; Bessent's Nvidia deadline) | **Context only, no card** | UNVERIFIED secondary; HENRY and VULCAN own them | — |

## 3. Counts from my ledgers

- **Owner thesis grades (`POSTMORTEMS.md` § 2026-11-21 table):** with WAL recorded, the table holds grades from **13 distinct owner desks** (counted by command: BOND, BRENT, BROCK, DEWEY, FALCON, HENRY, LABOR, LIQUID, RED, REGINALD, VIOLET, VULCAN, WAL). On STATUS's running basis (11 of 12 [11/26], owed WAL and PROME ORCL), WAL makes it **12 of 12**; **PROME's ORCL grade is still owed**. ⚠️ The "of 12" denominator does not reconcile with the 13 desks in the table (LABOR's 11/26 grade appears to sit outside it); I report both rather than pick one.
- **TRY-FIRE-006 (Kharg strand):** three owner rows (BRENT UNRESOLVED, FALCON RIGHT on its leg, RED MIXED); unchanged today.
- **SETUPS.tsv:** 71.0% of the read cap at boot, under the 75% line; no rotation owed; one row added (`TRY-NOTRADE-DRAIN-NOV27`).
- **CRWV (WQ-745, approved NOT-FIRED):** $43.57 +2.35% (vendor 12:35), green but under the $48.00 trigger; no entry on 11/27 per the card; any entry from 11/30 needs a fresh LIQUID 5Y read (WILL_QUEUE row 745 window to 12/11).
- **BOARD scan run, 0 new since SIG-W-20261125-041, 0 logged.** Corrections check rc 0.

## 4. Addendum 12:39 EST — the 11/25 HY cell posted (377), re-pulled; answer unchanged

PROME (cross-session, 12:38 ET): the 11/25 cell posted at 12:37 ET = 377, a new high above 376 [11/20]. **Re-pulled by TERRY 12:39 EST:** FRED BAMLH0A0HYM2 first-published 363 [11/23] · 372 [11/24] · **377 [11/25]**. The first CSV URL served a cached copy ending 11/24; a URL with a different start date returned 11/25 (the request, not the series, was stale). BAMLH0A3HYC (CCC) 1405 → **1417** (+12); BAMLH0A1HYBB (BB) 225 → **228** (+3); CCC/BB ratio **6.244 → 6.215 (fell)**. Daily closes (vendor, venv yfinance): RSP 213.96 [11/24] → **215.74 [11/25] (+0.83%)**; HYG 76.43 → 76.52; SPY 718.78 → 716.70; VIX 26.36 → 28.29.

**Grading the tell §1 wrote before this cell arrived** ("a first-published HY cell ≥ 376 with CCC leading, or HY > 376 on an RSP-down day"): the level is MET (377); CCC leading is NOT MET on the proportion convention DEWEY and BROCK use (ratio fell; CCC did widen more in bp, +12 vs +3); RSP-down is NOT MET (RSP closed up). **Half met: the headline fired and its composition did not confirm it.** It removes "credit flat" from reason 2. It does not answer construction rule #15 or VIOLET's 78%. **Still NO BUILD, NO CARD today.**

Spread re-pulled 12:39 EST: 30C 1.06/1.12, 40C 0.52/0.55 ⇒ mid $0.54, **outer $0.60** (−33% vs $0.89 [11/24]); VIX 24.48. ×5 at $0.60 = **$306.50** max loss.

**Card goes to Will (root rule #5), window 11/30 to 12/04, if:** a later first-published cell holds ≥ 376 with the CCC/BB ratio rising, or widens past 376 on an RSP-down close; **and** the outer is ≤ $0.65 on the build day. It substitutes for HYG ×5 on the same branch; it is not an add.

**Other effects of the 377 cell:** QQQ 640/650 study cell (IDEA-QQQ-CAPIT-NOV20, DECLINED, $0): third first-published HY cell > 350 (363, 372, 377), so its invalidation fires; study only. HYG ×5 hedge: void clock (5 closes ≤ 330) stays **0 of 5**. Answer sent to PROME by SendMessage 12:40 EST.

## 5. Addendum 12:4x EST — PROME's ORCL grade; owner-grade denominator reconciled

PROME's ELLISON grade for IDEA-ORCL-PUTSPREAD-OCT23 (packet 12:43 ET, commit 17a9dcc118): **MIXED** (direction right, ORCL −19.8% 10/23→11/20; credit-led mechanism not confirmed, DTCC 5Y reads on file 293–305 and none after 11/12). Recorded in `POSTMORTEMS.md`. **Denominator, from the 11/20 ask packets on disk** (`AGENTS/*/inbox/processed/2026-11-20_from-TERRY_postmortem-thesis-grade-ask.md`): 12 desks asked (BOND, BRENT, BROCK, DEWEY, FALCON, HENRY, LIQUID, RED, REGINALD, VIOLET, VULCAN, WAL) plus PROME for ORCL = **13 asks, 13 of 13 answered, none owed**. LABOR's KELYA grade was unasked, so the table now holds 14 owners. The §3 "12 vs 13" is resolved: "of 12" counted asked desks and left PROME out; the 13 in the table counted LABOR in.

## 6. Afternoon drain (read 16:56–17:0x EST) — six packets, NO CARD each; one study figure closed

Closes (vendor, venv yfinance, 16:57 EST; half session ended 13:00 ET): VIX **23.81** (−15.8% vs 28.29 [11/25]); SPY 728.32, RSP 218.38, HYG 76.61, KRE 70.35, CRWV 44.15, GLD 334.40. VIX Dec-16 30C shows DEAD (0/0) after the close; the last two-sided read of the spread is outer $0.60 [12:39 EST]. **VIOLET's 2' (VIX above 25 each close 11/27–12/10): a 23.81 close fails it on day one on the vendor print; VIOLET grades it on Cboe History.**

| # | Packet | TERRY answer | Reason | Changes on |
|---|---|---|---|---|
| 1 | BRENT 13:0x, `BZ=F` roll artifact; January diesel crack $71.61 | **NO CARD** | Confirms §2: `BZ=F` is now February BZG27, so today's −4.6% to −4.8% mixes contracts (construction rule #22); named contracts −2.2% to −2.4%. Crack $23.39 under the $95 leg of my OSPREY condition; BRENT's odds of the January crack above $80 before 12/21 about 10% | As §2 row 3 |
| 2 | HENRY 13:2x, HY 2026 high; half-day rally without credit | **NO CARD** | HENRY's broadening marker did NOT fire (RSP up 11/25); he expects the 11/27 cell at 370–374 and gives the marker about 15% on the 11/30 cell. A credit-lags-equity gap with VIX back under 24 is the VIX leg's own case, and its §4 conditions are unchanged | §4 conditions; HENRY's: HY > 376 on an RSP-down day, KRE < $65, HYG < $75.50 |
| 3 | LIQUID 12:5x, BB widening broad; no CoreWeave 5Y since 11/24 | **NO NEW CARD** | Ex-technology BB +28.9 bp, 89% of bonds wider: the widening is broad, which supports the already-approved broad HYG ×5 hedge over an AI-only expression. It does not alter §4's composition test (CCC/BB ratio, RSP direction). **CRWV:** the latest valid 5Y is 1,314 clean [11/24]; on LIQUID's count it is 3 sessions old for an 11/30 entry, so **no CRWV entry Monday without a fresh 5Y print** (LIQUID reads the 11/27 full file, about 20:15 ET, only if re-spawned) | A first-published cell > 377 (LIQUID ~60% by 12/9); two cells with BB < 215 and CoreWeave 5Y > 1,300 the other way |
| 4 | MIDAS 13:1x, GLD three-month lean withdrawn to neutral | **NO CARD; recorded for Will's held line** | `MGMT-GLD-SHARES-OCT24` is a management-rails card for Will's 18 shares (C5 paused 10/20: reference only, no trim push). MIDAS's three-month "modestly higher" view, which the card cites, is withdrawn to NEUTRAL (trust tonnes 1,034.43 t < 1,035.70 t line on 11/20); 11/19–11/20 graded liquidation days; GLD rose and fell with stocks, not as a hedge. MIDAS-12 (sign call to 2027-01-20) untouched, so this is a weaker thesis, not a broken one (root rule #7). At $334.40 [11/27 close] against $373.93 average cost the line is about −$711 (−10.6%) on the $6,730.67 basis | A HAVEN day (stress, GLD up, tonnes up); two or more issuer inflow days; Will asking for a sell or roll card |
| 5 | REGINALD 12:47, REG-T-04 exit run 0; bank leg absent but softer | **NO CARD** | No bank-credit vehicle; KRE beat SPY across the two sessions | The preferred basket −2% over 3 sessions, or IG +10 bp led by financials, or WAL-PA falling while WAL common holds |
| 6 | VULCAN 13:20, concentration falling; Nvidia 10-Q not filed; CoreWeave $4.5B loan not launched | **NO CARD** | No concentration-unwind trigger (Mag-7 32.48%, RSP−SPY +4.95 pp). **CRWV card:** its do-not-trade/kill clause is "CoreWeave's roughly $4B IG loan launches and prices"; VULCAN's $4.5B Meta-backed loan (talk 7–7.5%) is probably that deal at a revised size; identity NOT VERIFIED | The loan pricing (kills the CRWV card if it is the same deal); Nvidia's 10-Q (deadline 12/04, or 12/09 with a 12b-25) |

**QQQ 640/650 study cell (caution review (a), `research/2026-11-26_caution-review/NOTE.md`; IDEA-QQQ-CAPIT-NOV20 DECLINED, $0, study only):** its HY > 350 ×3 invalidation fired on the 11/25 cell (363/372/377), readable 11/27. The exit at 11/27 regular-session quotes (vendor, last trades 13:11–13:12): 640C 26.09/26.36, 650C 20.10/20.34 ⇒ **$5.75 at the bid side, $6.01 mid**. At the card's $4.50 limit that is **about +$122 to +$148** after ~$2.60 fees, replacing the open "+$20 to +$65 at 11/25 quotes". On the caution review's "Will's declines" line the forgone gain on his QQQ decline is about $57 to $128 larger than that table showed; the table's other rows are unchanged. A model study on vendor quotes, not a fill.

**BOARD scan:** SIG-W-20261127-002 (action: LIQUID, YURI, BRENT, FALCON) and -003 (action: CORAL) do not name TERRY; nothing to log. Boot ID-diff clean.

## 7. WALTER SIG-W-20261127-008 (AI credit) and -007 (US data), read 17:13 EST — NO CARD

| Item | TERRY answer | Reason |
|---|---|---|
| Semafor 11/26: Citi and JPMorgan marketing AI loan portfolios, some via synthetic risk transfer (no amounts) | **NO CARD** | Fits the CRWV card's thesis precondition (lenders backing away from AI-infrastructure credit) but moves none of its triggers (green close ≥ $48.00, a fresh 5Y ≥ 1,200 bp). Synthetic risk transfer moves loss risk OFF the banks, so it is not a bank-equity put case (REGINALD: bank leg absent) |
| SoftBank 5Y CDS 542 (Bloomberg chart via zerohedge, not read at Bloomberg) vs 466 verified [11/6]; retail bond spread ~229 bp | **NO CARD** | Chart-only level; no liquid US-listed option vehicle; an AI-financing stress gauge that feeds the same branch as HYG 76P ×2 and the CRWV lines |
| CoreWeave "senior bonds worthless" (one anonymous account); DDTL 5.0 parent-guaranteed per a filing summary | **NO CARD** | Opinion, not evidence; no new CoreWeave 5Y print. Will's CRWV Dec-4 41P and the card both sit on this name already |
| -007: Census October goods deficit $149.5B (issuer), inventories up; 8th District loan demand net −30% | **NO CARD** | CARL/ISHM/REGINALD's; no TERRY vehicle |

Logged in `SIGNALS.tsv` COMBO-CREDIT-FOLLOWING (members and counterevidence) and `board_log.tsv` (008 noted). 007 not on TERRY's action line, read, not logged.

## 8. Evening packets (read 18:1x EST) — NO CARD each

| Packet | TERRY answer | Reason | Changes on |
|---|---|---|---|
| YURI 11/27, jet fuel export ban renewed to 3/31/2027 (Resolution №1586); Baltic and at-sea threats, no measures | **NO CARD** | The one hard act continues a ban in force since June: no new barrel lost (BRENT owns barrels); the rest is words. No vehicle on this desk | A named Russian measure against Estonia or Baltic shipping, or an executed retaliation named in a Russian text (YURI ~35% / ~20% by 12/31, unscored); then OSPREY and HAWK price the war-risk |
| OTTO 11/27, Car-Mart (CRMT) prepackaged Chapter 11 (8-K 0001171843-26-007671), Nasdaq suspension at the open 12/2 | **NO CARD** | The ABS notes are 144A with no listed proxy (OTTO); no CRMT line in Will's book; the equity is a post-petition stalking-horse sale with trading suspended from 12/2, so a short or put there is a lottery on a delisting with no defined exit; no bank exposure (revolver repaid 10/30/2025) | A servicer termination notice or a missed 12/3 rollover with no extension (OTTO), and a listed vehicle that carries the trusts' collections |

## 9. WALTER deep-dive cards -010 to -015 (read 18:2x EST): NO CARD; a correction to my forward read

- **Correction (PROME packet `2026-11-27_from-TERRY_forward-read-correction-ras-tanura.md`):** the Robinhood forward read's USO row left out the **Ras Tanura loading halt REPORTED 11/26** (CNN via Newsquawk 14:05Z; Aramco silent, no force majeure), Iranian statements that a blockade breakout is underway (no escorted sailing confirmed), CENTCOM disabling the Pacific Archer on 11/26, and SOMO cargo delays (single source). These are upside risks to USO that I had not weighed. The tape disagreed on 11/27 (named crude −2.2% to −2.4%, USO −1.52%). It matters if the stoppage is confirmed to last days (FALCON and BRENT).
- **CoreWeave 10-Q (EDGAR via WALTER):** six of seven DDTLs parent-guaranteed ($13.1B); DDTL 4.0 (Meta-linked, $4.58B) non-recourse; $11.0B principal due 2027; notes 73.9–79.2, yield to worst about 17% [11/25]. Direction unchanged; it moves no CRWV card trigger. **SoftBank USD 5Y CDS 516–535 [11/26]** (542 is the yen contract); S&P loan-to-value above 30% vs a 35% downgrade trigger.
- **NO CARD** on -010 to -015. Oil is Will's own line, and the energy arm stays retired; the credit facts feed the existing HYG and CRWV lines. Carrier count: WALTER's -010 "still three" conflicts with its -004 anchor "three to two"; flagged to WALTER.

## 10. FALCON on Ras Tanura (packet 18:33 ET, read 18:3x EST): NO CARD; USO read unchanged

FALCON grades the loading halt **STILL ONE REPORT** (one unnamed CNN shipping source, 11/26; no Aramco, ministry, force majeure or tracker confirmation to about 23:31Z 11/27). Its unscored odds to about 12/04: loading shown resumed 45%, stays one report 35%, **multi-day stoppage evidenced 15%**, force majeure 4%. Ras Tanura loaded about 2.95 mb/d (Oct 1–25, Kpler via Asharq). This fits my 18:2x correction as written: the stoppage is an upside tail for Will's USO Dec-4 139C, about one in seven on FALCON's view, and the 11/27 tape did not price it. No change to the read, NO CARD.

**Correction 2026-11-27 22:3x ET (Will asked "1 in 7 chance upside? That's super low no?"):** "about one in seven" counted only the 15% bucket. FALCON's four buckets are exclusive (45+35+15+4 = 99%) and force majeure is also a stoppage, so a stoppage shown by about 12/04 is **15% + 4% = 19%, about one in five.** It is the odds of one catalyst, not the call's win odds: USO closed $137.77 on 11/27 (−1.52%, vendor), and the 139C at $2.51 breaks even at expiry at $141.51, about 2.7% higher, reachable by other routes (OPEC+ 11/29, broad oil). The read and NO CARD stand.

## 11. Late drain at closeout (22:3x EST; packets 19:18–20:35 ET): NO CARD each

| Packet | Read | Disposition |
|---|---|---|
| BRENT 19:19, Ras Tanura and SOMO as conditionals; revised 11/27 settles (BZF27 95.44, CLF27 83.08, USO 137.77) | A halt that runs a week or more shows first and largest in Brent and Brent over WTI, least in WTI. Unscored cases: about 3 days Brent Feb +$0–2, fades; about 7 days WTI Feb +$1.5–3.5; 14–30 days WTI +$5–10. OPEC+ Sunday: January hold about 80% | **Refines my 22:3x answer to Will.** USO tracks front WTI, so on CLF27 83.08 a 7-day halt is roughly +1.8% to +4.2% against the +2.7% the 139C needs by 12/04 at expiry ($141.51 vs $137.77). That is roughly break-even, not "the big jump"; only a 14-day-plus halt is large for USO, and it would be barely evidenced by 12/04. OPEC+ at 80% hold is a weak route too. Read for the call: lower than I implied. NO CARD; no sell or roll language (C5 paused) |
| CORAL 19:18, St. Johns at DeLand 6.25 ft, forecast 6.6 ft 12/01–12/04 vs the 6.33 record | Losses fall on uninsured households and counties, not listed insurers or banks | Agree. NO CARD |
| CYPHER, SAP GitHub development-platform incident; SAP ADR $213.65 +2.04% (11/27) | Decided by which keys were exchanged; CYPHER unscored 70% no customer advisory by 12/08, 30% an out-of-band certificate note. Equity grade is HENRY or VULCAN's | NO CARD: no confirmed customer-artifact exposure, the stock rose, and the KB analogues (SolarWinds, Progress) were small vector vendors, so they do not size a move in SAP. A put before 12/08 would be a bet on CYPHER's 30% branch at an unknown size. Re-read if CYPHER packets an advisory |
| LIQUID 20:35, CoreWeave 5Y: no trade 11/26 or 11/27; latest valid 1,371 dirty / 1,326 clean, 11/24 16:07 ET ($2M); the 1,359 / 1,314 figure withdrawn (its $3M prints errored) | Leg (b) of `IDEA-CRWV-AIFIN-NOV24` grades on clean: 1,326 ≥ 1,200 on level, but 11/24 is 3 sessions before 11/30, over the card's 2-session limit | Card stays APPROVED NOT-FIRED. **No entry on 11/30 unless a new 5Y print dated 11/27 or later is in hand**, and leg (a) also needs a green close ≥ $48.00 (CRWV $44.15 on 11/27). Recorded on the card §8d |

BOARD scan at closeout: 0 new action-line signals to TERRY since SIG-W-20261125-041.
