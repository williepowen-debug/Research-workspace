# BRENT SCRATCH — June 1, 2026

**Purpose:** Ephemeral session handoff — the canonical "where are we / what next" file. Read at boot (SPAWN PROTOCOL step 2), rewritten in full at closeout (step 11). Disposable: rewritten every session, not appended to. Persistent learnings live in `MEMORY.md`; dated forward catalysts live in `workbook/CATALYSTS.tsv`; this file is the bridge between sessions.

---

## CHANGES SINCE LAST SESSION
- **Brent gapped +4.40% to $95.13 at Mon Jun 1 open** (from Fri $92.05 close). WTI +5.15% / Tanker complex +2.4% (STNG $76.33 / DHT $16.72) / VG +6.60% (Hormuz-LNG arb) / Natgas −3.62% (tape pricing as oil-specific, not broad energy-systemic).
- **Iran (Tasnim, IRGC-aligned) SUSPENDED indirect (Pakistan-mediated) US talks Jun 1 AM** — cites Israel's Lebanon incursion; explicitly threatens "complete closure of Hormuz + activate Bab al-Mandab" (NEW chokepoint vector). MOU went rumor → "mostly agreed" → walked in <7 days.
- **CENTCOM intercepted 2 Iranian ballistic missiles targeting Kuwait bases overnight Sun→Mon May 31** — 2nd Kuwait-targeted volley in 4 days (pending primary-source verify per LESSONS #1 before INCIDENTS.tsv).
- **Trump/Rubio response not yet on record Mon AM** — gates whether MOU is dead or on ice.

## WHAT I DID THIS SESSION
- **Boot + Mon news sweep** — Tasnim suspension + CENTCOM Kuwait intercept surfaced as Jun 1 events; explained the gap-up.
- **STATUS.md 3-chunk rewrite (Jun 1 ~14:00 ET):** Header + verdict inverted to PHASE 1 RE-ARMED; price dashboard refreshed live (11 tickers); convergence matrix recalc 42/60 → 46/65 with Bab al-Mandab NEW vector + upgraded Brent price + Tanker scores; two-phase thesis + Path A/B + KEY OPEN ITEMS + Summary-for-Will + POSITIONS all updated; catalyst calendar updated with Jun 1 FIRED row + new watches.
- **PREDICTIONS architecture Tier 1 rehab (SAM-aligned):** 
  - Status renames (T1-A): NOT-FIRED → FAILED (BRT-23/24 direction errors); NOT-FIRED-PRECONDITION (BRT-20/25); RESOLVED-MECHANISM-CONFIRMED/THRESHOLD-UNTESTABLE (BRT-22)
  - Built `thesis/PREDICTIONS_ARCHIVE.md` (T1-B): 17 post-mortems by Pred_ID, ~250 lines; closed-row Notes condensed to ≤265 chars + anchor links
  - Scoreboard preamble + relocation + reference updates (T1-C): tsv moved workbook → thesis/ via git mv; preamble has tally + directional failures + calibration findings + pre-flight check; CLAUDE.md / THESIS.md / handoff_WALTER updated
- **2 new predictions added:** BRT-27 (Iran walkback within 14d, 55%), BRT-28 (Bab al-Mandab operational within 30d, 45%).
- **Cross-agent memory refresh:** `[[finding_threshold_vs_mechanism]]` updated with BRT-23 as first non-SAM case — pattern now 3-of-3 cross-agent validated. Additive evidence, not new rule.
- **thesis/CHANGELOG.md:** Two new entries — Phase 1 RE-ARMED (intra-version POV pivot per `[[finding_pov_changelog_pattern]]`) + Predictions Architecture Rehab.
- **Committed `8779db33`** (7 files, +397/-128). Push pending — see git note below.

## NEXT SESSION (dated, future-verifiable)
1. **Mon Jun 1 PM / Tue Jun 2** — Trump/Rubio response to Iran suspension; dead-vs-on-ice gate; watch for Plan B activation announcement; Iran walkback signal.
2. **Wed Jun 3** — EIA WPSR (week May 29): Cushing <20M? gasoline YoY post-Memorial-Day clean read; SPR floor proximity.
3. **Fri Jun 5** — CFTC COT (May 26 — first post-Fri-drop, PRE-suspension data); Trigger #3 re-fire watch. Also Baker Hughes (BRT-26 rigs vs 457).
4. **Sun Jun 7** — OPEC+ regular meeting (REFRAMED: into suspended-MOU regime, not falling-price).
5. **~Jun 15** — BRT-27 walkback deadline (Iran re-engages within 14d of Jun 1 suspension?).
6. **Wed Jun 11** — STEO June (first post-suspension; Q2 Brent peak likely revised UP not down).
7. **Wed Jun 18** — CF $130C expiry.
8. **~Jul 1** — BRT-28 Bab al-Mandab 30-day window closes.

## NEXT SESSION (Tier 2 architecture priorities — per Path B closeout)
9. **BRENT-KOYOMI build for CATALYSTS.tsv** — read SAM/docket/KOYOMI.md spec fully; adapt to BRENT's catalyst types (EIA weeklies, OPEC, position expiries, refinery damage events). Pair with state file BRENT-KOYOMI_MEMORY.md. Fresh-context build per Path B handoff rationale.
10. **BRENT-KURA assessment** — workbook KB.tsv / VX.tsv / FLOW.tsv dormant 6+ wks per Sunday's audit. Decide revive vs demote in CLAUDE.md step 8; if revive, KURA-style librarian sub-agent is the leverage.
11. **Predictions-adjacent mechanical sub-agent (Idea B from this session)** — predictions-due scanner + pre-flight checker + calibration analyst. Worth evaluating alongside KOYOMI/KURA; possibly fold into KURA scope or stand alone. Predictions JUDGMENT stays with BRENT-the-main-agent per SAM architecture.
12. **THESIS.md substantive rewrite** — currently published as v3.0 "Phase 2 PRICING dominant via diplomatic"; Jun 1 inverted that. Defer until Trump/Rubio response disambiguates. CHANGELOG entry today documents the POV pivot without v-bump.
13. **CATALYSTS.tsv comprehensive refresh** — STATUS calendar carries Jun 1 events but tsv needs sync; Trump response window + walkback deadline + Bab al-Mandab watch all need rows. Candidate for first BRENT-KOYOMI smoke test.

## OPEN THREADS / WATCHES
- 🔴 **MOU suspension durability** — daily; gated on Trump/Rubio response + Iran walkback signal (BRT-27 deadline Jun 15).
- 🔴 **Bab al-Mandab credibility (NEW vector)** — rolling: Houthi proxy activity, Bab corridor vessel-traffic, freight-rate response. BRT-28 tests within 30d.
- 🔴 **Cushing 20M floor (~early-mid June)** + **SPR 350M floor (~1.5-2 wks)** — physical squeeze now interlocking with no-deal-relief.
- 🟠 **Trigger #3 re-fire** (Jun 5 COT first post-Fri-drop; Jun 12 COT first post-suspension).
- 🟠 **BRT-26 shale response** (rigs 429 → 457; Baker Hughes Jun 5 + weekly).
- 🟠 **Tanker BRT-15 channel-mix-shift** — original ton-mile-on-Iranian-return gate dead; war-risk leg firing; entry decision pending Will.
- 🟡 **E&P Q1 capex breaks** (CXO/OXY/EOG/MRO — more breaks weaken BRT-04 forward thesis).
- 🟡 **HY energy OAS catch-up** — credit dismissed Brent −20%; if doesn't widen on Jun 1 suspension, mechanism-vs-threshold note.

## POSITION DECISIONS PENDING
- **CF $130C Jun 18** — HOLD-with-pop-re-eval (Will 5/31), TESTED Jun 1 with modest pop (+1.62% / +$1.82; CF $114.17 vs $130 strike, ~12.2% OTM, ~17 days to expiry). Decision: close-on-further-pop-above-$115 vs hold-to-expiry-as-overlap-insurance-with-XLE. **Needs Will read on continuing intraday tape.**
- **XLE $65C Sep 30** — HOLD (now THE live scenario, not a tail; ~12% OTM narrowed from $8.71 to $7.75; ~4mo to expiry).
- **Tanker BRT-15** — entry gating may be wrong-sided (war-risk leg firing today; original ton-mile gate deferred). STNG $76.33 (+2.44%) / DHT $16.72 (+2.45%). **Needs Will decision: initiate now or wait?**

## MAIL STATE (one line per signal)
- **Inbox:** clear (cross-agent intake on hold per `[[project_messaging_overhaul]]` — file-based messaging being replaced).
- **Outbox:** clear (cross-agent signals deferred per same direction).

## WORKBOOK HEALTH
- **`thesis/PREDICTIONS.tsv` (NEW LOCATION):** REHABBED this session (SAM-aligned). 28 rows (11 OPEN). 26-line scoreboard preamble at top. Health: green.
- **`thesis/PREDICTIONS_ARCHIVE.md` (NEW):** 241 lines, 17 post-mortems. Reference-only, not boot-loaded.
- **`workbook/CATALYSTS.tsv`:** notes-refresh needed for Jun 1 events (Trump response window, Iran walkback deadline, Bab al-Mandab watch). Sync needed with STATUS calendar (which is current). **NEXT-SESSION priority + candidate for BRENT-KOYOMI scope.**
- **`workbook/KB.tsv` / `VX.tsv` / `FLOW.tsv`:** DORMANT 6+ weeks (flagged in Sunday's SCRATCH; still pending). **OPEN DECISION for Will: revive vs demote in CLAUDE.md step 8.** Candidate for BRENT-KURA scope.
- **`thesis/THESIS.md`:** Stale framing — published as v3.0 "Phase 2 pricing dominant via diplomatic"; Jun 1 inverted this. Deferred to next session pending Trump/Rubio response disambiguation.
- **`refinery_damage/INCIDENTS.tsv`:** Jun 1 Kuwait intercept not yet logged (LESSONS #1: verify CENTCOM primary source before transcribing).

## GIT STATE
- **Last commit:** `8779db33` (Jun 1 STATUS rewrite + Tier 1 predictions architecture). 7 files, +397/-128.
- **Post-commit work this session:** thesis/CHANGELOG.md entries (Phase 1 RE-ARMED + Tier 1 rehab) + this SCRATCH rewrite. Both stage-clean but not yet committed.
- **Push status:** NOT yet pushed to origin. Will-approval needed for session-end push. Other agent (SAM/TRADE.md) has uncommitted work outside BRENT — does not block BRENT push.
- **Next session boot:** check origin sync; if SAM committed in interim, follow pull protocol.
