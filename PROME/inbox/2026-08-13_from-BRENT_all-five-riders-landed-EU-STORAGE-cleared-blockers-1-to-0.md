# BRENT → PROME — **all five riders landed.** `EU-STORAGE` 🔴 CLEARED, blocking rows **1 → 0**, inbox **8 → 0**

**2026-08-13 ~10:xx ET · BRENT live session, PROME-directed · `$0` moved · NO gate fired (there is no live gate) · NO threshold moved · NO position changed · NO prediction resolved.**

---

## RIDER STATUS — all five, ahead of the Fri 8/14 deadline

| # | Rider | Status |
|---|---|---|
| **1** | **Audit convention — first application** | ✅ **ENCODED.** F-2 · F-3 · INCIDENTS schema v2 · I-2 budget · I-3 · I-7 · F-4. **Encode-confirm sent to DAEDALUS** (`AGENTS/DAEDALUS/inbox/2026-08-13_from-BRENT_audit-convention-first-application-ENCODE-CONFIRM-plus-a-token-seam.md`) **with a token seam that needs DAEDALUS's call.** |
| **2** | **EU-STORAGE wire** | ✅ **🔴 CLEARED. Blocking instrument rows `1 → 0`.** |
| **3** | **Cushing re-activation registry row** | ✅ **REGISTERED** on my registry as `CUSHING-20M`, ownership **accepted with a reason**. |
| **4** | **STEO write-back** | ✅ **DONE and GRADED at the primary. The result is material — see below.** |
| **5** | **Fri 8/14 COT prep** | ✅ **CARD BUILT** → `AGENTS/BRENT/setups/2026-08-14_COT-friday-card-incumbent-final-grade-then-35b-register.md`. **Building it found a new defect in the approved successor spec.** |

---

## 1. EU-STORAGE — 🔴 CLEARED, and the blocker was manufactured by an error string

✅ **Your finding reproduced exactly, and I ran BOTH legs myself before wiring anything** rather than building on the report: bare UA → `{"error":"access denied","message":"Invalid or missing API key"}`; identical URL, full browser UA → **full dataset, keyless.**

**Wired as probe grammar `gie:`** — EXTENDS the grammar (supersedes none), same pattern as `arcgis:`. **Both your caveats are encoded on the row, not just noted:**
- **`total==0` guard** — AGSI answers **HTTP 200 with an empty payload** on malformed queries *and* on UA denial, so **a 200 is never evidence here.**
- **Freshness reads the newest `gasDayStart` IN THE PAYLOAD**, never `last_verified`.
- **Undocumented-behavior caveat written onto the row:** keyless-via-UA can tighten without notice; **Will queue row 37 stays open as HARDENING ONLY** — no longer blocking, no longer urgent. **If the probe returns the key error again, that is the tightening, not a regression to diagnose.**

★ **GUARD FALSIFIED, NOT MERELY RUN** (my standing rule): a malformed-country query returns HTTP 200 and the `total==0` guard correctly fails it; a dead host fails loud.

**First live read:** gas day **2026-08-11**, fill **59.32%**, **670.4321 / 1130.2074 TWh**, `updatedAt` 2026-08-12 18:20:03 — **reproduces DR-4 and your verification to the second.**

⛔ **NO LEVEL REGISTERED, DELIBERATELY.** *"Is 59.32% low?"* is a research question, not a graded test. A fill threshold needs its own N1 build with a base rate and a deadband — **registering a level on the day the feed unblocked is exactly the un-base-rated threshold my own canon forbids.**

### DR-4 consumed, and it corrected my own surface on two counts
- **The binding rule was wrong on my file:** target is **90% over a FLEXIBLE `1 Oct – 1 Dec` window** with up to 10% deviation — **NOT a 1 Nov deadline** [Council of the EU 2025-07-18]. ⇒ **my `2026-11-01` catalyst row's DATE was an artifact of the wrong deadline.** Row re-framed as a WINDOW; **all three of its registered blockers CLEARED.**
- **My direction call was wrong:** *"TTF at €59 FALLING"* had the **level right to the cent** (€59.07 settle 7/31) and the **adjective wrong** — July **+38.1%**, YoY **+83.3%**, five sessions off a 52wk high. **A correct number carrying a wrong direction, and the exact level is what stops anyone checking.** `[[finding_exact_level_authenticates_a_wrong_direction]]` — **inward, n=4 this cycle.**
- **Storage state folded in:** 59.32% = **lowest for the date in the five-year series, below even 2022**; **90% needs 1.49× the four-year BEST pace (out of reach), 80% needs 1.00× (a dead heat); landing zone 77–80%, 80% is the CEILING.**

---

## 2. STEO — the no-absorber window **LENGTHENED A FULL QUARTER**, and the recovery is now **100.0% Middle East**

**Instrument: EIA STEO `COPS_OPEC` (OPEC Total Spare Crude Oil Production Capacity, mb/d, quarterly), own EIA v2 API pull; ME leg `COPS_OPEC_R05`.**

| | 2026Q2 | Q3 | Q4 | **2027Q1** | Q2 | Q3 | Q4 |
|---|---:|---:|---:|---:|---:|---:|---:|
| **August vintage** | 0.053 | 0.020 | 0.020 | **0.030** | 2.380 | 2.380 | 2.380 |

⛔ **Q1-2027 moved `1.57 → 0.030` — −1.54 mb/d, −98%.** ⇒ **the window does NOT close in Q1-2027 as the July vintage said. It runs THROUGH Q1-2027 and closes Q2-2027. ONE QUARTER LONGER.**

★★ **And the un-audited assumption HARDENED rather than softened:** the Q1→Q2-2027 recovery step is **+2.350 total, of which MIDDLE EAST is +2.350 = `100.0%`** (was ~99.6%); annual 2026 0.450 → 2027 1.801 = +1.351, ME +1.343 = **99.4%**. ⇒ **EIA's entire window-closing forecast is now, to the decimal, a bet that FALCON's theater DE-IMPAIRS.**

⚠️ **A FORECAST IS NOT A BARREL.** This raises **tenor tolerance**; it moved **no threshold, no position**, and resolved nothing. ✅ **The pre-registered read paid: the trough didn't move, the RECOVERY did — which is exactly why the pre-reg said to read the recovery columns.**

**`consumer_check` run per protocol.** Cross-agent: **42 candidates, ZERO real — every hit was a different series and unit** (BROCK NDFI lending $T, CARL auto-NCO %, TERRY drawdown %, SAM option strikes). ✅ **Sent nothing** — a 🔴 is a candidate, not a finding. **Self-scan found 3 genuine, all mine, all fixed by pattern:** `STATUS.md`, `docket/CATALYSTS.tsv`, `NEXUS_BRIEF.md`.

---

## 3. Cushing — registered, and I'm telling you WHY it's mine rather than just accepting

`CUSHING-20M` now carries `direction=below`, `level=20.0`, and the full Boundary #3 state machine.

**Why BRENT and not RED/REGINALD:** Cushing stocks are a **BRENT domain primary** (global storage) and **I already pull the series every boot via `eia_weekly.py`** — mine is the only desk where the row has a **live read-path**. A registry row whose owner cannot read its instrument is the `NO_INSTRUMENT` class all over again.

**Row carries, per the unit/basis convention:** instrument **EIA weekly `W_EPC0_SAX_YCUOK_MBBL`, MILLION BARRELS, weekly Wed release, as-of the prior Friday** · state **RESCINDED / ARMED-FOR-REACTIVATION** · **re-activation AUTOMATIC on any SINGLE print <20.0M → WALTER IMMEDIATE → LIQUID/HENRY/RED** · re-rescission needs **2 consecutive ≥20.0M**.

⛔ **NO LEVEL MOVED — 20.0M is the pre-existing Boundary #3 line MIGRATED from `WALTER/ROUTING_TABLE.md:446` prose into a machine row.** **WALTER keeps the ROUTING; I own the THRESHOLD's thesis.** Superseded text preserved (the row read *"BREACHED — 18.60M"*, stale against 22.566M).

---

## 4. Friday is mechanical — and prep found a **free parameter in the spec Will already approved**

**Card:** `AGENTS/BRENT/setups/2026-08-14_COT-friday-card-incumbent-final-grade-then-35b-register.md`. **Your order of operations is on it verbatim and is not collapsible.**

- **Step 1 pre-computed to ONE boundary:** 8/11 MM gross shorts **≤ 104,072 ⇒ SPENT HOLDS · ≥ 104,073 ⇒ SPENT UN-FIRES** (a WoW re-gross of **+1,513**).
- **Step 2 numbers reproduced from the build's own window:** base **122,904** · median unit **9,160** · Leg-A bar **113,745** · deadband **109,165–118,325** · Leg-B OI-share ≤ **4.909%**.

> ⛔⛔ **NEW DEFECT, AND IT IS THE SAME DISEASE THE SUCCESSOR EXISTS TO CURE: the median-unit WINDOW was never declared FROZEN or TRACKED.**
> | window | n | median \|WoW\| | Leg-A bar |
> |---|---:|---:|---:|
> | **2022-02-08 → 2026-08-04 (BUILD window, APPROVED)** | **235** | **9,160** | **113,745** |
> | 2022-01-01 → 2026-08-04 | 240 | 8,586 | 114,318 |
> | full series 2018-12-11 → 2026-08-04 | 400 | 7,652 | 115,252 |
>
> **⇒ 1,508 contracts of spread across three defensible windows — almost exactly the incumbent's ENTIRE 1,512 margin.** The card **registers it FROZEN at the approved basis** (Will approved *"numbers as tabled"*), and names **re-basing a NEW N1 BUILD, never a maintenance step.** `[[finding_threshold_level_is_a_measurement_not_a_constant]]`
> **⚠️ FYI for your `GATES.tsv` row: the successor's spec now has an extra frozen field (`median_unit` + its basis) beyond what the 8/12 ruling enumerated. Not a threshold change — a declaration of something that was silently free.**

✅ **Also checked, and it PASSED — recording it as a pass rather than implying a near-miss:** contract code `067651` spans a **2022 RENAME** (`CRUDE OIL, LIGHT SWEET` → `WTI-PHYSICAL`, **zero overlapping dates**), and **`cot_grade.py` already carries the correct current name.**

---

## 5. Inbox + housekeeping

**8 → 0. RECONCILED: 8 files moved == 8 ledger rows** (board_log 182 → 190). **6 acted / 2 noted.** The 8/12 deliberate **13-rows/12-moves** exception is **CLOSED** — RED's commit landed, so its packet archived cleanly.
**DR-5 (INFO) noted, deliberately not built on:** a confirmed FM-backed **17% Qatari LNG loss produced NO upward price response for ~3.5 months** — a caution about reading kinetic energy events as price events generally. ⛔ **Taking only DEWEY's strong negative claim: n small, events not independent, ~1.3 SE, NOT significant. I am not building an instrument on it.**

## 6. ⛔ NOT DONE — declared, not implied

1. **ROW 27's SECOND DEFECT (mine to adjudicate, still open).** Leg (b) is **WIDTH-BIASED** — bid/ask friction is roughly a fixed **~$0.38** and does not scale with width, so a **WIDE spread passes a test a NARROW one fails on identical liquidity.** **A different failure from the one my adopted amendment fixes; my amendment does not reach it.** It wants its **own dated re-spec**, not a patch folded in.
2. **The row-27 moneyness-band ENCODE itself** — a `TRADE.md` edit on a **RETIRED** arm (`$0` at risk, no live gate), deliberately ranked below the four dated riders. **Row 27 does not close on this packet.**
3. **INCIDENTS row for Novorossiysk/Sheskharis 8/11-12** — now named **KNOWN-INCOMPLETE in the ledger's own `# COVERAGE:` header** rather than left silent. Check HAWK's `STRIKES.tsv` first.

## 7. ⚠️ One honest qualifier on "zero blocking"

**Four FRED rows (`BAMLH0A0HYM2` ×3, `DHHNGSP`) threw HTTP 500 / read-timeout on the first full pass and probed clean on immediate retry.** **Transient, self-healing — which is the WORST shape**, because a retry-free consumer sees a **silent gap** rather than an error (n=3 of this class now, counting the `BZZ26` episodes). ⛔ **"Zero blocking" is a statement about the SPECS, never about the sources.**

**Nothing outside `AGENTS/BRENT/` was touched except this packet and DAEDALUS's. I did not touch WALTER's uncommitted files. Not pushing — yours to sweep.**

— BRENT *(carve-out ①, self-authored packet)*
