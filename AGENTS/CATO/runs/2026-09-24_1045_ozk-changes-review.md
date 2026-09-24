# OZK changes review — September 24, 2026

**Disposition: retain the rebuild; make bounded corrections to consequential claims, then resume source work.** OZK made real changes to its working documents and executable filing watch. The desk is easier to resume, but document maintenance has not discharged its overdue research. Four findings below distinguish three substantive corrections from a smaller pre-print resolver clarification. CATO changed no OZK files and sent no instructions or packets.

## Assignment and evidence perimeter

Will asked to review OZK because it had been making many changes. Initial snapshot `37ed0a355a6b72e7404fa04e86ea2624c00c7a83`; clean startup, pull already up to date. Reviewed the September 24 catch-up/watch repairs and six working-file rebuilds (`6e28dff38`, `4f6852513`, `ef900ced0`, `59a84451d`, `cea53bbff`, `423ef7047`), including the old/current TODO and prediction-ledger diff. Concurrent owner commit `e9593591146942a4226dc6bc30fd52f50793a6ca` changed THESIS/CHANGELOG; its additions and relevant surrounding material were also inspected. That is the final evidence pin, not a claim the live desk stopped working.

Read STATUS, MEMORY, INDEX, CALENDAR, TODO, LESSONS, owner instructions and the relevant adjudication, Call Report log, prediction rows, scripts and correction packets. This was a bounded preservation and correctness review, not a census proving every deleted sentence was safely retired or a new audit of all 230 KB rows. Earlier locally inspected Q2/Q3 2025 primary PDFs remain evidence for the named-book balance decline; this session did not re-download them or independently re-pull the full Call Report series. No live boot, broker verification, market-price refresh, court/recorder search or hosted publication.

## What improved and what remains research

- The four detected whole-read startup files are now comfortably below the read budget: STATUS 14,032 B; MEMORY 13,402 B; LESSONS 11,753 B; CALENDAR 7,099 B. `read_cap_check --agent OZK` passes with zero rotation advisories. This is its four-file charter heuristic, not complete boot-read certification.
- TODO separates dated work, overdue checks, research, gated decisions and standing duties. The sampled important obligations survive: full Q2 10-Q read, Horton leasing, recorder check, severity comps, reserve-estimate re-derivation, subdomain refresh, broker confirmation, Q3 preparation and P-OZK-1/4/5. The closed salvage-trade prohibition survives. The retired WAL question has a prior correction/disposition in KB-OZK-229, rather than disappearing without any trace.
- Prediction-cell comparison from `24860a684^` to the final pin shows only OZK-02/03/04 Timeframe and OZK-09 Invalidation changed. Prediction text, confidence, status and outcome cells are unchanged. The thesis refresh now carries the previously approved A30/B45/C8/D17 weights and separates expected loss from the $140M prediction threshold. That is repair of stale mirrors, not a new model calibration.
- **RB2 owner correction verified:** adjudication §6/§6.5, STATUS, INDEX and refreshed THESIS distinguish observed reported-book decline, favored repayment inference and reclassification not excluded. REGINALD and BROCK correction packets exist; REGINALD's is processed, BROCK's remains inbox. This establishes owner correction and durable delivery, not all downstream consumption. The original wider propagation condition is not globally certified.
- **RB3 principal failures repaired:** owner selftest passes 10/10. Nine independent pinned checks pass: ordinary baseline/new filing, empty list/object, missing/boolean IDs, short response, older window and network timeout. The observed prior malformed-response failures now return UNKNOWN. CALENDAR/STATUS/boot instructions correctly describe a quiet result as scheduled-uncontradicted, not confirmed repricing. Coverage remains a heuristic; the duplicate-row advisory below is disclosed.
- Still unfinished, accurately carried by the owner: Q2 10-Q full read (keyword pass only), Horton leasing since late July, severity comparisons since July 31, and re-deriving the $150–300M reserve estimate after one supporting input was withdrawn. Reorganizing those tasks does not complete them.

## OZ1 — Medium: redemption is presented as removing a capital penalty without its capital cost

**Sources:** `THESIS.md`, invalidation §4 (new `e95935911` wording), says redemption removes the interest headwind **and the Tier 2 −20% haircut**. `CALENDAR.md:15` says a redemption/refinancing makes the interest and Tier-2 legs void.

**Verified externally:** [OZK Q2 2026 Management Comments, printed p.33](https://ir.ozk.com/2Q26_Management_Comments) describes $350M notes, the October 1 term-SOFR-plus-209bp reset, 20% reduction in Tier 2 recognition and quarterly redemption option. [12 CFR 324.20(d)(1)(iv)–(v)](https://www.ecfr.gov/current/title-12/chapter-III/subchapter-B/part-324/subpart-C/section-324.20) measures eligible capital net of redemptions and distinguishes replacement from demonstrating adequate remaining capital. Both sources opened September 24.

**Consequence / inference from those sources:** an outright redemption without replacement eliminates the redeemed notes' remaining capital contribution. On a simplified principal-only comparison, retaining the notes after a first 20% reduction leaves about $280M eligible; redeeming all of them leaves zero from those notes. Replacing them introduces a new instrument with its own eligibility and coupon. Avoiding the old haircut is not, by itself, a capital improvement. No bank-wide capital-ratio change is calculated here.

**Correction / close when:** distinguish retain/reset, redeem without replacement and refinance. Treat a new filing as a reason to recalculate interest and capital effects, not to cancel both as adverse factors automatically. Repair THESIS §4 and CALENDAR's October 2 branch; check the corresponding current desk/coordinator consumer if it copied that branch. Preserve the existing watch, event date and model probabilities. Management-confidence interpretation may remain an explicitly labeled inference.

## OZ2 — Medium: the rebuilt thesis converts a balance comparison into a proven loan flow

**Sources:** refreshed `THESIS.md`, wave 2 and migration table, says the past-due decline was entirely the 30–89 bucket emptying **into** NPA, rather than cures. Its governing support, `CALL_REPORT_2026Q2_LOG.md:176–191`, expressly calls the roll-forward implied, not disclosed, but then treats the migration conclusion as settled. The categorical claim predates the rebuild and is repeated in its new summary.

**Verified arithmetic, not fresh primary extraction:** the stored series has 30–89 accruing balances $190.947M → $23.273M, nonaccrual $296.575M → $300.416M, and OREO $149.570M → $288.135M. Those endpoints show the delinquent bucket fell and nonperforming assets rose. They do not identify the departing loans.

**Independent counterexample ($K; hypothetical):** let 167,674 of the initial 30–89 bucket cure/pay off, leaving 23,273. Let other, formerly current loans supply 198,660 into nonaccrual; transfer 138,565 from nonaccrual into OREO and apply the owner's simplified 56,254 net charge-off decrement. Then nonaccrual is `296,575 + 198,660 − 138,565 − 56,254 = 300,416`, and OREO is `149,570 + 138,565 = 288,135`. Every cited endpoint matches with **zero** transfer from the initial delinquent bucket into nonaccrual. This uses the log's simplifying flow assumptions; it is not an assertion about actual loan movements or a reconciliation of every filing line.

**Consequence:** an inference is being used as proof that a literally fired thesis invalidation was harmless. Rising aggregate stress remains relevant evidence, and this counterexample does not disprove the bear thesis. It does prevent claiming the endpoints prove all departing delinquent loans worsened.

**Correction / close when:** retain the observed balances and literal trigger, label migration as an inference unless credit-level/actual roll-forward evidence identifies it, and carry the limitation into THESIS, STATUS and the supporting log's adjudication. Keep P-OZK-4 Will-gated; CATO is not selecting a replacement kill condition or requiring a new confidence mark. Any consequential disposition change must follow the existing owner/Will decision process.

## OZ3 — Medium: an explicitly unverified catalyst is still presented as an established event

**Sources:** `TODO.md:29` retains the April 22 task to verify or remove the alleged Affinius $2.7B October bond maturity, specifically warning of possible Affinius/USAA Capital conflation. Nevertheless `CALENDAR.md:19`, `STATUS.md:101` and `scripts/boot.py:41` continue to present that maturity as a dated catalyst. Their caveat concerns OZK's exposure, not whether the named issuer/maturity is real.

**Consequence:** the rebuilt calendar can direct research and interpret news around a potentially wrong issuer/event, even though its own source-verification task is outstanding. This review establishes inconsistent evidence status, **not that the bond is fictitious**. No independent bond/CUSIP investigation was assigned or performed.

**Correction / close when:** verify issuer, instrument, amount and maturity from a primary source, or mark the event itself unverified/suspend it from actionable catalyst treatment while keeping C5 open. Carry that event-level qualifier to CALENDAR, STATUS and the boot countdown. This does not require launching CREED or broadening the counterparty research.

## OZ4 — Low, pre-print: finish the prediction resolver clarification

**Sources:** `workbook/PREDICTIONS.tsv`, OZK-03 and OZK-09; `STATUS.md:66`; `CALENDAR.md:33`.

OZK-03's Timeframe was moved to the Q4 earnings event, but its Invalidation cell still says the February 27, 2027 print. The changed date therefore has not reached both sides of the same row. The unresolved RESG-versus-bank-wide scope remains correctly gated as P-OZK-5; a date correction does not fix that separate issue.

OZK-09 now requires three completed, dated searches before negative resolution and blocks on UNKNOWN. That is a useful necessary condition, but completion is not enough when filings carry losses only in aggregate. A concrete case is: every instrument was inspected successfully; no named RaDD disclosure was found; aggregate losses cannot be allocated. All searches can be VERIFIED/SEARCH-NOT-FOUND while the loss amount remains unresolved. STATUS already correctly requires STUCK for missing attribution. The ledger should make that substantive guard explicit, so the new instrument is not read as authorizing FALSE whenever all three searches completed. This is an instruction ambiguity; no actual misgrade occurred.

**Close when:** align OZK-03's two date references, and explicitly require sufficient attribution (or a valid bound) before grading OZK-09, preserving STUCK when searches succeed but the amount cannot be established. Preserve the approved event window, threshold and confidence. A synthetic no-attribution example is sufficient to demonstrate the clarification; no extra research platform is needed.

## Lower-impact residue and review limits

- The watch counts raw rows for its coverage floor. A synthetic response containing 182 copies of baseline 11981 returns QUIET/coverage OK despite only one unique filing. Reproduced, but no such live API failure observed. The original empty/malformed examples are fixed; duplicate-ID rejection/unique-ID coverage is a small deferred robustness improvement, not a reason to rebuild the service. Even that would not independently prove source completeness.
- STATUS/INDEX/adjudication describe $1.20B at June 2025 to $0.43B at June 2026 as 18 months; the shown endpoints span 12 months. MEMORY still refers to old S-item identifiers after TODO renumbering. Correct at the next ordinary owner touch; these are not reasons for another whole-file rewrite.
- The new THESIS still contains inherited tension between “distinguishes loss-driven contraction” and its later correct caveat that charge-offs do not explain the earlier shrink. Include that sentence in the next inference cleanup. No automatic expansion into all historical research is assigned.
- The preserved transcript, subdomain, reserve-estimate and attribution limitations mean this review does not certify the entire OZK thesis or approve a position. CATO did not author the owner repairs; its tests are independent checks of those implementations. The reproduction file itself is CATO-authored evidence, not an independently reviewed production control.

## Checks and suggested next step

`python3 -B AGENTS/OZK/scripts/flng_watch.py --selftest`: 10/10 pass. `python3 -B AGENTS/CATO/runs/2026-09-24_1045_ozk-review-repro.py`: nine watcher checks, prediction-cell diff and flow counterexample pass; output in the adjacent `2026-09-24_1045_ozk-review-evidence.json`. `read_cap_check.py --agent OZK`: pass within the stated perimeter. Closeout: exact-path whitespace check and weekday claim check (DOCKET, GATES, WILL_QUEUE, this report) pass; orphan advisory clean, no foreign staged paths. Commit/fresh-fetch push receipt delivered in-session.

Suggested instruction for Will to give PROME: “Keep OZK's rebuilt files. Have OZK correct the redemption/capital interpretation, qualify the unsupported delinquency-to-NPA flow claim, quarantine or verify the Affinius maturity, and finish the prediction date/attribution guards. Keep existing grades, weights and Will-gated proposals unchanged unless a separate decision is needed. Show the exact changes and the counterexamples they handle. Then prioritize the already-open full Q2 10-Q read and Horton leasing check ahead of further document restructuring.”

This wording has **not** been sent. CATO's assignment ends with this review; no owner fixes, new research, sends or launches are authorized by closeout. Next session: orient and await Will.
