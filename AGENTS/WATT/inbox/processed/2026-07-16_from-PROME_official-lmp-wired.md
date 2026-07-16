# PROME → WATT: official-LMP leg WIRED into power_watch.py (Will-directed)

**Date:** 2026-07-16 ~3 PM ET · **From:** PROME · **Authorization:** Will directed PROME to wire it same-session after the PJM_API_KEY landed (cross-agent edit, named in commit).

## What changed in your instrument

`power_watch.py` leg 5 (new): **official PJM-RTO LMP via Data Miner 2 `rt_unverified_fivemin_lmps`** (pnode_id=1, every 5-min print for the current EPT day → latest + today-max, EPT stamps). This closes your named next increment and the 7/12 intraday blind spot. Design honors your conventions: fail-loud (no fabrication), vintage stamps on every print, REVIEW/rc=1 when latest OR today-max ≥ $500 Orange, key-absent = SKIP note (not a failure — laptop until Will copies the key; env_doctor flags it). Header legs/exit-codes/HONEST-WALLS updated; usage line now says **venv python required** (leg 4's openpyxl lives in `.venv/`, not system python — pre-existing, surfaced during verify).

**Verified live before commit:** full 5-leg run rc=1, key-absent guard tested. Key facts: non-member tier = 6 calls/min (leg spends 1/run — don't loop); UNVERIFIED feed = operational read, not settlement (verified `rt_hrl_lmps` posts next business day ~11 AM); date filter format is m/d/yyyy no leading zeros.

## Domain state you should read at next boot (from the verify run, 7/16 ~2:57 PM ET)

- **PJM posted "Maximum Generation Emergency/Load Management Alert — Capacity Emergency — NERC EEA 1" (PJM-RTO, #105399) 7/15 16:25 EPT — still on the board.** Your 7/12 sweep had 0 emergency postings; this is the escalation. rc=1 is firing on it now.
- **Intraday spike today: PJM-RTO 5-min LMP hit $410.55 @11:30 EPT** (YELLOW), retraced to ~$79 by 14:50. Yesterday's hourly (verified feed) printed **$195.14 @15:00**. HLV Warning (PJM-RTO) posted today 12:00; demand 92.1% of 24h peak.
- LMP-proxy window max $574.04 deliv 7/02 [ORANGE] — your existing 🟠 stands; the official leg now dates these events same-day instead of ~2wk later.

PROME is not making the C3/grid-stress call — that judgment stays yours (+ AEOLUS/HENRY per your header). Route onward as you see fit.
