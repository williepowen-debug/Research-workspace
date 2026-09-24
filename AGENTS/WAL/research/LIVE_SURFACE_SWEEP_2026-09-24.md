# WAL Live-Surface Staleness Sweep — 2026-09-24

**Mode:** READ-ONLY sweep. This file is the only write; no other file edited, no git operations. `AGENTS/WAL/CLAUDE.md` was **not** reviewed (the desk owner is doing it).
**Reference truth (given by the caller, verified 2026-09-24):** v2.4 (8/20) 2/16/45/30/7 · EV $75.96 · PT $52-76 · last close **$75.60 [Wed 9/23] = 0.47% BELOW EV** · `GATE-REG-T02` FIRED 9/1 ($77.26) → RESOLVED/TERMINAL · live guard `GATE-TERRY-ROLL70-EXIT` (≥$81.90 ×3, 0-of-3) · **live book = 1 leg, Dec-18 $70P ×1 Robinhood**, time stop 12/04 · Sep-18 pair finished OTM 9/18 (booking unrecorded) · KB **200 rows / 20 groups**, expiry backlog 0 · Cantor residual **$72.4M gross / $3.5M allowance**, loss recognized **26.5%** of exposure · Q2 share count **flat (−0.08%)** · NDFI nonaccrual $122.5M · MI3 ran 8/7, DISCONFIRMED (21.20%) · **both Q3 frames WRITTEN 9/24** · CEO Barclays 9/16 guide (B2) · 7 root + 7 FRAUD files archived 9/24 · Q2 13F ran 9/24 (KB-199).
**Instruments run (read-only):** `derived_drift_check.py --quiet` → at baseline (12/12 · 62/63); KB recount = 200 rows / 20 distinct `Group` values; 41 ACTIVE rows with a blank `Stale_By`.

**Severity key:** HIGH = a reader would act on a wrong *current* fact · MED = misleading · LOW = cosmetic / broken link.
**Not flagged, on purpose:** history that carries its own date or sits in a section marked SUPERSEDED (THESIS v2.3/v2.2.1/v2.2/v2.1 sections, SCENARIOS superseded EV tables), CHANGELOG, `archive/`, `STATUS_ARCHIVE.md` / `MEMORY_ARCHIVE.md`, dated REGINALD_CHANNEL entries, frozen frames (Q2_GRADING_FRAME, PREPRINT_RECON), and EARNINGS_PREP content.

---

## 1. Findings by surface

### THESIS.md (WAL-owned)

| # | path:line | Stale text (short) | Why stale | Sev | Suggested replacement |
|---|---|---|---|---|---|
| T1 | THESIS.md:3 | "EV $75.96 · PT $52-76 · **overvaluation 5.4% @ $80.05**" | This is the boot-read header, and it states the 8/20 overvaluation as the current one. At the 9/23 close of $75.60, spot is **0.47% BELOW EV** | **HIGH** | `EV $75.96 · PT $52-76 · spot vs EV → STATUS.md (at 9/23 close $75.60: −0.47%, below EV; 5.4% @ $80.05 was the 8/20 mark)` |
| T2 | THESIS.md:17 | "the live Sep-18 cores sit **below** the new EV … both expire worthless" | This sits in the ★CURRENT v2.4 section. The Sep-18 pair finished OTM on 9/18 and the live book is 1 leg (Dec-18 $70P) | **HIGH** | Add after the line: `> *Rider 2026-09-24: the Sep-18 pair finished OTM 9/18 (tape; booking unrecorded, FORGE D-58). Live book = Dec-18 $70P ×1 → POSITIONS.md. The line above is the 8/20 record.*` |
| T3 | THESIS.md:396 | "live Sep core is $67.5P+$70P per POSITIONS 6/19" | This is the POSITIONS pointer paragraph, and it names a dead book as live | **HIGH** | `Current positions: grep POSITIONS.md (canonical) — do not trust any strike list in this file. (As of 9/24: 1 leg, Dec-18 $70P; the Sep-18 pair finished OTM 9/18.)` |
| T4 | THESIS.md:363-369 | §PREDICTIONS table: REG-24 **65%**, REG-25 **72%**, "First-chance resolve **Jul 21 AMC**" | The section has no banner. These are now WAL-01 **25%** and WAL-02 **50%**, open to Q3 (`workbook/PREDICTIONS.tsv`; INDEX:7) | **HIGH** | Put a banner over the table: `> 🧊 v2.2-era table (pre-7/22). LIVE: WAL-01 (ex-REG-24) 25% · WAL-02 (ex-REG-25) 50% · both OPEN to Q3 → workbook/PREDICTIONS.tsv (canonical).` |
| T5 | THESIS.md:236 | "The 10% bear-fast weight is **NOT yet re-allocated** — that is v2.4 proposal P7, Will-gated" | It contradicts the header. P7 was ruled 8/12 and executed at v2.4 on 8/20 (10%→2%) | MED | `~~NOT yet re-allocated~~ → EXECUTED at v2.4 (2026-08-20): bear-fast 10%→2%, Base 45 / Bull 30 (Will's 8/12 ruling, P7).` |
| T6 | THESIS.md:357 | "PT vs current \| … \| **$55-70 range / $80-82 spot**" | The PT and spot here are both May-vintage. The live figures are PT $52-76 and spot $75.60 [9/23] | MED | `PT $52-76 (v2.4) / spot → STATUS.md ($75.60 [9/23])`, or mark the table `(May-2026 vintage)` |
| T7 | THESIS.md:379-390 | §WATCH DATES: "FFIEC PDD bulk integration **STILL PENDING**"; next rows are Jun 18 and Late-Jul | MI3 ran 8/7. Every date in the table is past, and none of the live Q3 carriers is listed | MED | Replace with: `Forward catalysts live at STATUS.md §CATALYSTS (Q3 print ~Oct, date not announced; Q3 10-Q ≥10/26; $99M appraisal; Q3 Call Report; Dec-18 time stop 12/04). Table below = May-2026 record.` |
| T8 | THESIS.md:398 | "SCENARIOS.md **still reflects pre-Q1 probability weights** — needs refresh in Wave 1 chunk 2" | SCENARIOS carries the v2.4 EV table (8/20) | MED | `SCENARIOS.md §EV SUMMARY is v2.4 (8/20). Only its strike-by-strike sections are May-vintage (rebuild owed, one leg).` |
| T9 | THESIS.md:418-425 | §OPEN RESEARCH (post-v2): item 1 "Q1 Call Report MI3 trajectory (May 1-10)", item 4 "Investor Day May 12" | Item 1 was done 8/7 and item 4 is past. The live open list is in MEMORY NEXT SESSION and INDEX §Open Threads | MED | Strike 1 and 4 with `✅ 8/7 MI3 ran` / `✅ held 5/12`. Add `Live open list → MEMORY.md NEXT SESSION` |
| T10 | THESIS.md:302, 310-312, 318 | V3 heading "**NEAR-DISCONFIRMED AT AGGREGATE**"; rows marked "disconfirmed" | The section is undated and reads as live. The Q2 10-Q shows NDFI at 25.9% of HFI, a record, and FFIEC 9a rose in 11 of 12 quarters. STATUS:65 has V3 "UNDER CHALLENGE", re-score P1 owed | MED | Add under the heading: `> ⚠️ Q1-vintage read (5/1). Since challenged: Q2 10-Q NDFI 25.9% of HFI (record, KB-146) + FFIEC 9a up 11 of 12 qtrs. Live state = STATUS §CONVERGENCE (V3 1/5, UNDER CHALLENGE).` |
| T11 | THESIS.md:224 | "OZK IQHQ **Aug maturity is the next discrete event window**" | Corrected 8/28 elsewhere in the same file (:202, :214). The carrier is OZK's Q3 call, ~Oct | LOW | `OZK IQHQ resolution is carried by OZK's Q3 call (~Oct 2026); the Aug date was the maturity, not the disclosure.` |
| T12 | THESIS.md:1 | Title "…Tail Risk **Actualizing on Q2 Timeline**" | v2.2-era framing. The v2.4 framing is "compounder with concentrated CRE tail risk" | LOW | `# WAL — Compounder with Concentrated CRE Tail Risk` |
| T13 | THESIS.md:435 | `../REGINALD/research/WAL_10Q_DRILL_2026-05-21.md` | Broken path. REGINALD moved the file to `../REGINALD/archive/research/` | LOW | `../REGINALD/archive/research/WAL_10Q_DRILL_2026-05-21.md` |

### SCENARIOS.md (WAL-owned)

| # | path:line | Stale text | Why stale | Sev | Suggested replacement |
|---|---|---|---|---|---|
| S1 | SCENARIOS.md:10 | "**Current Price:** **$80.05** [2026-08-20…]" | The file header labels an 8/20 price as current. Last close is $75.60 [9/23] | **HIGH** | `**Price:** → STATUS.md (last: $75.60 [Wed 9/23 close]; $80.05 was the 8/20 v2.4 mark)` |
| S2 | SCENARIOS.md:3 | "The Sep-18 cores ($67.5P/$70P) **now sit** $8.46 and $5.96 BELOW EV" | Top-of-file banner. Those legs finished 9/18 | **HIGH** | `> ⚠️ (8/20 record) The Sep-18 pair finished OTM 9/18 (tape; booking unrecorded). Live book = Dec-18 $70P ×1, $5.96 below EV → POSITIONS.md.` |
| S3 | SCENARIOS.md:7 | "the live Sep core is **$67.5P + $70P** (plus RH $77.5P **Aug-21**…)" | Neither is live. The Aug-21 leg was SOLD 8/18 and the Sep-18 pair finished 9/18 | **HIGH** | `the Sep-18 pair finished OTM 9/18 and the Aug-21 $77.5P was sold 8/18; live book = Dec-18 $70P ×1 (POSITIONS.md)` |
| S4 | SCENARIOS.md:38, 40, 42 | "Overvaluation … = **5.4%** at spot $80.05"; "**WAL is still overvalued** against my EV … by 5.4%" | This is the ★CURRENT v2.4 section. At the 9/23 close spot is 0.47% **below** EV | **HIGH** | After :38 add: `**Re-derived 2026-09-24:** (75.60 − 75.96)/75.96 = **−0.47%** at the Wed 9/23 close — spot is BELOW EV for the first time this cycle (STATUS owns the live figure). The 5.4% below is the 8/20 mark.` |
| S5 | SCENARIOS.md:44 | "The **live** Sep-18 cores sit BELOW the new EV … both expire worthless" | Same section. The legs are no longer live | **HIGH** | Same rider as S2. Optionally: `Dec-18 $70P is $5.96 below EV and $5.60 below spot [9/23].` |
| S6 | SCENARIOS.md:2 | "overvaluation 12.4% → 5.4% at spot $80.05 [8/20]" | Dated correctly, but it is the only valuation reading at the top of the file | MED | Append: `→ −0.47% at $75.60 [9/23 close] (price move, not a re-mark)` |
| S7 | SCENARIOS.md:11 | "Short Interest: **3.54%** float / 2.71 days (Mar 25 — REFRESH PENDING)" | Superseded by 4.91% float [FINRA 6/30] (INDEX:28, WEAKNESSES:17) | MED | `Short Interest: 4.91% float [FINRA 6/30] — never refresh from yfinance (KB-192)` |
| S8 | SCENARIOS.md:496-511 | "## WHY MARKET IS (STILL) MISPRICING — v2.0"; reason 1 "MI3 reclassification … forcing function" | Undated, present tense. MI3 was tested and disconfirmed 8/7, and v2.4 says the bear is priced (STATUS:95) | MED | Retitle: `## WHY MARKET WAS MISPRICING — v2.0 (5/1 record; superseded — MI3 disconfirmed 8/7, spot below EV 9/23)` |
| S9 | SCENARIOS.md:515-532 | §WHAT WOULD CHANGE THE WEIGHTING: "Q2 NCO ex-fraud > 45bps", "Office classified > $500M Q2", "Investor Day delivers…" | All the triggers are keyed to Q2 and Investor Day, both past. The live triggers are the Q3 frames | MED | Banner: `> 🧊 Pre-Q2 triggers (May record). Live triggers = Q3_PRINT_GRADING_FRAME_2026-09-24.md + Q3_10Q_GRADING_FRAME_2026-09-24.md + STATUS §EXIT RULES.` |
| S10 | SCENARIOS.md:12 | "**Q1 2026 EPS:** $1.65 GAAP / $2.22 adjusted" | The header shows the prior quarter. Q2 is $2.36 GAAP = adjusted (KB-149) | LOW | `**Q2 2026 EPS:** $2.36 GAAP = adjusted (10-Q, KB-149); Q1 $1.65 / $2.22` |
| S11 | SCENARIOS.md:536 | "KB evidence: **177 rows**" | KB is 200 rows | LOW | `KB evidence: → workbook/KB.tsv (200 rows at 9/24)`. Better: drop the count so the footer cannot rot |
| S12 | SCENARIOS.md:536 | `../REGINALD/research/WAL_10Q_DRILL_2026-05-21.md` | Broken path (moved to REGINALD archive) | LOW | `../REGINALD/archive/research/WAL_10Q_DRILL_2026-05-21.md` |

### STATUS.md (WAL-owned)

| # | path:line | Stale text | Why stale | Sev | Suggested replacement |
|---|---|---|---|---|---|
| ST1 | STATUS.md:95 | "**The next substantive act is the Q3 frame, due Tue 10/13.**" | Both Q3 frames were WRITTEN 9/24 (STATUS:30 says so itself). This is the BOTTOM LINE, and it sends the reader to write a frame that already exists | **HIGH** | `**Both Q3 frames are written (9/24). The next acts: pin the print date on announcement (~10/2-10/9) and re-pin WAL-01/02 Resolve_By.**` |
| ST2 | STATUS.md:30 | Catalyst row dated "⏱ **TUE Oct 13**" … "**19 days out.**" | §CATALYSTS is labelled "forward only", but this deadline is already met. The row reads as a pending event | MED | Delete the row, or re-date it: `✅ DONE 9/24 — both Q3 frames written (L170/L171); owed: pin print date (§9) / 10-Q date (§8)` |
| ST3 | STATUS.md:14 | "Raise from ~mid-October (**≈10/13, with the Q3 frame**)" | The frame anchor is gone, because the frame was written 9/24 | LOW | `Raise from ~mid-October (≈10/13, with the print-date pin), not before.` |

### MEMORY.md (WAL-owned)

| # | path:line | Stale text | Why stale | Sev | Suggested replacement |
|---|---|---|---|---|---|
| M1 | MEMORY.md:13 | Open Q #2: "The Thesis-RETIRE rule says 'ACL/NPL >100%' **with no denominator** ⇒ **pin it in the Q3 frame before the print.**" | Pinned 9/24 in Q3 frame §7 as (funded + unfunded ACL) ÷ total nonaccrual (STATUS:77; NEXUS:16) | MED | `~~pin it~~ ✅ PINNED 9/24 (Q3 frame §7): (funded+unfunded ACL) ÷ total nonaccrual; full-NPL reported alongside, non-gating.` |
| M2 | MEMORY.md:42 | "⚖️ **desk CLAUDE.md lines 16/150 still say ~$46M, awaiting Will's OK to edit**" | Done at `904f2e1cd` (Will OK) | MED | `✅ CLAUDE.md:16/150 corrected 9/24 (904f2e1cd, Will OK).` |
| M3 | MEMORY.md:27 | "**KB expiry backlog 61 → 41**" | Contradicts N-5 at :40 in the same file (61 → 0). The backlog ended at 0 | LOW | `KB expiry backlog 61 → 0 over three row-by-row passes (first pass 61 → 41)` |
| M4 | MEMORY.md:5 | "Raise from ~mid-October (**with the Q3 frame, ~10/13**)" | Same dangling anchor as ST3 | LOW | `(with the print-date pin, ~10/13)` |

### INDEX.md (WAL-owned mirror)

| # | path:line | Stale text | Why stale | Sev | Suggested replacement |
|---|---|---|---|---|---|
| I1 | INDEX.md:108 | Open thread 6(b): "`.env` is **laptop-only, desktop has no creds**" | Contradicts STATUS:14, MEMORY:5 and the boot card: creds are on the **DESKTOP only**, and the laptop cannot pull MI3. A reader would try the pull on the wrong machine | **HIGH** | `(b) creds (.env) are on the DESKTOP only (DESKTOP-BC6EF81); the laptop cannot pull MI3.` |
| I2 | INDEX.md:104 | Open thread 2: "**Sep-18 expiry is the forcing date**" | Sep-18 passed 9/18. One leg is left to rebuild for | MED | `…still open; forcing date now the Dec-18 $70P time stop 12/04 (one leg).` |
| I3 | INDEX.md:19 | "**ACL/NPL coverage** \| **96% — below 100%**" | Wrong label. 96% is (funded+unfunded ACL) ÷ **nonaccrual**; on full NPL it is **69.1%** (NEXUS:121; the denominator was pinned 9/24) | MED | `**ACL ÷ nonaccrual** (funded+unfunded) \| **96%** — below 100% (full-NPL basis 69.1%)` |
| I4 | INDEX.md:101 | "Open Threads (re-triaged session #1 2026-07-25; **updated session #2 2026-08-07**)" | Items 13 and 4 were updated 9/24 | LOW | `…; last updated session #7 2026-09-24)` |
| I5 | INDEX.md:52, 53, 67 | "⬅ ★★ **NEW**", "⬅ **NEW**", "⬅ **NEW 8/7**" | These tags have been "new" for 48 days | LOW | Drop the NEW tags |

### NEXUS_BRIEF.md (WAL-owned, consumer-facing)

| # | path:line | Stale text | Why stale | Sev | Suggested replacement |
|---|---|---|---|---|---|
| N1 | NEXUS_BRIEF.md:32-42 | "## ⛔ FOR CONSUMERS, **READ FIRST** (2026-08-20 closeout)". The table has EV "ABOVE both **live** Sep-18 strikes", tape $78.71 [8/27], "REG-T-02 re-graded **UN-FIRED**" | The title tells consumers to read this first. The strikes are gone, REG-T-02 FIRED 9/1 and is TERMINAL, and the tape figures are 4 weeks old | **HIGH** | Retitle: `## 🧊 (8/20-8/28 record — SUPERSEDED 9/24) the tape/model tension`, with the line `Resolved: REG-T-02 FIRED 9/1 ($77.26), TERMINAL; Sep-18 pair finished OTM 9/18; live state = header items 1-7.` |
| N2 | NEXUS_BRIEF.md:99-101 | "## Recent pivot (required)" — "**v2.2.1 → v2.3 (7/25) — the last thesis motion, and it still stands**"; "Spot has since drifted to **$81.77** … overvaluation **10.6%**" | This is a schema-required field and it names the wrong pivot. The last motion is **v2.3 → v2.4 (8/20)**. The spot and overvaluation are 8/7 figures | **HIGH** | `**v2.3 → v2.4 (8/20) — the last thesis motion, and it still stands.** MI3 disconfirmed → bear-fast 10→2, Base 45 / Bull 30, EV $73.92→$75.96, PT $52-76; total bear 26→18. Since then only PRICE moved: $75.60 [9/23] = 0.47% below EV.` |
| N3 | NEXUS_BRIEF.md:19 | Item 7: "KB 187 → 200; **expiry backlog 61 → 41**" | Contradicts item 7c at :17 (61 → 0). The final state is 0 | MED | `KB 187 → 200; expiry backlog 61 → 0 (row-by-row, 3 passes)` |
| N4 | NEXUS_BRIEF.md:162 | "⏱ **Q3 frame due Tue 10/13** → …" | First item in FORWARD CATALYSTS, but the frames were written 9/24 (the brief's own :16 says so) | MED | `✅ Q3 frames written 9/24 → Q3 date announcement (~10/2-10/9) → …` |
| N5 | NEXUS_BRIEF.md:129 | v2.3.1: "**Still unratified; Will owes ratify-with-repair or reject.**" | REJECTED + retired as P4 on 8/20 (the brief's own :5 and :145) | MED | `→ REJECTED + retired 8/20 (P4).` |
| N6 | NEXUS_BRIEF.md:158 | "carry the V1a ≠ V1 fence and the **weights-unchanged note** together" | Weights changed at v2.4 (8/20) | MED | `carry the V1a ≠ V1 fence together with v2.4's re-mark (bear-fast 10→2, bear-medium HELD 16)` |
| N7 | NEXUS_BRIEF.md:71 | "Implied shares out **−1.7%**, buyback-consistent" | A retired claim (RETIRED_CLAIMS; KB-200: Q2 share count flat, −0.08%) with no annotation in a consumer brief | MED | `~~Implied shares out −1.7%~~ (retired 9/24: 13G rounding noise; 10-Q covers show −0.08%, KB-200)` |
| N8 | NEXUS_BRIEF.md:64-65 | "margin of safety … **5.4% (8/20)**"; "The model says the **Sep-18 cores** expire worthless" | Under a dated 8/20 heading, but written as instructions ("three things NEXUS should carry") | MED | Append to :64: `(→ −0.47% at 9/23 close)`. Append to :65: `(Sep-18 pair finished OTM 9/18)` |
| N9 | NEXUS_BRIEF.md:93 | "Weights are UNCHANGED … **v2.4 proposal P7, Will-gated. WAL will signal when he rules.**" | Dated 8/7 section. Ruled 8/12, executed 8/20 | LOW | Append `→ RULED 8/12, EXECUTED 8/20 (v2.4).` |
| N10 | NEXUS_BRIEF.md:128 | "**KB now 163 rows**" | Dated section. KB is 200 | LOW | `(163 at 8/7; 200 at 9/24)` |

### workbook/KB_INDEX.md (WAL-owned navigator)

| # | path:line | Stale text | Why stale | Sev | Suggested replacement |
|---|---|---|---|---|---|
| K1 | workbook/KB_INDEX.md:48 | Hidden CRE (V1a): "MI3 24.2% and growing" → "**STILL UNTESTED (127)** … The standing embarrassment" | MI3 ran 8/7 and DISCONFIRMED (21.20%). The same file's :33 says so | **HIGH** | `✅ TESTED 8/7 — DISCONFIRMED (164-170): 23.88% / 21.20%, never ≥25% in 12 qtrs; bear-fast 10→2 (v2.4). V1a ≠ V1.` |
| K2 | workbook/KB_INDEX.md:11 | SSFA key fact: "**Q2: warehouse/NDFI book SHRINKING by mgmt choice**" | Refuted at the Q2 10-Q: NDFI 25.9% of HFI, a record, all sub-lines up (KB-146), plus FFIEC 9a up in 11 of 12 quarters | **HIGH** | `Q2 call claimed shrinking (121, A2) — REFUTED by Q2 10-Q: NDFI $15.81B = 25.9% of HFI, record (146); NDFI nonaccrual $122.5M. V3 under challenge.` |
| K3 | workbook/KB_INDEX.md:36, 50 | V3: "**DISCONFIRMED at aggregate**; lone confirming sub-vector now shrinking (121)"; "FURTHER WEAKENED (121)" | Same refutation as K2. STATUS:65 has V3 1/5 UNDER CHALLENGE, re-score P1 owed | MED | `1/5 UNDER CHALLENGE — 121's 'shrinking' refuted by 146 (A1) + FFIEC 9a; Crestline lender role 195 vs mgmt plan 196` |
| K4 | workbook/KB_INDEX.md:2 | "**180 rows \| 16 groups** \| … Last refresh 2026-08-20" and "implied shares −1.7%" | Now 200 rows / 20 groups; last real refresh 9/24 (KB.tsv header). −1.7% is retired (KB-200) | MED | `**200 rows \| 20 groups \| Last real data refresh 2026-09-24** (rows 188-200: tape, catalyst sweep, Barclays B2, Crestline, Cat-IV, 13F + share-count correction)`. Strike `−1.7%` → `(retired: −0.08%, KB-200)` |
| K5 | workbook/KB_INDEX.md:8-25 | Group Map row counts (e.g. HIDDEN_CRE 23, JEFFERIES 14, CANTOR 15…) and only 16 groups | Actual: HIDDEN_CRE 37, JEFFERIES 18, INSIDER 17, EARNINGS 17, CANTOR 16, SSFA 14, CAPITAL 13, MARKET 11, … Missing groups: **TAPE 4, OWNERSHIP 4, METHOD 4, NDFI 3** | MED | Regenerate the counts from KB.tsv and add rows for TAPE / OWNERSHIP / METHOD / NDFI |
| K6 | workbook/KB_INDEX.md:12, 52 | CANTOR: "vs ZION 83% … $26.1M charged (**89%** of $29.6M reserve)"; Auditor row: "Cantor charge directionally validated **ZION 83%**" | Retired pairing. 88-89% is reserve **utilisation**. The loss recognized is **26.5% of the $98.5M exposure** vs ZION ~83% (THESIS:281). The residual is $72.4M gross / $3.5M allowance | MED | `Q1: $26.1M charged = 26.5% of $98.5M exposure (vs ZION ~83%); reserve utilisation ~88% ($3.5M left). Residual $72.4M gross.` |
| K7 | workbook/KB_INDEX.md:24 | FRAUD_GENERAL: "but **First Brands & Tricolor SILENT**" | The 9/24 FRAUD review rules the "First Brands SILENT" reading wrong. First Brands/Point Bonita = the LAM charge-off (KB-135/-186); Tricolor exposure was never evidenced (FRAUD/STATUS.md:3 rider, AUDITOR_NEXUS.md:2) | MED | `First Brands/Point Bonita = the LAM charge-off (135/186); Tricolor exposure never evidenced — see FRAUD/FIRST_BRANDS.md §FOLD` |
| K8 | workbook/KB_INDEX.md:77 | WAL-01 test: "Q3 deck slide-12 donut **+ 10-Q Schedule O**" | The Schedule O cite was VOIDed 8/20 (P2): no 10-Q publishes classified by property type (INDEX:112) | MED | `Q3 deck "Classified Assets Mix" slide (A2-visual) + 10-Q total-classified cross-check; NO-VERDICT band → Q3_PRINT_GRADING_FRAME_2026-09-24.md` |
| K9 | workbook/KB_INDEX.md:84-93 | §Staleness table: "2026-04-30 (PASSED)", "2026-07-31 (imminent)" … | The expiry backlog was cleared to 0 on 9/24 (37 SUPERSEDED, 24 extended). The table describes the pre-9/24 state | MED | Replace with: `Run scripts/kb_expiry_check.py (boot 4b). 9/24: 0 past Stale_By; 41 ACTIVE rows BLANK Stale_By (not a pass).` |
| K10 | workbook/KB_INDEX.md:69 | "Standing re-checks **owed at the Q2 10-Q**" | The Q2 10-Q was read 8/7. What remains carries to the Q3 10-Q frame | LOW | `Standing re-checks carried to the Q3 10-Q frame: 121 (→146), 123 Cantor tie-out` |
| K11 | workbook/KB_INDEX.md:10, 11, 15 | Research folders `research/HIDDEN_CRE/`, `research/SSFA/`, `research/JEFFERIES/` | These never existed (INDEX:99 already struck them) | LOW | `MI3_FIRST_RUN_2026-08-07.md` / `Q2_10Q_READ_2026-08-07.md` / `FRAUD/FIRST_BRANDS.md` + `FORGE/research/jefferies/` |

### WEAKNESSES.md (WAL-owned)

| # | path:line | Stale text | Why stale | Sev | Suggested replacement |
|---|---|---|---|---|---|
| W1 | WEAKNESSES.md:13 | "**Q3 is the N=3 test** … a 3rd non-confirmation triggers the retire rule" | Contradicts STATUS:76-77 and :86: Q3 is migration **DP2 of 3**, and RETIRE is "1 of 3 — earliest **Q4 print ~Jan 2027**" | MED | `Q3 is data point 2 of 3; the retire rule's N=3 lands at the Q4 print (~Jan 2027) at the earliest (STATUS §EXIT RULES)` |
| W2 | WEAKNESSES.md:34 | "**Q3 10-Q**: 0 new office migrations (N=3) + benign appraisal" | Wrong carrier and wrong N. Office migrations are carried only by the **Q3 deck slide 12 + call** (STATUS:74); Q3 = N=2 | MED | `Q3 deck slide 12 + call: 0 new office migrations (DP2) + benign appraisal (8-K / Q3 call / Q3 10-Q) → bear-medium KILL` |
| W3 | WEAKNESSES.md:36 | "ACL/NPL rebuilt >100%" | No denominator, though it was pinned 9/24 | LOW | `(funded+unfunded ACL) ÷ total nonaccrual >100% (pinned 9/24; full-NPL reported alongside)` |
| W4 | WEAKNESSES.md:28 | "H2 NPL-resolution path (**3-4 of the six** closing in Q3)" | CEO 9/16 (B2): "six credits … **four down, two to go**", last two in Q4 (KB-194) | LOW | `(CEO 9/16, B2: four of six resolved, two in Q4 — at par or with charge-downs?)` |

### Other WAL-owned files

| # | path:line | Stale text | Why stale | Sev | Suggested replacement |
|---|---|---|---|---|---|
| O1 | EARNINGS_PREP_BANNER_RIDER_2026-08-23.md:3 | "**Status:** ⬜ **PROPOSED — awaiting disposition**" | Self-ruled and applied 2026-09-02 (EARNINGS_PREP.md:3). A live root file says it is still open | LOW | `**Status:** ✅ SELF-RULED + APPLIED 2026-09-02 (EARNINGS_PREP.md:3)` |
| O2 | LEADERSHIP.md:2 | STALE-VINTAGE banner omits two things: Vecchione took the board chair 6/10, and V4 is now 3/5 (vs the body's "20/20") | The banner is correct as a banner. The additions just save a reader one hop | LOW | Append: `Since: CEO took board chair 6/10 (KB-WAL-135-era sweep); V4 = 3/5 (STATUS §CONVERGENCE).` |
| O3 | sources/INSIDER_SCAN_WAL.md:1 | "## WAL — 🟠→🔴 SOPHISTICATED REPOSITIONING (Score 19→20)" and no date | Undated. The superseding sweep is `INSIDER_SCAN_WAL_2026-07-25.md` | LOW | Add line 1: `> 📼 Vintage ~2026-03-25 (through ~Feb). Superseded by INSIDER_SCAN_WAL_2026-07-25.md; V4 now 3/5.` |
| O4 | scripts/derived_drift_check.py:29-30 | Docstring "BASELINE of **11** check-1 and **35** check-2 hits" (8/23) | Code at :193 carries 12 / 63. The docstring itself says "Re-baseline in this docstring whenever you do a sweep" | LOW | `…settles (re-measured 2026-09-24) at a BASELINE of 12 check-1 and 63 check-2 hits — see BASE_DRIFT/BASE_REVIVED` |
| O5 | scripts/derived_drift_check.py:196 | Comment: "Known blind spot found 9/24: **CLAUDE.md:16/150 still ASSERT '~$46M'**" | Fixed at `904f2e1cd` (the blind-spot mechanism note stays valid) | LOW | `…CLAUDE.md:16/150 asserted '~$46M' (fixed 904f2e1cd) but were EXCUSED by marker proximity — the blind spot stands.` |
| O6 | scripts/derived_drift_check.py:240 | `BASE_RECHECK_BY = "2026-10-13"  # = Q3 frame deadline` | The frame was written 9/24. The date still works as a re-check date, but its label is stale | LOW | `# re-measure by 10/13 (ex-Q3-frame deadline; frames written 9/24) and at every thesis bump` |

**Checked and clean (no finding):** POSITIONS.md (all current; the Sep-18 pair is correctly in History); STATUS.md header, POSITIONS, EXIT RULES and EXPECTED SIGNALS sections; INDEX.md:7 token line and :29; WEAKNESSES.md:11-12, 18, 27; THESIS.md:281/297 (Cantor corrected); EARNINGS_PREP.md (banner consistent with the rider; `../REGINALD/domain/WAREHOUSE_EXPOSURE.md` resolves; no path to any file archived today); MARKET/ (README is a dated 3/25 chart note; TRADE_LOG is FROZEN-bannered); scripts/kb_expiry_check.py (its "64 of 177" is explicitly "measured at birth"); scripts/predictions_due_check.py (its "41 blank" still = 41).

---

## 2. Broken relative links to files archived 2026-09-24

| path:line | Link text | Resolves? | Suggested re-point | Sev |
|---|---|---|---|---|
| FRAUD/STATUS.md:99 | `TRICOLOR.md` (file table) | ❌ | `../archive/FRAUD/TRICOLOR.md` (path fix allowed in a bannered record) | LOW |
| FRAUD/STATUS.md:103 | `CLASS_ACTION_FINDINGS.md` | ❌ | `../archive/FRAUD/CLASS_ACTION_FINDINGS.md` | LOW |
| FRAUD/STATUS.md:104 | `INVESTIGATION_ROADMAP.md` | ❌ | `../archive/FRAUD/INVESTIGATION_ROADMAP.md` | LOW |
| FRAUD/STATUS.md:106 | `ZION_AUDIT_COMPARISON.md` | ❌ | `../archive/FRAUD/ZION_AUDIT_COMPARISON.md` | LOW |
| FRAUD/AUDITOR_NEXUS.md:208 | `GRANT_THORNTON_NEXUS.md` | ❌ | `../archive/FRAUD/GRANT_THORNTON_NEXUS.md` | LOW |
| FRAUD/AUDITOR_NEXUS.md:210 | `TRICOLOR.md` | ❌ | `../archive/FRAUD/TRICOLOR.md` | LOW |

**Already correct (no action needed):** INDEX.md:82 and :85 (name `archive/` and `archive/FRAUD/` explicitly); FRAUD/STUPIN_CRE.md:138 and FRAUD/AUDIT_COMMITTEE.md:2 (use `../archive/FRAUD/…`); KB.tsv:73 (KB-WAL-071 re-pointed to `archive/FRAUD/ISSUER_B_ELIMINATION.md`); MEMORY.md:41 (names the sweep record). `research/FRAUD_CORPUS_REVIEW_2026-09-24.md` names the moved files as the subject of the review (record, correct as written). No live surface links to any of the 7 root files archived today (AUDIT_MAR25, EXTERNAL_PROMPTS, INVESTOR_DAY ×2, PRIOR_RESEARCH_EXTRACTS, TECHNICALS_20260401, V21_RESPONSE) except INDEX:85, which is correct.
**Broken links not from today's archiving:** THESIS.md:435 and SCENARIOS.md:536 → `../REGINALD/research/WAL_10Q_DRILL_2026-05-21.md` (now at `../REGINALD/archive/research/`); listed as T13 / S12.

---

## 3. Repo-level mirrors pointing at WAL — ⚠️ NOT WAL-owned (flag to PROME only; never edit)

| path:line | Stale text | Why stale | Sev | Suggested replacement (for PROME) |
|---|---|---|---|---|
| PROME/ROSTER.md:107 | "Office/B1-migration/**MI3 idiosyncratic bear; thesis-of-record v2.3**" | The thesis-of-record is **v2.4** (8/20). MI3 was disconfirmed 8/7 (bear-fast 2%), so "MI3 bear" misdescribes the live bear | MED | `Western Alliance Bancorp specialist (secured-office tail / $99M appraisal idiosyncratic bear; MI3 disconfirmed 8/7; thesis-of-record → AGENTS/WAL/THESIS.md)` — pointing at THESIS avoids a version token that rots |
| PROME/ROSTER.md:107 | Status cell "new†††††" | Registered 7/25; ACTIVE for 2 months | LOW | `ACTIVE†††††` |
| AGENTS/_NETWORK.md:28, 81 | WAL node + REGINALD peer edge | Clean (topology only) | — | — |
| AGENTS.md:33 | "Single-name bank depth: OZK, WAL, FLG → REGINALD" | Clean | — | — |

---

## 4. Counts

| Severity | WAL-owned findings | Broken links | Non-WAL (flag-only) | Total |
|---|---|---|---|---|
| HIGH | 15 (T1-T4, S1-S5, ST1, I1, N1, N2, K1, K2) | 0 | 0 | **15** |
| MED | 30 | 0 | 1 | **31** |
| LOW | 23 (T11-T13, S10-S12, ST3, M3-M4, I4-I5, N9-N10, K10-K11, W3-W4, O1-O6; T13/S12 are broken REGINALD paths) | 6 | 1 | **30** |

*The MED count covers T5-T10, S6-S9, ST2, M1-M2, I2-I3, N3-N8, K3-K9 and W1-W2.*
