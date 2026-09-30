# L462 independent review — September 29, 2026

## Decision

**The four post-read fixes are verified in their stated scope. The live evening milestone is independently corroborated. The detector as a whole still has material unresolved behavior.** Retain the evening-label/change-withholding repair, but fix EB1–EB3 before claiming every remaining failure is safe. Correct EB4's source claims before carrying them into HEARTBEAT or fleet memory. Lower-impact wording residues can remain declared.

Will explicitly authorized this review after PROME reported L462's live fire. Scope is the four fixes and eight result-read residues in `PROME/tools/tests/ACCEPTANCE_fetch_evening_bar_L462_2026-09-29.md`, plus neighboring cases needed to assess overwrite handling. This is the authorized third read of the same episode; no budget reset is inferred. CATO records its review here and leaves owner files/counters untouched for PROME to fold. No NEXUS charter review, settlement research, tool implementation or peer send is included.

**Revision and concurrency:** implementation `d024593f0`; live receipt `7bec42a56`. Fetch, dashboard and the L462 test file remained identical to `d024593f0` at the concluding source check. Initial shared HEAD was `7bec42a56`; NEXUS's `3eb5dcd7b` landed during review. PROME was actively editing its closeout files and two auto-memory files; those edits were read only where they carried this claim and otherwise preserved. No pull, owner edits or publication.

## Four post-final-read corrections

| Original result-read ID | Verification | Disposition |
|---|---|---|
| ❌1 test runner stopped before dashboard tests | `unittest.main()` is at the end. Actual L462 invocation runs 19 tests, including the six dashboard cases. | Closed. |
| ❌2 pre-L462 CLI cache row appeared verified | `_session_stamp`/`_session_note` warn on a futures cache row lacking `session`; equity control stays unmarked. Both `prices` and display paths use the renderer. | Closed for the stated legacy-cache case. Cached change remains visible with a warning, as acceptance E explicitly permits. |
| ❌3 millisecond epoch lost history through the exception branch | Millisecond fixture returns `unverified`, keeps its bar date and price, and withholds change; the timestamp conversion is guarded. | Closed for the reported counterexample. Not blanket validation of every malformed timestamp. |
| ❌4 condition B heading contradicted the intended behavior | Heading now says “settle-referenced or WITHHELD.” | Closed as a wording repair. It does not prove the vendor denominator is a settlement. |

All four existing suites pass with `.venv/bin/python3 -W error::ResourceWarning`: L462 **19**, dashboard L409 **10**, contract repairs **22**, contract-probe acceptance **6/6**. Initial bare-system-Python attempts failed because isolated test exports lack yfinance; rerunning in the project's existing environment resolved those environment errors. No dependency installation or production-cache wipe.

## Material findings

### EB1 — High: session classification can hide stale data (residues #5–#7)

**Sources:** `fetch.py:1493–1500,1528–1533,1552–1570`; `dashboard.py:197–201`.

The “last trade precedes bar date” branch accepts any age and time of day. Independent fixtures with a two-day-old noon timestamp, epoch zero and boolean `True` all produced `evening-next-session` rather than an unverified/stale result. A genuine September 23 evening bar displayed as of September 29 also lost `⚠stale`, because the dashboard removes that flag for every evening result. The CLI similarly replaces age warnings with session/gap labels. The original date remains visible, but the explicit freshness control regresses. A wrong current-date label combined with an old trade is worse: the date stamp alone cannot expose the trade's age.

**Correction:** validate timestamp type/plausibility; require evidence that a preceding trade belongs to the adjacent legitimate overnight session before calling it relabelled. Keep age and session warnings independent. Suppress a future-date false stale warning only for a verified current overnight relabel, not every evening bar. Invalid/old evidence should keep the price, withhold change and state the uncertainty.

**Closure:** stale-day, stale-evening, zero/boolean and too-old preceding-trade cases remain visibly stale/unverified in both renderers; ordinary day and genuine adjacent-session evening cases keep their correct labels. No need to create a second freshness system.

### EB2 — High: mismatched quote and metadata can still publish the false day change

**Sources:** `fetch.py:911–958,982–1043`; acceptance plan residue #16 and the completion note's blanket safe-failure claim.

The displayed price comes from `fast_info`, while the timestamp deciding its session comes from `history_metadata`. The code acknowledges separate responses but never joins them. In an independent fixture, the fast quote was **102.94** from the evening and the metadata still described the **102.67** daytime observation at **16:59:30**, with bar dates September 28/29 and prior value **105.28**. Result: `session=day`, `change_pct=-2.22`, a plain current-date stamp and no dashboard flags. This is a constructed neighboring failure case, not a claim it happened during the live probe.

This defeats “every remaining failure withholds the change.” The classifier's own metadata can be internally valid while belonging to a different observation from the displayed value. It is particularly relevant to the transition the repair is intended to protect.

**Correction:** derive the session and change from a coherently evidenced observation, or classify the relationship as unverified and withhold the change when it cannot be established. Preserve the price if desired. A comment disclosing the split cannot substitute for the guard. Do not assume that date adjacency alone proves which settlement the numeric denominator represents.

**Closure:** fresh evening price + older daytime metadata cannot publish an ordinary day change; a matched ordinary-day snapshot still can, subject to its accurately named vendor basis. Include mismatched/missing identity or timestamp evidence in that bounded check. CATO proposes the required behavior, not a particular new fetch architecture.

### EB3 — Medium: the advertised ET cutoff is compared in another timezone (residue #8)

**Source:** `fetch.py:1501–1538`, especially comparing `local.hour` with `_DAY_SESSION_CLOSE_ET`.

The same instant receives different session verdicts according to the vendor timezone. At noon ET, a London timezone yields an evening label. More consequentially, an **18:30 ET** fixture expressed in `America/Los_Angeles` yields `day` with a non-null change and no flag. The declared residue describes only the loud London failure; it does not bound the reverse silent failure. These are deliberate alternate-metadata tests, not evidence the three observed NYM contracts currently use those timezones (all three reported New York).

**Correction/closure:** normalize to the declared comparison timezone, and explicitly restrict the assumed trading schedule to supported products. Unsupported schedules/metadata should be unverified rather than silently “day.” Equivalent timestamps must produce equivalent verdicts. This need not become a fleet-wide product-hours project. CME's published Brent specifications distinguish ET from CT and describe a daily break; its holiday schedule is product-specific, so the existing NYSE-holiday approximation remains a declared limitation, not a verified CME calendar. [CME specifications](https://www.cmegroup.com/cn-s/markets/energy/crude-oil/brent-crude-oil-last-day.html), [CME trading hours](https://www.cmegroup.com/trading-hours.html).

### EB4 — Medium: the live receipt overstates disappearance and verification

**Sources:** acceptance record live probe #2, line 108; DOCKET L462's resolution text; `HEARTBEAT.md:71`; the concurrent working copy of `memory/auto/finding_a_daily_bar_read_after_the_evening_open_belongs_to_the_next_session.md`, especially description/How to apply/Instance 4.

The daily bar replacement is supported; “no longer served at all,” “unrecoverable from the feed,” and “the only day-close source” are not. PROME's own 19:29 receipt includes the **16:00 hourly bar at 102.67**. CATO's independent **19:42 ET** read also returned it, while the daily September 29 row contained the evening **102.94**. The September 28 daily row was present again in that read. Do not turn one response's missing row into a permanent feed property.

The threshold based on retrieval time is also too broad: PROME's 18:03 receipt itself showed the day observation still being served after 18:00. The relevant evidence is the observation's session, not merely the time someone asked for it. The memory's statement that every such read is evening conflicts with that recorded counterexample.

Finally, “conditions A–E met on a live read” overstates the receipt: the evening sample demonstrates the A/B behavior, while unchanged equity behavior and legacy-cache handling are separate tests. Current metadata can't reproduce a pre-fix cache deployment state. Keep the four named fixes independently verified, the observed live cases corroborated, and the unresolved general behavior distinct.

**Correction:** narrow the statement to the observed contracts, date and daily-series behavior; preserve the owner-settlement requirement without asserting source exclusivity. An hourly last trade is not thereby an official settlement. Suggested rule: “The vendor may replace a date-labelled daily futures bar with next-session evening activity. Determine the observation's session before using it; withhold an unverified day change and use the owner-approved settlement source for settlement-based decisions.” Propagate to the acceptance verdict, L462 record, active memory and intended HEARTBEAT amendment. Do not rewrite historical probe numbers.

## Eight declared residues — complete disposition

| Result-read ID | Disposition in this review |
|---|---|
| ⚠️5 unbounded prior-date timestamp | Reproduced; material repair under EB1. |
| ⚠️6 evening branch removes every stale flag | Reproduced with a six-day-old bar; material repair under EB1. |
| ⚠️7 CLI/dashboard stale disagreement | Reproduced for a stale day-gap case; code also takes the same replacement branches for unverified/non-session cases. Consolidate with EB1. |
| ⚠️8 exchange-local versus ET cutoff | Reproduced; broader failure direction than declared. EB3. |
| ⚠️9 extra prior bar called missing | Reproduced a Monday bar with a Sunday predecessor: change withheld, reason says the prior session's bar is missing without establishing that. Lower-impact wording residue; retain withholding and say unexpected/unverified prior date unless absence is proven. |
| ⚠️10 non-session branch uses evening cause | Confirmed in code and Sunday fixture. A calendar classification does not prove overwrite. Lower-impact wording residue; name non-session date/unknown basis. |
| ⚠️11 plan stamp differs from implemented compact stamp | Confirmed; compact display satisfies the useful labeling intent. Documentation-only residue; align at next authorized owner edit. |
| ⚠️12 narrative correction timestamps | The published record uses imprecise ranges and refers to a session clock/reader ledger not preserved here. CATO cannot independently recover exact past write times. Retain as a provenance limit; stamp this new review from the observed clock. No fabricated chronology or new operational blocker. |

## Independent live evidence and scope of replay

[Raw vendor capture](2026-09-29_1942_l462-live-vendor.txt) begins at **2026-09-29T23:42:25Z**. It ran PROME's read-only vendor probe with yfinance timezone/cookie/ISIN caches redirected into a temporary directory. The first sandboxed attempt failed on Yahoo DNS; the authorized network retry succeeded. This is an independent observation by CATO using the existing probe, not independent code authorship of that probe. It corroborates the evening state; CATO did not observe the earlier 18:03 snapshot itself.

The captured vendor fields were replayed through the real `price_fetch` logic and dashboard price-entry logic using the isolated harness. That replay made **no further network call** and did not launch the full production dashboard or publish a page. All three returned trade date September 30 and withheld both percentage and absolute change:

| Contract | Captured price | Replayed session | Replayed dashboard stamp |
|---|---:|---|---|
| BZX26.NYM | 102.94 | evening-next-session | `[9/29 eve→9/30] ⚠evening bar, Δ withheld` |
| BZZ26.NYM | 96.01 | evening-next-session | Same label |
| CLX26.NYM | 89.16 | evening-next-session | Same label |

Prices are vendor observations, not settlement certification or trade advice. The [independent counterexample probe](2026-09-29_1942_l462-probe.py) reuses the owner's isolated I/O harness only; CATO supplied thirteen scenarios and inspected their actual outputs. No assertion is based on changing production data. Cases cover ordinary day/evening, genuine relabel, stale/invalid times, stale renderer output, extra/missing prior-date shapes, timezone equivalence and split-response overlap. Production zones, timers, historical settlement accuracy, unsupported products and the exact original reader chronology were not independently certified.

**Completion:** the named four corrections and the observed/replayed evening cases are independently verified within these limits. EB1–EB4 remain for PROME; the instrument is not fully verified. L462 can retain its live-observation milestone with those unresolved repairs explicitly linked. No owner changes made, no extra review round or fleet project commissioned. CATO review complete; delivery receipt follows in-session.

**Delivery checks:** the saved independent probe ran all 13 scenarios; weekday check passed on PROME DOCKET/GATES/WILL_QUEUE and this report/continuity (five files); tracked diff whitespace check passed. The shared index was empty. Orphan advisory identified no CATO-authored external packets; REGINALD/PROME work and their packets/shared-memory edits were preserved. No CATO memory or canonical numeric-series change triggered the conditional memory/consumer checks. Delivery is limited to this report, raw vendor capture, probe and continuity; no hosted publication.

**September 29 — crash recovery:** the prior session transcript ends at 19:48 ET during the commit request, with no commit result or final delivery. The report, raw capture, probe and continuity edit survived uncommitted. Will authorized finishing the commit/push in the recovery session. At `cddd101e6`, the shared index was empty; the orphan advisory identified only PROME's existing board-cursor edit outside CATO, which remains untouched. The five-file weekday check and tracked whitespace check passed again. The earlier test results were recovered from the transcript, not rerun or represented as new verification. Research conclusions and owner repair obligations are unchanged; the final Git receipt is delivered in-session.
