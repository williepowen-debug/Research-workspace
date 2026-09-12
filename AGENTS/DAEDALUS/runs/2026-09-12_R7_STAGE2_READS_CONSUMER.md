# R7-stage-2 — READS.tsv CONSUMER HALF (DOCKET L209)

**DAEDALUS · 2026-09-12 (Sat) · TOOLING/WIRING sitting**
**Artifact changed:** `scripts/read_cap_check.py` (DAEDALUS `scripts/` grant, Will-ruled 2026-07-31)
**Declaration half (PROME's, NOT edited by me):** `PROME/registry/READS.tsv`, born 2026-08-31, 85 data rows.

---

## 0. ACCEPTANCE CONDITIONS — written BEFORE the edit (WQ-229)

Stated in the defect's own terms, not as a restatement of the symptom. The symptom was *"read_cap_check
finds 1 of PROME's ~7 boot reads."* That is too narrow a condition: passing it only requires finding 7 files.

**C1 — A declared desk is graded on its DECLARATION, not on a scan of its charter.** A desk with a VALID
`ATTESTATION` row gets its perimeter from READS.tsv; the verdict line says `DECLARED`.
**C2 — The two defect axes stay separate.** Cap-bearing modes (`whole`, `programmatic`) are MEASURED.
Not-cap-bearing modes (`scoped`, `grep`, `summary`) are LISTED and never counted. Collapsing them
re-creates the false-breach the `mode` column exists to prevent.
**C3 — An unattested desk is UNKNOWN, never clean** (READS.tsv's own ⛔). Rows without an attestation are
a PARTIAL perimeter; the verdict must not print a clean bill over one.
**C4 — An undeclared desk keeps today's behaviour exactly.** ~14 desks invoke this tool in a closeout step;
a strict flip breaks all of them at once. The heuristic stays, and says it is a heuristic.
**C5 — `declared_by != reader` voids the attestation.** The file's enforceability rule. A PROME-signed
attestation for another desk is INFERENCE, and must not clear that desk.
**C6 — A declared path that is ABSENT from disk is reported.** This is the condition the heuristic
structurally cannot produce: a scan can only find what exists, so a manifest pointing at a deleted file
reads as silence. `finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit`.
**C7 — `RETIRED-<date>` rows are skipped, not measured.**
**C8 — A cross-agent read lands in the READER's perimeter** (Will's ruling 1) and is measured normally.
**C9 — A CLASS row (glob) is neither silently dropped nor counted as one file.**
**C10 — An unparseable / half-written READS.tsv returns rc 2, never rc 0.** PROME may be editing it.
**C11 — rc contract unchanged: 0 clean · 1 FINDINGS · 2 CANNOT-EVALUATE.** The strict flip is opt-in
(`--require-manifest`), because changing the fleet default is PROME's/Will's call, not mine.

## 0b. NEIGHBOUR CATEGORIES — considered, per WQ-229 (consider, not perform)

| Category | Disposition |
|---|---|
| **ordinary** | PROME (declared+attested) and DAEDALUS (undeclared → heuristic). Both drilled. |
| **overlap** | A path both declared AND findable by the heuristic — must not double-count, and the declared mode must win. Drilled. |
| **wrong owner** | `declared_by != reader` attestation must be REJECTED (C5). Drilled — it is READS.tsv's own selftest negative control. |
| **missing information** | Declared path absent from disk (C6); rows present but no attestation (C3). Both drilled. |
| **concurrent activity** | READS.tsv lives in `PROME/`; PROME edits it. Malformed/truncated file ⇒ rc 2 (C10). Drilled. |

## 1. WHY THE CONSUMER HALF WAS THE RIGHT HALF TO BUILD — measured, not assumed

`python3 scripts/read_cap_check.py --agent PROME` returns **rc=0 ✅ having found exactly ONE
boot-mandated read** (`STATUS.md`, 10,478 B). PROME's actual declared boot perimeter in READS.tsv is
**29 rows**. The tool's own perimeter line names the cause: it scans `CLAUDE.md` boot sections, and
PROME's reads are mandated by `PROME/BOOT.md`, which it never opens.
**VERIFIED 2026-09-12 13:5x ET.** This is `finding_instrument_reports_clean_against_the_wrong_reference`:
a clean scan against the wrong perimeter.

## 2. THE AMBIGUITY PROME RAISED IS ALREADY SETTLED — at PROME's own artifact

PROME's spawn brief described a *"live ambiguity READS.tsv should settle"*: whether `PROME/GATES.tsv`
(46,653 B = **143% of the 32,550 B budget**, named a boot read by `BOOT.md` step 3) is a read-whole
surface or is instrument-covered — *"Both readings are currently live and nothing records which is
intended."*

**That is REFUTED at the artifact.** `PROME/registry/READS.tsv` already carries the row:

> `READ · PROME · PROME/GATES.tsv · mode=summary · PROME:BOOT.md-3`
> *"⚠️ PROTOCOL/PRACTICE MISMATCH, DECLARED NOT PAPERED OVER — and note WHICH debt this is. On CAP
> grounds nothing is owed: a ledger consumed by a script is the cold/on-demand class… The debt is
> PROTOCOL-TEXT ACCURACY: BOOT.md step 3 says 'Read', and what executes is bounded… PROME owes step 3
> a rewrite naming the real operation. A step whose verb does not describe the operation is a defect
> on its own axis, cap or no cap."*

And the file's header names this exact row as the live instance of its axis-(b) defect class.

**So: the intent IS recorded, the distinction IS already a column (`mode`), and the owed fix is already
named — a BOOT.md step-3 rewrite, which is PROME's file, not mine.** PROME re-derived the judgement
this morning by grepping GATES instead of reading its own registry.
`finding_ask_which_surface_the_reader_travels_not_where_the_fact_belongs` — the answer was filed where
the reader does not travel. **PAT-124 shape:** a reviewer's proposal list measures where the law is
hard to find; PROME proposed a column that already exists.
⚠️ **Not a criticism that costs nothing to state: the registry is not on PROME's boot path, so nothing
would have shown it.** The remedy is a pointer from BOOT.md step 3 to the READS row, not more prose.

**One real defect inside that row, mine to report and PROME's to fix:** the note says GATES sits *"at
161% of budget."* Measured today: **46,653 B = 143.3%**. A live measurement written into prose, stale
within days — the precise thing `PROME/CLAUDE.md` § Session Process Controls forbids, and the reason
READS.tsv itself carries ⛔ NO BYTE COLUMN. The row's own rule is violated by the row's own note.

## 3. THE FINDING THAT MATTERS MOST FOR L209 — the rollout, not the code

`READS.tsv` declares **2 readers**: **WALTER (56 rows) and PROME (29)**. **2 ATTESTATION rows.**
The fleet is ~40 desks. **VERIFIED** by census of the file.

So the consumer half does not "replace the heuristic" fleet-wide today. It replaces it for **2 desks**
and, for the other ~38, converts a *falsely clean* line into an *honestly heuristic* one. That is a real
improvement in the direction that matters — but **the 30-desk rollout is the gating work, and it is a
DECLARATION task each desk must do itself** (no desk may commit inside `PROME/`, and PROME may not
attest for anyone: `PROME(from-charter)` can never attest, by the file's own rule).

⛔ **PROME is ONE desk and I did not generalise from it.** Whether other desks' boot chains are equally
invisible to the checker is a MEASUREMENT — §5 below.

## 4. WHAT WAS BUILT — `scripts/read_cap_check.py`, R7-stage-2 consumer

**Precedence:** a desk's own **ATTESTED** declaration beats a scan of its charter. Three states, and they are
deliberately three, not two:

| Desk state | Perimeter | Verdict |
|---|---|---|
| **DECLARED + ATTESTED** (PROME, WALTER) | READS.tsv rows for that reader | graded normally; the clean line says *"Perimeter = the desk's own declaration, not a scan"* |
| **DECLARED, NOT attested** | — | **rc 2 CANNOT-EVALUATE.** Fails CLOSED, never back to the heuristic — falling back would print a clean line over a partial perimeter, which is the exact defect READS.tsv exists to retire |
| **UNDECLARED** (35 desks) | charter heuristic, unchanged | rc as before, and the clean line now carries *"⚠️ PERIMETER IS THE CHARTER HEURISTIC … NOT a clean bill. 29 of 37 desks delegate boot to a file it cannot see."* |

**Mode handling** (C2 — the two axes stay separate): `whole`/`programmatic` MEASURED · `scoped`/`grep`/`summary`
printed as `◦ … declared, not cap-bearing, not counted` · `RETIRED-*` skipped · CLASS rows (globs) shown, never
counted as one file · `BASIS`/`ATTESTATION` rows are not reads.
**New states the heuristic structurally could not produce:** a declared path **absent from disk**; a mode outside
the manifest's own vocabulary; an attestation signed by someone other than the reader. Each is rc 1 or rc 2, named.
**`--require-manifest`** (opt-in) makes an undeclared desk rc 2. **NOT the default** — ~14 desks invoke this tool in
a closeout step, and flipping the fleet default is PROME's/Will's call, not mine. Proposed in §6.

## 4b. `--selftest` ADDED — and it retires its own gap row

**24/24 legs, capable AND clean case per leg, fixtures frozen in tempdirs** (never pinned to a live surface —
PROME's 9/9 finding). Legs map 1:1 to C1–C11 plus a five-case end-to-end rc drill.
⭐ **This closes `scripts/validate_all_gaps.tsv` row A9 by the register's own terms** — *"Retire this row when
read_cap_check gains `--selftest`… the fix-shipper retires it."* Leg **A9 is now REGISTERED** in `validate_all.py`
and the gap file has **zero data rows**. Production: **12 PASS · 0 DECLARED-GAP** (was 11 PASS · 1 DECLARED-GAP).
That is one fewer standing "not checked" line a green run has to carry.

## 5. WHAT THE NEW PERIMETER FOUND — three live findings, none of them mine to fix

**① PROME: 1 → 7 cap-bearing reads measured, + 16 declared-not-counted.** Two are in **rotate-tier**, and
*neither was visible to any instrument before today*:
| surface | bytes | % of 32,550 B budget |
|---|---|---|
| `HEARTBEAT.md` | **27,999 B** | **86.0%** — past the 75% rotation trigger |
| `PROME/ACTIVE_DECISIONS.md` | **24,639 B** | **75.7%** — past the trigger |
PROME's remaining five (`SCRATCH` 20,386 · `BOOT.md` 19,036 · `HANDOFF` 12,145 · `STATUS` 10,478 · `USER.md` 4,126)
are clear. **rc 0 — nothing is over budget.** Rotation, not a breach. PROME's call, PROME's files.

**② WALTER: rc 1 — a CROSS-AGENT read over budget, invisible at BOTH ends by construction.**
`AGENTS/RED/registry/FALSIFICATION_TRIGGERS_SCAN.tsv` = **32,918 B = 101.1% of budget**, declared `whole` by
WALTER at boot step 6b. **RED owns the file; WALTER pays the context.** Neither desk's own heuristic perimeter
could see it — RED's because RED does not read it at boot, WALTER's because the heuristic never opened WALTER's
`design/BOOT_PROTOCOL.md`. This is the exact class PROME named in its 8/31 addendum, and it is the **first time an
instrument has actually caught one.** ⚠️ **Live and growing:** the file is dirty in the working tree right now and
RED is in session. Packets to both.

**③ The fleet: 29 of 37 desks delegate boot to a file the checker cannot open** (`BOOT.md` ·
`scripts/boot.py` · `MAINTENANCE.md` · `design/BOOT_PROTOCOL.md`). **PROME is the majority case, not an outlier** —
which is what I was told not to assume, and it measured the other way. Only **4 of 37** desks are down to
STATUS-only, so the heuristic is not empty; it is *systematically narrow*, and narrow in the silent direction.

## 5b. PHAN's finding — resolved, and the count was wrong by one

`read_cap_check.py --agent PHAN` returned `READ-CAP 2 CANNOT-EVALUATE: no charter at AGENTS/PHAN/CLAUDE.md`.
**Cause:** the resolver knew one path template; sub-agents live at `AGENTS/<PARENT>/sub_agents/<NAME>/`.
**Fixed** — second location added, all resolve, no regression to `--fleet` or `--selftest`.
⚠️ **PHAN enumerated SEVEN (CARL's DOC · GIG · META · PHAN · POLLY · POP · STUE). The sweep for the PATTERN finds
EIGHT: `AGENTS/MARCO/sub_agents/TOURISM`.** PAT-136 — an enumeration is exhaustive only of its author's search,
and PHAN was reporting from CARL's tree. **Cost while the hole was open:** PHAN's `DOSSIER.md`, a boot whole-read,
reached **41,078 B = 126% of budget**, and no fleet instrument could have flagged it.
**RULED and written into `BLUEPRINTS/READ_CAP.md`'s "what binds" table, which is what PHAN actually asked for:**
the budget **binds** a sub-agent (its charter mandates boot reads like any other), `--agent <NAME>` now grades it,
and **`--fleet` stays unchanged** — a sub-agent has no ROSTER seat and no FLEET_MAP row, so it is covered
**on demand, never in the fleet denominator**, and the parent desk owns running it. Until today that exclusion was
an artifact of a path template rather than a decision; a reader of the blueprint would have assumed coverage.

## 6. WHAT I AM *NOT* DOING, AND WHAT I ASK

⛔ **I did not edit `PROME/registry/READS.tsv`, `PROME/BOOT.md` or root `CLAUDE.md`.** All three are PROME's.
**ASK 1 — the dated strict flip.** `--require-manifest` exists and is opt-in. The honest end state is that it
becomes the default, because a heuristic perimeter that prints a clean line is a control that only advises. But
that flip turns ~35 desks rc 2 at their next closeout, so it needs a **rollout, not a switch**: each desk declares
and attests (a packet to `PROME/inbox/` — no desk may commit inside `PROME/`), and the flip lands when coverage
justifies it. **The rollout is the gating work; the code is done.** I propose the 9/18 or 9/25 slot; Will's call.
**ASK 2 — `BOOT.md` step 3.** The GATES row's own note says PROME owes step 3 a rewrite naming the real operation
(`summary`, not "Read"). Still owed, still PROME's.
**ASK 3 — a pointer from `BOOT.md` to the READS row.** The registry is not on PROME's boot path, which is why the
GATES question got re-derived this morning. One pointer is the whole fix.
**ASK 4 — the "161% of budget" figure in the GATES row's note is stale (143.3% today).** A live measurement in
prose, in a file whose header forbids a byte column for that exact reason.
**ASK 5 — HEARTBEAT.md (86%) and ACTIVE_DECISIONS.md (75.7%) are past the rotation trigger.** Newly visible.
