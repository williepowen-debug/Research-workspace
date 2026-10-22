# OZK → PROME — 2026-10-22 · D:L520 Q3 call Stage-2 READ · D:L463 post-event check · D:L588 / D:L763 dates · catch-up done

**Row keys:** D:L520 (WQ-313 ③) · D:L126/D:L463 · D:L588 · D:L763. **Desk commits:** ee6829772 (Stage-2 + state), e9ffef117 (WALTER 011 filed). Full read → `AGENTS/OZK/research/threads/2026-10-22_Q3_CALL_STAGE2_READ.md`; card RESULTS appended to `AGENTS/OZK/workbook/Q3_2026_SCORING_CARD.md` (pre-print text untouched).
**Source:** the 10/21 call is a **secondary** transcript: TradingKey `tradingkey.com/news/transcripts/262229860-tradingkey`, extracted-text sha256 `4fae2fec5cf79d48ae3a050cf6931008348c12e0bd88151e3cff0ea201924640`, read whole. Cross-checked against Investing.com (same analysts, same quotes). **Not stored in the tree** (public repo, Will option A); short quotes only. ⚠️ **Quartr is NOT available:** the MCP returns `subscription_required` (Quartr Pro) on this account. It is a plan gap, not an auth gap.

## D:L520 — Stage-2 graded

| Stage-1 PENDING item | Call result | Status |
|---|---|---|
| Special mention −$313M flow | Not itemized ("a clear positive", CFO) | **UNKNOWN → 10-Q (L763)** |
| RaDD rating | CEO: "[a] pass credit on our books" | pass, now **SPOKEN** (was by elimination) |
| RaDD reserve / readvance | Neither mentioned; nobody asked | **OZK-09 OPEN/STUCK** |
| 45-day bridge | Extension structure agreed first; the 45 days let mezz + equity agree future capital contributions "if needed" | ⚠️ more capital calls are anticipated |
| RaDD leasing | "lab demand is not what it was"; marketing widened to office/non-lab; no lease | no lease |
| OREO $420M / Boston | Buyers on all 7 main properties except Atlanta (leasing); "appropriately valued"; "several quarters"; no price | **no OREO sale priced** |
| Sullivan | Not mentioned | PENDING 10-Q |
| Loss outlook | MC p.21 (primary): NCO may "remain elevated" 2026–27, "improving trend in 2027"; CEO: cycle "largely behind us" by YE-2027 | earnings drag, not capital event |

**Net:** the call adds nothing toward stress and closes no open leg. New contrary items: Oct 1–19 RESG payoffs ≈$690M with Q4 "perhaps record", driven by debt-market liquidity (Hamblen); OZK is below the 300% CRE guideline; the reported Portico (Oakland) sale was a full payoff. Tape: 10/21 close **$48.09 (+4.18%, KRE flat, 1.84× volume)**, so the move was stock-specific. Short interest 9/30 **17.60M ≈17.4%** of float.

⚖️ **P-OZK-7 (Will-gated, NOT applied): conviction 🔴🔴 HIGH → 🟡 LOW.** Its two Q2 legs are gone: the RaDD maturity catalyst (executed extension, CEO-stated pass) and the adverse-selection conjunction (C&C −22% while RESG −1%). The residual thesis would be "OREO and Boston marks untested by sales; losses elevated through 2027; earnings drag." If approved, the desk writes THESIS v1.7 + CHANGELOG. **No prediction weight, threshold or scenario number moves.** Reversal triggers: an OREO sale well below carrying, SM migrating into classified in the 10-Q, a RaDD reserve or readvance, or `RIAD5409` charging off again.

## D:L126 / D:L463 — sub-notes post-event check (3 weeks late; now done)

`flng_watch.py` 2026-10-22 ~11:05 ET: only 12019 (10/12 8-K) and 12022 (Q3 bundle) after 11981. **No redemption or refi filing.** The issuer itself confirms the reset (Q3 MC p.35, primary): **6.14% for Q4-26**, Q4 NIM −3bp, Tier 2 −20%, callable at par each quarterly date. This supersedes the desk's ≈6.19% / ≈$12.3M estimate (now ≈$12.0M/yr). **Recommend L463 → RESOLVED.** REGINALD's 6.14% consumer packet was APPLIED to CALENDAR, SCENARIOS, WEAKNESSES and KB_INDEX (→ processed).

## D:L588 / D:L763 — dates confirmed at the primary

| Row | Date | Basis |
|---|---|---|
| L588 call-notice window | **Mon 11/2 → Tue 12/22** for a par call on 2027-01-01 | Fiscal Agency Agreement §8: at least 10, no more than 60 days' notice (read 10/1, `research/threads/2026-10-01_SUBNOTES_RESET.md`). A notice need not be FDIC-filed; press check too |
| L763 Q3 10-Q | **~Thu 11/5** (the row says 11/6) | FDIC `instflng` index: Q3 10-Qs filed **11/5/2024** (11600) and **11/5/2025** (11823). ⚠️ The same day the FFIEC JWT expires (Will's action), which gates the Call Report pull |

## News since 10/21 / WALTER lane

- SIG-W-20261021-003 (Boston failed sale) was **OZK-originated**, already consumed in the Stage-1 grade W9 (board_log 10/21).
- After-close 013 set: nothing routed to OZK. EGBN (013: NPA $166.0M, 76% of inflows from one loan; NCO 0.25%) and ZION (009: classified −$204M) printed the **same direction** as OZK, so part of OZK's Q3 improvement is cohort-wide. EGBN's call was not read (REGINALD/RED own the comp).
- SIG-W-20261022-011 (HBAN/VLY/SSB) filed noted: OZK fits WALTER's reserve-thinning shape (ACL ratio −~4bp/qtr while MC guides NCO elevated). Diagnostic only.
- For REGINALD on Will's 005 question (does HY widening reach regional banks?): OZK's main de-risking mechanism right now is **refinance payoffs from liquid debt markets** (Hamblen, 10/21). Sustained credit widening is the variable that would slow it. That is OZK's single-name angle; the cohort read stays REGINALD's.
- EFR cert 110: no insider filing after 8/14. No other OZK-specific news found (web, 10/22).

## Shared-index note

My staged `git mv` of the REGINALD inbox packet was committed inside **WALTER 5854ecb98** (it swept the shared index). The result is correct (R100 to `processed/`), and nothing was lost. Flagged as a fact only.

## COMPLETION — OZK — 2026-10-22
STATUS: ✅ DONE (L520 Stage-2); ⚠️ OZK-09 and SM flow remain OPEN until the 10-Q
CHANGED: AGENTS/OZK/{STATUS,CALENDAR,MEMORY,INDEX,TODO,SCENARIOS,WEAKNESSES}.md, LIFE_SCI/STATUS.md, workbook/{KB.tsv,KB_INDEX.md,Q3_2026_SCORING_CARD.md}, scripts/boot.py, board_log.tsv, research/threads/2026-10-22_Q3_CALL_STAGE2_READ.md, 2 inbox→processed; this packet
RESULT: Stage-2 read; nothing toward stress, no leg closed; P-OZK-7 proposed; L463 check clean; L588/L763 dates confirmed (L763 → ~11/5)
GAPS: Quartr needs a paid plan; SM flow, RaDD reserve, Sullivan → 10-Q; EGBN call not read
WILL_NEEDS: P-OZK-7 word (conviction re-grade); FFIEC JWT renewal by 11/5 (existing)
FOLLOW-UP: re-date D:L763 to ~11/5; resolve D:L463; spawn OZK at the 10-Q
