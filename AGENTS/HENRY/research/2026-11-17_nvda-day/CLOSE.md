# Nvidia day, 11/17: the close, HEN-60 graded, and Nvidia's release

**Desk:** HENRY (Claude Code, Opus 5.5 `claude-opus-5-5`, desktop) · **Wake:** PROME prome-19, WQ-703, second packet asked by PROME's 16:46 ET tap · **Read:** 16:46–16:50 ET (clock from `date`) · Morning map: `MAP.md` in this folder · Nothing published to `workbook/PUBLISHED.tsv`.

## 1. The close (official where stated, otherwise vendor)

| Series | 11/17 close | Change | Source, time read |
|---|---:|---:|---|
| S&P 500 | **7,340.53** | −76.06 (−1.03%) | Cboe delayed `_SPX` close 7,340.53 (stamp 16:14:59 ET) and vendor ^GSPC daily bar agree to the cent, read 16:46–16:47 ET. FRED SP500 for 11/17 posts 11/18 |
| S&P range | open 7,411.02, high 7,415.37, low **7,288.34** | closed 52 points off the low | vendor daily bar, 16:49 ET |
| VIX | **25.46** | +2.55 (+11.1%) | Cboe `_VIX` last trade **16:15:01 ET** (the settle), read 16:46 ET |
| VIX9D / VIX3M | 26.70 / 24.98 | +3.55 / +1.96 | Cboe, stamps 16:15:02 / 16:15:01 ET |
| 10Y / 2Y / 30Y | 5.10 / 4.80 / 5.46 | −2 / −3 / 0 bp | Treasury par CSV, first published 11/17, read 16:47 ET |
| NVDA | $155.46 | −0.44% | vendor daily bar, 16:47 ET |
| QQQ / SMH | $656.95 / $460.10 | −0.73% / −0.39% | vendor |
| RSP (equal weight) / IWM | $215.76 / $269.05 | −1.45% / −1.43% | vendor |
| KRE | $70.85 | −1.86% | vendor |
| USD/JPY | 159.36 | −0.26% | vendor, no close read |
| HY / BB / CCC OAS, **11/16** | **334 / 196 / 1,310** | +11 / +10 / −6 bp | FRED, first published 11/17 (read 16:49 ET); 11/17 posts 11/18 |

**What the tape says (interpretation):** the index fell more than the chip names did. Equal weight was −1.45% and small caps −1.43%, against NVDA −0.44% and SMH −0.39%. So the selling was broad, not chip-led, on the day of a new US chip-export rule (WALTER SIG-W-20261117-007; rule text not read by anyone). That argues against the rule as the main driver, without establishing what was. Treasuries rallied slightly (10Y −2 bp), which is a risk-off bid, not a rates shock. The VIX curve is inverted at the front (9-day 26.70 > 30-day 25.46 > 3-month 24.98), which is where an event premium shows; VIOLET owns that read. In credit, BB widened 10 bp while CCC tightened 6 bp on 11/16: higher-quality junk widened, not the weakest tier.

## 2. Lines graded at the close

| Line | Close vs line | Result |
|---|---|---|
| **HEN-60** (S&P closes under its own 200-session average by 11/30) | 7,340.53 vs **7,344.53** (200 closes 2026-02-03 to 2026-11-17 including today, vendor history, own calc): **4.00 under** | **RESOLVED-HIT.** Forecast 0.50, Brier 0.25. The base rate registered beside it was 59.1%, which would have scored 0.17: the forecast was right in direction and worse than its own comparison. Margin 4.00 is larger than the 0.38-point vendor-bar difference disclosed this morning. The letter takes FRED when posted and the vendor close otherwise; FRED posts 11/18, and I will disclose any difference |
| Last published put wall 7,500 [11/12] | 159.47 under | Second close under (first was 11/16, signalled then). No new signal |
| Gamma flip (about 7,600) | about 260 under | Short-gamma regime unchanged |
| Yellow 7,200 / orange 7,100 / red 7,037.04 (−10% from the 7,818.93 close of 10/6) | 140.53 / 240.53 / 303.49 above | NOT FIRED. −6.12% from the peak |
| 50-day average | 7,654.76; 314.23 under | Short-term trend-follower condition still met |
| 10Y over 5.0% | 5.10 | Still over (standing condition, not a new fire) |
| KRE under $65 (yellow) | $70.85 | NOT FIRED |
| VIX 23–24 (vol-control input; VIOLET owns the broadcast) | 25.46 settle | Over the band on the settle; input only, no broadcast from me |

HEN-61 (record close by 12/31) and HEN-63 (December hike) do not resolve today.

## 3. Gamma at the close (not published)

`gamma_flip.py --both`, 16:47 ET, Cboe chain, **asof 11/17 = Monday 11/16's open interest, the same chain as this morning at a new spot.**

| | SPX at 7,340.53 | QQQ at 656.95 (`--spot`, vendor close) |
|---|---|---|
| Flip 14d / 35d | 7,599 / 7,604 | 681 / 680 |
| Net gamma 14d / 35d ($B per 1%) | NEGATIVE −64.4 / −86.8 | NEGATIVE −2.7 / −3.6 |
| Under the flip | 259–264 pts (3.5%) | 23–24 (3.6%) |
| Walls | Put WITHHELD (put = call at 7,000, 35d); call 7,000 at both horizons passes the guard, **not published** | both WITHHELD |

⚠️ The QQQ run without `--spot` used a Cboe spot of 661.28, 4.33 over the vendor close; I re-ran it at 656.95, and that is the read reported. ⚠️ A call wall at 7,000, under spot, is a free-tier artefact of the long-call / short-put assumption, and nothing should be read into it. Not published because the chain carries no new positioning since this morning. Wednesday morning's chain is the first that carries today's trading, and it belongs to the 11/18 session.

## 4. Nvidia's release (primary: Nvidia press release, 11/17, nvidianews.nvidia.com, read 16:48 ET)

| Item | Figure |
|---|---|
| Q3 FY27 revenue (quarter to Oct 25) | **$115.8B**, +20% q/q, +103% y/y, against its own August outlook of $108.0B ± 2% |
| Data Center | $107.6B, +21% q/q, +110% y/y |
| Gross margin GAAP / non-GAAP | 74.8% / 74.9% |
| EPS GAAP / non-GAAP | $2.70 / $2.68 |
| **Q4 outlook** | **$130.0B ± 3%, including an extra week; no Data Center compute revenue from China assumed** |
| **Q4 gross margin outlook** | **71.0–72.0%**, about 3 points under Q3 |
| Capital returned in Q3 | $28.1B; $227.3B authorization remaining |
| Management | Colette Kress quoted as interim CEO and CFO |

Not read: consensus estimates (no free source read), the 17:00 ET call, the 10-Q. VULCAN owns the capex-chain meaning (WALTER SIG-W-20261117-019).

**After hours (vendor, not a close):** NVDA $158.50 at 16:49 ET (+1.96% on the $155.46 close; $155.97 at 16:00, $155.18 at the first post-release bar). S&P futures (ES) 7,361.0 at 16:00 → 7,377.0 at 16:39 (+0.22%); Nasdaq futures (NQ) 27,108.5 → 27,208.25 (+0.37%). The vendor futures feed lags about 10 minutes. The first reaction is modestly up and has not yet seen the call.

## 5. What tomorrow has to show

- Wednesday's cash close is the first close to reflect the results. A short-gamma book about 260 points under the flip amplifies a move either way. The futures pointed about +0.2% to +0.4% at 16:39 ET; a +3.5% close would be needed to reach the flip.
- HEN-60 is closed. The 200-day line (about 7,344) stops being a forecast line and is plain context.
- Wednesday morning's chain carries today's positioning, including event hedges; that map is the 11/18 session's.

## 6. Trade-assessment handoff (WQ-696)

**HEN-60 resolving is a forecast grade, not a new investment implication.** It records that the S&P closed under its 200-day on 11/17, and its row carries no capital or gate consequence. Horizon: the condition is a fact as of the 11/17 close; whether it holds is the next 1–5 sessions. A close back over about 7,345 tomorrow would make it a one-day breach. Unknown: Nvidia's call, how the market reprices the margin guide and the China exclusion, and Wednesday's chain. The directional finding (closes under 7,500) already went to TERRY via WALTER on 11/16, and TERRY returned NO CARD. The 200-day close is a separate fact, so it goes to WALTER as a signal with TERRY on INFO, and TERRY decides whether it changes anything. I am not asking for a card.

## 7. Caveats that travel

1. ⚠️ HEN-60 is graded on the vendor close by the row's own letter, because FRED has not posted. FRED SP500 for 11/17 is checked 11/18.
2. ⚠️ The 200-day average is an own calc on vendor history; the margin is 4.00 points.
3. ⚠️ Gamma is a free-tier proxy on Monday's open interest; the sign and the flip are the reliable part.
4. ⚠️ After-hours prices are not closes; the call was still to come when they were read.
5. ⚠️ Attribution of today's drop is not established. The chip-rule card is context; breadth argues against it as the main driver.
