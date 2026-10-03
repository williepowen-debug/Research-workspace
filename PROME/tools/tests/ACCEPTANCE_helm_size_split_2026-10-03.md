# ACCEPTANCE CONDITIONS — the Helm size split (`will_handbook.py` + `desk_attention.py` → small page + `docket.html` supporting file)

**Written 2026-10-03 13:47 EDT by PROME (`prome-ed`), BEFORE any code** (WQ-229). Driver: Will 2026-10-03 13:37 ET *"can we fix that so close out doesnt keep reading it at close out"* and 13:4x *"Its not something you could fix easilly yourself?"*. At this stamp HEAD `37b92ed0c`; `will_handbook.py` md5 `a25d45cd568622a38f6f73eb501a9b82`; `desk_attention.py` md5 `c1a822fe0121e94ccc2ca89d60eeb90a`. The 13:1x closeout build measured 419,929 B (`measure.py`, scratchpad `handbook.html`), of which the desk tab's `#prome-work` section — 77 pending PROME docket rows rendered with every cell whole — was 242,829 B, and `Top priorities` 54,878 B on ONE line (`render_body` joins blocks with `""`). The manual tab was 10,325 B: the DAEDALUS scope addition of 13:5x aimed at the wrong tab and is corrected by this record.

## The property, in its own terms

The publisher refuses to republish a page the session has not VIEWED; a supporting file published beside the page needs only an in-session file LISTING. So the cost of a republish is the page's bytes, and the page must carry only what Will reads at the desk. **Property: the Helm page keeps one identifying line per pending PROME docket row and a link to that row's full record; the full records move, unchanged, to a supporting file beside the page; nothing is lost, no link dangles, and no line of either file is longer than a reader's page.**

## Conditions (the test list)

| # | Condition | How it is checked |
|---|---|---|
| P1 | **No loss.** The set of docket line numbers in the page's `#prome-work` section == the set in `docket.html` == `pending_work()`'s rows; for every row, `docket.html` contains the escaped `title`, `state`, `next` and `evidence` strings exactly as the pre-split render (`legacy_attention.html`, captured at this stamp) carried them. | test + script diff against the captured legacy render |
| P2 | **No dangling link.** Every `href` from the page into `docket.html` names an `id` present in `docket.html`; `docket.html` is a complete document (doctype · charset · viewport · `<title>` · explicit body background · dark-mode tokens) and links back to the page. | test (regex over both outputs) |
| P3 | **Size.** Page bytes after the split < 60% of the pre-split build on the same sources; the longest line of the page and of `docket.html` ≤ 10,000 B (`render_body` joins with newlines; the docket page one row per line). | `measure.py` before/after, in the delivery note, never in prose |
| P4 | **Republish after viewing only the page.** The Helm republishes with `files={"docket.html": …}` after a view of the page alone. THIS session already viewed the Helm (16:27 10/2), so the only live test possible today is that the publish-with-files call succeeds; **the condition itself is PENDING until the first closeout of a NEW session** — recorded as such, never claimed. | next session's closeout report |
| P5 | **Contract kept.** `desk_attention.render(root)` called as today (no link target) returns the pre-split output byte-for-byte; the error list is unchanged in both modes; `will_handbook.py --no-feed` returns 0 with the same ALERTS as before; the change-feed still advances exactly once per real render. | existing suite + a byte-equality test on the legacy mode |
| P6 | **Write order.** `docket.html` is written BEFORE `handbook.html`, so a page never exists on disk without the file it links to; if `pending_work` raises, the page carries the error (as today) and NO link to a file that was not written. | test (raise injected → page has no `docket.html` href) |

## The five categories (CONSIDER each; N/A must be justified)

1. **Ordinary** — P1, P2, P3.
2. **Overlap** — a row both OVERDUE and PENDING, both in the page and in the file (every row is): P1's set equality is the test. A page rendered in legacy mode and in split mode in the SAME process must not share mutable state — P5 renders both orders and compares.
3. **Wrong owner** — rows that do not name PROME stay out of BOTH files; rows naming PROME inside another owner cell (`TERRY (PROME commissions)`) are in both: the one filter function serves both renders, P1 checks it.
4. **Missing information** — an unparseable pending date raises as today (unchanged, tested already at L100 of the suite); the split adds the P6 case: when the rows cannot be built, the page must not link to an absent file.
5. **Concurrent activity** — N/A: one process writes both files in sequence; the publisher receives both in one call. (The change-feed single-writer property is unchanged and already tested.)

## Not in scope (named so they are not silently claimed)

The content of `HANDBOOK.md` § Top priorities (55 KB of PROME-curated text — a rotation, owed separately) · the brief tab (56 KB) · republish cadence of the supporting file (a CLOSEOUT.md rule; 10/25 review) · the Deck reference page's staleness (Will's call, brought with this build's result).

## Disposition (filled after the reads)

IMPLEMENTED: — · TESTED: — · INDEPENDENTLY VERIFIED: — · STILL UNRESOLVED: —
