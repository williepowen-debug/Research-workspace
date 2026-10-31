# Settlement and energy-OAS repair verification

Checked 2026-10-31 ~15:50 ET. **Partial repair: public CME preliminary settlement rows recovered; ICE Endex contract calendar recovered. Official ICE Brent/TTF settlements and a live energy-HY OAS feed remain unverified.** No owner grade or boundary count changed.

## Scope and runtime

Bounded WALTER Rule 9 helper. Actual runtime: Codex/OpenAI, inherited GPT-6 family; exact model ID unavailable. Actual cwd `/home/willi/Research-workspace/AGENTS/WALTER`; repository root `/home/willi/Research-workspace`. Root `CLAUDE.md`, root/user-supplied `AGENTS.md`, `USER.md`, WALTER `CLAUDE.md`, and relevant `PROME/COMPLETION_SPEC.md` / `ORCHESTRATION_PLAYBOOK.md` runtime sections explicitly consulted. Shell and web verification tools available; no native fleet-wide active-agent discovery. Owner/status/ruling evidence was read before public-source verification. No owner files, grades, dispatches, accounts, installed tools or Git commits changed. One-off evidence-capture script removed after running; JSON evidence remains here.

## CME: actionable recovery, preliminary bulletin only

The public [CME Daily Bulletin index](https://www.cmegroup.com/market-data/daily-bulletin.html) links its [Energy Futures Products PG61 PDF](https://www.cmegroup.com/daily_bulletin/current/Section61_Energy_Futures_Products.pdf). Web extraction succeeded: **bulletin 210, Friday October 30, 2026, PRELIMINARY**. Physical pages 1–2 clearly label the `SETT. PRICE` column. These are exchange-published preliminary settlements, not Yahoo last prices.

| Named delivery | CL, $/bbl | RB, $/gal | HO, $/gal | RB×42−CL, $/bbl | HO×42−CL, $/bbl |
|---|---:|---:|---:|---:|---:|
| December 2026 | 104.12 | 3.1565 | 4.6761 | 28.4530 | 92.2762 |
| January 2027 | 102.21 | 3.0976 | 4.5818 | 27.8892 | 90.2256 |

Arithmetic is helper calculation; no trade or boundary grade is implied. December is the front common CL/RB month for the October 30 gasoline comparison. The January observation is also **October 30 trade-date data**, not a future November 2 settlement. BRENT's held-VLO December crack is $2.1162 above $90.16 using this preliminary exchange basis; January is a different instrument and must not grade that trade.

The PDF also lists **NYMEX BZ Oil Last Day Futures** December 117.64 / January 113.43 on physical page 3. These are not a directly retrieved ICE Futures Europe settlement and must not silently replace that governing leg. Markers on page 46 are another distinct basis.

**Repair:** make the public bulletin an explicit available retrieval path and send BRENT the dated preliminary rows. Recheck the final bulletin before recording final-certification language. The index describes final publication at approximately 10:00 CT next business day. The mutable `/current/` URL requires saving the actual dated bulletin when accessible. A local direct PDF capture timed out; the web tool's extracted rows were accessible. This does **not** prove the prior box/IP block is removed. No IP/proxy change or unblock attempt occurred.

## ICE: calendar fixed, settlements still missing

Direct [Brent data](https://www.ice.com/products/219/Brent-Crude-Futures/data) and [Dutch TTF data](https://www.ice.com/products/27996665/Dutch-TTF-Natural-Gas-Futures/data) returned page shells without settlement rows. Public [ICE Europe futures report 10](https://www.ice.com/report/10) and [ICE Endex futures report 159](https://www.ice.com/report/159), linked by the Report Center, also yielded only the report shell. ICE advertises subscription EOD CSV packages; no subscription or account was requested.

A [TTF data query page](https://www.ice.com/products/27996665/Dutch-TTF-Natural-Gas-Futures/data?marketId=6277389&span=2) exposed Dec26 **103.505** / Jan27 **103.060** at October 30 20:59 GMT under **Last**. Those are official-exchange displayed trade values, **not certified settlements**, and cannot settle HANS's October 28 disagreement or sustain an official-settlement test.

The governing [ICE Endex Dutch TTF expiry page](https://www.ice.com/products/27996665/Dutch-TTF-Natural-Gas-Futures/expiry) is readable and gives:

| Delivery | Last trading date | Final settlement date |
|---|---|---|
| Dec26 | 2026-11-27 | 2026-11-30 |
| Jan27 | 2026-12-30 | 2026-12-31 |

**Repair:** forward these exact primary-calendar dates to HANS for its Z26/F27 calendar debt. Do not infer T07 exit, settlement, or winter-curve state. The page's CSV link was unsupported by web extraction and direct local retrieval returned HTTP403; page table itself was available.

WALTER boundary 8 still requires the official ICE Brent leg and three consecutive same-month official-settlement sessions. Its ruled month basis remains December through October 30; January from November 2, with count restarted at zero. No absent official settlement can increment or reset the old count. This pass recovered only October 30 CME rows, not a three-session chain.

## WQ-533 is not a boundary substitution authority

`AGENTS/BRENT/RULINGS.md` R-2026-10-29-WQ-533(b), corroborated in `TRADE.md`, accepts WQ-420 sources (2)/(3) for BRENT's crack basis while CME blocks the box, with no unblock attempt. Near the held-VLO December $90.16 boundary (roughly $1–2), vendor-vintage uncertainty requires NOT MEASURABLE; BRENT may ask Will for his device's CME reading. That narrow owner ruling does not authorize substituting vendor rows into WALTER #8's official-settlement persistence count or replacing ICE with NYMEX BZ. Recovered public CME observations should be handed to the owner with their preliminary status.

## Energy HY OAS: bad identifier diagnosed; feed not mapped

Using the existing authenticated FORGE FRED helper, metadata for `BAMLH0A0E2Y` again returns **HTTP400: series does not exist**. Same-session positive control `BAMLH0A0HYM2` returns valid broad-US-HY OAS metadata in percent, proving this is not simply missing credentials or a general FRED outage. This repeats the earlier definitive owner finding in `BRENT/research/2026-09-08_batch2/REPORT.md`; it should no longer be described as an unexplained fetch error.

Two authenticated [FRED series-search](https://fred.stlouisfed.org/docs/api/fred/series_search.html) queries, `ICE BofA Energy` and `high yield energy`, each return zero matches. Exact responses and request parameters without credentials are retained in `fred-energy-mapping-probes.json`. This bounded search does not prove no licensed energy index exists.

Primary [ICE-hosted index methodology, August 10, 2017](https://www.ice.com/publicdocs/BoA_Change_Reference_Data_Source.pdf), physical page 4, identifies **US High Yield Energy Index: H0EN**. This establishes historical index identity, not a current FRED symbol, OAS field mapping, entitlement, current methodology or October 2026 observations. Broad HY OAS is not an energy-sector substitute.

**Repair now:** classify `BAMLH0A0E2Y` as INVALID SERIES / NO VERIFIED ENERGY-OAS FEED in current WALTER evidence and stop treating repeated HTTP400 as a transient problem. **Still required:** owner-approved current energy-HY index identity plus accessible dated OAS observations, explicit units (400 bp = 4.00% if supplied as percent), and 2–3 sessions for boundary 4. H0EN is a vendor-identification lead only; no replacement series installed and no boundary re-registration inferred.

## Evidence retained and limits

- `fred-energy-mapping-probes.json`: four authenticated, sanitized FRED responses.
- `settlement-access.json`: exact local PDF timeout and CSV403 outcomes; neither a PDF nor CSV was successfully saved.
- `settlement-extracted-rows.json`: manually transcribed web-extracted CME rows and ICE expiry dates with source URLs and version labels.

No final CME bulletin, official ICE Brent settlement, official TTF settlement or operational energy-HY OAS feed was recovered. These remaining gaps are specific access/instrument gaps; retries or broad-HY/last-price substitutions do not close them.
