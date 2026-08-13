---
signal_id: SIG-W-20260813-003
date: 2026-08-13
time_dispatched: 2026-08-13T15:5xZ
origin: Will-Telegram batch #9 2026-08-13T14:57Z items 1 + 4 of 9, COMBINED per Phase-1b (two sources, one fiscal object) — batch manifest BM-20260813-02. Item 1 = @KobeissiLetter (X); item 4 = FFTT LLC / Luke Gromen receipts chart + its commentary.
source: **PRIMARY** — US Treasury Monthly Treasury Statement, July FY2026 (record_date 2026-07-31), pulled by WALTER from `api.fiscaldata.treasury.gov` (`mts_table_1`, `mts_table_9`) 2026-08-13 ~15:4xZ. **CLAIMS** — Kobeissi Letter post (~1h before capture) + FFTT chart/commentary.
domain: MACRO_INFLATION
cluster: FED_FRAMEWORK
precedence: PRIORITY
action: [BOND, HENRY]
info: [LIQUID, RED, CARL]
entities: [MTS, US-budget-deficit, net-interest-outlays, Medicare, National-Defense, Treasury-receipts]
signal_type: correction
confidence: 0.95
verdict: CORRECTED-framing
consumer_lens: BOND's issuance/supply read; HENRY's term-premium and fiscal-dominance channel; CARL's MACRO_INFLATION row.
corrects: EXTERNAL: @KobeissiLetter post 2026-08-13 + FFTT/Gromen receipts commentary — no prior WALTER signal carried these figures
---

# 🟠 **The −$432B July deficit is EXACT and the Treasury confirms it. Two things built on top of it are wrong: interest has NOT passed Medicare, and the record is mostly a Saturday.**

## 1. The headline number is right — verified to the dollar

**July FY2026 deficit = $432,307,874,621 = −$432.3B.** The post said −$432B. **Exact.** No dispute, and I am leading with that because the corrections below only matter if the number itself is sound.

## 2. 🔴 But the load-bearing rhetorical claim is FALSE

> *"interest expense has officially surpassed both National Defense and Medicare … the US government now spends more on interest than it does to fund the entire US Military or to provide healthcare for seniors."*

**MTS Table 9, FY2026 fiscal-year-to-date through July:**

| Function | FYTD FY2026 | FYTD FY2025 | YoY |
|---|---:|---:|---:|
| **Medicare** | **$954.5B** | $823.4B | +15.9% |
| **Net Interest** | **$931.4B** | $840.8B | +10.8% |
| **National Defense** | **$803.7B** | $758.0B | +6.0% |

⇒ **Net interest HAS passed National Defense — by $127.7B. It has NOT passed Medicare: Medicare is $23.1B HIGHER, and Medicare is growing FASTER (+15.9% vs +10.8%).** The claim is half right, stated as wholly right, and the half that fails is the one carrying the rhetorical weight.

**Two further figure mismatches:** the post's **$118B** monthly interest is **$104.2B** on the MTS *net interest* line, and its **$1.17T FY2026 interest** is **$931.4B** FYTD. Both gaps are consistent with the post using **gross** interest where the MTS reports **net**. ⚠️ **Gross and net are different objects — do not carry one under the other's label.** *(I did not pull the gross series, so I am naming the likely reconciliation, not asserting it.)*

## 3. 🔑 The record is substantially a CALENDAR ARTIFACT — and the fiscal year is the tell

**2026-08-01 fell on a SATURDAY. 2025-08-01 fell on a Friday.** When the 1st is a weekend, August benefit payments accelerate into July 31 — a well-known MTS distortion.

The decomposition says exactly that:

| | July FY2026 | July FY2025 | Δ |
|---|---:|---:|---:|
| Receipts | $334.0B | $338.5B | **−$4.5B** |
| Outlays | $766.3B | $629.6B | **+$136.7B** |
| Deficit | **$432.3B** | $291.1B | **+$141.2B** |

⇒ **97% of the YoY swing is OUTLAYS; 3% is receipts.** And within outlays, **CMS alone (Medicare + Medicaid) went $229.6B → $309.2B, +$79.6B in one month** — more than half the entire swing, on precisely the line a payment-date shift moves.

**🔴 THE DISCRIMINATOR: fiscal-year-to-date deficit is $1,798.8B vs $1,775.4B — up only +1.3% YoY.** A month at +48.5% inside a year at +1.3% is a timing signature, not a deterioration signature. **The month is a record; the fiscal year is nearly flat.**

## 4. Item 4 folded in — the receipts claim is TRUE, and much smaller than advertised

The FFTT chart and its commentary assert *"US tax receipts are falling."* **The MTS confirms it: July receipts $334.0B vs $338.5B, −1.3% YoY.** Independently corroborated, and worth crediting.

**But it is 3% of this month's swing**, so it cannot carry the doom-loop framing the commentary builds on it (*higher rates → weaker economy → lower receipts → higher interest → larger deficits → higher rates*). ⚠️ **Two further problems with that leg:** the commentary attributes falling receipts to *"the Iran war,"* an unsupported causal claim; and **the chart's x-axis cannot be dated from the screenshot** — its last legible label reads `25-Feb` with the circled point at the right edge, so I cannot establish what period the red circle marks. **Do not quote a value off that chart.**

## 5. What genuinely survives all of this

**Net interest grew +10.8% YoY to $931.4B FYTD and has decisively passed National Defense.** That is real, primary, and directionally what the fiscal-dominance thesis expects. **The trend does not need the exaggeration.**

## 6. 🚦 TERRY gate — CHECKED, NOT FIRED

**T-1** no registered TERRY instrument keys to a deficit or interest-expense figure (`SETUPS.tsv` / `PAPER_BOOK.tsv` / `SIGNALS.tsv` checked). **T-2** no number on a TERRY surface is corrected here — the fiscal figures appear on none of them. **T-3** markets open. ⇒ **no line, including `info:`.** *(Fiscal supply is "relevant to" duration, and §3.5.5 says relevance is exactly what does not qualify.)*

## 7. ASK

1. **BOND — does a +1.3% FYTD deficit against a +48.5% single month change anything in your issuance/supply read, or is the calendar shift already in how you read MTS months?** The August MTS (released ~9/10) should give back most of the July spike; **if it does NOT, that is the real signal and it is a September object.**
2. **HENRY — net interest $931.4B FYTD, +10.8%, now $127.7B above National Defense but $23.1B below Medicare.** Does the Medicare crossover matter to your fiscal-dominance framing, or is Defense the threshold you actually track?
3. **CARL — receipts −1.3% YoY is a real datum for `MACRO_INFLATION`;** flagged because it is true and because the framing attached to it is not.

## 8. What I did NOT establish

- **I did not pull GROSS interest**, so the $118B-vs-$104.2B and $1.17T-vs-$931.4B reconciliations are named as *likely* gross-vs-net, not proven.
- **I did not quantify the Saturday shift.** That Aug 1 2026 was a Saturday is verified; that it explains most of the $136.7B is an inference from the CMS line's size and timing, **not a measured decomposition.** The clean test is the August MTS.
- **"Largest July deficit in history"** — I verified July 2026 > July 2025 and confirmed the level; **I did not check every prior July.**
- **The FFTT chart is undateable from the artifact** and no value is taken from it.

---

*Routed by WALTER · Will-directed image batch · every figure re-pulled from Treasury's own API before dispatch, not from the posts. **BOND and HENRY own the fiscal reads; WALTER establishes only what the MTS says.***
