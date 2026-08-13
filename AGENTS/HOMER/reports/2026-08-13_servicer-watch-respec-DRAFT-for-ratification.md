# Nonbank Servicer Credit Watch — RE-SPEC **DRAFT**, pre-registered, awaiting Will's ratification

**Status:** ⛔ **DRAFT — NOT LIVE.** The superseded spec governs until Will rules.
**Authority:** Will, 2026-08-12, rule batch row 45, relayed via PROME (`PROME/proposals/2026-08-12_rule-batch-RULED.md`). ⚠️ That was a **batch approval off PROME recommendations** — Will's authority, **not** his individual attention on this row. Ratification of the text below is a separate act.
**Drafted:** 2026-08-13 by HOMER · **Live surface it would amend:** `docket/CATALYSTS.tsv` row 11
**Riders honored:** dated re-spec · superseded text preserved verbatim · **no threshold moved in this edit** · own surface only · zero capital.

---

## 1. Why — the defect, stated precisely

**UWM Holdings, 2026-08-06:** Q2 net loss **$451.9M**; equity **$1.6B → $1.0B**; **first dividend suspension in company history**; **$2.05B rescue equity from Oaktree + SFS (Ishbia family)**; stock **−49% intraday**. UWM is the **largest US mortgage lender by origination volume** and sits on my watched panel.

**On the letter of the live trigger, none of that fires.** The registered enumeration is *rating action · covenant breach · facility draw · emergency transfer*. A rescue recapitalization is **none of the four**, so the watch correctly stayed 🟠 and I did not fudge it.

★ **The defect is not that the list was too SHORT. It is that the list enumerates MECHANISMS.** I wrote four **liquidity** mechanisms and omitted the **solvency / recapitalization** channel entirely — so the single largest US mortgage lender taking a rescue round could not fire the watch that exists to catch exactly that. **Any enumeration of mechanisms will miss the next novel one.** §4 proposes a fix for that deeper problem; §3 encodes what Will actually ruled.

---

## 2. SUPERSEDED TEXT — preserved verbatim (rider)

> **what_to_check:** `(1) Rating actions: Freedom Mortgage (KBRA BB+/Stable 10/17/25; S&P B), loanDepot, Onity; (2) PFSI 10-Q advance-loss provision line (Q1-26 $20M, ~5x YoY — the curtailment tell; Q2 10-Q ~early-Aug); (3) any facility-draw / covenant-breach / emergency-transfer headline`
>
> **threshold_signal:** `A discrete stress event at a mainstream servicer = the thing DEWEY confirmed has NOT happened yet; first occurrence flips servicer row 🟠→🔴 + immediate REGINALD note`

**Nothing in §3 removes any existing class.** Classes A–D below are the four above, restated unchanged.

---

## 3. PROPOSED SPEC — the three Will-ruled classes, made operational

**Firing any ONE class flips the servicer row 🟠 → 🔴 and triggers an immediate REGINALD note.** (Unchanged from the live spec.)

### Classes A–D — UNCHANGED
**A** rating action (downgrade or outlook-to-negative by KBRA/S&P/Moody's/Fitch) · **B** covenant breach · **C** emergency facility draw · **D** emergency servicing-transfer.

### Class E — RESCUE RECAPITALIZATION *(new)*
An equity or equity-linked injection meeting the **size floor** AND **at least one distress marker**:

- **Size floor:** gross proceeds **≥10% of pre-announcement market capitalization** (measured at the last close before announcement).
- **Distress markers** (≥1 required):
  - **(i)** priced at a discount **≥15%** to the 10-trading-day VWAP before announcement; **or**
  - **(ii)** carries governance concessions — board seats, veto/consent rights, or preferred with a liquidation preference senior to common; **or**
  - **(iii)** described by the **issuer, the investor, or a rating agency** as supporting liquidity, capital adequacy, or going-concern.

### Class F — FORCED / NON-GROWTH DILUTIVE ISSUANCE *(new)*
Issuance diluting existing common by **≥20%** where proceeds are for **general corporate purposes, liquidity, or debt paydown** — *not* an identified acquisition or organic-growth use. Includes **creditor debt-for-equity conversion** and **mandatory conversion** of existing instruments.

### Class G — DIVIDEND SUSPENSION *(new)*
**Unscheduled** suspension, omission, or **≥50% reduction** of a previously-paid common dividend.
⚠️ **"Unscheduled" is load-bearing** — a dividend cut at a servicer can be routine earnings management. Excluded: cuts pre-announced as policy, or tied to a disclosed strategic transaction. **A first-ever suspension is the strongest form** and should be noted as such when it occurs.

### 🚫 NO-VERDICT BAND — required, and it is what keeps the spec honest
These **do not fire** the watch and must be logged as observations only:

1. **Equity drawdown alone, at ANY magnitude — including 52-week lows and a −49% session.** This deliberately preserves the 7/31 discipline where I held 🟠 with all four listed names at 52-week lows. **Price is not a credit event.**
2. A raise **≥10% of market cap** that is priced **at or above** market, carries **no** governance concessions, and is issuer-described as growth/opportunistic → **NO VERDICT**.
3. A dividend cut **<50%** that was scheduled or previously guided → **NO VERDICT**.
4. Ratings **affirmation** with negative commentary but no action → **NO VERDICT** (Class A needs an action).

### Entity scope
**Listed:** PFSI · RKT · UWMC · LDI · Onity. ⚠️ **COOP is delisted** — Rocket closed the $14.2B all-stock acquisition 2025-10-01; Mr. Cooper now reads through RKT and pre-Oct-2025 COOP comparisons are invalid.
**Private:** Freedom Mortgage · Lakeview · Carrington — **in-window silence is the expected base case and is weak evidence**, not a negative.

---

## 4. ⚠️ BEYOND THE RULING — a backstop I am proposing, NOT encoding

**PROME's packet is explicit: if I think the ruling is wrong on the merits, flag it before encoding rather than encode a guess. This is that flag.** Will ruled three named classes. **§3 delivers exactly those and nothing more.** What follows is a separate ask.

**§3 fixes the 2026-08-06 miss. It does not fix the class of miss.** E/F/G are three more mechanisms bolted onto four; the fourth novel form of distress will evade all seven. I would add:

> **Class Z — SUBSTANCE BACKSTOP.** Any event, **however effected**, that an issuer, auditor, regulator or rating agency characterises in writing as bearing on the entity's **solvency, capital adequacy, or ability to continue as a going concern** — including going-concern language in a filing, a covenant *waiver* (as distinct from a breach), or a regulator-directed capital action.

**The argument for:** it is keyed to **economic substance attested by an accountable third party**, not to a mechanism I had the imagination to list in advance.
**The argument against, stated fairly:** it is softer than A–G, it imports someone else's judgment, and "characterises in writing" is a looser boundary than a number. It could admit false positives that A–G would exclude.

**I am not encoding Class Z. Ratify it, reject it, or defer it separately from §3.**

---

## 5. 🔴 RATIFICATION QUESTIONS — three, and I will not assume any of them

**Q1 — Does the re-spec apply RETROACTIVELY to UWM 8/6?**
Under the **live** spec, UWM does not fire and the watch is correctly 🟠. Under **§3**, it fires **twice** (Class E: $2.05B ≈ ~70% of pre-announcement market cap, with governance concessions and rescue framing · Class G: first-ever dividend suspension).
⚠️ **I am NOT firing it.** `LESSONS.md` forbids retro-fitting, and a spec written *after* an event and then applied *to* that event is the exact failure the pre-registration discipline exists to prevent. **But the stress is live and the next UWM print is ~November**, so "forward-only" means the watch stays 🟠 through a quarter in which the largest US mortgage lender took a rescue round. **That is a real cost either way and it is your call, not mine.**
> Options: **(a)** forward-only, watch stays 🟠 · **(b)** one-time seeding — ratify §3 *and* flip 🔴 on UWM, recorded explicitly as a seeding decision rather than a trigger firing · **(c)** forward-only, but raise the row to 🟠+ with a dated note that a Class-E/G event has already occurred un-scored.
> **My recommendation: (b)**, precisely *because* it is recorded as a seeding decision. It gets the surface to the right colour without pretending the old trigger fired, and the honesty is preserved in the label.

**Q2 — Class Z: in, out, or deferred?** (§4)

**Q3 — Are the numbers right? I have NOT base-rated them, and you should know that before ratifying.**
⚠️ **This is the weakest part of the draft and I am not hiding it.** My own standing rule is *base-rate a threshold before building it, and "don't build it" is a real answer.* I do not hold a history of nonbank-servicer capital raises and dividend actions, so **≥10% of market cap, ≥15% VWAP discount, ≥20% dilution and ≥50% dividend cut are reasoned, not calibrated.**
- The one observation I have: **UWM clears the Class-E floor ~7×** (~70% vs 10%), so the floor is not obviously too tight for a genuine rescue.
- **What I cannot tell you is the false-positive rate** — how often a healthy servicer raises ≥10% of market cap at a ≥15% discount in an ordinary year.
> **Proposed remedy:** ratify §3 **provisionally** with a dated obligation to base-rate the four numbers against 2019–2026 capital actions at the five listed names, and re-anchor before the spec is cited as load-bearing. **Or defer ratification until that work is done** — a defensible answer, at the cost of leaving the current known-defective spec live in the meantime.

---

## 6. What happens on ratification

1. Amend `docket/CATALYSTS.tsv` row 11 — superseded text preserved verbatim inline, dated, **no other threshold touched**.
2. Note the amendment in `STATUS.md` servicer rows and `NEXUS_BRIEF.md` (REGINALD consumes this watch).
3. Reply to `PROME/inbox/` confirming the encode — **PROME's packet says row 45 closes on my encode confirmation, not on the approval**, so it stays open until then.

**Zero capital. Zero thresholds moved. Nothing in this file is live.**

— HOMER, 2026-08-13

---

# ✅ RATIFICATION RECORD — Will, 2026-08-13 (two rulings, same day)

**This file is no longer a draft. The spec below is LIVE, encoded in `docket/CATALYSTS.tsv` row 11.**

| Question | Ruling |
|---|---|
| **Q1 — retroactivity** | **OPTION (b):** ratify §3 **and** set the row 🔴 as a **labelled one-time SEEDING decision** on UWM 8/6. ⛔ **Not a trigger firing — no registered trigger has ever fired on this watch.** The new spec was **not** applied retroactively as a trigger. |
| **Q2 — Class Z** | ⚠️ **First ruled UNADDRESSED** (encoded as NOT ratified, hours earlier) → then **RATIFIED** on a second same-day ruling. **Z is LIVE.** The interim "not ratified" text is preserved verbatim in the docket row per the rider — it is the record of a real interim state, not an error to erase. |
| **Q3 — base-rating** | **Not ruled.** Ratification therefore recorded **PROVISIONAL on the A–G numbers**, with a dated obligation to anchor them against 2019–2026 capital actions and dividend changes at PFSI / RKT / UWMC / LDI / Onity **before the spec is cited as load-bearing in any packet or trade rail.** **Z is exempt by construction** — it has no numeric threshold. |

## Class Z as encoded

**Trigger:** any event **not already captured by A–G** in which an **accountable attestor** states **in writing** that the entity's own **solvency, capital adequacy, or ability to continue as a going concern** is in question.

- **Accountable attestor = the issuer** (filing, release, or prepared remarks/transcript), **its independent auditor**, a **prudential or securities regulator**, or an **NRSRO**. Nobody else.
- **Must concern this entity's CURRENT condition** — not the sector, not a peer, not a hypothetical.
- ⛔⛔ **Z CANNOT BE FIRED WITHOUT THE VERBATIM ATTESTING SENTENCE AND ITS SOURCE DOCUMENT WRITTEN INTO THE ROW. No quote, no fire.** **This is the operational substitute for the number Z cannot have** — it converts "someone called it serious" into a checkable artifact, and it is what keeps the softest class in the spec auditable.

**Qualifying examples** (non-exhaustive — that is the point): auditor going-concern qualification or emphasis-of-matter; management's ASC 205-40 substantial-doubt disclosure; a covenant **waiver** obtained to *avoid* a breach (class B is the breach itself); a regulator-directed capital action, capital-plan rejection or supervisory agreement; an NRSRO publication citing going-concern/capital-adequacy risk **without** an accompanying rating action (an action is class A).

**🚫 Z no-verdict:** ⛔ **boilerplate and standing risk factors — the single largest false-positive source**, since nearly every 10-K carries going-concern-adjacent language and risk text repeated unchanged from a prior period is by definition not a current-condition statement; sector or peer commentary; analyst, press, short-seller or social-media characterisation; **and HOMER's own inference, which is never an attestation.**

**⚠️ Accepted weaknesses, recorded at ratification rather than discovered later:** Z imports a third party's judgment rather than measuring anything, and *"characterises in writing"* is a looser boundary than a threshold — **so Z may admit false positives A–G would exclude. It was ratified with those costs known and stated.** **Z is a residual, not a shortcut:** if an event fits A–G, score it there.

## Standing state after ratification

- **Row is 🔴 SEEDED.** The word **SEEDED** must travel with the colour. Correct phrasing anywhere it is cited: *"HOMER's servicer watch is 🔴 by a Will-ruled seeding decision on the UWM recapitalization; no registered trigger has fired."*
- **First genuine firing = the next class A–G or Z event occurring after 2026-08-13**, logged explicitly as distinct from the seed.
- **Open obligation:** base-rate the four A–G numbers (Q3 above).

**Zero capital. No threshold outside this ratified re-spec was moved.**
