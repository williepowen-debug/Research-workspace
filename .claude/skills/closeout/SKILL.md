---
name: closeout
description: PROME session closeout runner — the execution order for `PROME/CLOSEOUT.md` (which stays canonical). Use on "close out", "lets close out", before /clear or a machine switch, or a long pause. Picks the tier, writes each fact once, freezes and audits the finished candidate, gates, then reports which of committed/pushed/published was reached.
user-invocable: true
---

# /closeout — ordered index over `PROME/CLOSEOUT.md`

An **index in execution order**, nothing more. Every rule, tier, threshold and recipe lives in `PROME/CLOSEOUT.md`; conditional procedures live in `PROME/CLOSEOUT_PROCEDURES.md`. On any conflict the manual wins — fix this index rather than working around it.

0. **Pre-closeout + tier** → CLOSEOUT.md "Pre-closeout" (items 1–4; item 3 applies at ANY tier). Take the clock per BOOT.md step 0 before writing any stamp.
0b. **Publication prerequisites, NOW and not at the render** → CLOSEOUT.md § Delivery. Check the Deck explainer coverage, and **view the live artifact this session** so the republish cannot be refused at step 10. An unmet prerequisite is decided here.
1. **Write each fact ONCE** → CLOSEOUT.md § Boot↔Closeout symmetry — ONE HOME PER FACT. The targeted-update test applies at **every tier**: *does the boot path already reach it?* Registered ⇒ do not restate. Nothing changed in a column ⇒ a **stated no-op**.
2. **Steps 1–7 of § The routine, in order** → GATES/DOCKET first + view · WILL_QUEUE + ledger + view · SCRATCH/STATUS/ACTIVE_DECISIONS/HEARTBEAT/HANDOFF · memory · residual triggers · root steps 1b–1e · Helm/Deck sources + Fleet-Ops build. **Step 7 is the last step that may edit anything.**
3. 🔴 **FREEZE, then AUDIT** → CLOSEOUT.md § The routine step 8:
   `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/argus_scope.py --record-review`
   then spawn `argus`; apply ❌ only, ⚠️ → residue, RUN-LOG row. ⛔ **Any ❌ fix that changes the candidate ⇒ re-review the changed portion, regenerate affected outputs, `--record-review` again.**
4. **FINAL gate** → step 9: `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/prome_gate.py closeout` — includes the BLOCKING `ARGUS review manifest (content, not paths)`. rc=1 ⇒ fix, regenerate derived artifacts, re-run the FULL gate.
5. **Render + publish** → step 10.
6. **Commit + push + verify** → step 11, including `python3 PROME/tools/argus_scope.py --verify-review` reading **UNCHANGED** after the commit, and the verbatim push receipt.
7. **ARGUS baseline** → step 12, AFTER the commit.
8. **Report** → CLOSEOUT.md § Delivery: name **committed · pushed · published** separately; two of three is **PARTIAL** with its concrete blocker.
