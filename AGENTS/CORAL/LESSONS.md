# LESSONS.md — CORAL Mistake Patterns & Rules

*Read at boot. Learn once, prevent forever. Verified mistakes that burned us — each with a prevention rule. For Will's working preferences and data-source learnings, see `MEMORY.md`. Seeded from REGINALD/OZK LESSONS during CORAL spinout 2026-06-19: shared structural rules copied, FL-specific rules added.*

---

### [Data] — Verify Agent Data Against Primary Filings
**Mistake:** PSEC was reported at 35% PIK across the fleet — actual was 8.6% per SEC filing. Agent-relayed and aggregator numbers propagate as fact.
**Rule:** Before any metric informs a trade or a cross-agent signal, verify against the primary — SEC 10-K/10-Q for banks, FL OIR for insurers, FL Realtors for housing, the Call Report for bank ratios. Agent research and trade-press headlines are a starting point, not ground truth.

### [Data] — Verify Real-Time Prices Before Building Narratives
**Mistake:** A STATUS file stated Brent $118–125 and an entire FL energy-shock cascade was built on it. Actual was ~$81. The error propagated through multiple sections before being caught.
**Rule:** Confirm price/level inputs from a live source before modeling downstream effects. A large error on one input produces garbage on every output.

### [Analysis] — Don't Confuse a Thermometer With the Mechanism (FL condo inventory)
**Mistake pattern:** The "FL condo inventory >9 months = distress" threshold breached in Mar 2026 (9.1mo) then reverted to 8.9mo in April — sales rose, inventory tightened. Treating the single-month breach as confirmation of an accelerating cascade would have been wrong.
**Rule:** Separate the durable *mechanism* (SIRS reserve gap, assessment cascade, receivership pipeline — structural) from the monthly *thermometer* (inventory months, DOM — noisy, mean-reverting). State which one moved. A one-month threshold tag is not a trend.

### [Analysis] — A Falling Early-Delinquency Bucket Can Be Up-Migration, Not Cooling
**Mistake pattern (caught in self-steelman, 2026-06-25):** I read SBCF's 30-89d past-due −14% QoQ as "cooling / benign" and led with it — while the *same* print showed nonaccrual +32% QoQ ($72→95M) and the 60-89 sub-bucket up ~10×. By the OCC bucket-migration model (loans migrate UP: 30-89 → 90+ → nonaccrual), a *falling* early bucket with a *rising* late bucket is the cascade **steepening** (loans rolling forward), not curing. Leading with the early-bucket headline inverts the signal.
**Rule:** Never grade a delinquency trend off one bucket. Read the **whole aging ladder QoQ** (30-59 / 60-89 / 90+ / nonaccrual) together. A falling early bucket is only "cooling" if the later buckets are ALSO flat/down; if nonaccrual or 60-89 is rising, it's up-migration — flag it as the cascade advancing. The sharpest fresh-quarter signal usually sits in nonaccrual, not the headline 30-89.

### [Analysis] — FL Stress Is Timing-Delayed, Not Absent
**Mistake pattern:** Framing the FL cascade as acute/imminent when the transmission is slow. The snowbird-$ hole and assessment-default wave land on a winter-2026-27 timeline, not Q2-Q3 2026.
**Rule:** Date the *expected landing* of each FL channel explicitly. Don't upgrade to acute on a structural-but-slow signal. "Real but delayed" is the honest call.

### [Process] — Reconcile the FL Read With MARCO Before Publishing
**Mistake risk:** CORAL and MARCO both cover FL condo inventory, airports, and migration. Divergent numbers across two agents on the same geography is data fiction.
**Rule:** Before publishing an FL housing/airport/migration figure, cross-read `../MARCO/STATUS.md`. MARCO owns the population-driven read; reference it rather than maintaining a drift-prone parallel copy. Flag genuine disagreements to REGINALD, don't paper over them.

### [Process] — Date Your Data
**Rule:** Every metric carries a date and a source tag. "FL #2 foreclosure" or "Citizens ~$678B" means nothing without the as-of date. FL housing and insurance data go stale within a month.

### [Process] — STATUS.md Is a Dashboard, Not a Research Report
**Rule:** STATUS.md is current state — signal status, thresholds, FL bank exposure. Research detail belongs in `sources/`, `research/`, or `workbook/`. Keep STATUS under 250 lines.

### [Analysis] — A Stock/Flow Ratio Needs FOUR Legs, Not Two: Level · Volume · Price REALIZATION · Velocity
**Mistake (2026-08-23, mine; the rule it corrects was HOMER's, written the same session):** I read FL condo months-supply falling **9.6 → 7.8** alongside sales **+11.0%** and a flat median, and asserted *"the market is CLEARING BY CUTTING PRICE"* across four surfaces. HOMER — who had just handed me the rule *"name the legs that could invert a stock/flow ratio, and for a supply ratio those legs are PRICE and VOLUME"* — **accepted it in full and republished it.**

**Both of us were wrong, and the legs that actually inverted it were neither price level nor volume.** The same primary carried them: **median pct. of ORIGINAL list received 93.0% vs 92.1%** (sellers getting *more* of their ask, not less) and **median time to contract 68 → 76 days.**

**Rule — for any stock/flow ratio in a transaction market, the leg set is FOUR:**
> **price LEVEL · VOLUME · price REALIZATION (pct-of-original-list) · VELOCITY (time-to-contract / time-to-sale).**
> **Level and volume ALONE cannot separate *"cut until it cleared"* from *"held the ask and waited."* Both produce a falling months-supply.**

**What survives:** absorption was real and is still stated (sales +11.0%, dollar volume +14.0%, inventory −12.9%). **Only the MECHANISM was withdrawn.** Distinguish the two when retracting — killing the observation along with the inference throws away good data.

### [Process] — I Verified the FIGURE and Not the CAUSAL STORY Riding On It — and a Second Witness Made It Worse
**Mistake (2026-08-23, the process half of the above, and the more general failure):** every *number* in that claim was pulled from the primary and correctly sourced. **The mechanism bolted to them — "by cutting price" — got no verification at all.** A figure arrives with provenance I know how to check; **a mechanism arrives as prose and reads as judgement rather than as a claim carrying its own evidentiary burden.**

⚠️ **And the cross-check failed in the way cross-checks fail:** HOMER and I **held the same primary**, neither of us read the realization legs on first pass, and HOMER's agreement then raised my confidence. **Shared source is not shared verification — it is a shared blind spot with two witnesses, and the second witness makes the first MORE confident, not less.** This is a live hazard in the CORAL↔HOMER and CORAL↔MARCO reconciles specifically, because both are *designed* as two-agent cross-checks on the same FL data.

**Rules:**
- **Apply the same rigor to the causal clause as to the number.** Write the mechanism as a testable claim and ask what would refute it — see the non-discriminating-test rule below.
- **Agreement from an agent reading the SAME source is corroboration of nothing.** Before treating a peer's assent as confirmation, ask: *did they check an INDEPENDENT instrument, or did they read my instrument and agree with my prose?*
- **When a peer accepts your framing wholesale, that is the moment to re-read the source, not to bank it.**

### [Data] — Name the Missing Comparator Instead of Reaching for the Available One
**Near-miss (2026-08-23, caught by HOMER before it was drawn):** the July primary gave me **FL CONDO cash share 51.0%**. My CALENDAR already carried **NAR's national all-cash share 26%** as a baseline anchor for the same forward read. **51 vs 26 invites an enormous "Florida is twice the national cash market" differential — and it is not a Florida finding at all**, because 26% is **all-homes** and condos run cash-heavier than single-family *everywhere*.
**Rule:** when two figures are adjacent, in-scope and tempting, **verify the PERIMETER matches before differencing** — and where the correct comparator does not exist, **record it as MISSING on the surface rather than substituting the available one.** Both rows now name the trap explicitly so a later reader cannot walk into it.
**Related:** *A Scope Label Is a Claim Too* (below) is the same failure at the labelling stage; this one happens at the comparison stage, where the labels are each individually correct.

### [Process] — A Fresh Body Can Leave a Headline It Just Falsified (the inverse of the stale-header trap)
**Mistake (2026-08-23, caught by PROME on read-back within the hour):** in ONE commit I added the Will-ruled MSI stand-down condition as a new `OPEN QUESTIONS §A` — and left the §5 block headline reading *"…AND THE LEG HAS NO REGISTERED STAND-DOWN"*, plus the same claim in the `Last Updated` header and a pillar row. **Three summary surfaces asserting the gap, in the same file as the body that closed it.**

**Why it is worse than a typo:** the fleet's known failure is a **stale header certifying a fresh body**. This is the **inverse** — a fresh body leaving a stale headline standing — and it is nastier, because **a reader skimming headlines is doing exactly what headlines are for, and the correction is invisible to precisely that reading pattern.** It is also the same shape one level up as the scope-label rule: *the summary carried a claim the detail had already superseded.*

**Rule:** when an edit changes a STATE (gap→ruled, open→closed, pending→graded), **grep the whole file for the OLD state's phrasing before committing** — headline, `Last Updated` line, dashboard/pillar rows, and any cross-agent brief. The body is the edit you're thinking about; the summaries are the ones that travel. Sweep by **phrase**, not by memory of what you touched.
⚠️ **And do not fix only the instance you were told about: PROME reported ONE, the phrase-sweep found THREE.** Fixing the reported line and stopping is its own version of the same failure — the reporter saw the surface they happened to read, not the set.
**Companion (the clause the rule fails without):** distinguish **live-tense** from **historical** instances — SCRATCH/MEMORY/KB records that say *"the leg HAD no falsifier, and it was ruled"* are correct and must NOT be swept. Only present-tense assertions of the superseded state are defects. **A sweep that overruns erases the evidence that the gap ever existed**, which is the part worth keeping.
**Fleet copy:** propagated 2026-08-23 to `finding_header_edit_is_the_edit_most_mistaken_for_maintenance` as its inverse (PROME, credited). **That is the canonical fleet form — this entry is the desk-local instance record; if the two ever disagree, the fleet memory governs the rule and this holds the worked example.**

### [Analysis] — A Test Whose Statistic Moves the Same Way Under the Rival Hypothesis Is Not Evidence
**Mistake (self-caught late, HOMER-caught first, n=2 in one session — 2026-08-23):** I claimed that Florida's rising blended median *confirms* the Coral Bleaching mechanism, on the reading that the vintage, assessment-hit low end has **stopped clearing**. My proposed evidence was the low end's **SHARE** of transactions falling.

**Why that was not evidence, and the shape is the point:** a **low-end freeze** raises the median. A **high-end surge** *also* raises the median — and it cuts the low end's share **with zero low-end units lost**. So the share statistic moves the same way under my hypothesis and under its rival. **I would have "confirmed" my thesis whether or not it was true.** And every figure I actually had ($1M+ sales +29.5%, Miami-Dade +29.14%, Sarasota >$1M +38.4%) was the **rival** mechanism; I had inherited HOMER's surge evidence and attached my own mechanism to it.

**The primary settled it against me** (FL Realtors July condo summary): **average sale price +2.7% against a flat median** = a fattening right tail, i.e. the surge observed directly; **sales +11.0% and cash sales +14.9%** = not a frozen low end; and decisively, **a genuine freeze would have pushed the median UP and it did not move at all.**

**Rule — one line, run it before adopting any favourable reading:**
> **Name the rival mechanism, then ask whether it moves your statistic in the SAME DIRECTION. If yes, the statistic is not evidence — find one that separates them.**

**Corollaries, each earned the same day:**
- **The discriminator is almost always UNIT VOLUME, not SHARE.** Shares move when *either* end of a distribution moves; counts don't.
- ⚠️ **You will preferentially reach for the non-discriminating test precisely when it favours you.** This is not bad luck; it is the selection effect. **The second instance the same session:** on the Miami for-sale/rental divergence I found one confound that biased *against* my reading, concluded "survives its own confound," **and stopped looking** — missing a second confound (submarket supply composition) that would have made the observation discriminate nothing. **A confound that cuts your way gets audited; one that cuts the other way doesn't get looked for.**
- **Enumerate confounds by SIGN, not by count, and never stop at the first one that flatters you.**
- **This is the same shape as a fired signal with no falsifier** (my 🔴 MSI leg, found the same session): *a condition that cannot come back against you is not a condition.* Whether it's a trading rail or an analytical claim, the test is identical — **can this observation come back negative?**

**Related:** the sibling failure below (*A Scope Label Is a Claim Too*) is the measurement-side version — a wrong label survives every magnitude check. This is the inference-side version: a wrong *test* survives every honesty check, because you did run it and it did come back positive.

### [Data] — A Scope Label Is a Claim Too: Verify Personal-vs-Total Before It Becomes Canon
**Mistake (caught 2026-07-21):** CORAL carried "Citizens 294,253 **personal-lines** policies (May 15)" as a dashboard canonical for ~5 weeks. The number was real but the LABEL was wrong — Citizens' own policies-in-force reports show it was a mid-May **TOTAL** (true Apr-30 personal was 289,824). The mislabel then manufactured a phantom cross-agent divergence with AEOLUS (whose ~395K was simply a stale Jan-31 total), which cost an open reconcile item across three sessions — chasing a scope difference that didn't exist.
**Rule:** when adopting any count/level from press, verify the SCOPE dimension (personal vs total, capped vs uncapped, SA vs NSA, monthly vs cumulative window) against the primary before writing the label into a dashboard row. A wrong label is worse than a wrong number: the magnitude looks plausible, so it survives sanity checks while corrupting every downstream comparison. Most treacherous exactly when scopes nearly coincide (Citizens is ~98% personal, so total ≈ personal and nothing looked off).

### [Data] — In Season, Pull the Full NHC Advisory, Not the Outlook
**Mistake pattern (near-miss 2026-07-21):** a research pull based on the NHC Tropical Weather Outlook (MIATWOAT) carried TS Bertha as "45 kt, S of Panama City" with no track — reading it alone would have left the FL-landfall trigger question open. The full public advisory (MIATCPAT2) showed 60 mph, moving W AWAY from FL toward MS/LA, weakening — trigger question closed in one fetch.
**Rule:** any time a named storm exists, the advisory (position/intensity/track/watches) is the load-bearing document; the outlook is only a formation-odds product. Verify trigger-adjacent storm claims against the advisory before writing dispositions.

---

*Last reviewed: **2026-08-23** (added the non-discriminating-test rule — n=2 in one session, both caught by HOMER; sits beside the scope-label rule as its inference-side twin). Prior: 2026-07-21 (scope-label + NHC-advisory rules). Seeded 2026-06-19 during spinout from REGINALD/OZK LESSONS.*
