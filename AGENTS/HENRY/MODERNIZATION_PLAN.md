# HENRY MODERNIZATION PLAN

**Author:** HENRY · **Date:** 2026-06-03 (drafted ~22:00 ET) · **Status:** 🔵 PROPOSAL — Will review before any execution
**Scope:** Internal house-keeping only. No signals (inbox/outbox), no position work. Goal = get HENRY's own files current + restructure the tree to match SAM/BRENT.
**Decisions locked by Will at drafting:** (1) *Plan first, don't execute.* (2) Thesis layer = **full mirror** of SAM/BRENT (THESIS + CHANGELOG + TIMELINE + PREDICTIONS_ARCHIVE).

---

## 0. The diagnosis in one paragraph

HENRY's **live layer** (STATUS, MEMORY) is same-day fresh. Its **workbook + domain layer is frozen at ~Apr 16-17** — a 7-week gap predating the entire trap-clinch→split-axis evolution. And architecturally HENRY is **one generation behind SAM/BRENT**: it has no versioned thesis layer — the thesis lives *inline* in STATUS, so there's no version history, no audit trail, no separation of durable-view from daily-snapshot, and STATUS is bloating toward its 250-line cap. Three of Will's saved cross-agent memories already pre-tag these exact transfers (`finding_pov_changelog_pattern`, `finding_boot_predictions_scan`, `finding_boot_closeout_hardening_recipe`) — this is a roadmap item, never executed.

---

## 1. Current state vs target tree

```
                          NOW                                AFTER
  HENRY/
    STATUS.md          (triple-duty: snapshot+thesis+      STATUS.md   (pure live snapshot)
                        thresholds, ~160 lines)
    LESSONS.md  MEMORY.md  LAST_COMPLETION.md              (unchanged)
    CLAUDE.md          (boot: STATUS→LESSONS→MEMORY)       CLAUDE.md   (boot: THESIS→STATUS→LESSONS→MEMORY
                                                                        + docket countdown; hardened closeout)
    —                                                      MAINTENANCE.md      ← NEW (structural-change log)
    —                                                      thesis/             ← NEW
      (thesis inline in STATUS)                              THESIS.md         ← NEW (v1.0 = split-axis)
      —                                                      CHANGELOG.md      ← NEW (POV-pivot audit trail)
      —                                                      TIMELINE.md       ← NEW (resolved-event chronology)
      workbook/PREDICTIONS.tsv                               PREDICTIONS.tsv   ← MOVED here
      —                                                      PREDICTIONS_ARCHIVE.md ← NEW (closed post-mortems)
    —                                                      docket/             ← NEW
      domain/ECON_CALENDAR.md (stale 4/16)                   CALENDAR.md       ← MOVED + refreshed
      (catalysts inline in STATUS)                           CATALYSTS.tsv     ← NEW (machine-readable + countdown)
    workbook/
      KB.tsv (4/17, 137 rows)                              KB.tsv  (gap-filled to 6/3)
      VX.tsv (4/17, 6 dup IDs)                             VX.tsv  (dup IDs fixed)
      FLOW.tsv (Mar-Apr war-era, 27 rows)                  FLOW.tsv + FLOW_ARCHIVE.tsv (refresh-split)
      THESIS_VALIDATION.md (Apr-17 "Loaded Machine")       → folded into thesis/THESIS.md §Validation
      VX_HISTORY.tsv  MARKET_DATA.tsv                      (unchanged)
    domain/ research/ sources/ archive/ scripts/           (unchanged)
    inbox/ outbox/                                         (untouched — no-signal directive)
```

---

## 2. PHASE A — Stale refresh (mechanical, low-risk, fully reversible)

No script reads any of these TSVs, so every edit is boot-safe. All reversible via git.

| # | File | Action | Detail |
|---|------|--------|--------|
| A1 | `workbook/KB.tsv` | **Gap-fill** ~6-8 rows | Close 4/17→6/3. Content already exists in STATUS/MEMORY, just needs KB rows: split-axis decomposition, FRED convention, sibling-staleness cascade, NVDA 5/20 read-through, USD/JPY 160 cross, APO sub-130, R11-dead/HEN-31-expired, energy-driven-vs-Fed-pivot yield easing. ID continues `ML-HEN-137+`. |
| A2 | `workbook/VX.tsv` | **✅ DONE 6/15 — Fixed 6 dup IDs** | Rows 47-53 (oil-shock SLOW-MOVING block) collided with rows 19-24 (Beige Book block), both `VX-HEN-19.01–.06`. Renumbered the oil-shock block → `VX-HEN-21.01–.07` (in place). **Correction to original scope:** "pure key fix, no data change" **under-scoped it** — the cross-refs ARE data: required per-ref remaps of 3 internal 20.xx cross-links + 12 KB + 5 FLOW refs (Batch-A-targeting kept 19.xx; the 6 split tokens, esp. 19.03, would've corrupted Batch A on a blanket replace). ML-HEN-081's pre-existing CRE→19.03 imprecision flagged inline, not "fixed." |
| A3 | `workbook/FLOW.tsv` | **Refresh-split** (SAM pattern) | All 27 vectors are Mar 3–Apr 17, mostly "ACTIVE/ARMED" under the *selloff/war* regime — now stale under compression. Split: resolved point-in-time telemetry (oil-shock staircase, immigration dual-shock, Mar gamma cascade) → new `FLOW_ARCHIVE.tsv` with `[RESOLVED date]` prefix; keep + refresh the still-structural vectors (cascade order, credit-equity lead, 0DTE feedback, risk-parity) to split-axis framing. |
| A4 | `workbook/THESIS_VALIDATION.md` | **Don't refresh in place — fold** | It's the Apr-17 "Loaded Machine" thesis w/ Mar validations; superseded by split-axis. In Phase B its *live* invalidation criteria migrate into `thesis/THESIS.md §Validation`; the historical "Loaded Machine" record archives. (Listed here because it's the stale trigger; executed in B.) |
| A5 | `domain/ECON_CALENDAR.md` | **Refresh forward rows** | "Mar-Jun" calendar, stale 4/16. June rows now live only in the inline STATUS stack. Refresh, then in Phase C it becomes `docket/CALENDAR.md`. |

**Phase A boot-impact:** none. **Reversibility:** total (git). **Checkpoint:** after A1-A3, show you the KB rows + FLOW split before moving on.

---

## 3. PHASE B — Thesis layer (FULL MIRROR — your locked choice)

The keystone. Extract HENRY's thesis out of STATUS into a versioned `thesis/` directory matching SAM/BRENT exactly.

### B1 — `thesis/THESIS.md` (NEW, v1.0)
- Establish **v1.0 = SPLIT-AXIS** (6/3). HENRY's thesis has *never* been versioned — this is the baseline.
- Lift the "SPLIT-AXIS THESIS" + "INVALIDATION TRIAD" + core methodology (cascade mechanics, credit-primary rule) out of STATUS/CLAUDE into one durable doc. Structure mirrors BRENT: Version / Status / Conviction / Core Thesis / one-liner / channels (cyclical axis vs structural axis) / **§Validation** (absorbs the live criteria from THESIS_VALIDATION.md A4).
- STATUS then *points* to THESIS for the view and keeps only the live snapshot.

### B2 — `thesis/CHANGELOG.md` (NEW)
- First entry = the **trap-clinch-WIDER (5/21) → SPLIT-AXIS (6/3)** pivot, old-view→new-view, exactly the honest downgrade already narrated in STATUS/MEMORY.
- Seed a compact **pre-v1.0 history pointer block** (don't reconstruct in full): Mar "gamma cascade" → Apr "complacency trap" → May "trap-clinch" → Jun "split-axis." Preserves trajectory per `finding_pov_changelog_pattern`.
- Versioning convention adopted: major (X) = structural/conviction reversal/axis change; minor (Y) = refinement.

### B3 — `thesis/TIMELINE.md` (NEW)
- Resolved-event chronology: HEN-27 confirmed, R11/HEN-31 expired-un-fired, NVDA 5/20 catalyst-decay, USD/JPY 160 cross, Hormuz re-spike + full unwind, the 13-day dark gap. Dated, RESOLVED-tagged. Light to start; grows at closeout.

### B4 — `thesis/PREDICTIONS.tsv` (MOVED) + `thesis/PREDICTIONS_ARCHIVE.md` (NEW)
- `git mv workbook/PREDICTIONS.tsv thesis/PREDICTIONS.tsv` (history preserved).
- Move closed-row post-mortems (HEN-27 confirmed; HEN-31 expired) to `_ARCHIVE.md`, leave one-line lesson + `→ #HEN-NN` pointer inline (BRENT/SAM convention). Keeps OPEN rows (HEN-28/30/32) live.

### B5 — Slim STATUS.md
- After extraction, STATUS = pure live snapshot: LIVE TAPE table, VOL REGIME block, ACTIVE THRESHOLDS (STANDING-vs-STATE convention stays), CROSS-AGENT DEPENDENCIES, BOTTOM LINE. Thesis prose → pointer to `thesis/THESIS.md`. Target: comfortably under the 250 cap with headroom.

**Phase B boot-impact:** **changes the boot sequence** (THESIS becomes read #1). That's a CLAUDE.md SPAWN PROTOCOL edit → **eval re-baseline trigger** — flag to Will, don't silently ship. **Reversibility:** high (git; moves not deletes). **Checkpoint:** show THESIS.md + CHANGELOG first entry + slimmed-STATUS diff before committing.

---

## 4. PHASE C — Docket + maintenance + CLAUDE.md hardening

| # | Item | Action |
|---|------|--------|
| C1 | `docket/CATALYSTS.tsv` | NEW machine-readable forward-catalyst feed (replaces inline STATUS "JUNE CATALYST STACK"). Schema = SAM's: date / event / priority / who_cares / threshold_signal. Seed with 6/5 NFP, 6/10 CPI (the gate), 6/11 PPI, 6/16-17 FOMC, 6/18 expiry cluster, late-Jul BDC/WAL Q2. |
| C2 | `docket/CALENDAR.md` | `git mv domain/ECON_CALENDAR.md` → here (refreshed in A5). Narrative/routing/threshold prose; **no live spot** (SAM TRUTH-MODEL: TSV owns the event set, CALENDAR owns prose, neither owns live levels). |
| C3 | `scripts/catalyst_countdown.py` | Lift + adapt SAM's countdown script (re-path to HENRY docket; keep its holiday-skip set). Boot runs it → trading-days-to-next-catalyst surfaces automatically. *Optional / can defer — manual works.* |
| C4 | `MAINTENANCE.md` | NEW structural-change log (separate from analytical CHANGELOG, per SAM). First entry = this whole modernization. |
| C5 | `CLAUDE.md` | Boot step: add THESIS as read #1 + docket countdown. Closeout: catalyst-sweep *before* prediction-resolve; resolve-don't-leave-OPEN-stale rule; doc-ownership table; FILES-table rewrite for the new tree. Applies `finding_boot_closeout_hardening_recipe`. |

**Phase C boot-impact:** CLAUDE.md changes = eval re-baseline trigger (same flag as B). **Reversibility:** high.

---

## 5. Open decisions for execution time (not blocking the plan)

1. **THESIS_VALIDATION.md fate** — recommend *fold live criteria into THESIS.md §Validation + archive the "Loaded Machine" doc* (matches SAM/BRENT keeping validation inside THESIS). Alternative: keep as a standalone refreshed file. → my rec: fold.
2. **VX.tsv** — recommend *minimal dup-ID fix now*; defer the SAM-style "slim-to-unique" audit (37→6 there) to a later workbook pass. Don't bundle a big VX rationalization into this arc.
3. **catalyst_countdown.py (C3)** — recommend *defer*; stand up CATALYSTS.tsv first (data), wire the script only if you want the boot-time countdown. Manual is fine near-term.
4. **TIMELINE depth** — start light (resolved events only); not a full back-fill of the Feb-Jun arc.

---

## 6. Boot-impact, git, reversibility (cross-cutting)

- **Boot-safe:** no HENRY script reads KB/VX/FLOW/PREDICTIONS — Phase A is invisible to boot. Phase B/C *change CLAUDE.md boot/closeout* → eval re-baseline trigger (flag to Will + PROME; don't ship silently).
- **Git:** every file is inside `AGENTS/HENRY/` → safe to stage per isolation rule. **Note:** working dir currently shows *SAM* workbook TSVs modified (JGB_YIELDS / MOF_FLOWS / USDJPY) — at commit I stage `AGENTS/HENRY/` only, never `-A`. Use `git mv` for all moves (PREDICTIONS, ECON_CALENDAR) to preserve history + keep deletions staged.
- **Reversibility:** Phase A fully reversible; B/C are moves+adds (not destructive deletes) — the old "Loaded Machine" / war-era FLOW content is archived, not erased.

---

## 7. Recommended session arc (for when you green-light)

| Session | Does | Risk | Gate |
|---------|------|------|------|
| **1** | Phase A (A1-A3, A5) — KB gap-fill, VX dup-fix, FLOW split, calendar refresh | low | checkpoint after KB+FLOW |
| **2** | Phase B — thesis/ full mirror + STATUS slim + CLAUDE boot edit | med (boot change) | checkpoint before commit; eval flag |
| **3** | Phase C — docket + MAINTENANCE + CLAUDE closeout hardening + FILES rewrite | low-med | eval flag |

Mechanical-before-creative: A is pure hygiene, B is the structural keystone, C is the plumbing that makes B durable. Each session = one clean commit, front-loaded decisions, proceed-pacing at boundaries (per `feedback_front_load_planning`).

---

*This is a proposal. Nothing above is executed. On green-light I start at Session 1 / Phase A and checkpoint as marked.*
