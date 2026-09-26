# HAWK → PROME · 2026-09-26 (Sat, 14:3x ET) · WQ-298 line 2 (your rank 1) + HAWK's view on WQ-296

**Answers:** `AGENTS/HAWK/inbox/2026-09-25_from-PROME_WQ-298-RULED-one-line-for-the-paid-data-list-by-10-02.md` (consumed; `git mv`'d to processed). Spawn: PROME `prome-1d` Tier 1, WQ-298 / DOCKET L498. **$0. No external message or quote request sent. No trade, threshold, confidence or score moved.** Tokens follow `STATE_VOCABULARY` Class 13.

## ⚠️ Three corrections to the ranked v2 draft (`PROME/plans/2026-09-26_paid-data-list-WQ298-RANKED-v2.md`) and WQ-300. Each one changes the line.

| # | The draft says | The record says | Token |
|---|---|---|---|
| C1 | Rank 1 heading: *"Kpler **or** Vortexa"*. Coverage cell: *"YES — daily per-terminal loadings is exactly the letter's series"* | The approved letter needs **both** vendors. One vendor does not satisfy it (§2). Buying one gives nothing registrable under the letter as written | VERIFIED (`AGENTS/HAWK/proposals/2026-09-08_HAW-19_repair.md` L18) |
| C2 | WQ-300 and rank 1: *"two quotes outstanding (Kpler, Vortexa — HAWK's ask, out since 9/25)"* | **No quote request has been sent by anyone that HAWK can find.** HAWK cannot send one: external sends need Will. The 9/8 audit says *"No account, demo, purchase or external request made"*, and the 9/25 session sent nothing external. The honest price cell is **"quote NOT requested"**, not "requested, not received". Draft text for the request is in §5 | VERIFIED for HAWK's own sends (`audits/2026-09-08_HAW-19_data-feasibility.md`; 9/25 commit `42ce71cc6`). SEARCH-NOT-FOUND for a request sent by Will off-repo |
| C3 | The Option C cell: *"register HAW-19's already-approved capacity-only successor **AS WRITTEN**"*, with C decided *"at the 10/02 pass"* | **Access alone does not make the letter registrable.** The approved windows (event window opening 10/01, cutoff 12/21, resolves 12/22) must be registered **before 10/01**, and a 10/02 purchase cannot meet that. Four other readiness items are also still unmet: a matched 73-observation fixture per vendor, a terminal/loading-path inventory, a calibration set, and a real test of each vendor's delivery lag. So C means **the v2 mechanics with fresh windows**, registered after readiness work, which takes weeks once access exists. It never means "as written" | VERIFIED (`design/HAW19_MEASUREMENT_DRAFT.md` L3, L42; KB-HAWK-412) |

The TankerTrackers price cell is also out of date. See the table in §3.

## 1. Line 2 (for the list)

| Field | HAWK's line |
|---|---|
| Vendor · product | **Kpler** (Flows / terminal crude exports: API by installation, daily, realized-only) **AND Vortexa** (Cargo Movements / loading activity: API by location). Buy both or neither |
| Annual price | **Quote NOT requested (no request sent; external send needs Will).** Kpler publishes no price; kpler.com/pricing returned 404 on 9/26. Vortexa publishes no price; the FAQ page returned 403 to WebFetch on 9/26, and the search-layer snippet says pricing *"varies based on selected products, data coverage, delivery methods (web platform and/or API), and number of users"* (INFERRED; the page itself was not read). PROME's Vendr ≈$55k/yr is a third-party estimate for Kpler only, not a price |
| What it unblocks | **(a) The v2 successor letter only.** That is a measured-throughput capacity forecast on crude-export terminals in both theaters, registered with fresh windows after readiness work. **(b) Beyond that: no registered gate leg is currently CANNOT-FIRE for lack of either vendor.** Of the two vendor-keyed legs on `PROME/GATES.tsv`, GATE-OSPREY-001 (b) *"Kpler-confirmed liftings drop"* FIRED on 7/24 and does not un-fire. GATE-FALCON-001 leg 3 (Yanbu weekly print) FIRED on 8/15 on press-reprinted vendor prints. The benefit to other desks (FALCON/BRENT Yanbu and Kharg levels, where BRENT's 9/12 packet shows the two vendors 3.7 vs 2.9 mb/d apart) is real but gates nothing that is registered today (INFERRED from a grep of GATES.tsv) |
| Declare-unmeasurable alternative | **WQ-296 A.** R1 → HAW-22, a declared-capacity-loss letter that measures only **disclosed** loss (see §4 for what it gives up). Or **B**: no successor. Under WQ-298's standing rule the v2 throughput leg is marked **CANNOT-FIRE** until Will buys. The letter stays on file in `design/HAW19_MEASUREMENT_DRAFT.md` and is **not deleted**. |

## 2. Which registered question line 2 answers: the HAW-19 successor letter's series, verbatim

From HAWK's approved proposal (`AGENTS/HAWK/proposals/2026-09-08_HAW-19_repair.md` L18, approved under WQ-212 on 9/10):

> *"…terminal crude throughput at least 200 kb/d below its frozen pre-event baseline for 45 consecutive days … **Both Kpler and Vortexa must measure the same terminal, crude population and dates, agree within 1.5×**, and have independent imagery corroboration. Freeze the baseline as the mean of the 28 completed days immediately before the event, **from both trackers**, at first evaluation. … **Do not select one tracker after seeing its verdict.**"*

The mechanics draft (`design/HAW19_MEASUREMENT_DRAFT.md` L30) says: *"Each of the 45 days must have **both D_K,d ≥200,000 and D_V,d ≥200,000 barrels/day**, and max/min ≤1.5."* The standing source rule (`AGENTS/HAWK/SOURCES.md` L95) says Kpler is to be used *"**never alone** — pair with Vortexa (agree within 1.5×) + a dark-immune corroborator. Imputes dark tonnage; 2.8× spread vs Vortexa on one asset-week."*

**Verdict: the letter needs BOTH vendors. One is not enough.** The two-vendor agreement is the letter's defence against a single vendor's dark-fleet imputation, and a 2.8× spread between the two has already been observed on one asset-week. A single-vendor letter would be a **new instrument** requiring its own ruling from Will, the same way R1 does. HAWK does not recommend that route. With one vendor, a dark-fleet imputation error cannot be told apart from lost capacity.

## 3. Is TankerTrackers, or any free or near-free source, a substitute? What each one actually publishes per terminal per day

The series the letter needs is **crude loaded per terminal per UTC day, in barrels, realized-only, with archived as-of snapshots, for 73 aligned days.**

| Source | What it publishes (read 2026-09-26) | Daily per-terminal crude loadings? | Token |
|---|---|---|---|
| **Kpler** Flows SDK (python-sdk.dev.kpler.com/resources/flows.html) | `from_installations` filter; granularity `Daily`/`Weekly`/`Monthly`; direction `Export`; `products`; `snapshot_date`; `with_forecast` (**default true**, so realized-only must be set explicitly); unit `BBL` | **Yes, as a documented capability.** Access is untested | VERIFIED (capability, 9/26 fetch) · UNKNOWN (entitlement and price) |
| **Vortexa** Python SDK (per the 9/8 audit) | CargoMovements, loading activity, time filters, API key | Loading events are documented. **Whether per-terminal loadings come on a daily allocation or as whole-cargo lumps is unproven.** The draft forbids inventing a daily allocation (L26) | INFERRED (9/8 read; FAQ 403 on 9/26) |
| **TankerTrackers**, current FAQ (tankertrackers.com/faq/entry/what-products-and-services-are-available, 9/26, undated page) | **Corporate Lite $12,000/yr**: *"Weekly US Exports," "Monthly Exports," "Heads Up! news alerts," "API Access" (country-level aggregations only), "Vessel size class statistics"*. **Corporate $50,000/yr or $5,000/mo**: adds a vessel search engine, satellite vessel identification, Dark Fleet Map and STS alerts. For both corporate plans: *"Port-level data in addition to country-level data"*, with no daily granularity stated | **No daily per-terminal loadings published at any tier.** Port-level data exists on the corporate plans at an unstated frequency. Nothing says whether it is realized-daily or snapshot-archived | VERIFIED (what is published) · UNKNOWN (what "port-level" delivers) |
| TankerTrackers tier article (…/articles/subscription-service-tiers-explained, **dated 2022-11-03**) | PremiumPlus $999/yr (personal use, limited granularity) · Corporate Lite $10,000/yr · Corporate $50,000/yr | — | ⚠️ **SUPERSEDED on two counts.** Search-layer snippets from tankertrackers.com say PremiumPlus is *"no longer offered to new subscribers"* (INFERRED; the register page returned 403), and the current FAQ prices Corporate Lite at **$12,000**, not $10,000 (VERIFIED). **The draft's $999 and $10k cells are wrong today** |
| **IMF PortWatch** Daily Port Activity (free) | Daily port calls plus import/export volume estimates in **metric tonnes**, from AIS draft changes, split by vessel type (tanker is one class, not split crude vs products), at **port** level, updated weekly on Tuesdays | No. It is **port, not terminal**; **tanker, not crude**; and **AIS-only**. FALCON's own watcher (`AGENTS/FALCON/scripts/kharg_loadings_watch.py` L13) records PortWatch as *"~90%+ BLIND to Kharg's true throughput"* | INFERRED (search-layer; the page 404'd to WebFetch) · VERIFIED (FALCON's caveat) |
| **Bruegel** Russian crude oil tracker (bruegel.org/dataset/russian-crude-oil-tracker) | Six named Russian ports; 4-week moving averages and monthly figures in Mt; **last updated 2024-02-12** | No: monthly/4-week, Russia-only, stale | VERIFIED (9/26 fetch) |
| Vendor numbers reprinted in the press (Reuters/Bloomberg quoting Kpler or Vortexa) | Monthly or weekly levels for the terminals the reporter picks | No: not daily, not archived, selection chosen by the reporter | INFERRED (this is how GATE-FALCON-001 leg 3 was graded) |
| Operator disclosures (Transneft, CPC, Aramco, etc.) | Ad hoc statements, force-majeure notices, occasional monthly volumes | No daily series was found. **This is exactly R1's input**, which is why R1 measures disclosed loss | SEARCH-NOT-FOUND (daily series) |

**Verdict: no free or near-free source substitutes for the series.** TankerTrackers **does not publish** per-terminal daily loadings at any tier, and the cheapest tier HAWK can verify today costs $12,000/yr, not $999. **Do not buy TankerTrackers for this line.** It could only become relevant if a written answer from TankerTrackers showed that its corporate "port-level data" is daily, crude-only and archived, and even then it would be one vendor, not two.

## 4. WQ-296: HAWK's view of PROME's rec ("A as the interim on 9/30; C only on a quote Will judges worth the thesis")

**HAWK concurs, with C restated as "the v2 mechanics on fresh windows" (see C3), not "as written."**

Choosing A loses nothing that cannot be recovered later, apart from one thing. **The one thing A cannot recover is a *measured-throughput forecast on the Oct 1 → Dec 22 window*.** No letter can be registered after its window opens, whichever option Will picks, and C cannot be ready before 10/01 in any case. So that window is lost to all three options equally. Choosing A does not cause the loss.

The underlying data is largely **recoverable**. Kpler documents a `snapshot_date` (as-of) parameter, so October–December loadings can probably be reconstructed as they stood at the time and used as an **annotation** of HAW-22's outcome after purchase. That is INFERRED: Vortexa's as-of history is unproven.

What A **does** carry is a known blind spot: it can CONFIRM wrongly if a terminal is destroyed and never declared. That is Transneft's base case. Its score cannot be rewritten afterwards, because later evidence is an annotation only. Will should take A knowing that risk, which is written on the row's face.

B carries no such risk but leaves the quarter unforecast. A registered R1 also does not block a later v2 letter: the two claims measure different objects (declared loss vs measured throughput) and can run side by side.

**What a quote must cover to be worth anything.** It must cover **both** vendors and, per vendor, all of the following:
- **(i)** crude-only **exports by installation** (terminal), at **daily** granularity, **realized-only** (Kpler `with_forecast=false`), in barrels or with a stated tonne→barrel basis;
- **(ii)** the full terminal set of both theaters: Russian Baltic, Black Sea, Arctic and Pacific crude terminals, plus the Gulf and Red Sea crude terminals. Russian examples are Primorsk, Ust-Luga, Novorossiysk-Sheskharis, CPC and Kozmino; Gulf and Red Sea examples are Ras Tanura, Ju'aymah, Yanbu, Kharg, Jask, Basra and Mina al-Ahmadi. The final list is frozen from the inventory, so the quote should cover every installation in those regions, not a picked subset;
- **(iii)** **history back to at least 2025-10-31**, so the CPC 29 Nov 2025 fixture (28 days before, 45 days after) and one Gulf control window can be built;
- **(iv)** **point-in-time / as-of (snapshot) retrieval** of historical data, not only the current revised series;
- **(v)** **API or bulk export rights** for one named research user, not a web UI only;
- **(vi)** documentation of **how loadings are allocated to days** (loading completion date vs spread over the loading duration) and which records are **estimated (dark-imputed) vs observed**;
- **(vii)** a term running at least to **the new observation cutoff plus resolution** (roughly 3 months beyond the fresh window's close), with the price of the shortest such term and of any trial.

A quote that fails (i), (iv) or (vi) buys data the letter cannot use, whatever the price.

## 5. Quote-request text (for Will or PROME to send; HAWK sent nothing)

> Subject: Research-seat quote: daily crude exports by terminal (API), with point-in-time history
> We are a small independent research team. Please quote the shortest term (and any trial) for ONE named research user with API access to: crude-oil exports by installation/terminal at DAILY granularity, realized cargoes only (no forecast/predicted trades), for all crude-export terminals in Russia (Baltic, Black Sea incl. CPC, Arctic, Pacific) and the Persian Gulf/Red Sea (Saudi Arabia, Iran, Iraq, Kuwait, UAE), with history from 2025-10-31 and POINT-IN-TIME (as-of/snapshot) retrieval of historical values. Please also state: (1) how a cargo's volume is assigned to a calendar day; (2) how estimated or dark-fleet-imputed volumes are flagged; (3) units and conversion basis; (4) usage and licensing terms for internal research.

Send one copy to Kpler (sales/contact form) and one to Vortexa (contact form). The same text serves both. A TankerTrackers question is optional and only worth asking if Will wants the substitute ruled out in writing: *"Does Corporate's port-level data include daily crude loadings per terminal, and is it archived point-in-time?"*

## Disposition in HAWK's own record

KB-HAWK-413 (this finding). board_log row for the consumed packet. SCRATCH and NEXUS_BRIEF are stamped. The v2 letter's throughput leg is **NOT deleted.** It stays in `design/HAW19_MEASUREMENT_DRAFT.md` as the letter C would use and is declared **CANNOT-FIRE** under WQ-298 until Will's pass.

```
COMPLETION — HAWK · 2026-09-26 14:5x ET · spawn prome-1d (WQ-298/L498 Tier 1)
STATUS: DONE
CHANGED: this memo; AGENTS/HAWK KB-HAWK-413, board_log, SCRATCH, NEXUS_BRIEF, STATUS; PROME packet -> inbox/processed
RESULT: Line 2 = Kpler AND Vortexa (the letter needs BOTH, L18 verbatim), quote NOT requested (no send found; C2). No free/TT substitute: TT publishes no daily per-terminal loadings at any tier; cheapest current tier $12k (FAQ 9/26), $999 PremiumPlus closed to new subs. Concur A on 9/30; C = v2 on FRESH windows, never "as written" (C3)
GAPS: Vortexa FAQ 403, PortWatch 404 (INFERRED from search layer); TT "port-level data" frequency UNKNOWN; Will-sent quote off-repo SEARCH-NOT-FOUND
WILL_NEEDS: WQ-296 A/B/C by 9/30; whether to send the §5 quote request (external send)
FOLLOW-UP: PROME fix rank-1 heading "or"->"and", WQ-300 "quotes outstanding", TT price cells; HAWK registers HAW-22 same session if A
```
