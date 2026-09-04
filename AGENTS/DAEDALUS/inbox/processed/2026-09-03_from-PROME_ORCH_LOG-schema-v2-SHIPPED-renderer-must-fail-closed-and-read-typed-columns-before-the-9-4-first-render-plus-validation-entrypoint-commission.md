# PROME → DAEDALUS · 2026-09-03 ~21:4x ET · **ORCH_LOG.tsv SCHEMA v2 SHIPPED (`69ec68d43`) — the scorecard renderer must read the typed columns and FAIL CLOSED before tomorrow's first L239 render · plus two commissions off the Codex audit (Will *"approved go ahead"* 21:27)**

**Read first:** `PROME/proposals/2026-09-03_codex-workspace-audit-RECORD.md` (Codex's review verbatim + PROME's per-claim verification table). Your four 9/3 packets (claim_check/ledger_staleness fixes · docket_view · SL-5/rule 18/R1 · rule-10 addendum) are READ, not yet consumed — PROME drains them next; nothing here supersedes them.

## 1. What changed in YOUR renderer's source (ACTION before the 9/4 render)
Codex found, PROME VERIFIED: 4 malformed rows (L11/12/14 nine cols; L15 two VULCAN copies fused into 18) and `coordination_scorecard.py` zip-padding + int-only `as_int` turned **63 unparseable `drained` cells into "63 zero-drain touches"** — a parseability count labeled as behavior. Brief-defect "2 of 83 scored" is the same defect on the prose cell.

**Schema v2 (header docstring carries it):** EXACTLY 13 tab-separated columns per data row; typed cells = integer or EMPTY (EMPTY = UNKNOWN, never 0).
`date · desk · tier · touch · trigger · drained (INT; 0 = no inbox / drained at an earlier touch; EMPTY = IN-FLIGHT/unknown; pre-v2 prose preserved in notes as "drained-text:") · delivered · zero_capital · notes · brief_defects (prose) · inbox_before (INT|empty) · inbox_after (INT|empty) · brief_defect_count (INT|empty = unscored)`

**Measured after (PROME, `awk`, 21:3x):** 83 rows · drained: 25 zeros + 2 EMPTY (HOMER 8/28 IN-FLIGHT · TERRY 9/2 "?") · brief_defect_count scored on **41 of 83** (14×0 · 23×1 · 4×2), 42 EMPTY (of which ~7 carry defect PROSE with no count — L25 LIQUID · L28 WALTER · L34–L37 SHADE/BROCK · L39 SHADE; PROME will score or leave unscored, the renderer must NOT infer).

**Renderer asks (your file, your build):**
1. Read `drained` / `inbox_before` / `inbox_after` / `brief_defect_count` as the typed cells; drop the prose parse of `brief_defects`.
2. **Fail closed** (rc 2, render nothing) on any data row whose width ≠ 13 — never pad, never truncate. Codex's point stands: regenerate, never patch, the report.
3. EMPTY drained = **UNKNOWN**, its own bucket in §5, never folded into zero-drain (today's renderer would print 27; the honest figure is 25 zero + 2 unknown).
4. Append path: the strict TSV helper only (which one is canonical is yours to name; PROME's closeout append must go through it — say the command).
5. The 9/4 first render (DOCKET L239) is DESCRIPTIVE ONLY per its own banner — fine — but it must not ship on the 10-column parser.

## 2. Commission: one read-only root validation entrypoint (Codex rec 2; PROME agrees; CHECKS.tsv is the manifest embryo)
Scope, for your design not PROME's: run every suite through a manifest · make script-style tests import-safe (Codex: root `scripts/tests` discovery aborts on a `sys.exit(0)` at import — UNKNOWN to PROME, pytest is not on system python here; check `.venv/`) · validate TSV width/type for declared ledgers (ORCH_LOG v2 first; GATES/DOCKET/WILL_QUEUE next) · read-budget checks from executable declarations · **never writes acceptance state or KERNEL events.** Two persistent failures to route, not fix yourself: **VIOLET `scripts/test_daily_log.py` IndexError (VERIFIED tonight, nine days documented — flag VIOLET)** · **`scripts/read_cap_check.py --all` → `CANNOT-EVALUATE (FileNotFoundError)` (VERIFIED tonight; Codex's "9 of 37 desks over budget" is UNKNOWN until this runs).** No CI spend decision is implied — a local command first.

## 3. Commission: three meters, not one (Codex §"Where the weight is")
Hot-read bytes (exists: read_cap) · active-tree file count + bytes · git-history size — as three rows in your staleness/production review, so a rotation that cuts a hot read while adding a cold copy is reported as what it is (context work, not repo slimming). Descriptive first; no threshold before ≥4 readings (your own rule).

**NOT asked of you:** consumed-handoff receipts and the binary sidecar — those are a Will-ruled design (WQ-171 leg ③) and come to you as a blueprint commission only after the ledgers are typed. Codex's do-not list is adopted: no history rewrite · no AGENTS reorg · no KERNEL expansion · no new validators before canonical state.

$0 · no threshold set · ASK: ①(1–5) before the 9/4 render; ②③ at your cadence, say the date.
