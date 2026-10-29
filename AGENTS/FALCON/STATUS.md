# FALCON STATUS

**Updated:** 2026-10-29 12:14 EDT / 16:14 UTC, weekly scenario + GATE-FALCON-001 review (owed 10/28, graded one day late), Will-directed after boot. Runtime Claude Code, Opus 5.5 (claude-opus-5-5). [Review report](reports/2026-10-29_weekly-review-gate001.md). [Prior dashboard preserved verbatim](domain/sources/STATUS_before_2026-10-29_review.md).

## Current marks and authority

| State | Disposition / evidence date |
|---|---|
| B / C / D | **1 / 14 / 85 HELD** at the October 29 weekly review (owed October 28). No registered rung met October 21–29. Next weekly review **November 4**. Convergence **43/50** retained; seven ceiling vectors limit sensitivity |
| D75→85 | FIRED September 28 on FAL-05 route(c); immutable letter in EXIT_PROTOCOL archive. Cannot fire twice |
| Production rung D 85→92 | REGISTERED October 1, WQ-355; ARMED, NOT FIRED. Counting source must establish hostile strike on Gulf-ally production-class facility from September 29. Pipelines/pumps/export terminals/refineries/offices OUT. **Ras Tanura October 27 Houthi claim = refinery + export terminal = OUT-class even if confirmed**; damage UNKNOWN (KB-348/349) |
| Ship losses | **5 confirmed**, unchanged. Class(i)=1 dhow; class(ii)=2 Cape Dao/GFS PRIDE; class(iii-B)=2 Kylo/Riesco; class(iii-A)=0. No new named sinking confirmed. **October 29 ~03:00Z: UKMTO relays a vessel on fire ~9 NM N of Khasab (unnamed, cause unknown; one secondary says projectile and "mostly submerged"); IRGC separately claims 3 tankers hit mines (claim-only, not linked). VI-0085 / KB-354 — not counted until confirmed.** WQ-431 class(ii) HOLD unchanged |
| FAL-06 | OPEN at 70%, resolves November 5. Tests NET Gulf-ally crude/condensate supply; no qualifying net loss established. Required dated search ON November 5. Route hit or single-terminal halt alone cannot fire it |
| FAL-07 | OPEN at 65%, qualifying US offensive strike on Iran October 22–December 31. **NOT FIRED.** WSJ October 27: US told Gulf states to prepare for a "short, intense" post-midterm campaign (~20 warships next month) = reported posture; WH October 22 "not before the midterms" stands. Failed resolution search January 2, 2027 if not confirmed earlier |
| GATE-FALCON-001 | **LIVE**, reviewed October 29 (owed October 28). Leg 1 FIRED 7/23 + leg 3 FIRED 8/15 stand; **leg 2 NOT MET** (own TankerMap October 29: lowest 7d/prior ratio 80.0% vs ≤65%; October 28 6,800 vs 5,330); event override NOT TRIGGERED October 22–29. **Next review_by November 4** |
| L229 permanent route | LAPSED / NOT VERIFIED AS AGREED October 26 (owner grade delivered). Iran FM: strait could open "within days" if US meets conditions; conditional, no executed framework. PROME owns docket; BRENT owns BRT-30 |
| WARRISK | All 5 rows EXPIRED (registered falsifier +23d). WQ-298 standing rule: CANNOT-FIRE, no access re-argued. DEWEY October 25: no matched October quotes exist publicly |
| EXIT / prices | Thesis-kill 0/7. EXIT rewrite triggers not newly met. BRENT owns oil/flow/settlements; HENRY VIX; LIQUID credit. No live FALCON settle clock; step 12b no-op. Trade construction TERRY; no trade or Will decision proposed |

## October 29 review — changes

| Object | Verified change / unresolved limb |
|---|---|
| Ras Tanura | Houthi claim October 27 (Reuters). Only non-Houthi damage source: one anonymous Bloomberg source, terminal-area fire contained. No Saudi/Aramco statement. Own FIRMS read: October 27 heat (~22 MW) inside the site's routine 30-day flare population (~1–38 MW/day) ⇒ uninformative. "Aramco fire contained, 8 injured" relay is a 2016 story, killed. Ops UNKNOWN |
| Sinokor | Iran PGSA October 27: "legal action" against ALL Sinokor vessels from **November 1**; ≥7 already actioned. Reuters: ~40% of September Hormuz crude outflow (unnamed data firms). Hormuz flow already ~1 tanker/day (PortWatch 10/19–25: 23 total, 6 tankers) ⇒ band can't move; a named-hull detention from November 1 would be a shipping-vector event. Declaration, not seizure |
| US maritime posture | NAVCENT/JMIC October 28: non-essential vessels stay well clear; extra time for "military blockade enforcement operations"; neutral vessels may face visit and search. Posture tightening, not kinetic |
| Diplomacy | Conditional 4–5-day reopening offer and reported $1B Saudi→Houthi payment via Tehran: unconfirmed leads only. Vector stays 3 |
| Sensors | **PortWatch repaired:** server-side HTTP-400 flake on ~half of identical requests → retry added. Transit newest 10/25 = 2 total / 1 tanker, DEEPENING unchanged. **Bypass gauge BLIND:** Sohar port988 returns zero rows; crash would have exited 1 (= false COLLAPSE on inverted gauge) → guard added, now rc 2. Sohar new ID not yet found |

## Convergence Matrix

Scores retained; no vector crossed its threshold column at the October 29 review.

| Vector | Score | Current State | Threshold → Next Level | Last Updated |
|---|---:|---|---|---|
| Hormuz status |5| PortWatch ~1 tanker/day to 10/25; PGSA Sinokor action from 11/1; NAVCENT stay-clear | Verified operational reopening + sustained recovery → down | October 29 |
| Iran/proxy operations |5| Houthi Ras Tanura + Najran/Khamis Mushait claims; damage unestablished | One week two-sided quiet incl proxies →3 | October 29 |
| US-Iran direct kinetic |5| Posture build (WSJ, NAVCENT); no qualifying strike | Formal ceasefire + blockade lifted →2 | October 29 |
| Energy tape |5| BRENT owns current figures/settlements | Registered owner fade test, BRENT input | October 29 ownership check |
| Gulf production/bypass |5| No production-class loss established; bypass gauge blind (Sohar ID) | Registered production rung needs IN-class facility/source | October 29 |
| Diplomacy |3| Conditional reopening offers; Oman temporary outline blocked | Dated executed framework →2; actual breakdown event →4 | October 29 |
| Shipping/insurance |5| Census 5 unchanged; all 5 insurance rows expired | At ceiling; no mine attribution inferred | October 29 |
| Cyber/data |2| No verified new cable incident (not re-searched October 29) | Operator-confirmed in-theater incident | October 26 scoped search |
| Macro/credit |3| Owner context; CENTCOM cost ≥$47.1B mid-October (CBS) | HENRY/LIQUID owner input | October 29 |
| Bab al-Mandeb |5| Gate reviewed; leg 2 NOT MET; no enforcement event | Apply gate letter, not secondary totals | October 29 |

**Convergence: 43/50.**

## Evidence controls and next work

- Registered definitions: workbook/EXIT_PROTOCOL.md §2a and domain/FRESH_LEG_BASELINE.md gate letter govern; immutable letters unchanged. FAL-05 failed on route loss; net barrels were not demonstrated. Production ≠ pipeline throughput ≠ export capacity ≠ delivered cargo.
- Four loss instruments never summed: FALCON since-spinout hulls, IMO Sunk, UKMTO total losses, CENTCOM destroyed.
- FIRMS heat/non-detection establishes neither hostile cause, damage, facility identity nor normal operations; run a population control before calling a spike (Ras Tanura flares daily).
- Facility high-water advanced to **October 28** (STRIKES header); newest event row still September 10.
- **Next:** November 1 Sinokor watch (named-hull detention/seizure, Sinokor/Korea response); November 4 weekly + gate review; November 5 FAL-06 dated search; January 2 FAL-07 failure search if unresolved. Ras Tanura operator statement / loadings. UKMTO 182/183/184+ originals (403 from this box). Sohar PortWatch ID.
- Not done this session: CTP/ISW Iraq/PMF read (no quiet inference); cyber/cable re-search; UKMTO 182/183 follow-ups.
- Carried builds remain: KB-168 Yanbu proxy, baseline hot/cold split, sub-$80 duration bar, archive-content guard, EXIT boot reader and full VX sweep; **Sohar portid re-map** (new). Bypass empty-series guard DONE October 29.

## BOTTOM LINE

Nothing this week met a registered trigger, so the marks stay B 1 / C 14 / D 85 and the Bab el-Mandeb tripwire stays live with its tanker-count leg not met. The Houthi Ras Tanura hit is still a claim with no confirmed damage, and it can't fire the production rung because refineries and terminals are excluded. The single most important thing to watch is November 1, when Iran says it will start "legal action" against every Sinokor tanker: a seizure of a named hull would be the next real escalation event, though it can't shrink a Hormuz flow already at about one tanker a day. US posture is tightening (Navy stay-clear advisory, a reported post-midterm campaign plan), but no qualifying strike has happened. Late in the session UKMTO reported a vessel on fire inside the strait off Khasab this morning; its name, cause and whether it sank are unknown, so the loss count stays at 5 until confirmed.
