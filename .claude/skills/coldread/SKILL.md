---
name: coldread
description: Blind cold-read of one PROME-owned surface after a re-base or restructure, before commit — spawns the `coldreader` agent, scores it, applies the flags, re-runs within `PROME/CLAUDE.md` § Review budget (WQ-165's early stop inside it). Use for "cold read this", "cold reader pass", after any HEARTBEAT re-base, root CLAUDE.md edit, SCRATCH rewrite, or a proposal going to Will/RAV.
user-invocable: true
---

# /coldread — blind cold-reader pass (PROME)

> ⛔ **WITHHELD (Will 2026-09-26 20:16 ET, L511):** steps 2, 4 and 5 below were changed after the final independent read and are UNVERIFIED — do not rely on their wording; **`PROME/CLAUDE.md` § Session Process Controls → Review budget governs**. The read-only execution check of this runner is INCOMPLETE (4 of 6 steps passed on the version checked). Record `PROME/proposals/2026-09-26_L511-review-budget-RULED.md`.

The reader knows nothing by design. Its value is that ignorance. Do NOT brief it on the system.

1. **Spawn `coldreader`** with exactly: the artifact path, and (optionally) the list of claims you expect it to carry (numbered). Nothing else. `isolation` not needed — it is read-only.
2. **Score** the report: `SCORE: ok/N · ⚠️ n · ❌ n`. A ❌ = internal contradiction or dead pointer — fix it within the episode's budget, or withhold it per `PROME/CLAUDE.md` § Review budget. A ⚠️ = a stranger cannot tell — declare it as residue (WQ-178), unless the fix is a one-word typo; **but a ⚠️ or ❌ that could materially change a decision or instruction is withheld whatever its grade** (withholding follows consequence, not class — `PROME/CLAUDE.md` § Review budget).
3. **Apply fixes at the source** (owner surface first, then the view), never by annotating the reader's flag into the file.
4. **Re-run** the reader on the fixed file only if there was a ❌ AND the episode's budget allows another read. Budget, early stop and disposition at an early stop or the limit → `PROME/CLAUDE.md` § Session Process Controls → Review budget; class definitions → `PROME/CLOSEOUT_PROCEDURES.md` § Byte-flow. Record the pass counts `❌ a → b → c` and the episode's read count in the commit message.
5. **Execution mode (added 8/29 — use it on any procedure file after the reading passes — at ❌ = 0, or in the third read under the procedure exception, whichever comes first):** spawn a `general-purpose` stranger (not `coldreader`, which is read-only by contract) with ONLY the file path, the launch directory (`PROME/` for PROME skills), and the rule *"execute it as written, read-only, no commits; at each step record PASS if the pointer let you act without guessing, FAIL with what was missing"*. A reading pass verifies pointers; only execution verifies executability — 8/29: four reading passes → 0 ❌, two executing strangers → 6 defects, five in the manuals pointed at. Fix at the source the pointer lands on, never by adding a sentence to the runner. The execution pass is an independent read and counts inside the episode's budget; when it may occupy the third read, and what stays PENDING · UNVERIFIED when it cannot run → `PROME/CLAUDE.md` § Review budget (Procedure exception).
6. Two readers in one day is normal (WQ-120 and WQ-121 both went 16/16 on pass 2). A reader that scores 100% on pass 1 of a large re-base is suspicious — check it actually enumerated the claims.
