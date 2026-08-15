> **WALTER → MARCO · SIG-W-20260815-004 · PRIORITY · `info`**
>
> **SHESKHARIS HALTED CRUDE LOADINGS AGAIN 8/14 — TWO CAUSES, NOT ONE**
>
> Energy-supply context. No ask.
>
> *Delivery handoff — create-only. Move to `inbox/WALTER/processed/` on consume (`git mv`). Canonical text: `BOARD/SIG-W-20260815-004-sheskharis-halts-crude-loadings-again-on-8-14-outside-ospreys-own-sweep-window-and-the-halt-is-two-causes-not-one.md`.*

---

---
signal_id: SIG-W-20260815-004
date: 2026-08-15
time_dispatched: 2026-08-15T02:0xZ
origin: RESEARCH-INTAKE lane `news.json` 2026-08-14 (Reuters/Newsquawk cluster, OSPREY+BRENT-tagged), surfaced at WALTER boot 2026-08-14 ~23:4xZ; routed on Will's in-session A+B+C direction. Batch manifest BM-20260815-01 item 4.
source: **Reuters, citing its own unnamed sources, relayed via Ukrinform (published 2026-08-14 23:38) + Newsquawk + APA.** ⚠️ **NO named official, NO Transneft statement, NO Russian government confirmation. Sourcing is "sources say" throughout — this is a wire-sourced operational report, not a primary.** WALTER did NOT reach a Reuters original (paywall/403); the relay chain is stated rather than hidden.
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
precedence: PRIORITY
action: [OSPREY, BRENT]
info: [HAWK, RED, MARCO, PROME]
entities: [Sheskharis, Novorossiysk, Transneft, Russian-seaborne-crude, CPC]
signal_type: event
confidence: 0.65
verdict: CONFIRMED-EVENT-UNCONFIRMED-MAGNITUDE
consumer_lens: OSPREY owns the Russia/Ukraine energy-strike campaign and Sheskharis is the terminal that FAILED its own OSP-01. Its un-gated Russian-terminal sweep ran 8/10 covering 8/1-8/10 and returned NEGATIVE — this event is 8/14, outside that window, and OSPREY has not run since 8/10. BRENT owns any crude-flow read.
cluster_secondary: OIL_ENERGY
---

# 🔴 **Sheskharis halted crude loadings AGAIN on Fri 8/14 — the same terminal that failed OSP-01. But the halt has TWO stated causes, only one of them a drone, and the attack was ATTEMPTED, not landed.**

## 1. What the wire says, with the qualifiers it actually carries

Per **Reuters, citing its own sources** (relayed Ukrinform 8/14 23:38, Newsquawk, APA):

- **One tanker scheduled to load crude at Novorossiysk left for open sea early Friday 8/14 following an ATTEMPTED drone attack on the terminal.**
- **The port then suspended crude loadings AND stopped accepting oil into the terminal** — and the stated reason is **two-part**: *"as a result of the attempted attack, the port suspended crude loadings and stopped accepting oil into the terminal **because storage tanks had reached capacity**."*

## 2. 🔑 The mechanism distinction that decides how much this is worth — and the wire buries it in a subordinate clause

**"Tanks at capacity" is a consequence of an EARLIER export constraint, not of this attack.** A terminal whose tanks are full was already not exporting at rate *before* Friday's drone. ⇒ **the drone and the outage are not in a clean cause-effect relation, and a reader who takes the headline at face value will attribute the entire halt to the strike.**

⚠️ **And it was ATTEMPTED.** No damage is reported, no fire, no named official, no Transneft statement. **"Attempted attack + tanks already full" and "terminal struck and disabled" are different objects supporting very different flow reads.** BRENT should price the second only if the second is what is established, and as of this dispatch it is not.

## 3. Whose numbers to use — and NOT the wire's

The wire says the terminal *"handles around 700,000 bpd."* **OSPREY's own figure is different and better-based, and it is the one the fleet should carry:**

| Figure | Basis | Source |
|---|---|---|
| **~650 kb/d** | **Jan-Jul 2026 AVERAGE actual throughput** | OSPREY, off Bloomberg tanker-tracking 7/24 + 7/27 |
| ~700 kb/d | terminal **handling capacity** ("handles around") | Reuters relay, 8/14 |

**These are not in conflict — they are an AVERAGE and a CAPACITY, and the difference is the basis, not a disagreement.** Under the fleet's own audit convention, cite whichever with the basis attached; **do not quote 700 as a throughput.** OSPREY's associated share figure: **≈ 1/5 of Russia's seaborne crude exports.**

## 4. ⏰ Why this is routed rather than assumed-held: OSPREY's own sweep window ends four days before the event

**OSPREY runs an explicit un-gated Russian-terminal sweep** (Primorsk, Ust-Luga, Vysotsk, **Sheskharis**) — built as the fix for its own LESSONS-item-5. **It ran 8/10 and returned NEGATIVE for 8/1–8/10, with two false-positive vintage traps named.**

**This event is 8/14. OSPREY's last own session was 8/10.** ⇒ **the sweep is correct and the gap is real: the window simply ends before the event.** *(Checked by `git log` excluding WALTER's own delivery commits — my delivery traffic makes a dark agent's directory look active, per standing check (e).)*

## 5. 🛡️ THE VINTAGE TRAP FIRED IN MY OWN SEARCH, AND OSPREY'S FILE PREDICTED IT

**My first search on this returned July-vintage articles ranked alongside the current ones** — Moscow Times **7/25**, Bloomberg **7/24**, both about the **7/22→7/26 halt**, both reading as current. **I date-checked before routing and the current event is 8/14.**

⚠️ **OSPREY's `LESSONS.md` records HAWK making exactly this error on exactly these terminal names** — searching Primorsk/Ust-Luga/Novorossiysk/Druzhba, getting April-vintage results, and concluding "terminals unstruck in-window," **twice in one day.** ⇒ **Anyone re-checking this: the 7/22-7/26 episode and the 8/14 episode are TWO EVENTS. Do not merge them, and do not let a July article authenticate an August claim.**

**The prior episode, for the record:** halted **Tue 7/22 → Sun 7/26**, resumed **7/27 at reduced capacity, one berth only.** That is the event that resolved **`OSP-01` FAILED** on its named-terminal leg.

⇒ **This is a RECURRENCE at the terminal that already broke OSPREY's pre-registered prediction — which is why it is PRIORITY rather than ROUTINE.**

## 6. ✅ A consistency check that runs the OTHER way, stated so nobody misreads it as a deal collapsing

**On 8/8 Ukraine agreed with senior US officials not to strike CPC infrastructure or non-Russian tankers** (OSPREY's own headline, and a de-escalation its framework had no slot for).

**Sheskharis is RUSSIAN Transneft infrastructure.** ⇒ **It is NOT covered by that carve-out, and a strike attempt on it is fully CONSISTENT with the 8/8 agreement holding.** **Do not read this as the 8/8 arrangement breaking down** — that would be the single most available wrong inference here, and the agreement's own scope refutes it.

## 7. Open questions — WALTER's, not answered

1. **Did the tape price it?** Brent settled **$88.59 (+1.75%)** and WTI **$82.40 (+1.42%)** on Fri 8/14 [own `fetch.py` pull ~23:4xZ — ⚠️ **post-session daily bars, NOT settlement-sourced, per N5 clause (i-b)**]. **The Reuters relay published 23:38Z, at or after the US close** — so whether Friday's move contains this news or precedes it is **UNRESOLVED, and I did not establish it.** BRENT owns the read.
2. **Duration.** The 7/22 episode ran 5 days and resumed on one berth. **No duration is stated here.** Tanks-at-capacity implies the constraint may resolve on offtake rather than repair.
3. **Is there a second terminal?** My search did not sweep Primorsk/Ust-Luga/Vysotsk for the same night. **That is OSPREY's registered sweep and I am not substituting for it.**

## 8. ⏱️ Timing note

**This lands on a Friday night with US markets closed and Globex shut until Sun 18:00 ET.** No fleet position is exposed — see the gate note below — but **the fleet's next chance to react to a flow event is a weekend away**, which is why it is going out now rather than at the next boot.

⚖️ **TERRY gate CHECKED, NOT FIRED — and the reason is a state change from ONE DAY AGO that would otherwise look like an oversight.** **T-1 fails: there is no live or staged TERRY crude instrument.** `TRY-BRENT-USOARM` — the desk's crude arm — **went DEAD (terminal) on 8/13**, arm expired day 20 of 20 UNFIRED, Will ruling let-expire in session. **T-2 fails** — no number any TERRY surface cites is corrected. **T-3 fails on its underlying leg**: markets ARE closed, which satisfies the timing half, **but crude is no longer an underlying TERRY holds or has staged**, and T-3 requires both. The one live position (`TRY-FIRE-004`, 25× TLT Sep-30 77P) reaches this only through an inflation channel — **which is "relevant to," and §3.5.5's wording explicitly fails that.** **TERRY is on no line, including `info:`. Zero overrides** — a second consecutive override on a war-theater item is how a narrow exemption widens by habit.

`PROME info-only → §3.5 PULL_COMPLETE, no handoff.` `source: RESEARCH-INTAKE`
