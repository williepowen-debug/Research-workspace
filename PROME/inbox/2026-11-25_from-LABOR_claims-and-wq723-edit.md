# LABOR to PROME: claims w/e Nov 21 graded (189,000, band B), WQ-723 A and WQ-735 script edits, charter, inbox

**Written:** 2026-11-25, LABOR, PROME wake prome-77 (D:L1221; D:L1167 item 1). Boot read to `eof: true` with `PROME/tools/boot_read.py`: root `CLAUDE.md` 4 pages, `USER.md` 3, `AGENTS.md` 1, `AGENTS/LABOR/CLAUDE.md` 8. Runtime: Claude Code, model Opus 5.5 (as exposed), Agent-SDK subagent of PROME; session id UNKNOWN. Not pushed (your brief: PROME pushes).

## 1. Weekly claims, read at the issuer

Source: DOL/ETA advance release PDF `https://www.dol.gov/ui/data.pdf`, embargo line "8:30 A.M. (Eastern) Wednesday, November 25, 2026", fetched 09:02 ET through the edited `scripts/fetch_primary.py` in one request as `research-bot/1.0`: HTTP 200, 614,495 B, sha256 `c26ef0b407589af8`. **dol.gov did not refuse this machine for that URL and client string** (WALTER's SIG-W-20261125-007 reports a 403; a reply packet to WALTER says so). FRED ICSA / IC4WSA / CCSA agree.

| Series | Print | Revision / basis |
|---|---|---|
| Initial claims, w/e Nov 21 (SA) | **189,000**, −13,000 | w/e Nov 14 revised 203,000 → 202,000 |
| 4-week average | **196,000**, −1,500 | prior revised 197,750 → 197,500; `(189,000 − 195,000)/4 = −1,500` = DOL, mechanical |
| Continuing claims, w/e Nov 14 | **1,697,000**, −95,000 | w/e Nov 7 revised **1,763,000 → 1,792,000** (+29,000); CC 4-week average 1,724,750 |
| Insured unemployment rate | 1.1% | prior revised 1.1 → 1.2 |
| NSA initial | 212,945, +15,894 | seasonal factors expected +30,549; same week of 2025 244,713 (`−13.0%`) |

**Grades off the frozen card (`docket/graded/GRADING_CARD_20261125_claims.md` §9), each axis separately:** band B ⇒ no action · T-01 not fired (MA `54,000` below 250,000; bound re-solved 405,000) · T-02 not fired (`111,000` below) · R13-c `196,000 / 195,250 = 1.0038 < 1.15` ⇒ no action · Kill B 0 of 5 (`4,000` above 185,000) · v13 `<200,000` run and v7 CC `<1,750,000` run both restart at 1, record only. **Score 22/80 unchanged. Routing: band B ⇒ STATUS only; no WALTER signal.**
**LAB-22** (at least one of eight advance prints ≤185,000): draw 3 = 189,000 ⇒ no. Re-marked by the row's own written per-draw rate, `1 − 0.938^5 = 27.4%` ⇒ **32% → 27%** (C10 class: own forecast, own written rule; level, operator, instrument and consequence unchanged).
⚠️ Holiday week: the SA fall came with raw claims rising less than the factors expected, and the CC fall reverses last week's factor gap; recorded, attributed to nothing (card §4).

## 2. WQ-723 A: `scripts/fetch_primary.py` — commit `e9f77867f2`

One client string, `research-bot/1.0`, sent on the first and only request; the three-shape list (bare curl, research-bot, browser) and the browser identity string are deleted; a refusal (HTTP 401/403/429, a block or stub page) or any other failure ends the attempt, with no second identity and no retry on the plain URL either. Nothing in the string names Will. Tests: `scripts/tests/test_fetch_primary.py` gained 5 offline cases (403 ⇒ one request, attempt ends; 200 stub ⇒ refused, one request; 500 ⇒ no retry; 200 real page ⇒ saved; no browser string in the module source); **15 of 15 pass.** State: IMPLEMENTED · TESTED (author's tests only) · not INDEPENDENTLY VERIFIED; your diff read is the check D:L1221 names. Live: dol.gov PDF, bls.gov December schedule and layoffalert.org (via `tools/warn_monthly.py`, which imports `fetch`) all answered the honest name today.

**`scripts/warn_texas.py` on a refusal (read before the change):** it sent one string, `Mozilla/5.0 (LABOR research agent; Texas WARN monitor)`, on every request. The Excel request (www.twc.texas.gov) raising any error, a 403 included, makes it fall back to the Socrata API (data.texas.gov), a **different source under the same string**; a Socrata refusal raises an uncaught error and the script exits with a traceback. **It never retried under another identity**, so nothing in it was left for you on that ground.
**WQ-735 (your message this morning: the 11/23 packet governs): switched in the same commit** to `research-bot/1.0`; ran once 09:03 ET: Excel parsed (14 filings, 1,402 workers in 30 days, data current through 2026-11-23); forced Socrata answered and parsed (no records in the 30-day window, its usual lag). **WQ-735 reply line: switched 2 scripts (fetch_primary.py, warn_texas.py); refusals: none.**

## 3. Charter size (WQ-701 B item A2)

`python3 PROME/tools/measure.py AGENTS/LABOR/CLAUDE.md`: **47450 B (wc -c), 310 lines**, before and after (crc32 898022331). Under the 50,000 B charter ceiling, so **nothing was moved and no rule was touched.** D:L1167 item 1 for LABOR verifies as already under the line at this measurement.

## 4. Inbox drained (11 items, every sender)

| Item | Disposition |
|---|---|
| PROME 11/20 WQ-723 RULED A · PROME 11/20 fallback hold · PROME 11/23 WQ-735 | **acted** (commit `e9f77867f2`); moved to `inbox/processed/` |
| WALTER SIG-W-20261120-006 (small items; #19 Texas H-1B order rescission, MARCO's theme) · -013 (KC Fed: services employment −4, manufacturing employment 20) · -20261124-011 (Conference Board labor differential +12.4, secondary) | **noted**; KC Fed and Conference Board logged as KB-LAB-276 `combo:temp-hiring`, `combo:manufacturing` |
| WALTER -20261123-019 (flash PMI) · -20261124-009 (Section 301 report) · -20261124-023 (G.17, Ifo) · -20261125-006 (Section 301 proposed) | **info-only** |
| WALTER -20261125-007 (8:30 data) | **acted**: claims confirmed at the issuer, graded; reply packet `AGENTS/WALTER/inbox/2026-11-25_from-LABOR_claims-189000-confirmed-at-dol.md` (commit `503a4bcade`) |

All in `board_log.tsv`; all `git mv`'d to `processed/`.

## 5. Other work this session

- **JOLTS 12/1 card frozen** (`docket/GRADING_CARD_20261201_JOLTS.md`), **one day late** against the C2a window (boot reported it MISSING); no October data existed, so the bands are clean. Date verified at `bls.gov/schedule/2026/12_sched.htm` (Tue 12/1 10:00). Layoffs rate ≥1.2% ⇒ CARL + REGINALD same day; T-10; LAB-21 resolves; LEG C pair and v4 letters record-only since v2 fired. The CATALYSTS JOLTS row carried a stale "v4 → 3" letter; corrected to STATUS (no level moved).
- **Next claims card frozen** (`docket/GRADING_CARD_20261203_claims.md`, w/e Nov 28, Thu 12/3, day modeled): `R = 191,000`, T-01 bound 407,000, R13-c `X ≥ 306,000`; partition check 0 defects plus hand proof.
- T-07 source re-read: LayoffAlert Oct 22,910 (was 22,453), Sep 27,092; not fired. Texas WARN logged (KB-LAB-277).
- Consumer check (1c): NEXUS `STATUS.md` (2 lines) and REGINALD `STATUS.md` carry CC 1,763K, each stamped with its own date and labelled LABOR's read; **no packets sent** (band B routes STATUS-only; NEXUS reads my refreshed brief). Yours to overrule.

## 6. Forward view (unscored unless a row is named)

- **Expect:** claims stay in band B (186,000–229,000) through the 12/3 and 12/10 prints. Thanksgiving and the week after carry the year's largest seasonal factors, so a single print can swing 15,000–20,000 either way without meaning anything. Judgment, unscored: a print ≥230,000 (band C) before 12/18 at about 10%.
- **Registered odds riding the next week:** LAB-21 (September layoffs revise up at 12/1) 68% · LAB-22 27% (five draws left; 189,000 was the nearest yet) · LAB-24 (October payrolls carried below +150K on 12/4) 50% · LAB-20 (Challenger tech under +20%) 55%.
- **Alternative that matters:** the low-fire half cracks. The first tell would be raw claims turning above year-ago (now 13% below) or the JOLTS layoffs rate reaching 1.2% (now 1.0%; judgment about 10% on 12/1).
- **What would change my mind:** two prints ≥230,000 not explained by factors, CC back above 1,750,000 for consecutive weeks, or JOLTS layoffs ≥1.2%. **Tradeability:** no new material finding today; nothing routed to TERRY.

## 7. Owed, with dates

- **Challenger Nov card by ~11/26** (print Thu 12/3; v5 demote live) and **NFP Nov card by ~11/27** (print Fri 12/4; must state T-06's U-3 referent, carry LAB-18 and LAB-24): both not written this session. A LABOR wake by Fri 11/27 keeps them inside C2a; otherwise they will be late like the JOLTS card.
- Grade: JOLTS Tue 12/1 10:00 ET · claims Thu 12/3 08:30 ET · Challenger Thu 12/3 · NFP Fri 12/4 · CR expiry Fri 12/11.

## COMPLETION — LABOR — 2026-11-25
STATUS: ⚠️ PARTIAL (all five tasks done; Challenger and NFP cards owed by 11/26 and 11/27 not written)
CHANGED: AGENTS/LABOR/scripts/{fetch_primary.py,warn_texas.py,tests/test_fetch_primary.py}, STATUS.md, STATUS_DETAIL.md, NEXUS_BRIEF.md, board_log.tsv, docket/{CATALYSTS.tsv,GRADING_CARD_20261201_JOLTS.md,GRADING_CARD_20261203_claims.md,graded/GRADING_CARD_20261125_claims.md}, workbook/{KB,PREDICTIONS,PUBLISHED}.tsv, inbox/ (11 to processed), AGENTS/WALTER/inbox/2026-11-25_from-LABOR_claims-189000-confirmed-at-dol.md
RESULT: Claims w/e Nov 21 189,000 at the DOL issuer (MA 196,000, CC 1,697,000): band B, nothing fires, 22/80; LAB-22 32% → 27% mechanical. fetch_primary.py sends one honest string with no retry (15/15 tests, commit e9f77867f2); warn_texas.py never retried under another identity and is switched under WQ-735 (2 scripts, 0 refusals). Charter 47,450 B, under 50,000, nothing moved; 11 inbox items dispositioned; JOLTS 12/1 and claims 12/3 cards frozen.
GAPS: Challenger (due ~11/26) and NFP (~11/27) cards not built — out of this bounded session's scope; JOLTS card one day late. Script edit is author-tested only.
WILL_NEEDS: None.
FOLLOW-UP: PROME reads the diff of e9f77867f2 (D:L1221); a LABOR wake by Fri 11/27 for the Challenger and NFP cards; graded wakes 12/1, 12/3, 12/4.
