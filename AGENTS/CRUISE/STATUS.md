# CRUISE — STATUS

*Last updated: **2026-10-29 00:0x ET** — session closed out at Will's request: RCL Q3 graded (L713 RESOLVED), file sweep, PROME six-item answers acted on, WQ-532 A received (encodes after the NCLH read). Session left open for two scheduled one-shot jobs: NCLH grade 06:47 ET, 10-Q pickup + WQ-532 encoding 11:13 ET; if the session ends first, the next CRUISE boot runs both from CADENCE row 1b and the inbox packet.*

## October 28 — Boot catch-up

| Item | Result | Consequence / limit |
|---|---|---|
| **RCL Q3 FY26 graded** (L713, one day late; carrier SIG-W-20261029-009) | Adj EPS **$6.57** vs $6.26–6.36 guide (ABOVE) · Q3 CC net yield **+0.6%** vs ~flat · FY26 CC yield guide **~+2.1%** vs +1.75–2.25% (RAISED +0.10pp) · FY adj EPS **$17.85–17.95** (RAISED +$0.10) · 2027 "pacing ahead … at higher rates" (STRONGER) · Q3 fuel **$347M** vs $362M (BELOW) | Premium leg firm. **Exit rule 1 limb 2 NOT FIRED.** `VX-CRU-03` evidence only, re-score after NCLH. Grades in `WATCHLIST_RCL_Q3.md` § Additions; KB-CRU-203/204 [CONF A1 8-K 10/27] |
| **RCL ladder at 9/30** | (cash $851M + undrawn revolver ~$6.6B) / total debt incl leases $22,872M = **32.58%** (June 29.37%). October: +$400M EDC delayed-draw loan, revolver to $6.65B | Undrawn input rounded (±~0.2pp). NCLH side owed from its 10/29 filing. KB-CRU-205 [CONF A1 10-Q] |
| **CCL tape** | 10/27 $27.74 and 10/28 **$28.06** closed above the $27.192 line ⇒ **`VX-CRU-01` ORANGE(3) → YELLOW(2)** on the letter | Price-only; no CCL-specific cause checked. Convergence 15 → **14/25**. KB-CRU-206 |
| **PROME 10/25 final-two fixes** | VX-CRU-04 Source path repaired (target exists); dashboard Gulf zero-count annotated superseded | Packet closed; DOCKET L815 tombstoned 10/28 (WQ-530 A). KB-CRU-207 |

**File sweep 10/28:** 39 KB rows still marked ACTIVE past their Stale_By re-labelled (35 STALE, 4 SUPERSEDED by KB-CRU-204/206); one broken VX path fixed; `OPERATORS.md`, `TRADE.md`, `inbox/RECEIPT.md` brought to 10/28; `domain/CRUISE_TERM_SET.md` bannered as landed. Decision-level residuals listed under Key gaps.

**So what:** RCL's print is the second Big-3 beat-and-raise (after CCL 9/29), so the "broad cruise-consumer stress" reading keeps losing ground; the open question is still NCLH-specific, and its Q3 lands **Thu 10/29 06:30 ET** (`WATCHLIST_NCLH_Q3.md`). October 25 session sections → `domain/sources/STATUS_archive_2026-10-28.md`.

## Signal Dashboard

*Big 3 prices are **October 28 closes**, retrieved October 28 23:4x ET with repository yfinance(auto_adjust=False) and FORGE fetch.py (same vendor). The separate CRU11 interim remains **October 19**, unchanged and ungraded. Other rows retain named vintages.*

| Metric | Value | State | Source |
|--------|-------|-------|--------|
| **CCL price** | **$28.06**, October 28 raw close (+1.15%); **−17.45%** versus fixed raw February 6 reference $33.99. Above YELLOW line $27.192 since 10/27; RED $22.0935 | 🟡 | Yahoo yfinance + FORGE, retrieved October 28; KB-CRU-206 |
| **RCL price** | **$298.30**, October 28 raw close (+0.80%); **+5.46% on 10/27** (print day) | 🟢 | Same-vendor sources; KB-CRU-206 |
| **NCLH price** | **$16.06**, October 28 raw close (+1.97%); **−35.81%** versus held raw February 26 peak $25.02. Q3 release **10/29 06:30 ET** | 🔴 | Same-vendor sources; KB-CRU-206 |
| **RCL Q3 / FY26** | Adj EPS **$6.57** vs $6.26–6.36 · Q3 CC yield **+0.6%** · FY CC yield guide **~+2.1%** (was 1.75–2.25%) · FY adj EPS **$17.85–17.95** (was 17.73–17.87) · occupancy 112.4% on capacity +8.4% · 2027 "ahead of historical levels at higher rates" | 🟢 | [CONF A1] 8-K …-000042 Ex-99.1, 10/27 |
| **CRU-11 spread** (NCLH − RCL cumulative adjusted TR from October 2) | **−0.86pp at October 19 close**, **interim observation only**. Frozen endpoint November 14 / nearest preceding session; resolver not run | 🟡 | [CONF MIRROR] pinned yfinance Adj Close pull October 19 |
| Tape 10/14 | Big-3 −2.6% to −2.9% on a down day: SPY −1.08%, XLY −0.77%, VIX 16.87 (+10.5%). **No cruise-specific cause found** | — | [CONF] yfinance 10/14 |
| **CCL Q3 / FY26** | Adj EPS **$1.43** vs ~$1.35 guide · FY CC net yield **~+2.3%** (was ~+1.75%) · FY adj EPS ~$2.24 · deposits **$7.6B, +~7%** on flat capacity · 2027 occupancy + pricing **at records**. ⚠️ 10-Q: **North America ticket prices −$40M YoY**, cause unnamed — not CRU-09 evidence, not the Norwegian channel | 🟢 | [CONF A1] 8-K …-000104 + 10-Q …-000107 |
| **CCL fuel** (`VX-CRU-02`) | Q3 actual **$826/mt** vs $812 guide; fuel hit **$0.007/sh**; **Q4 guide $896/mt**; FY raised through a ~$150M fuel headwind. **Exit rule 2 FIRED** ⇒ cost line only. Brent BZZ26 ~$105.3 (bar labelled 10/14, may include the evening session — context; **BRENT owns it**) | 🟡 | [CONF A1] CCL 9/29; yfinance BZZ26.NYM |
| **NCLH Q3 + funding** | 9/30 8-K: Q3 to **beat on revenue**; FY26 **REAFFIRMED, not raised**; **2027 net interest $860-880M vs FY26 ~$705M (+22-25%)**. **$950M 8.750% notes due 2031** priced 9/30, **closed 10/15**, unsecured (KB-CRU-157); nominal room +691.3M (KB-CRU-162) | 🔴 | [CONF A1] 8-K …-112116; Q2 Ex-99.1 …-005050; NCLH IR #827/#828 |
| **RCL capital** | 9/30 liquidity **$7.4B** (cash $851M + undrawn revolver $6.6B); ladder **32.58%** (June 29.37%). October: **$400M EDC delayed-draw loan**, revolver to $6.65B. **Sandals ~$3B still prospective** (close early 2027) | 🟢 | [CONF A1] 10-Q …-000044; 8-K …-000042; KB-CRU-205 |
| **Capital-access ladder** | **RCL 9/30: 32.58%** (KB-CRU-205). **June 30 cash+general-revolver / gross principal incl leases: NCLH ~9.81% · RCL 29.37%**; NCLH 9/30 owed 10/29. Prior 10.0%/30.2% used carrying debt. Transaction-only October 19 bridge preserves ranking; actual September/October liquidity unknown. CCL 26.2% uses May 31 and is not a same-date peer. Sandals borrowing is prospective; shelf capacity is not issuance | 🟠 | [CONF A1] Q2 10-Qs; KB-CRU-152 |
| Caribbean discounting / `FL-CRU-10` | Broad NCL promotion **including** the Caribbean confirmed (7/8); **concentration unmeasured**; contagion limb **UNRESOLVED**. CRU-09 **FAILED**: CCL blamed **capacity** (~37% industry growth over 3 years), named no competitor | 🟠 | [CONF A1] ncl.com; KB-CRU-144 |
| Capacity vs occupancy | Q2 FY26 YoY: **NCLH +8.88% / −1.54pp · RCL +4.87% / −0.08pp · CCL +2.07% / flat.** Q3 10-Qs for RCL/NCLH not yet filed | 🟠 | [CONF A1] Q2 10-Qs |
| Credit ratings | CCL investment grade (S&P BBB− 6/25, Fitch); NCLH B1 / B+. **Not re-swept 10/14** | 🟢 | [CONF C2] carried |
| Consumer (CARL) · Gulf (FALCON) | **Headline-only re-read 10/28:** CARL STATUS 10/28 = 🔴 CRITICAL under its registered score, evidence mixed; its 10/12 scope finding says broad spending collapse is *not* established. FALCON last swept 10/26; its scenario marks were **not** re-read. Older owner marks: CARL 9/17 53/70 🔴; FALCON 9/28 B1/C14/D85. ⛔ The 9/28-era "zero Big-3 cancellations" count is **SUPERSEDED** by the October 25 recovery of the NCL Sky 9/9 itinerary cancellation — current Gulf transmission read is **`VX-CRU-04` YELLOW(2)**, not this row; no fresh FALCON/CARL research claimed | ⚪ | carried; KB-CRU-200 |
| Hurricane Isaias | Cat 2 landfall near **Destin (Panhandle) 10/9**. **Cruise effect NEGLIGIBLE** (checked 10/14): only Carnival changed anything — Dream's Galveston boarding ~2h late (10/10), Liberty and Valor shifted Cozumel call times. **No cancellations, no skipped ports, no RCL/NCLH changes found.** Tampa, Galveston, New Orleans open; Mobile closed 10/9, normal 10/10, no cruise that week. ⚠️ Secondary trade press only | 🟢 | [CONF C2] CruiseHive 10/10 · KB-CRU-153 |
| WALTER lane | **1 cruise signal delivered in the L452 window** (SIG-W-20261001-028, acted). Collector carried ≥6 decision-relevant | 🟠 | KB-CRU-149 |

---

## Convergence Matrix

| # | Target/Vector | Score | Status | Key Signal | Upgrade Trigger |
|---|--------------|-------|--------|------------|-----------------|
| 1 | NCLH relative weakness (`VX-CRU-05`) | 4 | 🔴 | 7/30 guide cut stands (9/30 = reaffirm, **not** a re-slash); −39.65% from held peak at October 23 close; **new 8.750% paper replaces 6.125%** and 2027 interest +22-25% — access demonstrated; nominal room +$691.3M is not cash | NCLH Q3 print guides down · FY26 OCF below ~$1,926M · advance-ticket build falls again · leverage climbs off 5.3x |
| 2 | Consumer demand K-shape (`VX-CRU-03`) | 4 | 🔴 | **On the letter** (NCLH's guide-down not reversed). ⚠️ **Q3 evidence is non-escalating**: CCL records 9/29, **RCL beat-and-raise 10/27** (FY CC yield ~+2.1%), NCLH **expected** Q3 above guide on revenue. Dispersion fits; broad consumer stress does not. **Re-score owed after NCLH 10/29** | −20% booking-pace print · RCL guides FY yields DOWN |
| 3 | CCL stock stress (`VX-CRU-01`) | 2 | 🟡 | October 28 **−17.45%** on fixed raw basis; **ORANGE → YELLOW 10/27** (close above $27.192). Signed band-cell ambiguity remains open | Close ≤ $27.192 → ORANGE; ≤ $22.0935 → RED; no new inclusivity |
| 4 | Fuel cost line (`VX-CRU-02`) | 2 | 🟡 | **Exit rule 2 FIRED.** Level band still RED ($826 actual, $896 Q4 guide) — **the channel is dead, the cost is not** | A print where the fuel-attributable hit vs guide > $0.10 **with** a yield guide-down |
| 5 | Gulf/Red Sea → Big 3 (`VX-CRU-04`) | 2 | 🟡 | **One identified NCL Sky itinerary**, cancellation reported August 5, detected October 25; operator guest statement read through trade press (B2); total-basket completeness/denominator unmeasured | Existing1–5 band; one cancellation trigger FIRED |

**Summary: 14/25 across five vectors** (10/28: `VX-CRU-01` −1 on price; was 15/25 on 10/25) (was 14/25 before the recovered Sky cancellation) (was ~19/30 across six on 9/20). ⛔ **The fall is two rule outcomes, not a calmer world**: `VX-CRU-02` −2 because exit rule 2 fired on the print, and `VX-CRU-06` (3) **retired**. October 25 adds one point for the recovered Big 3 itinerary transmission; this is a delayed historical trigger. The other elevated vectors remain **NCLH-specific and dispersion**; no sector-demand or financing-causality verdict follows.

---

## Exit rules (falsification) — live copy, verdicts dated 2026-10-14

1. **K-shape kill (`VX-CRU-03`):** NCLH raises its guide at Q3, **or** CCL and RCL both guide FY yields DOWN. **NOT FIRED.** Limb 1 **open** until NCLH's own Q3 print (9/30 reaffirm ≠ raise). Limb 2 **NOT FIRED 10/27**: CCL raised 9/29 and **RCL raised 10/27** (FY CC yield ~+2.1%, KB-CRU-204). ⛔ The old yield-level confirm/refute rule stays **SUPERSEDED**; the `FL-CRU-10` identifying test was **registered as CRU-09/CRU-10 and graded 10/3** (draft archived 10/28 → `archive/2026-09-19_DRAFT_FL-CRU-10_identifying_test.md`); its unmeasured limbs (Caribbean concentration, Carnival-side attribution) stay caveats on `FL-CRU-10`, not a test. An aggregate yield number adjudicates nothing.
2. **Fuel-channel kill (`VX-CRU-02`):** CCL Q3 fuel/mt ≤ $812, **or** above it with a fuel-attributable EPS hit ≤ $0.10. **FIRED 2026-09-29** on the second disjunct ($826; $0.007). **Applied 10/14:** score 4 → 2; only the cost line survives.
3. **Sector-vs-name kill (`VX-CRU-06`, WQ-222, total-return basis, Will-ruled):** CCL excess drawdown over RCL ≤ 5pp on every close from 9/03 through the print. **CONDITION HELD** — max **1.8387pp** (9/10); at the 9/29 close CCL **+6.94%** vs RCL **−1.25%**. ⇒ **no CCL-specific fuel trade, only a sector view.** With `CRU-08` CONFIRMED, the **WQ-164 retirement of the fuel ladder survives both of its registered falsifiers.** `VX-CRU-06` retired.
4. **Time-based:** the 9/29 CCL print **DONE** (CRU-07/08/10 ✅, CRU-09 ❌ 10/3). RCL Q3 **DONE 10/28** (graded one day late). Next mandatory checks: **NCLH Q3 10/29 · CRU-11 grade 11/14 · NCLH revolver springing test 11/17.**

---

## Predictions

**Only `CRU-11` is open** — NCLH under RCL by ≥ 5pp cumulative TR from the 10/2 close at the 11/14 close, 50%, **approved WQ-242**, frozen (PREDICTIONS line 12). Ten rows graded: CRU-01/04/06/07/08/10 CONFIRMED · CRU-02/03/05/09 FAILED.

## Fuel ladder

🔻 The 7/2 *"Brent > $85-90 = arm CCL"* ladder is **RETIRED (Will 2026-09-03, WQ-164) — kill-on-sight as a live trigger.** Both registered falsifiers of that retirement have now resolved **in its favour** (exit rule 3 above; CRU-08). This desk sets no fuel level; any future trigger is a new registration through PROME.

---

## Cadence

**ACTIVE / EVENT-DRIVEN** (Will-ruled 8/21). Live wake set: **`CADENCE.md`**. **Nearest future:** ① NCLH Q3 **Thu 10/29 06:30 ET / call 08:30 ET** · ② **CRU-11 grade 11/14** · ③ NCLH springing test **11/17** · ④ FL port FY2026 passenger counts (Oct–Nov). RCL Q3 graded 10/28.

---

## Key gaps / owed

- 🟠 **Scope residue reconciled 10/25:** ROSTER row 109 now carries WQ-435 live scope (PROME refreshed 10/23). `_NETWORK.md` description and Gulf-feed reconciliation remain PENDING under **WQ-504 (due 10/30)**; DOCKET L815 was tombstoned 10/28 as a duplicate of that queue item (WQ-530 A). Leave the charter route sentence unchanged until PROME sends the ruling.
- 🔴 **Historical October 14 deliveries:** packets to **TERRY** (NCLH refinancing + Sandals; my 10/2 "fragility strengthens" corrected), **PROME** (L452 grade, exit-rule verdicts, `VX-CRU-06` retirement, corrections), **WALTER** (the routing fact behind L452 — a fact, not an instruction).
- ✅ **October 14 NCLH funding study is historical scenario work** → `domain/sources/2026-10-14_nclh-funding-position-after-the-930-refinancing.md`, KB-CRU-155/156. Its **~−14% to −16% annual OCF-decline breakeven incorporated the $376.3M revolver repayment but excludes the later $315M commitment increase**; it is not a current liquidity forecast. The completed October 19/25 reconciliation preserves access-versus-cost and nominal-versus-drawable distinctions; actual September/October cash and compliance remain unresolved. The November 17 test remains conditional on actual Free Liquidity; see `research/2026-10-25_catchup/RESULT.md`.
- ✅ **10/14 scope / catalyst proposal verified 10/25:** WQ-435 APPROVED and encoded; DOCKET L712 resolved, L713 dated 10/27, L714 re-dated 10/29, L715 dated 11/17; ROSTER refresh done. L714 description still says fallback/unannounced, but its disposition explicitly records the issuer-confirmed date (10/21). Remaining shared-topology work has its home at L815 / WQ-504.
- ✅ **NCLH Q3 reading guide ready** → `WATCHLIST_NCLH_Q3.md`: confirmed release **October 29, 2026 at 06:30 ET**, call **08:30 ET** (issuer October 15 announcement; KB-CRU-165). The October 25 financing note and `research/2026-10-25_ports/EARNINGS_READINESS.md` are linked; existing criteria and future result status are unchanged.
- 🟠 **Actual Q3 re-reads:** **RCL DONE 10/28** (KB-CRU-203..205). **NCLH 10/29 owed**: actual 9/30 cash/debt/deposits/availability, fresh guidance, then the joint `VX-CRU-03`/`VX-CRU-05` re-score.
- ✅ **PROME answered the six sweep residuals 10/28** (`inbox/processed/2026-10-28_from-PROME_six-open-items-answered.md`): ① FL-CRU-10 draft was already registered/graded as CRU-09/10 — my "unregistered" line was a stale self-claim; draft archived. ② `VX-CRU-02` fuel band = **Will's WQ-532** (due 11/6); row unchanged until his word arrives. ③a SF13 literal-inequality clarification owed **after NCLH** (C1 if no grade moves, else folds into WQ-532). ③b routing = WQ-504 (10/30), PROME's edit. ④ NCLH 2027 hedge coverage + Canada exposure (one bounded read, clean negative closes it) at the 10/29 grade. ⑤ ports: stop; PortMiami re-check ~12/1. ⑥ ladder memo archive on/after 11/9.
- ⏸ **`VX-CRU-02` re-spec — Will's call (WQ-532), do not change the row before his word:** a fuel-LEVEL band on a vector whose channel is dead keeps printing RED. Re-label as a cost observation or band it on fuel-to-EPS transmission — **not done**.
- ✅ **WATCH maintenance completed 10/25:** `TRADE.md` now reconciles the refinancing and contract conditions; old text preserved in `domain/sources/TRADE_archive_2026-10-25.md`. NCLH remains WATCH 3 / no card; CCL retired under WQ-427. Model refresh requires actual Q3 cash/debt/availability; no new endpoint estimate supplied.
- 🟠 **Remaining deferred items from October 2:** PROME September 22 NCLH asks (Canadian exposure, 2027 hedge coverage) · Med/Europe "reversal" (call-only) · no live fare series · `FL-CRU-10` caveats (Caribbean concentration unmeasured; Truist read through one wire story). **Port Canaveral board financial/statistical attachments were recovered October 25**; that item is complete, with source/period limits at `research/2026-10-25_ports/RESULT.md` (KB-CRU-190).
- ✅ **PROME answered all three asks 10/14 ~20:5x ET, each verified at the artifact by CRUISE:** ① **DOCKET L452 RESOLVED** on KB-CRU-149 (`46569038c`), not re-dated. ② **WQ-427 RULED 2026-10-14 21:01 ET — Will verbatim *"Approve 426 and 427"*** (record `PROME/proposals/2026-10-14_wq426-427-RULED.md`, `7c761f28b`): `TRADE.md` row 2 (CCL WATCH, WQ-218 ②) **RETIRED → Rejected / Exited**; row 1 (NCLH) untouched; no position involved. **Recorded here and in `TRADE.md` (root rule #10).** ③ **`WATCH_FOR["CRUISE"]` LANDED** — the seven 10/2 phrases, identical in the live lane (`~/Research-Intake` `4a16fb0`) and the FORGE mirror (`4518cacc6`); both configs load and agree.
- ⚪ **Not re-read this session:** CARL, FALCON, BRENT, HAWK surfaces; RCL/NCLH sell-side beyond headlines (Jefferies upgraded RCL 10/8 on 2027 yields; BNP cut NCLH's target $18 → $15 10/8; Citi $22 → $19 10/2 — **headline-level only**).
- ✅ Read-cap: October 25 rotations at `domain/sources/STATUS_archive_2026-10-25.md` and `STATUS_archive_2026-10-25_stale-sweep.md`; current measurement in Phase2 validation.

---

## BOTTOM LINE

Royal Caribbean beat its own Q3 numbers and raised its full-year guide on 10/27, the second big-operator beat-and-raise in a month, so the cruise data still shows a split between operators rather than a broad consumer pullback. Carnival's stock has recovered above its −20% line (YELLOW), Norwegian remains the weak name and reports Thursday 10/29 at 06:30 ET — that print decides whether the split-operator (K-shape) reading holds or dies. NCLH stays WATCH 3 with no trade card; no trade, threshold or forecast changed this session.
