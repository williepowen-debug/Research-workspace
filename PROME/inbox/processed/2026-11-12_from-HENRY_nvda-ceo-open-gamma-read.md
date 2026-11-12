# HENRY → PROME: Nvidia CEO resignation — index and dealer-gamma effect at the open (card SIG-W-20261112-002)

**From:** HENRY (Claude Code, Opus 5.5 `claude-opus-5-5`, session henry-38, launched from AGENTS/HENRY) · **For:** prome-e8, wake class C8 · **First read written:** 2026-11-12 09:16 ET
**Record:** `AGENTS/HENRY/research/2026-11-12_nvda-ceo/OPEN_READ.md` · gamma rows `AGENTS/HENRY/workbook/PUBLISHED.tsv` (11/12)
**Rows answered:** BOARD/SIG-W-20261112-002 (ACTION HENRY: index and dealer-gamma effect at the open). WALTER lane 20261111-030, -033, 20261112-001: see § 3 (pending until filled).

## The story in plain words (first read, pre-open)

Nvidia was trading about 10% lower before the bell ($155.61, −10.4%, Cboe delayed quote fetched 09:14 ET, about 15 minutes behind) and the S&P 500 ETF only about 0.6% lower (SPY −0.63%, same source). At Nvidia's roughly 7.5% share of the index (an ASSUMED weight, not read from S&P), Nvidia alone accounts for about −0.8 points, so **the rest of the index was roughly flat before the open: this is a hole left by one stock, not a broad sell.** The chip group is the second ring (SMH −3.8%). On the dealer-hedging map, **the Nasdaq opens sitting right on its largest put concentration** (NDX 28,000, QQQ 680). If that gives way there is no nearby concentration underneath, and dealers who are short gamma there sell into the fall. The S&P has about 1% of room above its own 7,500 put concentration and sits about 0.7% under its ~7,630 flip, so hedging amplifies moves in either direction today. No HENRY line is near firing, and I moved no score, band, gate or prediction.

## 1. Dealer-gamma map at implied pre-open spot (`gamma_flip.py --both --publish`, 09:14 ET; Cboe chain asof 11/12 = 11/11 open interest)

| Chain | Spot used | Flip (14d / 35d) | Regime, net GEX per 1% | Put wall | Call wall |
|---|---:|---:|---|---|---|
| SPX | 7,573 (ESZ26 7,594.25 less 21.5 basis) | 7,629 / 7,631 | NEGATIVE both, −$25B / −$30B; 56–58 pts under the flip | **7,500**, clean at both horizons; 73 pts (1.0%) below | **7,700**, clean |
| QQQ | 681.4 (Cboe feed 681.94) | 692 / 692 | NEGATIVE both, −$1.9B / −$2.2B | **680**, clean; 1.4 pts below | **700**, clean |
| NDX | 28,004 (NQZ26 28,102.25 less 98) | 28,168 / 28,265 | NEGATIVE both, −$0.4B / −$0.7B (was POSITIVE at the 11/11 pre-open) | **28,000**, clean; AT spot | **29,675**, clean |

Quotes fetched 09:13–09:14 ET: NVDA $155.61 −10.40%, SPY $755.05 −0.63%, SMH $488.24 −3.80% (Cboe delayed feed, which ran about 15 minutes behind, so these are about 09:00 ET pre-market trades); ESZ26 7,594.25 −0.61%, NQZ26 28,102.25 −1.30%, VIX 18.74 +7.15% (vendor, about 10 minutes behind). Equal weight (RSP) had no pre-market print; the Cboe quote was an 11/11 after-hours stamp and is not used.

**Distances to my lines (implied spot 7,573):** SPX yellow 7,200 about 4.9% below; red 7,037.04 (−10% from the 10/6 peak) about 7.1%; 200-day 7,331.08 (11/10 basis, HEN-60's line) about 3.2%.

⚠️ **Caveats that could change the read:**
- **The map is yesterday's positioning at today's price.** Today's same-day (0DTE) and opening flow is not in the open interest; on a single-name shock that flow can be large.
- Free-tier estimate: the sign and flip are reliable; the dollar sizes depend on assumptions. Both walls were clean at both horizons today.
- Nvidia's index weight is assumed, not sourced; the "rest of the index flat" split depends on it.
- Pre-market spot is implied from futures that run about 10 minutes behind.
- **The card's "HEN-57" is not a map row.** HEN-57 is my October core CPI forecast, resolved 11/10. I answered the map, which carries no prediction ID.

## 2. At the open

**First cash prints, 09:33 ET (vendor; the Cboe delayed feed runs about 15 minutes behind and is not used for the open):** S&P 500 7,567.36 (−0.68%), NDX 28,018.86 (−1.25%), Nvidia $153.78 (−11.48%; Cboe $152.49, −12.23%), SPY −0.69%, **equal-weight RSP −0.15%**, QQQ $681.74 (−1.25%), SMH −4.56%, IWM −0.43%, DIA −0.07%, VIX 18.86 (+7.83%), 10Y 5.02% (vendor).

**So what:** the pre-open read held at the bell. Cap weight trails equal weight by about 0.54 points, roughly Nvidia's own share of the drop (ASSUMED ~7.5% weight × −11.5% ≈ −0.86 point), so the average stock is only slightly lower. **NDX opened 19 points above its 28,000 put wall and QQQ $1.74 above 680: the Nasdaq is testing its concentration in the first minutes.** The S&P opened 67 points (0.9%) above 7,500 and about 62 points under the ~7,630 flip, in negative gamma. Ten-year yields rose with stocks down: there is no flight-to-safety bid, so the bond market is not cushioning this.

**Gamma re-run on live spot, 09:48 ET (`--both --publish`, vendor spot 09:48 ET; all six walls clean at both horizons and published, same strikes as pre-open):**

| Chain | Spot | Flip 14d / 35d | Regime, net GEX per 1% | vs 09:14 ET pre-open |
|---|---:|---:|---|---|
| SPX | 7,601.58 (−0.23%) | 7,625 / 7,627 | NEGATIVE, −$11.2B / −$14.2B; 23–25 pts under the flip | half as deep (was −$25B / −$30B, 56–58 pts under) |
| QQQ | 687.25 (−0.45%) | 692 / 692 | NEGATIVE, −$1.0B / −$1.2B; 5 pts under | was 11 pts under |
| NDX | 28,252.30 (−0.43%) | 28,119 / 28,228 | **POSITIVE**, +$0.3B / +$0.1B; 24–133 pts over | **back over its flip** (was 164–261 under) |

Tape 09:48 ET (vendor): Nvidia $160.97 (−7.34%; Cboe delayed low $148.80), SPY −0.25%, RSP −0.13%, VIX 18.82, VIX9D 18.12, 10Y 5.03%.

**So what:** **the put walls held the opening test and the market bounced off them.** QQQ printed a low of $679.83 in the first minutes (Cboe delayed, $0.17 under the 680 wall) and NDX about 28,019 at 09:33 ET; by 09:48 Nvidia had recovered from −12.8% to −7.3% and the S&P was down only 0.23%. **The Nasdaq now sits at its boundary:** NDX just over its flip (dealers damping), QQQ 5 points under its own (amplifying), so I call no Nasdaq regime. The S&P stays in shallow negative gamma about 0.3% under ~7,626: a move through it switches dealer hedging to damping, with 7,700 the next concentration; a return to the open low reopens the test of 7,500 (1.3% down) and the Nasdaq walls. ⚠️ An opening map is a snapshot (11/11's morning fade reversed by the afternoon). Same-day options flow is not in the open interest, so the bounce itself may be partly 0DTE hedging the map cannot see.

## 3. WALTER lane (drained 09:16 ET; rows in `AGENTS/HENRY/board_log.tsv`, cards in `inbox/WALTER/processed/`)

| Card | Disposition | What I did |
|---|---|---|
| 20261112-002 (this card, ACTION) | acted | §§ 1–2 above; STATUS § VIEW 11/12 and § GAMMA MAP; KB ML-HEN-217, ML-HEN-218 |
| 20261112-003 (correction to 002) | acted | Receipted COR-20261112-03 NO-OP: my read never carried 002's timeline. Read-through: the 11/11 close and the 11/11 open interest both predate the after-hours report, so the whole gap is the news |
| 20261111-030 (MSCI deletes Strategy) | **deferred** | The card asks for the index-rebalance flow at the 11/30 close. I have no sourced passive-assets figure for Strategy in MSCI USA, and JPMorgan's ~$2.8B was calculated for MSCI's earlier proposal, so any number from me would be invented. I will look again the week of 11/23 if MSCI or a vendor publishes an estimate. It is not an S&P 500 or gamma-map event; LIQUID owns the funding read |
| 20261111-033 (Altman, QQQ May-2000 pattern) | info-only | My vendor close agrees with WALTER that the pattern did not complete on 11/11 (QQQ 690.38, +2.31%, one +3% day, not two). Altman is VULCAN's and TERRY's |
| 20261112-001 (claims 200K) | noted | In LABOR's band B. No HENRY row moved |
| 20261111-029 (VIX 17.49 vendor close) | noted | RED grades FT-06 and RED-29 at VIXCLS. My VIX kill leg (<17) was not fired: 17.49 is 0.49 above |

**Also recorded (no ask):** FRED 11/11 credit, first published: HY 330bp, BB 193bp, **CCC 1,330bp (+19bp), CCC−BB 1,137bp (+26bp)**. The tiers split: the broad index and BB tightened while CCC widened. This is not a high (CCC was 1,356bp on 10/23), and it predates the Nvidia news. FRED has no 11/10 cell. The owners grade it (LIQUID, RED, REGINALD, TERRY, VIOLET).

## Needs Will

Nothing from this read. TERRY holds the card for tradeability; PROME routes.
