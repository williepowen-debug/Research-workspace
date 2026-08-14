# finding_digit_regex_on_markup_can_match_the_threshold_value

**Found:** 2026-08-14 (BRENT, grading BRT-26 rigs against a frozen 457 line) · **Class:** verification / instrument integrity

## The finding

**A bare digit-regex run against HTML can return your exact threshold value out of markup that contains no data at all — and because the false value EQUALS the number you were watching for, the result looks like the signal rather than like noise.**

Grading a rig-count threshold frozen at **457**, a `grep -oE "45[0-9]"` on the Baker Hughes page (HTTP 200) returned **`457` twice**. Every hit was a Drupal CSS class / UUID fragment:

```
block--8690a9bb-8f5e-457a-934a-62cf4f5795d5
```

**The page carried NO rig counts in its HTML at all** — they live in a linked file. A grep-based grade would have recorded *"rigs at 457 = the frozen line EXACTLY BREACHED"* off a stylesheet identifier.

## Why this is worse than an ordinary bad read

- A wrong number that looks wrong gets caught. **A wrong number that equals your threshold gets BELIEVED**, because it is precisely the outcome the check exists to detect. Confirmation does the rest.
- Hex UUIDs make it likely, not freakish: any 3-digit decimal string appears in random hex/GUID soup at high frequency. **The more markup on the page, the more likely your specific level appears in it.**
- It is silent. No error, no 404, no empty result — a plausible number, in the expected range, from a 200-OK fetch of the correct URL.

## The rule

> **Never grade a numeric threshold off a bare digit-regex against HTML. Anchor to a PARSED FIELD WITH A LABEL, or do not grade.**

A labelled read looks like this — the row *says* what it is, so a stray match cannot impersonate it:

```
Area | Last Count | Count | Change | Date of Prior Count
U.S. | 14 Aug 2026 | 593  | +5     | 07 Aug 2026
```

**Corollary — strip markup before matching, or match structure, never digits alone.** If you must regex, regex the *label and the value together*, not the value.

## Two companions found in the same hour (same source, same session)

1. **A clean HTTP 200 with a large real payload is still not a fresh read.** The same site's linked workbook downloaded at 11.8 MB with 169,320 genuine rows — **every sheet stamped a YEAR stale** (2025-08-29 while grading 2026-08-14). Cousin of `finding_partitioned_source_returns_stale_window_at_200`. **Check the vintage INSIDE the payload; size and status code certify nothing.**
2. **Five outlets agreeing is one source.** Five separate publications carried the prior week's figure verbatim — all one Reuters wire, down to the headline. `n=1`, not five, and not two. **Distinguish RELAY from INDEPENDENCE before claiming corroboration** (`finding_crosscheck_with_free_parameter_validates_nothing`).

## The distinction worth keeping

When the grade was finally made, the oil figure was **still `n=1`** — but from a *distinct lineage* whose **companion total reproduced the primary's labelled table to the unit**. That is materially different from five copies of one wire: one has a cross-checkable anchor, the other has none. **Say which kind of single-source you have; do not round either up to "two witnesses."**
