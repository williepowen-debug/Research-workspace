# SCRATCH.md template

Every session rewrites `SCRATCH.md` using the structure below. Boot reads SCRATCH first, so the template is optimized for next-session triage in <30 seconds.

**Enforcement rules (also referenced in `CLAUDE.md` § SPAWN PROTOCOL step 14):**
- **PRIORITY-1 must be future-verifiable** — never carry forward event references without checking the date is still in the future.
- **IMMEDIATE items must have dates.** If a date has passed, remove or reclassify.
- **Outbox/inbox summaries: one line per signal** so the next session can triage without reading files.
- **Workbook health:** run `wc -l` and `stat` on TSVs to populate.

---

## Template body (copy verbatim, then fill in)

```markdown
# CARL SCRATCH
**Last session:** YYYY-MM-DD ~HH:MM UTC
**Type:** [brief description of session work]

**PRIORITY-1:** [Single most important thing for the next session. One line.]

---

## WHAT HAPPENED
[Numbered list of what this session accomplished. Keep brief.]

## STATUS CHANGES
| Item | Change |
|------|--------|
[One row per changed value, threshold, or file. Include old→new.]

---

## NEXT SESSION SHOULD

### IMMEDIATE (this session / 24hrs)
[Items with deadlines in the next 24 hours. Max 3-4.]

### UPCOMING (this week)
[Items due this week. Include dates.]

### UPCOMING (next 2 weeks)
[Items due in 2 weeks. Include dates.]

### BACKLOG (no deadline)
[Lower priority items. Keep under 6.]

---

## OUTBOX ([N] signals, awaiting HERMES)
| File | To | Summary |
|------|----|---------|
[One row per outbox signal with one-line summary.]

## INBOX ([N] items, unprocessed)
| File | From | Summary |
|------|------|---------|
[One row per inbox item with one-line summary.]

---

## WORKBOOK HEALTH
| TSV | Rows | Last Modified | Note |
|-----|------|---------------|------|
[One row per workbook TSV. Flag anything >7 days as stale.]

---

## URGENT
[Max 3 bullet points. Only truly time-sensitive items.]
```
