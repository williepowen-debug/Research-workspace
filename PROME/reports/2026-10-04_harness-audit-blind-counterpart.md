# Harness audit — BLIND COUNTERPART ledger (PROME prome-ed, 2026-10-04)

**Started:** Sun Oct 4 11:37:16 EDT 2026 (`date`) · read-only auditor · subject commit `f1dbe2e70`

## Header
| File @f1dbe2e70 | bytes (`git show f1dbe2e70:<p> \| wc -c`) | lines |
|---|---|---|
| CLAUDE.md | 24199 | 133 |
| AGENTS.md | 4991 | 62 |
| AGENTS/DAEDALUS/CLAUDE.md | 33509 | 198 |
| AGENTS/DAEDALUS/builds/RAV_CHARTER.md | 20695 | 189 |

Method files read (working tree): `AGENTS/DAEDALUS/sweeps/HARNESS_AUDIT_SWEEP.md` (2377 B), `AGENTS/DAEDALUS/HARNESS_AUDIT_2026-07-07.md` (14096 B).

**Blindness disclosure:** HARNESS_AUDIT_SWEEP.md's Run Log contains a 2026-10-04 row I was told to ignore; reading the playbook necessarily displayed it. What I saw: "PARTIAL:13 full primary/canon files +5 clause reads; 42 primary files +9 nested remain · TERRY recovery/receipt counterexamples, LIQUID coverage and source conflicts · Proposed only; independent result challenge complete, actual blind PROME counterpart pending · last_run July7/original deadline October5 unchanged; recommended overflow 10/6 not approved". None of it names a finding in the four files below. No other blinded artifact opened.

## Working notes (incremental) — all four target files read in full at f1dbe2e70 by 11:4x ET; root CLAUDE.md @f1dbe2e70 is byte-identical to the working tree (diff empty).

Drift check: `git diff --stat f1dbe2e70 -- <each of the 4 files>` printed nothing → all four are byte-identical in the working tree; line numbers below are valid at both.
Existence of every path the four files point at was checked with `git cat-file -e f1dbe2e70:<path>` (47 paths incl. 3 memory slugs) → all present (VERIFIED). Two of those paths sit under `AGENTS/DAEDALUS/runs/` (cited by DAEDALUS CLAUDE.md L44/L131); I checked existence only and did NOT open them.

---

## 1. Root `CLAUDE.md` @f1dbe2e70

### STRIKE
(none — no step fails all three legs outright; the candidates below fail one leg but each has a reason to stay as a short pointer, so they are REWRITE)

### REWRITE
**R-ROOT-1 ⚠️ Gate C custody paragraph + carve-out ④ procedure are dormant text in every session's context.**
- claim: L80 (carve-out ④) and L82 (Gate C custody, PROME-only) carry full procedural detail for a mechanism with no live window; L82 binds only PROME.
- artifact: `CLAUDE.md:80`, `CLAUDE.md:82`; mechanism doc `KERNEL/GATE_C_C4_CUSTODY.md` (status "COMPLETE — RED REGISTERED DORMANT — NOT LIVE").
- command: `git show f1dbe2e70:KERNEL/GATE_C_C7_ACTIVATION_2026-08-27.json | grep -E "window_end|revoked_at"`; `git show f1dbe2e70:KERNEL/GATE_C_C4_CUSTODY.md | grep -ncE "additions-only|writer_id|substitute|exact (file )?pathspec"`
- observed: the only non-draft activation window ended 2026-08-27T18:00Z and was revoked 17:52Z; the C4 doc carries the custody terms (17 keyword hits).
- proposed: fails (a) for every non-PROME session and partly (c). Keep the AUTHORITY sentences in root (root is git canon — commit grants must live here) and move the procedure (prove one writer, inspect staged paths, additions-only checks, substitute-custodian terms) to the KERNEL runbook with one pointer. Will-gated root edit.

**R-ROOT-2 ⚠️ "Rules only" header contradicted by in-body provenance.**
- claim: L3 says reasons/incidents/dates live in `docs/CANON_PROVENANCE.md`; body still carries provenance parentheticals.
- artifact: `CLAUDE.md:3` vs `:22` ("WQ-137: the hand-copied chain that lived here had already diverged…"), `:105` ("WQ-96, Will 2026-09-01; cold-read verified empirically"), `:106` ("WQ-171 ①, Will 2026-09-03"), `:79` ("Why mandatory: …").
- command: `git show f1dbe2e70:CLAUDE.md | grep -nE "WQ-137|WQ-96|WQ-171|Why mandatory"`
- observed: 4 hits.
- proposed: fails (a) — move to CANON_PROVENANCE (it has a key scheme); keep the rule text. Low value per byte but the header's own promise is the test.

**R-ROOT-3 ⚠️ Root hooks do not reach the launch mode root prescribes (cross-file: root `.claude/settings.json`).**
- claim: L13 tells every desk to launch from `AGENTS/<NAME>/`; the repo-root `.claude/settings.json` hooks (SessionStart banner, BLOCKING commit-subject guard for rule 4d, pipeline-rc block) only fire for a repo-root launch, which L13 calls the wrong launch.
- artifact: `CLAUDE.md:13`, `CLAUDE.md:106` (4d); `.claude/settings.json` (hooks); `PROME/BOOT.md:47` ("Subdirectory launches require local hook wiring (`finding_subdir_launch_hooks_dont_fire`)").
- command: `git ls-tree -r --name-only f1dbe2e70 | grep -E "(^|/)\.claude/settings(\.local)?\.json$"`
- observed: settings exist only at root, PROME/, AGENTS/WALTER/, AGENTS/BARON/ — no AGENTS/DAEDALUS/ (or other desk) settings.
- proposed: KEEP rule 4d and "Pull at session start" as prose — for in-folder desks they are NOT mechanized (criterion b holds). Do NOT strike 4d on the strength of the hook. Flag the settings gap to the owner (root hooks protect only mis-launched sessions). INFERRED: hook non-firing rests on PROME/BOOT.md's statement + memory slug, not re-tested here.

### KEEP notes (surprising keeps)
- **Rule 1 "Read before editing"** (`:32`) looks like harness-enforced weak-model hand-holding (the 7/7 §0 model-upgrade test names it) — but the Edit/Write read-guard does not cover edits made through Bash (`sed -i`, heredoc), which this harness explicitly steers agents toward in bypass mode. Not mechanized for that path → KEEP; also stable-numbered (`:44-46`).
- **Rule 11 "trash > rm"** (`:42`): no hook blocks `rm` — `grep -nE "\brm\b|trash"` over `PROME/tools/hooks/git_guard.py` and `pipeline_rc_block.py` → no hit (SEARCH-NOT-FOUND, owner-declared hook files checked) → not mechanized → KEEP.
- **Session-end 1b–1e** (`:90-94`): each named tool exists and accepts the documented form (VERIFIED: `safe-push.sh:113` prints exactly the `Pushed. CONFIRMED: HEAD … (fresh fetch).` receipt; `ledger_staleness.py:1126/1133` positional agent + `--nudge` flag; `LEDGER_GLOB` parsed at `ledger_staleness.py:582`; `consumer_check.py` has `--self`/`--from-ledger`; `orphan_check.sh:69` emits `[likely YOURS]`; `check_memory_length.sh` exits 1/2). There is no fleet-wide closeout runner in `scripts/` (only DAEDALUS's and PROME's private gates) → steps are not mechanized for most desks → KEEP.


---

## 2. Root `AGENTS.md` @f1dbe2e70

### STRIKE
**S-AG-1 ❌ The "Transmission chains" table is a hand-copied route mirror that root canon forbids, and it has already diverged from `_NETWORK.md`.**
- claim: root says topology is canonical at `_NETWORK.md`, AGENTS.md is for navigation, and routes must not be reconstructed "here or in any other mirror"; AGENTS.md itself says "nothing below is restated here" and then restates 10 chains.
- artifact: `CLAUDE.md:22`; `AGENTS.md:17` ("Sources of truth (nothing below is restated here)"), `AGENTS.md:29-42`; canon `AGENTS/_NETWORK.md` (mermaid edges + "Chain summary").
- command: `git show f1dbe2e70:AGENTS/_NETWORK.md | grep -E "YURI|HAWK -->|MARCO -->|HANS -->|ZHAO -->"` vs `git show f1dbe2e70:AGENTS.md | sed -n 29,42p`
- observed (divergences): (1) `AGENTS.md:35` "YURI → {OSPREY, HAWK} → {OSPREY, FALCON} → HAWK" implies HAWK → OSPREY/FALCON; canon has only OSPREY→HAWK and FALCON→HAWK (HAWK receives), and canon's YURI edges `YURI -.-> HANS` and `YURI -.-> BRENT` are missing. (2) `:33` "OZK, WAL, FLG → REGINALD" — canon draws OZK/WAL as undirected dotted "peer bank surface" and has REGINALD→FLG plus FLG→REGINALD. (3) Edges absent from AGENTS.md: HANS→LIQUID (no Europe chain at all), MARCO→BRENT, BOND→LIQUID, ZHAO→SAM, BARON→HAWK (dormant, defensible). The table is maintained by `builds/REGISTRATION_CHECKLIST.md` row 3, which is why it keeps living.
- proposed: fails (c) — owned at `_NETWORK.md`. Replace `AGENTS.md:29-42` with one pointer line ("Chains → `AGENTS/_NETWORK.md` § Chain summary"); keep the potash line `:44` only if FERT's rule needs a nav pointer (root `:24` already carries it — see X-3). Update REGISTRATION_CHECKLIST row 3 in the same changelist so builds stop re-growing it. Will-gated (AGENTS.md core).

### REWRITE
**R-AG-1 ❌ (INFERRED) AGENTS.md is the auto-loaded file for the fleet's two Codex reviewers, and it tells them the git rules are "auto-injected".**
- claim: `AGENTS.md:21` routes "Fleet operating and Git rules" to "root `CLAUDE.md` (auto-injected)". RAV (Codex CLI, commits directly on master per ROSTER § SPECIAL) and CATO (Astra through Codex) do not get CLAUDE.md injected; Codex's harness file is AGENTS.md.
- artifact: `AGENTS.md:21`; `AGENTS/RAV/README.md:3` ("it loads no `CLAUDE.md` and must be handed its context"); `RAV_CHARTER.md:15`; ROSTER § SPECIAL RAV row.
- command: `git show f1dbe2e70:AGENTS/RAV/README.md | sed -n 3p`; `git show f1dbe2e70:PROME/ROSTER.md | grep -n "^\*\*RAV\*\*"`
- observed: RAV README confirms no CLAUDE.md load; ROSTER confirms direct master commits. That Codex auto-loads AGENTS.md is INFERRED from Codex CLI's documented default, not tested on this box.
- proposed: one sentence in AGENTS.md: "Codex sessions (RAV, CATO) do not receive `CLAUDE.md` — read root `CLAUDE.md` § Git Protocol before any git write." Cheapest fix to the RAV pull/push gap in X-1.

**R-AG-2 ⚠️ Cross-chain roles line restates roster-class descriptions.**
- artifact: `AGENTS.md:46` vs `AGENTS.md:27` ("Do not recreate roster membership or responsibility classes here").
- command: read both lines.
- observed: `:46` gives each of 9 agents a role description (one is DAEDALUS "launched by PROME or Will" — consistent with ROSTER § SPECIAL today). Not membership, but the same drift class as S-AG-1.
- proposed: keep only if it is the nav aid AGENTS.md exists for; otherwise point at ROSTER. Low priority.

### KEEP notes
- `AGENTS.md:52` CREED permission line: ROSTER's CREED row says it is "carried in AGENTS.md, sourced here 8/29" — deliberate dual pointer with ROSTER as owner. KEEP.
- `AGENTS.md:56` Gate C pointer: one line, cites root ④, correct that it is inactive (activation window expired/revoked 2026-08-27). KEEP.


---

## 3. `AGENTS/DAEDALUS/CLAUDE.md` @f1dbe2e70 (33,509 B — over 32,550 B, but NOT a breach: `BLUEPRINTS/READ_CAP.md` rule 20 / table row L40 rules the charter out of the read cap (harness-injected, a context cost); noted for the composite-context watch only — it was 31,931 B at the 9/19 ruling)

### STRIKE
**S-DA-1 ⚠️ SPAWN step 8 "Deliver before idling" restates root.**
- artifact: `AGENTS/DAEDALUS/CLAUDE.md:47` vs `CLAUDE.md:20` (same rule, same wording: SendMessage AND write to file, never idle holding).
- command: `git show f1dbe2e70:CLAUDE.md | sed -n 20p`; `git show f1dbe2e70:AGENTS/DAEDALUS/CLAUDE.md | sed -n 47p`
- observed: identical content.
- proposed: fails (c). Replace with "8. Deliver per root (coordinator spawn rule)" or drop the step number's body (keep the numbering — the gate spec cites step numbers).

**S-DA-2 ⚠️ `#1 RULE — File > verbal` block restates root Output Canon (the 7/7 S4 class, on the auditor's own file).**
- artifact: `:29` vs `CLAUDE.md` Output Canon ("**File > verbal** — work not written to a file in your dir doesn't exist").
- proposed: keep ONLY the DAEDALUS-specific exception (OFF-FLEET records go in the subject's zone); strike the generic restatement.

**S-DA-3 ⚠️ `trash > rm` and `git add -A`/`git add .` in AUTHORITY restate root rule #11 and root Git Protocol.**
- artifact: `:104`. proposed: fails (c); strike the restated clauses, keep the DAEDALUS-specific ask-first items (wiring/retiring an agent, deleting another agent's work).

### REWRITE
**R-DA-1 ❌ GIT section restates the non-ff recovery recipe and has drifted from root — the exact S2 failure the section's own heading says it avoids.**
- claim: heading says "cite, don't restate — S2 2026-07-08"; body then gives "Non-ff abort → `git pull --rebase` + re-push; NEVER force."
- artifact: `AGENTS/DAEDALUS/CLAUDE.md:112`, `:115` vs `CLAUDE.md:96` (root step 3: `git pull --rebase --autostash` ONLY after the dirty-path overlap check `git diff --name-only "$(git merge-base HEAD origin/master)..origin/master"` vs `git status --porcelain`; overlap ⇒ stop and flag PROME; escalation test).
- command: `git show f1dbe2e70:AGENTS/DAEDALUS/CLAUDE.md | sed -n 115p`; `git show f1dbe2e70:CLAUDE.md | sed -n 96p`
- observed: DAEDALUS's version omits the overlap check, the stop-and-flag branch and the escalation test.
- proposed: replace `:115` with "Non-ff → root Git Protocol session-end step 3 in full." Keep `:114` (the scripts/ grant — see X-4) and `:116` (DAEDALUS-specific).

**R-DA-2 ❌ The harness audit's own unconditional trigger ("on any model upgrade") is wired nowhere, and the boot cadence-check presents as covering sweeps.**
- claim: the playbook makes a model upgrade an unconditional trigger; DAEDALUS CLAUDE.md step 5 says the cadence check surfaces DUE sweeps; nothing checks the model-upgrade leg, so a CLEAN `sweeps_due` after a model change certifies a sweep status it never evaluated.
- artifact: `AGENTS/DAEDALUS/sweeps/HARNESS_AUDIT_SWEEP.md:3` ("every 90 days — AND unconditionally on any model upgrade"); `AGENTS/DAEDALUS/CLAUDE.md:42`, `:69-72`; `AGENTS/DAEDALUS/scripts/sweeps_due.py`.
- command: `git show f1dbe2e70:AGENTS/DAEDALUS/scripts/sweeps_due.py | grep -niE "model|upgrade|harness"` → no output; `git grep -niE "model.upgrade|model upgrade" f1dbe2e70 -- scripts/ AGENTS/DAEDALUS/scripts/ PROME/tools/` → no output; `git show f1dbe2e70:AGENTS/DAEDALUS/CLAUDE.md | grep -niE "harness audit|model.upgrade"` → rc 1.
- observed: VERIFIED absent in the owner-declared checker and in all three script trees; the trigger lives only in the playbook, SPEC.md (read once at first boot) and a REGISTRY free-text cell (file matched by `git grep -l`; cell not read, per blindness). sweeps_due parses `cadence_days` only.
- proposed: this is a criterion-(b) item: mechanize (record the model ID at each harness-audit run; sweeps_due compares it to the running model or to a manually-updated `MODEL` line and prints DUE on mismatch), or — if not mechanizable — add the trigger as one line to SPAWN step 5. Either way the Job 2 list must name the sweep (R-DA-4).

**R-DA-3 ⚠️ SPAWN 5/5b/5c and step 9's bullet list restate what `daedalus_gate.py` already runs.**
- claim: `:42` says the gate "runs steps 5, 5b and 5c… the steps it wraps stay written here as its spec"; `:48` says the same for closeout.
- artifact: `:42-44`, `:48-55`; `AGENTS/DAEDALUS/scripts/daedalus_gate.py` @f1dbe2e70 — boot B1 sweeps_due (`:146`), B2 corrections_boot_check (`:148`), B3 inbox (`:151`), B4 read_cap_check (`:166`), B5 docket_owed (`:170`); closeout C0 sweeps_due/SELF-ROW, C1 orphan_check, C2 consumer_check incl. `--self` (`:201`), C3 ledger nudge, C4 memory index+length, C5 claim_check, C6 PATTERNS_HOT conservation, C7 read_cap BLOCKING, C8 complete_check, C9 STATUS stamp, C10 rule-declared; verify V1 → verify_push.sh (`:306`).
- command: `git show f1dbe2e70:AGENTS/DAEDALUS/scripts/daedalus_gate.py | grep -nE "child_step\(|Step\(\"C|Step\(\"B"`
- observed: every mechanical bullet is wired (VERIFIED). Non-mechanized residue that must stay as prose: (i) regen PATTERNS_HOT on a TEXT edit — C6 checks row-count conservation only and says so ("NOT checked: whether a row's TEXT changed"); (ii) re-cut own FLEET_MAP row (C0 only detects ≥5d slip); (iii) apply a declared rule to its own artifact (C10 is DECLARED-only); (iv) commit + safe-push.
- proposed: per 7/7 S3 precedent, collapse to the invocation line + the four residue items; move the per-step spec to `design/2026-09-17_DAEDALUS_GATE_SPEC.md` (which already exists). Also `:54` tells the agent to run `bash verify_push.sh` while `:48` says run `daedalus_gate.py verify` — the gate's V1 already calls verify_push.sh, so as written the push is verified twice; name one.

**R-DA-4 ⚠️ Job 2 "Recurring form" restates cadences and lists 3 of the registry's sweeps — omitting the Harness Audit that PAT-050 says covers this very file.**
- artifact: `:69-72` vs `AGENTS/DAEDALUS/sweeps/REGISTRY.tsv` (cols 1-6 only), whose own comment line says "sweeps/*.md reference it, don't restate it".
- command: `git show f1dbe2e70:AGENTS/DAEDALUS/sweeps/REGISTRY.tsv | cut -f1-6`
- observed: registry has 5 named sweeps + 8 queue rows + 4 dated/other rows (Harness Audit 90d last_run 2026-07-07; PROME Spine 21d; Wiring DATED; Gate Basis 21d; Prose-Remedy 21d; H2 DATED; scorecard 7d). The three cadences quoted (21/14/21) match today; the list is not the set.
- proposed: replace the three bullets with "Recurring sweeps: `sweeps/REGISTRY.tsv` (cadence canon) — playbooks in `sweeps/`." Keep the two load-bearing authority clauses (Production Review fully autonomous own-map-only; Falsification dispositions task-packet-only) as one line each, since those are behavior-gates not homed in REGISTRY.

**R-DA-5 ⚠️ YEYOU still named as a live layer owner beside the paragraph that retires it (two live instructions).**
- artifact: `:23` ("Per-push compliance | YEYOU"), `:27` ("You are not YEYOU (mechanical, per-push, read-only)"), `:191` ("inbox/ … incl. YEYOU flags to aggregate"), vs `:108` (seat RETIRED 2026-09-05) and ROSTER § RETIRED ("YEYOU — RETIRED 2026-09-05").
- proposed: mark the table row RETIRED/vacant (the layer has no owner — that is the true state and is what `:108` says); strike the `:191` parenthetical. Compress `:108` (story: "asserted zero findings for 16 days…") to the two behavior facts: no mechanical reviewer exists; the L5 mechanical-QC leg is N/A.

**R-DA-6 ⚠️ Standing rule written beside its own live violation.**
- artifact: `:52` "Standing rule: two tools may not share a basename across `scripts/` and `AGENTS/<NAME>/scripts/`" — and the same bullet documents that `scripts/read_cap_check.py` and `AGENTS/DAEDALUS/scripts/read_cap_check.py` both exist.
- command: `ls scripts/read_cap_check.py AGENTS/DAEDALUS/scripts/read_cap_check.py` (both present; local one still registered at `AGENTS/DAEDALUS/CHECKS.tsv:32`).
- proposed: either rename the local tool (DAEDALUS owns both) or record the grandfathered exception explicitly; a rule its author violates in the same sentence will not be applied by anyone else.

**R-DA-7 ⚠️ MEMORY MODEL / OUTPUT RULES carry story and self-describing figures that fail (a).**
- artifact: `:148` (PAT-115 promotion narrative, ~1.2 KB inside one table cell), `:150` ("Notes (124 KB)… Gaps (62.6%…, 4.5 KB)… Next_upgrade (13.6 KB) is next"), `:151` (CHECKS.tsv origin measurement), `:166` (three instances + the fourth), `:167` (32,550 B and its derivation restated — root Data Hygiene + READ_CAP.md own the number; the 75%/70% rotation band is the DAEDALUS-local part).
- proposed: keep each rule sentence; move story/figures to the archive block the file already uses (`archive/CLAUDE_ARCHIVE_2026-09.md`). Byte figures for other files are stale by the next edit.

**R-DA-8 ⚠️ Job 1 registration surface list still names "root".**
- artifact: `:64` "ROSTER/root/AGENTS.md/_INDEX/_NETWORK" vs `builds/REGISTRATION_CHECKLIST.md:10` (row 2: root no longer carries a roster or chain — "usually a NO-OP; verify by grep, do not insert").
- proposed: cite the checklist only; drop the inline list (fails c).

**R-DA-9 ⚠️ Step 9 command uses a cwd-relative path while step 5 uses the cwd-proof form.**
- artifact: `:42` `python3 "$(git rev-parse --show-toplevel)/AGENTS/DAEDALUS/scripts/daedalus_gate.py" boot` vs `:48` `python3 AGENTS/DAEDALUS/scripts/daedalus_gate.py closeout …` — the agent launches in `AGENTS/DAEDALUS/` (root `:13`), where the relative form fails. Same for `:51-54`.
- proposed: use the cwd-proof form throughout.

### KEEP notes
- AUTHORITY two-guard model (`:97-100`) and Job 5 OFF-FLEET rules 1-5 (`:83-91`): behavior-gates, not mechanizable, homed only here → KEEP (7/7 "Not struck" list concurs for the two-guard model).
- FILES table `:190` scripts list is incomplete (no daedalus_gate, docket_owed, complete_check, verify_push, regen_patterns_hot) — a nav aid; low value either way.


---

## 4. `AGENTS/DAEDALUS/builds/RAV_CHARTER.md` @f1dbe2e70 (RAV's harness: `AGENTS/RAV/README.md:5` says hand the Codex session §3, §5, §8)

### STRIKE
**S-RAV-1 ❌ §6 "ON YEYOU'S REVIVAL — composition, not handoff" describes a path ROSTER has closed.**
- artifact: `RAV_CHARTER.md:129-141`; also `:24` ("YEYOU has never run (`reviews/REVIEW_LOG.tsv`, zero findings all-time), so RAV is covering QC alone. On YEYOU's revival the two compose"), `:101` ("while YEYOU is down"), `:112` ("YEYOU on revival (its ⚪ NEEDS-VERIFY escalations arrive here)"), `:158` ("fold into the YEYOU revival pass, which is one decision away").
- command: `git show f1dbe2e70:PROME/ROSTER.md | grep -n "YEYOU"` ; `git show f1dbe2e70:AGENTS/DAEDALUS/CLAUDE.md | sed -n 108p`
- observed: ROSTER § RETIRED: "YEYOU — RETIRED 2026-09-05 … RAV is now the STANDING sole-QC (was interim-pending-YEYOU-revival; the compose-on-revival path is closed)". DAEDALUS CLAUDE.md `:108`: YEYOU ran once 2026-08-20 (25 REVIEW_LOG rows, 13 findings). So `:24` is false on both counts (it did run; it will not revive) and §6 is dead.
- proposed: fails (a) — strike §6; rewrite `:24` to "YEYOU retired 2026-09-05 (ROSTER); RAV is the standing sole QC — no mechanical per-push reviewer exists"; strike the revival clauses at `:101`, `:112`, `:158`. `:101` and `:112` sit in §5, which RAV is handed.

### REWRITE
**R-RAV-1 ❌ §8 checklist gives a cross-directory committer a bare "Pull." with no shared-tree guard, and no push step.**
- claim: RAV runs on Codex, loads no CLAUDE.md (`:15`), and commits directly on master into other agents' directories (ROSTER § SPECIAL). Its only git instructions are §8 step 1 "Pull." and step 8 (path-scoped commit, no `git add -A`, no `git reset HEAD`).
- artifact: `RAV_CHARTER.md:178`, `:185`; root `CLAUDE.md:109-115` ("Before pulling": check for uncommitted changes outside your dir; other agents' dirs modified ⇒ STOP, do not pull), `CLAUDE.md:95-100` (auto-push via safe-push; non-ff recovery with overlap check; never force).
- command: `git show f1dbe2e70:AGENTS/DAEDALUS/builds/RAV_CHARTER.md | sed -n '178p;185p'`
- observed: none of the pre-pull STOP rule, `git commit --amend` ban (root 4b), the no-pathspec commit hazard (4c), the 100-char subject (4d), or a push/non-ff instruction reaches RAV. Fence (a) (`:91`) says RAV's cross-dir commits set no precedent, but nothing gives RAV the shared-index hazards that root's recipes exist for. Whether Will's RAV prompt adds them: UNKNOWN.
- proposed: replace step 1 with "Follow root `CLAUDE.md` § Git Protocol 'Before pulling' — read it; you do not receive it automatically", and step 8 with a pointer to root 4–4d + session-end step 2–3. Pair with R-AG-1.

**R-RAV-2 ❌ §7 Classification grades RAV against a Meta L5 leg the ladder has struck.**
- artifact: `RAV_CHARTER.md:171` ("L5 clean closeouts + roadmap") vs `AGENTS/DAEDALUS/CLAUDE.md:135` (the "+ EVOLUTION roadmap live" leg "was STRUCK from the Meta class ceiling", 2026-08-17 F28, Will-approved) and the ladder table `:129-131` (Meta L4 "builds/retirements executed clean; PATTERNS accruing", not "builds/repairs").
- proposed: replace the restated rubric with "graded on the Meta column of DAEDALUS CLAUDE.md § MATURITY LADDER" (fails c — owned there).

**R-RAV-3 ❌ (low) §7 rows 2/3 and the footer still hold a PROME-lane action that root canon now forbids.**
- artifact: `:155` ("Root `CLAUDE.md` + `AGENTS.md` lines ⛔ PROME-lane, Will-gated — PROME queued them"), `:189` ("Remaining: four PROME-lane shared-doc lines (§7 rows 2/3/4/6)"), and `:156` (rows 4/6 "flagged 8/03… Routed, not edited").
- command: `git show f1dbe2e70:AGENTS/_INDEX.md | grep -n RAV`; `git show f1dbe2e70:AGENTS/_SYNTHESIS_OPS.md | grep -n RAV`; root `CLAUDE.md:24` ("Do not re-list membership anywhere else"); `AGENTS.md:27`.
- observed: rows 4/6 are DONE (`_INDEX.md:64`, `_SYNTHESIS_OPS.md:34` both carry RAV). Rows 2/3 are obsolete BY DESIGN (WQ-120/WQ-137 removed membership from root; AGENTS.md forbids it) — "completing" them would violate root. Same stale line in `AGENTS/RAV/README.md:15`.
- proposed: mark rows 2/3 "N/A — superseded by WQ-120/137 (root and AGENTS.md carry no membership)", rows 4/6 DONE; fix the footer.

**R-RAV-4 ⚠️ Fence (a) counts root carve-outs as three; root has four.**
- artifact: `:91` ("Root `CLAUDE.md`'s three carve-outs are unchanged and this is not a fourth") vs `CLAUDE.md:76` ("Carve-outs ①–④ — four fleet-wide self-authorship carve-outs").
- proposed: "RAV's commits are not a root carve-out and set no precedent." (meaning unchanged; drop the count).

**R-RAV-5 ⚠️ §5 reconciliation block is closed but reads as open; one internal pointer is wrong.**
- artifact: `:120` ("Neither RAV-facing doc currently points at `runs/` except this one — fixed by §8 step 0"), `:125` ("Two items routed to PROME 8/03, not fixed here"), `:123` (statuses quoted title-case `Superseded`).
- command: `git show f1dbe2e70:PROME/codex/RAV_QC_WORKFLOW.md | grep -niE "reconcil|SUPERSEDED"`
- observed: workflow `:21` "RECONCILED with charter §5, 2026-08-03 EVE"; `:45` re-cased to `SUPERSEDED`. Both routed items are done. §8 step 0 is the inbox read, not a runs/ pointer (the runs/ home is §8 step 7 / §5).
- proposed: collapse `:114-125` to two lines: runs/ = run report; `PROME/codex/RAV_QC_LEDGER.md` = disposition surface (statuses per the workflow, canonical UPPER tokens).

**R-RAV-6 ⚠️ (INFERRED) A second Codex contract exists that RAV's charter does not reconcile with.**
- artifact: `PROME/codex/CHARTER.md` ("every Codex spawn prompt includes… 'Read `PROME/codex/CHARTER.md` first'"; "Read-only by default… Never touch `AGENTS/<NAME>/`") vs `RAV_CHARTER.md` §3 (bounded repair inside other agents' files).
- observed: the two describe different lanes (PROME's cross-vendor review spawns vs Will-driven RAV), but both are "Codex", and the charter's own §5 premise is "whichever document it is handed IS its charter that run". Which one a Will-driven RAV run receives: UNKNOWN.
- proposed: one line in RAV_CHARTER §1 naming `PROME/codex/CHARTER.md` as a different lane that does not govern RAV runs (or vice versa) — owner call.

### KEEP notes
- §3 repair/flag split, the load-bearing sentence (`:83`) and fences (a)/(b)/(c): VERIFIED homed in `AGENTS/WALTER/REGISTRY.tsv:18` (fences a, b "Will-approved 7/30"; FENCE 3 = (c), "adopted verbatim"), quoted here by design (`:89`). Not mechanizable (judgment) and the charter is what Codex is handed → KEEP despite the restatement; this is the one place where restating is the delivery mechanism.
- §8 step 0 (read inbox; >30-day packet is a finding about the sender): behavior-gate for a session with no boot → KEEP.


---

## 5. Cross-file contradictions

| # | Tag | Surfaces | Contradiction | Owner of the fix |
|---|---|---|---|---|
| X-1 | ❌ | `AGENTS.md:21` · `RAV_CHARTER.md:15,178,185` · root `CLAUDE.md:95-115` · ROSTER § SPECIAL (RAV) | The one agent with standing cross-dir commit authority and no CLAUDE.md load gets git rules from neither AGENTS.md ("auto-injected") nor its charter (bare "Pull.", no push/non-ff/amend/4c/4d) — = R-AG-1 + R-RAV-1 | Will/PROME (AGENTS.md) + DAEDALUS (charter) |
| X-2 | ❌ | root `CLAUDE.md:22` · `AGENTS.md:17,29-42` · `_NETWORK.md` · `REGISTRATION_CHECKLIST.md` row 3 | Root forbids route mirrors; AGENTS.md keeps one (diverged at the YURI row) and the checklist re-feeds it at every build — = S-AG-1 | Will/PROME + DAEDALUS (checklist) |
| X-3 | ❌ | ROSTER § RETIRED/SPECIAL · `RAV_CHARTER.md:24,101,112,129-141,158` · `DAEDALUS/CLAUDE.md:23,27,191` | YEYOU retired, compose-on-revival closed (ROSTER) vs charter "never run… on revival the two compose" and DAEDALUS table naming YEYOU as live owner — = S-RAV-1 + R-DA-5 | DAEDALUS |
| X-4 | ⚠️ | `DAEDALUS/CLAUDE.md:114` · `DAEDALUS/SURFACES.tsv:13` · root `CLAUDE.md:74,84,116` | DAEDALUS's Will-ruled `scripts/` commit grant (2026-07-31) is homed only in DAEDALUS's own files; root's Scope note ("Everyone else: own `AGENTS/<NAME>/` dir") and its "your directory" definition omit it, so a reader of the git canon sees a violation in every DAEDALUS scripts/ commit. `grep -n "scripts/" CLAUDE.md` → no grant line (VERIFIED). | Will/PROME (root Scope note, one clause) |
| X-5 | ⚠️ | root `CLAUDE.md:95` · `DAEDALUS/CLAUDE.md:54` | Root: the `Pushed. CONFIRMED: HEAD … (fresh fetch).` line IS the receipt. DAEDALUS: "The `Pushed.` line is not a receipt for YOUR work" — HEAD-on-origin does not prove your commit was made (failed commit inside a push train); identity = content check. Compatible (DAEDALUS stricter) but a desk reading both gets two receipt definitions; the stricter one is fleet-relevant. | PROME (root) — cite or adopt |
| X-6 | ❌ | `RAV_CHARTER.md:171` · `DAEDALUS/CLAUDE.md:129-135` | Charter grades RAV on a struck Meta-L5 "roadmap" leg — = R-RAV-2 | DAEDALUS |
| X-7 | ⚠️ | `RAV_CHARTER.md:155,189` · `AGENTS/RAV/README.md:15` · root `:24` · `AGENTS.md:27` | Pending "add RAV line to root/AGENTS.md" vs both files' no-membership rule — = R-RAV-3. README also says "charter §8 step 1" for the inbox read; the charter has it at step 0. | DAEDALUS |
| X-8 | ⚠️ | root `:13` · root `.claude/settings.json` · `PROME/BOOT.md:47` | Root prescribes in-folder launches; root hooks fire only on repo-root launches — = R-ROOT-3 (INFERRED) | DAEDALUS (settings audit) → Will |

Checked and consistent (no finding): DAEDALUS spawnability (`DAEDALUS/CLAUDE.md:5` = `AGENTS.md:46` = ROSTER § SPECIAL); CREED permission (`AGENTS.md:52` = ROSTER Tier-2 row); RAV "never on a cadence" (`DAEDALUS/CLAUDE.md:108` = `UPGRADE_PROTOCOL.md:76`); `UPGRADE_PROTOCOL.md` Step 0 exists (`:21`) as `DAEDALUS/CLAUDE.md:78` cites; RAV fences homed at `WALTER/REGISTRY.tsv:18`; DAEDALUS charter size vs read cap ruled out of scope by `READ_CAP.md` rule 20.

---

## COMPLETION
Sun Oct  4 11:44:59 EDT 2026
- **STATUS: DONE** (all four files read whole at f1dbe2e70; every pointer existence-checked; mechanization claims checked at the callsite).
- **Counts (per-file findings; cross-file X-rows mostly re-index these — only X-4, X-5 are new):**
  - root `CLAUDE.md`: ❌ 0 · ⚠️ 3 (R-ROOT-1..3) · STRIKE 0
  - `AGENTS.md`: ❌ 2 (S-AG-1, R-AG-1) · ⚠️ 1 (R-AG-2)
  - `AGENTS/DAEDALUS/CLAUDE.md`: ❌ 2 (R-DA-1, R-DA-2) · ⚠️ 10 (S-DA-1..3, R-DA-3..9)
  - `RAV_CHARTER.md`: ❌ 4 (S-RAV-1, R-RAV-1..3) · ⚠️ 3 (R-RAV-4..6)
  - cross-file new: ⚠️ 2 (X-4, X-5)
  - **Total: ❌ 8 · ⚠️ 19**
- **Could not assess / limits:**
  - Whether Codex auto-loads `AGENTS.md` on this box, and what prompt Will hands RAV/CATO — UNKNOWN (R-AG-1, R-RAV-1, R-RAV-6 rest on Codex CLI's documented default + RAV README).
  - Whether root `.claude/settings.json` hooks fire for in-folder launches — INFERRED from `PROME/BOOT.md:47`, not tested (R-ROOT-3).
  - REGISTRY row 5 free-text cell not read (blindness); its mention of "model upgrade" seen only as a `git grep -l` file match — so R-DA-2's "wired nowhere" covers scripts, not prose.
  - Did not run any gate/selftest (read-only brief); "wired" = callsite present at f1dbe2e70, not "passes today".
  - No model-version history check (would need commits after f1dbe2e70 or harness metadata) — whether a model upgrade has occurred since 2026-07-07 is UNKNOWN; if one has, the Harness Audit was due on that trigger regardless of the 90-day clock (last_run 2026-07-07 + 90d = 2026-10-05).
- **Blindness:** the only blinded content seen was the 2026-10-04 Run Log row inside the playbook I was told to read (quoted in the header); it names TERRY and LIQUID findings, none on these four files. Existence-only checks (`git cat-file -e`) on two `AGENTS/DAEDALUS/runs/` paths cited by DAEDALUS CLAUDE.md; not opened.
