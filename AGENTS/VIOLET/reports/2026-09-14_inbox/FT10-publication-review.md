# VIOLET decision on the Wednesday publication question

**Written:** 2026-09-14T23:34:11-04:00. **VIOLET review complete; CONCUR WITH REPAIR. RED/PROME chain adoption is pending, not claimed.** Requested by Will in this VIOLET session: resolve the Wednesday rule question, formally process the reviewed inbox, and reconcile the docket descriptions. This authorizes the review and coordination; it is not a claim that Will approved unseen rule text or that VIOLET owns RED's grade.

**Timing:** the September 14 bar is already known. This is a dated revision proposal before the September 15/16 observations, not a re-labelled pre-September-14 registration. RED's original framework and trigger registry remain unchanged by VIOLET.

## Decision

Accept the distinction between an unresolved publication frontier, a genuinely missing session and a non-session. **Reject date/row-count/hash change as proof that the target session was published or should be present.** Those describe the retrieved representation, not its coverage. An unchanged file can be cached, re-served or regenerated without that bar. A changed file can contain only historical corrections or formatting changes. None proves the frontier advanced through the missing date.

## Exact replacement allocation offered to the registered chain

Evaluate expected sessions in chronological order using the publisher of record and the declared session calendar. Preserve all previously evidenced grades; a weaker later fetch does not erase earlier evidence.

| State | Required evidence | Disposition |
|---|---|---|
| NON-SESSION | Established exchange closure under the existing owner rule/calendar, never absence alone | Outside count domain; bridge. A holiday-labelled VIX observation cannot turn a closure into a session. |
| PUBLISHED OBSERVATION | Valid target-session value in the declared Cboe SKEW archive, validated for date, schema and numeric value | RED applies the existing operator, tie precision, sustain and reset rules. A known sub-threshold bar resets even if a later bar is unavailable. |
| SESSION IN PROGRESS | Known open session has not completed | No closing grade yet; no advance, reset or weight action from absence. |
| ACCESS / PARSE / PUBLICATION STATUS UNKNOWN | Timeout, HTTP failure, invalid/ambiguous payload, calendar uncertainty, or closed latest target absent with no proof that archive coverage passed it | HELD at the last supportable state; no new fire, no advance, no invented bar, no reset solely on unavailable evidence. Grade remains explicitly owed. Do not label the cause “not yet published” as a proven fact. |
| MISSING SESSION INSIDE PUBLISHED COVERAGE | Target was a completed exchange session, it is absent/unreconciled in a valid grading archive, and a **later completed-session SKEW bar is actually present** in that archive (or an explicit publisher statement identifies this specific omitted session) | Existing clause 6: gap breaks the candidate run. Name the missing date, later witness date and saved source. Do not bridge across the hole to complete a sustain. |
| LATER CORRECTION / RECOVERY | Publisher later supplies or changes the affected bar | Dated re-derivation with prior grade struck/annotated as a revision, never silently overwritten; original thresholds remain. |

**Precedence:** calendar/session identity first; validate the source; consume available chronological observations and genuine internal gaps; stop at an unresolved frontier. HTTP 200 alone is not validation. Changed bytes alone do not prove coverage. A later-bar witness must itself be plausible, completed and from the declared series. Existing authoritative evidence remains usable through a subsequent outage; unknown access never rolls a known failure back to “held.” An explicit publisher statement is evidence of omission, not a substitute numeric observation for completing a fire.

**No new deadline or grace period:** at the September 16 grade attempt, save a receipt and mark publication/access uncertainty explicitly. Re-attempt at the next owner session and keep the obligation open until authoritative evidence resolves it. Elapsed wall time alone neither completes nor kills a run. No fabricated 17:00 publication guarantee. A stale or unavailable archive cannot produce a new fire in either bullish or bearish direction.

## Counterexamples that reject the original discriminator

1. Prior file ends Sep 15. New file corrects Sep 1 but still ends Sep 15: hash changes, Wednesday absent. **UNKNOWN**, not missing Wednesday.
2. Prior and new files have equal row counts, but new file drops Sep 1 and adds Sep 17; Sep 16 is missing. **MISSING Sep 16**, despite equal counts.
3. Byte-identical response with no Sep 16: **UNKNOWN**. It does not distinguish a cached response from a genuinely unregenerated archive.
4. Valid archive contains Sep 17 but no Sep 16, both exchange sessions: **MISSING**, even if the numeric endpoint happens to resemble a prior value.
5. Wednesday bar is present below 150; Thursday fetch fails: Wednesday's reset stands. An outage cannot preserve a run the known bar already broke.
6. Archive finally supplies the missing Wednesday bar: revise and re-derive dated; do not delete the earlier missing-data grade.

The worked cases are formalized in `publication_cases.py` as an offline specification check. It does not fetch, grade FT-10, write a registry, or establish owner approval.

## Other defects noticed in the supplied framework

- §5 still quotes the withdrawn **0.79% mirror defect rate**, despite RED's own operative-basis correction. Remove the obsolete rate from current prose or point to KB-RED-093; retaining the provisional-only mirror rule requires no rate.
- “Exactly 150.00 FIRES” is only true when it is the final required observation. A tie satisfies the non-strict observation predicate; sustain still governs the fire.
- The published count receipt says 9,223→9,226 rows but describes two added bars. Those row counts differ by three. Recount parsed records and separate header/blank lines from data rows; do not use the claimed byte/row arithmetic as a publication witness.
- The quoted 57–60% answers RED's dated one-of-four state, not an automatically refreshed probability. VIOLET adopts the prohibition on substituting unconditional 0.8%; it does not carry the old conditional estimate as current or independently reproduced.

## Ownership and completion

VIOLET's chain response is **CONCUR WITH THE ABOVE REPAIR; NO ASSENT TO THE ORIGINAL REGENERATION TEST**. RED owns the letter, operator and grading; PROME owns the coordination docket. Requested next action: RED adopts or records a reasoned superseding disposition; PROME records its chain response and reconciles L376. Neither a VIOLET packet nor an inbox move certifies that adoption occurred. No count, grade, weight or capital action is made here.
