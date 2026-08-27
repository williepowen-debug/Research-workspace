# BLUEPRINT — Utility-Agent

**Owner:** DAEDALUS · **Status:** 🟢 ACTIVE (built + activated 2026-06-28, Will + PROME approved) — the *sole* grading standard for utility agents. *(The former `templates/CLAUDE_TEMPLATE.md` was deleted by Will 2026-06-30, commit `58c30516`; the redirect-cleanup follow-up is therefore moot.)*
**Assembled best-of-breed from** `BEST_PRACTICES.md` (the 2026-06-27 fleet harvest). Composed, not cloned.
**Use for:** agents that produce a **service the fleet consumes**, not a market thesis — **WALTER, NEXUS, RED, TERRY, ORACLE, YEYOU.** Not market (owns a thesis → `market-agent.md`); not meta (authority to *change* the system's structure → `meta-agent.md`). *(Class discriminator at the bottom.)*

> **Governing principle — THIN FLOOR + ROLE CEILING (PAT-015 + the DARWIN lesson, PAT-001).** This blueprint exists *because* forcing market machinery (KB/VX/convergence-matrix/TRADE.md) onto a non-market agent produces dead, never-filled files and kills it (DARWIN). So it is a **thin shared floor** every utility agent meets + a **role-specific ceiling** that varies by agent. It **GRADES; it does not MANDATE** — never bolt machinery onto RED/TERRY/ORACLE to hit an L-number. Edits off it stay *encode-existing-handles-only*.

---

## THE SPINE — the OUTPUT-CONSUMPTION CONTRACT (lead here, not the L-labels)

A utility agent's whole reason to exist is an output other agents consume. The ONE thing this blueprint standardizes — **uniformly, across every utility agent** — so PROME and the fleet can see it *without spawning the agent*:

**Every utility agent carries a CONTRACT block** (in `CLAUDE.md` or `STATUS.md`), three lines:
- **PRODUCES** — the named artifact/service (a routing disposition + BOARD; a `NEXUS_BRIEF`; a steelman + honest odds; a trade construction; a probability read; a review verdict).
- **CONSUMED BY** — which agents / Will, via which surface (the brief, an inbox, the board, the digest).
- **PROOF OF CONSUMPTION** — evidence it was actually received & used: telemetry (WALTER's `produced ≠ received ≠ consumed`), a consumer citing it, a `board_log`/ledger row. **Absence of proof IS the gap.**

> **Refinement — the gate must not recreate the false-negative it exists to prevent (PAT-028).** Some utility output is consumed *informally*, with no ledger row possible — RED's steelman shifts a decision, TERRY's construction gets traded. **Qualitative proof counts** (a consumer citing it; a decision that visibly moved). Where consumption is genuinely *un-instrumentable*, that is a **structural-ceiling NOTE, not a fix-it debt** — do NOT grade the agent down for telemetry it cannot have. Apply this blueprint's own anti-DARWIN logic to its own L4 gate.

This is the **L4 gate** *and* the payoff: uniform coordination visibility is the load-bearing knowledge for the coordinator. Accurate grading is a byproduct — lead with the contract, not the level.

---

## REQUIRED SECTIONS — the shared FLOOR (every utility agent)

1. **Header + IDENTITY** — class (Utility), the role it owns, a "where it sits / no-overlap" table, the `File > verbal` rule.
2. **THE CONTRACT** — produces / consumed-by / proof-of-consumption (above). *The defining handle.*
3. **Role rubric** — the explicit, consistently-applied criteria for its function. *(L3 gate: "rubric applied consistently.")*
4. **Structured record (logging)** — a valid, accruing, **class-aware** record of what it did (NOT KB/VX/FLOW). *(L2 floor, PAT-008.)*
5. **Standing disciplines** — **interpreter-proof tool invocations (PAT-103, propagated 2026-08-17 — venv-only deps behind a bare-`python3` recipe: fix at the tool via self re-exec)** + **check/tool output contracts per `BLUEPRINTS/CHECK_STANDARD.md` §1–§11** *(cite added 2026-08-17, self-audit F12)* + boot↔closeout symmetry + 3-col Δ-discipline (`metric · Δ signed pp · last-updated`) + the role's anti-bias rule + **cwd-proof boot invocations** (every runnable boot/closeout command self-locates via `"$(git rev-parse --show-toplevel)"`, never a bare root- or own-dir-relative path that depends on the incidental launch cwd — PAT-031) + **git = cite-don't-restate** (git text = pointer to root `CLAUDE.md §Git Protocol` + own pathspec + exceptions only; local recipe copies drift — harness-audit S2, 2026-07-08) + **durable cadence home for every recurring tool** (a recurring script ships with its cadence wired one durability class above the session that created it, same session — boot step or registry row, never only SCRATCH/STATUS prose or a docstring; test: "where does the NEXT session learn to run this?" — PAT-040/PAT-041) + **structured-record staleness two-state** (each accruing record file is either LIVE with a boot-time staleness alert — where the record is TSV-shaped, wire a cwd-proof `scripts/ledger_staleness.py <NAME> --quiet` boot line — or dead with a FROZEN-vocabulary banner (FROZEN/RETIRED/NOT CURRENT/DO NOT CITE/NOT MAINTAINED/ARCHIVED); never the silent-rot middle. No `--trade` leg — utility agents hold no TRADE.md by design. PAT-023/PAT-035; utility parity added 2026-07-10) + **two-clock freshness headers on LIVE accruing records** (`# LIVE — Last real data refresh: <d1> | Staleness sweep (no data): <d2> | Next: <checkpoint>` — the data clock and the hygiene clock are separate; a hygiene pass must not be able to launder freshness. PAT-044, baked 2026-07-12; enforcement loop closed 2026-07-22 — `ledger_staleness.py` now parses the header and prefers it over git time) + **ledger-append hardening** (shell-appends to load-bearing TSVs only via `scripts/tsv_append.py` fields-as-argv or Python, never bare `printf`/`echo` — the `%`-in-market-text corruption class hit WALTER kill_log 7/19 + LABOR board_log 7/20; doctors run `--check` column-count lint) + **⚡ SPAWNED-MODE BOOT CARD** (top of CLAUDE.md, ~5 lines, shape per market-agent §8: repo-root-relative read list · one critical-semantics warning · git discipline w/ no-push-when-spawned · deliver-before-idle BOTH halves · domain drift gate; bodies stay per-agent — utility agents get coordinator-spawned too; WALTER excluded per its own spec) + **controlled state tokens & STRICT text** (NEW state-bearing surfaces use `BLUEPRINTS/STATE_VOCABULARY.md` canonical tokens; cost-bearing text — packet ACTION lines, script messages, rubric/gate specs — follows `BLUEPRINTS/STRICT_TEXT.md`; floor-not-ceiling, prose out of scope — PAT-075, 2026-07-31) + **R1 corrections boot leg (REQUIRED fleet-wide, FORUM-6 ①)** — cwd-proof boot line `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" <NAME>`; NAMED register rows BLOCK until receipted to the desk's own `registry/corrections_receipts.tsv`, ALL rows WARN, unparseable date = rc=2 (full contract → market-agent.md's R1 bullet; cite, don't restate) + **cross-session messaging = cite, don't restate** (before first use of harness `SendMessage`/`ListAgents` between independently-launched sessions, read `MESSAGING/CROSS_SESSION_MESSAGING.md` + `PROME/ORCHESTRATION_PLAYBOOK.md` §Cross-session; core: messages carry coordination, artifacts carry content · verify peer claims at artifacts · a relayed operator word never clears a Will-gated surface · never route signals around WALTER; teams-mode spawns out of scope, deliver-before-idle unchanged — Will-ruled 2026-08-16, open p2p + rule 3 ratified).
6. **Cross-agent routing** — standing route-matrix + `NEXUS_BRIEF` writeback + crisis-only outbox. *(Utility agents are defined by routing.)*
7. **AUTHORITY & SAFETY** — *only if it has cross-fleet write power.* State the guards (permission + idle, batched) — **or** state the read-only boundary explicitly (YEYOU: *flag, never fix*).
8. **BOTTOM LINE** — required; STATUS under the agent's **DECLARED** line cap **+ the byte tier beside it (Will-ratified 2026-08-17 — full form: market-agent.md §BOTTOM LINE; ≥75% of byte budget ⇒ rotate verbatim+crc to archive until <70%)**. *(Sharpened 2026-08-21, YEY-004: "under the agent's line cap" is VACUOUSLY satisfied by an agent that never declared one — TERRY measured 588 lines / 240,882 B with no cap in its charter, the fleet's largest STATUS, invisible to this line as previously written. The cap and the byte budget are NUMBERS NAMED in the agent's own charter or STATUS header; an undeclared cap is the gap, not a smaller cap.)*

### WHAT IT DOES NOT GET — the DARWIN guard
**No convergence matrix · no TRADE.md · no thesis-predictions ledger.** Those are market constructs; forcing them produces dead files. The utility analogue of "predictions resolving" is a **role-calibration loop** (below), not a market ledger.

---

## ROLE-SPECIFIC CEILING (varies by agent — do NOT mandate across roles)

The floor above is shared; the ceiling is per-role. Each agent's rubric, output, and calibration loop are its own:

| Agent | Role | PRODUCES | Role rubric | Calibration loop |
|---|---|---|---|---|
| **WALTER** | signal/news routing | dispatch+kill dispositions + BOARD | KILL/DISPATCH rules; read full body before KILL (no-kill-on-lede) | `delivered_but_unconsumed` telemetry |
| **NEXUS** | cross-agent synthesis | **the synthesis** (convergence matrix + antecedent map + narrative gap + prob-split) + owns the `NEXUS_BRIEF` *schema/template* — ⚠️ the per-agent `NEXUS_BRIEF.md` files are **INPUTS** NEXUS consumes, NOT its output | independence re-test; citation-vs-observation guard | brief vs peer-brief diff; mined-edges |
| **RED** | adversarial review | strongest steelman → honest odds | lead with the strongest bull case, *then* odds | steelman / odds hit-rate |
| **TERRY** | trade construction | trade structures + tooling (`grade_print`/`chain_fetch`) | construction rubric; live-chain marks | realized vs constructed |
| **ORACLE** | prediction-market diagnostics | probability reads / `NEXUS_BRIEF` | crowd-signal weighting; thin-liquidity discipline | Brier scoreboard |
| **YEYOU** | per-push conformance review | review verdicts/flags + finding ledger | the REVIEW_CHECKLIST; flag-never-fix; escalation budget | flag accuracy / false-positive rate |

*The calibration column is the role's truth-loop — the utility analogue of a market predictions ledger. Build it to the role's cadence; never force a market shape.*

> **Forum-4 canon (Will-ratified 2026-08-11) binds utility outputs too:** **N3** reference-discipline bundle (any published comparison — ≥2 references, same-variable percentiles, commensurability, epoch+sample-with-reason) and **N7** defect-register-travels-at-grade-time (any graded label ships with its append-only register). Canonical mirror text → `market-agent.md` §3/§5; cite, don't restate. **N5** (futures-bar/capture-time) is WALTER-owned — `SIG-W-20260811-002` **at v1.1 (2026-08-13)**; version moves in the same touch when WALTER bumps N5.

---

## CLASS DISCRIMINATOR (resolves meta-vs-utility — PAT-027)

The subject being "the system" does **not** make an agent meta — WALTER and NEXUS act on the fleet too. The discriminator is **authority to change the system's structure:**
- **Meta** (→ `meta-agent.md`): authority to *mutate* the system — build/edit/retire agents (DAEDALUS); orchestrate/task/prioritize (PROME).
- **Utility** (→ here): produces a *consumed service/output*, **no structure-mutation authority.**

**YEYOU → Utility** (resolved 2026-06-28): it produces review verdicts consumed by PROME (+ agents in Phase 2), is read-only ("flag, never fix; never the final word"), and holds no authority to change structure. It is the per-push analogue of RED (which is utility). *(YEYOU's own "meta-agent exemptions" note means "non-market exemptions" — they apply to every utility agent.)*

---

## MATURITY CEILING (per `SPEC.md §5`)
**L3** role rubric applied consistently · **L4** output consumed by others (the CONTRACT proven — *qualitative proof counts; un-instrumentable consumption is a ceiling NOTE, not a debt, PAT-028*) · **L5** clean closeouts, zero YEYOU flags (**waivable-when-dormant** — Will 7/22, SPEC §5; this variant missed the 7/22 encode while holding the unblocked candidate WALTER — fixed 2026-08-17, self-audit F24), current. Floor L0–L2 universal (skeleton → live STATUS+BOTTOM LINE → accruing structured record). **Adjudication form (Will-ruled 2026-08-20): every ladder leg gets a per-leg verdict row (PASS / FAIL / WAIVED-cite / NOT-ADJUDICATED) at grade time — canonical text in `UPGRADE_PROTOCOL.md` §Review method rule 2.**

## SOURCING (best-of-breed)
WALTER (delivery infra + telemetry, exemplar) · NEXUS (synthesis disciplines + independence) · RED (adversarial structure) · YEYOU (severity scale + escalation budget + ledger) · ORACLE (boot↔closeout + calibration). No single agent is the whole standard.
