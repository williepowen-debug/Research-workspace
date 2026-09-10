# `validate_all.py` v1 — BUILD RECORD

**Author:** DAEDALUS · **Date:** 2026-09-10 (~10:3x–11:1x ET) · **Commission:** DOCKET **L284** (due today), per my own load-split plan `runs/2026-09-05_9-14_LOAD_SPLIT.md` **correction 1** — it must land BEFORE the 9/12 TOOLING/WIRING sitting (its suite legs ARE several of that sitting's mechanical legs) and it is the declared precondition of **WQ-171 ③** (DOCKET L263, 9/18).
**Artifacts:** `scripts/validate_all.py` · `scripts/validate_all_gaps.tsv` (known-gap register) · `scripts/validate_all_baseline.json` (swept baselines)

---

## ⚠️ SCOPE — carried forward from the 9/5 pre-build ruling, unchanged

`design/2026-09-05_VALIDATE_ALL_IS_NOT_THE_YEYOU_REPLACEMENT.md`: back-tested against YEYOU's 13 real findings — **1 caught cleanly · ~4 partial · 6–7 missed**, the largest missed category (4/13) being mail-loop. Structural, not fixable by adding legs: this tool is **state**-based where YEYOU was **watermark/diff**-based, checks **file properties** where YEYOU judged **contradictions against a desk's own stated rules**, and its perimeter is `CHECKS.tsv` — i.e. bounded by checks that already exist, which is exactly what a reviewer is for.

**The tool now says this itself, in its own output, on every run** — the `NOT CHECKED` block and the `A PASS here proves:` paragraph print on clean runs and failing runs alike (CHECK_STANDARD §2, amended form). The ruling is no longer carried only by a document a future reader may not open.

---

## What it is

A **suite runner**: it runs each registered shared check in its own self-verifying mode, **types the three PROME decision ledgers**, and returns ONE aggregate verdict under the §9 rc contract. 14 legs in four groups.

| Leg | Escalation | What it does |
|---|---|---|
| **A1–A8** | structural | `--selftest` on `corrections_boot_check` · `docket_view` · `orch_log` · `claim_check` · `memory_index_check` · `consumer_check` · `ledger_staleness` · `memory_citation_census` |
| **B1** | structural | `PROME/DOCKET.tsv` — 6 cols/row, col-1 against a **declared trigger grammar**, state cell non-empty |
| **B2** | structural | `PROME/GATES.tsv` — 12 cols/row, `gate_id` present, leading date on `registered`/`review_by`, `state` non-empty |
| **B3** | structural | `PROME/WILL_QUEUE.md` — 7 cells/row, integer ids, **ids unique** |
| **C1** | delta-keyed | commit subjects ≤100 chars (root 4d / WQ-171 ①) |
| **C2** | delta-keyed | fleet KB `Stale_By` expiry vs non-terminal `Status` |
| **D1** | delta-keyed | `read_cap_check --fleet` desks over budget / over cap |

`--selftest` · `--list` · `--only <ids|groups>` · `--json` · `--rebaseline` · `--strict-dates` · `--timeout` · `--commit-scan` · `--root`.

**Escalation vs verdict (the distinction that cost this build its one defect — see below).** `structural` = any defect is FINDINGS. `delta-keyed` = the **LEVEL** is ADVISORY and only a rise above the **recorded baseline** escalates. The **verdict reads the resulting STATE**, never a per-leg boolean.

**rc contract (§9):** `0` no leg in FINDINGS or CANNOT-CERTIFY · `1` ≥1 FINDINGS · `2` CANNOT-CERTIFY (a leg could not run, a tool is missing, input unparseable, usage error, or an EXPIRED gap row). **2 dominates 1.**

---

## §3 VERIFICATION — NO GUARD SHIPS UNVERIFIED

### (a)/(b) — 24 fixture drills, capable AND clean case watched per leg. **`--selftest` → 24/24, rc 0.**

Every drill builds a **frozen fixture tree in a tempdir** — never a mutated live surface (§3 monkeypatched-legs form), and never a regression assertion pinned to a live file (`finding_regression_test_pinned_to_a_live_surface_rots_on_the_next_edit`; PROME hit that exact class on 9/9 when Am.#3 landed and two live-pinned tests failed by construction).

Drills, by what they falsify:
- **B1/B2/B3** capable (bad date, short row, duplicate WQ id) → FINDINGS rc1; clean → PASS rc0.
- **B1 empty ledger** → CANNOT-CERTIFY rc2. *A ledger that parses to zero rows is never reported clean.*
- **B2 absent file** → CANNOT-CERTIFY rc2.
- **Gap register:** EXPIRED row → rc2 (re-flags itself) · MALFORMED → CANNOT-CERTIFY rc2 and suppresses nothing · UNEXPIRED row → converts a FINDINGS leg to DECLARED-GAP, rc0.
- **C2** delta above baseline → FINDINGS rc1 · at baseline → ADVISORY rc0 · **positive control failure (0 parseable `Stale_By` cells) → CANNOT-CERTIFY rc2** (§14: an absence is never a finding).
- **A-leg sub-check:** tool ABSENT → CANNOT rc2 (never silently skipped) · rc=1 → FINDINGS rc1 (**the aggregate cannot hide a failing member**) · rc=3 → CANNOT rc2 · rc=0 → PASS rc0.
- **C1** no git history → CANNOT rc2.
- **D1** unparseable summary line → CANNOT rc2 (**fails closed**, `finding_lenient_parser_reports_unparseable_as_a_behavior`) · 9/37 over baseline 6 → FINDINGS rc1 · 6/37 at baseline → ADVISORY rc0.
- **rc precedence:** FINDINGS + CANNOT together → rc **2**.
- **§2 output contract:** a CLEAN run still prints the perimeter, the NOT-CHECKED list and the what-a-PASS-does-NOT-prove paragraph.

### (e) PRODUCTION ACCEPTANCE SET — real inputs, named by path, re-run at every version
- **Real CLEAN input:** `PROME/GATES.tsv` → B2 PASS.
- **Real DEFECTIVE input:** `PROME/DOCKET.tsv` with col 1 typed as a bare date → **68 flags**, reproducible with `python3 scripts/validate_all.py --only B1 --strict-dates`. Retained as a runnable demonstration of why the grammar exists.

### ⭐ The rule paid for itself on the FIRST run — one real defect, caught by its own selftest

Drill *"D1 9/37 over baseline 6 → FINDINGS, rc1"* returned **FINDINGS but rc 0**. Cause: `verdict()` flipped only on `state == FINDINGS **and** leg.flips`, and D1 is a delta-keyed leg with `flips=False`. **The leg computed the finding correctly and the verdict could not read it** — `[[finding_guard_correctness_and_wiring_are_independent]]`: correctness and wiring are separate questions, and one boolean cannot say both "advisory at its level" and "flipping at its delta". Fixed by keying the verdict on **STATE**, with the reasoning written as a comment at the site. The whole delta-keyed design (3 of 14 legs) was inert before this run.

`py_compile` and `rc=0` would both have passed. Only the watched capable case failed.

---

## §12 BASE-RATE — the check was scoped to the MEASURED population, not an assumed one

**First production run flagged 8 DOCKET + 27 GATES "defects". Every one was a legitimate ledger form.** Typing was cut to the measured grammar:

**DOCKET col 1 (310 rows):** 241 `YYYY-MM-DD` · 60 `YYYY-MM-DD..YYYY-MM-DD` window · **7 `next-<desk-or-pass>` event-keyed** · 1 `~YYYY-MM-DD` approximate · 1 repeated header token.
**GATES `registered`/`review_by` (20 rows):** **every dated cell carries trailing annotation**; 3 `review_by` cells are terminal em-dashes. The leg types the LEADING token and **reports** the annotation count — it does not flag it, because flagging would require making a right row less right (CHECK_STANDARD §1, last bullet).

Each run prints the grammar it accepted, so the reader sees what was typed rather than a bare ✅.

**Recorded baselines** (`scripts/validate_all_baseline.json`, swept 2026-09-10 at HEAD `6f342d55b`): `C2_kb_stale_by: 534` · `D1_read_cap_over_budget: 6`. C1: 13/200 over 100 chars (report-only — history is fixed; root 4b forbids amend, so flagging it would pin permanent red and kill the signal for the subject that CAN still be fixed: the next one. Declared as a comment at the site, §6).

---

## §1 KNOWN-GAP REGISTER — `scripts/validate_all_gaps.tsv`

Per-instance, expiry-dated, never a pattern. **EXPIRED rows re-flag themselves to rc 2**, so a quiet run means genuinely quiet. A malformed register suppresses NOTHING and says so (both paths drilled).

One row today: **`read_cap_check.py` has no `--selftest`**, so leg A9 is **NOT REGISTERED** rather than registered-and-silently-skipped. Expiry **2026-10-10**; the fix-shipper retires the row. Evidence recorded in the register: `--help` returns `READ-CAP 2 USAGE`, and `grep -c -- '--selftest'` = 0.

## §10 SELF-SCOPE — DAEDALUS's own directory is IN SCOPE
Legs A2/A6/A7/A8 and D1 exercise or read DAEDALUS-authored surfaces, and DAEDALUS's desk sits in D1's fleet population like every other. Stated in the docstring.

## §13 PRIOR-ART LINE
Symptom *"suite runner reports green while a leg never ran" / "aggregate check hides a failing member"* searched against `memory/auto/MEMORY.md`, `INDEX_COLD*.md`, `PATTERNS_HOT.md`. **NOT novel** — five hits, and the build is shaped around them: `finding_guard_correctness_and_wiring_are_independent` · `finding_a_check_that_only_advises_is_overridden_the_control_is_downstream` · `finding_instrument_reports_clean_against_the_wrong_reference` · `finding_lenient_parser_reports_unparseable_as_a_behavior` · PAT-074 / PAT-110 / PAT-146.

## §11 READER
DAEDALUS at any tooling sitting; **PROME at closeout when a decision ledger was touched.** Registered in `CHECKS.tsv` at build. *(Wiring it into a boot/closeout step is a PROME/Will call, not mine to take — see the ASK in the delivery memo.)*

---

## Production run, 2026-09-10 — **rc 0, `11 PASS · 0 FINDINGS · 3 ADVISORY · 0 DECLARED-GAP · 0 CANNOT-CERTIFY`**

Three advisory levels, all at or below baseline, all reported and none flipping:

1. **C2 — 534 fleet KB rows are past `Stale_By` with a non-terminal `Status`**, over 1,231 dated cells across 31 KBs; **20 KBs carry no `Stale_By` column at all.** This is the largest number this build surfaced and it was not previously measured fleet-wide. Recorded as the baseline; a RISE escalates. **It is an owner-by-owner judgement, not something this tool can rule on — flagged to PROME in the delivery memo, no packets sent.**
2. **D1 — 6/37 desks over the read-cap BUDGET, 1/37 over the hard CAP.** Consistent with my own standing debt row (9/37 over budget at the 9/4 wiring-sweep detection pass; the perimeter differs, so the two are not directly comparable and I am not treating the fall as progress).
3. **C1 — 13/200 recent commit subjects over 100 chars.** Report-only.

**What a PASS here does NOT prove** (printed on every run, so a green line cannot be over-read): that any finding was acted on · that mail was read · that a desk contradicts its own stated rules · anything about external truth. **It does not refill the retired per-push review seat.**

---

## Two findings for PROME (ledger owner) — reported, not acted on

- **7 DOCKET rows are event-keyed (`next-<DESK>-session`, `next-KERNEL-spec-pass`), not dated**, against a ledger whose own header says *"dated catalysts only"*. B1 now ACCEPTS them as a declared grammar because they are clearly deliberate — but they are invisible to every date-keyed reader, including `docket_view --check` and the WQ-184 `spawn_list.py` due-row driver that spawned this session. **An event-keyed row can never come due.** Worth one ruling: register the form (and a companion `Trigger` cell a reader can key on) or convert them.
- **Every dated cell in `GATES.tsv` carries trailing prose after the date** (24 cells) — a typed column doing double duty as a note field. Harmless to a leading-token parser; brittle for anything that reads the column as a date.

## Owed / next version
`ledger completeness vs the trading calendar` (needs a calendar source) · `wiring_census` / `asmade_audit` forward legs (agent-judged output — a runner cannot adjudicate them) · leg **A9** when `read_cap_check` gains `--selftest` (gap row expires 10/10) · a `--since` mode so C1 scans a session's own commits rather than a fixed window.
