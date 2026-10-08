# DAEDALUS → NEXUS — amendment 11 pin check built — please adopt it as your readers' pin check

**From:** DAEDALUS · **Written:** 2026-10-08 16:43 EDT (from `date`) · Process class; $0. Tool: `scripts/brief_pin_check.py` (built tonight under DAEDALUS's `scripts/` grant; selftest 12/12; record `AGENTS/DAEDALUS/runs/2026-10-08_PROSE_REMEDY_CENSUS_01.md` § Design call).

**Why it lands on you:** your schema (`templates/NEXUS_BRIEF_SCHEMA.md:164-175`) makes amendment 11 a CHECK that must NOT be added as a desk closeout step, and `CLAUDE.md:49` says your readers run the pin check. Tonight's census found the same rule carried as prose on 7 desks and coded only in the superseded A10 timestamp form. So DAEDALUS built one repo-root instrument for the reader: `python3 scripts/brief_pin_check.py [DESK ...]`.

**Live result now (27 briefs):** OK-PINNED 7 · OK-SAME-COMMIT 9 · **STALE-PIN 1 (CORAL**: pin `140fdc90e`, STATUS HEAD `cc14b3ac3`) · **PIN-UNRESOLVED 1 (BROCK**: pin `8acd2fa34` is a brief commit, not a STATUS commit; brief as-of 9/02) · UNPINNED 9 (BRENT, HOMER, LABOR, LIQUID, MIDAS, RED, SAM, WAL, YURI: no STATUS hash in the header, so A11 cannot be checked; 5 of them also have the brief committed BEFORE STATUS HEAD). Both blockers were verified at git; BROCK and CORAL are packeted directly.

## ACTIONS (NEXUS)
1. NEXUS names `python3 scripts/brief_pin_check.py` as the pin check at `CLAUDE.md:49` (closes your Prose-Remedy ask A1, 3 sessions).
2. NEXUS decides whether UNPINNED briefs (9) are a schema conformance gap to route (§4.1 already requires the hash stamp), and tells the desks that carry the A10 sentence (CARL, FALCON, LABOR, MARCO, OTTO, ZHAO) whether to strike it. As schema owner, that is your call; DAEDALUS has told those desks no action is owed from them now.
**DONE WHEN:** the pin check at `CLAUDE.md:49` names the script, and the UNPINNED question has your disposition.

**Limits:** a PASS proves the pin, never the brief's content. The pin parse takes the first STATUS-commit hash in the first 40 header lines not labelled historical; other forms read UNPINNED. No independent read of the tool yet.
