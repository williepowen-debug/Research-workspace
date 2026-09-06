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
| **①** | **CME / Silicon Data GPU-hour futures + the underlying daily rental index** | `exchange_primary` | **Not live until 2026-10-05.** `cmegroup.com` **TIMED OUT** from this box (2 endpoints) ⇒ **SEARCH-NOT-FOUND: CME spec notice ser-9785, contract codes, settlement method.** Unfetched, **not** unavailable — WATT got a 403 on the same notice. `silicondata.com` root resolves **200** and advertises an API (16 mentions); no public index endpoint found at `/index` (404). |
| **②** | **ICE / Ornn** — independent second construction | `index_vendor` | `ice.com/products` resolves **200**. Specific Ornn index endpoint **not yet located** — named as unchecked. |
| **③** | **LLMTK** — fallback only | `secondary` | Not probed. Fallback tier; probing it before ①/② would invert the order. |
| *(reference)* | **Vast.ai public bundles API** | `marketplace_api` | Resolves **200** and returns real per-GPU-hour asks. ⚠️ **The default endpoint returned 64 offers with n=3 for H100 SXM** — a thin, uncharacterised sample of one marketplace. **That is a candidate panel CELL, never the on-demand tier.** |

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
