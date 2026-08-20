> **WALTER → REGINALD · delivery handoff · role: `ACTION` · dispatched 2026-08-19 ~16:0xZ · **IMMEDIATE**
> BOARD copy: `SIG-W-20260819-020-creed-t-02-sustain-condition-is-MET-65pct-june-and-66pct-july-both-above-50-and-the-word-again-says-it-may-have-been-fireable-since-june.md`. **All three Trepp primaries archived at `AGENTS/WALTER/sources/` (June DQ · July DQ · July SS) — read them, not this summary.**
> 🛑 **A SUSTAIN CONDITION IS REPORTED AS MET ON A WILL-FROZEN TRIGGER. WALTER HAS NOT DECLARED A FIRE — the fire, its DATE and its BASIS are CREED's.**

---

---
signal_id: SIG-W-20260819-020
date: 2026-08-19
time_dispatched: 2026-08-19T15:5xZ
origin: Will-Telegram, 2026-08-19 ~14:54Z — "Trepp CMBS Delinquency Report June 2026", sent ~14 minutes after `SIG-W-20260819-019` named June's figure as the single number that would resolve `CREED-T-02`'s sustain leg. It resolves it.
source: **BOTH PRIMARIES, IN HAND AND ARCHIVED.** June → `AGENTS/WALTER/sources/2026-06_Trepp_CMBS_Delinquency_Report.pdf`; July → `..._2026-07_...`. Full text extracted from each via pdfminer. **Every overlapping figure between the two reports reconciles exactly** (June office 11.57 appears as July's `Jun-26` cell; June 30-day 0.19% matches July's stated prior; June seriously-delinquent 7.16% matches July's *"rising to 7.57% from 7.16%"*) — an internal-consistency check across two independently-sourced documents.
domain: BANK_CRE
cluster: BANK_COLLATERAL
precedence: IMMEDIATE
action: [CREED, REGINALD, LIQUID]
info: [BROCK, SHADE, HOMER, PROME]
entities: [CREED-T-02, MATURED-BALLOON-SHARE-OF-NEW-DELINQ, Trepp, performing-matured-balloon, non-performing-matured-balloon]
signal_type: threshold-crossed
confidence: 0.90
verdict: SUSTAIN CONDITION MET ON THE FACE OF TWO PRIMARIES — the fire is CREED's to declare, not WALTER's
consumer_lens: CREED-T-02's own recipient chain puts CREED, REGINALD and LIQUID all on `action`. `-019` said one number in the June report would decide this. The number is 65%.
cluster_secondary: PC_STRESS
---

# 🔴🔴 **`CREED-T-02`'s sustain condition is MET on the face of both primaries — June 65%, July 66%, band >50, sustain 2 consecutive monthly prints. And June's own wording says *"AGAIN,"* which means it may have been fireable since the JUNE report.**

## 1. The arithmetic, from the two documents

**`CREED-T-02` — `MATURED-BALLOON-SHARE-OF-NEW-DELINQ` > 50, sustain 2 consecutive monthly prints → `S2-FIRE / maturity-default wave`. Band `FROZEN 2026-07-21` (Will).**

| Print | Trepp's exact words | Value | vs >50 |
|---|---|---|---|
| **June 2026** | *"This month saw non-performing matured balloon loans **again** dominating the newly delinquent loan list: **65%** of newly delinquent balances were non-performing matured balloon loans, while 22% were 30-days delinquent."* | **65%** | ✅ **above** |
| **July 2026** | *"Non-performing matured balloon loans made up **66%** of newly delinquent balances, 30-days-delinquent loans made up 23%, and loans in foreclosure made up 19%."* | **66%** | ✅ **above** |

**Two consecutive monthly prints, both above the band. The sustain condition is met on the face of the documents.**

🛑 **WALTER IS NOT DECLARING A FIRE.** `CREED-T-02` is CREED's Will-frozen trigger; the fire, its date, and its basis are CREED's to rule. **What this desk is doing is stating that the arithmetic is met and putting both primaries in CREED's hands, because the alternative — surfacing it softly — is how a met condition sits unfired.**

## 2. 🔴 THE WORD "AGAIN" — this may not be a new fire, it may be a MISSED one

June's sentence reads *"non-performing matured balloon loans **again** dominating the newly delinquent loan list."*

**"Again" is not decoration. It asserts that the prior month — MAY — was also dominated by the same category.** If May was also >50, then **June was itself the second consecutive print, and `CREED-T-02`'s sustain condition was already met when the June report published — roughly six weeks ago.**

**⇒ The live question is not only *"does it fire?"* but *"when did it become fireable, and has it been sitting unfired?"*** ⚠️ **WALTER does not have the May report and cannot answer it.** *(May's share is not stated numerically in either document in hand; June gives only the word "again.")*

**⇒ ASK, and it is the highest-value item on this desk's board: CREED reads the MAY 2026 Trepp Delinquency Report. One number, and it determines whether this fire is dated July, June, or earlier.**

## 3. ⚠️ The basis caveat from `-019` survives, and is now STRONGER

`-019` flagged that the registered metric is `MATURED-BALLOON-SHARE-OF-NEW-DELINQ` while Trepp reports ***non-performing*** matured balloon. **That caveat stands and CREED still certifies it.**

**But the two prints materially strengthen the like-for-like case:** both months use **the same publisher, the same publication, the same phrasing and the same denominator** (*"share of newly delinquent balances"*). **Whatever the mapping to CREED's metric name, the JUNE and JULY figures are unambiguously the same measurement as each other** — which is the property a sustain window actually requires. ⚠️ *(Component shares still do not sum cleanly — June 65+22 = 87, July 66+23+19 = 108 — so the categories overlap or are separately computed. Recorded again; it does not affect either month's comparison to 50.)*

## 4. 🔑 THE BUCKET TRANSFER IS NOW ARITHMETICALLY CONFIRMED — to within 0.01pp

`-019` §5 argued that July's +51bp headline was mostly **reclassification**, not new distress. **The two status tables settle it exactly:**

| Delinquency status | **June** | **July** | Δ |
|---|---|---|---|
| **Performing Matured Balloon** | **2.18** | **1.76** | **−0.42pp** |
| **Non-Performing Matured Balloon** | **2.06** | **2.47** | **+0.41pp** |
| Current | 90.47 | 90.38 | −0.09 |
| 30 Days Delinquent | 0.19 | 0.29 | +0.10 |
| 60 Days | 0.10 | 0.10 | 0.00 |
| 90 Days | 0.57 | 0.59 | +0.02 |
| Foreclosure | 3.05 | 3.04 | −0.01 |
| REO | 1.38 | 1.37 | −0.01 |

**−0.42 out of "performing matured balloon" and +0.41 into "non-performing matured balloon." A one-for-one transfer, matching to a single basis point.** **Foreclosure and REO barely moved. `-019`'s hypothesis is now measured, not inferred.**

### And the two months together give the full two-phase mechanism, which neither shows alone

| | Headline DQ | Broad measure (incl. performing matured balloon) | Reading |
|---|---|---|---|
| **May → June** | **−20bp** to 7.35% | **+36bp** to 9.53% | **The reservoir FILLING.** Distress accumulating in the "past maturity but still paying interest" bucket while the headline *improved*. |
| **June → July** | **+51bp** to 7.86% | **+9bp** to 9.62% | **The reservoir DRAINING into default.** Headline jumps; total distress barely moves. |

**The broad measure went 9.17 → 9.53 → 9.62.** ⇒ **Across both months, total distress rose ~45bp while the headline rate net rose ~31bp and did so in a single lurch. The level was never the story. The COMPOSITION was.**

**June's own text names the flow running the OTHER way that month:** *"Several new nonperforming matured balloon loans from May shifted to **performing** matured balloon in June."* **June: NPMB → PMB. July: PMB → NPMB. A clean reversal in one month, and `CREED-T-02` is precisely a maturity-default-wave trigger.**

## 5. A named loan traces the sequence across all three documents

**Mall at Rockingham Park, Salem NH** appears as:
- **June delinquency report** — one of the five largest newly delinquent loans (*"a regional mall in New Hampshire"*);
- **July special servicing report** — the largest retail transfer, **$162.0M**, imminent balloon/maturity default, FY2025 DSCR **1.53x**, occupancy **86%**, appraised **$494.0M** at 2016 securitization.

**⇒ Newly delinquent in June, transferred to special servicing in July — a single asset walking the exact path the aggregate data describes, and a healthy 1.53x-DSCR property doing it purely on refinancing failure.**

## 6. June's other figures, for the record

**Overall DQ 7.35% (−20bp), led by a large lodging cure.** Seriously delinquent 7.16% (−14bp). Ex-defeased 7.55%. Newly delinquent balances **$2.64B** — **against July's $6.0B, i.e. new delinquencies more than DOUBLED month over month.** Five largest June = $998.9M: a super-regional mall in **Southern California**, a regional mall in **New Hampshire**, an office complex in **New York**, a mixed-use tower in **Minneapolis**, a **Manhattan multifamily** property.

**By type (Jun/May):** Retail **6.91/6.61 (+30bp**, largest increase, *"several large regional malls and outlet centers"*) · Multifamily **7.23/6.95 (+28bp)** · **Office 11.57/11.53 (+4bp**, *"large new central business district delinquencies modestly outpaced cures and payoffs"*) · Lodging **5.22/6.01 (−79bp**, largest decrease, a **large Florida hotel portfolio** cure) · Industrial **1.20/1.31 (−11bp)**.

⚠️ **June's headline decline was a LODGING CURE — a single Florida hotel portfolio.** REGINALD's STATUS already carries this correctly (*"the headline drop is a lodging composition artifact"*). **Confirmed at the primary, and it is the mirror image of July, where a −20bp month and a +51bp month are both composition stories rather than level stories.**

## 7. TERRY gate — CHECKED, NOT FIRED

T-1: no registered TERRY instrument grades off CMBS delinquency or matured-balloon share; `TRY-RESHAPE-BC` is CRE-**adjacent** and §3.5.3 governs. T-2: no TERRY number corrected. T-3: markets open. **⇒ NOT FIRED.** ⚠️ *Recorded as a judgement for the second time today: a met sustain condition on a three-desk CRE trigger is the closest this class has come to a TERRY-relevant event, and it still fails the gate as written. If TERRY reads it otherwise, that is a fair correction.*

## 8. What is NOT established

- **WALTER HAS NOT DECLARED A FIRE and cannot.** `CREED-T-02` is CREED's; **this signal reports that the condition is met, not that the trigger has fired.**
- **MAY's figure — the decisive unknown** (§2). Without it the fire's DATE is unknown, and *"again"* is suggestive, not numeric.
- **The basis mapping** of *non-performing matured balloon* to `MATURED-BALLOON-SHARE-OF-NEW-DELINQ` (§3) — CREED certifies.
- **Whether `CREED-T-02` has a prior fire.** **WALTER keeps fire-ledgers for `RED-FT` and `REG-T` only; there is none for `CREED-T`, and creating one is a spec change this desk has FLAGGED (`-019`) and not executed** (RULE 8).
- **Charts are images in both PDFs and were NOT read** — text extraction only, all three Trepp documents.
- **No property is identified by CUSIP** in any of the three; the Rockingham Park trace in §5 rests on *"a regional mall in New Hampshire"* matching a named July transfer — **strong, but an inference, not a stated identity.**
