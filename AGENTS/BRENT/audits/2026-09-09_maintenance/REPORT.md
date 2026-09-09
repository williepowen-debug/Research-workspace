# BRENT maintenance — September 9, 2026

Implemented the local repairs from the [file-health audit](../2026-09-09_file-health/REPORT.md). **41 regression tests pass.** Remote routine activation and source-dependent composite construction remain incomplete. The existing main folder layout is retained.

Scope: Will approved working through the maintenance. This pass extends existing readers and continuity surfaces; it does not create a trading rule, change a registered numerical level, grade a prediction, refresh missing incident evidence or infer a broker fill. Base before-image: `7b8461779`. Results below are confirmed by local checks and the saved September 9 validation captures, not a new market outlook.

## Audit dispositions

| Item | Result | Evidence / remaining limitation |
|---|---|---|
| A1 Quote integrity | Implemented | No previous-close substitution. Quotes retain source, timestamp, returned symbol/currency, prior close and quality state. Missing, future, nonfinite and >30-minute observations cannot produce a current threshold verdict. Missing prior close produces unknown change, not 0%. |
| A2 EIA completeness | Implemented | Each metric carries its own observation date. Missing fields, mixed weeks and stale dates produce FINDINGS/rc=2. WoW requires an adjacent week; gasoline comparison requires all four current and four exactly 52-weeks-prior observations. Nulls/conflicting duplicates remain holes. Partial API data are not silently filled from local history. |
| A3 Local EIA reader | Implemented | Chooses the latest dated numerical report, skipping publication notices. September 2 report correctly selected after September 9 notice; week ending August 28, release September 2. File mtime cannot refresh observations. Explicit --live fails closed if unavailable. |
| A4 Retired wording | Implemented | Tracked tickers are not labeled holdings; tanker equities are not freight measurements. Retired gasoline Phase-2 trigger removed from execution. SPR output no longer asserts a universal statutory floor. Both boot summary messages describe findings without blaming the spec for every timeout. COT docstring corrected; executable grading unchanged. |
| A5 Release coverage | Ready, NOT INSTALLED | [Exact schedule, prompt additions and activation checks](ROUTINE_UPDATE.md): timezone-aware local times, Thursday EIA fallback, Friday 16:15 after releases. No callable RemoteTrigger/routine-control tool is available in this session. Actual configuration and first-run acceptance still require remote access. The live mirror remains unchanged. |
| A6 Complete composites | Partially completed | Full STNG/FRO/DHT quote/previous-close diagnostic now replaces the STNG-only instrument probe. New explicit-contract CLI calculates matched WTI–Brent and ULSD cracks with date/unit/identity checks. Registry WTI–Brent and diesel probes deliberately remain component-only: their original benchmark/roll/history basis is still unestablished. The diagnostic is not that historical construction, an official settlement, t-4 comparison or gate grade. |
| A7 Deadlines | Implemented for audited cases | Explicit outer bounds are scanned; missing bounds do not crash. Unresolved BRT-29 M surfaces its August 31 sub-deadline separately from September 30 final scoring. Weekday countdown now says weekdays and explicitly includes holidays. Other internal sub-deadlines/event preconditions and STUCK rows still need owner review. |
| A8 Refiner tool | Retired | CLI prints a retirement notice and valid archive pointer, performs no retrieval or TSV append. Historical functions/data preserved, not commissioned as current signals. |
| A9 Hot-file maintenance | Implemented | Two older dated STATUS blocks archived verbatim; only nonbinding CLAUDE rationale moved to RULINGS. FASTOW PENDING disposition and next-run hints reconciled with the full-set generated calendar. Historical run/ownership/standing/calibration text preserved. [Checksums](rotation-manifest.json), [preservation checks](preservation.json). |

## Reader policy and use

The 30-minute quote tolerance accommodates delayed vendor quotes but is a data-quality tolerance, not an entry/exit threshold or authenticated real-time guarantee. It is deliberately conservative outside market hours: older closes remain dated context and become UNGRADED. Existing registered market windows and complete trade readers still govern actions.

Composite quote legs must have the requested USD instrument identity, aware timestamps, the same ET observation date and at most five minutes of timestamp separation. Tanker window is open only if all three observations and retrieval are within 14:00–16:00 ET on a weekday. That is a diagnostic availability label, not an exchange-holiday calendar or authorization to repeat a once-per-session grade. The owner must still read complete BE-04 through BE-12, including C and the close veto. Boot always retains OWNER_GRADE_REQUIRED even after all components return.

The existing CUSHING-20M ten-day observation budget is reused for weekly EIA integrity, not widened to conceal the holiday gap. API retrieval time is not release time. The current API and local reports both return August 28 observations, twelve days old; both therefore correctly return rc=2 on September 9. Local gasoline YoY is the rounded published report; API computes the exact aligned comparison. Both are record-only for this reader.

Commands from repository root:

```bash
.venv/bin/python3 AGENTS/BRENT/scripts/boot.py --verbose
.venv/bin/python3 AGENTS/BRENT/scripts/eia_weekly.py --local
.venv/bin/python3 AGENTS/BRENT/scripts/composites.py --tanker
.venv/bin/python3 AGENTS/BRENT/scripts/composites.py --wti CLX26.NYM --brent BZX26.NYM --product HOX26.NYM
.venv/bin/python3 -m unittest discover -s AGENTS/BRENT/scripts/tests -v
python3 AGENTS/BRENT/audits/2026-09-09_maintenance/verify_preservation.py
```

November symbols are an explicit dated example, not an automatic roll policy. Select/verify the intended contract before subsequent use. No new background job is installed by these commands.

## Validation

- [41 tests](tests.txt) cover desired behavior for bad quotes, partial/misaligned EIA data, notice selection/mtime, conditional bounds, sub-deadlines, retired CLI, frozen COT boundaries, complete/missing/skewed composite legs, units/maturities/currency and registry routing. These are offline fixtures, not evidence of feed availability at a later time.
- [Network boot](boot-network.txt), September 9 ~12:56–12:57 ET: all nine scripts ran, five OK and four FINDINGS, rc=2. EIA dated observations; BRT-29 unresolved M; Baker Hughes listing timeout; ledger nudge. Two remaining component-only spread probes and the tanker owner-grade requirement are explicit advisories. No script crashed. One final generic summary sentence was corrected after this capture and verified by the boot-output regression; the saved capture is preserved as actually emitted.
- [Local EIA capture](eia-local.txt): correct September 2 numerical report, August 28 observation, twelve-day age; no publication-notice or mtime substitution. rc=2 expected.
- [Live matched-contract diagnostic](futures-network.json): all three November legs passed symbol, currency and timestamp checks; observations 17:01:21–17:01:30 UTC, nine-second separation; rc=0, no source errors. This validates the reader, not official settlements or original BRT-12 ordering. Incidental quotes were not promoted into STATUS/TRADE market state.
- [Preservation receipt](preservation.json): all 49 registry rows retained; only tanker probe, coverage, consumer and explanatory metadata changed. All numeric fields, status/window letters and last_verified dates preserved. Binding SPECS files, TRADE, predictions, thesis/changelog, incident/mail/docket/lesson ledgers, frozen KB/VX/FLOW and historical ratio data match the base. COT executable AST unchanged. All eleven TRACKER alert rows retain exact values and vintages.
- Generated calendar matches all 20 docket events. Read-cap check passes; final exact byte sizes/headroom are in the preservation receipt. Scope does not claim a full semantic check of all historical files.
- [Navigation check](navigation.json): eight touched active documents, zero missing explicit local Markdown targets. A historical FASTOW proposal's nonexistent archive link is now labeled as a proposed path. Weekday checker flags the yearless generated “Sun Jan 31”; its canonical docket date is January 31, **2027**, a Sunday, so no calendar edit is warranted. Lesson index/prose agree (26/26); corrections register reports zero unreceipted named rows.

The old file-health reproduce.py intentionally asserts the pre-repair defects; it is historical evidence, not the acceptance suite to keep passing after repair. New preservation checks are a one-time audit artifact, not another boot obligation.

## Work still open, in order

1. **Remote A5 activation:** read actual configs, apply bounded timing/prompt changes, re-fetch receipts and synchronize the live mirror. Until then, the September 10/11 reads in SCRATCH are owner tasks; unattended coverage is not established.
2. **Published September STEO comparison**, then **September 10 WPSR** with intended September 4 observation and supporting-file completeness. Preserve original SPR two-print windows; no one-print final verdict.
3. **BRT-29 M evidence determination and BRT-12 original construction/upstream credit history.** New diagnostics do not resolve their missing evidence. September 25 observation/September 30 final windows remain as registered.
4. **Current incident/flow/legal evidence:** nine stale ACTIVE plus three other stale present-status incident rows; exact PortWatch targets, same-series Vortexa Sidi, official Russian instruments and SPR contract/authority. No invented current outage total. Baker Hughes timeout is an access finding, not proof of a dead source or invalid registration; recheck at the next primary read.
5. **Receipt/owner work:** XLE receipt remains pending; USO October call remains closed on the already-recorded PROME receipt. No first-sale-price re-ask or assumed resting-order cancellation. Existing trade applicability/history obligations remain at their complete canonical readers.

Ledger-nudge disposition: registry metadata repaired this pass; no new lesson warrants a lesson/index write, no consumed packet warrants a board_log row, and no newly verified facility evidence warrants an INCIDENTS update. Do not reset those stamps to silence the nudge. No source/spec gap is closed merely because its scanner now displays it.
