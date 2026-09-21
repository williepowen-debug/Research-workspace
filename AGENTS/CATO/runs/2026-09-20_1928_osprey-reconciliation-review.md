# OSPREY reconciliation review — 2026-09-20 19:28 ET

**Disposition: stronger evidence of production transmission; reconciliation and upgrade recommendation not yet decision-ready.** Review requested by Will after OSPREY reported all four residuals fixed and reconciliation complete. Owner commit: `a93d02b547ea25819536712bc739e1b80c8f2b4b`; initial shared HEAD: `cfd9b91159c4f2d484edc24462ec12ff1c4784be`. No live OSPREY differences from the reviewed commit when checked. Prior CATO receipt: [128a90879 report](2026-09-20_1850_osprey-correction-receipt.md).

Scope: inspect the four-file owner change, surviving consumer claims, cited source families and the existing upgrade wording. Independent review of OSPREY's work; author follow-up to CATO's own earlier findings. No OSPREY edits, score changes, messages, launches or trade proposals. Shared CONTINUITY and other sessions' SAM/CRUISE/PROME/memory changes preserved. This report supplies the separate resume point. The claimed transient push race/no-autostash history was not independently reconstructed; presence on origin can be verified without certifying that operational narrative.

## What improved

STATUS now explicitly withdraws CATO's supposed concurrence and identifies holding the marks as OSPREY's judgment. Its September count is corrected to ten exact-refinery records. SCRATCH's prominent unit-damage warning now distinguishes unverified reporting from proven vintage contamination. The reconciliation table usefully separates measurement families, retains the July basis discrepancy and admits no post-September-15 observation. Its residual section correctly retains both matcher precision and evidence retention, though the response to Will mentions only retention.

## Findings

### 1 — High: a forecast is presented as measured corroboration

`RECONCILIATION_2026-09-20.md:10,24` and KB-146 call a September-10 Bloomberg/Rystad figure an independent processing decline for August/early September. The accessible September-10 [Bloomberg wire syndicated by Rigzone](https://www.rigzone.com/news/wire/russias_crude_output_fell_in_august-10-sep-2026-184586-article/) reports August production and strike-related constraints, but contains neither Rystad nor the claimed 30% processing observation. A [Moscow Times September-10 relay](https://ru.themoscowtimes.com/2026/09/10/rossiya-stolknulas-sobvalnim-padeniem-dobichi-nefti-posle-ukrainskih-udarov-ponpz-a205803) contains that combination; it is not itself the named primary.

[Rystad's own publication](https://www.rystadenergy.com/news/russia-crude-production-constraint) instead gives a July–December throughput **forecast** around 4 M bpd, compared with a 2016–2023 seasonal norm around 5.7 M bpd. Its page metadata says published August 14, modified September 8. It explicitly supports attacks constraining upstream production and limited ability to absorb surplus crude, but does not establish the owner table's measured August/early-September runs decline. It also discusses sanctions, export constraints and ageing wells. The numerical resemblance supports an outlook comparison, not measurement validation. If another primary supplies a realized 30% figure, identify its exact passage and observation period. Until then, withdraw “independently corroborated” as a measured-band claim.

### 2 — High: identifying different measures does not reconcile their values

`RECONCILIATION:19–24` claims the gap is resolved because utilization was below 100% and surviving units run harder. CATO previously established non-comparability, not that these explanations had quantitatively reconciled the figures. The report supplies neither observed utilization nor a matched-period capacity/run balance.

**Conditional arithmetic using OSPREY's own rounded assumptions**, not a replacement estimate: 7 M bpd nameplate with 50% unavailable leaves 3.5 M bpd. A 30% decline from 5.5 leaves 3.85 M bpd. Treating both as the same universe and time requires 110% of remaining nameplate. Subtracting IIR's 3.805 from 7 leaves 3.195, implying about 120.5% utilization to process 3.85. Nameplate is not an inviolable engineering ceiling; scope, timing, rounding and above-nameplate operation may matter. Those are precisely the missing reconciliation inputs. Merely noting baseline utilization below 100% does not close the gap.

[IIR](https://www.industrialinfo.com/news/article/unplanned-outages-at-17-russian-refineries-average-38-million-bpd-offline-in-august-2026--362113) reports average unplanned crude/condensate outages and warns August may be revised upward as confirmations arrive. Its lower initial August estimate versus July is not proof that final August impairment eased. [S&P](https://www.spglobal.com/energy/en/news-research/latest-news/refined-products/090326-russian-august-crude-exports-fall-on-month-amid-black-sea-attacks) reports nearly half of capacity offline at end-August. Point-in-time and monthly-average estimates cannot be directly subtracted from an unmatched forecast. Mark the quantitative reconciliation OPEN, with definitions separated. Neither worsening nor stability follows from their numerical difference alone.

### 3 — High: the trigger gains a runs-only qualifier without a governing citation

`thesis/THESIS.md:38` says **“sustained runs <3 M bpd or an independent >40% offline aggregate.”** The new reconciliation rejects capacity-offline evidence because the band's basis is runs; the response to Will rewrites the second limb as a runs-based aggregate. Those are different propositions. A proxy used for the band does not silently redefine the separate upgrade test. Earlier `ANALYSIS_2026-07-12.md:31` explicitly linked a capacity-offline aggregate above 40% to the upgrade, reinforcing the need to identify any later authorized change.

The S&P estimate therefore merits explicit eligibility adjudication against the existing wording; it cannot be dismissed solely because it is capacity-based. Source tier, observation age and methodology remain relevant. This is **not** CATO certifying a fired trigger or ordering an upgrade. `CLAUDE.md` §1b still reserves upgrades to Will. Ask him to decide from the rule actually in force, or clearly label a proposed rule change/discretionary override.

The suggested future alternatives also need correction: a September print merely confirming current impairment would not necessarily cross either threshold; a Moscow processing halt alone is not the national trigger. An already-idle plant also cannot lose operating throughput again without an intervening restart. “Close to 5” is a judgment, not a demonstrated distance to the written thresholds.

### 4 — Medium: quota shortfall does not prove involuntariness or isolate strikes

The Bloomberg wire supports the reported shortfall and describes attacks disrupting refining and exports. That is evidence for the transmission mechanism. But `RECONCILIATION:27` says policy compliance would place production at/above quota. A quota shortfall alone does not identify its cause, and “above” is not the definition of compliance. [OPEC's August-2 release](https://www.opec.org/pr-detail/611-2-august-2026.html) also retains voluntary adjustments and compensation for prior overproduction. The relevant adjusted target and other causes must be checked before using the raw gap as causal proof.

Do not reverse the correction to the original reassurance: direct reporting now supports strike-related upstream constraints. Keep that source-attributed conclusion while withdrawing the invalid quota syllogism. Neither the quota gap nor the approximately 1.7 M bpd processing imbalance is a measured strike-attributable production loss; exports, inventory changes and other drivers intervene. “Primarily strikes” as an exact attribution was not established in the primaries inspected here.

### 5 — Medium: “all four residuals fixed” is not supported by the artifacts

The commit changed STATUS, one SCRATCH passage, the new reconciliation and KB-146. It did not change NEXUS_BRIEF. Current SCRATCH still reports September eleven (`:21`), still labels the Moscow halt the only route to a mark/band move (`:27`), and still credits a fourth recall success (`:35`). NEXUS still carries the suspected-vintage opening and handoff (`:7,:21`) and recall-pass claim (`:70`). STATUS now says reconciliation run (`:17`) while its dashboard and OWED-50 still say reconciliation owed/not reread (`:22,:71`). These current instructions are not consistently marked superseded. No feed repair was made. Correcting the prominent sentence is progress, not complete propagation.

## Acceptance conditions and resume

Before presenting the upgrade/hold choice, OSPREY should: (1) replace the conflated source entry with precise primary links and observed-versus-forecast labels; (2) either provide a matched-basis quantitative bridge or leave reconciliation open; (3) adjudicate the >40% limb without importing an uncited runs-only restriction; (4) remove quota-based causal certainty; (5) propagate the disposition across current startup and consumer summaries. Retain the production-risk finding at its supported strength. This is a bounded correction request recommendation, not permission to launch more work or alter policy.

Verification: owner commit/diff inspection; targeted current-text comparisons; direct web reads of Rystad, Bloomberg syndication, IIR, S&P and OPEC; Rystad HTML metadata fetched read-only after sandbox DNS failure; conditional arithmetic reproduced below. Proprietary source datasets, historical versions of Rystad's page, adjusted Russian quota schedule and OSPREY's push-retry execution were not audited. Weekday checks passed on this report and three shared task records. The orphan advisory identified another session's memory edit, preserved. Push receipt delivered in-session.

Arithmetic: `5.5*(1-.30)=3.85`; `7*(1-.50)=3.5`; `3.85/3.5=1.10`; `7-3.805=3.195`; `3.85/3.195=1.2050`. These expose required assumptions, not prove the source estimates false.

**Resume:** review delivered; await Will or an OSPREY correction receipt, rechecking owner revision first. No further research, owner repairs or score adjudication is assigned. This session authors only this report; other CATO work remains separate.
