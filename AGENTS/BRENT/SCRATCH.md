# BRENT SCRATCH — Mon Jun 22, 2026 PM (Monday confirms Phase-2-in-price → THESIS v4.2)

**Purpose:** Ephemeral session handoff — the canonical "where are we / what next" file. Read at boot (SPAWN PROTOCOL step 2), rewritten in full at closeout (step 11). Disposable. Supersedes the Jun-20 SCRATCH.

**Session arc:** Booted Mon Jun 22 PM (after Will-coordinated pull — already synced). Processed 3 Jun-21 WALTER signals. Ran a verification sweep (`wf_21dca756-c61`, 4 finders + adversarial synth) to ground the Monday read — it **confirmed de-escalation** and surfaced two things I didn't have at boot: (1) the **US Treasury 60-day Iranian-crude license** + concluded 60-day roadmap = the first *supply-return mechanism*; (2) the boot $78.14 was an after-hours tick, real **settle $77.90**. Bumped **THESIS v4.1→v4.2 (minor)**, corrected STATUS, wired a real **LIVE mode into eia_weekly.py**, and closed out. **4 session commits PUSHED to origin** — swept by a CARL/WALTER push-train (`pull --rebase` + push); SHAs rewritten, work content-verified on origin.

---

## ⚡ NEXT BOOT FIRST MOVES
1. 🔴 **Wed Jun 24 ~10:30 ET — EIA WPSR (wk-6/19)** — now ONE command (live): `python3 AGENTS/BRENT/scripts/eia_weekly.py`. Watch **Cushing sub-20M → Boundary #3** (flag PROME → LIQUID/HENRY/RED); **SPR remaining-authorization barrels**; **gasoline datapoint #3** (Trigger #2 clock). eia_ cache TTL 5min — run a few min after release.
2. 🔴 **Fri Jun 26 — CFTC COT (Jun 16 data)** = the FIRST post-MOU forced-liquidation read → **XLE stub decision** + Trigger #3 re-arm. Validate the record-short washout magnitude (ICE Brent MM net length 2026-low; specs ~1M bbl from Dec ATH) against the actual print.
3. 🟠 **Re-derive Brent 6-mo curve** from the BZQ26/BZV26 strip to confirm/deny contango — currently [EST] (a Jun-5 snapshot still showed backwardation).

## CHANGES SINCE LAST SESSION (Jun 20 → Jun 22)
- **Brent fell $80.57 (Jun 19) → $77.90 settle (Jun 22, −3.3%, lowest since early March)** — the Sunday reopen did NOT gap up on Iran's Jun-20 Hormuz re-closure.
- **NEW (Jun 22): US Treasury 60-day general license authorizing Iranian-crude production/sale/transport** (~to Aug 21) + **Switzerland round CONCLUDED** with a 60-day roadmap (Hormuz deconfliction line, demining coordination, IAEA re-entry). The Jun-21 "walkout" was TRANSIENT.
- **HAW-11 RESOLVED UNFIRED** — zero Gulf energy-infra/tanker/mine events Jun 20-22; Iran re-closure declaratory (CENTCOM ~55 transits).
- **Record-short positioning** — ICE Brent MM net length at a 2026 low (174,807 lots, −43,283 wk); specs within ~1M bbl of the Dec ATH short (all COT as-of Jun 16, pre-MOU).
- **WALTER coordination (via Will):** Cushing now dashboard-native (FORGE dashboard, EIA v2); EIA API key set in gitignored FORGE/.env; my eia_weekly.py "LIVE mode" was a no-op (now fixed).

## WHAT I DID THIS SESSION
- **Processed 3 Jun-21 WALTER signals** (board_log + git mv): SIG-001 (walkout, noted), SIG-004 (Hormuz 15→3, acted), SIG-010 (spec-short washout, acted).
- **Verification sweep** `wf_21dca756-c61` (4 finders: tape / kinetic-HAW-11 / positioning / diplomacy + adversarial synth). Web-confirmed; settles cross-checked.
- **THESIS v4.1→v4.2 (minor)** + CHANGELOG entry (commit `c5cbd2c4`). Conviction UNCHANGED.
- **STATUS v4.2** — 4 corrections + JUN 22 PM section + dashboard/positioning refresh, 210 lines (commit `ff55e0aa`).
- **eia_weekly.py real LIVE mode** — full WPSR live via FORGE eia_fetch, 7 series validated, boot now live (commit `948d5e00`).
- **Closeout:** CATALYSTS (HAW-11 RESOLVED + SPR 17.5M refinement + XLE note); NEXUS_BRIEF v4.2 (Treasury license routed to HENRY/CARL/SAM/HAWK); this SCRATCH.

## NEXT SESSION (dated, future-verifiable)
1. **Wed Jun 24** — EIA WPSR (wk-6/19) via live eia_weekly.py: Cushing sub-20M (Boundary #3), SPR remaining, gasoline datapoint #3.
2. **Fri Jun 26** — CFTC COT (Jun 16) forced-liquidation read → XLE stub decision + Trigger #3 re-arm; + Baker Hughes (BRT-26).
3. **~early Jul (Jul 3 modeled)** — SPR re-auth decision; verify remaining barrels (only ~17.5M of 172M drawn) vs Jun 24 EIA.
4. **Re-derive Jun-22 M1−M3 / 6-mo strip** to stamp contango [CONF] or correct.
5. **Jul 8** — EIA STEO (July), first post-deal price-path revision.

## OPEN THREADS / WATCHES
- 🔴 **Re-escalation into a record-short book** — squeeze fuel; live vectors = Lebanon seam + Trump "take over Hormuz" threat (tape-tier). Un-invert trigger = a CONFIRMED kinetic Hormuz/energy event (vessel/mine/energy-infra strike OR JWC reclass/insurer pull).
- 🔴 **Cushing sub-20M / Boundary #3** — fires as soon as Jun 24.
- 🟠 **Contango UNVERIFIED [EST]** — re-derive from strip; load-bearing for Phase-2-in-price.
- 🟠 **Hormuz physical legs (0/4)** — liners off Cape = the cleanest reopening tell; ~22-27% dark transits (Windward).
- 🟠 **SPR re-auth (early July)** — 17.5M drawn vs 172M; "fully withdrawn" likely = first 86M tranche.
- 🟡 **Russian crude-export channel** (HAWK KB-187) — Brent-positive on export saturation OR Ukraine pivot to crude terminals.
- 🟡 **LIQUID HY-Energy-OAS pull** — owed, DEFERRED per Will Jun 20.

## POSITION DECISIONS PENDING
- **XLE $65C Sep 30** — HOLD on a short leash through Jun 26 (Will Jun 20 hold; v4.2 hold-not-lapse). HAW-11 unfired satisfied the "don't-lapse-pre-HAW-11" gate, but record-short asymmetry > the ~$42 salvage. **Don't sell-into-vol** (no bid, VIX 17.28). Reassess after Jun 26 COT + early-July SPR re-auth. Sell into any incident vol spike.
- **No new flat-price longs** — de-escalation confirmed + contango + crowded short = wrong regime to add length either way.

## MAIL STATE (one line per signal)
- **Inbox/WALTER:** 3 Jun-21 signals processed → board_log + git mv to processed/. Lane CLEAR.
- **Outbox:** no new acute outbox this session — the Treasury license + de-escalation routed via NEXUS_BRIEF SENDING (not outbox, per `[[feedback_outbox_restraint_for_push_friction]]`). Legacy undelivered cruft (Apr–Jun, HERMES-degraded) untouched.

## WORKBOOK HEALTH
- **eia_weekly.py now LIVE** — boot EIA monitor was silently reading stale Jun-5-week markdown all session; fixed (auto-LIVE via FORGE key, --local fallback). Series IDs validated 2026-06-22.
- THESIS → v4.2 + CHANGELOG entry. PREDICTIONS unchanged this session (no BRENT resolutions; HAW-11 is HAWK's). KB/VX/FLOW remain demoted/archival.
- **GIT:** the 4 session commits are **PUSHED to origin** — swept by a CARL/WALTER push-train (`pull --rebase` + push), which rebased the SHAs: THESIS v4.2 → `77fc285a`, STATUS v4.2 → `b8fe5303`, eia_weekly live → `9100a576`, closeout → `a093f0d1` (original local SHAs c5cbd2c4/ff55e0aa/948d5e00/42400721 were rewritten — `[[finding_forced_update_rebase_churn]]` + `[[finding_push_train_pattern]]`). Content verified on origin (THESIS v4.2 / $77.90 STATUS / fetch_live_metrics). Local HEAD == origin/master `0f3d646d`, tree clean. This SCRATCH git-note update is a small follow-up commit — local until the next push-train sweep.
