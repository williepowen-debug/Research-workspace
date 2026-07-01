# BRENT SCRATCH — Wed Jul 1, 2026 (full-file "get everything current" pass: EIA wk-6/26 + fresh cycle low → 3 predictions resolved → live surfaces refreshed → stale ledgers frozen)

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

**Session arc:** Boot at 2:10 PM (WALTER inbox clear) → boot.py delivered the EIA WPSR wk-6/26 print LIVE (the #1 next-boot item) + a fresh Brent cycle low → Will asked to get ALL BRENT files current → I assembled a scoped list, got "proceed in order" + delegated the freeze-vs-catchup call → executed 5 chunks: ①verify ②resolve BRT-08/28 (+caught BRT-09) ③sync 6 OPEN preds ④refresh live surfaces ⑤forward-state + froze 4 stale ledgers. **All committed + auto-pushed.**

---

## ⚡ NEXT BOOT FIRST MOVES
1. 🔴 **Fri Jul 3 — CFTC COT (Jun-30 kinetic-week data)** — the read that matters: short-COVERING (Tier-2 convex-arm lean) vs continued LIQUIDATION (structural holds) + Trigger #3 2nd-decline. Re-pull main ICE Brent net too.
2. 🔴 **~Jul 3 — SPR 172M auth fully withdrawn → DOE re-auth decision** — the buffer-clock deadline.
3. 🔴 **~Jul 2/3 — Baker Hughes** (440 last, +7; 17 to 457; deceleration test lands mid-Jul).
4. 🟡 **THE key decision watch: the NEXT EIA (wk-7/3) — does Cushing BUILD AGAIN + draws keep decelerating?** A 2nd deficit-closing print = the up-whipsaw genuinely dissolving → **convex-arm auto-disarm approaching (v5.1 trigger)**. This is now the single most decision-relevant thing I'm watching.
5. 🟡 **CHASE HAWK on HAW-15** (crude-export pivot — Tier-1 convex-arm trigger; HAWK STATUS Jun-27, unfired, window to Jul-15). Also track reopening 2nd-derivative (P&I resumption / liners-off-Cape).
6. 🔴 **Jul 8 — EIA STEO (July)** first post-deal price path.

## CHANGES SINCE LAST SESSION (Jun 29 → Jul 1)
- **Brent broke to a FRESH ~4-mo cycle low $71.36 (−2.14%)** under the ~$72 Jun-27/28 trough; **WTI $68.32 broke $70.** Decoupling EXTENDING.
- **EIA wk-6/26 (live): the FIRST "deficit-closing" data point.** Cushing BUILT +0.71M to 19.67M (first build; sub-floor drain reversed = reopening barrels landing); commercial −3.77M / SPR −5.54M / distillate +2.48M (all crude draws DECELERATED); gasoline 4-wk YoY −2.58% (never −5%); util 96.6%. → race leans gentle-normalization → **softens the v5.0 upside-convex tail** (one print, not a reversal).
- Refiners +4.38% on a crude-down day = cracks WIDENING (BRT-12 compression still absent; z ~+1.3σ exhausted). Rigs 440 (+7).

## WHAT I DID THIS SESSION (full-file update pass)
- **Predictions:** RESOLVED **BRT-08** (gasoline never −5% → DIR-CONFIRMED/THRESHOLD-UNREACHED), **BRT-28** (HAW-10 expired unfired → MECHANISM-CONFIRMED/THRESHOLD-MOOT), and **BRT-09** (caught as Q2-window-passed → MECHANISM-CONFIRMED/LEAD-LAG-INCOMPLETE). Synced the 6 remaining OPEN notes (07/12/16/17/21/26) to Jul-1. Header recount: OPEN 8→6. All 28 rows 10-col-intact.
- **Live surfaces refreshed:** STATUS (rewritten current, 184 lines — new Jul-1 section, dashboard, storage, Path-B, convergence matrix 47→44, predictions, summary; June compressed to trajectory), TRADE.md (Jul-1 race read; USO ref $103.82), CHANGELOG (Jul-1 WATCH note, **NO version bump** per Will-delegated call — v5.1 trigger registered), NEXUS_BRIEF (rewritten; cross-domain SENDING/WAITING refreshed), TRACKER (Jul-1 banner + Trigger #2 resolved + weekly-log row).
- **Forward-state:** CATALYSTS.tsv pruned (fired pre-Jul-1 rows) + refreshed forward (11 rows, event-set matched to STATUS calendar). INCIDENTS: **decided Kiku is HAWK's** (vessel/UAV = military op, not facility damage) — no BRENT row.
- **Data-Hygiene FREEZE (decision A — my call, Will can veto):** froze **KB.tsv / VX.tsv / FLOW.tsv / TIMELINE.md** with banners (16-day / 2.5-mo stale; live knowledge flows through STATUS/THESIS/PREDICTIONS/TRACKER). KB was CRLF — froze binary-safe, CRLF preserved. Chose freeze over catch-up (catch-up just duplicates the maintained surfaces + resumes rot).

## OPEN THREADS / WATCHES
- 🔴 **The TIMED RACE — first data point landed, leaning normalization.** Near-term 0.70 hold unchanged; medium-term up-whipsaw SOFTENED at the margin (not gone). Watch the 2nd deficit-closing print (see NEXT BOOT #4). Counter-weights still live: P&I not resumed (~0-1/4 verified legs), demining weeks-to-months, two rising Russian crude fuses (HAW-15).
- 🟡 **Convex arm = ARMED, no capital; today leaned AWAY from it (no trigger).** Fires on Tier-1 (HAW-15 pivot / reopening-stalls-while-buffers-empty) or Tier-2 (Brent >$75 ×2 / durable collapse). Auto-disarm approaching on a 2nd deficit-closing print. Full plan: TRADE.md. Will [Approve] at fire.
- ✅ **Open-items knock-out (Jul-1, post-currency-pass):** (1) **Energy credit** — broad HY OAS 275bps (−5bps, Jun-30) = calm, well <400bps; energy-only OAS needs LIQUID's paid source (no free FRED series). (2) **Japan** — crude stocks at 4-yr low CORROBORATED (qcintel/Bloomberg → SAM). (3) **HAW-15 = CLEANLY UNFIRED** (Russian crude exports at 2026-high ~3.83M bpd, KB-187). **Jul-1 SELF-CORRECTION:** the crude-export-port strikes (Ust-Luga/Primorsk/Novorossiysk) were **Mar-Apr, NOT June** — I misread a June-published Carnegie recap as June events; ports RECOVERED (Ust-Luga +49% MoM May, CREA), June+ = refineries → **HAWK's "refineries-only June" framing was RIGHT** (retracted my discrepancy flag). **Added the attacks to INCIDENTS** (RF-035 Primorsk, RF-036 Novorossiysk; RF-011 Ust-Luga → RESOLVED w/ recovery note). **Remaining → Jul-3 COT:** main ICE Brent MM net + M1-M3 curve (no free COT fetcher; .NYM Brent proxies unreliable).
- ✅ **Boot gaps ADDRESSED:** (a) window-passed prediction scan **WIRED into boot.py** (`predictions_due.py` — flags 🔴DUE/🟠SOON-≤7d; sanity-tested it would've caught BRT-08/09/28); (b) `scripts/ledger_staleness.py` still missing → **routed to PROME** (`outbox/2026-07-01_to-PROME_ledger-staleness-script-missing.md`); moot for BRENT's now-frozen ledgers.

## POSITION DECISIONS → see `TRADE.md` (canonical)
- **v5.0 stance UNCHANGED: no flat-price length either way; forward = defined-risk long-convexity, deploy-on-trigger.** No capital today (data leaned away from the arm). XLE $65C Sep-30 = LAPSE (deep-OTM backstop). Conditional Phase-2 short = DORMANT.

## MAIL STATE
- **Inbox/WALTER:** CLEAR (nothing new; last batch drained Jun-29 → processed/). **Outbox:** none new (HAWK reconciliation via NEXUS_BRIEF, not outbox). HAW-15 re-verify + BRT-28-resolved-unfired flagged to HAWK via NEXUS_BRIEF.

## WORKBOOK HEALTH
- **LIVE & current (Jul-1):** STATUS (184 ln), TRADE, NEXUS_BRIEF, CHANGELOG, PREDICTIONS.tsv (6 OPEN), TRACKER, CATALYSTS.tsv (11 fwd rows), SCRATCH (this). **THESIS v5.0 unchanged** (no bump; Jul-1 is a CHANGELOG watch note).
- **FROZEN Jul-1:** KB.tsv, VX.tsv, FLOW.tsv, TIMELINE.md (banners point to the live surfaces).
- **GIT:** all committed + auto-pushed this session. Predictions resolved: BRT-08/09/28. No new KB/VX/FLOW rows (frozen).
