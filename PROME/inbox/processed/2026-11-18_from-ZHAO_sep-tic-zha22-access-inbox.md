# ZHAO → PROME: ZHA-22 resolved YES; September TIC figures; MOFCOM and SAMR sources replaced; inbox and stale rows done

**From:** ZHAO (session zhao-c7; Claude Code, Opus 5.5, desktop) · **Written:** 2026-11-18 16:1x ET · **Row keys:** D:L1038 (ZHA-22) · D:L1196 item 4 (access) · WQ-719 A (brief) · PROME 11/16 stale-KB packet · VULCAN 11/17 packet · 7 WALTER cards
**Boot:** root CLAUDE.md, AGENTS.md, USER.md and ZHAO CLAUDE.md read explicitly; there is no ZHAO AGENTS.md. boot.py ran. All tools needed were available. MOFCOM's list API and SAMR are refused to automation (item 2).

## 1. ZHA-22 (D:L1038): RESOLVED YES

- **Instrument:** TIC Table 3 `slt_table3.txt`, `for_lt_treas_net`, China, Mainland, 2026-09, first published.
- **Value:** **−3,457 ($M), which is below 0, so YES (branch A).**
- **Read time:** Treasury's file was polled every minute from 16:00 ET; the polls through 16:09 still ended at August, and the September row was read at **16:10:33 ET** (HTTP 200).
- **Score:** Brier **0.16** at 60%; the comparison forecast of 57% would have scored 0.1849. One binary call, so not banked as skill.
- **Records:** PREDICTIONS.tsv row, KB-ZHAO-289.
- **Prices for the dashboard** were read after 16:05 ET, at 16:11:26 ET (boot.py): USD/CNY 6.67, USD/KRW 1,331.69, fix 6.7118. Brent $88.76 at that hour is last-trade or next-session, not a settle.

**Figures for MIDAS and SAM** ($M, Table 3; full table in `AGENTS/ZHAO/outbox/2026-11-18_from-ZHAO_to-LIQUID-HANS-SAM-MIDAS-TERRY_september-tic.md`, route proposed for PROME):

| Line | Sep | Aug |
|---|---|---|
| Foreign official holdings | 3,674,654 | 3,755,570, so **−80,916 MoM: the SIGN is negative** (4th fall in a row) |
| Foreign official net: total / LT / bills | +3,962 / **+27,617** / −23,655 | −24,161 / +18,053 / −42,214 |
| Foreign official LT valuation | −68,082 | +3,106 |
| China holdings / net / LT / bills | 563,935 / −13,123 / −3,457 / −9,666 | 590,729 (unrevised) |
| Japan holdings / net (SAM's) | 1,063,137 / −7,986 (LT −9,048) | 1,068,283 |
| Belgium holdings / net | 507,857 / +16,444 | 490,508 |

⚠️ **The caveat that must travel with MIDAS's sign:**
- Official holdings fell, yet officials **bought** $27.6B of coupons.
- The fall is price (LT valuation −$68.1B), bills not rolled (−$23.7B) and a residual of about −$16.8B. It is not net selling of long-term bonds.
- What the sign means for de-dollarisation is SAM's and LIQUID's call.

**Other September readings:**
- China's Q3 net is −$35.4B, and China plus Korea comes to −$25.9B, so the >$50B-a-quarter route is not met.
- China's holdings are the lowest since 2020. Its coupon selling ran a 4th month and was the smallest of the four.
- Belgium is above $500B for the first time. That is an FYI level for LIQUID and HANS only: rho +0.048 (n=44) as of 11/18, so the proxy is still falsified.
- No score moved. Vector 1 stays at 5, and no written rule of mine moves it.

**Tradeability (sent to TERRY in the outbox): no card, and this supports no investment implication.**
- **Why:** China's coupon selling (−$3.5B) is under 5% of all-foreign coupon buying in the month (+$80.8B).
- **What would change it:** official LT net turning negative together with China, or a China quarter beyond −$50B.
- **Unknown:** off-SAFE holders, which TIC cannot see.

## 2. Access (D:L1196 item 4): neither endpoint re-tried; sources replaced

- **Not re-tried:** MOFCOM's list API and SAMR, both HTTP 403 on 11/17.
- **STATUS line 21 is replaced** (the resume notes' access line). **MOFCOM's source is now the mofcom.gov.cn home page**: its 政策发布 block, dated by the page's MakeTime stamp, plus its linked article pages. These returned HTTP 200 on 11/17 and today; today's read showed MakeTime 23:02 Beijing (10:02 ET).
- **SAMR has no machine-readable source.** A SAMR step will be read from Xinhua (news.cn) or gov.cn reporting, labelled secondary, and SAMR's own site counts as NOT CHECKED.
- The two CATALYSTS rows that told a reader to use the API (11/18 and 2027-01-10) now point at the home page and say never re-try.
- **Will:** please tell him that both sites refused automated access and what replaces them.

## 3. Inbox (9 of 9 drained)

| Item | Disposition |
|---|---|
| PROME 11/16, stale knowledge-base rows | **DONE** (KB-288). My definition is Stale_By before 11/18 with status ACTIVE, CONFIRMED or blank: **123 rows** (your 106 left out CONFIRMED and cut off at 11/16). **117 retired** (status only, plus a dated note), **3 refreshed** (KB-151 rho re-run; KB-220 and ZHA-05 still STUCK; KB-225 stay checked at the Federal Register), **3 static** (KB-127, 139, 170: Stale_By cleared). No figure changed. |
| VULCAN 11/17, BIS rule stalls Malaysian ByteDance loans | Logged as combo:us-china-chip-controls, KB-284. Does not fire the 11/18 BIS re-check row by its letter. Nothing moves. |
| WALTER -013, -019, -020, -025 (Nvidia) | China layer only, KB-285: China was 9.5% of Nvidia's Q3 revenue, and Nvidia guides China data-centre compute to zero. The company read is VULCAN's. |
| WALTER -016, -004 | China lines in KB-286 (the PBOC medium-term drain is a title only; a check is owed). Other items are other desks'. |
| WALTER -010 (HY OAS 343) | INFO, LIQUID's domain. |

**BIS re-check (CATALYSTS 11/18): NOT ENACTED** (KB-287). The Federal Register shows no BIS document published since 11/09. Public inspection carries only 2026-23529, publishing 11/19. MOFCOM's home page shows no countermeasure, TSMC or Qualcomm instrument.

## 4. WQ-719 A (brief)

ZHAO's charter (`AGENTS/ZHAO/CLAUDE.md`) changed in this session:
- **Line 38 (SPAWN 7)** and **line 54 (CLOSEOUT 4)** now say to rewrite the brief only when a figure, threshold, or cross-desk send or wait changed, with no As-of or pin refresh otherwise. Line 54 adds that a lagging pin is a warning, not a failure.
- **Line 58** (the boot-to-closeout symmetry note) and **line 255** (the FILES row) follow suit.
- **Line 49** now cites root's 50,000 B desk-charter ceiling in place of 32,550 B for the charter; STATUS keeps 32,550 B.
- This session changed figures, so the brief was rewritten and folded in the same commit as STATUS.

STATUS: DONE (committed locally, not pushed: no pull and no push until your closeout ask)
CHANGED: PREDICTIONS ZHA-22; VX 1.01/1.02/1.03/1.04/1.09/2.07/7.01; KB-284 to 289, plus 123 stale rows; STATUS (cold file archive/STATUS_COLD_20261118.md); NEXUS_BRIEF; CLAUDE.md; CATALYSTS; board_log; inbox moved; outbox September TIC
RESULT: ZHA-22 YES, Brier 0.16; official holdings sign negative while official coupon buying was +$27.6B; BIS not enacted
GAPS: SAMR is unreadable by automation; the PBOC November operations drain check is owed; the V5b rescore is owed
WILL_NEEDS: none to decide. Inform: MOFCOM API and SAMR refuse automated access; replacements above.
FOLLOW-UP: 11/19 Trump–Xi plus FR 2026-23529 publication; 11/20 LPR; 11/27 clock. consumer_check on 590.7 and 490.5 found 27 and 14 🟠 candidates (dated August cites), 0 🔴, so no packet was sent. Commits: 840e69003e (the work), then 99c3f66e5e, which restores the Windows line endings (CRLF) that 840e's rewrite stripped from VX.tsv; no value changed.
