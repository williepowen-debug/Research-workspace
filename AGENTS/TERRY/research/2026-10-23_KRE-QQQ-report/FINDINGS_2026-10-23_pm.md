# KRE vs QQQ — afternoon findings (TERRY, 2026-10-23 13:4x ET from `date`)

Will-directed next steps #1 (book under scenarios) and #2 (how episodes end). Research only: no card, no order, no gate moved. Detail: `book_scenarios/RESULTS.md`, `episode_study/RESULTS.md` (scripts + raw pulls beside them).

## Correction to the morning report (finding 1)
The 20-day correlation was **positive every session in October until 10/21 (+0.03; +0.15 on 10/7)** and reached **−0.2357 on 10/22 alone**, pulled by one session (KRE +2.54%, QQQ −2.86%). The "2nd percentile" reading is true of that one close; the current episode is **0 sessions old** at the 10/22 close. Morning report and live pages still read as if the regime were established — not yet corrected (on Will's word).

## #2 — how do these episodes end? (mechanical rule, 5,116 bars 2006-06-22 → 2026-10-22)
Signal = first close with 20-session correlation ≤ the 10/22 reading; re-arms above 0. 13 completed episodes.

| Within 40 sessions of the signal close | Count |
|---|---:|
| **Both KRE and QQQ fell ≥5%** | **0 of 13** (0 at every threshold −0.15 / −0.20 / −0.30, n = 16 / 13 / 10) |
| Both rose ≥5% | 5 of 13 (4–6 across thresholds) |
| A day with both ≤ −1% | 9 of 13 (median 15 sessions in) — joint down DAYS happen, joint 5% falls did not |
| Correlation back above 0 within 20 sessions | 10 of 13 |

At +20 sessions: continued 5, flat 6, snap-back 2. Median from signal: QQQ +2.7% (+20) / +5.7% (+40); KRE −0.2% / +3.3%.
Rate split does not transfer: the "falling yields ⇒ continued" cases (4 of 6) were all QQQ leading; KRE leading while yields fall (today) has one weak precedent (2017-06, 10y −0.05 pts, flat).
**Caveats:** n = 13, overwhelmingly bull-market years; no crisis episode exists in the sample (correlation runs high in crises, so these episodes never start there); the August 2024 joint drop (KRE −10.2% / QQQ −7.6%, 7/31→8/5) came after KRE had rallied +12% from the 7/5 signal, so it never took both 5% below the signal close.

## #1 — the book under scenarios (MODEL, quotes 13:38 ET)
Lines: 29 Fidelity bank/credit puts + 2 Robinhood (unverified since 9/29) and QQQ Oct-26 710P ×1 / 705P ×2 / Nov-20 690/670P ×2. Value at screening mid: bank/credit $2,239 · Nasdaq $2,751 · total $4,989. KRE Nov-27 70P has no vendor quote (IV 30% ASSUMED).

| By 11/13 close (Oct-26 lines excluded) | KRE | QQQ | Book change |
|---|---:|---:|---:|
| Flat | 0% | 0% | −$1,693 |
| See-saw continues | +5% | −5% | −$466 |
| Snap-back | −5% | +5% | −$415 |
| Both fall (Aug-2024 shape) | −10% | −8% | +$9,077 |
| Both fall hard | −15% | −12% | +$17,642 |
| Both rally | +5% | +5% | −$3,032 |

By Monday 10/26 close (whole book, the Oct-26 puts expire): flat −$1,355 (−$1,150 of it the Oct-26 lines) · see-saw +$2,658 · snap-back −$1,444 · both fall −3% +$7,913 · both rally +2% −$3,223.

## So what
The book is now a **joint-fall** position: it pays large only if KRE and QQQ fall together, and it loses in every other scenario by 11/13 (−$415 to −$3,032). From this starting state, history shows **0 of 13** joint ≥5% falls within 40 sessions and 5 of 13 joint ≥5% rallies. That does not refute the theses behind the lines (credit for the bank puts — REGINALD/LIQUID/DEWEY; dealer gamma for the spread — HENRY); it says **the KRE/QQQ divergence itself is not evidence for the joint fall the book needs.** No sell, hold or expiry prompt is implied (C5 paused; Will manages his own expiries).

## Deep push to 1985 (14:5x ET) — `deep_1985/RESULTS.md`
Stand-ins validated on 2006-06 → 2026-08 first: KBW Bank Index ^BKX vs ^NDX recovered 10 of KRE/QQQ's 13 signals; Ken French equal-weighted Banks vs ^NDX 9 of 13 (daily-return corr with KRE 0.90 / 0.92). Same rule (threshold −0.2357, re-arm > 0).

| Pair | Span | Episodes (complete) | Both ≥5% down in 40d | Both ≥10% down | Both ≥5% up | Joint ≥10% declines with a see-saw signal in the prior 60 sessions |
|---|---|---:|---:|---:|---:|---|
| ^BKX vs ^NDX | 1993 → 2026-08 | 17 | 1 (2021-11-23 → the 2022 bear market; runway 2 sessions) | 1 | 10 | 4 of 40 (base rate 11%) |
| FF EW Banks vs ^NDX | 1985 → 2026-08 | 15 | 0 | 0 | 7 | 0 of 19 (base rate 8%) |

**Finding: negative daily bank/tech correlation is a CALM-MARKET phenomenon.** Neither stand-in found a single episode in 1985–1992, 1998–2016 (incl. the 2000–02 dot-com bust and 2007–09), or any crisis. Joint declines started from a median 20d corr of **+0.68** (lockstep). The 2000 banks-up / tech-down rotation was a LEVEL divergence with POSITIVE daily correlation — a correlation rule cannot see it. The deep push added only 4–5 episodes (all 1993–97 bull years), and one counterexample: 2021-11-23, a −0.25 signal that turned into a joint ≥10% decline within 2 sessions.
Raw French file not committed (21 MB): `deep_1985/raw_french/` is re-created with `curl -o ff49_daily.zip https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/49_Industry_Portfolios_daily_CSV.zip && unzip ff49_daily.zip` inside `deep_1985/raw_french/` (Ken French data library, CRSP 202608 vintage; a later vintage may revise history).

## Correction to "calm-market phenomenon" (15:2x ET, Will challenged it) — VIX at signal (`deep_1985/vix_1990.csv`, 9,272 bars from 1990)
Wording withdrawn: the data supports "no episode began in a CRISIS regime" (max VIX at any signal 25.4; VIX ≥30 on 8% of days since 1990), NOT "markets are calm now". VIX 19.03 at the 10/22 close = 58th percentile since 1990 (median 17.6) and above the median episode signal (12.7–14.3). Episodes at VIX ≥18: KRE/QQQ 4 (both rose ≥5%: 4, both fell: 0) · BKX/NDX 7 (rose 5, fell 1) · FF EW/NDX 6 (rose 4, fell 0) — almost all 2020–21 post-COVID easing. The one joint fall, **2021-11-23 (VIX 19.4, hawkish-Fed turn)**, is the closest VIX match to today. Credit widening (HY 266 → 327–340), CCC 18% yields, FOMC 10/28 and the 11/3 election are stress inputs VIX alone does not carry; their read is LIQUID/DEWEY/HENRY's.

## KRE vs the rest of financials (16:0x ET, Will-directed) — `financials/RESULTS.md`
- **KRE leads every bank segment now:** 5d +3.8% vs large banks (KBWB) +0.9% and money-center (JPM/BAC/C/WFC) −2.1%; KRE vs ^BKX 20-day relative +4.2% = 92nd percentile since 2006. Since 10/6: KRE +3.4%, XLF +3.5% (insurers +5.3%), money-center −2.9%, BDCs −1.6%, QQQ −7.3%.
- **Split inside financials:** regionals up while money-center banks (−9.6% 3m) and private credit fall (alt managers APO/BX/KKR/ARES/OWL −25.1% YTD; BIZD −7.7% YTD). KRE up AND BIZD down ≥3% over 20 sessions: 2.9% of days since 2013. **In none of the 13 past see-saw episodes was BIZD down more than 0.2% over the 20 sessions into the signal; now −3.2% (10/22) / −4.3% (10/23).**
- **History:** KRE trailed large banks 2023 −2.8 pts, 2024 −14.2, 2025 −18.6; **2026 YTD +9.9 pts ahead** (KRE +13.7% vs ^BKX +3.9%), first year ahead since 2022. KRE/BKX ratio still at 27% of its 5-year range ⇒ a catch-up from a depressed level.
- **Inference (hypothesis — REGINALD/LIQUID/BROCK own the read):** the market is treating regionals as the financials LEAST exposed to the current stress (software loans / private credit / capital markets). The book's 16 KRE puts are aimed at the strongest segment; DEWEY's map puts the stress in BDC and loan holders — relevant to the WQ-509 BDC leg. Not a sell or hold prompt.
