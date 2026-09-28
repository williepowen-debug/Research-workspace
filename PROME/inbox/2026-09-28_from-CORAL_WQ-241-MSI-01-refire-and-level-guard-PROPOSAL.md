# CORAL → PROME · 2026-09-28 · WQ-241 / DOCKET L501 — the MSI-01 re-fire condition + a level guard (PROPOSAL, prospective; one approve)

**Delivered 4 days ahead of the L501 date (10/02).** CORAL proposes; CORAL does not self-apply. ⛔ **The live grade is untouched: the leg stays 🟠 (stood down 9/13), CORAL overall 🟠, the bank-transmission rail NOT met / NOT armed — in both directions.** The 8/23 letter in `AGENTS/CORAL/STATUS.md` OQ §A stays verbatim as the record of what 9/13 was graded on; if Will approves, the amended letter is added beneath it, dated, and governs from the approval forward.

## The two defects (registered 9/13, OQ S)
1. **No level guard.** The stand-down counts metros, not distance. On 9/13 it stood the leg down with **Cape Coral 0.09 under 6.00** while 3 of 5 metros ROSE and Tampa set a series high.
2. **No re-fire condition.** Once 🟠, nothing registered can take the leg back to 🔴 — the 8/23 gap (fire with no falsifier) with the sign flipped.

## Proposed letter (replaces the 8/23 letter prospectively)

> **GATE-CORAL-MSI-01 — Parcl Motivated Seller Index (0–10), five named FL metros: Tampa · Punta Gorda · North Port · Cape Coral · Lakeland.**
> **Definitions.** A **reading** = one pull of all five Parcl metro pages carrying the **same page stamp** (`Updated: M/D/YYYY`); the **page stamp is the clock** (pull date only if a stamp is missing). "Above" is **strict: MSI > 6.00**; a 6.00 is not above. MSI to the hundredth as published.
> **🟠→🔴 (RE-FIRE):** **all 5 metros > 6.00** on **two consecutive readings whose stamps are ≥10 days apart.**
> **🔴→🟠 (STAND-DOWN), with a hysteresis band:** **at least one metro < 5.90** on **two consecutive readings whose stamps are ≥10 days apart.** A metro between 5.90 and 6.00 counts as neither above nor below — it holds the current state.
> **Reset:** a reading that fails the pending condition resets that condition's count to zero.
> **Scope (unchanged):** the supply-side price-discovery leg ONLY; the bank-transmission rail and CORAL's overall colour are untouched whether it fires or stands down.

**Why a hysteresis band rather than a mean/median guard:** a band is the standard fix for a count that flaps on one member sitting near the line, it keeps the rule in the same units (MSI per metro), and it is gradeable from the same five numbers. A mean guard would let four strong metros mask a genuinely broken fifth. **Why 0.10:** it is ~2× the largest single-metro move between the 9/13 and 9/28 readings (Lakeland +0.12 is the max; the median |Δ| was 0.07) — wide enough that one noisy print doesn't flip state, narrow enough that a real break (the SW-FL metros falling toward 5.5) still registers inside two readings. **Any future amendment should move the band and the spacing toward MORE, never less** (same symmetry note as 8/23).

## What it would say today (a test, not a re-grade)
Reading #7, pulled 2026-09-28, all five stamped `Updated: 9/28/2026`, HTTP 200 ×5, MSI read 3 ways and agreeing to the hundredth: **Tampa 7.18 · Punta Gorda 6.51 · North Port 6.34 · Cape Coral 5.96 · Lakeland 6.13 ⇒ 4-of-5 > 6.00.**
| Rule | What reading #7 (9/28) is under it | Leg state |
|---|---|---|
| **8/23 letter (in force)** | 4-of-5 > 6.00 — no re-fire condition exists, so **no rule applies** | **🟠** |
| **Proposed letter** | Cape Coral 5.96 sits inside the 5.90–6.00 band: **not** a re-fire reading (not > 6.00), **not** a stand-down reading (not < 5.90) | **🟠** |
- ⇒ **Adopting the proposal changes nothing today.** That is intended: the amendment must not be chosen for what it does to the current state. It would have prevented the 9/13 stand-down (Cape 5.91 is inside the band) — **I state that openly; it is the defect being fixed, not a reason to re-grade 9/13, which stands as graded.**

## DAEDALUS gate-basis residuals (9/17 packet) — answered by the letter above
Metros named · clock named (page stamp) · tie convention (strict > 6.00) · "reading" defined · reset defined. DAEDALUS's final recheck (9/17) withdrew its asks; these are folded in anyway because they cost nothing once the letter is re-cut.

## ASK
**Will: approve / amend / decline the proposed letter.** On approve, PROME re-cuts `GATES.tsv` `GATE-CORAL-MSI-01` as a pointer; CORAL installs the letter under the 8/23 text in STATUS OQ §A and adds a THESIS changelog entry the same session.

$0 · no position · no threshold moved until ruled.

— CORAL *(carve-out ① packet, self-committed)*
