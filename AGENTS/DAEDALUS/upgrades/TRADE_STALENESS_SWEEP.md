# TRADE.md / Ledger Staleness Sweep — PROPOSAL (PAT-025)

**By:** DAEDALUS · **Date:** 2026-07-04 · **Status:** ✅ **EXECUTED + INSTITUTIONALIZED** (approved; ran 7/4 as Fleet Staleness Sweep #1 — `sweeps/STALENESS_SWEEP.md` + REGISTRY row; mechanism extended 7/22 w/ the two-clock parse. Banner flipped 7/22 self-sweep; original framing: 🟡 PROPOSAL-HELD)
**Scope:** the fleet's *trade/position* surfaces (`TRADE.md` / `POSITIONS.md`) + the shared boot-alert mechanism. Sources: root `CLAUDE.md` "Data Hygiene" rule, PAT-023/PAT-025, and a live fleet scan (7/4).

---

## The rule being enforced
Root `CLAUDE.md` Data Hygiene: every ledger/position/trade surface must sit in ONE of two states, **never the silent-rot middle** —
- **(a) FROZEN** — a line-1 banner declaring it dead ("STATUS is canonical, do not cite rows as current"), or
- **(b) LIVE** with a **boot-time mtime staleness alert** so any drift behind STATUS is surfaced at boot, not left to rot.

A stale surface with *no banner and no boot-alert* reads as current when it isn't (PAT-023). REGINALD/TRADE.md is the live exemplar: March-vintage content still headed **"🔴🔴🔴 EXTREME — Eight channels active, NFP −92K, Brent $90"** with no banner, 63d behind its own STATUS.

## The core finding — this is a MECHANISM gap, not just N stale files
The enforcement mechanism (`scripts/ledger_staleness.py`, boot-wired by **6** agents: CARL/BRENT/BROCK/HAWK/REGINALD/RED) **globs `workbook/*.tsv` only** — it does **not** cover the trade/position surface. Two live demonstrations (7/4):

1. **Coverage gap.** Run with `--glob 'TRADE.md'`, the *same script* correctly flags `REGINALD/TRADE.md` → `⚠️ STALE +63d behind STATUS`. The surface is **enforceable, merely unenforced** — no agent points the alert at its TRADE.md, so the single surface most likely to be quoted into a trade is the one silent-rot can hide in.
2. **Banner-vocabulary mismatch (latent false-flag).** The freeze-check matches only the literal string **"FROZEN"** in line 1. The fleet's real dead/stale banners vary — CARL `⛔ RETIRED`, MARCO `⚠️ FEB-VINTAGE — NOT CURRENT` — both semantically compliant but **keyword-invisible**. They pass *today* only because they were recently touched (within threshold); once either ages past `--days`, it would **false-flag as stale** despite carrying a correct dead-banner.

→ The durable fix is **two layers**: fix the mechanism once (fleet-wide), then disposition the handful of genuine violations. Banner-by-banner-only would leave the gap open for the next stale TRADE.md.

---

## PROPOSAL — What / Why / Effort / Expected Value / First Step

**What.** *(Layer 1 — mechanism, the DAEDALUS-lane structural fix)* Extend `ledger_staleness.py` to (a) recognize the fleet's real freeze/dead-banner vocabulary, and (b) cover trade/position surfaces; then wire a one-line trade-surface boot-alert into each agent that carries a `TRADE.md`. *(Layer 2 — dispositions)* Route the genuine silent-rot violations to owners for freeze-or-refresh; make a lifecycle call on the dormant cluster.

**Why.** The two-state rule is on the books *fleet-wide* but **unenforced for the exact surface most likely to be cited in a trade.** One shared-script change closes the gap for every wired agent at once — mechanism-over-discipline (the same principle that made `ledger_staleness.py` worth building for workbooks). Discipline alone already failed here: REGINALD's TRADE.md rotted 63d with the rule "on the books."

**Effort.** Layer 1 = **S** (one shared-script edit — a recognizer regex + a `--trade` convenience flag — plus a one-line boot addition per TRADE.md-carrying agent, ~8–10 agents, each their own adoption). Layer 2 = **XS per surface** (a banner line), mostly owner-routed; **REGINALD is already routed** (BATCH_03).

**Expected Value.** **High / structural** — converts a fleet-wide *latent silent-rot class* into a boot-surfaced alert, and prevents the "old content presented as live 🔴🔴🔴" class from recurring silently. Low ceiling on downside: the script exit code is always 0 (alert, not gate), so wiring it can't break a boot.

**First Step.** Will/PROME approve the **mechanism change** (shared script → PROME/owner coordination, since 6 agents already call it). Then DAEDALUS drafts the script patch + a boot-line task-packet per agent; agents adopt at their next boot. No agent file is touched until approved.

---

## Per-surface disposition (fleet scan, 7/4)

| Surface | Age | Current state | Disposition | Route |
|---|---|---|---|---|
| `BRENT/TRADE.md` | 2d | **FROZEN✓** | none | — |
| `HAWK/TRADE.md` | 2d | **FROZEN✓** (applied 7/1) | none | — |
| `SAM/TRADE.md` | 2d | **FROZEN✓** | none | — |
| `CARL/TRADE.md` | 6d beh. | `⛔ RETIRED` banner — compliant-by-intent, keyword-invisible | none (Layer-1 recognizer fixes the latent flag) | — |
| `MARCO/TRADE.md` | 0d beh. | `⚠️ FEB-VINTAGE NOT CURRENT` banner — compliant-by-intent, keyword-invisible | none (Layer-1 recognizer) | — |
| `BOND/TRADE.md` | 2d | **LIVE**, dated 7/1, STATUS-sourced (informal state b) | wire trade-surface boot-alert (Layer 1) | BOND (adopt boot line) |
| `TERRY/{TRADE_BOOK,POSITION_INTAKE}.md` | 13d | **scaffold-correct** (0 trades fired) — not rot (PAT-025 N/A) | none | — |
| **`REGINALD/TRADE.md`** | **70d / 63d beh.** | **SILENT-ROT** — Mar "🔴🔴🔴 EXTREME" content, no banner | **freeze-or-refresh** | **REGINALD — ALREADY ROUTED (BATCH_03), owner-pending** |
| `BROCK/trade/TRADE.md` | 18d | position-truth stale (Mar-16 base / May-21 clean) | freeze-or-refresh | BROCK / PROME-lane (known) |
| `ORACLE/TRADE.md` | 15d | repurposed no-sizing surface, 6/18 revival, no banner | **live-vs-frozen design call** | ORACLE (in `ORACLE_CARD.md`) |
| `REGINALD/POSITIONS.md` | 14d | dated 6/19 w/ cleared-cluster note (borderline) | verify live-or-freeze | REGINALD |
| `LABOR/TRADE.md` | content 6/9 | input-agent, KELYA-only, dated header | low-priority verify | LABOR |
| `VIOLET/TRADE.md` | thin, no date | header gives no as-of — can't classify from head (L2, un-profiled) | read → banner-or-date | VIOLET |
| `AEOLUS/TRADE.md` | 5d | new agent (built 6/28), thin domain-ideas scaffold | verify scaffold-correct | AEOLUS |
| `OTTO/TRADE.md` (+5 stale workbook ledgers) | 108d | tier-2, genuinely stale/low-cadence | freeze or spin-up-refresh | OTTO (tier-2) |
| **Dormant cluster:** `OZK/{TRADE,POSITIONS}.md`, `ZHAO/TRADE.md`, `FERT/TRADE.md` | 70–108d | archive-source agents, no banner | **lifecycle call: bulk-freeze in place, or `git mv` → `_archive/`** | DAEDALUS retire-lane (design call below) |
| `REGINALD/archive/*`, `RED/research/POSITION_*` | 92–108d | archive/research artifacts | exempt (archive) — the script already `ref`-exempts `archive/`+`history` basenames | — |

**Tally:** 3 FROZEN-compliant · 2 compliant-by-intent (keyword-invisible) · 2 live/scaffold-correct · **1 clear silent-rot (REGINALD, already routed)** · 3 known-flagged (BROCK/ORACLE PROME-or-card lane) · 4 borderline-verify (BOND-adopt/POSITIONS/LABOR/VIOLET/AEOLUS) · 1 tier-2 (OTTO) · 1 dormant cluster (lifecycle).

*(Separately, the workbook side — the script's existing scope — currently flags stale ledgers at 9 agents (OTTO ×5, REGINALD FLOW/KB, RED FLOW, BROCK, CARL, HANS, HAWK, BRENT, MARCO). Those are each owner's boot-alert to freeze-or-refresh, **not** part of this trade-surface sweep — noted only as evidence the mechanism finds real rot when it's actually pointed at a surface.)*

---

## Layer-1 mechanism spec (the shared-script change — approval-gated)
1. **Broaden the dead-banner recognizer.** `is_frozen()` → `is_declared_static()`: match line-1 (case-insensitive) against `FROZEN | RETIRED | NOT CURRENT | STALE | VINTAGE | ARCHIVED`. *(Evidence: CARL `⛔ RETIRED`, MARCO `⚠️ NOT CURRENT` are correct banners the current check misses.)* Keeps good banners; avoids forcing rewrites.
2. **Cover the trade/position surface.** Add a `--trade` convenience flag globbing `{TRADE.md, TRADE_BOOK.md, POSITIONS.md}` (opt-in — **non-breaking** for the 6 current `workbook/*.tsv` callers), and document `ledger_staleness.py <NAME> --trade --quiet` as the boot line for any agent with a TRADE.md.
3. **Wire it in.** One boot line per TRADE.md-carrying agent, adopted at that agent's next boot (task-packet; live/self-sweep owners route, idle agents direct on approval). cwd-proof per PAT-031 (`(cd "$(git rev-parse --show-toplevel)" && …)`).

## Authority & routing
- **Shared script = PROME/owner coordination**, not a unilateral DAEDALUS edit — 6 agents depend on it. Propose → approve → DAEDALUS patches → agents adopt. (The change is additive + non-breaking, but the *coordination* is the gate.)
- **Per-surface banners:** idle agents → direct on approval + fresh idle-check (PAT-009); live/self-sweep owners → task-packet. REGINALD already routed.

## Open design calls for Will/PROME
1. **Trade-surface coverage:** `--trade` convenience flag (recommended — opt-in, non-breaking) vs a default-glob change (touches all 6 current callers).
2. **Banner vocabulary:** broaden the recognizer (recommended — keeps CARL/MARCO's good banners) vs standardize every dead surface to the literal "FROZEN" (forces rewrites).
3. **Dormant cluster** (OZK/ZHAO/FERT + OTTO tier-2): bulk-freeze in place (cheap, keeps them scannable) **or** `git mv` → `AGENTS/_archive/` (true lifecycle retirement — DAEDALUS's retire-lane, bigger, needs a rewiring/impact pass). Recommend **bulk-freeze now**, revisit archival separately.

---

## BOTTOM LINE
The staleness rule is enforced for *workbook ledgers* but **not for the trade/position surface** — the one most likely to be quoted into a trade. The fix is structural, not clerical: **one additive, non-breaking change to `ledger_staleness.py`** (recognize the fleet's real dead-banners + a `--trade` glob) + a one-line boot adoption per agent closes the class fleet-wide; only **one** surface is in genuine active silent-rot (REGINALD, already routed) and it's the proof the rule needs a mechanism, not more discipline. **HELD for approval** — mechanism change first (PROME/owner-coordinated), then per-surface routing.
