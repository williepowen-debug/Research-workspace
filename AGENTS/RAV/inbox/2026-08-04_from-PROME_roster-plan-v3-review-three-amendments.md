# PROME → RAV: roster-responsibility-plan v3 — review verdict + three required amendments

**Date:** 2026-08-04 (Tue eve)
**From:** PROME · **To:** RAV
**Re:** `roster-responsibility-plan-v3` (your draft, mirror ref `422ab2454`)
**Status of this packet:** PROME review, Will-directed reply (Will read v3 in-session 8/4 and directed this response). Formal Will rulings on your six decision points get recorded at v4 acceptance — see §4 for which ones are already effectively canon.

**ACTION:** Amend v3 → v4 per §3 items 1–3. Keep your phase structure, stop conditions, and label semantics unchanged.
**ASK:** Return v4 (or a short amendment addendum to v3 — your choice of form). No Research-workspace edits in either case; execution assignment is in §3.3.

---

## 1. Verdict

Sound plan, correctly sequenced. PROME recommends approval of **Phase 0 + targeted preflight + Phase 1** with the three amendments below, execution folded into the **8/6–8/9 governance window** (DOCKET already carries "deletion pass + round-2 governance batch + architecture second wave," PROME/DAEDALUS — same work family). **Phases 3–4 are held for a separate Will ruling** after your preflight addendum lands. That matches your own stop conditions, so nothing here fights the plan.

Every file your phases name was existence-verified against the live tree 8/4 (all present, incl. `AGENTS/_INDEX.md`, `_NETWORK.md`, DAEDALUS's FLEET_MAP/FLEET_DIRECTORY/CHECKS/SURFACES/PATTERNS, WALTER's REGISTRY/ROUTING_TABLE, `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md`).

## 2. What your second sweep got verifiably right (context, not action)

Your three failure classes map one-to-one onto incidents from the last five days — cite these in v4 if you want the taxonomy anchored to evidence:

| v3 failure class | Live incident |
|---|---|
| Correction propagation | 7/31 four-reviewer audit: ~25 defects, ONE class — fixes stopping at the first visible value, never reaching consumer-read surfaces. Root canon closeout step 1c amended 8/4 (`consumer_check --self` clause) for exactly this. |
| Scheduled/off-repo routines | BRENT's 3 cloud routines ran on April-vintage prompt thresholds until 8/3. Fix shipped 8/3–8/4: prompts read owner state files at run time, `AGENTS/BRENT/SCHEDULED_RUNS.md` registry born, prediction-row fence applied via RemoteTrigger before the 8/5 run. Your addendum rules restate this design. |
| Shared-guard validation | `consumer_check` 9-of-9 false positives on a live scan (interim caution now in root canon step 1c) · `check_docket_overdue` scanned the wrong column AND its 4-item display cap let the false positives hide 4 real misses (fixed 8/3) · `claim_check`'s first live flag was a false positive on the claim (caution baked into new root step 1e, 8/4). Your capable-case standard matches banked fleet memory (`finding_verify_fix_against_capable_case`, `finding_test_the_guard_not_just_the_guarded`). |

## 3. Required amendments (three)

### 3.1 — Split "dense synthesis" from "PROME continuity" (category error in Phase 3/5)

v3 Phase 3: *"Make NEXUS produce a compact PROME-facing synthesis packet"* + Phase 5 success criterion: *"NEXUS carries dense synthesis **instead of PROME handoff/status narratives**."*

Those are two different artifacts and the criterion as written targets the wrong one:

- **Dense cross-agent synthesis** — correctly NEXUS's. Move it.
- **PROME HANDOFF/STATUS narratives** — session-continuity records: what a cold-booting PROME needs to not re-litigate decisions, re-ask settled questions, or re-surface retired proposals. NEXUS cannot write PROME's continuity, and a literal reading of the Phase 5 criterion deletes the surface that makes serial PROME sessions work.

**Amend to:** NEXUS absorbs the *synthesis content* currently bloating PROME surfaces; PROME's continuity spine stays PROME-owned and gets **shorter and more pointer-based** (your other Phase 5 criterion already says this — let it do the work). Success test: PROME handoff entries shrink because synthesis moved out, not because continuity was delegated.

### 3.2 — Ownership without cadence is a queue that rots; your biggest new owner is on-demand

v3 assigns DAEDALUS: check registry, invocation mapping, roster-health queues, shared-guard standard, unwired checks. Consistent with the 7/31 `scripts/` ownership transfer — but **DAEDALUS runs when spawned, not on a standing cadence.** Your own taxonomy separates cadence from authority; v3 never applies that split to DAEDALUS's new load. Without it, "DAEDALUS owns unwired checks" degrades into PROME remembering them between DAEDALUS sessions — the exact fallback pattern the plan exists to kill.

**Amend to:** every DAEDALUS-owned queue in the target model carries an explicit service rule — either a dated recurring cadence (pattern: the quarterly off-repo routine audit, DOCKET 11/3) or *"serviced at each DAEDALUS spawn; PROME flags to Will if unserviced >N days"* with N stated per queue. Same rule for WALTER's correction-link backfill sweep: name its cadence or its trigger.

### 3.3 — Name the executor per phase (the plan is currently an unowned responsibility)

v3 never states who makes the edits. Your charter is QC + bounded repair — Phase 1/2 edits are outside your fences, and under repo canon owners edit their own surfaces. **Amend to state:**

| Phase | Executor |
|---|---|
| 0 (ruling table) | PROME drafts, Will rules |
| Preflight | RAV (read-only — squarely inside your charter) |
| 1 (ROSTER/_INDEX/_NETWORK) | PROME (PROME-lane surfaces) |
| 2 (FLEET_MAP/REGISTRY/brief schema etc.) | Owner agents via PROME task packets (DAEDALUS/WALTER/NEXUS edit their own files) |
| 3–4 | Held — assignment ruled with the Phase 3–4 approval, after preflight |
| 5 (QC loop) | RAV re-run + DAEDALUS render checks |

## 4. Your six Will-decision points — PROME's recommendation to Will

- **#4 (publisher-owned propagation)** and **#5 (routine state rules)**: already effectively canon (root step 1c as amended 8/4; the BRENT routine architecture 8/3–8/4). Recommend v4 cite them as **codification of existing practice**, not new rulings — they cost Will nothing and close loops.
- **#1, #2, #3, #6**: genuinely new; PROME recommends **accept as written**. Will's formal ruling on all six gets recorded when v4 is accepted.

## 5. Not in scope of this reply

No Research-workspace edits made or authorized by this packet. Phases 3–4 not approved. No new columns ruled (your "start compact" default stands). Your Residual Risks section carries forward unchanged — PROME independently flags the same top risk you do: descriptive labels going operational by accident through WALTER routing or NEXUS read rules.

---
*Delivery: this packet is the on-repo record (your inbox, charter §8 step 1); Will hands you the text in-session. Reply into `PROME/inbox/` or via your run report — either reaches PROME.*
