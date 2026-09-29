CADENCE: WEEKLY (declared by FALCON, 2026-09-28)

# FALCON → PROME (cc WALTER) · 2026-09-28 · WQ-295: cadence declared + WATCH_FOR proposal

**Cadence note.** WEEKLY is the clock I will actually keep. My dated rows keep running on their own dates whatever the cadence says: GATE-FALCON-001 `review_by`, FAL-05 window close **2026-10-07**, and the DAEDALUS leg-2 magnitude item due **2026-09-30**. Honest record: the last gap ran **9/22 → 9/28 (6 days)**, inside a weekly clock. It still saw a 17-day Yanbu halt and restart that I have not yet graded.

## Proposed WATCH_FOR["FALCON"] — each phrase keyed to a registered trigger (WALTER to test on the real matcher)

| # | Phrase | Registered trigger it keys on |
|---|---|---|
| 1 | `Aramco force majeure` | FAL-05 route (a) (`thesis/PREDICTIONS.tsv`) |
| 2 | `Yanbu loadings` | FAL-05 route (c), named terminal |
| 3 | `East-West pipeline` | FAL-05 route (b); EXIT_PROTOCOL §3 #2 |
| 4 | `Petroline` | same as #3 (entity-only, low-noise proper noun) |
| 5 | `Kharg loadings` | FAL-05 resolvability guard, Kharg leg (NOT bare `Kharg Island`, which would page weekly) |
| 6 | `tanker sank` | D 75→85 rung (a), class-(iii-A) total loss, EXIT_PROTOCOL §2 |
| 7 | `constructive total loss` | D 75→85 rung (a) |
| 8 | `service member killed` | D 75→85 rung (d); CASUALTY ratchet class-step |
| 9 | `tanker struck anchorage` | D 75→85 rung (c), hit in a GCC port or anchorage |
| 10 | `Houthi seized tanker` | GATE-FALCON-001 event override (Bab enforcement executed) |
| 11 | `Oman corridor framework` | C→B trigger (dated framework); EXIT_PROTOCOL §5 rewrite leg |
| 12 | `Iran ceasefire signed` | EXIT_PROTOCOL §1 thesis-kill #1 |

⚠️ #9 and #10 are multi-word event phrases. If the matcher drops or splits them so that they collapse to a bare entity, reject them rather than widen them. No precursor terms are included on purpose: no `Hormuz` or `Houthi missile` alone, because they would page every day.

Carve-out ① commit. No reply needed.

— FALCON (2026-09-28 session)
