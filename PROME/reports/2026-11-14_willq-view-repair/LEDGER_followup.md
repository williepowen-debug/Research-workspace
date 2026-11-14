# Follow-up read: willq_fix2.diff (bounded to the fix diff), 2026-11-14

Base verified: /tmp/prome-boot-da3a4bd9/willq_view.read1.py is byte-identical to the copy I read in read 1.
Fix under test: PROME/tools/willq_view.py (copied to /tmp/tmp.obTVDsYlsp/fix2.py).
Fixtures: cx.py (C-cases), cx2.py (N-cases against the fix), cx3.py (N-cases against my trial copy trial.py).

## Ledger
| # | Claim checked | Artifact | Command | Observed | Proposed change |
|---|---|---|---|---|---|
| ❌F1 | The zero-row guard now catches every row the parser silently skips | willq_view.py zero-row branch: the `re.match(r"[\s>]+\|", line)` test on lines that do not start with `|` | cx2.py N7 | One open row written without its leading pipe (`684 \| **Approve the thing** \| … \|`, which GFM still renders as a table row under the header): old tool REFUSED; fix returns `[]`, i.e. "0 open … none". Same dangerous direction and same class as read-1 ❌2. | In the zero-row case, also count any non-`\|`-led line with ≥7 cells (`len(split_cells(line)) >= 7`). Trial copy trial.py: selftest 51/51; N7–N10 refused; N1–N4, N6, C7, C9, C14 still render `[]`; N11 rows-present parity is unchanged. |
| ⚠️F2 | Same class, contrived lead characters | the same line | N8 (zero-width space lead), N9 (BOM mid-file), N10 (`- ` list item) | Each returns `[]`; old refused. These are unlikely edits; N10 renders as a list item rather than a table row. | The same trial change covers all three. |
| ⚠️F3 | A true empty queue is not wrongly refused | header/separator test | N5 (header first cell `WQ (2026)`) | REFUSED (refuses safely, with a clear message). The live header's first cell is `#`, so this does not apply today. | None. Disclose it in the residue. |
| ✅F4 | Read-1 ❌1 and ❌2 fixed | fix diff | cx.py C1, C2, C3, C4, C15 | All REFUSED with the new messages | — |
| ✅F5 | True empty states still render | fix diff | C7 (CRLF), C9, C14, N1 (colon separator), N2 (spaced separator), N3 (blank line between header and separator), N4 (comment between them), N6 (live WILL_QUEUE with every numbered row removed) | All `[]` | — |
| ✅F6 | Selftest | — | `python3 PROME/tools/willq_view.py --selftest` | `willq_view selftest: 51/51 PASS` | — |
| ✅F7 | Non-empty output unchanged | — | before.py vs fix on the live queue: render(parse_open) | byte-identical (True); N11 rows-present `['684']` on both | — |

## N-case fixtures and output
import fix2 as new, old, datetime as dt, re
H="| # | Item | Type | Needed by | Since | PROME rec | Notes |\n"
S="|---|---|---|---|---|---|---|\n"
R="| 684 | **Approve the thing** | DECISION | 2026-11-20 | 11/14 | rec | note |\n"
W=lambda body:"# q\n## OPEN\n"+body+"## RECENTLY DONE\n"
live=open("/home/willi/Research-workspace/PROME/WILL_QUEUE.md",encoding="utf-8").read()
sec=live.split("## OPEN",1)[1].split("\n## ",1)[0]
live_empty=live.replace(sec,"\n".join(l for l in sec.splitlines() if not re.match(r"\|\s*\d",l))+"\n",1)
cases={
 "N1 colon separator": W(H+"|:---|:---:|---:|---|---|---|---|\n"),
 "N2 spaced separator": W(H+"| --- | --- | --- | --- | --- | --- | --- |\n"),
 "N3 blank line between header and separator": W(H+"\n"+S),
 "N4 comment between header and separator": W(H+"<!-- none open -->\n"+S),
 "N5 header first cell holds a digit ('#1')": W(H.replace("| # |","| WQ (2026) |")+S),
 "N6 live WILL_QUEUE with every numbered row removed": live_empty,
 "N7 lone open row WITHOUT leading pipe (GFM-valid)": W(H+S+R.lstrip("|")),
 "N8 lone open row led by zero-width space": W(H+S+"​"+R),
 "N9 lone open row led by BOM": W(H+S+"﻿"+R),
 "N10 lone row as list item '- |'": W(H+S+"- "+R),
 "N11 rows present + leading-pipe-less row (A7 parity)": W(H+S+R+R.replace("684","685").lstrip("|")),
}
def run(m,t):
    try: return "ROWS "+str([r['n'] for r in m.parse_open(t)])
    except m.WillqError as e: return "REFUSED: "+str(e)[:95]
for k,t in cases.items(): print(f"{k}\n   old: {run(old,t)}\n   fix: {run(new,t)}")
d=dt.date(2026,11,14)
print("A5 live parity vs before.py:", old.render(old.parse_open(live),d)==new.render(new.parse_open(live),d))

--- output against fix (cx2.py):
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
   fix: ROWS []
N8 lone open row led by zero-width space
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: ROWS []
N9 lone open row led by BOM
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: ROWS []
N10 lone row as list item '- |'
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: ROWS []
N11 rows present + leading-pipe-less row (A7 parity)
   old: ROWS ['684']
   fix: ROWS ['684']
A5 live parity vs before.py: True
--- output against trial.py (cx3.py):
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
   fix: REFUSED: OPEN table parsed to zero rows but holds 1 indented or quoted table line(s) the parser does not
N8 lone open row led by zero-width space
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: REFUSED: OPEN table parsed to zero rows but holds 1 indented or quoted table line(s) the parser does not
N9 lone open row led by BOM
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: REFUSED: OPEN table parsed to zero rows but holds 1 indented or quoted table line(s) the parser does not
N10 lone row as list item '- |'
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   fix: REFUSED: OPEN table parsed to zero rows but holds 1 indented or quoted table line(s) the parser does not
N11 rows present + leading-pipe-less row (A7 parity)
   old: ROWS ['684']
   fix: ROWS ['684']
A5 live parity vs before.py: True
--- C-cases against fix (cx.py):
C1 header row lost, one open row (with separator)
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: REFUSED: OPEN table parsed to zero rows and its first table line ('684') is not a header followed by its separator row    <<< CHANGED
C2 header row lost, one open row, no separator
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: REFUSED: OPEN table parsed to zero rows and its first table line ('684') is not a header followed by its separator row    <<< CHANGED
C3 one open row indented 1 space
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: REFUSED: OPEN table parsed to zero rows but holds 1 indented or quoted table line(s) the parser does not read — refusin   <<< CHANGED
C4 one open row in blockquote
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: REFUSED: OPEN table parsed to zero rows but holds 1 indented or quoted table line(s) the parser does not read — refusin   <<< CHANGED
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
   new: REFUSED: OPEN table parsed to zero rows but holds 1 indented or quoted table line(s) the parser does not read — refusin   <<< CHANGED
C16 struck number ~~684~~ only
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: REFUSED: OPEN table parsed to zero rows but holds 1 table line(s) whose first cell is not a WQ number (first: '~~684~~'   <<< CHANGED
C17 header wrapped in code fence lines (```) with nothing open
   old: REFUSED: OPEN table parsed to zero rows — refusing to write an empty block
   new: ROWS []   <<< CHANGED
