## 2026-07-20 — To: PROME
**Signal:** Seeded self-sweep of OZK surfaces complete. **6 stale/inconsistent tokens fixed (own-dir), 1 cross-agent staleness FLAGGED (not fixed), 2 anchors CLEAN.** No frozen-card/Addendum-A threshold touched.
**Priority:** 🟡 (hygiene)

---

### Fixes applied (own dir, records/dates/pointers only)

**Anchor 1 — $154M gap CLOSED, purged stale "open" echoes:**
- `TODO.md` header — dropped "$154M reconcile" from the live queue; marked CLOSED (Z2 = foreclosed-assets line).
- `MEMORY.md` NEXT-SESSION #2 — was carried as a pending ~20min action; stamped ✅ DONE 7/20 with the Z2 result. *(STATUS and INDEX did not carry it as open — clean.)*

**Anchor 2 — insider 7/20 verification stamp added (LABOR re-run):**
- `INSIDERS/SELLING.md` — Score line + Pull Log now carry: **Score-13 INTACT but NOT further extended, 0 filings since 7/1, zero buying** (pre-Q2 window closed ~7/7 quiet). The "EXTENDED at 7/6 pull" wording stays (accurate as of 7/6). Source cited: `AGENTS/LABOR/outbox/2026-07-20_to-PROME_insider-rerun.md`.
- `workbook/KB_INDEX.md` INSIDER row — "streak intact through 7/6/26" → "through 7/20/26 per LABOR re-run".

**Anchor 4 — stale price token:**
- `STATUS.md` Signal Dashboard — OZK price `$49.65 [7/6]` → **`$52.01 [7/20 pre-mkt]`** (off 7/16 $53.09 high). Header line already carried the correct as-of from this morning.

**Bonus — INDEX mirror-drift (boot entry-point was stale vs canonical):**
- `INDEX.md` — Thesis **v1.3 → v1.5** (3 spots) and KB **200 rows / 28 groups → 216 / 33** (4 spots), synced to canonical STATUS/THESIS/CHANGELOG/KB_INDEX (all v1.5, 216 rows verified by direct `wc` + 7/18 reconcile). The 7/6 tree-hygiene pass-log and MAINTENANCE/KB_INDEX historical notes left intact (accurate records of prior state — not rewritten).

### CLEAN anchors (verified, no fix — no hygiene-padding)
- **Anchor 3 (dates/weekdays):** all "Tue Jul 21 / Wed Jul 22 8:30a" tokens correct across STATUS, INDEX, CALENDAR, TODO, MEMORY, scoring card, LIFE_SCI. Z8 (OZK-08 FALSE only after the full Wed call) already encoded in Addendum A.
- **Anchor 5 (fleet regime echoes):** **no** TRY-FIRE-004 / HBAN-exit-thesis / $88.10-settle / "HOLD FLAT" echoes on any OZK live surface. (The `$330` and `HBAN` grep hits are unrelated: Campus at Horton construction loan / real-estate schedule / substandard-accrual estimate, and raw/llm_outputs peer-comp provenance — not regime echoes.) Will's OZK legs (45P Aug-21 ×4 + 42.5P ×1) noted unchanged; STATUS positions-table stale-banner left AS-IS per Will's 7/4 steer.

### ⚑ FLAG — cross-agent staleness (NOT fixed; REGINALD-owned)
`STATUS.md` §Signal Dashboard cross-feed line is explicitly *"ref only, [[REGINALD]] owns"* and is stale-dated: **KRE $75.02 [live 7/4] · HY OAS 278bps [FRED 6/25] · Brent ~$72 [live 7/4].** These are dated (honestly stamped stale), but ~2wks old. Recommend REGINALD refresh the canonical values; I don't maintain an own copy (per one-source-of-truth). Possible reconcile point for the energy strand: the fleet "7/17 settle $88.10" (BZ=F settle canon) vs my Brent-spot ref ~$72 [7/4] look like different series — REGINALD/energy to confirm which is current. Low-stakes for OZK (single-name; macro backdrop only), flagging for completeness.

---
**Verdict:** OZK surfaces internally consistent and print-ready for Tue 7/21. Frozen scoring table + Addendum A untouched.
