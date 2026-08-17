# Fleet Production Review — Playbook (DAEDALUS recurring)

**Owner:** DAEDALUS · **Cadence:** every **14 days** (Will 2026-07-04) **— OR on-demand right after a session where Will actively worked multiple agents** (that's when the map drifts fastest). · **Trigger:** boot cadence-check (`scripts/sweeps_due.py`) + on-demand · **Registry:** `sweeps/REGISTRY.tsv` · **First run:** 2026-07-04.

**What it does:** keeps `FLEET_MAP.tsv` + `profiles/` honest by diffing each agent's **production** (commits + STATUS) since the last review — catching mis-grades (under- *or* over-rated), stale profile notes, resolved open-questions, and new/refined patterns. **Fully autonomous: it touches ONLY DAEDALUS's own map** (FLEET_MAP / profiles / PATTERNS) — no cross-agent mutation, so **no approval gate** (unlike the Staleness Sweep, which freezes others' surfaces). Enforces the design fact that an agent's maturity/notes **drift within hours of active work**, so the map is only trustworthy when re-diffed against real production (PAT-024 under-rating cuts both ways; PAT-029 the re-read IS the re-verification).

> **Why the on-demand trigger matters as much as the 14-day tick:** the map drifts by **WORK VOLUME, not calendar time.** Will, 2026-07-04: *"I've been working those specific agents this entire time — they moved very far from their status this morning."* A morning FLEET_MAP read was already stale by afternoon (the consume-loop). **Run this right after any heavy Will-active session, not only on the calendar.**

---

## Procedure

### 1. Detect (read-only)
> **Self-inclusion (2026-07-12, PAT-050):** DAEDALUS is IN SCOPE like any shipped agent — own FLEET_MAP row currency, own STATUS/EVOLUTION banner-truth, own cards/batch-doc dispositions, own outbox `delivered/` hygiene. The 7/12 self-sweep exists because the architect's surfaces rot in exactly the classes it polices; never skip self.
```bash
LAST="<last_run from REGISTRY>"
# the period's commits, newest first
git log --after="$LAST 00:00" --pretty=format:"%h | %cd | %s" --date=format:"%m-%d %H:%M"
# who shipped (agent-prefix tally)
git log --after="$LAST 00:00" --pretty=format:"%s" | sed -E 's/^([A-Z]+).*/\1/' | sort | uniq -c | sort -rn
# scripted L0-L2 floor (wired 2026-08-17, self-audit F10 — this scan previously had NO invocation
# site anywhere; run it here every review, diff hints against FLEET_MAP before step 2)
python3 "$(git rev-parse --show-toplevel)/AGENTS/DAEDALUS/scripts/maturity_scan.py"
```

### 2. Per active agent (shipped since last review): read the STATUS delta + key commits, assess via the maturity/structure lens
- Did it **clear or slip a gate?** (L-level change — PAT-024 under-rating is the common case; PAT-030 grade content-not-filename; don't over-grade mechanically — flag *confirm-read owed* if you didn't do a full firming.)
- Did a **profile open-question resolve**, or a **profile/row note go stale?**
- **Profile-trigger check (added 2026-07-12, self-sweep T3-1):** read the agent's `profiles/<AGENT>.md` **Staleness:** line and test the NAMED trigger against the period's commits/STATUS. Trigger fired → refresh the profile in this review (or banner it ⚠️ STALE w/ the fired trigger + a named checkpoint if the refresh can't happen now — the HAWK-banner pattern). The 7/12 self-sweep found 7/24 profiles past-due by their own named triggers because nothing checked them between ad-hoc firmings; this step is that checker.
- Did it surface a **new pattern**, or let me **reconcile an existing one?**
- Any **cross-agent thread** (something *another* agent should act on)?

### 3. Classify → disposition (all DAEDALUS-own-file → autonomous)
| Finding | Action |
|---|---|
| **Mis-grade** | re-grade the FLEET_MAP row (conf per depth of read; `confirm-read owed` if not a full firming) |
| **Row-gap marked RESOLVED** | **also stamp the originating card/assessment doc with a one-line closure, SAME pass** (7/22 self-sweep: the 7/12 fixbatch fixed the STOCK of record-lag; review-time resolutions re-seeded the FLOW — PAT-058) |
| **Stale note / resolved open-Q** | update the row / profile |
| **New or refined pattern** | `PATTERNS.tsv` |
| **Cross-agent observation** | **note it / route via `outbox/`** — never edit their files here |

### 3b. Coverage + check-register pass (added 2026-08-03 — the two cheapest steps in this playbook)

**Run the coverage doctor** — it is INFO-severity and roster-derived, so a review cadence is its correct home, not a boot step:
```
python3 "$(git rev-parse --show-toplevel)/scripts/lane_coverage_check.py"
```
It reads `PROME/ROSTER.md` at runtime, so it does **not** rot as the roster changes; its findings are coverage FACTS to relay (route to WALTER/PROME), never alarms to action here. **Why it lives here:** it was built 2026-07-16 and wired to nothing, so its findings sat unread for 18 days — including that both single-name bank specialists (OZK, WAL) have no autonomous lane, because *a spinout does not inherit one*. Any promotion or spinout since the last review is a reason to expect a new INFO row.

**Run the canon-conformance check** — finds docs that *prescribe* a command root canon forbids:
```
python3 "$(git rev-parse --show-toplevel)/scripts/canon_check.py"
```
Suppresses same-line prohibitions, historical/mail surfaces, dormant agents' docs, and any doc that forbids the command elsewhere in itself (a doc with a stance is explaining, not instructing). **Re-verify its `PROHIBITIONS` table against root `CLAUDE.md` § Git Protocol on this pass** — the table is a restatement of prose canon, so if canon adds a prohibition the table does not know.

**Review `CHECKS.tsv`** — every row's `Invoked_by` and `Last_verified_run`. Three questions, in order:
1. Did anything land in `scripts/` since the last review **without** a row? (a new check with no row is the register's own blind spot)
2. Is any row still `UNWIRED` that is not `MANUAL-BY-DESIGN`? **An UNWIRED load-bearing check is a finding, not a backlog item.**
3. Does any row's `Null_meaning` still describe behaviour the script no longer has? (a fixed check with a stale null-meaning is worse than no row — it certifies a guarantee that lapsed)

> ⚠️ **This step exists because the register would otherwise become the thing it measures.** `CHECKS.tsv` was created 2026-08-03 off the finding that two load-bearing checks had no invocation site; a register with no invocation site is the same defect wearing the auditor's badge. **The fix for an unwired check is almost never a new protocol step — it is attaching it to a step that already fires.** Adding steps is what produced the invocation problem; prefer folding into an existing conditional step, a sweep, or a harness hook (the only invocation model an agent cannot skip by forgetting).

### 4. Record
REGISTRY `last_run` + `last_findings`; the Run Log below; STATUS/EVOLUTION if material; PATTERNS if it taught something durable. **`CHECKS.tsv` rows touched this pass** (state changes, new rows, corrected null-meanings).

### 5. Regenerate the directory
After any FLEET_MAP row change, regenerate the readable fleet directory so it stays in sync with the source:
```
python3 "$(git rev-parse --show-toplevel)/AGENTS/DAEDALUS/scripts/render_directory.py"
```
`FLEET_DIRECTORY.md` is GENERATED (joins `PROME/ROSTER.md` + `FLEET_MAP.tsv`) — never hand-edit it; edit the sources then re-run. The script fails loud if ROSTER's format changes or a new FLEET_MAP agent is unhandled (add it to the SPECIAL map or DROP set). Also re-run whenever ROSTER's active/tier-2/dormant classification changes.

---

## Run Log
| Date | Who shipped | Map changes | Notes |
|---|---|---|---|
| 2026-08-17 | 20+ prefixes, 1,177 commits in 10d (PROME 309 · DAEDALUS 135 · WALTER 117 · BRENT 75 · SAM 59) | **Run #4 (on-demand, 4d early): NEXUS L4→L5 M · FERT L1→L2 H · 0 downgrades · 21 rows re-cut · VIOLET Conf H→M · CARL L5 DENIED (3 boot false-greens) · dark-desks = the period's governing fact (8 desks ≥5d) · PAT-112/113 · full record `upgrades/PRODUCTION_REVIEW_2026-08-17.md`** | First wired maturity_scan run; register passes (On_FAIL fill + Q1 catch) ran in-line; 2 of the reviewer's own same-day cells refuted and owned |
| 2026-08-07 | 30+ shippers / 1,766 commits — heaviest period on record | **Run #3 (9-reader fan-out): 3 promotions (VULCAN L2→L3 · WATT L2→L3 · FALCON L3→L4), 0 downgrades, 36 rows re-banked; LABOR L5 SUSTAINED; PAT-078..087 banked; full record `upgrades/PRODUCTION_REVIEW_2026-08-07.md`** *(row backfilled 2026-08-17, self-audit F18 — the run predated only the registry cell; this playbook log is the register-of-record and was missing the largest run)* |
| 2026-07-22 | EVERYONE — 30+ prefixes (PROME 275 · WALTER 110 · TERRY 59 · REGINALD 38 · +26 more) | **7 level moves:** WATT/VULCAN/OSPREY L1→L2 · MIDAS/FALCON L1→L3 · CORAL L2→L3 · TERRY L3→L4 (boot) + **OZK first-ever row L4** + NEXUS PROVISIONAL lifted + BOND conf M→H; 3 L5 promote-on-verify staged (BRENT/LABOR/VIOLET); 0 downgrades; HAWK sunset armed | Ran +4d over (7/18→7/22 — the slip = own L5 blocker). 6-reader cohort fan-out. PAT-051..057 banked (spawn-driver gap / build-vintage fossilization / frozen-frame grading standard+ledger-leg failure / consumer-mutated state / compress-regrow / packet-clears-debt-books / condition-cited banners). 12 profiles trigger-fired → bannered-w/-deltas per playbook path, 4-priority refresh-at-touch queue. KOSPI gap dispositioned 3-way. Routing: PROME spawn-flag bundle (VULCAN same-day, CARL POP 7/24, HOMER/WATT/AEOLUS/MIDAS/HAWK) + OZK & BROCK task packets. Full report: `upgrades/PRODUCTION_REVIEW_2026-07-22.md` |
| 2026-07-04 | WALTER 8 · CREED 8 · PROME 4 · (DAEDALUS 5) | **CREED L1→L2** (conf M, confirm-read owed — cleared the live-accruing-ledger gate via its native source-pack/thesis-rails, PAT-030) | Consume-loop rollout **resolved** (WALTER+PROME per-recipient: CARL drop+doctor-exempt / REGINALD keep+drain / SAM install / RED done / CREED drained) → **PAT-034 reconciled**; WALTER spine-lag + I3-kill-retract **self-resolved**; asymmetric-records class recurring + fleet-acknowledged ([[finding_asymmetric_records_need_reconciliation]], [[finding_complete_vs_selective_scan_drop_safe]]). Open thread: NEXUS intake lane not in the WALTER rollout scope (spec'd-ahead-of-wiring?). No other classification changes. |
