# WATT — STATUS

**Last Updated:** 2026-10-15 08:13 ET — **L692/L693 graded (PROME Tier-1 wake; crash-recovery session)**; market observation **through 2026-10-15 08:07 ET** (board/DOE/DM2/EIA-930; 10/12–10/14 tapes complete). P1 **5 HELD — RED re-fired 10/13; de-escalation NOT MET**; WATT-08 **~50% OPEN**; composite **16/20** unchanged.
**Class:** Market-agent (grid stress → power price → power cost) · **Spawnable by:** PROME or Will · **Maturity:** **L4 (Conf H)** *(DAEDALUS 2026-09-05)*
**Read-cap budget:** **32,550 B** per boot-read surface (root `CLAUDE.md` §Data Hygiene; binding above any owner number). Old "64,000 B" line retired → archive Block BG.
**Superseded content →** `status_archive/STATUS_ARCHIVE_2026-10.md` (Oct rotations; Blocks BH– moved 10/9) · `status_archive/STATUS_ARCHIVE_2026-09.md` (Sept rotations, per-block bytes + crc32 in its manifests; Blocks L–AC moved 9/11; **AD–AW moved 9/25**) · `status_archive/STATUS_ARCHIVE_2026-08.md` (**CLOSED**) · `archive/SCRATCH_ARCHIVE_2026-07-08.md`

**Read-cap:** read the figure from `boot.py` leg 3 / `PROME/tools/measure.py`, never from this sentence. 9/25 rotations: Blocks AD–BG verbatim, bytes + crc32 in the archive manifest. Rotation, never deletion.

> **October 13–14 = PJM's 5th capacity emergency of 2026 (L692/L693, KB-147…151):** DOE §202(c) **202-26-50 ISSUED 10/12** (effective 10/13–16); EEA-1 Max Gen/Load Mgmt Alerts for 10/13 and 10/14; CP demand response dispatched ×4; **RED re-fire 10/13** — 29 consecutive 5-min ≥$1,000 (17:30–19:50 EPT), peak $2,327.04, at ~108 GW load with ~61 GW offline. No EEA-2 (M-13 rev 98 §2.3.2), no load shed; PJM: no large-load backup generation used (10/13). **L693: 10/8–14 window NOT MET → P1 stays 5; re-test first boot ≥10/22.** 10/15 clear through 08:07 ET, but the outage forecast is 67.7 GW (KB-155). Report: `reports/2026-10-15_DOCKET-L692-L693_PJM-emergency-clear-day-grade.md`.

> **Correction 10/15 (KB-152):** KB-047's CoreWeave "exactly two things / no power percentage" hedge inference is **withdrawn** (Top-Up clause (c) verified by WATT; §5.25 redacted power percentages per PROME's primary read). Hedged share stays UNKNOWN. October 12 L654/L200 coordination receipt: `PROME/reports/2026-10-12_WATT-L654-L200-consumption.md` (30770e3bb).

---

## CONVERGENCE MATRIX (universal 5-pt + local state)

| # | Channel | Score (1–5) | Local state | Independence | Key signal [src, date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| **P1** | Stress → price | **5**, held; **RED re-fired 10/13** | 5th emergency episode 10/13–14: EEA-1 both days, DR ×4, DOE 202-26-50 (10/13–16). 10/14 two ≥$1,000 prints, not consecutive. PJM: conditions end after 10/14. 10/15 clear through 08:07 ET | shared outage-season root; 202-26-50 shares P1's root — count once | [DM2/board/DOE/EIA-930 10/14–15] 10/13 29-interval run, max **$2,327.04**; peak load **108,122 MW**; outages **61.9 GW** (10/14), **67.7 GW** forecast 10/15 | →3 earliest first boot **≥10/22** IF 10/15–10/21 clear, 202-26-50 lapses 10/16 unrenewed, no RED re-fire. EEA2+ triggers cascade review |
| **P2** | Structural capacity cost | **5 🔴🔴** | confirmed short — **3 straight at-cap clears, 2 straight RTO-wide shortfalls**; **IRAS/BYONC core REJECTED 10/9; definition/registry only accepted. WATT-10 MISS; Door B confidence ~50%.** ⭐ limb (c)'s mechanism was **AUTHORISED**, never observed running — **and that authority lapsed 9/8 unmeasured** | independent (auction structure); IRAS is a **regulatory** root. ⚠️ **The 9/1 §202(c) order is NOT independent of P1** — same heat episode, count once | 26/27 **$329.17 cap**; 27/28 **$333.44 cap** (6,623 MW short); **28/29 cleared 7/14 at $325 = AT its own cap (100%), 6,831 MW short**, uncapped sim $554.72, **$16.4B** [PJM Inside Lines 7/14, VERIFIED]. **FERC 197 FERC ¶61,019, 10/9: definition/registry effective 10/12; integrated IRAS/BYONC rejected. Compliance within 30 days; cost allocation unresolved** | de-escalate only if 29/30 BRA clears below cap AND queues drain |
| **P3** | Data-center demand leg | **4 🔴** | held at 4 — unchanged. Demand leg intact. **authority ✅ · deployment ❓UNKNOWN · utilisation record ❌** — **and the §202(c) authority LAPSED 9/8 with the record still ❌.** ✅ ACTION #105472 (5 zones) **was** dispatched = demand response. ⚠️ **Texas large-load milestones [9/8] are CONDITIONAL, not operating** | couples to HEN-36 AI-capex | **PJM 32 GW** peak-load growth 2024–30, **30 GW (94%) data centers** [PJM via DCD]. **WoodMac 55 GW/2030** (utility-self-reported). **Active queue ≈250 GW = 1.56×** the 160,451 MW peak; **needs 2× ≈321 GW.** Mix: gas 106 GW (48%), storage 67, nuclear 18, solar 15, s+s 9, wind 5 | **ACTIVE queue > 2× forecast summer peak** OR IPP load-growth guide **raised** (not reaffirmed) → 5 |
| **P4** | Gas → power coupling | **2**, held | NOT-FIRED; no direction inference from stress window | 10/13–14 outliers share P1 root | [boot 10/15] **+$89.20/MWh**, HR7: power $112.00 on-peak 10/9–14 n=1,141 minus HH $3.257 dated 10/15; HR8 +$85.94. **Intraday gas, not settlement; 10/13 + 10/14 outliers** | Negative 3+ sessions on one consistent basis; no widening claim from this window |

**Composite: 16/20** *(P1 5 + P2 5 + P3 4 + P4 2 — net unchanged since 9/25: P1 5→3 as of 9/26 (de-escalation graded late), 3→5 on 10/7 (RED re-fire, forced by the DM2 tape + EIA-930, KB-133). P2/P3/P4 unmoved.)*

**⚠️ Status 🔴 on the letter.** *10/13 is different in kind: posting limb + DR + DOE order (KB-148).* Earlier: a 25-minute spike with no operator action scores 5 because the demand limb fires at nearly any evening peak — the second time (9/16, 10/7). The letter is graded as written; the limb's weakness is a re-spec question for the owner (not moved here — gate letters go through PROME/Will). ⚠️ **Still no deploy-posture change** (TERRY Non-Negotiable #15); see `TRADE.md`. *9/25 paragraph → Block BI.*

**⏸ TRIGGERED CHANNEL — B1 battery export controls (registered 9/25; NOT open, NOT scored, NOT in the composite).** *Ruled by PROME 9/22 (DOCKET L437, Will → PROME 9/19); trigger wording ZHAO's (9/25, KB-ZHAO-187), channel wording mine.* **Channel:** China's 公告2025年第58号 controls — **11 body codes incl. LFP cathode ≥2.5 g/cm³ AND ≥156 mAh/g (3C901.a.1)**, cells ≥300 Wh/kg, graphite anode, cell/cathode/anode equipment + technology — **→ grid-storage (LFP, >80% of new stationary installs, industry B2) supply/cost → storage buildout pace in PJM/ERCOT**. **Opens on T1:** the first day NO MOFCOM suspension instrument covers 58 (today 公告2025年第70号, 「至2026年11月10日」 ⇒ window **11/10–11/11 Beijing**; 「至」 inclusivity INFERRED); graded **only** on a mofcom.gov.cn announcement — an extension re-dates T1 automatically. **Or T2 (≥10/19):** a PRC official source says the suspension ends / will not be extended, **or** MOFCOM publishes implementing material for 58. ⛔ MOFCOM silence ≠ positive · US statements (Bessent's "to 1/10/2027"), readouts, press, BIS Affiliates Rule, market moves **never** trip it. **Guards:** magnitude UNKNOWN, not large · first use, no precedent · ⛔ never carry "300 Wh/kg spares stationary storage". Finished-cell (EV) leg UNOWNED.

---

## LIVE CHANNEL READS (sourced + dated)

- **P1 — 5 HELD** [DM2/board/DOE/EIA-930 read 10/14 23:45 – 10/15 08:07 ET; KB-147…151, 155]: **RED re-fire 10/13** (29 consecutive ≥$1,000, max $2,327.04 @17:50, EEA-1 #105557 live, demand 100.8% of trailing peak). 10/12 full day max $845.48, 0 RED; 10/14 max $1,083.71, not 2 consecutive. EEA-1 alerts for 10/13 + 10/14; Pre-Emergency DR ×4 (not an EEA2 trigger, M-13 rev 98 §2.3.2); **202-26-50 issued 10/12**, effective 10/13–16, backup generation last-resort only, PJM: none used to date (10/13). Same-day outages 62.6→60.6→61.9 GW; maintenance 5.8→3.4 GW after the recall. Episode #5 is supply-driven at ordinary load. **10/15:** no posting, no new DOE order, max $268.62 through 08:00; outage forecast **67.7 GW** and 65.0–68.1 GW each day through 10/21 (watch fact, not a call).
  **The episode, from primaries** → archive Block AX + KB-121/122: Max Gen / Load Mgmt Alert for 9/17 issued 9/16 (>35 GW planned outages, exports south/west); DR dispatched 9/17; **DOE 202-26-45** (9/17–9/18, backup generation at large loads before/during EEA-3). Max Gen Alert = **NERC EEA-1**; no EEA-2 found.
  **Why it happened** → archive Block AY + KB-123: forced ~10.5 GW (ordinary) · **planned 0 → 16.1 GW on 9/12** (part may be classification) · total 38.5 GW (9/16) → **44.8 GW (9/25)**. `WATT-11` step 2: measured planned-outage cluster ⇒ **no P2 escalation.** Backup-generation authority granted a 3rd time; utilisation still ❌.
  Retail backdrop [EIA, 2026-07]: industrial **9.77¢/kWh**, residential **18.31¢/kWh**. ⚠️ **The load at which PJM goes to emergency now has three points:** 159,046 MW (July) · 152,518 (9/1) · **~127,700 (9/16–9/17)** — it falls as outages rise, so **a peak-load threshold cannot see a shoulder-season emergency** (L-53; OPEN #4's 6.5 GW gap is now one instance of this).
- **P2 — 5 HELD**: auction cap/short unchanged. **FERC rejected IRAS/BYONC 10/9**, accepting definition/registry only (KB-140). Proposed tariff cost/curtailment burden removed; physical/contracted expenses persist. Emergency backup-generator deployment remains unobserved; new request is not proof of issuance.
- **P3 — Data-center demand leg** 🔴 **held at 4, unchanged** — 32 GW firm coincident vs 55 GW utility-reported (non-coincidence + duplication, NOT a haircut); Texas large-load milestones CONDITIONAL. Full bullet → archive Block BA.
  ✅ **VULCAN seam CLOSED 9/25 at ITS artifact** — `VULCAN/STATUS.md` S3 rows (lines 29, 53, 73 as read 9/25) carry the corrected population wording verbatim ("~55 GW aggregate utility-reported forecast / ~32 GW firm coincident-peak … NOT a nameplate or queue figure"), adopted 9/6 across 8 surfaces [DAEDALUS PR-6 R4 claim 4; re-read 9/25].
- **P4 — 2 NOT-FIRED** [boot 10/15]: same-vintage stress-window **+$89.20/MWh**, HR7, on-peak 10/9–14 n=1,141; HR8 +$85.94. HH $3.257 dated 10/15 is intraday, not settlement; 10/13 ($349.94) and 10/14 ($140.64) contaminate the window vs a $59.75 median. **No persistent widening/compression claim.** Appalachian basis and settlement clock remain unmeasured.


### P2 — the regulatory layer → archive (full text, verbatim)
**Graded copy:** `workbook/PREDICTIONS.tsv` WATT-08/09 OPEN; `workbook/PREDICTIONS_ARCHIVE.tsv` WATT-10 MISS (10/9 order, graded 10/12); KB-140/141.
**Regulatory current 10/12:** ER26-3515 verified; IRAS/BYONC rejected 10/9. Definition/registry accepted effective 10/12, compliance within 30 days. WATT-08 **~50% OPEN**, 2027-06-30; actual socialization unresolved. **EL26-67 abeyance granted 8/14**: responses **11/16**, answers **12/16**; qualifying section 205 filing can suspend that respondent’s duty. WATT-09 OPEN, outer 11/30 unchanged. Companion backstop not graded here; any refile needs a new primary read.

**Season emergency count = 5 episodes** (7/3 EEA2 + §202(c) precedent · 7/15–16 EEA-1 + 202-26-35 · 9/1–9/3 EEA-1 ×3 + 202-26-41 · 9/16–9/18 Max Gen / EEA-1 + DR + 202-26-45 · **10/13–10/14 EEA-1 ×2 + DR ×4 + 202-26-50**, PJM-declared end after 10/14, order to 10/16). **First three heat-peak (152–159 GW); the last two maintenance-season (~128 GW, ~108 GW).** `WATT-11` graded **MISS** 9/25. *Prior paragraph → archive Block AW.*

---

## ⛔ WITHDRAWN — do not re-assert (full 11-row register → archive)

**14 claims withdrawn or scoped (9/6 review + 9/10)** — register verbatim → archive Blocks BE + § `CORRECTIONS_LEDGER_FULL_2026-09-06`; reasoning → `LESSONS.md` L-46…L-51.

**The standing do-not-reassert list, in one line each:**
⛔ **Do-not-reassert, in eight words each (full list verbatim → archive Block V):** backup generation *authorised, not observed* (authority lapsed, record still ❌) · 55 GW seam agreed on the *number* · P2/P3 *linked* roots · 28/29 cleared at *100%* of its own cap · 9/1 = *episode* peak, not season · spark neither *widened* nor *never moved* · reconstruction = *sensitivity analysis* · autumn non-heat emergency *opens an investigation*.

## EXIT / INVALIDATION (standing-rule-vs-state triad)

**Kill rail re-derived: 2026-09-02** *(TESTED, not rewritten, on 9/6 and again on 9/10.)*

| Channel | Standing rule | Current state @ level | FIRED? |
|---|---|---|---|
| P1 | **8/17 letter unchanged:** EEA2+ OR (LMP ≥$1,000 for 2+ consecutive 5-min AND [posting OR demand ≥97% trailing 24h peak]) | **FIRED 10/13** (29 consecutive ≥$1,000 + EEA-1 live + demand 100.8%); 10/14 NOT met (non-consecutive); 10/15 none through 08:00; no EEA2+ | **NOT-FIRED at this read; historical fire on 5 days**: 9/2, 9/16, 9/17, 10/7, 10/13 |
| P2 | BRA clears at cap AND short of reliability req | 26/27 + 27/28 + **28/29 all at cap**; 27/28 + 28/29 both RTO-wide short | **FIRED — at MAX (5)** (3 consecutive at-cap, 2 consecutive shortfalls) |
| P3 | PJM **ACTIVE** gen-interconnection queue (Cycle intake **+** transition remainder, nameplate MW) **> 2× forecast summer peak** | **≈250 GW = 1.56×** the 160,451 MW 2027 peak (wider tracker definition 1.76×; Cycle-1-only 1.37×). **Trip needs ≈321 GW.** IPP guidance reaffirmed, not raised | **NOT-FIRED on every basis.** ⚠️ **score ≠ triad** — P3=4 came from the demand-side discriminator, not this |
| P4 | Spark negative for 3+ sessions on a consistent basis | **+$89.20/MWh** stress window 10/9–14; intraday gas dated 10/15, outlier flag | **NOT-FIRED**; direction claim withheld |

**Fired-count: 2 of 4** *(P1 + P2)*. **P1's last firing day = 10/13.** **Thesis-kill vs channel-kill:** the shoulder season is a fragility window, not a dormant one — `WATT-12` HIT on outages alone (no heat), so **FL-WATT-15 is CONFIRMED-PARTIAL**. Still no reserve-margin-erosion finding (planned outages are scheduled, and PJM's advisory names recalling them as its first lever). The thesis dies only if the 29/30 BRA clears well below cap **AND** data-centre queues drain. *9/25 narrative → Block BI.*

**Bidirectional flip → archive Blocks BC + Z:** structural = the **29/30 BRA** (~mid-2027); near-term = **FERC on IRAS (WATT-10)**.

---

## INSTRUMENT — the two operative facts (reasoning → **L-44**, KB-WATT-101/104; long form → archive)

① 5-min feed keeps **~15 days**, short windows return NO error (assert per-day coverage) · ② contamination flag = single-day detector, silence ≠ clean · ③ `rt_hrl_lmps` keeps **≥67 days**. *Full text → archive Blocks BF + U.*

---

## OPEN ON WATT (compact — working detail lives in `SCRATCH.md` § CURRENT PICKUP; one home per fact)

*Closed items through 9/11 → archive Block BD.*

| # | item | when |
|---|---|---|
| 2 | 🔴 **P1 de-escalation 5→3 — NOT MET (L693 graded 10/15, KB-149)** and RE-ARMED: 202-26-50 in force, EEA-1 for 10/13–14, RED 10/13. Next: clear calendar days 10/15–10/21 → first boot ≥**10/22**, if 202-26-50 lapses 23:59 10/16 unrenewed, no EEA-class posting, no new PJM §202(c), no RED. Residual: 202(c) utilisation records (para E, not public); **9/17 EEA-2 re-adjudication under M-13 rev 98 (historical, KB-150)** | **≥10/22** (PROME row requested) |
| 3 | **IRAS resolved:** WATT-10 MISS; WATT-08 ~50% OPEN; EL26-67 responses 11/16 with section205 proviso. **PROME consumed** exact report427c1280f/deliveryd9127ded0 at its L654/L200 receipt. Other consumer acknowledgments unknown | compliance within30days;11/16response |
| 4 | 🟠 **The 6.5 GW gap** (July @159,046 vs Sept @152,518 MW) — still INFERRED. 5-min route closed; use the DM2 **generation-outage** series, method per KB-WATT-089 | open |
| 5 | **2 OPEN predictions:** WATT-08 (2027-06-30), WATT-09 (11/16 response; 11/30 outer). WATT-10 **MISS**, archived 10/12; WATT-12 HIT, archived 10/9 | — |
| 6b | 🟠 **CONDITIONAL, NOT a dated catalyst — premise open.** The 9/1–9/3 window reaches `FL-WATT-08` by **PRICE** on a ~3-month lag (trailing-3-month mark, ~Dec 2026), but the covenant marks *Excess **UNHEDGED*** costs. 🔑 **Resolve the hedged/floating split FIRST — the date exists only on one branch.** 10/15: the 8/4 "material unhedged tail" tilt is withdrawn (KB-152); §5.25 sets redacted power percentages — split still UNKNOWN. *Detail → archive Block J* | premise first |
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
| **P1 re-escalation watch** | any boot | re-fire on the RED conjunction; **67.7 GW offline forecast 10/15** (65.0–68.1 GW through 10/21); KILL_MEMO cascade on C1/C2/C3 |
| **202-26-50 lapse / renewal; de-escalation re-test** | **10/16 23:59 lapse; first boot ≥10/22** | L692/L693 closed 10/15 (KB-147…149). Renewal or any new EEA-class posting re-dates the clock; no automatic monitoring claimed |
| **🔴 EEA-2/3, voltage reduction, load shed** | any time | the only P1 state above the current one — KILL_MEMO cascade |
| **IRAS compliance / any revised section 205 proposal** | within 30 days of 10/9 order | WATT-10 MISS; definition/registry only accepted. Refile date unverified |
| **EL26-67 show-cause response** | **11/16; answers 12/16** | Abeyance granted 8/14; qualifying section 205 filing may suspend duty. WATT-09 outer 11/30 unchanged |
| **WATCH_FOR["WATT"] 14-term review** (DOCKET L487) | **10/31** | review the PJM-emergency wake list (16 terms incl. 2 FERC) at the date WATT-12 was set to close; WATT-12 resolved HIT 10/9, the review date stands |
| **Weekly cadence** (WQ-295) | next boot **≤10/19**; event checks sooner | Price-only events need tape pulls; 10/12–10/15 08:00 tapes are saved under `sources/2026-10-15/` (the 5-min feed keeps ~15 days) |
| ⚠️ **CONDITIONAL, not a catalyst — CRWV DSCR mark** | *~Dec 2026 **IF** largely floating* | premise (hedged/floating split) UNRESOLVED — see OPEN 6b; not a registered dated trigger |
| **B1 T2 re-check (ZHAO)** | **≥10/19** | battery channel opens early only on a PRC official signal or MOFCOM implementing material — silence is not positive |
| **B1 T1 — 公告70 suspension lapse** | **11/10–11/11 (Beijing)** | channel opens if no MOFCOM instrument covers 58; an extension re-dates it |
| **ERCOT Batch Zero PUCT filings** | **12/10** | large-load energization paused until then; changes no registered WATT item (KB-137) |
| **NERC ride-through provisions filed** | by **2026-12-31** | the un-sized AI-capex compliance cost line |
| **Winter P1 window** *(gate HELD)* | **mid-Jan–Feb 2027** | peak-based, sign-agnostic, never "no EEA because El Niño" |

## BOTTOM LINE

**PJM ran its fifth capacity emergency of 2026 on October 13–14 — EEA-1 alerts both days, demand response called four times, DOE §202(c) Order 202-26-50 issued October 12 — and the price tape re-fired P1's RED letter on October 13 (29 straight 5-minute intervals ≥$1,000/MWh, peak $2,327.04) at only ~108 GW of load with ~61 GW offline.** The October 8–14 clear-day window therefore failed: P1 stays 5, composite 16/20, earliest de-escalation the first boot on/after October 22. No EEA-2, no load shed, no KILL_MEMO cascade; PJM said on October 13 it had not used large-load backup generation and expects conditions to end after October 14. October 15 is quiet through 08:07 ET, but PJM forecasts 65–68 GW of generation out every day through October 21, more than during the emergency. Separately, WATT withdrew its August inference that CoreWeave's unhedged power exposure is material; the hedged share is unknown.
