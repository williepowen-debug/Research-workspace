# BOND Receipt — 2026-08-15

**Run:** 2026-08-15 (Sat) ~12:30–13:15 ET · **Trigger:** Will — "drain the general inbox" · **Scope:** `PROTOCOL.md` § Inbox Processing, followed as written
*(Second BOND session of 8/15 — the ~11:50–12:20 boot is the prior commit `079bb425c`.)*

---

## Inbox

| File | Action | Why | Workbook rows | STATUS change | Outbox / packets |
|---|---|---|---|---|---|
| `2026-08-10_from-SAM_RETRACTION-no-us-agent-oat-seller…` | **INTEGRATE** | Withdrawn claim BOND never carried — checked before replying, no BOND surface had a US-agent OAT seller. The *material underneath* it is worth keeping. | `KB-BND-113` | — | → SAM |
| `2026-08-11_from-PROME_forum4-close-kalshi-erratum-boj-…` | **INTEGRATE** | MIDAS's DFII10 label correction lands on a figure BOND publishes. Kalshi-not-dark + BOJ cite-both-or-neither recorded. | `KB-BND-108` | **DFII10 row rewritten** | → NEXUS (count reconciled) |
| `2026-08-12_from-LABOR_T7-convergence-is-a-shared-antecedent…` | **INTEGRATE** | LABOR is right; the independence claim was in **BOND's own** T7 registration text. | `KB-BND-112` | **T7 registration: clause RETRACTED + vintage trap adopted** | → LABOR, cc NEXUS/PROME |
| `2026-08-12_from-NEXUS_your-c36-ruling-landed…` | **INTEGRATE** | Brief was 18 days stale; T-23 routed to BOND for ownership. | — | `NEXUS_BRIEF.md` **re-pinned** | → NEXUS |
| `2026-08-14_from-SAM_RETRACTION-2-fima-funded…` | **INTEGRATE** | Measured FIMA zero + §4 custody lead **explicitly handed to BOND for adjudication**. | `KB-BND-109/110/111` | **New STATUS section: Japan→UST supply, adjudicated** | → SAM (cc LIQUID) |

**All 5 `git mv`'d to `inbox/processed/`. Inbox EMPTY. WALTER lane EMPTY (drained in the prior session).**

---

## The work, ranked by consequence

### 1. 🔴 SAM's custody lead — ADJUDICATED, and the verdict inverts the read

SAM handed this over explicitly (*"This is your domain. I am naming the instrument and the numbers, not the verdict."*). Pulled **57 H.4.1 releases** from the Fed primary — FRED's custody family (`WMTSECL` et al.) was discontinued **2012-11-07**, which is a fact about FRED and not about the data.

| Window | Δ Wed level | z | pctile |
|---|---:|---:|---|
| **BUILD** 7/16 → 7/30 | **+58,716mn** | **+2.45** | **100th — largest 2wk build in sample** |
| **UNWIND** 7/30 → 8/13 | −59,791mn | −1.68 | 2nd — largest 2wk decline |
| **NET** 7/16 → 8/13 | **−1,075mn** | — | **≈ zero** |

**The four rows SAM sent show only the unwind half, which reads as "foreign officials sold ~$60B around the intervention." With the preceding fortnight attached the level round-tripped and net-changed by nothing** — 8/13 sits within $1.1B of 7/16 and $0.4B of 7/09. **The build is the more anomalous half.** Also resolved SAM's flagged basis disagreement: weekly-average net **+18,530mn** vs Wednesday **−1,075mn** — opposite signs, same substance. ⚠️ **The secular decline is separate and real: YoY −257,964mn.**

### 2. 🔴 Parser defect caught BEFORE publication

First-pass scraper's numeric regex required 4+ chars and **silently skipped week/week changes under 1,000**, shifting the column index onto the **federal agency debt** row. 4 of 57 releases produced apparent weekly changes of **−2.6M (the whole level)**; base-rate stdev came out **980,561 against a true 20,347**. Nothing errored. **The op-window rows were never affected — what was wrong was the base rate I was about to grade against.** v2 fails loud on a band violation and reconciles the release's own printed Δ against my differenced averages: **0 mismatches in 56 consecutive pairs.** `KB-BND-110`.

### 3. 🔴 DFII10 "series high" — wrong three ways

All-time max **3.15 (2008-11-21)**; **133 pre-2026 obs exceed the 2026 max** (last 2.52, 2023-10-25) ⇒ correct label is **post-2023 / ~2.75yr high**; and **the 2026 peak is 2.47 (7/31), not the 2.43 carried.** MIDAS caught the first two; **the third nobody had flagged.** Consequence: the TLT add-gate's closest approach this cycle was **3bp**, not the 7bp published. **Gate still never fired.**

### 4. 🟠 T7 independence claim — retracted, my error

LABOR graded off the **7/29 statement + Warsh presser**; T7 grades **the minutes of that same meeting** ⇒ shared antecedent. **I asserted the provenance of LABOR's work without checking it.** Clause struck from the registration; the frozen CONFIRM/DENY/AMBIGUOUS text untouched. **Vintage trap adopted as binding: grade the 111K / −74K vintage the Committee actually held, never today's +20K / −103K.**

---

## Files written

`STATUS.md` (DFII10 row · T7 registration · new Japan→UST-supply section) · `NEXUS_BRIEF.md` (**re-pinned 7/28 → 8/15**, superseding block prepended, 7/28 body bannered and retained) · `PROTOCOL.md` (**stale FR2004 "known access gap" corrected — it closed 7/28 and the line had told 18 days of sessions not to try**; H.4.1 custody route added) · `workbook/KB.tsv` **+6 (`KB-BND-108…113`, 114 rows / 13 fields validated)** · `docket/CATALYSTS.tsv` **+2 (8/31 MOF, 11/13 FRBNY Q3)** · `RECEIPT.md` · `SCRATCH.md`.

## Packets out (self-authored → committed by me, root carve-out ①)

**SAM** (cc LIQUID) — custody verdict + both retractions accepted · **LABOR** (cc NEXUS/PROME) — concession + vintage trap adopted · **NEXUS** — re-pin, T-23 accepted, three wrong figures flagged.

## Verdict

**No threshold moved. No vector moved. No position change — TLT puts HOLD, no add. Composite unchanged 12/35.**

**`FL-BND-11` is the one substantive change: "actual MOF intervention = mechanical UST reserve selling = long-end supply shock" is now recorded as CONDITIONAL on the funding channel, with neither branch confirmed.** It was written as automatic before this drain. **That correction came entirely from another desk retracting its own work twice in five days.**
