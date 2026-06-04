# SAM Eval — v1.5.1 Re-Baseline Operator Packet

**Target run date:** 2026-06-07/08 (weekend, before Jun 9 SAM-21 mechanical trigger re-check)
**Drafted:** 2026-06-04 (pre-trigger scoping; SAM session)
**Operator:** Will (eval runs are by-design Will-driven, per `README.md` § Runner protocol)

---

## Why now

- v1.1 baseline established 2026-05-27 (both cases PASS clean, against v1.4 thesis surface). Substantive prose surface changes since:
  - **v1.4 → v1.5** (2026-05-27) — Channel 1 demoted to deferred structural backstop after Big 3 mutual ESR window 3-of-3 benign.
  - **v1.5 → v1.5.1** (2026-06-03/04) — narrative reconciliation: new STRUCTURAL PILLARS section in THESIS, Channel 2 prose reconciled with CH-004 METHOD (Aug-2024-speed → upside tail; intervention paradox softened), conviction decomposed into direction-HIGH vs near-term-timing-MEDIUM.
- **Compounded auto-memory drift:** at least 14 new auto-memory entries since last re-baseline (rough count from MEMORY.md delta). The lesson surface has materially grown — runner now has CH-004 METHOD, structural pillars framing, thin-liquidity prediction-market discipline, escalation-mode discriminator, etc.
- **Per the updated README cadence rule** (this commit): Z-level patch with substantive prose surface restructure ⇒ re-baseline required. ≥10 new auto-memory entries since last re-baseline (heuristic threshold) ⇒ also fires.

## What's expected to be different

This is the **diagnostic frame**, not a target — score against the existing RUBRIC criteria as-is.

- **Case 01 (Nippon ESR / threshold-vs-mechanism):** Lesson surface has *strengthened* since 2026-05-27 — `[[finding_threshold_vs_mechanism]]` has been validated 3-of-3 (SAM-25 Nippon May 26 + Meiji May 26 + Sumitomo May 26) and is cited as a calibration anchor in the PREDICTIONS scoreboard. Expectation: easier PASS, possibly more elaborated mechanism articulation.
- **Case 02 (JGB 30Y / J-ICS causal direction):** Lesson surface largely unchanged — the "lifer-absence → yield-blowout" inversion was already canonical in v1.4 and remains canonical in v1.5.1. Expectation: PASS, similar to v1.1 baseline.
- **Watch-for: fiscal-dominance reasoning in Case 02.** The 2026-05-27 v1.1 runner argued June BOJ hike was LESS likely on fiscal-dominance logic — surfaced as a "substantive thesis input" candidate in results.tsv notes. Since then, the market has repriced the June hike UP (Polymarket 88% → 94.8%), going the OPPOSITE direction. **A fresh runner may or may not still produce the fiscal-dominance argument** — note in scoring whether it appears, what framing it takes, whether it acknowledges the May 31 repricing. This is diagnostic for the OS.1 thesis question being addressed pre-Jun-9 in a separate SAM-driven pass (see MEMORY NEXT SESSION).

## Pointer refresh logged

- **Case 02 RUBRIC L10** — citation pointer refreshed (2026-06-04): "(NEW v1.4 — May 21)" → "(kept live in v1.5 / v1.5.1; DOMESTIC mechanism…)". **No criterion change.** Scorer should confirm case behaves identically — if Case 02 result diverges materially from v1.1 baseline, it's an actual reasoning shift, NOT a rubric drift artifact.

## What's NOT changing

- **Case INPUTs** — both remain frozen at their historical dates (Case 01 = 2026-05-26 pre-print state; Case 02 = 2026-05-15 mid-session state). **Do NOT modify the INPUTs to reflect current state** — the cases test reasoning against known historical context.
- **Case RUBRIC criteria** — all EXPECTED + DO-NOT checkboxes unchanged. Only the lesson-source pointer in Case 02 L10 was touched.
- **Runner protocol** — same as v1.1 README. Fresh session, skip-boot, paste only the triple-backtick block, score against RUBRIC in a separate window.

---

## Operator steps (compressed — full protocol in `README.md`)

1. **Open a fresh Claude Code session** in `/home/willi/Research-workspace/AGENTS/SAM/`. New terminal, new conversation, no shared context with any running SAM.
2. **Case 01 first:**
   - Open `case_01_nippon_esr_INPUT.md`, copy ONLY the triple-backtick block.
   - Paste as the first prompt. Hit enter. Add no framing.
   - When the runner responds, open `case_01_nippon_esr_RUBRIC.md` in a separate window. Score against EXPECTED + DO-NOT.
   - Run the post-response contamination check.
   - Capture the response verbatim into `baseline_artifacts/2026-06-XX_v1.5.1_responses.md` (Case 01 section).
3. **Case 02 second** (separate fresh session — do NOT reuse Case 01's session):
   - Same protocol. Capture into the same artifacts file (Case 02 section).
4. **Append two rows to `results.tsv`** — one per case. Format:
   ```
   DATE \t case_01 \t YYYY-MM-DD-HHMM-v1.5.1 \t RESULT \t auto_memory_loaded_notes \t scoring_notes
   DATE \t case_02 \t YYYY-MM-DD-HHMM-v1.5.1 \t RESULT \t auto_memory_loaded_notes \t scoring_notes
   ```
5. **Update `evals/README.md` "Last baseline run"** line + the L125 "Next re-baseline scheduled" line to reflect the new completed run.
6. **Close both eval sessions** — context is contaminated with inputs, don't reuse for real work.

## Diagnostic notes to capture

Per the v1.1 baseline pattern, capture in `baseline_artifacts/2026-06-XX_v1.5.1_responses.md`:

- Which auto-memory entries appeared in the runner's context (visible at session start)
- Whether the runner cited `[[finding_threshold_vs_mechanism]]` or `[[finding_catalyst_vs_consequence_conflation]]` or other relevant lesson hooks — and whether the citation was substantive or surface-level
- Whether Case 02 runner produced a fiscal-dominance argument; if so, what framing (LESS likely / MORE likely / decoupled-from-spot-hike?)
- Any new substantive content beyond the RUBRIC criteria (the v1.1 baseline produced multiple "substantive finding worth surfacing" items — note any equivalents)
- Contamination signatures observed (verbatim phrase echo from RUBRIC, J-ICS cited without articulation, EXPECTED-mirrored bullet structure)

## Failure protocol

Per `README.md` § Failure protocol — same as v1.1 run. Four diagnostic buckets (lesson absent / lesson present but not applied / case bug / contamination). Don't revert the v1.5.1 thesis edits blindly on a fail — diagnose first.

---

## Out-of-scope handoff

- **OS.1 (fiscal-dominance / BOJ-frozen counter-frame)** — this is a thesis-side question, NOT an eval-suite cleanup. Scoped as a separate pre-Jun-9 SAM-driven task in MEMORY NEXT SESSION. The re-baseline run's diagnostic value to OS.1 is "did a fresh runner reproduce the fiscal-dominance argument?" — capture it as a data point, don't try to resolve OS.1 during the eval run.
- **OS.2 (Case 03 candidate)** — held per README discipline; revisit only if (a) one of existing 2 fails or (b) the catalyst-vs-consequence pattern recurs in real-time SAM work.

---

*Drafted by SAM on 2026-06-04 as part of Phase A of the Open Flags rail (Eval re-baseline scoping). Operator packet for future fresh-session run; SAM did NOT run the cases in the drafting session.*
