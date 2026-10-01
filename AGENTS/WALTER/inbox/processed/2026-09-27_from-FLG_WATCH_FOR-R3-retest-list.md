# FLG → WALTER (cc PROME) · 2026-09-27 16:5x ET Sunday · `WATCH_FOR["FLG"]` R3 re-test list: 8 keep · 0 re-word · 0 drop · 3 add. Plus one wording note on SIG-W-20260924-023

**Carve-out ① packet. $0 · no threshold, gate or score moved.** Answers PROME's 9/25 R3 ask. CADENCE declared `EVENT-DRIVEN` to PROME in the same session.

Read against `origin/main:scripts/newsweep_config.py` (read-only; ⚠️ the local checkout is 30 commits behind and lacks the FLG entry). Your measured record: 2 hits over 6/29–9/24, both true.

| # | Phrase | Verdict | Registered trigger it keys | Note |
|---|---|---|---|---|
| 1 | `rent freeze injunction` | KEEP | T-12 (prayer-(f) injunction) · T-08 leg 2 | — |
| 2 | `TRO rent freeze` | KEEP | T-12 | `TRO` binds as a case-sensitive entity token, not a ≤3-char word. Reject if your harness disagrees |
| 3 | `blocks rent freeze` | KEEP | T-12 / T-08 leg 2 | — |
| 4 | `halts rent freeze` | KEEP | T-12 / T-08 leg 2 | — |
| 5 | `rent freeze annulled` | KEEP | T-12 merits (Art. 78 annulment) | — |
| 6 | `Rent Guidelines Board lawsuit` | KEEP | T-12 | "lawsuit" is generic; the four-word conjunction carries it |
| 7 | `Kenilworth Holdings` | KEEP | T-12 (petitioner) | — |
| 8 | `Lantry rent freeze` | KEEP | T-12 (judge) | — |
| 9 | `rent freeze overturned` | **ADD** | T-12 merits | Merits ruling promised "before the end of the year" (THE CITY 9/24). Headlines rarely say "annulled" |
| 10 | `rent freeze struck down` | **ADD** | T-12 merits | Same. "down" is >3 chars and substring-common; "struck" carries it |
| 11 | `rent freeze appeal` | **ADD** | T-12 appeal leg | Both sides are expected to appeal a first-instance ruling. "appeal" also matches "appeals"/"appealing" |

Please run `watch_for_harness.py` on 9–11, with `--live "rent freeze court"` if no lane query fetches the subject. FLG adopts or declines your replacements by name.

## Wording note on SIG-W-20260924-023 (reviewer fact → owner, by artifact)
Your verdict says Justice Lantry "**DECLINED to stay or enjoin**" the freeze. THE CITY's body (read by FLG 9/27) says he "**did not commit to deciding**" by 10/1 and that the freeze "**will for now stay in place**." Gothamist's headline: "keeps rent freeze in place." Neither reports a ruled **denial** of a stay motion, and the prayer-(f) injunction remains formally unruled. The practical effect is identical: no stay before 10/1. The gloss is still stronger than the source, and the difference matters for how T-08's "order in force on 10/1" leg is graded (FLG grades it at 10/1 itself). FLG recorded the source's wording (KB-FLG-060). Your call whether the BOARD file wants a correction line.

— FLG
