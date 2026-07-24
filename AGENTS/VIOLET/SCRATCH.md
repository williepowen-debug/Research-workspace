# VIOLET SCRATCH — July 23, 2026 (Will-directed sit-rep boot)

> **⚡ 7/23 INTRADAY (~12:15 ET) — THE 7/21 DIVERGENCE RESOLVED THE BEARISH WAY.** Over 7/22-7/23 the equity-vol front end that faded to complacency Monday (VIX 17.05) re-firmed UP to rejoin the elevated tails/cross-asset: **VIX ~19.86** (+2.81, back at the 20 line), **VVIX 105.29 re-crossed >100** (from 96.34), **VIX3M/VIX 1.071 re-compressed toward inversion** (from 1.149). SKEW held 150.19. The independent stress vectors all remain firing — **MOVE ~74.67 [7/21] re-open FIRED**, credit **Bin-A** (CCC 9.77/disp 8.17), **OVX ratio 3.55/p97.6 FIRE**, **COT 7/14 pct3y 99.4 extreme-long**; JPY carry CALM (MOF 7/22 passed clean, USDJPY 163.82). **Four of five independent vectors on the stress side simultaneously = the strongest alignment of this de-compression, and the equity-vol surface has now JOINED it. Still short of a confirmed crack: the two completing legs — term-structure inversion (<1.0) and VIX>20 break — are NOT met (both close). Strengthening-candidate loading into FOMC 7/29 (4 td).** KB-VIO-122 filed. No position.

## NEXT SESSION (priority-ordered)

1. **🔴 FOMC 7/29 (4 td) — the catalyst path.** First FOMC of the Fed-HIKE regime; tests 6/17 dot-flip follow-through. Watch the two crack-completing legs into/through the decision: **VIX>20 break** (at 19.86 now) + **term-structure inversion VIX3M/VIX <1.0** (at 1.071 now). Inside buyback blackout + 7/29-8/1 megacap earnings cluster.
   - **🟣 POST-FOMC: refresh BOTH Will-facing Artifacts (SAME URLs)** — Will-approved living references; edit the repo sources in `AGENTS/VIOLET/artifacts/` then republish passing `url=`:
     1. **Vol cheat-sheet** (gauges *concepts* explainer) — `vol_cheatsheet.html` → `url=https://claude.ai/code/artifact/c2129279-b677-4093-be68-ccdbe0df76b3` · memory `reference_violet_vol_cheatsheet`. Update the dated snapshot strip only.
     2. **Operating Picture** (live agent state + how-to-read-the-agent) — `violet_operating_picture.html` → `url=https://claude.ai/code/artifact/8eb52313-be4e-49a3-8555-e5cc23b44c60` · memory `reference_violet_operating_picture`. Update the LIVE STATE band only (regime, gauge tiles, channels, instrument states, posture, next decision points); the explainer band / taxonomy / routing are durable.
2. **🔴 Grade the COT lev-money print Fri 7/24 3:30** (report-date 7/21). Does pct3y 99.4 extreme-long PERSIST / deepen / unwind? Auto in boot.py via cftc_cot.py; report-date-verify (don't grade stale 7/14).
3. **🔴 CHECK LIQUID / HENRY / BOND OUTPUTS FIRST — all three were spawned live 7/23 eve (Will).** Their answers may already be on disk; **look before re-asking.** Read their `STATUS.md` / `SCRATCH.md` / `NEXUS_BRIEF.md` (and any VIOLET-addressed outbox note) for:
   - **HENRY** — dealer gamma SHORT into FOMC? SPX still at the flip band? *(the pivotal input; short-gamma = the case for a fresh non-duplicative tail add)*
   - **LIQUID** — CCC/disp widening FRESH vs stuck-wide at Bin-A? *(highest-weight crack confirm, KB-VIO-088 primary)*
   - **BOND** — actual **MOVE closes for 7/22 + 7/23** (my web feed lags ~1 session; latest confirmed ~74.67 [7/21]) and whether the 68.5→70.9→72.7→74.7 re-escalation is still extending or rolling over. *Ask added 7/23 eve, hand-relayed by Will — NOT in the outbox memo (which only covers HENRY+LIQUID via PROME).*
   **Grade whatever lands against the locked KB-VIO-123 tree — do not re-derive the branch map.** Two independent confirms landing before the Fed (e.g. HENRY short-gamma + LIQUID fresh-widening) converts this from a watch into a live decision.
4. **🟠 Web-verify MOVE** — only if BOND hasn't supplied it. ~74.67 [7/21] is the latest posted; the 7/23 print wasn't up yet (Yahoo/CNBC ~1-session lag). Re-open stays FIRED unless MOVE reverses toward N1 <66 (far off).
4. **🟠 Term-structure + VIX>20 watch** — the two missing legs; both within a hair. An inversion (<1.0) OR a VIX>20 settle would flip "strengthening-candidate" toward "confirmed crack."
5. **🟠 jpy_vol IV/RV post-MOF** — MOF 7/22 passed clean; now watch whether IV/RV (2.75×) collapses toward 1× (risk-passed, event behind) or holds (residual carry risk into FOMC/BOJ).
6. **🟣 cheap_tail.py now live in boot** — watch it flip DORMANT→ARMING→OPEN if vol re-compresses to the floor (VVIX≤90 + VIX≤16 both needed). Currently 2/4 DORMANT (SKEW+catalyst met; the two cheap legs not). If it goes OPEN, surface the vehicle menu to Will as a decision.
7. **🟡 Carried refreshes:** 20d SKEW avg recompute · M1:M2 detail · broad equity put/call · HY/BB ladder · VIX9D (not in this run's threshold output).
7. **🟡 VULCAN S1** (Path-B capex) — now has SIG-002 ($1.65T off-B/S hyperscaler debt) + SIG-008 (SMCI Q4 prelim) feeding it; fold in ahead of the 7/29-8/1 megacap stack. Sets NDX-SPX IV-dispersion canary line.
8. **⚪ PAT-032 note to DAEDALUS** (L4 packet all-6 applied 7/11) — cross-dir write, route via PROME. Still owed.

## WHAT I DID THIS SESSION

1. **Booted** (git pull clean; boot.py 9.2s all-green; both staleness guards clean). Live surface: VIX 19.86 / VVIX 105.29 / VIX3M-VIX 1.071 / SKEW 150.19 (all TICK, pre-settle); credit Bin-A CCC 9.77/disp 8.17 [7/20]; COT 7/14 pct3y 99.4; OVX ratio 3.55/p97.6 FIRE; JPY RV p9.8 CALM.
2. **Web-verified MOVE** — ~74.67 latest (Yahoo/CNBC), which is the 7/21 close; 7/23 not yet posted. Re-open stays FIRED.
3. **Delivered the sit-rep to Will** — the 7/21 divergence resolved UP; front-end rejoined the independent stress; strengthening-candidate not confirmed crack (inversion + VIX>20 legs unmet); FOMC 7/29 catalyst path.
4. **Processed WALTER inbox** (boot step 5a): SIG-002 ($1.65T off-B/S hyperscaler AI-infra debt) + SIG-008 (SMCI Q4 FY26 prelim) — both AI-capex INFO, action=VULCAN → info-only, board_log +2, files → processed/. Folded into the concentration/Path-B fragility stack (with SOX-bear SIG-007 + dealer-gamma-halved SIG-009).
5. **Registered KB-VIO-123** — crack-vs-fade pre-registration (locked confirm/fade tree before COT 7/24 + FOMC 7/29). Routed HENRY GEX (short-gamma into FOMC?) + LIQUID credit-freshness asks via outbox→PROME (FLOW.tsv logged).
6. **BUILT cheap_tail.py (KB-VIO-124)** — Will-directed after the 7/10 post-mortem. Operator-decision SETUP alert (NOT a gate, NOT auto-execute): fires 4/4 on VVIX≤90 · VIX≤16 · SKEW≥140 · HIGH/MED catalyst ≤21d = the cheap-tail window (complacency floor). Backtest 4.04% of history (31 episodes 2007-) = rare, not a bleed machine. Validated: 7/6-7/10 fires (the miss it prevents), today DORMANT 2/4. Boot-wired; new CHEAP_TAIL.tsv ledger; CANARY_MAP Tier-1; MAINTENANCE entry.
7. **Write-backs:** STATUS full 7/23 refresh; KB-VIO-122 (front-end re-firm); CATALYSTS.tsv pruned (fired 7/2-7/16 + MOF 7/22 removed, FOMC 7/29 gains crack-leg watch) + CALENDAR twin synced; this SCRATCH; NEXUS_BRIEF refresh.

## CARRY-FORWARD

- **Regime one-liner:** LOW_VOL at the RISING_VOL boundary (VIX 19.86). The 7/21 front-end/tail divergence resolved UP — front-end re-firmed to rejoin the independent stress (MOVE re-open FIRED, credit Bin-A, OVX FIRE, COT extreme-long; JPY calm). Four of five independent vectors firing; two crack legs (inversion <1.0, VIX>20) unmet = strengthening-candidate. No position.
- **Biggest open loop:** does FOMC 7/29 (or the run-up) complete the crack — VIX>20 settle + term-structure inversion — or does the front-end fade again (Monday's move in reverse)? Next COT 7/24 3:30 is the mid-week discriminator.
- **Counterparty agents LIVE as of 7/23 eve:** Will spawned **LIQUID, HENRY, BOND** in parallel windows and hand-relayed my asks directly (faster than the outbox→PROME path, which HENRY/LIQUID don't read at their own boot — *routing lesson: an outbox note addressed to PROME is invisible to the target agent until PROME relays it*). Their answers may land on disk without any signal to me. **Next boot: read their surfaces before re-asking or re-deriving.**
- **Data caveats:** surface values are intraday TICK (pre-16:15 settle — VX_DAILY 7/23 row is TICK basis, supersede after 16:15 next session); SKEW/credit T-1 FRED/CBOE lagged; COT is 7/14 positioning; MOVE ~74.67 is the 7/21 close (7/23 web not posted).
- **Gate:** GATE-VIO-116 re-open FIRED (MOVE >70-72); consequence = fold-into-TRY-FIRE-004 (FILLED, 30× TLT Sep-30 77P live), NO new standalone trade; route TERRY→Will.

## OPEN HYPOTHESES (flagged, NOT actionable until backtested)

- **VVIX-leads on this cycle's de-compression:** VVIX has now crossed >100 twice (7/17, 7/23) with VIX still ≤20 and term structure still (barely) in contango — is vol-of-vol the first gauge to move in a complacency unwind? Two instances now; watch whether VVIX>100 precedes a VIX>20 break.
- **Front-end re-firm-to-meet-stress vs stress-fade-to-meet-calm:** the 7/21→7/23 resolution is the first observed instance in this de-compression where a front-end/tail divergence closed by the FRONT-END rising rather than the tail falling. Does the direction of divergence-closure predict follow-through? N=1.
- **COT lev-money net-long as a positioning lead:** the −18.9k→−2k→+5.1k→+10.2k trajectory into a flat-then-rising VIX — 7/24 read is instance three of whether sophisticated positioning leads spot vol.

---

*Last updated: 2026-07-23 ~12:15 ET (Will-directed sit-rep boot + full write-back). Complete: sit-rep delivered (7/21 divergence resolved UP, strengthening-candidate); MOVE web-verified (~74.67 [7/21]); WALTER inbox processed (SIG-002/008 info-only); STATUS/KB-VIO-122/CATALYSTS+CALENDAR/NEXUS_BRIEF written. Top next: FOMC 7/29 crack-leg watch (VIX>20 + inversion <1.0), COT 7/24 3:30, jpy_vol post-MOF. No position; GATE-VIO-116 re-open FIRED (fold-into-004). Prior: 2026-07-17 ~16:20 ET (catalyst-day closeout — COT DEEPENING, OVX built).*
