**REJECT. I found 2 ❌, both failing in the dangerous direction:** a real open decision can now be shown to Will as "0 open … none", and `--check` agrees with it (rc 0), where the old tool refused (rc 2). Everything else held. My fixtures are in `/tmp/tmp.obTVDsYlsp/` and I wrote nothing in the repository.

**The two failures**

1. **A table whose header row is missing.** The parser always treats the first table line as the header. If the header line is lost and only one open row remains, that row is taken as the header (it has 7 cells, so the width check passes), and the tool reports an empty queue. This breaks A4's "no header row → refused".
2. **A row that does not start at column 0.** A row led by a space, a non-breaking space, or `> ` (a quote line) is skipped silently. These rows likely still show as table rows in rendered markdown. When the only open row looks like that, the tool reports an empty queue.

**What held**

- A1, A2, A5, A6 and A7 hold, along with the narrow refusal shape A3 actually targets (first cell `WQ-684`, `**684**`, empty or `~~684~~`).
- Non-empty output is byte-identical to the pre-edit tool on its fixture, on the live queue and on a CRLF copy.
- A block written by the old tool is reported as drift (rc 1) once the queue empties.
- The live `--check` and `--dry-run` on `PROME/SCRATCH.md` both give rc 0 with "1 open … WQ-684 (—)".
- The selftests can fail: when I break the guard in specific ways, the relevant test fails each time.

**The fix I'd suggest** (I tried it on a temp copy only): in the zero-row case, also refuse when the header's first cell begins with a digit, or when a section line starts with whitespace or `>` and then `|`. The selftest stayed 42/42, my four failing cases are refused, and the true-empty cases (C7, C9, C14) still render.

**Ledger**

| # | Claim checked | Artifact | Command | Observed | Proposed change |
|---|---|---|---|---|---|
| ❌1 | A4 "no header row → refused" still holds now that zero rows render | `PROME/tools/willq_view.py` L96–100 (header taken from the first table line) with L128–129 (`return []`) | `parse_open` on C1 and C2; `--queue C1.md --write S1.md` then `--check S1.md` | New: rows `[]`, the block reads "0 open, 0 blocked … none", `--check` rc 0. Old: "REFUSED … zero rows", rc 2. A real open WQ-684 is hidden. | In the zero-row case, refuse when the header's first cell matches `\d`. The deck's existing `open_looks_populated` `^\|\s*\d+\s*\|` test catches the same shape. |
| ❌2 | A3's guard covers the zero-row parse failures the old guard caught | L90–92 (`if not line.startswith("|"): continue`) with L125–129 | `parse_open` on C3, C4, C15 | New: rows `[]` → "0 open". Old: refused. | In the zero-row case, count lines matching `^[\s>]+\|` as unreadable. Trial: selftest 42/42, C1–C4 and C15 refused, C7/C9/C14 still render. |
| ⚠️3 | A2 "closed in place → 0 open" is safe | L110 regex `✅\|DONE\b\|RESOLVED\b\|TERMINAL\b\|DECLINED\b\|CLOSED\b` | C5 (`**CLOSED-END fund sizing**`), C6 (`TERMINAL value check …`) | An open row whose item text starts with one of those words is treated as closed. If it is the only open row, the new tool renders "0 open" where the old one refused. This classifier predates the repair and is shared with the gate. A2 makes it the only defence for this case. | Note it in the acceptance file as a known limit of A2. No code change asked. |
| ⚠️4 | How the § OPEN section is delimited | L88 `split("\n## ", 1)` | C13 (a `## Notes on open items` heading inside OPEN, then an open row) | New: `[]` → "0 open". Old: refused. Rows under a stray `##` heading were already lost silently whenever any other row existed. | None for this repair. Disclose it. |
| ⚠️5 | A1 cannot reach the gate/deck backstop | `PROME/tools/prome_gate.py` L1285 / `PROME/tools/decision_deck.py` L229 | read only | The deck's populated-table guard counts closed digit rows too, so for the A2 state the gate's deck advisory would say UNKNOWN while this tool says 0 open. The acceptance file says "the deck already treats an empty queue as a real state", which is true only for the A1 shape. Outside this tool's scope. | Correct that sentence in the acceptance file. |
| ✅ | A1 true empty renders and checks clean | L128–129, L151 | selftest; C7 (CRLF), C14 (OPEN at end of file), C17 | `[]`, the item text is "none", `--check` rc 0 | — |
| ✅ | A2 closed-only → 0 open | L110–111 | selftest; C9 (header-only table with a trailing ✅ row) | `[]` | — |
| ✅ | A3 unnumbered rows refused | L105–107, L125–127 | selftest; C10 (empty first cell), C11 (`— *(none open)*` placeholder), C16 (`~~684~~`) | Refused, naming the count and the first cell | — |
| ✅ | A4 the other refusals are unchanged | L86–124 | selftest (header width, shifted row, non-ISO date, no table) | Pass. The headerless case is ❌1. | — |
| ✅ | A5 byte parity on non-empty queues | L151 | old vs new `render(parse_open(...))` on the fixture, the live WILL_QUEUE, and a CRLF fixture | True ×3 | — |
| ✅ | A6 drift caught across the 0/1 boundary; a pre-edit block is caught too | `do_check` L198–213 | selftest; block written by the old tool, then new `--check` on an empty queue | rc 1 both ways; message "block says ['WQ-684 (11/20)']; queue says —" | — |
| ✅ | A7 skip behaviour unchanged when rows exist | L105–107 | selftest "mixed" | `["12"]` | — |
| ✅ | The selftests can fail | — | A mutated copy: guard removed → 39/42 FAIL; refuse whenever an unnumbered line exists → crash; "none" replaced by "" → 41/42; old parser → crash | Each fault is caught | — |
| ✅ | Live state | `PROME/SCRATCH.md` | `--check PROME/SCRATCH.md`; `--write PROME/SCRATCH.md --dry-run` | Both rc 0, "1 open, 0 blocked … WQ-684 (—)" | — |

**Selftest last lines**

- `willq_view.py --selftest`: `willq_view selftest: 42/42 PASS`
- `queue_parser_selftest.py`: `QUEUE-PARSER SELFTEST ✓ gate · brief · willq_view · deck · table_check agree on the synthetic row set (26/26; split + date-classifier parity)`

**My counterexamples**

Each fixture is `# q\n## OPEN\n` + the table lines below + `## RECENTLY DONE\n`, using:
- H = `| # | Item | Type | Needed by | Since | PROME rec | Notes |`
- S = `|---|---|---|---|---|---|---|`
- R = `| 684 | **Approve the thing** | DECISION | 2026-11-20 | 11/14 | rec | note |`

| Case | Table lines | Old | New |
|---|---|---|---|
| C1 | S, R | REFUSED | `[]` ❌ |
| C2 | R | REFUSED | `[]` ❌ |
| C3 | H, S, ` `+R | REFUSED | `[]` ❌ |
| C4 | H, S, `> `+R | REFUSED | `[]` ❌ |
| C15 | H, S, ` `+R | REFUSED | `[]` ❌ |
| C5 | H, S, `\| 684 \| **CLOSED-END fund sizing** \| DECISION \| 2026-11-20 \| 11/14 \| rec \| note \|` | REFUSED | `[]` ⚠️ |
| C6 | H, S, `\| 684 \| TERMINAL value check on CRUISE \| DECISION \| — \| 11/14 \| rec \| note \|` | REFUSED | `[]` ⚠️ |
| C13 | H, S, `## Notes on open items`, R | REFUSED | `[]` ⚠️ |
| C7 | H, S, CRLF line endings | REFUSED | `[]` ✅ |
| C8 | H, S, R, CRLF line endings | `['684']` | `['684']` ✅ |
| C9 | H, S, `\| 9 \| ✅ **done** \| RULE \| 2026-09-01 \| 9/1 \| rec \| done \|` | REFUSED | `[]` ✅ |
| C10 | H, S, `\|  \| **orphan** \| …` | REFUSED | REFUSED `<blank>` ✅ |
| C11 | H, S, `\| — \| *(none open)* \|  \|  \|  \|  \|  \|` | REFUSED | REFUSED `—` ✅ (a hand-written "none" placeholder is refused, safe direction) |
| C12 | H, S, `### parked`, R | `['684']` | `['684']` ✅ |
| C14 | H, S at end of file, no next section | REFUSED | `[]` ✅ |
| C16 | H, S, `\| ~~684~~ \| …` | REFUSED | REFUSED ✅ |
| C17 | the header inside a fence | REFUSED | `[]` (renders empty) |

**Verdict:** REJECT, 2 ❌ (❌1 headerless table, ❌2 an indented, quoted or non-breaking-space-led row; both show a real open decision as an empty queue). I could not check how rendered markdown actually displays the C3, C4 and C15 rows (my claim that they still show is from the spec, not a render), or how the gate and brief parsers behave on C1 to C4 beyond reading the deck's guard. Both are outside this tool's scope.
