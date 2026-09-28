# Source check: junk-bond pulled/postponed/flexed deals + issuance volume (Will: "Lets do the source check" → pulled deals, item 6)

**Written:** 2026-09-28 19:03 ET by BOND · follows item 6 of `analysis/2026-09-28_coverage-gap-review.md` · **KB:** `KB-BND-358` · no build, no spend, no sign-up done.

## Verdict
**No free source gives a complete pulled-deal list.** The gap can be narrowed from "none" to **"partial and secondhand"** with two free routes. A complete list still needs a paid tracker (LCD/Debtwire/IFR), which is Will's call.

| Source | Reachable? | What it gives | Limit |
|---|---|---|---|
| **SEC EDGAR full-text search** (8-K launch press releases → a later **item 2.03** 8-K = deal closed) | ✅ free, primary, API | a **launch-without-close** candidate list for SEC-registrant issuers | **thin coverage:** 7 launch 8-Ks found 8/25–9/18 in a month of ~$38B HY. Most 144A issuers (sponsor-owned) never file. Rating tier not in the filing (IG/HY/converts mixed; converts excludable by text). Text matching on "pricing" missed Ellington (9/14) — **resolve on the structured item 2.03, not on text** |
| **Free credit newsletters** (DebtSerious "Weekender", junkbondinvestor) | ✅ free | secondhand pulled-deal mentions: the 9/26 Weekender names **Blackstone shelving a $3B collateralized fund obligation despite a 12% yield** and **cancelled European real-estate junk deals** (both via Bloomberg) | secondhand, selective, weekly; a news-intake job, i.e. **WALTER's lane**, not a BOND build |
| **SIFMA US corporate issuance statistics** (monthly; IG/HY split) | ⚠️ page reachable; **download gated by a sign-up form** (HubSpot) | monthly HY issuance totals (resolves "busiest month" questions after the fact) | through **August** only (≈1-month lag); needs contact details submitted → **Will's call**, not done |
| **FINRA API** (TRACE) | ❌ HTTP 401: needs an authenticated account | — | registration needed → **Will's call**; free-tier contents NOT verified |
| **PitchBook LCD weekly HY wrap** | ❌ Cloudflare bot challenge (fetch tool and curl both 403) | weekly volume + pulled/flexed commentary (the paid tracker's public teaser) | not reachable from this box's tools; a browser read was not tried |
| Bloomberg / Reuters wires | ❌ paywalled or 403 (as on 9/28) | — | WALTER reads wire bodies via syndication; route through WALTER |

**Side note on volume (another vintage):** a search summary quotes **Goldman at $38.5B** for September HY, on top of $37.8B (newsletter, ~9/25) and $38.51B (Bloomberg 9/28) (`KB-BND-352`). All three are consistent with a tie with April; still undecidable.

## Recommendation (for Will; nothing built)
1. **Cheapest real improvement: route it, don't build it.** Ask WALTER/PROME for a lane query on pulled-deal language (e.g. "pulls bond deal", "postpones notes offering", "shelved debt sale", "flexed wider"), routed to BOND/LIQUID/BROCK. Same pattern as the `treasury-moves` query that landed tonight.
2. **Optional BOND build (about half a session):** an EDGAR launch→item-2.03 monitor. Primary and free, but it only covers public issuers. Worth it only as a second, independent leg.
3. **Needs your word:** SIFMA sign-up (monthly totals), FINRA account (coverage unverified), or a paid tracker (the only complete list).

**Row 4's pulled-deal trigger stays unfireable on evidence until one of these lands.** The GAP label on `KB-BND-346` stands, now with a documented reason. Ownership: private-credit CFOs are BROCK's; EU real estate is HANS/LIQUID's.
