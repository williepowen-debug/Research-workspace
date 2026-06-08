# REGINALD SCRATCH

*Loose notes, intra-day workspace, observations that don't fit anywhere else yet.*

**Purpose:** Capture stuff during the work — half-thoughts, things noticed in passing, quotes worth remembering, format gotchas, draft language.

**What this is NOT:**
- Not a task list (use MEMORY NEXT SESSION)
- Not curated memory (use MEMORY)
- Not a thesis (use THESIS / sub-bank THESIS files)
- Not a research backlog (use ROADMAP — Investigations Backlog section)
- Not a session-bridge (MEMORY Session Notes does that)

**Maintenance discipline:**
- Date each entry / section
- Promote to KB / ROADMAP / STATUS / MEMORY when it grows up; delete when it's done
- Prune aggressively — if a note is older than ~2 weeks and hasn't earned a promotion, delete it

---

## 2026-06-02 — Boot + file-tree catch-up [pruned 4 stale sections >2wk: 5/1, 5/8, 5/10-11, 5/11; collapsed 5/15-17 to open items]

**Things noticed during the catch-up (factual hygiene session — no analysis pursued):**
- CALENDAR + STATUS PREDICTIONS sections were both stale at REG-24 60% / REG-25 55% — never synced to the 5/21 v2.2 ratchet (canonical PREDICTIONS.tsv was already 70%/75%). Synced both. Lesson echo: a thesis-version bump touches more files than the headline four; sweep PREDICTIONS *consumers* (STATUS, CALENDAR) not just the canonical tsv.
- Credit bifurcation is the one signal that didn't fade with the risk-on tape: CCC OAS 946 [6/1] vs HY 272, ratio 3.22x→3.48x. Recorded in STATUS macro-read; Will reviewed and chose to keep in STATUS (no separate tripwire / ROADMAP item this session). If it keeps widening, candidate for a CCC/ratio early-warning trigger to supplement the lagging HY>320 tripwire.

**Carried-forward open research threads (orphaned from pruned sections — promote to ROADMAP investigations on next research pass):**
- **"Juris banking"** (from WAL Q1 transcript, 5/1) — named multiple times as the "real surprise driver." Still no KB row capturing what it actually IS (business / counterparty / monetization). Research add.
- **Investor Day Slide 113 stress test** (from 5/15-17) — 5.3% total loan loss rate under 2026 severely-adverse, CET1 stressed to 9.0% — *exceeds* v2.2 Bear-fast assumptions. Mgmt pre-positioning "we can absorb worse than bears model." Open SCENARIOS.md cross-check (analysis pass, not this session).
- **Investor Day Slide 89 NDFI peer chart** (from 5/15-17) — "13% 12% 12% 11%" chart text vs 10-Q's 25.2%-of-HFI / 7.9% Business+PE. Likely different denominator. PDF deck would resolve. Low priority.

---

## 2026-06-08 — BOARD backlog drain + v2.2.1 ship + Orchestrator audit + closeout hardening

**Things noticed during the session:**
- WAL 10-Q drill recipe (curl + XBRL strip) preserved as one-liner — moved to MEMORY Findings rather than SCRATCH on this closeout (durable enough to deserve persistent home).
- Convergence Matrix WAL row in STATUS was caught by the drift-grep step IMMEDIATELY after I added the rule — pinned to v2.2's EV $67.98 / "Bear-medium speed" language while THESIS + SCENARIOS were on v2.2.1. **Dogfooded the rule on its first run** — concrete win for the new control.
- Director/Orchestrator audit caught 4 distinct error-classes in one session (denominator drift, secondary-source-precision, cohort-decomp half-done, over-meta-process-design). The "who reads it?" test is a transferable inversion of the build-it-first intuition. Promoted to MEMORY Feedback.

**Open threads carried (still ROADMAP-tracked):**
- Juris banking research (from 5/1 transcript).
- Investor Day Slide 113 stress test (5.3% loss / 9.0% CET1 stressed exceeds v2.2 Bear-fast).
- Investor Day Slide 89 NDFI peer chart (deck PDF needed).
- WAL Investor Day Q&A transcript hunt (downgraded priority post-v2.2.1; B1 already fired).
- Cross-bank life-science pattern (WAL $99M + OZK IQHQ; KREF distinct mechanism; watching for #3 with pass-grade-bank-walk mechanic specifically).
- Cohort NCO decomposition for ZION/CFG/MTB/FITB (v2.2.1 cohort framing held open pending; Hypothesis B could reverse the 30→25 Bear-medium trim).

---

## TEMPLATE FOR FUTURE DAYS

```
## YYYY-MM-DD <morning/PM> — <one-line context>

**<Section header>:**
- bullet
- bullet

**Things I noticed but didn't dig into:**
- ...

**One-liners cached:**
```bash
# ...
```

**Convention question / open-thread for next session:**
- ...
```

---

*Companion: `ROADMAP.md` (persistent state across sessions) | `MEMORY.md` (curated cross-session memory) | `STATUS.md` (live dashboard)*
