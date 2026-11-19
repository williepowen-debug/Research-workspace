# HENRY second touch 2026-11-19, midday reversal (prome-36 letter 12:15 ET; WALTER card SIG-W-20261119-017)

**Runtime:** Claude Code, Opus 5.5 (`claude-opus-5-5`), laptop. Every stamp below is from `date` in the same command as the read.

## 1. Tape (vendor live, intraday, NOT closes)

| Instrument | 12:16 ET | 12:19 ET | Prior close (11/18) | Note |
|---|---:|---:|---:|---|
| S&P 500 | 7,207.09 (−1.59%) | 7,206.42 (−1.60%) | 7,323.63 | Session high 7,415.64 on the 09:30 bar; low 7,193.83 on the 12:05 bar (5-minute bars, vendor) |
| VIX | 26.74 | **28.43 (+15.76%)** | 24.56 (Cboe settle) | +3.87 points intraday; VIOLET owns the broadcast |
| VIX9D / VIX3M | 27.17 / 25.57 | — | 23.95 / 24.29 | front over 3-month: inverted again (VIX3M/VIX 0.956 at 12:16) |
| QQQ | 648.76 (−1.63%) | 648.80 | 659.51 | |
| IWM | 264.58 (−2.05%) | 264.78 (−1.98%) | 270.12 | |
| RSP | 211.82 (−1.67%) | — | — | equal weight down as much as cap weight: broad, not a megacap-only drop |
| KRE | 68.88 (−2.33%) | 68.97 (−2.19%) | 70.52 | WAL −2.48%, ZION −2.56% |
| HYG / JNK / LQD | 76.62 (−0.03%) / 91.93 (−0.02%) / 103.10 (−0.05%) | 76.62 | — | credit ETFs flat |
| 10Y (vendor) | 5.07 | 5.05 | 5.07 par | about 2bp lower |
| AMD | 478.53 (−9.74%) | 478.32 (−9.77%) | — | Hunterbrook short report (CNBC via WALTER; report not read) |
| NVDA / SOXX / SMH | 148.37 (−1.72%) / 138.41 (−2.43%) / 449.97 (−2.08%) | — | — | |
| ANT (vendor ticker, Anthropic) | 96.94 | 95.56 | IPO price 83; open 111.50 (CNBC via WALTER) | about 14% under its open, still about 15% over the IPO price |

**Path (5-minute bars, S&P):** 7,411 at 09:30 → 7,390 at 10:00 → **7,304 at 10:30** → 7,315 at 11:45 → 7,281 at 11:50 → **7,220 at 12:00** → 7,194 low at 12:05. **Two legs, not one:** about −107 points from 10:00 to 10:30, before Anthropic opened, then about −121 points from 11:45 to 12:05 as it opened. The "fell the moment Anthropic began trading" account fits the second leg only; the first leg has no cause established here.

## 2. Dealer-gamma map (Cboe chain asof 11/19 = open interest through the 11/18 close; IV live-delayed; today's selling is NOT in the open interest)

`gamma_flip.py --both --spot 7203.64 --publish` at 12:17 ET (feed spot 7,247.84, about 15 minutes delayed):

| Read | Flip | Net gamma at spot ($B per 1%) | Walls |
|---|---|---|---|
| SPX 14d | 7,498 | −58.6 | call 7,000 (clean), put 7,000 (= call, unresolved) |
| SPX 35d | 7,517 | **−85.7** | call 7,000 (clean), put 7,000 (= call, unresolved) |
| Morning 10:04 ET (published) | 7,545 / 7,556 | −43.9 / −62.2 at 7,390 | withheld |
| QQQ 14d / 35d at 648.76 | 668 / 669 | −2.4 / −3.5 | put 650 near-tie band 640–650 at both (published); call 665 vs 700 (withheld) |

The flip moved about 40 points lower since 10:04 on the same open interest: that is the IV repricing (VIX +4), not new positioning. The robust part is unchanged: the S&P is about 300 points (4%) under the flip.

**Profile across levels (35d, own calc on the same chain, $B per 1%):**

| S&P level | All ≤35d | 11/20 expiry only | After 11/20 |
|---:|---:|---:|---:|
| 7,000 | −84.0 | −29.1 | −54.9 |
| 7,037 (red) | −85.2 | −30.3 | −54.9 |
| 7,100 (orange) | −86.8 | −32.6 | −54.2 |
| 7,150 | **−87.2 (trough)** | −34.4 | −52.8 |
| 7,200 (yellow) | −85.9 | −35.6 | −50.3 |
| 7,300 | −74.3 | −33.0 | −41.3 |
| 7,400 | −47.3 | −21.1 | −26.2 |
| 7,500 | −7.5 | −1.5 | −6.0 |
| 7,530 | +5.4 | +4.8 | +0.6 |
| 7,600 | +33.9 | +18.0 | +15.9 |

**Read:** the index sits at the bottom of the gamma trough: dealer hedging amplifies most per point between about 7,100 and 7,200, and stays heavily negative down to 7,000. **Friday's monthly expiry (11/20) holds about 24% of the ≤35d open interest and about 40% of the negative gamma at spot (−35.6 of −85.5).** After it rolls off, the remaining book is about −50 at today's level and the flip barely moves (about 7,525–7,530 ex-11/20). The single largest 11/20 strike is **7,000 (about 72K calls, 95K puts)**, 37 points under the red line 7,037.04; it is the dominant strike on both sides at both horizons. Published as `call_wall 7000` with that note (below spot, not resistance); put wall withheld.

**What would turn it:** a reclaim of about 7,500 (the flip band 7,498–7,530) turns dealers from amplifying to damping; nothing nearer does. Below, the only mechanical relief is time: Friday's expiry removes about 40% of the short gamma, so next week's moves need less fuel for the same size. Into the close and Friday: 7,200 (yellow, a close basis), 7,150 (the trough, most amplification), 7,100 (orange), 7,037 (red, −10% from the 10/6 peak), 7,000 (the expiry node).

⚠️ **Free-tier caveats (same as the morning):** sign and flip are robust; the $B magnitudes assume dealers long calls / short puts and hold IV fixed across the profile; the open interest is yesterday's and cannot see today's flows; 0DTE (11/19 expiries) are excluded (T = 0).

## 3. KRE vs the index (letter item 3)

KRE −2.19% to −2.33%, IWM −1.98% to −2.05%, RSP −1.67%, HYG −0.04%, 10Y about −2bp. KRE beta to IWM (daily, own calc): 0.61 (60 sessions), 0.66 (250), 0.89 (500). On the 500-session beta the expected KRE move is about −1.8%, so the excess is about 0.5 point; on the 60-session beta it is about 1 point, but that window holds the 'banks bid, tech sold' see-saw (D:L823), which deflates the beta. **My equity read agrees with REGINALD's BANK-ABSENT:** KRE is moving with small caps on a broad risk-off, credit ETFs are flat, and no bank headline is found (WALTER). One caveat that cuts the other way: my charter's attribution test ("KRE down despite falling yields = credit story") is met literally but weakly (10Y about −2bp); with HYG flat I do not read it as credit. D:L823 joint decline from 11/4 at the 12:16 read: KRE −7.0%, QQQ −6.2% (intraday; the study's line is −10% on both over 60 sessions, resolving 2027-01-20 to 02-18).

## 4. Red lines and thresholds (live figure, time)

| Line | Live | State |
|---|---|---|
| SPX yellow <7,200 (close basis) | 7,206.42 at 12:19 ET; low 7,193.83 on the 12:05 bar | **NEAR: 6 points over; traded through intraday.** Not a close |
| SPX orange <7,100 / red 7,037.04 | same | not near on a close basis (106 / 169 points over); −7.8% from the 7,818.93 peak |
| 200-day 7,331.08 (11/10 basis) | under | broken since 11/17 (HEN-60) |
| VIX >23 / >28 / >30 sustained | 28.43 at 12:19 ET | over the orange number intraday; the line is a close basis; VIOLET broadcasts |
| KRE <65 | 68.97 | not near (3.97 over) |
| 10Y >5.0 | 5.05 vendor | RED standing (par close basis) |
| HY OAS | 347 [FRED 11/18] | YELLOW; REGINALD's REG-T-04 (over 350 ×3) 3bp away, run 0 of 3 |
| CCC OAS | 1,353 [FRED 11/18], CCC−BB 1,148 | RED |

## 5. Grades of the WALTER lane (to WALTER by packet)

| Card | Disposition | Why |
|---|---|---|
| SIG-W-20261119-017 | acted | this record |
| SIG-W-20261119-018 | acted | HY 347 completes the third leg of the D:L823 study's unregistered watch sentence (HY rising from 3.40%, KRE ≥4% under its relative high, QQQ still falling); still unregistered, no measured precision |
| SIG-W-20261119-012 | noted | unnamed Fed official: no change to HEN-63 (0.70); unnamed, two candidate speakers, neither a 2026 voter on WALTER's read; KB combo row |
| SIG-W-20261119-013 | info-only | KC Fed is ISHM's grade, secondary figures only; a stronger regional adds to the hike side, KB combo row |
| AEOLUS Rhine exit (general inbox) | info-only | no HENRY surface carries the Rhine as firing (grep: none) |

## 6. PROJECTION (Will 11/19 12:01 ET; moves no score, band, gate or trade)

- **Base case, about 55%, through Friday 11/20:** wide, two-way trading with a downside lean while the S&P is in the gamma trough: closes inside 7,100–7,300 on 11/19 and 11/20; intraday ranges of 1.5–2.5%. After Friday's expiry roll-off ranges narrow next week (holiday week also thins volume, which confounds the test).
- **Main alternative, about 30%:** exhaustion and reflex. The day is an IPO event (an $81 billion raise; that holders sold other AI names to fund it is a hypothesis, not evidenced here) and a single-name short report, not a macro shock; credit and rates did not confirm. Tell: S&P back over 7,300 by Friday's close with HYG flat or up.
- **Tail, about 15%:** cascade. Close under 7,100 on 11/19 or 11/20 with VIX settling over 30 and HYG breaking down; HY over 350 on the 11/19 FRED print (posted 11/20) would add the credit leg that is missing today.
- **Dated tells:** VIX 16:15 settle today (over 28 = orange close); FRED HY 11/19 (posted 11/20 morning, REG-T-04 at 350); Friday expiry; KRE vs IWM spread (a KRE drop past −3% with IWM flat would be the bank-specific leg REGINALD says is absent).
- **Registered:** HEN-64, S&P closes under 7,100 on any session 11/19–11/25, probability 0.40 (base rates in the row).
- **For a channel, card or position:** no new investment implication from the evidence; TERRY gets the WQ-696 form.
