# HANS STATUS.md
**Updated:** 2026-09-18 ~21:5x ET — **CLOSED OUT. 8-DAY CATCH-UP: THE BoE PIVOTED THE GILT LONG END, THE FED HIKED, AND ONE OF MY PUBLISHED MECHANISMS IS REFUTED BY IT.** Will: *"catch up on events and news"* → post-commit audit → PROME's rearmament ask → Saudi/Europe. Levels re-pulled today or dated.
**Boot:** rc1 · `doc_audit.py` **0 findings** · 58 tests OK · R1 **rc=1 → receipted** · mail lanes empty. I own **`EUROPE_MACRO`** (BOND = time-critical backup). **UK leg: MINE.**

---

## 🔴 THE HEADLINE — BoE 9/17: THE BANK STOPPED SELLING LONG GILTS. Read at PRIMARY 9/18. Detail → `workbook/2026-09-18_BOE_APF_BLOCK.md`, fact → `KB-HANS-064`

**Bank Rate HELD 3.75%** (meeting ended 9/16) — the rate is the *least* important half. Of a **£488.2bn** APF stock: **£222bn** pre-2035 **held to maturity** · **£120bn of the LONGEST-DATED held to maturity** (banknote backing) · **£146bn** of 2035–2049 **under review** · active sales **£20bn/yr**, unwind ~2034 · **auctions PAUSED** pending a review of selling gilts *direct to Government*, decision **by April 2027**. **£222+£120+£146 = £488bn — the entire stock is held to maturity or under review.** ⚠️ **The £222bn leg is mine from primary and was NOT in WALTER's relay** — a relay is not a primary.
**Market — right size, wrong duration:** 30Y **5.7415 (−12bp)** / 10Y **5.2169 (−8bp)** intraday 9/17 → **10Y back to 5.29 (+6bp) by 9/18**, ~half the rally given back in a session. **30Y 5.75.** ⇒ **Both UK thresholds moved AWAY; near-trigger flags DOWNGRADED** (`T-13` 25bp under, was 7bp at a post-1998 high; `T-06` 21bp under). **Neither ever fired — no exit to record.**
🔴 **NOT "UK STRESS HAS EASED": THIS IS A SUPPLY WITHDRAWAL, NOT A DEMAND RECOVERY.** The seller of last resort stopped adding paper; nothing changed about the fiscal position that put the 30Y at a 1998 high days earlier — **the 9/18 give-back is the tell.** **`11/26 UK Budget` unchanged as the LDI-adjacent date.**


---

## 🔴 THE FED HIKED 9/16 — AND IT REFUTES A MECHANISM I PUBLISHED 9/10. Detail → `workbook/2026-09-18_FED_HIKE_REFUTATION_BLOCK.md`, fact → `KB-HANS-065`

**FOMC 2026-09-16: +25bp to 3.75–4.00%, first hike since 2023, 12–0; 16 of 18 expect another this year.** **What I wrote 9/10:** *"the differential compresses on a Sept ECB hike into a Fed on HOLD — that is the euro-strength mechanism."* **Both halves failed:** the differential is **unchanged at 137.5bp** (both legs +25bp) and the euro **WEAKENED** to **1.1489**. ⇒ **Exclusion-argument leg (2) must be RE-ARGUED, not restated.** → BOND/TERRY; `KILL_TREE` C-1.
🔴 **THE NEAR-MISS WITH IT.** DAEDALUS PR6 flagged `VX-HANS-4.03` as 137.5 on a stale 2.25% ECB, true value **112.5** — correct at their read. Between it and mine **the Fed hiked**, moving both legs +25bp back to **exactly 137.5**. **Applying the ask mechanically would have written a wrong number into an accidentally-correct row, every structural check passing.** ⇒ **Recompute derived rows from BOTH legs at their own primaries; never accept a supplied delta.** → `ML-HANS-451`


---

## 🔴 FRANCE — BOTH `T-10` LEGS NEAR-TRIGGER, GRADE DECIDED INSIDE MY OWN BASIS GAP. Detail → `workbook/2026-09-18_FRANCE_T10_BLOCK.md`, fact → `KB-HANS-066`

**OAT–Bund at a 1-YEAR HIGH.** Single-source daily series (ideal-investisseur, both legs one screen), bp: **80.4** [8/31] → **84.7** [9/4] → **89.8** [9/11] → **95.6** [9/16, OAT **4.52**] → **95.0** [9/17] → **96.8** [9/18, OAT **4.47** / Bund **3.50**]; 1-yr low 59.0, avg 73.7.
**`T-10` = spread >100bp AND OAT >4.50. VERDICT: NOT FIRED — 3.2bp and 3bp under.** 🔴 **But TE-minus-TE for the same day gives 105.5bp / OAT 4.5735, which clears BOTH legs and would have been logged as a fire.** Both trip lines sit **inside my OAT basis gap, widened ~7bp → ~10bp** and still outside my ±5bp tolerance. **Graded on the single-source spread — a spread is never derived across two sources.** ✅ **On 9/16 the LEVEL leg alone was met (OAT 4.52) while the spread was not — the compound structure did its job.**
**Fiscal:** 2027 budget targets **5.0% of GDP vs an estimated 5.4% in 2026** via **€54bn** restraint, freezing **non-defence** spending; debt service adds **~€10bn/yr** on ~€65bn. ⚠️ **The 5.4% outturn is worse than the 4.7% TARGET I carried in a current-value position.** **Submission early Oct.** 🔴 **France yields MORE than Italy** (OAT 4.47–4.57 vs BTP 4.438).


---

## ENERGY — STORAGE RE-WIDENED THROUGH THE BAND; THE 9/10 RULING WAS RIGHT

| Metric | Latest | Ladder / band | Source ✓ |
|---|---|---|---|
| **TTF front-month** | **€79.38/MWh (9/18, +3.96% on the day)** — off the €81.00 leg high of 9/10, still ~+125% YoY | **L2 ORANGE (€66) OPEN**; **L3 (€100) ~26% away** | own `fetch.py` ✓ 9/18 |
| **EU storage gap to 5-yr norm** 🔴 | **−19.7pp** (68.3% fill vs an 88.0% norm) — **RE-WIDENED back through the −15pp band** from −14.7pp [gas day 9/8] | 🟠 **`HANS-F-004` OPEN — and now unambiguous** | GEF/AGSI+ derived ✓ ~9/18 |
| EU storage fill | **69.06% / 781.50 TWh (9/18)** ⚠️ **a different gas day from the gap's own 68.3% leg — do NOT merge** | not the binding metric | GEF AGSI+ tracker ✓ 9/18 |
| Refill pace | **~+0.21pp/d** — **BELOW** the ~0.29–0.30pp/d I carried and below the rate needed for 80% by Nov 1 | 🔴 **`HNS-07` at risk** | GEF ✓ 9/18 |

✅ **THE 9/10 RULING IS VINDICATED.** WALTER asked whether −14.7pp exited the fire; I ruled **NOT AN EXIT** — 0.3pp was inside the cross-source error. **Ten days later: −19.7pp.** Closing it would have traded a loud-and-safe state for a silent-and-certifying one, with the re-widening arriving into a board reading clear `[[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]`.
⚠️ **The row's real defect is unfixed:** `HANS-T-08` has **no registered exit condition** and its gap is still **cross-source** (AGSI fill − GEF norm). Owed: derive the norm from AGSI history; register an exit (proposed: inside −12pp, 5 gas days).
⚠️ **AGSI+ UNINSTRUMENTED ON THIS BOX** — no `AGSI_API_KEY` (machine-local). Boot §[2] blind on storage; today's fill is **secondary**. **It reached AGSI+ on 9/10 from the other machine — re-check per box.**

**Unchanged and structural:** Hormuz shut ~6 months · **Qatar LNG FM into November** (exports −96%) · **LNG cannot be STS-transferred through Hormuz the way crude can.** ⚠️ **BRENT's correction stands: the EU gas leg and the US crude leg share Hormuz — ONE WITNESS, TWO READOUTS.** US diesel ATH **$216.26/bbl (9/10)**. *(Chain → `FLOW-HANS-8`.)*

### 🔴 SAUDI CRUDE TO EUROPE — **Will asked 9/18; premise substantially right, desk was BEHIND.** Detail → `workbook/2026-09-18_SAUDI_EUROPE_BLOCK.md` · `HANS-T-15` (new) · `KB-HANS-073`–`080`

**Was carrying:** *some* late-Sept cargoes to ≥3 refiners. **Broke 9/18:** Aramco has told European **term** customers **ZERO October crude**, **all European term buyers** (Bloomberg 9/18). **Petroline — the ~7 mb/d HORMUZ BYPASS — drone-struck 9/10; nothing out of Yanbu since 9/11; bypass ~half in ~a month, full repair 4–6 weeks.** 🔴 **Both Saudi export routes impaired at once.** ⛔ **Principal-unconfirmed: Aramco declined comment; no FM on any leg.**
🔑 **Concentration, not aggregate:** ~**577 kb/d** = **~4–5% of European runs**, replaceable at a price — but **Orlen runs Saudi at ~40–50% of slate.** ⇒ a **slate-and-differentials** event, not a shortfall.
⚠️ **MY BRENT NUMBER WAS WRONG AND IS WITHDRAWN.** "Brent −5.8% on 9/18 / faded **on the day**" compared **December to November's prior close** — `BZ=F` **rolled 9/18**. At named November: **108.75 [9/15] → 103.21 [9/18] = −5.09% over three sessions**; 9/17→9/18 is **−1.54%, noise.** ✅ **The three-session fade survives; the same-day claim is dead.** PROME flagged (HAWK found the class; **4th desk today**); **reproduced at my own named-contract pull first.** ⚠️ **I had criticised coverage for exactly this error one contract over.** → `KB-HANS-078`, `ML-HANS-453`
🔴 **Same class on my OWN open fire:** boot pulls generic **`TTF=F`** → `TTFV26.NYM` **October, expires 9/29** — right today, **rolls inside two weeks on a LEVEL ladder.** Sized: Oct **79.38** vs Nov **78.00** = **−1.38, no rung crossed** ⇒ no state change. **Contract now named in `T-07`.** → `KB-HANS-079`
🆕 **Against my own alarm: TTF is BACKWARDATED into winter** (Oct 79.38 > Nov 78.00, same date; Dec 75.78 / Jan 75.61 ⚠️ one day stale). With storage **−19.7pp** the textbook shape is winter *contango*. **The curve is not pricing a winter crisis.** Untested. → `KB-HANS-080`
⚠️ **ECB read — GENUINELY AMBIGUOUS.** Hawkish: costs rise via differentials into a Council that named energy an upside risk, October window **inside** pre-**10/29**, `T-04` one hike away. Dovish: the headline oil input is **disinflating**. ⇒ **Not a clear hike signal.** Discriminator — do European refined products decouple upward from a falling Brent? **Unobservable here.** → `KB-HANS-077`

---

## ECB / EURO-AREA MACRO — THE GROWTH LEG TAKES A FIFTH REFUTATION

| Metric | Latest | Source ✓ |
|---|---|---|
| Deposit / refi / marginal | **2.50 / 2.65 / 2.90%** — hiked 9/10, **IN EFFECT 2026-09-16** | ECB `mp260910` ✓ primary |
| Next GovC | **2026-10-29** (NL election same day), then 12/17. **`T-04` fires at ≥2.75 — one hike away** | ECB calendar ✓ primary |
| EA flash HICP (Aug) | **3.3%** (Jul 2.9%) — energy **14.3%**, services 3.0%, core 2.4% | Eurostat `2-01092026-AP` ✓ primary |
| German CPI (Aug) · ifo | **2.9%** (energy **10.5%**) · ifo **88.8**, up from 86.7 | Destatis · ifo ✓ |
| German IP | **−1.1% m/m (Jul)** — ⚠️ `VX-HANS-8.05` wants **YoY** and stays stale deliberately; a basis mismatch is worse than stale | Destatis ✓ |

🔴 **FIFTH REFUTATION OF MY BELOW-CONSENSUS GROWTH LEG** — German institutes **raised** forecasts early Sept; **ifo autumn (9/3): "Recovery Forces Gain the Upper Hand"**, GDP **+1.4% 2026**. Following the ECB revising growth up for 2026 **and** 2027, France Q2 **+0.2%** vs my "stagnated," EA Q2 **+0.4%**, and all three August PMI finals revising **up**. **Five independent refutations is not bad luck — the leg is wrong and the ISM-weakness transmission it fed is dead.** `T-02` stays correctly OPEN. → `KB-HANS-067`

**European banks: no stress. `T-14` NOT firing on a CURRENT dated sweep (9/18)**, not a recycled sentence — answering WALTER's 9/15 ask. No G-SIB earnings warning tied explicitly to private-credit losses; no ECB/ESRB warning **naming** institutions — the ESRB taskforce is **EXAMINING** the ~$3.1tn sector (Jul 2026), and **an examination is not a naming warning.** FSR primary (9/5): **€62.5bn drawn, 12 banks = 0.2% of assets.** ⛔ **ESRB report STILL UNREAD — no onward routing.** → `KB-HANS-068`

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

**Open fires: 4 of 15 — `T-02` · `T-05` · `T-07` · `T-08`. No new fire; the one that nearly happened (`T-10`) is above. 🆕 `T-15` Saudi-crude-to-Europe REGISTERED 9/18** (see §SAUDI). 🔴 **`T-12` (EUR/USD 3M basis) remains UNINSTRUMENTED and cannot fire at all — excluded from any clean-board count.** A clean scan of the 6 daily-scannable rows does not clear the 14.

---

## PREDICTIONS

| ID | Prediction | Conf | Resolves | State 2026-09-18 |
|---|---|---|---|---|
| **HNS-06** | German Mfg PMI **≥50.0** on the Sept flash | **80%** | **2026-09-23** | 🟢 **ON TRACK, 5 days out.** ✅ **Release VERIFIED 9/23 07:30 UTC.** ⚠️ **GRADE THE FLASH** — that is what was registered; grading the final ~10 days later is the mirror image of the 9/5 error. Aug final 54.3. |
| **HNS-07** | EU storage **≥80%** by Nov 1 | **65%** | 2026-11-01 | 🔴 **AT RISK.** From **69.06% [9/18]**, 44 days at the observed **+0.21pp/d → ~78.3%, a MISS**; at my carried +0.30pp/d → ~82.3%, a HIT. **Observed pace now sits on the MISS side.** ⚠️ **Not re-marked** — 65% was set *because* my two instruments straddled the line; one moving is what 65% already priced. Re-mark only on a pre-committed rule. |
| **HNS-08** | Bund does **NOT** close ≥4.00% before Dec 31 | **70%** | 2026-12-31 | 🟢 **OPEN.** Buffer to a 4.00 **close**: **~48–50bp** (3.50–3.5187, 9/18). Continuous — MISS the instant it **closes** ≥4.00. |
| **HNS-09** | No large euro-area bank reports a Q3-2026 materially private-credit-driven loss | **70%** | 2026-11-30 | 🟢 **OPEN.** `T-14` sweep 9/18: no qualifying event. Q3 results is the live window. |

**7/16 book: 2 HIT, 1 MISS** · **`HNS-05` ✅ HIT 9/10** — outcome HIT, **rationale-quality FAIL**; §3b **TACTICAL 3–1**.
🔴 **STANDING CALIBRATION LESSON:** *my HITs are momentum continuations; my one MISS was the only call requiring a TURN.* `HNS-06` is written on the opposite side of it — and **`HNS-07` is the live test of whether I re-mark a straddling call that drifts against me.**

---

## CATALYST DOCKET

| Date | Event | Pri |
|---|---|---|
| ~~Sept 10 · 16 · 17~~ | ~~ECB / FOMC / BoE~~ — **all three GRADED above:** ECB +25bp→2.50% (eff. 9/16) · Fed +25bp→3.75–4.00% · BoE held 3.75%, **APF auctions PAUSED** | ✅ closed |
| **2026-09-23** 🔴 | **German/EA flash PMI (Sept) 07:30 UTC** — `HNS-06` resolver. **Grade the FLASH**; EA HICP **10/1** | 🔴 |
| **early Oct 2026** 🔴 | **France submits the 2027 budget** (5.0% target, €54bn) — OAT–Bund at a 1-yr high, both `T-10` legs ~3bp out | 🔴 |
| **2026-10-29** 🔴 | **ECB GovC — `T-04` (≥2.75) ONE 25bp hike away.** Netherlands election same day | 🔴 |
| **~early Nov 2026** 🔴 | **Hormuz / Qatar FM next extension decision** | 🔴 |
| **2026-11-01** | `HNS-07` resolves (storage ≥80%) — in the Oct 1–Dec 1 compliance window | 🟠 |
| **2026-11-26** 🟠 | **UK Autumn Budget** into a multibillion-pound fiscal gap — **the LDI-adjacent date, with the long-end seller now stood down ahead of it** | 🟠 |
| **by Apr 2027** | **BoE decision: sell gilts direct to Government?** (£146bn 2035–2049 in review) | 🟠 |
| **2027-01-01** | EU ban on Russian LNG, LONG-TERM contracts — bites inside the `HNS-07` winter | 🟠 |
| Sep–Dec 2026 | German 2027 budget in review — borrowing **>€203bn**, defence **€109.8bn (+34%)** | 🟠 |

---

## 📬 INBOX — **all lanes CLEAR.** → `workbook/2026-09-18_INBOX_DISPOSITIONS.md`

4 packets + 5 WALTER SIGs read and filed one at a time. **WALTER BoE** ✅ actioned, **extended at primary** · **WALTER thresholds** ✅ answered in full · **DAEDALUS PR6** ✅ both asks · **HAWK split** ✅ **CONCURRED** · **`COR-20260910-02`** NO-OP. 🆕 **PROME cross-session ×4** — rearmament read, Saudi supplement, roll-artifact correction accepted, local enumeration returned.


## CROSS-AGENT FLAGS — **full state → `DISPATCH_LOG.md`** (LIVE; 2026-09-18 rows appended there)

🔴 **BOND/TERRY** euro-strength mechanism **REFUTED** (Fed hiked 9/16) + **BoE removed the long-end gilt seller** · 🔴 **BRENT/HENRY** Saudi-to-Europe + **Brent roll-artifact correction at named contracts** · 🟠 **HENRY** ISM-weakness leg **dead, 5th refutation** · 🟢 **HAWK** rearmament split **CONCURRED**, S&P figure qualified · 🟠 **WALTER** threshold pass **answered in full** · 🟠 **DAEDALUS** PR6 discharged + supplied-delta pickup · 🟡 **LIQUID/REGINALD** `T-14` not firing, ESRB unread · 🔴 **PROME** fiscal leg **does NOT support "rising conflict risk"** (`research/2026-09-18_REARMAMENT_FISCAL_READ.md`), `T-08` still has no exit, OAT basis gap now decides a threshold, roll enumeration returned.

---

## NEXT SESSION — WHAT IS OWED

🔴 **FIRST ACTION NEXT BOOT: `python3 scripts/doc_audit.py`.** `CLAUDE.md` RULE #1b. It is the only thing that reliably disagrees with a surface I just wrote.
🔴 **SECOND: the CONTRACT ROLL lands 9/28 (`NG=F`) and 9/29 (`TTF=F`).** `KB-HANS-079`/`081` expire **9/25** so boot raises it **before** the roll — *a warning dated on its own event is not a warning.* **`T-07` is a LEVEL ladder with L1+L2 FIRED: never grade a rung crossing across a roll.** Harmless this time (−€1.38, no rung crossed) **and only by the curve's shape.**

| # | Owed | Due |
|---|---|---|
| 3 | **`HNS-06`** — German Mfg PMI ≥50.0, **9/23 07:30 UTC flash**. **Grade the FLASH, not the final** | **2026-09-23** |
| 4 | **ESRB `esrb.report202602` at primary.** FSR constraint lifted; **this is not** | open |
| 5 | 🔴 **TWO OPEN BASIS GAPS, one now DECIDES A THRESHOLD.** (a) **OAT ~10bp** (TE 4.5735 vs i-i 4.47, 9/18), **widened from ~7bp** — both `T-10` trip lines sit inside it. (b) **UK 10Y**: BoE `IUDMNPY` par vs TE benchmark. **Pin both before either is cited** | 🔴 |
| 5b | 🆕 **No free DAILY CLOSE source for gilts.** Lead: **DMO** (`ExportReport?reportCode=D4H`) — plain GET returns an HTML shell, needs a form POST. **One session; closes `T-06`/`T-13`** | open |
| 8 | **AGSI UNINSTRUMENTED ON THIS BOX** — no `AGSI_API_KEY`; boot §[2] blind on storage. Worked on the other machine 9/10. **Re-check per box**; signup `agsi.gie.eu/account` | open |
| 9 | **`T-08` needs a registered EXIT CONDITION** (none) **+ an AGSI-derived norm** so the gap stops being cross-source. Proposed: inside −12pp, 5 gas days | next boot |
| 12 | **`HNS-07` drifting against me on pace.** Not re-marked — decide **in advance** what would justify one, pre-committed rather than at the resolver | before 11/01 |
| 13 | **Re-argue exclusion leg (2).** The Fed hike killed the euro-strength mechanism; `KB-HANS-014` untouched but a support is gone | open |
| 14 | 🆕 **`VX-HANS-11.03` Defense_Issuance_5yr 64d stale** — the vector that should carry the rearmament question isn't current. Read the German budget at **primary**; settle `KB-051`'s €203bn vs €118.7bn perimeter | 🟠 |

## 🔴 POST-COMMIT AUDIT (Will asked) — **5 DEFECTS IN MY OWN SESSION'S WORK, ALL FIXED.** Detail → `workbook/2026-09-18_POST_COMMIT_AUDIT.md`

**① STATUS-TOKEN SEMANTICS.** Minted tokens **without opening `STATE_VOCABULARY.md`**. Two guards read one column differently: boot printed **"10 EXPIRED" when the truth was 3**; **`doc_audit` C8 — an allowlist of ONE token — silently dropped 3 rows, plus 4 never checked.** 🔴 **Loud-and-wrong is survivable; quiet-and-unsupervised is not.** Fixed: shared dead-PREFIX predicate · **unknown tokens = LIVE on purpose** · boot names unrecognised tokens · **7 tests, mutation-verified.** → `ML-HANS-452`, RULE #1c
**② ML ID collision** (`450` taken) → `451`, corrected **in the delivered packet with a visible note**. **③ Doc counts** 51/7 → **58/8**. **④ PUBLISHED metric-name SPLIT** — new names for existing series orphaned them **and left 67.33 / 87.4 reading CURRENT**, disabling stale-consumer detection; repaired by **continuing the established names** (append-only ⇒ never rename) → `ML-HANS-455`. **⑤ `/tmp/enum.py` shadowed the stdlib** — ran as an import, **printed success, then crashed**; writes verified clean, but that was **luck about ordering** → `ML-HANS-454`.
⚠️ **UNFIXED:** the **ECB pull is INTERMITTENT** — a blank §[2] is not a quiet board.


⚠️ **STANDING PRIOR, SIX sessions:** every defect here found **from outside or by a script**, never by re-reading (8/28 ×4, 9/5 ×3, 9/10 ×7, **9/18 ×5**). 🆕 **Tonight added a new route: two came from a PEER's flag, and chasing one of those found the roll exposure on my own open fire.** The near-defects I avoided were caught by rules written **in advance**; the ones I shipped, by running the tools again. **None by reading.**

## TWO-SENTENCE SUMMARY

**The Bank of England stopped selling long gilts** — auctions paused, £120bn of the longest-dated and £222bn maturing pre-2035 held to maturity out of a £488.2bn stock, leaving £20bn/yr of active sales — which pulled the 30Y down 12bp to 5.75 and moved both my UK thresholds *away* from their bands, **but this is a supply withdrawal and not a demand recovery**: nothing changed about the fiscal position that put the 30Y at a 1998 high days earlier, the 10Y gave back half its rally within a session, and the 11/26 Budget now arrives with the long end's biggest seller stood down. **Against that, three things cut against my own book and all three are on the record:** the Fed **hiked** on 9/16 and killed the euro-strength mechanism I published on 9/10 (EUR/USD 1.1489, *weaker*), German institutes and ifo revised growth **up** in a **fifth** independent refutation of the below-consensus growth leg my ISM-weakness transmission rested on, and the EU storage gap **re-widened to −19.7pp** — vindicating the 9/10 refusal to close that fire on a 0.3pp margin, while `HNS-07`'s refill pace has now drifted onto the MISS side of the line.

---
*Archives → `workbook/`. Falsification → `thesis/KILL_TREE.md`. Flags → `DISPATCH_LOG.md`. Thresholds → `registry/`.*
