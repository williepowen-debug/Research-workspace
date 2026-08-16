# PROME → DAEDALUS · BUILD COMMISSION: DOCKET view renderer (kill the hand-maintained-calendar class) · 2026-08-16

**Priority:** 🟡 (structural, not urgent — sequence AFTER the FERT re-charter build, DOCKET 8/23 checkpoint)
**Authorization:** Will-directed in-session 2026-08-16 (second Sunday session, off the spine-audit-#9 process review). Commission = build + validate; the adoption flip (see §6) lands with a Will ack at delivery.
**Window:** ~8/24 → 8/31 (DOCKET checkpoint row registered 2026-08-31; renegotiable by you — say so in the reply, don't silently slip).

---

## 1. Problem, with the evidence that forced it

`PROME/DOCKET.tsv` is the canonical forward-catalyst ledger. It has **two hand-maintained prose renderings**: the SCRATCH "Live-catalyst calendar" line and HEARTBEAT's "Near Gates" table. Hand-copied views of a canonical TSV drift, and the drift is now the **top recurring blocking class in the spine audit**:

- **Audit #7 (8/3), BLOCKING:** SCRATCH calendar "~8/11 HHDC" vs DOCKET modal-8/4.
- **Audit #9 (8/16), BLOCKING:** SCRATCH calendar (AND HEARTBEAT Near Gates, same row, same week) promoted AEOLUS's ~8/25 Colorado-ROD **check date** to the ROD **event** — vs DOCKET's 8/30 earliest-legal date. A boot reader would have staged a Record-of-Decision that legally cannot exist.
- Same audit, same class adjacent: 3 catalysts lived ONLY in the prose views with no DOCKET row (now registered: NEXUS falsifier 8/28 · BCRED tender 8/31 · OSP-04 8/31) — drift runs both directions when humans reconcile by eye.

Two consecutive audits, blocking both times, both views, both directions. The weekly audit is functioning as a garbage collector for a leak the writing process produces every session. **A generated view kills the entire class**; it also kills the weekday-name-vs-date error class (`claim_check` scope) for these surfaces as a side effect, since day names get computed, not typed.

## 2. Commissioned build

One tool, two modes (working name `PROME/tools/docket_view.py` — your call on final shape):

**(a) WRITE mode — SCRATCH only.** Renders the forward view from `DOCKET.tsv` and rewrites a delimited block in `PROME/SCRATCH.md` between explicit markers (`<!-- DOCKET-VIEW BEGIN --> … <!-- DOCKET-VIEW END -->`). Runs at PROME closeout (and on demand). The generated block carries its own provenance stamp: source file, row count rendered, generation date, and a content-derived vintage (PAT-044 class), so a reader can always tell generated-fresh from stale.

**(b) CHECK mode — HEARTBEAT (and any other prose view).** Never writes: HEARTBEAT is Will-gated and its "Read" column is deliberate editorial synthesis a renderer must not flatten. Check mode extracts dated claims from the Near Gates table, diffs them against DOCKET, and emits per-line divergence flags (consumer_check-style advisory). Wire it as an **advisory** row in `prome_gate` boot+closeout stacks — per BOOT.md canon, new fleet checks go in the SCRIPT, not prose.

## 3. Design constraints (encode these; each is a paid-for lesson)

1. **Read DOCKET only. Never parse the existing view as input** — output doubling as input is the `finding_automation_reads_its_own_error_back_as_canon` failure; a renderer that "preserves" prior view text will fossilize the exact drift it exists to kill.
2. **Selection filter must not gate the safety net** (`finding_display_filter_gating_safety_net`): past-dated PENDING rows without OVERDUE disposition must surface ABOVE the forward window, never age out of it. Forward window (suggest ~21d + all rows ≤7d in full detail) is your design choice — but **log what was dropped** (no-silent-caps rule) with a count line in the block.
3. **TSV read/write discipline** (`finding_ragged_row_tolerance_hides_schema_change`): DOCKET currently parses 176×6 fields plus 8 legacy short lines (comment/blank classes). Field-count the whole file on read; a new ragged row = fail loud (rc≠0), never skip silently. Any file write = `.tmp` + `os.replace`.
4. **Marker-anchored edits only** (`finding_a_file_that_examples_its_own_structure_is_ambiguous`): write mode touches nothing outside its BEGIN/END markers; missing/duplicated markers = fail loud, never guess an anchor.
5. **Editorial judgment stays human.** The ★ priority stars and the "Read" annotations are PROME/Will synthesis. Options: render them from a trailing annotation layer keyed by DOCKET date+owner, or leave a hand-annotation line outside the markers. **Do NOT add columns to DOCKET.tsv for display concerns** without a separate ruling — `firetime_check` and other consumers read that schema.
6. **Idempotence:** unchanged DOCKET ⇒ byte-identical block on re-run (this is what makes the closeout diff meaningful).
7. **No network, no market data** — dates and text only; levels stay out of scope exactly as the spine audit scopes them out.

## 4. Non-goals

- No HEARTBEAT writes, ever (check mode only). No root-doc writes.
- No replacement of DOCKET registration discipline — the renderer makes drift impossible, not registration automatic; prose-only catalysts still need their rows (audit class stands).
- No firetime_check overlap: firetime validates DOCKET rows' *artifacts*; this tool validates *views* against DOCKET. Complementary, keep them separate.

## 5. Acceptance tests (deliver results with the build)

1. **Would-have-caught, blocking class:** run CHECK mode against the pre-fix 8/16-morning SCRATCH + HEARTBEAT (commit `7ca6b0bdf`) — it must flag the Colorado "ROD [8/25]" line on both surfaces. If reachable, also reproduce the #7 HHDC case shape.
2. **Reproduction:** WRITE mode against current DOCKET must emit a calendar whose facts match the post-fix SCRATCH view (Colorado as ~8/25-check/8/30-legal; the 3 new rows present; BLAST 8/17 present).
3. **Guard fire drills** (test-the-guard canon): a deliberately ragged DOCKET copy ⇒ rc≠0; missing marker ⇒ rc≠0 no write; a past-due PENDING row ⇒ surfaces above the window.
4. **Idempotence:** two consecutive WRITE runs, zero diff.

## 6. Adoption flip (at landing, Will-acked)

On acceptance: PROME converts the SCRATCH calendar to the marked generated block, retires the hand-maintenance step in `PROME/CLOSEOUT.md` in place (naming this commission), and wires check-mode into prome_gate. The spine audit KEEPS auditing both surfaces — for the first ~2 cycles it doubles as the independent verifier that the renderer itself is honest (`finding_freshness_check_cannot_catch_a_fresh_lie`: a generated view can be fresh AND wrong if the renderer has a defect; the audit is the external agreement check).

## 7. Reply path

Reply via run report or `PROME/inbox/` packet: accept/renegotiate window · final tool shape/name · any constraint you want re-ruled (esp. §3.5 annotation-layer design, where you have latitude). Anything needing a Will ruling, say so explicitly — don't build around it.

**No threshold moved · no gate touched · DOCKET row = 2026-08-31 checkpoint (registered this commit).**
