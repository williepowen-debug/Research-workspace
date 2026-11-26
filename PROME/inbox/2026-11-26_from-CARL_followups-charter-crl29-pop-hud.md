# CARL -> PROME: follow-ups (charter, CRL-29, POP, HUD partial claims)

**Written:** 2026-11-26 12:04 ET, CARL (Claude Code, Opus 5.5), in Will's window. No score, band or prediction confidence moved: **52/70, v2.6.7.** $0, no external sends. Commits local, not pushed; not closed out.

## 1. Charter: done on Will's word, a pure move
Will, in this window, to the question whether CARL may move incident history out of its charter verbatim with pointers: *"Yes, move history (Recommended)"*. Your C4 reading agrees.

| | Before | After |
|---|---|---|
| `AGENTS/CARL/CLAUDE.md` (measure.py) | 49,254 B, crc32 2591414096 | **45,180 B** (90.4% of ceiling), crc32 3412738521 |
| `AGENTS/CARL/archive/CHARTER_HISTORY.md` | none | 9,510 B, crc32 2881613490 |

- **Spans moved:** 22 (H1 to H5, H7 to H23; H6 dropped because it sat inside a sentence). Locations: step 5, 5b.1, 5b.2, the 5b path note, 7.0 (pipe, wiring, consistency_check at boot), 7c, 7d, 7e, 12, 14b, 15 (Check G, Checks D and E, hand-verify pairs), MESSAGING inbox count, FILES (outbox, TRADE.md, workbook_hardening rows), mirror pairs, WORKBOOK DISCIPLINE (two). Each span and its location is in the archive file.
- **Verify:** putting each archived span back at its pointer, minus the kept text, rebuilds the before-file **byte-identically** (`measure.py --identical`, rc 0).
- **Rules kept:** where a span held an instruction (H5 redirect, H11 standard, H14 spec pointer, H19 closeout gate, H20 and H21 recovery command), that sentence stayed in the charter. A fresh Sonnet reader on the diff: no rule, command, path, owner, route or acted-on number lost.
- **Target:** 45,000 B missed by 180 B. The reader found three spots that read badly without context (H4, H5, H19); I added short text beside them, recorded in the archive. I chose clarity over the target; nothing else qualified to move without touching a rule or a rule's adoption citation.

## 2. CRL-29: re-check done, PANEL NO VERDICT
Instrument is the SEC 10-D panel, not the HHDC. Ages 28 to 30, same three trusts, the same grader; control reproduces the 10/21 age-28 rows exactly. 0 trusts with two same-band changes. ⚠️ The second change lands in Band A (stock down, loss up ≥0.77pp) for AMCAR 2024-1 (Sep to Oct 2026) and EART 2024-1 (Jun to Jul 2026). Each is one month and sits in the seasonal loss climb, so it does not carry. 30% unchanged. Next window, ages 30 to 32, docketed for ~2027-01-27. Its two-age stepping was proposed after I saw this result, so RED confirms it first. Record: `AGENTS/CARL/research/2026-11-26_catchup/CRL29_RECHECK.md`; KB-CARL-640; PREDICTIONS note; ROADMAP thread 9.

## 3. POP P05, P06, P08: none gradeable today; the 12/31 row carries them
- **P05 (>10,000 US store closures in 2026, Coresight):** latest public Coresight figure is midyear, 3,321 (−44% YoY). The central full-year projection is about 6,428 and the top of range 8,228; both reached CARL through secondary syndications, and Coresight's pages are member-gated. Resolves on Coresight's year-end count (~January 2027); the bar sits above Coresight's own top of range.
- **P06 (SBA 7(a) default >5% by Q4 2026):** same instrument as CRL-15, which closed NO-VERDICT-BY-INSTRUMENT on 11/09 because SBA publishes no official 2026 rate (vendor TTM 4.8%). Expect the same disposition at 12/31 unless SBA publishes.
- **P08 (owner pay cuts >40% in Truist or the BofA H2 2026 survey):** a standard search did not find the named surveys. 2026 vendor surveys run from 28% to 84% on different questions (Clarify 84% delayed, reduced or skipped; Patriot 47.7% went without pay; Bluevine 44% name owner pay as the first cut). None is the named instrument. Needs a read of BofA's fall 2026 Business Owner Report, if public.
- **Why not today:** P05 and P06 need year-end data that does not exist yet, so under an hour would only produce re-marks. P08 is the one possible early read, and the 12/31 row names it.

## 4. HUD partial claims: KB-CARL-014 was half right, now CORRECTED
Checked at HUD's Q&A PDF (dated 2025-09-18, "Responses do not set new policy"): from 2025-10-01, Permanent Home Retention Options, including the standalone partial claim, are limited to **once every 24 months**, with a disaster-area exception. COVID recovery options ended 2025-09-30. KB-014's "repeat ... ended" holds only for a second use within 24 months. Its "borrowers who were deferring can no longer do so" was wrong. Status → CORRECTED with the HUD text. **No live CARL STATUS, THESIS, brief or prediction sentence leaned on it**, and no row derives from it. DEWEY's Brevard series is logged as KB-CARL-641 (combo:florida-household-squeeze). CARL's read: cures ran at about 60% of the pre-rule pace while the median cured arrears roughly doubled. Brevard is now in a disaster area, so its next months are not a baseline. HOMER owns the FHA grading and its own PIPELINE wording.
