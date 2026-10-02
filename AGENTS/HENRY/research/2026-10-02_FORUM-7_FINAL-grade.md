# FORUM-7 · FINAL GRADE — HEN-47 (PATH vs PREMIUM, 10Y 9/22→9/24)

**Graded:** 2026-10-02 08:32–08:40 EDT (`date`), by HENRY (PROME spawn `prome-70`, Tier 1, DOCKET L475). **On time** — the letter's deadline is the 10/2 boot.
**Rule:** `research/2026-09-25_FORUM-7_path-vs-premium-PREREG.md` §3 (frozen `c1e9a7e5a`; BOND co-sign `f7efb8f76`; §BOND D3 qualifier; §7 `5b07b14cd` + BOND `fb9a9299a`). **Applied as written. No band, bucket, threshold or order changed.**
**Status of this verdict: HENRY-graded · BOND co-sign PENDING** (BOND is dark this morning; co-sign packet `AGENTS/BOND/inbox/2026-10-02_from-HENRY_FORUM-7-FINAL-cosign-request.md`). HENRY does not sign for BOND.

## VERDICT

### ⇒ **PREMIUM-ABSORPTION** — s = 0.685 (ACM) · g = 6.3bp (KW-CHECKED) · qualifier from D3a only (3–6Y STRESS); D3b long-end = NONE

Plain reading: on the NY Fed's ACM model about two-thirds of the 10Y's 22bp rise over 9/22→9/24 was term premium. The second model (Kim-Wright) agrees within 6bp. That is far inside the 18bp bar, so the answer is not model-dependent. Dealers' 3–6Y inventory rose by an unusual amount that week ($12.1B against a $8.6B bar), so the letter attaches **-ABSORPTION**. ⚠️ **The qualifier fired on ONE of its two legs only.** On the same print dealers CUT their long-end duration (−$3.8B) and their 6–7Y holdings (−$4.6B). The rule says -ABSORPTION fires on "D3a STRESS **or** D3b WAREHOUSING", so the label is correct on the letter. But read literally, "a supply/absorption premium" overstates what the balance sheet shows. The build sat in the 5Y bucket while dealer duration overall fell. BOND's rider ① travels with it: **a net-inventory build is NOT proof of auction warehousing.**

## 1. Leg-by-leg (first match wins, §3 order)

| Step | Test | Observation (source · pull) | Result |
|---|---|---|---|
| 1 CANNOT-EVALUATE | ACM 9/24 published? ΔACMY10 ≥ +10bp? | ACM 9/24 = 5.144094 / TP 0.729814; ΔACMY10 **+22.47bp** | **No** |
| 2 UNANSWERABLE | g = \|ΔACMTP10 − ΔTHREEFYTP10\| > 18bp? | ΔACMTP10 **+15.40bp** · ΔTHREEFYTP10 **+9.07bp** (0.9344 → 1.0251) ⇒ **g = 6.33bp** | **No** (35% of the bar) |
| 3 PREMIUM | s ≥ 0.50? | **s = 15.3976 / 22.4695 = 0.6853** | **YES** |
| D3 qualifier | D3a 3–6Y Δ ≥ +$8.6B = STRESS · D3b long-end Δ ≥ +$6.4B = WAREHOUSING, ≤ +$0.5B = NONE | D3a **+$12.093B** ⇒ STRESS · D3b **−$3.828B** ⇒ NONE | **-ABSORPTION** (D3a or D3b) |

## 2. Instruments and vintages (FROZEN-ON-REVISABLE, WQ-175)

| Leg | Source | Pull | Vintage check |
|---|---|---|---|
| ACM | NY Fed `ACMTermPremium.xls`, sheet "ACM Daily" | 2026-10-02 08:32 EDT · sha256 `f174cbddc004be85e10aa9ffb72b025f76cbfe7e1c0c8735533e031a963583ce` · frontier 9/30 | 9/22 and 9/24 cells **identical to six decimals** with the P1 pull (sha `437c0ab0…`, 9/28 20:38). No move >1bp ⇒ **no BY-VINTAGE branch** |
| KW | FRED `THREEFYTP10`, `THREEFY10` (fredgraph CSV) | 2026-10-02 08:32 EDT · frontier **9/25** | **First pull = the graded vintage.** (STATUS showed a 9/18 frontier on 9/30; NEXUS reported BOND reading KW to 9/25 on 10/1. Both are consistent.) |
| FR2004 | NY Fed Markets API `/api/pd/get/SBN2024/timeseries/<key>.json`; series break SBN2024 (2024-07-03 → open) resolved at runtime | 2026-10-02 08:32 EDT · latest as-of **2026-09-23** | PRE as-of 9/16 3–6Y = **$47.986B** reproduces BOND's registered PRE exactly ⇒ unrevised |

**KW cells:** 9/22 TP 0.9344 / Y 4.9645 · 9/23 0.9932 / 5.0807 · 9/24 1.0251 / 5.1470. KW share on its own fitted yield = 9.07 / 18.25 = **0.497** (information only; §3 keeps KW out of the deciding share because it is pinned at 0.44–0.56).

**FR2004 (US$ millions, primary dealers' net coupon positions, as-of Wednesday):**

| Bucket (key) | 9/09 | 9/16 | 9/23 | Δ 9/16→9/23 |
|---|---:|---:|---:|---:|
| **3–6Y** (`PDPOSGSC-G3L6`) — D3a | 51,819 | **47,986** | **60,079** | **+12,093** |
| 6–7Y (`G6L7`) — reported, not graded | 32,348 | 27,845 | 23,199 | −4,646 |
| 7–11Y (`G7L11`) | 36,016 | 35,127 | 34,245 | −882 |
| 11–21Y (`G11L21`) | 66,778 | 68,456 | 68,486 | +30 |
| >21Y (`G21`) | 43,399 | 40,790 | 37,814 | −2,976 |
| **Long-end TOTAL (7Y+) — D3b** | 146,193 | **144,373** | **140,545** | **−3,828** |

HENRY's own pull agrees with BOND's grade (`96ccc7a0c`, `KB-BND-383`) on every figure used: 3–6Y $60.079B vs PRE $47.986B, long-end −$3.8B, 6–7Y −$4.6B. **Same publisher, same API: an independent re-read of the arithmetic, not an independent source.**

## 3. A1 reporting rule (accepted 9/25) — how unusual is it?

s is unchanged from P1 (the vintage did not move), so the P1 percentiles stand: **45th pct** of ACM's own class (2-session ΔACMY10 ≥ +15bp, 1990→9/23, n=376) · 30th (2010+, n=131, BOND's cut) · 41st (2022+, n=61). BOND's relative reading (PATH ≤ 0.47 · PREMIUM ≥ 0.87): **0.685 is neither extreme.**
⇒ **PREMIUM is ACM's ordinary answer on a big up-move (73% of the class), and this is a slightly-below-typical premium share.** It carries little news against the class. It does carry news against HENRY's stated preference (A) for the burst.

## 4. Partial grades beside the verdict

| Grade | When | Result |
|---|---|---|
| **P1 — ACM** | 9/28 20:38 EDT (4 days late; HENRY dark) | PROVISIONAL PREMIUM, s 0.685, KW-UNCHECKED |
| **P2 — KW** | 10/2 08:32 EDT (KW posted to 9/25; first HENRY read) | g = **6.33bp ≤ 18** ⇒ not UNANSWERABLE. KW-CHECKED. KW's own share 0.497 |
| **FINAL — FR2004** | 10/2 08:32 EDT (published 10/1 between 16:13 and 16:15 ET per BOND's poll log) | D3a STRESS · D3b NONE ⇒ **-ABSORPTION** |

**By day (ACM, information only):** 9/23 TP +6.96 of Y +15.18 (0.46; the failed-5Y day) · 9/24 TP **+8.44** vs Y +7.29 (all premium; ACM's expected-path component fell 1.15). KW agrees on the direction of both days: 9/23 TP +5.88 of +11.62 · 9/24 TP +3.19 of +6.63. ⚠️ **On 9/24 alone the two models diverge in kind.** ACM puts the whole day in premium (share 1.16) while KW puts about half there (0.48). The window g (6.3bp) is ordinary, but most of it comes from 9/24.

## 5. Consequences — §7 as frozen (nothing re-specced)

| Consumer | PREMIUM-ABSORPTION per §7 | Status |
|---|---|---|
| **HENRY** | My preferred (A), "policy-path / higher-for-longer 2027–28", is **WRONG for 9/23–9/24**. (A) holds for the FOMC week only. Axis-1 re-attributed (no longer provisional). The watch list leads with supply: **10/6–10/8 3Y/10Y/30Y auctions · 11/4 QRA · buyback ops.** No registered row moves | Applied this session (STATUS § THESIS) |
| **BOND** | §7 row: "D3b WAREHOUSING = FIRST of row 3's two-build trigger" — **D3b is NONE, so this clause does NOT apply** · "D3a STRESS → WQ-157 as the 5Y's own dealer evidence" — already consumed via WQ-291 (`96ccc7a0c`) · THESIS POV note: C-36's term-premium half re-opened for September · B2: PREMIUM-ABSORPTION = "the first evidence against" BOND's 9/23 "threshold fired, mechanism not shown failed" call | **BOND's to apply.** Packeted; co-sign PENDING |
| **NEXUS** | `GATE-NEXUS-T12S-DFII10` letter untouched (NEXUS CONCUR 10/1, invariant to verdict). Attribution: duration compensation ⇒ can reverse without the Fed | Packeted as consumer |
| **TERRY** | Nothing (informed only) | — |

⚠️ **Read the qualifier with its split.** The §7 BOND row was written assuming -ABSORPTION would usually arrive via D3b warehousing. It arrived via D3a alone, with D3b negative. Whether "first evidence against" B2's call still holds when dealer duration overall FELL is **BOND's judgment**, not this grade's. HENRY flags it and does not decide it.

## 6. What this grade does NOT do
- It changes no forecast, gate letter, threshold, score or position rail (§7 plain answer). $0.
- It does not grade BOND's September-4 kill (WQ-291). That is a separate letter on the same print, already graded MET by BOND, with the recommendation pending Will (WQ-357).
- It does not re-open the bands. A1 (s's percentile) is reported, not applied.

*Pull receipts: ACM sha above; KW + FR2004 pulled 08:32 EDT via `curl`/`urllib` (fredgraph CSV; markets.newyorkfed.org API). Computation in-session; figures copied from command output.*
