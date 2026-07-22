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

> **Self-inclusion (2026-07-12, PAT-050):** `AGENTS/DAEDALUS/` is IN SCOPE — check own ledger-class surfaces (FLEET_MAP row currency, upgrades/ batch-doc banners vs dispositions, outbox flat-files vs `delivered/`) the same way. The 7/12 self-sweep found 9 dead outbox files + a 2-week-stale self-row precisely because this sweep never looked inward.

### 2. Classify each flagged surface (judgment)
| Class | Test | Disposition |
|---|---|---|
| **Dormant / archive-source** | no *self-authored* commits (dir commits from WALTER/PROME routing ≠ self-editing — verify via `git log`), STATUS.md months old | **FREEZE in place** — prepend a **condition-cited** banner: `FROZEN <date> — <surface-level reason, e.g. "not maintained since <date>; refresh/unfreeze when <condition>">`. **NEVER cite agent lifecycle state ("<agent> dormant/retired") as the reason — it goes FALSE the day the agent revives while the freeze itself usually stays right (PAT-057; the OZK 7/4 banners are the cautionary instance, my own).** Revival playbooks must include a FROZEN-banner re-sweep step |
| **Live agent** | recent self-authored commits / active STATUS | **owner freeze-or-refresh** — route a task-packet; **never direct-edit a live agent's surface** |
| **Scaffold-correct** | 0 trades / honestly-empty (e.g. TERRY TRADE_BOOK) | not rot — skip |
| **Already-routed** | check BATCH docs + prior run-log rows | don't re-route |

### 3. Disposition & authority
- **Detection is autonomous** (read-only). **All mutations are approval-gated** unless standing pre-approval exists (see below).
- **Dormant freezes: STANDING PRE-APPROVED (Will, 2026-07-04) — autonomous under the gate below.** idle-verify (`git log`: no *self-authored* commits + STATUS older than cadence) → prepend a `FROZEN` banner → commit by pathspec → **log + report.** Ambiguous idle-verify → fall back to surface-for-approval (don't freeze on a maybe).
- **Live/owner surfaces:** consolidate to one PROME rollout packet or per-owner task-packet (outbox-restraint — don't spray).
- **New mechanism gaps** (a surface the script doesn't cover, a banner vocabulary it misses): patch `scripts/ledger_staleness.py` **additively/non-breaking** + validate the default mode is byte-identical for existing callers (PAT-035).

> **Standing pre-approval — GRANTED 2026-07-04 (Will), tightly scoped.** DAEDALUS may **freeze dormant surfaces autonomously** each sweep and report, under ALL of:
> - **(a) freeze-only** — prepend a "not maintained" banner; **never** delete or content-refresh.
> - **(b) idle-verification passes** — the surface is script-flagged stale **AND** the agent has **zero *self-authored* commits** within the cadence window (WALTER/PROME routing commits do **not** count — check `git log` author + content) **AND** STATUS.md predates the cadence.
> - **(c) always logged** in the Run Log + reported to Will each run.
> - **(d) reversible** — it's a banner; removed on revival.
>
> **Everything else stays gated:** live-agent surfaces are **routed, never direct-edited**; `ledger_staleness.py` patches need approval. **If idle-verification is ambiguous, fall back to surface-for-approval — do not freeze on a maybe.** *(This pre-grant covers "permission" for the bounded class; the per-action idle guard still runs — PAT-036.)*

### 4. Record (close the loop)
- Update `sweeps/REGISTRY.tsv` → `last_run` + `last_findings`.
- Append a row to the Run Log below.
- STATUS/EVOLUTION note if the run was material; bank a PATTERN if the run taught something durable.

---

## Run Log
| Date | Scope | New stale found | Dispositions |
|---|---|---|---|
| 2026-07-04 | full (ledger + trade) | trade: REGINALD/TRADE +63d, OTTO/TRADE +113d, dormant OZK×2/ZHAO/FERT (70–108d); workbook: 9 agents (OTTO ×5, REGINALD FLOW/KB, RED FLOW, BROCK, CARL, HANS, HAWK, BRENT, MARCO) | dormant cluster **FROZEN** (Will-approved); REGINALD already routed (BATCH_03); OTTO→PROME; mechanism extended (`--trade` + header-block recognizer, non-breaking, PAT-035); boot-line rollout → one PROME packet; workbook rot = each owner's boot-alert (not re-routed) |
