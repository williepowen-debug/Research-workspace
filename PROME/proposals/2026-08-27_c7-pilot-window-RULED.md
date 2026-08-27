# C7 Pilot Window — RULED

**Date:** 2026-08-27 ~12:2x ET (16:2xZ), Will in-session (same-day reboot after the EIGHT-DESK-DAY closeout)
**Chain:** approved-in-principle + day-boundary rider waived in-session 2026-08-27 AM (packet v2 ruling line) → sitting deferred on Will's word *"we will work on this directly in the next reboot"* → THIS reboot.

## The ruling

- Will, in-session ~16:16Z: **"can we just do the pilot now?"** — the go word for the sitting.
- Window options put to Will with exact half-open UTC bounds; **Will selected: `[2026-08-27T16:30:00Z, 2026-08-27T18:00:00Z)`** (12:30–2:00 PM ET, 2026-08-27). This selection is the ruled window and is written verbatim into the activation document (runbook step 2).

## Step-0 record (preconditions, run 16:23Z)

- All six pinned hashes **re-verified byte-exact** (CMD-…033 · CMD-…034 · actors.json · capability-grants.json · custody-policy.json — values per `KERNEL/GATE_C_C7_RUNBOOK.md`); source commit `1d9400425` present.
- Staged index **EMPTY**; `KERNEL/` and `AGENTS/SAM/outbox/kernel/` **clean**.
- **Deviation, Will-ruled PROCEED (~16:24Z):** tree not fully clean — sam-59 (live session) held 3 unstaged in-flight files in its own `AGENTS/SAM/` working set (`METSUKE_MEMORY.md`, `KURA.md`, `KURA_MEMORY.md`), unrelated to every custody path. Put to Will with the substance stated (nothing staged, custody paths clean, exact-pathspec commits throughout); **Will selected "Proceed"**; deviation recorded here per the sitting rule (stop condition ⇒ no disposition without Will).

## Sitting execution

Per `KERNEL/GATE_C_C7_RUNBOOK.md` steps 0–9 verbatim. Writer = PROME (custody primary). C8 closeout reviewer = RED or DAEDALUS, never PROME (ruled 8/26).
