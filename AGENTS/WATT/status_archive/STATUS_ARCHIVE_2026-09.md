# WATT — STATUS ARCHIVE, rotations made in 2026-09

**Container rule (adopted 2026-09-02 from DAEDALUS's 9/2 packet + its same-day CORRECTION):** the month in this filename is the **ROTATION month** — when the block moved — **not** the month the content describes. A date in a filename asserts a **CLOSED range**. Blocks below therefore all moved in **September 2026** and may describe August content. **Per-block assert at the splice:** if a block's rotation month != this file's month, open the next month's file — the check runs **per block**, never once per session (a session-level check passes on block one and the rest ride through — DAEDALUS's correction, from CARL's 8-pass file).

**What this is:** superseded content rotated verbatim out of `STATUS.md`. `STATUS.md` carries **LIVE current state only**; everything here was **replaced by a later read**, not deleted. Nothing is edited on the way in.

⚠️ **Do not cite anything in this file as current.** If a figure here disagrees with `STATUS.md`, `STATUS.md` wins.

**Why this rotation happened:** root `CLAUDE.md` §Data Hygiene read-cap rule — any surface a boot protocol tells a session to READ WHOLE stays under **32,550 B**, binding above any owner-set number. WATT's `STATUS.md` measured **41,493 B = 127% of budget**; its own header claimed a self-set **64,000 B** budget, which the fleet rule overrides. See STATUS's header note.

---

## CRC MANIFEST

| block | source lines | bytes | crc32 | why rotated |
|---|---|---:|---|---|
| `LEAD_2026-08-17` | 8–8 | 1,361 | 2904104778 | session lead blockquote — superseded by the 2026-09-02 lead. |
| `P1_RED_BAND_INVESTIGATION_2026-08-17` | 27–38 | 2,779 | 300199442 | the 8/16 re-specification narrative + the four-explanations elimination trail. |
| `LIVE_READ_P1_2026-08-17` | 44–44 | 2,923 | 1516731811 | P1 live read — superseded by the 9/1-9/2 emergency episode read. |
| `TWO_STATE_PILOT_2026-08-17` | 90–94 | 1,316 | 183063610 | pilot section — the pilot window closed 8/22; result delivered to DAEDALUS 8/17. |
| `BOTTOM_LINE_2026-08-17` | 96–106 | 4,542 | 2764499296 | session BOTTOM LINE — superseded by the 2026-09-02 version. |
| **TOTAL** | | **12,921** | | source `STATUS.md` @ 41,493 B crc32 1183333349 |

**Rotation month assert:** every block above rotated **2026-09** == this file's month **2026-09** ✅ (checked per block).

---

## LEAD_2026-08-17

*Rotated 2026-09-02 · source `STATUS.md` lines 8–8 · 1,361 B · crc32 2904104778 · verbatim.*
**Why:** session lead blockquote — superseded by the 2026-09-02 lead

> **Sixth session, 2026-08-17.** Two things fired and **neither one was the summer heat this seat was built to catch.** **(1) P2's switch stopped being a forecast: PJM has FILED Door B.** Its ~8/13 **Interim Resource Adequacy Service (IRAS)** petition asks FERC to accept, within 60 days, a framework in which new Large Loads *"build, bring, or buy the new generation resources… **paying the full cost of those resources**"* — the exact assignment **WATT-08** was registered to forecast, put in front of FERC ~10 months before its resolve date. **Not banked** (a filing by the proposing party is not an order by the deciding one); confidence ~65% → **~70% Door B, date unchanged**, and FERC's order is registered as **WATT-10**. **(2) P1 produced its first RED-band price print of the season — and it is anti-correlated with demand.** On Sunday **8/16** the 5-min RT LMP hit **$1,217.52**, five intervals ≥$1,000 across two short episodes, **on the month's LOWEST-demand day (122,075 MW)** while the month's *highest* day (145,375 MW, 8/6) printed a max of only $422.35. **That exposed a real mis-specification in my own RED band**, recorded below as fired-on-letter / mechanism-refuted rather than reinterpreted away. **WATT-06 resolved MISS** on three independent legs. **Composite holds 13/20; P1 held at 2 deliberately; no deploy-posture change.**

---

## P1_RED_BAND_INVESTIGATION_2026-08-17

*Rotated 2026-09-02 · source `STATUS.md` lines 27–38 · 2,779 B · crc32 300199442 · verbatim.*
**Why:** the 8/16 re-specification narrative + the four-explanations elimination trail. THE BAND TEXT ITSELF STAYS LIVE in STATUS's exit triad; only the investigation narrative rotates. Superseded 2026-09-02: the 8/16 verified hourly printed $502.38 (ORANGE, 0 hrs >=$1,000) exactly as pre-registered, AND a mechanism-CONFIRMED RED fired 9/2.

## ⚠️ P1 RED BAND — RE-SPECIFIED 2026-08-17 (my own rule fired on its letter; I am recording that, not reinterpreting it)

**The old rule:** *"RT LMP >$1,000 sustained 2+ intervals."* It named **no interval length** and carried **no scarcity qualifier**.

**What happened 8/16:** two consecutive 5-min intervals (19:50 $1,084.94, 19:55 $1,081.81) printed ≥$1,000. **On the 5-min reading the letter FIRED. On the verified-hourly reading it cannot fire at all** — a 10–20 minute spike inside a **$78.41-mean day** cannot produce a ≥$1,000 hourly print. *The instrument you grade on decides the answer, and the rule never said which.*

**How it is recorded:** **FIRED-ON-LETTER / MECHANISM-REFUTED.** I am **not** retro-reading the rule to manufacture a NOT-FIRED — relaxing a guard to fit an unwanted reading is the failure the root-rule-#6 break test exists to stop. The old rule's firing **stays in the record**.

**The replacement (conjunction, per the standing LIQUID discipline my own THRESHOLDS section already mandates):**
> **RED fires when LMP ≥$1,000 sustained 2+ CONSECUTIVE 5-min intervals *AND* (an emergency-class posting is live *OR* demand ≥97% of the trailing 24h peak).** Price alone = a **logged transient**, not a band.

⚠️ **And the inverse guard, because it cuts both ways:** *a standing guard against a known false positive is what waves away the real event.* The genuinely new information in 8/16 is that **PJM printed $1,200 at ~67% of installed capacity with no posting** — scarcity-*type* pricing decoupled from demand **level**. That was logged as a live hypothesis (**FL-WATT-10**, minimum-commitment fragility) — and **tested and REFUTED the same day** (its crux prediction of thin online reserve failed: 2,514 MW vs 2,571 MW on the peak day). **Local congestion is decisively ruled out** (max $3.84 vs a $1,217.52 total ⇒ 99.6–99.8% system energy), and the successor **FL-WATT-13** (ramp/flexibility scarcity) was registered with its own test and **REFUTED hours later**: across 8/3–8/13 the **20 steepest net-load up-ramps** (to **+6,595 MW/hr**) max out at **$155.18** with none clearing $300, while the window's highest price came on a ramp ranked **239/263**. **FOUR explanations are now eliminated** — congestion · thin reserve · ramp · forced outage (z=+0.23) — and a fifth (elevated maintenance) is contradicted by 8/15 carrying more of it with no spike. **The cause is UNEXPLAINED, and that is the recorded state, not a placeholder for a sixth guess.** ⚠️ **Do not let *unexplained* drift into *suspicious*:** a 20-minute transient on the month's quietest day, with the RED band re-specified so price alone can no longer fire it, needs no further action. **The value of the work was ELIMINATION.**

---

## LIVE_READ_P1_2026-08-17

*Rotated 2026-09-02 · source `STATUS.md` lines 44–44 · 2,923 B · crc32 1516731811 · verbatim.*
**Why:** P1 live read — superseded by the 9/1-9/2 emergency episode read

- **P1 — Stress → price** 🟡 **COLD ON POSTINGS, ONE UNEXPLAINED PRICE TRANSIENT** [boot 2026-08-17 12:31Z + deliberate DM2 range pulls]. **WATT-06 RESOLVED MISS** — zero PJM-RTO emergency-class postings effective 7/17–8/15, resolved on **three independent legs** because the PJM board retains only recent postings and cannot alone certify a 30-day window: **(1) board/ID-continuity** — my dated 8/4 boot recorded 0 emergency-class with #105429 (8/3) latest; today's board carries **#105434 (8/6) as the only posting and the latest ID**, so nothing of any class was issued 8/6→8/17, confining residual uncertainty to IDs **105430–105433**; **(2) physical** — EIA-930 across the whole window, highest **August** day **145,375 MW (8/6)**, ~14 GW below the **159,046 MW** at which the 7/15-16 EEA-1 fired and ~37 GW below ~182 GW capacity; **(3) publisher** — PJM issued a **Hot Weather Alert for Aug 9-11** (forecast 136,029/146,541/144,018 MW) and states it is *"a routine procedure"* that *"does not require any action from customers"* — **preparatory, explicitly not emergency-class** — and published no Max Gen / Load Management / EEA post in August. **August was not flat-mild:** demand ramped from a 113,985 MW trough (7/25) to 145,375 MW (8/6). ⚠️ **THE 8/16 EVENT** — max **$1,217.52 @16:35 EPT**, **5 intervals ≥$1,000** across two ~20-min episodes, day mean **$78.41**; **8/16 is the ONLY August day with any print ≥$500** (10 of 4,149 intervals, 0.24%) and it was the month's **LOWEST**-demand day (122,075 MW) while the **highest** (145,375 MW, 8/6) maxed at $422.35. **Zero postings of any class.** ⚠️ **Tested 8/17 — FOUR explanations eliminated, none surviving: UNEXPLAINED.** *(congestion · thin reserve · net-load ramp · forced outage; detail → KB-WATT-068/069/086/087/088/089.)* ⚠️ **THE VERIFIED HOURLY FOR 8/16 IS NOT AVAILABLE UNTIL ~8/20 — and my stated clock for it was wrong, corrected same session (L-33).** Re-pulled at 09:16 EPT 8/17: still 0 rows. **The reason is not the Sunday-posting rule I published this morning — the feed's frontier is 2026-08-13, a ~4-day lag.** 8/14 and 8/15 also return 0, while a control pull of **7/23–8/2 returns its full 264 rows**, so the query is sound and the feed simply has not reached mid-August. **PUBLIC-AND-UNFETCHED, not unavailable.** ▶ **Pre-registered in its place:** predicted max hourly **$502.28 @ 19:00 EPT** (upper bound ~$525), **zero hours ≥$1,000** — from the 12-print-per-hour mean, an estimator validated across **261 overlapping hours (mean error −$0.13/MWh, max |err| $22.25)**. ⚠️ **$502.28 is in the ORANGE band** — the verified read is likely *Orange, not Red*, missing the RED bar by ~2×, which **strengthens** the transient verdict without depending on it. Retail backdrop [EIA, 2026-05]: industrial **8.71¢/kWh**, residential **18.44¢/kWh**. (KB-WATT-068/069/081.)

---

## TWO_STATE_PILOT_2026-08-17

*Rotated 2026-09-02 · source `STATUS.md` lines 90–94 · 1,316 B · crc32 183063610 · verbatim.*
**Why:** pilot section — the pilot window closed 8/22; result delivered to DAEDALUS 8/17. Superseded by the fleet READ_CAP rule, which replaced the 61,440 B pair cap with a per-surface 32,550 B budget.

## TWO-STATE STATUS PILOT — live state (WATT = control case) · full report DELIVERED to DAEDALUS

**Pair: 61,440-byte cap · currently ~4 bytes under after THREE rotations in one session** (67,485 → 52,799 → **64,880 OVER** → 58,361 → **61,589 OVER** → 61,436). Every rotation was genuinely superseded content — two 8/4 session-lead blockquotes, superseded live reads, the 8/16 raw tape detail (now permanent in KB), the 6 OPEN items that closed, a dead hypothesis trail, and the morning BOTTOM LINE. **Nothing deleted, nothing edited on the way in, nothing manufactured.** Archive → `status_archive/STATUS_ARCHIVE_2026-08.md`.

**Reported to DAEDALUS in full** (3 packets, 8/17): the rotation result; **the finding that its scan was wrong about me in the direction of "clean"** — density and accretion are independent, and a scan keyed on section *headings* cannot see accretion living inside prose blockquotes (second mis-read of this agent in two weeks by the same detector class); and the addendum that **the cap bound twice in one session**, so for this seat it is a live constraint rather than slack, and a 4-byte margin is not a stable state. **Falsifier not hit.** ⚠️ **Amendment-10 exception declared** at this close, with reasons, rather than satisfied by manufacturing a brief edit.

---

## BOTTOM_LINE_2026-08-17

*Rotated 2026-09-02 · source `STATUS.md` lines 96–106 · 4,542 B · crc32 2764499296 · verbatim.*
**Why:** session BOTTOM LINE — superseded by the 2026-09-02 version

## BOTTOM LINE

**Two things fired this session and neither was the weather.** **P2's switch stopped being a forecast: PJM has *filed* Door B** — its ~8/13 IRAS petition asks FERC to accept, inside 60 days, a framework in which new Large Loads *"build, bring, or buy… paying the full cost of those resources."* That is the precise assignment **WATT-08** was registered to forecast, arriving ~10 months early **from the proposing party**. Confidence **~65% → ~70%, date unchanged, NOT banked** — a filing is not an order, and much of retail allocation sits at state commissions FERC does not reach. FERC's order is registered as **WATT-10** (~10/12). The under-noticed limb is the **curtailment** one: it writes priority **into tariff**, converting the DOE §202(c) precedent from an emergency action into a **standing commercial term of service**. The **abeyance is still unruled** with a **third** motion filed (Silver Run, 8/3), FERC having declined a shortened answer period **twice** — while *every* ISO/RTO asked for the same 90 days, which is evidence about how hard these rules are to write, not about PJM.

**The second firing was my own rule, and the day's real work was killing explanations for it.** Sunday **8/16** printed **$1,217.52/MWh** on the month's **lowest**-demand day with **no posting of any class** — 10 of 4,149 August intervals cleared $500 and **all ten were that Sunday**. My RED band named no interval and no instrument, so the letter fired on the 5-min tape and could not fire on the hourly; recorded **FIRED-ON-LETTER / MECHANISM-REFUTED** and re-specified prospectively as a conjunction. Then I tested the explanations and **eliminated four**: local congestion (congestion max **$3.84** against a $1,217.52 total ⇒ 99.6–99.8% system energy), thin online reserve (**2,514 vs 2,571 MW** on the peak day — FL-WATT-10 refuted on its own crux), net-load ramp (the **20 steepest** ramps across 8/3–8/13 max out at **$155.18**, none clearing $300, while the window's highest price came on a ramp ranked **239/263** — FL-WATT-13 refuted), and a large forced outage (**z = +0.23**). A fifth, elevated maintenance, is contradicted by 8/15 carrying more of it with no spike. **No surviving explanation. Recorded as UNEXPLAINED — not as a placeholder for a sixth guess.** ⚠️ *Unexplained is not suspicious*: a 20-minute transient on the quietest day of the month, with the band re-specified so price alone cannot fire it, needs no further action.

**The instrument work was the other half, and most of it was correcting myself.** The DM2 **verified-hourly clock** I published in the morning was assumed and wrong; my *correction* was measured **once** and also wrong — the frontier moved **8/13 → 8/15 while I was working**, so the feed is **batch-published with a variable ~1–4 day lag** and the standing form is *measure the frontier at use time*. The **queue figure** I had embargoed resolved at PJM primaries to **811 projects / 220 GW** (Cycle 1) **+30 GW** transition remainder ⇒ **active ≈250 GW = 1.56×** the 2027 peak, not the **1.32×** I published — a correction that runs *toward* my trigger, which is why it went to VULCAN rather than quietly into my file. **P3's rule never named its population either**, so it was re-specified — the same defect as the RED band, second surface, same day. And PJM's **`solar_gen`/`wind_gen` return a full 24-row day of `0.0`** for unpublished dates where the LMP feed returns 0 rows: I was one step from silently deleting ~10–12 GW of solar from a net-load calculation that would have passed every structural check.

**Delivered:** the **P4 instrument fixed** (same-vintage spark primary at **+$48.12**; the stale-proxy spark **refused, not caveated**), both **DAEDALUS SFG actions** (rc-or-marker boot guard, tested 5/5; EIA cache-provenance wall stated), **`THESIS.md` rewritten** (9 contradictions and a **dead flip** that pointed at an auction resolved 7/14), the **`KILL_MEMO`** my own thresholds had always mandated, `FLOW.tsv`'s missing vintage column, and the `CLAUDE.md` 3-legs rot open since 7/22. Packets to **VULCAN ×2, HENRY, CARL, DAEDALUS ×3, PROME ×2**.

**Composite holds 13/20 · status holds 🟠 · P1 held at 2 · no deploy-posture change.** ⚠️ **Two process defects of my own are in the record** (an empty `noop` commit, and a declared Amendment-10 exception), and **the pilot pair sits 4 bytes under a cap it breached twice today** — the trajectory, not the endpoint, is what DAEDALUS should grade.



---

## ASHBURN_RIDE_THROUGH_2026-08-11

*Rotated 2026-09-02 (second pass, same session) · source `STATUS.md` line 46 · 1,312 B · crc32 252073485 · verbatim.*
**Why:** stable sourced background, permanent in `workbook/KB.tsv`; STATUS keeps a pointer + the live-this-week joins. **Rotation month 2026-09 == file month 2026-09 ✅**

- **P2/P1 — correlated-control risk: the Ashburn event, with a regulatory clock.** [PJM Inside Lines **8/11**] **~3,800 MW** of data-center load disconnected **7/22** — largest such event in PJM history. A **mechanical failure** triggered automatic removal of a **230 kV** line in Northern Virginia; data centers disconnected in **two cascading waves — 2,970 MW, then 1,099 MW.** **PJM restored balance in nine minutes against NERC's 30-minute standard**; PJM's verdict: they *"should not disconnect from the grid"* during routine faults properly cleared. 🔑 **FORWARD COST LINE, DATED:** PJM is evaluating **ride-through standards** through the Planning Committee, to set requirements *"before the load comes on the system"*; **FERC has ordered NERC to submit enforcement provisions by 2026-12-31**, minimum voltage/frequency ride-through standards **expected 2027**. A compliance cost landing on **operators**, not utilities → degrades AI-capex ROI directly. **VULCAN carries no such cost line.** ⚠️ **NOT SIZED.** **Mechanism is inverted vs the viral framing:** the disturbance came from the sudden **ABSENCE** of load ⇒ risk scales with **concentration + identical automation**, not demand growth. **Direct join: the 10-GW OpenAI/SoftBank Ohio campus sits in PJM.** (KB-WATT-071, FL-WATT-11.)

---

## CRWV_DDTL_POWER_COVENANT_2026-08-03

*Rotated 2026-09-02 (second pass, same session) · source `STATUS.md` line 47 · 1,367 B · crc32 2788768241 · verbatim.*
**Why:** stable sourced background, permanent in `workbook/KB.tsv`; STATUS keeps a pointer + the live-this-week joins. **Rotation month 2026-09 == file month 2026-09 ✅**

- **P3 — filed mechanism: power price is a CONTRACTUAL input to neocloud borrowing capacity** [VULCAN 8/3, from DEWEY's read of Exhibit 10.1 to CoreWeave's 8-K of 2026-03-31, acc `0001769628-26-000129`]: CRWV's **$8.5B DDTL 4.0** re-marks its Base Case Model for **exactly two things: hedge/SOFR rates, and POWER.** **§5.25 "Power Cost Protection"**; **"Excess Unhedged Power Costs"** a defined term; unhedged power marked to *"the average actual Power Costs for the most recently completed three calendar months"*; debt-sizing resolves to **Projected DSCR ≥ 1.20:1.00** tested every Monthly Date, plus maintenance **DSCR ≥ 1.15:1.00**; a **"Negative NOI Event"** forces repayment **two calendar months BEFORE the first projected negative month**. ⇒ **power price → Modeled Power Costs → Projected DSCR → borrowing capacity AND mandatory prepayment**, ~3-month lag on the unhedged portion, biting on a **projection**. ⚠️ **Correction carried:** DEWEY initially tied the borrowing base to **GPU depreciable cost** and **retracted it** — the advance rate is **90% of COST struck at funding date**. **Open on WATT (owed to VULCAN):** what share of neocloud load is hedged via `Permitted Commodity Agreements` vs floating. 🔑 **This week's join: a §202(c)-driven scarcity episode is exactly the event that moves the unhedged three-month average.**

---

## CRWV_10Q_393MW_2026-08-12

*Rotated 2026-09-02 (second pass, same session) · source `STATUS.md` line 48 · 616 B · crc32 173181001 · verbatim.*
**Why:** stable sourced background, permanent in `workbook/KB.tsv`; STATUS keeps a pointer + the live-this-week joins. **Rotation month 2026-09 == file month 2026-09 ✅**

- **🆕 P3 — a FILED, dated, site-specific undelivered-MW quantity** [CoreWeave 10-Q, period 2026-06-30, acc `0001769628-26-000366`, filed **8/12**]: **$35.5B of leases executed but not yet commenced**, and **excluded from that $35.5B — explicitly because the payments are uncertain — a single-site lease with 393 MW of electrical power still UNDELIVERED**, phased 2026 and 2028. 🔑 **The class my 32-vs-55 reconciliation was short of:** a filer telling the SEC under liability that a named site is short a specific MW quantity on a dated schedule. ⚠️ **n=1.** Double-count guard applies. (KB-WATT-075.)

---

## ERCOT_474GW_AUDIT_2026-08-13

*Rotated 2026-09-02 (second pass, same session) · source `STATUS.md` line 49 · 673 B · crc32 1292669421 · verbatim.*
**Why:** stable sourced background, permanent in `workbook/KB.tsv`; STATUS keeps a pointer + the live-this-week joins. **Rotation month 2026-09 == file month 2026-09 ✅**

- **🆕 P3 — Texas ordered the measurement I can only suspect in PJM.** Abbott directed **PUCT + ERCOT to audit every data center in the interconnection process** — **474 GW** of large-load requests, **>1,800 projects**, ~90% data-center, **>5× the state's record peak**; **Batch Zero transmission study POSTPONED**. ⚠️ **An audit, not a moratorium.** The August STEO **cut ERCOT 2027 load growth 14% → 6%**. 🔑 **474 GW against a <95 GW record peak cannot all be real demand.** ⚠️ **ANALOGUE, NOT TRANSFER** — do **not** apply an ERCOT attrition rate to PJM. **No PJM score moves** — out of footprint, and the fleet has no ERCOT owner. (KB-WATT-074.)


---

## WATT-02_GRADE_LONGFORM_2026-09-02

*Rotated 2026-09-02 (third pass, same session) · 2,366 B · crc32 2846099708 · verbatim.*
**Why:** the long form of a record whose permanent home is elsewhere — the WATT-02 grade lives in `workbook/PREDICTIONS.tsv`, the read-cap receipts in the commit message. STATUS keeps the verdict, the lesson and the receipt table. **Rotation month 2026-09 == file month 2026-09 ✅**

## ✅ WATT-02 — RESOLVED **HIT**, and the grading exposed a defect in my own notes

**Registered 7/10, verbatim:** *"At least one more PJM **EEA2+ (or DOE §202(c))** grid-emergency event before Labor Day 2026."* **Criteria, verbatim:** *">=1 EEA2+ posting **or 202(c) order** in PJM footprint by 9/7."*

**Resolved HIT on the §202(c) limb.** **DOE Order No. 202-26-41**, issued **2026-09-01** to PJM Interconnection, effective through **11:59 PM ET 9/8** — a 202(c) order in the PJM footprint, before 9/7. **The EEA-postings limb did NOT fire: EEA-1 is not EEA2+.** Both facts recorded; the disjunction only needed one.

⚠️ **AND IT WAS ALREADY A HIT ON 2026-07-14, SEVEN WEEKS BEFORE I GRADED IT.** **Order No. 202-26-35** (issued **7/14**, PJM, effective 7/14–7/21, *"dispatch units for reliability; backup generation at loads before/during EEA 3"*) also satisfies the criteria. On 7/22 I wrote *"the 7/15-16 EEA-1 is sub-EEA2 (near-miss, **not banked**)"* — **a correct statement about the posting limb, applied as if it settled the whole prediction.** The DOE order covering that same episode was one index page away.

🔑 **Root cause, and it is a documentation defect, not a research one.** The registered row in `PREDICTIONS.tsv` carries both limbs. **Every carry-forward summary of it dropped the second one** — STATUS said *"WATT-02 (9/7) — EEA2+ by Labor Day"*, SCRATCH said *"its bar is a **POSTING**"*, and the PROME task brief for this session inherited that compression and restated it back to me as fact. **Four surfaces, one dropped limb, and the ledger was right the whole time.** `[[finding_summary_section_merges_what_the_body_separates]]` — **grade at the registered row, never at the surface that quotes it.** (⚠️ Note the *neighbouring* prediction is genuinely posting-only: **WATT-06's** criteria really does say *"on emergencyprocedures.pjm.com"* — so the compressed sentence was true of WATT-06 and got attached to WATT-02. **A correct caveat migrated to the wrong prediction.**) Logged **L-39**.

**Registered `if_falsified` does NOT execute** (it was written for a MISS). The HIT's content: **the recurrence case is n=3 episodes in one season, and it now spans July AND September** — the "heat-clustered, not a cadence" read that WATT-06's MISS established for *July* does not extend across the season.

---



---

## READ_CAP_REASONING_LONGFORM_2026-09-02

*Rotated 2026-09-02 (third pass, same session) · 2,786 B · crc32 2338958150 · verbatim.*
**Why:** the long form of a record whose permanent home is elsewhere — the WATT-02 grade lives in `workbook/PREDICTIONS.tsv`, the read-cap receipts in the commit message. STATUS keeps the verdict, the lesson and the receipt table. **Rotation month 2026-09 == file month 2026-09 ✅**

## ⚠️ READ-CAP — the 64,000 B budget is retired, and I am saying why rather than dropping it quietly

My header carried **"budget 64,000 B — set from measurement (392 B/line), fleet convention Will-ratified 2026-08-17."** **It is retired.** Root `CLAUDE.md` §Data Hygiene: *any surface a boot protocol tells a session to READ WHOLE stays under **32,550 B** — **binding above any owner-set number**, per surface; owners choose rotation or hot/cold split, **never the number**.*

**Does the 8/17 Will ratification survive it? No, and the reason is scope, not seniority.** What Will ratified on 8/17 was the **byte-tier CONVENTION** — that a STATUS cap should be set in bytes as well as lines, and that a measured B/line beats a default assumption. **That reasoning is still correct and I keep it.** What it did not do, and could not have, is exempt this file from a *physical* limit discovered later: past **54,250 B** a harness `Read` returns a **partial file with no error**, so a 64,000 B budget authorises a boot that silently reads a fragment while every line-count guard passes. **A budget above the cap is not a looser policy; it is an unenforceable one.** `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]` — the 8/17 ratification governed the writes of 8/17. **No Will ruling is being overridden; a narrower one is being superseded by a later, wider one, and I am not treating "Will-ratified" as a shield.**

**Executed this session (READ_CAP rules 16–17, `python3 PROME/tools/measure.py` receipts in the commit):**
| surface | before | after | remedy |
|---|---:|---:|---|
| `SCRATCH.md` | **62,072 B** (191% of budget, **114% of the physical cap**) | see commit receipt | **hot/cold split** — lines 54–367 verbatim → `archive/SCRATCH_ARCHIVE_2026-07-08.md` (56,324 B, body crc32 **1809430476**, round-trip verified) |
| `STATUS.md` | **41,493 B** (127%) | see commit receipt | **rotation** — 5 blocks / **12,921 B** verbatim → `status_archive/STATUS_ARCHIVE_2026-09.md`, per-block crc |
| `workbook/PREDICTIONS.tsv` | 16,397 B (50%) | unchanged | ✅ ok |

**Audited BY OBLIGATION, both directions.** Every owed action and standing watch was enumerated **before** the cut and re-homed **before** the bytes moved — the table is in `archive/SCRATCH_ARCHIVE_2026-07-08.md` § "WHAT WAS OWED AT ROTATION TIME" (12 items: 1 discharged this session, 8 still open and carried below, 2 already closed, 1 re-homed as a standing operational constraint). **Nothing was retired by being rotated.** ⚠️ **The one that nearly went:** the standing **PJM rate limit** (non-member = 6 calls/min, never loop) lived only in rotated session notes — it is an operational constraint, not history, and is now in the live `SCRATCH.md` header.

---




---

## BOTTOM_LINE_LONGFORM_2026-09-02

*Rotated 2026-09-02 (fourth pass, same session) · 2,746 B · crc32 3854707426 · verbatim.*
**Why:** four paragraphs against a CLAUDE.md spec of '2-4 plain-language sentences' — compacted in place, long form preserved here. **Rotation month 2026-09 == file month 2026-09 ✅**

## BOTTOM LINE

**The channel this desk was built for finally fired, and it fired clean.** PJM ran a capacity emergency on **two consecutive days**, dispatched **load management** in five zones, served a **season-high 152,518 MW**, and operated under a **DOE §202(c) order** — while the tape printed **$1,868.78/MWh on eight consecutive five-minute intervals** with **congestion of $1.25**, i.e. 99.85% system-wide energy scarcity. My RED band, re-specified in writing two weeks earlier and deliberately hardened so price alone could not trip it, **met every limb**. **P1 2 → 5, composite 13 → 16/20, status 🟠 → 🔴.** No deploy-posture change: a fired gate raises conviction and supplies no entry.

**The discipline that makes the upgrade trustworthy is what it did NOT lean on.** The 8/16 mystery spike closed this session on its own pre-registered terms — verified hourly **$502.38 @19:00 against a forecast of $502.28**, a ten-cent error, **ORANGE not RED, zero hours ≥$1,000**. Its registered upgrade trigger did **not** fire and **contributed nothing** to P1's move. 8/16 stays **UNEXPLAINED and closed**; September is a separate event with the opposite signature — high demand, live postings, RTO-wide. **Same price band, opposite mechanism, and they are not allowed to borrow evidence from each other.**

**The session's uncomfortable finding is in my own filing cabinet, not in the market.** **WATT-02 resolves HIT** — but its registered criteria always read *"EEA2+ posting **or 202(c) order**"*, and **every summary surface I wrote had dropped the second limb**, so it was already a HIT on **2026-07-14** (Order 202-26-35) and I graded it *"trending MISS"* for seven weeks. The ledger was correct throughout; four derived surfaces were not, and this session's own task brief inherited the error and handed it back to me as fact. **Grade at the registered row, never at the surface that quotes it.** The neighbouring caveat that caused it — *"the bar is a POSTING"* — is **true of WATT-06 and was migrated to the wrong prediction.**

**Structurally nothing moved and one thing sharpened.** P2 holds at max; P3 holds at 4 on a genuine net of opposing evidence (DEWEY's slot-reservation finding against the operational reliance on large-load backup generation); P4 widened a third time to **+$53.65/MWh** on a power-side move, not a gas one. **The sharpened item is IRAS limb (c):** Order 202-26-41 authorised PJM to direct **backup generation at large loads** this week — **the practice ran ahead of the tariff.** That corroborates Door B's direction and must not be banked as its outcome, because the gap between an *emergency action* and a *standing commercial term of service* **is the entire prediction.**


---

## OPEN5_WINTER_GATE_LONGFORM

*Rotated 2026-09-02 (fourth pass, same session) · 1,068 B · crc32 4289929332 · verbatim.*
**Why:** stable carry-forward; permanent in KB-WATT-076. STATUS keeps the rule + the new September counter-example. **Rotation month 2026-09 == file month 2026-09 ✅**

5. **⚠️ Winter P1 registration is GATED and the gate HELD — but its premise now has a counter-example.** AEOLUS: winter **ENERGY/mean DOWN, ESTABLISHED**; winter **PEAK — NO SIGN** (n=2 very-strong analogues, split). **2023-24 is decisive: US warmest winter on record AND PJM still peaked 134,777 MW on Jan 17 2024**, running Cold Weather Advisory → Alert → Conservative Operations → NERC TLR-1. ⇒ **do NOT register "no EEA because El Niño."** Any winter P1 call must be **peak-based and sign-agnostic, weighted mid-Jan–Feb, not December.** 🔑 **Reinforced this week:** the September episode fired at a **lower** load than July's — **the load level at which PJM goes to emergency is not a constant**, which is exactly why a peak-based call must not be pinned to a fixed MW threshold. Vintage discipline: ONI is revised as ERSSTv5 updates; `sstoi.indices` runs a different baseline from the discussion prose — **never mix +2.03 and +1.2 in one sentence.** The "~1–3 °F Ohio Valley" figure is **secondary and uncorroborated**. (KB-WATT-076.)



---

## TWO_DOORS_LF_LADDER_LONGFORM

*Rotated 2026-09-02 (fifth pass, same session) · 987 B · crc32 2955226729 · verbatim.*
**Why:** the $555/MW-day load-factor ladder is settled, delivered to VULCAN 8/21 and permanent in KB-WATT-077; STATUS keeps the cited figure + the basis caveat. **Rotation month 2026-09 == file month 2026-09 ✅**

- **THE TWO DOORS (WATT owns the docket).** **DOOR A — cost lands on RATEPAYERS** ⇒ consumer power prices rise across PJM (~65M people, 13 states + DC) = a CPI / consumer-squeeze channel → **CARL, HENRY**. **DOOR B — cost lands on the DATA CENTERS** ⇒ hyperscaler opex rises and AI-capex ROI degrades → **VULCAN S1, HENRY HEN-36**. Same dollar, one door or the other. Prior number on the table: the stakeholder-approved reliability backstop caps average cost at **$555/MW-day (≈$202,575/MW-year)** = **$25.69/MWh @90% LF · $27.21 @85% · $33.04 @70% · $38.54 @60%** — cite **85%/$27.21**; basis is arithmetic at assumed load factors, **not observed utilisation**, and must travel with the number. 🔑 **The read is insensitive across the whole band** — even at 60% LF the queue-skip price is **5×–33× below** the $201–1,283/MWh cost of a year of delay (FL-WATT-07). ⚠️ **KEEP THE TWO DOCKETS APART** — capacity backstop ≠ transmission cost allocation.


---

## OPEN7_ERCOT_LONGFORM

*Rotated 2026-09-02 (fifth pass, same session) · 862 B · crc32 291993621 · verbatim.*
**Why:** long form of an open instrument task; the finding, the basis caveat and the prohibition are all retained in STATUS. **Rotation month 2026-09 == file month 2026-09 ✅**

7. **🟡 The ERCOT counter-signal needs its discriminator run** (WALTER SIG-W-20260828-049) — ERCOT North Hub **Cal-27 ~$42/MWh**, all four strips lower than early July. **WALTER named the discriminator and it is mine: is it a gas-cost story or a demand story?** Partial answer already in hand and it leans **demand/supply, not gas** — front Henry Hub *rose* ~12% (2.694 → 3.017) over roughly the same window in which Cal-27 power fell ~18%, so implied heat rate compressed. ⚠️ **[INFERRED, basis mismatch stated]** — that pairs a **chart-read Cal-27 power level** with a **spot** gas move; the clean test needs the ERCOT North Hub Cal-27 strip and the Henry Hub Cal-27 strip **on the same date**, neither of which I can pull free. **Levels are chart-read and must never be quoted as settles or used to set a threshold** (WALTER's caveat, adopted).



---

## P1_8-16_CLOSURE_LONGFORM_2026-09-02

*Rotated 2026-09-02 (sixth pass, same session) · 1,115 B · crc32 818099015 · verbatim.*
**Why:** a CLOSED item whose permanent home is KB-WATT-090 + `workbook/PREDICTIONS.tsv`; STATUS keeps the figures, the not-met trigger and the do-not-retro-fit guard. **Rotation month 2026-09 == file month 2026-09 ✅**

- **P1 — the 8/16 puzzle is CLOSED, and it closed on its own pre-registered terms** [KB-WATT-090]. The verified hourly (`rt_hrl_lmps`, pnode 1, 8/16) finally published: **24/24 rows, max $502.38 @19:00 EPT, ZERO hours ≥$1,000, day mean $78.34.** Against the estimate registered **on 8/17, before the data existed** — max **$502.28 @19:00**, zero hours ≥$1,000, day mean **$78.41** — the errors are **+$0.10 on the max (0.02%), −$0.07 on the day mean**, both inside the ±$22.25 validation band. ⇒ **the estimator is confirmed**, and substantively **8/16 was ORANGE, not RED, missing the RED bar by ~2×.** **The registered upgrade trigger *"the 8/16 verified hourly confirming ≥$1,000 → P1 2→3"* is NOT MET.** 🔑 **This matters for the honesty of the P1 upgrade above: 8/16 contributed ZERO to it.** The five eliminated explanations stand; 8/16 stays **UNEXPLAINED and closed**. ⚠️ **Do not retro-fit 8/16 to the September event** — 8/16 was the month's lowest-demand day with no posting; 9/2 was near season-peak with an EEA-1 and a §202(c) order. Same price band, opposite mechanism.



---

## IRAS_COMPONENTS_LONGFORM

*Rotated 2026-09-02 (seventh/final pass, same session) · 1,071 B · crc32 2048713310 · verbatim.*
**Why:** components (a)–(d) are quoted verbatim in `workbook/PREDICTIONS.tsv` WATT-10 `resolution`, which is the GRADED copy. STATUS keeps the headline, limb (c), and all four caveats. **Rotation month 2026-09 == file month 2026-09 ✅**

- **PJM HAS FILED DOOR B (~2026-08-13).** The **Interim Resource Adequacy Service (IRAS)** petition asks FERC to accept, **within 60 days (⇒ ~2026-10-12)**, a framework in which new Large Loads *"build, bring, or buy the new generation resources and electricity needed to satisfy their new energy demands, **paying the full cost of those resources**."* Components: **(a)** Reliability Backstop Procurement, from **June 2027**; **(b)** a **Large Load Registry**; **(c)** **emergency load-reduction procedures PRIORITIZING large loads over residential consumers**; **(d)** from **2029/30**, new large loads without their own supply **excluded** from procurement calculations. ⚠️ **NOT BANKED** — a filing by the proposing party is not an order by the deciding one; states/ratepayer advocates/large loads will litigate; much retail allocation sits at **state** commissions outside FERC's rate-design jurisdiction. ⚠️ **DOCKET NUMBER STILL NOT VERIFIED — cite no docket for IRAS.** ⚠️ **Relationship to EL26-67 NOT established.** (KB-WATT-070, FL-WATT-12.)



---

## ABEYANCE_LONGFORM_2026-08-17

*Rotated 2026-09-02 · 2,036 B · crc32 1290759886 · verbatim.*
**Why:** a 16-day-stale regulatory read whose permanent record is KB-WATT-072 and whose live action is STATUS OPEN #2. STATUS keeps the state, the two tells and the fused-claim warning. **Rotation month 2026-09 == file month 2026-09 ✅**

- **⚠️ THE ABEYANCE WAS STILL UNRULED at last check (8/17) — THREE motions.** Silver Run Electric filed **8/3** for 90 days on **EL26-67-000**; **FERC declined a shortened answer period for the second time**, answers 5:00 p.m. ET Fri **8/7** [FR **91 FR 51171-72**, FR Doc 2026-16175]. 🔑 **Declining a shortened answer period twice is weak evidence AGAINST a grant.** ⚠️ **A search-engine summary once asserted "Abeyance Granted" over text reciting only the MOTIONS — a fused claim, refuted by the FR primary.** 🔑 **Fleet-wide unanimity:** *every* ISO/RTO asked for the extra 90 days [RTO Insider 8/4; EL26-67/68/70/71/72] — evidence about the **difficulty of writing large-load rules**, consistent with the administrative-rationing read (FL-WATT-07). **⚠️ NOT RE-CHECKED THIS SESSION — 16 days stale. See OPEN #2.** (KB-WATT-072.)
- **📁 STANDING P2/P3 REFERENCE — four sourced mechanism bullets rotated 2026-09-02 to `status_archive/STATUS_ARCHIVE_2026-09.md` (verbatim, per-block crc), because they are STABLE BACKGROUND, not live state, and each is permanent in `workbook/KB.tsv`:** the **Ashburn 3,800 MW correlated-control event** + its ride-through regulatory clock (NERC enforcement provisions due **2026-12-31**, standards expected 2027 — an un-sized AI-capex compliance cost landing on OPERATORS) [KB-WATT-071, FL-WATT-11] · **CoreWeave's $8.5B DDTL §5.25 Power Cost Protection** covenant chain (power price → Modeled Power Costs → Projected DSCR ≥1.20 → borrowing capacity AND mandatory prepayment, ~3-month lag on the unhedged share) [FL-WATT-08] · the **393 MW undelivered single-site lease** excluded from CRWV's $35.5B not-yet-commenced total, n=1 [KB-WATT-075] · **Texas/ERCOT's 474 GW large-load audit** and the STEO's 14%→6% ERCOT load-growth cut — **ANALOGUE, NOT TRANSFER**, no PJM score moves [KB-WATT-074]. ⚠️ **The double-count guard and the ANALOGUE-NOT-TRANSFER caveat travel with these and are NOT rotated — they are restated in the P3 live read above.**




---

## P2_REGULATORY_LAYER_LONGFORM_2026-09-03

*Rotated 2026-09-03 · 2,963 B · crc32 3019213517 · verbatim.*
**Why:** the P2 regulatory case file, duplicated in `workbook/PREDICTIONS.tsv` (WATT-08/09/10 `resolution`, the GRADED copy) and KB-WATT-070/072. STATUS keeps the live state, limb (c), the two doors, the cited figure and every caveat. **Rotation month 2026-09 == file month 2026-09 ✅**

### P2 — the regulatory layer (the switch by which AI capex becomes macro)

- **PJM HAS FILED DOOR B (~2026-08-13).** The **Interim Resource Adequacy Service (IRAS)** petition asks FERC to accept **within 60 days (⇒ ~2026-10-12)** a framework in which new Large Loads *"build, bring, or buy the new generation resources… **paying the full cost of those resources**."* **All four components (a)–(d) are quoted verbatim in `workbook/PREDICTIONS.tsv` → WATT-10 `resolution`** — that is the graded copy; this is a pointer, not a second one. 🔑 **The live limb is (c)** — *"emergency load-reduction procedures **prioritizing large loads over residential consumers**"* — which writes curtailment priority **into tariff**, converting the DOE §202(c)/Manual 13 precedent from an **emergency action** into a **standing commercial term of service**. ⚠️ **NOT BANKED** — a filing by the proposing party is not an order by the deciding one; states/ratepayer advocates/large loads will litigate; much retail allocation sits at **state** commissions outside FERC's rate-design jurisdiction. ⚠️ **DOCKET NUMBER STILL NOT VERIFIED — cite no docket for IRAS.** ⚠️ **Relationship to EL26-67 NOT established.** (KB-WATT-070, FL-WATT-12.)
- **THE TWO DOORS (WATT owns the docket).** **DOOR A — cost lands on RATEPAYERS** ⇒ consumer power prices rise across PJM (~65M people, 13 states + DC) = a CPI / consumer-squeeze channel → **CARL, HENRY**. **DOOR B — cost lands on the DATA CENTERS** ⇒ hyperscaler opex rises and AI-capex ROI degrades → **VULCAN S1, HENRY HEN-36**. Same dollar, one door or the other. The backstop caps average cost at **$555/MW-day ≈ $202,575/MW-year** ⇒ **cite $27.21/MWh @85% LF** (full LF ladder + basis: KB-WATT-077, adopted verbatim by VULCAN 8/21). **Basis travels with the number: arithmetic at ASSUMED load factors, not observed utilisation.** 🔑 **The read is insensitive across the whole band** — even at 60% LF the queue-skip price is **5×–33× below** the $201–1,283/MWh cost of a year of delay (FL-WATT-07), which is what makes it safe to publish. ⚠️ **KEEP THE TWO DOCKETS APART** — capacity backstop ≠ transmission cost allocation.
- **⚠️ THE ABEYANCE — 16 DAYS STALE, NOT RE-CHECKED THIS SESSION.** Last verified state (8/17): three Rule 212 motions on **EL26-67-000** for a 90-day abeyance (PJM + Indicated TOs 7/28, **Silver Run 8/3**); **FERC declined a shortened answer period twice**, answers 5:00 p.m. ET **8/7**; **unruled**. 🔑 **Declining a shortened answer period twice is weak evidence AGAINST a grant**; *every* ISO/RTO asked for the same 90 days, which is evidence about the difficulty of writing large-load rules, not about PJM. ⚠️ **A search summary once ran the heading "Abeyance Granted" over text reciting only the MOTIONS — a fused claim, refuted by the FR primary [91 FR 51171-72].** **Full record KB-WATT-072; the live action is OPEN #2.**




---

## P2_REGULATORY_LAYER_FULL_2026-09-03

*Rotated 2026-09-03 · 2,595 B · crc32 2211048658 · verbatim. Supersedes the partial rotation above — this is the whole subsection.*
**Why:** L-43 applied — relocate the block, do not rewrite it. Live actions live in STATUS OPEN #2; the graded copy is `workbook/PREDICTIONS.tsv`. **Rotation month 2026-09 == file month 2026-09 ✅**

### P2 — the regulatory layer (**full text → `status_archive/STATUS_ARCHIVE_2026-09.md`; graded copy → `workbook/PREDICTIONS.tsv` WATT-08/09/10; live actions → OPEN #2**)

**In one block, because the detail is duplicated in two permanent homes and STATUS is a live-state surface, not a case file:** PJM **filed Door B ~8/13** — the **IRAS** petition asks FERC to accept within 60 days (⇒ **~2026-10-12**) a framework where new Large Loads *"build, bring, or buy… **paying the full cost of those resources**."* 🔑 **The live limb is (c)** — *"emergency load-reduction procedures **prioritizing large loads over residential consumers**"* — which writes curtailment priority **into tariff**, converting the DOE §202(c)/Manual 13 precedent from an **emergency action** into a **standing commercial term of service**. ⚠️ **NOT BANKED** (a filing by the proposing party is not an order by the deciding one; states/ratepayer advocates/large loads will litigate; much retail allocation sits at **state** commissions outside FERC's rate-design reach). ⚠️ **DOCKET NUMBER STILL UNVERIFIED — cite no docket for IRAS.** ⚠️ **Relationship to EL26-67 NOT established.** **The abeyance was UNRULED at last check (8/17, now 16 days stale)** — three Rule 212 motions on **EL26-67-000**, FERC having **declined a shortened answer period twice** (weak evidence *against* a grant); *every* ISO/RTO asked for the same 90 days, which is evidence about how hard large-load rules are to write, not about PJM. ⚠️ **A search summary once ran the heading *"Abeyance Granted"* over text reciting only the MOTIONS — a fused claim, refuted by the FR primary [91 FR 51171-72].**

**THE TWO DOORS (WATT owns the docket).** **DOOR A — cost lands on RATEPAYERS** ⇒ consumer power prices rise across PJM (~65M people, 13 states + DC) = a CPI / consumer-squeeze channel → **CARL, HENRY**. **DOOR B — cost lands on the DATA CENTERS** ⇒ hyperscaler opex rises and AI-capex ROI degrades → **VULCAN S1, HENRY HEN-36**. Same dollar, one door or the other. The backstop caps average cost at **$555/MW-day ≈ $202,575/MW-year** ⇒ **cite $27.21/MWh @85% LF** (ladder + basis: KB-WATT-077, adopted verbatim by VULCAN 8/21). **Basis travels with the number: arithmetic at ASSUMED load factors, not observed utilisation.** 🔑 **Insensitive across the whole band** — even at 60% LF the queue-skip price is **5×–33× below** the $201–1,283/MWh cost of a year of delay (FL-WATT-07). ⚠️ **KEEP THE TWO DOCKETS APART** — capacity backstop ≠ transmission cost allocation.



---

# ROTATION PASS — 2026-09-06 (eighth session)

**Why:** `STATUS.md` measured **30,858 B = 94% of the 32,550 B read cap** at the 2026-09-06 boot; `boot.py` leg 3 called the rotation. Blocks below were **superseded by a later read** — chiefly the close of the 9/1–9/3 PJM emergency episode — not deleted.

**CRC manifest (this pass)** — source `STATUS.md` @ 30,858 B crc32 3066285840

| block | source lines | bytes | crc32 | why rotated |
|---|---|---:|---|---|
| `LEAD_2026-09-03` | 8–8 | 1,048 | 815005748 | session lead blockquote — superseded by the 2026-09-06 lead (episode closed). |
| `P1_EPISODE_LIVE_READ_2026-09-02` | 29–34 | 3,783 | 391420467 | the live-episode P1 read (postings/order/price/mechanism/9-3 re-read) — the episode CLOSED 9/3; superseded by the 2026-09-06 episode-closed read. |
| `P1_8-16_PUZZLE_CLOSED_2026-09-02` | 36–36 | 1,021 | 2165859202 | the 8/16 puzzle close-out narrative — resolved; permanent record is KB-WATT-090 + PREDICTIONS.tsv. |
| `WATT-02_GRADE_AND_READCAP_2026-09-03` | 66–72 | 3,197 | 1560113384 | WATT-02 grade + read-cap retirement session notes — WATT-02 is RESOLVED (graded row in PREDICTIONS.tsv) and the read-cap remedy is EXECUTED; long-form reasoning already archived 9/2. |
| `OPEN5_WINTER_GATE_2026-09-02` | 78–78 | 883 | 494082341 | winter P1 gate long-form — gate HELD, does not fire until mid-Jan-2027; basis is KB-WATT-076. Pointer retained on STATUS. |
| `OPEN7_ERCOT_DISCRIMINATOR_2026-09-02` | 80–80 | 814 | 1192047109 | ERCOT Cal-27 discriminator long-form — still INFERRED, unchanged since 9/3. Pointer retained on STATUS. |
| `BOTTOM_LINE_2026-09-03` | 101–101 | 1,181 | 2557202554 | session BOTTOM LINE — superseded by the 2026-09-06 version. |
| **TOTAL** | | **11,927** | | |

**Rotation month assert:** every block above rotated **2026-09** == this file's month **2026-09** ✅ (checked per block, at each splice).

---

## LEAD_2026-09-03

*Rotated 2026-09-06 (eighth session) · source `STATUS.md` lines 8–8 · 1,048 B · crc32 815005748 · verbatim. Rotation month 2026-09 == file month 2026-09 ✅ (asserted at this splice).*

> **Seventh session, 2026-09-02 → 09-03.** **P1 went from 2 to 5 in one episode, and for the first time this year it did so with the mechanism CONFIRMED rather than refuted.** PJM ran a **capacity emergency on two consecutive days** (NERC **EEA-1** alerts 9/1 18:03 and 9/2 16:00), **dispatched a Pre-Emergency Load Management Reduction Action** in five zones on 9/1, served a **season-high 152,518 MW**, and **DOE issued §202(c) Order 202-26-41** covering 9/1–9/8. The 5-min tape printed **$1,868.78/MWh @19:30 on 9/2 with EIGHT CONSECUTIVE intervals ≥$1,000.** **My re-specified RED band's every limb is met.** Separately, the 8/16 puzzle **closed exactly as pre-registered** — the verified hourly landed at **$502.38 @19:00 vs my $502.28 forecast, a $0.10 error**, ORANGE not RED, zero hours ≥$1,000 — so **8/16 contributed nothing to this upgrade and remains a transient.** **WATT-02 resolves HIT** on its `§202(c)` limb, and the grading found a defect in my own carry-forward notes (§ WATT-02 below). **Composite 13 → 16/20.**

---

## P1_EPISODE_LIVE_READ_2026-09-02

*Rotated 2026-09-06 (eighth session) · source `STATUS.md` lines 29–34 · 3,783 B · crc32 391420467 · verbatim. Rotation month 2026-09 == file month 2026-09 ✅ (asserted at this splice).*

- **P1 — Stress → price** 🔴🔴 **LIVE EMERGENCY EPISODE, 9/1–9/3+, and it is not over as I write** [boot 2026-09-02 02:47Z + 3 deliberate DM2 range pulls + 2 primary web pulls].
  **① THE POSTINGS** (full board + IDs → KB-WATT-091). One 48-hour window: 3 DOM local warnings (9/1 15:49–16:18) → **#105472 Pre-Emergency Load Management Reduction ACTION** (9/1 17:15, **AEP BGE COMED DOM PEPCO**) → **#105473 Max Gen Emergency/Load Mgmt Alert–Capacity Emergency–NERC EEA 1** (PJM-RTO, 9/1 18:03) → **#105479 same class again** (9/2 16:00) → 3 more AEP/FE-AP local warnings (9/2 19:18–19:22, **inside the price spike**). 🔑 **The Action at 17:15 preceded the Alert at 18:03** — PJM dispatched load management *before* posting the capacity-emergency alert.
  **② THE ORDER.** **DOE §202(c) Order No. 202-26-41**, issued **2026-09-01** to PJM, effective **9/1 → 11:59 PM ET 9/8**: *"directs PJM to dispatch specified units and to order their operation as needed to maintain reliability"* and *"authorizes PJM… to direct **backup generation resources** to operate as a last resort before declaring an Energy Emergency Alert (EEA) 3 or during an EEA 3."* [DOE CESER 2026 202(c) order index, VERIFIED; corroborated independently by PJM Inside Lines 9/2: *"PJM requested and received a combined emergency order… to be effective through Sept. 8… for temporary relief from environmental permit restrictions for generating units **and/or to direct backup generation resources at large loads to operate**"*].
  **③ THE PRICE.** **9/2: max $1,868.78 @19:30 EPT**, **10 intervals ≥$1,000**, **8 of them CONSECUTIVE (19:00, 19:05, 19:10, 19:15, 19:20, 19:25, 19:30, 19:35)** plus an earlier consecutive pair (17:40 $1,093.27 / 17:45 $1,050.64); day mean **$122.64**, n=273 prints. **9/1: max $1,015.61 @19:15**, 2 intervals ≥$1,000 (**not consecutive** — 19:10 printed $949.84), **29 intervals ≥$500** spanning 16:40–20:10, day mean **$150.53**, n=288. [DM2 5-min UNVERIFIED — operational read, not settlement.]
  **④ THE MECHANISM, AND IT IS THE OPPOSITE OF 8/16's.** **Congestion at the $1,868.78 print = $1.25; day max congestion $2.72** ⇒ **99.85%+ of the price is SYSTEM ENERGY**, RTO-wide scarcity. And unlike 8/16 it is **demand-COUPLED**: 9/1 served a **season-high 152,518 MW** [PJM primary; EIA-930 152,547 MW @9/1 18:00 EPT, reconciles to 29 MW]. ⚠️ **Note what that means and it is the uncomfortable read: July's EEA-1 fired at 159,046 MW; this one fired at 152,518 MW — ~6.5 GW LOWER.** PJM went to emergency on **less** load than in July. September carries heavier planned maintenance, so this is consistent with a thinner available-capacity denominator rather than a bigger numerator — **but I have NOT measured the September outage stack and am not asserting it. [INFERRED, flagged for test.]**
  **⑤ RE-READ AT 2026-09-03 07:15 ET — THE EPISODE IS INTO ITS THIRD DAY AND HAS NOT ESCALATED.** New since the 9/2 close: **#105485 Max Gen Emergency/Load Management Alert–Capacity Emergency–NERC EEA 1 (PJM-RTO, 9/3 00:01)** — a **third consecutive EEA-1 day** — and **#105486 Synchronized Reserve Event (priority ACTION, PJM-RTO, 9/3 05:33)**. **NO EEA-2, no voltage reduction, no load shed** ⇒ **the KILL_MEMO cascade did NOT trip; P1 holds at 5, it does not go higher.** Overnight demand troughed at **103,879 MW @10Z** and the morning tape is quiet (**DM2 max $66.02 @07:10 EPT**, 87 prints) — as expected; the risk is the **evening** peak against PJM's **152,496 MW forecast for 9/3**, with a Max Gen Alert and a Load Management Alert already issued for the day and **§202(c) Order 202-26-41 in force to 9/8.** **The next session must re-read the board before citing any of this as past tense.**

---

## P1_8-16_PUZZLE_CLOSED_2026-09-02

*Rotated 2026-09-06 (eighth session) · source `STATUS.md` lines 36–36 · 1,021 B · crc32 2165859202 · verbatim. Rotation month 2026-09 == file month 2026-09 ✅ (asserted at this splice).*

- **P1 — the 8/16 puzzle is CLOSED on its own pre-registered terms** [KB-WATT-090; long form → archive]. The verified hourly finally published: **24/24 rows, max $502.38 @19:00 EPT, ZERO hours ≥$1,000, day mean $78.34** — against the estimate registered **8/17, before the data existed** ($502.28 @19:00, zero ≥$1,000, mean $78.41). Errors: **+$0.10 on the max (0.02%), −$0.07 on the mean**, both inside the ±$22.25 validation band ⇒ **estimator confirmed**, and substantively **8/16 was ORANGE, ~2× below the RED bar.** 🔑 **The registered trigger *"8/16 verified hourly ≥$1,000 → P1 2→3"* is NOT MET — 8/16 contributed ZERO to the P1 upgrade above.** The five eliminated explanations stand; 8/16 stays **UNEXPLAINED and closed**. ⚠️ **Do not retro-fit 8/16 to the September event**: 8/16 was the month's lowest-demand day with no posting; 9/2 was near season-peak with an EEA-1 and a §202(c) order. **Same price band, opposite mechanism — they may not borrow evidence from each other.**

---

## WATT-02_GRADE_AND_READCAP_2026-09-03

*Rotated 2026-09-06 (eighth session) · source `STATUS.md` lines 66–72 · 3,197 B · crc32 1560113384 · verbatim. Rotation month 2026-09 == file month 2026-09 ✅ (asserted at this splice).*

## ✅ WATT-02 — RESOLVED **HIT** · ⚠️ READ-CAP — the self-set 64,000 B budget RETIRED
*(Both records in full: grade → `workbook/PREDICTIONS.tsv` WATT-02 · read-cap reasoning + receipts → `status_archive/STATUS_ARCHIVE_2026-09.md` and this session's commit message. STATUS keeps the verdicts and the lessons.)*

**WATT-02 HIT on its `§202(c)` limb** — criteria verbatim: *">=1 EEA2+ posting **or 202(c) order** in PJM footprint by 9/7"*; **DOE Order 202-26-41**, issued 9/1 to PJM, effective to 9/8. **The postings limb did NOT fire — EEA-1 is not EEA2+.** ⚠️ **It was already a HIT on 2026-07-14** (Order **202-26-35**, PJM, 7/14–7/21) and I called it *"trending MISS"* for seven weeks, because **every carry-forward surface I wrote had dropped the `or 202(c) order` limb** — STATUS *"EEA2+ by Labor Day"*, SCRATCH *"its bar is a **POSTING**"*, and this session's own task brief inherited the compression and handed it back to me as fact. **The registered row was right throughout; four derived surfaces were not.** `[[finding_summary_section_merges_what_the_body_separates]]` — **grade at the registered row, never at the surface that quotes it.** 🔑 **The caveat that caused it is TRUE of the neighbour:** WATT-06's criteria really is posting-only. **A correct caveat migrated to the wrong prediction** (L-40). **Content of the HIT:** recurrence is now **n=3 episodes spanning July AND September** — WATT-06's *"heat-clustered, not a cadence"* read does **not** extend across the season.

**READ-CAP.** The header's *"64,000 B, Will-ratified 2026-08-17"* is **RETIRED**: root `CLAUDE.md` binds every boot-read surface to **32,550 B**, *"binding above any owner-set number… owners choose rotation or hot/cost split, never the number."* **The 8/17 ratification does not survive, and the reason is SCOPE not seniority** — Will ratified the **byte-tier CONVENTION** (set the cap in bytes; a measured B/line beats a default), which is still correct and I keep it. It could not exempt this file from a *physical* limit found later: past **54,250 B** a harness `Read` returns a **partial file with no error**, so a 64,000 B budget authorises a boot that silently reads a fragment while every line-count guard passes. **A budget above the cap is not a looser policy; it is an unenforceable one.** `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]` — **no Will ruling is overridden; a narrower one is superseded by a later, wider one, and I am not treating "Will-ratified" as a shield.** Remedies: `SCRATCH.md` **hot/cold split** (62,072 B → lines 54–367 verbatim to `archive/`, body crc32 **1809430476**, round-trip verified); `STATUS.md` **rotation** (41,493 B → 13 blocks verbatim to `status_archive/STATUS_ARCHIVE_2026-09.md`, per-block crc). **Audited BY OBLIGATION** (rule 17): all 12 owed actions/watches enumerated and re-homed **before** the bytes moved — table in `archive/SCRATCH_ARCHIVE_2026-07-08.md`. ⚠️ **The one that nearly went:** the standing **PJM rate limit** (non-member 6 calls/min, never loop) lived only in rotated session notes — an operational constraint, not history. Now in the live `SCRATCH.md` header.


---

## OPEN5_WINTER_GATE_2026-09-02

*Rotated 2026-09-06 (eighth session) · source `STATUS.md` lines 78–78 · 883 B · crc32 494082341 · verbatim. Rotation month 2026-09 == file month 2026-09 ✅ (asserted at this splice).*

5. **⚠️ Winter P1 registration is GATED and the gate HELD — full basis KB-WATT-076, do not re-derive.** In one line: **never register "no EEA because El Niño."** AEOLUS established winter **energy/mean DOWN**; winter **PEAK — NO SIGN** (n=2, split), and **2023-24 is decisive** (warmest US winter on record AND PJM still peaked 134,777 MW on 1/17/24, running Cold Weather Advisory → Alert → Conservative Operations → NERC TLR-1). Any winter call must be **peak-based, sign-agnostic, weighted mid-Jan–Feb, not December.** 🔑 **Reinforced this week:** September's episode fired at a **lower** load than July's — **the load level at which PJM goes to emergency is not a constant**, so a peak-based call must not be pinned to a fixed MW threshold. ⚠️ Vintage: ONI is revised as ERSSTv5 updates; **never mix +2.03 and +1.2 in one sentence** (different baselines).

---

## OPEN7_ERCOT_DISCRIMINATOR_2026-09-02

*Rotated 2026-09-06 (eighth session) · source `STATUS.md` lines 80–80 · 814 B · crc32 1192047109 · verbatim. Rotation month 2026-09 == file month 2026-09 ✅ (asserted at this splice).*

7. **🟡 Run the ERCOT discriminator** (WALTER SIG-W-20260828-049): ERCOT North Hub **Cal-27 ~$42/MWh**, all four strips below early July — a **counter-signal** to the data-centre demand story. **WALTER named the discriminator and it is mine: gas-cost story or demand story?** Partial answer leans **demand/supply, not gas** — front Henry Hub *rose* ~12% (2.694 → 3.017) over roughly the window in which Cal-27 fell ~18%, so implied heat rate compressed. ⚠️ **[INFERRED — basis mismatch stated]**: that pairs a **chart-read** Cal-27 level with a **spot** gas move. The clean test needs the ERCOT Cal-27 strip and the Henry Hub Cal-27 strip **on the same date**; I can pull neither free. ⚠️ **Levels are chart-read — never quote as settles or set a threshold on them** (WALTER's caveat, adopted).

---

## BOTTOM_LINE_2026-09-03

*Rotated 2026-09-06 (eighth session) · source `STATUS.md` lines 101–101 · 1,181 B · crc32 2557202554 · verbatim. Rotation month 2026-09 == file month 2026-09 ✅ (asserted at this splice).*

**The channel this desk was built for finally fired, and it fired clean:** PJM ran a capacity emergency on two consecutive days, dispatched load management in five zones, served a season-high **152,518 MW**, and operated under **DOE §202(c) Order 202-26-41**, while the tape printed **$1,868.78/MWh across eight consecutive five-minute intervals** with congestion of **$1.25** — 99.85% system-wide scarcity — so the RED band I hardened two weeks earlier met **every** limb. **P1 2→5, composite 13→16/20, status 🟠→🔴, no deploy-posture change.** What makes the upgrade trustworthy is what it did *not* lean on: the 8/16 mystery closed on its own pre-registered terms at **$502.38 vs a $502.28 forecast** — ORANGE, zero hours ≥$1,000 — so its upgrade trigger did **not** fire and contributed nothing. **The session's uncomfortable finding is in my filing cabinet, not the market:** WATT-02 resolves **HIT** and was already a HIT on **7/14**, because every summary surface I wrote had dropped the *"or 202(c) order"* limb the registered row always carried. **Next:** the episode is live through ~9/8 — re-read the board before citing any of this as past tense.

---

## P3_32_VS_55_GW_BASIS_2026-09-06

*Rotated 2026-09-06 (eighth session, second pass) · 729 B · crc32 1006411970 · verbatim. Rotation month 2026-09 == file month 2026-09 ✅ (asserted at this splice). Stable methodological background for the 32/55 GW split; the LIVE seam state stays on STATUS.*

**32 GW is the firm figure** (PJM's vetted system-**coincident** peak growth, 30 GW data centers); **55 GW is an aggregate of utility-REPORTED forecasts**; the ~23 GW gap is **non-coincidence + self-report duplication**, *not* a vetting haircut (PJM's 2026 trim cut summer-2028 peak 4.4 GW / 2.6%; large loads only **0.7%**) and *not* queue attrition (those stats are **GENERATION**-queue, wrong population). **Curtailability is a RECLASSIFICATION, not a haircut:** NCBL went voluntary, is **NOT in effect**, and 28/29 cleared at cap AND short without it ⇒ **capacity-obligation offset = 0 GW today.** **STANDING DOUBLE-COUNT GUARD:** never add IPP PPA-MW (VST 3,800+2,609, TLN 1,920) or a filer's site MW to capex-implied MW.


---

## FIRED_COUNT_CHANNEL_KILL_NARRATIVE_2026-09-06

*Rotated 2026-09-06 (eighth session, third pass) · 1,258 B · crc32 2639500453 · verbatim. Rotation month 2026-09 == file month 2026-09 ✅ (asserted at this splice). The summer channel-kill / L-42 narrative; its live obligation is now discharged by the registered prediction WATT-11, so STATUS keeps the count and the pointer.*

**Fired-count: 2 of 4** *(was 1 of 4 — P1 joins P2)*. **Thesis-kill vs channel-kill:** the summer **killed P1's live read** (4→3→2, WATT-03 MISS, WATT-06 MISS) and **September brought it back at 5** — which is the migration path in reverse and worth naming honestly: **a channel-kill is seasonal, and I said so at the time** (*"a mild summer kills P1's live read for the season, NOT the structural thesis"*). **The channel was not dead; it was out of season.** ⚠️ **The correct lesson is NOT "I was wrong to de-escalate"** — WATT-03 and WATT-06 were graded correctly on their windows, and de-escalating on evidence is what the rail is for. **The lesson is that a channel-kill has an expiry the rail never wrote down** (L-42). ✅ **DISCHARGED 9/6: `WATT-11` writes that expiry down** — zero EEA-class postings and zero new §202(c) orders in the PJM footprint, **9/15 → 11/30**. A quiet autumn confirms the channel is heat-coupled and seasonally dormant; **an autumn emergency with no heat event says the constraint is reserve margin, which is a P2 escalation and a materially bigger read than any single summer episode.** The thesis dies only if the 29/30 BRA clears well below cap **AND** data-center queues drain. Neither is in evidence.

---

## INSTRUMENT_RETENTION_AND_FLAG_SCOPE_2026-09-06

*Rotated 2026-09-06 (eighth session, fourth pass) · 0 B · crc32 0 · verbatim. Rotation month 2026-09 == file month 2026-09 ✅ (asserted at this splice). Full reasoning now lives at LESSONS L-44 and KB-WATT-101/104; STATUS keeps the operative one-liner.*



---

## INSTRUMENT_RETENTION_AND_FLAG_SCOPE_2026-09-06

*Rotated 2026-09-06 (eighth session, fourth pass) · 1,739 B · crc32 2575662558 · verbatim. Rotation month 2026-09 == file month 2026-09 ✅ (asserted at this splice). Full reasoning now lives at LESSONS L-44 and KB-WATT-101/104; STATUS keeps the operative one-liner.*

## INSTRUMENT — a limit found this session, and the guard it broke

⚠️ **The PJM DM2 `rt_unverified_fivemin_lmps` feed retains only ~15 days and returns the surviving slice with NO error.** Measured 9/6: an 8/10–8/23 request returned **336 rows covering 8/22–8/23 only**. `read_pjm_onpeak_mean` guarded on `len(vals) < 100` — a **COUNT** check — so a truncated 14-day request still passes and returns **a 2-day mean labelled as a 14-day one.** **Fixed this session:** per-day **COVERAGE** assert (every requested day present, each ≥150 of 192 on-peak prints), raising with the missing days named. Full reasoning → **L-44**.
⚠️ **WHAT THE CONTAMINATION FLAG IS, NARROWLY** (tightened 9/6, CODEX r2 — it verified the coverage repair against synthetic missing/thin days and correctly narrowed this): a **single-day outlier detector against the window median**, *not* an emergency-window classifier. **It fails BY CONSTRUCTION when the contaminated days are the MAJORITY** — 4 high days of 6 lift the median and nothing fires. It caught this window only because 9/1 alone was extreme (3.1× a $68.36 median). **Read a silent flag as "no single day dominates," never as "this window is clean."** No second detector is being built; the wording is the fix.
**Consequence, scoped:** a same-vintage spark older than ~15 days is **not re-derivable from the 5-min feed** — but PJM retains longer-lived hourly data (8/12–8/17 came back complete on `rt_hrl_lmps`), so a *comparable* reconstruction exists. Whether the **July EEA-1** comparison can be rebuilt that way is **UNTESTED, not foreclosed.** → **§ CORRECTIONS #10**. **Forward rule: record the window COMPOSITION beside every spark figure at write time.**

---

---

## P1_EPISODE_CLOSE_DETAIL_2026-09-06

*Rotated 2026-09-06 (eighth session, fifth pass) · 1,636 B · crc32 3999152782 · verbatim. Rotation month 2026-09 == file month 2026-09 ✅ (asserted per block). The episode closed 9/3; its blow-by-blow is history. STATUS keeps the verdict + the de-escalation clock.*

  **① IT BROKE ON THE 9/3 EVENING PEAK.** PJM forecast **152,496 MW for 9/3** with a Max Gen Alert and a Load Management Alert already issued, and the tape answered: **max $437.15 @18:50, ZERO intervals ≥$500, zero ≥$1,000, day mean $55.20** (n=288). Then **9/4 max $149.05 / mean $44.55**, **9/5 max $157.68 / mean $43.81**, **9/6 max $26.29 @01:10** (latest $18.85 @10:25). Demand today **86,814 MW @9/6 13Z = 71.7%** of a **121,088 MW** 24h peak — against **152,518 MW on 9/1**, the episode's peak *(not a "season high" — July's EEA-1 ran at 159,046 MW; → § CORRECTIONS #6)*.
  **② NO ESCALATION, AND THE NEGATIVE IS CARRIED PROPERLY.** No EEA-2, no EEA-3, no voltage reduction, no load shed ⇒ **KILL_MEMO cascade C1/C3 never tripped.** Board today: **15 postings, latest 9/4 13:50, all routine local Post Contingency Local Load Relief Warnings + a Hot Weather Alert — zero emergency-class.** ⚠️ **The board is a CURRENT view, not a history** (msg_ids 105484–86 and 105488–89 have already dropped off), **so the board cannot prove the negative** — the *tape* does: a load shed does not happen at a $437 peak. Stating which instrument carries the negative, because the one I looked at first could not.
  **③ SEASON TOTAL: 3 episodes, all heat-clustered, all closed** — detail in the § Season emergency count line below; the 9/1–9/3 read verbatim → `status_archive/STATUS_ARCHIVE_2026-09.md` § `P1_EPISODE_LIVE_READ_2026-09-02`. **④ The 6.5 GW gap (July EEA-1 @159,046 MW vs September @152,518 MW) is still INFERRED, not measured, and the 5-min tape for July has now aged out** — see OPEN #4.

---

## WAKE_SET_FULL_2026-09-06

*Rotated 2026-09-06 (eighth session, sixth pass) · 2,110 B · crc32 2140886012 · verbatim. Rotation month 2026-09 == file month 2026-09 ✅ (asserted per block). The full 12-row wake set; STATUS keeps the dated near-term rows, and `NEXUS_BRIEF.md` carries the cross-agent routing.*

## WAKE SET — named triggers, dates, owners (for PROME BD-02)
*Written because this desk has gone 16 days dark twice this summer, and both times a live channel moved while it was dark.*

| # | trigger | date / cadence | who sees it first | why it needs WATT |
|---|---|---|---|---|
| 1 | **🔴 PJM EEA-2, EEA-3, voltage reduction, or load shed** | any time; **episode closed 9/3 — none occurred** | WALTER / any boot | KILL_MEMO cascade event — the only P1 state above the current one |
| 2 | **🔴 §202(c) 202-26-41 EXPIRY / extension** | **11:59pm ET Tue 9/8** | WATT / WALTER | lapse is limb ① of P1's 5→3; an **extension** re-arms P1 |
| 2b | **P1 de-escalation review** | **9/10** (7 clear days from #105485) | WATT | the dated half of the rule — must not be missed in either direction |
| 3 | **FERC order on the IRAS petition** (`ER26-3515-000`) | **~10/12, outer bound 10/31** | WATT | resolves **WATT-10**; near-term resolver for WATT-08 |
| 4 | **FERC ruling on the 3 EL26-67 abeyance motions** | overdue since ~8/07 — **~30 days** | WATT | sets **WATT-09**'s resolve date (8/17-era vs ~mid-Nov) |
| 4b | **WATT-11 autumn-shoulder window** | **9/15 → 11/30** | WATT / WALTER | the heat-vs-reserve-margin discriminator; **absence is the data** |
| 5 | **PJM's substantive EL26-67 response** | 8/17 if denied, ~11/15 if granted | WATT | resolves **WATT-09** |
| 6 | **NERC ride-through enforcement provisions filed** | **by 2026-12-31** (FERC-ordered) | WATT | the un-sized AI-capex compliance cost line |
| 7 | **PJM 29/30 BRA** | ~mid-2027 | WATT | the clean bidirectional thesis flip |
| 8 | **Winter P1 window** | **mid-Jan–Feb 2027**, not December | AEOLUS → WATT | the gated registration; peak-based, sign-agnostic |
| 9 | **GEV Q3'26 10-Q** — does slot GW keep outgrowing firm conversion? | **~Oct 2026** | DEWEY (T2) | WATT's turbine-leg read of the power-equipment order book |
| 10 | **Mead actual crossing 1,035 ft** | AEOLUS watches; ~10/27 straight-line, bias-adj. later | AEOLUS | **NOT a WATT score** — out of footprint (WECC, not PJM); see the AEOLUS answer |

---

## CORRECTIONS_ROWS_RESOLVED_2026-09-06

*Rotated 2026-09-06 (eighth session, seventh pass) · 852 B · crc32 1630399481 · verbatim. Rotation month 2026-09 == file month 2026-09 ✅ (asserted per block). Ledger rows #5 (BRA cap ratio) and #12 (IRAS docket tier) — both RESOLVED at primary; their live facts sit in the P2 block and KB-WATT-032/102. STATUS keeps only rows whose withdrawal is still live guidance.*

| # | claim | status | resolution | caught by |
|---|---|---|---|---|
| 5 | 28/29 cleared at **"97.5% of cap"** | ✅ **RESOLVED at PJM primary** | **$325 IS the 28/29 cap; cleared at 100%.** PJM 7/14 headline: *"Comes in at the Cap of $325, **Down 2.5%**"* — 🔑 **that 2.5% is the YoY cap decrease, relabelled here as within-year utilisation: a real figure with a swapped denominator**, which is why it passed every arithmetic check. WATT-01 HIT unaffected | CODEX r1/r4 + self r3 |
| 12 | IRAS docket **"not primary-verifiable"** | ✅ **RESOLVED — PRIMARY-VERIFIED** | `ER26-3515-000`, *"…IRAS & a Large Load Registry **to be effective 10/12/2026**"*, filed 8/13/26, acc. 20260813-5118 — **FR/GPO govinfo FR-2026-08-18.** ⛔ **"eLibrary blocked ⇒ primary unreachable" was a false dead end: one blocked door treated as the only door.** ⚠️ EL26-67 absent from *this* notice = scoped negative | CODEX r3 |

---

## CORRECTIONS_LEDGER_FULL_2026-09-06

*Rotated 2026-09-06 (eighth session, eighth pass) · 4,585 B · crc32 3973363341 · verbatim. Rotation month 2026-09 == file month 2026-09 ✅ (asserted at this splice). The full 11-row withdrawal register from the 5-round external review; the review cycle is CLOSED and every row's lesson lives in `LESSONS.md` L-46…L-50 and `workbook/KB.tsv` KB-103/105/106/107. STATUS keeps a pointer + the standing do-not-reassert list.*

## ⛔ CORRECTIONS LEDGER — every claim withdrawn or scoped, in ONE place
*Canonical home. Cells and live reads carry a one-line flag and point HERE; nothing restates the reasoning. Opened 2026-09-06 after an external review (CODEX, two rounds) plus two self-catches. **Verified at the artifacts by me before acceptance in every row.***

| # | claim as it stood | status | what is defensible instead | caught by / lesson |
|---|---|---|---|---|
| 1 | §202(c) shows backup gen **"operationally relied upon"** / **"LIMB (c) RAN"** | ⛔ **WITHDRAWN** | **authority granted ✅ · deployment observed ❓UNKNOWN · para. E utilisation record ❌.** Kept distinct + still verified: ACTION #105472 (5 zones) **was** dispatched = demand response | CODEX r1 · **L-47** |
| 2 | 55 GW wording **"agreed with VULCAN, verbatim in its files"** | ⛔ **WITHDRAWN** | Seam agreed on the **number**, **OPEN on the POPULATION**. `VULCAN/STATUS.md:27` still reads "55 GW **nameplate** interconnection ceiling" under "SEAM CLOSED" | CODEX r1 · **L-46** |
| 3 | P2 + P3 are **"two INDEPENDENT structural roots"** | ⛔ **WITHDRAWN** | **Linked** — PJM's auction reliability requirement is computed FROM the load forecast P3 measures. Complementary, not independent | CODEX r1 · **L-48** |
| 4 | §202(c) order **"[VERIFIED ×2]"** | ⚠️ **SCOPED** | Two independent publications for the order's **existence/terms**; **one lineage** for the stress narrative (DOE recites PJM's application) | CODEX r1 · **L-48** |
| 6 | **"season-high 152,518 MW"** (9/1) | ⛔ **WITHDRAWN** | **The episode's peak.** My own text records July's EEA-1 at **159,046 MW** — "season-high" was false on this surface's own numbers | CODEX r1 |
| 7 | Spark **"widened for a third consecutive read / moving away from the trigger"** | ⛔ **WITHDRAWN** | The **rolling averages do not establish persistent widening** — each window's level tracked its emergency-day count | self, 9/6 · **L-45** |
| 8 | **"the spark never moved"** *(my own first correction)* | ⛔ **WITHDRAWN** | Adjusted series **+$30.46 → +$41.09 → +$26.33 → +$28.98**: a mid-Aug window sits ~35% above 8/4 **even after excluding 8/16**, and does not persist. **Both "widened for a third read" and "never moved" are withdrawn**; what survives is only *"the reported readings do not establish persistent widening"* | CODEX r2/r5 · **L-49** |
| 9 | boot window "contains **FOUR** emergency days" | ⚠️ **CORRECTED** | **THREE** (9/1, 9/2, 9/3). Measured per-day on-peak: 8/31 $51.38 · **9/1 $210.35 · 9/2 $157.68 · 9/3 $68.36** · 9/4 $52.49 · 9/5 $47.12 | self, 9/6 |
| 10 | 8/17's +$48.12 **"permanently unauditable"** | ✅ **WITHDRAWN — reconstruction done, PROVISIONAL** | `rt_hrl_lmps` retains **≥67 days**; all four published sparks reproduce within **$0.62**. Excluding 8/16 lowers the window spark **$7.04 (14.6% of $48.13)**. ⛔ *"contamination", "floor" and the 17% figure (adjusted-value denominator) all WITHDRAWN → #13* | CODEX r2/r5 |
| 11 | "no doorbell — **no named deadline**" | ⚠️ **REASONING INCOMPLETE** | Rule 6b leg 3 has **TWO** limbs: **3a** named referent **and 3b** cadence (dark duration > the desk's own **p75** inter-session gap, WALTER `BOARD_CONSUMPTION_SPEC` §3.5.7, n≥8 or 3b cannot fire). **Neither fires here**, so the decision stands — but **apply both branches, never stop at 3a**. ⛔ *I then said the reviewer used "a proxy, not the declared estimator" — **WRONG, withdrawn**: `BOARD_CONSUMPTION_SPEC.md:264` defines the statistic AS "calendar days between consecutive **AUTHORED commit-days**," which is exactly what it used, with n=12 (VULCAN) and n=17 (DEWEY), both ≥8 ⇒ **3b was computable and simply did not fire.*** | CODEX r2, r3 |
*(Rows **#5** BRA cap ratio and **#12** IRAS docket tier are **RESOLVED at primary** and rotated verbatim → `status_archive/STATUS_ARCHIVE_2026-09.md` § `CORRECTIONS_ROWS_RESOLVED_2026-09-06`; their live facts sit in the P2 block above.)*

| 13 | The reconstruction write-up: **"de-contaminated"**, **"contamination is a FLOOR"**, **"identifies the gas vintage"**, **"17%"/">100%"** | ⛔ **ALL WITHDRAWN same-day** | **Sensitivity analysis, not error correction** · **no floor** (4 mixed-sign offsets don't bound 8/16; PJM hourly *is* a 5-min average, so smoothing hits peaks not means) · gas $2.690 **INFERRED** (a fit with 2 unknowns that can offset) · **14.6% and 50.6%** — my percentages used the **ADJUSTED value as denominator**, ⚠️ **the same denominator error as the BRA cap, one day later** | CODEX r5 |

---

---

## `P4_RECONSTRUCTION_AND_CLOSED_ITEMS_2026-09-10` — rotated verbatim from STATUS.md at the ninth session (2026-09-10)

**Rotation reason:** STATUS measured 31,026 B = 95% of the 32,550 B fleet read-cap at boot on 2026-09-10, and the session ADDS the DOCKET-L249 grade. Blocks below are settled 2026-09-06 session detail whose surviving one-line reads stay on STATUS. **Rotation, never deletion.** Source crc32 of STATUS.md before this rotation: **3915194899** (31,026 B, 123 lines, `PROME/tools/measure.py`).

### Block A — P4 spark reconstruction table + method paragraphs (STATUS lines 37–48)

| read | window | reconstructed | **adjusted** *(high day excluded)* | Δ within reconstruction | as published |
|---|---|---:|---:|---:|---|
| 8/4 | 7/29–8/3 | +$30.46 | *n/a — no day excluded* | — | +$29.84 |
| 8/17 | 8/11–8/16, minus **8/16** | +$48.13 | **+$41.09** | **−$7.04 = 14.6%** of $48.13 | +$48.12 |
| early Sept | 8/27–9/1, minus **9/1** | +$53.32 | **+$26.33** | **−$26.99 = 50.6%** of $53.32 | +$53.65 |
| post-episode | 9/4–9/5 | +$28.98 | *n/a* | — | +$28.98 |

  🔑 **THIS IS A SENSITIVITY ANALYSIS, NOT AN ERROR CORRECTION** *(reframed 9/6 on review; "de-contaminated" was an overclaim).* **The published readings were not wrong** — they measured windows holding real high-price days. What it shows: **a 6-day window mean is extremely sensitive to one day**, so the series cannot carry a trend claim either way.
  ⚠️ **8/16 WAS NOT AN EMERGENCY DAY — my own record says so** (no posting, no §202(c); KB-068/069). Excluding it is a **judgment** that it was a self-classified transient, not an "emergency-free" criterion. **9/1's exclusion is better founded** (EEA-1 + §202(c)). **The two exclusions do not have equal standing.**
  🔑 **THE SURVIVING READ, and it is narrower than what I published this morning:** the reported readings **do not establish persistent widening** — the adjusted series runs **+$30.46 → +$41.09 → +$26.33 → +$28.98**, up then back below its own baseline. ⛔ **Both "the spark widened for a third consecutive read" AND "the spark never moved" are withdrawn**; what remains is that **a mid-August window sits ~35% above the 8/4 window even after excluding 8/16**, which no window artefact explains.
  ⚠️ **METHOD, with its uncertainties NOT smoothed over:** window recovered from my own archive (*"trailing 6d, n=1,144"* ⇒ 8/11–8/16). **Gas vintage $2.690 is INFERRED, not recovered** — I chose it because it reproduces the published spark, and with the original gas input unrecorded **and** the power feed changed, **two unknowns can offset**; a 1¢ fit is a *compatible* reconstruction, not proven provenance `[[finding_crosscheck_with_free_parameter_validates_nothing]]`. ⛔ **My "the contamination is a FLOOR" claim is WITHDRAWN** — four mixed-sign feed offsets (−$1.27 to +$0.08) do not bound 8/16, and **PJM's hourly price IS an average of the 5-min values**, so smoothing reduces *peaks*, not necessarily *means*. All four published figures reproduce within **$0.62** — that much stands.
  ⚠️ **Basis:** RT on-peak LMP ≠ ICE peak-period OTC. ⚠️ **N5 (i-b): spark stays PROVISIONAL** until the NG=F settlement clock is established.

### Block B — fired-count / channel-kill narrative (STATUS line 76)

**Fired-count: 2 of 4** *(P1 + P2)*. ⚠️ **P1's is a SPENT fire, not a live one** — the season count stands; the live rail reads NOT-FIRED as of 9/6. **Thesis-kill vs channel-kill:** the summer killed P1's live read (WATT-03/WATT-06 MISS, correctly graded) and September brought it back at 5 — **the channel was not dead, it was out of season**, and **L-42's "a channel-kill has an expiry the rail never wrote down" is now DISCHARGED by `WATT-11`** (zero EEA-class postings + zero new §202(c) orders, 9/15→11/30). Falsification: a non-heat autumn emergency **OPENS AN INVESTIGATION — it does not establish reserve-margin erosion.** Outage-cluster, transmission and fuel-supply explanations must each be eliminated first (`WATT-11` `if_falsified` governs). ⛔ *This line read "…says the constraint is reserve margin ⇒ P2 escalation" until 9/6 — the withdrawn automatic inference, surviving in a summary after the ledger fix landed. **Third time a canonical fix failed to reach its summary.*** *Full narrative verbatim → `status_archive/STATUS_ARCHIVE_2026-09.md` § `FIRED_COUNT_CHANNEL_KILL_NARRATIVE_2026-09-06`.* The thesis dies only if the 29/30 BRA clears well below cap **AND** data-centre queues drain. Neither is in evidence.

### Block C — OPEN row 6, VULCAN both legs closed (STATUS line 99)

| 6 | ✅ **BOTH VULCAN LEGS NOW CLOSED.** Wording committed verbatim (`db3d4ae2b`) — ⚠️ and VULCAN corrects my provenance: the "nameplate" phrasing was **my own** imprecision from 8/4, which my packet mis-assigned. **Backup-dispatch leg ANSWERED: `FL-WATT-08` never priced limb (c) as observed** — it is dated **four weeks before** the order and carries **no interruption term at all**; its only physical input is a price series. **Nothing to correct.** ⚠️ *And VULCAN had already answered in `db3d4ae2b` — I doorbelled without checking the inbox first.* **Still owed BY ME: hedged-vs-floating** | ✅ closed |

### Block D — OPEN row 6b, CRWV DSCR conditional (STATUS line 100)

| 6b | 🟠 **CONDITIONAL — the 9/1–9/3 window reaches `FL-WATT-08` by PRICE, not by event, on a ~3-month lag.** The 9/2 tape ($1,868.78, 8 consecutive ≥$1,000) is realized cost feeding the covenant's **trailing-three-month mark (~Dec 2026)**. ⚠️ **NOT registered as a dated catalyst — its premise is open.** The covenant marks *Excess **UNHEDGED** Power Costs*: largely hedged ⇒ never reaches DSCR; largely floating ⇒ September lands in December. 🔑 **Resolve the split FIRST — my owed deliverable is the switch, and the date only exists on one branch** | premise first |

### Block E — OPEN row 7, GPU-instrument ruling (STATUS line 101)

| 7 | ✅ **RULED 2026-09-03 — and I never saw it.** Owner **VULCAN**, **BOTH tiers PLUS the spread**, exchange-primary first, **re-decide 10/05** (ruling `ff2efeeff`, verified at the artifact today). ⚠️ **The cc line named WATT and DEWEY and no copy was ever written to either inbox** — *a cc in a header is a label, not a delivery* `[[finding_delivery_check_is_not_a_knowledge_check]]`. My "unruled" reading was correct for the artifacts I could see. 🔑 **The ruling went BROADER than my recommendation *because of* my finding:** I proposed contract-tier-only; **my sign-inversion evidence is why PROME ruled both tiers + the spread.** ✅ **VULCAN's 9/3 amendment is ANSWERED by the ruling — I owe VULCAN nothing on it** | re-decide **10/05** |

### Block F — P1 episode-close detail bullet (STATUS line 30)

  **THE CLOSE, in three numbers:** 9/3 evening peak **$437.15 max, 0 intervals ≥$500** against a 152,496 MW forecast · 9/4–9/6 benign ($149.05 / $157.68 / $26.29) · demand **71.7%** of a 24h peak that fell 152,518 → 121,088 MW. **No EEA-2/3, no voltage reduction, no load shed.** ⚠️ **The negative is carried by the TAPE, not the board** — the PJM page is a CURRENT view and cannot prove a historical negative. **Season total 3 episodes, all heat-clustered, all closed.** ⚠️ **The 6.5 GW gap (July EEA-1 @159,046 MW vs Sept @152,518) is still INFERRED** → OPEN #4. *Blow-by-blow verbatim → `status_archive/STATUS_ARCHIVE_2026-09.md` § `P1_EPISODE_CLOSE_DETAIL_2026-09-06`.*


### Block G — CONVERGENCE MATRIX P1 cell, 9/6 vintage (STATUS line 16)

| **P1** | Stress → price | **5 🔴🔴** *(held)* | **EPISODE CLOSED 9/3, NO ESCALATION — and 5 is held by the RULE, not by the grid.** The 9/3 evening peak PJM forecast at 152,496 MW **never reached even the ORANGE band** ($437.15 max, **0 intervals ≥$500**). 9/4–9/6 fully benign. **No EEA-2, no EEA-3, no voltage reduction, no load shed ⇒ the KILL_MEMO cascade never tripped.** ⚠️ **I am not de-escalating early to match the tape** — the registered rule has two limbs and both still bind (right-hand column) | shares the heat antecedent with P4 — **count the September heat root ONCE**. ⚠️ Independent of the 8/16 event, closed as a transient | **[9/6 14:32Z, VERIFIED]** DM2 5-min: **9/3 max $437.15 @18:50, 0 ≥$500, mean $55.20** · 9/4 $149.05 · 9/5 $157.68 · 9/6 $26.29. Demand **86,814 MW = 71.7%** of a 121,088 MW 24h peak (vs **152,518 MW on 9/1**, the episode's peak — ⛔ *previously written "season-high"; my own text records July's EEA-1 at **159,046 MW**, so "season-high" was false on this surface's own numbers* [CODEX 9/6]). Board: 15 postings, latest 9/4 13:50, **all routine local — zero emergency-class** | **DE-ESCALATION ARITHMETIC, both limbs binding:** ① **§202(c) 202-26-41 is in force to 11:59pm ET 9/8** and the rule holds 5 while any of {EEA posting, §202(c) order, Max Gen Alert} stands. ② Last emergency-class posting **#105485 EEA-1, 9/3 00:01** ⇒ 7 clear days complete **end of 9/10**. **⇒ earliest legitimate 5→3 is 9/10–9/11, and only if the Hot Weather Alert is lifted.** 5 remains the ceiling |

### Block H — CONVERGENCE MATRIX P4 cell, 9/6 vintage (STATUS line 19)

| **P4** | Gas → power coupling | **2 🟡** | **NOT-FIRED.** Defensible form: **the post-episode reading RETURNED NEAR the August baseline; the rolling averages do not establish persistent widening.** ⛔ 3 claims withdrawn → **§ CORRECTIONS #7 #8 #9** | shares the heat antecedent w/ P1 | **CLEAN post-episode (primary): +$28.98/MWh** — on-peak mean (HE08–23 EPT, **9/4–9/5**, n=384) PJM-RTO RT LMP **$49.81** − 7.0 × HH **$2.975** (9/4, gap 1d ≤ 3d limit ✅). @HR 8.0: **+$26.01**. ⛔ **The boot's same-vintage +$77.02 (8/31–9/5) is REFUSED as a level — its window contains THREE emergency days** *(9/1, 9/2, 9/3; "FOUR" was my own error, corrected 9/6 against the measured per-day on-peak means: 8/31 $51.38 · **9/1 $210.35 · 9/2 $157.68 · 9/3 $68.36** · 9/4 $52.49 · 9/5 $47.12)*; the stress-window figure for the record is **+$124.62** (9/1–9/3, n=575). Series on one basis: **+$29.84 (8/4) → +$48.12 (8/17, ⚠️ re-derivable only from a DIFFERENT feed, see § INSTRUMENT) → +$28.98 (9/4–9/5 clean)** | compresses 50% or negative, sustained 3+ sessions → 3 — **on ONE consistent basis, and now also on ONE uncontaminated window** |

### Block I — P2 live-channel bullet, 9/6 vintage (STATUS line 36)

- **P2 — Structural capacity cost** 🔴🔴 **AT MAX, the switch is a FILING, and limb (c)'s MECHANISM was AUTHORISED — not observed running.** Auction leg unchanged: **28/29 BRA cleared 7/14 at $325/MW-day = AT the cap (100% of the 28/29 cap; $333.44 was 27/28's, and PJM's "Down 2.5%" is the YoY cap change, not a utilisation ratio)**, **6,831 MW short**; 138,318 MW UCAP+DR procured; **$16.4B** vs ~$30B uncapped. **3rd straight at-cap clear, 2nd consecutive RTO-wide shortfall. WATT-01 HIT.** Attribution caveat: ~$6.3B of the $16.4B pinned on data centers is the **Market Monitor's** figure, **not PJM's**. ⭐ **NEW AND IT IS THE SESSION'S BEST P2 ITEM:** IRAS limb (c) proposes *"emergency load reduction procedures prioritizing large loads over residential consumers."* **Order 202-26-41 authorised PJM to direct backup generation at large loads — the same policy, GRANTED as emergency authority, while the tariff version sits at FERC.** ⇒ **the AUTHORITY is running ahead of the tariff.** ⛔ *Previously written as "executed as an emergency action" and "the practice is running ahead" — that reads permission as use and is **WITHDRAWN** [CODEX 9/6]. Whether any backup generation actually operated is **UNKNOWN** pending the para. E utilisation report.* That is corroboration for WATT-08/WATT-10's direction **but must NOT be banked as an outcome** — an emergency order is precisely the *"emergency action"* status quo that limb (c) seeks to convert into a **standing commercial term of service**. **The gap between them is the whole prediction.**

### Block J — OPEN rows 6 / 6b / 7, 9/6 vintage (STATUS lines 91-93)

| 6 | ✅ **BOTH VULCAN LEGS NOW CLOSED.** Wording committed verbatim (`db3d4ae2b`) — ⚠️ and VULCAN corrects my provenance: the "nameplate" phrasing was **my own** imprecision from 8/4, which my packet mis-assigned. **Backup-dispatch leg ANSWERED: `FL-WATT-08` never priced limb (c) as observed** — it is dated **four weeks before** the order and carries **no interruption term at all**; its only physical input is a price series. **Nothing to correct.** ⚠️ *And VULCAN had already answered in `db3d4ae2b` — I doorbelled without checking the inbox first.* **Still owed BY ME: hedged-vs-floating** | ✅ closed |
| 6b | 🟠 **CONDITIONAL — the 9/1–9/3 window reaches `FL-WATT-08` by PRICE, not by event, on a ~3-month lag.** The 9/2 tape ($1,868.78, 8 consecutive ≥$1,000) is realized cost feeding the covenant's **trailing-three-month mark (~Dec 2026)**. ⚠️ **NOT registered as a dated catalyst — its premise is open.** The covenant marks *Excess **UNHEDGED** Power Costs*: largely hedged ⇒ never reaches DSCR; largely floating ⇒ September lands in December. 🔑 **Resolve the split FIRST — my owed deliverable is the switch, and the date only exists on one branch** | premise first |
| 7 | ✅ **RULED 2026-09-03 — and I never saw it.** Owner **VULCAN**, **BOTH tiers PLUS the spread**, exchange-primary first, **re-decide 10/05** (ruling `ff2efeeff`, verified at the artifact today). ⚠️ **The cc line named WATT and DEWEY and no copy was ever written to either inbox** — *a cc in a header is a label, not a delivery* `[[finding_delivery_check_is_not_a_knowledge_check]]`. My "unruled" reading was correct for the artifacts I could see. 🔑 **The ruling went BROADER than my recommendation *because of* my finding:** I proposed contract-tier-only; **my sign-inversion evidence is why PROME ruled both tiers + the spread.** ✅ **VULCAN's 9/3 amendment is ANSWERED by the ruling — I owe VULCAN nothing on it** | re-decide **10/05** |

### Block K — BOTTOM LINE + composite note, 9/6 vintage (STATUS lines 21, 113-115)

**Composite: 16/20** *(P1 5 + P2 5 + P3 4 + P4 2 — **unchanged, and the stillness is the honest read.** The grid de-stressed materially this week and the composite did not move, because P1's de-escalation rule is dated (9/10) and I am not front-running it, and because P4's apparent widening turned out to be my own measuring window. **A session that corrects two of its own numbers and moves no score is not a session with no signal** — the P4 correction is the signal.)*

## BOTTOM LINE

**The September emergency episode closed 9/3 without escalating** — the 9/3 evening peak, forecast at 152,496 MW, printed **$437.15 with zero intervals over $500** — and **P1 holds at 5 only because its own dated rule has not been met** (§202(c) to **9/8**; seven clear days to **9/10**). **Composite 16/20, unchanged.** **The session's work was almost entirely on my own instruments, and the last piece is deliberately narrower than it started:** on a verified-hourly reconstruction, **excluding the single highest day lowers the 8/17 window spark by $7.04 (14.6%) and the early-September one by $26.99 (50.6%)** — which shows a 6-day mean is dominated by one day, **not that the published readings were wrong.** ⛔ **"De-contaminated", "the contamination is a floor", "identifies the gas vintage" and my 17%/>100% figures are all withdrawn** — the last two used the *adjusted* value as denominator, **the same denominator error as the BRA cap, one day later.** **What survives: the reported readings do not establish persistent widening** (adjusted series **+$30.46 → +$41.09 → +$26.33 → +$28.98**), and a mid-August window still sits ~35% above the 8/4 one after excluding 8/16 — **unexplained, with no posting behind it, and asked of BRENT and AEOLUS rather than guessed at.** **Five external review rounds, ~18 claims withdrawn or scoped, and no channel score moved on any of them** — the thesis was never what was in question; my claims about it were. **Next:** §202(c) expiry **9/8**, de-escalation review **9/10**, and the 8/13–8/16 question.


---

## `P1_DEESCALATION_EXECUTION_2026-09-11` — rotated verbatim from STATUS.md at the tenth session (2026-09-11)

**Rotation reason:** STATUS booted at 26,706 B = 82% of the 32,550 B fleet read-cap (rotate-tier per `boot.py` leg 3, NOT a breach) and the session REPLACED the 9/10 ARMED state with the 9/11 EXECUTED state. Blocks below are the superseded 9/10-vintage cells; each carries the surviving live read on STATUS. **Rotation, never deletion.** Source crc32 of STATUS.md before this rotation: 4065611123. Per-block crc32 over the block text as it stood (UTF-8, no terminating newline). Month-assert: every block moved in September 2026 and describes September 2026 content.

| block | STATUS source line(s) | bytes | crc32 |
|---|---|---:|---|
| Block L | 8 | 1,227 | 507681876 |
| Block M | 10 | 984 | 3334080567 |
| Block N | 18 | 1,146 | 1368457711 |
| Block O | 23, 25 | 844 | 872456413 |
| Block P | 31, 32, 33 | 2,704 | 1723543601 |
| Block Q | 62, 67 | 1,531 | 3761809873 |
| Block R | 87, 101 | 439 | 2255061938 |
| Block S | 112 | 1,228 | 2094859047 |

### Block L — declared read-cap residue paragraph, 9/10 vintage (STATUS line 8)

**⚠️ DECLARED RESIDUE (read-cap, 2026-09-10):** this surface measured **95% of the 32,550 B read-cap at boot**; **16,298 B were rotated verbatim to `status_archive/` this session** (Blocks A–K) and every settled 9/6 narrative was compacted, but the surface **still sits above the 75% rotation trigger** because the L249 grade is ~4.5 KB of genuinely LIVE state — **read the current figure from `boot.py` leg 3 / `PROME/tools/measure.py`, never from this sentence.** *(A "~78%" was written here first and was wrong within one edit: **declaring the residue is itself ~800 B**, so the number described a file that no longer existed by the time it was saved. Root rule #4's shape applied to our own prose — a self-describing measurement is stale at the next keystroke.)* **Not trimmed further — "rotation, never deletion; never trim live state to hit the number."** 🔑 **Structural, not a one-session miss: this desk's STATUS has run 95–102% of cap for three consecutive sessions, so every instrument keeps rewarding a smaller file.** The owner's remaining lever is a **hot/cold split**, which is a design change, not a mid-session edit — **flagged to PROME 9/10, needs a decision before the next dense session.**

### Block M — ninth-session lead blockquote, 9/10 vintage (STATUS line 10)

> **Ninth session, 2026-09-10.** **DOCKET L249 GRADED: outcome (d) — a QUIET LAPSE.** DOE §202(c) Order 202-26-41 expired **23:59 ET 2026-09-08 and was NOT extended**; no successor order names PJM; **no EEA-2/EEA-3, no voltage reduction, no load shed** through the lapse. **Limb (c) — whether a large-load direction was ever actually issued under the clause — stays UNKNOWN, not negative** (the para. E utilisation report is the named unchecked document). **A quiet lapse is a real finding, and per NEXUS's pre-registered rule it closes M-09's PJM row as evidence AGAINST the power-constraint leg — NEXUS owns that weighing, not me.** P1's own de-escalation rule: limb ① (order lapsed) ✅ and the HWA is lifted ✅, but **limb ② the 7-clear-day clock completes at 23:59 ET tonight** — so **P1 holds 5 today and the 5→3 is ARMED for the next boot on/after 9/11.** Composite **16/20 unchanged.** *(Full grade → `reports/2026-09-10_DOCKET-L249_202c-lapse-grade.md`.)*

### Block N — CONVERGENCE MATRIX P1 cell, 9/10 vintage (STATUS line 18)

| **P1** | Stress → price | **5 🔴🔴** *(held — final hours of the clock)* | **§202(c) LAPSED QUIET 23:59 9/8 — graded at DOE + PJM primaries 9/10 (DOCKET L249 = outcome (d)).** No extension, no successor PJM order, no EEA-2/3, no voltage reduction, no load shed. **5 is held by the RULE, not by the grid** — limbs ① (order lapsed) and ③ (HWA lifted) are SATISFIED; **limb ② the 7-clear-day clock completes 23:59 tonight.** ⚠️ **I am not taking the last 12 hours** | shares the heat antecedent with P4 — **count the September heat root ONCE** | **[9/10, VERIFIED]** DM2 5-min per-day max, **n=288/day, ZERO intervals ≥$500 on any day**: 9/4 $149.05 · 9/5 $157.68 · 9/6 $87.03 · 9/7 $220.29 · **9/8 $283.51** · **9/9 $457.28** · 9/10-noon $223.88. Demand 112,674 MW = **82.3%** of a 136,896 MW 24h peak. Board: **12 postings, newest 9/9 16:27, all local-relief/informational — zero emergency-class**; **no Hot Weather Alert in effect** | **5→3 ARMED, executes at the first boot on/after 9/11** absent an emergency-class posting or a new §202(c) before 23:59 9/10. An extension or a new order re-arms P1 at 5 |

### Block O — composite note + status paragraph, 9/10 vintage (STATUS lines 23, 25)

**Composite: 16/20** *(P1 5 + P2 5 + P3 4 + P4 2 — **unchanged, and the stillness is again the honest read.** The order lapsed quiet and the grid is benign, yet nothing moves today because P1's clock has ~12 hours left: **front-running a dated rule on a quiet tape is the exact error the rule exists to prevent.** The move is ARMED for 9/11, not withheld.)*
**⚠️ Status 🔴 HELD, and the reason is a dated rule rather than a live reading.** The 8/17-registered band fired on its letter on 9/2; the episode closed 9/3. **5 persists only because the de-escalation clause has not been satisfied yet (9/8 order lapse, 9/10 posting clock)** — not because anything is currently stressed. ⚠️ **Still no deploy-posture change** — a fired gate is not a thesis confirmation and supplies no entry (TERRY Non-Negotiable #15); see `TRADE.md`.

### Block P — P1 live-channel bullet (grade + de-escalation paragraphs), 9/10 vintage (STATUS lines 31, 32, 33)

- **P1 — Stress → price** 🔴🔴 **held at 5 for the final hours of its own clock. The §202(c) order LAPSED QUIET; the 5→3 is ARMED, not yet earned** [DOE + PJM primaries + DM2 tape, all read 2026-09-10].
  **DOCKET L249 GRADE = (d) QUIET LAPSE.** **(a) extension — NO [VERIFIED]:** the order's DOE page states *"in effect beginning on September 1, 2026, and shall expire at 11:59 PM ET on September 8, 2026"* with no amendment posted, and the **DOE 2026 202(c) index** shows **41 is the LAST PJM order of 2026** — successors went elsewhere (**42 = Orlando Utilities**, **43 = Duke Carolinas**). **(b) EEA-2/3, voltage reduction, load shed — NO [VERIFIED]:** board shows **12 postings, newest 9/9 16:27, all local-relief/informational, zero emergency-class**, and the DM2 tape has **ZERO intervals ≥$500 on every day 9/4–9/10** (n=288/day; max **$457.28 @9/9**). **(c) a large-load direction actually issued — UNKNOWN, NOT a negative [SEARCH-NOT-FOUND]:** no para-E utilisation report is published — *authority ✅ · deployment ❓ · utilisation record ❌* stands. ⚠️ **The board is a CURRENT view and cannot prove a historical negative** (#105485 has dropped while OLDER 9/1–9/2 rows persist) — **the tape carries that leg.** 🔑 **The finding: the emergency authority to direct backup generation at large loads — IRAS limb (c)'s policy, granted early — EXPIRED WITHOUT A SINGLE PUBLISHED UTILISATION RECORD. The authorised-vs-observed gap did not close; it expired unmeasured.** ⚠️ **NEXUS owns whether this counts** (M-09 ARMED→COUNTED); WATT grades the event. *Full evidence, per-day table and instrument limits → `reports/2026-09-10_DOCKET-L249_202c-lapse-grade.md`.*
  **DE-ESCALATION RULE, graded limb by limb on its own letter:** ① no §202(c)/EEA/Max-Gen-Alert standing — **SATISFIED** · ③ **HWA lifted — SATISFIED** (PJM board 9/10) · ② **7 clear days from #105485 (EEA-1, 9/3 00:01) — NOT YET COMPLETE:** my registered letter reads *"7 clear days complete **end of 9/10**"* (clear days 9/4…9/10), and at 12:2x ET that day is still running. ⇒ **P1 = 5 today; 5→3 executes at the first boot on/after 2026-09-11**, absent an emergency-class posting or a new §202(c) before 23:59 tonight. ⚠️ **I am not taking the last 12 hours** — both halves of the rule are obligations and a quiet tape is exactly when going early feels harmless. *(⚠️ **The clock has two readings and I only noticed at grade time:** 9/3 00:01 + 7×24h = **9/10 00:01, already complete**, vs the calendar reading = **end of 9/10**. I grade on my own registered letter. **A duration rule that never said clock-vs-calendar is a defect** — **L-51**.)*

### Block Q — EXIT TRIAD P1 row + fired-count line, 9/10 vintage (STATUS lines 62, 67)

| P1 | **As re-specified 8/17, unchanged:** EEA2+ posting **OR** (LMP ≥$1,000 sustained 2+ **consecutive 5-min** intervals **AND** [emergency-class posting live **OR** demand ≥97% of trailing 24h peak]) | **FIRED 9/2; the fire is HISTORICAL.** 9/4–9/10 tape: **0 intervals ≥$500**, let alone ≥$1,000; no emergency-class posting; demand 82.3% of 24h peak. **Current state satisfies NEITHER limb.** 5 is held only by the **separate de-escalation clause**, whose last limb expires 23:59 tonight | **🔴 FIRED (9/2), NOT RE-FIRING.** ⚠️ *fired* is an event, *firing* is a state — **a triad that cannot say which will carry a spent fire forward for months.** Season count 2-of-4; live rail **NOT-FIRED as of 9/10** |
**Fired-count: 2 of 4** *(P1 + P2)*. ⚠️ **P1's is a SPENT fire, not a live one** — the season count stands; the live rail reads **NOT-FIRED as of 9/10**. **Thesis-kill vs channel-kill:** the summer killed P1's live read and September brought it back at 5 — **the channel was not dead, it was out of season**; **L-42 is DISCHARGED by `WATT-11`**. Falsification: a non-heat autumn emergency **OPENS AN INVESTIGATION — it does not establish reserve-margin erosion** (outage-cluster, transmission and fuel-supply explanations eliminated first; `WATT-11` `if_falsified` governs). *Full narrative verbatim → archive § `FIRED_COUNT_CHANNEL_KILL_NARRATIVE_2026-09-06` + Block B.* The thesis dies only if the 29/30 BRA clears well below cap **AND** data-centre queues drain. Neither is in evidence.

### Block R — OPEN row 2 + WAKE row P1 execution, 9/10 vintage (STATUS lines 87, 101)

| 2 | 🔴 **P1 de-escalation — GRADED, ARMED, NOT YET EXECUTED.** Limbs ① (order lapsed) + ③ (HWA lifted) SATISFIED; **limb ② the 7-clear-day clock runs to 23:59 ET 9/10.** ⇒ **5→3 at the first boot on/after 9/11**, absent an emergency-class posting or new §202(c) tonight | **execute 9/11** |
| 🔴 **P1 de-escalation EXECUTION** | **9/11** (first boot on/after) | graded + armed 9/10; only the 7-clear-day clock remained |

### Block S — BOTTOM LINE, 9/10 vintage (STATUS line 112)

**The §202(c) order lapsed quiet.** DOE Order 202-26-41 expired at **23:59 ET 9/8 and nothing replaced it** — no extension, no successor PJM order, and through the whole lapse window **no EEA-2/3, no voltage reduction, no load shed**, on a tape with **zero 5-min intervals ≥$500 on any day 9/4–9/10** (n=288/day; the highest print was **$457.28 on 9/9**). **That is a real finding, not a null:** the emergency authority that let PJM direct backup generation at large loads — the same policy IRAS limb (c) wants written into tariff — **expired without a single published utilisation record.** The gap between *authorised* and *observed* did not close; **it expired unmeasured**, and the one document that could still close it is the paragraph-E utilisation report. **P1 stays 5 today** because its own clock has ~12 hours left, and **front-running a dated rule on a quiet tape is precisely the error the rule exists to prevent** — the 5→3 is **armed for 9/11**, not withheld. **Composite 16/20, unchanged.** ⚠️ **NEXUS owns whether this counts** (M-09 ARMED→COUNTED); I graded the event, NEXUS weighs it. **Next:** execute the de-escalation 9/11, the 8/13–8/16 elevation, and hedged-vs-floating for VULCAN.

### Blocks T–U — second rotation pass, same session (2026-09-11)

| block | STATUS source line(s) | bytes | crc32 |
|---|---|---:|---|
| Block T | 43 | 1,394 | 2799524619 |
| Block U | 75, 76, 77 | 750 | 4284464153 |

### Block T — P2 regulatory layer, the four things paragraph, 9/10 vintage (STATUS lines 43)

**The four things that must not be lost off this surface:** ① **PJM filed Door B ~8/13** (IRAS) — **NOT BANKED**, a filing is not an order. ② 🔑 **limb (c)** writes curtailment priority **into tariff**, converting the §202(c) precedent from an emergency action into a **standing commercial term of service** — ⚠️ **and the precedent itself lapsed quiet 9/8 with no utilisation record, so the tariff case cannot lean on demonstrated use.** ③ ✅ **IRAS = `ER26-3515-000`, PRIMARY-VERIFIED** (FR/GPO govinfo FR-2026-08-18), filed 8/13/26, acc. 20260813-5118, comments closed 9/3, **requested effective 10/12/2026**, ✅ **service availability 1 Jun 2027** [new 9/8, WALTER SIG-013 off the filing]. Companion RBP `ER26-3380-000` (7/31). ⛔ **EL26-67 relationship UNESTABLISHED.** ⚠️ **TWO cost questions, never merged:** *(a)* generation to serve Large Loads → **large loads pay "the full cost"** [PJM primary] = WATT-10's core, **INTACT**; *(b)* **compensation** for interruption + residual RBP → **PJM declined to allocate; left to states/EDCs**, max **50%** of the Non-Performance Charge Rate, loads may **waive**. **(b) is NOT a gutting of (a).** ④ **Door A → CARL/HENRY (~65M ratepayers) · Door B → VULCAN/HENRY (AI-capex opex)**; backstop **$555/MW-day ⇒ $27.21/MWh @85% LF**, basis = arithmetic at **assumed** load factors and **travels with the number**.

### Block U — INSTRUMENT section, the three operative facts, 9/6-9/10 vintage (STATUS lines 75, 76, 77)

⚠️ **DM2 `rt_unverified_fivemin_lmps` retains ~15 days and returns short windows with NO error.** `read_pjm_onpeak_mean` asserts **per-day COVERAGE** — **a count check cannot see a window shorter than the one it labels.** *(Held today: n=288 on every full day 9/4–9/9.)*
⚠️ **The contamination flag is a SINGLE-DAY OUTLIER detector against the window median — NOT a window classifier.** It **fails by construction when the contaminated days are the majority.** **Silence means "no single day dominates," never "this window is clean."**
✅ **`rt_hrl_lmps` retains ≥67 days (to 7/1).** The 5-min horizon is **one feed's**, not the archive's. **When one feed's horizon blocks a question, probe the siblings before recording it closed.**

### Blocks V–X — third rotation pass, same session (2026-09-11)

| block | STATUS source line(s) | bytes | crc32 |
|---|---|---:|---|
| Block V | 54 | 800 | 1751072484 |
| Block W | 45 | 567 | 2527810490 |
| Block X | 37 | 309 | 374078184 |

### Block V — WITHDRAWN do-not-reassert one-liner list, 9/10 vintage (STATUS line 54)

⛔ backup generation was **authorised, not observed** (authority ✅ · deployment ❓ · utilisation record ❌ — **and the authority has now lapsed with the record still ❌**) · ⛔ the 55 GW seam is agreed on the **number**; the "nameplate" wording was **my own** imprecision · ⛔ P2 and P3 are **linked**, not independent roots · ⛔ 28/29 cleared at **100% of its own cap** ("97.5%" was a YoY cap decrease relabelled as utilisation) · ⛔ 9/1 was the **episode's peak**, not a "season high" (July ran 159,046 MW) · ⛔ the spark neither **"widened persistently"** nor **"never moved"** · ⛔ the reconstruction is a **sensitivity analysis** — no floor, INFERRED gas vintage · ⛔ a non-heat autumn emergency **opens an investigation**, it does not establish reserve-margin erosion.

### Block W — season emergency count paragraph, 9/10 vintage (STATUS line 45)

**Season emergency count = 3 episodes, ALL CLOSED:** 7/3 (**EEA2**, set the DOE §202(c) precedent that PJM can curtail ≥50 MW data centers; KB-WATT-034) · 7/15-16 (EEA-1 + Order 202-26-35) · **9/1–9/3 (EEA-1 ×3 + §202(c) 202-26-41 + a dispatched load-mgmt action) — closed 9/3 with no escalation; its order lapsed quiet 9/8.** ⚠️ **All three are heat-clustered. Whether that is the MECHANISM or just the season is exactly what `WATT-11` tests** — and its window does **not** open until **9/15**, so this week is corroboration, **not a resolved leg**.

### Block X — P3 VULCAN-seam sub-line, 9/6-9/10 vintage (STATUS line 37)

  ⛔ **THE VULCAN SEAM IS OPEN ON MEANING** — agreed on the number, divergent on the population; `VULCAN/STATUS.md:27` still reads "55 GW **nameplate** interconnection ceiling" under "SEAM CLOSED". **Correction sent 9/6; application is PENDING — closure is at ITS artifact, not my packet.** → **L-46**.

### Blocks Y–Z — fourth rotation pass, same session (2026-09-11)

| block | STATUS source line(s) | bytes | crc32 |
|---|---|---:|---|
| Block Y | 38 | 829 | 1058925012 |
| Block Z | 69 | 452 | 1661379627 |

### Block Y — P4 live-channel bullet, 9/10 vintage (STATUS line 38)

- **P4 — Gas → power coupling** 🟡 **NOT-FIRED. +$28.26/MWh same-vintage on-peak** (9/4–9/9, n=1,151, HR 7.0, gas $2.805 @9/10) — positive and flat vs the 8/4 baseline (+$29.84). ⛔ **"DE-CONTAMINATED" was an overclaim and is WITHDRAWN** *(the word survived in this headline after the body was corrected on 9/6 — a summary outliving its own correction for a fourth time; fixed 9/10)*. **What stands: the readings do NOT establish persistent widening** — adjusted series **+$30.46 → +$41.09 → +$26.33 → +$28.98**; a mid-Aug window sits ~35% above the 8/4 one even excluding 8/16, **unexplained, no posting behind it**. ⚠️ Basis: RT on-peak LMP ≠ ICE peak OTC. ⚠️ **N5 (i-b): spark stays PROVISIONAL.** *Table + method verbatim → archive § `P4_RECONSTRUCTION_AND_CLOSED_ITEMS_2026-09-10` Block A.*

### Block Z — cleanest bidirectional flip paragraph, 9/6-9/10 vintage (STATUS line 69)

**Cleanest bidirectional flip (BRENT discipline):** the **29/30 BRA clear** (~mid-2027) — at cap again → structural through the decade; materially below cap with queues draining → structural leg falsified. **Near-term flip:** FERC's order on IRAS (**WATT-10**, ~10/12, outer 10/31) — acceptance of the full-cost provision confirms Door B; rejection or a gutted acceptance flips near-term evidence to Door A and *removes* the AI-capex opex drag.


### Blocks AA–AC — fifth rotation pass, same session (2026-09-11)

| block | STATUS source line(s) | bytes | crc32 |
|---|---|---:|---|
| Block AA | 92 | 413 | 3597026841 |
| Block AB | 104 | 376 | 279825274 |
| Block AC | 6 | 414 | 43244531 |

### Block AA — OPEN row 10 (lower-urgency list), 9/10 vintage (STATUS line 92)

| 10 | 🟡 **Lower urgency:** NG=F settlement clock (N5 i-b — spark stays PROVISIONAL) · **KB-WATT-034 metered-vs-DR record-break split (PJM official due "~early Sept" = NOW;** likely home of the "season-high" error — resolve together) · **para. E utilisation report** (the one document that could still convert limb (c) from UNKNOWN) · Oracle/We Energies · Hut8 · TSMC-AZ · EIA-923 heat rate | mixed |

### Block AB — WAKE row, CRWV DSCR conditional, 9/6-9/10 vintage (STATUS line 104)

| ⚠️ **CONDITIONAL, NOT A CATALYST — CRWV DSCR mark absorbs September** | *~Dec 2026 **IF** the load is largely floating* | **Premise UNRESOLVED** ⇒ not a registered dated trigger: the covenant marks *Excess **UNHEDGED*** costs. **Resolve the hedged/floating share FIRST.** *(Registering a date whose premise is open is how a modelled date becomes treated as real.)* |

### Block AC — header 'Superseded content' pointer line, 9/10 vintage (STATUS line 6)

**Superseded content →** `status_archive/STATUS_ARCHIVE_2026-09.md` (Sept rotations; **12,921 B moved 9/2 + 11,927 B moved 9/6 + 7,541 B moved 9/10 + Blocks L–S moved 9/11 (bytes/crc in the archive manifest)**, per-block crc, month-asserted per splice) · `status_archive/STATUS_ARCHIVE_2026-08.md` (**CLOSED** — Aug-17 rotations only) · `archive/SCRATCH_ARCHIVE_2026-07-08.md` (SCRATCH cold half, 56,324 B)

