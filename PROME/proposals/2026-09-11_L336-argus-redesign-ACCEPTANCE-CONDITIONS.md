# L336 — ACCEPTANCE CONDITIONS, written BEFORE any edit

**Will's authorization 2026-09-11 19:07 ET:** *"Proceed with one bounded session to redesign ARGUS's scope and
complete the three remaining repairs. Define acceptance conditions first, test the complete workflow, and obtain
independent review of the final candidate. Keep any condition violation open. Then run the existing trial and
report effectiveness and cost."*

**Nothing below is implemented at the time of writing.** This file is the contract and the test list. A
condition that ends the session unmet stays OPEN and is reported as OPEN — relabelling is what reopened F1.

---

## PART A — ARGUS scope redesign

**The diagnosis being fixed (external reviewer, and it is the root cause of all five prior defects):**
authorship and audit boundaries were RECONSTRUCTED from commit subjects and file names instead of RECORDED.
Four regex repairs did not change that.

**A1 — RECORDED BASELINE, not a matched one.** The audit baseline is read from an explicit record written at
the previous closeout. No regex decides what a closeout is. If the record is absent, the tool says so and
fails loudly to a named fallback; it never silently picks a wrong baseline.
*Falsifier:* a commit whose subject is ABOUT closeout cannot become the baseline, because subjects are not read.

**A2 — RECORDED PERIMETER, not scattered patterns.** One declared manifest lists every path rule with its class
(`OWNED` / `SHARED` / `EXCLUDED`) and a reason. The code contains no path regexes; it reads the manifest.
*Falsifier:* adding a surface requires a manifest row, not a code edit.

**A3 — ATTRIBUTION BY RECORDED OWNERSHIP, never by commit subject.** The candidate change set is every change
to an `OWNED` path since the baseline, whoever committed it. A commit subject never confers or denies scope.
*Falsifier:* a recipient consuming a PROME packet (`git mv` into `processed/`) is out of scope because
`processed/` is declared `EXCLUDED`, not because of who wrote the subject.

**A4 — NO SILENT DROP. EVER.** Any uncommitted path that is neither clearly `OWNED` nor clearly `EXCLUDED`
is reported `UNATTRIBUTED`. The two failure directions are not symmetric: claiming another desk's work is
visible and correctable, dropping PROME's own work is invisible. *(F-4 blocker: the ratified `MSG-*.md` route
can never contain `from-PROME`, so a filename key dropped it silently.)*
*Falsifier:* a PROME artifact in another desk's inbox under ANY filename appears somewhere in the output.

**A5 — NO SHARED SURFACE IS CLAIMED BY FILENAME PATTERN.** `memory/auto/`, `memory/YYYY-MM-DD.md` and every
future shared surface are `SHARED`: lineage-inferred at most, labelled as inference, never asserted as owned.
*(F-5 blocker.)* *Falsifier:* another desk's pending edit to the shared daily note does not enter PROME's scope.

**A6 — OVERLAP PRESERVED.** A path both committed and pending carries both states and both prescribed reads;
the size threshold counts unique paths.

**A7 — THE AGENT'S OWN INSTRUCTIONS MATCH THE TOOL, IN BOTH COPIES.** Every state the tool can emit has a read
instruction in `.claude/agents/argus.md`, and the root and `PROME/.claude/` copies are byte-identical.

**A8 — PROPERTY TESTS, NOT STRING TESTS.** Each condition is tested as a property over generated inputs, not by
pinning the reviewer's literal strings. The existing five string tests stay as regression anchors, but they do
not discharge A1–A7. *(Owed gap named in the prior residue.)*

---

## PART B — the three remaining repairs (original audit F2 · F3 · F4; DOCKET L335)

**B1 (audit F2) — a correction to a decision record produces an event.** The ledger compares the full semantic
payload minus generated write metadata. A corrected `record`, `title`, `rec`, `type`, `since` or `source`
yields an `UPDATED` event, and the rendered Deck shows the corrected text.
*Falsifier:* correct a terminal row's record; the Deck must not render the obsolete version while `check` passes.

**B2 (audit F3) — two legitimate same-day updates do not break the ledger.** Events carry a unique identity, so
two deadline changes on one day both append and `check` passes. Idempotence remains semantic: re-syncing an
unchanged queue still appends nothing. The closeout recovery text stops equating rc=1 with a broken seal.
*Falsifier:* move a deadline twice in one day; both events exist and `check` returns 0.

**B3 (audit F4) — every tap is preserved and the effective ruling is determined explicitly.**
🔴 **EVIDENCE FIRST, BEFORE ANY CODE CHANGE:** inspect the hosted tap history and report whether any real tap
was lost. Until that is done the claim is SEARCH-NOT-FOUND, not "no data lost". Then: unique id per tap, full
timestamp retained as data, pickup determines the latest ruling explicitly; disabling a control is never the
uniqueness guarantee.
*Falsifier:* two conflicting taps 0.8 s apart on one WQ leave TWO documents, and pickup names which one rules.

---

## PART C — process conditions (Will's instruction, verbatim legs)

**C1 — the COMPLETE WORKFLOW is tested,** not the units: a closeout-shaped end-to-end run — write, commit some,
leave some pending, compute scope, and confirm what an auditor would actually receive.
**C2 — INDEPENDENT REVIEW of the FINAL candidate**, against A1–A8 and B1–B3, with its own counterexample. ONE
bounded pass: verify the changes and their interaction, carry forward evidence for unchanged behaviour, do not
restart an open cycle.
**C3 — ANY CONDITION LEFT UNMET STAYS OPEN** and is reported as OPEN, with what is outside coverage named.
**C4 — THEN run the existing ARGUS trial and report EFFECTIVENESS AND COST** — defects caught before commit vs
after, against the 9/11 baseline, and the token/wall-clock cost of the run.

## Neighbour categories (WQ-229; CONSIDER all five, justified N/A allowed)

| Category | Applies? |
|---|---|
| Ordinary | YES — all conditions |
| **Overlap** | YES — A6; and B2 (two events, one day) |
| Wrong owner | YES — A3, A5 |
| Missing information | YES — A1 (no baseline record), A4 (no attribution) |
| Concurrent activity | YES — B3 (two taps); **N/A for A1–A7**: the tool takes two non-atomic git snapshots and a second session could mutate between them — declared OUT OF SCOPE for this session and reported as such, not silently ignored |

---

## INDEPENDENT REVIEW RESULT (C2) — one bounded pass, 2026-09-11 ~19:1x ET

Reviewed `ee79e1ef6` against these conditions. **31 tests passed and three of the reviewer's own counterexamples
still broke behaviour the suites assert.** That is the whole argument for C2 in one line.

**Graded: A1 A2 A3 A5 A6 A7 B1 C1 VERIFIED · A4 A8 B2 NOT MET · B3 verified in code, CANNOT TELL on the hosted leg.**

### The three ❌ — all FIXED in this session, each with the reviewer's own counterexample as a test

| ❌ | What it was | Fix |
|---|---|---|
| **A4** | A PROME artifact in a **routing-lane subdirectory** appeared NOWHERE — not SHARED, not UNATTRIBUTED, only inside an anonymous `excluded` integer. A drop by path rule, which is what the redesign claims to have made impossible. | Lanes stay `EXCLUDED` (39 live paths of WALTER routing traffic; reclassifying them wholesale would have doubled the audit surface with mail PROME did not write). A row placed BEFORE the lane exclusion makes `*from-PROME*` in a lane `SHARED`. **Include-on-hint can only over-include; it was EXCLUDE-on-filename that dropped the MSG-* route.** |
| **B2** | The reviewer drove the REAL sync path — `needed_by` 10-01 → 10-08 → 10-01 on one day — and **the tool's check rejected history the tool had just written.** Audit-F3's exact failure mode surviving at n=3. And **B1 made it MORE likely**: `COMPARED` went from 3 fields to 10, every one able to oscillate. | The payload key was too coarse. A duplicate is a **NO-OP WRITE — the same payload twice IN A ROW for one WQ**. `sync` never appends an unchanged state, so an A→B→A oscillation is three legitimate changes. Not a loosening: the consecutive no-op is still rc 1. |
| **A8** | The five string anchors did not "stay" — 25 test defs removed, 22 added. Most content was absorbed into the property classes, but **`--no-pending` coverage was lost outright** while the code path stayed live. | Restored, plus a named anchor per reviewer finding so none can be re-lost. |

### ⚠️ also fixed (cheap, and each was a correctness gap rather than a preference)

- **⚠️2 baseline ancestry.** `cat-file -e` PASSES on a commit orphaned by the routine non-ff rebase recovery in
  root `CLAUDE.md` session-end step 3. A third state A1 never named: record PRESENT, record INVALID. Now
  `merge-base --is-ancestor`, rc 2 with a re-record instruction.
- **⚠️3 committed renames.** The pending side synthesized a rename origin; the committed side used
  `--name-only`, which prints the destination alone — so `git mv` to `archive/`, routine closeout work, made the
  origin vanish. Now `--no-renames`. The old test asserted the property in its NAME while covering only the
  uncommitted half.
- **⚠️4 / ⚠️5 stale text I introduced this session:** the agent file carried BOTH the redesign's description and
  the deleted `watermark` output line — ARGUS's own method rule 2 ("two live versions = ❌") turned on its
  author. And one suite had three different counts across three surfaces. Counts are now measured, with the
  rule written into the test README.

### ⛔ DECLARED RESIDUE — NOT fixed, and one of them is a design question, not a defect

- **⚠️1 — B1 silently re-dates a decision on the Deck.** Every non-REGISTERED event stamps `at = today` and the
  Deck renders the last event's date, so **correcting a typo moves the date Will was told the decision
  happened.** Live ledger: 200 rows, **0 UPDATED events**, so this is latent until the first correction — i.e.
  the next closeout. This is a SEMANTICS call (what does a decision's date mean after a correction?), not a
  patch, and it belongs to Will, not to a late-session edit.
- **⚠️6 — B3's hosted leg.** The reviewer has no access to the tap store; PROME's no-loss finding is
  **recorded, not independently verified**. Residual in the code: "latest" compares a CLIENT-clock `ts`, so two
  taps in the same millisecond or two devices with skewed clocks leave "latest" undefined.
- **⚠️7 — cost, carried to C4. FIGURES CORRECTED after ARGUS trial run 1 found the first set did not sum.**
  Measured now, after the final A4 fix, by `python3 PROME/tools/argus_scope.py --json` + a lane count:
  **OWNED 38 · SHARED 89 = 78 inbox + 11 fleet-memory · EXCLUDED 190.** Of the 78 inbox paths only
  **14** carry a `from-PROME` hint; **64** do not — which is exactly why no filename may decide visibility.
  ⚠️ **A4's no-drop guarantee roughly TRIPLES the audit surface over the OWNED lane alone.** That is the
  declared PRICE of the honest failure direction. It is a price, not a free win, and it is reported as one.
- The session's own declared N/A: two non-atomic git snapshots under a concurrent second session.

### What the reviewer could NOT break
> *"No commit subject can influence any lane, and no classification lives in code... The prior five defects are
> genuinely dead as a class — the three ❌ above are NEW boundaries (a lane subdirectory, a ledger revert, a
> deleted test), not re-runs of subject or filename inference."*
