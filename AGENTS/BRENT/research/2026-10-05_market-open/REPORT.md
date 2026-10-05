# October 5 market-open refresh

**Scope:** capture at 09:44 ET, supplemental pull 09:50 ET; news checked through approximately 09:53 ET. Futures quotes lag the equity quotes. This is a dated diagnostic, not a settlement grade, broker valuation, or new capital approval. Raw observations: [snapshot.json](snapshot.json), [supplemental.json](supplemental.json); reproducible reader: [pull.py](pull.py). No scheduled routine was launched.

## Tape and structure

[CONF vendor observations, Yahoo/yfinance, 2026-10-05; changes versus vendor previous close, not independently authenticated settlements.] All prices USD; oil/cracks per barrel, products per gallon, gas per MMBtu. Quote times ET.

| Instrument | Quote | Change | Time |
|---|---:|---:|---|
| December Brent BZZ26.NYM | 101.63 | −0.61% | 09:34:50 |
| January Brent BZF27.NYM | 98.24 | −0.48% | 09:34:40 |
| February Brent BZG27.NYM | 95.43 | −0.52% | 09:32:51 |
| November WTI CLX26.NYM | 89.62 | −1.64% | 09:34:50 |
| December WTI CLZ26.NYM | 88.32 | −1.24% | 09:34:50 |
| November ULSD HOX26.NYM | 4.5523 | +1.14% | 09:34:48 |
| December ULSD HOZ26.NYM | 4.4201 | +1.44% | 09:34:48 |
| November RBOB RBX26.NYM | 3.2586 | −1.62% | 09:34:47 |
| November gas NGX26.NYM | 3.006 | −0.96% | 09:34:50 |
| USO | 144.69 | −1.85% | 09:44:16 |
| VLO | 406.955 | +0.16% | 09:44:18 |
| MPC | 423.27 | +0.25% | 09:44:48 |
| XLE | 62.15 | −1.27% | 09:44:53 |
| STNG / FRO / DHT | 86.32 / 53.6325 / 24.02 | +0.15% / +1.70% / +1.41% | 09:44:34–52 |
| LNG / VG | 268.045 / 12.89 | −0.68% / −1.79% | 09:44:45–52 |

[EST arithmetic from the named vendor legs.] Same-date quote validation, USD identity and maximum 300-second inter-leg skew passed; neighboring contract expiry metadata are distinct. No conversion from continuous futures and no official-settlement claim.

| Spread | Value | Interpretation |
|---|---:|---|
| December–February Brent | +6.20 | Backwardation; above existing +3.50 research line intraday |
| December–January Brent | +3.39 | Backwardation |
| December WTI–Brent | −13.31 | Matched contract month |
| November ULSD–WTI | 101.5766 | HOX26 ×42 − CLX26; $6.58 above notice/$11.42 above exit levels intraday |
| December ULSD–WTI | 97.3242 | HOZ26 ×42 − CLZ26; context, not the November F1 basis |
| November RBOB–WTI | 47.2412 | RBX26 ×42 − CLX26; retired gasoline-crack line stays retired |

**Assessment:** softer crude with firmer diesel supports keeping crude-direction exposure separate from refiner-margin evidence. VLO-HELD-01 requires the specified settlement or signed policy; this capture grades neither. Friday's $97.97 was a settlement-window vendor proxy, so do not call the difference a matched daily change. Today's valid February quote does not repair Friday's absent settlement-window bar. Tanker quotes recovered after the pre-open freshness failure, but the specified decision window is not open; no Stage-A grade follows.

## Physical, retail and storage

[CONF primary-series observations retrieved October 5, dates below; EIA API and FRED keyless CSV.] No new WPSR print: all metrics remain week ending **September 25**. Commercial crude **427.320M (+0.922M)**; SPR **283.767M (−0.785M)**; Cushing **24.301M (+0.553M)**; gasoline **204.362M (−1.684M)**; distillate **105.180M (−2.251M)**; refinery utilization **92.5%**; gasoline four-week YoY **+0.2587%**. The next release is **Wednesday October 7, 10:30 ET**, data week October 2; it is outside BRT-31's window.

| Series | Latest available observation | Value |
|---|---|---:|
| DCOILBRENTEU, physical Dated Brent | September 29 | $113.96/bbl |
| DCOILWTICO, WTI spot | September 29 | $96.16/bbl |
| DHHNGSP, Henry Hub spot | September 29 | $3.18/MMBtu |
| GASREGW, US regular retail gasoline | September 28 | $4.465/gal |
| GASDESW, US retail diesel | September 28 | $6.382/gal |
| BAMLH0A0HYM2, broad HY OAS | October 1 | 3.24% / 324bp |

FRED URLs use `https://fred.stlouisfed.org/graph/fredgraph.csv?id=<series>`. Retail diesel is down $0.147 week/week; gasoline down $0.013. These are last week's observations, not Monday October 5 pump prices. HY OAS is broad-market context, **not energy-sector OAS**; no fresh energy-credit measurement is claimed. Spot and today's futures have different dates: no physical/paper premium is calculated.

[CONF GIE AGSI+ API](https://agsi.gie.eu/api/data/eu), gas day **October 3**, provider status **E**: EU storage **72.40%**, **819.8844 TWh**; October 2 **72.15%**, October 1 **71.98%**. This extends the observed refill; it does not meet the existing 80% floor. The October 1 decision-date grade used September 30 and remains a historical grade. No winter adequacy or target-date extrapolation is registered.

## Saudi operations: disputed flow, named capacity assurance

[AFP, October 5](https://robodaily.com/reports/261005084339.jedqrmxd.html) attributes a pumping halt and Khurais-station damage after the October 4 attack to an anonymous Saudi energy source. [Bloomberg via Newsquawk](https://www.newsquawk.com/headlines/saudi-arabias-east-west-pipeline-is-flowing-as-normal-bloomberg-reports-citing-sources) reports normal East–West flows. [Reuters separately reports uninterrupted flows, citing an unnamed source](https://www.dawn.com/news/2034915/saudi-east-west-pipeline-oil-flows-uninterrupted-source-says).

[Reuters' named Nasser interview, October 5](https://www.gulftoday.ae/news/2026/10/05/aramco-can-make-12-million-barrels-per-day-available-within-days-ceo-says) says Aramco could make its 12 mb/d maximum sustainable capacity available within days, describes its system as intact and says exports/customers are being served using alternate routes and inventories. **That is an operator capacity/availability claim, not measured current production or a station-specific damage clearance.** It is counterevidence to an unqualified total-outage claim; it does not resolve the conflicting pipeline reports.

Nasser's separate [official prepared speech](https://www.aramco.com/en/news-media/speeches/2026/remarks-by-amin-h-nasser-at-energy-intelligence-2026) warns that products and depleted buffers remain stressed and estimates rebuilding inventories could take up to two years. His quantities refer to different objects: nearly 10bn barrels of initial total stocks; nearly 3bn of cumulative supply lost; over 1bn drawn from stocks; commercial stocks below 6bn. These are attributed operator estimates, not independently audited balances. **Lost supply is not an inventory draw.** The speech gives no clean new Petroline output-loss figure. Full text was available through the official-page search extraction; direct web open returned an access error.

**Disposition:** new Khurais/Petroline damage, net loss and duration remain UNKNOWN. BG-02 R1/R4 qualifying quantified-loss evidence is absent in this review. No new incident-loss number, frame-breaker fire, reopening of lapsed instance (4), or restart grade. WQ-264 shadow period continues through October 24.

## Export recovery: preserve each perimeter and vintage

WALTER `SIG-W-20261005-002` is integrated against [Reuters September 28](https://www.marketscreener.com/news/mideast-oil-exports-rebound-in-september-as-saudi-arabia-boosts-shipments-ce785addd888f724): preliminary September regional crude **16.328 mb/d**, February comparator **19.513**; separate through-Hormuz estimate **9.719 mb/d**. Regional scope includes bypass routes and ship-to-ship transfers. The displayed regional ratio is **83.68%**, while the quoted recovery description is just under 80%; its denominator remains unresolved. Do not derive a Hormuz normalization percentage from a regional baseline.

[Reuters October 5, 07:54 EDT](https://www.marketscreener.com/news/middle-east-oil-exports-top-pre-war-levels-for-part-of-september-but-tanker-attacks-increase-ce785ddbd18ef622) supplies a different window: Kpler **seven-day crude average 18.3 mb/d on September 30**; Vortexa **14-day crude-plus-condensate average 18.6 mb/d**. This is stronger late-September regional-flow evidence than the preliminary monthly average, but the periods and commodity sets differ. It is not a final September monthly replacement, an October 5 observation, or a matched dual-vendor BG-02 test. No AIS-dark-share disclosure. The October 4 wire's **18.5 mb/d on October 1** also has a different endpoint; do not describe 18.3 as a simple revision of 18.5.

**Assessment:** improving all-route exports can coexist with constrained Hormuz access, product scarcity, buffer depletion and attacks. Exported barrels are not a measure of production or full facility repair. This extends the existing physical-supply watch only; no new instrument or watch is registered.

## Policy, insurance and incoming context

- **US diesel policy:** the [October 2 presidential pool reports](https://www.presidency.ucsb.edu/documents/pool-reports-october-2-2026) record Trump's on-record rejection of an export ban. This supersedes our old “no White House word” reader path. [Wright did not categorically rule out future restrictions on October 4](https://www.cbsnews.com/news/face-the-nation-full-transcript-10-04-2026/). No signed new restriction was identified in the bounded White House/Federal Register search. Neither statement rewrites B1 or proves a permanent exemption; TERRY owns grading.
- **JWC:** the [IUA index](https://www.iial.co.uk/IUANew/UnderwritingItems/Committees/Joint_War_Committee_Risk_List.aspx) still lists JWLA-035 newest (index September 17). The [LMA primary PDF](https://lmalloyds.com/wp-content/uploads/2026/09/JWLA-035-Black-Sea.pdf), dated September 16, changes the Black Sea; the Gulf/Gulf of Oman and Southern Red Sea remain listed (pp1,3). `KILL-LEG2-JWC-LISTING` NOT FIRED. Human verification stamp refreshed; BRT-30 frozen JWLA-034 baseline and October 26 resolution date unchanged. Listing is not a premium quote or transit count.
- **WALTER -001:** [owner packet](../../../../BOARD/SIG-W-20261005-001-planned-fe1-suez-return.md) noted. FE1's October 17 origin departure is planned, not a completed Suez transit; container capacity does not measure tanker supply. HAWK owns the event watch.
- **WALTER -004:** [owner packet](../../../../BOARD/SIG-W-20261005-004-uk-shipping-sanctions-bounded-sakhalin-licences.md) noted with its sanctions/licence limits. No measured LNG export loss follows; do not label all eight designated ships LNG carriers. No independent legal interpretation or new loss figure from BRENT.

## Positions and remaining work

The October 1 mirror remains the last receipted holding evidence. The USO October 9 $150 call feed returned **zero bid/ask and a Friday October 2 last trade**: unusable as today's mark. At the captured USO price, the strike is $5.31 away (3.67% underlying gain to reach it); this is arithmetic, not a probability or option valuation.

The [TERRY management card](../../../TERRY/setups/USO150C-KRE65P_roll-management-notes_2026-10-01.md) already contains ×1 addenda. BRENT's claim that it still used ×2 was stale and is corrected in TRADE. TERRY's October 2 SELL lean is a recommendation, not approval or a fill. Current holding status was requested from Will; until a receipt arrives it remains unconfirmed after October 1. Existing October 9 15:00 ET rail remains.

Next: settlement-basis refiner check at the specified close; tanker liveness only in its existing window; October 6 STEO/SPR bids/crack-month sitting; October 7 WPSR; October 9 COT and option deadline; October 15 first eligible BRT-31 release. Preserve WQ-192 stand-down, staged VLO shares, declined USO harvest, paid-data deferral and the CATO routine-deployment deferral. No trade or remote routine action.
