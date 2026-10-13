# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> ✅ **2026-10-13 (Tue) — RECONCILE BY ANVIL to Will's Fidelity positions received Tuesday 10/13. Exact broker capture/mark time UNKNOWN; these marks are NOT certified live or closes.** Source `PROME/data/2026-10-13_broker-capture-TRANSCRIPTION.md`; no Activity or post-snapshot events supplied. Independently verified 18/18 value-minus-basis rows: positions **$21,409.49** + cash **$12,317.57** + pending **+$1.97** = **$33,729.03 to the cent**. Vs committed prior mirror: **3 NEW** (QQQ Oct-14 744P ×1; KRE Nov-27 67P ×4; CMG Oct-30 28P ×2), **3 GONE from this account view** (QQQ Oct-12 755C, QQQ Oct-15 745P, TLT Oct-16 82P; exit mechanism/realized UNKNOWN), **2 QTY CHANGE** (VLO 1→2; TBT 10→5), **13 MARK ONLY**. USO displayed last×qty differs from displayed value by 1¢; both source cells retained (D-79).
>
> ⚠️ **ACCOUNT SCOPE — Fidelity: ONE Traditional IRA; account id redacted, identity not independently verified. Robinhood Individual NOT provided — carried 9/29 rows unverified today; absence establishes no closure.**
>
> **Updated:** 2026-10-13 = receipt date only · marks = UNKNOWN (all Fidelity cells `[10/13 rcv]` = `[broker export received 2026-10-13; time UNKNOWN ET]`; exact capture time UNKNOWN) · **Fidelity cash (money market):** $12,317.57 (36.52%) + **Pending activity +$1.97** · **Fidelity account total:** $33,729.03 (Today +$407.34 / +1.22%; open G/L +$1,161.07 / +5.73%). Vs prior $33,284.88: **+$444.15 = positions +$910.06 + cash −$387.60 + pending −$78.31**; snapshot change, not daily/realized P&L. **No new realized result booked:** Activity missing for all changes. Prior derived realized 10/9 QQQ755P +$123.28, QQQ750C +$80.68 (already booked), USO150C −$298.67; three closes −$94.71. Oct-01 740P full-cohort +$142.44 (D-71), never additive over earlier partial bookings. Prior 10/11 Activity cash $12,785.45 was that vintage's cash+pending, not today's cash. **Robinhood:** $295.15 / BP $8.94 `[9/29 13:4x intraday]`, not re-captured. Prior mirror in git; rotations `_archive/STATUS_ROTATION_2026-10-11.md` and `_archive/STATUS_ROTATION_2026-10-08.md`; earlier rotations remain there.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (its own header names the current base and amendment count). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All cells `[10/13 rcv]` (received 2026-10-13, capture/mark time UNKNOWN); VLO/TBT QTY CHANGE, other four MARK ONLY versus prior mirror. Rounded average costs and percentages are preserved as displayed, not exact fills. Settled fill notes → rotation 10/01 chunk B.*

| Ticker | Type | Qty | Cost | Mark 10/13 rcv | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 10 | $23.65 | $341.29 | $3,412.90 | +$3,176.45 / +1343.39% | Today +$3.20; exact basis $236.45. 9/15 sale of 5 sh (≈+$1,534.92, derived) in rotation; pre-7/30 5-sh sale = D-1 |
| GLD | Stock | 17 | $374.74 | $381.75 | $6,489.75 | +$119.25 / +1.87% | Today −$6.80; exact basis $6,370.50. MIDAS domain; largest line by this capture’s value |
| USO | Stock | 37 | $122.28 | $152.748 | $5,651.67 | +$1,127.40 / +24.91% | Today +$63.56; exact basis $4,524.27. Last×37 rounds $5,651.68 vs displayed value $5,651.67 (D-79); source cells retained. **WQ-200 DECLINED by Will 9/10 — NO harvest/give-back rule live; Will manages by hand.** BRENT thesis (Hormuz-gap entry) |
| VLO | Stock | 2 | $426.00 | $454.47 | $908.94 | +$56.94 / +6.68% | Today +$36.94; exact basis $852.00. **QTY CHANGE 1→2**; net added basis $440 is NOT a verified fill. Entry/authorization/scope UNKNOWN (D-76/D-78). Original share bought 9/18 @ $412.00 (fill TIME not shown — D-55). **Historical Will confirmation 2026-10-07: “Yes, still one share”; superseded on quantity only by this two-share view.** WQ-213 originally 1 of 3; **its remaining 2-sh scale instruction was STAND DOWN** under `PROME/GATES.tsv` GATE-TERRY-VLO-SCALE, TERMINAL on the 9/25 F1 fire (TERRY 4ad672c43; its optional CME source-① override remains as written there). **The additional share does not autoapprove the terminal scale rule or establish extension of the original management scope. The originally held share's exit rule is `GATE-TERRY-VLO-HELD-01` — the letter (condition AND consequence cells, incl. who acts on each leg) is read at `PROME/GATES.tsv`, as amended by WQ-386 (`PROME/proposals/2026-10-07_VLO-december-management-RULED.md`, approved 10/7); nothing of it is restated here.** The gate reads the crack and the text, not the share's mark. The prior note, which restated the letter, is verbatim in rotation 10/08 chunk H |
| APD | Stock | 2 | $294.79 | $289.99 | $579.98 | −$9.59 / −1.63% | Today +$12.24; exact basis $589.57. Historical 10/1 "D" badge / $1.81 reference-price adjustment remains unverified; no dividend row in the 10/2–10/8 Activity. Thesis tag unassigned since 7/30 |
| TBT | Stock | 5 | $34.40 | $41.65 | $208.25 | +$36.24 / +21.06% | Today −$1.80; exact basis $172.01. **QTY CHANGE 10→5**, basis $346.46→$172.01; removed basis $174.45 is NOT proceeds. Transaction mechanism/fill/realized UNKNOWN (D-76). Duration-short leg (BOND/TERRY). **WQ-357 LATER 10/3 selected path C while BOND researches; 10/14 decision clock remains for the surviving holding, no new order inferred.** |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows — the VIX $20C/$25C spread (CLOSED 2026-07-30, realized −$111.60) and the five Aug-21-2026 EXPIRED rows (realized −$2,816.72 total) are terminal → rotation records.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent unless separately recorded. **SELL-OR-ROLL before expiry** (`USER.md`, 9/30 19:03 ET); TERRY recommends, Will orders. New QQQ/CMG rows have no contract-specific card/approval established by this capture; grouping is navigation, not a thesis or scope ruling. Last marks are not executable bids; working orders UNKNOWN. Receipt-day DTE is scheduling only; broker capture time UNKNOWN.

| Ticker | Strike | Expiry | Qty | Cost | Mark 10/13 rcv | Value | P&L | Note |
|--------|--------|--------|-----|------|---------------|-------|-----|------|
| USO | $150C | Oct-14-2026 | 2 | $1.88 | $2.97 | $594.00 | +$218.67 / +58.26% | `[10/13 rcv]`; MARK ONLY; BOUGHT OPEN 10/9 net −$375.33; exact basis $375.33. Today +$124.00. **Wednesday 10/14 expiry, 1 calendar DTE from receipt.** Distinct from closed Oct-09 call and 37 shares; no roll/linkage inferred. No inherited 10/09 hard stop; existing delivered TERRY card reused (PROME receipt); working order UNKNOWN |
| QQQ | $744P | Oct-14-2026 | 1 | $2.76 | $3.56 | $356.00 | +$80.34 / +29.14% | `[10/13 rcv]`; NEW; exact basis $275.66; Today +$63.00. **Wednesday 10/14 expiry, 1 calendar DTE.** Entry date/fill/working order UNKNOWN; new card requested by PROME, consumption unverified; SELL-OR-ROLL before expiry. No linkage to absent 745P or 755C inferred (D-76/D-77) |
| QQQ | $740P | Oct-15-2026 | 4 | $5.31 | $2.82 | $1,128.00 | −$994.65 / −46.86% | `[10/13 rcv]`; MARK ONLY; basis $2,122.65; bought 10/2 net −$2,122.65. Today +$180.00. **Thu 10/15 expiry, 2 calendar DTE.** `MGMT-QQQ740P-OCT15`: SELL-OR-ROLL BEFORE THURSDAY; Wed10/14 times remain a PROPOSAL for Will. If exercised: sell400 QQQ at$740 ($296,000), mechanics only, D-60 |
| CMG | $28P | Oct-30-2026 | 2 | $0.55 | $0.42 | $84.00 | −$25.33 / −23.17% | `[10/13 rcv]`; NEW; basis $109.33; Today −$14.00. 17 calendar DTE. Entry date/fill, thesis/desk ownership and contract-specific management approval UNKNOWN; no inferred replacement, research approval or trade card (D-76/D-77) |

*GONE from this account view, disposition UNKNOWN (D-76): QQQ Oct-12 755C ×1 (prior basis $144.66; BOUGHT OPEN10/9); QQQ Oct-15 745P ×1 (prior basis $283.66; BOUGHT OPEN10/7 ×2 net−$567.33, earlier1 sold10/8 net+$605.32 ⇒ +$321.65 derived). No close, expiry, roll/linkage or new realized P/L inferred. The passed10/12 expiry does not establish the 755C outcome. Prior `MGMT-QQQ745P-OCT15` deadline SELL-OR-ROLL before Thu10/15 and proposed Wed times are historical duties pending disposition reconciliation, not a claim of a currently held contract.*

*Oct-09 QQQ 755P/750C and USO 150C CLOSED by 10/9 sell-closing rows. Net proceeds $361.94 / $237.34 / $0.99 respectively; derived realized +$123.28 / +$80.68 / −$298.67. 750C +$80.68 already booked; USO “expired worthless” prior disposition superseded by sell-closing receipt. Gross prices, fill times and initiator UNKNOWN. Prior 10/8 realized +$918.30; Oct-02 740P −$886.90 and Oct-05 735P −$1,302.97 remain historical bookings. No exercise/short-stock outcome inferred.*

## Fidelity — Thesis Puts

*Instrument grouping is navigation, not approval: the Fidelity WAL/OZK rows below are Will-direct holdings (bought 10/7, Activity); thesis/desk ownership and management approval are NOT established by the broker view.*

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

*TLT $77P Sep-30 ×15 (TRY-FIRE-004's last lot): SOLD TO CLOSE 9/30 ⇒ −$154.64; no replacement TLT line; detail → rotation 10/01 chunk D.*

*TLT Oct-16 $82P ×1 is GONE from this account view; disposition/realized UNKNOWN (D-76). Prior exact basis $167.67; 9/28 prior1-of-2 sale @ $3.60 ⇒ +$191.66. WQ-357 LATER10/3 selected path C to10/14 while BOND researches; research delivered10/5 (`ff0992bf1`), not a new trade ruling. `MGMT-TLT82P-OCT16` / WQ-302 Wed10/14 close clock remains an unreconciled historical duty until disposition is evidenced, not an asserted current holding or cancellation. Prior2.50× last-mark multiple was not a price trigger; nothing adjudicated. ITM expiry handling remains UNOBSERVED (D-60).*

### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
*All four rows `[10/13 rcv]` (received 2026-10-13, capture/mark time UNKNOWN); new Nov27 row does not establish ownership/management approval. KRE $60P Sep-30 ×2 sold 9/30 @ $0.01 ⇒ −$451.48 (leg 1 of the roll into the Dec-31 65P; detail + the D-67 mark note → rotation 10/01 chunk D). Rail on the 65P: *"hard stop Thu 12/31 15:00 ET"* (`MGMT-KRE65P-DEC31`, `5ce609f80`).*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $67P | Nov-27-2026 | 4 | $1.28 | $1.23 | $492.00 | −$18.65 / −3.66% (today −$16.00). NEW; basis $510.65; entry date/fill/card UNKNOWN (D-76/D-77). Grouping under KRE is not desk ownership/approval. 45 calendar DTE from receipt10/13 |
| $60P | Dec-18-2026 | 2 | $2.57 | $0.49 | $98.00 | −$415.34 / −80.91% (today −$6.00). MARK ONLY; basis $513.34. 66 calendar DTE from receipt10/13 |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.49 | $147.00 | −$731.02 / −83.26% (today −$9.00) — multi-lot marker; basis $878.02; **five** Dec-18 KRE 60P across two lots. MARK ONLY. 66 calendar DTE from receipt10/13 |
| $65P | Dec-31-2026 | 2 | $1.69 | $1.47 | $294.00 | −$43.33 / −12.85% (today −$24.00) — MARK ONLY; basis $337.33. Bought 9/30 ×2 @ $1.68 (roll leg 2). Will's own add; `MGMT-KRE65P-DEC31` (`5ce609f80`): hard stop Thu 12/31 15:00 ET, not a price gate. 79 calendar DTE from receipt10/13 |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*$70P + $67.5P Sep-18 ×1 each: **EXPIRED as of 9/18, broker-confirmed** (ledger rows posted 9/21) ⇒ realized **−$768.67 and −$750.67 = −$1,519.34** (full basis) — the WQ-168 ①② LAPSE as ruled. Rows → rotation record. Duration roll = the Robinhood WAL Dec-18 $70P ×1 below. The RH WAL $77.5P Aug-21 sale: P&L UNRECORDED — D-18.*

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $1.05 | $105.00 | −$1,079.67 / −91.14% | `[10/13 rcv]`; basis $1,184.67; Today −$20.00. MARK ONLY; BROCK thesis vehicle. Will ruled HOLD 2026-08-13 (`PROME/proposals/2026-08-13_private-credit-batch-RULED.md` §②; vehicle-mismatch flag live). 66 calendar DTE from receipt10/13 |
| HBAN | $16P | Oct-16-2026 | 2 | $0.96 | $0.70 | $140.00 | −$51.34 / −26.84% | `[10/13 rcv]`; basis $191.34; Today +$14.00. MARK ONLY. The 7/18 ride-to-expiry premise failed per TERRY 9/26; `MGMT-HBAN16P-OCT16` / WQ-302 re-rule due **Wed 10/14**. Current moneyness not verified (no underlying quote in the view). 3 calendar DTE from receipt10/13 |
| OZK | $40P | Nov-20-2026 | 4 | $0.81 | $0.30 | $120.00 | −$202.65 / −62.81% | `[10/13 rcv]`; basis **$322.65** (10/7 view showed $322.66 — D-75); Today −$52.00. **Bought 10/7, −$322.65 (Activity); Will-direct.** Thesis/desk ownership and management approval UNRECORDED; holdings do not autoapprove research or a trade. Sell-or-roll before expiry; no contract-specific card recorded. 38 calendar DTE from receipt10/13 |
| WAL | $65P | Dec-18-2026 | 4 | $1.71 | $1.50 | $600.00 | −$82.65 / −12.11% | `[10/13 rcv]`; basis $682.65; Today +$60.00. **Bought 10/7, −$682.65 (Activity); Will-direct.** Thesis/desk ownership and management approval UNRECORDED; holdings do not autoapprove research or a trade. Sell-or-roll before expiry; no contract-specific card recorded. Distinct from Robinhood WAL Dec-18 $70P ×1. 66 calendar DTE from receipt10/13 |


## Robinhood — satellite account (Individual)

*All holdings/figures below retained from the 9/29 source; carried DTE annotations are historical, not a current freshness assertion.*

> ⚠️ **NOT CAPTURED IN THIS 10/13 RECEIPT (nor 10/11, 10/7, 10/1 or 9/30) — every cell below is the 9/29 card, unverified today.** 9/29 card: **account $295.15, BP $8.94** `[9/29 13:4x intraday]`; lines + BP = $290.15 ⇒ **$5.00 UNEXPLAINED (D-64)**. Per-line cost/value DERIVED from P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). The prediction-market line and the 9/01→9/25 dead-by-date bookings — USO $159C Sep-11 (bought 9/10, expired $0 — D-58) · QQQ $713C Sep-16 + USO $165C Sep-16 (both expired $0 — D-57) — verbatim → rotation 10/08 chunk B.

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — bought 9/02 @ $2.20 (RH activity) ✓ | ≈$265.00 *(derived; mark ≈$2.65)* | ✅ **ON CARD 9/29 — +$45.00 / +20.45%** | TRY-WAL-ROLL70 (filled in Robinhood). Guard **`GATE-TERRY-ROLL70-EXIT`** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last recorded here** (REGINALD through 9/23, per TERRY STATUS 9/24; not re-read this pass). The option's +20.45% is not the gate — the gate reads WAL's close (rule 7). **$4.40 GTC sell order: CANCELLED / not there — Will 9/28** (`PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`) ⇒ **no resting exit order; any take-profit is Will's manual act.** Time stop Fri 12/4. 78 DTE. **D-47** |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived ✓ | ≈$1.00 *(derived)* | ✅ **ON CARD 9/29 — −$52.00 / −98.11%** | Deep-OTM lottery; entry pre-7/16, never recorded — **D-54** (before the 9/01 activity view). 106 DTE |
| T | stock | 1 | — | — | ⚠️ no stocks card 9/29; no T row in RH activity 9/01→9/25 | Hypothesis: sold before 9/01, unconfirmed — **D-20**. The card no longer closes to the cent (D-64), so the 9/27 "no stock line" inference is weaker |

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. VLO ×1 (this section's only row since 9/19) moved to § Fidelity — Longs on the 9/25 ledger (D-55 account leg CLOSED). The section stays as the landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`).*

---

## ⚠️ Reconcile discrepancies (received 2026-10-13; capture/mark time UNKNOWN)

> Broker view > Will's word > desk record; conjectures labeled. Robinhood not captured. DTE from receipt10/13 only. **Permanently UNKNOWN by WQ-167 (never asks): 9/2 USO 135C sale price.** Immediately prior section → `867fa90e5:FORGE/STATUS.md`; earlier section byte-exact → `_archive/STATUS_ROTATION_2026-10-11.md`; carried duty detail → rotation 10/08 chunks D1/D2.

### Will supplies / PROME re-reads — facts owed

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| NEW | USO Oct-14 150C ×2 + QQQ Oct-14 744P ×1 | 🔴 Wednesday10/14, 1 calendar DTE | Values $594/$356; bases $375.33/$275.66; SELL-OR-ROLL before expiry | USO card already delivered per PROME; new QQQ card requested, consumption unverified; working orders UNKNOWN. No inherited Oct09 USO stop or roll linkage | **Will** orders; **TERRY** recommendations; PROME records |
| DATED | QQQ Oct-15 740P ×4 / HBAN Oct-16 16P ×2 / TBT5 | 🟠 Wednesday10/14 management, expiries10/15–16 | QQQ sell-or-roll before Thu; Wed times proposals. HBAN re-rule Wed; TBT surviving5 retain10/14 decision clock | Broker view does not approve/cancel management. Absent QQQ745P/TLT82P duties reconcile through D-76 | **Will / TERRY** |
| **D-60** | Fidelity future ITM expiry handling | 🔴 next expiries10/14–16 | Historical OPTION LIQUIDATION Oct09 QQQ755P/USO150C sell closes establish no policy. USO calls×2 exercise buys200 at$150 ($30,000); QQQ744P×1 exercise sells100 at$744 ($74,400), mechanics only. No QQQ/TLT shares in this view | Moneyness at liquidation, initiator, deterministic LIQUIDATE vs EXPIRED policy UNKNOWN; no future outcome inferred | **Will** — broker policy |
| **D-76** | Missing Activity: 3 absent contracts, 3 entries, VLO/TBT changes and cash flows | 🟠 expiry/disposition reconciliation first | QQQ755C Oct12, QQQ745P Oct15, TLT82P Oct16 absent; QQQ744P Oct14/KRE67P Nov27/CMG28P Oct30 new; VLO1→2, TBT10→5. Account snapshot +$444.15 ties its component bridge | Exit mechanism/fill/realized, entry dates, cash/pending flows UNKNOWN. VLO +$440 basis not fill; TBT $174.45 removed basis not proceeds. No roll linkage or new realized booking | **Will** supplies Activity; **PROME** records; **TERRY** reconciles management duties |
| **D-78** | VLO additional share authorization and management scope | 🟠 scope before action | Broker2 shares, basis$852. Original1-share WQ-213 holding and terminal GATE-TERRY-VLO-SCALE remain historical approved scope; original held-share rule referenced in Longs | Second-share entry/authorization UNKNOWN; capture does not override terminal scale rule or extend original gate to the additional share | **Will** authorization; **PROME / TERRY** scope reconciliation |
| **D-70** | Management mappings/cards follow-through | 🟡 review | Every changed source hash withholds old mappings until PROME re-review; QQQ740P retains proposal/deadline distinction; absent rows cannot remain live mappings | Receipt/consumption requires PROME verification; holdings never approve a card | **PROME** mapping re-review; **TERRY** cards |
| **D-77** | New QQQ744P / KRE67P / CMG28P ownership and cards | 🟠 QQQ10/14; other rows record | New positions verified; bases$275.66/$510.65/$109.33; grouping is navigation | Contract-specific card/approval/desk ownership unestablished; no inferred research approval or replacement linkage | **PROME** routes scope; **Will / TERRY** |
| **D-74** | Fidelity bank-put ownership/management | 🟡 record | WAL Dec18 65P×4 basis$682.65/value$600; OZK Nov20 40P×4 basis$322.65/value$120. Bought10/7; Will-direct | Thesis/desk owner/approval unestablished; no autoapproved research/trade | **PROME** routes scope; **Will / TERRY** |
| **D-79** | USO displayed quote/value precision | 🟡 record | Source last$152.748×37=$5,651.676→$5,651.68; displayed value$5,651.67. Displayed value−basis=$1,127.40 and account sum tie exactly | Hidden quote precision/asynchronous fields possible, UNVERIFIED; neither source cell altered | **PROME** retains evidence; broker detail if available |
| **D-75 · D-66 · D-69 · D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1** | **Carried discrepancies (18) — every row still OPEN; rows verbatim → rotation 10/08 chunk D1 (D-75) + D2 (the other 17)** | 🟡 carried | None closed, re-dated or re-owned; every cell unchanged in the record. Ticker-bearing items, for the text scan: STNG (D-17) · RH QQQ $715P Aug-31 (D-28) · RH KRE $25P entry (D-54) · RH WAL $77.5P Aug-21 sale (D-18) · the RH T share (D-20) · AAPL 5-sh sale pre-7/30 (D-1) · D-75 (OZK 40P basis 1¢; mirror carries $322.65, record only) | Returns to this table when its state changes | As recorded, per row: **Will** — D-66 · D-69 · D-63 · D-64 · D-61 · D-59 · D-45 · D-55 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1; **RH history before 9/01** — D-28; **PROME** — D-62 · D-65 (re-reads of desktop-local images) · D-75 (record) |

*D-69 remains OPEN: the supplied 9/30→10/1 Activity still lacks +$53.54 (latest 9/30 $14,094.06 − Oct1 buy $890.65 = $13,203.41 versus $13,256.95 shown). No dividend/adjustment invented; Will supplies missing row. D-66 also retains all fill-time/gross-price unknowns, including10/9 entries/exits; new10/13-view transaction gaps also tracked in D-76. D-75 remains record-only, unchanged $322.65 basis confirmed. No carried duty closed by silence.*

*D-71 broker-evidence leg CLOSED: four Oct1 QQQ740P sell-closing cash rows $343.34 + $396.34 + $1,113.98 + $22.75 = $1,876.41 against Sep30 opening $1,733.97 ⇒ full-cohort realized +$142.44. Prior final-lot-only inferred −$747.91 is superseded as a cohort result; do not double-book earlier partial results. Quantities per fill, times and gross prices absent, not inferred; record under D-66. WQ-347 evidence now supplied. WQ-397 disposition supplied: remaining QQQ755P sold close net $361.94; full 755P cohort +$719.93. USO full Oct09 cohort −$207.00; WQ-396 earlier worthless word is history, not broker outcome. PROME updates decision records; ANVIL does not.*

*Owner decisions/guards remain: D-47 RH WAL70P gate `GATE-TERRY-ROLL70-EXIT`, last recorded 0-of-3, no resting exit, time stop12/4; REGINALD grades/TERRY proposes/Will harvests. VLO original held-share gate and terminal scale instruction in Longs/GATES remain; additional-share scope UNKNOWN (D-78); WQ-200 USO stock no rule live; APD tag/adjustment unverified. D-72/D-73 prior closures remain history → rotation10/08 chunkF.*

---

## Immediate Actions (10/13 receipt; marks not live/close)

| Item | State | Owner |
|---|---|---|
| 🔴 USO Oct14 150C×2 + QQQ Oct14 744P×1 — SELL-OR-ROLL before Wednesday expiry; USO card delivered; new QQQ card requested; working orders UNKNOWN | 1 calendar DTE | **Will / TERRY** |
| 🟠 QQQ Oct15 740P×4 — SELL-OR-ROLL before Thursday; Wed times proposals only | 2 calendar DTE | **Will / TERRY** |
| 🟠 HBAN16P×2 re-rule Wed10/14, Fri10/16 expiry; TBT5 retain10/14 decision clock | dated | **Will / TERRY** |
| 🔴 D-60 — future ITM handling UNKNOWN; liquidation history establishes no deterministic policy | next expiries | **Will** broker policy |
| 🟠 D-76 — Activity needed for3 absent contracts,3 entries,VLO/TBT changes,cash/pending; no new realized result | disposition/evidence | **Will** supplies; **PROME / TERRY** reconcile |
| 🟠 D-78 — VLO second share is real; authorization/management scope UNKNOWN; terminal scale instruction not autoapproved | scope | **Will / PROME / TERRY** |
| 🟡 D-70/D-74/D-77 — mappings/cards/ownership; all18 carried discrepancies stay OPEN; D-69 missing+$53.54; D-79 quote precision; Robinhood stale | integration/evidence | **PROME / TERRY / Will** |

---

*History → `_archive/JOURNAL.md` | Prior reconciles in git history + `_archive/`; immediately prior whole mirror = `git show 867fa90e5479f1ca0eb2229bb994b8701ac47bda:FORGE/STATUS.md` | Full-portfolio Feb snapshot → `PORTFOLIO.md` (**FROZEN/superseded, historical only — never cite as live**) | Position truth = Will/broker direct (off-repo) | Marks-of-record transcription → `PROME/data/2026-10-13_broker-capture-TRANSCRIPTION.md` (Fidelity positions received Tuesday10/13; exact capture/mark time UNKNOWN; no Activity supplied); prior `…2026-10-11_…` (positions + Activity) · `…2026-10-07_…` · `…2026-10-01b_…` (post-close) · `…2026-10-01_…` (intraday + Pending list) · `…_2026-09-30_…` · `…_2026-09-29_…` (RH rows' source)*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(Pass notes 9/27 → 10/8 → rotation 10/08 chunk G. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows.)*
