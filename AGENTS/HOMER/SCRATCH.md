# HOMER SCRATCH — 2026-08-12 (Wed) — PROME-directed RECOVERY session

**Purpose:** Canonical ephemeral session handoff. Read at boot; rewrite at closeout. Durable findings → `MEMORY.md`/workbook; live state → `STATUS.md`.

**Shape of the session:** spawned by PROME with Will's approval to work the **five self-registered resolver dates that passed while HOMER was dark 12 days** (PAT-089 instance 3, DOCKET row 32, window 8/8–8/12 ending today) plus **two 🔴 figure defects on consumed surfaces**. All five graded, both defects closed, **and a sixth resolver — not on the list and more consequential than four that were — turned out to have been sitting available since 7/31.**

**Rules honored: every grade is against the frozen spec as written. Zero thresholds moved. Zero confidences moved. Zero capital. Where a spec was defective I recorded the defect and graded NO-CALL — I did not rewrite the spec in the same touch.**

---

## THE FIVE (all graded — full detail in `STATUS.md`, ledger rows in `workbook/`)

1. **Trepp July CMBS — RESOLVED.** MF **7.69% (+46bps)**, largest single-month move in my series; overall 7.86% (+51bps). ⚠️ **NOT a new high — Apr-2026 7.71% ATH stands 2bps above.** ⚠️ **Maturity-adjusted MF rate NOT published this month — that leg of my own spec is UNGRADED, not substituted.** ★ The MF leg and the index moved for **different reasons**: index = matured-balloon **refi** failure (66% of newly delinquent); MF = loans in **Ohio/Texas/New York going 30 days delinquent**, i.e. **payment** failure.
2. **LGI Homes Q2 — GRADED at PRIMARY** (SEC 8-K EX-99.1, 8/4). GM **19.8%, −306bps YoY** — compression holds. ★ **The +0.5% headline ASP is a COMPOSITION MASK**: at the Q2-2025 segment mix, 2026 segment ASPs blend to **−1.2%**. ★ **Florida is the worst segment: ASP −6.5% YoY bought +14.7% closings.** ★ Counter-signal recorded as such: **FY guide RAISED a second straight quarter**, first in my Q2 set.
3. **PMMS 8/6 — RESOLVED.** **6.69%, fifth straight rise, but only +3bps.** Neither 6.72 nor the 7.0% RED band crossed; **ORANGE on the letter of the band table.** ★ **My "30Y pre-load" framing named the wrong tenor** — PMMS tracks the 10Y and DGS10 was flat 4.71→4.69. ✅ **Spread recomputed to ~200bps; the 7/31 STALE-FLAG is cleared and ~187bps is retired.**
4. **GSE condo mandate 8/3 — EFFECTIVE: CONFIRMED. MECHANISM: NO-CALL.** Fannie **LL-2026-03** landed on schedule. ⚠️ **The instrument I registered (warrantable-vs-non-warrantable spread) cannot be read for ~60-90 days.** Earliest honest read **~Oct-Nov**.
5. **TX August auctions — RESOLVED, and the July decline REVERSED.** **>$1.15B / 47 loans**; **>50% of the whole Texas Triangle pipeline is multifamily SYNDICATOR paper**; county leader rotated **Dallas → Tarrant**. ⚠️ My carried "down from >$1B in May and June" was **wrong on June ($1.3B)**.

## ★ THE SIXTH — HOM-01 Leg-1, not on the list, biggest consequence

**The FMHPI June print had been out since 2026-07-31** — Freddie's own page: *"Posted on July 31, 2026: Latest data is for June 2026."* It landed **hours after** my 7/31 20:30 ET check read the prior stamp. **Neither side erred; then nobody looked for 12 days.**

**PRIMARY figures** (Freddie's own `fmhpi_master_file.csv`, `GEO_Type == 'US'`, pulled 8/12): **June YoY SA +2.06%, MoM SA +0.32%; May in that same vintage +1.58%.** CR mirror (pub **2026-08-03**, date-verified) matches the SA series exactly.

- **Leg-1 required June's YoY BELOW the prior month's as published in that same release: +2.1% vs +1.6% → printed ABOVE → LEG-1 NOT MET.**
- **Early-kill arm 1 of 2 has FIRED (>+1.9%). If the Jul-data release (~8/31) also prints >+1.9%, HOM-01 CLOSES MISSED EARLY and does not wait for its Sep resolver.**
- **Status stays OPEN. No confidence move** — one arm of a two-arm kill is not a resolution, and any mark move is Will-gated.
- ⚠️ **My carried May +1.9% was REVISED DOWN to +1.58%.** Grading against the carried figure would have shown +20bps of acceleration instead of the true +50bps.
- ⚠️ **Third consecutive year-trap on this series, and it INVERTED** — this month's stale candidate (CR's July-**2025** article, pub 2025-09-02) would have **falsely KILLED** the prediction where July's would have falsely confirmed it. **The trap is indifferent to direction; only the date check is.**
- ★ **The Realtor.com list-price lead is 0-for-1.** Its registered IF-MISSED clause is now **live and dated to 8/31**.

## 🔴 DEFECTS CLOSED

- **`STATUS.md` Miami-Dade condo cell** carried the **superseded 8.9mo statewide** figure while a row three lines below carried the correct **8.1mo (June)** — both written 7/31, wrong figure on the more-read cell, `STATE_HSG.tsv` correct throughout. **An INTRA-file contradiction: the CORAL lock held everywhere except inside my own file.** Fixed with a dated note.
- **`NEXUS_BRIEF:13`** still read **"94% multifamily"** for the BANC block 12 days after STATUS was corrected to **95.8%** — **the residue survived inside the 7/31 audit's own fix pass, on the surface REGINALD reads.** Fixed with a dated note.
- **Found while working, not on anyone's list: `docket/CATALYSTS.tsv` row 5 still carried the RETRACTED "stress concentrated in the unprotected leg" read** — retracted 7/31 eve, propagated to STATUS/NEXUS_BRIEF/MULTIFAMILY.tsv, **never to the docket.** Struck with the full corrected weight arithmetic. **Same class as the two above: a correction that reached the surfaces I checked and not the one I didn't.**
- **Date defect:** `docket/CATALYSTS.tsv` had NAR EHS at **8/10**; actual release **8/11** (`PRICING.tsv` was right). Corrected. **⚠️ I briefly wrote "8/20" into a `PRICING.tsv` header from memory before verifying — caught and fixed in the same session. Do not date a release from recall.**

## ⚠️ OPEN / UNSETTLED — do not let these get published as settled

1. **HOM-01 is one arm from an early MISS.** The 8/31 FMHPI July print decides it. **Grade on that release's own as-published figures for BOTH months — do NOT grade against the +2.1% recorded here.**
2. **Trepp's maturity-adjusted MF rate is UNHELD for July.** June's 9.53% has no counterpart. Do not carry 9.53% forward and do not substitute the overall-index mat-adj.
3. **"7.69% is a new high" is FALSE** — Apr-2026 7.71% stands. Kill on sight.
4. **The TX $1.15B level is single-source** (TRD proprietary series). Direction + composition are the finding; the dollar level is unverified at primary. County trustee postings are the primary and were not pulled.
5. **The "~700 South Florida / 1,438 statewide non-warrantable buildings" figure is UNVERIFIED and undated in its carrier. Do not publish.** Fannie's unavailable-projects list is the primary.
6. **The GSE-condo row is spec-defective:** a date-triggered catalyst whose instrument lags its own trigger by 60-90 days. It will read "overdue and unworked" at every boot until October regardless of diligence. **Needs a MEASUREMENT date distinct from its EFFECTIVE date — Will-gated, not fixed here.**
7. **The nonbank-servicer watch trigger is spec-defective and it just cost me a real event.** See below.
8. **Carried forward, unchanged:** $160B+ MF maturity wall still PROVISIONAL, re-source still owed to CREED · "post-GFC high" still NOT established on Freddie's quarterly series (Q3-25 also 0.51%) · GSE MF band re-spec still owed (warned, not re-banded) · Parcl/Reventure proprietary-index class still a cross-check flag only.

## 🔴 THE SERVICER-WATCH DEFECT — flagged to Will via PROME, NOT fixed

**UWM Holdings fell −49% intraday on 2026-08-06** (WALTER SIG-W-20260809-012, unprocessed in my inbox 3 days): Q2 **net loss $451.9M**, equity **$1.6B → $1.0B**, **first dividend suspension in company history**, **$2.05B rescue equity from Oaktree + SFS (Ishbia family)**. UWM is the **largest US mortgage lender by origination volume** and is already on my listed-servicer panel.

**On the LETTER of my standing trigger, this does NOT fire it.** The registered trigger enumerates *rating action / covenant breach / facility draw / emergency transfer*. **An emergency recapitalization is none of the four. Watch stays 🟠 — no trigger-fudging.**

**But that is the defect, not the verdict:** I wrote a trigger listing **liquidity** mechanisms and omitted the **recapitalization / going-concern** channel, so **the single largest US mortgage lender taking a rescue round cannot fire the watch that exists to catch exactly that.** Re-spec is Will-gated. **Do not quietly widen it.**

## SENT THIS SESSION (all committed — check `outbox/` is EMPTY, that is the point)

- **PROME** — the recovery rollup: one table, five rows + the HOM-01 addendum + the two defect closures + three asks.
- **CREED** — Trepp July figures + **the courier arrangement failed its first test**, plus the $160B+ re-source still owed.
- **REGINALD** — Path C: TX syndicator concentration + Trepp MF + the three-instrument cohort convergence.
- **CORAL** — LGI's **Florida ASP −6.5%** segment datum + the GSE condo mandate effective-date confirmation + the 8.1mo lock repair on my side.
- **CARL** — answer to the Q2 HHDC ask (**nothing HOMER publishes is share-based off CCP mortgage balances; nothing moves**) + the FC-notations-vs-ATTOM-starts divergence.

## NEXT SESSION

1. **🔴 Fannie + Freddie JULY monthly MF DQ (~8/12-14) — OWED NOW, not pulled.** The cleanest forward test of the recognition-regime finding. Pull Freddie at PRIMARY with curl+UA.
2. **🔴 MBA Q2-2026 NDS — checked 8/12, NOT out.** HOM-02 resolver 1 of 3. Re-check first thing.
3. **🔴 FMHPI July data ~8/31 — the HOM-01 decision point.** Issuer path, not the mirror: `freddiemac.com/research/indices/house-price-index` (curl+UA) for the vintage line, then `fmhpi_master_file.csv`. **Year-verify.**
4. **MBA weekly apps owed** (not pulled 8/12); PMMS Thu 8/13.
5. **ATTOM July monthly ~mid-Aug** + reconcile against the CCP notations decline (55.2K) and the ResiClub 55,160-vs-115,714 label collision (SIG-W-20260812-003).
6. **Process the remaining WALTER inbox** — 5 unprocessed at boot; UWM consumed, the ResiClub one consumed, **3 still unread** (Spokane fire/insurance 8/2, NY Fed VantageScore basis break 8/12, retail-closures inoculation 8/12).
7. **Process the 3 stale non-WALTER inbox packets** (PROME 8/2 dead-path ask — answerable in one line, the regression was not in a HOMER surface; CORAL 8/3; PROME 8/4 amendment-10).
8. **Re-source the $160B+ wall.** CREED is still carrying it provisional on my say-so.

## OPEN THREADS

- **HOM-01 OPEN — one early-kill arm fired, 8/31 decides.**
- **HOM-02 OPEN — resolver 1 not released as of 8/12.** HUD ML 2026-08 (mandatory 9/21) remains a documented measurement risk to its numerator. No re-spec.
- **CRL-23** open at CARL; LGI is not a trigger entity. Next checkpoints PHM Q3 ~Oct / DHI FQ4 ~Nov.
- **Marquee (recognition regimes)** — strengthened, not changed: Trepp's July MF move is the **payment-failure** leg, which is the one the GSE mod-suppression story does not cover.
- **★ The cohort convergence is now the sharpest thing on my board:** TX syndicator paper >50% of the pipeline · Trepp MF driver naming Texas · Arbor REO above delinquencies. **Three independent instruments, one 2021-22 floating-rate Sun Belt vintage, one window.**
