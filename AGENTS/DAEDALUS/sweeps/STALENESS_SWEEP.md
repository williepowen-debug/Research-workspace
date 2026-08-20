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
# --strict leg (added 2026-08-11, run #3): name-exempt surfaces (archive/history/…)
# reviewed as CANDIDATES once per sweep — deliberate exemptions are never LOOKED at
# otherwise (SAM FLOW_ARCHIVE sat +74d exempt-by-name with a +39d unnamed sibling).
# Exempt-class flags are candidates for the owner's judgment, NOT defects.
(cd "$(git rev-parse --show-toplevel)" && .venv/bin/python3 scripts/ledger_staleness.py --all --strict --quiet)
```
> ⚠️ **A zero-flag `--trade` pass certifies ~24 hardcoded-name files, not the fleet** (16 agents print "no ledgers found" only in non-quiet; silent under `--quiet`). Until the fail-loud/report-unmatched patch ships, read a clean trade pass as "the 24 matched files are clean," never "the fleet's position surfaces are clean." (Run #3 finding.)
Staleness is measured **vs each agent's own STATUS.md** (default 30d threshold). Declared-static surfaces are auto-exempt — the recognizer scans the header block for `FROZEN | RETIRED | NOT CURRENT | DO NOT CITE | NOT MAINTAINED | ARCHIVED`.

> **Self-inclusion (2026-07-12, PAT-050):** `AGENTS/DAEDALUS/` is IN SCOPE — check own ledger-class surfaces (FLEET_MAP row currency, upgrades/ batch-doc banners vs dispositions, outbox flat-files vs `delivered/`) the same way. The 7/12 self-sweep found 9 dead outbox files + a 2-week-stale self-row precisely because this sweep never looked inward.

### 2. Classify each flagged surface (judgment)
| Class | Test | Disposition |
|---|---|---|
| **Dormant / archive-source** | no *self-authored* commits (dir commits from WALTER/PROME routing ≠ self-editing — verify via `git log`), STATUS.md months old | **FREEZE in place** — prepend a **condition-cited** banner: `FROZEN <date> — <surface-level reason, e.g. "not maintained since <date>; refresh/unfreeze when <condition>">`. **NEVER cite agent lifecycle state ("<agent> dormant/retired") as the reason — it goes FALSE the day the agent revives while the freeze itself usually stays right (PAT-057; the OZK 7/4 banners are the cautionary instance, my own).** Revival playbooks must include a FROZEN-banner re-sweep step |
| **Live agent** | recent self-authored commits / active STATUS | **owner freeze-or-refresh** — route a task-packet; **never direct-edit a live agent's surface** |
| **Scaffold-correct** | 0 trades / honestly-empty (e.g. TERRY TRADE_BOOK) | not rot — skip |
| **Already-routed** | check BATCH docs + prior run-log rows — **AND the recipient's last SELF-authored commit (dark-recipient gate, run #3 / MARCO)**: a packet into an inbox not drained since the packet's date is UNDELIVERED-IN-EFFECT and the finding stays OPEN, whatever the routing history says. Three MARCO dispatches by three route shapes reached zero sessions | don't re-route the same way; if the recipient is dark, escalate the SPAWN, not the packet |

### 3. Disposition & authority
- **Detection is autonomous** (read-only). **All mutations are approval-gated** unless standing pre-approval exists (see below).
- **Dormant freezes: STANDING PRE-APPROVED (Will, 2026-07-04) — autonomous under the gate below.** idle-verify (`git log`: no *self-authored* commits + STATUS older than cadence) → prepend a `FROZEN` banner **(condition-cited form per the §2 template / PAT-057 — never lifecycle-cited)** → commit by pathspec → **log + report.** Ambiguous idle-verify → fall back to surface-for-approval (don't freeze on a maybe).
- **Live/owner surfaces:** consolidate to one PROME rollout packet or per-owner task-packet (outbox-restraint — don't spray).
- **New mechanism gaps** (a surface the script doesn't cover, a banner vocabulary it misses): patch `scripts/ledger_staleness.py` **additively/non-breaking** + validate the default mode is byte-identical for existing callers (PAT-035).

> **Standing pre-approval — GRANTED 2026-07-04 (Will), tightly scoped.** DAEDALUS may **freeze dormant surfaces autonomously** each sweep and report, under ALL of:
> - **(a) freeze-only** — prepend a condition-cited "FROZEN <date> — <surface-level reason>; not maintained" banner (§2 template, PAT-057); **never** delete or content-refresh.
> - **(b) idle-verification passes** — the surface is script-flagged stale **AND** the agent has **zero *self-authored* commits** within the cadence window (WALTER/PROME routing commits do **not** count — check `git log` author + content) **AND** STATUS.md predates the cadence.
> - **(c) always logged** in the Run Log + reported to Will each run.
> - **(d) reversible** — it's a banner; removed on revival.
>
> **Everything else stays gated:** live-agent surfaces are **routed, never direct-edited**; `ledger_staleness.py` patches need approval. **If idle-verification is ambiguous, fall back to surface-for-approval — do not freeze on a maybe.** *(This pre-grant covers "permission" for the bounded class; the per-action idle guard still runs — PAT-036.)*

### 3b. Run #4 SCOPE ADD (Will-approved 2026-08-20 — staleness-cadence proposal rollout step 3; registered here so the ~9/1 session inherits it regardless of who runs)
- Run the **(a)+(c) CANDIDATES pass**: `--all --writes` and `--all --abs-floor` beside the default pass. **CANDIDATES, not defects** (PROME 8/4 item 2 verbatim): a flagged ledger is a prompt for the OWNER to confirm its real cadence — route per-owner notes, never freeze on the writes/abs read alone. Seed context: the 8/4 backlog framing measured ~32 ledgers ≥12 STATUS-writes behind.
- The (b) nudge is NOT sweep work — it's the per-agent closeout line (root canon, PROME landing it); the sweep only spot-checks that the line exists in root canon by run #4's date.

### 4. Record (close the loop)
- Update `sweeps/REGISTRY.tsv` → `last_run` + `last_findings`.
- Append a row to the Run Log below.
- STATUS/EVOLUTION note if the run was material; bank a PATTERN if the run taught something durable.

---

## Run Log
| Date | Scope | New stale found | Dispositions |
|---|---|---|---|
| 2026-08-11 | full (ledger + trade) + **first 6-reader fan-out** (flags · repeat-offender · largest-flag · PAT-092 census · null-verification · self-scope) | script: 3 agents / 9 surfaces (CARL ×6 +31d, MARCO ×2 +59d, REGINALD VX +130d); trade: zero. **Readers re-cut the picture:** CARL 3-of-6 = recognizer FP (`FROZEN-VINTAGE` line-1 banners vs glue guard #4) → **rule 4b shipped same-run** (6-case capable suite; fleet diff = EXACTLY the 3 intended flips; trade byte-identical), 2 = Will-ratified dossier cadence (skip), 1 real (GIG/AV_TRACKER — session ran 8/10, ledger left 7/08). **MARCO = THIRD-FLAG MECHANISM INDICTMENT** (same 15-line wiring fix dispatched 3× by 3 route shapes, 0 reached a session; dark 11d, 8-packet backlog; relative clock re-measured a frozen +59d while true age grew to 70d). **REGINALD VX: the boot-alarm premise is FALSIFIED** — a real 8/10 recovery session drained 17 packets with the +130d alarm firing and never touched VX (PAT-095) → needs a NAMED ask line. **Null-verification: 0 missed-stale, 3 blind-spots** — ORACLE TRADE.md sub-threshold rot (2 superseded odds cited to BRENT/HAWK, crosses 30d ~8/21) · HANS contradiction inside a passing ledger (dormant relative-clock, true 50d; breached self-kill 26d un-adjudicated) · SAM archive pair name-exempt (+74d/+39d). v4 restorations CONFIRMED GRADING (first live catch: PHAN/COCKROACH); BROCK VX_HISTORY genuinely closed. `--trade` certifies 24 files not the fleet (16 agents = silent nulls under --quiet). **Census: 12 agents ≥7d dark; the 8/10 forum swept all six 8/7-dark agents back in — forum = de-facto liveness mechanism; today's dark set ≈ non-participants.** Consequence priorities: MARCO (unread FIRED signal eff. 8/19) · AEOLUS (both triggers passed while dark on a TERRY-killed vehicle) · DEWEY (8/14 deadline, 16-deep, NO STATUS.md — invisible to every STATUS-relative check) · HANS. Self-scope: outbox clean (8/11 fixes held); CREED profile self-declared wrong + SHADE clock expires 8/12; 13 unbannered upgrade docs; SURFACES half-false WAL cell fixed + FORGE/timing row added; HERMES 45d undated RETIRE-candidate | **0 dormant freezes** — MARCO ML.tsv fails pre-approval leg (b) (STATUS 11d < cadence) despite doc-declared-frozen; surfaced to Will instead of frozen-on-a-maybe. Recognizer rule 4b = my lane (7/31 grant), capable-cased. Consolidated PROME rollup + direct ORACLE packet. Mechanism items registered: `--strict` leg each sweep (SAM pair class) · `--trade` fail-loud/report-unmatched · absolute-age floor (PAT-092, joins the greenlit staleness-cadence draft). **Reader ops note: 4-of-6 idled without delivering despite the instruction in every prompt — the chase is a standing part of the fan-out, plan for it** |
| 2026-07-25 | full (ledger + trade) | **trade: ZERO flags — first-ever clean pass** (7/4 freeze cluster + 7/22 PAT-057 re-words + PAT-059 v3 recognizer all held). workbook: 5 agents / 11 surfaces — HENRY FLOW/KB/MARKET_DATA (+30d ×3), MARCO FLOW/ML (+37d), BROCK FLOW (+42d), OTTO ×3 (+80–101d), REGINALD FLOW/KB (+141d/+104d) | **0 dormant freezes** (nothing qualified — pre-approval unused this run). TRUE silent-rot = **HENRY + MARCO** (boot-wiring verified ABSENT: HENRY boot.py covers tape/gamma/credit/preds only; MARCO staleness.py = STATUS+VX only — both were in the 7/4 PROME boot-line rollout, still unapplied → **re-pinged in one PROME packet**, not re-routed fresh). BROCK wired (CLAUDE:33) + REGINALD wired (CLAUDE:43, honest two-clock headers) = compliant owner-alert lane; **REGINALD's pre-registered refresh gate (post-7/21 print) has now PASSED** → folded into the WP-W0 nudge (same post-print pass as v2.3). OTTO tier-2 already-routed 7/4, idle since — not re-routed. Self-scope (PAT-050): FLEET_MAP re-scored same boot, outbox 1 flat file = live WAL-cutover packet (legitimately open), CORAL card/proposal banners closed this boot |
| 2026-07-04 | full (ledger + trade) | trade: REGINALD/TRADE +63d, OTTO/TRADE +113d, dormant OZK×2/ZHAO/FERT (70–108d); workbook: 9 agents (OTTO ×5, REGINALD FLOW/KB, RED FLOW, BROCK, CARL, HANS, HAWK, BRENT, MARCO) | dormant cluster **FROZEN** (Will-approved); REGINALD already routed (BATCH_03); OTTO→PROME; mechanism extended (`--trade` + header-block recognizer, non-breaking, PAT-035); boot-line rollout → one PROME packet; workbook rot = each owner's boot-alert (not re-routed) |
