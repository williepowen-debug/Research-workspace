# FLG STATUS

> 🔴 **FIRST-LIVE-SESSION BANNER — UNSPENT.** This desk was built 2026-08-20 and **has not yet run a session of its own.** Every figure below is **MIRROR-grade**: extracted from REGINALD or recomputed from that extract, never pulled by FLG at a primary. Run `CLAUDE.md § FIRST LIVE SESSION` before treating any read here as this desk's own work, and strike this banner when it is spent.

**Last Updated:** 2026-08-20 16:33 ET — **BUILD SESSION (DAEDALUS, Will-approved in-session).** Agent created off REGINALD's convergence matrix v2.0 (`75f0dd18b`, 16:04 ET the same day), which ranked FLG **🔴 6/6 — 1st of 14 scored banks** after v1 had ranked it **7th of 7, last**, and which REGINALD reported with no thesis file on the name. Build proposal: `AGENTS/DAEDALUS/builds/FLG_BUILD_PROPOSAL_2026-08-20.md`.

**Class:** Market domain — print-driven single-name specialist · **Level:** L1 at birth *(no FLEET_MAP row yet — ROSTER registration is PROME's and lands first, PAT-047)*

---

## 🔴 START HERE — the desk's read changed on build night

**The load-bearing figure on this name is 29% ACL/nonaccrual COVERAGE — not the composite 6/6, and not the 4.88% nonaccrual rate.**

DAEDALUS challenged REGINALD's channel-1 instrument at build (could the SR 07-1 ratio be rising on a shrinking denominator?). REGINALD tested it at the primary the same evening and **REFUTED it** (`fb1f68659`, matrix §3b, verified at artifact): CRE numerator **−32.2%** ($48.33B → $32.76B), capital **flat −2.6%**, ratio **−143pp, falling in all 11 quarters**. **But the answer redirected the desk**, and REGINALD asked explicitly that FLG start from the redirect rather than the composite:

| Channel | Level | Trajectory | Read |
|---|---|---|---|
| CRE concentration | 327.5%, above the 300% line | **−143pp, ~2 quarters from crossing below 300%** | ⬇️ **DE-RISKING — not deterioration** |
| Nonaccrual rate | 4.88%, cohort-worst | **past peak, 5.49% → 4.88%** | ⬇️ improving |
| **ACL / nonaccrual coverage** | **29%, cohort-thinnest** | **87% → 29%, monotonic; ACL$ down 8 of 8 quarters, $1.27B → $0.87B** | 🔴 **THE LIVE SIGNAL** |

**Q2b was then answered the same evening, and the answer is a THIRD case my binary did not have.** REGINALD pulled Schedule RI-B Part II unprompted (`6dfd8ed53`; identity re-derived first-hand here and it **ties to the dollar**): begin $1,029,999K + provision $15,923K − charge-offs $232,410K + recoveries $55,488K = $869,000K.

- ❌ **Not release** — provision is **positive in every quarter**; nothing was reversed into income.
- ❌ **Not clean disposition** — at EGBN the ACL was consumed by disposition *and* the concentration left the balance sheet.
- 🔴 **It is consumption by charge-off with provisioning STOPPED.**

**CO/provision: FY2023 0.3× (building) → FY2024 0.8× → FY2025 2.4× (draining) → 2026 H1 ×2 = 14.6×.** Provisioning **−97.1%** from FY2024 while charge-offs held near half a billion a year ⇒ **runway ≈2.15 years on a TTM basis** *(corrected from ~1.9yr — H1×2 overstated charge-offs ~15%; TTM $403,816K, not $464,820K)*** against a **$2,988M** nonaccrual book.

✅ **BASE-RATED THE SAME EVENING — 168 bank-quarters, and 14.6× IS remarkable.** Cohort median CO/prov **1.00×** (p90 1.63, p95 2.00); **the entire ≥10× tail across all 168 bank-quarters is FLG's own two 2026 quarters — 74.7× [Q1] and 14.6× [Q2], with no other bank reaching 10× in three years.** True releases are 1.2% of quarters (ZION only); FLG never released. **The line stands with a denominator.** ⚠️ `RIAD` is YTD so annualisations are REGINALD's not the company's; 24.4% cohort non-tying makes FLG's 6-of-11 unremarkable **as a rate**, but FLG's **6/12 = 50% tie rate IS an outlier**; 14 filers is not the industry.

🔴 **And the same base rate killed this desk's kill condition.** `CO/prov < 1.0× ×2 quarters` fires on **42.8%** of ordinary bank behaviour — FLG satisfied it for **six consecutive quarters ending eighteen months before the pattern began.** Four replacement forms were base-rated here before proposal and **all four died.** `EXIT_PROTOCOL.md` K-3's kill cell is now **UNSET with a stated requirement** (see Q2e). **An honest gap beats a falsifier that retires theses at random.**

⚠️ **And the "improving nonaccrual" leg is now CONTESTED — REGINALD raised it against its own reading.** You do not charge off $232M in six months without the rate falling; **a rate falling by charge-off is not a rate falling by cure**, and the roll-forward nets so it cannot separate them. That composition read is FLG's (`THESIS.md` Q2c), and `EXIT_PROTOCOL.md` K-3 has **suspended its nonaccrual-rate legs** until it is split — otherwise the kill fires on the bank's own losses.

⚠️ **Instrument lesson, corrected TWICE in one evening:** the desk shipped with the coverage *ratio*; my first fix added **ACL in dollars**; that was still insufficient. **The discriminator is `CO / provision`** — neither the ratio nor the ACL level separates consumed-by-loss from released-into-income. K-3 now grades on CO/provision and is the desk's primary leg.

---

## BUILD-SESSION FINDING — the flow half

🔴 **The deleveraging may already have bottomed, and nobody had noticed.**

Total loans QoQ across the 11 quarters in `workbook/MI3_FLG.tsv` (FFIEC Call Report, RSSD 694904):

`−0.1 · −2.9 · −1.1 · −10.9 · −5.8 · −3.0 · −4.0 · −1.9 · −3.5 · −0.6 · **+0.9**`

**2026-06-30 is the first positive loan quarter in the series**, and the prior four decelerate monotonically toward zero. All eleven `loans_qoq_pct` cells were recomputed against `total_loans_k` at build and reproduce to 2dp (KB-FLG-014 — the desk's only first-hand row).

**Why it matters:** `workbook/EXIT_PROTOCOL.md` leg **K-1 is the thesis-kill**, and it requires **two consecutive** positive quarters. It is **one print from firing**, resolving at the Q3-2026 Call Report **~2026-11-14**. This surfaced on the same afternoon the cohort ranked FLG its worst name.

**What it is NOT:** a refutation of REGINALD's matrix. The matrix measures concentration and credit quality; this measures balance-sheet direction. Both can be true — that tension is the desk's central open question, not a contradiction to resolve by picking a side.

---

## Position

**NO POSITION** (verified 2026-08-20 against `FORGE/STATUS.md`, reconciled 2026-08-14). Surface: `TRADE.md`.

⚠️ Historically traded: **FLG $13P ×3, $45** (`AGENTS/RED/research/POSITION_RECONCILE_2026-06-10.md:37`) — outcome **UNRECORDED, not zero**. Live print **$13.49, −1.46%, 2026-08-20** (`FORGE/tools/market-data/fetch.py`, pulled at build). The old strike is ~ATM. **Never cite that price after today** — pull live (root Critical Rule 4).

**No position may be proposed before the first-live-session protocol is spent.**

---

## Seed state (all MIRROR-grade — re-verify before load-bearing)

| Read | Value | Source | Grade |
|---|---|---|---|
| CRE concentration (SR 07-1; denom = total risk-based capital) | **327.5%** — above the 300% supervisory line, cohort-worst | REGINALD matrix v2.0 ch.1 | MIRROR |
| Nonaccrual rate (nonaccrual / total loans) | **4.88%** — cohort-worst, ~5.5× median | REGINALD matrix v2.0 ch.2 | MIRROR |
| ACL / nonaccrual coverage | **29%** — cohort-thinnest (AMTB 51%, EGBN 88%); monotonic from 87% | REGINALD matrix v2.0 §3b | **PRIMARY (REGINALD-pulled) — NOT FLG-verified** |
| Total assets | $111.17B (2023-09-30) → **$87.71B** (2026-06-30), **−21.1%** | `MI3_FLG.tsv` | MIRROR |
| Total loans | $85.92B → **$61.19B**, **−28.8%** | `MI3_FLG.tsv` | MIRROR |
| MI3 `v1_pct` | 5.28% → **3.65%** | `MI3_FLG.tsv` | MIRROR |

**The two instruments point opposite ways.** Concentration and credit quality read cohort-worst; the balance sheet reads eleven quarters of contraction with a falling MI3. That is `THESIS.md` Q1 and Q2.

---

## Open questions (priority order — full form in `THESIS.md`)

| # | Question | State |
|---|---|---|
| ~~**Q1**~~ | ~~Is the concentration ratio measuring risk, or a shrinking denominator?~~ | ✅ **ANSWERED + REFUTED same evening at the primary** — capital held flat, so the artifact is impossible here. Concentration thresholds UNBLOCKED (base-rate against a *falling* series). The answer redirected the desk to coverage |
| ~~**Q2b**~~ | ~~Taken-and-disposed, or released?~~ | ✅ **ANSWERED 8/20 — NEITHER.** Consumption by charge-off with provisioning stopped (CO/prov 14.6×, **2.15yr** runway TTM). The binary needed a third cell |
| **Q2c** | Is the nonaccrual improvement **cure or charge-off**? | 🔴 **NEW PRIMARY** — REGINALD raised it against its own leg. Decompose the delta into cures/paydowns/charge-offs/OREO. Stage 4 currently reads "improving" on a figure that may be measuring its own charge-offs |
| ~~**Q2d**~~ | ~~Is 14.6× actually unusual?~~ | ✅ **ANSWERED 8/20 — YES, 99.4th percentile** (leave-one-out 1/165 = 0.6%; including-the-observation 2/166 = 1.2% — both framings on file). Cohort median 1.00×; the entire ≥10× tail across 168 bank-quarters is FLG's own two 2026 quarters (74.7× Q1, 14.6× Q2). **The line stands, with a denominator.** ⚠️ **14.6 is a ROUNDED display value — the datum is 14.5959×. Never register a level typed from the printed form of the observation it describes** |
| ~~**Q2e**~~ | ~~What kill condition can this thesis have?~~ | ✅ **ANSWERED 8/20 — NONE, measured.** Runway cuts <0.75/<1.00/<1.25 clear base rate, spurious-fire AND not-breached — **and all fail latency: FLG moves AWAY at ~+0.06yr/qtr, so on trend it never arrives.** K-3 stays UNSET **for a measured reason** |
| **Q2f** | 🔴 **Does this desk still have a bear case?** Three of four instruments now soften it | **OPEN — and it is a SCOPE question, raised to PROME 8/20, not decided here** |
| **Q2** | Has the deleveraging bottomed? | 🔴 **LIVE** — one print from resolution (~2026-11-14) |
| **Q3** | Does the rent-regulation mechanism actually transmit? Stages 1–2 are **entirely un-instrumented** | 🟠 Until instrumented, this desk holds a credit observation, not a causal thesis |

---

## Structural state at build

- **Ledgers live:** `MI3_FLG.tsv` (12 quarters, RSSD 694904, `Verified_By` empty = not FLG-verified) · `KB.tsv` (14 rows: 13 seeded + 1 first-hand) · `TRIGGERS.tsv` (7 rows, all `[EST]`/`RULE`-anchored, **none is a registered gate**) · `PREDICTIONS.tsv` (**empty by design** — a seeded prediction would be the architect's forecast, not this desk's).
- **Kill rail:** `workbook/EXIT_PROTOCOL.md`, stamped `Kill rail re-derived: 2026-08-20`, **PROVISIONAL** (authored against the seed; no thesis exists yet). K-1 flagged one quarter from firing.
- ⚠️ **Known always-red flag, do NOT silence it:** `boot.py` leg 1 reports `MI3_FLG.tsv +52d behind STATUS` and will keep doing so, growing to ~135d, every session between quarterly filings. **Expected by construction** — the data clock is the Call Report's own vintage and bumping it would launder freshness (PAT-044). Design-vs-neglect boundary is the **next-due date (~2026-11-20)**, written in the ledger's own header. Root cause is a registered fleet gap now at **n=2**: STATE_VOCABULARY Class 8 has no SCHEDULED/PERIODIC cadence token (REGINALD hit it the same day on `NDFI_COHORT.tsv` and correctly refused to mis-declare). DAEDALUS owns the token; draft at the ~8/28 wiring sweep.
- **boot.py:** 4 legs — ledger staleness · predictions-due · triggers-due · **quarter-due** (Call Report clock). All four paths watched at build per `CHECK_STANDARD.md` §3: clean rc=0, due rc=1, missing-register rc=2, fixtures restored byte-identical.
- **Registration:** ROSTER + root canon are **PROME/Will-scoped and OPEN** — packet routed 2026-08-20. No `FLEET_MAP` row until ROSTER lands (PAT-047 order; `render_directory.py`'s co-registration guard fails loud on the reverse).
- **Parent seam:** REGINALD owns the cohort view and the matrix row. `VX-REG-6.03` was **RULED DUAL-ACTION 2026-08-20 evening** (REGINALD + FLG): **FLG is ON the action line, does NOT edit the row, and DOES act on a fire.** Baseline **FROZEN not rolling** — bands are absolute **$12.82 / $12.10 / $11.39**. At $13.49 the vector sits −5.3%, **53% of the way to band 1** (plain GREEN under-reported that; REGINALD sharpened the token). Tie-break on any disagreed FLG figure: **the primary**, not either ledger.

---

## Next actions (the first-live-session list, in order)

0. ⚠️ **`inbox/` holds an UNPROCESSED PROME first-boot packet — read it, it is deliberately left for you.** Its §1 (process REGINALD's Q2b answer) has been **pre-integrated by DAEDALUS at build**, and one figure in it is **superseded**: it cites ~1.9yr runway; the corrected TTM figure is **2.15yr** (`20308388d`). §2–§3 are standing orientation and still yours to read.
1. **Re-verify the seed at FFIEC CDR** (RSSD 694904), at minimum the two most recent quarters; stamp `Verified_By`. ⚠️ **The FIRST-LIVE-SESSION banner stays up until YOU pull at the primary** — a peer having pulled is not this desk having pulled (PROME's instruction, and it is right).
2. **Recompute the SR 07-1 ratio yourself**, both definitions written out; report the delta against 327.5% whichever way it falls.
3. ~~Answer Q1~~ ✅ refuted 8/20 · ~~Answer Q2b~~ ✅ answered 8/20 (neither — consumption by charge-off, provisioning stopped). **Now, in order:**
   **3a. Answer Q2c — split the nonaccrual delta into cure vs charge-off.** This is the desk's first analytical job and nobody else can do it: REGINALD explicitly left the composition read here as single-name depth. Stage 4 of the transmission table is currently recorded as improving on a figure that may be measuring its own charge-offs.
   **3b.** ~~Ask REGINALD for the cohort base rate~~ ✅ **DELIVERED 8/20 — 168 bank-quarters. 14.6× is the 99th percentile; the line stands.**
   **3c. Design a kill condition this thesis can actually have (Q2e).** 🔴 **K-3's kill cell is UNSET and must stay unset until a form passes all four tests on the rail** (cohort base rate <~10% · not breached at write time · low spurious-fire history · latency ≤2–3 quarters). The likely instrument is the runway (ACL ÷ annualised charge-offs) or coverage vs nonaccrual — **both blocked today**: the first needs a validated per-quarter charge-off series (`RIAD` is YTD), the second needs Q2c. **REGINALD will base-rate any candidate before it registers — send it there first, do not register on intuition.**
4. **Base-rate the 7 `[EST]` triggers** against the series; retire the ones that do not separate. "Don't build it" is a real answer.
5. **Instrument stage 1 or 2** (RGB series / maturity profile) — without one, Q3 stands unanswered and the seat is unjustified.
6. **Re-derive and re-stamp** `EXIT_PROTOCOL.md`; author `THESIS.md` v1.0 only when its five-point bar is met.
7. **Write back:** STATUS + BOTTOM LINE, PROME packet (gate proposals), REGINALD packet (the step-2 reconciliation).

---

## BOTTOM LINE

**FLG is one day old, four independent primary pulls have hit it, and three of the four softened the case for its own existence.** Concentration is de-risking, not deteriorating. Nonaccruals are past peak — and contested, because a rate falling by charge-off is not a rate falling by cure. Runway bottomed at 1.29yr in Q1-2025 and has lengthened for **eight straight quarters** to 2.15. **What survives is narrow and genuinely unusual: CO/provision at 14.6× is the 99.4th percentile of 168 bank-quarters, and the entire ≥10× tail is this bank's own two 2026 quarters — nobody else in the cohort reaches 10× in three years.** Provisioning is down 97.1%; coverage at 29% is the thinnest in the cohort. **But the two survivors are in tension with each other, and that tension is now the desk's real work:** coverage falls *because* charge-offs consume the reserve, which is the same mechanism lengthening the runway — one mechanism, two opposite readings, and nothing here resolves it. **The desk also has no falsifier, deliberately and for a measured reason:** four kill-forms were base-rated and died, then three runway cuts cleared base-rate, spurious-fire and not-breached — and all failed latency, because FLG moves *away* from every cut at ~+0.06yr/quarter. **The honest structural fact underneath all of it: stages 1–2 of this desk's own transmission chain — the NYC rent-regulation front end that is the only reason it isn't a REGINALD cohort row — still have zero instruments.** Everything found so far came from REGINALD's instruments, not this desk's. That is why a **scope checkpoint is pre-registered at the Q3 Call Report ~2026-11-14** (raised to PROME 8/20, by the builder, before it could be graded charitably later). **Next, in order: (1) read the PROME first-boot packet still in the inbox; (2) split the nonaccrual delta into cure vs charge-off — nobody else can; (3) pull at the FFIEC primary and only then strike the MIRROR-grade banner; (4) instrument stage 1 or 2, or say plainly that it cannot be done.**

