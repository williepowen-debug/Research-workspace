# WATT — STATUS

**Last Updated:** 2026-10-12 12:31 ET — **final records-only closeout**, Will-directed; power observation remains **2026-10-12 10:35 EPT**, no new tape/DOE read. P1 **5 HELD**; WATT-10 **MISS**; WATT-08 **~50% OPEN**. Composite **16/20** unchanged.
**Class:** Market-agent (grid stress → power price → power cost) · **Spawnable by:** PROME or Will · **Maturity:** **L4 (Conf H)** *(DAEDALUS 2026-09-05)*
**Read-cap budget:** **32,550 B** per boot-read surface (root `CLAUDE.md` §Data Hygiene; binding above any owner number). Old "64,000 B" line retired → archive Block BG.
**Superseded content →** `status_archive/STATUS_ARCHIVE_2026-10.md` (Oct rotations; Blocks BH– moved 10/9) · `status_archive/STATUS_ARCHIVE_2026-09.md` (Sept rotations, per-block bytes + crc32 in its manifests; Blocks L–AC moved 9/11; **AD–AW moved 9/25**) · `status_archive/STATUS_ARCHIVE_2026-08.md` (**CLOSED**) · `archive/SCRATCH_ARCHIVE_2026-07-08.md`

**Read-cap:** read the figure from `boot.py` leg 3 / `PROME/tools/measure.py`, never from this sentence. 9/25 rotations: Blocks AD–BG verbatim, bytes + crc32 in the archive manifest. Rotation, never deletion.

> **October 12 L654:** morning max **$52.90/MWh through 10:35 EPT**; no EEA-class posting. Advisories extend October 12–14; maintenance recall due October 14 noon. PJM replaced a one-minute “obtained” DOE notice with “requested”; new issuance UNKNOWN. **WATT-10 MISS**; **WATT-08 ~50% OPEN**. Report and KB-WATT-138…144 carry evidence and caveats.

> **Closeout coordination:** PROME's exact consumption and publication receipt is `PROME/reports/2026-10-12_WATT-L654-L200-consumption.md` (30770e3bb); prior “pending publication/approval” warnings are superseded. Existing event follow-ups registered L692/L693. Procedure comparison saved; protocol unchanged.

---

## CONVERGENCE MATRIX (universal 5-pt + local state)

| # | Channel | Score (1–5) | Local state | Independence | Key signal [src, date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| **P1** | Stress → price | **5**, held from 10/7 | No new observed RED 10/9–10/12 **through 10:35**; morning max $52.90. No EEA-class posting. Maintenance recall and DOE backup request; new issuance/use unverified | shared outage-season root; count once | [PJM DM2/board 10/12] daily outage forecast **62,592 MW**; advisories 10/12–14. Superseded “obtained” notice ended one minute later | →3 earliest **10/15** IF complete 10/8–14 clear window and no new DOE order; resolve request. EEA2+ triggers cascade review |
| **P2** | Structural capacity cost | **5 🔴🔴** | confirmed short — **3 straight at-cap clears, 2 straight RTO-wide shortfalls**; **IRAS/BYONC core REJECTED 10/9; definition/registry only accepted. WATT-10 MISS; Door B confidence ~50%.** ⭐ limb (c)'s mechanism was **AUTHORISED**, never observed running — **and that authority lapsed 9/8 unmeasured** | independent (auction structure); IRAS is a **regulatory** root. ⚠️ **The 9/1 §202(c) order is NOT independent of P1** — same heat episode, count once | 26/27 **$329.17 cap**; 27/28 **$333.44 cap** (6,623 MW short); **28/29 cleared 7/14 at $325 = AT its own cap (100%), 6,831 MW short**, uncapped sim $554.72, **$16.4B** [PJM Inside Lines 7/14, VERIFIED]. **FERC 197 FERC ¶61,019, 10/9: definition/registry effective 10/12; integrated IRAS/BYONC rejected. Compliance within 30 days; cost allocation unresolved** | de-escalate only if 29/30 BRA clears below cap AND queues drain |
| **P3** | Data-center demand leg | **4 🔴** | held at 4 — unchanged. Demand leg intact. **authority ✅ · deployment ❓UNKNOWN · utilisation record ❌** — **and the §202(c) authority LAPSED 9/8 with the record still ❌.** ✅ ACTION #105472 (5 zones) **was** dispatched = demand response. ⚠️ **Texas large-load milestones [9/8] are CONDITIONAL, not operating** | couples to HEN-36 AI-capex | **PJM 32 GW** peak-load growth 2024–30, **30 GW (94%) data centers** [PJM via DCD]. **WoodMac 55 GW/2030** (utility-self-reported). **Active queue ≈250 GW = 1.56×** the 160,451 MW peak; **needs 2× ≈321 GW.** Mix: gas 106 GW (48%), storage 67, nuclear 18, solar 15, s+s 9, wind 5 | **ACTIVE queue > 2× forecast summer peak** OR IPP load-growth guide **raised** (not reaffirmed) → 5 |
| **P4** | Gas → power coupling | **2**, held | NOT-FIRED; no direction inference from stress window | 10/7 outlier shares P1 root | [boot 10/12] **+$37.23/MWh**, HR7: power $59.20 on-peak 10/6–11 n=1,142 minus NG=F $3.139 dated 10/12; HR8 +$34.09. **Intraday gas, not settlement; 10/7 outlier** | Negative 3+ sessions on one consistent basis; no widening claim from this window |

**Composite: 16/20** *(P1 5 + P2 5 + P3 4 + P4 2 — net unchanged since 9/25: P1 5→3 as of 9/26 (de-escalation graded late), 3→5 on 10/7 (RED re-fire, forced by the DM2 tape + EIA-930, KB-133). P2/P3/P4 unmoved.)*

**⚠️ Status 🔴 on the letter, transient in state.** A 25-minute spike with no operator action scores 5 because the demand limb fires at nearly any evening peak — the second time (9/16, 10/7). The letter is graded as written; the limb's weakness is a re-spec question for the owner (not moved here — gate letters go through PROME/Will). ⚠️ **Still no deploy-posture change** (TERRY Non-Negotiable #15); see `TRADE.md`. *9/25 paragraph → Block BI.*

**⏸ TRIGGERED CHANNEL — B1 battery export controls (registered 9/25; NOT open, NOT scored, NOT in the composite).** *Ruled by PROME 9/22 (DOCKET L437, Will → PROME 9/19); trigger wording ZHAO's (9/25, KB-ZHAO-187), channel wording mine.* **Channel:** China's 公告2025年第58号 controls — **11 body codes incl. LFP cathode ≥2.5 g/cm³ AND ≥156 mAh/g (3C901.a.1)**, cells ≥300 Wh/kg, graphite anode, cell/cathode/anode equipment + technology — **→ grid-storage (LFP, >80% of new stationary installs, industry B2) supply/cost → storage buildout pace in PJM/ERCOT**. **Opens on T1:** the first day NO MOFCOM suspension instrument covers 58 (today 公告2025年第70号, 「至2026年11月10日」 ⇒ window **11/10–11/11 Beijing**; 「至」 inclusivity INFERRED); graded **only** on a mofcom.gov.cn announcement — an extension re-dates T1 automatically. **Or T2 (≥10/19):** a PRC official source says the suspension ends / will not be extended, **or** MOFCOM publishes implementing material for 58. ⛔ MOFCOM silence ≠ positive · US statements (Bessent's "to 1/10/2027"), readouts, press, BIS Affiliates Rule, market moves **never** trip it. **Guards:** magnitude UNKNOWN, not large · first use, no precedent · ⛔ never carry "300 Wh/kg spares stationary storage". Finished-cell (EV) leg UNOWNED.

---

## LIVE CHANNEL READS (sourced + dated)

- **P1 — 5 HELD** [DM2/board/DOE 10/12; KB-138/139/144]: no new fire **through 10:35**. Maintenance recall due 10/14 noon; advisories 10/12–14; **202(c) requested, new issuance unverified**. Observed daily tape maxima 10/9–11: $316.17/$295.19/$624.66; 10/12 morning $52.90. Outage forecast 62,592 MW, not live availability; recall causality not isolated.
  **The episode, from primaries** → archive Block AX + KB-121/122: Max Gen / Load Mgmt Alert for 9/17 issued 9/16 (>35 GW planned outages, exports south/west); DR dispatched 9/17; **DOE 202-26-45** (9/17–9/18, backup generation at large loads before/during EEA-3). Max Gen Alert = **NERC EEA-1**; no EEA-2 found.
  **Why it happened** → archive Block AY + KB-123: forced ~10.5 GW (ordinary) · **planned 0 → 16.1 GW on 9/12** (part may be classification) · total 38.5 GW (9/16) → **44.8 GW (9/25)**. `WATT-11` step 2: measured planned-outage cluster ⇒ **no P2 escalation.** Backup-generation authority granted a 3rd time; utilisation still ❌.
  Retail backdrop [EIA, 2026-07]: industrial **9.77¢/kWh**, residential **18.31¢/kWh**. ⚠️ **The load at which PJM goes to emergency now has three points:** 159,046 MW (July) · 152,518 (9/1) · **~127,700 (9/16–9/17)** — it falls as outages rise, so **a peak-load threshold cannot see a shoulder-season emergency** (L-53; OPEN #4's 6.5 GW gap is now one instance of this).
- **P2 — 5 HELD**: auction cap/short unchanged. **FERC rejected IRAS/BYONC 10/9**, accepting definition/registry only (KB-140). Proposed tariff cost/curtailment burden removed; physical/contracted expenses persist. Emergency backup-generator deployment remains unobserved; new request is not proof of issuance.
- **P3 — Data-center demand leg** 🔴 **held at 4, unchanged** — 32 GW firm coincident vs 55 GW utility-reported (non-coincidence + duplication, NOT a haircut); Texas large-load milestones CONDITIONAL. Full bullet → archive Block BA.
  ✅ **VULCAN seam CLOSED 9/25 at ITS artifact** — `VULCAN/STATUS.md` S3 rows (lines 29, 53, 73 as read 9/25) carry the corrected population wording verbatim ("~55 GW aggregate utility-reported forecast / ~32 GW firm coincident-peak … NOT a nameplate or queue figure"), adopted 9/6 across 8 surfaces [DAEDALUS PR-6 R4 claim 4; re-read 9/25].
- **P4 — 2 NOT-FIRED** [KB-142, boot 10/12]: provisional stress-window **+$37.23/MWh**, HR7, 10/6–11 n=1,142; HR8 +$34.09. NG=F $3.139 dated 10/12 is intraday, not settlement; October 7 contaminates the window. **No persistent widening/compression claim.** Appalachian basis and settlement clock remain unmeasured.


### P2 — the regulatory layer → archive (full text, verbatim)
**Graded copy:** `workbook/PREDICTIONS.tsv` WATT-08/09 OPEN; `workbook/PREDICTIONS_ARCHIVE.tsv` WATT-10 MISS (10/9 order, graded 10/12); KB-140/141.
**Regulatory current 10/12:** ER26-3515 verified; IRAS/BYONC rejected 10/9. Definition/registry accepted effective 10/12, compliance within 30 days. WATT-08 **~50% OPEN**, 2027-06-30; actual socialization unresolved. **EL26-67 abeyance granted 8/14**: responses **11/16**, answers **12/16**; qualifying section 205 filing can suspend that respondent’s duty. WATT-09 OPEN, outer 11/30 unchanged. Companion backstop not graded here; any refile needs a new primary read.

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
| P1 | **8/17 letter unchanged:** EEA2+ OR (LMP ≥$1,000 for 2+ consecutive 5-min AND [posting OR demand ≥97% trailing 24h peak]) | Last FIRED **10/7**. No new observed RED 10/9–10/12 **through 10:35**; no EEA-class posting; DOE request pending | **NOT-FIRED at this read; historical fire on 4 days**: 9/2, 9/16, 9/17, 10/7 |
| P2 | BRA clears at cap AND short of reliability req | 26/27 + 27/28 + **28/29 all at cap**; 27/28 + 28/29 both RTO-wide short | **FIRED — at MAX (5)** (3 consecutive at-cap, 2 consecutive shortfalls) |
| P3 | PJM **ACTIVE** gen-interconnection queue (Cycle intake **+** transition remainder, nameplate MW) **> 2× forecast summer peak** | **≈250 GW = 1.56×** the 160,451 MW 2027 peak (wider tracker definition 1.76×; Cycle-1-only 1.37×). **Trip needs ≈321 GW.** IPP guidance reaffirmed, not raised | **NOT-FIRED on every basis.** ⚠️ **score ≠ triad** — P3=4 came from the demand-side discriminator, not this |
| P4 | Spark negative for 3+ sessions on a consistent basis | **+$37.23/MWh** provisional 10/6–11 stress window; intraday gas dated 10/12, outlier flag | **NOT-FIRED**; direction claim withheld |

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
| 2 | 🔴 **P1 de-escalation 5→3 — RE-ARMED** after the 10/7 re-fire: execute at the first boot ≥**10/15** if 10/8–10/14 carry no EEA-class posting and no new PJM §202(c). **October12–14 advisory window (L692)** is the test (KB-134). Residual: 202-26-41/-45 utilisation reports (limb (c)) | **≥10/15, L693** |
| 3 | **IRAS resolved:** WATT-10 MISS; WATT-08 ~50% OPEN; EL26-67 responses 11/16 with section205 proviso. **PROME consumed** exact report427c1280f/deliveryd9127ded0 at its L654/L200 receipt. Other consumer acknowledgments unknown | compliance within30days;11/16response |
| 4 | 🟠 **The 6.5 GW gap** (July @159,046 vs Sept @152,518 MW) — still INFERRED. 5-min route closed; use the DM2 **generation-outage** series, method per KB-WATT-089 | open |
| 5 | **2 OPEN predictions:** WATT-08 (2027-06-30), WATT-09 (11/16 response; 11/30 outer). WATT-10 **MISS**, archived 10/12; WATT-12 HIT, archived 10/9 | — |
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
| **PJM advisory / maintenance window — L692** | **10/13–10/14; recall10/14noonEPT** | Includes fullOctober12 outcome. Lastreadonly10:35; DOEissuance/use unverified; no automatic future execution claimed |
| **🔴 EEA-2/3, voltage reduction, load shed** | any time | the only P1 state above the current one — KILL_MEMO cascade |
| **IRAS compliance / any revised section 205 proposal** | within 30 days of 10/9 order | WATT-10 MISS; definition/registry only accepted. Refile date unverified |
| **EL26-67 show-cause response** | **11/16; answers 12/16** | Abeyance granted 8/14; qualifying section 205 filing may suspend duty. WATT-09 outer 11/30 unchanged |
| **WATCH_FOR["WATT"] 14-term review** (DOCKET L487) | **10/31** | review the PJM-emergency wake list (16 terms incl. 2 FERC) at the date WATT-12 was set to close; WATT-12 resolved HIT 10/9, the review date stands |
| **Weekly cadence** (WQ-295) | next boot **≤10/19**; event checks sooner | Price-only events need tape pulls; advisories through 10/14 |
| ⚠️ **CONDITIONAL, not a catalyst — CRWV DSCR mark** | *~Dec 2026 **IF** largely floating* | premise (hedged/floating split) UNRESOLVED — see OPEN 6b; not a registered dated trigger |
| **B1 T2 re-check (ZHAO)** | **≥10/19** | battery channel opens early only on a PRC official signal or MOFCOM implementing material — silence is not positive |
| **B1 T1 — 公告70 suspension lapse** | **11/10–11/11 (Beijing)** | channel opens if no MOFCOM instrument covers 58; an extension re-dates it |
| **ERCOT Batch Zero PUCT filings** | **12/10** | large-load energization paused until then; changes no registered WATT item (KB-137) |
| **NERC ride-through provisions filed** | by **2026-12-31** | the un-sized AI-capex compliance cost line |
| **Winter P1 window** *(gate HELD)* | **mid-Jan–Feb 2027** | peak-based, sign-agnostic, never "no EEA because El Niño" |

## BOTTOM LINE

**FERC rejected IRAS/BYONC on October 9: WATT-10 is a MISS and the broader large-load cost-assignment forecast stays OPEN at ~50%.** Definition/registry alone were accepted effective October 12; rejection does not establish actual socialization or remove physical/contracted expenses. PJM’s October 12 tape is quiet **through 10:35 EPT** (max $52.90/MWh), but advisories extend through October 14, maintenance outages are recalled by October 14 noon, and new backup-generation authority is **requested, not verified issued**. P1 stays 5; de-escalation needs the complete clear window and DOE recheck at the first boot on/after October 15.
