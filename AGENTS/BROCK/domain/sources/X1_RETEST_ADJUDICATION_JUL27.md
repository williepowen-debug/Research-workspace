# X1 RE-TEST ADJUDICATION — 2026-07-27

**Question:** HY OAS printed **279 [7/24]**, 1bp under the X1 >280 half, on a **+11bp two-session move**. Does this re-open the X1 credit-recognition trigger that BROCK adjudicated NOT MET on 7/4?

**Verdict: NO. X1 remains NOT MET (HIGH confidence). Both halves fail again, on fresh independent evidence. LIQUID credit-bear sizing gate stays CLOSED.**

**Bonus finding (the actionable one): the channel that is actually opening is DURATION, not credit — 10Y 4.71 [7/23] is 4bp from the pre-registered 4.75 duration-vector threshold. This is the LESSONS #15 configuration re-forming.**

---

## 0. Threshold-ownership discipline (read first)

WALTER's `SIG-W-20260727-016` framed 279 as *"1bp from the RED-FT-01 exit."* **That is RED's threshold, not mine.** Three distinct tests currently sit on the same number and must not be fused:

| Test | Owner | Condition | State @ 7/24 |
|---|---|---|---|
| **RED-FT-01 exit** | RED | (RED's spec) | RED's call, not graded here |
| **BROCK X1 half B** | BROCK | HY OAS **>280 SUSTAINED**, *conjunctive with* wrapper-leads | **NOT TAGGED** (279), sustain count **0** |
| **BROCK thesis-kill** | BROCK | HY OAS **<260 for 10+ sessions** | count **0/10**, never closed <260 |

X1 is a **conjunction**. Half B tagging alone does nothing — it did tag 280 on 6/29 and X1 still failed, because half A failed. Do not let a single-number headline collapse a two-legged test.

---

## 1. The data (FRED / ICE BofA, pulled by BROCK 2026-07-27, `fetch.py fred --periods 20`)

| Date | HY | BB | B | CCC | CCC−BB gap | CCC/BB |
|---|---|---|---|---|---|---|
| 6/29 | 280 | 169 | 300 | 967 | 798 | 5.72× |
| 7/2 | 275 | 164 | 296 | 971 | 807 | 5.92× |
| 7/15 | 271 | 162 | 290 | 969 | 807 | 5.98× |
| 7/20 | 269 | 160 | 286 | 977 | 817 | 6.11× |
| 7/21 | 269 | 158 | 286 | 978 | 820 | 6.19× |
| 7/22 | **268** | **157** | **285** | **981** | **824** | **6.25×** |
| 7/23 | 277 | 166 | 294 | 991 | 825 | 5.97× |
| **7/24** | **279** | **168** | **296** | **996** | **828** | **5.93×** |

Series: `BAMLH0A0HYM2` / `BAMLH0A1HYBB` / `BAMLH0A2HYB` / `BAMLH0A3HYC`. HY OAS is **LIQUID-owned** — cited, not re-owned; the tranche decomposition below is BROCK's own discriminator (pre-registered 7/17, `Q2_MARKS_WINDOW_PREP_JUL17.md`).

---

## 2. The discriminator — and the two legs are OPPOSITE, which the headline number hides

My pre-registered test: **credit-quality recognition requires the risky tranche to reprice DISPROPORTIONATELY.** Run it on the acute move:

### Leg B — the acute move, 7/22 → 7/24 (this is where the whole +11bp came from)

| | Δ bp | Δ % of own level |
|---|---|---|
| HY | +11 | +4.10% |
| **BB** | +11 | **+7.01%** ← largest |
| B | +11 | +3.86% |
| **CCC** | +15 | **+1.53%** ← smallest |

- Absolute bp says CCC led (+15 vs +11).
- **Proportionally BB moved 4.6× more than CCC.**
- **CCC/BB ratio COMPRESSED 6.25× → 5.93× across exactly the two sessions that produced the entire move.**

**A quality-recognition leg expands the ratio. This one compressed it.** ⇒ **Leg B is BETA / level repricing, not credit recognition.** PROME's "BB-led, CCC-laggard, absolute-bp artifact" call is **independently CONFIRMED here** off my own FRED pull.

### Leg A — the quiet stretch, 7/15 → 7/22 (the fragment that IS thesis-supporting)

| | Δ bp |
|---|---|
| HY | **−3 (TIGHTENED)** |
| BB | **−5 (TIGHTENED)** |
| B | −5 (TIGHTENED) |
| **CCC** | **+12 (WIDENED)** |

**CCC widened 12bp while the index and the two higher tranches tightened.** Ratio 5.98× → 6.25×. **That is the quality-dispersion signature — and it fired while the headline number was moving the *other* way.**

### Net 7/15 → 7/24 — the two standard normalizations DISAGREE

| Metric | Reading | Verdict |
|---|---|---|
| CCC−BB gap | 807 → **828** (+21bp) | weakly bear ✅ |
| CCC/BB ratio | 5.98× → **5.93×** (flat/down) | not bear ❌ |
| Acute-move composition | BB-led proportionally, ratio compressed | not bear ❌ |

**The disagreement IS the finding.** A genuine credit-recognition leg registers on **both** normalizations. This one registers on one, fails the other, and fails the acute move outright. **⇒ NOT a credit-quality recognition leg.** Score: mixed-to-negative, no escalation.

> ⚠️ **Method note, worth keeping:** on 7/22→7/24 the absolute-bp lens and the proportional lens gave **opposite winners** off the same four numbers. Any "parallel widening" or "CCC-led" claim that does not say which normalization it used is unfalsifiable. Cf. `[[finding_number_carries_threshold_unit_source]]`, `[[finding_composition_mask_unmask_discriminator]]`.

---

## 3. X1 half A — wrapper-leads: NOT FIRING, now on a SECOND independent leg

7/2 close → 7/27 live intraday [dashboard 7/27 ~1:55 PM ET]:

| | 7/2 | 7/27 | Δ |
|---|---|---|---|
| **Managers** | | | |
| APO | $118.61 | $124.07 | **+4.6%** |
| ARES | $116.90 | $126.82 | **+8.5%** |
| **Wrappers** | | | |
| ARCC | $18.73 | $18.90 | +0.9% |
| FSK | $10.43 | $10.82 | +3.7% |
| OBDC | $10.82 | $10.93 | +1.0% |
| BIZD | $12.51 | $12.48 | **−0.2%** |

**Managers led the recovery by 1.2–9×.** Combined with the 7/4 adjudication (managers led the *selloff* down by 3–6×), the record is now:

> **Wrappers lag in BOTH directions.** They lagged the June down-leg and they are lagging the July up-leg.

That is not suppressed-recognition-waiting-to-break. **It is beta-insensitivity — the signature of a mark-to-model asset class whose equity does not reprice on either tape direction.** The 7/4 call was one observation and could have been a down-leg artifact; **this is the symmetric second observation, and it strengthens rather than re-opens the verdict.**

⚠️ **Consequence for the X1 test design itself:** if wrappers are structurally beta-insensitive, "wrapper basket LEADS managers" may be a **near-unfireable** condition outside a forced-deleveraging event — i.e. a possible *resolvability* defect, not a confidence question (`[[finding_resolvability_defect_is_status_not_confidence]]`). **Not re-specifying it today** — flagged for review after the 8/4-8/6 marks cluster, which is the un-maskable substance test the tape cannot mask either way.

---

## 4. Verdict

| X1 half | Test | State | Call |
|---|---|---|---|
| **A — wrapper-leads** | wrapper basket leads managers down | Managers led UP 4.6–8.5% vs wrappers +0.9–3.7%, BIZD −0.2% | **NOT FIRING** (2nd independent leg) |
| **B — HY >280 sustained** | >280, sustained | **279 [7/24]**, never exceeded the 6/29 280 print; sustain **0**; composition BB-led/beta | **NOT TAGGED** |

**⇒ X1 NOT MET. Unchanged from 7/4, now on fresh evidence from an opposite-signed tape leg. LIQUID credit-bear sizing gate stays CLOSED. No convergence score moves. Position unchanged.**

---

## 5. 🔴 The finding that DOES move — the duration channel is re-opening

| | Last STATUS mark | **Now** | Δ | My threshold |
|---|---|---|---|---|
| **10Y** | 4.49 [6/17] | **4.71 [7/23]** | **+22bp** | **>4.75** → duration vector 🟠(3)→🔴(4) |
| TLT | — | $83.68 [7/27] | — | — |
| VIX | 16.78 | 19.45 | +2.7 | — |

**4 basis points from my own pre-registered escalation line**, and it is the *only* threshold on my board within touching distance.

**LESSONS #15 is explicit about this exact configuration.** May 2026: substance validated, equity-put channel closed (regime-suppressed), duration channel open — the BROCK-domain equity put book ran **−84%** while the same thesis expressed through duration ran **+$600**. Today: substance firming, **credit-recognition channel adjudicated closed for the second time**, and duration +22bp into its trigger.

**This is a channel-selection observation, not a trade.** It says: *if* the private-credit thesis is to be expressed over the next leg, the transmission channel currently open is duration — not wrapper equity, not manager equity, not HY. **Vehicle construction is TERRY's; sizing is Will's.** BROCK's job was to say which channel is open, and it is not the one my narrative wants.

⚠️ Duration is **LIQUID/HENRY's metric** — cited `[FRED 7/23]`, not re-owned. The *threshold* (>4.75 on my duration-channel vector) is mine.

---

## 6. What would actually re-open X1

1. **HY >280 closing, sustained 5+ sessions, WITH the CCC/BB ratio EXPANDING through the move** (both normalizations agreeing) — the acute-move test that failed above.
2. **Wrappers leading on a fresh leg** in either direction — after two symmetric failures, this needs a forced-deleveraging or a mark event, not tape drift.
3. **The 8/4-8/6 marks cluster** (OCSL 8/5 · OBDC 8/5 AMC · FSK 8/6 · MFIC 8/6), with **ARCC 7/29 pre-open** as lone first-read — substance the tape cannot mask, and the real adjudication venue.

**Next dated checkpoint: ARCC Wed 7/29 pre-open.** Grading criteria pre-registered in STATUS §"ARCC Q2 prep."

---

*BROCK 2026-07-27. Supersedes nothing — extends `X1_WRAPPER_LEADS_ADJUDICATION_JUL04.md` with a second, opposite-signed test leg. HY OAS / tranche levels are LIQUID-owned and cited from FRED; the tranche discriminator, the X1 spec, and the 4.75 duration line are BROCK's.*
