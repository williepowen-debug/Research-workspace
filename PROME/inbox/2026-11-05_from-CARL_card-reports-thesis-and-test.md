# CARL -> PROME: DEWEY's two card reports change neither the thesis nor the test yet; one Capital One line stays open

**Date:** 2026-11-05 | **Assignment:** Will, 2026-11-04 21:12 ET | **Full answer:** `AGENTS/CARL/research/2026-11-05_card-reports/ANSWER.md`, commit `0e11b4958` | **KB:** KB-CARL-583

## Answer in plain words

**1. Does it change the consumer thesis? Not yet, on one line.** The line is the masking framework's Capital One row in `thesis/THESIS.md`, with DR-1's tell "re-default on modified pools". Capital One's borrowers on hardship plans got visibly worse in one quarter: late balances $645M to $993M (+54.0%, against +11.1% for the book), late share 17.2% to 25.2%, defaults $152M to $230M. That is where the framework says to look. But it is one quarter at one lender, the cause is unknown, and the whole card book is better than a year ago (3.74% against 3.89%). Score 53/70, version 2.6.6 and every vector stand. The October 12 finding stands too: concentrated strain supported, broad collapse not established.

**2. Does it change the existing test? No.** The class-wide 50 basis point test stays NOT COMPUTABLE, neither passed nor failed. DR-1 stays PARTIAL: 97.4 bp weighted / 22.5 bp best leg, both older mortgage proxy illustrations. CRL-20 and CRL-31 name Capital One but key on charge-offs, which fell 73 bp in Q3, so neither moves. CRL-21, CRL-30 and the score are untouched. Computable: each lender's own scale, late share, flows and defaults. Not computable: any causal effect, any class-wide figure, any true default rate, the cause of the Capital One move.

**Trap 1, "specific" is not "benign".** Peers flat on late share means the move is not shared on that one measure. It says nothing about harm.
- If it is real, it is real households failing plans and a real lender loss. The open question is whether it is Capital One's own problem or the first place weak borrowers show up. Synchrony and Bread, which also lend to weaker borrowers, show no jump, which argues against "first", but one quarter cannot separate "first" from "only".
- Size: if the whole $348M rise were lost, that is about 13% of one quarter's domestic charge-offs (derived). Material to this group, no threat to the lender.
- The filing can separate only one thing. The 10-Q excludes loans already in default at entry from its default count, so part of the rise is movement into default after entry. It cannot be sized. DEWEY's report does not quote that sentence.
- Discover, portfolio mix and any programme or definition change stay open; the filing cannot separate them. It states no such change, and silence is not proof.
- ⚠️ "Only Capital One" overstates it. Citi is unread, and on default dollars against group size, JPMorgan and American Express also rose on the year (crude, each against itself).

**Trap 2, JPMorgan.** A true default rate is NOT COMPUTABLE from what DEWEY has, so neither "higher" nor "flat" can be claimed. Group size alone explains 58% to 82% of the extra $71M. ⚠️ Defaults still grew faster than the group (+126.8% against +74.1%), so a crude ratio rose (3.41% to 4.44%), but that is not a rate: the group's age moved a lot and the table has no at-risk base. Late share fell from 12.4% to 11.6%. JPMorgan's default (two consecutive missed contractual payments) trips earlier than Capital One's (90+ days, charge-off or nonaccrual), so the two cannot be compared.

**Recommendation:** no threshold, level, gate, score or weight should change. No trade idea arises. The ordinary January issuer read will show whether the $418M at 90+ days cures, re-ages or charges off. No watch or job was registered.

## Notes for PROME

- **Own-record correction:** the THESIS COF cell merged two Discover dates. KB-245 says originations about 100% by end Q3 2026 and back-book Q4 2026 to Q1 2027. Fixed with a CHANGELOG entry, no version bump. If the April timeline held, existing-account conversion came after this jump. Whether it held is UNKNOWN.
- **Assignment facts that differed:** the WALTER caveats were not in my inbox; I read SIG-W-20261104-080 at `BOARD/`. The board-ledger gap packets number four, not three.
- **Boot read:** bounded reader to `eof: true` on all four: root `CLAUDE.md` 5 pages, `AGENTS.md` 1, `USER.md` 2, `AGENTS/CARL/CLAUDE.md` 9.
- **Desk boot, abridged for a bounded session.** SKIPPED: TEAM, whole MEMORY/ROADMAP/SCHEMA reads, ABS monitor (`--quick`), predictions due-scan 7b/7c, ledger staleness 7d, research retirement sweep. `boot.py` rc 1 was only the BOARD gap step.
- **Runtime:** Claude Code, Opus 5.5 (`claude-opus-5-5`). The session clock jumped about 11 hours (21:13 ET to 08:24 ET) while tools were in flight; the first-round stamps were corrected to commit time at `0760f967b`.
- **Checks:** consistency 0 hard, 6 soft, rc 0; read-cap rc 0; claim check clean; brief pin OK; `board_gap --closeout` rc 0. **Nonzero and left:** `board_gap` rc 1 (10 owed action signals) and corrections rc 1 (COR-20261031-22, oil-rig routing). `ledger_staleness --nudge` flagged 26 ledgers; nothing in them changed, so no action. `consumer_check` N/A: no figure superseded.
- **Left in the inbox, none bearing on these questions:** four PROME board-ledger gap packets, DAEDALUS sweep #5, three ISHM packets, eleven `inbox/WALTER/` signals. The 11/03 PHAN runner and GIG band ruling is UNREVIEWED past its date. Named in SCRATCH PRIORITY-1.
- **Not mine:** `AGENTS/WALTER/research/2026-11-04_evening-boot/.cache/` untracked, left alone.

## COMPLETION — CARL — 2026-11-05
STATUS: ⚠️ PARTIAL (assignment done in full; desk closeout partial, owed BOARD and correction items left by instruction)
CHANGED: AGENTS/CARL/research/2026-11-05_card-reports/ANSWER.md, STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, ROADMAP.md, ROADMAP_THREADS.md, thesis/THESIS.md (one dated cell), thesis/CHANGELOG.md, workbook/KB.tsv, docket/CATALYSTS.tsv, docket/CALENDAR.md, board/BOARD_LOG.tsv, board_log.tsv, scripts/data (3 pulse TSVs), two DEWEY packets to inbox/processed/
RESULT: Thesis NOT YET on the masking Capital One row only; no score, version, vector or prediction moved. The class-wide 50 bp test stays NOT COMPUTABLE, DR-1 PARTIAL (97.4 bp weighted / 22.5 bp best leg, historical proxies). "Capital One-specific" is not "benign": the filing shows part of the rise is post-entry default but cannot size it or separate Discover, mix or programme change; a true JPMorgan default rate is NOT COMPUTABLE, though its crude ratio did rise.
GAPS: Cause of the Capital One move UNKNOWN (filing silent). Citi unread (DEWEY's row, not chased). Whether the April Discover timeline held is UNKNOWN. Figures checked at DEWEY's evidence files and saved 10-Q text, with no fresh SEC pull. Desk boot abridged, skips named above.
WILL_NEEDS: None. No ruling asked; no threshold, gate or trade recommended.
FOLLOW-UP: CARL's next full session drains 10 owed signals, 8 inbox packets, 11 lane signals and COR-20261031-22. DEWEY finishes Citi at its next session once filed.
