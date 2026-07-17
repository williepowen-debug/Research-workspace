---
name: finding-discovery-tool-wrong-slice-false-zero
description: "A search/discovery tool that silently scans the wrong or partial slice returns 'zero results' that is FALSE — the gap is manufactured by the query, not the data. Before banking a 'no market/record/file exists' conclusion, verify the tool's own coverage against an authoritative enumeration (ORACLE/Kalshi search vs /series+/events, 2026-07-17)."
metadata:
  node_type: memory
  type: finding
  originSessionId: 5f02d11a-4227-4f02-8208-c79eb27ae831
---

**The pattern:** ORACLE's 2026-07-09 "comprehensive Kalshi sweep — 14 keyword queries, ZERO open events across the whole structural-credit axis" was logged as a genuine data-gap and propagated into STATUS/NEXUS_BRIEF as "structural credit is genuinely un-priced by real money." On 2026-07-17 re-check, the conclusion was **partly false**. Root cause: the `kalshi.py search` command scans `/markets?status=open&limit=1000` (~6 pages) — a slice **dominated by sports/entertainment** — and does crude substring matching. So `search "recession"`, `"oil"`, `"crude"`, `"inflation"` all returned **0 open markets** for markets that demonstrably exist and pull fine by ticker every session; `search "Fed"` returned 19 hits, **all sports multigame tickers** with `FED` inside the ticker code. The authoritative path — `/series?category=X` then `/events?series_ticker=X&status=open` — found several credit-stress + oil-settle markets open and liquid (US-credit-rating-downgrade, $67.6K vol; a Brent settle-reference ladder; Iran crude-production).

**Why it's dangerous:** the gap *felt* thoroughly verified — 14 queries is a lot of queries — and thoroughness is exactly what made the false wall credible enough to enter canon. But **running a broken query N times is still one broken query.** The failure is not in the data and not in effort; it is in the mismatch between what the tool *appears* to search (all open markets) and what it *actually* searches (a non-representative slice). A tool that silently under-scans reports absence indistinguishably from real absence.

**How to catch it — before banking any "X does not exist" from a discovery/search/grep tool:**
1. **Positive control.** Query the tool for something you KNOW exists (a market/record already in your watchlist). If it returns zero, the tool's coverage is broken, not the data — stop and find the authoritative enumeration. (`search "recession"` → 0, while `pull` fetched recession fine → instant tell.)
2. **Inspect a hit, not just the count.** `search "Fed"` returning 19 *sports* rows exposed the wrong-slice scan; the count alone (19 > 0) would have looked healthy.
3. **Prefer an authoritative enumeration over a search index.** Registries/`/series`+`/events`/`ls`+manifest enumerate the true population; a search endpoint returns whatever slice it indexed. When they disagree, the enumeration wins.
4. **A declared gap is a claim requiring verification, same as a figure** — and "I verified it thoroughly" is not evidence when the verification tool itself was never coverage-checked. [[finding_declared_data_wall_needs_fleet_memory_check]]

**The honest-scope discipline:** the correction did NOT erase the gap — the *specific* series I originally cared about (CRE-default, CC-delinquency, mortgage-default, Fed-facility) really were still zero-open on the authoritative check. The overstatement was the *broad* "credit is un-priced," not the *narrow* series gap. Correcting a false-wide claim does not license asserting its inverse. [[finding_refuted_claim_citation_vs_fact_failure]]

**Related:** [[finding_declared_data_wall_needs_fleet_memory_check]] (sibling — that one is a *cross-system* door existing elsewhere; this one is the *same* tool's scan silently partial) · [[finding_fail_loud_on_incomplete_data]] (the tool should have failed loud on a capped scan, not returned a clean 0) · [[finding_verify_runtime_context_before_tool_broken]] · [[finding_comprehensive_grep_over_sampling]] (comprehensive only counts if the surface scanned is the right one)
