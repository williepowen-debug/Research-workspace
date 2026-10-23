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
