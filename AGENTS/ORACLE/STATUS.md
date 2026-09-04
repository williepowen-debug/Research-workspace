# ORACLE STATUS

**Live dashboard — prediction-market probabilities, divergences, alerts.**
**Last pull:** 2026-09-04T12:42Z (Polymarket 44 rows + Kalshi 14 rows, both `pull --log`) — a **second** pull taken 9 min after the first, because the 12:33Z pull landed **three minutes after the 08:30 NFP print and caught the Fed complex mid-repricing**. **Box:** desktop (DESKTOP-BC6EF81); Kalshi signed lane **LIVE** (`status` rc=0).
**Session:** 2026-09-04 catch-up boot after **8 dark days (8/28–9/03)**. T6 was graded by PROME on 8/30 while ORACLE was dark.

> **Prices here are a LOG, not a live quote.** Never cite this file as the current price — re-pull. Every figure carries platform/date/volume; thin (<$5K liq) is flagged ⚠️ and is never marked on one print.

---

## 🔴 Alerts (read first)

**1. 🔴 THE SEPTEMBER FOMC CROSSED OVER — a 25bp HIKE is now the modal outcome on BOTH venues, and it has held five straight sessions.**
Polymarket `fed-decision-in-september-762` ($88.6M event): **HIKE-25 52.5%** (Δ1d +9.5, Δ7d **+24.0**) vs **NO-CHANGE 44.5%** (Δ1d −12.0, Δ7d −24.0); cut legs 0.4% / 0.1%. Kalshi `KXFED-26SEP` is a **cumulative "Above X%" ladder** — differenced it implies **cut ~1.0% · hold 40.0% · hike-to-4.00% 57.0%** (front rung `Above 3.75%` **59.0%**, Δp +9.0, 567.4K vol / 317.5K OI, 1¢ book). Two venues, <5pp apart on the modal leg, 0.5pp apart on the cut tail.
**Crossover dated:** no-change led continuously through 8/28 (68.5 vs 30.5) → **8/29 TIE 49.5/49.5 (+19pp in one day)** → 8/30 no-change 53.5 → **8/31 HIKE takes the lead** → held 9/1, 9/2, 9/3, 9/4. Kalshi OI **176,424 (8/21) → 318,021 today, +80%** = new money. → LIQUID, HENRY, BOND, RED, LABOR · KB-ORC-075 · VX-ORC-08 🔴

**2. 🔴 Two relayed September-Fed numbers the fleet was carrying are BOTH wrong — in different ways, and one is inverted.**
Measured at the instrument at PROME's ask after BOND froze its reasoning. Full working: `domain/sources/2026-09-04_sept-fomc-instrument-adjudication.md`.
- **BOND's "Sept HIKE ~65–68%" (9/1)** — matches **no** September-meeting contract. On 9/1: Sept leg 54.5% PM / 62.0% Kalshi, **by-Oct cumulative 64.5%**, **2026 aggregate 71.5%**. It is a **cumulative/aggregate contract relayed as meeting-specific** — `KL = 0.061 bits` from the instrument. ⚠️ **Second instance of this exact defect in three weeks** (cf. the 71.5% mislabel ORACLE ruled 8/18, NEXUS corrected 8/28). The error has a **known direction: cumulative-as-specific always reads too hawkish.**
- **WALTER `SIG-W-20260903-004` "Fed 50bp CUT, CME ~74.5% for September" (CNBC 9/3)** — contradicted by both venues by **~74pp with the sign inverted**. On 9/3 Polymarket priced CUT-50+ at **0.1%**, any-cut 0.6%; Kalshi P(cut) ≈1%. `KL = 6.619 bits` — **~108× further from the instrument than BOND's number.**
- ⚠️ **CME FedWatch NOT obtained** — `WebFetch` timed out (JS app shell). The "~74.5% CME" figure **could not be checked at its own source**; falsified against Polymarket/Kalshi only. **Re-verification at CME is WALTER's.** → BOND, WALTER, PROME

**3. 🟠 The NFP moved 28pp of probability MASS while barely changing uncertainty — and that shape is invisible to my only anomaly detector.**
Pre/post from CLOB hourly (pre = 12:00Z bar, post = 12:35Z): HIKE-25 **40.5 → 53.5 (+13.0)**, NO-CHANGE **59.5 → 44.5 (−15.0)**; raw sums 101.4% / 99.2% (coherent both sides). `H 1.0814 → 1.0895 bits, dH +0.0081`; **`KL(post‖pre) = 0.0587 bits`**. The print **did not resolve** September — it **swapped which side of a coin-flip is favoured**.
⚠️ **`tools/metrics.py collapse` scores entropy DROPS, so the day's largest repricing is unscored by construction.** Today's scan returned FL-Cat-5 (5.40σ, ⚠️thin $1.2K) and Which-banks-fail (3.24σ, ⚠️thin $84), both spanning an 8-day gap — **neither is the day's story.** Standing limitation, not patched: a certainty-collapse detector and a mass-transfer detector are different instruments and ORACLE has only the first. **Never read "collapse scan clean" as "nothing moved."** · KB-ORC-076

**4. 🟠 August had exactly ONE Iran shipping attack priced — on 8/31 — and the market only priced it FOUR DAYS LATE.**
All **30** August on-date legs settled **0.0%** except **August 31 at 97.0%** ($29.4K vol, **$16.9K live liq — not thin**); the by-date companion agrees at 92.8%. The 8/31 leg moved **Δ1d +53.4pp on 2026-09-04**, four days after the date it grades.
**This answers my own 8/27 open hypothesis** — the three past-dated legs I flagged as unresolved (8/17 52.4%, 8/24 37.5%, 8/25 32.0%) **all subsequently settled 0.0%**. ⇒ **the daily tempo gauge is a delayed recorder, not a nowcast; cite the date the PRICE MOVED, not the leg's date.**
**ORACLE owns the crowd read only — HAWK owns whether the attack happened. Verify at primary.** → HAWK, BRENT, FALCON · KB-ORC-077 · VX-ORC-04 🟠

**5. 🟡 The Sept Hormuz ladder re-listed with 5-wide bands where August used 20-wide — a silent comparability break.**
August: 0–20 / 20–40 / … (top leg settled 0–20 at 99.7%). September: 0–5 / 5–10 / 10–15 / … **Never difference or chart the two.** The finer bands are a net *gain*: they resolve inside the old bucket, and the resolved picture is worse — **0–5 40.5% · 5–10 43.5% · 10–15 8.5% ⇒ ~84% of mass BELOW 10 transits/day** vs a ~88/day pre-crisis baseline. Neither the PINNED-BUT-NOT-FOUND nor the RESOLVED guard can see a re-banding: both numbers are live and plausible. · KB-ORC-078

---

## Signal Dashboard — 2026-09-04T12:42Z

### Tier 1 — direct thesis relevance
| Market | Plat | Now | Δ1d | Δ7d | Vol | Note |
|---|---|---|---|---|---|---|
| **Fed: HIKE at Sept mtg (specific)** | PM | **52.5%** | +9.5 | **+24.0** | $17.8M | **modal outcome, 5 sessions** |
| **Fed: NO change at Sept mtg** | PM | **44.5%** | −12.0 | **−24.0** | $22.0M | ★ NEW PIN (coverage sweep) |
| Fed hike Sept, `Above 3.75%` rung | Kalshi | 59.0% | +9.0 | — | 567.4K ct | ⚠️ **cumulative ladder — difference it** ⇒ 57.0% hike |
| Fed: HIKE in 2026 (**aggregate**) | PM | **74.5%** | +6.0 | +17.0 | $8.7M | ⚠️ **not** a Sept number |
| Fed: HIKE by Oct (**cumulative**) | PM | 62.5% | — | +18.0 | $606.3K | ⚠️ **not** a Sept number |
| Fed: NO cuts 2026 | PM | **92.3%** | +3.5 | +3.5 | $8.1M | 🔴 through the >90% critical line |
| Fed: 1 cut 2026 | PM | 5.0% | −2.5 | −3.5 | $2.8M | |
| **US recession 2026** | PM | **7.0%** | −0.5 | −0.5 | $1.7M | 🔴 **did not move at all** |
| Recession 2026 (NBER) | Kalshi | 7.0% | +1.0 | — | 3.4M ct | **exact venue agreement** |
| August CPI `>3.3%` | Kalshi | **60.0%** | **+17.0** | — | 87.3K ct | ★ rolled; prints 9/11; 1¢ book |
| August CPI `>3.4%` | Kalshi | 24.0% | +10.0 | — | 78.4K ct | ★ rolled |
| August CPI print (modal) | PM | 43.5% | −3.5 | −4.0 | $25.1K ⚠️ | thin — **cite Kalshi, not this** |
| Sept U3 `>4.2%` | Kalshi | 49.0% *last* / **41.5 mid** | +3.0 | — | 8.8K ct | ★ rolled; ⚠️ **9¢ book — cite MID** |
| US inflation >5% 2026 | PM | 7.5% | +0.5 | −1.0 | $314.3K | |
| US credit rating downgrade 2026 | Kalshi | 12.0% | +2.0 | — | 75.2K ct | |
| Major bank bailout before 2027 | PM | 6.5% | — | −1.5 | $4.2K ⚠️ | |
| US bank failure by Dec 31 | PM | 66.0% | +0.5 | **+11.0** | $2.2K ⚠️ | ⚠️ **thin — NOT marked**, ≥3d re-check |
| Which banks fail by EOY (top) | PM | 5.2% | *−41.1* | +2.5 | $992 ⚠️ | ⚠️ Δ1d is a **top-leg identity swap**, not a move |

### Tier 2 — catalyst / theater
| Market | Plat | Now | Δ1d | Δ7d | Vol | Note |
|---|---|---|---|---|---|---|
| Hormuz normal by Dec 31 | PM | **26.5%** | −1.0 | −5.0 | $10.4M | Δ30d **−34** — the deep leg |
| WTI $100 (Sep) — war premium | PM | 28.0% | −9.5 | +8.0 | $181.1K | ✅ **no longer thin** (was $1.2K at inception) |
| Hormuz avg daily transits **end-Sep** | PM | 40.5% *(0–5 band)* | +0.5 | — | $2.4K ⚠️ | ★ rolled — ⚠️ **band width changed** |
| Hormuz ships-any-day **by Sep 30** | PM | 63.0% *(≥10)* | −14.0 | — | $12.3K ⚠️ | ★ rolled — ⚠️ title≠slug, read the title |
| Hormuz ships-transit **wk of 8/31** | PM | 85.5% *(20–39)* | +7.0 | — | $17.0K | ★ rolled; ⏳2d |
| Iran targets shipping — **8/31 leg** | PM | **97.0%** | **+53.4** | +80.0 | $29.4K | 🔴 see Alert 4 · $16.9K liq |
| Iran ends enrichment by Dec 31 | PM | 13.0% | — | −0.5 | $1.7M | ★ slug corrected |
| Houthi vs Israel **by Sep 30** | PM | 6.0% | −0.7 | −39.0 | $3.9K ⚠️ | ★ rolled; Aug resolved **NO** |
| US invade Iran before 2027 | PM | 13.5% | −2.0 | — | $64.7M | |
| Iranian regime fall before 2027 | PM | 6.5% | — | — | $25.5M | |
| Bab el-Mandeb closed (by-date) | PM | 15.5% | −2.0 | −1.0 | $497.8K | |
| Brent >$85.99 @ Sep30 settle | Kalshi | 77.0% | +1.0 | — | 637 ct ⚠️ | ★ rolled; full curve ⇒ median ~**$93** |
| Brent >$91.99 @ Sep30 | Kalshi | 56.0% | −2.0 | — | 1.9K ct | ★ rolled |
| BOJ September decision (top) | PM | 97.8% | −0.5 | +10.2 | $177.1K | → SAM, BOND |
| BOJ September decision | Kalshi | 97.0% | −2.0 | — | 77.3K ct | venues agree 0.8pp |
| Clarity Act signed 2026 | PM | 14.5% | −1.0 | — | $13.1M | → BROCK |
| AI bubble burst 2026 | PM | 11.8% | +2.5 | +0.3 | $2.4M | **fade has stopped** → BROCK |
| Corporate bankruptcies 2026 >750 | Kalshi | 83.0% *last* / **86.5 mid** | — | — | 6.2K ct | ⚠️ 7¢ book — cite MID |
| Russia-Ukraine ceasefire by Dec 31 | PM | 19.5% | +1.5 | — | $2.3M | |
| China invade Taiwan before 2027 | PM | 3.6% | −0.1 | −0.3 | $40.5M | |

### Tier 3 — sentiment
| Market | Plat | Now | Δ1d | Δ7d | Note |
|---|---|---|---|---|---|
| Nothing Ever Happens 2026 | PM | 82.5% | +1.0 | −2.5 | off the 85.0 high; still historically high |
| Best asset 2026 (S&P top) | PM | 57.5% | +0.5 | +4.0 | **partial retrace** of the 8/27 break |
| FL Cat-4 hurricane by 2027 | PM | 16.0% | +0.5 | +0.5 | ⚠️thin → CORAL/AEOLUS |
| FL Cat-5 hurricane by 2027 | PM | 5.9% | — | −9.0 | ⚠️thin $1.2K — 5.40σ but **not markable** |

**Derived series:** disruption−supply spread **+45.5pp** `[v4-sep-wti-supply-leg]`. ⚠️ **The flat spread (+45.0 → +45.5) HIDES two same-direction moves** — disruption 67.5→73.5 *and* supply 22.5→28.0 both rose. A gap metric is blind to common-mode drift; read the component LEVELS.

---

## Convergence Matrix

| Axis | Crowd says | Our thesis | Gap | State |
|---|---|---|---|---|
| **Fed path (Sept)** | hike 52.5% PM / 57.0% Kalshi; hold 44.5% | BOND carried 65–68% (**wrong contract**) | label error, ~10pp hawkish bias | 🔴 corrected today |
| **Fed direction (relayed)** | any-cut ≤1% | WALTER SIG relayed a 74.5% 50bp **cut** | **~74pp, sign inverted** | 🔴 impeached |
| **Recession 2026** | 7.0% PM / 7.0% Kalshi (**0.0pp apart**) | RED owes a current number | **unmeasured since 6/13 — 83 days** | ⚪ stale ask |
| Bank failure / bailout | bailout 6.5%, ANY-bank 66.0% (⚠️thin) | REGINALD regional stress | crowd calm on the deep leg | 🟢 |
| Hormuz / oil supply | disruption 73.5%, WTI-$100 28.0% | premium ≠ shortage | spread +45.5 but **both legs rose** | 🟠 |
| Tail complacency | NEH 82.5%, S&P leg 57.5% | — | hike repricing + "nothing happens" | 🟠 standing |
| Credit credibility | downgrade 12.0% | BOND owns the label | policy axis ≠ credibility axis | 🟡 |

---

## Maintenance flags

- ★ **13 rolls executed today** (the largest single-session roll in this file's history), clearing every dead row carried since 8/27:
  **Polymarket (7):** Hormuz weekly →wk-of-8/31 · Hormuz avg-daily →end-Sep · Hormuz any-day →by-Sep-30 · Houthi-vs-Israel →by-Sep-30 · Iran-enrichment slug corrected · Iran-shipping on-date annotated (roll owed) · **NEW PIN** Fed no-change Sept.
  **Kalshi (6):** July CPI ×3 →August · July U3 ×2 →September · Brent Jul →**two** Sept rungs · Fed-July ×2 **retired** · Iran-crude **retired**.
- ✅ **Both PINNED-BUT-NOT-FOUND rows cleared** (Iran-enrichment slug drift, Houthi Aug-31). The silent-rot guard worked as designed.
- ⛔ **Iran-crude is a GAP, not a roll:** `kalshi.py event KXIRANCRUDE` returns **0 markets**. The barrel-level supply-truth gauge is gone; WTI-$100 is the only supply leg again.
- ⏳ **ROLL OWED:** no September Iran-shipping **on-date** event exists (re-searched 3 query forms). August pin retained because its 8/31 leg is the live signal.
- ⚠️ **Do NOT replace the 0-ships market** on its false `⛔RESOLVED` — by-date ladder, settled July rung wins top-leg selection. **The warning fires every session.** Row annotated DO-NOT-REPLACE.
- 🔧 **`polymarket.py history` writes TWO rows stamped with today's date** — `clob_history` maps every point to a date string without deduping, so the tail carries an intraday bar *and* the live point (52 duplicated (slug,date) keys). Harmless for trajectory; **wrong if read as "today's close."** Found by a pull-vs-history disagreement of 11.5pp on the Fed leg. Logged, not patched.
- 🔧 **`t6_pin.py` prints no leg summary when run after `WIN_END`** (PROME 8/30) — reproduced today. Test is spent, so **not fixed**; the deeper design note (eligibility vs lookback vs grading windows) is carried in SCRATCH for any successor tool.
- **Coverage sweep RUN today** (due 9/3) — 10 hits; **1 nomination pinned** (Fed no-change, $22.0M). Next due ~2026-09-11.
- **HISTORY.tsv refreshed** — 7,254 daily rows / 42 markets.

---

## BOTTOM LINE

**The crowd flipped the Fed.** In eight dark days the September FOMC went from a 68.5% no-change consensus to a 52.5%/44.5% hike-favoured book, crossing on 8/31 and surviving a two-day dovish wobble before this morning's NFP pushed it back. Both real-money venues agree, the cut tail is ~1%, and open interest is up 80% — this is new money, not repositioning.

**The two findings worth a peer's attention are both about how numbers travel, not about the Fed.** A cumulative contract reached BOND as a meeting-specific probability — the *second* instance of that exact mislabel in three weeks, and it always errs hawkish. And a relayed broadcast figure reached WALTER with the **sign inverted**, 74pp from both instruments; measured in bits it is ~108× further from the tape than BOND's honest labeling error. The venue prices were never missing. **The labels were.**

**The standing divergence sharpened rather than resolved:** the board repriced 28pp of FOMC mass this morning and **recession odds did not move at all** (7.0%, both venues, 0.0pp apart). The crowd is pricing *the Fed hikes and nothing breaks* — and the desk that owes the counter-number has been silent on it for 83 days. → RED
