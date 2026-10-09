# PROME / NEXUS September 29 afternoon — first correction pass

## Current assessment

**October 8 correction follow-up, NEXUS `6e6321fdc` / PROME `0932c324a`: PN7 and PN8 CLOSED in the checked scope.** The cross-date counter-evidence is withdrawn; the owed cold-read ledger exists and its seven error fixes are present. Attribution-first is staged for the scheduled October 9 grade, with PROME L553 carrying the corrected instruction; ~55% is explicitly the forecast of record. PRED-50's log, tally and grade date are unchanged; the prior calculation remains accepted. STATUS is 22,708B, just 77B below its owner rotation target: useful working room remains undelivered and is explicitly deferred to Friday before the anchor additions. Stop tonight's correction cycle; next observation is the grade and already authorized research result. No owner edits, sends or launches. Earlier PN1/PN2/PN5 checked-instance closures and PN3/PN4/PN6 closed dispositions stand; no general source or board certification. Await Will.

The useful result survives: the same HY observation should not become several independent votes because several desks consume it. The evidence does **not** yet establish the stronger conclusion that this cluster has exactly two causes, with AI disruption established as the second. Preserve that distinction in the decision summaries.

## Scope and evidence limits

Will requested: “PROME and NEXUS had an extensive session … read through the commits … First pass lets just look for errors or corrections.” Reviewed the afternoon sequence `e612e1644^..9c60f7c8c`, concentrating on PROME's WQ-339/340/341/342 registration and consumption, NEXUS's `83e6fe366` synthesis and `319b391e2` / `0e9ebf96d` / `9c60f7c8c` follow-ups, the FORGE reconciliation and mapping update, and the L462 code change `d024593f0`. Morning commits were navigational context, not a fresh morning-session audit.

Starting branch master, HEAD `9c60f7c8c`; staging initially empty. REGINALD and PROME had dirty files; later REGINALD had staged inbox moves and PROME was preparing closeout. No pull, reset, stash, owner edit or message. Findings below refer to the committed snapshot; unfinished PROME closeout/HEARTBEAT edits are excluded. BOND/LIQUID owner artifacts were read to test specific consumer claims. No fleet agents launched.

This is an independent review of these implementations, not independent verification of every market observation. No new external market pull, account access or original screenshot inspection was performed. Broker-table arithmetic can be checked; transcription fidelity cannot. No fresh trade recommendation or certification of holdings beyond the dated records.

## Findings

### PN1 — High: PRED-50 does not define a complete, unambiguous grading rule

**Evidence:** `AGENTS/NEXUS/analysis/2026-09-29_one-root-or-many.md:65`; mirrored at `PREDICTIONS_MONITOR.md` L14. Positive branch: B OAS rises at least 5bp on at least two rates-quiet sessions. Negative branch: “≤ −5bp, or |Δ| < 5 on every rates-quiet session (≥2 of them).” NO-VERDICT is only for fewer than two quiet sessions.

**Counterexamples, with all listed sessions rates-quiet:**

| B OAS daily changes, bp | Result under the written branches |
|---|---|
| +6, 0 | No branch, under either plausible reading of the negative clause |
| +6, −6 | Negative if one −5-or-lower cell suffices; no branch if the quantifier covers every cell |
| +6, +6, −6 | Both positive and negative if one negative cell suffices |
| −6 only | Negative and NO-VERDICT if the negative cell has no two-session minimum |

Thus even the charitable all-sessions reading leaves ungraded mixed outcomes. This is consequential because WQ-341 waits on this grade before assigning or rejecting a research cause.

**Correction / closure:** NEXUS should preserve the original frozen letter, explicitly register the defect and a dated correction, and specify mutually exclusive, exhaustive branches, minimum sample size and mixed-outcome handling. State how correction timing affects the observation window rather than silently replacing the original. Close when the examples above, exact ±5 boundaries, missing observations and zero/one quiet-session cases each receive exactly one intended result. Propagate to L14/PRED-50 and PROME L553/WQ-341. CATO has not supplied or authorized replacement thresholds.

### PN2 — High: the tests do not identify the cause the summaries claim

**Evidence:** analysis lines 13–17, 56, 58 and 64–65; STATUS lines 8, 41, 50, 103 and 147; WQ-340 delivery and WQ-341 in `PROME/WILL_QUEUE.md`.

Three separable problems support one correction:

- PRED-50 tests contemporaneous **nominal** DGS10 changes, while its claim concerns independence from the **real-yield** cause. A hypothetical +10bp real-yield move offset by −10bp inflation compensation gives a quiet nominal yield without a quiet real-yield cause. Even with truly quiet real yields, delayed credit response to earlier rates changes can satisfy this rule without an independent cause. Conversely, no qualifying credit move in eight cells does not establish that every prior move had the same cause.
- The IG >94 line measures a spread level. Its firing does not by itself establish “index-wide discount-rate repricing” or impaired “market function”; failure to fire does not show that rates have not transmitted into lower-quality credit. LIQ-07 similarly measures B/CCC spread behavior, not AI attribution. No sector contribution evidence in the supplied page closes those logical gaps.
- The page itself labels HY attribution UNDETERMINED and the bank mechanisms unadjudicated; its caveat says cable attribution is partly from memory and rests on one quiet-rates day. Nevertheless its headline and PROME's delivery receipt say TWO ROOTS / effective-N ≈2. STATUS line 50 simultaneously says the second face is **not a second root until PRED-50 says so**. That is an internal contradiction, not merely a difference in tone.

**Correction / closure:** describe an established rates-related cluster plus a **candidate** additional credit cause; keep Rhine separately scoped as the control. Narrow the test's verdict to the behavior actually measured, and leave causal attribution unresolved without additional discriminating evidence. Do not turn failure of this test into proof that AI disruption is a non-root or a reason to close a distinct coverage question. Preserve the mechanism caveat in STATUS and WQ-340/341 summaries, not only in the analysis footnotes. Close when all named consumers carry the same conditional claim and no test result automatically installs a causal root that the observations cannot identify. This does not authorize a new study or alter the frozen split.

### PN3 — High: WQ-339 falsely says the expiring September puts are the book's only rates expression

**Evidence:** `PROME/WILL_QUEUE.md:27`, introduced `24f04fdd2`, calls TLT Sep-30 77P ×15 “the book's only rates expression.” Its cited BOND analysis, `AGENTS/BOND/analysis/2026-09-29_WQ-317_PARTIAL_same-day-attribution_book-lines.md` §3, explicitly includes **TLT Oct-16 82P ×1 and TBT ×10**. Both are also in the September 29 broker transcription and FORGE mirror. They were already present in BOND's cited report, so this is not caused by a later purchase.

**Consequence:** “fresh card or stand down on duration” can be read as replacement of exposure about to disappear, although two other expressions survive September 30. This matters to any subsequent sizing or portfolio framing.

**Correction / closure:** rewrite WQ-339 around the expiring **September leg**, name the surviving October put and TBT shares, and distinguish declining additional exposure from exiting existing exposure. Have any eventual TERRY card consume the dated complete book. Close on the corrected decision row and associated sitting/summary language. No trade or size is recommended by this finding.

### PN4 — Medium: WQ-339 and its October 2 execution row disagree on which tests govern the recommendation

**Evidence:** WQ-339's recommendation asks for the FR2004 dealer result and the “term-premium/Tokyo falsifiers,” then says “if both hold” commission a card; “if either fails” stand down. `PROME/DOCKET.tsv:552`, added `b95470b8c`, lists BND-30 as input ③ but its actual branch is only **① NOT MET and ② holds**; it expressly allows ③ to be unpublished. BOND's publication ceilings are BND-30 October 9 at 17:00 ET and BND-31 October 2 at noon; an October 2 early boot can precede a terminal missing-data disposition.

**Counterexample:** dealer leg NOT MET, Tokyo BND-31 TRUE, ACM BND-30 FALSE. The docket's recommendation branch commissions, while the WQ wording calls for standing down if a named falsifier fails. UNPUBLISHED/VOID also has no consistent decision disposition across the two surfaces.

**Correction / closure:** PROME must make one explicit recommendation rule and mirror it: is BND-30 binding or contextual; what happens for FALSE, UNPUBLISHED and VOID; and which decisions await publication? Preserve Will's approval gate. Do not infer the intended investment rule from the looser surface. Close when the example and missing-data cases produce the same recommendation in WQ-339 and L552.

### PN5 — Medium: “first-published” provenance is broader than the evidence supplied

**Evidence:** analysis basis line 4 and caveat line 73 call the credit/rates observations first-published; L553 specifies first-published B OAS. But the cited LIQUID STATUS §5 explicitly says latest-revised except its HY watcher. PROME had already consumed `PROME/inbox/processed/2026-09-29_from-LIQUID_CORRECTION-L525-memo-provenance-label-B-CCC-latest-revised.md` in `e612e1644`: equivalence was tested only for aggregate HY, **not B, CCC, BB, BBB or IG**. NEXUS states it made its own FRED pull but supplies no preserved first-vintage evidence for the blanket claim in the reviewed changes.

**Correction / closure:** label inherited figures with their demonstrated vintage; supply a captured first publication or ALFRED evidence if asserting a stronger basis. Define and retain the B-OAS first-publication inputs for PRED-50 if that remains its chosen convention. A same-day retrieval timestamp alone is not evidence that every historical observation in the window is unrevised. No numeric error or re-grade is established here; this is a provenance overclaim. Close when the claim matches the available evidence on the page and its grading consumer.

### PN6 — Low: the late LIQ-076 addendum reintroduces a superseded W2 state

**Evidence:** analysis line 79 and STATUS R7 say W2 UNMEASURED. The analysis's own row 3 says **NOT MET [9/16]**, as do LIQUID STATUS and PROME GATES. The routed write-up preserved the earlier unmeasured account; consuming it later did not make it the newest state.

**Correction / closure:** use “W2 NOT MET on the measured September 16 observation; later vintage not established here” where appropriate, retaining any actual publication gap. Do not revert the established measurement. The conjunction remains MET via W1+W3; no gate re-grade follows. Close on the two current NEXUS surfaces.

## Small corrections and disclosed limitations

- Analysis line 39 labels September 23 Tuesday; it was Wednesday in 2026. Correct the weekday, retain the date. Python calendar check reproduced.
- LAST_COMPLETION's current “NOT done and owed” section still lists the predictions rotation after the same file records it complete. Remove that stale obligation, keeping the dated history.
- The L462 acceptance file says `reads: 1` but enumerates plan and result reads and says the episode closed at two. Align the count with the listed record. This does not itself imply an additional review was required.
- Existing disclosed limitations are not new findings: the live evening detector is unobserved; its post-result fixes and known timestamp/product-calendar residue were already disclosed. Broker D-62/63/64/65 and other residual gaps remain explicit. CATO did not inspect original images or claim those gaps resolved.

## Verification and disposition

- Inspected the new L462 fetch/dashboard code and acceptance record; ran `.venv/bin/python3 -W error::ResourceWarning PROME/tools/tests/test_fetch_evening_bar_L462.py`: **19 passed**. Initial documented system-`python3` invocation failed 13 setup imports because that interpreter lacks yfinance; the project-venv retry passed. No live market probe, production watcher invocation or cache mutation by CATO.
- Independently recomputed the 15 Fidelity transcription rows: positions **$18,720.83**, cash plus positions **$36,822.87**, daily G/L **−$845.38**, total G/L **−$479.55**; all match the table's totals. This verifies arithmetic, not screenshot fidelity or current marks.
- Byte-checked the complete pre-rotation STATUS and PREDICTIONS_MONITOR files from `0e9ebf96d^` inside their cold companions; both present exactly, CRC32 `1bcc0bee` / `632afdf4` match. Live prediction IDs remain represented. This establishes preservation, not every compressed sentence's semantic equivalence.
- Evaluated PN1's examples under both plausible negative-clause interpretations and verified the missing/overlapping outcomes above. These are CATO-devised counterexamples, not owner self-tests.
- Publication scope: local repository report and in-session delivery only. No peer message, inbox packet, external send, website publication or owner correction made. Owner response is pending, not inferred.

Stop condition met for this first pass: concrete corrections, affected consumers, counterexamples and closure conditions recorded. On a requested follow-up, read the owners' disposition and changed text against PN1–PN6; do not restart a fleet-wide audit. Delivery checks and Git receipt follow below/in-session.

Delivery checks: root orphan advisory found only other owners' work outside CATO, preserved; no CATO-authored packet was stranded. Weekday check on DOCKET/GATES/WILL_QUEUE and the two CATO deliverables flagged only this report's deliberate quotation of NEXUS's incorrect weekday, immediately corrected in the next clause; no owner-file weekday flag. CATO diff whitespace check passed. No figure superseded at an owner, STATUS/ledger update, or auto-memory edit, so consumer, ledger-nudge and memory checks were not triggered. Exact-file commit/push receipt is delivered in-session; no commit exists merely to record its own hash.

## September 29 — closeout follow-up, `2fb305ba9` / `2fa0b4327`

Will supplied PROME's closeout receipt. Bounded review of the changed BRIEF, WQ explainers/ledger, generated Decision Deck, publication record, ARGUS note and L462 read counter; BOND's registered publication clauses checked against the new delivery language. HEAD at follow-up `f406f5aa9`; NEXUS and WALTER had untracked work, left untouched. No new full-session audit or repeated fixture suite.

**Disposition: PN1–PN6 remain open at these closeout commits. PN2/PN3/PN4 now have additional consumer instances.**

- **PN3 propagation:** BRIEF §QUESTION now says “after tomorrow's expiry the book has no rates bet.” WQ_EXPLAINERS row 339 says “The only rates bet in the book” while its own decline consequence acknowledges **one October put and ten TBT shares**. WQ_LEDGER row 339 and generated `PROME/artifacts/decision_deck.html` carry the original “only rates expression” premise. Correct those consumers along with WQ-339; this is the same finding, not another portfolio error.
- **PN2 propagation:** BRIEF repeats the definite two-root conclusion and IG causal discriminator, and §FALSIFIER now says failure of credit widening makes Root B “a one-print artefact.” WQ_EXPLAINERS row 341 says the test “decides it by 10/9.” Both overstate what PRED-50 can show; the letter also expressly allows a re-window. The causal and no-verdict caveats must survive rendering.
- **PN4 timing:** PROME's operator receipt says “all inputs Friday”; BRIEF and WQ_EXPLAINERS row 339 promise both tests in hand. BND-30 is publication-anchored with an **October 9 17:00 ET** ceiling; BND-31's missing-row ceiling is **October 2 noon**. Friday's sitting can occur, but it cannot promise those results. Preserve the distinct UNPUBLISHED/VOID handling and clarify which test is binding.
- **Closed small correction:** L462 acceptance now reads `reads: 2`, matching its enumerated plan/result reads. No need to reopen that count.
- **Final base-rate repair:** the changed BRIEF distinguishes BOND's 5.2% frequency for +9bp from the uncomputed +11bp frequency. That addresses the named attribution error on text inspection. It remains a two-session historical frequency, not a calibrated probability for the remaining intraday-to-expiry interval. No recomputation of the series in this follow-up, and no claim of independently verifying PROME's entire final candidate.
- **Delivery evidence:** the two named commits exist; PROME's STATUS/ORCH receipt records the stated publication versions. Hosted artifacts were **not fetched by CATO**; publication is owner-reported. The generated Decision Deck contains PN3. The report's proper closeout distinctions and disclosed unreviewed fix do not certify unrelated analytical claims.

Recommended next action remains an owner correction of the named sources **and their generated/published consumers**. No send or owner edit by CATO. The new untracked NEXUS proposal is not an installed correction and was not reviewed here. This follow-up is complete; await Will.

## September 29 — owner-correction verification, `15af37445` / `5fa4d2949`

Will relayed NEXUS's claimed closure. Read the changed NEXUS analysis, STATUS, prediction ledger, grading log and completion note, plus PROME's `716e6bef2` / `b858142ac` consumer corrections. Starting HEAD `fa2c5f09d`; NEXUS's proposal and WALTER's assessment remained untracked, preserved. No owner edits or sends. No process proposal approval inferred from this review.

**Closed / independently checked:**

- **PN3:** WQ-339, BRIEF and explainer now name the October TLT put and ten TBT shares and frame the choice as additional exposure. The prior unqualified claims are removed from the checked generated Deck/handbook surfaces; historical correction quotations remain appropriately identified.
- **PN4:** the decision-rule block is verbatim identical in WQ-339 and L552. BND-31 must be TRUE; UNPUBLISHED/VOID defers. BND-30 FALSE vetoes if published; UNPUBLISHED/VOID is disclosed and is not a veto. The saved case (dealer NOT MET, Tokyo TRUE, ACM FALSE) now consistently stands down. This verifies consistency of PROME's recommendation, not investment merit or Will's approval.
- **PN6:** both NEXUS current surfaces now say W2 NOT MET on the measured September 16 observation, later vintage not established.
- **PN1 original gap/overlap:** C1's ordered n/W/T rule partitions **all 165 possible count triples for n=0 through 8**, tested independently. The four original examples now grade NOT OBSERVED / NOT OBSERVED / OBSERVED / NO-VERDICT, respectively. Exact ±5, zero/one-session and tied W/T examples also pass. Quiet now requires both real and nominal yields within ±3; an unavailable required cell is excluded by the stated rule. This is verification of the mathematical rule, not of a production grader or future logged observations. The original letter is explicitly retained as superseded, with a dated governing correction.
- Small items: September 23 weekday corrected; completed rotation struck from owed work; C1 stamps now match the correction commit's 16:26 ET timestamp. NEXUS's reported checker flag arising from the adjacent historical year is not grounds for changing the correct Monday September 28 date. No new stamp policy is recommended here.

**Remaining, narrowed to these repairs:**

1. **PN1 — revision handling disagrees.** Analysis C1 vintage bullet says compare both vintages and return INDETERMINATE-BY-VINTAGE only if **verdicts differ**. L14 and PROME L553 instead say a **boundary-crossing revision itself** yields NO-VERDICT. Counterexample: three quiet sessions with B changes **+5.1, +6, +6**, then the first change revised to **+4.9**. W falls from 3 to 2; both vintages remain OBSERVED. The page retains OBSERVED, the summaries force NO-VERDICT. Mirror the page's verdict-disagreement condition (or explicitly revise the governing rule); close when this case receives the same grade everywhere. This is a propagation defect in the new amendment, not a reopening of the repaired original branches.
2. **PN2 — live causal residue remains.** `AGENTS/NEXUS/STATUS.md:113` still concludes **“Two roots, not seven.”** STATUS line 106 and analysis line 58 still call LIQ-07 **“Root B's own discriminator.”** WQ-341 still says PRED-50 **“tests whether the root exists.”** Replace those current claims with the corrected candidate/behavior wording; retained original letters and labelled historical accounts need not be erased.
3. **PN2 — “necessary, not sufficient” is also incorrect.** Analysis C1, L14 and PROME L553/WQ-341 say OBSERVED is necessary for a second cause. An independent credit cause can operate only on rates-active days, or fail to produce two ≥5bp moves in this short window; its existence does not require this test to pass. Use **“neither necessary nor sufficient to establish an independent cause; measures the specified behavior.”** The current “NOT OBSERVED does not establish non-root” sentence is right but conflicts with “necessary.” This is consequential logic, not a stylistic preference.
4. **PN5 — live basis contradiction remains.** The page's basis and new caveat 2a correctly label credit tiers latest-revised. But caveat **4, line 89**, still says **“the 9/28 cells are first-published.”** Qualify or remove that conflicting blanket sentence. Frozen-on-revisable logging is now specified and the three base entries exist; actual future logging/vintage handling remains untested. The claim that no first-window data had published when corrected is owner-reported, not independently reconstructed by CATO.

**Consumer/publication limit:** PROME's revised BRIEF/explainers correct the portfolio premise and timing promises; the C1-specific changes landed later than the recorded v62/v44/v46 publication. CATO inspected repository render/source content, not live hosted versions. Any corrected published copy must carry the final owner wording; no new publication by CATO.

Recommend one bounded consistency pass on these named lines and the revision counterexample, then stop. No re-mark of the split, new study, new control or debrief-list approval is needed from this review. The independent result is **substantial repair, partial closure**, not NEXUS's claimed complete closure of PN1/PN2/PN5/PN6.


## October 8 evening — NEXUS catch-up and PRED-50 review

**Scope and decision.** Will supplied NEXUS's evening closeout and asked for suggestions. Reviewed commit `be40871814d5c01f01f1cb96bc31f40d0cb72eaa` (16 changed paths including four inbox renames), its PM pass record, completion note, STATUS changes, grading log, prediction ledger, charter changes and outgoing packets. Traced the governing C1 analysis, PROME L553 and the October 3 WQ-341 ruling. Starting HEAD `3b6121e7f`, master; PROME had dirty DOCKET/MACHINE_LOCAL/ORCH_LOG and an untracked rotation plan, preserved. NEXUS working tree clean when checked. Morning letters and prior review are supporting context, not a fresh certification of all ten matrix rows. No new raw market pull or external-source validation: arithmetic below is independently recomputed from committed owner observations; auction/storm/news/loan claims remain attributed owner evidence.

**Direction / execution / return.** Finish the dated grade and use the approved research branch to clarify attribution. Do not spend another sitting rediscovering that the behavior test cannot establish a cause. Restore the two damaged qualifications below and complete the existing rotation control; no new tool or fleet audit needed. Stop this review after these concrete recommendations and delivery.

### What holds up

Using exact decimal arithmetic on the log's recorded values, the quiet sessions are September 29 (nominal +2bp, real +1bp, B +7bp ⇒ W), September 30 (+3, +2, 0 ⇒ F), October 5 (+3, +3, +2 ⇒ F), and October 7 (+1, +1, +6 ⇒ W). October 1, 2 and 6 are excluded by the rates rule. Inclusive ±3 boundaries matter. Result: n=4, W=2, T=0, F=2. Enumerating the remaining cell as W, T, F or excluded leaves W≥2 and W>T in every case. This validates the claim about the final cell **on the logged vintage**, not an unconditional final verdict.

A revision can still matter: if October 7 B were revised from 308 to 306 with October 6 unchanged at 302, that day's +6 becomes +4 and W falls to 1. With a flat final observation, the revised verdict differs from the logged OBSERVED verdict; C1 requires INDETERMINATE-BY-VINTAGE. Conversely the prior PN1 counterexample (+5.1/+6/+6 with the first revised to +4.9) still yields OBSERVED in both vintages. C1, L14 and L553 now explicitly agree on **verdict disagreement**, rather than any boundary crossing, as the condition. L553 retains superseded introductory language but its governing C1 amendment is explicit; the pending PM packet calls out the old nominal-only lead.

The active letter and evening synthesis correctly say behavior, not cause. The actual second W follows the rates-active −12bp B move on October 6; a rebound is a live alternative explanation, not merely an imagined caveat. Preserve Disc-A's named-cable check on qualifying dates in the already approved research read, and report whether evidence distinguishes that candidate from a rebound or lagged rates response. This recommends use of the existing mechanism question; it does not amend PRED-50 after observing results or commission a new study.

WQ-341's October 3 ruling explicitly pre-authorizes VULCAN's bounded sub-read with LIQUID owning the credit expression; PROME commissions on the grade **without a second ask**. NEXUS correctly staged rather than prematurely graded it. No new capital authority follows. The frozen split remains 20/47/33. Separately, PRED-50's current confidence was raised from ~55% to ~95%; the original ~55% remains in C1. Preserve the original registration probability for evaluation and label 95% as a post-observation update, not a new successful 95% forecast. No scoring error is established here.

KRE's recorded 69.59 anchor gives 64.0228 / 75.1572 at ±8%, correctly rounded to 64.02 / 75.16. Deferring the Brent anchor when the available bar was an evening-session bar is appropriate. OZK loan maturity remains a relayed Citi-note claim, not a filing independently checked by CATO; retain that qualification in summaries.

### PN7 — Medium: bank/credit counter-evidence mixes observation dates

**Evidence:** `AGENTS/NEXUS/STATUS.md:62` calls it “one day of counter-evidence” to REGINALD's bank-leads-credit interpretation while expressly pairing **October 7** credit widening with **October 8** bank-equity gains. This establishes a sequence of different dated observations, not simultaneous divergence. A bank bounce the day after credit widening can coexist with the prior lead/lag claim.

**Correction / closure:** label the observations separately and withhold the divergence inference until matched-date bank and credit observations are compared. A matched October 7 comparison, then October 8 credit when available, is enough; no new study. Close when the current summary supports its inference with matching dates or removes that inference. This does not change the PRED-50 tally or establish that REGINALD is right.

### PN8 — Medium: claimed complete closeout omits the required post-rotation read

**Evidence:** `AGENTS/NEXUS/CLAUDE.md:71` puts a READ_CAP rule-5 rotation in HEAVY with step 15a; line 106 explicitly includes “a rotation” among rewrites requiring a coldreader before commit. `LAST_COMPLETION.md:18` instead calls 15a inapplicable because the work used exact-string edits and verbatim rotations. STATUS_COLD H15/H15b/H15c/H15d record four rotations/compressions, two explicitly called rule-5 compression. The morning cold-read ledger predates these PM edits. Choosing Edit rather than Write does not supply the charter's missing rotation exception. Therefore the claimed complete PM closeout is not supported under its written rule. This is a control omission, not proof the whole board is wrong.

**Correction / closure:** NEXUS should perform the existing cold read on the final compressed surface and record its disposition, acknowledging that it occurred after the original commit. If the policy should exempt some mechanical moves, that is a prospective instruction decision, not a retrospective waiver. CATO's bounded review is not a substitute for NEXUS's declared instrument and full required coverage.

The committed STATUS is **22,782 bytes**, three below its own 70%-of-32,550 rotation target (22,785), **9,768 below the root hard cap**. Four compression rounds barely reaching the target create immediate repeat work. Recommend the already planned structural rotation remove accumulated historical explanation while preserving active letters, qualifiers, dates and owner obligations, leaving practical room for the next grade. No new size policy proposed; archive checksums/semantic equivalence were not independently certified in this review.

**Disposition and limits.** Findings delivered to Will; owner corrections and cold read remain recommendations, not implementation. Prior approvals survive. No fleet launch, peer packet/message, owner-file edit, market re-grade or hosted publication. The next useful observation is the October 9 grade and the authorized branch's attribution result; this assignment does not create a monitoring job or trigger unrelated CATO work.

**Delivery checks (October 8 follow-up):** all five weekday inputs verified readable: PROME/DOCKET.tsv, PROME/GATES.tsv, PROME/WILL_QUEUE.md, CATO/CONTINUITY.md and this report. The only weekday flag is this report's retained quotation of the original September 23 error, explicitly corrected beside it; no new error. Six actual startup inputs directly measured below 32,550B: CATO AGENTS 6,465; CHARTER 9,921; CONTINUITY 24,909; root CLAUDE 24,961; USER 5,200; AGENTS 5,313. Generic read-cap returns rc2 CANNOT-EVALUATE because CATO has no local CLAUDE.md; not a pass. Diff whitespace clean. Orphan advisory identified only concurrent TERRY/PROME work outside CATO; preserved and disclosed to Will, no authored packet stranded. No own STATUS/declared ledger, auto-memory or fleet-cited figure changed, so ledger/memory/consumer checks do not apply. Exact two-file commit and fresh-fetch push receipt delivered in-session; no hosted publication.


## October 8 19:45 follow-up — owner corrections accepted within scope

Will relayed NEXUS's `6e6321fdc` delivery. Read that seven-file correction, the new cold-read ledger, current final STATUS, corrected prediction row and pass/completion records. Also checked PROME's subsequent `0932c324a` L553 consumption. Starting HEAD `0932c324a`, master, working tree and staging clean; current NEXUS files match `6e6321fdc`. No new market-data pull, comprehensive board review, repeated tally test or owner edit.

- **PN7 CLOSED:** STATUS M-05 and the REGINALD chain row remove the October 8 equity / October 7 credit counter-evidence. They now identify the matching October 7 observations separately from October 8's incomplete pair. The chain verdict explicitly says whether banks lead is **untested**. Remaining attributed “may be running ahead” wording is a hypothesis, not an independently demonstrated lead. CATO checked the date/logic correction, not the raw equity source values.
- **PN8 CLOSED for the omitted-read finding:** a substantive cold-reader ledger now exists, stamped read 19:26:40 / written 19:36:17 ET, with 7 errors, 31 warnings and 47 passes. This repairs the omission after the earlier commit; it does not make that earlier closeout complete retroactively. The reader assessed a 22,452B candidate; the final corrected file is 22,708B. CATO checked all seven named repairs against that final file: cold-pointer range, staged rather than live branch, claims reference week, chain verdict, LIQ-076 moved to NOT CONFIRMING, IG superlative scope, and Persian Gulf versus US Gulf barrel-loss scope. These are independent checks of those corrections, not a second full cold read or independent verification of the reader's runtime/model identity. Remaining warning residue is disclosed; no blanket clean-board claim.
- **Forecast / attribution recommendation implemented and consumed:** PRED-50's Conf cell now explicitly preserves the original ~55% as the graded probability; post-hit status is separate. STATUS split/T-27/R4 say attribution first and keep the branch staged until the grade. PROME `0932c324a` adds the named-mechanism versus rebound/lagged-rates question, the 55% correction, and withdrawal of counter-evidence directly to L553. The packet has moved to processed. No additional approval is required under the existing WQ-341 ruling.
- **Space recommendation remains deferred:** measured STATUS 22,708B = 69.763% of 32,550B; 77B below 22,785B owner target and 9,842B below the root hard cap. Structural rotation occurred, but enough room for the next update was not delivered. Owner explicitly owes another block rotation before Friday's five anchor additions. Keep that ordinary startup duty; do not require another overnight correction cycle or design a new cap/control. Stop once enough space exists for the planned write and the applicable existing review is complete.

Verified the PRED-50 grading log is byte-unchanged between `be4087181` and `6e6321fdc`; no recalculation was needed. Split 20/47/33 and held matrix confidence claims are unchanged in the reviewed diff. The prior arithmetic/source limits survive. This follow-up closes the two bounded findings and records residual space work; it does not certify all 31 warnings, archive preservation or underlying market facts. No owner edits/sends/launches or hosted publication; await Will after delivery.

**Follow-up delivery checks:** orphan advisory clean outside CATO; exact two-file diff whitespace clean, staging empty before commit. Weekday inputs verified readable: PROME DOCKET/GATES/WILL_QUEUE, CATO CONTINUITY and this report; only the retained, explicitly corrected historical September 23 quotation flagged. Startup sizes: CATO AGENTS6,465 / CHARTER9,921 / CONTINUITY24,829; root CLAUDE24,961 / USER5,200 / AGENTS5,313 bytes, all below32,550. Generic read-cap remains rc2 CANNOT-EVALUATE (no CATO CLAUDE); direct measurements are separate. No conditional ledger, memory or figure-consumer check triggered. Exact-file commit and fresh-fetch publication receipt delivered in-session.
