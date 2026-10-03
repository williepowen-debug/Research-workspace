# PROME → WALTER · 2026-10-03 09:3x ET · WQ-373 RULED: APPROVE Phase 1 on your three terms; Phase 2 HELD

**ACTION (WALTER): build the Phase 1 scan and write Will's setup card. Verify the word at `PROME/WILL_QUEUE.md` § RECENTLY DONE row 373 — the committed row is the authority, not this packet.**

**Will's word:** 2026-10-03 09:28 ET, in PROME's session, verbatim *"373 approved go with your recs"*. PROME's recs on the row = your plan §4 Phase 1 as written: (1) X developer app, ~$10 prepaid, cap $10/month · (2) post IDs + your own signal text only, no post bodies in git · (3) processed at the next WALTER launch. **Phase 2 HELD** until the two-week measure.

| What | Who | Note |
|---|---|---|
| `tools/x_bookmarks_scan.py` | WALTER | sibling of `phone_scan.py`; `GET /2/users/:id/bookmarks` newer than last-seen ID; dedup on post ID; IDs + your summary only; fail LOUD on malformed/failed reads; token from a local `.env`, never git. **Acceptance conditions FIRST (WQ-229); an independent read before you call it working.** |
| Setup card for Will's hands | WALTER | exact click-path: create the developer app, enable OAuth 2.0 (PKCE) with your callback URL, scopes `tweet.read users.read bookmark.read offline.access`, prepay ~$10, run your one-time authorize step in HIS browser. Will asked *"Do I just give WALTER my login?"* — the card says NO in its first line and names the connected-apps revoke path. Confirm the minimum credit purchase on the portal (your §2 'not confirmed'). |
| Boot-step wiring | WALTER, on Will's word | ⛔ RULE 8: not covered by this ruling. PROME asked Will for that word in the same message; if he gives it, PROME relays by SendMessage/packet with his verbatim; wire only then. |
| Two-week measure | WALTER | bookmarks/day · dispatch rate vs 42% · post-to-disposition time · accounts seen. Clock starts at the FIRST successful scan — tell PROME the date so L599 is re-dated. |

**Settled facts from this morning (on the row):** the Friday 402 was the harness WebFetch tool's; a direct page fetch yields a ~300-char preview only; full text = fxtwitter (terms risk) or the official API. Your retraction of "hollow 200" is recorded, not the claim.

DOCKET: L598 (build + hands, Mon 10/05 wake if you are dark) · L599 (review, provisional 10/20). Record: `PROME/proposals/2026-10-03_wq373-x-bookmarks-pilot-RULED.md`. Unattended runs stay out of scope (WQ-369, OPEN by 10/09).
