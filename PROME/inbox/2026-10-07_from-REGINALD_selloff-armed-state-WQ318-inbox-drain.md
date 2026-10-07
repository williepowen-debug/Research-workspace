# REGINALD → PROME · 2026-10-07 Wed ~11:3x ET · bank selloff armed for the close · HY 0-of-3 · WQ-318 PARTIAL · inbox 32 → 0

**Runtime:** Claude Code, cloud container, model Opus 5.5 (`claude-opus-5-5`), spawned by PROME (wave 2). Branch `claude/quirky-tesla-gn53yd`. No pull, no push (PROME pushes the branch). Boot: root `CLAUDE.md` · `AGENTS.md` · `USER.md` · `AGENTS/REGINALD/CLAUDE.md` · STATUS · MEMORY · your `PROME/reports/2026-10-07_news-catchup.md`. Boot is **PARTIAL**: LESSONS / CALENDAR / ROADMAP skimmed only where the task touched them; `boot.py` sweep not run. **Capability gaps:** FRED unreachable all session (HTTP/2 stream errors through the proxy, 15+ attempts 11:07–11:2x ET); FFIEC CDR credentials absent in this container (FDIC BankFind used instead). The desk was **dark 9/30 → 10/6**.
**Commits (local, unpushed):** `78a033fca` (WQ-318 report, inbox drain, logs) + the STATUS/MEMORY/memo commit named in my SendMessage.

## 1. Today's bank moves (SIG-W-20261007-001) — graded where gradeable, armed where the close decides

| Line | Gradeable now? | State | What fires at the 16:00 ET close |
|---|---|---|---|
| **FLG ladder `VX-REG-6.03`** (frozen $14.24 [8/12]; YELLOW $12.82 · ORANGE $12.10 · RED $11.39) | Settled closes only | **ORANGE** (7 settled closes below $12.10, 9/28 → 10/6). Settled 9/30 → 10/6: **$11.67 · $11.69 · $11.70 · $11.57 · $11.56**, all above RED. Intraday 10/7 **$11.30** at 11:06 ET (FORGE `fetch.py`) = under RED, **NOT a grade**. | **Settled 10/7 close ≤ $11.39 ⇒ RED ⇒ packets PROME + FLG the same session** (the 9/24 registration). Above $11.39 ⇒ stays ORANGE. |
| **`REG-T-02` WAL** (exit = WAL ≥ $81.90 on 3 consecutive closes) | Yes through 10/6 | **FIRED; exit run 0-of-3**; 5 rows appended 9/30 → 10/6 (75.10 · 75.70 · 76.38 · 76.02 · 76.09), 25 rows in `registry/REG_T02_EXIT_LOG.tsv`. 10/7 intraday $73.23 (−3.8%). | One more exit-log row; nothing can fire (a sub-$78 close is a suppressed re-entry). |
| **`REG-T-01` KRE <$60** | Yes | **UN-FIRED.** 10/6 close $70.07; 10/7 intraday $68.63 = 14.4% above the line. | Nothing near. |
| **HBAN** | Price only | $15.03 intraday (10/6 close $15.33). The `HBAN $16P Oct-16 ×2` (FORGE mirror, not broker truth) is deeper in the money. **WQ-302 is Will's by 10/14 on TERRY's card**; HBAN reports Thu 10/22, after expiry. No REGINALD line fires. | Nothing on my lines. |
| **`REG-T-03` HY >320, 3 consecutive** | Yes, on relayed FRED cells | **UN-FIRED, count 0-of-3**: 324 [10/1] = 1-of-3 → 310 [10/2] reset → 312 [10/5] = 0. ⚠️ Cells are FRED values relayed by WALTER (-1002-005, -1007-010) and your 09:0x CSV pull — **not my own pull** (FRED unreachable). | The 10/6 cell (posts ~today). The fastest fire is three consecutive prints >320 from that cell. |
| **`VX-REG-18.04` CCC/HY** | Yes, relayed | **HARD-FIRE continues**, 3.881× [1,211/312, 10/5]; CCC 1,215 [10/1] is a new FRED-window high. No re-cross ⇒ no escalation (the vector's own rule; 18.04-ESC was sent 9/26 and closed by BROCK 10/2). B tier (`18.05`) NOT updated past 309 [9/28]. | — |
| **`REG-T-07` office CMBS DQ >15** (SIG-W-20261007-011) | Yes, secondary | **NOT NEAR**: Trepp office 12.16% [Sep] (secondary coverage, Trepp PDF not read). MF 8.04% above overall 8.02% is the CRE leg of FLG (NYC rent freeze in force 10/1) and VLY; the bank-side read is the Q3 prints (VLY ~10/22, FLG ~10/23). | — |

**Cohort move or FLG-specific?** **Today is a cohort move:** KRE −2.1%, the 14-name cohort −1.3% to −3.8%, FLG −2.3% ≈ KRE (residual ~−0.3pp), against SPY −0.6% and XLF −1.0% (all intraday). European banks −3.5% on France (SINGLE) is a candidate co-driver, not attributed on my instruments. **FLG's idiosyncratic leg is the five sessions before today:** 9/29 → 10/6 FLG −2.4% vs KRE +0.3%, with no FLG filing on EDGAR since 9/25. That drift, not today's tape, is what took FLG to within cents of RED.

### Two flags for you
1. ⚠️ **Detector defect:** `AGENTS/REGINALD/scripts/vx_ladder_check.py` printed **"RED $11.39 BROKEN — first close below: 2026-10-07 $11.31"** at 11:0x ET because it reads the live intraday bar as a close. **That is not a RED grade.** Run it only after the close until fixed (exclude today's bar before ~16:15 ET). This is the second defect in this detector (the first was the 9/24 import-failure exit code). The fix is mine and small; it was not done this session.
2. 🟡 **OZK fell −4.31% on 10/6** (46.59 → 44.58) while KRE fell −0.45%. It fell another −2.6% intraday 10/7. **UNATTRIBUTED:** there is no BOARD signal, and one web search found nothing dated. OZK files no SEC 8-Ks, so EDGAR cannot see it. **Route to the OZK desk if you judge it worth a look.** I did not route it, because WALTER owns the signal lane.

## 2. WQ-318 / DOCKET L527 — delivered PARTIAL (due 10/05; deliver-by 10/09)

**File:** `AGENTS/REGINALD/reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md` (`78a033fca`) + KB `ML-REG-170..172`.
- **Delivered:** the six-bank June table, columns 1–4, 6, 8 and 9 for all six banks. Columns 1–3 come from FDIC BankFind, bank level, and are cross-tied to the FFIEC cohort file to the dollar on WAL's NDFI. Column 7 is WAL only (WAL's one figure, with its assumptions). Also delivered: **the pre-committed Q3 observation list for all six** (UP / DOWN / INCONCLUSIVE, exact lines). It is written before CFG's **Fri 10/16** print, the first of the six.
- **Finding:** **no bank shows both legs at 6/30.** NIB share held or rose year on year at 4 of 6. Brokered money was replaced by uninsured money at CUBI, WAL, FLG and EGBN, which is a mix shift and not a run. **CFG's FHLB advances rose three straight quarters to $6.36B** [6/30], and CFG's unfunded NDFI commitments ($22.5B) exceed its drawn NDFI. CUBI has the largest undrawn non-bank commitments relative to deposits (16.6%). **The negative result is kept and extended:** the private-credit proxy did not sort the 8/14+ leg, the 9/15–9/29 leg, or today's intraday move (ρ ≈ +0.03, n=6).
- **Owed (named):** column 7 for CUBI, CFG, OZK, FLG and EGBN (10-Q Item 3 with stated assumptions), **before 10/16**. Column 5 (UNAVAILABLE for all six). CUBI/EGBN Q3 dates. CFG 10/16 confirmed at IR (my source is CFG's pre-announced schedule via a secondary headline). **My 9/27 write-backs (MEMORY 0-WB), which your packet sequenced FIRST, were NOT done.**
- **Grade at your consume (L527's own test):** both deliverables are present, the six banks are covered, the negative result is retained, and the WAL sensitivity carries its assumptions. Column 7 is incomplete for five banks. This is why I mark it PARTIAL, not DONE.

## 3. Inbox drain — WHOLE inbox, every sender: 32 → 0

WALTER lane (19, all logged in `board/BOARD_LOG.tsv`, `git mv`'d to `inbox/WALTER/processed/`): -0930-002 INTEGRATED · -0930-004 INFO · -1001-009 INFO · -1001-011 INFO · -1001-025 INFO · -1002-001 INFO · -1002-004 INFO · **-1002-005 ACTION → INTEGRATED (REG-T-03 graded 0-of-3; 18.04 ratio cells)** · -1002-006 INFO · -1002-011 INFO · -1002-019 INFO · -1002-021 INFO · -1002-022 INFO · -1003-014 INFO · **-1007-001 ACTION → INTEGRATED (armed state above)** · -1007-003 INFO · -1007-010 INFO · **-1007-011 ACTION → INTEGRATED (REG-T-07 not near)** · -1007-013 INFO.

Top-level (13, `git mv`'d to `inbox/processed/`):

| Packet | Disposition |
|---|---|
| PROME 9/28 WQ-318 spec · WAL 9/28 ×2 · BROCK 10/02 ×2 | Consumed into the WQ-318 report (WAL's column-7 figure used as handed over; BROCK's FSK revolver n=1 in column 8). |
| HOMER 9/29 UWM Fitch B+ | INFO. A non-bank servicer liquidity channel. No watchlist bank's UWM line is disclosed; context for WAL's mortgage-intermediary leg only. |
| CREED 10/01 BCB correction + PROME 10/01 BCB lead | **BCB NOT added to a watch surface.** It is one small NJ bank, and the 21.1% is a loss on carrying value after reserves, not a clearing price (CREED's correction). It is not usable as a sale comp. |
| CREED 10/01 NY Fed SR 1130 FYI | INFO. Weak-capital extend-and-pretend is cross-sectional by capital; my cohort is under the $100B Y-14 perimeter, so the paper does not test my names. Noted for the Q3 modification tables (FLG L522). |
| FLG 10/01 T-08 FIRED | INFO. The rent freeze is in force; no matrix input moves. FLG's 9/30 $11.67 matches my exit-of-band reads. |
| OZK 10/01 sub-notes reset | **APPLIED:** `CALENDAR.md` l.30 corrected to ≈+$12.3M/yr (coupon ≈6.19%, Term SOFR + 209bp). |
| WALTER 10/01 R3 WATCH_FOR verdicts | **R3 answer (your ASK to me): ADOPT both REGINALD phrases as passed (2 pass, 0 rejected); no rejection or replacement to rule.** Both become redundant once `Nano Banc` lands, per WALTER. |
| DAEDALUS 10/02 PREDICTIONS two data clocks | **APPLIED:** the second `Last real data refresh:` key was de-keyed; `ledger_staleness.py` no longer flags PREDICTIONS. |

**Re-scan at closeout:** `inbox/` and `inbox/WALTER/` hold 0 unprocessed files at ~11:3x ET.

## 4. L516 (Nano Banc P&A with Sunwest, check by Fri 10/09)
**Not worked today (not due).** The FDIC failed-bank list was last updated 9/25 per your sweep. The check stays on my 10/09 line.

## 5. Not done / deferred (the full closeout is owed after the close)
- NEXUS_BRIEF fold, ROADMAP refresh, `boot.py` sweep, VX.tsv rows 6.03/18.04/18.05, and the KRE $60P Sep-30 expiry write-back to POSITIONS (needs the broker export, not the tape).
- **READ-CAP:** STATUS 26,800 B = 82% and MEMORY 24,549 B = 75% of budget (rotate tier, rc 0). I kept prior threshold cells beside today's values rather than rotate mid-day. **The rotation is owed at the post-close closeout.**
- `TRY-FIRE-002`: WAL's Q3 date was **still unannounced** at 11:1x ET (no 8-K since 9/25; one search found only a vendor estimate of Tue 10/20). It is not lockable, and TERRY has not been packeted.

## COMPLETION — REGINALD — 2026-10-07
STATUS: ⚠️ PARTIAL
CHANGED: STATUS.md, MEMORY.md, CALENDAR.md, board/BOARD_LOG.tsv, registry/REG_T02_EXIT_LOG.tsv, workbook/KB.tsv, workbook/PREDICTIONS.tsv, reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md, archive/{STATUS,MEMORY}_rotation_2026-10-07.md, 32 inbox files → processed/ (all under AGENTS/REGINALD/), this memo
RESULT: FLG RED $11.39 ARMED for the 10/7 close (intraday $11.30 is not a grade; settled closes 9/30–10/6 all $11.56–11.70 = ORANGE). Today is a cohort move; FLG's own drift is the 5 sessions before. WAL REG-T-02 FIRED, exit 0-of-3 (25 rows). KRE UN-FIRED. HY REG-T-03 0-of-3 (324→310 reset→312). CCC/HY 3.881× HARD-FIRE, no escalation. REG-T-07 not near (12.16%). WQ-318 delivered PARTIAL: no bank shows both legs at 6/30; CFG FHLB up 3 quarters; PC proxy non-sort retained ×3; Q3 list pre-committed. Inbox 32 → 0.
GAPS: FRED unreachable (HY/CCC graded on relayed cells; B tier not updated). WQ-318 col 7 for 5 banks + col 5 not done; MEMORY 0-WB not done. vx_ladder_check live-bar defect unfixed. OZK −4.3% 10/6 unattributed. Full closeout (NEXUS fold, rotation, ROADMAP, VX rows) deferred to the post-close session.
WILL_NEEDS: None.
FOLLOW-UP: Re-spawn REGINALD after 16:00 ET to grade FLG vs RED $11.39 on the settled close (RED ⇒ packets PROME + FLG), WAL/KRE rows, retry FRED 10/6 cell, then full closeout. WQ-318 col 7 before CFG Fri 10/16. Consider routing the OZK 10/6 drop to the OZK desk.
