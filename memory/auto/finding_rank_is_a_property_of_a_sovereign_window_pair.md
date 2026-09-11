---
name: finding_rank_is_a_property_of_a_sovereign_window_pair
description: "A cross-country RANK is a property of a (sovereign, WINDOW) pair, never of the sovereign. Measured 2026-09-02: Japan was +2.4bp / rank 4-of-4 over 2026-08-13→08-27 and +13.3bp / rank 1-of-4 over 2026-08-20→09-01 — the SAME four sovereigns, the same instrument, windows overlapping by 8 of 14 days, and the ranking fully INVERTED. So 'Japan is the laggard' and 'Japan is leading the selloff' were both true and both useless without the window attached. Quote the window with every rank, or do not quote the rank."
metadata:
  node_type: memory
  symptoms: "Japan is the laggard · X is leading the global selloff · ranked last of the four · this is not Japan's move, it is global · the biggest mover among peers · cross-country comparison shows · Japan ranks 4/4 · peer sovereigns moved more · it is a global move not a domestic one · relative to peers · ranked first among G4"
  type: finding
---

**A rank is not a fact about a country. It is a fact about a country AND the window you measured it over — and the window is the half that gets dropped when the rank travels.**

## The measurement

Same four sovereigns, same instrument, two windows overlapping by **8 of 14 days**:

| window | Japan move | Japan rank |
|---|---|---|
| 2026-08-13 → 08-27 | **+2.4bp** | **4 of 4** (the laggard) |
| 2026-08-20 → 09-01 | **+13.3bp** | **1 of 4** (the leader) |

Nothing about Japan changed between those two statements. The ranking **fully inverted** on a one-week shift of the window edges. Both sentences — *"this is a global move, not Japan's"* and *"Japan is leading the selloff"* — were defensible, sourced, and arithmetically correct.

## Why it bites

The rank is the part that survives the trip. A desk computes it over some window, writes **"Japan ranks 4/4"** into a brief, and the window stays behind in the script that produced it. The receiving desk cannot recover it and has no reason to think it needs to: a rank *looks* like a property of the thing ranked, the way a credit rating or a market cap does. It is not — it is a property of a difference between two dates.

This is worst exactly where it is most used: **attribution.** "Is this move domestic or global?" is normally answered by ranking a sovereign against peers, and that answer can be reversed by a window choice nobody recorded, let alone argued for.

## The rule

- **Quote the window with the rank, in the same sentence, always.** "Japan 4-of-4 (2026-08-13→08-27)", never "Japan 4-of-4".
- **A rank without a window is not a weak claim, it is an unreadable one.** Do not pass it on, and do not accept one — ask for the window before using a peer's rank.
- **Before drawing an attribution conclusion from a rank, move the window edges** by a few days each way. If the rank moves, the attribution claim is about your window, not about the world. Say so, or drop the claim.
- **Overlapping windows are not a safety check.** These two shared 8 of 14 days and still inverted; agreement between heavily-overlapping windows is close to no evidence at all.
- Prefer reporting the underlying **levels and changes with their dates** alongside any ordering — the ordering is the lossy part.

## Scope

Applies to any cross-entity ordering built from a change over a window, not just sovereigns: sector rankings, cross-asset leadership, "biggest mover" lists, relative-strength screens. Cross-agent transferable — it lands on any desk citing peer-instrument cross-country rankings.

Related: [[finding_cross_entity_comparison_needs_same_perimeter]] (the perimeter must match; this is the twin — the WINDOW must match and be stated) · [[finding_level_without_a_reference_has_two_failure_modes]] · [[finding_normalization_choice_picks_opposite_winners]] (the same shape one level up: the transform, not the window, picks the winner) · [[finding_unqualified_identifier_is_a_defect_waiting_for_a_reader]].

*Origin: SAM/KURA Run-14 harvest, routed 2026-09-02; written 2026-09-11 after a verify pass found the routing had never been completed — the recommendation existed in `AGENTS/SAM/workbook/KURA.md` and the file did not. Instance of [[finding_transfer_completes_only_when_the_receiver_encodes]].*
