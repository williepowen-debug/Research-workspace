# Proposal: an industrials / manufacturing-cycle desk (v2)

WALTER, 2026-10-23, at Will's request ("I think we need a domain with coverage for industrials/manufacturing"). v2 applies DAEDALUS's review (`AGENTS/DAEDALUS/design/2026-10-23_INDUSTRIALS_DESK_PROPOSAL_REVIEW.md`, 09:28 ET): fixes 1-4, the smaller seams, the data-limits line and the tier recommendation. Each DAEDALUS citation was checked at the file before adoption. Will sends this to PROME; DAEDALUS re-reads it first.

## The question

**Is the US manufacturing upturn real end-demand, or tariff front-running plus AI/defence capex and inventory rebuild, and when does it roll over?**

Where the answer transmits: C&I lending → REGINALD / GIBBS · industrial earnings → HENRY · factory hiring → LABOR · power demand → WATT.

## The ask

Build a new domain desk that owns that question, the same way CYPHER was built on 10/22: Will names it and sets the scope, DAEDALUS builds it, PROME adds it to the ROSTER, and WALTER mints the domain code and routing row on Will's sign-off.

**Tier (DAEDALUS recommendation):** Tier-2, woken by dated DOCKET rows on the monthly print calendar (CRUISE / GIBBS precedent).

## Why: nobody owns the industrial cycle as a question

- No desk's CLAUDE.md claims industrials, capital goods, industrial production, durable goods, freight volumes or industrial companies (grep of `AGENTS/*/CLAUDE.md`, 10/23).
- The data prints are claimed several times over. Each claimant reads them for its own purpose, and none reads them as the cycle: CARL (routing row MACRO_INFLATION, `ROUTING_TABLE.md:58`), HENRY (`AGENTS/HENRY/CLAUDE.md:4`, "Owns ISM, PPI, PCE"), LABOR (ISM employment).
- Supporting evidence, weighted as such: September's S&P Global flash manufacturing PMI (57.0, strongest since May 2022) and September's ISM manufacturing report never became BOARD signals. Both sat on the MACRO_INFLATION row with CARL as action desk, so this is **partly a WALTER routing miss**, not proof of the gap by itself.
- Kill log: 5 manufacturing-class items killed since 8/1. This is a keyword count, not an audit of each kill.
- Correction on record: WALTER's August "zero ISM coverage" claim (SIG-W-20260813-001) was wrong; CARL refuted it.

## Proposed scope

1. **Surveys:** S&P Global flash and final US PMIs; ISM manufacturing (new orders, production, inventories, prices); regional Fed surveys (Philadelphia, Empire, Richmond, Kansas City, Dallas).
2. **Hard data:** industrial production and capacity utilization; durable goods and core capital-goods orders and shipments; factory orders.
3. **Freight and transport volumes, excluding tankers:** Cass Freight Index, rail carloads, trucking and Class 8 orders, air cargo.
4. **Industrial bellwether earnings and guidance:** e.g. Caterpillar, Deere, Honeywell, Eaton, GE Aerospace, Parker-Hannifin, 3M, Emerson, Union Pacific.
5. **Tariff and reshoring effects on manufacturers:** input costs, margins, and the timing of capex announcements.

## Ownership of the ISM/PMI prints (a route change, so Will's call via PROME)

ISM already has two claimants: CARL action on `ROUTING_TABLE.md:58`, with HENRY as backup, and HENRY's own "Owns ISM" line. Proposed split:

| Read of the same print | Owner |
|---|---|
| Manufacturing-cycle read of ISM / PMI (the one headline figure) | **New desk** |
| Equity positioning read (vol stays VIOLET's) | **HENRY** |
| Prices-paid and the consumer / inflation side | **CARL** |
| Employment sub-index as a labor input | **LABOR** |

**HENRY's `ISM Mfg <47 → LABOR, PROME` trigger** (`AGENTS/HENRY/CLAUDE.md`, trigger table): name its owner after the move. WALTER's recommendation is that it moves to the new desk with HENRY on info, but this is Will's call.

## Inbound edge: HANS → new desk

HANS's charter (`AGENTS/HANS/CLAUDE.md`, § PMI → ISM lead) holds that German manufacturing PMI leads US ISM by about 2 months (directional r = +0.573 DE→US at 6 months vs +0.185 US→DE; HANS says the exact lag is not identifiable). HANS also carries a standing caveat: German PMI strength is driven by **defence spending, data-centre construction and inventory rebuild**, confirmed verbatim at S&P. That caveat is the question above, one ocean over.

**Open, unchecked by WALTER or DAEDALUS:** does the same caveat apply to the US September flash at 57.0? First task for the new desk.

## Boundaries and seams

| Desk | Keeps / seam |
|---|---|
| VULCAN | AI capex, data centers, semis |
| WATT | Grid and power equipment demand. **Eaton and GE Vernova sit on this seam; name one figure owner.** GE Aerospace is a separate company and is the new desk's |
| MIDAS | Metals |
| CARL | Consumer and inflation read of the prints (one figure, shared); TARIFF_TRADE announcements stay CARL's, the new desk owns the effect on manufacturers. **Trucking and rail volumes are shared with CARL's goods read** |
| FERT / CARL | **Deere's farm-income side** |
| HAWK (dormant book) | **Defence spending** and the **US–China trade war** are listed in HAWK's dormant book (`AGENTS/HAWK/CLAUDE.md:3,181`). Settle which of defence capex and the tariff effect moves |
| LABOR | ISM employment as a labor input |
| HANS | Europe; inbound edge above |
| ZHAO | China PMIs |

## Data limits

- Hard data (IP, capacity utilization, durables, core capex orders, factory orders) should be free via FRED. **Not fetch-tested.**
- ISM history is paywalled (off FRED since 2016) and S&P Global's full PMI dataset is paid, so **the desk cannot back-test survey thresholds on free data.**
- Class 8 orders are available only as press-release headlines.

## Interim until it is built

US PMI and ISM prints keep routing to CARL to act, with HENRY for information. WALTER notes the coverage gap on each such dispatch. Today's example: the October flash PMIs at 9:45 ET (forecast manufacturing 55.4 vs 55.9 prior; services 57.9 vs 58.8 prior).
