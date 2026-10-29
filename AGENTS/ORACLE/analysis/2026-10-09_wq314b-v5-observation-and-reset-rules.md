# WQ-314 (b): the October $110 oil leg, its observation rule and its reset rules

**ORACLE · written 2026-10-09 10:3x ET (from `date`) · PROME spawn `prome-75`, L0 wake under WQ-221 (DOCKET L618).** This answers the PROME/CATO packet `inbox/processed/2026-09-28_from-PROME_v5-thresholds-define-reads-and-resets-CATO.md` (items 1–4). Part (a) was ruled 9/28 (Will: *"Approve WQ-314(a); hold (b) pending ORACLE's observation and reset rules."*): the leg stays **v5**, and the ICE venue is disclosed.

**Scope:** this letter defines how the levels are read and when the count resets. It does **not** move a level. Alert ≥40% and Critical ≥60% (or YES) are the 9/28 proposal unchanged, and nothing is encoded until Will rules. $0, no trade.

**RULED 2026-10-15 12:23 ET — Will APPROVED (b) as written** (Deck tap; record `PROME/proposals/2026-10-15_deck-batch-16-RULED.md`); cadence = one ORACLE pull-session per US business day until 11/1 (DOCKET L729). **Owner clarifications dated 2026-10-16 (§7)** answer the commissioned second read (`PROME/reports/2026-10-15_wq314-settlement-second-read/READ1.md`): the settlement text is quoted verbatim in §7.1, and the edits in O2, O8, R1, R2, R4 and §5.1–5.2 below were made that day. No level, operator or instrument moved (§7.3 states the C1 claim per item). **WQ-453 RULED 2026-10-20 (Will, *"WQ 453 approved"*): the Critical→Alert step-down, the touch-before-close rule and the November carry are encoded in §8 (2026-10-21).**

---

## 1. Current odds (context only; this is not a fire)

| Item | Read | Basis |
|---|---|---|
| **Oct $110 leg** | **8.5%** (bid 8 / ask 9, last 8) · Δ1d −2.5 | Polymarket id 4936102, Gamma 2026-10-09T14:26Z. ⚠️ Gamma's own Δ7d field reads −1.0, but the CLOB bars give ~−3 to −4 from 10/2. The Δ7d is not cited; use the path row |
| Depth | vol **$74.8K** lifetime · **$8.2K** 24h · liq **$41.0K** (passes the $5K bar) | same read. On 9/28 it was $224 vol and $3.3K liq (THIN) |
| October ladder | $100 **34.0** · $110 **8.5** · $120 3.9 · $130 1.5 | event `what-price-will-wti-hit-in-october-2026`, $1.4M (9/28: $19.9K) |
| Path since 9/28 | 38.0 (9/28 00Z) → 25.5 (my 9/28 13:49Z read) → 16–18 (9/30–10/2) → 12.5 (10/3–10/5) → 4.5–9.5 (10/6–10/9) | CLOB `prices-history`, 6-hour bars. **Context only, never a read** (§2 O5) |
| Spot | CLX26 **$91.27** · CLZ26 **$90.38** (delayed quotes) ⇒ $110 is +20.5% above spot | `fetch.py` 2026-10-09 ~14:26Z (CME proxy; the leg resolves on ICE) |
| Derived spread | **+73.0pp** = PortWatch-basis 81.5 − 8.5. This is the first October row that is not thin | `disruption_supply_spread.py`, REGIME `v5-oct26-icewti110` |

Under the rule below, today's read is **qualified run = 1** (the 9/28 read was thin and does not count). The level is 31.5pp below Alert, so nothing is near a fire.

## 2. Observation rule: what is observed

| # | Rule |
|---|---|
| **O1 Instrument** | Polymarket market **id 4936102**, slug `will-wti-reach-110-in-october-2026` (*"Will WTI Crude Oil (WTI) hit (HIGH) $110 in October?"*), YES outcome, conditionId `0x28c4…0aae4e`. Value = Gamma `outcomePrices[YES]`, as `polymarket.py pull --log` writes it to `workbook/ODDS_LOG.tsv` (`yes_prob`). |
| **O2 What it resolves on** | **The market's own text governs and is quoted verbatim in §7.1 (retrieved 2026-10-16T17:37Z, sha256 `bfff6022…0b62`); this cell is ORACLE's summary of it.** Text re-read at Gamma on 2026-10-09T14:26Z, unchanged from 9/28. The leg resolves YES if any **Pyth 1-minute candle High ≥ $110.00** prints for the **Active Month of ICE Futures Europe WTI (Pyth "CLL")** during an October 2026 trading session, at any point after the market was created. ICE sessions open at 8:00 PM ET the evening before (Monday's opens 6:00 PM Sunday). If Pyth is unavailable, the fallback is the ICE official daily high (`ice.com/report/10`). Prices are taken as published, without rounding. Market end: **2026-11-01T03:59:59Z** (11:59 PM EDT Sat 10/31). The last October session is the one dated Fri 10/30. |
| **O3 One read** | One read is ORACLE's **first** `pull --log` row for this slug on a **US business day** (ET date). There is **at most one read per business day**. Later pulls that day are context. Weekend and holiday pulls are context. Several polls on one day are one read: rapid polling does not show persistence (CATO item 1). |
| **O4 Liquidity test** | Each read is tested in the same row: ODDS_LOG `liquidity` (Gamma market-view `liquidity`) **≥ $5,000** ⇒ **QUALIFIED**. Below that ⇒ **THIN**. |
| **O5 Only live reads count** | Only ORACLE's own live pulls count as reads. CLOB `prices-history` backfill is **context only**, because liquidity at a past time cannot be reconstructed. |
| **O6 Band test** | Levels are compared at the venue's printed precision. Round to 0.1pp **before** testing ≥40.0 or ≥60.0 (the L546 float-tie class: `0.4*100` need not equal `40.0`). |
| **O7 Run and arming** | A **run** is a sequence of QUALIFIED reads on distinct business days with no reset event (§3) between them. **ARMED** = the last 3 reads form a run. **Alert** = an armed run of 3 reads, each ≥40.0%. **Critical** = an armed run of 3 reads, each ≥60.0%, **or the leg resolves YES** (§4). |
| **O8 Clearing** | A fired state clears only on **3 consecutive qualified reads below its level**. This uses the same evidence bar to clear as to fire. *(2026-10-16:)* "Consecutive" means a clearing run under the same rules as an arming run: a thin read (R1), a gap (R2), the switch (R3) or the month roll (R4) **restarts the clearing count at 0**, and a read at or above the level also restarts it. A reset event (§3) **never clears a fired state**. The state is held and re-graded on the next 3 qualified reads. This fails closed: the Active-Month switch lowers the odds mechanically, so letting it clear an alert would be a false all-clear. |

## 3. Reset rules (CATO items 2 and 3)

| # | Event | Effect on the count | Effect on a fired state |
|---|---|---|---|
| **R1 Thin read** | A read below $5K liq | **Reset to 0 and disarm.** A thin read is not skipped, because skipping would let a thin stretch, where one bet moves the price, sit inside a "sustained" run | Held, not cleared: a thin read is no evidence either way. The clearing count restarts at 0 (O8) |
| **R2 Gap** | More than **2 business days** between two consecutive reads | The run restarts at the later read (it counts as 1 if qualified). Persistence over an unobserved stretch has not been observed | Held. The clearing count restarts at the later read (O8) |
| **R3 Active-Month switch** | **8:00 PM EDT Wed 2026-10-14 = 2026-10-15T00:00Z.** Nov26 → Dec26. ICE LTDs were re-read at `ice.com/products/213/WTI-Crude-Futures/expiry` today (HTTP 200): **Nov26 10/19 · Dec26 11/19 · Jan27 12/18** (VERIFIED). Nov26's third-to-last session is the one dated Thu 10/15, which matches the market's own worked example | **Reset to 0 and disarm.** No run contains reads from both sides of the switch. Sides are classed by **UTC timestamp vs 2026-10-15T00:00Z, not by ET date**: a pull on Wed 10/14 after 8 PM ET is post-switch. This is the only switch inside October | Held, then re-graded on the first 3 qualified post-switch reads. **Step size:** CLX26−CLZ26 = **$0.89** at today's delayed quotes (it was $3.95 on 9/28). Re-measure at the switch. The step lowers the touch odds with no change in risk |
| **R4 Month roll (November)** | See §5 | Reset to 0 and disarm. The November leg earns its own run | *(2026-10-16, replaces "October's state ends with October's series":)* R4 is a reset event, so O8 governs: **a fired October Alert/Critical is held across the pin and carried onto VX-ORC-04 into November**, then re-graded on the November leg's first 3 qualified reads (the R3 precedent). It clears only by O8 on November reads. A recorded October YES stands as a fact |

## 4. How a resolution is recorded

- **YES (touch).** The leg is recorded as resolved when Gamma shows it `closed` with `outcomePrices` YES = 1 (or `umaResolutionStatus` resolved). **Critical fires on YES at once, with no sustain needed.** This applies even after the November pin: a $110 print inside an October session is a real event. ORACLE records the following:
  1. The Gamma read with its UTC timestamp. The ODDS_LOG row is written automatically.
  2. A KB row giving the basis (Pyth CLL Active Month) and the touch evidence from the resolution source: the Pyth 1-minute candle (time, contract, high) or the ICE `report/10` daily high as fallback.
  3. VX-ORC-04 set to 🔴 Critical with that evidence.

  A news report of a "$110 print" is never the resolution record. Between the touch and the formal close, a price near 99 is counted as an ordinary read. `disruption_supply_spread.py` hard-exits on a resolved leg by design, so the October segment closes with no rows written on a dead leg.
- **NO.** This is recorded at the close, 2026-11-01T03:59Z: Gamma `closed`, YES = 0. The record is the last qualified read before the close plus the close itself, and the segment closes. ⚠️ In the final sessions the YES price falls as the days left to touch run out. A falling read then is **expiry, not de-escalation**, as with the September leg's 1.4% exit.
- If the tool reports **`PINNED BUT NOT FOUND`**, query Gamma `closed=true` before calling the market delisted. The bank-family not-founds were all resolutions (KB-ORC-101).

## 5. When and how the leg resets for November

1. **Listing.** No November market was listed at 14:26Z 10/9 (Gamma `public-search` and the event slug both returned none). The seven prior monthly WTI events (**April–October 2026**, created 25 Mar – 25 Sep) were each created on the **25th of the preceding month, 04:01–04:03Z** (Gamma `startDate`, re-read 2026-10-16T17:38Z; no `…-march-2026` event exists under this slug). ⇒ Expected ~**2026-10-25T04:0xZ** (INFERRED from n=7).
2. **Pin.** ORACLE pins it on its first pull after listing, before the October close. ⚠️ Pinning auto-rolls the spread tool's supply leg (`SUPPLY_PREFIX` family match), so four things go in **one edit**: the pin, the `REGIME` bump, relabelling the October pin to drop its `war premium` label key (the tool's selection guard, MAINTENANCE 2026-09-28), and the MAINTENANCE entry. The October **arming** series ends at the pin: no October run can arm or fire after it, and October's later reads are context. A fired October state does not end at the pin; it is held and carried per R4. An October YES is still recorded per §4.
3. **Meaning check at pin.** Read the November resolution text first. If the strike is $110, the venue is ICE / Pyth CLL and the Active-Month rule is the same, it opens REGIME segment **`v5-nov26-icewti110`** under the month-roll rule. That stays v5 and needs no ask. If the strike, venue or rule differs, the difference is disclosed and put to Will as a meaning question, as (a) was, before any of its reads count.
4. **Count.** The November leg starts disarmed at run 0. Its first read is an **entry** read, never differenced against the October exit: a fresh month's touch odds are structurally higher because there are more days left to touch.
5. **November's own switch.** Dec26 → Jan27 at the open of the session dated Tue 11/17 = **8:00 PM EST Mon 2026-11-16 = 2026-11-17T01:00Z** (DST ends 11/1). This follows from Dec26 LTD Thu 11/19 (ICE VERIFIED today). The date applying to the November market is INFERRED from October's rule until its text is read at pin. R3 applies.
6. **No listing by the October close.** The v5 leg pauses: no rows are written, and the tool's stale-pair guard hard-exits. The absence is recorded, not filled. ORACLE does not re-strike, because a strike change is a new version and Will's call.

## 6. Caveats that travel with the letter

- ⚠️ **A higher chance of WTI touching $110 is evidence about a price event, not proof of lost physical supply** (CATO item 4). The physical-loss test remains the Kalshi Iran-crude context column (<2.0 mbpd), which is OI 0 and thin today. **HAWK and BRENT own the reality.**
- ⚠️ **Cadence dependency.** ORACLE does not wake itself. The bands can arm only if ORACLE is pulled on most business days: 3 reads with gaps of no more than 2 business days. With today's wake pattern (dark 9/28 → 10/9) the bands would never arm. If Will approves, they work only with a pull cadence, which is PROME's to schedule.
- ⚠️ Polymarket's settlement text was read by ORACLE on 9/28 and again today. A second reader has **not** checked it (CATO's 9/28 note still stands). The ICE dates are VERIFIED today at ice.com.
- ⚠️ Pyth's own "CLL" Active-Month roll is assumed to follow the market text's rule. That is not verified: the resolution text defines the Active Month itself, and the text governs.

---

## 7. Owner clarifications, 2026-10-16 (answers the commissioned second read)

**ORACLE · 2026-10-16 13:3x–13:5x ET (from `date`) · PROME spawn `prome-ac`, DOCKET L729 first daily pull.** These are written **prospectively**: no fired state exists today (§8), so none of them can change a past grade.

### 7.1 The settlement text, verbatim

Retrieved from Gamma `GET /markets/4936102` at **2026-10-16T17:37Z** (`updatedAt` 2026-10-16T17:34:52Z). `description` field sha256 **`bfff6022b8048b8840406ce693acc027d9c7c383e9c2b7f13fa27a61f91c0b62`**. `resolutionSource` = `https://app.pyth.com/explore?search=CLL`. `startDate` 2026-09-25T04:02:10Z · `endDate` 2026-11-01T03:59:59.999Z. Quoted exactly, between the rules:

```text
This market will resolve to "Yes" if, at any point after market creation and during a trading session of October 2026, any Pyth 1-minute candle for the Active Month of ICE Futures Europe WTI Crude Futures (denoted by Pyth as "CLL") has a final "High" or "Low" price equal to or beyond (above for ↑ High Prices, below for ↓ Low Prices) the listed price. Otherwise, this market will resolve to "No".

Prices will be used exactly as published by Pyth, without rounding.

Only prices achieved during an applicable trading session of the specified timeframe's business days will be considered (See: "Trading Hours" at https://www.ice.com/products/213/WTI-Crude-Futures). The trading session for a given business day typically begins at 8:00 PM ET on the prior calendar date, except for the session dated Monday, which begins at 6:00 PM ET on the preceding Sunday, and where modified by holiday or other special hours (See: https://www.ice.com/holiday-hours).

The Active Month is the nearest listed contract, except during that contract's final three trading sessions. At the open of the third-to-last trading session, the next listed contract becomes the Active Month.

Each contract's last trading day will be determined by ICE Futures Europe per the WTI Crude Futures contract specification (generally the 4th US business day prior to the 25th calendar day of the month preceding the contract month, or five US business days prior if the 25th calendar day is not a US business day). The last trading day for each contract is posted at https://www.ice.com/products/213/WTI-Crude-Futures/expiry.

For example, if the last trading session for the nearest listed contract is the session for Monday the 20th, the next listed contract would become the Active Month at the start of the trading session for Thursday the 16th (8:00 PM ET on Wednesday), assuming a standard trading calendar.

If the relevant Pyth data is unavailable due to a system outage, data failure, or other disruption that prevents verification of the required 1-minute candle data, the official daily high/low price published for the Active Month WTI Crude Oil Futures contract by ICE Futures Europe may be used to determine whether the listed price was reached during the applicable trading session (See: https://www.ice.com/report/10 with "T-West Texas Intermediate Light Sweet Crude Future" selected).

In the event of a contract specification change, feed change, or similar structural modification affecting the underlying market during the listed time frame, this market will resolve based on adjusted prices as displayed on Pyth.

If the Active Month contract does not trade at all during the listed time frame, this market will resolve to "No".

The resolution source for this market is Pyth — specifically, the ICE Futures Europe WTI Crude Futures Active Month "High" and "Low" prices available at https://app.pyth.com/explore?search=CLL, with the chart settings configured for 1-minute candles. Historical 1-minute candles may be accessed by appending a Unix timestamp (seconds) to the Pyth chart URL using the "t=" parameter.
```

### 7.2 What the verbatim text settles (second-read ⚠️ items)

| READ1 item | Settled by the text |
|---|---|
| ⚠️4 tie at $110.00 | *"equal to or beyond (above for ↑ High Prices…)"* ⇒ **≥ $110**, inclusive; *"exactly as published by Pyth, without rounding"* |
| ⚠️5 Active Month meaning | *"the nearest listed contract, except during that contract's final three trading sessions. At the open of the third-to-last trading session, the next listed contract becomes the Active Month."* |
| ⚠️6 the worked example | quoted in full above (*"…last trading session … Monday the 20th … Active Month at the start of the trading session for Thursday the 16th (8:00 PM ET on Wednesday)…"*). R3's 2026-10-15T00:00Z switch follows from it with Nov26 LTD Mon 10/19 |
| ⚠️7 first session | sessions begin 8:00 PM ET the prior calendar date ⇒ the first October session (Thu 10/1) opened 8:00 PM EDT Wed 9/30 = 2026-10-01T00:00Z |
| ⚠️9 fallback scope | only when Pyth data is unavailable *"due to a system outage, data failure, or other disruption that prevents verification of the required 1-minute candle data"*; and the fallback *"may be used"* (permissive). Scope per session is not stated further |
| ⚠️19 Pyth roll vs text | the text defines the Active Month and names Pyth's CLL as the source; a structural change resolves *"based on adjusted prices as displayed on Pyth"*. ORACLE does not adjudicate a Pyth-vs-text mismatch; the venue resolves it (UNKNOWN until it happens) |

### 7.3 The three ❌ and the clearing-count ⚠️ — what changed, and the C1 claim

| Item | Edit (in place, above) | Level / operator / instrument / consequence moved? |
|---|---|---|
| ❌37 fired state at the November pin | R4 cell and §5.2 rewritten: the pin ends October's **arming** series only; a fired state is **held and carried** into November and re-graded on November's first 3 qualified reads (R3 precedent); clears only by O8 | **No.** R4 sits in the §3 reset table and O8 already says *"A reset event (§3) never clears a fired state"*; the old R4 wording contradicted that, and the edit removes the contradiction in O8's direction (fail-closed). ⚠️ PROME to verify the claim; the alternative reading (state ends at the pin) would be the consequence change and goes to Will |
| ⚠️36① thin/gap during clearing | O8, R1, R2 cells: a thin read, gap, switch or roll **restarts the clearing count at 0** | **No.** O8's own sentence *"the same evidence bar to clear as to fire"* compels it; only ever holds a state longer |
| ❌23 n=7 vs Mar–Oct | §5.1: the seven events are **April–October 2026** (created 25 Mar – 25 Sep), re-read at Gamma today | No (basis wording; the pin waits for a listing anyway) |
| ❌43 dead pointer | L3 → `inbox/processed/…CATO.md` | No |

### 7.4 States still undefined — declared, not fixed today

| READ1 item | Status | Can it bite before 11/1? |
|---|---|---|
| ⚠️36② mixed re-grade (2 below, 1 above) | Covered by 7.3: a read at/above the level restarts the clearing count | — |
| ⚠️36③ Critical→Alert downgrade (3 reads <60 but ≥40) | **RULED 2026-10-20 (WQ-453 DEF = A), encoded 2026-10-21 — see §8.** *(10/16 text: OPEN. Proposed: that clears Critical and leaves Alert held. Moves a consequence ⇒ for Will via PROME, not encoded.)* | Only if Critical fires first (today 20.5%) |
| ⚠️21 touch seen before the Gamma close | **RULED 2026-10-20 (WQ-453 DEF = A), encoded 2026-10-21 — see §8.** *(10/16 text follows.)* OPEN. Today: Critical on YES records at Gamma close (§4). A Pyth ≥$110 candle seen earlier is reported to PROME/BRENT as an UNRESOLVED touch, no state. Changing when Critical fires = a consequence ⇒ Will | Yes, if WTI reaches $110 (CME CLZ26 proxy $98.64 at 2026-10-16T17:37Z via `fetch.py` = +11.5% below; the leg resolves on ICE) |
| ⚠️22 which read is the NO record | Clarified: the NO record = the last **counting** read (on or before the pin) plus the close | No |
| ⚠️31 holiday calendar | **OPEN** (US business day = ? calendar). Moot through 10/30: no NYSE or federal holiday 10/16–10/30 | No |
| ⚠️34 half-tie rounding | Moot at the venue's precision: Polymarket prints this leg at 0.001 (0.1pp), so no x.x5 half-tie can reach O6's 0.1pp rounding (INFERRED from the printed prices) | No |
| ⚠️39 gap counting | **RULED 2026-10-21 (WQ-476 GAP = A), encoded 2026-10-28 — see §9.1: strictly between.** *(Superseded text:)* OPEN (strictly-between vs difference). Moot while reads land on consecutive business days. **2026-10-21: it now bites on the label only — see §8.3** | Only if a pull is missed |
| ⚠️25 switch lowers odds "mechanically" | True only while Dec26 < Nov26. The fail-closed rule stands either way | No |

---

## 8. Will's rulings of 2026-10-20 (WQ-453), encoded 2026-10-21

**ORACLE · 2026-10-21 22:2x ET (from `date`) · PROME spawn by prome-56, catch-up wave 2.** Will, verbatim 2026-10-20 12:01 ET: *"WQ 453 approved"*, recorded by PROME as its recommendation on all three units (`PROME/WILL_QUEUE.md` row 453; packet `inbox/processed/2026-10-20_from-PROME_wq453-ruled.md`). Encoded here and on `workbook/VX.tsv` (VX-ORC-04 Alert cell; new VX-ORC-11). Nothing below moves a level, operator or instrument; the two DEF items and ROLLCARRY are the consequence definitions Will ruled.

### 8.1 453.DEF = A — both definitions as drafted in §7.4

| Item | Rule now in force |
|---|---|
| **Critical steps down to Alert** (⚠️36③) | When a band Critical (≥60.0 on an armed run of 3) is held, **3 consecutive qualified reads below 60.0 clear Critical and leave Alert HELD**; it does not drop to none. Alert then clears only by O8: 3 consecutive qualified reads below 40.0. The O8 restart rules (thin read, gap, switch, roll, or a read at/above the level) apply to each clearing count. A Critical fired by a **YES resolution** is a recorded fact and does not step down. |
| **Touch seen before the formal close** (⚠️21) | A Pyth CLL 1-minute candle High ≥ $110.00 seen **before** Gamma shows the leg resolved **does not fire Critical**. ORACLE reports it to PROME and BRENT as an **UNRESOLVED touch** (time, contract, high, source), with no state change. **Critical fires when Gamma shows the leg resolved YES** (§4: `closed` with YES = 1 or `umaResolutionStatus` resolved). Reads taken between the touch and the close remain ordinary reads under O3–O7. |

⚠️ **Reading of "as drafted", for PROME to check:** the touch item had no separate draft beyond §7.4's description of the current rule (*"Critical on YES records at Gamma close (§4). A Pyth ≥$110 candle seen earlier is reported to PROME/BRENT as an UNRESOLVED touch, no state"*); ORACLE encodes that text as the ruled definition. If Will meant the opposite direction (fire on the candle), that is a new ruling.

**Declared residue (not defined by the draft; cannot bite unless Critical fires first; today 13.5%):** whether qualified reads below 40.0 that fall inside the run clearing Critical also count toward Alert's own clearing count. Until ruled, the fail-closed reading applies: Alert's clearing count starts at the first read after Critical clears. Listed for Will via PROME.

### 8.2 453.ROLLCARRY = A

A fired October Alert or Critical is **HELD and carried onto VX-ORC-04 into November** at the pin, and re-graded on the November leg's first 3 qualified reads (R4, §5.2 as rewritten 2026-10-16). It is now Will-ruled; the 10/16 C1 claim is superseded. Today no state is fired, so nothing will carry unless one fires before the pin (~10/25).

### 8.3 The 10/19–10/20 gap and ⚠️39 (gap counting)

Business-day reads: 10/16 (Fri) 20.5 → **no read 10/19 (Mon) or 10/20 (Tue)** → 10/21 (Wed) 13.5 at 2026-10-22T02:22Z = 22:22 EDT, the first pull of ET 10/21 (O3 has no time-of-day limit; precedent: the 10/14 read at 23:56 EDT). R2 says *"more than 2 business days between two consecutive reads"*:

| Reading of R2 | Count 10/16 → 10/21 | Effect |
|---|---|---|
| Business days strictly between (10/19, 10/20) | 2, not more than 2 | No restart: run 4, ARMED |
| Difference in business days | 3, more than 2 | Restart: run 1, disarmed |

Under both readings the state is **none**: 13.5 < 40.0. No future fire differs either, because an Alert needs its own last 3 reads each ≥ 40.0 and today's read cannot be one of them. Only the ARMED label differs, so the ledger records both. ⚠️39 stays **OPEN for Will**. ORACLE's recommendation is the strictly-between reading, because it is the letter's own word ("between"). The choice would change a consequence only if a state were fired and a clearing count straddled a gap.


## 9. WQ-476 rulings encoded, the 10/22–10/27 gap, and the November pin (2026-10-28)

**ORACLE · 2026-10-28 20:4x ET (from `date`) · Will-launched session, laptop `WilliePOwen`.** Will, verbatim 2026-10-21 22:46 ET: *"Approve 472 A, 473 A, 474 A, 475 A, 476 A"* (PROME packet `inbox/processed/2026-10-21_from-PROME_WQ476-RULED-A.md`). PROME asked for this encode at the 10/22 read; no ORACLE session ran 10/22–10/27, so it lands now.

### 9.1 476.GAP = A — ⚠️39 CLOSED

R2 counts **business days strictly between** two consecutive reads. Applied to §8.3: 10/16 → 10/21 = 2 between ⇒ no restart; the 10/21 read was **run 4, ARMED** (state none, 13.5 < 40.0). The "difference" reading is retired. §7.4 item 39 is closed by this ruling.

### 9.2 476.DEFRES = A — fail-closed

Alert's O8 clearing count (3 qualified reads < 40.0) starts only **after** Critical clears. Reads inside the Critical-clearing run do not count toward Alert's clearing. The touch reading in §8.1 stands (UNRESOLVED touch before Gamma's close; Critical fires only on Gamma YES).

### 9.3 The 10/22–10/27 gap

No ORACLE pull between 2026-10-22T02:22Z and 2026-10-29T00:44Z. Business days strictly between 10/21 and 10/28: **10/22, 10/23, 10/26, 10/27 = 4 > 2 ⇒ R2 restart.** The 10/28 October read (3.6%, liq $46.6K, QUALIFIED) is run 1, disarmed, state none. No fire was possible in the gap that ORACLE could have recorded: reads are live pulls only (O5).

### 9.4 The November pin (§5)

- **Listed** 2026-10-25T04:01:51Z (market id 6172751), matching the n=7 inference in §5.1.
- **Meaning check** at Gamma 2026-10-29T00:4xZ: the resolution text is identical to October's except the month (strike $110, ICE Futures Europe WTI Pyth CLL Active Month, 1-minute candle High, same Active-Month rule) ⇒ REGIME **`v5-nov26-icewti110`**, stays v5, no ask.
- **Pinned** in one edit 2026-10-29T00:4xZ: Nov pin + October relabel (drops `war premium`) + `REGIME` bump + MAINTENANCE entry. The October arming series ends here; the 00:44Z October read was its last arming read. No October state was fired, so nothing carries (§8.2).
- **November entry read** 2026-10-29T00:46Z: **52.5%**, liq $28.6K ⇒ QUALIFIED under O4. ⚠️ Lifetime volume is **$3.4K**: the fetcher's volume floor flags it thin. O4 is a liquidity test, so the read counts, but the price is quoted more than traded. CLOB context since listing: 50.0 → 60.0 → 38.0 → 52.5.
- **Consequence ahead:** reads on 10/29 and 10/30 each ≥ 40.0 and qualified ⇒ **Alert fires at the 10/30 read.** DOCKET L729's cadence ends 10/30 (until 11/1); November reads after that need a cadence decision from PROME.

### 9.5 WQ-527 C — scheduled pulls (2026-10-28 21:1x ET)

Will, verbatim 2026-10-28 20:59 ET: *"527 C approve"*. From Thu 10/29, `tools/daily_pull.sh` (cron, laptop) runs ORACLE's own `pull --log` once per ET weekday. Its rows are **ORACLE's own live pulls** under O5, so the first one on an ET date is that day's read under O3. The routine never grades: the next live session grades from ODDS_LOG and writes the ledger rows. Registry: `SCHEDULED_RUNS.md`.
