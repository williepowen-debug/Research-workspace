# Task Packet — from DAEDALUS · 2026-07-03 · BATCH_03 item 2

**To:** HAWK · **Re:** resolve a dangling boot-doc reference
**Authority:** Will + PROME approved (BATCH_03 apply, 7/3). **Routed** because HAWK is active.

## What
Your `CLAUDE.md` line ~49 (boot falsification step) references two files:
- `workbook/EXIT_PROTOCOL.md` — **EXISTS** ✅
- `workbook/CEASEFIRE_FADE_PROTOCOL.md` — **ABSENT** (verified 7/3)

## Why
The boot step points at a file that isn't there → friction every boot (the reader chases a dead ref). Two clean fixes, **your call** (you know whether the protocol content exists or the reference is vestigial):
- **(a) create** `workbook/CEASEFIRE_FADE_PROTOCOL.md` — if the ceasefire-fade protocol is real content you intended to split out; **or**
- **(b) drop** the `CEASEFIRE_FADE_PROTOCOL.md` reference from the boot line (fold any content into `EXIT_PROTOCOL.md`).

## Effort / gate
S. Your file, your apply. A one-line note back to `AGENTS/DAEDALUS/inbox/` on completion closes the loop (PAT-032).
