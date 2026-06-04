# KB.tsv AUDIT & REFERENCE MAP

**Purpose:** single source of truth for the KB.tsv prune/consolidation arc (multi-session). Holds the verified inbound-reference graph so no pass re-derives it or forgets a cross-link. **Read before touching KB.tsv.**

**Status:** 🔵 Active prune arc, opened 2026-06-03. Baseline: **136 data rows** (ML-HEN-001 → 136), dated 2026-01-26 → 2026-04-17.

---

## THE RULE

**NEVER archive a load-bearing ID without first re-pointing its inbound links** (KB Cross_Links/Vector_Links + VX/FLOW/PREDICTIONS + **LABOR/KB.tsv**). Leaf rows = judge on content. When **merging** within a theme, anchor on the **highest-ref ID** so inbound links survive.

**Reference corpus (what counts as an inbound link):** `HENRY/workbook/{KB,VX,FLOW}.tsv` + `HENRY/workbook/PREDICTIONS.tsv` + `LABOR/workbook/KB.tsv`. A full-tree grep (2026-06-03) confirmed LABOR is the **only** cross-agent referrer of HENRY ML-HEN IDs; HENRY archive/ + research/prompts/ also contain refs but are historical (not live consumers).

---

## VERIFICATION (2026-06-03)

Reference map originally built by Prome/3rd-party LLM; **independently reproduced by HENRY from raw files** — exact match on 38 load-bearing / 98 leaf, all hub counts, all mid/light IDs, and the three asterisk flags. **One correction:** Prome scanned HENRY-internal only and missed the cross-agent link → **ML-HEN-032 added as 39th protected ID** (referenced by `LABOR/KB-LAB-005`).

---

## PROTECTED SET (39 — re-point or keep, never blind-archive)

**Hubs (merge anchors, keep):**
`003` (8: VX5/FLOW3) · `089` (5: VX3/KB1/FLOW1) · `065` (5: KB) · `097` (3) · `093` (3) · `090` (3) · `077` (3: VX) · `073` (3: KB) · `059` (3: KB) · `058` (3: KB)

**Mid (2 inbound):** `134` · `132`\* · `096` · `092` · `086` · `085` · `082` · `050`

**Light (1 inbound):** `123` · `122` · `118`\* · `107` · `100` · `099` · `098` · `091` · `084` · `083` · `079` · `078` · `071` · `068` · `067`\* · `064` · `063` · `054` · `004` · `002`

**Cross-agent (LABOR inbound — HENRY-scan missed):** `032` (1: LABOR/KB-LAB-005)

\* *= also a status-flagged archive-candidate → MUST re-point before archiving:*
- `067` SUPERSEDED, inbound VX1 → re-point VX then archive (Pass 1)
- `132` RESOLVED, inbound FLOW1+VX1 → re-point both then archive (Pass 1)
- `118` NEW + live (PCE-prep framework) → **keep-live, not archive**

---

## PASS PLAN (chunked by era — staleness tracks date)

| Pass | Scope | ~Rows | Status |
|------|-------|-------|--------|
| **0** | Status-flagged-non-live AND leaf (safe 12) | 12 | ✅ done 6/3 (KB 136→124) |
| **1** | Jan 2026 — process/wrapper/resolved-PIT (14 archived, 17 kept) | 31 | ✅ done 6/3 (KB 124→110) |
| **1.5** | Re-point + archive held 067/132 | 2 | ✅ done 6/3 (KB 110→108) |
| **2** | Feb 2026 | 27 | pending |
| **3a** | Mar 1-12 | ~35 | pending |
| **3b** | Mar 13-31 | ~25 | pending |
| **4** | Apr 2026 | 13 | pending |

Per-row verdict taxonomy: **KEEP-LIVE** / **REFRESH** (update stale framing in place) / **ARCHIVE** (point-in-time telemetry → KB_ARCHIVE.tsv) / **MERGE** (anchor on highest-ref ID) / **recategorize** (collapse 34 categories → ~9, SAM precedent).

---

## PASS 0 — safe 12 (archived 2026-06-03)

All status-flagged-non-live by a prior HENRY AND leaf (0 inbound) AND referenced nowhere outside the mapped files. No content judgment, no re-pointing.

| ID | Status | Cat | Description |
|----|--------|-----|-------------|
| 006 | SUPERSEDED | SEN | Complacency divergence — VIX green / fundamentals red |
| 007 | DELIVERED | COMMS | Signal sent to CARL — household equity ATH |
| 008 | DELIVERED | COMMS | Signal sent to SAM — Japan 1989 parallels |
| 009 | DELIVERED | COMMS | Alert sent to SHARED_INTEL — CAPE >40 |
| 020 | SUPERSEDED | CON | Great Rotation 2026 |
| 037 | SUPERSEDED | GAM | Gamma domain established |
| 040 | SUPERSEDED | GAM | Regime assessment: fragile equilibrium |
| 046 | SUPERSEDED | BRD | Technical breadth deep dive |
| 060 | DUPLICATE | RETAIL | Retail flows $48B (dup of 058) |
| 061 | DUPLICATE | STRUCTURE | 115+ blowups (dup of 059) |
| 070 | SUPERSEDED | CREDIT | REGINALD HY OAS 335-355 cross-agent trigger |
| 076 | RESOLVED | MACRO | ADP/ISM Feb pending (Mar 4 releases) |

## PASS 1 — January (done 2026-06-03)

Session-001 "Loaded Machine" foundational rows. Framing evolved (→split-axis) but structural substrate persists → kept the durable facts, archived scaffolding/wrappers/resolved-point-in-time. All 14 archived = leaf (verified 0 inbound). 4 protected Jan IDs (002/003/004/032) all KEPT.

**Archived (14):** 001 010 011 (process/wrappers) · 016 (superseded by VX) · 017 026 034 (wrappers) · 019 (ZBT played-out) · 022 035 036 (resolved point-in-time) · 021 023 025 (Jan sentiment snapshots).
**Reusable bits salvaged before archive:** 021 3-pillar sentiment-reversal framework + 025 data-source cadence list → folded into `domain/REFERENCE_TABLES.md` (not pure-dropped).
**Kept (17):** 002🔒 003🔒 004🔒 005 012 013 014 015 018 024 027 028 029 030 031 032🔒 033 — durable substrate (concentration/0DTE/passive/private-credit/structural-bid/methodology). Some numbers stale → flagged for a later numbers-refresh pass. **031 kept this pass**, pending end-of-arc merge into 027.

## PASS 1.5 — held load-bearing rows re-pointed + archived (done 2026-06-03)

The 2 status-flagged rows held back from Pass-0 (load-bearing, so blind-archive would orphan links). Re-pointed inbound refs FIRST, then archived. KB 110→108.
- **067** SUPERSEDED (LIQUID HY-OAS 335-355 overestimate; actual 308 — lesson in LESSONS.md). Inbound `VX-HEN-20.01` → re-pointed.
- **132** RESOLVED (Apr-6 muddle-through squeeze narrative, played out; forward 300/340 framework persists in `FLOW-HEN-027`). Inbound `VX-HEN-16.01` + `FLOW-HEN-027` → re-pointed.
- **Re-point convention `[ARCH]`:** an archived ID referenced by a live VX/FLOW row is tagged `ML-HEN-NNN[ARCH]` — still findable in KB_ARCHIVE.tsv, flagged not-live. Apply this whenever a future pass archives a load-bearing ID.
