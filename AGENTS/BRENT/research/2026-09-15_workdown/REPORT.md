# BRENT workdown — September 15, 2026

## Completed in this batch

| Item | Result |
|---|---|
| USO September 11 159C outcome | Will confirmed **sold before expiry** this session. TRADE records CLOSED; sale date, price and proceeds remain UNKNOWN. No P/L inferred. |
| Receipt reader | Scoped to actual execution/position sections; navigation no longer counts. Outstanding receipts return FINDINGS even without a mirror contradiction. Explicit expiry dates surface unresolved expired holdings. Same-ticker closures are candidates requiring contract/account matching. Missing sections fail closed. |
| Diesel coverage schema | Moved the complete September 14 warning from probe_scope to notes, byte-for-byte; component_only restored. Full spread remains unverified; warning is PARTIAL_COVERAGE rather than unknown schema. No threshold changed. |
| Baker Hughes reader / September 11 observation | Publisher workbook recovered and live reader repaired. Minimal headers work today; bounded alternate request shape retained. Date checked in filename AND workbook. Missing US Oil cannot fall through to Canada; ambiguous links/counts fail. |
| Trade/state text | Removed obsolete stacked TRADE header, recorded the sale, refreshed BRT-26 standing state, rotated dated September 14 analysis verbatim, replaced yesterday's current-looking synthesis with the new evidence boundary. |
| IATA source task | Original PDF recovered and visually checked; jet-specific basis integrated below. Exact latest observation/value absent from chart, so latest-price comparison declined. |

## BRT-26 — owner reading at the primary

**[CONF Baker Hughes, observed September 11; retrieved September 15] US Oil 450, +1 from 449; 457 not reached. BRT-26 remains OPEN, confidence unchanged at its existing 85% re-mark.** Two remaining scheduled September prints are September 18 and 25; October 2 falls outside Q3. This is the delayed September 11 observation-grade, not early resolution of the full prediction.

Primary: [Baker Hughes current listing](https://rigcount.bakerhughes.com/na-rig-count), selected workbook `ac9a8c23-3a35-4a0c-88d3-d8678af2f5c6`, saved as bh-current.xlsx. Content-Disposition names September 11; NAM Summary D4 agrees. Row 22: Oil 450 / +1 / 449. US total 591; gas 132; miscellaneous 9. Horizontal 536 (+1), directional 43 (+1), vertical 12 (+2); both breakout sums equal 591. The earlier secondary reading is confirmed. Horizontal rose this week, unlike September 4; no mechanical shale-response inference from the oil headline alone.

Retrieval integrity: original saved workbook plus a separate successful live-reader pull ([receipt](rig-live-verification.json)); prior September 11 routine independently retrieved secondary mirrors. **One underlying measurement lineage: Baker Hughes.** Multiple mirrors and pulls do not create independent measurement witnesses. Do not repeat older two-lineage claims from the historical outcome prose. Primary publication is sufficient for this non-breach observation; no claimed independent census.

## Saudi cargo report — direct article recovered

[Argus, September 15](https://www.argusmedia.com/en/news-and-insights/latest-market-news/2878080-aramco-defers-cancels-some-european-sep-crude-sources) reports at least three European refiners affected by late-September cancellations/deferrals, potentially into November; two others await notice. Aramco declined comment. No affected barrel volume is supplied. Earlier delays predated the pipeline attack. Its apparent absence of Yanbu departures since September 11 carries an explicit AIS-undercoverage caveat.

**Assessment:** delivery disruption now has direct reporting; yesterday's blanket zero-loss language cannot certify today's conditions. Attribution, aggregate lost supply and duration remain unmeasured. No BG-02 fire follows from a secondary report or single-tracker observation. Exact cargo sizes, buyer notices, replacement dates and both-tracker coverage remain owed. Direct-source recovery is COMPLETE; quantitative scope is PARTIAL.

## Jet fuel — physical basis integrated, price comparison withheld

[IATA September 11 report](https://www.iata.org/en/iata-repository/publications/economic-reports/structural-shifts-increase-jet-fuel-crack-risks/) uses the global jet-fuel price index minus Dated Brent, USD/barrel, sourced to Platts/IATA. PDF text and rendered page both checked. It attributes higher and more volatile margins to refining concentration/import exposure and middle-distillate pressures. This supports a separate airline fuel-cost channel; a crude-only hedge need not capture the product premium.

The chart spans 2012–2026 with regime averages. Publication date is exact; the last point's date/value is not labelled. No exact $70 current reading, HO-futures equivalence or Boundary #6/#8 grade is established. Integration is complete at the report's actual scope.

## BRT-29 M — additional candidate review; still not enough to grade

Reviewed the full prediction and linked history. Three further named carrier announcements by August 31, with the specified cause, remain the original test. No subsidiary multiplication, retroactive duration choice, airspace-only substitution, or outcome-date substitution.

| New primary examined | Disposition |
|---|---|
| [AirAsia Group, August 13](https://newsroom.airasia.com/news/airasia-group-financial-results-second-quarter-2026) | Announces planned Q3 capacity reduction of 20–25% YoY amid fuel economics and seasonality. Adds a supported group-level candidate to prior AF-KLM evidence. A group announcement does not establish three distinct additional carriers, nor isolate a fuel-only effect. |
| [Thai AirAsia, August 14](https://newsroom.airasia.com/news/2026/8/14/aav-announces-financial-results-second-quarter-2026) | Reports Q2 cuts and continued Q3 restraint. The quarter ended before the registration baseline. No distinct new eligible package established; do not count alongside its parent by assumption. |
| [AirAsia Philippines, August 8](https://newsroom.airasia.com/news/2026/8/8/airasia-philippines-ranks-no-1-among-the-worlds-most-punctual-low-cost-airlines-in-july-2026) | Connects fleet adjustments to fuel/geopolitical costs, but reports benefits of already-implemented changes. No dated new capacity-cut announcement established. |
| [Air India May 13](https://www.airindia.com/in/en/newsroom/press-release/Air-India-rationalises-international-route-network-through-August-2026.html) | Primary confirms fuel-linked June–August reductions were announced in MAY. Excluded: an August operating period is not an August announcement. |

Result: evidence coverage improved, **M remains UNRESOLVED / not established**, not proof of zero and not a final failure grade. Prior paired jet/gasoline leadership remains intermittent, with the original duration ambiguity. Final prediction stays OPEN to September 30; no mark/date/letter moved. Next useful research is carrier-specific first-announcement dating beyond these parent-group releases, not another pass through the same summaries.

## Still open / next work

- September 16 10:30 ET WPSR / L305 SPR resolver and BRT-29 T; future release not completed now.
- Six remaining standing-row reconciliations; nine ACTIVE incident rows and three other current-status rows need actual operating evidence. No automatic downgrade to a restart.
- Saudi cargo quantities and timing, YASREF verification (FALCON), Shanghai/Brent synchronized chart (SIG-007), lower-48 gas primary check, Yanbu offtake, war-risk terms, BRT-12 evidence, GROUP_MAP retirement, separate resolver lesson and seasonal measurement questions.
- WQ-234 / BG-02 policy choice and prior DAEDALUS read-floor work remain at their existing owners. No trade or threshold authority changed.
- Scheduled Friday COT run is still too early; an exact proposed schedule repair already exists at audits/2026-09-09_maintenance/ROUTINE_UPDATE.md. Remote settings unverified; no local edit is claimed as installation.

## Validation and continuity

60 offline tests passed, including 12 receipt and 7 rig regressions. Full network boot ran after code changes: receipts OK; instruments WARNINGS, with Baker Hughes no longer blocking. EIA freshness, BRT-29 review, ledger nudge and standing reconciliation remain findings. Calendar and final write-back checks recorded separately. No claim that the desk is fully clean.

Sender-owned five WALTER packets remain untracked as of this work pass; dispositions are in BRENT's board log, durable integration is here, and archive moves wait for sender commit. No outbound sends. Sender-owned work remains uncommitted, so startup pull was deferred; only exact own paths are included in the local commit. Safe-push outcome is recorded at closeout.

### Final local checks

- All 60 offline tests pass after the final code change; registry lesson sweep passes with all 13 governing lessons cited. TSV row/column counts preserved; BRT-26/BRT-29 first nine fields unchanged.
- Calendar matches all 25 events. Six standing rows remain findings; no blanket re-stamp.
- Read-cap checker passes its five-file perimeter: STATUS 19,044 bytes before final banner adjustment. TRADE 25,166 bytes remains in the rotation advisory tier; further reduction requires preserving the live gate/structure clauses and is still owed.
- Whole-change weekday scan flags eight pre-existing historical assertions, plus four copies in immutable before-images. None was introduced in this batch; historical date reconciliation remains a separate task.
- INCIDENTS and LESSONS unchanged: no newly verified operational state and no new lesson authored. Existing ledger nudge retained rather than freshened through a metadata-only edit.

Staged whitespace check passes for authored code/current prose. Raw publisher HTML, extracted text and verbatim archives retain source whitespace; these are intentionally preserved, not normalized.
