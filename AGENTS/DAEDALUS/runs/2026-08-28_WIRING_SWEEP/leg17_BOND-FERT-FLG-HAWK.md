# ⑰ METRIC-SURFACE AUDIT — BOND / FERT / FLG / HAWK (n=20 rows, 5/desk)

**Sample caveat carried forward:** n=20 rows from 4 desks, seeded random (`leg17_SAMPLE.md`). This is a sample, not a census — do not extrapolate a fleet rate from it.

Verdict tokens used exactly as specified. Where the strict token set does not have a clean fit for a retired/pre-registration/qualitative row, I say so explicitly rather than force a token, per rule 4 (never guess a clean verdict).

---

## BOND — `AGENTS/BOND/workbook/VX.tsv`

### VX-BND-09 (L10) — Auction Tail — RETIRED
Threshold text verbatim: Th_Y=`n/a`, Th_R=`n/a`. Score=`RETIRED`.

- **(a) INSTRUMENT:** NONE — but this is *by design*, not a gap. Row text: "the auction-tail METRIC was formally retired 7/28 as unscoreable... `grade_auction.py` computes no tail." Verified: `AGENTS/BOND/monitors/grade_auction.py` docstring states "NO TAILS. A tail needs the when-issued yield at bid deadline and TreasuryDirect does not publish it. Retired 2026-07-28 as unscoreable from primaries; no gate may key on one." Grepped `AGENTS/BOND` for any tail-scoring code: none found; `monitors/AUCTION_HEALTH.md` carries the same retirement banner ("Wire-reported tails are `[med-conf]` and are recorded in Notes only, never used to fire a classification").
- **(b) BASIS/WINDOW:** UNSTATED (n/a cells) — deliberately, since retired.
- **CONJUNCTION:** N/A (single dead vector, no legs).
- **POINTER:** NO-POINTER.
- **MECHANISM:** CANNOT-JUDGE / N/A — retired, no live mechanism claim in force.
- **BOOT-RENDERED:** NO. BOND has no `boot.py`; `monitors/boot_recompute.py` (the boot-6 instrument) pulls H.15/credit levels + prints `TRADE.md`'s gate table — it never reads `VX.tsv`. Confirmed by grep: no `VX.tsv` reference in `boot_recompute.py`, `grade_auction.py`, `fr2004_fetch.py`, or `cdx_proxy.py`.
- **STATIONARITY:** N/A (retired).

**Verdict on this row: this is a CLEAN example, not a defect.** The retirement is explicit, dated, causally explained (structural TreasuryDirect data limit, not a data gap), cross-referenced at `monitors/AUCTION_HEALTH.md`, and the scoring code was actually changed to match. Contrast with FERT/HAWK findings below where a stated gap is *not* this clean.

### VX-BND-10 (L11) — IG Primary Issuance — 🟢, Score 1, **Last_Updated 2026-07-28 (31 days stale as of 2026-08-28)**
Th_Y=`<$5B/day or visible concession`, Th_R=`ZERO 2+ days / blue-chip pulled deals`.

- **(a) INSTRUMENT:** NONE. Grepped `AGENTS/BOND` for a $/day IG issuance-volume producer: no script. The row's own Last_Signal cell is pure prose ("IG primary still open; no pulled deals reported") with no $/day figure at all. The closest analog, `AGENTS/BOND/monitors/CREDIT_PRIMARY_MARKET.md` (refreshed 2026-08-27, i.e. current), literally states its own IG-volume cell is "wire-level, NOT pulled at primary" — i.e. even the fresher sibling surface has no real producer for this metric, only a WALTER wire relay.
- **(b) BASIS/WINDOW:** PARTIAL. Unit is named ($/day) and the Red leg names a window ("2+ days"), but no vendor/primary is attached to the row itself — the only vendor mentioned in Notes (SIFMA) is about a *different*, unrelated monthly-split refresh task, not this trigger's day-level read.
- **CONJUNCTION:** Both Th_Y and Th_R are OR-gates over two legs each.
  - Th_Y leg 1 ($5B/day) = NONE (above). leg 2 ("visible concession") = PROSE-VALUE, untracked on this row.
  - Th_R leg 1 ("ZERO 2+ days") = NONE (same instrument gap). leg 2 ("blue-chip pulled deals") = PROSE-VALUE but *is* actually tracked, just on the sibling doc, not here — `CREDIT_PRIMARY_MARKET.md` carries a live "Pulled deals: ZERO [8/27]" line.
  - Gate verdict: **CANNOT-FIRE cleanly on this row as written** (no leg on VX-BND-10 itself has a citable instrument); the one leg that IS trackable fleet-wide (pulled deals) is tracked on a different, uncited file.
- **POINTER:** NO-POINTER, and this is itself the finding — the row does not cross-reference `CREDIT_PRIMARY_MARKET.md`, which is BOND's own actively-maintained, same-topic surface (refreshed 8/27 vs. this row's 7/28). Two views of the same fact at wildly different vintages inside one desk.
- **MECHANISM:** MATCH in concept (primary-market access), but the row cannot demonstrate it given the staleness/instrument gap.
- **BOOT-RENDERED:** NO (same reason as VX-BND-09 — VX.tsv is not a boot-read surface for BOND).
- **STATIONARITY:** CANNOT-JUDGE precisely, but worth flagging: `CREDIT_PRIMARY_MARKET.md` records June 2026 IG issuance at a **record ~$175–187B/month** (~$6-8B/day) — i.e. the market is currently issuing well above a "$5B/day = freeze warning" Yellow line during a documented boom, which is at minimum evidence the fixed nominal $5B/day anchor has not been re-validated against current issuance scale.

### VX-BND-12 (L13) — Term Premium / Long-End Risk — Score 3
Th_Y=`30Y near 5%`, Th_R=`30Y >5% sustained plus weak auction/funding stress`.

- **(a) INSTRUMENT:** COMMAND-NAMED. `FRED THREEFYTP10` (Kim-Wright 10Y term premium), pulled via the desk's standard live-FRED path (`FORGE/tools/market-data/fetch.py fred <SERIES>`, per BOND `CLAUDE.md` boot step 6: "Pull load-bearing figures LIVE... via `FORGE/tools/market-data/fetch.py`"). Confirmed the series is NOT in `boot_recompute.py`'s hardcoded `H15_SET`/`GATES` dict (it only carries `DGS2/DGS10/DGS30/DFII10/T10YIE/T5YIFR` + 3 credit series) — so THREEFYTP10 is refreshed by a separate, manual `fetch.py fred THREEFYTP10` call each session, not by the automated boot recompute. This is a real, if narrow, gap: the desk's own "refresh the RELEASE as a SET" doctrine (established after 6 method errors on 8/18) does not cover this series.
- **(b) BASIS/WINDOW:** STATED — series named, daily cadence, explicit as-of dates (8/21), n given for both the full-series and 2026-window superlatives, three model caveats disclosed (model output not reconcilable to ACM, lags, n=1 model).
- **CONJUNCTION:** N/A — Th_R is a genuine two-leg AND ("30Y >5% sustained" **plus** "weak auction/funding stress"), but VX-BND-12 itself only carries the level leg; the STATUS matrix row explicitly notes it scores this differently: "this vector scores 4 on the level alone while the STATUS matrix... additionally requires a weak auction." So within THIS row, only one leg is graded — CAN-FIRE on the level leg alone (30Y is well above 5%), but the row's own text discloses that the *matrix* roll-up requires the second leg and that leg has been re-tested and did not fire (per VX-BND-05, out of sample). Flagging for completeness, not as a defect — the desk states this divergence is "intentional, not drift."
- **POINTER:** NO-POINTER (self-contained FRED citation).
- **MECHANISM:** MATCH — decomposition explicitly ties the level to the term-premium mechanism (vs. policy-path), with caveats disclosed.
- **BOOT-RENDERED:** NO (VX.tsv not boot-read; and per (a), THREEFYTP10 isn't even in the automated boot_recompute pull list).
- **STATIONARITY:** OK — this is a deliberate regime-level call (30Y approaching a 19-year high) with explicit historical context (2007 peak ~5.44%, 2026 max 5.31%) rather than a naively fixed level; the desk documents the historical distribution each time it cites the level.

### VX-BND-13 (L14) — FOI Demand Hole — Score 2
Th_Y=`INSTRUMENTED [2026-08-20]: indirect %-of-competitive-accepted BELOW the auctioned tenor's own trailing-12 MEDIAN at 2 consecutive coupon auctions`; Th_R=`indirect below the tenor's own trailing-12 MIN at 2+ auctions inside 30 days... OR TIC foreign-official UST holdings falling 3 consecutive monthly prints [ZHAO owns TIC]`.

- **(a) INSTRUMENT:** COMMAND-NAMED. `monitors/grade_auction.py --cusip/--date` against TreasuryDirect `TA_WS` (verified in script header: "% of COMPETITIVE ACCEPTED... Benchmarks are PER TENOR"). This is one of the best-instrumented rows in the sample.
- **(b) BASIS/WINDOW:** STATED — per-tenor trailing-12 medians/mins, %-of-competitive-accepted basis, TreasuryDirect TA_WS source, explicit per-tenor benchmark table cross-referenced in `monitors/AUCTION_HEALTH.md`.
- **CONJUNCTION:** Th_R is a 2-leg OR: leg 1 (auction-composition, TreasuryDirect) = COMMAND-NAMED/STATED as above. leg 2 (TIC foreign-official holdings, "ZHAO owns TIC") = POINTER, traveled below. **Gate verdict: CAN-FIRE** — both legs have real, live instruments.
- **POINTER:** OK. Traveled to `AGENTS/ZHAO/STATUS.md`/`workbook/VX.tsv`: ZHAO runs a live, primary-sourced TIC program (Treasury TIC Tables 1/3/5, direct pull, most recent read 2026-08-21 — "ZHA-04 FIRED (TRUE at 42%)" on China's June TIC print). Same series concept (foreign-official UST demand), real target, currently live. OK.
- **MECHANISM:** MATCH — explicitly scoped as an "AUCTION-altitude read" distinct from ZHAO's custody-altitude read, with the divergence between the two named as the thing to watch.
- **BOOT-RENDERED:** NO (VX.tsv not boot-read for BOND).
- **STATIONARITY:** OK — trailing-12 rolling percentile bands are self-adapting, not fixed absolute levels; this is a well-designed instrument for a non-stationary series.

### VX-BND-16 (L17) — Treasury Buyback Posture / Debt-Management — Score 4, 🔴 fired 2026-08-19
Th_Y=`Long-end offer/accept ratio rising (now ~13x, was ~2x at 2024 launch) OR long-end share rising`; Th_R=`$2B long-end liquidity accept cap LIFTED (YCC-lite / stealth long-end suppression)`.

- **(a) INSTRUMENT:** Th_Y leg (offer/accept ratio, long-end share) = **NONE**. Grepped `AGENTS/BOND` and repo-wide for a buyback-operations fetch script: none found; the only automated touch is `monitors/docket_check.py`, which carries a *hardcoded calendar-row string* for the 9/9 stepped-up op, not a ratio computation. The "~13x" and "~2x" figures in the row are uncomputed narrative. Th_R leg (cap lifted) = **PROSE-VALUE** — a real, one-time primary-document event (Treasury press release `sb0607`, verified from the box on 8/19), not a running command, but genuinely checked at the primary rather than relayed.
- **(b) BASIS/WINDOW:** Th_Y = UNSTATED (no vendor, no window, no recomputation method for the offer/accept ratio). Th_R = STATED (dated event, primary doc cited, explicit letter-vs-mechanism split).
- **CONJUNCTION:** Th_R is effectively 2 co-mingled claims in ONE cell — a MEASURABLE clause (cap lifted) and an INTERPRETIVE clause ("YCC-lite / stealth long-end suppression"). **This is a self-diagnosed spec defect, quoted verbatim from the row itself:** *"SPEC DEFECT NAMED: this trigger FUSES a measurement with its interpretation in one cell, so 'did it fire?' has no clean answer — KB-BND-099 class... re-cut (separate MEASUREMENT from INTERPRETATION) goes into the 8/25-27 pre-registration cluster."* I checked the 8/25-27 cluster (VX-BND-01, out of sample but read in full for context): it covers auction-composition rules only (I'/MATRIX_V2), **not** this row. **As of today (2026-08-28), this named re-cut has not happened** — the fused cell is still live, 9 days after BOND itself flagged it and named a remediation date that has since passed.
- **POINTER:** NO-POINTER (self-contained primary citation).
- **MECHANISM:** CANNOT-JUDGE cleanly, by the row's own admission — that is precisely its stated finding (measurable clause MET, interpretive clause REJECTED on the letter). This is a case where "cannot cleanly judge mechanism" is the row's own correct output, not an audit gap.
- **BOOT-RENDERED:** NO.
- **STATIONARITY:** N/A — this is a policy-program threshold (a named, dated Treasury operation), not a statistical band.

### BOND summary table

| Row | Instrument | Basis/Window | Conjunction | Pointer | Mechanism | Boot-Rendered | Stationarity |
|---|---|---|---|---|---|---|---|
| VX-BND-09 | NONE (by design, retired) | UNSTATED (n/a, deliberate) | N/A | NO-POINTER | N/A | NO | N/A |
| VX-BND-10 | NONE | PARTIAL | CANNOT-FIRE (on this row) | NO-POINTER (uncited sibling doc) | MATCH (conceptually) | NO | flag: nominal level un-rebased vs. record issuance |
| VX-BND-12 | COMMAND-NAMED | STATED | N/A (single-leg on this row) | NO-POINTER | MATCH | NO | OK |
| VX-BND-13 | COMMAND-NAMED | STATED | CAN-FIRE | OK (ZHAO) | MATCH | NO | OK |
| VX-BND-16 | NONE (Y) / PROSE-VALUE (R) | UNSTATED (Y) / STATED (R) | fused-cell spec defect, self-flagged, unfixed 9 days past its own deadline | NO-POINTER | CANNOT-JUDGE (by design) | NO | N/A |

**BOND triage: mostly PER-ROW, plus one CONVENTION fact.** BOND's own hygiene discipline is unusually strong — 3 of 5 sampled rows are well-instrumented, and the two weak rows (BND-10, BND-16) are largely *already self-diagnosed* by BOND (staleness on BND-10 is visible from its own Last_Updated field; the fused-cell defect on BND-16 is BOND's own KB-BND-099 finding). The one CONVENTION-level fact worth fixing once: **`VX.tsv` is not read by any boot instrument** — `boot_recompute.py` refreshes underlying series levels and `TRADE.md`'s gate table, but never checks that a VX.tsv *band/score* still matches those levels. A wrong band on any BOND VX row (not just the 5 sampled) would not be caught mechanically. Do not rewrite rows for this — it's a missing cross-check, not a per-row content problem.

---

## FERT — `AGENTS/FERT/workbook/TRIGGERS.tsv`

Structural note: this is a **wake register** (`ID/Trigger/Instrument/Next_Check/Cadence/Why_It_Wakes_You/Notes`), not a banded VX file — there is no Threshold_Yellow/Red column. The closest analog to "the threshold text" is the combination of the `Why_It_Wakes_You` cell and Notes. FERT has exactly one Python file (`AGENTS/FERT/boot.py`) — grepped `AGENTS/FERT` for any other `.py`/fetch script: none exists. Every row's "Instrument" column names a source URL/PDF, never a wired command.

`boot.py` leg 3 (`triggers-due`) prints `DUE: <ID> [<date>] <Trigger text, truncated to 60 chars>` for any row past `Next_Check`. As of 2026-08-28: T2 (due 8/25), T4 (due 8/20) and T12 (due 8/24) are all **currently overdue and would print at boot**; T9 and T10 are not yet due.

### T2 (L3) — USDA ERS Food Price Outlook monthly update
Trigger/basis: "Upward revision to 2027 food-at-home (2.9% as of the 7/24 edition) CITING INPUTS = transmission signal."

- **(a) INSTRUMENT:** NONE. `ers.usda.gov Food Price Outlook` is a named source, not a wired fetch — no script pulls it. Retrieval is a manual read at `Next_Check`.
- **(b) BASIS/WINDOW:** STATED. This is actually a well-specified categorical signal, not a numeric one: Notes explicitly redefine the fire condition as fertilizer *appearing* in the cited driver list, not the % moving — "Diff the vintages, not just refresh... The signal is fertilizer APPEARING, not the number moving." Cadence (monthly ~25th) and vintage (7/24 edition) are both named.
- **CONJUNCTION:** N/A (single categorical leg).
- **POINTER:** NO-POINTER.
- **MECHANISM:** MATCH — food-at-home transmission of input costs is exactly FERT's charter mechanism.
- **BOOT-RENDERED:** YES (currently DUE, would print at boot per `boot.py` leg 3) — but only ID+date+first-60-chars of the Trigger text; none of the qualifying Notes logic travels into the boot print.
- **STATIONARITY:** N/A (categorical, not a numeric band).

### T4 (L5) — DTN weekly retail fertilizer article
Trigger text: "Benchmark refresh: urea retail + DAP/MAP TIGHT-LEG WATCH — the phosphate leg is the live one."

- **(a) INSTRUMENT:** PRODUCER-EXISTS-UNCITED. The row itself names only a URL (`dtnpf.com`), no script. But the row's *actual* numeric threshold lives elsewhere and is real: `PROME/GATES.tsv` **`GATE-FERT-G5`** (found by traveling the DOCKET pointer below) fully specifies: *"DTN retail DAP OR MAP > $1,000/ton (instrument = DTN Progressive Farmer weekly retail $/ton — NEVER conflate w/ Pink Sheet $/mt or NOLA $/st). Base-rated at registration: 93rd-pct context, MAP +4.3% / DAP +9.1% to the line."* This is a real, base-rated, Will-ratified gate — but **T4's own row in `TRIGGERS.tsv` never cites `GATE-FERT-G5` by ID**, so a reader of TRIGGERS.tsv alone would see only "benchmark refresh," not the $1,000/ton line that actually governs it.
- **(b) BASIS/WINDOW:** PARTIAL on the row as written (cadence stated: weekly Wed, clock established with two consecutive 7-day-apart articles; but no numeric basis on the row itself — "TIGHT-LEG WATCH" names no level). STATED once you travel to GATES.tsv.
- **CONJUNCTION:** N/A (single leg once resolved via GATES.tsv).
- **POINTER:** This is the key finding for FERT. `PROME/DOCKET.tsv` row (2026-08-20) **points TO** `AGENTS/FERT/workbook/TRIGGERS.tsv T4` as "the DOCKET backing FERT's ASK-1," and `GATES.tsv` `GATE-FERT-G5`'s Source_of_truth column also names `TRIGGERS.tsv (T4 DTN weekly = the wake)`. But **the link is one-directional**: T4 does not point back to `GATE-FERT-G5`. Verdict: **NO-POINTER on the row itself**, though the target it should point to (GATE-FERT-G5) does exist, is real, and is well-specified. Also worth noting from `GATES.tsv`: the gate's own status trail shows it slipping — "RE-DATED at PROME 8/28 boot (consumer 8/27 passed with FERT dark — its 8/27 DTN read unverified)" — i.e. FERT has not actually graded this gate on its last two scheduled reads.
- **MECHANISM:** MATCH — GATES.tsv base-rate note ties the $1,000/ton line to "cost-push root (rock + sulfur + Mosaic idles)," which is the same mechanism T12 (below) tracks directly. Good cross-row coherence once resolved.
- **BOOT-RENDERED:** YES (currently DUE, `Next_Check` 8/20 has passed) — flag-only, no $ level in the boot print.
- **STATIONARITY:** OK-with-caveat. The $1,000/ton line was base-rated at registration (93rd-pct context stated, not a blind pick), which is good practice; a nominal commodity-price level threshold over a multi-year horizon would eventually need re-basing, but for the desk's stated near-term thesis window this is acceptable.

### T9 (L10) — Morocco AD/CVD suspension expiry
Trigger text: "Suspension expires ~2027-02-28; lapse re-tariffs the phosphate import leg into an already-tight market."

- **(a) INSTRUMENT:** NONE (a one-shot regulatory-calendar event, not a metric — Federal Register is the named primary, checked manually).
- **(b) BASIS/WINDOW:** STATED, and unusually precise for a one-shot: exact FR doc number (2026-13588), signing date (6/29/26), 8-month suspension window, explicit "check ~2wk ahead" lead-time logic (Next_Check 2027-02-15 vs. actual expiry 2027-02-28 — deliberately offset, not a discrepancy).
- **CONJUNCTION:** N/A (single dated event).
- **POINTER:** OK. Traveled to `PROME/DOCKET.tsv` (row dated 2027-02-28): "Morocco phosphate AD/CVD suspension EXPIRES (~8 months from 6/29/26 proclamation signing; Fed Register doc 2026-13588 + Commerce 2026-13796, verified at primary 8/16)... Owner = FERT once re-chartered." Same FR doc number, same date, same series — target exists, matches. OK.
- **MECHANISM:** MATCH — tariff snap-back on a specific import leg into a named tight market, precisely FERT's charter mechanism.
- **BOOT-RENDERED:** NO (Next_Check 2027-02-15, not due).
- **STATIONARITY:** N/A (one-shot regulatory event, not a numeric band).

### T10 (L11) — China export quota / guidance-price state re-read
Trigger text: "THE vector that decides price — never a frozen constant."

- **(a) INSTRUMENT:** NONE. Sources named (MOFCOM/NDRC relays, CF commentary, Profercy) are all manual-read; no script.
- **(b) BASIS/WINDOW:** PARTIAL, and this is a genuine, self-disclosed gap rather than a hidden one: the row states "floor $660/$670 LIFTED early June and replaced by an unpublished lower guidance price. **The replacement LEVEL is PUBLIC-AND-UNFETCHED — find it.**" I.e., FERT's own most-important trigger ("THE vector that decides price") is currently running with **no known current level** for its own governing number. Cadence is stated (monthly + every-wake re-read); the level is not.
- **CONJUNCTION:** N/A.
- **POINTER:** Content-parallel but not cross-referenced to `PROME/GATES.tsv` **`GATE-FERT-G3`** ("China 2026 urea export quota revised DOWN, OR a guidance floor reimposed ABOVE prevailing intl FOB... $660 floor LIFTED early-June [kill-on-sight as a live constraint]"). Same facts, same $660 figure, same "floor lifted" state — but GATE-FERT-G3's own Source_of_truth cites `AGENTS/FERT/workbook/KB.tsv (KB-FERT-006)`, not TRIGGERS.tsv T10, and T10 does not cite GATE-FERT-G3 either. Verdict: **NO-POINTER** (parallel content, no explicit cross-link either direction) — lower severity than T4's gap since T10 already discloses its own missing-level problem in plain text.
- **MECHANISM:** MATCH — explicitly named as the price-floor mechanism.
- **BOOT-RENDERED:** NO (Next_Check 2026-09-15, not due).
- **STATIONARITY:** N/A (no live level to judge stationarity of).

### T12 (L13) — Phosphate margin inputs: sulfur + US producer curtailment
Trigger text: "The MECHANISM under the phosphate leg — cost-push, not demand pull."

- **(a) INSTRUMENT:** NONE (Advanced Turf weekly PDF + Mosaic IR, both manual-read; no fetch script — same pattern as T4/T5's PDF sources).
- **(b) BASIS/WINDOW:** PARTIAL. Concrete levels ARE given (Tampa Q3 sulfur contract +$50/lt to $705/lt; US Gulf prilled sulfur $1,150/mt; named plant curtailments), but no explicit as-of date is attached to those specific figures on the row, and the row self-flags a reliability gap: "Currently SINGLE-SOURCE (one trade distributor) — get a second read before treating as load-bearing."
- **CONJUNCTION:** N/A.
- **POINTER:** NO-POINTER (no cross-reference needed/present; row is self-contained).
- **MECHANISM:** MATCH, explicitly named as such, and internally consistent with T4's cost-push framing (same root cause cited: rock + sulfur + Mosaic idles) — good cross-row coherence.
- **BOOT-RENDERED:** YES (currently DUE, Next_Check 8/24 passed).
- **STATIONARITY:** N/A (no fixed band; the row is a data point, not a threshold).

### FERT summary table

| Row | Instrument | Basis/Window | Conjunction | Pointer | Mechanism | Boot-Rendered | Stationarity |
|---|---|---|---|---|---|---|---|
| T2 | NONE (named URL, manual) | STATED (categorical, well-specified) | N/A | NO-POINTER | MATCH | YES (flag-only) | N/A |
| T4 | PRODUCER-EXISTS-UNCITED (GATE-FERT-G5, real, uncited) | PARTIAL (row) / STATED (via GATES.tsv) | N/A | NO-POINTER (one-directional link exists FROM Gates/Docket, not TO them) | MATCH | YES (flag-only) | OK (base-rated) |
| T9 | NONE (one-shot, manual) | STATED | N/A | OK (DOCKET) | MATCH | NO | N/A |
| T10 | NONE (manual) | PARTIAL — self-disclosed missing level | N/A | NO-POINTER (parallel, uncross-linked GATE-FERT-G3) | MATCH | NO | N/A |
| T12 | NONE (manual, single-source) | PARTIAL | N/A | NO-POINTER | MATCH | YES (flag-only) | N/A |

**FERT triage: CONVENTION, not per-row.** Two whole-registry facts explain nearly everything above: (1) FERT has zero fetch scripts — every Instrument column names a source, not a producer, by design (`boot.py` is a pure date-scanner, not a data puller); this is consistent with FERT's Will-ruled TRIAGE/EVENT-DRIVEN charter (log+flag, not deep automation) and should not be read as negligence. (2) `TRIGGERS.tsv` rows systematically do not cross-cite the `PROME/GATES.tsv` IDs that actually carry their base-rated numeric thresholds (found on both sampled rows that have a matching GATES.tsv entry, T4↔G5 and T10↔G3) — this is a one-time registry-wide fix (add the GATE-FERT-Gn ID to the corresponding TRIGGERS.tsv row's Notes), not five separate row rewrites. Mechanism alignment across the sample is uniformly good.

---

## FLG — `AGENTS/FLG/workbook/TRIGGERS.tsv`

Structural note: the file header is explicit and load-bearing — **"⚠️ NOTHING HERE IS A REGISTERED GATE. These are wake PROMPTS. Thresholds base-rate at first live session, then route to PROME for GATES.tsv registration with an assigned grader."** FLG is a greenfield desk (built 2026-08-20) that per `PROME/DOCKET.tsv` "has run ZERO sessions." This context matters for every verdict below: a pre-registration wake-prompt presenting as such is not the same defect class as a live-scored VX row failing to be gradeable.

`AGENTS/FLG/boot.py` leg 3 (`triggers-due`) and leg 4 (`quarter-due`, FLG-specific: flags a closed Call Report quarter missing from `MI3_FLG.tsv`) both exist and are wired. None of the 5 sampled rows are currently due (`Next_Check` = 2026-11-14 / 2026-11-09 for all).

### T-01 (L2) — Q3-2026 Call Report filed (RSSD 694904)
- **(a) INSTRUMENT:** PRODUCER-EXISTS-UNCITED. Row names "FFIEC CDR bulk / UBPR, RSSD 694904" (the source) but not a script. A real, live-callable producer for this exact source exists: `AGENTS/REGINALD/scripts/mi3_cohort_screen.py` ("FFIEC CDR REST/JWT, RetrieveFacsimile/SDF") — but it is REGINALD's script, uncited on FLG's row, and FLG has no equivalent of its own.
- **(b) BASIS/WINDOW:** STATED — Anchor_Type=RULE, explicit derivation ("quarter-end 2026-09-30 + 45d filing lag"), and Notes flag the restatement risk ("Call Report data is RESTATED — amendments can cross a line months later").
- **CONJUNCTION:** N/A.
- **POINTER:** target file `AGENTS/FLG/workbook/MI3_FLG.tsv` exists and is real: it carries actual quarterly data through 6/30/2026 (`loans_qoq_pct`, `item9a_k`/`item9b_k` etc.), matching the series this row names. **But** its own header discloses: *"PROVENANCE — SEEDED, NOT SELF-PULLED. Extracted verbatim 2026-08-20 by DAEDALUS at FLG build from `AGENTS/REGINALD/workbook/MI3_COHORT.tsv`... Not PRIMARY to FLG until re-verified at FFIEC CDR."* `Verified_By` is blank on every row (UNSET). Verdict: **OK-with-caveat** — the target exists and carries the right series, but it is a one-time mirror FLG has never independently re-pulled or verified, and no FLG-owned command will refresh it when Q3 lands; `boot.py`'s leg-4 `quarter-due` check will correctly flag the gap when Q3 closes, but filling it still requires either borrowing REGINALD's script or building FLG's own.
- **MECHANISM:** MATCH — SR 07-1 concentration/coverage ratios are exactly the thesis-load-bearing figures this filing reprices.
- **BOOT-RENDERED:** NO currently (not due); WOULD be rendered via leg-4 `quarter-due` once the window opens — this is a real, wired, FLG-specific boot check (unusual positive: most desks in this sample don't have an analog).
- **STATIONARITY:** N/A (event-anchored, not a numeric band).

### T-02 (L3) — Q3-2026 10-Q filed (EDGAR, Flagstar Financial Inc.)
- **(a) INSTRUMENT:** NONE, and this is a concrete, checkable gap rather than a domain-inherent one. Row names "EDGAR full-text / company filings feed." REGINALD owns a real, wired EDGAR/8-K filing monitor for its own cohort — `AGENTS/REGINALD/scripts/8k_monitor.py`, `TARGETS = {"WAL":..., "OZK":..., "EGBN":..., "ZION":..., "VLY":...}` — grepped the file: **Flagstar (FLG) is not in the TARGETS dict.** An analogous producer exists for structurally identical peer banks and was simply never extended to FLG's own CIK. FLG has no filings-monitor of its own either.
- **(b) BASIS/WINDOW:** PARTIAL — Anchor_Type=RULE with an explicit [EST] derivation (quarter-end+40d), but the row itself flags the harder半 of the gap: "⚠️ HOLDING COMPANY, not RSSD 694904 — do not compare line-for-line without stating the perimeter" (a real, self-aware basis caveat, well done).
- **CONJUNCTION:** N/A.
- **POINTER:** NO-POINTER.
- **MECHANISM:** MATCH — the row correctly scopes itself as the "narrative half the Call Report does not carry."
- **BOOT-RENDERED:** NO (not due; and even when due, no filings-monitor exists to auto-surface the actual filing — `boot.py`'s triggers-due leg would only flag the *date*, not confirm the filing happened).
- **STATIONARITY:** N/A.

### T-04 (L5) — Deleveraging check: total loans QoQ turned positive?
- **(a) INSTRUMENT:** COMMAND-NAMED (file+column). Row cites `AGENTS/FLG/workbook/MI3_FLG.tsv loans_qoq_pct` directly, and that column contains real, non-empty quarterly data (e.g. 6/30/2026: `0.9`). Same MIRROR/UNVERIFIED caveat as T-01 applies (see above) — the number is real and checkable today, but its refresh path runs through REGINALD's script, not an FLG-owned one.
- **(b) BASIS/WINDOW:** STATED — unit (QoQ %), series (loans_qoq_pct), source (FFIEC Call Report via the MI3 mirror), window (quarterly) are all named on the row or in the immediately-adjacent MI3_FLG.tsv header.
- **CONJUNCTION:** The row's real fire condition (per Notes and cross-referenced `EXIT_PROTOCOL.md` K-1) is "**two consecutive** positive quarters," not a single print — this is a counted-run condition on one series, not an AND/OR across different metrics. N/A for the strict conjunction test, but worth flagging: per `PROME/DOCKET.tsv`'s FLG scope-checkpoint row, Q2-2026 loans_qoq was already +0.9% (first positive in 11 quarters), i.e. this counter is currently 1-of-2 and one more positive quarter fires the counter-thesis — a live, close-to-firing condition on a desk that has run zero sessions to notice.
- **POINTER:** OK (MI3_FLG.tsv exists, right column, right series) — same caveat as T-01 (mirror, unverified-by-FLG).
- **MECHANISM:** MATCH — explicitly registered as the bidirectional/counter-thesis leg (blueprint §4), which is good falsification hygiene.
- **BOOT-RENDERED:** NO currently (Next_Check 2026-11-14).
- **STATIONARITY:** N/A (a directional sign-change test, not a level band).

### T-05 (L6) — Coverage check: ACL / nonaccrual crossing 100%?
- **(a) INSTRUMENT:** Same as T-01/T-04 pattern — PRODUCER-EXISTS-UNCITED (REGINALD's `mi3_cohort_screen.py`/`BANK_EXPOSURE_MATRIX.md` derive this; FLG's row cites only "FFIEC Call Report, ACL and nonaccrual cells").
- **(b) BASIS/WINDOW:** STATED, and unusually well-verified: FLG's own `KB.tsv` (KB-FLG-004/017/018/019/020/021) shows this seed figure (29% coverage) was derived from a real primary — REGINALD's `BANK_EXPOSURE_MATRIX.md` and FFIEC Schedule RI-B Part II, with an identity re-derived first-hand at FLG (KB-FLG-018: "identity re-derived first-hand at FLG and reproduces exactly") and cohort-base-rated against 168 bank-quarters (KB-FLG-021). This is genuinely rigorous, load-bearing work — one of the best-sourced numbers in the entire 20-row sample, even though it predates FLG's own charter as a mirror.
- **CONJUNCTION:** N/A (single ratio, "crossing 100% in either direction is arithmetic").
- **POINTER:** OK (KB.tsv chain resolves cleanly to REGINALD's primary-verified derivation).
- **MECHANISM:** MATCH — "the reserve cannot cover loans already on nonaccrual" is precisely what the cited KB rows establish and stress-test.
- **BOOT-RENDERED:** NO currently.
- **STATIONARITY:** N/A (a %-coverage ratio with a hard arithmetic meaning at 100%, not a fitted band).

### T-07 (L8) — REGINALD VX-REG-6.03 price ladder
- **(a) INSTRUMENT:** COMMAND-NAMED. "REGINALD market.py" resolves to the real, repo-root `scripts/market.py` (confirmed: FLG ticker is in its `WATCHLIST` dict, live yfinance pull), which REGINALD's own `boot.py` also calls (`MARKET_PY = WORKSPACE/scripts/market.py`).
- **(b) BASIS/WINDOW:** STATED — REGINALD's `VX-REG-6.03` row gives FROZEN absolute-dollar bands ($12.82/$12.10/$11.39, -10/-15/-20% off a dated $14.24 baseline from 8/12), live comparison via market.py, explicit "FROZEN, not rolling" label.
- **CONJUNCTION:** N/A (single instrument, tiered severity bands, not multiple ANDed metrics).
- **POINTER:** OK. `AGENTS/REGINALD/workbook/VX.tsv` `VX-REG-6.03` exists, is live (Last_Updated 2026-08-20), and matches the row's cited baseline/bands exactly, including the dual-action ruling language quoted verbatim in both places.
- **MECHANISM:** MATCH — a bank-equity price ladder as proxy for market-priced credit stress, consistent with FLG's own credit thesis.
- **BOOT-RENDERED:** NO on FLG's own boot — `AGENTS/FLG/boot.py` only date-scans `TRIGGERS.tsv`/`PREDICTIONS.tsv`/quarter-due; it does not pull `scripts/market.py` or check REGINALD's live price against the bands. Since T-07 is explicitly a "dual-action" gate where "FLG is now ON the action line" for a fire, this is a real wiring gap: **a live price breach would not wake a dark FLG desk through FLG's own boot instrument** — only through REGINALD noticing and routing (REGINALD's own boot behavior for this was outside this audit's assigned scope).
- **STATIONARITY:** OK — the FROZEN-baseline design is a deliberate, stated anchor for a bear-thesis price ladder, not an unaware fixed level on a naturally drifting series.

### FLG summary table

| Row | Instrument | Basis/Window | Conjunction | Pointer | Mechanism | Boot-Rendered | Stationarity |
|---|---|---|---|---|---|---|---|
| T-01 | PRODUCER-EXISTS-UNCITED (REGINALD's script) | STATED | N/A | OK-with-caveat (mirror, unverified) | MATCH | NO (would fire via leg-4 quarter-due) | N/A |
| T-02 | NONE (analog exists for peers, not extended to FLG) | PARTIAL | N/A | NO-POINTER | MATCH | NO | N/A |
| T-04 | COMMAND-NAMED (file+column, real data) | STATED | N/A (counted-run, not AND/OR) | OK-with-caveat | MATCH | NO | N/A |
| T-05 | PRODUCER-EXISTS-UNCITED (well-verified upstream) | STATED (rigorously) | N/A | OK | MATCH | NO | N/A |
| T-07 | COMMAND-NAMED | STATED | N/A | OK | MATCH | NO (FLG's own boot doesn't check it) | OK |

**FLG triage: CONVENTION.** The file header's own disclaimer ("NOTHING HERE IS A REGISTERED GATE... wake PROMPTS") is the accurate frame — FLG is pre-live, and every gap above traces to one of two whole-desk facts, not per-row carelessness: (1) FLG's core data (`MI3_FLG.tsv`, the KB chain) is a **one-time mirror of REGINALD's work**, seeded at build and never independently re-pulled or verified by FLG itself (self-disclosed in the file's own header — good transparency, but it means every FLG row inherits REGINALD's refresh cadence, not its own); (2) an EDGAR/8-K filings-monitor pattern already exists and works for REGINALD's structurally-identical cohort (WAL/OZK/EGBN/ZION/VLY) but was never extended to include FLG's own CIK — a one-line fix to a shared script rather than five row rewrites. T-07's finding (FLG's boot doesn't check the live price ladder it's supposed to act on) is the one genuinely PER-ROW/per-gate wiring gap worth a specific fix.

---

## HAWK — `AGENTS/HAWK/workbook/VX.tsv`

**Structural finding that governs every row below:** `AGENTS/HAWK/scripts/boot.py` carries this docstring, verbatim: *"FROZEN 2026-07-09 — NOT wired into the boot protocol; do not invoke as a boot step. Test-run this session (--quick) surfaced internal state that flatly contradicts current STATUS.md... Wiring this in... would inject stale, contradictory data into every boot rather than genuine automation coverage (PAT-034). Disposition: (b) RETIRE."* Its sub-script `oil_infrastructure.py` carries a **hardcoded** `FACILITIES` registry last updated `2026-04-13` (not live-fetched). Its sibling `thresholds.py` DOES pull live Brent via yfinance against $80/$100/$120 scenario bands — a real instrument, but for Brent price only, orthogonal to the 5 sampled event-state rows. **Consequence: BOOT-RENDERED = NO for every row in this file, by an explicit, dated, documented decision — not an oversight.** HAWK's VX.tsv bands are also structurally different from BOND's: most are qualitative geopolitical/policy *states* (e.g. "Production resumes + tankers flowing + FM lifted"), not numeric levels — for this domain PROSE-VALUE is the expected, appropriate instrument class, not automatically decoration. I flag genuine gaps within that context rather than penalizing the qualitative form itself.

### VX-HAWK-IRAQ-01 (L5) — Iraq Oil Production — RED (unchanged)
Bands: Green="Production resumes + tankers flowing + FM lifted" / Yellow="Partial recovery (>2M bpd)" / Orange="Cuts deepening but not full shutdown" / Red="✅ TRIGGERED: FM declared Mar 20 on all foreign fields; no restart Apr 20."

- **(a) INSTRUMENT:** NONE. No script found (grepped `AGENTS/HAWK/scripts`: `oil_infrastructure.py`'s hardcoded facility list does not cover Iraqi fields/Basra). The row is built entirely from manual web sweeps (Al Arabiya, WorldOil, MEForum, SANA) on a stated 45-day re-sweep clock.
- **(b) BASIS/WINDOW:** PARTIAL. The Yellow band names a numeric level (">2M bpd") but no vendor/primary or refresh cadence is attached to *that specific figure* — the row's re-sweep cadence (45 days) governs the whole row's freshness, not this number's sourcing.
- **CONJUNCTION:** N/A (mutually exclusive state bands, not ANDed legs).
- **POINTER:** NO-POINTER (inline primary citations are the row's own resolved sourcing).
- **MECHANISM:** MATCH — row explicitly attributes cause to Hormuz-transit risk (FALCON-theater), not Iraqi domestic failure, and the bands track exactly that transit/restart mechanism.
- **BOOT-RENDERED:** NO (structural, see above).
- **STATIONARITY:** OK — the ">2M bpd" bar is referenced against Iraq's own ~4.5M bpd national capacity (stated elsewhere on the row), a reasonably stable reference frame.

### VX-HAWK-TRADE-01 (L6) — US-China Trade War — YELLOW
Bands: Green="Tariff rollback, deal progress" / Yellow="Status quo" / Orange="New tariffs or rare earth controls" / Red="Full decoupling, retaliation escalation."

- **(a) INSTRUMENT:** PROSE-VALUE — fully qualitative policy-state tracking, no numeric metric exists to instrument. Appropriate for the domain.
- **(b) BASIS/WINDOW:** UNSTATED — no cadence or vendor is named on this specific row (re-sweeps are ad hoc/content-triggered: "[Jul25 RE-SWEPT vs external primaries]" is the only freshness marker, not a scheduled window).
- **CONJUNCTION:** N/A (categorical).
- **POINTER:** NO-POINTER.
- **MECHANISM:** MATCH.
- **BOOT-RENDERED:** NO.
- **STATIONARITY:** N/A.

### VX-HAWK-TRADE-02 (L7) — Broad Tariff Policy — ORANGE (held)
Bands: Green="Trade deals, exemptions" / Yellow="Status quo" / Orange="New country tariffs, auto tariffs" / Red="Comprehensive tariff wall."

- **(a) INSTRUMENT:** PROSE-VALUE, but exceptionally rigorous sourcing method for a qualitative row: named Federal Register doc numbers (Proclamation 11056, FR doc 2026-17294), a CBP CSMS number pulled from a working non-standard fetch path, explicit weekday-audit of every cited date, and independent cross-verification against a parallel MARCO pull with no contact between the two sessions.
- **(b) BASIS/WINDOW:** STATED, thoroughly (dated primaries, explicit "PRIMARY, pulled 2026-08-22 ~17:15-17:35 ET" provenance block).
- **CONJUNCTION:** **This is the headline HAWK finding.** The Orange band text is itself a 2-limb conjunction ("New country tariffs, **auto tariffs**"), and the row's own Notes explicitly diagnose that the two limbs have diverged: *"The COUNTRY-TARIFF limb firmed... the AUTO-TARIFF limb FELL... One limb up, one limb down => Orange remains the honest mark and no band transition is triggered in either direction... the band's two limbs have SEPARATED, which is a reason to re-cut the band text at the next sweep."* This is HAWK self-diagnosing exactly the ambiguous-conjunction failure mode this audit is built to find — correctly reasoned in the moment (a mark held rather than moved on an internal split), but **the band text itself has not been re-cut as of Last_Updated 2026-08-22, and remains unfixed 6 days later as of this audit (2026-08-28).** Gate verdict: CANNOT-FIRE-CLEANLY (a genuine escalation on one limb while the other retreats cannot currently move this row in either direction without a ruling on which limb governs).
- **POINTER:** NO-POINTER (self-contained; routes correction TO other desks, e.g. CARL/MARCO/REGINALD, but carries no incoming pointer of its own).
- **MECHANISM:** MATCH, extensively cross-verified.
- **BOOT-RENDERED:** NO.
- **STATIONARITY:** N/A.

### VX-HAWK-SULPHUR-01 (L8) — Gulf Sulphur → Copper → Grid Chain — RED
Bands (delivered-Kolwezi basis, ruled 2026-08-15): Green="<$200/t" / Yellow="$200-400/t" / Orange="$400-700/t" / Red=">$700/t OR DRC miner force majeure announced."

- **(a) INSTRUMENT:** NONE for the actual scored basis. The row explicitly states the current $900/t delivered-Kolwezi figure is "unchanged since March per KB-HAWK-049" — a ~5-month-old carried value with no live refresh mechanism. The one series HAWK DOES track with any frequency (TradingEconomics Chinese domestic sulfur, 9,535.67 CNY/t) is explicitly disqualified by the row's own text as the wrong perimeter: *"the 9,535.67 CNY/t print is a CHINESE DOMESTIC price... NOT the Dar-es-Salaam-to-Kolwezi basis this row's bands were written on — do not score the bands against it directly."* So the metric that actually scores this RED trigger has no live instrument at all.
- **(b) BASIS/WINDOW:** STATED as a matter of definition (the basis ambiguity was self-caught 8/10 and formally RULED 2026-08-15 at `PROME/proposals/2026-08-12_rule-batch-RULED.md` row 40 — all four bands restated in delivered-Kolwezi terms) — a genuinely well-run correction. But the WINDOW/vintage on the number that basis now applies to is severely stale (~5 months, Argus Media March 2026).
- **CONJUNCTION:** Red is a 2-leg OR: leg 1 ($/t threshold) = fired per the row, on a stale basis (above). Leg 2 (DRC miner force majeure) = explicitly tested and NOT fired ("NO DRC miner force majeure located — the Red band's second limb is UNFIRED," self-disclosed). Gate verdict: **CAN-FIRE** (already fired via leg 1 per the row's own ruling) — but the firing leg's underlying number has not been independently refreshed in ~5 months, which is a live risk that the RED verdict itself may be stale rather than current.
- **POINTER:** OK, lightly checked — `PROME/proposals/2026-08-12_rule-batch-RULED.md` row 40 is cited with enough specificity (named ruling doc + row number + commit-adjacent detail) to be plausible; not deep-verified within this audit's time budget.
- **MECHANISM:** MATCH — cost-push margin-squeeze on SX-EW copper via sulfuric-acid feedstock, consistent with the row's own framing.
- **BOOT-RENDERED:** NO.
- **STATIONARITY:** FIXED-ON-DRIFTING. The row's own evidence records sulfur +269% YoY — i.e., the underlying commodity has moved through a structural regime shift since these $200/$400/$700 bands were set (dated to ~March per KB-HAWK-049), and the bands themselves have not been re-based against the new price regime, only re-based on FCA-vs-delivered *basis* (a units fix, not a levels fix).

### VX-HAWK-CEASEFIRE-01 (L10) — Ceasefire Durability & Countdown — SUPERSEDED
- **(a) INSTRUMENT:** NONE — deliberately, correctly retired ("SUPERSEDED (merged into IRAN-01/DIPLOMACY-01)... Row kept as historical anchor").
- **(b) BASIS/WINDOW:** N/A (historical).
- **CONJUNCTION:** N/A.
- **POINTER:** OK. Traveled to `AGENTS/FALCON/workbook/VX.tsv`: `VX-HAWK-IRAN-01` and `VX-HAWK-DIPLOMACY-01` both exist there, live, actively updated (last touched 2026-07-30), consistent with the file's own top-of-file `#SPLIT-NOTE` (theater rows routed to OSPREY/FALCON 2026-07-12). Target exists, is live, correct series. OK.
- **MECHANISM:** N/A (retired).
- **BOOT-RENDERED:** NO (structural).
- **STATIONARITY:** N/A.

**Verdict on this row: a second clean retirement example**, alongside BOND's VX-BND-09 — correctly marked, cross-referenced, and the routing target verified live.

### HAWK summary table

| Row | Instrument | Basis/Window | Conjunction | Pointer | Mechanism | Boot-Rendered | Stationarity |
|---|---|---|---|---|---|---|---|
| VX-HAWK-IRAQ-01 | NONE (manual) | PARTIAL | N/A | NO-POINTER | MATCH | NO | OK |
| VX-HAWK-TRADE-01 | PROSE-VALUE | UNSTATED | N/A | NO-POINTER | MATCH | NO | N/A |
| VX-HAWK-TRADE-02 | PROSE-VALUE (rigorously sourced) | STATED | **CANNOT-FIRE-CLEANLY — self-diagnosed limb split, unfixed 6 days past its own flagged re-cut** | NO-POINTER | MATCH | NO | N/A |
| VX-HAWK-SULPHUR-01 | NONE (scored basis has no live feed; the live feed it has is disqualified) | STATED (definition) / stale (vintage, ~5mo) | CAN-FIRE (already fired, on a stale number) | OK | MATCH | NO | FIXED-ON-DRIFTING |
| VX-HAWK-CEASEFIRE-01 | NONE (correctly retired) | N/A | N/A | OK (FALCON) | N/A | NO | N/A |

**HAWK triage: CONVENTION (boot-wiring) plus two notable PER-ROW findings.** The dominant, whole-file fact is structural: `boot.py` is explicitly FROZEN and not wired into any boot protocol, so **no HAWK VX row of any kind is boot-rendered** — this is a documented, deliberate decision (correctly made, given the sub-scripts' stale hardcoded data), not an oversight, but it does mean nothing mechanically re-checks any HAWK band against fresh data between manual re-sweeps. Layered on top of that convention, two rows carry real, specific, non-convention defects worth a targeted fix rather than a registry-wide rewrite: **TRADE-02**'s self-diagnosed but still-unfixed limb-split (the Orange band's two conditions have diverged and the band text needs a re-cut, which HAWK itself already proposed and has not yet executed), and **SULPHUR-01**'s ~5-month-stale scoring basis underneath a live RED verdict (the row correctly fixed a units/basis ambiguity in August but never refreshed the underlying price point it was fixing the units of). The two "clean" rows in this sample (IRAQ-01, CEASEFIRE-01) show the qualitative-tracking model works well when kept current.

---

## Cross-desk pattern note (n=20, not a fleet claim)

Consistent with the CONTEXT's prior finding that leg (b) BASIS/WINDOW is where defects concentrate: **11 of 20 rows** in this sample land on PARTIAL or UNSTATED for basis/window (BND-10 partial, BND-16-Y unstated; T2 stated but T4/T10/T12 partial; FLG T-02 partial; HAWK TRADE-01 unstated, IRAQ-01 partial, SULPHUR-01 stale-vintage). By contrast, leg (a) INSTRUMENT more often resolves to a real (if uncited or manual) producer once traveled — the more common failure in this sample is **an instrument existing somewhere in the fleet but not being cited on the row that needs it** (FERT T4/T10, FLG T-01/T-02/T-05, BOND BND-10), rather than no instrument existing anywhere. Two genuinely clean conjunctive gates were found (BND-13, HAWK SULPHUR-01's OR-structure reasoning, though on a stale number) and one clearly still-broken one (HAWK TRADE-02, self-diagnosed). Two exemplary retirements were found (BND-09, HAWK CEASEFIRE-01) — worth citing as the model other desks' dead vectors should follow.

## What this audit could NOT see

- **External sources not fetched.** Per instructions, no live web/API calls were made. All "instrument exists" verdicts rest on reading the producer script's code/docstring in-repo, not on running it to confirm it currently returns a value. A script that compiles and reads correctly could still be broken at runtime (network, auth, upstream schema change) — this audit cannot rule that out for any row.
- **UNCHECKED-EXTERNAL targets.** TreasuryDirect, FRED, FFIEC CDR, EDGAR, ERS, DTN, MOFCOM/NDRC relays, Federal Register, and Advanced Turf/Mosaic IR were all treated as existing/authoritative on the strength of the desks' own citations; none were independently fetched to confirm current content.
- **REGINALD's own boot/session behavior** was read only as far as needed to verify FLG's and HAWK's pointer targets (`VX-REG-6.03`, `mi3_cohort_screen.py`, `8k_monitor.py`, `scripts/market.py`) — I did not audit REGINALD's own rows, its boot wiring, or whether REGINALD's boot would actually notice and route a live breach of `VX-REG-6.03` to FLG. That is a REGINALD-side wiring question this leg was not scoped to answer.
- **ZHAO's TIC instrument** (pointer target for BND-13) was confirmed live and real via its own STATUS.md, but I did not open ZHAO's underlying fetch script to verify it still runs cleanly.
- **PROME/proposals/2026-08-12_rule-batch-RULED.md row 40** (HAWK SULPHUR-01's ruling pointer) was cited but not opened — I judged it plausible from the specificity of the citation (named doc, row number) rather than reading the doc itself.
- **Judgment calls I am less certain of:**
  - Classifying FERT's named-but-unwired URL sources as NONE rather than COMMAND-NAMED is a judgment call on how literally to read "command/script/fetch" — I chose the stricter reading (an executable producer) because FERT's own charter (TRIAGE depth, manual log+flag) makes the distinction between "a human reads a URL" and "a script returns a number" operationally real, not pedantic.
  - HAWK's PROSE-VALUE classifications assume qualitative event-tracking is the *correct* instrument model for a war-risk desk, not a workaround for a missing quantitative one. I believe this is right given the domain, but it is a judgment call, not a scripted determination.
  - I did not attempt to independently verify whether GATE-FERT-G5's 93rd-percentile base-rate claim or HAWK's various primary-document quotations are accurate transcriptions of their underlying sources — I took the desks' own citations at face value where the cited document number/date was internally consistent.
