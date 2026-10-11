# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> ✅ **2026-10-11 (Sun) — RECONCILE BY ANVIL to Will's Fidelity positions + Activity received Sunday 10/11. Exact broker capture/mark time UNKNOWN; these marks are NOT certified live or closes.** Source `PROME/data/2026-10-11_broker-capture-TRANSCRIPTION.md`. Independently verified 18/18 rows: positions **$20,499.43** + cash **$12,705.17** + pending **+$80.28** = **$33,284.88 to the cent**. Vs committed prior mirror: **2 NEW** (QQQ Oct-12 755C ×1; USO Oct-14 150C ×2), **3 GONE** (Oct-09 QQQ 755P/750C, USO 150C; matching sell-closing rows), **16 MARK ONLY**, no surviving quantity changes.
>
> ⚠️ **ACCOUNT SCOPE — Fidelity: ONE Traditional IRA; account id redacted, identity not independently verified. Robinhood Individual NOT provided — carried 9/29 rows unverified today; absence establishes no closure.**
>
> **Updated:** 2026-10-11 = receipt date only · marks = UNKNOWN (all Fidelity cells `[10/11 rcv]`; exact capture time UNKNOWN) · **Fidelity cash (money market):** $12,705.17 (38.17%) + **Pending activity +$80.28** · **Fidelity account total:** $33,284.88 (Today −$928.22. / −2.71%; open G/L +$816.21 / +4.15%). Vs prior $34,650.69: −$1,365.81 = positions −$1,446.09 + cash +$1,283.98 + pending −$1,203.70; snapshot change, not P&L. **Derived realized 10/9:** QQQ 755P +$123.28; QQQ 750C +$80.68 (already booked, no duplicate); USO 150C −$298.67; three closes total **−$94.71**. Oct-01 740P full cohort **+$142.44** newly supported (D-71); do not add that full cohort over earlier partial bookings. Activity latest cash **$12,785.45 = cash + pending**, not additional cash. **Robinhood:** $295.15 / BP $8.94 `[9/29 13:4x intraday]`, not re-captured. Prior mirror in git; rotations `_archive/STATUS_ROTATION_2026-10-11.md` and `_archive/STATUS_ROTATION_2026-10-08.md`; earlier rotations remain there.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (its own header names the current base and amendment count). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All cells `[10/11 rcv]` (received 2026-10-11, capture/mark time UNKNOWN); all six MARK ONLY versus prior mirror. Rounded average costs and percentages are preserved as displayed, not exact fills. Settled fill notes → rotation 10/01 chunk B.*

| Ticker | Type | Qty | Cost | Mark 10/11 rcv | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 10 | $23.65 | $336.64 | $3,366.40 | +$3,129.95 / +1323.72% | Today −$37.80. 9/15 sale of 5 sh (≈+$1,534.92, derived) in rotation; pre-7/30 5-sh sale = D-1 |
| GLD | Stock | 17 | $374.74 | $384.58 | $6,537.86 | +$167.36 / +2.62% | Today +$101.32. MIDAS domain; largest line by this capture’s value |
| USO | Stock | 37 | $122.28 | $148.20 | $5,483.40 | +$959.13 / +21.19% | Today +$22.94. **WQ-200 DECLINED by Will 9/10 — NO harvest/give-back rule live; Will manages by hand.** BRENT thesis (Hormuz-gap entry) |
| VLO | Stock | 1 | $412.00 | $433.75 | $433.75 | +$21.75 / +5.27% | Today −$10.05. Bought 9/18 @ $412.00 (fill TIME not shown — D-55). **Holding confirmed by Will 2026-10-07: “Yes, still one share”**. WQ-213: 1 of 3; **the remaining 2 sh STAND DOWN** under `PROME/GATES.tsv` GATE-TERRY-VLO-SCALE, TERMINAL on the 9/25 F1 fire (TERRY 4ad672c43; its optional CME source-① override remains as written there). **The held share's exit rule is `GATE-TERRY-VLO-HELD-01` — the letter (condition AND consequence cells, incl. who acts on each leg) is read at `PROME/GATES.tsv`, as amended by WQ-386 (`PROME/proposals/2026-10-07_VLO-december-management-RULED.md`, approved 10/7); nothing of it is restated here.** The gate reads the crack and the text, not the share's mark. The prior note, which restated the letter, is verbatim in rotation 10/08 chunk H |
| APD | Stock | 2 | $294.79 | $281.26 | $562.52 | −$27.05 / −4.59% | Today +$5.76. Historical 10/1 "D" badge / $1.81 reference-price adjustment remains unverified; no dividend row in the 10/2–10/8 Activity. Thesis tag unassigned since 7/30 |
| TBT | Stock | 10 | $34.65 | $42.05 | $420.50 | +$74.04 / +21.37% | Today −$1.40. Duration-short leg (BOND/TERRY). **WQ-357 LATER 10/3: HELD on path C while BOND researches; 10/14 decision clock remains; no exit order inferred.** |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows — the VIX $20C/$25C spread (CLOSED 2026-07-30, realized −$111.60) and the five Aug-21-2026 EXPIRED rows (realized −$2,816.72 total) are terminal → rotation records.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent. **SELL-OR-ROLL before expiry** (`USER.md`, 9/30 19:03 ET); TERRY recommends, Will orders. New calls have no contract-specific card/approval established by this capture. Last marks are not executable bids; working orders UNKNOWN. Receipt-day DTE is scheduling only; broker capture time UNKNOWN.

| Ticker | Strike | Expiry | Qty | Cost | Mark 10/11 rcv | Value | P&L | Note |
|--------|--------|--------|-----|------|---------------|-------|-----|------|
| QQQ | $755C | Oct-12-2026 | 1 | $1.45 | $0.86 | $86.00 | −$58.66 / −40.56% | `[10/11 rcv]`; NEW; BOUGHT OPEN 10/9 net −$144.66; exact basis $144.66. Today −$58.66. **Monday 10/12 expiry, 1 calendar DTE from receipt.** Sell-or-roll before expiry; no linkage/roll inferred. Card/working order UNKNOWN; D-60 policy unknown |
| USO | $150C | Oct-14-2026 | 2 | $1.88 | $2.09 | $418.00 | +$42.67 / +11.36% | `[10/11 rcv]`; NEW; BOUGHT OPEN 10/9 net −$375.33; exact basis $375.33. Today +$42.67. **Wednesday 10/14 expiry, 3 calendar DTE from receipt.** Distinct from closed Oct-09 call and 37 shares; no roll/linkage inferred. No inherited 10/09 hard stop; card/order UNKNOWN |
| QQQ | $745P | Oct-15-2026 | 1 | $2.84 | $2.93 | $293.00 | +$9.34 / +3.29% | `[10/11 rcv]`; MARK ONLY; basis $283.66; Today −$230.00. Bought 10/7 net −$567.33; prior 1 sold 10/8 net +$605.32, realized +$321.65 derived. **Thu 10/15 expiry, 4 calendar DTE from receipt.** `MGMT-QQQ745P-OCT15`: SELL-OR-ROLL BEFORE THURSDAY 10/15; Wed 10/14 times remain a PROPOSAL for Will |
| QQQ | $740P | Oct-15-2026 | 4 | $5.31 | $1.78 | $712.00 | −$1,410.65 / −66.46% | `[10/11 rcv]`; MARK ONLY; basis $2,122.65; bought 10/2 net −$2,122.65. Today −$756.00. **Thu 10/15 expiry, 4 calendar DTE from receipt.** `MGMT-QQQ740P-OCT15`, same rail/caveat as 745P. If exercised: sell 400 QQQ at $740 ($296,000), mechanics only, D-60 |

*Oct-09 QQQ 755P/750C and USO 150C CLOSED by 10/9 sell-closing rows. Net proceeds $361.94 / $237.34 / $0.99 respectively; derived realized +$123.28 / +$80.68 / −$298.67. 750C +$80.68 already booked; USO “expired worthless” prior disposition superseded by sell-closing receipt. Gross prices, fill times and initiator UNKNOWN. Prior 10/8 realized +$918.30; Oct-02 740P −$886.90 and Oct-05 735P −$1,302.97 remain historical bookings. No exercise/short-stock outcome inferred.*

## Fidelity — Thesis Puts

*Instrument grouping is navigation, not approval: the Fidelity WAL/OZK rows below are Will-direct holdings (bought 10/7, Activity); thesis/desk ownership and management approval are NOT established by the broker view.*

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

*TLT $77P Sep-30 ×15 (TRY-FIRE-004's last lot): SOLD TO CLOSE 9/30 ⇒ −$154.64; no replacement TLT line; detail → rotation 10/01 chunk D.*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $82P | Oct-16-2026 | 1 | $1.68 | $4.20 | $420.00 | +$252.33 / +150.49% (today +$0.00) `[10/11 rcv]`. MARK ONLY; basis $167.67. 9/28: sold 1 of 2 @ $3.60 ⇒ +$191.66. **WQ-357 LATER 10/3 selects path C: HELD to 10/14 while BOND researches.** Research delivered 10/5 (`ff0992bf1`), not a new trade ruling. `MGMT-TLT82P-OCT16` (×2 original, ×1 remaining) / WQ-302: **Wed 10/14 close** clock remains; no undecided A/B/C choice asserted here. 2.50× basis is a last-mark multiple, not a price trigger; nothing adjudicated. ITM expiry handling in the IRA UNOBSERVED (D-60). 5 calendar DTE from receipt 10/11 |

### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
*All three rows `[10/11 rcv]` (received 2026-10-11, capture/mark time UNKNOWN). KRE $60P Sep-30 ×2 sold 9/30 @ $0.01 ⇒ −$451.48 (leg 1 of the roll into the Dec-31 65P; detail + the D-67 mark note → rotation 10/01 chunk D). Rail on the 65P: *"hard stop Thu 12/31 15:00 ET"* (`MGMT-KRE65P-DEC31`, `5ce609f80`).*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $60P | Dec-18-2026 | 2 | $2.57 | $0.70 | $140.00 | −$373.34 / −72.73% (today +$10.00). MARK ONLY; basis $513.34. 68 calendar DTE from receipt 10/11 |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.70 | $210.00 | −$668.02 / −76.09% (today +$15.00) — multi-lot marker; basis $878.02; **five** Dec-18 KRE 60P across two lots. MARK ONLY. 68 calendar DTE from receipt 10/11 |
| $65P | Dec-31-2026 | 2 | $1.69 | $1.27 | $254.00 | −$83.33 / −24.71% (today +$0.00) — MARK ONLY; basis $337.33. Bought 9/30 ×2 @ $1.68 (roll leg 2). Will's own add; `MGMT-KRE65P-DEC31` (`5ce609f80`): hard stop Thu 12/31 15:00 ET, not a price gate. 81 calendar DTE from receipt 10/11 |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*$70P + $67.5P Sep-18 ×1 each: **EXPIRED as of 9/18, broker-confirmed** (ledger rows posted 9/21) ⇒ realized **−$768.67 and −$750.67 = −$1,519.34** (full basis) — the WQ-168 ①② LAPSE as ruled. Rows → rotation record. Duration roll = the Robinhood WAL Dec-18 $70P ×1 below. The RH WAL $77.5P Aug-21 sale: P&L UNRECORDED — D-18.*

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $1.44 | $144.00 | −$1,040.67 / −87.85% | `[10/11 rcv]`; basis $1,184.67; Today +$0.00. MARK ONLY; BROCK thesis vehicle. Will ruled HOLD 2026-08-13 (`PROME/proposals/2026-08-13_private-credit-batch-RULED.md` §②; vehicle-mismatch flag live). 68 calendar DTE from receipt 10/11 |
| HBAN | $16P | Oct-16-2026 | 2 | $0.96 | $0.75 | $150.00 | −$41.34 / −21.61% | `[10/11 rcv]`; basis $191.34; Today +$0.00. MARK ONLY. The 7/18 ride-to-expiry premise failed per TERRY 9/26; `MGMT-HBAN16P-OCT16` / WQ-302 re-rule due **Wed 10/14**. Current moneyness not verified (no underlying quote in the view). 5 calendar DTE from receipt 10/11 |
| OZK | $40P | Nov-20-2026 | 4 | $0.81 | $0.47 | $188.00 | −$134.65 / −41.74% | `[10/11 rcv]`; basis **$322.65** (10/7 view showed $322.66 — D-75); Today −$32.00. **Bought 10/7, −$322.65 (Activity); Will-direct.** Thesis/desk ownership and management approval UNRECORDED; holdings do not autoapprove research or a trade. Sell-or-roll before expiry; no contract-specific card recorded. 40 calendar DTE from receipt 10/11 |
| WAL | $65P | Dec-18-2026 | 4 | $1.71 | $1.70 | $680.00 | −$2.65 / −0.39% | `[10/11 rcv]`; basis $682.65; Today +$0.00. **Bought 10/7, −$682.65 (Activity); Will-direct.** Thesis/desk ownership and management approval UNRECORDED; holdings do not autoapprove research or a trade. Sell-or-roll before expiry; no contract-specific card recorded. Distinct from Robinhood WAL Dec-18 $70P ×1. 68 calendar DTE from receipt 10/11 |


## Robinhood — satellite account (Individual)

*All holdings/figures below retained from the 9/29 source; carried DTE annotations are historical, not a current freshness assertion.*

> ⚠️ **NOT CAPTURED IN THIS 10/11 RECEIPT (nor 10/7, 10/1 or 9/30) — every cell below is the 9/29 card, unverified today.** 9/29 card: **account $295.15, BP $8.94** `[9/29 13:4x intraday]`; lines + BP = $290.15 ⇒ **$5.00 UNEXPLAINED (D-64)**. Per-line cost/value DERIVED from P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). The prediction-market line and the 9/01→9/25 dead-by-date bookings — USO $159C Sep-11 (bought 9/10, expired $0 — D-58) · QQQ $713C Sep-16 + USO $165C Sep-16 (both expired $0 — D-57) — verbatim → rotation 10/08 chunk B.

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — bought 9/02 @ $2.20 (RH activity) ✓ | ≈$265.00 *(derived; mark ≈$2.65)* | ✅ **ON CARD 9/29 — +$45.00 / +20.45%** | TRY-WAL-ROLL70 (filled in Robinhood). Guard **`GATE-TERRY-ROLL70-EXIT`** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last recorded here** (REGINALD through 9/23, per TERRY STATUS 9/24; not re-read this pass). The option's +20.45% is not the gate — the gate reads WAL's close (rule 7). **$4.40 GTC sell order: CANCELLED / not there — Will 9/28** (`PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`) ⇒ **no resting exit order; any take-profit is Will's manual act.** Time stop Fri 12/4. 78 DTE. **D-47** |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived ✓ | ≈$1.00 *(derived)* | ✅ **ON CARD 9/29 — −$52.00 / −98.11%** | Deep-OTM lottery; entry pre-7/16, never recorded — **D-54** (before the 9/01 activity view). 106 DTE |
| T | stock | 1 | — | — | ⚠️ no stocks card 9/29; no T row in RH activity 9/01→9/25 | Hypothesis: sold before 9/01, unconfirmed — **D-20**. The card no longer closes to the cent (D-64), so the 9/27 "no stock line" inference is weaker |

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. VLO ×1 (this section's only row since 9/19) moved to § Fidelity — Longs on the 9/25 ledger (D-55 account leg CLOSED). The section stays as the landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`).*

---

## ⚠️ Reconcile discrepancies (received 2026-10-11; capture/mark time UNKNOWN)

> Broker view > Will's word > desk record; conjectures labeled. Robinhood not captured. DTE from receipt 10/11 only. **Permanently UNKNOWN by WQ-167 (never asks): 9/2 USO 135C sale price.** Prior section byte-exact → `_archive/STATUS_ROTATION_2026-10-11.md`; carried duty detail → rotation 10/08 chunks D1/D2.

### Will supplies / PROME re-reads — facts owed

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| NEW | QQQ Oct-12 755C ×1 | 🔴 Monday 10/12, 1 calendar DTE | Basis $144.66; value $86.00; bought 10/9. SELL-OR-ROLL before expiry | Card, working order and approval UNKNOWN; no roll/linkage inferred | **Will** orders; **TERRY** recommendations; PROME records |
| NEW | USO Oct-14 150C ×2 | 🟠 Wednesday 10/14, 3 calendar DTE | Basis $375.33; value $418.00; bought 10/9. SELL-OR-ROLL before expiry | No inherited Oct-09 hard stop, stock rule or inferred roll | **Will** orders; **TERRY** recommendations |
| **D-60** | Fidelity future ITM expiry handling | 🔴 next expiries 10/12–16 | New OPTION LIQUIDATION sell closes: Oct-09 QQQ 755P and USO 150C; these close holdings, not establish a policy. No QQQ/TLT shares in IRA view. QQQ call ×1 exercise buys 100 shares at $755 ($75,500); USO call ×2 buys 200 at $150 ($30,000), mechanics only | Moneyness at liquidation, initiator and deterministic LIQUIDATE vs EXPIRED policy UNKNOWN | **Will** — broker policy |
| **D-70** | Management mappings/cards follow-through | 🟡 review | Every changed source hash withholds old mappings until PROME re-review; new call cards not established; surviving QQQ put cards retain proposal/deadline distinction | Receipt/consumption needs PROME verification; holdings never approve a card | **PROME** mapping re-review; **TERRY** cards |
| **D-74** | Fidelity bank-put ownership/management | 🟡 record | WAL Dec-18 65P ×4 basis $682.65, value $680; OZK Nov-20 40P ×4 basis $322.65, value $188. Bought 10/7; Will-direct | Thesis/desk owner/approval unestablished; no autoapproved research/trade | **PROME** routes scope; **Will / TERRY** |
| **D-75 · D-66 · D-69 · D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1** | **Carried discrepancies (18) — every row still OPEN; rows verbatim → rotation 10/08 chunk D1 (D-75) + D2 (the other 17)** | 🟡 carried | None closed, re-dated or re-owned; every cell unchanged in the record. Ticker-bearing items, for the text scan: STNG (D-17) · RH QQQ $715P Aug-31 (D-28) · RH KRE $25P entry (D-54) · RH WAL $77.5P Aug-21 sale (D-18) · the RH T share (D-20) · AAPL 5-sh sale pre-7/30 (D-1) · D-75 (OZK 40P basis 1¢; mirror carries $322.65, record only) | Returns to this table when its state changes | As recorded, per row: **Will** — D-66 · D-69 · D-63 · D-64 · D-61 · D-59 · D-45 · D-55 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1; **RH history before 9/01** — D-28; **PROME** — D-62 · D-65 (re-reads of desktop-local images) · D-75 (record) |

*D-69 remains OPEN: the supplied 9/30→10/1 Activity still lacks +$53.54 (latest 9/30 $14,094.06 − Oct1 buy $890.65 = $13,203.41 versus $13,256.95 shown). No dividend/adjustment invented; Will supplies missing row. D-66 also retains all fill-time/gross-price unknowns, now including new 10/9 entries and exits. D-75 remains record-only, unchanged $322.65 basis confirmed. No carried duty closed by silence.*

*D-71 broker-evidence leg CLOSED: four Oct1 QQQ740P sell-closing cash rows $343.34 + $396.34 + $1,113.98 + $22.75 = $1,876.41 against Sep30 opening $1,733.97 ⇒ full-cohort realized +$142.44. Prior final-lot-only inferred −$747.91 is superseded as a cohort result; do not double-book earlier partial results. Quantities per fill, times and gross prices absent, not inferred; record under D-66. WQ-347 evidence now supplied. WQ-397 disposition supplied: remaining QQQ755P sold close net $361.94; full 755P cohort +$719.93. USO full Oct09 cohort −$207.00; WQ-396 earlier worthless word is history, not broker outcome. PROME updates decision records; ANVIL does not.*

*Owner decisions/guards remain: D-47 RH WAL70P gate `GATE-TERRY-ROLL70-EXIT`, last recorded 0-of-3, no resting exit, time stop12/4; REGINALD grades/TERRY proposes/Will harvests. VLO held-share gate and terminal scale instruction in Longs/GATES remain; WQ-200 USO stock no rule live; APD tag/adjustment unverified. D-72/D-73 prior closures remain history → rotation10/08 chunkF.*

---

## Immediate Actions (10/11 receipt; marks not live/close)

| Item | State | Owner |
|---|---|---|
| 🔴 QQQ Oct-12 755C ×1 — SELL-OR-ROLL before Monday expiry; no card/working order established | 1 calendar DTE from receipt | **Will / TERRY** |
| 🟠 USO Oct-14 150C ×2 — SELL-OR-ROLL before Wednesday expiry; no inherited Oct09 hard stop | 3 calendar DTE | **Will / TERRY** |
| 🟠 QQQ Oct-15 745P ×1 + 740P ×4 — SELL-OR-ROLL before Thursday; Wed times proposals only | 4 calendar DTE | **Will / TERRY** |
| 🟠 TLT82P ×1 path C / HBAN16P ×2 — Wed10/14 management/re-rule clock, Fri10/16 expiry; TBT path C retains10/14 clock | dated | **Will / TERRY** |
| 🔴 D-60 — future ITM handling remains UNKNOWN despite two further liquidation receipts | next expiries | **Will** broker policy |
| 🟡 D-70 / D-74 — mappings/cards/ownership; all18 carried discrepancies stay OPEN at owners above; D-69 missing+$53.54; Robinhood stale | integration / evidence | **PROME / TERRY / Will** |

---

*History → `_archive/JOURNAL.md` | Prior reconciles in git history + `_archive/`; immediately prior whole mirror = `git show 0bbcf6aa292941e867c86cc8e53a1a15f5e1274c:FORGE/STATUS.md` | Full-portfolio Feb snapshot → `PORTFOLIO.md` (**FROZEN/superseded, historical only — never cite as live**) | Position truth = Will/broker direct (off-repo) | Marks-of-record transcription → `PROME/data/2026-10-11_broker-capture-TRANSCRIPTION.md` (Fidelity positions + Activity received Sunday10/11; exact capture/mark time UNKNOWN); prior `…2026-10-07_…` · `…2026-10-01b_…` (post-close) · `…2026-10-01_…` (intraday + Pending list) · `…_2026-09-30_…` · `…_2026-09-29_…` (RH rows' source)*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(Pass notes 9/27 → 10/8 → rotation 10/08 chunk G. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows.)*
