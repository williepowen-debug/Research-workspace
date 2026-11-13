# HENRY · October PPI graded (HEN-58, D:L776) and the post-print dealer-gamma map · 2026-11-13

**Written:** 2026-11-13 10:2x ET (clock 10:21 at file creation), PROME wake prome-72 (D:L776; Will's standing rules WQ-184, WQ-667 B). Claude Code, Opus 5.5 (`claude-opus-5-5`). No threshold, band or level is set or moved here. HENRY makes no card; tradeability is TERRY's.

## 1. The grade

**HEN-58: NONE. Final demand +0.3% m/m (SA), first print. My frozen expectation was NONE: HIT.** Graded about 1h50m after the 08:30 ET release (the 08:00 ET pre-open launch did not happen); the letter says a late grade is not NO-VERDICT, and the delay is disclosed here.

| Series (BLS ID, SA) | Oct 2026 m/m | Sep 2026 m/m, as now revised | Sep first print (KB ML-HEN-179) |
|---|---:|---:|---:|
| **Final demand (WPSFD4)** | **+0.3** (unrounded +0.348) | **+1.4** (+1.408) | +1.3 |
| Final demand goods (WPSFD41) | +0.5 (+0.529) | +2.5 | — |
| Final demand services (WPSFD42) | **+0.2** (+0.210) | **+1.0** (+0.997) | +0.8 |
| Foods (WPSFD411) | **+1.3** (+1.342) | +1.1 | — |
| Energy (WPSFD412) | **−0.1** (−0.125) | +10.0 | — |
| Goods less foods and energy (WPSFD413) | +0.5 (+0.546) | +0.3 | — |
| Final demand less foods and energy (WPSFD49104) | +0.3 (+0.326) | +0.8 | — |
| Final demand less foods, energy and trade (WPSFD49116) | **+0.5** (+0.486) | +0.5 | +0.5 |
| Final demand, NSA, year on year (WPUFD4) | **+6.5** (+6.520) | +6.3 (+6.286) | +6.3 |

All figures are my arithmetic on index levels from the BLS public API (`api.bls.gov/publicAPI/v1`, pulled 10:17 ET 11/13; every October value flagged P, preliminary). One decimal is rounded from the unrounded change.

**What I could not open:** the BLS release itself. `bls.gov/news.release/ppi.nr0.htm`, the PDF, the PPI home page and the release schedule page all returned **HTTP 403** from this box (10:17 ET). The BLS series catalog at `download.bls.gov` also 403'd, so the series names in the table are from my standing knowledge of the PPI IDs, not read from the catalog. The grade therefore rests on agency index data, not the release text. Press relays agree on +0.3% headline, +6.5% year on year and a September revision to +1.4% (Stocktitan, MLQ via web search, 10:1x ET); none quotes the BLS text directly to me. ⚠️ Press "core" figures disagree (0.3 vs 0.5): that is the two core definitions, less foods and energy +0.3, less foods, energy and trade +0.5, both in the table.

**Consensus:** 0.4% (press relay, source not named; no survey panel read). ⚠️ Unverified at source. On that relay the print was 0.1 under consensus.

**Did my expectation hold for the right reason?** Partly. My one instrumented leg (energy products fell in October) held: energy −0.1. The leg I said I could not instrument, services, came in soft at +0.2, which is what kept the headline under the line. Food (+1.3) ran hot and I had no view on it. So the verdict was right; half of the reason was luck on an uninstrumented leg, as stated before the print.

**Revision worth carrying:** September is now +1.4 (first print +1.3) and services September +1.0 (first print +0.8). The September heat was larger than first reported; October cooled from a higher base. Year on year +6.5% is the highest since 2022 per press.

## 2. Tape reaction (vendor, 5-minute bars, 11/13)

| Time ET | S&P futures (ESZ26) | S&P cash | 10Y (vendor ^TNX, not par) |
|---|---|---|---|
| 08:25 bar | 7,642.50 | — | 5.15 |
| **08:30 bar** | **high 7,669.25, close 7,666.75 (+24 pts)** | — | **low 5.12 (−3bp)** |
| 09:25 bar | 7,642.75 (pop gone) | — | 5.16 |
| 09:30 open | — | **7,616.85 (+0.32%)**, high 7,621.78 | 5.17 |
| 10:00 bar | 7,564.25 | 7,543.59 | 5.15 |
| **10:18–10:20** | ES 7,562 (vendor, ~10 min behind) | **low 7,506.56 at 10:18; 7,508.6 at 10:20 (−1.10%)** | 5.15 |

Other legs at 10:18–10:20 ET (vendor): NVDA $160.43 (−3.47%), SMH −4.73%, QQQ −2.01%, SPY −1.08%, equal-weight RSP −0.52%, IWM −1.27%, KRE $71.99 (−0.73%), VIX 19.86 (+6.2%), VIX3M 20.77 (contango), USD/JPY 159.81.

**Read:** the market bought the cooler-than-consensus print for about 45 minutes in futures, and yields dipped 3bp; both reversed before the cash open. Since 09:30 the S&P has fallen 1.5% from its high (7,621.78 to 7,506.56) with yields back up and chips leading. Treasury par for 11/13 publishes after the close; the vendor 10Y is not my line's basis.

**Context verified, as asked:** Treasury par 11/12 10Y **5.10%** (home.treasury.gov CSV, re-read 10:18 ET 11/13; 2Y 4.86, 30Y 5.43). PROME's NOW page figure is correct; it is 10bp over my 5.0 red line (a cross with no sustain clause). FRED DGS10 has not yet posted 11/12.

## 3. Dealer-gamma map, re-run on live data (`gamma_flip.py --both --spot 7510.52 --publish`, 10:19 ET)

Chain: Cboe, asof 11/13 = **11/12 open interest** (the first chain carrying post-Nvidia trading). Spot: vendor live 7,510.52 at 10:19 ET (the Cboe feed price, 7,543.84, ran about 15 minutes behind).

| Read | 14d | 35d | Cross-horizon guard |
|---|---|---|---|
| Flip | ~7,631 | ~7,633 | **band 7,631–7,633**, unchanged from 11/12 (7,630–7,635) |
| Net dealer gamma at spot | **−$43.7B per 1%** | **−$60.6B per 1%** | **NEGATIVE both: dealers amplify**; spot 121–123 pts (1.6%) under the flip |
| Put wall | 7,500, clean (+33%) | 7,000 = call wall 7,000, put side UNRESOLVED | **⛔ WITHHELD** |
| Call wall | 7,600 near-tie, band 7,600–7,700 | 7,000 | **⛔ WITHHELD** |

**No wall is published today.** The last published put wall is **7,500** (11/12, clean at both horizons). The S&P came to within 6.56 points of it (low 7,506.56 at 10:18 ET) and had not printed under it as of 10:20 ET. A watcher on a vendor print under 7,500 runs to 16:05 ET.

**The computed profile held.** My 11/12 spot-grid (11/11 open interest) put net gamma at 7,500 at −$50.3B / −$60.9B per 1%. Today's re-run at 7,510 on new open interest reads −$43.7B / −$60.6B. The flip moved by 2–4 points. ⚠️ Free-tier proxy: sign and flip robust, $B assumes long-call / short-put dealers; comparing $B across days mixes in open-interest change.

## 4. Which scenario the print and the tape landed in (`research/2026-11-12_nvda-ceo/PPI_SCENARIO_MAP.md`)

| Question | Answer |
|---|---|
| Which print case? | **In-line (0.3–0.4%)**, the case where the map gave **no direction**. Not Case A (hot, 0.5 or more) and not Case B (cool, 0.2 or less, my judgment line). |
| Which map path did the tape take? | **Case A's path, without Case A's trigger.** From the 7,592 close the S&P went through the 7,567 low (between 09:45 and 10:00 ET) to the 7,500 wall (10:18 ET), in negative gamma the whole way, with yields up. That is the computed downside path; the hot print that Case A assumed never came. |
| Case A's falsifiers (hot print; S&P holds 7,567 through the first hour, yields fall, or VIX falls)? | Not applicable as written (the print was not hot). Every one of the three tape conditions went the other way: 7,567 broke inside the first 30 minutes, yields rose, VIX rose. |
| Case B's falsifier ("cool print with yields down but the S&P failing to reach ~7,630, or reversing below 7,567: the drag is Nvidia / AI leadership, not rates")? | Its premise is half met: yields fell for 45 minutes and then rose. The S&P did fail to reach 7,630 (cash high 7,621.78) and did reverse below 7,567. **My judgment: both legs are driving.** Chips lead (SMH −4.7%, QQQ −2.0% vs RSP −0.5%) and long yields rose on a soft print. Neither leg alone explains the move. |
| In-line row's caveat ("an ordinary move still travels further in an amplifying tape") | **Confirmed in kind:** a 1.4% slide from the open (7,616.85 to 7,506.56) on a non-event print. Net gamma reads two to three times the 11/12 close figure, mostly because spot is 82 points lower on the same profile. This is consistent with the map; it does not prove the map caused it. |

**So what:** the inflation print was not the problem. The S&P is under its flip and sitting on its last published put wall, in a tape where good inflation news did not bring yields down. On the computed profile, the amplification deepens below 7,500 to about 7,350–7,450 (computed 11/12; today's open interest not re-gridded). My yellow line is 7,200; the red line is 7,037.04.

## 5. Not done here

- No spot-grid re-run on today's open interest (about 3 s per level; offered if PROME or TERRY wants it).
- No QQQ or NDX map today.
- No consensus survey read at source; no BLS release text (403).
- No sizing of the PPI reaction (map caveat 4 stands).

Sources: BLS public API v1 (series above, pulled 10:17 ET); home.treasury.gov par CSV (10:18 ET); FRED fredgraph.csv SP500, VIXCLS, BAMLH0A0HYM2, BAMLH0A1HYBB, BAMLH0A3HYC (10:2x ET); vendor `FORGE/tools/market-data/fetch.py` and yfinance 5-minute and 1-minute bars (10:16–10:20 ET); Cboe chain via `AGENTS/HENRY/scripts/gamma_flip.py`; press via web search (stocktitan.net/articles/october-2026-ppi-report; mlq.ai; cnbc.com/2026/11/13/treasury-yields-fed-rates.html); letter `research/2026-10-29_catchup/PREREG_nov-releases.md`.

## 6. Hold-window reads (PROME asked me to hold for the close read)

**11:30 ET checkpoint, S&P map** (`gamma_flip.py --both --spot 7525.35`, not published): flip 7,632–7,634; net gamma −$39.5B (14d) / −$54.3B (35d) per 1%, negative at both; 14d put wall 7,500 clean (+29%), call 7,700 near-tie (band 7,600–7,700); 35d 7,000 = 7,000, put side unresolved; **both walls withheld**. No material change from 10:19. S&P last 7,525.35; day low 7,499.40 unchanged.

**12:06 ET, QQQ map, first run today** (`gamma_flip.py --both --underlying QQQ --spot 675.98`, chain asof 11/13 = 11/12 open interest; not published). Asked by PROME relaying Will's question "do we think QQQ will rebound? What is our base case?"

| Read | 14d | 35d | Cross-horizon guard |
|---|---|---|---|
| Flip | ~693 | ~690 | band 690–693 |
| Net dealer gamma at spot | −$1.9B per 1% | −$2.4B per 1% | NEGATIVE both |
| Put wall | 680, clean (+59%) | 680, clean (+52%) | passes at both |
| Call wall | 700, clean (+22%) | 700, clean (+38%) | passes at both |

**QQQ is under its own put wall** (675.98 vs 680; vendor 676.85 at 12:06). Live 12:06 ET (vendor): S&P 7,534.86 (−0.76%), QQQ $676.85 (−1.64%), NVDA $161.04 (−3.10%), VIX 20.40, 10Y (vendor ^TNX) 5.13%.

**Base case into Nvidia results (Tue 11/17), my judgment:** no direction call on level. The in-line PPI removed the rates catalyst without removing the rates pressure (vendor 10Y 5.13 on a soft print). Both the S&P and QQQ sit under their flips, so dealers amplify whichever way the next move goes; the skew of that is downside while QQQ stays under 680. Into a binary event I would not call a rebound before it; the result decides.

| Toward rebound | Toward a further leg down |
|---|---|
| QQQ back over 680 and holding (back inside its put wall) | S&P close under 7,500 (last published put wall) |
| QQQ through 690–693 / S&P through 7,631–7,634 (regime flips to dampening) | QQQ holding under 680 into Tuesday with chips still leading |
| 10Y par back under 5.0 | 10Y par holding over 5.10 (11/12 par) |

**Cannot see:** today's open interest (chain carries 11/12's); NDX not run; no spot-grid below 680 for QQQ or a re-grid below 7,500 for the S&P on today's open interest; the gamma $B are a free-tier proxy (sign and flip robust, magnitude assumption-dependent); Nvidia's result itself.

**13:00 and 14:30 ET checkpoints:** S&P 7,535.58 and 7,556.70; day low 7,499.40 never re-broken. QQQ $676.63 at 13:00, $679.77 at 14:30 (under 680 both times). No trigger; no message.

## 7. Close read, 11/13 (asked by PROME 16:01 ET; data pulled 16:16–16:17 ET)

**The S&P closed back above 7,500 but still under its flip; QQQ closed $0.11 under its 680 put wall. Rates did not ease: 10Y par 5.15%, 15bp over my 5.0 red line, a second straight par close over it. No registered row or score moves.**

### Close tape

| Item | Close 11/13 | Change | Basis |
|---|---:|---:|---|
| S&P 500 | **7,561.67** | −0.40% (11/12 7,592.40) | vendor ^GSPC 16:16 ET, yfinance daily bar agrees; FRED SP500 11/13 not posted |
| S&P day range | low **7,499.40** (~10:22 ET), high 7,621.78 (09:30–09:35 ET) | close 62 pts over 7,500, 68 under the flip | yfinance daily and 1-minute bars |
| QQQ | **$679.89** | −1.20% | vendor 16:16 ET; day low $671.71, high $688.75 (yfinance) |
| SPY / RSP (equal weight) / IWM | $754.21 / $221.16 / $277.54 | −0.38% / **+0.20%** / −0.32% | vendor 16:16 ET |
| SMH / NVDA | $486.75 / **$162.85** | **−2.99%** / −2.01% | vendor 16:16 ET |
| KRE | $72.74 | +0.30% | vendor 16:16 ET |
| VIX / VIX3M | **19.03** / 20.51 | +1.8% / +2.2% | yfinance daily bars at 16:16 ET (vendor 19.02 / 20.50), one minute after the 16:15 index close; FRED VIXCLS 11/13 not posted |
| VIX3M / VIX | **1.078, contango** | 11/12: 20.06 / 18.70 = 1.073 | own arithmetic on the row above |
| 10Y Treasury par | **5.15%** | +5bp (11/12 5.10) | home.treasury.gov par CSV, 11/13 first published, read 16:17 ET; 2Y 4.88, 20Y 5.52, 30Y 5.47 |
| USD/JPY | 159.75 | −0.07% | vendor 16:16 ET, live, not a close |

**Breadth and leadership:** the selling was concentrated in chips and the Nasdaq-100; the average stock rose. SMH −2.99% and QQQ −1.20% against equal-weight RSP +0.20%. The S&P recovered 62 points off the 10:22 ET low (+0.83%), and QQQ recovered $8.18 (+1.22%) off its low, but neither got back to the flip. Intraday (10:20 ET) the gap was wider: SMH −4.73%, QQQ −2.01%, RSP −0.52%.

### Gamma maps at the close (not published; chain asof 11/13 = 11/12 open interest)

| Chain | Spot | Flip 14d / 35d | Net gamma 14d / 35d ($B per 1%) | Put wall | Call wall |
|---|---|---|---|---|---|
| SPX (16:16 ET) | 7,561.67 | **7,630 / 7,630** | **NEGATIVE −30.9 / −40.8**, 68 pts (0.9%) under the flip | **⛔ WITHHELD:** 14d 7,500 clean (+17%) vs 35d 7,000 near-tie (band 7,000–7,600) | 7,700 at both horizons (14d clean +12%; 35d near-tie, band 7,700–8,000): **passes the guard** |
| QQQ (16:17 ET) | 679.89 | **692 / 691** | **NEGATIVE −1.6 / −2.1** | **680 at both (clean, +56% / +50%)** | **700 at both (clean, +29% / +42%)** |

**What changed since 10:19 ET (S&P):** the flip moved 1–3 points; negative gamma at both horizons is 29–33% smaller (−43.7 → −30.9, −60.6 → −40.8) because spot is 51 points higher on the same profile. **The S&P call wall now passes the guard at 7,700** (at 10:19 the 14d call side was a 7,600 near-tie against a 35d 7,000). The put side is still withheld, now because the 35d put side resolved to a 7,000–7,600 band, not because it equaled the call wall. Last published S&P put wall: 7,500 [11/12].

**QQQ:** the 12:06 ET map is superseded by the 16:17 ET re-run, which says the same thing: walls 680 / 700 clean at both horizons, flip 691–692, negative gamma. QQQ closed **$0.11 under** its put wall, so it did not reclaim 680. One of the rebound signs I gave PROME at 12:06 (QQQ back over 680 and holding) is **not met**, by a margin smaller than the vendor spread.

**Not published, and why:** PROME's wake rules this session are "no new level, band or threshold." Publishing the S&P 7,700 call wall or the QQQ 680 / 700 walls would put new levels in `PUBLISHED.tsv`, where consumers pick them up. They pass my guard; publishing is mine to do at a normal wake and is offered. The 10:19 ET S&P flip and net-gamma rows remain the last published.

### Registered rows and scores on today's close

| Row | Today | Moves? |
|---|---|---|
| HEN-60, S&P close under its own 200-session average by 11/30 | close 7,561.67 vs 200-session average **7,340.32** (own calc, yfinance closes through 11/13), 221 over | No (OPEN) |
| HEN-61, record close over 7,818.93 by 12/31 | 7,561.67, 3.29% under | No (OPEN) |
| HEN-63, December FOMC hike | not a close-driven row | No (OPEN) |
| SPX yellow / orange / red (7,200 / 7,100 / 7,037.04) | 7,561.67; −3.29% from the 7,818.93 peak | NOT FIRED |
| VIX >23 / >28 / >30 | 19.03 | NOT FIRED (VIOLET owns the broadcast) |
| VIX kill leg <17 | 19.03 | NOT FIRED |
| KRE <$65 / <$62 / <$60 | $72.74 | NOT FIRED |
| 10Y >4.5 / >4.8 / >5.0 | **5.15% par 11/13** | **RED, already crossed on 11/12 (5.10)**; no sustain clause, so the second close over is a fact, not a new fire |
| HY OAS >320 | 11/13 not posted (FRED publishes Mon 11/16) | unknown today; 11/12 was 320, at the line |
| Put wall tested / broken (signal row) | printed 7,499.40 at ~10:22 ET (signal routed to WALTER 10:2x ET); closed 7,561.67 | already signalled; no new signal |
| USD/JPY velocity ±2% / day | −0.07% | NOT FIRED (SAM owns the call) |

**Base case into Nvidia results (Tue 11/17), unchanged from 12:06 ET:** no direction call. Both maps are in negative gamma, so dealers amplify the next move either way; the downside skew holds while QQQ is under 680 and the 10Y is over 5.10. **Toward rebound:** QQQ back over 680 and holding; S&P through 7,630 or QQQ through 691–692; 10Y par under 5.0. **Toward a further leg down:** S&P close under 7,500; QQQ under 680 into Tuesday with chips leading; 10Y par holding over 5.10.

**Cannot see:** today's open interest (Cboe's chain carries 11/12's; 11/13's arrives with Monday's chain); NDX not run; no spot-grid re-run below 7,500 or 680 on today's open interest; gamma $B are a free-tier proxy (sign and flip robust, magnitude assumption-dependent); VIX and S&P closes are vendor until FRED posts; HY and CCC 11/13 until FRED posts Monday; Nvidia's result.
