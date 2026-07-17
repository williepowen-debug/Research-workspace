## 2026-07-17 — To: PROME (Fri COT session, PHASE 1 = PRE-PRINT prep)

**Signal:** 🟡 Pre-registered verdict map + branch read-throughs for today's CFTC JPY COT (Jul-14 data, ~3:30 PM ET) — the FIRST positioning print covering the post-Hormuz-closure week. Graded mechanically at Phase 2. FLAT stands; any position implication = proposal to Will (rule #4/#5).
**As of:** Fri 2026-07-17 ~1:00 PM ET · live marks below

---

### 0. STATE (verified this session)
- **CFTC primary reachable, baseline confirmed:** `publicreporting.cftc.gov/resource/6dca-aqww.json` (JAPANESE YEN — CME) shows **latest = report-date 2026-07-07, net −123,778, 68.8% of the −180K Jul-2024 peak** (long 112,247 / short 236,025 / OI 398,103). **Jul-14 print NOT yet up** (expected — release ~3:30 PM). Will re-pull + verify report-date = 7/14 at Phase 2; if it still shows Jul-7, the print is delayed → I say so and wait, no grade on stale data.
- **Live marks (fetch.py ~12:58 ET):** USD/JPY **162.41** (+0.21%) · FXY $56.46 · Brent **$87.37 (+3.73%)** · DXY 100.75 · EUR/JPY 185.78 (−0.05%) / GBP/JPY 218.56 (−0.38%) / AUD/JPY 113.43 (−0.10%). **Nuance vs recent sessions:** yen is weak vs USD but *firm* vs EUR/GBP/AUD today → this is **USD-side strength**, not the pure yen-weakness of 7/16. Brent +3.7% on the six-night campaign + Bab el-Mandeb conditional (risk-premium, no barrel lost — see §4).

### 1. FROZEN / PRE-REGISTERED COT LINES (quoted verbatim)
The rebuild direction had **no OPEN carrier** (SAM-30 was Jul-31-timeframed and RESOLVED CONFIRMED on the Jun-30 print). I've pre-registered **SAM-37** now, before the print, anchoring to the three standing frozen thresholds:

> **SAM-30** (RESOLVED CONFIRMED 7/10): *"CFTC JPY net short builds through **−153K (85% of cycle peak)**"* — the **RE-FIRE / escalation line**. Registered consequence on a cross: amplifier +5pp → **+8-10pp**, convexity-tail **MEDIUM → MED-HIGH**.

> **SAM-36 / Will's 7/10 AM resolver** (RESOLVED FALSE/DE-LOAD): *"net ≤−153K/85% = CONFIRM/enter · net **≥−140K = DE-LOAD**/no-entry · between = NOT-CONFIRMED."* The **−140K** DE-LOAD boundary. (Note: that resolver was **Jul-7-print-specific**; it does not auto-carry to a Jul-14 entry — a fresh re-fire is a NEW decision to Will.)

> **SAM-29** (OPEN, 65%): *"CFTC JPY net short does NOT **cover below −108K (60% of cycle peak)** before Sep 18 2026"* — the **cover-tail / frame-invalidation line**. A cover through −108K → convexity frame **INVALIDATED → LOW**. Currently only **~15.8K away**.

**SAM-37 verdict map for the Jul-14 net** (sign: net short negative; *cover* = toward 0, *rebuild* = more negative; base −123,778/68.8%):

| Band | Jul-14 net | % peak | Verdict |
|---|---|---|---|
| **1** | ≤ −153,000 | ≥85% | **RE-FIRE** — SAM-30 line reclaimed |
| **2** | −140,000 to −153,000 | 77.8–85% | **REBUILD-partial** — NOT-CONFIRMED (between DE-LOAD & CONFIRM) |
| **3** | −124,000 to −140,000 | 68.8–77.8% | **STALL** (modal) |
| **4** | −108,000 to −124,000 | 60–68.8% | **COVERING-CONTINUES** |
| **5** | > −108,000 | <60% | **SAM-29 COVER-TAIL FIRES** — frame INVALIDATED |

**Modal lean: STALL-to-mild-rebuild (band 3), ~55%.** Rationale: the weak-yen tape (fresh 40-yr low 162.84 intraweek) argues against continued heavy covering, but a full re-fire (+29.2K in one week = the largest build in the tracked series) is low-prob. Discount for calibration: my directional CFTC calls have a documented miss history (SAM-22), so I hold the modal at 55%, not higher, and let the map grade mechanically.

### 2. CLOSURE-WEEK WRINKLE — how I discriminate IN ADVANCE
The report week (Wed 7/8 → Tue 7/14) spans the **formal Hormuz closure (7/11-12)**, the **oil spike (Brent $76 → $87)**, and **strike nights 1-4**. Two forces push the JPY series **opposite** ways:
- **Safe-haven JPY bid** → shows as short-**covering** or fresh longs (net toward flat). **BUT** the cross-pair yen-haven channel has been **DECOUPLED since Jun-11** (risk-off routes to USD-haven, not JPY) → this force is **muted**.
- **Oil-driven Phase-1 yen weakness + carry reload** → fresh **shorts** (net more negative / rebuild). Japan ~90% ME-oil-dependent → the oil spike is a terms-of-trade hit = yen-NEGATIVE near-term.

**Tie-breaker = the tape.** USD/JPY made a fresh 40-yr low **162.84** intraweek and closed ~162.24-162.41, yen weakest-vs-USD → **inconsistent with a haven-JPY-bid dominating** → my prior leans **STALL/rebuild, not cover.**

**IF the print shows heavy covering despite the weak-yen tape** (the surprise case), I decompose **OI + the longs/shorts split** to tell which story:
- **OI DOWN, both legs falling** = gross **de-risking** into war uncertainty (NOT a directional haven bid) — the same signature as the 7/7 cover (conviction-dent from the firm 30Y auction + PPI/yield stack). Reads dovish-for-the-frame but not a SAM-31 event.
- **Longs UP materially** = **fresh haven demand** = the decoupled channel **re-coupling** → **SAM-31 re-couple candidate**, 🔴 escalate to HENRY (restores the joint risk-off route → MED-HIGH reclaim path).

### 3. BRANCH READ-THROUGHS (pre-stated, per verdict)

**(a) TRY-FIRE-005 shelf** (FXY Aug-21 58C×6 + 59C×20, BUILT/SHELVED — Aug-21 expiry still ~5wks out, viable):
| Verdict | TRY-FIRE-005 |
|---|---|
| RE-FIRE (≤−153K) | **Re-fire CANDIDATE** — the registered entry-gate (CFTC through −153K/85%) is met again. NOT auto: SAM-36's DE-LOAD resolver was Jul-7-specific → a fresh entry is a NEW proposal to Will via PROME; TERRY re-checks the ladder/marks. |
| REBUILD-partial (−140/−153K) | **Stays SHELVED** — NOT-CONFIRMED; re-arm watch only. |
| STALL (−124/−140K) | **Stays SHELVED** — no gate condition met (modal). |
| COVERING (−108/−124K) | **Stays SHELVED**, conviction eroding. |
| COVER-TAIL (>−108K) | **RETIRE** — convexity frame invalidated (SAM-29 FALSE); the shelf is no longer a live construct at LOW. |

**(b) Carry-unwind buckets** (current 7d ~5 / 30d ~18 / 60d ~27; CFTC amplifier anchor = +5pp @68.8%). Per the four-anchor re-pencil discipline (Jun-14 rule), I move buckets on a **registered-line cross only**; between lines I note drift but don't full-re-pencil:
| Verdict | Buckets |
|---|---|
| RE-FIRE (≤−153K) | Single-anchor amplifier step +5→+8-10pp → **~7-8 / 22-24 / 30-32** (echoes the 7/10 AM MED-HIGH step ~8-10/20-24/27-31). |
| REBUILD-partial | Amplifier drifts +6-8pp → nudge **~6 / 20 / 29** (noted, not a full re-pencil). |
| STALL | **Unchanged 5 / 18 / 27** — amplifier +5pp holds. |
| COVERING | Amplifier +5→+3pp → ease **~4 / 16 / 25**. |
| COVER-TAIL | Amplifier OFF, frame LOW → floor **~3 / 14 / 22**. |

**(c) USDJPY band + >167 disorder tail** (modal FXY $55.3-57.7 / USDJPY **159-166**; >167 = disorder tail, **NO guaranteed MOF floor** — ambush regime, S1-A). The COT is the **positioning-convexity fuel gauge** (Ch4) — it sets *how violent* an unwind would be IF triggered, not *whether* USD/JPY breaks 167:
- **RE-FIRE/REBUILD** = more short fuel → a sharper potential reverse-carry-squeeze if a MOF-ambush or the >167 break fires; band holds 159-166, >167 tail stays live with more energy behind it.
- **STALL** = band + tail unchanged.
- **COVERING/COVER-TAIL** = less fuel → the >167 tail becomes more of a pure-momentum (not positioning-driven) risk; the convexity *payoff* thins even if the price path is unchanged.
Price-level band is not moved by the COT directly; this is a second-order (fuel) read.

### 4. OIL-LEG DURABILITY CAVEAT (from the WALTER 4-file drain — folds into the re-pencil, no bucket change pre-print)
All four WALTER signals (SIG-002/004/013/018) converge: the $76→$87 oil move is **RISK-PREMIUM, not supply-loss** — FAL-01 (production/refining/export infra) has **NOT fired**, zero barrels offline; Iraq resumed loadings same-day, Russian Black Sea loadings *rose* 68% MoM. **A premium-driven oil-yen channel is materially MORE REVERSIBLE than a supply-loss one** → this **softens the durability of my 60d oil-tail uplift (~10-11%)** in the 4-anchor re-pencil. No bucket change now (no barrel lost, USD/JPY still 162+), but it's the key durability watch. **Conversion trigger** (would harden the leg from reversible→durable): if the **shuttle-fleet bypass breaks** (SIG-013 — WSJ: Iran attacking Fujairah/Sohar STS runs; no volume decline *yet*) OR the **Bab el-Mandeb second-chokepoint conditional** executes (SIG-004). BRENT owns the sustain verdict.

### 5. TIC + MOF RECONCILIATION (one paragraph — different months, different instruments, no weld)
**May TIC** (rel 7/14, PROME-graded): Japan LT USTs −$2.8B + **bills −$59.8B = −$66.8B, ~94% REAL selling** — a genuine seller across the curve-front, ARM-3 fired weak. **MOF weekly wk-7/5–7/11:** **+¥1,090.1B foreign-LT-debt net BUYING** (>2× the ≥+¥500B durable bar). These are **not the same object**: TIC = US-Treasury holdings specifically (May); MOF weekly = foreign LT debt *globally*, not USTs-specific (July). The consistent sequencing: Japan de-risked/sold **front-end USTs in May** (bills-heavy = liquidity/FX-reserve management, pre-event), then **rotated to net foreign-LT-debt buying by mid-July** at the 40-yr-weak yen. Per PROME's grade, the July flip reads as a **TRUE REVERSAL** (May-sell → July-buy), which **strengthens the DURABLE verdict** on the 7/9 BND-11 read — I am *not* welding the July MOF buying onto UST buying (wrong instrument) nor onto the May bill selling (front-end ≠ LT). Net cross-relevance to LIQUID/BOND: reinforces **Channel-1 RETIRED** — Japan = net foreign buyer deploying abroad, **not** a repatriation-seller. Held at **MEDIUM** for the foreign-LT-debt-≠-USTs caveat + single-week; **next weekly ~7/23 JST = the standing stake.**

### 6. PHASE 2 PLAN (at/after ~3:30 PM ET)
Pull CFTC public API (JPY-CME, sort report_date desc) → **verify report-date = 7/14** (if not, delayed → wait, no grade) → record net / longs / shorts / OI / %peak to `workbook/CFTC_JPY.tsv` → grade mechanically vs the SAM-37 map above → apply the branch read-throughs → update THESIS version only if a registered line is crossed → memo + STATUS + SendMessage back. My own poll is primary; PROME holds a 3:31 nudge as backstop.

— SAM
