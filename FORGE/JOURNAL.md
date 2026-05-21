# FORGE — Trade Journal

*Every entry, exit, and decision. The record.*

---

## Reconstruction Gap — Feb 27 to May 21, 2026

> **Acknowledged gap.** Trades opened, closed, and rolled between the Feb 27 entries below and the 5/21 Fidelity CSV snapshot were not journaled in real time. The list below was reconstructed from `FORGE/STATUS.md` (Mar 25 vintage) + Fidelity CSV diff (May 21) + SAM TRADE.md v1.4. **No per-trade P&L is reconstructable** — entry and exit prices for these events are not in the available sources. Listed here for audit-trail completeness; for current positions see `STATUS.md`.

### Equity closures (no exit prices recoverable)

- **AAPL** — Trimmed 100 → 80 (per Mar STATUS, between Feb 27 and Mar 25), then trimmed 80 → 30 (between Mar 25 and May 21). ~70 shares total proceeds, prices unknown.
- **SLV** — 5 of 10 shares trimmed Mar 9 @ $76.71 (-17%) per Mar STATUS; remaining 5 closed Mar 25 → May 21 at unknown price.
- **SLVP** — 3 shares closed Mar 25 → May 21.
- **USO** — 1 of 3 shares trimmed Feb 27 @ $81.99 (+17%); remaining shares closed Mar 25 → May 21 (USO LP also exited per Mar STATUS).
- **GOOG** — 1 share closed Mar 9 @ $295.68 (-11.5%); any further GOOG activity unknown.
- **OKLO** — 3 shares closed Mar 9 @ $56.70 (-37.4%).
- **PALL** — 1 share closed Mar 9 @ $149.57 (-7%); any subsequent activity unknown.
- **AMH** — 6 shares closed Mar 9 @ $29.42 (flat).
- **RKLB** — 2 shares closed Feb 27 @ $65.51 (-32%).
- **PLTR** — 1 share closed Feb 27 @ $134.59 (-15%).
- **GLD, GDX, PPLT, CPER, XAR, ITA, INVH (remaining), CEPT, UMAC, STNG** — All closed Mar 6 → May 21, exit prices unknown.

### Options expired worthless

- **USO $118C Mar 27** × 1 — Expired Mar 27 (was at -89% on Mar 25)
- **OWL $9.5P Apr 2** × 1 — Expired Apr 2 (replaced via roll to OWL $9.5P Jun 05 × 2)
- **APO $100P Apr 17** × 1 — Expired Apr 17 (was at -55% on Mar 25)
- **SOFI $16P May 1** × 2 — Expired May 1 (replaced via roll to SOFI $16P Jun 05 × 1)
- **OZK $42.5P May 15** × 2 — Expired May 15 (replaced via roll to OZK $42.5P Jul 17 × 2)
- **TLT $88P May 15** × 2 — **Disposition unknown.** Was at +100% on Mar 25 with "sell decision pending Will." Absent from 5/21 CSV. Either closed at some point between Mar 25 and May 15 (P&L unknown) or expired worthless. **Worth checking with RED/Will if it matters for taxes/performance.**

### Options trim (no exit prices)

- **HYG $75P Jun 18** × 10 → × 8 (trimmed by 2 between Feb 27 and Mar 25 per Mar STATUS); current = 8 contracts at -90%.
- **KRE $60P Jun 18** × 2 → × 1 (trimmed by 1 between Mar 25 and May 21).
- **AAL** — Restructured 4 Jul → 2 Jul + 2 Jun (per Mar STATUS), then current = 2 Jun + 1 Jul.

### Options opens — no documented entry thesis or fill price

The 5/21 CSV shows these positions present that were not in Mar 25 STATUS:

- KRE $60P Aug 21 × 3 @ $2.70 avg
- WAL $65P Jul 17 × 1 @ $4.36
- HBAN $16P Oct 16 × 4 @ $0.96
- FITB $45P Jun 18 × 2 @ $0.91
- CCL $25P Jul 17 × 2 @ $1.96
- DIS $90P Jul 17 × 2 @ $1.99
- IWM $257P Jun 18 × 1 @ $9.39
- QQQ $698P May 21 × 1 @ $3.82 (expires 5/21 at $0.01)
- XLE $65C Sep 30 × 2 @ $2.28
- USO $155C Jun 12 × 1 @ $10.08 (roll from Mar 27 $118C)
- OWL $9.5P Jun 05 × 2 @ $0.59 (roll from Apr 2 $9.5P)
- SOFI $16P Jun 05 × 1 @ $0.71 (roll from May 1 $16P)
- OZK $42.5P Jul 17 × 2 @ $1.02 (roll from May 15 $42.5P)

### Equity opens

- **APD** — 2 shares @ $294.79 avg cost. Thesis unknown to FORGE/PROME.
- **FXY** — Tranche 1: 8 shares @ ~$57.36 (entry date unknown from sources). Tranche 2: 5 shares @ $57.66 (executed 5/21 ~12:46 ET per SAM v1.4). Total 13 shares; blended $58.32 per Fidelity, $57.48 per SAM (minor drift).
- **FXY $58C Jun 18** — 1 contract @ $0.40 per SAM v1.4 (executed 5/21). **Not in 5/21 2:03 PM Fidelity CSV — reconciliation pending.**

### Roll patterns confirmed

| From | To | Reason |
|---|---|---|
| USO $118C Mar 27 | USO $155C Jun 12 | Continued oil-up thesis after Mar expiry |
| OWL $9.5P Apr 2 | OWL $9.5P Jun 05 × 2 | Roll out + add (1→2) |
| SOFI $16P May 1 × 2 | SOFI $16P Jun 05 × 1 | Roll out + size reduction |
| OZK $42.5P May 15 × 2 | OZK $42.5P Jul 17 × 2 | Roll out, same size |

---

## Closed Positions

### Mar 9, 2026 (NFP red day — partial book trim)

*(Surfaced from FORGE/STATUS.md Mar 25 "Positions Closed Since Last Update" section; moved here during 5/21 rehab.)*

| Date | Trade | Entry | Exit | P/L | Return |
|------|-------|-------|------|-----|--------|
| Mar 9 | SSB $90P Jun | $1.87 | $5.45 | +$358 | +191% |
| Mar 9 | GOOG 1 share | $334 | $295.68 | -$38 | -11.5% |
| Mar 9 | OKLO 3 shares | $90.78 | $56.70 | -$102 | -37.4% |
| Mar 9 | AMH 6 shares | ~$29.50 | $29.42 | ~-$5 | flat |
| Mar 9 | SLV 5 shares | ~$91 | $76.71 | ~-$80 | -17% |
| Mar 9 | PALL 1 share | ~$161 | $149.57 | ~-$11 | -7% |

### Feb 27, 2026

| Ticker | Action | Qty | Price | Proceeds | P/L | Notes |
|--------|--------|-----|-------|----------|-----|-------|
| KRE $62P Mar | Sell to Close | 2 | $1.32 | $262.65 | +14% | Rolling out of Mar expiry |
| FXY | Sell | 4 | $58.90 | $235.60 | ~flat | Closed yen thesis |
| FXY | Sell | 10 | $58.87 | $588.70 | ~flat | Closed yen thesis |
| USO | Sell | 1 | $81.99 | $81.99 | +17% | Trimmed to 2 shares |
| RKLB | Sell | 2 | $65.51 | $131.02 | -32% | Cut loser |
| PLTR | Sell | 1 | $134.59 | $134.59 | -15% | Cut loser |
| PALL | Sell | 1 | $162.00 | $162.00 | +1% | Closed |

**Pending (not filled):**
- KRE $60P Dec — limit $4.60 (open)
- VLY $10P Mar — 5 contracts @ $0.10 (open)

---

## Historical Exits

*(Add as trades close. Oldest at bottom.)*

