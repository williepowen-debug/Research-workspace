# FALCON SCRATCH — 2026-07-12 (spinout / build session)

**Purpose:** Ephemeral session handoff — the canonical "where are we / what next" file. Read at boot (SPAWN PROTOCOL step 2), rewritten in full at closeout (step 13). Disposable: rewritten every session, not appended to. Persistent learnings live in `MEMORY.md`; the cross-agent twin is `NEXUS_BRIEF.md`.

**This is FALCON's first SCRATCH** — written by DAEDALUS (build sub-agent, WP-1) at scaffold time, not by a live FALCON session. Treat everything below as a **seeded snapshot from HAWK's 2026-07-12 live state**, not a FALCON-verified read. FALCON's first real session should re-verify CURRENT MARKS against fresh search before acting on them.

---

## CURRENT MARKS (one line)
- Scenario: **B 8% / C 34% / D 58% (BASE)** · Convergence **~37/50 🔴** (4 kinetic vectors maxed = war-first) · Kinetic risk **🔴** (3rd strike round done; 4th possible) · Brent ref **~$76** [defer price to BRENT; sustain test FAILED → DENY 7/10]

## CHANGES SINCE LAST SESSION
- **FALCON was created 2026-07-12** — spun out of HAWK per Will-approved concept (`AGENTS/HAWK/design/2026-07-12_war-agent-split-spec.md`) and DAEDALUS's ratified build spec (`AGENTS/DAEDALUS/builds/OSPREY_FALCON_BUILD.md`). Root cause: HAWK held two acute, independent wars (Iran/Gulf + Russia/Ukraine) and the load asymmetry produced the HAW-15 miss (a 22-day-stale, gappy Russia strike ledger). FALCON now owns the Iran/Gulf theater exclusively; sibling **OSPREY** owns Russia/Ukraine; **HAWK** becomes cross-war synthesis + the dormant book (Taiwan/Venezuela/trade-war/Suez/Malacca/defense/global war-risk-shipping synthesis).
- STATUS.md, workbook/{VX,FLOW,SCHEMA,EXIT_PROTOCOL}, thesis/{PREDICTIONS,THESIS,TIMELINE,CHANGELOG}, domain/energy-strikes/{STRIKES,ANALYSIS}, LESSONS.md, MEMORY.md, SOURCES.md were all seeded from HAWK's live 2026-07-12 content per the build spec's migration manifests (`AGENTS/DAEDALUS/builds/hawk_split/MANIFEST_{A,B,C}`). KB.tsv, board_log.tsv, and PREDICTIONS.tsv all start **fresh** (0 rows / 1 OPEN row respectively) — the historical record is frozen under `AGENTS/HAWK/`.
- Tier-1 ledger-discipline fixes (swept-through high-water-mark, boot staleness alarm, closeout sweep cadence, raw-log/interpretation split) are baked into FALCON's CLAUDE.md from day one — this is the direct root-cause fix for the HAW-15-class miss.

## WHAT I DID THIS SESSION
- (DAEDALUS, build sub-agent WP-1) Read the build spec + all three migration manifests + the blueprint standard; scaffolded `AGENTS/FALCON/` per build spec §5; migrated VX (7 rows), FLOW (11 rows), STRIKES (4 rows) verbatim via mechanical extraction (no hand-retyping of TSV data — awk-filtered from HAWK's source files to avoid transcription error); wrote CLAUDE.md, STATUS.md, LESSONS.md, MEMORY.md, SOURCES.md, PREDICTIONS.tsv (fresh, FAL-01 ← HAW-16), THESIS/TIMELINE/CHANGELOG (wholesale inherit), ANALYSIS_2026-07-12.md (near-empty, template only), KB.tsv (fresh, 0 rows), board_log.tsv (fresh, header only). Created `.gitkeep` placeholders for inbox/outbox processed/delivered dirs.
- Did **not** run `git pull`, boot predictions-scan, ledger_staleness.py, or baghdad_watch.py — this is a build/scaffold session, not a live FALCON boot. Did not touch any file under `AGENTS/HAWK/` (read-only per build constraints; HAWK's own re-cut is WP-3, a separate work package).

## NEXT SESSION (dated, future-verifiable) — inherited Iran-coded items from HAWK's 7/12 handoff
1. **4th US strike round / further kinetic** — did strikes continue past 7/12, or halt? Check news first thing on FALCON's first live boot.
2. **FAL-01 gate watch** (← HAW-16) — any Gulf-ally/Iranian oil-PRODUCTION-infra hit (Aramco/ADNOC/Kharg-oil) OR vessel confirmed SUNK? = C→D-runaway confirm + Brent decoupling breaks. Window to **Jul 26**.
3. **Brent sustain (BRENT-owned)** — does Brent finally break and HOLD >$85 w/ ≥2 institutional legs? Failed twice (6/28, 7/10). Single cleanest D-vs-C market discriminator.
4. **Oman two-route Hormuz proposal** — does it land with a date (→B) or die (→D)? US-Iran technical-talks readout watch.
5. **Iraq/PMF backlash** — Baghdad watch QUIET as of 7/12; re-run at first live boot once `baghdad_watch.py` lands via WP-3 git mv (unfired CONFIRM-D discriminator #5).
6. **Mojtaba public-reappearance watch** — would ease the incapacitation/longer-tail flag.

## FIRST-INCREMENT ITEMS (founding backlog — flagged at spinout, not yet actioned)
1. **Gulf-Iran strike backfill sweep** [FOUNDING MANDATE] — the inherited `domain/energy-strikes/STRIKES.tsv` is only 4 Mar-2026-vintage seed rows; HAWK's pre-split analysis layer was ~95% Russia-theater. Run a date-careful Mar→Jul 2026 backfill sweep before computing any Gulf-Iran aggregate. See `domain/energy-strikes/ANALYSIS_2026-07-12.md`.
2. **Refresh-and-pull-forward candidates from frozen `AGENTS/HAWK/scripts/`** — `war_monitor.py`, `thresholds.py`, `oil_infrastructure.py`, `sanctions_tracker.py` all carry stale Apr-vintage hardcoded data (War Day 51, D82-C12-B6 baseline, Apr-13 facility states) and were **deliberately NOT ported** at build time (build spec §2 — porting stale-authoritative-looking scripts is worse than no scripts). If FALCON wants any of these, treat as a from-scratch rebuild using the frozen files only as a design reference, not a source of current data.
3. **`thesis/THESIS.md` rewrite backlog** — inherited file carries its own Apr-20 SUPERSEDED banner; the current canonical scenario read lives in STATUS.md. Rewriting THESIS.md to the current regime (post-7/12 step-up) is open and unclaimed.

## OPEN THREADS / WATCHES
- 🔴 4th US strike round / further kinetic — hourly-relevant, check news before any FALCON action
- 🔴 FAL-01 hard-gate (production-infra hit / vessel sunk) — the C→D-runaway kill-switch
- 🔴 Brent break-and-hold >$85 w/ ≥2 legs (BRENT-owned; failed 6/28 + 7/10)
- 🟠 Oman two-route Hormuz mediation — the live B-path
- 🟠 Iraq/PMF backlash (unfired discriminator #5; Baghdad watch automated, pending WP-3 script arrival)
- 🟡 Mojtaba public reappearance (incapacitation/longer-tail flag)

## PREDICTIONS DUE / DECISIONS PENDING
- FAL-01 (Jul 26, production-infra/vessel-sunk gate). No Will-decision pending (FALCON holds no trade book).

## MAIL STATE (one line per surface)
- Inbox (root): clear (fresh agent, no items yet)
- WALTER lane: clear (fresh agent, no items yet)
- Outbox: clear (fresh agent, no items yet)

## PENDING PUSH / GIT (if any)
- **Build-phase note:** this scaffold is committed by DAEDALUS under pathspec `AGENTS/FALCON/`, per build spec `AGENTS/DAEDALUS/builds/OSPREY_FALCON_BUILD.md` §7 (Will/PROME-approved new-agent build). FALCON's own auto-push-at-closeout regime starts at its first live session.
