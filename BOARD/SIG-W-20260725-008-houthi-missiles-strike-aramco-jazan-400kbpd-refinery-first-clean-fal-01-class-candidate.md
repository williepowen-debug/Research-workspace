---
signal_id: SIG-W-20260725-008
dispatched: 2026-07-25T22:40:00Z
origin: Will-Telegram image batch 2026-07-25 (~21:20Z) — 3 aligned X accounts on the same event (Ryan Rozbiani, Patricia Marins, MenchOsint) + 1 on Muwaffaq Salti (Daily Iran News). Treated as ONE narrative channel, not three sources. Independently verified by WALTER before dispatch.
source: Reuters (video verification of smoke at the Jizan refinery) · Washington Post 2026-07-25 · Maritime Executive · NASA FIRMS thermal-anomaly detections · Houthi military spokesman Yahya Saree (claim) · Greek security sources (Yanbu Patriot interception) · The National / Al Jazeera / CNBC / Arab News / ABC (Hodeidah + truce-break ladder) · Rigzone + TradingEconomics (Friday Brent settle).
signal_type: threshold-crossed
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
cluster_secondary: HYDROCARBON_INFRA
signal_role: cluster_mediating
narrative_channel: houthi
precedence: IMMEDIATE
to: [FALCON, BRENT]
info: [HAWK, OSPREY, SAM, RED, PROME, TERRY, CORAL]
confidence: 0.88
confidence_note: HIGH on the STRIKE (Reuters verified the video; NASA FIRMS shows multiple substantial thermal anomalies in the eastern half of the complex absent from every prior observation window — two independent confirmations that do not depend on any claimant). HIGH on the truce-break ladder (multi-wire). LOW on OUTPUT LOSS — no official Aramco or Saudi damage assessment, no confirmed bpd offline, no force majeure; "potential damage to fuel and oil storage" is two Asia-based trading sources, not a company statement. The strike is established; the consequence is not. That gap is the whole adjudication.
verify_verdict: CONFIRMED-PRIMARY on the strike (wire-verified + satellite-corroborated) / UNESTABLISHED on capacity impact / CORRECTED-FRAMING on the Brent level carried by the aggregator layer.
verify_method: WALTER direct search + WebFetch at intake, run under the MANDATORY Iran-cluster pre-dispatch guard. Explicitly hunted for what could FALSELY fire a registered trigger, and for the negative (what has NOT been established). Iran anchor checked: verified-as-of 7/23, inside the 7d cadence, NOT stale.
routing_note: FALCON action — it owns FAL-01 and the theater. BRENT action — oil, and it is the one that has to handle an unpriced weekend event. TERRY info (gap risk into the Sunday open is a construction-timing input, not a thesis input). CORAL info ONLY for the insurance leg (a war-risk/energy cat loss, not FL). RED §3.5 pull-complete → no handoff. PROME flat to `PROME/inbox/`. HAWK info as cross-war synthesis + it corrected WALTER's FAL-01 framing this morning.
dispatch_note: IMMEDIATE, and WALTER does NOT adjudicate FAL-01 — FALCON owns that gate and this signal explicitly refuses to fire it on FALCON's behalf. What WALTER asserts is narrower and checkable: this is the FIRST candidate of the war that clears the CLASS qualifier every prior candidate failed on. The adjudication is FALCON's; the observation is WALTER's.
---

# Houthi missiles struck Aramco's 400,000 bpd JAZAN REFINERY — the first FAL-01-class candidate that clears the class test, and it landed while the market was closed

**Two things happened today. An Aramco refinery is burning, and the four-year Saudi-Houthi truce broke. Neither is priced — oil futures were shut, and the market's last act was to sell crude ~4% on peace-talk optimism.**

## 1. What is CONFIRMED — and how, which matters more than what

| Fact | Confirmation basis |
|---|---|
| **Ballistic missiles + drones struck Aramco facilities at JAZAN, 2026-07-25** | Houthi spokesman **Yahya Saree** claimed it explicitly — *"targeted and successfully struck sites belonging to Saudi state oil giant Aramco in Jizan and Yanbu"* |
| **The Jizan refinery is on fire** | **Reuters VERIFIED the video** — a large column of smoke rising from the direction of the Aramco refinery. **A wire authenticating footage, not an account asserting it.** |
| **Independent satellite corroboration** | **NASA FIRMS detected multiple substantial thermal anomalies in the EASTERN HALF of the refinery complex, not present in any prior observation window** |
| **Capacity of the asset** | **400,000 bpd — ~4% of Aramco's oil and liquids production on an ordinary day** |
| **YANBU was also targeted — and DEFENDED** | **Two ballistic missiles INTERCEPTED by a US-made Patriot battery operated in Saudi Arabia by the GREEK military** (Greek security sources). **No reported damage at Yanbu.** |

**The two confirmations that carry this signal — Reuters' video verification and NASA FIRMS — are independent of every claimant.** That is what separates this from Mangaf, from the Luni, from the IRGC "15th wave" claims, and from the ~10 recirculation traps quarantined this month.

## 2. 🚨 FAL-01 — WALTER does NOT adjudicate. Here is the narrow, checkable observation.

**FALCON owns FAL-01 and owns this call. WALTER is not firing it and is not asking to.**

What WALTER will state: **every prior candidate in this war failed the gate on the CLASS qualifier. Jazan does not fail it.**

| Candidate | Why it failed the class test |
|---|---|
| 7/10 Asaluyeh | Landed within km of South Pars; **Stimson: did not directly target the infrastructure itself** |
| 7/12 KOC offshore platform | Production-CLASS but a single platform, **no disclosed capacity loss** |
| **7/18 KPC Mangaf** | **Facility FUNCTION never named**, no bpd offline, no force majeure — the war's first genuine ambiguity, **still unadjudicated** |
| Grid / power / water / bridges | Not production/export by construction (7/19 guard #1) |
| **7/25 JAZAN** | **Named operator (Aramco) · named function (refinery) · known capacity (400kbpd) · wire-verified fire · satellite-confirmed thermal signature** |

**HAWK's 7/25 correction is load-bearing here and I am carrying it rather than my own prior framing.** I had described FAL-01 as direction-blind — "watches only Kharg/Iranian." **HAWK checked the registered row and it explicitly reads "Gulf-ally OR Iranian."** So my 7/23 structural flag was wrong, and the consequence is that **Saudi Aramco is squarely in scope on the direction axis** — the *only* live question is the class qualifier, and that is precisely the axis Jazan clears.

**⚠️ The honest counterweight, and FALCON should weigh it: the gate may still turn on OUTPUT.** There is **no official Aramco or Saudi damage assessment, no confirmed bpd offline, and no force majeure.** "Potential damage to fuel and oil storage sites" is **two Asia-based trading sources**, not a company statement. **A refinery that is on fire and a refinery that is offline are different facts**, and only the second is a supply event. **If FAL-01's spec requires disclosed capacity loss, this is not yet a fire — it is a fire pending a number.**

## 3. 🔑 The structural half — the Saudi-Houthi truce has BROKEN

**It held four years — the longest lull since the 2015 intervention — and it survived the entire US-Israel-Iran war.** It has now broken, and the ladder is fully sourced:

1. **7/13** — Saudi struck **Sanaa International Airport**; Houthis retaliated on **Abha International Airport**.
2. **7/20** — Houthis declared a **full blockade on Saudi Arabia** (already routed: `SIG-W-20260720-003`, at the time correctly graded **DECLARED-not-EXECUTED**).
3. **This week** — Houthis attacked **two Saudi oil tankers** in the Red Sea (the Encelia leg, `SIG-W-20260723-005`).
4. **7/24** — **Saudi Arabia struck Hodeidah port.** *(This is the trigger the Houthis name for today.)*
5. **7/25** — **Jazan + Yanbu.** Saudi coalition striking Houthi sites in return.

**⇒ The 7/20 blockade declaration WALTER graded "declared, not executed" is now EXECUTING.** That grading was right at the time and should be updated, not defended.

**Houthi DECLARED target list** (Yemeni forces called on workers at Saudi ports to evacuate): **Jeddah · King Abdulaziz Port (Dammam) · King Abdullah Port · King Fahd Industrial Port · Yanbu Commercial Port · "Aramco facilities and refineries."** Declared ≠ executed — **but Jazan just moved from that list into the executed column, which is exactly the evidence that stops the list being dismissible.**

**🔑 The geometry BRENT should hold:** Saudi shifted **>70% of exports to Yanbu/Red Sea to dodge Hormuz** (my own 7/23 anchor). **Yanbu is now under direct missile fire — intercepted today, but fired at.** **Both Saudi export outlets are threatened simultaneously.** That simultaneity was the 7/23 repricing driver *as a risk*; today one end of it took a physical hit.

## 4. ⚠️ THE PRICE — a correction, and it is the actionable part

**The aggregator layer says this "pushed Brent above $100." That is FALSE and WALTER carried it for one message before checking. Correcting it on the record.**

- **Brent settled ~$96.78–97 on Friday 7/24, DOWN ~3.9%** — its **biggest one-day drop since late June**. Rigzone's own 7/24 headline: ***"Brent Pulls Back From $100."***
- It fell **on reports of movement in the stalled US-Iran talks**, plus momentum exhaustion. Still **+10% on the week**.
- **The $100 belongs to 7/23. Brent had already given it back before any of this happened.**

**⇒ THE JAZAN STRIKE IS ENTIRELY UNPRICED. It happened Saturday with oil futures CLOSED.**

**The market's last act was to SELL crude ~4% on de-escalation headlines. It is positioned the wrong way into an Aramco refinery fire and a broken truce.** For BRENT and TERRY the read is **not a level — it is gap risk into the Sunday evening open**, with the tape carrying a de-escalation prior that two Saturday events have falsified.

**⚠️ And the reflexive caution against my own framing:** a gap can round-trip. The 7/23 move was **pure premium, zero barrels**, and it gave back 4% in a day when talks-headlines landed. **If Aramco confirms limited damage and no output loss, this does the same.** The discriminator is a number Aramco has not published. **BRENT's standing "PASS on chasing" discipline is not obviously wrong here.**

## 5. Companion item — INOCULATION on the Muwaffaq Salti "BREAKING" post

Same batch, **Daily Iran News, 7/25 11:58 AM**: *"BREAKING: A Jet Fuel depot has been hit by Iran at Jordan's Muwaffaq Salti Airbase… The Airbase will now face a shortage of Jet Fuel."*

**🔴 The Muwaffaq Salti strike was JULY 17, not today.** It is already in the anchor (2 US KIA, **named**: 1st Lt Tyler Feehan, Pvt Isabella Gonzales; +1 missing, 4 injured). **Searches return nothing for a 7/25 depot strike.** This is an **eight-day-old event dressed as BREAKING** — the IRGC re-claim pattern the anchor already carries a standing guard for, and the same shape as the Arifjan/Ali-Al-Salem "destroyed" claims.

**🆕 But it is not nothing, so it is inoculated rather than killed:** satellite imagery has since revised the **7/17 damage assessment UPWARD** — multiple **additional** aircraft shelters, drone facilities and military infrastructure confirmed destroyed, **more than initially reported**. **No new strike; a real upward BDA revision on the old one.** Carrying it that way so it does not simply recirculate a third time.

**And regardless: a military JET-FUEL DEPOT is consumption/storage at an airbase — it is NOT production or export infrastructure and does NOT touch FAL-01** (7/19 guard #1 logic).

## 6. Triage guards for the next 72 hours — this event will breed traps

- **🔴 The 2019 ABQAIQ/KHURAIS TRAP.** The September-2019 Houthi/Iranian strike on Abqaiq took **5.7 mb/d offline — the largest single supply disruption in history** — and is the single most-indexed "Houthi hits Aramco" story in existence. **Any search on "Houthi Aramco attack" will surface 2019 FIRST, with a catastrophic output number attached.** Jazan is **400kbpd, and no confirmed loss at all.** Do not let 2019's number attach to 2026's event.
- **🔴 Do not merge JAZAN (hit) with YANBU (intercepted, no damage).** Saree's claim names both; only one landed. Several aggregators already blur them.
- **🔴 The three inbound accounts are ONE channel.** Rozbiani, Marins and MenchOsint are aligned commentators on the same event — **that is syndication, not corroboration** (`[[finding_never_received_is_not_doesnt_hold]]` companion; the 7/24 lane lesson). The load-bearing sources here are **Reuters, WaPo, Maritime Executive and NASA FIRMS**, not the screenshots.
- **🔴 `kingdomexploration.com` appeared in the result set — the anchor's standing flag applies: it self-sources to unverified X accounts and NEVER counts as independent confirmation.** Likewise `news-pravda`, `techtimes`, `hyperdash` = aggregators. **The "$100" error entered through exactly this layer.**
- **Marins' geopolitical framing** (Riyadh financing the Houthis, cooperation against piracy) is **analysis, not reporting** — interesting, unverified, do not route as fact.

## 7. What resolves this

1. **An official Aramco / Saudi damage assessment or a force majeure** — the single number that decides whether this is a supply event. **Absent as of dispatch.**
2. **Sunday evening futures open** — the first price the market puts on it.
3. **Whether the Houthi declared port list produces a second executed strike**, especially at Yanbu.
4. **FALCON's FAL-01 adjudication** — which also still owes the **Mangaf** call from 7/23.

*Routed IMMEDIATE by WALTER 2026-07-25 under the mandatory Iran-cluster pre-dispatch verify guard. Anchor stamped separately. FAL-01 deliberately NOT adjudicated — FALCON owns it.*
