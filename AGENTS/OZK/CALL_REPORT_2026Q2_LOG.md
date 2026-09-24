# Q2-2026 FFIEC Call Report — LOG-ONLY pull, first-ever OZK series

**Date:** 2026-08-07 · **Session:** OZK #? (PROME-directed spawn; docketed sitting 8/10-8/21 pulled forward + OZK's own pre-registered `CALENDAR.md` "~Aug 1-10" Q2 Call Report window).
**Instrument:** FFIEC CDR Public Web Service, **REST + JWT**, `RetrieveFacsimile` / SDF. Recipe from the DAEDALUS→WAL packet, commit `f32f2fb8a`.
**Entity:** **ID_RSSD 107244 — BANK OZK, Little Rock AR, FDIC cert 110, filer type 041.** *Verified at the FFIEC primary this session (`RetrievePanelOfReporters`, reportingPeriodEndDate 6/30/2026) — not assumed. `HasFiledForReportingPeriod: true`.*
**Series data:** `workbook/CALL_REPORT_SERIES.tsv` (18 quarters machine-readable: 12 PRIMARY + 6 BASELINE_CHECK).

> ## ⛔ SCOPE — pre-registered, and honored exactly
> **`CALENDAR.md` AUGUST row:** *"~Aug 1-10 · Q2 Call Report (FFIEC, REPDTE 20260630) · Log-only vs supplement basis (Z6 — never re-grades); CRE-specific NCO (OZK-01 archive note); past-due/NCO basis fork check · **Documentation, no grade moves.**"*
>
> **Nothing in this document re-graded a prediction, moved a threshold, moved a scenario weight, or touched a probability.** `PREDICTIONS.tsv` is unchanged by this session. OZK-09 (45%, Will-approved 7/23) is untouched. The Option-2 recognition-window ruling (FROZEN 7/23) is untouched. Everything with a thesis consequence below is written as a **PROPOSAL to Will via PROME**, marked ⚠️ PROPOSAL, and is **not applied**.
>
> Two findings below are dramatic. The pre-registration is what makes them trustworthy — so the scope holds regardless.

---

## 1. THE PULL — provenance

| Step | Result |
|---|---|
| `RetrieveReportingPeriods` (`dataSeries: Call`) | 200 — periods through **6/30/2026** available |
| `RetrievePanelOfReporters` (6/30/2026) | 200, **4,298 reporters** — OZK found by FDIC cert 110 → **ID_RSSD 107244** |
| `RetrieveFacsimile` × 12 quarters, 9/30/2023 → 6/30/2026 | all **200**, 1,737-1,937 MDRM rows each |
| `RetrieveFacsimile` × 6 extra, 3/31/2022 → 6/30/2023 | all **200** — baseline-check only (§3) |

**Entity confirmation, two independent ties:**
1. `RCON2170` total assets **$41,703,134K** at 6/30/2026 — Bank OZK scale, and the ratio denominator that reproduces OZK's own reported NPA% (below).
2. **Four recorded OZK figures reproduce from the primary to the dollar or to the basis point** — see §2. A wrong entity does not reproduce four independent anchors.

**Live gotchas (both already in fleet memory; confirmed again here):** the header is literally **`Authentication:`**, not `Authorization:`. `dataSeries: Call` is a **header**, not a query parameter (a query-string form returns `500 / "Error Code 5001: Invalid or missing Data Series"`). The SDF payload arrives as a **JSON string containing base64**, decoding to `Call Date;Bank RSSD;MDRM #;Value;Last Update;Short Definition;Call Schedule;Line Number` — it is not plain text on the wire.

---

## 2. ★ BASELINE CHECK FIRST — what reproduces, before anything is claimed

Run before any new number was believed (the WAL lesson from this morning: if the baseline does not reproduce, the correct output is a basis dispute, not a verdict).

| Recorded figure | Source of record | Computed from primary | Verdict |
|---|---|---|---|
| Q1-26 past-due **$487.5M / 1.48%** [Call Report] | `STATUS.md`, `THESIS.md` §1 | `RCON1406`+`1407`+`1403` = **$487,522K**, ÷`RCON2122` = **1.48%** | ✅ **EXACT** |
| Q1-26 nonaccrual **$296.6M** | `STATUS.md` | `RCON1403` = **$296,575K** | ✅ **EXACT** |
| Q1-26 OREO **$149.6M** | `STATUS.md` | `RCON2150` = **$149,570K** | ✅ **EXACT** |
| Q1-26 NPA **$446.1M / 1.07%** | `STATUS.md` | $296,575K + $149,570K = **$446,145K**; ÷`RCON2170` = **1.07%** | ✅ **EXACT** — and this pins the ratio basis: **OZK reports NPA over TOTAL ASSETS, not loans** |
| Q2-26 NCO **$56.3M / 0.69% ann.** | `STATUS.md` [Mgmt Comments] | YTD-differenced `RIAD4635−4605` = **$56,254K**; ann. on RC-K avg loans = **0.69%** | ✅ **EXACT** |
| Q1-26 NCO **0.56% ann.** [Call Report] | `STATUS.md`, `THESIS.md` §2 | **0.56%** on RC-K **average** loans (`RCON3360`) · **0.55%** on period-end loans | ✅ reproduces — **basis-dependent, see ⚠️ below** |
| **MI3 = 37.6%**, "worst in the REGINALD screen", ML-REG baseline | `AGENTS/OZK/CLAUDE.md:16`, `LESSONS.md:18-19`, `STATUS.md`, `THESIS.md` *(⚠️ **corrected 8/7 post-delivery** — I first wrote "root `CLAUDE.md`"; PROME grep-verified the quote lives in the **agent-local** CLAUDE.md. Root has **zero** hits for "37.6".)* | **does not reproduce at any of 18 quarters on either documented basis** | ❌ **FAILS — §3** |

> ⚠️ **A load-bearing 1bp, logged not acted on.** `THESIS.md` kill-criterion §2 reads *"Q1 26 NCO came in at 0.56% annualized [Call Report] — **1bp above** the ≤55bps kill line."* On the **average-loans** basis (`RCON3360`, the standard regulatory basis) that is right: **0.56%**. On **period-end** loans (`RCON2122`) it is **0.55%** — i.e. **exactly AT the line, not above it.** The recorded figure is defensible and is the better basis; but the "1bp above" framing is basis-dependent and should say which basis it is on. **Q2's 0.69% is 0.69% on both bases**, so OZK-05's TRUE grade is robust to the choice and **nothing here re-opens it (Z6).** Documentation only.

---

## 3. 🔴 FINDING 1 — the 37.6% MI3 baseline does not reproduce, and the live ratio is **9.35%**

**The claim under test.** `LESSONS.md:18-19` records the recipe and the result: *"Pull FFIEC Call Report Schedule RC-C Part I. Item 4 = C&I loans. Memo Item 3 (RCON2746) = 'Loans to finance CRE not secured by RE.' **Ratio = Memo3/Item4. Flag if >20%.** Key finding: **OZK worst in screen at 37.6%.**"* The figure propagates as a **live property of OZK** into `AGENTS/OZK/CLAUDE.md:16` ("37.6% Memo Item 3 ratio (hidden CRE via C&I classification) — worst in the REGINALD screen. ML-REG baseline") and its §DOMAIN SCOPE ("37.6% MI3 (hidden CRE) baseline and trajectory"), plus `STATUS.md` and `THESIS.md`. ⚠️ **Correction, 8/7 post-delivery:** this document first said the line was in **root `CLAUDE.md`**. It is not — root has **zero** occurrences of "37.6"; both quotes are from the **agent-local** `AGENTS/OZK/CLAUDE.md`, which auto-loads alongside root and which I conflated with it. PROME caught it by grep before routing. **This narrows the blast radius from a Will-gated fleet doc to OZK-local surfaces plus REGINALD's screen — it lowers P-OZK-2's urgency, and it does not touch the primary finding.**

**The series, on the recipe's own basis** (`RCON2746 ÷ RCON1766`):

| Quarter | RCON2746 $K | item-4 C&I $K | **MI3 ÷ item 4** | MI3 ÷ (item 4 + item 9) |
|---|---:|---:|---:|---:|
| 2022-03-31 | 1,298,286 | 440,203 | **294.93%** | 67.00% |
| 2022-12-31 | 1,479,154 | 902,321 | 163.93% | 56.70% |
| 2023-06-30 | 1,364,503 | 1,268,787 | 107.54% | 43.29% |
| 2023-09-30 | 1,097,944 | 1,257,018 | 87.35% | 35.26% |
| 2023-12-31 | 1,241,457 | 1,269,610 | 97.78% | 38.40% |
| 2024-06-30 | 1,229,202 | 1,499,489 | 81.97% | 33.91% |
| 2024-12-31 | 1,055,957 | 1,728,801 | 61.08% | 26.24% |
| 2025-06-30 | 1,202,101 | 2,330,142 | 51.59% | 21.83% |
| 2025-09-30 | 769,920 | 2,870,535 | 26.82% | 14.07% |
| 2025-12-31 | 721,546 | 3,431,585 | 21.03% | 11.66% |
| **2026-03-31** | **489,284** | **3,818,846** | **12.81%** | **7.10%** |
| **2026-06-30** | **430,277** | **4,603,672** | **9.35%** | **5.46%** |

*(full 18 rows → `workbook/CALL_REPORT_SERIES.tsv`)*

**What this establishes:**

1. **37.6% never occurs.** On the recipe basis the series runs **294.93% → 9.35%** and steps straight over 37.6% between 2025-06-30 (51.59%) and 2025-09-30 (26.82%). On the fuller basis it runs 67.00% → 5.46% and steps over 37.6% between 2023-06-30 (43.29%) and 2023-09-30 (35.26%). **No quarter in 18 lands on 37.6% on either basis.** *(The six 2022→mid-2023 quarters were pulled **solely** for this check — a "does not reproduce" claim over 12 quarters is weaker than over 18.)*
2. **The error is not "stale by a bit" — it is wrong in both directions at different times.** Through 2024 the recipe basis put OZK **60-295%**, i.e. far *worse* than 37.6%. Today it is **9.35%**, i.e. far *better* — and **below the screen's own >20% flag threshold**, on the frozen recipe, for two consecutive quarters.
3. **The numerator is genuinely shrinking, not just being diluted.** RCON2746 has fallen **$1,202,101K (Q2-25) → $430,277K (Q2-26): −$771.8M / −64.2% in four quarters.** Denominator growth is also real (C&I $440M → $4,604M over the 18 quarters, ~10×), but the numerator decline is the substantive half.

### ⚠️ P-OZK-1 (PROPOSAL, not applied) — the item-4 denominator is not merely conservative for OZK, it is a category mismatch

WAL's **P8** this morning flagged that RCON2746's own FFIEC definition places its balance in RC-C items **4 *and* 9**, while the spec divides by item 4 only — for WAL, an over-statement. **For OZK it is worse than that.** From the RC-C Memo-10 breakdown (available from 2025-03-31, when the line was introduced):

| Quarter | `RCONPV09` — item 9.a "**Other** loans to nondepository financial institutions" | `RCON2746` — Memo 3 |
|---|---:|---:|
| 2025-03-31 | 1,133,405 | 1,133,405 |
| 2025-06-30 | 1,202,101 | 1,202,101 |
| 2025-09-30 | 769,920 | 769,920 |
| 2025-12-31 | 721,546 | 721,546 |
| 2026-03-31 | 489,285 | 489,284 |
| 2026-06-30 | 430,277 | 430,277 |

**Six consecutive quarters agreeing to the dollar** (Q1-26 differs by $1K — a rounding tell that argues *for* a real identity, not an artifact). The inference: **OZK's entire Memo-3 "hidden CRE" balance is classified in RC-C item 9.a, not in item 4.** Dividing it by item-4 C&I therefore divides a number by a base that contains ~none of it — the ratio's movement is dominated by unrelated C&I growth.

**Proposal:** re-base OZK's MI3 to `RCON2746 ÷ (item 4 + item 9)` with a re-derived flag level, **or** keep item 4 and state on the metric that it is a deliberately non-overlapping (and for OZK, structurally misleading) basis. **⚠️ Re-basing changes the LEVEL, not the direction — both bases fall by ~⅔ over the last four quarters and both are far below anything the "worst in screen" language implies.** Not applied. Cross-route: this is the same defect class as WAL's P8, so the *screen* (REGINALD's ML-REG cohort) likely needs the same repair — **REGINALD's call, not ours.**

### ⚠️ P-OZK-2 (PROPOSAL, not applied) — the "37.6% / worst in screen / ML-REG baseline" line needs a disposition

It is currently asserted as live in **four OZK-local surfaces** (`AGENTS/OZK/CLAUDE.md:16` + its §DOMAIN SCOPE, `LESSONS.md`, `STATUS.md`, `THESIS.md`). I have **not edited any of them** — they state a **cross-agent screen result that REGINALD owns**, and two agents correcting one figure separately is how the fleet ends up carrying two. *(⚠️ Corrected 8/7: this paragraph originally claimed root `CLAUDE.md` was among them and leaned on its Will-gated status as the reason for restraint. Root is **not** among them — but the REGINALD-ownership reason stands on its own and is the real one.)* **Ask:** PROME routes to REGINALD for the screen's own re-run; OZK's local copies get corrected once the screen basis is settled, so the fleet lands on **one** figure rather than two.

**What this does NOT settle:** MI3 measures *hidden* CRE — CRE-purpose lending **not secured by real estate**. **The RESG book, the IQHQ/RaDD credit, the classified balance and the 11 tracked problem credits are all in the SECURED book and are untouched by this result.** ⚠️ **Do not read "MI3 collapsed" as "the CRE concentration thesis weakened."** §4 and §5 point the other way.

---

## 4. Past-due / NCO basis fork — extended to Q2 ✅ (pre-registered item ③)

The Q1 fork was **1.48% Call Report vs 1.41% 10-Q/supplement**. It persists at almost exactly the same size.

| | Q1-2026 | Q2-2026 |
|---|---|---|
| **Call Report basis** (`RCON1406`+`1407`+`1403` ÷ `RCON2122`) | **$487,522K / 1.48%** | **$323,689K / 0.99%** |
| **Supplement / 8-K basis** (recorded in `STATUS.md`) | $465M / 1.41% | $298M / 0.92% |
| **Fork** | **+$22.5M / +7bps** | **+$25.7M / +7bps** |

**The fork is stable in sign and size across both quarters (+7bps both times).** Treat it as a definitional constant, not noise: the Call Report basis runs ~7bps hotter because it sweeps all three RC-N columns including nonaccrual. **Both bases still cross the same thresholds in the same direction**, which is why this is documentation and not a re-grade — OZK-06's FALSE (≤$550M **and** <2.00%) holds on either basis with wide margin.

**NCO fork:** none material. Q2 = **0.69%** on both period-end and average-loans bases; Q1 = 0.56% avg / 0.55% period-end (§2 ⚠️).

---

## 5. 🔴 FINDING 2 — CRE-specific NCO ✅ (pre-registered item ②, the OZK-01 archive note), and a **first-ever** debt-on-debt charge-off print

**CRE-specific NCO**, on RC-C RE-secured CRE categories (1a1 construction 1-4, 1a2 other construction/land, 1d multifamily, 1e1 owner-occ NFNR, 1e2 other NFNR), quarter-standalone, annualized on the same five balances:

| Quarter | CRE NCO $K | CRE loan base $K | **CRE NCO ann.** | Bank-wide NCO ann. |
|---|---:|---:|---:|---:|
| 2025-03-31 | 13,458 | 21,071,341 | 0.26% | 0.25% |
| 2025-06-30 | 4,187 | 21,620,936 | 0.08% | 0.10% |
| 2025-09-30 | 29,135 | 21,194,177 | 0.55% | 0.42% |
| **2025-12-31** | **92,821** | 19,875,925 | **1.87%** | 1.19% |
| 2026-03-31 | 11,625 | 19,701,130 | 0.24% | 0.56% |
| **2026-06-30** | **35,543** | 18,141,162 | **0.78%** | 0.69% |

**H1-2026 CRE NCO = $47,168K, annualized 0.50%** on the H1 average base — **nowhere near the >5% in OZK-01's wording**, consistent with OZK-01's FALSE grade (7/21). *This is the archive-note documentation the CALENDAR row asked for; it changes nothing about the resolved grade (Z6).* The CRE base itself is shrinking — **$21.6B (Q2-25) → $18.1B (Q2-26), −16%** — consistent with the RESG-runoff picture.

### ★ The genuinely new datum: `RIAD5409` prints for the first time in 18 quarters

RI-B Part I **Memo 1** = *"charge-offs on loans to finance commercial real estate, construction, and land development activities **not secured by real estate**"* — i.e. **charge-offs on the Memo-3 / debt-on-debt book itself.**

| Quarter | `RIAD5409` YTD $K | RI-B item 7 "All other loans" charge-offs, YTD $K |
|---|---:|---:|
| every quarter 2022-03-31 → 2025-12-31 (16 qtrs) | **0** | 992 – 4,015 |
| 2026-03-31 | **0** | **28,485** |
| **2026-06-30** | **42,437** | **43,812** |

Two things at once:
1. **The "All other loans" charge-off line broke regime.** It ran at a **$1-4M annual** rate for sixteen quarters, then printed **$43,812K in H1-2026 alone** — an order-of-magnitude break.
2. **The Q2 filing attributes $42,437K of it — 97% — to CRE-purpose lending not secured by real estate.** That is the **debt-on-debt / note-assignment book charging off**, said by OZK on a standardized regulatory schedule.

**Tie to the 10-Q, dollar-level:** `STATUS.md:11` records a **"~$490M RESG 'debt-on-debt'/note-assignment book"** derived from the Q1'26 10-Q "Other" Call category. `RCON2746` at **3/31/2026 = $489,284K.** These are the **same book**, seen through two independently-prepared regulatory filings. It fell to **$430,277K at 6/30/2026: −$59.0M / −12.1% QoQ** — and $42.4M of charge-offs is most of that decline.

⚠️ **Reporting caveat, stated rather than improvised around.** `RIAD5409` reads **0 at Q1-2026** in a quarter whose 10-Q describes **"The Jack" charged off $27.7M** — a debt-on-debt credit — while RI-B item 7 that quarter shows **$28,485K**. The Q2 YTD memo ($42,437K) ≈ the Q1 item-7 amount plus most of Q2's. Best reading: **the Q1 Memo-1 attribution was omitted and is effectively captured in the Q2 YTD figure.** Consequence: **the YTD figure is trustworthy; a Q1-vs-Q2 standalone split of Memo 1 is not.** `CALL_REPORT_SERIES.tsv` therefore carries `RIAD5409` **YTD only, un-differenced**, and this document quotes no standalone quarter for it.

### ⚠️ P-OZK-3 (ROUTE, not a grade) — BROCK's flip condition (a)

The 7/20 PROME provision-attribution packet (processed this session) records BROCK's pre-registered debt-on-debt flip set: *"(a) a 2nd debt-on-debt name to NA/CO; (b) a reserve BUILD against this book; (c) Claros/Affinius/SqMile counterparty-stress commentary — absent all three = idiosyncratic, DORMANT-watch."* **STATUS records those flips as NOT fired, re-confirmed on the 7/22 call.**

$42,437K of YTD Memo-1 charge-offs against a book whose H1 total charge-off history was ~$2M/yr is a **named-schedule datum bearing directly on (a)** — but **the Call Report does not name credits**, so it cannot by itself establish a *second name*. Per the 7/20 packet's own hygiene rule, the correct handling is to route it as **UNATTRIBUTED at the credit level** rather than declare (a) fired. **I have not graded BROCK's condition — that is BROCK's to grade.** Outbox signal written; PROME routes.

---

## 6. ⚖️ THESIS kill-criterion §1 — ADJUDICATED (DAEDALUS 7/22 sweep item 2)

**The criterion** (`THESIS.md` §WHAT WOULD INVALIDATE THIS THESIS, item 1): *"**Past-due regime reverses.** If Q2 26 past-due stabilizes or declines (<$400M vs Q1 26's $487.5M / 1.48% [Call Report…]), the migration-velocity pipeline is not flowing as predicted."* `THESIS.md` "Current state" line still read **"None fired (2026-04-23)"** — false since 7/21.

**Step 1 — did the literal condition fire? YES, on every basis.**

| Basis | Q1-2026 | Q2-2026 | vs `<$400M` |
|---|---|---|---|
| Supplement / 8-K (the 7/21 print) | $465M | **$298M** | **FIRED** |
| Call Report (the basis the criterion's own parenthetical cites) | $487.5M | **$323.7M** | **FIRED** |

**The firing does not depend on today's pull** — it was already true on the 7/21 supplement print. The Call Report only removes the basis escape hatch.

**Step 2 — did the *mechanism* the criterion was built to detect occur? UNDETERMINED from these data** *(this read "NO" until 2026-09-24 — CATO OZ2)*. The criterion's own stated meaning is *"the migration-velocity pipeline is not flowing."* OZK-06's note pre-registered the ambiguity: *"past-due-still-accruing can FALL as credits migrate to nonaccrual/NPA (removes from bucket)."* **The Call Report decomposition — which the supplement does not provide — narrows it but does not settle it:**

| RC-N component | Q1-2026 $K | Q2-2026 $K | Δ |
|---|---:|---:|---:|
| 30-89 days, accruing (`RCON1406`) | 190,947 | 23,273 | **−167,674 (−88%)** |
| 90+ days, accruing (`RCON1407`) | 0 | 0 | 0 |
| Nonaccrual (`RCON1403`) | 296,575 | 300,416 | **+3,841** |
| **Total (the graded measure)** | **487,522** | **323,689** | −163,833 |
| OREO (`RCON2150`) | 149,570 | 288,135 | **+138,565 (+93%)** |
| **NPA = nonaccrual + OREO** | **446,145** | **588,551** | **+142,406 (+31.9%)** |

**The entire decline is the 30-89 bucket. Nonaccrual did not fall — it rose.** And nonaccrual held roughly flat *while shedding ~$138.6M into OREO*, which requires large replacement inflow. Implied nonaccrual inflow ≈ ending − beginning + OREO transfers + charge-offs = 300.4 − 296.6 + 138.6 + 56.3 ≈ **$198.7M** — against a Q1 30-89 bucket of **$190.9M**. ⚠️ **This is an implied roll-forward, not a disclosed one** (it ignores OREO sales/writedowns and treats all charge-offs as nonaccrual-sourced; both push the estimate high). It is **not** a filed reconciliation and it is **not decisive**: ⚠️ *[2026-09-24, CATO OZ2]* the endpoints fit a flow with **zero** transfer from the Q1 30-89 bucket — let 167,674 of it cure/pay off, other formerly-current loans supply 198,660 into nonaccrual, 138,565 move to OREO and 56,254 charge off: nonaccrual 296,575 + 198,660 − 138,565 − 56,254 = 300,416 and OREO 149,570 + 138,565 = 288,135, every endpoint matched. Balances do not identify which loans left the bucket. *(This sentence read "directionally decisive" until 9/24.)*

**Adjudication (narrowed 2026-09-24): FIRED-LITERAL · mechanism UNDETERMINED.** OBSERVED: the literal condition fired (<$400M on every basis) and aggregate stress rose (NPA +31.9% QoQ, OREO +93%). INFERRED, not proven: that the 30-89 bucket emptied by migrating through to nonaccrual/OREO/charge-off rather than by cures — balance endpoints cannot distinguish the two (see the counterexample above). ⚠️ **So the fired warning is not shown to be harmless; it is shown to be ambiguous.** Resolving it needs credit-level or disclosed roll-forward evidence. *(Was "NON-DISCONFIRMING-ON-MECHANISM … the 30-89 bucket emptied by migrating through" 8/7→9/24.)* Any change to the criterion or to conviction goes through P-OZK-4 / Will — not this log.

**The criterion is mis-specified, not merely mis-triggered.** It grades a **transit bucket**, whose emptying is ambiguous between cure and progression by construction. A criterion that fires on a 32% rise in NPA is not measuring what its own sentence says it measures.

### ⚠️ P-OZK-4 (PROPOSAL, Will-gated, NOT applied) — re-specify kill §1 on a bucket-invariant measure

Replace the transit-bucket test with a stock-invariant one, e.g. *"kill §1 fires if **30-89 + nonaccrual + OREO** declines QoQ for two consecutive quarters."* On that candidate measure: **Q1-2026 = $637,092K** (190,947 + 296,575 + 149,570) → **Q2-2026 = $611,824K** (23,273 + 300,416 + 288,135) — **−4.0% QoQ, one quarter, not two.** **This is a THRESHOLD CHANGE and is therefore a proposal, not an execution.** ⚠️ And note honestly that the re-spec is **not** a device for making a disconfirming print read as confirming: on the candidate measure Q2 is **mildly down**, so it converts a false clean kill into a *soft, one-quarter directional caution* — the honest reading, not a friendlier one. That is precisely why it goes to Will rather than into the file.

**What was written to `THESIS.md` this session:** the **factual record only** — that the literal condition fired at Q2 on both bases, the decomposition, and the adjudication — with the stamp refreshed and a `CHANGELOG.md` entry. **No weight, probability, threshold or scenario branch was changed**, and the criterion's own text is left **verbatim** pending Will's ruling on P-OZK-4.

---

## 7. ✅ Frame-spec latent-bug check (PROME 7/25 packet — "pre-register against the filing that CARRIES the metric")

Walked every live pre-registered frame. **Two real instances found.**

| Frame | Metric | Which filing carries it | Exists at the pre-registered grade date? | Verdict |
|---|---|---|---|---|
| **OZK-02** | RESG problem-category share (Office+LifeSci+Land+Hotel ÷ RESG commitments) | Mgmt Comments RESG property-type table, released **with** the Q4 print | ✅ yes, at the Feb-2027 print | **OK** |
| **OZK-03** | **FY-2026 *RESG-segment* NCO ≥60bps** | ⚠️ **no single filing carries a RESG-segment NCO *rate*.** The 8-K/Mgmt Comments give bank-wide NCO plus narrative RESG charge-off color; the Call Report has no RESG segment (confirmed today); the 10-K lands late-Feb | ⚠️ **NOT as specified** | 🔴 **INSTANCE** |
| **OZK-04** | RESG problem-credit ratio | Numerator is **our own** `SEVEN_CREDIT` roster, not a filing line | Gradeable only if we keep the roster current to the print | 🟠 **carrier = own workbook — note it** |
| **OZK-09** | **$140M+ RaDD-attributable loss recognition** | ⚠️ OZK's **filings do not name credits.** RaDD was named by management **on the Q2 call Q&A**, not in the release. Z10 already requires "executed-and-disclosed" | ⚠️ carrier is likely the **earnings-call transcript**, not a filing — and credit-level attribution may **never** be disclosed | 🔴 **INSTANCE** |

**🔴 OZK-03 — the instance the packet predicted.** The prediction says *RESG* NCO; the tracking note inside the same row cites *"Q1 26 was 57bps in-line with 50bps guide"* — a **bank-wide** figure. **The frame is written on one series and tracked on another.** Exactly the failure mode PROME described: at grade time under pressure, whatever is available (bank-wide NCO) gets substituted for what was specified (RESG NCO), producing a confident verdict off the wrong series.
**Handling (no substitution made):** flagged here and in `TODO.md`. Either re-key OZK-03 to bank-wide NCO **explicitly** (a wording change to a live frame → ⚠️ **PROPOSAL P-OZK-5**, Will/PROME-gated, **not applied**) or mark the RESG leg **unscoreable-at-print** in advance. **It resolves Feb-2027 — there is ample time to fix it honestly rather than at the grade.**

**🔴 OZK-09 — attribution-carrier risk.** The threshold is credit-specific ($140M+ on RaDD); the disclosure practice is aggregate. Under the frozen Option-2 window, recognition counts through the Q4'26 print (late Jan '27) — a date at which **RaDD-attributable** recognition may not be separately disclosed anywhere. Pre-register now that the carrier set includes the **earnings-call transcript** (as Stage-2 already did at Q2), and that a **no-attribution outcome is a resolvability defect → STATUS `STUCK`, not a confidence cut.** ⚠️ **Recorded as a flag only. OZK-09's 45% and its Option-2 ruling are untouched** — the mission's untouchable, and correctly so.

---

## 8. What this session did NOT do

- **No grade moved.** `PREDICTIONS.tsv` unchanged. Z6 honored — the Call Report re-graded nothing.
- **No threshold, probability or scenario weight moved.** OZK-09 45%, weights A30/B45/C8/D17, weighted EL ~$129M, the ≤55bps kill line, the $400M kill §1 line, the Option-2 FROZEN ruling — **all untouched**.
- **No position action and no position recommendation.** `POSITIONS.md` was corrected to *mirror* `FORGE/STATUS.md` (8/2 ANVIL reconcile) with Will's 8/4 RIDE ruling cited. That is a record fix, not a trade.
- **No edits outside `AGENTS/OZK/`** except the delivery packet into `PROME/inbox/` (root carve-out ①).
- **No IQHQ re-mark.** Nothing in the Call Report touches the recognition-window frame; the Call Report carries no classified/criticized line and no credit names (§7 confirms this the hard way).

---

*Pulled and computed 2026-08-07 from FFIEC CDR PWS, ID_RSSD 107244, RSSD verified at the primary. All figures carry REPDTE + MDRM item code. Series → `workbook/CALL_REPORT_SERIES.tsv`. Companion: WAL's same-day first-run → `../WAL/MI3_FIRST_RUN_2026-08-07.md` (independent bank, same instrument, same P8 basis defect).*
