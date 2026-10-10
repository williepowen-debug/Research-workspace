# HAWK STATUS
**Last Updated:** 2026-10-10 Sat 13:0x ET (from `date`). **L0 DRAIN after 12 dark days** (last session 9/28; PROME `prome-ce` Tier 1, DOCKET L669; session hawk-1010, Claude Code, model Opus 5.5). **Basis: the Fri 10/9 close.** Vendor last trade read Sat 12:4x ET via `fetch.py`: Brent front month **$104.72 (+0.42%)**, contract identity UNKNOWN by name-cut; WTI Nov (CLX26) **$91.85 (+0.39%)**. BRENT owns price. **$0. No mark, band, threshold, score or prediction letter moved.**

**Drain receipt:**
- **Inbox drained whole:** 7 top-level packets, 66 WALTER-lane signals and 3 BOARD info-lane signals found by ID-diff. Lane dispositions: 12 acted / 38 noted / 16 info-only; the 3 BOARD rows: 2 noted / 1 info-only.
- **6 named corrections receipted** in the WQ-399 form (corrections check rc 0); details in `board_log.tsv` and `registry/corrections_receipts.tsv`.
- ⛔ **Late, stated:** WALTER SIG-W-20261004-014 (ACTION, *"before Monday's open"*, 10/05) **lapsed unanswered while this desk was dark.** It is answered late here and in KB-HAWK-434.

**What changed while dark (synthesis; owners in brackets):**
1. **Gulf: the threat moved upstream and inside the Gulf.**
   - The Saudi transport chain is REPORTED recovered. Petroline has three flow estimates, never averaged: ~3.5 (Bloomberg 9/28), ~5.5 (Argus 10/01) and the minister's "5.8" (10/06, no daily unit).
   - **Yanbu port was struck 10/01** (temporary terminal-wide suspension, Vanguard).
   - Houthi spokesman Saree (10/08) told staff at ALL Saudi oil facilities to leave target areas.
   - **Shedgum gas plant burning since 10/09** and north-Ghawar upstream heat on 10/10. Cause is UNVERIFIED and FIRMS never counts [FALCON].
   - **The hull war moved west of the Strait:** off Qatar 10/07 and off RAK 10/09; the IRGC threatens ships outside the Strait [FALCON].
   - FALCON holds B1/C14/D85, losses 3. KB-HAWK-434.
2. **Iran diplomacy: my 9/28 "rejection stands" read is RETIRED.**
   - The US reply was handed over in Doha 9/29 and Iran is amending via mediators; the state is a mediated exchange with no framework.
   - Trump (10/08): no attack before the 11/3 midterms. That is tape, not a decision record, and a three-day strike option is reported drafted. KB-HAWK-431.
3. **Russia: refinery strikes continued through the US–Russia diesel deal** [OSPREY].
   - Volgograd fully halted 10/02; Omsk, Salavat, Ukhta and the Rostov products terminal were also hit. Capacity, not barrels.
   - OSPREY C2 was KILLED 10/09 (dormant-armed). C3 reset to AFRAMAX RIO 10/06.
4. **Sanctions coalition is diverging by jurisdiction AND product.**
   - US OFAC GL 135 (10/09) licenses Russian diesel to 2027-04-07.
   - The UK designated 8 ships on 10/01 and 38 targets including Zarubezhneft on 10/08; the EU 22nd package was agreed 10/07.
   - The US tightened on Iran the same week (17 vessels). KB-HAWK-429/433.
5. **NATO: Russia's Kaliningrad nuclear non-paper (9/30) moves no EURMIL rung; ORANGE holds.** KB-HAWK-430.

**Answers delivered to siblings** (packet `AGENTS/OSPREY/inbox/2026-10-10_from-HAWK_c3-limb2-undetermined-gl135-partly-supported.md`):
- **OSPREY C3 limb 2 for the 10/06 window = UNDETERMINED.** No in-window insurer/P&I act or print is held, and the 9/21 REPRICED grade is pre-window (KB-HAWK-428).
- **GL 135 → mainstream tonnage = PARTLY SUPPORTED, US-person leg only.** The EU/UK caps still bind non-shadow tonnage (KB-HAWK-429).

**Encoded:**
- **WQ-362 vendor inquiry LAPSED** (KB-HAWK-426; banners on the option-C files).
- **FALCON qualifier + HAW-19 9/29–30 residual (no fire)** appended to the HAW-19 Outcome cell (KB-HAWK-427).
- **DAEDALUS L546 float-tie:** `scripts/thresholds.py` (frozen suite) now rounds before the edge compare; exact-on-edge test 56.54 vs 51.4 reads WITHIN (it read OUTSIDE unrounded).
- **DAEDALUS Prose-Remedy #1 + WALTER WQ-399:** two C4-class own-charter edits (closeout 10 byte gate; boot 6a-2 receipt line).
- **Aggregates refreshed and fingerprints recorded** (`derived_freshness` PASS).

**Owed, not done (L0 drain scope):**
- **TRADE-02 is 49 days since its last update**, so a re-sweep is due under the 45-day cadence.
- EURMIL-01's 10/03 first checkpoint was not run.
- The October STEO (10/06) N6 observation is owed.
- LESSONS.md is at 86% of its read budget (`rotation_due=1`); rotation deferred to the next HAWK session.

**Prior STATUS (9/28) verbatim:** `archive/2026-10-10_STATUS_before-L0-drain.md`. **Prior headers 9/18–9/26:** `archive/2026-09-28_STATUS_prior-headers_0918-0922.md`.

## Cross-war decision summary

The asymmetry holds and has moved. **Russia's damage is REFINING/PRODUCTS** while its crude exports hold (Bloomberg four-week average 3.76 mb/d to 10/04, B3/UNCONFIRMED per OSPREY). **The Saudi damage was CRUDE TRANSPORT and is REPORTED recovered**, while the threat has moved to upstream sites and hulls inside the Gulf. Different molecules and mechanisms: no pooled lost-barrel figure. **New cross-war link:** GL 135 ties a US product-supply arrangement to Russian refining that Ukraine is striking. Trump's own text makes the 3 Mt tranche conditional on *"the condition of their Diesel Refineries"*. ⛔ A diesel barrel lost to a refinery strike and an undelivered GL 135 tranche are ONE barrel: count it once, at the refinery.

Source authority: OSPREY/FALCON own theater facts. BRENT owns prices, measured balances and trade inputs. Prior table rows (9/16–9/28) are in the archived STATUS.

| Leg | Current synthesis / evidence limit |
|---|---|
| Saudi crude transport | Petroline: shut 9/11 (precautionary), restart REPORTED 9/22, Yanbu exports REPORTED resumed 9/28. **Flow estimates, different bases, never averaged:** ~3.5 mb/d (Bloomberg 9/28, one source; corrects my 9/28 "no volumes", COR-20260928-20), ~5.5 mb/d (Argus via Newsquawk 10/01, one source), minister's "5.8 million" (10/06; the Reuters copy has no daily unit). **Yanbu port struck 10/01:** a projectile inside the port and a temporary terminal-wide suspension (Vanguard via MarEx, the stronger source; COR-20261002-16). Aramco reportedly supplying all November crude requested by European refiners (Bloomberg 10/09, unnamed). Still NOT operator-confirmed as metered flow. |
| Saudi upstream (new) | Khurais-spot heat 10/03–07; Shedgum gas plant burning since 10/09 night; four north-Ghawar upstream heat spots 10/10 (one 0.86 km from an Ain Dar GOSP). **Cause UNVERIFIED; no Aramco/MoE/SPA word; FIRMS never counts; gas plants are OUT of FALCON's rung.** Named threat: Saree 10/08 (all Saudi oil facilities). KKIA airport hit 10/08 (3 killed, GACA) and again 10/10. |
| Russia refining/products | [OSPREY 10/10] Volgograd fully halted 10/02 (~280 kb/d, Reuters); Omsk 10/08 (governor: "industrial zone" only); Salavat 10/08; Ukhta 10/09; Rostov NZNP products terminal 10/09–10; Samara LPDS (crude transit, inland) 10/02 and 10/10. Capacity, not barrels. OSPREY band ~30% (25–35% EST) unchanged; FT/Kpler "~60% of capacity" is utilization, Ukraine MoD "51% hit" is belligerent. |
| Russian crude exports | [OSPREY/BRENT] Bloomberg four-week average 3.71 to 9/27, 3.76 to 10/04 (B3/UNCONFIRMED: not read at text). **OSPREY C2 KILLED 10/09**, dormant-armed; re-arms at 5 on the next in-geography terminal/pipeline/oil-port row. Open lead: two vessels damaged in Azov port 10/10. |
| Novorossiysk September9 | [CONF owner September15 correction] fuel-oil/products terminal, not a confirmed Sheskharis crude-berth hit. Tank inventory cannot become bpd. |
| Route interaction | Yanbu northbound cargoes via Suez/SUMED avoid Bab; southbound cargoes do not. Upstream feed loss and downstream delays on the same cargo count once. Spare downstream capacity cannot replace absent upstream feed. EIA geography checked September16; actual cargo allocations unknown. |
| Bab territorial gains | Capability/geography differs from enforced closure. Hanish is north of the strait. Tanker observations cannot establish safe passage for every nationality or measure crude flow. **10/10:** "Houthis mined Bab" rests on one anonymous source (unsupported); the Taiz ground push is capability, not enforcement. |
| Insurance | **Refreshed 10/10** (`domain/war-risk/CROSS_THEATER_WAR_RISK.md`). FALCON adopted the 9/25 Gulf quotes (Hormuz 6–9%, Saudi Red Sea ports up to 7%, Yanbu ~3%) on 9/28. All of them, and every other leg, are now **>10 days old (15 days)** and pre-date both the 10/01 Yanbu port strike and the hull war's move west of the Strait. **No newer comparable quote exists.** Black Sea: no numeric print; the structural repricing (9/16–10/01) is pre-window for OSPREY's reset C3 clock. Matched cross-theater ratio UNKNOWN. |

**No-double-count rule:** identify dyad/direction, asset, molecule, flow layer, event date and prior outage. Cargo loading, departure, transit and arrival differ. Hull loss is not lost productive capacity; sanctions listings are not seized cargoes; total tanker counts do not measure accessible crude liftings. Freight indices, ETF prices, negotiated hull premiums and owner earnings are separate instruments. **Added 10/10:** a refinery-strike loss and an undelivered licensed-import tranche of the same product are one barrel.

## Existing approvals and prediction obligations

| Item | State retained / next action |
|---|---|
| HAW-19 | **DEFECTIVE-INSTRUMENT, no calibration credit** (encoded 9/28, `2d3bb96df`, KB-HAWK-415). ✅ **Residual 9/29–30 checked 10/10: no fire evidenced.** LEG A cannot fire from that window (A.3 latest start 9/17). For LEG B, the four Hormuz hulls struck 9/28–29 are afloat, not disabled or boarded, and B.5 is still vendor-unreachable. **FALCON qualifier appended:** its "zero barrels offline" is barrels-to-market, not capacity (600 kbpd stated April capacity loss on its ledger). No grade change (KB-HAWK-427). Row closed. |
| Successor / DOCKET L321 | Registered 9/26 as HAW-22 (WQ-296 A). **WQ-362 RULED 10/01 (Will, "lapse"): the Kpler/Vortexa inquiry LAPSED, with no price obtained.** Terminal-level daily export data is a **NAMED UNAVAILABLE input**. Consequence: lost-versus-rerouted barrels stay unmeasured at terminal level, so HAW-22's disclosed-loss basis and warning carry the weight. **Re-open: Will's word** (KB-HAWK-426). Option C (two-vendor v2 letter) has no data path. |
| HAW-22 | OPEN **65% UNCALIBRATED**; event window 10/01–10/31, resolves 12/22 IMMOVABLE. ⚠️ *Undisclosed damage can produce a misleading CONFIRM — a CONFIRM on this letter is a claim about what was DISCLOSED, never about capacity.* **Print 10/01–10/10: no candidate.** Yanbu 10/01 fails confirmation on the letter (one source chain, no operator/sovereign, no FM or estimate). The Rostov products terminal, Ghawar gas plants and Azov hulls are explicit non-fires (KB-HAWK-432). |
| HAW-20 | OPEN 65%, resolves 10/31; four frozen instruments (US 301, US 338, Iran toll bill, Mecca pact). **10/10:** no signal on leg (c), the Majlis 7% toll bill, in the lane 9/28–10/10. The Mecca pact (Saudi–Turkey–Pakistan) was reported "activated" 10/05 with Pakistani troops in-kingdom (WALTER -1008-014). That is a step UP, not a softening, so leg (d) (repudiation or exit) is unfired. **Nothing on the four legs has softened on the lane 9/28–10/10;** grade owed at resolution (10/31). |
| HAW-18 / WQ-208 | FAILED history; scored55%, first-call60% separately preserved. No score edited. |
| WQ-216 | Joint taxonomy approved, prospective only; asset loss without capacity loss and campaign/row grain retained. No back-catalogue re-grade. |
| N6 / WQ-211 | The AGREEMENT rule applies from October: anchors 2.38/2.35 mb/d; missing or wrong-vintage inputs CANNOT-FIRE. **The October STEO was published 10/06 (cutoff 10/01, WALTER -1007-003); the N6 observation on it is OWED, not run 10/10 (L0 drain).** The September observation remains outstanding under the old OR/OR branches. |
| OSPREY downgrade path | September15 owner window closed without objection; HAWK's September10 NO OBJECTION stands. Upward moves remain Will-gated; inaccessible export instrument does not support a new grade. |
| OSPREY C3 limb 2 (HAWK grades) | **UNDETERMINED for the reset window 10/06–10/27** (KB-HAWK-428): no in-window insurer/P&I repricing held. A kill needs OSPREY's dated in-window canvass; HAWK grades it on arrival. |
| TD3C / FLOW21 | September11 instrument finding retained as a dated assessment; TD3C is not a fixture, owner earnings or insurance premium. RED September14 accepts scoped critique, retains its own registered September30 letter with caveat. No HAWK authority to void RED's series/grade. Retest owner realized TCE at Q3 releases late October/early November. |

## Dormant book — marks carried; NOT re-swept 10/10 (L0 drain)

| Vector | Mark / unresolved evidence |
|---|---|
| VEN | GREEN; September8 partial review. Crude-only export basis and complete military posture remain unresolved. |
| TWN | YELLOW; September8 operating reserve is not LNG/coal inventory. Replacement cargo and rationing/TSMC legs unresolved. |
| TWNMIL | YELLOW; Taiwan-own exercises are not PLA activity. PRC notices, traffic intersection and actor ambiguity remain unresolved. |
| IRAQ | **🟡 YELLOW, WQ-319 RULED 9/28** (SOMO Aug 2026 report pub 9/6: 73,687,617 bbl = 2,377.020 kb/d **exports**; GREEN = FM lift, unmet). BRENT confirmed exports 9/28 at secondaries (KB-425); production leg not cross-read. ⛔ The 8/10 "no restart" negative was wrong at its date (KB-HAWK-417/422). Iraqi launch-origin evidence is not Iraqi production-loss evidence. |
| TRADE-01 | **9/28 headline (not re-graded):** US–China truce extension to 2027-01-10 and "30-for-30" tariff cuts are ANNOUNCED only; no BIS/MOFCOM notice found, so the 11/10 and 11/27 clocks stand (KB-HAWK-421; ZHAO owns China). ORANGE under WQ-211 September10 adoption-stage ruling; bands unchanged. Adoption August6 / scheduled applicability December4 / collection UNKNOWN. **10/10:** MOFCOM wrote the 2027-01-10 extension down 9/28 with no instrument; both 11/10 clocks still read 11/10 (ZHAO via WALTER -0930-003). |
| TRADE-02 | ORANGE; the comprehensive-wall RED bar remains undefined and needs a separate ruling. ⚠️ **RE-SWEEP DUE: last updated 8/22, 49 days > 45-day cadence.** Not executed 10/10 (L0 drain scope). |
| CODIF | **9/28:** Section 338 **import bans** on some Canadian goods from 9/29 = step UP. The broad 50% is reported effective **8/22 vs the registered 8/19**; reconcile (KB-HAWK-421). ORANGE; implemented Canadian counter-tariff, collection UNKNOWN. One instrument across separate legal/rate axes, never additive. |
| SULPHUR | RED holds (re-swept 9/28) on the >$700/t limb, **but the basis is mine-gate**: Ivanhoe Kamoa-Kakula Jul–Aug acid offtake ~$840/t (Q2, 7/29). No open delivered-Kolwezi print; no acid FM. Russia acid-export ban ~9/22–12/31. Next: Ivanhoe Q3 (~early Oct). KB-HAWK-419. |
| FININFRA | YELLOW holds on events (re-swept 9/28: no financial-infrastructure hit, halt or major cyber event). Yellow's own "evacuation reversed" text is unevidenced. **WQ-320 RULED 9/28:** bank-serving cloud counts only where damage is documented to interrupt a named bank (bank / function / causal evidence / date / restoration). March AWS event vs ADCB/Emirates NBD: causal link undocumented ⇒ not ORANGE. "Evacuation reversed" struck from YELLOW; RED unchanged. KB-HAWK-418/423. |
| CEASEFIRE | SUPERSEDED historical; FALCON owns live diplomacy. Excluded from re-sweep scheduling. |
| **EURMIL** | **🟠 ORANGE, unchanged** (registered 2026-09-18). Criteria hold: firing authority above national capitals, ≥1 NATO-mandate engagement since, and the political-legal ladder unstepped. **10/10: Russia's 9/30 Kaliningrad non-paper moves no rung** (threat statements are explicit NOT-RED); Lithuania ~100 troops to the Kaliningrad border, Moldova incursions and Danish sabotage claims are not rungs (KB-HAWK-430). The Article 4 negative is primary-closed only through 2026-06-17. Clean evidence stays two items (① Leipzig/Halle ② Neptun Deep); the engagement count is contaminated (zero of four engagements is a confirmed Russian probe). The **10/03 first checkpoint was not run** (desk dark); backstop 11/02. Full 9/18–9/19 cell, incl. both self-corrections and the HANS concurrence: archived STATUS + KB-HAWK-385..399. |

Dormant book is **11 rows**. **10/10 cadence scan (45 days):** TRADE-02 (8/22, 49 days) is **DUE**. VEN/TWN/TWNMIL/CODIF (9/08, 32 days), TRADE-01 (9/10, 30 days), EURMIL (9/18) and IRAQ/SULPHUR/FININFRA (9/28) are inside cadence. CEASEFIRE is excluded. No missing feed is treated as no event.

## Other obligations retained

- Overdue from 9/9–9/11 and **not re-worked 10/10:** Canada general SOR and Gazette dates; September STEO; QatarEnergy seller notice; matched premium/flow evidence; Sidi comparator; CPC August24 durability disposition; dormant missing legs.
- HAW-21 CONFIRMED September8 at65%;629 Canadian item/rate match remains historical adjudication. CA$27.6B is import coverage, not revenue; collection/employment effect unknown.
- Dictionary owner confirmations; HAW01 dropped-premise and HAW04/05 provenance limits; no retrospective credit inferred.
- Early-November Qatar review is an estimate, not an announced event. November9 Syria/Russia MOU approximation, November10 Chinese controls and December4 polysilicon applicability stay distinct in CATALYSTS.
- Enforcement/PGM live feed and RU/AF-language instrument unbuilt; legacy monitors frozen. FLOW18 ownership closed July25 (ZHAO primary/BRENT consumer). Tankage saturation remains assumption; CPC east-of-Suez/Pearl GTL questions stay with BRENT.
- **New catalysts 10/10 (CATALYSTS.tsv):** EU 22nd package formal approval expected 10/12; FE1 Suez first sailing 10/17 (planned, not a passage); OSPREY C3 earliest kill 10/27; UK Sakhalin-2 licence window 2027-01-01; GL 135 expiry 2027-04-07. H.R. 5334 action deadlines ~10/18–19 carried.

## BOTTOM LINE

**Combined read (2026-10-10, Fri 10/9 close: Brent front month $104.72, WTI Nov $91.85, vendor last trades):**
- **The two wars still hurt oil through different pipes,** and both pipes moved while this desk was dark.
- **Gulf:** Saudi crude transport is reportedly flowing again, but the attacks moved to where the oil is produced and to tankers inside the Gulf. Ghawar's Shedgum gas plant has been burning since Friday night (cause unverified), and hull strikes now come off Qatar and the UAE.
- **Russia:** Ukraine keeps knocking out refineries, even as the US licensed Russian diesel imports. That makes part of Washington's diesel plan depend on the capacity Ukraine is destroying.
- **Watch next:** whether Aramco or Saudi Arabia names damage at a Ghawar crude-processing unit (FALCON's production rung), and Iran's formal reply through Qatar. Trump says no US strike before 11/3.
- **Changed since 9/28:** no HAWK mark moved. The "rejection stands" read is retired, the vendor-data line lapsed on Will's word, and every war-risk premium on the book is now over 10 days old.
