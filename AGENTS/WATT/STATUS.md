# WATT — STATUS

**Last Updated:** 2026-09-25 09:36 ET (eleventh session — Will-directed boot + catch-up; **desk was DARK 9/12–9/24**) · **Status:** 🔴 **P1 3→5 RECORDED 9/25 on the registered RED letter — PJM ran a second autumn capacity emergency 9/16–9/18 while this desk was dark.** 9/16 evening PJM-RTO 5-min held **~$3,710/MWh** (29 intervals ≥$1,000); 9/17 **EEA-1** (Max Gen / Load Mgmt Alert) + Pre-Emergency/Emergency DR + DOE §202(c) **202-26-45** (9/17–9/18, lapsed unrenewed). **WATT-11 MISS.** The fire is SPENT — de-escalation eligible at the first boot ≥9/26. Composite **14→16/20**
**Class:** Market-agent (grid stress → power price → power cost) · **Spawnable by:** PROME or Will · **Maturity:** **L4 (Conf H)** *(DAEDALUS 2026-09-05)*
**Read-cap budget (root `CLAUDE.md` §Data Hygiene — fleet rule, binding above any owner-set number):** **32,550 B** per boot-read surface. **⛔ The old "64,000 B" line is RETIRED** — reasoning → archive § `WATT-02_GRADE_AND_READCAP_2026-09-03`.
**Superseded content →** `status_archive/STATUS_ARCHIVE_2026-09.md` (Sept rotations, per-block bytes + crc32 in its manifests; Blocks L–AC moved 9/11; **AD–AW moved 9/25**) · `status_archive/STATUS_ARCHIVE_2026-08.md` (**CLOSED**) · `archive/SCRATCH_ARCHIVE_2026-07-08.md`

**Read-cap:** read the current figure from `boot.py` leg 3 / `PROME/tools/measure.py`, never from this sentence. 9/25: 20 lines rotated verbatim (Blocks AD–AW, bytes + crc32 in the archive manifest) BEFORE the emergency write-back replaced them. Rotation, never deletion; never trim live state to hit the number.

> **Eleventh session, 2026-09-25 — catch-up after 13 dark days.** ⚠️ **The desk missed a live P1 emergency inside its own registered test window (`WATT-11` opened 9/15; no WATT session 9/12–9/24), and no fleet route delivered it** — HENRY, AEOLUS and NEXUS surfaces carry nothing on it. Recorded 8 days late, from primaries: DM2 5-min tape (pulled 9/25 — the feed's ~15-day retention still reached 9/11), EIA-930, PJM Inside Lines 9/16 + 9/17, DOE 202-26-45 (PDF read by a sweep agent). **Driver = maintenance season, not breakdowns:** PJM-RTO planned outages **0 → 16,056 MW overnight 9/11→9/12**, forced outages ordinary (~10.5 GW); load peaked only **127.7 GW** (July's EEA-1: 159.0 GW). → KB-121…129, **L-53**, FL-WATT-15, `WATT-12`.

---

## CONVERGENCE MATRIX (universal 5-pt + local state)

| # | Channel | Score (1–5) | Local state | Independence | Key signal [src, date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| **P1** | Stress → price | **5 🔴🔴** *(3→5 recorded 9/25; FIRED 9/16 + 9/17, SPENT)* | **RED CONJUNCTION FIRED ON THE LETTER, TWICE — recorded 8 days late.** **9/17 = the clean fire:** 24 intervals ≥$1,000 (run 18:20–20:05, max **$1,611.69 @18:50**) **AND** EEA-1 live (Max Gen / Load Mgmt Alert, PJM-RTO) + Pre-Emergency DR in all zones ex-ComEd/Mid-Atlantic, Emergency DR in BGE/PEPCO/DOM + §202(c) **202-26-45**. **9/16 = the weaker fire:** 29 intervals ≥$1,000, a ~$3,710 plateau 18:20–19:45, max **$3,715.47 @19:10** **AND** demand 127,732 MW = 100% of trailing 24h peak — ⚠️ **the ≥97% limb is near-automatic at an evening peak** (L-53). KILL_MEMO cascade **NOT tripped** — no EEA-2+ (C1), 24h peak <158 GW (C3), no named large-load curtailment (C2). **Supply-driven:** ~36–38 GW offline, forced outages ordinary | 9/16 and 9/17 share ONE root (maintenance-season outages + late heat + exports south/west) — **count once**; shares the heat antecedent with P4 | **[9/25 09:05 ET]** DM2 5-min 9/18–9/24 daily max $85–$518, 0 ≥$1,000. **9/25: ONE interval $1,009.26 @08:10 → $375 → $87** (single print, fails "2+ consecutive" — a transient, L-29) at **85,273 MW = 92.2%** of a 92,481 MW 24h peak, with **44,802 MW offline (planned 27,537)**. Board 9/25: 1 posting (#105478 FE-AP local, 9/2), 0 emergency-class. DOE: 202-26-45 lapsed 23:59 9/18, no renewal (newest order 202-26-48, Duke Carolinas) | **→3 (same registered letter as 9/11):** ① 202-26-45 lapsed ✅ · ② 7 clear CALENDAR days 9/19…9/25, complete 23:59 9/25 (L-51) · ③ HWA lifted — **execute at the first boot on/after 9/26, after re-reading the board + the full 9/25 tape.** **Re-fire:** the RED conjunction again. **→4 path after de-escalation:** EEA-1 / Max-Gen Alert / new §202(c) naming PJM. `WATT-12` (9/26–10/31) carries the outage-season test |
| **P2** | Structural capacity cost | **5 🔴🔴** | confirmed short — **3 straight at-cap clears, 2 straight RTO-wide shortfalls**; **the allocation switch has MOVED: PJM filed Door B.** ⭐ limb (c)'s mechanism was **AUTHORISED**, never observed running — **and that authority lapsed 9/8 unmeasured** | independent (auction structure); IRAS is a **regulatory** root. ⚠️ **The 9/1 §202(c) order is NOT independent of P1** — same heat episode, count once | 26/27 **$329.17 cap**; 27/28 **$333.44 cap** (6,623 MW short); **28/29 cleared 7/14 at $325 = AT its own cap (100%), 6,831 MW short**, uncapped sim $554.72, **$16.4B** [PJM Inside Lines 7/14, VERIFIED]. **IRAS `ER26-3515-000` filed 8/13; requested effective 10/12; service availability 1 Jun 2027** | de-escalate only if 29/30 BRA clears below cap AND queues drain |
| **P3** | Data-center demand leg | **4 🔴** | held at 4 — unchanged. Demand leg intact. **authority ✅ · deployment ❓UNKNOWN · utilisation record ❌** — **and the §202(c) authority LAPSED 9/8 with the record still ❌.** ✅ ACTION #105472 (5 zones) **was** dispatched = demand response. ⚠️ **Texas large-load milestones [9/8] are CONDITIONAL, not operating** | couples to HEN-36 AI-capex | **PJM 32 GW** peak-load growth 2024–30, **30 GW (94%) data centers** [PJM via DCD]. **WoodMac 55 GW/2030** (utility-self-reported). **Active queue ≈250 GW = 1.56×** the 160,451 MW peak; **needs 2× ≈321 GW.** Mix: gas 106 GW (48%), storage 67, nuclear 18, solar 15, s+s 9, wind 5 | **ACTIVE queue > 2× forecast summer peak** OR IPP load-growth guide **raised** (not reaffirmed) → 5 |
| **P4** | Gas → power coupling | **2 🟡** | **NOT-FIRED.** Defensible form: **the readings do not establish persistent widening** — the post-episode level returned near the August baseline. ⛔ 3 claims withdrawn → **§ WITHDRAWN** | shares the heat antecedent w/ P1 | **+$28.26/MWh same-vintage** (on-peak HE08–23, **9/4–9/9**, n=1,151, RT LMP $47.89 − 7.0 × HH $2.805 @9/10); @HR 8.0 **+$25.45**. Clean post-episode 9/4–9/5 **+$28.98**. Series on one basis: **+$29.84 (8/4) → +$48.12 (8/17) → +$28.98 → +$28.26** | compresses 50% or negative, sustained 3+ sessions → 3 — **on ONE consistent basis and ONE uncontaminated window** |

**Composite: 16/20** *(P1 5 + P2 5 + P3 4 + P4 2 — **moved 14→16 on the P1 RED letter (fired 9/16 + 9/17), recorded 9/25.** The fire is SPENT and the tape is benign apart from one 9/25 transient; the letter holds 5 until the de-escalation clause pays out (earliest 9/26). P2/P3/P4 unmoved — **no P2 escalation**: `WATT-11`'s step 2 finds a measured planned-outage cluster, not reserve-margin erosion.)*

**⚠️ Status 🔴 on the letter, SPENT in state.** Sequence: planned outages step +16 GW on 9/12 → evening prints $515–$936 on 9/12–9/15 → **9/16 ~$3,710 plateau** → 9/17 EEA-1 + DR + §202(c) 202-26-45 → Max Gen Alert carried into 9/18 → order lapsed 23:59 9/18 → 9/19–9/24 benign → 9/25 one-print transient. ⚠️ **Still no deploy-posture change** — a spent fire supplies no entry and no exit (TERRY Non-Negotiable #15); see `TRADE.md`.

**⏸ TRIGGERED CHANNEL — B1 battery export controls (registered 9/25; NOT open, NOT scored, NOT in the composite).** *Ruled by PROME 9/22 (DOCKET L437, Will → PROME 9/19); trigger wording ZHAO's (9/25, KB-ZHAO-187), channel wording mine.* **Channel:** China's 公告2025年第58号 controls — **11 body codes incl. LFP cathode ≥2.5 g/cm³ AND ≥156 mAh/g (3C901.a.1)**, cells ≥300 Wh/kg, graphite anode, cell/cathode/anode equipment + technology — **→ grid-storage (LFP, >80% of new stationary installs, industry B2) supply/cost → storage buildout pace in PJM/ERCOT**. **Opens on T1:** the first day NO MOFCOM suspension instrument covers 58 (today 公告2025年第70号, 「至2026年11月10日」 ⇒ window **11/10–11/11 Beijing**; 「至」 inclusivity INFERRED); graded **only** on a mofcom.gov.cn announcement — an extension re-dates T1 automatically. **Or T2 (≥10/19):** a PRC official source says the suspension ends / will not be extended, **or** MOFCOM publishes implementing material for 58. ⛔ MOFCOM silence ≠ positive · US statements (Bessent's "to 1/10/2027"), readouts, press, BIS Affiliates Rule, market moves **never** trip it. **Guards:** magnitude UNKNOWN, not large · first use, no precedent · ⛔ never carry "300 Wh/kg spares stationary storage". Finished-cell (EV) leg UNOWNED.

---

## LIVE CHANNEL READS (sourced + dated)

- **P1 — Stress → price** 🔴🔴 **5 on the letter (fired 9/16 + 9/17, SPENT), recorded 9/25** [DM2 5-min pulled 9/25 09:1x ET · EIA-930 · PJM Inside Lines 9/16 + 9/17 · DOE 202-26-45].
  **The episode, from primaries** → archive Block AX + KB-121/122: Max Gen / Load Mgmt Alert for 9/17 issued 9/16 (>35 GW planned outages, exports south/west); DR dispatched 9/17; **DOE 202-26-45** (9/17–9/18, backup generation at large loads before/during EEA-3). Max Gen Alert = **NERC EEA-1**; no EEA-2 found.
  **Why it happened** → archive Block AY + KB-123: forced ~10.5 GW (ordinary) · **planned 0 → 16.1 GW on 9/12** (part may be classification) · total 38.5 GW (9/16) → **44.8 GW (9/25)**. `WATT-11` step 2: measured planned-outage cluster ⇒ **no P2 escalation.** Backup-generation authority granted a 3rd time; utilisation still ❌.
  Retail backdrop [EIA, 2026-07]: industrial **9.77¢/kWh**, residential **18.31¢/kWh**. ⚠️ **The load at which PJM goes to emergency now has three points:** 159,046 MW (July) · 152,518 (9/1) · **~127,700 (9/16–9/17)** — it falls as outages rise, so **a peak-load threshold cannot see a shoulder-season emergency** (L-53; OPEN #4's 6.5 GW gap is now one instance of this).
- **P2 — Structural capacity cost** 🔴🔴 **AT MAX, unchanged** — facts in the matrix row; full bullet → archive Block AZ (+ Block I). Limb (c) = backup-generation priority: **authorised three times as emergency authority (202-26-35/-41/-45), never observed running**; the tariff version (IRAS) is still unruled at FERC.
- **P3 — Data-center demand leg** 🔴 **held at 4, unchanged** — 32 GW firm coincident vs 55 GW utility-reported (non-coincidence + duplication, NOT a haircut); Texas large-load milestones CONDITIONAL. Full bullet → archive Block BA.
  ✅ **VULCAN seam CLOSED 9/25 at ITS artifact** — `VULCAN/STATUS.md` S3 rows (lines 29, 53, 73 as read 9/25) carry the corrected population wording verbatim ("~55 GW aggregate utility-reported forecast / ~32 GW firm coincident-peak … NOT a nameplate or queue figure"), adopted 9/6 across 8 surfaces [DAEDALUS PR-6 R4 claim 4; re-read 9/25].
- **P4 — Gas → power coupling** 🟡 **NOT-FIRED. +$27.33/MWh same-vintage on-peak** [9/19–9/24, n=1,135, HR 7.0: RT LMP $50.19 − 7.0 × HH $3.265 @9/25; @HR 8.0 +$24.07] — flat vs +$29.84 (8/4) / +$28.26 (9/11); the window contains no emergency day. **The gas leg moved:** NG=F $2.831 (9/11) → **$3.297 (9/24, a 13-week high)**, ≈+16%, nearly all of it 9/22–9/24, on a **Columbia Gas Transmission force majeure in West Virginia (~1.8 MMDth/d of firm service cut, 9/24)** [SECONDARY; yfinance closes, not settlements]. ⚠️ ⚠️ **CORRECTED 9/25 (BRENT, `f7bbdc42e`): the basis SIGN is UNKNOWN, not "against PJM".** Mountaineer XPress is an Appalachian **takeaway** line — shutting it traps gas in the production area, so production-area basis (Eastern Gas South / TCO pool) likely **WEAKENS** vs Henry ⇒ an HH-based spark would **overstate** western-PJM gas cost; eastern market-area sign ambiguous. **Assessment, not measurement — no free primary for hub basis** (EIA NGWU ended 1/22). ⚠️ **NG=F rolled Oct→Nov on 9/25:** the $3.265 gas leg above is **NGX26**, not the NGV26 series quoted before it. The 8/13–8/16 elevation is still unexplained.


### P2 — the regulatory layer → archive (full text, verbatim)
**Graded copy:** `workbook/PREDICTIONS.tsv` WATT-08/09/10 · **KB** 070/072/077.
**Kept live (full paragraph → archive Blocks BB + T):** IRAS `ER26-3515-000` filed 8/13, **NOT BANKED**, requested effective 10/12, service 1 Jun 2027 — **no FERC action found as of 9/25**; companion RBP `ER26-3380-000` (bid window reportedly 9/30–10/21, SECONDARY); EL26-67 relationship UNESTABLISHED, no ruling. Door A → CARL/HENRY · Door B → VULCAN/HENRY.

**Season emergency count = 4 episodes, ALL CLOSED** (7/3 EEA2 + §202(c) precedent · 7/15–16 EEA-1 + 202-26-35 · 9/1–9/3 EEA-1 ×3 + 202-26-41 · **9/16–9/18 Max Gen / EEA-1 + DR + 202-26-45**). **The first three were heat-peak events (152–159 GW); the fourth came at ~128 GW with ~36 GW offline — a maintenance-season event.** `WATT-11` graded **MISS** 9/25. *Prior paragraph → archive Block AW.*

---

## ⛔ WITHDRAWN — do not re-assert (full 11-row register → archive)

**14 claims withdrawn or scoped (13 in the 2026-09-06 five-round review; a 14th — the P4 headline word "de-contaminated" — found still standing and fixed 9/10).** Register verbatim → archive § `CORRECTIONS_LEDGER_FULL_2026-09-06`; reasoning → `LESSONS.md` **L-46…L-51**, `workbook/KB.tsv` **KB-103/105/106/107/110-113**.

**The standing do-not-reassert list, in one line each:**
⛔ **Do-not-reassert, in eight words each (full list verbatim → archive Block V):** backup generation *authorised, not observed* (authority lapsed, record still ❌) · 55 GW seam agreed on the *number* · P2/P3 *linked* roots · 28/29 cleared at *100%* of its own cap · 9/1 = *episode* peak, not season · spark neither *widened* nor *never moved* · reconstruction = *sensitivity analysis* · autumn non-heat emergency *opens an investigation*.

## EXIT / INVALIDATION (standing-rule-vs-state triad)

**Kill rail re-derived: 2026-09-02** *(TESTED, not rewritten, on 9/6 and again on 9/10.)*

| Channel | Standing rule | Current state @ level | FIRED? |
|---|---|---|---|
| P1 | **As re-specified 8/17, unchanged:** EEA2+ posting **OR** (LMP ≥$1,000 sustained 2+ **consecutive 5-min** intervals **AND** [emergency-class posting live **OR** demand ≥97% of trailing 24h peak]) | **FIRED 9/16 (demand limb) and 9/17 (posting limb: EEA-1 live); both SPENT.** 9/18–9/25 09:05: one interval ≥$1,000 (9/25 08:10, single — fails "2+ consecutive"); no emergency-class posting on the 9/25 board | **🔴 FIRED on 3 days this season (9/2, 9/16, 9/17), NOT RE-FIRING.** Live rail **NOT-FIRED as of 9/25 09:05** |
| P2 | BRA clears at cap AND short of reliability req | 26/27 + 27/28 + **28/29 all at cap**; 27/28 + 28/29 both RTO-wide short | **FIRED — at MAX (5)** (3 consecutive at-cap, 2 consecutive shortfalls) |
| P3 | PJM **ACTIVE** gen-interconnection queue (Cycle intake **+** transition remainder, nameplate MW) **> 2× forecast summer peak** | **≈250 GW = 1.56×** the 160,451 MW 2027 peak (wider tracker definition 1.76×; Cycle-1-only 1.37×). **Trip needs ≈321 GW.** IPP guidance reaffirmed, not raised | **NOT-FIRED on every basis.** ⚠️ **score ≠ triad** — P3=4 came from the demand-side discriminator, not this |
| P4 | spark spread negative (gas-fired uneconomic) sustained 3+ sessions | **+$28.26/MWh** same-vintage on-peak (9/4–9/9, n=1,151) — positive, and **flat vs the 8/4 baseline (+$29.84), not widening** | **NOT-FIRED** — comfortably. ⚠️ **The "moving away from the trigger" note carried since 8/17 is WITHDRAWN**: it was window composition. Distance-to-trigger unchanged since August |

**Fired-count: 2 of 4** *(P1 + P2)*. ⚠️ **P1's is a SPENT fire** (last firing day 9/17). **Thesis-kill vs channel-kill:** the shoulder season is **not** a dormant season for P1 — `WATT-11` wrote the dormancy expiry down (L-42) and the channel re-opened inside it, on outages rather than heat. Falsification unchanged: a non-heat emergency **opens an investigation**; this one's investigation found a **measured planned-outage cluster**, so it does not establish reserve-margin erosion. The thesis dies only if the 29/30 BRA clears well below cap **AND** data-centre queues drain. Neither is in evidence. *Prior narrative → archive Block AQ + § `FIRED_COUNT_CHANNEL_KILL_NARRATIVE_2026-09-06`.*

**Bidirectional flip → archive Blocks BC + Z:** structural = the **29/30 BRA** (~mid-2027); near-term = **FERC on IRAS (WATT-10)**.

---

## INSTRUMENT — the two operative facts (reasoning → **L-44**, KB-WATT-101/104; long form → archive)

① `rt_unverified_fivemin_lmps` retains **~15 days** and returns short windows with NO error — `read_pjm_onpeak_mean` asserts per-day COVERAGE (held 9/11: n=288 on 9/10). ② The contamination flag is a **single-day outlier detector**, not a window classifier — silence ≠ clean. ③ `rt_hrl_lmps` retains **≥67 days**; when one feed's horizon blocks a question, probe the siblings. *Full text verbatim → archive Block U.*

---

## OPEN ON WATT (compact — working detail lives in `SCRATCH.md` § PICK UP HERE; one home per fact)

*Closed items through 9/11 → archive Block BD.*

| # | item | when |
|---|---|---|
| 2 | 🔴 **P1 de-escalation 5→3 — ARMED, not executed.** Execute at the first boot on/after **9/26** after re-reading the board + the full 9/25 tape (the $1,009.26 08:10 transient is already logged). **Residual:** the 202-26-41 / -45 utilisation reports — the only route off limb (c) UNKNOWN | **≥9/26** |
| 3 | 🟠 **IRAS** — ✅ **service availability 1 Jun 2027 and requested effective 10/12 now both primary-sourced** (WALTER SIG-W-20260908-013 off the 8/13 filing). Residual: settle the **EL26-67** relationship, still unestablished after 4 sources | before **10/12** |
| 4 | 🟠 **The 6.5 GW gap** (July @159,046 vs Sept @152,518 MW) — still INFERRED. 5-min route closed; use the DM2 **generation-outage** series, method per KB-WATT-089 | open |
| 5 | 🟡 **Predictions: 4 OPEN, 1 resolved 9/25** — WATT-08 (2027-06-30) · WATT-09 (~11/30, contingent) · WATT-10 (10/31 outer; ⚠️ a secondary source claims FERC's effective action deadline is **Fri 10/9** — UNVERIFIED) · **WATT-12 (9/26→10/31, outage season)** · ~~WATT-11~~ **MISS 9/25** → archive | — |
| 6b | 🟠 **CONDITIONAL, NOT a dated catalyst — premise open.** The 9/1–9/3 window reaches `FL-WATT-08` by **PRICE** on a ~3-month lag (trailing-3-month mark, ~Dec 2026), but the covenant marks *Excess **UNHEDGED*** costs. 🔑 **Resolve the hedged/floating split FIRST — the date exists only on one branch.** *Detail → archive Block J* | premise first |
| 8 | ⚠️ **Winter P1 gate HELD** — basis KB-WATT-076, **do not re-derive**. Never *"no EEA because El Niño"*: **peak-based, sign-agnostic.** 🔑 **The MW level at which PJM goes to emergency is not a constant.** Never mix ONI +2.03 / +1.2 | mid-Jan–Feb 2027 |
| 9 | 🟡 **ERCOT Cal-27 discriminator** — still INFERRED; pairs a **chart-read** level with **spot** gas. ⚠️ **Never quote chart-reads as settles** | open |
| 10 | 🟡 **Lower urgency:** NG=F settlement clock (N5 i-b) · **KB-WATT-034 metered-vs-DR split (PJM official was due ~early Sept — overdue)** · **para-E utilisation report** (the one route off limb (c) UNKNOWN) · Oracle/We Energies · Hut8 · TSMC-AZ · EIA-923 heat rate. *Verbatim → archive Block AA* | mixed |
| 11 | 🟠 **What drove the 8/13–8/16 spark elevation?** No posting, no §202(c); asked BRENT + AEOLUS 9/6, **no answer yet**. **Do not attach a cause without measuring one** | open |
| 12 | 🔴 **Dark-desk routing gap** — a PJM EEA-1 + §202(c) + $3,710 tape reached NO fleet surface in 8 days; WATT had no session 9/12–9/24 inside its own test window. Flagged to PROME 9/25 (the fix is a spawn/route rule, not mine to build) | PROME |
| 13 | 🟡 **Appalachian gas basis (P4) — UNMEASURED, sign UNKNOWN.** BRENT (9/25): no free primary for hub basis (a paid feed is Will's call); force majeure in effect "until further notice" [SECONDARY]; production-area basis likely **weakens** (takeaway cut) ⇒ HH-based spark errs HIGH for western PJM, if anything. **Do not fire or un-fire P4 on it** | open (no instrument) |

## WAKE SET — dated near-term only (full 12-row table → archive; routing → `NEXUS_BRIEF.md`)

| trigger | date | why it needs WATT |
|---|---|---|
| **P1 re-escalation watch** | any boot | re-fire on the RED conjunction; **44.8 GW offline (9/25) is the new fragility**; KILL_MEMO cascade on C1/C2/C3 |
| **🔴 EEA-2/3, voltage reduction, load shed** | any time | the only P1 state above the current one — KILL_MEMO cascade |
| **FERC order on IRAS `ER26-3515-000`** | **~10/12** *(PJM's requested effective date, primary-verified)*, outer 10/31 | resolves **WATT-10** |
| **FERC ruling, 3 EL26-67 abeyance motions** | overdue since ~8/07 (~30d) | sets **WATT-09**'s resolve date |
| **`WATT-12` outage-season window** | **9/26 → 10/31** | ≥1 PJM-RTO 5-min ≥$1,000 — ⚠️ **the 5-min feed keeps ~15 days: boots must be ≤14 days apart or the window has unrecoverable gaps** |
| ⚠️ **CONDITIONAL, not a catalyst — CRWV DSCR mark** | *~Dec 2026 **IF** largely floating* | premise (hedged/floating split) UNRESOLVED — see OPEN 6b; not a registered dated trigger |
| **B1 T2 re-check (ZHAO)** | **≥10/19** | battery channel opens early only on a PRC official signal or MOFCOM implementing material — silence is not positive |
| **B1 T1 — 公告70 suspension lapse** | **11/10–11/11 (Beijing)** | channel opens if no MOFCOM instrument covers 58; an extension re-dates it |
| **NERC ride-through provisions filed** | by **2026-12-31** | the un-sized AI-capex compliance cost line |
| **Winter P1 window** *(gate HELD)* | **mid-Jan–Feb 2027** | peak-based, sign-agnostic, never "no EEA because El Niño" |

## BOTTOM LINE

**PJM ran a second autumn capacity emergency on 9/16–9/18, and this desk was dark for all of it.** Real-time prices held near **$3,710/MWh for about 1½ hours on 9/16** and ran **$1,200–$1,600 on 9/17** as PJM declared EEA-1, dispatched demand response and got DOE order 202-26-45 — again authorising data-centre backup generation, with still no record it was ever used. **The cause was maintenance season, not heat or breakdowns:** ~36 GW offline at only ~128 GW of load (July's emergency came at 159 GW), forced outages ordinary. **P1 recorded 3→5 on its letter, composite 14→16/20; `WATT-11` graded MISS; no P2 escalation.** It is quiet now — one $1,009 transient at 08:10 today — but **44.8 GW is offline and rising**, so the shoulder season is a fragility window, not a dormant one (`WATT-12`). **Next:** de-escalate P1 at the first boot ≥9/26 if the board stays clear · FERC on IRAS (~10/9–10/12) · keep boots ≤14 days apart.
