# Third read: willq_fix3.diff (bounded to the fix diff), 2026-11-14
Base verified: /tmp/prome-boot-da3a4bd9/willq_view.read2.py is byte-identical to fix2.py, the copy I read second. Fix under test: copied to fix3.py.

| # | Claim | Artifact | Command | Observed | Proposed change |
|---|---|---|---|---|---|
| ✅G1 | F1/F2 and read-1 ❌1/❌2 fixed as a class | zero-row branch: `"\|" in line` | cx_f3.py (C1-C4, C15), cx2_f3.py (N7-N10) | all REFUSED | — |
| ✅G2 | True empty states still render | — | C7, C9, C14, N1-N4, N6 | all [] | — |
| ✅G3 | Selftest | — | --selftest | 55/55 PASS | — |
| ✅G4 | Non-empty output unchanged | — | before.py vs fix3, live queue | byte-identical (True); N11 rows-present ['684'] on both | — |
| ⚠️G5 | A true empty queue is refused when the OPEN section holds any prose pipe | `"\|" in line` | P1 (note with an inline-code pipe), P2 (HTML-comment row template), P3 (escaped `\|` in prose) | REFUSED (the safe direction). The live file holds no such line today (N6 renders []). | Add to the residue block: an empty queue may be refused if prose with a pipe is added to § OPEN. |
| ⚠️G6 | Open rows still hidden as "0 open" | — | P4 (stray `## ` heading = ⚠️4), P5 (`DONE when…` = ⚠️3), P6 (HTML table row), P8 (fullwidth ｜ pipes) | [] | P4/P5 are already declared residue. P6/P8 are not markdown pipe tables; this tool has never read them. |
| ✅G7 | U+2028 inside a row | — | P7 | REFUSED as SHIFTED (old tool the same) | — |

## Fixtures and full output
print("=== NEW against fix3")
more={
 "P1 true empty + prose note with inline-code pipe": W(H+S+"\n*Nothing open since 11/13; check with `willq_view.py --check | tail -1`.*\n"),
 "P2 true empty + commented row template": W(H+S+"<!-- template: | NNN | **Question?** | DECISION | YYYY-MM-DD | m/d | rec | note | -->\n"),
 "P3 true empty + escaped pipe in prose": W("Rows are `# \\| Item`.\n"+H+S),
 "P4 hidden: open row under a stray '## ' heading (residue ⚠️4)": W(H+S+"## Parked\n"+R),
 "P5 hidden: lone open row, item starts 'DONE when'": W(H+S+"| 684 | DONE when Will rules? | DECISION | 2026-11-20 | 11/14 | rec | note |\n"),
 "P6 hidden: row inside HTML table": W(H+S+"<table><tr><td>684</td><td>Approve</td></tr></table>\n"),
 "P7 hidden: row wrapped by U+2028 inside item": W(H+S+"| 684 | **x y** | DECISION | 2026-11-20 | 11/14 | rec | note |\n"),
 "P8 hidden: open row with fullwidth pipes ｜": W(H+S+R.replace("|","｜")),
}
for k,t in more.items(): print(f"{k}\n   old: {run(old,t)}\n   fix: {run(new,t)}")

N1 colon separator
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: ROWS []
N2 spaced separator
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: ROWS []
N3 blank line between header and separator
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: ROWS []
N4 comment between header and separator
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: ROWS []
N5 header first cell holds a digit ('#1')
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: REFUSED: OPEN table parsed to zero rows and its first table line ('WQ (2026)') is not a header followed 
N6 live WILL_QUEUE with every numbered row removed
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: ROWS []
N7 lone open row WITHOUT leading pipe (GFM-valid)
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: REFUSED: OPEN table parsed to zero rows but holds 1 line(s) with a pipe that do not start with `|` (inde
N8 lone open row led by zero-width space
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: REFUSED: OPEN table parsed to zero rows but holds 1 line(s) with a pipe that do not start with `|` (inde
N9 lone open row led by BOM
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: REFUSED: OPEN table parsed to zero rows but holds 1 line(s) with a pipe that do not start with `|` (inde
N10 lone row as list item '- |'
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: REFUSED: OPEN table parsed to zero rows but holds 1 line(s) with a pipe that do not start with `|` (inde
N11 rows present + leading-pipe-less row (A7 parity)
   old: ROWS ['684']
   fix: ROWS ['684']
A5 live parity vs before.py: True
=== NEW against fix3
P1 true empty + prose note with inline-code pipe
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: REFUSED: OPEN table parsed to zero rows but holds 1 line(s) with a pipe that do not start with `|` (inde
P2 true empty + commented row template
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: REFUSED: OPEN table parsed to zero rows but holds 1 line(s) with a pipe that do not start with `|` (inde
P3 true empty + escaped pipe in prose
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: REFUSED: OPEN table parsed to zero rows but holds 1 line(s) with a pipe that do not start with `|` (inde
P4 hidden: open row under a stray '## ' heading (residue ⚠️4)
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: ROWS []
P5 hidden: lone open row, item starts 'DONE when'
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: ROWS []
P6 hidden: row inside HTML table
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: ROWS []
P7 hidden: row wrapped by U+2028 inside item
   old: REFUSED: SHIFTED WQ-684: 2 cells vs header 7 — an unescaped `|` inside a cell shifts every column; write
   fix: REFUSED: SHIFTED WQ-684: 2 cells vs header 7 — an unescaped `|` inside a cell shifts every column; write
P8 hidden: open row with fullwidth pipes ｜
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: ROWS []
C1 header row lost, one open row (with separator)
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: REFUSED: OPEN table parsed to zero rows and its first table line ('684') is not a header followed by its separator row    <<< CHANGED
C2 header row lost, one open row, no separator
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: REFUSED: OPEN table parsed to zero rows and its first table line ('684') is not a header followed by its separator row    <<< CHANGED
C3 one open row indented 1 space
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: REFUSED: OPEN table parsed to zero rows but holds 1 line(s) with a pipe that do not start with `|` (indented, quoted or   <<< CHANGED
C4 one open row in blockquote
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: REFUSED: OPEN table parsed to zero rows but holds 1 line(s) with a pipe that do not start with `|` (indented, quoted or   <<< CHANGED
C5 open row whose Item begins CLOSED-END
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: ROWS []   <<< CHANGED
C6 open row whose Item begins 'TERMINAL value'
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: ROWS []   <<< CHANGED
C7 CRLF true empty
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: ROWS []   <<< CHANGED
C8 CRLF one open row
   old: ROWS ['684']
   new: ROWS ['684']
C9 header-only + trailing closed row
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: ROWS []   <<< CHANGED
C10 first cell empty
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: REFUSED: OPEN table parsed to zero rows but holds 1 table line(s) whose first cell is not a WQ number (first: '<blank>'   <<< CHANGED
C11 empty-queue placeholder row (— none open)
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: REFUSED: OPEN table parsed to zero rows but holds 1 table line(s) whose first cell is not a WQ number (first: '—') — re   <<< CHANGED
C12 open row inside ### subsection
   old: ROWS ['684']
   new: ROWS ['684']
C13 open row after '##OPEN-like' text split: row below a '## Notes' heading inside OPEN
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: ROWS []   <<< CHANGED
C14 empty OPEN at end of file, no following section
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: ROWS []   <<< CHANGED
C15 non-breaking-space-led row
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: REFUSED: OPEN table parsed to zero rows but holds 1 line(s) with a pipe that do not start with `|` (indented, quoted or   <<< CHANGED
C16 struck number ~~684~~ only
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: REFUSED: OPEN table parsed to zero rows but holds 1 table line(s) whose first cell is not a WQ number (first: '~~684~~'   <<< CHANGED
C17 header wrapped in code fence lines (```) with nothing open
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: ROWS []   <<< CHANGED
