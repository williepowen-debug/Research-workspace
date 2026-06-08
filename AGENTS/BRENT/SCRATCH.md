# BRENT SCRATCH — Mon Jun 8, 2026 (PM — protocol-coordination session)

**Purpose:** Ephemeral session handoff — the canonical "where are we / what next" file. Read at boot (SPAWN PROTOCOL step 2), rewritten in full at closeout (step 11). Disposable; rewritten every session. Persistent learnings live in `MEMORY.md`; dated forward catalysts live in `docket/CATALYSTS.tsv` (FASTOW); cross-agent synthesis lives in `NEXUS_BRIEF.md` (now the primary cross-agent channel).

---

## CHANGES SINCE LAST SESSION (Sun Jun 7 night → Mon Jun 8 PM)

- **Mon Jun 8 AM live tape:** Brent **$94.38 +1.39%**, WTI **$91.37 +0.92%** [CONF boot.py]. Modest bid post-OPEC+ Vienna Sun outcome (base case +188K July landed as expected — "paper + trapped behind Hormuz" → muted reaction). Consistent with my Sun PM "optically mildly bearish, functionally neutral" read.
- **Tanker complex still bid down:** STNG $75.74 (-0.29%), DHT $16.44 (-1.26%), FRO $34.92 (-0.71%). War-risk leg of BRT-15 staying unwound; no Mon AM regime change in tanker pricing.
- **VIX, energy services, equity — no boot.py refresh this session** (didn't run --verbose).
- **No catalysts fired** (next: EIA STEO Tue Jun 9).
- **No new kinetic events** in published feed since Sun closeout.
- **No predictions DUE** on light-touch scan.

## ADDENDUM — Jun 8 PM-2 (HAWK inbox process)

After main closeout, Will asked me to evaluate the HAWK→BRENT message (`HAWK/outbox/delivered/2026-06-08_to-BRENT_decoupling-thesis-plus-brt-27-28-scope-ask.md`). Verdict: high-value signal — independent convergence on decoupling regime + named falsification anchor (HAW-11 by Jun 22) + clean scope-clarification ask. Will gated full restructure.

**BRT-27 / BRT-28 SCOPE-NARROWED Jun 8** (event-shaped → price-consequence conditionals on HAW-09/HAW-10):
- BRT-27 new form: Brent <$92 within 5td if HAW-09 confirms; $94-100 hold if HAW-09 falsifies. Cond conf 55%.
- BRT-28 new form: Brent gap ≥$5 + curve steepens ≥$12/6mo within 3td if HAW-10 fires; range hold if expires. Cond conf 70%.
- Calibration delta resolved: BRENT's prior 65% on Iran-walkback was Trump-rhetoric-overweighted; deferred to HAW-09's 35%.
- Vessel-traffic-only path in original BRT-28 retired to HAWK (KB-HAWK-159 canonical).

**Files touched:** PREDICTIONS.tsv (BRT-27, BRT-28), STATUS.md (predictions table + OPEN-ITEMS #6/#7), CHANGELOG.md (entry above Jun 3 row), NEXUS_BRIEF.md (rev-5 with calibration row + As-of refresh), new outbox `to-HAWK` reply (closes their loop).

**NOT done:** FLOW.tsv BRENT counterpart row (workbook revive/demote decision still open with Will — see this SCRATCH's WORKBOOK HEALTH below). No THESIS v-bump (prediction-scope refinement only).

**Position implications:** None this session. BRT-15 tanker thesis still TABLED; XLE/CF positions unchanged. Restructured BRT-27/28 conditionals are observational, not actionable on their own.

---

## NEW THIS SESSION

- **Fleet-protocol coordination triggered by CARL.** CARL surfaced (via Will) that root `CLAUDE.md` Git Protocol "At session end: ... Push to GitHub" directly contradicts Will's standing rule `[[feedback_defer_push_coordinate]]` ("commit local, defer push until Will coordinates"). CARL fixed CARL's local step 16; flagged root as upstream cause.
- **BRENT independent corroboration:** I deferred my own pull at boot today because HAWK had 3 uncommitted files outside my dir — the existing "if blocked, defer" branch fired correctly. But absent that block, BRENT's closeout would default to push. Same latent bug, inherited from root.
- **Local fix (commit A):** added explicit line to **BRENT/CLAUDE.md step 14**:
  > "Default: commit locally only. Push only when Will has explicitly opened a push window. Push-train pattern applies only inside an authorized push window — outside it, commit and wait."
  Belt-and-suspenders so BRENT's local doc is unambiguous regardless of root state.
- **PROME outbox flag (commit A):** wrote `outbox/2026-06-08_to-PROME_root-claudemd-push-protocol-conflict.md` — durable record from BRENT (independent of CARL's parallel flag) covering: the contradiction, both agents' corroborating observations, what's been fixed locally, what remains upstream (root reconcile + retire/qualify `[[finding_push_train_pattern]]` + propagate SAM's gating). Note: telegram-nudge route for HAWK noted as N/A (only WALTER and PROME have telegram).
- **CARL's flag — gave Will my independent assessment:** agreed CARL is right on substance; refined that BRENT's local CLAUDE.md is more defensible than CARL implied (doesn't explicitly say "push" — inherits from root); flagged that the `[[finding_push_train_pattern]]` auto-memory itself may be outdated under the standing rule.

## WHAT I DID THIS SESSION

- Boot per SPAWN PROTOCOL (deferred pull due to HAWK uncommitted files outside dir; STATUS/SCRATCH/LESSONS read; boot.py 9.3s; predictions scanned — none DUE).
- Responded to Will's CARL-relay with ranked recommendations.
- Executed #3 (BRENT/CLAUDE.md step 14 explicit push-discipline line) and #4 (PROME outbox flag).
- Light-touch STATUS refresh (Mon AM tape line + stamp); NEXUS_BRIEF rev-4 stamp-only refresh.
- Closeout commits (A: protocol fix; B: closeout batch). NO PUSH per standing rule.

## NEXT SESSION (dated, future-verifiable)

1. **Tue Jun 9** — **EIA STEO (June)** — first post-suspension; Q2 Brent peak ($115 Apr) likely revised UP.
2. **Wed Jun 10** — **EIA WPSR (week Jun 5) = THE BIG PRINT.** SPR ~350M floor-touch (DIRECTIONAL — throttle bullish / drain-through near-term bearish + medium-term bullish, NOT symmetric). First clean post-MD demand read (BRT-08/09 candidate).
3. **Thu Jun 11** — OPEC MOMR (June), first post-Vienna.
4. **Thu Jun 12** — US CPI **(energy component = the clean separable test for the oil→CPI→Fed leg, isolable from AI-unwind noise per Jun-7 PM reframe).**
5. **Fri Jun 12** — CFTC COT (Jun 2 wk, post-suspension) = real Trigger #3 re-fire test; Baker Hughes (431 last, +2 WoW, vs 457).
6. **Sun Jun 15** — BRT-27 walkback deadline (trending partial-confirm).
7. **Thu Jun 18** — CF $130C expiry (~8 trading days from Mon close).
8. **~Jul 1** — Cushing 20M floor (modeled); BRT-28 Bab al-Mandab window closes.
9. **Every closeout** — refresh `NEXUS_BRIEF.md` (step 12). Keep SENDING/WAITING-FOR fresh — that IS BRENT's cross-agent comms now.

## NEXT SESSION (Tier 2 — carried forward)

10. **THESIS.md v3.1 bump candidate** — gate on Jun 9 STEO + Jun 10 EIA + Jun 12 CPI as the converging evidence batch.
11. **FASTOW Run 2** — cheap (~3-5 min; monthly trigger doesn't fire until Jul 1).
12. **Workbook KB/VX/FLOW** — dormant 6+ wks; revive-vs-demote decision still OPEN with Will.
13. **Crack-spread refresh** (last Mar 27 $42 3:2:1) — BRT-12 channel test setup.

## OPEN THREADS / WATCHES

- 🔴 **Macro transmission** — multi-root reframe holds. Standing oil→CPI→Fed leg untested by Fri; clean separable test = **Jun-12 CPI energy component**. Watch HY OAS catch-up (LIQUID primary).
- 🔴 **SPR ~350M floor (Wed Jun 10)** — directional, not symmetric.
- 🟠 **CF chain-decoupling** — Mon AM mark check deferred (no boot.py CF row this session); revisit at next boot.
- 🟠 **BRT-15 re-arm** — fresh kinetic-with-facility-damage / US-Iran direct exchange / Hormuz vessel attack / barnacle re-surfacing.
- 🟠 **Trigger #1 (M1-M3 ≤$3)** — likely re-steepened FAR from threshold; ICE CONF pending.
- 🟡 **HY energy OAS catch-up**, crack refresh, dated-Brent-Platts (terminal-only).

### Fleet-protocol thread — queued for Will / PROME
- **PROME outbox flag dropped this session** (`2026-06-08_to-PROME_root-claudemd-push-protocol-conflict.md`). Will to coordinate root CLAUDE.md reconcile + retire/qualify `[[finding_push_train_pattern]]` + propagate SAM's gating pattern. Until then, BRENT's local fix holds.
- **Push queue** — shared `master` has 2 unpushed local commits (`66c6be00` CARL + `ca854ccf` BROCK); BRENT's two closeout commits will join the queue. Will to coordinate the push window. No agent pushes until then.
- **HAWK uncommitted** — 3 files (STATUS.md, board_log.tsv, workbook/KB.tsv) still in shared tree. Will to nudge (telegram is WALTER/PROME-only per Will's Jun 8 clarification).

### NEXUS_Brief thread — queued for LIVE NEXUS (its calls, not BRENT's)
- **Amendment-9 (CASCADE sub-block)** — real heavy-domain gap; raised in pilot-2 review.
- **Amendment-10 (acute-vs-steady marker)** — soft; brief is primary channel now.
- **Light-end pilot still un-run** — HAWK nominated.
- **Cap** — BRENT (81) co-anchors with SAM (75) for "heaviest real domain"; provisional 100 holds.
- **Fallback instrumentation LIVE in NEXUS** (proxy-applied Jun 7) — awaiting live-NEXUS review on its next boot.

## POSITION DECISIONS PENDING

- **CF $130C Jun 18** — HOLD CONFIRMED (Will, Jun 1 PM). ~8 trading days. CAVEAT: chain-decoupling pattern. Revisit if Mon AM mark + first move vs USO shows continued decoupling. **Mon AM mark not pulled this session** — revisit at next boot.
- **XLE $65C Sep 30** — HOLD. XLE not refreshed this session (no boot.py --verbose); Fri close was $57.67, strike $7.33 OTM. Kinetic-tail insurance NOT being paid on escalation-without-damage. 4mo runway is the asset.
- **Tanker BRT-15** — TABLED Jun 4 (Option B). War-risk leg fully unwound; Mon AM tape confirms (STNG/DHT still bid down). Re-arm watch above.

## MAIL STATE (one line per signal)

- **Inbox:** 1 item — `2026-06-07_from-NEXUS_brief_pilot2_review.md` (pilot-2 reference artifact; not processed-moved per Sun PM note).
- **Outbox:** 2 items —
  - `2026-06-07_to-NEXUS_fallback_rate_instrumentation.md` (spec; already applied live to NEXUS, record-only — HERMES delivery moot)
  - **🆕 `2026-06-08_to-PROME_root-claudemd-push-protocol-conflict.md`** (this session — durable record of root CLAUDE.md push-protocol contradiction + BRENT's independent corroboration + local fix + upstream asks)

## WORKBOOK HEALTH

- **`NEXUS_BRIEF.md`:** LIVE, rev-4 stamp-refresh this session (no content change — no material STATUS change to propagate). 81 lines, hash points to `ce65758f` (Sun PM macro-reframe commit, current canonical STATUS state).
- **`thesis/PREDICTIONS.tsv`:** green; no DUE-stale rows. No changes this session.
- **`docket/CATALYSTS.tsv`:** green; FASTOW-maintained; next FASTOW run not due until ~Jul 1.
- **`workbook/KB/VX/FLOW.tsv`:** DORMANT 6+ wks — Tier-2 revive/demote decision open.
- **`thesis/THESIS.md`:** v3.0; v3.1 bump candidate gated on Jun 9 STEO + Jun 10 EIA + Jun 12 CPI batch.
- **`refinery_damage/INCIDENTS.tsv`:** 35 rows; green; no new facility-damage (kinetic all intercepts).

## GIT STATE

- **Commits this session (all within AGENTS/BRENT/):**
  - **A** (this closeout — protocol fix): CLAUDE.md step 14 explicit push-discipline + new `outbox/2026-06-08_to-PROME_*` flag
  - **B** (this closeout — light refresh): STATUS.md (Mon AM stamp + tape line) + SCRATCH.md (rewrite) + NEXUS_BRIEF.md (rev-4 stamp)
- **HAWK** has 3 uncommitted files (STATUS.md, board_log.tsv, workbook/KB.tsv) — left untouched per `[[feedback_agent_git_isolation]]`. They do NOT block these path-scoped commits.
- **Push: NO** (per Will's standing `[[feedback_defer_push_coordinate]]` + newly-written BRENT step 14 default). Will coordinating the push window. Queue: CARL `66c6be00` + BROCK `ca854ccf` + BRENT A + BRENT B (4 commits) will ride together when Will opens the window.

## NEW AUTO-MEMORY THIS SESSION

- **No new promotions this session.** The protocol-bug-finding is well-captured in the PROME outbox file + BRENT's local CLAUDE.md edit; it's operational-fleet-coordination work rather than a transferable thesis-level lesson. The pre-existing auto-memories that fired and held the line are: `[[feedback_defer_push_coordinate]]`, `[[feedback_agent_git_isolation]]`, `[[feedback_cross_agent_inbox_writes]]`, `[[project_openclaw_prome_degraded]]`. The candidate-for-retirement is `[[finding_push_train_pattern]]` (flagged in PROME outbox; Will-scope decision).
