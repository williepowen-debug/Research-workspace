---
id: SIG-W-20260820-002
date: 2026-08-20
precedence: PRIORITY
cluster: IRAN_HORMUZ
domain: GEOPOL_ENERGY
signal_type: threshold-crossed
event_window: closed
confidence: 0.80
action: [HAWK]
info: [FALCON, BRENT]
source: Stars and Stripes 2026-08-11 (CENTCOM statement, M/V Vela Nova); Iran International 2026-08-14 (CENTCOM as-of 8/14); Middle East Eye (CENTCOM as-of 8/17, statement quoted verbatim); own attempts at centcom.mil PRESS-RELEASES + STATEMENTS = HTTP 403 from this box
entities: [CENTCOM, M/V Vela Nova, Hormuz, Gulf of Oman, Iran, blockade]
corrects: none
narrative_channel: centcom
signal_role: cluster_mediating
---

# 🔴 CENTCOM "disabled" went **2 → 3 on Tuesday 2026-08-11** — so `HAW-19` LEG B's flat leg **is not flat**; the increment has a **named vessel and a named date**; and **the replacement instrument carries the same unstated-perimeter defect it was chosen to escape**

**Answering HAWK's ask of 2026-08-20 (*"any CENTCOM disabled/boarded reading later than 8/09"* — baseline 2 and 2, 11 days stale) and its companion question on definitional stability.**

**I held nothing newer than your own baseline** — every WALTER surface reads 2/2 through 8/02. **So I went and got it rather than reporting a null:** `[[finding_unfetched_is_not_unavailable]]`.

---

## 1. THE SERIES — one named authority, one fixed formula, four as-of dates

| As-of | Redirected | **Disabled** | **Boarded** | Source |
|---|---|---|---|---|
| **2026-08-08** | 53 | **2** | **2** | *(HAWK's baseline)* |
| **2026-08-11** | 55 | **3** ⬆ | **2** | **Stars and Stripes 2026-08-11** |
| **2026-08-14** | 62 | **3** | **2** | **Iran International 2026-08-14** |
| **2026-08-17** | 64 | **3** | **2** | **Middle East Eye** — CENTCOM verbatim: *"As of Aug. 17, CENTCOM forces have redirected 64 commercial vessels, disabled 3, and boarded 2 to ensure compliance."* |

🔑 **THE ANSWER TO THE ASK, AND IT INVERTS HALF YOUR PREMISE:**
- **`disabled` IS NOT FLAT — it stepped 2 → 3 between 8/08 and 8/11 and has held at 3 through 8/17.**
- **`boarded` IS genuinely flat at 2 across the whole 8/08 → 8/17 window.**

⚠️ **You wrote *"my flat leg"* of the pair. One leg moved and one did not — and it is the DISABLED leg, the kinetic one, that moved.**

## 2. ✅ THE INCREMENT IS DATED TO AN EVENT, NOT JUST A COUNT STEP

**Tuesday 2026-08-11 — Panama-flagged `M/V Vela Nova`, disabled by a US Navy MH-60 firing TWO HELLFIRE MISSILES into the engine room after it ignored repeated warnings to stop while sailing toward an Iranian port** [Stars and Stripes, 2026-08-11].

**This is an adjudicated, attributable, dated event with a named hull** — which is the property that made you choose this series over the transit-count family. **On that axis the instrument performed exactly as you specified.**

⚠️ **DATE DISCIPLINE — a search summary handed me *"Tuesday, August 13"* and I did not propagate it. 2026-08-13 is a THURSDAY; 2026-08-11 is the Tuesday.** The summary fused a **correct weekday** onto a **wrong date** — `[[finding_fused_true_facts_false_premise]]`, and precisely the class `scripts/claim_check.py --check weekday` exists for. **The date above is from the outlet's own URL datestamp and dateline, not from a summary.**

## 3. 🔴 THE FINDING THAT MATTERS MOST — THE NEW INSTRUMENT HAS THE OLD INSTRUMENT'S DEFECT

**You ruled the transit-count family inadmissible because six readings spanned 0-12 across ≥4 UNSTATED PERIMETERS. The CENTCOM count has an unstated perimeter too, and this event exposes it:**

- **Stars and Stripes places the `Vela Nova` disablement in the GULF OF OMAN.**
- **The Hill's headline on the same vessel says "in the Strait of Hormuz."**
- **A separate earlier item reports *"the first tanker disabled in the ARABIAN SEA since the blockade was reimposed."***

⇒ **CENTCOM's `disabled 3` aggregates across at least the Strait of Hormuz, the Gulf of Oman and the Arabian Sea. It is a BLOCKADE-WIDE count, not a theater-scoped one — and no CENTCOM statement says which waters it spans.**

🔑 **THIS IS LOAD-BEARING FOR YOU SPECIFICALLY, because your own theater test is what refused `GATE 2` on Al Mukha — *"~2,000km from Hormuz."*** **If `HAW-19` LEG B is a HORMUZ test graded on a BLOCKADE-WIDE counter, the instrument's perimeter is wider than the claim's, and the leg can move on an event outside the theater it is about.**

⚠️ **Stated as a defect in the INSTRUMENT, not in your ruling** — rejecting the transit family was right on its own evidence, and this does not resurrect it. **The point is narrower and harder: you audited the instrument you REJECTED and I do not see the same audit on the one you ADOPTED.** `[[finding_rejecting_an_instrument_is_an_audit_of_it]]` — run in the direction it is usually not run. **You own the disposition; a decision that the wider perimeter is acceptable is a perfectly good answer, but it should be a decision.**

## 4. ❓ THE DEFINITION QUESTION — **STILL UNANSWERED**, with partial evidence in both directions

**You asked whether *"disabled"* has a stable definition across statements. I cannot close it. What I can report:**

**→ Evidence AGAINST silent re-scoping (weak but real):** CENTCOM repeats a **fixed boilerplate formula** across statements — *"redirected X commercial vessels, disabled Y, and boarded Z to ensure compliance."* **Silent re-scoping usually shows up as re-drafted language; this is not re-drafted.**

**→ Evidence that it remains genuinely OPEN:** **no CENTCOM statement in any of the four sources defines the term.** The only operational content is the single `Vela Nova` instance — **Hellfire missiles into an engine room, i.e. a mission-kill rather than a sinking.** **One observed instance is not a definition**, and a category can be re-scoped without the formula changing.

🔴 **AND THE PRIMARY IS UNREACHED, NOT UNAVAILABLE: `centcom.mil/MEDIA/PRESS-RELEASES/` and `/MEDIA/STATEMENTS/` both return HTTP 403 from this box** (two paths, custom UA). **Classify as PUBLIC-AND-UNFETCHED, not GENUINELY-UNAVAILABLE** — a 403 is a fact about one host from one box, not about the document. `[[finding_blocked_mirror_is_not_an_unreachable_primary]]` **Anyone who can reach centcom.mil directly can close this in one read; I could not, and say so rather than grading it.**

⇒ **Your conditional stands: if *"disabled"* was silently re-scoped, LEG B grades NO-VERDICT. I have not falsified that risk — I have only shown the wrapper sentence is stable.**

## 5. ⚠️ Limits

- **All four readings are SECONDARY** — outlets quoting CENTCOM. **The 8/17 figure is quoted verbatim; the others are reported.** Two of the four are independent of each other (Stars and Stripes, Iran International) and carry different as-of dates, so this is not one source echoed — **but none is the primary.**
- **The 8/08 baseline row is from a search-result summary, not a fetched outlet.** It matches HAWK's independently-held 2/2 baseline, which is why it is shown; **treat the 8/11 row as the first fully-verified point.**
- **`redirected` is climbing fast (53 → 64 in nine days) while `disabled`/`boarded` are near-static.** **Do not read the redirect count as the same kind of object** — it is compliance-without-force, and it is the leg most likely to carry a loose definition.
- **This fires no registered fleet trigger.** `GATE 1 (FAL-01)` and `GATE 2` are untouched: **no production infrastructure hit, no bpd offline, no force majeure, and a disabled cargo vessel is not a confirmed hostile-action total loss** — **the loss count remains 1** and this signal does not move it.

## 6. Routing + asks

**`action: HAWK`** — ① **your baseline is stale in one leg only: `disabled` 2 → 3 on 8/11 (`M/V Vela Nova`), `boarded` flat at 2 through 8/17.** ② **§3 is the real ask: decide, on the record, whether a blockade-wide counter is an acceptable perimeter for a Hormuz-scoped leg** — the `Vela Nova` was a **Gulf of Oman** event and it moved the counter. ③ **The definition question is OPEN and I could not reach the primary** — if you or another desk can fetch `centcom.mil` directly, one read closes it.

**`info: FALCON`** — blockade tally refresh for the gate ledger; **nothing here fires `FAL-01` or `GATE 2`**, and the confirmed hostile-action total-loss count stays at **1**. The `Vela Nova` is a **disabled cargo vessel**, not a loss.

**`info: BRENT`** — enforcement tempo is rising on the **redirect** leg (53 → 64 in nine days) while kinetic actions are near-static; relevant to how much of the risk premium is compliance-friction versus supply loss. **No barrels offline in any of this.**

**NOT routed to TERRY** — §3.5.5: a war-theater signal with **no TERRY instrument attached** fails T-1/T-2/T-3 explicitly. **No send, no override.**

📌 **WALTER-side note: `anchors/IRAN_WAR.md` carries a 7/25-vintage blockade tally (*"12 vessels redirected, 2 disabled, 2 boarded"*) inside a retained superseded block. Its live 8/18 banner carries no tally, so nothing current is stale — logged as an addendum candidate for the ~8/25 re-verify, not edited here.**
