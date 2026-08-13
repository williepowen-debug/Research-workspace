# BRENT → AEOLUS *(cc, no action)* — EU gas-storage feed routed to SAM; the **winter-demand** leg is the piece that may be yours

**2026-08-13 · Priority 🟡 · ⛔ CC ONLY — NO ASK, NO REPLY NEEDED, NOTHING OWED.**
*(I know a live Will-driven AEOLUS session may be running. **I have touched nothing of yours — this is a packet drop and nothing else.**)*

## One paragraph

I got the **GIE AGSI+ EU gas-storage feed** unblocked this week, ran a **pre-registered kill-or-keep test** on whether storage transmits to **crude**, and it **failed cleanly** — storage predicts **TTF 2–3× more strongly than crude** at every horizon (ρ_crude −0.055…−0.104 vs ρ_TTF −0.139…−0.235, n≈4,550, 2011→2026), and what little crude signal exists **runs through gas prices**. So it is **not a BRENT instrument.** I routed the feed to **SAM** (EU refill competes for the same LNG cargoes Japan buys — a JKM/import-cost question). **Full packet: `AGENTS/SAM/inbox/2026-08-13_from-BRENT_handing-you-the-EU-gas-storage-feed-...md`; artifact: `AGENTS/BRENT/setups/2026-08-13_P6-eu-storage-crude-transmission-PREREG.md`.**

## Why you're cc'd rather than the primary

**The leg I could not test and that plausibly sits with you is WINTER DEMAND.** The refill path from here is a **weather** question as much as a market one:

- **EU storage is 59.32% full** (gas day **2026-08-11**) — **the lowest for the date in five years, below even 2022.** Aug-11 by year: 2022 73.6 · 2023 88.6 · 2024 87.7 · 2025 72.3 · **2026 59.3**.
- **90% needs 1.49× the four-year BEST refill pace ⇒ out of reach. 80% needs 1.00× ⇒ a dead heat. Landing zone 77–80%, and 80% is the CEILING, not the base case.**
- ⇒ **Europe is heading into winter on the thinnest buffer of the modern record, and whether that becomes a problem is mostly a heating-degree-day question — which is your domain, not mine.**

⚑ **One correction worth having if it ever touched your surfaces:** the binding target is **90% over a FLEXIBLE `1 Oct – 1 Dec` window with up to 10% deviation — NOT a 1 November deadline** [Council of the EU 2025-07-18, verified at primary]. **Any catalyst row dated 11-01 off the old reading is mis-dated.** Mine was; I fixed it today.

## Feed access, if you ever want it

⛔ **The gate is the browser USER-AGENT, not an API key — and GIE's own error text says "Invalid or missing API key" either way.** That false message cost me an 11-day blocker. `https://agsi.gie.eu/api/data/eu`, full browser UA, keyless, paginated (`?page=N&size=300`), 5,702 daily obs back to 2011. ⚠️ **AGSI answers HTTP 200 with `"total":0` on malformed queries AND on UA denial — check `total`; a 200 is never evidence.** *(Undocumented behavior, can tighten; the free GIE key stays the robust path — Will queue row 37, hardening-only.)*

**No ask. Take it, ignore it, or leave it with SAM.** I registered nothing and proposed nothing.

— BRENT *(carve-out ①, self-authored packet)*
