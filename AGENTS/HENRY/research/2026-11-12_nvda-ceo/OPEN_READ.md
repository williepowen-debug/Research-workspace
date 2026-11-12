# 2026-11-12 — Nvidia CEO resignation: index and dealer-gamma effect at the open

**Trigger:** WALTER card SIG-W-20261112-002 (IMMEDIATE, ACTION HENRY), PROME wake class C8 from session prome-e8. Fact verified by PROME at the primary (Nvidia 8-K Item 5.02, accession 0001045810-26-000082, EDGAR accepted 08:52 ET 11/12). HENRY did not re-read the 8-K. No reason is given by Nvidia.
**Runtime:** Claude Code, Opus 5.5 (`claude-opus-5-5`), session henry-38. Every stamp below is from `date`.

## 1. First read — pre-open (gamma 09:14 ET; quotes 09:13–09:14 ET)

### Tape (pre-market, not prints of the cash session)

| Instrument | Level | Change vs 11/11 close | Source, time |
|---|---:|---:|---|
| Nvidia (NVDA) | $155.61 | −10.40% (from $173.73) | Cboe delayed quote, stamp 14:14:14Z = 09:14 ET |
| SPY | $755.05 | −0.63% | Cboe delayed, 09:14 ET |
| SMH (chip ETF) | $488.24 | −3.80% | Cboe delayed, 09:14 ET |
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

## 2. Opening re-run

(pending: after about 09:47 ET)
