# METSUKE MEMORY

State file for the trade-doc staleness-flagger sub-agent. Spec is in [`METSUKE.md`](METSUKE.md) (durable). This file holds dated state: run history, pending items, standing monitors, calibration.

**Ownership:** METSUKE writes this file directly at end-of-run — `## LAST RUN` append, `## PENDING` / `## STANDING MONITORS` adjust, `## NEXT RUN HINTS` write. **`## CALIBRATION` is SAM-owned** (METSUKE cannot self-grade its own approve/decline rate from inside a run). SAM may also pre-edit between runs to seed `## NEXT RUN HINTS` or `## PENDING`.

**Spawn order:** METSUKE reads `METSUKE.md` first (spec), then `METSUKE_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what was last flagged*.

---

## CHANGES SINCE LAST RUN

*Auto-populated by METSUKE at run start: what's moved in STATUS / THESIS / PREDICTIONS / CHANGELOG / TIMELINE / docket since the previous run. Cleared at end-of-run.*

*(empty — inaugural METSUKE_MEMORY entry; first run will populate)*

---

## LAST RUN

*(empty — METSUKE has not yet been spawned. First run will populate.)*

### Run template (for the inaugural and subsequent runs)

```
### Run N — YYYY-MM-DD (one-line context — e.g. "post Jun-1 POV pivot sweep")
- STALE-MARK:        [N items, brief one-line each]
- STALE-FRAMING:     [N items]
- DUP-LIVE-SPOT:     [N items]
- TRIGGER-STATUS-DRIFT: [N items]
- CAL-DRIFT:         [N items]
- ARCHIVE-CANDIDATE: [N items]
- MONEY-FIELD-ESCALATION: [N items — Will-confirm only]
- CHANGELOG-GAP:     [N items]
- Sections checked + clean: <short summary>
- SAM-applied:       <which flags SAM applied this turn> (filled by SAM post-run; left blank by METSUKE)
- SAM-declined:      <which flags SAM declined + brief reason> (filled by SAM post-run)
```

---

## PENDING (escalations SAM hasn't yet resolved)

*Items METSUKE has flagged across runs that SAM has not yet applied or declined. Cleared by SAM as they're resolved. METSUKE only adds, never removes.*

*(empty — first METSUKE_MEMORY)*

---

## STANDING MONITORS (surface each run)

*Recurring drift watches METSUKE should re-check every run.*

- **SAM-21 mark in TRADE/STRATEGY body** vs current PREDICTIONS trajectory tail. Highest-frequency drift type historically (BOJ-hike mark moves on CPI prints, market repricing, BOJ commentary).
- **SAM-23 mark in TRADE/STRATEGY body** vs current PREDICTIONS trajectory tail. Moves on MOF intervention zones, Iran/MOU status changes, Brent direction.
- **THESIS header banner date** vs `Last Updated:` lines in TRADE / STRATEGY headers. When THESIS banner has a more-recent POV-pivot annotation than the TRADE/STRATEGY header, downstream body drift is likely.
- **RISK FACTORS mitigation columns** — THESIS table is canonical; TRADE's parallel table tends to lag 1-2 POV pivots on the mitigation prose.
- **STRATEGY "WHERE WE ARE IN THE TRADE" stage-table top-row prose** — captures the live narrative; highest framing-drift watch.
- **TRADE Hard-Trigger status notes** (PENDING / ✅ FIRED / NEAR-MISS / partial-trigger annotations) — drift on intervention zones, channel-status transitions, Big 3 ESR resolutions, etc.
- **TRADE Key Dates** vs `docket/CALENDAR.md` forward-event set — drifts whenever KOYOMI updates CALENDAR without a follow-up TRADE refresh.
- **Live-spot duplication in TRADE/STRATEGY forward tables** — anything framed as *current* (vs *historical breach on date X*) that duplicates a STATUS feed.

---

## CALIBRATION

*SAM-owned. METSUKE does NOT edit this section. Records SAM's pattern of which flag categories SAM accepts/applies vs declines, and what makes the difference. Lets METSUKE bias future reporting toward what SAM actually treats as drift.*

*(empty — populated by SAM after the first METSUKE run, as the approve/decline pattern emerges. Template categories below.)*

### Categories to track (SAM fills these in as data accumulates)

- **STALE-MARK accept rate:** _(SAM fills)_ — likely near 100% (numerical drift is unambiguous)
- **STALE-FRAMING accept rate:** _(SAM fills)_ — expected to be lower (framing edits often deliberate or iterating)
- **DUP-LIVE-SPOT accept rate:** _(SAM fills)_ — should be high if the no-same-data-in-two-docs rule holds
- **TRIGGER-STATUS-DRIFT accept rate:** _(SAM fills)_
- **CAL-DRIFT accept rate:** _(SAM fills)_ — calibrates against KOYOMI cadence
- **ARCHIVE-CANDIDATE accept rate:** _(SAM fills)_ — biased low; SAM tends to keep history
- **MONEY-FIELD-ESCALATION rate:** _(SAM fills)_ — escalations should be rare; high rate = METSUKE running too hot on money fields
- **Run-level signal-to-noise:** _(SAM fills, e.g. "Run N: 6 flags / 5 applied / 1 declined as iterating = 83% S/N")_
- **Common decline reasons:** _(SAM fills, e.g. "framing left intentionally pending Will decision," "iterating; not stale")_

---

## NEXT RUN HINTS

*Forward-looking context to bias the next run. SAM seeds these between runs; METSUKE may also write at end-of-run when a future condition is anticipated.*

### Inaugural-run hints (Jun 1 2026 baseline state of trade docs)

- **First-ever METSUKE run will be a full sweep.** No watermark; read both files end-to-end against current state-of-truth. Expect a longer report than steady-state runs — TRADE got a 2-pass refresh on Jun 1 (post-MOU break) but STRATEGY's last refresh was 2026-05-28 (Tokyo CPI dovish-miss framing) and is now ~4 days behind two material POV pivots (May 31 BOJ repricing → SAM-21 70%; Jun 1 MOU break → SAM-23 ~72%).
- **Likely STRATEGY drift hotspots (inaugural run targets):**
    1. Header `Last Updated: 2026-05-28` and `**Position:** ... | **Thesis:** v1.5 (single-path)` block — the May 28 framing predates two POV pivots.
    2. § WHERE WE ARE IN THE TRADE row 3 — explicitly says "**June BOJ in 13 trading days is the dominant remaining catalyst — now dovish-impaired after Tokyo May CPI (core-core 1.6%, May 28) softened the hike to ~50%**" and "WE ARE HERE — v1.5 single-path; Channel 1 deferred; Channel 3 dormant on Brent collapse; June BOJ is the dominant remaining near-term trigger (coin-flip post-Tokyo-CPI)." Both clauses are superseded twice (May 31 repricing + Jun 1 MOU break).
    3. § DECISION RULES > Post-Tranche-2 hard-triggers table — BOJ row "SAM-21 ~50%" stale; Bessent / Channel 3 row "dormant since on Brent collapse" stale; USDJPY-sub-155 row "Oil now $93.13" carries live-ish spot.
    4. Any references to Channel 3 as "dormant" anywhere downstream.
- **Likely TRADE drift hotspots (inaugural run targets):**
    1. § Watchlist > TLT — § 5/27 framing may be marginally out of date; check.
    2. § Carry Unwind Probability table — recently refreshed Jun 1 but verify against STATUS.
    3. § Risk Factors table — recently refreshed Jun 1 (Jun 1 THESIS 18:07 commit propagated; double-check parity).
    4. § Key Dates — refreshed Jun 1 but verify CAL-DRIFT vs docket/CALENDAR.
- **Sequencing:** METSUKE's inaugural run should be spawned AFTER any pending SAM-side TRADE/STRATEGY refresh, not before. Running while SAM is mid-edit will race the working tree.
- **Inaugural-run mode is "report-only — calibrate against."** SAM uses Run 1 to grade what's signal vs noise, then fills CALIBRATION accordingly before Run 2.
