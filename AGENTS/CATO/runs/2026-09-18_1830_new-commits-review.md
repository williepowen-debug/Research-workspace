# New commits and PROME follow-through — September 18

## Scope and limits

Will asked CATO to read/analyze the new commits after relaying PROME’s responses. Main snapshot: `a2522254c`, range `d86e72206..a2522254c`: nine commits / 31 paths, including CATO’s own prior feedback commit (not independently reviewed). Eight other commits concern HAWK’s new Europe theme/closeout and PROME’s shared-price warning/BRENT packet. Also inspected SAM’s earlier `512ac5a1c` roll checker and current BOND/WQ-157 evidence because those were explicit subjects of the response.

Read-only review of owners; no repairs, messages, launches, grades or trade changes. Risk-selected review, not certification of all HAWK research or PROME closeout. External checks sampled the cited incursion source, Council SAFE overview and NATO/Estonian Article 4 primaries. No fresh market-data pull or certification of the quoted historical prices. Historical probe loads pinned Git bytes, mocks data, and writes only CATO evidence. Exit zero reproduces defects; it is NOT repair acceptance.

## Findings

### N1 — HIGH: the corrected BRENT packet still predicts a roll-only verdict without the basis

Owner PROME; consumer BRENT. `AGENTS/BRENT/inbox/2026-09-18_from-PROME_CL-F-mislabels-its-contract-your-MKT-CL-F-ABOVE-100-line-reads-off-it.md:21`, revision `f02a7dded`. Its table already identifies CL=F with November on September 18, but the forward-risk paragraph says it becomes November after September 22 and that a sub-$100 print next week would be a roll, not an un-fire. The first claim contradicts its own measured state; the second is not established by any future matched-contract observation or the still-unresolved close/intraday rule. Line 18’s blanket attribution of any “crude cracked today” narrative to roll also exceeds its own reported genuine October decline.

The future-switch wording also appears in `FORGE/tools/market-data/README.md:40` and `AGENTS/HAWK/NEXUS_BRIEF.md` WATCH. PROME’s earlier distance-versus-move correction is real and useful, but does not close this remaining inference. Exact expiration has not been independently certified in this review; the defect does not depend on that date being exact.

Acceptance: say the continuous quote already tracked November in the observed pull; separate exchange expiry from vendor roll; leave subsequent trigger/exit status to BRENT’s registered contract and observation basis. Do not erase the genuine matched-contract decline. Reconcile the warning consumers, not only the plan. This is a high-priority misleading instruction to a live gate owner, not evidence that an incorrect grade or trade actually happened.

### N2 — MEDIUM: SAM’s roll check certifies incomplete requested windows

Owner SAM. `scripts/oil_roll_check.py:66–80,125–129`, pinned `a2522254c` (same script as `512ac5a1c`). Only returned continuous observations are iterated; absent sessions never enter the unresolved set. Requested September 15–18, mocked series ending September 16: rc 0, NO ROLL, basis-clean. A single September 15 observation also returns rc 0 and 0.00%. An interior missing weekday is likewise accepted. Printed endpoints expose the shorter span, but the success state does not withhold the requested-window certification.

Controls: complete four-day no-roll rc 0; complete four-day roll rc 2. This is a missing-coverage counterexample, not a claim that today’s live data was missing or a roll was actually missed. Standalone default supports both BZ=F and CL=F; boot.py invokes BZ=F only. That boot scope is not by itself a defect in the original Brent repair. Boot’s successful-roll advisory behavior is deliberate and separate from this incomplete-data problem.

Acceptance: define required observable sessions/endpoints using the relevant market calendar and publication/as-of policy; reject or declare incomplete coverage without falsely requiring weekend/holiday prints; require enough observations for a change. Test missing beginning/end/interior, one-point data, legitimate nontrading dates and healthy roll/no-roll. Never silently shrink the requested comparison.

### N3 — MEDIUM: HAWK’s narrative counts a declined engagement as a kill

Owner HAWK. `domain/europe-rearm/LADDER.md:33` says four Romanian July shoot-downs; `research/2026-09-18_european-rearmament-evidence-sweep.md` §1b repeats four on July 24–27. Its own INCURSIONS rows EUR-2026-005/006/007 show three kills; EUR-2026-008 explicitly says NONE / crossed unengaged. The [cited running record](https://www.grosswald.org/russian-drone-and-missile-incursions-nato-territory/) also distinguishes three kills from the fourth unengaged target. This is a source-to-summary mismatch, not an independent primary verification of every incident.

Acceptance: reconcile to three shoot-downs and one unengaged target unless contrary event evidence is supplied; preserve the latter as a restraint observation. The separate four Baltic engagements are not disputed by this finding.

### N4 — MEDIUM: HAWK’s new falsifier promises more identification than it supplies

Owner HAWK. `thesis/FALSIFICATION.md` §EURMIL E3 says re-attributing two objects as deliberate Russian probes would make the engagement count a clean intent measure. It would remove those provenance objections, but cannot remove the separately documented change in NATO engagement rules, nor the lack of an exposure/detection denominator. The new LADDER itself explicitly recognizes that confound. Re-attribution could strengthen the threat interpretation without making the count clean.

Related analytical limit: research §9 treats telegraphed orders as therefore largely discounted, supported there by one current price snapshot rather than an expectations/valuation test. Keep that as a hypothesis; the evidence shown establishes neither how much is priced nor that a future ladder step would surprise markets. No need to commission a new study merely to narrow the wording.

Acceptance: E3 retracts only the provenance caveat it actually tests; other confounders remain. Separate evidence of preparation, inference about intent, and inference about market pricing.

## Follow-through verified at the snapshot

- **PROME’s distance correction:** implemented in `f02a7dded`, with explicit correction history, distinct distance/move, timestamps and close/intraday caveat. N1 remains.
- **WQ-263:** the promised recognizer-boundary rewrite is not present. The row still preserves literal -m command-position blocking and downgrades -F/heredoc inference; all three R4 wrapped-prose cases still return BLOCK. Plain echo ALLOW and actual over-cap Git BLOCK controls pass. Existing policy remains until Will rules; no policy change by CATO.
- **BOND A2:** analysis §7, line 141 still calls the 68% subgroup the standalone signal. **PROME’s current WQ-157 row correctly labels n=22 as I-prime with dealer leg FALSE**, alongside n=30 paired at 27%. No 68% occurrence found in current BRIEF, STATUS or HEARTBEAT. Thus the reviewed coordinator prose is correct on this specific population; the owner evidence remains defective. Exact aggregate 23/52 still requires underlying-row verification; it was not recomputed here.
- **Owner delivery:** no new September 18 PROME CATO-review packets found in BOND, DAEDALUS, WALTER or SAM inbox trees. LIQUID has the already-known September 17 review packet delivered by PROME on September 18. DAEDALUS’s BROCK packet merely references CATO and is not delivery of A5–A7. This is a bounded filesystem observation, not proof that no live communication occurred. PROME’s promised sends remain in progress, not a breached completion claim.
- **Registrations:** no new BND-26 cutoff row, separate BRENT trigger-basis row, or new L386 annotation from the quoted plan was present. Historical BND-26 mentions are not the missing publication-cutoff obligation. PROME’s active plan/review is not certified as applied.
- **HAWK progress:** owner packets exist; scope disagreements remain explicitly proposed; 19 incursion ledger records distinguish violation/kill/provenance; inventory vintage and Article 4 primary gap are disclosed. Aggregate fingerprint checker PASS at review, which proves declared bytes only. Some added sources (BRENT listing, WALTER STS report) are not in its static dependency list: do not interpret PASS as certifying every new input.

## Additional bounded observations

HAWK’s live Europe README still says no VX row exists and a HANS packet is needed, despite both being committed. Its dated opening sweep may legitimately preserve pre-registration history; the live folder contract needs the current disposition. Low priority.

Article 4 chronology: [Estonia’s government](https://www.valitsus.ee/en/news/estonian-government-request-nato-article-4-consultations) requested consultations on September 19, 2025; [NATO’s statement](https://www.nato.int/en/about-us/official-texts-and-resources/official-texts/2025/09/23/statement-by-the-north-atlantic-council-on-recent-airspace-violations-by-russia) records the Council meeting September 23. HAWK’s September 23 reference is defensible as meeting date, but request versus meeting must be explicit when defining a request-triggered rung. These sources do not establish the absence of a 2026 invocation. The later NATO eastern-flank page is not an exhaustive consultation register. No upgrade of that negative finding.

## Checks and next action

Evidence: [probe](2026-09-18_1830_new-commits-probe.py), [output](2026-09-18_1830_new-commits-probe.txt). Five offline roll cases and five hook cases reproduce; HAWK derived_freshness PASS. No whole-suite or full-source audit claimed. CATO authored evidence/continuity only; tests are CATO’s review probes, not independent verification of CATO itself.

Recommended order: preserve BOND’s decision-facing limitation for tomorrow; correct N1 before interpreting the BRENT line; get N2 disposition before treating the new roll guard as window certification; fold HAWK’s count and inference corrections into its existing theme work. Delivery and launching remain separate, and no sends are assigned by this report. Next session: orient and await Will; recheck active PROME changes before evaluating completion.

Final pre-commit check: HEAD remained a2522254c; owner working tree and shared index were clean. CATO whitespace check, root orphan advisory and weekday checks on the three PROME queues passed. CONTINUITY measured 24063 bytes (below 32,550). No source repairs or superseded canonical figures, so no consumer sweep triggered. Commit/push receipt delivered in-session.
