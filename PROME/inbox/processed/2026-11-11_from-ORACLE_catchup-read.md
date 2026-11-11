# ORACLE → PROME: 11/11 catch-up read (prome-2b wake, Will 09:24 ET)

**From:** ORACLE (Claude Code, Opus 5.5, desktop DESKTOP-BC6EF81, Kalshi lane SIGNED) · **Read:** 2026-11-11 14:45Z (09:45 ET), the first pull of the ET date, so it is today's gate read · **Record:** commit bd6bf9d89c

## What changed since my last read (Sun 11/08 16:58Z), in plain words

1. **The December Fed meeting now prices as a near-certain hike, with about a 1-in-8 chance of a half point.** On Sunday the crowd gave about 22% to no change. Today both betting venues give about 3% to no change, about 85% to a quarter-point hike and 11 to 12% to a half point or more. Fed funds futures say the same thing slightly more hawkishly: about +29bp expected, which is one full hike plus a small chance of a second. HENRY's relayed "+28 to +29bp, more than one full hike" is **confirmed in size** by my own pull, using the same arithmetic. The venues and the futures differ by about 2bp, which is inside the conversion's own error, so I am not calling it a disagreement.
2. **Most of the move came from Governor Waller's speech, not the CPI print.** The no-change bet fell from 18.5% to 6.5% in the hour after his 04:00 ET text went out on 11/10. The half-point bet moved mostly on the 08:30 CPI print (4% to 12%). That fits his "50bp if core is about 0.3" condition.
3. **Iran: the crowd now leans toward a quiet two weeks starting soon, and has priced out most of the oil war premium.** The chance that a two-week pause with no US strikes starts by 11/15 rose from 41.5% to 54.5%, crossing 50% for the first time. The chance of WTI reaching $110 in November fell from 17% to 7%. Thin Kalshi Brent bets fell by 20 to 26 points.
4. **Nvidia: the move is in CEO-tenure risk, not in AI-crash risk.** The chance of Jensen Huang leaving or being removed by year-end is about 15 to 17% on both venues, up from about 10.5% on Monday. Kalshi's by-mid-2027 contract rose 10 points today, to 39%, on real money (379K and 224K contracts open). The "AI bubble bursts in 2026" contract has not moved (7.0%). I found no SoftBank or AI-capex contract.

⚠️ **Caveats that matter for any decision:** (a) futures give an expected size of move, not probabilities: +28.9bp fits many mixes of hold, 25 and 50; (b) the futures prices are Yahoo last trades about 10 minutes old, not CME settlements, on Veterans Day; the NY Fed is closed today, so the latest published effective fed funds rate is 11/09 (3.88%); (c) I could not read CME FedWatch (cmegroup.com blocks this machine); (d) the Huang move's cause rests on WALTER's cards, and I have not read the underlying reports.

## Row-by-row

| Key | Read (2026-11-11 14:45Z unless stated) | Source quirk |
|---|---|---|
| **KB-ORC-133** 12/9 FOMC, Polymarket | hold **3.5** · +25 **85.5** · +50 or more **11.8** · cuts 0.6 ($25.4M event; +25 liq $681.2K, +50 liq $367.8K) | "+50 or more" is open-ended; the legs add to 101.4, a small overround |
| KB-ORC-133 12/9 FOMC, Kalshi `KXFED-26DEC` | above 4.00 97.0 (OI 140.1K) · above 4.25 12.0 (OI 161.0K) · above 4.50 1.0 (OI 159.6K) ⇒ **hold 3 · +25 85 · +50 11** · more 1 | cumulative rungs; the thin >5.00 rung (2.0, OI 970) sits above >4.50, a book artifact |
| KB-ORC-133 futures | `ZQZ26` 95.915 ⇒ Dec average 4.085; days 1–9 at EFFR 3.88 ⇒ post-meeting 4.169 = **+28.9bp**. `ZQF27` 95.815 = +30.5bp into January. Unit check `ZQX26` 96.12 = 3.880 = EFFR | expected value, not probability; assumes EFFR stays 13bp above the range floor after a hike; ignores month-end and year-end dips. 1bp of basis = 4 points on the half-point odds |
| KB-ORC-133 where they disagree | venues about +27bp vs futures +28.9bp. With hold at 3%, futures imply about 19% for +50 (78% for +25); venues say 11 to 12% | inside the conversion's error, so not routed as a divergence |
| KB-ORC-133 path | futures +19.0bp (11/06 close) → +20.4 (11/09) → +27.5 (11/10) → +28.9 (11/11 09:30 ET). PM hold 18.5 (09Z 11/10) → 6.5 (10Z) → 2.6 (14Z) → 3.5 now; +50 0.5 → 4.2 → 11.8 | CLOB hourly; Waller text 04:00 ET = 09Z, CPI 08:30 ET = 13:30Z |
| **VX-ORC-12** Dec hike gate | reads 11/09 **77.5** · 11/10 **84.5** · 11/11 **85.5**, all qualified; Alert held, no band touched | ⚠️ the leg is +25 only: a later fall can be money moving to +50, not a collapse |
| **VX-ORC-07** 48h moves | 🟠 Alert, stepped down from Critical: PM no-change at Dec −18.35 (24h, deep); another hike in 2026 +16.65; +50 leg +11.3; pause by 11/15 +11.0 | moves over 20 points exist only on thin Treasury-yield ladders ($29 to $610 liquidity): recorded, not marks |
| **KB-ORC-134** Iran pause | begins by 11/15 **54.5** · 11/22 65.0 · 11/30 68.5 · 12/31 82.5; by-11/8 leg 25.5 | by-11/8 at 25.5 ≈ 75% that a qualifying strike landed in its window (possibly the 11/08-night Qeshm report, card SIG-W-20261111-005); resolver evidence unread |
| KB-ORC-134 Iran escalation, Hormuz | invade 7.5 (10.5 on 11/08) · declares war 1.5 · regime fall 2.5 · Hormuz normal by 12/31 8.5 · by 11/30 2.2 · blockade end by 3/31/27 64.5 (−4.0 on the day) · senior meeting by 12/31 38.5 | Hormuz legs resolve on the IMF PortWatch print, which runs low |
| **VX-ORC-04** oil, WTI $110 Nov | reads 11/09 11.5 · 11/10 7.5 · 11/11 **7.0** (liq $23.6K); state none. Kalshi Brent over $97.99 / $95.99 at 11/30: 25.0 / 30.0 (OI 8.2K / 5.3K, 3¢ to 4¢ books) | spread +84.5pp; the widening is the oil leg falling, not more disruption |
| **KB-ORC-135** Nvidia, AI | PM Huang out by 12/31 **15.5** · by 3/31/27 26.5 · by 12/31/27 35.5. Kalshi Huang leaves before 1/1/27 **17.0** (OI 379.3K) · before 7/1/27 **39.0** (+10, OI 224.4K). PM Nvidia largest company 12/31 21.0 (63.5 on 11/03). AI bubble burst 7.0. NVDA beats Q3 EPS 94.5 on $937 (unreadable) | PM "announced resignation or removal" vs Kalshi "leave": different rules, never difference them. Largest-company mostly tracks the NVDA/AAPL price ratio. No SoftBank contract on PM; the Kalshi search is NOT CERTIFIED |
| Inbox | WALTER cards 20261109-001, 20261109-009, 20261111-006 processed. COR-20261109-09 and COR-20261111-06 receipted NO-OP: my records never carried the Rubio, IRGC or Abqaiq limbs | your brief said 4 cards; 3 were in my inbox. BOARD card 20261110-001 names ORACLE in its body but not on its recipient lines; I read it anyway |

**Tradeability (Will 11/10):** I found no tradeable gap from my side. Venues and futures agree within about 2bp, and the Huang contracts are a CEO-risk gauge, not a price dislocation. If you want TERRY's read on the half-point tail or the Huang odds, that routing is yours. I sent nothing to TERRY under this brief's one-packet limit.

**Suggested routing (yours; I sent none):** HENRY, LIQUID, BOND and CARL get KB-ORC-133 (ORACLE's charter routes a Fed-odds shift over 15pp in a week to LIQUID; the rule is written for cut odds, and this is the same size of move on the hold leg). HAWK, BRENT and FALCON get KB-ORC-134. VULCAN, BROCK and SAM get KB-ORC-135.

## COMPLETION — ORACLE — 2026-11-11
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/ORACLE/{STATUS.md, registry/corrections_receipts.tsv, workbook/KB.tsv, VX.tsv, V5_NOV110_READS.tsv, ODDS_LOG.tsv, KALSHI_ODDS_LOG.tsv, DISRUPTION_SUPPLY_SPREAD.tsv}, 3 cards to inbox/WALTER/processed/ (bd6bf9d89c); this packet
RESULT: Gate read 14:45Z, 51 PM and 9 Kalshi rows. The 12/9 FOMC prices hold 3.5, +25 85.5, +50 11.8 on PM; hold 3, +25 85, +50 11 on Kalshi; futures +28.9bp, about 2bp more hawkish. HENRY's relay is confirmed. Graded 3 gate rows (VX-ORC-12 Alert held, VX-ORC-07 Alert, VX-ORC-04 none) and 3 V5 reads. Added KB-ORC-133 to 135. Inbox drained, 2 corrections receipted.
GAPS: October CPI headline YoY not verified (the BLS API refused: daily request limit reached); the PM October CPI market (3.7% at 94.6, 92.5 before the print) resolves today and is graded at resolution. CME FedWatch could not be read (blocked from this machine). The Huang reports are unread. Coverage sweep (due ≤11/11) and the Hormuz weekly re-pin wait for closeout. Not pushed: safe-push runs at closeout.
WILL_NEEDS: None.
FOLLOW-UP: Next gate read Thu 11/12 (the routine may take it). Closeout on your ask.
