# ZHAO → PROME — L0 drain, DOCKET L223 Plenum confirm, China-side read of the 10/22 selloff, L482 pre-fetch

**Date:** 2026-10-22 (Thu), session ~13:25–13:45 ET · **Spawn:** PROME prome-25, WQ-487 RULED A · **Runtime:** Claude Code, Opus 5.5 (claude-opus-5-5), Agent-tool teammate spawn.
**Boot reads (bounded reader, every file to `eof: true`):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 · `USER.md` 2 · `AGENTS/ZHAO/CLAUDE.md` 6 · `STATUS.md` 5. boot.py run (REVIEW: 7 key-figure ages stale >14d; not all refreshed, see GAPS). Corrections check rc 0.
**Records:** KB-ZHAO-206 (Plenum + NPCSC) · 207 (selloff read) · 208 (L482 pre-fetch) · 209 (drain) · CATALYSTS new row (NPCSC 11/2–6) · board_log ×3 · STATUS + NEXUS_BRIEF.

## 1. L0 drain: whole inbox, 3 of 3 (root lane empty)

| Signal | Disposition | Note |
|---|---|---|
| SIG-W-20261020-020 (gold net exports; Aug TIC flows) | info-only | TIC figures match ZHAO's own 10/16 pull (KB-197). No foreign-Treasury-exit inference drawn; gold is MIDAS's. |
| SIG-W-20261020-027 (DeepSeek–Huawei chip design) | info-only | VULCAN's action. No export-control instrument changed: Federal Register BIS documents since 10/20 = 0. |
| SIG-W-20261022-002 (Asia selloff 10/22) | acted | §3 below, KB-207. |

All three logged in `board_log.tsv` and moved to `inbox/WALTER/processed/`; the commit carries `consume:ZHAO`.

## 2. DOCKET L223: Fifth Plenum. **Dates and agenda CONFIRMED; narrow the row to 10/26–29.**

| Item | Finding | Source / grade |
|---|---|---|
| Dates | **2026-10-26 to 10-29, Beijing** | Politburo 2026-09-21 (Xinhua via english.www.gov.cn, KB-195, A1); re-confirmed today: CGTN 2026-09-21, SBS |
| Agenda | Central Committee **decision on strengthening full and rigorous Party self-governance**. Not the five-year plan (the 2025 Fourth Plenum adopted that). | Xinhua 2026-07-30 via english.www.gov.cn; Qiushi 10/15 ran Xi's article on the same theme |
| 🆕 The legal venue for a fiscal number | **NPC Standing Committee 25th session, 11/2–6.** Set today by the 74th Council of Chairpersons meeting. The proposed agenda has **no budget adjustment, no extra debt quota and no special treasury bond item**. It does include a Financial Law draft and a State Council report on financial work. | Xinhua news.cn, 2026-10-22 19:47 Beijing, A1 |

**Recommendation: PROME narrows L223 to 10/26–29.** The communiqué is expected on the evening of 10/29 Beijing time (morning of 10/29 ET). ZHAO grades inside the window. I also suggest PROME **register the NPCSC 11/2–6 session as the successor venue** for the "saved not withheld" branch. ZHAO's CATALYSTS row is written.

**What a CSI 300 bear market going into the Plenum changes for ZHA-15's "saved not withheld" branch:**
- **Odds of a large RMB fiscal figure by 11/6: LOWER, not higher.** Both venues in the next 15 days point away from one. The Plenum points away by its agenda, and the NPCSC by its proposed agenda. Q3 GDP at 4.5% beat expectations, which reduces urgency (Maybank, via Yahoo/BeInCrypto). My working estimate is about 10%; it is **not registered** as a forecast.
- **Odds of equity-market support (state-fund ETF buying, CSRC measures, PBOC equity facilities): HIGHER.** A stock drawdown historically draws market-support tools, not a budget outlay (INFERRED).
- **Evidence that would raise the fiscal odds:** (a) a budget-adjustment or debt-quota bill added to the 11/2–6 agenda. I remember the October 2023 one-trillion-yuan bond revision as a late addition to an NPCSC agenda, but I did **not verify** that this session. (b) A Plenum communiqué economic paragraph that carries a concrete RMB figure. (c) A finance ministry press conference announcing a new bond quota.
- **Evidence that would lower them:** the communiqué says nothing on the economy and the NPCSC closes 11/6 with no budget bill. The venue then moves to the December Politburo and Central Economic Work Conference.
- ⚠️ A future registration of this branch needs a **size floor in new outlay**. ZHA-15's original bar had none (KB-125).

## 3. China-side read of the 10/22 selloff (KB-207)

| Question | Finding | Grade |
|---|---|---|
| Index basis | CSI 300 closed **4,036.30, −1.91%** and the Shanghai Composite **3,658.03, −1.48%**. The **"bear market" uses the intraday high.** On closes, the CSI 300 ETF (510300) peaked at 5.091 on **6/22**; with today's move it is **about −19.4%**, at the line rather than clearly through it. The Hang Seng was −3.03% to 22,934.68, −18.0% from its 1/29 peak. | VERIFIED (fetch.py/yfinance 13:26–13:31 ET); drawdown INFERRED via the ETF proxy |
| PBOC | **No 10/22 statement.** The news list's newest item (10/21) is a commemorative-coin notice. Pan's 10/19 Financial Street Forum speech, read whole at pbc.gov.cn, covered: a liquidity backstop for non-bank mass redemptions (**bond** market, with NFRA and CSRC); a wider SLF; an interbank–exchange bond connect; 8 offshore clearing banks admitted onshore; a possible move of the main policy tenor to overnight; and an exit from benchmark rates. **No rate cut, RRR or equity signal.** The LPR was held on 10/20 for the 17th month. | VERIFIED at primary |
| CSRC / MoF | Wu Qing spoke on 10/19 (before the drop): 18 active ETFs, buybacks, "consolidate stabilisation mechanisms" (SCMP, secondary). The market did not respond. **No 10/22 CSRC or MoF statement found.** | B2 / SEARCH-NOT-FOUND |
| State buying ("national team") | **No Huijin statement found.** Volume on 10/22 against each fund's 20-day average: 159919 **12.7×**, 510330 **6.0×**, 510300 **3.5×**, 510050 **3.2×**. These are the broad-index ETFs Huijin has historically bought, so the volume **fits state buying but does not prove it.** Volume is not net creation. Bloomberg Intelligence (one note, 10/22): Huijin **sold** about $231B of ETFs in H1 and has redeployed only about $43B since July. | INFERRED. The test is ETF share-creation data (T+1). |
| Capital flight? | **No.** USD/CNY 6.66 and CNH 6.67, both about 0.0%. This is a domestic equity and AI-valuation drawdown, not money leaving China. | VERIFIED (live) |
| Chips / export controls | SMIC −6.1%. CXMT is −27% from its post-listing peak. MetaX and Moore Threads are each down about half (Investing.com). Every report read names AI-valuation doubt as the driver. **No new control instrument:** Federal Register BIS documents since 10/20 = 0. The 10/27 BIS Entity-List re-check stands. CXMT capacity is VULCAN's. | B2 + VERIFIED absence |
| Taiwan posture | **Unchanged.** Lai's 10/10 speech drew a TAO rebuke, and PLA live-fire notices in four seas ran 10/12–20 (Reuters/US News 10/11). Nothing found for 10/21–22. TAIEX −1.81%. The military read is HAWK's. | B2; 10/21–22 SEARCH-NOT-FOUND |

**New lead, not chased:** the PBOC published a **policy-position document on the yuan on 10/8** (Xinhua). Pan's 10/19 summary: "no need and no intention" to devalue, intervention only in extreme scenarios, and acting to prevent overshooting toward depreciation. This is direct evidence for the owed two-directional re-spec of Vectors 6 & 9 (STATUS NEXT #4). I did not read the primary this session.

## 4. DOCKET L482 pre-fetch (report only, not graded; the registered date is 10/27)

**There is still no instrument for the 2027-01-10 extension.** Federal Register, published since 10/20: BIS 0, USTR 0. Presidential documents: 2 (women's health; the Graham Act EO already read 10/20). A search for "January 10, 2027" returned 0. Public inspection on 10/21 and 10/22 had no China, BIS or USTR item. On whitehouse.gov the newest action is 10/19, with nothing on China. MOFCOM's newest is a 10/20 wool-quota notice; 公告49–52 date to 10/19, and none re-suspends 公告70. The Tariff Commission returned **502 again**. **Both 11/10 clocks stand, 19 days out.**

## 5. Not changed
No score, threshold, mark or prediction moved. The total is 28/60. No trade idea, so no TERRY packet. STATUS dashboard: only Brent ($112.46 live; contract label UNKNOWN, WALTER says Dec) and USD/CNY were refreshed.

---
**COMPLETION**
STATUS: DONE. L0 drain 3/3; L223 confirmed; selloff read; L482 pre-fetch.
CHANGED: KB-ZHAO-206..209 · CATALYSTS +NPCSC 11/2–6 · board_log ×3 · 3 signals → processed (consume:ZHAO) · STATUS · NEXUS_BRIEF.
RESULT: Plenum 10/26–29, agenda Party discipline (A1) ⇒ narrow L223. NPCSC 11/2–6 has no budget item ⇒ fiscal-figure odds LOWER into 11/6; market-support odds higher. Selloff: no PBOC/MoF statement; CSI 300 about −19.4% on closes; ETF volume 3–13× fits state buying (unconfirmed); yuan flat; Taiwan unchanged. L482: no instrument.
GAPS: CSI 300 index history not on yfinance (ETF proxy used). No ETF share-creation data. Huijin/CSRC 10/22 SEARCH-NOT-FOUND. Tariff Commission 502. PBOC 10/8 yuan document not read at primary. boot.py staleness (HK peg, HIBOR, PMI) not refreshed.
WILL_NEEDS: none.
FOLLOW-UP: PROME narrows L223 to 10/26–29 and considers a row for NPCSC 11/2–6. ZHAO grades the communiqué ~10/29, re-checks L482 on 10/27, and checks 510300/159919 share creations at the next touch.
