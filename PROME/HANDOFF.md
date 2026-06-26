# PROME HANDOFF

**Purpose:** Single live continuity surface for Prome across OpenClaw and Claude Code. Keep this file short: latest 3–5 entries only. Archive older entries to `PROME/archive/`.

**Archive:** Full pre-merge OpenClaw + Claude Code handoff history through 2026-06-14 is preserved in `PROME/archive/HANDOFF_2026Q2.md` (older 2026-06 entries appended there as they roll off).

---

## 2026-06-26 ~13:00 ET — Standing rule + detection/action hardening cluster + arch peer-review (committed local, push pending)

**Status:** Long working session off Will's current book (2 images). Arc: bank-put **reshape proposal** built → Will set the **STANDING RULE** (deploy only on a fired trigger; $500/card) → **detection/action HARDENING cluster** (LIQUID/SENTRY/TERRY, Prome-directed teams-mode) → **arch peer-review + fix round** → **HEARTBEAT reconcile** → closeout. **All committed locally; NOT pushed** (Will-coordinated). 3 agents released.

**What landed:** (1) `PROME/proposals/2026-06-26_bank-put-reshape-roll.md` — shelved as the ready "if HY 280" card. (2) Memory `feedback_deploy_on_trigger_not_calendar`. (3) **P1 detection** — `config.py` retuned (HY 265/280, 10Y 4.40, wrapper series; closes the "281 reads GREEN" hole) + **live `liquid-hy-watch` systemd timer** (Mon–Fri 13:00 ET, enabled+active, VERIFIED firing 278→amber → `AGENTS/LIQUID/alerts/`). (4) **P2/P3** — `AGENTS/TERRY/scripts/chain_fetch.py` (live chain CLI), `TRADE_CARD_TEMPLATE_FIRE.md` + 2 setups ($500), `grade_print.py` (Jul-print grader, 3 traps as hard guards). (5) **Arch fix round** — LIQUID STATUS 28→7KB + watcher `--selftest` (8 PASS) + X1 dedupe→KILL_MEMO; TERRY +MEMORY +CLOSEOUT +honest STATUS. (6) HEARTBEAT reconciled (HY→278, X1→KILL_MEMO, auto-watch noted). Records in `PROME/cluster/`.

**The read:** no market trigger fired — this was a **maintenance + system-hardening** session, NOT a new-conviction entry. Live **HY 278 [6/25], 2bp from the >280 X1** (grinding 271→276→278). The detection blind spot is now closed: the timer auto-catches a 280 cross between sessions.

**Next / pending:** Push the whole session (5 earlier commits + closeout batch) at the next Will window. WILL/trading-journal: 3 journal deletions (Will-intentional) + 2 book JPGs left untouched, Will's to commit. The shelved (b)/(c) card fires only on HY>280 sustained or WAL Jul-30 — max-loss $500, needs live broker book at fire-time. 10Y 6/30 re-pull still scheduled.

## 2026-06-26 — Verification pass (Tier-1 banks + Tier-2 labor): corrections applied + PUSHED

**Status:** Ran the queued `VERIFICATION_PASS_2026-06-26` action-card as two verify->adversarial->propagate Workflows — `wzmprhwb2` (8 Tier-1 banks vs EDGAR 10-Q / FDIC Call Report) + `wzlhvzlcb` (5 Tier-2 labor groups vs FRED/BLS/CBO). ~24 load-bearing Q1'26 figures checked, each adversarially re-pulled. **PUSHED** — origin master `903e7f4b`, synced 0/0 (`d1cbbafe` corrections + `903e7f4b` route packets).

**What landed:** 17 stamped `[CORRECTED/VERIFIED 06-26]` edits across the 3 synthesis docs + `PROME/proposals/2026-06-26_tier1-verification-results.md` (full scorecard). Tier-1: 11 ok / 9 delta / 5 conflict / 3 unverifiable. Tier-2: 8 ok / 5 delta / 3 conflict / 1 unverifiable. 3 upstream route packets placed in LABOR/MARCO/CORAL inboxes (next-boot SIGs).

**The read:** **both theses SURVIVE.** (b) AOCI + (c) WAL stay the live Q2 exception; (a) consumer-source + labor stay 2027. Material catches (none move a path's odds): ALLY "released $224M" -> +$50M BUILD (growth-driven=collective, non-counting); ZION muni "$5.78B AFS" -> ~$869M (re-anchored on total AFS); WAL "$99M charge-off" -> outstanding CRE loan balance, appraisal-pending (not a realized loss); WAL 39bps = NON-GAAP adjusted (GAAP 1.45%); EGBN CRE 547% -> 295.1% (now below the 300% threshold); labor +93K revisions were UP not down, "31-mo" -> ~37-mo Information-sector, prof-biz openings "<1M" false, 2.2M removals = DHS-disputed not CBO (realized LF ~1.0M). **Meta-finding: the synthesis docs were CLEANER than their STATUS-file inputs** — most labor errors lived upstream in LABOR/CORAL/MARCO, the synthesis layer had already filtered them.

**Decisions / next:** Tier 3/4 (macro/regime — HY/CCC, the 10Y 6/30 re-pull for path (b), bank prices) deliberately NOT run; those are live-pull-at-trade levels (rule #4), not static baselines. The 3 route packets await LABOR/MARCO/CORAL next-boot processing. Housekeeping this session: MEMORY.md pruned 25.9->23.0KB (under the load cap, all 158 links preserved); HANDOFF rolled the 06-21 x3 / 06-22 / 06-25-morning entries to `archive/HANDOFF_2026Q2.md`.

## 2026-06-25 ~20:40 ET — Front-half "Three Masks" de-mask cluster + adversarial + reconciliation + Jul grading instrument (committed local, NOT pushed)

**Status:** 2nd orchestration of the day. Will ran the **front-half de-mask cluster** as PERSISTENT teams-mode agents Prome directed live across rounds (CARL_FH=credit / LABOR=labor / MARCO=migration), + a **5-lens independent adversarial round** (HOLDS-WITH-ADDITIONS), + a **full front↔back reconciliation** (REGINALD_T re-spawn), + a **Jul-print grading instrument**. **4 agents RELEASED at closeout** (no warm-parking — new lesson after tonight's CARL name-collision sweep). RESEARCH/DRAFT-ONLY throughout; wrote nothing canonical. Committed local; **push pending** (Will-coordinated).

**What landed — 3 new `PROME/synthesis/` docs:** `2026-06-25_front-half-demask-cluster.md` (v2, post-adversarial), `_front-back-reconciliation.md`, `_Q2-bank-print-grading-instrument.md`.

**The read:** the consumer/labor/migration SOURCE is a **2027 story** (calm ~50-55% genuine; masks roll forward; Jul prints likely reinforce the all-clear → roll duration to Q1-27, no Q2 short). **Reconciliation key result:** the front/back "conflict" was a **ledger-line artifact** — provision/ACL **BUILD = Q2-visible** (doesn't defer); realized **NCO = 2027**. The front-half **TRIMS the consumer-source path** (a ~25-35%→~15-22%) and leaves **(b) AOCI/rates ~25-30% + (c) WAL ~28-32% = the live Q2 exception.** Single grade = **Provision$ vs NCO$ (BUILD/RELEASE) + specific-vs-collective**(=beta). LABOR: labor = white-collar structural GRIND → 2027-diffuse, ~30% Aug-7 option (a real 31-mo white-collar recession masked by the immigration supply floor). **COF = the bridge** (segment provision split: Card=Axis A / Commercial=Axis B); **ZION muni/AOCI = top mis-grade risk.**

**Decisions / handoffs for Will:** route (1) FORGE duration-roll, (2) REGINALD/CORAL winter-27 FL-$ ~$850M (floor ~$450-700M), (3) NEXUS feed (refresh-hold). Trade construction for (b)/(c) = the Will-gated next thread (needs the book).

**Next:** Jul forward-watch via the grading instrument (CFG/OZK Jul16 → monolines+ZION Jul21 GATE → EGBN Jul22 → WAL Jul30; COF date confirm ~early Jul; 10Y re-pull 6/30). Push the 3 docs next window. Lessons captured: `feedback_warm_parked_agent_collision`, `finding_cluster_adversarial_catches_framing`. MEMORY.md prune + HANDOFF trim-debt (roll 6/21 entries) still deferred.

## 2026-06-25 ~17:30 ET — Transmission-terminus cluster orchestration + pre-Q2 adversarial stress-test (PUSHED)

**Status:** Same-day continuation. Will ran an orchestration exercise — spawn 3 agents Prome directs/builds with — and chose the **transmission-terminus cluster** (CARL=consumer / CORAL=FL banks / REGINALD=bank-terminus hub) over Prome's trigger-cluster (LIQUID/BROCK/RED) pick. Full arc delivered + **PUSHED**: origin master `92a92a83`, synced **0/0**, 24 commits (22 cluster + 2 Prome: FXY/git stale-row fixes + the synthesis doc). Three agents parked warm (pending Will release).

**What landed:** A Q2-Print Bank-Transmission Convergence Grid — *does credit stress LAND on bank balance sheets?* Pass-1 legs → verified 10-Q reconcile → finalized grid + CCC/HY >3.6× tripwire (VX-REG-18.04, dormant 3.49×). Then a Will-approved **pre-Q2 adversarial stress-test**: Wave-1 self-steelman (3 genuine hits — CARL category error → unsecured bifurcates H2-26; CORAL wrong-signed "cooling"; REGINALD diagnostic altitude-mismatch) + Wave-2 independent blind-spot critics + judge (non-credit channel unwatched / ZION false-control; monolines unscored; one-directional bias → WAL over-claim). Verdict **HOLDS-WITH-ADDITIONS**, all 5 additions implemented.

**The read:** systemic-2027 floor holds for *realized synchronized charge-offs*, but it's **less "nothing until 2027," more "three live ~25-35% Q2-able paths the green tape isn't pricing"** — (a) synchronized reserve-build ≥2 banks IS Q2 transmission; (b) non-credit/AOCI selloff (10Y +11bp = live-but-mild; ZION re-registered off-credit); (c) WAL >55bps + $99M charge-off (~30-35%, not 70%). Two-axis model: Axis A unsecured/monoline-lead/H2-26 vs Axis B regional-terminus/Q1-27; **COF = dual-axis standout.** Durable doc: `PROME/synthesis/2026-06-25_transmission-terminus-cluster.md`; pre-registered playbook in `AGENTS/REGINALD/research/Q2_PREREG_ADVERSARIAL_2026-06-25.md`.

**Regime delta:** **FXY position CLOSED (Will 6/25)** — old broker-truth open item resolved, long-FXY tail given up. HY 276 [6/24] (4bp from >280 X1), conviction 61. The non-credit/AOCI channel newly on the watch list.

**Next:** Q2 forward-watch (10Y re-pull 6/30; monoline prints Jul 15-22; regionals Jul 16-30, WAL Jul 30 on magnitude; CCC/HY daily). NEXUS-handoff package ready (gated on Will's refresh-hold). Auto-memory capture + MEMORY.md prune still deferred. Three cluster agents warm pending release.

## 2026-06-25 ~15:55 ET — Warm-LIQUID deep-cleanup arc (11 commits, PUSHED)

**Status:** Will ran a **persistent warm LIQUID #1** (directable) + a **read-only LIQ_DOCAUDIT** boot-doc auditor to get LIQUID caught up to data and its architecture working smoothly. Full arc done, independently verified at each step, **PUSHED** — origin master swept the session's 11 commits (10 LIQUID/PROME + closeout), local+origin **synced 0/0**, tree clean. Both agents released.

**What landed (the arc):** PAUSED→ARMED relabel (KB-063); Track-1 STATUS reconcile + **Track-2 KB.tsv 56-row drift fix + boot.py selftest KB-guard + KB-062 backfill**; 6/24 inbox (metals = **washout-not-crunch**); **boot-doc batch — boot.py was flashing false all-clears, wired in the >280 X1 alert rung + flipped APO sub-$130 to bearish** + MEMORY 314→117 lossless split; **KILL_MEMO rebuilt two-sided** (added the >280 X1-confirm side = PROPOSE→Will never auto-execute; book-flat); VX/FLOW de-masqueraded; **thesis re-mark 60→61** (held +1 from proposed +2 per Will calibration → KB-064).

**Regime delta:** **HY OAS 276 [6/24]** — the print resolved WIDER, now **4bp from the >280 X1-trigger**. Conviction **61, CONCENTRATED/higher-variance** — the bear funneled to one live root (credit-bifurcation, CCC-BB 798) while the other legs inverted/dormant (energy deflated, plumbing calm, duration dormant); X1 UNFIRED (widening is beta not substance). **FXY position FULLY CLOSED (Will 6/25)** — old open item resolved.

**Next:** LIQ-03 resolves 6/30 (boot.py-tracked); BDC monitor full-populate before ~7/25 Q2 marks; auto-memory capture of the KB-064 calibration principle + X1 rule deferred pending the MEMORY.md prune (over-limit); LIQUID outbox cleanup (low). Watch the next HY print vs 280 + the wrapper basket.

---
