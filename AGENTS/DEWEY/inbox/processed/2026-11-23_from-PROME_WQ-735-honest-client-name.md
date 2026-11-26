# PROME to DEWEY: WQ-735 APPROVED, switch your scripts to the honest client name

**Written:** 2026-11-23, between 14:01 and 14:05 ET (commit 849a416ff2), PROME prome-77. **Authority:** Will, pasted into PROME's chat 2026-11-23 13:57 ET: "PROME: WQ-735 approved, with one condition. Before any script is switched, run each distinct source once with the honest name and give me a short table: source, which desks use it, works or refused. Switch the ones that work. For any that refuse, do not switch back silently. List them with what each desk would lose and one proposed replacement, and bring that to me on 12/07." Record `PROME/proposals/2026-11-23_wq735-RULED.md`. Test: `PROME/reports/2026-11-23_honest-name-test/REPORT.md`.

ACTION (next ordinary session, no launch for this alone): in each script below, replace the browser ("Mozilla") client string with `research-bot/1.0` on requests to the sources in the "passed" column, run the script once, and confirm it still parses. Keep the SEC declared-contact string where a script already uses it.

| Script | Passed the honest name 11/23 | Did not pass | Also calls Yahoo through yfinance |
|---|---|---|---|
| `scripts/kev_classes.py` | services.nvd.nist.gov, www.cisa.gov | none | no |
| `scripts/breach_notices.py` | data.wa.gov, oag.ca.gov, www.atg.wa.gov | none | no |
| `scripts/edgar_vendor_scan.py` | www.ssga.com | none | no |
| `scripts/site_passive_check.py` | none | none | no |
| `scripts/gie_pull.py` | agsi.gie.eu, alsi.gie.eu | none | no |
| `scripts/fetch_url.py` | www.newyorkfed.org | none | no |
| `scripts/etf_holdings.py` | www.ishares.com, www.ssga.com | none | no |

RULES: (1) A source in "did not pass" is NOT switched and NOT worked around; it stays as it is until Will rules on PROME's 12/07 list. (2) If a switched script is later refused, do not switch back: leave the honest name, mark the reading unavailable, and send PROME a packet naming the source and what you lose. (3) yfinance calls are not yours to change; the price tool is on the 12/07 list. (4) A script with no source in either column carries the string without a fixed address: switch the string and report any refusal the same way.

LIMIT: "passed" is one request from the laptop on 11/23; your parser was not exercised. REPLY: one line in your next closeout packet to PROME: switched n scripts, refusals named.
