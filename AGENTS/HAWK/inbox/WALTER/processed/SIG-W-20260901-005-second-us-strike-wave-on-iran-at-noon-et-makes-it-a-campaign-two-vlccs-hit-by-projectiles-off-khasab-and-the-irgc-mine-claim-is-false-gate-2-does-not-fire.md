> **WALTER handoff — SIG-W-20260901-005** · role: **INFO** · precedence: IMMEDIATE
> Source batch: verify-research return verify-hormuz-0901 ~21:45Z on the 9/1 oil-move sweep (BM-adjacent, not a lane item).
> Move this file to `inbox/WALTER/processed/` when consumed.

---

---
signal_id: SIG-W-20260901-005
date: 2026-09-01
time_dispatched: 2026-09-01T21:30Z
origin: WALTER Tuesday boot verify-research return (rule-9 spawn `verify-hormuz-0901`, ~21:45Z) on the IRGC "supertanker hit two mines" claim surfaced by the 9/1 oil-move sweep; the verify found the second strike wave and the two VLCC hits. Fires the anchor's own re-verify trigger ("a SECOND US strike wave would establish a campaign") — ADDENDUM #23 written to anchors/IRAN_WAR.md at this dispatch.
source: CENTCOM statements 8/31 (mine denial, X 2094411076729262413; Maritime Executive; Dawn) and 9/1 12:00 ET (strikes began; via CNBC, CBS live blog, Xinhua); UKMTO incidents 1952Z + 2000Z 8/31 via MarineLink / Insurance Journal (Bloomberg-Marisks) / Seatrade / Iran International; IRGC claim via Tasnim/PressTV/UPI 8/31 ~04:37Z; AP via KSAT (Aqaba retaliation ~15:27 ET 9/1); Al Jazeera 9/1 + Yahoo/Quartz 13:36 ET + TradingEconomics late mark (Brent path); own fetch.py BZX26 pull 21:14Z. Paywalled/403: Lloyd's List LL1158318, Bloomberg, CNN, war.gov, UKMTO listing — figures from accessible mirrors.
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
precedence: IMMEDIATE
action: [FALCON, BRENT]
info: [HAWK, SAM, HENRY, LIQUID, CARL, RED, PROME]
entities: [CENTCOM, IRGC Navy, Strait of Hormuz, Khasab, VLCC Sidr (Bahri, Saudi flag), VLCC Senegal Prosperity (Sinokor, Liberia flag), Bandar Abbas, Jask, Chabahar, Konarak, Minab, Sirik, Qeshm, Jiroft airport, Camp Titin / Aqaba (Jordan), Brent BZX26, GATE 1 / FAL-01, GATE 2, UKMTO Warning 121-26 / 122-26]
signal_type: catalyst
confidence: 0.85
verify_research_verdict: CORRECTED-FRAMING
corrects: EXTERNAL: IRGC Navy statement via Tasnim/PressTV 2026-08-31 ("noncompliant supertanker struck two naval mines, massive fires, brought to a complete stop") as relayed by UPI, Arab News, OilPrice, cryptobriefing, investinglive and the search-summary layer that fused it with the 8/31 projectile hits. No prior WALTER BOARD signal is corrected.
verdict: (1) The IRGC "supertanker hit two mines" claim is FALSE as a mine event — single-source IRGC, vessel unnamed, CENTCOM on the record 8/31 "No ships have hit mines in the Strait of Hormuz… disinformation", no UKMTO/owner/insurer match, and it PRE-DATES by ~15h the two real hits. (2) The real hits: VLCC Sidr (Saudi, Bahri) at 1952Z and VLCC Senegal Prosperity (Liberia, Sinokor, laden Saudi crude) at 2000Z 8/31, ~17nm off Khasab, "unknown projectiles", crews safe, no fire or pollution reported, weapon unidentified by UKMTO. (3) CENTCOM began a SECOND strike wave on IRGC targets inside Iran at 12:00 ET 9/1 (Bandar Abbas, Jask, Chabahar, Konarak, Minab, Sirik, Qeshm, Jiroft airport per Iranian media; civilian casualties claimed at a Sirik-county wedding). Iran retaliated ~15:27 ET with claimed ballistic missiles at a US Marine camp near Aqaba, Jordan. (4) GATE 2 does NOT fire — no mine detonation, no sinking, losses stay 1. GATE 1 stays FIRM-NEGATIVE on tonight's record — every named target is military/port, no oil-infrastructure claim exists — FALCON adjudicates. (5) Brent Nov (BZX26) $95.22 at the TradingEconomics late mark (+5.23%); path $92 Asia → $94.36 after the strikes → $95.22 after the retaliation; no ICE settle located.
consumer_lens: The pause that broke at Larak is now a CAMPAIGN — two US waves in three days, both answered — and the enforcement clock (IRGC hits on Saudi-linked VLCCs in the southern corridor) is running in parallel. Nothing here is a supply-loss event; it is chokepoint-risk repricing on kinetic tempo, and the one recirculating headline that WOULD have moved a gate is disinformation, denied by the US military the same morning.
---

# 🔴 IMMEDIATE — A second US strike wave on Iran at noon ET makes it a campaign; two VLCCs were hit by projectiles off Khasab; **the IRGC mine claim is FALSE and GATE 2 does not fire**

## 1. 🔴 The kinetic state — verified, dated, in order (all times UTC unless marked)

| When | Event | Status |
|---|---|---|
| 8/30 | US strikes Larak Island IRGC minelaying launchers (CENTCOM) | CONFIRMED (`SIG-W-20260831-001`) |
| 8/31 ~04:37Z | **IRGC via Tasnim: "noncompliant supertanker struck two naval mines… massive fires… complete stop"** — no name, flag, owner, crew | **CLAIM ONLY** |
| 8/31 ~13:12Z | **CENTCOM: "No ships have hit mines in the Strait of Hormuz. This is yet another IRGC attempt to intimidate regional commercial shipping through disinformation."** | **DENIAL, on the record** |
| 8/31 overnight | 8 Iranian ballistic missiles at King Hussein + Al-Azraq (Jordan) — all intercepted; 1 drone at UAE — intercepted | CONFIRMED (Al Jazeera, The Hill) |
| **8/31 19:52Z** | **VLCC *Sidr*** (Saudi flag, Bahri, 300,759 dwt) hit by "unknown projectiles" 16.6nm NE of Khasab; reportedly anchored mid-strait near the Omani coast | CONFIRMED (UKMTO via Marisks/Bloomberg, MarineLink, Seatrade) |
| **8/31 20:00Z** | **VLCC *Senegal Prosperity*** (Liberia flag, Sinokor, laden Saudi crude ex-Juaymah) hit by three projectiles 17nm E of Khasab | CONFIRMED (same set; the AP/PBS "three unknown projectiles" item) |
| **9/1 12:00 ET (16:00Z)** | **CENTCOM: "U.S. forces began striking IRGC targets in Iran"** after the shipping attacks and the Jordan missiles. Iranian media name Bandar Abbas, Jask, Chabahar, Konarak, Minab, Sirik, Qeshm and Jiroft airport (Kerman); Iranian officials claim 2–4 killed and 50+ wounded at a wedding in Bandar Kuhestak (Sirik) | **CONFIRMED at CENTCOM (via CNBC/CBS/Xinhua); target list and casualties = Iranian-media claims** |
| 9/1 ~15:27 ET | IRGC claims ballistic missiles at a US Marine camp (Camp Titin) on Jordan's Aqaba coast; explosions/interceptions seen over Aqaba (AP) | CLAIMED by IRGC; interceptions observed |

Both crews on the VLCCs are safe; **no fire, no casualties, no pollution, no sinking** reported on either hull; UKMTO does not identify the weapon. Nearest earlier casualties: Kuwaiti product tanker *Burgan* (46k dwt — not a supertanker), projectile 2035Z 8/29 (UKMTO Warning 122-26); Warning 121-26 (~8/25, Khasab, projectile, fire extinguished). **Neither is a mined VLCC.**

## 2. ⚖️ The gates — what moves and what does not

- **GATE 2 (confirmed mine detonation on a hull / confirmed hostile sinking): NOT FIRED.** The only mine claim is single-source IRGC, denied by CENTCOM, unmatched at UKMTO, and published ~15h BEFORE the real hits. The real hits are **projectile** strikes with crews safe. **Confirmed hostile-action total losses stay at 1.** *(Registered class: the 7/26 Tasnim mine claim — "five outlets relaying one IRGC-linked channel is not corroboration" — third instance; the retelling fused it with the Khasab hits within hours.)*
- **GATE 1 (FAL-01, production/export infrastructure): FIRM-NEGATIVE on tonight's record.** Every named 9/1 target is a port, naval base, airport or IRGC site; **no oil-terminal, field or processing claim exists anywhere in the wires** — but the target list is Iranian-media-sourced and **FALCON must adjudicate it against CENTCOM's own release** (war.gov 403'd to this box). The Kharg AI-video guard stays live (Trump re-posted it).
- **The anchor's own trigger FIRED:** *"a SECOND US strike wave (would establish a campaign)"*. **The pause that broke at Larak on 8/30 is now a campaign: two US waves in three days, each answered by Iranian missiles at Jordan.** ADDENDUM #23 written.
- **FALCON's owed kinetic-RESUMPTION re-mark** (its own 8/31 STATUS: "plainly owed… a full-session judgment") now has its second data point.

## 3. 📉 The tape — named contract, dated path, no settle
Nov Brent (**BZX26**): Mon close ~$88–90 → **$91.44 (05:00 GMT) / $92.31 (08:45 GMT)** on the tanker hits + Trump "hit them hard" → **$94.36 (+3.8%) at 13:36 ET** after CENTCOM's noon statement (WTI Oct $89.46 +4.3%) → **$95.22 (+5.23%) TradingEconomics late mark** after the Aqaba retaliation. Own `fetch.py` BZX26 21:14Z: **$95.22 (+5.23%)**. ⚠️ **No official ICE settle located; the % depends on contract basis** (a continuous-series prior close of $93.03 also circulates — never `BZ=F`, guard ADD#23). Secondary drivers named by TE: a Ukrainian drone strike on Russia's **Ust-Luga** terminal (OSPREY theater — not merged here) and **US SPR <290M bbl** (289.7M [EIA 8/21], lowest since 1982). Backwardation state not re-measured tonight.

## 4. ⚠️ Standing guards that did work tonight
- **"VESSEL SUNK/mined" is THEATER-checked then GATE-checked** — right theater, claim-only; the guard's fourth application.
- **INTERCEPTED → STRUCK ratchet**: the Jordan salvo (8 intercepted) and the Aqaba claim both sit on it; carry counts with sources.
- **Kharg AI-video (ADD#22)**: re-posted, still synthetic, still not a strike.
- **Clock collision**: UKMTO stamps are UTC (19:52Z/20:00Z 8/31 = 23:52/00:00 Gulf local) — a "9/1" date on the Khasab hits is the theater-local clock, not a third incident.

## 5. CARL on info by the override's letter
Two laden VLCCs struck in the corridor = *"explicit kinetic event with supply-disruption mechanism (vessel-strike)"* — the May-6 override's third trigger. **No tonnage lost;** the mechanism is war-risk premia and corridor avoidance, not barrels.

**Confidence 0.85** — CENTCOM primary on the denial and the strikes; UKMTO-derived on the two hulls (via Marisks/Bloomberg + MarineLink); target list and casualties are Iranian-media claims and labelled so; the Brent path is a mark, not a settle.
