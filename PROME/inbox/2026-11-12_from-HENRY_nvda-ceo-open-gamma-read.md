# HENRY → PROME: Nvidia CEO resignation — index and dealer-gamma effect at the open (card SIG-W-20261112-002)

**From:** HENRY (Claude Code, Opus 5.5 `claude-opus-5-5`, session henry-38, launched from AGENTS/HENRY) · **For:** prome-e8, wake class C8 · **First read written:** 2026-11-12 09:16 ET
**Record:** `AGENTS/HENRY/research/2026-11-12_nvda-ceo/OPEN_READ.md` · gamma rows `AGENTS/HENRY/workbook/PUBLISHED.tsv` (11/12)
**Rows answered:** BOARD/SIG-W-20261112-002 (ACTION HENRY: index and dealer-gamma effect at the open). WALTER lane 20261111-030, -033, 20261112-001: see § 3 (pending until filled).

## The story in plain words (first read, pre-open)

Nvidia was trading about 10% lower before the bell ($155.61, −10.4%, Cboe delayed quote 09:14 ET) and the S&P 500 ETF only about 0.6% lower (SPY −0.63%, same source). At Nvidia's roughly 7.5% share of the index (an ASSUMED weight, not read from S&P), Nvidia alone accounts for about −0.8 points, so **the rest of the index was roughly flat before the open: this is a hole left by one stock, not a broad sell.** The chip group is the second ring (SMH −3.8%). On the dealer-hedging map, **the Nasdaq opens sitting right on its largest put concentration** (NDX 28,000, QQQ 680). If that gives way there is no nearby concentration underneath, and dealers who are short gamma there sell into the fall. The S&P has about 1% of room above its own 7,500 put concentration and sits about 0.7% under its ~7,630 flip, so hedging amplifies moves in either direction today. No HENRY line is near firing, and I moved no score, band, gate or prediction.

## 1. Dealer-gamma map at implied pre-open spot (`gamma_flip.py --both --publish`, 09:14 ET; Cboe chain asof 11/12 = 11/11 open interest)

| Chain | Spot used | Flip (14d / 35d) | Regime, net GEX per 1% | Put wall | Call wall |
|---|---:|---:|---|---|---|
| SPX | 7,573 (ESZ26 7,594.25 less 21.5 basis) | 7,629 / 7,631 | NEGATIVE both, −$25B / −$30B; 56–58 pts under the flip | **7,500**, clean at both horizons; 73 pts (1.0%) below | **7,700**, clean |
| QQQ | 681.4 (Cboe feed 681.94) | 692 / 692 | NEGATIVE both, −$1.9B / −$2.2B | **680**, clean; 1.4 pts below | **700**, clean |
| NDX | 28,004 (NQZ26 28,102.25 less 98) | 28,168 / 28,265 | NEGATIVE both, −$0.4B / −$0.7B (was POSITIVE at the 11/11 pre-open) | **28,000**, clean; AT spot | **29,675**, clean |

Live quotes (09:13–09:14 ET): NVDA $155.61 −10.40%, SPY $755.05 −0.63%, SMH $488.24 −3.80% (Cboe delayed); ESZ26 7,594.25 −0.61%, NQZ26 28,102.25 −1.30%, VIX 18.74 +7.15% (vendor, about 10 minutes behind). Equal weight (RSP) had no pre-market print; the Cboe quote was an 11/11 after-hours stamp and is not used.

**Distances to my lines (implied spot 7,573):** SPX yellow 7,200 about 4.9% below; red 7,037.04 (−10% from the 10/6 peak) about 7.1%; 200-day 7,331.08 (11/10 basis, HEN-60's line) about 3.2%.

⚠️ **Caveats that could change the read:**
- **The map is yesterday's positioning at today's price.** Today's same-day (0DTE) and opening flow is not in the open interest; on a single-name shock that flow can be large.
- Free-tier estimate: the sign and flip are reliable; the dollar sizes depend on assumptions. Both walls were clean at both horizons today.
- Nvidia's index weight is assumed, not sourced; the "rest of the index flat" split depends on it.
- Pre-market spot is implied from futures that run about 10 minutes behind.
- **The card's "HEN-57" is not a map row.** HEN-57 is my October core CPI forecast, resolved 11/10. I answered the map, which carries no prediction ID.

## 2. At the open

**First cash prints, 09:33 ET (vendor; Cboe 09:31 ET agrees within a few cents):** S&P 500 7,567.36 (−0.68%), NDX 28,018.86 (−1.25%), Nvidia $153.78 (−11.48%; Cboe $152.49, −12.23%), SPY −0.69%, **equal-weight RSP −0.15%**, QQQ $681.74 (−1.25%), SMH −4.56%, IWM −0.43%, DIA −0.07%, VIX 18.86 (+7.83%), 10Y 5.02% (vendor).

**So what:** the pre-open read held at the bell. Cap weight trails equal weight by about 0.54 points, roughly Nvidia's own share of the drop (ASSUMED ~7.5% weight × −11.5% ≈ −0.86 point), so the average stock is only slightly lower. **NDX opened 19 points above its 28,000 put wall and QQQ $1.74 above 680: the Nasdaq is testing its concentration in the first minutes.** The S&P opened 67 points (0.9%) above 7,500 and about 62 points under the ~7,630 flip, in negative gamma. Ten-year yields rose with stocks down: there is no flight-to-safety bid, so the bond market is not cushioning this.

**Gamma re-run on live spot:** (pending, about 09:48 ET; Cboe's chain carries zero implied volatility for about 15 minutes after the open)

## 3. WALTER lane

(pending)

## Needs Will

Nothing from this read. TERRY holds the card for tradeability; PROME routes.
