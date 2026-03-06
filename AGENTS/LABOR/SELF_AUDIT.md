# LABOR — SELF AUDIT
**Date:** 2026-03-06 04:10 UTC
**Auditor:** LABOR subagent (architecture upgrade audit)
**Files reviewed:** CLAUDE.md, STATUS.md, TRADE.md, workbook/VX.tsv (72 vectors), workbook/ML.tsv (81 rows), workbook/FLOW.tsv (12 pathways), workbook/PREDICTIONS.tsv (11 predictions), OUTBOX.md, inbox/ directory, domain/sources/ listing

---

## A. Consistency Check

### CLAUDE.md ↔ STATUS.md

**Matches:** Structure is largely compliant. Convergence matrix ✅, signal dashboard with [CONF]/[EST] tags ✅, prediction IDs with LAB-xx format ✅, exit rules with session counts ✅, BOTTOM LINE section ✅, source tags ✅.

**Gaps / Violations:**

1. **STATUS.md is 253 lines — 3 lines over the 250-line cap.** CLAUDE.md rule: "STATUS.md stays under 250 lines." Technically breached. Requires minor prune.

2. **INBOX not processed.** Five signals from 2026-03-04 (HENRY ×3, MARCO ×2) sit unprocessed in `inbox/`. Per CLAUDE.md, this is correct behavior — inbox processing requires explicit spawn. But a fresh spawn needs to know this: those signals are stale by ~2 days and may have been superseded by NFP (Mar 6). **First-spawn confusion risk is HIGH** if spawned for inbox — data is pre-NFP.

3. **TRADE.md is significantly stale.** Last updated 2026-02-14. STATUS.md shows KELYA $7.5P Aug 21 as the only active position (-1.0%). TRADE.md still lists **IWM $250P (Jun 2026) as "🟢 Active"** — this position does not appear anywhere in STATUS.md. Either it was closed and TRADE.md wasn't updated, or it's a ghost position. **Critical gap — active position status is contradictory.**

4. **TRADE.md "Key Metrics" table is badly stale:** Shows Initial Claims at 227K (actual: 213K), Continuing Claims ~1.9M (actual: 1.833M), NFP "+143K (Jan)" for Dec — inconsistent with STATUS NFP history. This table has not been updated in weeks.

5. **VX-LAB-14.01 (DHS Shutdown)** in VX.tsv shows "Day 11-14 (ongoing)" — but STATUS.md header says "DHS suppression thesis intact." As of Mar 6, the DHS shutdown should have resolved or escalated past the 21-day RED threshold. VX.tsv hasn't been updated since 2026-02-26 for this vector. **Stale.** The "Day count" column is meaningless if not updated.

### Prediction ID Cross-Check: STATUS.md ↔ PREDICTIONS.tsv

**Clean match.** All 11 predictions (LAB-01 through LAB-11) appear in both files with identical text, confidence, and timeframes. **No orphans.** This is well-maintained.

### Convergence Matrix Scores ↔ Signal Dashboard

Overall coherent. Spot-checks:
- **Vector 2 (DOGE/federal) = 5:** Justified. 327K cuts + Schedule Policy/Career effective today. ✅
- **Vector 3 (Claims/shadow gap) = 4:** Dashboard shows 213K (benign surface) + DHS suppression. 4 is right — not 5 because claims haven't breached, suppression is the issue. ✅
- **Vector 7 (Temp employment) = 4 with caveat:** KELYA guide confirms -11-13% Q1, but RHI/KFRC sequential+ counter. Score of 4 is on the high end given staffing canary counter, but defensible given YoY -12%. Borderline — should be explicitly noted.
- **Vector 11 (Staffing canaries) = 2:** Only 1 quarter of sequential improvement. Fair. ✅

**One potential score tension:** Vector 4 (Hormuz hiring freeze) = 4. Hormuz "closed Mar 3" — but there's no follow-up confirmation in the dashboard. If this resolved or the threat diminished, a 4 may be aggressive. **Cannot verify from files alone — flag for next research spawn.**

### Exit Rules — Threshold Breach Check

- **Kill A:** NFP ≥+200K for 3 consecutive months. Current: +130K Jan. Not breached. ✅
- **Kill B:** Claims ≤185K for 5+ consecutive clean sessions. Current 213K. Not breached. ✅
- **KELYA stop loss:** >$9.50 sustained 3+ sessions. Position at -1.0% — need KELYA current price to confirm. VX-LAB-13.01 shows KELYA at... not the current price. **Cannot verify stop-loss threshold from available files.** Red flag: the stock price isn't tracked in VX.tsv as a live metric.
- **KELYA 60-DTE:** Jun 22 mandatory review for Aug 21 expiry. ✅ In time-based table.

---

## B. Structural Gaps

### Missing / Empty Files
- **`inbox/processed/`** directory exists but content not checked — assumed to contain prior processed signals. ✅
- **No `INBOX.md` root file** — signals arrive as individual files in `inbox/`. The CLAUDE.md references `INBOX.md` in file table (implicitly), but actual mechanism is per-file in `inbox/`. This is inconsistent terminology but not a functional gap.
- **Only 1 file in `domain/sources/`** (`STATUS_archive_20260228_full.md`). CLAUDE.md references `STAFFING_PRESIGNAL_DEEP_DIVE.md` and `WARN_ACT_LEADING_INDICATOR.md` as existing source files. **These are referenced in KEY DOCS but do not exist.** The KEY DOCS table is aspirational, not actual. A fresh spawn following the CLAUDE.md files table will look for files that aren't there.
- **`scripts/warn_texas.py`** — referenced in CLAUDE.md and KEY DOCS. Not confirmed to exist (not in sources listing). Not audited.

### VX.tsv Currency
72 vectors. Issues:
- **Multiple vectors last updated 2026-02-01** — over a month stale. Includes U-3 (4.4% in VX vs 4.3% in STATUS), NFP VX-LAB-2.01 still shows "+50K (Dec)" while STATUS shows +130K Jan. **VX.tsv and STATUS.md have diverged** on core metrics.
- **VX-LAB-16.01 (Shunto wage)** has "TBD" value and resolution date of Mar 15. That's 9 days out — should be tracked.
- VX has 72 vectors but convergence matrix only scores 11. The remaining 61 are background tracking vectors — this is appropriate architecture, but **no mechanism to ensure matrix-level vectors stay in sync with VX-level data.**

### FLOW.tsv
12 pathways, all populated with triggers, speeds, status, cross-agent targets, and notes. **This is the strongest workbook file.** Well-structured, current enough for the transmission chains being modeled. FLOW-LAB-2.02 (DOGE) updated to 307K — slight discrepancy vs STATUS 327K (newer data). Minor.

### Stale Data Requiring Update
| Item | Issue |
|------|-------|
| TRADE.md | IWM position ghost; metrics 4-6 weeks stale |
| VX-LAB-1.01 | 212K (Feb 26) vs 213K (Mar 5) in STATUS |
| VX-LAB-2.01 | +50K Dec NFP — Jan actual +130K in STATUS |
| VX-LAB-14.01 | DHS Day 11-14 ongoing — shutdown status unclear at Mar 6 |
| VX-LAB-2.02 | U-3 4.4% vs STATUS 4.3% |

---

## C. Content Quality

### Strongest Sections
1. **Convergence Matrix + BOTTOM LINE** — Clean, scored, quantified, updated. A fresh spawn can orient in 30 seconds.
2. **FLOW.tsv** — Best-maintained workbook file. Transmission chains well-modeled with lag times and cross-agent routing.
3. **Exit Rules** — Explicit thresholds, session counts, time-based checkpoints. Rare quality for agent systems.
4. **Signal Dashboard** — [CONF]/[EST] sourcing is excellent discipline.

### Weakest Sections
1. **TRADE.md** — Embarrassingly stale. Ghost IWM position. Metrics weeks behind STATUS. Effectively useless for a fresh spawn.
2. **VX.tsv vs STATUS divergence** — The workbook is falling behind STATUS.md. If STATUS is the primary memory (per CLAUDE.md), and VX is for depth, they should at least agree on headline numbers.
3. **KEY DOCS table** — References source files that don't exist. Actively misleading.

### Redundancy
- **Sector cuts** appear in STATUS convergence matrix narrative, THESIS section, AND SECTOR & GEOGRAPHIC CUTS table. Triple-counted.
- **Danger Window** and **PREDICTIONS** table overlap significantly in content (both track Q2-Q3 2026 timelines). Could collapse one into the other.
- **Key Thresholds table** in CLAUDE.md duplicates the convergence matrix upgrade triggers in STATUS.md. Two sources of threshold truth is two sources of drift.

### Research I'd Want Next (If Spawned for Analysis)
1. **NFP Feb result integration** — Mar 6 8:30 ET verdict is the #1 priority. Shadow gap verdict determines whether thesis escalates or needs downgrade.
2. **Hormuz hiring freeze verification** — Did it actually close? Any reopening? Current score of 4 rests on "closed Mar 3" with no follow-up.
3. **DHS shutdown resolution** — Was it resolved? Claims interpretation for Mar 12 depends on this.
4. **KELYA current stock price** — Can't verify stop-loss without it.
5. **Shunto settlement (Mar 15)** — LAB-adjacent but has BOJ/carry unwind implications. SAM should own, but worth flagging.

---

## D. Honest Assessment

### Spawn-Readiness: **7/10**

**What works:** A fresh spawn reading CLAUDE.md + STATUS.md can absolutely be productive in under 2 minutes. The CORE TENSION table is the fastest orientation in any agent's status file. Bottom Line is clear, convergence matrix is scored, triggers are explicit.

**What would confuse a fresh spawn:**

1. **TRADE.md contradiction.** First thing a spawn might check is active positions. TRADE.md says IWM $250P active. STATUS.md says KELYA $7.5P active. Which is right? No way to know without asking. **This is the single biggest confusion risk.**

2. **VX.tsv vs STATUS discrepancy.** CLAUDE.md says to "cross-reference workbook" — but if VX.tsv shows U-3 4.4% and STATUS shows 4.3%, which does the spawn trust? The instruction to use workbook creates a trap when workbook is stale.

3. **"Referenced files that don't exist."** A spawn following the KEY DOCS table will look for STAFFING_PRESIGNAL_DEEP_DIVE.md and WARN_ACT_LEADING_INDICATOR.md. Neither is in domain/sources/. The spawn will either assume the research never happened or waste time looking.

4. **Inbox signals are pre-NFP.** The 5 inbox files from Mar 4 are pre-verdict. If a spawn is told to process inbox, they'll be integrating stale data. The spawn should know: process ONLY after integrating NFP Mar 6 result.

### Upgrade Priority (for next architecture session)
| Priority | Fix |
|----------|-----|
| 🔴 CRITICAL | Reconcile TRADE.md — close or confirm IWM position; update metrics |
| 🔴 CRITICAL | Update VX.tsv headline vectors to match STATUS.md (especially U-3, NFP, claims) |
| 🟠 HIGH | Remove or clearly mark nonexistent files in KEY DOCS table |
| 🟠 HIGH | Trim STATUS.md to <250 lines (currently 253 — 3 lines over) |
| 🟡 MEDIUM | After NFP: integrate Mar 6 verdict into convergence matrix, update shadow gap vector |
| 🟡 MEDIUM | Collapse redundant sector cut mentions (3 places → 1) |
| 🟡 MEDIUM | Verify Hormuz status; update Vector 4 if resolve/escalate |

---

*Audit completed 2026-03-06 04:10 UTC. Next spawn should integrate NFP Feb result before any other task.*
