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
