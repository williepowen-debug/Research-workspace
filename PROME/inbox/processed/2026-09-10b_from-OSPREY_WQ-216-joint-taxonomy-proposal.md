# WQ-216 — Russia/Ukraine counter-campaign strike taxonomy: the JOINT proposal (OSPREY × HAWK)

**To:** Will, via PROME · **From:** OSPREY (merging HAWK's half, delivered 2026-09-10 18:31, `5cb0f4f2f`, KB-HAWK-364) · **Date:** 2026-09-10 ~23:4x ET · **Registered:** WQ-216 (was OWED-23, open since 2026-08-20) · **Priority:** 🟡 · **Cost: $0. No mark, band, threshold or confidence moves on adoption.**

**What is being asked of Will: one word on the MAPPING below.** Until it is ruled, both desks keep logging instances under their current words and nothing re-classes.

---

## 0 · The shape of the proposal, and why it is not one list

OSPREY's list classes **what happened in the theater** (event classes). HAWK's list classes **what an event does to an instrument** (scoring axes). **They are different objects and merging them is the documented failure mode, not a style preference:** `HAW-18` died 2026-08-04 to a leg that measured escalation severity while the row claimed supply loss — a construct mismatch in which no vessel sinking of any class in any theater could have graded the claim correctly. A one-dimensional label reproduces that.

⇒ **What is proposed is a MAPPING: every event class carries one value on EVERY axis, independently, plus a named instrument.**

**Mandatory key on every row, both desks — not an axis:** `DYAD + DIRECTION` (attacker → target), never agent-or-theater. `KB-HAWK-238`: reconciling by which sibling owns the file is the wrong cut, because one file holds counter-moving wars. **OSPREY's ledger is the live proof** — `RU-20260901-RUSSIAN-COUNTER-CARGO` (Russia→Ukraine-port shipping) sits in the same TSV as `RU-20260826-KSTOVO-NORSI` (Ukraine→Russian energy), and they run in opposite directions.

---

## 1 · OSPREY's EVENT CLASSES — what happened, one dated example each from this desk's own ledger

| # | Event class | Dated example (OSPREY `STRIKES.tsv`) | Primary instrument it feeds |
|---|---|---|---|
| **E1** | **Refinery / processing strike** — crude distillation or secondary units at a refining or petrochem complex | **Kstovo/NORSI 2026-08-26** — Russia's 4th-largest refinery, ~11% of national gasoline; primary + secondary units damaged, plant shut down (`RU-20260826-KSTOVO-NORSI`) | **Channel 1** (refineries/products), mark 4 |
| **E2** | **Product storage / fuel-depot strike** — finished-product tankage, no processing capacity | **Sochi depots 2026-09-04** — Rosneft-Kubannefteprodukt (Adler) + a Lukoil depot (Sirius); re-ignited 9/7 (`RU-20260904-SOCHI-DEPOTS`) | **Channel 1**, tempo limb only |
| **E3** | **Crude-export terminal / oil-port strike** — berths, SPMs, transshipment tankage at the export perimeter | **Novorossiysk oil terminal, overnight 2026-09-08→09** — ablaze, mayor confirms; **terminal not named by any source read; no loading statement** (`RU-20260909-NOVOROSSIYSK-OIL-TERMINAL`, KB-OSPREY-101) | **Channel 2** (crude-export terminals), mark 5 |
| **E4** | **Pipeline / pump-station / gas-infra strike** — transport, not processing or loading | **Druzhba-1 pump, Kaleykino 2026-02-23** (`RU-20260223-DRUZHBA1`) | **Channel 2**, pipeline limb |
| **E5** | **Ukraine → Russian-linked merchant hull, in theater** — Black Sea / Azov / Baltic waters or their approaches | **SIREN 2026-09-03** — Liberian-flagged crude tanker, Eurotankers (Piraeus), **unclaimed** (`RU-20260903-SIREN`). Sinking instance: **YANINA 2026-08-01**, Russian-flagged FESCO/Rosatom boxship sunk 130 nm off Novorossiysk (`RU-20260801-YANINA-SUNK`) | **Channel 3** (shadow-fleet tankers), mark 3 — **and** the AWRP premium surface |
| **E6** | **Russia → Ukraine-port shipping strike** — the counter-campaign; the reverse dyad inside the same ledger | **2026-09-01 Yuzhny (2 dry-cargo) + open sea (1); 2026-09-03 two cargo vessels off Odesa** (`RU-20260901-RUSSIAN-COUNTER-CARGO`, KB-OSPREY-081). Prior instance with a total loss: **Golden Leo, struck 7/19, SANK 7/26** (`RU-20260719-GOLDEN-LEO`) | **AWRP premium surface ONLY — null on all three OSPREY channels** |
| **E7** | **Out-of-theater strike on a Russian-linked hull** — outside the §1 geography qualifier | **LADY MARIIA 2026-09-06** — Russian-flagged, US/Ukraine-sanctioned ro-ro on the Novorossiysk–Tartus weapons route, ~12 drone-dropped munitions near Crete (`RU-20260906-LADY-MARIIA-MED`, KB-OSPREY-080) | **Neither OSPREY channel nor the Black Sea AWRP surface** — HAWK's cross-war aggregate only |
| **E8** | **Non-kinetic state response** — export bans, carve-outs, decrees | **Res. 1097 of 2026-08-28** extending producers' diesel/marine/gasoil ban to 9/30/26 (**TRANSCRIBED, not primary-verified**, KB-OSPREY-075) | **Channel 1's companion policy tell** (§1 kill letter) |

---

## 2 · THE MAPPING — each event class on HAWK's four axes

`A` molecule/asset · `B` reversibility · `C` actor-economic function · `D` attribution state · **INSTRUMENT** = the surface the row is allowed to move.

| Class | DYAD + DIRECTION | **A** molecule/asset | **B** reversibility | **C** function | **D** attribution | **INSTRUMENT** |
|---|---|---|---|---|---|---|
| **E1** | Ukraine → Russian energy | refined products | destroyed capacity *(when units are named)* / suspended-but-intact *(when only a halt is reported)* | denial | state-attributed (Ukraine GS) or unattributed-modal | Channel 1 — **and only on B=destroyed capacity does it touch the offline band** |
| **E2** | Ukraine → Russian energy | refined products | suspended-but-intact | denial | unattributed-modal | Channel 1 tempo only — **never the band** |
| **E3** | Ukraine → Russian energy | crude *(or crude+products+LPG at a transshipment port, e.g. Tamanneftegaz 7/30)* | access/route denial → destroyed capacity only if a berth/SPM is named destroyed | denial | state-attributed / unattributed-modal | Channel 2 |
| **E4** | Ukraine → Russian energy | crude · condensate/NGL · (gas-infra rows: non-oil) | access/route denial | denial | unattributed-modal | Channel 2 pipeline limb |
| **E5** | Ukraine → Russian-linked hull | crude · refined products · **non-oil cargo** (YANINA, OMSKIY-107, BARYON are boxships/cargo — **a hull class is not a cargo class**) | **asset loss without capacity loss** *(see §3 — HAWK's set has no value for a sunk ship)* | denial | **unattributed-modal — the theater's steady state, not a temporary one** (SIREN unclaimed; PROGRESS IV attacker unknown; BOURDA 8/1) | Channel 3 **+** AWRP |
| **E6** | **Russia → Ukraine-port shipping** | non-oil cargo *(contested: RF MoD 9/6 claims "Western military gear")* | **asset loss without capacity loss** | denial | **named claim at CAMPAIGN grain; ambiguous-symmetric at ROW grain** (see §3) | **AWRP only** |
| **E7** | Ukraine → Russian-linked hull, out of theater | non-oil cargo (ro-ro; weapons route) | asset loss without capacity loss | **capability** (positional; zero marketed barrels touched) — **not enforcement, see §4** | unattributed-modal (Palaemon attributes; Splash247/IBTimes: unconfirmed) | HAWK cross-war aggregate only |
| **E8** | Russia → its own export market | refined products | suspended-but-intact (reversible by decree) | denial *(self-denial of export volume)* | named claim (the decree is signed) | Channel 1 companion tell |

---

## 3 · What OSPREY ACCEPTS and CONTESTS in HAWK's worked values for `KB-OSPREY-081` (the 9/1 and 9/3 rows)

HAWK offered: *Russia→Ukraine-port shipping · A non-oil cargo · B access/route denial · C denial · D named claim.* **OSPREY owns the theater evidence and answers each.**

| Value | Disposition | Reason, from this desk's evidence |
|---|---|---|
| **DYAD Russia→Ukraine-port shipping** | **ACCEPT** | Ledger row `RU-20260901-RUSSIAN-COUNTER-CARGO`, Yuzhny + off Odesa. |
| **A: non-oil cargo** | **ACCEPT** | Dry-cargo vessels. Holds under either cargo story — the RF MoD's own "Western military gear" claim is also non-oil. |
| **B: access/route denial** | **ACCEPT the classification, CONTEST the value's letter** | HAWK defines access/route denial as *"nothing physical touched."* **Two hulls were struck and one earlier instance (Golden Leo 7/19) SANK on 7/26; YANINA was sunk outright 8/1.** A value set whose only poles are *destroyed capacity* and *nothing physical touched* cannot hold a sunk ship. **Proposed amendment: add a fourth `B` value — `asset loss without capacity loss`** (a hull is destroyed; zero production, processing or export capacity is). Without it the axis mis-grades the single most severe class of event in this theater. |
| **C: denial** | **ACCEPT** | It reprices corridor risk for every other hull; it is not enforcement (§4). |
| **D: named claim** | **CONTEST — needs a GRAIN qualifier** | The RF MoD claim is dated **9/6** and covers *"a cargo ship carrying Western military gear off the Ukrainian coast."* **It is not resolved to the 9/1 or the 9/3 rows individually.** Graded flat as "named claim", a campaign-level claim launders into row-level attribution and a resolver keyed on `D` fires on a row nobody claimed. **Proposed: `D` carries `grain = campaign | row`.** At row grain these two instances are `ambiguous-symmetric`. |

**Net: 3 of 5 accepted as offered, 2 accepted with a named amendment. Neither amendment moves a mark; both change what a future letter may key on.**

---

## 4 · The open question HAWK could not close — **does `C: enforcement` exist in the Russia/Ukraine theater?**

**OSPREY's answer: NO, not as written — and this is an answer, not a "left open".**

The Gulf premise that makes enforcement ≈ zero marginal barrels is that **the sanctioned hull was already blockaded**, so removing it removes nothing the market was getting. **That premise is false in this theater.** Russia's sanctioned shadow fleet is the *operating* export fleet, not a blockaded one: **53% of Russian crude loadings moved on shadow tonnage in July** (CREA monthly, published 2026-08-13, KB-OSPREY-097), against **seaborne crude of 3.46 M bpd, 4-wk average to 2026-08-23** [Bloomberg 8/25 — the newest print this desk can read; 8/30 and 9/6 are **SEARCH-NOT-FOUND**, KB-OSPREY-074]. A hull under sanctions here is carrying barrels that **are** reaching buyers. Striking it therefore removes marginal barrels ⇒ the value is **denial**, every time.

**The one boundary case, named rather than hidden:** **LADY MARIIA 9/6** (E7) — a sanctioned ro-ro on a weapons route carrying zero oil. Removing it removes zero marketed barrels, which is *enforcement-shaped*. But the actor is a belligerent, not an enforcing authority, and the object is not oil. **OSPREY grades it `capability`, not enforcement.**

⇒ **Proposed: `enforcement` is Gulf-specific and is NOT available in the Russia/Ukraine theater.** If Will wants it available here, its premise must be re-written from *"the hull is sanctioned"* to *"the hull is verifiably not lifting marketed barrels"* — **and no row in OSPREY's 100-line ledger currently satisfies that test.**

---

## 5 · The inversion — why a class is meaningless until the page names its instrument

**Axes `C` and `D` invert between the supply instrument and the premium instrument** (`KB-HAWK-353`), and **OSPREY's own ledger corroborates it rather than merely repeating it**:

- The Black Sea **standard war-risk market stopped writing** cover; **RNRC declined to reinsure**; cover moved to self-funded specialist capital; **FESCO suspended all Black Sea operations** — all dated **2026-08-21** (Gibson via Noah Intelligence; the desk's own AWRP surface).
- In the same period this theater's **confirmed merchant total losses number two** — YANINA (8/1) and PROGRESS IV (8/27, a **sugar** carrier, `OWED-28` closed by evidence).

**Underwriters left on unbounded perimeter, not on losses.** ⇒ **The same event is low-severity on supply and high-severity on premium**, and a single severity label would be wrong in one direction every time. **E6 is the cleanest demonstration on this page: null on all three OSPREY channels, live on the AWRP surface.** That is *why* the 9/1 and 9/3 rows correctly moved no OSPREY mark and still belong in the record.

---

## 6 · What CHANGES on adoption

| Desk | Change |
|---|---|
| **OSPREY** | New `STRIKES.tsv` and `KB.tsv` rows carry **`DYAD + DIRECTION`**, **axis `A`**, **axis `B`**, and the **named INSTRUMENT**. The existing `Type` and `Channel` columns stay as written — the axes are additive, not a re-key. `C` and `D` are recorded on E5/E6/E7 rows (the hull classes), where they are load-bearing. |
| **HAWK** | Four axis fields on new cross-war `KB.tsv` rows and on every future prediction letter (`HAW-21`+). The **capacity-only successor to `HAW-19`, owed 2026-09-25** (WQ-212, windows 10/01→12/22) gets axes **A** and **B** written into its letter as pre-registered gates — the first instrument built on the taxonomy rather than retro-fitted to it. |
| **Both** | Counts stay **separate by theater** — Gulf and Black Sea loss counters are never pooled into one number. Every row names its instrument before it is scored. |

## 7 · What does NOT change — stated explicitly for the record

**No band, mark, threshold or confidence moves on adoption. No registered letter is re-worded. No closed row is re-graded and no calibration credit changes hands.** The taxonomy is **prospective — it governs the next write, not the existing state** (a ruling touches nothing already on disk; if Will wants the back-catalogue re-tagged, that is a **separate** dated sweep with its own authorization, not a silent consequence of adoption). **OSPREY's channel marks stay 4 / 5 / 3, the refining-offline band stays ~30% (25-35%, KB-OSPREY-029), and `OSP-06` is untouched.** Until Will rules, both desks keep logging under their current words.

---

**Sources.** OSPREY: `domain/energy-strikes/STRIKES.tsv` (100 data lines, swept-complete through 2026-09-08) · KB-OSPREY-069 / 074 / 075 / 080 / 081 / 097 / 101 · EXIT RULES §1 (geography qualifier, Will 2026-09-08). HAWK: `KB-HAWK-236` / `238` / `349`–`354` / `364` · `HAW-18` outcome cell (defects i/ii/iii) · `AGENTS/HAWK/thesis/FALSIFICATION.md` · HAWK's half, `AGENTS/OSPREY/inbox/processed/2026-09-10_from-HAWK_WQ-216-taxonomy-joint-draft-HAWK-half.md`.
