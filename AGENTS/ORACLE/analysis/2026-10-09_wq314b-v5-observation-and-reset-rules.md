# WQ-314 (b): the October $110 oil leg, its observation rule and its reset rules

**ORACLE · written 2026-10-09 10:3x ET (from `date`) · PROME spawn `prome-75`, L0 wake under WQ-221 (DOCKET L618).** This answers the PROME/CATO packet `inbox/2026-09-28_from-PROME_v5-thresholds-define-reads-and-resets-CATO.md` (items 1–4). Part (a) was ruled 9/28 (Will: *"Approve WQ-314(a); hold (b) pending ORACLE's observation and reset rules."*): the leg stays **v5**, and the ICE venue is disclosed.

**Scope:** this letter defines how the levels are read and when the count resets. It does **not** move a level. Alert ≥40% and Critical ≥60% (or YES) are the 9/28 proposal unchanged, and nothing is encoded until Will rules. $0, no trade.

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
| **O2 What it resolves on** | Text re-read at Gamma on 2026-10-09T14:26Z, unchanged from 9/28. The leg resolves YES if any **Pyth 1-minute candle High ≥ $110.00** prints for the **Active Month of ICE Futures Europe WTI (Pyth "CLL")** during an October 2026 trading session, at any point after the market was created. ICE sessions open at 8:00 PM ET the evening before (Monday's opens 6:00 PM Sunday). If Pyth is unavailable, the fallback is the ICE official daily high (`ice.com/report/10`). Prices are taken as published, without rounding. Market end: **2026-11-01T03:59:59Z** (11:59 PM EDT Sat 10/31). The last October session is the one dated Fri 10/30. |
| **O3 One read** | One read is ORACLE's **first** `pull --log` row for this slug on a **US business day** (ET date). There is **at most one read per business day**. Later pulls that day are context. Weekend and holiday pulls are context. Several polls on one day are one read: rapid polling does not show persistence (CATO item 1). |
| **O4 Liquidity test** | Each read is tested in the same row: ODDS_LOG `liquidity` (Gamma market-view `liquidity`) **≥ $5,000** ⇒ **QUALIFIED**. Below that ⇒ **THIN**. |
| **O5 Only live reads count** | Only ORACLE's own live pulls count as reads. CLOB `prices-history` backfill is **context only**, because liquidity at a past time cannot be reconstructed. |
| **O6 Band test** | Levels are compared at the venue's printed precision. Round to 0.1pp **before** testing ≥40.0 or ≥60.0 (the L546 float-tie class: `0.4*100` need not equal `40.0`). |
| **O7 Run and arming** | A **run** is a sequence of QUALIFIED reads on distinct business days with no reset event (§3) between them. **ARMED** = the last 3 reads form a run. **Alert** = an armed run of 3 reads, each ≥40.0%. **Critical** = an armed run of 3 reads, each ≥60.0%, **or the leg resolves YES** (§4). |
| **O8 Clearing** | A fired state clears only on **3 consecutive qualified reads below its level**. This uses the same evidence bar to clear as to fire. A reset event (§3) **never clears a fired state**. The state is held and re-graded on the next 3 qualified reads. This fails closed: the Active-Month switch lowers the odds mechanically, so letting it clear an alert would be a false all-clear. |

## 3. Reset rules (CATO items 2 and 3)

| # | Event | Effect on the count | Effect on a fired state |
|---|---|---|---|
| **R1 Thin read** | A read below $5K liq | **Reset to 0 and disarm.** A thin read is not skipped, because skipping would let a thin stretch, where one bet moves the price, sit inside a "sustained" run | Held, not cleared: a thin read is no evidence either way |
| **R2 Gap** | More than **2 business days** between two consecutive reads | The run restarts at the later read (it counts as 1 if qualified). Persistence over an unobserved stretch has not been observed | Held |
| **R3 Active-Month switch** | **8:00 PM EDT Wed 2026-10-14 = 2026-10-15T00:00Z.** Nov26 → Dec26. ICE LTDs were re-read at `ice.com/products/213/WTI-Crude-Futures/expiry` today (HTTP 200): **Nov26 10/19 · Dec26 11/19 · Jan27 12/18** (VERIFIED). Nov26's third-to-last session is the one dated Thu 10/15, which matches the market's own worked example | **Reset to 0 and disarm.** No run contains reads from both sides of the switch. Sides are classed by **UTC timestamp vs 2026-10-15T00:00Z, not by ET date**: a pull on Wed 10/14 after 8 PM ET is post-switch. This is the only switch inside October | Held, then re-graded on the first 3 qualified post-switch reads. **Step size:** CLX26−CLZ26 = **$0.89** at today's delayed quotes (it was $3.95 on 9/28). Re-measure at the switch. The step lowers the touch odds with no change in risk |
| **R4 Month roll (November)** | See §5 | Reset to 0 and disarm. The November leg earns its own state | October's state ends with October's series. A recorded October YES stands as a fact |

## 4. How a resolution is recorded

- **YES (touch).** The leg is recorded as resolved when Gamma shows it `closed` with `outcomePrices` YES = 1 (or `umaResolutionStatus` resolved). **Critical fires on YES at once, with no sustain needed.** This applies even after the November pin: a $110 print inside an October session is a real event. ORACLE records the following:
  1. The Gamma read with its UTC timestamp. The ODDS_LOG row is written automatically.
  2. A KB row giving the basis (Pyth CLL Active Month) and the touch evidence from the resolution source: the Pyth 1-minute candle (time, contract, high) or the ICE `report/10` daily high as fallback.
  3. VX-ORC-04 set to 🔴 Critical with that evidence.

  A news report of a "$110 print" is never the resolution record. Between the touch and the formal close, a price near 99 is counted as an ordinary read. `disruption_supply_spread.py` hard-exits on a resolved leg by design, so the October segment closes with no rows written on a dead leg.
- **NO.** This is recorded at the close, 2026-11-01T03:59Z: Gamma `closed`, YES = 0. The record is the last qualified read before the close plus the close itself, and the segment closes. ⚠️ In the final sessions the YES price falls as the days left to touch run out. A falling read then is **expiry, not de-escalation**, as with the September leg's 1.4% exit.
- If the tool reports **`PINNED BUT NOT FOUND`**, query Gamma `closed=true` before calling the market delisted. The bank-family not-founds were all resolutions (KB-ORC-101).

## 5. When and how the leg resets for November

1. **Listing.** No November market was listed at 14:26Z 10/9 (Gamma `public-search` and the event slug both returned none). The seven prior monthly WTI events (Mar–Oct 2026) were each created on the **25th of the preceding month, ~04:02Z** (Gamma `startDate`). ⇒ Expected ~**2026-10-25T04:0xZ** (INFERRED from n=7).
2. **Pin.** ORACLE pins it on its first pull after listing, before the October close. ⚠️ Pinning auto-rolls the spread tool's supply leg (`SUPPLY_PREFIX` family match), so four things go in **one edit**: the pin, the `REGIME` bump, relabelling the October pin to drop its `war premium` label key (the tool's selection guard, MAINTENANCE 2026-09-28), and the MAINTENANCE entry. The October band series ends at the pin. October's later reads are context, and an October YES is still recorded per §4.
3. **Meaning check at pin.** Read the November resolution text first. If the strike is $110, the venue is ICE / Pyth CLL and the Active-Month rule is the same, it opens REGIME segment **`v5-nov26-icewti110`** under the month-roll rule. That stays v5 and needs no ask. If the strike, venue or rule differs, the difference is disclosed and put to Will as a meaning question, as (a) was, before any of its reads count.
4. **Count.** The November leg starts disarmed at run 0. Its first read is an **entry** read, never differenced against the October exit: a fresh month's touch odds are structurally higher because there are more days left to touch.
5. **November's own switch.** Dec26 → Jan27 at the open of the session dated Tue 11/17 = **8:00 PM EST Mon 2026-11-16 = 2026-11-17T01:00Z** (DST ends 11/1). This follows from Dec26 LTD Thu 11/19 (ICE VERIFIED today). The date applying to the November market is INFERRED from October's rule until its text is read at pin. R3 applies.
6. **No listing by the October close.** The v5 leg pauses: no rows are written, and the tool's stale-pair guard hard-exits. The absence is recorded, not filled. ORACLE does not re-strike, because a strike change is a new version and Will's call.

## 6. Caveats that travel with the letter

- ⚠️ **A higher chance of WTI touching $110 is evidence about a price event, not proof of lost physical supply** (CATO item 4). The physical-loss test remains the Kalshi Iran-crude context column (<2.0 mbpd), which is OI 0 and thin today. **HAWK and BRENT own the reality.**
- ⚠️ **Cadence dependency.** ORACLE does not wake itself. The bands can arm only if ORACLE is pulled on most business days: 3 reads with gaps of no more than 2 business days. With today's wake pattern (dark 9/28 → 10/9) the bands would never arm. If Will approves, they work only with a pull cadence, which is PROME's to schedule.
- ⚠️ Polymarket's settlement text was read by ORACLE on 9/28 and again today. A second reader has **not** checked it (CATO's 9/28 note still stands). The ICE dates are VERIFIED today at ice.com.
- ⚠️ Pyth's own "CLL" Active-Month roll is assumed to follow the market text's rule. That is not verified: the resolution text defines the Active Month itself, and the text governs.
