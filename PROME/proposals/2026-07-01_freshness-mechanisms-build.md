# Freshness Mechanisms Build — fire-time check + spine reconciliation
**Date:** 2026-07-01 PM-3 · **Author:** Prome · **Status:** WILL_APPROVED (in-session, 7/1: "1. ok that works. 2. your rec. 3. lets do it tonight") — BUILD IN PROGRESS same session.
**Origin:** Will asked for a rating of the PROME setup; the two ranked gaps were (1) no fire-time artifact freshness check (WAL Jul-30 rode 5 days in the fire-time proposal) and (2) no standing spine-reconciliation cadence (boot-read docs carried canon-contradicting directives until a Will-triggered audit). This spec is the approved plan; Tier-2 items (new TSV + new monitoring protocol) are covered by this approval.

## Phase 0 — anchors
- **`PROME/DOCKET.tsv`** — canonical machine-readable forward-catalyst docket. PROME-owned; write-back at closeout (operator-card pair); LIVE-ledger discipline via `scripts/ledger_staleness.py PROME --glob 'DOCKET.tsv' --days 7` (no script change needed — path+glob args already support it). SCRATCH operator card + HEARTBEAT near-gates become prose views; **DOCKET wins on drift.**
- **Mirror map** — "canonical fact → known mirrors" table in `PROME/SYSTEM.md` (Boot Trust Stack), seeded from the 7/1 24-file audit (we know where every mirror is today). Mechanizes `[[finding_doc_mirror_consistency_check]]`.

## Phase 1 — `scripts/firetime_check.py` (fire-time freshness)
Read-only, flags-never-fixes, fail-loud on missing docket. Checks per artifact:
1. **Pointer resolution** — backtick-quoted repo paths exist on disk.
2. **Date drift** — dates extracted from the artifact that match NO docket row but fall near (±45d) a docket date → flag (the Jul-30-vs-Jul-16 class). Historical-annotation heuristic: dates preceded on the same line by "corrected from / was / superseded / slid / designed when" are skipped (alert-fatigue control).
3. **Canon-ordering** — artifact's last git-commit time vs last-change time of the canon docs it cites → "artifact predates canon change" info flag.
- v2 (deferred): band-literal check vs `config.py` — the spine audit covers bands in v1.
- **Discipline rule (encoded in wiring, not script):** any date/band flag ⇒ full logic re-read of the artifact, not a find-replace — the 7/1 date fix exposed a sequencing break no parser catches.
- **Acceptance test:** the pre-fix bank-put proposal (from git history) MUST trip on Jul-30 + its 2 dead pointers; the current version must pass clean.

**Wiring:** BOOT conditional (docket catalyst ≤7d → run `--window 7`); CLOSEOUT Chunk-3 trigger (docket date changed → run + re-read rule); freshness line in `action-cards/TEMPLATE.md`; task packet → TERRY (pre-fire checklist line; TERRY owns fire rules).

## Phase 2 — spine reconciliation
- **Canon-change-gated sweep (cheap, deterministic):** CLOSEOUT Chunk-3 trigger — canonical doc changed this session → walk its Mirror-Map row and verify each mirror before commit.
- **Weekly mini-audit (catch-all):** 5-reader workflow (`PROME/tools/spine_audit.workflow.js` — in-repo, NOT `.claude/` which is untracked/machine-local) over the ~9 boot-read/protocol files vs enumerated canon anchors. **"Last spine audit: DATE" stamp in `PROME/STATUS.md`**; boot flags it when >7d.
- **Acceptance test:** first run comes back near-clean but flags the 2 known deliberately-left minors (ORCHESTRAL L32 unqualified agent count; scrub-plan playbook tense) — sensitivity calibration.

## Phase 3 — first live runs + calibration
Run both tonight; tune false positives (v1 flags only high-confidence classes — **alert fatigue is how these mechanisms die**); memory the pattern. Fleet extension (agents' STATUS files share the disease) → DAEDALUS pattern packet LATER; v1 is PROME-scope.

## Non-goals / scope guards
No auto-fixing; no new cross-agent messaging (overhaul parked per `[[project_messaging_overhaul]]`); no HEARTBEAT edit tonight (Will-gated — its near-gates table gets the DOCKET pointer at its next regime update); no fleet rollout in v1.
