# BRK-02 — INDUSTRY NON-ACCRUAL INSTRUMENT: BLIND DEFINITION-MATCH SPEC

**Author:** BROCK · **Date:** 2026-08-13 Thu · **Status:** ✅ **RATIFIED BY WILL 2026-08-13 — THIS IS THE RESOLVER OF RECORD FOR BRK-02.**
**Ratification:** FORUM 5 slate item, approved as recommended — rulings-record `FORUM/2026-08-13_private-credit-recognition/04_synthesis/03_PROME_rulings-record.md` (commit `408110c0d`); batch artifact ⑤ `PROME/proposals/2026-08-13_private-credit-batch-RULED.md` updated. **Cite those; do not reconstruct.**
⚠️ **Branch B5 of the P2 branch set ("spec still unratified at 9/30 ⇒ NO-VERDICT by default") is now MOOT and cannot fire.** All other branches stand unchanged.
⚠️ **The §4 metadata-only rule survives ratification and still binds:** the C4 availability check runs on publication calendars / listing pages / prior-edition dates ONLY. **Opening the report body before resolution contaminates the blindness this spec exists to protect.**
**⚠️ TWO DISTINCT RATIFICATIONS, in sequence — do not read them as one:** **(1) the METHOD** was ratified earlier on 8/13 by ruling ⑤ in `PROME/proposals/2026-08-13_private-credit-batch-RULED.md` (*"write the blind spec, basis criteria only, zero values"*, with my three constraints folded in) — that authorized me to WRITE this document. **(2) THIS DOCUMENT** was then ratified as a FORUM 5 slate item, which is what makes it the **resolver of record**. **A reader who conflates them will think the spec was ratified before it existed.**
**Predecessor rulings on the same prediction:** ① name set = SCRATCH six (basis, not outcome) · ⑤(a) proxy scope guard RATIFIED.

> ## ⛔ BLINDNESS DECLARATION
> **ZERO current values were pulled in writing this spec.** No non-accrual level, rate, or print for any candidate was fetched, read, or consulted. Every criterion below is **structural** — what a publication *measures*, over *what population*, on *what basis*, on *what schedule*. **Nothing here was chosen after seeing a number it would produce.**
>
> **Prior-exposure disclosure, carried per PROME's instruction:** I hold **one** directional datum on **one** candidate — `KB-BRK-161` (Fitch BDC Q1-26 review, 6/19): *"non-accruals INCREASED."* **Direction only, no level.** Verified 8/13 by bounded grep that I hold **zero industry-level non-accrual VALUES** anywhere in KB or STATUS — the only aggregate rows are *default* rates (KB-BRK-123/156) and a single-name ARCC row (KB-BRK-134). **There is no level on any BROCK surface to back-fit a threshold against.**

---

## 1. What the letter actually requires — fixed BEFORE any candidate is scored

The registered letter is **"Industry non-accruals rise to >2.5%"** (`PREDICTIONS.tsv`, made 2026-02-23, resolve 2026-09-30, 75%). Decomposed, it constrains a qualifying instrument on four axes:

| Axis | Requirement from the letter | Source of the requirement |
|---|---|---|
| **Quantity** | **NON-ACCRUALS.** Not defaults. Not NAV. Not PIK. | The letter's own noun |
| **Form** | A **RATE** comparable to a 2.5% line — a percentage of a portfolio, not a count or a dollar balance | ">2.5%" is a rate |
| **Basis** | **COST (or amortized cost), NOT fair value** | My own 7/28 pre-data ruling fixed BRK-02's basis to cost; **FV was rejected on the record.** Cost and FV bases differ ~1.7× across my cluster (e.g. 4.6% vs 2.8% at MFIC), so basis is decisive, not cosmetic |
| **Population** | **INDUSTRY** — a broad private-credit / BDC population, not a hand-picked set | The letter's own adjective, and the whole reason ruling ① confined the six-name median to proxy status |

⚠️ **Non-accrual ≠ default, and this is the criterion that does the most work below.** A loan can be placed on non-accrual without a payment-default event (deterioration, doubt over collectability), and a defaulted loan can sit in an index whose population is loans rather than BDC balance sheets. **They are different quantities over different populations. An instrument measuring one does not resolve a letter written about the other.**

## 2. Basis criteria (the four PROME/Will ratified, applied in this order)

**C1 — Definition match.** Does it publish **non-accruals**, as a **rate**, on a **cost** basis? *Failure here is disqualifying and is checked first, because it is answerable with zero values.*
**C2 — Coverage breadth.** Is the population broad enough to be called "industry," and is its selection rule independent of the outcome being measured?
**C3 — Publication cadence.** Is it a **standing series** on a known schedule, or a one-off?
**C4 — Availability by 9/30.** Will a reading covering a period after the letter's window publish **before the resolve date**?

## 3. Candidate scoring — structural only, zero values

| Candidate | C1 Definition | C2 Coverage | C3 Cadence | C4 By 9/30 | Verdict |
|---|---|---|---|---|---|
| **KBRA DLD** | ❌ **FAIL — measures DEFAULTS, not non-accruals.** Wrong quantity; also a *loan* population, not BDC balance sheets | — | — | — | 🔴 **DISQUALIFIED at C1** |
| **Reuters 51-BDC** | ❌ **FAIL — the quantity I hold from it is NAV (−2.35%) and PIK ($477M). It is not a non-accrual series** | — | ❌ **FAIL — a one-off 5/29 aggregation article, not a standing series** | — | 🔴 **DISQUALIFIED at C1 and C3, independently** |
| **Fitch 32-rated-BDC review** | 🟡 **PARTIAL — it DOES report non-accruals** (KB-BRK-161 direction). ⚠️ **BASIS UNVERIFIED: whether Fitch reports at cost or fair value is unknown to me and is decisive** | 🟡 **QUALIFIED — 32 *rated* BDCs is broad but is a RATED universe**, which skews to larger/rated issuers. Selection rule is independent of non-accrual outcomes ✅, but "rated" ≠ "industry" | ✅ **PASS — quarterly standing series** (Q1-26 landed 6/19) | 🔴 **OPEN — the decisive unknown** | 🟡 **SOLE SURVIVOR, conditional** |

**⇒ Blind definition-match eliminates two of three candidates before any value is pulled — which is the criterion doing exactly the work it was ratified to do.**

## 4. ⚠️ THE CONTAMINATION HAZARD IN MY OWN FEASIBILITY CHECK — named, with the handling rule

**C4 cannot be answered by opening the Fitch report, because the report body carries the value.** A naive availability check would destroy the blindness this spec exists to protect — **the feasibility test contaminating the instrument it is testing.**

**Handling rule, binding:**
- ✅ **Permitted:** publication calendars, index/listing pages, press-release titles, prior-edition publication *dates* — **metadata that carries a date but not a level.**
- ❌ **Forbidden until resolution:** the report body, any summary quoting a figure, any secondary article reporting the number.
- ⚠️ **If C4 cannot be settled from metadata alone, it stays OPEN and the §5 fallback governs. It is never settled by opening the report.**

## 5. Pre-registered outcomes — fixed now, before any value exists

| Condition | Resolution |
|---|---|
| A **qualifying** instrument (passes C1-C4) publishes a post-window reading **before 9/30** | **BRK-02 resolves on that instrument's number vs the 2.5% line.** Values pulled **only at that moment** |
| **No qualifying industry instrument publishes by 9/30** | 🔴 **BRK-02 resolves NO-VERDICT** — pre-registered per ruling ⑤(c). **NEVER the proxy** |
| The six-name median (3.50% at Q2-26) | ⚠️ **TELL ONLY, NEVER THE RESOLVER** — ruling ⑤(a). It informs the read; it cannot resolve the row |

**NO-VERDICT is a legitimate outcome, not a failure of this spec** — and on the structural picture above it is a live possibility, since the sole surviving candidate's C4 is genuinely open. *(`[[finding_prereg_verdict_boundary_must_be_a_number]]`: a number plus a no-verdict band; here the band is "no qualifying instrument.")*

## 6. Widening — allowed on definition/cadence only, and one candidate DELIBERATELY EXCLUDED

Ruling ⑤(b) permits widening the candidate set on definition/cadence grounds. Two admissible classes, both **unexamined and value-free** as of this writing: **(a)** SEC-derived aggregations compiled from BDC 10-Q non-accrual disclosures at cost — best definition-match in principle, since it is the same quantity and basis as the letter; **(b)** rating-agency or vendor BDC-sector reviews other than Fitch's, subject to the same C1-C4.

🔴 **DELIBERATELY EXCLUDED — Cliffwater CDLI, and the exclusion is the disclosure.** CDLI reports a non-accrual rate over a broad direct-lending population and would otherwise be a strong C1/C2 candidate. **I am excluding it because I already know its level (0.6%, carried on my own watch list since June).** Adding a candidate whose value I hold would be a **value-informed selection**, which is precisely the contamination this blind pass exists to prevent — and it would tilt the same direction as my logged bias, since a low-reading instrument makes the >2.5% letter *harder* to fire. ⚠️ **I am recording the exclusion rather than silently omitting it, so that a later reader can see the choice was made and why, and can overrule it deliberately.** If Will or PROME judges CDLI admissible notwithstanding, that is their call to make **with the contamination disclosed** — not mine to make quietly.

## 7. What this spec does NOT establish

- **No candidate has been verified to pass C1's basis test.** Fitch's cost-vs-FV treatment is unknown to me and is the single most likely disqualifier of the sole survivor.
- **No value of any kind was pulled**, so nothing here says whether the 2.5% line is near, far, or already crossed on any industry instrument.
- **C4 is unresolved** and, per §4, may remain so.
- **This is not live.** It resolves nothing until Will ratifies it as the resolver.

---

*Pre-registered 2026-08-13 under ruling ⑤. Superseded text preserved; no unrelated threshold touched; the 2.5% line and the 9/30 resolve date are UNCHANGED by this spec.*
