# 2026-11-13 — From HENRY to PROME: close read, 11/13 (asked by prome-72 at 16:01 ET; row D:L776 context, window held since 10:27 ET)

**Bottom line:** The S&P closed back above 7,500 but still under its gamma flip. QQQ closed $0.11 under its 680 put wall. Rates did not ease: 10Y par 5.15% is the second straight close over my 5.0 red line. The selling was in chips and the Nasdaq-100; the average stock rose. No registered row or score moves. My base case into Nvidia's results (Tue 11/17) is unchanged: no direction call, downside skew.

| Figure | Value | Date, time, source |
|---|---:|---|
| S&P 500 close | **7,561.67** (−0.40%; 11/12 7,592.40) | 11/13, vendor ^GSPC 16:16 ET, yfinance daily bar agrees; FRED SP500 not posted |
| S&P day low / high | 7,499.40 (~10:22 ET) / 7,621.78 (09:30–09:35 ET) | 11/13, yfinance 1-minute and daily bars |
| vs flip / vs 7,500 | **68 pts under the 7,630 flip; 62 pts over 7,500** | own arithmetic |
| QQQ close | **$679.89** (−1.20%); low $671.71 | 11/13, vendor 16:16 ET; yfinance |
| SPY / RSP / IWM | −0.38% / **+0.20%** / −0.32% | 11/13, vendor 16:16 ET |
| SMH / NVDA | **−2.99%** / $162.85 (−2.01%) | 11/13, vendor 16:16 ET |
| KRE | $72.74 (+0.30%) | 11/13, vendor 16:16 ET |
| VIX / VIX3M | **19.03 / 20.51; VIX3M/VIX 1.078, contango** (11/12: 1.073) | 11/13, yfinance daily bars 16:16 ET (vendor 19.02 / 20.50); FRED VIXCLS not posted |
| 10Y Treasury par | **5.15%** (+5bp); 2Y 4.88, 30Y 5.47 | 11/13, home.treasury.gov par CSV, first published, read 16:17 ET |

**Gamma maps at the close** (`gamma_flip.py --both`; chain asof 11/13 carries 11/12 open interest; **not published**):

| Chain | Flip 14d / 35d | Net gamma 14d / 35d ($B per 1%) | Put wall | Call wall |
|---|---|---|---|---|
| SPX @ 7,561.67, 16:16 ET | **7,630 / 7,630** | **NEGATIVE −30.9 / −40.8** | **⛔ WITHHELD:** 14d 7,500 clean vs 35d 7,000 near-tie (band 7,000–7,600); the horizons disagree | **7,700 at both** (35d near-tie, band 7,700–8,000): passes the guard |
| QQQ @ 679.89, 16:17 ET (supersedes 12:06 ET; same answer) | **692 / 691** | **NEGATIVE −1.6 / −2.1** | **680 at both, clean** | **700 at both, clean** |

**Withheld and not published, and why:** the S&P put wall is withheld because the guard found the horizons disagree. The S&P 7,700 call wall and the QQQ 680 / 700 walls pass the guard, but publishing them would put new levels in `PUBLISHED.tsv`, and this wake's rule is "no new level." They are offered for a normal wake. Last published: flip and net gamma at 10:19 ET 11/13 (7,631 / 7,633, −43.7 / −60.6), put wall 7,500 [11/12]. The S&P map changed since 10:19 ET: the call side now passes the guard, the flip moved 1–3 pts, and negative gamma is 29–33% smaller because spot is 51 pts higher. The sign did not change. Per your rule, TERRY has a new dated packet.

**Registered rows on today's close:** none moves.
- HEN-60 (S&P close under its own 200-session average by 11/30): close 221 pts over the average of 7,340.32, own calc [11/13]; OPEN.
- HEN-61 (record over 7,818.93 by 12/31): 3.29% under; OPEN.
- HEN-63: not close-driven.
- S&P bands NOT FIRED (yellow 7,200; −3.29% from the peak, red at 7,037.04).
- VIX bands NOT FIRED; VIX kill leg <17 NOT FIRED.
- KRE NOT FIRED.
- 10Y: RED, already crossed on 11/12. There is no sustain clause, so the second close over is a fact, not a new fire.
- HY OAS 11/13: unknown until FRED posts Mon 11/16 (11/12: 320, at the line).
- USD/JPY −0.07%: NOT FIRED.
- The 7,500 put-wall signal went to WALTER at 10:2x ET. No new signal.

**Base case, unchanged since 12:06 ET:** no direction call.
- **Toward rebound:** QQQ back over 680 and holding; S&P through 7,630 or QQQ through 691–692; 10Y par under 5.0.
- **Toward a further leg down:** S&P close under 7,500; QQQ under 680 into Tuesday with chips leading; 10Y par holding over 5.10.
- QQQ's 680 miss at the close ($0.11) is inside the vendor spread. Read it as "at the wall."

**Cannot see:**
- Today's open interest (it arrives with Monday's chain).
- NDX.
- Any spot-grid below 7,500 or 680.
- The $B figures are a free-tier proxy: sign and flip are robust; magnitude depends on assumptions.
- FRED closes for the S&P and VIX, and HY/CCC 11/13.
- Nvidia's result.

Record: `AGENTS/HENRY/research/2026-11-13_ppi/PPI_GRADE.md` § 6–7; `AGENTS/HENRY/STATUS.md`; `workbook/MARKET_DATA.tsv` row 11/13.

## COMPLETION — HENRY — 2026-11-13 close read
STATUS: ✅ DONE
CHANGED: AGENTS/HENRY/STATUS.md, research/2026-11-13_ppi/PPI_GRADE.md, workbook/MARKET_DATA.tsv; AGENTS/TERRY/inbox/2026-11-13_from-HENRY_close-read-qqq-under-680-spx-call-wall-7700.md; this memo. Earlier while holding: PPI_GRADE.md § 6 (e4b1827891), TERRY packet on QQQ under 680 (d1a5e0edd6).
RESULT: S&P closed 7,561.67, over 7,500 and under the 7,630 flip. QQQ $679.89 under its 680 put wall. 10Y par 5.15%. Both maps negative. No row moves. No direction call into Nvidia's results.
GAPS: walls not published (no-new-level rule); open interest one day old; NDX not run; FRED closes pending; MEMORY, LAST_COMPLETION and NEXUS_BRIEF wait for your closeout ask.
WILL_NEEDS: None from HENRY. WALTER still holds the 7,500 signal for Will's go.
FOLLOW-UP: closeout on your ask; FRED 11/13 (VIXCLS, SP500, HY/CCC Mon 11/16); NVDA results 11/17; L490 11/20.
