# HANS STATUS.md
**Updated:** 2026-09-18 ~21:3x ET — **8-DAY CATCH-UP. THE BoE PIVOTED THE GILT LONG END, THE FED HIKED, AND ONE OF MY PUBLISHED MECHANISMS IS REFUTED BY IT.** Spawned by Will: *"catch up on recent events and news,"* then a post-commit audit on his question. Every level below is re-pulled today or dated.
**Boot:** `boot.py` exit 1 · `doc_audit.py` **0 findings** before and after this session's edits · R1 corrections **rc=1 → receipted** · 9/10 blocks rotated. I own **`EUROPE_MACRO`** (BOND = time-critical backup). **UK leg: MINE.**

---

## 🔴 THE HEADLINE — BoE 9/17: THE BANK STOPPED SELLING LONG GILTS. READ AT PRIMARY 9/18.

**Bank Rate HELD at 3.75%** (MPC meeting ended 9/16) — and the rate is the *least* important half. **Primary: BoE Market Notice, 17 September 2026**, read in full.

Of a **£488.2bn** APF gilt stock: **£222bn** maturing pre-2035 **held to maturity** · **£120bn of the LONGEST-DATED held to maturity** to indirectly back banknote issuance — 🔴 *the long end is withdrawn from sale* · **£146bn** of 2035–2049 **under review** · active sales just **£20bn/yr**, unwind ~2034 · **auctions PAUSED** while the Bank reviews selling gilts *directly to the Government*, decision **by April 2027**. *(Full figures → `KB-HANS-064`.)*

**£222 + £120 + £146 = £488bn — the entire stock is now held to maturity or under review.** ⚠️ **The £222bn leg is mine from primary and was NOT in WALTER's relay** (accurate on what it carried) — a relay is not a primary `[[finding_asymmetric_rigor_counterparty_claims]]`.

**Market response — right size, wrong duration:** 30Y **5.7415 (−12bp)** / 10Y **5.2169 (−8bp)** intraday 9/17 → by **9/18 the 10Y was back to 5.29 (+6bp)**, ~half the rally given back in one session. **30Y 5.75.**

⇒ **Both UK thresholds moved AWAY; near-trigger flags DOWNGRADED:** `T-13` **25bp** under the 6.00 orange (was **7bp**, at a post-1998 high) · `T-06` **21bp** under 5.50 (was 14bp). **Neither ever fired — no exit to record.**

🔴 **THE READ, AND IT IS NOT "UK STRESS HAS EASED": THIS IS A SUPPLY WITHDRAWAL, NOT A DEMAND RECOVERY.** The seller of last resort stopped adding paper to the long end; nothing changed about the fiscal position that put the 30Y at a 1998 high days earlier. **A yield that falls because the seller left is not a yield that fell because the bid returned** — the 9/18 give-back is the tell. **`11/26 UK Budget` unchanged as the LDI-adjacent date.** Chain: `FLOW-HANS-5 UK_Pension_Stress`.

---

## 🔴 THE FED HIKED 9/16 — AND IT REFUTES A MECHANISM I PUBLISHED ON 9/10

**FOMC 2026-09-16: +25bp to 3.75–4.00%, first hike since 2023, vote 12–0.** Warsh: inflation still too high. **16 of 18 participants expect another hike this year.**

**What I wrote 9/10, verbatim:** *"Fed–ECB differential compresses further on a Sept ECB hike into a Fed on hold … that is the euro-strength mechanism already visible at 1.16."*
**Both halves failed.** The Fed hiked, so the differential did **not** compress — **unchanged at 137.5bp** (both legs +25bp) — and the euro **WEAKENED**: **1.1489 [9/18] vs 1.16 [9/5]**. ⇒ **Exclusion-argument leg (2) must be RE-ARGUED, not restated.** → BOND/TERRY; `KILL_TREE` C-1.

🔴 **AND THE NEAR-MISS WITH IT.** DAEDALUS PR6 (9/17) flagged `VX-HANS-4.03` as **137.5bp on a stale 2.25% ECB**, true figure **112.5** — correct at their read. But between it and mine **the Fed hiked**, moving *both* legs +25bp back to **exactly 137.5**. **Applying the ask mechanically would have written 112.5 — wrong — into an accidentally-correct row, with every structural check passing.** ⇒ **Recompute derived rows from BOTH legs at their own primaries; never accept a supplied delta.** → `ML-HANS-451`

---

## 🔴 FRANCE — BOTH `T-10` LEGS NEAR-TRIGGER, AND THE GRADE WAS DECIDED INSIDE MY OWN BASIS GAP

**OAT–Bund is at a 1-YEAR HIGH.** Single-source daily series (ideal-investisseur, both legs off one screen), spread in bp: **80.4** [8/31] → **84.7** [9/4] → **89.8** [9/11] → **95.6** [9/16, OAT **4.52**] → **95.0** [9/17] → **96.8** [9/18, OAT **4.47** / Bund **3.50**] — **1-yr high**; 1-yr low 59.0, avg 73.7. *(Full table → `KB-HANS-066`.)*

**`HANS-T-10` = spread >100bp AND OAT >4.50. VERDICT: NOT FIRED — 3.2bp and 3bp under, respectively.**

🔴 **BUT READ HOW CLOSE THIS WAS TO A FALSE FIRE.** TE-minus-TE for the same day gives **OAT 4.5735 − Bund 3.5187 = 105.5bp**, clearing **both** legs — it would have been logged as a fire. **Both trip lines sit INSIDE my unresolved OAT basis gap, now WIDENED from ~7bp [9/10] to ~10bp and still outside my ±5bp tolerance.** Graded on the **single-source spread** because *a spread is never derived across two sources* — same class as the `T-08` gap `[[finding_instrument_error_correlated_with_the_trigger_biases_the_gate]]`. **Open item #11 was registered 9/10 for exactly this case and paid for itself today.**

✅ **And the compound structure did its job:** on **9/16 the LEVEL leg alone was MET (OAT 4.52)** while the spread leg was not — a single-leg row would have fired on a day the fragmentation signal was absent.

**Fiscal:** Lecornu's 2027 budget targets **5.0% of GDP vs an estimated 5.4% in 2026** via **€54bn** of restraint and a pared-back levy (**€5bn, was €8bn**), freezing **non-defence** spending; debt service adds **~€10bn/yr** on ~€65bn. ⚠️ **The 5.4% outturn is worse than the 4.7% TARGET I carried in a current-value position.** **Submission early Oct.** 🔴 **France yields MORE than Italy** (OAT 4.47–4.57 vs BTP 4.438).

---

## ENERGY — STORAGE RE-WIDENED THROUGH THE BAND; THE 9/10 RULING WAS RIGHT

| Metric | Latest | Ladder / band | Source ✓ |
|---|---|---|---|
| **TTF front-month** | **€79.38/MWh (9/18, +3.96% on the day)** — off the €81.00 leg high of 9/10, still ~+125% YoY | **L2 ORANGE (€66) OPEN**; **L3 (€100) ~26% away** | own `fetch.py` ✓ 9/18 |
| **EU storage gap to 5-yr norm** 🔴 | **−19.7pp** (68.3% fill vs an 88.0% norm) — **RE-WIDENED back through the −15pp band** from −14.7pp [gas day 9/8] | 🟠 **`HANS-F-004` OPEN — and now unambiguous** | GEF/AGSI+ derived ✓ ~9/18 |
| EU storage fill | **69.06% / 781.50 TWh (9/18)** ⚠️ **a different gas day from the −19.7pp gap's own 68.3% leg — do NOT merge them** | not the binding metric | GEF live AGSI+ tracker ✓ 9/18 |
| Refill pace | **~+0.21pp/d** — **BELOW** the ~0.29–0.30pp/d I carried, and below the rate needed for 80% by Nov 1 | 🔴 **puts `HNS-07` at risk — see PREDICTIONS** | GEF ✓ 9/18 |

✅ **THE 9/10 RULING IS VINDICATED.** WALTER asked whether −14.7pp exited the fire; I ruled **NOT AN EXIT** — 0.3pp was inside the cross-source error. **Ten days later: −19.7pp.** Closing it would have traded a loud-and-safe state for a silent-and-certifying one, with the re-widening arriving into a board reading clear `[[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]`.
⚠️ **The row's real defect is unfixed:** `HANS-T-08` still has **no registered exit condition**, and its gap is still **cross-source** (AGSI fill − GEF norm). Owed: derive the norm from AGSI history; register an explicit exit (proposed: inside −12pp on the AGSI-derived norm, sustained 5 gas days).
⚠️ **AGSI+ is UNINSTRUMENTED ON THIS BOX** — no `AGSI_API_KEY` in `FORGE/tools/market-data/.env` (gitignored ⇒ machine-local). Boot §[2] is blind on storage here and today's fill is a **secondary** read. **It DID reach AGSI+ on 9/10 from the other machine — re-check per box.**

**Unchanged and structural:** Hormuz shut ~6 months · **Qatar LNG FM into November** (exports −96%) · **LNG cannot be STS-transferred through Hormuz the way crude can** — the asymmetry explaining gas vs oil. ⚠️ **BRENT's correction stands: the EU gas leg and the US crude leg share Hormuz — ONE WITNESS, TWO READOUTS.** New: **Saudi Petroline/Yanbu shut since 9/11**, ~4.5 mb/d halted, late-Sept European cargoes cancelled/deferred — ⛔ **no force majeure established on Saudi crude** (Argus/Reuters/Kpler/Bloomberg silent; kill-on-sight absent an operator primary). US diesel ATH **$216.26/bbl (9/10)**. *(Chain detail → `FLOW-HANS-8`.)*

---

## ECB / EURO-AREA MACRO — THE GROWTH LEG TAKES A FIFTH REFUTATION

| Metric | Latest | Source ✓ |
|---|---|---|
| Deposit / refi / marginal | **2.50 / 2.65 / 2.90%** — hiked 9/10, **IN EFFECT 2026-09-16** | ECB `mp260910` ✓ primary |
| Next GovC | **2026-10-29** (NL election same day), then 12/17. **`T-04` fires at ≥2.75 — one hike away** | ECB calendar ✓ primary |
| EA flash HICP (Aug) | **3.3%** (Jul 2.9%) — energy **14.3%**, services 3.0%, core 2.4% | Eurostat `2-01092026-AP` ✓ primary |
| German CPI (Aug) · ifo | **2.9%** (energy **10.5%**) · ifo **88.8**, up from 86.7 | Destatis · ifo ✓ |
| German IP | **−1.1% m/m (Jul)** — ⚠️ `VX-HANS-8.05` wants **YoY** and stays stale deliberately; a basis mismatch is worse than stale | Destatis ✓ |

🔴 **A FIFTH REFUTATION OF MY BELOW-CONSENSUS GROWTH LEG, recorded as such rather than arriving one desk at a time.** German institutes **raised** forecasts in early September (*surprisingly strong exports*; the Iran war *less severe than feared*); **ifo's autumn forecast (9/3): "Recovery Forces Gain the Upper Hand"** — GDP **+1.4% 2026**. That follows the ECB revising growth up for 2026 **and** 2027 on *"greater than expected resilience"*, France Q2 **+0.2%** against my "stagnated," euro-area Q2 **+0.4%**, and all three August PMI finals revising **up**. **Five independent refutations is not bad luck — the leg is wrong and the ISM-weakness transmission it fed is dead.** `HANS-T-02` (>52) stays correctly OPEN. → `KB-HANS-067`

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
| EUR/USD · DXY · GBP/USD | **1.1489 · 100.21 · 1.3394** | <1.05 watch far away, **direction REVERSED** | own pull ✓ 9/18 |
| EuroStoxx50 · DAX · FTSE | **6,236 · 25,717 · 10,816** | — | ✓ 9/17–18 |

**Open fires: 4 of 14, unchanged — `T-02` · `T-05` · `T-07` · `T-08`. No new fire this session, and the one that nearly happened (`T-10`) is documented above.** 🔴 **`T-12` (EUR/USD 3M basis) remains UNINSTRUMENTED and cannot fire at all — excluded from any clean-board count.** A clean scan of the 6 daily-scannable rows does not clear the 14.

---

## PREDICTIONS

| ID | Prediction | Conf | Resolves | State 2026-09-18 |
|---|---|---|---|---|
| **HNS-06** | German Mfg PMI **≥50.0** on the Sept flash | **80%** | **~2026-09-23** | 🟢 **ON TRACK, 5 days out.** ✅ **Release date VERIFIED: 2026-09-23, 07:30 UTC Germany** (EA aggregate 30 min later). ⚠️ **GRADE ON THE FLASH** — that is what was registered; the final lands ~10 days later and grading on it would be the mirror image of the 9/5 error. Aug final 54.3. |
| **HNS-07** | EU storage **≥80%** by Nov 1 | **65%** | 2026-11-01 | 🔴 **AT RISK — the pace deteriorated.** From **69.06% [9/18]**, 44 days at the observed **+0.21pp/d → ~78.3%, a MISS**; at my carried +0.30pp/d → ~82.3%, a HIT. **The observed pace now sits on the MISS side of the line.** ⚠️ **Not re-marked** — the mark was made at 65% precisely because my two instruments straddled the line, and one instrument moving is what 65% already anticipated. Re-mark only on a pre-committed rule, not on drift. |
| **HNS-08** | Bund does **NOT** close ≥4.00% before Dec 31 | **70%** | 2026-12-31 | 🟢 **OPEN, no MISS.** Buffer to a 4.00 **close**: **~48–50bp** (3.50–3.5187, 9/18). Continuous-monitoring — MISS the instant the Bund **closes** ≥4.00. |
| **HNS-09** | No large euro-area bank reports a Q3-2026 materially private-credit-driven loss | **70%** | 2026-11-30 | 🟢 **OPEN.** `T-14` sweep 9/18 found no qualifying event. Q3 results season is the live window. |

**7/16 book: 2 HIT, 1 MISS** · **`HNS-05` ✅ HIT 9/10** — outcome HIT, **rationale-quality FAIL**; §3b **TACTICAL 3–1** → `thesis/ECB_2026-09-10_GRADE.md`.
🔴 **STANDING CALIBRATION LESSON:** *my HITs are momentum continuations; my one MISS was the only call requiring a TURN.* `HNS-06` is written on the opposite side of that error — and **`HNS-07` is now the live test of whether I re-mark a straddling call that drifts against me.**

---

## CATALYST DOCKET

| Date | Event | Pri |
|---|---|---|
| ~~Sept 10 · 16 · 17~~ | ~~ECB / FOMC / BoE~~ — **all three GRADED above:** ECB +25bp→2.50% (eff. 9/16) · Fed +25bp→3.75–4.00% · BoE held 3.75%, **APF auctions PAUSED** | ✅ closed |
| **2026-09-23** 🔴 | **German/EA flash PMI (Sept) 07:30 UTC** — `HNS-06` resolver. **Grade the FLASH**; EA HICP **10/1** | 🔴 |
| **early Oct 2026** 🔴 | **France submits the 2027 budget** (5.0% target, €54bn) — OAT–Bund at a 1-yr high, both `T-10` legs ~3bp out | 🔴 |
| **2026-10-29** 🔴 | **ECB GovC — `T-04` (≥2.75) is ONE 25bp hike away.** Netherlands election same day | 🔴 |
| **~early Nov 2026** 🔴 | **Hormuz / Qatar FM next extension decision** | 🔴 |
| **2026-11-01** | `HNS-07` resolves (storage ≥80%) — inside the Oct 1–Dec 1 compliance window | 🟠 |
| **2026-11-26** 🟠 | **UK Autumn Budget** into a multibillion-pound fiscal gap — **the LDI-adjacent date, with the long-end seller now stood down ahead of it** | 🟠 |
| **by Apr 2027** | **BoE decision on selling gilts direct to Government** (£146bn 2035–2049 in review) | 🟠 |
| **2027-01-01** | EU ban on Russian LNG under LONG-TERM contracts — bites inside the `HNS-07` winter | 🟠 |
| Sep–Dec 2026 | German 2027 budget in review — borrowing **>€203bn**, defence **€109.8bn (+34%)** | 🟠 |

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
| 4 | **ESRB `esrb.report202602` at primary.** FSR constraint lifted; **this one is not** | open |
| 5 | 🔴 **TWO OPEN BASIS GAPS, and one now DECIDES A THRESHOLD.** (a) **OAT: ~10bp** (TE 4.5735 vs i-i 4.47, both 9/18) — **widened from ~7bp**, and both `T-10` trip lines sit inside it. (b) **UK 10Y**: BoE `IUDMNPY` par vs TE benchmark; BOND raised it. **Pin both before either is cited** | 🔴 elevated |
| 5b | 🆕 **No free DAILY CLOSE source for gilts — said so rather than implying coverage.** Lead: **DMO** daily conventional gilt yields (`dmo.gov.uk/data/ExportReport?reportCode=D4H`) — plain GET returns an HTML shell, needs a form POST. **One session; closes `T-06`/`T-13` grading** | open |
| 8 | **AGSI storage UNINSTRUMENTED ON THIS BOX** — no `AGSI_API_KEY`; boot §[2] blind on storage here. It worked on the other machine 9/10. **Re-check per box**; free signup `agsi.gie.eu/account` | open |
| 9 | **`HANS-T-08` needs a registered EXIT CONDITION** (it has none) **and an AGSI-derived norm** so the gap stops being cross-source. Proposed exit: inside −12pp, sustained 5 gas days | next boot |
| 12 | 🆕 **`HNS-07` drifting against me on observed pace.** Not re-marked — but decide **in advance** what would justify one, so it is pre-committed rather than taken at the resolver | before 11/01 |
| 13 | 🆕 **Re-argue exclusion leg (2).** The Fed hike killed the euro-strength mechanism; `KB-HANS-014` is untouched but a support is gone | open |

**Passive (recipient owes):** HENRY corrections · WALTER `REGISTRY.tsv`. **Verify at their trees, never `outbox/delivered/`.**

## 🔴 POST-COMMIT AUDIT (Will asked) — **3 DEFECTS IN MY OWN COMMITTED WORK, ALL FIXED.** Detail → `workbook/2026-09-18_POST_COMMIT_AUDIT.md`

**① STATUS-TOKEN SEMANTICS (serious).** I minted `SUPERSEDED-BY-KB-HANS-059` and `EXPIRED-NOT-REFRESHED` **without opening `STATE_VOCABULARY.md`, which root canon points at.** Two guards here then read one column differently: `boot.py` printed **"10 EXPIRED" when the truth was 3**; **`doc_audit.py` C8 — an allowlist of ONE token — silently dropped 3 rows from the stale-value check, plus 2 `CORRECTED` + 2 `CONFIRMED` never checked at all.** 🔴 **Loud-and-wrong is survivable; quiet-and-unsupervised is not.** FIXED: one shared dead-PREFIX predicate in both guards · **unknown tokens resolve to LIVE on purpose** · boot NAMES unrecognised tokens · KB in canon form · **7 regression tests, mutation-verified.** Boot §[7] now reads **3 expired** — true. → `ML-HANS-452`, RULE #1c
**② ML ID COLLISION (mine, same session):** cited `ML-HANS-450`, already taken by my 9/10 lesson. Corrected to `451` here **and in the delivered DAEDALUS packet with a visible note**, not silently. **③ Doc counts:** `CLAUDE.md` said 51 tests / 7 checks; actual **58 / 8**.
⚠️ **UNFIXED, standing:** the **ECB primary pull is INTERMITTENT** — consecutive boots gave a clean §[2], then a triple failure (AAA 10Y + DE base leg, so spreads were correctly not computed). It **fails loud and refuses to compute off a stale base** — but **a blank §[2] is not evidence of a quiet board.**


⚠️ **STANDING PRIOR, now SIX sessions:** every defect here has been found **from outside or by a script**, never by re-reading (8/28 ×4, 9/5 ×3, 9/10 ×7, **9/18 ×3 — and those 3 were in work I had committed an hour earlier**). **The two near-defects I avoided were caught by rules written IN ADVANCE; the three I shipped were caught by running the tools again.** Neither was caught by reading.

## TWO-SENTENCE SUMMARY

**The Bank of England stopped selling long gilts** — auctions paused, £120bn of the longest-dated and £222bn maturing pre-2035 held to maturity out of a £488.2bn stock, leaving £20bn/yr of active sales — which pulled the 30Y down 12bp to 5.75 and moved both my UK thresholds *away* from their bands, **but this is a supply withdrawal and not a demand recovery**: nothing changed about the fiscal position that put the 30Y at a 1998 high days earlier, the 10Y gave back half its rally within a session, and the 11/26 Budget now arrives with the long end's biggest seller stood down. **Against that, three things cut against my own book and all three are on the record:** the Fed **hiked** on 9/16 and killed the euro-strength mechanism I published on 9/10 (EUR/USD 1.1489, *weaker*), German institutes and ifo revised growth **up** in a **fifth** independent refutation of the below-consensus growth leg my ISM-weakness transmission rested on, and the EU storage gap **re-widened to −19.7pp** — vindicating the 9/10 refusal to close that fire on a 0.3pp margin, while `HNS-07`'s refill pace has now drifted onto the MISS side of the line.

---
*Archives → `workbook/`. Falsification → `thesis/KILL_TREE.md`. Flags → `DISPATCH_LOG.md`. Thresholds → `registry/`.*
