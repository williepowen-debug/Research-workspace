# Harness Audit Sweep — Playbook (DAEDALUS recurring #4)

**Owner:** DAEDALUS · **Cadence:** every **90 days** — **AND unconditionally on any model upgrade** (the boot/closeout instruction layer is calibrated to a model's failure modes; a new model re-opens every deletion/rewrite call) · **Registered:** 2026-07-22 (Will-ruled — the recurrence commitment from the 7/7 audit had lost its registry slot to the Falsification sweep and was tracked nowhere) · **Registry:** `sweeps/REGISTRY.tsv` · **First run:** 2026-07-07.

**What it does:** re-tests every agent's harness layer (CLAUDE.md boot/closeout steps, standalone CLOSEOUT docs, PROME BOOT/CLOSEOUT) against the deletion criterion ratified 7/7: *keep a step only if it is (a) an ACTION/behavior-gate, (b) not mechanizable, and (c) not owned elsewhere* — re-tested per model upgrade. Produces a strike-list (delete), rewrite-list (compress/fix), and disposition per file.

**Method + criterion detail:** `HARNESS_AUDIT_2026-07-07.md` (the first run IS the playbook's worked example — method §1-2, criterion §3, strike/rewrite lists §4-5). Cite, don't restate.

**Authority:** detection autonomous/read-only; ALL harness edits are approval-gated (an agent's boot doc is maximally load-bearing) — batch to one changelist per the 7/7 pattern (S1-S6 strikes were one Will approval). Live agents → task packets.

**Self-inclusion (PAT-050):** DAEDALUS's own CLAUDE.md SPAWN/closeout steps are in scope.

## Run Log
| Date | Scope | Findings | Dispositions |
|---|---|---|---|
| 2026-07-07 | 33 CLAUDE.md + PROME BOOT/CLOSEOUT + 3 standalone closeouts | strike-list S1-S6, rewrite-list R1-R5, 11 roadmap dispositions | S1/S4 output-canon consolidation + S2 git cite-don't-restate applied 7/8; R1 OTTO routed; R2 root git rewrite = Will/PROME lane; full record `HARNESS_AUDIT_2026-07-07.md` |
