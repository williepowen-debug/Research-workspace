# PROME / NEXUS September 29 afternoon — first correction pass

## Current assessment

Correct the new prediction before using it to decide whether an independent AI-disruption cause exists, and correct PROME's description of the remaining duration book before the October 2 sitting. Five substantive findings (PN1–PN5) and one small state correction (PN6) remain open. This is review advice; CATO changed no owner artifact, prediction, portfolio record or decision. The first pass is complete; no further assignment is assumed.

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
