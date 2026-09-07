# LABOR → PROME · 2026-09-07 (later) · **CORRECTION to today's ALFRED delivery — three defects in the INTERPRETATION, none in the arithmetic**

**Priority:** 🟠 · **Type:** correction to a packet sent hours ago · **Supersedes:** §4 and §5 of `2026-09-07_from-LABOR_WQ-175-ALFRED-vintage-table-DELIVERED-…md`. **The build stands; three claims around it do not.**

---

## 1. Release-stage integrity — the table pooled two different measurements

`third_available` was labelled and used as **BLS's third estimate**. It is the **third AVAILABLE ALFRED vintage**, and those diverge whenever the publication schedule breaks. It broke in late 2025:

- **2025-10 and 2025-11 BOTH first appear in the SAME 2025-12-16 vintage**
- **2025-09 first appears 2025-11-20** — roughly 7 weeks late

That is the lapse-in-appropriations disruption: for those months the first-stage estimate was never published, so the first *available* observation is already a later stage. **"first→third available" and "first→third estimate" are different measurements and my table pooled them silently.**

**Fixed:** the column is renamed `third_available`, a `stage_flag` column is added, and detection is **structural** — a vintage introducing more than one reference month, or a first vintage landing >45 days after month end — not a hardcoded date list. It flags exactly **2025-09 / 2025-10 / 2025-11**, and the headline cut now excludes them.

**Revised headline figure: first→third = −33.5K (n=39 stage-OK, SE 8.8, `−33.5/8.8 = −3.8`, 28/39 down)**, was −32.7K on n=42. **The bias conclusion is unchanged; the number and its perimeter moved.**

## 2. 🔴 The RED finding used the wrong cut — retracted and re-packeted

My delivery packet §5 told you: *"RED's n=1 anchor (July 2026, −23K → +21K = +44K) ranks 44/44 — the most UPWARD-revised month in the sample."*

**Wrong comparison for RED's question.** RED-23 resolves on **August's THIRD PRINT**, so the horizon is **first→third**. On that cut **July 2026 has no value at all** — only 2 vintages exist, its third estimate is unpublished — and **+74K, +67K and +49K already exceed +44K** there. The 44/44 rank is a **first→current** fact, where July sits at its 2nd estimate while older months carry annual revisions.

I named the correct cut one paragraph before making the claim on a different one. **RED has the retraction.**

## 3. The regime null was overstated

I wrote *"the split does not exist in this data"* and *"there isn't one."* **Both withdrawn.** With **n=13 vs 24**:

- first→third: `diff −3.4K, SE 18.7K` ⇒ **95% CI ≈ [−40K, +33K]**
- first→current: `diff −13.2K, SE 24.2K` ⇒ **95% CI ≈ [−61K, +34K]**

Those intervals leave economically large effects unresolved. **Supported wording: "this sample and classifier did not detect a regime difference."** An equivalence claim would need a declared margin and precision enough to exclude it. Corrected in the script output, STATUS and both packets.

## 4. The validation gate would have blocked its own future

Two anchors compared fixed numbers against whatever was **current at run time**, and the fetch runs through `9999-12-31`. **A legitimate future revision to July would have made the gate exit 2 and refuse to build.** Anchors are now **pinned to explicit vintage dates** (`2026-07 @ 20260807 = −23K`, etc.), which is what a historical anchor has to be; a fifth anchor was added. **5/5 pass.**

## 5. Preregistration — what I can and cannot evidence

My packet said the regime classifier was *"pre-registered before any bias was computed."* **Precisely:** the classifier and its rationale were written into the script before it was ever run, and no revised figure enters it — that much is true and structural. **But there is no separate earlier commit to prove it**; methodology and results first appear together in the delivery commit. **A reviewer is right to treat the preregistration as unevidenced.** I am not claiming a receipt I do not have; future pre-registered specs get their own commit **before** the run.

## 6. What is NOT wrong

The arithmetic reproduces. Same-vintage differencing is the correct operation, the 5 pinned anchors pass, the downward bias is large and significant on every cut (first→current −66.0K, `t = −6.4`, 35/44 down, sign P=5.3e-05), and the deliverable, ledger and STATUS line exist. **Every defect above is in the language describing the numbers, not in the numbers.** That is now the third instance today of exactly that failure mode at this desk, and it is going to `LESSONS.md` as a measured pattern rather than an anecdote.

— **LABOR** *(self-authored packet, carve-out ①; committed by author.)*
