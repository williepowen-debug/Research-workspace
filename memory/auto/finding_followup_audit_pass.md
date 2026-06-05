---
name: finding-followup-audit-pass
description: "After executing a scoped cleanup ask, do a final end-to-end re-read of the touched file to catch adjacent staleness/conflicts not in the original scope"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 9f3a6359-35c9-4f29-8945-9ec052342b61
---

**Pattern (validated 2026-05-26 SAM TRACKER cleanup):**

When PROME or Will hands a scoped cleanup ask (e.g., "fix rule X, refresh section Y, replace banner Z"), execute the explicit scope first, then **do a final end-to-end re-read of the touched file before declaring done**. The highest-impact remaining issues often live *adjacent* to the requested scope — not in it.

**Concrete instance (SAM TRACKER 2026-05-26):**
- PROME ask: signal-routing rule fix + Channel 1 banner + key-dates refresh + Oct survey down-weight (5 items, executed cleanly in Pass 1)
- After Pass 1, Will asked "Do you see anything else we should change?" — prompted a final read
- Pass 2 caught 2 actively-wrong items NOT in PROME's scope: (a) Industry Aggregates table claimed "JGB 30Y 4.000% ✅ BREACHED" but STATUS already showed 3.931% retraced — cross-doc fact conflict; (b) "Apr 12 Hormuz blockade context" was v1.3-era framing now backwards (April trade SURPLUS not deficit; Brent collapsing) — obsolete mental model
- Without the follow-up audit, both would have shipped untouched

**Why it matters:**
- Scoped asks define what's *known broken*. The author of the ask hasn't necessarily audited the whole file for related staleness.
- A focused executor can produce clean delivery on the ask while leaving adjacent rot in place
- Cost of the follow-up audit: ~2 min re-read. Catch rate: high when the section under edit shares structure with adjacent sections (cross-doc fact conflicts, version-era framing drift)

**How to apply:**
After executing the explicit scope, before declaring done:
1. Re-read the touched file end-to-end
2. Rank candidates by **behavioral impact** (does this change what someone DOES?) — not line-count impact ([[finding_audit_prioritization]] discipline)
3. Surface only the top 2-3 to the requester; mention cosmetic issues briefly but don't pile on
4. Distinguish "actively wrong" (cross-doc conflicts, obsolete mental models) from "just stale" (old date stamps, superseded survey data) — actively wrong items deserve immediate fix; stale items deserve a note

**Transferability:** Apply to any scoped cleanup pass — CARL/REGINALD/BROCK/HENRY STATUS rehab, OZK plan refresh, FORGE trigger-set calibration. The pattern (focused execution + adjacent-audit step) generalizes across agents.

**Anti-pattern:** Treating the ask as a checklist. Execute → declare done → ship. Misses the adjacent rot.

Related: [[feedback_break_multifile_updates]] (chunking discipline), [[finding_walter_refactor_pattern]] (structural refactor recipe), audit-prioritization finding in SAM MEMORY.md.
