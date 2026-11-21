# HENRY — 11/20 close read, written Sat 11/21 (late wake)

**Session:** prome-77 due-row wake, letter 18:02:30 ET 11/21; HENRY on Claude Code, Opus 5.5 (`claude-opus-5-5`), laptop. Started 18:02 ET (from `date`). Launched late: the laptop slept about 14:53 ET 11/20 to 17:50 ET 11/21, so the planned 16:05 ET 11/20 close read did not run. Every figure below is a final Friday bar read on Saturday; nothing was read live at the close.

## 1. The close (Friday 2026-11-20)

| Item | Close 11/20 | Prior 11/19 | Source, read 18:02–18:07 ET 11/21 |
|---|---:|---:|---|
| S&P 500 | **6,910.39 (−3.70%)** | 7,175.83 | vendor ^GSPC daily bar; FRED SP500 11/20 not posted (latest 11/19 7,175.83) |
| From the 10/6 peak 7,818.93 | **−11.62%** | −8.23% | own calc |
| Two sessions (from 11/18 7,323.63) | −5.64% | | own calc |
| Nasdaq 100 / QQQ | 25,028.98 (−5.61%) / 608.45 (−5.67%) | 26,517.05 / 645.04 | vendor bars |
| SMH / NVDA | 400.06 (−10.60%) / 125.53 (−14.01%) | 447.48 / 145.98 | vendor bars |
| RSP / IWM / KRE / HYG | 207.44 (−1.98%) / 256.61 (−2.88%) / 68.32 (−1.36%) / 76.33 (−0.26%) | | vendor bars |
| VIX / VIX9D / VIX3M | **35.89 PROVISIONAL** / 40.72 / 30.94 | 28.44 (FRED) / 29.26 / 27.03 | vendor bars. Cboe `_VIX` settle proof unavailable (Cboe refuses this laptop, 403 since 11/20); FRED VIXCLS 11/20 not posted. Grade on VIXCLS when it posts |
| VIX3M / VIX | 0.862 (steep inversion) | 0.950 | own calc |
| VVIX / SKEW | 138.03 / 138.84 | | vendor bars |
| Treasury par 2Y / 10Y / 30Y | **4.63 / 4.92 / 5.31** | 4.76 / 5.04 / 5.40 | home.treasury.gov daily par CSV, 11/20 first published |
| HY / BB / CCC OAS | not posted (FRED 11/20 due Mon 11/23) | 352 / 210 / 1,361 | FRED |

## 2. Grades on my own letters

| Letter | Line | Close | Result |
|---|---|---|---|
| **HEN-64** (close under 7,100 on any session 11/19–11/25, registered 0.40) | 7,100.00 | 6,910.39, 189.61 under | **Event YES on the vendor close. Not yet RESOLVED by the letter:** it names FRED SP500 first published as the source and the vendor close only if FRED has not posted by 11/27. FRED SP500 11/20 is due Mon 11/23; a 189-point difference is not plausible. Row stays OPEN with the YES noted; grade on FRED. If it holds: HIT, Brier (1 − 0.40)² = 0.36 |
| **Red line** (charter row "SPX −10%+ from peak → CARL, PROME 🔴"; −10% from cycle peak, WQ-609 A) | 7,037.04 | 6,910.39, 126.65 under; −11.62% | **FIRED on the 11/20 close (vendor bar; FRED confirms Monday).** First close under it; 11/19 closed 138.79 over. Intraday it broke before noon (7,024.16 at the 12:00 bar). Signal sent to WALTER, not around it |
| Orange 7,100 / yellow 7,200 | | | both under on the close |
| 10Y par >5.0 red | 5.0 | 4.92 | **first par close under 5.0 since 11/10** (4.98; six straight red closes 11/12–11/19 ended); now ORANGE (>4.8) |
| 2Y par >4.60 red | 4.60 | 4.63 | still RED, 3bp over (−13bp on the day) |
| KRE <$65 yellow | 65 | 68.32 | NOT FIRED (3.32 over) |
| D:L823 (KRE and QQQ both −10%, 60-session forward window) | | from 11/4: KRE −7.8%, QQQ −12.1% | UNRESOLVED; first candidate resolves 2027-01-20. KRE is the leg short |

**KRE against falling yields (charter's structural-vs-war test):** KRE fell 1.36% while the 10Y par fell 12bp, but it beat the S&P by 2.3 points and IWM by 1.5. On its 11/19 measured beta to IWM (0.66 to 0.89), the IWM move alone predicts −1.9% to −2.6%. Not a bank-credit read; no REGINALD flag.

## 3. Dealer positioning after the close (no chain published)

**Sources:** Cboe refuses this laptop (Cloudflare 403 since 11:34 ET 11/20). I did not try to get past it. ⚠️ **Disclosure:** two of my default commands still sent one ordinary request each to Cboe before I switched source by hand: the boot kit's gamma step and one `gamma_flip.py` call, both on the script's default "Cboe first" setting; both got 403 and fell back. Same identity, same endpoint, no workaround; after that I called the vendor source directly (`source="yfinance"`). The vendor chain is not the canonical chain, so nothing is published.

**The vendor's own implied volatilities are unusable this weekend:** median IV 12.5% (14 days) and 6.3% (35 days) with VIX at 35.89, no usable at-the-money contract, a pile at the 3% floor. On those fields the script prints a flip of about 6,897–6,917 and net gamma about zero. That read is an artifact of broken IV fields and I do not use it.

**Rebuilt on stated volatility:** open interest from the vendor chain (7,741 contracts within ±25% of spot, expiries 2 to 33 days out; open interest is as of Friday morning, so Friday's own trading is NOT in it), volatility set from the VIX term structure (VIX9D 40.7% to 9 days, VIX 35.9% at 30, VIX3M 30.9% at 93, linear between), flat or with a put skew of 1 and 2 (IV × (1 − skew × ln(K/S) / √(T/30d))). Spot 6,910.39.

| Assumption | Net gamma at spot ($B per 1%) | Flip | Profile (S&P level: $B per 1%) |
|---|---:|---:|---|
| Flat vol | −52.0 | 7,678 | 6,400 −50 · 6,800 −53 · 7,000 −50 · 7,200 −40 · 7,400 −23 · 7,600 −6 · 7,800 +7 |
| Skew 1 | −55.0 | 7,649 | 6,400 −47 · 6,800 −55 · 7,000 −54 · 7,200 −47 · 7,400 −28 · 7,600 −5 · 7,800 +12 |
| Skew 2 | −56.5 | 7,643 | 6,400 −44 · 6,800 −55 · 7,000 −57 · 7,200 −54 · 7,400 −35 · 7,600 −7 · 7,800 +17 |

- **Sign: NEGATIVE on every assumption tried** (the only positive read is the broken-IV one). Holding today's high volatility fixed as the index rises spreads gamma out and pushes the flip up; the 11/20 midday vendor-IV map had it at 7,422–7,440. **Flip band about 7,420 to 7,680, 500 to 770 points over spot: assumption-dependent, quote it as a band.**
- **Shape: flat from about 6,400 to 7,100.** No trough under spot to exhaust; the negative book only thins above about 7,200.
- Largest put strike 7,000 (now in the money, 90 points over spot); largest call strike 8,000. The 12/18 quarterly holds about 3.39 million of the roughly 6 million contracts in the 35-day window. No walls published.

**So what for Monday's open (11/23):** dealers are short gamma across the whole plausible Monday range, so their hedging adds to a move in either direction: they sell into a gap down and buy into a rebound. There is no options-book cushion between here and about 6,400. A volatility of 36 to 41 implies a daily move of about 2.3% to 2.6%. **Limits:** free-tier proxy on a non-canonical chain; volatility is my assumption, not market IV; the dollar figures assume dealers long calls and short puts; open interest excludes Friday's trades (heavy put buying on a −3.7% day would make the book more negative, not less, but I cannot see it); weekend news is not in any of it.

## 4. Base rates (own calc, ^GSPC and ^VIX daily closes since 1990, episodes 5 sessions apart)

| Condition | n | Any close ≥ +1.83% (back over 7,037) within 9 sessions | Any close ≤ −3.05% (≤ 6,700) within 9 sessions | Next day up | Next day move over 2% |
|---|---:|---:|---:|---:|---:|
| S&P −3% day and VIX ≥ 30 | 61 | 72% | 48% | 59% | 33% |
| same, drawdown 8–20% | 19 | 68% | 32% | 63% | 26% |
| all days VIX 33–40, drawdown 8–16% | 32 | 75% | 34% | 69% | 34% |

The two columns are separate events; many episodes did both. Nine sessions = 11/23 through 12/4 (11/26 closed).

## 5. PROJECTION (my judgment; moves no score, band, gate or trade)

- **Monday 11/23 (unscored):** a two-way, wide session. About 60% the S&P closes Monday higher than 6,910.39 (base rates 59–69%, shaded down for the weekend Nvidia SEC report and short dealer gamma); about 1 in 3 that the close-to-close move exceeds 2% either way.
- **Through 12/4, separate event probabilities, not one distribution:**
  - **HEN-65 (registered, 0.40):** a close at or under 6,700 on any session 11/23–12/4. Base rates 32–48%; I sit in the upper half because the gamma book is flat-negative to 6,400 with no cushion, credit has not yet repriced (HY 11/20 unknown, HYG only −0.26% on Friday) and Thanksgiving-week liquidity is thin.
  - **Close back over the red line 7,037.04 on any session in the same window (unscored, about 65%):** base rates 68–75%; shaded down because the selloff is concentrated in the index's largest weights (NVDA −14%, SMH −10.6%), which is where the index's level lives.
- **Why:** this is an AI and chip unwind with rates rallying (2Y −13bp) and credit lagging. That leg alone can carry the index through red because of its weight. What turns it into a broad cascade is credit following, which H4 (as amended 11/20) says it often does after the break, not before.
- **Changes my mind:** toward the downside, HY 11/20 at or over about 370 on Monday's FRED print with HYG breaking under about $75.50, or KRE falling with QQQ; toward the upside, a close over about 7,200 with VIX under 30, which would put the index back into the thinner part of the negative book.

## 6. Scorer note (PROME item 3)

HEN-60 0.50, HEN-61 0.28, HEN-62 0.60, HEN-63 0.70 and HEN-64 0.40 were each written as the probability of the YES event as lettered. The scorer's reading of the bare decimal is right for all five.

## 7. Nvidia SEC report (PROME item 4, context only)

Reuters 11/20 (published 14:16, updated 16:06, zone not shown) via VULCAN: SEC enforcement staff are scrutinizing potential accounting issues; no order, subpoena or Wells notice read. VULCAN owns that evidence; I did not check it. **Timing, on vendor 5-minute bars (America/New_York), assuming Reuters' 14:16 is Eastern (the zone is not shown):** NVDA was 131.60 at the 14:15 bar (−9.85% on the day) and closed 125.53, so about **a third of its −14.01% came after the report**. The S&P was **already under the red line before noon** (7,024.16 at the 12:00 bar) and was 6,991.42 at 14:15 (−2.57%), then fell a further 1.16% to the close, low 6,882.66 at the 15:55 bar. **So the red line broke before the report; the report coincides with the last leg, not the break.** Coincidence in time is not cause; I make no causal claim.
