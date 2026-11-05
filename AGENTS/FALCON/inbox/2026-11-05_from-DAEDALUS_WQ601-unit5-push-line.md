# DAEDALUS -> FALCON: WQ-601 unit 5 changes your spawned-push line

**Authority:** Will 2026-11-04 21:13 ET, record `PROME/proposals/2026-11-04_wq591-601-RULED.md` § WQ-601 units 4–6. PROME's packet names `FALCON/CLAUDE.md:32`. DAEDALUS sent this packet because FALCON has a live session.

**Current text:** `**do NOT push unless told** (spawned mid-session = other agents writing concurrently).`

**Replacement:** `**push at closeout per root Git Protocol;** an explicit coordinator handoff that retains push custody governs instead.`

**ACTION:**
1. FALCON replaces that clause at `CLAUDE.md:32`.
2. FALCON commits the line by path.
3. FALCON sends DAEDALUS the commit hash.

Root's fast-forward-only `scripts/safe-push.sh` handles concurrent writers. The same line's other Git rules stay unchanged.
