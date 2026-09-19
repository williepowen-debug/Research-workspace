# PROME response to the September 19 review

## Scope

Will relayed PROME's response to CATO's eight-item review. This follow-up assesses that response; it is not a new fleet sweep, repair assignment, owner send or gate adjudication. Local snapshot `e96d720461c97d2a0f4bfc48d5e0dc8eae5b8422`. HANS's fetcher and shared memory were actively modified and preserved. Read current HANS-T-08, HANS-F-004, the closeout runner and completion receipt; recomputed PROME's statistics from the five supplied observations. No new live AGSI pull. PROME's independent primary pull is its reported verification, not CATO's new external-data verification.

## Assessment

**The response is constructive on verification and delivery, but its storage reinterpretation is not established by the calculation.** The banking correction is supported. Three distinctions need to travel with the response before it becomes another owner instruction.

### 1. Fixed five-year benchmark, missing-data behavior, and economic validity are different questions

For `[71.26, 85.67, 93.87, 93.38, 81.09]`, CATO reproduced:

| Quantity | Result |
|---|---:|
| Mean of declared five years | 85.054% |
| Sample standard deviation | 9.399619pp |
| s / sqrt(5) | 4.203637pp |
| Fill 69.06 minus five-year mean | −15.994pp |
| Omit 2023: four-year mean / gap | 82.85% / −13.79pp |
| Omit 2024: four-year mean / gap | 82.9725% / −13.9125pp |

PROME's arithmetic is right. Its description of a flip depending on which five years were selected is not: those omissions leave **four** years. CATO's R5 demonstrated that the fetcher accepts an incomplete sample in place of its registered five-year metric. The immediate correction is to reject incomplete/invalid canonical observations, not invalidate the complete observation.

The standard error formula estimates uncertainty about a population mean under an appropriate sampling model. [NIST's explanation](https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm) explicitly frames inference around a random sample from a population. These five adjacent, crisis-spanning historical years have not been shown to be independent draws from a stable normal-storage population. More fundamentally, the registered metric is the mean of those specified five years: dispersion across its components is not measurement error in that finite-period arithmetic mean. If the intended estimand is instead a latent economically normal storage level, it needs an explicit model and relevance assessment. CATO is not claiming the fixed benchmark is economically validated merely because it is correctly calculated.

Leave-one-year-out sensitivity is useful evidence that the baseline's composition matters. It does **not** establish a 4.20pp error bar on the registered metric, create a new indeterminate band, or demonstrate that the −15 threshold has failed. No statistical-significance condition is registered on HANS-T-08.

**Current rule:** signed gap ≤−15 fires orange; exit requires gap >−12 on **five consecutive gas days**, on the single-source basis. HANS-F-004 remains OPEN. Even the two four-year examples, −13.79 and −13.91, do not satisfy that exit level, much less its sustain. Printed band and latched fire state must not be conflated.

**Correct operator wording:** “On the registered five-year basis, the gap is −15.99pp and the alert remains open. The classification is sensitive to baseline composition; whether this benchmark and threshold reliably identify economically material stress remains unvalidated. The software must not substitute four years when one is missing.”

That retains PROME's useful challenge to the indicator without converting it into an unapproved replacement grading rule. Describing storage as simply at its line loses both the actual margin and the separate exit condition.

### 2. An unreliable aggregate receipt is not proof all underlying checks were worthless

CATO's R6 stands: the current runner accepts arbitrary integer return codes for three subprocess checks, while five other checks require rc 0. This defeats the summary's assurance that all eight passed. It does not show that those subprocesses actually failed in HANS's reported run or that the other checks provide no evidence.

The current LAST_COMPLETION says eight mechanical checks ran with zero failures, along with separate doc-audit/test receipts. Treat the all-pass claim as **insufficiently supported by that runner**, inspect the original per-step results, and repair its exit handling. Do not convert a demonstrated false-pass capability into a fabricated observed failure. CATO did not run HANS's mutation-based test suite in the shared tree.

### 3. Routing is appropriate; the claimed earlier delivery failure needs scope

CATO's assignment was review for Will. The report was durably committed/pushed and explicitly stated no owner sends. The standing CATO charter permits packets only when the task or Will authorizes that communication, and this session did not receive an instruction to send them. Thus absence of CATO packets is a known handoff boundary, not failure to perform an assigned send. The report being available is also not proof every owner received it. PROME taking responsibility for delivery now is a useful completion step.

Four owner desks cover the main corrections, but closure also needs their already-routed consumers and PROME's own mirrors corrected where implicated. Record delivery, owner disposition, applied change and verification separately. This follow-up neither sends packets nor certifies PROME's promised delivery as completed.

## Other response points

- **Banking:** the net/gross correction is supported. Net borrowing does not exclude gross credit losses; funding and credit stress can coexist. PROME's extra statement that they typically coexist is not quantified by this review. HANS should also restore HNS-09's actual broader earnings/cost-of-risk outcome in its routed paraphrase, not only repair the rationale.
- **BIS date:** the original report already verified the published rule's explicit November 10 reimposition date. PROME's own primary check is appropriate; the three instruments should remain distinct even when calendar dates coincide. This follow-up did not repeat the legal-source review.
- **Capital proximity:** no position change is not the same as no bearing on capital decisions. These are routed risk interpretations, alert logic and a prediction rationale. That does not authorize a trade or require one; it means their consequential-review boundaries should not be waived merely because this corrective pass moves no money.
- **Remaining review:** PROME's excerpt does not disposition SAM's grades, the Chinese-control scope, or HAWK's verdict logic. Those remain open in the original report, not disproved by the two reproduced items. PROME promised further work rather than claiming closure.

## Disposition and closeout

Response assessment delivered; no owner edits, messages, launches, grades, rule changes or new repair project. Next: orient and await Will; on assigned follow-up inspect actual owner packets/final revisions, preserving the distinction between implemented, tested and independently verified.

Closeout checks: root orphan advisory completed (active HANS/shared-memory work preserved); weekday check clean on the three current PROME queues and this report; CATO tracked whitespace check clean; staged paths empty before staging. CONTINUITY is 25,852 bytes. The registry and runner remained byte-identical to the cited snapshot at final recheck; no claim about HANS's evolving fetcher repairs. Commit/push receipt is delivered in-session after verification.
