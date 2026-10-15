# POSITION NOTE — new Fidelity bank puts: WAL $65P Dec-18-2026 ×4 · OZK $40P Nov-20-2026 ×4 — observed 10/7, not carded

**Date:** 2026-10-07 Wed, written 22:10 ET (`date` 22:10:35; live reads 21:45 ET after the close). **Session:** PROME `prome-0e` spawn (Tier 1). Model: Claude Opus 5.5.
**Ids:** `NOTE-WAL65P-DEC18` · `NOTE-OZK40P-NOV20` (notes, not management cards; registered in `setups/INDEX.md`).
**Terry verdict:** 🟡 **RECORDED — Will's own hand; NO management card unless Will asks.** The sell-or-roll rail is his standing practice (`USER.md`, 9/30 19:03 ET); this note only dates when a card is owed under PROME's C5 commission: **OZK by Wed 11/18 · WAL by Wed 12/16** (two sessions before each expiry).
**`$0` MOVED · NO ORDER · NO CARD · NO GATE OR THRESHOLD MOVED.** Construction rule #20: the entry half (fill date, price, reason, trigger) is **UNRECOVERABLE** from a positions view and is not reconstructed here. `[POSITION_STATE_INCOMPLETE]` — FORGE D-73 / D-74.

| | WAL $65P Dec-18 ×4 (Fidelity) | OZK $40P Nov-20 ×4 (Fidelity) |
|---|---|---|
| Capture (received 10/7, time UNKNOWN; FORGE `e8fd99acf`) | basis **$682.65** ($1.71) · last $1.60 ⇒ $640.00 (−$42.65); Today = Total ⇒ consistent with a same-session entry | basis **$322.66** ($0.81) · last $0.65 ⇒ $260.00 (−$62.66); Today = Total |
| Underlying, 10/7 close (yfinance) | **WAL $74.35 (−2.29%)**; 10/5 $76.02 · 10/6 $76.09 | **OZK $43.56 (−2.29%)**; 10/5 $46.59 · 10/6 $44.58 (−4.3%) |
| Out of the money | **$9.35 (12.6%)** | **$3.56 (8.2%)** |
| Vendor bid / ask (SCREENING, Fidelity governs) | 1.40 / 1.80 · 25% wide · OI 34 · 8 traded today | 0.60 / 0.75 · 22% wide · OI 2,197 · 240 traded today |
| ×4 at the vendor bid, after $2.60 fees | ≈ $557.40 ⇒ ≈ −$125.25 | ≈ $237.40 ⇒ ≈ −$85.26 |
| Forward max loss (construction rule #20(d)) vs the $500 card cap | ≈ $560–640 ≈ 1.1–1.3× | ≈ $240–260, inside |
| Own Q3 print inside the tenor | **Mon 10/19 after the close, call Tue 10/20 12:00 ET — LOCKED** at the issuer release (Business Wire 10/06 09:00 ET, read in full by REGINALD via syndication; REGINALD packet `fe37dd785`, consumed 22:13 ET). REGINALD's 60-day realized vol 23.3% ⇒ ≈ 10.5% one-sd move to expiry (realized, not implied) | **Tue 10/20 after the close, call Wed 10/21 08:30 ET — CONFIRMED** by the OZK desk from OZK's 9/30 release (`AGENTS/OZK/CALENDAR.md`). REGINALD: 60-day realized vol 20.9% ⇒ ≈ 7.3% one-sd to expiry; OZK fell −4.31% on 10/6 vs KRE −0.45%, ~~cause UNKNOWN (no news found)~~ **cause found 10/8 (WALTER `SIG-W-20261008-017`, from the OZK desk; attribution INFERRED):** a Citi note on the **$915M RaDD loan's "Fifth Modification"** (filed San Diego County 10/2), which moved the maturity only to **Fri 2026-10-09**. Citi: *"a brief forbearance period"*; OZK's CCO: routine. ~~**📅 Fri10/9 — the bridge matures** (possible outcomes then unresolved)~~ → **L635 executed10/9 extension toDecember2029 with$100Mnew capital; earlier near-maturity-default hypothesis disconfirmed, recognition/redraw/appraisal limits below.** October20/21 are information events, not established future losses |
| Construction rule #18 (regional-bank print envelope: median 2–3%, 0 of 32 ≥ 10%) | **12.6% OTM: the print cannot be this strike's catalyst**; its payoff needs multi-quarter transmission, which the Dec tenor (≈ 50 sessions) partly spans | 8.2% OTM: inside 10%, beyond the median; a print alone reaches it only near the envelope's p95 (≲ 9%) |
| Exercise path if held in the money at expiry | 400 WAL at $65 = $26,000 short (IRA cannot carry; D-60 UNOBSERVED) | 400 OZK at $40 = $16,000 short (same) |

**Kept distinct (Will's instruction via PROME):** the **Robinhood WAL $70P Dec-18 ×1** (`TRY-WAL-ROLL70`, filled 9/02 @ $2.20, `GATE-TERRY-ROLL70-EXIT`) is a different account, strike and card; its Robinhood state is stale since 9/29 (FORGE D-47). Tonight's vendor quote for that strike, for reference only: 2.75 / 3.20.

**Book context, said once:** both lines join the same antecedent as the KRE 60P / 65P, APO 95P, HBAN 16P and the Robinhood WAL 70P — credit stress reaching regional banks. They add exposure, not diversification (N_eff stays 1). No fired registered trigger is on file for an add (durable finding 1; `TRY-COND-KREADD` read CONDITIONAL — NO FILL on 9/30 with REG-T-01 un-fired). **Recorded, not re-litigated.** The thesis owners are REGINALD (WAL, regional banks) and the OZK desk.

**APPROVAL REQUIRED — Will must approve/reject before execution** (no action is proposed).


## OZK evidence update — 2026-10-12 10:51:42 EDT

Primary issuer October12 Form8-K Item7.01p2 ([FDIC12019](https://securitiesfilings.fdicconnect.fdic.gov/api/instflng/12019/attachment/1)); web fetch unavailable at this desk, saved primary text `AGENTS/OZK/sources/2026-10-12/FDIC_FLNG_12019_8K.txt` read, saved PDF SHA256 verified13585c0379a619112e32c3776dad2bab89c56be4d47abc09ff985ea6fed19d01. Owner report `AGENTS/OZK/research/threads/2026-10-12_RADD_BRIDGE_OUTCOME.md`: agreement executed10/9 extending toDecember2029 with$100Mnew sponsor/partner capital. Largest-credit/$915M/SanDiego anchors identify RaDD, borrower name not literal in filing. Near-term maturity-default catalyst materially disconfirmed within November20 puts' life; OPEN prediction/unknown recognition is not affirmative support for holding.

Caveats retained: $121.3Mpaydown may all be readvanced; funded$579.1M/unfunded$335.9M/commitment$915M; 68.4% fully-funded LTV uses September as-stabilized appraisal, not current liquidation value. Provider identity/equity-vs-debt form, current leases and accounting/rating unknown. WQ395 extension leg MET, recognition legUNKNOWN (no<$140Mbound); no FALSE/Brier inferred. Next accounting resolverL520 October20AMC/October21 08:30ET and early-Nov10-Q. Existing OZK C5 deadline11/18 remains. No option re-mark, holdings refresh, new card/trade or threshold change.


## L690 bounded owner update — 2026-10-12 11:36:16 EDT

OZKpacket/memo `AGENTS/OZK/research/threads/2026-10-12_POST_EXTENSION_REVIEW.md` consumed as owner evidence: other-credit earnings/recognition risks survive, **no compelling specific near-term downside or confirmed large-loss catalyst established**. Q3 releaseOctober20AMC/callOctober21 08:30ET and early-Nov10-Q are information events, not assured loss events. Boston financing/title, OREOcash realization, named SMmigrations and earnings burden are pending tests; actual cures/cash sales at carrying/pass reversals weaken the case. All baselines Q2, no Q3 results assumed. No new option quote/card/salvage successor or order. C5November18 remains.

Horton current occupancy **UNRESOLVED**, not no tenants; Q1forecast243,000SF is not October lease-up. Redevelopment/permit obligations confound comparison with completed RaDD; historical credit bid/severity band is not a reverified cash sale or fresh loss estimate. WALTERCOR10scope scan found no current Horton carry at this desk; no numerical re-mark. L635paydown-redraw/appraisal/capital-source/recognition caveats above remain. OPEN/STUCK recognition is not affirmative bearish evidence.


## Machine-switch source/timing reconciliation — 2026-10-12T15:21:37-04:00

Committed OZK coordination packet **aea8a07a7**, full wrap-up handoff **41526df5e** and durability delivery **26ff20a0e** read and byte-matched. Current research passes are complete through available evidence; future Q3 outcomes remain pending. This annotates the obsolete October9 wording in the original table/STATUS, not a new valuation, card, salvage successor or sell/roll instruction. Existing C5 dates OZKNovember18/WALDecember16 and current-book requirements remain.

At the existing OZK Q3 read, use the owner's scoring card/baseline: Boston transaction cash versus bank-retained exposure; RaDD funding/accounting and redraw; actual recoveries/cures versus retained loans/OREO, then earnings/reserve/loss capacity. State counterevidence; proposed sale price and noncash transfers are not realized bank recovery, and unpublished recognition remains UNKNOWN. Funding form/provider/liquidity/full guarantees and authenticated closing/payoff gaps survive. No new score, probability, numerical option re-mark, capital action or holdings/fill inference. Original disclosure/source caveats above remain.


## October13 BOARD evidence integration — 2026-10-13 19:13:07 EDT

Full signals SIG-W-20261012-021/022/026 read. BPRE IQHQ common value$317,371,980 atJune30, subsequent$270,611,845 (disclosedAugust28, exact markdown dateUNKNOWN), derived−$46,760,135/14.7335%, is not an October seniorOZKloan loss. Alewife actualapproximately$111Madvance and conditional$134Mcapacity do not identify RaDDcapitalprovider or current runway; fundedinterest is not intrinsically impairment. These share a sponsorfinancing lineage, not independent new views.

Bounded contraryevidence: RenaissanceMilwaukeeWest brokerreports completedQ3sale (exactclosingdate/price/bankcashUNKNOWN); TheJack reported partnership lacks funding/recap proof;10Prospect signed10,500SFfirstlab lease/plannedmove does not prove occupancy/rent/bankpayoff. June$16.7Mhotel nonaccrual and proposedBoston$330Mversus dated$169.3Mcredit are historical/conditional bases. Do not manufacture current loss severity or cash cure. These weaken universal failed-close/no-partner/no-lease descriptions while preserving cash/retainedrisk/recognition tests. No new trade/card/price/grade; existingC5/Q3datesunchanged. October13brokerActivity confirmsOctober7OZKentry$322.65/WALentry$682.65; original entry decision/rationale remains unreconstructed, no rolllinkage inferred.


## 2026-10-14 21:07 ET — superseded as the management surface (WQ-425)
Will's word 2026-10-14 20:49 ET (*"Approve 425, spawn TERRY for the OZK and WAL cards"*) pulled both C5 dates forward to before each line's Q3 print. The management surfaces are now **`MGMT-OZK40P-NOV20`** (`setups/OZK40P_nov20-sell-or-roll_preprint_2026-10-14.md`: SELL ×4 before the Tue 10/20 print, no roll) and **`MGMT-WAL65P-DEC18`** (`setups/WAL65P_dec18-preprint-management_2026-10-14.md`: lean SELL ×4 before the Mon 10/19 print, HOLD ×4 priced as the alternative, no roll). This note stays as dated history; its entry fields remain UNRECOVERABLE. $0 moved, no order.
