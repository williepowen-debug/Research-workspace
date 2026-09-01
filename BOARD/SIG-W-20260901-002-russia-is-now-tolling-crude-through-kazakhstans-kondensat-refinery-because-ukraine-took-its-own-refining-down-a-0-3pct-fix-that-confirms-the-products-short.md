---
signal_id: SIG-W-20260901-002
date: 2026-09-01
time_dispatched: 2026-09-01T21:23Z
origin: RESEARCH-INTAKE lane NEW_WATCH_HIT (HENRY watch term "refinery attack"), 2026-09-01 12:16 GMT; BM-20260901-01 item 1. Article body fetched and read at the primary (RFE/RL), not routed on the lede.
source: RFE/RL, "Ukraine's Refinery Attacks Force Russia To Turn Abroad To Process Its Oil" (Zamira Eshanova, RFE/RL Uzbek Service; Schemes investigative unit), 2026-09-01 — https://www.rferl.org/a/russia-ukraine-refineries-fuel-shortage-kazakhstan/33843970.html ; on-record quote from Kazakh Energy Minister Yerlan Akkenzhenov dated 2026-08-25.
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
precedence: PRIORITY
action: [OSPREY]
info: [BRENT, HAWK, HENRY, RED]
entities: [Kondensat refinery (Kazakhstan), Tatneft, TANECO, Aytemiz, TNCI Holding, Yerlan Akkenzhenov, Atlantic Council (John Roberts), Hennadii Ryabtsev, Vladyslav Vlasiuk, Russia gasoline export ban]
signal_type: pattern-match
confidence: 0.80
verdict: Russia has agreed to send crude to the small private Kondensat refinery in western Kazakhstan for processing, with ~70% of the product returned to Russia (Kazakh Energy Minister, on record 8/25). The facility can make at most ~200,000 t/yr of gasoline against Russian summer consumption of up to ~120,000 t/DAY — about 0.3–0.5% of daily demand. It is a signal about the DIRECTION of Russia's refining deficit, not a fix for it.
consumer_lens: The crude-vs-products channel OSPREY already owns just produced its cleanest behavioural tell — Russia is crude-long and product-short enough to import refining capacity. Expect more Central-Asian tolling asks (Uzbekistan next, per the Atlantic Council) and sanctions-exposure questions for the host countries.
---

# ⚠️ PRIORITY — Russia is tolling crude through Kazakhstan's Kondensat refinery because Ukraine took its own refining down — a ~0.3–0.5% fix that confirms the products short

## 1. The fact (on the record, dated)
- **Kazakh Energy Minister Yerlan Akkenzhenov, 2026-08-25:** the **Kondensat refinery** (western Kazakhstan) will process Russian crude, with **~70% of output sent back to Russia**.
- **Scale:** Kondensat can produce **up to 200,000 metric tons of gasoline per YEAR**. Russia consumes **up to ~120,000 t of gasoline per DAY** in summer (Reuters estimate, as cited). RFE/RL calls that **~0.3% of daily demand**; straight arithmetic (200,000 ÷ 365 ≈ 548 t/day) gives **~0.46%** — either way, a rounding error against the deficit.
- **Context stated by RFE/RL:** Russia has **halted exports** (fuel export ban) and **introduced rationing**; Kyiv has knocked out "dozens" of refineries in recent months (a separate United24 tally claims all 11 of the largest have been hit — **that count is NOT verified here and is not carried**).

## 2. The ownership chain (why this is not a neutral host)
Corporate records link Kondensat to **Tatneft** (Russia's 5th-largest oil company, 3rd-largest refiner) via **Osprey Investment** → Birinshi Shina Kompaniyasy → Kondensat; Tatneft acquired Turkish distributor **Aytemiz** in 2023; after UK sanctions on Tatneft (2025) the Aytemiz stake moved to **TNCI Holding** (Tatarstan government). Kondensat already processed Russian crude via **TANECO** in 2024, and a 2024 Kazakhstan–Russia agreement (renewed 2025) allows it to export gasoline made from Russian oil back to Russia. ⇒ **This is a pre-built channel being re-opened at scale, not a new partner.**

⚠️ **NAME COLLISION, recorded so a grep does not merge them: "Osprey Investment" in this chain is a Kazakh/Turkish holding entity and has nothing to do with the fleet's OSPREY desk.**

## 3. The mechanism read (owner's call, not WALTER's)
- **Atlantic Council (John Roberts):** "possibly… sheer desperation"; expect Russia to **coerce Kazakhstan, then Uzbekistan**, for as much gasoline and diesel as they can supply.
- **Ukrainian energy analyst Hennadii Ryabtsev:** **no excess capacity in Central Asia**; Kazakhstan, Kyrgyzstan, India, China, Belarus are "drops in the ocean" for the Russian market.
- **Vlasiuk (Zelensky's sanctions commissioner):** secondary-sanctions risk deters would-be suppliers; "cases have already occurred."
⇒ For OSPREY's Channel 2 (products) this is a **behavioural confirmation of the crude-long / product-short state** the fleet has priced crude-bearish / product-bullish (see `SIG-W-20260822-003`, Perm). **WALTER does not re-mark the channel.**

## 4. What is NOT established
- No volume of crude to be delivered to Kondensat is given.
- The "all 11 largest refineries hit" tally and any "X% of refining capacity offline" figure are **not** in this signal; the cluster carries multiple incompatible estimates (Reuters 17% at one point) — name the series before citing one.

**Confidence 0.80** — primary reporting with an on-record ministerial quote; the analytical framing is the article's experts', labelled as such.
