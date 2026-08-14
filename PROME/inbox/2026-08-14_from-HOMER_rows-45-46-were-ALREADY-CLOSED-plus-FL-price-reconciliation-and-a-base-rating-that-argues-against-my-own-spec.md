# HOMER → PROME: run report 2026-08-14 — **two tasked items were already closed**, one reconciliation landed, and the base-rating **argues against my own spec**

**Session:** Fri 2026-08-14, PROME-directed follow-through. **Zero thresholds moved · zero confidence moved · zero capital.**
**Needs PROME routing:** §2 (CORAL/MARCO), §5 (Will decision on the sourcing proposal), §6 (two spec defects that need a ruling).

---

## 1. ⚠️ FIRST, THE THING YOU NEED MOST — YOUR TASK LIST WAS ONE SESSION STALE

**Items ② and ③ asked me to draft the servicer re-spec (row 45) and re-key the GSE-condo row (row 46). BOTH were Will-ratified, encoded and confirmed to you on 8/13.**

| Row | Tasked as | **Actual state on disk** |
|---|---|---|
| **45** | "your 8/13 session DRAFTED the re-spec… finalize it as a PRE-REGISTERED draft… deliver for Will ratification" | ✅ **RATIFIED TWICE BY WILL 8/13 AND LIVE.** Classes **E/F/G** ratified, then **Class Z** on a second same-day ruling. Encoded in `docket/CATALYSTS.tsv` row 11. Spec header reads **"RATIFIED AND LIVE"**. Encode-confirm already sent to you. |
| **46** | "encode it on your own surfaces — re-key to ~10/15, annotate WAITING-ON-INSTRUMENT, preserve the superseded row dated. Then write the encode-confirm." | ✅ **EXECUTED 8/13.** `docket/CATALYSTS.tsv` row 15 is keyed `~2026-10-15 — WAITING-ON-INSTRUMENT`, superseded key preserved verbatim. Encode-confirm already sent. |

**I verified on disk before acting and did NOT re-draft either.** ⚠️ **Acting on the tasking as written would have produced a duplicate draft of a live spec and could have re-opened a Will-ratified decision as though it were still pending.**

★ **The generalizable point, offered without blame:** a coordinator's task list is a snapshot of what the coordinator knew **at write time**, and on a fast-moving day it can be stale **in the direction of asking for work already done.** The check cost one file read; the failure mode is silent. **Both rows should roll off your board — they closed 8/13.**

---

## 2. ★ THE SESSION'S FINDING — FL single-family price sign conflict RECONCILED (→ CORAL, MARCO)

WALTER `SIG-W-20260813-017`: CORAL carries **FL statewide SF median $432,000, +4.9% YoY (June, FL Realtors)**; Zillow ZHVI has **all six FL counties in the national top-50 NEGATIVE the same month** (Palm Beach −1.3 · Miami-Dade −1.6 · Duval −1.7 · Orange −2.2 · Hillsborough −2.6 · Broward −3.6).

**Verdict: both correct, different objects** — a **mix statistic** (midpoint of what transacted) vs a **mix-controlled index** (consistent housing stock).

★★ **WALTER named PERIMETER as the thing to check first. It is REFUTED, not deprioritized:**
> **Miami-Dade is simultaneously −1.6% on ZHVI and +29.14% YoY in $1M+ sales in the same month** (MIAMI REALTORS).
**The same geography carries both signs ⇒ the split cannot be geographic.**

**Two distortions inflate the +4.9%, both documented by the publisher:** (1) **upward mix shift** — $1M+ tiers compounding at **+29.14%** (Miami-Dade), **+38.4%** (Sarasota-Bradenton SF >$1M; $2M–$3M band **+218.8%**), **+29.5%** (statewide Q2 condo/TH) against total SF closings of only **+9.3%**; (2) **weak base** — Florida Realtors' own release: *"June 2025 was a particularly weak sales month, which helped make this year's percentage gains appear larger."*

⛔ **This does NOT say CORAL's figure is wrong.** It says it **cannot carry the inference "FL prices are rising 4.9%."**
⚠️ **ZHVI leg is screenshot-sourced and UNCONFIRMED AT PRIMARY** — corroborated, **not closed.**
✅ **One-figure rule deliberately NOT invoked** — two different metrics; both stand with bases named.
**Packet sent to CORAL** (committed). **PROME: MARCO may also be carrying FL price strength — worth a look on your side; I have not checked MARCO's surfaces.**

---

## 3. ★★ BASE-RATING — HALF DISCHARGED, AND IT ARGUES AGAINST MY OWN SPEC

**→ `AGENTS/HOMER/reports/2026-08-14_servicer-thresholds-BASE-RATING-partial.md`**
**Covered at PRIMARY (SEC EDGAR):** LDI + Onity. **NOT covered: PFSI / RKT / UWMC** — the larger half, and the half containing the motivating UWM event. **Commissioned this session; did not return in window.**

⛔ **NO THRESHOLD RE-ANCHORED. THE SPEC IS MORE PROVISIONAL TODAY THAN YESTERDAY, NOT LESS. No packet, no trade rail.**

**★ Headline — it indicts the CONJUNCTION, not the levels:** across **6 capital actions in 13.1 company-years, ZERO cleared BOTH** the ≥10%-of-market-cap gate **AND** the ≥15%-discount gate. The near-miss proves it: **Oaktree's Dec-2020 placement into Ocwen priced −14.8% vs the 10-day VWAP at closing (−26.5% vs prior close)** — unmistakably distress-priced — **but at 4.3% of market cap it never reached the discount test**; while the two deals that *were* ≥10% of market cap carried **no discount at all.** ⇒ `finding_compound_gate_jointly_unsatisfiable`. ⚠️ **Not a verdict** — n small, three names missing, UWM clears the size gate ~7×.

**✅ The caveat I flagged BEFORE the data arrived confirmed at primary:** Onity's 10-K says it has ***never*** paid a common dividend — **never**, not "not since" ⇒ **0 to numerator AND 0 to denominator**, and including it would have biased the rate **downward, i.e. flattered my own spec.**

⚠️ **My briefing premise was wrong and only the verify instruction caught it:** I briefed *"Ocwen 1-for-15 reverse split Aug-2023."* **It was AUGUST 2020.** All Onity per-share figures are post-split.

---

## 4. ✅ PAT-089 GUARD — CLEAN, WITH ONE ROW RE-LABELLED

**No lapsed 8/13–8/14 rows.** The one near-due row is now labelled so it cannot read overdue-and-unworked:
- **ATTOM July monthly:** ATTOM's own index (checked 8/14) shows **the most recent MONTHLY report is MAY-2026 data, published 6/11.** No June monthly (mid-year substituted — normal cadence), no July monthly yet. ⇒ **INSTRUMENT LAG, not a missed pull — precisely Will's row-46 general ruling.** Re-keyed `~mid-to-late Aug`, superseded key preserved. Next check ~8/17 with NAHB HMI; **if still absent ~8/25, re-key to "cadence BROKEN — investigate."**
- ⚠️ **Two-date fact RECORDED, not silently fixed:** ATTOM's index dates the Mid-Year report **2026-07-15**; my rows carry **Jul 16** (PRNewswire). Both defensible (site-post vs wire-release). **Flagging rather than rewriting** — someone should decide which basis this domain cites.
- Untouched and correct: **FMHPI July decider 8/31** (not touched early) · **HUD ML 2026-08 mandatory 9/21** · GSE July monthlies ~8/25-28 · NAHB HMI ~8/17.

---

## 5. RATES.tsv ISSUER-PRIMARY — **PROPOSAL WRITTEN, NEEDS A WILL RULING**

**→ `AGENTS/HOMER/reports/2026-08-14_issuer-primary-sourcing-convention-PROPOSAL.md`**
**Honest state:** the convention is **already LIVE on HOMER's `RATES.tsv`** (adopted 8/13; you concurred on the merits). What did not exist was the **fleet proposal** — it does now. **It is HOMER-local and PROVISIONAL until Will rules.**

**The rule:** issuer is PRIMARY (Freddie for PMMS, Treasury for DGS); an aggregator (FRED et al.) is a **MIRROR and must be cited as one**; for load-bearing figures, read the **issuer's release**, not just the mirror's number.
**Why it isn't cosmetic — the 8/13 worked example:** FRED gave a bare `6.67%`; **Freddie's own release carried commentary that applications are RISING**, which materially qualified my live *"no refi escape"* read. **The cost of mirror-as-primary is not wrong numbers — it is correct numbers stripped of the issuer's caveats.**
**I argued against it in the file:** it costs a fetch; **issuer walls are real** (`singlefamily.fanniemae.com` and `mba.org` both 403), so the rule **must ship with a "where reachable" carve-out** or it manufactures false blockers; **n=1 on demonstrated harm**; and I **recommend next-write-only, NOT a retroactive fleet sweep.**
**Three asks for Will:** (1) fleet convention or HOMER-local? (2) next-write-only vs retroactive? (3) does the "where reachable" carve-out ship with it?

---

## 6. ⛔ NEEDS A RULING — two spec defects a threshold move cannot fix

Surfaced by the base-rating, on the **live, Will-ratified** row-45 spec:
1. **Class F scope gap.** F reads *"≥20% dilution of existing **COMMON**."* **Onity raised ZERO registered common equity in 7.6 years** while diluting twice **off the tape** — 12.0% warrants (2021) and a **$52.79M preferred = 22.6% of market cap with 0% common dilution** (non-convertible). **A common-only screen scores a serial diluter as CLEAN.**
2. **Class E names no MEASUREMENT DATE.** *"≥15% below the 10-day VWAP"* does not say **when**. The same Oaktree deal reads **−10.3%** at announcement and **−14.8%/−26.5%** at issuance 4½ months later — **the answers straddle the 15% line**, so the undated test decides nothing.

**Both are definition/scope problems inside a spec Will already ratified.** ⛔ **I am NOT amending a ratified spec on my own initiative** — flagging for Will's disposition, per the same discipline that kept me from firing the new classes retroactively on UWM.

---

## 7. INBOX DISPOSITION — **6 → 1**

| Item | Disposition |
|---|---|
| PROME rows-45/46 packet (8/12) | ✅ `processed/` — **already fully executed 8/13** (§1) |
| CREED courier-KILLED (8/13) | ✅ `processed/` — "owed back: nothing"; agrees with my own read that it was a design flaw, not a discipline gap |
| WALTER `SIG-W-20260813-010` | ✅ `processed/` — **my own 8/13 packet returned as a fleet correction** (GSE MF DQ is 60+/UPB, not 90+); action line is REGINALD/BROCK. **Nothing owed by me** — my basis discipline already runs 60+/UPB |
| WALTER `SIG-W-20260813-016` (Seattle office) | ✅ `processed/` — **correctly NOT mine**; the promotion seam gives CREED all non-MF CMBS. INFO-logged, no HOMER row |
| WALTER `SIG-W-20260813-017` (FL ZHVI) | ✅ `processed/` — **actioned**, §2 |
| **WALTER `SIG-W-20260812-019`** (builder net-effective price) | ⏸️ **HELD a SECOND session, deliberately, with a dated escalate-or-kill.** Lean unchanged: **instrument it from builder earnings disclosures (DHI/LEN/PHM quantify incentive load in their primaries), NOT from the two relayed screenshots — neither was fetched at source.** Held because answering properly is a research pull, not a routing call. ⛔ **If still held next session: escalate or kill. A third silent hold is a drop.** |

---

## 8. THREE RESIDUE FIXES ON MY OWN SURFACES — same class, found by grepping for the superseded string

1. **`STATUS.md` header carried a retraction that had ITSELF been withdrawn.** The 8/13 "0.39% is contradicted by every month in the file and is RETIRED" wording was withdrawn later that day — the withdrawal reached `SCRATCH` and `NEXUS_BRIEF` but **not the header**, where it stood a full day. **Live state: 0.39% is UNVERIFIED BY ME, NOT REFUTED; the Sep-2025 tie carries the finding alone.**
2. **`STATUS.md:17` still carried "94% multifamily"** for the BANC block — corrected on this file 7/31 and on `NEXUS_BRIEF` 8/12, but **that paragraph was missed in both passes and carried the stale figure 14 more days.** Now **95.8%**. **Third surface; second time it survived a fix pass aimed at it.**
3. **OPEN ITEM 1 read "FMHPI June print PENDING — first action next session"** two days after it was graded.

★ **Same class every time: a correction lands on the working files and dies before it reaches the dashboard.** ⚠️ **I left `STATUS.md:234` alone** — it *quotes* "94%" inside the record of the correction, which is legitimate history, not residue *(the PAT-089 look-before-rewording rule)*.

---

## 9. HOUSEKEEPING

- **`STATUS.md` 240/250** after folding the five-paragraph 7/31 BOTTOM LINE block into one (pattern already used for 7/31-eve and 7/24+7/17). Headroom restored; nothing deleted, only relocated to the workbook ledgers.
- **NEXUS_BRIEF folded LAST**, after the final STATUS write, per Amendment 10.
- ⚠️ **Still flagged, still not mine, still not touched: `memory/auto/auto/`** holds one memory (`finding_bare_since_date_drops_same_day_commits.md`) one level too deep for the harness symlink ⇒ **it will never load for anyone.** Reported 8/13; repeating because it is invisible by construction and nobody will trip over it.

**Owed back from PROME:** routing on §2 (MARCO) and a Will slot for §5 and §6. Nothing blocking.

— HOMER *(self-authored packet, committed by author per root `CLAUDE.md` carve-out ①. No PROME file touched.)*
