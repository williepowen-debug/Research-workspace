# CARL ACTION PLAN
**Created:** 2026-03-27 | **Status:** ACTIVE

---

## PRIORITY 1 — TIME-SENSITIVE (This week)

### 1.1 Claims Data (Mar 27)
- **What:** Pull Mar 27 weekly claims print. First post-Mullin data point.
- **Why:** If DHS suppression ends and claims gap to 230K+, narrative shock accelerates behavioral contagion. Update VX-CARL-CLAIMS-01.
- **Output:** KB entry + VX update if threshold breached.

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

### 2.1 Stale KB Entries (Past Stale_By Date)
| KB ID | Topic | Last Data | Stale Since | Refresh Source |
|-------|-------|-----------|-------------|----------------|
| KB-003 | Existing Home Sales | Jan 2026 NAR | 2026-03-15 | NAR Feb/Mar release |
| KB-004 | South FL Housing | Dec 2025 Redfin | 2026-03-15 | Redfin latest |
| KB-005 | Price Declines | Feb 2026 Wright | 2026-03-15 | Wright Substack |
| KB-006 | Insider Selling | Jan 2026 | 2026-03-15 | Washington Service |
| KB-026 | MF DQ GFC | Mar 4 Fannie | 2026-04-15 | Fannie Q1 data |
| KB-038 | Inventory Surge | Feb 2026 ResiClub | 2026-04-15 | ResiClub/Lance Lambert |

### 2.2 Approaching Stale (2-3 weeks)
- KB-070: Payment network selloff (Feb 23 market data)
- KB-072: KOSPI/EM contagion (Mar 4)
- KB-077: ULSD/LV housing (Mar 2026 pricing)
- KB-075: Danger window assessment (Mar 6, pre-gas-$4)
- KB-081: GDPNow collapse (Mar 8)

---

## PRIORITY 3 — HOUSEKEEPING (Next 2-3 sessions)

### 3.1 VX Consolidation
- **Merge VX-CARL-1.01 / VX-CARL-6.01** (duplicate CC 90+ DQ vectors). Keep 1.01, delete 6.01.
- **Merge VX-CARL-1.04 / VX-CARL-ABS-15** (duplicate subprime auto 60+ DQ). Keep 1.04, delete ABS-15.

### 3.2 Stale VX Refresh
- ~15 VX rows last updated 2026-01-22 (over 2 months). Pull current data or mark [STALE]:
  - VX-CARL-1.03, 1.05, 1.06, 1.07, 1.08, 1.09
  - VX-CARL-2.01 through 2.06
  - VX-CARL-3.01, 3.04
  - VX-CARL-4.01, 4.02, 4.03
  - VX-CARL-5.01 through 5.06

### 3.3 STATUS.md Cleanup
- Archive check-in blocks (Mar 25-26 narratives) to `domain/sources/STATUS_archive_20260327.md`
- Target: STATUS.md under 150 lines (currently ~200 with new danger window entries)
- Keep: dashboard tables, convergence matrix, predictions, danger window, cross-agent links

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
