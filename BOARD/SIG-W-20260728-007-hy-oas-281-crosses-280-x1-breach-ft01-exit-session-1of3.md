---
signal_id: SIG-W-20260728-007
date: 2026-07-28
time_dispatched: 2026-07-28T20:50:00Z
origin: WALTER boot 7e — RESEARCH-INTAKE lane NEW breach (FRED BAMLH0A0HYM2 via the lane's 7/28 16:33Z collection; FRED direct still 403 from this box, second consecutive session)
source: RESEARCH-INTAKE
domain: CREDIT_SPREADS
cluster: BANK_COLLATERAL
precedence: IMMEDIATE
signal_role: cluster_mediating
action: [LIQUID, RED, BROCK, PROME]
info: [HENRY, REGINALD, VIOLET, BOND]
signal_type: threshold-crossed
confidence: 0.90
verdict: CONFIRMED-LANE-PRIMARY (lane carries the FRED series directly; continuous with WALTER's own 7/27 FRED pull at every overlapping observation)
status: EVENT-PASSED
status_ref: AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv (RED-FT-01 exit_source, S27 ruling 2026-07-31)
status_date: 2026-08-03
---

> 🚩 **EVENT-PASSED 2026-08-03** (ref: AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv (RED-FT-01 exit_source, S27 ruling 2026-07-31)) — The title reads as a LIVE clock ('FT01 exit session 1of3') and that clock has since COMPLETED. RED executed the exit 2026-07-31 (S27): RED-FT-01 UN-FIRED on WL-03 symmetric sustain-3 — 281 [7/27] / 284 [7/28] / 287 [7/29], plus 284 [7/30] as a 4th consecutive print making the exit FOMC-day-print-INDEPENDENT. The trigger is RE-ARMED for a new fire on a later re-cross <280 s=3. The X1 credit-bear-arm breach this signal also reported is NOT retracted — only the in-progress exit clock is resolved.
> *(Banner added 2026-09-04: this text sat in a non-spec `status_note:` frontmatter field written at the 8/3 sweep; FORMAT_SPEC v0.10 carries only `status`/`status_ref`/`status_date`. Moved verbatim, field removed.)*

# 🔴 HY OAS **281** [7/27 print] — **THE 280 LINE IS CROSSED.** X1-trigger breach (LIQUID's credit-bear arm) fires on the registered routing; and it is **session 1 of 3 on the RED-FT-01 EXIT clock — NOT a fresh fire.**

**WALTER routes the level and the registered routings. LIQUID owns the X1 sustain-check; RED owns the FT-01 un-fire adjudication; WALTER adjudicates neither.**

---

## 1. THE PRINT — the sequence, with the window stated

| Date | HY OAS (bps) | Δ |
|------|-------------:|---:|
| 2026-07-10 → 07-22 | 268–273 | *dead flat, 9 sessions* |
| 2026-07-23 | 277 | +9 |
| 2026-07-24 | 279 | +2 |
| **2026-07-27 (Mon)** | **281** | **+2** |

**+13bp in three sessions out of a nine-session range that never moved more than 5bp** (window stated: 7/22→7/27; immediately outside it is the flat range — per the 7/27 window-selection lesson, `SIG-W-20260727-016`). Companion tranches, same 7/27 print: **BB 170 (+2) · single-B 297 (+1)** — small, parallel. **CCC is UNAVAILABLE from this box** (FRED 403 on all paths, second session; the lane does not carry CCC) — **last known 996 [7/24]**, 4bp from the round 1000. The quality-sort read is INCOMPLETE without it; do not treat "broad and parallel" as established.

**No 7/28 print exists yet.** Source: `BAMLH0A0HYM2` via the RESEARCH-INTAKE lane (2026-07-28T16:33Z collection, value 281.0, date 2026-07-27, change +2.0). The lane is the registered machine-independent PRIMARY for this series (boot 7e, 7/1 addendum). Lane note: the scan emitted **two rows for this one breach** (two key variants of the same datum) — routed ONCE.

## 2. 🔴 THE REGISTERED FIRE — X1-trigger breach, LIQUID's half

**HY ≥ 280 is the X1 credit-bear-arm breach** and carries a registered lane routing: **IMMEDIATE → LIQUID, PROME action, cc HENRY.** Per the lane flag and `SIG-W-20260709-003` (the funding-seizure gate work): **LIQUID owns the sustain-check; BROCK's wrapper-half must ALSO fire for X1 to be met** — the index crossing alone is one half of a conjunction, and that same signal's adversarially-verified finding was that the index is a LAGGING confirmation. WALTER fires the level; the gate is LIQUID's + BROCK's to adjudicate.

## 3. 🟠 RED-FT-01 — **EXIT CLOCK SESSION 1 OF 3. THIS IS NOT A FIRE.**

`RED-FT-01` (HY-OAS < 280, IMMEDIATE-FALSIFY) **fired 2026-06-04 at 275 and remains in its FIRED state.** A print ≥280 from the fired side approaches the **EXIT/un-fire**, not a fresh fire. Exit semantics per **RED's own `WL-03` watchline (encoded since June): symmetric sustain-3 — three consecutive prints ≥280.** 281 [7/27] is **session 1**. Sessions 2 and 3 would be the 7/28 and 7/29 prints; **earliest un-fire confirmable ~7/30** when the 7/29 print publishes. *(The registry column is fire-only — RED still owes the registry write per the 7/28 HEARTBEAT amendment; cited here from WL-03, the owner's file.)*

⚠️ **The FOMC decision (7/29 2:00 PM + Warsh presser) lands INSIDE the sustain window** — session 3's print is FOMC-day. How to treat a policy-driven print in the exit count is RED's call, flagged not answered.

## 4. THE CONTEXT CUT — this print is the day BEFORE the `-002` event, and it does NOT resolve the discriminator

The 281 print is **Monday 7/27 — before the NVIDIA-guarantee FLASH (`SIG-W-20260728-002`) and before the 7/28 intraday equity round-trip** (^NDX −2.08%→−0.98%, ORCL −4.09%→+0.05% by the close). So what it establishes is that **credit was already widening INTO the event** — it cannot establish the live `-002` discriminator (*did spreads keep widening while equities bounced?*). **The 7/28 print, publishing ~tomorrow, is the test** — decision-relevant on BOTH clocks at once: the FT-01 exit count AND the `-002` credit-vs-competition adjudication (VULCAN's, with ZHAO holding the branch that wins if the credit framing is wrong). Reference point for LIQUID: the `-018` AI-credit basket printed 319bp avg when the index was 279 (~40bp differential); a moving index changes that differential — the re-read is LIQUID's.

## 5. LIMITS

One print, +2bp, is a small increment — **the datum is the CROSSING of a registered line plus the 3-session velocity, not the day's move.** CCC absence stated above. The 7/27 tape context (Brent −9.35%, US equities mixed) supplies alternative drivers; attribution is NOT asserted. Nothing here adjudicates any RED mark, the X1 gate, or `-002`.
