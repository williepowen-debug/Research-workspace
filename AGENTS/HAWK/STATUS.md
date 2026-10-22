# HAWK STATUS
**Last Updated:** 2026-10-21 Wed 20:3x ET (from `date`; hook clock 20:29 ET at the turn start). **Will-launched boot and news catch-up after 11 dark days** (last session 10/10; session hawk-1021, Claude Code, model Opus 5.5; WALTER `walter-14` sent a catch-up brief mid-session). **Price [BRENT owns]:** Brent front month **$110.03**, last trade 20:15 ET 10/21 in the evening session (it belongs to 10/22; contract UNKNOWN by name-cut); WTI Dec (CLZ26) **$98.05** (`fetch.py`). On 10/9 the figures were $104.72 and WTI Nov $91.85, which is a different WTI contract. **$0. No mark, band, threshold, score or prediction letter moved.**

**Drain receipt:**
- **Inbox drained whole:** 10 top-level packets → `inbox/processed/` (KB-HAWK-443). 57 WALTER-lane signals → `inbox/WALTER/processed/`: 20 acted, 30 noted, 7 info-only. All 9 WALTER ACTION items were decided (KB-435..439).
- **BOARD info-lane ID-diff 10/10–10/21:** 59 IDs, 0 unmatched.
- **6 named corrections receipted:** 3 NO-OP, plus 1 APPLIED to the L432 card (Tsentr-2026, KB-435). The 2 FALCON loss-count corrections are APPLIED in this STATUS (losses 5).
- ⚠️ **SKIPPED, stated:** both derived aggregates (closeout 13/13a) and the derived fingerprint record. FALCON is live and mid-catch-up (`VESSELS.tsv`/`CASUALTIES.tsv` uncommitted; its last STATUS is 10/14), so a regeneration now would be stale within hours. `derived_freshness` stays rc 1. Refresh at FALCON's commit.

**What changed while dark (synthesis; owners in brackets):**
1. **Gulf: escalation signals stacked, with no verified production loss** [FALCON 10/14 + my 10/21 sweep].
   - US ordered departure from Saudi Arabia 10/21. Reuters says Saudi only. AFP says all staff and families, with families also told to leave the UAE/Jordan/Qatar/Bahrain. **The two reports CONFLICT.**
   - A third carrier, TR, is heading out (Fox; arrives by end-November), plus the Makin Island ARG.
   - Netanyahu 10/21 directive to topple the regime. Kharg oil-infrastructure strike options reported (anonymous Erem chain, **no decision**).
2. **Iran diplomacy went backwards.** Iran rejected the Pakistani proposals 10/20–21, and Araghchi says Hormuz stays closed absent US acceptance. ORACLE 10/15: the odds that the US ends the blockade by 12/31 fell from 59.1 to 37.9. Trump's pre-11/3 no-strike pledge is tape.
3. **Hull war spread across the whole Gulf.** FALCON losses **3 → 5**: GFS PRIDE sank 10/13, and CAPE DAO is "Sunk" per IMO, which JMIC disputes. Tankers were hit off Al Jubail 10/18, Al Faw 10/20 and Bukha 10/21. JMIC raised the Arabian Gulf to SUBSTANTIAL 10/18. **No mine blast verified.**
4. **Saudi targets moved toward Aramco.**
   - Dhahran HQ 10/13 is an office (OUT).
   - Abqaiq 10/08: heat at the flare stacks, no counting source.
   - Shaybah 10/21: drone intercepted, debris killed 2 (MoE).
   - **FALCON production rung D 85→92 NOT FIRED** as of 10/14. FALCON's 10/21 review is in progress.
5. **Russia [OSPREY 10/21, `481b5a917`]:** the 10/11 "energy ceasefire" was never in force. Strikes resumed 10/15 (Ryazan; CDU-6 shut per Reuters), then Surgut condensate 10/16 and the St Petersburg Oil Terminal 10/17–18 (C2 RE-ARMED). Scores 5/5/3, band ~30%.
6. **The sanctions coalition widened its split** (KB-436/437).
   - **US eases on Russia:** Graham Act waiver 10/16, with s.4(b) preserving the existing EO measures. GL 135 diesel cargoes are moving; destinations are signalled, not delivered.
   - **US tightens on Iran:** 26 targets 10/15–16, plus the Karnakis network 10/21.
   - **France boarded DF Peak** south of Réunion 10/12: first enforcement boarding outside European waters on this record.
7. **EURMIL:** Russia-attributed attacks on merchant ships in Romanian/Bulgarian EEZs (10/5, 10/6, 10/13). Bulgaria **considered** Article 4; PM Radev said no grounds, so **none was requested**. ORANGE holds (KB-439).

## Cross-war decision summary

**The decoupling holds on flow, and the escalation drivers are stacking.** Kpler via WSJ (10/21; secondary relay, single source) reports Middle East oil flows averaged **>24 mb/d vs 23.3 prewar** in the week to 10/18, with Hormuz at **~82% of prewar**. So Brent at ~$110 is mostly **risk premium, not lost barrels** (FLOW-HAWK-19; ORACLE's 10/15 gauge reads the same). The two wars still hit different molecules:
- **Russia:** refining and products capacity.
- **Gulf:** hull losses and the threat to processing.

Never pool a lost-barrel figure across the two. **The conversion risk:** one counting-source hit on a Saudi crude-processing unit, or a US strike on Kharg, would turn premium into physical loss. **The post-11/3 window is the dated known-unknown.**

| Leg | Current synthesis / evidence limit |
|---|---|
| Saudi upstream / processing | Abqaiq 10/08 flare-stack heat (FALCON KB-293), cause unknown. Shedgum gas-plant fire subsided by 10/14. Dhahran HQ office 10/13. Haradh BM intercepted. Shaybah intercepted 10/21 (2 debris deaths). Yanbu missile intercepted 10/16. "Pipeline targeted again" is an IRIB claim only. **No Aramco/MoE counting-source production loss.** Gas plants and offices are OUT of FALCON's rung. |
| Saudi crude transport | Carried from 10/10: three unaveraged Petroline estimates; Yanbu loadings reported resumed (WALTER -1015-009). Not metered. |
| Hull war (Gulf) | FALCON losses 5. Four loss instruments, **never summed** (FALCON 5, IMO 3 sunk, UKMTO, CENTCOM). Container ships are now targeted. IRGC mine claims name no hull. |
| Russia refining / products | [OSPREY] C1 5 (Ryazan 10/15 anchor). Capacity, not barrels. Band ~30% (25–35% EST). |
| Russian exports | [OSPREY] C2 RE-ARMED 10/18 (St Petersburg Oil Terminal, products, 12.5 Mt/yr capacity, no damage figure); earliest re-kill 11/17. Tambov Nikolskoye LPDS 10/20 is an inland companion watch. Bloomberg 4-wk ~3.7 to 10/11 (B3). |
| Diesel cross-link | GL 135 cargoes: Primorsk ~40 kt 10/13; Leruo (to Brazil) and Dolunay (to Turkey) signalled. ⛔ A refinery-strike loss and an undelivered licensed tranche are ONE barrel. |
| Insurance | **Hormuz 6–10% of hull** (FT brokers ~10/06; supersedes 6–9% from 9/24, per FALCON 10/14). It **pre-dates** the 10/11–13 run. WC Saudi ~3% is 9/24. JWC unchanged. Black Sea: ~$200K → ~$2.5M per vessel (Lukoil-Bulgaria executive, ~10/13; single interested source, never comparable with % of hull). **Every leg is >10 days old; aggregate not re-based 10/21 (SKIPPED above).** |

**No-double-count rule (unchanged):** identify dyad/direction, asset, molecule, flow layer, event date and prior outage. Hull loss is not lost productive capacity. A sanctions listing or boarding is not a seized quantified cargo. A refinery-strike loss and an undelivered licensed-import tranche are one barrel.

## Existing approvals and prediction obligations

| Item | State retained / next action |
|---|---|
| HAW-22 | OPEN **65% UNCALIBRATED**; event window 10/01–10/31, resolves 12/22 IMMOVABLE. ⚠️ *Undisclosed damage can produce a misleading CONFIRM — a CONFIRM on this letter is a claim about what was DISCLOSED, never about capacity.* **Print 10/11–10/21: no candidate** (KB-441). St Petersburg is a products terminal. Azov: no oil terminal named. Gulf strikes were intercepts or hulls. Re-print at FALCON's commit. |
| HAW-20 | OPEN 65%, **resolves 10/31**. Four frozen instruments: US 301, US 338, the Iran toll bill, the Mecca pact. Bounded 10/21 check: no softening found on 338 (search absence ≠ legal absence). **Grade all four legs at primaries by 10/31.** |
| HAW-19 / HAW-18 / WQ-208 / WQ-216 | Closed history, unchanged (see archived STATUS). |
| Successor / WQ-362 | Vendor inquiry LAPSED (Will 10/01). Terminal-level daily export data is a NAMED UNAVAILABLE input. Re-opens only on Will's word. |
| N6 / WQ-211 | **October STEO (pub 10/06) observation still OWED**, not run 10/21. The AGREEMENT rule applies (anchors 2.38/2.35 mb/d). |
| OSPREY C3 limb 2 (HAWK grades) | UNDETERMINED (KB-428). OSPREY owes a dated in-window canvass before **10/27**. The Black Sea $2.5M/vessel lead is one input, not a print. |
| TD3C / FLOW21 | Unchanged; retest owner realized TCE at Q3 releases (late October/early November). |

## Dormant book — marks carried; bounded checks only 10/21

| Vector | Mark / unresolved evidence |
|---|---|
| VEN | GREEN; Sept exports 1.08 mb/d, 629 kb/d to US (Bloomberg 10/2, secondary). **Re-sweep due 10/23.** |
| TWN | YELLOW (LNG/TSMC chain). Helium named-fab allocation (CBS 10/18) is VULCAN's. **Re-sweep due 10/23.** |
| TWNMIL | YELLOW. PLA joint readiness patrols 10/6 and 10/9; CCG in Kinmen restricted waters; PRC live-fire notices 10/12–17, outcome not found. **Re-sweep due 10/23.** |
| IRAQ | 🟡 YELLOW (WQ-319). Tanker hit ~30 nm off Al Faw 10/20 is a hull, not Iraqi production. |
| TRADE-01 | ORANGE. The truce extension to 2027-01-10 is still ANNOUNCED-only. **Three US measures lapse 11/9–10, with nothing on record extending them** (Thomson Reuters; KB-442). The 11/10 clocks stand. |
| TRADE-02 | ORANGE. ⚠️ **RE-SWEEP OVERDUE: last updated 8/22, 60 days > 45.** Not executed 10/21. |
| CODIF | ORANGE. No 338 softening found. **Re-sweep due 10/23.** |
| SULPHUR | RED (mine-gate basis). Ivanhoe Q3 not checked. |
| FININFRA | YELLOW. IRGC Hormuz cable threat renewed 10/20 with no damage verified (WALTER -1020-031): watch, no event. |
| CEASEFIRE | SUPERSEDED historical; excluded. |
| EURMIL | 🟠 ORANGE. Article 4 considered by Bulgaria, not requested. Dobrindt warning, the Poland threat and the Patriot consent delays are not rungs (KB-439). Backstop 11/02. |

Dormant book is **11 rows**. **10/21 cadence scan (45 days):** TRADE-02 is overdue. VEN/TWN/TWNMIL/CODIF (9/08) fall due 10/23. TRADE-01 (9/10) falls due 10/25. EURMIL (9/18) falls due 11/02. IRAQ/SULPHUR/FININFRA (9/28) fall due 11/12.

## Other obligations retained
- Carried from 10/10 and not re-worked: the 9/9–9/11 overdue list (Canada SOR/Gazette, September STEO, QatarEnergy notice, matched premium/flow, Sidi comparator, CPC durability, dormant missing legs); GL 135 grade upgrade/falsifier (KB-429); dictionary owner confirmations; and **LESSONS.md rotation (86%, deferred again 10/21)**.
- Prior STATUS (10/10) verbatim: `archive/2026-10-21_STATUS_before-catchup.md`.

## BOTTOM LINE

**Combined read (2026-10-21; Brent ~$110 on the 10/21 evening session, WTI Dec ~$98):**
- **Oil is pricing fear more than loss.** Middle East flows are reported at or above prewar levels while Brent sits near $110 (single secondary source).
- **What changed is US posture.** An embassy drawdown in Saudi Arabia, a third carrier, and Kharg oil infrastructure now on the reported options list. Meanwhile Iran rejected the latest mediation and the Houthis keep aiming at Aramco.
- **Watch:** a counting-source hit on a Saudi processing unit, any US move on Kharg, and the days after the 11/3 midterms, when Trump's no-strike pledge ends.
- **Russia:** Ukraine is back to hitting refineries and export terminals despite Washington's diesel deal.
