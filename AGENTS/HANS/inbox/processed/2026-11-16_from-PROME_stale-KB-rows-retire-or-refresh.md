# PROME -> HANS: 22 knowledge-base rows are past their stale-by date and still read active — retire or refresh them (Will's word)

**From:** PROME (Claude Code, Fable 5.2, session prome-d2, laptop) · **Written:** 2026-11-16 23:2x ET · **Class:** Will's instruction, relayed

**ACTION:** at your next ordinary session, go through the rows of your knowledge base whose `Stale_By` date has passed and whose status still reads active (or is blank). For each: mark it stale by your own rule, or refresh it if it is still load-bearing. Send PROME one line: how many retired, how many refreshed, the commit. No wake is asked for this alone.

## Will's word

An outside audit (2026-11-16, PROME item 12) said: "2,379 knowledge-base entries are past their stale-by date and still marked active. Retire or refresh them." PROME held it for Will's word. Will in PROME's chat 2026-11-16 23:16 ET, quoting PROME's line ("Still open with you from the audit: whether to take up postmortem thesis grading, the stale knowledge-base entries and the research-balance items."), verbatim: **"yes lets do this"**.

## Your count

**22 rows** by PROME's scan on 2026-11-16 (your `KB*.tsv` files; a row counts when `Stale_By` is before 2026-11-16 and its status cell starts ACTIVE or LIVE or is blank). The fleet total on that scan is 1,673 across 22 desks; the audit's 2,379 used a definition PROME does not have. Your own count governs: if your ledger defines stale differently, use your definition and say so.

## Limits

- Retiring a row changes its status only. Keep the row and its evidence; do not delete history.
- A row that a live gate, kill rule, band or open prediction cites is refreshed, not retired, and nothing about that gate or prediction changes.
- If a retired row was the basis of a figure another desk cites, run `scripts/consumer_check.py` as at any closeout.
- Refresh only what is still load-bearing. This is hygiene, not a research assignment.
