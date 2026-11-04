# CYPHER supplier-query recency comparison

**Captured:** 2026-11-04T22:29:30.911764+00:00. OpenAI Codex Rule 9 bounded verification helper `/root/verify_supplier_recency`; exact model unavailable. Root/local CLAUDE.md and root AGENTS.md explicitly consulted; root resolved to `/home/willi/Research-workspace`. Shell/Python/network and parent messaging available. No production write, owner launch, deployment, commit or external message. Parent retains recommendation/publication.

## Decision

Recommend PROME prefix **both existing supplier query strings with `when:7d `**, preserving their parenthesized entity and incident groups and all 51 adopted WATCH_FOR phrases. This is a bounded freshness improvement for the existing two daily queries, not proof that seven days is optimal or that incident recall is complete. No third query, scheduler, monitor, automatic old-item kill or phrase widening is proposed. Historical missed-day coverage must remain a separate bounded workflow; replacing routine queries cannot cover gaps longer than seven days.

## Exact comparison and evidence

Current config: `/home/willi/Research-Intake/scripts/newsweep_config.py`, rows labelled `bank-vendor-incidents-core` and `bank-vendor-incidents-msp`; `MAX_ARTICLES_PER_SOURCE = 15`. The live collector caps each query before seen filtering; therefore older first-ranked items occupy real collection slots. Production files were read only.

Existing `tools/watch_for_harness.py` run with `--desk CYPHER --current --since 2026-10-29 --show 3`: **51 phrases, 1,537 unique headlines across 7 lane days**. Output `supplier-harness-lane.txt`. Historical comparison `../2026-10-29_late-boot/watchfor-cypher-live.txt` used 56 proposed phrases; current adoption is 51, so counts are not directly comparable.

The harness CLI's `--live` helper always appends `when:<days>d` and discards publication dates. Running it as-is would contaminate the no-recency control and hide age. The bounded `supplier_compare.py` uses the **existing lane URL constructor, HTTP getter, RSS parser and real WATCH_FOR matcher**, without writing lane state; retrieves the four exact query variants concurrently and saves full RSS/XML and all dated results. No production harness change. This is one snapshot, not a replicated recall study.

| Query | Variant | RSS returned | First 15 or fewer | RSS-dated within 7 days | WATCH_FOR matched titles / phrase hits in capped set |
|---|---|---:|---:|---:|---:|
| Core | Current, no date operator | 41 | 15 | 0 / 15 | 5 / 5 |
| Core | Leading `when:7d` | 6 | 6 | 6 / 6 | 0 / 0 |
| MSP | Current, no date operator | 47 | 15 | 0 / 15 | 11 / 11 |
| MSP | Leading `when:7d` | 7 | 7 | 7 / 7 | 2 / 3 |

All **88** no-recency results, not just the capped 30, have RSS publication ages >7 days at capture; none provides a recent-title positive control for a retention test. Leading recency returns **13** unique titles within seven days. This demonstrates improved sampled publication freshness, **not 100% recent-event recall**. No recent result from the unbounded sample can be shown lost because that sample contains none; the retention denominator is zero.

Core current first15 ages span roughly 37.6–715.6 days, including Sharetec outage, August Fiserv/Jack Henry and 2024 Finastra breach reports. MSP current first15 ages span7.2–86.1 days, including October ConnectWise and August N-able/TruStage items. These may remain relevant history; age alone does not make them false or authorize killing them.

Leading core includes one bank-supplier incident follow-up **headline lead** (Jack Henry says cyber incident not financially material, scanx.trade, about1 day old); five other titles are earnings/ratings/product/settlement/commentary rather than clear incident-update headlines. Leading MSP includes ConnectWise security advice, a multi-event October roundup, an N-able product release and general cyber/China commentary. The 13 were screened at title/date level only: full bodies and event dates were not fetched, and no new fact was dispatched. A WATCH_FOR match is not an event confirmation. The Jack Henry lead is specifically **not** proof of non-materiality or a new incident; it needs normal primary/body validation if handled by the parent.

## Exact candidate strings

- `bank-vendor-incidents-core`: `when:7d ("Jack Henry" OR Fiserv OR Finastra OR Sharetec OR Corelation OR Alkami OR "Q2 Holdings" OR Candescent) (breach OR outage OR ransomware OR cyberattack)`
- `bank-vendor-incidents-msp`: `when:7d (ConnectWise OR "N-able" OR TruStage OR Fedwire) (breach OR outage OR ransomware OR cyberattack)`

## Limits and deployment handoff

- RSS publication time is not incident time. New publication can revisit old events; publisher bodies and source dates still require ordinary WALTER validation.
- Search ranking is volatile. Four fetches succeeded and parsed; no evidence establishes publisher completeness, Google index completeness, optimal lookback, or retained old-but-newly-relevant discoveries.
- Core recency yields zero adopted phrase hits even though a potentially relevant headline says “cyber incident”; phrase expansion is outside this test and is not proposed by stealth. Query results still carry CYPHER as their configured owner; matcher behavior remains unchanged.
- Do not carry the old 56-phrase test as a current adoption or recall result. Current 51-phrase adoption is a separate completed owner decision.
- Recommendation is ready for the parent/PROME deployment lane. Until PROME applies and verifies the exact two row changes, current production queries remain unchanged. Roll back the date prefix if a concrete material recent item is demonstrably suppressed by the bounded query while the prior form retrieves it; investigate the item/date/query cause rather than adding a new automatic monitor.

## Completion

STATUS: COMPLETE bounded comparison, recommendation only. CHANGED: local four RSS captures, results JSON, exact comparison script/text, existing harness output and this report. RESULT: current capped sample0/30 within7 days versus candidate13/13; four successful feeds. GAPS: event-date/body validation and real recall unproved. WILL_NEEDS: none for this bounded review. FOLLOW-UP: parent decides existing owner handoff; no further helper work or production action.
