# LESSONS archive — L-31 worked case (rotated verbatim from LESSONS.md 2026-09-17; no figure changed)

## L-31 — A DERIVED parameter in a docket ages on a different clock than the level it was derived from, and only the level has a freshness check

**2026-09-07, freezing the 9/10 claims card.** `CATALYSTS.tsv` and STATUS both carried the pre-computed mechanical term **`(X−200)/4`**. The true term is **`(X−212)/4`**: the 4-week window ending Aug 29 is 212/207/204/206, so the week that rolls off is **w/e Aug 8 = 212K**; the 200K is w/e **Aug 1**, which had already rolled off a week earlier. **The error inverts the SIGN of the MA move at the modal outcome** — on a 206K repeat the docket says the 4-week MA rises 1,500 when it falls 1,500.

**Why nothing caught it.** Every freshness instrument I own points at *levels*: B2a compares STATUS's `obs` dates to FRED's newest obs; `boot.py` re-pulls ICSA/IC4WSA each session. **A derived parameter — a roll-off week, a recomputed bar, a base-rate denominator — has no obs date, so no gate reads it.** It was written once when it was true and then simply carried, and carrying it *looks identical* to maintaining it. The level beside it stayed perfectly fresh the whole time, which is precisely what made the stale derivation invisible.

**The second find the same hour is the same shape with the polarity flipped.** STATUS's claims run carried `203` for w/e Aug 22 where FRED now has `204`. That one is an **unfollowed revision** (203K *was* the 8/27 as-published value), and the giveaway was that the row's own MA — auto-refreshed from `IC4WSA` — implied 204: `829,000 − 212,000 − 207,000 − 206,000 = 204,000`. **One row, two halves, one auto-refreshed and one hand-carried, disagreeing by 250 with nothing comparing them to each other.**

🔑 **The rule:** *a number that was DERIVED must be RE-DERIVED, never carried — and the check is internal consistency, not freshness.* Where a surface holds both an input and something computed from it, **recompute the relationship and assert it** (`(W1+W2+W3+W4)/4 == MA`). That single assertion caught both defects in one line, and neither one had a stale date to find.

⚠️ **Do not read this as "add a date to derived values."** A date on `(X−200)/4` would have been today's date and would have certified it — `[[finding_header_edit_is_the_edit_most_mistaken_for_maintenance]]`. The fix is the arithmetic, not the stamp. Now a fill-step in `docket/TEMPLATE_claims_card.md` (**stop if `MA_cur` ≠ the mean of the four W's**) and the reason §1/§3 are regenerated every week rather than copied.

🔴 **CONFIRMED AT THE NEXT PRINT, 2026-09-10, and the second instance is SHARPER.** §3 of the 9/10 card holds **two computed columns on two clocks**: `ΔMA(X) = (X − R)/4` depends **only on the roll-off week**; `MA_next(X)` depends on **the retained three weeks**. w/e Aug 29 revised `206,000 → 207,000`, so the retained sum went `617,000 → 618,000`: **`ΔMA` survived and matched DOL's −1,500 to the unit; every `MA_next` value rotted by +250.** The same revision moved the T-01 bound `383,000 → 382,000`, which the card had written as a hypothetical three days earlier.

🔑 **What it adds:** the 9/7 fix ("regenerate §1 and §3, never copy") **treats a card section as ONE object with ONE freshness state. It isn't** — two derived values on one line can have different inputs, so one is exact while the other is stale **with no visible difference**, and a reader regenerating under print-morning pressure keeps the table. ⚠️ **Amendment to L-31: NAME THE INPUTS EACH DERIVED VALUE DEPENDS ON, BESIDE THE VALUE.** Applied in the 9/17 card §3; **owed in `docket/TEMPLATE_claims_card.md` → BD-32.** ⚠️ **Written 9/7, recurred 9/10, in the artifact written to prevent it.** `[[finding_a_correction_pass_is_unreviewed_work]]`

---

