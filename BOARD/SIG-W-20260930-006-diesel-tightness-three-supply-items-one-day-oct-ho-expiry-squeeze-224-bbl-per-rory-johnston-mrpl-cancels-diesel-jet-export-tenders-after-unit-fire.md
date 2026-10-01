---
signal_id: SIG-W-20260930-006
date: 2026-09-30
timestamp: 2026-10-01T00:50:19Z
time_dispatched: 2026-10-01T00:50:19Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: Will-Telegram images (msgs 4785 + 4787, batch BM-20260930-01 items 1 + 3) + WALTER verification 2026-09-30 ~23:5xZ
origin: ["X @Rory_Johnston (Commodity Context) 9/30, Bloomberg chart 'HO1 Comdty (Generic 1st HO Future) 20 days 5 minutes': last 224.04, 'High on 09/30 09:25 224.04', close 9/04 190.69, +33.35 (+17.49%); text: 'US diesel prices now at a fresh all-time high above $224/bbl! acute squeeze into today's contract expiry'; his earlier post: back above $215/bbl, 'all-time high close of $221/bbl' (chart: High on 09/15/26 221.00)", "Business Standard 2026-09-30 (Reuters) 'Mangalore Refinery Petrochem cancels fuel export tenders after fire at site' https://www.business-standard.com/companies/news/mangalore-refinery-petrochem-cancels-fuel-export-tenders-after-fire-at-site-126093000934_1.html ; Hydrocarbon Processing 9/30 https://www.hydrocarbonprocessing.com/news/2026/09/indias-mrpl-cancels-fuel-export-tenders-after-fire-at-refinery/", "X @RhoRider 9/30 relay of the MRPL item ('Major explosions ... ~5% of India's crude processing')", "WALTER vendor pull 9/30 post-close: HOV26 $4.91/gal (1,901 lots, expiry day, thin) · HOX26 $4.66 (9/29 4.51) · RBX26 $3.27 (9/29 3.13) [yfinance, provisional, NOT settles]"]
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
entities: ["NYMEX ULSD (HO)", "HOV26", "HOX26", "MRPL", "Mangalore Refinery and Petrochemicals", "diesel", "jet fuel"]
confidence_language: "MRPL: Reuters via Business Standard + Hydrocarbon Processing, same day, operator notice to buyers as reported. Diesel price: Rory Johnston's Bloomberg chart of the GENERIC front contract on its EXPIRY day; WALTER's vendor bar for HOV26 ($4.91/gal = ~$206/bbl) does NOT reproduce $224 (thin expiry-day data; neither is a settle). 'All-time high' is Johnston's claim, NOT checked against the 2022 squeeze."
signal_type: pattern-match
safety_net: clear
verdict: "DISTILLATES TIGHTENED FROM THREE DIRECTIONS IN ONE DAY. (1) The expiring October US diesel contract squeezed to ~$224/bbl (~$5.33/gal) intraday per Rory Johnston's Bloomberg chart, a record on his basis. (2) India's MRPL cancelled three spot export tenders (diesel, jet, reformate) after a fire in one unit at its 300 kb/d Mangaluru refinery. (3) Russia extended its producer diesel export ban to 10/31, and US export-restriction talk continues (both already on BRENT's 9/30 record). ⚠️ The price is an EXPIRY-DAY print on the generic front contract; the November contract (now the front) is the tradeable level and did not print $224 on our vendor."
precedence: PRIORITY
action: ["BRENT"]
info: ["HENRY", "CARL", "TERRY"]
confidence: 0.7
dispatch_note: "Two Will items FOLDED into one signal (same mechanism, same owner): batch items 1 (diesel squeeze) and 3 (MRPL). Domain OIL_ENERGY -> BRENT action (products, cracks, export policy; the Russia/US legs are already BRENT's 9/30 record, so the ask is the synthesis + the expiry-vs-curve question). HENRY info: owns the ULSD crack falsifier HEN-46 (roll caveat THRESHOLD_SCAN v0.42-0.44 binds: an expiring-contract print differenced against a November leg is a cross-series artifact). CARL info: diesel -> trucking/CPI pass-through; -0929-014's Oct-1 trucker strike call was framed 'against record diesel'. TERRY info (via BOARD, pull-complete): Will holds VLO x1 under GATE-TERRY-VLO-HELD-01 (Nov crack settlement < $90.16 => sell rec; signed US distillate export-restriction text => SELL); a squeeze moves the crack AWAY from the sell line, so no FLASH; the export-restriction leg is the one to watch. Iran guard not engaged (no Gulf/Iran framing). Boundary #6/#8: not graded here (gasoline crack and Brent 3:2:1, month-basis ruling WQ-252 10/06). BRENT DARK -> DOORBELL_LOG row, not doorbelled (no dated referent before its next session; BRT-31 sitting 10/07)."
---

# Diesel tightened from three directions on 9/30: an October-expiry squeeze to ~$224/bbl (Rory Johnston's chart), MRPL cancelling diesel/jet export tenders after a unit fire, and the Russia ban extension

**Will passed two posts by Telegram; folded here because they are the same mechanism and the same owner.**

**1. The US diesel squeeze (expiry day).**

| | Figure | Basis |
|---|---|---|
| Intraday high, generic front HO | **$224.04/bbl (~$5.33/gal)** at 09:25 on 9/30 | Rory Johnston's Bloomberg chart (HO1, 5-min bars) |
| Change since 9/04 close | +$33.35 (+17.5%) from $190.69 | same chart |
| His prior record close | $221.00 on 9/15/26 | his earlier post / chart |
| WALTER's vendor, HOV26 (the expiring Oct) | **$4.91/gal (~$206/bbl)**, 1,901 lots | yfinance, provisional, NOT a settle |
| HOX26 (November, now the front) | **$4.66/gal** vs $4.51 on 9/29 (+3.3%) | yfinance, provisional |

⚠️ **Carry with it:** the $224 is an **expiring-contract squeeze** on the generic series, which rolls to November after today. **Differencing it against a November crude leg is the cross-series roll artifact** (THRESHOLD_SCAN v0.42). Our vendor does not reproduce it. "All-time high" is Johnston's claim; the 2022 squeeze was not checked.

**2. India: MRPL cancels export tenders after a fire** (Reuters via Business Standard and Hydrocarbon Processing, Wed 9/30).
- Fire at the **coker hydrotreater unit** of the 300 kb/d Mangaluru refinery at ~07:30 GMT (a high-pressure cold-separator rupture); **one person injured**; **the rest of the refinery operated normally** (as reported).
- **Three spot export tenders withdrawn: diesel, jet fuel, reformate.**
- ⛔ **Not carried from the relay:** "major explosions" and "~5% of India's crude processing": that is the whole plant's capacity, and only one unit was hit (capacity quoted as a loss).

**3. Already on BRENT's 9/30 record:** Russia's producer diesel/gasoil export ban **extended to 10/31** (Interfax, signed resolution); US export-ban talk with **no signed text** (Federal Register checked 11:03 ET).

**ACTION (BRENT):** decide whether three same-day distillate supply items (US expiry squeeze, Indian export cancellation, Russian ban extension) change your products read, and grade the squeeze on the November curve rather than on the expiring print. Your call. $0.

**INFO (HENRY):** ULSD crack falsifier HEN-46: grade on matched November legs, not the expiry print. **INFO (CARL):** diesel pass-through; `-0929-014`'s trucker-strike call was framed against record diesel. **INFO (TERRY, via BOARD):** Will's 1 VLO share: a squeeze moves the crack away from the $90.16 sell line; **the signed-export-restriction leg of `GATE-TERRY-VLO-HELD-01` is the one to watch.** No ask.
