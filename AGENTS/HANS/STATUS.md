# HANS STATUS.md
**Updated:** 2026-11-26 (Thu, US Thanksgiving, ET by `date`) — **hans-1126, PROME launch on Will's word (prome-80): whole-inbox drain 25 of 25 (23 WALTER, PROME WQ-735, DAEDALUS), live refresh, honest client name switched.** *11/23 STATUS verbatim → `git log -- AGENTS/HANS/STATUS.md`.*
**Boot 11/26:** rc1 (attention, no BLOCKING) · R1 corrections rc1 → 6 receipted (1 APPLIED, 5 NO-OP) → rc0 · pull REFUSED on other desks' dirty files (PROME, RED), worked on the current checkout, which matched origin · not pushed (PROME's brief) · runtime Claude Code, Opus · I own **`EUROPE_MACRO`** (BOND = time-critical backup). **UK leg: MINE.**

---

## 🔴 CARRY FORWARD — the live consequences through **11/26**. **Narrative → `SESSION_LOG.md`** · verbatim → `workbook/`

- 🟠 **FRANCE: S&P DECIDES FRI 11/27** — date now SOURCED (Börsen-Zeitung 2026-10-24, read: *"Standard & Poor's will nun am 27. November entscheiden"*; `KB-213`, closes the `KB-188` gap). OAT–Bund **149.5bp, OAT 4.75, Bund 3.25 [i-i 11/26]**; window max 174.6 [10/22]. `T-10` OPEN (exit 0/5). Assembly rejected the PLF 2027 revenue part 458–0 on 11/04; Senate from 11/20 (search summaries). **Forward view:** S&P most likely affirms A+ and may move the outlook to negative (Fitch did 10/30, Moody's holds Aa3 negative); `HNS-14` 30% stands. A cut lands after Friday's close and would show first on the 11/30 row — the only path left for `HNS-10` (+25.5bp needed in two rows; unscored view under 5%). Mind-changer: a government fall or censure before Friday.
- 🟠 **GAS: storage draw ACCELERATING on the cold turn while price eased.** EU **67.83% [gas day 11/24]**, draws 0.36 / 0.50 / **0.58pp/d** in the last three days (11-day average 0.267); gap **−17.90pp** to the AGSI 5-yr norm 85.73; `T-08` OPEN, exit 0/5. Germany **55.25% [11/24]**. Named-front **TTFZ26** closes 89.74 [11/23], **91.67 [11/24]**, 87.30 [11/25], 87.55 [11/26 bar] — no close ≥100, L3 not re-fired, L1+L2 OPEN (`KB-214`). Z26 last trade 11/27, then **F27** (87.06 [11/25]); never grade across the roll. **Forward view:** `HNS-12` (≥53.0% on 12/31) passes at the 11-day draw (~57.9) and fails at this week's (~46.4): it is a weather call now; 45% stands. `HNS-16` (close ≥100 by 12/30, 35%): unscored view down from ~50% (11/23) to ~40% — price is lower and two items cut against the tail (Putin talking energy-infrastructure talks again; Qatar LNG busiest month since the war, title), while the faster draw supports it. Mind-changer: a cold January forecast or a Norwegian or LNG outage.
- 🟢 **GIE DATA IS NOT BLOCKED.** AGSI+ and ALSI+ return data under the honest name `research-bot/1.0` **with the fleet key** already in `FORGE/tools/market-data/.env` (`AGSI_API_KEY`) and an empty array without it (tested 11/26 12:44 ET, both sites). DEWEY's empty list is the **no-key** case, not the client name. Packet to DEWEY; no new registration needed for HANS.
- 🟡 **CREDIT:** euro high-yield spread **356bp [11/24]** (ICE BofA via FRED) from 260 [9/1], peak 364 [10/23]; US 372 [11/24] from 265. Same size since September, smaller in November (euro +30 vs US +49 since 11/13). European bank shares −11.1% since 9/1 vs Euro Stoxx 50 −6.3% (Yahoo). **Bank FUNDING: NOT SHOWN** (no free bank CDS or senior-spread series). `T-14` NOT-MET; `KB-216` combo:european-credit-funding.
- 🟡 **PMI FLASH (secondary, TE via WALTER):** Germany mfg **55.0** (54.2), EA composite **51.7** (51.7); Ifo 90.6. FLASH — rows take the FINAL: mfg 12/01, services and composite 12/03. `T-02` stays OPEN on the Oct final (`KB-215`).
- 🟡 **UK:** Ofgem Jan–Mar cap **£2,166 (+26%)**, wholesale gas allowance +59% (letter read by WALTER): headline CPI from the January print; core (`T-17`, 2.8 vs 3.0 watch) only via second round (`KB-217`). BoE 4.00% [IADB 11/25]; UK 10Y par 5.1531, 20Y par 5.4353 [IADB 11/24].
- 🟡 **`T-15`:** leg (a) NOT-MET through 11/26 — Jazan Port (commercial, Saudi Red Sea) hit with minor damage 11/25 and Ras Tanura claimed, but no Aramco, SPA or buyer notice cutting European allocations (`KB-218`). Leg (b) grades the HICP ENERGY aggregate as registered; at the grade I read the liquid-fuels component beside it (DAEDALUS flag 11/25). Narrowing the instrument is **recommended to Will via PROME, not made.** ⚠️ The 12/02 flash carries the energy aggregate only.
- 🟡 **`T-16` EA core WATCH OPEN** (2.6 Oct final, `HANS-F-008`); Nov flash 12/02. Supports `HNS-13` (70%, unchanged).
- 🟡 **`russia-custody-eu-holders`** (`KB-187`): no change read; YURI's JTI falsifier 11/28.
- ✅ **WQ-735 DONE:** `fetch_eu.py` and `pmi_ism_lead_test.py` send `research-bot/1.0`; ECB, GIE (with key), BoE and Eurostat answered; no refusals.
- ✅ **`T-12` LETTER NOT PENDING WILL** (WQ-534 B). EUR→USD funding UNMEASURED.
- 🔴 **AGSI: A REJECTED KEY RETURNS HTTP 200 + AN EMPTY ARRAY** — `fetch_eu` discriminates; re-check 2026-12-19 (owed #22).
- ⚠️ **STANDING PRIOR: every defect is found from OUTSIDE or by a script, never by re-reading.**

## ENERGY — STORAGE DRAWING INTO WINTER. **Full 9/18 block** → `workbook/2026-09-18_SESSION1_ENERGY_ECB_READS.md`

| Metric | Latest | Ladder / band | Source ✓ |
|---|---|---|---|
| **TTF front-month** | **€87.55** on named **`TTFZ26`** [11/26 vendor bar, not a settlement]; closes 91.67 [11/24], 87.30 [11/25]; F27 87.06 [11/25]; Z26 last trade 11/27 | **L3 CLOSED 11/20 (`HANS-F-007`), re-armed at >€100**; L1+L2 OPEN | own pull ✓ 11/26 |
| **EU storage gap to 5-yr norm** | **−17.90pp** (mean norm 85.73) | 🟠 **`HANS-F-004` OPEN**; exit >−12 ×5, clock **0/5** | **AGSI+ single-source** ✓ gas day 11/24 |
| EU storage fill | **67.83%** — gas day 2026-11-24 (trend −0.58pp/d; 11-day avg 0.267) | `HNS-12` needs ≤0.40pp/d to 12/31 | **AGSI+ primary** ✓ |
| Germany fill | **55.25%** — gas day 2026-11-24 (−0.64pp/d that day) | `HNS-15` needs ≤0.317pp/d to 3/31 | AGSI+ primary ✓ 11/26 |

📄 **Winter read 10/29 → `research/2026-10-29_TTF_100_WINTER_READ.md`:** EU end-winter 12.6–37.7% on past drawdowns; Germany 29% to dry (crude templates). Weather lean MILD (C3S, secondary); tail = Jan/Feb cold; FT 11/14 "record polar vortex breakdown" (title, AEOLUS's). No utility cash stress: since 9/30 E.ON +11.3%, Verbund +7.9%, Engie +8.8%, RWE −1.8%, Fortum −2.4%, EnBW −3.8% vs DAX +2.7% (`KB-200`).
**Structural:** Hormuz disrupted since March · **LNG cannot be STS-transferred through Hormuz the way crude can.** ⚠️ **EU gas and US crude share Hormuz — ONE WITNESS, TWO READOUTS** (`FLOW-HANS-8`). **EU Russian-LNG long-term ban bites 2027-01-01.** ECB FSR 11/18: gas storage "historically low ahead of the winter".
⚠️ **This desk cannot see the TTF curve** without ICE data (`KB-125`).

### SAUDI CRUDE TO EUROPE — `HANS-T-15` · full block → `workbook/2026-09-18_SAUDI_EUROPE_BLOCK.md`
10/10–11/16 (WALTER, secondary): Yanbu loadings resumed; "full November crude to Europe restored" re-reported 11/16 (single low-weight site, `KB-122`). ⛔ Principal-unconfirmed. 11/26: Kpler Yanbu ~2.7 mb/d November to date vs 3.07 October (relay); Jazan Port hit 11/25; leg (a) still NOT-MET (`KB-218`). **Re-grade owed (#29).**

## ECB / EURO-AREA MACRO

| Metric | Latest | Source ✓ |
|---|---|---|
| Deposit / refi / marginal | **2.50 / 2.65 / 2.90%** — held 10/29 | ECB `mp261029` ✓ primary |
| Next GovC | **2026-12-17**. **`T-04` fires at ≥2.75**; `HNS-13` 70%. Vujcic "very likely", Nagel "highly probable", Lane backs (secondary) | ECB calendar ✓ |
| EA HICP (Oct) **FINAL** | **4.0** (Sept 3.8), energy **21.0**, **core 2.6** (flash 2.5e), services 3.3, ex-energy 2.3, m/m 0.5 | Eurostat `2-18112026-ap` ✓ primary |
| Next HICP | Nov flash **12/02**; Nov final **12/17** | Eurostat ✓ |
| EA Q3 GDP (preliminary) | **+0.4** (exp 0.2): IE +5.5, ES +0.6, DE +0.2, IT 0.0, FR −0.1 | TE (secondary) |
| ECB FSR Nov 2026 | AI valuations, fiscal imbalances, geoeconomic tensions; no institution named | ECB ✓ primary 11/18 |

🔴 **FIVE REFUTATIONS OF MY BELOW-CONSENSUS GROWTH LEG (Sept) — the leg is wrong and the ISM-weakness transmission it fed is dead.** → `KB-HANS-067`

## SOVEREIGN / FX BOARD — LEVELS 2026-11-26. ⚠️ **Rows marked "not re-read" carry an older value.**

| Metric | Level | Band | Source ✓ |
|---|---|---|---|
| German 10Y Bund | i-i Bund leg **3.25** [11/26]; ECB AAA **3.259** [11/25] = proxy; TE 3.3202 [11/11, **not re-read**] | **>3.00 watch ✅FIRED** / >3.75 orange · `HNS-08` | i-i · ECB ✓ |
| France 10Y OAT | **4.75** [i-i 11/26]; ECB monthly Oct 4.890 | >4.50 level leg ✅ MET | i-i ✓ |
| OAT–Bund spread | **149.5bp** [i-i 11/26]; ECB monthly Oct 147.4 | >100 ✅ MET, **`T-10` OPEN**; exit <90 AND OAT <4.40 ×5 — **0/5** | i-i ✓ |
| Italy 10Y BTP / BTP–Bund | ECB monthly Oct 4.680 / 126.4bp; daily **not re-read** | >5.50 AND >200 — far | ECB ✓ |
| UK 10Y gilt | BoE par **5.1531** [11/24]; TE 5.2344 [11/11, **not re-read**] | >5.50 orange | IADB ✓ |
| **UK 30Y gilt** | TE 5.653 [11/11, **not re-read**]; BoE 20y par 5.4353 [11/24] = proxy, never T-13 | **>6.00 orange** | TE |
| Spain–Germany 10Y | ECB monthly **65.0** [Oct] governs | 80 Yellow | ECB ✓ |
| BoE Bank Rate | **4.00%** [IADB 11/25] — next due 12/17 | — | BoE ✓ primary |
| EUR/USD · DXY · GBP/USD | **1.10 · 103.78 · 1.31** | <1.05 watch | Yahoo ✓ 11/26 intraday |

**Open fires: 6 of 17 thresholds (6 OPEN fire rows; `T-07` carries L2 only since the L3 close 11/20) — `T-02` · `T-05` · `T-07` · `T-08` · `T-10` · `T-16`.** ⚠️ boot's integrity check keys on the threshold, not the tier: an L3 re-fire would NOT print BLOCKING while the L2 row is open; read §[1]'s rung. 🔴 **`T-12` (EUR/USD 3M basis) UNINSTRUMENTED — cannot fire, excluded from any clean-board count.** A clean scan of the 6 daily-scannable rows does not clear the 17.

---

## PREDICTIONS

| ID | Prediction | Conf | Resolves | State 2026-11-26 |
|---|---|---|---|---|
| **HNS-10** | France–Germany 10Y prints **≥175.0bp** on an i-i daily row, 10/22–11/30 | **55%** | 2026-11-30 | 🟠 **OPEN — NOT HIT.** Max 174.6 [10/22]; 149.5 [11/26]; two rows left |
| **HNS-09** | **Q3-2026 European banks: NII/earnings holding, NO material cost-of-risk rise** | **70%** | 2026-11-30 | 🟢 **OPEN — grader HIT (re-run 11/26: 5 graded, 0 fail).** Formal grade 11/30 |
| **HNS-14** | S&P lowers France's rating or outlook, 11/06–11/30 | **30%** | 2026-11-30 | **OPEN.** S&P decides Fri 11/27 (sourced, `KB-213`) |
| **HNS-13** | ECB deposit rate ≥2.75 at the 12/17 decision | **70%** | 2026-12-17 | **OPEN.** `T-16` fired 11/18; Vujcic, Nagel, Lane lean December. No re-mark rule; not re-marked |
| **HNS-11** | France–Germany 10Y does **NOT** print >200.0bp before 12/31 | **75%** | 2026-12-31 | 🟢 **OPEN.** 50.5bp under [11/26] |
| **HNS-08** | Bund does **NOT** close ≥4.00% before Dec 31 | **70%** | 2026-12-31 | 🟢 **OPEN.** i-i Bund 3.25 [11/26] |
| **HNS-12** | EU storage ≥53.0% on gas day 12/31 | **45%** | 2027-01-04 | **OPEN.** 67.83 [11/24]; at −0.267pp/d → ~57.9, at −0.58 → ~46.4 |
| **HNS-15** | Germany storage ≥15.0% on gas day 2027-03-31 | **55%** | 2027-04-05 | **OPEN.** 55.25 [11/24] |
| **HNS-16** | Named-front TTF closes **≥ €100.00** on any session 11/20–12/30 (PROJECTION) | **35%** | 2027-01-04 | **OPEN, no close ≥100 yet.** Max close 91.67 [11/24]; 87.55 [11/26]; needs +14.2%; **unscored desk view ~40%**, registered 35% stands (no re-mark rule) |

**`HNS-07` ❌ MISS 11/06 at 30%.** Book before it: 2 HIT, 1 MISS in the 7/16 cohort, `HNS-05` ✅, `HNS-06` ✅.
🔴 **CALIBRATION:** my HITs are momentum continuations; my MISSes needed a TURN. The pre-committed re-mark did the work on `HNS-07`, not judgement on the day.

---

## CATALYST DOCKET

| Date | Event | Pri |
|---|---|---|
| **11/20 → 12/30** | Russian retaliation for the Crimean Bridge strikes (target unnamed) — watch Ukrainian gas assets (OSPREY) · `T-07` L3 re-fire on any named-front close >€100 (`HNS-16`) | 🟠 |
| **2026-12-01 / 12-03** | Nov FINAL PMIs (mfg 12/01; services and composite 12/03) — flash DE mfg 55.0, EA comp 51.7 (`KB-215`); `KB-004` refresh owed | 🟠 |
| **2026-11-27** 🔴 | **S&P France decision (sourced, `KB-213`), after the European close** · TTF Z26 last trade, then F27 graded (never across the roll) · YURI JTI falsifier 11/28 (`KB-187`) | 🔴 |
| **2026-11-30** | `HNS-09` formal grade · `HNS-10` and `HNS-14` windows close | 🟠 |
| **2026-12-02** | EA Nov flash HICP (core after the `T-16` fire) | 🟠 |
| **2026-12-17** 🔴 | **ECB and BoE decisions** · EA Nov final HICP | 🔴 |
| **~end Dec · 2026-12-30** | Qatar force-majeure extension · TTF F27 last trade | 🟠 |
| **2027-01-01** | EU ban on Russian LNG long-term contracts | 🟠 |

---

## 📬 INBOX / CROSS-AGENT FLAGS — **inbox CLEAR 2026-11-26** (25 of 25: 23 WALTER, PROME WQ-735, DAEDALUS; dispositions in `board_log.tsv`; GIE-key packet to DEWEY, PROME memo; no TERRY packet: nothing fired or resolved). 🔴 **The LIVE flag table is `DISPATCH_LOG.md`, not this line.**
**Combination themes (WQ-622; charter line = `CLAUDE.md` Inbox step 3a), `combo:` in KB Notes:** `european-credit-funding` · `uk-cost-squeeze` · `europe-operational-disruption` · `europe-gas-politics` · `france-growth-fiscal` · `russia-custody-eu-holders`.
**DAEDALUS WQ-678 Changelist B:** applied M46 (fire state out of the band table) and M47 (FSR obligation met 9/5); declined the other 14 for now — no defect, a charter pass is not this session's work.

## NEXT SESSION — WHAT IS OWED

🔴 **FIRST: `python3 scripts/doc_audit.py`** (RULE #1b).
⚠️ **Closeout 1c has TWO forms; `--self` is the only one seeing figures I superseded.** ⛔ **Residual 13 NOT to be cleared** → `ML-HANS-456`.

| # | Owed | Due |
|---|---|---|
| 33 | **`HNS-09`: UniCredit and Crédit Agricole PENDING, BNP and SocGen INCOMPLETE — formal grade at 11/30** (grader HIT on re-run 11/26) | 11/30 |
| 43 | **`HNS-10`, `HNS-14` grades:** read the S&P France release (11/27 evening) and the i-i 11/27 and 11/30 rows | 11/30 |
| 37 | **`KB-004`** (charter cites it): refresh needs the HCOB or S&P text, at the Nov finals | 12/01–12/03 |
| 38 | **`VX-8.04` TTF/HH ratio still on 10/29 inputs.** Stale vectors with no new print read: `VX-1.08` TIC · `8.05` German IP · `4.07` ECB QT · `4.09` · `7.07` · `11.03` (#14) · `5.01` | 🟠 |
| 40 | **Still not re-read:** German 10Y on TE/Bundesbank basis (`T-05` carries 3.3202 [11/11]), daily BTP, UK 30Y benchmark (`T-13`), France budget Senate vote | next wake |
| 44 | **`test_hans.py` writes into live `CLAUDE.md` and `VX.tsv` and restores them** (PROME relay of DAEDALUS 11/25). Restored clean on the 11/26 run; the risk is a reader during the ~60s run or a crash before `finally`. Move those tests onto temp copies | 🟡 |
| 45 | `HANS_T_FIRED_LOG` `HANS-F-008` dispatch path: re-point to BOND `processed/` (C4-MOVED, informational) | 🟡 |
| 29 | `T-15` leg (a) Saudi re-grade (11/26: still NOT-MET, `KB-218`) | 🟠 |
| 5 | 🟡 **UK 10Y basis:** gate ≥5 verified-close pairs; 3 held (`KB-124`) | accrues |
| 14 | **Split `VX-HANS-11.03`** into German annual outlay + a real EU issuance series | 🟠 |
| 23 | `ML.tsv` legacy key collision — `C12` guards new ones; not renumbered → `ML-HANS-473` | 🟠 |
| 22 | Empty-key discriminator is vendor-quirk-dependent — re-verify | **2026-12-19** |

## TWO-SENTENCE SUMMARY

**11/26:** The one dated event left for my France calls is S&P's decision tomorrow (Friday 11/27, now sourced); with the French spread at 149.5bp, well off its 174.6 peak, I expect an affirmation with at most a negative outlook, so the "spread reaches 175" call (`HNS-10`) is very likely to miss on Monday. In gas, storage is now drawing about twice as fast as two weeks ago on the cold turn while the price eased to about €87.5, so whether storage ends December above 53% has become a weather call; and the GIE storage feeds the fleet thought it had lost still work, using the key the fleet already holds.

**11/23:** European gas stayed under €90 for five straight closes through Friday 11/20, so by my written rule the €100 alarm (L3) that fired 10/28 closed; the €60 and €66 alarms stay on. The price jumped back to about €91 on Monday on colder forecasts and Norwegian outages.


---
*Archives → `workbook/`. Falsification → `thesis/KILL_TREE.md`. Flags → `DISPATCH_LOG.md`. Bands → `registry/`.*
