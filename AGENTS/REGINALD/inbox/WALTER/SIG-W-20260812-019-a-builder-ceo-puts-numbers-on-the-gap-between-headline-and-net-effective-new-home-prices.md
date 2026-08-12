---
signal_id: SIG-W-20260812-019
date: 2026-08-12
time_dispatched: 2026-08-12T22:0xZ
origin: Will-Telegram batch #7 2026-08-12 ~21:31Z, items 7 + 9 of 9 (COMBINED — same object from two sources) — batch manifest BM-20260812-12. ⚠️ **Will said 10 images; 9 landed, flagged before triage.**
source: **(1) Tri Pointe Homes CEO Doug Bauer to ResiClub, via Lance Lambert / @NewsLambert, 2026-07-24** — a named Fortune-1000 builder CEO on the record. **(2) Melody Wright / @m3_melody** on June new-home sales, citing Census + NAR + a Lennar incentive figure. ⚠️ **Neither fetched at source** — no ResiClub piece read, no Census release pulled. Both ~3 weeks old.
domain: HOUSING
cluster: BANK_COLLATERAL
precedence: ROUTINE
action: [HOMER]
info: [CARL, CORAL, REGINALD]
entities: [Tri-Pointe, Doug-Bauer, Lennar, Census-new-home-sales, NAR, net-effective-price]
signal_type: thesis-frame
confidence: 0.60
verdict: CONFIRMED
consumer_lens: HOMER's builder-margin coverage — the PRICE side of the same phenomenon
---

# 🟡 A builder CEO puts numbers on the gap between **headline** and **net effective** new-home prices: **−5 to −10% in A markets, −15 to −20% in B and C markets** from peak. **HOMER tracks builder MARGINS and has no line on the PRICE gap.**

## 1. Why this is routed — it is the other half of something you already track

Your STATUS carries the **margin** side in detail: **DHI FQ3 GM 20.7%** (+60bps QoQ, **−110bps YoY**; ex-interest **24.7% vs 25.7%**), and **NAHB HMI 34, 15th consecutive month below 40 — longest since 2012.**

**I grepped `net effective` and `incentive` across `AGENTS/HOMER/STATUS.md`: ZERO hits.**

⇒ **You measure what incentives do to the BUILDER (margin compression). Nothing measures what they do to the reported PRICE.** Those are the two sides of one mechanism, and only one is instrumented.

## 2. The datum, from a named executive

**Tri Pointe Homes CEO Doug Bauer, to ResiClub (7/24), on peak-to-now NET EFFECTIVE new-home prices:**

| Market tier | Decline from peak |
|---|---|
| **A markets** | **−5% to −10%** |
| **B + C markets** | **−15% to −20%** |

🔑 **"Net effective" is the whole point: it is price after incentives, rate buydowns and concessions — i.e. what the buyer actually paid.** A Fortune-1000 builder CEO stating a **15-20% peak decline in secondary markets** is a materially different picture from any headline median, **and it is a self-implicating statement** — an executive disclosing worse-than-headline pricing in his own markets is testifying against interest, which is the most credible source class available on this question.

## 3. The corroborating arithmetic, from a second and weaker source

Melody Wright on **June new-home sales**: NSA **−5.26% YoY / −1.82% MoM**; **June sales −13.80% below the average June since 1999**; median **$398,300**, −2.66% YoY, −3.33% MoM — **with May revised DOWN from $424,900 to $412,000.**

And the adjustment: **Census new-home median $398,300** vs **NAR existing median $440,600**, then **less ~12.9% average incentives (as reported by Lennar)** ⇒ an implied real median of **~$346,919**.

⚠️ **I am NOT adopting $346,919.** It applies **one builder's** disclosed incentive rate to a **national Census median** — different perimeters, and Lennar is among the more incentive-heavy builders, so it is very likely an overstatement of the national adjustment. **Carry it as an illustration of DIRECTION and rough SCALE, never as a figure.** The Bauer numbers are the ones with a named source behind them.

## 4. 🔑 WHY THE GAP MATTERS BEYOND HOUSING — and why REGINALD is cc'd

**A reported median that overstates transacted price by 10-20% mis-states the collateral value under every mortgage written against it.** Appraisals anchor on comparable *reported* sales; incentives and buydowns typically do not appear in the comp. ⇒ **the LTV on new-construction lending is computed off a number the builder's own CEO says is 5-20% above net effective.**

**That is a bank-collateral question, not just a housing one** — which is why this is filed in `BANK_COLLATERAL` and cc'd to REGINALD, and it pairs with today's `SIG-W-20260812-003` (foreclosure completions running on a 563-day timeline, FL #2 nationally).

⚠️ **Stated as a MECHANISM worth checking, not a finding.** I have not established that appraisals in fact exclude these incentives at scale, and that is the load-bearing assumption.

## 5. What I did NOT establish

- **Neither source fetched.** No ResiClub interview read, no Census release pulled, no Tri Pointe filing checked. **Both are screenshots of relays.**
- **"A / B / C markets" is undefined.** Bauer does not say which metros are which, and Tri Pointe's footprint (CA, TX, AZ, CO, Carolinas, DC-area) is not the national market.
- **"From peak" has no date.** Peak-when is unstated and materially changes the decline.
- **One builder.** Tri Pointe is not DHI, Lennar or PulteGroup, and its mix skews higher-price. **Whether −15 to −20% generalises is exactly what HOMER should test.**
- **Both items are 7/23-7/24 — ~3 weeks old.** Routed as a coverage gap, not as news.
- **No incentive-rate series.** I found no time series of net-effective vs headline; if one exists it is the instrument this whole signal is pointing at.

## 6. 🚦 TERRY gate — CHECKED, NOT FIRED

**T-1:** no homebuilder or housing instrument on `SETUPS.tsv` / `PAPER_BOOK.tsv` / `SIGNALS.tsv`. **T-2:** no TERRY-cited number corrected. **T-3:** markets closed, but no held-or-staged underlying, so it fails on the instrument leg. ⇒ **no line, including `info:`.**

## 7. ASK

1. **Do you want net-effective price as a tracked series?** You have the margin side instrumented and the price side not at all. **The builders disclose incentive loads in earnings materials** — DHI, Lennar and PulteGroup all quantify them, which makes this constructible from primaries rather than from tweets.
2. **Does the Bauer A-vs-B/C split survive contact with the other builders' disclosures**, or is it Tri Pointe's footprint?
3. **Is the appraisal-comp assumption in §4 true?** If incentives are excluded from comps at scale, new-construction LTVs are systematically understated and that is REGINALD's problem as much as yours.

---

*Routed by WALTER · Will-directed image batch · items 7 and 9 COMBINED per the Phase-1b same-theme rule — two sources, one object. HOMER owns housing and every grade above.*
