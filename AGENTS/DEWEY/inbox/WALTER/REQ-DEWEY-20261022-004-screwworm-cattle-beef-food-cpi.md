---
request_id: REQ-DEWEY-20261022-004
from: WALTER (discovery under Will's standing direction in the WALTER terminal, 2026-10-22 12:01 ET: "discovering valuable/significant research tasks/threads and assigning them to DEWEY")
to: DEWEY
created: 2026-10-22 (UTC stamp in the commit)
state: NEW
flag_trigger: T1 new coverage channel (no fleet desk owns livestock disease or beef supply) + T2 cross-channel (animal disease to beef prices to food CPI, a path not mapped)
originating_evidence: SIG-W-20261022-010 (USDA confirmed 10/21 the first New World screwworm case in US wildlife, an elk in Pecos County, Texas; Reuters reports a New Mexico beef cow case; the outbreak began with a Zavala County calf in early June)
clusters: INFLATION_TRANSMISSION (secondary CONSUMER_STAGFLATION)
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv row REQ-DEWEY-20261022-004
kill_condition: At intake, confirm at USDA APHIS that the wildlife case and the New Mexico case are real and dated October 2026. If either is not, report the correction to WALTER first and run leg 1 only. Stop the price legs if USDA declares the Texas and New Mexico detections eradicated before the run.
deliver_by: no hard date; useful before the October CPI release in mid-November
---

# DEEP-RESEARCH REQUEST — New World screwworm in the US: how much could it move cattle supply, beef prices and food inflation?

**Why now:** screwworm is now confirmed in US wildlife, which is much harder to contain than a single herd. The fleet has no desk for livestock or beef, so a supply shock here would reach food CPI with nobody watching. Beef prices were already a known pressure point in 2025–26 because the US cattle herd was at multi-decade lows.

**Decision question:** if screwworm becomes established in Texas and New Mexico wildlife, what is the realistic effect on US cattle supply and retail beef prices over 6 to 18 months, and how much could that add to food-at-home and headline CPI?

**What changes with the answer:** CARL (consumer and food inflation) and RED (inflation triggers) learn whether this is a rounding error or a real food-inflation leg worth a watch row. If it is material, a new routing lane is needed (a T1 coverage gap WALTER would raise with PROME). If it is small, WALTER routes future screwworm items as context only.

## Scope (in bounds)

1. **Facts first, primary sources.** USDA APHIS and Texas Animal Health Commission statements: case count, locations, dates, the infested-zone boundaries, sterile-fly supply and dispersal capacity (US and Panama/Mexico plants, any new US facility and its start date), and the status of Mexican cattle import suspensions. Check the "Florida deer outbreak last year" line in SIG-010: the known Florida Keys deer outbreak was 2016–17, so confirm which event is meant and its date.
2. **History.** The US eradication campaign (1950s–1966 Southeast, Southwest to 1982) and the 2016–17 Florida Keys outbreak: duration, cost, livestock losses, and what made containment work or fail.
3. **Supply channel.** US cattle inventory (USDA NASS January and July reports), the role of Mexican feeder-cattle imports (head per year, share of feedlot placements) and what the suspension has already cost; treatment, inspection and movement-restriction costs for Texas ranchers; any effect on cattle futures (live and feeder) since June, with dates.
4. **Price channel.** Retail beef prices (BLS CPI beef and veal, USDA ERS), beef's weight in CPI food at home and in headline CPI, and pass-through estimates from past supply shocks. Give a range of CPI effects with assumptions, not a point estimate.
5. **Scenarios.** Contained by spring (best case), regional establishment in Texas and New Mexico, wider spread north. For each: duration, cattle loss or slaughter delay, and the CPI range.
6. **Counter-evidence, required.** Reasons the impact may be small: sterile-fly success, wildlife cases that did not spread, beef demand shifting to other proteins, imports from other countries.

## Out of bounds

Trade ideas or position sizing (TERRY); animal-health advice; grading any desk's thesis.

## Deliverable

Tables over prose, every cell sourced and dated: (1) a verified case and policy timeline; (2) historical outbreak table; (3) cattle supply and import figures; (4) price and CPI-weight table with pass-through ranges; (5) scenario table; (6) counter-evidence; (7) explicit UNKNOWNs, and a one-line view on whether this deserves a routing lane and which desk should own it.

**On return:** archive to AGENTS/DEWEY/output/, then hand back via a create-only handoff in AGENTS/WALTER/inbox/DEWEY/ naming REQ-DEWEY-20261022-004. WALTER routes it as a research-output signal: CARL action; FERT, AEOLUS, RED and PROME info.
