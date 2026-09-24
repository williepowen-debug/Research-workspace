# WQ-266 / DOCKET L447 — Channel-2 geography qualifier: ADOPTED TEXT (2026-09-24)

**Author:** OSPREY (owner of the letter). **Written:** 2026-09-24, ~00:5x ET, inside a PROME Tier-1 spawn (WQ-184 due-row, L447). **$0** — this letter feeds a channel retirement, not a capital rail. STAND DOWN (WQ-192) untouched. No score, band, threshold or prediction moved by this edit.

## 1. The ruling this text implements

**Will, 2026-09-19 12:05 ET, in terminal, verbatim: *"Yes — apply it to both."*** (`PROME/WILL_QUEUE.md` WQ-266, RECENTLY DONE.) Channel 2 gets the same geography qualifier Will gave Channel 3 on 2026-09-08: only Black Sea / Baltic incidents reset its clock, and a Caspian oil port stops keeping a Black Sea channel alive. This is option **B** of `OWED39_DISPOSITION_2026-09-19.md` §2d. PROME wrote no text. The words below are OSPREY's.

**What the ruling did NOT decide, and this text leaves alone:**
- **The CPC asymmetry is intended and stays.** `GATE-OSPREY-001` ("CPC Channel-2 UPGRADE tripwire") makes a CPC event Channel-2-material on the EVENT side while excluding Kazakh barrels from the THROUGHPUT series. CPC's marine terminal is at Novorossiysk, on the Black Sea, so it stays inside the geography on limb 1. Limb 2 is unchanged.
- **Option ② (moving products terminals out of Channel 2) was NOT ruled.** §2d called it the same edit but a separate choice. Will's words cover geography only. The 9/9 Novorossiysk **fuel-oil** terminal therefore still counts on limb 1 through the `oil-port` class, and ② stays open (see §5).

## 2. The template: Channel 3's qualifier of 2026-09-08, verbatim

> *"no **qualifying vessel-strike incident** **in Black Sea, Sea of Azov or Baltic waters or their approaches** for **21+ days** …"*

## 3. SUPERSEDED Channel-2 text (verbatim, `AGENTS/OSPREY/CLAUDE.md` EXIT RULES §1, as of commit `1a11a069f`)

> *"**Channel 2 (crude-export terminals) kill:** no `crude-terminal`/`pipeline`/`oil-port`-class row for **30+ days** AND seaborne crude exports hold ≥3.5M bpd 4-wk-avg (Kpler/Bloomberg) with no shut-in signal."*

## 4. ADOPTED Channel-2 text

> **Channel 2 (crude-export terminals) kill:** no `crude-terminal`/`pipeline`/`oil-port`-class row **whose struck asset lies on the Black Sea, Sea of Azov or Baltic coast — including the Kerch Strait and the Gulf of Finland — or in those waters or their approaches** for **30+ days** AND seaborne crude exports hold ≥3.5M bpd 4-wk-avg (Kpler/Bloomberg) with no shut-in signal.
> **In geography:** Novorossiysk (Sheskharis, CPC Marine Terminal and the port's other oil terminals), Tuapse, Taman/Volna, Port Kavkaz, Taganrog/Azov, the occupied-Crimea ports, Primorsk, Ust-Luga, Vysotsk, and the Kaliningrad oil terminals.
> **⛔ Out of geography. These events are still ROWED and go on the Channel-2 companion watch in STATUS. They no longer reset the clock:** the Caspian (Makhachkala, Kaspiysk, Astrakhan) · Arctic and Pacific ports · **inland** pipeline assets (trunk-line pump stations, Druzhba) and river ports not on those coasts · all other waters.
> **Test for a pipeline row:** the location of the STRUCK ASSET decides, not the port the line feeds. A pump station 1,000 km inland that feeds Primorsk is out. A pipeline manifold or tank farm inside a Black Sea / Azov / Baltic port is in.

**Why the pipeline test uses the asset's location and not the line's destination.** A test based on where the line leads would count more events and make Channel 2 **harder** to kill. That would be the desk choosing, under its own letter, the reading that keeps its 5 alive. Will's words were *"only Black Sea / Baltic incidents"*, and an incident is where the strike landed. The stricter reading is the one the ruling supports. It cuts **against** this desk (DELEGATION_TIER test 4 direction: easier to kill).
**What this reading costs, stated so the cost stays visible:** the campaign against Transneft's inland trunk lines (e.g. `RU-20260722-TUYMAZY-PUMP`) no longer shows up on this clock. That is why the companion watch is mandatory (§2f condition).
**Effect today: zero.** The newest pipeline-class row is Tuymazy on 7/22, 64 days before this record, so it is outside every live window.

## 5. The clock under the adopted letter, read from `STRIKES.tsv` on 2026-09-24 (not from memory; LESSONS 9)

| Reading | Anchor row | Elapsed 9/24 | Limb-1 kill date |
|---|---|---:|---|
| **Adopted letter (B)** | `RU-20260909-NOVOROSSIYSK-OIL-TERMINAL` (Black Sea, oil-port class via fuel-oil terminal) | **15/30** | **2026-10-09** |
| Superseded bare letter (D) | `RU-20260910-MAKHACHKALA` (Caspian) | 14/30 | 2026-10-10 |
| B + ② (unruled) | `RU-20260908-CPC-SPM` | 16/30 | 2026-10-08 |

- **Direction check (LESSONS 10, stated in words):** the adopted letter moves the Channel-2 kill **one day EARLIER** (10/10 → 10/09). **Channel 2 becomes EASIER to kill, which cuts against this desk.**
- **New events 9/17 → 9/23 (this session's sweep):** none in geography. `RU-20260919-KASPIYSK` (Caspian, target not established) would not reset the clock under either letter. It goes to the companion watch. A search-summary item placing a **Vysotsk** strike on 9/21 was traced to July-2026 reporting. It was REJECTED as vintage and not rowed (KB-OSPREY-155).
- **Limb 2 today:** Bloomberg 4-wk **3.53 M bpd to 9/20** (via search relay 9/22; the article was 403 and not read in full), **0.03 above the 3.50 floor**. The same report says weekly volumes fell with **a halt of departures from Novorossiysk**, cause NOT ESTABLISHED. ⚠️ **If that halt is a shut-in, limb 2's "no shut-in signal" clause is NOT met, and no Channel-2 kill can be written on this print whatever limb 1 reads.** A kill call still needs the fresh mechanism-level sweep the letter's NOTE demands.

## 6. Riders (DELEGATION_TIER form, applied although this is a Will ruling and not a self-ruling)
- **R1 dated:** 2026-09-24, on Will's 2026-09-19 word.
- **R2 superseded text preserved verbatim:** §3 above, and in place in CLAUDE.md.
- **R3 no mark moved:** C1/C2/C3 = 4/5/3, band ~30%, OSP-06 45%. All unchanged.
- **Consumers notified:** BRENT and HAWK packets 2026-09-24.

## 7. Declared residue (not fixed here, on purpose)
1. **② products-terminal assignment is UNRULED.** Today it moves Channel 2 by one day (15/30 → 16/30) and Channel 1 by zero. It stays with Will only if PROME judges one day worth his attention. OSPREY's own view is that it is not worth asking now: a one-day change is below the ledger's resolution (Disposition §2e). Raise it again only when it changes a kill date that is within 7 days.
2. **"Approaches" for fixed assets** is defined by the in-geography list plus the location test, not by a distance. Kerch Strait and Gulf of Finland are written in by name. Any port not named is graded when an event arrives, and each such grade is logged to KB.
3. **The Arctic and Pacific exclusion** follows from the ruling's words and is not otherwise argued. Limb 2's Bloomberg series counts ALL Russian seaborne crude, Pacific included. So the two limbs still measure different subjects, which is intended (Disposition §2a).
