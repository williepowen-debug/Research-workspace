---
signal_id: SIG-W-20261002-009
date: 2026-10-02
timestamp: 2026-10-02T14:40:09Z
time_dispatched: 2026-10-02T14:40:09Z
timestamp_note: stamped from the system clock at write, not typed
source: Will-Telegram
origin: ["Will via Telegram 2026-10-02 14:39Z: screenshot of @zerohedge headlines '*MACRON: WILL RELEASE UP TO 100 MILLION BARRELS' (10:00 AM 10/2) quoting '*MACRON: G7 DECIDED TO RELEASE DIESEL AND CRUDE STOCKS / ...OVER 4 MONTHS' (~40m earlier)", "NBC News 2026-10-02 10:22 ET 'G-7 countries to release up to 100 million barrels of diesel and crude oil reserves'", "Bloomberg 2026-10-02 'G7 to Release Up to 100 Millions of Barrels of Diesel and Oil' (headline only); Newsquawk headline", "WALTER fetch.py 10:39 ET"]
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
cluster_secondary: IRAN_HORMUZ
entities: ["G7", "Emmanuel-Macron", "IEA", "Scott-Bessent", "US-diesel-export-ban", "CLX26", "BZZ26", "HOX26", "RBX26", "USO"]
confidence: 0.92
confidence_language: "confirmed"
signal_type: catalyst
safety_net: clear
verdict: "G7 decided (Macron, after a G7 videoconference 10/02; NBC, Bloomberg) to release up to 100M bbl of diesel + crude over 4 months, with a substantial diesel release in the first 20 days; IEA-coordinated. Split, country volumes and whether the US dropped its export-ban threat NOT published. 10:39 ET: WTI Nov $88.71 (-4.5%), ULSD Nov $4.39 (-5.3%), USO $142.85."
precedence: IMMEDIATE
action: ["BRENT"]
info: ["HANS", "HAWK", "HENRY", "CARL", "TERRY", "RED", "PROME"]
dispatch_note: "State change on SIG-W-20261002-002 (proposal -> G7 decision); same recipients. Corrects -002's 'fully rejects' object (EU rejects the BAN). Held-position line: USO Oct-09 $150 call, ~$7 OTM; TERRY info, exposure only. Will-originated (Telegram 4861). CARL, RED, TERRY, PROME pull-complete."
---

# G7 DECIDED: up to 100M bbl of diesel + crude released over 4 months, diesel front-loaded in 20 days (Macron); oil −3–5%; US ban threat status unknown

**Short version:** This morning's French *proposal* (`-002`) became a **G7 decision**. French President **Macron**, after hosting a G7 videoconference, said the G7 **decided to release diesel and crude stocks: up to 100 million barrels over four months**, with **"a substantial diesel release within the first 20 days"** (NBC 10:22 ET; Bloomberg; Newsquawk; Macron headlines on zerohedge at ~09:20 and 10:00 ET, the screenshot Will sent). **Trump:** *"Europe has just agreed to release a massive amount of their heavily stocked Diesel Oil. The process will begin immediately."* The release is coordinated by the IEA (NBC).

| Contract | 10:39 ET | Change | vs `-002` pre-open |
|---|---|---|---|
| WTI Nov (CLX26) | **$88.71** | −4.5% | $89.23 |
| Brent Dec (BZZ26; fetch identity UNKNOWN) | **$98.99** | −3.3% | ~$99.69 |
| ULSD Nov (HOX26) | **$4.39** | **−5.3%** | $4.53 |
| RBOB Nov (RBX26) | $3.23 | −5.0% | $3.26 |
| USO | **$142.85** | −4.8% | — |

## What is and is not settled
- ✅ **Settled (multiple outlets, head of state on record):** the G7 agreed to release up to 100M bbl of diesel + crude over 4 months, front-loaded on diesel within 20 days.
- ❌ **NOT settled:** the **diesel/crude split** and **per-country volumes** (not published); **whether the US dropped its diesel export-ban threat**. NBC finds no such commitment, and Bessent: US stakeholders *"should not be left carrying the burden of a global diesel shortage."* EU countries had asked for that commitment as a condition (`-002`); **whether they got it is unknown.**
- 📌 **Correction to `-002`:** the "EU **fully rejects**" phrase that `-002` killed as unattributed appears in NBC as the EU *"fully rejects any **ban** on diesel"*. **The rejection is of the export BAN, not of the release.** `-002` was right not to carry "EU rejects the US demand"; the phrase's object is now identified.
- Size vs US ask: the US asked for 120M bbl over 180 days (Al Jazeera) or 100M bbl within 20 days (Reuters relay). **"Up to 100M over 4 months, diesel front-loaded" sits between them.** WALTER does not grade which ask it satisfies.
- For scale: IEA members approved a **400M bbl** crude release in **March** (NBC).
- US retail diesel: **$6.37/gal** (NBC) vs **$6.53** record (Al Jazeera, last week). Benchmarks not named; two figures, not reconciled.

## Requested action
**BRENT:** carry the decision against VLO-HELD-01 leg B1 (does it retire the export-ban leg, or does the ban threat stand?) and against your 10/02 EU-taskforce row, and size the diesel-first release against the crack. HANS, HAWK, HENRY, CARL, RED, PROME: information. **TERRY / exposure only:** Will's **USO Oct-09 $150 call**. USO is **$142.85 at 10:39 ET (−4.8%)**, about **$7 below the strike** with five sessions to expiry. The order is Will's; this is not a trade proposal.
