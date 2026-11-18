# BOND SCRATCH — 2026-11-18 standard closeout (desktop, PROME prome-6e registered wake: DOCKET L1184 WQ-709, L1166 WQ-699 A, L1168)

> STATE AT WRITING (13:1x ET 11/18): Composite **17/35** (5+3+2+3+1+1+2, unchanged). **Clean-nominal counter 2**; auction health 3. Outside composite: VX-BND-15=2, 16=4, 17=1 (matched basis from today), 18=2, 19=3, 20=2. **OPEN predictions 4 (BND-34 to 37), earliest resolution 12/17, none past its timeframe.** Position **FLAT** (FORGE 10/30; last broker capture 10/30). Latest cells: Treasury 2Y/10Y/30Y 4.80/5.10/5.46 [11/17]; real 10Y 2.89 [11/17]; 5Y5Y 2.16 [11/17]; HY/CCC/IG 343/1329/92 [11/17]; PMMS spread 213bp matched [11/12]; FR2004 long-end $150.760B [as-of 11/4]; FHLB ratio 3.6 [9/30]. THESIS v1.2.13, token unchanged.

## WHAT I DID

- **Boot:** root CLAUDE.md, AGENTS.md, USER.md, BOND CLAUDE.md read explicitly (no BOND AGENTS.md). Claude Code `claude-opus-5-5`. No pull (PROME's instruction: no pull, no push until its closeout ask). docket_check rc=0 (verified through 11/25; blind span 11/26–12/9 UNVERIFIED, the 12/7 December row exists). corrections rc=1 → COR-20261117-02 receipted NO-OP. boot_recompute rc=1: T5YIFR distance in STATUS (fixed by the rewrite), F2 read owed for 11/17 (done), FOMC 2027-03-17 not docketed (added).
- **11/16 session recovered:** the laptop session committed KB-BND-579 to 583, the 20Y and TIPS bars and VX-BND-18 Q3 (held 2) but wrote no STATUS/SCRATCH/brief before the 21:11 ET restart; folded into today's STATUS.
- **20Y `912810UZ9` graded REGISTERED CLEAN** at 13:04 ET (KB-BND-584): 60.18 / 26.74 / 13.08, BTC 2.63 vs I′ 57.11, OLD 52.47/17.59, cover 2.36. Counter 1 → 2; health held 3.
- **Series through 11/17** (KB-BND-585, 586): Treasury par/real CSVs saved in `analysis/2026-11-18_20y/`. HY +20bp in two sessions to 343, better tiers led.
- **F2 11/17 op** read and routed to RED (`AGENTS/RED/inbox/2026-11-18_from-BOND_F2-2026-11-17-20-30Y-off-the-run-read.md`), ledger row in `registry/f2_reads.tsv`; offers under the cap for the first time since the step-up (KB-BND-587).
- **WQ-699 A applied** (KB-BND-588): `monitors/rates_context.py` joins the last Treasury close strictly before the PMMS date (`join_prior(strict=True)`), four new fixtures, 57/57 pass; live 219/228/213bp match HOMER. VX-BND-17 row updated; band, thresholds, scope unchanged; 11/5 and 11/12 records stand.
- **WQ-719 A:** CLOSEOUT.md C11, CLAUDE.md line 37 and `closeout_run.py` JUDGEMENT now say: rewrite the brief only when a figure, threshold, send or wait in it changed; otherwise untouched with `--noop`. This session's brief was rewritten because its figures changed.
- **Month-end bars frozen early** (2Y, 5Y, 7Y; all announced with CUSIPs; grader accepted all three).
- **Inbox drained, 10 of 10:** 6 packets → `inbox/processed/`, 4 WALTER cards → `inbox/WALTER/processed/` with board_log rows. KB rows 584–591. Stale KB rows: 15 past Stale_By and ACTIVE (PROME counted 8 on 11/16; today's date adds 7), all 15 retired to STALE by their own date, 0 refreshed (none cited by a live gate, kill, band or open prediction).
- **Answers to PROME** (packet `PROME/inbox/2026-11-18_from-BOND_...`): archive layout and count (29 rows, 28 scorable, 1 VOID; the scorer agrees: 32 BOND calls scored); Florida muni spread NO (EMMA 403, no Florida fund on the vendor); HANS T-16 logged.

## NOT MOVED

No score, gate, band or threshold. Composite 17. Token unchanged. THESIS untouched (no thesis-level change).

## NEXT SESSION (dated)

1. **11/19:** 10Y TIPS `91282CRE3` grade on frozen bars (not a counter auction) · PMMS, the first live matched-basis read · H.4.1 custody leg (KB-BND-576) · FR2004 as-of 11/11.
2. **11/23–11/25:** grade 2Y, 5Y, 7Y on the frozen bars (counter at 2; a third registered clean makes 3, which moves nothing at score 3).
3. **HY:** BND-34 needs ≥352 by 12/30; a print above 350 is the HY-function upgrade leg, then check for pulled deals.
4. 11/25 VX-BND-20 review; FR2004 as-of 11/18 about 11/25–27. 12/2 and 12/8 F2 reads. Before 12/2: any 12/9 curve-shape row with a base rate. 12/27: re-record the FOMC calendar.
5. Quiet session: blind span 11/26–12/9 against the Treasury QRA by hand; Bund and WQ400 re-read; VX-BND-06 CDX proxy re-read; WQ-678 Changelist B trims; `rates_context.py` HENRY→ORACLE label.

## OPEN THREADS

Japan intervention funding (H.4.1 split with LIQUID). True CDX, pulled-deal census, private funding unchanged. WQ291 funding window UNGRADED. Florida muni spread: no free automated source.

## STATED NO-OPS

THESIS/CHANGELOG (no thesis-level change) · predictions (none DUE) · FLOW (no channel change) · MEMORY (no new BOND lesson; the stamp correction is the fleet's existing clock rule).

## POSITION

FLAT on this thesis. BOND executes nothing; no expiry reminders.

## MAIL / DELIVERY

Sent: RED F2 read (above); PROME packet (one, citing L1184, L1166, L1168, the four answers). SendMessage to prome-6e after the commit. No TERRY packet: no finding implies a trade (reason in the PROME packet). Not pushed (PROME's closeout ask governs).
