# HANS STATUS.md
**Updated:** 2026-09-18 ~21:0x ET — **8-DAY CATCH-UP. THE BoE PIVOTED THE GILT LONG END, THE FED HIKED, AND ONE OF MY PUBLISHED MECHANISMS IS REFUTED BY IT.** Spawned by Will: *"catch up on recent events and news."* Every level below is re-pulled today or dated.
**Boot ack:** `boot.py` exit 1 · `doc_audit.py` **0 findings** before and after this session's edits · R1 corrections **rc=1 → receipted** · 9/10 blocks rotated. I own **`EUROPE_MACRO`** (BOND = time-critical backup). **UK leg: MINE.**

---

## 🔴 THE HEADLINE — BoE 9/17: THE BANK STOPPED SELLING LONG GILTS. READ AT PRIMARY 9/18.

**Bank Rate HELD at 3.75%** (MPC meeting ended 9/16) — and the rate is the *least* important half. **Primary: BoE Market Notice, 17 September 2026**, read in full.

| Leg | Figure | So what |
|---|---|---|
| APF gilt stock | **£488.2bn** (purchase-proceeds) | the denominator |
| Held to maturity, pre-2035 | **£222bn** | never sold |
| Held to maturity, **longest-dated** | **£120bn** — retained to indirectly back banknote issuance | 🔴 **the long end is withdrawn from sale permanently** |
| Under review, 2035–2049 | **£146bn** | the only bucket still in play |
| Active sales | **£20bn/yr**, unwind concluding ~2034 | a multi-year path to a zero monetary-policy stock |
| Auctions | **PAUSED** while the Bank reviews selling gilts *directly to the Government*; decision **by April 2027** | supply removed now, structure decided later |

**£222 + £120 + £146 = £488bn — the entire stock is now either held to maturity or under review.** ⚠️ **The £222bn pre-2035 figure is mine from primary and was NOT in WALTER's relay** (which carried the £120bn and £146bn legs) — the relay was accurate on what it carried; I read the notice because a relay is not a primary `[[finding_asymmetric_rigor_counterparty_claims]]`.

**Market response, and it is the right size but the wrong duration:** 30Y gilt **5.7415 (−12bp)** and 10Y **5.2169 (−8bp)** intraday 9/17 → but by **9/18 the 10Y was back to 5.29 (+6bp)**, giving back ~half the decision-day rally in one session. **30Y 5.75.**

⇒ **Both my UK thresholds moved AWAY from their bands and the near-trigger flags are DOWNGRADED:** `T-13` 30Y now **25bp** under the 6.00 orange (was **7bp** on 9/10, at a post-1998 high) · `T-06` 10Y now **21bp** under 5.50 (was 14bp). **Neither ever fired; there is no exit to record.**

🔴 **THE READ, AND IT IS NOT "UK STRESS HAS EASED": THIS IS A SUPPLY WITHDRAWAL, NOT A DEMAND RECOVERY.** The seller of last resort stopped adding paper to the long end; nothing changed about the fiscal position that put the 30Y at a 1998 high days earlier. **A yield that falls because the seller left is not a yield that fell because the bid returned** — the 9/18 give-back is the tell. **`11/26 UK Budget` unchanged as the LDI-adjacent date.** Chain: `FLOW-HANS-5 UK_Pension_Stress`.

---

## 🔴 THE FED HIKED 9/16 — AND IT REFUTES A MECHANISM I PUBLISHED ON 9/10

**FOMC 2026-09-16: +25bp to 3.75–4.00%, first hike since 2023, vote 12–0.** Warsh: inflation still too high. **16 of 18 participants expect another hike this year.**

**What I wrote on 9/10, verbatim from the rotated block:** *"Fed–ECB differential compresses further on a Sept ECB hike into a Fed on hold (Warsh hawkish-hold, per WALTER 8/28 cross-read) — that is the euro-strength mechanism already visible at 1.16."*

**Both halves failed.** The Fed did not hold, it hiked — so the differential did **not** compress, it is **unchanged at 137.5bp** (both legs +25bp). And the euro did not strengthen: **EUR/USD 1.1489 [9/18] vs 1.16 [9/5] — it WEAKENED.** ⇒ **Leg (2) of the term-premium exclusion argument now cuts the other way and must be RE-ARGUED, not restated.** → dispatched to BOND/TERRY; `KILL_TREE` C-1.

🔴 **AND THE NEAR-MISS THAT CAME WITH IT.** DAEDALUS PR6 (9/17) flagged `VX-HANS-4.03` as reading **137.5bp on a stale 2.25% ECB** and computed the true figure as **112.5** — correct on 9/17. But between their read and mine **the Fed hiked**, moving *both* legs +25bp and returning the differential to **exactly 137.5**. **Applying their ask mechanically would have written 112.5 — a wrong number — into an accidentally-correct row, and every structural check would have passed.** ⇒ **Recompute a derived row from BOTH legs at their own primaries; never accept a supplied delta, however well-sourced.** → `ML-HANS-450`

---

## 🔴 FRANCE — BOTH `T-10` LEGS NEAR-TRIGGER, AND THE GRADE WAS DECIDED INSIDE MY OWN BASIS GAP

**OAT–Bund is at a 1-YEAR HIGH.** Single-source daily series (ideal-investisseur, same screen for both legs):

| Date | OAT | Bund | Spread |
|---|---|---|---|
| Aug 31 | 4.11 | 3.31 | 80.4 |
| Sep 4 | 4.19 | 3.34 | 84.7 |
| Sep 11 | 4.41 | 3.51 | 89.8 |
| **Sep 16** | **4.52** | 3.56 | 95.6 |
| Sep 17 | 4.48 | 3.53 | 95.0 |
| **Sep 18** | **4.47** | **3.50** | **96.8** ← 1-yr high (1-yr low 59.0, avg 73.7) |

**`HANS-T-10` = spread >100bp AND OAT >4.50. VERDICT: NOT FIRED — 3.2bp and 3bp under, respectively.**

🔴 **BUT READ HOW CLOSE THIS WAS TO A FALSE FIRE.** Subtracting TradingEconomics from TradingEconomics for the same day gives **OAT 4.5735 − Bund 3.5187 = 105.5bp** — which clears **both** legs and would have been logged as a fire. **The two trip lines sit INSIDE my unresolved OAT basis gap, which has WIDENED from ~7bp [9/10] to ~10bp [9/18] and is still outside my declared ±5bp tolerance.** I graded on the **single-source spread quote** because *a spread must never be derived across two sources* — the same class as the `T-08` storage gap `[[finding_instrument_error_correlated_with_the_trigger_biases_the_gate]]`. **Open item #11 was registered on 9/10 for exactly this case and it paid for itself today.**

✅ **And the compound structure did its job:** on **9/16 the LEVEL leg alone was MET (OAT 4.52)** while the spread leg was not — a single-leg row would have fired on a day the fragmentation signal was absent.

**Fiscal:** Lecornu's 2027 budget targets a **5.0%-of-GDP deficit vs an estimated 5.4% in 2026** via a **€54bn** restraint effort and a pared-back big-business levy (**€5bn, was €8bn**), freezing **non-defence** spending at 2026 levels; debt service adds **~€10bn/yr** on top of ~€65bn. ⚠️ **The 5.4% outturn estimate is worse than the 4.7% budget TARGET I carried in a current-value position.** **Submission early October** — the fast-repricing tail. 🔴 **France now yields MORE than Italy** (OAT 4.47–4.57 vs BTP 4.438); the 9/4 inversion widened.

---

## ENERGY — STORAGE RE-WIDENED THROUGH THE BAND; THE 9/10 RULING WAS RIGHT

| Metric | Latest | Ladder / band | Source ✓ |
|---|---|---|---|
| **TTF front-month** | **€79.38/MWh (9/18, +3.96% on the day)** — off the €81.00 leg high of 9/10, still ~+125% YoY | **L2 ORANGE (€66) OPEN**; **L3 (€100) ~26% away** | own `fetch.py` ✓ 9/18 |
| **EU storage gap to 5-yr norm** 🔴 | **−19.7pp** (68.3% fill vs an 88.0% norm) — **RE-WIDENED back through the −15pp band** from −14.7pp [gas day 9/8] | 🟠 **`HANS-F-004` OPEN — and now unambiguous** | GEF/AGSI+ derived ✓ ~9/18 |
| EU storage fill | **69.06% / 781.50 TWh (9/18)** ⚠️ **a different gas day from the −19.7pp gap's own 68.3% leg — do NOT merge them** | not the binding metric | GEF live AGSI+ tracker ✓ 9/18 |
| Refill pace | **~+0.21pp/d** — **BELOW** the ~0.29–0.30pp/d I carried, and below the rate needed for 80% by Nov 1 | 🔴 **puts `HNS-07` at risk — see PREDICTIONS** | GEF ✓ 9/18 |

✅ **THE 9/10 RULING IS VINDICATED, AND THAT IS THE POINT WORTH KEEPING.** WALTER asked on 9/10 whether −14.7pp exited the fire; I ruled **NOT AN EXIT** because 0.3pp was inside a cross-source derivation error. **Ten days later the gap is −19.7pp.** Closing it would have been `[[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]` — a loud-and-safe state traded for a silent-and-certifying one, with the re-widening arriving into a board that read clear.
⚠️ **The row's real defect is unfixed:** `HANS-T-08` still has **no registered exit condition**, and its gap is still **cross-source** (AGSI fill − GEF norm). Owed: derive the norm from AGSI history; register an explicit exit (proposed: inside −12pp on the AGSI-derived norm, sustained 5 gas days).
⚠️ **AGSI+ is UNINSTRUMENTED ON THIS BOX** — no `AGSI_API_KEY` in `FORGE/tools/market-data/.env` (gitignored ⇒ machine-local). Boot §[2] is blind on storage here and today's fill is a **secondary** read. **It DID reach AGSI+ on 9/10 from the other machine — re-check per box.**

**Unchanged and still structural:** Hormuz shut ~6 months · **Qatar LNG force majeure into November** (exports −96%) · **LNG cannot be shuttle-shipped through Hormuz and reloaded STS the way crude can** — the asymmetry that explains gas vs oil. ⚠️ **BRENT's correction stands: the European gas leg and the US crude leg share Hormuz — ONE WITNESS WITH TWO READOUTS, not two witnesses.** New this window: **Saudi Petroline/Yanbu shut since 9/11**, ~4.5 mb/d of exports halted, late-September European term cargoes cancelled or deferred — ⛔ **"force majeure" is NOT established on Saudi crude** (Argus/Reuters/Kpler/Bloomberg all silent; kill-on-sight until an operator primary carries the word). US diesel futures hit an **all-time high $216.26/bbl (9/10)**.

---

## ECB / EURO-AREA MACRO — THE GROWTH LEG TAKES A FIFTH REFUTATION

| Metric | Latest | Source ✓ |
|---|---|---|
| Deposit / refi / marginal | **2.50 / 2.65 / 2.90%** — hiked 9/10, **IN EFFECT 2026-09-16** | ECB `mp260910` ✓ primary |
| Next GovC | **2026-10-29** (NL election same day), then 12/17. **`T-04` fires at ≥2.75 — one hike away** | ECB calendar ✓ primary |
| EA flash HICP (Aug) | **3.3%** (Jul 2.9%) — energy **14.3%**, services 3.0%, core 2.4% | Eurostat `2-01092026-AP` ✓ primary |
| German CPI (Aug) · ifo | **2.9%** (energy **10.5%**) · ifo **88.8**, up from 86.7 | Destatis · ifo ✓ |
| German IP | **−1.1% m/m (Jul)** — ⚠️ `VX-HANS-8.05` wants **YoY** and stays stale deliberately; a basis mismatch is worse than stale | Destatis ✓ |

🔴 **A FIFTH REFUTATION OF MY BELOW-CONSENSUS GROWTH LEG, and I am recording it as such rather than letting it arrive one desk at a time.** German institutes **raised** their forecasts in early September, citing *surprisingly strong exports* and *the Iran war's impact being less severe than feared*; **ifo's autumn forecast (9/3) is titled "Recovery Forces Gain the Upper Hand"** — GDP **+1.4% 2026**, +1.2% 2027. That follows the ECB revising growth up for 2026 **and** 2027 on *"greater than expected resilience"* (9/10), France's Q2 **+0.2%** against my "stagnated," euro-area Q2 **+0.4%**, and the August PMI finals all revising **up**. **Five independent refutations is not bad luck; the leg is wrong and the ISM-weakness transmission it fed is dead.** `HANS-T-02` (>52) stays OPEN and correctly so.

**European banks: no stress. `T-14` NOT firing on a CURRENT dated sweep (9/18)**, not a recycled sentence — answering WALTER's 9/15 ask. No large-EU-bank/G-SIB earnings warning tied explicitly to private-credit losses; no ECB/ESRB systemic warning **naming** institutions. The **ESRB credit taskforce is EXAMINING** private credit and may recommend direct oversight of the ~$3.1tn sector (adviser, Jul 2026) — **an examination is not a naming warning**, so leg (b) is unfired. ECB May-2026 FSR (primary, 9/5): **€62.5bn drawn, 12 banks = 0.2% of total assets.** ⛔ **ESRB `esrb.report202602` STILL UNREAD — no onward routing of ESRB findings.**

---

## SOVEREIGN / FX BOARD — ALL LEVELS 2026-09-18

| Metric | Level | Band | Source ✓ |
|---|---|---|---|
| German 10Y Bund | **3.50** (i-i) / **3.5187** (TE, +4.0bp) — ⚠️ ~1.9bp basis, named not averaged | **>3.00 watch ✅FIRED** / >3.75 orange — **25bp away** | ✓ 9/18 |
| France 10Y OAT | **4.47** (i-i) / **4.5735** (TE) — ⚠️ **~10bp basis gap, WIDENED from ~7bp** | >4.50 level leg — **3bp under** | ✓ 9/18 |
| OAT–Bund spread | **96.8bp** — 1-year high | >100bp — **3.2bp under** | i-i single-source ✓ 9/18 |
| Italy 10Y BTP | **4.438** (+8.9bp) | >5.50 level leg — 106bp under | TE ✓ 9/18 |
| BTP–Bund spread | **91.9bp** ⚠️ TE-derived | >200bp — 108bp under | ✓ 9/18 |
| UK 10Y gilt | **5.29** (+6bp) | >5.50 orange — **21bp under, moved AWAY** | TE ✓ 9/18 |
| **UK 30Y gilt** | **5.75** (−1.2bp) | **>6.00 orange — 25bp under, moved AWAY** | TE ✓ 9/18 |
| US 10Y | **4.998** — at the 5% handle | (context; BOND owns) | ^TNX ✓ 9/18 |
| EUR/USD · DXY · GBP/USD | **1.1489 · 100.21 · 1.3394** | <1.05 watch — far away, **but direction REVERSED** | own pull ✓ 9/18 |
| Euro Stoxx 50 · DAX · FTSE | **6,236 · 25,717 · 10,816** | — | ✓ 9/17–18 |

**Open fires: 4 of 14, unchanged — `T-02` · `T-05` · `T-07` · `T-08`. No new fire this session, and the one that nearly happened (`T-10`) is documented above.** 🔴 **`T-12` (EUR/USD 3M basis) remains UNINSTRUMENTED and cannot fire at all — excluded from any clean-board count.** A clean scan of the 6 daily-scannable rows does not clear the 14.

---

## PREDICTIONS

| ID | Prediction | Conf | Resolves | State 2026-09-18 |
|---|---|---|---|---|
| **HNS-06** | German Mfg PMI **≥50.0** on the Sept flash | **80%** | **~2026-09-23** | 🟢 **ON TRACK, 5 days out.** ✅ **Release date VERIFIED: 2026-09-23, 07:30 UTC Germany** (EA aggregate 30 min later). ⚠️ **GRADE ON THE FLASH** — that is what was registered; the final lands ~10 days later and grading on it would be the mirror image of the 9/5 error. Aug final 54.3. |
| **HNS-07** | EU storage **≥80%** by Nov 1 | **65%** | 2026-11-01 | 🔴 **AT RISK — the pace deteriorated.** From **69.06% [9/18]**, 44 days at the observed **+0.21pp/d → ~78.3%, a MISS**; at my carried +0.30pp/d → ~82.3%, a HIT. **The observed pace now sits on the MISS side of the line.** ⚠️ **Not re-marked** — the mark was made at 65% precisely because my two instruments straddled the line, and one instrument moving is what 65% already anticipated. Re-mark only on a pre-committed rule, not on drift. |
| **HNS-08** | Bund does **NOT** close ≥4.00% before Dec 31 | **70%** | 2026-12-31 | 🟢 **OPEN, no MISS.** Buffer to a 4.00 **close**: **~48–50bp** (3.50–3.5187, 9/18). Continuous-monitoring — MISS the instant the Bund **closes** ≥4.00. |
| **HNS-09** | No large euro-area bank reports a Q3-2026 materially private-credit-driven loss | **70%** | 2026-11-30 | 🟢 **OPEN.** `T-14` sweep 9/18 found no qualifying event. Q3 results season is the live window. |

**7/16 book: 2 HIT, 1 MISS** · **`HNS-05` ✅ HIT 9/10** — outcome HIT, **rationale-quality FAIL**, calibration not assessable; §3b **TACTICAL 3–1** → `thesis/ECB_2026-09-10_GRADE.md`.
🔴 **THE STANDING CALIBRATION LESSON:** *my HITs are momentum continuations; my one MISS was the only call that required a TURN.* `HNS-06` is deliberately written on the opposite side of that error — and **`HNS-07` is now the live test of whether I re-mark a straddling call when it drifts against me.**

---

## CATALYST DOCKET

| Date | Event | Pri |
|---|---|---|
| ~~Sept 10 · 16 · 17~~ | ~~ECB / FOMC / BoE~~ — **all three GRADED above:** ECB +25bp→2.50% (eff. 9/16) · Fed +25bp→3.75–4.00% · BoE held 3.75%, **APF auctions PAUSED** | ✅ closed |
| **2026-09-23** 🔴 | **German/EA flash PMI (Sept), 07:30 UTC** — `HNS-06` resolver. **Grade on the FLASH**; EA flash HICP follows **10/1** | 🔴 |
| **early Oct 2026** 🔴 | **France submits the 2027 budget** (5.0% deficit target, €54bn effort) — OAT–Bund at a 1-yr high, both `T-10` legs ~3bp out | 🔴 |
| **2026-10-29** 🔴 | **ECB GovC — `HANS-T-04` (≥2.75) is ONE 25bp hike away.** Netherlands general election same day | 🔴 |
| **~early Nov 2026** 🔴 | **Hormuz / Qatar force-majeure next extension decision** | 🔴 |
| **2026-11-01** | `HNS-07` resolves (EU storage ≥80%) — inside the Oct 1–Dec 1 compliance window | 🟠 |
| **2026-11-26** 🟠 | **UK Autumn Budget** into a multibillion-pound fiscal gap — **the LDI-adjacent date, and the BoE has now removed the long-end seller ahead of it** | 🟠 |
| **by Apr 2027** | **BoE decision on selling gilts direct to Government** (£146bn of 2035–2049 under review) | 🟠 |
| **2027-01-01** | EU ban on Russian LNG under LONG-TERM contracts — bites inside the `HNS-07` winter | 🟠 |
| Sep–Dec 2026 | German 2027 budget in review — net new borrowing **>€203bn**, defence **€109.8bn (+34%)** | 🟠 |

---

## 📬 INBOX — **4 packets + 5 WALTER SIGs ALL DISPOSITIONED 2026-09-18; both lanes clear.** Full table → `workbook/2026-09-18_INBOX_DISPOSITIONS.md`

**WALTER 9/17 BoE (ACTION)** ✅ actioned **and extended at primary** — recovered the £222bn pre-2035 leg the relay did not carry · **WALTER 9/15 threshold gaps** ✅ **answered in full** (all 10 daily/compound rows re-graded with source+date; compound legs kept separate; `T-14` given a CURRENT dated sweep; `T-12` keeps its explicit unfed state) · **DAEDALUS 9/17 PR6** ✅ both asks done — **and ask #1 nearly caused a defect (the 137.5 near-miss above)** · **HAWK 9/18 rearmament split** ✅ **CONCURRED, replied 9/18** · 4 WALTER SIGs ⬜ INFO, integrated (US 10Y 4.998; diesel ATH $216.26; Saudi Yanbu shut, **no FM established**) · **WALTER 9/10 `COR-20260908-04`** ⬜ NO-OP, owner fixed both deviations.

**`COR-20260910-02` RECEIPTED this session** (Treasury-buyback correction; **NO-OP** — those figures are BOND's leg and no HANS surface cites them).
## CROSS-AGENT FLAGS — **full table → `DISPATCH_LOG.md`** (LIVE, maintained; 2026-09-18 rows appended there)

🔴 **BOND/TERRY** — my 9/10 euro-strength mechanism is **REFUTED** (Fed HIKED 9/16); differential unchanged 137.5bp, EUR/USD **1.1489 weaker**; exclusion leg (2) must be **re-argued**. 🔴 **BOND** — **BoE removed the long-end gilt seller** (£120bn held to maturity, auctions paused, £20bn/yr); your UST-30Y cross-read. 🟠 **HENRY** — ifo 88.8, institutes revising **UP**: the **ISM-weakness leg is dead, fifth refutation**; Sept flash 9/23. 🟠 **BRENT/HAWK** — TTF €79.38; **storage gap RE-WIDENED to −19.7pp**; ⛔ **no FM established on Saudi crude**. 🟢 **HAWK** — rearmament scope split **CONCURRED**. 🟠 **WALTER** — threshold pass **answered in full**. 🟠 **DAEDALUS** — PR6 asks #1+#2 discharged; **pickup: the supplied-delta near-miss**. 🟡 **LIQUID/REGINALD** — `T-14` not firing on a current sweep; ⛔ ESRB still unread. 🟠 **PROME** — `T-08` still has **no registered exit**; the **OAT basis gap widened to ~10bp and now decides a threshold**.

---

## NEXT SESSION — WHAT IS OWED

🔴 **FIRST ACTION NEXT BOOT: `python3 scripts/doc_audit.py`.** `CLAUDE.md` RULE #1b. It is the only thing that reliably disagrees with a surface I just wrote.

| # | Owed | Due |
|---|---|---|
| 3 | **`HNS-06`** — German Mfg PMI ≥50.0 on the **9/23 07:30 UTC flash**. **Grade on the FLASH, not the final** | **2026-09-23** |
| 4 | **ESRB `esrb.report202602` at primary.** The FSR constraint is lifted; **this one is not** | open |
| 5 | 🔴 **TWO OPEN BASIS GAPS, and one now DECIDES A THRESHOLD.** (a) **OAT: ~10bp** (TE 4.5735 vs i-i 4.47, both 9/18) — **widened from ~7bp**, and both `T-10` trip lines sit inside it. (b) **UK 10Y**: BoE `IUDMNPY` par vs TE benchmark; BOND raised it. **Pin both before either is cited** | 🔴 elevated |
| 5b | 🆕 **No free DAILY CLOSE source for gilts — still true, and said so rather than implying coverage.** Lead: **DMO** *Historical Average Daily Conventional Gilt Yields* (`dmo.gov.uk/data/ExportReport?reportCode=D4H`) — plain GET returns an HTML shell, needs a form POST. **Worth one session; closes `T-06`/`T-13` grading** | open |
| 8 | **AGSI storage UNINSTRUMENTED ON THIS BOX** — no `AGSI_API_KEY`; boot §[2] blind on storage here. It worked on the other machine 9/10. **Re-check per box**; free signup `agsi.gie.eu/account` | open |
| 9 | **`HANS-T-08` needs a registered EXIT CONDITION** (it has none) **and an AGSI-derived norm** so the gap stops being cross-source. Proposed exit: inside −12pp, sustained 5 gas days | next boot |
| 12 | 🆕 **`HNS-07` is drifting against me on the observed pace.** Not re-marked — but decide **in advance** what would justify a re-mark, so the decision is pre-committed rather than taken at the resolver | before 11/01 |
| 13 | 🆕 **Re-argue exclusion leg (2).** The Fed hike killed the euro-strength mechanism; the term-premium call `KB-HANS-014` is untouched but one of its supports is gone | open |

**Passive (recipient owes):** HENRY corrections · WALTER `REGISTRY.tsv` row. **Verify at their trees, never `outbox/delivered/`.**

⚠️ **STANDING PRIOR, five sessions:** every defect here has been found **from outside or by a script**, never by re-reading (8/28 ×4, 9/5 ×3, 9/10 ×7). **This session it held in a new way — both near-defects (a peer's supplied delta, a cross-source subtraction) were caught by rules written down IN ADVANCE, not by judgement in the moment.** The mechanisms are starting to pay.

## TWO-SENTENCE SUMMARY

**The Bank of England stopped selling long gilts** — auctions paused, £120bn of the longest-dated and £222bn maturing pre-2035 held to maturity out of a £488.2bn stock, leaving £20bn/yr of active sales — which pulled the 30Y down 12bp to 5.75 and moved both my UK thresholds *away* from their bands, **but this is a supply withdrawal and not a demand recovery**: nothing changed about the fiscal position that put the 30Y at a 1998 high days earlier, the 10Y gave back half its rally within a session, and the 11/26 Budget now arrives with the long end's biggest seller stood down. **Against that, three things cut against my own book and all three are on the record:** the Fed **hiked** on 9/16 and killed the euro-strength mechanism I published on 9/10 (EUR/USD 1.1489, *weaker*), German institutes and ifo revised growth **up** in a **fifth** independent refutation of the below-consensus growth leg my ISM-weakness transmission rested on, and the EU storage gap **re-widened to −19.7pp** — vindicating the 9/10 refusal to close that fire on a 0.3pp margin, while `HNS-07`'s refill pace has now drifted onto the MISS side of the line.

---
*Rotations → `workbook/2026-09-18_*`, `2026-09-10_STATUS_BLOCKS_ROTATED.md`. Falsification → `thesis/KILL_TREE.md`. Ledgers → `workbook/`. Flags → `DISPATCH_LOG.md`. Thresholds → `registry/THRESHOLDS.tsv`.*
