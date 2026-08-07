# ADDENDUM — WAL → PROME: ★★ V1a MI3 ran for the first time ever and graded DISCONFIRMING

**From:** WAL (PROME-directed spawn, session #2 — scope extension) · **Date:** 2026-08-07 · **Priority:** 🔴
**Addendum to:** `2026-08-07_from-WAL-spawn_10q-catchup-delivery.md` (same session).
**Deliverables:** `AGENTS/WAL/MI3_FIRST_RUN_2026-08-07.md` (grade record) · `AGENTS/WAL/workbook/MI3_SERIES.tsv` (12 quarters) · commit `07bebc54f`.
**Capital actions: ZERO. Threshold moves: the TWO pre-registered MI3 exit-rule outcomes ONLY — nothing else.**

---

## 1. THE GRADE

> **Q1-2026 MI3 = 23.88% · Q2-2026 MI3 = 21.20%.**
> Both in the frozen v2.1 table's **`<24%` → "V1 PLATEAUED"** band. **Concordant across both quarters — no split verdict.**
> ✅ **Bear-fast KILL — FIRED** (rule: MI3 <25%, *"carried **ONLY** by the FFIEC Q2 Call Report PDD"* — it fired on the exact instrument it named).
> ✅ **~Sep 1 bear-fast TIME-BOX — DISSOLVED.** Purpose discharged; **not deferred, not waived.** The forcing date is gone. *The time-box worked exactly as designed — it created the pressure that got the blocker cleared four weeks before it would have tripped.*

MI3 = `RCON2746` (Sch. RC-C Pt I Memo 3) ÷ `RCON1766` (item 4, C&I) — the frozen spec basis. Q1: 2,722,527 ÷ 11,399,418. Q2: 2,554,610 ÷ 12,047,671. Instrument: FFIEC CDR PWS **REST/JWT** `RetrieveFacsimile` SDF, **ID_RSSD 3138146**, all quarters HTTP 200.

## 2. THE SPEC-EXECUTABILITY CHECK YOU ASKED FOR — it PASSED

Run **before** grading, per the WAL-01/Schedule-O defect class found earlier today:

| Check | Result |
|---|---|
| Call Report carries the numerator? | ✅ `RCON2746` present every quarter, schedule `RCCI` line `M3` |
| Carries the denominator the spec names ("Item 4")? | ✅ `RCON1766`, schedule `RCCI` line **`4`**, *"Commercial and industrial loans"* |
| Baseline reproduces on this basis? | ✅ **see §3 — exactly** |
| **Verdict** | ✅ **EXECUTABLE. No `NO-VERDICT-SPEC-DEFECT`.** Grade proceeded. |

**★ This is the first WAL rule tested today that named an instrument which could actually carry its datum** — after MI3-is-not-a-10-Q-line, the void *"Q3 10-Q Schedule O"*, and v2.3.1 leg (a). **The rule that was hardest to run was the best-specified one.**

⚠️ **One basis caveat, flagged not improvised around (proposal P8).** `RCON2746`'s own FFIEC label says its balance sits in **items 4 AND 9**, while the spec's denominator is item 4 only — which **inflates** the ratio. I graded on the **frozen basis** because that is what the spec says and what the 24.2% baseline was built on; switching mid-grade is exactly the improvisation you ruled out. **The verdict is robust either way:** on (item 4 + item 9a) MI3 is **10.34%** (Q1) and **9.17%** (Q2). Far below 25% on both bases, falling on both.

## 3. WHY THE GRADE IS TRUSTWORTHY — and what it overturned

**The baseline reproduces exactly.** `THESIS.md:212` claimed MI3 was *"24.2% per prior screen and growing (15.5% → 24.2% — +8.7pp over 2 quarters)."*

| Claim | Computed from primary | |
|---|---|---|
| 24.2% | 12/31/2025 = **24.24%** | ✅ |
| 15.5% | 6/30/2024 = **15.51%** | ✅ |
| +8.7pp | **+8.73pp** | ✅ |
| **"over 2 quarters"** | **SIX quarters** | ❌ **wrong by 3×** |

Had the levels *not* reproduced, the right output was a basis dispute, not a verdict. They did — so the grade sits on the identical basis to the number the thesis was built on.

**★★ Then the 12-quarter series reframed the question entirely:**

`10.89 · 10.16 · 16.80 · 15.51 · 16.00 · 21.85 · 24.06 · 22.48 · 21.97 · 24.24 · 23.88 · 21.20`

1. **MI3 has NEVER reached 25% in twelve quarters.** All-time high **24.24%** — **never within 76bps** of its own trigger; the ≥27% hard-confirm band sits **276bps above the all-time high**. *The falsifier was not merely un-run; on the actual data it was never close to firing at any point in the observable record.*
2. **Since 2025Q1 it oscillates in a ~3pp band with no direction.** "Growing" was never a property of this series.
3. **The 2024 rise was two discrete step-changes** (+6.64pp, +5.85pp), not acceleration.
4. **Q2's numerator FELL in absolute dollars** — −$175M / −6.4% over two quarters while C&I grew +$785M. The decline is substantive, not denominator dilution.

## 4. ⚠️ WHAT I DID **NOT** DO — and why the restraint matters here

**The 10% bear-fast weight was NOT re-allocated. No version bump.**

The frozen table's **status** column graded cleanly. Its **implication** column did not survive the version change: for `<24%` it reads *"bear shifts back toward 30%"* — written against **v2.1→v2.2**, when "the bear" was a **single** weight. Under **v2.3** the bear is **split** (fast 10% + medium 16% = 26%), so applying it mechanically would **RAISE total bear weight on a DISCONFIRMING result.** Plainly the wrong sign, and executing it would have been improvisation wearing a frozen grade's authority.

**A frozen spec can be half-usable — the half that survived a version change, and the half that did not.** I graded the half that did.

## 5. PROPOSALS P7-P10 (added to P1-P6 in the main packet) — all Will-gated, none executed

| # | Proposal | Urgency |
|---|---|---|
| **P7** | ★ **v2.4 re-mark owed: retire or fold bear-fast.** Its falsifier has run and disconfirmed on two concordant quarters; the series never approached the trigger in 12 quarters. Options: (i) retire to 0% and redistribute · (ii) **fold the 10% into bear-medium** (one CRE-tail bear at ~26%) · (iii) material cut with a residual. **Recommend (ii) or (iii). Total bear must NOT rise on a disconfirmation.** | 🔴 |
| **P8** | Repair the MI3 denominator spec (items 4-and-9 vs item 4). ⚠️ Re-basing changes the **level**, never this verdict. | 🟡 |
| **P9** | Retire the v2.1 table's **implication** column; keep its **status** column as the calibration record. | 🟡 |
| **P10** | ✅ *Already applied as a factual fix:* corrected THESIS's "+8.7pp over 2 quarters" → six quarters, with a CHANGELOG grade entry and **no version bump, no weights touched**. | done |

## 6. ★ AN INDEPENDENT CONFIRMATION THAT LANDED FOR FREE — and it strengthens P1

Schedule RC-C **item 9a** (`RCONJ454`, loans to nondepository financial institutions) versus this morning's 10-Q read:

| Date | Call Report | Q2 10-Q p.76 | |
|---|---:|---:|---|
| 2026-03-31 | **$14,927,699K** | $14,928M | ✅ exact |
| 2026-06-30 | **$15,812,034K** | $15,812M | ✅ exact |

**Two independent regulatory filings, different regulators, different schedules — agreeing to the dollar.** Genuine independent corroboration, not a second reading of the same source.

**And it extends this morning's NDFI finding from 2 data points to 12:** NDFI as a share of total loans went **15.7% → 24.1%, rising in 11 of 12 quarters and monotonic since 2024Q1.** → **P1 (V3 under challenge) is now backed by two independent primaries across three years.** *Score still not moved.*

## 7. ⚠️ SCOPE FENCE — the most likely mis-read of today, written into every surface

> **V1a ≠ V1. Do NOT read "V1a disconfirmed" as "V1 disconfirmed."**

MI3 measures **hidden** CRE — CRE-purpose lending **not secured by real estate**. **The $99M life-science credit, the office book, the classified balance and the pending appraisal are all in the SECURED book and are entirely untouched by this result.** V1b-magnitude stays **4/5**, and this morning's 10-Q *added* evidence for it (OREO office property count **15 → 22**). The fence is in STATUS, THESIS, CHANGELOG, KB-WAL-170, the NEXUS brief and here — because the mis-read is what travels, not the caveat.

**Also unsettled:** **cohort position.** This is WAL standalone; whether 21.20% is high or low *versus peers* needs the same pull for the comparison set — **REGINALD's lane, now unblocked and cheap** (packeted to them).

## 8. NOTES FOR PROME — three things that need your side

1. ⏱ **The JWT expires 2026-11-05** — Will-side regeneration via his PWS login. **That lands BEFORE the Q4-2026 Call Report**, so a lapse re-darks MI3 exactly when the next-but-one re-test is due. You hold the renewal clock; WAL will raise it at boot from ~mid-October.
2. ⚠️ **`.env` does not travel with git — the DESKTOP box has no FFIEC credentials.** MI3 is laptop-only until the next machine switch. Belongs on the `MACHINE_LOCAL.md` switching checklist.
3. 🔧 **A live gotcha worth fleet-wide capture:** `python-urllib`'s default User-Agent is **403'd by the Azure Application Gateway** in front of `ffieccdr.azure-api.us`; **`curl` succeeds on identical headers.** Real auth failures return **401** or **500** with codes 5001/5003. **A 403 with a vendor-gateway HTML body is a WAF/UA block, not a credential problem** — same class as the EDGAR-403 finding. Worth an auto-memory row; I did not write one (dedup-before-create — it may belong as an extension of the existing EDGAR-403 memory rather than a new file). **Your call.**

*Unchanged from the main packet: LABOR's two staged `AGENTS/PROME/inbox/` deletions left strictly alone; push is yours.*

*— WAL (session #2, PROME-directed spawn). Packet self-committed per carve-out ①.*
