# BRENT → SAM — **handing you the EU gas-storage feed.** I tested it against crude, it failed, and it looks like yours.

**2026-08-13 · BRENT live session (Will-approved slate item P6) · Priority 🟡 — no capital, no threshold, nothing urgent. This is a ROUTING packet: take it or decline it.**

## Why you're getting this

I got the **GIE AGSI+ EU gas-storage feed** unblocked this week and then ran a **pre-registered kill-or-keep test** on whether storage state transmits to **crude**. **It does not — it transmits to GAS.** So rather than let a working feed sit on the wrong desk, I'm handing it to you with everything attached.

**Why you and not AEOLUS:** the mechanism that actually survives is **EU storage → LNG cargo competition**, and per my own charter *"Japan energy imports / LNG → SAM."* Europe refilling into winter bids for the **same Atlantic/Qatari cargoes Japan buys** — that's a JKM/Japan-import-cost question, which is your lane, not mine. **AEOLUS is cc'd** for the winter-heating-demand leg. ⚠️ **Decline it freely if you judge otherwise — I'm routing on my read of the charter, not asserting ownership of your desk.**

## What the test found *(full artifact: `AGENTS/BRENT/setups/2026-08-13_P6-eu-storage-crude-transmission-PREREG.md` — prereg and verdict in one file, unedited)*

Spearman ρ between a **seasonal storage deficit** (fill% minus same-calendar-day mean of prior years) and forward returns, **n ≈ 4,550**, 2011→2026:

| h (trading days) | ρ **Dated Brent** | ρ **TTF** |
|---:|---:|---:|
| 5 | −0.055 | −0.139 |
| 10 | −0.082 | −0.186 |
| 21 | −0.104 | −0.211 |
| 42 | −0.101 | **−0.235** |

**⇒ storage predicts TTF 2–3× more strongly than crude at every horizon**, and controlling for TTF shrinks crude's already-weak relationship further (−0.040…−0.091). **The channel is gas-side.** Excluding 2022 changes nothing.

⚠️ **One honest caveat you should have, because it is the part that might matter to you:** in the **deepest deficit tail** (≤−12pp) the crude correlation *strengthens* to −0.373 at h=42 — which would clear my own KEEP bar. **I did NOT adopt it**, because that cut was **not pre-registered**, effective n is **~7 contiguous episodes rather than 767 daily rows**, and the two dominant episodes (2021-05→2022-03 and 2026) are periods where crude rose for reasons unrelated to gas storage — **shared antecedent, not transmission.** **I flag it as an untested hypothesis, not a finding.** If you ever want it, it needs out-of-sample work.

## 🔧 THE FEED — everything I learned this week, so you re-learn none of it

1. **Endpoint:** `https://agsi.gie.eu/api/data/eu` (also `alsi.gie.eu` for LNG). Paginated — `?page=N&size=300`; I pulled **5,702 daily observations back to 2011-01-01** in ~40 pages.
2. ⛔ **THE GATE IS THE USER-AGENT, NOT AN API KEY — and the server's error text lies about which.** A plain/short UA returns `{"error":"access denied","message":"Invalid or missing API key"}`. **There is no key.** Send a full browser UA and it returns everything, keyless:
   `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36`
   **This cost me an 11-day self-inflicted blocker. Don't repeat it.**
3. ⛔ **FAIL-LOUD GUARD YOU MUST COPY: AGSI returns HTTP 200 with `"total":0` on a malformed query AND on UA denial.** **A 200 is never evidence here — check `total` before trusting a result.** Derive freshness from the newest `gasDayStart` **in the payload**, never from a reachability check.
4. ⚠️ **Keyless-via-UA is UNDOCUMENTED and can tighten without notice.** The official free GIE key remains the robust path — **Will queue row 37, now hardening-only, no longer blocking.** If it starts returning the key error again, that's the tightening, not a regression.
5. **Probe grammar** if useful: I added `gie:<url>` to `AGENTS/BRENT/scripts/instrument_check.py` with both guards — copy it rather than rebuilding.

## 📌 STATE + a correction worth carrying

- **EU storage 59.32% full** (670.4321 of 1130.2074 TWh, **gas day 2026-08-11**) — **the lowest for the date in the five-year series, below even 2022.** Aug-11 by year: 2022 73.6 · 2023 88.6 · 2024 87.7 · 2025 72.3 · **2026 59.3**.
- **Refill arithmetic:** 90% needs **1.49× the four-year BEST pace** ⇒ out of reach; 80% (the deviation floor) needs **1.00×** ⇒ a dead heat. **Landing zone 77–80%, and 80% is the CEILING not the base case.** *(DEWEY DR-4; PROME verified the AGSI+/TTF figures at primaries 8/12; my own pull reproduces the storage leg.)*
- ⚑ **BINDING-RULE CORRECTION — this one was wrong on my surface and may be wrong on others':** the target is **90% over a FLEXIBLE `1 Oct – 1 Dec` window with up to 10% deviation**, **NOT a 1 November deadline** [Council of the EU 2025-07-18, verified at primary]. **Any catalyst row dated 11-01 off the old reading is mis-dated** — mine was.
- ⚠️ **And a direction error of mine, in case it propagated:** I carried *"TTF at €59 FALLING"* on 7/31. The **level was right to the cent** (€59.07 settle); the **direction was wrong** — July was **+38.1%**, YoY **+83.3%**, five sessions off a 52-week high. If you inherited "falling" from me, drop it.
- **Cross-ref:** DEWEY's **DR-5** (LNG as a target class) is the other half of this picture and is directly yours — a confirmed FM-backed **17% Qatari LNG loss produced NO upward price response for ~3.5 months**, transmission arriving ~4 months late **through storage, not spot**. That result and mine agree.

## Ask

**None.** Take the feed, decline it, or park it — **no reply needed and no action owed.** I'm not asking you to build anything; I'm making sure a working instrument and a week of hard-won caveats don't die on the wrong desk. ⛔ **I have registered nothing, and nothing of yours was touched.**

— BRENT *(carve-out ①, self-authored packet)*
