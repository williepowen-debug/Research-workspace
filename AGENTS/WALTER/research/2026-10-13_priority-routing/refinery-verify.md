# Wood River catalytic-cracker verification — 2026-10-13

Checked: 2026-10-13T23:12:54Z. Role: thread-local WALTER verify-research helper; not BRENT or another domain owner. Runtime: OpenAI Codex; inherited model label unavailable. Repository root: `/home/willi/Research-workspace`; inherited cwd: `AGENTS/WALTER`. Root AGENTS.md/CLAUDE.md and local CLAUDE.md explicitly consulted; local AGENTS.md does not exist. Shell/web/task messaging are available. No fleet-presence inference, canonical edits, recipient edits, routing, paid access, outreach or Git operations were performed.

**Overall verdict: INDETERMINATE on the claimed operational event; CORRECTED-FRAMING on refinery-wide loss, diesel inference and ownership.** October 13 secondary reports exist and trace to a FirstSquawk item attributed to Reuters, but the original Reuters item or a faithful Reuters syndication could not be retrieved in this bounded public-web check. This retrieval gap is not evidence that the event did not happen. No event-specific operator confirmation was retrieved.

## Existing assessment reuse

Executed `rg -n --glob '*.md' --glob '*.tsv' 'Wood River'` only against `AGENTS/BRENT` and `BOARD`; no matches (exit 1). This is a scoped duplicate check, not a finding that BRENT lacks relevant refinery or diesel assessments elsewhere. Do not duplicate a broader refinery/diesel thesis from this result.

## Source chain and dates

| Source | Publication/event dates | What it actually supports | Limit |
|---|---|---|---|
| [AlphaPilot](https://www.alphapilot.tech/discover/phillips-66-s-wood-river-cracker-problem-a-small-earnings-dent-on-a-stock-that-has-doubled) | Updated 2026-10-13; exact publication time unavailable | Its indexed text reports catalytic-cracker trouble, recognizes 355,000 b/d as plant capacity, and says restart date and lost throughput are unspecified | Direct open failed; indexed text only. Its equity/earnings interpretation is not verified evidence of operational severity |
| [Reddit / MarketFluxHub](https://www.reddit.com/r/MarketFluxHub/comments/1x594nl/phillips_66_wood_river_refinery_in_roxana_hit_by/) | Dated 2026-10-13; exact post time not independently extracted | Repeats an operational-issues claim attributed to Reuters and links Market Flux | Repost of a summary, not independent corroboration |
| [Market Flux linked article](https://news.marketflux.io/news/phillips-66-wood-river-refinery-in-roxana-hit-by-catalytic-cracker-57d33f6715d66ae9e59bfaac08f4c907.html) | 2026-10-13 17:15 ET (21:15 UTC) | Its source list identifies FirstSquawk at 15:43 ET (19:43 UTC), with a headline attributed to Reuters sources, as the refinery-event source | Page explicitly describes itself as AI-generated clustered reporting. Other listed items concern stock momentum, investor attention and even Phillips Edison; they do not independently verify the refinery event. The event onset is not stated |
| [Newsquawk](https://www.newsquawk.com/headlines/phillips-66-psx-355000-bpd-refinery-in-roxana-illinois-having-issues-with-catalytic-cracker-unit-according-to-reports-citing-sources) | Page published 2026-10-13 20:03 UTC; page states feed time 19:43 UTC | Repeats a source-attributed catalytic-cracker issue at the 355,000-b/d Roxana refinery | Secondary headline. Same feed time as the FirstSquawk item is compatible with common provenance; independence is unproven. Context below the headline is editorial mechanism discussion, not an operator report |

The FirstSquawk link is exposed as source 4 in the Market Flux page, but the web click returned an inaccessible result. Reuters-domain, TradingView and MarketScreener searches did not retrieve the October 13 wire. Retrieved Reuters syndications about **2025** crude-unit issues and a **2025-03-20** planned turnaround are different events and were not substituted.

## Verified framing corrections

| Claim | Verdict and source basis | Implication for routing |
|---|---|---|
| A 355,000-b/d refinery is affected, therefore 355,000 b/d is lost | **CORRECTED-FRAMING.** All retrieved October 13 summaries refer to a catalytic-cracker issue. None measures refinery-wide shutdown or the volume removed. 355,000 b/d is their quoted plant capacity, not measured lost crude runs or product output | No numerical lost-throughput claim; no refinery-wide outage claim |
| This establishes a new diesel supply loss | **INDETERMINATE for this event.** Phillips 66's [2022-09-22 Wood River upgrade account](https://www.phillips66.com/newsroom/hydrocracker-upgrade-boosts-wood-river/) distinguishes the hydrocracker's middle-distillate production (diesel/jet/kerosene) from the FCC's gasoline-range yield. Its [current refinery profile](https://www.phillips66.com/refining/wood-river-refinery/) lists both processes; neither source reports today's unit status | A gasoline-oriented unit issue cannot be promoted to a quantified diesel disruption without actual product/run evidence. Diesel effects remain possible but unmeasured |
| WRB remains a 50/50 Phillips 66–Cenovus venture | **CORRECTED-FRAMING.** Phillips 66's [fourth-quarter 2025 earnings release, basis-of-presentation note](https://s22.q4cdn.com/128149789/files/doc_financials/2025/q4/Phillips-66-Fourth-Quarter-2025-Earnings-Release-FINAL.pdf) says its acquisition of the remaining 50% produces 100% consolidated Wood River/Borger results from **2025-10-01**. Operator document accessed 2026-10-13; financial period ended 2025-12-31 | Reddit/Market Flux ownership wording is stale and must not be carried forward |

## Unknowns that gate any change to existing conclusions

| Field | Verified status at check time |
|---|---|
| Original Reuters publication timestamp/byline/full wording | Unretrieved; the dated secondary feed supports report timing only |
| Event onset | Unknown; do not equate October 13 publication with onset |
| Specific FCC/unit number | Unknown |
| Actual shutdown versus operating issue/reduced operation | Unknown; do not replace “issues” with a confirmed shutdown |
| Duration, restart date, repair scope | Unknown |
| Lost crude throughput, gasoline output or diesel output | Unknown; no b/d estimate supported |
| Other units affected; refinery-wide operation | Unknown |
| Event-specific operator confirmation or regulatory filing | Not retrieved in this bounded check; not an absence finding |

**Change to existing conclusion:** none established for diesel supply or refinery-wide loss. The candidate adds a dated, source-attributed Midwest FCC-issue pointer with unresolved primary provenance and severity. WALTER retains the routing decision; BRENT retains any operational assessment. Safe candidate wording, if routed under WALTER's full workflow: “October 13 secondary feeds report a catalytic-cracker issue at Phillips 66's Wood River refinery, attributed through FirstSquawk to Reuters sources; original wire/operator confirmation and onset, duration, lost throughput and diesel impact remain unverified.”

## COMPLETION — WALTER verify helper — 2026-10-13
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/WALTER/research/2026-10-13_priority-routing/refinery-verify.md
RESULT: Traced 3 secondary surfaces to a source-attributed October 13 FCC report; corrected 355,000-b/d loss and 50/50 ownership framing with operator-source context.
GAPS: Original Reuters wire/full faithful syndication and event-specific operator status not retrievable in the bounded public-web search; onset, duration, lost throughput and diesel effects unresolved.
WILL_NEEDS: None.
FOLLOW-UP: Parent WALTER decides disposition and persistence; retain unknowns if routed and refresh upon original wire or operator evidence.
