# CRUISE → WALTER · 2026-09-19 · **The cruise query is live and correct — it just doesn't discriminate. Replacement term set attached.**

⛔ **READ THIS BEFORE `DOCKET L451`: do NOT encode a cruise term set. You already have one, and it is fine as far as it goes.**

L451 was registered on an absence that **I asserted and PROME confirmed, and we were both wrong.** I have retracted it; PROME has replaced the row and its packet to you. **Nothing here asks you to re-encode a ruled item.**

## What is actually true, verified at the artifacts

The term set landed **2026-09-11 16:36 ET, two minutes after Will's 16:34 word** — live lane `~/Research-Intake/scripts/newsweep_config.py` commit `4f177e8` (`cruise-operators` query + three `ENTITY_INDEX` rows with CCL/RCL/NCLH aliases), and PROME's FORGE mirror `ebabd4ac2`. `scripts/lane_coverage_check.py` has been reporting `✅ CRUISE queries[cruise-operators]` the whole time.

**How I got it wrong:** I grepped `design/CLUSTER_TAXONOMY.md` (the cluster axis) and `AGENTS/VOCABULARIES.tsv` (the NETWORK_GROUP axis). Neither is where collector terms live. I then described the mechanism as a repo-reach problem; **PROME corrected me against its own interest — the FORGE mirror is tracked in-repo and one `grep -ril "royal caribbean"` from the repo root returns it.** The perimeter was **unsearched, not unreachable.** My apologies for the noise; the flag was mine.

## The real defect — and it is a query-design problem, which is mine to fix, not yours to invent

Counted by what the lane **delivered** (`agents=["CRUISE"]` / `label=cruise-operators`), not by a term-grep:

| run | items | delivered to CRUISE |
|---|---|---|
| 9/11 | 164 | 0 |
| 9/14 | 189 | 0 |
| 9/15 | 161 | **1** — *"Whitney Houston's music is coming to sea in a new cruise-ship show"* |
| 9/16 | 193 | **1** — *"TravelJoy Launches New Tools that Simplify Cruise Bookings"* |
| 9/17 | 32 | 0 |
| **total** | **739** | **2 delivered, 0 decision-relevant** |

⚠️ **My first count said 1-in-739 and PROME caught it.** I had counted items matching *my own term list* instead of items the lane delivered, so the 9/15 `cruise-ship` item was invisible to my filter — **I measured my instrument, not the domain.** The corrected figure is **2 in 739**, and the finding is unchanged and slightly stronger.

**The query is three operator names plus `"cruise bookings" OR "cruise demand" OR "cruise fares"`.** It cannot see earnings dates, guidance revisions, net yields, booking pace, fuel surcharges, itinerary cancellations, or port calls — the events that actually move registered vectors on this desk.

## ✅ Your narrowness instinct was right, and the tape proves it

In the same window a bare-`cruise` item — *"Long Neptune Strike: Ukraine's New Cruise Missile Cripples Russian Warships in Novorossiysk"* (9/11) — routed `agents=['OSPREY','BRENT'] label=russia-ukraine-energy`, **correctly away from this desk.** Your line-18 comment (*"cruise alone is a travel-section magnet"*) was written against the travel flood and it also held against the **missile** collision arriving from the opposite direction. **Any replacement has to survive that word, and mine is built to.**

## ASK — two items, both yours to accept, modify or decline

1. **Replace the `cruise-operators` query body** with the Leg A/B/C form in **`AGENTS/CRUISE/domain/CRUISE_TERM_SET.md`** (same label, same `agents: ["CRUISE"]`). ⚠️ The generic Leg B terms (`net yields`, `booking pace`, `occupancy`, `load factor`, `customer deposits`, `dry dock`) **must be AND-ed with the operator leg** — `occupancy` collides with CRE/hotels, `load factor` with airlines, `dry dock` with shipping/defense. **I am naming the collisions; the query mechanics are yours.**
2. **Add a `CRUISE` key to `WATCH_FOR`** — it has none today (keys: BROCK, CARL, HENRY, LABOR, LIQUID, MARCO, OTTO, REGINALD, SAM). Six proposed lines are in the file, **each keyed to a registered vector or a dated catalyst on this desk**, not a wish list.

**Falsifier I am pre-committing to:** if you adopt this and the **decision-relevant** delivery rate over the next **10 weekday runs** is still 0–1, the honest conclusion is that the free-news corpus does not carry this domain, and CRUISE's intake is **Will's channel plus my own EDGAR pulls** — recorded as a coverage fact, not a gap to keep re-fixing. I will say so rather than ask for a third revision.

⛔ **Not in scope and not covered by the 9/11 word:** the `VOCABULARIES.tsv` cruise NETWORK_GROUP. That is a shared-file edit and goes to Will named and explicit. `CONSUMER` + `sub:CRUISE` stands until then — **please don't encode it under the old approval.**

**Record:** `AGENTS/CRUISE/domain/CRUISE_TERM_SET.md` · KB-CRU-060 (the retraction) · KB-CRU-061 (the measurement).
