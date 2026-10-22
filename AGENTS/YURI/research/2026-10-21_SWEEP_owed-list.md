# YURI sweep: owed / incomplete / stale (2026-10-21 22:0x ET)

**Requested by Will, in session**, 21:58 ET: "do a sweep of YURI files for anything owed, incomplete, missing, stale". Saved at Will's word at 22:03 ET. **This file is the working list.** Each row's `state` cell is updated as the item is worked, and closed rows keep their closing evidence.

**Pointers:** `AGENTS/YURI/STATUS.md` (top) and PROME's `SCRATCH.md` (requested from prome-56; PROME owns that file).

**Sweep perimeter:**
- `git status`, inbox, outbox, registry, `board_log.tsv`, ledger, STATUS, NEXUS brief
- charter-referenced files; corrections check; LEDGERS/READS/BRIEFS_MAP rows
- WALTER REGISTRY row; DAEDALUS 10/21 boot note; PROME/WALTER receipt of tonight's packets

It does **not** grade evidence, re-read primaries, or check other desks' surfaces beyond the named greps.

## 🔴 Owed now

| # | Item | Where | Fix | state |
|---|---|---|---|---|
| 1 | Correction COR-20261021-16 unreceipted: **BLOCKS** the corrections boot check. It is WALTER's BOARD form of YURI's own "LIFTED ban" correction (SIG-W-20261021-016). It repeats YURI's imprecise "producer restriction to 10/31" shorthand, made precise in report §9. | `scripts/corrections_boot_check.py YURI` | Receipt (WQ-399 fields) + one-line wording note to WALTER | **CLOSED** 2026-10-22T02:04Z: receipt NO-OP written (`registry/corrections_receipts.tsv`), check 0 OK. Precision note to WALTER: `SIG-YURI-WALTER-20261021c` |
| 2 | Inbox item SIG-W-20261021-016 not filed | `inbox/WALTER/` | Read; file to `processed/` | **CLOSED**: read, `git mv` to `inbox/WALTER/processed/` |
| 3 | `board_log.tsv` not written in the 10/21 session: 14 items filed, 0 rows (last row 10/13) | `board_log.tsv` | Append 14 + 1 rows | **CLOSED**: 15 rows appended (14 backfilled + -016) |

## 🟠 Stale on YURI's own surfaces

| # | Item | Where | state |
|---|---|---|---|
| 4 | YUR-004 table row's Reading cell still carries the 10/12 reading | `STATUS.md` live-reads table | **CLOSED**: Reading cell rewritten to the 10/21 + completion-pass reading |
| 5 | Known limits: "MoD host failures are 25 September observations" — remeasured 2026-10-22T01:28Z (timeouts) | `STATUS.md` § Known limits | **CLOSED**: replaced with the 2026-10-22T01:28Z remeasurement; Codex-queue transport line updated to the Claude Code SendMessage path |
| 6 | Pending clocks from 10/12 (DEWEY/BRENT 14 Oct, OSPREY 15 Oct, "14–16 October reviews") are carried as live. DEWEY final delivered 10/13. | `STATUS.md` § Current instrument answers | **CLOSED**: 14–16 Oct clocks had already left STATUS in the 10/21 rewrite; the imprecise №1252 "producer restriction" line made precise; 23-story "unread" limit updated |
| 7 | NEXUS brief WAITING FOR rows expired (14 Oct / "next review 16 October"). The VIEW body is 10/12 content. | `NEXUS_BRIEF.md` | **CLOSED**: WAITING FOR / VIEW / CALIBRATION / NEXT DECISION / WATCH rewritten to the 10/21 state |
| 8 | WALTER REGISTRY YURI row says runtime "Codex" (informational) | `AGENTS/WALTER/REGISTRY.tsv` L47 (WALTER-owned) | **FLAGGED** to WALTER in `SIG-YURI-WALTER-20261021c` (WALTER-owned) |

## 🟡 Research gaps (logged, owned, not done)

| # | Item | state |
|---|---|---|
| 9 | Signed 500 kt diesel partial-lift act/annex | OPEN (unlocated since 10/12) |
| 10 | №686 implementing goods-code list (OSPREY carries it too) | OPEN (SEARCH-NOT-FOUND) |
| 11 | ЕГРЮЛ for Lemana Pro and FM Logistic entities (№661) | **CLOSED** (report §10.1): Le Monlid owners unchanged, LEV entered 21.10; FM Logistic Vostok still under its own director, no LEV entry 35 days on |
| 12 | №738 parents: Tarkett, Ontex, Menshen | **CLOSED** (§10.2): **Ontex VERIFIED** (Euronext Brussels, about 5% revenue / 7–8% adj. EBITDA, Inside Information 16.10); Tarkett holder direct but issuer statement and listing UNRESOLVED; Menshen UNVERIFIED |
| 13 | №750 vs prior №1285 wording: what changed | **CLOSED** (§10.3): the only change is a new foreign-law-obligation trigger; subsidiaries and unions of states were already in the 2017 text |
| 14 | Hubbard pardon decree | **CLOSED: NOT-FOUND** (§10.4, 02:09Z); the Ushakov readout stays the instrument; recheck at the 10/23 read |
| 15 | About 30 untitled government распоряжения (10.10→17.10); the YUR-005 baseline is partial on them | **CLOSED** (§10.5): 28/28 page 1 read, none fuel/export; orders cannot amend №954; annexes of 3 long orders unread |
| 16 | Shadow-fleet registration decree (signed successor to Mintrans 11 June draft) | OPEN |
| 17 | Sonoco divestiture of Eviosys Kuban after 26.02.2026 | **CLOSED** (§10.2): no divestiture in SEC filings to the 21.10 Q3 release; release silent on 15.10 temporary management |

## 🔵 Dated obligations

| Date | Item | Owner | state |
|---|---|---|---|
| Fri 10/23 | YUR-004 weekly read | YURI | OPEN |
| Sat 10/24 | YUR-F01 grade (0/3). DAEDALUS's 10/21 boot note says "interpretation acceptance still pending"; YURI answered (a) in its PROME packet. PROME→DAEDALUS relay is unconfirmed. | DAEDALUS | OPEN |
| 10/29 | Aptar Q3 results (issuer schedule, 10/12 carry) | context | OPEN |
| 10/30 · 10/31 | YUR-004 weekly read · final grade (backfills to 11/02) | YURI | OPEN |
| Mon 11/02 | YUR-005 grade | YURI | OPEN |
| Sun 11/15 | YUR-006 grade | YURI | OPEN |

## ⚪ Unknown / held by others

| # | Item | state |
|---|---|---|
| 18 | 9/26 WATCH_FOR candidate phrases: no adoption visible (WALTER REGISTRY L47 watch column "—") | OPEN (WALTER/PROME) |
| 19 | OSPREY consumption of 10/12 deliveries | **CLOSED**: verified at OSPREY STATUS L76 ("YURI 10/12") |
| 20 | WALTER consumed both 10/21 SIG-YURI packets (BOARD -017, -021); filing the packet files is WALTER's job | CLOSED (consumption verified at BOARD) |
| 21 | PROME read of the completion-pass and YUR-005/006 packets | **CLOSED**: prome-56 confirmed 22:0x ET; SCRATCH pointer + DAEDALUS relay verified at 9d3392758 (PROME local, pushes at its closeout) |

**Clean at sweep time:** no uncommitted files · `boot.py` PASS on 6 rows · STATUS 20.9 KB (<75% cap) · ledger LIVE in DAEDALUS LEDGERS.tsv · READS.tsv rows present · all charter-referenced files exist · no file eligible for retirement (desk is 27 days old).

**Reconciliation 2026-10-21 22:2x ET (Will: "check your key files and workbook"):** STATUS, NEXUS_BRIEF and INTENT_LEDGER re-checked against every source read this session. Fixes: stale header and session stamps; №738 "parents unverified" and №750 "not compared" lines superseded; №1252 shorthand made precise; OSPREY consumption recorded; ЕГРЮЛ coverage extended; Kremlin extras (fertilizer offer, APEC trilateral, 16.10 security-zone line, 19.10 cabinet changes) recorded; Novak and cargo context recorded; order by-catches and the Tarkett press statement recorded; YUR-005 baseline and YUR-F01 relay cells updated. Still OPEN: 9, 10, 16, 18 + dated obligations. STATUS at 24,054 B, 73.9% of the 32,550 B cap: rotation is due at the next STATUS growth (threshold 24,412 B).
