---
name: coldread
description: Blind cold-read of one PROME-owned surface after a re-base or restructure, before commit — spawns the `coldreader` agent, scores it, applies the flags, re-runs until zero ❌ or the WQ-165 two-read stop (basis-and-pointer class only). Use for "cold read this", "cold reader pass", after any HEARTBEAT re-base, root CLAUDE.md edit, SCRATCH rewrite, or a proposal going to Will/RAV.
user-invocable: true
---

# /coldread — blind cold-reader pass (PROME)

The reader knows nothing by design. Its value is that ignorance. Do NOT brief it on the system.

1. **Spawn `coldreader`** with exactly: the artifact path, and (optionally) the list of claims you expect it to carry (numbered). Nothing else. `isolation` not needed — it is read-only.
2. **Score** the report: `SCORE: ok/N · ⚠️ n · ❌ n`. A ❌ = internal contradiction or dead pointer — must be fixed. A ⚠️ = a stranger cannot tell — fix if the fix is one line (gloss the term, add the unit/basis/date, replace "row N" with "WQ row N"), otherwise judge.
3. **Apply fixes at the source** (owner surface first, then the view), never by annotating the reader's flag into the file.
4. **Re-run** the reader on the fixed file if there was any ❌. **Stop rule (WQ-165, Will 2026-09-03 08:45, verbatim *"yes approved implement that fix please"*): stop at ❌ = 0, OR after two consecutive reads whose ❌ are ALL of the basis-and-pointer class** — a figure that is right but lacks its basis, vintage, unit or perimeter; a pointer, item number or cross-reference that resolves to the wrong place — **with no ❌ of the action class** (a reader would place, cancel, chase or calendar something wrong: an executed order listed as live, a dead event on the calendar, a wrong position count, a wrong unit against a bar). An action-class ❌ ALWAYS forces another pass. When stopping on the two-read branch, fix the last read's ❌ unreviewed and DECLARE them plus every ⚠️ as residue in the commit message. Record the pass counts `❌ a → b → c` in the commit message and the SCRATCH executed-list. Reason → `PROME/CLOSEOUT.md` Chunk 1 (blind-reader bullet).
5. **Execution mode (added 8/29 — use it AFTER a reading pass reaches ❌ = 0 on any procedure file):** spawn a `general-purpose` stranger (not `coldreader`, which is read-only by contract) with ONLY the file path, the launch directory (`PROME/` for PROME skills), and the rule *"execute it as written, read-only, no commits; at each step record PASS if the pointer let you act without guessing, FAIL with what was missing"*. A reading pass verifies pointers; only execution verifies executability — 8/29: four reading passes → 0 ❌, two executing strangers → 6 defects, five in the manuals pointed at. Fix at the source the pointer lands on, never by adding a sentence to the runner.
6. Two readers in one day is normal (WQ-120 and WQ-121 both went 16/16 on pass 2). A reader that scores 100% on pass 1 of a large re-base is suspicious — check it actually enumerated the claims.
