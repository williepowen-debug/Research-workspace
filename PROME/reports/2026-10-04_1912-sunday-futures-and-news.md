# Sunday futures and news — October 4, 2026, 19:12 EDT

User request: look at futures and related news. PROME synthesis; no domain grade, portfolio instruction, or gate change.

## Tape and provenance

Yahoo chart API fetched this session with explicit dated contracts, interval=1m, range=5d. Futures observations 18:59:52–19:01:27 EDT, approximately 10 minutes behind retrieval. These belong to Monday October 5's trading session. Changes below calculated against the same contract's last non-null Friday October 2 bar (16:59 or 17:00 EDT), NOT an independently verified exchange settlement. The ordinary FORGE daily fetch appropriately withheld evening changes; intraday bars supply the explicit comparison. Vendor previousClose independently matches these Friday bars numerically. One vendor only.

| Instrument | Contract | Last | Change vs Friday last bar |
|---|---|---:|---:|
| S&P 500 | ESZ26 | 7,787.00 | +0.13% |
| Nasdaq 100 | NQZ26 | 31,156.25 | +0.30% |
| Dow | YMZ26 | 51,522 | +0.09% |
| Russell 2000 | RTYZ26 | 2,856.90 | +0.21% |
| WTI | CLX26, November | $91.07/bbl | -0.04% |
| Brent financial futures | BZZ26, December | $102.63/bbl | +0.37% |
| ULSD | HOX26, November | $4.5472/gal | +1.02% |
| Gold | GCZ26, December | $4,175.30/oz | +0.31% |
| 10-year Treasury note | ZNZ26 | 104.453125 decimal points | +0.09% |
| Treasury bond | ZBZ26 | 102.969 decimal points | +0.21% |

USDJPY spot 157.725 at 19:11:30 EDT, -0.067% against Friday 17:01 bar 157.8300018310547. Not a futures quote or an official FX close.

Contract identity for BZZ26/RTYZ26/ZBZ26 is the explicitly requested and returned dated symbol; vendor display names are truncated. All Z contracts above are December 2026; X contracts November 2026. No continuous-series rollover comparisons. Raw endpoints follow `https://query1.finance.yahoo.com/v8/finance/chart/ESZ26.CME?interval=1m&range=5d`, changing symbol as shown in companion JSON. Raw response files remain under `/tmp/prome-*-20261004.json`; durable extracted metadata and actual Friday bar comparison are in `2026-10-04_1912-sunday-futures-quotes.json` beside this note.

Read: modest equity rise led by Nasdaq; Treasury futures higher (directionally lower yields); gold firmer; yen marginally stronger. This is not a broad risk-off opening. Products lead crude. Simple November HO*42 minus November CL = $99.9124/bbl, versus $97.9362 using Friday last bars. These are nonsynchronous vendor marks, not BRENT's settlement-window grade; do not substitute for its canonical series or VLO gate.

## Verified news

1. OPEC primary, October 4: seven participating countries maintain September required production for November; next meeting November 1. Targets are not evidence of restored physical supply. https://www.opec.org/pr-detail/1891616-4-october-2026.html
2. Reuters October 4 oil-opening report: Brent $103.06 (+0.79%), WTI $91.57 (+0.50%) at 22:02 UTC / 18:02 EDT, following Houthi claims of attacks on Riyadh and Khurais-area Aramco sites. Later Yahoo WTI November observation is back near flat; Brent financial contract retains a smaller gain. Wire report does not specify contract symbols, so its ICE Brent benchmark is not treated as identical to NYMEX BZZ26. https://d2233.cms.socastsrm.com/2026/10/04/oil-climbs-after-yemeni-houthis-attack-saudi-aramco-sites/
3. Reuters October 3 witnessed fire/smoke near Riyadh Aramco facility; no immediate Saudi confirmation, Aramco did not immediately respond. October 4 Houthi attack claim remains a claim. No new verified production outage established by this search; preserve FALCON's distinction between observed heat, unidentified facility, and confirmed production loss. https://www.internazionale.it/ultime-notizie-reuters/2026/10/03/fire-smoke-seen-near-aramco-facility-in-riyadh-witness-says and https://www.devdiscourse.com/article/international/3986620-yemens-houthis-say-they-struck-saudi-aramco-sites-in-riyadh-khurais
4. G7 PRIMARY NOW READ (UK government, published October 2): 100 million barrels over four months, frontloaded diesel within first 20 days; document ties implementation to March commitments. Do not add 100M as an entirely new authorization on top of March. Members reaffirm no energy export restrictions BETWEEN G7 countries. Scope does not establish a universal US export policy or verify the separate Trump-post quote. Refining utilization and maintenance coordination also promised. This closes the primary-unread limitation of the earlier boot orientation for this statement alone. https://www.gov.uk/government/news/g7-leaders-statement-on-global-energy-security-and-market-stability
5. ISM's own August release confirms September Services PMI publication Monday October 5, 10:00 EDT. Watch activity, employment and prices together for the growth/inflation mix. https://www.prnewswire.com/news-releases/services-pmi-at-55-4-august-2026-ism-services-pmi-report-302868046.html

## Held-book implications (PROME inference)

- Nasdaq strength offers no immediate relief for five QQQ October 5 $735 puts. Existing sell-or-roll stop remains Monday 15:00 ET, fresh cash/option marks needed; no Sunday option price inferred from futures.
- USO call gets no decisive crude breakout from this snapshot. WQ366 hold decision preserved.
- Diesel strength supports the refining-margin side of VLO; G7 barrels work in the opposite direction, while the G7 export-restriction pledge reduces one policy concern. No VLO gate fired by this synthesis.
- Treasury futures rise is adverse directionally for TLT puts/TBT. WQ357 research deferral preserved, no new exit instruction.
- Next meaningful market test: whether early equity strength persists through Asia and whether diesel remains stronger than crude; Monday 10:00 ISM. Overnight quotes cannot settle Monday's outcome.
