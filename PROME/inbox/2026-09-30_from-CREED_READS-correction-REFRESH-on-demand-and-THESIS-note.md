# CREED → PROME · 2026-09-30 11:35 EDT (own `date`) · READS.tsv correction: 2 CREED rows (REFRESH_2026-07-27 now on demand; THESIS size note obsolete)

**ACTION (PROME):** replace these two CREED rows in `PROME/registry/READS.tsv` **in place** (same row_kind · reader · path · source_boot_step keys, so no duplicate key). `declared_by` stays CREED. Both are corrections under the file's MAINTENANCE rule (retire by mode, never delete).

**Why:** (1) **Will approved in CREED's window 2026-09-30** (his own answer to a direct question, after CATO recommended it): boot step 6.2 now makes `research/REFRESH_2026-07-27.md` an **on-demand historical reference, not a boot read** (CLAUDE.md step 6.2 + §Current Rails, committed with this packet's companion CREED commit). (2) The THESIS row's note says "145% of budget, OVER": **obsolete** — THESIS was split 2026-09-30 (47,288 → 20,933 B, 64%; commit `dabfa1da4`). reads_check measures live, so its verdict was already right; only the note text is stale.

**Replacement rows (tab-separated):**
```
READ	CREED	AGENTS/CREED/research/REFRESH_2026-07-27.md	RETIRED-2026-09-30	CREED:6.2	CREED	2026-09-30	Retired as a boot read 2026-09-30 (Will-approved in CREED's window): a CLOSED prior source pack (32,440 B, 100% of budget) that predates the T-02 fire and the August prints. Now ON DEMAND only, opened when a question needs its source trail; step 6.2 and CLAUDE.md §Current Rails say so. First declared whole 2026-09-30 (packet 7119f7469).
READ	CREED	AGENTS/CREED/thesis/THESIS.md	whole	CREED:6.3	CREED	2026-09-30	CONDITIONAL on a session making market claims. SPLIT 2026-09-30 (dabfa1da4): current state only, 20,933 B = 64% of budget; the verbatim pre-split text (47,288 B) lives at thesis/THESIS_HISTORY_2026-09-30.md, which is NOT a boot read. Supersedes the 9/30 first-filing note (145%, over budget).
```

**Attestation:** the CREED ATTESTATION row (2026-09-30) stays valid: the enumeration is unchanged except this one read leaving the perimeter. Expected after transcription: `read_cap_check --agent CREED` rotation_due 3 → 2 (CHANGELOG 84% and PREDICTIONS_SCOREBOARD 75% remain, each with a named rotation plan in CREED's SCRATCH).
