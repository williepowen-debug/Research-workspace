# REGINALD — TRADE SURFACE

> **LIVE — rebuilt 2026-09-29 ~19:3x ET (stamp corrected at closeout against `date`; first written as ~20:1x from narrative) on Will's word (*"Do it now"*), replacing the March-2026 document (FROZEN 7/09; archived verbatim → `archive/TRADE_frozen_2026-03-07_archived_2026-09-29.md`, crc32 `ab819e73`).** This file carries the trade THESIS, the triggers by name, the refuters and the anti-trades. It carries **no marks and restates no strike it does not own**: position truth is off-repo (Will/broker); the structured mirror is `FORGE/STATUS.md` (PROME/ANVIL, last reconcile **2026-10-07 intraday Fidelity capture**; Robinhood last 9/29); this desk's structural ledger is `POSITIONS.md`. **Trade construction = TERRY; approval = Will (root rule #5).** Re-check size at any append (READ_CAP budget 32,550 B).

## 1. What this desk's trades are a bet on (state 2026-09-29; §2–§3 refreshed 2026-10-07; §1 credit-bet line + §3 trigger states refreshed 2026-10-10 from STATUS, 10/8–10/9 settled)

**Thesis (STATUS-canonical since 8/13):** regional-bank credit stress is **CONCENTRATED, not tier-wide** — 3 elevated names of 14 (FLG 6 · EGBN 5 · AMTB 5, matrix v2.0), the CRE cut narrows to FLG · EGBN · OZK, and the cross-bank Q2 filings showed CRE bad-loan rates FALLING (2.46% → 2.23%). The index expression (KRE) is therefore **tail insurance on a sector repricing**, not a directional call on cohort credit.

**What the tape is doing (attribution 9/29, `reports/2026-09-29_selloff_attribution_and_preprint_observables.md`):** 8/14 → 9/14 was small-cap/market beta with **no** financials component; 9/15 → 9/29 was a **financials-sector move led by the LARGEST banks** (14-name size sort ρ −0.72), in which KRE beat its factor loading and my credit ranking sorted the WRONG way (+0.48). Credit instruments (preferreds, BDCs, HY ETFs) barely moved. ⇒ **A KRE put today is a bet that the large-bank financials repricing continues and drags regionals at ~0.85 beta. It is NOT yet a bet on regional credit.** The credit-shaped exceptions are FLG and VLY (NYC rent-regulated multifamily; worst in both legs; FLG ladder ORANGE 9/28).

**What would make it a credit bet:** B-tier OAS holding >300 into >330 · loans to non-bank financials STALLING in H.8 · a Q3 print cluster (~10/20–28) showing breadth at the mid-pack (DOCKET L180) · an 8-K at a thesis name. None of the credit legs has happened. ⚠️ **10/10: two FUNDING bars from the 9/29 set crossed:** small-bank borrowings +11.7% in 3 weeks to 9/30 (largest in 160 weeks; ⚠️ that window starts after SVB, whose first week was +$290B, ~9× this; FHLB system debt rose only +$6.2B in Sep, so it was likely mostly NOT FHLB money, unless the FHLBanks funded it from their liquidity holdings; not yet separable), and discount-window primary credit above its 60-week p90 for two weeks ($8.74B [9/30], $9.97B [10/7]). Credit-side bars stay 🟢: non-bank lending still growing, no line draws, small-bank deposits flat. That reads as banks lining up cash, not credit reaching balance sheets (`reports/2026-10-10_FHLB_Q2_composition_and_REG-T-06_base_rate.md`).

## 2. Live legs — pointers, not restatements

| Leg | Owner of the record | State (per FORGE 9/29 reconcile) | Guard / rule |
|---|---|---|---|
| `KRE $60P Dec-18-2026 ×5` | `POSITIONS.md` · FORGE | LIVE, 72 DTE, deep OTM (KRE $68.89 [10/7]) | `REG-T-01` KRE <$60 UN-FIRED; tripwire close ≤$66 → TERRY |
| `KRE $65P Dec-31-2026 ×2` | FORGE (`MGMT-KRE65P-DEC31`, `5ce609f80`) | **NEW 9/30 — Will's own roll:** the Sep-30 $60P ×2 was SOLD 9/30 @ $0.01 (−$451.48, leg 1) and these bought @ $1.68 (leg 2) | TERRY rail: hard stop Thu 12/31 15:00 ET (not a price gate) |
| `WAL $70P Dec-18-2026 ×1` (RH) | `../WAL/` · FORGE | LIVE, the ROLL70 duration roll (filled 9/02 @ $2.20); RH not re-captured since 9/29 | `GATE-TERRY-ROLL70-EXIT` = `REG-T-02` exit: WAL ≥ $81.90 ×3 closes — **0-of-3 after 26 graded closes through 10/7** (`registry/REG_T02_EXIT_LOG.tsv`) |
| `WAL $65P Dec-18-2026 ×4` (Fidelity) | FORGE D-74 | **NEW vs the 10/1 mirror** (fill/date/approval UNRECORDED); 12.6% OTM at $74.35 [10/7]; spans the 10/19 print + Q3 10-Q | No card. ROLL70's gate does NOT transfer to this line. Thesis read → memo `PROME/inbox/2026-10-07_from-REGINALD_WQ318-baseline-T03-and-ladder.md` |
| `OZK $40P Nov-20-2026 ×4` (Fidelity) | FORGE D-74 · `../OZK/` | **NEW vs the 10/1 mirror** (fill/date/approval UNRECORDED); 8.2% OTM at $43.56 [10/7]; spans the 10/20 print + FDIC 10-Q | No card. OZK desk thesis (RESERVOIR) + its own <$45 band; thesis read → same memo |
| `HBAN $16P Oct-16-2026 ×2` | `POSITIONS.md` · FORGE | ITM since 9/26 (mark $0.85 [10/7 rcv]); the 7/18 "rides to expiry" premise FAILED | Card `MGMT-HBAN16P-OCT16`; **Will rules by Wed 10/14 (WQ-302)**. HBAN prints 10/22, AFTER expiry (OZK desk calendar) |
| `APO $95P Dec-18-2026 ×1` | `POSITIONS.md` · FORGE | LIVE, 72 DTE; BROCK thesis vehicle | Will ruled HOLD 8/13; vehicle-mismatch flag live (BROCK) |
| `KRE $25P Jan-15-2027 ×1` (RH) | FORGE only | Deep-OTM lottery, entry never recorded (D-54) | Not thesis-scope |

**Open card(s):** **KRE-put ADD (Will asked 9/29) → TERRY built `TRY-COND-KREADD` 9/30 08:12 ET (`AGENTS/TERRY/setups/KRE_add-puts_conditional-card_2026-09-30.md`): CONDITIONAL, NO FILL.** Arms only on a REGINALD instrument (`REG-T-03` ×3 with the bank-credit cross-check, a FAILED L180 breadth test, or `REG-T-01`) **plus** X1 open or Will's Tier-3 word **plus** a green day. **State 10/7: NOT ARMED on my legs** — `REG-T-03` 0-of-3 (peak run 1, 10/1), `REG-T-01` UN-FIRED, L180 grades 11/07. No Will decision is owed until it arms (root rule #10 loop: proposal recorded; decision pending the arm). Separately, Will rolled the Sep-30 KRE leg himself (row above).

## 3. Triggers this desk grades (levels live in `STATUS.md` §THRESHOLD STATUS — never here)

| Trigger | Letter | State (vintage in each cell; live levels → `STATUS.md` §THRESHOLD STATUS) | Consequence |
|---|---|---|---|
| `REG-T-01` | KRE < $60 | UN-FIRED, 13.1% away (KRE $69.01 [10/9 settled]) | 🔴 to ALL; the KRE puts' thesis level |
| `REG-T-02` | WAL < $78 | **FIRED since 9/1 (cycle 2)**; exit ≥ $81.90 ×3, run 0-of-3 (28 rows through 10/9, $74.27) | Guards ROLL70; 2-of-3 → packet TERRY |
| `REG-T-03` / `-04` | HY OAS > 320 ×3 / > 350 | **0-of-3** at the 10/8 cell (315); 324 [10/1] was 1 of 3, reset by 310 [10/2] | Credit transmission — **run the bank-credit cross-check first** (`reports/2026-07-30_bank-side-HY-attribution.md`) |
| `VX-REG-18.04` / `18.05` | CCC/HY > 3.6× ×3 · B-tier > 300 / 330 / 380 | HARD-FIRE (3.975× [10/8]; CCC 1,252 = FRED-window high, both legs widening, no CCC-led re-cross) · B 315 [10/8] = YELLOW; peak 329 [10/1], 1bp under ORANGE | Escalation SENT 9/26; watch, not re-escalate (Will 9/26) |
| `VX-REG-6.03` | FLG ladder −10 / −15 / −20% vs $14.24 | **🔴 RED — broke on the 10/7 close $11.30** (−20.6%) | Packets PROME + FLG sent 10/7 (`018af9846`); no band beyond RED |
| `REG-T-06` | FHLB advances > $700B ×3 qtrs | leg 2 of 3 ($810.7B [6/30]); composition 10/10: ~half of H1 growth = four very large banks | Q3 print (~late Oct) fires it. ⚠️ **The letter does not discriminate** (>$700B in 12 of 26 quarters since 2020); re-letter question with Will via PROME (WQ-414, due 10/24). **Q3 nowcast 10/10 ≈ $770B** (FHLB debt −$42.1B in Q3; `reports/2026-10-10_FHLB_Q3_nowcast_from_OF_debt.md`) ⇒ fires as lettered while lending likely shrank |
| Claims (LABOR) | > 300K | → `STATUS.md` (LABOR owns) | all ORANGE banks → RED |

**Exit rules** (STATUS §EXIT RULES, unchanged): HY < 260 is a REVIEW trigger, not an auto-exit (Will 6/19); BTFP-2.0 = thesis broken (auto-exit); CRE-channel anchors (WAL NCO ex-fraud < 25bp AND no office migration; office CMBS-DQ flows reversing 2 prints + bank CRE-DQ tier-creep reversing).

## 4. Refuters for any bank put on this desk (write them on the card)

B-tier OAS back **< 300** (a 9/15-style reversal) · HY back **< 280** · KRE reclaims **$72.74** (the 9/16 gap-down close) · a clean Q3 print cluster (no mid-pack breadth, L180) · H.8 non-bank lending re-accelerating with small-bank deposits stable · ~~LABOR's bull-side kill (Sep NFP ≥ +150K, 10/2)~~ did NOT fire: payrolls +29K, net revisions −60K (WALTER -20261002-001) — the labor leg stands.

## 5. Anti-trades (tempting, and the evidence says no)

- **Single-name puts on my top-scored names as a "credit" expression.** EGBN and AMTB (matrix 5) were the two BEST performers of the selloff (−2.9% / −0.2% vs KRE −10%); the market is not pricing my ranking. A credit thesis needs a print, not a score.
- **Adding on a red day.** Root rule #6: puts on GREEN days. Breaking it needs the direct measurement written on the card before the fill (`AGENTS/TERRY/RISK_RULES.md`); "the window is closing" is a chase. 9/29 was red.
- **Treating the March document as live.** Its eight-channel frame, its April earnings plan and every leg in it are dead (archived with crc above). Cite `STATUS.md` for thesis state.
- **Reading a HY level as bank transmission.** The 7/27–29 sustain over 280 was BANK-ABSENT; HY sits downstream of bank credit in my chain. Cross-check first.
- **Trimming for size when the thesis is intact.** Root rule #7: roll duration, don't trim (trimming = thesis broken). Any roll rides on TERRY's card.
- **Chasing the deposit-flight narrative with a trade.** "Agentic bank run" (Slok 9/27) is a mechanism frame with no flow data; it was a WQ-318 question, answered 10/7: no NIB-share decline at any of the six banks through 6/30 (`reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md`), so nothing to grade yet.

## 6. History — what this desk's names have done to the book

Jun-18 / Jun-30 clusters cleared (FORGE 7/16) · Jul-17 legs lapsed OTM (WAL $65P, ZION $57.5P, FLG $13P ×3) · **Aug-21 `KRE $60P ×3` lapsed worthless — broker-confirmed on the FORGE 9/29 ledger (five Aug-21 rows, realized −$2,816.72 book-wide)** · WAL Sep-18 pair (`../WAL/`) expired 9/18, broker-confirmed 9/21, −$1,519.34 · SSB $90P and KRE $70P = the two unrecorded-exit phantoms that built the POSITIONS-first rule (`LESSONS.md`). **Lesson the book keeps teaching: deep-OTM index puts with sub-quarter tenor have lapsed four times in a row; the live expressions that have paid or held are the duration roll (WAL Dec-18) and the ITM HBAN leg nobody expected.**

---
*Owner REGINALD. Levels → `STATUS.md`; strikes/qty → `POSITIONS.md` + `FORGE/STATUS.md`; construction → TERRY; approval → Will. Rebuilt 2026-09-29; prior file archived verbatim (crc above).*
