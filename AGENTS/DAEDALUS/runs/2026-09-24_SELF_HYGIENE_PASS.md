# 2026-09-24 — DAEDALUS self-hygiene pass (CHECKS · SURFACES · doc retirement · upgrades/ banners)

**By:** DAEDALUS maintenance subagent (teams-mode, lead = DAEDALUS) · **Perimeter:** `AGENTS/DAEDALUS/` only · **Git:** the only mutating git command run was `git mv` (Task 3). Nothing was committed. The renames are **STAGED in the shared index**, so the lead must commit them by explicit pathspec, naming both the old and the new paths. A no-pathspec commit would sweep them (root 4c).
**Scratchpad:** `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-DAEDALUS/23c86d4b-580a-416e-8271-107104870b83/scratchpad/self-hygiene/` holds pre-edit copies of `CHECKS.tsv`, `CHECKS_HISTORY.tsv` and `SURFACES.tsv`, the two edit scripts, and the Task-4 file lists.
**Source:** `runs/2026-09-24_STALENESS_SWEEP_05.md` §0b/§5/§6/§9 (self-scope items).

## Files changed or moved

| File | Change |
|---|---|
| `CHECKS.tsv` | 9 rows updated, 1 row added (`walter_route_check.py`). Width is 10 cells on all 38 rows (header + 37 data). Size 69,570 → 69,247 B |
| `CHECKS_HISTORY.tsv` | +38 verbatim rotated cells (check · column · 2026-09-24 · old text) |
| `SURFACES.tsv` | all 13 rows re-reviewed. Width is 8 cells on all 14 rows. Size 19,849 → 11,262 B |
| `SURFACES_HISTORY.tsv` | **NEW**, in the same form as CHECKS_HISTORY: 44 verbatim rotated cells. Created because no history home existed, and replacing cells without one would have deleted their content |
| `archive/retired_2026-09-24/` (7 files, `git mv` + banner) | BATCH_01_handles · NEXUS_CARD · CORAL_S8_PROPOSAL · UTILITY_FIRMING_2026-07-03 · TRADE_STALENESS_SWEEP · LABOR_CARD · LABOR_GAP_ASSESSMENT_2026-07-10 |
| `outbox/delivered/` (2 files, `git mv`) | `2026-09-02_to-PROME_WQ-163-item1-RULING-…` · `2026-09-02_to-PROME_inbox-drained-9-items-…` |
| `upgrades/` (23 files, +2 lines each, body untouched) | STATUS banner (Task 4 table) |
| this record | new |

## TASK 1 — CHECKS.tsv currency

Method: I read each build record and quoted its figures. I also **re-ran every selftest read-only this pass**, and each matched its record: docket_view 26/26 · validate_all 42/42 · pipeline_rc_guard 85/85 · corrections_boot_check 18/18 · read_cap_check 101/101 · market 14/14 · walter_route_check rc 0. `render_directory.py --check` ran live: rc 0, "would change: no", md5 unchanged. `corrections_boot_check --coverage` returned 38/38 = 100%. PROME's wrapper `pipeline_rc_block.py --selftest` returned 34/36 rc 1, as the v4 record predicts. Replaced cells went to CHECKS_HISTORY.tsv verbatim.

| Row | What is true now (cells changed) |
|---|---|
| `scripts/safe-push.sh` | Null/Last/Gap/Notes: every message is rc-labelled; wording-only edit; **not yet run end-to-end** (the build could not fetch) |
| `scripts/market.py` | Null/Last/Gap/Notes: ⚠prev-close/⚠stale/⚠no-asof tags; `--selftest` 14/14; weekend ⚠stale is expected |
| `AGENTS/DAEDALUS/scripts/render_directory.py` | Null/Last/Gap/Notes: `--check` never writes and returns the rc a write would. The build's pre-YURI rc 1 is now rc 0 on the live tree (lead regenerated with YURI) |
| `scripts/docket_view.py` | **State BUILT-UNWIRED → WIRED-SINGLE-INVOKER, Invoked_by** (`PROME/CLOSEOUT.md:71` + validate_all A2); ᶜ tag fix; residue ᵒ substring |
| `scripts/validate_all.py` | **Detects 14 → 15 legs** (A9 read_cap_check was already registered 9/12; the old Gap claimed otherwise); baseline C2 1345 / D1 2; inert `recheck_by`; consumer_check owed (534→1345, 6→2) |
| `scripts/pipeline_rc_guard.py` | **State BUILT-UNWIRED → WIRED-HARNESS, Invoked_by** (`.claude/settings.json:31` via PROME's wrapper, ADVISORY since WQ-263); v4 85/85; the wrapper is 34/36 (PROME's to fix); settings statusMessage still says "BLOCKING" |
| `scripts/corrections_boot_check.py` | State = `WIRED — D4(a) edit BUILT 2026-09-24, independent read PENDING (WQ-229 gate)`; SAM 0→1 on COR-20260826-02 |
| `scripts/read_cap_check.py` (ROOT) | Class rows measured per member; rule-20 charter line; **OPEN EMPTY_CLASS_SEVERITY ruling** (WALTER ⛔). The stale "no --selftest on the root tool" Gap was removed |
| `scripts/ledger_staleness.py` | Null_meaning **appended**: "PASS proves only `workbook/*.tsv` or a declared LEDGER_GLOB; 154 TSVs printed NOT-scanned at run #5". This also discharges PR#6 §3b's "edit owed at the 9/18 riders" |
| **NEW** `AGENTS/DAEDALUS/scripts/walter_route_check.py` | MANUAL-BY-DESIGN (Wiring Sweep route-census leg only; no boot/closeout step); leg-A-only perimeter; `--drops` + ROSTER screen; rc 1 still fires on retired YEYOU (ruling needed) |

**Not done:** On_FAIL cells were left alone except on the new row. Every row states that the 9/24 edits are **UNCOMMITTED** at this pass, so the lead should re-cut those phrases after the commit. CHECKS.tsv at 69 KB is over the 54,250 B cap. It is not a declared whole-read, so this is not a read-cap defect, but it is noted.

## TASK 2 — SURFACES.tsv re-review (13 rows, all `Last_reviewed=2026-09-24`)

| Surface | State (was → now) | What the gap is now (verified at the artifact) |
|---|---|---|
| FORGE/ | PARTIAL → PARTIAL | `ledger_staleness.py` has 0 FORGE refs, so `--trade` is blind to FORGE/STATUS.md. Header 9/20 (WQ-272): quantities from the 9/16 capture, marks from the 9/10 close, and it says **no broker export exists**. The Enforcing cell is re-pointed to `position_agreement_check` at PROME/BOOT.md:67 |
| BOARD/ | ENFORCED | INDEX.md is GENERATED (WQ-174); 1,042 SIG files = header count; walter_doctor checks present (not run) |
| memory/auto/ | ENFORCED | INDEX_COLD.md 40,119 B = **123% of budget** (under the cap since the 9/06 shard); MEMORY.md 74% of its 25,600 B cap |
| HEARTBEAT.md | ENFORCED | 24,349 B = **74.8% of budget**, 0.2 pt under the rotate trigger |
| CLAUDE.md (root) | PARTIAL | The Enforcing cell pointed at a prome_gate "mirror-walk". The mechanism now is `consumer_check.py --mirror-map`, a MANUAL advisory at closeout. 74% of budget |
| AGENTS.md | UNMECHANIZED | The roster table was removed 8/29 (WQ-128), so the drift gap is moot. Only a prose rule stops it being re-added |
| MESSAGING/ | UNMECHANIZED | No conformance reader. Allowlist-vs-desk match is **UNVERIFIED 2026-09-24** |
| SIGNALS/ | DEAD-FROZEN-BANNERED | Banner present. The feeds.yml removed 8/29 was `.github/workflows/feeds.yml`; `SIGNALS/feeds.yml` is still tracked. `AGENTS/SIGNALS.md` has **no row** (see below) |
| scripts/ | OWNED | 8 root files + 2 local tools edited and uncommitted; 2 independent reads owed |
| PROME/WILL_QUEUE.md | ENFORCED-advisory | check_will_queue (:641) + validate_all B3 (19 rows PASS) |
| FORGE/timing/ | FROZEN-DECLARED | Banner present at README.md:1; no check keeps it there |
| KERNEL/ | ENFORCED | README: NO ACTIVATION LIVE. Gap (a) is **UNVERIFIED 2026-09-24**: I could not confirm whether WQ-150's root-④ re-key completed (root ④ text dates from a284c86bd 8/30) |
| PROME/registry/READS.tsv | **SCHEDULED → PARTIAL** | 5 desks attested (PROME·WALTER·BROCK·RED·DAEDALUS). `reads_check --fleet` reads **all 5 as ❓ UNKNOWN** (the attestation predates a later boot change); 37 undeclared |

**Not done:** I did not add a row for `AGENTS/SIGNALS.md`, the live shared ledger under carve-out ②. It sits outside every AGENTS/<NAME>-scoped enforcer. It is a candidate for the next surfaces-currency pass (DAEDALUS's call). I also did not run walter_doctor.py (WALTER's) or reads_check beyond `--fleet`.

## TASK 3 — Doc retirement and outbox tail

**Referrer check re-run:** `git grep -l -F <basename>`, excluding archive/_archive/processed/delivered/INDEX*/FLEET_DIRECTORY.md/MEMORY.md/self/PATTERNS.tsv. It found referrers the sweep did not list: upgrade cards. Every such card carries a "CLOSED AS A QUEUE 2026-08-17 — historical, not maintained" banner (BROCK/SHADE/CARL/REGINALD/YEYOU), or its "old section table remains historical" (HAWK/RED 9/08). Those references are therefore record-class. I also checked the second hop: none of the 10 live-travelled NOT-eligible docs, and no `profiles/*.md` or `sweeps/*.md`, names a moved file.

| File | Verdict | Evidence |
|---|---|---|
| BATCH_01_handles.md | **MOVED** | Its own status: all 8 APPLIED 6/28. Referrers BROCK_CARD:9 and SHADE_CARD:9 are ✅APPLIED provenance with commit hashes inside closed queues. ⚠️ This **reverses** `runs/2026-09-17_OVERDUE_BATTERY.md:28` "KEPT (live cards)": those cards were closed as queues 8/17 |
| NEXUS_CARD.md | **MOVED** | CLOSED/SUPERSEDED 7/22; only referrer is FLEET_MAP_HISTORY |
| CORAL_S8_PROPOSAL.md | **MOVED** | APPLIED 7/23; 0 referrers |
| UTILITY_FIRMING_2026-07-03.md | **MOVED** (ruling: the PATTERNS pointer does not protect) | Only HELD item is YEYOU, now moot (seat retired 9/05). Card referrers are method provenance |
| BATCH_02_handles.md | **KEPT (reverted after moving)** | Live referrer through a second hop: `BLUEPRINTS/market-agent.md:42/:74` travel `upgrades/HANDLE_SWEEP_independence-action.md`, and HANDLE_SWEEP's authoritative disposition banner (:6) points into BATCH_02 for its dispositions. I restored the file byte-identical to HEAD |
| TRADE_STALENESS_SWEEP.md | **MOVED** | All 3 open design calls are resolved elsewhere: `--trade` shipped (sweep #5 ran `--trade --all`); banner vocabulary broadened (`scripts/ledger_staleness.py:236`); the dormant cluster OZK/ZHAO/FERT is ACTIVE (`PROME/ROSTER.md:79/106/110`). The violations table is now the recurring Staleness Sweep's |
| LABOR_CARD.md + LABOR_GAP_ASSESSMENT_2026-07-10.md | **MOVED (pair)** | All items resolved at `upgrades/PRODUCTION_REVIEW_2026-07-22.md:30`; `AGENTS/LABOR/workbook/PREDICTIONS_SCOREBOARD.md` exists |
| TERRY_CARD.md | **KEPT** | One item is still open: Will's question **"Track every considered setup, or approved/rejected only?"**, still open at `AGENTS/TERRY/STATUS.md:60`. The other items are resolved: risk unit (STATUS.md:59, 8/4), firetime integration (TERRY `archive/STATUS_ARCHIVE_2026-09-01.md:176`), WALTER inbox cleared (only `processed/` remains), real card fired 7/20, YEYOU leg N/A |
| WALTER_CARD.md | **KEPT** | One item is still open: **item 5, SIGNAL_INTAKE.md (I3) reconcile-or-kill.** No disposition was found. Per-desk SIGNAL_INTAKE.md files still live at CARL/ORACLE/SAM, and the template was re-headered 9/15. Resolved: item 3, the spine regen (`AGENTS/WALTER/STATUS.md:48`, regenerated 9/24); the PAT-055 counters (BOTTOM LINE is now regenerator step 12(e)); YEYOU leg N/A |

**Outbox:** both 9/02 flat files are **byte-identical** (cmp) to tracked copies in `PROME/inbox/processed/`. I moved them to `outbox/delivered/` with `git mv`.
**Banner on each moved doc:** `> RETIRED 2026-09-24 — <reason>; >60d since last commit, not boot-read; referrers at retirement: none live.`
**Clause ①:** no moved file is the registered artifact of a pending DOCKET/GATES row. The git grep over the whole repo returned no PROME hit.

## TASK 4 — upgrades/ closing banners

The perimeter is 43 docs: every `upgrades/` entry except the 7 moved files, `*READER*`, `*_raw*`, `*_CARD.md`, the `_readers/` dir and 1 `.json`. BATCH_02 is not counted; it was restored after the census and already carries DISPOSITIONED at its line 3. Of these, **23 got a banner.** **10 were left alone** because they already carry the 8/17 F5 `🗄 DATED AUDIT/WORK RECORD … history, not a live queue` banner, which my keyword heuristic missed: AEOLUS_QC · BRENT_AUDIT · DAEDALUS_SELF_SWEEP_07-12 · FORGE_AUDIT · LABOR_QC · PRODUCTION_REVIEW_08-07 · PROME_AUDIT · RAV_CHANGE_REVIEW · TERRY_ARCHITECTURE_AUDIT · WP4_ECHO. The other 10 carry a real closing status already. `PROME_SWEEP_2026-09-08_EVIDENCE.json` was skipped, because a banner would break the JSON.

| File | Banner (`> STATUS 2026-09-24: …`) |
|---|---|
| BOND_REVIEW_2026-08-20 | CLOSED — FLEET_MAP_HISTORY.tsv:74 |
| BRENT_ARCHITECTURE_REVIEW_2026-09-07 | CLOSED — upgrades/BRENT_CARD.md (re-cut from it; open items live there) + profiles/BRENT.md §4 |
| BRENT_REVIEW · BRENT_ROUTING_SCRIPTS_CLUSTER · BRENT_STRUCTURAL_REVIEW · SAM_FALSIFICATION_REVIEW · SAM_ROUTING_SCRIPTS_REVIEW · SAM_SPINE_REVIEW (all 2026-08-17) | CLOSED — SAM_BRENT_REVIEW_2026-08-17_SYNTHESIS.md (verdict layer) + FLEET_MAP_HISTORY.tsv:77/:83 |
| SAM_BRENT_REVIEW_2026-08-17_SYNTHESIS | CLOSED — FLEET_MAP_HISTORY.tsv:77 (BRENT) / :83 (SAM) |
| CREED_REVIEW_2026-08-20 | CLOSED — FLEET_MAP_HISTORY.tsv:85 |
| HOMER_REVIEW_2026-08-22 | CLOSED — upgrades/HOMER_CARD.md (live queue; profiles/HOMER.md:14) |
| HOMER_REVIEW_PLAN_2026-08-22 | SUPERSEDED by upgrades/HOMER_REVIEW_2026-08-22.md |
| LEDGER_STALENESS_RC_CONTRACT_2026-08-17 | CLOSED — CHECKS.tsv ledger_staleness On_FAIL + BLUEPRINTS/CHECK_STANDARD.md:82 |
| PRODUCTION_REVIEW_2026-07-22 | CLOSED — sweeps/PRODUCTION_REVIEW.md:91 + FLEET_MAP_HISTORY 7/22 rows |
| PRODUCTION_REVIEW_2026-08-17 | CLOSED — sweeps/PRODUCTION_REVIEW.md:89 |
| PRODUCTION_REVIEW_2026-09-01 | CLOSED — sweeps/PRODUCTION_REVIEW.md:88 |
| PRODUCTION_REVIEW_2026-09-17 | CLOSED — sweeps/PRODUCTION_REVIEW.md:87 + FLEET_MAP 7bfee0060; §3b owed item landed today |
| PROFILE_S3_AUDIT_2026-08-11 | **OPEN — 13 of 20 un-rowed agents' §3 invalidation rows still un-derived (runs/2026-08-23_FALSIFICATION_SWEEP_02.md:138; not re-measured)** |
| PROME_SWEEP_2026-09-08 | CLOSED — FLEET_MAP_HISTORY.tsv:216 |
| PROME_WAVE_ACCEPTANCE_GRADE_2026-08-11 | CLOSED — FLEET_MAP_HISTORY.tsv:38 |
| RAV_FEEDBACK_REVIEW_2026-08-21 | CLOSED — PROME/codex/2026-08-21_RAV_operating-improvements-feedback.md §RULED/§MINTED |
| RED_AUDIT_2026-08-12 | CLOSED — FLEET_MAP_HISTORY.tsv:87 (+ :136) |
| WAR_TRIAD_REVIEW_2026-08-15 | CLOSED — archive/STATUS_ARCHIVE_2026-08-17.md + FLEET_MAP_HISTORY.tsv:11 |

Every banner diff is `+2/-0` (git diff --numstat), so no body text was changed.

## Not done (out of perimeter, or needs a ruling)
- No commit, push, or closeout battery. **The staged renames need a path-scoped commit.**
- STATUS/REGISTRY/Run Log for sweep #5 were not touched (forbidden surfaces). FLEET_MAP/PATTERNS/EVOLUTION were not touched.
- Stale run records named by the LOCAL_TOOLS build (`runs/2026-09-17_WIRING_SWEEP_02_JUDGMENT_W1.md` OTTO "0 all-time") were not edited, because this pass may write only this one record under runs/.
- The `render_directory` / consumer-check residue (534→1345, 6→2) is left for the committing closeout (root 1c).
