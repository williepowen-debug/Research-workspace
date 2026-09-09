# OSPREY THESIS — v1.0 (2026-09-08)

**Status: v1.0 — first owner-written version.** Supersedes the v0.1 spinout-seed (2026-07-12) whose staleness banner set a v0.2 due date of **2026-09-05**; this file lands **9/8, three days late — recorded as the hygiene defect the banner said it would be**, not quietly extended. Written after the two dependencies the banner named resolved: HAWK's basis-pair audit landed 9/8 and the export-decline persistence question printed a sixth week (8/25). **Live state is `STATUS.md`; this file is the model.** Falsification lives in `CLAUDE.md` § EXIT RULES (single home; this file only points).

---

## 1. Core thesis

Ukraine's campaign against Russian oil runs through **three parallel, independently scored channels** — not a sequential switch and not a scenario ladder:

1. **Refineries / products.** Strikes on refining capacity degrade Russian *domestic* fuel supply. In the first phase of the campaign (spring–mid-July 2026) this **freed crude for export** — a products/crack story, bearish-to-neutral for Brent.
2. **Crude-export terminals.** Baltic (Primorsk, Ust-Luga, Vysotsk) and Black Sea / Azov (Sheskharis-Novorossiysk, Tuapse, Taman, CPC) loading infrastructure. The Brent-relevant channel *if* barrels actually stop leaving.
3. **Shadow-fleet tankers and the port perimeter.** Kinetic strikes on hulls in the Russian trade — Russian-flagged, "shadow", and (since August) Western-managed tonnage — plus Russia's counter-strikes on Ukrainian-port shipping.

**What the campaign has actually done to world crude (the finding that reorganised the model on 8/20):** it has removed barrels **without destroying any capacity**. No crude-export berth has been confirmed destroyed; every individual halt reversed in 2–7 days. Yet Russian seaborne crude fell from a wartime high of **4.22 M bpd (4-wk to 7/5) to 3.46 (to 8/23), six consecutive weekly falls, ~-760 kbpd** [Bloomberg tanker-tracking]. The mechanism is **deterrence of offtake at the perimeter** (`FLOW-OSPREY-03`): a credible threat at or near a berth → charterers, owners and insurers decline → loadings stop → shore tanks fill → the terminal stops accepting pipeline deliveries → upstream cuts. It is observable at every step except the last and it is **symmetrically fast to reverse**. HAWK's sentence, adopted verbatim so consumers hear one phrasing: **BARRELS DESTROYED = zero; BARRELS NOT SHIPPED = large, rising, reversible.**

**The products side is the durable half.** Refinery runs printed **3.6 M bpd in July and ~3.8 in August** against a 5.3–5.5 norm [EA Analytics via Bloomberg] — roughly **30% below norm on the runs proxy**, which is the canonical refining-offline band (**~30%, 25–35% [EST], KB-OSPREY-029**). Seaborne diesel/gasoil exports ran ~80–150 kb/d in August, ~80% below the seasonal norm [Vortexa via Bloomberg]; producers' diesel exports are banned to 9/30, traders' diesel and gasoline to 1/31/27, jet to end-November. Russia is tolling its own crude through a Kazakh refinery. **This half is not reversible in days; it is reversible in repair cycles of 2–3 weeks per plant against a strike cadence of ~20 refinery hits a month.**

## 2. What prices, and who owns the price

The channel model's market-relevance premise is that **the crude channel prices on Brent and the products channel prices on cracks, and the two must not be merged.** OSPREY owns the *inputs* — strike rows, loading status, the export series as an observable, the offline band — and **BRENT owns every price** (Brent, cracks, freight, floating storage, Urals). A Brent move is attributed by BRENT/FALCON; the 7/23 $100 print and the 9/1 move were Iran-primary, with this theater a named secondary driver at most (theater-attribution guard). The model would be **falsified** by a confirmed physical crude disruption out of this theater that Brent does not reprice (EXIT RULES §2, model-falsification clause) — that has not been tested, because no disruption here has yet been *physical*.

## 3. The diplomatic overlay

On **8/8** a US-brokered understanding had Ukraine agree not to strike **CPC infrastructure** or **non-Russian tankers not carrying Russian cargo, not Russian-owned, not under Ukrainian sanctions**. It removed the campaign's most-instrumented target (the CPC gate, `GATE-OSPREY-001`) by diplomacy rather than attrition, and it is **fragile by construction**: unacknowledged by Kyiv, holding on observed behaviour only, a restraint free to grant and free to revoke. It has survived one clean test (Skiros 8/16 — a non-Russian hull *carrying Russian crude*, the carve-out exercised) and carries one open test (SIREN 9/3 — cargo state unpublished). It **has not been formalised or extended** as of the ~9/8 rung. It also shaped the campaign: since 8/8 Ukraine's perimeter strikes have concentrated on Russian hulls and Russian-trade hulls, and the Russian terminals themselves (Ust-Luga twice, Sheskharis, Taman) rather than CPC.

## 4. What the model has gotten wrong, and what changed because of it

- **OSP-01 FAILED (7/31):** the tanker campaign *did* reach a named Russian crude terminal (Sheskharis) — while this desk's attention sat on the registered CPC gate (LESSONS 5).
- **OSP-05 FAILED on a construct defect (8/20):** a mechanism-enumerating test (destroyed capacity / sustained interdiction) graded 0-of-2 in the week the outcome it was built for arrived by an unenumerated route. **Every N-leg test now carries an outcome-measuring leg**, and `OSP-06` names its instrument at registration.
- **Two ledger-completeness failures found late** (Taman 7/30 after 21 days; the Yanina sinking 8/1 after 38 days): a sweep anchored on a facility list or an object class certifies coverage it cannot deliver. **The Channel-3 instrument is now a dated-window maritime bulletin run first**, before any name query (LESSONS 7, 8).
- **Two label failures (9/2, 9/8):** a DARK mark licensed a ~45%-stale floating-storage figure, and an uncited June table cell travelled as a "May-vintage" Urals discount. **A label is not provenance**; this desk now carries no figure it cannot trace to a KB row.

## 5. Channel state and what to watch (as of 2026-09-08 — `STATUS.md` is canonical)

| Channel | Mark | What would move it |
|---|---|---|
| Refineries/products | **4 🔴** | Up: sustained runs <3 M bpd or an independent >40% offline aggregate. **No downgrade path exists** (OWED-15). |
| Crude-export terminals | **5 🔴** (Will, 8/20, liftings limb) | **No downgrade path exists** — the largest spec hole on the desk. A snap-back print (≥3.9 M bpd, OSP-06's bar) is the evidence a downgrade would need. |
| Shadow-fleet / perimeter | **3 🟠** | Up: a named crude tanker sunk/total-loss, or a war-risk *buyer* pullback (three adjacent withdrawals — MSC, FESCO, the standard war-risk market — none a buyer). |

**The single most important observable is the weekly Bloomberg seaborne-crude print: a seventh week, or the snap-back.** Second: any strike on CPC infrastructure or a non-Russian hull without Russian cargo (the understanding breaking). Third: the September runs print (~4.2 expected) — if it lands, the band's *lower* edge, not its centre, becomes the question.

## 6. Known holes in the model, written down so they are distinguishable from blind spots

- **No downgrade path for any channel** (approved to build; blocked on BRENT+HAWK score semantics).
- **Channel-3 kill letter has no geography qualifier** (Mediterranean strikes on Russian hulls, 9/5-6) — routed, not self-ruled.
- **Gas/LNG** is represented (`VX-OSPREY-GAS-01`, `FLOW-OSPREY-01`) but thinly swept; **vol/credit** transmission (`FLOW-OSPREY-02`) is seeded and has never had an own-theater observation.
- **Druzhba / EU** remains a pointer, not a tracked series.
- The **war-risk rate** is event-driven observable and has printed twice in seven weeks; the TD6 freight proxy is a tripwire, not a level.

## 7. What would change this thesis
→ `CLAUDE.md` § EXIT RULES (v1.0, firmed 7/12; §2 sequencing repair 8/10; §3 attribution clause 8/15; re-read 9/8). Not duplicated here.

## Provenance
v0.1 seeded 2026-07-12 from HAWK's STATUS/SUMMARY/outbox content. v1.0 written 2026-09-08 from OSPREY's own record: `STRIKES.tsv` (98 rows, swept-complete 9/8), `KB.tsv` (KB-OSPREY-001..090), `PREDICTIONS.tsv` (OSP-01..06), the dated `ANALYSIS_*.md` series, and `FLOW-OSPREY-03`. Prior version preserved in git history (`git log -p -- AGENTS/OSPREY/thesis/THESIS.md`).
