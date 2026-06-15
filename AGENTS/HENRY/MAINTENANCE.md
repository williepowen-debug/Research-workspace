# HENRY MAINTENANCE LOG

*Structural-change log — doc created/retired/moved, script built or behavior-changed, protocol/CLAUDE.md amendment, schema change. Analytical changes live in STATUS/thesis; routine content edits don't qualify. SCRATCH/session notes get overwritten — structure persists HERE. (Modeled on VIOLET/SAM MAINTENANCE.md; created 2026-06-15.)*

---

### 2026-06-15 — RETIRED `scripts/refresh_status.py`
- **Trigger:** Boot-audit + Will/ORC/Prome convergent review flagged it as a stale-data writer.
- **What changed:** Moved `scripts/refresh_status.py` → `archive/retired/refresh_status.py`.
- **Why (do NOT resurrect):** It read a STATIC `MARKET_DATA.tsv` row (not a live pull) and **authored the Signal-Status line with a hardcoded narrative** ("COMPLACENCY TRAP / CPI 3.3% locks Fed"). Running it would silently overwrite STATUS's live header with stale, wrong framing — the exact "stale presented as live" trap HENRY's state-claim convention exists to prevent.
- **Files touched:** `archive/retired/refresh_status.py` (moved), `scripts/boot.py` (comment), `BOOT_AUDIT.md` (lines 23/42).
- **Boot-impact:** None — `boot.py` calls `fetch.py` directly for the live tape; it never imported refresh_status.
- **Spec for any FUTURE refresher (if one is ever built):** must be (1) **live-sourced** (fetch.py/FRED, never a static TSV); (2) update **mechanical table rows only**, NEVER author the Signal Status / thesis narrative; (3) default to **dry-run / diff**; (4) ship with a **test fixture**. Absent all four, don't build it.

### 2026-06-15 — BUILT `scripts/boot.py` v1
- **Trigger:** Boot-parity upgrade (HENRY was the only macro-cluster agent without a boot kit).
- **What changed:** New read-only boot orchestrator — (a) live tape via fetch.py real-time quotes, (b) FRED credit via credit_monitor.py, (c) predictions-due scan of PREDICTIONS.tsv (OPEN/ACTIVE, resolve-date ≤ today). `--verbose / --quick / --selftest`.
- **Boot-impact:** Optional convenience now; becomes a boot step only via the deferred CLAUDE.md change (eval-gated). Read-only by design — does NOT write STATUS.
- **Validation:** `--selftest` PASS (due-scan surfaces an ACTIVE past-deadline row, ignores closed); dry-run tape+credit matched manual pull.

### 2026-06-15 — STOOD UP `NEXUS_BRIEF.md`
- **Trigger:** BRIEFS_MAP had HENRY as ❌ MISSING Priority-#2 ("3 of 4 briefs waiting on HENRY").
- **What changed:** New `NEXUS_BRIEF.md` from the NEXUS template (schema R3 + amendment 7). NEXUS already reads HENRY's brief at its boot step 6 (HENRY pre-registered) — self-serve, no NEXUS registration needed.
- **Boot-impact:** Makes HENRY visible to the cross-agent synthesis layer NOW. The reciprocal wiring (HENRY *reads* peer briefs at boot + maintains its own at closeout) is a CLAUDE.md change = **DEFERRED** (eval-triggering; needs a minimal eval suite as a net first).

### DEFERRED (post-FOMC, eval-gated) — boot/closeout protocol wiring
- Tiered per ORC: (1) **additive** NEXUS read-at-boot / write-at-closeout first (light review — closes the VIOLET-stale miss); (2) behavior-changing logic (live-event EXECUTE-override, staleness overlay into protocol, LAST_COMPLETION-vs-SCRATCH reconcile, catalyst docket) only AFTER a minimal HENRY eval suite exists.
- Any CLAUDE.md boot/closeout step addition = eval re-baseline trigger; flag to Will/PROME, never silent-ship.
