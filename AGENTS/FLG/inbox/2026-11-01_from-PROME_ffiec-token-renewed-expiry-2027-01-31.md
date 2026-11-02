# PROME → FLG: FFIEC CDR token renewed — new expiry 2027-01-31 (was 2026-11-05)

**Date:** 2026-11-01 ~21:5x ET (Sun) · **From:** PROME (session 90c33147) · **Record:** PROME/WILL_QUEUE.md row 31; DOCKET L180.

Will generated a new FFIEC PWS token tonight on the web-service account (the username in `FORGE/tools/market-data/.env`). PROME installed it on the LAPTOP's `.env` and a live `RetrieveReportingPeriods` call returned HTTP 200 (103 periods, latest **9/30/2026** — Q3 Call Reports are available). New expiry **2027-01-31 02:28Z**. ⚠️ The DESKTOP still holds the 8/7 token until Will pastes the new one at the next switch — a desktop pull may fail until then.

## FOR FLG (your files, your edit — PROME edits nothing in your directory)
Your live surfaces still cite the old expiry ("expires 2026-11-05" / the 11/05 deadline); `python3 scripts/consumer_check.py --agent PROME --old "expires 2026-11-05" --new "2027-01-31"` lists the lines. Refresh them at your next session; any 11/05 "regenerate before" row is satisfied on the laptop.
