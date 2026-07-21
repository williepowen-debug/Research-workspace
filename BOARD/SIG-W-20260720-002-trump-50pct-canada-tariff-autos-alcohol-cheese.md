---
signal_id: SIG-W-20260720-002
dispatched: 2026-07-21T00:05:00Z
origin: WALTER today-sweep (Will-directed, 2026-07-20 ~23:45Z) — catch-all news agent, multi-outlet
source: USA Today / Financial Times / The Times / Indian Express, all 2026-07-20 (via WALTER news-sweep agent — WebSearch quota exhausted, WebFetch/RSS-sourced)
source_tag: WALTER-SWEEP
signal_type: catalyst
domain: TARIFF_TRADE
cluster: INFLATION_TRANSMISSION
event_window: closed
precedence: PRIORITY
to: [CARL]
info: [HENRY, REGINALD, RED, MARCO]
confidence: 0.80
verify_verdict: >
  not-spawned (sweep-degraded session — WebSearch quota exhausted, all agents WebFetch/RSS-only). 4-outlet corroboration (USA Today / FT / The Times / Indian Express, all 7/20) → the FACT is well-sourced; the ~30-day runway + exact product scope are as-reported. CARL should verify the effective date + covered-goods list against a primary (USTR/White House EO) before modeling the CPI pass-through.
routing_note: >
  CARL (action, TARIFF_TRADE owner — cost-push → consumer/CPI). Trump imposed a 50% tariff on a broad range of Canadian goods (autos, alcohol, cheese) today, citing a wildfire-smoke "invasion" pretext; threats began 7/17-18, today is the actual imposition, with a ~30-day implementation runway before it bites. This is the day's biggest genuinely-missed item — no fleet coverage. INFLATION_TRANSMISSION cluster (tariff front-loading / cost-push with a 3-6mo CPI lag). HENRY info (macro/Fed — feeds the same-day "tighten not cut" tilt, SIG-W-20260720-005). REGINALD info (Canada-exposed bank/borrower 2nd-order). MARCO info (cross-border/trade-flow). RED info (adversarial — a 30-day runway + a wildfire pretext invites legal challenge / carve-outs / negotiation reversal; the announced scope may not be the enacted scope).
---

# Trump imposes 50% tariff on broad Canadian goods (autos / alcohol / cheese) — cost-push, ~30-day runway

From WALTER's Will-directed today-sweep (2026-07-20). **Source:** USA Today / FT / The Times / Indian Express, all 2026-07-20 (WALTER news-sweep agent; ⚠️ WebSearch quota was exhausted this session — RSS/WebFetch-sourced, 4-outlet corroborated).

## What happened
- **Trump imposed a 50% tariff on a broad range of Canadian goods** — autos, alcohol, cheese named — **citing a wildfire-smoke "invasion" of US air as the pretext.** Threats began 7/17-18; **today (7/20) is the actual imposition**, with a **~30-day implementation runway** before it takes effect.
- Markets barely moved on it (Dow −0.6% on the day, but that was Iran-war-driven risk-off, not the tariff) — this is a **slow-fuse cost-push** item, not a same-day shock.

## Why it matters / read (WALTER routes, does not model)
- **CARL owns it (TARIFF_TRADE):** a 50% tariff on a top-2 US trading partner across autos/alcohol/cheese is a **cost-push inflation-transmission** event — the INFLATION_TRANSMISSION cluster's exact "tariff front-loading" channel, with the usual 3-6 month CPI lag. Feeds directly into the consumer-stagflation thesis and lands the **same day** as Warsh's hawkish "no tolerance for inflation" testimony (SIG-W-20260720-005) — a tariff-driven goods-price impulse into a Fed that just signaled it won't look through inflation.
- **Two-sided (RED):** the 30-day runway + the unusual "wildfire" pretext make this **highly reversible/negotiable** — the announced scope is not necessarily the enacted scope (carve-outs, USMCA friction, legal challenge, or a deal all live). Route the announcement; the enacted tariff is what transmits.
- ⚠️ **Verify before modeling:** confirm the effective date + covered-goods list against a primary (USTR / White House EO) — the sweep was RSS-sourced.

**Routing:** CARL (action) / HENRY, REGINALD, RED, MARCO (info). Domain TARIFF_TRADE. Cluster INFLATION_TRANSMISSION. PRIORITY. Confidence 0.80 → **0.88 (primary-verified, see addendum).**

---

## 2026-07-21 VERIFICATION ADDENDUM — primary-checked vs whitehouse.gov (Will-directed dig)

*One WebFetch-to-primary verification agent (WebSearch unavailable). Confirms + sharpens + CORRECTS one framing point.*

- **✅ REAL and SIGNED (not a threat):** whitehouse.gov/presidential-actions confirms **FOUR proclamations dated 2026-07-20** — separate ones for **motor vehicles / alcoholic beverages / dairy**, plus a same-day **aluminum** action (distinct, §232). Multi-outlet (AP/BBC/Guardian/NYT/WaPo/CNN/CBC, all 7/20).
- **Terms:** **50% ad valorem; effective 2026-08-19 12:01am ET (30-day runway confirmed).** Imposed-in-LAW but not-yet-in-EFFECT (reconciles the "threatens" vs "imposes" outlet split).
- **🔴 CORRECTION — legal authority is Section 338 of the Tariff Act of 1930 (19 U.S.C. 1338)** (the rarely-used "offset foreign discrimination" statute) + §604 Trade Act 1974 — **NOT IEEPA, NOT §232.** The proclamation's stated basis is **Canada's discriminatory tariff treatment of US autos since 2025-04-09 (~22% drop in US auto exports to Canada)** — a trade-discrimination rationale.
- **🔴 CORRECTION — the "wildfire-smoke invasion" framing is TRUMP'S RHETORIC, not the legal basis.** The proclamations contain **zero mention of wildfire/air-quality**; Trump's "invasion / poisoned air / pay damages" comments were separate (a reported World Cup-final confrontation with PM Carney). Route the §338 trade-discrimination action; treat wildfire as negotiating color. *(My original "wildfire pretext" framing above is corrected on-record here.)*
- **Significance of the §338 basis:** a signed instrument (firmer than a threat) but on **rarely-used, legally-untested-at-scale** ground → challengeable; the 30-day window is real negotiating runway.
- **Canada response — EXPLICIT NEGATIVE:** no official retaliation / counter-tariff / WTO / USMCA-dispute action found as of 7/20 (cbc.ca 403'd — access gap, not confirmed absence). **CAD weakened** (USD/CAD up, also on soft Canada CPI).
- **Context:** an escalation within a live 2026 US-Canada trade campaign (Feb-2026 15% levy, softwood-lumber disputes, late-June "US not extending USMCA / decade-countdown to end the pact") — not a bolt from the blue.
- **Confidence 0.80 → 0.88** (whitehouse.gov primary confirmation). CARL: model the Aug-19 effective date + the auto/alcohol/dairy annexes; the §338 basis is the durability question.
