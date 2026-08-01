# MARCO SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-07-31 ET (session 20. Boot → **PROME audit worked in full (items 1–4)** → residue sweep found 3 more surfaces the audit didn't name → **inbox drained 27 → 0** + WALTER consume step installed → FL metro-masking gets a third dataset.)

## CHANGES SINCE (session 19 → 20)
Same day. s19 closed, then **PROME's Will-directed four-reviewer audit landed** (`395b6797`) and Will directed working it. Everything below is s19's own work being checked and corrected, plus the inbox backlog that had been deferred since 7/11.

## WHAT I DID (session 20)

### 1. PROME audit — all four items closed, not batched forward
**The verdict survived; the layer around it did not.** Reviewers recomputed all 34 DID cells from the committed raw pull — exact reproduction, t-stats reproduce, the 7/25 pre-commit is real (`67473a1f`, six days before the test). The Channel-1 demotion stands on the numbers.

- **Item 1 — FL diagnostic MISSED and was never scored.** `PREREG` §3:52 predicted FL DID ≈ 0 confirms Amendment 2; actual **+6.89pp / +7.38pp**. Scored **MISS** — *not* passed under a sign expectation re-derived after seeing the number. (The control-swap reasoning is real — Amendment 1 replaced a floor-matched control with TTU — but it was never written down pre-pull, and `PREREG` line 114 discusses that swap without noticing it broke the diagnostic.) **Two further defects found beyond the audit, both against me:** "stable in every month of 2026" is **false** (June is +2.96pp above the Jan–May mean), and +6.89 decomposes to +4.88 treated leg **+1.81 control leg** — FL's TTU fell 3.52→1.85 May→June, so the June figure came from the denominator. **Answer to PROME's direct question: "statutory reading STRENGTHENED" does NOT survive.** Retracted to CARL. Forward $14→$15 Sep-30-2026 impulse untouched.
- **Item 2 — both propagated numbers were wrong, and correcting them cuts against me twice.** "~6pp detection floor" was **1.96×SE for a stratum-mean difference** — significance threshold, not power MDE (**8.78pp**), not a single-state rule (band **11.53pp**). So the test was *weaker* than claimed AND the 7/25 headline was *further* inside the noise (~0.4 sd). "3.2pp swing" reproduces under **no** definition → **4.02pp** (median 6-mo range, TTU, 14 states). Sign consistency **11 of 14**, not all.
- **Item 3 — retracted 2.2M** killed in boot-read `MEMORY.md:9` and `STATUS:105`.
- **Item 4 — all eight closed:** VX-2.02 re-scoped FROZEN/NO-PRIMARY with a do-not-re-point warning; 17 banners → pointer-not-value; MAINTENANCE:67 closed; 58→57 vectors; FIGURES:96 provenance (45% was MAR-24's own, not MAR-14); orphan CSV tracked.
- **Built `scripts/fl_diagnostic_score.py`** — reproduces every figure these documents assert, from the committed raw pull. That was the actual gap: nothing was derived anywhere.

### 2. Residue sweep — the audit's own scope had a blind spot
Will asked whether I'd worked *all* of it. Grepping instead of trusting my summary found **three more carriers the packet never named**:
- **`workbook/KB.tsv` CH1-34/35** still held **both** bad figures. I swept VX in s19 and never swept KB — *"sweep the vector ledger"* was my own lesson and KB is a ledger too.
- **`SCRATCH.md`** carried the bad pair for a full session (this file — deferring it to closeout is exactly how handoff surfaces freeze stale).
- **`SDL_HISTORICAL_ANALOGS.md`** — the worst one. Its whole *scale calibration* section **derives an analytic judgment from the retracted 2.2M** ("plausible and likely conservative"), which then reads as independent corroboration of it. At the accurate ~1.0–1.5M the arithmetic inverts: **~5–7% of the undocumented population, not ~11%**, and the Operation Wetback rate comparison does not survive. Bannered; body left intact so the error stays legible.
- Also annotated **`BANXICO_STATE_REVERSE`**: its own independently-derived **~625K fewer senders** disagreed with 2.2M by ~3.5x **from April 2026** — three months before the fleet correction — and the disagreement was filed as a supporting bullet. Third instance of MARCO's material holding the right answer while the narrative asserted the wrong one.

### 3. Inbox drained 27 → 0 (was recorded as 17 — the WALTER lane was 18, not 9)
- **Installed the WALTER consume boot-step** asked for 7/11 and carried 20 days — the mechanical cause of the whole backlog, including a **7/10 ACTION item that sat 21 days**. Marked explicitly exempt from the "no inbox on normal spawns" rule, since that ambiguity is what let it build. `board_log.tsv` created, 18 dispositioned (4 acted / 1 noted / 13 info-only — 12 of those correctly other agents' lanes).
- **🔎 THE FIND — PROME's 7/21 question answered with data, not assertion.** Pulled BLS CES **metro-level** FL L&H employment: **Orlando +3.74%** (positive every month) vs **Punta Gorda −3.09%** (negative **all six months of 2026**); FL statewide **+0.55%** vs US **+0.68%**. **Internal spread 6.83pp around a statewide figure that displays neither end**, and FL is marginally *below* national and was negative Jan–Apr. Answer: **(c) composition**, decisively — "tourism resilience" does not survive at state level. CORAL's datum and MoM framing are both correct; only the inference fails, and CORAL logged it UNGRADED so it resolved cleanly.
- **Punta Gorda is now negative on three independent datasets** — ATTOM #1 US (0.50%), ZHVI −8.2%, L&H −3.09% × 6/6. Three agencies, three bases, same two metros. **NOT promoted to an instrument** (small MSA 9.4K, wide CES small-area bands; employment is a quantity, Channel 2 is a $-per-visitor thesis).
- **Corrected my own MEMORY caveat:** Miami-Dade is a **World Cup host city** and posted **+0.90%**, below state and nation — the WC hospitality-employment mask is *weaker* than I assumed. Measured now, not assumed. Bears on ES-MARCO-01's Aug-8 read.
- **Citizens self-contradiction fixed:** STATUS carried CORAL's corrected PIF **278,246** in one block while **four lines below** it still said "~385K policies" + a superseded rate-cut date; `CLAUDE.md`'s threshold table had the stale one too. CORAL's primary-verified packet sat unprocessed **10 days**.
- **AEOLUS repointed — a dead lane found only because three packets accumulated.** Three C5 packets (6/28, 7/9, 7/22) all asked MARCO to reconcile a goods-CPI pass-through. MARCO has had no price/cost transmission instrument since v2.7 and none at all since v3.0, and the food leg went to **CARL in Jan 2026** (my own retired `VX-2.07` records it). Named the three legs I *do* want: travel cost, El Niño snowbird push, hurricane→migration.
- KB +2 rows (Parcl vacation-town listings 3× national incl. Key West 3.1%; reinsurance supply-side easing) — both logged with the **insurer-side vs household-cost** trap attached.

### 4. STATUS open-items table de-rotted
Six rows were stale within hours of being written. One was **actively dangerous**: *"Wage-panel build (thesis v2.7 follow-through)"* instructed a future session to run **the exact test v3.0 demoted** — it survived the v3.0 write-up by six hours. Killed with the reason recorded.

## NEXT SESSION
1. **🔴 Aug 1 (TOMORROW) — DOUBLE PRINT.** **Banxico June remittances**: transfer **COUNT YoY** is the cleanest *surviving* SDL-01 proxy (May −1.7%; **positive = the tell breaks**). **OFLC H-2A Q3** — rebuilt puller auto-fetches on publication; MAR-11 (>425K, 88%) on a 254,688-through-Q2 base.
2. **Do NOT hunt a fourth wage instrument.** v3.0 pre-commits against it and the STATUS row telling you otherwise is now killed. Reopening needs a non-payroll source: **H-2A offer premia ABOVE the AEWR floor** (never AEWR itself — administratively set, NASS basis canceled Aug 2025), vacancy duration in immigrant-intensive occupations, or firm-level cost disclosure. **`WAGE_OFFER` needs a pay-unit filter first** (median $15.79 / mean $93.64 = mixed units).
3. **MAINTENANCE T1-F — KB.tsv has 2 duplicate IDs** (`KB-MARCO-REM-03`, `KB-MARCO-TX-04`), so those citations are ambiguous. Cheap fix, and I wrote to KB twice today without resolving it.
4. **Channel 4 rebuild** (optional, scoped) — EMMA/MSRB filings + rating actions, TX Comptroller / AZ DOR border-city receipts, CBP crossing counts. **This is the honest test: the downgrade was made on absent evidence, not contrary evidence.**
5. **MCO via BTS T-100** — carried s16→s20; blocks MAR-24 *and* MAR-22.
6. **VX-3.01 FL OIR primary** — no household-insurance figure adopted; aggregators span $3,815–$8,458.
7. **~Aug 12** July CPI → close ES-05 (3rd sub-6% print ⇒ resolve DID_NOT_APPEAR, don't push a 4th time). **~Aug 15** NTTO June → ES-MARCO-09 (leans FAIL).
8. **Lakeland** — CORAL's #2 US foreclosure metro, unassigned by either of us. Pull ZHVI + L&H if CORAL doesn't answer.

## OPEN THREADS
| Item | Status |
|------|--------|
| Channel-1 transmission | ⚫ **CLOSED as UNDEMONSTRATED (v3.0)** — 3 pre-registered nulls; reopen only on a non-payroll instrument. Audit reproduced all 34 cells: **the verdict is sound** |
| 🔎 **SW-FL concentration — 3 independent datasets** | 🟠 **STRENGTHENED 7/31 eve.** Punta Gorda: ATTOM #1 US 0.50% · ZHVI −8.2% · L&H −3.09% (6/6 months). Cape Coral one notch milder. **Convergent texture, deliberately NOT an instrument** |
| FL migration divergence (canonical +22,517 vs BofA Q1'26) → CORAL | 🟠 carried from 7/9 — **the only genuinely open CORAL item** |
| Lakeland — migration-implicated or not? | 🟠 NEW 7/31 eve — asked CORAL; unassigned in both books |
| MCO pax via BTS T-100 | 🟠 carried s16→s20; blocks two predictions |
| VX-3.01 household insurance — no figure adopted, needs FL OIR primary | 🟠 carried |
| KB.tsv 2 duplicate IDs (T1-F) | 🟠 carried from 7/31 — wrote to KB twice today without fixing |
| H-2A offer-premium-above-AEWR (pre-reg §5) — NOT run; needs pay-unit filter | 🟠 carried |
| Banxico + slaughter fetchers still mtime-cadenced (T2-E) | 🟡 carried |
| ES-MARCO-09 World Cup reversal | 🟠 leans FAIL; NTTO June ~Aug 15. **NB: the WC employment mask is now measured and small** |
| El Niño 81% very-strong Oct-Dec → FL winter 26-27 snowbird window | 🟡 carried; second-order, not modelled. AEOLUS asked to keep routing this leg |
| ~~WALTER consume step~~ / ~~inbox backlog~~ / ~~SDL-01 magnitude~~ / ~~ATTOM overlap~~ / ~~VX refresh backlog~~ | ✅ all closed 7/31 |

## Mail state
**Inbox: 0.** Drained 27 → 0 (11 top-level + 18 WALTER, incl. the PROME audit packet). `board_log.tsv` live, 18 rows.
**Outbox/sent this session:** CARL (FL-diagnostic correction — *CARL had already refused to build on the bad sentence under PROME's caution and integrated the correction mid-pass, `b472cd58`*), LABOR (rule re-scoped + 3.2pp withdrawn), PROME ×2 (audit closure + the FL hospitality answer), CORAL (SW-FL convergence + Lakeland gap + 3 corrections adopted), AEOLUS (dead-lane repoint). All committed under the self-authored-packet carve-out.

## PUSH STATE
Session 20 commits pushed in three tranches: `c8f4af30` `4c8b4e9a` `414304b1` `1ac8c82c` `7193598a` (audit + residue), then `a8cb8070` + `f10e12d4` (inbox pass + replies), then this closeout. **Origin verified 0/0 after each.** No aborts, no rebases needed.
**Note:** OSPREY and WALTER had uncommitted work in flight on this box all session — left untouched, flagged not swept.
