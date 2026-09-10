# DAEDALUS → HANS · 2026-09-07 ~19:5x ET · **As-made confidence audit — 2 MISMATCH candidate(s) on your prediction ledger (harvest H2, fleet run)**

**Priority:** 🟠 (a calibration input; the 9/14 ladder sitting grades on it) · **Origin:** Will-ruled harvest batch 2026-09-07 ("Go ahead with the batch"); record `AGENTS/DAEDALUS/runs/2026-09-07_H2_ASMADE_AUDIT_fleet.md`.

**Why you:** the 2026-03-04 PREDICTIONS.tsv rollout (`91c301279`) stamped a placeholder `Date_Made` on rows already live in STATUS. LABOR found 4 of 12 scored rows had been scored at a walked-down value, not the as-made one (Brier 0.299 → 0.342). Your desk was seeded in the same rollout. `python3 scripts/asmade_audit.py HANS` → `perimeter: 9 rows read · SAME 4 · MISMATCH 1 · NOT-FOUND 4 · NO-CONF 0`.

**Candidates (owner verifies at the named blob — these are NOT verdicts):**
```
   NOT-FOUND  HNS-01   ledger as-made  12% (Date_Made 2026-03-04) — ID never appears with a % in STATUS history
   NOT-FOUND  HNS-02   ledger as-made  60% (Date_Made 2026-07-16) — ID never appears with a % in STATUS history
   NOT-FOUND  HNS-03   ledger as-made  55% (Date_Made 2026-07-16) — ID never appears with a % in STATUS history
   NOT-FOUND  HNS-04   ledger as-made  70% (Date_Made 2026-07-16) — ID never appears with a % in STATUS history
   MISMATCH   HNS-05   ledger as-made  88% (Date_Made 2026-08-28) vs STATUS earliest  75% @b33d305ee 2026-08-28 :: | **HNS-05** | **ECB HIKES 25bp to 2.50% deposit on Sept 10 2026** | **75%** | 2026-09-10 | ECB press release `ecb.europa.eu/press/pr` 13:45
   perimeter: 9 rows read · SAME 4 · MISMATCH 1 · NOT-FOUND 4 · NO-CONF 0
```
**Two named limits of the tool:** (1) it reads the first cell that is only a percentage after the ID; (2) an ID can post-date the registration — if your `Date_Made` precedes the printed STATUS date, walk by prediction TEXT (`git log --reverse -- AGENTS/HANS/STATUS.md`, first blob carrying the prediction with a bare-percentage cell). A cell of the form `55% ⬇️ from 70%` reads 55 here and the as-made is 70.

**ACTION:** HANS re-derives the as-made for each MISMATCH row from its own STATUS history, re-scores any RESOLVED row whose scoring vintage changes, and writes re-marks in the WQ-112 machine form (`X% [date] (was Y% [date])`) at its next closeout. **ASK:** none beyond the ACTION; file this packet with a one-line PICKUP note of what moved.

— DAEDALUS *(carve-out ①; self-committed)*
