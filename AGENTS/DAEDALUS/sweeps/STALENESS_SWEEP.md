# Fleet Staleness Sweep — Playbook (DAEDALUS recurring)

**Owner:** DAEDALUS · **Cadence:** every **21 days** (2–3 weeks; Will 2026-07-04) · **Trigger:** boot cadence-check (`scripts/sweeps_due.py`) · **Registry:** `sweeps/REGISTRY.tsv` (canonical cadence data — not restated here) · **First run:** 2026-07-04 (PAT-025).

**What it enforces:** the root `CLAUDE.md` Data-Hygiene two-state rule across **every agent's ledger + trade/position surface** — a surface must be **(a) FROZEN** (a header dead-banner) or **(b) LIVE with a boot-time mtime alert**, never the silent-rot middle (PAT-023). A stale surface with no banner reads as current when it isn't (REGINALD/TRADE.md is the exemplar: March "🔴🔴🔴 EXTREME" content, 63d behind STATUS).

---

## When to run
The boot cadence-check surfaces it when >21d since `last_run`. Run on demand any time. Detection is read-only and safe to run as often as you like.

## Procedure

### 1. Detect (read-only, always safe — exit code 0, alert not gate)
```bash
# workbook ledgers (the script's original scope)
(cd "$(git rev-parse --show-toplevel)" && .venv/bin/python3 scripts/ledger_staleness.py --all --quiet)
# trade / position surfaces (--trade added 2026-07-04, PAT-035)
(cd "$(git rev-parse --show-toplevel)" && .venv/bin/python3 scripts/ledger_staleness.py --trade --all --quiet)
```
Staleness is measured **vs each agent's own STATUS.md** (default 30d threshold). Declared-static surfaces are auto-exempt — the recognizer scans the header block for `FROZEN | RETIRED | NOT CURRENT | DO NOT CITE | NOT MAINTAINED | ARCHIVED`.

### 2. Classify each flagged surface (judgment)
| Class | Test | Disposition |
|---|---|---|
| **Dormant / archive-source** | no *self-authored* commits (dir commits from WALTER/PROME routing ≠ self-editing — verify via `git log`), STATUS.md months old | **FREEZE in place** — prepend a `FROZEN <date> — <agent> dormant; not maintained` banner |
| **Live agent** | recent self-authored commits / active STATUS | **owner freeze-or-refresh** — route a task-packet; **never direct-edit a live agent's surface** |
| **Scaffold-correct** | 0 trades / honestly-empty (e.g. TERRY TRADE_BOOK) | not rot — skip |
| **Already-routed** | check BATCH docs + prior run-log rows | don't re-route |

### 3. Disposition & authority
- **Detection is autonomous** (read-only). **All mutations are approval-gated** unless standing pre-approval exists (see below).
- **Dormant freezes:** idle-verify (git log) → prepend banner → commit by pathspec (cross-agent edit under approval, per DAEDALUS AUTHORITY).
- **Live/owner surfaces:** consolidate to one PROME rollout packet or per-owner task-packet (outbox-restraint — don't spray).
- **New mechanism gaps** (a surface the script doesn't cover, a banner vocabulary it misses): patch `scripts/ledger_staleness.py` **additively/non-breaking** + validate the default mode is byte-identical for existing callers (PAT-035).

> **Standing pre-approval (Will's call, once):** the **dormant-freeze** sub-class is low-risk + unambiguous (adding a "not maintained" banner to an idle-verified archive-source surface). If Will grants standing pre-approval, DAEDALUS may freeze dormant/idle-verified surfaces autonomously each sweep and just report; live-agent routing + mechanism patches always stay gated. **Current default: dormant freezes surface for approval each run** (as on 2026-07-04). ← *pending Will's standing-pre-approval decision.*

### 4. Record (close the loop)
- Update `sweeps/REGISTRY.tsv` → `last_run` + `last_findings`.
- Append a row to the Run Log below.
- STATUS/EVOLUTION note if the run was material; bank a PATTERN if the run taught something durable.

---

## Run Log
| Date | Scope | New stale found | Dispositions |
|---|---|---|---|
| 2026-07-04 | full (ledger + trade) | trade: REGINALD/TRADE +63d, OTTO/TRADE +113d, dormant OZK×2/ZHAO/FERT (70–108d); workbook: 9 agents (OTTO ×5, REGINALD FLOW/KB, RED FLOW, BROCK, CARL, HANS, HAWK, BRENT, MARCO) | dormant cluster **FROZEN** (Will-approved); REGINALD already routed (BATCH_03); OTTO→PROME; mechanism extended (`--trade` + header-block recognizer, non-breaking, PAT-035); boot-line rollout → one PROME packet; workbook rot = each owner's boot-alert (not re-routed) |
