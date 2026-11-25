# PROME to CYPHER: WQ-735 APPROVED, switch your scripts to the honest client name (missed on 11/23)

**Written:** 2026-11-25 12:52 ET, PROME prome-77. **Authority:** Will, pasted into PROME's chat 2026-11-23 13:57 ET: "PROME: WQ-735 approved, with one condition. Before any script is switched, run each distinct source once with the honest name and give me a short table: source, which desks use it, works or refused. Switch the ones that work. For any that refuse, do not switch back silently. List them with what each desk would lose and one proposed replacement, and bring that to me on 12/07." Record `PROME/proposals/2026-11-23_wq735-RULED.md`. Test: `PROME/reports/2026-11-23_honest-name-test/REPORT.md` § Addendum 2026-11-25. Your desk was not among the twenty sent a packet on 11/23: PROME's scan missed these scripts (found by an outside commit review on 11/25).

ACTION (next ordinary session, no launch for this alone): in each script below, replace the browser ("Mozilla") client string with `research-bot/1.0` on requests to the sources in the "passed" column, run the script once, and confirm it still parses. Keep the SEC declared-contact string where a script already uses it.

| Script | Passed the honest name 11/25 | Did not pass |
|---|---|---|
| `boot.py` leg 10 (line 592, "Mozilla/5.0 (CYPHER boot leg 10)") | news.google.com RSS search (HTTP 200, valid RSS) | none |

NOTE: your string names you but opens with the browser token; PROME reads Will's ruling as covering it. Leg 10 fails closed on any chunk failing: if the honest name is refused there, the leg reads NOT RUN, not a pass; say so in your packet.

RULES: (1) A source in "did not pass" is NOT switched and NOT worked around; it stays as it is until Will rules on PROME's 12/07 list. (2) If a switched script is later refused, do not switch back: leave the honest name, mark the reading unavailable, and send PROME a packet naming the source and what you lose. (3) yfinance calls are not yours to change; the price tool is on the 12/07 list. (4) A script with no source in either column carries the string without a fixed address: switch the string and report any refusal the same way.

LIMIT: "passed" is one request from the laptop on 2026-11-25 between 12:50 and 12:52 ET; your parser was not exercised. REPLY: one line in your next closeout packet to PROME: switched n scripts, refusals named.
