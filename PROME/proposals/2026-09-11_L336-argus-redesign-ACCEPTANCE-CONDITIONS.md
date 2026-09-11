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
