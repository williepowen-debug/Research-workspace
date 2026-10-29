# REGINALD boot + catch-up — 2026-10-28 (Wed, 22:21–23:0x ET)

**Launched by:** Will ("boot up… catch up on any owed tasks or updating with new data or news"). Last session closed 10/23 17:12 ET, so three trading days (10/23 close, 10/26, 10/27) were ungraded.
**Runtime:** Claude Code CLI. Model Opus 5.5 (`claude-opus-5-5`), session `reginald-78`, cwd `AGENTS/REGINALD`, repo root `/home/willi/Research-workspace`. Tools: Bash/Read/Edit/Write, Agent (one fork used for signal reading), ListAgents/SendMessage (verified: DEWEY doorbell delivered), web via curl. MCP servers definite and mtnewswire and Prisma-Local failed to connect (not needed). Quartr is available but was not used.
**Git at boot:** 0 ahead / 0 behind origin after fetch. Dirty paths belonged to FERT, OTTO and PROME (live work), so no pull was needed or attempted.

**Read order:** root CLAUDE.md and charter (injected) → STATUS → MEMORY → ROADMAP → LESSONS → CALENDAR → USER.md → AGENTS.md → PROME/COMPLETION_SPEC.md → BANK_RESEARCH_STANDARD.md → PLAYBOOK § Runtime mechanics → docs/GIT_WORKTREE_PROCEDURES.md. **Scripts:** `market.py`, `vx_ladder_check.py`, `ledger_staleness.py` (both), `boot.py` (rc 1 ALERT: insider, 8-K, FLG ladder, corrections, inbox), `settled_bars.py` WAL/KRE (RC 0), FRED pulls with a fresh cache dir, `corrections_boot_check.py` (now rc 0), `read_cap_check.py`.

## §1 Mechanical grades (root rule #8 first)

| Item | Reading | Grade |
|---|---|---|
| `REG-T-02` WAL exit | settled $76.12 [10/23], $75.44 [10/26], $76.40 [10/27]; Yahoo and Nasdaq agree | Below 81.90 every day: run **0-of-3**, state FIRED. 40 log rows through 10/27. 10/28 bar excluded as unsettled |
| `REG-T-01` KRE | $72.46 / $72.73 / $72.58 settled | UN-FIRED, ~$12.6 above $60 |
| `REG-T-03` HY >320 | FRED BAMLH0A0HYM2: 338 [10/23], 330 [10/26], **318 [10/27]** | Stays FIRED. The 8-close run above 320 ended 10/27. Exit needs ≤300 ×5: run 0 |
| `REG-T-04` HY >350 ×3 | Peak 340 [10/22] | **NEVER FIRED.** Run 0 of 3 throughout. DOCKET L818's 10/28 publication check is answered: no fire, no WQ-512 disclosure needed |
| CCC/HY `VX-REG-18.04` | 4.01× [10/23], 4.08× [10/26], **4.15× [10/27]** (CCC 1,356 → 1,345 → 1,321) | HARD-FIRE continues, NO escalation. From 10/22, HY fell 6.5% and CCC 1.4%, so the ratio rose on the denominator. The vector's own rule: HY-tightening-led = artifact |
| Tier shape (L818 ②) | BB 210 → 187, B 346 → 322, CCC 1,340 → 1,321 [10/22 → 10/27] | BB and B are tightening faster than CCC: the reversal is led by the upper tiers. **No transmission widening** |
| `REG-T-08` SOFR−IORB | +2 [10/23], +3 [10/26], **+5 [10/27]**; IORB 3.90 | 10bp under the line. SOFR rose 7bp in a week into month-end. Descriptive; LIQUID owns the read |
| `VX-REG-6.03` FLG ladder | last settled **$10.14 [10/27] = −28.8%** vs FROZEN $14.24 | RED, 14 settled closes below RED since 10/7. Ladder exhausted |
| Claims | 194K [w/e 10/17] still latest; next print Thu 10/29 | 🟢 |

**FLG insider (boot alert, verified at the filing):** director Alan L. Frank made an open-market purchase of **10,000 shares at $10.14 on 10/27** (Form 4 acc 0001649471-26-000006, code P, direct, holds 76,463 after). About $101K, four sessions after the Q3 miss. This is context, not a thesis input. The FLG desk owns the name. KB ML-REG-254.

**8-K monitor:** the only cohort 8-Ks since 10/21 are the Q3 earnings releases (2.02) already read. WAL, ZION and CFG are clear. OZK has no FDIC filing since 10/20.

## §2 SBCF Q3 and the Florida frame

Seacoast (SBCF) 8-K acc 0001628280-26-067572, EX-99.1, filed 10/27. Filer name verified on the EDGAR submissions API.

| Frame cell (FROZEN `reports/2026-09-24_FL_bank_rail_Q3_FROZEN_frame.md`) | Q2 baseline | Q3 | Bar | Cell |
|---|---|---|---|---|
| Criticized+classified % (8-K) | 2.88% | **2.90%** | TRANSMITS ≥3.20% | **HOLDS** |
| CRE+constr 30-89 accruing (primary, 10-Q) | $7.09M | not in release | ≥$12.48M AND 60-89 ≥$3M | UNREAD |
| CRE+constr nonaccrual (10-Q) | $43.42M | not in release | >$55.8M | UNREAD |
| Resi nonaccrual (FL-resi sub-read, excluded from the combiner) | $28.6M | not in release | >$36M | UNREAD |

**SBCF = HOLDS-PENDING-P** (A2.4: all read cells hold, primary unread). Release context: nonperforming loans $73.3M (0.54%), down from $86.5M (−15%). Accruing past-dues $27.4M, up from $20.1M (+36%; category split not disclosed). NCO $5.4M vs $3.2M. ACL 1.41% (+3bp), including an **$8.4M measurement-period reserve on one acquired VBI loan** (unexplained in the release). CRE at 250% of bank-level risk-based capital (230% Q2). TBV/share fell from $17.25 to $15.96, with ~$1.63 from AOCI on higher rates. The call (10/28 10:00 ET) was not heard.

⚠️ The past-due rise could still reach the primary bar. If all +$7.3M were CRE+construction, the cell would be ~$14.4M, above $12.48M, and the 60-89 limb would still decide it. That is why SBCF stays PENDING rather than HOLDS.

**Aggregate (A3 overlay):** AMTB HOLDS final; SSB HOLDS provisional; BKU HOLDS-PENDING-P; SBCF HOLDS-PENDING-P. T = 0, H = 1, m = 3, so the aggregate is **PROVISIONAL / UNKNOWN pending SSB, BKU and SBCF 10-Qs** (target ~11/14). No cell at any name transmits. If the 10-Q cells hold, it resolves NO TRANSMISSION, extending the Q2 read. Under the frame's rule, no CORAL/PROME packet fires (that needs two TRANSMITS).

## §3 Funding read (blind-spot set, descriptive)

**H.8, released 10/23 (data w/e 10/14; Fed tables 8 and 9; saved with sha256 in `domain/sources/2026-10-28_boot/MANIFEST.tsv`):**

| Small domestically chartered banks | w/e 10/7 | w/e 10/14 | Change |
|---|---|---|---|
| Borrowings SA | 307.3 | **316.4** | +9.1 (+3.0%); above 9/30 (314.8 rev) |
| Borrowings NSA | 295.3 | 302.7 | +7.4 |
| Deposits SA | 5,688.4 | 5,695.4 | +7.0 |
| Cash assets SA | 482.1 | 494.2 | +12.1 |
| C&I SA | 742.2 | 742.0 | flat |
| NDFI loans SA | 200.8 | 202.3 | +1.5 |

($B.) The 10/7 "partial reversal" did not hold: borrowing is back to the high of this window. Deposits and cash rose with it, and the credit lines are flat. This is the same reading as 10/10: banks lining up cash, with no run and no credit draw shown. All banks: NDFI 2,105.8 (+0.4%), C&I 2,992.6 (+0.2%). KB ML-REG-255.

**H.4.1 of 10/22 verified at the Fed artifact:** primary credit $9.169B on Wed 10/21, $8.935B weekly average. That matches WALTER SIG-W-20261022-034. The next H.4.1 is Thu 10/29.

## §4 BaaS / sponsor-bank perimeter (WQ-228)

- **Coastal (CCB) 8-K, 9/28** (acc 0001437958-26-000065, Item 8.01, read for the first time today): ~**$447M of Bluevine-related deposits on balance sheet at 9/25/26**; 22 active CCBX partners at 6/30. Coastal expects no material adverse liquidity effect and can bring sweep deposits back on-balance-sheet. Against $4,861.9M total deposits at 6/30/26 (XBRL, 10-Q acc 0001437958-26-000061), that is **~9%**. The two figures are dated 9/25 and 6/30 respectively. Valley closes Bluevine ~early 1Q27 and moves the deposits within 180 days. This answers the ROADMAP row's open question (on-balance-sheet share). It is a funding exit, not a credit loss. KB ML-REG-253. CCB reports Q3 Thu 10/29 pre-market and promised more detail.
- **CARL join fields: ACCEPTED** on all seven COVERAGE rows, with three bank-side notes (packet `a6caf49aa`). One of them was verified today: WebBank's parent, Steel Partners Holdings (CIK 1452857), last filed a 10-Q on 2024-11-08, so WebBank has no listed-parent route in 2026.
- **Q3 dates (carried item closed):** Pathward (CASH) printed its September quarter on 10/21 (8-K acc 0000907471-26-000042), unread here. Green Dot (GDOT) has no Q3 8-K yet; its last 2.02 was 8/10. Coastal reports 10/29.

## §5 Nano Banc

FDIC failed-bank page fetched 22:28 ET: HTTP 200, "Last Updated: October 19, 2026". The links are the bid summary, FAQ, creditor notice and press release only, so the **P&A is still NOT POSTED**. Under the CALENDAR rule, I sent DEWEY a request for a **passive** public-record route (packet `228cfa31a`). Per DOCKET L516, an FDIC Resolutions Call Center inquiry is an external send that needs Will's OK. **I do not recommend it now.** Nano is a ~$0.7B failure. The shared figure (≈$120M ≈ 17%, 9/22 base) moves only on the P&A schedules or the Fed OIG review (~3/25/27), and DEWEY's 10/14 template read warns the public schedules may not list loans anyway.

## §6 Inbox lanes and corrections

- **WALTER lane:** 45 signals read whole and filed. **BOARD diff:** 174 cards since 10/23 were scanned and 5 REGINALD-addressed cards read. Of the 50 BOARD_LOG rows: INFO_ONLY 41, BACKFILL 5, REFERRED 3 (HOMER housing order; OZK Chicago refinancing SIG-W-20261027-041; OZK Culver City SIG-W-20261027-052), INTEGRATED 1 (correction 025-002, applied 10/23). None moved a REGINALD figure. Context worth keeping: MainStreet (MNSB, Fairfax VA, outside the cohort) has problem loans of $92.0M vs $23.4M a year ago, nonaccrual 4.71%, and CRE at 374% of capital. That is DC-metro context beside EGBN (SIG-W-20261027-030, issuer primary). Trepp's Q3 preview office DQ of 12.33% conflicts with the 12.16% monthly series; CREED reconciles (noted on the REG-T-07 row, not substituted). The reading was done by a fork with no repo writes; I verified its counts, columns and the rows touching my surfaces before applying.
- **General inbox (9):** CARL accepted; ISHM boundary accepted (`1500962a7`); DEWEY FHA/VA pointer sent. The 7/25 "kill" was a **name-level split** (`fe55364ea`, `309751823`). BROCK's CFG correction is integrated (§7). CYPHER ×3 graded no bank consequence (no named bank or victim). LABOR T-07 and the DEWEY correction are INFO.
- **Corrections (R1):** COR-20261025-02 APPLIED (done 10/23); COR-20261023-39, -20261029-04 and -20261029-07 NO-OP after my own grep. `corrections_boot_check.py` is now rc 0.
- **DEWEY REQ-003** was delivered 10/23 (ahead of 10/26) and consumed that session. The MEMORY carry was stale.

## §7 Correction to my own record (BROCK 10/25)

CFG's $8,756M + $4,096M = $12,852M is the **March 31** Table 9 figure; June 30 is $9,852M + $4,875M = $14,727M. My **10/21 owed-items report, row 12, wrongly called both June 30 endpoints.** A dated correction is appended there, and that row is kept as written. KB ML-REG-148 (7/25) also labelled the Q1 lines as Q2. **ML-REG-251** now records the correction, and the cold dashboard is annotated. My 10/11 and 10/16 reports were already right. FLOW.tsv and the 10/10 snapshot are frozen and not edited. BRK-31 is BROCK's.

## §8 Trade-idea route

No candidate (TRADE.md §2b row 2026-10-28). SBCF held. REG-T-04 never fired, so the broad-credit window WQ-509 targeted did not open (that card is TERRY's). The 10-year remains the live driver, and its falsifier is already in TRADE §4.

## §9 Not done / carried

- SBCF call not heard; the VBI-loan reserve and the past-due composition wait for the 10-Q.
- Pathward September-quarter release not read (BaaS row; next session).
- CARL and ISHM were not found among local Claude sessions; non-Claude runtimes were not enumerated. Their liveness is UNKNOWN (not DARK), and PROME is told. Packets are committed.
- **JWT for FFIEC CDR expires 11/05**, two days before the 11/07 Call Report run and ranking test. Regeneration is Will's (PWS login).
- Read-cap: STATUS, ROADMAP and CALENDAR rotated this session (verbatim + crc). The charter (77% of budget) trim is pending Will.

**§5 addendum (22:45 ET, DEWEY reply `41c72f558`):** there is no passive public-record route a desk session can complete tonight (`AGENTS/DEWEY/output/2026-10-28_nano-loans-passive-records-route.md`). On file: FDIC-R asserted succession on the Ontario deed of trust (*Plaza Continental* Doc 100, filed 10/2, WAL's 10/14 read). So the receiver still held that one loan as of 10/2: one loan, one date. That is **not** proof that the FDIC retained all four liens, or that Sunwest took none. The recorder indexes need a human; CourtListener now needs an account token (Will's call, already registered by OTTO). The shared figure (≈$120M ≈ 17%, 9/22 base) is unchanged. DEWEY also corrected its R30/R39 row to "kill narrowed by name".

**§3 correction (same evening, after Will asked for depth):** the "lining up cash" reading above rests on one week. Over the six weeks 9/2 to 10/14, cash rose $13.7B against $33.5B of borrowing, and loans rose $47.6B. The borrowing mostly funded loan growth, alongside rising deposits, so "not a run" stands and "cash-building" does not. The 10/7 to 10/14 cash rise refilled cash spent on a one-week $9.7B credit-card portfolio step. Full analysis → `reports/2026-10-28_small-bank-borrowing-deep-dive.md`.

**§6 addendum (closeout, 23:3x ET):** OZK channel entry (10/28 23:0x) ACKed. OZK's own loss at transfer on six 2026 resolutions is 24.6% pooled (range 7–32%; KB-269). That is wider than the 13–22% realized haircuts in my 10/22 appraisal test, and it is the OZK input for the next loss-bridge run. WAL pointer: the cold dashboard's NDFI $1.54T row (retracted by BROCK 3/17) is struck; KB ML-REG-259. CREED's VLY multifamily packet (uncommitted by its author at close) is deferred to next session. It is consistent with the VLY early flag.
