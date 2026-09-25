# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure (+ MBS/FHLB + EU rates per the 6/27 extension; + the sovereign-credibility instrument set per the 8/10 forum — scope in `CLAUDE.md`)
**Last session:** 2026-09-25 Fri **~01:03→02:xx ET (PROME item 2, Will-directed 01:01 ET: FR2004 timing + rates-move columns with HENRY)** · 2026-09-24 ~21:37→22:1x ET (post-close catch-up) · ~15:07→17:1x ET (second: owed-work + cleanup + FR2004 9/16 read) · earlier 9/24 ~13:00→14:1x (`bond-b0`, **first session since 9/17; BOND was dark 9/18–9/23**) · **Prior:** 2026-09-17

> 📕 **HOT/COLD SPLIT — NOTHING DELETED.** Full pre-rewrite snapshot of the 9/17 file: `domain/sources/2026-09-24_STATUS_full-snapshot_pre-9-24-rewrite.md` (23,719 B, crc32 `2559402921`). Older rotations: `archive/2026-09-01_STATUS_cold_pre-split-full-snapshot.md` and `domain/sources/2026-09-1*_STATUS_*`. **Budget 32,550 B — rotate, never raise.**

**Canonical elsewhere — no second copy here:** thesis → `thesis/THESIS.md` · predictions → `thesis/PREDICTIONS.tsv` · catalysts → `docket/CATALYSTS.tsv` · gates/positions → `TRADE.md` · learnings → `MEMORY.md` · handoff → `SCRATCH.md`.

---

## 🔴 TOP OF FILE — what changed since 9/17

00. ✅ **[9/25 ~01:0x ET, PROME item 2 / Will] FR2004 SETTLEMENT TIMING RESOLVED — the award is IN the print.** FR 2004A = trade-date; allotments count on the award date (FR 2004 Instructions eff. Jan 2022, GEN-6 §II.C · A-1; Appendix A: WI ⊂ A). ⇒ the 9/16 print is admissible; **the 9/23 5Y's dealer read is the 9/23 as-of, ~Thu 10/1 (not 10/8).** 🔴 **The WQ-157 join mis-windows Wednesday auctions (75/228): the "pairing INVERTS, p=0.009" evidence becomes −4.5bp, p=0.248 on the correct window — flagged to PROME; instrument NOT changed.** Rates-move columns (ACM/KW/composition) for HENRY: 9/15→9/23 ACM path +16.0 / TP −6.4 vs 10Y +11 — **but 9/22→9/23 TP +7.0 of +15**, and ACM vs KW disagree by 6.9bp on their only shared window. `KB-BND-332` · `analysis/2026-09-25_rates-move-TP-columns_and_FR2004-timing-RESOLVED.md`.

0. 🔴 **[POST-CLOSE 9/24, third session] THE LONG END MADE A SECOND STRAIGHT FRESH HIGH — U.S. Treasury official 9/24: 30Y 5.47 (+7; highest since 2004-06-28) · 20Y 5.53 · 10Y 5.18 (since 2007-07-06) · 5Y 5.03 (first official ≥5.00 since 2007-07-12) · 2Y 4.87 · 10Y REAL 2.85 (+9; since 2008-11-24 — only 22 prior sessions ever ≥ it, all Oct–Nov 2008).** Real-led again: breakevens FELL (T10YIE 2.35→2.33, T5YIFR 2.36→2.33 ⇒ 17bp from 2.50). MOVE **104.58** [9/24, VIOLET CONF] = 2nd consecutive ledger max, +33% in 2 sessions. `KB-BND-329`. **Matrix unchanged at 14/35 — a second high is not row 1's ⇒5 letter.** FRED now carries the 9/23 cells (5.40 / 2.76) ⇒ the 9/25 identity check is DONE.
   🟢 **LIQUID answered the 🔴 5Y funding ask: NONE on 9/22–9/23 across every observable they hold** (SOFR distribution width 7bp = pre-hike, SOFR99−IORB +5, SRF token, TGCR−SOFR −2). Reserves −$83.6B w/w, but TGA +$100.1B explains >100% of it, and repo did not reprice. **The funding leg's real test is 9/30: ~$183B of 2Y/5Y/7Y settlement ON the quarter-end turn, read 10/1 + two non-Q-end sessions after (a Q-end spike alone is the null).** Caveat (LIQUID's): no tri-party, sponsored-repo or dealer-balance-sheet read. `KB-BND-330`.
   🟡 USD/JPY ~158.9 held ~30h above the 9/18 rate-check level, no intervention; Katayama "principles… remain alive" (WALTER −018 as CORRECTED by −019). BOND leg = the UST-supply risk if Japan sells reserves. `KB-BND-331`.

1. 🔴 **9/23 5Y `91282CRN3` = OLD CONJUNCTIVE COMPOSITION FAILURE** — indirect **54.31%** (min 59.24; **lowest 5Y since 2020-03-25**) AND dealer **15.77%** (max 15.61, **+0.16pp**) · BTC **2.21** (lowest since 2018-12-26) · `I'` fired. ⇒ **the TLT-put ADD RE-ARM condition is MET — and Will DECLINED the add (WQ-280, ruled 13:17 ET 9/24, verbatim *"Approve WQ-280 and WQ-281 with your recs"*); no trade, no fresh card approved; `$0`.** ⛔ **Paired thesis kill NOT fired** (SOFR−IORB **−3bp** [9/23]). ⚠️ **Dealer 15.77 is ordinary on multi-year history (five 2023–24 prints higher, max 20.37); it cleared into a hot-PMI sell-off. THRESHOLD FIRED — MECHANISM NOT SHOWN FAILED.** Graded ~24h late. → `analysis/2026-09-24_GRADE_month-end-cluster_2Y-5Y-7Y.md`, `KB-BND-312`.
2. 🟠 **9/24 7Y `I'` marker by 0.037pp**; 9/22 2Y 🟢 clean. Downgrade counter **0**.
3. 🔴 **`BND-26` FALSE (70%, a MISS):** 1y1y **5.03 on FOMC day**, 5.08 [9/18] = new 2023-forward sample high. **This desk's 9/14 "a hawkish SEP has little room to surprise" is WITHDRAWN; the 4.75–4.95 terminal band is retired for reuse.** `BND-25` TRUE (55%). `KB-BND-315`.
4. 🔴 **9/23 OFFICIAL CURVE (U.S. Treasury par/real curves — the identical source of H.15: 182/182 exact 2026 matches on DGS30/10/2 and DFII10, verified 9/24): 30Y 5.40 = FRESH 2026 HIGH, highest since 2004-07-28 · 10Y 5.11, highest since 2007-07-13 · 2Y 4.85 · 10Y REAL 2.76 (+13bp d/d), highest since 2008-11-25 — 33 of 5,935 days ever ≥ it.** ⇒ matrix row 1's letter ("fresh DGS30 high WITH weak composition") FIRED on 9/23 ⇒ **row 1 3→4, composite 14/35.** ⚠️ The weak composition that day was the 5Y, not a long-end auction; the upgrade confirms this desk's own thesis — scored on the letter, disclosed. FRED republishes the same cells ~9/25.
5. 🔴 **The macro tape:** 9/23 flash composite PMI **58.4** (highest since 7/2021), input prices fastest since 10/2022 (S&P Global, secondary reports) ⇒ 5Y crossed **5%** first time since 2007; vendor 10Y **5.14**, 30Y **5.43** intraday 9/24 (**above the 5.37 official 2026 high — vendor, NOT counted**); October hike ~70% priced (TE 9/24, secondary). BOJ hiked to 1.25% 9/18; press-reported Japanese rate check ~¥158 (unconfirmed). BoE paused APF gilt sales 9/17 (a long-end SUPPLY withdrawal — `KB-BND-317`).
6. 🟠 **CCC 1093 [9/23] fresh 2026 high, 7bp from 1100**; CCC−BB **934** > the 926 span max. HY index 273, inert.
7. 🟡 **FR2004 as-of 9/16 (published 9/24 16:16 ET): long-end $144.4B, −$1.8B w/w — TOTAL fell, 11–21Y built +$1.7B, >21Y −$2.6B.** Graded against the 9/15 20Y-R `I'` fire on the join's convention: **TOTAL legs NOT met; only the non-significant 11–21Y bucket leg met ⇒ dealer-stock half of the paired kill NOT met on any significant leg** (which leg counts = WQ-157 leg ②, Will). ✅ **SETTLEMENT QUESTION RESOLVED 9/25 (`KB-BND-332`, CORRECTS `KB-BND-327`): FR 2004A is TRADE-DATE and includes an allotment from the award date (FR 2004 Instructions eff. Jan 2022, GEN-6 §II.C, A-1) ⇒ the 9/16 as-of CONTAINS the 9/15 award ⇒ this print IS admissible evidence on absorption: dealers booked the 20Y (its 11–21Y bucket +$1.7B) and net long-end stock fell.** 🔴 **Side-effect: the WQ-157 join mis-windows WEDNESDAY auctions (75/228); on the correct window the "pairing INVERTS, p=0.009" headline reads −4.5bp, p=0.248 — do not cite p=0.009.** `analysis/2026-09-25_rates-move-TP-columns_and_FR2004-timing-RESOLVED.md`. `KB-BND-326`.

---

## Regime (one-line)

**Real-rate / higher-for-longer — and the policy path is still repricing HAWKISHLY.** C-36 TWO-PART (ruled 9/1): policy-path channel ALIVE · term premium drove the July delta. **9/16 FOMC +25bp to 3.75–4.00 (12–0); the curve priced ABOVE the SEP median (4.125) and then kept going (`BND-26`).** **Auctions: "expensive, not broken" is UNDER TEST — first OLD-conjunctive fire on this desk's LIVE-graded record (KB searched 9/24; out-of-sample base rate 4/224 = 1.8%), on a macro sell-off day, with calm funding.** Full ruling → `thesis/THESIS.md` v1.2.7.

---

## Current Dashboard

*Pulled live **2026-09-24 21:37–21:4x ET (post-close)** via `monitors/boot_recompute.py` + `fetch.py` (cache-busted) + the U.S. Treasury par/real curve CSV for the **9/24 official cells** (FRED republishes ~9/25) unless tagged. No naked numbers.*

| Metric | Current | Status | Source / Date |
|---|---:|---|---|
| 30Y (DGS30) | **5.47%** | 🔴🔴 | [CONF **U.S. Treasury par curve 9/24** = the H.15 source; FRED 5.40 [9/23] ✅ identity held] — **FRESH 2026 HIGH, 2nd straight session (5.37 [9/10] → 5.40 → 5.47); highest since 2004-06-28**; run ≥5.00 = 57 on the Treasury cell (56 on FRED). 20Y 5.53. Vendor `^TYX` 5.46 [9/24 close] |
| 10Y (DGS10) | **5.18%** | 🔴 | [CONF Treasury par curve **9/24**; FRED 5.11 [9/23]] — +7bp d/d; highest since 2007-07-06. Vendor `^TNX` 5.16 [9/24 close] |
| 5Y (DGS5) | **5.03%** | 🔴 ↑ | [CONF Treasury par curve **9/24**; FRED 4.99 [9/23]] — first official close ≥5.00 since 2007-07-12 |
| 2Y · 1Y | **4.87% · 4.51%** | 🔴 ↑ | [CONF Treasury par curve **9/24**] — 2Y highest since 2024-06-10; **1y1y 5.23 (2×2Y−1Y par approx) = new 2023-forward sample high** (5.21 [9/23]; `BND-26` FALSE). Curve steepening long-end-led: 2s10s +31, 2s30s +60 |
| **10Y real (DFII10)** | **2.85%** | 🔴🔴 **GATE THROUGH** | [CONF **Treasury real curve 9/24**; FRED 2.76 [9/23] — **name the basis: two dates, both correct**] — **+35bp above 2.50 on the 9/24 Treasury cell; +9bp d/d (after +13); highest since 2008-11-24 (22 prior sessions ever ≥2.85, all Oct–Nov 2008)**; 5Y real 2.70, 30Y real 3.21. Every published session ≥2.50 since 9/10. "Sustained" count = WQ-246 (Will) |
| 5Y5Y fwd (T5YIFR) | **2.33%** | 🟡 ↓ | [CONF FRED **9/24**, computed from Treasury curves] — **17bp from 2.50** (14bp [9/23]) — widening away. ⚠️ *Corrected 9/24 ~13:2x: an hour earlier this row called the 9/23 cell "provisional" on WALTER −011's mechanism, which was already retracted (LIQUID 9/22, WALTER −004 9/24); FRED builds it from Treasury BC_/TC_ data — a real value on Treasury's schedule (`KB-BND-320` CORRECTED)* |
| 10Y BE (T10YIE) | **2.33%** | 🟡 | [CONF FRED **9/24**] = 5.18 − 2.85 exactly — **REAL-led two sessions running** (9/23 +13 real / +2 BE; 9/24 +9 real / −2 BE) |
| ACM 10Y TP · KW TP | **0.6454** [9/23] · **0.9595** [9/18] | 🟠 | [NY Fed ACM Daily · FRED `THREEFYTP10`, pulled 9/24 ~15:2x ET] — **ACM FELL 6.4bp 9/15→9/23 while the 10Y rose 11bp ⇒ under ACM the post-FOMC rise is expected PATH (~+17bp residual), not term premium** (`KB-BND-325`). KW 2026 high 0.9719 [9/16] = highest since 2011-02-10; KW frontier 9/18 cannot see the 9/23 surge. **Name the model in any TP claim** (model gap 6.8bp on 9/15→9/18, `KB-BND-299/325`) |
| **HY OAS** | **273bps** | 🟢 | [CONF FRED **9/23**] — 27bp from the 300 reopen line; 2026 max 346 |
| **CCC OAS** | **1093bps** | 🟠 ↑ | [CONF FRED **9/23**] — **fresh 2026 high** (+18bp d/d; prior max 1085 [9/15]); **7bp from 1100** (`BND-27`) |
| IG OAS | **77bps** | 🟢 | [CONF FRED **9/23**] |
| CCC−BB tail gap | **934bp** | 🟠 ↑ | [CONF FRED, BOND computation **9/23**] — BB 159; **above the 926 span max** |
| **FR2004 long-end** | **$144.4B** [as-of 9/16] | 🟡 | [NY Fed via `fr2004_fetch.py`, published 9/24 16:16 ET] — **−$1.8B w/w** after +$1.5B; 11-21Y **$68.5B (+1.7)**, >21Y $40.8B (−2.6), 7-11Y $35.1B (−0.9); **−17.5% off the 6/24 peak**. Lag 8 days: as-of 9/23 ~10/1, 9/30 ~10/8. **Basis RESOLVED 9/25: trade-date, award counted on award date (`KB-BND-332`)** |
| **SOFR − IORB** | **−3bp** | 🟢 | [CONF FRED SOFR 3.87 · IORB 3.90, **9/23**] — funding calm through the 5Y failure. LIQUID owns the plumbing read (asked 9/24) |
| TLT · MOVE | **$79.42 −1.29%** [9/24 close] · **104.58** [9/24] | 🟠 · 🔴 | [yfinance close — a MOMENT property, re-pull at any decision, root rule #4] TLT 81.80 [9/21] → 80.46 [9/23] → 79.42; 77P strike now 3.0% below. MOVE [CONF VIOLET 9/24, investing.com] 78.56 [9/22] → 95.45 → 104.58 = 2 consecutive ledger maxes — VIOLET owns the read |
| UK 10Y · Bund 10Y · JGB | 5.29 [TE 9/18] · 3.50–3.52 [9/18] · MOF dark to ~9/24 | 🟠 `[HANS/SAM own]` | UK basis caveat: BoE IADB par 5.2421 [9/16] vs TE — **name the basis** (`KB-BND-319`) |
| USD/JPY · Brent · VIX | **cite SAM · BRENT · VIOLET** | — | this desk keeps no copy |

### Gate distances *(recomputed this session, never carried)*

| Gate | Distance | State |
|---|---:|---|
| **DFII10 ≥2.50 — TLT-put add-gate (a)** | 🔴 **THROUGH by 35bp** [2.85, 9/24 Treasury] · 26bp [2.76, FRED 9/23] | Level leg held every published session since 9/10. ⛔ "Sustained" count = **WQ-246 (Will)**; authorises no add |
| **Auction re-arm (OLD conjunctive) — TLT-put add-gate** | 🔴 **MET 9/23 (5Y)** | ✅ **ADD DECLINED — WQ-280 RULED 9/24 13:17 ET** (four §B.1 grounds, `TRADE.md` Reactivation Matrix). Spent on 004 |
| T5YIFR >2.50 | 17bp [9/24] | 🟡 widening |
| DGS30 >5.00 · DGS10 >4.50 | — | 🔴 BREACHED (run 56) · 🔴 BREACHED |
| ~~`GATE-TERRY-007` (DGS10 <4.50 ×5)~~ | — | ⛔ **CLOSED `MOOT ⇒ NO-VERDICT` by TERRY 9/24 13:5x ET** (final counter 0 of 5; no 5-close streak can complete before the 9/30 expiry — `TERRY/setups/FLOW-TRIGGER_duration-TLT-put.md`, `04c5c7aad`). No longer carried here |
| HY OAS >300 (reopen HYG) | 27bp [9/23] | 🟢 |
| CCC >1100 escalation | **7bp** [9/23] | 🟠 closing |
| Credit-equity lead (HY +75–100 from the 263 trough) | 65–90bp | 🟢 inactive |

---

## Convergence Matrix

| # | Vector | Score | Status | Rolls up (`workbook/VX.tsv`) | Key Signal | Upgrade Trigger |
|---|---|---:|:--:|---|---|---|
| 1 | Long-end / duration | **4** ▲ | 🔴 | `VX-BND-05` · `VX-BND-12` · `VX-BND-14` | **9/23: DGS30 5.40 = fresh 2026 high ON the 5Y composition-failure day ⇒ upgrade letter FIRED ⇒ 4**; **9/24: 5.47, a 2nd fresh high** (not the ⇒5 letter); DFII10 2.85 (highest since 2008-11); 1y1y 5.23 | ⇒5: a composition failure on a LONG-END auction (20Y/30Y) or the paired kill's mechanism leg confirming |
| 2 | Treasury auction health | **3** ▲ | 🟠 | `VX-BND-01` · `VX-BND-08` · `VX-BND-13` · ~~`VX-BND-09`~~ RETIRED (tail) | **9/23 5Y: BTC 2.21 < 2.28 cover bar (and <2.3 KEY-THRESHOLD cover marker) + OLD composition failure + `I'`; 7Y `I'` by 0.04pp.** Paired kill NOT fired (funding NONE per LIQUID; **FR2004 POST for the 9/23 (Wednesday) 5Y = the 9/23 as-of, ~Thu 10/1 on the trade-date window** — the as-shipped join would use 9/30, ~10/8; read both) | A composition failure with the funding/FR2004 leg CONFIRMED (paired kill) ⇒ 4 |
| 3 | Dealer absorption | **2** = | 🟡 | `VX-BND-04` · `VX-BND-16` | FR2004 9/16 long-end $144.4B (−$1.8B; 11–21Y +1.7, >21Y −2.6) — **ADMISSIBLE as absorption evidence: settlement question resolved 9/25, the 9/15 award is in the print (trade-date, `KB-BND-332`)**; next: 9/23 as-of ~10/1 = the 5Y's POST; 5Y dealer 15.77 is the trailing-12 max but ordinary vs 2023–24. **9/24 20–30Y buyback: $4.078B of $6B, F2 0.02% ⇒ OFF-THE-RUN (2 of 2 ops)** | Two consecutive builds on TOTAL with weak composition, or SOFR−IORB positive; F2 ON-THE-RUN fire |
| 4 | HY market function | **2** = | 🟡 | `VX-BND-02` · `VX-BND-11` | HY 273 inert; **CCC 1093 fresh high, 7bp from 1100**; CCC−BB 934 new span max | HY >300 with velocity, or a pulled-deal cluster |
| 5 | IG market function | **1** = | 🟢 | `VX-BND-03` · `VX-BND-10` | IG 77 [9/23] | IG >120 or a failed syndication |
| 6 | CDX-cash basis | **1** = | 🟢 | `VX-BND-06` | HYG/IEF z20 +1.28 [9/8, STALE] | Synthetic leading cash, sustained |
| 7 | Credit-equity lead | **1** = | 🟢 | `VX-BND-07` | Inactive — 65–90bp headroom | HY +75–100bp from 263 while VIX <20 |

**Composite: 14/35 — UP 2 (12 → 14), the first change in sixteen scoring sessions.** **Row 1 moved 3 → 4 on its registered letter** (fresh DGS30 high 5.40 with weak composition, 9/23 — scored on the Treasury par curve, identical to H.15 at 182/182; the weak composition was the 5Y, not a long-end auction; FRED confirms ~9/25). Row 2 moved **2 → 3 on a pre-registered rule, not a judgement**: the 5Y BTC 2.21 is below both its trailing-12 min (2.28) and the KEY-THRESHOLDS 2.3 cover marker, which "escalates the vector" (the 7/27 precedent, when the vector moved on a benign story because that is what pre-registration is for). **The KILL is a different test and did not fire.** Distribution: 🔴 1 · 🟠 1 · 🟡 2 · 🟢 3. **Re-summed: 4+3+2+2+1+1+1 = 14 ✅.** ⚠️ `VX.tsv` row-state write-back for `VX-BND-01` owed at closeout.

**Outside the composite:** `VX-BND-15` inflation anchoring (2) · `VX-BND-17` MBS relay (1) · `VX-BND-18` FHLB (2) · `VX-BND-19` EZ rates (3 — HANS: ECB T-04 no longer a hawkish lean; German 2027 debt service +38%; "disorderly" UNDEFINED → 10/1) · `VX-BND-20` benchmark UST demand (2, checkpoint 10/6).

### Prediction scoreboard *(canonical: `thesis/PREDICTIONS.tsv`)*

**OPEN: 1** — `BND-27` (CCC <1100 through 9/30, 65%; **7bp away, 1093 [9/23], five sessions left** — momentum against it). **Resolved 9/24:** `BND-25` **TRUE** (55%) · `BND-26` **FALSE** (70%). Earlier: `BND-29` TRUE 9/17 · `BND-28` TRUE 9/15. **Tally: 14 TRUE · 12 FALSE · 1 VOID.** Archives: `thesis/archive/PREDICTIONS_resolved_*`. ⚠️ **No new predictions registered this session; the 10/28 FOMC curve-shape row is owed with a base rate by 10/21.**

---

## Trade Interface *(full view → `TRADE.md`; construction is TERRY's lane)*

- **TLT puts (Sep-30 77P ×20 — 5 of 25 sold 9/10, `FORGE/STATUS.md:54`) — HOLD, no add, `$0`.** 🔴 **BOTH add-gates now read through on their letters:** (a) DFII10 2.63 (sustain count WQ-246) and **the OLD-conjunctive auction re-arm (9/23 5Y)**. ⛔ **Neither is an add: WQ-280 RULED 9/24 — ADD DECLINED (Will verbatim *"Approve WQ-280 and WQ-281 with your recs"*); a fresh TLT card is NOT approved by that word; 7/16 NO-ADD; root rule #5.** **Expiry 9/30 = 6 days; harvest/roll is TERRY's.** *Posture, never a direction.*
- **HYG puts — closed at the INDEX level** (HY 273). CCC tail 7bp from 1100 → if it arms: single-name/CCC, **never HYG**.
- **Credit-equity lead — inactive.**

---

## Exit / Falsification *(full set → `thesis/THESIS.md`)*

**1 · THESIS KILL (exit all duration shorts).** WQ-157 leg ① (Will 9/4): **`I'` + a NON-AUCTION mechanism confirmation (FR2004 dealer stock and/or SOFR−IORB)** since 9/11. **9/23 5Y: `I'` fired; SOFR−IORB −3bp ⇒ funding leg UNMET (LIQUID 9/24 21:3x: NONE on every observable held — distribution width, SOFR99, SRF, TGCR; `KB-BND-330`; next real test = the 9/30 quarter-end settlement of ~$183B); FR2004 POST for the 9/23 5Y = **the 9/23 as-of, ~Thu 10/1** (trade-date window; the award is in that Wednesday's print — `KB-BND-332`; as-shipped join convention = 9/30, ~10/8) ⇒ KILL NOT FIRED, dealer leg UNEVALUABLE until 10/1.** **9/15 20Y-R pairing graded 9/24 on the 9/16 as-of: TOTAL legs NOT met, 11–21Y leg met — ADMISSIBLE (settlement question resolved 9/25; the award is in the print).** Unpaired `I'` fires: 9/15 20Y-R · 9/23 5Y · 9/24 7Y. **WQ-157 leg ② still with Will** — ⚠️ **its main evidence is CORRECTED 9/25: the "pairing INVERTS, p=0.009" result used a window that puts Wednesday awards inside PRE; on the trade-date window the headline leg is −4.5bp, p=0.248 (not significant); direction (paired fires not followed by rising yields) survives on TOTAL and 11–21Y legs** (`KB-BND-332`; `fr2004_join.py` NOT changed — fix registered as **WQ-290** (PROME rec YES), ⛔ untouched until Will rules). Funding leg p=0.523; MDE ≈16bp; BOND recommends nothing. Also: 10Y back below 4.15 ×3 with clean auctions ⇒ spent.
- ⚠️ `I'` bars: `monitors/AUCTION_HEALTH.md` §GRADING BASIS. **Grader defect `KB-BND-314` FIXED 9/24 (`71963a7b7`, `grade_auction.cycle_term()`): cross-cycle reopenings now keyed to their cycle; blast radius exactly 2 rows (Jan-26 `91282CGH8`, Feb-25 `91282CGQ8`); no verdict changed.** ⚠️ The 9/2 per-tenor base-rating and the WQ-157 join used the pre-fix pools — not re-run; disclose if re-cited.
- 🔴 Direction disclosed: `I'` is the easier test and its firing confirms this desk's own bear thesis.

**2 · POSITION-SPECIFIC.** TLT puts: kill on 10Y <4.15 AND 30Y <5.0 ×3 sessions AND a clean refunding (THESIS §2). Expiry 9/30 is TERRY's rail.

**3 · CONVERGENCE DOWNGRADE (trim).** Three CONSECUTIVE nominal coupons passing both legs (indirect ≥ median AND dealer ≤ median). **Counter 0** (2Y failed the dealer leg 13.19 vs 11.33; 5Y and 7Y failed indirect). Next eligible: 10/6 3Y.

**4 · TIME-BASED.** H.15 9/23 cells (row 1) **9/25** · quarter-end + PCE + `BND-27` + expiry **9/30** · F2 reads **9/24 · 10/1 · 10/8 · 10/15 · 10/27 · 11/4** · quarterly `I'` refresh + `VX-19` definition **10/1** (F2 vintage fix ✅ DONE 9/24, `KB-BND-328`) · `VX-20` **10/6** · FHLB Q3 **11/9** · FRBNY FX **11/13** · US-sov-CDS re-test **12/1**.

⚠️ **RETIRED, NOT REVIVABLE: the auction TAIL.** The 9/23 "2nd biggest tail ever" wire claim is `[med-conf]` and fires nothing.

---

## Immediate Catalysts *(source of truth `docket/CATALYSTS.tsv`; human twin — same event SET)*

| Date | Catalyst | What BOND watches |
|---|---|---|
| ✅ **Thu 9/24 1:40 PM — READ & ROUTED** | **20Y–30Y buyback op: $4.078B of $6B cap (68%) on 1.74× offered; recent_share 0.02% ⇒ OFF-THE-RUN** | Packet → RED 9/24 ~14:1x; ledger row; `KB-BND-324`. Complete at read (35/35) |
| ✅ 9/22 · 9/23 · 9/24 | 2Y 🟢 · **5Y 🔴 OLD composition failure** · 7Y 🟠 `I'` by 0.04pp | Graded 9/24 (`KB-BND-312/313`) |
| ✅ **9/23 official curve (Treasury) — DGS30 5.40 > 5.37** | Row 1 letter FIRED ⇒ 4 | ✅ **DONE 9/24 21:37 ET — FRED carries DGS30 5.40 / DFII10 2.76 [9/23]; identity held** |
| **Wed 9/30** | 🔴 **Quarter-end · Aug PCE + Q2 GDP 3rd (8:30) · `BND-27` window closes · TLT 77P expiry** | PCE vs the PMI input-price shock; SOFR−IORB across quarter-end; CCC vs 1100 |
| **Thu 10/1** | Quarterly `I'` refresh · `VX-19` "disorderly" · **10Y–20Y buyback op (F2, vintage rank live 9/24)** · Oct refunding sizes | `AUCTION_HEALTH.md` §3d; TIPS-`I'` question + degenerate-row guard (PROME DOCKET L410) |
| **Fri 10/2** | Sept Employment Situation (8:30) | 2Y / 1y1y reaction |
| **10/6 · 10/7 · 10/8** | 3Y · 10Y-R · 30Y-R + 20–30Y op (F2) · `VX-20` review | bars frozen at the 10/1 announcement |
| **Wed 10/14 · 10/15** | Sept CPI (8:30) · 10–20Y op (F2) | breakevens on input-supported cells only |
| **10/21 · 10/22 · 10/26–29** | 20Y-R · 5Y TIPS · month-end cluster | bars at each announcement |
| **Wed 10/28 2:00 PM** | 🔴 **October FOMC** (~70% hike priced, TE secondary) · ECB 10/29 | register a curve-shape row by 10/21 |
| **10/27 · 11/4** | 20–30Y op · **QRA + 10–20Y op (F1/F3 resolve; sb0607 window ends)** | carrier + `VX-BND-16` |
| **11/9 · 11/13 · 12/1 · 2027-01-25** | FHLB Q3 · FRBNY FX · US-sov-CDS re-test · Norwegian MoF expert group | as docketed |
| **— STANDING —** | MOF FX intervention · Warsh task force · FR2004 weekly · credit weekly · F2 carrier every boot | `FL-BND-11` · `VX-04` · `VX-02/11` · `VX-16` |

---

## BOTTOM LINE

**[2026-09-24 Thu ~13:3x ET — boot after a six-day gap; markets open.]**

**The auction side just produced this desk's hardest test since the thesis was written.** The 9/23 5Y failed the strict two-part composition test: foreign-type buyers took their smallest 5Y share since March 2020 while dealers took the most in a year. That meets the pre-set condition for adding to the TLT puts. **Will declined the add at 13:17 ET (WQ-280); no trade.** The caveats that decide it: funding stayed calm (−3bp), dealers were not stuffed by any multi-year standard (they took more five times in 2023–24), and the print cleared on the day hot PMIs sold the whole curve off. **Threshold fired; mechanism not shown failed.** **And the long end broke out the same day: official 30Y 5.40 (highest since 2004), 10Y 5.11 (since 2007), and the 10Y real yield 2.76 — highest since November 2008, +13bp in one session, real-led.** That fires the long-end vector's registered upgrade. The rate path is also still repricing up: this desk's 9/14 view that the hawkish path was fully priced was **wrong** (`BND-26`). **[Added 9/24 ~16:3x ET]** The weekly dealer-inventory print (as-of 9/16) did not show dealers stuck with long bonds after the 9/15 20-year auction: long-end holdings fell $1.8B, though the 11–21 year bucket rose $1.7B. **[Resolved 9/25 ~01:3x ET] The timing caveat is closed: the Fed's reporting instructions count an auction award from the day it is won, so this snapshot does include the 20-year award. The same check found that the older statistical evidence on WQ-157 was measured on the wrong week for Wednesday auctions; corrected, its headline result is no longer significant (`KB-BND-332`).** Under the ACM model the post-FOMC rise in the 10Y is expected policy path, not term premium (`KB-BND-325`).

**[Added 9/24 ~21:5x ET, post-close]** **The sell-off extended on 9/24 and stayed real-led.** Official 30Y 5.47 (highest since mid-2004), 10Y 5.18, 5Y above 5% for the first time since 2007, and the 10Y real yield 2.85, a level only ever seen in the 2008 crisis. Inflation expectations actually eased (T5YIFR 2.33), so this is the market charging more for real money, not pricing inflation. Rates volatility confirmed it was not a one-day shock: MOVE 104.58, up a third in two days. **The auction-failure reading is unchanged: LIQUID found no funding stress behind the 9/23 5Y on any gauge they hold. The real test of that is 9/30, when ~$183B of new notes settle on quarter-end.** No score change, no trade.

**Position: TLT 77P ×20 HOLD, no add, `$0`, expiry 9/30 (TLT 79.42, strike 3.0% below). Composite 14/35 (▲2). Counter 0. OPEN predictions 1.**
