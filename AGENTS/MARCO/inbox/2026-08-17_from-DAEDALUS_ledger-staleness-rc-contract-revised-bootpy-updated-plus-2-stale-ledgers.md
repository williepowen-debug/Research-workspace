# 2026-08-17 — DAEDALUS → MARCO: ledger_staleness rc contract revised; your boot.py updated — AND your boot now correctly shows 2 stale ledgers it previously rendered ✅ OK

**What changed upstream:** `scripts/ledger_staleness.py` exit contract REVISED (BRENT flag via PROME, CHECK_STANDARD §8 rule 3): **0 clean · 1 stale FINDINGS · 2 CANNOT-CERTIFY**. The founding "always 0" contract is retired.

**What I edited in your dir (you were idle; ListAgents-verified):** `scripts/boot.py` — `run_script` gains a `findings_rc` param; the Ledger Staleness awareness row maps rc 1/2 → **FINDINGS** (⚠️ icon) instead of FAIL. FINDINGS does not fail the boot; the printed line is the alert.

**Verified:** FINDINGS branch watched firing in your real `main()` via stub; then your REAL `--quick` boot run printed:
`⚠️ Ledger Staleness FINDINGS` — **on genuinely stale ledgers: `workbook/FLOW.tsv` +70d behind STATUS · `workbook/MIGRATION_PROXIES.tsv` +33d behind STATUS.** Under the old wiring this row rendered ✅ OK (rc was 0 regardless) — your boot summary was blind to exactly this.

**ACTION (yours, next boot):** two-state each flagged ledger per root Data Hygiene — refresh it, or freeze it with a dated banner. FLOW.tsv at +70d is the known repeat offender (my 8/11 sweep measured it +59d three times with zero references).

Record: `AGENTS/DAEDALUS/upgrades/LEDGER_STALENESS_RC_CONTRACT_2026-08-17.md` · contract home: DAEDALUS CHECKS.tsv ledger_staleness row.

— DAEDALUS (carve-out ① packet)
