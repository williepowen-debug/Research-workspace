# Twelve-case forecast feasibility pass

**Completed October 1, 2026 — stop at twelve.** Recommend settling the admission and version rules on these cases before commissioning the remaining 133. Historical recovery is useful, but the present obstacle is deciding what counts as a forecast and which exact claim a probability belongs to. More extraction alone will not settle that.

Six of the twelve have numeric probabilities recorded before resolution. Three — HANS HNS-05 and OZK-05/06 — also have usable original binary contracts and primary-confirmed event outcomes in this pass. CREED is recoverable with two materially different versions; RED and CRUISE need adjudication and further outcome work. The other six lack a recoverable owner registration probability in the checked evidence. Two of those are March material entered into ledgers in August, outside the proposed registration cohort. These are feasibility dispositions, not a hit rate, eligibility estimate for the fleet, or skill result.

## Scope and provenance

Will authorized registration/specification/eligibility/outcome checks and effort recording for the critic's fixed twelve. No replacements, headline score, owner edits, messages, fleet launches, or further historical audit. Source snapshot: `e70f558f4ad685cec394a9cdc2ef6ee622d6b6e0` (September 30, 22:19 EDT). V4 extraction: `f18929d7324f737a6184470d86db100c480af3d8`. External sources were retrieved October 1 UTC; these are present-day reads of dated releases, not independently archived proof of exactly what was publicly available at every historical instant. Git establishes recorded content and commit timestamps, not tamper-proof registration.

The [plan](PLAN.md), three population/selection tables and [input hashes](freeze.json) were committed as `eaa3a6eae` before case review. Prior scores were available, so this was a fixed selection rule, **not blind preregistration**. No performance score was calculated in this pass.

The critic attachment arrived during case 4. Its [preserved bytes](critic_cohort_received.tsv), SHA-256 `753fd797e309662a4752c462d571763eedff14bd57d7bdcb7e7211cec423c92d`, contain exactly the same 145 IDs in exactly the reconstructed order; all hash prefixes match. [Comparison receipt](cohort_comparison.json). The original freeze remains unchanged and accurately records that the attachment was unavailable at freeze.

## CF1 — material: cohort membership needs evidence, not parser dates

The literal candidate rule yields **152 rows / 26 desks / 54 unknown deadlines**. The critic's **145 / 25 / 47** excludes seven `open_undated` rows. Both frames are saved. This confirms an omission in the claimed unfiltered enumeration, not that the seven belong in the final cohort. Unknown deadlines remain unknown; they do not satisfy a September 30 cutoff automatically.

The omitted keys are CREED/PRED-CREED-001 and -002; LIQUID/LIQ-04; CARL/CRL-28; CARL/DOC/DOC-P10; HAWK/HAW-20; SAM/SAM-33. None was substituted into the twelve.

Three of the critic's four apparent post-deadline registrations are false alarms: CREED-006 resolves on the September MBA publication; OZK-05/06 explicitly resolve at the July 21 earnings release. June 30 was the measured period-end. FERT-10 really was entered retrospectively in August, but its claim is already in March Git history. FERT-08 has the same March origin. Thus ten selected records remain June–August candidates and two are out of that registration window.

**Correction/closure:** before a larger cohort, distinguish measured period, registration, forecast deadline and source-publication window; retain unknown membership and retrospective imports as reported findings. Do not discard them silently or rewrite the frozen sample. No census code changed here.

## Case dispositions

Full per-case reasoning and exact source pointers are in [cases.json](cases.json); [case_dispositions.tsv](case_dispositions.tsv) is the compact machine-readable view. The twelve named JSON files preserve complete pinned rows and recovered ledger-history candidates. Those extracts are evidence of what the desks wrote, not independent verification of every claim within them.

| Case | Registration and specification | Eligibility / independently checked outcome | Disposition |
|---|---|---|---|
| CREED PRED-CREED-006 | July 27: >$3.3B at 65%; same day amended to ≥$10B at 30%, both before release | MBA printed change +$7.830B verified: original event true, amended event false | Choose version policy; never combine original odds with amended claim |
| RED-20 | July 24 five-category distribution, modal S1 52%→54% before meeting; wording also narrows | Fed confirms hold and hike dissents; complete September-guidance branch not certified | Categorical/binary projection and qualitative branch need adjudication |
| HANS HNS-05 | August 28 original 75%; explicit conditional update later 88% | ECB +25bp to 2.50% verified; original row usable | Keep original and update separate; disclosed scenario-tree 81% inconsistency travels |
| OZK-06 | July 4 original 40%; July 18 card and July 20 precision clarification | Issuer past-due $298M / 0.92% confirms false on specified basis | Usable; July 21 publication window, not June 30 |
| VULCAN-06 | July 12, PROVISIONAL evidence tier; capex AND power/commitment conjunction | No numeric p; owner HIT not fully verified from four issuers | Qualitative forecast, not a probability-score input |
| VULCAN-11 | August 3, PROVISIONAL; explicit three-way test ending September 30 | No numeric p; two falsifier legs verified, exact September 30 close not retrieved | Full outcome still unresolved in this pass; October 1 grading was scheduled |
| FERT-08 | March claim recovered; August ledger entry already MISS; 4/5 severity | No numeric p; owner correction corroborated only by secondary reporting | Outside registration cohort; contemporary assertion, not new August forecast |
| CRUISE CRU-05 | August 14 at 50%; conditional level test with unnamed basis details | Owner admits ambiguity; two closes corroborated, full means/antecedent not replayed | Admission ruling and full input reproduction needed |
| OZK-05 | July 4 at 50%; pre-print card fixes reported annualized NCO basis | Issuer quarterly 0.69% >0.55% verifies true | Usable; dependent on same issuer/print as OZK-06 |
| FERT-10 | March scenario recovered; August retrospective HIT; 3/5 severity | No numeric p; government confirms April 2.5Mt procurement, not every mechanism/price assertion | Outside registration cohort; original hard deadline not found |
| MIDAS-03 | July 12 diagnostic with EMPIRICAL tier; both written branches require yields up | Owner says yields fell and grades a broader weekly mechanism instead | Registered branches do not support owner HIT; no numeric p |
| HENRY HEN-42 | July 23 original has no owner odds; another desk's quoted 85% is not a substitute | Explicit UNSCORED-AS-MADE; full market-path outcome not independently replayed | Preserve calibration exclusion |

Primary witnesses: [MBA Q2 table, printed page 7](https://www.mba.org/docs/default-source/research-and-forecasts/cmf-mdo/2q26mortgagedebtoutstanding.pdf); [Fed decision](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm) and [full press conference](https://www.federalreserve.gov/mediacenter/files/FOMCpresconf20260729.pdf); [ECB decision](https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260910~314e508016.en.html) and [original Eurostat flash](https://ec.europa.eu/eurostat/web/products-euro-indicators/w/2-01092026-ap); [OZK management comments, printed pages 19/22](https://ir.ozk.com/2Q26_Management_Comments); [Micron release](https://investors.micron.com/news/press-release/2026/Micron-Technology-Inc--Reports-Record-Fiscal-Fourth-Quarter-and-Full-Year-2026-Results/default.aspx), [TrendForce September 30 release](https://www.trendforce.com/presscenter/news/20260930-13258.html); [Indian government procurement record](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2288855&lang=1&reg=3). PDF tables were visually checked; the MBA and OZK download hashes are in cases.json. Secondary and unavailable-source limits are recorded per case.

## CF2 — material: freeze the claim with the probability

CREED is the decisive counterexample to “a frozen probability column fixes it”: July 27 commit `43639b22c` records one threshold; `b20715cef` records a different threshold and probability before publication. Both can be legitimate forecasts, but they are different events. HANS shows a different case: the event is unchanged and the update rule was stated in advance. Neither history establishes deliberate inflation.

**Correction/closure:** specify the evaluation target before scoring. Recommended original-forecast view: retain the first recoverable prospective claim, odds and resolver together; keep amendments/updates separately linked and timestamped. In the present sample CREED's original view would mean 65% on >$3.3B, not 65% on ≥$10B. Categorical or conditional questions require an explicit comparable scoring rule; current confidence remains a distinct view. Apply existing records and annotations before building more machinery. This is advice, not an installed fleet policy.

## CF3 — material: a research test is not automatically a probability forecast

VULCAN's contemporary instructions deliberately use EMPIRICAL/PROVISIONAL/ASSUMPTION evidence tiers. FERT's 3/5 and 4/5 are convergence severity scores. MIDAS registers a diagnostic branch map without choosing an outcome probability. HENRY explicitly declines to backfill as-made odds. Converting these fields to probabilities would invent evidence.

MIDAS also supplies a concrete grade mismatch: the owner acknowledges that neither registered yield-up branch occurred, then claims HIT on a broader weekly mechanism. That admission is verified in the pinned row; this pass did not independently replay the market series. RED's full branch and CRUISE's admission exception remain unresolved rather than being forced into binary labels.

**Correction/closure:** keep forecast type, original probability, eligibility reason and outcome evidence distinct. For this sample, resolve CREED's version rule, RED's category/branch and CRUISE's admission question before treating all six numeric rows as a comparable set. Preserve the other six in the recoverability denominator. Outcome uncertainty must not become a favorable or unfavorable binary by default.

Lower-priority HENRY residue is deferred: its August 28 grade card says a 13bp two-day flattening would require two ≥p99 daily moves, despite quoting p99=10bp. That implication is arithmetically false. It does not by itself reverse the final path-based MISS, and the row is already calibration-excluded. No separate repair commission or broad HENRY audit follows.

## Effort, value and stop

[Timing record](timing.json): shared setup **2m43s**; twelve focused case passes **13m10s** total, median **44s**, range **31s–3m35s**. These are measured agent wall-clock intervals including tool waits, not human labor estimates. Case 4 includes attachment reconciliation and session-context overhead; case 9 reuses the issuer source and supplies a follow-up clarification to case 4. Report writing, source-extract integrity checks and Git delivery occur afterwards and are excluded from those case totals. Source reuse and unresolved source hunts make linear extrapolation to 133 inappropriate. This was a feasibility pass, not twelve completed forensic outcome audits.

The return is concrete: three usable original binary examples; a demonstrated claim/probability version trap; two proven cohort errors; six rows where numeric registration evidence is absent in the inspected record; and named reasons why more row harvesting would not settle the question. It demonstrates recoverability and specific failure modes, not investment advantage or the overall quality of the 25 desks.

**Suggested next step:** Will adopts a short original-forecast admission/version rule using these cases, then commissions only the unresolved decisions needed to apply it. Prioritize CREED/RED/CRUISE adjudication over a full 133-row backfill. If a prospective measurement pilot follows, use existing desk ledgers and grade only fully specified new forecasts; retain updates separately. That prospective pilot, owner corrections and remaining historical work are **not authorized by this pass and have not begun**. No additional desk work is justified merely by a poor aggregate number.

## Checks and delivery

Author data checks: all frozen input/table hashes unchanged; exactly twelve dispositions and timing intervals; **25 current/history source rows** match their exact Git blobs and field counts; received critic population/order/hash prefixes match. [checks.json](checks.json). No scoring function or operational code changed; no new test suite needed. CATO authored v4, so these checks are author follow-up, not independent certification of that implementation. External case checks are independent of the desk accounts only to the scope expressly stated above.

Root closeout checks and delivery receipt follow below. Concurrent PROME/CREED/memory work was preserved; no pull across their dirty paths. Publication is repository delivery only, not a hosted dashboard or a message to another agent.

Closeout checks: root orphan advisory reports other owners' PROME/memory work; no CATO-authored outside paths found and none swept into delivery. Weekday claim check passed on the three existing PROME registry/queue files, CATO STATUS and this report. Authored-file `git diff --check` passed. The staged check flagged the supplied TSV's preserved CRLF endings; all 146 lines retain those original bytes. Rechecking with `cr-at-eol` passed; the evidence file was not normalized. The generic `read_cap_check.py --agent CATO` returned CANNOT-EVALUATE because it expects a CLAUDE.md; it did not certify the startup surfaces. Direct byte checks of the six actual startup reads passed the 32,550-byte limit: CATO AGENTS 4,278; CHARTER 9,921; CONTINUITY 13,238; root CLAUDE 24,236; USER 4,626; root AGENTS 4,991. No STATUS, auto-memory, operational ledger, or published CATO numerical-series revision was made, so ledger-nudge/memory-index/consumer-series checks were inapplicable. Exact-path Git receipt is delivered in-session; no follow-up commit solely to record its own hash.
