# Re-accumulated `AGENTS/PROME/` contents (2026-06-25 → 2026-07-24)

The `AGENTS/PROME/` tree was archived **2026-06-24** (see the parent directory's README). It then **re-accumulated 55 files over the next month** because several senders had the path baked into their routing, and PROME's own `BOOT.md` step 6 told PROME to keep scanning it as "a live legacy delivery surface until the messaging overhaul re-homes it."

**Will ruled 2026-07-24: PROME uses `PROME/inbox/`. The `AGENTS/PROME/` tree is killed.** RED executed the migration.

## What went where

| Content | Destination |
|---|---|
| **5 LIVE, unprocessed packets** (2× DEWEY 7/24, 1× WALTER 7/24, 1× RED 7/24, + undelivered signal `SIG-W-20260724-006`) | **`PROME/inbox/`** — flat, top level, so they cannot be missed at boot |
| 16 `inbox/processed/` files | `./inbox_processed/` |
| 33 `inbox/WALTER/processed/` signal files | `./inbox_WALTER_processed/` |
| `.claude/settings.local.json` | `./PRESERVED_settings.local.json.txt` — **gitignored, so git history would NOT have preserved it**; copied here deliberately |

## ⚠️ Two things a deletion does not fix

1. **The senders still point here.** `AGENTS/WALTER/routed/delivery_log.tsv` has ~30 rows targeting `AGENTS/PROME/inbox/WALTER/`, the most recent written **2026-07-24T23:55Z** (`SIG-W-20260724-006`, status `written_not_delivered_pending`). DEWEY routed here twice on 7/24. **Until WALTER's and DEWEY's routing targets change, this directory will be recreated** — exactly as it was after the 6/24 archival. WALTER and DEWEY own those files; RED flagged rather than edited them.
2. **`PROME/BOOT.md` step 6 still instructs PROME to scan `AGENTS/PROME/inbox/`.** That line is now stale and should be retired or re-pointed — PROME owns `PROME/`, so RED did not edit it.

The ratified `MESSAGING/DIRECT_MESSAGING_V1_SPEC.md` §"For messages addressed to PROME" already says implementations must use PROME's ratified inbox location "rather than assume an `AGENTS/PROME/` directory" — so Will's ruling matches the spec that was already on the books. The gap was enforcement, not policy.

*Migrated by RED, 2026-07-24, on Will's explicit instruction (outside RED's normal write scope).*
