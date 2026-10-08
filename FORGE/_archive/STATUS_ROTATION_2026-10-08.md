# FORGE/STATUS.md — ROTATION RECORD 2026-10-08 (read-cap relief; superseded or cold 10/8-reconcile material, verbatim)

> **Source:** `FORGE/STATUS.md` as committed at `ef2bc83f1` (the 10/8 intraday reconcile; the later mappings pass a1eb75287 changed only `FORGE/position_management.tsv`; working file byte-identical to HEAD at rotation start — `git diff --quiet -- FORGE/STATUS.md` clean; receipt: `git show ef2bc83f1:FORGE/STATUS.md`). **Rotated:** 2026-10-08 evening by PROME (`prome-07`, laptop), NOT inside a reconcile — no position, mark, quantity or basis changes; plan + reads: `PROME/plans/2026-10-08_forge-status-rotation-PLAN.md`. **Reason:** read-cap relief — the live file measured 32,523 B = 100% of the 32,550 B budget (`scripts/read_cap_check.py FORGE/STATUS.md`, rotate-tier) with Friday 10/9 fills to book next. **Every chunk below is COLD or SUPERSEDED in the hot file by a pointer or a shorter restatement; every OPEN obligation it carries is still OPEN at its owner — the plan's obligation audit names where each survives. Cite as history, never as current.**
>
> **Chunks are verbatim source line ranges** (each line newline-terminated as in source; the single blank line between chunks is the separator, not source). Receipts = `PROME/tools/measure.py` semantics over each chunk as extracted, before insertion (bytes = UTF-8 incl. the final newline; crc32 over the same bytes):
> - **Chunk A** — source line 5 (the 10/8 reconcile banner paragraph (ANVIL verification receipt)): **1084 B · crc32 3510813514**
> - **Chunk B** — source line 94 (§ Robinhood NOT-CAPTURED blockquote (9/29 card detail, prediction-market line, dead-by-date bookings)): **842 B · crc32 2632567345**
> - **Chunk C** — source lines 112–121 (§ Reconcile discrepancies → ### EXPIRING subsection (header, table, 6 rows incl. D-60)): **2926 B · crc32 2591328773**
> - **Chunk D1** — source line 128 (facts-owed row D-75 (OZK basis 1¢, record-only)): **523 B · crc32 2218341014**
> - **Chunk D2** — source lines 131–147 (facts-owed rows D-66 · D-69 and the 15 carried rows D-62 → D-1): **4007 B · crc32 487926030**
> - **Chunk E** — source lines 149–156 (### Owner decides — ruled / gated subsection (header, table, D-47 · WQ-386/VLO-SCALE · WQ-200 · APD)): **1664 B · crc32 2660099432**
> - **Chunk F** — source lines 158–162 (### CLOSED this pass (D-72 · D-73 · the 10/8 QTY/NEW/MARK summary)): **936 B · crc32 2479073510**
> - **Chunk G** — source line 183 (the PARSED-BY-MACHINE footer line (consumer registry + pass notes)): **1772 B · crc32 89507236**
> - **Chunk H** — source line 28 (§ Longs VLO row (the full prior owner note)): **1172 B · crc32 2811584083**
> - **Chunk I** — source lines 174–177 (§ Immediate Actions — the four 🟡 discrepancy rows as built 10/8): **521 B · crc32 365315039**

## Chunk A — source line 5

> ✅ **2026-10-08 (Thu) — RECONCILE BY ANVIL to Will's Fidelity capture RECEIVED ≤15:26 ET TODAY: positions + Activity ("Pending" + "Past 30 days"). INTRADAY; exact capture time UNKNOWN; marks are NOT closes.** Source `PROME/data/2026-10-08_broker-capture-TRANSCRIPTION.md` (WALTER verbatim §①, PROME tie §②); both images viewed independently by ANVIL and match §①. All Fidelity cells `[10/8 rcv]` = `[broker capture 2026-10-08 intraday, received ≤15:26 ET, exact time UNKNOWN]`. ANVIL Decimal re-verification from §①: value = last × qty (×100) within 1¢ and value − basis = G/L on 19/19 rows; Σ positions **$21,945.52** + cash **$11,421.19** + pending **+$1,283.98** (= +$835.32 + $605.32 − $156.66) = **$34,650.69 to the cent**; Σ basis $19,858.21; Σ G/L +$2,087.31; Σ Today +$1,734.39. Activity running balance: every link of the 11 rows holds. **Vs `git show e8fd99acf:FORGE/STATUS.md` (10/7 intraday): 1 NEW (QQQ $750C Oct-09 ×1) · 0 GONE · 2 QTY CHANGE (QQQ $755P Oct-09 2→1 and $745P Oct-15 2→1, each SOLD TO CLOSE 10/8) · 16 MARK ONLY.**

## Chunk B — source line 94

> ⚠️ **NOT CAPTURED IN THIS 10/8 RECEIPT (nor 10/7, 10/1 or 9/30) — every cell below is the 9/29 card, unverified today.** **Home card 9/29 intraday: account $295.15 (Today +$35.00 / +13.45%), BP $8.94** `[9/29 13:4x intraday]` — was $228.15 / $8.94 `[RH card 9/27]` ⇒ +$67.00. Lines + BP = $290.15 ⇒ **$5.00 UNEXPLAINED (D-64)**. Per-line cost/value DERIVED from shown P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). **Prediction market:** Nithya Raman "Yes" 26.22 @ 58¢ ≈ $15.21 (+65.71% ⇒ cost ≈$9.18, derived — price and % identical to 9/27) — recorded, not adjudicated. **Recent activity 9/01→9/25 books the dead-by-date lines:** USO $159C Sep-11 (bought 9/10 $152, expired $0 — D-58) · QQQ $713C Sep-16 (bought 9/16 $167) + USO $165C Sep-16 (bought 9/14 $150), both expired $0 (D-57).

## Chunk C — source lines 112–121

### EXPIRING — Fri 10/09 → Fri 10/16 (sell-or-roll before expiry, `USER.md`)

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| WQ-347 | **QQQ $755P Oct-09 ×1 (was ×2)** | 🔴 Fri 10/09; 1 DTE; **ITM** | 1 sold 10/8 @ $8.36 (+$835.32; realized +$596.65 derived); 2nd sell $8.50 Verified Canceled. Remaining basis $238.66; $7.85 / $785.00 `[10/8 rcv]`; ITM ≈$7.84 at QQQ $747.16 `[WALTER 15:26:49 ET screening]`. Card: *"Do not carry into Friday"*; TERRY's assignment caveat now covers ONE contract (≈$75,500 notional, was ≈$151k) | Working order UNKNOWN; last ≠ bid. Whether Will intends to hold into Friday: UNKNOWN | **Will** (order); TERRY (card); PROME records |
| **D-60** | **Fidelity expiry handling — ITM leg UNOBSERVED** | 🔴 bears on the 755P ×1 Fri, then 10/15–16 | Liquidation leg now **×5** (adds Oct-02 740P, liquidated 10/2, its expiry day); expired-no-cash **×4** (adds Oct-05 735P, as of 10/5). IRA holds 0 QQQ / 0 TLT. Exercise of the 755P ×1 = sell 100 QQQ at $755 ($75,500) — mechanics, not a claim | ITM handling and what decides LIQUIDATE vs EXPIRED: UNKNOWN; moneyness of the two new observations not shown | **Will** — Fidelity's handling |
| — (new) | **QQQ $750C Oct-09 ×1 — NEW, no card** | 🔴 Fri 10/09; 1 DTE | BOUGHT TO OPEN 10/8 @ $1.56, −$156.66; $1.79 / $179.00 `[10/8 rcv]`; ≈$2.84 OTM (WALTER screening). No card; no approval record; C5's two-session lead impossible at 1 DTE (PROME → TERRY 10/8 asks) | Relationship to the 755P ×1 NOT declared — none inferred | **Will** (order); **TERRY** (card question); PROME records |
| WQ-366 | **USO $150C Oct-09 ×1** | 🔴 Fri 10/09 15:00 ET; 1 DTE | Still held (no sale row 10/2–10/8). $0.66 / $66.00 / −$233.66 `[10/8 rcv]`; USO $147.9101 in the same view, $2.09 below strike. **Will DECLINED early sale 10/3: hold to the hard stop** (`MGMT-USO150C-OCT09`; DOCKET L605). No harvest gate | Working order UNKNOWN; no executable bid shown | **Will** (order); TERRY (existing card) |
| WQ-347 | **QQQ $745P Oct-15 ×1 (was ×2) + $740P Oct-15 ×4** | 🟠 Thu 10/15; 7 DTE | 745P: 1 sold 10/8 @ $6.06 (+$605.32; +$321.65 derived); ×1 $573.00. 740P ×4 $1,620.00 / −$502.65. Cards: *"SELL-OR-ROLL BEFORE THURSDAY 10/15"*; their Wed 10/14 times = *"a PROPOSAL for Will"* | Working orders UNKNOWN | **Will**; TERRY cards; PROME records |
| WQ-302 / WQ-357 | **TLT $82P Oct-16 ×1 + HBAN $16P Oct-16 ×2** | 🟠 Wed 10/14 management clock; 8 DTE | TLT $405.00 / +141.54%; HBAN $140.00 / −26.84% `[10/8 rcv]`. TLT path C (Will LATER 10/3), held to 10/14; BOND research 10/5 is not a trade ruling. HBAN re-rule due 10/14. Neither percentage is a fired price trigger | Working orders / underlying moneyness UNKNOWN in this capture | **Will**; TERRY cards / BOND research |

## Chunk D1 — source line 128

| **D-75** 🆕 | **OZK 40P ×4 basis: 10/7 view $322.66 vs 10/8 $322.65** | 🟡 record, no cash effect | 10/7 view: basis $322.66, G/L and Today −$62.66, pending −$1,572.64 — consistent, and tying the 10/7 total. 10/8: Activity and basis $322.65; cash bridge ties exactly at $1,572.63. **Mirror now carries $322.65** | A 10/7 misread is UNLIKELY (it would break the 10/7 tie). Conjecture: same-day provisional cost settled 1¢ lower. 10/7 image not at its cited path ⇒ not re-viewed | **PROME** — record only |

## Chunk D2 — source lines 131–147

| **D-66** (narrowed) | **Fill TIMES / per-contract buy prices** | 🟡 carried | 10/8 Activity gives entry DATES + net amounts for all five 10/7-new identities, and fill prices for the three 10/8 orders ($8.36, $6.06, $1.56). Still not shown: any TIME; per-contract prices on the 10/2–10/7 buys; the 9/30 and 10/1 times | Sequence from row order only; no time invented | **Will** — order detail |
| **D-69** | **Prior cash +$53.54 above 9/30-implied** | 🟡 carried | Expected $18,102.04 − $4,007.98 = $14,094.06 versus both 10/1 views $14,147.60. The 10/1→10/8 path is fully bridged by rows (D-71); the gap sits in 9/30→10/1 | September money-market dividend — conjecture only, separate from D-63 | **Will** — Activity 9/30→10/1 (below the cut) |
| **D-62** | **Fidelity ledger — $0.45 break in the broker's own running balance** | 🟡 carried | 17,740.43 + 359.34 (TLT 82P, 9/28) = 18,099.77 vs 18,099.32 shown; 33 of 34 links hold | A fee/adjustment without its own row, OR a transcription digit misread | **PROME** re-reads the 9/29 image cell |
| **D-63** | **Cash bridge +$2.27 unattributed** | 🟡 carried | 9/25-close cash + pending + the 9/28 rows = $18,099.77 vs cash $18,102.04; the Sep-30 Activity showed no dividend / interest row; 9/29 rows (if any) not captured | Money-market dividend, the APD dividend, or interest — ANVIL picks none (see D-69) | **Will** — Activity 9/29 (low) |
| **D-64** | **Robinhood card — $5.00 unexplained** | 🟡 carried | $290.15 of lines + BP vs $295.15 shown `[9/29 13:4x intraday]`; not re-captured since | BP ≠ cash, a line valued off another price, or a line not on the card | **Will** — RH cash/account detail |
| **D-65** | **RH 9/14–9/15 put/call labels do not pair** | 🟡 no live position | 707 "Put" bought → 707 "Call" sold; 708 "Call" bought → 708 "Put" expiration | Hypothesis: the 9/15 "Call" rows are Puts ⇒ 707P +$104, 708P −$41 — NOT booked | **PROME** — re-read the image |
| **D-61** (narrowed) | **9/28 fills — times for QQQ 730P ×1 and TLT 77P ×5; TLT 77P $0.02 receipt-vs-ledger** | 🟡 | Ledger Σ $28.43 vs receipt $28.45; ledger used | Receipt digit or transcription — UNKNOWN | Will (order detail), low |
| **D-59** (narrowed) | **RH buying power 9/16 → 9/27: −$0.48 residual** | 🟡 | −$119.95 from the activity vs BP −$120.43 | Regulatory fees on four sells + rounding — labeled | Will, low |
| **D-45** (residual) | **+$43.81 before the 9/01 Activity view** | 🟡 | 8/28 cash + pending $14,323.25 vs derived 9/01 opening $14,367.06 | 8/31 activity or interest (an August month-end credit would match D-69's form — conjecture) | **Will** — Activity 8/28–8/31 |
| **D-55** (residual) | **VLO fill TIME** | 🟡 | Fidelity, 9/18 | — | Will, low |
| **D-28** | **RH QQQ $715P ×1 — expired 8/31, outcome UNRECORDED** | 🟡 carried | Cost ≈$193.24; before the 9/01 view | Expired OTM / sold / exercised — none verified | RH history before 9/01 |
| **D-54** | **RH KRE $25P Jan-15-2027 — entry never recorded** | 🟡 carried | Cost $53.00 derived; on the mirror since 7/16 | Entry pre-7/16 ≈$0.53 — a derivation | Will |
| **D-18** | **RH WAL $77.5P Aug-21 — sale CONFIRMED 8/18, P&L UNRECORDED** | 🟡 carried | Existence closed 8/18 | Do not book at $0 | Will (not urgent) |
| **D-20** | **RH T share — absent; event contracts** | 🟡 carried | No stocks card; no T row 9/01→9/25 | Sold before 9/01, unconfirmed | Will — full RH view |
| **D-37** | **RH ≈$360 inflow (8/14→8/28) + "13 days left" banner** | 🟡 carried | Arithmetic recorded 8/29 | Deposit/transfer; banner referent unknown | Will (one line) |
| **D-17** | **STNG — in no capture, nowhere in FORGE** | 🟡 carried | Absent since 8/2 | Recalled / closed pre-7/30 / a third account | Will — one line |
| **D-1** | **AAPL 5-sh sale pre-7/30 — date + price unrecorded** | 🟡 carried | Predates the 7/30–8/28 window | ~$565 cash class | Will / an older window |

## Chunk E — source lines 149–156

### Owner decides — ruled / gated

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-47** | **RH WAL Dec-18 $70P ×1 — `GATE-TERRY-ROLL70-EXIT`** | 🟡 stale source | ≈$265.00 derived `[9/29 13:4x intraday]`; entry 9/02 @ $2.20; 0-of-3 as last recorded, not regraded; no resting exit order (cancelled by Will 9/28); time stop 12/4 | Current existence/mark unverified today; new Fidelity WAL is a different contract/account | **Will** manual harvest; REGINALD grades / TERRY proposes |
| WQ-386 / VLO-SCALE | **VLO held share ×1 management APPROVED; 2 additional shares STOOD DOWN** | registered / scale TERMINAL | Held-share Nov through 10/14; Dec 10/15–11/19, no roll suppression; review 11/18. Prior exits owed / B1 unchanged; exact rule/ref retained in Longs. $445.995 last / $445.99 value `[10/8 rcv]` does not adjudicate crack/text gate | No buy, sale or new order inferred; optional official-CME scale override only as GATES specifies | **TERRY** grades; **Will** executes; PROME integrates |
| WQ-200 | **USO 37 sh — no management rule live** | ⚪ | Card DECLINED 9/10; $147.9101 last / $5,472.67 value `[10/8 rcv]` informational | No inherited option rule on stock | **Will** hand |
| — | **APD thesis tag / historical "D" badge** | ⚪ | Tag unassigned since 7/30; historical 10/1 last − change reference $276.42 versus 9/30 $278.23 ($1.81 gap) remains an unverified adjustment; no dividend row in 10/2–10/8 Activity | Ex-dividend adjustment conjectured; amount / pay date not shown | **PROME / Will** |

## Chunk F — source lines 158–162

### CLOSED this pass (receipts = the 10/8 Activity view, transcription §①)

- **D-72 CLOSED:** Oct-02 740P ×4 (basis $890.65) — OPTION LIQUIDATION 10/2 +$3.75 ⇒ −$886.90; Oct-05 735P ×5 (basis $1,368.32) — SOLD TO CLOSE 10/2 +$65.35 + EXPIRED as of 10/5 ⇒ −$1,302.97. Derived line totals; the D-71 bridge shows no other net cash 10/1→10/2. Per-row contract counts NOT shown — conjecture only: +$65.35 fits ×1 @ $0.66 less $0.65 fee.
- **D-73 CLOSED:** five identities' entries — 740P Oct-15 10/2 −$2,122.65 · 755P 10/6 −$477.33 · OZK 40P 10/7 −$322.65 · WAL 65P 10/7 −$682.65 · 745P 10/7 −$567.33. Running balance $15,524.70 → $12,993.82 (= 10/7 cash) → $11,421.19 (= 10/8 cash): every link holds. The 10/7 pending −$1,572.64 settled at −$1,572.63 (D-75).
- **QTY CHANGE ×2 + NEW ×1:** realized 10/8 +$918.30 (derived); NEW 750C ×1. **16 MARK ONLY.** Robinhood remains 9/29, unverified.

## Chunk G — source line 183

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(Pass notes 9/27 → 10/1 intraday → rotation 10/01 chunk F; 10/7 note → `git show e8fd99acf:FORGE/STATUS.md`. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows.)* *(10/8 pass: no structural change; `Mark 10/8 rcv` binds by prefix; 19 Fidelity rows (NEW `$750C` row, same shape as `$150C`) plus stale Robinhood rows; `**Updated:** 2026-10-08` / `marks = 2026-10-08` = received ≤15:26 ET, time UNKNOWN; pending now positive. Limits: desk_attention's Robinhood observation is stale; date-only consumers cannot show the clock; source hashes need PROME re-review.)*

## Chunk H — source line 28

| VLO | Stock | 1 | $412.00 | $445.995 | $445.99 | +$33.99 / +8.25% | Today +$21.89. Bought 9/18 @ $412.00 (fill TIME not shown — D-55). **Holding confirmed by Will 2026-10-07: “Yes, still one share”** (operator statement; current broker mark separately stamped `[10/8 rcv]`). WQ-213: 1 of 3; **the remaining 2 sh STAND DOWN** under `PROME/GATES.tsv` GATE-TERRY-VLO-SCALE, TERMINAL on the 9/25 F1 fire (TERRY 4ad672c43; optional CME source-① override remains as written). **Exit rule on the held share: `GATE-TERRY-VLO-HELD-01` REGISTERED 9/28 18:36 ET (WQ-330, Will "both"): Nov crack settlement < $90.16 ⇒ sell rec (< $95 notice); signed US distillate export-restriction text at primary ⇒ SELL at the next regular session (Will may act without the desk; TERRY recs if he has not); A: TERRY grades, Will executes; not adjudicated here (rule 7)** — **WQ-386 approved 10/7: Nov through 10/14; Dec HOZ26×42−CLZ26 from 10/15 through 11/19, no roll suppression; review 11/18; prior exits remain owed; B1 unchanged.** Exact amendment: `PROME/proposals/2026-10-07_VLO-december-management-RULED.md`. The gate reads the crack and the text, not the share's mark |

## Chunk I — source lines 174–177

| 🟡 **D-71 / D-69 / D-66** — the same Activity scrolled to 9/30–10/1 + order detail | one view | **Will** |
| 🟡 **D-70 / D-74 / D-75** — mappings re-review; cards; new bank-put ownership; OZK 1¢ recorded | owner integration | **PROME / TERRY** |
| 🟡 **D-62 / D-65** — historical image re-reads; **Robinhood** D-64 / D-28 / D-54 / D-18 / D-20 / D-37, account not captured | carried | **PROME / Will** |
| 🟡 Older Activity / detail: D-63 / D-61 / D-59 / D-45 / D-55 / D-17 / D-1 | carried | **Will** |
