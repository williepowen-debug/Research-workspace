# 2026-09-18 — BOJ MPM grade, FOMC, and the dark-period catch-up

**Session:** Will-directed boot, September 18 2026 ~11:00 ET. SAM was dark 2026-09-15 09:35 → 2026-09-18; the BOJ MPM, the FOMC and the August trade/CPI prints all landed inside that window.

**Primaries parsed in-session (not relayed):** `k260918a.pdf` (BOJ statement, pdfminer) · `ope20260916.xlsx` (BOJ operation record, openpyxl) · federalreserve.gov SEP projections · customs/METI via `trade_balance.py` · Statistics Bureau via `cpi.py`.

---

## 2026-09-18 — BOJ MPM GRADE (owner grade; PROME DOCKET L34 closes on this)

**BOJ raised the policy rate 25bp to 1.25%, vote 7–2, effective September 24.** Primary: `k260918a.pdf`, downloaded and text-extracted in-session — vote footnote read verbatim, not relayed.

SAM pre-registered a three-leg read of this meeting (prior § WHAT TO WATCH). Graded on its own terms, no leg re-tuned at scoring time:

| Leg | Registered condition | Outcome | Grade |
|---|---|---|---|
| **1. Vote split** | "a 2+ dissent **for a faster pace** is the only hawkish surprise left" | 2 dissents — **both for HOLD.** ASADA Toichiro: CPI less fresh food "being below 2 percent … desirable for the Bank to **maintain** the guideline." SATO Ayano: developments "did not appear to have substantially accelerated … not appropriate … to raise the policy interest rate at this time." | 🔴 **HAWKISH SURPRISE DID NOT FIRE.** The dissent count matched; the SIGN is the mirror image of the registered condition. |
| **2. Oil naming** | downside-risk-to-activity ⇒ dovish-for-pace · second-round-price-risk ⇒ hawkish | Named **both ways**, activity framing dominant: Middle East "expected to push down economic activity" (twice, incl. Attachment ¶2 on crude specifically); price side reaches only PPI ("high crude oil prices and the depreciation of the yen"), while CPI is framed as wage-pass-through. | 🟢 **DOVISH-FOR-PACE**, as the leg's dovish branch specifies. |
| **3. Balance sheet** | "a change is the surprise" | **No JGB purchase-plan change.** Sole balance-sheet-adjacent action: climate-response funds-supplying ops moved to a floating loan rate with loan caps — **unanimous**, technical, not the FY2027 plan. | 🟢 **NO SURPRISE**, as registered. |

⚠️ **The composite clause MISSED on mechanism and landed on direction, and it is graded as a miss.** The registered sentence was *"The surprise is a HOLD, and it is yen-NEGATIVE."* **No hold printed** — a fully-priced hike did. The yen weakened anyway (USD/JPY 154.82 [9/15] → **157.34** [9/18 15:01:50 UTC]), but through the **dovish split + full pricing**, not the named mechanism. ⛔ Do not bank this as a directional hit: the desk's own failure-pattern canon (mechanism-direction class) is that a right call for a wrong mechanism is a calibration LOSS, not a win.

**What the meeting actually establishes:** the BOJ hiked with core CPI at **1.7% — below its own 2% target** (National August, 2025 base; the BOJ's own text says "in the range of 1.5-2.0 percent", and Asada's dissent turns on exactly this). That is a hike delivered *ahead of* the data, with two members saying so on the record. **CH-004 confirmed a third time: a fully-priced hike does not unwind carry.**

**Consequences — none to the frame.** Carry-convexity remains RETIRED to LOW (v1.7); no retired gate re-arms; the 160 gate stays VOID, not re-armed; book FLAT. **SAM-33 is unaffected and un-falsified** — separately verified at the operation record (below), not inferred from the statement's silence.

**SAM-33, verified at the record:** BOJ `ope20260916.xlsx`, parsed in-session — 25Y+ bucket offered **750** (×¥100M), i.e. **exactly the Aug-31 scheduled size** (`mpr260831a.pdf`); bids ¥1,385 / accepted ¥751 ⇒ **BTC 1.84×** (was 2.51× on Sep-9 — a BOJ *purchase-op* cover ratio, NOT an auction BTC; different object, no demand grade drawn). No fixed-rate op, no unscheduled op, no size increase. **Falsifier UN-FIRED.**

**Also resolved while dark — FOMC Sep-16:** hiked 25bp to **3.75–4.00%**, 12–0; SEP medians moved **UP** (2026 3.8→4.1%, 2027 3.6→4.1%). SAM's registered Fed-side tripwire is an **actual dot walk-back** — this is its opposite, by 50bp on the 2027 median. Route **ANTI-FIRED**.

---

---

## Dark-period ledger — everything that moved 9/15 → 9/18

| Item | Value | Basis |
|---|---|---|
| BOJ policy rate | 1.00% → **1.25%**, effective Sep-24 | `k260918a.pdf` |
| BOJ vote | **7–2**, Asada + Sato dissenting **for HOLD** (both dovish) | statement [Note], verbatim |
| Fed funds target | 3.50–3.75% → **3.75–4.00%**, 12–0 | federalreserve.gov |
| Fed SEP median 2026 / 2027 | 3.8 → **4.1%** / 3.6 → **4.1%** | SEP projections table |
| Japan Aug trade balance | **−¥1,105.6B** (Jul −¥638.3B) | customs, sokuho |
| Japan Aug crude volume | 11,594 kKL, **+3.6% YoY** | customs |
| Japan Aug **ME** crude volume | 7,255 kKL, **−30.9% YoY** | customs |
| Japan Aug crude value | ¥1,190.5B, **+58.7% YoY**; $102.8/bbl | customs |
| National CPI Aug (2025 base) | headline **1.9** / core **1.7** / core-core **1.9** | Statistics Bureau |
| MOF weekly foreign LT debt | **+¥1,082.9B buying**, Sep 6–12 | MOF ITS |
| MOF 4-week LT | **−¥1.608T** (prior window −¥1.55T) | recomputed from MOF_FLOWS.tsv |
| USD/JPY | 154.82 [9/15] → **157.34** [9/18 15:01:50Z] | yfinance `USDJPY=X` |
| FXY | 59.43 [9/14 close] → **58.30** [9/18 15:01:25Z] | vendor |
| Brent | $106.90 [9/15] → **$99.56** [9/18 14:51:21Z] | BZ=F, continuous |
| JGB MOF 10Y / 30Y / 40Y | **2.993 / 4.047 / 4.036%** [Sep-17] | MOF curve |
| US–JP differential 5Y / 10Y | **2.458 / 1.947pp** [Sep-17] | `rate_differential.py` |

⚠️ **The trade-balance row is the one that needs a second look and gets one separately:** total crude volume ROSE +3.6% while Middle East crude volume FELL 30.9%. Japan substituted barrels rather than losing them. That is a different physical story from the one the oil-in-yen Phase-1 framing assumes, and it is taken up in its own pass — it is not graded here.

## What did NOT happen

- **No BOJ emergency or unscheduled long-end capping operation** (SAM-33 falsifier un-fired, verified at the record).
- **No JGB purchase-plan change** at the MPM.
- **No Fed dot walk-back** — the opposite, by 50bp on the 2027 median.
- **No MOF intervention signature** identified in the window.
- **No retired gate re-armed.** Carry-convexity stays RETIRED to LOW; the 160 gate stays VOID; book FLAT.
