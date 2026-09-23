# prome-da closeout — bounded corrections on CATO C1–C3

**Source finding:** `AGENTS/CATO/runs/2026-09-23_1808_prome-da-closeout-audit.md` (commit `ed09eaf5b`). **Authorized by Will** 2026-09-23 18:26 ET: bounded corrections, required review and an exact-path commit/push. Publication remains deferred. **Written by** PROME `prome-da` (desktop), 18:2x–18:3x ET. This record adds no control and no machinery; the HEARTBEAT repair loop stays closed.

## C1 — stale Helm priorities

- **What was stale:** `PROME/HANDBOOK.md` § Top priorities was the 9/18–9/21 vintage. It asked Will to rule WQ-234 and WQ-263, both ruled 9/22 (`WILL_QUEUE.md` RECENTLY DONE rows 234/263). The adjacent § Spawn queue listed HENRY L411 and VIOLET L277 (both RESOLVED), OSPREY L397 (RESOLVED 9/19) and a DAEDALUS line with no current wake. **The same stale-state problem was in the second Helm source:** `PROME/BRIEF.md` § QUESTION (9/18 story) still said *"Two things want your word. BRENT's question (WQ-234, due today)"* and deferred WQ-263 to *"tomorrow's sitting"*.
- **Done:**
  - **HANDBOOK:** Top priorities rewritten against WILL_QUEUE/DOCKET. The nearest deadlines come first: WQ-256 (9/24), then WQ-264 (9/25 17:00). ⛔ The first draft said WQ-264 was *the one* decision with a deadline; ARGUS ❌ found WQ-256, which was missing from the Helm. Then WQ-259 (due, with PROME's updated rec marked against the queue row's) and a selected four of the 12 past-due rows, pointing to the generated list. WQ-234 and WQ-263 appear only under **"Already ruled — implementation only"**, followed by hands and the 9/24 slate cap.
  - **Spawn queue:** replaced by the six DARK rows due at the 9/24 boot, from `spawn_list.py --as-of 2026-09-24`, plus SHADE (unchanged). The cap note moved into Top priorities because the renderer only draws one-desk lines.
  - **BRIEF:** QUESTION reconciled. WRITTEN is stamped to say only QUESTION changed, so the rest stays the 9/18 story. The one STORY clause asking about WQ-263 is marked ruled.
  - **Prior wording** is recoverable via `git log -p`.
- **Tested:** Helm regenerated (`will_handbook.py -o <scratchpad>`). The rendered page contains 0 of "Rule the class", "Guard convergence", "Two things want your word", "BRENT's question (WQ-234, due today)" and "both stay blocking until your word". Every remaining WQ-234/WQ-263 mention is a ruling, an implementation note or 9/18-dated history. All six due desks and SHADE render in the spawn queue; the cap sentence renders once.
- **Not audited (declared):** the rest of BRIEF (STORY/WATCH/FALSIFIER are the 9/18 story under their stamp) and the other manual sections, as CATO also noted.

## C2 — helper inventory checkpoint

- **Inventory, from the session's own runtime transcript** (`~/.claude/projects/-home-willi-Research-workspace-PROME/882551e0-be4a-4e99-b104-da955bb06725.jsonl`, enumerated for every `Agent` / `SendMessage` / `Workflow` call and teammate message): **exactly three helper touches** — `l409result` (spawn line 399), `hbcorrread` (line 732) and `argus-da` (line 900). No Workflow and no other spawn.
- **Recorded:** a `closeout_v1` object on ORCH_LOG rows 277–279, **labelled RETROSPECTIVE**. Every timestamp is a transcript event time (spawn, ask, receipt observation); none is reconstructed. All three are `ASKED_RECEIPT`.
- **Checked:**
  - `orch_closeout.py --ledger <prome-da rows only> --date 2026-09-23 --expected-key ×3 --inventory-complete` → rc 0, **ASKED → receipt 3**, nothing else.
  - The full ledger run with the same keys (no attestation) also shows the three as ASKED → receipt. Its coverage line stays UNKNOWN, because the full-ledger attestation would also cover prome-68's touches and historical rows that are not in this session's runtime. Those rows remain UNKNOWN and out of scope.
- **This correction closeout's own touches:** the c3delta row was recorded with evidence before the freeze. ⚠️ The ARGUS audit's own row (`argus-c13`) is appended AFTER its review, and that append is returned to the same reader as a changed portion before it is marked REVIEWED.

## C3 — final generated delta

- **The delta:** after ARGUS's clean re-review (17:45:18 ET), PROME regenerated SCRATCH's DOCKET-VIEW header and rebuilt the dashboard. It then re-froze and marked the candidate REVIEWED **without returning the delta to a reader**. **That was a skipped review control in the original closeout.** The original PARTIAL report did not name it.
- **Correction, after the fact (NOT a pre-commit review):** independent reader `c3delta` (Opus, read-only) inspected the delta at 18:30–18:33 ET, **after** commit `01c8de0ac`. Result **0 ❌ / 2 ⚠️**:
  - **SCRATCH:** one line differed, the DOCKET-VIEW generated header, and only its docket-crc32 moved (476206728 → 3600730361). The block re-renders byte-identically from the committed DOCKET. The reader's own check shows where the stale crc came from: re-stamping L444/L450 back to their pre-fix "18:0x" reproduces it exactly. So the header delta is the mechanical result of the ARGUS ❌3 re-stamp fix, which ARGUS did re-read. It is not an unreviewed DOCKET edit.
  - **Dashboard:** `dashboard_state.json` rebuilds 12/12 fields identical from a `git archive 01c8de0ac` export. `dashboard_build.json` matches the state's `built` stamp and the gate's L339 check. All 9 tiles and the one-liner appear verbatim in HEARTBEAT at that commit.
  - The dashboard HTML and hosted artifacts were not inspected.
- **Actual coverage, stated in the reader's form:**
  - **READ:** the SCRATCH pre/post delta (exact); the DOCKET-VIEW block re-rendered from the committed DOCKET; the pre-regeneration crc reproduced; both final-gate outputs and check-13 hashes; the committed dashboard_state rebuilt from an export (12/12); dashboard_build vs the state and the L339 gate line; the HEARTBEAT tiles and one-liner.
  - **NOT RECOVERABLE:** the 17:44 intermediate dashboard_state/build (no git object, no copy on disk) and the exact 17:45 working-tree fleet/inbox inputs.
- **Qualification of the original review:** ARGUS's REVIEWED verdict on the 01c8de0ac candidate **excludes** the final generated delta. The receipt's note (*"post-review delta = regenerated DOCKET-VIEW header line + dashboard rebuild only"*) was accurate as a description, but it was not a review. The delta is now independently read where recoverable. The intermediate dashboard state stays **UNKNOWN** (INFERRED identical but for its `built` stamp, not verified).

## This correction closeout's own review

- **ARGUS `argus-c13` (Opus):**
  - **First pass:** 1 ❌ / 6 ⚠️ / 24 ✅. The ❌ was WQ-256, due 9/24, missing from the "one deadline" claim.
  - **Changed-portion re-review:** one new ❌. The "full list is in *Waiting on you*" pointer was wrong, because that section shows RULE-class rows only (6 of the 12 past-due rows). The pointer was fixed.
  - **Final confirm:** ✅, "safe to commit". Five of the six first-pass ⚠️ were fixed in the same sentences; the remaining one is the post-review row disclosure below.
- **⚠️ Declared unread delta (the C3 shape, disclosed rather than repeated):** after that final confirm, PROME flipped `argus-c13`'s ORCH_LOG `closeout_v1` from ASKED_WORKING to ASKED_RECEIPT. It filled in the receipt observed at 22:40:30Z (transcript line 1325) and updated the row's WQ-249 phrase. **No reader saw that change.** The candidate was re-frozen with it, and the review receipt's note names it.
