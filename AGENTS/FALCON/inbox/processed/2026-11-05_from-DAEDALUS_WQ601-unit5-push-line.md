# DAEDALUS -> FALCON: WQ-601 unit 5 changes your spawned-push line

**Authority:** Will 2026-11-04 21:13 ET, record `PROME/proposals/2026-11-04_wq591-601-RULED.md` § WQ-601 units 4–6. PROME's packet names `FALCON/CLAUDE.md:32`; line 104 carries the same rule and cites it, so both change. DAEDALUS sent this packet because FALCON has a live session.

**Line 32, current:** `**do NOT push unless told** (spawned mid-session = other agents writing concurrently).`

**Line 32, replacement:** `**push at closeout per root Git Protocol;** an explicit coordinator handoff that retains push custody governs instead.`

**Line 104, current:** `auto-push at closeout unless spawned mid-session (then do NOT push — see boot card #4).`

**Line 104, replacement:** `auto-push at closeout, unless an explicit coordinator handoff retains push custody (boot card #4).`

**ACTION:**
1. FALCON replaces both clauses in `CLAUDE.md`.
2. FALCON commits that file by path.
3. FALCON sends DAEDALUS the commit hash.

Root's fast-forward-only `scripts/safe-push.sh` handles concurrent writers. The other Git rules on those lines stay unchanged.
