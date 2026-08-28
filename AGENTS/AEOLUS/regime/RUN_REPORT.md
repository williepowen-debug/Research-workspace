run_date: 2026-08-27

observations_added: 5 rows to SERIES.tsv (nino34_weekly/nino3_weekly/nino12_weekly/nino4_weekly for 19AUG2026 week), 3 rows to LOG.tsv (enso_discussion_unchanged, weekly_briefing_deck_found, weekly_mismatch_basis_investigation_UNRESOLVED)

threshold_state:
- ONI vs "strong" ≥1.5 line: +1.39 (MJJ 2026, CPC-oni.ascii, unchanged since 8/13) — 0.11 below — NOT-FIRED
- Very-strong probability (>90%, OND NH fall/winter): 90% (CPC-ensodisc 13Aug2026, still current issue) — RESTATED not raised — NOT-FIRED (already >90% since 8/13)
- Historic-event probability (≥+2.5 RONI, OND): 69% (CPC-ensodisc 13Aug2026) — unchanged — NOT-FIRED
- RONI MJJ 2026: +0.98 — unchanged since 8/21 pull (no new season posted) — 1.52 below the +2.5 historic bar — NOT-FIRED
- Weekly Niño-3.4: +2.6 (19AUG2026, CPC-wksst9120.for) — down from +2.7 (12AUG) — first WoW pullback of the season

changes:
- Weekly Niño-3.4 ticked DOWN for the first time this season: 05AUG +2.6 -> 12AUG +2.7 -> 19AUG +2.6. Niño-1+2 also eased: +4.0 (12AUG, unchanged) -> Niño-4 +1.0 -> +0.8. Niño-3 still climbing: +3.2 -> +3.3.
- No new ONI or RONI season posted (still MJJ 2026 on both); no new sstoi monthly (still Jul 2026). Next release ties to the 10Sep2026 monthly ENSO Diagnostic Discussion.
- ensodisc.shtml (the monthly discussion) is UNCHANGED — still the 13Aug2026 issue, still quoting July monthly index values +1.4/+1.7/+2.9 (Niño-3.4/3/1+2, ERSSTv5/v6 basis).
- Found and pulled CPC's standing WEEKLY product "ENSO: Recent Evolution, Current Status and Predictions" (33-slide PDF, https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/lanina/enso_evolution-status-fcsts-web.pdf), prepared-date 24Aug2026 — confirms a weekly update DOES exist and DID land in the 8/13->9/10 monthly-discussion gap. Not currently listed in SOURCES.md. RONI restated as "1.0°C" (rounds from 0.98, consistent). Alert status unchanged: El Niño Advisory.
- 🔴 RESOLVED THE SOURCE (but not the mechanism) of the 8/20-21-logged discussion-basis trap: the anomalous 1.8/2.5/3.2 (Niño-3.4/3/1+2) quote traces to this weekly briefing deck's "latest weekly SST departures" bullet slide, NOT ensodisc.shtml (whose own July monthly figures are a third, different triple). Full investigation below.

proposed_findings:
1. RONI vs ONI magnitude, two separate reads, never averaged (written into DOSSIER §OPEN QUESTIONS item 2, AEOLUS still owns the actual channel-sign re-derivation): ONI +1.39 (0.11 below "strong"); RONI +0.98 (moderate on the dynamical scale, needs ~+1.5 more over 5 seasons to OND to reach the +2.5 historic bar CPC quotes odds against, at the current ~+0.45-0.53/season acceleration pace).
2. Propose adding the weekly briefing PDF (URL above) to SOURCES.md as a fifth verified source — it is the only CPC primary that updates in the gap between monthly ENSO Diagnostic Discussions, and it is where the discussion-basis trap actually originates. AEOLUS's call whether to formalize it and assign it an instrument name.
3. The 24Aug deck's RONI restatement (1.0°C, rounds from 0.98) is internally consistent with CPC-RONI.ascii — no discrepancy there, only on the Niño-region weekly bullet slide.

gaps: none — all four indices + the monthly discussion + the weekly briefing deck were pulled successfully on the first try, all via SOURCES.md-listed or newly-verified CPC primary URLs.

---

## STEP 3 — THE NAMED OPEN JOB: verdict = UNRESOLVED

**Question:** what basis produces the CPC weekly-briefing-deck figures (Niño-3.4/3/1+2/4 = 1.8/2.5/3.2/0.0) that mismatch CPC's own `wksst9120.for` (12AUG: 2.7/3.2/4.0/1.0)?

**Traced the actual source:** NOT `ensodisc.shtml` (the monthly discussion) — that document's own "July Niño index values" are a THIRD, different triple: +1.4/+1.7/+2.9 (Niño-3.4/3/1+2), sourced to ERSSTv5/v6 monthly data, per its own prose. The mismatched 1.8/2.5/3.2/0.0 quad is from a DIFFERENT product: the weekly briefing PDF "ENSO: Recent Evolution, Current Status and Predictions," slide "Niño Region SST Departures (°C) Recent Evolution," bullet "The latest weekly SST departures are:".

**Ruled out, with method:**
1. **Any single 2026 week of `wksst9120.for`** — pulled the full 2026 series (Jan–19Aug) and checked every row for the quad 0.0/1.8/2.5/3.2 across all four regions simultaneously. No match at any date.
2. **A running mean of recent weekly OISST** — 4–5 week trailing mean of Niño-3.4 ≈ 2.5–2.6, well above 1.8; does not explain the gap.
3. **The monthly ERSST figures quoted in `ensodisc.shtml`** — a different, third triple (+1.4/+1.7/+2.9), does not match either.
4. **A stated CPC product/methodology difference** — checked the weekly briefing deck's own RONI-slide footnote: *"a different SST dataset is used for weekly SST monitoring (slides #4-9) and is using OISSTv2.1 (Huang et al., 2021)"* — i.e. CPC's own documentation says the Niño-region weekly slide SHOULD be on the same OISSTv2.1 basis as `wksst9120.for`. No base-period, product, or smoothing-window difference is documented anywhere I found (RONI definition page, ONI/RONI footnotes, the deck's own methodology slides) that would explain the mismatch.

**New evidence this pass, offered as a pattern, not a proof:** the identical 0.0/1.8/2.5/3.2 quad reappears VERBATIM in the 24Aug2026-dated deck — 11 days after the DOSSIER's first read of it around 8/20-21 — while `wksst9120.for` itself moved in that same window (12AUG 2.7/3.2/4.0/1.0 → 19AUG 2.6/3.3/4.0/0.8) and the SAME deck's RONI figure (1.0°C, rounding 0.98) DID update correctly. This is consistent with that one bullet-list slide being stale / not regenerated on the weekly refresh cycle that the rest of the deck follows — but no CPC text confirms this, so it is reported as an observation, not a resolution.

**A uniform ~−0.8°C offset across all four Niño regions simultaneously** (rather than a region-varying offset, which a base-period change would produce) is the pattern most consistent with subtracting a common quantity (e.g., a RONI-style tropical-mean term) — but I found no CPC documentation stating that this specific slide does that, and the magnitude (~0.8) does not cleanly match the current documented ONI−RONI seasonal offset (~0.41) or any obvious multiple of it. Not asserted; flagged as the one hypothesis the evidence shape would fit if it turns out to be real.

**Ruling applied:** treat `wksst9120.for` as the sole authoritative weekly figure. Do not cite the weekly-briefing-deck bullet numbers for anything scored. Full detail logged to `workbook/LOG.tsv` under `weekly_mismatch_basis_investigation_UNRESOLVED`.
