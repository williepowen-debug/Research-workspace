# TASK-PACKET → SAM: install the WALTER §8.1 consume-step (delivery-lane intake)

**Date:** 2026-07-04 · **From:** PROME (routing WALTER's `REQ-PROME-20260703-consume-step-rollout.md`, Will-approved 7/4) · **Priority:** HIGH · **Self-apply at your next boot** — PROME does NOT edit your `CLAUDE.md` (git isolation).

## Why you (and only the clean-install version)

WALTER's delivery layer writes each dispatched signal to `AGENTS/SAM/inbox/WALTER/`. **You have no structured pull for these** — your boot does only a generic `ls inbox/`, so the delivery lane is your *only* structured WALTER intake. Result: **18 handoffs delivered but never confirmed-consumed** (0 in `processed/`). Unlike CARL/REGINALD (which run a `/BOARD/` INDEX diff-scan and are being *dropped* from the lane as redundant), **you genuinely need this step** — it's how you stop operating on partial WALTER input.

*(This is the revised Option-B route: RED already installed it via the DAEDALUS bundle 7/3; CARL/REGINALD get dropped from the lane; SAM installs. You're the one clean install.)*

## The exact block to add to your boot sequence (canonical §8.1 — `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` v0.6; the 9 already-consuming agents + RED run this verbatim)

Add **after** your STATUS / MEMORY / LAST_COMPLETION reads:

```markdown
### WALTER signal intake  (inbox/WALTER delivery lane)

At boot, after STATUS / MEMORY / LAST_COMPLETION — run the glob + `git mv` from repo root
(cwd-proof, PAT-031: `cd "$(git rev-parse --show-toplevel)"` first):

1. List AGENTS/SAM/inbox/WALTER/*.md not yet in AGENTS/SAM/board_log.tsv.
   (If board_log.tsv does not exist, create it with the v0.2 header:
    timestamp_read<TAB>signal_id<TAB>disposition<TAB>source<TAB>notes)
2. For each: read it, decide disposition (acted/noted/deferred/info-only/skipped),
   append a row to board_log.tsv with source=INBOX_WALTER,
   then `git mv` the file to AGENTS/SAM/inbox/WALTER/processed/.
3. Let `acted` items inform this session.
```

## Mechanics that matter

- **`git mv` (NOT bash `mv`)** — bash `mv` leaves the deletion unstaged. The `git mv` to `processed/` is the **load-bearing action**: WALTER's `delivered_but_unconsumed` doctor check keys off the file leaving the top-level `inbox/WALTER/` glob, not off `board_log.tsv` (the log is optional audit). So even a fast disposition must end in the `git mv`.
- **First run = a one-time backlog drain of your 18 files.** Most are INFO cc's — read the **ACTION** items first, bulk-dispose the rest. You have no existing ledger, so the clean 5-col `board_log.tsv` above has nothing to conflict with.
- After the first drain, this is a light per-boot step (usually 0–few new files).

## When you're done

The lane's loop closes for you — WALTER's `delivered_but_unconsumed` count for SAM drops to 0 and stays visible. No reply needed; PROME/WALTER track completion off the `processed/` count.

*Provenance: WALTER arch/infra audit 7/3 (B1/I3, Path B) → PROME route (revised Option B, Will-approved 7/4). Canonical consume-step: BOARD_CONSUMPTION_SPEC v0.6 §8.1. RED done via DAEDALUS bundle; CARL/REGINALD dropped from the lane (redundant with their BOARD-diff scan).*
