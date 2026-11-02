# Combined preregistration package — review addendum

November 2, 2026. **Draft only; no approval, registration or schedule.** [PDF](KRE_prereg_combined.pdf) · [Searchable extraction](combined_pdf_text.txt) · [Earlier review](REVIEW.md) · [Manifest](MANIFEST.json)

## What is new and useful

This 15-page package contains the previously supplied proposal, the printed resolver, two printed base-rate scripts, and selected historical state rows. It is the companion to the prospective proposal, not another completed empirical study. The original standalone resolver is still absent, but its logic can now be inspected. This supersedes the earlier blanket statement that the code was unavailable.

The data section presents month-end observations and daily observations from June through October 2026, rounded to four decimals. The cover explicitly says the full 5,059-row table is in a companion Markdown file that was not supplied. The underlying adjusted-price and Treasury inputs are also absent from this package. Printed code cannot establish the claimed SHA-256 of the original file: PDF layout changes whitespace and line wrapping. No attempt was made to represent a reconstructed script as the hash-verified original.

The historical scripts clarify several points:

- Inputs are truncated at October 30 before shifting the state series forward 63 rows; this removes unresolved forward outcomes at the end of the history. Adjacent conditioning dates still produce overlapping outcomes. Missing rows could make 63 rows differ from 63 exchange sessions.
- The benchmark substitutes **BKX price-index returns** where KBWB returns are missing. That is not an equivalent dividend-adjusted return series, and the fallback is not explicitly restricted to pre-inception dates.
- Episode grouping uses calendar-day approximations: greater than 95 days in one script, greater than 94 days in the other. This is not an exact 63-trading-session gap, and the two definitions can disagree.
- Printed probabilities are rounded to two decimals. This offers a plausible explanation for the 0.99 C1 total, but exact counts/probabilities are still needed for scoring.

## Resolver findings

Two failures were reproduced offline using synthetic inputs and **only the inspected `stats()` function** extracted from the PDF. This is a bounded behavior check, not replication of the historical study or execution of the operational resolver. [Check script](inspect_resolver.py) · [Results](resolver_inspection_checks.json)

| Case | Observed result | Why it matters |
|---|---|---|
| Only 62 supplied return dates | `RESOLVED`, 62 returns | No complete-window requirement in `stats()`. The calling code also lacks a length check after selecting actual dates. An unscheduled closure or incomplete vendor history could therefore produce premature resolution after the fixed calendar date gate. |
| Four different dates missing across two ETFs, two per ETF | `RESOLVED`, 59 returns | `max()` counts the largest per-ticker missing count, not the union of dropped sessions. The written rule requires more than three dropped sessions to be void. |

Additional findings from code inspection:

- Missing prices are filled separately before returns are computed. When one ETF misses a day, its following return spans two days while other ETFs and yield changes still span one. Dropping the first row afterward does not align the remaining intervals.
- The actual-session list comes from the union of downloaded timestamps. A day missing from every series disappears without being counted as missing; an independently established exchange calendar is needed to distinguish this from closure.
- The code flags near-threshold values but does not implement the promised fallback-source cross-check, corporate-action/benchmark-change void checks, or Brier-score calculation. These would require an explicit manual process or additional implementation.
- Only the price CSV representation is hashed in the resolution output. Treasury inputs are neither hashed nor saved there; neither full raw input snapshot is persisted by this script.

These findings are code/protocol discrepancies, not evidence that the earlier 0.719 correlation is wrong. The original matching-window arithmetic remains supported by the existing local checks.

## Disposition

Keep the package: it substantially improves auditability and shows precisely what needs repair. It does not yet make the prospective test ready for use. Obtain the original code and full input/output files, reconcile the missing-data and calendar rules, specify exact scoring benchmarks, and preserve any authorized changes as a new version. Do not silently replace the frozen draft.

The prior concerns about first-session information already seen, small historical samples, and interpreting a KRE-only rate coefficient as bank-wide remain. No proposed probabilities were adopted, and no future run was scheduled.
