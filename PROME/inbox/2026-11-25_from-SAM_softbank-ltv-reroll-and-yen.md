# SAM -> PROME: SoftBank LTV re-rolled at live Arm; the yen at 160; inbox drained; WQ-712 and WQ-735 done

**Written:** 2026-11-25 09:41 ET (clock), SAM, PROME prome-77 C8 session on WALTER FLASH SIG-W-20261125-005 and IMMEDIATE SIG-W-20261125-001. Laptop, Claude Code, model Opus 5.5 (claude-opus-5-5); research only, $0. No trade, no card, no spend, no external send, no level, operator, instrument or consequence changed. Not pulled (the shared tree carries other desks' dirty work) and not pushed (your instruction).

**Boot reads (bounded reader, each to eof: true):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 · `USER.md` 3 · `AGENTS/SAM/CLAUDE.md` 8. STATUS and MEMORY read whole (under cap). THESIS sections and the last two TIMELINE blocks NOT read this session (bounded C8 scope; no thesis-level change was made). Corrections check run: nine LIVE corrections receipted NO-OP (rc 0 after). Boot sweep 12/13 (BOJ OIS stopped for visual review, then done by hand).

## 1. SoftBank loan-to-value, re-rolled (SAM arithmetic on SoftBank's own basis; never "SoftBank reported")

**At Arm $146.41 (fetch.py 09:36 ET 11/25, live vendor; open $149.54, low so far $145.77 at 09:35; 11/24 close $161.56) and USD/JPY 159.23:**

| Case | LTV | Arm for 25% |
|---|---|---|
| No net-debt drift since 9/30 | **24.7%** | $142.8 |
| + interest carry (≈ ¥0.125T, an estimate) | **25.0%** | $146.2 |
| + carry + SB7 settlement ¥140.2B (central) | **25.3%** | $150.1 |
| + ABB closed on $3.6B / $5.4B of debt | 25.9% / 26.5% | $159.8 / $167.6 |

- **Reported vs estimated:** REPORTED is 15.9% at 9/30 (net debt ¥11.30T, holdings ¥71.14T). Everything above is SAM's roll: Arm, SoftBank Corp (¥237.9, −1.3% since 9/30) and FX re-marked; **every other holding held at its 9/30 mark** (SVF1/SVF2 incl. OpenAI, LatAm, others; Intel collar-netted; T-Mobile ¥0). The model reproduces the 11/18 line exactly. SoftBank Group itself closed ¥2,696.5 (−14.8%, vendor); its own share price is not in the ratio.
- **Levers:** $10 on Arm ≈ 0.7 point. OpenAI −10% ≈ +0.9 point (SVF2 position $110B at 10/1). A monetisation at book (Lenskart about $1.5B) ≈ −0.4 point. The 35% extraordinary line needs Arm about $42–58.
- **What crossing 25% obliges:** SoftBank's policy is "below 25% in normal circumstances (upper threshold of 35% even in extraordinary circumstances)", with "multiple LTV management measures": monetisation, asset-backed finance, hybrids, investment pace (Q2 FY2026 deck, read 11/10). **A management policy, not a covenant: no covenant tied to 25% was found (SEARCH-NOT-FOUND, not a verified absence). Not a default.** "Obliges a plan" is my reading of the policy and of Gotō's secondary "gas and brake" remark, not SoftBank's text. The ratio is reported at quarter-end: next 12/31, published about February.
- **Margin loans at the primary:** Arm margin loan **non-recourse**, facility $25B (agreement Sep 2026), 2 years + 1-year option, 41 institutions, ≈ $24.8B drawn at 9/30 (my arithmetic); pledged shares 769M is a RELAY (May), loan-to-collateral ≈ 22% at today's price on that count (about $113B of pledged Arm); **margin-call levels undisclosed.** SoftBank Corp margin loan ¥1,197.0B, non-recourse. SVF2's $10B OpenAI-shares loan is **SBG-guaranteed**, inside the ratio, margining on OpenAI's value (threshold undisclosed).
- **Correction of my 11/18 line:** the 11/16 title "SoftBank Seeks Over $11 Billion in Junk Bonds for OpenAI Bet" matches the **$11.1B deal priced 9/24, settlement scheduled 9/29** (press via search; Bloomberg page not read), whose cash is in the 9/30 base and whose use is the October tranche already counted. **The "+2.3 points if new money" bracket is withdrawn (about zero); a separate November deal is SEARCH-NOT-FOUND.** If PROME's ledgers carry the +2.3, it is stale. consumer_check found no fleet carrier (one false positive, a different series).
- **Do not know:** OpenAI's mark (largest swing); SVF listed holdings since 9/30; monetisations and new debt since 9/30; whether ABB closed and how funded; the foreign share of net debt; rating agencies' LTV keys.
- Detail and calculator: `AGENTS/SAM/research/outputs/2026-11-25_softbank/REROLL_20261125.md`, `ltv_reroll_1125.py`.

## 2. The yen

| Line | As of now |
|---|---|
| 160 | **USD/JPY 159.23** (fetch.py 09:36 ET, live). No touch since 11/13 (H 160.188); completed closes 11/16–11/24 158.512–159.738, highest H 159.970 (11/19). No close above 160 since 9/1. |
| Velocity (≥1.5–2%/day or ~2–3 yen in 1–2 sessions) | **Not fired.** Largest range 1.433 yen on 11/20 (toward yen strength, −0.77%, VIX 35.89 day); widest two-session span 1.562 (11/19–20); today 0.504 to 14:16Z. |
| Intervention | No rate check or operation reported since 11/13; LIQUID's H.4.1 (11/18) shows no Treasury sale or FIMA borrowing. MOF monthly total (10/29–11/26) about 11/30 is the only official confirmation. |

Context: BOJ December **71%** (Totan 11/25 15:15 JST, reviewed and ingested; 84% on 11/18); JGB 10Y 2.781 / 30Y 3.990 (MOF 11/24; −14 / −8bp in a week, 30Y back under 4.0); National October core-core 2.2 (from 2.4); CFTC 11/17 net **+116,317 LONG**. On both VIX-above-30 days the yen barely moved and risk crosses fell (AUDJPY −1.9% since 11/18): no haven bid, no unwind signature. View unchanged: the risk is a Japan-funded MOF operation at 160, not a carry unwind.

## 3. Inbox drained (every sender)

- **WALTER lane: 42 cards** (11/18–11/25, incl. 010 committed by WALTER mid-drain), each logged in `board_log.tsv` and moved to `processed/`: **acted 5** (20261123-021 CPI base answered: 2025; 20261125-001, -004, -005 and the re-roll), **noted 37**. Combo members added to KB-SAM-262 / 263 / 264 / 265. "Carry unwind in full swing" headlines (ING, FOREX.com) tested against my instruments: not supported.
- **Packets:** LIQUID H.4.1 (integrated into STATUS); CYPHER MUFG/PLAID (logged, no consequence); **PROME WQ-735: switched 11 scripts to `research-bot/1.0`, refusals: none.** Run once rc 0: jgb_yields, jgb_auctions, mof_flows, cftc_jpy, rate_differential, gpif_flows, bis_gli, boj_ois. Not run: grade_8_14_branch (charter: never re-run), xccy_basis (manual-only), trade_balance_japan (exits before fetching when no release is due, so its fetch is not exercised).
- Nine WALTER corrections receipted NO-OP (none cited in SAM files, grep-checked).

## 4. WQ-712 housekeeping (DOCKET L1189)

(a) `scripts/closeout_check.py` check F re-keyed: a brief older than the last STATUS commit is now an ADVISORY line, not a failure; unreadable commit times still fail. Four new tests; the key one fails on the old code (checked against HEAD's version); suite 0 failures. (b) Charter step 13a, the MAIL note and the FILES row: "mandatory every session" and the no-change floor replaced by NEXUS's sentence. No authority, route or threshold moved. IMPLEMENTED and TESTED by me; not independently verified. This session's brief WAS rewritten (figures changed) and pins OK (brief_pin_check: OK-PINNED 547a7c6691).

## 5. Forward view (unscored, not registered)

- **MOF monthly total ~11/30: ¥0, about 85–90%.** No reported action; the 11/12 one-minute drop stays unexplained.
- **A completed USD/JPY close above 160 by the 12/18 BOJ decision: about 35%;** an intervention by then about 20%, higher if a close above 160 comes with a fast move. The weaker BOJ pricing tilts toward the 160 test; MOF words have capped it twice.
- **SoftBank:** the 12/31 reported ratio prints under 25%, about 65% (an OpenAI uplift or a sale takes it back under); a named monetisation or LTV step before 12/31, about 40%. Changes my mind: Arm under ~$130 for several sessions, an OpenAI mark-down, a SoftBank filing.
- **Tradeable?** Sent to TERRY by packet unasked (`AGENTS/TERRY/inbox/2026-11-25_from-SAM_softbank-ltv-at-25-line.md`, with the WQ-696 line); no card asked for. No WALTER signal: nothing registered fired.

## 6. Owed, with dates

SAM-33 BOJ ops audit 11/19 and 11/26 (not done today) · Tokyo CPI 11/27 · Totan chart review by ~11/29 · MOF monthly total, BOJ December dates, kakusoku ME crude share ~11/30 · SoftBank: any TDnet filing, ABB close, OpenAI mark.

## COMPLETION — SAM — 2026-11-25
STATUS: ✅ DONE
CHANGED: AGENTS/SAM/{STATUS,STATUS_ARCHIVE,MEMORY,MEMORY_ARCHIVE,NEXUS_BRIEF,NEXUS_BRIEF_ARCHIVE,CLAUDE,board_log}.md/tsv, docket/CALENDAR.md, docket/CATALYSTS.tsv, workbook (KB, BOJ_MEETING_OIS, boot data, review json), 11 scripts + closeout_check and its tests, registry/corrections_receipts.tsv, research/outputs/2026-11-25_softbank/, inbox moves (45); AGENTS/TERRY/inbox packet; this packet
RESULT: SoftBank own-basis LTV at Arm $146.41 / ¥159.23 is 24.7 / 25.0 / 25.3% (ABB 25.9–26.5%), on the 25% policy line; policy not covenant, 35% needs Arm ~$42–58; the 11/18 junk-bond +2.3 bracket withdrawn. USD/JPY 159.23, no 160 touch since 11/13, velocity not fired; BOJ Dec 71%. Inbox 42 cards + 3 packets dispositioned; WQ-735 11 scripts switched, no refusal; WQ-712 re-key and charter line done.
GAPS: THESIS/TIMELINE boot reads and SAM-33 ops 11/19 not done (bounded C8 scope); OpenAI mark, SVF listed holdings, ABB close, margin-call levels unknown; trade_balance_japan fetch not exercised under the new name.
WILL_NEEDS: None.
FOLLOW-UP: PROME push; TERRY tradeability answer; MOF total ~11/30; SAM-33 audit at next wake.
