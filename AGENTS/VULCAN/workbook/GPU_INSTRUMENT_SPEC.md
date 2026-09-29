# GPU-RENTAL PRICE INSTRUMENT — SPEC

**Owner:** VULCAN (PROME coordination ruling, Tier 1, **2026-09-03**; WATT and DEWEY cc, nothing owed by them)
**Status:** 🟢 **PANEL FROZEN 2026-09-13 — `GPU-PANEL-01` is SEALED (§9). CADENCE PRE-COMMITTED · ZERO ROWS WRITTEN — still deliberately: the freeze is NOT a reading, and 2026-09-13 is not a cadence date. First row is reading 2, **2026-09-18 post-close**.**
**2026-09-11:** 🔴 **`GPU-PANEL-01` NOT FROZEN at the 9/11 deadline — READING 1 IS RECORDED AS MISSED** (see §4 addendum). ✅ **PROME's 9/6 AMENDMENT to ruling para. 3 is ENCODED — §3 below and the ruling now AGREE** (①a index LIVE, ①b futures 10/05; `term_normalized` + segment accepted into the registry vocabulary; PROME concurs; cc reached WATT/DEWEY as files) [KB-VULCAN-159].
**Ledger:** `workbook/GPU_SERIES.tsv` (11th ledger; schema declared in `workbook/SCHEMA.tsv`, enforced by `scripts/validate_workbook.py` boot leg 7)
**Register:** `docket/CATALYSTS.tsv` — readings ~~**2026-09-11 · 09-18 · 09-25**~~ (all MISSED) · **10-02** (now the FIRST row) · 🆕 **extension registered 2026-09-29: 10-09 · 10-16 · 10-23 · 10-30 · 11-06 · 11-13 · 11-20 · 11-27** · re-decide **2026-10-05** (rule pre-written in §7a)

---

## 1. Why this instrument exists

DEWEY's `REQ-001` measured a base rate across three historical episodes: **the marginal UNCONTRACTED unit led in 3 of 3; contracted/backlog measures led in 0 of 3.** That finding recommends a spot/on-demand GPU-rental price as a leading instrument on AI-capex demand.

This desk has carried the **compute-spot baseline as a registered open item since 2026-07-22** and already runs the only working instance of DEWEY's finding — DRAM spot on a pre-committed cadence. A GPU-hour is a **compute output price**, with no transmission line into WATT's P1–P4, which is why WATT declined it with reason and both desks independently recommended VULCAN.

---

## 2. 🔴 The one thing that makes this hard, and it inverted my own recommendation

**On 2026-09-03, before PROME ruled, WATT inverted the tier — and the inversion flips the sign.**

| Tier | Move, same window |
|---|---|
| H100 **1-year contract** | **+40%** ($1.70 Oct-25 → $2.35 Mar-26) |
| H100 **on-demand median** | **flat to down** |

**The spot series I had recommended would have read *softening demand* over a window in which contracted pricing rose 40%.**

⇒ **The fix is neither tier. Register BOTH, plus the SPREAD, and publish the PANEL at every reading.**

🔑 **A flat lead against a +40% lag is either a genuine leading divergence or a broken panel, and only the spread-plus-panel distinguishes them.** WATT's own trap warning is the candidate explanation for WATT's own datum: hyperscaler H100 medians run **$6.26–9.34** against marketplace **$1.95–2.58** — **3–6× for the same silicon** — so *"panel composition moves the index more than price does."*

**⚠️ Do not grade either tier alone. No threshold on any level until the panel is stable across ≥3 readings.**

---

## 3. Source order (PROME ruling para. 3) — and what is actually reachable

| Rank | Source | Class | Reconnaissance, 2026-09-06 |
|---|---|---|---|
| **①a** | **Silicon Data daily GPU rental INDEX** (the underlying) | `index_vendor` | 🔴 **LIVE NOW — CORRECTED 2026-09-06.** ⚠️ **My 9/6 row bundled this with the futures and marked the pair "not live until 2026-10-05." That conflated a CONTRACT LISTING with a PUBLISHED SERIES and it was wrong.** The H100 Rental Price Index publishes **daily**, in **USD per GPU-hour**, and a current level is publicly readable on the product page: **$2.53/GPU-hour, ticker `SDH100RT` (NEO-CLOUD reading)** [silicondata.com/products/silicon-index/h100, read 2026-09-06]. ⚠️ **The full series + history + API are PAID** (7-day trial; "distributed via web and API" behind the portal) ⇒ this is a **COST/ACCESS blocker, not a reachability unknown** — a materially different state from SEARCH-NOT-FOUND. |
| **①b** | **CME / Silicon Data GPU-hour FUTURES** | `exchange_primary` | **Not listed until 2026-10-05** (planned launch, pending regulatory review). `cmegroup.com` **TIMED OUT** from this box (2 endpoints) ⇒ **SEARCH-NOT-FOUND: CME spec notice ser-9785, contract codes, settlement method.** Unfetched, **not** unavailable — WATT got a 403 on the same notice. |
| **②** | **ICE / Ornn** — independent second construction | `index_vendor` | 🔴 **CLOSED 2026-09-13 — IT IS LIVE, AND PART OF IT IS FREE.** ~~Specific Ornn index endpoint not yet located — named as unchecked.~~ The **Ornn Compute Price Index (OCPI)** publishes **`OCPI-H100` = $2.78/GPU-hour, settled 2026-09-13**, *"a volume-weighted, winsorized average of transacted GPU rental prices"* settling **once per trading day** [data.ornn.com/preview, own read 2026-09-13]. **Three months of daily history are free**; full history / hourly grain / CSV are paid. ⚠️ **The service condition is NOT stated** — so OCPI enters as `term_normalized`, exactly like `SDH100RT` (§3b). 🔑 **And ICE's futures are tied to OCPI**, which means the 10/05 re-decide now has **two** exchange tracks, not one — see §7. |
| **③** | **LLMTK** — fallback only | `secondary` | Not probed. Fallback tier; probing it before ①/② would invert the order. |
| *(reference)* | **Vast.ai public bundles API** | `marketplace_api` | Resolves **200** and returns real per-GPU-hour asks. ⚠️ **The default endpoint returned 64 offers with n=3 for H100 SXM** — a thin, uncharacterised sample of one marketplace. **That is a candidate panel CELL, never the on-demand tier.** |

---

## 3b. 🔴 SERVICE-CONDITION CORRECTION (2026-09-06, CODEX review — ACCEPTED, mechanism CORRECTED)

**The defect is real and it lands before the freeze, which is the only reason it is cheap.** §5.3 says *"`spot` for on-demand"*, and `price_basis` declares `spot | 1mo | ... | 36mo`. That mapping cannot survive contact with the rank-①a source.

🔴 **CORRECTION TO THIS SECTION, 2026-09-06 (CODEX follow-up, ACCEPTED — and the error is MINE).** This section originally read *"CODEX's mechanism was the opposite of the truth."* **It was not.** CODEX wrote that Silicon Data *"distinguishes on-demand, interruptible spot, and reserved pricing in its methodology explanation"* — which is **exactly what the methodology does**. I restated that as a claim that the vendor *publishes three separate series*, which CODEX never made, and then corrected the stronger claim I had authored for it. ⚠️ **That is impeaching a claim the source did not make** `[[finding_impeachment_must_be_scoped_to_the_claim_not_the_source]]`, **and it ran in the flattering direction** — reading the reviewer as wrong made my own contribution look larger `[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]`. The normalization detail below is a genuine ADDITION to CODEX's flag, not a refutation of it. ~~CODEX's mechanism was the opposite of the truth~~

**What the methodology actually establishes:** the vendor **tracks** on-demand, spot (interruptible) and reserved, and **adjusts heterogeneous observations to a benchmark-equivalent contract before aggregation**, explicitly because *"a short-duration Spot rental in one region is not economically equivalent to a multi-year Reserved contract in another. Blending them directly creates noise rather than insight."* Observations are *"standardized for rental term length, cluster scale, and interconnect"* [silicondata.com/blog/building-a-robust-gpu-index, read 2026-09-06].

🔑 **So the consequence for the instrument is: the index is a TERM-NORMALIZED COMPOSITE whose REFERENCE BASIS HAS NOT BEEN ESTABLISHED.** ⚠️ **SCOPED DOWN 2026-09-06 (CODEX follow-up, ACCEPTED):** this read ~~"it has no single-term basis at all"~~, which is **stronger than the evidence**. The methodology says observations are adjusted to a benchmark-equivalent contract; it does **not publish that contract's complete reference terms.** So the correct statement is *not established*, not *does not exist* — and the difference is live, because if the vendor later publishes the reference terms the row may well have a declarable basis.
- Filing `SDH100RT` as `tier=on_demand, price_basis=spot` would **assert a service condition whose presence has not been established.**
- Worse for the instrument's whole purpose: the **spread** would then subtract a *specific 12-month contract* from a *normalized-across-all-terms* composite — so part of the measured spread would be **Silicon Data's normalization**, not the market. That is the composition trap of §2 re-entering through the units instead of the vendor list.

**Resolutions required in `GPU-PANEL-01` before reading 1 — these are ADDITIONS to §5, not replacements:**
1. **`price_basis` gains `term_normalized`** as a first-class value. ⚠️ **NARROWED 2026-09-06 (CODEX follow-up, ACCEPTED): it is REQUIRED for a row sourced from an index whose reference contract is UNSPECIFIED — which today means Silicon Data's `SDH100RT` — and is NOT a blanket rule for every `index_vendor` row.** ~~any index-vendor row MUST use it~~ generalised ONE vendor's method to indices I have not read, which is the same over-reach in the opposite direction `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`. **Each index vendor is read before its first row; if a vendor DOES publish its reference contract terms, that row declares the real basis.** An index level is not a quoted price and must never silently borrow one's basis.
2. **A `term_normalized` row may not be differenced against a single-term row** to produce `spread_*`. If both sides are not on a declared like-for-like basis, `spread_pct` is `UNGRADEABLE` — which is exactly why that column is typed String.
3. **Segment must be recorded, not just the vendor.** The index publishes **neo-cloud and hyperscaler as separate readings**, and the public ticker is the **NEO-CLOUD** one. §2's 3–6×-for-the-same-silicon dispersion is *already segmented by the vendor* — quoting "Silicon Data" without the segment silently picks one side of the very dispersion this instrument exists to measure.
4. **The paid-access decision is a panel input, not an afterthought:** the free public figure is a single current level with **no history and no audit trail**, on a marketing page whose format can change. A weekly series built from it is reconstructible only going forward. Decide, in the panel spec, whether that is the source of record or a cross-check.

⚠️ **PROME's ruling para. 3 inherited the same futures-vs-index assumption** (it ranks "CME/Silicon Data" as one `exchange_primary` source available at the 10/05 listing). **Corrected back to PROME by packet 2026-09-06** — the correction has to reach the instruction, not just my copy of it `[[finding_ask_which_surface_the_reader_travels_not_where_the_fact_belongs]]`.

---

## 4. 🔴 Why ZERO rows were written on 2026-09-06

A first row taken from an unspecified panel **silently becomes the series' baseline**, and every later reading is then measured against a composition nobody chose. Given §2 — where composition is the *known* dominant term — writing a row from the thin default sample above would have manufactured an instrument rather than built one.

**The cadence was pre-committed anyway, and that ordering is the point:** PROME's ruling para. 3 requires *"cadence pre-committed BEFORE the first row."* Committing the reading dates while zero rows exist is the only moment at which the commitment is provably unselected. It is the same discipline as `semi_watch.py`'s cadence — **whoever chooses the run times chooses the readings [L-21]** — applied one step earlier.

**⚠️ If `GPU-PANEL-01` is not frozen by 2026-09-11, that is a MISSED READING and is recorded as one**, exactly as a missed `semi_watch` slot is. It is not silently deferred.

> 🔴 **ADDENDUM 2026-09-11 — IT WAS NOT FROZEN, AND THIS IS THE RECORD OF THE MISS.** The 9/11 session (PROME-spawned, DOCKET L323: DEWEY REQ-002 integration + a 14-item inbox drain) did not freeze the panel. **Reason, so it is a decision and not a lapse:** §5 item 1 requires a NAMED, FIXED vendor set per tier with the reason each is in, and the **contract tier has no reconnaissance behind it** — which vendors publicly quote a 12-month H100 price, and whether the ICE/Ornn endpoint exists, are both still `SEARCH-NOT-FOUND` (§3). Freezing a panel whose contract tier is unspecified would have minted a `panel_spec_id` from an unspecified composition — **the exact failure this section exists to prevent, on the instrument whose known dominant term is composition.** Recording the miss is cheaper than recording a baseline nobody chose. **What IS done:** PROME's 9/6 amendment is encoded above; `term_normalized`, the segment field and the `UNGRADEABLE` spread rule are settled. **Next:** a dedicated freeze pass BEFORE the 2026-09-18 reading 2 — vendor probes (Lambda / CoreWeave / Nebius / Crusoe reserved-term pages; Vast.ai H100 SXM n≥3; ICE/Ornn), then freeze, then read. If 9/18 is also missed it is recorded the same way. `[[finding_record_of_an_action_is_not_the_action]]` — the record here is of the NON-action, which is the honest half.

---

## 5. What `GPU-PANEL-01` must specify before reading 1

1. **Vendor set per tier** — named, fixed, with the *reason* each is in. Hyperscaler, neocloud and marketplace are three populations, not three quotes.
2. **`gpu_model` set** — H100_SXM at minimum; models are not interchangeable.
3. **`price_basis` set per tier** — ⚠️ **RECONCILED 2026-09-06 (CODEX follow-up): this line said ~~`spot` for on-demand~~ full stop, which §3b now contradicts, and leaving both live is the exact two-live-instructions defect this desk logged on the 55 GW wording one day earlier** `[[finding_correction_beside_an_instruction_leaves_two_live_instructions]]`. **Corrected: `spot` for a DIRECTLY QUOTED on-demand price; `term_normalized` for an index whose reference contract is unspecified (see §3b).** The contract tier must declare its duration (12mo unless stated). **A `term_normalized` row may not be differenced against a single-term row — `spread_pct` is then the literal `UNGRADEABLE`, pending the reference specification.**
4. **Minimum `n_observations` per cell**, below which the cell reports `UNGRADEABLE` rather than a number. *(The `spread_pct` column is typed **String** for exactly this reason — it must be able to hold the literal `UNGRADEABLE` without coercion manufacturing false precision. Same reasoning as `KB.as_of` and `LAYER_SERIES.*_share_pct`.)*
5. **A tie/precision convention** and the basis line required by WQ-162 / `SPEC_LETTER_STANDARD`: **tier · vendor · unit · vintage · precision**.
6. **A zero-free-parameter validation** the row must pass, on the `mag7.py` / `tsmc_watch.py` pattern — and it must **refuse to write** on failure, never degrade silently.

⚠️ **Any later change to the panel mints a NEW `panel_spec_id`.** Old rows keep the old id. A series whose panel drifted silently is measuring its own composition, which is precisely the defect §2 exists to prevent.

---

## 6. Grading discipline (PROME ruling para. 5) — stated as a prohibition

> **NO THRESHOLD IS REGISTERED ON THIS INSTRUMENT AND NONE MAY BE UNTIL ≥4 WEEKLY ROWS EXIST *AND* A BASE RATE IS STATED.**

**PROME set no number. Neither have I.** Reading 4 lands **2026-10-02**, three days before the re-decide — after which the precondition is *met*, not *satisfied*: a base rate must then actually be stated before any number is registered.

---

## 7. The 2026-10-05 re-decide

**CME + Silicon Data list cash-settled Compute Futures on NYMEX (H100 and B200 Rental Index Futures).** At listing, rank ① becomes primary, because **an exchange-settled index is composition-controlled by construction** — that is the date the panel problem becomes *tractable* rather than merely *disclosed*.

🔴 **AMENDED 2026-09-13 — THERE ARE TWO EXCHANGE TRACKS, NOT ONE.** This section assumed CME/Silicon Data was the only one. **ICE's planned GPU futures settle on Ornn's OCPI**, and OCPI is already publishing daily (§3 rank ②, §9.2). So the 10/05 re-decide is no longer *"does rank ① go live?"* — it is **which of two competing exchange-settled constructions becomes primary**, and the two underlying indices **already disagree by 9.4%** on the same silicon (§9.3). 🔑 **That disagreement is the re-decide's real input**, and it is measurable from reading 2 onward at zero cost, which is why `dispersion_D` is in the panel from the first row rather than being discovered on 10/05. ⚠️ **Neither index has published its reference contract**, so an exchange-settled figure is composition-**controlled** by construction without being composition-**disclosed** — those are not the same guarantee, and §2's trap survives the listing in the second form.

⚠️ This listing **supersedes KB-031's 2026-07-22 "NO regulated futures" finding** — correct when asked, overtaken, and **nothing here was watching for the flip.** A resolved binary is a standing bet that the world has not moved, and it expires silently.

---

### 7a. 🔒 THE 10/05 BASIS DECISION — PRE-WRITTEN 2026-09-29 (DOCKET L250), BEFORE READING 4 AND BEFORE EITHER LISTING

**Why now:** on 10/05 the rule must be applied, not chosen. Picking the primary after seeing reading 4 and the listing terms would be picking the answer; today both are unseen.

**Inputs to read ON 10/05, at the primaries, and nothing else:**
- **CME:** contract spec notice ser-9785. Is the contract TRADING (not "approved", not "pending regulatory review")? What is the final-settlement index, and does the spec state the reference contract's **service condition** (commitment term, on-demand vs reserved, segment, cluster scale)?
- **ICE:** are futures settled on Ornn's compute price index (OCPI) trading? Does OCPI's methodology document state the same service condition?
- ⚠️ `cmegroup.com` timed out from this box on 9/06. If it still does, the input is **UNFETCHED, not absent**, and R-A below reads "not established".

| Rule | Letter |
|---|---|
| **R-A: listing changes CLASS only when trading.** | A source moves to `source_class=exchange_primary` only once its contract is **trading**. Announced, approved or pending does not count ⇒ no change, and the re-decide **re-dates to the announced first trade date**, registered only once that date is announced. |
| **R-B: listing changes BASIS only on DISCLOSURE.** | Exchange settlement controls a figure's **vintage and manipulation surface**. It does **not** disclose its **composition** (§7). A construction leaves `price_basis=term_normalized` **only** if the exchange spec or index methodology names the reference contract's service condition ⇒ `spot` or a term (`1mo` … `36mo`). Without that, **R4 stands**: never differenced against a tier-A or tier-B row. |
| **R-C: ranking constructions that pass A+B.** | ① a basis that **fills or matches a gradeable tier**: a disclosed **`12mo`** construction ranks FIRST, because it re-opens tier C and with it the on-demand-minus-contract spread §2 was built for; a disclosed `spot` construction is next, because it is comparable to tier A/B · ② **transacted** prices over **asks/quotes**, where the methodology states which (OCPI states transacted; SDH100RT's construction is **not established here — not assumed either way**) · ③ daily settlement readable at no cost (a paywall is a recorded COST blocker, not "unreachable"). |
| **R-D: a tie gives no single primary.** | Both stay as tier-D cells; `dispersion_D` stays the diagnostic. **Never average the two into one figure.** |
| **R-E: one passes.** | It becomes primary **for its declared basis only**; the other stays as the `dispersion_D` cross-check. |
| **R-F: neither passes.** | **No primary.** Both stay tier-D `term_normalized`. A trading contract's **settlement price** may be ADDED as its own tier-D cell (`instrument=futures`, `source_class=exchange_primary`, `price_basis=term_normalized`). That adds a settlement guarantee, **not** a composition guarantee, and it is never differenced against a single-term row. |
| **R-G: no threshold on 10/05, under any branch.** | §6 stands: ≥4 weekly rows AND a stated base rate. With 9/11 · 9/18 · 9/25 all MISSED, **reading 4 (10/02) is the FIRST row** ⇒ the earliest 4-row point is **10/23**, on the cadence extension registered today (below). |
| **R-H: a panel change re-bases by NAME.** | Any change to tier-D membership or basis from this decision ships as **`GPU-PANEL-02`**, stamped on every row from its first reading. Never a silent edit to `GPU-PANEL-01`. |

**Expected branch, written before the fact so it cannot be mistaken for news: R-F**, or R-A if CME's contract is not yet trading.
- On 9/13 neither index published its reference contract (§9.3, §9.4).
- CME's listing was "pending regulatory review" as of the 9/29 news sweep.
- ⇒ The most likely 10/05 outcome is **no change of primary, possibly one added settlement cell.** That is a real decision, not a deferral: a listing that controls composition without disclosing it does not buy the composition guarantee the instrument needs.

**🔴 CADENCE EXTENSION: REGISTERED TODAY, NOT ON 10/05.** The registered cadence ends at **10/02**, and that reading is now the first row. Renewing after seeing reading 4 would be selecting the series. By this desk's renewal rule (extend **before** the last committed slot fires; see `mag7.py` in `CLAUDE.md`), the extension is registered **2026-09-29**. **Eight post-close Fridays: 10/09 · 10/16 · 10/23 · 10/30 · 11/06 · 11/13 · 11/20 · 11/27**, sharing the `mag7.py` Friday slot. It is independent of the basis decision: R-H governs which panel the rows carry, not whether they are taken. *(This supersedes my own note an hour earlier in the 9/25 register row, which had "put the extension to the 10/05 re-decide". That would have placed the renewal after reading 4 and broken the renewal rule. Corrected before it was acted on.)*

## 8. Provenance

- **PROME ruling** 2026-09-03 07:3x ET — `inbox/2026-09-03_from-PROME_RULED-you-own-the-GPU-rental-price-instrument...`
- **WATT tier inversion** 2026-09-03 (`b325bc906`) · **VULCAN amendment filed BEFORE PROME ruled** (`d932b817b`) — the loop closed at the decision, not after it
- **DEWEY REQ-001** base rate — `AGENTS/DEWEY/output/2026-09-02_dr-req001-ai-order-book-phantom-demand.md`
- KB-031 (superseded binary) · KB-144 (CME listing) · KB-148 (the FX/reproducibility discipline that applies to any foreign-currency quote entering this panel)

---

## 9. 🟢 `GPU-PANEL-01` — **FROZEN 2026-09-13** (the dedicated freeze pass §4's addendum demanded)

**Frozen:** 2026-09-13, **freeze commit `d437a068d` at 20:29:43 ET** (git commit time — the only clock on this record that was machine-taken). ~~*~20:2x–21:0x ET*~~ **RE-STAMPED 2026-09-25 per PROME's 9/13 receipt §3:** the narrative stamp ran up to ~80 min AHEAD of the wall clock (the whole session sat inside ~20:25–20:35 ET). **The STAMP is amended; the SEAL is not reopened** — §9.1's integrity claim is an ORDERING claim (criteria to disk before the first fetch), and the ordering is unaffected. PROME-spawned Tier-1 session (DOCKET **L330**, dated 2026-09-11, COVERED annotations all SPENT). **Markets closed since the Fri 2026-09-11 close.**
**`panel_spec_id` = `GPU-PANEL-01`.** Any later change to §9.3 mints a NEW id; old rows keep the old one (§5 closing rule).
**What unblocked it:** the 9/11 addendum named ONE blocker — *the contract tier has no reconnaissance behind it.* That reconnaissance was run this session (§9.2). **It returned a negative, and the negative is the finding (§9.4).** A panel cannot wait forever on a tier that does not publicly exist.

### 9.1 Inclusion criteria — **DECLARED BEFORE THE FIRST FETCH OF THIS SESSION**

⚠️ **Ordering is the integrity claim here, so it is stated plainly:** these criteria were written to disk **before any vendor page was fetched** this session, precisely so the panel cannot have been selected on observed levels. `[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]` — a freeze performed after seeing the prices is exactly the composition-selection defect §2 exists to prevent, and the only defence is the timestamp.

A vendor/tier **cell** enters `GPU-PANEL-01` iff **all** of:

| | Criterion |
|---|---|
| **C1** | **PUBLICLY QUOTED** — a per-GPU-hour price readable with no login, no contract and no sales contact, at a stable URL. |
| **C2** | **MODEL-IDENTIFIED** — the quote names **H100 SXM (80GB)**, or the vendor states a form factor that maps to it under §9.3's declared mapping. A bare "H100" ambiguous with PCIe fails. |
| **C3** | **SERVICE CONDITION DECLARABLE** — on-demand (uninterruptible, pay-as-you-go) or a **committed term with a stated DURATION**. A price whose service condition cannot be declared is **EXCLUDED, not guessed** (§3b). |
| **C4** | **POPULATION-LABELLED** — assignable to exactly ONE of {hyperscaler, neocloud, marketplace, index} (§5.1: three populations, not three quotes). |
| **C5** | **REPRODUCIBLE IN USD** — same URL returns the same units; quoted in USD, no FX conversion [KB-148]. |

**Rules over the criteria:**
- **R1** Tier assignment is by **SERVICE CONDITION**, never by vendor identity.
- **R2** 🔴 **The observed PRICE LEVEL is NEVER an inclusion input.** Cells are admitted or excluded on C1–C5 alone.
- **R3** Every exclusion is recorded **with the failed criterion**. No silent drops — an unrecorded exclusion is indistinguishable from a vendor that does not exist.
- **R4** An index whose **reference contract is unspecified** enters as `price_basis=term_normalized` and **may not be differenced** against a single-term row (§3b resolution 2).
- **R5** A tier below its declared minimum `n` reports the literal **`UNGRADEABLE`**, never a number.

### 9.2 Reconnaissance record — 2026-09-13, own reads

> 🔴 **THIS IS NOT A SERIES ROW AND MUST NEVER BE READ AS ONE.** `GPU_SERIES.tsv` still holds **zero data rows**. These are composition evidence: what the panel *looked like* at the moment it was sealed, recorded so a future reader can audit the freeze. The first series row is **reading 2, 2026-09-18 post-close**.

| Tier | Vendor | Quote as read | Basis | Verdict |
|---|---|---|---|---|
| A on-demand | **Lambda** H100 **SXM** 80GB, 8× node | **$3.99**/GPU-hr (1× $4.29 · 2× $4.19 · 4× $4.09) | on-demand, self-serve | ✅ **IN** |
| A on-demand | **CoreWeave** HGX H100, 8-GPU node | **$49.24**/node-hr ⇒ **$6.1550**/GPU-hr | on-demand | ✅ **IN** |
| A on-demand | **Nebius** HGX H100 | **$3.85**/GPU-hr (preemptible $2.15, separate) | on-demand | ✅ **IN** |
| A on-demand | **Crusoe** H100 80GB HGX | **$3.90**/GPU-hr | on-demand | ✅ **IN** |
| B marketplace | **Vast.ai** H100 SXM, 1-GPU rentable | **n=10**; min $1.7356 · **median $1.8689** · max $4.5471 | live asks, public API | ✅ **IN** |
| C contract 12mo | — | — | — | 🔴 **EMPTY — see §9.4** |
| D index | **Silicon Data** `SDH100RT` (**NEO-CLOUD** segment) | **$2.53**/GPU-hr; page publishes **no as-of date** ⇒ vintage `UNSPECIFIED` | `term_normalized` | ✅ **IN** |
| D index | **Ornn** `OCPI-H100` | **$2.78**/GPU-hr, **settled 2026-09-13** | `term_normalized` | ✅ **IN** |

*Sources, all own reads 2026-09-13: lambda.ai/pricing · coreweave.com/pricing · nebius.com/prices · crusoe.ai/cloud/pricing · console.vast.ai public bundles API · silicondata.com/products/silicon-index/h100 · data.ornn.com/preview.*

**One more thing the reconnaissance measured, recorded because it is WATT's warning arriving as a number:** the neocloud list mean **$4.4737** against the Vast.ai marketplace median **$1.8689** is **~2.4× for the same silicon** — WATT's *"3–6× for the same silicon … panel composition moves the index more than price does"* is no longer a caution, it is a measurement, and it is why tiers `on_demand` and `marketplace` are **never netted**. ⚠️ Still NOT a series row.

**Median convention applied, not assumed:** Vast.ai's 10 sorted asks give middle values $1.8689 and $2.0022. Under §9.6's declared **lower-of-the-two-middle** rule the median is **$1.8689**; a float average would print **$1.93555**. *The convention exists so a decimal series is never decided by float* `[[finding_float_precision_empties_the_tie_set_and_voids_the_operator]]`.

### 9.3 🔒 THE FROZEN PANEL

**`gpu_model` (all tiers): `H100_SXM` (80GB) only.** Models are not interchangeable (§5.2).

**Declared form-factor mapping (a convention, recorded so it can be overturned, not an inference left implicit):** a vendor quote reading **"HGX H100 80GB"** maps to `H100_SXM` — the HGX baseboard carries SXM5 modules. A quote reading bare **"H100"** with no form factor and no HGX label does **not** map and fails C2.

🔗 **Letter → ledger token binding (so the spec and `GPU_SERIES.tsv` speak ONE vocabulary):** **A = `tier=on_demand`** · **B = `tier=marketplace`** · **C = `tier=contract`** · **D = `tier=index`**. ⚠️ **`marketplace` and `index` did not exist in the `tier` enum before this freeze** — `SCHEMA.tsv` carried only `on_demand | contract | spread`, which could not express the panel without merging a marketplace ask into a neocloud list price. **The enum was widened in the same pass** (and `source_class` gained `vendor_primary`, because a vendor’s own price page is a primary, not a secondary). The letters are for reading; **the tokens are what the ledger stores.**

| Tier | Population | `price_basis` | Frozen member set | Min `n` | Rule |
|---|---|:---:|---|:---:|---|
| **A** | neocloud, **directly quoted** | `spot` | Lambda · CoreWeave · Nebius · Crusoe | **3 of 4** | **Scale convention: take the 8-GPU / single-node quote** where a vendor publishes several scales — 8×SXM is one HGX baseboard, which is the physical unit the other three quote. Report the **mean** across admitted vendors and **also** the member list. |
| **B** | marketplace | `spot` | Vast.ai, H100 SXM, **1-GPU rentable** offers | **5 offers** | Report the **median** under §9.6's tie rule. **NEVER netted into tier A** — it is a different population (§3 reference row). |
| **C** | committed term, 12mo | `12mo` | 🔴 **EMPTY SET** | — | Writes an **`ERR:` sentinel** every reading, with the reason, until a member qualifies under C1–C5. §9.4. |
| **D** | index vendors | `term_normalized` | Silicon Data `SDH100RT` (neo-cloud) · Ornn `OCPI-H100` | **1** (2 for the cross-check) | Each index is read **for its own reference basis before its first row** (§3b res. 1). Both are currently **unspecified** ⇒ both `term_normalized`. **Segment is recorded, never just the vendor** (§3b res. 3). |

**Spreads permitted at this freeze — and the one that is not:**
- ✅ `spread_A_minus_B` — neocloud list vs marketplace ask. **Both legs are `spot`**, so it is like-for-like and gradeable.
- ✅ `dispersion_D` — `|OCPI-H100 − SDH100RT| ÷ their mean`. At freeze: **$2.78 vs $2.53 ⇒ 9.4%** (mean basis; 9.0% on the higher leg, 9.9% on the lower — the basis is named because the three differ).
- ⛔ **`spread_on_demand_minus_contract` — the spread §2 says the whole instrument is for — is `UNGRADEABLE` and will stay so while tier C is empty.** It may **never** be faked by differencing a tier-A row against a tier-D `term_normalized` index (R4). Part of that difference would be the vendor's own normalization, which is §2's composition trap re-entering through the units.

### 9.4 🔴 THE FINDING THE RECONNAISSANCE ACTUALLY RETURNED

**There is no publicly quoted 12-month H100 contract price. Not at one vendor — at any of the four.**

| Excluded cell | Failed |
|---|---|
| **Lambda** 1-Click Clusters — $6.16 (16 GPU) / $5.85 (64) / $5.54 (256) | **C3**: the term is *"2 weeks – 1 year"*. **A duration RANGE is not a duration.** Second defect: the price moves with cluster scale, an uncontrolled axis. **1 year+ = "contact sales" ⇒ also C1.** |
| **CoreWeave** reserved — *"up to 60% discounts"* | **C1** — contact sales; no number published. |
| **Crusoe** committed rates | **C1** — contact sales. |
| **Nebius** | **C1** — no committed tier published at all. |
| **SemiAnalysis** 1-yr H100 series — **$1.70 (Oct-2025) → $2.35 (Mar-2026), the +40%** | **C1** — paid research, not a public quote. ⚠️ **This is the NAMED unreachable, not an absence** `[[finding_a_named_unchecked_fallback_makes_an_absence_closable]]`. |

🔑 **And this closes a provenance question that has been open since 2026-09-03: WATT's tier-inverting datum — H100 1-year contract +40% while on-demand was flat-to-down — traces to SemiAnalysis, a third-party research vendor, NOT to any vendor price page.** That does not impeach it. It establishes that **the contract leg of this instrument is not independently reproducible by this desk from public sources**, which is a different and more useful statement than "we haven't found it yet." `[[finding_declared_data_wall_needs_fleet_memory_check]]` — at four vendors returning the same negative, the finding is **ACCESS, not data**.

⚠️ **Consequence, stated so it cannot be quietly forgotten:** the instrument as conceived in §2 — *register both tiers plus the spread* — **is at freeze a ONE-TIER instrument plus two index composites.** The spread that was supposed to distinguish "genuine leading divergence" from "broken panel" **cannot be computed.** What replaces it until tier C fills: **`dispersion_D`, two independently constructed indices over the same silicon.** They disagree by **9.4%** on day one, which is precisely the panel-stability diagnostic §2 asked for, arriving from a different direction.

### 9.5 Minimum `n`, precision, tie convention, basis line

- **Min `n`:** tier A **3 of 4 vendors** · tier B **5 offers** · tier D **1 index** (both for `dispersion_D`). 🔴 **Below the floor, WHAT IS WRITTEN DEPENDS ON THE COLUMN’S TYPE, and getting this wrong would fail boot leg 7 on the first row:** `price_usd` is a **required Float** and **blank is forbidden**, so an ungradeable cell writes an **`ERR:` sentinel** there — the same honest-failure convention `S2_SERIES.tsv` already carries (`ERR:` values are skipped by `validate_workbook.py`, so they fail LOUD in the ledger without failing the schema) [L-16]. `n_observations` is a required Integer ≥ 1, so a zero-cell writes `ERR:` there too — **never `0`**. **`spread_pct` is the one column typed String on purpose, and it takes the literal `UNGRADEABLE`** (§5.4).
- **Precision:** a **quoted** price is recorded **exactly as quoted** and never re-rounded. A **derived** price (node ÷ GPU count, medians, spreads) carries **4 decimal places**, and the divisor is written into `notes`.
- **Tie / median convention:** for an even `n`, the median is the **LOWER of the two middle values**. Deterministic, exact on a decimal series, no float average.
- **Basis line** (WQ-162 / `SPEC_LETTER_STANDARD`), required in `notes` of every row: **tier · vendor(s) · unit · vintage · precision**. A tier-D row's vintage is the **settlement date**, and `UNSPECIFIED` where the vendor publishes none (`SDH100RT` today).

### 9.6 Validations — **refuse to write, never degrade silently** (§5.6)

| | Validation | On failure |
|---|---|---|
| **V1** | **Unit** — every price is USD per **GPU**-hour. A per-node quote is divided by the node's stated GPU count and the divisor is recorded. | **REFUSE** |
| **V2** | **Model** — `gpu_model == H100_SXM`, via a direct SXM quote or §9.3's declared HGX mapping. | **REFUSE** |
| **V3** | **Tier purity** — no tier mixes `price_basis` values across its member cells. | **REFUSE** |
| **V4** | **Spread gate** — `spread_pct` is written ONLY when both legs carry an **identical declared** `price_basis`; otherwise the literal `UNGRADEABLE`. | write `UNGRADEABLE` |
| **V5** | **n-floor** — a cell under §9.5's floor reports `UNGRADEABLE`. | write `UNGRADEABLE` |
| **V6** | **Index cross-check** — compute `dispersion_D` and record it **every reading**. | **record, no band** |

⚠️ **V6 sets NO number, and that is deliberate.** §6 forbids any threshold on this instrument until ≥4 weekly rows exist *and* a base rate is stated. A dispersion band picked tonight would be a free parameter chosen from a sample of one. **`dispersion_D` is measured from reading 2 and its own base rate is stated at reading 4 (2026-10-02) — after which a band may be *proposed*, not assumed.**

### 9.7 What reading 2 executes (2026-09-18, post-close)

1. `.venv/bin/python tools/gpu_panel.py` — fetches tier B live, takes tiers A and D from a declared input, runs V1–V6, and **refuses to append** on any REFUSE.
2. Tier C (`contract`) writes **`ERR:UNGRADEABLE-no-public-contract-quote`** in `price_usd` and `n_observations`, with the §9.4 reason in `notes`. **It is not left blank** — a blank cell passes every presence audit `[[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]]`.
3. Re-confirm both tier-D levels **at their own pages**, and record whether `data.ornn.com/preview` is still the reachable surface — a **preview** page is not yet established as a source of record, and that is an open question this freeze does not close.
4. **If 9/18 is missed it is recorded as a missed reading**, exactly as 9/11 was. The freeze removes the *reason* for a miss; it does not excuse one.

### 9.8 What this freeze does NOT do

**No threshold registered. No band set. No score moved. No capital path.** `GPU_SERIES.tsv` holds **zero rows** and will until 2026-09-18 post-close. The freeze is a **composition decision**, and its most important content is a **negative** — that one of its two designed tiers has no public members.
