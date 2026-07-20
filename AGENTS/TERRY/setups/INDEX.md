# TERRY CARD INDEX — the master registry of every trade card
**Updated:** 2026-07-20 ~10:05 ET · **Owner:** TERRY · **Purpose:** the single "where is everything / what's live" view. Update this whenever a card is added, changes status, fires, or is archived.

> **Standing rules:** all cards are **PROPOSE-ONLY** — Will approves/rejects, TERRY never executes. Max loss **$500/card** (TRY-FIRE-006 = a separate **$200** Tier-2 tranche). **★ 1 card fired live** as of 2026-07-20 — TRY-FIRE-004 (30× TLT Sep-30 77P @ $0.11, $330 at risk). Was 0 for the first month; the refusals were the product until now.

---

## 📁 Folder layout (where cards live)
| Location | What's there |
|---|---|
| `setups/` (this folder) | **LIVE + STAGED cards** — anything that can still fire, plus the two index/support docs below |
| `setups/_archive/` | **DEAD / SHELVED / SPENT** — cards killed by their own gate + spent one-time templates; kept for the record, not maintained |
| `daytrading/` | **Day-trade lane** — separate from the thesis book by design (Will 6/27); `QQQ_DESK_CARD.md` etc. |
| `AGENTS/TERRY/` (root) | Templates (`TRADE_CARD_TEMPLATE.md`, `TRADE_CARD_TEMPLATE_FIRE.md`), ledgers (`TRADE_BOOK.md`, `SETUPS.tsv`), `POSTMORTEMS.md` |

**Cross-indexes:** `SETUPS.tsv` (structured/greppable tracker) · `TRADE_BOOK.md` (human ledger) · `FIRE_CARDS_LADDER.md` (fire-card 001-004/006 side-by-side comparison). This INDEX is the top-level registry; those are the detail views.

---

## 🟢 LIVE / STAGED cards (`setups/`)

| ID | Status | Class | Instrument / structure | Trigger / catalyst | Thesis owner | File |
|---|---|---|---|---|---|---|
| **TRY-FIRE-004** | 🟢 **FIRED LIVE 7/20** (30× 77P @ $0.11, $330 at risk; ~$170 bank dry) | FLOW | TLT Sep-30 77P — pure gap-tail | FILLED on arm-#2 LIT + rule-#6-clean GREEN-TLT entry; pays on a GAP (7/22→8/13 catalyst cluster), disarm on DGS10 close <4.50 | BOND / HENRY | `FLOW-TRIGGER_duration-TLT-put.md` |
| **TRY-FIRE-001** | STAGED (closest-to-live after 004) | PRICE | KRE puts, 3-6mo, 8-12% OTM | HY OAS ≥280 sustained (271 [7/16], 9bp under) | REGINALD + NEXUS | `PRICE-TRIGGER_HY280_regional-put.md` |
| **TRY-FIRE-002** | STAGED | PRINT | WAL / EGBN puts, post-print Sep/Jan | WAL 7/21 AMC · EGBN 7/22 — path (a)/(c) grade | REGINALD / CARL | `PRINT-TRIGGER_WAL-EGBN-build.md` |
| **TRY-FIRE-003** | STAGED | PRINT | COF / SYF / ALLY monoline puts | SYF/ALLY 7/21 · COF 7/21-23 — path (m) un-mask | CARL + REGINALD | `PRINT-TRIGGER_monoline-COF-SYF-ALLY.md` |
| **TRY-FIRE-006** | PRE-BUILT / **ARMABLE** (GATE-TERRY-006 LIVE 7/18; dependency discharged; $200 tranche) | FLOW | USO OTM call spread, ~45-60 DTE | **Corroborator-anchored** (dark-fleet-capable, ≥2d, not vetoed) — PortWatch AIS loadings = refuting VETO only, NOT Hormuz transit | RED / BRENT / FALCON | `FLOW-TRIGGER_kharg-strand-USO-call.md` |
| **TRY-WAL-GRIND** | CONDITIONAL (REGINALD confirm pending) | PRINT/roll | WAL 77.5/67.5P Jan-2027 put spread | post-7/21 green WAL day; roll target for dying Sep WAL puts | REGINALD `[confirm]` | `WAL_grind-putspread_2026-07-17.md` |
| **TRY-BUILDER-DHI-PHM** | CONDITIONAL (HOMER confirm pending) | PRINT | DHI/PHM Sep put SPREAD (NOT front-week naked) | DHI 7/21 BMO · PHM 7/22 BMO | HOMER `[confirm]` | `HOMER_builder-putspread_2026-07-17.md` |
| **HBAN stub** | 🪦 **RETIRED 7/18 — dust-rider** (Will EXIT-THESIS; rides to expiry as ~$20 dust, do not pay to close, no re-entry) | PRINT | HBAN Oct-16 16P ×2 (already owned) | ~~HBAN Q2 7/23~~ MONITOR-ONLY | Will (opportunistic) | `HBAN_oct16-16P_stub.md` |

**Support docs in `setups/` (not cards):** `FIRE_CARDS_LADDER.md` (fire-card comparison) · `HBAN_oct16-16P_two-branch-decision-memo.md` (HBAN decision memo) · `INDEX.md` (this file).

---

## 🔴 ARCHIVED (`setups/_archive/`) — dead / spent, not maintained

| ID / item | Why archived | File |
|---|---|---|
| **TRY-FIRE-005** (FXY carry-convexity calls) | 🔴 DEAD — 7/10 COT print resolved DENY; never entered, $0 at risk; terminal per its own kill rule (needs a fresh build, not a revival). Postmortem in `POSTMORTEMS.md`. | `_archive/FLOW-TRIGGER_carry-convexity-FXY-call.md` |
| **ARM3 TIC grading template** | Spent — the arm-#3 grade it served ran 7/16 (fired weak); one-time template, no further use | `_archive/ARM3-TIC-grading-template_2026-07-16.md` |

---

## 🗂 Conventions (going forward)
- **Fire-card numbering:** `TRY-FIRE-NNN` — a stable, gap-free ledger. **Do not reuse a number** even after a card dies (005 stays 005, archived). Non-fire construction cards use a descriptive ID (`TRY-WAL-GRIND`, `TRY-BUILDER-DHI-PHM`).
- **Filenames:** numbered fire cards use `CLASS-TRIGGER_descriptor.md` (PRICE/PRINT/FLOW); dated construction cards use `TICKER_structure_YYYY-MM-DD.md`. *(Existing names grandfathered — don't rename live files, it breaks cross-references; apply the convention to new cards.)*
- **Status lives in this INDEX (a column), NOT in per-status subfolders** — cards change status often (staged→armed→fired), and shuffling files between folders breaks references. Only truly-dead cards move to `_archive/`.
- **When a card dies:** `git mv` it to `_archive/`, update its row here (LIVE → ARCHIVED), update any live pointer (LADDER/POSTMORTEMS), and record a postmortem if it was ever near-fired.
