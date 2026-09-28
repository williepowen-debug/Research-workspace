# BOND rates-context implementation review

**Current disposition, September 28, 2026:** the three components are implemented and wired into the normal boot path; the quoted readings reproduce on the stated source basis. **Accept the useful implementation, but request bounded corrections before calling the coverage gaps fully closed.** Independent failure-path cases expose stale/partial-data false clears and a limited calendar guard. No rebuild, rollback, new research commission or change to registered thresholds is warranted. The ordinary arithmetic is not the problem.

Will asked CATO to analyze BOND's completion claim at `a5dbeb21e` and make sure the work was done properly. Code at that commit was unchanged through the inspected HEAD (initial shared HEAD `cf069fdb3`, advancing concurrently during review). CATO did not implement this BOND change. This is an independent source/code/behavior review, with CATO-authored test cases. No domain files were edited and no messages were sent. Recommendations do not grant trade or launch authority.

## What checked out

- `CLAUDE.md` boot step 6 invokes `boot_recompute.py`; its normal path imports `rates_context`, adds `run()`'s finding count to the boot result, and catches failures as findings. The three component calls exist. An earlier boot fetch failure returns a non-pass before reaching this block; this is not evidence that the block silently passed. Wiring is verified, not every future session's compliance with boot instructions.
- BOND's `rates_context.py --selftest` passed **14/14**. These cover arithmetic, date parsing, selected edge cases and declared labels. They do not establish full I/O/freshness/calendar coverage.
- CATO independently downloaded the NY Fed workbook and extracted `ACMTP10` from **ACM Daily**: **0.774716 on September 25**, versus **0.635932 on September 18** = **+13.8784bp across five observations**. Correct series, units and computation. [NY Fed source workbook](https://www.newyorkfed.org/medialibrary/media/research/data_indicators/ACMTermPremium.xls).
- A separate vendor download at **17:58 ET** found 17 September-28-dated contracts through January 2028; February 2028 was dated September 25 and was excluded, while March/April were unavailable. The peak was **4.855003% in November 2027**, **+18.0000bp from September 21**. January 2028 was about 4.5bp below it. This reproduces the quoted vendor reading, not an official settlement or an independent quote source. [Saved source-check extracts](2026-09-28_1744_bond-rates-context-source-checks.json).
- November 2026 implies **4.050003%**. Latest published [EFFR](https://fred.stlouisfed.org/series/EFFR) is **3.88% for September 25**. Their difference is about 17bp, or **68% of 25bp**. The official [Fed calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) has the October 27–28 and December 8–9 meetings, with none in November. Thus the October shortcut is numerically defensible **conditional on a hold-or-25bp-hike interpretation and the stated EFFR assumption**; it is not a reconstruction of the full CME probability tree. [CME methodology](https://www.cmegroup.com/articles/2023/understanding-the-cme-group-fedwatch-tool-methodology.html).
- [KW/FRED THREEFYTP10](https://fred.stlouisfed.org/series/THREEFYTP10) confirms **0.9595 for September 18**. The model and lag are disclosed. Its ten-day observation age is below the tool's explicit 14-day stale threshold; this is not fresh corroboration of the later sell-off.
- [PMMS](https://fred.stlouisfed.org/series/MORTGAGE30US) is **7.03% on September 24**, and [DGS10](https://fred.stlouisfed.org/series/DGS10) is **5.18% that date**: **185bp**, inside the 180–230bp spread band. The tool triggers a review, not a trade or automatic vector reactivation, outside the band. The unmonitored GSE-release and active-MBS-sales legs are explicitly disclosed.
- [T5YIFR](https://fred.stlouisfed.org/series/T5YIFR) is **2.35% on September 28**, so **15bp** below 2.50 is correct. Both live STATUS distances were updated. This is a catch by the existing boot/drift machinery during the first newly wired run, not a new T5YIFR calculation inside `rates_context`.
- The archived STATUS snapshot is **25,020 bytes, CRC32 1800580424**, exactly as claimed. Snapshot-to-current differences are confined to the session header, archive pointer and top-summary block. Current STATUS is **23,641 bytes**, below 75% of its stated 32,550-byte budget. No deletion outside that bounded condensation was found.

## Findings and minimum corrections

### BR1 — High: stale inputs can report a clean result

**Evidence:** `monitors/rates_context.py:185` consumes the latest EFFR without checking its observation age; `:85` defines live futures solely as bars sharing the newest date in the returned strip. Neither checks that the newest date is timely. `:280` accepts PMMS and the latest prior Treasury observation without checking either freshness or join distance. Only the term-premium block enforces `STALE_DAYS`.

**Independent cases:** with today fixed to September 28, all futures dated August 10 still print a terminal and October reading with **0 findings**; an EFFR anchor dated August 7 also produces **0**. A mortgage/Treasury pair dated August 13 prints **185bp, spread leg not fired, 0 findings**. A current mortgage quote paired with an August 13 Treasury quote does the same. Fetch success and dates printed on screen do not make these safe automated clears.

**Correction:** add source-specific age/publication checks for EFFR, futures and weekly PMMS, plus a bounded prior-date Treasury join. Respect weekends, holidays and ordinary publication lag; do not apply a simplistic same-calendar-day rule. Stale or temporally incompatible evidence should be **GAP plus a finding**, not a current no-fire or complete terminal assessment. Historical values may still be displayed with their dates.

**Closure:** demonstrate valid weekend/weekly-release cases still work, and the stale-strip, stale-anchor, stale-PMMS and stale-join fixtures cannot return a clean current verdict. Owner chooses the tolerances and documents their source; CATO has not installed new policy thresholds.

### BR2 — Medium: futures coverage is validated before stale contracts are removed

**Evidence:** `:197` requires six raw contracts, then `:203–204` removes older-dated contracts. It never revalidates the usable set. `:231–232` prints “odds not computed” when a needed contract is absent but adds **no finding**.

**Independent cases:** six raw contracts with only the current month on the newest date yield a one-contract **TERMINAL**, no usable next-meeting calculation, and **0 findings**. A separate six-current-contract case missing November also returns **0** despite the explicit missing-meeting-contract warning.

**Correction:** validate usable coverage after the freshness filter, including the required meeting contract and the horizon over which the claimed peak is meaningful. Report unavailable required calculations as findings. Label the output **peak of the available strip**, with its horizon; a short or truncated strip cannot establish the cycle's terminal rate. Unlisted far contracts beyond the supported horizon need not create permanent alarms.

**Closure:** the healthy fixture and actual 17-current-contract snapshot remain usable, while the one-current-contract and missing-November cases are visibly incomplete and nonzero. Do not add automatic trades or change FOMC probability assumptions to force a result.

### BR3 — Medium: the calendar check detects an empty future docket, not a missing next meeting

**Evidence:** `:225–230` checks only whether any future FOMC decision row exists. It chooses the earliest surviving row without comparison to the issuer's schedule. This is useful but narrower than preventing recurrence of a missing-meeting error.

**Independent case:** remove October 28 from the test docket while retaining December 9. The tool calls December the next meeting, assumes EFFR holds until then, prints **124% of a 25bp move**, and returns **0 findings**. The actual current October row is correct; this is a counterexample to coverage, not a claim that tonight's docket missed October.

**Correction:** use an issuer-checked next-meeting/calendar snapshot (freshness/provenance explicit), or clearly limit the tool to **next docketed meeting** with a calendar-completeness GAP until the existing human issuer-calendar check is recorded. A second hand-maintained unverified calendar would not solve it. Keep raw bp pricing distinct from probabilities: outside a validated hold/+25bp case, do not describe bp/25 as the probability of a hike.

**Closure:** deleting an earlier meeting while leaving a later one must not produce an unqualified next-meeting claim. Verify the no-November assumption from the issuer-backed calendar rather than absence from an incomplete local list. No need to build a full FedWatch clone.

### BR4 — Medium: the morning bar label asserts a provenance it cannot know

**Evidence:** `bar_timing_label` decides entirely from the current clock. At **11:00 ET on a weekday**, it says the last bar is the prior session's close even though a vendor daily bar can already be today's evolving bar. The selftest enshrines two labels but does not test this ordinary morning-boot case. The 14:30 cutoff also conflates a post-settlement trade with the next session; a settlement time is not the session rollover time.

**Correction:** always retain the vendor/not-settlement caveat; label the actual returned bar date/session and capture time. If intraday status cannot be established, say it is unknown. Do not infer prior close or next session solely from the wall clock.

**Closure:** a morning capture containing today's bar must not label it yesterday's close. Cover ordinary morning, post-settlement/pre-roll, evening rollover and weekend captures using actual bar timestamps. No impact on the correctly qualified 17:38 vendor reading established here.

## Interpretation limits, not another research assignment

The two rising readings are **consistent with both channels contributing**, but they do not constitute a causal decomposition of this sell-off. The FF change is **September 21–28** in a roughly one-year-forward monthly average; the ACM change is **September 18–25** in a modelled ten-year term premium. KW ends earlier still. Align dates and horizons before making a stronger attribution, or keep the conclusion qualified. ACM is an estimate, not an observed independent risk price; [NY Fed's explanation](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs) explicitly identifies its model basis. WQ-317 remains the already-approved bounded comparison; do not commission a duplicate study.

The mortgage spread is an explicitly defined **weekly survey minus dated daily Treasury proxy**. [Freddie Mac](https://www.freddiemac.com/pmms) describes a Thursday-through-Wednesday application-rate average, so a Thursday publication stamp does not make both legs synchronous market quotes. Keep that basis visible, particularly when only 5bp from an edge. This review does not move the registered band or claim it fired. The two non-spread restart conditions remain uncovered as already disclosed; all three coverage topics are not equivalent to all three mortgage trigger legs being automated.

## Verification, delivery and stopping point

[Independent offline fixtures](2026-09-28_1744_bond-rates-context-fixtures.py) mock I/O and call the actual BOND policy/mortgage functions. Run with `.venv/bin/python AGENTS/CATO/runs/2026-09-28_1744_bond-rates-context-fixtures.py` from the repo root. **12 expectations: 4 met / 8 unmet** at the reviewed revision; exit 1 is expected because this is a review regression suite exposing open defects. Passing controls: healthy October calculation, empty-future-docket flag, healthy 185bp spread, 231bp review trigger. Eight failures map to BR1–4; they are not eight separate production incidents. No code or source fixtures were changed to manufacture a live market signal.

Direct source checks were independent of the BOND parser. The futures re-read uses the same underlying vendor and cannot validate official settlements. NY Fed xls and vendor extracts are saved beside this report; FRED/Fed/Freddie/CME pages were read via browser. Network access for two direct downloads required sandbox escalation and succeeded. Full BOND boot was not executed: its existing cache bust deletes shared FRED cache entries, and the bounded review did not require mutating those caches. Normal-path wiring/return propagation was inspected statically; component behavior was tested in isolation. Existing broad closeout checker's historical rc=0 remains owner-reported, not independently rerun or disproved by its out-of-scope misses.

Only CATO report, fixtures, source extracts and continuity changed. Concurrent owner commits were preserved; no owner edits, broker actions, packets, launches or hosted publication. Initial working tree was clean; no pull was performed during the live shared-session review. Applicable documentary checks and final exact-path Git delivery are recorded below/in the in-session receipt. The review assignment is delivered; **BR1–4 remain owner repair work**, not a claim that CATO fixed them. No automatic next review; orient and await Will.


Closeout checks: root orphan advisory clean outside CATO; three-file weekday claim check passed. Exact-path whitespace checks passed. No auto-memory, domain STATUS, registered figure or ledger changed, so those conditional checks do not apply. Four CATO files form the delivery. Known review-fixture failures are preserved as evidence, not reported as passing implementation tests. Final commit/fresh-fetch push receipt is in-session.
