# OSPREY SCRATCH — 2026-11-27 (Fri) · osprey-1127 · PROME prome-80 wake (D:L914 C1 5→4 test; D:L1057 C3 first kill window)

*Rewritten in full (template). The 11/20 SCRATCH is in git history.*

## CURRENT MARKS (one line)
- Refineries/products **5** · crude-export terminals **5** · shadow-fleet tankers **⚪1 KILLED 11/27 (limb 1 only; limb 2 NOT MEASURED)** · band ~30% [EST] unmoved, stale and understating (Rystad 2.6–2.7 M bpd at 11/23; OWED-52) · Brent → BRENT.

## CHANGES SINCE LAST SESSION (11/20 close → 11/27)
- Refinery strikes: Perm 11/23, Syzran + Kuibyshev 11/25, Slavyansk ECO 11/26 (newest); Subkhankulovo LPDS 11/26. KB-315.
- Sparta II (ro-ro military cargo) hit 11/21 in the Gulf of Finland; Zelensky confirmed Ukraine 11/24. KB-316.
- Rystad via Bloomberg: runs 2.6–2.7 M bpd at 11/23, lowest in 20+ years. KB-318.
- Lukoil International definitive sale 11/25 (OFAC pending); Putin 11/24: Trump asked Kyiv to halt refinery strikes, retaliation "inevitable"; jet-fuel export ban extended. KB-319.
- HAWK graded C3 limb 2 (c) NOT MEASURED for 11/27 (eaad1fcb4d).

## WHAT I DID THIS SESSION
- Boot: root CLAUDE (4 pages to eof), AGENTS (1), USER (3), desk CLAUDE (9 pages to eof) via boot_read.py; STATUS, SCRATCH, LESSONS; ledger_staleness rc 1 (VX +32d, refreshed today; WARRISK declared quiet); corrections check rc 1 → 4 receipts → PASS. Pull NOT run (PROME's dirty files in the tree); fetch 0 behind.
- WQ-735 A: strike_feed.py → `research-bot/1.0`; run 11/27, 38 rows, none refused, all dispositioned. Palaemon 16–22 Nov unpublished.
- L914 graded NOT MET (leg A 1/14 from Slavyansk ECO 11/26, earliest 12/10; leg B UNREACHABLE). KB-314.
- C3 limb 1 counted (none qualifying in 11/07–11/27) → C3 KILLED limb 1 only (KB-317). +6 STRIKES rows; KB-314…321; VX two vectors.
- Inbox 4 packets + 16 WALTER cards → processed (16 board_log rows). Packets: HAWK, BRENT, TERRY, ORACLE, WALTER. STATUS 11/20 block rotated (archive/STATUS_ROTATED_2026-11-27.md, crc32 1926839633).

## NEXT SESSION (dated, future-verifiable)
1. **When published:** Palaemon 16–22 and 23–29 Nov → a qualifying in-window tanker VOIDS the C3 kill; advance the ledger mark.
2. **~12/01:** +5d re-reads Perm, Syzran, Kuibyshev, Slavyansk ECO (halts, units); date Novoshakhtinsk; Vitino date still open.
3. **12/07:** OSP-12 grade (state whether OSPREY's kill on HAWK's grade satisfies "HAWK writes"). **12/10:** C1 leg A. **12/11:** earliest C2 re-kill. **12/18:** GATE-OSPREY-001, OSP-11. **By 12/27:** §5 re-read.
4. **When printed:** November runs (OSP-10 90%, OSP-13 55%, sub-3.00 risk) → OWED-52; Bloomberg 4-wk after 11/8 (asked BRENT). DAEDALUS WQ-678 Changelist B still unread.

## OPEN THREADS / WATCHES
- 🔴 Refinery tempo (16 November rows). 🟠 Energy-strike moratorium talk (Putin's Trump claim; Kyiv's reciprocity condition). 🟠 Ukrainian maritime strikes on military shipping (Baltic, Mediterranean). 🟡 OWED 41–52 carried.
- ⚠️ PREDICTIONS.tsv still over the read budget (PROME's D:L1168 scorer repair). STATUS 30,347 B (measure.py, before the closeout commit).

## PREDICTIONS DUE / DECISIONS PENDING
- None due before 12/07. No Will decision pending from this desk.

## MAIL STATE (one line per surface)
- Inbox clear (4 → processed). WALTER lane clear (16 → processed). Packets 11/27: HAWK 9b0650adec, BRENT 54b929aee2, TERRY 97346b0d71, ORACLE a6bf84d37d, WALTER f1f644de2e; PROME memo at closeout.

## PENDING PUSH / GIT
- Evidence 289f2dcd15 + packets above + closeout commits; pushed via scripts/safe-push.sh at closeout.
