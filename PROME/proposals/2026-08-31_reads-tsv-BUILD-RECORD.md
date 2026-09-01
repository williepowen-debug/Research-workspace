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

## 7. Cold read, ROUND 2 — a seventh blocker and nine missing falsification cases

The reader's sections B–D arrived after the first commit and were **more valuable than round 1**, because they attacked the assumptions the falsification set shared rather than the code it covered. Its framing: my 10 cases all assumed *`declared_by` is honest, `path` is a real repo file, and the sheet is well-formed* — and it went hunting outside all three.

**❌7 — AN ATTESTATION NEVER EXPIRED, in a file whose entire argument is that stored values rot.** `declared_on` was shape-checked and never compared to anything. The reader ran an attestation dated **2019-01-01**: it printed `manifest ATTESTED 2019-01-01` and certified **`✅ READS-CAP 0`**. The header spends five lines arguing a stored byte is "a stale mirror within hours" — then stored the one value that gates `rc=0` with no expiry. A desk attests once, its boot protocol changes for a year, the tool keeps saying clean. `finding_dated_stamp_is_a_trigger_not_a_shield`.
⇒ **FIXED, and content-derived rather than clock-keyed:** an attestation names in `path` the protocol it enumerated, so a **git COMMIT to that file after `declared_on`** makes it STALE and drops the desk to UNKNOWN. Commit date, never mtime (root canon: a git sync restamps mtime, so an mtime-keyed check fails false-negative). It immediately caught four of my own test fixtures attesting to a protocol file that does not exist.

**⭐ D1 — MODE-FLIP LAUNDERING, the most important finding of the night.** Re-declaring the ⭐ 139%-of-budget headline row as `summary` took the tool from `rc=1` to a clean `rc=0`, printing *"correctly NOT a breach and nothing owed."* **A breach is erasable by one word, in the field the header itself calls the most corruptible.**
⇒ **Fixed as far as it CAN be honestly fixed.** No instrument can adjudicate whether contents entered a session's context, so the tool must not pretend to rule — but it must never let the claim pass silently. Every over-budget row excused by declaration is now printed in a `⚠️ MODE IS A SELF-ASSERTED CLAIM` block **with whoever signed the excuse**, and the verdict line says the exclusion was by declaration, not by measurement. Running it against the live registry immediately names **PROME's own four excused rows.**

| Case | Was | Now |
|---|---|---|
| D3 attested desk with **zero** READ rows | `rc=0` — "manifest of 0 declared read(s) is under budget" | **rc=2** — nothing measured is UNKNOWN |
| D12 every row `RETIRED-*` | `rc=0`, measured nothing | **rc=2** (same rule; my case 13's expectation was superseded and flipped) |
| D4 one reader, one path, one step, **two modes** | `rc=0` | **rc=1** — dedup key now excludes `mode`, so a contradiction is caught while ruling 1's legitimate multi-rows still pass |
| D5 `path` is a **directory** | `rc=0` — 4,096 B, 13% | **rc=1** — `isfile`, not `getsize` |
| D6 `path` absolute (`/etc/hostname`) | `rc=0` — 16 B, measured outside the repo | **rc=1** — `os.path.join` ate the leading `/` |
| D8 invalid mode | header printed `1 declared read(s) = 0 + 0` | bucket arithmetic is exact; UNCLASSIFIED rows are counted and named |
| D9 `row_kind` typo (`Read`) | row **silently vanished** from the perimeter — `0 declared read(s)` over a 52 KB whole read | counted as UNCLASSIFIED, never dropped |
| D11 `--agent` with no value | uncaught `IndexError`, exit outside the 0/1/2 contract | **rc=2** with a usage line |
| D10 fleet precedence | **structurally untestable** — the harness only ever called `report_agent` | the harness now asserts on OUTPUT as well as exit code |

**Falsification set: 13 → 20 cases, all passing. Ten of the twenty came from the cold reader.** Five of my existing cases failed on the first run of the hardened code — every one a fixture defect the new rules exposed, which is the guard working on its own author.

**Stranger-execution test (section B) — four forced guesses, two still open:** what `path` means on an ATTESTATION row (now defined and enforced: the protocol enumerated, and it must exist); who may assert `manifest-complete` (now enforced); **`source_boot_step` grammar is still unruled** — three incompatible shapes ship in the file (`PROME:CLAUDE.md-Boot-1`, `PROME:BOOT.md-3`, `WALTER:6b`), with no rule and no validation, and the field is part of the duplicate key, so guessing wrong silently defeats dedup. **Owed.**

⏳ **Still owed:** section C (output vs. promise) and the tail of B, truncated again in transit; the `source_boot_step` grammar; a re-verify pass on the hardened build. **This record is not the end of the review, and the tool is 20-for-20 on a set it has now been taught — which is not the same as being right.**

## 8. WALTER attested within the hour — and the attestation found four reads nobody had registered

WALTER's own word, 2026-08-31 ~21:0x ET (commit `2be6952b2`), registered under `declared_by: WALTER`. **Every byte figure it gave was verified at the artifact before registration; all four were exact.**

**⭐ The finding that matters is PROME's.** `PROME/state/ORCH_LOG.tsv` — **58,230 B = 179% of budget and 107% of the 54,250 B PHYSICAL CEILING** — is mandated at every WALTER boot (step 9b, to establish who is IN-FLIGHT before doorbelling). **It is PROME's file, it was measured by nobody, and it cannot be read whole by anyone.** Second PROME-side finding of the night, after `BOOT.md` step 3. **OWED: a split or rotation.** Not done at 00:2x — rotating a live ledger is exactly the broad edit the correction-count late-session rule says to defer.

Also registered: `AGENTS/*/STATUS.md` headers as a **class row** (39 files, ~1.94 MB whole; only the `Updated:` block is the input) — ⚠️ `reads_check` does not expand globs, so the row is declared-and-visible but unmeasured, a known gap recorded rather than hidden. Plus two conditional LIAISON reads, both dormant today: CARL 46,069 B (142%) and **RED 67,806 B (208% of budget, 125% of the ceiling — the largest declared read in the registry)**. A conditional read is still a mandated read when its condition holds; this is the obligation class that goes invisible precisely when it fires.

**⭐ THE ROOT CAUSE, IN THE READER'S OWN WORDS, IS THE ARGUMENT FOR `declared_by == reader`:** WALTER's steps 8, 9 and 9b each **named a FILE without naming the OPERATION** — the same defect that shipped two operator-facing defects out of its step 1, where the charter said "read" and what executed was `sed -n '1,45p'`. **PROME could not have found these by reading the charter, because the charter was wrong.** Only running the boot exposes it. That is precisely why the cold reader's ❌1 fix — an attestation must be the desk's own word — is load-bearing rather than ceremonial.

**Both PROME attributions it corrected were the ones PROME had flagged as uncertain:** the two fired logs move `6b → 6c` (6b says they *may* be read, which is permission; 6c's repeat-fire suppression is what *mandates* them). All four boot tools are `summary` per ruling 3, with two conditional follow-on reads noted in their rows — `corrections_boot_check` at rc=1 and `intake_scan` at 7e(d.1) both send the session onward to a real read the bounded output does not cover.

**And WALTER applied the no-byte-column argument back to its own charter:** it did not update the two stale figures, it **removed** them, with a "NO BYTE FIGURE HERE, DELIBERATELY" note and a pointer to `reads_check` — because updating a number in prose just resets the clock on the same failure. It also self-flagged `AGENTS/WALTER/CLAUDE.md` at 53,960 B = 99.5% of its auto-load cap, up from 94% at boot, rotation owed.

## 9. Review round 3 (Will, relayed) + WALTER's retraction — the pilot's five gates

**Verdict received: "excellent architecture and a meaningful improvement over the heuristic, but it is still a pilot. Fix the incomplete PROME perimeter and false fleet enumeration before allowing `READS-CAP 0 [PROME]` to function as an authoritative clean result."** All five items verified at the artifact; four confirmed, one already fixed with a better point underneath it.

1. **PROME's manifest omitted its programmatic inputs — CONFIRMED, and the diagnosis was sharper than the symptom.** It declared GATES/DOCKET/WILL_QUEUE `summary` but omitted the symmetry check, dashboard state, harness caps, the BOARD diff + cursor, the firetime allowlist, corrections receipts + register + fleet directory, the STATUS fan-outs and the `.claude` parity trees — **so it mixed two models of what a manifest IS**, which made "complete" too strong. **Model now DECLARED in the attestation:** *every surface a boot step causes to be read, whether it lands in context or only feeds a bounded verdict.* **11 rows added; PROME re-attested against the stated model.** Three of the additions are cross-agent (`AGENTS/WALTER/registry/CORRECTIONS.tsv`, `AGENTS/DAEDALUS/FLEET_DIRECTORY.md`, and `BOARD/INDEX.md` — the last being ruling 1 in its intended form: **the same path declared by two readers at two steps with two different operations**).
2. **Fleet discovery — the `.claude`/`_archive` symptom was already fixed hours earlier, but the point underneath was right and my fix was still a heuristic.** Membership now parses **`PROME/ROSTER.md`**, honouring the exclusion classes, and **fails loud (`rc=2`) rather than falling back to the filesystem** — degrading quietly to the heuristic is how a wrong denominator gets quoted as a fleet verdict. ⭐ Proof the prefix filter was still wrong: ROSTER correctly excludes **ATHENA**, an ARCHIVE SOURCE with a live directory that my filter counted as a desk owing a declaration. Denominator 43 → 42.
3. **Attestations could still rot — CONFIRMED.** The staleness check watched only the ONE file the attestation named, so nothing aged it when `CLAUDE.md` or `prome_gate.py` changed. **New `BASIS` row kind:** a reader declares the surfaces that DEFINE its boot, and a commit to ANY of them after `declared_on` makes the attestation stale. **A desk with no `BASIS` rows is stale by construction** — it has no dated basis. PROME declares five: `PROME/CLAUDE.md`, root `CLAUDE.md`, `prome_gate.py`, `board_scan.py`, and the `/boot` runner.
4. **Exactly one attestation per reader — CONFIRMED and enforced.**
5. **All six named negative tests added.** Set is now **26 cases, 26 passing.** Adding them broke six existing fixtures — every one a fixture that had been asserting clean without a basis, i.e. the new rule catching its own author for the third time tonight.

**WALTER RETRACTED its attestation the same hour** (packet `2026-09-01b`, commit `8eef19a29`) after re-walking its charter against the registered rows: **five more mandated reads, including `design/SIGNAL_PROCESSING_CHECKLIST.md` at 114,310 B = 351% of budget and 211% of the physical ceiling — unconditional, every boot, and its own file.** Its root cause is the one its first attestation named, turned on itself: *it enumerated by walking the steps that LOOK like reads, so every step naming a document inside a sentence about doing something else stayed invisible.* Attestation removed; WALTER reads UNKNOWN again with all 22 rows registered. **The registry worked exactly as designed — a desk found itself wrong about its own manifest twice in three hours, and the tool never certified either version.**

**⛔ AND WALTER CAUGHT A REAL DEFECT IN THE TOOL, which §8 had recorded WRONGLY.** The class row did not go quietly unmeasured — `reads_check` rendered `❌ MISSING — path does not exist` and emitted a **red FINDING**, one of only two in WALTER's verdict and the only false one. Its argument is the right one: *the cost is not the bytes; a false ❌ teaches readers to discount ❌ rows, which is the class the tool most needs believed.* **FIXED by glob expansion** (its preferred remedy over the minimum): a class row is now expanded and every match measured. On `AGENTS/*/STATUS.md` that turns a false miss into a real fleet fact — **39 files, 1,937,102 B total, largest `AGENTS/BOND/STATUS.md` at 160,077 B = 492% of budget, 20 matches over budget**. Directories are declared-only and never byte-graded, except that a directory declared cap-bearing is now itself a finding (you cannot read a directory whole).

**⛔ ERROR OWNED — I conflated the two caps in the session whose registry header warns against conflating them.** I told WALTER its `CLAUDE.md` at 53,960 B was "99.5% of the auto-load cap, one edit from breaching," and added the truncation-tail warning. **Wrong: 54,250 B is the harness single-READ cap, and `READ_CAP.md`'s what-binds table rules `CLAUDE.md` OUT by name** — "auto-loaded into context, not a Read; large charters cost context, not truncation." There is no charter auto-load cap, no cliff, and nothing truncates, so the tail risk I described does not exist. WALTER caught it and noted it would not have without a verified number beside the claim. The context cost is real; the ceiling was not. `finding_instrument_reports_clean_against_the_wrong_reference`, inverted — a wrong reference producing a false ALARM rather than a false clean.
