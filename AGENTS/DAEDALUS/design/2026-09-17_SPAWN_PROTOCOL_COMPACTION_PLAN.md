# SPAWN PROTOCOL compaction — plan for independent read BEFORE application (rule 4a: the remedy is the review object)

**Date:** 2026-09-17 20:5x ET · **Authority:** Will "approved go ahead" on CATO `87776263a` step 1 ("move explanatory history to its existing archive with resolvable pointers, preserving commands, order, conditions and authority") · **Scope:** `AGENTS/DAEDALUS/CLAUDE.md` § SPAWN PROTOCOL only (the boot + closeout section the comparison was about). Other sections untouched.

## 1. Mechanics
- The ORIGINAL section (7,541 B, crc32 1151981870) is moved VERBATIM to `archive/CLAUDE_ARCHIVE_2026-09.md` as **block 6**, in the file's existing format (`## block N — <what> (line L), rotated <date> (crc32 <dec>; <bytes> B)`).
- The COMPACT section (§2 below, 6260 B, 17% smaller) replaces it in place. Every pointer in it resolves (blocks 4, 5, 6; `outbox/delivered/`; root CLAUDE.md steps).
- Two ADDITIONS are made and declared, not slipped in: step 3b (inbox read — existing practice, now a step, so the READS attestation can name it) and the step-9 report form (RAN / NOT-APPLICABLE / FAILED / UNKNOWN — CATO correction #5).
- One RE-SCOPING: the verify_push clause now says the subject LOCATES and the content check is IDENTITY (CATO correction #4). Nothing else changes meaning.

## 2. Proposed compact text (verbatim as it will be written)

```markdown
## SPAWN PROTOCOL

When spawned with a task:

1. **Read `STATUS.md`** — your current state, open builds, standing structural debt.
2. **Read `FLEET_DIRECTORY.md`** — the GENERATED hot index of the maturity map: per agent class · level · confidence · last-scored · what it does · missing/next. **`FLEET_MAP.tsv` is the COLD full register** — it owns the complete Gaps/Next_upgrade text; read it **per-agent on demand** (`grep -P '^AGENT\t' FLEET_MAP.tsv`) when you work that agent, and **whole at a Production Review**. **Cold ≠ unwatched:** `sweeps_due.py`'s SELF-ROW line, the Production Review and the co-registration guard all read FLEET_MAP. ⚠️ **Never hand-edit `FLEET_DIRECTORY.md`; regenerate on every row change (step 7).** *(Story → `archive/CLAUDE_ARCHIVE_2026-09.md` block 4.)*
3. **Read `PATTERNS_HOT.md`** — the generated one-line index of design lessons dated within a **rolling 45-day window** (+ `[HOT]`-tagged rows). *Apply them; don't re-learn them.* Older rows sit in `PATTERNS_COLD_INDEX.md` (generated, grep on demand, NOT a boot read); full rows from `PATTERNS.tsv` by ID. The byte guard on every boot read is `read_cap_check.py` at closeout (step 9), never this line's promise. *(Story → archive block 5.)*
3b. **Read `inbox/`** — every packet present, whole; disposition each before idling. *(Encoded 2026-09-17: the read was practice at every session, not a numbered step — a declared perimeter must name it.)*
4. *(conditional)* **`EVOLUTION.md`** — read only when the task touches the standard itself (blueprint work, gradings against a changed rubric, roadmap questions); skip on routine sweeps/reads.
5. **Cadence-check** — run `python3 "$(git rev-parse --show-toplevel)/AGENTS/DAEDALUS/scripts/sweeps_due.py"` (cwd-proof, read-only; also carries the profile-clock, SELF-ROW and DIRECTORY-STALE lines). If a sweep is **DUE**, surface it to Will/PROME. *Detection autonomous; dispositions approval-gated.* Registry: `sweeps/REGISTRY.tsv`; playbooks: `sweeps/`.
5b. **R1 corrections check** — `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" DAEDALUS` (§9 rc 0/1/2; rc=1 = a NAMED correction is unreceipted: read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` + commit your receipts file).
6. **Execute the task** (build / maintain / score / retire — see JOBS).
7. **Write results back** — update `STATUS.md`; log new lessons to `PATTERNS.tsv`; update `FLEET_MAP.tsv` rows you re-scored. **Write-back tail rule:** when you process an inbound write-back (an owner applied your routed work), close the WHOLE chain — the FLEET_MAP row AND the originating `upgrades/` card AND the batch doc's banner *(a former fourth leg, outbox/delivered/ copies, is STRUCK — its record is `outbox/delivered/`'s FROZEN banner)*. Your own surfaces are IN SCOPE of all three sweeps (PAT-050 self-inclusion) — including your own FLEET_MAP row's currency. **If you changed ANY `FLEET_MAP` row (or ROSTER classification shifted), regenerate the directory: `python3 "$(git rev-parse --show-toplevel)/AGENTS/DAEDALUS/scripts/render_directory.py"`** (GENERATED join of ROSTER+FLEET_MAP; never hand-edit it, edit the sources; fails loud on format-change/unhandled agent). Append to `EVOLUTION.md` if the standard changed. **If you ran a sweep, update its `sweeps/REGISTRY.tsv` row (`last_run` + `last_findings`) + the playbook Run Log.**
8. **Deliver before idling** — `SendMessage` the result to your caller AND write it to a file. Never idle "holding."
9. **Closeout battery** — run every step **by name** and report each as RAN · NOT-APPLICABLE (with the reason) · FAILED · UNKNOWN — never silence:
   - root CLAUDE.md session-end **1b** orphan_check · **1c** consumer_check (you PUBLISH figures other agents cite: byte budgets, rc contracts, thresholds) · **1c-bis** ledger nudge · **1d** memory checks · **1e** claim_check (cite root, don't restate);
   - **re-cut your own FLEET_MAP row** if the session re-scored you (the SELF-ROW line in `sweeps_due.py` fires at boot when this slips ≥5d);
   - **`scripts/regen_patterns_hot.py`** if PATTERNS.tsv changed (conservation-checked);
   - **`python3 scripts/read_cap_check.py --agent DAEDALUS`** — the ROOT tool. ⚠️ Two tools share this basename: repo-root `scripts/read_cap_check.py` is the fleet tool and takes `--agent`; `AGENTS/DAEDALUS/scripts/read_cap_check.py` is the local FILE-LIST checker that imports its constants. Standing rule: two tools may not share a basename across `scripts/` and `AGENTS/<NAME>/scripts/`. The byte budget is RE-DERIVED from the harness read cap (§9 rc 0/1/2). ⛔ **If it fires, trim/rotate/relocate — never raise the budget: the read cap is not ours to move.**
   - **`python3 AGENTS/DAEDALUS/scripts/complete_check.py`** — the COMPLETE-check, work-finished beside files-committed (PAT-101/102): pairing + pair-symmetry + EVOLUTION-placement legs gate rc; the claim walk-list you WALK before closing;
   - **commit path-scoped** (GIT below) → **`scripts/safe-push.sh`** → **`bash AGENTS/DAEDALUS/scripts/verify_push.sh "<commit subject>"`** — §9 rc contract: **0 on origin · 1 genuinely NOT on origin · 2 CANNOT-CERTIFY** (retry; never read cannot-certify as absent — under concurrent git activity the remote-tracking ref is momentarily unreadable, which reads identically to "my commit is absent"). **The `Pushed.` line is not a receipt for YOUR work.** The subject LOCATES the commit (a rebase rewrites unpushed hashes); IDENTITY is the content check — `git show origin/master:<path> | md5sum` on files you care about `[[finding_push_train_hides_a_failed_commit]]`;
   - **if this session declared or amended a rule, apply it to the artifact that declares it before closing** — one re-read of what you just wrote, the cheapest instance of PAT-050 there is.

*(How each step was earned — the 8/17 self-audit that found no closeout sequence, the 8/19 silent push failure and the retracted one-liner, PAT-115's same-diff counterexample, the 9/02 basename collision, the 8/23 hot/cold re-homing and the six days FLEET_MAP sat at 121% — verbatim in `archive/CLAUDE_ARCHIVE_2026-09.md` block 6, crc32 1151981870; 7,541 B.)*

```

## 3. Preservation checklist — every command · order · condition · authority clause in the ORIGINAL, and where it lives in the COMPACT

| # | Clause (original) | Class | In compact? | Where |
|---|---|---|---|---|
| 1 | Step 1 read STATUS.md — state, open builds, structural debt | read | yes | step 1 verbatim |
| 2 | Step 2 read FLEET_DIRECTORY.md as GENERATED hot index; column list | read | yes | step 2 |
| 3 | FLEET_MAP.tsv is COLD; owns full Gaps/Next_upgrade; per-agent grep command; whole at Production Review | condition + command | yes | step 2 |
| 4 | Cold ≠ unwatched: sweeps_due SELF-ROW, Production Review, co-registration guard read FLEET_MAP | condition | yes | step 2 |
| 5 | Never hand-edit FLEET_DIRECTORY; regenerate on every row change (step 7) | authority | yes | step 2 |
| 6 | Step 3 read PATTERNS_HOT.md; rolling 45-day window + [HOT]; apply don't re-learn | read + condition | yes | step 3 |
| 7 | Cold index generated, grep on demand, NOT a boot read; full rows by ID in PATTERNS.tsv | condition | yes | step 3 |
| 8 | "the guard is the promise; the prose is only its label" — closeout runs read_cap_check instead of trusting this line | condition | yes (reworded) | step 3 last sentence |
| 9 | Step 4 EVOLUTION.md conditional — when task touches the standard; skip on routine sweeps | condition | yes | step 4 verbatim |
| 10 | Step 5 sweeps_due.py exact command; cwd-proof; read-only; DUE ⇒ surface to Will/PROME; detection autonomous, dispositions approval-gated; registry + playbook paths | command + authority | yes | step 5 (+ names the three extra lines it now carries) |
| 11 | Step 5b corrections_boot_check exact command; rc 0/1/2; rc=1 procedure incl. --receipt actions and commit | command + condition | yes | step 5b verbatim |
| 12 | Step 6 execute (build/maintain/score/retire) | order | yes | step 6 verbatim |
| 13 | Step 7 write-back: STATUS, PATTERNS, FLEET_MAP rows re-scored | order | yes | step 7 |
| 14 | Write-back tail rule: close FLEET_MAP row AND upgrades/ card AND batch banner | condition | yes | step 7 |
| 15 | Former fourth leg (outbox/delivered) STRUCK, record at its FROZEN banner | history + pointer | yes (pointer kept) | step 7 parenthetical |
| 16 | Own surfaces in scope of all three sweeps (PAT-050), incl. own FLEET_MAP row currency | condition | yes | step 7 |
| 17 | Regenerate directory on ANY FLEET_MAP row change or ROSTER shift; exact command; never hand-edit; fails loud | command + authority | yes | step 7 |
| 18 | Append EVOLUTION if standard changed | condition | yes | step 7 |
| 19 | Sweep run ⇒ REGISTRY row last_run + last_findings + playbook Run Log | condition | yes | step 7 |
| 20 | Step 8 deliver before idling — SendMessage AND file; never idle holding | authority | yes | step 8 verbatim |
| 21 | Step 9 root 1b–1e by name; consumer_check emphasis (published figures); cite root don't restate | command | yes | step 9 bullet 1 (+1c-bis added: root lists it; the original omitted it) |
| 22 | safe-push.sh at closeout | command | yes | step 9 push bullet |
| 23 | Re-cut own FLEET_MAP row if re-scored; SELF-ROW fires at ≥5d | condition | yes | step 9 bullet 2 |
| 24 | Regenerate PATTERNS_HOT if PATTERNS.tsv changed; conservation-checked | condition | yes | step 9 bullet 3 |
| 25 | read_cap_check ROOT tool with --agent; two-tool basename warning; local namesake is file-list checker; standing basename rule 9/02 | command + condition + rule | yes | step 9 bullet 4 |
| 26 | Budget re-derived from harness read cap; §9 rc 0/1/2; all three paths watched | condition | yes (the "watched on real cases" provenance → archive) | step 9 bullet 4 |
| 27 | If read-cap fires: trim/rotate/relocate, never raise the budget | authority | yes | step 9 bullet 4 |
| 28 | complete_check.py — pairing + pair-symmetry legs (PAT-101/102) + claim walk-list you WALK | command + condition | yes (+ EVOLUTION-placement leg named — it exists in the script since 8/21) | step 9 bullet 5 |
| 29 | Verify own commits reached origin; Pushed. is not a receipt for YOUR work | condition | yes | step 9 push bullet |
| 30 | verify_push.sh command; rc 0/1/2; cannot-certify is its own state with retry; concurrent-git reason | command + condition | yes | step 9 push bullet |
| 31 | Verify by SUBJECT not hash (rebase rewrites); memory link | condition | yes, RE-SCOPED per CATO #4: subject LOCATES, content check is IDENTITY | step 9 push bullet |
| 32 | Content check `git show origin/master:<path> \| md5sum` | command | yes | step 9 push bullet |
| 33 | Rule declared/amended this session ⇒ apply to the artifact that declares it before closing | authority | yes | step 9 last bullet |
| 34 | Step 9 report form RAN / NOT-APPLICABLE-with-reason / FAILED / UNKNOWN | NEW (CATO #5) | added | step 9 lead line |
| 35 | Step 3b read inbox/ | NEW — declared existing practice (CATO: "do not silently expand every-boot scope" — this is the non-silent form) | added | step 3b |

**Moved to archive block 6 (history only, no live clause):** the 8/17 self-audit F3 story · the 8/19 silent-push story and the retracted `merge-base --is-ancestor` one-liner · PAT-115's same-diff counterexample story · the 9/02 basename first-diagnosis story (already block 1) · the 8/23 hot/cold re-homing and the 121% FLEET_MAP story (already blocks 4/5) · the 8/17 F37/PAT-111 split note · the 7/07 harness-audit S6 demotion note · the 7/12 self-sweep "6 cards + 9 outbox files stale" count · the "first run caught its own author" note on complete_check · the density-constant history.

## 4. Reader acceptance criteria (opus, blind to my reasoning; brief carries the ORIGINAL and the COMPACT, not this checklist's verdicts)
- A. Every row 1–33 above: confirm the clause is present in the compact with the same COMMAND text, the same ORDER position, the same CONDITION and the same AUTHORITY (who may / must). Report any row where the compact weakens, strengthens, or re-orders it. A reworded clause passes only if a stranger would act identically.
- B. Find any live clause in the ORIGINAL that the checklist does NOT list (the checklist is the author's enumeration — PAT-136).
- C. The two additions (34, 35) and the one re-scoping (31): state whether each is what the plan says it is, and nothing more.
- D. Counterexample: state the one clause you would expect a compaction like this to lose, and whether it was lost.
- Output: a table of FAIL rows first, then PASS count, then B/C/D. No edits.

## 5. Post-read amendments — APPLIED before landing (reader `2026-09-17_SPAWN_PROTOCOL_COMPACTION_READER.md`: 31/33 PASS, 2 FAIL, 4 uncovered clauses, 4 undeclared corrections)
| Reader item | Disposition |
|---|---|
| FAIL row 24 — `scripts/regen_patterns_hot.py` does not exist at repo root | FIXED: `python3 AGENTS/DAEDALUS/scripts/regen_patterns_hot.py`. The reader's §D sting stands: the basename-ambiguity rule was preserved and broken in the adjacent bullet by its own author (PAT-050 n+1). |
| FAIL row 22 — safe-push moved from battery position 2 to after the checks, `commit path-scoped` added | KEPT and DECLARED: the original's order (push before three checks that exist to run before a push) was incoherent; the compact runs checks → commit → push → verify. A re-order is a meaning change and is now declared here, not hidden in "nothing else changes." |
| B1 — "don't restate" instruction dropped | RESTORED ("recorded ONLY at … FROZEN banner; don't restate") |
| B2 — charter → block 4 → EVOLUTION (c) chain dead-ends (c rotated to EVOLUTION_ARCHIVE block 1) | FIXED inline in step 2's pointer (archive blocks are crc-sealed, never edited) |
| B3 — "a generated file cannot be rotated" constraint dropped | RESTORED in step 9 regen bullet ("split the ROW SET") |
| B4 — the retracted `merge-base --is-ancestor` DO-NOT dropped | RESTORED as one clause in the verify bullet |
| Row 34 rider — "by name" widened from root 1b–1e to every step | DECLARED, intended |
| Row 35 riders — "whole" and "disposition each before idling" | DECLARED, intended: both are the existing practice the step encodes |
| Undeclared accurate corrections: row 10 (sweeps_due's three carried lines) · row 28 (complete_check's EVOLUTION-placement leg) · row 21 (1c-bis explicit) · row 22's `commit path-scoped` | DECLARED here; all verified by the reader against the artifacts; direction = charter toward what the scripts do |
| Format note — archive block headers duplicate the label | MATCHED the file (`## block 6 — block 6 — …`); fixing all six is a separate hygiene item |

**POST-REVIEW (rule 4b label — landed AFTER the read, not in the reviewed set):** step 5 and step 9 each gained a lead sentence pointing at `scripts/daedalus_gate.py boot` / `closeout` / `verify` (built this session after the read; spec `design/2026-09-17_DAEDALUS_GATE_SPEC.md`, drills `runs/2026-09-17_DAEDALUS_GATE_BUILD.md`). The enumerated steps are unchanged and stay as the runner's spec. Not re-read by the reader; declared so the next reader knows which bytes were reviewed.

**Honest size result:** compact **7,300 B** vs original 7,541 B = **3% smaller**, not the 18% of §1 — the four restorations, the declared riders and the runner pointers added ~1.1 KB back. The deliverable is the history out of the boot path (1.7 KB of incident narrative now in block 6) and the runner wired, not a byte figure; PAT-161 says rewording compressed text grows it, and it did.
