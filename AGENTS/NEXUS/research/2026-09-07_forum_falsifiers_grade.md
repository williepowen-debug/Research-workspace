# FORUM FALSIFIERS — GRADE DAY ① (2026-09-07)

**Author:** NEXUS · 2026-09-07 ~12:1x–13:2x ET · PROME Tier-1 due-row spawn (WQ-184 L0; `PROME/DOCKET.tsv` L39, registered 2026-08-07)
**Sources graded:** `FORUM/2026-08-07_system-review/06_proposals/03_NEXUS_ask-before-need.md` §6 · `…/05_NEXUS_copy-kill.md` §falsifier
**Both branches numeric in each falsifier; neither renewable. Graded on the record. Every count below names its vintage and its command.**

⚠️ **Self-grade disclosure:** both falsifiers are mine, registered by me, graded by me. Both verdicts below go **against** the proposals. The measurements are reproducible from the commands given; the perimeter statements are the part a reviewer should attack.

---

## ① ABN (Ask-Before-Need) — **VERDICT: BRANCH 1 MET ⇒ REPLACE, NOT TUNE**

### The registered letter
> Re-run tonight's fires-now list on **2026-09-07**. **If ABN has read clean for 30 days while a BOND-class wait still occurred, the metric is missing a cost channel and should be replaced, not tuned.** Symmetrically: if ABN fires more than ~5 items in any single week, it has become a nag list and the second leg is not doing its job.

### What actually shipped, versus what was proposed
| Proposed (§1–§3) | Shipped | Gap |
|---|---|---|
| `consumed_by` on **4 surfaces** (GATES · WILL_QUEUE · packet headers · pre-reg cards) | **GATES.tsv only** — column 8, enforced by `PROME/tools/prome_gate.py::scan_gates_rows` | 3 of 4 surfaces unfielded |
| Fires on `slack ≤ 0` **OR** `slack < owner's median session cadence` | **Deadline clause only** (`consumer-date … passed`), plus an EMPTY-field defect check | **The cadence clause — §3's "whole point," the predictive half — was never built** |
| Printed at **every agent's boot** via the SessionStart hook | `scripts/session_banner.sh` contains **zero** ABN/slack/consumed_by references (VERIFIED by grep); the check runs only inside PROME's `prome_gate.py boot`/`closeout` | The C-36 lesson (*"the desk that could rule was not booted"*) is **not** implemented |

### The 30-day fire count — measured, not recalled
Method: replay `scan_gates_rows` against the last `PROME/GATES.tsv` commit of each day, with `today` set to that day (script `/tmp/abn_replay.py`, deterministic; re-derivable from `git log -- PROME/GATES.tsv`).

| Window | Days with a GATES commit | ABN fires | Items |
|---|---:|---:|---|
| 2026-08-08 → 2026-09-06 | 23 | **1 day** | `GATE-FALCON-001 consumer-date 2026-08-25 passed` (seen at the 8/27 commit; cleared by the next) |
| 2026-09-07 (live run, `prome_gate.py boot`) | — | **0** | *"all LIVE rows have live consumers or declared NONE"* |

**Rate ≈ 1 fire / 30 days ≈ 0.23 per week.**

### Branch 2 (nag list) — **REFUTED, numerically.** 0.23 fires/week against a ~5/week bar; the maximum in any single week of the window was **1**.

### Branch 1 (read clean while a BOND-class wait occurred) — **MET.**
A BOND-class wait = the ACTION owner has not consumed or ruled **and** a dated decision that consumes the answer falls inside the window. In the 30 days ABN read clean (1 fire, on a row that self-cleared), **at least four occurred, and none was on a GATES row:**

1. **HENRY's gamma-flip refresh.** `STATUS.md` BREACHED table: *"POSITIVE, spot above — `[STALE 8/6, 28 days]` · REFRESH OWED BY OWNER — M-04 rests on it."* Owner un-consumed; consumer = M-04's standing 20% mark, live continuously. ABN: silent (not a GATES row).
2. **OSPREY Channel-3 kill clock**, `[STALE 8/15]`, owner dark since 8/20, carried on the board as stale-marked rather than graded. ABN: silent.
3. **RED-FT-09 5y5y**, `[STALE 21 sessions]`, owner refresh overdue. ABN: silent.
4. **NEXUS itself.** This desk went dark 8/28→9/03 holding **7 unconsumed inbox items** and an **unpinned C#2 window start**; it took a **PROME Tier-1 dark-owner spawn** to drain it — and again today, 9/07. ABN: silent both times.

**And the diagnosis is sharper than the branch's wording.** ABN did not mis-calibrate; **it was pointed at the one surface where the waits do not happen.** Every measured wait sat on an *agent* surface — a threshold row, an inbox item, a prediction — none of which carries the field. Meanwhile the function ABN was designed for is now being performed by a **different instrument built 29 days later**: WQ-184's `PROME/tools/spawn_list.py`, which on this same 2026-09-07 boot fired **3 items** (`D:L189 BROCK` · `D:L208 WALTER` · `D:L39 NEXUS`, all DARK with due rows) against ABN's **0** — and it is the reason this session exists.

### Verdict and recommendation
> **REPLACE, per the registered branch.** The successor already exists and is already load-bearing: **`spawn_list.py` (WQ-184 L0) + the BD-02 desk-catalyst summons line.** It keys on the thing ABN's cadence clause was trying to approximate — *will the owner be at the desk before the date?* — but measures it directly (`ListAgents` liveness + last self-commit) instead of estimating it from a median.
>
> **KEEP** the `consumed_by` field on GATES.tsv. It is cheap, it is enforced, and its EMPTY-field check is a real (if quiet) defect guard. **Do not extend it to the other three surfaces** — that is the "tune" the falsifier forbids, and the 30-day record says it would buy ~0.23 fires/week on surfaces whose waits are already covered.
> **RETIRE** the unbuilt half explicitly rather than leaving it as a paper obligation: the cadence clause and the every-agent-boot hook line should be **struck from the proposal record as SUPERSEDED by WQ-184**, not carried as debt.
>
> ⚠️ **Honest limit on this grade:** ABN's clean 30 days is a statement about GATES.tsv, whose rows are also the best-tended in the fleet. The correct reading is *scope*, not *calibration* — I would not claim ABN would have been noisy elsewhere; I claim it was never asked.

---

## ② COPY-KILL — **VERDICT: NOT ZERO ⇒ THE DELETION WAS INSUFFICIENT (2 of 3 classes)**

### The registered letter
> On **2026-09-07**, grep the fleet for a new instance of each killed class. **Zero new instances in all three → the classes are extinguished.** **Any new instance → the deletion was insufficient and that class needs a *declared field*, not a check and not a paragraph.** A mistake the deleted prose would have prevented and the check did not catch → the prose was load-bearing, restore it.

**Perimeter, declared:** instruction-prose surfaces = root `CLAUDE.md`, `AGENTS.md`, `PROME/{CLAUDE,BOOT,CLOSEOUT}.md`, `AGENTS/*/CLAUDE.md`, skill definitions. Data-file headers = all tracked non-archive `*.tsv`. Path tokens resolved against `git ls-files` **and** disk; template forms (`YYYY-MM-DD`, `<date>`, `LEDGER_GLOB`) and paths cited *as negative examples* excluded by hand; agent-relative paths resolved against the agent's own dir before being called dead.

### KILL 1 — file paths in instruction prose: **1 NEW INSTANCE**
`AGENTS/WALTER/CLAUDE.md:64`, introduced **2026-09-03** (`b0e761882`), 27 days after the program registered:
> *"If its line-0 banner sha256 ≠ `sha256sum registry/FALSIFICATION_TRIGGERS.tsv`, it is STALE: read canon, flag RED."*

`registry/FALSIFICATION_TRIGGERS.tsv` is **cwd-relative**. WALTER launches from `AGENTS/WALTER/`, where the file does not exist; the canon is `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv`. **The dead path is inside the staleness guard itself** — the one line whose job is to tell WALTER its generated view has rotted. ⚠️ **This is a guard-wiring defect, not a typo:** run as written it errors instead of comparing, so the guard cannot fire correctly in either direction (`[[finding_guard_correctness_and_wiring_are_independent]]`).
*Adjacent, outside the instruction-prose perimeter and already detected:* `AGENTS/WALTER/design/BOARD_INDEX_GENERATION_DESIGN.md` → `BOARD/INDEX.generated.md`, flagged **today** by `scripts/firetime_check.py` as `DEAD POINTER`. **The promised replacement check exists and works — it just does not cover the class's cheapest form, a bare relative path.**

### KILL 2 — written counts of computable sets: **the deletion was NEVER EXECUTED, in its own named target**
`AGENTS/NEXUS/BRIEFS_MAP.md:41` still carried, as of this morning: *"★ 2026-07-31 disk-verified census: **25 briefs exist**"* plus a hardcoded 25-name roster. Disk, 2026-09-07, `ls AGENTS/*/NEXUS_BRIEF.md | wc -l` → **26** (SHADE, created 8/03). **Three later lines in the same file say 26** — the single census home contradicted itself in place for **35 days**.
This is not a new instance; it is the *original* instance, prescribed for deletion on 8/07 and never deleted. **Under the falsifier's own logic that is worse than a new one:** a new instance means the countermeasure was too weak; this means the countermeasure was never applied and the file's "SINGLE census home" claim was, for 35 days, an assertion of authority over a wrong number. **It is my file. Repaired in this session** — the number is gone, replaced by the command, with the failure recorded in place.
*Checked and CLEAN:* WALTER's `CLAUDE.md` §6b, which the same class would have caught — it carries **the instruction to count** beside dated snapshots, and all four snapshots verify correct against disk today (RED-FT 12 · REG-T 8 · CREED-T 11 · HANS-T 14). That is the class handled the right way.

### KILL 3 — policy restated in a data-file header: **1 NEW INSTANCE; the named instance was CURED**
✅ **Cured:** `AGENTS/NEXUS/brief_fallback_log.tsv`'s header now carries **only** the `cause` value definitions — format, which the rule expressly permits. The decision rules and the 40–50% thresholds are gone. *(One prescribed detail unexecuted: the header carries no `decision rules → CLAUDE.md §9a` pointer line. Cosmetic; not a violation.)*
🔴 **New instance:** `PROME/GATES.tsv` header, introduced **2026-09-03** (`b0e36d039`) — the same edit that correctly moved the rules out to `GATES_README.md` left a **numeric policy** behind:
> *"READ_CAP budget 32,550 B for a whole read (prome_gate meters); practical ceiling ~50,000 B per the README's CAPS rule (never 54,250)."*
Two caps whose authoritative homes are `READ_CAP.md` and `GATES_README.md`, restated in a TSV header — and the parenthetical `(never 54,250)` is a correction of a previously-wrong copy, i.e. **the drift signature the class is defined by**, already visible in the copy's first month.
*Checked and CLEAN (format side of the line, correctly):* `PROME/state/ORCH_LOG.tsv` names its single home (`ORCHESTRATION_PLAYBOOK §Two-tier`) and then restates **schema** — column list, fail-closed width, typed-cell semantics. Format may be restated. Not a violation.

### Third branch — **UNTESTABLE, and that is a finding**
The branch reads: *a mistake the deleted prose would have prevented and the check did not catch ⇒ restore the prose.* **No recognition paragraph was ever deleted.** Root `CLAUDE.md` still carries the `PROME/inbox/` warning verbatim; the per-agent existence-check bullets survive. The proposal's hard ordering constraint (*ship the check, prove it, then delete the prose*) was honoured on its first half and **never reached its second** — so the program's actual risk was never taken, and this branch cannot be graded. Recorded as **UNRESOLVED-BY-CONSTRUCTION**, non-renewable, exactly as the letter demands.

### Verdict and recommendation
> **NOT ZERO ⇒ per the registered branch, KILL 1 and KILL 3 need a DECLARED FIELD, not a check and not a paragraph.** Minimum viable, and it is small:
> - **KILL 1 — declared field:** every path token in instruction prose is written **repo-root-relative**, or carries an explicit `[cwd: <dir>]` marker. That makes it machine-checkable from one rule, which a bare relative path is not, and it is the same defect class as root canon's *"run all git operations from the repo root"*. Then widen `firetime_check.py`'s DEAD-POINTER leg over `AGENTS/*/CLAUDE.md` — **it already catches this class one directory away.**
> - **KILL 3 — declared field:** a header block is tagged `# FORMAT:` or `# POINTER:`. Anything else in a data-file header is a lint failure. Numbers sourced from another file's rule are `# POINTER:` by definition.
> - **KILL 2 — no new field needed.** The rule was right and simply unexecuted; the fix is a one-line sweep for standing counts in index surfaces, and I have done mine.
>
> ⚠️ **The program's own lesson, turned on itself:** copy-kill was chosen to ship first *because* it was cheap, bounded and reversible — a test of whether the fleet could execute a deletion at all. **It could not.** One class was cured, one was never executed in its author's own file, and two new instances appeared inside 31 days, both introduced by careful sessions that were *reducing* duplication elsewhere in the same commit. That is the transferable finding: **`[[finding_a_correction_pass_is_unreviewed_work]]` applies to de-duplication passes too — the pass that moves rules to their proper home is exactly where a leftover copy gets minted.**

---

## What this grade does NOT do
- It does not re-mark any convergence, threshold or the probability split. No market datum was consumed.
- It does not rule the **S1 disposition** — that is Will's word (rider on DOCKET L39). Facts + recommendation in the delivery memo `PROME/inbox/2026-09-07_from-NEXUS_forum-falsifiers-grade-day-1.md`.
- It does not edit another desk's files. The two live defects found in WALTER's surfaces are packeted to WALTER, not fixed by me.
