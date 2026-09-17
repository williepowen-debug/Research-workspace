# DEWEY drafts review + architecture read — 2026-07-10 (Will-directed)

> **✅ DISPOSITION — CLOSED SAME-DAY 2026-07-10 (verified against origin, commit `a89d8f3b`).** All approved items LANDED: drafts 1–5 committed; N1 (TOOLS lede + RULES #4 harmonized to two-engine frame) + N2 (build-pass trigger homed in CLOSEOUT step 11, ≥3-past-gate → surface to Will) both applied verbatim-correct; hook (a) adopted (step-8 `impact:` backfill, honestly ceiling-noted); proposal (b) drafted to `AGENTS/DEWEY/outbox/2026-07-10_to-PROME_impact-capture-walter-ledger.md` in exactly the reshaped framing (WALTER-ledger `impact` column on `DEEP_RESEARCH_FLAGGED_LOG`, PROME-routed, WALTER owns the call, explicitly NOT a fleet readback loop). Open on others: helper builds (jgb_mof/disaster_shocks/ffiec_callreport) = Will-greenlit BACKLOG candidates, correctly NOT built; proposal (b) awaits PROME/WALTER. Nothing pending on DEWEY or DAEDALUS for this review. *(Verification note: DEWEY's verbal report attributed drafts 1–5 to `204b5780` — actually all in `a89d8f3b`; cosmetic misattribution, content verified present.)*

**Reviewer:** DAEDALUS · **Target state:** DEWEY LIVE (uncommitted drafts appeared mid-session — files are his; all feedback routes via Will/inbox, zero DAEDALUS edits)
**Scope:** (1) the 5 uncommitted drafted changes (CLAUDE.md ×4, BACKLOG.md ×1); (2) the decision-impact loop proposal (options a/b); (3) overall file-architecture read.
**Diff reviewed:** working tree vs HEAD `204b5780` — `AGENTS/DEWEY/CLAUDE.md` (+14/−4), `AGENTS/DEWEY/scripts/BACKLOG.md` (+2).

---

## 1. Verdict on drafts 1–5: APPROVE ALL, as written. Two non-blocking harmonization notes.

| # | Draft | Verdict | Notes |
|---|---|---|---|
| 1+2 | ENGINE reframe → "two engines, sized per prompt" + Engine-sizing heuristic | ✅ APPROVE | Converts a permissive aside into a decision rule with calibration anchors (prompt 08 = harness-oversized; 13/11 = harness-warranted). Correctly homed in the durable spec surface (PAT-041 clean). Honest about what the fan-out is actually good at (breadth/history/verify, not synthesis) — matches the evidence in 8 delivered runs. |
| 3 | RUN PROTOCOL step-3 return-partial guardrail | ✅ APPROVE | Direct encoding of the prompt-13 failure (un-guarded 5-bank pull died mid-run returning NOTHING; guarded re-spawn completed all 5). Evidence-anchored, right home. |
| 4 | Step-6 rate-limit recovery recipe | ✅ APPROVE | salvage → resume-from-cache (re-pass `args`) → re-spawn dead plain-Agent legs. Matches banked auto-memory `finding_workflow_rate_limit_resume_recovery`; links it. |
| 5 | BACKLOG BUILD GATE lowered (2+ hits → BUILD; periodic top-3 pass) | ✅ APPROVE | Right economics ("un-built helper = per-run tax"), evidenced by edgar_doc.py's payback. Trigger note below. |

**Non-blocking harmonization (same-commit polish, DEWEY's call — [[finding_doc_mirror_consistency_check]]):**
- **N1.** TOOLS section lede still reads "**Engine:** the `/deep-research` skill (**primary**, for depth)" and RULES #4 still reads "**The skill is the engine**" — both now mildly contradict the new "two engines, fan-out opt-in" frame. Intent survives (don't reimplement fan-out), but a future session reading TOOLS/RULES first inherits the old default. One-line touch-ups.
- **N2.** BUILD GATE's "**periodically** run a build-the-top-3 pass" has no owner/clock ("periodically" is unowned — the PAT-041 class, mild form). Cheap fix, no new machinery: extend CLOSEOUT step 11 (promotion scan — which already touches BACKLOG.md every run) with "if ≥3 candidates sit past the gate, surface a build-pass suggestion to Will in the debrief." Builds stay Will-greenlit (trace_bond precedent); this just guarantees the suggestion fires.

**Commit mechanics:** DEWEY commits his own drafts (own-dir pathspec). No DAEDALUS action.

## 2. Decision-impact loop: ADOPT (a) now; RESHAPE (b) — don't build a readback protocol.

- **(a) DEWEY-side INDEX `impact:` annotation — ENDORSE, adopt now.** Own-file, additive (notes column), opportunistic-and-honest. PAT-028-clean: qualitative proof counts; consumption DEWEY never learns about stays a ceiling note, not debt.
- **(b) Fleet readback loop (consuming agents tag "moved decision X / no-op") — DO NOT build as drafted.** Three grounds:
  1. **Out-of-scope class:** root CLAUDE.md §Data Hygiene rules new cross-agent send protocols out of scope — messaging redesign routes to the messaging-overhaul effort ([[project_messaging_overhaul]]). A fleet-wide readback-tagging convention is exactly that class.
  2. **The infrastructure half-exists, WALTER-side:** DEWEY's output already flows through one chokepoint (WALTER, single entry point), which already instruments delivery/consumption (delivery_log 515 rows, walter_doctor `delivered_but_unconsumed`, board_log at 9 agents) and already owns a per-flag lifecycle ledger DEWEY feeds (`DEEP_RESEARCH_FLAGGED_LOG`, flag-close in DEWEY closeout step 10). **The architecturally-correct small version: an `impact`/`disposition` column on DEEP_RESEARCH_FLAGGED_LOG** — one owner (WALTER), one surface, no new protocol, and WALTER reads the consuming agents' surfaces routinely anyway.
  3. **PAT-028 false-negative:** a mandatory consumer-side tag-back under-counts by construction (decisions move without ledger rows — a REGINALD proposal absorbing a DEWEY number won't reliably tag). The gate would nag agents and still read "unconsumed" for genuinely-consumed work.
- **Routing:** DEWEY drafts the PROME proposal (his suggestion, his outbox) but framed as the **WALTER-ledger extension**, not the fleet readback loop. Recommendation relayed via Will to the live session.
- **Evidence consumption ALREADY happens** (for the record): 3 of the 7/9 reports became BOARD SIGs same-day (SIG-W-20260709-001/002/003); prompt-11's urea correction landed in CARL (`f1f53939` "DEWEY urea/CRL-10 integration landed" per PROME SCRATCH); prompt-08 re-characterized SAM's CH-010 trigger; prompt-13 un-blinds REGINALD's V1 falsifier. The gap (b) targets is *systematic capture*, not absence of consumption.

## 3. Architecture read (for FLEET_MAP re-grade)

**DEWEY is the fleet's cleanest utility agent and its L0 row was badly stale.** Two-level identity (deep research + data-pull script home, Will-ratified 6/20) has held without drift. File set is minimal-by-design and each surface earns its place: CLAUDE.md (spec, actively maintained — 3 substantive self-encodings in 48h), CONTEXT.md (staleness-bannered, flags-not-rewrites), scripts/ (5 helpers + recurrence-gated BACKLOG), output/ + INDEX.tsv (17 reports; **the deliberately-only state file, with an explicit anti-default against STATUS/SCRATCH/predictions machinery** — anti-DARWIN PAT-001 applied at file-architecture level, in writing). The self-improvement loop is **fleet-reference**: Process Report (mandatory per report) → promotion scan (closeout 11) → BACKLOG/auto-memory → debrief to PROME → Will disposition → **same-week encoding back into CLAUDE.md** (the 7/9 8-item debrief was dispositioned AND implemented within 24h; today's drafts are the loop running again).

**Grade: Utility L4, Conf M** (was L0/"stateless by design" — a design-intent note that rotted into a wrong grade as DEWEY accrued a spec, ledger, tooling layer, and consumed output). L2 ✓ INDEX.tsv accruing (17 rows). L3 ✓ role rubric (citation/source-tag/counter-evidence/process-report) applied consistently across the corpus. L4 ✓ output consumed (BOARD SIGs + REGINALD/SAM/CARL integrations above). Conf M not H: core-spec surfaces read today; report corpus + scripts internals not fan-out read — full profile pending.

**L5-path gaps (all small):** N1/N2 above · no labeled CONTRACT block (utility blueprint §2 — PAT-033 predates-the-blueprint class; substance scattered in IDENTITY/CLOSEOUT) · (a)-hook once adopted.

**Follow-ups (DAEDALUS lane):** profiles/DEWEY.md + DEWEY_CARD.md (Mode-A read, next queue slot) · FLEET_MAP row re-scored today · PAT-045 banked (stateless-agent learning-loop pattern).

---
*Review file is the deliverable; DEWEY LIVE → no cross-agent edits made. Disposition write-back → Will (in-session).*
