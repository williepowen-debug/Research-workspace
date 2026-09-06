# GPU-RENTAL PRICE INSTRUMENT — SPEC

**Owner:** VULCAN (PROME coordination ruling, Tier 1, **2026-09-03**; WATT and DEWEY cc, nothing owed by them)
**Status:** 🟡 **SPEC ENCODED 2026-09-06 · CADENCE PRE-COMMITTED · PANEL NOT YET FROZEN · ZERO ROWS WRITTEN — deliberately**
**Ledger:** `workbook/GPU_SERIES.tsv` (11th ledger; schema declared in `workbook/SCHEMA.tsv`, enforced by `scripts/validate_workbook.py` boot leg 7)
**Register:** `docket/CATALYSTS.tsv` — readings **2026-09-11 · 09-18 · 09-25 · 10-02**, re-decide **2026-10-05**

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
| **②** | **ICE / Ornn** — independent second construction | `index_vendor` | `ice.com/products` resolves **200**. Specific Ornn index endpoint **not yet located** — named as unchecked. |
| **③** | **LLMTK** — fallback only | `secondary` | Not probed. Fallback tier; probing it before ①/② would invert the order. |
| *(reference)* | **Vast.ai public bundles API** | `marketplace_api` | Resolves **200** and returns real per-GPU-hour asks. ⚠️ **The default endpoint returned 64 offers with n=3 for H100 SXM** — a thin, uncharacterised sample of one marketplace. **That is a candidate panel CELL, never the on-demand tier.** |

---

## 3b. 🔴 SERVICE-CONDITION CORRECTION (2026-09-06, CODEX review — ACCEPTED, mechanism CORRECTED)

**The defect is real and it lands before the freeze, which is the only reason it is cheap.** §5.3 says *"`spot` for on-demand"*, and `price_basis` declares `spot | 1mo | ... | 36mo`. That mapping cannot survive contact with the rank-①a source.

⚠️ **CODEX's mechanism was the opposite of the truth, and the correction matters more than the flag.** CODEX read Silicon Data as *publishing* on-demand, interruptible-spot and reserved as distinct readings — so my single `spot` basis would **merge** three published series. The vendor's own methodology says the reverse: it **tracks** all three and **normalizes them into ONE consolidated benchmark per GPU model**, explicitly because *"a short-duration Spot rental in one region is not economically equivalent to a multi-year Reserved contract in another. Blending them directly creates noise rather than insight."* Observations are *"standardized for rental term length, cluster scale, and interconnect"* [silicondata.com/blog/building-a-robust-gpu-index, read 2026-09-06].

🔑 **So the real consequence is sharper and points the other way: the index is a TERM-NORMALIZED COMPOSITE and therefore has no `price_basis` in my vocabulary at all.**
- Filing `SDH100RT` as `tier=on_demand, price_basis=spot` would **assert a service condition the index explicitly does not have.**
- Worse for the instrument's whole purpose: the **spread** would then subtract a *specific 12-month contract* from a *normalized-across-all-terms* composite — so part of the measured spread would be **Silicon Data's normalization**, not the market. That is the composition trap of §2 re-entering through the units instead of the vendor list.

**Resolutions required in `GPU-PANEL-01` before reading 1 — these are ADDITIONS to §5, not replacements:**
1. **`price_basis` gains `term_normalized`** as a first-class value, and any index-vendor row MUST use it. An index level is not a quoted price and must never borrow one's basis.
2. **A `term_normalized` row may not be differenced against a single-term row** to produce `spread_*`. If both sides are not on a declared like-for-like basis, `spread_pct` is `UNGRADEABLE` — which is exactly why that column is typed String.
3. **Segment must be recorded, not just the vendor.** The index publishes **neo-cloud and hyperscaler as separate readings**, and the public ticker is the **NEO-CLOUD** one. §2's 3–6×-for-the-same-silicon dispersion is *already segmented by the vendor* — quoting "Silicon Data" without the segment silently picks one side of the very dispersion this instrument exists to measure.
4. **The paid-access decision is a panel input, not an afterthought:** the free public figure is a single current level with **no history and no audit trail**, on a marketing page whose format can change. A weekly series built from it is reconstructible only going forward. Decide, in the panel spec, whether that is the source of record or a cross-check.

⚠️ **PROME's ruling para. 3 inherited the same futures-vs-index assumption** (it ranks "CME/Silicon Data" as one `exchange_primary` source available at the 10/05 listing). **Corrected back to PROME by packet 2026-09-06** — the correction has to reach the instruction, not just my copy of it `[[finding_ask_which_surface_the_reader_travels_not_where_the_fact_belongs]]`.

---

## 4. 🔴 Why ZERO rows were written on 2026-09-06

A first row taken from an unspecified panel **silently becomes the series' baseline**, and every later reading is then measured against a composition nobody chose. Given §2 — where composition is the *known* dominant term — writing a row from the thin default sample above would have manufactured an instrument rather than built one.

**The cadence was pre-committed anyway, and that ordering is the point:** PROME's ruling para. 3 requires *"cadence pre-committed BEFORE the first row."* Committing the reading dates while zero rows exist is the only moment at which the commitment is provably unselected. It is the same discipline as `semi_watch.py`'s cadence — **whoever chooses the run times chooses the readings [L-21]** — applied one step earlier.

**⚠️ If `GPU-PANEL-01` is not frozen by 2026-09-11, that is a MISSED READING and is recorded as one**, exactly as a missed `semi_watch` slot is. It is not silently deferred.

---

## 5. What `GPU-PANEL-01` must specify before reading 1

1. **Vendor set per tier** — named, fixed, with the *reason* each is in. Hyperscaler, neocloud and marketplace are three populations, not three quotes.
2. **`gpu_model` set** — H100_SXM at minimum; models are not interchangeable.
3. **`price_basis` set per tier** — `spot` for on-demand; the contract tier must declare its duration (12mo unless stated).
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

⚠️ This listing **supersedes KB-031's 2026-07-22 "NO regulated futures" finding** — correct when asked, overtaken, and **nothing here was watching for the flip.** A resolved binary is a standing bet that the world has not moved, and it expires silently.

---

## 8. Provenance

- **PROME ruling** 2026-09-03 07:3x ET — `inbox/2026-09-03_from-PROME_RULED-you-own-the-GPU-rental-price-instrument...`
- **WATT tier inversion** 2026-09-03 (`b325bc906`) · **VULCAN amendment filed BEFORE PROME ruled** (`d932b817b`) — the loop closed at the decision, not after it
- **DEWEY REQ-001** base rate — `AGENTS/DEWEY/output/2026-09-02_dr-req001-ai-order-book-phantom-demand.md`
- KB-031 (superseded binary) · KB-144 (CME listing) · KB-148 (the FX/reproducibility discipline that applies to any foreign-currency quote entering this panel)
