# WAL — Charter reference (read on demand)

Moved VERBATIM from `CLAUDE.md` on 2026-11-16 (WAL, PROME prome-6f wake; DOCKET L810 charter hot/cold split, READ_CAP rule 5). Nothing reworded in the move; sha256 of the moved text = `e47b54e6919a66511c34da45dfb1677ef8e924e18eef5c26e0c412f26424428b`. Two DAEDALUS WQ-678 Changelist B corrections (C13: stale "v2.4" tokens dropped; C20: stale "awaiting the 10-Q" parenthetical dropped) and the PREDICTIONS row list (WAL-01 to WAL-07) were applied in `CLAUDE.md` immediately BEFORE the move, in the same commit. The charter keeps a one-line pointer to each section. No authority, route or threshold moved.

---

## DOC OWNERSHIP (no duplication)

| Doc | Owns | Does NOT contain |
|-----|------|------------------|
| **STATUS.md** | Price, thesis-state line, convergence matrix, exit rules, catalysts, expected signals, print snapshots. Dashboard. | Deep research (→ FRAUD/, research/, sources/), thesis rationale (→ THESIS), session history (→ MEMORY) |
| **THESIS.md** | Structural thesis, scenario weights, calibration tables, kill criteria. Slow-moving. | Daily updates |
| **CHANGELOG.md** | Thesis evolution, version-pinned, old-vs-new + why. | Current state |
| **SCENARIOS.md** | Current valuation block and scenario ranges; prior lineage/May strike analysis linked to a verbatim archive. Any option rebuild is separately scoped. | Probability weights (→ THESIS) |
| **WEAKNESSES.md** | Living counter-argument — where the bear case fails. | Confirmatory evidence (→ THESIS + KB) |
| **INDEX.md** | Cold-spawn entry point — file map + current-state tokens (MIRRORS canonical; sync at closeout). | Canonical values (it mirrors, never originates) |
| **POSITIONS.md** | WAL option legs from broker data (canonical post-split). | Trade rationale, price levels |
| **FRAUD/** | The WAL-lensed fraud corpus — LAM/Jefferies litigation, Cantor residual, auditor nexus. Q1-cycle records bannered as records. | Cross-agent fraud ecosystem (→ OTTO First Brands, shared JEF node → `FORGE/research/jefferies/`) |
| **Q2_GRADING_FRAME / PREPRINT_RECON / EARNINGS_PREP** | 🧊 FROZEN pre-registration + calibration records. Path fixes only, content NEVER. | — |
| **Q3_PRINT_GRADING_FRAME / Q3_10Q_GRADING_FRAME** (2026-09-24) | Pre-registered Q3 grades. **Until each filing lands: only dated annotations in their final section. After: graded verbatim, never edited.** | — |
| **Q3_10Q_RESCORE_RULE** (2026-10-22, Will-approved 12:37 ET) | Pre-registered mapping from each 10-Q outcome to the Bear-medium/Tail weights. Amendable only by dated note before the 10-Q hits EDGAR; then applied verbatim in a versioned THESIS/SCENARIOS/CHANGELOG edit. | Weights themselves (→ THESIS/SCENARIOS) |
| **workbook/KB.tsv + KB_INDEX.md** | Evidence rows (KB-WAL-xxx), cluster rollups. Two-clock header. | — |
| **workbook/PREDICTIONS.tsv** | WAL-01, WAL-02, **REG-15** (transferred in from REGINALD 8/12, scored 8/20) + all future WAL predictions. Dual-provenance notes preserved. Two-clock header. | — |
| **MEMORY.md** | Session handoff, Feedback, Findings, first-boot mandates. | STATUS recaps |
| **REGINALD_CHANNEL.md** | Pair log with REGINALD (ACK discipline, ~300-line archive rule). | Signals for other agents (→ the recipient's `inbox/`) |
| **NEXUS_BRIEF.md** | Synthesis brief for NEXUS (schema R3 + amendment 7). | — |

---

## FILES

| File / Dir | Purpose |
|------|---------|
| `INDEX.md` | Cold-spawn entry point — mirrors canonical tokens. |
| `STATUS.md` | Live dashboard (≤250 ln). Primary snapshot. |
| `THESIS.md` + `CHANGELOG.md` | Current thesis + version-pinned history. *(De-versioned 8/20: a version token mirrored here rots on every bump — THESIS.md owns its own version.)* |
| `SCENARIOS.md` | Current valuation/range block; historical strike analysis is linked in its verbatim archive, not current holdings guidance. |
| `WEAKNESSES.md` | Living counter-argument — **must be re-folded at every thesis bump** (it went a full version stale after v2.4 and asserted an already-run falsifier was "never-run"). |
| `POSITIONS.md` | WAL option legs (canonical). **This desk's only trade surface — there is no TRADE.md.** |
| `Q2_GRADING_FRAME_2026-07-21.md`, `PREPRINT_RECON_2026-07-17.md`, `EARNINGS_PREP.md` | 🧊 Frozen pre-registration/calibration records. |
| `Q3_PRINT_GRADING_FRAME_2026-09-24.md` · `Q3_10Q_GRADING_FRAME_2026-09-24.md` | ★ Pre-registered Q3 frames. |
| `Q3_10Q_RESCORE_RULE_2026-10-22.md` | ★ Will-approved pre-registered weight mapping for the post-10-Q re-score. |
| `Q2_10Q_READ_2026-08-07.md` · `MI3_FIRST_RUN_2026-08-07.md` | Q2 10-Q primary read (+ its §6 NOT-resolved list) · the first MI3 falsifier run. |
| `LEADERSHIP.md` · `Q1_2026_ANALYSIS.md` | Insider/leadership record (refreshed 10/28; THESIS travels it) · Q1 8-K mining (held from retirement: THESIS travels it). |
| `FRAUD/` | WAL-lensed fraud corpus. **Live homes (9/24): `FIRST_BRANDS.md` §FOLD (LAM/Jefferies + collateral-perfection screen) and `STUPIN_CRE.md` §FOLD (Cantor).** The rest are bannered records. |
| `MARKET/` | TRADE_LOG only, bannered (phantom-strike residue); 3/25 charts → `archive/MARKET/`. |
| `workbook/` | `KB.tsv` + `KB_INDEX.md` + `PREDICTIONS.tsv` (**WAL-01 to WAL-07, REG-15**) + `RETIRED_CLAIMS.tsv` + `MI3_SERIES.tsv`. *(Row/group counts de-listed 9/24 — they rotted here at "180 / 16"; INDEX.md mirrors the live count.)* |
| `sources/` | Primary extracts; `q*/` + `10k_*/` binaries gitignored, `.md` synthesis tracked. |
| `research/` | WAL-specific research threads (incl. 9/24: catalyst sweep, FRAUD corpus review, Q2 13F aggregate). |
| `STATUS_ARCHIVE.md` · `MEMORY_ARCHIVE.md` · `archive/` (+ `archive/FRAUD/`) | Verbatim, crc-stamped rotations (COLD, citable with their dates) · retired files with banners (sweep records inside). |
| `board_log.tsv` · `registry/corrections_receipts.tsv` | WALTER signal consumption receipts (boot 7b) · R1 correction receipts (boot 7a). |
| `scripts/kb_expiry_check.py` | Reads KB's `Stale_By` column (nothing did before 8/20). Boot step 4b, advisory, exit 0. |
| `scripts/predictions_due_check.py` | Reads PREDICTIONS' `Resolve_By`. Boot step 4d. |
| `scripts/boot.py` + `test_boot.py` | Boot step 5 (10/28), read-only. |
| `scripts/market_tracker.py` + `workbook/MARKET_TRACKER.tsv` | Short interest (% of shares), price snapshot, realized vol, beta vs KRE, spot vs EV (10/30, Will). Dry run by default; `--write` appends only new readings; boot step 5 flags when due. |
| `scripts/derived_drift_check.py` + `workbook/RETIRED_CLAIMS.tsv` | Catches derived surfaces still asserting pre-bump state. Boot step 4c. **Add a RETIRED_CLAIMS row whenever you kill a claim.** |
| `scripts/maintenance_state_check.py` + `scripts/test_maintenance_state_check.py` | Named current-field checks (KB/INDEX/KB_INDEX counts, position mirrors, inbox lanes) run inside 4c; `python3 -m unittest test_maintenance_state_check` from `scripts/` (10/10 on 10/22). Fixtures must read live values, not hard-coded counts. |
| `MEMORY.md` | Session handoff + first-boot mandates. |
| `NEXUS_BRIEF.md` | NEXUS synthesis brief. |
| `REGINALD_CHANNEL.md` | Pair log with REGINALD. |
| `inbox/` · `outbox/` | Signals in (+ `processed/`) · optional sender copies out (+ `delivered/`). |
