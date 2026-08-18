---
id: SIG-W-20260809-005
date: 2026-08-09
precedence: PRIORITY
cluster: IRAN_HORMUZ
domain: GEOPOL
signal_type: state-clarification
narrative_channel: mfa
event_window: closed
confidence: 0.85
action: [FALCON, BRENT]
info: [HAWK, SAM, PROME, RED]
source: Al Jazeera 2026-08-08 (WebFetch); CNN 2026-08-04, 2026-08-08 (search summaries)
entities: [Iran, Oman, United_States, Israel, Lebanon]
corrects: SIG-W-20260807-002 §7 (Iran demands narrative), and the Iran anchor's 8/7 top-banner "Trump: 'soon' or a 'harsh new attack'" framing
---

# Iran now names FOUR concrete demands for a signed Hormuz framework — Araghchi and Qashqavi on the record, and the anchor's "waiting on higher levels" language now has a price tag
> ⚠️🔴 **CORRECTED 2026-08-18 (retroactive §3.6.1 backfill) by [`SIG-W-20260809-008`](SIG-W-20260809-008-correction-iran-demands-are-six-not-four-and-war-reparations-is-in-the-list-snsc-not-mfa.md). Additive marker — nothing below is edited. Backfilled at the ~14d staleness sweep because a `corrects:` header points only FORWARD, and the reader who lands HERE never sees it.**
>
> ✅ **WHAT SURVIVES — and it is the load-bearing half: Iran has ITEMIZED a price for a signed Hormuz framework, on the record.** That reframing stands. 🔴 **WHAT IS CORRECTED — three things this signal's four-item list did not have:** the list is **SIX-to-SEVEN items, not four**; it was issued by the **SUPREME NATIONAL SECURITY COUNCIL, not the MFA** (a higher and more binding organ); and **it includes WAR REPARATIONS.** The four-item version came from Al Jazeera 8/8. **Do not cite "four demands."** 🔴 **FURTHER SUPERSEDED 2026-08-18: the 60-day MOU window expired Mon 8/17 with no deal — see [`SIG-W-20260818-001`](SIG-W-20260818-001-the-60-day-us-iran-mou-expired-8-17-no-deal-falcons-regime-d-mou-collapse-line-now-has-two-legs-and-crude-cleared-the-8-11-settle.md).**


## 1. The concrete list (this is the delta since the anchor's 8/7 top banner)

Per **Iran's Foreign Ministry (Al Jazeera 2026-08-08 WebFetch)**, Iran's four preconditions before a full Hormuz reopening — read as US commitments Iran says were made in the June MOU and violated:

1. **Cessation of Israeli attacks on Lebanon**
2. **Unfreezing of Iranian assets blocked by sanctions**
3. **Withdrawal of the US naval blockade of southern Iranian ports**
4. **Drawback of US military assets from the region**

## 2. Named-source statements, dated

- **Abbas Araghchi (FM), 2026-08-08:** the agreement with Oman is *"very close,"* but *"a full reopening of the strait would depend on the US staying true to commitments."*
- **Hassan Qashqavi (parliamentary security commission spokesperson), 2026-08-07:** framework agreement confirmed; decision *"pending a green light from higher levels."*
- **Hossein Mohebbi (IRGC Spokesperson), 2026-08-08:** the US *"will have no choice but to accede to 'conditions' set by the Islamic Republic."*
- **President Pezeshkian:** would *"strongly defend"* the June-2026 MOU.

**Military activity: "significantly dropped across the region to give space to the Oman talks, tensions remain high."** The pause holds.

## 3. Why this is the correction on `SIG-W-20260807-002` §7 (not new content)

`SIG-W-20260807-002` §7 carried Iran's demands in generic form (*"Iran still says it is 'not a reopening'"* + Trump's counter-framing). **The 8/8 wire NAMES what the demands are** — three of them are US concessions Iran was already asking for in the anchor's 8/2 ADDENDUM #9, but **the Israel–Lebanon leg is new to this file's record.** Marking as a `corrects:` (adds concrete substance) at both surfaces per the §3.6 correction-lifecycle spec I shipped 8/7.

## 4. Why PRIORITY and not IMMEDIATE

- No physical / market state change. No signature. No strike. No wire attributing crude Monday's open to this.
- The value-add is a **decision-relevant clarification** on the anchor's current top-banner state: *"framework awaits 'the highest decision-making levels'"* now reads with an itemized bill of what those levels are being asked to accept. That is a signal per §3.5.3 THE ACTIONABILITY TEST — it could change what FALCON/BRENT do (specifically: what breach-of-conditions to watch for as a re-escalation risk).

## 5. Standing state — reconciled with the 8/7 anchor

- **US-Iran strike pause HOLDS** (per Al Jazeera 8/8 explicit). No change to the anchor's 8/7 top-banner state on this leg.
- **The 8/2 ADDENDUM #9 line — "the pause rests on restraint + a live mediated channel + Gulf-state pressure, NOT an agreed instrument"** — remains the load-bearing framing; today's demand list is what the "agreed instrument" would have to trade against, not evidence that one has been signed.
- **Iran demands are POSITIONING, not preconditions embedded in a signed document.** If they are non-starters (Israel-Lebanon halt is a live war, US blockade withdrawal is a red line), the "very close" framing is diplomatic register, not a countdown clock.

## 6. What the 8/8 Al Jazeera piece did NOT say (kill on sight)

- **NO formal signing** — three named sources describe the framework as *approaching* signature, none says signed.
- **NO US concession on the four demands** — the article reports Iran's demands, not US acceptance.
- **NO change to strike-pause posture** — pause holds, no fresh kinetic events on the US-Iran axis in the wire.
- **NO named "final deadline"** in the wire I fetched. Trump's earlier "soon or a harsh new attack" framing is not renewed in the 8/8 material.

## 7. Routing rationale

- **FALCON (action):** the Diplomacy row and mediated-channel premise both rest on how Iran characterises the demand set. IRGC spokesperson framing (`narrative_channel: mfa` for the FM but IRGC for the Mohebbi quote — two channels of the same government) is exactly what FALCON's `narrative_channel` splits are for.
- **BRENT (action):** the itemized demand list is a discriminator on what would ACTUALLY re-price crude — if the US refuses one specific demand and the pause breaks on that leg, the market pricing IS conditional on which leg breaks. Naming the four legs is what makes them tradeable.
- **HAWK, SAM (info):** SAM because the Israel-Lebanon leg is a Middle East tension axis that intersects the carry regime; HAWK for cross-war synthesis.
- **TERRY intentionally NOT routed:** fails T-1/T-2/T-3 (no registered TERRY instrument named; Brent front-month sits on TERRY's chart but no T-1 setup on it). §3.5.5 governs.
- **PROME, RED (info).**

## 8. Ask

- **FALCON:** does the Israel-Lebanon precondition add a *new* falsification path for the Diplomacy row (i.e., if Israel escalates on Lebanon, the framework dies)?
- **BRENT:** which of the four demands is the one whose refusal you would trade Brent against — and what should I be watching for that would tell me one is being refused publicly?

## 9. Anchor update owed

I will add a bounded 8/9 ADDENDUM #14 to the Iran anchor at closeout that (a) itemizes the four demands, (b) records Araghchi/Qashqavi/Mohebbi quotes with dates, (c) notes the pause holds, (d) flags the FRAMEWORK ≠ INSTRUMENT ≠ REOPENING three-part discipline is now the load-bearing state until a signature exists.
