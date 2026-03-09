# CARL Migration Plan
**Created:** 2026-03-10
**Status:** READY TO EXECUTE

---

## Overview

Migrate CARL to HAWK/ZHAO gold standard. CARL is roughly where ZHAO was pre-migration: oversized STATUS, old-format TSVs, no KB, heavy inbox backlog. Key difference: 69 VX rows (largest in network), 5 sub-agents (LEAVE ALONE), and a TRADE.md that exists but predates the template.

**Estimated effort:** 2 sessions (one for Prome structural work, one for CARL spawn)

---

## Phase 1: STATUS.md Rewrite (Prome, manual)

**Current:** 311 lines. Missing: Convergence Matrix, Exit Rules, Bottom Line.

**Archive to `domain/sources/STATUS_archive_20260310.md`:**
- Athene/APO thesis section (~40 lines) — keep 3-line summary, detail → archive
- CVNA fraud watch (~20 lines) — move to `domain/sources/CVNA_FRAUD_WATCH.md`
- Private credit cascade section (~15 lines) — compress to 3 lines, detail in archive
- Check-in notes from header — strip, archive

**Archive to `archive/`:**
- `CHECKIN_MAR6.md` → `archive/`
- `INBOX.md` → `archive/` (legacy, replaced by mail system)

**Add missing sections:**
- **Convergence Matrix** — score CARL's ~10 key vectors on 5-point scale. Candidates:
  1. CC 90+ DQ (4 — 92% of GFC)
  2. Subprime Auto ABS 60+ (5 — THRESHOLD BREACHED 7.1%)
  3. Fannie MF DQ (4 — 6bps from GFC)
  4. Student Loan 90+ (4 — 0.4pp from 10%)
  5. Gas Price Squeeze (4 — Brent $90, pump lag Mar 20)
  6. UI Exhaustion Wave (3 — Mar 24 first wave, not yet hitting)
  7. FL Triple Squeeze (4 — energy + HOA + insurance)
  8. Reverse Wealth Effect (3 — materializing, 6-8 week lag)
  9. K-Shape Widening (4 — Wendy's -11.3% vs McDonald's +6.8%)
  10. Foreclosure Acceleration (3 — +41% YoY, target 70K/qtr)

- **Exit Rules:**
  - Thesis kill: Claims sustained <220K for 8+ weeks AND CC 90+ DQ declines 2 consecutive quarters
  - K-shape closing: Subprime metrics improve for 2 consecutive quarters while aggregate worsens (survivorship bias clearing)
  - Position-specific: Fannie MF — exit if DQ reverses below 0.65% for 2 months
  - Time-based: Q1 consumer earnings (April) = mandatory review

- **Bottom Line:** 2-4 sentences

**Target:** ≤200 lines (CARL has dense data — allow slightly more than ZHAO's 152)

---

## Phase 2a: FLOW.tsv — VERIFY ONLY

Already 9-col HAWK standard (15 rows). Spot-check Current_Position values for staleness.

---

## Phase 2b: VX.tsv Migration (Prome, manual)

**Current:** 69 rows, 11-col OLD format (Vector_ID, Category, Confidence — no Green)
**Target:** 11-col HAWK standard (ID, Name, Current_Value, Status, Green, Yellow, Orange, Red, Last_Updated, Source, Notes)

**Changes:**
- Rename `Vector_ID` → `ID`
- Drop `Category` (encode in ID numbering or Notes)
- Drop `Confidence`
- Add `Green` column
- Update stale values from check-ins and inbox signals:
  - NFP -92K (unemployment 4.4%)
  - Brent $90 (was $84)
  - Subprime Auto 7.1% (was 6.9% in some rows — CRL-02 may be CONFIRMED)
  - Gas price estimate for Mar 20
  - Any new data from 9 inbox signals

**⚠️ 69 rows is a LOT.** Consider chunking: do 1.xx (credit) first, then 2.xx (housing), etc. Or do the column remap mechanically for all rows, then update stale values in a second pass.

---

## Phase 2c: ML.tsv → KB.tsv (Prome or spawn)

**Current:** 66 rows, 9-col old format
**Target:** 13-col KB standard (add Conf, Epistemic, Status, Stale_By, DerivedFrom)

Same mechanical migration as ZHAO. Check for duplicate IDs. Assign Admiralty codes based on source quality. Add new KB entries for data from inbox signals.

**Note:** CARL's ML entries include ABS infrastructure setup (ML-CARL-ABS-001/002) and research synthesis docs (ML-CARL-01 through 06). These are more meta/framework entries than factual claims — assign appropriate Epistemic tags.

---

## Phase 2d: PREDICTIONS.tsv

**Current:** 2 rows, no Invalidation column
**Target:** Add Invalidation + expand from STATUS inline predictions

Predictions to add from STATUS:
- CRL-02: May already be CONFIRMED (subprime auto 7.1% > 7.0%)
- Fannie MF DQ >0.80% (90% conf, Q2)
- Student 90+ >10% (88% conf, Q1)
- CC 90+ >13.74% GFC (75% conf, Q2)
- Foreclosures >70K/qtr (Q2 target)
- FL UI exhaustion → DQ spike May 2026

---

## Phase 2e: SCHEMA.tsv + CLAUDE.md

- Copy `AGENTS/templates/SCHEMA.tsv` to `CARL/workbook/`
- Rewrite CLAUDE.md to template standard:
  - Add spawn protocol with KB/VX/FLOW logging steps
  - Add mail/PROTOCOL.md pointer (remove inline inbox instructions)
  - Add workbook section with column schemas
  - Add TRADE.md reference
  - Add Korea/KOSPI to domain scope? (probably not — leave with ZHAO)

---

## Phase 2f: TRADE.md Update

**Current:** 123 lines, Feb 14 vintage. Pre-template format. Watchlist-style with checkboxes.
**Target:** Template format (Active Recommendations table, Domain Catalysts, Cross-Agent Dependencies, Rejected/Exited)

Key updates needed:
- CRL-02 CONFIRMED (subprime auto 7.1%) — should this upgrade any watchlist items?
- NFP -92K arrived — several entry triggers may now be checked
- Brent $90 — gas squeeze confirmed base case
- Add fertilizer/food CPI second-order trade idea
- CVNA fraud thesis → active or still watching?

---

## Phase 3: Inbox Processing (Spawn CARL)

**9 signals waiting:**

| Signal | From | Key Data | Pre-integrated? |
|--------|------|----------|-----------------|
| Feb 24 batch 1 | Prome | 6%+ rate mortgages 21.2%, Wright data | Partially in STATUS |
| Feb 24 batch 2 | Prome | Student loan 90+ by age vertical spike | Partially in STATUS |
| Mar 4 Mexico remittances | MARCO | -1.4% YoY, first Jan decline since 2015 | NOT in STATUS |
| Mar 4 Korea KOSPI | SAM | KOSPI -12%, EM credit contagion | NOT in STATUS (low CARL relevance?) |
| Mar 6 NFP broadcast | ALL | NFP -92K, federal -10K, UE 4.4% | Partially in STATUS header |
| Mar 6 Brent $90 | HAWK | Gas surge Mar 20, storage crisis, dual shock | Partially in STATUS |
| Mar 6 NFP consumer timeline | HAWK | Accelerate DANGER WINDOW, CC DQ watch now | Partially in STATUS |
| Mar 8 fertilizer shock | HAWK | 13% global fertilizer from Gulf, food CPI 6-12 weeks | NOT in STATUS |
| Mar 9 diesel + Vegas housing | Prome | ULSD parabolic, Las Vegas 19% cancellation | NOT in STATUS |

**Pre-move candidates (already integrated):** Feb 24 batches and NFP broadcast are partially reflected in STATUS. Could move to processed before spawn to reduce noise — but let CARL decide what's new vs. stale. Better to let the agent process all 9 fresh.

**Key spawn task beyond inbox:** Model the fertilizer → food CPI → consumer stress second-order chain (FLOW candidate).

---

## Phase 4: Housekeeping

- Move `CHECKIN_MAR6.md` → `archive/`
- Move `INBOX.md` → `archive/`
- Verify `domain/sources/` has the STATUS archive
- Git commit + push

---

## Execution Order (Recommended)

**Session 1 (Prome):**
1. Phase 4 housekeeping (quick)
2. Phase 1 STATUS.md rewrite
3. Phase 2a FLOW verify
4. Phase 2e SCHEMA.tsv copy
5. Phase 2b VX.tsv migration (heavy — may need to chunk)

**Session 2 (Prome + Spawn):**
1. Phase 2c KB.tsv migration
2. Phase 2d PREDICTIONS.tsv
3. Phase 2f TRADE.md update
4. Phase 2e CLAUDE.md rewrite
5. Pre-spawn audit (same as ZHAO — trace spawn path, fix issues)
6. Phase 3 CARL spawn for inbox processing

---

## Success Criteria

- [ ] STATUS.md ≤250 lines with Convergence Matrix, Exit Rules, Bottom Line
- [ ] VX.tsv 11-col HAWK standard, stale values updated
- [ ] FLOW.tsv verified
- [ ] KB.tsv 13-col, migrated from ML.tsv
- [ ] PREDICTIONS.tsv with Invalidation column, 6-8 rows
- [ ] SCHEMA.tsv present
- [ ] CLAUDE.md template standard
- [ ] TRADE.md template format
- [ ] Inbox cleared (9 signals processed)
- [ ] CHECKIN_MAR6.md and INBOX.md archived
- [ ] All files consistent (no broken refs, no stale values contradicting across files)
