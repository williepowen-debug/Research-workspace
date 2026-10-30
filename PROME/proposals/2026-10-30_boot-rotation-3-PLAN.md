# WQ-552 A — BOOT.md rotation #3 — PLAN (Will 2026-10-30 12:15 ET, verbatim *"okay go ahead with 552 A"*)

**Authority:** WQ-552 rec A (four units) approved; row text in `PROME/WILL_QUEUE.md` RECENTLY DONE. **Owner:** PROME (BOOT.md and BOOT_MODULES.md are PROME manuals). **Reads:** ONE plan read of THIS file (Sonnet coldreader) → fix ❌ only, ⚠️ to the residue block → the move in ONE edit set → ONE result read at the commit → declared residue (Review budget; the two prior rotations' shape). **Process-ceiling accounting:** one process-class change (Will-approved), the session's third.

## Measurements (instrument: `python3 -c 'import zlib…'` over the exact bytes at HEAD a6ba1db40; re-measured after the move)
| Unit | Source span in `PROME/BOOT.md` | Bytes | crc32 | Destination |
|---|---|---|---|---|
| BANNERS | lines 6 and 8 (the two bold banner paragraphs; the blank lines 5/7/9 collapse to one) | 766 | 3574064564 | CONSOLIDATED into step 3b (one sentence each + ruling pointers); verbatim prior text → `BOOT_MODULES.md` § Rotated banners (2026-10-30) |
| NONNEG | `## Non-Negotiables` heading through the line before the `---` separator (lines 16–25) | 990 | 816980847 | REPLACED by a pointer section (text below); verbatim prior text → `BOOT_MODULES.md` § Rotated Non-Negotiables (2026-10-30) |
| LOGREAD | inside step 5's ⚡ ONE-SHOT GATE bullet: from `**Log-read contract` through `Acquisition details: \`PROME/tools/SESSION_PILOT.md\`.` | 2218 | 3869686084 | MOVED verbatim → `BOOT_MODULES.md` § Gate log-read contract; pointer sentence left in place |
| MEMORIES | `## Boot-class fleet memories` heading to EOF (lines 108–121) | 2060 | 2981797587 | MOVED verbatim → `BOOT_MODULES.md` § Boot-class fleet memories; step 4b rewritten to carry the five every-boot hooks as one line |

Sum leaving the boot-read path ≈ 6034 B before pointers; expected size after = measured by `PROME/tools/measure.py` at the result read, target < 22,785 B (70% of 32,550). READS.tsv: BOOT.md stays `whole`; BOOT_MODULES.md stays `scoped` (not cap-bearing) — no registry change.

## NEW texts (exact)
### N1 — step 3b: APPEND to the end of the 3b bullet (same line):
` **Standing banners folded here (WQ-552 A, 2026-10-30; the banners above the Boot Sequence were removed in rotation #3 — the rulings are unchanged):** Helm RETIRED (WQ-461, 2026-10-19; `PROME/proposals/2026-10-19_wq461-helm-retired-RULED.md`) — no routine dashboard generation, presentation upkeep, hosted reads or publication; the boot book line, WALTER intake and decision checks remain active. Decision Deck PAUSED BY WILL (WQ-460, 2026-10-19; `PROME/proposals/2026-10-19_wq460-decision-deck-paused-RULED.md`) — pickup, upkeep, builds and publication suspended until explicit resume and reconciliation; the hosted page is not disabled and unseen taps remain UNKNOWN.`
### N2 — replaces the whole Non-Negotiables block (heading through the line before `---`):
```
## Non-Negotiables → their homes (WQ-552 A, 2026-10-30)

Every non-negotiable this file once restated binds from its canonical home, each of which loads before this manual: root `CLAUDE.md` § Critical Rules (#4 live prices · #5 Will approves every trade · the Git Protocol · position-truth canon) · `PROME/CLAUDE.md` § Ask First (external sends, shared/root edits, no agent edits without Will's word, spawn tiers) · `PROME/GIT_COORDINATION.md` (another agent's local/branch work) · `PROME/ORCHESTRATION_PLAYBOOK.md` + `PROME/COMPLETION_SPEC.md` (more than one agent). Two boot-local reminders survive here: **repeated same-day respawns** do not rewrite HEARTBEAT or churn state for hygiene alone (a real market/system event or a user decision is required); **FRED citations name observation dates, not retrieval dates.** The block's verbatim prior text: `PROME/BOOT_MODULES.md` § Rotated Non-Negotiables (2026-10-30).
```
### N3 — replaces the LOGREAD span inside the ⚡ bullet:
`**Log-read contract → `PROME/BOOT_MODULES.md` § Gate log-read contract (verbatim, moved 2026-10-30 under WQ-552 A).** The one sentence that stays here: read `gate.txt` to EOF with the bounded reader; a named log is read ONLY as drill-down on a ⚠️/❌ line whose preview does not name the item PROME must act on; `--sessions-json` snapshots are scoped evidence, never a desk-absence proof — the full contract (WQ-249 line, spawn-list line, orch-compact view, rc meanings, snapshot coverage) is in the module.`
### N4 — replaces line 63 (the 4b bullet) whole:
`   - **4b. Read the Boot-class fleet memories** → `PROME/BOOT_MODULES.md` § Boot-class fleet memories (moved verbatim 2026-10-30, WQ-552 A). The every-boot five, kept here so the read survives the move: `finding_boot_sweep_macro_regime_context` (check principals, not only feeds) · `finding_inbound_lane_is_the_falsification_channel` (a lane carrying a falsifier is boot-mandatory) · `finding_gitignored_private_drop_boot_surfaced` (gitignored drops are invisible to git status) · `feedback_front_load_planning` (one planning pass, Will batch-approves) · `finding_display_filter_gating_safety_net` (a forward filter gates the past-due net). Already-mechanized pointers and the trigger-keyed groups are in the module, not acted on at boot. Full lessons: `memory/auto/<slug>.md`.`
### N5 — BOOT.md line 6–8 banners: DELETED (their content lives in N1); one blank line remains between the header block and the Context-loading paragraph.
### N6 — `PROME/BOOT_MODULES.md`: four sections APPENDED after § Resume after a restart, each introduced by one italic provenance line (`*Moved verbatim from PROME/BOOT.md 2026-10-30 under WQ-552 A (rotation #3); crc32 <n> over the moved text; plan PROME/proposals/2026-10-30_boot-rotation-3-PLAN.md.*`): `## Gate log-read contract` (LOGREAD verbatim) · `## Boot-class fleet memories` (MEMORIES verbatim, its own heading line replaced by this section heading, body byte-identical) · `## Rotated Non-Negotiables (2026-10-30)` (NONNEG verbatim) · `## Rotated banners (2026-10-30)` (BANNERS verbatim). Header line 1 parenthetical gains `; M7 rotation #3 (log-read contract · fleet memories · Non-Negotiables · banners) 2026-10-30 — plan PROME/proposals/2026-10-30_boot-rotation-3-PLAN.md`.
### N7 — pointer-adjusted edits (invariant 6 carve-out):
| # | File · line | Before | After |
|---|---|---|---|
| P1 | `PROME/.claude/skills/boot/SKILL.md` and `.claude/skills/boot/SKILL.md` (identical; parity gate), item 3 | `BOOT.md step 5 owns the gate's meaning and log-read contract (run-directory identity, retry guard, **`gate.txt` to EOF; a named log only as drill-down on a flagged line whose preview does not name the item** — the log-read contract, change 2026-10-16)` | `BOOT.md step 5 owns the gate's meaning (run-directory identity, retry guard, **`gate.txt` to EOF; a named log only as drill-down on a flagged line whose preview does not name the item**); the full log-read contract is `PROME/BOOT_MODULES.md` § Gate log-read contract (moved 2026-10-30, WQ-552 A)` |
| P2 | same two files, item 4 | `step 4b (Boot-class fleet memories)` | `step 4b (the five every-boot fleet-memory hooks; the full section is `PROME/BOOT_MODULES.md` § Boot-class fleet memories)` |
| P3 | `PROME/BOOT.md` header line 2 `**Updated:**` | as is | prefix `2026-10-30 12:xx ET (rotation #3, WQ-552 A — four blocks to BOOT_MODULES; plan …boot-rotation-3-PLAN.md). Prior:` and keep the existing latest stamp as the one prior (the line keeps the latest and at most ONE prior) |

## Invariants (what the reads check)
1. Each moved block appears in BOOT_MODULES byte-identical to its source span (crc32 above = crc32 of the destination body, heading line excluded for MEMORIES as stated).
2. No rule changes meaning: N1 restates the two rulings with their record pointers; N2 names the homes that already bind and keeps the two boot-local reminders verbatim in substance; N3 keeps the one operative sentence of the contract; N4 keeps the five every-boot hooks by slug.
3. The /boot runner's two copies stay identical (parity gate) and point at the new homes (P1, P2).
4. READS.tsv unchanged; BOOT_MODULES remains `scoped`.
5. `python3 PROME/tools/measure.py PROME/BOOT.md` < 22,785 B after the move; `scripts/read_cap_check.py --agent PROME` shows rotation_due=0.
6. Nothing else in BOOT.md changes: `git diff --numstat` shows only the spans named here plus P3.
7. The execution order paragraph and every step number are unchanged (the runner cites them).

## Plan read / Result read / Declared residue
Plan read: PENDING. Result read: PENDING. Residue: (after the reads)
