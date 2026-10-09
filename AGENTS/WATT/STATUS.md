# WATT — STATUS

**Last Updated:** 2026-10-09 10:06 ET (twelfth session — PROME Tier-1 WATT-12 coverage wake, DOCKET L595; desk dark 9/26–10/8) · **Status:** 🔴 **P1 = 5 on the letter, RE-FIRED 10/7.** The 9/26 de-escalation (5→3) was due and never ran — graded MET as of 9/26. Then **10/7 17:45–17:50 EPT PJM-RTO 5-min $2,978 / $2,964** at only ~94 GW load with **70.3 GW offline** → RED letter re-fires on the demand limb (weak, L-53; no posting, no §202(c)). **`WATT-12` HIT.** PJM posted a **Capacity Advisory for Mon 10/12**. Composite **16/20** (net unchanged)
**Class:** Market-agent (grid stress → power price → power cost) · **Spawnable by:** PROME or Will · **Maturity:** **L4 (Conf H)** *(DAEDALUS 2026-09-05)*
**Read-cap budget:** **32,550 B** per boot-read surface (root `CLAUDE.md` §Data Hygiene; binding above any owner number). Old "64,000 B" line retired → archive Block BG.
**Superseded content →** `status_archive/STATUS_ARCHIVE_2026-10.md` (Oct rotations; Blocks BH– moved 10/9) · `status_archive/STATUS_ARCHIVE_2026-09.md` (Sept rotations, per-block bytes + crc32 in its manifests; Blocks L–AC moved 9/11; **AD–AW moved 9/25**) · `status_archive/STATUS_ARCHIVE_2026-08.md` (**CLOSED**) · `archive/SCRATCH_ARCHIVE_2026-07-08.md`

**Read-cap:** read the figure from `boot.py` leg 3 / `PROME/tools/measure.py`, never from this sentence. 9/25 rotations: Blocks AD–BG verbatim, bytes + crc32 in the archive manifest. Rotation, never deletion.

> **Twelfth session, 2026-10-09 — coverage wake, 14 days after the last.** The 5-min tape still reached 9/25, so **0 WATT-12 days were lost** (n 286–288/day 9/26–10/8). One scarcity spike in the window, **10/7 17:45 $2,978.38**, heat-free and posting-free, on a maintenance stack that **rose 44.8 → 70.3 GW** since 9/25 (forced 8.4 → 11.7 GW). → KB-132…137, FL-WATT-15 CONFIRMED-PARTIAL, `WATT-12` HIT (archived). *Eleventh-session callout → archive Block BI.*

---

## CONVERGENCE MATRIX (universal 5-pt + local state)

| # | Channel | Score (1–5) | Local state | Independence | Key signal [src, date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| **P1** | Stress → price | **5 🔴🔴** *(5→3 due 9/26, graded MET 10/9; 3→5 on the 10/7 re-fire)* | **RED LETTER RE-FIRED 10/7 on the WEAK limb:** $2,978.38 @17:45 + $2,964.47 @17:50 (2 consecutive ≥$1,000), then $905–$977 to 18:10, $141 by 18:20 **AND** demand 91,929–94,274 MW = 98.7–100% of trailing 24h peak. ⚠️ **No emergency-class posting, no §202(c), no heat** — price + an evening ramp (L-53). KILL_MEMO cascade **NOT tripped** (no EEA-2+, peak ≪158 GW, no named curtailment). **Supply-driven:** 70.3 GW offline (planned 49.9, forced 11.7) | shares the outage root with 9/16–9/17 (one maintenance season) — count once | **[10/9 09:55 ET]** 10/8 max $576; 10/9 max $87.86. Board: **Capacity Advisory #105546 (10/8 11:45) FOR 10/12** — precursor, not EEA-class; 2 local load-relief warnings (PPL, DOM). DOE: no PJM order since 202-26-45 (newest 202-26-49, Tri-State/SPP) | **→3:** 7 clear calendar days 10/8–10/14 (complete 23:59 10/14) with no EEA-class posting + no new PJM §202(c) ⇒ first boot ≥10/15. **Resets on** a Max Gen / Load Mgmt Alert or EEA-1 (10/12 is the live test). **→ above:** EEA-2+ = KILL_MEMO |
| **P2** | Structural capacity cost | **5 🔴🔴** | confirmed short — **3 straight at-cap clears, 2 straight RTO-wide shortfalls**; **the allocation switch has MOVED: PJM filed Door B.** ⭐ limb (c)'s mechanism was **AUTHORISED**, never observed running — **and that authority lapsed 9/8 unmeasured** | independent (auction structure); IRAS is a **regulatory** root. ⚠️ **The 9/1 §202(c) order is NOT independent of P1** — same heat episode, count once | 26/27 **$329.17 cap**; 27/28 **$333.44 cap** (6,623 MW short); **28/29 cleared 7/14 at $325 = AT its own cap (100%), 6,831 MW short**, uncapped sim $554.72, **$16.4B** [PJM Inside Lines 7/14, VERIFIED]. **IRAS `ER26-3515-000` filed 8/13; requested effective 10/12; service availability 1 Jun 2027** | de-escalate only if 29/30 BRA clears below cap AND queues drain |
| **P3** | Data-center demand leg | **4 🔴** | held at 4 — unchanged. Demand leg intact. **authority ✅ · deployment ❓UNKNOWN · utilisation record ❌** — **and the §202(c) authority LAPSED 9/8 with the record still ❌.** ✅ ACTION #105472 (5 zones) **was** dispatched = demand response. ⚠️ **Texas large-load milestones [9/8] are CONDITIONAL, not operating** | couples to HEN-36 AI-capex | **PJM 32 GW** peak-load growth 2024–30, **30 GW (94%) data centers** [PJM via DCD]. **WoodMac 55 GW/2030** (utility-self-reported). **Active queue ≈250 GW = 1.56×** the 160,451 MW peak; **needs 2× ≈321 GW.** Mix: gas 106 GW (48%), storage 67, nuclear 18, solar 15, s+s 9, wind 5 | **ACTIVE queue > 2× forecast summer peak** OR IPP load-growth guide **raised** (not reaffirmed) → 5 |
| **P4** | Gas → power coupling | **2 🟡** | **NOT-FIRED.** Defensible form: **the readings do not establish persistent widening** — the post-episode level returned near the August baseline. ⛔ 3 claims withdrawn → **§ WITHDRAWN** | shares the heat antecedent w/ P1 | **+$28.26/MWh same-vintage** (on-peak HE08–23, **9/4–9/9**, n=1,151, RT LMP $47.89 − 7.0 × HH $2.805 @9/10); @HR 8.0 **+$25.45**. Clean post-episode 9/4–9/5 **+$28.98**. Series on one basis: **+$29.84 (8/4) → +$48.12 (8/17) → +$28.98 → +$28.26** | compresses 50% or negative, sustained 3+ sessions → 3 — **on ONE consistent basis and ONE uncontaminated window** |

**Composite: 16/20** *(P1 5 + P2 5 + P3 4 + P4 2 — net unchanged since 9/25: P1 5→3 as of 9/26 (de-escalation graded late), 3→5 on 10/7 (RED re-fire, forced by the DM2 tape + EIA-930, KB-133). P2/P3/P4 unmoved.)*

**⚠️ Status 🔴 on the letter, transient in state.** A 25-minute spike with no operator action scores 5 because the demand limb fires at nearly any evening peak — the second time (9/16, 10/7). The letter is graded as written; the limb's weakness is a re-spec question for the owner (not moved here — gate letters go through PROME/Will). ⚠️ **Still no deploy-posture change** (TERRY Non-Negotiable #15); see `TRADE.md`. *9/25 paragraph → Block BI.*

**⏸ TRIGGERED CHANNEL — B1 battery export controls (registered 9/25; NOT open, NOT scored, NOT in the composite).** *Ruled by PROME 9/22 (DOCKET L437, Will → PROME 9/19); trigger wording ZHAO's (9/25, KB-ZHAO-187), channel wording mine.* **Channel:** China's 公告2025年第58号 controls — **11 body codes incl. LFP cathode ≥2.5 g/cm³ AND ≥156 mAh/g (3C901.a.1)**, cells ≥300 Wh/kg, graphite anode, cell/cathode/anode equipment + technology — **→ grid-storage (LFP, >80% of new stationary installs, industry B2) supply/cost → storage buildout pace in PJM/ERCOT**. **Opens on T1:** the first day NO MOFCOM suspension instrument covers 58 (today 公告2025年第70号, 「至2026年11月10日」 ⇒ window **11/10–11/11 Beijing**; 「至」 inclusivity INFERRED); graded **only** on a mofcom.gov.cn announcement — an extension re-dates T1 automatically. **Or T2 (≥10/19):** a PRC official source says the suspension ends / will not be extended, **or** MOFCOM publishes implementing material for 58. ⛔ MOFCOM silence ≠ positive · US statements (Bessent's "to 1/10/2027"), readouts, press, BIS Affiliates Rule, market moves **never** trip it. **Guards:** magnitude UNKNOWN, not large · first use, no precedent · ⛔ never carry "300 Wh/kg spares stationary storage". Finished-cell (EV) leg UNOWNED.

---

## LIVE CHANNEL READS (sourced + dated)

- **P1 — Stress → price** 🔴🔴 **5 on the letter (re-fired 10/7, demand limb)** [DM2 5-min 9/25–10/9 + gen_outages_by_type, pulled 10/9 · EIA-930 · PJM board 10/9 · DOE index 10/9]. 10/7 detail → KB-WATT-132/133; outage stack → KB-134. **The emergency load keeps falling as outages rise:** 159.0 GW (July) · 152.5 (9/1) · ~127.7 (9/16) · **~94 GW (10/7, price only)**.
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

**14 claims withdrawn or scoped (9/6 review + 9/10)** — register verbatim → archive Blocks BE + § `CORRECTIONS_LEDGER_FULL_2026-09-06`; reasoning → `LESSONS.md` L-46…L-51.

**The standing do-not-reassert list, in one line each:**
⛔ **Do-not-reassert, in eight words each (full list verbatim → archive Block V):** backup generation *authorised, not observed* (authority lapsed, record still ❌) · 55 GW seam agreed on the *number* · P2/P3 *linked* roots · 28/29 cleared at *100%* of its own cap · 9/1 = *episode* peak, not season · spark neither *widened* nor *never moved* · reconstruction = *sensitivity analysis* · autumn non-heat emergency *opens an investigation*.

## EXIT / INVALIDATION (standing-rule-vs-state triad)

**Kill rail re-derived: 2026-09-02** *(TESTED, not rewritten, on 9/6 and again on 9/10.)*

| Channel | Standing rule | Current state @ level | FIRED? |
|---|---|---|---|
| P1 | **As re-specified 8/17, unchanged:** EEA2+ posting **OR** (LMP ≥$1,000 sustained 2+ **consecutive 5-min** intervals **AND** [emergency-class posting live **OR** demand ≥97% of trailing 24h peak]) | **FIRED 10/7 17:45–17:50 (demand limb, no posting).** 10/8–10/9 09:55: 0 intervals ≥$1,000; no emergency-class posting; Capacity Advisory for 10/12 | **🔴 FIRED on 4 days this season (9/2, 9/16, 9/17, 10/7).** Live rail **NOT-FIRED as of 10/9 09:55** |
| P2 | BRA clears at cap AND short of reliability req | 26/27 + 27/28 + **28/29 all at cap**; 27/28 + 28/29 both RTO-wide short | **FIRED — at MAX (5)** (3 consecutive at-cap, 2 consecutive shortfalls) |
| P3 | PJM **ACTIVE** gen-interconnection queue (Cycle intake **+** transition remainder, nameplate MW) **> 2× forecast summer peak** | **≈250 GW = 1.56×** the 160,451 MW 2027 peak (wider tracker definition 1.76×; Cycle-1-only 1.37×). **Trip needs ≈321 GW.** IPP guidance reaffirmed, not raised | **NOT-FIRED on every basis.** ⚠️ **score ≠ triad** — P3=4 came from the demand-side discriminator, not this |
| P4 | spark spread negative (gas-fired uneconomic) sustained 3+ sessions | **+$28.26/MWh** same-vintage on-peak (9/4–9/9, n=1,151) — positive, and **flat vs the 8/4 baseline (+$29.84), not widening** | **NOT-FIRED** — comfortably. ⚠️ **The "moving away from the trigger" note carried since 8/17 is WITHDRAWN**: it was window composition. Distance-to-trigger unchanged since August |

**Fired-count: 2 of 4** *(P1 + P2)*. **P1's last firing day = 10/7.** **Thesis-kill vs channel-kill:** the shoulder season is a fragility window, not a dormant one — `WATT-12` HIT on outages alone (no heat), so **FL-WATT-15 is CONFIRMED-PARTIAL**. Still no reserve-margin-erosion finding (planned outages are scheduled, and PJM's advisory names recalling them as its first lever). The thesis dies only if the 29/30 BRA clears well below cap **AND** data-centre queues drain. *9/25 narrative → Block BI.*

**Bidirectional flip → archive Blocks BC + Z:** structural = the **29/30 BRA** (~mid-2027); near-term = **FERC on IRAS (WATT-10)**.

---

## INSTRUMENT — the two operative facts (reasoning → **L-44**, KB-WATT-101/104; long form → archive)

① 5-min feed keeps **~15 days**, short windows return NO error (assert per-day coverage) · ② contamination flag = single-day detector, silence ≠ clean · ③ `rt_hrl_lmps` keeps **≥67 days**. *Full text → archive Blocks BF + U.*

---

## OPEN ON WATT (compact — working detail lives in `SCRATCH.md` § PICK UP HERE; one home per fact)

*Closed items through 9/11 → archive Block BD.*

| # | item | when |
|---|---|---|
| 2 | 🔴 **P1 de-escalation 5→3 — RE-ARMED** after the 10/7 re-fire: execute at the first boot ≥**10/15** if 10/8–10/14 carry no EEA-class posting and no new PJM §202(c). **10/12 Capacity Advisory day** is the test (KB-134). Residual: 202-26-41/-45 utilisation reports (limb (c)) | **≥10/15** |
| 3 | 🟠 **IRAS** — **FERC order NOT YET ISSUED as of 10/9 10:01 ET** (eLibrary ER26-3515: 5 issuances, all notices, latest 9/2; answers still being filed — IMM 10/8). The secondary "10/9 deadline" has no support on the docket (KB-135). Residual: EL26-67 relationship | **~10/12**, outer 10/31 |
| 4 | 🟠 **The 6.5 GW gap** (July @159,046 vs Sept @152,518 MW) — still INFERRED. 5-min route closed; use the DM2 **generation-outage** series, method per KB-WATT-089 | open |
| 5 | 🟡 **Predictions: 3 OPEN** — WATT-08 (2027-06-30) · WATT-09 (~11/30, contingent) · WATT-10 (10/31 outer) · ~~WATT-12~~ **HIT 10/9** (10/7 $2,978) → archive · ~~WATT-11~~ MISS 9/25 | — |
| 6b | 🟠 **CONDITIONAL, NOT a dated catalyst — premise open.** The 9/1–9/3 window reaches `FL-WATT-08` by **PRICE** on a ~3-month lag (trailing-3-month mark, ~Dec 2026), but the covenant marks *Excess **UNHEDGED*** costs. 🔑 **Resolve the hedged/floating split FIRST — the date exists only on one branch.** *Detail → archive Block J* | premise first |
| 8 | ⚠️ **Winter P1 gate HELD** — basis KB-WATT-076, **do not re-derive**. Never *"no EEA because El Niño"*: **peak-based, sign-agnostic.** 🔑 **The MW level at which PJM goes to emergency is not a constant.** Never mix ONI +2.03 / +1.2 | mid-Jan–Feb 2027 |
| 9 | 🟡 **ERCOT Cal-27 discriminator** — still INFERRED; pairs a **chart-read** level with **spot** gas. ⚠️ **Never quote chart-reads as settles** | open |
| 10 | 🟡 **Lower urgency:** NG=F settlement clock (N5 i-b) · **KB-WATT-034 metered-vs-DR split — overdue; re-stated to PROME 10/9 as a DOCKET row (review 10/23)** · **para-E utilisation report** (the one route off limb (c) UNKNOWN) · Oracle/We Energies · Hut8 · TSMC-AZ · EIA-923 heat rate. *Verbatim → archive Block AA* | mixed |
| 11 | 🟠 **What drove the 8/13–8/16 spark elevation?** No posting, no §202(c); asked BRENT + AEOLUS 9/6, **no answer yet**. **Do not attach a cause without measuring one** | open |
| 12 | ✅ **Dark-desk routing gap — CLOSED by PROME 10/2** (DOCKET L487 RESOLVED: WATCH_FOR["WATT"] landed 9/25; DAEDALUS dark_window_check.py exists, alert level N is Will's, L596). WATT's half = the weekly cadence. ⚠️ A price-only spike (10/7) has no headline and no posting, so **no intake term can see it** — only a tape pull can | — |
| 13 | 🟡 **Appalachian gas basis (P4) — UNMEASURED, sign UNKNOWN.** BRENT (9/25): no free primary for hub basis (a paid feed is Will's call); force majeure in effect "until further notice" [SECONDARY]; production-area basis likely **weakens** (takeaway cut) ⇒ HH-based spark errs HIGH for western PJM, if anything. **Do not fire or un-fire P4 on it** | open (no instrument) |
| 14 | 🟡 **Inbox deferrals (10/9):** L546 LATENT `power_watch.py:178` demand-% float (feeds the ≥97% limb) — round before compare at the next instrument touch, **review 10/23** · AEOLUS's interchange test (was PJM exporting into MISO/TVA on 9/16–17?) — not run, open | 10/23 |

## WAKE SET — dated near-term only (full 12-row table → archive; routing → `NEXUS_BRIEF.md`)

| trigger | date | why it needs WATT |
|---|---|---|
| **P1 re-escalation watch** | any boot | re-fire on the RED conjunction; **70.8 GW offline (10/9)**; KILL_MEMO cascade on C1/C2/C3 |
| **PJM Capacity Advisory day** | **Mon 10/12** | first P1 test after the re-fire; an alert/EEA posting resets the 10/15 de-escalation |
| **🔴 EEA-2/3, voltage reduction, load shed** | any time | the only P1 state above the current one — KILL_MEMO cascade |
| **FERC order on IRAS `ER26-3515-000`** | **~10/12** requested effective, outer 10/31 | resolves **WATT-10**; not issued as of 10/9 10:01 ET |
| **FERC ruling, 3 EL26-67 abeyance motions** | overdue since ~8/07 (~30d) | sets **WATT-09**'s resolve date |
| **WATCH_FOR["WATT"] 14-term review** (DOCKET L487) | **10/31** | review the PJM-emergency wake list (16 terms incl. 2 FERC) at the date WATT-12 was set to close; WATT-12 resolved HIT 10/9, the review date stands |
| **Weekly cadence** (WQ-295) | next boot **≤10/16** | 5-min feed keeps ~15 days; a price-only spike reaches no headline |
| ⚠️ **CONDITIONAL, not a catalyst — CRWV DSCR mark** | *~Dec 2026 **IF** largely floating* | premise (hedged/floating split) UNRESOLVED — see OPEN 6b; not a registered dated trigger |
| **B1 T2 re-check (ZHAO)** | **≥10/19** | battery channel opens early only on a PRC official signal or MOFCOM implementing material — silence is not positive |
| **B1 T1 — 公告70 suspension lapse** | **11/10–11/11 (Beijing)** | channel opens if no MOFCOM instrument covers 58; an extension re-dates it |
| **ERCOT Batch Zero PUCT filings** | **12/10** | large-load energization paused until then; changes no registered WATT item (KB-137) |
| **NERC ride-through provisions filed** | by **2026-12-31** | the un-sized AI-capex compliance cost line |
| **Winter P1 window** *(gate HELD)* | **mid-Jan–Feb 2027** | peak-based, sign-agnostic, never "no EEA because El Niño" |

## BOTTOM LINE

**PJM's real-time price spiked to ~$2,978/MWh for ten minutes on 10/7, at only ~94 GW of load, because ~70 GW of generation is offline for autumn maintenance — up from 45 GW two weeks ago.** No heat, no emergency posting, no DOE order: the outage stack alone produced a shortage price, so `WATT-12` is a **HIT** and the shoulder-season fragility reading is now confirmed-in-part. On the letter P1 re-fires to 5 (after a 9/26 de-escalation that should have run and didn't), but on the weak demand limb — this is a price event, not a grid emergency. **Next:** PJM has flagged **Mon 10/12** as a tight-capacity day (Capacity Advisory) · FERC has **not yet** ruled on IRAS (10:01 ET 10/9; requested effective 10/12) · P1 de-escalates at the first boot ≥10/15 if 10/12 passes without an alert. *9/25 bottom line → Block BI.*
