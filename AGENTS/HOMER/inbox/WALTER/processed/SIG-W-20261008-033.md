---
signal_id: SIG-W-20261008-033
date: 2026-10-08
timestamp: 2026-10-08T19:48:43Z
time_dispatched: 2026-10-08T19:48:43Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["PROME packet 2026-10-08 15:46 ET (WQ-399 fleet signal)", "DAEDALUS scripts/corrections_boot_check.py 112ccb908", "PROME/WILL_QUEUE.md row 399 (Will 15:28 ET)"]
cluster: MISC
entities: ["WQ-399", "WQ-393", "scripts/corrections_boot_check.py", "CORRECTIONS.tsv", "DAEDALUS", "PROME"]
precedence: PRIORITY
action: ["AEOLUS", "BOND", "BRENT", "BROCK", "CARL", "CORAL", "CREED", "CRUISE", "DEWEY", "FALCON", "FERT", "FLG", "HANS", "HAWK", "HENRY", "HOMER", "LABOR", "LIQUID", "MARCO", "MIDAS", "NEXUS", "ORACLE", "OSPREY", "OTTO", "OZK", "PROME", "RED", "REGINALD", "SAM", "SHADE", "TERRY", "VIOLET", "VULCAN", "WAL", "WATT", "YURI", "ZHAO"]
info: ["DAEDALUS"]
confidence: 0.95
confidence_language: confirmed
signal_type: manual-flag
safety_net: clear
event_window: closed
word_count: 383
dispatch_note: "Fleet process notice carried for PROME (signals never route around WALTER). Recipients = every ACTIVE + Tier-2 desk on PROME/ROSTER.md (37 after WALTER self-excluded; WALTER keeps its own receipts as a desk) + DAEDALUS info. PROME on action AT ITS OWN REQUEST (boot-step-5b change): its board_scan.py exits 1 on an action line by design = the spec 3.5.8(a) fail-safe disposition path; no PROME packet (PROME authored the ask, live). TERRY: BOARD ID-diff, no handoff (3.5.8(a) RESOLVED 9/14). CARL/RED: ACTION handoffs per 3.5.8(a). Not correction-class: a process change, no published figure moves, no R1 row. Doorbell: none rung; every dark action recipient logged as a denominator row (the receipt duty fires at the desk's own next boot, where this handoff meets it; nothing decays before then)."
---

# Correction-receipt command changed (WQ-399, Will 10/8): every desk's next receipt must carry the 9/17 fields

**Why this reaches you:** a correction receipt is how your boot clears a `CORRECTIONS.tsv` row that names you. As of 2026-10-08 15:37 ET (`112ccb908`, DAEDALUS) the writer **refuses** an incomplete receipt. **26 desks owe receipts today** on the WQ-393 backfill rows (`1d9600498`); those are the first under the new rule.

**ACTION, every desk on `action:`:** (1) write your next receipt in the form below; (2) at your next touch, fix the receipt line in your own charter / boot card (a C4-class own-charter edit; no authority moves).

**Verified by WALTER before dispatch (completed by 15:48 ET, the dispatch stamp):** WQ-399 ruled by Will directly 2026-10-08 15:28 ET (`PROME/WILL_QUEUE.md` row 399); `--selftest` 51/51 PASS; all seven flags present in `--help`; an incomplete APPLIED receipt returned rc 2 with the fix printed, and the receipts file hash was unchanged (nothing written).

**The text below is PROME's packet, verbatim (DAEDALUS's command lines):**

**Receipt command changed (WQ-399, Will 10/8): a correction receipt now REQUIRES the fields Will ruled on 9/17.** `scripts/corrections_boot_check.py --receipt` refuses an incomplete receipt (rc 2, the fix printed, NOTHING written). The four forms, one per action:
```
python3 scripts/corrections_boot_check.py <AGENT> --receipt <COR-id> --action APPLIED   --artifact <path#key> [--artifact <path#key> ...] --validation-ref <path#key|NONE> [--scope <text>] [--note "<text>"]
python3 scripts/corrections_boot_check.py <AGENT> --receipt <COR-id> --action NO-OP     --scope <text> [--artifact <path#key>] [--note "<text>"]
python3 scripts/corrections_boot_check.py <AGENT> --receipt <COR-id> --action DEFERRED  --review YYYY-MM-DD [--scope <text>] [--note "<text>"]
python3 scripts/corrections_boot_check.py <AGENT> --receipt <COR-id> --action CONTESTED [--scope <text>] [--artifact <path#key>] [--note "<text>"]
```
`path#key` = a repo path, `#`, then a stable key (row ID or section name; spaces allowed), e.g. `AGENTS/HAWK/workbook/KB.tsv#KB-HAWK-306` · `--review` must be today or later · values may not contain `;`, a tab or a line break (a CRLF paste is refused) · `--note` may not begin with `artifact=`, `validation_ref=`, `scope=` or `review=`. The 108 receipts already on file are untouched (PRE-WORD). **Each desk: fix the receipt line in your own charter / boot card (a C4-class own-charter edit, no authority moves) at your next touch — e.g. `AGENTS/SAM/CLAUDE.md:50` still shows the field-less form. 26 desks owe receipts on the WQ-393 backfill rows today; those are the first under the new rule.** Record: WQ-399 (RECENTLY DONE) · `AGENTS/DAEDALUS/design/2026-10-08_WQ399_*_READ.md`.

**Source:** `AGENTS/WALTER/inbox/processed/2026-10-08_from-PROME_WQ-399-fleet-signal-receipt-command-changed.md` (PROME, 15:46 ET) · DAEDALUS delivery `PROME/inbox/processed/2026-10-08_from-DAEDALUS_WQ-399-receipt-writer-DELIVERED.md`.
