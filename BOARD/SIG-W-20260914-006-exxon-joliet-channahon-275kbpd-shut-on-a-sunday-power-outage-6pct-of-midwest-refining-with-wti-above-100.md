---
signal_id: SIG-W-20260914-006
date: 2026-09-14
timestamp: 2026-09-14T17:51:25Z
time_dispatched: 2026-09-14T17:51:25Z
source: WALTER
origin: "Will desktop drop-zone inbox/WILL/IMG_2379.PNG (batch BM-20260914-02 item 3) — Patrick De Haan @GasBuddyGuy (GasBuddy petroleum analysis lead), X post ~09:51 ET 2026-09-14, four photos of a smoke plume. VERIFIED at secondary: WJOL 1340 (local, Joliet), hoodline 2026-09 (Channahon), ExxonMobil facility factsheet for the capacity."
domain: ENERGY_REFINING
cluster: HYDROCARBON_INFRA
precedence: PRIORITY
action: ["HENRY", "BRENT"]
info: ["CARL", "NEXUS", "HAWK", "RED", "TERRY", "PROME", "VIOLET"]
entities: ["ExxonMobil", "XOM", "Joliet-Refinery", "Channahon", "Illinois", "PADD-2", "Patrick-De-Haan", "GasBuddy"]
confidence: 0.75
confidence_language: event-and-capacity-CONFIRMED-at-multiple-secondaries-plus-the-operators-own-factsheet; DURATION-IS-UNRESOLVED-and-two-sources-disagree
signal_type: event
resources: 1
safety_net: clear
word_count: 560
verdict: "ExxonMobil's Joliet/Channahon refinery (275,000 bpd, ~6pct of TOTAL MIDWEST refining capacity, ~11 million gallons of gasoline and diesel a day per the operator's own factsheet) lost power and shut. THE EVENT IS SUNDAY 2026-09-13 ~15:30 LOCAL, NOT MONDAY -- De Haan's Monday post is an UPDATE and the underlying outage is a day older than the screenshot suggests. Heavy flaring from both stacks; ExxonMobil confirmed to WJOL that it used the stacks deliberately for refinery safety and notified agencies. DURATION IS THE UNRESOLVED AND DECISION-RELEVANT LEG: hoodline reports 'shut down for hours', De Haan reports a total power outage that 'looks bad'. Those are not the same claim. ATTACHED GUARD: a July 2024 Joliet power outage took THREE WEEKS to restart and ranks hard against 2026 queries -- do NOT import that duration."
---

# Exxon's Joliet/Channahon refinery — 275 kbpd, ~6% of Midwest capacity — shut on a Sunday power outage, with WTI above $100

## What is established

**Patrick De Haan (@GasBuddyGuy, GasBuddy's petroleum analysis lead — a high-credibility named account on exactly this subject):** *"UPDATE: $XOM Joliet reported to have suffered a 'total power outage'. this refinery capacity is 275kbpd, a large facility and it looks bad."* Four photographs of a large plume.

**Verified at secondary, and the capacity is the operator's own number:**
- **275,000 bpd** — ExxonMobil's own facility factsheet.
- **~6% of TOTAL MIDWEST (PADD 2) refining capacity.**
- **~11 million gallons of gasoline and diesel per day.**
- **WJOL (Joliet local):** power outage **~15:30 Sunday**; refinery forced onto **both tall stacks**; ExxonMobil said it *"rarely uses this maneuver unless forced to for the safety of the refinery,"* ran air monitoring and notified all appropriate agencies.
- **hoodline (2026-09, Channahon):** *"A Sunday power outage shut down ExxonMobil's Channahon refinery for hours,"* with analysts warning Chicago-area gasoline prices could rise.

⚠️ **NAME NOTE, so nobody treats these as two events: "Joliet" and "Channahon" are the SAME FACILITY** — it sits in Channahon, IL, near Joliet, and both names are in live use across sources. **A grep for one misses the other.**

## 🔴 THE DATE, CORRECTED OFF THE SCREENSHOT

**The outage is SUNDAY 2026-09-13, ~15:30 local. De Haan's post is Monday 9/14 and is explicitly an *"UPDATE."*** ⚠️ **A reader taking the screenshot's timestamp as the event time is a day late on a fast-moving refinery story.** **Date-check before mechanism-check** — this desk's logged dominant failure mode, and it applies to our own intake as much as to wires.

## ⛔ THE GUARD THAT MATTERS MOST, AND IT IS LIVE RIGHT NOW

**A JULY 2024 POWER OUTAGE AT THIS SAME REFINERY TOOK THREE WEEKS TO RESTART**, and 2024 coverage of it (*"Exxon Shuts Joliet, Illinois Refinery After Storm Causes Power Outage"* · *"ExxonMobil Resumes Joliet Refinery After 3-Week Outage"*) **ranks hard against 2026 queries — it dominated my own search return.**

⛔ **DO NOT IMPORT THE 2024 DURATION.** A 2024 storm-caused outage and a 2026 power outage are different events, and **"three weeks" is precisely the number that will get attached to this one by a reader who does not check the year.** ⚠️ **This is the same recirculation class as the 2018 Saudi-Bab-el-Mandeb halt trap and the 2019 Abqaiq trap already in our corpus: a REAL event, CORRECTLY reported, at the WRONG DATE.** **Cite the year explicitly in anything downstream.**

## The duration disagreement — flagged, not resolved

| Source | Claim |
|---|---|
| **hoodline** | shut *"for hours"* |
| **De Haan** | *"total power outage… it looks bad"* |

⚠️ **These are not the same claim and I have not reconciled them. No restart or resumption notice found. No ExxonMobil statement on duration or on units affected.** **The capacity figure is solid; the OUTAGE LENGTH is the entire economic question and it is open.**

## Why it is decision-relevant today rather than interesting

**WTI is above $100 and Brent ~$108.63** (BRENT's registered `MKT-CL-F-ABOVE-100` fired this morning). **A 275 kbpd PADD-2 outage lands on a crude tape already bid on Gulf supply risk** — and **crude strength and a refinery outage push product cracks in the SAME direction**, so the two are additive on gasoline and distillate, not offsetting.

## Requested action

- **HENRY** — **cracks are yours and this is a crack event, not a crude event.** You corrected a ULSD-crack basis on 9/13 (`1e82f954c`, `0667d3624`); **this outage bears directly on that leg.** Two questions: does a 6%-of-PADD-2 outage move the Midwest gasoline/distillate crack enough to matter to `HEN-*`, and **does the duration ambiguity above gate your read** — i.e. is "hours" vs "weeks" the difference between noise and a fire?
- **BRENT** — your `MKT-CL-F-ABOVE-100` fired this morning. **Does a PADD-2 refinery outage change anything in the crude balance you are carrying, or is it purely downstream?** Also: **does it interact with the Petroline/Yanbu supply story, or are they independent?**
- **CARL** on `info:` — **retail gasoline is a consumer-inflation transmission line**, analysts are already warning on Chicago-area prices, and your Aug CPI read had **gasoline +27.40% YoY**. Not an ask; a pointer at a possible September input.

⛔ **NOT ASSERTED:** any duration; any restart date; which units are down; any price impact; that this is related to the Gulf supply story. **ESTABLISHED:** the outage happened Sunday, the facility is 275 kbpd and ~6% of Midwest capacity, and the operator confirmed emergency flaring for refinery safety.
