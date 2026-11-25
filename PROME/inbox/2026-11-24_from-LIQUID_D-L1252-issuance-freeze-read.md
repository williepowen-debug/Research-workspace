# LIQUID -> PROME: D:L1252 LIQUID leg done. Not a freeze: selective. Two of my gates fired on the 11/20 data (072 IG leg, first time; 069 L4)

**Row key:** D:L1252 (DOCKET physical line 1252). **From:** LIQUID, session liquid-desk-agent-2026-11-24, Claude Code, Opus 5.5 (claude-opus-5-5), laptop, woken by PROME prome-77 on Will's word 23:19 ET 11/24 ("wake LIQUID and HENRY now"). **Written:** 2026-11-24, `date` 23:33 ET before writing. $0. No trade proposal. No push (PROME pushes).

**Boot:** root `CLAUDE.md` 4 pages, `AGENTS.md` 1, `USER.md` 3, `AGENTS/LIQUID/CLAUDE.md` 4, `PROME/COMPLETION_SPEC.md` 4, each through `PROME/tools/boot_read.py` to `eof: true`. STATUS read whole; `boot.py` run 23:21 ET (31 series, 0 fetch errors). **No pull:** the tree carries other desks' work (PROME state files, AEOLUS, HENRY). The harness refused my desk research report file (`research/.../REPORT.md`, "subagents should not write report files"), so **this memo is the only full record of the evidence**; STATUS points here.

## For Will, in plain words

**The answer:** No, the market for new junk-company borrowing has not shut. Ordinary high-yield deals were still getting done last week, some on better terms than first offered. What is being refused is narrower: the weakest borrowers, and anything tied to AI data centres or loans against AI chips. One ordinary $400M loan (UST Global) was pulled on 11/16; a buyout loan (Fullscript) had to go to private lenders because the regular loan buyers passed; a bank (ING) could not find enough buyers for about $500M of data-centre loans on 11/20; another bank sold a piece of an Oracle data-centre loan at about 85 cents on the dollar.

**What it means:** the spread is doing the job we track it for, but only in one corner so far. The chain is: wider spreads, then weak companies cannot refinance, then defaults, then losses at lenders, then less lending to the economy. Right now the first link is working only for AI-infrastructure borrowers and the bottom tier. Investment-grade companies borrowed $46.5B last week at tighter prices than first offered, and the overnight money markets show no stress at all.

**Two of my own alarm lines tripped on Friday 11/20's data** (posted Monday, while the fleet was off):
- The investment-grade spread hit 0.98 points, above my 0.94 line, the first time since I set it in July. Its job is to say "re-check whether AI-linked borrowers are being priced like junk." Re-checked: yes, mostly in technology names, while the rest of the market stays open.
- My AI-credit line tripped a third leg: IREN fell 18.0%, Applied Digital 17.8% and Nebius 16.1% on 11/20 while the junk spread widened 0.24 points. It had already tripped two legs, so this adds no new action. CoreWeave's 5-year default insurance cost about 13.1% a year on 11/24, its highest in my recent record.

**What it does not establish:** ⚠️ I could not get last week's total junk-bond volume from free sources (the weekly totals sit behind paywalls), so "not a freeze" rests on named deals, not a full count. ⚠️ This is Thanksgiving week, which is nearly empty every year (a year ago the week before priced $6.4B in 7 deals and the holiday week was close to nothing). This week cannot tell a holiday lull from a freeze. Most deal facts are relays of Bloomberg or FT reports I could not open.

**What I expect next:** the real test is the week of 11/30 to 12/4, when deals parked before the holiday (TeamHealth, Internet Brands, the ADT buyout's $9.6B of bank debt) either get done or get pulled. My guess, unscored: about 70% that at least one more named junk deal is pulled by the 12/9 Fed meeting; about 20% that it becomes a broad freeze; about 35% that the whole move turns out to be an echo of the AI stock shock and fades. Repo-market stress is the last link, not the next one (about 10% by year end).

## 1. ISSUANCE-FREEZE read: NOT A FREEZE, SELECTIVE

Basis key: **P** = page I read; **S** = secondary relay of a paywalled original (Bloomberg, FT, IFR) that I did not read. No figure here was checked against an offering document.

| Date | Deal | Market | What happened | Source |
|---|---|---|---|---|
| 11/16 | UST Global $400M 5Y refinancing loan, Citi | US lev loan | **PULLED** "amid weak investor demand"; talk SOFR+425 to 450, 98 OID | Bloomberg 11/16 via debtserious Weekender 11/21 (S; single relay, no second report found) |
| 11/16 | Epoch Digital (Actis) $488M data-centre loan, Malaysia | Asian syndication | **DELAYED** (lender sessions, site visit cancelled; leads committed) | Bloomberg 11/16 headline; The Edge (S) |
| 11/16 | HSBC $300M piece of an Oracle New Mexico data-centre loan | secondary | sold mid-80s | Bloomberg via Weekender (S) |
| 11/17 | Fullscript LBO $1.3B, Morgan Stanley | to private credit | SOFR+400, 96 OID; Blue Owl, Antares, Golub, Carlyle; "BSL lenders passed" | Bloomberg 11/17 via Weekender (S) |
| 11/17 | Restaurant Brands $500M 6.00% senior secured | HY-type | **PRICED** | company release 11/17 (search summary) |
| 11/18 | Proofpoint $1.25B bonds + $735M TL (Thoma Bravo, JPM) | US HY + loan | **PRICED TIGHTER than talk**: 8.5% from about 9%; TL SOFR+450, 99.3 | Bloomberg 11/18 via Weekender, hedgeco (S) |
| 11/18 | Bridge Data Centres $6.6B to $7B loan (Bain; Citi, JPM) | loan | chip-access compliance clause added (Megaspeed link) | Bloomberg 11/18 headline (S) |
| 11/19 to 20 | SpaceX GPU lease notes (Saturn Funding Trust; Apollo, Goldman), KBRA prelim A- | IG structured | **PRICED, upsized**: A3 $25.168B T+345, 8.259%; public total $32.1B | WALTER SIG-W-20261123-012 (Apollo release read by WALTER; IFR via helper) |
| 11/20 | ING about $500M data-centre loan auction (Stargate NM, Vantage, CyrusOne) | secondary | **not enough bids**; individual sales | Bloomberg 11/20 via WALTER SIG-W-20261123-008 (S); Bisnow title 11/23 |
| 11/16 to 20 | US IG primary $46.48B, 58 tranches, 33 issuers | IG | **25 bp tighter than initial talk on average** | 9fin US IG Wrap 11/20 (P) |
| week to 11/20 | global | — | "investment-grade ... issuance remaining strong, while high-yield bonds came under pressure"; global HY spread +56 to 360 | T. Rowe Price recap dated 23 Nov 2026 (P) |
| 11/6 week | Cloud Software Group $2B HY | US HY | priced **wider** than high-9% talk (10%) | Octus LevFin Weekly 11/6 (P) |
| 11/6 week | Moneris $600M loan | US loan | **flexed wider** after missing 11/3 deadline | Octus 11/6 (P) |
| 11/6 week | TeamHealth multibillion loans + bonds | US HY + loan | **SIDELINED** after premarketing | Octus 11/6 (P) |
| 11/6 week | Internet Brands about $1.5B HY | US HY | launch "in the coming weeks"; reverse inquiry 10.5 to 11% | Octus 11/6 (P) |
| 11/13 week | Peloton $700M secured, Baldwin $2.15B loan | US HY + loan | **PRICED, UPSIZED** | Octus 11/13 (P) |
| 11/13 week | CCC Intelligent $2.85B, CVR $1.5B, Reliance Worldwide $1.35B (due 11/17 to 11/19) | US loans | **outcome not found** | Octus 11/13 (P) |
| pending | ADT take-private about $9.6B bank debt; Apollo backstop about $9.65B "in case participation from banks is lukewarm" | US loan | not syndicated | Octus (search summary; S) |
| Oct (rep. 11/9) | Nebius planned HY bond | US HY | dropped before launch; $3.5B one-year Citi loan instead | Reuters 11/9 via Yahoo/TheStreet (S) |
| October | at least 7 issuers, over $5B postponed | US + Europe | "biggest spate of debt sale delays this year" | Bloomberg via Advisor Perspectives 10/21 (S) |

| Week | US HY bond volume | Basis |
|---|---|---|
| 11/17 to 11/21, 2025 (same week a year earlier) | **$6.405B, 7 deals** | Informa IGM via search summary (S; page not opened) |
| 11/24 to 11/26, 2025 | near empty ("on eve of Thanksgiving all is quiet") | IFR headline (S) |
| 11/2 to 11/6, 2026 | "quiet issuance week", no figure in text | Octus (P) |
| 11/9 to 11/13, 2026 | "modest rebound in issuance", no figure in text | Octus (P) |
| **11/16 to 11/20, 2026** | **UNMEASURED** (Octus 11/20 text unreachable; Bloomberg/LCD paywalled) | gap |
| **11/23 to 11/25, 2026** | **UNMEASURED**; no HY pricing found 11/23 or 11/24 by search, not proof of none | gap |

**Free sources can show** named deals in free newsletters, headline relays, company releases and IG weekly tallies. **They cannot show** the weekly HY dollar total, deal count, parked-pipeline size, order books, or every pull. Seeking Alpha returned 403 to automation (stopped, not bypassed).

## 2. Gate statuses on their letters (no level, operator, instrument or consequence changed)

FRED first-published (`fetch.py fred --first-published`, my pull 23:22 ET 11/24; **11/24 cell not posted**), bp, 11/13 · 16 · 17 · 18 · 19 · **20** · 23: HY 323 · 334 · 343 · 347 · 352 · **376** · 363; IG 89 · 90 · 92 · 93 · 94 · **98** · 97; BB 186 · 196 · 204 · 205 · 210 · **229** · 219; B 344 · 357 · 368 · 373 · 380 · **408** · 393; CCC 1,316 · 1,310 · 1,329 · 1,353 · 1,361 · **1,402** · 1,387. Equity closes raw (yfinance `auto_adjust=False`), cross-checked with Nasdaq via `AGENTS/REGINALD/scripts/settled_bars.py` (all agree through 11/23; rc 0).

| Gate | Status (owner grade 2026-11-24 23:3x ET) |
|---|---|
| **GATE-LIQ-072** | **Leg (2) FIRED on the 11/20 observation: IG 98, strictly above 94** (97 [11/23] also). First fire since registration 7/9. Basis half not met (266 [11/23], line <180). Legs (1)/(4) UNGRADED: SpaceX A- notes at T+345 / 8.259% resemble "IG at BB-like spreads" (BB 229 [11/20]) but are a relay and a structured lease, not my source. Leg (3) CANNOT-FIRE. **Consequence on the letter: re-open the systemic-mispricing assessment; route HENRY + NEXUS** — routed via WALTER (packet below). Re-assessment: tech IG +30 bp since 10/6 vs +16 all IG (Wallstreetcn via Fixed Income News Australia 11/25, S); IG primary open and tightening from talk (9fin, P); read = AI credit repricing inside an open market, not a seizure. |
| **GATE-LIQ-069** | **L4 FIRED on the 11/20 session**: IREN −17.97% (14.41 → 11.82), APLD −17.81% (13.98 → 11.49), NBIS −16.11% (96.92 → 81.31); CRWV −12.02%; HY +24 bp (352 → 376) ≥ +5. **Legs fired: L2 (9/26), L5, L4 (11/20) = 3; no new consequence** (TWO-fired consequence already taken). L1 NOT FIRED 11/20 (BB 229 > 220 but CCC 5-session +86 vs 11/13, not flat) or 11/23 (BB 219). L4 NOT FIRED 11/23 (cohort +20 to +24%; HY −13). **11/24: credit half UNGRADEABLE (cell unpublished), equity half fails** on vendor post-close bars read 23:24 ET (CRWV −11.85%, APLD −11.58%, IREN −11.54% — BROCK's figure verified — NBIS −10.73%; with SOX −7.88% per WALTER SIG-W-20261124-007, so a sector move, IREN-specific cause not established), so L4 cannot fire 11/24. L2 stands, no re-count: CoreWeave 5Y Dec-2031, unflagged DTCC prints, my converter, clean: 1,078 [11/18], 1,151 [11/19], 1,233 [11/20], 1,076 to 1,092 [11/23], **1,267 to 1,314 [11/24]** (23.10 pt, 15:12 ET), above the 1,154 [11/10] recorded high. L3 NO_INSTRUMENT (ING, Nebius, Oracle-loan items logged, not graded; letter bars proxies). L5 no new Oracle rating action (search 11/24; S&P BBB- since 7/9, Moody's Baa2 negative). |
| **GATE-HY-REKILL** | **NOT FIRED, 0 of 2 through 11/23** (HY 363, 103 above 260). |
| **X1** | CLOSED / DON'T-SIZE, unchanged by its letter: the HY >280 price half stays met (363); BROCK's relative wrapper-leads half not graded here; GATE-LIQ-079 does not open X1. |
| GATE-LIQ-079 | NOT ARMED: SOFR99 − IORB +8 to +10 bp 11/12 to 11/23 (latest-revised, `transmission_check.py`); SRF ≤ $0.104B; reserves $2,979.7B [11/18]. |
| >320 sustained (WQ-444) | extends to 7 observations (323 … 363). |

**GATES cell wording PROME should carry (owner's wording, current):**
- **GATE-HY-REKILL:** `LIVE — owner NOT FIRED 0 of 2 through November 23 (HY 363 first-published, graded 23:3x ET 11/24 by LIQUID), 103 above 260; 376 [11/20], 352 [11/19]. Letter unchanged → workbook/KILL_MEMO_HY_OAS_260.md. >320 run 7 observations; REG-T-04 FIRED 11/23 (REGINALD grades); funding unchanged (SOFR99−IORB +9 [11/23], SRF $0); X1 stays CLOSED.`
- **GATE-LIQ-069:** `LIVE — owner grade 11/24: L4 FIRED on the 11/20 session (IREN −17.97%, APLD −17.81%, NBIS −16.11%; HY +24 bp 352→376), legs fired now 3 (L2, L5, L4), no new consequence. L1 NOT FIRED 11/20 (BB 229, CCC 5-session +86, not flat) and 11/23 (BB 219). L4 11/23 NOT FIRED; 11/24 credit half unpublished, equity half fails (worst CRWV −11.85%). CoreWeave 5Y about 1,314 bp clean [11/24, DTCC]. L3 NO_INSTRUMENT; L5 no new action. Next review on the 11/24 and 11/25 cells.`
- **GATE-LIQ-072 (state cell, currently the 11/12 grade):** `LIVE — owner leg (2) FIRED on the 11/20 observation: IG 98 first-published, strictly above 94 (97 [11/23]); first fire since 7/9. Basis 266, line <180, not met. Legs (1)/(4) UNGRADED (SpaceX A- notes T+345 a relay, not a graded source); leg (3) CANNOT-FIRE. Consequence taken 11/24: assessment re-opened (repricing inside an open IG market, not a seizure); HENRY + NEXUS routed via WALTER.`
- **Recommended review_by:** 069 → 2026-11-27 (grades the 11/24 and 11/25 cells; holiday 11/26); 072 → keep 2026-12-31 (one-observation leg, already fired; the assessment re-runs only on a new leg).

**Instrument note:** `gate069_legs.py` grades only the newest session, so on 11/24 it printed L4 NOT FIRED and could not see the 11/20 fire; graded by hand. A fix in my own tool (grade every session since the last graded one), owed in STATUS §3, no new checker.

## 3. PROME's addition: nonbank mortgage servicers (HOMER's Fitch item)

Inside my charter only for the spread and funding mechanics; the names and the bank-lender side stay HOMER's and REGINALD's. **Plausible, but on the bond side, not yet the warehouse side:** BB +14 and B +20 bp (11/18 → 11/23) raise the cost of servicers' unsecured refinancing, while warehouse lines are bank repo against loans, renewed on schedule and not priced off HY spreads day to day. **What I would watch:** a servicer bond deal pulled or priced wide of talk (Pennymac, UWM, Freedom, Rocket), a warehouse or MSR facility not renewed or with a higher haircut in a 10-Q or 8-K, and margin calls if rates move fast (MSR values fall when rates fall; 10Y 4.92 [11/23] from about 5.14 earlier in the month, secondary).

## 4. Forward view (PROJECTION, unscored, nothing registered)

**Is the spread a lead?** Historically yes, through refinancing: wide spreads come before more defaults and slower borrowing. Tonight that channel is working only at the bottom tier and in AI-infrastructure lending.

| By | Expectation | Mine |
|---|---|---|
| 12/11 | at least one more named US HY bond or lev loan pulled/postponed citing markets | ~70% |
| 12/11 | broad freeze: the 11/30 or 12/7 week under about $2B US HY with several non-AI pulls | ~20% |
| 12/11 | HY ≤330 on 5 consecutive first-published closes | ~30% |
| 12/31 | GATE-LIQ-079 arms | ~10% (LIQ-10 already registered) |
| 1 to 3 months | a neocloud or data-centre borrower restructures or misses a financing deadline | ~45% |

**Order if real:** AI-infrastructure and CCC financing (now to January) → distressed exchanges and defaults in the weakest names (Optimum grace about 12/16) → private-credit and BDC marks (Q4 marks, February) → bank lending standards (loan officer survey, early February) → repo funding last, if at all. **Alternative (~35%): an echo** of the AI equity shock (Nvidia SEC report 11/20, Huang exit and return, AMD resale registration 11/23); the spread gave back 13 bp in the 11/23 rebound. **The 17-business-day lag** in my 079 note: low weight; n=1, and it describes credit lagging a funding shock, while here credit moved and funding did not. Not a timer. **What changes my mind:** toward a broad lead, non-AI pulls in the week of 11/30 (TeamHealth, Internet Brands, ADT going to its backstop), IG deals stop tightening from talk, multi-billion HY fund outflows, CCC and B widening on up-equity days; toward an echo, the calendar clears at or inside talk, HY under 340 twice with B and CCC narrowing, CoreWeave 5Y back under about 1,100.

## 5. Tradeability

Sent to TERRY (`AGENTS/TERRY/inbox/2026-11-24_from-LIQUID_D-L1252-issuance-read-for-reread.md`) with the WQ-696 handoff lines: what the evidence implies, horizon, invalidation, unknowns. LIQUID constructs nothing.

## 6. Gaps

- US HY weekly volume 11/16 to 11/20 and 11/23 to 11/25 UNMEASURED (paywalled); year-ago figure is a search summary.
- UST Global pull rests on one relay; three launched loans' outcomes not found.
- 11/24 ICE cell unpublished: every 11/24 credit grade waits for it.
- Desk research report file refused by the harness; evidence lives in this memo only.
- No `AGENTS/SIGNALS.md` row (the brief limits commits to my directory and packets; WALTER packet carries the fires).
- **Deferred:** the inbox drain (3 packets, 27 WALTER cards incl. TERRY's 11/20 postmortem ask, PROME WQ-735, SIG-W-20261124-002 and -010), the 076 W1 as-of 11/17 addendum, the `gate069_legs.py` fix. Reason: items 1 to 3 first; drain follows in this session if time allows, else next wake.

## COMPLETION — LIQUID — 2026-11-24
STATUS: ⚠️ PARTIAL
CHANGED: PROME/inbox/2026-11-24_from-LIQUID_D-L1252-issuance-freeze-read.md, AGENTS/TERRY/inbox/2026-11-24_from-LIQUID_D-L1252-issuance-read-for-reread.md, AGENTS/WALTER/inbox/2026-11-24_from-LIQUID_ROUTE-072-IG-fire-069-L4.md, AGENTS/LIQUID/STATUS.md
RESULT: ISSUANCE-FREEZE read = NOT A FREEZE, SELECTIVE: 20 named deals since 11/02; mainstream HY priced (Proofpoint 8.5% inside 9% talk), IG $46.5B 25bp inside talk; refusals concentrated in AI-infra and weak credits (UST Global pulled 11/16, ING DC auction failed 11/20, Fullscript to private credit). GATE-LIQ-072 leg 2 FIRED (IG 98 [11/20], first since 7/9); GATE-LIQ-069 L4 FIRED 11/20 (IREN −17.97%, HY +24bp), 3 legs, no new consequence; HY-REKILL 0 of 2; X1 CLOSED; 079 not armed.
GAPS: US HY weekly volume UNMEASURED (paywalled); 11/24 ICE cell unpublished; inbox drain deferred (items 1-3 first); desk report file refused by harness.
WILL_NEEDS: None.
FOLLOW-UP: Week of 11/30-12/4 is the freeze test (parked pipeline prices or pulls); LIQUID grades 069 on the 11/24-25 cells (review_by 11/27 recommended); drain inbox; TERRY re-read.
