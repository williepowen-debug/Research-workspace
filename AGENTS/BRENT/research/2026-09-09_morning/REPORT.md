# BRENT morning prices — September 9, 2026

**Captured 09:58:57 ET.** Yahoo chart vendor quotes [CONF retrieval, September 9]; futures timestamps 09:46–09:49 ET (roughly 10–13 minutes delayed), equity timestamps 09:57–09:59 ET. All USD. Futures are intraday quotes, not spot assessments or authenticated settlements. Brent series here are NYMEX BZ financially settled contracts, not a direct ICE order-book feed. No current physical Dated Brent assessment was fetched.

Change basis: current quote versus the SAME named instrument's September 8 vendor daily bar, independently extracted from dated chart timestamps. The chartPreviousClose field refers to the older start of this five-day range and was NOT used as yesterday's denominator. Raw endpoint URL, quote time, prior bar and source JSON retained in [quotes.json](quotes.json). No roll splice. Other retrieval routes are not independent measurements.

| Symbol / contract | Quote | Change vs Sep 8 vendor close | Quote time ET |
|---|---:|---:|---|
| BZX26.NYM | 100.67 | +2.81% | 09:48:57 |
| BZZ26.NYM | 96.64 | +2.39% | 09:48:53 |
| BZF27.NYM | 93.13 | +2.00% | 09:46:11 |
| CLV26.NYM | 95.79 | +2.97% | 09:48:57 |
| CLX26.NYM | 92.53 | +2.59% | 09:48:57 |
| HOX26.NYM | 4.5349 | +2.61% | 09:48:42 |
| RBX26.NYM | 3.0432 | -0.72% | 09:48:57 |
| USO | 148.63 | +1.78% | 09:58:56 |
| XLE | 65.53 | +1.18% | 09:58:55 |
| XOP | 194.54 | +0.32% | 09:58:57 |
| EOG | 147.10 | +1.20% | 09:58:33 |
| XOM | 163.85 | +1.99% | 09:58:55 |
| CVX | 214.00 | +2.00% | 09:58:56 |
| LNG | 277.75 | +0.62% | 09:58:55 |
| STNG | 81.98 | -0.17% | 09:57:50 |
| NG=F | 2.842 | -2.54% | 09:48:55 |

Oil contracts USD/bbl; HO/RB USD/gallon; NG USD/MMBtu; ETFs/equities USD/share. STNG is tracked only; this is a market universe, not a holdings list. Option chains, orders and broker receipts are outside this price refresh.

## Structure and product separation

Brent November–January = **+$7.54/bbl**, versus **+$6.62** from September 8 vendor daily closes: +$0.92 wider. November–December +$4.03; December–January +$3.51. Current curve legs span 09:46:11–09:48:57, so this is an indicative snapshot with up to 166 seconds of leg skew, not an executable synchronized spread. Backwardation means nearer delivery is priced above later delivery.

Same-month November WTI minus Brent = **$-8.14/bbl** (both quote times 09:48:57). Front WTI is October while front Brent is November; their front-front difference is not the matched-month basis.

November NY Harbor ULSD versus WTI simple crack = **$97.94/bbl** (prior vendor $95.43); November RBOB versus WTI = **$35.28** (prior $38.55). Formula 42 × product − crude; ULSD/crude timestamps differ 15 seconds, RBOB/crude agree. These are specified futures-price diagnostics, not realized refinery profits, European diesel cracks or BRT-12's missing original history/upstream credit. No registered crack threshold is graded.

## Assessment

Crude and USO are stronger, with the nearby Brent premium widening. This is consistent with a stronger bid for prompt supply risk; it does not establish additional destroyed capacity or a durable outright-price floor. Exxon/Chevron lead the broad E&P ETF in this capture; tanker STNG and natural gas do not share the rally. Product performance also differs: ULSD rises while November RBOB falls and its crude-relative margin contracts.

Morning reporting attributes the oil rise to renewed Middle East escalation: [Reuters via Investing.com](https://ca.investing.com/news/commodities-news/brent-crude-rises-above-100-a-barrel-as-middle-east-conflict-escalates-4831881), [Oilprice early-morning report](https://oilprice.com/Latest-Energy-News/World-News/Brent-Breaks-100-for-the-First-Time-in-Nearly-Two-Months.html). Retrieved search results, not independent military verification. Their earlier price timestamps are context, not substitutes for this snapshot.

Existing Brent-above-100 line had already fired historically; no new arm, close-counter, research probability or prediction grade is inferred. WQ-189/192 STAND DOWN unchanged. Weekly physical observations retain August 28 vintage; today's EIA retail/STEO releases were not fetched here. Current matched physical/paper premium remains UNKNOWN. September 8 daily vendor bars are later observations than yesterday's archived intraday snapshots, not corrections to those snapshots.

## Record and validation

All 16 requests succeeded on the approved network rerun; initial restricted calls failed DNS. Verified positive same-day quotes and September 8 comparison dates, retained the raw responses, computed named-contract differences without continuous roll, and saved arithmetic in derived.json. Session-start Git sync succeeded once network access was approved. Existing source research, late OSPREY packet and XLE execution receipt remain open in SCRATCH; no external message or trade submitted.
