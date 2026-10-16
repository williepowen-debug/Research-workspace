# 2026-10-16 — BROCK → PROME: D:L653 CABO backstop · BRK-31 MTB/CFG · CRMT 10/15 window · L0 drain

**Spawn:** prome-ac, WQ-184 L0, Tier 1, $0. Booted at 13:36 ET (root CLAUDE.md, AGENTS.md, USER.md, BROCK CLAUDE.md, SCRATCH, STATUS, LESSONS read explicitly). Not pulled: the tree holds other desks' uncommitted work (WALTER, BOARD, PROME state).

## 1. D:L653 — Cable One (CABO) MBI close, backstop read
| Check | Result |
|---|---|
| CIK | **0001632127 VERIFIED** (submissions JSON: "Cable One, Inc.", ticker CABO) |
| Feed (JSON + browse-edgar Atom, owner=include), 13:37 ET | Newest filing is **still the 10/14 Graham 13D/A** 0000950157-26-001101 (index page accepted 2026-10-14 21:55:47 ET); before it, the 10/2 8-K. **No close 8-K, no extension, no financing agreement.** An Item 2.01 8-K for a 10/9 close would have been due by 10/15. |
| Close outcome | **NOT CLOSED, per press. UNDISCLOSED at EDGAR.** Light Reading (2026-10-12): a New York federal court entered a **temporary restraining order (TRO) on Fri 10/9**, after a suit by lender **CoBank** (~$1.1B secured), pending a hearing whose date is not stated. CoBank alleges a fraudulent transfer and says Cable One "is trending towards a bankruptcy proceeding". Cable One's statement, which is not on EDGAR, cites progress with GTCR, existing lenders and "a consortium of leading private lending institutions" on financing for $2.45B of obligations, with **no definitive agreements**. ⚠️ Press only: the court docket (SDNY, PACER) was not read. |
| Price | **CABO $7.51 (−11.39%)** [fetch.py 2026-10-16 13:37 ET]; it was $11.88 on 10/9 |
| Grade / next read | Silence grades nothing. The TRO is positive press evidence that the deal has not closed. **Next read: Fri 10/23** (BROCK CATALYSTS row added), or sooner on a WALTER signal about the hearing outcome. ⇒ Suggest annotating L653 COVERED and registering a 10/23 row, if PROME wants the spawn driver to carry it. |
| Routing gap | The 10/9 TRO never reached BOARD or BROCK's lane: grepping BOARD/ for "CoBank" returns no 10/9–10/16 hit. **Packet sent to WALTER** (self-committed). |

KB-BRK-348.

## 2. BRK-31 — MTB and CFG Q3 releases (frozen frame 2026-10-09; letter unedited)
| Bank (8-K, 10/16) | Measured | F1 / F2 |
|---|---|---|
| **CFG** 0000759944-26-000206 | Provision $125M vs net charge-offs $137M ⇒ total allowance **$2,184M → $2,172M (−$12M, a release)**. CFG attributes it to an improved loan mix (CRE office and multifamily). C&I allowance +$10M (generic C&I, excluded by rule R4). **The reserve for unfunded lending commitments rose $215M → $267M (+$52M) and CFG gives no category for it.** Deck p27: capital-call facilities $10.5B + private credit finance $4.5B = $15.0B. | **No fire.** The +$52M is **INSUFFICIENT**: linking it to capital-call commitments is my inference, which rule R3 excludes, so it waits for the call or the 10-Q. The book is not compared for growth, because the $12.852B baseline and REGINALD's $14.727B still disagree. |
| **MTB** 0000036270-26-000057 | Provision $135M vs net charge-offs $127M (Q2: $80M); allowance **+$3M**, with no category given. **Criticized loans +$245M**: C&I +$213M, "predominantly driven by a loan to an auto leasing company". This ends the nine-quarter decline in the Q2 baseline. | **No fire.** The borrower is unnamed, and it is a borrower rather than a private-credit vehicle (R5). |

5 of 11 banks have now been read. **OPEN 45%.** Calls were not consumed. Next: WAL 10/19, OZK 10/20, EGBN/BKU/SSB 10/21, AMTB 10/22. KB-BRK-350/351 · `AGENTS/BROCK/research/2026-10-16_BRK-31_MTB_CFG_read.md`.

## 3. CIK 799850 (America's Car-Mart) — the 10/15 16:59–17:30 ET gap
**Empty, VERIFIED** (JSON + Atom + index page): nothing was accepted after the 10/15 8-K (16:05:16 ET). The JSON clock is again 4 hours ahead. CRMT $1.12 (−17.04%) [fetch.py 13:37 ET]. L740 (the 10/22 scheduled-termination-date read) is unchanged. KB-BRK-349.

## 4. L0 drain — 7/7 (inbox_census: top-level 0 · WALTER/ 7)
| Signal | Disposition |
|---|---|
| SIG-W-20261016-002 (correction) | noted. My 10/15 board_log row had carried the "fourth failure" framing; it is withdrawn in the new row. COR-20261016-02 receipted APPLIED. |
| -005 Volta | noted (watch carried) |
| -006 AM tape | info-only |
| -008 Anthropic BB+ (ACTION) | deferred into the existing AI-infra financing leg, which stays deferred "on Will's ask"; not new-direction work |
| -014 CoreWeave founders | info-only |
| -017 Volta Bloomberg terms | noted |
| -019 Trepp | info-only |

⚠️ **-017 and -019 are untracked in my clone [as of 13:41 ET]**: WALTER has not committed them. They are logged as consumed, but `git mv` cannot move them, so they stay in `inbox/WALTER/`.

**Residue:** STATUS is at 73% of the read-cap budget, over the 70% target. A rotation by obligation is owed next session (it is in SCRATCH).
No score, threshold or trade moved; convergence 58/70; APO HOLD unchanged.

## COMPLETION
STATUS: DONE · D:L653 read (no filing; TRO press-only) · BRK-31 MTB/CFG no fire · CIK 799850 window empty · drain 7/7
CHANGED: BROCK STATUS/SCRATCH/KB(348–351)/CATALYSTS(+10/23 row)/PREDICTIONS(BRK-31 note)/board_log/catchup 10-16/research note/corrections receipt; WALTER packet
RESULT: CABO NOT CLOSED (10/9 CoBank TRO, Light Reading 10/12), EDGAR silent, $7.51 −11.39% @13:37 ET; BRK-31 5/11 read OPEN 45%; CRMT nothing after 16:05 ET 10/15
GAPS: SDNY docket unread (PACER); MTB/CFG calls not consumed; CFG +$52M unfunded reserve unattributed; -017/-019 untracked (WALTER); STATUS 73% > 70%
WILL_NEEDS: none
FOLLOW-UP: PROME — annotate L653, consider registering a 10/23 CABO row; WALTER — CoBank TRO intake; BROCK — WAL 10/19, CRMT 10/22, CABO 10/23
