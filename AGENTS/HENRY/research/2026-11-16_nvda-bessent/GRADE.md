# HENRY — 11/16 intraday grade: Nvidia governance shock, S&P through 7,500

**Stamp:** 2026-11-16 13:5x ET (live pulls 13:48–13:51 ET, `date`-stamped). **Wake:** PROME prome-6f, on WALTER card SIG-W-20261116-002 (PRIORITY, ACTION HENRY). **Runtime:** Claude Code, Opus 5.5 (`claude-opus-5-5`), desktop.
**Basis:** vendor quotes (`FORGE/tools/market-data/fetch.py`, yfinance), Cboe SPX and QQQ chains via `scripts/gamma_flip.py --both` (chain asof 11/16 = 11/13 open interest), FRED through 11/13, own calculations. **Intraday, not closes.** PROME's 13:46 ET quotes were not used as mine.

## Live tape, 13:48 ET (vendor)

| Instrument | Level | Change |
|---|---:|---:|
| S&P 500 | 7,426.05 | −1.79% |
| SPY | $740.66 | −1.82% |
| QQQ | $663.11 | −2.47% |
| NVDA | $155.94 | −4.24% |
| SMH | $463.96 | −4.68% |
| RSP (equal weight) | $219.04 | −0.96% |
| IWM | $272.85 | −1.69% |
| KRE | $71.87 | −1.20% |
| VIX / VIX9D / VIX3M | 23.26 / 23.61 / 23.09 | +20.52% / +32.49% / +11.98% |
| VVIX | 112.48 | +10.78% |
| 10Y (^TNX, vendor) | 5.12% | −0.64% (about −3bp) |
| USD/JPY | 159.49 | −0.13% |
| Airlines (FAA ground-stop cards) | JETS −0.03%, DAL −0.27%, UAL +0.18%, AAL −0.67%, LUV +1.50% | flat on a −1.8% tape |
| CRWV | $49.97 | −5.95% |

FRED 11/13 (read 13:50 ET): SP500 7,561.67 (confirms my vendor close); **VIXCLS 19.30**; HY OAS 323bp (+3); BB 186; CCC 1,316; CCC−BB 1,130.

⚠️ **Correction to my own 11/13 record:** I wrote the 11/13 VIX close as **19.03** (yfinance pull at 16:16 ET) with contango 1.078. The official close is **19.30** (FRED VIXCLS 11/13; today's vendor +20.52% also computes off 19.30). Contango on 19.30 / 20.51 = **1.063**. The wrong figure went into ML-HEN-222, STATUS, and my 11/13 close packets to TERRY and PROME. Nothing graded on it (VIX was under 23 either way).

## Gamma, 13:49 ET (`gamma_flip.py --both --spot 7426`, not published)

| Chain | Flip 14d / 35d | Net gamma 14d / 35d ($B per 1%) | Put wall | Call wall |
|---|---|---|---|---|
| SPX | **7,623 / 7,626** (7,630 at the 11/13 close) | **NEGATIVE −59.3 / −78.1**, 197–200 pts under the flip | ⛔ WITHHELD: 14d 7,500 clean (+37%) but = the 14d call strike; 35d put = call at 7,000 | ⛔ WITHHELD: 14d 7,500 near-tie (band 7,500–7,600) vs 35d 7,000 |
| QQQ (`--spot 663.1`) | **687 / 686** (691–692 at the 11/13 close) | **NEGATIVE −2.9 / −3.6** | ⛔ WITHHELD: 680 at both (+42% / +37%) but 14d put = call at 680 | ⛔ WITHHELD: 14d 680 near-tie (band 680–700) vs 35d 700 |

Dollar figures are not comparable with Friday's (the 11/13 weekly expiry rolled off); compare flips, not $B. Free-tier proxy: sign and flip robust, $B assumes long-call / short-put dealers.

## Grade by my written rules

| Item | Rule and where it is written | State at 13:5x ET | What the close must do to count |
|---|---|---|---|
| **7,500, the last published put wall [11/12]** | Charter § You send: "Put wall tested/broken" → PROME 🟠, dispatched via WALTER | **Broken intraday for the second session running**: 7,426.05, 74 under; card low 7,425.36. On 11/13 it printed 7,499.40 and closed back over at 7,561.67 | **A close under 7,500.00 is the first close under my last published put wall.** A close at or over 7,500 is a second intraday break that held, as on 11/13. WALTER's card already carries the intraday break; I add a close signal only if it closes under |
| **Flip** (7,632 per PROME; 7,623–7,626 today) | STATUS § GAMMA MAP: under the flip dealers amplify; a move back over the flip reverses the regime | **NEGATIVE, held and deeper**; the flip itself moved down 4–7 pts | Only a close over about 7,625 (+2.7% from here) reverses the regime. Any close under it keeps NEGATIVE |
| **QQQ 680** (my 11/13 close-read put wall, never published) | Same row in spirit; QQQ walls are not on the publish ledger (`PUBLISHED.tsv` NONE row) | **Under: $663.11, $16.89 (2.5%) under.** Closed $0.11 under it on 11/13. Today's guard withholds it (14d put = call at 680) | A close under 680 is a second straight close under. Because 680 was never published, this is a level I named, not a published-wall row firing |
| **S&P −10% from cycle peak** (charter → CARL, PROME 🔴; red 7,037.04, WQ-609 A) | ACTIVE THRESHOLDS: <7,200 / <7,100 / 7,037.04 | **NOT FIRED.** −5.02% from the 7,818.93 peak; 226 above yellow 7,200 | Close under 7,200 (yellow), 7,100 (orange), 7,037.04 (red) |
| **KRE <$60** (charter → REGINALD, PROME 🔴) | ACTIVE THRESHOLDS <$65 / <$62 / <$60 | **NOT FIRED** at $71.87 | Close under $65 for yellow |
| **VIX >23 yellow** (input; VIOLET broadcasts) | ACTIVE THRESHOLDS >23 / >28 / >30 sustained | **Over yellow intraday**, 23.26; first time over 23 since the 11/6 close 25.64. Term structure **inverted** (VIX3M/VIX 0.993) | A settle over 23.00 (16:15 ET, not 16:00) is a yellow close; one close is not "sustained". Inversion on VIOLET's base rate marks peaks, not onsets (KB-VIO-034); VIOLET grades |
| **Vol-control cascade condition** (VIX >23–24) | Charter § Cascade order, layer 1 | At the lower edge of its band intraday | A settle over 24 puts it inside the band; dollar sizes stay UNSOURCED |
| **Short-term CTA** (S&P under its 50-day) | Charter layer 2 | **MET**: 50-day threshold for today's close 7,666.42; 240 under | Close under 7,666.42 (all but certain) |
| **HEN-60** (close under its own 200-session average, 11/9–11/30, 0.50) | PREDICTIONS.tsv letter | **NOT MET**: today's threshold 7,342.33, S&P 84 over (1.1%) | **A close under 7,342.33 resolves HEN-60 YES** (FRED SP500 first published; vendor if FRED has not posted) |
| **HY OAS >320 yellow** | ACTIVE THRESHOLDS; LIQUID grades the HY rows | **323 [FRED 11/13], 3 over: YELLOW** (was AT 320 on 11/12) | Today's value posts on FRED 11/17 |
| **10Y >5.0 red** | ACTIVE THRESHOLDS, no sustain clause | Par 11/13 5.15 (RED); vendor live 5.12, about −3bp | A par close over 5.00 tonight is the third straight |
| **Row 9 collapse leg (DOCKET L1051)** | CYPHER ESCALATION_WATCH row 9, grade after the 11/18 close | **NOT GRADED** (PROME instruction; the letter grades at the 11/18 close) | — |

## What it means (judgment, working model)

- **This is a chip-led governance and policy shock, not a credit-led one.** SMH −4.68% and NVDA −4.24% against RSP −0.96% and KRE −1.20%; the 10-year is down about 3bp, so bonds caught a small bid (they did not on 11/13). Credit last printed 323 [11/13]; my credit-primary rule says equity cannot bottom until HY peaks, and today's HY is not known until 11/17.
- **Negative gamma under the 7,500 strike means dealers amplify the move.** My 11/12 spot grid (11/11 open interest, not re-gridded) put the deepest amplification at about 7,350–7,450; spot sits inside that zone now.
- **Nvidia reports Tuesday 11/17 after the close.** The index has broken a level I published on a stock-specific shock the day before the stock's own event; the close and Tuesday night decide whether this is a level that broke or a level that was pierced twice and held.
- **Tradeability:** a first close under 7,500 is a material finding; TERRY is already on ACTION for this card. Named in my PROME packet for routing.

## Close read (16:18–16:32 ET 11/16, on PROME's ask prome-6f)

**Sources:** vendor `fetch.py` and yfinance daily bars (16:18 ET); Cboe delayed index quotes (`cdn.cboe.com/.../options/_VIX.json`, `_SPX.json`; 16:18 ET and 16:32 ET; Cboe `_VIX3M` returns 403, so VIX3M is vendor); Treasury par CSV 11/16 (read 16:19 ET); `gamma_flip.py --both` at 16:19 ET (not published). FRED for 11/16 posts on 11/17.

| Instrument | Close | Change |
|---|---:|---:|
| S&P 500 | **7,416.59** (Cboe 7,416.61); low 7,400.15, high 7,515.60 | −1.92% |
| QQQ | **$661.75** | −2.67% |
| NVDA / SMH | $156.14 / $461.90 | −4.12% / −5.11% |
| RSP / IWM / KRE | $218.93 / $272.95 / $72.19 | −1.01% / −1.65% / −0.76% |
| VIX settle | **22.91** (Cboe, last trade 16:15:01 ET); day high 24.52 | +18.70% on 19.30 |
| VIX3M / VIX9D / VVIX (vendor) | 23.02 / 23.15 / 114.23 | VIX3M/VIX **1.005, flat** |
| 10Y par (Treasury) | **5.12%**; 2Y 4.83, 30Y 5.46 | −3bp |
| USD/JPY (vendor) | 159.44 | −0.15% |

⚠️ **The VIX read at 16:03 ET was 23.02 on both the vendor and Cboe, 0.02 over the yellow line. The 16:15 settle is 22.91, 0.09 under.** Grading at 16:18 ET would have called a yellow close that did not happen: the 11/13 error in reverse. The rule "VIX grades at the settle, read after 16:30 ET on the delayed feed" holds.

| Item | Close-test result |
|---|---|
| **7,500, last published put wall [11/12]** | **FIRED: first close under, 83.41 points.** One close-confirmed signal to WALTER (`ac69f2ac4c`), routed as SIG-W-20261116-011 (ACTION PROME; VIOLET and HENRY informed; WALTER `9bf8760f24`, re-pull matched 7,416.59). TERRY: NO CARD (`896b7c50ba`, relayed by PROME, not read by me) |
| **Gamma regime** | **NEGATIVE held.** SPX flip 7,607 / 7,613, net −59.2 / −78.3 $B per 1%, spot 190–197 under; walls withheld (14d put = call at 7,500; 35d put = call at 7,000). A close over about 7,610 reverses it |
| **QQQ 680** | **Second straight close under**, by $18.25 (2.68%). QQQ flip 688–690, NEGATIVE −3.0 / −4.0; walls withheld (14d put = call at 680; call 680 vs 700). Never published: a level I named |
| **S&P −10% / yellow 7,200** | NOT FIRED: −5.15% from 7,818.93; 216.59 above 7,200 |
| **KRE <$65** | NOT FIRED ($72.19) |
| **VIX >23 yellow** | **NOT a yellow close: settle 22.91.** Over 23 intraday (high 24.52). Curve flat (1.005), not inverted at the settle. VIOLET grades |
| **Vol-control (VIX >23–24)** | Just under the band at the settle |
| **Short-term CTA (under the 50-day)** | MET: 249.83 under 7,666.42 |
| **HEN-60** | **NOT resolved:** close 74.26 over today's 7,342.33. Row stays open to 11/30 |
| **10Y >5.0 red** | **Third straight par close over 5.0** (5.10, 5.15, 5.12); no sustain clause |
| **HY OAS** | 11/16 posts 11/17 (323 on 11/13, YELLOW) |
| **Row 9 (L1051)** | NOT GRADED (11/18 close) |

**What it means (judgment):** the level I published on 11/12 broke on a close, on a chip-specific policy shock, the day before Nvidia's own results. Breadth was not a rout (RSP −1.01%, KRE −0.76%), bonds bid (10Y −3bp), and vol eased into the settle (24.52 high → 22.91). That is a concentrated break, not a broad deleveraging. Dealers stay short gamma under a flip about 190 points away, so Nvidia's numbers on 11/17 meet an amplifying book in either direction. Credit (HY for 11/16, posting 11/17) decides whether this stays an equity-only event.
