# DEWEY → WALTER · handoff · DR-4 European energy aggregate baseline

**State:** NEW · **From:** DEWEY · **Date:** 2026-08-12
**Report (canonical):** `AGENTS/DEWEY/output/2026-08-12_dr4-european-energy-baseline.md`
**Flag:** `REQ-DEWEY-20260731-004` · **INDEX row:** appended (48 rows / 48 files, reconciles clean, 8-field)
**⚠️ Second handoff from me today** — the first is `2026-08-12_from-DEWEY_c3-masking-duration-base-rates.md` (CARL C3). Two separate reports, two separate rows.

**Stubs written by me at write-time (constrained-B):** BRENT *(action)* · DAEDALUS *(org question)* · AEOLUS, HANS, CARL, MARCO *(info)* — all `AGENTS/<X>/inbox/2026-08-12_from-DEWEY_dr4-european-energy-baseline.md`, except DAEDALUS at `..._dr4-europe-gas-org-question-evidence.md`.

---

## ⚠️ Ledger item first: this commission's framing premise was wrong

DR-4's scope line reads *"Explain the year's central puzzle: THREE-PLUS impaired channels with **TTF at €59 FALLING**."*

**The level was exactly right — TTF settled €59.07 on 7/31, the day you wrote it.** The **direction is inverted**: TTF rose **+38.1% across July** (€42.78 → €59.07), is **+83.3% YoY**, and on 7/31 sat **five sessions off a 52-week high of €63.58** set 7/24. It closed **€60.49 on 8/12**, in the top 5% of its 52-week range.

**So the puzzle the commission exists to explain does not exist.** Impaired channels + rising price is coherent, and I record an explicit negative: **no evidence the price reflects complacency about storage.** The same "TTF ~€59 and FALLING" line is carried in DEWEY's own `CONTEXT.md` §Geopolitical/energy sourced to BRENT 7/31 — I have flagged it to BRENT and will correct my own CONTEXT copy; **BRENT's surface is theirs to fix, and I have edited nothing of theirs.** Worth a ledger note since a directional error in a scoping premise propagates into every downstream consumer of that commission.

## One-paragraph summary for the `research-output` signal

**EU gas storage is at a five-year low for the date — 59.32% full (670.4 of 1,130.2 TWh, gas day 8/11), 13.0pp below 2025 and 14.3pp below 2022**, and 19.05% of annual consumption vs 21.71% in 2022. It is the **second consecutive undershoot** (2025 peaked at 83.2% vs 95-99% in 2022-24). **Europe will not refill to target:** measuring pace from Aug-11 to each year's actual peak and applying it over the 87-day median window, 2026 lands **77–80%**; **90% requires 1.49× the best rate of the last four years**, and even the **80% deviation floor is a dead heat with the 2022 crisis maximum** (2.687 TWh/d needed vs 2.684 best) sustained 87 straight days. The binding rule is 90%, **flexible 1 Oct – 1 Dec**, with up to 10% deviation [Council of the EU 2025-07-18, extended 2025-27]. **The impairment is measured at the receiving end: EU LNG send-out is −20.4% YoY at only 38.3% utilisation with 4,896 GWh/d idle — the constraint is cargoes, not regas** — and the YoY send-out gap alone is ~69 TWh ≈ 6.1pp of storage.

**Confidence:** High on storage/LNG/price arithmetic (GIE AGSI+/ALSI+ and ICE TTF, all primary, fully reproducible). The forward projection is a **continuation estimate on n=4 seasonality — medium**, stated as a range, not a forecast.

## ⚠️ PARTIAL DELIVERY — do not close this row as fully served

**4 of 6 legs unmet or partial.** Channel-by-channel pipeline attribution (Norway/Algeria/Azeri/Russian residual) **NOT ANSWERED** — ENTSOG is reachable (HTTP 200) but point-keyed and needs a border-point→channel mapping **build**, not a pull. Per-channel impairment (Qatar FM replaced share, Greenstream post-Mellitah, Egypt post-Damietta) **not quantified at primary**. Rhine logistics leg **not pulled**. Demand side is **normalisation only** — AGSI's `consumption` is a static annual reference, not observed demand. **The two legs that ARE answered are the decision-critical ones, but this does not discharge the "one ledger" ask.** Your call whether that reopens as a follow-on.

## Process items for your ledger

1. **New keyless primaries worth knowing fleet-wide:** GIE **AGSI+** (`agsi.gie.eu/api/data/eu`) and **ALSI+** (`alsi.gie.eu`) — free, no API key, daily, operator-reported, clean multi-year history. Five years of EU storage + LNG in ~10 calls.
2. **Silent-failure class for BACKLOG:** AGSI/ALSI return **HTTP 200 with `"total":0, "data":[]`** on a malformed query — a silent empty, not an error. **Check `total` before trusting a result.** Same shape as `[[finding_partitioned_source_returns_stale_window_at_200]]`.
3. **Three errors caught in-run**, all logged in the report: projecting injection to the *regulatory* date rather than the *physical* storage peak (storage turns to withdrawal before Dec 1); mixing two window lengths in the headline pace ratio; and **treating AGSI `consumption` (annual TWh) as a daily GWh flow** and building a supply/demand balance on it — caught only because the value was *identical* across 2024/25/26. That last one is the **same class** as the H.8 $M-vs-$B error in today's C3 run: two fields whose magnitudes are close enough that the wrong unit still looks sane.
4. **Build candidates logged to BACKLOG, both Will-gated, neither built:** `gie_pull.py` (AGSI/ALSI wrapper — highest value-to-effort in this domain) and `entsog_flows.py` (the channel mapping — higher value, real maintenance debt).

— DEWEY
