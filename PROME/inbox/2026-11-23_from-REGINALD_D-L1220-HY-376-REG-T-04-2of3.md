# REGINALD -> PROME: D:L1220 done. REG-36 VOID encoded; HY 376 [11/20] puts REG-T-04 at 2 of 3; bank side still absent

**Row key:** D:L1220 (DOCKET physical line 1220, due 2026-11-23). **From:** REGINALD, Claude Code, Opus 5.5 (claude-opus-5-5), laptop; session id not exposed (scratchpad 834b3d2f). **Written:** 2026-11-23 12:16 ET (`date`). $0, no trade. No push (PROME pushes). **Priority:** 🟠 (a registered credit line is one print from firing).

**Boot (this spawn):** root CLAUDE.md, AGENTS.md, USER.md, PROME/COMPLETION_SPEC.md and AGENTS/REGINALD/CLAUDE.md, each read through `PROME/tools/boot_read.py` to `eof: true`: **5, 1, 3, 4 and 4 pages** (root CLAUDE.md also harness-injected, identical by `cmp`). Then STATUS, LESSONS, CALENDAR, MEMORY, ROADMAP whole. No pull: HEAD was 4 ahead, 0 behind origin at 12:05 ET, and other desks' tracked files are dirty (PROME, HENRY, BROCK). `boot.py` rc 1 (ALERT: thresholds, insider, FLG ladder, inbox lanes; no timeouts), `vx_ladder_check.py` rc 1 (FLG RED unchanged), staleness clean, corrections rc 1 → receipt COR-20261119-20 NO-OP → rc 0, peer channels 0 entries. **Gap:** the harness refused a separate `reports/` file for this session, so this memo carries the full read; my STATUS, CALENDAR, ROADMAP, MEMORY, TRADE and NEXUS brief point here.

## 1. D:L1220 assignment: what I found and what I did

| Ask | Found at 12:05 ET | Done |
|---|---|---|
| REG-36 marked VOID (superseded by REG-37), byte-preserved, no grade | **Not yet marked**: Status still `OPEN` (the ruling came 11/20, after my last session) | `workbook/PREDICTIONS.tsv` REG-36: Status `OPEN → VOID`, Date_Resolved `2026-11-20` (the ruling date, as REG-07's VOID used its ruling date), Outcome cell = VOID record with Will's verbatim word and the record path, "not scored, no grade", "neither 30% nor any outcome enters any Brier score". **Pred_ID, Date_Made, Prediction, Confidence 30%, Timeframe, Invalidation and Notes (with the 13:39 ET pointer to REG-37) byte-preserved**, checked by sha256 of each cell before and after. One header line prepended (the file's convention). Diff: 2 lines. Commit `3290faca41`. |
| REG-34 unchanged, exception named | Unchanged (25%, 11/05) | Not touched. Its near-miss clause is named as an exception wherever I cite it (STATUS HY row and predictions line, CALENDAR, NEXUS brief): if the third print is 349 or 350 and no later run follows by 12/29, REG-34 is NO-VERDICT, not FALSE. |

## 2. HY grade (FRED first-published via `fetch.py fred <ID> --first-published`, read 12:06 ET 11/23; latest-revised identical)

| Series | 11/20 | 11/19 | 11/18 | 11/17 | 11/16 | 11/13 |
|---|---|---|---|---|---|---|
| HY OAS | **376** | **352** | 347 | 343 | 334 | 323 |
| CCC OAS | **1,402** | 1,361 | 1,353 | 1,329 | 1,310 | 1,316 |
| B OAS | 408 | 380 | 373 | 368 | 357 | 344 |
| BB OAS | 229 | 210 | 205 | 204 | 196 | 186 |
| IG OAS | 98 | 94 | 93 | 92 | 90 | 89 |
| CCC/HY | 3.73× | 3.87× | 3.90× | 3.87× | 3.92× | 4.07× |

Your dashboard figures (376, CCC 1,402) and LIQUID's 352 match my read.

| Line | State after the 11/20 print |
|---|---|
| **`REG-T-04`** (HY > 350 on 3 consecutive closes, strict, first-published) | **NOT FIRED, 2 of 3** (352 [11/19], 376 [11/20]). **Next cell: HY [11/23], published about 08:00 ET Tue 11/24. Above 350 fires it** (ISSUANCE-FREEZE to LIQUID and Will, with the WQ-512 rider); 350 or lower resets the run to 0. |
| `REG-37` (30%, scored) | OPEN, 2 of 3; resolves TRUE on the same 11/23 print if > 350. Not re-marked (no re-mark is authorised, and one now would score hindsight). |
| `REG-34` (25%) | OPEN, 2 of 3, exception as in §1. |
| `REG-T-03` | FIRED, held; exit run 0. |
| CCC/HY tripwire | Still fired, **no escalation**: 11/20 was HY-led (HY +24, CCC +41), so the ratio fell 3.87 → 3.73. |
| Single-day move | +24 bp: one short of WALTER's +25 safety net (not my line). |
| WQ-512 rider | Runs only at a fire. Pre-read: for the level without named restructuring issuers to be 350 or lower, they would need to supply 26 bp or more of the move; CSC alone (0.47% of HYG [10/22]) would need about +5,500 bp. The widening is in every tier (since 11/13: BB +43, B +64, CCC +86). Expect "not issuer-driven"; computed formally at the fire. |

## 3. Bank-credit cross-check (my standing rule on a print above 350)

| Instrument | 11/17 → 11/20 (3 sessions) | Flip datum | Met? |
|---|---|---|---|
| Bank preferred basket (ZIONP, WAL-PA, OZKAP, VLYPO, VLYPP, CFG-PE, HBANL, HBANM, KEY-PI, TFC-PR) | **mean −1.14%**; ZIONP −2.62%, TFC-PR −2.39%; **no ex-dividends in the window** | −2% or worse over 3 sessions | NO |
| IG OAS (all IG; no free financials-only series) | +6 bp (92 → 98) | +10 bp, financials leading | NO |
| KRE vs SPY, settled (Yahoo and Nasdaq agree) | −3.57% vs −5.82%; on 11/20 alone −1.36% vs −3.64% | not a flip datum | banks fell less than the index |

**Read: BANK-ABSENT, weaker in direction** (basket −0.25% last week, −1.14% now, with the 10-year falling, which should have helped fixed-rate preferreds). The selloff is AI and chip-led (Nvidia −14% on 11/20 after Reuters reported SEC enforcement staff scrutiny of its accounting; WALTER SIG-W-20261121-001, VULCAN owns).

## 4. FORWARD VIEW: PROJECTION (my judgment; moves no score, gate or trade; unscored except REG-37)

- **Expect (~75%): the 11/23 print is above 350 and REG-T-04 fires at Tuesday's publication.** Why: to miss, HY must tighten 26 bp or more in one day; FRED's three years show that on 3 of 783 sessions (0.4%), and the cash index lags ETFs on rebound days.
- **Meaningful alternative (~25%): today's rebound pulls HY to 350 or below and the run resets.** Why: SPY is up 4.8% intraday (vendor, ~12:08 ET), the largest up-day in the sample but one; on the 5 days with SPY up 2.5% or more, HY tightened a median 18 bp and once 38 bp; a fitted 4.6 bp per 1% of SPY puts the print near 354, close to the line. HYG +0.39% with the 10-year up ~3 bp implies roughly 15 bp of tightening.
- **If it fires:** ~65% no exit (HY ≤ 330 on 5 closes) before 12/11. ⚠️ The ISSUANCE-FREEZE label is weaker than it sounds in Thanksgiving week, when new issues are thin anyway; whether deals are actually pulled is LIQUID's read.
- **For banks:** ~70% stays BANK-ABSENT through 12/11 (falling yields help bank books; banks outperformed on the worst day); **~30% (up from 25% on 11/19) the bank leg starts to lead**, because the preferred basket weakened with no dividend to explain it.
- **Horizon:** Tue 11/24 for the fire; 12/11 (REG-37) and 12/29 (REG-34); Fed Wed 12/9.
- **What would change my mind:** a financials-led IG move of 10 bp or more, a bank pulling a debt deal, or a bank naming loans to AI data-center or GPU-financing borrowers would move me to bank transmission; an 11/23 print at or below 350 would drop the fire to roughly a coin flip over the 13 remaining sessions, not to zero.

## 5. Other tape and filings (settled 11/20 unless marked)

WAL $67.90 (REG-T-02 FIRED, exit 0 of 3, log 58 rows through 11/20) · KRE $68.32 ($8.32 above the $60 line) · FLG $9.96, −30.1% vs FROZEN $14.24, 32 closes below RED · **FLG CFO Lee Matthew Smith bought 5,000 shares at $9.93 on 11/20** (Form 4, acc 0001582883-26-000006, read at EDGAR; third insider buy since 10/27; small, ~$49,650; KB ML-REG-318) · VIXCLS 35.89 · 10Y 5.04 [11/19] · no 8-K at my filers since 11/16. Today intraday (vendor, not graded): SPY +4.81%, KRE +1.30%, WAL +2.72%, HYG +0.39%.

## 6. Inbox drained: 6 packets, every sender

| Item | Disposition |
|---|---|
| PROME 11/20 WQ-722 ruling | INTEGRATED (§1); filed to processed (`a8cd5d9eda`) |
| TERRY 11/20 postmortem thesis-grade ask (3 cards) | ANSWERED by packet: WAL Sep-18 pair **WRONG** for its window (REG-26 disconfirmed at Q2, WAL $78.54 at 9/18); TRY-WAL-ROLL70 **UNRESOLVED** (price leg resolves at the 12/18 close; mechanism against it at the Q3 10-Q); IDEA-CREDIT-HYG-BDC-OCT23 **WRONG for its window** (peak 348 by 11/13), direction later borne out in part. Filed. |
| WALTER SIG-W-20261119-020 (correction) | INFO_ONLY; receipt COR-20261119-20 NO-OP |
| WALTER SIG-W-20261120-001 FLASH | INTEGRATED (HY 352 = run 1, graded with 376) |
| WALTER SIG-W-20261120-006 small items | INFO_ONLY; item 17 logged combo `re-modified-cre` (KB ML-REG-319) |
| WALTER SIG-W-20261121-001 LATE FLASH | INTEGRATED (settled WAL and KRE 11/20) |
| BOARD diff (CONSUMER_STAGFLATION info): 20261120-002, -003 | INFO_ONLY, no letter of mine |

BOARD_LOG 6 rows; the 4 WALTER cards are in `inbox/WALTER/processed/`.

## 7. TERRY (Will's standing word 2026-11-10)

Packet `AGENTS/TERRY/inbox/2026-11-23_from-REGINALD_REG-T-04-2-of-3-HY-376.md`: trigger state NOT-FIRED with the WQ-696 handoff sentence (implication, horizon, invalidation, unknowns); **bank leg: no candidate card**; the HY-leg expression is LIQUID's and TERRY's (TERRY holds LIQUID's IDEA-HYG-FOLLOW-NOV05, approved and unfilled to 12/04). WQ-724 (the QQQ card that used REG-T-04 failing as its filter) was declined by Will today, so nothing of mine rides on it. Commit `403c81cb0e` (with the postmortem packet).

## 8. Gaps and owed

- **Owed Tue 11/24 (~08:00 ET publication):** grade HY [11/23]. If it fires: the WQ-512 rider from the latest saved holdings file, the ISSUANCE-FREEZE consequence to LIQUID and Will, REG-37 and REG-34 resolved TRUE, cross-check re-run. This needs a REGINALD session Tuesday; D:L1220 already names the 11/23 cell.
- No financials-only IG spread read (no free series). H.4.1 and H.8 since 11/06 still not read.
- STATUS 26.4 KB, MEMORY 25.5 KB, NEXUS brief 27.2 KB (measure.py): under the 32,550 B cap; read_cap_check rc 0 with 9 rotations flagged due (advisory).

**Commits (local, unpushed):** `3290faca41` (VOID, ledgers, WALTER lane) · `403c81cb0e` (TERRY packets) · `a8cd5d9eda` (inbox filing) · `f1a68a2220` (STATUS, CALENDAR, ROADMAP, MEMORY, TRADE) · `62692737e8` (NEXUS brief) · this memo's commit.

## COMPLETION — REGINALD — 2026-11-23
STATUS: ✅ DONE
CHANGED: AGENTS/REGINALD/{workbook/PREDICTIONS.tsv, workbook/KB.tsv, registry/REG_T02_EXIT_LOG.tsv, registry/corrections_receipts.tsv, board/BOARD_LOG.tsv, STATUS.md, CALENDAR.md, ROADMAP.md, MEMORY.md, TRADE.md, NEXUS_BRIEF.md, inbox → processed (6)}; AGENTS/TERRY/inbox (2 packets); this memo
RESULT: REG-36 marked VOID on WQ-722 (cells byte-preserved, no grade); REG-34 untouched with its exception named. HY 376 [11/20] after 352 [11/19]: REG-T-04 NOT FIRED, 2 of 3; HY [11/23] > 350 fires it at Tue 11/24 publication. Bank cross-check BANK-ABSENT (basket −1.14%, IG +6bp, KRE −3.57% vs SPY −5.82%). Projection, unscored: fire ~75%, bank leg absent ~70%.
GAPS: 11/23 HY not yet published (Tuesday). No separate report file (harness refused it; this memo carries the read). No financials-only IG series.
WILL_NEEDS: None.
FOLLOW-UP: REGINALD session Tue 11/24 after FRED posts HY [11/23]: grade REG-T-04; at a fire run the WQ-512 rider and send ISSUANCE-FREEZE to LIQUID and Will.
