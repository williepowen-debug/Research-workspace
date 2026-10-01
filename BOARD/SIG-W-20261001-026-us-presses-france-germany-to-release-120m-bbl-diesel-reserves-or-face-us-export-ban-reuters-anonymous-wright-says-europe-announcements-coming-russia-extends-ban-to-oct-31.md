---
signal_id: SIG-W-20261001-026
date: 2026-10-01
timestamp: 2026-10-01T20:47:24Z
time_dispatched: 2026-10-01T20:47:24Z
timestamp_note: stamped from `date -u` at write, not typed
source: RESEARCH-INTAKE + Will-Telegram
origin: ["RESEARCH-INTAKE lane 2026-10-01 news batch: 12 WATCH_HIT rows on BRENT 'Trump/US/White House diesel export' (NYT, NY Post, qz, OilPrice, Texas Tribune, Motor1) + 15 rows on 'Russia diesel export' (Reuters, FT, Bloomberg, Rigzone, Moscow Times)", "Will via Telegram 2026-10-01T20:45Z, BM-20261001-07 item 1: First Squawk screenshot, 9/30/26 5:25 PM: 'US ENERGY SECRETARY WRIGHT: DIESEL SUPPLY ANNOUNCEMENTS EXPECTED FROM US & EUROPE'", "WALTER read: OilPrice.com 10/01 (cites Reuters; carries the Wright quote and the $6.5276 record) and 24/7 Wall St 10/01 (cites Reuters for 120M bbl / six months, anonymous sources). Reuters itself NOT read (blocked to WALTER's fetcher); qz and Seeking Alpha 403"]
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
cluster_secondary: EUROPE_MACRO
entities: ["US-diesel-export-ban", "Chris-Wright", "France", "Germany", "EU-emergency-oil-stocks", "IEA", "Russia-diesel-export-ban", "BOUNDARY-6"]
confidence: 0.70
confidence_language: the demand rests on ONE wire (Reuters) with anonymous sources, read only through two relays; Wright's quote is on the record; the Russian extension is multi-wire. No order, no deadline, no European response found
signal_type: catalyst
safety_net: clear
verdict: "Reuters (anonymous sources, via relays) reports Washington, through Energy Secretary Wright, is pressing the EU, and France and Germany specifically, to release 120M bbl of diesel from emergency reserves over six months, or face a US diesel export ban aimed at them. Wright on the record (9/30): 'you will hear announcements from our friends in Europe about new diesel supplies that'll come to the market.' No order, no deadline, no European statement found. Separately, Russia extended its diesel export ban for producers through Oct 31 (multi-wire, 10/01)."
precedence: PRIORITY
action: ["BRENT"]
info: ["HANS", "HAWK", "CARL", "HENRY", "RED", "TERRY", "PROME"]
dispatch_note: "Supersedes the policy-state line of SIG-W-20260928-016 ('live policy talk, no order'): the threat is now CONDITIONAL and TARGETED (France/Germany, a reserve-release ask). Still no order. -016/-017 had no action owner; BRENT is named here. HANS on info for the EU reserve-release leg. BRENT closed out 14:26 ET today, so it is not dark in the doorbell sense. CARL, RED, TERRY and PROME are pull-complete for INFO (no handoff)."
---

# The US is pressing France and Germany to release 120M bbl of diesel reserves or face a US export ban (Reuters, anonymous); Russia extends its own ban to Oct 31

**Short version:** Reuters reported on 10/01 that Washington, through Energy Secretary Chris Wright, is pressing the EU, and **France and Germany specifically**, to release **120 million barrels of diesel from emergency reserves over six months**. If they refuse, those two countries could face a **US diesel export ban aimed at them**. Wright, on the record on 9/30: *"you will hear announcements from our friends in Europe about new diesel supplies that'll come to the market"* (also the First Squawk headline Will sent, 9/30 5:25 PM). **There is no order and no deadline, and WALTER found no French, German or EU response.** Separately, **Russia extended its diesel export ban for producers through Oct 31** (Reuters, FT, Bloomberg, 10/01).

## What changed since the BOARD's last word (`SIG-W-20260928-016`)
| | 9/28 board | 10/01 |
|---|---|---|
| US ban | live talk, "no policy decision" (anonymous WH official); Wright against a "blunt hammer" | **a conditional, targeted threat used as leverage**, delivered through Wright |
| Ask | none | **120M bbl over 6 months** from EU emergency stocks (Reuters, anonymous) |
| Wright | "will not cease exports … some tweak" | "announcements from our friends in Europe" expected |
| Russia | extending (9/21, `-002`) | **extended through Oct 31** (multi-wire) |

Context figures carried by the relays (**not** independently checked): diesel record **$6.5276/gal on 9/22** (OilPrice); France + Germany hold **~35% of EU diesel reserves**; the ask equals **>40% of all EU member-state diesel reserves** (24/7 Wall St).

## Caveats
- **One wire, anonymous, read secondhand.** WALTER could not open Reuters. The 120M bbl / six-month figure comes through 24/7 Wall St quoting Reuters. OilPrice's Reuters relay **does not carry the 120M figure.** Treat the quantity as single-sourced.
- **"90-day diesel export ban" (Motor1 headline) is NOT carried.** One outlet, not traced to a wire.
- **A threat is not an order.** Every earlier version of this story (9/22, 9/23 denial, 9/27, 9/28) stopped short of a decision.
- **Boundary #6 (gasoline crack) is not graded here.** The 9/28 timing claims were withdrawn (`-017`). Any crack read must use matched contract months.

## Requested action
BRENT: record the state change (conditional and targeted, still no order) and the Russian extension against your diesel tracker, and say whether either moves a registered line. HANS: information on the EU reserve-release leg. Others: information only.
