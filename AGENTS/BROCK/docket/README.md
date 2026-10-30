# BROCK docket — `CATALYSTS.tsv` rules

Declared 2026-10-30 (DAEDALUS profile refresh item 7). The 8-column schema stays as it is (`date, event, what_to_check, threshold_signal, priority, who_cares, notes, date_class`); no reader is re-keyed.

## Row state (no state column; the `event` cell carries it)

| Prefix on `event` | Meaning |
|---|---|
| `✅ CLOSED <date> — <outcome> —` / `✅ GRADED` / `✅ READ` / `✅ PASSED` | Done; the outcome is stated in the prefix. History only. `brock_selfcheck.py` 1b skips these rows. |
| `⚠️ PASSED UNMET` / `⚠️ PASSED — outcome not recorded` | The date passed and the read did not happen, or its result was never written down. Said plainly rather than inferred. |
| `STANDING` | The date is a placeholder for an undated test. |
| no prefix | Live. A row with no prefix and a date before today is a defect: give it an outcome at closeout step 8. |

## `date_class` (what kind of date it is)

| Token | Meaning |
|---|---|
| `hard` | Contractual or statutory date (a deadline, an expiry, a scheduled termination date) |
| `confirmed` | Announced by the issuer or venue and verified |
| `modeled` | Inferred from the issuer's own filing history; not announced |
| `estimated` | A looser estimate (press or analyst), not modelled from filings |
| `window` | A span; the row's date is the start or the modelled centre |
| `soft` | A review or check date set by a desk, not by the world |
| `standing` | An undated standing test |
| `fired` | Legacy (pre-split): the event happened on this date |
| `attempted-unresolved` | A read was attempted and could not resolve (source unavailable) |

New rows use one of these tokens. A new token is added here first.
