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

## 2026-06-19 — Boot + 11-day-gap catch-up + BOARD CRE-credit mini-cluster [pruned stale 6/02 section >2wk; its threads live in ROADMAP]

**Noticed during the catch-up:**
- The CCC/HY "narrowing" framing I shipped 6/8 (3.48→3.44x) has **re-widened to 3.57x** on the 6/17 FRED refresh — HY tightened to 263bps faster than CCC came in. The bifurcation read keeps oscillating on the 2-day window; the durable statement is "tail lags the index rally," not a clean trend either way. If I keep re-litigating this every boot, it's a candidate for a CCC/HY-ratio tripwire (e.g. >3.6x sustain) so it stops being a prose judgment call. Flagged, not built.
- **IORB sanity-check caught a framing trap:** WALTER's BOARD signals repeatedly say "Fed flipped cut→HIKE 6/17." IORB is flat at 3.65 → no actual hike happened. It was a hawkish *guidance/dots* flip. Transcribing the signal's shorthand as "hike" would have been wrong. (Echoes [[finding_circular_corroboration_via_state_file]] / verify-from-raw-series.)
- **HY OAS 263 is 3bps from my own Exit-100% rule (<260).** Risk-on tape is quietly walking me toward my own exit trigger from the credit side while the CRE-fundamental side deteriorates. The bear can be "right on fundamentals, stopped out on credit spreads" — hold both in view.
- The Trepp CRE-DQ-by-tier signal (009) *looks* like it contradicts my 6/8 cohort finding but is a different metric (DQ vs NCO). Logged the distinction explicitly in STATUS + BOARD_LOG so a future read doesn't false-flag a contradiction.

**Threads carried (all in ROADMAP):** CRE-DQ-by-tier drill (new, OZK-cleanest), capital-rules final-rule watch (new), WAL $85P disposition flag (new) + prior: Juris banking, Slide 113 stress test, Slide 89 NDFI chart, Q&A transcript, life-sci #3, MI3/FFIEC, APO Q1, OZK 10-Q.

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
