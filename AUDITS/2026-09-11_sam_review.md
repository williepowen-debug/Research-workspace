# SAM review — September 11, 2026

## Assessment and scope

SAM's analytical restraint is stronger than its closeout reliability. It declined a defective futures feed, recognized limits in its auction grading, and used its internal reviewers to find real mistakes. However, the handoff did not catch up with those corrections, and several repaired tools still accepted evidence that did not establish their claimed condition.

Reviewed September 11 SAM commits from the prior-day baseline `b552b60a` through `644fc8388`, with the shared checkout inspected through `b9071b818`. This includes the CFTC drift instrument, auction rulings, futures activation decision, memory/proposal rollers, state/brief changes and internal review receipts. This is a focused review, not an independent reproduction of every source pull or a full forecast audit. Repairs are isolated on `review/codex-20260911`, following the PROME/CARL review. No active SAM files in the shared checkout were changed.

## Findings and corrections

### P1 — The cross-agent brief contradicts SAM's completed work

`NEXUS_BRIEF.md` still referenced early-morning STATUS commit `eb31d5946`. Later same-day work corrected RED's supposedly unread report, declined futures-feed activation, completed the auction ruling and reviewed a second Totan chart. The brief still said RED was unread, activation and the ruling were owed, and presented the first chart's forward-path softening without the partial reversal. These are observed content contradictions, not just an old timestamp.

Corrected the local brief against STATUS `644fc8388` and the decision artifacts. Quote values remain explicitly SAM's recorded September 11 snapshot, not fresh market data. Genuine basis research remains open even though the defective proxy's activation was declined. The correction also removes categorical language suggesting that an anticipated hike leaves no possible hawkish surprise.

### P1 — Memory protection applies too broadly in the wrong direction

Today's `subagent_memory_roll.py` repair correctly recognized a run-named child under PENDING as pending work. But it treated children of **every** NEVER_ROLL parent as eligible for heading-based closure. A fixture `## CALIBRATION / ### CLOSED examples` was selected for archiving, despite the explicit rule that calibration never rolls. A heading saying `NOT CLOSED` also passed the substring test.

Corrected protected-section containment: only PENDING's individually closed children can move; calibration, standing monitors, hints and change summaries remain protected. Pending closure requires an affirmative declaration rather than a negated or missing-marker heading. Existing live pending/run-name behavior is covered. These were reproduced edge cases; I did not find or allege an actual lost calibration section.

The prior “byte conservation” claim was also too strong: it checked approximate character counts after writing, with added pointer text able to mask losses. The repair verifies the exact section partition before writes. Archival behavior was exercised on temporary files, including Unicode content and protected rules.

### P1 — Proposal landing proof can accept a different proposal

Today's KURA fix compared only the first 40 normalized topic characters. Two topics with a common prefix but different endings were certified as the same landing. Empty topics and repeated IDs with conflicting topics could also evade the intended check. The run parser additionally consumed the remainder of the document, including trailing operating instructions; the actual KURA file has a trailing “The rule” section within that capture range. It is currently protected by the newest-run window, not by a structural boundary.

Corrected full normalized-topic comparison, rejection of empty/conflicting topic evidence, and run boundaries at the next peer or parent heading. Proposal archive writes now retain the exact body rather than stripping trailing whitespace. Source spans are checked before writes. ID-plus-topic identity remains a limited check: it does not prove that every prose correction or recommendation accompanying the proposed rows was applied. Mixed proposal/correction blocks still require SAM's disposition review before an actual roll.

### P2 — The CFTC rule did not enforce consecutive observations

`cftc_jpy.py` took the last two usable physical rows, silently skipped malformed changes, and never checked dates. A fixture containing August 11 and August 25 printed a “two consecutive B0” drift flag. Reverse-order and duplicate data could also select the wrong evidence.

Corrected chronological ordering, duplicate/malformed-data rejection, weekly adjacency and the B0 run-length count. Unevaluable inputs propagate a nonzero result through the script's main path. Frozen deadband, drift threshold and strict comparison are unchanged. The actual reviewed ledger still produces NOT APPLICABLE: its September 1 move is outside the deadband.

The seven-day check is deliberately conservative. CFTC data normally describe Tuesday positions, but official holiday exceptions exist; an unusual interval now asks for verification rather than inventing continuity. Sources: [CFTC report description](https://www.cftc.gov/MarketReports/CommitmentsofTraders/AbouttheCOTReports/cot_about.html) and [historical holiday exceptions](https://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalSpecialAnnouncements/index.htm).

### P2 — Preserving a forecast record is not the same as endorsing its score

The auction amendment acknowledges that SAM-35's AND condition lost its tail conjunct, then says the prediction was graded “on its letter.” Both cannot hold. Corrected that explanation locally: retain the historical record, disclose the application error, and require a separate scoring disposition before counting it as an unqualified confirmation. No prediction terms or result rows were changed.

Withdrawing the live demand-floor inference was the right action. MOF's documentation supports treating uniform-price 40-year auctions differently: [official issuance-method discussion](https://www.mof.go.jp/english/policy/jgbs/publication/debt_management_report/2024/esaimu2024.pdf). Two observed bid-cover ratios cannot establish a population probability of one, and the new ruling's “can only ever print SOFT” wording goes beyond those observations. Its conservative non-applicability decision does not require that overclaim.

## What SAM did well, and what remains

The futures-feed refusal is well supported by SAM's source-quality evidence: rounding, timestamp mismatch and an unstable policy assumption. Its arithmetic sensitivity is useful; it does not establish that a hike would mechanically move the observed residual by 25bp if the input stayed fixed. Making spot policy an input also does not turn a futures/bill residual into matched-tenor cross-currency basis. Keep the genuine basis research obligation separate from fixing that proxy.

The internal reviewers produced concrete corrections, particularly the dormant pending-block problem and the withdrawn 40-year inference. But this has not solved the context-cost problem. Current memory sizes are METSUKE **378,026 bytes**, KURA **209,222**, and KOYOMI **123,324**. “Nothing terminal to roll” is not evidence of a bounded spawn read. SAM needs deliberate dispositions and a compact active-work index; automatically archiving ambiguous live work would make matters worse.

The VECTOR-5 arithmetic is useful as an exposure sanity check. Failure to erase Japan's whole current-account surplus is not, by itself, proof that an oil shock cannot affect the yen or produce a tradable move. NONE remains a defensible decision under SAM's registered framework, but the macro conclusion should not be presented as a mathematical impossibility.

## Validation and delivery

- 14 new offline regression tests pass, including both rollers' apply paths on disposable fixtures.
- Existing CFTC frozen self-test: 8/8 pass.
- Both rollers ran report-only against the reviewed SAM files; no live memory/spec archival was applied.
- CFTC drift ran read-only against the reviewed ledger; frozen thresholds remain unchanged.
- Whitespace/diff validation passed. No market fetches, messages, trade actions or shared-checkout edits were performed.

The patch includes the three tools, regression tests, reconciled NEXUS brief, corrected auction-scoring explanation and this report. It is local review work, not pushed or merged.
