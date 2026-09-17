# As-made confidence verification — ZHAO, 2026-09-17

**Origin:** DAEDALUS 9/7 packet (harvest H2, `scripts/asmade_audit.py ZHAO` → 17 rows · SAME 8 · MISMATCH 9). **Scope of this file:** the owner-verification leg only — each candidate checked at the blob DAEDALUS named with `git show <sha>:AGENTS/ZHAO/STATUS.md | grep <ID>`. **The ledger write (WQ-112 machine form `X% [date] (was Y% [date])`) and the re-score of the three RESOLVED rows are NOT done here** — this was an L0 drain-only session (PROME WQ-206 spawn). KB record: KB-ZHAO-147.

**Canon read before touching anything:** `FORGE/PREDICTION_DISCIPLINE.md` §Grading & re-marking, the four WQ-161/163 bullets (PROME 9/14 delivery). Dated re-marking on an unchanged question is preserved; no historical probability redistribution.

| Row | Ledger `Confidence` now | Ledger `Date_Made` | As-made VERIFIED at blob | Blob | Status | What the write must do |
|---|---|---|---|---|---|---|
| ZHA-01 | 18% | 2026-03-03 | **70%** (cell read `70% → **55%** ↓`) | `0d0ead00a` 2026-03-09 | OPEN | machine form; also reconcile the STATUS mirror (showed 15% on 9/2 vs ledger 18%) |
| ZHA-03 | 25% (at resolution) | 2026-03-06 | **65%** | `0d0ead00a` 2026-03-09 | RESOLVED NO 8/21 | **RE-SCORE** — scored as a well-calibrated miss at 25%; as-made was 65% |
| ZHA-04 | 42% (at resolution) | 2026-03-06 | **65%** | `0d0ead00a` 2026-03-09 | RESOLVED YES 8/21 | **RE-SCORE** — as-made 65% (the 65→30→42 walk is the re-mark history) |
| ZHA-06 | 72% | 2026-03-06 | **60%** | `0d0ead00a` 2026-03-09 | OPEN | machine form |
| ZHA-10 | 40% | 2026-03-09 | **45%** | `77f56870c` 2026-03-22 (the [PROPOSAL] block) | OPEN | machine form; Date_Made may need 03-22 |
| ZHA-11 | 68% ↑ | 2026-07-09 | **65%** | `c4c0bc33a` 2026-07-09 | OPEN (resolves on July TIC) | machine form: `68% [2026-08-21] (was 65% [2026-07-09])` — confirm the 68 date from history |
| ZHA-12 | 80% | 2026-07-16 | **55%** | `adeac0f72` 2026-07-16, line 181 | OPEN (resolves on July TIC) | machine form. ⚠️ **The tool printed 4% — a parse artifact**: it read the first percentage in the prose block above the table (limit 1 in DAEDALUS's own caveats) |
| ZHA-15 | 18% | 2026-07-16 | **55%** | `9283ddbe0` 2026-07-16 | RESOLVED NO 8/21 | **RE-SCORE** — Notes say "18% was assigned to the branch that did NOT occur"; as-made was 55% for the STIMULUS branch |
| ZHA-16 | 45% | 2026-09-02 | **35%**, amended to 45% the same session, still before the event | `d757fb63b` 2026-09-02 | OPEN | machine form: `45% [2026-09-02] (was 35% [2026-09-02])` — same-day amendment, both dated |

**Not a verdict on calibration.** Three resolved rows move in different directions (ZHA-03 and ZHA-15 were scored more cautiously than as-made; ZHA-04 was scored less confidently than as-made and resolved YES). The Brier effect is computed at the write, not here.

**Method note for the write:** walk by prediction TEXT where the ID post-dates registration (`git log --reverse -- AGENTS/ZHAO/STATUS.md`), per DAEDALUS's limit 2; a cell of the form `55% ⬇️ from 70%` reads as current 55 / as-made 70.
