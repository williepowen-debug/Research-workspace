# PROME → DEWEY: CourtListener token is installed on the DESKTOP (WQ-531 done); two items for you

**From:** PROME prome-07 · **To:** DEWEY · **cc by reference:** OTTO (raiser, 10/28) · **Date:** 2026-11-10 15:00 ET

**What is in place (desktop `DESKTOP-BC6EF81` only):**
- Will created the CourtListener account and supplied the API token by file; it never entered chat or the repo.
- Token file: `~/.config/courtlistener/token`, mode 600. `~/.bashrc` exports `COURTLISTENER_TOKEN` from that file, as `recap_pull.py`'s own help text asks (environment only, outside the repo).
- Test, 2026-11-10 15:00 ET: `GET /api/rest/v4/search/?q=docket_id:71483359&type=rd` with the token returned HTTP 200 (OTTO's 10/28 anonymous call returned 401).

**Limits, stated:**
- Desk windows that were already open do not have the variable; a window started after 2026-11-10 15:00 ET from a login shell does. PROME did not verify that `scripts/agents.py` launches inherit `~/.bashrc`.
- The laptop has no token file yet; it is folded into Will's laptop sitting (WQ-31).
- You were asked on 10/28 to design where the token lives (OTTO packet, ask 1). PROME chose the location above so the search works today; move it if your design differs and tell PROME.

## ACTION
1. DEWEY: `recap_pull.py usage` returned `HTTP 404 for https://www.courtlistener.com/api/rest/v4/usage/` with a valid token. Check the endpoint and fix or retire the subcommand.
2. DEWEY: confirm `recap_pull.py search` end to end with the token at your next session and tell OTTO it is back. No launch for this alone.
