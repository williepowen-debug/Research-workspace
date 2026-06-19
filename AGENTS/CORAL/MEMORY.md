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
- Spinout record: `archive/CORAL_SPINOUT_2026-06-19.md`
- SSB thesis: `research/SSB_THESIS.md`

---

## Findings (added 2026-06-19 refresh)

| Date | Finding |
|------|---------|
| 2026-06-19 | **The FL thesis is SPLIT, and the split is the whole point.** The household/condo leg confirms hard (FL #1 foreclosure, REOs +108% YoY, condo −6.1%, 92% of markets down, assessments live). The *bank* leg does NOT (SSB/SBCF/BKU/VLY Q1 NCOs 9-14bps, stable credit). Don't conflate "Florida real estate is stressed" with "FL banks are about to take losses" — Q1 2026 says the banks are absorbing it. |
| 2026-06-19 | **"Rate-shock reclass ≠ loss content" is the bank-leg crux.** SSB's classified CRE ($2.5B) is loans underwritten at 3% rate-shock now stressed by the 5% move — but 56% wtd-avg LTV and 98% current. Until LTVs break or payments stop, classified-CRE growth is a reclassification artifact, not realized loss. Q2 earnings test: does it migrate to nonaccrual/charge-off, or cure? |
| 2026-06-19 | **Insurance channel went the OTHER way.** Original thesis treated FL insurance as a hardening amplifier; in 2026 it's easing — Citizens depopulated to 294K (−64% YoY) + 8.8% rate cut, reinsurance −15-20% at 6/1. A hurricane landfall is the only near-term reversal risk. |
| 2026-06-19 | **CORAL and MARCO independently converged** on "acute FL stress delayed to winter 2026-27." Shared condo-inventory metric matches exactly (8.9mo statewide, Miami-Dade 12.9mo) — MARCO is the live owner; CORAL references. |

## Session Notes

⚠️ **Open question:** At Q2 2026 FL bank earnings (~late Jul), does the rate-shock classified CRE (esp. SSB's $2.5B, SBCF's 2 commercial credits) migrate to nonaccrual/charge-off, or cure? That single question decides whether the bank-loss leg ever arrives.

**CHANGES SINCE:** (next boot populates)

**LAST SESSION (2026-06-19 — promotion + first data refresh):**
- **Promotion (earlier today):** CORAL → top-level peer agent (`AGENTS/CORAL/`), git mv + peer infra, parent refs updated. (3 commits, pushed.)
- **Data refresh (this session):** full live pull via web research subagents + verification. Rewrote STATUS.md (🔴 RED → 🟠 ELEVATED, thesis-split framing), wrote `research/REFRESH_2026-06-19.md` (all sourced), added 6 KB rows (ML-CORAL-008..013), rebuilt CALENDAR.md.
- **Resolved Mar-3 open question:** the "RED cascade extending / short SSB" framing is superseded — household distress real, bank transmission absent, SSB short broken (Q1), $90P expired worthless.
- Live levels captured: KRE $71.61 (6/18), SSB ~$93 (6/17), BKU $46.88 (6/17), VLY ~$14.34 (6/11), SBCF mktcap $3.17B (6/12). *(No venv/yfinance in cloud container — prices via web, not market.py.)*

**NEXT SESSION:**
1. **Q2 2026 FL bank earnings (~late Jul)** — the bank-leg re-test (see Open question). Pull SSB classified trend, SBCF 2-credit status, VLY criticized direction.
2. **Resolve 2026 condo legislation** — did the session amend/delay SIRS reserve mandate? (NOT FOUND this pull.)
3. **Refresh Fannie blacklist count** — 1,400+ figure is Mar-2025; get current.
4. **Send the cross-agent signals** — draft REGINALD (FL banks stable, SSB retired, foreclosure accelerating) + MARCO (convergence confirmed) + CARL (assessment cash drain) into `outbox/`.
5. **MARCO reconciliation handshake** — lock MARCO as live owner of shared condo-inventory metric.

**Mail state:** 1 pending inbox signal (2026-03-04 BayFirst SBA exit, from REGINALD) — still unprocessed (stale, pre-dates refresh); outbox empty (signals queued for next session per item 4).
