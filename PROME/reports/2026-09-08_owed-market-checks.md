# Owed market checks — 2026-09-08

Owner: PROME (Codex). Recorded 2026-09-08 16:24 ET. Scope: Will's “yes go ahead” to the 9/7 handoff's owed market checks. Consumer verification; domain owners retain grading and Will executes at the broker.

## Decision at the close

**VERIFIED: XLE's 9/8 regular-session close is $64.77, below the $66.50 hold condition.** WQ-168 row ⑦ therefore selects the already-approved exit: sell the two XLE Sep-30-2026 $65 calls at the bid on the 9/9 open, subject to the live broker position. No order placed or fill reported in this session. DOCKET L252 is resolved as the close-test observation; L253 remains PENDING for Will's execution.

Authority: `PROME/WILL_QUEUE.md` row 168 (Will 9/3 12:45) and `PROME/inbox/processed/2026-09-03_from-TERRY_expiry-pass-Sep18-Sep30-seven-lines-007-grade-UNKNOWN-mirrors.md` §⑦. The registered close test is unchanged.

## Verified observations

Price source: Yahoo via yfinance, MIRROR. Second pull began **16:21:41 ET**; unadjusted daily bars agree with regular-market metadata. XLE/USO/TLT market timestamp = 16:00:00 ET; WAL = 16:00:02 ET. The earlier 16:13 pull showed provisional XLE $64.76 / WAL $80.00; use the later session-stamped observations below. Evidence: `PROME/reports/2026-09-08_owed-market-checks_evidence.json`.

| Object | Observation | Consumer consequence |
|---|---|---|
| XLE, 9/8 regular close | $64.77 | $1.73 below $66.50; approved next-open exit selected |
| WAL, 9/8 regular close | $79.94 | Below $81.90; ROLL70-EXIT remains 0 of 3 on the observed close series; REGINALD owner grade owed |
| USO, 9/8 regular close | $146.03 | Above $135; USO135C give-back leg B not triggered; existing time stop remains |
| TLT, 9/8 regular close | $82.20 | Context only; cannot substitute for official DGS10 |
| DGS10, **9/4 observation** | **4.78%** | 28 bp above 4.50%; 007 remains 0 of 5 through available officials; TERRY owner grade still owed |
| DFII10, **9/4 observation** | **2.43%** | 7 bp below the 2.50% add line; NO-ADD |
| HY BAMLH0A0HYM2, **9/4 and 9/7 observations** | **2.68% = 268 bp each** | Neither <260 nor ≥280; HY re-kill remains 0 of 2 |

Rates/spread source: uncached [FRED DGS10](https://fred.stlouisfed.org/series/DGS10), [DFII10](https://fred.stlouisfed.org/series/DFII10), and [HY OAS](https://fred.stlouisfed.org/series/BAMLH0A0HYM2), retrieved at the second pull; FRED is the registered grading series. DGS10/DFII10 first pulls ended 9/3; the later uncached API pull returned 9/4. The browser-rendered H.15 page still showed its 9/4 release/9/3 observations, so independent H.15 confirmation of 9/4 is **UNKNOWN**, not claimed. September 8 yield observations were not returned; no proxy substituted.

**VERIFIED calendar discrepancy:** NEXUS `PREDICTIONS_MONITOR.md` L1b says 9/7 is a holiday with no observation. FRED's public HY page and uncached API both actually publish 9/7 = 2.68%. The calendar premise is false for this series. **INFERRED consequence:** the 268-bp 9/4 and 9/7 observations break any qualifying A/B run crossing them; the remaining possible three-observation run is 9/8–9/10. L1b's necessary 9/8-and-9/9 test therefore survives on the observed values, but the eligible-cell explanation needs owner verification. No C#2 grade or split change made; grade date remains 9/11. Route through WALTER to NEXUS/LIQUID.

## WALTER L273

**VERIFIED:** generator `--check` returns CHECK PASS; 891 IDs identical, zero hand-only markers at risk. Live `BOARD/INDEX.md` still starts with the hand-maintained preamble; no generated banner or committed cutover receipt found in the inspected live index, owner STATUS, or design record. **Cutover remains unverified/PENDING.** Parity readiness is not execution.

The `BOARD/INDEX.generated.md` firetime warning is a mention of an unused default output path: design §4 step 2 explicitly says the soak runs `--check` without writing. My boot carry treating that missing file as the cutover artifact was incorrect. The other firetime hits are the DEWEY literal-glob pointer and a quoted, already-declared bad canon pointer in the 9/7 ruling record; no new DATE flag was reported.

## PJM / DOE L249 — interim only

**VERIFIED:** [DOE Order 202-26-41](https://www.energy.gov/ceser/federal-power-act-section-202c-pjm-interconnection-llc-pjm-order-no-202-26-41) expires at **23:59 ET 9/8**. [PJM's board](https://emergencyprocedures.pjm.com/ep/pages/dashboard.jsf), stamp **9/8 15:50:16 EPT**, contains no EEA-2/3, voltage reduction, load shed, or backup-generation deployment directive among the displayed postings. It includes local transmission warnings and maintenance notice #105504 (possible website interruption, not a grid emergency).

PJM notice **#105500 (9/4)** says it identified no reliability need for the specified resources for operating days 9/5–9/8. This is not evidence that backup generation was actually deployed. **SEARCH-NOT-FOUND:** no extension in the inspected DOE order page, displayed PJM postings, or targeted DOE search. The DOE orders index could not be opened; extension absence is not an exhaustive certified negative. **UNKNOWN:** tonight's final lapse/extension outcome. Re-check after expiry; WATT owns the grade, including its separate seven-clear-day de-escalation clock. No score lowered and no NEXUS evidence type counted.

## FT-10 / L275

**VERIFIED:** Cboe's [official SKEW CSV](https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv) still ends **9/4 = 151.58**, preceded by 9/3 = 150.63. **UNKNOWN:** the 9/8 bar. Preserve the known 2-of-4 run without advancing or resetting it. Earliest possible fire remains the 9/9 close, contingent on both missing future grades. Re-fetch when the publisher adds the dated bar; RED grades, VIOLET carries the instrument.

## Handoff and delivery limits

Available now: closing-price test, 9/4 official refresh, WALTER parity consumer read, interim PJM check, and Cboe publication check. Pending: Will's 9/9 XLE execution; WALTER cutover; PJM post-23:59 outcome; Cboe 9/8 publication; owner grades. BROCK remains held to 9/9 by the explicit handoff.

Claude Code fleet `ListAgents`/`SendMessage` tools are unavailable in this Codex session. Live desk presence is **UNKNOWN**; no desk was declared dark from that absence and no duplicate desk was spawned. File packets to TERRY and WALTER preserve the work; doorbells and recipient consumption remain unverified. This session did not execute trades or change owner domain files.

## Validation

Evidence assertions PASS (regular-session XLE metadata/bar agreement, FRED dates/values, Cboe latest bar). Docket row positions and all non-target fields preserved; execution L253 remains PENDING. Weekday claims and diff hygiene PASS. The generated calendar was refreshed. The broad SCRATCH prose checker still flags inherited date associations; comparison against the original file found no new DATE diagnostics. Its narrower boot scope is the catalyst-calendar section. The calendar renderer emitted its advisory block-size warning; no content was hidden to suppress it.
