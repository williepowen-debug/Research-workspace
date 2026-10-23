# France bond market deep dive — 2026-10-22 (hans-1022), the night before Moody's

**Question (Will, in-session):** beyond the 10Y benchmark, what is the French bond market telling us — credit or supply, near or far, orderly or seizing, and where does the ECB act?
**Basis:** vendor closes 10/22 unless dated. Governing T-10 basis = ideal-investisseur (i-i). Everything else is a cross-check. **No primary AFT read** (aft.gouv.fr returns 403 to both WebFetch and curl); auction figures are the AFT press-release text as surfaced by search, flagged as such.

## 1. The answer in four lines

1. **It is France cheapening, not Germany richening.** Measured against euro swaps, the OAT widened ~40bp in 4 sessions; the Bund's position against swaps did not move. The whole OAT–Bund widening is French.
2. **Default insurance moved too, so it is not only supply.** 5Y CDS ~57bp [9/26] → ~81 [10/2] → ~86–90 [10/20–21] (secondaries). A pure supply/positioning shock widens the bond against swaps and leaves CDS alone. Both moved.
3. **The stress sits in the 3–10Y belly, which is the 2027 election window, not the long end.** 10/22 French moves: 5Y +10bp, 7Y +9bp, 30Y +2bp. That's not the long-end term-premium story.
4. **The primary market is still clearing.** October auctions covered 2.0–3.0×. Liquidity is the weak point: Allianz put market depth >50% below normal on 10/9.

## 2. Curve — France vs Germany, TradingEconomics 10/22

| Tenor | France | Germany | FR–DE | FR day | DE day | FR month |
|---|---|---|---|---|---|---|
| 3M | 2.77 | 2.54 | 23bp | +0.7bp | +1.1bp | +3.9bp |
| 2Y | 3.78 | 3.01 | **77bp** | +6.1bp | −7.0bp | +16.3bp |
| 5Y | 4.46 | 3.12 | **134bp** | **+10.0bp** | −8.3bp | +39.2bp |
| 7Y | 4.69 | 3.22 | 147bp | +9.1bp | −8.2bp | +41.3bp |
| 10Y | 5.08 | 3.33 | 175bp | ⚠️ cell reads +0.03bp (page conflict; its own text says +7bp) | −8.4bp | +43.2bp |
| 30Y | 5.54 | 3.68 | 186bp | +2.4bp | −8.2bp | +32.3bp |

- **Germany moved in parallel:** −7 to −8bp at every tenor. That's a flight-to-quality bid, not a German story.
- **France moved most in the 5–7Y belly.** French 2s10s ≈ 130bp vs German ≈ 32bp. The French curve is steep because of credit, not term premium.
- ⚠️ This is a single vendor, and TE's 10Y daily-change cell contradicts its own text. Treat the tenor *shape* as reliable and individual day changes as ±2bp.

## 3. Credit or supply? The swap decomposition (the key test)

EUR 10Y Euribor swap: **3.481 [10/22]**, 3.532 [10/21], 3.543 [10/16] (Investing.com). BlueGamma gives 3.48 / 3.54 / 3.52, which agrees within 2bp.

| | 10/16 | 10/22 | Change |
|---|---|---|---|
| OAT − swap (i-i OAT) | 4.79 − 3.543 = **125bp** | 5.13 − 3.481 = **165bp** | **+40bp** |
| OAT − swap (TE OAT 5.076) | — | **160bp** | — |
| Bund − swap (i-i Bund) | 3.42 − 3.543 = **−12bp** | 3.38 − 3.481 = **−10bp** | +2bp |
| Bund − swap (TE Bund 3.3311) | — | **−15bp** | — |

**Reading:**
- **The Bund trades ~10–15bp *through* swaps, and that richness did not change** (−12 → −10/−15).
- So the +37bp OAT–Bund move (137.4 → 174.6) is essentially the **OAT cheapening against swaps (+40bp)**. The safe-haven bid on Bunds this week shows up in the *level* of German yields, not in their spread to swaps. Germany and swaps fell together.
- **Credit vs supply:** asset-swap widening alone could be supply/positioning. Allianz (10/9) names hedge-fund asset-swap unwinds, Japanese repatriation and speculative shorts. But **CDS rose with it**, which supply does not do.
- **Rough basis check (time-mismatched, direction only):** FR 5Y 4.46 − 5Y swap ~3.46 [10/21, BlueGamma] ≈ 100bp vs 5Y CDS ~86–90. The bond is ~10–15bp cheaper than its default insurance, so there is a supply/positioning premium on top of credit. **Both are present; credit is the larger part.**
- ⚠️ CDS is secondary (CNBC 89.8 [10/21]; Investing.com 86.28 [10/20]; Bloomberg via finews 86.8; Italy 66.9). **France's CDS is above Italy's**, consistent with the France-only spread read. The 10/22 CDS print is not found.

## 4. Money-market edge

- **French 3M bill 2.77% vs DFR 2.50% / MLF 2.90%.** That's 13bp under the ECB's ceiling rate and 23bp over the German 3M (2.54).
- The 3M window covers the 10/29 hold and part of a Dec hike (~87% priced), so the expected policy average is ~2.55. **About 20bp of the French 3M yield is a France premium; the German 3M carries ~0.**
- Allianz (10/9) flags "French and Italian three-month bills converging toward the MLF" as the funding-disruption tell, where a break above the MLF = disruption. **Not broken. Watch it.**
- The 6M (3.03) sits above today's MLF, but it includes the Dec hike. That's not evidence of stress by itself.

## 5. Auctions (AFT, via search; the primary page returned 403)

| Date | Type | Lines | Bid-to-cover | Size |
|---|---|---|---|---|
| 10/01 | Long-term | 2036 / 2037 / 2038 / 2048 | 2.00 / 3.02 / 2.48 / 2.43 | €12.0bn on €27.5bn bid (~2.29×) |
| 10/15 | Medium-term | Feb-31 / Nov-31 / Feb-32 / Nov-33 | 2.32 / 2.30 / 2.30 / 2.23 | €12.0bn |

- **Demand is clearing at a price.** Covers in the ~2–3× range are normal for AFT. The 10/15 auction preceded the +37bp leg.
- **Next tests: long-term ~11/05, medium-term ~11/19** (AFT's usual first/third Thursday; dates not confirmed at AFT).

## 6. Where the ECB acts — Allianz Research framework (9 Oct 2026, primary analyst note, Subran/Boata/Darmet/Krizan)

| OAT–Bund 10Y | Allianz reading | ECB response (Allianz) |
|---|---|---|
| 120–150bp | Baseline: watered-down budget, pre-election range | None |
| **>150bp** | **"Tipping point"** | Verbal: "monitoring" → "ready to act" / "disorderly market dynamics" |
| **150–175bp** | **France-centred crisis; 2027 GDP +0.0%** | Talk, possibly repo intervention |
| ~175bp **with BTP ~150bp and Spain/Portugal widening** | General fragmentation | Operational steps: QT tweak (~€4.8bn/month relief), temporary operations |
| ~200bp with widespread, persistent contagion | Eurozone crisis | TPI, "late in the process" |

**Where we are 10/22:**
- **174.6bp is at the top of the France-centred band and the edge of the operational-steps line.**
- **The contagion condition is NOT met:** BTP–Bund ~127bp vs the ~150 needed.
- Under this framework, the ECB stays verbal. That's consistent with `KB-126`/`127` (TPI's fundamentals carve-out, Lagarde: "lies at home in France").
- Allianz also noted on 10/9 that "current pricing, if sustained, would even imply a BBB rating."

## 7. Holders and liquidity (Allianz 10/9)

- Foreign banks/non-banks hold **36%** (the most price-sensitive group). Domestic banks/non-banks hold 32%. Central banks hold 32%.
- Japanese investors hold ~**5% (~€137bn)**, which exposes France to Japanese repatriation as JGB yields rise (SAM's lane).
- Market depth was **>50% below normal**, and realized OAT spread volatility was at the 90th percentile (as of 10/9).
- ⛔ **No daily flow data** — "foreigners are selling" is unmeasured here.

## 8. Moody's Fri 10/23 (Aa3 negative)

- **ING base case (10/22, via FXStreet): a one-notch cut to A1 with a stable outlook, aligning with Fitch/S&P A+. A negative outlook "cannot be ruled out."** One analyst preview, not a consensus.
- **A1 stable is largely priced** (the market already trades France below its ratings). The asymmetric outcomes are:
  - **A1 negative** — a second cut becomes a live option within 12–18 months.
  - **A hold** — relief, but unlikely.
- A1 keeps France investment grade and ECB-eligible. There's no forced-selling cliff at this notch.

## 9. Open items

- ⚠️ **Budget calendar conflict:** Allianz (10/9) says the Assembly votes on 10/20 and 10/27; my STATUS carries a full-budget vote 11/17–18 (secondary), and a WALTER-surfaced search mentions the revenue vote being delayed. **Not resolved. Re-check before citing a date.**
- The 10/22 CDS print — not found.
- AFT primary auction pages — 403. Retry or read via a different client.
- The 30Y OAT asset swap — not computed (no 30Y swap).

## Sources

- ideal-investisseur OAT–Bund page (10/22 close)
- TradingEconomics France/Germany/Italy bond pages (10/22)
- Investing.com EUR 10Y IRS history; BlueGamma 10Y Euribor swap (10/22)
- Allianz Research, "Toasted, not burnt: France's bond sell-off and the road to the 2027 election", 9 Oct 2026 (PDF, read in full via pdfminer)
- ING via FXStreet 10/22 09:06 GMT
- CDS: CNBC (10/21), Investing.com (10/20), finews/Bloomberg, roic.ai/S&P GMI (10/1–10/2); all secondary
- AFT press releases 10/01 and 10/15 as surfaced by search (primary page 403)
