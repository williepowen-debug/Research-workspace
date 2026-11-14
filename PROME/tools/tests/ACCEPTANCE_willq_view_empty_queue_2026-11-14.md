# Queue view: a true empty queue renders, an unreadable one still refuses

Written before the edit, 2026-11-14 (session prome-fe). DOCKET row dated 2026-11-16, "THE QUEUE VIEW TOOL CANNOT SHOW AN EMPTY QUEUE". `reads: 3` (the ceiling; all three by one independent Opus reader, recorded under Result).

The defect, in its own terms: `PROME/tools/willq_view.py` treats "the OPEN table yielded no open rows" as proof of a parse failure. Those are two different states. A queue with a well-formed header and nothing open is a true state (first seen 2026-11-13 when WQ-31 closed), and the tool must show it as 0 open. A table it cannot read must keep refusing. Scope: this one tool and its selftest. The gate, the brief and the deck have their own parsers and are not edited; the deck already treats an empty queue as a real state.

Acceptance:
- A1. Header of 7 columns, separator, no table line after it: `parse_open` returns an empty list; `--write` renders a block reading "0 open, 0 blocked" whose item text is the word "none"; `--check` on that block returns rc 0.
- A2. Header present and every data row closed in place (leading ✅, DONE, RESOLVED, TERMINAL, DECLINED, CLOSED): also 0 open, same render. Closed-in-place rows were never open asks.
- A3. Header present, zero recognised rows, and at least one table line of header width whose first cell does not begin with a digit: REFUSED (rc 2), the message naming the count and the first such cell. This is the parse-failure shape the old guard protected against (a row numbered `WQ-684` or `**684**`), and it must not render as "0 open".
- A4. Unchanged refusals: no `## OPEN` section, no header row, a header that is not 7 columns, a shifted row, a non-ISO date.
- A5. A non-empty queue renders byte-identical to the tool before the edit (the existing 32 selftest cases, minus the one zero-row case this file replaces, and the live `--check` on `PROME/SCRATCH.md`).
- A6. Drift across the boundary is caught: a block saying 1 open over an empty queue is rc 1, and a block saying 0 open over a queue with one open row is rc 1.
- A7. When at least one row is recognised, a non-digit line is skipped exactly as before. This repair does not change that behaviour.

Neighbours:
- Ordinary: A1, A5.
- Overlap: A2 (rows present and closed at once); a closed-in-place row beside an unnumbered row with nothing open refuses (A3 wins over A2).
- Wrong owner: N/A, the tool reads one PROME-owned file and writes one PROME-owned block; no ownership branch exists.
- Missing information: A3, A4.
- Concurrent activity: N/A, one read then one write of a single file, unchanged by this repair.

Required result: selftest extended with A1, A2, A3, A6 and the overlap case; `queue_parser_selftest.py` still agrees; live `--check` rc 0; an independent reader devising its own counterexample before the repair is called fixed.

## Result

Recorded 2026-11-14 11:23 ET by PROME prome-fe. One independent reader (Agent-tool helper `willq-reader`, Opus, read-only on the repository, fixtures under its own temp directory), three reads, each with counterexamples of its own. Ledgers, copied whole: `PROME/reports/2026-11-14_willq-view-repair/LEDGER_read1.md`, `LEDGER_followup.md`, `LEDGER_read3.md`.

| Read | Verdict | Blocking findings | What PROME changed |
|---|---|---|---|
| 1 (whole repair) | REJECT, 2 | ❌1 a table whose header line was lost read its one open row as the header and rendered "0 open" · ❌2 an open row led by a space, a non-breaking space or `> ` was skipped and rendered "0 open" | zero rows render only when the first table line is a header with no digit in its first cell and the separator is the next table line; indented or quoted table lines refuse |
| 2 (fix diff only) | REJECT, 1 | ❌F1 an open row written without its leading pipe rendered "0 open" | the named shapes replaced by the class: with zero rows, any unread line of the section that holds a pipe refuses |
| 3 (fix diff only) | ACCEPT, 0 | none | nothing after this read |

Both rejections failed in the dangerous direction (a real open decision shown as nothing pending); A3 as first written covered only the unnumbered-first-cell shape. The conditions the code now meets are A1 to A7 plus the two zero-row rules in the table above.

**Completion note.** IMPLEMENTED: `PROME/tools/willq_view.py`, the zero-row branch of `parse_open` and the "none" item text in `render`. TESTED: selftest 55/55 (was 32; the one zero-row refusal case replaced), `queue_parser_selftest.py` 26/26, live `--check PROME/SCRATCH.md` rc 0, live render byte-identical to the pre-edit tool. INDEPENDENTLY VERIFIED: read 3 ACCEPT with 0 blocking, on the final text; no edit was made after it. STILL UNRESOLVED: the declared residue below; and the live file has not yet been empty under the new tool (the reader exercised a copy of the live queue with every numbered row removed, its case N6).

**Declared residue, 2026-11-14 (flags not fixed).**
- Read 1 ⚠️3 and read 3 P5: a row whose item text begins with CLOSED, TERMINAL, DONE, RESOLVED or DECLINED is classed closed in place. If it is the only open row the tool now renders "0 open" where the old one refused. The classifier predates this repair and is shared with the gate; A2 makes it the only defence for that shape.
- Read 1 ⚠️4 and read 3 P4: a stray `## ` heading inside § OPEN ends the section; rows under it are not read, and with nothing above it the tool renders "0 open". Rows under a stray heading were already lost silently whenever another row existed.
- Read 1 ⚠️5: the sentence above that the deck "already treats an empty queue as a real state" is true for the header-and-no-rows shape only. For the closed-rows-only shape (A2) the deck's populated-table guard counts closed numbered rows, so the gate's deck advisory would read UNKNOWN while this tool reads 0 open. Outside this tool's scope; not changed.
- Read 2 ⚠️F3: a header whose first cell holds a digit (for example `WQ (2026)`) is refused when nothing is open. Fails safe; the live header is `#`.
- Read 3 ⚠️G5: a true empty queue is refused if § OPEN holds any prose or comment line containing a pipe. Fails safe; the live section has no such line.
- Read 3 P6 and P8: an HTML table, or a row written with fullwidth `｜`, is not a markdown pipe table and renders "0 open" when nothing else is open; this tool never read those shapes.
- Not checked by the reader: whether a row without its leading pipe is displayed as a table row by a markdown renderer (the refusal does not depend on it).
