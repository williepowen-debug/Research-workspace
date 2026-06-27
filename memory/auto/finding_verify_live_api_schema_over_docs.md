---
name: finding_verify_live_api_schema_over_docs
description: "wiring a new external API: verify base URL / auth / response field names against a LIVE call before building the parse layer — aggregator docs and model priors go stale; build the field map from the wire"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 89b1ddd3-1f8e-45a5-8f53-0546435a41f6
---

When integrating a new external API, the doc summary (or your prior) is a hypothesis, not ground truth. Confirm three things against a real response before writing the normalizer: the **base URL**, the **auth/signing scheme** (on a known endpoint), and the exact **response field names + where the data lives**.

ORACLE 2026-06-27 wiring Kalshi — three errors caught ONLY by hitting the live API, each of which silently produced all-zero/None data that first looked like "illiquid markets":
1. **Base URL stale:** `trading-api.kalshi.com` → 401 "API has been moved"; correct host is `api.elections.kalshi.com`. (Probed both in the test harness, didn't assume.)
2. **Field names renamed:** docs/priors said `last_price` / `volume` / `yes_bid`; the live API returns `last_price_dollars` (0-1) / `volume_fp` / `yes_bid_dollars` / `open_interest_fp` / `previous_price_dollars`. Reading the old names returned None for everything.
3. **Data location:** nested markets inside `/events` are lightweight (price fields null); the live quote is only on `/markets?event_ticker=`. Same field, different endpoint.

The tell that something is a *reader* bug, not "the markets are dead": **4000 markets all showing volume=0 is implausible** — dump the raw response keys and a known-liquid record before concluding illiquidity.

**How to apply:** before building a fetcher's parse layer, make ONE live call and print `sorted(obj.keys())` + a full sample of a known-active record; map fields from the wire. Confirm auth on a trivial endpoint (status) AND an authed one (balance) so a bad signature fails loudly up front. Sibling of [[finding_verify_reader_before_source]] (a "tool broken" verdict can be a reader bug) and [[feedback_suspect_fresh_pull_over_curated_record]].
