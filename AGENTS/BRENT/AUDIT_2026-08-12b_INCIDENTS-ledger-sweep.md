# BRENT SELF-AUDIT — COMPANION B: `refinery_damage/INCIDENTS.tsv`
**2026-08-12 Wed ~18:4x ET · PROME-directed, Will-facing · closing the gap I named in Companion A**

**Why this exists:** Companion A listed this file as *"the largest coverage gap — no sweep of any kind ran against it."* Will directed it closed. Same adversarial standard.
**⛔ Zero capital, zero trades, zero thresholds moved or registered.**

---

## 0. DENOMINATOR

| | |
|---|---|
| Data rows in scope | **53** (RF-001 … RF-053) |
| Rows machine-swept on **every** field | **53 / 53** |
| Rows whose `notes` prose I **read in full** | **~30** — all 21 `bpd_offline_est=0` rows, the 12 stale-ACTIVE rows, the 12 repeat-group rows (overlapping) |
| Rows whose `notes` were **regex-swept only** | **~23** — mostly RESOLVED US-refinery and MONITORING rows |
| Header/comment lines read | **8 / 8** (the scope block, in full) |

**⚠️ Limit:** `source_url` values were **not fetched**. I checked internal consistency, units, staleness and arithmetic — **not whether any cited source still says what the row claims.** A row can be internally perfect and externally wrong; that class is untested here.

---

## 1. FINDINGS — ranked

### 🔴 I-1 — CONFIRMED — The ledger cannot represent gas/LNG losses at all, and records them as **zero** — while my own thesis says gas/LNG is the leg in supply-loss
**Rows `RF-030`, `RF-004`, `RF-016` · owner: WILL/PROME to rule the schema · NOT edited** ⚑ *(this line originally read "(+ RF-033)" — **WRONG, corrected in the ADDENDUM**: RF-033's zero is a documented anti-double-count, not a unit failure. See also the ADDENDUM's I-9: `capacity_bpd` is a SECOND column with the same disease.)*

`bpd_offline_est` is a **liquids** unit. Three **ACTIVE** rows describe large non-liquid capacity losses and therefore carry **`0`**:

| row | facility | what the note says | `bpd_offline_est` |
|---|---|---|---:|
| **RF-030** | Ras Laffan LNG / Shell GTL | **"77 MTPA LNG affected; permanent FM declared"** | **0** |
| **RF-004** | South Pars / Asaluyeh | **"~12% Iran gas production damaged"** | **0** |
| **RF-016** | Habshan (gas processing) | **"UAE's largest gas processing facility; suspended"** | **0** |

**⇒ The single largest energy-capacity loss in the ledger — a permanent force majeure on 77 MTPA of LNG — is stored as the number zero.**
⛔ **And it contradicts my own canon head-on: `THESIS.md` v5.2 says the discriminator is MOLECULE-SCOPED — *"zero CRUDE barrels destroyed… LNG and refined product are in SUPPLY-LOSS."*** **My thesis's central caveat is precisely the thing my ledger's only quantitative column cannot express.** Anyone aggregating this file to ask "how much energy capacity is offline?" gets an answer that is **structurally blind to the leg the thesis says is actually impaired.**
★ **This is Companion A's three-costume pattern in its purest form: the BASIS (liquids-only) never matched the SCOPE (the header explicitly admits "LNG, petrochem, gas fields, nuclear"), and the label never said so.**
**Recommendation (not applied — schema change):** add a `capacity_unit` column (`bpd` / `MTPA` / `bcf_d` / `MW`) and a `capacity_qty`, or a separate `gas_offline_est`. **Until then, no sum over this file may be described as "capacity offline" — only as "liquids capacity offline, gas excluded."**

### 🔴 I-2 — CONFIRMED — 23 rows assert capacity is offline **right now**, median 124 days since anyone checked
**owner: MINE to re-verify · REPORTED, not edited (re-verification is research, not a mechanical fix)**

`status=ACTIVE` is a **present-tense claim**. Measured:

| | |
|---|---:|
| ACTIVE rows | **23** |
| median `last_verified` age | **124 days** |
| max age | **146 days** |
| ACTIVE rows unverified **≥90d** | **18** |
| bpd those 18 carry | **4,774,000 of 6,474,000 = 74% of the ACTIVE total** |

Worst: `RF-004` South Pars 146d · `RF-005` Bazan 145d · `RF-009` Kirishi 139d · `RF-013` Ufa 132d · `RF-014` Mina Al-Ahmadi 131d — **all `source_tier` A-1**, i.e. the highest-confidence rows are the stalest.
**⇒ Three-quarters of the offline capacity this ledger asserts rests on verification that is 3–5 months old.** If any of those restarted, the file says offline and nothing would flag it. `[[finding_dated_carry_item_has_no_expiry_check]]` — **a carried assertion is a string; reading it never grades it.**
**Recommendation (not applied):** a staleness budget per status (`ACTIVE` ≥60d ⇒ re-verify-or-downgrade) surfaced at boot. ⚠️ **Retirement ratchet applies — this would be a tenth check, and it should EXTEND `instrument_check.py` rather than stand up a new script.**

### 🟠 I-3 — CONFIRMED — A 56-day hole in the record that is never stated as either "quiet" or "unlogged"
**owner: MINE · REPORTED**

| month | rows | | month | rows |
|---|---:|---|---|---:|
| 2026-03 | 15 | | 2026-06 | **0** |
| 2026-04 | 13 | | 2026-07 | 7 |
| 2026-05 | 2 | | 2026-08 | 10 |

**Longest gap between consecutive logged events: 2026-05-17 → 2026-07-12 = 56 days.** All of June, half of July.
**Probed, not assumed:** June 2026 was the de-escalation window (Islamabad MOU signed 6/17; Brent fell to the 7/1 cycle low $71.36), so a genuine lull is **plausible** — and a grep of my own `CHANGELOG`/`TRACKER` for June facility-damage events surfaced **none**. ⇒ **I believe the gap is real, not missed logging.**
⛔ **But that is exactly the point: the ledger does not say so, and a reader cannot distinguish "no events occurred" from "nobody logged."** This is the **7/23 zero-transit failure in a different file** — a window edge that has never been probed. `[[finding_verification_zero_is_ambiguous]]`
**Fix I would make (flagging first, not applying — it is a factual claim about coverage):** a `# COVERAGE:` header line stating the period the ledger claims to be complete for, and naming the June gap as verified-quiet.

### 🟠 I-4 — CONFIRMED — 13 rows carry a **blank** `bpd_offline_est` and a naive sum silently reads them as zero
**owner: MINE · REPORTED**

`RF-040 … RF-053` (minus RF-044) — **the 13 most recent rows**, i.e. the entire August Russian strike wave, the CPC SPM-3 re-strike and the FSRU. **Blank, not zero.** 12 are `MONITORING`, 1 is `ACTIVE`.
**Measured:** naive sum over the file = **6,989,000 bpd**, and those 13 rows contribute **nothing** to it. My STATUS already records *"NO capacity-offline figure published for ANY of the eight [Russian plants]"* — so **blank is honest**; the defect is that **blank and zero are indistinguishable to any consumer**, and there are 21 zeroes and 13 blanks.

### 🟡 I-5 — CONFIRMED — The `0` token carries **at least four** distinct meanings
**owner: MINE · REPORTED**

Across the 21 rows using `0`: **(a) restored/resolved** — 11 RESOLVED rows · **(b) attacked but undamaged** — 2 `ATTACKED_INFRA_INTACT` (**RF-019 Kharg strike-2**, RF-034 Barakah) · **(c) deliberately zeroed to prevent double-count** — **RF-044 Jazan, RF-033 VTTI Fujairah** · **(d) real loss the unit cannot express** — RF-030, RF-004, RF-016 (finding I-1).
⚑ **MEMBERSHIP CORRECTED in the ADDENDUM: category (c) originally listed "RF-044 Jazan, RF-019 Kharg." RF-019 belongs in (b), not (c)** — its note says *"oil infra AGAIN spared… 90% export capacity is standing,"* so its zero is genuine-no-damage. **RF-033 is the actual second instance of (c), and it documents itself.** Four categories, count unchanged; two memberships wrong on the first pass.
**⇒ Four meanings, one token, no key.** Combined with I-4's blanks, the column has **six** states and documents none of them. ⛔ **And per the ADDENDUM's I-9, `capacity_bpd` is a SECOND column with the same six-state disease — 39 numeric / 7 zero / 7 blank — which this finding did not cover.**

### 🟡 I-6 — MIXED — No facility key: repeat strikes are invisible to mechanical matching; the anti-double-count convention **works where applied** but is not applied everywhere
**owner: MINE · REPORTED**

**Exact-name matching found ZERO repeat-struck facilities. Token matching found 6 groups / 12 rows.** The ledger has no facility identifier, so **no mechanical check can detect a re-strike.**

| group | rows | verdict |
|---|---|---|
| **Jazan** | RF-039 `400,000` + RF-044 **`0`** | ✅ **CORRECT** — deliberate zero, explicitly documented |
| **Kharg** | RF-002 `1,500,000` + RF-019 **`0`** | ✅ **CORRECT, but RE-CLASSIFIED in the ADDENDUM** — this is an **INFRA-INTACT** zero (*"oil infra AGAIN spared"*), **not** an anti-double-count zero. My original category was wrong. |
| **CPC Marine Terminal** | RF-038 `1,300,000` + RF-042 **`(blank)`** | ⚠️ **LATENT** — same terminal, 6th strike. Blank ≠ deliberate zero. **If anyone fills that blank, it double-counts 1.3M bpd.** |
| **Dos Bocas** | RF-003 `100,000` + RF-020 `50,000` | 🟡 **CANDIDATE double-count of up to 50,000 bpd** — one refinery; a coke-warehouse strike on an already-100k-offline plant may not be additive. **Needs judgment ⇒ reported, not resolved.** |
| Mina Abdullah / Mina Al-Ahmadi | RF-007, RF-014 | ✅ **FALSE POSITIVE** — different Kuwaiti plants |
| Bashneft-UNPZ / Bashneft-Novoil | RF-047, RF-048 | ✅ **FALSE POSITIVE** — different plants, same Ufa cluster |

**⇒ Of 6 groups: 2 correct, 2 false positives, 1 latent hazard, 1 candidate defect.** The convention I documented **works 2-for-2 where a human applied it** — and there is nothing to apply it automatically.

### 🟡 I-7 — CONFIRMED — A provenance pointer that rotted: `RF-030` cites "per BRENT STATUS" and `Ras Laffan` appears **0 times** in current `STATUS.md`
**owner: MINE · REPORTED (the underlying fact is sound; only the pointer is dead)**

`Ras Laffan` returns **0 hits in `STATUS.md`** but **5 hits across `workbook/STATUS_archive_*.md`** and **4 in `THESIS.md`.**
**⇒ The claim was TRUE WHEN WRITTEN and rotted when STATUS was archived** — not a fabrication. **But a reader following it today finds nothing**, and the permanent-force-majeure fact behind the largest capacity loss in the ledger is currently sourced to a surface that no longer carries it. `[[finding_record_of_an_action_is_not_the_action]]`
**Recommendation:** repoint to `thesis/THESIS.md`, which does carry it. **Not applied** — I would rather Will/PROME see that a *provenance* repoint on a force-majeure claim is a judgment call, not a typo fix.

### 🟡 I-8 — CONFIRMED — The Novorossiysk / Sheskharis strike of 8/11-12 is absent, as I declared
**owner: MINE · still owed**
**Rows dated ≥2026-08-11: NONE.** Latest `date_first` is 2026-08-10. The three Novorossiysk/CPC rows (RF-036 Apr, RF-038 7/18, RF-042 7/30) all predate it. ✅ **Consistent with my board_log entry, which recorded it `noted` and explicitly declined to claim the row was written.**

---

## 2. CHECKS THAT PASSED — reported as results

| # | Check | Result |
|---|---|---|
| **P-1** | ID continuity | ✅ **CLEAN.** RF-001…RF-053, **0 missing, 0 duplicate.** |
| **P-2** | Schema integrity | ✅ **CLEAN.** 15 columns on **54 of 54** non-comment lines. |
| **P-3** | **Over-count from RESOLVED rows — my own stated hypothesis** | ✅ **REFUTED BY MEASUREMENT.** I expected restored capacity to inflate the sum. **All 11 RESOLVED rows carry `0`** and contribute **nothing**. The error runs the *other* way (I-4, under-count). **Recording this because a hypothesis I formed and then disproved is worth more than one I never tested.** |
| **P-4** | Anti-double-count convention | ✅ **2 of 2 correct where applied** — ⚑ **MEMBERSHIP CORRECTED in the ADDENDUM: the two are `RF-044` Jazan and `RF-033` VTTI, NOT Jazan and Kharg.** Kharg's zero is infra-intact. Verdict unchanged, membership wrong on first pass. |
| **P-5** | Scope ruling (floating assets) | ✅ **CLEAN and genuinely good.** The 8/7 ruling resolves the FSRU-vs-ship ambiguity with a functional test, correctly admits RF-043, correctly **excludes** three in-transit vessels, and **explicitly declines to redefine HAWK's boundary unilaterally.** Self-consistent on re-read. |
| **P-6** | COMPLETE-check (side effects in notes) | **3 candidates → 1 real (I-7), 1 valid (`RF-033` "see RF-012" — RF-012 exists), 1 unresolved candidate (`RF-042` "folded into", not chased).** |
| **P-7** | `last_verified` parseability | ✅ **CLEAN.** 53/53 parse; none blank. |

---

## 3. WHAT I FIXED vs WHAT I STOPPED ON

**✅ Fixed: nothing in this file.** Every finding is either a **schema change** (I-1, I-4, I-5), a **factual coverage claim** (I-3), a **re-verification campaign** (I-2), or a **judgment call** (I-6 Dos Bocas, I-7 provenance repoint).
**⇒ I deliberately made zero edits to INCIDENTS.tsv.** PROME's standard was *"fix what is unambiguously mechanical, stop and report anything needing judgment"* — **on this file that set is empty**, and the honest output is a report, not a diff.

## 4. VERDICT — this is NOT a clean ledger, and the reason is one defect

**8 findings, all CONFIRMED except I-6's Dos Bocas leg (CANDIDATE).** The mechanical hygiene is genuinely good — IDs, schema, dates, scope ruling all clean, and the anti-double-count convention works where a human applied it.

**But the quantitative column does not mean what its name says.** `bpd_offline_est` is:
- **blind to gas/LNG** (I-1) — including the largest loss in the file,
- **six-valued** across zero/blank/four zero-meanings (I-4, I-5),
- **74% resting on 3–5 month-old verification** (I-2),
- **undefended against re-strikes** by any mechanical means (I-6).

**⇒ No aggregate over this file is currently quotable.** That is the single recommendation I would put in front of Will: **not a fix, a usage constraint — until the schema carries units and a staleness budget, this ledger is a good EVENT RECORD and is not a CAPACITY MEASURE, and nothing in it should be summed into a number that reaches a decision.**

★ **And the pattern from Companion A holds a third time: a number whose BASIS moved while its label stayed still. F-1 was a retracted input inside a derived figure; F-2/F-3 were two bases registered as one test; I-1 is a unit that never matched the scope its own header declares.**

---

# ADDENDUM — 2026-08-12 ~19:1x ET · PROME flagged `RF-033`; reading it produced **two corrections to this report** and one new finding

**PROME's catch:** I counted 3 ACTIVE-storing-zero rows in I-1 and mentioned `RF-033` only in a parenthetical without testing it. **PROME counted 4 and asked which of three explanations held. Reading the row resolved it — and it was none of the three.**

## ✅ CORRECTION 1 — **I-1's scope is 3 rows, not 4. `RF-033` does NOT belong in it, and my parenthetical was wrong.**

`RF-033`'s own note explains its zero **explicitly**:
> *"…(export-disruption context; **left out of `bpd_offline_est` to avoid double-count with RF-012 bypass**)"*

**⇒ `RF-033` is a documented ANTI-DOUBLE-COUNT zero — I-5 category (c) — not a unit-representation failure.** The row is **correct and self-documenting.** I-1 stands at exactly **RF-030, RF-004, RF-016**, and I have removed the `(+ RF-033)` claim.

## ✅ CORRECTION 2 — **I mis-classified `RF-019` Kharg, and the convention count was wrong**

Companion A/B said the anti-double-count convention was *"2-for-2 where applied (Jazan, Kharg)."* **Reading `RF-019` shows that is wrong:** it carries `capacity_bpd = 1,500,000` with `bpd_offline_est = 0` and `status = ATTACKED_INFRA_INTACT`, and its note says *"oil infra AGAIN spared… 90% export capacity is standing."*
**⇒ Kharg's zero is a genuine INFRA-INTACT zero (category b), not an anti-double-count zero.** The convention is **2-for-2 where applied — `RF-044` Jazan and `RF-033` VTTI** — and Kharg was never an instance of it. **P-4 is unchanged in verdict (2 of 2 correct) and changed in membership.**

## 🟠 NEW — I-9 — CONFIRMED — `capacity_bpd` is a **second** column with the identical disease, and I never audited it

PROME asked whether I-1 generalizes to *"the ledger cannot represent non-production assets."* **I tested that and it is NOT the right generalization** — the cross-tab refutes it: **9 of 13 non-production rows DO carry a `capacity_bpd`** (CPC, Primorsk, Novorossiysk export terminals all quote a bpd throughput).

**The real generalization is narrower in cause and wider in reach: there is no UNIT FIELD, so any asset not naturally denominated in barrels/day stores as `0`.**

| `capacity_bpd` state | rows |
|---|---:|
| numeric | **39** |
| **`0`** | **7** |
| **blank** | **7** |

**The 7 zeros, read individually:**

| row | asset | natural unit | why `0` |
|---|---|---|---|
| RF-004 | South Pars | bcf/d (gas field) | **wrong unit** |
| RF-016 | Habshan | bcf/d (gas processing) | **wrong unit** |
| RF-030 | Ras Laffan | **MTPA (LNG)** | **wrong unit** |
| RF-034 | Barakah | **MW (nuclear)** | **wrong unit** |
| RF-011 | Ust-Luga | throughput — its own note quotes *"up to 40% of RU oil exports"*, a **percentage** | **wrong unit** |
| RF-033 | VTTI Fujairah | storage/throughput | **wrong unit** |
| **RF-037** | KOC offshore platform | **bpd IS the right unit** — note calls it *"the FIRST production-CLASS asset struck"* | ⛔ **capacity simply UNKNOWN, stored as 0** |

**⇒ `capacity_bpd = 0` conflates *wrong-unit* (6 rows) with *unknown* (1 row) — and adds 7 blanks on top.** Same six-state failure as `bpd_offline_est`, in a column my sweep never opened.
⛔ **Coverage admission: Companion B audited `bpd_offline_est` and reported the ledger's quantitative problem as if it were one column. It is two.** The verdict is unchanged and slightly strengthened — **not a capacity measure** — but the schema fix in I-1 must cover **both** columns, and must separate *unmeasurable-in-this-unit* from *unknown*.

## 🟡 One dated carry-item surfaced by the same read
`RF-033`'s note holds an open item from **2026-05-31 (73 days)**: *"Borouge petrochemical + Emirates Global Aluminium collateral damage reported in prior BRENT STATUS — **UNVERIFIED** in the 2026-05-31 source pass; **not logged as separate facilities pending confirmation**."* **Honest discipline when written; nobody has returned to it in 73 days.** An I-2-class instance with a name.

## What this addendum changes for a Will ruling
- **I-1 scope: 3 rows** (RF-030 / RF-004 / RF-016), not 4.
- **The schema ask now covers TWO columns** (`capacity_bpd` *and* `bpd_offline_est`) and must distinguish **wrong-unit** from **unknown**.
- **Verdict unchanged:** still a good **event record**, still **not a capacity measure**, still **no quotable aggregate.**

★ **Worth recording plainly: PROME's flag was one row, and reading it overturned two of my own classifications and opened a column I had not looked at. My sweep read 53 rows and still generalized from the column I happened to audit.** `[[finding_verification_zero_is_ambiguous]]` — **a check certifies its SCOPE, not your capability** — this time on my own audit rather than on my data.
