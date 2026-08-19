# WALTER — Routing & trigger-coverage defects: what to actually do

**Status:** PROPOSAL. Nothing here is executed. **RULE 8: spec changes land as a proposal to Will first.**
**Raised by:** Will, 2026-08-19 ~15:33Z — *"Okay how do we address these problems. What do we have to do?"*
**Prompted by:** two routing defects found in one session (`SIG-W-20260819-019` §3, `SIG-W-20260819-023`).

---

## 0. The measurement first — because the defect is bigger than the two instances

**I scanned rather than assumed. Two passes, because the first was keyed on filenames and that is its own trap** (`[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`).

**Pass 1 — structured trigger registries (files with a `trigger_id` column):**

| Registry | Rows | WALTER boot reads it? |
|---|---|---|
| `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` | 9 | ✅ |
| `AGENTS/REGINALD/registry/THRESHOLDS.tsv` | 8 | ✅ |
| **`AGENTS/CREED/registry/THRESHOLDS.tsv`** | **11** | ❌ |

**⇒ 17 of 28 structured triggers are in the boot array. 39% of them are invisible.**

**Pass 2 — content scan for registered gate/trigger ID families actually in use across STATUS files:**

`CREED-T-NN` · `RED-FT-NN` · `REG-T-NN` · **`GATE-FALCON-NN` · `GATE-LIQ-NN` · `GATE-OSPREY-NN` · `GATE-SAM-NN` · `GATE-TERRY-NN` · `GATE-VIO-NN` · `HAW-NN` · `FAL-NN`**

🔴 **⇒ THE REAL FINDING, AND IT IS NOT "WALTER FORGOT CREED": only THREE agents in the fleet keep a machine-readable trigger registry. At least SIX more gate families exist as PROSE inside STATUS files. WALTER cannot scan those even in principle, and no amount of WALTER-side work changes that.**

**Feasibility datum for §3 below:** the `entities:` header is populated on **101 of 769** BOARD signals all-time (13%) — **but 23 of 23 today (100%)**. It is a live, adopted-forward field. **Forward-only is the right expectation** — the `corrects:` precedent (PROME, 8/08): *"mandatory-at-dispatch reaches 100% in days, archive sweeps never do."*

---

## 1. FIX A — mechanize the action-line rule *(recommended first)*

**The defect:** §3.5.4 says an ask directed at a named recipient goes on `action:`, never `info:` with the ask buried in the body. **I violated it five times in ninety minutes** — *"HOMER's call"* in the body, HOMER on `info:`.

**The fix:** a new `walter_doctor` check (#27), fully deterministic, no judgement:

> **For each BOARD signal: if an agent name from `REGISTRY.tsv` appears in the signal BODY, and that agent is on the `info:` line rather than `action:` → FLAG.**

- **Cost:** ~40 lines in `tools/walter_doctor.py`. It has 26 checks; this is a natural 27th.
- **Would have fired:** 5 times today, on `-019`/`-020`/`-021`/`-022` (HOMER) — before dispatch, not after.
- **Why this one first:** §3.5.4 is **already ratified and currently enforced by discipline alone.** `[[finding_mechanize_the_cap_not_the_ritual]]` — *a deferrable rule wants a check, not a remembered ritual.* **My discipline held on the TERRY gate five times today and failed on this one five times today. That is exactly the asymmetry a machine closes.**
- ⚠️ **Known false-positive class, stated up front:** a signal that legitimately *mentions* an agent without asking anything of it (e.g. *"HAWK's framing is the one to carry"*). **Mitigation: flag, never block — and tune on observed FP rate rather than pre-guessing.**

**Will's call: build it?**

---

## 2. FIX B — add CREED's registry to boot 6b/6c *(recommended, cheap)*

**The defect:** `-019` §3 — CREED appears **zero** times in `AGENTS/WALTER/CLAUDE.md`. The nearest trigger on the board (9bp) and the session's only candidate crossing were both invisible to boot.

**The fix:** add `AGENTS/CREED/registry/THRESHOLDS.tsv` to the step-6b read-loop and the 6c passive scan.

⚠️ **NOT a clean 17 → 28 array extension, and must not be specced as one.** Of CREED's 11 rows:

| Numerically scannable (5) | Not scannable (6) |
|---|---|
| `T-01a` OFFICE-CMBS-DQ-TREPP >12 | `T-04` *"rising QUALITATIVE — no numeric band set"* |
| `T-01b` OFFICE-CMBS-SS-TREPP >18 | `T-05` *"HOMER-OWNED — CREED does not score this"* |
| `T-02` MATURED-BALLOON-SHARE >50 | `T-06` requires a **cluster** judgement |
| `T-03` FDIC-NONOWNER-CRE-PDNA >3.40 | `T-06b`, `T-07`, `T-08b` compound / two-leg |
| `T-08a` VNQ-VS-SPY-3MO < −10 | |

- **Cost:** one `CLAUDE.md` edit + extending the 6c pull to the 5 scannable metrics. **Three of the five (`T-01a`, `T-01b`, `T-02`) are monthly Trepp prints, not daily pulls** — so 6c would surface them as *"last known print + its date"*, not as a live level. **Say so in the spec or it will silently imply freshness it does not have.**
- **Open sub-question for CREED, not WALTER:** there is **no WALTER fire-ledger for `CREED-T`** (only `RED-FT` and `REG-T` have one). Should there be? **That is a shared-ownership question — CREED may already keep its own — and creating one unilaterally would duplicate a record and split the truth.** ⇒ **Ask CREED before building.**

**Will's call: add it? And does CREED want a WALTER-side fire-ledger?**

---

## 3. FIX C — entity→owner coverage check *(proposed, but I recommend the LIGHT version)*

**The defect:** CORAL owns `FL_REAL_ESTATE` and received nothing, while a Florida hotel portfolio moved the national lodging rate 79bp.

**The full version:** map each signal's `entities:` list against the `REGISTRY.tsv` Domain column; flag any domain owner not on `action:`/`info:`.

⚠️ **HONEST ASSESSMENT — THIS IS THE ONE MOST LIKELY TO ROT.** Catching CORAL requires knowing *Orlando → Florida → `FL_REAL_ESTATE`*, i.e. a **geography→domain map** that must be maintained, will drift, and whose staleness is invisible (`[[finding_dated_stamp_is_a_trigger_not_a_shield]]`). **A coverage check that silently stops covering is worse than none — that is this desk's own repeated finding.**

**⇒ RECOMMENDED LIGHT VERSION instead:** no new map. **At dispatch, when a document carries a PROPERTY-TYPE, GEOGRAPHY, or SECTOR BREAKDOWN, enumerate those axes and check each against the REGISTRY Domain column** — which already contains the vocabulary (`FL_REAL_ESTATE`, `HOUSING`, `CMBS`, `MULTIFAMILY`, `INSURANCE_RISK`…). **No map to maintain; the REGISTRY is the map, and it is already refreshed at every boot (step 8).**

**This is a CHECKLIST step and will therefore decay — I am saying so rather than pretending otherwise.** **Its justification is narrow: it is cheap, it needs no new artifact, and the failure it prevents (a whole desk gets nothing) is the most expensive of the three.**

**Will's call: light version, full version, or neither?**

---

## 4. NOT WALTER'S TO FIX — escalate

**Six gate families live as prose in STATUS files** (`GATE-FALCON`, `GATE-LIQ`, `GATE-OSPREY`, `GATE-SAM`, `GATE-TERRY`, `GATE-VIO`, plus `HAW-`/`FAL-`). **No WALTER check can reach them. Fixes A-C do nothing about this.**

**The question is a fleet-architecture one:** *should registered gates live in a machine-readable registry per agent, or is prose acceptable for most desks?* **There is a real argument for prose** — most of those gates are compound or judgemental, exactly like CREED's six unscannable rows, and forcing them into a TSV would produce a registry that lies by omission.

⇒ **Route to PROME and DAEDALUS, Will-gated. DAEDALUS is live in another window right now** and this is squarely its fleet-architect remit. **WALTER's contribution is the measurement in §0, not the answer.**

---

## 5. What I am NOT proposing, and why

- **No change to the pull-complete exemptions.** Nothing today implicates them; §3.5.4 is a *precondition* for them and Fix A strengthens it.
- **No retroactive `entities:` backfill.** 13% all-time, 100% today. **Forward-only per the `corrects:` precedent — archive sweeps never finish.**
- **No auto-widening of any recipient list.** Two defects is not evidence that routing is broadly too narrow; **`-023` found five of seven recipients were correct as sent.** **The fix is targeted, not a broadcast.**
- **No new cadence.** `[[finding_rows_leave_when_the_reader_can_discharge_them]]` — a second cadence is a second thing to forget. **Fix A rides the existing doctor; Fix B rides the existing boot; Fix C rides the existing dispatch.**

---

## 6. Recommendation, ranked

| # | Fix | Cost | Prevents | Recommend |
|---|---|---|---|---|
| **1** | **A — mechanize §3.5.4 in the doctor** | ~40 lines | today's 5× violation | **DO IT** — mechanical, enforces a ratified rule |
| **2** | **B — CREED registry into 6b/6c** | 1 edit + 5 metrics | today's invisible 9bp | **DO IT** — but ask CREED about the fire-ledger first |
| **3** | **C — light coverage step** | 1 checklist line | CORAL getting nothing | **DO IT, expect decay** — no artifact to rot |
| **4** | **D — fleet gate-registry question** | — | the other 6 families | **ESCALATE** to PROME/DAEDALUS, not WALTER's |

**Sequence matters: A before B.** **Fix B widens what I read; Fix A catches what I do wrong with what I have already read.** **Widening intake before fixing the handling multiplies the error I actually made today.**
