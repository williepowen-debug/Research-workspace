# BRENT SCRATCH — Sun Jun 14, 2026 (stale-data sweep + full workbook demotion; Orc 2-round cross-check; 4 commits pushed)

**Purpose:** Ephemeral session handoff — canonical "where are we / what next." Read at boot (SPAWN PROTOCOL step 2), rewritten in full at closeout (step 11). Disposable.

**Session arc:** Booted Sunday (markets closed) for a stale-data sweep; became a full workbook-triage session with Orc adversarial cross-check. Refreshed the stale TRACKER + STATUS, then **demoted all three dormant workbooks (KB/VX/FLOW) to archival**, corrected a load-bearing SPR error (KB-011), and **surfaced a live-positioning thesis bug — the "350M operational floor" — now queued for fix pending Orc's §6241 cite.** Supersedes the Jun-13 SCRATCH.

---

## ⚡ NEXT BOOT FIRST MOVES
1. 🔴 **350M-FLOOR THESIS FIX (PRIORITY-1)** — pending Orc's exact EPCA **§6241** statutory floors. STATUS/THESIS/TRACKER all say SPR "drained THROUGH the ~350M operational floor" — that 350M is almost certainly the **2023 trough (~347M) mis-cited as an operational floor**; real floors far lower (~150M statutory / ~252M non-emergency, exact pending). **Impact:** at 349M there are MONTHS of runway, so the "finite backstop / medium-term bullish" leg is NOT imminent and the near-term "marginal supply stays in market" bearish branch runs longer. Fix all 3 docs (incl. the TRACKER header **I** propagated it into this session) once Orc posts the cite.
2. 🔴 **Mon Jun 15 (MONDAY) convergence settle** (carried) — pull Mon settles first thing: Trigger #1 completion (3rd consecutive M1−M3 <$3; Fri $2.40 / Thu $2.67) + XLE re-eval (2nd consecutive sub-$88 Brent close; Fri #1 $87.20). [HAW-09/BRT-27 already resolved Jun 13.]
3. 🟠 **Wed Jun 17 EIA WPSR** (wk Jun 12) — gasoline datapoint #2 (deepening toward −5%? Trigger #2 clock) + SPR sub-floor path + IEA OMR (June).

## CHANGES SINCE LAST SESSION (Jun 13 → Jun 14)
- **Markets CLOSED Sat/Sun — no tape moves.** Boot.py Sun: Brent futures $87.33 / WTI $84.88 / USO $125.43 (= Friday Jun-12 closes; consistent w/ STATUS settles).
- **Other agents committed + swept to origin while I worked:** VIOLET 6/14 closeout (`7029fdf7`, STATUS/NEXUS_BRIEF/VIX_THESIS now current on origin), CARL 6/14 closeout (`4bdf816a`), LABOR 6/14 (`a26097d2`/`3a4b37a2`), auto-mem LABOR (`16291f03`).
- No kinetic/diplomatic delta processed this session (the sweep was data-hygiene, not news).

## WHAT I DID THIS SESSION
- **Stale-data sweep (`0efa6930`, pushed):** refreshed `demand_destruction/TRACKER.md` live sections (header + PATH B trigger table + verdict + Tier-1/2 dashboard + Jun-10 EIA log cell) — body was Apr/May-era while header read Jun 12. STATUS: removed stale HY-OAS dashboard row (LIQUID/VIOLET/HENRY own credit; BRENT's channel = crack-compression BRT-12); updated stale Jun-12 8:43AM intraday marks → Fri closes (WTI $84.88, USO $125.43); cleaned energy-credit convergence-vector note.
- **Workbook demotion — all 3 ledgers frozen (Orc 2-round adversarial cross-check):**
  - **KB.tsv (`0d568609`, pushed):** archival header (frozen Mar–Jun acute-war corpus; default disposition declared). **KB-011 SPR CORRECTED** ("~350M historic lows" was the 2023 trough mis-dated; real 2026 SPR ~413M→349M [CONF EIA], anchored on EIA NOT the D-3 KB-090 — **caught my own miscitation of a D-3 row as A-1 in the cross-check**). 6 D-3 LLM-generated rows (KB-089–094) → new **UNVERIFIED-RETIRED** status.
  - **VX.tsv (`9729c81a`, pushed):** lean demote (no triage — taxonomy superseded by STATUS convergence matrix); header points to that as live successor; verified zero live consumers.
  - **FLOW.tsv (`c87c00ac`, pushed):** demote; **FLOW-BRT-30 (8-threshold WALTER auto-dispatch contract) RETIRED** — verified dead WALTER-side (WALTER Jun-10 STATUS: BRENT "dormant-structural, no BOARD-intake, LIAISON-era backfill"; 0 dispatches ever; venue in CLOSED/). Rows 26–29 are transmission records (NOT contracts), mirrored live in CLAUDE.md → froze as historical, nothing stranded.
- **Surfaced (not yet fixed): the 350M-floor thesis bug** — see FIRST MOVES #1. Queued.
- **Auto-memory (uncommitted, pending sweep):** wrote `finding_workbook_demote_by_verification` (memory/auto/).

## NEXT SESSION (dated, future-verifiable)
1. **Next boot** — 350M-floor thesis fix (PRIORITY-1, on Orc's §6241 cite): STATUS + THESIS + TRACKER.
2. **Mon Jun 15** — convergence settle (Trigger #1 completion + XLE re-eval). Pull settles.
3. **Wed Jun 17** — EIA WPSR gasoline datapoint #2 + SPR path; IEA OMR.
4. **Thu Jun 18** — CF $130C expiry (ride; zero bid) + Baker Hughes (Juneteenth-moved).
5. **Fri Jun 19** — CFTC COT (Jun 9 wk): first capturing halt+settlement; forced-liquidation watch on underwater spec length.
6. **~Jun 20** — prune BRT-27 catalyst row from `docket/CATALYSTS.tsv` (1-wk retention).

## OPEN THREADS / WATCHES
- 🔴 **350M-floor correction** — pending Orc §6241; live-positioning framing overstates near-term scarcity.
- 🔴 **Dawn-#5 fade vs Trigger #1 completion** — ladder COUNTERED (Iran refused timeline Jun 13); if Trigger #1 completes Mon with no hardening → Phase 2 via Path B while physical draws argue snap-back.
- 🟠 **XLE re-eval clock 1/2** (sub-$88 close #1 = Jun 12; Mon = #2 candidate).
- 🟠 **Pump pass-through STALLED** — RB sticky ~$130, gas crack $42.55 vs WTI; CARL CRL-08 affected.
- 🟠 **BRT-12 crack-compression clock** — widening now; compression when products follow crude down = the early warning. Re-check each EIA Wed.
- 🟠 **WALTER routing-bug** — escalation sent Jun 13; awaiting fix confirm + fleet-vs-BRENT-only audit.
- 🟡 **Workbooks DEMOTED** — revive-vs-demote decision RESOLVED (all 3 archival). Live state owned by STATUS/THESIS/CLAUDE.md.

## POSITION DECISIONS PENDING
- **XLE $65C Sep 30** — HOLD; premise (sustained $90+ Brent) BREAKING. Re-eval on signed MOU OR 2 consecutive sub-$88 closes (clock 1/2; Mon = #2 candidate). Live clock inherited.
- **CF $130C Jun 18** — RIDE TO EXPIRY (zero bid; corrected mark $0.10; nothing decidable).
- **BRT-15 tanker** — TABLED; numeric conditional registered pre-outcome; arms only on hardened signing (currently counter-evidenced — STNG rallied into the announcement).

## MAIL STATE (one line per signal)
- **Inbox:** 1 reference artifact only (`2026-06-07_from-NEXUS_brief_pilot2_review.md`, not actionable). No new signals.
- **Outbox:** clear (top-level). ⚠️ **2 routing-bug signals (to PROME/WALTER, Jun 13) remain UNTRACKED in their inboxes** — outside my dir, can't commit; won't reach origin for pickup until a memory/cross-dir commit sweeps them. Flagged to Will Jun 14.

## WORKBOOK HEALTH
- **KB/VX/FLOW: DEMOTED → ARCHIVAL this session** (frozen; headers declare disposition). No longer live ledgers; revive-vs-demote question CLOSED.
- **NEXUS_BRIEF.md:** refreshed Jun 14 (rev-9 — stamp + SPR-floor pending-correction flag).
- **PREDICTIONS.tsv / CATALYSTS.tsv / THESIS.md:** unchanged this session (350M-floor fix will touch THESIS next session). No DUE-stale predictions.
- **GIT:** 4 commits this session, **ALL PUSHED** (`0efa6930` stale-sweep, `0d568609` KB, `9729c81a` VX, `c87c00ac` FLOW). Closeout commit (SCRATCH + NEXUS_BRIEF) pending — local, push next window. Auto-memory + MEMORY.md index line written but uncommitted (shared memory/, not mine to commit — flag for sweep).
