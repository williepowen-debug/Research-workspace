# BRENT SCRATCH — Sun Jun 14, 2026 (stale-data sweep + full workbook demotion; Orc 2-round cross-check; 4 commits pushed)

**Purpose:** Ephemeral session handoff — canonical "where are we / what next." Read at boot (SPAWN PROTOCOL step 2), rewritten in full at closeout (step 11). Disposable.

**Session arc:** Booted Sunday (markets closed) for a stale-data sweep; became a full workbook-triage session with Orc adversarial cross-check. Refreshed the stale TRACKER + STATUS, then **demoted all three dormant workbooks (KB/VX/FLOW) to archival**, corrected a load-bearing SPR error (KB-011), and **surfaced + FIXED a live-positioning thesis bug — the "350M operational floor" (THESIS v3.1→v3.2, §6241 verified against primary).** Supersedes the Jun-13 SCRATCH.

---

## ⚡ NEXT BOOT FIRST MOVES
1. 🔴 **Mon Jun 15 (MONDAY) convergence settle** — pull Mon settles first thing: Trigger #1 completion (3rd consecutive M1−M3 <$3; Fri $2.40 / Thu $2.67) + XLE re-eval (2nd consecutive sub-$88 Brent close; Fri #1 $87.20). [HAW-09/BRT-27 already resolved Jun 13.]
2. 🟠 **Wed Jun 17 EIA WPSR** (wk Jun 12) — gasoline datapoint #2 (deepening toward −5%? Trigger #2 clock) + SPR draw trajectory (vs the REAL 252.4M §6241 floor, NOT 350M — see below) + IEA OMR (June).

**✅ DONE this session — 350M-floor thesis fix (was the carried PRIORITY-1):** §6241 verified against primary (Cornell LII) — **the only statutory floor is 252.4M (§6241(h), limited authority); the emergency authority §6241(d) a Hormuz-shock release runs under has NO floor** (252.4M itself cut from 340M in 2021). **The "~350M operational floor" was the 2023 trough mis-cited.** Dropped the wrong "~150M." Corrected across STATUS / THESIS (v3.1→**v3.2**, CHANGELOG entry) / TRACKER / NEXUS_BRIEF (rev-10) / CATALYSTS + KB-011. Net thesis effect: near-term-bearish SPR leg runs LONGER (~97M / ~12 wks runway), medium-term "finite backstop" bullish leg DEMOTED. **No conviction change** (flat-price cautious-neutral).

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
- **350M-floor thesis fix — SURFACED + FIXED this session** (§6241 verified vs Cornell LII primary): corrected the SPR-floor framing across STATUS/THESIS(v3.2+CHANGELOG)/TRACKER/NEXUS_BRIEF/CATALYSTS. Real floors 252.4M (limited §6241(h)) / none (emergency §6241(d)); ~350M was the 2023 trough. Bearish branch runs longer; finite-backstop bullish leg demoted; no conviction change.
- **Auto-memory (committed + pushed `242062df`):** `finding_workbook_demote_by_verification`.

## NEXT SESSION (dated, future-verifiable)
1. **Mon Jun 15** — convergence settle (Trigger #1 completion + XLE re-eval). Pull settles. [350M-floor fix DONE this session — no longer carried.]
2. **Wed Jun 17** — EIA WPSR gasoline datapoint #2 + SPR path; IEA OMR.
3. **Thu Jun 18** — CF $130C expiry (ride; zero bid) + Baker Hughes (Juneteenth-moved).
4. **Fri Jun 19** — CFTC COT (Jun 9 wk): first capturing halt+settlement; forced-liquidation watch on underwater spec length.
5. **~Jun 20** — prune BRT-27 catalyst row from `docket/CATALYSTS.tsv` (1-wk retention).

## OPEN THREADS / WATCHES
- ✅ **350M-floor correction — RESOLVED this session** (§6241 verified; THESIS v3.2; corrected across all live docs). No longer open.
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
- **NEXUS_BRIEF.md:** refreshed Jun 14 (rev-10 — SPR-floor CORRECTED flag + v3.2 version refs).
- **THESIS.md → v3.2** (SPR-floor correction) + CHANGELOG v3.2 entry; **CATALYSTS.tsv** Jun-10 SPR row annotated. PREDICTIONS unchanged; no DUE-stale.
- **GIT:** committed+pushed this session: `0efa6930` stale-sweep · `0d568609` KB · `9729c81a` VX · `c87c00ac` FLOW · `88277df3` closeout · `242062df` auto-memory. **PENDING (uncommitted): the v3.2 SPR-floor correction batch** — STATUS + THESIS + CHANGELOG + TRACKER + NEXUS_BRIEF + CATALYSTS + this SCRATCH. Commit + push next.
