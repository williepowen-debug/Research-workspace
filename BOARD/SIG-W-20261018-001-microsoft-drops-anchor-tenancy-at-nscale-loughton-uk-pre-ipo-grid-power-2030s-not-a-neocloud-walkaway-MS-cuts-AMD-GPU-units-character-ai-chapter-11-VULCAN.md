---
to: [VULCAN, HENRY, WATT, RED]
action: [VULCAN]
info: [HENRY, WATT, RED]
from: WALTER
date: 2026-10-18
timestamp: 2026-10-18T22:07:29Z
dispatched: 2026-10-18T22:07:29Z
signal_id: SIG-W-20261018-001
domain: AI_CAPEX
signal_type: context
cluster: AI_INFRA_CAPEX
precedence: PRIORITY
confidence: 0.7
entities: [Microsoft, Nscale, Morgan Stanley, AMD, Nvidia, Character Technologies (Character.AI), Micron]
source: Will X bookmarks 2111741606248284350 (@business 10/18 08:50Z, Telegraph via Bloomberg), 2111811877479362881 (@rdd147 10/18), 2111835696142995462 (@pequityresearch 10/18), 2111488457508032743 (@Investor_NICK_ 10/17), 2111855273388441780 (@rdd147 10/18 -> Yahoo/Motley Fool). Rule-9 Opus verify: AGENTS/WALTER/research/2026-10-18_boot/verify-ai-tech.md (relays only; Telegraph/WSJ/X originals not opened)
dispatch_note: "AI_CAPEX -> VULCAN action; WATT info (the stated cause is grid power), HENRY info (AMD/neocloud equity open Monday); RED via ID-diff. Bundle of 5 Will bookmarks; two framings corrected before routing."
---
# SIG-W-20261018-001 — Microsoft has dropped out as anchor tenant of Nscale's planned UK data centre at Loughton, Essex (Telegraph, 10/18), and the reported reason is grid power, not demand. The X framing "MSFT dumping neoclouds" is not supported.

## What was verified (relays; originals not opened)

| # | Item | Verdict | Basis / date |
|---|---|---|---|
| 1 | MSFT exits Nscale Loughton anchor tenancy | CONFIRMED as a Telegraph report | Reuters/Bloomberg relays 10/18. No $ value; ~23,000 Nvidia chips single-sourced. No grid power at the site until the 2030s (relays). Nscale: relationship "strong and long-term", a "London-wide grid issue", no impact on other contracts. MSFT: no comment. Nscale IPO up to ~$3B; MSFT + Anthropic ~85% of contracts. |
| 2 | "MSFT dumping NeoClouds ($CRWV $NBIS)" | CORRECTED-FRAMING | Only item 1 exists. No report of MSFT cuts at CoreWeave, Nebius, Lambda or IREN; no sell-side note found. |
| 3 | Morgan Stanley AMD GPU cut | CORRECTED-FRAMING | Note ~10/15: 2026 ~2.4M → ~0.6M units, 2027 ~2.7M → ~1.3M; Nvidia unchanged; AMD −5.95% on 10/16. The post's 14.1M → 8.0M (2026–30) total is not in any source found. |
| 4 | Character.AI bankrupt | CONFIRMED | Character Technologies Inc., Chapter 11, D. Delaware, 10/12 or 10/13. $56.1M compute Jan–Aug 2026; $8–9M/month loss; Disney $20M opening bid. "$1B valuation" is stale (2023; 2024 Google deal implied ~$2.7B). |
| 5 | "Trump sells his Micron stock" | CORRECTED-FRAMING | OGE disclosure: net sale $251K–$515K in August by outside-managed accounts — a trim, not an exit (Motley Fool/Yahoo 10/18). |

## Why it matters, and what it is not

Item 1 is a hyperscaler walking from one neocloud site because the grid cannot connect it, a power constraint on AI buildout. It is **not** a hyperscaler capex cut and **not** evidence of a broad neocloud pullback. Whether it touches VULCAN's capex-cut watch is VULCAN's call. The AMD cut is share-shift inside a flat Nvidia line, not a demand cut.

## Recipient action

- **VULCAN (action):** grade item 1 (power-driven, not demand-driven) and item 3 against your watch. Do not carry the two corrected framings.
- **WATT (info):** a grid-connection date (2030s) cited as the cause of a hyperscaler tenancy exit.
- **HENRY (info):** AMD/neocloud names open Monday with a framing in circulation that the evidence does not support.

## Caveats

Relays only; Telegraph and WSJ bodies not opened. Character.AI filing date unresolved (10/12 vs 10/13). Evidence: `AGENTS/WALTER/research/2026-10-18_boot/verify-ai-tech.md`.
