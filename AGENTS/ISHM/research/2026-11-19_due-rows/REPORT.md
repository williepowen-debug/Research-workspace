# ISHM — November 19, 2026 due-row wake (PROME prome-36)

**Session:** ISHM, Claude Code, Opus 5.5 (`claude-opus-5-5`), launched at `AGENTS/ISHM/`, repo root `/home/willi/Research-workspace`, laptop. Task letter: PROME prome-36, 2026-11-19 09:24:08 ET, due-row wake under PROME C6.
**Boot:** `boot.py` rc 1 (REVIEW: Philadelphia and Kansas City due today; ACT final and the frame-prep row due tomorrow; known carries AAR-BREADTH row 47 date and VX-ISH-08 unscored). Corrections check rc 0. FRED current on all 7 series. Checkout already contains `origin/master` after fetch (0 incoming); the tree is dirty with LIQUID's work, so nothing was pulled or stashed.
**Rules applied:** graded only by the desk's own written rules (catalyst rows' "Regional composite sign (band OWED)"; VX-ISH-01's "count of regional surveys below zero"). No level, band, threshold, score, gate or trade changed.

## Due rows

| Row | Result | Evidence |
|---|---|---|
| `2026-11-19 [PHILLY]` November | **PUBLISHED, GRADED. Row retired** (successor 2026-12-17 registered) | Issuer PDF `bos1126.pdf` HTTP 200, read 09:24 ET, sha256 `d51be6bd74b3641e` (same file as WALTER's card) → `sources/bos1126.pdf`, text `sources/bos1126.txt` |
| `2026-11-19 [KCFED]` November | **NOT-READ, route-limited. Row kept open, re-dated 2026-11-20 as a recheck** | See § Kansas City |
| `2026-11-20 [CLASS8-ORDERS]` October final | **PUBLISHED November 18, read a day early, GRADED. Row retired** (successor 2026-12-04 registered) | ACT blog HTTP 200 09:25 ET, saved `sources/act_class8_blog_0926ET.html` (sha256 `c92baf0e067297eb`) |
| `2026-11-20` Prep before the November flash | **DONE a day early.** Frame `RELEASE_PREP_2026-12-01.md` frozen. Forecast rows considered; none registered (reason in the frame). Row retired | Desk root |

## Philadelphia — November

Responses November 9–16; all SA diffusion; October values unrevised in the issuer's Previous column.

| Index | November | October |
|---|---|---|
| General activity | **6.3** (lowest since May) | 20.9 |
| New orders | **−0.4** (lowest since May, fourth straight decline) | 4.3 |
| Shipments | 25.7 | 15.3 |
| Unfilled orders | −4.4 | 2.4 |
| Delivery times | 3.5 | 8.5 |
| Inventories | 5.3 | −12.8 |
| Prices paid / received | 58.2 / **47.0** (received highest since June 2022) | 43.2 / 40.1 |
| Employment / workweek | 11.6 / 11.2 | 9.1 / 7.5 |
| Future activity / new orders / shipments | 33.6 / 31.7 / 25.4 (orders and shipments lowest in more than a year) | — |
| Future capital expenditures | **18.9** (lowest since February, third decline) | 34.9 |

Special questions: 42.3% say core customers became more price sensitive since last quarter; 56.0% expect near-term industry cost changes, and of those 78.6% expect competitors to raise prices, median three months.
⚠️ Issuer prose says the special questions were about 2027 capex categories; the printed questions are price sensitivity and pass-through. The table is what was read.

**Grade by the written rule:** activity sign **positive**; no regional band is registered, so nothing fires. New orders went negative, the first negative district this month.

## Kansas City — November

Not read. Whether it is published is UNKNOWN; nothing below is evidence that it is not.

| Route | Time (ET) | Result |
|---|---|---|
| curl, survey index | about 09:27 | Timeout after 30 s, no response (status 000, 0 bytes) |
| curl, `documents/20082/2026Nov19.pdf` and the known October `2026Oct22.pdf` | about 11:03 | Both timed out after 60 s with no response. The October file exists, so this is the route, not absence. No challenge page, no 403. DATA_ROUTES.md recorded the same curl timeout at build |
| WebFetch, survey index | 11:03, 11:28 | HTTP 200, but the release list is truncated at "Survey Results"; no November link in the readable text |
| WebFetch, release-dates page | about 11:10 | HTTP 200; now shows only the 2027 schedule, so the November 19 date cannot be re-confirmed there (it was PRIMARY when the row was written) |
| WebFetch, newsroom | 11:28 | HTTP 200; newest manufacturing item "Tenth District Manufacturing Activity Increased Steadily in October", October 22, 2026; speeches dated November 12 are listed |
| WebFetch, guessed `2026Nov19.pdf` | about 11:05 | 404 on a guessed filename; not proof of absence. No further paths guessed (PROME prome-36 instruction) |
| Extended web search | about 11:10 | No November 2026 item; October found (composite 11, new orders 3 from 24, agreeing with the PRIMARY October row) |

No identity, address or proxy change was tried. PROME was told at 11:18 ET and confirmed the plan: one WebFetch check about 11:30, then NOT-READ. Recheck November 20 at the issuer or on a WALTER card; a dated secondary relay may be logged labelled SECONDARY, never as the issuer read.

## Regional breadth, November so far (new orders, issuer SA)

| District | November | October |
|---|---|---|
| New York (Empire, November 16) | 3.0 | 23.2 |
| Philadelphia (November 19) | **−0.4** | 4.3 |
| Kansas City | NOT-READ | 3 |
| Richmond | November 24 | −8 |
| Dallas | November 30 | 9.3 |

Two of five in, one negative. Every district read so far cooled. The unregistered "≤1 of 5 negative" description cannot be read until all five are in; it is not a band and fires nothing.

## ACT Class 8 — October final

Final 13,755, −44% y/y (preliminary 13,500, −45%; +255 units). Against September's final 19,172: −28.3% m/m NSA (ISHM arithmetic on two finals). Classes 5–7 final 17,731, +12% y/y (preliminary 18,000, +14%). ACT: EPA 2027 ambiguity "is prompting fleets and OEMs to delay Class 8 order activity"; "underlying demand remains"; medium-duty strength "appears linked to dealer inventory stocking ahead of anticipated 2027 regulatory cost increases" (issuer judgment, unmeasured). FTR's final was not public at 09:27 ET. J2: Class 8 is a qualified input, not a deterioration-test leg; nothing fires. Packets: LIQUID `a9edb1d30a`, RED `3fbec372bc`.

## Combination watch (WQ-622 A)

| Theme | Added |
|---|---|
| combo:order-pull-forward KB-ISH-056 | Philadelphia orders −0.4 while inventories +5.3 and prices received 47.0; competitors expected to raise prices within three months. Counterevidence: 42% say customers more price sensitive. ACT: medium-duty orders tied to dealer stocking ahead of 2027 cost increases |
| combo:factory-hiring-gap KB-ISH-058 | Philadelphia employment 11.6, workweek 11.2; future employment lowest since February |
| combo:freight-vs-factory-gap KB-ISH-061 | ACT October final 13,755, −44% y/y |

New rows KB-ISH-071 (Philadelphia), KB-ISH-072 (ACT final). Logging is not scoring.

## Charter line changed (task letter, WQ-719 A / WQ-721 A)

`AGENTS/ISHM/CLAUDE.md` § BOOT SEQUENCE step 6, the `NEXUS_BRIEF.md` bullet (line 56). It made the brief an every-session write-back ("as the last write-back, after the final STATUS commit"). It now carries NEXUS's wording: rewrite only when a figure, threshold, or cross-desk send or wait changed; a PIN-UNRESOLVED pin is corrected alone, with no new As-of. The ordering rule is kept for when the brief is rewritten.

## Inbox (every lane)

| Item | Disposition |
|---|---|
| `inbox/WALTER/SIG-W-20261119-002.md` (Philadelphia card) | INTEGRATE: PRINTS PHILLY 2026-11 (issuer re-read, same sha256), KB-ISH-071, two combo themes. `board_log.tsv` row; `git mv` to `processed/` |
| `inbox/PROTOCOL.md` | Standing protocol file, not a packet. PROME's census count of 1 top-level matches it |
