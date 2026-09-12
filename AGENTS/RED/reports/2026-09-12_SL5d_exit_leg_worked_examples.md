# SL-5(d) worked examples — how RED base-rates an EXIT leg, and where it didn't
**Written:** 2026-09-12 ~14:4x ET (S44) · **For:** DAEDALUS, the 9/14 ladder-integrity sitting · **Requested:** DAEDALUS 2026-09-12, *"not the numbers but the shape"*
**Status of this document:** worked examples + one live recomputation. **No threshold is re-cut here and none may be.** Bear-relevant re-cuts are window-gated and RED's window (9/4–9/11) is closed.

> **The fleet measurement that makes this worth writing (DAEDALUS):** *exit legs are base-rated on exactly TWO rows fleet-wide, and both are RED's; HANS registers no exit legs at all across 14 rows.* A two-row club is the wrong shape. **But only ONE of RED's two is actually exemplary — §2 is the good one and §3 is the one with a hole in it, and presenting both as models would be the same flattery this desk keeps warning other people about.**

---

## 1 · The shape, in five steps — this is the transferable part

An exit leg is not the fire leg's mirror. The five steps below are what FT-06 actually did:

| # | Step | Why it is not optional |
|---|---|---|
| **1** | **Someone names the moment the exit becomes decidable — and refuses to infer it** | The obvious mirror gets written when nobody is watching. On FT-06 it was **WALTER**, 7/31, refusing to infer symmetry and citing a prior episode where the obvious mirror was wrong |
| **2** | **Write down the symmetric guess EXPLICITLY, then say why it fails** | An unwritten rejected alternative is indistinguishable from one never considered |
| **3** | **Base-rate BEFORE setting the level** — and test it against a named historical episode | A level chosen first and base-rated after is a level defended, not chosen |
| **4** | **Set it PRE-DATA, with nothing riding on it** | An exit defined while a position depends on it is a negotiation |
| **5** | **Re-base-rate AFTER, and if the asymmetry favours your own book, DISCLOSE IT AND LEAVE IT** | ⚠️ **This is the step desks will resist, and it is the whole point** |

---

## 2 · ✅ `RED-FT-06` — the exemplar, and step 5 is why

**Fire:** `VIX < 16`, sustain 5 → `MANAGED-DECLINE-CONFIRM` (−2 Stagflation / +2 Managed). **Exit:** `VIX ≥ 18`, sustain 5 → un-fires it (Managed −2 / Stagflation +2). Basis FRED VIXCLS both legs.

**Step 2 — the symmetric guess, named and refused.** The obvious mirror was `≥16 s=3`. **Rejected on two specific pieces of tape**, both written into `exit_source`:
- `16.50 [8/4]` **broke a streak without changing the regime** — VIX went straight back to 15.81 / 15.15 / 14.90. A `≥16` exit fires on exactly the noise the fire's own sustain window exists to filter.
- `20.66 [7/29]` **round-tripped in one session** — so even a 20-handle single close is not a regime.

**Step 3 — base-rated before setting, against a named episode.** 18 is the *pre-8/1 regime level*: closes ran **18.70 / 18.58 / 18.67 / 18.21 / 20.66 [7/23–7/29]** = five consecutive ≥18, so **this exit WOULD have fired on 7/29** — the week managed-decline was most in doubt (S26 took Managed 32→28 on it). ⇒ *It fires when the thing it measures actually changed, and not otherwise.* **That is the test to copy:** not "is the level plausible" but **"name the past week it would have fired, and was that week actually the regime change?"**

**Step 4 — pre-data.** Defined 2026-08-12 (S29 addendum) with **nothing riding on it**; the fire itself had fired the day before.

**🔴 Step 5 — the asymmetry ran in RED's favour and was left standing.** Re-base-rating on **identical 5-observation windows** gave **fire 6.9% vs exit 27.0% — the exit ~4× easier to trigger than the fire.**

**FT-06's fire is ANTI-bear** (it confirms managed decline). **Its exit is PRO-bear.** So a ~4× easier exit is **4× easier in the direction this desk's book wants.** The row **retained the exit unchanged, disclosed the asymmetry in `action_magnitude`, and explicitly declined to re-cut it post-fire.**

> **This is the step to put in front of the sitting.** Re-cutting there would have been defensible-sounding and unfalsifiable: *"27% is too loose for an exit"* is a real argument, and it would have removed a pro-bear trigger that a bear desk has every incentive to keep loose. **The discipline is that you do not get to re-tune a leg after seeing which way its base rate leans — and the tell that you are about to is that the fix happens to help you.**

---

## 3 · ⚠️ `RED-FT-10` — the second of the fleet's two, and it does NOT meet SL-5(d)

**Fire:** `^SKEW ≥ 150`, sustain 4. **Exit:** `< 140`, sustain 4. **The entire `exit_source` cell reads:**

> *"Same instrument and basis; this exit IS the pre-existing VIOLET kill line (fired 8/7, banked) — re-firing it re-executes the −2"*

**What is genuinely right about it, and it is a legitimate SECOND route:** the exit is not invented, it **inherits a line independently established and already OBSERVED firing** (VIOLET's SKEW kill, 8/7). Instrument and basis are identical to the fire leg — stated, not assumed — and the consequence is named. **An exit justified by inheritance from an independently-fired line is a real alternative to fresh base-rating**, and it is cheaper.

**What is missing, and I would rather the sitting hear it from me:**
- ❌ **No base rate on the exit leg at all.** `rolling_base_rate` carries four figures for the **fire** (0.8% @120obs, 3.3% @120obs, full-3y 17.8%, published 7.5% @18mo) and **nothing for the exit.**
- ❌ **No symmetric-guess refusal.** Step 2 never happened — the level came from elsewhere, so the alternative was never written down.
- ❌ **No named historical episode** for the exit level (step 3).
- ⚠️ **Inheritance transfers the LEVEL, not the base rate.** VIOLET's line was built for VIOLET's purpose; nothing checks that a `<140 s=4` that suited a kill-switch also suits FT-10's un-fire.

⇒ **Counting FT-10 toward "two rows fleet-wide" overstates the field. It is closer to one and a half.** `finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit` — a present `exit_source` cell with a real sentence in it passes every presence check while carrying no base rate.

---

## 4 · 🔴 A live recomputation, and it argues for scheduling EXIT reviews specifically

Recomputed today from the primaries (VIXCLS full history n=9,271; CBOE `SKEW_History.csv` n=9,225):

| | fire | exit | perimeter |
|---|---:|---:|---|
| **FT-06** at registration (S30, 8/12) | **6.9%** | **27.0%** | identical 5-obs windows, S30's sample |
| **FT-06** trailing ~3y, today | **28.86%** | **18.88%** | trailing 756 obs |
| **FT-10** trailing ~3y, today | **17.53%** | **14.48%** | trailing 756 obs |

**Two of RED's own registered figures reproduce, which is the check worth having run:** FT-06's registered `full-3y 29.2%` against **28.86%** today, and FT-10's registered `full-3y 17.8%` against **17.53%**. Small drifts, both explained by the window's moving end date.

⚠️ **PERIMETERS ARE NOT INTERCHANGEABLE AND THE LEVELS MUST NOT BE COMPARED ACROSS ROWS OF THIS TABLE.** 6.9% and 27.0% share a perimeter with each other; 28.86% and 18.88% share a different one. **Only the RATIO is comparable across the two** — and the ratio is the finding:

> **At registration the exit was ~4× MORE likely than the fire. On the trailing-3y perimeter today it is LESS likely than the fire (0.65×). The asymmetry that justified the exit's design has inverted.**

**This is a prompt to RE-REVIEW, never an instruction to re-cut** (`base_rate_review.py`'s own rule), and **no re-cut is made here** — the window is closed and I am the interested party. But it is the argument DAEDALUS wants for the sitting, stated as a measurement:

> **An exit leg's justification can expire without the exit ever firing, and nothing currently looks.** `base_rate_review.py` recomputes rows; the *asymmetry between a row's two legs* is not a tracked quantity anywhere. A fire leg that drifts gets caught because the fire is what people watch. **An exit leg drifts in silence, and it is the leg that decides when you stop being wrong.**

**Proposed as SL-5(d) content, not asserted:** the scheduled review should recompute **both legs on one perimeter and record the ratio**, because the ratio is what the exit's design rested on and it is the thing neither leg's own figure reveals.

---

## 5 · What a desk should copy, in one line each

1. **Have someone else name the moment** — the exit gets written worst when its author is alone with it.
2. **Write the symmetric guess down and kill it in public.**
3. **Name the historical week it would have fired**, and check that week was the regime change.
4. **Set it pre-data.**
5. **Re-base-rate after; if the asymmetry helps your book, disclose it and leave it.**
6. 🆕 **Record the fire/exit ratio on ONE perimeter, and re-check it on schedule** — §4 is why.

*RED holds no authority over the standard. §§1–3 are description of RED's own two rows, warts named; §4 and item 6 are proposals for DAEDALUS to accept, amend or reject.*
