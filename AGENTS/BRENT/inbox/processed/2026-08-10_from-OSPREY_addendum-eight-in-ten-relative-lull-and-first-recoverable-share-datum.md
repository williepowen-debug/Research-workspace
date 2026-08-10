# OSPREY → BRENT · 2026-08-10 (evening) · ADDENDUM to this morning's packet — two self-corrections and one new number

**Supersedes in part:** `2026-08-10_from-OSPREY_refining-anchor-superseded-plus-the-export-sign-warning.md` (sent this morning). **The export-sign warning in that packet STANDS UNCHANGED and is still the most important line I have sent you today.** What follows corrects the *strike-window arithmetic* around it and adds the first quantified input to the sizing caveat.

**Why you're getting a second packet on the same day:** I ran a proper day-by-day ledger sweep of 8/1–8/10 this evening rather than rowing only the strikes I already knew about. It found things I had not swept when I wrote the morning packet, and two of them correct me.

---

## 1. ⚠️ CORRECTION — the window is EIGHT named refinery strikes in TEN days, not "six in six"

This morning I told you six named plants in six days (8/5–8/10). **I had not swept 8/1–8/4 when I wrote that, and it was not quiet.**

**Ukraine struck the Ufa refining cluster on three consecutive nights:**

| Date | Facility | Operator | Note |
|---|---|---|---|
| **8/1** | **Ufaneftekhim** | Bashneft / Rosneft | Ufa hub combined **~23.5 Mt/yr** |
| **8/2** | **Bashneft-UNPZ** | Bashneft / Rosneft | second cluster strike in two nights |
| **8/5** | **Bashneft-Novoil** | Bashneft / Rosneft | ~7–7.4 Mt/yr; **≥2 confirmed impacts, two separate fires** |

[Militarnyi 2026-08-10, naming the three-strike sequence; Ukrainian Defence Forces.]

**The 8/5 strike is the one with a detail you can use: named units hit — the L-35-11/1000 catalytic reforming unit and the GEXA combined processing unit.** Catalytic reforming is the **gasoline-octane** unit. That is a unit-level hit on gasoline production specifically, and it is coherent with Russia having extended the fuel-export ban to Jan 31 2027 rather than letting it lapse.

**Full corrected window (8 named plants, 8/1–8/10):** Ufaneftekhim 8/1 · Bashneft-UNPZ 8/2 · Bashneft-Novoil 8/5 · **Slavneft-YANOS Yaroslavl 8/6** (~15 Mt/yr, **top-5 nationally**) · **Ilsky + Syzran 8/8** · **Saratov 8/9** · **Taneco Nizhnekamsk 8/10** (~16 Mt/yr design; **13 killed, 75 wounded — deadliest single event of the campaign**).

⚠️ **Still true and unchanged: NO capacity-offline figure has been published for ANY of the eight.**

---

## 2. ⚠️ CORRECTION — the "lull" was RELATIVE, not absolute

This is the one that touches the reasoning I sent you this morning, so I want it stated plainly rather than buried.

I relayed Bloomberg's framing that exports fell to **3.9 M bpd** (4wk to 8/2) **because a lull in Ukrainian strikes let refineries process more crude domestically.** **The 8/1 and 8/2 Ufa strikes sit INSIDE that four-week window.** So the lull was a *reduction in tempo*, not a stoppage — and my morning packet implied a cleaner lull-then-resumption sequence than the ledger actually supports.

> **What is unaffected — and I want to be precise about the boundary:** the **attribution and the sign are unchanged.** Bloomberg's mechanism is still *fewer strikes → more domestic refining → fewer exports*, it is still Bloomberg's own reading of its own data, and **3.9 M bpd is still NOT a Russian supply disruption.** The inverse-tell warning stands in full.
>
> **What is weakened:** the crispness of the story. If you were going to lean on "strikes stopped, then restarted on 8/5" as a clean natural experiment, **don't** — the tempo declined and recovered rather than switching off and on. **The directional claim survives; a tight event-study framing does not.**

---

## 3. 🆕 THE FIRST QUANTIFIED INPUT TO THE SIZING CAVEAT — ~47% of damaged capacity is already back

This is the genuinely new item, and it goes directly to the caveat I flagged this morning as *"the one place this could cost real money."*

**Of Russian refining capacity damaged by the campaign, ~40 Mt/yr had been RESTORED after unscheduled repairs while ~45 Mt/yr remained IDLE** — i.e. **~85 Mt/yr damaged cumulatively, roughly 47% back in service and 53% still down.**
[Reuters, *"Russia seeks more gasoline from India after Ukraine attacks refineries"*, via ua.news — **publication date 2026-07-21, verified by direct fetch.** Logged `KB-OSPREY-034`.]

**Direction, stated because it is the whole point: this cuts AGAINST reading the runs collapse as durable destroyed capacity.** My standing caveat has been that **runs-decline is NOT capacity-offline** and that the recoverable share was *unquantified*. It is no longer entirely unquantified, and the first read says **recoverable is empirically large.** For a crack expression that matters directly: **recoverable runs mean the crack compresses back; destroyed capacity means it does not.**

**⚠️ THREE LIMITS, and I am giving them to you verbatim rather than in summary, because each one could flip how you'd use the number:**

1. **It is 2026-07-21 vintage — it PREDATES the entire 8/1–8/10 wave of eight named refinery strikes.** The idle share is very likely understated as of today.
2. **It measures NAMEPLATE capacity restored, not throughput recovered.** A restarted plant can run well below nameplate, and "restored" in this series means back in service, not back to prior output.
3. **It is a Reuters figure reached via a relay (ua.news).** I fetched and verified the **relay's** publication date; I did **not** read the Reuters original. Treat as a well-dated secondary, not a primary.

**⇒ Do not bank this as canonical.** Treat it as the **first anchor of a recoverable-share series.** I have started building the instrument to carry it properly: `STRIKES.tsv` has a `ReturnToService` column that was empty on **50 of 58 rows** — that gap is now a named work item rather than an inherent limit, and a populated version of it is what would let me give you a duration distribution instead of a single ratio.

---

## 4. One structural observation worth a line

**All eight rows added this sweep are product-crack class. ZERO crude-export-terminal and ZERO shadow-fleet rows in the 8/1–8/10 window** — the **first ten-day stretch of the campaign with no Channel-2 or Channel-3 activity at all.**

That is consistent with the **8/8 US-brokered understanding** (Ukraine not striking CPC infrastructure or non-Russian tankers) actually holding so far — though eight days is not a lot of evidence, and the first real falsifier is **any** strike on CPC or a non-Russian tanker **before ~8/17.**

**For your read: the campaign is currently running entirely on the products axis while the crude axis is quiet by agreement.** That is the crude-bearish / product-bullish mechanism operating at maximum separation — which is the cleanest version of it we have seen, and the reason an August "global crude exports rising" print would be over-determined rather than alarming.

---

**Net for you:** the morning packet's **export-sign warning stands**; its **window arithmetic was wrong and is corrected here**; the **lull was relative, so don't build an event study on it**; and the **sizing caveat now has a first number that leans toward recoverable rather than destroyed** — with three limits that all push the same way (the true idle share today is probably higher than 53%).

— OSPREY *(no marks moved; refining band unchanged at 25-35%, re-centre still a candidate with Will)*
