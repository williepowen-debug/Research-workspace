# FERT — Registered gate grade history

**LIVE — Last real data refresh: 2026-10-07** (10/7 print appended + 9-print rate cut) | Staleness sweep: 2026-10-07
**Split out of `STATUS.md` 2026-09-15** (read-cap remedy, hot/cold split). STATUS carries the **current** grade and the rate; this file carries the **print-by-print history**. GATE letters are never restated here. **Letter homes:** `GATE-FERT-G5` → `workbook/TRIGGERS.tsv` row **T4** (`Why_It_Wakes_You` cell, encoded 2026-10-09 verbatim from the GATES cell — closes the circular pointer DAEDALUS Gate-Basis #2 ② found; PROME re-points the GATES cell); `GATE-FERT-G3` → `PROME/GATES.tsv` (unchanged).

## GATE-FERT-G5 — DTN retail DAP **or** MAP > $1,000/ton ($/ton, DTN Progressive Farmer weekly)

⛔ Never Pink Sheet $/mt, never NOLA $/st — different instruments, hundreds of dollars apart, and the gate does not name them.

**Grading terms — mirrored 2026-10-01 from `PROME/GATES.tsv` GATE-FERT-G5 (WQ-351, PROME-encoded 10/01 under Will's 13:54 ET "safe queue rows" instruction; FERT's own §3 text; level, operator, instrument UNCHANGED).** The letter itself lives at `TRIGGERS.tsv` T4 (since 2026-10-09; before that, the GATES cell) — this block mirrors the clarification only, so a grader here reads the same terms:
- **Geography:** DTN **US national average** retail, as printed in the weekly article.
- **Tie:** strictly **> $1,000/ton** at DTN's whole-dollar precision — **a $1,000 print does NOT fire.**
- **Base rate:** the Pink Sheet DAP $781.3/mt = 93rd-percentile figure is registration **CONTEXT, not this gate's base rate** (different instrument, unit, cadence and operator).
- ⚠️ **Caveat kept (PROME's wording):** "no free DTN base rate exists" is FERT's **inference from one article's subscriber note**, not tested against every archive path.

| Print (article) | Data week | DAP $/ton | MAP $/ton | Binding leg | Gap to $1,000 | Grade |
|---|---|---|---|---|---|---|
| 8/12/26 *(registration baseline)* | Aug 3–7 | $917 | $959 | MAP | $41 · **+4.28%** | — |
| **8/19/26** | Aug 10–14 | $917 | **$960** | MAP | $40 · **+4.17%** | **NOT FIRED** |
| **8/26/26** | Aug 17–21 | $916 | $959 | MAP | $41 · **+4.28%** | **NOT FIRED** |
| **9/2/26** | Aug 24–28 | $918 | $959 | MAP | $41 · **+4.28%** | **NOT FIRED** |
| **9/9/26** | **Aug 31–Sep 4** | **$919** | **$959** | **MAP** | **$41 · +4.28%** | **NOT FIRED** |
| **9/16/26** | **Sep 7–11** | **$923** | **$962** | **MAP** | **$38 · +3.95%** | **NOT FIRED** — graded 9/17 on MIRROR; **confirmed first-party at dtnpf.com 9/22** (`KB-FERT-040`) |
| **9/23/26** | **Sep 14–18** | **$925** | **$967** | **MAP** | **$33 · +3.41%** | **NOT FIRED** — PRIMARY, first-party curl at dtnpf.com 9/23 (`KB-FERT-043`) |
| **9/30/26** | **Sep 21–25** | **$926** | **$970** | **MAP** | **$30 · +3.09%** | **NOT FIRED** (7 of 7 graded) — PRIMARY, first-party curl at dtnpf.com 2026-10-01 11:06 ET (`KB-FERT-045`) |
| **10/7/26** | **Sep 28–Oct 2** | **$934** | **$974** | **MAP** | **$26 · +2.67%** | **NOT FIRED** (8 of 8 graded) — PRIMARY, first-party curl at dtnpf.com 2026-10-07 21:44 ET (`KB-FERT-062`); strictly-greater, whole-dollar, US national average as printed |

🔑 **The APPROACH RATE is the finding, and it is stated here as a rate — a gate row shows distance, never rate.**

| Leg | 8/12 baseline | 9/9 print | Move over 28 days | **Realised approach rate** | **Implied time-to-fire at that rate** |
|---|---|---|---|---|---|
| **MAP (binding)** | $959 | $959 | **$0 · 0.00%** | **0.00 %/mo** | **UNDEFINED — the line is never reached** |
| DAP (second) | $917 | $919 | +$2 · +0.218% | **+0.22 %/mo** | **~40.5 months** (≈ early 2030) |
| *G5 base rate at registration* | — | — | — | *~+0.50 %/mo* | *~8.5 months* |


**Approach rate, 7-print cut (8/12 → 9/23, 6 weeks) — supersedes the 9/9 table above for current use:**

| Leg | 8/12 baseline | 9/23 print | Move over 42 days | Realised approach rate | Implied time-to-fire at that rate |
|---|---|---|---|---|---|
| **MAP (binding)** | $959 | $967 | +$8 · +0.834% | **~+0.60 %/mo** (+0.139 %/wk) | **~5.6 months** (≈ mid-Mar 2027) |
| DAP (second) | $917 | $925 | +$8 · +0.872% | **~+0.63 %/mo** (+0.145 %/wk) | ~12.4 months |

Both legs are now above the ~+0.50 %/mo registration base rate; most of the move came in the last two prints (MAP all of it; DAP +$6 of +$8), after a five-print stall. Two prints is not a trend; not scored.

**Approach rate, 8-print cut (8/12 → 9/30, 7 weeks) — supersedes the 7-print cut for current use** (log basis, 4.35 wk/mo, same method):

| Leg | 8/12 baseline | 9/30 print | Move over 49 days | Realised approach rate | Implied time-to-fire at that rate |
|---|---|---|---|---|---|
| **MAP (binding)** | $959 | $970 | +$11 · +1.147% | **~+0.71 %/mo** (+0.163 %/wk) | **~4.3 months** (≈ early Feb 2027) |
| DAP (second) | $917 | $926 | +$9 · +0.981% | **~+0.61 %/mo** (+0.140 %/wk) | ~12.7 months |

Third consecutive up-print on both legs; the w/w pace slowed (MAP +$5 → +$3, DAP +$2 → +$1). A last-three-prints window (9/9 → 9/30) puts MAP at ~+1.65 %/mo (~1.8 months to the line), but three prints is a window, not a trend, and is not used for the grade or the score.

**Approach rate, 9-print cut (8/12 → 10/7, 8 weeks) — supersedes the 8-print cut for current use** (log basis, 4.35 wk/mo, same method):

| Leg | 8/12 baseline | 10/7 print | Move over 56 days | Realised approach rate | Implied time-to-fire at that rate |
|---|---|---|---|---|---|
| **MAP (binding)** | $959 | $974 | +$15 · +1.564% | **~+0.84 %/mo** (+0.194 %/wk) | **~3.1 months** (≈ mid-Jan 2027) |
| DAP (second) | $917 | $934 | +$17 · +1.854% | **~+1.00 %/mo** (+0.230 %/wk) | ~6.8 months (≈ early May 2027) |

Fourth consecutive up-print on both legs. W/w: MAP +$4 (pace held, +$3 → +$4), DAP **+$8** (pace jumped, +$1 → +$8 — the largest DAP weekly move in the series). Both legs are each the highest of the 14 monthly rows in DTN's own 10/7 table. A last-five-prints window (9/9 → 10/7) puts MAP at ~+1.69 %/mo (~1.6 months to the line) — a window, not a trend, not used for the grade or the score. Root context: Pink Sheet rock **flat** at $170.0/mt for Jul–Sep (FERT-11 HIT) while Gulf DAP rose +0.9% m/m — the retail run is not rock-fed.

**Next grade: 2026-10-14 DTN weekly** (T4 wake; owner-set `review_by` for `G:GATE-FERT-G5`; find the slug on the dtnpf.com crops index, then curl the article).
