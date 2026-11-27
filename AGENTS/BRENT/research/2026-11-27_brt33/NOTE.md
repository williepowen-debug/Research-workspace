# BRT-33 resolution and the 11/27 Brent fall (2026-11-27, written from 13:10 EST)

Session brent-desk-2026-11-27, woken by PROME prome-80 for D:L993 (DOCKET line 993). Times from `date`. Vendor captures: `pull.py g1` (13:01 EST) and `pull.py g2` (after the window, see § 1); raw one-minute and daily bars per symbol in `raw/`; levels script `levels.py`, outputs `levels_g1.json`, `levels_g2.json`; window script `window.py`, output `window_g2.json`. [EST vendor, not settles; cmegroup.com IP-blocked, not attempted; no ICE page read.]

## 1. BRT-33 — graded by its own row

**The row's rule is not settlements.** `thesis/PREDICTIONS.tsv` BRT-33: vendor one-minute volume-weighted price per leg over [14:28,14:30) ET, both legs from one capture, each with at least one bar of positive volume, 4 decimals; "PROXY, labelled as such; no settlement substitution". PROME's wake letter asked for a grade "on SETTLEMENTS"; the registered letter governs and forbids that substitution, so the grade below is on the window proxy. No secondhand settle is used for any session.

| Session | M1−M3 (BZF27 − BZH27 window VWAP) | Valid | Read in |
|---|---|---|---|
| Fri 11/06 | none (BZH27 no window bar) | NO OBSERVATION | `../2026-11-06_window/NOTE.md` |
| Mon 11/09 | +3.8039 | yes | count line, `../2026-11-20_brt33/NOTE.md` § Count (read at the time in that week's notes) |
| Tue 11/10 | +3.7552 | yes (the low) | count line, `../2026-11-20_brt33/NOTE.md` § Count (read at the time in that week's notes) |
| Wed 11/11 | +3.8713 | yes | count line, `../2026-11-20_brt33/NOTE.md` § Count (read at the time in that week's notes) |
| Thu 11/12 | +4.2394 | yes | count line, `../2026-11-20_brt33/NOTE.md` § Count (read at the time in that week's notes) |
| Fri 11/13 | +4.9903 | yes | count line, `../2026-11-20_brt33/NOTE.md` § Count (read at the time in that week's notes) |
| Mon 11/16 | +4.5200 | yes | `../2026-11-16_brt33/NOTE.md` |
| Tue 11/17 | +5.0920 | yes | `../2026-11-17_brt33/NOTE.md` |
| Wed 11/18 | +5.0656 | yes | `../2026-11-20_brt33/NOTE.md` |
| Thu 11/19 | +4.8513 | yes | `../2026-11-20_brt33/NOTE.md` |
| Fri 11/20 | none (BZH27 no window bar) | NO OBSERVATION | `../2026-11-20_brt33/NOTE.md` |
| Mon 11/23 | +4.8917 | yes | `../2026-11-24_red-sea/NOTE.md` § 2 |
| Tue 11/24 | +4.8131 | yes | `../2026-11-24_red-sea/NOTE.md` § 2 |
| Wed 11/25 | +6.5515 | yes | `../2026-11-25_jazan/NOTE.md` |
| Thu 11/26 (Thanksgiving) | none (vendor holds no one-minute bars dated 11/26) | NO OBSERVATION | `../2026-11-26_jazan-refinery/NOTE.md` |
| Fri 11/27 | none: no bar for any leg in [14:28,14:30) ET (US energy stopped printing at 13:00 ET; last bars BZF27 12:58, BZH27 13:00) | NO OBSERVATION | this note, capture g2 (14:31:21 EST), `window_g2.json`; the same capture reproduces 11/25 at +6.5515 as a control |

(The per-session values are the ones recorded in the linked notes at each read; this note does not recompute sessions outside the vendor's reach.)

**Count:** 12 valid sessions, none strictly under +3.5000; low +3.7552 (11/10). The floor of 8 valid sessions is met.

**Grade: BRT-33 FAILED — outcome NO** (registered 20% on YES). Graded at 14:31 EST on 11/27, the first read after the last session of the window closed (the row says "the first read after 11/27"; every session in the window is now read and the market is shut until Sunday 18:00 ET, so no later read can add an observation). If PROME reads "after 11/27" as a calendar date, the same grade stands at any later read: nothing can change it. Lesson on the miss (WQ-619 A): what surprised me is that the curve tightened through the window instead of drifting: M1−M3 rose from about +3.8 (11/9–11/11) to +6.55 (11/25) as the Saudi Red Sea hits arrived, so the "deal-scare narrows paper" path never came. For the next comparable forecast: a driftless walk overstated the chance of a cross when the window opens on a rising, news-driven spread; price the drift sign, not only the volatility.

## 2. The 11/27 fall — what it was and what it was not

**Most of the headline "−4.63%" is a vendor roll, not a market move. VERIFIED from capture g1:** the vendor's continuous Brent `BZ=F` daily history holds the January contract (BZF27) on 11/24 (91.40) and 11/25 (94.61) and the February contract (BZG27) on 11/27 (90.02 daily, 90.15 last; one-minute `BZ=F` equals BZG27 bar for bar). 90.23 / 94.61 − 1 = −4.63%: the quoted fall compares February today with January on Wednesday. February sits about $4 under January. Oilprice.com's undated quote page showed the same kind of figure (−5.17%), so the artifact is not ours alone.

**Named-contract moves (vendor last traded 11/27 at capture g1, 13:01 EST, vs the vendor bar dated 11/26, last night's capture f1; capture g2 later added a BZF27 bar at 12:58, 94.00 on 35 lots):**

| Contract | 11/26 (last, f1) | 11/27 last (time ET) | Change |
|---|---|---|---|
| Brent Jan BZF27 (M1, last trade 11/30) | 96.48 (secondhand ICE settle 96.57) | 94.14 (12:34, last positive-volume bar) | −2.34 (−2.4%) |
| Brent Feb BZG27 (M2, = `BZ=F` now) | 92.19 | 90.15 (13:00) | −2.04 (−2.2%) |
| Brent Mar BZH27 (M3) | 89.29 | 87.32 (13:00) | −1.97 (−2.2%) |
| WTI Jan CLF27 | 85.69 (no CME settle on 11/26) | 82.85 (13:00) | −2.84 (−3.3%); vs Wed 11/25 daily 83.68: −0.83 |
| Heating oil Jan HOF27 | 3.7360 | 3.6776 | −1.6% |
| Gasoline Jan RBF27 | 2.4634 | 2.4320 | −1.3% |

Against Wednesday 11/25 (vendor daily) Brent January is −0.47 (−0.5%): **today gave back Thursday's Jazan and mine jump (+1.96 on 11/26) and a little more; two-day net is about flat.**

**Curve and cracks at the last bars (not same-minute for BZF27, thin expiry leg):**

| Read | 11/27 | Comparison |
|---|---|---|
| M1−M3 BZF27−BZH27 | +6.82 | +7.19 (11/26 daily last), +6.55 (11/25 window) |
| M1−M2 / M2−M3 | +3.99 / +2.83 | 11/25 window +3.92 / +2.64 |
| WTI M1−M3 CLF27−CLH27 | +2.58 | 11/24 window +2.08 |
| Brent−WTI Feb (BZG27−CLG27) | +8.62 | +8.21 (11/26) |
| **Diesel crack Jan HOF27×42 − CLF27** | **$71.61** | $71.09 (11/26), $69.81 (11/25), $80.51 Dec pair at the 11/20 window |
| Diesel crack Feb HOG27×42 − CLG27 | $71.10 | — |
| Heating oil Feb vs Brent Feb (HOG27×42 − BZG27) | $62.48 | — |
| Gasoline crack Jan RBF27×42 − CLF27 | $19.29 | — |
| 3-2-1 Jan vs CLF27 | $36.73 | $37.53 (11/24 window) |

Products fell less than crude (diesel crack +$0.52): the fall is in crude, not in product demand.

**Vendor daily bars dated 11/27 at capture g2 (14:31 EST)** differ from the last trades and look like the exchange's settlements, published after the close; NOT VERIFIED (CME blocked; no ICE page read):

| Contract | Daily 11/27 (g2) | vs 11/26 bar (f1) | vs Wed 11/25 daily |
|---|---|---|---|
| BZF27 | 94.65 | −1.83 (−1.9%); −1.92 vs the secondhand ICE settle 96.57 | +0.04 |
| BZG27 | 90.52 | −1.67 (−1.8%) | −0.12 |
| BZH27 | 87.71 | −1.58 | −0.30 |
| BZJ27 (April) | 85.48 | — | −0.55 |
| CLF27 | 83.01 | — | −0.67 (−0.8%) |
| HOF27×42 − CLF27 | $70.95 | — | — |
| HOG27×42 − CLG27 | $70.37 | — | — |
| RBF27×42 − CLF27 | $19.26 | — | — |

On this basis the day's fall in the front Brent is about −1.9%, and the next pinned pair BZG27−BZJ27 is +5.04. `BZ=F` daily reads 90.55, 0.03 off BZG27's 90.52: one more reason not to grade on `BZ=F`.

**Timing:** the vendor holds no bars between 11/25 23:56 and 11/27 09:30 ET. Brent January was $96.60 (+3 cents) at 12:39 GMT = 07:39 ET (Reuters via Media Selangor, page title "Oil on track to snap three-week losing streak"); vendor BZF27 95.54 at 09:30, 94.14 by 12:34. WTI January fell from 84.04 (09:30) to 82.85 (13:00) in a steady grind on thin holiday volume (about 2,000–5,500 lots per 10 minutes); the largest 5-minute drop was −0.39. **No step a single headline would make.** US energy futures stopped printing at 13:00 ET (holiday early close; last vendor bar 13:00, none by 13:09 EST).

**Cause — what is and is not established:**

| Candidate | Status | Basis |
|---|---|---|
| Vendor roll in `BZ=F` | **VERIFIED**, explains about half of the quoted −4.6% | capture g1 daily rows |
| A named bearish headline in US hours | **SEARCH-NOT-FOUND** | Trading Economics' 11/27 Brent item ("Brent Crude Trims Weekly Gains to Less than 2%", about −2.4%) gives no reason for the day's fall; its only bearish context is Gulf shipment recovery and OPEC+ expected to hold. Reuters/Bloomberg day stories not read |
| Profit-taking after about +6% in two sessions, thin holiday trade into a 13:00 close and a weekend with OPEC+ on Sunday | **INFERRED**, not sourced | grind pattern, volume, calendar |
| Risk-off macro | **Against**: S&P 500 +1.37% and VIX −7.5% at 12:30 ET (WALTER card 002, vendor) | — |
| Brent-specific Gulf premium unwind | **Weak**: WTI fell more than Brent and Brent−WTI widened | table above |
| The Middle East Eye OPEC-lobbying story | **Timing does not fit**: published 17:15 GMT = 12:15 ET, after most of the fall | § 3 |

## 3. WALTER card SIG-W-20261127-002, items in my lane

| Item | Check | Status |
|---|---|---|
| Russia extends jet-fuel export ban to 2027-03-31 | government.ru fetch failed (not retried); English and Russian searches find only the original ban to 2026-11-30 (June decree) and the gasoline/diesel extension to 2027-01-31 (decree 954, 7/30); OSPREY's packet cites a title only | **UNVERIFIED** (no primary read) |
| US lobbied Iraq and Venezuela to exit OPEC (Middle East Eye) | MEE page read: published 2026-11-27 17:15 GMT; the claim rests on "a Reuters report" (sources' number and naming not given); lobbying dated "the summer" / "earlier this year"; Iraq's PM raised withdrawal, the oil ministry opposed it and wanted a higher quota; the Crown Prince "had to directly intervene" to keep Venezuela paying OPEC dues; no government confirmation or denial reported. The Reuters story itself NOT FOUND by search | **SINGLE OUTLET relaying an unread Reuters report; UNVERIFIED** at Reuters |

Barrel meaning, either way: none this month. Venezuela produces little; Iraq is already pressing for a higher capacity rating (search summaries citing Reuters sources, not read: Iraq and Kazakhstan want higher estimates at Sunday's meeting). The story raises the cohesion question for 2027 quotas, not December barrels.

## 4. OSPREY packet (Russian runs; C3 killed)

- C3 3 → 1 (no qualifying tanker strike since 10/6): the tanker-strike channel is not a supply input now; no BRENT row keys on it.
- Runs 2.6–2.7 M bpd at 11/23 (Rystad via Bloomberg via Militarnyi; one-date estimate, relayed twice): supports diesel cracks in principle, but the January diesel crack is $71.61: $23.39 under TERRY's $95 condition and $18.55 under the $90.16 line. The product the runs loss removes is mostly export diesel and fuel oil to Europe and Asia; the US crack is not where it shows first, and ICE gasoil is unread here.
- OSPREY's ask (Bloomberg 4-week seaborne print after 11/8): relay found, 3.9 M bpd 4-week average, week ending 11/15 (Oilprice.com 11/17 from Bloomberg vessel tracking). Replied by packet.

## 5. Forward view (unscored; no row registered)

- **OPEC+ Sunday 11/29 (D:L913):** a hold of quotas through Q1 2027 about 80% (Reuters sources via relays say agreement in principle; my 11/26 figure was 75%). A hold is priced; a surprise either way moves Monday's open more than today did.
- **Brent February (the new front from 12/01):** over the next week I expect it in roughly $86–95, centre about $90; the alternative that matters is another confirmed Saudi Red Sea outlet hit (Yanbu, Rabigh, Jeddah) or a mined-tanker confirmation, which would retest January's $96–97 equivalent (about $92–93 February). A US-Iran mediation headline is the downside branch (about $85). Horizon: to the 12/04 settle.
- **Curve:** M1−M3 on the new pinned pair (BZG27−BZJ27) reads +5.04 on today's vendor daily bars (BZG27 90.52 − BZJ27 85.48) and should hold +4.5 to +5.5 into the first week of December; January's +6.8 is expiry-week squeeze, not a level to carry forward.
- **Diesel crack January:** $68–75 range; a move back above $80 needs a named-contract product event (a European diesel outage or a new Russian product export cut confirmed at a primary). About 10% before 12/21, below my 11/20 figure of 20%, because the crack has not recovered while crude rose 6% in two sessions.
- **What would change my mind:** a Brent-WTI widening above about $10 on the February pair with flat price rising (a Gulf-specific loss), or a weekly EIA distillate build reversal.
