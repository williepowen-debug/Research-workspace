# CARL ACTION PLAN
**Created:** 2026-03-27 | **Status:** ACTIVE

---

## PRIORITY 1 — TIME-SENSITIVE (This week)

### ~~1.1 Claims Data (Mar 27)~~ — DONE
Pulled Mar 27. Initial 210K, continuing 1,819K (lowest since May 2024). Counter-signal logged in KB-117 + red_team/. VX-CARL-CLAIMS-01 updated to GREEN.

### 1.2 Gas $4.00 Documentation
- **What:** When AAA formally prints $4.00+ national avg, document as KB entry.
- **Why:** Behavioral breakpoint confirmed. Upgrade gas vector language in STATUS.md.
- **Output:** KB entry, STATUS update. Mechanical — no analysis needed.

### 1.3 USDA Mar 31 — Planting Intentions
- **What:** Monitor USDA Planting Intentions report. Assess impact of triple nitrogen seizure on 2026 crop outlook.
- **Why:** Urea at $683/mt (watch $800). All three nitrogen sources offline. This report sets the food CPI trajectory for Q3-Q4.
- **Output:** KB entry, update VX-CARL-FOOD-01/02, signal to HAWK if food CPI timeline changes.

---

## PRIORITY 2 — DATA REFRESH (Next 1-2 sessions)

### ~~2.1 Stale KB Entries (Past Stale_By Date)~~ — 5/6 DONE (Mar 27)
| KB ID | Topic | Status | Notes |
|-------|-------|--------|-------|
| ~~KB-003~~ | Existing Home Sales | DONE | Feb 4.09M SAAR (+1.7%), mild counter-signal |
| ~~KB-004~~ | South FL Housing | DONE | FL 83 days on market (+6 YoY) |
| ~~KB-005~~ | Price Declines | DONE | 47/50 cities declining — major escalation |
| ~~KB-006~~ | Insider Selling | DONE | Ratio 0.24 vs 0.34 median |
| **KB-026** | **MF DQ GFC** | **OPEN** | **Need Fannie Feb 2026 PDF for exact MF DQ rate** |
| ~~KB-038~~ | Inventory Surge | DONE | 66/200 metros above 2019 levels |

### 2.2 Approaching Stale (2-3 weeks)
- KB-070: Payment network selloff (Feb 23 market data)
- KB-072: KOSPI/EM contagion (Mar 4)
- KB-077: ULSD/LV housing (Mar 2026 pricing)
- KB-075: Danger window assessment (Mar 6, pre-gas-$4)
- KB-081: GDPNow collapse (Mar 8)

---

## PRIORITY 3 — HOUSEKEEPING (Next 2-3 sessions)

### ~~3.1 VX Consolidation~~ — DONE (Mar 27)
- ~~Merge VX-CARL-1.01 / VX-CARL-6.01~~ — consolidated, 6.01 marked CONSOLIDATED
- ~~Merge VX-CARL-1.04 / VX-CARL-ABS-15~~ — consolidated, ABS-15 marked CONSOLIDATED

### 3.2 Stale VX Refresh
- ~15 VX rows last updated 2026-01-22 (over 2 months). Pull current data or mark [STALE]:
  - VX-CARL-1.03, 1.05, 1.06, 1.07, 1.08, 1.09
  - VX-CARL-2.01 through 2.06
  - VX-CARL-3.01, 3.04
  - VX-CARL-4.01, 4.02, 4.03
  - VX-CARL-5.01 through 5.06

### ~~3.3 STATUS.md Cleanup~~ — DONE (Mar 27)
- ~~Archive check-in blocks~~ — archived to `domain/sources/STATUS_archive_20260327.md`
- ~~Target under 150 lines~~ — achieved 128 lines

### 3.4 ABS Baselines (12 PENDING vectors)
- VX-CARL-ABS-01 through ABS-07 (CC: Discover, Cap One payment rates, DQ, charge-off, vintage)
- VX-CARL-ABS-11 (Exeter auto 30+ DQ)
- VX-CARL-ABS-12 (Ally auto payment rate)
- VX-CARL-ABS-14 (ABS vs NY Fed divergence)
- **Decision needed:** Do a dedicated EDGAR pull session, or mark as DEFERRED with rationale?

---

## PRIORITY 4 — ANALYTICAL IMPROVEMENTS (Ongoing)

### 4.1 Counter-Evidence Tracking
- No bull case or disconfirming data currently tracked anywhere.
- Options: (a) Add a "COUNTER" column to KB.tsv, (b) Dedicated COUNTER_EVIDENCE.md file, (c) Section in STATUS.md.
- Purpose: guard against confirmation bias at 44/50 convergence score.

### 4.2 Convergence Score Calibration
- Current 44/50 is subjectively scored. Define what 25/50 or 30/50 would look like.
- Consider: what data would move individual vectors from RED back to ORANGE?

---

## CATALYSTS CALENDAR

| Date | Event | CARL Impact |
|------|-------|-------------|
| **Mar 27** | Weekly claims | Shadow gap normalization? |
| **Mar 31** | USDA Planting Intentions | Food CPI trajectory |
| **~Apr 1-5** | Gas $4.50 (est.) | Next behavioral breakpoint |
| **~Apr 10** | SYF March 8-K | Consumer credit bellwether |
| **Mid-Apr** | Q1 ABS trust reports | First hard DQ update since Feb |
| **Late Apr** | Q1 earnings (ALLY, CACC, SYF) | Consumer finance guidance |
| **Apr 26** | FL UI Wave 2 peak | Second exhaustion cohort |
| **Apr/May** | April CPI | First print with full oil shock + tariffs |
| **Jun 24** | FL Wave 1 UI exhaustion cliff | DQ spike follows 30-60 days |
| **Jul-Aug** | FL + national exhaustion peak | $800M-$930M/mo spending hole |
