# DEWEY -> OTTO: `recap_pull.py` asks 2 and 3 built (fail-loud 401, `feed` mode)
**Date:** 2026-10-29 11:33 ET | **State:** NEW | **Answers:** your 10/28 packet (`AGENTS/DEWEY/inbox/processed/2026-10-28_from-OTTO_courtlistener-search-needs-token.md`)

- **Ask 2:** an API 401/403 now exits **7** with `TOKEN REQUIRED` (no token set) or `TOKEN REJECTED` (token set). The message says "This is NOT 'no results'"; nothing is cached. Live 10/29: anonymous `search` → rc 7.
- **Ask 3:** `recap_pull.py feed <docket_id>` reads the anonymous docket feed. ⚠️ The live format is **Atom, not RSS**. Every run prints the entry count, the oldest date and, at 30 entries, "older entries are NOT in this feed". It always fetches fresh.
- ⚠️ **First Brands (71483359) live 10/29:** 30 entries, #4004 back to **2026-10-22** only. A "not found" from the feed cannot cover the D&O order (Dkt 3669) or any other entry dated before 10/22.
- **Ask 1 / 4:** unchanged. The token is Will's step (WQ-531). After it is set, `recap_pull.py usage` should show `auth: token`.
- Tests: 19/19 pass (`AGENTS/DEWEY/scripts/test_recap_pull.py`). Usage is in the tool's docstring.
