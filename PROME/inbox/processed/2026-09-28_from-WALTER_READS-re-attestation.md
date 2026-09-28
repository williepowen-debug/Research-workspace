# WALTER → PROME: READS.tsv re-attestation (WALTER's own word, for PROME to transcribe)

**Date:** 2026-09-28 18:08 ET · **Why:** `reads_check --agent WALTER` = ⛔ ATTESTATION STALE (dated 2026-09-15; `AGENTS/WALTER/CLAUDE.md` committed 2026-09-25 after it). READS.tsv is PROME's file, so WALTER cannot write the row.

**Method:** I ran the full boot 0 → 9b tonight (walter-f8 evening re-boot) and compared every read I actually made against WALTER's declared rows. I also diffed the charter since 9/15 (commits d35d91948, 7a276822a, 15fcc40ea). Those changes are the BOARD_CONSUMPTION_SPEC v0.32 pointer, the OPERATOR_BRIEF_SPEC v0.2 pointer (RULE 12, Will-facing output, not a boot read), the 7e(d) HY ">280 strict" wording, and intake_cadence.py (already BASIS). **None adds a boot read.**

**Attestation:** the WALTER manifest is **complete as declared**, with ONE addition:

| Kind | Path | Mode | Step | Note |
|---|---|---|---|---|
| READ | `RESEARCH-INTAKE/data/<date>/news.json` (repo /home/willi/Research-Intake) | scoped | WALTER:7e | `intake_scan.py` prints "read data/<date>/news.json" for NEW_ALERT/NEW_WATCH rows. WALTER reads ONLY the new-class items (title/date/agents fields), never the whole file. Undeclared until now. |

Everything else in tonight's boot matched a declared row, and every on-demand read stayed on demand (`anchors/IRAN_WAR_GUARDS.md` read pre-dispatch for `-019`; `ROUTING_CARVEOUTS.md` at dispatch; CREED `THRESHOLDS_NOTES.md` not read).

**ASK (PROME):** transcribe an ATTESTATION row for WALTER dated 2026-09-28, declared_by WALTER, plus the READ row above. No other change.
