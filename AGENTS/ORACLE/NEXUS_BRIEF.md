# ORACLE — NEXUS Brief

**As of:** 2026-09-17 (Thu, 01:49–01:52Z 9/18 UTC / **21:49–21:52 ET 9/17**) | **STATUS commit:** *(this session — see `git log AGENTS/ORACLE/STATUS.md`)* | **Session:** catch-up boot at Will's direction. **THE DESK WAS DARK 2026-09-08 → 2026-09-16 (TEN DAYS) AND MISSED BOTH THE 9/11 CPI AND THE 9/16 FOMC.**
**Status:** 🔴 — the Fed hiked, WTI touched $105, September CPI is priced far hotter than August, and **my primary derived instrument is dead by resolution.**
**Domain:** Prediction-market monitoring (Polymarket + Kalshi) — crowd-implied probabilities & crowd-vs-thesis divergence. Inbound routed by WALTER.
**Box:** **LAPTOP** (`WilliePOwen`) — the **authenticated** Kalshi lane is **DOWN here by design** (`~/.config/kalshi` absent). **Kalshi figures below are UNAUTHENTICATED PUBLIC trade-api reads**, which `PROME/MACHINE_LOCAL.md` row 6 explicitly sanctions. **Record lane state per-box, never as a fleet fact.**
**Constraint honored:** no trade implied, no P&L, no position language. No new gate registered.
⚠️ **Δ1d IS UNRELIABLE THROUGHOUT** — the fetcher differences against my last logged print, which for most rows is **ten days old**. **Read Δ7d / Δ30d**, and prefer the `history`-derived Δ30d (CLOB daily series, not my gappy log).

> **★ THE ONE THING TO TAKE FROM THIS BRIEF — the oil shock, the CPI print and the Fed hike are ONE transmission chain, and my 9/07 alert was standing at the front of it.**
> **The Fed hiked 25bp to 3.75–4.00% on 2026-09-16**, its first increase since 2023, **vote 12-0 unanimous**, and it named **oil-driven inflation** as the reason. Primary: Kalshi `KXFED-26SEP-T3.75` settled **`result: yes`**, **`expiration_value: "4.00%"`**, OI **637,353 ct**, **last trade 86.0¢**.
> **WTI touched $100 and then $105 in September** — `will-wti-reach-105-in-september-2026` went **Δ7d +84.5 → 100.0%** ($713.5K vol); the $110 leg sits 15.5–16.0% at **Δ7d −29.0**, so **the high printed between $105 and $110**. Spot has retraced to **~$96**.
> **August CPI landed in (3.3%, 3.4%]** (`KXCPIYOY-26AUG`: `>3.3%` **YES**, `>3.4%` **NO**, `>3.5%` **NO**) and **September's `>3.5%` rung is now 83.0 mid where August's was 10.0% at the same rung.**
> ⇒ **On 9/07 I flagged the supply leg at 39.5% (+25.5pp/7d) and asked *"what is bidding the oil supply tail, if not the missiles?"* The tail was RIGHT about direction within seven days.** ⛔ **I still cannot name the cause**, and the 9/07 finding holds: the **$66.7M** invasion contract is **16.5%, Δ30d −1** — it never reacted. (KB-ORC-083, KB-ORC-084, KB-ORC-085)
>
> **★ MY PRIMARY DERIVED INSTRUMENT IS DEAD, AND IT DIED BY SUCCEEDING.** The disruption−supply spread existed to detect a flip from a price story to a **supply** story. **The supply event happened:** the WTI-$100 leg **resolved YES**, and `disruption_supply_spread.py` **hard-exited and logged nothing** ("STALE-PAIRED … 11d apart") — the registered leg-resolution killer working exactly as built. **Last valid row: +36.0pp @ 2026-09-07T16:10Z.** ⛔ **CONSUMERS: do NOT compute 82.5 − 100 = −17.5pp as a spread** — differencing against a settled leg is the v1 failure this guard was built after, and I name the tempting-but-wrong number so nobody derives it independently. **The series is PAUSED by design, not stale by neglect.** (VX-ORC-04)
>
> **★ I DID NOT RE-PIN A SUCCESSOR, AND THAT IS THE DELIBERATE CALL.** **WQ-190 ratified the $100 leg as v4 when $100 was a 22–40% TAIL. It has now been touched, and spot is ~$96** — so a $100 threshold is **at-the-money**, and any successor at that strike **measures something the ratified instrument did not. That is a change of MEANING, not a maintenance roll**, and executing it silently is precisely the option-A error I caught myself committing on 9/07. ⚠️ **NO OCTOBER WTI $100 MARKET EXISTS** — searched four ways; **absence RECORDED, not inferred away**, which was my own 9/07 pre-commitment. **Candidate for a ruling, NOT adopted: the $110 rung** (vol $633.6K, liq $86.6K — genuinely deep, unlike the Kalshi option-B rung at OI 10). **Will/PROME rule.** (KB-ORC-084)
>
> **★ PROME's ASK ① IS ANSWERED: the venue gap closed by CONVERGENCE, not by a standing basis.** On 9/07 I had PM hike-25 50.5 / Kalshi differenced 50.0; PROME's 9/14 packet relayed futures **~90%** and Reuters **86-of-101 (85%)** post-CPI; **Kalshi's own final settle was 86.0¢.** ⇒ **the venues moved TO the futures.** ⭐ **And for OCTOBER the two venues agree to 0.0pp** — PM hike-25 **50.5%** vs Kalshi `KXFED-26OCT` differenced **≈50.5%** (Above-4.00 52.0 mid − Above-4.25 1.5). **Second episodic-convergence datum; still NOT a standing-basis finding.** ⛔ **I claim NO lead-lag** — I hold no intraday series across 9/11–9/16 for any venue. **CME FedWatch remains unreachable (JS shell — do NOT re-attempt `WebFetch`);** BOND's three-venue question is unchanged and unadvanced. (KB-ORC-083 · VX-ORC-08)
>
> **★ THE TWO IRAN AXES HAVE DECOUPLED AND POINT OPPOSITE WAYS.** **Chokepoint disruption DEEPENING:** Hormuz-normal-by-Dec-31 **17.5%** (Δ30d −18, **Δ90d −69**, $11.8M), normal-by-Oct-31 **6.5%**, and the end-September **0–5 transits/day** band **64.0%** (was 40.5% on 9/07, **+23.5pp**). **Escalation DRAINING:** Iran-targets-Bahrain **11.5%** (Δ7d −61.0), Iran-targets-UAE **18.5%** (Δ7d −54.0), SPR-to-280M **10.2%** (Δ7d −65.5). ⚠️ **INFERENTIAL, not measured** — the instrument that would have measured it is the dead one above, so I am reasoning around a hole in my own toolkit. ⚠️ **The Hormuz-normal leg resolves on the IMF PortWatch PRINT, not throughput** (KB-ORC-079): **a detection failure and a real stoppage resolve identically**, so "deepening" may partly be "PortWatch still not printing ≥60." **That caveat cuts against my own headline and is not optional when this is quoted.** ⚠️ Bahrain/UAE are thin ($1.2K / $4.3K) — **directional, not marks.** **Hypothesis, not a finding: a supply interruption that ALREADY happened and is priced as slow to reverse, rather than a war still widening.** (KB-ORC-087)
>
> **★ AN INSTRUMENT DEFECT ON MY OWN LEDGER, FOUND THIS SESSION.** My standing *"cite the MID on wide books"* rule (KB-ORC-069) **returns 50.0% on every SETTLED Kalshi market**, because a resolved contract quotes **bid 0.00 / ask 1.00**. Observed on **five** settled rungs in one pull. **The "WIDE book" flag fires on exactly these rows**, so the rule does not go silent — **it actively recommends maximum uncertainty for an outcome that is certain and known.** **Amendment: apply the mid rule only when `result` is empty; when settled, read `result`.** 🔑 **Second time in three sessions an ORACLE instrument made a settled contract look live** — the Polymarket settled-leg artifact is the same bug on the other side (falsely **certain**; this one falsely **uncertain**). **One shared cause: a display layer that does not read the resolution field.** ⚠️ **A sweep of past ORACLE surfaces for a 50.0-mid citation is NOT done — open check, not a clean bill.** (KB-ORC-086)

---

## Cross-agent tensions

**Two live, one newly opened, one carried unresolved.**

1. 🔴 **ORACLE → PROME/Will, the v4 succession — A RULING IS OWED AND THE DEADLINE MOVED UP.** WQ-190 ratified the $100 leg with the October roll (~9/28) as the deadline. **The leg resolved early, so the instrument is already down and the deadline is effectively NOW.** I have deliberately not re-pinned. **Packet written to `PROME/inbox/` this session.** The decision is not "which slug" but **"does the successor preserve the tail semantics the ratified instrument had, given $100 is now at-the-money."**
2. 🟠 **ORACLE ↔ BRENT/HAWK/FALCON, oil.** WTI printed $105 and retraced to ~$96; Kalshi Brent rungs moved hard (>$85.99 **94.5 mid**, was 82.0 on 9/07; >$91.99 **80.0 mid**, was 61.0). **I own the crowd read only — BRENT owns the tape and the curve, HAWK owns whether the de-escalation in the Gulf-state legs is real.** The 9/18 Active-Month step (KB-ORC-082) is moot for the settled September leg **but governs any October successor verbatim**, so the disclosure does not retire with the contract.
3. 🟠 **ORACLE ↔ RED, recession — the gap PERSISTED, which is the second datum the hypothesis needed.** PM **8.5%** (disjunction contract) vs Kalshi `KXRECSSNBER-26` **5.0 last / 5.5 mid** (927.5K OI). **Both legs drifted up and the ~3pp gap did not close across ten days ⇒ n=2, not a 3-day artifact.** ⛔ **Still NOT asserted as the disjunction premium:** the one call that settles it — **read `KXRECSSNBER-26`'s rules text** — is **carried for a third session** and is the top mechanical item next session. RED's 4–12% interval still contains both venues, so there is **no dispute on level.** (VX-ORC-02)
4. ⚠️ **ORACLE self-flag, carried: my own VX-ORC-02 thresholds cannot see the divergence they name** (keyed >20/40/60pp; the gap is ~3pp). **Flagged a THIRD time, still not silently re-keyed.** This now belongs in the DAEDALUS F-1 instrument build, not in another flag.

---

## DAEDALUS PR#6 — the two asks, both due 2026-09-30, both still OPEN

- **① ORC-04's bands name the AUGUST WTI contract while my readings are SEPTEMBER.** ⚠️ **The ask has been overtaken by events and is now larger than DAEDALUS scoped it:** the September leg has since **resolved**, so re-pointing the bands at "September" would encode a *dead* contract. **The correct fix is a ROLL RULE, not a re-point** — and the roll rule cannot be written until the succession ruling (tension 1) lands. **Sequenced behind the ruling, not dropped; DAEDALUS informed.**
- **② The downgrade trigger has no instrument that can fire it.** **Confirmed, and I found a second instance of the same class this session:** VX-ORC-09's registered tell is *"NEH <30% OR gold retakes the best-asset lead"* — **NEH has never been below 70% in this row's entire history**, so that condition is **not a threshold, it is a decoration.** Both are the untrippable-band class. **Not fixed this session; named with dates.**

---

## Forward catalysts (ORACLE-relevant, dated)

| Date | Event | Instrument to read | Note |
|---|---|---|---|
| **Fri 9/18** | **BOJ September MPM — decision day** | PM top leg **99.9%** ($431.4K) ⏳resolves 9/18 | → SAM, BOND. Venue agreement was 1.2pp on 9/07 |
| **Fri 9/18** | ⚠️ **WTI Active-Month step OCT→NOV CL** | moot for the settled Sept leg; **governs any successor** | **mechanical level shift, no risk content** (KB-ORC-082) |
| Sun 9/20 | Hormuz weekly ladder (wk-of-9/14) resolves | newly rolled pin | ✅ depth checked ($21.0K) |
| **~Thu 9/24** | **Coverage sweep due** | `polymarket.py coverage` | ✅ run 9/17 — 6 hits, nothing pinned |
| Wed 9/30 | Sept Hormuz ladders + Kalshi Brent Sep-30 rungs resolve | | → BRENT, HAWK, FALCON |
| **Wed 9/30** | **DAEDALUS PR#6 ①+② due** | see section above | ① sequenced behind the succession ruling |
| Fri 10/2 | Kalshi Sept U3 rungs resolve | `KXU3-26SEP` (13.5 / 4.5 mid) | → LABOR, HENRY |
| **Wed 10/14** | **September CPI prints** | **Kalshi is the instrument:** `>3.5%` **83.0 mid** | 🔴 **re-read the ladder 10/10 (T-4) for a clean like-for-like vs August** |
| **Wed 10/28** | **October FOMC decision** | PM hike 50.5% / Kalshi differenced ≈50.5% | **venues agree to 0.0pp.** Pin the day before; read same-day |
| Fri 10/30 | BOJ October MPM | PM 79.0% ⚠️thin | → SAM |

---

## What I do NOT claim

- **No lead-lag between PM, Kalshi and rate futures** across 9/11–9/16 — I hold no intraday series for any of them.
- **No CME figure.** FedWatch is a JS shell; every CME number I have ever held is a WALTER relay.
- **No cause for the oil move.** The tail was directionally right; **why** is BRENT's and HAWK's.
- **No physical claim about Hormuz throughput** — my leg resolves on the **PortWatch print**.
- **No clean bill on past surfaces** for the settled-mid defect (KB-ORC-086) — the sweep is not done.
- **Nothing about the desktop's Kalshi lane.** This is the laptop; lane state is per-box.
