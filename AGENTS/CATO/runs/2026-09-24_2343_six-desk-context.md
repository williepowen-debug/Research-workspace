# Six-desk live-session context — September 24, 2026

**Disposition:** initial context read delivered. Will is running PROME, VIOLET, HENRY, LIQUID, ORACLE and BOND and asked CATO to act as a second pair of eyes, beginning with their recent updates. Their shared market interpretation is more qualified than the early evening summaries. VIOLET's in-progress RQ8 study has a material forward-return comparison defect and overlapping verdict rules; resolve these before relying on its claimed predictive result. No owner edit, send, launch, publication or trading action by CATO.

**Current disposition, September 25 follow-up at `d6cc9bc0d`:** SG1 arithmetic repaired and independently checked against all 40 saved post-event return cells (maximum error zero); inference wording remains too strong. SG2 collision disclosure and exploratory-subgroup labeling accepted in the current report; neither branch selected as the formal verdict. Owner now attributes the missing current event to an absent September 22 yfinance bar; source explanation disclosed, raw series not independently checked by CATO. Recommend one bounded wording completion, then park RQ8; no expanded study assigned. Suggested group directions below are proposals to Will, not issued tasks.

## Scope and evidence

Entry/latest inspected committed HEAD `89363b3b713e6f1e79e9d8d7498aa092d855fa8b`; master. Read all six current STATUS files, PROME's current SCRATCH directions and relevant closeout/ruling records, HENRY's peer synthesis and new FedWatch-method note, ORACLE's recession-contract correction, and VIOLET's RQ8 report, code and saved results. The study was actively dirty/untracked; findings concern the saved snapshot, not a completed owner delivery. Companion `2026-09-24_2343_six-desk-context-evidence.json` preserves its source texts, hashes and CATO arithmetic. No pull over owner work.

Market figures below describe owner-recorded September 24 observations (credit primarily September 23), not independently refreshed or live quotes. This is a bounded context/read-through, not primary-source certification, a full code review or a whole-fleet acceptance.

## Group context

| Desk | Current contribution | Limit / next obligation already on its record |
|---|---|---|
| PROME | HEARTBEAT 21st rebase; WQ-288 invalidation-at-fire clause encoded; Deck v42/reference v8 publication owner-reported. WQ-289 subsequently ruled at 23:37, covering the held push and narrow rename-verification repair. | Later closeout's HELD state predates that word; do not request it again. Repair remains L473, acceptance conditions and independent reader required. HEARTBEAT amendments queued for September 25. Hosted delivery not independently inspected here. |
| VIOLET | Rates volatility and equity volatility moved on the same days; rates moved further. Withdrawn lead-lag and uncalibrated signature claims. New RQ8 base-rate study underway. | CBOE history still missing September 23–24 in owner snapshot. WQ-259 page refresh remains contingent on confirmation. RQ8 issues below. |
| HENRY | Nominal 10Y +22bp over two sessions equals the real-yield change in its matched data. Gamma estimates straddle zero at the flip; old walls withdrawn. New October-hike estimate ~72%. | 72% is a vendor-futures calculation under hold/+25 assumptions, not CME's published probability or settlement. Cannot directly measure the gap to differently timed ORACLE quotes. F1 crack estimate is not finalized settlement; September 25 grade/board refresh owed. |
| LIQUID | September 23 widening reached B as well as CCC; HY +5bp remained ordinary on its unconditional comparison. Reserves fell while TGA rose; observed funding gauges calm. | One day does not establish transmission. No tri-party/sponsored-repo/dealer-balance-sheet observation. September 30 settlement/quarter-end, then non-quarter-end observations, is the named next test. Old BOTTOM LINE now explicitly bannered; substantive recut owed. |
| ORACLE | October hike repricing agrees across prediction venues. Recession rules read corrects months-old NBER-only label: Kalshi contract is GDP-based; PM has an additional NBER-announcement branch. | Contract mismatch prevents a clean disagreement inference; RED correction packet exists, consumption unverified. September oil leg is expiring; October $110 contract availability/re-pin due September 28. |
| BOND | Second real-led long-end high; 5Y auction composition rule fired, funding confirmation absent. ACM decomposition supports expected-path repricing over its stated window. | Threshold fire does not prove auction mechanism failure. Add declined under WQ-280. FR2004 settlement/as-of alignment unresolved; do not turn an inventory snapshot potentially preceding settlement into disproof of absorption stress. |

**Synthesis:** observed repricing is strongest in rates; equity volatility and lower-quality credit have moved, but broad credit/funding transmission is not established. Differences of units, observation windows and instruments prevent ranking these changes as a measured causal cascade. HENRY's same-date real/nominal decomposition is useful; it alone does not identify why real yields rose. ACM/Kim-Wright claims must retain model and window. September 30–October 2 is the group's shared catalyst window; no new trade follows from agreement among the desks.

## SG1 — Material: RQ8 compares different return windows

**Source:** saved `scripts/rq8_study.py`, `forward_paths()` versus `unconditional_baseline()`; report §§4–6.

The cohort return divides VIX at T+k by VIX at T−1 (`p0 - 1`); the baseline divides VIX at T+k by VIX at T. Thus the claimed T+1 signal includes the event-day move in a two-session cohort return but compares it to one-session unconditional returns. The pre-registration also calls T−1 the session before a two-day window, an inconsistent description needing clarification.

**Independent saved-data arithmetic:** calculate `100*(VIX[T+k]/VIX[T]-1)` for each of the ten saved events, then take the median. T+1 = **−0.5765%**, versus baseline −0.62%, approximately **0.006 baseline standard deviations** apart. The draft's +12.4% / 1.68σ is not a post-event predictive result. Matched T+3/T+5/T+10 medians are −4.2798% / −7.5007% / −6.2808%. This is descriptive arithmetic on owner data, not a significance test or a source-verified historical backtest.

**Consequence:** the report can mistake same-day co-movement for the forward transmission it was commissioned to test, even while disclaiming applicability to today's low-VIX state.

**Correction / closure:** owner defines the return clock explicitly, reports matched cohort/control windows and distinguishes contemporaneous response from post-event returns; correct report/STATUS/KB/brief and routed copies where adopted. Retain the original pre-registration and disclose amendments. Do not claim a real future signal from the present comparison.

## SG2 — Material: RQ8 PASS and FAIL rules overlap

**Source:** report frozen §1 falsification rules, §4 results and §5 verdict.

PASS allows ≥60% VVIX>100 AND ≥60% ratio<1.10 at T+5 (or a return-separation alternative). FAIL fires if any T+1/3/5/10 return separation is <0.5σ. The draft reports 80%/100% threshold frequencies, but 0.30σ at T+3 and 0.17σ at T+10. Its own numbers therefore satisfy both rules; reporting only “PASSES on the letter” is unsupported without precedence. The claimed “pre-committed subsegment” n<8 rule was not registered as a low-starting-VIX subgroup rule in §1; that stratification is exploratory.

**Correction / closure:** disclose the rule collision and do not retrospectively select the favorable branch. Any amended verdict logic is dated as such; exploratory subgroup results remain exploratory. Thresholds already satisfied at T+0 do not show that the signal predicted a new crossing. Keep unsupported dashboard thresholds withdrawn.

**Further bounded reconciliation owed before acceptance:** the report ends its purported through-September-24 cohort in March 2026, although the owner's September 22/24 MOVE levels imply a qualifying +33.12%. This could be source-series disagreement or sample handling; raw pulled series were not preserved/read here, so cause UNKNOWN. Reconcile inclusion and horizon-specific missing observations. No historical labels or date-count claims certified.

## Corrections to earlier context and operating limits

- Startup carried RC1 OPEN from CATO's afternoon cutoff. PROME now records RC1 closed after NEXUS `2c73ce505`; CATO inspected the current owner letter's corrected checklist and repeated-C paragraph: no quiet-market inference, squared rates explicitly an independence illustration, frozen branch rule retained. Those local interpretation corrections are verified here; complete STATUS/brief/consumer propagation is not re-certified.
- VIOLET's second walk-back and LIQUID's banner/frozen completion record have landed; do not send duplicate requests for those changes.
- WQ-288 and WQ-289 are ruled, not new asks. WQ-259 has an outstanding data condition. WQ-246 and WQ-157 remain separate owner/operator questions; this context read changes neither. Broker/current-book verification remains WQ-274; no trading authority inferred.
- No owner repairs implemented or owner tests rerun. CATO independently recomputed the saved RQ8 returns only. Further source checks and later owner changes are unverified.

**Resume:** support Will's six-desk session on his next direction. Recommended immediate focus: a bounded RQ8 correction/recheck before new studies or predictive claims. Then keep the existing settlement/publication/quarter-end obligations in view. Findings delivered to Will in-session; no packets or messages sent to owners. CATO report/evidence/continuity only; exact-path commit and push receipt delivered in-session.

## September 25 — directions requested by Will

Will relayed PROME's verification/correction receipts, then asked what instructions to issue next. Rechecked current VIOLET report §§1a/4–6, return code, saved forward CSV, STATUS/NEXUS_BRIEF and PROME SCRATCH at `d6cc9bc0d`. The corrected `vix_pct_vs_t0` column agrees exactly with independently recomputed VIX[T+k]/VIX[T]−1 for each of ten events at four positive horizons. Medians reproduce −0.576509%, −4.279849%, −7.500674%, −6.280775%. No network/source refresh or whole-program rerun.

**SG1 partial closure:** code and saved arithmetic accepted in scope. Report/STATUS retain “no measurable” or “indistinguishable” language, which a difference of medians divided by the baseline standard deviation cannot establish. T+1 is slightly ABOVE the baseline, so the repeated “at or below every horizon” is also literally wrong, though economically tiny. Concrete final wording: “The corrected ten-event sample does not establish a forward VIX signal in either direction. The previously reported positive signal is withdrawn.” Apply to active report/STATUS/brief/KB and PROME summary wherever the stronger claim survives; retain clearly labeled history. Then stop this correction round. Do not commission an inference study just to justify the stronger wording.

**SG2 closed in the inspected report's formal disposition:** §1a preserves the original rules and records their collision, §5 does not select a formal winner, subgroup labeled exploratory. The substantive paragraph still overinterprets FAIL as a statistical finding; this is SG1's surviving inference limitation, not grounds to redesign the frozen letter. Missing September 22 vendor bar is an owner-reported coverage defect, not two equally complete measurements of a two-session event. Reproducible calendar/source reconciliation is required before future reuse of the instrument; shelving the study with the limitation disclosed does not require expanding it now. Other historical-label, cluster-calendar and source-data questions remain outside acceptance.

**Recommended operator instructions (not sent):**

1. PROME: produce one short joint brief from existing records on rates repricing versus broader transmission. For each unresolved question name owner, next available observation and what it can decide. Preserve existing September 25 settlement/CBOE/gamma tasks, September 30 position-expiry ownership, and September 28 ORACLE roll. Keep WQ-289/L473 encoding separate and bounded; no new dashboard or audit system.
2. VIOLET: complete the inference wording above, park RQ8 follow-ons, and perform scheduled source/positioning/vol refreshes when due. WQ-259 publication remains conditional on CBOE confirmation.
3. HENRY + BOND: compare policy-path and term-premium evidence on common dates, retaining model and publication lags. State the strongest contrary observation. BOND resolves the existing FR2004 trade/settlement coverage question before using the snapshot to judge auction absorption.
4. LIQUID: at next published observations, determine whether B/CCC widening persists and whether it reaches stronger credit tiers or funding. State the existing quarter-end baseline and distinguishing post-quarter-end observations; no new fitted thresholds. Preserve missing-market coverage.
5. ORACLE + HENRY: if comparing priced hike probabilities, align the event, timestamp and hold/+25/tail assumptions; if infeasible, state the comparison is unavailable. ORACLE confirms correction receipt at RED and prepares the already-due October oil-contract check.

Priority is the joint transmission question and scheduled checks; optional richer research is not authorized by this recommendation. No owner sends/edits/launches/publication. Resume with Will's chosen task; this pass delivers suggested directions only.
