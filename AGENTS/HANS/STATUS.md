# HANS STATUS.md
**Updated:** 2026-09-19 (Sat, market closed) — **narrative for this session lives in `SESSION_LOG.md`; below is state only.** **(owed-board catch-up + CATO correction pass): THE ESRB REPORT IS READ AT PRIMARY AND IT SAYS THE SUPERVISOR CANNOT SEE THE EXPOSURE MY OWN FIRE ROW WAITS ON.** Two fires/predictions got fail-closed exit rules; a BANKING vector had been measuring a broad index for three weeks. Sessions 1–3 digested below; every block has a verbatim file.
**Boot:** rc1 · `doc_audit.py` **0 findings** · **67 tests OK** · R1 **rc=0** · mail lanes not processed (normal spawn). I own **`EUROPE_MACRO`** (BOND = time-critical backup). **UK leg: MINE.**

---

## 🔴 CARRY FORWARD — the live consequences of 2026-09-18/19. **Narrative → `SESSION_LOG.md`** · verbatim → `workbook/`

**Conclusions that change what the next session does.** The how is in `SESSION_LOG.md`; every item below is load-bearing.

- 🔴 **`T-14`'s SILENCE MEANS LESS THAN IT LOOKS.** ESRB `report202602` read at primary 9/19: identified bank exposure to private equity/private credit is **€4bn**, which the report calls *"far below the figures implied by supervisory intelligence"* before **dropping the class from its analysis**; leverage there *"cannot be computed from existing data"* and the non-EU gap is *"likely to remain"* after reform. **`T-14` is NOT fired and this does not fire it** — but leg (b) waits for a supervisor to NAME institutions, which is downstream of that supervisor being able to SEE the exposure. **Band unchanged, deliberately not re-tuned.** → `KB-HANS-090`–`092`, `ML-HANS-464`
- 🔑 **`HNS-09` keeps 70% on a NEW BASIS:** euro-area banks are aggregate **NET DEBTORS** to NBFI (~15% of balance sheets) where US banks are net lenders ⇒ **FUNDING is the dominant euro-area route.** ⛔ **It does NOT bound the credit channel** — a net position says nothing about GROSS exposure, and the same report puts asset-side NBFI exposure at **~10% of SI assets, ~a quarter to potentially leveraged entities**. ⚠️ **Two perimeters never merged:** FSR **€62.5bn drawn** ≠ ESRB **€4bn identified**. ⛔ **Not claiming the exposure is larger — it is unquantifiable.**
- ⛔ **THE STORAGE GAP MOVED −19.7 → −15.99pp AND THAT IS A BASIS CORRECTION, NOT A RECOVERY** (~80% denominator: norm 88.0 → an AGSI-native 85.05; fill moved +0.76pp). **`HANS-F-004` STAYS OPEN**, 1.0pp inside its band. **Anyone reading the direction as good news is reading it wrong.** → `KB-HANS-094`
- 🔴 **AGSI: a REJECTED KEY RETURNS HTTP 200 + AN EMPTY ARRAY**, identical to an unpublished gas day — and since the norm is now AGSI-native a dead key blinds **both legs**. `fetch_eu` discriminates (KEY REJECTED / no-data / BLIND); **quirk-dependent, re-check 2026-12-19** (owed #22). → `KB-HANS-095`
- ⚠️ **`VX-HANS-5.01` held EURO STOXX 50 against SX7E bands for 3 weeks** — could not fire; C10/C11 both passed. Now **SX7E 313.44**. **GREEN there is a weak negative, not corroboration.** LEVEL two-source; 52-wk range/YTD single **secondary**. → `KB-HANS-093`, `ML-HANS-465`
- ⚠️ **`HNS-07` anchor corrected 9/19:** 45d from **gas day 9/17**, required **0.2431 pp/d** vs **0.22 observed** (was 9/18/44d/0.249). **Verdict unchanged, MISS-side.** → `ML-HANS-471`
- 🆕 **Instruments:** `doc_audit` **13 checks** (C9 prose-superseded · C12 key-uniqueness · C13 value/band scale), **86 tests**. **`8.05` German IP −1.6% YoY GREEN→YELLOW** — hard data contracting while surveys drove five refutations of the growth leg; **do not let the PMI read silence it.** **`4.09` UK food: AHDB partly REFUTES the claim that created the row** (wheat −12%, spring barley −19%, but winter barley in line, OSR **+19%**) — alarm marked down.
- ⚠️ **STANDING PRIOR, NINE sessions: every defect here is found from OUTSIDE or by a script, never by re-reading.** 9/19 held five times — a deferred primary, a staleness scan, a new API key, a peer's negative control, and an operator asking me to double-check.

## ENERGY — STORAGE RE-WIDENED THROUGH THE BAND. **Full block** → `workbook/2026-09-18_SESSION1_ENERGY_ECB_READS.md`

| Metric | Latest | Ladder / band | Source ✓ |
|---|---|---|---|
| **TTF front-month** | **€79.38/MWh (9/18, +3.96%)** — still ~+125% YoY | **L2 ORANGE (€66) OPEN**; L3 (€100) ~26% away | own `fetch.py` ✓ 9/18 |
| **EU storage gap to 5-yr norm** 🔴 | **−15.99pp** — ⛔ **A BASIS CORRECTION, NOT A RECOVERY** (norm 88.0→85.05 gave +2.95pp of the +3.71; fill only +0.76) | 🟠 **`HANS-F-004` OPEN**, by 1.0pp | **AGSI+ SINGLE-SOURCE** ✓ 9/19 |
| EU storage fill | **69.06% / 781.50 TWh — gas day 2026-09-17** (both legs now the SAME gas day) | not the binding metric | **AGSI+ primary** ✓ 9/19 |
| Refill pace | **+0.22pp/d** (AGSI direct) — **BELOW** the ~0.29–0.30 carried and below the rate for 80% by Nov 1 | 🔴 **`HNS-07` at risk** | **AGSI+ primary** ✓ 9/19 |

✅ **THE 9/10 RULING IS VINDICATED.** WALTER asked whether −14.7pp exited the fire; I ruled **NOT AN EXIT** — 0.3pp was inside the cross-source error. **Ten days later: −19.7pp** `[[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]`.
✅ **9/19 LATE — WILL PROVISIONED THE AGSI KEY AND THE PICTURE CHANGED TWICE.** The exit condition (owed #9) is registered AND its single-source precondition is now satisfied. 🔴 **But the first single-source pull found the instrument had been wrong in BOTH directions:** my carried **−19.7** used a GEF **88.0** norm; `fetch_eu.py` carried a **hardcoded 82.0 frozen on 2026-08-28** and printed **−12.9**. The AGSI-native truth is **−15.99** (fill 69.06% [gas day 09-17] vs an AGSI norm of **85.05%** = mean of 09-17 across 2021–25; median basis −16.61). 🔴 **The frozen constant was the dangerous one: the true norm RISES through the injection season, so a frozen denominator makes the gap read BETTER as time passes — fail-OPEN drift, and it had the fire on the wrong side of its own −15 band.** Fixed: `agsi_norm()` computes the norm from AGSI history and **fails closed — no norm ⇒ NO GAP PRINTED**, never a constant fallback. → `ML-HANS-467`, `KB-HANS-094`
⛔ **DO NOT READ −19.7 → −15.99 AS IMPROVEMENT.** ~80% of it is the denominator. **The fire stays OPEN** by 1.0pp (mean) / 1.6pp (median). 🔑 **AND A SECOND FAILURE MODE, from PROME's negative control, verified by reproducing it:** **a REJECTED AGSI key returns HTTP 200 with an EMPTY array — shape-identical to an unpublished gas day**, so silent expiry prints exactly the message that means *come back tomorrow*, and a desk defers its checkpoint forever. **Now that the norm is AGSI-native a dead key blinds BOTH legs.** Wired a discriminator (empty-`x-key` probe ⇒ KEY REJECTED vs genuine no-data vs BLIND), quirk-dependent with a **re-check date 2026-12-19** and failing in the safe direction → `KB-HANS-095`.
⚠️ **I nearly refuted that control with a probe that never left my machine** — `curl -H "x-key: "` DROPS the header, so I silently re-tested the ABSENT case and got a reproducible wrong answer twice. **Reproducibility did not rescue it; varying the client did** → `ML-HANS-468`. An injection test then found **two key-resolution paths** I had created an hour earlier → `ML-HANS-469`.
⚠️ **OPEN, NOT A DEFECT (`KB-HANS-096`, due Tue 9/22):** AGSI lag may be **D+2, not D+1**. One Saturday observation cannot separate that from a weekend schedule. **It touches `HNS-07`'s grading date** (11/02 vs 11/03) — the resolver gas day itself does not move.
✅ **This morning's fail-closed exit clause earned itself on its first live pull** — had I taken the cross-source −12.9, the row would have looked 2.1pp from an exit on a norm AGSI's own history contradicts.
**Structural:** Hormuz shut ~6 months · **Qatar LNG force majeure into November** (−96%) · **LNG cannot be STS-transferred through Hormuz the way crude can.** ⚠️ **EU gas and US crude share Hormuz — ONE WITNESS, TWO READOUTS.** *(→ `FLOW-HANS-8`.)*
**9/19 boot pull:** TTF **€79.52** (L2 ORANGE still OPEN, no rung crossed) · EUR/USD **1.15** · DXY **100.22** · euro-area AAA 10Y **3.488% [9/17]**. Market closed Sat — these are Friday closes, no new fire.

### 🔴 SAUDI CRUDE TO EUROPE — **full block** → `workbook/2026-09-18_SAUDI_EUROPE_BLOCK.md` · `HANS-T-15` · `KB-HANS-073`–`083`

**Aramco told European TERM customers ZERO October crude — all of them** (Bloomberg 9/18). **Petroline, the ~7 mb/d Hormuz BYPASS, drone-struck 9/10**; nothing out of Yanbu since 9/11; repair 4–6 weeks. 🔴 **Both Saudi export routes impaired at once.** ⛔ **PRINCIPAL-UNCONFIRMED — Aramco declined comment, no force majeure on any leg.**
🔑 **Concentration, not aggregate: ~577 kb/d ≈ 4–5% of European runs, replaceable at a price — but Orlen runs Saudi at ~40–50% of slate** ⇒ **a slate-and-differentials event, not a volume shortfall.**
⚠️ **MY "Brent −5.8% on the day" WAS A CONTRACT-ROLL ARTIFACT AND IS WITHDRAWN.** At named November: **108.75 [9/15] → 103.21 [9/18] = −5.09% over three sessions.** **The three-session fade survives; the same-day claim is dead.** Corrected to BRENT, HENRY, PROME.
🔴 **SAME CLASS ON MY OWN OPEN FIRE:** boot's generic `TTF=F` → **`TTFV26.NYM`, October, expires 9/29** — **rolls inside two weeks on a LEVEL ladder.** Contract now named in `T-07`.
🆕 **Against my own alarm: TTF is BACKWARDATED into winter** (Dec 75.78 / Jan 75.61); with the storage gap at −15.99pp the textbook shape is winter *contango*. **The curve is not pricing a winter crisis.** Untested → `KB-HANS-080`.

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
| **HNS-07** | EU storage **≥80%** by Nov 1 | **65%** | 2026-11-01 | 🔴 **AT RISK.** From 69.06% [**gas day 9/17**], **45d** at **+0.22pp/d (AGSI direct) → ~78.96%, a MISS**; at the carried +0.30 → ~82.5%, a HIT. ⚠️ *Anchor corrected 9/19 late — the gas-day-vs-publication slip again; required pace is **0.2431**, verdict unchanged.* ⚠️ **Not re-marked** — 65% was set *because* the two instruments straddled the line. ✅ **The pre-committed rule now EXISTS (9/19)** — see §SESSION 4 |
| **HNS-08** | Bund does **NOT** close ≥4.00% before Dec 31 | **70%** | 2026-12-31 | 🟢 **OPEN.** Buffer ~48–50bp; MISS the instant it **closes** ≥4.00 |
| **HNS-09** | **At Q3-2026 European bank results: sector NII/earnings still holding with NO material rise in cost-of-risk** — **registered text, restored 9/19** | **70%** | 2026-11-30 | 🟢 **OPEN — same number, NEW BASIS 9/19.** Not "the sweep is clean" (clean over a blind perimeter) but **structural: euro-area banks are net DEBTORS to NBFI, so the credit channel is ** Q3 results the live window |

**7/16 book: 2 HIT, 1 MISS** · `HNS-05` ✅ HIT 9/10 — outcome HIT, **rationale FAIL**.
🔴 **CALIBRATION:** *my HITs are momentum continuations; my one MISS was the only call requiring a TURN.* **`HNS-07` is the live test of whether I re-mark a straddling call that drifts against me.**

---

## CATALYST DOCKET

| Date | Event | Pri |
|---|---|---|
| **2026-10-01 · 10-15 · 10-25** 🟠 | **`HNS-07` RE-MARK CHECKPOINTS** — evaluate rules (a)/(b)/(c) and nowhere else. ⛔ **No early resolution — rule (d) WITHDRAWN 9/19**; graded on the **11/01 gas day** | 🟠 |
| **2026-09-22** 🔴 | **AGSI lag D+1 vs D+2 — WEEKDAY check** (`KB-HANS-096`). Touches `HNS-07`'s GRADING date (11/02 vs 11/03), not its resolver | 🔴 |
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
| 5 | 🔴 **TWO BASIS GAPS, one DECIDES A THRESHOLD.** *(UK leg 9/19: BoE `IUDMNPY` is now a primary daily series, but the gap is still UNDECOMPOSED — 5.2421 [9/16] vs TE 5.29 [9/18] differ in date AND basis at once; needs SAME-DATE pairs.)* (a) **OAT ~10bp** — both `T-10` trip lines sit inside it. (b) **UK 10Y** BoE `IUDMNPY` vs TE. **Pin both before either is cited** | 🔴 |
| 5b | ✅ **DONE 9/19 — the claim was FALSE.** BoE IADB serves **daily, keyless** gilt yields; the CSV needs the `_iadb-` path prefix (the un-prefixed path returns **200 + the HTML landing page**). **UK 10Y and the BoE Bank Rate are now auto-pulled.** ⚠️ Lagged ~2–3 business days and a PAR-yield basis — both printed beside the level | ✅ |
| 8 | ✅ **RESOLVED 9/19 — Will provisioned `AGSI_API_KEY`.** Boot §[2] instrumented (rc1→**rc0**), `T-08` exitable in principle, `HNS-07` pace rules evaluable. **Immediately found a frozen-norm defect** → `ML-HANS-467` | ✅ |
| 13 | **Re-argue exclusion leg (2)** — the Fed hike killed the euro-strength mechanism | open |
| 14 | **Split `VX-HANS-11.03`** into (a) German annual outlay and (b) a real EU issuance series with matching bands | 🟠 |
| 15 | ✅ **DONE 9/19 — `C9` BUILT.** Scans the whole boot-read set, not just STATUS (widening it immediately found 2 stale figures STATUS-only would have missed). Band-suppressed after its first hit was FALSE; skips a self-declared statement-time record and says so | ✅ |
| 23 | 🟠 **`ML.tsv` KEY COLLISION — 475 rows, 324 unique IDs; 95 IDs shared by 246 rows with DIFFERENT findings.** All from the Feb-2026 bulk load; **none at ≥400**; whole-repo scan found **1** ambiguous citation (a completed artifact). **Not renumbered — append-only log, ~nil live harm.** ✅ **`C12` BUILT 9/19** — legacy backlog reported as a measured NOTE so it can never read clean, and a NEW collision (≥400) is a hard finding. **Renumbering still not done and still not planned** → `ML-HANS-473` | 🟠 |
| 20 | ✅ **DONE 9/19 — hot/cold split executed as its own task.** `SESSION_LOG.md` created; STATUS **85% → 67%**, under the <70% stop. Union censused, byte identity asserted. **Anti-regrowth guard `C14` added and falsified** | ✅ |
| 21 | **AGSI lag D+1 vs D+2 (`KB-HANS-096`)** — check on a WEEKDAY; touches `HNS-07`'s grading date (11/02 vs 11/03), not its resolver | **2026-09-22** |
| 22 | **Empty-key discriminator is VENDOR-QUIRK-DEPENDENT** — re-verify the negative control; if GIE tightened it, the probe reverts to always-empty (safe, but blind) | **2026-12-19** |
| 16 | **`VX-HANS-1.07` Germany UST** — sought at TIC primary, **not in Table 5**; keeps `1.08` mixed-vintage. Find it or retire the aggregate | 🟠 |

## TWO-SENTENCE SUMMARY

🆕 **Session 4's sharper one:** the ECB and ESRB jointly say supervisors **cannot quantify** euro-area bank exposure to private credit — they found €4bn, called it far below what supervisory intelligence implies, and dropped the category — so my `T-14` row, which waits for a regulator to *name* institutions, has been reading clean over a perimeter its own author calls blind; **the offset is that euro-area banks are net borrowers from the non-bank sector, not net lenders to it, so Europe's exposure is to losing that funding in a stress rather than to credit losses on private credit.**

**The Bank of England stopped selling long gilts** — auctions paused, £222bn pre-2035 and £120bn of the longest-dated held to maturity out of £488.2bn — which moved both my UK thresholds *away* from their bands, **but it is a supply withdrawal and not a demand recovery**, and the 11/26 Budget now arrives with the long end's biggest seller stood down. **Session 2 says why it could, and it cuts against my own ECB call:** UK CPI accelerated to 3.1% the day before the hold and euro-area HICP finalised at 3.2%, **yet on both sides of the Channel the entire overshoot is energy and core did not move** — so `T-04` is no longer a hawkish lean into 10/29, and **the one new number to carry forward is German debt service: €41.8bn in 2027 against €30.3bn in 2026, +38% in a year, the Bund at a 15-year high arriving inside the budget.**

---
*Archives → `workbook/`. Falsification → `thesis/KILL_TREE.md`. Flags → `DISPATCH_LOG.md`. Bands → `registry/`.*
