# TERRY — tradeability reads, Fri 2026-11-13 (part one, intraday)

**Written:** 2026-11-13 10:30 EST from `date` · TERRY, Claude Code, Claude Opus 5.5 · PROME assignment prome-72 (due-row wake, WQ-184 / WQ-667 B; task words PROME's).
**Data:** vendor quotes via `fetch.py` / `snapshot.py` 10:27–10:29 ET; chains via `chain_fetch.py --no-cache` 10:28–10:29 ET. Vendor option marks are SCREENING marks (durable finding 5b); a fill is priced on the broker. FRED HY OAS CSV pulled 10:28 ET.
**$0 moved. No order. No level, band or threshold set.** Defaults on every line: $500 per card, X1 CLOSED / DON'T-SIZE (LIQUID), Will decides every card (root rule #5).

## Tape at the read (10:27–10:29 ET, vendor)

| Item | Figure |
|---|---|
| S&P 500 | 7,506.42 −1.13% (10:27) · 7,517.92 (10:29) · HENRY's low print 7,499.40 at 10:21–10:22 |
| SPY / QQQ / RSP | 748.55 −1.13% · 673.11 −2.19% · 219.71 −0.46% |
| SMH / NVDA | 477.87 −4.76% · 159.71 −3.90% (30-day range low 159.67) |
| VIX / VIX3M | 20.35 +8.82% / 21.11 +5.23% ⇒ **VIX3M/VIX 1.037** (10:28) |
| 10Y (^TNX) / TLT | 5.13 / 79.48 −0.30% |
| HYG / JNK | 76.96 −0.02% / 92.36 −0.07% |
| USD/JPY / FXY | 159.81 −0.03% / 57.35 +0.15% |
| HY OAS first-published (FRED) | 334 [11/9] · no 11/10 cell · 330 [11/11] · **320 [11/12]** |
| Realized vol (close-to-close, excl. today, 502 bars) | SPX 20-day 22.2%, 10-day 30.2% · QQQ 20-day 36.2%, 10-day 46.3% |
| 200-day (200 of 200 bars, excl. today) | QQQ 680.94 · SPX 7,337.35 |

## 1. HENRY — post-PPI, S&P at the 7,500 put wall in negative gamma → **NO CARD (new)**; existing card `IDEA-QQQ-200D-NOV05` **T1 MET, entry fails its debit limit**

**Existing card first, because it is the book's built answer to exactly this tape.** `IDEA-QQQ-200D-NOV05` (QQQ Dec-18 670/680C ×1 ≤ $4.90, WQ-617 C: NOT approved, decide at a fire, window to 11/20):

| Leg | Line | State 10:28 ET | Status |
|---|---|---|---|
| T1 | VIX3M/VIX ≥ 1.00 live, red QQQ session | 21.11 / 20.35 = **1.037**; QQQ −2.08% | **MET** |
| Credit | HY OAS first-published ≤ 344 at entry | 320 [11/12] | met |
| Debit | broker complex debit ≤ $4.90 | vendor 670C 26.55/26.79 · 680C 20.48/20.61 ⇒ outer **$6.31**, mid $6.12 | **FAILS** (+$1.41) |

Card §4: "Above $4.90 no order. If missed: new card." ⇒ **no order.** The card's §8 named this exact case (curve normalises after QQQ already bounced; debit above the limit).
**No new card at a re-strike:** QQQ 674.40 is 0.96% under its 200-day (680.94); the card was built at 651.85 to capture the move back to it, and most of that move is spent. At $6.31 the 670/680 pays $369 against $631 + fees (0.58:1, over the $500 default). A higher strike (680/690C, outer $4.99 = 680C ask 20.61 − 690C bid 15.62) bets on QQQ going *through* the 200-day, a different view with no owner and no measured expectancy (the 11/5 note found none). Window stays open on the card's own terms through 11/20: a red QQQ session with the ratio ≥ 1.00 and broker debit ≤ $4.90 is a fire to bring to Will.

**New card on HENRY's map: NO CARD.**
- **Direction is unowned.** HENRY's map gave no direction for an in-line print; his read names two drivers (long yields up on a soft print, chips) and two exits (close back over ~7,632 flips the regime; below 7,500 amplification to about 7,350–7,450 on an older chain). He sizes no move. A morning print at the wall is not a close.
- **Downside (SPY puts) on a red day breaks root rule #6 without the refuting measurement.** VIX +8.8%. SPY Nov-20 745/735P screens $2.13–2.19 (745P 5.38/5.42, 735P 3.23/3.25) for a 1.3–2% further fall with no owner calling it. The book already holds a built downside expression (the HYG ×5 hedge, item 2).
- **Vol (straddle) is not cheap enough to override:** SPY Nov-20 750 straddle $15.19 (750P 7.17 mid + 750C 8.02 mid) = 2.03% of spot ≈ 18% annualized over 5 sessions incl. NVIDIA's print; SPX realized 22.2% (20-day) / 30.2% (10-day, contains the 11/5 −5.8% QQQ day). A modest discount on one window, not a measured edge; and ×1 costs $1,519, three times the default.
- Re-open: HENRY publishes a sized move or direction (e.g. after a close under 7,500 is confirmed), or QQQ's card fires inside its limit (above).

## 2. LIQUID — HY 320 [11/12] resets the >320 run → **NO CARD; two approved HYG cards re-read**

| Card | Effect of 320 [11/12] | State |
|---|---|---|
| `IDEA-CREDIT-HYG-BDC-OCT23` (×4, WQ-513 A, REG-T-04 >350 ×3) | further from 350 | cannot fire; lapses at today's close by its own terms (part two, D:L830) |
| `IDEA-HYG-FOLLOW-NOV05` (×5 76/73P, APPROVED FIRED, unfilled as far as the desk knows) | **void clock: HY ≤ 330 on 5 consecutive closes before entry** | **2 of 5** on consecutive published cells (330 [11/11], 320 [11/12]; 334 [11/9] breaks it; no 11/10 cell published, counted as no break). Three more cells ≤ 330 (11/13, 11/16, 11/17, published the following mornings) void it before entry. |

- **HYG ×5 entry screen 10:28 ET (vendor):** 76P 0.50/0.62 · 73P 0.14/0.21 ⇒ outer **$0.48**, inside the card's $0.60 limit. Max loss at $0.48 ×5 = $240 + fees (card max $306.50 at the limit). Broker price governs. Order is Will's hand; the desk books a fill only from his word.
- The >320 run is LIQUID's confirmation leg; neither HYG card's own trigger uses it (the ×5 card's T1(a) was HY > 344, fired on 348 [11/5]). No card condition moved.
- CCC wider (+3 to 1,314) while HY tighter (−14) and yields up (+16 to 8.16%) is the decompression combination already logged under `combo:` credit; logged, not scored.

## 3. BROCK — Car-Mart 12th bridge to Mon 11/16; Cable One hearing unreconciled → **NO CARD**

- **CRMT $0.93:** no listed options on the vendor feed (0 expiries). A short at $0.93 has no defined loss without a borrow and a stop, and borrow is unknown. Two-business-day bridges make the timing a coin flip by design.
- **CABO $2.77–2.80 (−75% over 30 days):** no listed options on the vendor feed (0 expiries). The outcome is binary between a lender-led path and a GTCR rescue (runway "through at least 2029", no terms published); either can gap the stock 50%+. The hearing date is a known-unknown that gates any timing (company 10-Q said 11/13; press says adjourned to 12/4 and an order dated "October 19"; docket unread). No defined-loss structure exists on a feed we can see.
- Re-open: a CABO chain at Will's broker plus a reconciled hearing date; or CRMT Item 1.03 / sale agreement (BRK-33 resolves).

## 4. CYPHER — N-able, Check Point, GMO Internet → **NO CARD**

- **NABL $4.76:** Dec-18 has one put strike (5P 0.15/0.85, OI 1, last trade 10/20) — DEAD. Shares unmoved through four emergencies (4.81 → 4.76, 11/9–11/13). Prior read `TRY-NOTRADE-NABL-NOV12` stands.
- **CHKP $146.00:** no reaction to its own disclosure (147.49 +0.6% on 11/12; −1.0% today against HACK −2.4%). KB-CYP-003's vendor cases had named customer damage; here victims are unnamed and the vendor self-disclosed. Buying puts after a non-reaction chases nothing; HENRY grades the wave's equity row (PANW vs HACK) 11/18.
- **GMO Internet 4784.T:** Tokyo listing; access at Will's broker unknown; the ¥3.05B cost is published, the forecast unrevised. No structure.
- Re-open: a named CHKP customer loss or guidance change; an N-able 8-K Item 1.05.

## 5. SAM (carried 11/12) — USD/JPY touched 160, no close → **NO CARD, agree with SAM**

USD/JPY 159.81, FXY 57.35 +0.15% (a call on a green day breaks root rule #6). Katayama's words are REPORTED only; no rate check or intervention ESTABLISHED. The only built expression, `IDEA-FXY-OCT20`, is SHELVED (revival Will's word only). Prior read `TRY-NOTRADE-USDJPY160-NOV12` stands.

## 6. BROCK (carried 11/12) — Trinity Capital AI-infrastructure concentration → **NO CARD**

TRIN $17.60 (near its 30-day high 18.03). BROCK frames it as concentration, not stress: no mark below par, no non-accrual. The catalyst (FY2026 10-K marks, about early March 2027, date unverified) falls after the Jan expiry; Jan-15 17.5P 0.55/0.85 (43% wide, OI 2,287). A 5-month put on a non-signal is premium bleed. Re-open: BROCK's own line fires (an AI-infrastructure mark under 95% of cost, or a non-accrual), or the 10-K date is verified and an Apr-16 chain is priced against it.

## 7. OTTO (carried 11/12) — Exeter EART 2026-5 absent from its window → **NO CARD, agree with OTTO**

Exeter is private; its ABS is not reachable at Will's broker. A halt candidate on one shelf, with the sister shelf launched 9/17. OTTO-07 unmoved at 15%.
