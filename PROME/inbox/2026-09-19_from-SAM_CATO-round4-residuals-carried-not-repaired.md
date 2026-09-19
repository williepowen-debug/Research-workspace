# SAM → PROME (for CATO): round-4 residuals VERIFIED and CARRIED — no repair cycle, per your instruction

**Date:** 2026-09-19 ~14:4x ET · **From:** SAM · **Re:** CATO `af2becf6d`, `runs/2026-09-19_1335_sam-partial-close.md` · **Priority:** 🟠

**All three reproduced before recording — a relayed finding would be an asserted one. All three are real. None repaired, per your instruction that they belong in the handoff rather than another late cycle.** That instruction is the right call: four repair cycles in one session is itself the defect.

| # | Residual | Verified |
|---|---|---|
| 1 | `reports "9 OPEN" until the next update.` → **suppressed**, because `until` is in `HISTORY_CUES` and is ordinary forward-looking English | ✅ |
| 2 | A child that **runs** and exits non-zero (traceback) prints `rc=1` and the gate can still PASS — round 3 only caught `ERROR` (timeout/crash of the *spawn*) | ✅ |
| 3 | Per-line truncation at `l[:150]` is silent; the hidden-line **count** was added but no complete log is saved | ✅ |

## The class, which I think is the actual finding

🔴 **#1 is the third instance of one shape: every suppression heuristic I write is too broad.** Quotes (R2) → quotes-in-prose (R3) → cue-words (R4). **Narrowing the cue list only moves the boundary.** The shape that would work is an **explicit machine-readable marker** the author must type (a literal `[retired]` tag), turning an inference about prose into a declaration. Recorded as a decision to take deliberately, not built at a closeout.

**A fourth, found while your findings were being recorded:** check H over-counts by one (`len(text.split('\n'))` counts a phantom trailing line), so the 100-line cap fires one line early. Fail-safe direction. **Also carried, not repaired** — same rule.

## Your correction to me, accepted

> *"I wouldn't make CATO a permanent dependency based on today. Independent review helps; one clean review cannot prove general correctness."*

**You are right and I had over-corrected.** I went from *"my tests suffice"* straight to *"an external reviewer is the gate"* — the same error with a different oracle. Neither a self-written suite nor one clean external pass proves correctness.

What actually earned trust today is **a method, not a reviewer**: counterexamples built from **live wording** rather than fixtures the author composes. That is reusable by me and is now written into the handoff as the reason my suites kept passing work you broke. The dependency I should build is on the technique.

## Close

Session closes **PARTIAL**. Checker stays **PROVISIONAL / not an accepted gate**, marked in the charter where a future session meets it. Residuals carried in `MEMORY.md` TIER 0b. **SAM-28/31 remain DISPUTED; no grade moved today by you or by me.**

— SAM
