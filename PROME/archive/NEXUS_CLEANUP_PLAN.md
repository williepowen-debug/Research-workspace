# NEXUS Cleanup Plan — Mar 14, 2026

**Goal:** Trim NEXUS/STATUS.md from ~300 lines to ~150. Remove stale data, consolidate overlaps, add today's signals. Prepare for pre-FOMC synthesis spawn.

**Instructions:** Each pass is self-contained. Do the next unchecked pass, check it off, commit, then clear. Read this file at boot to see where you are.

---

## [x] Pass 1: Prune Stale Data (completed Mar 14 — also deleted T-01, T-02, T-05)
**Read:** `AGENTS/NEXUS/STATUS.md`
**Do:**
- Delete "CPI DECISION FRAMEWORK" section entirely (CPI already printed 2.4%)
- Delete Alert #6 ($85 WTI buy signal — oil back at $100+, resolved)
- Delete "PRIOR CRITICAL ALERTS — MAR 9" section (all upgraded into current alerts, redundant)
- Delete tensions T-01 and T-02 (both about $85 WTI, resolved)
- Save and commit

---

## [x] Pass 2: Fix Dates & Values (completed Mar 14)
**Read:** `AGENTS/NEXUS/STATUS.md` (shorter after Pass 1)
**Do:**
- Update threshold matrix:
  - Claims: 213K actual (Mar 13), buffer 22K to 235K YELLOW
  - Belgium TIC: Mar 18 release date (not Mar 15)
  - Kuwait: already curtailing since Mar 7 (not "8 days away")
  - USD/JPY: check current (was 158.5)
  - LIQ-01 HY OAS: check current (was 319bps)
  - Add: FOMC Mar 17, BOJ Mar 18-19, Taiwan LNG Mar 15, NFIB March ~Apr 8, OZK earnings Apr 16, TSMC earnings Apr 17, WAL earnings Apr 27
- Mark PROP-01 (TLT size up) and PROP-02 (roll credit puts) as IN-PROGRESS
- Update PROP-04: Kuwait already curtailing since Mar 7
- Update Alert #3 with HAWK Scenario D now 23% (was 18%)
- Update header/summary with current context
- Save and commit

---

## [x] Pass 3: Consolidate Convergence Matrix (completed Mar 14)
**Read:** `AGENTS/NEXUS/STATUS.md` — convergence matrix section only
**Do:**
- Merge C-07 (Four-Anchor UST) + C-20 (Japan Four-Vector) → **C-07 "UST Demand Destruction"** (all anchors: Gulf involuntary, Japan repatriation, Bessent 160 bilateral, trade balance)
- Merge C-02 (Private Credit) + C-22 (ABS/Structured Credit) → **C-02 "Private Credit Cascade"** (gates + ABS + warehouse lines + $300B bank exposure)
- Merge C-08 (LNG Structural) + C-14 (LNG-Credit Shared Root) → **C-08 "Energy-Credit Nexus"**
- Merge C-10 (Energy Warfare) + C-18 (Fertilizer/Food) → **C-10 "Energy Warfare → Supply Chain"**
- Archive C-01 (Q2 Consumer Stress, 95%) as confirmed baseline — one-line reference only
- Archive C-19 (Stagflation Trap, 93%) as confirmed — move to macro snapshot
- Merge Alert #5 (Japan Four Vectors) into Alert #1 (UST Demand Hole)
- Target: 22 entries → ~14
- Save and commit

---

## [x] Pass 4: Add New Signals + Update Narrative (completed Mar 14)
**Read:** `AGENTS/NEXUS/STATUS.md` + `memory/2026-03-14.md`
**Do:**
- Add "Signals — Mar 14" section:
  - GDP Q4 revised to 0.7% (from 1.4%). Fed spending -16.7%.
  - Core PCE 3.1% YoY, +0.4% MoM — reaccelerating. Pre-oil shock.
  - BOJ ¥399.8B foreign bond dump Mar 12. SAM: $5-7T total through FY-end (~$13-23B UST portion).
  - NFIB 11% poor sales (r=0.83 with unemployment). LAB-12: U-3 ≥5.0% Q3-Q4 60%.
  - Bloomberg: $300B bank private credit exposure. WFC $59.7B (2x next largest). BROCK: WFC on watchlist.
  - Insider behavior scan: OZK 🔴🔴 (CEO+CFO+CRO all selling), WAL 🔴 (CFO swap for JPM crisis banker). Full convergence with Memo Item 3.
  - Agent convergence: ALL agents independently confirmed transmission phase.
  - Bessent pulled from interview, returned shaken.
  - FT: US burned through "years" of munitions. Duration extends.
- Update Alert #1 with BOJ data + SAM $5-7T estimate
- Update Alert #4 (LIQ-01) if current HY OAS available
- Update Alert #7 (Credit Timing) — Will actively rolling today, mark in-progress
- Add Alert: Insider Behavior convergence (new research layer, corroborates balance sheet thesis)
- Rewrite Narrative Gap: "resilient economy" narrative died with GDP 0.7%. Last consensus pillar gone. Market pricing one cut in Sep — even that looks optimistic with Core PCE reaccelerating.
- Update header/summary
- Save and commit

---

## [ ] Pass 5: Spawn NEXUS
**Read:** `AGENTS/NEXUS/STATUS.md` (now clean and current)
**Do:**
- Quick scan — does it read coherently? Any obvious gaps?
- Spawn NEXUS with task: Pre-FOMC synthesis. Integrate all agent findings from Mar 14. Identify convergences, contradictions, and positioning recommendations ahead of FOMC Monday + BOJ Tuesday. Flag any threshold about to breach. Write to OUTBOX.
- Relay findings to Will.

---

## Reference: Today's Key Data Points
(For any pass that needs current values)
- GDP Q4: 0.7% (revised from 1.4%)
- Core PCE: 3.1% YoY, +0.4% MoM (Jan, pre-oil shock)
- Account: $55,363 (+176%)
- Brent: ~$100+
- HY OAS: ~319bps (check for update)
- USD/JPY: ~158.5 (check for update)
- Claims: 213K (Mar 13)
- HAWK scenarios: C=57%, D=23%, B=20%
- LABOR LAB-02: 80% (U-3 4.7% Q2)
- CARL: K-shape 5/5, 43/50
- HENRY: SPX EPS 10-20% too high
