# SHADE MAINTENANCE LOG

Structural-change log for SHADE architecture: docs/scripts/protocol/schema changes. Analytical changes belong in `STATUS.md` or research files.

---

### 2026-07-27 — Catch-up boot: both mail lanes drained; new primary-research artifact; new discovery route recorded (with its limit)
- **Trigger:** Will catch-up boot (7-day gap). `inbox/WALTER/` had accumulated **10 unprocessed signals** since 7/21 and `inbox/` root held **5** (two of which — DEWEY's double-jeopardy map 21:57 and PROME's weld-2 amendment 22:11 — landed *after* the 7/20 closeout at ~21:30 and had never been seen).
- **Mail:** all **15** logged to `board_log.tsv` with reasoned dispositions and `git mv`'d to the respective `processed/` dirs. **Both lanes now CLEAN.** Created `inbox/processed/` (did not previously exist for the root lane).
- **New research artifact:** `research/DELAWARE_LIFE_RELATED_PARTY_RESTATEMENT_2026-07-27.md` — primary-verification of WALTER `SIG-W-20260727-004`.
- **New discovery route recorded (with its boundary):** insurer **statutory financial statements** can be SEC-visible when a carrier bundles the depositor insurer's statements into its separate-account **Form N-VPFS** filings — this is how the Delaware Life statutory related-party note became reachable/searchable on EDGAR. **Explicitly recorded as issuer-specific, NOT general:** Athene's N-VPFS filings carry separate-account statements only, so the **Athene Schedule-BA/statutory wall stands**. Also recorded that an **EDGAR full-text screen for a statutory-note phrase is a FALSE ZERO as a cohort test.** Both written to `MEMORY.md` so a future session doesn't re-derive or over-generalize the route.
- **STATUS structural changes:** added §0d; added a new dashboard row (*Related-party classification integrity*) and a new §5 watchlist row (*Group 1001 — Delaware Life + Clear Spring*); added 2 §6 calendar rows; added §8 items 7–10; rewrote BOTTOM LINE. Convergence index vector #1 rescored 4→5 (composite 19→20/30) — **first time any SHADE vector has been scored firing.**
- **Corrections applied to existing surfaces:** §3 double-jeopardy row (DEWEY's named-entity lender-leg refutation + the MassMutual/Barings fund-facility reading withdrawn); §3 ratings row (the standing "no downgrade/neg-outlook on any PE-adjacent life insurer" claim is no longer true — S&P negative outlook on Delaware Life).
- **Cross-agent packets written (root CLAUDE.md carve-out ①, self-authored, committed explicitly-pathed):** `AGENTS/BROCK/inbox/2026-07-27_from-SHADE_delaware-life-related-party-PRIMARY-verified.md` and `PROME/inbox/2026-07-27_from-SHADE_vector1-FIRING-delaware-life-primary.md`.
- **Files touched:** `STATUS.md`, `SCRATCH.md`, `MEMORY.md`, `MAINTENANCE.md`, `board_log.tsv`, `research/DELAWARE_LIFE_RELATED_PARTY_RESTATEMENT_2026-07-27.md` (new), 15 moved inbox files, 2 outbound packets.
- **Note for next session:** `fetch.py` has **no `hy_oas` symbol** (it routes to yfinance and 404s); HY OAS must be pulled via `python3 FORGE/tools/market-data/fetch.py fred BAMLH0A0HYM2`. Worth remembering — the obvious invocation fails silently-ish with a Yahoo "delisted" error.

### 2026-07-09 (eve) — Will-directed fleet self-sweep (stale/inconsistent info)
- **Trigger:** Will-directed fleet-wide self-sweep for stale/inconsistent info, same evening as the LIGHT catch-up spawn.
- **Dead pointer fixed:** STATUS §9 "Phase documents" list pointed to `research/STATUS_DRAFT_2026-06-15.md` / `STATUS_REFRESH_PHASE1_MAP_2026-06-15.md` / `STATUS_REFRESH_PHASE3_SOURCES_2026-06-15.md` — all three were `git mv`'d to `archive/` on 6/26 (T1c pass below) but STATUS's own pointer was never updated. Corrected to `archive/...` paths.
- **Retirement (>60d + unreferenced):** `research/NAIC_SPRING_MAR26.md` (mtime 2026-03-27, ~104d old, zero references anywhere in STATUS/SCRATCH/CLAUDE/MEMORY, content superseded by the current NAIC CLO-RBC narrative in STATUS §2/§6) → `git mv`'d to `archive/NAIC_SPRING_MAR26.md`.
- **Overdue calendar rows re-spec'd (STATUS §6):** the 2026-06-23 NAIC RBC IRE WG webex (16d overdue) and 2026-07-06 NAIC CLO C-1 Residuals/PAF comment deadline (3d overdue) were still labeled "New / imminent" / "live comment window" — factually stale framing. Re-spec'd both as PASSED-UNGRADED with an explicit note that no fresh NAIC pull was done this LIGHT catch-up (no fleet agent carries the outcome either) — flag for next SHADE session, do not assume relief/resolution from silence.
- **Asymmetric-record fix:** the 7/5 AI-capex-preload-cc → HENRY contribution (drafted this evening, `outbox/2026-07-09_to-HENRY_ai-capex-insurer-contribution.md`) was logged `drafted-pending-route` earlier the same session; PROME then delivered it to `AGENTS/HENRY/inbox/` (Will-authorized) before the sweep. Updated `board_log.tsv` disposition to `acted`/DELIVERED-7/9, and reconciled STATUS/SCRATCH/outbox-file language so sender and (per PROME) receiver records agree.
- **Checked, no fix needed:** WAL/OZK Q2-date claims (none present in SHADE files), X1/BND-11/truce/QT canon (SHADE's own STATUS/SCRATCH already matched tonight's digest — written earlier this same session), Athene figures (already the 7/4-verified $154.9bn/+42%/yr/~35%-of-assets set throughout; no residual +49%/40-43%/34.7% vintage found). `domain/sources/` KB docs (01-08) already carry `LAST_REVIEWED: 2026-03` + explicit >60d-stale banners from the 6/26 T1a pass — left as-is (already correctly bannered, not silently rotted).
- **Files touched:** `STATUS.md`, `SCRATCH.md`, `board_log.tsv`, `outbox/2026-07-09_to-HENRY_ai-capex-insurer-contribution.md`, `MAINTENANCE.md`; `git mv` `research/NAIC_SPRING_MAR26.md` → `archive/`.

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
