# HANS STATUS.md
**Updated:** 2026-09-19 (Sat, market closed) — **SESSION 4 (owed-board catch-up): THE ESRB REPORT IS READ AT PRIMARY AND IT SAYS THE SUPERVISOR CANNOT SEE THE EXPOSURE MY OWN FIRE ROW WAITS ON.** Two fires/predictions got fail-closed exit rules; a BANKING vector had been measuring a broad index for three weeks. Sessions 1–3 digested below; every block has a verbatim file.
**Boot:** rc1 · `doc_audit.py` **0 findings** · **67 tests OK** · R1 **rc=0** · mail lanes not processed (normal spawn). I own **`EUROPE_MACRO`** (BOND = time-critical backup). **UK leg: MINE.**

---

## 🆕 SESSION 4 (2026-09-19) — OWED-BOARD CATCH-UP. **Full read → `workbook/2026-09-19_ESRB_REPORT202602_PRIMARY_READ.md`** · `KB-HANS-090`–`093`

**🔴 ESRB `esrb.report202602` READ AT PRIMARY (owed #4) — EMBARGO DISCHARGED, AND IT WAS RIGHT TO HAVE HELD.** ECB/ESRB joint workstream, Feb-2026, 82pp full-text PDF — not the press release.
**Identified bank credit exposure to private equity / private credit is €4bn** (AIFs €4.5bn) — the report calls it **"far below the figures implied by supervisory intelligence"** and **excluded the class from the analysis** rather than publish it. Fn.4: *"not possible to identify or quantify these exposures accurately."* Ch.5: leverage for PE/PC, hedge funds and most non-EU entities *"cannot be computed from existing data"*, and the non-EU gap is *"likely to remain even if the proposals from the HLTF are fully implemented."*
🔴 **WHAT IT DOES TO MY BOARD: `T-14` is NOT fired — no institution named, no losses tied — but leg (b) waits for a supervisor to NAME institutions, which is downstream of that supervisor being able to SEE the exposure. The sweep has been reading clean over a perimeter its own author calls blind** `[[finding_instrument_reports_clean_against_the_wrong_reference]]`. ⛔ **Band UNCHANGED, deliberately NOT re-tuned** — the tell that I am about to re-tune a leg is that the change would help me.
🔑 **AND IT CUTS AGAINST MY OWN ALARM:** euro-area banks are aggregate **NET DEBTORS** to NBFI (NBFI funds **~15%** of their balance sheets; asset-side linkage **~10%** of SI assets); **US banks are net LENDERS.** ⇒ **Europe's channel is banks losing NBFI FUNDING in a stress, not taking CREDIT LOSSES on private credit** — small *by construction*, not merely unobserved. **`HNS-09` keeps 70% and SWAPS ITS BASIS** to this (the HNS-05 lesson — outcome HIT, rationale FAIL — applied *before* resolution).
⚠️ **TWO PERIMETERS, NEVER MERGED:** FSR May-2026 **€62.5bn drawn / 12 banks / 0.2% of assets** (drawn lines) ≠ ESRB **€4bn** (identified exposure). ⛔ **NOT claiming the exposure is LARGER** — it is *unquantifiable*: a known-unknown, not a direction. **Routed → LIQUID, REGINALD, PROME.**

**🔴 TWO FAIL-CLOSED RULES REGISTERED, both written BEFORE they bind.**
- **`T-08` EXIT (owed #9)** — it had **none**, so an open fire had no way to close. Now **inside −12pp for 5 consecutive gas days**; hysteresis −15 fire / −12 exit = a **3pp dead band ≈10× the cross-source error**. ⛔ **A blind gas day never counts toward an exit**; ⛔ **no exit on the cross-source basis** (9/10 proved 0.3pp sits inside the error). **Consequence recorded: until the AGSI key lands, `T-08` cannot exit at all.**
- **`HNS-07` PRE-COMMITTED RE-MARK RULE (owed #12)** — registered **43 days before the resolver**, which is the point. Checkpoints **10/01 · 10/15 · 10/25**; triggers: required pace > season's best trailing-14d pace (→≤35%), instruments converging off the straddle (→80%/30%), 5+ days net withdrawal pre-10/25 (→≤20%), arithmetic kill (resolve MISS early). ⛔ **ANTI-CHASE: drift *inside* the range my two instruments already straddled is NOT a trigger — that is what 65% priced.** Anchor **0.249 pp/d required** vs **~0.21 observed**.

**🔴 A BANKING VECTOR HAD BEEN MEASURING A BROAD INDEX FOR THREE WEEKS.** `VX-HANS-5.01` carried **Euro Stoxx 50** (~6,486) against bands **240/210/180** built for **SX7E** (~268) — it could not fire and was not measuring bank stress `[[finding_instrument_measures_a_superset_of_the_thesis_subject]]`. Restored to **SX7E 313.44 [9/18]**; independent 313.96, **deltas agree** (−2.25 / −2.08). 52-wk **224.58–322.11**, +36% y/y. ⚠️ **GREEN here is a weak negative, not corroboration** — equity near a 52-wk high cannot confirm the absence of an exposure the supervisor says it cannot quantify.

**STALE ROWS CLEARED — boot §[6] had 5 over 21d, now 0:** **`8.05`** 89d → **−1.6% YoY** (Destatis `PE26_316_421`, rel. 9/7), the basis the row wants; **GREEN→YELLOW**, 0.4pp off Orange — ⚠️ **the hard data is contracting YoY while the surveys drive the fifth-refutation growth picture; do not let the PMI read silence it.** · **`4.09`** the named artifact was found and **PARTLY REFUTES the claim that created the row** — AHDB 8/28: wheat **−12%** and spring barley **−19%** vs 5-yr, but winter barley **in line** and OSR **+19%**; **not a uniform failure**, "food shortages within months" unsupported; alarm **DOWN**, confidence LOW→MEDIUM; the falsifier is **`T-17`**. · **`11.04`** **FROZEN OUT-OF-SCOPE** → HAWK/BRENT (65d stale at RED — a stale RED implies someone is watching when nobody is; ⚠️ do not cite 42.7% as current). · **`4.07`** reviewed, unchanged at 503 — an **annual-programme construct**, so a 22d flag is a **cadence mismatch, not rot**; next real move **12/17**.

⚖️ **FOR WILL — one free API key now gates TWO instruments.** `AGSI_API_KEY` (free, `agsi.gie.eu/account`, ~2 min) → `FORGE/tools/market-data/.env`. Without it **`T-08` cannot exit** and **`HNS-07`'s re-mark rule cannot be evaluated**. Both fail *safe* — nothing reads "all clear" — but both are blind. Escalated via PROME.

**STATUS rotated 9/19, two passes, 91% → 74% of budget** → `workbook/STATUS_ROTATED_2026-09-19.md` (sessions 1–3 digests, post-commit audit, discharged owed rows, pre-compaction SAUDI + INBOX — all verbatim; **union censused and byte identity checked**, because rotation success and failure look identical from the byte count alone `[[finding_anchor_splice_deletes_everything_between_nested_anchors]]`). ⚠️ **STOPPED AT 74%, BELOW THE 75% TRIGGER BUT ABOVE RULE 5's <70% STOP — and that is a judgement, not an oversight.** Everything still in this file is live state (current levels, open fires, the prediction book, the owed board). Cutting further would mean deleting live content from the desk's primary memory to hit a byte target. **Flagging rather than doing it:** if the rule is meant to bind absolutely, the fix is a hot/cold split of STATUS, not more shaving — that is a structural change I have not made unilaterally.

---

## 🔴 SESSION 1 (9/18) — THE THREE LIVE READS, COMPACTED. **Verbatim → `workbook/STATUS_ROTATED_2026-09-19.md` + each block file.**

**① BoE 9/17 — THE BANK STOPPED SELLING LONG GILTS** → `workbook/2026-09-18_BOE_APF_BLOCK.md` · `KB-HANS-064`
Rate HELD **3.75%**. Of **£488.2bn** APF: **£222bn** pre-2035 and **£120bn** longest-dated held to maturity, **£146bn under review**, sales **£20bn/yr**, **auctions PAUSED** pending an Apr-2027 decision on selling gilts direct to Government. 🔴 **A SUPPLY WITHDRAWAL, NOT A DEMAND RECOVERY.** **Both UK thresholds moved AWAY; neither ever fired — no exit to record.** The 11/26 Budget now arrives with the long end's biggest seller stood down.

**② FED HIKED 9/16 — REFUTING A MECHANISM I PUBLISHED 9/10** → `workbook/2026-09-18_FED_HIKE_REFUTATION_BLOCK.md` · `KB-HANS-065`
+25bp to **3.75–4.00%**, 12–0. I wrote the differential compresses on a Sept ECB hike into a Fed on HOLD: **unchanged at 137.5bp and the euro WEAKENED to 1.1489 — both halves failed.** ⇒ **Exclusion leg (2) must be RE-ARGUED (owed #13).** 🔴 **Near-miss:** a stale-flag on `VX-HANS-4.03`=137.5 was correct at their read, then the Fed moved both legs back to exactly 137.5 — **recompute from BOTH primaries; never accept a supplied delta** → `ML-HANS-451`

**③ FRANCE — `T-10` NEAR-TRIGGER, GRADED INSIDE MY OWN BASIS GAP** → `workbook/2026-09-18_FRANCE_T10_BLOCK.md` · `KB-HANS-066`
**OAT–Bund 96.8bp [9/18], a 1-yr high; OAT 4.47 / Bund 3.50. `T-10` (spread >100 AND OAT >4.50) NOT FIRED — 3.2bp and 3bp under.** 🔴 **TE-minus-TE the same day reads 105.5bp / 4.5735 and clears BOTH legs** — both trip lines sit **inside my ~10bp OAT basis gap** (owed #5). **Fiscal:** 2027 budget targets **5.0% of GDP vs ~5.4% in 2026** (worse than the 4.7% carried). 🔴 **France yields MORE than Italy** and sold **−$62.4bn of USTs across June–July.**

## ENERGY — STORAGE RE-WIDENED THROUGH THE BAND. **Full block** → `workbook/2026-09-18_SESSION1_ENERGY_ECB_READS.md`

| Metric | Latest | Ladder / band | Source ✓ |
|---|---|---|---|
| **TTF front-month** | **€79.38/MWh (9/18, +3.96%)** — still ~+125% YoY | **L2 ORANGE (€66) OPEN**; L3 (€100) ~26% away | own `fetch.py` ✓ 9/18 |
| **EU storage gap to 5-yr norm** 🔴 | **−19.7pp** (68.3% fill vs 88.0% norm) — **RE-WIDENED back through −15pp** from −14.7pp [9/8] | 🟠 **`HANS-F-004` OPEN** | GEF/AGSI+ derived ✓ ~9/18 |
| EU storage fill | **69.06% / 781.50 TWh (9/18)** ⚠️ **a different gas day from the gap's 68.3% leg — do NOT merge** | not the binding metric | GEF ✓ 9/18 |
| Refill pace | **~+0.21pp/d** — **BELOW** the ~0.29–0.30pp/d carried and below the rate for 80% by Nov 1 | 🔴 **`HNS-07` at risk** | GEF ✓ 9/18 |

✅ **THE 9/10 RULING IS VINDICATED.** WALTER asked whether −14.7pp exited the fire; I ruled **NOT AN EXIT** — 0.3pp was inside the cross-source error. **Ten days later: −19.7pp** `[[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]`.
✅ **9/19: the exit condition is now REGISTERED** (§SESSION 4, owed #9) — but the gap is still **cross-source** (AGSI fill − GEF norm) and ⚠️ **AGSI+ is UNINSTRUMENTED on this box**, so **`T-08` cannot exit until the key lands**, by design. Today's fill is **secondary**; AGSI+ was reachable from the other machine on 9/10 — **re-check per box.**
**Structural:** Hormuz shut ~6 months · **Qatar LNG force majeure into November** (−96%) · **LNG cannot be STS-transferred through Hormuz the way crude can.** ⚠️ **EU gas and US crude share Hormuz — ONE WITNESS, TWO READOUTS.** *(→ `FLOW-HANS-8`.)*
**9/19 boot pull:** TTF **€79.52** (L2 ORANGE still OPEN, no rung crossed) · EUR/USD **1.15** · DXY **100.22** · euro-area AAA 10Y **3.488% [9/17]**. Market closed Sat — these are Friday closes, no new fire.

### 🔴 SAUDI CRUDE TO EUROPE — **full block** → `workbook/2026-09-18_SAUDI_EUROPE_BLOCK.md` · `HANS-T-15` · `KB-HANS-073`–`083`

**Aramco told European TERM customers ZERO October crude — all of them** (Bloomberg 9/18). **Petroline, the ~7 mb/d Hormuz BYPASS, drone-struck 9/10**; nothing out of Yanbu since 9/11; repair 4–6 weeks. 🔴 **Both Saudi export routes impaired at once.** ⛔ **PRINCIPAL-UNCONFIRMED — Aramco declined comment, no force majeure on any leg.**
🔑 **Concentration, not aggregate: ~577 kb/d ≈ 4–5% of European runs, replaceable at a price — but Orlen runs Saudi at ~40–50% of slate** ⇒ **a slate-and-differentials event, not a volume shortfall.**
⚠️ **MY "Brent −5.8% on the day" WAS A CONTRACT-ROLL ARTIFACT AND IS WITHDRAWN.** At named November: **108.75 [9/15] → 103.21 [9/18] = −5.09% over three sessions.** **The three-session fade survives; the same-day claim is dead.** Corrected to BRENT, HENRY, PROME.
🔴 **SAME CLASS ON MY OWN OPEN FIRE:** boot's generic `TTF=F` → **`TTFV26.NYM`, October, expires 9/29** — **rolls inside two weeks on a LEVEL ladder.** Contract now named in `T-07`.
🆕 **Against my own alarm: TTF is BACKWARDATED into winter** (Dec 75.78 / Jan 75.61); with storage −19.7pp the textbook shape is winter *contango*. **The curve is not pricing a winter crisis.** Untested → `KB-HANS-080`.

## ECB / EURO-AREA MACRO — THE GROWTH LEG TAKES A FIFTH REFUTATION

| Metric | Latest | Source ✓ |
|---|---|---|
| Deposit / refi / marginal | **2.50 / 2.65 / 2.90%** — hiked 9/10, **in effect 2026-09-16** | ECB `mp260910` ✓ primary |
| Next GovC | **2026-10-29** (NL election same day), then 12/17. **`T-04` fires at ≥2.75 — one hike away** | ECB calendar ✓ primary |
| EA HICP (Aug) **FINAL** | **3.2%** (Jul 2.9%) — energy **14.3%**, services 3.0%, **core 2.4% UNREVISED**. ⚠️ I carried the **3.3% flash** 17d | Eurostat `2-17092026-AP` ✓ primary |
| German CPI (Aug) · ifo | **2.9%** (energy **10.5%**) · ifo **88.8**, up from 86.7 | Destatis · ifo ✓ |
| German IP | **−1.1% m/m (Jul)** — ⚠️ `VX-HANS-8.05` wants **YoY**, stays stale deliberately: a basis mismatch is worse than stale | Destatis ✓ |

🔴 **FIFTH REFUTATION OF MY BELOW-CONSENSUS GROWTH LEG** — German institutes **raised** forecasts early Sept; **ifo autumn (9/3), GDP +1.4% 2026**; the ECB revised growth up for 2026 **and** 2027; France Q2 **+0.2%** vs my "stagnated"; EA Q2 **+0.4%**; all three August PMI finals revised **up**. **Five independent refutations is not bad luck — the leg is wrong and the ISM-weakness transmission it fed is dead.** `T-02` stays correctly OPEN → `KB-HANS-067`

**European banks: no stress. `T-14` NOT firing on a CURRENT dated sweep (9/18, re-checked in session 2)** — no G-SIB warning tied explicitly to private-credit losses, no ECB/ESRB warning **naming** institutions; the ESRB taskforce is **EXAMINING** the ~$3.1tn sector, and **an examination is not a naming warning.** FSR primary: **€62.5bn drawn, 12 banks = 0.2% of assets.** ✅ **ESRB `report202602` READ AT PRIMARY 9/19 — embargo discharged, routed; it does NOT fire `T-14`, but see §SESSION 4: it says the exposure cannot be quantified** → `KB-HANS-068`, `090`–`093`


## 🆕 SESSION 3 (9/18) — DESK SWEEP, ALL ITEMS WORKED. **Rotated 9/19 → `workbook/STATUS_ROTATED_2026-09-19.md`** · full block `workbook/2026-09-18_SESSION3_DESK_SWEEP.md` · `ML-HANS-459`–`463`. Headline: **core inflation gained a surface (`4.11`/`4.12`, `T-16`/`T-17` as FALSIFIERS), two policy vectors pointed the wrong way, `doc_audit` gained C10+C11, and three defects I introduced while fixing were caught by the new tests → RULE #1d.**

## SESSION 2 (9/18) — NEWS CATCH-UP. **Rotated 9/19 → `workbook/STATUS_ROTATED_2026-09-19.md`** · full block `workbook/2026-09-18_SESSION2_NEWS_CATCHUP.md` · `KB-HANS-084`–`088`. Headline: **the overshoot has NO CORE LEG on either side of the Channel** — UK CPI 3.1% with core 2.6% and services 3.4% both UNCHANGED (all motor fuels +23.0%); EA HICP final 3.2% with energy +14.3% = 1.29pp and **core 2.4% UNREVISED**. ⇒ **`T-04` is NOT a hawkish lean into 10/29.** Plus **TIC July** (8 vectors refreshed; France **−$62.4bn** over two months, UK **+$58.4bn** to 998.3, total 9,248.1 lowest since Oct-2025) and **German 2027 debt service €41.8bn vs €30.3bn, +38% in one year.**

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

**Open fires: 4 of 17 — `T-02` · `T-05` · `T-07` · `T-08`. No new fire; the one that nearly happened (`T-10`) is above. 🆕 `T-15` Saudi-crude-to-Europe REGISTERED 9/18** (see §SAUDI). 🔴 **`T-12` (EUR/USD 3M basis) remains UNINSTRUMENTED and cannot fire at all — excluded from any clean-board count.** A clean scan of the 6 daily-scannable rows does not clear the 17.

---

## PREDICTIONS

| ID | Prediction | Conf | Resolves | State 2026-09-18 |
|---|---|---|---|---|
| **HNS-06** | German Mfg PMI **≥50.0**, Sept flash | **80%** | **9/23 rel.**, `Resolve_By` **9/25** | 🟢 **ON TRACK.** The two dates are not drift: 9/25 absorbs ±2d flash slip (`Anchor_Type` EXPECTED-RELEASE). ⚠️ **GRADE THE FLASH** — grading the final ~10d later is the mirror image of the 9/5 error |
| **HNS-07** | EU storage **≥80%** by Nov 1 | **65%** | 2026-11-01 | 🔴 **AT RISK.** From 69.06% [9/18], 44d at the observed **+0.21pp/d → ~78.3%, a MISS**; at the carried +0.30 → ~82.3%, a HIT. ⚠️ **Not re-marked** — 65% was set *because* the two instruments straddled the line. ✅ **The pre-committed rule now EXISTS (9/19)** — see §SESSION 4 |
| **HNS-08** | Bund does **NOT** close ≥4.00% before Dec 31 | **70%** | 2026-12-31 | 🟢 **OPEN.** Buffer ~48–50bp; MISS the instant it **closes** ≥4.00 |
| **HNS-09** | No large euro-area bank reports a Q3-2026 materially private-credit-driven loss | **70%** | 2026-11-30 | 🟢 **OPEN — same number, NEW BASIS 9/19.** Not "the sweep is clean" (clean over a blind perimeter) but **structural: euro-area banks are net DEBTORS to NBFI, so the credit channel is small by construction.** Q3 results the live window |

**7/16 book: 2 HIT, 1 MISS** · `HNS-05` ✅ HIT 9/10 — outcome HIT, **rationale FAIL**.
🔴 **CALIBRATION:** *my HITs are momentum continuations; my one MISS was the only call requiring a TURN.* **`HNS-07` is the live test of whether I re-mark a straddling call that drifts against me.**

---

## CATALYST DOCKET

| Date | Event | Pri |
|---|---|---|
| **2026-09-23** 🔴 | **German/EA flash PMI (Sept) 07:30 UTC** — `HNS-06` resolver. **Grade the FLASH.** EA HICP flash **10/1** | 🔴 |
| **2026-09-28/29** 🔴 | **`NG=F` / `TTF=F` rolls** — `T-07` is a LEVEL ladder with L1+L2 fired; **never grade a rung crossing across a roll** | 🔴 |
| **early Oct 2026** 🔴 | **France submits the 2027 budget** — OAT–Bund at a 1-yr high, `T-10` legs ~3bp out | 🔴 |
| **2026-10-29** 🔴 | **ECB GovC — `T-04` (≥2.75) one 25bp hike away**, but 🆕 **no longer a hawkish lean** (core unrevised, Lagarde on energy). NL election same day | 🔴 |
| **~early Nov 2026** 🔴 | **Hormuz / Qatar force-majeure next extension** | 🔴 |
| **2026-11-01** | `HNS-07` resolves (storage ≥80%) — in the Oct 1–Dec 1 compliance window | 🟠 |
| **2026-11-26** 🟠 | **UK Autumn Budget** — **the LDI date, with the long-end seller now stood down ahead of it** | 🟠 |
| **by Apr 2027** | **BoE: sell gilts direct to Government?** (£146bn in review) | 🟠 |
| **2027-01-01** | EU ban on Russian LNG long-term contracts — bites inside the `HNS-07` winter | 🟠 |
| Sep–Dec 2026 | **German 2027 budget in parliament** — €118.7bn core NKA / €203.6bn all-in; **debt service +38%** | 🟠 |

---

## 📬 INBOX / CROSS-AGENT FLAGS — **inbox lanes CLEAR** (session 1; not re-processed s2–s4, per MAIL rule). 🔴 **The LIVE flag table is `DISPATCH_LOG.md`, not this line.** Session-1 dispositions → `workbook/2026-09-18_INBOX_DISPOSITIONS.md`; session-1 flags (BOND/TERRY · BRENT/HENRY · HENRY · HAWK · WALTER · DAEDALUS · LIQUID/REGINALD · PROME) carry their 9/18 rows there.

🆕 **DISPATCHED 9/18** → `BOND` (🟠 `T-04` no longer a hawkish lean into 10/29; German debt service +38% y/y on the common-mode LEVEL channel) · `ZHAO` (🟠 TIC July: France −$62.4bn over two months, UK +$58.4bn to ~$1tn).
🆕 **DISPATCHED 9/19** → `LIQUID` + `REGINALD` (🟠 ESRB primary read) · `HAWK` + `BRENT` (🟡 orphaned `VX-HANS-11.04`) · `PROME` (🟠 ESRB + ⚖️ the AGSI-key escalation). ⚠️ **Verify at the recipient tree, never here.**

## NEXT SESSION — WHAT IS OWED

🔴 **FIRST: `python3 scripts/doc_audit.py`** (RULE #1b) — **see owed #15: it reads clean over surfaces it does not scan.**
🔴 **SECOND: the CONTRACT ROLL lands 9/28 (`NG=F`) / 9/29 (`TTF=F`).** `KB-HANS-079`/`081` expire **9/25** so boot raises it **before** the roll. **`T-07` is a LEVEL ladder with L1+L2 FIRED: never grade a rung crossing across a roll.**
⚠️ **Closeout 1c has TWO forms; `--self` is the only one seeing figures I superseded.** ⛔ **Residual 13 NOT to be cleared** — silencing a graded row resolves a flag backwards → `ML-HANS-456`.

| # | Owed | Due |
|---|---|---|
| 3 | **`HNS-06`** — German Mfg PMI ≥50.0, **9/23 07:30 UTC**. **Grade the FLASH** | **2026-09-23** |
| 5 | 🔴 **TWO BASIS GAPS, one DECIDES A THRESHOLD.** (a) **OAT ~10bp** — both `T-10` trip lines sit inside it. (b) **UK 10Y** BoE `IUDMNPY` vs TE. **Pin both before either is cited** | 🔴 |
| 5b | **No free DAILY CLOSE gilt source.** Lead: DMO `ExportReport?reportCode=D4H`, needs a form POST | open |
| 8 | ⚖️ **ESCALATED 9/19 — `AGSI_API_KEY` now gates TWO instruments** (`T-08` exit + `HNS-07` re-mark rule), not just boot §[2]. Free, ~2 min. **Will-facing ask, via PROME** | 🔴 |
| 13 | **Re-argue exclusion leg (2)** — the Fed hike killed the euro-strength mechanism | open |
| 14 | **Split `VX-HANS-11.03`** into (a) German annual outlay and (b) a real EU issuance series with matching bands | 🟠 |
| 15 | 🔴 **`doc_audit` C2 still does NOT scan `STATUS.md`** — registry and `VX.tsv` only. C9 owed, reusing C8's citation detector → `ML-HANS-459` | 🔴 |
| 16 | **`VX-HANS-1.07` Germany UST** — sought at TIC primary, **not in Table 5**; keeps `1.08` mixed-vintage. Find it or retire the aggregate | 🟠 |

## 🔴 POST-COMMIT AUDIT (session 1) — 5 DEFECTS IN MY OWN WORK, ALL FIXED. **Rotated 9/19 → `workbook/STATUS_ROTATED_2026-09-19.md`** · verbatim `workbook/2026-09-18_POST_COMMIT_AUDIT.md`. The one that must not be re-learned: **I minted status tokens without opening `STATE_VOCABULARY.md` and two of my own guards then read one column with different semantics** → `ML-HANS-452`, RULE #1c. ⚠️ **UNFIXED: the ECB pull is INTERMITTENT — a blank boot §[2] is not a quiet board.** ⚠️ **STANDING PRIOR, now EIGHT sessions: every defect on this desk is found from OUTSIDE or by a script, never by re-reading** — session 4 holds: the ESRB finding came from reading a primary I had been deferring, and the `5.01` broad-index defect came from a staleness scan, not from re-reading STATUS.

## TWO-SENTENCE SUMMARY

🆕 **Session 4's sharper one:** the ECB and ESRB jointly say supervisors **cannot quantify** euro-area bank exposure to private credit — they found €4bn, called it far below what supervisory intelligence implies, and dropped the category — so my `T-14` row, which waits for a regulator to *name* institutions, has been reading clean over a perimeter its own author calls blind; **the offset is that euro-area banks are net borrowers from the non-bank sector, not net lenders to it, so Europe's exposure is to losing that funding in a stress rather than to credit losses on private credit.**

**The Bank of England stopped selling long gilts** — auctions paused, £222bn pre-2035 and £120bn of the longest-dated held to maturity out of £488.2bn — which moved both my UK thresholds *away* from their bands, **but it is a supply withdrawal and not a demand recovery**, and the 11/26 Budget now arrives with the long end's biggest seller stood down. **Session 2 says why it could, and it cuts against my own ECB call:** UK CPI accelerated to 3.1% the day before the hold and euro-area HICP finalised at 3.2%, **yet on both sides of the Channel the entire overshoot is energy and core did not move** — so `T-04` is no longer a hawkish lean into 10/29, and **the one new number to carry forward is German debt service: €41.8bn in 2027 against €30.3bn in 2026, +38% in a year, the Bund at a 15-year high arriving inside the budget.**

---
*Archives → `workbook/`. Falsification → `thesis/KILL_TREE.md`. Flags → `DISPATCH_LOG.md`. Bands → `registry/`.*
