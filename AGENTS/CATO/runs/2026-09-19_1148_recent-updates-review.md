# Recent agent updates — September 19 review

## Scope and disposition

Will asked CATO to review recent commits and agent updates for needed corrections. Main pinned range: `a2522254c..1b148338809bedc4de7a0e1f1c78c34273964ae1` — **112 commits / 318 changed paths**, including one CATO evidence commit. This is a risk-selected review of SAM adjudication, HANS research/data controls, ZHAO export-control packets, HAWK monitoring logic, and PROME follow-through; not certification of all 111 other commits. OSPREY's scope/backfill corrections, DAEDALUS's read-cap ruling, and PROME's sitting/rebase reports received a narrower documentary read.

**Eight correction items below. No owner repairs, sends, launches, grades or trading actions performed.** HANS and MARCO were actively changing files; their work was preserved. CATO's earlier implementation is not independently certified by this review. Sources were inspected directly where indicated; other claims remain owner evidence. No live market prices or complete historical price-series reconstruction are certified.

Evidence: [offline probes](2026-09-19_1148_recent-updates-probe.py), [results](2026-09-19_1148_recent-updates-probe.txt), [inventory](2026-09-19_1148_recent-updates-inventory.txt). Probe success reproduces historical defects; it is not repair acceptance.

## R1 — HIGH — HANS turns aggregate net borrowing into assurance about gross credit losses

**Locations:** `AGENTS/HANS/workbook/2026-09-19_ESRB_REPORT202602_PRIMARY_READ.md:64–66`; `workbook/PREDICTIONS.tsv`, HNS-09; `workbook/KB.tsv`, KB-HANS-091; delivered ESRB packet to LIQUID/REGINALD, item 3. Introduced in `013785271` and routed in `e2e4ef081`.

The new rationale says the euro-area private-credit loss channel is small by construction because banks are aggregate net debtors to NBFIs. That does not follow: net borrowing does not bound gross loans, concentration, losses or their effect on equity. A bank with 150 of NBFI funding and 100 of NBFI loans is a net borrower of 50; a 20% loan impairment still loses 20. It can suffer funding stress and credit losses together. Sector-wide net positions also cannot certify each institution's exposure.

The [ECB/ESRB report](https://www.esrb.europa.eu/pub/pdf/reports/esrb.report202602_financialstabilityrisks.en.pdf), executive summary and §§3/3.3, emphasizes funding vulnerabilities but retains counterparty credit risk and says data gaps prevent a complete assessment. Its PE/PC exclusion supports HANS's measurement warning, not the inference that the unknown exposure is necessarily small. CATO verified these passages at the primary.

**Second manifestation:** the outbound packet describes HNS-09 as no bank reporting a materially private-credit-driven loss. The actual frozen prediction is broader: sector NII/earnings holding with no material rise in cost of risk. The narrower paraphrase could change the later grade.

**Correction:** retain the funding-risk insight and data-gap caveat; withdraw the inference that net debt excludes/materially limits gross private-credit losses. Restore HNS-09's actual outcome in summaries and ask HANS to reassess the rationale for its unchanged 70%, without CATO setting a replacement probability. Correct both recipients and the canonical row/KB. The report's observed low risk for some other exposures is not a blanket private-credit conclusion.

## R2 — HIGH — ZHAO's Chinese-control packet changes both the unit and the end-use scope

**Locations:** `AGENTS/ZHAO/outbox/delivered/2026-09-18_to-VULCAN-HAWK_the-other-half-of-the-clock-chinas-own-restraint-expires-11-10.md:18–20`; matching recipient packets; KB-ZHAO-166 and `docket/CATALYSTS.tsv` November 10 row. Introduced in `5ce72a1e9` and routed in `020569fed`.

The packet describes any goods with 0.1% Chinese rare-earth content, and advanced chips destined for military AI. The named [MOFCOM Announcement 61](https://interview.mofcom.gov.cn/mofcom_interview/front/swfgk/article?id=20251003602119), §I(1), instead uses a **value proportion** between specified Annex 1 input and output classes. It is not a generic mass/content test covering every manufactured good. Section IV covers the specified advanced logic/memory and related equipment/material end uses **or** development of AI with potential military uses; military AI is not a necessary qualifier on every chip case. Section III separately addresses military end uses.

**Consequence:** the question sent to VULCAN could overcount unrelated products while excluding relevant civilian advanced-chip end uses. A B2 source caveat does not cure those scope errors.

**Correction:** ZHAO should rewrite the packet and its calendar/KB mirrors against the primary, bind the 0.1% calculation to value and Annex classes, and preserve the separate end-use limbs. [Announcement 70](https://interview.mofcom.gov.cn/mofcom_interview/front/swfgk/article?id=20251103606112) was accessible and confirms the November 7, 2025 suspension instrument through November 10, 2026. That closes the recorded inability to fetch the named primary, but does not establish an exact intraday restart or certify absence of subsequent amendments. CATO did not classify any particular product under the annexes.

## R3 — MEDIUM — ZHAO/PROME treat the last suspension day as the BIS reactivation day

**Locations:** ZHAO's delivered `2026-09-18_to-VULCAN-HAWK_bis-affiliates-rule-stay-lapses-nov-9-one-day-before-the-truce.md:18`; calendar November 9/10 rows; PROME's newly registered three-clock docket sequence and recipient packets.

The packet says controls reactivate November 9, one day before the tariff event. The [published BIS rule, 90 FR 50857, §§I.B–C](https://www.govinfo.gov/content/pkg/FR-2025-11-12/pdf/2025-19846.pdf), expressly distinguishes suspension ending November 9 from reimposition **effective November 10, 2026**. Reading only its summary loses that distinction. Verified in the published PDF and matching public-inspection text.

**Correction:** keep November 9 as an advance monitoring deadline if useful; label it accordingly. Correct the US reactivation date and withdraw the one-day-apart assertion. Keep the instruments separate, and do not infer identical intraday clocks across jurisdictions. This is a correction to the cited instrument, not a comprehensive legal-currentness opinion.

## R4 — HIGH — SAM's firm FALSE grades exceed their unresolved episode evidence

**Locations:** `AGENTS/SAM/docket/2026-09-19_SAM28_SAM31_GRADE.md:83–99,109–122`; terminal prediction rows and scoreboard; `16eb01475` and `c3c498ecc`. Compared with the September 9 governing packet and frozen original rows.

The corrections to the prep file are useful, including restoring the omitted September 8 observation and withdrawing whole-window appreciation as the route test. They do not resolve these problems:

1. **SAM-28 is existential: at least one route.** Four failed routes cannot settle a fifth whose qualifying convention remains unresolved. The report admits a reasonable TRUE reading yet uses the four failures and the modal forecast to justify FALSE. Forecast probability is not outcome evidence. The governing packet explicitly permits qualified/no-verdict when the convention remains unresolved.
2. **The new timing argument counts a weekend as a trading session.** July 31 was Friday; August 3 was Monday, the next session, not the second session after the final operation. This incorrect distance is used to characterize attribution as an extra retrospective concession. Correcting it does not prove causality, but removes that claimed reason for rejection.
3. **Episode B is not an established untreated control.** Its September 7/8 official attribution remains OPEN. Even a genuinely unexposed episode with a similar return would establish that price shape alone is non-identifying, not that the documented intervention in Episode A had no causal effect. Unknown treatment cannot become known absence.
4. **SAM-31's negative average cannot independently disprove an episode claim.** Seven risk-off sessions had positive FXY returns by SAM's corrected count. A negative average across all 24 can coexist with a qualifying yen-haven episode. The September 9 packet also called for matched intraday cross-pair evidence, especially July 13; the new grade supplies aggregate FXY statistics instead. Its regime argument may ultimately support FALSE, but is a separate convention-sensitive judgment, not rescued mechanically by the mean.
5. **A single modal hit cannot establish probabilistic calibration.** The new record's correctly-calibrated label for these outcomes should be narrowed to the observed outcome under the chosen convention, with calibration assessed across appropriately resolved forecasts.

**Correction:** SAM should correct the session count; retain uncertainty about the September control; adjudicate each original episode requirement with its contemporaneous convention and matched evidence. Where no convention resolves the alternatives, carry a qualified/no-verdict disposition rather than an unqualified failed row. Recompute the scoreboard only after that owner adjudication. CATO is **not** assigning TRUE instead, recomputing the live market histories, reopening the retired frame, or proposing a trade.

## R5 — MEDIUM — HANS's five-year norm accepts four years and invalid observations

**Locations:** pinned `AGENTS/HANS/scripts/fetch_eu.py:125–130,213–226`; registry HANS-T-08 defines the norm as the mean of the previous five years for the same gas day. New implementation in `b32de23ba`.

Offline response fixtures using HANS's reported five historical values reproduce:

| Case | Returned norm | Gap at fill 69.06 | Printed band |
|---|---:|---:|---|
| All five years | 85.054 | −15.994 | ORANGE |
| 2023 unavailable | 82.85 | −13.79 | GREEN |
| Two years unavailable | unavailable | withheld | UNKNOWN |
| All records have the wrong gas day | accepted as five requested years | −15.994 | ORANGE |
| All values are `NaN` | `nan` | `nan` | GREEN |

The four-year quorum is deliberate in the function, but does not implement the registered five-year metric; it changes the band solely because data is absent. The output prints the year count, so this is not concealment, but still certifies a substitute basis. Response date identity and finite values are also unchecked.

**Correction:** require the registered five valid, date-matched historical observations for a canonical gap; otherwise mark it incomplete and withhold the canonical band/observation. If HANS wants a four-year estimate, label it separately and establish its permitted use explicitly. Validate finite, plausible fill values and aggregate identity. Test healthy, one/two missing years, wrong dates and nonfinite inputs.

**Limit:** no live bad AGSI response was observed. These are controlled counterexamples. The published five-year arithmetic reproduces. The script does not itself close HANS-T-08: its exit additionally requires five consecutive gas days above −12, and that separate condition is preserved. The finding is a wrong displayed band/observation, not an actual false exit.

## R6 — MEDIUM — HANS's closeout runner reports process failures as passed

**Locations:** `AGENTS/HANS/scripts/closeout_check.py:53,56,59,137`, introduced in `9378cfd66`.

Three checks treat any integer return code as success. Mocking the two consumer checks and ledger nudge to return **1**, **2**, or **−15** in separate runs still produces `8/8 executed · 0 failed` and exit zero, with a final assertion that every mechanical step passed. The remaining five controls return zero in each test. A Python traceback, argument failure or terminated subprocess can therefore receive the success summary.

The runner's disclaimer that it cannot certify judgment does not address its own process-success claim. Consumer checks are invoked without `--strict` and normally return zero even for advisory findings; accepting arbitrary nonzero codes is not needed to preserve those advisory findings.

**Correction:** distinguish successful execution with findings from failure/unknown according to each tool's actual return contract. Propagate unexpected nonzero exits/signals and enough diagnostic output. Test all-pass, advisory output with expected rc, explicit checker failure, argparse error, signal and timeout. Do not silently turn every advisory finding into a blocker.

**Review precaution:** the HANS test suite deliberately writes/restores real charter/ledger files. CATO did not run that suite in the shared active tree; the counterexamples use pinned in-memory modules and mocked subprocesses only.

## R7 — MEDIUM — HAWK's Article 4 revision still overclaims what observation can identify

**Locations:** `AGENTS/HAWK/domain/europe-rearm/LADDER.md:64,103,105–110`, revised in `4044ad71a`/`233dfc212`.

Two claims need narrowing:

- The June-updated [NATO eastern-flank overview](https://www.nato.int/en/what-we-do/deterrence-and-defence/strengthening-natos-eastern-flank) mentioning September 2025 consultations does not certify zero invocations through June 2026. It is not an exhaustive consultation register. A relevant contemporary page is better evidence than an old page, but its silence is still not an affirmative absence record.
- One future invocation/non-invocation within seven days cannot establish that the threshold never rose/has demonstrably risen, nor justify declaring the indicator dead. Severity, attribution, politics, existing responses and timing remain alternatives. HAWK identifies those confounders elsewhere, then discards them in this binary test. The assertion that a requester gains nothing from invocation is also unsupported: [NATO describes Article 4](https://www.nato.int/en/what-we-do/introduction-to-nato/the-consultation-process-and-article-4) as consultation potentially leading to joint decisions/action, not a one-time capability switch.

**Correction:** label the absence inference with its coverage limits. Retain the future event as evidence updating competing hypotheses, with the seven-day window a proposed convention; do not promote either branch into definitive identification or automatic indicator retirement. The methodological objection survives even if all named incident facts are later verified.

## R8 — MEDIUM — HAWK's Monday mobilisation card permits a false definitive negative

**Locations:** `AGENTS/HAWK/research/2026-09-19_L432_resolution_card.md:44–46,69–75`; associated September 21 CATALYSTS entry.

The card correctly quotes three permitted primary classes, including a dated Western-government assessment. Its final rule permits only a decree title or official statement, while the Western-government publication path is still unresolved. More importantly, the negative branch promotes absence of a mobilisation-titled decree and Kremlin announcement to NOT DECIDED. That establishes at most **no announcement found in those checked surfaces/window**, not that no decision occurred. A differently titled act, body-only provision, Duma/MoD statement or another permitted primary can escape this test. The card expressly admits unreadable bodies and an unchecked MoD leg.

**Correction:** restore all permitted primary classes and a usable Western-government source path; state exactly what a negative search establishes. Where coverage cannot answer the registered question, use STILL UNKNOWN or distinguish no public announcement found from no decision. Retain a bounded observation window and the prohibition on press speculation becoming a grade. CATO did not grade the future event or attempt a comprehensive Russian legal-publication audit.

## Prior findings and work that improved

- **HAWK's earlier Romanian count error remains:** LADDER still says four July shoot-downs; INCURSIONS has three KILL rows (005–007), followed by 008 explicitly unengaged. The old E3 falsifier still says re-attribution would make the engagement count a clean intent measure. Those are retained September 18 N3/N4, not new findings. Several other HAWK corrections are real: mandate timing/effective date separated, unsupported 22-year denominator withdrawn, incompatible Romanian count bases disclosed. These improvements do not settle R7.
- **SAM's roll-window checker and PROME's wrapped-prose hook are unchanged from the last pinned review.** Do not treat new research commits as closing their earlier counterexamples.
- **BOND's subgroup-versus-standalone summary needs its earlier correction;** the WQ-157 wording was already better. No historical auction dataset regrade performed here.
- **PROME's sitting explicitly refuses to manufacture the ARGUS trial metric**, separates daily spawn counts from per-boot limits, and identifies missing attribution. These are useful limits. Its M1 first/last/carried-commit medians are proxies, not an enumeration of every actual boot; the phrase all defensible readings is stronger than those three samples establish. This pass did not reconstruct all boots or independently grade the trial.
- **PROME's HEARTBEAT rebase documents its correction of an invented blocking rule**, known residue, and new rotation checking. The heading-multiset selftest passes 7/7 and queue-parser synthetic parity passes 26/26. These are limited checks, not independent verification of every rebase fix, hosted publication, or all agent output.
- **OSPREY records its two withdrawn scope claims and new strike backfill, and PROME's WQ-266 carries that correction.** No independent vessel-event enumeration or ratification of its self-ruling was performed here.

## Delivery and next step

Recommended correction order: **HANS's already-routed credit inference and ZHAO's routed rule scope/date first; SAM's scoreboard adjudication next; HAWK's September 21 negative-verdict logic before that event; then the data/runner controls and Article 4 overclaims.** Route through the responsible owners; this review itself sends nothing and changes no owner judgment. The full evidence remains here for Will/PROME to use directly.

CATO's assigned review is delivered. No repair project is started. Next session: orient and await Will; if follow-up is assigned, recheck current revisions and owner dispositions before reopening any item.

Closeout/revision recheck is recorded below before commit; the actual commit and fresh-fetch push receipt are delivered in-session.

## Final recheck and validation

At `503c65677`, HANS's newer authentication diagnostics had landed alongside MARCO/PROME work outside the main review snapshot. Compared 14 cited source files against the pinned snapshot: 11 unchanged; HANS fetcher, KB and predictions changed. The specific KB-HANS-091 and HNS-09 rows remain byte-identical. The fetcher changes address empty-response authentication diagnostics and publication-lag uncertainty; they do not repair R5. [Current-code probes](2026-09-19_1148_recent-updates-current-probe.txt) reproduce all storage and closeout counterexamples, including actual rendered output and structured storage observations. Each loaded module's SHA256 is recorded. No claim that the later MARCO/PROME commits received the full review.

[Closeout checks](2026-09-19_1148_recent-updates-checks.txt): orphan advisory rc 0 (other-session HANS completion and memory work preserved), weekday check rc 0, rotation selftest 7/7, queue-parser parity 26/26, CATO tracked whitespace check clean, staged list empty at check. CONTINUITY 25,146 bytes, below the 32,550-byte limit. No owner test suite was run against mutable owner files. No canonical figure was superseded by CATO, so no consumer sweep was triggered. Only the six new evidence/report files and CATO CONTINUITY belong in this commit.
