# HEN-57 graded: October 2026 CPI (BLS, released Tue 2026-11-10 08:30 ET)

**Graded 2026-11-10 11:1x ET** (desktop, Claude Code, Opus 5.5 `claude-opus-5-5`; launched by PROME prome-07 after the 11/10 machine switch). DOCKET L775. **Late by about 2h40m after the print, disclosed; the letter says a late grade is NOT NO-VERDICT.** Cause of the delay: the laptop session closed at 10:1x ET without a wake (STATUS § CROSS-DESK, MEMORY 11/9 note). Letter frozen 10/29 at `research/2026-10-29_catchup/PREREG_nov-releases.md`; procedure `research/2026-11-09_cpi-wake/CPI_GRADE_SHEET.md`. Nothing re-specced.

## Grade

| Field | Value |
|---|---|
| Core CPI m/m, SA, one decimal (graded) | **+0.3%** |
| Unrounded, index-derived (not graded) | +0.296% (CUSR0000SA0L1E 339.900 / 338.896, api.bls.gov v1, pulled 11:09 ET; `latest=true` on M10) |
| BLS one-decimal wording | "rose 0.3 percent" core, "rose 0.4 percent" all items: BLS release text as quoted in press (CNBC, Axios, Quartz search summaries, 11/10). bls.gov returns 403 from this box, so the release page itself is unread. **Index derivation and the press-quoted BLS figure agree on both**; no basis conflict to disclose |
| Letter | 0.4 or higher = FIRED; 0.3 or lower = NOT FIRED |
| **Verdict** | **HEN-57 NOT FIRED** |
| Expectation (frozen 10/29) | NOT FIRED, at +0.2 |
| Expectation grade | **Verdict HIT; level MISSED by 0.1 on the hot side.** Core ran +0.296% against the Cleveland Fed nowcast +0.21% and the Bloomberg-survey consensus 0.22% (relay). The 0.4 line held by about 0.05pp of unrounded room (0.35 rounds to 0.4) |
| Positive control | September core from the same pull 338.896 / 337.765 = +0.335% → 0.3, matches the published September 0.3 |

**MISS LINE (WQ-619 A format):** I priced core at the nowcast and the survey, both about 0.2. The print was the third straight 0.3. The September unrounded core +0.335% and the nowcaster's hot-side miss on September core PCE (L774) both pointed hotter, and I named them as the risk and still wrote +0.2. Next CPI expectation starts from the three-month run rate of core (0.3, 0.3, 0.3), not from the nowcast alone.

## Headline versus core, and the energy share

| Index (SA) | Sep → Oct index | Oct m/m | Sep m/m |
|---|---|---:|---:|
| All items CUSR0000SA0 | 336.298 → 337.476 | **+0.350% (0.4)** | +0.648% |
| Core CUSR0000SA0L1E | 338.896 → 339.900 | **+0.296% (0.3)** | +0.335% |
| Energy CUSR0000SA0E | 337.834 → 340.197 | +0.699% | +5.196% |
| Gasoline (all types) CUSR0000SETB01 | 376.558 → 380.468 | +1.038% | +9.094% |
| Food CUSR0000SAF1 | 350.477 → 352.134 | +0.473% | +0.048% |
| Shelter CUSR0000SAH1 | 431.908 → 433.224 | +0.305% | +0.391% |
| Services less energy services CUSR0000SASLE | 448.723 → 450.247 | +0.340% | +0.369% |
| Commodities less food and energy CUSR0000SACL1E | 168.361 → 168.631 | +0.160% | +0.251% |

**Headline minus core: +0.054pp unrounded** (0.350 − 0.296). Approximate contribution with ASSUMED weights (energy about 6.5%, food about 13.5%, core about 80%; NOT the BLS relative-importance table, which is not loaded): core about +0.24pp, food about +0.06pp, energy about +0.05pp, sum about 0.35, which reconciles to the headline. ⚠️ The split is illustrative to about ±0.01pp; the index changes above are the agency figures.

**Read against my pre-print sheet:** I wrote that headline and core would land close together at about +0.2 each with a small energy share. **Close together, yes (0.05pp apart); +0.2, no.** Energy did not fall: SA gasoline rose +1.04% while NSA retail gasoline fell −1.0% in October (FRED GASREGW, my 11/9 calc). The seasonal factor flipped the sign, which my sheet flagged as possible ("SA gasoline could print near flat") but in the wrong size. Food (+0.47%) added as much as energy did.

**Against the war fuel path the L775 row names (Brent ~$108–110 through 10/21):** the war leg hit September (energy +5.2%). October energy added +0.7% on top rather than giving it back. Brent is now about $90.6 (vendor 11:09 ET 11/10, a futures bar, not a settle; BRENT owns), so the November energy leg should run the other way; that is a forward read, not a grade.

## Tape after the print (vendor 5-minute bars, intraday, NOT closes)

| Instrument | Prior close | 08:25 ET | 08:35 ET | RTH open | RTH low / high | ~11:10 ET | Day |
|---|---:|---:|---:|---:|---:|---:|---:|
| ES (Dec) | 7,574.25 | 7,578.75 | 7,536.75 | 7,523.00 | 7,503.75 / 7,566.25 | 7,521.75 (11:00) | −0.69% |
| SPX | 7,549.94 | — | — | 7,513.09 | **7,482.52** / 7,543.92 | 7,501.40 | −0.64% |
| 2Y note future ZT (Dec) | 102.348 | 102.215 | 102.094 | 102.051 | 101.977 / 102.059 | 101.980 (11:00) | −0.36% in price |
| 10Y yield (^TNX, vendor) | ~4.86 | | | | | 4.99 | +2.63% (about +13bp) |
| NVDA | 178.67 | 177.41 | 175.96 | 173.98 | **167.69** / 174.65 | 169.43 | **−5.17%** |
| SMH | 487.41 | 482.30 | 475.79 | 478.57 | 475.48 / **492.74** | 483.82 | −0.74% |
| QQQ | 679.35 | 676.95 | 671.72 | 672.55 | 669.92 / 680.95 | 674.36 | −0.73% |
| RSP | 220.95 | 221.49 | 220.62 | 219.59 | 218.90 / 219.98 | 219.53 | −0.64% |
| IWM | | | | | | 278.95 | −1.26% |
| KRE | 73.45 | 73.66 | 73.15 | 73.37 | 72.37 / 73.61 | 72.51 | −1.28% |
| VIX / VIX3M | 19.92 / 20.85 | | | | | 20.91 / 21.57 | +4.97%; contango 1.03 holds |

**The print moved the rates path, and the index only a little.** ES fell 0.55% in the ten minutes around 08:30 and has not extended: SPX is −0.6% at 11:10 ET, equal weight matches cap weight, small caps and regional banks lag (−1.3%), VIX +1 point with contango intact. The 08:30 bar is the CPI effect; the drift after the open is small.

**December hike, own calc, my 9/24 method (Dec average = 100 − ZQZ26; days 1–9 at EFFR 3.88 [FRED 11/9], days 10–31 at the post-meeting rate; P = (post − 3.88) / 0.25):**

| Read (vendor last, not CME settlement) | ZQZ26 | Post-meeting | Priced | Binary probability |
|---|---:|---:|---:|---:|
| 11/6 15:00 ET | 95.985 | 4.070 | +19.0bp | 76% |
| 11/9 15:00 ET | 95.975 | 4.084 | +20.4bp | 82% |
| 11/10 08:25 ET (pre-print) | 95.945 | 4.127 | +24.7bp | 99% |
| 11/10 08:35 ET and 11:00 ET | 95.920 | 4.162 | **+28.2bp** | **over 100%: a 25bp hike fully priced plus about 13% of a further 25bp** |

⚠️ One 0.005 tick = 0.7bp = 2.8 points. **Most of the move came BEFORE the print** (82% → 99% overnight, cause not established); the print added about 3.5bp at December and about 11bp at March 2027 (ZQH27 95.725 → 95.615, 4.275% → 4.385% contract average). The binary 25-or-hold model fails above 100%; the residual is consistent with some pricing of a 50bp December move. Press says the 0.3 core met Governor Waller's stated line for weighing a half-point hike (Stocktitan, MLQ headlines via search, **not read, secondary**). ORACLE owns venue odds; BOND owns the curve; HEN-63 (hike at 12/9, 0.70) is not re-marked here, and the scheduled 15:00 ET rerun stands.

## Against the map, with gamma negative

`gamma_flip.py --both --publish`, 11:1x ET, chain carries 11/9 trading, live vendor spot ~7,490:

| Horizon | Flip | Net GEX per 1% | Put wall | Call wall |
|---|---:|---:|---|---|
| 14d (4,924 contracts) | ~7,633 | −$47.9B | 7,500, clean #1, **but equals the 14d call wall** | 7,500, near-tie with 7,700 |
| 35d (8,333 contracts) | ~7,636 | −$57.3B | 7,500 clean (+36%) | 7,700, near-tie with 7,500 |
| Cross-horizon | 7,633–7,636 | NEGATIVE both | **WITHHELD** (put side unresolved at 14d) | **WITHHELD** (14d 7,500 vs 35d 7,700) |

**Read:** gamma is negative on both horizons, the flip ~7,635 sits about 1.9% overhead, and the largest gamma strike on both sides is now **7,500, which is where SPX is trading.** Spot has been either side of it all morning (low 7,482.52). Neither wall is published at this read, so 7,500 is a concentration at spot, not a support line. Dealers amplify moves either way below the flip; today that amplification has not shown up in size (−0.6%). The asymmetry I wrote into the grade sheet (a HOT CORE print is the case where the hike repricing and dealer amplification point the same way) was keyed on 0.4; the print was 0.3, the hike repricing happened, and the index did not cascade.

KRE −1.3% with yields up: under my 6/6 discriminator a falling KRE is the credit story, but KRE moved with IWM on a rate day, so this is not a credit read. HY and CCC for 11/10 publish on FRED 11/11; 11/9 was HY 334 (−8), CCC 1,311, BB 200, CCC−BB 1,111 [FRED 11/9].

## WALTER SIG-W-20261109-011 (ACTION HENRY): Nvidia on the session tape

**Nvidia's fall is its own, for the second day; CPI moved the index, not Nvidia's gap.** NVDA −5.17% at 11:10 ET against SMH −0.74%, QQQ −0.73%, RSP −0.64%: about 4.4 points worse than its own chip index. On 11/9 the close was NVDA −4.27% vs SMH +5.05%. Through the CPI bar NVDA moved with the market (177.41 → 175.96, −0.8%, while QQQ −0.8%); the relative loss came after the open (open 173.98, low 167.69) while SMH traded UP to 492.74 (+1.1%) in the same session. From 200.13 on 11/4 to 169.43 is −15.3% (vendor). Same single-name test as ML-HEN-208, same answer: this does not read through to the AI tape or to chips. The key-person and counterintelligence question is VULCAN's (KB-409); no read on it here. Point attribution of NVDA's index drag not run.

Sources: api.bls.gov v1 JSON saved beside this file (8 series); BLS figures as quoted in press: [CNBC preview 11/9](https://www.cnbc.com/2026/11/09/october-cpi-report-2026-inflation.html), [Axios 11/10](https://www.axios.com/2026/11/10/cpi-october-inflation-fed), [Quartz 11/10](https://qz.com/core-cpi-rose-october-matching-september-august-111026), [Stocktitan](https://www.stocktitan.net/articles/october-2026-cpi-inflation-report), [MLQ](https://mlq.ai/news/october-cpi-runs-hotter-than-expected-as-core-inflation-hits-wallers-threshold-for-a-half-point-hike/) (search summaries, pages not opened); vendor bars yfinance via `.venv`; FRED EFFR and BAML series; Cboe chain via `gamma_flip.py`.

**Addendum 2026-11-10 11:2x ET:** the "cause not established" overnight move above is now attributed on timing and the primary text to Governor Waller's London speech released 04:00 ET (09:00 GMT); his 0.3 core / 50bp line is read at federalreserve.gov, no longer secondary. See `OVERNIGHT_HIKE_REPRICING.md`.
