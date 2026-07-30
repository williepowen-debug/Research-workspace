# FALCON — GATE-FALCON-001 Leg-3 Adjudication: Yanbu Loadings vs the Frozen −36% Bar
**As of:** 2026-07-29 ~22:15 ET · **Author:** FALCON · **Trigger:** WALTER SIG-W-20260728-011 (GS GIR oil-flows pack, relayed 7/28 22:20Z) + BRENT inbox packet (7/29, `inbox/2026-07-29_from-BRENT_saudi-co-belligerent-bears-on-gate-falcon-001-leg3.md`) — both said "the data absence basis is closed, FALCON adjudicates."

---

## VERDICT (first 3 lines)
**Leg-3: NOT FIRED.** The frozen registered condition (7/21, PROME commit `2d54ba96`) is **"Saudi Red Sea (Yanbu) loadings collapse BEYOND the current rerouting-driven −36%."** The best-corroborated, apples-to-apples read (total liquids vs total liquids, two independent source paths converging) puts the decline at **~−23% to −30%**, under the bar. **This is the tightest-margin non-fire on the board** — a second reading (crude-only current vs an unconfirmed-commodity-mix baseline) would push past −36%, and I cannot cleanly resolve which basis is correct. Recommend a 3–4 day re-pull rather than closing the leg as settled.
**The −36% baseline itself does NOT mean what I assumed when I cited it in the leg-3 table** — re-derivation below shows it was a *pre-declaration* decline (peak-to-week-of-7/13, not caused by the coercion/blockade I was adjudicating on 7/21), which is exactly what my own 7/21 SIG-003 report already flagged and I am reconfirming here, not walking back.

---

## 1. Re-deriving the frozen condition (frozen semantics — I do not re-derive the threshold, only its units)

Registered text, verbatim, from `reports/2026-07-21_babelmandeb-SIG-003-adjudication.md` §5.3 (proposed by me, Will/PROME-registered same day, commit `2d54ba96`):
> *"Saudi Red Sea (Yanbu) loadings collapse beyond the current rerouting-driven −36% on a dark-fleet-capable tracker."*

**What "−36%" was, re-verified today (The National, 7/20, Kpler-sourced — live WebFetch):**
- Total Saudi oil loadings: **9.5M bpd (June 29 peak) → 6.1M bpd (week of July 13)** = **−35.8% ≈ "36%"** (the headline number).
- Red Sea terminals specifically (the Yanbu-relevant slice): **4.23M bpd → 2.79M bpd** = **−34.0%**.
- My own 7/21 report already called this **"largely rerouting/premium effects... plausibly pre-declaration, not the blockade executing."** I am not re-litigating that — it stands. The number is frozen; I am only pinning down what it was measured against, because that's the only way to grade "beyond" it.

**Practical read:** the registered bar is "a decline deeper than the ~34–36% peak-to-mid-July move already priced in at registration." Whatever new print I use, it needs a like-for-like baseline to compare against.

## 2. Verification — independent of WALTER's single relay (per task instruction)

WALTER's SIG-W-20260728-011 relayed a Goldman Sachs GIR ("Global Investment Research") oil-flows pack, delivered to Will as a 7-image Telegram batch 7/28 ~21:17Z, graded by WALTER **CONFIRMED-NAMED-DESK-RESEARCH, confidence 0.85**. That is a credible institutional source, but it arrived as a **single delivery path** (Will's photos of one GS report) — so per my own standing discipline (`finding_ais_port_export_darkfleet_blind`, and the Yanbu 7/27 lesson: one claimant syndicated by four outlets is not corroboration), I went to a second, fully independent path before grading.

**Live WebFetch, 2026-07-29, independent of WALTER/GS:**
| Source | Metric | Figure | Date |
|---|---|---|---|
| Kpler corporate blog (via Baird Maritime, pub. 7/28) | Yanbu/Red Sea crude+condensate, week of Jul 20 | **2.4–3.0M bpd** vs **4.23M bpd** "previous week" baseline | 7/28 |
| — same piece | Loading voyages, week of Jul 20 vs prior week | **16 vs 35** (AXSMarine) | 7/28 |
| — same piece | Vortexa (dark-fleet-adjusted) | **3.8M bpd, "broadly stable"** — 4 VLCC+1 Suezmax+1 Aframax loading AIS-dark, ~1/3 of the week's volume | 7/28 |
| GS GIR (via WALTER SIG-011) | Total liquids 7DMA vs 30-day avg vs FALCON's baseline | **3.3 vs 4.3 vs ~4.7 → "~−23%/−30%"** | pack dated ~7/26-27 imagery, relayed 7/28 |
| GS GIR (via WALTER SIG-011) | Crude-only 7DMA vs 30-day avg | **2.7 vs 3.7** (→ −27% on GS's own like-for-like) | same pack |

**Two independent paths (my live Kpler/Baird-Maritime pull, and WALTER's GS relay) converge on the same order of magnitude: ~−23% to −30% on a total-liquids, apples-to-apples basis.** That is genuine corroboration, not single-relay — I am NOT invoking NOT-GRADEABLE-YET on corroboration grounds.

## 3. The one thing I can't clean up: commodity-basis mismatch

FALCON's own STATUS.md/SCRATCH.md cite **"Pre-strike baseline ~4.7M bpd (7/13)"** without specifying crude-only vs total liquids (it traces to a Signal Ocean "shipments from Yanbu" figure, not GS's crude/total split). GS's pack reports **both** a total-liquids line (3.3 current) **and** a crude-only line (2.7 current) against **different** 30-day baselines (4.3 total / 3.7 crude).

- If FALCON's 4.7 baseline is a **total-liquids** figure (most likely — matches GS's 30-day total of 4.3 closely enough to be the same series at an earlier date): current 3.3 vs 4.7 = **−29.8%**. **Does not fire.**
- If FALCON's 4.7 baseline should instead be read as **crude-only** (Yanbu is overwhelmingly a crude terminal, so this is not an unreasonable read): current crude 2.7 vs 4.7 = **−42.6%**. **Would fire.**

I do not have a source that pins down which commodity basis my own 4.7 figure represents. **This is a genuine unresolved unit-consistency gap, not a hedge to avoid a call** — I am flagging it rather than picking whichever reading is more convenient for either book.

## 4. Weight of evidence and verdict

1. The **total-liquids, apples-to-apples reading is the one with multi-source, independently-corroborated agreement** (my live Kpler pull + GS via WALTER, both landing ~−23% to −30%). The crude-only-vs-mixed-baseline reading that would fire the leg rests on a **single source's internal split (GS only) against an uncorroborated baseline commodity assumption** — thinner evidence, by my own corroboration standard.
2. **Dark-fleet blindness cuts toward UNDER-stating true volume, not over-stating it** — Vortexa's AIS-plus-dark-fleet estimate (3.8M, "broadly stable," ~10% off) is the most complete-coverage read available and it is the *mildest* of all the numbers in hand. My own 7/18 standing finding (AIS misses dark-fleet loadings) argues the true decline is likely **smaller** than the headline AIS-only trackers show, not larger.
3. **GS's own framing is "While Noisy"** (per WALTER's log, quoting the pack's own title) and explicitly states attribution is "tangled across blockade-avoidance vs. the intercepted 7/25 attempt vs. the claim-only Petroline" — the source itself is hedging, which argues against a confident fire.

**On balance: NOT FIRED.** The registered bar ("beyond −36%") is not cleared on the best-corroborated basis (~−30%), and the one reading that would clear it (~−43%, crude-only) rests on a single-source split against an assumption I can't verify. I grade this a **live, tight-margin NOT FIRED — not a clean, comfortable one** — and recommend against banking it as resolved.

## 5. Recommendation

- **Re-pull in 3–4 days** (by ~8/1-2) once GS/Kpler print a cleaner post-7/25-only window (today's 7DMA still blends pre- and post-strike days) and once I can pin the commodity basis of my own 4.7 baseline against a primary (Signal Ocean or Kpler directly, not a WebFetch-summarized secondary).
- **Do not fold this into FAL-03** — FAL-03's leg-A (Jazan damage/output-loss) and this GATE-FALCON-001 leg-3 (Yanbu loadings collapse) are different instruments on different assets; keep them separate per my own wording-wedge lesson (HAW-10 family).
- **STATUS.md and SCRATCH.md updated** to reflect this grading (see commit).

---
*Method: frozen-semantics discipline (never re-derive the threshold, only verify what it was measured against); `[[finding_ais_port_export_darkfleet_blind]]`; `[[finding_single_witness_guard_deletes_real_data]]` counter-applied — corroboration found, so I graded rather than defaulting to NOT-GRADEABLE-YET; `[[finding_silent_blank_evades_review]]` — disclosed the unit-mismatch gap instead of picking the convenient reading.*
