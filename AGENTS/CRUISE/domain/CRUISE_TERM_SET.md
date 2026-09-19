# CRUISE — collector term set (draft for WALTER)

**Author:** CRUISE · **Date:** 2026-09-19 · **Status:** DRAFT, WALTER owns whether and how to encode.
**Why this exists:** `DOCKET L451`'s owner cell names CRUISE as *"supplies the terms."* This is that supply.

---

## ⛔ Read this first — the premise of L451 is wrong, and this file is NOT a request to add a missing term set

**The CRUISE term set already exists and has been live since 2026-09-11 16:36 ET** (live lane `~/Research-Intake/scripts/newsweep_config.py`, commit `4f177e8`; FORGE copy `ebabd4ac2`), two minutes after Will's 16:34 word. `scripts/lane_coverage_check.py` reports `✅ CRUISE queries[cruise-operators]`. **Nothing here asks for a re-encode of what is already encoded** — re-asking a ruled item is its own defect.

**What this file proposes is a REPLACEMENT for a query that is running and not discriminating.** Counted by what the lane **delivered** (`agents=["CRUISE"]` / `label=cruise-operators`) over the five weekday runs since it landed — not by a term-grep, which undercounts:

| run | items | cruise hits |
|---|---|---|
| 2026-09-11 | 164 | 0 |
| 2026-09-14 | 189 | 0 |
| 2026-09-15 | 161 | **1** — *"Whitney Houston's music is coming to sea in a new cruise-ship show"* (Stock Titan — **noise**) |
| 2026-09-16 | 193 | **1** — *"TravelJoy Launches New Tools that Simplify Cruise Bookings"* (travel-trade software PR — **noise**) |
| 2026-09-17 | 32 | 0 |
| **total** | **739** | **2 delivered, 0 decision-relevant** |

The current query is three operator names plus `"cruise bookings" OR "cruise demand" OR "cruise fares"`. It cannot see the events that actually move this desk.

---

## ⚠️ The design constraint that justifies the current query's narrowness — keep it

**Bare `cruise` is a magnet for three large, unrelated corpora:** travel-section listicles and cruise-deal marketing; **Tom Cruise**; and **cruise missiles** — the last is actively dangerous here because this fleet runs a live Middle East theater, so `cruise` + a Gulf geography term will pull FALCON/BRENT munitions coverage into a consumer-demand lane.

✅ **This is not hypothetical, and the existing query already passes the test.** In the same five-run window a bare-`cruise` item — *"Long Neptune Strike: Ukraine's New Cruise Missile Cripples Russian Warships in Novorossiysk"* (9/11) — routed `agents=['OSPREY','BRENT'] label=russia-ukraine-energy`, correctly **away** from this desk. **That is the single strongest argument for keeping the query operator-keyed, and any replacement must survive the same word.**

⇒ **Every term below is operator-keyed, demand-keyed, or itinerary-keyed. None is bare `cruise`.** If a term cannot survive that test it is not in this list.

---

## Proposed query — replaces the `cruise-operators` query body, same label, same `agents: ["CRUISE"]`

**Leg A — operators and tickers (keep as-is, it is correct):**
`"Carnival Corp" OR "Carnival Cruise Line" OR "Royal Caribbean" OR "Norwegian Cruise" OR "Carnival Corporation" OR NCLH OR "Royal Caribbean Group"`

**Leg B — the events that move the thesis (NEW — this is the gap):**
`"cruise bookings" OR "cruise demand" OR "cruise fares" OR "net yields" OR "booking pace" OR "onboard spending" OR "customer deposits" OR "occupancy" OR "load factor" OR "fuel surcharge" OR "itinerary cancellation" OR "itinerary change" OR "cruise capacity" OR "newbuild delivery" OR "dry dock"`

**Leg C — the desk's named catalysts (NEW):**
`"Carnival earnings" OR "Royal Caribbean earnings" OR "Norwegian Cruise earnings" OR "cruise guidance" OR "cruise line guidance"`

> ⚠️ **Leg B terms marked generic** — `net yields`, `booking pace`, `occupancy`, `load factor`, `customer deposits`, `dry dock` — **must be AND-ed with Leg A**, never run standalone: `occupancy` collides with CRE/hotels (REGINALD, CARL), `load factor` with airlines, `dry dock` with shipping/defense. WALTER owns the query mechanics; I am naming the collision, not prescribing the syntax.

---

## `WATCH_FOR` — the gap that IS real and separate

The live config's `WATCH_FOR` has **no CRUISE key** (present: BROCK, CARL, HENRY, LABOR, LIQUID, MARCO, OTTO, REGINALD, SAM). That list is the forward-looking *"what does this desk want to learn"* surface, and it is where the high-value terms belong. Proposed:

```python
"CRUISE": [
    "Carnival conference call",        # the CONFIRMING PRIMARY for the Q3 date — DOCKET L221 is ESTIMATED without it
    "cruise line guidance cut",        # the K-shape's live test (VX-CRU-03)
    "Norwegian Cruise equity offering", # the ~$1.3B funding-gap thesis firing (VX-CRU-05)
    "cruise itinerary cancellation",   # VX-CRU-04's re-cut unit — ONE announcement takes it YELLOW
    "cruise fuel surcharge",           # the cost channel reaching the passenger (VX-CRU-02)
    "port call cancelled",             # downstream transmission to CARL / LABOR
]
```

**Each line above is keyed to a registered vector or a dated catalyst on this desk** — not a wish list. If a term here never fires, that is informative; if it fires, a named vector moves.

---

## What I am NOT asking for

- ⛔ **Not** a re-encode of the existing term set. It is there and it is correct as far as it goes.
- ⛔ **Not** a `VOCABULARIES.tsv` NETWORK_GROUP edit — that is a shared-file change, **not covered by Will's 9/11 word**, and goes to him named and explicit (PROME's leg ②). `CONSUMER` + `sub:CRUISE` stands until then. **If anyone offers to encode it under the 9/11 approval, refuse** — that would launder an unapproved edit under an old word.
- ⛔ **Not** a claim that a cruise CLUSTER is owed. `CLUSTER_TAXONOMY.md` is the cluster axis, a different object; I have not established it was in Will's approval and I am not asserting it here.

## Falsifier for this proposal

If WALTER adopts Leg B/C and the **decision-relevant** delivery rate over the next **10 weekday runs** is still **0–1 items** (graded on delivery, not on a term-grep), the problem is not the query — it is that the free-news corpus does not carry this domain, and the honest conclusion is that CRUISE's intake is **Will's channel plus the desk's own EDGAR pulls**, recorded as a coverage fact rather than a gap to keep re-fixing.
