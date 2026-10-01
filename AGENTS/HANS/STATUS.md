# HANS STATUS.md
**Updated:** 2026-10-01 (Thu) — **PROME Tier-1 spawn (DOCKET L549, WQ-317): EU/UK rows shipped to BOND · 🔴 `T-10` DEEPENED to 130.3bp / 4.90 (France-idiosyncratic) and its EXIT is now registered · `T-13` UK 30Y closed 5.943, 6bp under, after an intraday touch of 6.03 · whole inbox drained.** *Prior:* 2026-09-25 (Fri) — **PROME Tier-1 spawn (WQ-294): `HANS-T-10` FRANCE FIRED 2026-09-24 (`HANS-F-006`), `HNS-06` graded HIT, whole inbox drained (17 items), TTF ladder pinned to a named contract.** *Prior:* 2026-09-19 (Sat, market closed) — **narrative for this session lives in `SESSION_LOG.md`; below is state only.** **(owed-board catch-up + CATO correction pass): THE ESRB REPORT IS READ AT PRIMARY AND IT SAYS THE SUPERVISOR CANNOT SEE THE EXPOSURE MY OWN FIRE ROW WAITS ON.** Two fires/predictions got fail-closed exit rules; a BANKING vector had been measuring a broad index for three weeks. Sessions 1–3 digested below; every block has a verbatim file.
**Boot:** rc1 · `doc_audit.py` **0 findings** · **67 tests OK** · R1 **rc=0** · mail lanes not processed (normal spawn). I own **`EUROPE_MACRO`** (BOND = time-critical backup). **UK leg: MINE.**

---

## 🔴 CARRY FORWARD — the live consequences of 2026-09-18/19, **9/25 and 10/01**. **Narrative → `SESSION_LOG.md`** · verbatim → `workbook/`

**Conclusions that change the next session's actions.** The how is in `SESSION_LOG.md`.

- 🔴 **10/01 — `T-10` DEEPENED, NOT EXITING: OAT–Bund 130.3bp / OAT 4.90** [i-i 17:35 CEST, +13.2bp d/d] — 111.2 [9/29] → 117.1 [9/30] → 130.3. **Composition (CORRECTED 10/01 12:3x on WALTER `-009`): NOT France-only.** The Bund RALLIED ~8–9bp [TE 3.4937 / CNBC 3.494] while BTP +6–7 and Bonos +2, so this was a flight-to-quality bid plus a broad periphery widening (spreads FR ~+17, IT ~+16, ES ~+10). i-i's Bund leg (3.60, +2) is contradicted by both vendors, so the spread level is uncertain between **130.3 (i-i) and ~143 (TE/CNBC)**; the state is MET either way (`KB-HANS-106`). ⛔ Cause is HEADLINE-ONLY (2027 budget presentation, a €54bn consolidation package). **EXIT REGISTERED (owed #24 closed): spread <90 AND OAT <4.40 on i-i, 5 consecutive sessions; a session back over a fire line resets the count.** Routed BOND + LIQUID. → `KB-HANS-100`
- 🟠 **10/01 — UK long end touched both lines intraday and closed under:** 30Y **5.943** [TE] (intraday high 6.0289 [CNBC]) is 6bp under `T-13`; 10Y **5.40** (intraday high 5.51) is 10bp under `T-06`. **The next close above 6.00 fires `T-13`. The 11/26 Budget is the LDI date.** → `KB-HANS-101`
- 🟡 **Rhine record low: German IP downside; may FLATTER the PMI headline** (delivery times). Read October output, not the headline. Sept final **53.9**, `T-02` MET. → `KB-HANS-103`
- 🔴 **9/25 — `T-10` FIRED 9/24 (`HANS-F-006`) at 109.9bp / 4.67** on the governing i-i basis, also firing on TE; ~11bp of the OAT move was common-mode Bund. **Full bullet → `SESSION_LOG.md` § STATUS ROTATION 2026-10-01.** → `KB-HANS-097`
- 🔧 **`T-07` now graded on NAMED `TTFV26.NYM` (L429 fixed)** — explicit calendar V26 9/29 → X26 10/29 → Z26 11/27 (**X/Z expiries COMPUTED from the ICE rule, re-verify**), no fallback to `TTF=F`, roll-window warning ≤3d. At 9/24–25 X26 ≈ €74 vs V26 €70.96 — the roll lifts the level ~€3, **crosses no rung** (L2 66 / L3 100).

- 🔴 **`T-14`'s SILENCE MEANS LESS THAN IT LOOKS.** ESRB `report202602` read at primary 9/19: identified bank exposure to private equity/private credit is **€4bn**, which the report calls *"far below the figures implied by supervisory intelligence"* before **dropping the class from its analysis**; leverage there *"cannot be computed from existing data"* and the non-EU gap is *"likely to remain"* after reform. **`T-14` is NOT fired and this does not fire it** — but leg (b) waits for a supervisor to NAME institutions, which is downstream of that supervisor being able to SEE the exposure. **Band unchanged, deliberately not re-tuned.** → `KB-HANS-090`–`092`, `ML-HANS-464`
- 🔑 **`HNS-09` keeps 70% on a NEW BASIS:** euro-area banks are aggregate **NET DEBTORS** to NBFI (~15% of balance sheets) where US banks are net lenders ⇒ **FUNDING is the dominant euro-area route.** ⛔ **It does NOT bound the credit channel.** Funding withdrawal and credit losses **co-occur** — the same counterparty stress drives both — and a net position says nothing about GROSS exposure: the report puts asset-side NBFI exposure at **~10% of SI assets, ~a quarter to potentially leveraged entities**. ⚠️ **Two perimeters never merged:** FSR **€62.5bn drawn** ≠ ESRB **€4bn identified**. ⛔ **Not claiming the exposure is larger — it is unquantifiable.**
- ⛔ **THE STORAGE GAP MOVED −19.7 → −15.99pp AND THAT IS A BASIS CORRECTION, NOT A RECOVERY** (~80% denominator: norm 88.0 → an AGSI-native 85.05; fill moved +0.76pp). **`HANS-F-004` STAYS OPEN**, 1.0pp inside its band. **Anyone reading the direction as good news is reading it wrong.** → `KB-HANS-094`
- 🔴 **AGSI: a REJECTED KEY RETURNS HTTP 200 + AN EMPTY ARRAY**, identical to an unpublished gas day; with an AGSI-native norm a dead key blinds **both legs**. `fetch_eu` discriminates (KEY REJECTED / no-data / BLIND); **quirk-dependent, re-check 2026-12-19** (owed #22). → `KB-HANS-095`
- ⚠️ **`VX-HANS-5.01` held EURO STOXX 50 against SX7E bands for 3 weeks** — could not fire; C10/C11 both passed. Now **SX7E 313.44**. **GREEN there is a weak negative, not corroboration.** LEVEL two-source; 52-wk range/YTD single **secondary**. → `KB-HANS-093`, `ML-HANS-465`
- 🟡 **10/01 post-delivery (dated, sourced):** LIQUID read T-10 at its side and found no US-funding transmission (its figures: SOFR99−IORB +9bp, SRF $1.2bn [9/30]; `ef013f618`). The EUR basis is unmeasured on both desks. DEWEY DR-4 re-run is registered **DOCKET L566 for 10/12**, so HNS-07 rule (b) is deferred and the mark stays 65%. **DOCKET L549 RESOLVED** by PROME (WQ-317 delivered; read corrected to periphery-wide). **T-12: ONE joint letter, PENDING Will, NOT registered.** PROME ruled LIQUID owns USAGE (`usd_swapline.py`); HANS keeps bidders ≥8 + daily-ops/tenor legs; my $1.5bn line withdrawn → `research/2026-10-01_T12_…`
- ⚠️ **STANDING PRIOR, TEN sessions: every defect is found from OUTSIDE or by a script, never by re-reading.** 10/01: WALTER `-009` caught the Bund-leg error.

## ENERGY — STORAGE RE-WIDENED THROUGH THE BAND. **Full block** → `workbook/2026-09-18_SESSION1_ENERGY_ECB_READS.md`

| Metric | Latest | Ladder / band | Source ✓ |
|---|---|---|---|
| **TTF front-month** | **€79.38/MWh (9/18, +3.96%)** — still ~+125% YoY | **L2 ORANGE (€66) OPEN**; L3 (€100) ~26% away | own `fetch.py` ✓ 9/18 |
| **EU storage gap to 5-yr norm** 🔴 | **−15.99pp** — ⛔ **A BASIS CORRECTION, NOT A RECOVERY** (norm 88.0→85.05 gave +2.95pp of the +3.71; fill only +0.76) | 🟠 **`HANS-F-004` OPEN**, by 1.0pp | **AGSI+ SINGLE-SOURCE** ✓ 9/19 |
| EU storage fill | **69.06% / 781.50 TWh — gas day 2026-09-17** (both legs now the SAME gas day) | not the binding metric | **AGSI+ primary** ✓ 9/19 |
| Refill pace | **+0.22pp/d** (AGSI direct) — **BELOW** the ~0.29–0.30 carried and below the rate for 80% by Nov 1 | 🔴 **`HNS-07` at risk** | **AGSI+ primary** ✓ 9/19 |

📦 **9/19 storage narrative ROTATED VERBATIM 9/25 → `SESSION_LOG.md` § STATUS ROTATION 2026-09-25.** Live consequences: CARRY FORWARD above, `KB-HANS-094`/`095`.
⚠️ **OPEN, NOT A DEFECT (`KB-HANS-096`, due Tue 9/22):** AGSI lag may be **D+2, not D+1**. One Saturday observation cannot separate that from a weekend schedule. **It touches `HNS-07`'s grading date** (11/02 vs 11/03) — the resolver gas day itself does not move.
**Structural:** Hormuz shut ~6 months · **Qatar LNG force majeure into November** (−96%) · **LNG cannot be STS-transferred through Hormuz the way crude can.** ⚠️ **EU gas and US crude share Hormuz — ONE WITNESS, TWO READOUTS.** *(→ `FLOW-HANS-8`.)*

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


## SOVEREIGN / FX BOARD — LEVELS 2026-10-01 unless dated

| Metric | Level | Band | Source ✓ |
|---|---|---|---|
| German 10Y Bund | **3.49** (TE/CNBC 10/01, −9bp: flight-to-quality) ⚠️ i-i 3.60 and Bundesbank 3.66 read UP, contradicted / ECB AAA **3.582** [9/30] | **>3.00 watch ✅FIRED** / >3.75 orange — **~26bp away** | ✓ 10/01 |
| France 10Y OAT | **4.90** (i-i, +15bp d/d) / CNBC **4.925** — highest since Jun-2002 [TE headline] | >4.50 level leg — **✅ MET, +40bp**; Red 5.00 is 10bp away | ✓ 10/01 |
| OAT–Bund spread | **130.3bp** i-i (suspect Bund leg) / **~143** TE-CNBC; 111.2 [9/29] → 117.1 [9/30] | >100bp — **✅ MET, `T-10` OPEN** · exit <90 AND OAT <4.40 ×5 | i-i GOVERNING ✓ 10/01 |
| Italy 10Y BTP | **4.696** (+6bp, 3-yr high) | >5.50 level leg — 80bp under | TE ✓ 10/01 |
| BTP–Bund spread | **120.2bp** ⚠️ TE-derived (~+16 d/d) | >200bp — 80bp under | ✓ 10/01 |
| UK 10Y gilt | **5.40** (−2bp); intraday high 5.51 [CNBC] | >5.50 orange — **10bp under on the close** | TE ✓ 10/01 |
| **UK 30Y gilt** | **5.943** (−2bp); intraday high **6.029** [CNBC] | **>6.00 orange — 6bp under on the close; next close >6.00 fires** | TE ✓ 10/01 |
| US 10Y | **4.998** — at the 5% handle | (context; BOND owns) | ^TNX ✓ 9/18 |
| EUR/USD · DXY · GBP/USD | **1.12 · 102.07 · 1.32** | <1.05 watch far away | boot pull ✓ 10/01 |
| EuroStoxx50 · DAX · FTSE | **6,175 · 24,939 · 10,428** | — | boot pull ✓ 10/01 |

**Open fires: 5 of 17 — `T-02` · `T-05` · `T-07` · `T-08` · 🆕 `T-10` (9/24).** The US row is a 9/18 level, not re-pulled 10/01. 🆕 `T-15` Saudi-crude-to-Europe REGISTERED 9/18** (see §SAUDI). 🔴 **`T-12` (EUR/USD 3M basis) remains UNINSTRUMENTED and cannot fire at all — excluded from any clean-board count.** A clean scan of the 6 daily-scannable rows does not clear the 17.

---

## PREDICTIONS

| ID | Prediction | Conf | Resolves | State 2026-09-18 |
|---|---|---|---|---|
| **HNS-06** | German Mfg PMI **≥50.0**, Sept flash | **80%** | 9/23 | ✅ **HIT 9/25 — flash 53.8.** Secondaries only; final does not re-grade it |
| **HNS-07** | EU storage **≥80%** by Nov 1 | **65%** | 2026-11-01 | 🔴 **AT RISK.** From 69.06% [**gas day 9/17**], **45d** at **+0.22pp/d (AGSI direct) → ~78.96%, a MISS**; at the carried +0.30 → ~82.5%, a HIT. ⚠️ *Anchor corrected 9/19 late — the gas-day-vs-publication slip again; required pace is **0.2431**, verdict unchanged.* ⚠️ **Not re-marked** — 65% was set *because* the two instruments straddled the line. ✅ **The pre-committed rule now EXISTS (9/19)** — see §SESSION 4 |
| **HNS-08** | Bund does **NOT** close ≥4.00% before Dec 31 | **70%** | 2026-12-31 | 🟢 **OPEN.** Buffer ~48–50bp; MISS the instant it **closes** ≥4.00 |
| **HNS-09** | **At Q3-2026 European bank results: sector NII/earnings still holding with NO material rise in cost-of-risk** — **registered text, restored 9/19** | **70%** | 2026-11-30 | 🟢 **OPEN — same number, NEW BASIS 9/19.** Not "the sweep is clean" (clean over a blind perimeter) but **structural: euro-area banks are net DEBTORS to NBFI, so the credit channel is ** Q3 results the live window |

**7/16 book: 2 HIT, 1 MISS** · `HNS-05` ✅ HIT 9/10 — outcome HIT, **rationale FAIL** · `HNS-06` ✅ HIT 9/25 (momentum).
🔴 **CALIBRATION:** *my HITs are momentum continuations; my one MISS was the only call requiring a TURN.* **`HNS-07` is the live test of whether I re-mark a straddling call that drifts against me.**

---

## CATALYST DOCKET

| Date | Event | Pri |
|---|---|---|
| **2026-10-01 · 10-15 · 10-25** 🟠 | **`HNS-07` RE-MARK CHECKPOINTS** — evaluate rules (a)/(b)/(c) and nowhere else. ⛔ **No early resolution — rule (d) WITHDRAWN 9/19**; graded on the **11/01 gas day** | 🟠 |
| **2026-09-22** 🔴 | **AGSI lag D+1 vs D+2 — WEEKDAY check** (`KB-HANS-096`). Touches `HNS-07`'s GRADING date (11/02 vs 11/03), not its resolver | 🔴 |
| **2026-09-23** 🔴 | **German/EA flash PMI (Sept) 07:30 UTC** — `HNS-06` resolver. **Grade the FLASH.** EA HICP flash **10/1** | 🔴 |
| **2026-09-28/29** 🔴 | **`NGV26` 9/28 / `TTFV26` 9/29 expire** — boot now grades `T-07` on the NAMED contract and warns in the roll window; **never grade a rung crossing across a roll** | 🔴 |
| **early Oct 2026** 🔴 | **France submits the 2027 budget** — **`T-10` FIRED 9/24 and OPEN**; no exit registered yet | 🔴 |
| **2026-10-02** 🔴 | **PRE-REGISTERED periphery test (a)–(d), written 10/01 before the print** → `research/2026-10-01_T12_BASIS_AND_OFFICIAL_YIELD_SOURCES.md` §3. T-10 graded on the screen whose Bund leg is within 5bp of ECB AAA. **EA HICP flash (Sep)**: first `T-15` leg (b) read | 🔴 |
| **2026-10-07** 🟠 | **ECB USD 7-day op**: first funding read since 10/01 (proposed T-12 Leg A >$1.5bn or ≥8 bidders; last $207mn/3) | 🟠 |
| **2026-10-29** 🔴 | **ECB GovC — `T-04` (≥2.75) one 25bp hike away**, but 🆕 **no longer a hawkish lean** (core unrevised, Lagarde on energy). NL election same day | 🔴 |
| **~early Nov 2026** 🔴 | **Hormuz / Qatar force-majeure next extension** | 🔴 |
| **2026-11-01** | `HNS-07` resolves (storage ≥80%) — in the Oct 1–Dec 1 compliance window | 🟠 |
| **2026-11-26** 🟠 | **UK Autumn Budget** — **the LDI date, with the long-end seller now stood down ahead of it** | 🟠 |
| **by Apr 2027** | **BoE: sell gilts direct to Government?** (£146bn in review) | 🟠 |
| **2027-01-01** | EU ban on Russian LNG long-term contracts — bites inside the `HNS-07` winter | 🟠 |
| Sep–Dec 2026 | **German 2027 budget in parliament** — €118.7bn core NKA / €203.6bn all-in; **debt service +38%** | 🟠 |

---

## 📬 INBOX / CROSS-AGENT FLAGS — **inbox lanes CLEAR 2026-09-25** (L0 drain, PROME Tier-1 spawn: 4 top-level + 13 WALTER, every sender; log → `board_log.tsv` [created 9/25 — this desk had none] + `workbook/2026-09-25_INBOX_DISPOSITIONS.md`). `VX-HANS-11.04` RETIRED — declined by BRENT, HAWK and OSPREY. ⚠️ **PROME's WQ-295 cadence packet was never delivered to this inbox** (answered from a sibling copy). 🔴 **The LIVE flag table is `DISPATCH_LOG.md`, not this line.**

🆕 **DISPATCHED 9/18** → `BOND` (🟠 `T-04` no longer a hawkish lean into 10/29; German debt service +38% y/y on the common-mode LEVEL channel) · `ZHAO` (🟠 TIC July: France −$62.4bn over two months, UK +$58.4bn to ~$1tn).
🆕 **DISPATCHED 9/19** → `LIQUID` + `REGINALD` (🟠 ESRB primary read) · `HAWK` + `BRENT` (🟡 orphaned `VX-HANS-11.04`) · `PROME` (🟠 ESRB + ⚖️ the AGSI-key escalation). ⚠️ **Verify at the recipient tree, never here.**

## NEXT SESSION — WHAT IS OWED

🔴 **FIRST: `python3 scripts/doc_audit.py`** (RULE #1b) — **see owed #15: it reads clean over surfaces it does not scan.**
🔴 **SECOND: the CONTRACT ROLL lands 9/28 (`NG=F`) / 9/29 (`TTF=F`).** `KB-HANS-079`/`081` expire **9/25** so boot raises it **before** the roll. **`T-07` is a LEVEL ladder with L1+L2 FIRED: never grade a rung crossing across a roll.**
⚠️ **Closeout 1c has TWO forms; `--self` is the only one seeing figures I superseded.** ⛔ **Residual 13 NOT to be cleared** — silencing a graded row resolves a flag backwards → `ML-HANS-456`.

| # | Owed | Due |
|---|---|---|
| 3 | ✅ **DONE 9/25 — `HNS-06` HIT** (flash 53.8) | ✅ |
| 5 | 🟠 **(a) OAT gap SETTLED 9/25 — ideal-investisseur governs `T-10` (Bund leg = ECB AAA primary within 0.4bp); gap ~8bp, fire margins exceed it. (b) UK leg still open.** *(UK leg 9/19: BoE `IUDMNPY` is now a primary daily series, but the gap is still UNDECOMPOSED — 5.2421 [9/16] vs TE 5.29 [9/18] differ in date AND basis at once; needs SAME-DATE pairs.)* (a) **OAT ~10bp** — both `T-10` trip lines sit inside it. (b) **UK 10Y** BoE `IUDMNPY` vs TE. **Pin both before either is cited** | 🔴 |
| 24 | ✅ **DONE 10/01 — `T-10` EXIT REGISTERED** (band cell): spread <90 AND OAT <4.40 on i-i, 5 consecutive sessions; a row back over either fire line resets | ✅ |
| 25 | **`T-15` leg (b) label vs basis:** state says UNINSTRUMENTED, value_basis names a MONTHLY-instrumentable test (HICP energy vs Brent). Reconcile; first read 10/1 | **2026-10-01** |
| 26 | **Re-verify `TTF_CALENDAR` X26/Z26 expiries** (computed from the ICE rule) before 10/29 | **2026-10-26** |
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

**10/01:** European sovereign stress broadened. France widened most, but Italy widened almost as much, and the Bund rallied as a safe haven. So `T-10` is deepening (130–143bp depending on the Bund leg), and the stress is no longer France's alone. **The UK long end touched 6% intraday and closed 6bp under it**, so the one registered LDI line is a single close away, with the 11/26 Budget still ahead. *(9/18–9/19 summaries → `SESSION_LOG.md` § STATUS ROTATION 2026-10-01.)*

---
*Archives → `workbook/`. Falsification → `thesis/KILL_TREE.md`. Flags → `DISPATCH_LOG.md`. Bands → `registry/`.*
