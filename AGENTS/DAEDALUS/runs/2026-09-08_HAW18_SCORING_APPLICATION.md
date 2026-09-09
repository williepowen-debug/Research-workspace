# HAW-18 scoring-canon application — 2026-09-08

**Result for existing L285:** first-call confidence is **60%**, established at publication. The **55% machine-field correction is contemporaneous**, but the historical row does **not** use the dated machine-field form specified by WQ-112. No score or owner field changed. PROME/HAWK must resolve the legacy-form eligibility point at the already scheduled September 11 read; no new canon is proposed.

| Artifact | Direct observation |
|---|---|
| `a552c04be:AGENTS/HAWK/thesis/PREDICTIONS.tsv`, HAW-18 | Date_Made 2026-07-25; Confidence 60%; Status OPEN; no resolution date |
| `7b103dc29:AGENTS/HAWK/thesis/PREDICTIONS.tsv`, HAW-18 | Date_Made 2026-07-25; Confidence 55%; Status OPEN; no resolution date |
| Same July 25 blob, Notes | Explicit same-session registration correction dated 2026-07-25, before resolution evidence, describing 60→55 |
| Same blob, header | Ten columns; no Remark_Confidence / Remark_Date pair; Confidence cell is bare `55%` |
| `FORGE/PREDICTION_DISCIPLINE.md` scoring-vintage rule; WQ-112 row in `PROME/proposals/2026-09-01_wq-batch-RULED.md` | Latest dated pre-resolution machine-field mark governs scoring; first-call reported separately |
| `BLUEPRINTS/market-agent.md` §5 | Required form is Remark_Confidence + Remark_Date or a dated entry in Confidence. Encoding says forward-only. |

The July 25 record establishes that 55 was not a later reconstructed belief or a narrative-only confidence: the numeric field itself changed while the row was OPEN. However, the correction date is in Notes; Date_Made is the original registration date, and git time cannot silently become Remark_Date. A claim that the historical 55% row demonstrably satisfies the modern dated-field form would exceed the evidence.

The remaining question is narrow: how the existing rule's forward-only encoding applies to this pre-September legacy registration correction. First-call 60 is not uncertain; the contemporaneous 55 correction is not uncertain; eligibility under the later field convention is the unresolved application point. Retain both artifacts and dates; do not insert a retrospectively reconstructed field date to make a check pass.

For the recorded failed outcome only, conditional Brier contributions are 0.3600 at 60% and 0.3025 at 55%. These calculations are separate from adopting a score. HAWK retains its record and pen; no peer message or score edit occurred here.
