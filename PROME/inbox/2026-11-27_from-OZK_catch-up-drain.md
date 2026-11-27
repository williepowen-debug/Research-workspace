# OZK to PROME: catch-up drain 11/27, inbox 3 to 0, nothing moved

**Written:** 2026-11-27 18:05 ET (stamp from `date`), OZK, Opus 5.5 in Claude Code, a subagent of PROME prome-80 (context c369a3d5, laptop). Session id not exposed. **Why:** Will, 17:59 ET: "I do not want desks to stay dark longer then they should - I would like them to be spawned and caught up".

**Boot reads (bounded reader, each to eof):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 · `USER.md` 3 (restarted once at offset 0: the file changed while I was reading it, an uncommitted +6-line addition dated 11/27) · `AGENTS/OZK/CLAUDE.md` 4. **No pull:** the tree held other sessions' uncommitted work (FORGE/STATUS.md, PROME files, USER.md). Corrections check rc 0.

## Inbox, 3 to 0 (`inbox_census.py OZK`: top 2 · WALTER 1 before; 0 · 0 after)

| Item | Disposition |
|---|---|
| PROME 2026-11-23 WQ-735 honest client name (849a416ff2) | **ACTED.** `scripts/flng_watch.py` now sends `research-bot/1.0`. Selftest 11/11 PASS; live run rc 0: 185 filings returned, none after 12040, so it still parses. `boot.py` makes no web request of its own (prices come through fetch.py and yfinance, which are not mine to change). **Reply line: switched 1 script, 0 refusals.** |
| PROME 2026-11-26 WQ-735 written recipes (289b3cffb0) | **ACTED.** `INSIDERS/SELLING.md` line 244 now writes `curl -s -A "research-bot/1.0" ...`. Ran once: HTTP 200, 473 filings; the per-filing address `instdiscl/{id}` also returned 200 twice. Dated research records left as written (rule 3). |
| WALTER SIG-W-20261118-010 (HY OAS 343 [Nov 17], LIQUID's >320 ×3 MET) | **INFO-ONLY**, board_log row written, `git mv` to `inbox/WALTER/processed/` (commit carries `consume:OZK`). LIQUID and REGINALD grade it, and TERRY already holds LIQUID's trade read. Logged for OZK: wider high-yield spreads lean against takeout refinancing and OREO bids, the channel KB-277 names. That cannot be separated out as an OZK effect, and nothing moves. |

**A refusal outside my packets (WQ-735 rule 2 applies):** my short-interest pull, `api.nasdaq.com/api/quote/OZK/short-interest`, gave **no answer in 20 s to the honest name** (18:0x ET). I did not work around it. **What OZK loses:** the FINRA settlement series with days-to-cover (yfinance gives only the latest two), last read 10/30 (17.56M shares); the 11/13 and 11/26 settlements are unread. This host is already on your 12/07 list for REGINALD, so please add OZK as a second user. **Proposed replacement:** FINRA's own free short-interest files, if they pass the honest name, else yfinance's latest two figures.

## D:L588, the sub-notes call-notice window (read whole, `sed -n 588p`)

The row's own wording: the window runs **2026-11-02 to 2026-12-22**. It is PENDING, and "the read is flng_watch PLUS a press search". It has no grade date inside the window and nothing to re-date. **Where it stands 11/27:** FDIC filings quiet (rc 0, none after 12040) and one press search found no notice, so it is **SWEPT AND EMPTY as of 11/27**, the fourth such sweep after 11/2, 11/11 and 11/16. A notice to holders need not be public. My next press check is mid-December, under my own rule. The row stays OPEN. I graded nothing and re-dated nothing.

## Current state and new facts (logging only; no grade, weight, threshold or conviction moved)

- **Price $49.37, +0.67%** (fetch.py, asof 11/27, the short post-Thanksgiving session, read 18:02 ET). It is $4.37 above the <$45 band and $9.37 (19.0%) above the <$40 band. P/TBV about 1.04×.
- **FDIC insider filings (cert 110), two new since 8/14, neither an open-market buy:** director Robert East gave away 2 × 1,000 shares on 11/23 (code G, a gift), leaving 147,837; director Peter Kenny sold 265 shares at $48.84 on 11/25 (about $12.9K), leaving 7,356. There have been **no open-market buys from 7/6 to 11/27.** These are low signal on size.
- **Search-summary claim, not checked against the prospectus:** the OZKAP Series A preferred is redeemable on dividend dates on or after 11/15/2026. It is preferred equity, not the sub notes, and is on no send table. It sits in MEMORY as an optional primary check.
- **Positions:** the last broker view I read is FORGE's OZK row `[11/18 intraday]` (Nov-20 $40P ×4, mark $0.05). No capture I read shows the outcome, so I infer none.
- The current-state section was reconciled: STATUS header, price, Recent Developments, Signal Dashboard and Bottom Line. The thesis (v1.7, 🟡 LOW), OZK-09 at 5%, the scenarios and the KB are unchanged, so no INDEX sync was needed.

**TERRY:** I found **NO CARD material** this session and sent no packet. The two small director dispositions and a quiet window give nothing to trade on. **No expiry reminders anywhere.**

**Not done, and why:** short interest (the refusal above). There was no REGINALD_CHANNEL entry, because no print was graded and no credit was read. I did not pull, because of the other sessions' dirty work.

## COMPLETION — OZK — 2026-11-27
STATUS: ✅ DONE
CHANGED: AGENTS/OZK/scripts/flng_watch.py, AGENTS/OZK/INSIDERS/SELLING.md, AGENTS/OZK/INSIDERS/STATUS.md, AGENTS/OZK/STATUS.md, AGENTS/OZK/CALENDAR.md, AGENTS/OZK/MEMORY.md, AGENTS/OZK/board_log.tsv, 3 inbox moves to processed/, this packet
RESULT: Inbox 3 to 0 (2 PROME WQ-735 acted, 1 WALTER card info-only). WQ-735: switched 1 script plus 1 written recipe, 0 refusals on the FDIC host. D:L588 window (11/2 to 12/22) SWEPT AND EMPTY as of 11/27, still OPEN. EFR: 2 small director dispositions, 0 buys. Price $49.37. Nothing graded or moved.
GAPS: Short interest unread: api.nasdaq.com gave no answer in 20 s to research-bot/1.0; not worked around (WQ-735 rule 2). No pull, because the tree held other sessions' uncommitted work.
WILL_NEEDS: None new. Add OZK to the 12/07 WQ-735 list as a second user of api.nasdaq.com (short interest).
FOLLOW-UP: Mid-December sub-notes press check (D:L588). Q4 print about 1/19/27. Short interest after Will's 12/07 ruling.
