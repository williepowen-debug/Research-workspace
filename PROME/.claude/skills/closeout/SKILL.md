---
name: closeout
description: PROME session closeout runner — the execution order for `PROME/CLOSEOUT.md` (which stays canonical). Use on "close out", "lets close out", before /clear or a machine switch, or a long pause. Picks the tier, writes each fact once, freezes and audits the finished candidate, gates, then reports which of committed/pushed/published was reached.
user-invocable: true
---

# /closeout — ordered index over `PROME/CLOSEOUT.md`

An **index in execution order**, nothing more. Every rule, tier, threshold and recipe lives in `PROME/CLOSEOUT.md`; conditional procedures live in `PROME/CLOSEOUT_PROCEDURES.md`. On any conflict the manual wins — fix this index rather than working around it.

0. **Pre-closeout + tier** → CLOSEOUT.md "Pre-closeout" (items 1–4; item 3 applies at ANY tier). Take the clock per BOOT.md step 0 before writing any stamp.
0b. **Publication prerequisites, NOW and not at the render** → CLOSEOUT.md § Delivery. Check the Deck explainer coverage, and **view the live artifact this session — for the Helm also list its files** (§ Delivery, Pre-closeout item 5) — so the republish cannot be refused at step 11. An unmet prerequisite is decided here.
1. **Write each fact ONCE** → CLOSEOUT.md § Boot↔Closeout symmetry — ONE HOME PER FACT. The targeted-update test applies at **every tier**: *does the boot path already reach it?* Registered ⇒ do not restate. Nothing changed in a column ⇒ a **stated no-op**.
2. **Steps 1–7 of § The routine, in order** → GATES/DOCKET first + view · WILL_QUEUE + ledger + view · SCRATCH/STATUS/ACTIVE_DECISIONS/HEARTBEAT/HANDOFF · memory · residual triggers · root steps 1b–1e · **then ALL generation: Helm/Deck sources, `fleet_dashboard.py`, `will_handbook.py`, `decision_deck.py`.** ⛔ Renders write tracked snapshot files, so generation is the last step that may write any file **inside the reviewed candidate** — **step 7, before the freeze.** (Step 8's review receipt and step 12's baseline record are tracked too, but `RECEIPT_PATHS` excludes both from every manifest, which is why they may run later.)
3. 🔴 **FREEZE, then AUDIT** → step 8:
   `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/argus_scope.py --record-review`
   (consumed a packet this closeout by `git mv` into `PROME/inbox/processed/`? add `--consumed-move <ORIGIN> <DEST>` per pair, at every re-freeze → CLOSEOUT.md step 8; ⛔ NOT VERIFIED — the live condition is DOCKET L473's disposition cell (successor read L488); commit consumed packets separately before the candidate instead)
   spawn `argus`; apply ❌ only, ⚠️ → residue, RUN-LOG row; then `python3 PROME/tools/argus_scope.py --mark-reviewed "<one line>"`. ⛔ **Freezing writes FROZEN; only the audit earns REVIEWED.** Any ❌ fix ⇒ re-review the changed portion, regenerate, re-freeze, re-mark.
4. **FINAL gate WITH THE TIER** → step 9: `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/prome_gate.py closeout --tier <bounce|light|standard|heavy>`. standard/heavy: missing, unevaluable or merely-FROZEN review is BLOCKING.
5. **Commit → VERIFY → push** → step 10, in that order: `commit_check.py commit --stage -F <msgfile> -- <exact paths>` (⛔ **no `--push`**), then `python3 PROME/tools/argus_scope.py --verify-review --ref HEAD --paths <the same exact paths>`, then `bash scripts/safe-push.sh` **only on rc 0**. Verifying after a push detects an unreviewed delivery that has already shipped.
6. **Publish the verified artifacts** → step 11 (generated at step 7, verified at step 10).
7. **ARGUS baseline** → step 12, AFTER the commit.
8. **Report** → CLOSEOUT.md § Delivery: name **committed · pushed · published** separately; two of three is **PARTIAL** with its concrete blocker.
