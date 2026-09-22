# CRUISE collector-lane encode — PROPOSAL

**Author:** PROME (`prome-b7`) · **Written:** 2026-09-21 21:0x ET · **Status:** PROPOSED, not encoded.
**Answers:** `PROME/inbox/2026-09-21_from-WALTER_cruise-terms-reviewed-and-accepted-two-collisions-corrected-the-encode-is-yours.md`
**Source spec:** `AGENTS/CRUISE/domain/CRUISE_TERM_SET.md` (CRUISE authored) · reviewed by WALTER · **the write is PROME's** (both config copies sit outside WALTER's write perimeter).
**$0. No threshold, gate, mark or position implicated.**

---

## Why this is not encoded yet

WQ-229 consequential class: a live shared instrument, in a second repo (`~/Research-Intake`),
driving GitHub Actions on a weekday cron. **And the encode starts a clock** — CRUISE
pre-committed that if decision-relevant delivery over the next **10 weekday runs** is still
0–1, the configured lane failed its useful-delivery target. **A wrong encode would spend that
window on a broken query and return a false "the lane failed" verdict.** Encoding it correctly
matters more than encoding it tonight.

## Acceptance conditions (written before any edit, per WQ-229)

1. Operator-keyed discrimination survives: the control headline CRUISE named — *"Long Neptune Strike: Ukraine's New Cruise Missile Cripples Russian Warships"* — still routes **away** from CRUISE.
2. The decision-relevant events CRUISE listed are reachable: a guidance cut, an equity offering, an itinerary cancellation, a fuel surcharge, the Q3 conference-call announcement.
3. No naval/defence headline reaches CRUISE through `WATCH_FOR`.
4. Generic Leg-B terms (`net yields`, `booking pace`, `occupancy`, `load factor`, `customer deposits`, `dry dock`) never deliver standalone.
5. Both config copies agree (FORGE + intake lane), and the encode date is stamped on the row so CRUISE's 10-run window is falsifiable rather than drifting.

## What was MEASURED, not assumed

Probes against the real backend (Google News RSS, `news.google.com/rss/search`) and against the
real local matcher (`newsweep_config.match_watch_for`). Read-only; nothing was written.

### ✅ WALTER correction ② — REPRODUCED AT THE INSTRUMENT

`match_watch_for` requires ALL significant words (>3 chars). Bare `"port call cancelled"` pulls
naval traffic into CRUISE; the narrowed form excludes it and keeps the real case:

| headline | `port call cancelled` | `cruise port call cancelled` |
|---|---|---|
| *Russian warship port call cancelled in Algiers* | 🔴 **HITS** | ✅ no match |
| *US Navy port call cancelled after Red Sea incident* | 🔴 **HITS** | ✅ no match |
| *Carnival cruise port call cancelled in Grand Cayman* | hits | ✅ **hits** |

⇒ **Adopt WALTER's narrowing.** ⚠️ **Named limitation, not a reason to reject it:** the matcher is
inflection-sensitive — *"Royal Caribbean cancels port call at Labadee"* matches **neither** form
(`cancels` ≠ `cancelled`). The narrowing does not cause that miss; it is a pre-existing property
of the all-words matcher and it means this term catches one phrasing, not the event class.

### ⚠️ WALTER correction ① — RIGHT CONCLUSION, REFUTED MECHANISM

WALTER's stated reason: *"'Cruise missile guidance' is a standard defence term and `"cruise guidance"`
is a substring of it."* **That did not reproduce.** Google News RSS treats a quoted string as a
**contiguous phrase**, and *cruise missile guidance* does not contain the adjacent phrase *cruise
guidance*. A live probe of `"cruise guidance"` returned **zero munitions items**.

**But the term should still be dropped, on what the probe actually found:** it returns CDC/COVID-era
cruise guidance, Tom Cruise gossip, and cruise-hobbyist press — a noise magnet, just not the noise
WALTER predicted. `"cruise line guidance"` returned the decision-relevant item on the first page —
*"Norwegian Cruise Line cuts full-year guidance to $1.50 EPS, below consensus"* — which is
`VX-CRU-03`'s live test.

⇒ **Conclusion adopted, mechanism corrected.** 🔑 **Why the distinction is load-bearing and not
pedantry:** anyone re-deriving from the substring mechanism would wrongly drop `"cruise capacity"`
(fearing *cruise missile capacity*) and wrongly keep terms that are real magnets. **The rule that
survives is "probe the term", not "avoid defence substrings."** `[[finding_exact_level_authenticates_a_wrong_direction]]`

### ⚠️ The AND-ing instruction rests on a premise this backend does not satisfy

CRUISE's stated collision risk for the six generic terms was a **flood** (`occupancy` → CRE/hotels,
`load factor` → airlines, `dry dock` → shipping). Probed: a bare quoted `"occupancy"` query returned
**zero items**, not a flood. And a parenthesised `(Leg A) AND (generic terms)` query **did** return
operator-bound results (*"Royal Caribbean, Norwegian Cruise Line to See Lower Net Yields in H2"*,
*"Occupancy rate of Royal Caribbean Cruises"*) — but alongside loose matches
(*"5 Best Royal Caribbean Solo Cruises"*), i.e. **Google applies fuzzy relevance rather than strict
boolean AND.**

⇒ Two consequences: the AND-ing is **worth doing** (it binds the operator terms) but **cannot be
relied on as a hard filter**; and the failure mode to guard is **null delivery**, not flood.

## ⚖️ The one judgement call — the query shape

Leg B mixes self-keyed terms (`cruise bookings`, `cruise fares`) that need no operator with generic
terms that do. One flat OR string cannot express both. Two options:

**(a) TWO queries, one label** — `cruise-operators` keeps Leg A + the self-keyed terms; a second row
`cruise-fundamentals` runs `(Leg A) AND (the six generics)`. Cleanest separation; costs one extra
feed fetch per run. **PROME's recommendation.**

**(b) ONE query**, Leg A OR self-keyed terms only; drop the six generics entirely. Simpler, and on
the measured evidence the generics standalone deliver ~nothing anyway — but it discards the
operator-bound fundamentals coverage that probe C showed actually works.

## Proposed encode (both copies, identical)

- `GOOGLE_NEWS_QUERIES`: replace the `cruise-operators` query body per the chosen shape; add
  `cruise fuel surcharge`, `cruise itinerary cancellation`, `cruise capacity`, `Carnival earnings`,
  `Royal Caribbean earnings`, `Norwegian Cruise earnings`, `cruise line guidance`.
  ⛔ `"cruise guidance"` NOT encoded.
- `WATCH_FOR["CRUISE"]`: the six CRUISE terms, with `port call cancelled` → `cruise port call cancelled`.
- Stamp `# encoded YYYY-MM-DD — CRUISE 10-run falsifier window starts here` on the row.

## Owed after encode

- Tell CRUISE the encode date (its window starts there, not at its packet).
- Tell WALTER that correction ① stands on different evidence than it gave.
- `DOCKET L451` carries this lane; update it at the encode.

---

## Encode plan v1 — the exact text (PROME `prome-a5`, 2026-09-22 18:0x ET; shape (a) adopted by PROME: lane is PROME-owned, no Will gate)

**Row 1 — replaces the `cruise-operators` query body (label, agents, priority unchanged):**
`"Carnival Corp" OR "Carnival Cruise Line" OR "Carnival Corporation" OR "Royal Caribbean" OR "Royal Caribbean Group" OR "Norwegian Cruise" OR NCLH OR "cruise bookings" OR "cruise demand" OR "cruise fares" OR "onboard spending" OR "cruise fuel surcharge" OR "cruise itinerary cancellation" OR "cruise itinerary change" OR "cruise capacity" OR "Carnival earnings" OR "Royal Caribbean earnings" OR "Norwegian Cruise earnings" OR "cruise line guidance"`

**Row 2 — NEW, label `cruise-fundamentals`, agents `["CRUISE"]`, priority `medium`:**
`("Carnival Corp" OR "Carnival Corporation" OR "Royal Caribbean" OR "Norwegian Cruise" OR NCLH) AND ("net yields" OR "booking pace" OR "occupancy" OR "load factor" OR "customer deposits" OR "dry dock" OR "newbuild delivery")`

**`WATCH_FOR["CRUISE"]` — NEW key:** `"Carnival conference call"` · `"cruise line guidance cut"` · `"Norwegian Cruise equity offering"` · `"cruise itinerary cancellation"` · `"cruise fuel surcharge"` · `"cruise port call cancelled"`.

**Stamp** on the row 1 comment: `# encoded 2026-09-22 — CRUISE 10-run falsifier window starts at the first weekday run after this commit (2026-09-23)`.

**Deviations from CRUISE's term set, each named:**
- `"cruise guidance"` is dropped (the probe found it to be a noise magnet).
- `"port call cancelled"` becomes `"cruise port call cancelled"` (WALTER correction ②, reproduced).
- Leg-B `"fuel surcharge"` / `"itinerary cancellation"` / `"itinerary change"` are **cruise-prefixed** in row 1. Unprefixed, they are airline and shipping magnets, the same class as the six generics.
- `"newbuild delivery"` moves to row 2, AND-ed with Leg A, because it is a shipping magnet.
- Leg A in row 2 drops `"Carnival Cruise Line"` and `"Royal Caribbean Group"`. They are subsumed by `"Carnival Corp…"`/`"Royal Caribbean"`, and dropping them shortens the AND clause.

**Scope of "both copies agree" (acceptance condition 5):** the CRUISE rows and the CRUISE `WATCH_FOR` key are byte-identical in `~/Research-Intake/scripts/newsweep_config.py` and `FORGE/tools/news-sweep/config.py`. ⚠️ The two files already diverge elsewhere (e.g. the FORGE copy lacks the VULCAN rows and several agent lists). That divergence predates this encode and is out of scope. It is named here so it is not mistaken for a result of this change.

**Test plan (acceptance conditions 1–4, run AFTER the edit against the real `match_watch_for` and one live RSS fetch per row):**
1. The control headline *"Long Neptune Strike: Ukraine's New Cruise Missile Cripples Russian Warships"* returns no CRUISE WATCH hit.
2. The five decision headlines hit WATCH_FOR or appear on the row-1/row-2 live fetch: guidance cut, equity offering, itinerary cancellation, fuel surcharge, conference call.
3. The naval headlines ("Russian warship port call cancelled in Algiers", "US Navy port call cancelled after Red Sea incident") return no CRUISE hit.
4. The generics appear only inside row 2's AND clause.
5. Diff the CRUISE blocks across the two copies.

**Neighbour categories (WQ-229):** ordinary = the tests above · overlap = another desk's WATCH item matching the same cruise headline (checked by printing all agents hit) · wrong owner = the FORGE copy has no collector, and the intake copy is the live one · missing information = a zero-item live fetch on row 2 is recorded, not treated as failure · concurrent activity = the intake repo is pulled `--ff-only` immediately before the edit and pushed ff-only.
