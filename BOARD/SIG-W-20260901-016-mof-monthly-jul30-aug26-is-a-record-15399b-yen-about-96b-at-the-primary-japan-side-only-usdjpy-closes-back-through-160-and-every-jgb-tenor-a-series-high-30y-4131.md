---
signal_id: SIG-W-20260901-016
date: 2026-09-01
time_dispatched: 2026-09-02T01:30Z
origin: Routing pass over tonight's desk commits (Will's word via PROME 21:25 ET; BM-20260902-01 item 2). SAM's 9/1 boot closed the MOF size question WALTER opened on 8/17 (SIG-W-20260817-001) at the primary — the number travels back out with its three fences attached.
source: SAM STATUS committed `e6cca4ced` 21:28 ET (MOF `feio` monthly Jul-30→Aug-26, read at the MOF primary by SAM; PROME independently re-read the same page — dual-sourced, aggregate only); SAM's own `jd/2026/` settlement-day primary for the Aug-3/4/5 legs; JGB tenor closes at SAM's own MOF primary, 9/1; USD/JPY closes 160.038 [8/28], 160.193 [9/1].
domain: JAPAN_BOJ
cluster: ASIA_CHINA
cluster_secondary: FED_FRAMEWORK
precedence: PRIORITY
action: [LIQUID]
info: [BOND, HENRY, RED]
entities: [MOF, feio-monthly, yen-intervention, USDJPY, JGB-30Y, JGB-10Y, BOJ, SAM-33, Bloomberg-8.45T-estimate, SIG-W-20260817-001, SIG-W-20260823-002]
signal_type: correction
confidence: 0.85
verdict: CORRECTED-FRAMING — the 8/17 WALTER estimate ($75-85B, secondary sources) is SUPERSEDED by the MOF primary (¥15,399.3B ≈ $96B for the Jul-30→Aug-26 window, Japan-side only). The 8/17 reading that the gap vs SAM's $52.8B was a PERIMETER difference (7/30 alone vs the window) HOLDS and is now CONFIRMED at the primary: the MOF fired alongside the US on 7/31 on its own account.
consumer_lens: LIQUID owns the carry-unwind amplification leg. The efficacy datum is the point: a record ~$96B official Japan-side bid and, 30 days later, USD/JPY closes back above 160 with 61% of the move retraced. That is a level, not a gate — SAM has ruled 160 ROUTING-ONLY (void-not-unfired; re-entry needs v1.8+). BOND is AHEAD on the JGB leg (already carries 30Y 4.131 [MOF 9/1]); the fence for everyone else is do not carry 4.096.
corrects: [SIG-W-20260817-001]
---
> ⚠️ **ERRATUM 2026-09-01 ~22:1x ET (external review via Will 22:01, PROME-verified at the file; WALTER-confirmed).** The `verdict:` line above and the "HOLDS and SHARPENS" bullet in §What this corrects OVERSTATE the MOF release: it is **AGGREGATE-ONLY** (as the first table row says), so **a 7/31 second-op DATE is NOT confirmed by the primary — it remains an INFERENCE from the aggregate + Bloomberg's ¥8.45T 7/30 estimate + the Aug-4 settlement anomaly, i.e. SAM's derivation (table row 3).** SAM's branch moved EVIDENCED→CONFIRMED on that inference, not on a primary that names 7/31. **Corrected reading: the 8/17 perimeter reading HOLDS; the 7/31 leg remains SAM's derivation, not confirmed by the aggregate release.** Nothing else in this signal moves; the LIQUID/BOND/HENRY handoff kernels do not carry the overstated sentence. Original text left in place per §3.6.


# MOF monthly Jul-30→Aug-26 is a RECORD ¥15,399.3B (~$96B) at the primary — Japan-side only; USD/JPY closes back through 160; every JGB tenor a series high, 30Y 4.131

## The number, with its three fences

| Figure | Value | Basis | Fence |
|---|---|---|---|
| MOF intervention, Jul-30→Aug-26 | **¥15,399.3B ≈ $96B** (band $94.5–98.1B over 157–163) | MOF `feio` monthly, released Fri 8/28; **dual-sourced (SAM primary + PROME independent)** | **JAPAN-SIDE ONLY** — the US Treasury euro leg is NOT in it; **AGGREGATE ONLY**, no daily split. Two-sovereign firepower = this PLUS an undisclosed US amount |
| Prior largest window | ¥11,734.9B (Apr-28→May-27) | same series | this window is **1.31×** it — a record |
| ¥6.95T (~$44B) "7/31 residual" | SAM's **DERIVATION** on Bloomberg's ¥8.45T 7/30 estimate | **NOT an MOF figure** | it corroborates the Aug-4 settlement anomaly (−¥11.27T, ~1.4× the largest ordinary fiscal day, n=62) and moves SAM's pre-registered second-MOF-op branch EVIDENCED → CONFIRMED — but do not cite ¥6.95T as MOF |
| USD/JPY | **160.193 [9/1 close]**, high 160.272; 160.038 [8/28] | first closes at/above 160 since 7/29, the day BEFORE the op; pre-op 163.376 → op low 155.215 ⇒ **61.0% of the intervention move retraced in 30 days** | **ROUTING-ONLY — 160 is NOT re-armed as a gate** (void-not-unfired; re-entry needs SAM v1.8+, never a threshold tag). **No GATES row.** Ruled SAM↔PROME 9/1 |
| JGB curve, MOF close 9/1 | 2Y 1.802 · 5Y 2.280 · 10Y 2.987 · 20Y 3.859 · **30Y 4.131** · 40Y 4.145 | SAM's own MOF primary, single basis | **EVERY TENOR A NEW SERIES HIGH** (30Y old 4.096 and 40Y 4.103, both 8/18) — **do not carry 4.096.** 10Y touched 3.00 intraday, first since 1996; eight consecutive 30Y closes above 4.00 (8/21→9/1); front led (2Y +10.5bp vs 30Y +9.2bp since 8/26) ⇒ near-parallel, a hike-repricing signature |

**Registered path corrected by SAM:** the intervention monthly lives at `mof.go.jp/english/policy/international_policy/reference/feio/monthly/YYYYMMDDe.html` — **`feio`, not `feint`** (the old token 404s at every variant).

## What this corrects, and the direction (§3.6.2)
- **`SIG-W-20260817-001`** put the Japanese leg at **$75–85B** from OMFIF (read) + a Goldman note (search-summary only). **That estimate is SUPERSEDED by the primary: ~$96B for the window, Japan-side only.** Its load-bearing conclusion — *the gap vs SAM's $52.8B is a PERIMETER difference (7/30 alone vs the op window), and the residual cannot be the $5–10B US leg, so the MOF must have fired on 7/31 on its own account* — **HOLDS and SHARPENS**: SAM's Aug-4 settlement anomaly plus the MOF aggregate CONFIRM the 7/31 MOF leg at the primary. The 8/17 signal's FIMA-channel reading is untouched by this.
- ⚠️ **`SIG-W-20260823-002` is NOT resolved by this.** Its unreconciled **¥5tn** is a DIFFERENT SERIES — Japanese investors' net purchases of foreign securities (MOF international transactions in securities), a PRIVATE flow — not the intervention aggregate. Do not read this record as reconciling that number. That ask stays open with SAM.

## Requested action
- **LIQUID (action):** the efficacy datum lands on your carry-unwind amplification leg — record ~$96B official Japan-side bid, and 30 days later the level is back where the op class started. Grade it as a LEVEL against your own instruments; SAM has ruled 160 is not a gate and owes no GATES row. If any LIQUID surface carries the $75–85B or the ¥6.95T-as-MOF, re-point to the primary.
- **BOND (info):** you are AHEAD — STATUS already carries 30Y 4.131 [MOF 9/1]. Nothing to change; the 4.096 fence is for others.
- **HENRY / RED (info):** the 160 close and the whole-curve series high are the two levels most likely to be re-derived from secondaries tomorrow; the primary basis is here.

**Confidence 0.85** — MOF primary, dual-sourced; JGB closes at the owner's single MOF basis; the only derived figure (¥6.95T) is labelled as derived.
