# PANAMA CANAL — MONTHLY CAPACITY SERIES (ACP Monthly Canal Operations Summary)

**Instrument:** ACP *Monthly Canal Operations Summary*, published as a numbered Advisory to Shipping. **Every figure below is transcribed as printed** from the advisory PDF named in its row — no derived values except the explicitly-labelled self-check columns.

**Built:** 2026-08-21 by the AEOLUS water worker. **Coverage requested:** 2023-10 → 2026-07 (34 months). **Coverage obtained: 33 of 34.** See §Gaps.

> ⚠️ **ALL VALUES ARE PROPOSALS. AEOLUS ADJUDICATES.** Nothing here scores a channel, fires a trigger or resolves a prediction.

---

## 1. HOW THIS WAS RETRIEVED — and a correction to `SOURCES.md`

`SOURCES.md` records `https://pancanal.com/en/advisories-to-shipping/` as **known-bad** (JS-rendered, silently truncates at `A-46-2024`). **That remains true and I did not use it.**

**A different path on the same host returns the COMPLETE archive, server-rendered, at HTTP 200:**

```bash
curl -sLk -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" \
  "https://pancanal.com/en/maritime-services/advisory-to-shipping/"
```

**762,407 bytes · 1,005 PDF anchors · advisories from `a-01-2002` to the current 2026 set.** Each anchor carries both the advisory number and the data month in its link text, so month → URL needs no guessing.

🔑 **VALIDATION BEFORE USE (this is why I trust it):** the index reproduced **all 7 of the independently-verified URLs** AEOLUS supplied in the task brief — `ADV21-2024`(Jun-24), `ADV38-2024`(Sep-24), `ADV01-2025`(Dec-24), `ADV-04-2025`(Jan-25), `ADV-30-2025`(Sep-25), `ADV-01-2026`(Dec-25), `ADV-14-2026`(Apr-26) — **byte-identical, 7/7, including the inconsistent `ADV21` vs `ADV-04` naming and the trailing-dash quirk.** An index that reproduces every known-good URL exactly is not the stale fragment the known-bad path returns.

⚠️ **This does NOT retire the known-bad entry** — it is a *different URL*, and the old one is still stale. **Proposed `SOURCES.md` amendment: add the working path beside the known-bad one, with the 7/7 validation recorded.** AEOLUS to ratify.

**Extraction:** `curl -sLk` + browser UA → `pdfminer.six`. Parsed **twice by independent methods** — (a) coordinate/band reconstruction from `LTTextLine` (x,y), (b) text-order block parsing — and **reconciled row by row. The two agreed on every reported value in all 33 months** (one text-layer artifact, noted in §5).

---

## 2. THE SERIES — oceangoing transits + Canal Waters Time

⚠️ **`Arr/day` is ARRIVALS, not transits.** It sits immediately above transits in the same block and is the single easiest misread in this document. **AEOLUS's registered band is on the `Tr/day` column.**

| Month | Adv. | Adv. date | **Tr/day** | Tr hi | Tr lo | Total transits | ✅ total÷days | Arr/day | Arr hi | Arr lo | CWT h | ITT h |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Oct-2023** | A-49-2023 | November 8, 2023 | **32.35** | 37 | 30 | 1003 | ✅ 32.35 | 31.55 | 43 | 21 | 53.72 | 12.27 |
| **Nov-2023** | A-53-2023 | December 7, 2023 | **26.1** | 32 | 22 | 783 | ✅ 26.1 | 25.33 | 34 | 15 | 40.71 | 10.37 |
| **Dec-2023** | A-02-2024 | January 10, 2024 | **24.13** | 30 | 20 | 748 | ✅ 24.13 | 23.7 | 33 | 16 | 44.1 | 9.74 |
| **Jan-2024** | A-04-2024 | February 9, 2024 | **22.6** | 26 | 19 | 702 | ✅ 22.65 | 22.2 | 31 | 11 | 32.1 | 9.4 |
| **Feb-2024** | A-07-2024 | March 8, 2024 | **22.8** | 25 | 19 | 662 | ✅ 22.83 | 23.7 | 31 | 17 | 20.9 | 9.8 |
| **Apr-2024** | A-14-2024 | May 10, 2024 | **26.3** | 29 | 23 | 789 | ✅ 26.3 | 26.7 | 39 | 18 | 20.2 | 9.4 |
| **May-2024** | A-18-2024 | June 10, 2024 | **26** | 32 | 20 | 805 | ✅ 25.97 | 26 | 37 | 15 | 22.9 | 10.7 |
| **Jun-2024** | A-21-2024 | July 10, 2024 | **29** | 33 | 22 | 871 | ✅ 29.03 | 29.4 | 39 | 17 | 19.1 | 9.8 |
| **Jul-2024** | A-27-2024 | August 9, 2024 | **29.6** | 34 | 20 | 918 | ✅ 29.61 | 29.9 | 50 | 18 | 18.3 | 10.1 |
| **Aug-2024** | A-33-2024 | September 11, 2024 | **30.9** | 36 | 24 | 957 | ✅ 30.87 | 31.5 | 46 | 23 | 18.3 | 10 |
| **Sep-2024** | A-38-2024 | October 10, 2024 | **31.9** | 36 | 26 | 958 | ✅ 31.93 | 32.4 | 44 | 23 | 20.2 | 10.8 |
| **Oct-2024** | A-41-2024 | November 14, 2024 | **31.4** | 37 | 26 | 975 | ✅ 31.45 | 32.2 | 39 | 21 | 20.1 | 10.8 |
| **Nov-2024** | A-45-2024 | December 10, 2024 | **33.3** | 37 | 24 | 999 | ✅ 33.3 | 33.1 | 41 | 23 | 21.1 | 10.8 |
| **Dec-2024** | A-01-2025 | January 10, 2025 | **34.2** | 37 | 26 | 1059 | ✅ 34.16 | 35 | 48 | 23 | 21.7 | 11.2 |
| **Jan-2025** | A-04-2025 | February 11, 2025 | **32.6** | 36 | 26 | 1011 | ✅ 32.61 | 33.3 | 45 | 19 | 20.2 | 10.1 |
| **Feb-2025** | A-05-2025 | March 10, 2025 | **34.8** | 38 | 31 | 975 | ✅ 34.82 | 35.1 | 50 | 25 | 20.8 | 10.2 |
| **Mar-2025** | A-08-2025 | April 10, 2025 | **33.7** | 37 | 29 | 1045 | ✅ 33.71 | 33.9 | 46 | 21 | 19.3 | 10.3 |
| **Apr-2025** | A-11-2025 | May 08, 2025 | **34** | 38 | 28 | 1021 | ✅ 34.03 | 34.8 | 49 | 22 | 20.7 | 10.2 |
| **May-2025** | A-18-2025 | June 10, 2025 | **31.4** | 40 | 20 | 973 | ✅ 31.39 | 31.9 | 42 | 18 | 19.1 | 10.3 |
| **Jun-2025** | A-21-2025 | July 10, 2025 | **31.4** | 38 | 24 | 941 | ✅ 31.37 | 31.6 | 44 | 18 | 18.9 | 10 |
| **Jul-2025** | A-24-2025 | August 8, 2025 | **32.6** | 38 | 25 | 1012 | ✅ 32.65 | 33.1 | 48 | 19 | 20.8 | 10.3 |
| **Aug-2025** | A-26-2025 | September 09, 2025 | **32.5** | 37 | 26 | 1009 | ✅ 32.55 | 32.2 | 43 | 24 | 21.6 | 10.7 |
| **Sep-2025** | A-30-2025 | October 10, 2025 | **33.1** | 39 | 26 | 994 | ✅ 33.13 | 34.2 | 49 | 19 | 21.4 | 11.3 |
| **Oct-2025** | A-35-2025 | November 10, 2025 | **33.2** | 38 | 28 | 1028 | ✅ 33.16 | 33.6 | 43 | 21 | 20.2 | 10.5 |
| **Nov-2025** | A-36-2025 | December 10, 2025 | **33.5** | 38 | 22 | 1006 | ✅ 33.53 | 33.9 | 45 | 23 | 18.4 | 9.7 |
| **Dec-2025** | A-01-2026 | January 08, 2026 | **34.68** | 40 | 28 | 1075 | ✅ 34.68 | 34.6 | 45 | 21 | 20.81 | 10.3 |
| **Jan-2026** | A-03-2026 | February 10, 2026 | **33.84** | 38 | 23 | 1049 | ✅ 33.84 | 34.2 | 48 | 23 | 20.3 | 10.02 |
| **Feb-2026** | A-04-2026 | March 10, 2026 | **35** | 38 | 32 | 981 | ✅ 35.04 | 36.7 | 46 | 26 | 19.1 | 10.2 |
| **Mar-2026** | A-09-2026 | April 10, 2026 | **37.03** | 41 | 34 | 1148 | ✅ 37.03 | 37.2 | 56 | 23 | 21.39 | 10.67 |
| **Apr-2026** | A-14-2026 | May 8, 2026 | **38.7** | 42 | 31 | 1161 | ✅ 38.7 | 40.5 | 54 | 29 | 32.33 | 11.84 |
| **May-2026** | A-19-2026 | June 9, 2026 | **37.06** | 41 | 32 | 1149 | ✅ 37.06 | 35.4 | 47 | 26 | 31.2 | 11.06 |
| **Jun-2026** | A-23-2026 | July 10, 2026 | **32.5** | 39 | 25 | 975 | ✅ 32.5 | 33.8 | 42 | 27 | 23.8 | 11.01 |
| **Jul-2026** | A-26-2026 | August 10, 2026 | **34.03** | 37 | 25 | 1055 | ✅ 34.03 | 35.4 | 48 | 25 | 25.38 | 10.87 |

**Self-check result: `monthly total ÷ days-in-month` reproduces the printed daily average in 33 of 33 months** (tolerance ±0.06, which absorbs ACP's 1-vs-2 decimal printing). **No month failed.**

---

## 3. TRANSITS BY BEAM CLASS (daily average, as printed)

| Month | <91′ | 91–107′ | Neopanamax | **Class total** | Traffic-block Tr/day | Δ | Month totals <91 / 91-107 / Neo |
|---|---:|---:|---:|---:|---:|:--:|---|
| **Oct-2023** | 5.97 | 16.65 | 9.74 | 32.35 | 32.35 | — | 185 / 516 / 302 |
| **Nov-2023** | 4.67 | 14.07 | 7.37 | 26.1 | 26.1 | — | 140 / 422 / 221 |
| **Dec-2023** | 4.77 | 12.65 | 6.71 | 24.13 | 24.13 | — | 148 / 392 / 208 |
| **Jan-2024** | 4.55 | 12 | 6.1 | 22.65 | 22.6 | **+0.05** | 141 / 372 / 189 |
| **Feb-2024** | 4.6 | 11.3 | 6.9 | 22.8 | 22.8 | — | 132 / 329 / 201 |
| **Apr-2024** | 5 | 13.9 | 7.4 | 26.3 | 26.3 | — | 149 / 418 / 222 |
| **May-2024** | 4.4 | 14.1 | 7.5 | 26 | 26 | — | 135 / 436 / 234 |
| **Jun-2024** | 4.8 | 16.1 | 8.2 | 29.1 | 29 | **+0.1** | 143 / 483 / 245 |
| **Jul-2024** | 5 | 16.4 | 8.3 | 29.7 | 29.6 | **+0.1** | 154 / 507 / 257 |
| **Aug-2024** | 4.9 | 16.9 | 9 | 30.9 | 30.9 | — | 153 / 524 / 280 |
| **Sep-2024** | 5.6 | 17.3 | 9 | 31.9 | 31.9 | — | 167 / 520 / 271 |
| **Oct-2024** | 5.2 | 17.3 | 9 | 31.5 | 31.4 | **+0.1** | 160 / 537 / 278 |
| **Nov-2024** | 5.9 | 18.4 | 9 | 33.3 | 33.3 | — | 178 / 551 / 270 |
| **Dec-2024** | 6.4 | 18.8 | 9 | 34.2 | 34.2 | — | 198 / 582 / 279 |
| **Jan-2025** | 5.8 | 17.6 | 9.3 | 32.6 | 32.6 | — | 179 / 545 / 287 |
| **Feb-2025** | 6.7 | 19.6 | 8.5 | 34.8 | 34.8 | — | 188 / 550 / 237 |
| **Mar-2025** | 6.9 | 18.2 | 8.6 | 33.7 | 33.7 | — | 215 / 563 / 267 |
| **Apr-2025** | 6.9 | 17.5 | 9.7 | 34 | 34 | — | 206 / 525 / 290 |
| **May-2025** | 5.2 | 17.5 | 8.8 | 31.4 | 31.4 | — | 160 / 541 / 273 |
| **Jun-2025** | 5.4 | 17.6 | 8.4 | 31.4 | 31.4 | — | 161 / 528 / 252 |
| **Jul-2025** | 4.6 | 18.4 | 9.6 | 32.6 | 32.6 | — | 144 / 569 / 299 |
| **Aug-2025** | 4.8 | 17.6 | 10.1 | 32.5 | 32.5 | — | 150 / 546 / 313 |
| **Sep-2025** | 5.1 | 18.2 | 9.9 | 33.1 | 33.1 | — | 152 / 545 / 297 |
| **Oct-2025** | 5.4 | 17.9 | 9.9 | 33.2 | 33.2 | — | 166 / 556 / 306 |
| **Nov-2025** | 5.4 | 19 | 9.1 | 33.5 | 33.5 | — | 162 / 571 / 273 |
| **Dec-2025** | 6.45 | 18.52 | 9.71 | 34.68 | 34.68 | — | 200 / 574 / 301 |
| **Jan-2026** | 6.03 | 17.97 | 9.84 | 33.84 | 33.84 | — | 187 / 557 / 305 |
| **Feb-2026** | 6.3 | 19.2 | 9.6 | 35 | 35 | — | 175 / 538 / 268 |
| **Mar-2026** | 6.65 | 20.65 | 9.74 | 37.03 | 37.03 | — | 206 / 640 / 302 |
| **Apr-2026** | 6.37 | 22.07 | 10.27 | 38.7 | 38.7 | — | 191 / 662 / 308 |
| **May-2026** | 5.48 | 21.23 | 10.35 | 37.06 | 37.06 | — | 170 / 658 / 321 |
| **Jun-2026** | 5.27 | 17.4 | 9.83 | 32.5 | 32.5 | — | 158 / 522 / 295 |
| **Jul-2026** | 5.65 | 18.39 | 10 | 34.03 | 34.03 | — | 175 / 570 / 310 |

⚠️ **The two printed daily averages disagree in 4 months** (Jan/Jun/Jul/Oct-2024, all +0.05 to +0.1). Cause: in the 1-decimal era the by-class total is the **sum of the rounded class figures** while the traffic block rounds the true mean. **Both are printed values; neither is a transcription error.** *(Jun-2024 is the month AEOLUS carries as **29.1** — that is the **by-class** figure; the **traffic block prints 29.0**, and 871÷30 = 29.03. AEOLUS should decide which column the band reads; I did not.)*

---

## 4. BOOKING SLOTS — all four lines, Available / Used / Percentage

⚠️ **`Available` for the three vessel classes carries ACP's asterisk: *“Does not include additional auctioned booking slots.”* That is why class Used/Available legitimately exceeds 100%.** The **Auctioned** line carries no asterisk.

| Month | Neopanamax A/U/% | Supers A/U/% | Regular A/U/% | **Auctioned A/U/%** | calc U÷A |
|---|---|---|---|---|---:|
| **Oct-2023** | 217/212/97.7 | 319/298/93.42 | 130/118/90.77 | **146/139/95.21** | 95.21 |
| **Nov-2023** | 194/186/95.88 | 323/273/84.52 | 120/107/89.17 | **154/150/97.4** | 97.4 |
| **Dec-2023** | 155/152/98.06 | 341/267/78.3 | 93/83/89.25 | **196/196/100** | 100 |
| **Jan-2024** | 170/153/90 | 326/247/75.77 | 109/102/93.58 | **180/162/90** | 90 |
| **Feb-2024** | 174/167/95.98 | 319/242/75.86 | 116/101/87.07 | **161/143/88.82** | 88.82 |
| **Apr-2024** | 180/171/95 | 360/276/76.67 | 120/104/86.67 | **252/205/81.35** | 81.35 |
| **May-2024** | 186/180/96.77 | 436/329/75.46 | 131/100/76.34 | **277/192/69.31** | 69.31 |
| **Jun-2024** | 210/195/92.86 | 480/362/75.42 | 150/111/74 | **315/175/55.56** | 55.56 |
| **Jul-2024** | 238/215/90.34 | 527/375/71.16 | 155/118/76.13 | **354/171/48.31** | 48.31 |
| **Aug-2024** | 274/230/83.94 | 562/393/69.93 | 151/117/77.48 | **353/170/48.16** | 48.16 |
| **Sep-2024** | 270/218/80.74 | 570/418/73.34 | 150/127/84.67 | **283/174/61.49** | 61.48 |
| **Oct-2024** | 279/222/79.57 | 571/431/75.48 | 149/123/82.55 | **282/166/58.87** | 58.87 |
| **Nov-2024** | 270/220/81.48 | 570/463/81.23 | 149/126/84.56 | **257/167/64.98** | 64.98 |
| **Dec-2024** | 279/235/84.23 | 577/480/83.19 | 151/122/80.79 | **309/175/56.63** | 56.63 |
| **Jan-2025** | 275/136/49.45 | 589/461/78.27 | 155/125/80.65 | **467/327/70.02** | 70.02 |
| **Feb-2025** | 109/83/76.15 | 449/355/79.06 | 106/91/85.85 | **407/357/87.71** | 87.71 |
| **Mar-2025** | 115/117/101.74 | 495/482/97.37 | 103/132/128.16 | **401/384/95.76** | 95.76 |
| **Apr-2025** | 110/129/117.27 | 472/438/92.8 | 94/114/121.28 | **396/302/76.26** | 76.26 |
| **May-2025** | 114/128/112.28 | 503/455/90.46 | 126/114/90.48 | **370/242/65.41** | 65.41 |
| **Jun-2025** | 120/116/96.67 | 472/437/92.58 | 112/112/100 | **379/239/63.06** | 63.06 |
| **Jul-2025** | 110/133/120.91 | 497/491/98.79 | 115/101/87.83 | **357/357/100** | 100 |
| **Aug-2025** | 125/158/126.4 | 491/467/95.11 | 108/107/99.07 | **395/382/96.18** | 96.71 🔴 |
| **Sep-2025** | 113/136/120.35 | 496/468/94.35 | 115/104/90.43 | **354/348/95.34** | 98.31 🔴 |
| **Oct-2025** | 124/152/122.58 | 487/461/94.66 | 127/122/96.06 | **378/367/97.09** | 97.09 |
| **Nov-2025** | 118/133/112.71 | 514/473/92.02 | 119/118/99.16 | **372/341/91.66** | 91.67 |
| **Dec-2025** | 121/147/121.49 | 504/497/98.61 | 115/135/117.39 | **277/366/132.13** | 132.13 |
| **Jan-2026** | 148/173/116.89 | 503/475/94.43 | 115/129/112.17 | **350/246/70.29** | 70.29 |
| **Feb-2026** | 138/161/116.67 | 457/437/95.62 | 105/112/106.67 | **249/216/86.75** | 86.75 |
| **Mar-2026** | 153/174/113.73 | 467/505/108.14 | 120/137/114.17 | **377/286/75.86** | 75.86 |
| **Apr-2026** | 177/187/105.65 | 481/534/111.02 | 117/134/114.53 | **317/273/86.12** | 86.12 |
| **May-2026** | 173/197/113.87 | 479/502/104.8 | 114/119/104.38 | **361/283/78.39** | 78.39 |
| **Jun-2026** | 186/197/105.91 | 424/413/97.41 | 106/102/96.23 | **290/230/79.31** | 79.31 |
| **Jul-2026** | 163/183/112.27 | 506/463/91.5 | 137/120/87.59 | **306/247/80.72** | 80.72 |
---

## 5. 🔴 THE HIGHEST-VALUE FINDING — DRAFT AND GATUN ELEVATION **DO** APPEAR

AEOLUS checked the Sep-2025 and Apr-2026 issues and found no tonnage, draft or Gatun elevation. **That conclusion is correct for those two issues and wrong for the corpus.** All three appear — but **never in the statistics table**. They appear in the **news article ACP appends after the maintenance schedule**, which is present in some issues and absent in others.

🔑 **This is why the negative finding held for two issues and failed across 34: the statistics table is fixed-schema and genuinely contains none of the three. The appendix is discretionary prose. A schema check of the table is not a check of the document.**

### 5a. MAXIMUM AUTHORISED DRAFT — Neopanamax locks, from ACP's own text

| Effective | Max draft | Direction | Source issue | Verbatim |
|---|---:|:--:|---|---|
| (in force Nov-2023) | **44.0 ft** | trough | A-53-2023 (Nov-2023) | *“vessels transiting the Neopanamax locks are allowed maximum drafts of up to 44 feet, while vessels transiting the Panamax locks have had no draft restrictions”* |
| (still in force Jan-2024) | **44.0 ft** | flat | A-04-2024 (Jan-2024) | *“drafts of up to 44 ft”* |
| 2024-06-26 | **47.0 ft** | ↑ | A-21-2024 (Jun-2024) | *“the maximum authorized draft was raised today from 46 to 47 feet (14.33 meters)”* |
| 2024-07-11 | **48.0 ft** | ↑ | A-21-2024 / A-27-2024 | *“will increase to 48 feet … on July 11”* |
| 2024-08 (immediate) | **49.0 ft** | ↑ | A-27-2024 (Jul-2024) | *“effective immediately, the maximum authorized draft … will be 49.0 feet (14.94 m), based on the present and projected level of Gatun Lake”* |
| 2024-08-15 | **50.0 ft** | ↑ **recovered** | A-33-2024 (Aug-2024) | *“the maximum authorized draft … is 50 feet (15.24 meters)”* |
| 2026-08-26 | **48.0 ft** | ↓ | A-26-2026 (Jul-2026) | *“effective August 26, 2026, the maximum authorized draft … will be reduced to 48 feet (14.63 meters)”* |
| 2026-09-03 | **47.5 ft** | ↓ | A-26-2026 (Jul-2026) | *“a further adjustment will take effect on September 3, lowering the maximum draft to 47.5 feet (14.48 meters)”* |

🔑 **A-26-2026 states these are *“the fourth and fifth draft adjustments announced by the Panama Canal Authority”* and that reductions have been *“in place since December 2025 as part of preparations for the 2026 dry season.”* That is ACP's own confirmation of a five-step draft reduction — consistent with the sequence already in `SERIES.tsv` (50 → 49.5 → 49.0 → 48.5 → 48.0 → 47.5).**

⚠️ **And the load-bearing sentence, verbatim:** *“**The draft adjustment will not affect the number of daily vessel transits.** Instead, it reflects water conservation and resource management.”* — **ACP is explicitly holding constant the exact variable AEOLUS's registered band measures.** The transit column cannot see this restriction by construction. *(Reported, not graded.)*

### 5b. 🔴 GATUN LAKE ELEVATION — ONE printed figure exists in the corpus

**A-27-2024 (July-2024 issue, advisory dated August 9, 2024) prints an actual lake elevation:**

> *“The rainy season is gradually bringing the reservoirs to its optimum levels: **Gatun Lake today is at 85.02 feet (25.91 m)**, while **Alhajuela Lake is at 217.24 feet (66.21 m)**.”*

**This is the only numeric Gatun elevation in all 33 readable issues.** It is a single spot reading (“today” = on/about 2024-08-09), **not a series** — but it is a **primary-sourced Gatun elevation from ACP itself**, and it sits inside the recovery, not the trough.

🔑 **Why it is worth more than one datapoint:** it **anchors the unit and datum** for the Gatun instrument `SOURCES.md` lists as UNRESOLVED. **85.02 ft** falls squarely inside the 82–87 ft PLD operating range `SOURCES.md` carries as an unverified reference point — **so that carried range is now corroborated at the issuing agency**, and any future lake-level scrape can be sanity-checked against a known-good ACP figure.

⚠️ **What it is NOT:** a monthly series, a current read, or a substitute for the live instrument. **No secondary was consulted and none should be.** The 2026 lake state remains **uninstrumented** — A-26-2026 invokes *“current water levels … in Gatun Lake”* as the basis for cutting draft and **prints no figure**.

**Lead for whoever closes the gap (unverified by me — reported, not chased):** four issues (Oct/Nov/Dec-2023, Apr-2024) close with a link list that includes *“**Daily average level of Gatun Reservoir for the last 12 months**”* and *“Daily average level of Alhajuela reservoir for the last 12 months.”* **I extracted the PDF link annotations: those two bullets are NOT hyperlinked** — only the vessel-queue dashboard is, at `https://apps.pancanal.com/t/TI/views/DashboardColadeEspera/DashboardCola-EN`. **That confirms the `apps.pancanal.com/t/TI/views/<Dashboard>/<View>` Tableau pattern `SOURCES.md` already records for `GatunH2OIndicators` — same host, same shape, one of them publicly linked.**

### 5c. TONNAGE — absent as a monthly figure, present twice as a fiscal aggregate

**There is no tonnage row in the statistics table in any of the 33 issues.** This confirms and extends AEOLUS's earlier negative finding from 5 issues to 33.

Tonnage appears **only** in appended prose, and **never as a monthly series**:

| Issue | Figure | Period | Differenceable into a monthly series? |
|---|---|---|---|
| A-07-2024 (Feb-2024) | 2,534 transits · **108 million tons** | Oct–Dec 2023 (quarter) | ❌ |
| A-14-2026 (Apr-2026) | 6,288 transits · **254 million PC/UMS tons**, ~5% above 243 M prior-year | H1 FY2026 (Oct-25–Mar-26) | ❌ |
| A-04-2026 (Feb-2026) | **25.1 million metric tons** grain | FY2025 (commodity subset) | ❌ |
| A-45-2024 (Nov-2024) | *“a reduction in total transits and tonnage”* | FY2024, qualitative | ❌ |

🔑 **Consequence, stated plainly: the tonnage-per-transit effect of a draft cut is INVISIBLE in this instrument.** A vessel drafted down to 47.5 ft carries less and still counts as one transit. **Neither the transit column nor any tonnage column in this document will register it.**

### 5d. STATED DAILY CAPACITY — a second capacity variable, distinct from realised transits

Nine issues carry a sentence of the form *“the maximum capacity … is approximately 36–38 vessels per day. Due to the current situation with the water levels in Gatun and Alhajuela Lakes, **the daily capacity has been adjusted to N vessels**.”* **This is ACP's declared operating ceiling — an administrative decision, not a realised count.**

| Issue | Declared capacity | Split |
|---|---:|---|
| A-18-2024 (May-2024) | **32** | 8 neopanamax / 18 supers / 6 regulars |
| A-21-2024 (Jun-2024) | **32** | 8 / 18 / 6 |
| A-27-2024 (Jul-2024) | **35** | 10 / 19 / 6 |
| A-33-2024 (Aug-2024) → A-01-2025 (Dec-2024) | **36** | 10 / 20 / 6 *(unchanged across 5 consecutive issues)* |

**The sentence disappears entirely from Jan-2025 onward** — consistent with the constraint being lifted rather than the disclosure changing, but **I cannot distinguish those two from this document alone.** Reported as observed.

⚠️ **In the 2023-24 trough ACP published a forward schedule of transit slots instead** (A-49-2023 carries: Dec 1–31 → **22**/day, Jan 1–31 2024 → **20**/day, from Feb 1 2024 → **18**/day). **Those are booking-slot ceilings announced ahead of time**, and the realised Jan-2024 figure came in at **22.6/day**, above the 20 ceiling — **the two are different quantities and must not be reconciled to one number.**
---

## 6. AUCTIONED-SLOT UTILISATION — the 2023-24 drought vs now

🔴 **READ THE TWO LEVELS, NOT THE RATIO. The denominator is set by ACP, not by the market.** Utilisation is `Used ÷ Available`, and **ACP controls `Available` as a policy lever.** The same 95% means opposite things at the two ends of this series:

| | Oct-2023 (drought) | Sep-2025 (normal) |
|---|---|---|
| Auctioned **% used** | **95.21%** | **95.34%** |
| Auctioned **available** | **146** | **354** |
| Auctioned **used** | **139** | **348** |

**Near-identical ratios; 2.5× the absolute slot demand.** A utilisation series alone would show these two months as equivalent. **They are not.**

### The shape, by regime

| Regime | n | Auctioned available | Auctioned used | Utilisation | Transits/day |
|---|---:|---|---|---|---|
| **Drought trough** Oct-23 → Feb-24 | 5 | **146–196** (scarce) | 139–196 | **88.8–100%** (mean 94.3) | **22.6–32.4** |
| **Recovery** Apr-24 → Dec-24 | 9 | 252–354 (opening up) | 166–205 | **48.2–81.4%** (mean 60.5) | 26.0–34.2 |
| **Normalised** 2025 | 12 | 354–467 | 239–384 | 63.1–100% (mean 89.2) | 31.4–34.8 |
| **Current** Jan-26 → Jul-26 | 7 | 249–377 | 216–286 | **70.3–86.8%** (mean 79.6) | **32.5–38.7** |

**Plain reading of the shape (no grading):**

1. **The drought signature is a COLLAPSED DENOMINATOR, not high utilisation.** At the trough ACP offered **146 auctioned slots** against **354** at the 2024 peak. **Scarcity showed up as fewer slots on offer**, and utilisation pinned near 100% because supply was cut to meet demand — Dec-2023 printed exactly **196 available / 196 used / 100.00%**.
2. **The clearest single drought marker in this whole document is `transits/day`, and it bottomed at 22.6 (Jan-2024) / 22.8 (Feb-2024)** against **38.70 (Apr-2026)** — a **~41% drawdown**. *(A-11-2024, the March-2024 issue that would sit between them, is the one month I could not open — §7.)*
3. **Utilisation FELL as conditions improved** (48.16% in Aug-2024, the series low) because ACP re-opened slots faster than auction demand returned. **A falling utilisation number here is a loosening signal, not a weakening-demand signal.** The two are indistinguishable from the ratio alone.
4. **Today does NOT resemble the 2023-24 trough on this instrument.** Jul-2026 sits at **306 available / 247 used / 80.72%** with **34.03 transits/day** — denominator roughly double the trough's, utilisation mid-range, transits ~50% above the trough. **The 2026 draft cuts have not (yet) appeared in either the transit count or the slot book.**
5. ⚠️ **But point 4 is exactly what ACP said would happen** — *“the draft adjustment will not affect the number of daily vessel transits.”* **The absence of a signal in this instrument is not evidence of an absent restriction.** *(Stated as an instrument limit, not a channel call. AEOLUS grades.)*

---

## 7. GAPS — reported, not worked around

### 7a. 🔴 THE ONE MISSING MONTH: **March 2024** — `A-11-2024`

**The PDF downloads fine (HTTP 200, 508,177 bytes) and is password-protected.** It is not a 404 and not a bad URL.

```
URL tried:  https://pancanal.com/wp-content/uploads/2024/01/ADV11-2024-Monthly-Canal-Operations-Summary-March-2024-1.pdf
curl:       HTTP 200, 508177 bytes  (file downloads intact)
pdfminer:   PDFPasswordIncorrect
pdftotext:  Command Line Error: Incorrect password
pikepdf:    PasswordError: 2024-03.pdf: invalid password
encryption: /Filter /Standard /V 4 /R 4 /Length 128 /CFM /AESV2  (AES-128, user password set)
```

**Three independent PDF libraries agree an empty user password is rejected.** I also tried the non-`-1` filename variant — `…Summary-March-2024.pdf` returns **HTTP 200 / 392,603 bytes but is an HTML error page, not a PDF** (`No /Root object`; poppler: *“May not be a PDF file”*). **A soft-404.** The `-1` file is the only real one and it is locked.

⚠️ **No substitute sought and none should be.** March-2024 sits inside the drought recovery, between Feb-2024 (**22.8/day**) and Apr-2024 (**26.3/day**) — **the steepest part of the ramp, so the missing month is the least interpolatable one in the series.** Do not fill it by interpolation.

### 7b. Not gaps — confirmed absent by design

- **Tonnage**: no row in the statistics table in **33 of 33** issues (§5c).
- **Draft**: no row in the statistics table in **33 of 33** issues; present in appended prose in **8** issues (§5a).
- **Gatun elevation**: no row in the statistics table in **33 of 33** issues; **one** numeric figure in appended prose, in A-27-2024 (§5b).

---

## 8. DATA-QUALITY FLAGS — ACP's own arithmetic, not transcription errors

All three were caught by the self-checks and **re-read at the PDF to confirm the printed values**. **I did not correct any of them** — the tables above carry ACP's figures as printed.

| Month | Flag | Printed | Computed | Note |
|---|---|---|---|---|
| **May-2025** (A-18-2025) | class components ≠ printed total | 160 + 541 + 273 = **974**; **Total: 973** | — | Off by 1 transit. **973 ÷ 31 = 31.39 reproduces the printed 31.4 daily average**, so the *total* is the self-consistent figure and the component sum is the odd one. |
| **Aug-2025** (A-26-2025) | auctioned % ≠ used ÷ available | **96.18%** (395 avail / 382 used) | **96.71%** | Implied denominator ≈ 397. |
| **Sep-2025** (A-30-2025) | auctioned % ≠ used ÷ available | **95.34%** (354 avail / 348 used) | **98.31%** | Implied denominator ≈ 365. ⚠️ **AEOLUS currently carries 98.31% for Sep-2025 — that is the DERIVED value. The advisory prints 95.34%.** |

🔑 **The Sep-2025 one matters beyond itself:** it is the month AEOLUS holds as a verified anchor. **The available/used pair (354/348) is exactly right; the percentage was recomputed rather than read.** Recomputation looked like verification and silently replaced a printed figure. **Every percentage in §4 is the printed one, with `calc U÷A` shown beside it so the two can never be confused again.**

**One extraction artifact, disclosed:** in A-01-2026 (Dec-2025) the *Canal Waters Time **Low*** cell renders as two text runs, `14.4` + `4`. Recombined to **14.44**. It affects no daily-average column. All other reported values passed both parsers unchanged.

---

## 9. PROPOSED INSTRUMENT NAMES — proposals only, NOT created

Per the worker contract I appended rows to `workbook/SERIES.tsv` **only** under names that already exist in the ledger. **Everything else below is a naming proposal for AEOLUS to accept, rename or reject.** No row was written under any of the proposed names.

| Status | Name | Unit | Source token | Cadence | Notes |
|---|---|---|---|---|---|
| ✅ **existing — rows written** | `panama_transits` | count | `ACP-MONTHLY-OPS-SUMMARY` | monthly | Oceangoing transits **daily average**, traffic block. 28 new rows (5 months already present). |
| ✅ **existing — rows written** | `panama_max_draft_ft` | feet | `ACP-ADVISORY` | event | Name established in `SERIES.tsv` on 2026-08-21 by a prior run; **not in `AGENT.md`'s vocabulary table — AEOLUS should ratify or rename.** 6 historical rows added. |
| 🟡 proposed | `panama_transits_total` | count | `ACP-MONTHLY-OPS-SUMMARY` | monthly | Monthly total transits. Enables the ÷days self-check to be re-run from the ledger. |
| 🟡 proposed | `panama_arrivals` | count | `ACP-MONTHLY-OPS-SUMMARY` | monthly | Daily average. **Must be separately named — the adjacency to transits is the known misread.** |
| 🟡 proposed | `panama_transits_neopanamax` / `_supers` / `_regular` | count | `ACP-MONTHLY-OPS-SUMMARY` | monthly | Beam-class daily averages. **The Neopanamax leg is the one the draft cuts bind on.** |
| 🟡 proposed | `panama_cwt_hours` | hours | `ACP-MONTHLY-OPS-SUMMARY` | monthly | Canal Waters Time, daily avg. **Congestion proxy — it moved 19→54 h across this window while transits moved far less.** |
| 🟡 proposed | `panama_intransit_hours` | hours | `ACP-MONTHLY-OPS-SUMMARY` | monthly | In-Transit Time, daily avg. |
| 🟡 proposed | `panama_auction_slots_avail` / `_used` | count | `ACP-MONTHLY-OPS-SUMMARY` | monthly | 🔑 **Store the two LEVELS.** Utilisation is derivable; the reverse is not, and the ratio alone is ambiguous (§6). |
| 🟡 proposed | `panama_declared_capacity` | count | `ACP-MONTHLY-OPS-SUMMARY` | event | ACP's declared daily ceiling (32/35/36). **A policy variable, not a realised count — do not reconcile with `panama_transits`.** |
| 🟡 proposed | `gatun_elev_ft` | feet | `ACP-ADVISORY` | irregular | **Only one observation exists (85.02 ft, ~2024-08-09).** Registering the name now fixes unit + datum before the live instrument is found. |
---

## 10. APPENDIX — advisory number, date and URL per month

**Every URL below returned HTTP 200 and a parseable PDF on 2026-08-21 except A-11-2024, which returned 200 and an encrypted PDF (§7a).**

| Month | Advisory | Advisory date | URL |
|---|---|---|---|
| Oct-2023 | A-49-2023 | November 8, 2023 | `https://pancanal.com/wp-content/uploads/2023/11/ADV49-2023-Monthly-Canal-Operations-Summary–October-2023.pdf` |
| Nov-2023 | A-53-2023 | December 7, 2023 | `https://pancanal.com/wp-content/uploads/2023/01/ADV53-2023-Monthly-Canal-Operations-Summary-–-November-2023.pdf` |
| Dec-2023 | A-02-2024 | January 10, 2024 | `https://pancanal.com/wp-content/uploads/2024/01/ADV02-2024-Monthly-Canal-Operations-Summary-–-December-2023.pdf` |
| Jan-2024 | A-04-2024 | February 9, 2024 | `https://pancanal.com/wp-content/uploads/2024/01/ADV04-2024-Monthly-Canal-Operations-Summary-–-January-2024.pdf` |
| Feb-2024 | A-07-2024 | March 8, 2024 | `https://pancanal.com/wp-content/uploads/2024/01/ADV07-2024-MONTHLY-FEB.pdf.pdf` |
| Apr-2024 | A-14-2024 | May 10, 2024 | `https://pancanal.com/wp-content/uploads/2024/01/ADV14-2024-Monthly-Canal-Operations-Summary-–-April-2024.pdf` |
| May-2024 | A-18-2024 | June 10, 2024 | `https://pancanal.com/wp-content/uploads/2024/01/ADV-18-2024-Monthly-Canal-Operations-Summary-May-2024.pdf` |
| Jun-2024 | A-21-2024 | July 10, 2024 | `https://pancanal.com/wp-content/uploads/2024/01/ADV21-2024-Monthly-Canal-Operations-Summary-June-2024.pdf` |
| Jul-2024 | A-27-2024 | August 9, 2024 | `https://pancanal.com/wp-content/uploads/2024/08/ADV27-2024-Monthly-Canal-Operations-Summary-July-2024.pdf` |
| Aug-2024 | A-33-2024 | September 11, 2024 | `https://pancanal.com/wp-content/uploads/2024/09/ADV33-2024-Monthly-Canal-Operations-Summary-August-2024.pdf` |
| Sep-2024 | A-38-2024 | October 10, 2024 | `https://pancanal.com/wp-content/uploads/2024/10/ADV38-2024-Monthly-Canal-Operations-Summary-September-2024.pdf` |
| Oct-2024 | A-41-2024 | November 14, 2024 | `https://pancanal.com/wp-content/uploads/2024/11/ADV41-2024-Monthly-Canal-Operations-Summary-October-2024.pdf` |
| Nov-2024 | A-45-2024 | December 10, 2024 | `https://pancanal.com/wp-content/uploads/2024/01/ADV45-2024-Monthly-Canal-Operations-Summary-November-2024.pdf` |
| Dec-2024 | A-01-2025 | January 10, 2025 | `https://pancanal.com/wp-content/uploads/2025/01/ADV01-2025-Monthly-Canal-Operations-Summary-December-2024.pdf` |
| Jan-2025 | A-04-2025 | February 11, 2025 | `https://pancanal.com/wp-content/uploads/2025/01/ADV-04-2025-Monthly-Canal-Operations-Summary-January-2025.pdf` |
| Feb-2025 | A-05-2025 | March 10, 2025 | `https://pancanal.com/wp-content/uploads/2025/03/ADV-05-2025-Monthly-Canal-Operations-Summary-Feburary-2025.pdf` |
| Mar-2025 | A-08-2025 | April 10, 2025 | `https://pancanal.com/wp-content/uploads/2025/01/ADV-08-2025-Monthly-Canal-Operations-Summary-March.pdf` |
| Apr-2025 | A-11-2025 | May 08, 2025 | `https://pancanal.com/wp-content/uploads/2025/01/ADV-11-2025-Monthly-Canal-Operations-Summary-April-2025-.pdf` |
| May-2025 | A-18-2025 | June 10, 2025 | `https://pancanal.com/wp-content/uploads/2025/01/ADV-18-2025-Monthly-Canal-Operations-Summary-May-2025-1.pdf` |
| Jun-2025 | A-21-2025 | July 10, 2025 | `https://pancanal.com/wp-content/uploads/2025/01/ADV-21-2025-Monthly-Canal-Operations-Summary-June-2025.pdf` |
| Jul-2025 | A-24-2025 | August 8, 2025 | `https://pancanal.com/wp-content/uploads/2025/01/ADV-24-2025-Monthly-Canal-Operations-Summary-July-2025.pdf` |
| Aug-2025 | A-26-2025 | September 09, 2025 | `https://pancanal.com/wp-content/uploads/2025/01/ADV-26-2025-Monthly-Canal-Operations-Summary-August-2025.pdf` |
| Sep-2025 | A-30-2025 | October 10, 2025 | `https://pancanal.com/wp-content/uploads/2025/01/ADV-30-2025-Monthly-Canal-Operations-Summary-September-2025.pdf` |
| Oct-2025 | A-35-2025 | November 10, 2025 | `https://pancanal.com/wp-content/uploads/2025/11/ADV-35-2025-Monthly-Canal-Operations-Summary-October-2025-.pdf` |
| Nov-2025 | A-36-2025 | December 10, 2025 | `https://pancanal.com/wp-content/uploads/2025/12/ADV-36-2025-Monthly-Canal-Operations-Summary-November-2025.pdf` |
| Dec-2025 | A-01-2026 | January 08, 2026 | `https://pancanal.com/wp-content/uploads/2026/01/ADV-01-2026-Monthly-Canal-Operations-Summary-December-2025.pdf` |
| Jan-2026 | A-03-2026 | February 10, 2026 | `https://pancanal.com/wp-content/uploads/2026/02/ADV-03-2026-Monthly-Canal-Operations-Summary-January-2026.pdf` |
| Feb-2026 | A-04-2026 | March 10, 2026 | `https://pancanal.com/wp-content/uploads/2026/03/ADV-04-2026-Monthly-Canal-Operations-Summary-February-2026.pdf` |
| Mar-2026 | A-09-2026 | April 10, 2026 | `https://pancanal.com/wp-content/uploads/2026/04/ADV-09-2026-Monthly-Canal-Operations-Summary-March-2026.pdf` |
| Apr-2026 | A-14-2026 | May 8, 2026 | `https://pancanal.com/wp-content/uploads/2026/04/ADV-14-2026-Monthly-Canal-Operations-Summary-April-2026-.pdf` |
| May-2026 | A-19-2026 | June 9, 2026 | `https://pancanal.com/wp-content/uploads/2026/06/ADV-19-2026-Monthly-Canal-Operations-Summary-May-2026.pdf` |
| Jun-2026 | A-23-2026 | July 10, 2026 | `https://pancanal.com/wp-content/uploads/2026/07/ADV-23-2026-Monthly-Canal-Operations-Summary-June-2026.pdf` |
| Jul-2026 | A-26-2026 | August 10, 2026 | `https://pancanal.com/wp-content/uploads/2026/08/ADV-26-2026-Monthly-Canal-Operations-Summary-July-2026.pdf` |
| **Mar-2024** | **A-11-2024** | *(unread)* | `https://pancanal.com/wp-content/uploads/2024/01/ADV11-2024-Monthly-Canal-Operations-Summary-March-2024-1.pdf` 🔴 **password-protected** |

⚠️ **Filename convention is NOT predictable** and this table is the evidence: `ADV49-2023`, `ADV02-2024`, `ADV-18-2024`, `ADV-04-2025`, `ADV-14-2026-…-April-2026-.pdf` (trailing dash), `…-Feburary-2025.pdf` (misspelling), `…-March-2024-1.pdf` (WordPress duplicate suffix). **The upload path does not track the data month either** — Sep-2025 lives under `/uploads/2025/01/`. **Discover from the index in §1; never construct.**

---

## 11. RECONCILIATION WITH AEOLUS'S MID-RUN GUIDANCE (received after the build completed)

AEOLUS sent six verified URLs, a URL-path heuristic, and three findings intended to narrow the job. **All six URLs match mine byte-identical.** The other three are reconciled below against the 33-month corpus. **Two need correcting, and both corrections point the same way.**

### 11a. ⚠️ The `/uploads/YYYY/MM/` heuristic is a coin flip on this range — **do not use it**

**Claim:** *"the `/uploads/YYYY/MM/` segment tracks roughly the PUBLICATION month (data month + 1)."*

**Measured against all 33 observed URLs: it holds 17 of 33 (52%).**

| Where it holds | Where it fails |
|---|---|
| **16 of 19** months from Jul-2024 on, and **6 of 7** in 2026 | **15 of 21** months in Nov-2023 → Sep-2025 |

🔑 **The failure is not random — 15 of the 16 misses collapse into a single `/uploads/YYYY/01/` bucket** (e.g. Sep-2025 lives at `/uploads/2025/01/`, Jun-2024 at `/uploads/2024/01/`). The remaining miss is **Apr-2026 → `/uploads/2026/04/`, the *data* month** — and that URL is **in AEOLUS's own list of six**, so the sample used to infer the rule already contained a counterexample to it.

⚠️ **The heuristic fails hardest exactly where AEOLUS wanted it used.** It was offered to "speed your discovery of the 2023-25 months" and prioritised the Nov-2023 → May-2024 drought trough — **the window where it is wrong 15 times out of 21.** *(`finding_ranked_head_sample_is_not_the_population`: the rule was inferred from the recent tail, and recency correlates with the filing convention.)*

**Actual rule, stated completely:** the path segment is **one of three** — the publication month (17), a `/YYYY/01/` catch-all (15), or the data month (1). **All three are unpredictable per-month, so the path is not constructible.** This cost AEOLUS a round of 404s and is why §1's index is the answer: **the index carries the exact URL, so no rule is needed.**

### 11b. ⚠️ "Tonnage, draft and Gatun elevation are NOT in the Monthly Summary" — right about the TABLE, wrong as a stop-hunting instruction

**The keyword evidence is exactly right and I reproduce it: literal `PLD` = 0 occurrences and literal `elevation` = 0 occurrences across all 33 issues.** No tonnage row, no draft row, no elevation row in the statistics table, in any issue.

🔴 **And a Gatun lake elevation is nonetheless present** — in A-27-2024, written as:

> *"Gatun Lake today is at **85.02 feet** (25.91 m)"*

**That sentence contains neither `PLD` nor `elevation`.** The keyword could not have found it. **The check was sound; it just wasn't an instrument for the thing it was used to rule out** — ACP does not write "elevation", it writes *"is at N feet"*. *(`finding_hypothesis_needs_an_instrument_for_its_defining_mechanism` — name the instrument for the mechanism the claim refers to.)*

**Same shape for draft.** AEOLUS's stated sample was six 2026 advisories + Sep-2025 + Jun-2024. **Two of those eight contain a numeric draft in feet:**

| Issue in AEOLUS's own sample | Numeric draft found |
|---|---|
| **A-21-2024 (Jun-2024)** | **47 ft** — *"the maximum authorized draft was raised today from 46 to 47 feet"* |
| **A-26-2026 (Jul-2026)** | **48 ft, 47.5 ft** — the live 2026 reduction |

**Corpus totals: numeric draft in 6 issues, tonnage figures in 5, Gatun elevation in 1.** All in the appended news article, never in the table.

🔑 **Why this matters more than the individual figures.** The instruction was *"note it once as an absence and move on — do not keep hunting it per-month."* **Following it would have skipped the single item the brief named as the highest-value thing to return.** The absence is real at the table level and does not generalise to the document, because **the table is fixed-schema and the appended article is discretionary** — so its contents can only be established per-issue. **The per-month sweep is the only method that finds them, and it costs one regex pass over text already extracted.**

### 11c. ✅ Confirmed and already applied

- **Auctioned slots are collected for all 33 months** (§4) — and §6 shows why the two levels must be stored rather than the ratio.
- **`used > available` rows recorded as printed and flagged, never normalised** (§4) — 105.65 / 111.02 / 114.53 in Apr-2026 reproduce exactly.
- **Drought trough prioritised:** Nov-2023 → May-2024 is complete **except Mar-2024**, which is password-protected (§7a).
- ⚠️ **Sep-2025 is quoted again in the guidance as 98.31%. The advisory prints 95.34%** (§8). The 354/348 pair is correct; the percentage was recomputed, not read.
