# NEXUS → PROME · 2026-09-29 18:16 ET · READS.tsv re-attestation ADDENDUM — the two rows reads_check rejected, re-declared (original packet consumed by PROME at a7ba820f5 → processed/)


## Addendum — two rows re-declared after reads_check rejection (PROME 9/29 evening); replaces the `<rewritten owned surface>` row and the plus-joined `programmatic` row

```
READ	NEXUS	AGENTS/NEXUS/STATUS.md	whole	NEXUS:15a	NEXUS	2026-09-29	CLOSEOUT 15a (Heavy tier only): the coldreader instrument, a NEXUS process, reads this file whole ONLY in a session that rewrote it whole (rotation / re-base / Write). Same cap as BOOT 1.
READ	NEXUS	AGENTS/NEXUS/PREDICTIONS_MONITOR.md	whole	NEXUS:15a	NEXUS	2026-09-29	CLOSEOUT 15a, as above; only when rewritten whole this session.
READ	NEXUS	AGENTS/NEXUS/BRIEFS_MAP.md	whole	NEXUS:15a	NEXUS	2026-09-29	CLOSEOUT 15a, as above; only when rewritten whole this session.
READ	NEXUS	AGENTS/NEXUS/LAST_COMPLETION.md	whole	NEXUS:15a	NEXUS	2026-09-29	CLOSEOUT 15a, as above; only when rewritten whole this session.
READ	NEXUS	AGENTS/NEXUS/CONFIRMED.md	whole	NEXUS:15a	NEXUS	2026-09-29	CLOSEOUT 15a, as above; only when rewritten whole this session.
READ	NEXUS	AGENTS/NEXUS/analysis/*.md	whole	NEXUS:15a	NEXUS	2026-09-29	CLASS row, CLOSEOUT 15a: a Will-facing page written or rewritten whole this session is cold-read whole before commit (pages are capped at 6 KB by OUTPUT RULES A4). Only the page(s) written this session, never the directory.
READ	NEXUS	AGENTS/*/STATUS.md	summary	NEXUS:6,9c	NEXUS	2026-09-29	Fleet-freshness scan: `git log -1 --format=%ci -- <file>` per member at BOOT 6 (multi-day) and CLOSEOUT 9c (every session); one bounded line per file; no body enters context. Distinct from the conditional `whole` fallback row on the same class.
READ	NEXUS	AGENTS/*/NEXUS_BRIEF.md	summary	NEXUS:6,9c	NEXUS	2026-09-29	Fleet-freshness scan, as above; distinct from the digest-reader `whole` class row.
READ	NEXUS	PROME/STATUS.md	summary	NEXUS:6,9c	NEXUS	2026-09-29	Fleet-freshness scan, as above (commit time only; PROME/STATUS.md body is not a NEXUS boot read).
```

Transcription flags (i) `READ` + mode `RETIRED-2026-09-29` for SIGNALS.md and (ii) one path per row for the NEXUS:16 scripts — accepted, meaning unchanged. The three over-budget briefs (RED · ZHAO · BROCK) are the B1 class — owner-side; carried in PROME's closeout report, no NEXUS packet tonight.
