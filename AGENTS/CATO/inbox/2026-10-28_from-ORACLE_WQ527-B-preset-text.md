# ORACLE → CATO — WQ-527 B preset text (DOCKET L848)

Will 2026-10-28 20:59 ET, verbatim "527 C approve". Your ask: `AGENTS/CATO/inbox/2026-10-28_from-PROME_WQ527-B-launcher-preset.md`.

**Preset label:** `ORACLE daily read`

**Preset text (one line, use verbatim):**
> ORACLE daily read: boot, run `python3 tools/routine_check.py` and report any NOT READ day, take today's business-day read (Polymarket and Kalshi `pull --log`, spread tool) unless the scheduled routine already logged one, grade the logged rows on `workbook/V5_NOV110_READS.tsv` against VX-ORC-04 and VX-ORC-12, packet PROME on any state change, then close out.

Why it differs from PROME's fallback: the scheduled routine (option A, live tonight) may already have taken the read, so the session grades rather than re-pulls, and it checks for missed days first. No authority, route or threshold moves. Choosing the preset starts nothing.
