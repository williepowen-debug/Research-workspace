# WARN Act as Leading Indicator (2023-2026)
**Source:** Gemini Deep Research, Feb 2026

## Core Finding
WARN filings lead Initial Jobless Claims by **4-8 weeks** (peak correlation r=0.78 at τ=6 weeks). The "Alpha Window" — gap between WARN filing and public announcement — averages **7.2 days** for mega-layoffs (>1,000).

## The Alpha Window (Filing → Public)
| Company | Layoff Size | Alpha Window |
|---------|------------|-------------|
| UPS | 30,000 | **16 days** |
| Amazon | Corporate | 6 days |
| Meta (Reality Labs) | 1,500 | 4 days |

Logistics has longest windows (regional labor agreements slow disclosure). Tech is tightest (leaks + earnings pre-announcements).

## Best Data Sources (Ranked by Programmability)
1. **Texas** — OData API via Socrata, weekly updates, SoQL queryable. **Best source.**
2. **New York** — WARN Dashboard, daily updates, good filtering. NY also requires AI-role disclosure in layoffs (2025 directive).
3. **California** — Comprehensive but manual (email-based filing, ~10 day processing lag). SB 617 (Jan 2026) adds CalFresh coordination = signals layoff permanence.
4. **Oregon** — HECC Activity Tracking System, detailed but 6-year retention limit.

**URLs:**
- TX: https://data.texas.gov/dataset/Worker-Adjustment-and-Retraining-Notification-WARN/8w53-c4f6/data_preview
- NY: https://dol.ny.gov/warn-dashboard
- CA: https://edd.ca.gov/en/jobs_and_training/Layoff_Services_WARN/
- OR: https://www.oregon.gov/highered/about/workforce/pages/warn.aspx

## Key Insight: "Low-Hire/Low-Fire" Regime Changes the Signal
- Voluntary quits at post-pandemic lows → workers afraid to leave
- This INCREASES WARN reliability: more labor churn is now involuntary/mandated
- Formula: Separation Momentum = (0.85 × WARN filings) - voluntary attrition
- When voluntary attrition drops, WARN becomes a higher % of total separations

## Current Anomaly (Feb 2026)
- IJC: 206K-212K (remarkably low)
- WARN filings: surging (Dec 2025 / Jan 2026)
- **Gap = "shadow payrolls"** — workers on notice but still employed through notice period
- This gap closes in 4-8 weeks → expect IJC to rise March-April 2026

## Noise Filters (What to Exclude)
1. **Healthcare strikes** — nursing strikes trigger WARN-like filings but aren't economic layoffs (ULP strikes over staffing ratios)
2. **Seasonal retail** — post-holiday fulfillment center closures, Spirit Halloween etc.
3. **Temporary furloughs** — unless amended to "Permanent"
4. **Private companies** — no stock correlation but retain for aggregate macro signal

## Quant Fund Behavior (How Smart Money Uses This)
- **Breadth > magnitude** — a cluster of mid-size filings across diverse industries > one mega-layoff
- **AI cuts are "beta-neutralized"** — market assumes AI layoffs = capex reallocation, not demand weakness
- **Continuing Claims as validation** — if WARN spike isn't followed by continuing claims rise within 8 weeks, signal discarded as "reallocation"

## Application for LABOR
1. **Set up Texas API scrape** — highest quality, most programmable source
2. **Track WARN→IJC lag** — currently seeing surge in filings with flat claims. March-April is the test.
3. **Breadth signal** — monitor filing diversity across sectors, not just tech mega-layoffs
4. **Filter AI vs cyclical** — NY now requires AI disclosure. Use this to separate structural from demand-weakness layoffs.
5. **The shadow payroll gap is our edge** — IJC looks fine because notice periods haven't expired. 4-8 week lag = March-April 2026 claims should rise if WARN signal is real.
