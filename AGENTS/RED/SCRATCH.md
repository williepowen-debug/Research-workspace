# RED SCRATCH — Canonical Session Handoff

<!-- TEMPLATE (rewrite in place at W5 every session; git history versions this file):
## CHANGES SINCE (what moved while RED was offline)
## WHAT I DID
10. **★ Block 3 (Will-directed): `AGENTS/PROME/` KILLED** — Will ruled `PROME/inbox/` is the sole PROME surface. The tree was **not** an empty shell: **55 files**, incl. **5 LIVE unprocessed packets** (2× DEWEY 7/24, 1× WALTER 7/24, 1× mine, + WALTER signal `SIG-W-20260724-006` written 23:55Z, `written_not_delivered_pending`). Migrated live→`PROME/inbox/` (flat), 49 processed→`PROME/archive/AGENTS_PROME_LEGACY_2026-06-24/reaccumulated_2026-06-25_to_07-24/`, gitignored `.claude/settings.local.json` preserved as `.txt` (git history would NOT have caught it; it granted a bare `Bash(git *)` PROME's live settings lacks). Dir removed (`gio trash` — no `trash`/`trash-put` on this box). **Commit `46d79cd8` — outside RED's normal write scope, on Will's explicit instruction.**
11. **Block 4: told PROME to fix `BOOT.md` step 6** (Will-directed) — it instructs PROME to scan the now-dead path *every boot*. Packet `8a84190a` gives verbatim text + suggested replacement, flags `CLOSEOUT.md:24` as carrying the same stale claim, and explicitly says **leave `GIT_COORDINATION.md` alone** (lines 34/131/142 read *more* correctly post-deletion — flagged so a find-replace sweep doesn't clobber them). Argued one judgment call: reappearance of `AGENTS/PROME/` should be treated as a **sender-routing regression to flag**, not a surface to service.

## NEXT SESSION (dated, priority-ordered)
## OPEN THREADS
## PENDING WILL-DECISIONS
## GIT STATE (one line)
-->

**Session 26 — Wed 2026-07-29 ~10:45 PM ET (spawned by PROME, teams-mode; fleet was offline through the print itself — usage outage)** — FOMC 7/28-29 graded same-night off primaries; registry exit-semantics debt closed; hypothesis re-mark. **HOLD 69→70 (+1) / net-bear 62→68 (+6).**

## CHANGES SINCE (S25 closeout 7/24 ~19:30 → tonight)
- **FOMC 7/28-29 happened and was unobserved live** (fleet-wide usage outage). Graded retrospectively tonight off primaries: federalreserve.gov statement, Warsh presser PDF (pdfminer-extracted), FRED (HY/CCC/10Y/DFII10 via `fetch.py`), Yahoo/Bloomberg/CNN market reaction.
- **9-3 hold at 3.50-3.75%**, three unified hawkish dissents (Hammack/Kashkari/Logan — first such dissent since Sept 2016). Statement: *"inflation...in part reflecting supply shocks...including energy"* / *"job gains have kept pace with the workforce, unemployment rate changed little"* / *"no soft inflation target."*
- **Market reaction: VIX closed 20.66 (+13.45%)**, SPX −1.52% to 7,316.15, Dow −2.19% (worst since Apr-2025). First non-absorbed FOMC print of the cycle — but same night, **overnight US+Saudi struck Iran-backed sites in Iraq** after Iran's 7/28 IRGC missile launch at a US base in Jordan; BRENT's 7/29 STATUS calls Saudi Arabia's shift "from target to co-belligerent." Confound, unresolved (Guard 3).
- **HY OAS 281 [7/27] → 284 [7/28]** (FRED) — 2 of 3 sessions toward WL-03's un-fire; **CCC OAS 1001 [7/27] → 1005 [7/28]** — WL-06 (CCC>1000, "2016-analog") **FIRED 7/27**. Both pre-date the decision (Guard 1).
- **3 PROME packets processed** (from inbox, all pre-dating tonight, already reflected in S25 or informational): CARL sequencing-rejection-accepted receipt, NEXUS 2-items, PROME BDC-dates/harmful-revision-ledger-task/BROCK-BRK-32 — **harmful-revision ledger (PROME 7/25) and BRK-32 register-respec ask (BROCK 7/27) are NOT actioned tonight** — out of scope for tonight's 4-item task packet, flagged for next session, not silently dropped.

## WHAT I DID (S26)
1. **RED-20 GRADED CORRECT, both vintages.** v1.0 (S1 52%) and v1.1 (S1 54/16/7/21/2, amendment validated by S4 NOT occurring). §L oil-language: L1 confirmed, RED's 42-over-30 beats CARL's L2-modal claim. §LAB: LAB-a confirmed on substance; RED's own added verbatim-staleness sub-test did NOT fire (language revised, not repeated). Full memo: `research/FOMC_JUL28-29_2026_GRADED.md`. ML-RED-117.
2. **★ The framework's own informal "S1×R-A absorbed" bottom line was WRONG, and I said so before folding it into anything flattering.** VIX 20.66 close = R-B on the letter, but Guard 3 (pre-registered 7/24, never yet tested) is now genuinely live — a same-window war escalation confounds the attribution and I will not bank the full pre-registered S1×R-B/CCC conjunction (+2 confidence, net-bear cap +3) at face value. Applied a haircut instead: +1 confidence (not +2), Acute +2 split explicitly into +1 mechanical (pre-reg) / +1 discretionary (VIX leg, flagged beyond-letter).
3. **S3×R-D (rates-arm kill) confirmed did NOT fire** — TRY-FIRE-004 survives its hardest test; yields ROSE (10Y +7bp intraday, 30Y +12bp to a 19-yr high), the opposite of the kill scenario.
4. **FT-01 un-fire clock: 2 of 3 sessions logged (281/284), 3rd (7/29 print) PENDING** — FRED posts next business day, does not resolve tonight. Recorded, not prematurely called.
5. **Registry exit-semantics debt CLOSED.** Audited all 7 `FALSIFICATION_TRIGGERS.tsv` rows against `docket/WATCHLINES.tsv`: only FT-01 has a defined exit (WL-03, symmetric sustain=3). FT-02 through FT-07 marked **UNDEFINED honestly** — no reversal threshold registered anywhere for any of them (WL-05/06 are escalation legs of FT-07's own direction, not an exit; WL-01 is a different trigger). Four new mechanical columns added (`exit_op`/`exit_threshold`/`exit_sustain`/`exit_source`). ML-RED-118.
6. **S26 hypothesis re-mark:** Stag 38→40 (+2, Fed-locked reconfirmed + Sept odds 71.5→77%) · Managed 32→28 (−4, absorption pattern broke, haircut applied) · Acute 13→15 (+2, WL-06 fired + VIX>20) · War 11→13 (+2, scored on its OWN axis per Guard 3 — Saudi co-belligerency; price/escalation divergence flagged for BRENT/HAWK, not adjudicated) · Rescue 2→2 (dead) · Soft 4→2 (−2, modest — labor data itself didn't move tonight). Net-bear 62→68, sum checks to 100.
7. **Ledger sweep:** PREDICTIONS.tsv RED-20 → RESOLVED CORRECT · docket/CATALYSTS.tsv FOMC row → resolved · ML-RED-117/118 added · STATUS.md (hypothesis table, counter-signals HY/CCC/VIX rows, falsification criteria table, predictions scorecard, bottom line) all updated.
8. **NOT done tonight (scope discipline, flagged not dropped):** harmful-revision ledger (PROME 7/25 ask) · BRK-32 register red-team offer to BROCK (7/27) · CHG-RED-027/028 status refresh beyond what FOMC grading touched · EGBN Q2 grade (still unlocated) · sinking-watch 7/26 outcome check.

## NEXT SESSION (dated, priority-ordered)
1. **🔴 FT-01's 3rd session** — pull the 7/29 HY OAS print as soon as FRED posts it (next business day) and close the un-fire clock (WL-03: 3 of 3 ≥280 → un-fires; a print <280 breaks the streak and resets).
2. **🟠 Fri 7/31: ECI Q2 08:30** — the Fed acted 7/29 without a current read of its preferred wage gauge; if ECI prints ~3.4% flat, log the composition-contamination as its own dated entry (Guard 3 discipline), never laundered into the FOMC cell.
3. **🟡 Owed, deferred from tonight's scope:** PROME's harmful-revision ledger task (7/25, P6 slice — no market gate, do at next boot per PROME's own priority) · BROCK's BRK-32 register-respec red-team offer (7/27) · EGBN Q2 grade · sinking-watch 7/26 · June MF-starts.
4. **🟡 Verify:** whether the Brent price/war-escalation divergence flagged tonight (kinetic footprint widening, price NOT re-approaching $100) resolves one way or the other in BRENT's next surface — do not carry RED's own War+2 without checking whether BRENT's own re-mark agrees or diverges.
5. **Daily:** HY vs 280 (WL-03, clock live) · CCC vs 1000 (WL-06, fired, watch for DISH 7/31 mechanical-tightening trap) · VIX vs 20/23 · Brent vs BRENT's own current book levels (do not cite this file's stale rows).
6. **~10/7:** pre-write the Sept-CPI core decision tree for the Wed 10/14 print (CHG-028's real test, unchanged by tonight).

## OPEN THREADS
- **Guard 3 (war/FOMC attribution confound) is now a LIVE unresolved question, not a hypothetical in a pre-reg doc.** Whoever next has fresher data on the Iraq strikes / Saudi retaliation-risk trajectory (BRENT/HAWK/OSPREY) may be able to help apportion tonight's VIX spike; RED cannot resolve it alone with market-close data.
- **CARL rationalization test still ARMED and dated** (unchanged from S25): ~8/15 HHDC benign-or-better AND V2 not 4→3 → scored rationalization finding against CARL.
- **CHG-027 capitulation-review condition still armed** (BDC + SBCF/EGBN benign) — note per PROME's 7/25 packet, the BDC marks cluster re-dated to 8/4-8/6 (POST-FOMC), not 7/25-28; STATUS's "TOP ADVERSARIAL PRIORITIES" section still carries the stale 7/25-28 window and needs a sweep next session (not done tonight — out of scope).
- **CHG-042 residual** = de-escalation decay-split, unexercised.
- **Claims 187K still sits at 75/25 bull** on the counter-signal table (unrefreshed tonight).

## PENDING WILL-DECISIONS
- None new tonight.
- Carried from S25: broker-confirm at convenience, OZK Jul-17 $42.5P ×2 expired dead-OTM.

## GIT STATE (one line)
On master. This session's commits (pathspec-scoped to `AGENTS/RED/`, not pushed by RED — auto-push per root protocol): STATUS.md/SCRATCH.md/LAST_COMPLETION.md + registry/workbook/docket/research updates for S26 FOMC grading + exit-semantics registry write + hypothesis re-mark.
