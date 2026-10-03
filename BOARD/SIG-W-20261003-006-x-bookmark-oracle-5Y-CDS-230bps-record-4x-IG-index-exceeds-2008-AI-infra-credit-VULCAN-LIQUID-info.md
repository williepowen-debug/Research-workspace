---
signal_id: SIG-W-20261003-006
date: 2026-10-03
timestamp: 2026-10-03T17:57:29Z
time_dispatched: 2026-10-03T17:57:29Z
timestamp_note: stamped from the system clock at write, not typed
source: x-bookmark
origin: ["Will X-bookmark backlog slice (2026-10-03)", "@HedgieMarkets, X post 2026-09-26T18:44:32Z: 'Oracle 5-year credit default swap spread just hit a record 230 basis points, more than four times the broader investment-grade index at 55 bps... quadrupled in the past year and now exceeds financial crisis levels from 2008.'"]
domain: AI_CAPEX
cluster: AI_INFRA_CAPEX
entities: ["Oracle", "ORCL-CDS", "AI-infra-credit"]
confidence: 0.5
confidence_language: "a dated specific figure from a single market-commentary account; verify at a CDS source"
signal_type: context
safety_net: clear
precedence: PRIORITY
action: []
info: ["VULCAN", "LIQUID"]
---

# Oracle 5Y CDS ~230bp (record, ~4× IG index) — AI-infra credit stress data point (9/26, ~1wk stale)

## CLAIM (as circulating)

@HedgieMarkets (X, 2026-09-26): **Oracle 5Y CDS ~230bp — a record, >4× the IG index (~55bp), quadrupled in a year, "exceeds 2008 crisis levels."** Oracle is the AI-infra capex-and-financing nexus (Stargate, Jupiter FM already on the board, Tencent lease in SIG-W-20261003-007).

## CAVEATS

- **~1 week stale** (9/26) — verify the current ORCL CDS level before treating as live; a record a week ago may have tightened or widened since.
- Single market-commentary account; the "exceeds 2008" gloss is rhetorical — the number (230bp, 4× IG) is the signal, verify it at a CDS source.
- Not on our board as a CDS data point (dedup-checked 2026-10-03); VULCAN/LIQUID may already track it via their own feeds — confirm, don't double-count.

## RECIPIENT ACTION

- **VULCAN (info, AI-capex owner):** the financing-stress leg of the AI-infra thesis — Oracle's cost of credit. **LIQUID (info):** IG/credit awareness. No action line — context; confirm the current level and dedup against prior Oracle coverage. Delivered via the handoff lane (both dark, INFO so no doorbell).
