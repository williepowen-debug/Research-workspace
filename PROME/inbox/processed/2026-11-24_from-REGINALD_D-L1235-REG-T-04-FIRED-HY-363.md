# REGINALD -> PROME: D:L1235 done. REG-T-04 FIRED on HY 363 [11/23]; not issuer-driven; bank side still absent

**Row key:** D:L1235 (DOCKET physical line 1235, due 2026-11-24). **From:** REGINALD, Claude Code, Opus 5.5 (claude-opus-5-5), laptop; session id not exposed (scratchpad 8c139b72). **Written:** 2026-11-24 22:40 ET (`date`). $0, no trade proposal, no push (PROME pushes). **Priority:** 🔴 (a registered credit line fired). **Lateness:** this wake is a day late because PROME's session was offline from about 20:55 ET Mon 11/23 to 22:20 ET Tue 11/24; no desk ran on 11/24.

**Boot (this spawn):** root `CLAUDE.md` 4 pages, `AGENTS.md` 1, `USER.md` 3, `AGENTS/REGINALD/CLAUDE.md` 4, each through `PROME/tools/boot_read.py` to `eof: true` (root's Git Protocol section printed and read in full after tonight's WQ-744 trim; `docs/GIT_WORKTREE_PROCEDURES.md` read whole before the first commit). `PROME/COMPLETION_SPEC.md` read for the delivery section and the block template only (grep and line ranges, not whole). Then STATUS, LESSONS, CALENDAR, MEMORY, ROADMAP whole. No pull: 0 behind origin after `git fetch`, and PROME's tracked files are dirty. Corrections check rc 1 → receipt COR-20261123-03 NO-OP → rc 0. Staleness: one ledger behind STATUS (`WORKOUT_OUTCOME_BRIDGE.tsv`, +32 days, untouched by this task). **Not run:** `boot.py`, `market.py`, `vx_ladder_check.py` (settled closes came from `settled_bars.py` instead; FLG $10.22 [11/23] is still below its RED band).

## For Will, in plain words (PROME relays)

**What fired:** the high-yield bond spread, which is the extra yield investors demand to hold riskier company bonds instead of Treasuries, closed above 3.50 percentage points for three trading days in a row: 3.52 on Thursday 11/19, 3.76 on Friday 11/20 and 3.63 on Monday 11/23 (ICE BofA index at FRED, first-published values). That meets my registered rule REG-T-04, whose label is "issuance freeze": a spread this wide usually means weaker companies find it hard to sell new bonds.

**What it means:** broad corporate credit is under real strain, at the level I set months ago as the point to say so. It is also the condition behind the credit idea TERRY already holds from LIQUID; TERRY has been asked whether anything is tradeable now.

**What it does not establish:**
- **Not bank stress.** Over the same three days, bank preferred shares rose 0.61% on average, the investment-grade spread widened only 0.04 points, and the regional bank fund (KRE) fell 1.39% against 1.08% for the S&P 500 fund. Banks are moving with the market, not leading it. The selloff has been led by AI and chip stocks.
- **Not that new issues are actually shut.** That is LIQUID's read (are deals being pulled), not yet made.
- **Not one company's troubles.** The rule Will approved on 10/23 (WQ-512) makes me check whether a single restructuring company drove the cross. The obvious one, Optimum (CSC Holdings), skipped about $102.5M of bond interest due 11/16 and is in a 30-day grace period. It is 0.47% of the main high-yield ETF; to account for the cross alone its bonds would have had to widen about 27.7 percentage points in three days, its news was public before the window began, and the highest-quality slice of the index, which holds no Optimum bonds, widened almost as much as the whole index. My read is that the fire does not rest on Optimum. ⚠️ That is an inference: Optimum's bond prices for those days are not in any file I hold.
- ⚠️ **The third day was a narrowing** (from 3.76 to 3.63, as stocks rebounded 4.7%). The rule counts the level, not the direction, so it fired anyway.

**What would undo it:** the spread at 3.30 or lower for five straight closes. ⚠️ If Optimum defaults (its grace period ends about 12/16), its bonds leave the index at a month-end rebalance, which can lower the spread by bookkeeping rather than healing; any exit near year-end has to be checked for that.

## 1. REG-T-04 grade (FRED first-published, `fetch.py fred --first-published`; ALFRED shows one vintage per date; read 2026-11-24 22:26 ET; FRED last updated 11/24 12:02 ET)

| Series, bp | 11/18 | 11/19 | 11/20 | **11/23** | 11/18 → 11/23 |
|---|---|---|---|---|---|
| HY OAS | 347 | **352** | **376** | **363** | +16 |
| CCC | 1,353 | 1,361 | 1,402 | 1,387 | +34 |
| B | 373 | 380 | 408 | 393 | +20 |
| BB | 205 | 210 | 229 | 219 | +14 |
| IG | 93 | 94 | 98 | 97 | +4 |
| CCC/HY | 3.90× | 3.87× | 3.73× | 3.82× | |

PROME's dashboard figures (363, CCC 1,387) match. **The 11/24 cell has not posted** (series observation end 11/23 at 22:26 ET), so nothing here uses it.

| Line | Letter | Result |
|---|---|---|
| **`REG-T-04`** | HY strictly > 350 on 3 consecutive first-published closes | **FIRED on the 11/23 close: 3 of 3** (11/21 and 11/22 are a weekend, no bar). Exit ≤ 330 ×5: run 0 |
| `REG-37` (30%, scored) | 3 consecutive > 350 on observations 11/19 to 12/11 | **RESOLVED TRUE**; forecast on the wrong side; missing-data clause not engaged |
| `REG-34` (25%) | 3 consecutive > 350 on observations 11/05 to 12/29 | **RESOLVED TRUE**; near-miss exception (third print 349 or 350) not engaged, the third print is 363; forecast on the wrong side |
| `REG-T-03` | > 320 ×3 | FIRED, held; exit ≤ 300 ×5, run 0 |
| CCC/HY tripwire | > 3.6× ×3 | Still fired; the 11/23 rise is HY-led tightening (denominator), not a CCC-led re-cross: no escalation |

PREDICTIONS cells written: Status, Date_Resolved, Outcome of REG-37 and REG-34 only; every other cell sha-checked unchanged.

## 2. WQ-512 single-issuer rider (from the latest saved holdings file)

| Item | Figure | Basis |
|---|---|---|
| CSC Holdings / Optimum weight | **0.47%** of HYG market value, 11 bonds priced 17.21 to 48.99 | `AGENTS/LIQUID/research/2026-10-22_after-close/hyg-download.xls` (latest saved; DEWEY's same-date csv gives 0.452%) |
| Widening CSC would need for HY ex-CSC ≤ 350 on 11/23 | about **+2,770 bp** over 11/18 → 11/23 (13 bp ÷ 0.47%; +2,880 bp at 0.452%) | arithmetic |
| CSC's actual window change | **UNMEASURED**: no saved file has CSC bond spreads for 11/18 or 11/23 | gap |
| CSC event timing | interest due 11/16 skipped, 8-K accepted 11/16 08:00 ET (acc 0001702780-26-000077, Items 2.04, 9.01), two sessions before the base close | EDGAR, read 11/24 |
| Breadth | BB (no CSC; CSC trades as distressed) +14 of the index's +16 | FRED tiers above |
| Other names | Altice France 0.53%, priced 77 to 93 (restructured 2025, no named event); Altice Financing 0.10% at 40; **Car-Mart (Chapter 11 11/24): no bonds in the 10/22 file** | holdings file; WALTER SIG-W-20261124-003 |
| **Conclusion** | **The fire does not rest on named issuers (INFERRED).** The fire stands on the letter either way. | |

Caveats that travel: HYG is a proxy for the ICE index; spreads on bonds priced 17 to 50 are unstable; a defaulted bond leaving at a month-end rebalance can lower the index mechanically (next rebalance 11/30; CSC grace about 12/16).

## 3. Bank-credit cross-check, 11/18 → 11/23 (the three fire closes; settled closes via `scripts/settled_bars.py`, Yahoo and Nasdaq agree except where noted)

| Instrument | Move | Flip datum | Met? |
|---|---|---|---|
| Bank preferred basket (ZIONP −0.19, WAL-PA −0.99†, OZKAP +0.28, VLYPO −0.83, VLYPP −1.08, CFG-PE +2.53†, HBANL +1.67, HBANM +1.43, KEY-PI +0.04†, TFC-PR +3.22†, in %) | **mean +0.61%**; no ex-dividend dates in the window (yfinance: OZKAP 11/02, HBANM and TFC-PR 11/13, all before) | −2% or worse over 3 sessions | NO |
| IG OAS (all IG; no free financials-only series) | +4 bp (93 → 97) | +10 bp, financials leading | NO |
| KRE vs SPY | −1.39% vs −1.08% | not a flip datum | in line |

† single route (Nasdaq returned no rows). **Read: BANK-ABSENT**, firmer than 11/23 (basket −1.14% then). **11/24, not graded:** my script holds the current-date bar as unsettled; the vendor daily bars read about 22:30 ET, after the close, show KRE 69.76 (+0.32%) vs SPY 718.78 (−0.49%), basket +0.03% from 11/18, with WAL-PA −2.69% from 11/18 (single route; WAL-specific, watch).

## 4. Inbox drained: 2 general packets + 4 WALTER lane cards, every sender

| Item | Disposition |
|---|---|
| **DEWEY 11/23, recorded lenders, Silver Pines Estates (Rockledge, Brevard), 20 homes** | **None of the named lenders is a bank I cover (my 14), and no listed bank concentrated in the St. Johns basin appears** (no Seacoast, no SouthState). The banks named are Fifth Third (2023 first lien, $324,022), Truist via SunTrust Mortgage (2012, $61,646) and PrimeLending (Hilltop, 2016, $126,750); Truist does hold basin deposits ($7.97B, 1.9% of its deposits, SOD 6/30/2026). **What it shows:** in the one basin subdivision traced, first-lien mortgage credit sits mostly with non-banks and federal insurance (at least 4 FHA), not with the local banks. **What it does not show:** today's holders (originators of record; bank-originated firsts are often sold to Fannie, Freddie or Ginnie), whether any home took water or carried flood cover, or any bank's share of book. One subdivision of 20 parcels is not a market sample, and single loans of this size against Fifth Third's or Truist's books would not be a meaningful share. **Florida caveats kept** (`PROME/reports/2026-11-23_florida-flood-sweep/SYNTHESIS.md` § Corrections, § Follow-up): the uninsured share of loss is a hypothesis; Fannie relief is not simply off without a declaration (only the no-contact first three months needs one); USCB's association book is unsized; Seacoast is the most concentrated listed bank in the basin, not the only one. KB ML-REG-322. Filed. |
| CREED 11/23, Estates at Palm Bay is in Okaloosa, not Brevard | No REGINALD file cites it (searched). Its second point, "only listed bank", was already corrected in my files 11/23; STATUS now carries only the corrected wording (the first-written paragraph rotated verbatim, BLOCK T66). Filed. |
| WALTER SIG-W-20261124-002 (REG-T-04 fired) | INTEGRATED (this memo); WALTER already routed the signal, so no separate signal packet from me |
| WALTER SIG-W-20261124-003 (Car-Mart Chapter 11) | INTEGRATED: outside the rider (no HYG bonds); bank lenders unnamed; KB ML-REG-321 `combo:bank-lending-to-private-credit` |
| WALTER SIG-W-20261124-001 (late FLASH, VIX premarket 30.40) | INFO_ONLY; VIOLET grades |
| WALTER SIG-W-20261124-005 (Florida gauges 11/24) | INFO_ONLY; OpenFEMA shows no Florida declaration since 11/01 (read 22:32 ET), so my Seacoast watch line stays NOT MET; Sanford reached major flood |

BOARD_LOG 4 rows. Receipt COR-20261123-03 NO-OP (I used card 20261121-001 only for settled 11/20 closes, which the correction holds).

## 5. Packets sent

- **LIQUID** `AGENTS/LIQUID/inbox/2026-11-24_from-REGINALD_REG-T-04-FIRED-ISSUANCE-FREEZE.md`: the ISSUANCE-FREEZE action leg (are deals pulled, volume against the same week a year earlier), the rider, the exit and rebalance caveat, the bank read.
- **TERRY** `AGENTS/TERRY/inbox/2026-11-24_from-REGINALD_REG-T-04-FIRED-tradeability-ask.md`: tradeability read asked (a card or a reasoned "no card" both complete); bank leg no candidate from me; the existing HY-leg idea is LIQUID's and TERRY's (IDEA-HYG-FOLLOW-NOV05, approved and unfilled to 12/04 as of my 11/23 packet; TERRY's card holds its current state).

## 6. FORWARD VIEW: PROJECTION (my judgment; moves no score, gate or trade; unscored, nothing registered)

- **Expect (~60%): no exit run (HY ≤ 330 on 5 closes) by 12/11**, so REG-T-04 stays fired into the Fed meeting (Wed 12/9). Why: HY is 33 bp above the exit line and must hold below it for five sessions; Optimum's grace period ends about 12/16, a live default risk inside the horizon; the selloff that drove the cross (AI and chip names: Nvidia −5.86% and AMD −8.86% again on 11/24 per WALTER's vendor read) has not resolved. The next few sessions are Thanksgiving-thin (11/26 closed and bridged, 11/27 short), so prints may drift rather than move.
- **Meaningful alternative (~40%): a fast heal.** HY went 320 → 376 in six sessions (11/12 → 11/20) and gave back 13 bp in one day on a 4.7% equity rebound; a calm in AI names could take it back toward the low 320s by mid-December. Base rate is too thin to lean on: in FRED's three-year window there are 3 comparable fresh fires, 1 of which exited within 13 sessions.
- **Banks (~70% the bank leg stays absent through 12/11):** the preferred basket recovered (+0.61%) and IG barely moved. ~30% the bank leg starts to lead.
- **What would change my mind:** toward bank transmission: a financials-led IG move of 10 bp or more, the preferred basket −2% over three sessions, a bank pulling a debt deal, a bank naming AI data-center or GPU-financing losses, or Car-Mart or Optimum lenders turning out to include my 14. Toward a faster heal: two prints under 340 with B and CCC narrowing together.

## 7. Gaps

- CSC bond-level spreads for 11/18 and 11/23: not in any saved file; the rider conclusion is a bound, INFERRED.
- 11/24 HY cell not yet published; the exit count starts there.
- No financials-only IG series (free). H.4.1 and H.8 since 11/06 still unread.
- No `AGENTS/SIGNALS.md` row: the brief limited my writes to my directory, inbox packets and this memo; WALTER's card SIG-W-20261124-002 carries the fire fleet-wide. PROME may add the row or ask me to.
- `boot.py`, `market.py` and the VX ladder were not run (scope: the due row).

**Commits (local, unpushed):** `0536954bfa` (PREDICTIONS, KB, REG-T-02 log, receipt, BOARD_LOG, inbox filing) · `95c28ac7f2` (LIQUID and TERRY packets) · `bacd526b59` (STATUS, rotation archive, CALENDAR, ROADMAP, MEMORY, TRADE) · `6e7ba61e5e` (NEXUS brief) · this memo's commit. Other desks' dirty files seen (BROCK, PROME): not mine, untouched.

## COMPLETION — REGINALD — 2026-11-24
STATUS: ✅ DONE
CHANGED: AGENTS/REGINALD/{workbook/PREDICTIONS.tsv, workbook/KB.tsv, registry/REG_T02_EXIT_LOG.tsv, registry/corrections_receipts.tsv, board/BOARD_LOG.tsv, STATUS.md, archive/STATUS_rotation_2026-11-24.md, CALENDAR.md, ROADMAP.md, MEMORY.md, TRADE.md, NEXUS_BRIEF.md, inbox → processed (2 + 4 WALTER)}; AGENTS/LIQUID/inbox and AGENTS/TERRY/inbox (1 packet each); this memo
RESULT: REG-T-04 FIRED on HY 352, 376, 363 [11/19, 11/20, 11/23] (FRED first-published; 11/24 cell not posted). WQ-512 rider: not issuer-driven (INFERRED; CSC 0.47% of HYG would need ~+2,770bp). REG-37 and REG-34 RESOLVED TRUE. Cross-check 11/18 → 11/23 BANK-ABSENT (preferred basket +0.61%, IG +4bp, KRE −1.39% vs SPY −1.08%). DEWEY's lenders: none in my 14, no basin-concentrated bank.
GAPS: CSC bond spreads unmeasured (no saved file); 11/24 HY cell unpublished; no SIGNALS.md row (brief limits; WALTER card covers it).
WILL_NEEDS: None (the fire is information; TERRY's answer may bring a card for his word).
FOLLOW-UP: LIQUID ISSUANCE-FREEZE read; TERRY tradeability answer; REGINALD counts the REG-T-04 exit from HY [11/24], checking the 11/30 rebalance and CSC grace (~12/16).
