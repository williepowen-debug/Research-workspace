# HANS — third bounded correction review

**Disposition: PARTIAL; substantial repairs verified, original obligations still incomplete.** Will supplied HANS's final receipt through **`c7d02d7809f3dffc83a30c8c0c2b353a03936ebe`**. This pass checks the changes since `3cad378f0` against the six residual findings in the [second review](2026-09-19_1327_hans-correction-recheck.md). It is independent assessment of HANS's changes and author follow-up on CATO's earlier findings, not a general certification or new instrumentation assignment.

HANS's 120-test suite passes in an isolated snapshot; unmodified doc_audit has no blocking findings. Fresh fetch confirms the reviewed commit is on origin/master. Other desks have since advanced the shared branch, so c7d02d780 is no longer HEAD. Matching commit IDs establish identical committed trees; they do not establish an unmodified working tree or correct behavior. No shared HANS files were changed and no live authenticated fetch or operational closeout was run.

## Verified progress

- AGSI current and historical fill now reject NaN, infinity and out-of-range percentages; current dates reject future and ancient observations. The original four-year norm fixture is still refused.
- BoE rejects the original future and 12-day-old cases and selects the greatest valid date in shuffled responses.
- The runner rejects real Python tracebacks, missing scripts, argument errors, signals, timeout results and empty-success results for the three formerly permissive steps. Legitimate rc=1 nudge output remains accepted.
- C9 now catches the original unrelated-following-history clause, cross-series band collision and named-series spelled-out-unit examples. Historical comparisons and the sampled real band do not spuriously fire.
- C12 catches additions to both previously unique and already-exempt ML IDs. Its frozen multiplicities exactly match the original 95 duplicate groups, rather than absorbing a new collision. Duplicate prediction and FLOW identifiers are now detected.
- The ESRB primary note explicitly withdraws the net-position credit-loss bound at the offending section; LAST_COMPLETION carries the corrected registered forecast outcome, 120-test count and uncertified status. No replacement probability or forecast grade was assigned by CATO.

These are real repairs. The remaining failures below are why the original six cannot yet be closed wholesale.

## R1 — High: storage dates are still not validated against the requested historical dates

`AGENTS/HANS/scripts/fetch_eu.py:303–325` builds five date requests, then copies each requested year into the result without checking the returned gasDayStart. Five responses all dated **2020-01-01**, or five responses with **no date**, still form a named 2021–25 norm. With those wrong-date responses carrying fill 50 and a valid current 69.06, the real renderer prints **green +19.06pp**, reports `failures=[]`, and does not report a T-08 breach.

The current parser also accepts a **2025-09-17** observation on 2026-09-19; `_obs_date` only excludes dates older than two years. A JSON boolean `true` is accepted as 1.0%. These are injected counterexamples, not claims about live AGSI payloads.

**Required:** exact requested/returned date and identity validation for each historical record; reject missing dates and non-numeric schema types. Define usable current-data age separately from the two-year plausibility check. Do not apply the two-year cutoff to legitimately old norm years. Invalid observations must produce unknown/failure, never a qualifying exit day. The existing five-day fire-exit rule remains unchanged.

## R2 — High/medium: a real “nothing scanned” error still produces 8/8 success

`AGENTS/HANS/scripts/closeout_check.py:73–112` retains rc=1/2 acceptance for the non-strict consumer commands and uses `SELF mode` as the self-scan marker. The real root consumer, invoked against a nonexistent fixture agent directory, exits **2** with:

> self mode scans that directory and nothing else; nothing scanned.

That error contains the accepted marker. Feeding this actual child result into the self-scan step yields **MECHANICAL: 8/8 executed · 0 failed**, runner exit **0**. It is the root tool's real missing-directory error, not an invented error-code meaning. `scripts/consumer_check.py:1027–1029` is the source contract.

Separately, real subprocesses that print `CONSUMER CHECK`, `SELF mode`, or `HANS` and then terminate via SystemExit(1) all pass their corresponding steps. Those markers are headings, mode names or an agent name, not terminal completion receipts.

**Required:** reject nonzero status for these non-strict consumer invocations; recognize nudge's actual documented advisory result separately. Verify a terminal result, rather than an arbitrary substring that also appears in errors. Preserve diagnostics. This reproduces a false-success capability; it does not prove any child failed during HANS's reported live closeout.

## R3 — Medium: BoE parser improved; canonical benchmark coverage is still omitted

`fetch_eu.py` now uses a **uniform ten-calendar-day ceiling**, so a nine-day-old daily reading is accepted. This is a real policy limit, not the requested series-specific publication/holiday contract. The original 12-day-old fixture is repaired and should stay closed as that particular case.

The more immediate outstanding obligation is unchanged: `scripts/boot.py:141` names only UK 30Y among manual gilt legs; `CLAUDE.md:35` says UK 10Y is auto-pulled and only 30Y remains manual. Yet the fetched par yield is deliberately a cross-check and cannot supply the registered benchmark T-06. `fetch_eu.main()` repeats the incomplete manual perimeter. Its module header and BoE comments disagree about coverage as well.

**Required:** restore the UK 10Y benchmark to the explicit manual perimeter; describe par automation separately. Document/review the ten-day allowance without pretending it establishes expected publication freshness. No 30Y implementation is authorized by this finding.

## R4 — Medium: C9 still silently clears unrelated current values and dated stale claims

`doc_audit.py:270–300` still clears a retired number if its replacement numeric string appears **anywhere on the line**. The original class remains reproducible:

- `EU storage gap is -19.7pp; unrelated figure is -15.99.` → no C9 finding or advisory.
- `As of 2026-09-19, the current EU storage gap is -19.7pp.` → no finding or advisory; the new date exemption treats even an explicitly current dated assertion as history.
- `The gap is -19.7 percentage points.` → still silent, although the version naming EU storage now fires through the name heuristic.

**Required:** distinguish a current dated assertion from a historical statement and bind replacement values to the same assertion. Either normalize common units or disclose/advisory-report uncertainty. A heuristic may have explicit limits; it should not be described as closing this property while these original classes remain silent. There is no request for a general natural-language parser.

## R5 — Medium/low residual: fire-record keys remain outside C12

The ML multiplicity repair and prediction/FLOW coverage **are verified**. C12 still does not include `registry/HANS_T_FIRED_LOG.tsv`'s `fire_id`; appending a duplicate HANS-F-001 creates no C12 duplicate finding. This key was explicitly included in the previous acceptance conditions. Cover it or explicitly carry it as an accepted limitation. No historical ML renumbering is needed.

## R6 — Medium residual: active STATUS still contains the broken rationale and dead pointers

The primary note and LAST_COMPLETION repairs are verified. STATUS remains unchanged at these important entry points:

- Line 87: the HNS-09 basis is still the fragment **“structural: euro-area banks are net DEBTORS to NBFI, so the credit channel is ** Q3 results…”**. It does not supply the corrected reason recorded in the primary note.
- Lines 58 and 85 point to missing **§SESSION 4**, including the route to HNS-07's grading rule.
- Line 17 advertises **13 checks / 86 tests** while the handoff says 14 / 120. Line 3's 67-test boot receipt is distinguishable as historical, but the live instruments line is not.

**Required:** replace the broken active rationale and current instrument counts, and link the actual rule location. Do not merely add another corrective header. PROME's earlier consumer corrections remain credited in the prior report; recipient integration was not re-certified here.

## New C0 control: limited evidence, not a seventh repair demand

C0 counts matching **comment headings**. Its new regression test deletes a heading while retaining the implementation. I tested the complementary case: removing C14's implementation while retaining its heading allows an injected `## SESSION 99` block and still reports **14/14 checks present**. Thus C0 proves declared source headings are present, not that checks executed. This is consistent with its explicit source-census design, but limits the `C0-CHECKS-RAN` label and any assurance drawn from it. Retain behavioral tests; this review does not commission another general framework.

## Evidence and stopping point

[Probe](2026-09-19_1424_hans-third-pass-probe.py) · [results](2026-09-19_1424_hans-third-pass-probe.txt) · [shared review checks](2026-09-19_1424_review-checks.txt). HANS and root scripts are pinned in an isolated copy; ancillary owner paths and Git history are read-only references to the shared workspace. The source was saved from the tested temporary probe with only its repository-root discovery generalized. Assertions deliberately distinguish successful repairs from reproduced residuals. No report claims that invalid data actually occurred in production.

**Recommended next action:** prioritize R1 and R2, then remove the remaining misleading active text. The other checker gaps may be explicitly carried as provisional limits if Will wants to stop; don't equate a published closeout with certification. No additional review or repair cycle is automatically commissioned by this report. Current assignment is delivered; next session should orient and await Will. Other CATO's continuity is preserved; this report holds this task's resume point. No owner messages or publication were sent.
