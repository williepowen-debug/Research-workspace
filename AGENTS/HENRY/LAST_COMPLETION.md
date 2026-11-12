# HENRY — 2026-11-12 09:0x–16:1x ET: Nvidia CEO resignation, the index and dealer-gamma read through the day — CLOSED 16:1x ET on PROME's ask (Will 16:11 ET)

**RESULT:** Nvidia's CEO resigned before the open, and the S&P took a one-stock hole that broadened by the close. The S&P opened −0.68%, bounced above its dealer flip at 11:08, then gave it back and closed 7,592.40 (−0.35%, vendor 16:06 ET). The average stock fell more (equal weight −0.85%, small caps −1.64%); Nvidia closed −4.34%. **The official 10-year closed at 5.10% (+12bp), over my 5.0% red line,** on a day stocks fell. At the close dealer hedging amplifies moves (about −$20B per 1%) going into Friday's 08:30 PPI. None of my predictions moved. No index line fired: the S&P is 392 pts over its 7,200 yellow line.

**CHANGED:** `STATUS.md` (11/12 VIEW and close, GAMMA MAP to the close, rate rows graded on par 11/12, Fri 11/13 pickup, 11/11 blocks rotated) · `STATUS_COLD.md` (§ ROT-11/12-CLOSE) · `MEMORY.md` · this file · `NEXUS_BRIEF.md` · `workbook/PUBLISHED.tsv` (maps at 09:14, 09:48, 11:09, 15:36, 16:06 ET; wall rows) · `workbook/KB.tsv` (ML-HEN-217 to 219) · `workbook/MARKET_DATA.tsv` (11/12 row) · `research/2026-11-12_nvda-ceo/OPEN_READ.md` and `PPI_SCENARIO_MAP.md` · dashboard source and page (v6, same URL) · `memory/auto/reference_henry_operating_dashboard.md`. Packets to `PROME/inbox/` (four) and `AGENTS/WALTER/inbox/` (one, consumed).

## Session work

| Item | Outcome |
|---|---|
| Pre-open and opening maps | Published 09:14 and 09:48 ET; Nasdaq put walls held the opening test (QQQ low $0.17 under 680) |
| Flip cross 11:08 ET | Watcher fired; S&P map turned marginal POSITIVE; packet and doorbell to PROME |
| Close hour 15:36 ET (Will asked) | Back under the flip, NEGATIVE −$21B / −$25B; selling broadened; packet and doorbell to PROME, routed to TERRY |
| Close 16:06 ET | Published: flip 7,635 / 7,630, −$19.9B / −$21.5B; put wall 7,500 and call wall 7,700 clean at both horizons |
| Treasury par 11/12 | 10Y 5.10 RED crossed, 2Y 4.86 (RED, 26bp over), 30Y 5.43 ORANGE; to WALTER → SIG-W-20261112-008, ACTION BROCK |
| PPI scenario map (PROME ask) | Computed gamma at each level 7,200–7,750, hot and cool cases, judgment marked, a falsifier per case |
| WATCH_FOR | ADOPTED the 64-phrase megacap CEO/CFO-change set (PROME lands it) |
| Dashboard | v5 at midday, v6 at the close, same URL |
| Correction | I told you the put wall "tends to act as a floor". On my own model it is where hedging pushes hardest with the move; walls holding is a tendency, not a computed floor. Fixed everywhere |

## GAPS / still pending

- The VIX close is not logged: the index settles 16:15 ET and my last read was 18.87 at 16:12. FRED VIXCLS confirms it Friday.
- The S&P close is a vendor quote after the cash close, not FRED-confirmed yet.
- The gamma map is 11/11 open interest at today's prices (before the Nvidia news). Same-day and closing-auction flow are not in it; the dollar sizes are free-tier estimates.
- Nvidia's index weight (~7.5%) is assumed, not read from an index provider.
- D:L490 (Confidence backfill) not started: carried to Friday after PPI, as PROME directed.

## COMMITS

`16f961e17d` first read and pre-open maps · `655510e4b3` WALTER lane · `b4f1664f19` + `2792724681` + `ae91bd2029` opening packet · `4cc438b9eb` + `cbe75a8e24` flip cross · `54e9318d26` dashboard v5 · `4064c4153d` L490 carry · `ef6595caf0` WATCH_FOR · `791bfc6caa` + `1b2655b223` close-hour read · `1addf906ff` 10Y signal to WALTER · `4caa5af5fe` PPI scenario map · `021592ba4d` dashboard v6 · closeout commit "HENRY: 11/12 closeout".

## NEXT SESSION FOLLOW-UP

**Fri 11/13: pre-open map about 08:00 ET and producer prices (PPI) at 08:30 ET (HEN-58)**; D:L490 by 11/15; Nvidia results Tue 11/17 after the close; Palo Alto row 9 at the 11/18 close; release calendar rebuild before 11/20; FOMC Wed 12/9 (HEN-63; market price is ORACLE's).

## THESIS SNAPSHOT (frozen at close 11/12)

Rates are the pressure: 10Y par 5.10% (RED crossed), 2Y 4.86% (RED), 30Y 5.43% (ORANGE), and yields rose on an equity-down day. Equity: S&P 7,592.40, −2.9% from its 10/6 record, 3.4% over its 200-day, under its 50-day; dealer gamma NEGATIVE, 7,500 put wall 1.2% below. Credit (FRED 11/11): HY 330bp YELLOW, CCC 1,330bp RED. VIX about 18.9. AI capex: leadership shock at Nvidia; Q3 results 11/17.

## WILL_NEEDS

None from this desk. No money moved; no threshold, gate, band, prediction or card changed. Tradeability of the negative-gamma read before PPI is TERRY's (PROME routed it).

*Honest scope: equity quotes are vendor or Cboe delayed, not settlements; Treasury yields are official par; the gamma map is a free-tier estimate (sign and flip reliable, dollar sizes not); the PPI cases are judgment where marked.*
