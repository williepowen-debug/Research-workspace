# Full state series and chat resolver — latest addendum

November 2, 2026. **Archived draft; not approved, registered or scheduled.** [Earlier code review](COMBINED_PACKAGE_REVIEW.md) · [CSV](base_rate_state_series_thru_20261030.csv) · [Chat code copy](resolver_chat_copy.py) · [Check script](check_state_series.py) · [Results](state_series_checks.json)

## What this closes

The CSV contains all 5,059 observations, September 21, 2006–October 30, 2026, with unique sorted dates and finite values in all four columns. Its final row agrees with the displayed reference values: correlation 0.719338, annualized volatility 0.156135, SPY beta 0.327529 and rate beta −0.062001.

Applying the printed 63-row forward shift to these derived states reproduces the draft's three day-weighted conditional reference forecasts:

| Reference forecast | Exact counts | Reproduced probabilities |
|---|---|---|
| C1, conditioned on correlation <0.863 | 300 persist / 142 calm / 383 stress, of 825 | 36.3636% / 17.2121% / 46.4242% |
| C2, conditioned on beta <0.5 | 17 recoveries of 53 | 32.0755% |
| C3, conditioned on rate beta <−0.03 | 123 negative / 230 near-zero / 134 positive, of 487 | 25.2567% / 47.2279% / 27.5154% |

**The 99% C1 total is now explained as rounding.** Exact frequencies sum to one. The printed proposal still needs to specify which full-precision probabilities its scoring will use; this archival review does not amend or approve it.

The forward construction has 4,996 complete pairs and the last conditioning date is August 3, 2026, so no post-October-30 state is needed. These are overlapping daily observations, not 825 or 487 independent episodes. Episode-weighted tables and every historical claim were not revalidated in this bounded check.

## Code status

The full pasted code is saved as `resolver_chat_copy.py`, with a trailing newline. It parses successfully, and the syntax tree of `stats()` matches the function inspected in the PDF. Therefore the prior two synthetic defect checks apply to this calculation logic too. No operational `--resolve` run was performed.

The saved chat copy's SHA-256 differs from the hash printed in the preregistration. Formatting/blank-line changes can cause this; a mismatch alone does not establish changed logic. It remains a chat-supplied copy, not a byte-verified original frozen file. The source copy has not been repaired or activated.

## What remains missing or unresolved

This CSV contains calculated rolling statistics, **not the underlying ETF prices or Treasury yields**. It supports reproducing the reference probabilities, but cannot independently validate how every state was calculated. The original frozen `prices_adj.csv` (including BKX) and `ust_YYYY.csv` inputs would support that next layer of verification. Their absence does not make this supplied table worthless.

The resolver's incomplete-window and missing-session defects remain, as do interval alignment, fallback/void handling, exact scoring specification and input-snapshot preservation. Historical proxy and dependence caveats remain. The author's forecast probabilities (50/20/30, 35%, 40/35/25) are judgments, distinct from the reproduced historical frequencies. First-session information was already seen; any adoption retains that disclosure.
