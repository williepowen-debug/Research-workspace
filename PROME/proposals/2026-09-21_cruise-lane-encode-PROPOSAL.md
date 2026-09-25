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

## Encode plan v1 — the exact text (PROME `prome-a5`, 2026-09-22 ~17:10 ET [restamped; first written as 18:0x]; shape (a) adopted by PROME: lane is PROME-owned, no Will gate)

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

---

## Plan read v1 — verdict NO (coldreader `cruiseplancold`, Opus, 2026-09-22 ~17:12 ET [restamped from the commit clock at closeout; first written as ~18:1x]; ledger in the prome-a5 session scratchpad, findings summarised verbatim-in-substance here)

**3 ✅ · 5 ⚠️ · 4 ❌. NOT ENCODED. CRUISE's 10-run clock has NOT started.**

- ❌1 **Delivery dies at the KNOWN-entity suppression step, not at the query.** In `~/Research-Intake/scripts/fetch_newsweep.py` L95-97, `classify_article` suppresses any headline naming an ENTITY_INDEX entity (Carnival / Royal Caribbean / Norwegian Cruise → CRUISE, config L372-374) unless it hits WATCH_FOR or carries an escalation word. Live test: row 1 **kept 1 of 15**, row 2 **1 of 15**. Suppressed items included "NCLH CEO Calls for Major Changes as Booking Pace Slows" and "Royal Caribbean, Norwegian Cruise Line to See Lower Net Yields in H2". ⇒ **This is the likely mechanism behind the 0-decision-relevant-in-739 result**, and any encode that leaves it in place makes the falsifier grade the suppressor.
- ❌2 `match_watch_for` tests substrings, so `cruise port call cancelled` fires on "missile **cruiser**'s Havana port call cancelled". Acceptance condition 3 fails.
- ❌3 `cruise line guidance cut` reduces to cruise ∧ line ∧ guidance ("cut" ≤3 chars is dropped). It fires on "Pentagon issues new guidance on cruise missile production line" and misses "Royal Caribbean lowers 2026 guidance".
- ❌4 The deviation "Carnival Cruise Line is subsumed by Carnival Corp" is false.
- ⚠️ Only 2 of 5 decision events are reachable, each in one phrasing. An equity offering worded "Public Offering of Ordinary Shares" is suppressed. "Cruise lines cancel Red Sea sailings" is classed NOISE. The 15-item cap is filled by operator chatter, starving the self-keyed terms. Row 2 has no stamp. The two copies' `match_watch_for` implementations differ (the FORGE copy lacks entity-token logic).

**Disposition (PROME, 2026-09-22):** v1 is withdrawn. The next version is a **collector change, not a term encode**: CRUISE-row items must not be suppressed as KNOWN, following the precedent of the saudi-redsea keys comment at L566-570. It also needs word-boundary WATCH matching, or anchors that do not collide with "cruiser"/"cruise missile", and operator-keyed guidance and offering items. New acceptance condition 6: **a decision-relevant, operator-named headline survives `classify_article`.** Per the WQ-178 read budget, v2 gets its own plan read before any edit. Carried on DOCKET **L452** (the lane falsifier row; the earlier "L451 carries this lane" line above is WRONG — L451 is the CRU-09 retraction marker).

---

## Encode plan v2 — COLLECTOR change + operator-noun phrases (PROME `prome-2e`, 2026-09-25 12:4x ET; shape decided with WALTER's live read 12:41 ET: *"plan-read your v2, (a) plus (b). A word-boundary change doesn't fix CRUISE's real problem"* — a suffix-aware matcher is a separate fleet-wide change, kept apart)

**Why v2 is a collector change (v1's ❌1):** `classify_article` Step 4 suppresses every headline whose entity resolves through `ENTITY_INDEX` unless a WATCH phrase or an escalation word fires. CRUISE's three operators ARE index entities, so the operator-keyed query fetches the right items and the classifier then drops them (live: 1 of 15 kept per row). The desk's decision events — a guidance cut, an equity offering, a yield warning — carry no escalation word. **The suppressor, not the query or the corpus, is the mechanism behind 0-of-739.**

### Acceptance conditions v2 (written before any edit — WQ-229; conditions 1–5 carried from v1 verbatim)
1. Operator-keyed discrimination survives: *"Long Neptune Strike: Ukraine's New Cruise Missile Cripples Russian Warships"* still routes **away** from CRUISE (no entity, no CRUISE watch hit).
2. The decision-relevant events CRUISE listed are reachable: a guidance cut, an equity offering, an itinerary cancellation, a fuel surcharge, the Q3 conference-call announcement.
3. No naval/defence headline reaches CRUISE through `WATCH_FOR` — including *"missile cruiser's Havana port call cancelled"* and *"Pentagon issues new guidance on cruise missile production line"* (v1 ❌2/❌3).
4. Generic Leg-B terms (`net yields`, `booking pace`, `occupancy`, `load factor`, `customer deposits`, `dry dock`) never deliver standalone.
5. Both config copies agree on every CHANGED region (FORGE + intake lane), and the encode date + lane commit sha are stamped on the query rows so CRUISE's 10-run window is falsifiable rather than drifting.
6. **A decision-relevant, operator-named headline survives `classify_article` delivered and routed to CRUISE:** fixture = *"NCLH CEO Calls for Major Changes as Booking Pace Slows"* · *"Royal Caribbean, Norwegian Cruise Line to See Lower Net Yields in H2"* · *"Norwegian Cruise Line cuts full-year guidance to $1.50 EPS, below consensus"* (all three were suppressed at v1's live probe). Expected: classification `KNOWN`, `suppressed: False`, `agents` ∋ CRUISE.
7. **No other desk's delivery changes:** `classify_article` over every stored lane item (`data/*/news.json`, 9,931 items at 12:4x ET) is identical before and after on `classification · suppressed · entity · agents-via-entity · watch_hits`, EXCEPT items whose entity resolves to a cruise operator; the diff list is the receipt and its count is reported.
8. **Bare "carnival" no longer binds the operator:** *"Rio Carnival draws record crowds"* → entity `None` (today: entity `Carnival` → CRUISE, KNOWN-suppressed; after the flag it would be DELIVERED to CRUISE — the noise path the key rename closes). *"Carnival Corp"*, *"Carnival Cruise Line"*, *"Carnival Corporation"*, `CCL` (word-bounded) still bind.
9. **Neighbours (WQ-229, all five considered):** ordinary = 6 · overlap = a cruise-operator headline that ALSO hits another desk's WATCH phrase stays `NEW_WATCH_HIT` for that desk with CRUISE added through the entity agents, exactly as today · wrong owner = 1 and 8 · missing information = title-only classification is the collector's path (`fetch_newsweep.py` passes no description), unchanged; the description branch is untouched · concurrent = WALTER's `watch_for_harness.py` imports this config at test time — the new `deliver_known` field is additive and must not break the import (`--desk CRUISE --current` must load after the edit).
10. **Downstream token check:** `news.json` `by_class` will carry a `KNOWN` key for the first time. `fetch_newsweep.py`'s alert list (`NEW_ALERT · NEW_WATCH_HIT · DEVELOPMENT`) and WALTER's `intake_scan.py` (`NEW_ALERT → ACTION · NEW_WATCH → INFO`) neither count nor choke on it — verified by reading both call sites; WALTER is told by packet so its boot read is not surprised by the new key.

### The edits (exact; both copies unless marked)
**E1 — `ENTITY_INDEX` (both copies):** key `"Carnival"` → `"Carnival Corp"` with aliases `["CCL", "Carnival Cruise Line", "Carnival Corporation", "Carnival plc"]` and `"deliver_known": True`; add `"deliver_known": True` to `"Royal Caribbean"` and `"Norwegian Cruise"` (aliases unchanged). No other entry gains the field.
**E2 — `classify_article` Step 4 (both copies), the KNOWN branch only:**
```python
        else:
            result["classification"] = "KNOWN"
            # deliver_known (2026-09-25, CRUISE lane encode v2): an index entity whose
            # decision events carry no ESCALATION_QUALIFIER (a guidance cut, an equity
            # offering, a yield warning) is delivered as KNOWN instead of dropped.
            # Opt-in per entity; every other entity keeps KNOWN → suppressed.
            result["suppressed"] = not bool((entity_info or {}).get("deliver_known"))
```
The classification token stays `KNOWN` (no new vocabulary); only `suppressed` flips for flagged entities.
**E3 — `GOOGLE_NEWS_QUERIES` (both copies), shape (a) from the judgement call above:**
- `cruise-operators` body → `"Carnival Corp" OR "Carnival Cruise Line" OR "Royal Caribbean" OR "Norwegian Cruise" OR NCLH OR "cruise bookings" OR "cruise demand" OR "cruise fares" OR "cruise capacity" OR "cruise fuel surcharge" OR "cruise itinerary cancellation" OR "Carnival earnings" OR "Royal Caribbean earnings" OR "Norwegian Cruise earnings" OR "cruise line guidance"` (⛔ `"cruise guidance"` NOT encoded; `newbuild delivery` dropped — a shipbuilding term with no operator noun).
- NEW row `cruise-fundamentals`, agents `["CRUISE"]`, priority medium: `("Carnival Corp" OR "Royal Caribbean" OR "Norwegian Cruise") AND ("net yields" OR "booking pace" OR "occupancy" OR "load factor" OR "customer deposits" OR "dry dock" OR "onboard spending")` — Google applies fuzzy relevance, so this binds the generics to an operator without being a hard filter; the guarded failure is null delivery, not flood (measured 9/21).
- Both rows carry `# encoded 2026-09-25 <lane sha> — CRUISE 10-run falsifier window (DOCKET L452) starts at this commit`.
**E4 — `WATCH_FOR["CRUISE"]` (both copies) — 11 operator-noun phrases, LANDED ONLY AFTER WALTER's live R3 test (today's letter: a lane-only zero is UNINFORMATIVE), not part of the collector commit:** `Carnival conference call` (L221 Q3-date confirmer) · `Carnival guidance` · `Royal Caribbean guidance` · `Norwegian Cruise guidance` (VX-CRU-03; replaces v1's `cruise line guidance cut`, ❌3) · `Norwegian Cruise equity offering` · `NCLH offering` (VX-CRU-05; `NCLH` is a required word-bounded token) · `cruise itinerary cancellation` (VX-CRU-04) · `cruise fuel surcharge` (VX-CRU-02) · `cruise ship port call cancelled` (replaces `cruise port call cancelled`, ❌2 — a cruiser is not a ship in any headline that also says "port call") · `Carnival earnings` · `Royal Caribbean earnings` (Leg C; CCL Q3 ~9/28–29, L221).
**E5 — records:** DOCKET L452 state stamped with the encode date + lane sha, its VESTIGIAL 10/05 date re-dated to **2026-10-12** (the first PROME boot after the 10th weekday run, 9/28→10/09); CRUISE packet naming the encode date and the 11 phrases pending WALTER's test; WALTER packet (the `KNOWN` by_class key, the phrases for `--live` testing, correction ① standing on different evidence).
**E6 — FORGE mirror residue, declared not fixed:** `FORGE/tools/news-sweep/config.py` `match_entity` lacks the lane's 2026-07-30 ticker word-boundary fix (pre-existing divergence, found by v1's reader); E1–E4 are applied to it identically, the divergence is recorded here and on L452, and it is NOT repaired in this encode (a different change with its own read).

### Test (written before the edit): `~/Research-Intake/scripts/test_cruise_delivery.py`
- `--selftest`: conditions 1 · 3 · 6 · 8 as fixtures (expected classification / suppressed / entity / CRUISE in agents / watch_hits empty), plus condition 4 (each generic alone → no CRUISE delivery).
- `--baseline <json>` (run BEFORE the edit, saved to the session scratchpad) and `--diff <json>` (run AFTER): classify every stored title, compare the five fields; print the changed items; exit 1 if any changed item's entity is not a cruise operator (condition 7).
- The reader is asked to devise at least one counterexample of its own (WQ-229 consequential class: a shared collector).

### Owed after encode
- CRUISE: encode date + sha; the window starts there. WALTER: by_class `KNOWN` key + the 11 phrases for `--live` testing + correction ① note. DOCKET L452 update. Result read (one) of the diff; residue declared here.

## Plan read v2 — verdict NO as written (coldreader `cruiseplan2`, Opus, 2026-09-25 12:51 ET; ledger `scratchpad/cruise/planread_v2.md` in the prome-2e session; 15 ✅ · 8 ⚠️ · 5 ❌; 7 reader-devised counterexamples C1–C7). E1+E2 CONFIRMED to fix the suppression: live fetch of both v2 rows went from 0 and 1 of 15 kept to 15 of 15.

**❌ fixes applied to the plan (WQ-178: ❌ only, one pass), 12:5x ET:**
- **❌6 · ❌7 · ❌15 (E4 phrases fail conditions 3 and 8 under the substring matcher — C1 "missile cruiser's … port call cancelled as warship heads home", C2 "Royal Navy issues Caribbean hurricane guidance", C3 "Notting Hill Carnival: Met Police issue safety guidance") ⇒ E4 is REMOVED from this encode.** No `WATCH_FOR["CRUISE"]` key lands with the collector change. The phrases become a separate CRUISE-owned R3 proposal in ticker-bound form (`CCL` / `RCL` / `NCLH` as required word-bounded tokens: e.g. `NCLH guidance` · `RCL guidance` · `CCL guidance` · `NCLH equity offering` · `CCL conference call`), WALTER live-tests, PROME lands — the WQ-295 path every other desk took today. Conditions 3 and 8 hold at this encode by construction.
- **❌12 (condition 7 could not fail and its exception covered the real change) ⇒ condition 7 RESTATED:** over the stored corpus, changed titles are confined to those whose OLD entity was `Carnival` or a cruise operator, each printed with old→new entity/class; count reported. The classes E1/E2 RELEASE are absent from the stored corpus by construction and are declared as INTENDED consequences: (i) bare-"carnival" headlines: KNOWN-suppressed → `NEW`, delivered to the fetching query's agents only (those that carried an escalation word were ALREADY delivered — to CRUISE, wrongly; now to nobody by entity); (ii) operator headlines fetched by a non-cruise query or feed (gulf-theater, BBC): suppressed → `KNOWN` delivered to the fetcher's agents + CRUISE; (iii) entity re-attribution (C4 "Blackstone buys stake in Carnival festival promoter" → Blackstone/BROCK after the rename) — a correct re-attribution the old key was masking, counted in the diff.
- **❌11 (test crash `("Carnival",) | set`; exit 1 ambiguous) ⇒ `test_cruise_delivery.py` fixed:** set literal; the diff guard fails only on a changed title whose OLD entity is outside {Carnival, cruise operators}; any exception exits 2 (CANNOT-EVALUATE), never 1.

**⚠️ residue, declared (not fixed in this encode):** ⚠️3 "0-of-739" is CRUISE's own count (`CRUISE_TERM_SET.md`: 739 items, 2 delivered, 0 decision-relevant) — wording kept, source now named. ⚠️5 **`NOISE_TITLE_PATTERNS` drops any title containing "cancel" at Step 0, BEFORE watch matching — an itinerary-cancellation headline (VX-CRU-04, C6) is UNREACHABLE on this lane before and after this encode; CRUISE's falsifier counts 4 reachable events, not 5; narrowing the noise pattern is a separate fleet-wide change.** Live row 1's 15 capped slots all went to operator chatter (the cap starves the self-keyed terms — also v1's ⚠️). ⚠️9 the FORGE mirror's `match_watch_for` ALSO lacks the ticker logic (E6 widened); the row stamp carries the DATE and the commit is located by `git log -S"cruise-fundamentals"`, since a commit cannot carry its own sha. ⚠️14 condition 8's premise corrected: "Rio Carnival draws record crowds" is DELIVERED to CRUISE today ("record" is an escalation word) — the rename closes a LIVE noise path. ⚠️16 entity ordering is pre-existing (cruise entries sit first; C7 "Royal Caribbean reroutes ships around Strait of Hormuz" resolves to CRUISE ahead of Hormuz/HENRY) and unchanged by E1; the concurrent check becomes an import check of the harness, since `--current` has nothing to test without E4. ⚠️22 the window starts at the lane commit; ten WEEKDAY RUNS (9/28→10/09 if no run is missed) — a missed run extends it; grade at the first PROME boot after the 10th run. ⚠️23 moot (E4 out). ⚠️27 the test's `cruise_routed` = entity agents + watch hits, which is the collector's own agents rule minus the fetching query's defaults — acceptable for these fixtures.

## Result read v2 — installed E1/E2/E3 + test (coldreader `cruiseresult2`, Opus, 2026-09-25 12:58 ET; ledger `scratchpad/cruise/resultread_v2.md`; 16 ✅ · 11 ⚠️ · 2 ❌; verdict "mostly yes": edits match the fixed plan in both copies, E4 absent, C1–C3/C5 resolve to NEW, C4 → Blackstone as declared, corpus diff reproduced independently 1/9,433)

**❌ fixes applied (the one allowed further edit after the result read; neither changes a RULE — no third read):**
- **❌24 the `cruise-fundamentals` row delivered OLD news** (live: 15/15 items aged 36–1,508 days; the URL builder sends no recency limit and suppressed items were never marked seen) ⇒ ` when:7d` appended to that query in both copies; re-measured live 12:5x ET: 15/15 aged 0–6 days.
- **❌11 the "cancel" residue was OVERSTATED**: `NOISE_TITLE_PATTERNS` matches the BARE WORD only (`\b(subscription|cancel|refund)\b`); "cancels" / "cancelled" / "cancellation" pass and route to CRUISE. Lane comment corrected; **CRUISE's falsifier stays at 5 reachable events**; only the bare-word form (C6 "…to cancel Gulf sailings") is dropped.

**⚠️ residue declared — file CLOSED for the session (WQ-178):** ⚠️12 entity shadowing (C7 "Royal Caribbean reroutes ships around Strait of Hormuz" → CRUISE only; HENRY/SAM see it only if their own query fetched it) — pre-existing index order · ⚠️14/15 test docstring exit-code wording and `--selftest` exiting 1 on an exception (cosmetic; `--diff` is the guarded mode) · ⚠️16 condition-3 fixtures pass because no CRUISE watch phrases exist; no entity-collision fixtures · ⚠️18 mirror comments differ (code identical) · ⚠️19 `deliver_known` turns the FORGE mirror's loose substring matches into deliveries — the mirror runs nothing (no cron) · ⚠️20 the `git log -S` locator resolves only after the commit (it does now) · ⚠️23 KNOWN deliveries create no WALTER intake record and no run alert — by design (CRUISE reads its news.json rows; WALTER told by packet) · ⚠️25 "Carnival Corp" is still a substring key ("Notting Hill Carnival corporate sponsors…" → CRUISE) · ⚠️26 the `CCL` ticker alias binds CCL Industries (live 4/4 sampled) and `NCL` has the same shape — a noise path into CRUISE's window, counted there, CRUISE may ask to drop the aliases · ⚠️27 "Norwegian cruise missiles" → CRUISE via the entity.

**STATE (WQ-229): IMPLEMENTED · TESTED (selftest 16/16 · corpus diff 1 changed/0 unexplained · live 15/15 both rows, recency verified) · INDEPENDENTLY READ with two ❌ fixed AFTER the read and eleven ⚠️ carried · STILL UNRESOLVED: the WATCH_FOR["CRUISE"] phrases (CRUISE re-proposes ticker-bound forms through R3), the `CCL`/`NCL` alias noise path, the cap-starvation of self-keyed terms.**
