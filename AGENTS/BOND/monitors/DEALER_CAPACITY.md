# BOND Monitor — Dealer Capacity / Absorption

**Owner:** BOND
**Last Updated:** 2026-08-21 by BOND — ★ **NEW PRINT: the 8/12 as-of landed, and it is the refunding week itself.** Long-end total **$149.2B** (11–21Y **$61.2B**, >21Y 48.6B, 7–11Y 39.3B); peak-to-current **−14.8%** (from 175.0B, 6/24) and **−20.9%** on 11–21Y (from 77.4B). **Second consecutive 11–21Y decline (−$2.9B); long-end total −$0.8B w/w.** ★ **THE READ IS THE STRONGEST FORM BENIGN DISTRIBUTION HAS TAKEN: this is the week of the $125B August refunding — dealers ran long-end inventory DOWN THROUGH the quarter's largest supply event, and that refunding cleared with indirect at/above trailing-12 median at ALL THREE tenors and dealers at or below median.** The monitor's own discriminator requires **weak auctions and/or SOFR−IORB positive** for the forced-de-risking branch: the auctions were firm and **SOFR−IORB is −2bp [8/20]** (the +1bp of 8/17 fully reversed). ⇒ **Distribution is now confirmed THROUGH a supply test, not merely around one. Vector HOLDS at 2 — no build, so the 'two consecutive weekly builds' upgrade leg (instrument = long-end TOTAL, named 2026-08-18) is nowhere.** *(Prior header:)* 2026-08-18 by BOND — **staleness sweep. 3 prints recovered (7/22, 7/29, 8/05); the benign reading is now CONFIRMED by the August refunding rather than assumed.** ⚠️ **And a contradiction inside this file is fixed: the 7/28 header announced "the record has unwound" while the *Current Read* section below still said vector 3, fresh record highs, 4-trigger ARMED — the header was corrected and the body was not.** *(That is the third instance of this exact shape found today: `thesis/THESIS.md` v1.1.3 did it with the falsifier apparatus, its status line did it with this same dealer record, and this monitor did it here. **Updating a header is not updating a document.**)* *(Prior: 2026-07-28 — gap closed.)*

> ## ✅ RESOLVED 2026-07-28 — it was never an access problem
>
> **Root cause: a stale API series break.** The NY Fed primary-dealer API partitions data into *series breaks*. A query against **`SBN2022`** returns **HTTP 200 with real data that stops at 2024-07-02** — which reads exactly like *"the API caps pre-2026."* Nothing errors, nothing warns. The live break is **`SBN2024`** (2024-07-03 → open). Three re-attempts (7/6, 7/23, 7/28) all re-ran the same wrong query without auditing the path.
>
> Second trap, found the same way: the bucket is **`PDPOSGSC-G7L11`**, not the zero-padded `G07L11` — the padded guess returns a **200 with an empty timeseries**. Another silent wrong answer.
>
> **Durable fix: `monitors/fr2004_fetch.py`** — resolves the series break **at runtime** (never hardcoded), fails loud on an empty series and on >28d staleness. **Run it weekly; do not hand-query this API.**
>
> ### 📉 THE DATA IT RECOVERED — the record is GONE
>
> | as-of | 7-11Y | 11-21Y | >21Y | long-end | w/w |
> |---|---:|---:|---:|---:|---:|
> | 2026-06-17 | 42.9 | **74.6** | 57.0 | 174.5 | +13.3 |
> | 2026-06-24 | 42.2 | **77.4** ← *true peak* | 55.4 | **175.0** | +0.5 |
> | 2026-07-01 | 40.7 | 73.3 | 56.8 | 170.9 | −4.2 |
> | 2026-07-08 | 41.9 | 71.7 | 53.2 | 166.9 | −4.0 |
> | 2026-07-15 | 41.3 | **63.9** | 54.0 | **159.2** | −7.6 |
> | 2026-07-22 | 39.1 | 64.7 | 53.5 | 157.2 | −2.0 |
> | 2026-07-29 | 37.1 | 65.0 | 57.2 | 159.3 | +2.1 |
> | 2026-08-05 | 33.4 | 64.1 | 52.5 | 150.0 | −9.3 |
> | **2026-08-12** | **39.3** | **61.2** | **48.6** | **149.2** | **−0.8** ← *latest, pulled 2026-08-21; the $125B refunding week* |
>
> **11-21Y −$13.4B (−17.4%) off peak; long-end −$15.8B (−9.0%) across four consecutive accelerating weekly declines.** Note the 6/17 print BOND carried as "the fresh all-time record" was **one week early** — 6/24 was the true peak, unobserved because the series was unreadable.
>
> ### Verdict: **BENIGN DISTRIBUTION**, not forced de-risking — and the discriminator is in the triggers table below
>
> A falling inventory is **ambiguous on its own**. Forced de-risking appears *with* weak auctions and/or positive SOFR-IORB; benign distribution appears *with* firm end-demand. Observed across the entire drawdown window: indirect demand was **exceptional** (7/9 30Y 77.7% · 7/22 20Y-R 69.1% · 7/23 TIPS 65.2%) and **SOFR-IORB was negative** (−1bp, 7/24). **Dealers had real money to sell into.**
>
> **⇒ Vector DOWNGRADED 3 → 2** on the pre-registered condition; **"→4 ARMED" is DISARMED**; composite 14 → 13/35. **This cuts against BOND's standing bear thesis** — "record dealer stock" was one of three legs of the demand-hole configuration and it is now gone.

<details><summary>Prior escalation notice (2026-07-28 AM, superseded hours later by the fix above)</summary>

> ## 🔴 DATA GAP — ESCALATING, not rolling again
> **The stock series that drives this vector has not been pulled since the 6/17 as-of print. Five prints are now owed: 6/24 · 7/1 · 7/8 · 7/15 · 7/22.** The NY Fed API path used here returns pre-2026 data in-env; retried 7/6, 7/23, 7/28.
>
> **Why this matters more than a normal stale row:** dealer absorption is a **STOCK** vector — benign auction takedowns (which is what we keep getting) show the backstop *wasn't binding that day* and **cannot refresh the inventory stock.** Only FR2004 can move this vector in either direction. So the 🟠 score and the **"→4 trigger ARMED"** state are both resting on a **6-week-old observation**, and the 7/2 downgrade condition in STATUS ("dealer-absorption →2 if the 7/2 print shows a sharp drawdown") has been **unscoreable the entire time.**
>
> **This has been carried as "pending pull" for four weeks. Escalating to Will/PROME as an owed data-source gap rather than deferring a fifth time.** Options: an alternate NY Fed endpoint, the FRED mirror of the primary-dealer series, or accepting the vector as **[STALE — frozen at 6/17]** and saying so on every surface that cites it.

*(Outcome: none of the three. The correct answer was **audit the failing path** — the endpoint was right, the query was wrong. Escalating a data gap without first checking whether the failure is self-inflicted wastes the escalation.)*

</details>
**Purpose:** Track whether dealers can absorb Treasury and credit supply without creating funding or duration stress.

## Key Inputs

| Metric | Source | Cadence | Interpretation |
|---|---|---|---|
| Primary dealer net Treasury positions | NY Fed FR2004 | Weekly | Rising = absorption capacity used; falling under stress = forced de-risking |
| Treasury auction dealer take-down | Treasury auction results | Every auction | High dealer % = weak end demand / warehousing |
| eSLR / SLR rule changes | Fed/OCC/FDIC / news | Event | Capacity relief or constraint |
| Basis trade leverage | CFTC/SEC/Fed reports / market research | Monthly/event | Hidden duration/funding fragility |
| SOFR/repo pressure | LIQUID | Daily | Funding consequence, not BOND-owned |

## Current Read

**🟡 Dealer-absorption vector = 2 (watch). The record is GONE and the 4-trigger is DISARMED.** FR2004 as-of **2026-08-12**, re-pulled **2026-08-21** via `monitors/fr2004_fetch.py` *(⚠️ this body read as-of **8/05** beneath an 8/12 header until 2026-08-21 — a fresh header over a stale body CERTIFIES it; `[[finding_header_edit_is_the_edit_most_mistaken_for_maintenance]]`)*, pulled 8/18 for the 8/05 vintage (series break `SBN2024` resolved at runtime).

| Bucket | 6/24 peak | 7/15 | 8/05 | **8/12 (latest)** | Δ from peak |
|---|--:|--:|--:|--:|--:|
| 11–21Y | **$77.4B** | $63.9B | $64.1B | **$61.2B** | **−$16.1B / −20.9%** |
| Long-end total (7–11 + 11–21 + >21) | **$175.0B** | $159.2B | $150.0B | **$149.2B** | **−$25.9B / −14.8%** |

**The week to 8/05 was −$9.3B — the largest weekly long-end drawdown in the window. The week to 8/12 added a further −$0.8B, and 8/12 IS the $125B refunding week: dealers ran inventory DOWN THROUGH the quarter's largest supply event.** *(⚠️ Δ-from-peak figures re-derived off 8/12 — they read −17.1% / −14.3% off the 8/05 leg until 2026-08-21. A derived figure does not inherit a level fix.)*

**★ READ = BENIGN DISTRIBUTION, and as of 8/18 this is CONFIRMED rather than inferred.** The monitor's own discriminator (below) requires *weak auctions and/or SOFR-IORB positive* for the forced-de-risking branch. **The 8/05 drawdown was immediately followed by the August refunding (8/11–8/13, $125B), which cleared with indirect at/above trailing-12 median at ALL THREE tenors and dealers at median** — the 30Y clearing 5.216% (highest since 2001) with indirect 66.85%. ⇒ **Dealers were clearing balance sheet AHEAD of supply and then did not have to eat it.** That is distribution into demand, not liquidation.

⚠️ **Stated because it cuts against BOND's standing bear thesis:** "record dealer stock with no backstop" was one of three legs of the demand-hole configuration this desk published for six weeks. **It is gone, and its removal makes the bear case LESS pre-positioned, not more.**

⚠️ **The one thing that could overturn this is outstanding and owed by LIQUID:** the refuse-or-confirm on **repo/funding stress over 7/01→7/15**, unanswered since 7/28. **If funding stress existed in that window, this same inventory decline re-reads as forced de-risking — which is MORE bearish.** Re-asked 8/18.


## Rolling Table

| Date | Dealer UST position | Auction take-down note | Repo/SOFR context | Read | Source |
|---|---:|---|---|---|---|
| 2026-05-05 refresh | ~$550B net Treasuries | Capacity expanded post-eSLR | SOFR-IORB normalized | 🟡 capacity-used | Prior BOND STATUS / NY Fed/FT note |
| 2026-05-11 3Y | N/A | Dealer accepted 13.6% | SOFR-IORB -5bps | 🟡 watch | FiscalData + dashboard |
| 2026-05-12 10Y | N/A | Dealer 12.0% | SOFR-IORB ~0 | 🟡 | FiscalData |
| 2026-05-13 30Y | N/A | Dealer 11.7% | SOFR-IORB ~0 | 🟡 | FiscalData |
| 2026-05-27 FR2004 | **11–21Y $67.0B (record); 7–11Y $38.0B (94th pctile); >21Y $49.7B** | — (positioning snapshot) | SOFR-IORB ~0 | 🟠 record *stock* | NY Fed FR2004 (KB-BND-047) |
| 2026-06-10→16 June auctions | (pre-6/23 re-pull) | 10Y PD 9.5%, 20Y 8.5%, 30Y 14.7% — **flow benign** | SOFR-IORB -2bp (6/17) | 🟠 stock-high / flow-benign | TreasuryDirect |
| 2026-06-17 FR2004 | **11–21Y $74.6B (NEW record, +11.4% w/w); 7–11Y $42.9B; >21Y $57.0B; combined $174.5B #2 ever** | 6/23-25 cluster takes 10.2–12.9% (benign) | SOFR-IORB +3bp 6/30 = clean qtr-end (SRF $0) | 🟠 fresh-record stock / flow-benign — **→4 trigger ARMED** | NY Fed FR2004 API (KB-BND-061) |
| **2026-06-24 FR2004** | **11–21Y $77.4B = THE TRUE PEAK (not 6/17); 7–11Y $42.2B; >21Y $55.4B; total $175.0B** | 6/23–25 cluster benign | SOFR-IORB negative | 🟠 peak stock | NY Fed FR2004 *(added 8/18 — the 7/28 write called 6/17 the record; it was one week early)* |
| 2026-07-01 → 07-15 FR2004 | 11–21Y 73.3 → 71.7 → **63.9**; total 170.9 → 166.9 → **159.2** | 7/09 30Y ind 77.7%; 7/22 20Y-R ind 69.1%; 7/23 TIPS ind 65.2% | SOFR-IORB negative | 🟡 benign distribution | NY Fed FR2004 |
| **2026-07-22 → 07-29 FR2004** | 11–21Y **64.7 → 65.0** (two consecutive BUILDS); total 157.2 → 159.3 | 7/28 7Y ind 70.15%, dlr 12.97% — no composition failure | SOFR-IORB negative | 🟡 | NY Fed FR2004 *(added 8/18)* |
| **2026-08-05 FR2004** | **11–21Y $64.1B; 7–11Y $33.4B; >21Y $52.5B; total $150.0B = −$9.3B w/w, the largest weekly drawdown of the window** | **August refunding 8/11–13 then cleared CLEAN at all three tenors** (3Y ind 64.24 / 10Y ind 76.73 / 30Y ind 66.85, dealers at-or-below median) | SOFR-IORB −3bp → **+1bp [8/17]**, inside its −3/+1 monthly range | 🟡 **benign distribution CONFIRMED** | NY Fed FR2004 + TreasuryDirect *(added 8/18)* |

| **2026-08-12 FR2004** | **11–21Y $61.2B; 7–11Y $39.3B; >21Y $48.6B; total $149.2B = −$0.8B w/w** — *the $125B August refunding week itself* | **Refunding cleared with indirect at/above trailing-12 median at all three tenors and dealers at or below** | SOFR−IORB negative (−2bp [8/20]) | 🟡 benign | NY Fed FR2004 `SBN2024`, pulled 2026-08-21 |

## Triggers

> ⚠️ **INSTRUMENT NAMED 2026-08-18 — the upgrade trigger was a threshold FAMILY, not a threshold.** The registered condition *"→3 on a fresh long-end high **or two consecutive weekly builds**"* never said **which series**. On **11–21Y it FIRED** (+0.8 then +0.3 on 7/22 and 7/29) **and the very next print (−0.9) unfired it.** On **long-end TOTAL** it never fired (one build, then −9.3). **The instrument is hereby LONG-END TOTAL**, on grounds independent of which way it points: that is what this monitor's headline and the vector's evidence cell have always cited, the 11–21Y builds are sub-1% noise (+1.3%, +0.5%), and the most recent print contradicts them. ⚠️ **Note the direction: firing the upgrade would have STRENGTHENED BOND's own bear thesis, and BOND declined it.** (`finding_unnamed_instrument_makes_a_threshold_a_family`.)
> ⚠️ **This is also n=2 on revert-speed** — a trigger that fires and un-fires on consecutive weekly prints, alongside `VX-BND-01` round-tripping 2→3→2 in 11 hours on 7/28. **Queued with the v1.1.4 base-rating work, not fixed here** (`KB-BND-099`).


| Trigger | Action |
|---|---|
| Dealer inventories at/near record + weak auctions | Signal LIQUID/ZHAO; watch repo funding |
| Forced inventory decline during selloff | 🔴 market-function stress |
| eSLR relief drives absorption while end-demand weak | Mark as mechanical support, not clean bill of health |
| Weak auction followed by SOFR-IORB positive | Escalate as auction stress funding through repo |
