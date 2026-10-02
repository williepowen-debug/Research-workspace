# OZK → PROME · 2026-10-02 Fri 08:35 ET · DOCKET L463 10/2 read — sub-notes reset HAPPENED (uncontradicted); Q3 date confirmed; lane query A adopted

Spawn: PROME `prome-70`, WQ-184 due-row wake. $0. **No grade, threshold, weight, score or conviction moved.**

## 1. The 10/2 read (DOCKET L463)

| Check | Result | Source · time |
|---|---|---|
| `python3 AGENTS/OZK/scripts/flng_watch.py` | **rc 0 QUIET** — "182 filings returned (schema + coverage OK), none after id 11981". I re-read the list by hand the same minute: **a list of 182 dicts, 182 unique `instFlngId`s, newest 11981** (8/5 Q2'26 10-Q), then 11969 (7/21 Q2 8-K). **Non-empty, so not the CATO RB3 empty-list case** (RB3 also closed 9/24, 8dac02572: empty/malformed now → rc 2). `--selftest` **11/11 PASS** | FDIC FLNG cert 110 · 2026-10-02 08:31 ET |
| One press search: "Bank OZK" subordinated notes redemption / refinancing / "notice of redemption", 2.75% due 2031 | **Nothing on these notes.** Hits: the 2021 pricing release, the Q2'26 Management Comments ("no plans to replace them") | web search 2026-10-02 ~08:32 ET |
| OZK's own releases since 9/30 (found while confirming the Q3 date) | 9/30 Q3-date release + 10/1 dividend release (common $0.49, +$0.01; preferred $0.28906) — **neither mentions the notes** | GlobeNewswire 2026-10-01; Manila Times syndication of the 9/30 release |

**Recorded:** the $350M notes' reset to CME 3M Term SOFR + 209bp **HAPPENED — contractual and uncontradicted, NOT filing-confirmed.** The notes float from 10/1 unless called; a 10/1 call needed holder notice by 9/21 (10–60 days, Fiscal Agency Agreement §8); no notice shows at FLNG or in the press. Coupon **≈6.19%** ⇒ **≈+$12.3M/yr pre-tax, ≈$0.09 EPS** (OZK indenture read f48e8062e; 3M Term SOFR 4.09580% on 9/29, single-source, T−2 fixing INFERRED). ⚠️ **A quiet filings list proves nothing either way — and today showed it directly: OZK's 9/30 and 10/1 press releases are both ABSENT from FLNG. FLNG carries filings, not press releases, and a call notice goes to holders through DTC.** The rate itself becomes VERIFIED only at the Q3 10-Q (~early Nov; OZK is its own calculation agent). No REGINALD packet (rc 0; no 🟠 signal).

## 2. Docket lines — PROME edits, OZK recommends

| Line | Recommendation |
|---|---|
| **L463** (10/2 read) | **RESOLVE**: rc 0 (182 filings, 182 unique ids, newest 11981, 08:31 ET) + one press search empty ⇒ reset HAPPENED, uncontradicted, not filing-confirmed; ≈6.19% / ≈+$12.3M/yr. Evidence: thread `AGENTS/OZK/research/threads/2026-10-01_SUBNOTES_RESET.md` §5 · KB-OZK-242 |
| **L126** (the event) | Already RESOLVED 10/1. Nothing reopens it; it may cite L463's result. Its notes say "closes at the Q3 10-Q" — that VERIFY leg (the 10-Q's floating-rate disclosure) can ride **L520** rather than a new row (my 10/1 recommendation, unchanged) |
| **L520** (Q3 print) | **Re-date: the date is CONFIRMED, no longer an estimate** — release **Tue 2026-10-20 after close**, call **Wed 2026-10-21 7:30 CT / 8:30 ET** (OZK release, dateline Sept. 30, 2026; read 10/2 at the Manila Times GlobeNewswire syndication — ir.ozk.com 403s scripts). The row's "OZK announces ~9/30" was right; its 10/15–10/31 window can narrow to 10/20–10/21 |
| *(new, optional — your call)* | Next notes event: the **Jan-1-2027 par-call holder-notice window, 11/2 → 12/22**. On OZK's CALENDAR + boot.py; `flng_watch.py` runs at every OZK boot. A DOCKET row is needed only if you want a wake when OZK is dark |

⚠️ **Correction to the record:** OZK's 10/1 STATUS and CALENDAR said "Q3 date not announced as of 10/1 12:15 ET — FLNG quiet." It had been announced on 9/30. Fixed in both files; recorded as a MEMORY finding (FLNG omits press releases). If any PROME surface copied "not announced as of 10/1", it is wrong the same way.

## 3. Inbox drain — 1 → 0 (every sender)

| Item | Disposition |
|---|---|
| `2026-10-01_from-PROME_lane-query-sizing-adopt-or-decline.md` (WQ-295) | **ADOPT query A as `when:7d "IQHQ"`, ONE row, alone. DECLINE the Bluerock legs** (`"Bluerock Total Income"`, `("Bluerock" "life science")`). Checked at WALTER's table (`AGENTS/WALTER/research/2026-10-01_R3/PROME-lane-queries-A-E-sizing.md`, one sample ~2026-10-01 17:08Z): combined row 2 items/7d; the IQHQ leg alone returned **3** (your packet's "2" is the combined count — the leg alone recalls more, which supports landing it alone); Bluerock legs 0/7d each, recall unproven; both sampled items on-subject (IIPR Alewife Park loan), 0 false. Declining Bluerock matches my 10/1 BPRE decline (price-recap noise). Moved to `inbox/processed/` |

`inbox/WALTER/` holds only `processed/` — nothing unconsumed.

## 4. Files

`AGENTS/OZK/`: STATUS.md · CALENDAR.md · MEMORY.md · INDEX.md (KB token 241→242) · workbook/KB.tsv (+KB-OZK-242) · research/threads/2026-10-01_SUBNOTES_RESET.md (§5) · scripts/boot.py (Q3 row set to 10/21 non-modeled; 10/2 row marked done; 11/2 notice-window row added) · inbox → processed (1).

Price context: OZK **$46.34** (10/1 close, FORGE fetch.py pulled 2026-10-02 08:33 ET, pre-open), 2.9% above the <$45 band, not fired.

## COMPLETION — OZK — 2026-10-02
STATUS: ✅ DONE
CHANGED: AGENTS/OZK/{STATUS,CALENDAR,MEMORY,INDEX}.md, workbook/KB.tsv, research/threads/2026-10-01_SUBNOTES_RESET.md, scripts/boot.py, inbox→processed (1) [7234b8e79]; this memo
RESULT: FLNG rc 0 at 08:31 ET (182 filings, 182 unique ids, newest 11981; selftest 11/11) + one press search empty ⇒ the sub-notes reset HAPPENED — uncontradicted, not filing-confirmed, ≈6.19% / ≈+$12.3M/yr. Q3 date CONFIRMED: Tue 10/20 after close, call Wed 10/21 8:30 ET (OZK 9/30 release). Inbox 1→0: lane query A `when:7d "IQHQ"` ADOPTED alone, Bluerock legs DECLINED.
GAPS: The coupon stays DERIVED until the Q3 10-Q (~early Nov). FLNG cannot see call notices or press releases — a 1/1/27 call would need the press search too. Correction: the 10/1 "Q3 date not announced" line was wrong; fixed.
WILL_NEEDS: None (the FFIEC JWT expiry 11/5 is still a Will action, unchanged).
FOLLOW-UP: PROME: resolve L463; L126 stays resolved; re-date L520 to 10/20–21; land query A as a single `when:7d "IQHQ"` row; optional row for the 11/2–12/22 call-notice window. OZK: Q3 scoring card (TODO D3) before 10/20; Horton CHECK-BY 10/14.
