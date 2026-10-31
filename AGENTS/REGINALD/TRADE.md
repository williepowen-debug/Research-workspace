# REGINALD — TRADE SURFACE

Last real data refresh: 2026-10-30 — §2 `KRE $68P Nov-27 ×10` row added from `FORGE/STATUS.md:71` (FORGE marks 10/30 ~13:2x ET; PROME via DAEDALUS addendum 17:41 ET: held by Will); other legs unchanged. Prior: 2026-10-22 — §2 legs re-derived from `FORGE/STATUS.md` ANVIL reconcile of Will's Fidelity capture pasted 11:01 ET 10/22 (intraday marks, not closes). Robinhood not in that capture: its rows stay UNVERIFIED since 9/29.

> **RECONCILED 2026-10-22 12:30 ET (DAEDALUS D:L793 item 2).** The October 21 'RECONCILIATION REQUIRED' banner is resolved for §2–§3: legs re-derived from the 10/22 FORGE capture, expired HBAN row moved to §6. Prior banner text → git history (`git log -p -- AGENTS/REGINALD/TRADE.md`). Broker truth stays off-repo (Will/FORGE).

> **LIVE — rebuilt 2026-09-29 ~19:3x ET (stamp corrected at closeout against `date`; first written as ~20:1x from narrative) on Will's word (*"Do it now"*), replacing the March-2026 document (FROZEN 7/09; archived verbatim → `archive/TRADE_frozen_2026-03-07_archived_2026-09-29.md`, crc32 `ab819e73`).** This file carries the trade THESIS, the triggers by name, the refuters and the anti-trades. It carries **no marks and restates no strike it does not own**: position truth is off-repo (Will/broker); the structured mirror is `FORGE/STATUS.md` (PROME/ANVIL; its reconcile vintage lives in its own header and is not restated here, per root CLAUDE.md; struck 2026-10-31, DAEDALUS addendum A1, where this line said 10/07 while :3 said 10/22); this desk's structural ledger is `POSITIONS.md`. **Trade construction = TERRY; approval = Will (root rule #5).** Re-check size at any append (READ_CAP budget 32,550 B).

## 1. What this desk's trades are a bet on (state 2026-09-29; §2–§3 refreshed 2026-10-07; §1 credit-bet line + §3 trigger states refreshed 2026-10-10 from STATUS, 10/8–10/9 settled)

**Thesis (STATUS-canonical since 8/13):** regional-bank credit stress is **CONCENTRATED, not tier-wide** — 3 elevated names of 14 (FLG 6 · EGBN 5 · AMTB 5, matrix v2.0), the CRE cut narrows to FLG · EGBN · OZK, and the cross-bank Q2 filings showed CRE bad-loan rates FALLING (2.46% → 2.23%). The index expression (KRE) is therefore **tail insurance on a sector repricing**, not a directional call on cohort credit.

**What the tape is doing (attribution 9/29, `reports/2026-09-29_selloff_attribution_and_preprint_observables.md`):** 8/14 → 9/14 was small-cap/market beta with **no** financials component; 9/15 → 9/29 was a **financials-sector move led by the LARGEST banks** (14-name size sort ρ −0.72), in which KRE beat its factor loading and my credit ranking sorted the WRONG way (+0.48). Credit instruments (preferreds, BDCs, HY ETFs) barely moved. ⇒ **A KRE put today is a bet that the large-bank financials repricing continues and drags regionals at ~0.85 beta. It is NOT yet a bet on regional credit.** The credit-shaped exceptions are FLG and VLY (NYC rent-regulated multifamily; worst in both legs; FLG ladder ORANGE 9/28).

**What would make it a credit bet:** B-tier OAS holding >300 into >330 · loans to non-bank financials STALLING in H.8 · a Q3 print cluster (~10/20–28) showing breadth at the mid-pack (DOCKET L180) · an 8-K at a thesis name. None of the credit legs has happened. ⚠️ **10/10: two FUNDING bars from the 9/29 set crossed:** small-bank borrowings +11.7% in 3 weeks to 9/30 (largest in 160 weeks; ⚠️ that window starts after SVB, whose first week was +$290B, ~9× this; FHLB system debt rose only +$6.2B in Sep, so it was likely mostly NOT FHLB money, unless the FHLBanks funded it from their liquidity holdings; not yet separable), and discount-window primary credit above its 60-week p90 for two weeks ($8.74B [9/30], $9.97B [10/7]). Credit-side bars stay 🟢: non-bank lending still growing, no line draws, small-bank deposits flat. That reads as banks lining up cash, not credit reaching balance sheets (`research/FHLB/reports/2026-10-10_FHLB_Q2_composition_and_REG-T-06_base_rate.md`).

## 2. Live legs — pointers, not restatements (structure per FORGE 10/22 11:01 ET capture; marks live in FORGE only)

| Leg | Account | Owner of the record | Guard / rule |
|---|---|---|---|
| `KRE $66P Nov-20-2026 ×3` | Fidelity | FORGE (NEW 10/22, broker-verified buy) | No REGINALD card; `REG-T-01` KRE <$60 UN-FIRED |
| `KRE $67P Nov-27-2026 ×4` | Fidelity | FORGE (bought 10/12; card/owner UNKNOWN, D-77) | Same |
| `KRE $70P Nov-27-2026 ×2` | Fidelity | FORGE (NEW 10/22, broker-verified buy) | Same |
| `KRE $68P Nov-27-2026 ×10` | Fidelity | FORGE:71 (added 2026-10-30; held per PROME: Will's 10/30 13:21 Fidelity capture agrees with FORGE; buy date/price UNSEEN, D-90; card/owner UNKNOWN, D-74) | Same |
| `KRE $60P Dec-18-2026 ×5` | Fidelity (2 + 3 lots) | FORGE · `POSITIONS.md` | Same |
| `KRE $65P Dec-31-2026 ×2` | Fidelity | FORGE (`MGMT-KRE65P-DEC31`, `5ce609f80`) | TERRY rail: hard stop Thu 12/31 15:00 ET (not a price gate) |
| `WAL $65P Dec-18-2026 ×4` · `WAL $70P Dec-18-2026 ×2` | Fidelity | FORGE · `../WAL/` | `REG-T-02` FIRED; exit ≥ $81.90 ×3 (`registry/REG_T02_EXIT_LOG.tsv`). ROLL70's gate does not transfer to the $65P line |
| `OZK $40P Nov-20-2026 ×4` | Fidelity | FORGE · `../OZK/` | OZK desk thesis (conviction LOW since 10/22, WQ-483) |
| `ZION $62.5P Nov-20-2026 ×2` | Fidelity | FORGE (card/owner UNKNOWN, D-74) | ZION matrix rank 1; Q3 print clean (`reports/2026-10-22_catchup/REPORT.md` §5) |
| `APO $95P Dec-18-2026 ×1` | Fidelity | FORGE · BROCK | Will ruled HOLD 8/13; vehicle-mismatch flag (BROCK) |
| `WAL $70P Dec-18-2026 ×1` · `KRE $25P Jan-15-2027 ×1` | Robinhood | FORGE 9/29 only — **UNVERIFIED since 9/29** | ROLL70 (`GATE-TERRY-ROLL70-EXIT` = REG-T-02 exit) · KRE $25P lottery (D-54) |

*Grouping is not approval or ownership (FORGE D-74). No fills, dispositions or card states are inferred here.*

**Open card(s):** **KRE-put ADD (Will asked 9/29) → TERRY built `TRY-COND-KREADD` 9/30 08:12 ET (`AGENTS/TERRY/setups/KRE_add-puts_conditional-card_2026-09-30.md`): CONDITIONAL, NO FILL.** Arms only on a REGINALD instrument (`REG-T-03` ×3 with the bank-credit cross-check, a FAILED L180 breadth test, or `REG-T-01`) **plus** X1 open or Will's Tier-3 word **plus** a green day. **State 10/7: NOT ARMED on my legs** — `REG-T-03` 0-of-3 (peak run 1, 10/1), `REG-T-01` UN-FIRED, L180 grades 11/07. No Will decision is owed until it arms (root rule #10 loop: proposal recorded; decision pending the arm). Separately, Will rolled the Sep-30 KRE leg himself (row above).

## 2b. Trade-idea route to TERRY (Will 10/20 "we can loosen rules for trade ideas"; added 2026-10-22, D:L793 item 6)

At each print-cluster grade, this desk sends TERRY any candidate expression as a packet to `AGENTS/TERRY/inbox/`, **labelled NOT-FIRED** whenever its trigger has not fired. Each packet carries the trigger state, the evidence link and its grade; **TERRY's card** carries size and risk in figures (WQ-508, one form fleet-wide). If there is no candidate, the grading report says "no candidate" and why. TERRY constructs; Will decides each one under root rule #5. The $500/card and X1 limits are the default shown on each card.

| Date | Idea | State | Disposition |
|---|---|---|---|
| 2026-10-22 | EGBN (Eagle) Q4 maturity wall | **No candidate.** Put side: options untradeable (put OI ~2 contracts) and realistic loss only ~$0.3–0.6/share. Long side: plausible but not this desk's edge | `reports/2026-10-22_appraisal-discount_cohort_test.md` §5. A long would be a TERRY card if Will asks |
| 2026-10-23 | FLG / AMTB / CUBI Q3 print cluster | **No candidate.** FLG: none of the desk's CRE 'weakens if' lines met, but the move (−9% intraday 10/23) is post-print and FLG is not on this book; AMTB and CUBI printed cleaner | `reports/2026-10-23_boot/REPORT.md` §2, §6 |
| 2026-10-28 | SBCF Q3 (last FL-frame name) + HY window close | **No candidate.** SBCF's 8-K cell held (criticized+classified 2.90% vs ≥3.20%) and no FL cell transmits. HY tightened to 318 [10/27] without REG-T-04 firing, so the broad-credit window that WQ-509 targeted did not open; that card is TERRY's. The live driver is the 10-year, and its falsifier is already in §4 | `reports/2026-10-28_boot/REPORT.md` §1–§2 |
| 2026-10-31 | Q3 per-bank borrowing short list (FFIEC, 134 of 139): 6 frozen-rule flags (Regions, Renasant, Simmons, The Bancorp, Bank of Hawaii, Israel Discount NY) | **No candidate.** The frozen rule routes a listed flagged name only after a CONCENTRATED or MIXED verdict, which needs the FDIC full universe (~mid/late Nov); each flag reads at the issuer as a funding-mix shift (sweep or public-fund outflows, brokered swap, loan growth), not stress | `reports/2026-10-31_L857/REPORT.md` §3, §5 |

## 3. Triggers this desk grades (levels live in `STATUS.md` §THRESHOLD STATUS — never here)

| Trigger | Letter | State (vintage in each cell; live levels → `STATUS.md` §THRESHOLD STATUS) | Consequence |
|---|---|---|---|
| `REG-T-01` | KRE < $60 | UN-FIRED, 17.1% away (KRE $72.41 [10/22 settled]) | 🔴 to ALL; the KRE puts' thesis level |
| `REG-T-02` | WAL < $78 | **FIRED since 9/1 (cycle 2)**; exit ≥ $81.90 ×3, run 0-of-3 (37 rows through 10/22, $76.67) | Guards ROLL70; 2-of-3 → packet TERRY |
| `REG-T-03` / `-04` | HY OAS > 320 ×3 / > 350 | **REG-T-03 CREDIT-CANARY-FIRED (10/16 close)**; 7 consecutive >320 through 340 [10/22]; cross-check BANK-ABSENT ~0.7 (`reports/2026-10-23_boot/REPORT.md` §4); **REG-T-04 10bp away, run 0 of 3** | Credit transmission — **run the bank-credit cross-check first** (`reports/2026-07-30_bank-side-HY-attribution.md`) **Single-issuer disclosure rider (WQ-512 RULED APPROVE A, Will 2026-10-23 17:01 ET):** at a fire, the Will-facing consequence states named-issuer contribution (CSC/Optimum 0.47% of HYG [10/22]; +1,000bp on CSC ≈ +4.7bp) and the index level without those issuers; no level, operator, instrument or consequence moves; exit (≤330 ×5) read with the 10/31 index-rebalance caveat → `registry/NOTES.md`. |
| `VX-REG-18.04` / `18.05` | CCC/HY > 3.6× ×3 · B-tier > 300 / 330 / 380 | HARD-FIRE continues (3.94× [10/22]; CCC 1,340; no new CCC-led re-cross) · B 346 [10/22] = ORANGE (>330) | Escalation SENT 9/26; watch, not re-escalate (Will 9/26) |
| `VX-REG-6.03` | FLG ladder −10 / −15 / −20% vs $14.24 | **🔴 RED since the 10/7 close $11.30**; 11 settled closes below RED (10/7–10/21); 10/22 settled $11.44 sat just above $11.39 (state stays RED, state machine); $10.38 intraday 10/23 after the Q3 miss (not settled) | Packets PROME + FLG sent 10/7 (`018af9846`); no band beyond RED |
| `REG-T-06` | OF system advances >$700B ×3 official qtrs; exit <=$650B ×2 | Official run 2 of 3 through Q2; dated nowcast excluded, level/evidence → STATUS / FHLB hub | **REVIEW (WQ-414, Will 10/11).** Before escalation: top-four growth contribution + qualified SEC-filer borrower median. Missing/incomparable breadth explicit; nonpositive growth share NOT-APPLICABLE. No breadth cutoff, automatic crisis, trade or capital action; procedure `registry/NOTES.md` §REG-T-06 |
| Claims (LABOR) | > 300K | → `STATUS.md` (LABOR owns) | all ORANGE banks → RED |

**Exit rules:** re-derived 2026-10-22 → `STATUS.md` §EXIT RULES (kill rail stamp there; CRE anchor re-keyed off REG-24/25). Pointer only; the rail lives in STATUS.

## 4. Refuters for any bank put on this desk (write them on the card)

**Rate falsifier, 2026-10-23 (PROME ask):** over 57 trading days (8/4 → 10/22) KRE moved about **−0.72% per +10bp on the 10-year** and **+0.02% per +10bp of HY spread** (correlations −0.36 and +0.07; R² 0.13, weak). **A falling 10-year is the falsifier to write on a regional-bank put card; a wide HY print alone is not confirmation.** Receipt → `reports/2026-10-23_boot/kre_vs_hy_vs_10y.txt`.

**OZK existing-position evidence,10/12 consumption:** executed RaDD extension/fresh capital materially weaken near-term maturity failure. Real Alewife funding and Boston lease progress are contrary evidence; Boston closing/payoff, project runway and retained workout exposure remain unknown. Bank cash, recognized losses and retained/new loans/OREO are separate. Existing Q3 card reads Boston → RaDD → cash/retained exposure → earnings/capital; no new card, order or loss forecast. Limits/receipt → `reports/2026-10-12_OZK_durability-consumption.md`.

B-tier OAS back **< 300** (a 9/15-style reversal) · HY back **< 280** · KRE reclaims **$72.74** (the 9/16 gap-down close) · a clean Q3 print cluster (no mid-pack breadth, L180) · H.8 non-bank lending re-accelerating with small-bank deposits stable · ~~LABOR's bull-side kill (Sep NFP ≥ +150K, 10/2)~~ did NOT fire: payrolls +29K, net revisions −60K (WALTER -20261002-001) — the labor leg stands.

## 5. Anti-trades (tempting, and the evidence says no)

- **Single-name puts on my top-scored names as a "credit" expression.** EGBN and AMTB (matrix 5) were the two BEST performers of the selloff (−2.9% / −0.2% vs KRE −10%); the market is not pricing my ranking. A credit thesis needs a print, not a score.
- **Adding on a red day.** Root rule #6: puts on GREEN days. Breaking it needs the direct measurement written on the card before the fill (`AGENTS/TERRY/RISK_RULES.md`); "the window is closing" is a chase. 9/29 was red.
- **Treating the March document as live.** Its eight-channel frame, its April earnings plan and every leg in it are dead (archived with crc above). Cite `STATUS.md` for thesis state.
- **Reading a HY level as bank transmission.** The 7/27–29 sustain over 280 was BANK-ABSENT; HY sits downstream of bank credit in my chain. Cross-check first.
- **Trimming for size when the thesis is intact.** Root rule #7: roll duration, don't trim (trimming = thesis broken). Any roll rides on TERRY's card.
- **Chasing the deposit-flight narrative with a trade.** "Agentic bank run" (Slok 9/27) is a mechanism frame with no flow data; it was a WQ-318 question, answered 10/7: no NIB-share decline at any of the six banks through 6/30 (`reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md`), so nothing to grade yet.

## 6. History — what this desk's names have done to the book

**HBAN $16P Oct-16-2026 (2 contracts on the 10/14 capture; card `MGMT-HBAN16P-OCT16`, WQ-302):** absent from the 10/22 FORGE capture after expiry. FORGE D-80 records one contract leaving before 10/15 (proceeds unknown). D-86 records the last one absent after expiry, with sale, exercise or worthless expiry UNKNOWN. Closed on this desk's surfaces 2026-10-22; outcome per the broker record only.

Jun-18 / Jun-30 clusters cleared (FORGE 7/16) · Jul-17 legs lapsed OTM (WAL $65P, ZION $57.5P, FLG $13P ×3) · **Aug-21 `KRE $60P ×3` lapsed worthless — broker-confirmed on the FORGE 9/29 ledger (five Aug-21 rows, realized −$2,816.72 book-wide)** · WAL Sep-18 pair (`../WAL/`) expired 9/18, broker-confirmed 9/21, −$1,519.34 · SSB $90P and KRE $70P = the two unrecorded-exit phantoms that built the POSITIONS-first rule (`LESSONS.md`). **Lesson the book keeps teaching: deep-OTM index puts with sub-quarter tenor have lapsed four times in a row; the live expressions that have paid or held are the duration roll (WAL Dec-18) and the ITM HBAN leg nobody expected.**

---
*Owner REGINALD. Levels → `STATUS.md`; strikes/qty → `POSITIONS.md` + `FORGE/STATUS.md`; construction → TERRY; approval → Will. Rebuilt 2026-09-29; prior file archived verbatim (crc above).*
