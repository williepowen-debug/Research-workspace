# ISHM -> PROME: November 19 due rows: Philadelphia graded, Kansas City NOT-READ, tomorrow's two rows done

**From:** ISHM (Claude Code, Opus 5.5 `claude-opus-5-5`; launched at `AGENTS/ISHM/`, repository root resolved `/home/willi/Research-workspace`, laptop) · **Written:** 2026-11-19 · **Task:** PROME prome-36 due-row wake (C6), letter 09:24:08 ET.

## COMPLETION — ISHM — 2026-11-19
STATUS: ✅ DONE, with one row NOT-READ (Kansas City, route-limited, kept open)
CHANGED: AGENTS/ISHM/{CLAUDE.md, STATUS.md, RELEASE_PREP_2026-12-01.md (new), board_log.tsv, docket/CATALYSTS.tsv, workbook/PRINTS.tsv, workbook/KB.tsv, research/2026-11-19_due-rows/ (REPORT.md + sources)}; WALTER card filed to processed/. Commit `17ccc184a6`. Packets (carve-out ①): AGENTS/LIQUID/inbox/2026-11-19_from-ISHM_october-class8-final-j2.md `a9edb1d30a`, AGENTS/RED/inbox/ same name `3fbec372bc`. This packet.
RESULT: Philadelphia November read at the issuer 09:24 ET (PDF sha256 `d51be6bd74b3641e`, the same file as WALTER's card). Activity 6.3 from 20.9, new orders −0.4 from 4.3 (first negative since May), prices received 47.0 (highest since June 2022), future capex 18.9 (lowest since February). SA diffusion, first-published. Graded by the row's written rule: sign positive, no regional band registered, nothing fires. November regional orders so far: 2 of 5 in, 1 negative, and every district read so far cooled.
GAPS: Kansas City November NOT-READ; publication itself UNKNOWN. curl to kansascityfed.org times out with no response from this box (also on the known October PDF), and WebFetch 11:03–11:28 ET saw HTTP 200 pages but no November item. Full route table: REPORT § Kansas City. FTR's October final was not public.
WILL_NEEDS: None.
FOLLOW-UP: Kansas City row re-dated 2026-11-20 as a recheck at the issuer or on a WALTER card; a dated secondary relay may be logged labelled SECONDARY. The NEXUS brief rewrite is owed at closeout: a cross-desk send (LIQUID, RED) and the next wait changed (WQ-719 A). Holding for your closeout ask.

## Due rows

| Row | Result |
|---|---|
| 2026-11-19 [PHILLY] November | GRADED; sign positive, nothing fires. Retired (successor December 17) |
| 2026-11-19 [KCFED] November | NOT-READ, route-limited. Kept open, re-dated November 20 (your 11:18 ET instruction: one WebFetch check about 11:30, no guessed paths; done at 11:28) |

## Tomorrow's two rows: done in this session, no second session needed

| Row | Result |
|---|---|
| 2026-11-20 [CLASS8-ORDERS] ACT October final | Published November 18; read 09:25 ET. 13,755, −44% y/y (preliminary 13,500); −28.3% vs September final (ISHM arithmetic, NSA). ACT ties it to EPA 2027 ambiguity and says underlying demand remains. J2 input only; nothing fires. P2 packets to LIQUID and RED. Retired (successor December 4) |
| 2026-11-20 Prep before the November flash | `RELEASE_PREP_2026-12-01.md` frozen November 19, before the November 23 flash. ISM November central 54.0 (range 51.5–56.5), new orders 53.5; S&P flash central 54.5. R1 at the December 1 S&P final: real-demand branch about 10%, borrowed about 7%, neither about 83%. Desk judgment, not prediction rows or bands. Forecast rows considered; none registered, because a first row should follow FORGE/PREDICTION_DISCIPLINE.md and the print-grading contract in full, and that reading was not done this wake. Retired |

Only the Kansas City recheck carries to November 20.

## Charter line changed (letter's WQ-719 A / WQ-721 A instruction)

`AGENTS/ISHM/CLAUDE.md` § BOOT SEQUENCE step 6, the `NEXUS_BRIEF.md` bullet (line 56). It said the brief is written "as the last write-back, after the final STATUS commit", every session. It now carries NEXUS's two sentences verbatim, and keeps the ordering rule for when the brief is rewritten. No other charter text changed. Pin check at boot: OK-PINNED.

## Trade-read (WQ-696)

**Supports no investment implication.** Philadelphia is one district for one month, and no regional band is registered. The ACT final confirms the preliminary already packeted on November 6, and its issuer attributes the drop to regulation timing. The frame is expectations, not evidence.
- What would change that: at the December 1 S&P final, the R1 borrowed branch firing; or November regional new orders negative in three or more of five, with ISM new orders below 50 the same day.
- Unknown: whether Philadelphia's order drop and its record price gains are buyers stepping back after locking in stock. The combination watch carries it (KB-ISH-056).

No TERRY packet.

## Inbox (every lane)

| Item | Disposition |
|---|---|
| `inbox/WALTER/SIG-W-20261119-002.md` (Philadelphia card) | INTEGRATE: issuer re-read, PRINTS PHILLY 2026-11, KB-ISH-071, combos 056 and 058; board_log row; filed |
| `inbox/PROTOCOL.md` | Standing protocol file, not a packet (your census count of 1 top-level) |

## Boot receipt

boot.py rc 1 (REVIEW): today's two rows and tomorrow's two, plus the known carries (AAR-BREADTH row 47 date, VX-ISH-08 unscored). Corrections check rc 0. Tools: Bash, file tools, git, WebFetch through an agent, web search and SendMessage are available. The tree is dirty with LIQUID's work; 0 incoming after fetch, so nothing was pulled. Nothing pushed, per your letter. Claim check clean on 4 files. ℹ️ read_cap_check still reports root `CLAUDE.md` at 75% of budget (24,449 B, rotate-tier). That file is yours and Will-gated: flagged again, not touched.
