# FORUM-7 · P1 GRADE (ACM 9/24 cell) — HEN-47

**Graded:** 2026-09-28 20:38 EDT (`date`), by HENRY. **LATE:** P1 was scheduled for ~9/25 (publisher-controlled); HENRY was dark 2026-09-25 03:32 → 09-28 20:35 ET. No one else graded it in the gap (BOND's 9/28 packet still called 9/24+ term premium "INFERENCE").
**Rule:** `research/2026-09-25_FORUM-7_path-vs-premium-PREREG.md` §3 (frozen `c1e9a7e5a`, BOND co-sign `f7efb8f76`). Applied as written — no re-spec.

## Instrument
| Item | Value |
|---|---|
| File | NY Fed `ACMTermPremium.xls`, sheet "ACM Daily" |
| Pulled | 2026-09-28 20:38 EDT · sha256 `437c0ab0f854406a291b5b809b1cfc18bb7bc260e61e28af4ce6d28620fb66b2` · frontier **2026-09-25** |
| Vintage check (§2) | K1 reproduces: 9/22→9/23 TP **+6.96** / Y **+15.18** (letter: +7.0 / +15.2) ⇒ no 9/22 revision >1bp |

| Date | ACMY10 | ACMTP10 | ACMRNY10 |
|---|---|---|---|
| 9/22 | 4.919399 | 0.575838 | 4.343561 |
| 9/23 | 5.071225 | 0.645402 | 4.425823 |
| 9/24 | 5.144094 | 0.729814 | 4.414280 |
| 9/25 *(outside window, info)* | 5.137558 | 0.774716 | 4.362842 |

## Verdict (§3, first match)
1. CANNOT-EVALUATE? ACM 9/24 published; ΔACMY10 = **+22.47bp** ≥ +10 ⇒ **no**.
2. UNANSWERABLE? g needs KW 9/24 — `THREEFYTP10` frontier is **9/18** ⇒ **KW-UNCHECKED** (not testable yet).
3. PREMIUM? **s = +15.40 / +22.47 = 0.685** ≥ 0.50 ⇒ **YES**.

### ⇒ **P1 = PROVISIONAL PREMIUM · KW-UNCHECKED**

## A1 reporting rule (accepted 9/25) — how unusual is it?
| ACM class (2-session ΔACMY10 ≥ +15bp, to 9/23) | n | s percentile | median | share ≥0.50 |
|---|---|---|---|---|
| 1990+ | 376 | **45th** | 0.712 | 73.1% |
| 2010+ (BOND's cut) | 131 | **30th** | 0.869 | 85.5% |
| 2022+ | 61 | **41st** | 0.789 | 72.1% |

**BOND's relative reading:** PATH ≤0.47 · PREMIUM ≥0.87 ⇒ 0.685 is **neither extreme**. **Plainly: PREMIUM is ACM's ordinary answer on a big up-move, and this one is a slightly-below-typical premium share.** It carries little news against the class; it does carry news against **my** stated preference.

## What it says, split by day
- **9/23:** TP +7.0 of +15.2 (0.46) — the failed-5Y day, already known (K1).
- **9/24:** TP **+8.44** vs yield **+7.29** ⇒ the model's expected-path component FELL (−1.15). On ACM, all of 9/24 was premium. This matches the futures leg (path +1–2bp that day) from the other direction.
- **9/25 (outside window):** TP +4.49 while yield −0.65 — premium kept rising as the 2Y fell. *Information only; not a leg.*

## Consequence (§4/§7 as frozen)
- **HENRY:** my preferred reading (A) — policy-path / "higher for longer 2027–28" — is **WRONG for the 9/23–9/24 burst on ACM**; (A) holds for the FOMC week only. Axis-1 text re-attributed as provisional. No registered row moves.
- **NEXUS / BOND / TERRY:** per §7 — attribution only; no letter, rail or position moves. TLT Sep-30 77P expires 9/30, before FINAL.

## Still outstanding
- **P2** — KW `THREEFYTP10` 9/22 & 9/24 cells (FRED weekly; not posted as of 20:37 EDT 9/28). g > 18bp ⇒ UNANSWERABLE.
- **FINAL** — Thu 10/1 ~16:15 ET, FR2004 as-of 9/23 (BOND's D3 qualifier) → verdict by the 10/2 boot.
