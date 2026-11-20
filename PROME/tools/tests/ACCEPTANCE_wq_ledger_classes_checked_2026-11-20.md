# Acceptance — the queue ledger refuses a new decision row that does not say which grants were checked, 2026-11-20

reads: 1 of 3 (one result read; no plan read)

Authority: WQ-716 (Will 2026-11-17 21:15 ET), DOCKET L1188 item 3: `PROME/tools/wq_ledger.py` refuses a new OPEN DECISION row whose Notes do not state which done-without-asking classes (C1 to C13) were checked and why none applies. An existing tool is extended; no new tool.

Defect: PROME registers a decision for Will that one of his standing grants already covers, so he is asked for a word he already gave (`memory/auto/feedback_check_existing_grants_before_asking_will.md`, Will 11/17). Nothing at registration makes PROME look.

Written before any edit to the tool.

Properties:
1. Ordinary: `sync` finds a queue number the ledger has never seen, in the queue's OPEN table, whose Type cell contains DECISION, and whose Notes cell lacks the statement. It returns 1, appends nothing (ledger and seal bytes unchanged), and its message names the row and the words required. With the statement present the row is registered exactly as before.
   The statement: the words "C1 to C13 checked" ("through" or a dash also accepted), then "none applies", then a reason of at least 15 characters. Row 724 is the model: "Classes C1 to C13 checked: none applies (a trade, root rule #5; ...)".
2. Overlap:
   - a new row of any other Type (HANDS and the rest) registers without the statement;
   - a number first seen already decided (in RECENTLY DONE or an archive) registers without it: Will has already ruled;
   - a row the ledger already holds is never refused, whatever its Notes say: the check reads REGISTERED events only, so later edits (UPDATED), rulings and closes are untouched. Forward only;
   - a new DECISION row that is blocked (`⛔ waits`) needs the statement as an open one does;
   - one refused row refuses the whole run: no other event is appended until the row is fixed. Declared, so the ledger never holds a partial sync;
   - a broken seal is still refused first, with its existing message;
   - `backfill`, `check`, `state` and the existing selftest cases behave as before.
3. Wrong owner: N/A. Only PROME writes the queue and runs this tool.
4. Missing information: an empty Notes cell is refused. "C1 to C13 checked" with no "none applies", or with no reason after it, is refused.
5. Concurrent activity: N/A, one writer; the seal check is unchanged.

Declared limits before the build:
- The tool tests that the statement is there, not that the reason is right. A wrong or lazy reason passes. That judgment stays with PROME and with Will's undo.
- The Type test is on the word DECISION. A decision registered under another Type word is not checked.
- A row registered by hand-editing the ledger is outside this check (the seal catches that separately).

## Disposition 2026-11-20 13:22 ET (WQ-229 states)

IMPLEMENTED · TESTED (the tool's selftest, nine new cases; `test_wq_ledger_L336.py` 24 of 24; a sync on a copy of the live ledger appended 0 events) · INDEPENDENTLY VERIFIED by one Opus reader with its own counterexamples for properties 1 (open and blocked rows), 2 and 4; after every refusal the ledger and seal bytes were identical and `check` passed · STILL UNRESOLVED: the one failed property and the residue below. The code is committed as the reader read it; nothing in the tool was changed after the read.

The reader's one failure, answered by a limit written AFTER the read (this paragraph is unreviewed):
- A new DECISION row that the queue parser reads as already ANSWERED (its Item leads with Will's approval, or its Type cell carries RULED) registers without the statement. Property 1 as written did not except it. The code is left as it is on purpose: such a row records a word Will has already given (the C2 kind, registered and recorded in one step), and it is not an ask, the same reason as the already-decided bullet of property 2. The cost, stated plainly: a row can avoid the check by being written as answered when it is not. That is a false record of Will's word, which the ruling-record rules already forbid; this tool does not detect it.

Declared residue (reader's flags, none fixed):
- Any text after "none applies" counts as the reason, including an unrelated later sentence of the Notes cell.
- Refused although meant well: markdown inside the phrase (`C1 to **C13** checked`), and an escaped pipe straight after the colon. The refusal message spells out the words to write.
- The Type test is a substring: a Type cell reading `NON-DECISION` would be checked.
- Not tested: the `state` command, the command-line entry point, a refusal naming several rows, a number first seen in an archive file.
