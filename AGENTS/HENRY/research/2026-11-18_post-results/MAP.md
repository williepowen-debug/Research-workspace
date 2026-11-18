# 2026-11-18 — first dealer map after Nvidia's results, plus the FRED check of the 11/17 close

**Session:** HENRY, PROME prome-6e wake (D:L1051, D:L1163), Claude Code, Opus 5.5 (`claude-opus-5-5`), desktop. Launched about 10:15 ET. Every stamp below is from `date` in the same command as the read.

## 1. FRED check of the 11/17 close (HEN-60 was graded on the vendor close)

| Series | FRED latest at 10:16 ET 11/18 | HENRY's cell | Result |
|---|---|---|---|
| SP500 | **11/17 not posted**; latest row 11/16 = 7,416.59 | 11/17 7,340.53 (Cboe and vendor, agree to the cent) | **Not yet checkable.** 11/16 row confirms the 11/16 vendor cell 7,416.59 exactly. Retry at the 16:15 ET grade. |
| VIXCLS | 11/17 = **25.46** | 25.46 (Cboe settle, stamp 16:15:01 ET) | **Confirmed.** 11/16 22.91 also confirmed. |
| HY / BB / CCC OAS | 11/16 = 334 / 196 / 1,310; 11/17 not posted | 11/16 same | 11/17 not yet posted (ICE posts T+1, later in the day). |

HEN-60's grade stands on the letter's vendor basis; the FRED confirmation is pending, not failed. If FRED SP500 11/17 differs from 7,340.53 the difference is disclosed, not re-graded (the margin was 4.00 points under the 200-session average 7,344.53).

## 2. Which chain, which open interest

- **Chain:** Cboe delayed SPX options JSON (`cdn.cboe.com/api/global/delayed_quotes/options/_SPX.json`), payload timestamp **2026-11-18 15:16:23 UTC = 10:16:23 ET**; underlying last trade 10:01:21 ET (the 15-minute delay); 31,580 contracts, 30,034 with IV above zero (the 09:30–09:45 ET IV = 0 window had cleared; `src=cboe`, no vendor fallback). Total open interest 26.15 million contracts.
- **Open-interest vintage:** OCC open interest as of the **11/17 close**, posted this morning. This is the first chain carrying Tuesday's (Nvidia-day) trades. **It does not contain anything traded after Nvidia's results** (11/17 after-hours or today). Hedging done in reaction to the results is invisible to this map until Thursday 11/19's chain.
- QQQ: Cboe delayed QQQ chain, same fetch window, same vintage.

## 3. The reads (`gamma_flip.py --both`, free-tier proxy)

| Run (ET) | Spot used | Flip 14d / 35d | Net gamma 14d / 35d ($B per 1%) | Walls (cross-horizon guard) |
|---|---|---|---|---|
| boot (b), 10:16 | 7,365.91 (Cboe feed) | 7,543 (14d) | −52.8 | 14d put = call 7,400: withheld |
| `--both`, 10:16:48 | 7,353.00 (Cboe feed, 10:01 trade) | **7,572 / 7,579** | **−56.0 / −76.9** | call 14d 7,400 vs 35d 7,000: WITHHELD; put = call at both: WITHHELD |
| `--both --spot 7335`, 10:18:55 | 7,335 (vendor live 7,335–7,339) | **7,552 / 7,562** | **−55.9 / −77.7** | same: both WITHHELD |
| boot rerun, 10:19 | Cboe feed | — | −55.6 (14d) | — |
| **QQQ `--both`, 10:18:43** | 659.99 (Cboe feed) | **673 / 675** | **−1.7 / −2.6** | call 680 at both horizons passes (35d near-tie band 680–700); put = call at both: WITHHELD |

**Flip across four reads in three minutes: about 7,545–7,580.** The digits move with the spot used and the refetched chain, so the band is the finding, not any one number (LESSONS, two pulls).

**Against the 11/17 close read (11/16 open interest, at 7,340.53):** flip 7,599 / 7,604, net −64.4 / −86.8. The flip is about 25–55 points lower today. The $B are smaller, but Tuesday's expiries rolled off between the two chains, so the $B change is not a positioning change I can separate (MEMORY 10/30: compare flips, not $B, across an expiry). QQQ flip 681 / 680 → 673 / 675.

## 4. Tape at the map (vendor, 10:18 ET; Cboe delayed in brackets)

SPX 7,335.08 (−0.07%) [Cboe 7,352.70 at 10:01, low 7,303.22] · VIX 24.56 (−3.53%) [Cboe 24.24, high 26.26] · VIX9D 25.07 vs VIX3M 24.50: front still inverted, narrower than 11/17's 26.70 / 24.98 · NVDA 153.83 (−1.05% vs the 155.46 close; after hours 11/17 158.50, +1.96%) · SMH +0.15% · QQQ 659.30 (+0.36%) · RSP −0.10% · IWM +0.67% · KRE 70.81 (−0.06%) · 10Y 5.09 · USD/JPY 159.26. PANW 330.57 (+6.88%), HACK 116.78 (+3.62%): row 9 context only, graded after 16:15 ET.

NVDA's after-hours gain reversed after the WSJ report (via TechCrunch 21:48Z, WALTER SIG-W-20261117-025) of an SEC civil probe of Nvidia's disclosures; the report came after the 158.56 after-hours print. **Cause of the reversal not established.**

## 5. So what

**The results did not change the regime.** Dealers are still short gamma at about −$56B / −$77B per 1% (proxy), with the flip about 3% above spot (7,545–7,580). Moves in either direction are still amplified; a close over about 7,560 is where dealers would start damping instead. This map says how big moves get, not which way. The index is flat on the morning, so far the results are not an index event; Nvidia itself is down.

**Investment implication: none new.** The sign has been negative at every read since 11/13 and the flip moved modestly; nothing here is a fresh, testable direction call. No TERRY packet (WQ-696 rule: a forecast grade or a map is not by itself an implication). Not published: walls fail the guard, and this wake's letter changes no threshold; flip and net gamma are recorded here and offered.

⚠️ Free-tier proxy: sign and flip reliable; $B assumes dealers long calls and short puts; IV held fixed across the spot grid; positioning is Tuesday's, so results-day hedging is unseen until 11/19.
