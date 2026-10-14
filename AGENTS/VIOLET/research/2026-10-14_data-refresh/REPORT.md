# VIOLET data refresh — October 14, 2026

**Written:** 2026-10-14 15:35 ET. Same owner session `01a13bc1-8595-7e43-8101-874cf704d973`, Codex/OpenAI gpt-6.1-sol/high. Will: “lets look for other data that we need to update our VIOELT files. Things like SKEW move etc”. Existing desk tools and thresholds only; no trade, new monitoring rule, spending or external send.

**Result:** refreshed available observations and recovered **29 missing historical rows**. The latest final SKEW and primary MOVE daily observations are still October 13. The current intraday volatility surface repriced after CPI but remains upward; the earlier credit-vol WATCH is unchanged. This is a data/freshness pass, not a new trade opportunity or a grade before publication.

## Available observations and update implications

| Series | Latest verified basis | Change / limit |
|---|---|---|
|SKEW|154.74, official October 13; 20-session mean146.183|Official October 14 final bar absent; RED-FT-10 remains3 of 4. Rechecked publisher, not silently forwarded to today.|
|MOVE|101.09, primary daily table October 13|+2.66% vs98.47 onOctober9, below113.60 October 5 peak. October 12 absent from bond-market primary table, not a missing observation.|
|MOVE secondary|99.1438, Yahoo current-day bar October 14, retrieved15:30 ET|UNCORROBORATED cross-check only. Primary has no October 14 bar; not promoted to primary ledger or a grade. ICE offers intraday data, but a validated public publisher quote was not obtained.|
|VIX /VVIX|17.15 /97.40, Cboe delayed pull15:27:54 ET|Fresh TICK replaces earlier TICK in VX_DAILY using existing --supersede; never presented as final close. Source dates checked by existing publisher witness.|
|VIX9D /VIX3M /VIX6M|14.87 /18.96 /20.59, same pull|VIX9D/VIX0.8671; VIX3M/VIX1.1055; still upward.|
|VX monthly futures|October 13settlement, same October 21/November 18pair; +4.482%|No newer dated settlement obtained; no same-day CPI futures reaction inferred.|
|OVX|48.77 final October 13; separate delayed48.75 onOctober14|Official same-date ratio3.19 WATCH; intraday OVX stamp15:20:02.571 ET differs from VIX capture, so no mixed-time live ratio grade.|
|Correlation /dispersion|OfficialOctober13 retained; delayedOctober14COR1M9.43/COR3M13.05/COR30D9.58 at15:08:31 ET|Three earlier missing official days restored; today's TICK reconciled to the matched Cboe capture. DSPX36.72/VIXEQ40.58 separately delayed at15:08:32 ET. No official-close sustain grade.|
|Yen realized /option volatility|October 14pull RV10 =2.44%,RV20 =4.88%,rank3.9; FXY callIV11.1%,IV/RV4.55|Current-day FX observation is intraday; CALM realized leg with event premium in options. Historical optionIV/OI still unavailable.|
|VIX futures positioning|Latest actual CFTC report October 6; leveraged money+5,494,rank96.8|September 29 missing report restored; no October 13report presumed. Latest published ranks unchanged.|
|VIX options|October 14snapshot,October 21C/P OI2.79|Volumes refreshed; outstanding OI is not initiated net hedge flow. Snapshots need not exist for every trading session.|
|Credit /rates /holdings|Current LIQUID/BOND owner records and FORGE|Cross-desk truth referenced; no separate drifting credit/quantity mirror or new causal grade.|

Primary SKEW: https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv . MOVE desk primary: https://www.investing.com/indices/ice-bofaml-move-historical-data . Cboe delayed quote/history capture records: `sources.json`; latest writer input: `live-thresholds.json`. MOVE successful existing-reader capture is `MOVE_history.json`; generic requests403 is separately recorded, not misreported as a global primary outage. Secondary quote retained in `MOVE_crosscheck.json`. ICE frequency: https://developer.ice.com/fixed-income-data-services/catalog/ice-data-indices-move-index . All dates are observation dates, not just download dates.

**At-use SKEW integrity:** October 14 15:27 EDT,22/22 overlapping sessionsSeptember13–October 13 agree within0.005. Receipt `skew-integrity.txt` bounds this read only. Cboe remains grade authority; no official October 14close invented.

## Historical recovery, not a retroactive first-publication grade

| Ledger | Missing observations restored | Method / constraints |
|---|---:|---|
|OVX.tsv|12|Matched official Cboe OVX/VIX historical datesSeptember22–October 13; existing formula, historical quantiles ending each date, no later data. Historic state label is reconstruction, not a new live fire.|
|JPY_VOL.tsv|13|Yahoo USDJPY closes; each date uses its trailing3-year sample and existing10/20return standard deviation ×sqrt252. FXY IV/OI cells intentionally empty with explicit note.|
|IMPLIED_CORR.tsv|3|OfficialSeptember22/23/25 Cboe closes. Same existing direction-only constituent-vol estimate; source/basis recorded.|
|COT_VIX.tsv|1|CFTC2026annual archive, contract1170E1,September 29. Existing percentile/flag formula; no current rank changed.|

September 29leveraged-money net was **−7,467**, followed by October 6**+5,494**. September 29rank83.3 carries the legacy label ELEVATED_LONG, but net exposure was still short: a rank label is not a sign. All available2026VIX reports in the retrieved annual file now have ledger rows. Raw positions and recovery record: `CFTC_2026_VIX.json`, `recovery.json`.

**Freshness census:** VX_DAILY,OVX,JPY_VOL,IMPLIED_CORR now have **0 missing available sessions** in the boundedSeptember22–October 13 check. The check uses actual publisher session dates, not an invented holiday calendar. It does not certify all history or missing cells. `freshness.tsv` is this dated audit, not a new recurring monitor. Older futures settlement cells remain empty because the two existing writer conventions conflict; no unauthorized backfill convention was chosen. Prior source snapshots stay historical.

## State and visual summaries

STATUS/SCRATCH/NEXUS and the two existing local HTML live bands refreshed; durable gauge meanings, taxonomy and routing preserved. Expired pre-CPI pending-decision wording removed from visual bands. WQ418 PASSED remains actual disposition; no fresh opportunity. Repo visual source updated; **hosted publication remains unverified** because the original Artifact publisher is not exposed/verified in this runtime. Existing URLs were not replaced with new hosted pages.

Convergence remains30/50; thesis v4.1.2 unchanged. Counterevidence still matters: curve upward, VVIX below120, HY size/origin incomplete, dated funding nonconfirmation. Historical gap repair strengthens continuity; it does not strengthen a forecast by itself.

## Next dated test and closeout

October 14evening: actual final SKEW/VIX/VVIX/correlation/futures publication; MOVE primary frontier when it advances. RED owns FT-10grade. October 15published credit/funding provides matched post-CPI bridge; existingOctober16LIQUID/CFTC/WQ410obligations remain. Historical FXY option data and earlier settlement convention remain explicit gaps. No new threshold or research agent.

Owner preflight repeated19:22:58UTC onDESKTOP-BC6EF81: only desk-declaring VIOLET hostPID496602 is this owner; saved/native incomplete coverage remains UNKNOWN, no replacement launched. ForeignBROCK/WALTERdirty work means initial pull deferred. Whole boot16stages passes; corrections0named pending; normal scoped Git/closeout proof in `CLOSEOUT.md`. No new WALTER packet at intake. Recipient notification/consumption requires evidence and is not inferred from saved files.
