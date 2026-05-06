# RED Session 011 Handoff

**Date:** 2026-05-06 (Wed)
**Session length:** ~30-45 min focused
**Outcome:** Will-corrected mechanical recommendation → rule-form Exit-Window Framework + 6-file institutional propagation + clean push

---

## What landed

### Will-correction this session

RED came in at boot recommending "close near-dated theta-killers before May 15" (mechanical, in OUTBOX from Session 8 carryover). Will pushed back:

> *"I dont want to sell the puts into all time market highs though. I think I need to find a better opportunity between now and expiration to sell."*

Will's point was correct: SPY ATH ($723.77) + VIX 16.54 (vol floor) = worst-mark exit. Mechanical close-now crystallizes the worst execution. But "wait for better" without rules drifts to expiry-by-default at the same bad mark.

### Conversion executed

Mechanical "close now" → 3-piece rule-form discipline:

1. **5-trigger window menu** — VIX intraday >20 / SPY single-session ≤−2% / HY OAS >310 sustained 3d / catalyst hot-print (CPI 5/13, BOJ surprise, WAL MI3 ≥25%, OZK NCO accel) / hard backstop date
2. **Per-position backstops** — May 8 (OZK Thread 3 roll) / May 12 T-3 (May expiries: OZK $42.5/$47.5, SOFI, KRE) / Jun 11 T-7 (IWM Jun, HYG Jun)
3. **Loop closure in workbook** owed regardless of exit mark — even if answer is "we waited and ate it." Discipline preserved by framework, not by execution timing.

### Reflexivity flagged

Same divergence validating RED's "paper vs structural" framing (SIG-W-20260506-002 tape-vs-substance bifurcation #2 — 2-of-2 sessions of substance HARD vs tape SOFT) IS the divergence killing near-dated puts. RED carried this tension 18 days without forcing a decision. Backstops force the decision. Bull steelman is *strengthening* over time, not just holding.

---

## Files changed (6 across 2 chunks per multi-file discipline)

### Chunk 1 — operational framework
| File | Change |
|------|--------|
| `STATUS.md` | Header refreshed (Session 11) + new EXIT-WINDOW FRAMEWORK section (lines 104-138) + OPEN CHALLENGES Q2-mismatch row updated. 176 → 211 lines (11 over 200 guideline; acceptable for Will-approved framework). |
| `CALENDAR.md` | New POSITION EXIT-WINDOW BACKSTOPS section between IMMEDIATE and NEAR-TERM. 100 → 112 lines. |
| `workbook/ML.tsv` | ML-RED-058 METHODOLOGY row appended. |

### Chunk 2 — institutional memory
| File | Change |
|------|--------|
| `AGENTS/RED/MEMORY.md` | "Wait-for-better is a rule, not a hope" methodology bullet added. |
| `~/.claude/.../memory/feedback_exit_recommendations_need_mark_context.md` | New global feedback file (frontmatter + Why + How to apply) — transferable across agents. |
| `~/.claude/.../memory/MEMORY.md` | Index pointer added (line 33). |

---

## Boot-step 1.5 BOARD scan executed

5 new SIG-W dispatches today (4 RED-cc'd, 1 ROUTINE skipped per b1):

| Signal | Tier | RED Read |
|--------|------|----------|
| SIG-W-20260506-002 tape-vs-substance bifurcation #2 | b3 cluster_mediating | RED-validating: WALTER explicit *"RED 'risk-premium-already-priced' steelman = now tape-confirmed across 2 consecutive sessions"* |
| SIG-W-20260506-001 OPEC 36yr low | b3 cluster_mediating | More substance for energy-bear; composition-artifact warning re May print (UAE exit 5/1) |
| SIG-W-20260506-004 Arbor Fed UST 65.9% | b3 cluster_mediating | Don't propagate "Fed propping up" unmodified; needs SOMA composition split |
| SIG-W-20260506-003 Gromen gold | b4 CORRECTED-FRAMING | Direction confirmed, ratios overstated; needs IMPORTS leg |

`FALSIFICATION_FIRED_LOG.tsv` = header-only (0 fires). Near-watch:
- **RED-FT-06 VIX <16 ×5d:** VIX 17.02, 6.4% from trigger (just outside 5% near-trigger band)
- **RED-FT-01 HY-OAS <280 ×3d:** WALTER tape-inference suggests near or just below 280; **primary OAS pull owed from LIQUID** for sustain-day-1 declaration

---

## Thesis state (UNCHANGED this session)

- **Confidence: 73%** (Session 10 floor)
- **Hypothesis weights: 36/35/14/9/4/2** (Stagflation / Managed / Rescue / Acute / War / Soft)
- **Net bear: 49% / Net managed-rescue: 49% / Soft 2%**
- **Positions:** all unchanged from Session 10

This was operational discipline, not thesis update.

---

## Carryover open Will-decisions (still queued)

| Item | Source | Status |
|------|--------|--------|
| HYG closure (RED-TO-PROME-20260506-001) | Apr 10 falsifier fired, 26d sustain | Mark-context override accepted Session 11; Jun 11 backstop. **Loop closure in workbook still owed** regardless of exit mark. |
| WAL $65P Jun position (RED-TO-PROME-20260506-003) | CHG-RED-025 M4-incoherence | NORMAL precedence; HOLD-or-roll-to-Sep counter-recommendation; awaits Will or REGINALD response |
| CHG-RED-024 BRENT v2.0 | Issued Session 9 | Awaits BRENT response |
| CHG-RED-025 WAL V2.0 OVER-CORRECTED | Issued Session 10 | Awaits REGINALD response (Will-authorized inbox direct-write executed) |
| OZK $42.5P May Thread 3 roll | Pre-built spec | **Hard deadline T-2 (~May 8)** — pricing check + execute |

---

## Top adversarial priorities for next session

1. **WAL V2.0 stress-test follow-ups (CHG-RED-025)** — pre-catalyst frameworks: (a) MI3 4-bin decision tree, (b) 10-Q Table 16 LAM/Leucadia inventory test, (c) Investor Day May 12 mgmt-credibility framework
2. **Q1 Call Report May 4-10** — WAL MI3 line is RED-primary-tracked; pre-write decision tree
3. **Brent path watch** — $103 falling. If >$130 sustain → add. If <$95 sustain → bull-thesis steelman strengthens further
4. **VIX/HY OAS daily check** — RED-FT-06 within 6.4%, RED-FT-01 inference suggests sub-280; primary pull owed
5. **OZK adversarial overlay post-Q1** — past-due doubled but tape muted; bull steelman owed (carryover from Session 8/10)

---

## Git state at closeout

| Item | Value |
|------|-------|
| **Push** | ✅ Clean — `f1b1adff..60b11ee6` |
| **Working tree** | Clean (verified) |
| **Local/origin sync** | In sync at `60b11ee6` |
| **Other agents** | WALTER pushed twice during session (`866d761e` + `f1b1adff`) — uncommitted state at boot fully resolved |

---

## Methodology notes worth carrying forward

- **Wait-for-better is a rule, not a hope.** Mechanical close-now at unfavorable execution mark is wrong; "wait and hope" without rules is also wrong; rule-form middle ground (window-trigger menu + hard backstop + workbook loop closure) is the discipline.
- **Reflexivity check on RED's own framing.** Same divergence validating RED's framing kills RED's instruments. Owe a self-falsifier on the framing itself, not just on bear-thesis vectors. Sketched 4 candidates (Q2 clean beat, HY OAS sustained <280 60d+, structural data backs OFF, Brent <$95 + Hormuz <5 mbpd ×15d). 2-of-4 fire = capitulate framing. Not yet pre-registered as STATUS.md falsification trigger — candidate for Session 12.
- **Multi-file chunk discipline held.** 6 files split as 3+3 with checkpoint, per `feedback_break_multifile_updates.md`. Avoided batch-of-6 pattern.

---

## Mode at closeout

Standby / closeout. No active task at session end. Next session boots normally; backstops auto-surface from CALENDAR.md.

---

*RED: Will's correction this session is the canonical case for "rule-discipline + execution-mark = framework, not mechanical-close." Methodology now propagated to global memory; transferable to all agents recommending position cleanup.*
