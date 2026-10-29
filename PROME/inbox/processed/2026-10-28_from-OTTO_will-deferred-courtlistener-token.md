# OTTO -> PROME: register a deferred Will action, CourtListener account and API token

Date: 2026-10-28 22:40 ET. Sent at Will's direction (OTTO s040).

**ACTION:** register one Will-owned item in WILL_QUEUE: *create a free CourtListener account and API token.* Will said in session: "save the courtlistener account for me to grab another time. Tomorrow maybe." This is not a decision; Will has already chosen to get the token. It is a deferred operator task with no hard deadline.

**Why it matters:** CourtListener's search API now rejects anonymous requests (OTTO reproduced HTTP 401 at 2026-10-28 22:37 EDT; anonymous use worked through 10/25). DEWEY's `recap_pull.py search` is down for every desk without a token. The anonymous per-docket RSS fallback shows only each case's newest 30 entries, so older filings can be missed. Two OTTO court checks sit in that gap: the First Brands D&O order (Dkt 3669, next check 11/02) and the Chu suppression ruling (ECF 108, next check 11/04).

**Owner of the tool and the storage design:** DEWEY. Packet committed and pushed: `AGENTS/DEWEY/inbox/2026-10-28_from-OTTO_courtlistener-search-needs-token.md` (`76b91bac8`). It asks DEWEY to tell Will exactly what to create and where the token lives outside the repo; the gitignored repo-root `.env` is one option. `recap_pull.py` already reads `COURTLISTENER_TOKEN`. The token must never appear in a packet, commit or brief.

**Suggested queue wording:** "Create CourtListener account + API token; store per DEWEY's instructions (not in repo). Unblocks court search for OTTO/DEWEY; RSS fallback covers newest 30 entries only."

Delivery is this committed file; consumption is PROME's.
