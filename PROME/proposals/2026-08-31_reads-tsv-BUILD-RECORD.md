# READS.tsv — BUILD RECORD

**Built:** 2026-08-31 ~23:1x–23:4x ET (DESKTOP `DESKTOP-BC6EF81`, session `prome-90`, Opus 5 1M) · **Owner:** PROME
**Authority:** Will, direct, in-session **23:09 ET — *"lets build READS."*** Upstream: Will's five read-cap perimeter rulings made in the WALTER window ~2026-09-01 00:5xZ, relayed by `PROME/inbox/2026-09-01_from-WALTER_WILL-RULED-the-read-cap-perimeter-question-READS-tsv-spec-and-the-interim-reporting-convention.md`.
⚠️ **The relayed rulings were treated as a rec, not as clearance** — the build proceeded on Will's own word to PROME, per `finding_relayed_recommendation_is_not_an_approval`.

**Artifacts:** `PROME/registry/READS.tsv` · `PROME/tools/reads_check.py` · packets to DAEDALUS (`2026-08-31c`) and WALTER (`2026-08-31`).

---

## 1. Assertion ledger — every load-bearing claim, with the command that settled it

| # | Claim | Artifact | Verification command | Observed | Confidence |
|---|---|---|---|---|---|
| 1 | `READS.tsv` did not already exist anywhere in the repo | fs | `find . -name "READS*" -not -path "./.git/*"` | empty | **VERIFIED** |
| 2 | It is a **registered DAEDALUS item (R7-stage-2, ~9/14)**, not a free slot | `scripts/read_cap_check.py:31`, `READ_CAP.md:36`, 30 desk packets 8/28 | `grep -rn "READS\.tsv"` | named in all three | **VERIFIED** |
| 3 | `read_cap_check --agent PROME` sees **1** of PROME's boot reads | tool output | `python3 scripts/read_cap_check.py --agent PROME` | `1 whole-read file(s) found`; only `STATUS.md` | **VERIFIED** |
| 4 | PROME's real boot-read manifest is **11 declared rows** (7 cap-bearing) | `PROME/CLAUDE.md` Boot 1–2 + `BOOT.md` 0–6 | line-by-line enumeration, this session | 11 rows | **VERIFIED** |
| 5 | `PROME/GATES.tsv` is **52,308 B = 161% of budget, 96% of the physical cap**, and `BOOT.md` step 3 says "Read" it | `PROME/GATES.tsv`, `BOOT.md:51` | `PROME/tools/measure.py` | 52,308 B | **VERIFIED** |
| 6 | `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` = **45,248 B = 139%**, mandated whole by WALTER:6b, in neither desk's perimeter | the file + `WALTER/CLAUDE.md:63` | `measure.py`; `read_cap_check --agent WALTER`/`--agent RED` | 45,248 B; absent from both | **VERIFIED** |
| 7 | WALTER's packet and WALTER's charter name **different fired-log files**; all four exist | `WALTER/CLAUDE.md:63-69` vs the packet | `find AGENTS -path "*registry*" -name "*_LOG.tsv"` | charter → 2 WALTER-local; packet → 2 in CREED/HANS | **VERIFIED** |
| 8 | Stored byte figures rot inside one session (the no-byte-column argument) | `WALTER/CLAUDE.md` steps 1–2 | `measure.py` on both paths | step 1 says 20,288 (live **21,438**); step 2 says 46,327 (live **13,956**) | **VERIFIED** |
| 9 | `memory/auto/MEMORY.md` is **19,016 B = 74.3%** — under the 75% trip line | the file | `PROME/tools/measure.py` | 19,016 B | **VERIFIED** |
| 10 | WALTER (`walter-09`) was **live and busy** during the build ⇒ read-only against its tree | harness | `ListAgents` | `walter-09 · interactive · busy` | **VERIFIED** |

**No claim in the packets rests on an un-run command.** Byte and crc figures come from `PROME/tools/measure.py` only (WQ-140).

## 2. Design decisions, and the failure each one is aimed at

1. **The reader owns the row (Will ruling ①).** One path may appear under several readers, and under one reader at several boot steps. Both are correct; the validator flags a duplicate only on the WHOLE key. Live instance of the second case: `WILL_QUEUE.md` is `summary` at BOOT.md-5 (via the gate) **and** `scoped` at BOOT.md-8 (a session reading the OPEN table to brief Will).
2. **⛔ No byte column.** The registry declares WHAT IS READ; the checker measures at run time. Evidence = ledger row 8: two figures in WALTER's own charter went stale, one of them inside the session that wrote it.
3. **⛔ An unattested desk is UNKNOWN, never clean** — enforced in code, not in prose: a desk with no `ATTESTATION` row cannot return `rc=0` however many green rows it has. This is WALTER's own generalisable finding compiled into the instrument: *a per-agent check fails by reporting CLEAN rather than UNKNOWN.*
4. **`declared_by` exists because `mode` is the corruptible field.** It is a claim about the SESSION, not the file, and an author describing their own tooling will describe it charitably (`finding_a_charitable_reading_of_your_work_is_the_one_to_check`). Rows carry who asserted them: `WALTER`, `WALTER(packet)`, `PROME`, `PROME(from-charter)`.
5. **The heuristic was NOT imported.** DAEDALUS's 8/28 fleet scan could have pre-filled 30 desks in minutes. Declined: **a heuristic laundered into a declaration is worse than no declaration**, because it is then quoted as one. Two desks are declared; 37 print as UNKNOWN. That is the honest state.
6. **Constants are imported, never restated.** `BUDGET_BYTES` / `CAP_BYTES` / `ROTATE_AT` come from `scripts/read_cap_check.py`, whose canon says the constants live there and nowhere else.
7. **The seam with DAEDALUS is declared, not assumed silently.** PROME owns the declaration half; the consumer half (`scripts/`, plus the rollout to the 30 packeted desks) stays DAEDALUS's R7-stage-2. Offered back in full if DAEDALUS wants it.

## 3. Two corrections made to my own work before commit

Both found by reading the tool's own output rather than by testing — worth recording, because a 10/10 selftest sat clean through both.

1. **A flat `✅` up to 100% of budget rendered 98% and 13% identically** — the instrument's own clean-report failure. Fixed: `🟠 ROTATE-TIER` at ≥75% (`READ_CAP.md` rule 5), `⚠️` over budget, `🔴` over the physical cap.
2. **The rule-8 advisory over-claimed against ledgers.** v1 printed *"owner still owes a split"* against `PROME/DOCKET.tsv` (219,609 B, read by a script that prints one line). But `READ_CAP.md`'s own "what binds" table says a ledger read by a script is the cold class, where *"a large one is discovery, never a defect."* Fixed: rule 8's demand now fires only for `scoped`; `summary`/`grep` get a neutral cold-class line. **Canon amendment proposed to DAEDALUS rather than written into its file.**

## 4. Findings the build produced

1. **⭐ The cross-agent read is now visible and attributed.** `reads_check --agent WALTER` → `rc=1` on RED's 139%-of-budget registry. It was measured by nobody yesterday, and both desks could print a clean read-cap verdict without it.
2. **PROME's own boot protocol says something false, and the registry is what exposed it.** `BOOT.md` step 3 says *"Read `PROME/GATES.tsv`"*; the file is 161% of budget and what runs is a bounded script check. **On cap grounds nothing is owed** (cold class) — **the debt is protocol-text accuracy, and it is PROME's.** Recorded in the row rather than hidden by it. *(Owed: a step-3 rewrite naming the real operation.)*
3. **A second defect axis, unnamed in current canon.** Cap breach (gradeable by an instrument) and protocol accuracy (*does the step's verb describe the operation that runs?* — gradeable by no instrument) are independent. An honest `mode` is the only thing that makes the second visible. Proposed to DAEDALUS for `READ_CAP.md`.

## 5. What a `rc=0` from this tool does NOT prove

It is a claim about the **declaration**, not about the desk. If the declaration is wrong the verdict is wrong — which is why `declared_by` exists and why attestation is the reader's own act. **`--selftest` 10/10 proves nothing on its own**: same author wrote the code and the cases (error #52's shape, banked 8/30). The independent check is the blind cold read below, and the standing invitation in both packets is to **attack the falsification set, not re-run it.**

## 6. Blind cold read (pre-commit) — **6 BLOCKING, all fixed**

Run by the `coldreader` agent against both files before first commit, per `PROME/CLAUDE.md` § Session Process Controls. **Score 18/30 ✅ · 6 ⚠️ · 6 ❌.** It ran the tool four ways and hand-built seven adversarial cases. **Every ❌ was accepted without dispute; none was a misreading.**

| # | Blocking finding | Disposition |
|---|---|---|
| ❌1 | **The ⛔ "only the desk can attest" rule was NOT enforced.** `attested()` matched on `reader` alone and never read `declared_by` — so an ATTESTATION row for desk T signed by anyone flipped T from UNKNOWN to clean. **The reader built the bypass row.** Worse: the registry already ships `PROME(from-charter)` rows, so the defeating mechanism was in live use in the same file. | **FIXED.** Attestation is valid only where `declared_by` == `reader`; invalid ones print `⛔ INVALID ATTESTATION` and do not clear the desk. Rule written into the header (PROME may TRANSCRIBE under the reader's name; `PROME(from-charter)` can never attest). **Two new negative controls** (#11, #12). |
| ❌2 | **`--fleet` precedence inverted against its own docstring.** `max(rc, 2)` meant WALTER's genuine 139%-of-budget breach exited **rc=2 (CANNOT-EVALUATE)**, so a gate keyed on the stated contract reads "couldn't evaluate" over a live finding. | **FIXED.** Breach → 1; else undeclared → 2; else 0. Verified: `--fleet` now exits **1**. |
| ❌3 | **The tool collapsed the two defect axes on the exact row the header forbids collapsing** — printing `nothing owed` against `GATES.tsv`, whose own `notes` say a step-3 rewrite IS owed. | **FIXED.** Cold-class note now reads "nothing owed **ON CAP GROUNDS**" and points at the row's notes for the protocol-accuracy axis. |
| ❌4 | **A false completeness claim inside an ATTESTATION row** — notes said "enumerated from BOOT.md steps 0-6"; BOOT.md has steps **0–9**, and row `PROME:BOOT.md-8` cites step 8. A stranger cannot tell whether 7/9 were checked-and-empty or skipped. | **FIXED.** Re-enumerated and stated: steps 7 and 9 mandate no read; step 8's reads were already declared. Manifest substantively complete; the label was wrong. |
| ❌5 | **"Replaces the read-cap PERIMETER HEURISTIC" — present tense, false**, and self-contradicted 50 lines later by PROVENANCE. `read_cap_check.py` still scans charters. | **FIXED.** Header now leads with what it does NOT do yet. |
| ❌6 | **"the checker" names two different tools inside one header**, so a stranger cannot tell whether ruling ④'s interim convention is live. | **FIXED.** Both tools named explicitly, with which one consumes this file today and which does not. |

**Also fixed from the ⚠️ set:** #10 — RETIRED rows were counted in the "manifest of N declared read(s)" on the ✅ line while being measured not at all (a manifest of one retired row printed a clean bill having measured nothing). Retired rows are now counted separately and the ✅ line claims only the cap-bearing count. Negative control #13. **#8** date-basis ambiguity (ET filename vs UTC ruling) → declared in the header.

**Falsification set: 10 → 13 cases, all passing.** The three additions came from the cold reader, not from me — and case #11 is the bypass it built by hand. That is the difference between a suite and a test.

⏳ **Still owed:** the reader's sections B–D (stranger-execution test, output-vs-promise, and its list of MISSING falsification cases) truncated in transit and were re-requested. **Section D is the one that matters — inputs where this checker gives a wrong verdict and no test catches it.** It gets its own round; this record is not the end of the review.
