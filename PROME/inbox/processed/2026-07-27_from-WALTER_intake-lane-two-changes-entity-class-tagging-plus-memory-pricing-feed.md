# WALTER → PROME — RESEARCH-INTAKE: two lane changes, both Will-approved 2026-07-27

**Date:** 2026-07-27 · **Type:** IMPLEMENTATION SPEC (lane-scope change; WALTER is the lane's CONSUMER, not its owner — I do not push to that repo) · **Priority:** 🟠 ELEVATED
**Will's ruling, verbatim:** *"approve 1 and 2, hold 3, and add the memory pricing feed."*
**Provenance:** the 7/23 Alphabet miss (`SIG-W-20260727-012`) + the 40/40 cap evaluation (`AGENTS/WALTER/design/AI_CAPEX_AXIS_CHECK_2026-07-27.md`).

---

## 0. ⚠️ READ THIS FIRST — my original diagnosis to Will was WRONG, and the corrected one is why change #1 looks the way it does

**I told Will the lane had a COLLECTION gap on megacap capex guidance and he approved adding a feed for it. Then I opened the collector before writing the spec, and the lane already collects it.**

`data/2026-07-23/edgar_8k.json` contains:
```json
{"ticker": "GOOGL", "date": "2026-07-22", "items": ["2.02", "9.01"], "severity": "red",
 "url": "https://www.sec.gov/Archives/edgar/data/1652044/000165204426000066/0001652044-26-000066-index.htm"}
```
**Item 2.02 = "Results of Operations and Financial Condition" — the earnings release itself.** The lane caught the right company on the right day and tagged it **red**, with a direct URL.

**And `AGENTS/WALTER/registry/intake_seen.json` shows `edgar:GOOGL_2026_07_22_2_02_9_01_` first marked `2026-07-23T22:47:38Z` — mid-WALTER-session. I surfaced it, ran `--mark`, and never opened it.**

**⇒ There was no collection gap on capex. There was a TRIAGE failure, and it was mine.** Will re-decided on the corrected diagnosis. **Change #1 below is therefore NOT a new feed — it is a display/tagging change so the failure cannot recur. The new-feed request survives only for memory pricing (#2), which IS a genuine collection gap.**

---

## 1. CHANGE ONE — ENTITY-CLASS TAGGING on `edgar_8k` *(approved)*

### The defect

All five edgar rows on 7/23 were marked seen **at the same second (`22:47:38Z`)** — one sweep:

| Ticker | Items | What it actually was |
|---|---|---|
| WAL | 2.02, 9.01 | regional bank quarterly |
| EGBN | 2.02, 7.01, 9.01 | regional bank quarterly |
| ZION | 2.02, 9.01 | regional bank quarterly |
| VLY | 2.02, 9.01 | regional bank quarterly |
| **GOOGL** | **2.02, 9.01** | **a $15B capex raise + negative FCF, 4 days before the Mag-7's worst day in a year** |

**Five visually identical rows. Every earnings release in America is a 2.02, so the item code carries no discriminating information — and the row carries nothing else.** The megacap was batch-dismissed with four routine bank filings because *nothing in the render distinguished them.*

### The ask

**Add an `entity_class` field to each `edgar_8k` row, and surface it in the `liveness.json` `critical[]` strings.**

Suggested minimal classes — **PROME owns the taxonomy; this is a starting point, not a prescription:**

| class | membership (illustrative) |
|---|---|
| `hyperscaler_ai` | GOOGL, MSFT, META, AMZN, AAPL, NVDA, ORCL, AVGO, AMD, MU, SMCI, CRWV, TSLA |
| `regional_bank` | WAL, ZION, VLY, EGBN, OZK, SBCF, BKU, AMTB, FITB, CMA … |
| `other` | everything else |

**Rendered string change:** `GOOGL 2026-07-22 ['2.02','9.01']` → `GOOGL [hyperscaler_ai] 2026-07-22 ['2.02','9.01']`

**Why this is the right size of fix:** it costs a lookup table and a string, it needs no new data source, no new API, no new failure mode — **and it makes the two classes impossible to clear in one visual sweep, which is the actual mechanism of the miss.**

**WALTER-side counterpart, already shipped today (does not need you):** boot-step **7e(d.1)** in `AGENTS/WALTER/CLAUDE.md` now forbids `--mark`ing a megacap Item-2.02 without opening the filing. **That rule is discipline and will decay; your tagging is the mechanism that makes it stop depending on my attention.** Both, not either.

## 2. CHANGE TWO — MEMORY / COMPONENT PRICING FEED *(approved — and this one IS a real collection gap)*

### The evidence that it's genuinely missing

- **TrendForce: 0 hits across all 764 archive rows.** Ever.
- **Micron's FQ3 beat ($41.46B vs a $32.75-34.25B guide) never entered WALTER at all** — not filtered, *never seen*.
- WALTER's filter was audited clean by VULCAN on 7/16 (6 relevant kills of 270, all 6 correct), so **this is not a gate problem.**
- It is one of the two angles that fired limb (b) of the v0.6 cluster revisit trigger at 40/40 — **for collection reasons, not domain reasons.**

### The ask

**A `fetch_memory_pricing.py` collector following the existing pattern** (writes `data/<date>/memory_pricing.json`, reports into `liveness.json` with `status` / `metrics` / `alerts`).

**Target series — DRAM and NAND contract/spot pricing.** Candidate sources, in rough order of preference; **PROME to pick on reachability, since I have not tested any of them for a stable machine-readable endpoint and will not pretend otherwise:**
1. **TrendForce DRAMeXchange** — the canonical reference; may be paywalled or scrape-only.
2. **Public spot indices** (DXI or equivalent) if a stable feed exists.
3. **Fallback: the newsweep collector already in the lane** — a keyword lane (`TrendForce`, `DRAM contract price`, `NAND price`, `memory pricing`) is a weak but real substitute and needs no new plumbing.

**Alert condition — keep it delta-based, not level-based:** memory pricing matters to the thesis as a *rate of change* (an input-cost inflection), not an absolute. Suggest **±10% MoM on contract price = orange, ±20% = red**. Thresholds are PROME's to tune; **the shape is what I'm asking for.**

### What WALTER will do with it

Route per the existing 7e significance gate — this is a **VULCAN** input (its `memory/input-cost` axis, and the one it explicitly told me my cluster count was mis-measuring). **Not a dashboard.** Suppressed-still-true conditions won't re-push.

## 3. HELD — content extraction *(Will: "hold 3")*

Pulling **EX-99.1** from each 2.02 and extracting capex / FCF / guidance language would make the row carry a *reason* instead of an item code, and it is the durable version of change #1. **Will held it and I think that's right for now** — it is materially more work than #1, and #1 plus the WALTER rule already closes the demonstrated failure. **Recorded here so it isn't lost, not requested.**

## 4. Notes for the implementer

- **Lane is READ-ONLY to WALTER** (`pull --ff-only`, never push) — hence this packet rather than a PR.
- Changes are **additive**: a new field and a new collector. `intake_scan.py` on the WALTER side reads `liveness.json` defensively, but **please flag me before merge if the `critical[]` string format changes**, since my scan parses it.
- **Backfill is not needed** for #1 — the value is forward-only.
- **Seen-key stability matters:** if the `edgar` seen-key derives from the rendered string, adding `[entity_class]` will change the key and **every existing edgar row will re-fire once as a false onset.** Either keep the key derived from `ticker+date+items` only, or tell me and I'll re-seed `intake_seen.json` on the cutover. **This is the one thing that could bite.**

**— WALTER** *(self-authored packet, committed by author per root CLAUDE.md carve-out ①)*
