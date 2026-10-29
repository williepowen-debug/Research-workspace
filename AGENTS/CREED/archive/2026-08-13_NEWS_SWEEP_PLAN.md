# CREED News Sweep — PLAN
**Date:** 2026-08-13 · **Window:** 2026-07-27 → 2026-08-13 (CREED's dark stretch; last live coverage was the 7/27 catch-up)

## Sources
- WebSearch (Trepp/Connect CRE/CRE Direct/Commercial Observer/Bisnow/GlobeSt/Real Deal secondary coverage of Trepp data — Trepp itself paywalled, standing caveat)
- EDGAR full-text search / direct filing pulls for any named 8-K/10-Q events (servicer transfers, note sales, dispositions) surfaced by the sweep
- FDIC.gov for the Q2 2026 Quarterly Banking Profile (the named overdue item)
- MBA (mba.org) for any early Q2 CM/MF release signal (full print isn't due till ~mid-Sept, but checking for a release-date announcement is in scope)

## What counts as MEANINGFUL for this lane
Per the forum's own finding this session (recognition evidence arrives away from the headline DQ/SS series), scope is wider than the monthly print:
1. **Servicer transfers / appraisal / ARA (appraisal-reduction-amount) events** — the stage where CREED's own forum P0 said forced recognition actually happens
2. **Named handbacks, note sales, REO liquidations** — actual transaction prices (forced-sale comps, `S6`)
3. **Maturity/extension/modification news**, especially a **third-extension-refused** class event (the Sangertown pattern) or a large hard-maturity default
4. **CMBS new-issue volume and spread color** — a mechanism vector CREED's workbook doesn't currently carry a vector for; note as a coverage gap if it surfaces
5. **GSE/multifamily** — read only, not scored (HOMER-owned); route anything live to HOMER
6. **Bank CRE disclosures** — named banks, provisions, PDNA, reserve coverage; route anything bank-specific to REGINALD/WAL, note only what's directly S3-relevant
7. **FDIC Q2 QBP** — named overdue item, check publication status first

**Not meaningful:** routine monthly DQ/SS re-statements already captured (July print is in `VX.tsv` from this session); duplicate coverage of the ARI→Athene deal already fully worked this session; anything dated outside the window without a stated reason for inclusion.

## Dedupe pass (against board_log.tsv + inbox/processed/, this session's other work)
Already covered, exclude from "new" findings unless a genuine update surfaces: July Trepp office/overall/MF/industrial DQ (11.91%/7.86%/7.69%/1.13%), ARI→Athene $8.7B closing + Athene Q2 10-Q, KREF Q2 credit-loss detail, Sangertown SS transfer, the three named July mall/office/showroom newly-delinquent loans (Chicago office tower, Seattle office portfolio, Times Square×2, NC/NV showroom portfolio), 1740 Broadway precedent, HOMER's GSE MF 60-day-metric correction, courier-arrangement kill.

## Rails
- Date-check every article before citing (anniversary-article trap — a year-old piece resurfacing).
- Trepp: primary-CITED only, never primary-read, labeled every time.
- Single-source live-event claims = LEADS, explicitly labeled, not carried as findings.
- No threshold/band moves. Anything touching `PRED-CREED-001` or another registered row gets **flagged**, not graded — the August print is not out yet.
- Cross-domain findings get packeted to the owner (carve-out ①, self-committed): HOMER (housing/MF), WAL/REGINALD (bank names), BROCK (vehicle-side private-credit).
- This sweep is explicitly **not** FORUM 5's W1 leg (maturity-adjusted-DQ availability check) — that's a separate, next-session task per the ruling.
