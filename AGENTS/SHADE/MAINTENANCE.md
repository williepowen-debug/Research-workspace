# SHADE MAINTENANCE LOG

Structural-change log for SHADE architecture: docs/scripts/protocol/schema changes. Analytical changes belong in `STATUS.md` or research files.

---

### 2026-06-26 — Tier-1 fleet fixes applied (T1a/T1b/T1c)
- **Trigger:** Will-directed fleet architecture review; Prome Tier-1 fixes mandated across all agents.
- **T1a — Stale-ledger fix:** Added `LAST_REVIEWED` field to all 8 `domain/sources/` KB doc headers (Mar'26 vintage; flagged as ⚠️ >60d stale). Added KB staleness warning to STATUS §0. Note: KB-07 (FABN) is additionally superseded by `research/ATHENE_FABN_MATURITY_LADDER_2026-06-22.md` for kill-path-1 figures.
- **T1b — Pre-closeout git-status check:** Added mandatory `git status -- AGENTS/SHADE/` scan as step 5.5 (pre-closeout guard) in CLAUDE.md spawn protocol. Catches bash-mv residue, unintended cross-dir changes, and stale inbox — run before any writes.
- **T1c — Retirement rule + first-pass archive:** Added ">60d + not boot-read + not referenced → git mv to archive/" as step 10a in closeout protocol. First-pass archived: `LAST_COMPLETION.md` (dormant), `research/STATUS_DRAFT_2026-06-15.md`, `research/STATUS_REFRESH_PHASE1_MAP_2026-06-15.md`, `research/STATUS_REFRESH_PHASE3_SOURCES_2026-06-15.md` (stale STATUS-rebuild scaffolding), `research/tmp_aaia_extract/` (session-temp PDFs). All moved to `archive/` via `git mv`. CLAUDE.md step 12 adds explicit `git mv` mandate for inbox/research moves.
- **Files touched:** `CLAUDE.md`, `STATUS.md`, all 8 `domain/sources/*.md`, `MAINTENANCE.md`; git-mv'd 6 files to `archive/`.

### 2026-06-22 — FABN maturity ladder artifact + CLAUDE.md kill-path re-mark
- **Trigger:** Will requested the Athene FABN maturity ladder (next-action #2 from the 6/21 boot).
- **What changed:** Added `research/ATHENE_FABN_MATURITY_LADDER_2026-06-22.md` (program stack + maturity-dated tranche list + the structural-invisibility finding + kill-path-1 read). Re-marked the **$16.5B 2026-2027 FABN wall as third-party/unverified** across STATUS (§0/§2/dashboard/calendar/next-actions/§8) **and edited `CLAUDE.md`** (Primary Target line + kill-path-1 line) — first time SHADE's own spec doc was annotated for a verified-thesis correction.
- **Files touched:** `research/ATHENE_FABN_MATURITY_LADDER_2026-06-22.md` (new), `STATUS.md`, `CLAUDE.md`, `SCRATCH.md`, `MEMORY.md`, `MAINTENANCE.md`; auto-memory `finding_private_by_construction_unverifiable.md` (new, + index line).
- **Key finding:** Athene Global Funding is not an SEC filer; 100% of FABN is 144A/Reg S; no public FABN maturity ladder exists → the kill-path-1 quantum is structurally invisible (mechanism still sourceable). Recovery path logged (NPORT-P holder CUSIPs).
- **Methodology:** 4-finder Workflow + adversarial reconcile (basis-conflation guard caught the ALL-ISC-vs-FABN trap).
- **Same-session follow-up — NPORT-P bottom-up reconstruction:** scoping-probe agent → confirmed tractable → scripted EDGAR crawl (`research/AGF_NPORT_crawl_2026-06-22.py`, reusable; output `research/AGF_NPORT_floor_2026-06-22.json`) of 1,602 fund filings recovered a $3.29B registered-fund floor → wall **bracketed ~$13-18B**, upgrading the $16.5B from "unsourceable" to "corroborated." Re-marked across STATUS/CLAUDE.md/research/MEMORY. First time SHADE ran a direct deterministic Bash/Python EDGAR crawl (vs LLM sub-agents) — far more reliable for structured-data ETL; pattern worth reusing. New artifact files: `AGF_NPORT_crawl_2026-06-22.py`, `AGF_NPORT_floor_2026-06-22.json`.

### 2026-06-21 — board_log.tsv created (WALTER consumption v0.2) + first agent-run boot
- **Trigger:** First live SHADE boot. WALTER delivery lane (`inbox/WALTER/`) held one unprocessed signal and no `board_log.tsv` existed.
- **What changed:** Created `board_log.tsv` with the v0.2 header (`timestamp_read<TAB>signal_id<TAB>disposition<TAB>source<TAB>notes`); logged + `git mv`'d `SIG-W-20260619-008` to `inbox/WALTER/processed/`. Added `research/SHADE_BOOT_SWEEP_2026-06-21.md` (verified domain-sweep artifact). STATUS gained a top-of-file §0 verified boot-delta section (now 203 lines).
- **Files touched:** `board_log.tsv` (new), `research/SHADE_BOOT_SWEEP_2026-06-21.md` (new), `STATUS.md`, `SCRATCH.md`, `MEMORY.md`, `inbox/WALTER/processed/SIG-W-20260619-008.md` (moved).
- **Boot impact:** WALTER intake (step 4a) is now wired — future boots append to `board_log.tsv` and `git mv` consumed signals. STATUS §0 is the canonical at-top verified-delta block.
- **Methodology note:** boot used a Workflow (5 finders → adversarial verify → synthesis). The verify pass retracted an inverted reinsurance claim — keep the verify stage on future sweeps.
- **Still deferred:** `NEXUS_BRIEF.md`, `boot.py`. (`yfinance` not installed in `.venv/` — local `fetch.py price` fails; not blocking, owner agents supply marks.)

### 2026-06-15 — Boot architecture scaffold added
- **Trigger:** Prome stale-agent review found SHADE very stale (last substantive status Mar 26) and architecturally behind mature agents (no SCRATCH/MEMORY/NEXUS_BRIEF/MAINTENANCE/boot protocol spine).
- **What changed:** Added `SCRATCH.md`, `MEMORY.md`, `MAINTENANCE.md`; modernized `CLAUDE.md` with a read→write SPAWN PROTOCOL, BROCK/SHADE boundary, source-of-truth discipline, and pathspec-only git rules.
- **Files touched:** `CLAUDE.md`, `SCRATCH.md`, `MEMORY.md`, `MAINTENANCE.md`.
- **Boot impact:** Future SHADE sessions should read STATUS → SCRATCH → MEMORY, then use owner files only as needed. Initial scaffold warned STATUS was stale; that was resolved later the same day by the live STATUS refresh below.
- **Deferred:** `NEXUS_BRIEF.md`, `boot.py`, workbook/thesis scaffolding. Build after the next substantive audit clarifies stable data surfaces.

### 2026-06-15 — Live STATUS refresh / March stale state archived
- **Trigger:** Prome phased SHADE catch-up showed old 2026-03-26 live status overcalled immediacy and carried stale APO price/position/catalyst rows.
- **What changed:** Archived old live status to `archive/STATUS_2026-03-26_pre_refresh.md`; created Phase 1 map, Phase 2 draft, and Phase 3 source notes; rewrote live `STATUS.md` as 🟠 structural/latent insurer-wrapper stress rather than 🔴 immediate crisis.
- **Files touched:** `STATUS.md`, `archive/STATUS_2026-03-26_pre_refresh.md`, `research/STATUS_REFRESH_PHASE1_MAP_2026-06-15.md`, `research/STATUS_DRAFT_2026-06-15.md`, `research/STATUS_REFRESH_PHASE3_SOURCES_2026-06-15.md`, `SCRATCH.md`, `MEMORY.md`, `memory/2026-06-15.md`.
- **Key architecture result:** SHADE now separates BROCK-owned fund stress, LIQUID-owned broad credit/funding confirmation, REGINALD-owned bank/NDFI transmission, and SHADE-owned insurer-wrapper mechanisms.
- **New audit target:** AMAPS/MAPS-type structured-credit wrappers became the named watch item after Apollo/Athene source refresh.
