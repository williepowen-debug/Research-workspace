# ledger_staleness.py rc-contract revision — 2026-08-17

**Trigger:** PROME packet 2026-08-17 (BRENT flag, routed per git-protocol "flag to Prome"): the shared
check returns rc=0 even when it finds stale ledgers — the silent-fallback-green class (§8) in a shared
script multiple boots wire. **Authority:** DAEDALUS `scripts/` grant (Will-ruled 7/31) for the script;
PROME's packet ("own the fix", suggested shape endorsing the rc contract) read as the express PROME
approval for the coordinated consumer edits; all 7 consumer owners verified IDLE via `ListAgents`
before editing (only PROME + WALTER live). Scope reading stated in the PROME write-back for veto.

## Finding correction (worse than reported)

The packet said "rc=2 paths are reserved for MISCONFIGURED / LEDGERS-OUTSIDE-GLOB." **Source read
refutes this: those paths ALSO exited 0** — `main()` returned 0 unconditionally; only arg-errors
(agent-not-found / no-args) returned 2. Founding contract was "Exit code is always 0 — this is an
alert, not a gate" (docstring line 38), praised at adoption as "wiring it can't break a boot"
(TRADE_STALENESS_SWEEP.md 7/04). The 7/31 trio dead-code fix REMOVED consumers' rc branches instead
of fixing the producer's contract — the fix went the wrong direction (PAT-110).

## The revised contract (rides CHECK_STANDARD §8 rule 3)

| rc | meaning |
|---|---|
| 0 | clean — everything scanned, nothing stale, no enforcement warnings |
| 1 | FINDINGS — stale ledger(s) found (workbook or `--trade` mode) |
| 2 | CANNOT-CERTIFY — MISCONFIGURED LEDGER_GLOB / LEDGERS-OUTSIDE-GLOB / agent-not-found / usage. Dominates 1 in `--all` aggregation |

Markers (⚠️/🔴) remain the authoritative wrapper channel per §8 rule 5 — rc now AGREES with them
instead of contradicting them. `--trade` perimeter statement stays unmarked and rc-neutral.

## Consumer batch (same session — the 8/16 trio regression is why this is one batch, never two)

| file | change | capable-case watched |
|---|---|---|
| `scripts/ledger_staleness.py` | contract + docstring | clean→0 · BRENT `--days 1`→1 (the literal repro) · MISCONFIGURED→2 · OUTSIDE-GLOB→2 · not-found→2 · fleet `--all --quiet`→rc1 w/ 4 stale agents · `--all --trade`→rc0 + perimeter |
| WATT/VULCAN/MIDAS/FERT `boot.py` `run_alert` | rc∉(0,1)→2; verdict = rc1 OR marker | 4/4 imported live: clean=0 · stale=1 · misconf=2 |
| `AGENTS/BRENT/scripts/boot.py` | `FINDINGS_RCS` map + `run_script` param + stale-premise comment rewritten (his own dated-carry-item flag) | OK / FINDINGS / FINDINGS on clean/stale/misconf |
| `AGENTS/OTTO/scripts/boot.py` | rc1→FINDINGS status + ⚠️ icon | real boot clean-path OK ×2 rows; stub rc1 → "⚠️ … FINDINGS" watched in real `main()` |
| `AGENTS/MARCO/scripts/boot.py` | `findings_rc` param + icon | stub rc1 → FINDINGS watched; **real `--quick` run now prints `⚠️ Ledger Staleness FINDINGS` on MARCO's genuinely stale FLOW.tsv +70d / MIGRATION_PROXIES.tsv +33d — previously rendered ✅ OK** |

Not affected (verified): HENRY/CARL/ZHAO/RED boots carry LOCAL staleness implementations;
`position_agreement_check.py` imports functions only; VIOLET `canary_staleness` separate; YEYOU
comment-only; 16 protocol-doc boot lines are prose consumers reading printed output.

## Exposure 2 — glob-coverage audit (PROME shape #2): measured, detector DECLINED

Method: per agent, recursive non-exempt `.tsv` not matched by effective glob (LEDGER_GLOB if
declared else `workbook/*.tsv`), excluding inbox/outbox/processed/delivered/archive-class/memory.
(Audit script preserved below for reproducibility.)

**Result: 22 agents / 83 uncovered TSVs (5 frozen-bannered).** Dominant classes: `docket/CATALYSTS.tsv`
(~9 agents — covered by firetime_check/claim_check/countdown instruments), `thesis/PREDICTIONS.tsv`
(~7 — covered by boot predictions-due scans, row-49 blueprint REQUIRED form), fetcher-output data dirs
(MARCO `baselines/` 18, CARL `scripts/data/`, BRENT `scripts/data/`), registry/eval surfaces with own
graders (WALTER 16, RED, CREED, YEYOU). BRENT's 3 actually-rotting ledgers were: `board_log.tsv`
(deliberately NON_LEDGER-excluded), 2 subdir ledgers — a top-level-only detector extension would have
caught **none of them**, and a recursive one ships 83 flags. **Decision: no detector change — the fix
is per-owner LEDGER_GLOB declarations (BRENT's `f6c939f09` = the reference form) driven by the
registered-surfaces manifest** (`design/2026-08-15_LEDGER_STALENESS_REGISTERED_SURFACES_SPEC.md`,
build before Staleness #4 ~9/1; this table is its seed data; cross-referenced to FORGE-audit
scope-add (c), coverage-inversion class, per PROME's fold note).

Pre-existing stale findings surfaced by the fleet run (owner-lane, sweep catches on cadence):
CARL COCKROACH/REGULATORY +37d · CRUISE FLOW +43d · MARCO (packeted) · RED VX +76d.

<details>
Audit script (rerunnable):

```python
import glob as g, os, sys
sys.path.insert(0, "/home/willi/Research-workspace/scripts")
from ledger_staleness import read_ledger_glob, is_exempt, NON_LEDGER_NAMES, is_frozen
REPO = "/home/willi/Research-workspace"
SKIP_DIRS = {"inbox","outbox","processed","delivered","archive","_archive","archives","memory",".git","reports_archive","sent"}
for status in sorted(g.glob(os.path.join(REPO, "AGENTS", "*", "STATUS.md"))):
    d = os.path.dirname(status); name = os.path.basename(d)
    decl = read_ledger_glob(d); pats = decl if decl is not None else ["workbook/*.tsv"]
    covered = {os.path.abspath(x) for p in pats for x in g.glob(os.path.join(d, p))}
    unc = []
    for root, dirs, files in os.walk(d):
        dirs[:] = [x for x in dirs if x.lower() not in SKIP_DIRS]
        unc += [os.path.abspath(os.path.join(root, f)) for f in files
                if f.endswith(".tsv") and os.path.abspath(os.path.join(root, f)) not in covered
                and f not in NON_LEDGER_NAMES and not is_exempt(os.path.join(root, f))]
    if unc: print(name, "declared" if decl is not None else "default", len(unc))
```
</details>

## Routed

PROME write-back (scope-reading + §8-canon one-liner offer + audit rollup) · owner notes to
WATT/VULCAN/MIDAS/FERT/OTTO/MARCO/BRENT inboxes. PAT-110 banked. CHECKS.tsv row re-cut.
