> ## ⚠️ RATES ARE NO LONGER CANONICAL HERE — `workbook/WARRISK.tsv` IS (2026-07-31)
> **This file is a .md, so NO script grades it** — `ledger_staleness.py` globs `workbook/*.tsv` only. That is why the 7/21 rate sat here for 10 days with nothing but a sibling's cross-theater bar to flag it. The **rate ledger, source set, and staleness clocks moved to `AGENTS/OSPREY/workbook/WARRISK.tsv`**, which is auto-graded at boot (step 5a-2, `--days 7`).
> **What stays here:** the narrative logs below — insurer withdrawals/restrictions and owner-willingness signals — plus the historical rate rows B-01..B-05 **as a frozen record of how this surface was maintained before 7/31.**
> **Do not add new rate rows to this file.** Add them to the TSV. ⚠️ If the two ever disagree, **the TSV wins.**
> **Also corrected 7/31:** the "may be structurally unobservable" read stated earlier that day was **wrong** — it came from a ONE-outlet search set. Black Sea AWRP is *event-driven* observable (prints on step-changes), the source set is **8 outlets**, and there is a **daily continuous proxy** (Baltic **TD6 = 135,000mt CPC→Augusta**, the exact route under attack). Full reasoning in the TSV header.

# Black Sea War-Risk Rate Series — Named Watch Surface
**Owner:** OSPREY · **Created:** 2026-07-22 (Will-directed via PROME, `inbox/2026-07-22_from-PROME_war-risk-watch-assignment.md`; Will on record 7/21 late — "ASSIGN the watch", BRENT gap-sweep note)
**Scope:** Black Sea marine war-risk rate prints, insurer withdrawals/restrictions for Black Sea/CPC-relevant hulls, owner-willingness signals. **Watch only — no thresholds, no capital path** unless proposed and Will-gated later.
**Split:** OSPREY = Black Sea leg (this file). FALCON = Gulf + Red Sea + JWC listings + P&I club actions. BRENT consumes both. HAWK owns cross-war enforcement/insurance synthesis — cc on step-changes.
**Route rule:** any step-change (>1% holding, further repricing, insurer withdrawal/restriction) → BRENT + PROME, cc HAWK.
**Why this exists:** war-risk pricing is the binding transmission mechanism in all three live theaters (BRENT 7/21 gap sweep); it is the owner/insurer-pullback channel that GATE-OSPREY-001 leg-(b) reasoning already treats as the binding constraint on CPC halt duration (not repair time).
**KB anchor:** KB-OSPREY-018 (surface registration) · KB-OSPREY-016 (first live print, 7/21).

---

## Rate ledger (stamped observations — one row per print; source + date every claim; append, never overwrite)

| # | Print date | Rate / signal | Scope | Source (class) | Logged | Notes |
|---|---|---|---|---|---|---|
| B-01 | 2025-12-01 *(historical baseline)* | Russian Black Sea ports ~**0.65-0.8%** of hull value (up from ~0.6% prior week); Ukrainian ports ~**0.5%** (from ~0.4%) | Voyage AWRP, RU + UA Black Sea ports | Insurance Business (relaying shipping/insurance market participants), 2025-12-01 — **verified vintage, NOT a fresh print** | 2026-07-22 | Pre-campaign-escalation reference level. Caught as recirculated in 7/22 search results — usable as baseline only. |
| B-02 | 2026-07-21 | Black Sea war-risk rates rose **above 1%** (one broking source ~**1.5%**); prior ~**0.6%** net of no-claims bonus. One underwriting source still quoting ~0.6% ("a bit thin" per broker). | Black Sea AWRP, post 7/18-21 CPC tanker-strike wave | **The Insurer 2026-07-21** (primary trade press, named class per assignment) | 2026-07-22 | THE live baseline print. Quote spread (0.6% vs 1.5%) = repricing in progress, not settled. Registered at assignment as baseline 0.6% → >1%. |
| B-03 | 2026-07-22 | **No fresh rate print found 7/22.** B-02 stands. Adjacent owner-willingness signal: CPC storage tanks FULL → intake halted 7/21 (Reuters) — consistent with tankers staying away post-strikes. | Black Sea | 7/22 session sweep (WebSearch, live-dated filter) | 2026-07-22 | Absence-of-print row: distinguishes "no repricing" from "not checked" (fail-loud discipline). |
| B-04 | 2026-07-23 | **No fresh rate print found 7/23.** B-02 (>1% / ~1.5% broker, from ~0.6%) stands. 7/22-23 searches return only the 7/21 numbers. Adjacent owner-willingness signal escalated: Kazakhstan CUT crude output 7/23 (sharp at Tengiz) to prevent tank overflow — loading demand still effectively zero. | Black Sea | 7/23 day-4-check sweep (WebSearch, live-dated filter) | 2026-07-23 | Absence-of-print row. No step-change to route. |
| B-05 | 2026-07-24 → 2026-07-31 *(gap row, 8 days)* | **NO fresh rate print found anywhere in 7/24–7/31.** B-02 (>1% / one broker ~1.5%, from ~0.6%) **still stands as the live print, now 10 days old.** ⚠️ **THE 10-DAY FORMAL STALENESS BAR (HAWK's cross-theater bar, flagged 7/28) HAS NOW BREACHED — 2026-07-31.** | Black Sea | 7/31 full-session sweep (WebSearch, multiple query shapes incl. underwriter/broker/premium/reassess framings) | 2026-07-31 | **Absence row covering the 7-day dark period.** ⚠️ **VINTAGE TRAP CAUGHT (8th this campaign):** searches surface "RU Black Sea ports quoted ~0.65–0.8%, UA ports ~0.5%" — that is **B-01's Dec-2025 baseline recirculating**, NOT a fresh print. Do not read it as a *decline* from B-02. |
| — | — | **★ THE FINDING, not the absence:** BRENT asked directly (7/30) whether the insurer leg is repricing on **recurrence** rather than on any single event — *"frequency is exactly what underwriters price — if six strikes in twelve days has not moved the rate, that is a genuinely surprising negative."* **Answer as of 7/31: there is NO published print either way.** Six strikes on CPC in 12 days, three shutdowns in a month, a Russian terminal (Sheskharis) halted 5 days, and a sunk grain ship with 10 dead — and the trade press has published no Black Sea rate since 7/21. | — | 7/31 sweep | 2026-07-31 | **This is a measurement gap, not evidence of a flat rate** — the honest statement is "unobserved," and it must not be reported to BRENT as "unchanged." Distinguishing those two is the whole point of these absence rows. Recommended next step: this surface has hit the limit of what open-source trade-press sweeping can resolve; a genuine answer needs a broker/underwriter-side source OR acceptance that the leg is unobservable at this cadence. **Flagged to Will/PROME — a named-surface watch that cannot produce prints is a surface that needs a source upgrade or a written scope limit.** |

## Insurer withdrawals / restrictions log
*None recorded as of 2026-07-31. Log named-insurer withdrawals, Black Sea/CPC hull restrictions, JWC Black Sea listing changes (JWC listings themselves = FALCON's ledger; cross-reference here if Black Sea-specific).*
*7/31 note: no insurer withdrawal or restriction reported in the 7/24–7/31 window. Nearest adjacent facts are **owner-side, not insurer-side** — see the willingness log below.*

## Owner-willingness signals log
| Date | Signal | Source |
|---|---|---|
| 2026-07-21/22 | Post-4-strikes: no tanker reported returning to CPC SPMs; CPC storage tanks reached capacity → intake from Kazakhstan halted — de facto evidence loading demand (tanker calls) at zero | Reuters via Times of Central Asia 7/22; Kazakh Energy Min 7/21 |
| 2026-07-26 | **Owner willingness RETURNED at CPC** — SEAMAJESTY and MILOS loaded, both chartered by **Tengizchevroil**, with SPMs unrepaired and no FM. The same corporate family (Chevron/TCO) that was reported refusing to call on 7/23 came back 4 days later on its own barrels. **Resolves the natural experiment HAWK pre-registered 7/25: the halt was WILLINGNESS-bounded, not repair-bounded.** | Astana Times 7/27; Bloomberg 7/27; HAWK packet 7/28 |
| 2026-07-26 | **Sheskharis (Russian terminal) resumed on ONE berth only** after a 5-day halt — partial willingness/capacity return, not a full one. | Bloomberg 7/27; OilPrice 7/27 |
| 2026-07-30/31 | Willingness re-broken: NISSOS SIFNOS struck **while loading at SPM-3**; MARATHI struck while awaiting berth ~6nm out. CPC loadings suspended again, **not resumed as of 7/31**. ⚠️ Chevron CEO on the 7/31 earnings call said CPC is *"flowing and ships loading this week"* — **conflicts with the operator's own suspension statement; treated as loose/forward framing, NOT logged as a resumption.** | CPC operator statement; TASS 7/30; Times of Central Asia 7/30; Xinhua 7/31; Chevron earnings call via Investing.com 7/31 |

---

## Method notes
- **Source tier:** The Insurer / Lloyd's List / TradeWinds / Insurance Business / Reuters-insurance — named per print. Broker vs underwriter quotes distinguished where the source does.
- **Vintage discipline:** every print date-verified before logging (this surface was stood up the same session that caught FOUR recirculated-vintage items, incl. a Dec-2025 rate range circulating in 7/22 search results).
- **Rates are % of hull value per voyage/7-day (AWRP)** unless noted; no-claims-bonus adjustments noted where sources give them.
- **No thresholds live on this surface.** GATE-OSPREY-001 legs are the only registered tripwires; an insurance rate is NOT a gate leg (KB-OSPREY-016 note) — this surface feeds the leg-(b) mechanism read, it does not fire anything by itself.
