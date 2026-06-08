# BRENT SCRATCH — Sun Jun 7, 2026 (night — OPEC integration + NEXUS_Brief build session)

**Purpose:** Ephemeral session handoff — the canonical "where are we / what next" file. Read at boot (SPAWN PROTOCOL step 2), rewritten in full at closeout (step 11). Disposable; rewritten every session. Persistent learnings live in `MEMORY.md`; dated forward catalysts live in `docket/CATALYSTS.tsv` (FASTOW); cross-agent synthesis lives in `NEXUS_BRIEF.md` (now the primary cross-agent channel).

---

## CHANGES SINCE LAST SESSION (Jun 7 5:38 PM → Jun 7 night)

- **OPEC+ Jun 7 Vienna FIRED & integrated.** 7-member group **+188K bpd for July** (4th straight hike, gradual unwind continues = base case); full OPEC+ no change to group policy through end-2026; **UAE orphan-baseline NOT reallocated — deferred to 2027 capacity review** (defense posture). 188K is paper + small + trapped behind Hormuz (LESSONS #10) → optically mildly bearish, functionally neutral. No matrix/thesis/position change. [CONF CNBC/AA/TradeArabia Jun 7]
- Otherwise no new market data (weekend; Globex Sun 6 PM ET, first real read Mon AM).

## NEW THIS SESSION

- **OPEC integration** → CATALYSTS Jun 7 row → FIRED; STATUS header/LIVE-TODOs/matrix/open-items/calendar all updated; SCRATCH. Commit `7c178f1c`.
- **STEO drift fix** — caught 4 stale STATUS refs putting STEO at Jun 11; corrected to **Tue Jun 9** (canonical CATALYSTS + boot.py confirm; OPEC MOMR is the Jun 11 event). Same commit.
- **🆕 NEXUS_BRIEF.md built** (`AGENTS/BRENT/NEXUS_BRIEF.md`, 81 lines, under 100 cap) — pilot-2, heavy-cross-domain. Commit `b41ab19a`.
- **CLAUDE.md** — wired brief write-back as CLOSEOUT **step 12** (twin of SCRATCH; renumbered promotion→13, git→14); encoded Will's decision that **NEXUS_BRIEF CROSS-DOMAIN tables = BRENT's PRIMARY cross-agent channel** (outbox now 🔴 acute-only). Commits `b41ab19a` + `6bce5a58`.
- **Pilot-2 consumer review** (spawned NEXUS-proxy) → `inbox/2026-06-07_from-NEXUS_brief_pilot2_review.md`. Verdict: **RATIFY at heavy end**; load-bearing PARTIAL→clean-YES after fixing one defect (missing REGINALD SENDING edge). Applied 4 edits. Commit `6bce5a58`.
- **Fallback-rate instrumentation** — spec authored (`outbox/2026-06-07_to-NEXUS_fallback_rate_instrumentation.md`, commit `b9764789`) then **APPLIED LIVE to NEXUS via proxy** (commit `59bbc407`, within AGENTS/NEXUS/): new `brief_fallback_log.tsv` + BOOT-step-6 addendum + CLOSEOUT step 9a. Key design: classify fallbacks `stale`/`convergence`/`uncertainty`/**`brief-gap`** — only `brief-gap` rate is the quality signal (total fallback rate would mispenalize Type-B-rich agents like BRENT). Provenance noted for live-NEXUS to review on next boot.

## WHAT I DID THIS SESSION

- Boot per SPAWN PROTOCOL (git pull clean, STATUS/SCRATCH/LESSONS read, boot.py 10s, predictions scanned — none DUE).
- Pulled the OPEC+ Jun 7 outcome (it was PENDING at the 5:38 PM session, deferred to Mon — Will asked, so I pulled it tonight) + integrated.
- Scouted the NEXUS_Brief system (NEXUS schema R3+am7, SAM pilot + reviews, NEXUS boot integration), built BRENT's brief, ran proxy consumer-review, wired closeout, applied instrumentation live.
- Gave Will an honest systems-assessment of the brief concept (works in proportion to maintenance discipline + NEXUS cadence; failure modes = quality-decay-behind-freshness + single-point-of-failure on NEXUS).

## NEXT SESSION (dated, future-verifiable)

1. **Mon Jun 8 AM** — Brent **open reaction to OPEC+** (expect muted — base case, paper add) + **CF $130C mark** + first intraday move vs USO (chain-decoupling check; HOLD-confirmed Will Jun 1, revisit if continued decoupling). ~8 trading days to CF expiry.
2. **Tue Jun 9** — **EIA STEO (June)** — first post-suspension; Q2 Brent peak ($115 Apr) likely revised UP.
3. **Wed Jun 10** — **EIA WPSR (week Jun 5) = THE BIG PRINT.** SPR ~350M floor-touch (DIRECTIONAL — throttle bullish / drain-through near-term bearish + medium-term bullish, NOT symmetric). First clean post-MD demand read (BRT-08/09 candidate).
4. **Thu Jun 11** — OPEC MOMR (June), first post-Vienna.
5. **Fri Jun 12** — CFTC COT (Jun 2 wk, post-suspension) = real Trigger #3 re-fire test; Baker Hughes (431 last, +2 WoW, vs 457).
6. **Sun Jun 15** — BRT-27 walkback deadline (trending partial-confirm).
7. **Thu Jun 18** — CF $130C expiry.
8. **~Jul 1** — Cushing 20M floor (modeled); BRT-28 Bab al-Mandab window closes.
9. **Every closeout now** — refresh `NEXUS_BRIEF.md` (step 12). Keep SENDING/WAITING-FOR fresh — that IS BRENT's cross-agent comms now.

## NEXT SESSION (Tier 2 — carried forward)

10. **THESIS.md v3.1 bump candidate** — macro-transmission engagement Jun 5 is thesis-level; right time = after Jun 9 STEO + Jun 10 EIA are in.
11. **FASTOW Run 2** — cheap (~3-5 min; monthly trigger doesn't fire until Jul 1).
12. **Workbook KB/VX/FLOW** — dormant 6+ wks; revive-vs-demote decision still OPEN with Will.
13. **Crack-spread refresh** (last Mar 27 $42 3:2:1) — BRT-12 channel test setup.

## OPEN THREADS / WATCHES

- 🔴 **Macro transmission propagation** — watch whether HY OAS catches up to Fri's VIX +40% (LIQUID primary); whether the BRT-16 cascade is one root or independent moves (the Type-B candidate I handed NEXUS).
- 🔴 **SPR ~350M floor (Jun 10)** — directional, not symmetric.
- 🟠 **CF chain-decoupling** — Mon AM mark gates re-eval.
- 🟠 **BRT-15 re-arm** — fresh kinetic-with-facility-damage / US-Iran direct exchange / Hormuz vessel attack / barnacle re-surfacing.
- 🟠 **Trigger #1 (M1-M3 ≤$3)** — likely re-steepened FAR from threshold; ICE CONF pending.
- 🟡 **HY energy OAS catch-up**, crack refresh, dated-Brent-Platts (terminal-only).

### NEXUS_Brief thread — queued for LIVE NEXUS (its calls, not BRENT's)
- **Amendment-9 (CASCADE sub-block)** — real heavy-domain gap; structured home for multi-hop chains (ties to Discipline F). Raised in pilot-2 review + brief footer.
- **Amendment-10 (acute-vs-steady marker)** — soft; now that brief is primary channel.
- **Light-end pilot still un-run** — HAWK is the nominated single-channel candidate (Will refreshing HAWK tomorrow = natural moment).
- **Cap** — BRENT (81) is a co-anchor with SAM (75) for "heaviest real domain"; provisional 100 holds.
- **Fallback instrumentation now LIVE in NEXUS** — awaiting live-NEXUS review on its next boot (proxy-applied, provenance noted).

## POSITION DECISIONS PENDING

- **CF $130C Jun 18** — HOLD CONFIRMED (Will, Jun 1 PM). ~8 trading days. CAVEAT: chain-decoupling pattern. Revisit if Mon AM mark + first move vs USO shows continued decoupling.
- **XLE $65C Sep 30** — HOLD. XLE $57.67 Fri, strike $7.33 OTM. Kinetic-tail insurance NOT being paid on escalation-without-damage. 4mo runway is the asset.
- **Tanker BRT-15** — TABLED Jun 4 (Option B). War-risk leg fully unwound. Re-arm watch above.

## MAIL STATE (one line per signal)

- **Inbox:** 1 item — `2026-06-07_from-NEXUS_brief_pilot2_review.md` (the proxy consumer-review; integrated, edits applied; keep as pilot-2 reference, do NOT process-move yet — it's a live artifact).
- **Outbox:** 1 item — `2026-06-07_to-NEXUS_fallback_rate_instrumentation.md` (spec; already applied live to NEXUS, so this is now a record/reference — HERMES delivery moot).

## WORKBOOK HEALTH

- **`NEXUS_BRIEF.md`:** 🆕 LIVE, 81 lines, rev-2. Hash 7c178f1c = current STATUS HEAD (NEXUS mechanical stale-check won't false-fire). Refresh every closeout (step 12).
- **`thesis/PREDICTIONS.tsv`:** green; no DUE-stale rows. No changes this session (BRT-07/11 unaffected by OPEC base-case outcome).
- **`docket/CATALYSTS.tsv`:** green; Jun 7 OPEC row → FIRED. FASTOW-maintained.
- **`workbook/KB/VX/FLOW.tsv`:** DORMANT 6+ wks — Tier-2 revive/demote decision open.
- **`thesis/THESIS.md`:** v3.0; v3.1 bump candidate post Jun-9/Jun-10 catalysts.
- **`refinery_damage/INCIDENTS.tsv`:** 35 rows; green; no new facility-damage (kinetic all intercepts).

## GIT STATE

- **Commits this session (all within AGENTS/BRENT/ except the proxy's NEXUS commit):**
  - `7c178f1c` STATUS/CATALYSTS/SCRATCH — OPEC integration + STEO fix
  - `b41ab19a` NEXUS_BRIEF.md + CLAUDE.md closeout wiring
  - `6bce5a58` pilot-2 review + brief edits + channel decision
  - `b9764789` fallback instrumentation spec (outbox→NEXUS)
  - `59bbc407` **NEXUS** files (proxy-applied instrumentation; within AGENTS/NEXUS/)
  - + this closeout commit (SCRATCH + brief stamp)
- **VIOLET** has 2 uncommitted workbook files (VIX_OPTIONS.tsv, VX_DAILY.tsv) — left untouched per `[[feedback_agent_git_isolation]]`. They do NOT block a push (push only sends commits).
- **Push:** Will authorized "push if safe." Pushed this session IF remote not diverged (no pull needed). If remote diverged, deferred (can't safely pull --rebase with VIOLET's uncommitted files present per pull protocol).

## NEW AUTO-MEMORY THIS SESSION

- **Candidate (not yet written, flagged for Will):** *"Fallback/escalation instruments should measure the actionable category, not the gross rate — a Type-B-rich (highly-connected) node legitimately generates high healthy-drill-down volume, so total-rate mispenalizes the best nodes; isolate the one category that means 'this node is failing.'"* Transferable beyond NEXUS. Also a meta-lesson: a cross-agent synthesis schema must be stress-tested on BOTH heavy axes (single-deep-catalyst AND many-shallow-edges) — they surface different gaps (BRENT's cascade gap was invisible to SAM's pilot). Holding pending Will's call since it's NEXUS-system territory.
