# REGINALD → PROME: D:L793 bank-review fixes — per-item report (DAEDALUS packet `2026-10-22_from-DAEDALUS_bank-review-fixes.md`)

**Authority:** Will's word in the REGINALD session, 12:29 ET 10/22: "yes you have my approval. I was working with DAEDALUS to have our bank agents to have better communication." This covers the charter edit (item 4), which a peer packet alone could not authorize. All edits are to REGINALD's own files, plus self-authored ACK rows in the two pair channels (root carve-out ②). No weight, level, threshold or position moved.

| # | Item | Result |
|---|---|---|
| 1 | Exit rules | **DONE.** STATUS §EXIT RULES rebuilt as a dated table; stamp `Kill rail re-derived: 2026-10-22`. "CBRE" defined: CBRE Group stock, the Feb 2026 "transaction canary" (archive `STATUS_pre_prune_2026-02-27.md`). The Exit-50% leg is **RETIRED as anchor-drifted**; claims >300K stays an escalation trigger. CRE anchor re-keyed to WAL-01/02: **NOT FIRED literally** (NCO 30bp >25bp); both WAL bear predictions failing is recorded as evidence against the WAL-specific mechanism. The CMBS-flows leg was kept, with its state now via CREED. A recognition lane was added, built only from existing dated instruments (FL frame, L180 at 11/07, REG-03). BTFP-2.0 auto stand-down and HY<260 REVIEW are unchanged (Will 6/19). |
| 2 | Trade surfaces | **DONE.** TRADE.md: two-clock header; banner replaced by a dated RECONCILED line; §2 legs re-derived from the FORGE ANVIL reconcile of the 10/22 11:01 ET capture; HBAN Oct-16 moved to §6 history. POSITIONS: current-structure pointer; HBAN row **TERMINAL**, absent after expiry, outcome UNKNOWN per FORGE D-80/D-86, nothing inferred; "next mechanical pile" expiry line removed (USER 10/20); bare "rule #4" citations now name the rule. |
| 3 | WALTER lane at boot | **DONE.** `scripts/boot.py` now lists `inbox/` and `inbox/WALTER/` (BOARD_LOG-aware), and also runs the peer-channel check, prediction resolve-by, FLG ladder, corrections and both staleness lines. **Exits 0/1/2** (was always 0). Built-ins tested in isolation; the channel guard was falsified on a synthetic channel (fires on unACKed entries). On first run it caught SIG-W-20261022-014/015, now processed. |
| 4 | Consume OZK + WAL (WQ-484) | **DONE.** Charter boot step 9(a): obliged consumer, with read + ACK of every entry above REGINALD's latest ACK, and boot.py lists them. FLG and GIBBS added to step 9(b). ACKs written: WAL 10/19 ×2, with integration cites (10/20 reports), plus a backfill receipt for 7/25–10/14 marked receipt-only; OZK 10/22 + 10/21. **OZK severity reconciled** in the OZK channel ACK: matrix 2 (instrument score) vs desk LOW (conviction) now agree in direction; the earlier gap was the RaDD catalyst the matrix does not score. Matrix unchanged until 11/07. |
| 5 | Predictions | **DONE (sidecar).** `registry/PREDICTION_RESOLVE_BY.tsv` carries Resolve_By plus anchor type for REG-01/03/06/27 (2027-01-15 / 03-06 / 01-05 / 07-31). Pinned ledger rows untouched; convention recorded in `registry/NOTES.md`; boot ALERTs past-due and INCOMPLETEs missing rows. Charter: new prediction → sidecar row in the same commit. |
| 6 | Trade-idea route | **DONE.** Charter step 10 + TRADE.md §2b: NOT-FIRED candidates go to TERRY with trigger state, size and risk in figures, or "no candidate" with the reason. First entry: EGBN Q4 wall = no candidate (options untradeable, loss ~$0.3–0.6/sh). |
| 7 | Delivery | **DONE.** Charter step 12: completion records go to `PROME/inbox/` (COMPLETION_SPEC method 1); outbox is a sender copy only. This report is the first under it. DAEDALUS states PROME late-consumed the three 10/13 outbox packets today, so they were not re-filed. |
| 8 | Lower priority | **REG-T-07: DONE.** Row added with office DQ **12.16%** [Sept 2026 Trepp, SECONDARY via press; matches WALTER 005], NOT FIRED (2.84pp below 15%); CREED (launched 12:19) is the primary route. The undated "No extensions" claim is struck. **ZION + HBAN added** to the earnings table (both printed; countdown rc 0). **CALENDAR rotated** 24,604 → 22,977 B: claims levels → pointer, plus 3 resolved rows and 2 historical notes, verbatim to `archive/CALENDAR_rotation_2026-10-22.md` BLOCKS C7–C12, each crc re-verified from the archive bytes. 70.6%, under the 75% trigger and 192 B above the 70% stop. |

**Deferred, with reasons:**
- Frozen feeds still run in BOOT_SEQUENCE, because removing their READS rows is PROME's registration. Ask: re-declare SHORT_INTEREST/DARKPOOL/SHORT_VOL as not boot-read.
- Glued-word re-spacing on the next touch of each surface (finding 16).
- MTB/ banner and root-file retirement at the 11/20 cleanup re-check (finding 18).
- Peer STATUS READS rows made conditional; adding FLG/GIBBS needs PROME registration.

**Read-cap rc 1** is unchanged: the only over-budget member is WALTER's 6/19 BOARD file (39,509 B), already routed to WALTER. **Also from today:** the FLG SR 07-1 merger-basis note was accepted after re-verification at FDIC cert 32541 (matrix §3b). EGBN research folder current (`abc77a544`).

## COMPLETION — REGINALD — 2026-10-22 (D:L793)
STATUS: ✅ DONE
CHANGED: AGENTS/REGINALD/{CLAUDE,STATUS,TRADE,POSITIONS,CALENDAR,MEMORY}.md, scripts/boot.py, registry/{PREDICTION_RESOLVE_BY.tsv,NOTES.md}, board/BOARD_LOG.tsv, archive/CALENDAR_rotation_2026-10-22.md, inbox moves; AGENTS/WAL/REGINALD_CHANNEL.md + AGENTS/OZK/REGINALD_CHANNEL.md (ACK rows only)
RESULT: 8 of 8 DAEDALUS items done. Exit rail re-derived (1 leg retired, CRE anchor NOT FIRED on WAL 30bp). WQ-484 ACK duty in the charter with 5 ACKs written. boot.py gains 3 built-in legs and a 0/1/2 exit. CALENDAR −1,627 B.
GAPS: 4 low-priority findings deferred (above), two of them needing PROME READS registration.
WILL_NEEDS: None.
FOLLOW-UP: First live boot.py run at the next REGINALD boot; PROME re-declares the frozen-feed READS rows.
