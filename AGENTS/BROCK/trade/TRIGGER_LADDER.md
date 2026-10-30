# BROCK — TRIGGER LADDER + THESIS-KILL STEP 2 (LIVE)

**Status: LIVE.** This file is the only live home of the trigger ladder and the THESIS-KILL STEP-2 rule. `STATUS.md` § EXIT RULES §5 points here. `trade/TRADE.md` §9 (FROZEN 7/27) and the archived tables (`archive/STATUS_ROTATED_2026-09-02.md` §5, `catchups/2026-10-22.md` § Rotated) are history only.
**Last reviewed:** 2026-10-30 17:16 ET (BROCK, re-homed on DAEDALUS profile refresh item 1). **Maintenance:** closeout step 8 (forward-state). When a row fires, resolves or expires, update it here in the same session as STATUS (trap 5).
**Effects are not orders.** Every "effect" below is a prompt for a TERRY card under root rule #5. The instruments named in the 7/27 ladder (BIZD Sep $12P, the "BIZD basket", BX puts) are expired or were never specified. No row pre-authorises a trade.

## Ladder (11 rows)

| # | Trigger | State [as of 10/30] | Effect if it fires |
|---|---|---|---|
| 1 | APO sustained >$130 (3 sessions) | **FIRED 8/12, reviewed, HOLD** (Will 8/13, `PROME/proposals/2026-08-13_private-credit-batch-RULED.md` §②). APO $116.30 [10/30]. Next band: >$145 sustained, not reached | Re-evaluate the APO put view; Will's call |
| 2 | ~~HY OAS <260 for 10+ sessions~~ | **Observable only, not a kill** (WQ-106, 9/2). The kill is LIQUID's 2-close `GATE-HY-REKILL`. HY 326 [10/29] | Confirmation only. Authorises nothing |
| 3 | HY OAS <270 sustained 2+ sessions | **FIRED 8/27** (267 + 263); the kill-memo pre-stage was DISCHARGED (verdict 3). Spent. HY 326 [10/29] | None remaining |
| 4 | Arms-length sub-90¢ BDC loan transaction (= **BRK-25**) | **NOT FIRED.** Count stays at 2 (STATUS §4). Instrument named on the BRK-25 row | Stage-3 entry signal → TERRY card (the 7/27 instrument, BIZD Sep $12P, expired) |
| 5 | First SEC enforcement FILING on PC valuation or disclosure (= **BRK-26**) | **NOT FIRED.** Only post-5/1 events count (L657, 10/20). Instrument named on the BRK-26 row | Stage-3 catalyst → TERRY card |
| 6 | Major BDC NAV markdown >5% in a quarter | **Q2 GRADED NOT FIRED** (max FSK −2.81%). Q3 so far: BCRED −0.59% (KB-BRK-359), ARCC $19.35→$19.31, HTGC up. Not fired. FSK Q3 11/05 | Re-arm the markdown leg; TERRY card |
| 7 | KKR adds to FSK support within 90 days of the 5/11 ~$600M package | **WINDOW CLOSED 8/9, NOT FIRED.** A new KKR package at any time stays a standing watch (STATUS carried debts) | Bear upgrade on FSK → TERRY card |
| 8 | BCRED redemption gate held / sponsor backstop refused | **PARTIAL.** 5% cap enforced Q2 (5/29 expiry) and held Q3 (~50% satisfaction). The Q4 letter ~12/03 is GATE-BRK-R2 (a)'s third read at BCRED (DOCKET L286) | Gate-cascade escalation → TERRY card |
| 9 | Bank PC loss disclosure (NDFI reserve build) | **NEGATIVE so far.** Falsifier = **BRK-31**. 10/25 Q3 pass: no F1/F2 established, attribution INSUFFICIENT | REGINALD owns bank scores |
| 10 | VIX spike +3 without HY widening | **NOT RE-GRADED since 8/28.** This row dropped off STATUS at the 9/2 rotation with no retirement record; restored 10/30. VIX 21.29 [10/30] while HY widened 314→326 (10/28→10/29): not the pattern | HENRY/VIOLET own the vol read; BROCK routes, never trades it |
| 11 | 3+ convergence vectors downgrade 🔴→🟠 in one period | **2 of 3** (PIK and NDFI, both 9/3) | Reassess timeline (EXIT §3) |

## THESIS-KILL DECISION TREE — STEP 2 (rule, verbatim in substance from STATUS 8/28)

- **When it applies:** only after the literal kill fires. The kill is LIQUID's two-close `GATE-HY-REKILL`. BROCK's ten-session <260 observable authorises nothing.
- **Rule:** STEP 2 overrides the kill only if **2 of 3** substance checks have REVERSED:
  1. BCRED gate lifted AND non-accruals declining
  2. FSK/OBDC non-accruals reversing
  3. OTF software exits observed
- **Last run 2026-08-28: 0 of 3 reversed** (① first-ever 5% gate, Q3 cap held, NA 2.4→2.2% but distribution cut 10% and NAV −2.23% · ② FSK NAV −2.81%, FV/cost .9171→.9059; OBDC −1.04% · ③ not observed). Not re-run since: the kill has not fired (HY 326 [10/29]).
