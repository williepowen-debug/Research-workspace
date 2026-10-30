# CHECK_STANDARD §10 retroactive leg: self-inclusion audit of DAEDALUS-authored mechanisms

**Run:** 2026-10-30, 12:26 to 12:45 EDT (`date`). **Auditor:** a read-only subagent working for DAEDALUS, not the owner; this file is its only write. **Rule:** `BLUEPRINTS/CHECK_STANDARD.md:89-94` (§10, PROVISIONAL). **Retroactive leg status before this run:** planned for 2026-08-28, never run (`CHECK_STANDARD.md:94`, SEARCH-NOT-FOUND 2026-10-28). This record is that leg.

**Author's own directory** means `AGENTS/DAEDALUS/` plus repo-root `scripts/` (granted to DAEDALUS 2026-07-31; `SURFACES.tsv` row `scripts/`).

**Verdict tokens:** the five tokens from the brief, plus one this run had to add. **NO-PERIMETER** marks a tool with no directory or fleet perimeter for §10 to bind: it works on the staged index, on paths the caller passes, on one fixed file, or on one named agent. It is not a pass, just a sign that §10 does not apply. "Vacuous" means the perimeter would include DAEDALUS, but DAEDALUS has no member of the scanned class.

---

## §0 Summary

| Population | Items | SELF-IN-DECLARED | SELF-EXCLUDED-DECLARED | SELF-SILENT-BUT-COVERS | SELF-SILENT | SCOPE-LINE-OMITS-SELF | NO-PERIMETER |
|---|---:|---:|---:|---:|---:|---:|---:|
| A: sweeps in `sweeps/REGISTRY.tsv` | 18 | 7 | 0 | 6 | 4 (1 excluded in fact, 2 vacuous) | 1 (latent) | 0 |
| B: DAEDALUS-owner rows in `CHECKS.tsv` | 48 | 7 | 2 | 7 | 3 (all vacuous) | 4 (all excluded in fact) | 25 |
| C: standing conventions | 4 | 2 | 0 | 2 | 0 | 0 | 0 |
| **Total** | **70** | **16** | **2** | **15** | **7** | **5** | **25** |

Of the 45 items where §10 applies, 18 state self in or out, 15 cover self without saying so, and 12 break the rule as written (7 silent, 5 scope lines that leave self out).

**Worst class: the author's directory is excluded in fact while the text claims fleet or registry coverage (5 instances)**

| # | Item | What it claims | What it actually covers | Evidence |
|---|---|---|---|---|
| W1 | `scripts/read_cap_check.py --fleet` | Header line `READ-CAP FLEET — … 41 active+tier-2 desks`. Root CLAUDE.md makes the read cap binding on every desk's whole-read surfaces | It parses only the `ACTIVE`/`TIER-2` sections of `FLEET_DIRECTORY.md` (`read_cap_check.py:162`). DAEDALUS sits under `## 🔵 SPECIAL` (`FLEET_DIRECTORY.md:70,74`), so it has no desk row in the 2026-10-30 fleet run. `validate_all` leg D1 inherits the gap. `READ_CAP.md:45` declares a fleet-sweep exclusion for sub-agents only, not for SPECIAL | Run 12:3x: 41 desk rows, no DAEDALUS row. Mitigation: the charter's step 9 runs `--agent DAEDALUS` at every closeout (today rc 0, `rotation_due=1`). Compare `corrections_boot_check.py:72`, which reads "all sections: active, tier-2, dormant, special" |
| W2 | `scripts/validate_all.py` | `perimeter AGENTS/DAEDALUS/CHECKS.tsv` (`validate_all.py:10`, `:1369`) | 9 A-legs, all repo-root selftests. None of the 13 `AGENTS/DAEDALUS/scripts/*` rows in CHECKS.tsv has a leg, and `NOT_CHECKED_V1` (`:730-735`) does not list them. Several have a quick `--selftest` (`dark_window_check`, `prose_remedy_candidates`, `walter_route_check`) | `validate_all.py --list` output, 2026-10-30 |
| W3 | Profile-refresh queue (`REGISTRY.tsv` row "fired triggers + missing profiles") and `profile_clock_check.py` | Perimeter `38 profile(s) attempted (includes retired)` | `profiles/DAEDALUS.md` does not exist. The checker globs `profiles/*.md` (`profile_clock_check.py:21`), so a missing profile never shows up, and the "missing profiles" leg never names DAEDALUS. Meanwhile DAEDALUS grades itself (FLEET_DIRECTORY row L4 M, scored 2026-10-28), although `UPGRADE_PROTOCOL.md:23` requires a profile "before any upgrade work" and `OPERATIONS.md:22` says the same before grading | `ls profiles/` output. Checker output, line 1 |
| W4 | `scripts/lane_coverage_check.py` | `34 ACTIVE roster agents, 6 synthesis-class excluded (HAWK, NEXUS, PROME, RED, TERRY, WALTER)` | Only ROSTER `## ACTIVE` is read (`:93-107`). DAEDALUS (ROSTER `## SPECIAL`, `ROSTER.md:155`) is excluded silently. The exclusion is substantively right, since DAEDALUS has no external domain to collect, but the line names six exclusions and not the author | Run 12:3x output, line 1. The row's owner cell is split: intake WALTER/PROME, surface DAEDALUS |
| W5 (latent) | Production Review §3b check-registry question 1 | "Did anything land in `scripts/` since the last review **without** a row?" (`PRODUCTION_REVIEW.md:57`) | It asks only about repo-root `scripts/`, yet the CHECKS.tsv scope (`CHECKS.tsv:4`) was widened on 2026-08-17 to cover agent-local checks with no boot invoker, starting with DAEDALUS's own. So no step looks for new rowless checks under `AGENTS/DAEDALUS/scripts/`. No confirmed miss today. `scorecard.py` and `coordination_scorecard.py` have no row, but they are renderers and nobody has ruled whether they qualify | Script list compared against CHECKS rows, 2026-10-30 |

Other §10 breaks, less severe: the PROME Sweep and the Wiring Sweep are both SELF-SILENT and not vacuous. The Wiring Sweep was the registered home of this very retroactive leg (`CHECK_STANDARD.md:94`) and its scope doc says nothing about self.

---

## §1 Per-item table

### Population A: sweeps (`sweeps/REGISTRY.tsv`, 18 rows)

| # | Registry row | Playbook | Verdict | Evidence (file:line, quoted) |
|---|---|---|---|---|
| A1 | Fleet Staleness Sweep | `sweeps/STALENESS_SWEEP.md` | SELF-IN-DECLARED | `:29` "**Self-inclusion (2026-07-12, PAT-050):** `AGENTS/DAEDALUS/` is IN SCOPE — check own ledger-class surfaces…". Also, `ledger_staleness.py --all` prints `perimeter [DAEDALUS]: 7 ledger(s) scanned; 18 TSV(s) NOT scanned` |
| A2 | Fleet Production Review | `sweeps/PRODUCTION_REVIEW.md` | SELF-IN-DECLARED | `:14` "DAEDALUS is IN SCOPE like any shipped agent — own FLEET_MAP row currency, own STATUS/EVOLUTION banner-truth…" |
| A3 | Falsification Freshness Sweep | `sweeps/FALSIFICATION_SWEEP.md` | SELF-IN-DECLARED | `:26` "**Self-inclusion (2026-07-12, PAT-050):** DAEDALUS is IN SCOPE — its 'falsification surfaces' = PATTERNS.tsv rows…". The script leg excludes DAEDALUS by class and says so (see B-row falsification_scan). The playbook gives the self leg to a manual read, last run 2026-10-08 (`:40`) |
| A4 | Harness Audit | `sweeps/HARNESS_AUDIT_SWEEP.md` | SELF-IN-DECLARED | `:11` "**Self-inclusion (PAT-050):** DAEDALUS's own CLAUDE.md SPAWN/closeout steps are in scope." The registry `last_run` is 2026-07-07 on a 90-day cadence, which is a separate overdue question |
| A5 | PROME Spine & Will-Facing Surfaces | `sweeps/PROME_SWEEP.md` | **SELF-SILENT** | `:9-18` scope section covers PROME surfaces only. The only DAEDALUS mention (`:20`) is DAEDALUS acting as verifier. Not vacuous: the sweep's own logic (an outside reader for a desk with no reader above it) applies to DAEDALUS too, and nothing says whether DAEDALUS's Will-facing outputs are in or out |
| A6 | Queue: check-registry | `PRODUCTION_REVIEW.md` §3b | **SCOPE-LINE-OMITS-SELF** (latent, W5) | `:57` "Did anything land in `scripts/` since the last review **without** a row?" Compare `CHECKS.tsv:4`, whose scope includes agent-local checks with no boot invoker |
| A7 | Queue: invocation-mapping | `PRODUCTION_REVIEW.md` §3b | SELF-SILENT-BUT-COVERS | `:56` "Review `CHECKS.tsv` — every row's `Invoked_by`…". 13 rows are `AGENTS/DAEDALUS/scripts/*` (CHECKS data rows 20-26, 28, 30, 38, 48-50), so self is reviewed |
| A8 | Queue: roster-health | `PRODUCTION_REVIEW.md` | SELF-IN-DECLARED | `:14` "own FLEET_MAP row currency". `sweeps_due.py:58` prints "SELF-ROW: DAEDALUS FLEET_MAP row Last_scored …" |
| A9 | Queue: shared-guard-standard | `BLUEPRINTS/STATE_VOCABULARY.md` | SELF-SILENT-BUT-COVERS | The playbook pointer is a registry, not a procedure, so this run has no scope text at all. Coverage is proved by `STATE_VOCABULARY.md:269` "## Class 15 — DAEDALUS register enums" and charter `CLAUDE.md:117` "STRICT text & state tokens — self-binding" |
| A10 | Queue: unwired-checks | `PRODUCTION_REVIEW.md` §3b | SELF-SILENT-BUT-COVERS | `:59` "Is any row still `UNWIRED`…". Same 13 DAEDALUS-local rows are in the register |
| A11 | Queue: profile-refresh | `UPGRADE_PROTOCOL.md` | **SELF-SILENT, excluded in fact** (W3) | `UPGRADE_PROTOCOL.md:23` "Before any upgrade work, build (or refresh) the agent's **Profile** — `profiles/<AGENT>.md`". No `profiles/DAEDALUS.md`. The queue's "missing profiles" leg never names DAEDALUS |
| A12 | Queue: surfaces-currency | `PRODUCTION_REVIEW.md` | SELF-SILENT-BUT-COVERS | `SURFACES.tsv` row `scripts/ DAEDALUS`, so the author's non-agent surface is a row |
| A13 | Queue: doc-retirement | `sweeps/STALENESS_SWEEP.md` | SELF-IN-DECLARED | Covered by playbook-wide `:29`. Run log `:73` (2026-10-21) records the "retirement/self" mode |
| A14 | Wiring Sweep | `sweeps/WIRING_SWEEP.md` | **SELF-SILENT** | `:1-20` scope doc and leg ① ("R1 generic boot-leg wiring across ~30 boot surfaces") never enumerate surfaces or say whether DAEDALUS is in or out. This is the sweep that `CHECK_STANDARD.md:94` assigned the §10 retroactive leg to |
| A15 | Registered-Gate Basis Sweep | `sweeps/GATE_BASIS_SWEEP.md` | SELF-SILENT-BUT-COVERS (vacuous) | `:9` "Every gate in `PROME/GATES.tsv` (LIVE + FIRED-pending rows)…". No GATES row has DAEDALUS as owner (the 8 grep hits are prose mentions), so any future DAEDALUS gate would fall in scope |
| A16 | Coordination scorecard weekly render | `design/2026-08-28_coordination_scorecard_v1.md` | SELF-SILENT-BUT-COVERS | `:9` "**Perimeter stated** (CHECK_STANDARD §2): which ORCH_LOG rows…" with no self clause. Proved: `scorecards/2026-10-30.md:327` "\| DAEDALUS \| 19 \| 14 \| 91 …". ORCH_LOG has 21 DAEDALUS rows |
| A17 | Prose-Remedy Census | `sweeps/PROSE_REMEDY_SWEEP.md` | SELF-IN-DECLARED | `:8` "## Perimeter (self-inclusion: DAEDALUS IN scope)". Code: `prose_remedy_candidates.py:37` `SPECIAL_IN = ["DAEDALUS", "RAV"]`, perimeter check `:151-153` |
| A18 | H2 As-made confidence audit (one-time) | `runs/2026-09-07_H2_ASMADE_AUDIT_fleet.md` | SELF-SILENT (vacuous) | `:1-23`: subject is "11 desks seeded 2026-03-04" prediction ledgers. DAEDALUS has no prediction ledger |

### Population B: DAEDALUS-owner rows in `CHECKS.tsv` (48 rows; the one non-DAEDALUS row in that block, `AGENTS/BROCK/scripts/brock_selfcheck.py`, is excluded)

| # | Check | Verdict | Evidence |
|---|---|---|---|
| B1 | `scripts/read_cap_check.py` (fleet tool) | **SCOPE-LINE-OMITS-SELF, excluded in fact** (W1) | `:162` section filter `"ACTIVE" in section or "TIER-2" in section`. `:1973` prints "{n} active+tier-2 desks". No DAEDALUS desk row in the fleet output. `--agent DAEDALUS` works and is run at closeout (charter step 9) |
| B2 | `scripts/validate_all.py` | **SCOPE-LINE-OMITS-SELF, excluded in fact** (W2) | `:10` "Its perimeter is `AGENTS/DAEDALUS/CHECKS.tsv`". `--list`: legs A1-A9 cover root scripts only, with no `AGENTS/DAEDALUS/scripts` leg. `:730` NOT_CHECKED_V1 omits them |
| B3 | `AGENTS/DAEDALUS/scripts/profile_clock_check.py` | **SCOPE-LINE-OMITS-SELF, excluded in fact** (W3) | Output line 1: "PROFILE-CLOCK perimeter as-of 2026-10-30: 38 profile(s) attempted (includes retired)". No DAEDALUS profile exists, and absence is not reported. (Output lines naming DAEDALUS show it as the remedy owner, not as a subject) |
| B4 | `scripts/lane_coverage_check.py` | **SCOPE-LINE-OMITS-SELF, excluded in fact** (W4, reason valid but unstated) | Output line 1: "34 ACTIVE roster agents, 6 synthesis-class excluded (HAWK, NEXUS, PROME, RED, TERRY, WALTER)". `:38-50` SYNTHESIS_EXCLUDE has no DAEDALUS, because ACTIVE-only parsing already drops it |
| B5 | `AGENTS/DAEDALUS/scripts/calendar_docket_coverage.py` | SELF-IN-DECLARED | `--help`: "Default includes DAEDALUS; explicit --ledger narrows scope and prints that fact." Output line 2: "PERIMETER: [...] DAEDALUS included by default" |
| B6 | `AGENTS/DAEDALUS/scripts/prose_remedy_candidates.py` | SELF-IN-DECLARED | `:16` "(DAEDALUS, RAV)", `:37` SPECIAL_IN, `:153` "R6 perimeter: … DAEDALUS+RAV+PROME in" |
| B7 | `AGENTS/DAEDALUS/scripts/sweeps_due.py` | SELF-IN-DECLARED | `:58` "SELF-ROW: DAEDALUS FLEET_MAP row Last_scored …" |
| B8 | `AGENTS/DAEDALUS/scripts/complete_check.py` | SELF-IN-DECLARED (self by construction) | `:2-5` "did the work this session CLAIMED actually get done? … behind my own 'closed'" |
| B9 | `AGENTS/DAEDALUS/scripts/read_cap_check.py` (local) | SELF-IN-DECLARED (self by construction) | `:4` "DAEDALUS's STATUS byte budget…". It checks DAEDALUS's own file list |
| B10 | `AGENTS/DAEDALUS/scripts/regen_patterns_hot.py` | SELF-IN-DECLARED (self by construction) | `:2` "regenerate PATTERNS_HOT.md from PATTERNS.tsv" (DAEDALUS's own files) |
| B11 | `scripts/ledger_staleness.py` | SELF-IN-DECLARED (perimeter line names self) | `--all` output: "perimeter [DAEDALUS]: 7 ledger(s) scanned; 18 TSV(s) NOT scanned by this pass…" |
| B12 | `scripts/consumer_check.py` | SELF-EXCLUDED-DECLARED (accepted, reason given and a self mode exists) | `:967` "--agent … excludes AGENTS/<NAME>/ from the scan". `:979-1023` `--self` "scans AGENTS/<NAME>/ and nothing else". `:476` mirror-map mode is "self-INCLUSIVE". Root CLAUDE.md step 1c mandates the `--self` run |
| B13 | `AGENTS/DAEDALUS/scripts/falsification_scan.py` | SELF-EXCLUDED-DECLARED (accepted, class reason) | Output `:27` "No thesis-class file, non-Market — falsification not applicable (8): BARON, CATO, DAEDALUS, …". The playbook self leg (A3) covers what the script cannot |
| B14 | `AGENTS/DAEDALUS/scripts/maturity_scan.py` | SELF-SILENT-BUT-COVERS | The header "40 agents" has no self clause. Output `:38` "\| DAEDALUS \| Meta \| L2 \| L4? ⚠needs-read \| 258 \| — \|" |
| B15 | `AGENTS/DAEDALUS/scripts/render_directory.py` | SELF-SILENT-BUT-COVERS | It renders the SPECIAL section. `FLEET_DIRECTORY.md:74` "\| DAEDALUS \| Meta \| L4 \| M \| 2026-10-28 …" |
| B16 | `scripts/canon_check.py` | SELF-SILENT-BUT-COVERS | Header "(7023 doc(s) searched…)" has no self clause. Output `:3` flags "AGENTS/DAEDALUS/profiles/REFRESH_2026-09-17_VERIFY_P3_SAM_SHADE.md:313" |
| B17 | `scripts/wiring_census.py` | SELF-SILENT-BUT-COVERS | `--all` output `:88` "[DAEDALUS] scripts: AGENTS/DAEDALUS/scripts/daedalus_gate.py, …" |
| B18 | `AGENTS/DAEDALUS/scripts/walter_route_check.py` | SELF-SILENT-BUT-COVERS | `:134-139` iterates every `AGENTS/*` dir not starting with `_`, `CANON_NAMES` (`:101`) includes `CLAUDE.md`, and `AGENTS/DAEDALUS/CLAUDE.md` exists. Output gives counts only ("189 CORRECT"), so DAEDALUS is never named |
| B19 | `scripts/firetime_check.py` | SELF-SILENT-BUT-COVERS | `:14`, `:45` read every row of `PROME/DOCKET.tsv` regardless of owner, so DAEDALUS-owned rows are in |
| B20 | `scripts/corrections_boot_check.py` | SELF-SILENT-BUT-COVERS | `:72` "Every agent named in the generated FLEET_DIRECTORY.md (all sections: active, tier-2, dormant, special)". Charter step 5b runs it on DAEDALUS |
| B21 | `AGENTS/DAEDALUS/scripts/dark_window_check.py` | SELF-SILENT (vacuous) | Output line 1 "32 desk(s) holding a live test". The perimeter is `scorecards/LEDGERS.tsv` plus GATES (`:10`), and DAEDALUS has neither |
| B22 | `scripts/brief_pin_check.py` | SELF-SILENT (vacuous) | `:16` "Per brief (AGENTS/<D>/NEXUS_BRIEF.md)". There is no `AGENTS/DAEDALUS/NEXUS_BRIEF.md` |
| B23 | `scripts/asmade_audit.py` | SELF-SILENT (vacuous, source only) | Subject is seeded prediction ledgers (A18). `--all-seeded` did not finish in 90 s, so it was not observed |
| B24-B48 | `safe-push.sh`, `orphan_check.sh`, `memory_index_check.py`, `claim_check.py`, `position_agreement_check.py`, `env_doctor.py`, `session_banner.sh`, `check_memory_length.sh`, `gen_automemory_index.py`, `link_automemory.sh`, `tsv_append.py`, `market.py`, `archive/SENTRY_pipeline/fetch_feeds.py`, `memory_citation_census.py`, `docket_view.py`, `orch_log.py`, `pipeline_rc_guard.py`, `account_guard.py`, `orch_time.py`, `install-git-hooks.sh`, `install-claude-hooks.py`, `githooks/pre-commit`, `githooks/commit-msg`, `githooks/pre-push`, `AGENTS/DAEDALUS/scripts/verify_push.sh` | NO-PERIMETER (25) | Each works on the staged index or commit (`pre-commit:2-4`, `account_guard.py:1-5`, `commit-msg`, `pre-push`), on paths or one agent the caller names (`claim_check`, `orphan_check.sh:17`, `corrections`-style), on one fixed shared file (`check_memory_length`, `memory_index_check`, `memory_citation_census`, `gen_automemory_index`), on PROME ledgers (`docket_view`, `orch_log`, `orch_time`), on FORGE (`position_agreement_check`), on the box (`env_doctor` prints its own perimeter line without directories), or on pushes (`safe-push`, `verify_push`). None of them carves out a directory |

### Population C: standing conventions (4)

| # | Convention | Verdict | Evidence |
|---|---|---|---|
| C1 | `BLUEPRINTS/READ_CAP.md` | SELF-SILENT-BUT-COVERS (with the W1 caveat) | `:38` "`STATUS.md` \| **Yes, every desk**". Charter OUTPUT RULES applies 32,550 B to DAEDALUS's own STATUS. But the instrument section (`:54`) and the exclusion table (`:45`, sub-agents only) do not say that the fleet sweep skips SPECIAL desks, including the author |
| C2 | `BLUEPRINTS/STRICT_TEXT.md` | SELF-SILENT-BUT-COVERS | `:7-12` scope is by surface class (ACTION/ASK lines, script output, gate specs), with no directory carve-out. Self-binding is stated only in the charter (`CLAUDE.md:117` "STRICT text & state tokens — self-binding (PAT-075…)"), not in the artifact |
| C3 | `BLUEPRINTS/STATE_VOCABULARY.md` | SELF-IN-DECLARED | `:269` "## Class 15 — DAEDALUS register enums (pointer class, added 2026-10-28…)". The scope line `:11` itself is silent on self |
| C4 | Closeout battery (`scripts/daedalus_gate.py closeout`) | SELF-IN-DECLARED | `:2` "thin runner over DAEDALUS's EXISTING boot / closeout / post-push checks". `:328` C7 "read_cap_check --agent DAEDALUS". Spec `design/2026-09-17_DAEDALUS_GATE_SPEC.md:33` fingerprint covers `AGENTS/DAEDALUS scripts` |

---

## §2 Proposed fixes (proposals only; nothing here has been applied)

1. `scripts/read_cap_check.py` (`:162` and the `:1973` header): parse the `SPECIAL` section too, or print "SPECIAL desks (DAEDALUS, RAV, CATO) NOT in fleet perimeter — DAEDALUS covered by its closeout `--agent DAEDALUS`" in the fleet header.
2. `BLUEPRINTS/READ_CAP.md`, next to `:45`: add the row "A SPECIAL desk (DAEDALUS) — Yes, the rule binds; the FLEET SWEEP (`--fleet`) does not reach it today; covered by the owner's closeout `--agent` run."
3. `scripts/validate_all.py`: add to `NOT_CHECKED_V1` "agent-local CHECKS.tsv rows (13 under AGENTS/DAEDALUS/scripts/) — no leg in v1", or add `--selftest` legs for `dark_window_check`, `prose_remedy_candidates` and `walter_route_check`.
4. `AGENTS/DAEDALUS/scripts/profile_clock_check.py`, perimeter line: add "agents in FLEET_DIRECTORY with NO profile: <list>, DAEDALUS included".
5. `UPGRADE_PROTOCOL.md` (profile-refresh queue): add "DAEDALUS is IN scope: `profiles/DAEDALUS.md` is owed before the next self-grade, or the self-row is declared profile-exempt with a reason."
6. `sweeps/PRODUCTION_REVIEW.md:57`: change to "Did anything land in `scripts/` **or in an agent-local `scripts/`/`tools/` (DAEDALUS's own included) without a boot invoker** since the last review without a row?"
7. `scripts/lane_coverage_check.py`, header print: add "SPECIAL desks (DAEDALUS, RAV, CATO) not scanned: no external domain lane."
8. `sweeps/PROME_SWEEP.md`, scope section: add "Self-inclusion (§10): DAEDALUS's own Will-facing outputs are OUT of this sweep (it reads PROME's) and are covered by <named mechanism>", or declare them IN.
9. `sweeps/WIRING_SWEEP.md`, header: add "Self-inclusion (§10): DAEDALUS's own boot/closeout surfaces are IN scope of every leg unless the leg says otherwise", and record this run as the §10 retroactive leg's run record.
10. `AGENTS/DAEDALUS/scripts/maturity_scan.py`, `render_directory.py`, `canon_check.py`, `wiring_census.py`, `walter_route_check.py`: add "(DAEDALUS included)" to each tool's perimeter or header line, so coverage is stated instead of inferred.
11. `AGENTS/DAEDALUS/scripts/dark_window_check.py`, `scripts/brief_pin_check.py`, `scripts/asmade_audit.py`: add one docstring line each saying "DAEDALUS IN scope; vacuous today (no registered ledger / brief / seeded ledger)".
12. `BLUEPRINTS/STRICT_TEXT.md:7`: add "The author (DAEDALUS) is bound like any desk (self-binding, charter OUTPUT RULES)."
13. `design/2026-08-28_coordination_scorecard_v1.md:9`: add "DAEDALUS (the renderer) is IN the per-desk perimeter."
14. `BLUEPRINTS/CHECK_STANDARD.md:94`: replace SEARCH-NOT-FOUND with a pointer to this run record, after the owner has reviewed it.

---

## §3 Limits

- **Reading depth:** I read the playbooks' scope and perimeter sections and grepped for self-inclusion wording. I did not read playbooks whole. `WIRING_SWEEP.md` (42 KB) and `STATE_VOCABULARY.md` (41 KB) were read in part, and a self statement deeper in either would change A14 or C3.
- **Scripts:** most B verdicts come from targeted grep of the source and the `--help` docstring, not whole-file reads. NO-PERIMETER calls rest on headers and docstrings.
- **Runs:** these were run read-only at 12:28-12:40 EDT: `maturity_scan`, `falsification_scan`, `walter_route_check`, `profile_clock_check`, `lane_coverage_check`, `canon_check`, `wiring_census --all`, `brief_pin_check`, `dark_window_check`, `calendar_docket_coverage`, `ledger_staleness --all`, `sweeps_due`, `memory_citation_census`, `read_cap_check --fleet`, `read_cap_check --agent DAEDALUS`, `validate_all --list`, `complete_check`, `env_doctor`. Some of them ignored `--help` and ran in default mode. Afterwards `git status` showed no tracked change and no new file from these runs. The untracked `runs/2026-10-30_WAL_REFRESH_READERS/` and `runs/2026-10-30_WIRING_SWEEP_17_*` belong to another session. Outputs were saved to the session scratchpad only.
- **Not run:** `asmade_audit --all-seeded` (stopped at 90 s), every `--selftest`, `pipeline_rc_guard` (hook mode), `safe-push`, the install scripts and the githooks.
- **Ownership:** the population is the owner cell in CHECKS.tsv. For rows whose cell reads "DAEDALUS (surface)", DAEDALUS maintains the script but did not necessarily write it (for example `consumer_check` was authored by HENRY and `lane_coverage_check` belongs to the WALTER/PROME intake). §10 binds the author, so W4 especially may belong to another owner.
- **Profile requirement:** whether DAEDALUS should have a profile at all (W3) is a design question. This audit only records that no scope text settles it either way.
- **§10 status:** §10 is PROVISIONAL (`CHECK_STANDARD.md:89`). Its canon (`:91`) says "Every **new** sweep…", and existing mechanisms are reached only through the Retroactive leg (`:94`), which is this run. So the items above are retroactive findings for the owner to dispose of, not breaches at build time. §10 has no forward-only or next-edit clause of its own (I checked `:89-95`).

**Completed:** 12:45 EDT 2026-10-30.
