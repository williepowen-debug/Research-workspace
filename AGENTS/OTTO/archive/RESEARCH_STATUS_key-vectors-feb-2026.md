# RESEARCH_STATUS — retired section (verbatim, moved 2026-10-14, s029)

Sessions 006–007 (Feb 2026) vector tables. The VX registry is FROZEN (`workbook/VX.tsv`); live vector state is STATUS § CONVERGENCE MATRIX.

## KEY VECTORS ADDED/UPDATED THIS SESSION

### Session 006 (Carvana)
| VX-ID | Name | Status |
|-------|------|--------|
| VX-OTTO-060 | Carvana Related-Party Risk | 🟠 ORANGE |
| VX-OTTO-061 | Bridgecrest Portfolio | 🔴 RED |
| VX-OTTO-062 | Carvana Non-Prime ABS | 🟠 ORANGE |
| VX-OTTO-063 | Bridgecrest Repo Rate | 🔴 RED |
| VX-OTTO-064 | Carvana DQ Masking | 🔴 RED |
| VX-OTTO-065 | Garcia Insider Sales | 🔴 RED |
| VX-OTTO-066 | Carvana Discovery Order | 🟠 ORANGE |
| VX-OTTO-067 | Grant Thornton Conflict | 🟠 ORANGE |
| VX-OTTO-068 | Carvana S&P 500 Status | 🟡 YELLOW |

### Session 007 (Feb 2026 Sector Update)
| VX-ID | Name | Status | Change |
|-------|------|--------|--------|
| VX-OTTO-003 | Bank Losses | 🔴 RED | Updated ($1.8B+ total) |
| VX-OTTO-008 | Flagship Credit | 🟡 YELLOW | ⬇️ DOWNGRADED from RED |
| VX-OTTO-010 | CPS | 🟠 ORANGE | Updated ($900M FF, 19.75% ECNL) |
| VX-OTTO-016 | First Brands Wind-Down | 🔴 RED | ⬆️ ESCALATED (Ch. 7 risk) |
| VX-OTTO-024 | Tricolor Criminal | 🟠 ORANGE | Updated (Chu extraction) |
| VX-OTTO-025 | PrimaLend Restructuring | 🟠 ORANGE | ⬆️ UPGRADED (fraud angle) |
| VX-OTTO-069 | S&P Immigration Risk | 🟠 ORANGE | NEW |
| VX-OTTO-070 | Fed 2026 Stress Test | 🟡 YELLOW | NEW |
| VX-OTTO-071 | First Brands OEM Dependency | 🔴 RED | NEW |
| VX-OTTO-072 | PrimaLend BVY2 Fraud | 🟠 ORANGE | NEW |
| VX-OTTO-073 | First Help Financial (FHF) | 🟠 ORANGE | NEW |
| VX-OTTO-074 | Westlake Financial | 🟡 YELLOW | NEW |
| VX-OTTO-075 | Ally Financial | 🟡 YELLOW | NEW |

---

# RESEARCH QUEUE as it stood before the 2026-10-14 rebuild (verbatim)

## RESEARCH QUEUE

> ⛔ **REBUILT 2026-09-02. The table below had `CRITICAL — Carvana Feb 18 earnings` at the top on 2026-09-02 — a research item SIX AND A HALF MONTHS past, presented as the desk's top live priority, alongside a First Brands examiner report dated Feb 25 in a case that converted to Chapter 7 on Aug 24.**
> 🔑 **The instructive part: `STALE_PUNCHLIST` item ③ deleted this file's ACTIVE MONITORING table in s016 for exactly this disease — *"rotted into present-tense misinformation"* — and the RESEARCH QUEUE directly beneath it, carrying the same rot, survived that pass untouched.** A fix pass that deletes one table and leaves its twin is the correction-pass failure mode. Found by BROCK's heading test: *read every heading that implies currency*, because a stale queue carries no wrong token and no string sweep can see it. `[[finding_a_correction_pass_is_unreviewed_work]]`

| Priority | Topic | Rationale |
|----------|-------|-----------|
| **CRITICAL** | **Counts 7-8 exhaustive securitization list** (Tricolor criminal, owed ~2026-08-28 under the 8/14 bill-of-particulars ruling) | **UNVERIFIED.** Names the securitizations the government is charging = a direct read on the double-pledging perimeter. Highest-value unclaimed document on the criminal track |
| **HIGH** | **ENTRY of the First Brands conversion order** (`docket_id:71483359`) | OTTO-32's resolver at 97%. Dkt 3722 filed 8/27; entry UNVERIFIED. PacerMonitor's "Chapter 7" header is INFERRED, not verification |
| **HIGH** | **OTTO-10 new/used perimeter** — gate fires 2026-09-20 | Blocked on an instrument: Experian's Q1-2026 pair is chart-image locked and NOT primary-confirmable; only Q4-2025 is verified |
| MEDIUM | Kollar / Seibold plea transcripts (unsealing ordered 7/30) | Highest-yield unclaimed Tricolor document; may name corporate counterparties (OTTO-33) |
| MEDIUM | Re-key `panel_10d.py` upsert to `(deal, collection_period)` | Closes the 10-D/A vintage hole; base rate ZERO across ~800 filings, so owed at the ~Oct 1 cycle, not urgent |
| LOW | `EDGAR_8K_MONITOR` watch-window refresh + first FLG check | Windows are Apr-2026 vintage, marked `[STALE]` |
| ⛔ RETIRED | ~~Carvana Feb 18 earnings~~ · ~~First Brands examiner report (Feb 25)~~ · ~~Flagship Credit audit findings~~ | All three are past-dated records, not forward research. Removed rather than re-dated |
| ⛔ DEAD LEAD | ~~Rule 2004 counting across BDCs~~ · ~~DriveTime FOIA~~ · ~~TBK syndicate roster~~ | **Instrument gaps, not effort gaps** — Rule 2004 needs PACER (neither OTTO nor BROCK has it). Recorded so they do not age into "checked, nothing found" |
| ~~HIGH~~ ✅ **CLOSED 2026-08-27** | Bridgecrest servicing comparison | ~~Validate 0.117% fee as below-market~~ — **DONE, and it refuted OTTO's own restatement.** `[CONF SEC 424B5 ×3]` BLAST 2024-1 **3.50%/yr** vs SDART **3.00%** / Drive **4.00%** ⇒ **at market at the ABS level.** The 0.117% is Gotham's `[EST]` on the **third-party whole-loan** perimeter, which OTTO had widened to the $26B portfolio. Whole-loan rates are private agreements — **that perimeter is not reachable from public filings.** → `thesis/THESIS.md` v1.5 |

---
