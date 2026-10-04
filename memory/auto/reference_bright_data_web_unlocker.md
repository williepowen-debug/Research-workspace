---
name: reference_bright_data_web_unlocker
description: Bright Data Web Unlocker (free tier) — the fleet's bot-wall bypass; WALTER-only scope, key per-machine, budget unreadable by API
metadata:
  type: reference
symptoms: "WebFetch 403 on a primary source" · "curl blocked by Cloudflare" · "bdata budget returns 403" · "can another desk use Bright Data"
---

Bright Data Web Unlocker = the fleet's bot-wall bypass, LIVE since 2026-10-04 (WQ-383, Will: "Okay we can check it out").

- **Scope:** FREE tier only (5,000 requests/month, no card, hard stop at the limit, resets the 1st). Approved for WALTER's bookmark links that are bot-walled and have no screenshot. Paid structured tools (X posts, Zillow, …) are NOT approved; that would be a separate ask. Another desk that needs a blocked page asks WALTER (e.g., FALCON's UKMTO 150-26 case, 2026-10-04).
- **Where:** key `BRIGHTDATA_API_KEY` in `AGENTS/WALTER/.env` (gitignored, so it does NOT travel by git). Each machine also needs its own `bdata login --api-key <key>` (Node ≥20; it creates zones `cli_unlocker`/`cli_browser`). Inventory: `PROME/MACHINE_LOCAL.md` (present on `WilliePOwen` = laptop; desktop pending Will's install). Usage log: `AGENTS/WALTER/registry/brightdata_usage.tsv`.
- **Gotcha 1:** the key lacks account-read permission, so `bdata budget` returns 403. The request counter shows only in the Bright Data web UI.
- **Gotcha 2:** reaching a page is not getting its content. On 10/4 it reached ukmto.org past the 403, but `/recent-incidents` rendered "0 reports" in a 1,079 B scrape. A script-loaded feed that never rendered means NOT OBTAINED, never "absent" (`[[finding_negative_reachability_is_a_claim_about_your_request]]`).
- Usage ladder: WALTER design `AGENTS/WALTER/design/X_BOOKMARKS_ACCEPTANCE.md` §9a (Bright Data is the LAST rung, after image, X-native and WebFetch).
