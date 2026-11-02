# Prospective evaluation draft — PROME review

**Latest evidence:** [full state-series and chat-code addendum](STATE_SERIES_REVIEW.md) supplies the complete derived table, reproduces the conditional reference frequencies and explains the C1 rounding total. Missing-file statements below describe the earlier intake.

Reviewed November 2, 2026. **Archived proposal only: not approved, registered, scheduled or activated.** [Original draft](PREREGISTRATION.md) · [Provenance](MANIFEST.json) · [Collection guide](../../EVIDENCE_GUIDE.md)

**Later same-day addendum:** the [combined PDF review](COMBINED_PACKAGE_REVIEW.md) now inspects printed code and selected historical rows. References below to missing code describe the initial upload; exact standalone files and full data remain absent. Two resolver defects were reproduced on synthetic inputs.

## What this adds

The earlier studies ask what happened. This proposal asks what observations over the next quarter would support or weaken persistence of the unusual behavior. That is useful discipline, but it supplies no new completed-window result and no validated investment forecast.

It separates three questions:

| Test | Plain-English meaning | Draft forecast, not a verified probability |
|---|---|---|
| C1: KRE–KBWB correlation and KRE volatility | Does the unusual separation persist, or do the banks reconnect in calm or volatile conditions? | 50% persistence; 20% calm normalization; 30% stress normalization |
| C2: KRE beta to SPY | Does KRE regain more of its usual sensitivity to the broad stock market? | 35% probability beta reaches 0.80 |
| C3: KRE response to Treasury yields, controlling for SPY | Does KRE continue tending to benefit when yields fall? | 40% negative; 35% near zero; 25% positive rate beta |

These are statements about relationships, not predictions that KRE will rise or fall. Relative returns are appropriately kept separate from the scored claims. One evaluation window cannot establish forecast skill or causality; nonoverlapping windows are not automatically statistically independent.

## Checked here

The scheduled 63-session window is November 2, 2026–February 2, 2027. Session 21 is December 1 and session 42 is December 31. Counting weekdays with the stated holidays reproduces these dates; the [official NYSE calendar](https://www.nyse.com/trade/hours-calendars) confirms the scheduled holidays and early closes. Unscheduled closures could change the end date.

The C1 comparison forecast sums to **0.99**, not 1: 0.36 + 0.17 + 0.46. This may be display rounding, but the scoring rule needs exact probabilities or an explicitly agreed normalization rule.

The named `resolver.py` was not supplied beside these uploads. Its printed hash is an assertion, not a verified executable. Reference-window replication, historical probabilities and episode counts therefore remain reported-only.

## Repairs needed before operational adoption

1. **Preserve the late-registration disclosure.** The author saw November 2 prices before drafting. Will and PROME also discussed November 2 prices. This window cannot be described as an untouched prospective preregistration. Any later adoption needs an actual dated approval and that disclosure. Selecting an untouched future window would be a separate revision, not a silent correction.
2. **Supply the exact resolver and its inputs.** Preserve the code, input snapshots, historical outcomes, episode membership/weighting and full-precision benchmark probabilities. Verify its hash and reproduce the reference calculation. Historical forward windows must end by the information cutoff; this needs an explicit rule. Pre-KBWB history uses BKX: a reported 0.995 daily overlap correlation does not validate tail classifications, total-return comparability or the splice.
3. **Resolve the missing-data contradiction.** The draft promises exactly 63 daily returns but allows dropped sessions followed by multi-day returns. That changes sample size and the meaning of daily volatility annualized by sqrt(252). Specify how all regressors, particularly yield changes, align across gaps; define missing-yield and degenerate-sample behavior. Do not silently implement a preferred repair.
4. **Fix scoring precision.** Obtain the full-precision C1 benchmark or approve a deterministic normalization. Preserve the supplied source unchanged; report both the correction and its effect if the protocol later changes.
5. **Narrow interpretation.** C3 measures KRE alone; a negative KRE coefficient does not establish that a bank-wide regime persists. That needs a comparable bank benchmark. Correlations can rise with common volatility, but stress normalization does not mechanically prove either causal story. Small samples, overlapping historical outcomes and selected thresholds keep the proposed probabilities uncertain.

## Relationship to the accompanying PDF

[REPORT.pdf](../2026-11-02_kre-study3-review/REPORT.pdf) is the earlier Study 3 rate-analysis presentation, with embedded regime-map and rolling-beta figures. It is useful for preserving the visuals, not a new empirical study. Its existing review and caveats still apply.

This draft's `PREREGISTRATION.md` is **different from** Study 3's [PREREGISTERED_SPEC.md](../2026-11-02_kre-study3-review/PREREGISTERED_SPEC.md). Do not substitute one for the other or infer approval from either filename.
