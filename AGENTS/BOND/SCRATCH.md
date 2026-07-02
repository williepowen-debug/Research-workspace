# BOND SCRATCH — 2026-07-01

**Purpose:** Ephemeral session handoff. Read at boot, rewritten at closeout. Persistent learnings → `MEMORY.md`; durable thesis → `thesis/THESIS.md` (v1.1); live state → `STATUS.md`.

---

## CHANGES SINCE LAST SESSION (6/20 → 7/1, 11-day gap)
- **The long end re-engaged (phase III), globally synchronized:** 30Y 4.97 close 7/1 (+11bp/2d, 3bp from threshold) — domestic hawkish-data repricing (JOLTS 7.594M beat, ISM prices 73, Dec-hike ~79–82%) co-firing with a **JGB super-long rout** (6/30: 30Y JGB +8.8bp; 6/25 20Y JGB = weakest demand since May-2025; yen 162 = 40-yr low). Mid-window USTs had rallied to a 7-wk low (10Y 4.38) — the re-fire is 2 days old.
- **6/23–25 cluster cleared benign (6th straight)** but composition rotated: indirects <60% at 2Y (55.45) / 7Y (57.55), −13/−21pp m/m, absorbed ~1:1 by directs. FR2004 (6/17) made a **fresh all-time record** (11–21Y $74.6B) — dealer-absorption →4 trigger ARMED.
- **Predictions:** BND-02 FAILED (Apr–Jun = issuance BOOM), BND-04 FALSE (CLO AAA never through 160; MM near-miss 158), **BND-10 VOID** (kinetic Iran clause: Kiku tanker struck IN the Strait 6/27; substantive no-breach read recorded). Armed **BND-11** (7/7–9 refunding benign, 70%) + **BND-12** (30Y no sustained >5.0 through 7/24, 65%).
- Credit: HY 263→283→275 (equity-beta episode 6/24–26, Apple price-hike shock); CCC 970 non-retrace; IG 76 with RECORD June (~$175–187B). CDX-proxy z-breach 6/24–26 **failed the sign-check** (co-move, not divergence).
- Fed: Warsh Sintra 7/1 deferred balance-sheet/MBS-sales **"years, not months"** (2027 lane); WALCL rising (no active QT); quarter-end clean (SRF $0; SOFR-IORB +3bp benign).
- **Mandate extension integrated** (6/27 SIG): MBS/FHLB/EU-rates now BOND's (CLAUDE.md updated; VX-17/18/19 baselined; ECB is HIKING — depo 2.25%, OAT-Bund 77). HERMES refs removed per protocol-audit SIG. BOND-SWEEP-B applied (If_Falsified_Action column on PREDICTIONS.tsv).

## WHAT I DID THIS SESSION
1. Boot + git sync; processed **4 WALTER SIGs** (KB-057/058/059 + 5Y-tail verified into KB-060) and **4 general-inbox items** (PROME coverage-extension, PROME protocol-audit, SAM JGB ask, PROME DAEDALUS batch02 packet) — all → `inbox/processed/`.
2. Live pulls (FRED 13 series, yfinance 9 tickers, cdx_proxy) — FRED key works post-scrub (`.env` per-machine home). Computed CL1–2Y rolling corr for WALTER's ask: **30d +0.40 decaying, NOT inverting** (KB-058).
3. **8-leg Workflow research fan-out** (auctions/FR2004/Fed/credit/today-driver/Iran/JGB/new-mandate; ~580k tokens, 0 errors) covering the 11-day gap; all load-bearing figures from primaries where pinnable, flags carried.
4. Resolutions + write-back: PREDICTIONS (3 resolved, 2 armed, new column), KB-057→068, VX 16 refreshed + 3 new, FLOW (FL-08 reframed FX-routed, FL-09 corroborated, **FL-BND-11 new**), CATALYSTS rewritten (17-row July docket), 4 monitors refreshed, **THESIS → v1.1** + CHANGELOG, TRADE.md, STATUS full rewrite (composite 11→**12/35**).
5. **Replied to SAM** (`outbox/2026-07-01_to-SAM_jgb-transmission-read.md`): decoupled-via-duration verdict, FX/intervention leg armed, 3 baseline corrections (their levels were pre-rout 6/29 vintage).

## NEXT SESSION (dated, future-verifiable)
1. **Thu 7/2:** FR2004 as-of 6/24 (~4:15pm ET) — record check → dealer-absorption 3-vs-4 decision. Treasury announces 7/7–9 sizes. 10Y JGB auction result (vacuum down-curve test). H.4.1 for 6/30 quarter-end posts.
2. **Tue–Thu 7/7–9: mini-refunding = THE gate.** Resolve **BND-11** from TreasuryDirect primary (7/9 30Y heaviest; predicates in the row). A marker → TLT add re-arm + LIQUID signal.
3. **Daily:** 30Y vs 5.0 (BND-12 sustain-count); USD/JPY 165 / MOF actual intervention (FL-BND-11 trigger); DFII10 vs 2.5 (retraced to 2.20 — no longer "the one rising vector").
4. **7/24:** resolve BND-12. **End-July:** resolve BND-01 (HY 275; needs +75bp — low prob).
5. Housekeeping: re-pin Dec-hike odds from CME FedWatch directly (7/1's 82% is mirror-derived); verify ECB GovC date (7/23 vs 7/24) + QRA 8/5 before relying; EU xccy-basis proxy build (converge with LIQUID); Freddie Q1 net worth (Fannie done).

## OPEN THREADS / WATCHES
- 🟠 **Demand-hole configuration pre-positioned:** record dealer stock + fading indirects + 30Y 3bp from threshold + supply gauntlet — everything but the trigger (a failed auction). Six straight benign says it keeps not firing; 7/9 is the test.
- 🟠 JGB-FX channel (FL-BND-11): verbal-intervention stage; actual = mechanical UST reserve selling. Joint read with SAM if it fires into refunding week.
- 🟡 CCC 970 non-retrace (default-cycle tail); June US HY monthly total unpinned until LCD/SIFMA ~mid-July.
- 🟡 Energy HY OAS: structurally unpinnable publicly — stays [STALE Apr 28]; needs ICE via LIQUID.
- 📋 Packet 7 (NEXUS_BRIEF.md) still the remaining closeout gap. New: EU xccy proxy build; CC-MBS spread series/proxy before VX-17 thresholds are operational.

## POSITION DECISIONS
- **TLT puts: HOLD, no add** — tape rotated toward the thesis but no pre-registered gate fired. Add-gates: DFII10 >2.5 / 30Y >5.0 ×5 + weak auction / BND-11 FALSE marker.
- **HYG puts: stay closed** (issuance boom). Credit-equity lead inactive (needs +75–100bp off 263 trough).

## MAIL STATE
- Inbox: **clear** (8 items processed → `inbox/processed/`: 4 WALTER + 2 PROME SIGs + SAM ask + PROME DAEDALUS packet).
- Outbox: 1 sent — SAM reply (🟠, requested deliverable). No 🔴 signals warranted.

## WORKBOOK / PUSH HEALTH
- KB through **KB-BND-068**; VX 19 vectors (16 + 3 new-mandate); FLOW 11 (FL-11 new); PREDICTIONS: BND-01/11/12 OPEN, all others resolved, If_Falsified_Action column live (BOND-SWEEP-B).
- Commits path-scoped BOND-only; auto-push via `scripts/safe-push.sh` at closeout per current protocol.
