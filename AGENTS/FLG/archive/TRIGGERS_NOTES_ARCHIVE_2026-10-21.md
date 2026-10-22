# FLG — TRIGGERS.tsv Notes archive — rotated 2026-10-21

Verbatim note segments rotated out of `workbook/TRIGGERS.tsv` Notes cells on 2026-10-21 (read_cap_check rotate-tier: 85% of budget). Segments were ' | '-separated in the cell; here one per paragraph. History, never current — the live row carries the current state. crc32 is over the section body (segments joined by a blank line).

## T-07 — segments [1, 2, 5, 6] (crc32 `39868ddd`)

2026-08-28 FLG re-read: FLG $13.48 (fetch.py, live) = -5.34% vs the FROZEN $14.24 baseline; band 1 ($12.82) sits 4.9% below spot, 53% of the way. Essentially unchanged from the $13.49 build read eight days earlier — the tape has not moved on ANY of this session's findings.

🔴 2026-09-24 FLG: BAND 1 BROKEN ON 2026-09-16 (close $12.58 < $12.82) AND UNSEEN FOR 8 DAYS — this ladder has NO implementing script (PROME L441 census 2026-09-23:60), and this row's own Next_Check (2026-11-14) was a quarterly date on a DAILY instrument, so FLG's boot could not have caught it either. 9/23 close $12.30 = -13.6%; band 2 ($12.10) is 1.6% below. Since 8/28: FLG -8.5% vs KRE -4.7%, VLY -6.8% — mostly a NYC-regional move; FLG residual vs VLY ~-1.7pp; attribution UNKNOWN (KB-FLG-054). Next_Check re-dated to 2026-09-30 (weekly while within 5% of a band) — a hand clock, not a detector; the detector gap is routed to REGINALD/PROME.

2026-09-27 FLG: last close $12.37 (2026-09-25, fetch.py, pulled 9/27) = -13.1% vs FROZEN $14.24; band 2 ($12.10) 2.2% below; lowest intraday since 9/16 = $12.22 (9/24) — band 2 NOT touched. 9/23->9/25: FLG +0.6%, KRE +1.7%, VLY +1.6%.

2026-10-01 FLG (T-08 spawn; REGINALD 9/29 packet consumed): ONE BAR with REGINALD — yfinance daily closes pulled 10/1 11:06 ET: 9/28 $12.04 (-15.45% vs FROZEN $14.24) · 9/29 $11.84 (-16.85%) · 9/30 $11.67 (-18.05%) = three settled closes at or below ORANGE $12.10; REGINALD's 9/28 $12.04 and 9/29 $11.84 match to the cent. 10/1 intraday $11.39 at 11:06 ET (-2.44%; session low $11.365) = AT the RED line $11.39 — UNSETTLED, not graded; RED = a settled close <= $11.39 and REGINALD grades it. 9/25->9/30: FLG -5.66% vs VLY -3.52%, KRE -2.95% (residual vs VLY ~-2.1pp). EDGAR CIK 910073 newest filing still 2026-08-14 (checked 10/1 11:09 ET). CAUSE: UNKNOWN — the only dated name-specific item in the window is the freeze taking effect 10/1, public since June; FLG asserts no attribution. ORANGE carries NO consequence on FLG's side beyond the label: no position (TRADE.md), price is not a thesis input, no trade proposal forced. Next_Check 9/30 -> 2026-10-23 (next FLG wake = PROME DOCKET L522); REGINALD's vx_ladder_check.py stays the detector; 'weekly' was a hand clock on an idle desk.

## T-12 — segments [1, 2] (crc32 `37fedee5`)

READ PATH (stated 2026-09-24, PROME ask): FLG is idle until 9/30. Guaranteed reads = PROME's 9/25 GATE-FLG-T08 pre-fire check + this row's 9/30 check. BEST-EFFORT between them = WALTER intake term proposed 9/24 (inbox packet) — WALTER routes only what reaches its intake, so it is NOT a detector. A stay landing 9/26-9/29 is seen at earliest 9/30 unless WALTER intake carries it: ACCEPTED gap, 1 business day before T-08, stated not implicit.

2026-09-27 (KB-FLG-060): 9/24 hearing produced NO stay and NO merits ruling. Dated items: 9/29 city screenshot production · ~10/24 full production (30d) · merits 'before year-end' (EVENT, slips). Row stays weekly; after 10/1 the live question is the MERITS (annulment would land AFTER frozen leases are signed — retroactivity is an unread known-unknown). Watch terms re-proposed to WALTER 9/27 to add merits/appeal phrases.

## T-08 — segments [2, 3, 4] (crc32 `3d84384c`)

⚠️ 2026-09-24 (KB-FLG-053): the effective DATE is still HARD, but the order's SURVIVAL is not — seven landlords' suit to annul Order #58 is before Justice Lantry (NY Sup. Ct., Manhattan); discovery of Mayor's Office<->RGB communications ordered ~9/16 with the court citing 'significant concern' about the Board's procedure; no stay reported as of 9/17. Grade on fire BOTH legs: did 10/1 arrive, AND was the order in force on 10/1. See T-12.

🔎 RE-SOURCED 2026-09-24 (KB-FLG-059): Kenilworth Holdings LLC et al. v. NYC RGB, Art. 78, filed Richmond Index 85199/2026 (NYSCEF Doc 1, 7/22), transferred to NEW YORK COUNTY 8/21 (Porzio), Justice Lantry. Petition prayer (f) asks for an injunction 'if necessary' barring the freeze from taking effect — reported UNRULED as of 9/17. NY County index, discovery-order text and docket state = SEARCH-NOT-FOUND (NYSCEF Cloudflare 403).

2026-09-27 (KB-FLG-060): 9/24 hearing — NO STAY ISSUED; freeze 'will for now stay in place' for leases commencing on/after 10/01; merits ruling 'before the end of the year'. Leg 2 ('order in force on 10/1') is now highly probable but grade it AT 10/1, not from the 9/24 report — the source says the judge did not rule by 10/1, not that a stay motion was denied (WALTER's 'declined a stay' is a gloss).

## T-03 — 2nd pass, segments [0, 1] of the post-first-pass cell (crc32 `e2a35cb3`)

[EST] — EVENT anchor, SLIPS. Do not treat as dated. Confirm at IR once announced, then re-date this row and set Anchor_Type=HARD.

🔁 2026-09-27 RE-DATED 10/27 -> 10/16: the 10/27 check sat AFTER the likely event. Observed pattern: Q4-25 Fri 1/30, Q1-26 Fri 4/24, Q2-26 Fri 7/24 (all 4th Friday, 6:00 ET release, 8:00 ET call) => Q3-26 most likely Fri 2026-10-23 [EST, pattern-derived, NOT announced as of 2026-09-27 web search]. 10/16 = look for the date announcement; set Anchor_Type=HARD once announced.

## T-12 — 2nd pass, segments [2] of the post-first-pass cell (crc32 `f6029528`)

2026-10-01 (T-08 spawn): the 9/30 check was consumed one day late, at the T-08 grade. No stay, appeal, emergency application or merits ruling found through 10/1 10:11 ET (4 secondary; every court primary 403 — KB-FLG-071). 9/29 screenshot production: whether made = SEARCH-NOT-FOUND (no report found). Interim relief: Lantry declined to revert to 3%/4.5% (said it was not in his authority); a written order on prayer (f) = UNKNOWN (docket unreachable). Next dated items: ~10/24 full production (30 days from 9/24) · merits 'before the end of the year' (EVENT, slips). CADENCE CORRECTED: 'weekly' was a hand clock on an idle desk. FLG next wakes 10/23 (DOCKET L522); between wakes the only read is the intake term (DOCKET L467). Owner view sent to PROME: drop it to routine on 10/07, do NOT retire it before the merits ruling. Retroactivity of an annulment after 10/1 leases are signed: still unread.
