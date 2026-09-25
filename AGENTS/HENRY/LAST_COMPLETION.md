# HENRY — LAST_COMPLETION

**Session:** 2026-09-24 Thu 22:41 ET → 2026-09-25 Fri 01:15 ET (`date`, at closeout write), launched in-folder. **Will-directed:** boot, a peer read of VIOLET/LIQUID/BOND, correction packets, a cross-desk synthesis, the October-hike odds, then PROME's bounded follow-up (Will's items 2 + 4, 01:01 ET) with BOND and ORACLE.
**Status:** ✅ **COMPLETE.** PROME confirmed it received the follow-up; nothing more is owed on it. No threshold moved, no prediction registered, no trade view, $0.

## CHANGED (files)
- `research/2026-09-24_peer-read_VIOLET-LIQUID-BOND.md` (new): the three desks' reads, where they bear on HENRY, 4 peer-surface defects, and a cross-desk synthesis.
- `research/2026-09-24_fedwatch-method-october-odds.md` (new): October hike odds computed with the FedWatch method.
- `research/2026-09-25_rates-move-and-hike-alignment.md` (new): the deliverable for PROME items 2 + 4.
- `STATUS.md`: hike-odds cells re-based from "unverified" to measured; 9/24 SESSION row 11 added; the catalyst row is aligned with ORACLE. `NEXUS_BRIEF.md`: conviction line and FOMC row.
- Packets: `AGENTS/VIOLET/inbox/…correction-STATUS-87…` · `AGENTS/LIQUID/inbox/…correction-stale-BOTTOM-LINE…` · `PROME/inbox/2026-09-25_from-HENRY_items-2-4-…-COMPLETION.md`.

## RESULT (one line)
**This week's rate jump is the market pricing rates staying higher in 2027–28, not the October meeting. Expected rates after October and after December each rose 4bp, while late-2027 and late-2028 rose 19 and 22.5bp, as much as the 10-year (+22bp). Two days are contested: on 9/23 about half the move was term premium in the NY Fed's model, and on 9/24 the futures path barely moved at all.**

## Session Work
| Item | Outcome |
|---|---|
| Peer read (VIOLET · LIQUID · BOND) | All three agree with HENRY: the move was in real yields, funding is calm, and the CCC tail is wide. Four defects found in their files; **both desks applied the fixes within the hour** (LIQUID `e903519d2`, VIOLET `a16aa90f1`). |
| October hike odds | **~72% at 15:00 ET 9/24**, up from 56% on 9/22. This is my own FedWatch-method calculation on November fed-funds futures. CME blocks automated reads, and I did not get around that. Year-end: about +38bp, roughly 1.5 hikes. |
| Rates move, with BOND | Matched-date table 9/15→9/24. My preferred reading: the policy path was repriced for 2027–28. **The strongest evidence against it:** 9/23 split roughly +8.2bp path and +7.0bp term premium on BOND's ACM figures, on the day of the failed 5-year auction; and on 9/24 the 10-year rose 7bp while the futures path moved 1–2bp. BOND reached the same split on its own. |
| October odds vs betting markets, with ORACLE | **Only expected basis points can be compared, not probabilities.** At 15:00 ET: futures +18.0bp, Polymarket +16.5, Kalshi +16.1–16.6. The gap is the same size as the differences in what the two sides measure, so it is **not a disagreement.** ORACLE withdrew its earlier "venues 11–12 points below futures." |

## HONEST SCOPE
- **My own errors tonight, both caught before PROME acted on them:** (1) my first draft said neither term-premium model showed a rise. That was true for the whole window but false for 9/23, the day that mattered. (2) I typed a clock time in the PROME packet header (~01:4x) that was 30 minutes late. Both were corrected in follow-up commits.
- Futures prices are vendor last trades, **not CME settlements.** The risk premium inside futures is unmeasured.
- **The model reading that decides the question is unpublished:** ACM for 9/24 (about a day's lag) and Kim-Wright for 9/21 onward (weekly). If ACM shows term premium up again on 9/24, the two-day burst was premium-led.

## ADDENDUM 2026-09-25 02:30 EDT — FORUM-7 (Will 02:20 ET "proceed with #1")
- **Pre-registered, frozen and pushed before the deciding data:** the rule for whether 9/23–9/24 was Fed path or term premium. Governing commit `c1e9a7e5a`, BOND co-sign `f7efb8f76`, convener note `bc540e071`, PROME packet `1f1c63baf`. Neither desk read ACM 9/24 first (its daily file ended 9/23).
- **Caveat you'd want:** a PREMIUM verdict is ACM's ordinary answer on a big sell-off (73%); a PATH verdict would be the surprise.
- **My errors, caught before commit:** base rates first drawn from the wrong (monthly) sheet; a compromise rewrite that would have replaced BOND's co-signed rule — discarded unpublished.
- **Grades:** ACM 9/24 (~9/25) · Kim-Wright (~9/28–29) · final after dealer data 10/1 → verdict by 10/2.

## GAPS / Still pending
- Nothing is owed on PROME's follow-up. The 9/25 items below were deliberately not displaced by it.

## COMMITS
- `0b0390563` peer read · `9892f14ad` → VIOLET · `55fd8c077` → LIQUID · `a23b974e9` synthesis · `2eab069f7` October odds · `bf74fea99` rates-move draft · `e8aa8cda0` → PROME items 2+4 · `2d0f508e9` clock fix · (this commit) closeout.

## NEXT SESSION FOLLOW-UP
- 🔴 **Fri 9/25 after ~16:00 ET, before 18:00:** the HEN-46 F1 diesel-crack grade at the CME settlement (below $95.00 fires it; TERRY grades), then **re-measure the gamma board at the close.**
- Read ACM for 9/24 when it posts; it decides the 9/23–9/24 split.
- **Wed 9/30:** PCE + GDP, quarter-end settlement of ~$183B of notes (LIQUID/BOND's funding test), the Russian diesel-ban expiry, Japan's monthly intervention total, your TLT 77P expiry (TERRY's card). **Thu 10/1** ISM · **Fri 10/2** jobs.

## THESIS SNAPSHOT (frozen at close)
Rates are carrying the stress and have not passed it on: the 10-year is +22bp in two days, stock volatility only +10%, the junk index +5bp, funding unchanged. Markets are pricing a longer hiking path, not only October. The CCC tail is at a 3-year wide (CCC−BB 934bp). Dealer gamma is about zero, so there is no cushion either way. HEN-46 active at 0.35/0.30, F1 at its line.

## WILL_NEEDS
- **No decision tonight.** One caveat you'd want: **don't use "72%" or "the betting markets lag futures" without the basis attached.** The fair statement is: *"About +16–17bp on the betting markets versus about +18bp in futures at 3pm ET 9/24, before basis adjustments."*
