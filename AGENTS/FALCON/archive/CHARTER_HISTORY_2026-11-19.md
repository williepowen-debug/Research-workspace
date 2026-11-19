# FALCON charter history — moved out verbatim 2026-11-19
**Why:** WQ-701 A2 (Will 2026-11-16 22:07 ET, verbatim "okay go ahead with your recommendations"; root CLAUDE.md § Data Hygiene: a desk charter's ceiling is 50,000 B, met by moving history out, never by compressing what remains). Relayed by PROME packet `inbox/processed/2026-11-16_from-PROME_WQ-701-A2-charter-ceiling-trim.md`.
**What:** each section below is a passage cut from `AGENTS/FALCON/CLAUDE.md` byte for byte (between the BEGIN and END lines); the charter carries `[H<n>]` where it stood. No rule, threshold, level, operator, instrument, route or authority was changed by the move. Prior full charter: `git show HEAD~1:AGENTS/FALCON/CLAUDE.md` at the trim commit.

## H1 — Boot step 5a-2 (war-risk carry staleness): build-time verification

----- BEGIN H1 -----
**Verified working at build time:** at `--days 4` against 5-day-old data it printed `⚠️ STALE +5d`, confirming the content clock drives the alert rather than the file's mtime.
----- END H1 -----

## H2 — Boot step 3b (MEMORY.md): why the step was added

----- BEGIN H2 -----
⚠️ **ADDED 2026-09-14 BECAUSE ITS ABSENCE WAS THE DEFECT.** This file held durable findings and **was not boot-read by any step**, so a lesson written here was written into a surface nobody opened. PROME caught it at the 9/14 closeout: the self-pointer guard had been written to a SCRATCH bullet, a commit body and a session message — **none of which is read at boot** — and the session was called closed.
----- END H2 -----

## H3 — Boot step 5a-3 (WARRISK per-row expiry): the day-of-build measurement

----- BEGIN H3 -----
Measured on the day it was built: **all five rows were 7 days past their own `Stale_By`, and three legs — including `West Coast Saudi 0.1%`, the row the file itself labels `🎯 REGISTERED FALSIFIER` and "the cheapest early warning on the whole board" — had not been refreshed in 18 days**, silently, behind a file gate that looked green because the headline Hormuz leg was being attended to.
----- END H3 -----

## H4 — Boot step 5b-2 (Hormuz transit): the superseded level-cross rule and why it was retired

----- BEGIN H4 -----
⚠️ **SUPERSEDED, preserved so the reason travels: the old rule was `rc 1 = new print(s) at/below the 18/day fresh-leg bar`. It was retired because the series moved an order of magnitude past it** — prints now run 2-6/day total, so **every** print sat at-or-below 18 and the alarm would have fired on **every observation**. An alarm that cannot fail to fire carries no information; worse, **18 is the boundary of the LEAKING/recovery band**, so it nominally flagged the condition I would read as improvement while the deterioration band (`<10`) had no trigger at all.
----- END H4 -----

## H5 — Boot step 5b-4 (Kharg loadings): historical description of the retired veto

----- BEGIN H5 -----
Historical description follows, retained so the reasoning travels: IMF PortWatch port2164 `export_tanker` (AIS-est) — was the GATE-TERRY-006 Kharg-strand **refuting veto, NOT a numeric trigger** (source is AIS-blind to Iran's dark fleet → prints literal 0 for whole NORMAL months; `domain/KHARG_LOADINGS_SOURCE.md`). **INVERTED codes:** rc 1 = nonzero loadings in trailing-14d = flow CONTINUING → REFUTES a Kharg strand, gate must NOT fire on strand grounds; rc 0 = quiet = UNINFORMATIVE (blind source, silence proves nothing — do NOT read as a strand). rc 2 = fetch failure. The gate FIRES only on a dark-fleet-capable corroborator (official export-suspension naming Kharg / Kpler-Vortexa collapse / Kharg-specific war-risk notice) — this script can only veto, never fire. *(Built 2026-07-18 wave-1, GATE-TERRY-006 unblock.)*
----- END H5 -----

## H6 — Boot step 6c (WALTER lane): the 2026-09-14 duplicate check

----- BEGIN H6 -----
✅ **Checked 2026-09-14: `cut -f2 board_log.tsv | sort | uniq -d` returned EMPTY across 133 rows — zero duplicates; the mechanism is real and had NOT manifested here.**
----- END H6 -----

## H7 — Closeout step 14 (NEXUS_BRIEF): the 7/31 audit note

----- BEGIN H7 -----
*(The 7/31 fleet audit found 5-of-5 content-stale briefs had REFRESHED and then kept working — only the ordering constraint closes that mechanism.)*
----- END H7 -----

## H8 — Git section: build-phase note

----- BEGIN H8 -----
**Build-phase note:** this scaffold was committed by DAEDALUS per build spec `AGENTS/DAEDALUS/builds/OSPREY_FALCON_BUILD.md` §7 (DAEDALUS AUTHORITY — new-agent wiring requires explicit Will/PROME approval, granted 2026-07-12); FALCON's own auto-push regime starts at its first live session.
----- END H8 -----

## H9 — FILES, workbook/KB.tsv: drift note

----- BEGIN H9 -----
*(DAEDALUS 8/15 action #9: this cell read "66 rows thru 7/30" while the file held 95+, a boot-loaded pointer drifting against a maintained value. Fixed 2026-08-20 by pointing at the resolution rule instead of a number — the same class DAEDALUS flagged for the ANALYSIS pointer.)*
----- END H9 -----

## H10 — FILES, STRIKES.tsv: drift note and backfill history

----- BEGIN H10 -----
; this cell read "31 rows thru 7/30" while the file held 39 thru 9/8 — same drift class as the KB cell, fixed the same way 2026-09-08
----- END H10 -----

## H11 — FILES, STRIKES.tsv: backfill history

----- BEGIN H11 -----
✅ **The founding-mandate backfill is DONE** (executed 7/12, Feb-28→Jul-12) and the data-conflict resolution pass closed 7/27 (30→31 rows, 5 of 6 dates pinned).
----- END H11 -----

## H12 — FILES, ANALYSIS: drift note

----- BEGIN H12 -----
 (this cell said 7/27 was live while 8/06 and then 9/08 existed)
----- END H12 -----

## H13 — FILES, HAWK legacy scripts: execution evidence of 7/27

----- BEGIN H13 -----
**The spec said they'd *look* authoritative; executing them showed worse — all five exit `rc=0` and print confidently WRONG output** (`War Day 148/51`, `D 82/C 12/B 6`, `Yanbu OPERATIONAL`, hardcoded shadow-fleet metrics as live readings, and `war_monitor`'s **false-quiet** "no significant developments" on the Jazan week). Rejected on scope (`thresholds.py` = BRENT's lane *and* it encodes the price→scenario inference **Jun 11 falsified**; `sanctions_tracker.py` = HAWK's synthesis lane), supersession (`oil_infrastructure.py` ≪ `STRIKES.tsv`), and missing input (`catalyst_countdown.py` reads an unmigrated `CALENDAR.md`).
----- END H13 -----

## H14 — FILES, HAWK legacy scripts: 7/27 flag to HAWK

----- BEGIN H14 -----
*(Historical, 7/27: flagged to HAWK that its `boot.py` invoked all five. HAWK's `boot.py` header now reads FROZEN / not wired; `HAWK/CLAUDE.md` names `derived_freshness.py` as the sole live checker. HAWK's files — flagged, not edited.)*
----- END H14 -----
