# RED SCRATCH — canonical session handoff
**S63 HANDOFF — written 2026-11-12 09:53 ET (from `date`). Desktop, Claude Code, Opus 5.5. Booted 08:48 ET on Will's status-only task; Will 08:53 ET "ok go" on the proposal: grade FT-06 / RED-29 on the official close, re-derive if 11/11 < 18, do the intake, close out. The S61/S62 handoff and its addenda are in git history (`git log -p -- AGENTS/RED/SCRATCH.md`).**

## CHANGES SINCE (S62-c closed 11/10 19:33 → S63 11/12 08:48)
- Official: VIXCLS 19.46 [11/10], **17.49 [11/11]** · HY 334 / CCC 1,311 [11/09]; 11/10 ICE cell absent; FRED cells dated 11/11 (HY 330, CCC 1,330, BB 193, B 347, IG 90) sit on a SIFMA close, not counted · SKEW 151.12 [11/10], 149.09 [11/11] · 5y5y 2.15 [11/10] · claims 200K [w/e 11/07] · January Brent 91.49 settle [11/10, BRENT].
- ORACLE 11/11: December 9 hold 3.5 / +25 85.5 / +50 11.8; Iran pause by 11/15 54.5. FALCON weekly 11/11: marks 1/14/85 held, census 7. DEWEY 003R delivered (bank population, United Fidelity 69% of the smaller band). SAM: SoftBank own-basis 22.5% (was 22.7%).

## WHAT I DID (S63)
- Boot in full; boot.py, review_debt, ledger staleness, corrections, basis.
- Intake: 4 inbox packets (3 DEWEY, 1 SAM) and WALTER card 029 logged and filed; 5 corrections (COR-20261111-06/13/14/24/25) receipted NO-OP; basis drift read (WALTER BOARD_CONSUMPTION_SPEC §3.5.9, moved text, no rule change) and re-hashed.
- **FT-06 / RED-29 graded:** VIXCLS 17.49 [11/11], FRED 09:48 ET = Cboe; run broke at 4 of 5; exit 0 of 5; RED-29 WRONG (EVENT FALSE). Registry, scan view, PREDICTIONS, CATALYSTS, CALENDAR, STATUS mirrored.
- **Re-derivation (discretionary):** Stag 33 → 32, Managed 25 → 26, net-bear 68 → 67, HOLD 72 → `reports/2026-11-12_S63_weight_rederivation.md`. Bull steelman re-checked.
- KB-102 (credit tape) and KB-103 (oil) refreshed; KB-071 reviewed. ML-331 (a lower low cannot inherit the 'since' date) and ML-332 (the non-session clause governs citations too), both caught in my own draft before commit.
- STATUS current-state reconciliation: stale sections folded verbatim → `reports/2026-11-12_S63_status_folded.md` (17445 B, crc32 2605937422); counter-signal levels table rebuilt [11/12]; trigger table [11/12].
- Routing: OUTBOX -079; packet `PROME/inbox/2026-11-12_from-RED_S63-ft06-rederivation.md`; NEXUS vS63 (vS62-b rotated).

## NEXT SESSION (dated, ordered)
1. 🟠 **Fri 11/13:** KB review wave: KB-107 real wages (re-class; October unreadable, no Oct 2025 base), KB-086, -067, -105, -106, -108; combo theme credit-breadth-outside-ai (KB-110). Daily: FT-02 exit on the 11/10 ICE cell (LIQUID grades the cell's session).
2. 🟡 **11/14–11/17:** KB-043 (11/14); KB-083, -046, -052, -082 (11/15); KB-104 (11/17).
3. 🟡 **Tue 11/17:** CHG-045 closes as NOT REOPENED unless Will reopens his 8/16 choice (told in chat 11/12; RED recommends not reopening).
4. 🟠 **Thu 11/19:** CHG-057 re-review (NVIDIA 10-Q SB Energy guarantee line, ING auction bids, SoftBank Tokyo/CDS/rating; use SAM's 22.5% basis). STRONG → route to TERRY for a tradeability read.
5. 🟡 **By Fri 11/20:** Zweig thrust decision tree for the 11/27 VX-006 grade; combo themes KB-109, -112, -113; KB-054; Michigan final.
6. 🟡 **~11/25** FT-10 outcome grade · **11/26** Thanksgiving bar bridged · **11/30** CHG-044, CHG-054 · **12/04** payrolls → next re-derivation · **12/09** FOMC · **12/10** RED-28 · **12/15** CHG-055, RED-31 · **12/31** RED-25/26/27/30.
7. 🟢 Offered to Will, not assigned: retirement pass, about 8 files over 60 days.

## OPEN THREADS
- FT-10's ~11/25 CORRECT must not be read as war or credit foresight (tech and gamma trigger, ML-311).
- WL-11: price leg met on settle; flow leg is BRENT's; do not resolve by inference.
- The FRED ICE cells dated 11/11: whether they are the 11/10 session relabelled is LIQUID's call.

## PENDING WILL-DECISIONS
- CHG-045 reopen choice by 11/17 (not on WILL_QUEUE; Will told in chat; default = not reopened).

## GIT STATE
See the closeout message. Shared tree holds other desks' dirty files (CYPHER, DAEDALUS, LABOR, VULCAN, WALTER); RED commits by pathspec only.

## ADDENDUM S63-b — 2026-11-12 12:10 ET (from `date`)
- Will 12:08 ET approved RED's recommendation on DAEDALUS WQ-678 trims: 7 applied, U-R07 declined (→ `MAINTENANCE.md` S63-b). `OUTBOX.md` FROZEN; W8 = dated `PROME/inbox/` packet; `closeout_check.py` (e) reads it.
- No weight, trigger, prediction or catalyst change. 11/10 ICE OAS cell still absent on FRED at 12:05 ET (HY 334 [11/09], 330 dated 11/11 non-session).
- Next entry point unchanged: NEXT SESSION item 1 (Fri 11/13 KB wave).
