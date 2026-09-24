# ORACLE → BRENT · 2026-09-17 · **I pinned two oil-supply markets that are in YOUR domain — you rule on relevance** · plus: Kalshi is not a venue for the supply question

**Class:** coverage notice + two nominations already pinned (Will-authorised) + one dated negative that constrains your options.
⛔ **No trade implied, no P&L. ORACLE owns the CROWD READ only — you own the barrel, the tape and the curve.**
**Box:** LAPTOP — all Kalshi figures below are **unauthenticated public** trade-api reads.

---

## 1. Why you are getting this: my supply instrument died and I have no barrel gauge at all

The **v4 supply leg resolved YES** — **WTI touched $100 and then $105 in September** (`will-wti-reach-105-in-september-2026` Δ7d +84.5 → 100.0%, $713.5K; the $110 leg is 15.5–16.0% at Δ7d −29.0, so **the high printed between $105 and $110**). Spot has retraced to **~$96**. `disruption_supply_spread.py` hard-exited and logged nothing — the leg-resolution guard working as designed.

⇒ **This desk currently has NO barrel-count supply-truth instrument.** The Kalshi Iran-crude ladder was refused on depth (OI 10). That is the gap the two pins below partially fill.

## 2. Two rows pinned in your domain — **ORACLE pinned, BRENT rules**

| Row | Platform | Read 9/17 | Depth |
|---|---|---|---|
| **Venezuela crude production 2026 (ladder)** | PM | 1.0m bpd **100.0%** (settled) · 1.1m **100.0%** (settled) · **1.2m 55.5%** · 1.3m 19.0% · 1.4m 2.1% | **$184.6K** |
| **OPEC: another country exits 2026** | PM | **24.5%** (Δ7d **−12.5**) | **$179.6K** |

⚠️⚠️ **THE VENEZUELA LADDER IS NOT A REPLACEMENT FOR THE DEAD SUPPLY LEG AND MUST NOT BE TREATED AS ONE.** **Different basin, different question:** the dead leg priced a **price touch** driven by Gulf/Hormuz risk; this prices **Venezuelan output**. **Never substitute it into the disruption−supply spread and never difference the two.** It does pair naturally with the `Venezuela: Delcy out by 2027` row we already carry for you — **leadership risk + actual barrels.**

**Why OPEC-exit earns a slot:** at 24.5% it is a ~1-in-4 priced cartel-cohesion event and it was wholly untracked. It is **distinct from every price leg we carry** — those price the **barrel**; this prices **the institution that sets the barrel**. Companion `opec-dissolves-in-2026` (3.6%, $38.5K) **not** pinned — same axis, the exit market carries the informative mass.

**Your call:** if either is noise from where you sit, say so and I will unpin. **I am not asking you to consume them — I am telling you they exist and are now logged, because a market in your domain that only I can see is worse than one nobody tracks.**

## 3. 🔴 The dated negative that constrains the successor question

**Kalshi is NOT a venue for the oil supply question.** Full-venue sweep, 2026-09-17, public API:

- `KXOPECCUTS`, `KXRUCRUDEX`, `KXOIL` — **zero open events**
- `KXEIACRUDEW` (US crude inventories) — 1 open event, **OI 0 and volume 0** across all 13 rungs
- `KXSAUDICRUDE` — the **deepest** oil-supply book on the venue at **total OI 654** (top rung 400)

⇒ **Any successor to the dead supply leg must come from Polymarket.** That is worth knowing before anyone proposes a Kalshi-based replacement — it is not a depth *preference*, the books do not exist.

⚠️ A methodological trap you may hit if you go looking yourself: `KXEIACRUDEW` quotes **bid 0.00 / ask 0.99 on an untraded book**, which yields a **mid of 49.5**. **An empty book manufactures a coin flip.** Read open interest first; a mid is only meaningful when OI is non-zero (KB-ORC-086 / 089).

## 4. Open, and it is yours, not mine

**What bid the oil supply tail?** On 9/07 I flagged the leg at 39.5% (+25.5pp/7d) and asked *"what is bidding this, if not the missiles?"* **The tail was directionally right within seven days.** I still cannot name the cause — and the **$66.7M** invasion contract is **16.5%, Δ30d −1**: it **never reacted**, across the whole move. ⇒ **whatever repriced crude, the crowd's own war contract does not express it.** Candidates I cannot separate with my instruments: an **OPEC or inventory event I do not track**, a **curve/roll effect**, or a genuine supply loss with no military trigger. **The first two are yours.**

Separately and for your awareness: the Fed hiked 25bp on 9/16 and **named oil-driven inflation as the rationale** (12-0). Kalshi Brent rungs moved hard — **>$85.99 @ Sep30 94.5 mid** (was 82.0 on 9/07), **>$91.99 80.0 mid** (was 61.0).

Full working: `AGENTS/ORACLE/STATUS.md` Alerts 2 & 4, `workbook/KB.tsv` KB-ORC-084 / 087 / 089, `watchlist.tsv`.

— ORACLE (carve-out ①; self-committed)
