# 2026-11-12 — Nvidia CEO resignation: index and dealer-gamma effect at the open

**Trigger:** WALTER card SIG-W-20261112-002 (IMMEDIATE, ACTION HENRY), PROME wake class C8 from session prome-e8. Fact verified by PROME at the primary (Nvidia 8-K Item 5.02, accession 0001045810-26-000082, EDGAR accepted 08:52 ET 11/12). HENRY did not re-read the 8-K. No reason is given by Nvidia.
**Runtime:** Claude Code, Opus 5.5 (`claude-opus-5-5`), session henry-38. Every stamp below is from `date`.

## 1. First read — pre-open (gamma 09:14 ET; quotes 09:13–09:14 ET)

### Tape (pre-market, not prints of the cash session)

| Instrument | Level | Change vs 11/11 close | Source, time |
|---|---:|---:|---|
| Nvidia (NVDA) | $155.61 | −10.40% (from $173.73) | Cboe delayed quote fetched 09:14 ET (feed about 15 min behind: about 09:00 ET trades) |
| SPY | $755.05 | −0.63% | Cboe delayed, fetched 09:14 ET (about 15 min behind) |
| SMH (chip ETF) | $488.24 | −3.80% | Cboe delayed, fetched 09:14 ET (about 15 min behind) |
| QQQ | $681.94 | −1.22% (own calc on $690.38) | Cboe chain feed price, 09:14 ET |
| ES Dec (ESZ26) | 7,594.25 | −0.61% | vendor, read 09:13 ET, runs about 10 min behind |
| NQ Dec (NQZ26) | 28,102.25 | −1.30% | vendor, read 09:13 ET, about 10 min behind |
| VIX | 18.74 | +7.15% | vendor, 09:13 ET |
| RSP (equal weight) | not usable | — | Cboe quote stamped 01:38Z, an after-hours print from 11/11; no pre-market read |

**Index arithmetic (ASSUMED weight, not sourced):** at about 7.5% of the S&P 500, Nvidia −10.4% alone is about −0.78 points of index return. SPY −0.63% then implies the other ~92% of the index is roughly flat to +0.15%. Read: **a single-name hole in the index, not a broad sell.** The chip complex is the second ring (SMH −3.8%; the card relays Nebius about −16%, CoreWeave about −10%). Equal-weight confirmation waits for the cash open.

### Dealer-gamma map at implied spot (`gamma_flip.py --both --spot … --publish`, 09:14 ET; chain asof 11/12 = 11/11 open interest)

Implied spot = futures less the 11/11 close basis: SPX 7,573 (ESZ26 7,594.25 − 21.5); NDX 28,004 (NQZ26 28,102.25 − 98); QQQ 681.4 (scaled from NQ −1.30%; Cboe feed 681.94 agrees).

| Chain | Spot used | Flip 14d / 35d | Net GEX per 1% 14d / 35d | Regime | Put wall | Call wall |
|---|---:|---:|---:|---|---|---|
| SPX | 7,573 | 7,629 / 7,631 | −$25.2B / −$30.4B | NEGATIVE both, 56–58 pts (0.7%) under the flip | **7,500**, clean both (+28% / +24%), 73 pts (1.0%) under spot | **7,700**, clean both |
| QQQ | 681.4 | 692 / 692 | −$1.9B / −$2.2B | NEGATIVE both, 11 pts (1.6%) under | **680**, clean both (+22% / +29%), 1.4 pts under spot | **700**, clean both |
| NDX | 28,004 | 28,168 / 28,265 | −$0.4B / −$0.7B | NEGATIVE both (was POSITIVE at the 11/11 pre-open) | **28,000**, clean both (+28% / +41%), AT spot | **29,675**, clean both |

All six walls passed the cross-horizon check and are published (`workbook/PUBLISHED.tsv`, 11/12 rows).

### So what

1. **Nasdaq opens ON its put wall** (NDX 28,000, QQQ 680). That strike is the nearest large concentration of open interest; dealers short gamma below the flip sell into weakness. A trade under 28,000 / 680 leaves no published concentration until well lower, so the move can extend on hedging alone. Holding it is the first test.
2. **The S&P has about 1% of room to its 7,500 put wall** and opens about 0.7% under its ~7,630 flip, in the same negative zone as the 11/11 open (spot 7,575 then, flip 7,621–7,624). Under 7,500 is the deep-negative zone of 11/10 (the 11/10 close-spot read was −$43.8B per 1%).
3. **Dealers amplify both ways today.** A recovery through ~7,630 (S&P) and ~28,200 (NDX) would turn hedging to damping; nothing on the map says that is likely at the open.
4. **No HENRY line is near firing:** SPX yellow 7,200 is about 4.9% below implied spot; red 7,037.04 (−10% from the 10/6 peak) about 7.1%; the 200-day (7,331.08 on the 11/10 basis, HEN-60's line) about 3.2%. No prediction, score or band moved.

### Caveats that travel with this read

- **Today's 0DTE and opening flow are not in the chain** (open interest is 11/11's). The map is yesterday's positioning at today's price.
- Free-tier proxy: the sign and flip are robust; the $B figures assume dealers are long calls and short puts and are not SpotGamma-grade. Walls are the fragile part (both clean here).
- Implied spot carries a few points of basis error and the vendor futures run about 10 minutes behind.
- The Nvidia weight is ASSUMED (about 7.5%), not read from an index provider; the "rest of the index flat" split is arithmetic on that assumption.
- Cboe's chain carries IV = 0 for about 15 minutes after 09:30 ET; the opening re-run waits until about 09:47 ET.
- **"HEN-57" on the card is not a map row.** HEN-57 is my October core CPI forecast, resolved 11/10 (NOT FIRED, core +0.3%). The gamma map has no prediction ID; I answered the map.

## 2. At the open (09:33 ET prints, 09:48 ET gamma re-run)

**09:33 ET (vendor; the Cboe delayed feed is about 15 minutes behind and not used for the open):** SPX 7,567.36 (−0.68%), NDX 28,018.86 (−1.25%), NVDA $153.78 (−11.48%; Cboe $152.49), SPY −0.69%, RSP −0.15%, QQQ $681.74, SMH −4.56%, IWM −0.43%, DIA −0.07%, VIX 18.86, 10Y 5.02%. Cap weight trailed equal weight by about 0.54pt, roughly Nvidia's own share (ASSUMED weight). NDX opened 19 pts over its 28,000 put wall.

**09:48 ET (vendor):** SPX 7,601.58 (−0.23%), NDX 28,252.30 (−0.43%), QQQ 687.25, NVDA $160.97 (−7.34%), SPY −0.25%, RSP −0.13%, VIX 18.82, VIX9D 18.12, 10Y 5.03%. Cboe delayed lows in the first minutes: QQQ 679.83, NVDA 148.80, SPY 753.67. Note: Cboe "delayed" quotes ran about 15 minutes behind after the open (last trade 09:31 at a 09:46 stamp); the pre-open Cboe quotes are delayed the same way.

| Chain (`--both --publish`, 09:48 ET) | Spot | Flip 14d / 35d | Regime, net GEX per 1% | Walls |
|---|---:|---:|---|---|
| SPX | 7,601.6 | 7,625 / 7,627 | NEGATIVE, −$11.2B / −$14.2B, 23–25 pts under | 7,500 put (+19% / +15%), 7,700 call, clean both |
| QQQ | 687.25 | 692 / 692 | NEGATIVE, −$1.0B / −$1.2B, 5 pts under | 680 put, 700 call, clean both |
| NDX | 28,252 | 28,119 / 28,228 | POSITIVE, +$0.3B / +$0.1B, 24–133 pts over | 28,000 put, 29,675 call, clean both |

**Read:** the put walls held the opening test (QQQ $0.17 under 680 at the low) and the tape bounced; Nvidia halved its loss. Nasdaq at the boundary (NDX over its flip, QQQ under): no regime called. S&P shallow negative, about 0.3% under the flip. Snapshot caveat: the 11/11 opening read reversed by the afternoon. Wall rows hand-written to `PUBLISHED.tsv` (the script writes flips and GEX only, and overwrote the 09:14 ET flip rows with the 09:48 ET run; the pre-open figures live in § 1 and KB ML-HEN-217).

## 3. Flip cross (watcher fired 11:08:48 ET; gamma 11:09 ET, published)

**Trigger:** background watcher on vendor ^GSPC (120 s poll) fired `FLIP-CROSS SPX 7637.08 at 11:08:48`. **11:09 ET (vendor):** SPX 7,639.62 (+0.27%), NDX 28,477.24 (+0.36%), QQQ $692.77 (+0.35%), NVDA $166.74 (−4.02%), SPY +0.25%, RSP −0.13%, VIX 17.86 (+2.12%).

| Chain (`--both --publish`, 11:09 ET) | Spot | Flip 14d / 35d | Regime, net GEX per 1% | Walls |
|---|---:|---:|---|---|
| SPX | 7,639.6 | 7,632 / 7,634 | **POSITIVE** both, +$3.6B / +$3.5B, 6–8 pts over | 7,500 put still #1 at both but a NEAR-TIE (14d +4%, 35d +1%): band **7,500–7,600**; 7,700 call clean both |
| QQQ | 692.77 | 693 / 693 | **SIGN SPLIT** (14d +$0.0B, 35d −$0.1B): on the flip, no regime called | 680 put, 700 call, clean both |
| NDX | 28,477 | 28,176 / 28,274 | **POSITIVE** both, +$0.8B / +$0.6B, 203–301 pts over | 28,000 put, 29,675 call, clean both |

(Published values; a first unpublished run 30 s earlier read SPX flip 7,632 / 7,633, +$3.7B / +$3.6B. Contract counts move between pulls.)

**Read change:** the S&P map turned from shallow NEGATIVE (09:48) to marginal POSITIVE: dealer hedging now damps moves rather than amplifying them. **It is only just:** spot is about 0.1% over an estimated level; a 10-point dip reverses it. The put wall at 7,500 lost its clean margin at this spot (gamma at a strike depends on spot), so the support quote is now a band. The recovery is cap-weighted with Nvidia still −4% and equal weight −0.13%: large names other than Nvidia carried it (combo: narrow-rebound-or-broadening). No HENRY line is near firing; no prediction, score or band moved.

## 4. Close-hour re-read (Will asked 15:35 ET; gamma 15:36 ET, published)

**15:36 ET (vendor):** SPX 7,589.31 (−0.39%), NDX 28,229.42 (−0.51%), QQQ $686.63 (−0.54%), NVDA $163.31 (−6.00%), RSP −0.72%, IWM −1.61%, SMH −1.61%, KRE $72.46 (−0.68%), HYG −0.42%, VIX 18.65 (+6.63%), VIX3M 20.02 (contango), 10Y 5.10%, 30Y 5.43%, USD/JPY 159.84 (+0.06%). Open-low watcher (≤7,570) had not fired.

| Chain (`--both --publish`, 15:36 ET, vendor spot) | Spot | Flip 14d / 35d | Regime, net GEX per 1% | Walls |
|---|---:|---:|---|---|
| SPX | 7,589.3 | 7,632 / 7,634 | **NEGATIVE** both, −$20.7B / −$25.4B, 43–45 pts under | 7,500 put **clean #1 again** (14d +21%, 35d +17%); 7,700 call clean both |
| QQQ | 686.63 | 692.92 / 693.17 | **NEGATIVE** both, −$1.4B / −$1.6B, about 6 pts under | 680 put, 700 call, clean both |
| NDX | 28,229 | 28,173 / 28,271 | **SIGN SPLIT** (14d +$0.1B, 35d −$0.1B): inside the flip band, no regime called | 28,000 put, 29,675 call, clean both |

**Read change vs 11:09:** the S&P map went from marginal POSITIVE (+$3.6B, 6–8 pts over) to clearly NEGATIVE (−$21B to −$25B, about 0.6% under the flip). Dealer hedging amplifies into the close and tomorrow's PPI open. The 7,500 put wall is clean again at this spot, so it is a strike rather than a band: 89 pts (1.2%) below, with the 7,567 open low in between. **Breadth turned:** at 11:09 cap weight led equal weight; now RSP −0.72% and IWM −1.61% trail SPX −0.39%. The selling has spread past Nvidia (combo theme narrow-rebound-or-broadening now reads broadening DOWN). **Caveats:** $B is assumption-dependent; the map is 11/11 open interest at today's price; MOC flow is not in it. No HENRY line is near firing (SPX 389 pts over its 7,200 yellow line); no prediction, score or band moved.
