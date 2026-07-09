# TASK-PACKET → REGINALD: install a WALTER delivery-lane drain-step (KEEP the lane)

**Date:** 2026-07-04 · **From:** PROME (routing WALTER's reconciled `REQ-PROME-20260703-consume-step-rollout.md`, Will-approved 7/4) · **Priority:** HIGH · **Self-apply at your next boot** — PROME does NOT edit your `CLAUDE.md` (git isolation).

## Why you KEEP the lane (unlike CARL)

WALTER's delivery layer writes per-recipient handoffs to `AGENTS/REGINALD/inbox/WALTER/`. Your existing `/BOARD/` scan (step 9b) is **tiered/selective**, so it does *not* catch everything the lane delivers. WALTER's 7/4 reconciliation found **1 un-dispositioned ACTION your tiered scan missed**:

> **SIG-W-20260704-004** — Bank OZK took title to the Seattle U-District "Chapter Buildings" (I + II, ~394K SF office/life-science) via ground-lease **deed-in-lieu**; the two "signed LOI for recap" credits (Office ~$76M + Life-Sci ~$50M ≈ **$126M current exposure**) **realized** — recap failed, OZK holds them as REO. Recorded wk-ending 7/2.

That miss is exactly why REGINALD **keeps the lane + installs a drain-step** — whereas CARL (complete whole-INDEX scan, 0 misses) gets dropped. Your `/BOARD/` scan and the delivery lane are **complementary**: the lane guarantees per-recipient handoffs reach you even when the tiered scan's scope skips a single-name like OZK. **26 handoffs backlogged (0 processed).**

## The fix — a drain-step COMPLEMENTARY to your step 9b (not a replacement)

Add to your boot, after STATUS/MEMORY, distinct from step 9b (9b = shared `/BOARD/` INDEX; this = your per-recipient `inbox/WALTER/` handoffs). **Adapted to log into your EXISTING 11-col `board/BOARD_LOG.tsv` — do NOT create a parallel 5-col `board_log.tsv`:**

```markdown
### WALTER signal intake  (inbox/WALTER delivery lane) — complements the step 9b /BOARD/ scan

At boot, after STATUS / MEMORY — run the glob + `git mv` from repo root
(cwd-proof, PAT-031: `cd "$(git rev-parse --show-toplevel)"` first):

1. List AGENTS/REGINALD/inbox/WALTER/*.md whose SIG-W id is not yet in
   board/BOARD_LOG.tsv (BOARD_ID column).
2. For each: read it, decide disposition, append a row to your EXISTING 11-col
   board/BOARD_LOG.tsv (set Channels_Touched=INBOX_WALTER), then
   `git mv` the file to AGENTS/REGINALD/inbox/WALTER/processed/.
3. Let acted items inform this session.
```

## Mechanics that matter

- **`git mv` to `processed/` is the load-bearing action** — WALTER's `delivered_but_unconsumed` doctor check keys off the file leaving the top-level `inbox/WALTER/` glob, not off the log. So even a fast disposition must end in the `git mv`.
- **First run = drain your 26 backlog. Read `SIG-W-20260704-004` (OZK deed-in-lieu) FIRST** — it's the ACTION your tiered scan missed, and it feeds your **OZK Q2 read (now Tue 7/21**, confirmed — corrected today from the mis-docketed 7/16). The transfer recorded wk-ending 7/2 = a **Q3 subsequent event**, not an in-Q2 charge-off → watch the Q2 Chapter-Buildings **specific-reserve build** against your own pre-registered **$15-30M fail-band** ($20M mid already in the $628.5M ACL); it firms the OZK bear leg but is not a provision shock.
- **`SIG-W-20260704-005`** (S2 Capital $400M MF-fund dissolution / $311M N-Texas foreclosure) is also in your inbox as **info** — bank-lender exposure leg is Citibank + U.S. Bank Trust.

*Provenance: WALTER arch/infra audit 7/3 (B1/I3) → 7/4 reconciliation (REGINALD tiered-scan → 1 ACTION miss = keep-lane) → PROME route, Will-approved. Canonical consume-step: BOARD_CONSUMPTION_SPEC v0.6 §8.1, adapted to REGINALD's 11-col ledger.*
