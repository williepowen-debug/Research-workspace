---
signal_id: SIG-W-20260904-005
date: 2026-09-04
time_dispatched: 2026-09-04T14:02Z
origin: Will-terminal 5-image batch 2026-09-04 ~09:4x ET, item 3 — @HormuzLetter X post 9/2 14:17 ("The Netherlands has moved 86 tonnes of its gold stock, worth $12 billion, out of the US, citing Trump's unpredictability over the Iran war… per Daily Mail"). Two days old at intake; verified at the DNB primary.
source: De Nederlandsche Bank press release 2026-09-02, "DNB improves tradability of gold reserves" (dnb.nl/en/general-news/press-release-2026/…), OPENED by WALTER 9/4; corroborated at Kitco 9/2, Euronews 9/2, NL Times 9/2 (all same figures). Daily Mail not opened — it is the relay's source, not the primary.
domain: METALS
cluster: FED_FRAMEWORK
precedence: PRIORITY
action: [MIDAS]
info: [LIQUID, BOND, ZHAO, HENRY, RED, PROME]
entities: [DNB, De-Nederlandsche-Bank, Sleijpen, Bank-of-England, NY-Fed, Bank-of-Canada, Zeist, gold-custody, Netherlands]
signal_type: pattern-match
confidence: 0.92
confidence_language: confirmed
verdict: CONFIRMED at the DNB primary, CORRECTED-FRAMING against the relay. Between March and August 2026 DNB moved ~86 of the ~313 tonnes it held in the United States and Canada to London: ~59t by SELLING in New York and BUYING in London, and >27t physically via Zeist. Shares: New York 31.3% → 18.5% · Ottawa 19.7% → 18.5% · London 18.1% → 32.1% · Zeist 30.8% unchanged; total 612.4t (€72.2B at YE2025). DNB's stated reasons: "increasing geopolitical unrest," crisis preparedness, and that Bank-of-England-held gold is the world's most tradable and "most readily available for DNB in a crisis situation" (Governor Sleijpen: "we have improved the tradability of our gold reserves"). The primary names NO country, NO government, NOT Trump, NOT Iran. "Out of the US" is half the story (Canada was cut by the same share), "worth $12 billion" is the relay's valuation (~€10.1B on DNB's YE2025 mark), and "no longer safe in Trump's hands" appears nowhere in the release.
consumer_lens: MIDAS owns central-bank gold behaviour: a G10 central bank cutting its NY Fed custody share from 31% to 18.5% is the datum, and the MECHANISM DNB gives is liquidity (London = the tradable venue), not custody distrust — the discriminating detail is that 59 of the 86 tonnes never moved; they were sold in NY and re-bought in London. ZHAO/BOND: foreign-official behaviour toward US-held reserve assets — note DNB deliberately KEPT 18.5% in New York and cut Ottawa identically. LIQUID/HENRY: gold as the crisis-liquid asset is the frame the release itself uses.
corrects: none
---

# DNB moved 86 of 313 tonnes out of New York AND Ottawa to London, March–August, for TRADABILITY. 59 tonnes went by sale-and-repurchase, not shipment. No Trump, no Iran in the primary.

## 1. The primary, opened

| | DNB press release, 2026-09-02 |
|---|---|
| What | ~86 tonnes moved from the ~313t held in the **United States and Canada** to **London** |
| When | **March – August 2026** (announced 9/2) |
| How | **~59t sold in New York, gold bought in London**; **>27t physically transferred** US/Canada → Zeist (NL), and a similar quantity Zeist → London |
| Total holdings | **612.4 tonnes, €72.2B at year-end 2025** |
| Stated reason | *"increasing geopolitical unrest"*; crisis preparedness; Bank-of-England-held gold *"meets modern international trade standards… the world's most easily tradable gold… the most readily available for DNB in a crisis situation."* Governor Olaf Sleijpen: *"With this relocation, we have improved the tradability of our gold reserves."* |

| Location | Before | After |
|---|---:|---:|
| Zeist (NL) | 30.8% | 30.8% |
| London | 18.1% | **32.1%** |
| New York | 31.3% | **18.5%** |
| Ottawa | 19.7% | **18.5%** |

## 2. What the relay added that the primary does not say

| Relay claim (@HormuzLetter, "per Daily Mail") | Primary |
|---|---|
| "out of the US" | out of the US **and Canada**, to London — Ottawa cut by the same share; 18.5% deliberately left in New York |
| "citing Trump's unpredictability over the Iran war" | **no country, government, person or war is named**; "increasing geopolitical unrest" is the whole of it |
| "senior officials warning the gold is 'no longer safe' in Trump's hands" | **not in the release**; if it exists it is a Daily Mail sourcing, unlocated |
| "worth $12 billion" | ~€10.1B on DNB's own YE2025 valuation (86/612.4 × €72.2B); the relay's dollar figure is at a later gold price |
| "moved 86 tonnes" (physical) | **59 of the 86 never moved** — sold in NY, re-bought in London; ~27t physically shipped |

⚠️ **Not an Iran-cluster signal.** The Iran framing is the relay's; nothing here depends on war-state and the anchor is unaffected.

## 3. Why it still routes PRIORITY after the framing is stripped
A G10 central bank cut its NY Fed custody share by 13 points inside six months and said so. **The mechanism it gives — liquidity in a crisis — is a statement about what it expects to need, and that is the datum for MIDAS's central-bank-gold thread.** The sale-and-repurchase structure is the discriminator between "distrust of US custody" (would ship) and "wants tradable bars in London" (sells and re-buys): DNB did mostly the latter.

**Asks — MIDAS (action):** log against the CB-gold behaviour vector; is DNB the first Western CB to reduce NY share in 2026, or one of several? (Germany's Bundesbank and others have been asked the same question publicly.) **ZHAO / BOND (info):** foreign-official custody of US-held reserve assets, as one datum, not a trend claim.

**Confidence 0.92** — primary opened, three carriers agree on every figure; the only unverified element is the Daily Mail "no longer safe" quote, which is excluded rather than carried.
