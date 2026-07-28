# DEWEY → WILL · Entitlements: the S&P-first spec — **and it isn't a credit-card purchase**

**Date:** 2026-07-28 · **Closes:** PROME ruling `2026-07-25_from-PROME_entitlements-ruled-tier1.md` ("spec the exact product/tier/price for the S&P-first option and return a one-liner to Will")
**Rule #5 analog:** PROME rules the tier; only Will spends. Nothing bought, nothing committed.

---

## The one-liner

> **Buy nothing yet.** The correct S&P product is **RatingsXpress** (machine-readable ratings feed) if DEWEY is to consume it, or **Capital IQ Pro** (which now carries RatingsDirect content) if you want a human terminal — but **neither publishes a price, both are enterprise quote-only, and the credible third-party range is ~$12–30K per user per year.** That is 2–3 orders of magnitude above what "spec the price" implied, so it needs your decision on the *spend class*, not just the SKU.

## What I actually established

| Item | Finding | Source |
|---|---|---|
| **Public price for RatingsDirect** | **None exists.** Product page is a "contact us" form; no tier list, no per-seat rate | [S&P RatingsDirect](https://www.spglobal.com/market-intelligence/en/solutions/products/ratingsdirect) [PRIMARY-vendor] |
| **Public price for RatingsXpress** | **None exists.** Info-request form only | [S&P RatingsXpress](https://pages.marketintelligence.spglobal.com/RatingsXpress-Info-Request.html) [PRIMARY-vendor] |
| **Capital IQ Pro street price** | **~$12,000–30,000 per user per year**; Vendr procurement data across 55 verified purchases spans ~$14.8K–$215K/yr, median ~$53K/yr *(org-wide spend, not per seat)* | [CostBench](https://costbench.com/software/financial-data-terminals/sp-capital-iq/), [Vendr](https://www.vendr.com/marketplace/sandp-global) [INSTITUTIONAL — third-party procurement aggregators, not S&P] |
| **Which product for which job** | **RatingsXpress = feed/API** (programmatic, Xpressfeed, redistribution licensing). **RatingsDirect = desktop platform** (human, visualization). They are not interchangeable for our use | [S&P MI](https://www.spglobal.com/market-intelligence/en/solutions/products/ratingsdirect) [PRIMARY-vendor] |

**Confidence:** the *no-public-price* finding is HIGH (verified at the vendor's own pages). The **$12–30K range is MEDIUM and third-party** — S&P has not confirmed it and I could not reach a primary quote without entering a sales funnel in your name, which I did not do.

## 🟢 The finding that may matter more than the price

**S&P publishes rating actions and press releases FREE, at `spglobal.com/ratings/en/regulatory/`** — ratings actions, press releases, presale reports, annual reviews, behind a free registration.

**But it is machine-blocked.** I tested it two ways:
- `WebFetch` → **HTTP 403**
- Declared-User-Agent over `urllib` (the exact fix that solved the SEC EDGAR 403 and is logged DONE in my BACKLOG) → **HTTP 403 on both pages**

So this is a genuine **bot-block, not a UA problem** — the EDGAR precedent does not transfer. **A human browser gets it for $0; DEWEY cannot.**

**That reframes the purchase.** The entitlement is not buying *access to the rating action* — that's free to you. It is buying **machine access and timeliness**. Which makes the real question: how often is the blocker *"DEWEY couldn't fetch it"* versus *"nobody knew the action happened"*? Those have very different price tags, and the second one is already solved for free.

## What I'd recommend

1. **Cheapest real fix first ($0):** when a run hinges on an S&P action, DEWEY flags it and **you paste the page** — the same human-in-the-loop pattern as the broker screenshots TERRY already relies on. Test this for one cycle; it may close most of the recurrence.
2. **If that proves too slow**, get a **RatingsXpress quote** (the feed, not the terminal) — that is the product that actually fixes DEWEY's constraint. Quote-only, so it costs a sales conversation to learn the number.
3. **Do not buy Capital IQ Pro for this.** It is a human terminal at $12–30K/seat; it would not give DEWEY programmatic access, which is the actual gap.

**PROME's rider 2 already covers the review:** 60–90 days, graded off the `impact` column on `DEEP_RESEARCH_FLAGGED_LOG`. Option 1 costs nothing and generates exactly the evidence that review needs.

## Honest gap

I did not obtain a real quote for either S&P product, because doing so means submitting your contact details to an S&P sales funnel — outside what I should do unprompted. **If you want the actual number, that's a one-form action only you can take**, and I'd suggest asking specifically for **RatingsXpress, US corporates + financial institutions, single-user, no redistribution** — the narrowest scope that covers the fleet's use.

— DEWEY
