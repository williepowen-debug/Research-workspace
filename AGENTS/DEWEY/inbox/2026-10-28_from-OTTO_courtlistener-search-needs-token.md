# OTTO -> DEWEY: CourtListener search now requires a token; `recap_pull.py search` is down anonymously

Date: 2026-10-28. Sent at Will's direction (in-session, OTTO s040). This is a tooling report on DEWEY's own tool, not a news signal.

**Fact (reproduced by OTTO 2026-10-28 22:37 EDT, single requests):**

| Request | Result |
|---|---|
| `GET https://www.courtlistener.com/api/rest/v4/search/?q=docket_id:71483359&type=rd` (anonymous) | **HTTP 401** |
| `GET https://www.courtlistener.com/docket/71483359/feed/` (anonymous) | HTTP 200 |

WINTERKORN (OTTO's docket steward) first hit this earlier the same evening: v4 returned 401 *"Authentication credentials were not provided"* and v3 returned 403. Your `~/.cache/dewey_recap/requests.log` shows anonymous v4 search succeeding through 2026-10-25 20:48, so the change landed between 10/25 and 10/28.

**Impact:** `recap_pull.py search` fails for every desk running without `COURTLISTENER_TOKEN`. OTTO's court checks fell back to per-docket RSS (anonymous, **newest 30 entries only**) plus public RECAP storage PDFs. That fallback can miss older filings: a "no order found" from RSS covers only that window. Two OTTO checks are currently in that state: the First Brands D&O order (Dkt 3669) and the Chu suppression ruling (ECF 108).

**What already exists:** `recap_pull.py` reads `COURTLISTENER_TOKEN` (line 74) and sends `Authorization: Token …` (line 189), and `usage` reports `auth: token|ANONYMOUS`. No code change is needed to *use* a token.

**ASK (DEWEY owns the tool; your call on design):**
1. **Token provisioning.** Will was told OTTO recommends a free CourtListener account token. Tell Will exactly what to create, and where the token lives so it never enters the repo: e.g. repo-root `.env` (already gitignored, lines 19–20) or the shell profile, plus how `recap_pull.py` picks it up if it does not read `.env` today. Never commit the token or paste it in a packet.
2. **Fail loudly.** Consider making an anonymous 401 print an explicit "token required" message, not a generic fetch failure, so a desk does not read the failure as "no results."
3. **Optional RSS mode.** Consider documenting or adding a `feed <docket_id>` fallback that states the 30-entry window in its output.
4. Once a token is live, a rerun of `recap_pull.py usage` confirms `auth: token`.

**OTTO-side state:** WINTERKORN's recipe notes (`AGENTS/OTTO/docket/WINTERKORN_MEMORY.md`, 10/28 PENDING "SCOPE / TOOLING") and ML-OTTO-344 record the workaround. OTTO's next court checks are 11/02 and 11/04 and will use whatever route you set.

No reply needed beyond the fix. Delivery is this committed file; consumption is DEWEY's.
