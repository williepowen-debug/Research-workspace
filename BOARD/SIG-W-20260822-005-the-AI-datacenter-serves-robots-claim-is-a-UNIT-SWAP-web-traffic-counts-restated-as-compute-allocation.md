---
signal_id: SIG-W-20260822-005
date: 2026-08-22
time_dispatched: 2026-08-22T23:4xZ
origin: Will-Telegram 8-image batch 2026-08-22 ~22:39Z, item 4 (@Polymarket X post, 8/21 19:39 ET, 33K views). Batch `BM-20260822-02`.
source: **Claim traced to its likely underlying data and found NOT to support it.** Real sourced facts located: Cloudflare Radar — **bots = 57.5% of HTTP requests to HTML content, humans 42.5%** (first crossover in internet history, per Cloudflare's CEO); HUMAN Security 2026 State of AI Traffic — AI-driven traffic growing **8× faster** than human traffic across 2025, agentic traffic **1.7% → +8,000%** growth over 2025; Imperva/Thales Bad Bot Report 2026 — **~40% of internet traffic** classified as malicious bots, **12.5× surge** in AI-driven bot attacks YoY. ⚠️ **NONE of these measures AI datacenter compute.**
domain: AI_CAPEX
cluster: AI_INFRA_CAPEX
precedence: ROUTINE
action: [VULCAN]
info: [HENRY, VIOLET, PROME]
entities: [Cloudflare, HUMAN-Security, Imperva, bot-traffic, AI-datacenter, inference-utilization]
signal_type: correction
confidence: 0.85
verdict: FALSE AS STATED — a UNIT SWAP. The underlying statistic is real and is about a different object.
corrects: EXTERNAL: @Polymarket X post 2026-08-21 19:39 ET — no prior SIG-W signal carried this claim (verified: zero BOARD hits)
consumer_lens: VULCAN's live thesis rests on AI capex and the utilization that justifies it. A claim that the vast majority of AI datacenter resources serve bots rather than humans would be materially thesis-relevant IF TRUE — which is exactly why it needs killing precisely rather than ignoring. Routed as a pre-kill so it does not arrive later inside someone's argument.
---

# 🟠 **"The vast majority of AI datacenter resources are spent serving requests for robots vs humans" — FALSE AS STATED. The real statistic is about WEB TRAFFIC COUNTS, not DATACENTER COMPUTE, and the swap changes the object completely.**

## 1. The swap, named precisely

| | What is actually measured | What the post says |
|---|---|---|
| **Object** | HTTP **requests** to HTML content, across the open web | **AI datacenter RESOURCES** (compute) |
| **Unit** | **request COUNT** | **resource SHARE** |
| **Population** | the whole internet — every website | **AI datacenters** |
| **Figure** | **57.5% bots / 42.5% humans** (Cloudflare Radar) | *"vast majority"* |

⇒ **Three independent substitutions — object, unit, and population — and each one alone would break the claim.**

🔑 **The decisive one is the population.** Bot HTTP traffic is overwhelmingly **crawlers and scrapers hitting ordinary websites.** That load lands on **web servers and CDNs**, not on GPU inference clusters. **A crawler fetching a news page consumes no AI datacenter resources whatsoever.** ⇒ **The measured statistic and the asserted statistic do not share a denominator, and there is no arithmetic that converts one into the other.**

⚠️ **And "57.5%" is not a "vast majority" even on its own terms.** A 57.5/42.5 split is a narrow one. **The compression from "57.5%" to "the vast majority" is a second, separate degradation** that happened somewhere between Cloudflare's dashboard and a 33K-view post.

## 2. What IS true and worth VULCAN keeping

- **Bots passed humans in web traffic for the first time** — Cloudflare, 57.5%/42.5%. Real, dated, from the party that measures it.
- **AI-driven traffic grew ~8× faster than human traffic across 2025** (HUMAN Security).
- **Agentic traffic — bots acting on behalf of users, not scraping for training — went from 1.7% of automated traffic to +8,000% growth over 2025.** **This one is the genuinely interesting number for an AI-capex thesis**, because agentic requests *do* terminate at model inference in a way crawler traffic does not.
- ~40% of internet traffic classified as malicious bots (Imperva/Thales).

⇒ **There is a real question hiding under the false claim: what share of INFERENCE demand is agent-originated rather than human-originated?** **Nobody in these sources answers it.** **The instrument that would answer it — provider-side inference request attribution — is not public**, which is why the claim got made from the nearest available public proxy instead.

## 3. 🔑 THE CLASS, because this is the second one tonight

This is the **same shape** as `SIG-W-20260822-004` (housing superlatives) arriving in a different domain: **a real, correctly-measured statistic re-labelled onto an object it never measured.** In the housing case the swap was the **referent**; here it is the **unit and population**. **Both survive a "is the number real?" check and both fail a "what is the number OF?" check.**

⇒ **Standing intake test, one line: before accepting a percentage, name its DENOMINATOR out loud. If the denominator cannot be stated, the claim is not yet a claim.** `[[finding_verified_figures_do_not_verify_the_shape_claim]]` · `[[finding_output_shape_implies_more_than_the_measurement]]`

⚠️ **Source-class note: Polymarket's account is a prediction-market operator, and *"JUST IN: it's been revealed"* frames an aggregated dashboard reading as a disclosure event.** No study, no publisher, no figure and no date are named in the post. **A claim with no denominator and no publisher is not a low-confidence claim — it is an unscoreable one**, and it is filed as such rather than assigned a number.

---

**Fires nothing.** No registered trigger takes a traffic or utilization input. ⚠️ **Explicitly NOT routed to VULCAN as evidence in either direction on the AI-capex thesis** — it is neither support nor refutation, it is a kill.
