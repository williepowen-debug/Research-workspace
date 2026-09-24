# BOND RECEIPT — 2026-09-24 (Thu) SECOND session, ~15:07 → ~16:4x ET (Will boot)

*(Session 1 `bond-b0` ~13:00→14:2x receipt is in git: `git show d93987642:AGENTS/BOND/RECEIPT.md`.)*

| Item | Disposition |
|---|---|
| **Tasked** | Will: boot + "report on anything owed" (delivered in chat) → "clear the cleanup and read FR2004" |
| **Inbox** | 0 new (WALTER lane empty; general inbox empty) |
| **Boot checks** | pull: 0 behind, nothing to pull (CARL/ORACLE dirty, not ours, untouched) · docket_check rc0 (VERIFIED ONLY THROUGH 9/29; 9/30→10/15 blind span UNVERIFIED) · corrections rc0 · boot_recompute rc1, 14 findings → **1** after fixes |
| **Cleanup** | `GATE-TERRY-007` struck (TERRY closed MOOT) · DFII10 two-basis label · `KB-BND-314` marked FIXED · TRADE Next Review pruned (7 resolved bullets) · WATCH_DATES 4 rows retired + 004 count 20x |
| **Checker fixes** | `watchers.py`: nested-supersession + banner-line guard; nearest-preceding-gate distance attribution · `boot_recompute.check_fr2004` uses the block guard · selftest 15/15, new fixtures fail on old code (mutant-checked) |
| **Data** | TP re-pulled: ACM 0.6454 [9/23], KW 0.9595 [9/18] (`KB-BND-325`) · **FR2004 as-of 9/16** read at publication 16:16 ET (`KB-BND-326`) · open method question (`KB-BND-327`) |
| **Files written** | STATUS · TRADE · SCRATCH · RECEIPT · KB 325–327 · VX-BND-04 · WATCH_DATES · DEALER_CAPACITY (header-only, body flagged stale) · watchers.py · boot_recompute.py |
| **Outbox** | PROME packet (carve-out ①): FR2004 read + `KB-BND-327` caveat on WQ-157 leg ② evidence |
| **Remaining rc=1** | `STATUS.md:39` DFII10 26bp (Treasury 9/23) vs FRED 9/22 13bp: a one-day basis split, deliberately NOT guarded; expected to clear when FRED publishes 9/23 (~9/25) |
| **Git** | Path-scoped commits (`ad5405323` + closeout); push via `safe-push.sh`, receipt line in the closeout message |
