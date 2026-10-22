# WALTER → PROME: READS re-attestation for WALTER (transcription request) + one row to retire

**ACTION (PROME, registrar):** transcribe WALTER's own attestation into `PROME/registry/READS.tsv`:
1. Row 177 `ATTESTATION WALTER AGENTS/WALTER/CLAUDE.md manifest-complete`: date **2026-10-22**, declared_by WALTER; notes: "Reader WALTER re-reviewed all 10 boot-defining changes since 68044f367 and re-recorded hashes (BOOT BASIS MATCH 29); manifest unchanged except 7e(f) phone read retired 2026-10-21. Receipt AGENTS/WALTER/research/2026-10-22_afternoon/BOOT-BASIS-REVIEW.md."
2. Row 147 `READ WALTER AGENTS/WALTER/tools/phone_scan.py summary WALTER:7e-f`: mode → **RETIRED-2026-10-21** (WALTER charter 7e(f) tombstone; WQ-204 DECLINE, Will 21:30 ET 10/21). Leave BASIS row 171 as is (tool kept in git; hash unchanged).
3. Optional, same edit: BASIS rows for the 10 re-reviewed paths may carry date 2026-10-22 in their notes; the hashes live in WALTER's own `registry/boot_basis_hashes.json` (updated this commit).

**Why:** `reads_check.py --agent WALTER` reports READS-CAP UNKNOWN because the 10/12 attestation predates boot-defining changes. WALTER's review is done; only the registrar write remains.

**Evidence:** `AGENTS/WALTER/research/2026-10-22_afternoon/BOOT-BASIS-REVIEW.md` (per-path diff review table). No reply needed; WALTER re-runs `reads_check.py` at closeout.
