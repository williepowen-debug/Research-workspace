---
signal_id: SIG-W-20260910-007
date: 2026-09-10
timestamp: 2026-09-10T15:10:06Z
time_dispatched: 2026-09-10T15:10:06Z
source: WALTER
origin: "Will-directed full Iran primary sweep 9/10; owner ledgers read first"
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
precedence: IMMEDIATE
action: ["FALCON", "BRENT"]
info: ["HAWK", "SAM", "HENRY", "LIQUID", "CARL", "RED", "PROME"]
entities: ["Hercules-Star", "New-Andros", "Peninsula", "Dubai", "Al-Faw", "Iraq", "Basra", "UKMTO", "IRGC", "Anduril", "Dive-LD", "VX-FALCON-CASUALTY-01", "EXIT_PROTOCOL"]
confidence: 0.85
confidence_language: reports
signal_type: catalyst
resources: 1
safety_net: clear
word_count: 340
verdict: "Two non-Iranian hulls hit 9/9: Hercules Star struck at the Dubai anchorage (1 dead, 1 missing) and VLCC New Andros ablaze off Al-Faw — neither in FALCON's ledger; D→85 trigger (c) adjudication owed"
narrative_channel: centcom
confidence_note: "observation 0.85 (operator statement, UKMTO, Iraqi officials, multi-wire) / rung-trigger interpretation 0.50 — anchorage-vs-in-port is the owner's letter to read"
---

# Two non-Iranian hulls hit 9/9: Hercules Star struck at the Dubai anchorage (1 dead, 1 missing) and VLCC New Andros ablaze off Al-Faw — neither in FALCON's ledger; D→85 trigger (c) adjudication owed

## Signal and data

1. **Hercules Star** — Gibraltar-flag oil-products tanker, 7,998 dwt, operator Peninsula: struck **9/9 at the Dubai anchorage, ~44 km off the UAE coast**, apparent drone; **one seafarer killed, one missing**, all others accounted for, hull damage (Peninsula statement, carried by Al Arabiya, The National 18:47 and Maritime Executive 9/9). ⚠️ **Not in `AGENTS/FALCON/domain/vessel-incidents/VESSELS.tsv` (29 rows, last VI-2026-0029) nor `domain/casualties/CASUALTIES.tsv` as of FALCON's 9/8 23:4x ET record.** This is a hull struck IN A GCC ANCHORAGE one day after the IRGC's Kuwait/Bahrain in-port threat — the class FALCON's rung trigger (c) *"in-port GCC hull hit"* was written for; whether an anchorage satisfies the letter is FALCON's call, not WALTER's. Civilian-seafarer death: the casualty ratchet's RATE-STEP is already LIT; the CLASS-STEP (MILITARY_US / GCC / COALITION) does NOT fire on it.
2. **New Andros** — Panama flag; Maritime Executive gives 302,477 dwt (a VLCC), The National calls it a fuel-oil products carrier — **type conflict stated, not resolved**. UKMTO: struck by an unknown projectile **28 nm SE of Al-Faw, Iraq**, crew safe, no environmental impact; MarEx / Iraqi port officials to Reuters: **set ablaze, hull damage**, investigation open. Not in `VESSELS.tsv`. Iraqi export approaches (Basra/Al-Faw) — the Iraq crude-export leg, not Hormuz proper (which sea? Persian Gulf, Iraqi waters — GATE 2 needs a SINKING or mine; this is neither).
3. **IRGC 9/9 claims:** "extensive damage" to two US warships (CENTCOM: *"completely FALSE"*), eight tankers, ten other vessels; "10 tankers turned back"; and an announced **map of an expanded off-limits maritime zone** — the PERIMETER-EXTENSION question the anchor's 8/22 declaratory guard kept open is now a stated intent (declaratory until enforced). IRGC 9/8 claims seizure of a US Anduril Dive-LD UUV at the strait entrance — US no comment, CLAIM-ONLY.
4. **Riesco (from SIG-001, now corroborated):** a Reuters-captioned wire image shows the hull *"burns as it sinks"*; TankerTrackers names the five by IMO. FALCON's VI-2026-0028 still reads AFLOAT.
5. **Context, tape:** Brent settle $101.21 (+3.4%) 9/9; BZX26 $104.70 (+3.45%) intraday 9/10. Full sweep record: `AGENTS/WALTER/research/2026-09-10_iran-full-sweep.md`; anchor re-verified 9/10.

## Relevance and owner action

FALCON: add VI rows for Hercules Star and New Andros and a CASUALTIES.tsv row (civilian seafarer, Dubai anchorage 9/9); adjudicate D→85 trigger (c) on the anchorage hit and record the Riesco sinking on VI-2026-0028 / VX-FALCON-SUNK-01; the 9/14 re-mark is the same touch. BRENT: Iraqi export-approach exposure (Al-Faw / Basra) and the Dubai bunkering/products leg — no supply loss is claimed here.

## Sources

- https://english.alarabiya.net/News/gulf/2026/09/09/seafarer-from-oil-products-tanker-killed-in-incident-off-dubai-peninsula-says
- https://www.thenationalnews.com/news/gulf/2026/09/09/us-and-iran-hit-tankers-as-six-month-war-escalates/
- https://maritime-executive.com/article/iran-threatens-tankers-in-kuwait-and-bahrain-as-irgc-responds-to-us-attacks
- https://www.aljazeera.com/news/2026/9/9/has-iran-captured-an-unmanned-us-submarine-what-we-know
- https://x.com/TankerTrackers/status/2097452671867187400
- AGENTS/FALCON/domain/vessel-incidents/VESSELS.tsv + domain/casualties/CASUALTIES.tsv (read 9/10 ~15:1xZ)

Delivery: written_not_delivered_pending_push. Recipient consumption unverified.
