# CORAL — MEMORY

*Cross-session memory. Feedback (Will's corrections/confirmations), Findings (concrete tool/data/domain facts), References, and the session handoff. Not a STATUS recap. Prune superseded entries.*

---

## Feedback

| Date | Feedback |
|------|----------|
| 2026-06-19 | Will promoted CORAL from a REGINALD sub-agent to a **top-level peer agent** (parallel to OZK). Florida is to be a first-class agent again. Same path OZK took 2026-04-24. |

## Findings

| Date | Finding |
|------|---------|
| 2026-06-19 | **Boundary with MARCO is the live coordination risk.** MARCO's STATUS calls Florida its "primary focus — triple exposure (insurance + tourism + migration)" and has been carrying the live FL condo/airport/snowbird read while CORAL was dormant. Split: CORAL = bank-/CRE-level FL stress; MARCO = population-driven FL stress. Cross-read MARCO before publishing any shared FL metric. |
| 2026-06-19 | **CORAL's prior STATUS (last updated 2026-03-03) is materially stale.** Per MARCO's current read, FL condo inventory actually *tightened* back below 9mo by April (8.9mo), Miami-Dade 12.9mo (down YoY), and the acute-stress timing pushed to winter 2026-27 — the opposite direction from CORAL's Mar "RED / cascade extending" framing. Do NOT trade off the old STATUS until refreshed. |

## References

- Parent hub: `../REGINALD/STATUS.md` (convergence matrix, bank watchlist), `../REGINALD/SUB_AGENTS.md` (legacy sub-agent coordination doc)
- FL population-driven twin: `../MARCO/STATUS.md` ("Florida Triple Exposure" block)
- Spinout record: LOST (dead pointer confirmed 7/9 — see CLAUDE.md History note); no file to cite
- SSB thesis: `research/SSB_THESIS.md`

---

## Findings (added 2026-06-19 refresh)

| Date | Finding |
|------|---------|
| 2026-06-19 | **The FL thesis is SPLIT, and the split is the whole point.** The household/condo leg confirms hard (FL #1 foreclosure, REOs +108% YoY, condo −6.1%, 92% of markets down, assessments live). The *bank* leg does NOT (SSB/SBCF/BKU/VLY Q1 NCOs 9-14bps, stable credit). Don't conflate "Florida real estate is stressed" with "FL banks are about to take losses" — Q1 2026 says the banks are absorbing it. |
| 2026-06-19 | **"Rate-shock reclass ≠ loss content" is the bank-leg crux.** SSB's classified CRE ($2.5B) is loans underwritten at 3% rate-shock now stressed by the 5% move — but 56% wtd-avg LTV and 98% current. Until LTVs break or payments stop, classified-CRE growth is a reclassification artifact, not realized loss. Q2 earnings test: does it migrate to nonaccrual/charge-off, or cure? |
| 2026-06-19 | **Insurance channel went the OTHER way.** Original thesis treated FL insurance as a hardening amplifier; in 2026 it's easing — Citizens depopulated to 294K (−64% YoY) *(label corrected 7/21 → ML-CORAL-035: that was a TOTAL, not personal; Jun-30 canonical 278,246)* + 8.8% rate cut, reinsurance −15-20% at 6/1. A hurricane landfall is the only near-term reversal risk. |
| 2026-06-19 | **CORAL and MARCO independently converged** on "acute FL stress delayed to winter 2026-27." Shared condo-inventory metric matches exactly (8.9mo statewide, Miami-Dade 12.9mo) — MARCO is the live owner; CORAL references. |
| 2026-06-19 | **Sargassum integrated as a 2nd-order demand overlay (Will-provided briefing).** Record-tier 2026 belt lands on exactly CORAL's worst SE FL condo metros (Atlantic coast; Gulf spared) — *stacks on the same geography, doesn't diversify.* But it's perception-driven + modeled ($2.7B/yr not realized), does NOT touch insurance, and has NO Q1 bank-balance-sheet evidence → logged as monitored vector (VX-CORAL-SARG-01), NOT a status-mover. Boundary: MARCO owns tourism visitor-flow/spend; CORAL owns coastal-RE amenity/collateral. |
| 2026-06-20 | **Recent-vintage negative equity is now a formal upstream CORAL canary.** WALTER SIG-002 delivered Parcl/Lewris+Cotality corroboration: ~18-20% of 2024-vintage financed FL buyers underwater, 84%+ of underwater loans originated in last ~3.5 yrs, concentrated in SW-FL Gulf Coast (Cape Coral/Punta Gorda/Fort Myers/Naples/North Port/Lakeland). This is collateral deterioration upstream of bank P&L, not bank-loss evidence yet. |
| 2026-06-20 | **Bankruptcy rank resolved: true but population-inflated.** WALTER SIG-008/AOUSC packet confirms M.D. Fla #2 and S.D. Fla #6 by volume (12mo ended 2026-03-31), but FL per-capita filing rate (~190/100k) is only modestly above national (~168-173) and far below bankruptcy-belt states. The real signal is +22.2% YoY, consumer-led acceleration; tripwire = Ch.7/capita >~230/100k. |
| 2026-06-20 | **Insurance framing corrected to split read.** Personal/reinsurance easing remains true, but Citizens Commercial Lines +10.4% capped vs +18.8% uncapped means the condo-association/master-policy layer is still a live cost amplifier. Never summarize FL insurance as simply “easing” without layer. |
| 2026-06-20 | **Thesis rails installed at `thesis/THESIS.md` + `thesis/CHANGELOG.md`.** Durable CORAL rule: household/condo stress is confirmed, but bank-loss transmission upgrades only on bank evidence — synchronized deterioration across ≥2 FL-exposed banks or explicit USCB condo-association loan deterioration with corroborating consumer/collateral data. |
| 2026-07-21 | **Citizens policy-count scope trap (self-caught):** Citizens' book is ~98% personal, so a TOTAL mislabeled "personal-lines" survives every magnitude sanity check. The primary policies-in-force detail reports split personal/commercial — always pull those, never press paraphrases, for the count. Canonical vintage now Jun-30-26: 278,246 / 273,684 / 4,562. Full rule → LESSONS. |
| 2026-07-21 | **`scripts/boot.py` price rail needs the repo venv** — fetch.py imports yfinance which lives in `.venv/`, not system python; boot.py now auto-selects `.venv/bin/python3`. If prices fail at boot again, check interpreter first. |
| 2026-07-21 | **NHC product hierarchy:** the Tropical Weather Outlook (MIATWOAT) omits track/intensity — a named storm's disposition MUST come from the public advisory (MIATCPAT#). The outlook-based read on TS Bertha was materially wrong (45kt/no-track vs advisory 60mph/W-away-from-FL). Full rule → LESSONS. |
| 2026-07-21 | **Parcl MSI granularity:** the public motivated-sellers map is METRO-level all-seller MSI; the builder-specific cells (DRH/Toll/Pulte/Century) that seeded the tripwire come from a different Parcl product surfaced via WALTER/press. Don't silently swap granularities when grading the tripwire — document the basis. |

## Session Notes

⚠️ **Open question (unchanged, THE decision point):** At Q2 2026 FL bank earnings — now dated: BKU 7/22, VLY/SSB/AMTB/USCB 7/23 (gate day), SBCF 7/28 — does rate-shock classified CRE migrate to nonaccrual/charge-off, or cure? Pre-registered specs frozen in `workbook/FL_Forward_Log.md` + `FL_BANK_WATCHLIST.md`; grade as-written.

**CHANGES SINCE:** 7/21 EVE full live refresh (Will-directed) — all 10 pillars re-pulled; Citizens scope self-correction issued fleet-wide; Parcl MSI tripwire ARMED (sustain check ≥7/22); STATUS compacted 229→177 w/ archive. Prior: 7/21 AM employment pre-reg grade (benign branch); 7/17 ATTOM H1 + HOMER one-figure lock; 7/9 double catch-up.

**LAST SESSION (2026-07-21 EVE):** see `SCRATCH.md` (canonical handoff — boot intake ×6, 4 research lanes, 14 surfaces refreshed, commits `7b47aca5`/`6e803162`+closeout).

**NEXT SESSION:** graded prints week — 7/22 BKU + MSI sustain check; 7/23 gate-day cluster; 7/28-29 SBCF/Ocala/Amendment-3 hearing. Then: CCBG primary re-pull, HO-premium level reconcile.

**Mail state:** root inbox 0; WALTER lane 0 (drained 7/21); outbox 2 delivered (MARCO/AEOLUS corrections).
